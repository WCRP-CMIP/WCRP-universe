"""
Generate experiment entries

Not actually all experiments,
rather just those listed in
[Dunne et al., 2025](https://doi.org/10.5194/gmd-18-6671-2025)
for the CMIP7 fast-track.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict


class ExperimentUniverse(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    drs_name: str
    description: str
    activity: str
    additional_allowed_model_components: list[str]
    branch_information: str | None
    end_timestamp: datetime | None
    min_ensemble_size: int
    min_number_yrs_per_sim: float | None
    parent_activity: str | None
    parent_experiment: str | None
    parent_mip_era: str | None
    required_model_components: list[str]
    start_timestamp: datetime | None
    tier: int


class ExperimentProject(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    id: str
    activity: str
    min_number_yrs_per_sim: int | None = "dont_write"
    parent_mip_era: str | None = "dont_write"
    tier: int

    def write_file(self, project_root: Path) -> None:
        content = {
            "@context": "000_context.jsonld",
            "id": self.id,
            "type": "experiment",
            "tier": self.tier,
        }

        for attr in ("min_number_yrs_per_sim", "parent_mip_era"):
            val = getattr(self, attr)
            if val != "dont_write":
                content[attr] = val

        out_file = str(project_root / f"experiment/{self.id}.json")
        write_file(out_file, content)


class ActivityProject(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    id: str
    experiments: list[str]
    urls: list[str]


class Holder(BaseModel):
    """
    God class :)
    """

    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    experiments_project: list[ExperimentProject]
    experiments_universe: list[ExperimentUniverse]
    activities: list[ActivityProject]

    def initialise_activities(self) -> "Holder":
        self.activities = [
            ActivityProject(
                id="cmip",
                experiments=[],
                urls=["https://doi.org/10.5194/gmd-18-6671-2025"],
            ),
            ActivityProject(
                id="scenariomip",
                experiments=[],
                urls=["https://doi.org/10.5194/egusphere-2024-3765"],
            ),
        ]

    def add_experiment_to_activity(self, experiment: ExperimentProject) -> "Holder":
        for activity_idx, activity in enumerate(self.activities):
            if activity.id == experiment.activity:
                break

        else:
            msg = f"No activity {experiment.activity} found. {self.activities=}"
            raise AssertionError(msg)

        if experiment.id not in self.activities[activity_idx]:
            self.activities[activity_idx].experiments.append(experiment.id)

        return self

    def add_1pctco2_entries(self) -> "Holder":
        univ = ExperimentUniverse(
            drs_name="1pctCO2",
            description=(
                "1% per year increase in atmospheric carbon dioxide levels. "
                "All other conditions are kept the same as piControl."
            ),
            activity="cmip",
            additional_allowed_model_components=["aer", "chem", "bgc"],
            branch_information="Branch from piControl at a time of your choosing",
            end_timestamp=None,
            min_ensemble_size=1,
            # Defined in project
            min_number_yrs_per_sim=None,
            parent_activity="cmip",
            parent_experiment="picontrol",
            # Defined in project
            parent_mip_era=None,
            required_model_components=["aogcm"],
            start_timestamp=None,
            tier=1,
        )

        self.experiments_universe.append(univ)

        proj = ExperimentProject(
            id=univ.drs_name.lower(),
            activity=univ.activity,
            min_number_yrs_per_sim=150,
            parent_mip_era="cmip7",
            tier=1,
        )
        self.experiments_project.append(proj)

        self.add_experiment_to_activity(proj)

        return self

    def write_files(self, project_root: Path) -> None:
        for experiment_project in self.experiments_project:
            experiment_project.write_file(project_root)


def write_file(out_file: str, content: dict[str, Any]) -> None:
    assert False, "TODO: sort into order I like"
    with open(out_file, "w") as fh:
        json.dump(content, fh, indent=4)

    print(f"Wrote {out_file}")


def get_tier(experiment: str) -> int:
    # TODO: confirm this
    return 0


def main():
    REPO_ROOT = Path(__file__).parents[1]
    project_root = REPO_ROOT / ".." / "CMIP7-CVs"

    holder = Holder(experiments_project=[], experiments_universe=[], activities=[])

    holder.initialise_activities()

    holder.add_1pctco2_entries()
    # Generate entries as objects
    # Write out project experiment entries
    # Write out universe experiment entries
    # Write out project activity entries

    holder.write_files(project_root=project_root)
    assert False
    bases = ["vl", "ln", "l", "ml", "m", "hl", "h"]

    experiment_list = []
    for base in bases:
        for prefix in [
            "scen7-",
            "esm-scen7-",
        ]:
            for suffix in [
                "",
                "-ext",
            ]:
                experiment_name = f"{prefix}{base}{suffix}"

                id = experiment_name.lower()

                content = {
                    "@context": "000_context.jsonld",
                    "id": id,
                    "type": "experiment",
                    "drs_name": experiment_name,
                    "activity": "scenariomip",
                    "additional_allowed_model_components": ["aer", "chem", "bgc"],
                    "required_model_components": ["aogcm"],
                }

                out_file = f"experiment/{id}.json"
                with open(out_file, "w") as fh:
                    json.dump(content, fh, indent=4)

                print(f"Wrote {out_file}")
                experiment_list.append(id)

    experiment_list = sorted(experiment_list)
    out_file = "activity/scenariomip.json"
    content = {
        "@context": "000_context.jsonld",
        "id": "scenariomip",
        "type": "activity",
        "description": "Future scenario experiments. Exploration of the future climate under a (selected) range of possible boundary conditions",
        "drs_name": "ScenarioMIP",
        "experiments": experiment_list,
        "urls": ["https://doi.org/10.5194/egusphere-2024-3765"],
    }
    with open(out_file, "w") as fh:
        json.dump(content, fh, indent=4)

    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
