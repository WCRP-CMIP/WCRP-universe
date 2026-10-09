"""
Generate CMIP7 experiment entries

Not actually all experiments,
rather just those listed in
[Dunne et al., 2025](https://doi.org/10.5194/gmd-18-6671-2025)
for the CMIP7 fast-track
(plus a few extras that have been requested since).

Each experiment is made up of:

- a `UniverseExperiment`: the fields written to `experiment/` in this repository
- a `CMIP7Experiment`: the fields written to `experiment/` in the CMIP7-CVs repository

Fields set to `NOT_WRITTEN` are left out of the written file
(unlike `None`, which is written as `null`).

The activities (written to the CMIP7-CVs repository)
and their references (written to this repository)
are written at the end,
with each activity's experiments derived from the experiments' `activity` field.
"""

import copy
import dataclasses
import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).parents[1]
UNIVERSE_ROOT = REPO_ROOT
PROJECT_ROOT = REPO_ROOT / ".." / "CMIP7-CVs"


class NotWritten(Enum):
    """Type of the sentinel for fields that should not be written"""

    NOT_WRITTEN = "NOT_WRITTEN"


NOT_WRITTEN = NotWritten.NOT_WRITTEN


@dataclass(frozen=True, kw_only=True)
class UniverseExperiment:
    """
    Experiment fields written to the universe

    Optional fields default to `NOT_WRITTEN`.
    These are generally fields that are defined in the CMIP7 CVs instead.
    """

    drs_name: str
    description: str
    activity: str
    required_model_components: list[str]
    additional_allowed_model_components: list[str]
    min_ensemble_size: int
    tier: int
    branch_information: str | None | NotWritten = NOT_WRITTEN
    parent_activity: str | None | NotWritten = NOT_WRITTEN
    parent_experiment: str | None | NotWritten = NOT_WRITTEN
    parent_mip_era: str | None | NotWritten = NOT_WRITTEN
    start_timestamp: str | None | NotWritten = NOT_WRITTEN
    end_timestamp: str | None | NotWritten = NOT_WRITTEN
    min_number_yrs_per_sim: float | None | NotWritten = NOT_WRITTEN


@dataclass(frozen=True, kw_only=True)
class CMIP7Experiment:
    """
    Experiment fields written to the CMIP7 CVs

    Optional fields default to `NOT_WRITTEN`.
    These are generally fields that are already defined in the universe.
    """

    tier: int
    description: str | NotWritten = NOT_WRITTEN
    branch_information: str | None | NotWritten = NOT_WRITTEN
    parent_activity: str | None | NotWritten = NOT_WRITTEN
    parent_experiment: str | None | NotWritten = NOT_WRITTEN
    parent_mip_era: str | None | NotWritten = NOT_WRITTEN
    start_timestamp: str | None | NotWritten = NOT_WRITTEN
    end_timestamp: str | None | NotWritten = NOT_WRITTEN
    min_number_yrs_per_sim: float | None | NotWritten = NOT_WRITTEN
    min_ensemble_size: int | NotWritten = NOT_WRITTEN


@dataclass(frozen=True)
class Experiment:
    universe: UniverseExperiment
    cmip7: CMIP7Experiment


@dataclass(frozen=True, kw_only=True)
class Activity:
    """Activity, written to the CMIP7 CVs"""

    id: str
    references: list[str]
    """DOIs (or URLs if there is no DOI) of the activity's references"""

    description: str | NotWritten = NOT_WRITTEN


@dataclass(frozen=True, kw_only=True)
class Reference:
    """Reference, written to the universe"""

    id: str
    citation: str
    doi: str


ACTIVITIES: dict[str, Activity] = {
    activity.id: activity
    for activity in (
        Activity(
            id="aerchemmip",
            references=[
                "https://doi.org/10.5194/gmd-10-585-2017",
            ],
        ),
        Activity(
            id="c4mip",
            references=[
                "https://doi.org/10.5194/gmd-17-8141-2024",
                "https://doi.org/10.5194/gmd-18-5699-2025",
                "https://doi.org/10.5194/gmd-9-2853-2016",
            ],
        ),
        Activity(
            id="cfmip",
            references=[
                # "https://doi.org/10.5194/gmd-10-359-2017",
                "https://doi.org/10.5194/gmd-19-8693-2026",
                "https://doi.org/10.1029/2023GL104786",
            ],
        ),
        Activity(
            id="cmip",
            references=["https://doi.org/10.5194/gmd-18-6671-2025"],
            description=(
                # If you were doing this for CMIP6, you would write DECK and historical
                # as historical was separate from the DECK in CMIP6, but isn't in CMIP7,
                # see https://github.com/WCRP-CMIP/CMIP7-CVs/issues/327
                "CMIP core common experiments "
                "i.e. the DECK (Diagnostic, Evaluation and Characterization of Klima)."
            ),
        ),
        Activity(
            id="damip",
            references=["https://doi.org/10.5194/gmd-18-4399-2025"],
        ),
        Activity(
            id="dcpp",
            references=[
                "https://doi.org/10.5194/gmd-9-3751-2016",
            ],
        ),
        Activity(
            id="geomip",
            references=[
                "https://doi.org/10.5194/gmd-17-2583-2024",
                "https://doi.org/10.1175/BAMS-D-25-0191.1",
            ],
        ),
        Activity(
            id="lmip",
            references=["https://doi.org/10.5194/gmd-9-2809-2016"],
        ),
        Activity(
            id="pmip",
            references=[
                "https://doi.org/10.5194/gmd-10-3979-2017",
                "https://doi.org/10.5194/cp-19-883-2023",
            ],
        ),
        Activity(
            id="rfmip",
            references=[
                "https://doi.org/10.5194/gmd-9-3447-2016",
                "https://doi.org/10.5194/acp-20-9591-2020",
                "https://doi.org/10.5194/gmd-19-4447-2026",
            ],
        ),
        Activity(
            id="polmip",
            references=[
                "https://doi.org/10.1038/s41467-025-62983-5",
                "https://doi.org/10.1016/j.eng.2024.11.023",
                "https://doi.org/10.1016/j.accre.2023.11.004",
                "https://dx.doi.org/10.1088/1748-9326/adfbfb",
                "https://doi.org/10.5281/zenodo.21487424",
            ],
            description=(
                "Policy-Aligned Model Intercomparison Project (PolMIP). "
                "PolMIP is designed as a complementary effort to existing MIPs. "
                "While ScenarioMIP explores the breadth of future forcing levels under idealized assumptions, "
                "PolMIP focuses on the depth of policy-driven pathways, "
                "offering higher fidelity for regions where specific mitigation strategies and timelines are defined. "
                "By providing a coordinated infrastructure for policy-driven scenario simulations, "
                "PolMIP aims to deliver actionable science for national climate assessments, "
                "enhance the policy relevance of CMIP, "
                "and foster closer collaboration between the climate modeling community and policymakers. "
                "Ultimately, PolMIP seeks to ensure that the next generation of climate projections is not only scientifically robust "
                "but also deeply rooted in the real-world decisions shaping our collective future. "
                "The project has completed phase 1: demonstration and proof of concept, "
                "starting from the SSP2-com scenario that was developed by Chinese scientists "
                "that aligns with China's carbon neutrality pledge "
                "(peaking carbon emissions before 2030 and achieving carbon neutrality before 2060) "
                "within the SSP2 socioeconomic framework and the NDC data of countries worldwide. "
                "The next phase will expand the framework to include policy-aligned scenarios from other nations and regions, "
                "creating a multi-country ensemble "
                "that enables consistent cross-comparison of national climate action strategies under a unified protocol."
            ),
        ),
        Activity(
            id="scenariomip",
            references=["https://doi.org/10.5194/egusphere-2024-3765"],
            description=(
                "Future scenario experiments. "
                "Exploration of the future climate under a (selected) range of possible boundary conditions. "
                "In CMIP7, the priority tier for experiments is conditional on whether you are doing emissions- or concentration-driven simulations. "
                "There is no way to express this in the CVs (nor time to implement something to handle this conditionality). "
                "This means that, for your particular situation, some experiments may be at a lower tier than is listed in the CVs. "
                "For example, the `vl` scenario is tier 1 for concentration-driven models "
                "and tier 2 for emissions-driven models. "
                "However, in the CVs, we have used the highest priority tier (across all the possible conditionalities). "
                "Hence `vl` is listed as tier 1 in the CVs (even though it is actually tier 2 for emissions-driven models). "
                "For details, please see the full description in the ScenarioMIP description papers."
            ),
        ),
        Activity(
            id="firemip",
            references=[
                "https://gmd.copernicus.org/articles/19/3989/2026/",
            ],
            description=(
                "Fire Model Intercomparison Project. "
                "In CMIP7, FireMIP expands into the fully coupled Earth system modeling framework to: "
                "(1) evaluate fire simulations in state-of-the-art fully coupled Earth system models (ESMs); "
                "(2) assess fire regime changes in the past, present, and future, "
                "and identify their primary natural and anthropogenic forcings "
                "and causal pathways within the Earth system, including the associated uncertainties; "
                "and (3) quantify the impacts of fires and fire changes on climate, ecosystems, "
                "and society across Earth system components, regions, and timescales, "
                "and elucidate the underlying mechanisms. "
                "FireMIP in CMIP7 will advance fire and fire-related modeling in fully coupled ESMs, "
                "and provide a quantitative, comprehensive, "
                "and process-based understanding of fire's role in the Earth system "
                "by using models that incorporate critical climate feedbacks "
                "and CMIP7 multi-model, multi-initial-condition, and multi-scenario ensembles."
            ),
        ),
    )
}

EXPERIMENTS: dict[str, Experiment] = {}

# Commonly used model component combinations
AOGCM = dict(
    required_model_components=["aogcm"],
    additional_allowed_model_components=["aer", "chem", "bgc"],
)
ESM = dict(
    required_model_components=["aogcm", "bgc"],
    additional_allowed_model_components=["aer", "chem"],
)
AGCM = dict(
    required_model_components=["agcm"],
    additional_allowed_model_components=["aer", "chem", "bgc"],
)
AGCM_CHEM = dict(
    required_model_components=["agcm", "chem"],
    additional_allowed_model_components=["aer", "bgc"],
)
AGCM_AER = dict(
    required_model_components=["agcm", "aer"],
    additional_allowed_model_components=["chem", "bgc"],
)

# Universe fields for experiments that branch from piControl
FROM_PICONTROL = dict(
    branch_information="Branch from `piControl` at a time of your choosing",
    parent_activity="cmip",
    parent_experiment="picontrol",
)


def add(universe: UniverseExperiment, cmip7: CMIP7Experiment) -> str:
    """Register an experiment, returning its id"""
    id = universe.drs_name.lower()
    if id in EXPERIMENTS:
        raise AssertionError(f"{id} is already registered")

    if universe.activity not in ACTIVITIES:
        raise AssertionError(f"Unknown activity for {id}: {universe.activity}")

    EXPERIMENTS[id] = Experiment(
        universe=copy.deepcopy(universe), cmip7=copy.deepcopy(cmip7)
    )

    return id


def get(id_or_drs_name: str) -> Experiment:
    """Get a registered experiment from its id or its DRS name"""
    # Ids are always the lowercase version of the DRS name
    id = id_or_drs_name.lower()
    try:
        return EXPERIMENTS[id]
    except KeyError:
        msg = f"{id} is not registered (yet?). Registered: {sorted(EXPERIMENTS)}"
        raise KeyError(msg)


def universe_copy(id_or_drs_name: str, **overrides: Any) -> UniverseExperiment:
    """Copy the universe fields of a registered experiment, overriding some of them"""
    return dataclasses.replace(copy.deepcopy(get(id_or_drs_name).universe), **overrides)


def pick(obj: Any, *fields: str) -> dict[str, Any]:
    """Grab some fields from a dataclass, e.g. a parent's universe fields"""
    return {k: getattr(obj, k) for k in fields}


def year(timestamp: str) -> int:
    return int(timestamp.split("-")[0])


# Scenario-style experiments (ScenarioMIP, PolMIP) duplicate their timing info
# in the project so that the info doesn't need to be looked up from the universe.
def scenario_cmip7(universe: UniverseExperiment) -> CMIP7Experiment:
    return CMIP7Experiment(
        **pick(
            universe,
            "start_timestamp",
            "end_timestamp",
            "min_number_yrs_per_sim",
            "tier",
        ),
        parent_mip_era="cmip7",
    )


def scenario_description(description_base: str, drs_name: str) -> str:
    return (
        f"{description_base} Run with prescribed carbon dioxide concentrations "
        f"(for prescribed carbon dioxide emissions, see `esm-{drs_name}`)."
    )


def scenario_esm(id_or_drs_name: str, tier: int = 1) -> UniverseExperiment:
    """Get the emissions-driven equivalent of a concentration-driven scenario"""
    base = get(id_or_drs_name).universe
    if base.parent_experiment != "historical":
        raise AssertionError(base.parent_experiment)

    concentration_driven_suffix = (
        "Run with prescribed carbon dioxide concentrations "
        f"(for prescribed carbon dioxide emissions, see `esm-{base.drs_name}`)."
    )
    if not base.description.endswith(concentration_driven_suffix):
        raise AssertionError(base.description)

    description = base.description.replace(
        concentration_driven_suffix,
        "Run with prescribed carbon dioxide emissions "
        f"(for prescribed carbon dioxide concentrations, see `{base.drs_name}`).",
    )

    return universe_copy(
        base.drs_name,
        drs_name=f"esm-{base.drs_name}",
        description=description,
        **ESM,
        parent_experiment="esm-hist",
        branch_information=base.branch_information.replace("historical", "esm-hist"),
        tier=tier,
    )


def scenario_extension(
    id_or_drs_name: str, min_number_yrs_per_sim: float = 50.0, tier: int = 1
) -> UniverseExperiment:
    """Get the extension of a scenario"""
    base = get(id_or_drs_name).universe
    end_year = year(base.end_timestamp)

    return universe_copy(
        base.drs_name,
        drs_name=f"{base.drs_name}-ext",
        description=f"Extension of `{base.drs_name}` beyond {end_year}.",
        # Unclear to me how this is meant to work.
        # scenario ends at 2100-12-31, extensions starts at 2101-01-01.
        # Is it an implied join rather than a true overlap
        # (like we have for piControl to historical)?
        branch_information=f"Branch from `{base.drs_name}` at {base.end_timestamp}",
        start_timestamp=f"{end_year + 1}-01-01",
        end_timestamp="2500-12-31",
        min_number_yrs_per_sim=min_number_yrs_per_sim,
        parent_activity=base.activity,
        parent_experiment=base.drs_name.lower(),
        tier=tier,
    )


def add_scenario(universe: UniverseExperiment) -> str:
    return add(universe, scenario_cmip7(universe))


def add_deck_and_friends() -> None:
    for (
        drs_name,
        description_start,
        activity,
        components,
    ) in (
        ("1pctCO2", "", "cmip", AOGCM),
        (
            "1pctCO2-bgc",
            (
                "Biogeochemically coupled simulation "
                "(i.e. the carbon cycle only 'sees' the increase in atmospheric carbon dioxide, "
                "not any change in temperature) of a "
            ),
            "c4mip",
            ESM,
        ),
        (
            "1pctCO2-rad",
            (
                "Radiatively coupled simulation "
                "(i.e. the carbon cycle only 'sees' the increase in temperature, "
                "not any change in atmospheric carbon dioxide) of a "
            ),
            "c4mip",
            ESM,
        ),
    ):
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=(
                    f"{description_start}"
                    "1% per year increase in atmospheric carbon dioxide levels. "
                    "All other conditions are kept the same as piControl."
                ),
                activity=activity,
                **components,
                **FROM_PICONTROL,
                start_timestamp=None,
                end_timestamp=None,
                min_ensemble_size=1,
                tier=1,
            ),
            CMIP7Experiment(
                min_number_yrs_per_sim=150.0, parent_mip_era="cmip7", tier=1
            ),
        )

    for drs_name, description_start, activity in (
        (
            "abrupt-4xCO2",
            "Abrupt quadrupling of atmospheric carbon dioxide levels.",
            "cmip",
        ),
        (
            "abrupt-2xCO2",
            "Abrupt doubling of atmospheric carbon dioxide levels.",
            "cfmip",
        ),
        (
            "abrupt-0p5xCO2",
            "Abrupt halving of atmospheric carbon dioxide levels.",
            "cfmip",
        ),
    ):
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=f"{description_start} All other conditions are kept the same as piControl.",
                activity=activity,
                **AOGCM,
                **FROM_PICONTROL,
                start_timestamp=None,
                end_timestamp=None,
                min_ensemble_size=1,
                tier=1,
            ),
            CMIP7Experiment(
                min_number_yrs_per_sim=300.0, parent_mip_era="cmip7", tier=1
            ),
        )

    amip_sst_p4k = (
        "sea surface temperatures are increased by 4K in ice-free regions "
        "(sea ice and SSTs in grid boxes containing sea ice remain the same as in the `amip` experiment)"
    )
    for drs_name, description, activity, start_timestamp, tier in (
        (
            "amip",
            "Simulation of the climate of the recent past with prescribed sea surface temperatures and sea ice concentrations.",
            "cmip",
            "1979-01-01",
            1,
        ),
        (
            "amip-p4K",
            f"Same as the `amip` simulation, except {amip_sst_p4k}.",
            "cfmip",
            "1979-01-01",
            1,
        ),
        (
            "amip-m4K",
            (
                "Same as the `amip` simulation, except "
                f"{amip_sst_p4k.replace('increased', 'decreased')}."
            ),
            "cfmip",
            "1979-01-01",
            1,
        ),
        (
            "amip-p4K-SST-rad",
            (
                f"Same as the `amip` simulation, except {amip_sst_p4k} "
                "when calculating the upward longwave radiation from the sea surface using the Planck function "
                "(see Ogura et al., 2023, https://doi.org/10.1029/2023GL104786)."
            ),
            "cfmip",
            "1979-01-01",
            2,
        ),
        (
            "amip-p4K-SST-turb",
            (
                f"Same as the `amip` simulation, except {amip_sst_p4k} "
                "when calculating the turbulent transport of the latent and sensible heat fluxes "
                "at the air-sea interface using bulk aerodynamic formulae "
                "(see Ogura et al., 2023, https://doi.org/10.1029/2023GL104786)."
            ),
            "cfmip",
            "1979-01-01",
            2,
        ),
        (
            "amip-piForcing",
            (
                "Same as `amip` simulation, except it starts in 1870 "
                "and all forcings are set to pre-industrial levels "
                "rather than time-varying forcings."
            ),
            "cfmip",
            "1870-01-01",
            1,
        ),
    ):
        end_timestamp = "2021-12-31"
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description,
                activity=activity,
                **AGCM,
                branch_information=None,
                parent_activity=None,
                parent_experiment=None,
                parent_mip_era=None,
                start_timestamp=None,
                end_timestamp=None,
                min_ensemble_size=1,
                tier=tier,
            ),
            CMIP7Experiment(
                start_timestamp=start_timestamp,
                end_timestamp=end_timestamp,
                min_number_yrs_per_sim=float(
                    year(end_timestamp) - year(start_timestamp) + 1
                ),
                # Not the same as the universe tier for some experiments
                tier=1,
            ),
        )

    add(
        UniverseExperiment(
            drs_name="dcppB-forecast-cmip6",
            description=(
                "Simulation to examine forced climate change and variability up to 10 years into the future. "
                "This forecast is initialised from observations with forcing from ssp245 applied over its extent."
            ),
            activity="dcpp",
            # "ism" not included
            **AOGCM,
            branch_information=None,
            parent_activity=None,
            parent_experiment=None,
            parent_mip_era=None,
            # Not perfect, but the best we can do right now.
            # See https://github.com/ESGF/esgf-vocab/issues/241
            start_timestamp=None,
            end_timestamp="2035-12-31",
            min_number_yrs_per_sim=10.0,
            min_ensemble_size=10,
            tier=1,
        ),
        CMIP7Experiment(tier=1),
    )

    for (
        drs_name,
        description,
        min_number_yrs_per_sim,
        tier,
        parent_experiment,
        branch_information,
    ) in (
        (
            "piControl",
            (
                "Pre-industrial control simulation "
                "with prescribed carbon dioxide concentrations "
                "(for prescribed carbon dioxide emissions, see `esm-piControl`). "
                "Used to characterise natural variability and unforced behaviour."
            ),
            400.0,
            1,
            "picontrol-spinup",
            "Branch from `piControl-spinup` at a time of your choosing",
        ),
        (
            "piControl-spinup",
            (
                "Spin-up simulation. "
                "Used to get the model into a state of approximate radiative equilibrium "
                "before starting the `piControl` simulation."
            ),
            None,
            3,
            None,
            None,
        ),
        (
            "esm-piControl",
            (
                "Pre-industrial control simulation "
                "with prescribed carbon dioxide emissions "
                "(for prescribed carbon dioxide concentrations, see `piControl`). "
                "Used to characterise natural variability and unforced behaviour."
            ),
            400.0,
            1,
            "esm-picontrol-spinup",
            "Branch from `esm-piControl-spinup` at a time of your choosing",
        ),
        (
            "esm-piControl-spinup",
            (
                "Spin-up simulation. "
                "Used to get the model into a state of approximate radiative equilibrium "
                "before starting the `esm-piControl` simulation."
            ),
            None,
            3,
            None,
            None,
        ),
    ):
        has_parent = parent_experiment is not None
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description,
                activity="cmip",
                **(ESM if drs_name.startswith("esm-") else AOGCM),
                branch_information=branch_information,
                parent_activity="cmip" if has_parent else None,
                parent_experiment=parent_experiment,
                # If there is a parent, its MIP era is defined in project
                parent_mip_era=NOT_WRITTEN if has_parent else None,
                start_timestamp=None,
                end_timestamp=None,
                min_ensemble_size=1,
                tier=1,
            ),
            CMIP7Experiment(
                min_number_yrs_per_sim=min_number_yrs_per_sim,
                parent_mip_era="cmip7" if has_parent else NOT_WRITTEN,
                tier=tier,
            ),
        )

    for drs_name, description, parent_experiment, branch_information in (
        (
            "historical",
            (
                "Simulation of the climate of the recent past "
                "(typically meaning 1850 to present-day) "
                "with prescribed carbon dioxide concentrations "
                "(for prescribed carbon dioxide emissions, see `esm-hist`)."
            ),
            "picontrol",
            "Branch from `piControl` at a time of your choosing",
        ),
        (
            "esm-hist",
            (
                "Simulation of the climate of the recent past "
                "(typically meaning 1850 to present-day) "
                "with prescribed carbon dioxide emissions "
                "(for prescribed carbon dioxide concentrations, see `historical`)."
            ),
            "esm-picontrol",
            "Branch from esm-piControl at a time of your choosing",
        ),
    ):
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description,
                activity="cmip",
                **(ESM if drs_name.startswith("esm-") else AOGCM),
                branch_information=branch_information,
                parent_activity="cmip",
                parent_experiment=parent_experiment,
                start_timestamp="1850-01-01",
                min_ensemble_size=1,
                tier=1,
            ),
            CMIP7Experiment(
                start_timestamp="1850-01-01",
                end_timestamp="2021-12-31",
                min_number_yrs_per_sim=172.0,
                parent_mip_era="cmip7",
                tier=1,
            ),
        )


def add_flat10() -> None:
    flat10_id = add(
        UniverseExperiment(
            drs_name="esm-flat10",
            description="10 PgC / yr constant carbon dioxide emissions.",
            activity="c4mip",
            **ESM,
            branch_information="Branch from `esm-piControl` at a time of your choosing",
            parent_activity="cmip",
            parent_experiment="esm-picontrol",
            start_timestamp=None,
            end_timestamp=None,
            min_number_yrs_per_sim=100.0,
            min_ensemble_size=1,
            tier=1,
        ),
        CMIP7Experiment(parent_mip_era="cmip7", tier=1),
    )

    for drs_name, description, min_number_yrs_per_sim in (
        (
            "esm-flat10-cdr",
            (
                "Extension of `esm-flat10` where emissions decline linearly to -10 PgC / yr "
                "then stay constant until cumulative emissions "
                "(including the emissions in `esm-flat10`) reach zero. "
                "An extra 20 years is included at the end to allow for calculating averages over different time windows."
            ),
            220.0,
        ),
        (
            "esm-flat10-zec",
            "Extension of `esm-flat10` with zero emissions.",
            100.0,
        ),
    ):
        add(
            universe_copy(
                flat10_id,
                drs_name=drs_name,
                description=description,
                branch_information="Branch from `esm-flat10` at the end of year 100.",
                min_number_yrs_per_sim=min_number_yrs_per_sim,
                parent_activity=get(flat10_id).universe.activity,
                parent_experiment=flat10_id,
            ),
            get(flat10_id).cmip7,
        )


def add_damip() -> None:
    description_template = (
        "Response to historical {forcing} forcing "
        "({extension}). "
        "All other conditions are kept the same as piControl."
    )
    for drs_name, forcing in (
        ("hist-aer", "aerosol"),
        ("hist-GHG", "greenhouse gas"),
        ("hist-nat", "natural"),
    ):
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description_template.format(
                    forcing=forcing,
                    extension="often with extension using forcings from a scenario simulation specific to the CMIP phase",
                ),
                activity="damip",
                **AOGCM,
                **FROM_PICONTROL,
                start_timestamp="1850-01-01",
                min_ensemble_size=1,
                tier=1,
            ),
            CMIP7Experiment(
                description=description_template.format(
                    forcing=forcing,
                    extension="with extension using forcings from the `m` scenario simulation",
                ),
                start_timestamp="1850-01-01",
                end_timestamp="2035-12-31",
                min_number_yrs_per_sim=186.0,
                min_ensemble_size=3,
                parent_mip_era="cmip7",
                tier=1,
            ),
        )


def add_lmip() -> None:
    start_timestamp = "1901-01-01"
    end_timestamp = get("historical").cmip7.end_timestamp
    add(
        UniverseExperiment(
            drs_name="land-hist",
            description="Land-only version of `historical` with prescribed climate and weather inputs required to drive land models.",
            activity="lmip",
            required_model_components=["land"],
            additional_allowed_model_components=[],
            branch_information=None,
            parent_activity=None,
            parent_experiment=None,
            parent_mip_era=None,
            min_ensemble_size=1,
            tier=1,
        ),
        CMIP7Experiment(
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            min_number_yrs_per_sim=float(
                year(end_timestamp) - year(start_timestamp) + 1
            ),
            tier=1,
        ),
    )


def add_pmip() -> None:
    add(
        UniverseExperiment(
            drs_name="abrupt-127k",
            description=(
                "Simulation to examine the response to orbital and greenhouse gas concentration changes "
                "associated with the last interglacial (127 000 years before present)."
            ),
            activity="pmip",
            **AOGCM,
            **FROM_PICONTROL,
            start_timestamp=None,
            end_timestamp=None,
            min_number_yrs_per_sim=100.0,
            min_ensemble_size=1,
            tier=1,
        ),
        CMIP7Experiment(min_number_yrs_per_sim=100.0, parent_mip_era="cmip7", tier=1),
    )


def add_piclim() -> None:
    def present_day_description(quantifies: str, forcing_diff: str) -> str:
        return (
            "In combination with `piClim-control`, "
            f"quantifies present-day {quantifies} effective radiative forcing (ERF). "
            f"Same as `piClim-control`, except {forcing_diff} use present-day values "
            "(typically the last year of the `historical` simulation within the same CMIP era "
            "e.g. 2014 values for CMIP6, 2021 values for CMIP7)."
        )

    def co2_description(quantifies: str, factor: str) -> str:
        return (
            "In combination with `piClim-control`, "
            f"quantifies {quantifies} effective radiative forcing (ERF). "
            "Same as `piClim-control`, "
            "except atmospheric carbon dioxide concentrations "
            f"are set to {factor} `piControl` levels."
        )

    def co2_single_component_description(component: str, other: str) -> str:
        return (
            # What this is for?
            "Same as `piClim-control`, "
            "except atmospheric carbon dioxide concentrations "
            "are set to four times `piControl` levels, "
            f"but only for the {component} component of the model. "
            f"For any other model component that directly uses CO2 concentration, including {other}, "
            "the CO2 concentration should be set to the value used in `piClim-control`."
        )

    hist_end_year = year(get("historical").cmip7.end_timestamp)
    for drs_name, description, activity, components, tier in (
        (
            "piClim-control",
            (
                "Baseline for effective radiative forcing (ERF) calculations. "
                "`piControl` with prescribed sea-surface temperatures "
                "and sea-ice concentrations from a climatology of "
                "the model's `piControl` simulation."
            ),
            "cmip",
            AGCM,
            1,
        ),
        (
            "piClim-anthro",
            present_day_description(
                "total anthropogenic",
                "all anthropogenic forcings",
            ),
            "cmip",
            AGCM,
            1,
        ),
        (
            "piClim-ghg",
            present_day_description(
                "total well-mixed (non-ozone) greenhouse gas",
                "well-mixed (non-ozone) greenhouse gas concentrations",
            ),
            "rfmip",
            AGCM,
            1,
        ),
        (
            "piClim-4xCO2",
            co2_description(
                "a quadrupling of atmospheric carbon dioxide's (4xCO2's)", "four times"
            ),
            "cmip",
            AGCM,
            1,
        ),
        (
            "piClim-4xCO2-bgc",
            co2_single_component_description("biogeochemical", "radiation"),
            "rfmip",
            AGCM,
            3,
        ),
        (
            "piClim-4xCO2-rad",
            co2_single_component_description(
                "radiation", "the biogeochemical component"
            ),
            "rfmip",
            AGCM,
            3,
        ),
        (
            "piClim-2xCO2",
            co2_description(
                "a doubling of atmospheric carbon dioxide's (2xCO2's)", "two times"
            ),
            "rfmip",
            AGCM,
            3,
        ),
        (
            "piClim-0p5xCO2",
            co2_description(
                "a halving of atmospheric carbon dioxide's (0.5xCO2's)", "half of"
            ),
            "rfmip",
            AGCM,
            3,
        ),
        (
            "piClim-CH4",
            present_day_description(
                "methane",
                "methane concentrations or emissions (as appropriate for the model)",
            ),
            "aerchemmip",
            AGCM_CHEM,
            1,
        ),
        (
            "piClim-N2O",
            present_day_description(
                "nitrous oxide",
                "nitrous oxide concentrations or emissions (as appropriate for the model)",
            ),
            "aerchemmip",
            AGCM_CHEM,
            1,
        ),
        (
            "piClim-NOx",
            present_day_description(
                "nitrous oxide (NOx)",
                "nitrous oxide (NOx) emissions",
            ),
            "aerchemmip",
            AGCM_CHEM,
            1,
        ),
        (
            "piClim-ODS",
            present_day_description(
                "ozone-depleting substances",
                "ozone-depleting substances concentrations",
            ),
            "aerchemmip",
            AGCM_CHEM,
            1,
        ),
        (
            "piClim-SO2",
            present_day_description(
                "sulfur (dioxide)",
                "sulfur emissions",
            ),
            "aerchemmip",
            AGCM_AER,
            1,
        ),
        (
            "piClim-aer",
            present_day_description(
                "aerosol",
                "anthropogenic aerosol emissions",
            ),
            "rfmip",
            AGCM_AER,
            1,
        ),
        (
            "piClim-lu",
            present_day_description(
                "land-use change",
                "land states",
            ),
            "rfmip",
            AGCM_AER,
            1,
        ),
        (
            "piClim-p4K",
            (
                "Baseline for effective radiative forcing (ERF) calculations "
                "with a warmer background state. "
                "Same as `piClim-control`, "
                "except sea surface temperatures are increased by 4K in ice-free regions "
                "(sea ice and SSTs in grid boxes containing sea ice remain the same as in the `piClim-control` experiment)."
            ),
            "aerchemmip",
            AGCM,
            1,
        ),
        (
            "piClim-p4K-4xCO2",
            (
                "In combination with `piClim-p4K`, `piClim-control` and `piClim-4xCO2`, "
                "this experiment can be used to evaluate the sensitivity of 4xCO2 radiative forcing "
                "to a warmer background state. "
                "Same as `piClim-p4K`, "
                "except atmospheric carbon dioxide concentrations "
                "are set to four times `piControl` levels."
            ),
            "rfmip",
            AGCM,
            3,
        ),
        (
            "piClim-p4K-aer",
            (
                "In combination with `piClim-p4K`, `piClim-control` and `piClim-aer`, "
                "this experiment can be used to evaluate the sensitivity of aerosol radiative forcing "
                "to a warmer background state. "
                "Same as `piClim-control`, except anthropogenic aerosol emissions use present-day values "
                "(typically the last year of the `historical` simulation within the same CMIP era "
                "e.g. 2014 values for CMIP6, 2021 values for CMIP7)."
            ),
            "rfmip",
            AGCM,
            3,
        ),
    ):
        if drs_name == "piClim-control":
            branch_information = (
                "Branch from `piControl` at a time of your choosing. "
                "Given that you are using a climatology from your own model as boundary conditions, "
                "we recommended branching from the mid-point of the period over which you calculated the climatology "
                "(but this recommendation may not be appropriate for all models, "
                "so ultimately it is up to you to decide what introduces the smallest 'shock'/'jump' at the branch time)."
            )
        else:
            branch_information = "Same as `piClim-control`"

        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description,
                activity=activity,
                **components,
                start_timestamp=None,
                end_timestamp=None,
                min_number_yrs_per_sim=30.0,
                min_ensemble_size=1,
                tier=tier,
            ),
            CMIP7Experiment(
                description=re.sub(
                    r"\(typically.*\)",
                    f"({hist_end_year} values for CMIP7)",
                    description,
                ),
                branch_information=branch_information,
                # https://github.com/WCRP-CMIP/CMIP7-CVs/issues/382
                min_ensemble_size=1,
                parent_activity="cmip",
                parent_experiment="picontrol",
                parent_mip_era="cmip7",
                tier=tier,
            ),
        )

    for drs_name, description, future_experiment_cmip7, tier in (
        (
            "piClim-histaer",
            (
                "In combination with `piClim-control`, "
                "quantifies transient aerosol effective radiative forcing (ERF) "
                "over the historical period and a future experiment. "
                "This can be compared with `piClim-aer` which provides a more precise "
                "quantification of present-day aerosol ERF."
            ),
            "the `scen7-m` or `esm-scen7-m` experiment (whichever is relevant to your model setup)",
            1,
        ),
        (
            "piClim-histall",
            (
                "In combination with `piClim-control`, "
                "quantifies transient effective radiative forcing (ERF) "
                "over the historical period and a future experiment. "
                "This complements the `piClim-*` experiments which provide a more precise "
                "quantification of present-day ERF for various forcing components."
            ),
            "the `scen7-m` or `esm-scen7-m` experiment (whichever is relevant to your model setup)",
            1,
        ),
        (
            "piClim-histghg",
            (
                "In combination with `piClim-control`, "
                "quantifies transient well-mixed (non-ozone) greenhouse gas effective radiative forcing (ERF) "
                "due to changes in concentrations of these gases (not emissions) "
                "over the historical period and a future experiment. "
                "This complements the `piClim-*` experiments which provide a more precise "
                "quantification of present-day ERF for various greenhouse gas components."
            ),
            "the `scen7-m` experiment",
            2,
        ),
        (
            "piClim-histnat",
            (
                "In combination with `piClim-control`, "
                "quantifies transient natural effective radiative forcing (ERF) "
                "over the historical period and a future experiment. "
            ),
            "the `scen7-m` experiment",
            2,
        ),
    ):
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description,
                activity="rfmip",
                **AGCM,
                branch_information=None,
                start_timestamp="1850-01-01",
                min_ensemble_size=1,
                tier=tier,
            ),
            CMIP7Experiment(
                description=description.replace(
                    "a future experiment", future_experiment_cmip7
                ),
                start_timestamp="1850-01-01",
                end_timestamp="2100-12-31",
                min_number_yrs_per_sim=251.0,
                parent_activity="cmip",
                parent_experiment="picontrol",
                parent_mip_era="cmip7",
                tier=tier,
            ),
        )


def add_scenariomip() -> None:
    # In CMIP7, the tier depends on whether you are running
    # emissions- or concentration-driven.
    # We can't express this so everything gets the highest tier
    # (i.e. tier 1, see the ScenarioMIP activity description).
    # Similarly, extensions are tier 1 up to 2150 and tier 2 beyond that,
    # which we express via min_number_yrs_per_sim instead.
    for acronym, description_base in (
        (
            "vl",
            (
                "CMIP7 ScenarioMIP Very Low emission scenario - "
                "The Very Low emission scenario "
                "is designed to keep the temperature level as low as plausible given feasibility constraints. "
                "This scenario is thus relevant for the low end of the Paris range "
                "(staying as close as plausible to 1.5C at the time of peak warming "
                "and limiting warming to 1.5C by the end of the century)."
            ),
        ),
        (
            "ln",
            (
                "CMIP7 ScenarioMIP Low-to-Negative emission scenario - "
                "A scenario with a higher overshoot of the 1.5C goal, "
                "followed by stringent climate policies resulting in net-negative greenhouse gas emissions to return to lower warming levels, "
                "thus supporting research into the reversibility of climate outcomes and their impacts."
            ),
        ),
        (
            "l",
            (
                "CMIP7 ScenarioMIP Low emission scenario - "
                "The Low emission scenario is designed to be consistent "
                "with the pursuit of holding warming to a level likely below 2C, "
                "without returning to 1.5C before the end of the century. "
            ),
        ),
        (
            "ml",
            (
                "CMIP7 ScenarioMIP Medium-to-Low emission scenario - "
                "A scenario exploring a delayed increase in mitigation efforts, "
                "short of the Paris temperature goal but achieving net-zero CO2 emissions by the end of the century."
            ),
        ),
        (
            "m",
            (
                "CMIP7 ScenarioMIP Medium emission scenario - "
                "A middle scenario exploring consequences of extending current policies and trends into the future."
            ),
        ),
        (
            "hl",
            (
                "CMIP7 ScenarioMIP High-to-Low emission scenario - "
                "A scenario that follows approximately the same emissions pathway as the High, "
                "but changes course in the second half of the century, applying strong mitigation measures to reach net zero CO2 emissions by 2100."
            ),
        ),
        (
            "h",
            (
                "CMIP7 ScenarioMIP High emission scenario - "
                "A scenario with emissions as high as judged to be plausible, "
                "based on assuming developments that include a rollback of current mitigation policies. "
                "This scenario is expected to result in forcings below SSP5-8.5."
            ),
        ),
    ):
        drs_name = f"scen7-{acronym}"
        scenario_id = add_scenario(
            UniverseExperiment(
                drs_name=drs_name,
                description=scenario_description(description_base, drs_name),
                activity="scenariomip",
                **AOGCM,
                branch_information="Branch from `historical` at 2022-01-01.",
                parent_activity="cmip",
                parent_experiment="historical",
                parent_mip_era="cmip7",
                start_timestamp="2022-01-01",
                end_timestamp="2100-12-31",
                min_number_yrs_per_sim=79.0,
                min_ensemble_size=1,
                tier=1,
            )
        )
        add_scenario(scenario_extension(scenario_id))

        esm_id = add_scenario(scenario_esm(scenario_id))
        add_scenario(scenario_extension(esm_id))


def add_polmip() -> None:
    for (
        drs_name,
        description_base,
        branch_year,
        tier_concentration_driven,
        tier_emissions_driven,
        has_extension,
    ) in (
        (
            "vl-cf",
            (
                "Counterfactual emissions pathway that is as physically consistent as possible, while aiming for global surface air temperature to peak at 1.5C and stabilise or slowly decline."
            ),
            2016,
            2,
            1,
            True,
        ),
        (
            "SSP2-com-CMIP7",
            (
                "Policy-driven pathway aligned with China's carbon neutrality pledge, "
                "peaking carbon emissions before 2030 and achieving carbon neutrality before 2060. "
                "It is developed within the SSP2 socioeconomic framework "
                "and consistent with global Nationally Determined Contributions (NDCs) data."
            ),
            2022,
            1,
            1,
            False,
        ),
    ):
        scenario_id = add_scenario(
            UniverseExperiment(
                drs_name=drs_name,
                description=scenario_description(description_base, drs_name),
                activity="polmip",
                **AOGCM,
                branch_information=f"Branch from `historical` at {branch_year}-01-01.",
                parent_activity="cmip",
                parent_experiment="historical",
                parent_mip_era="cmip7",
                start_timestamp=f"{branch_year}-01-01",
                end_timestamp="2100-12-31",
                min_number_yrs_per_sim=float(2100 - branch_year + 1),
                min_ensemble_size=1,
                tier=tier_concentration_driven,
            )
        )
        esm_id = add_scenario(scenario_esm(scenario_id, tier=tier_emissions_driven))

        if has_extension:
            add_scenario(
                scenario_extension(
                    scenario_id,
                    min_number_yrs_per_sim=100.0,
                    tier=tier_concentration_driven,
                )
            )
            add_scenario(scenario_extension(esm_id, min_number_yrs_per_sim=100.0))


def add_firemip() -> None:
    # # Requested not to have lists, see https://github.com/WCRP-CMIP/WCRP-universe/pull/399#discussion_r4203053542
    # aerosol_fire_emissions = ["BC", "OC", "SO2", "CO", "NOx"]
    # full_fire_emissions = [*aerosol_fire_emissions, "CO2", "CH4", "N2O"]
    hist = get("historical")
    scen7_h = get("scen7-h")

    for (
        drs_name,
        description,
        branch_information,
        start_timestamp,
        end_timestamp,
        parent_activity,
        parent_experiment,
        tier,
    ) in (
        (
            "hist-nofire",
            (
                "Historical coupled simulations with fires set to zero. "
                "In models that use prescribed fire emissions (known as open biomass burning emissions in the forcings), "
                "both burned area in the model code and prescribed fire emissions in the forcing dataset "
                "should be set to zero. "
                "In models with interactive fire modules, set burned area to zero so that fire emissions are therefore diagnosed as zero. "
                "We encourage modeling groups to perform `piControl-nofire` to generate the initial state."
            ),
            "Branch from `piControl-nofire` or (as a fallback) `piControl` at a time of your choosing",
            hist.cmip7.start_timestamp,
            hist.cmip7.end_timestamp,
            None,  # Multiple options, which is not supported
            None,  # Multiple options, which is not supported
            1,
        ),
        (
            "piControl-nofire",
            (
                "Pre-industrial control simulation with no fire emissions. "
                "In models that use prescribed fire emissions (known as open biomass burning emissions in the forcings), "
                "both burned area in the model code and prescribed fire aerosol emissions in the forcing dataset "
                "should be set to zero. "
                "In models with interactive fire modules, set burned area to zero so that fire emissions are therefore diagnosed as zero."
            ),
            "Branch from `piControl-spinup` at a time of your choosing",
            None,
            None,
            "cmip",
            "picontrol-spinup",
            2,
        ),
        (
            "hist-nofireaer",
            (
                "Historical coupled simulations with fire aerosol emissions set to zero. "
                "In models that use prescribed fire emissions (known as open biomass burning emissions in the forcings), "
                "prescribed fire aerosol emissions in the forcing dataset should be set to zero."
            ),
            "Branch from `historical` no later than 1920",
            None,  # undefined so not written
            hist.cmip7.end_timestamp,
            "cmip",
            "historical",
            2,
        ),
        (
            "scen7-h-ca2010fire",
            (
                "The same as `scen7-h`, but with burned area and fire emissions fixed at their 2001-2020 averages. "
                "Burned area should be prescribed as an input field, using each model's own 2001-2020 average derived from its historical simulations. "
                "For models without interactive fire emission modules, all fire emissions (known as open biomass burning emissions in the forcings) "
                "should be replaced with the corresponding 2001-2020 average."
            ),
            scen7_h.universe.branch_information,
            scen7_h.cmip7.start_timestamp,
            "2060-12-31",
            scen7_h.universe.parent_activity,
            scen7_h.universe.parent_experiment,
            2,
        ),
        (
            "scen7-h-ca2010fireaer",
            (
                "The same as `scen7-h`, but with fire aerosol emissions fixed at their 2001–2020 averages. "
                "This does not apply to models that have interactive fire-emissions."
            ),
            scen7_h.universe.branch_information,
            scen7_h.cmip7.start_timestamp,
            "2060-12-31",
            scen7_h.universe.parent_activity,
            scen7_h.universe.parent_experiment,
            2,
        ),
    ):
        if start_timestamp is None or end_timestamp is None:
            min_number_yrs_per_sim = None
        else:
            min_number_yrs_per_sim = float(
                year(end_timestamp) - year(start_timestamp) + 1
            )

        cmip7 = CMIP7Experiment(
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            min_number_yrs_per_sim=min_number_yrs_per_sim,
            parent_mip_era="cmip7" if parent_activity else None,
            tier=tier,
        )
        id = add(
            UniverseExperiment(
                drs_name=drs_name,
                description=description,
                activity="firemip",
                **AOGCM,
                branch_information=branch_information,
                parent_activity=parent_activity,
                parent_experiment=parent_experiment,
                start_timestamp=start_timestamp,
                min_ensemble_size=3,
                tier=tier,
            ),
            cmip7,
        )

        add(
            universe_copy(
                id,
                drs_name=f"esm-{drs_name}",
                description=(
                    f"{description} "
                    "Here run with prescribed carbon dioxide emissions, "
                    "rather than prescribed carbon dioxide concentrations "
                    f"(for the equivalent prescribed carbon dioxide concentrations experiment, see `{drs_name}`)."
                ),
                **ESM,
                branch_information=branch_information.replace(
                    "`piControl", "`esm-piControl"
                ).replace("`historical`", "`esm-hist`"),
                parent_experiment=(
                    f"esm-{parent_experiment}".replace("esm-historical", "esm-hist")
                    if parent_experiment
                    else None
                ),
            ),
            cmip7,
        )


def add_aerchemmip() -> None:
    aq_description_template = (
        "Used to diagnose climate and air quality responses "
        "to the regionally heterogeneous evolution of anthropogenic non-CH4 SLCF emissions. "
        "Anthropogenic non-CH4 tropospheric O3 precursor emissions (NMVOCs, CO, NOx), "
        "aerosols, and aerosol precursor emissions (BC, OC, NH3, SO2) {focus_forcings_evolution}. "
        "All other forcings evolve as in `{other_forcings_experiment}`. "
        "Requires interactive chemistry. "
        "Models without interactive chemistry should run `{pair_experiment}` instead."
    )
    aq_components = dict(
        required_model_components=["aogcm", "aer", "chem"],
        additional_allowed_model_components=["bgc"],
    )
    aer_description_template = (
        "Used to diagnose climate responses "
        "to the regionally heterogeneous evolution of anthropogenic aerosol emissions. "
        "Anthropogenic aerosols and aerosol precursor emissions (BC, OC, NH3, SO2) {focus_forcings_evolution}. "
        "All other forcings evolve as in `{other_forcings_experiment}`. "
        "Intended for models without interactive chemistry. "
        "Models with interactive chemistry should run `{pair_experiment}` instead."
    )
    aer_components = dict(
        required_model_components=["aogcm", "aer"],
        additional_allowed_model_components=["bgc", "chem"],
    )

    hist_universe_fields = pick(
        get("historical").universe,
        "branch_information",
        "parent_activity",
        "parent_experiment",
        "start_timestamp",
    )
    for drs_name, pair_drs_name, description_template, components, note in (
        (
            "hist-piAQ",
            "hist-piAer",
            aq_description_template,
            aq_components,
            "(Renamed from `hist-piNTCF` in AerChemMIP phase 1.)",
        ),
        (
            "hist-piAer",
            "hist-piAQ",
            aer_description_template,
            aer_components,
            "(Identical to `hist-piAer` in AerChemMIP phase 1.)",
        ),
    ):
        description = description_template.format(
            focus_forcings_evolution="evolve as in `piControl`",
            other_forcings_experiment="historical",
            pair_experiment=pair_drs_name,
        )
        add(
            UniverseExperiment(
                drs_name=drs_name,
                description=f"{description} {note}",
                activity="aerchemmip",
                **components,
                **hist_universe_fields,
                min_ensemble_size=1,
                tier=1,
            ),
            CMIP7Experiment(
                start_timestamp=hist_universe_fields["start_timestamp"],
                **pick(
                    get("historical").cmip7, "end_timestamp", "min_number_yrs_per_sim"
                ),
                # https://github.com/WCRP-CMIP/CMIP7-CVs/issues/382
                min_ensemble_size=1,
                parent_mip_era="cmip7",
                tier=1,
            ),
        )

    hist_end_year = year(get("historical").cmip7.end_timestamp)
    for base_experiment, focus_forcings_evolution in (
        # vl gets replaced with h stuff
        ("scen7-vl", "evolve as in `scen7-h`"),
        ("esm-scen7-vl", "evolve as in `esm-scen7-h`"),
        # h gets replaced with present-day stuff
        ("scen7-h", f"are held constant at present-day ({hist_end_year}) levels"),
        ("esm-scen7-h", f"are held constant at present-day ({hist_end_year}) levels"),
    ):
        base_universe_fields = pick(
            get(base_experiment).universe,
            "branch_information",
            "start_timestamp",
            "end_timestamp",
            "min_number_yrs_per_sim",
            "parent_activity",
            "parent_experiment",
            "parent_mip_era",
        )
        for suffix, pair_suffix, description_template, components in (
            ("-AQ", "-Aer", aq_description_template, aq_components),
            ("-Aer", "-AQ", aer_description_template, aer_components),
        ):
            add(
                UniverseExperiment(
                    drs_name=f"{base_experiment}{suffix}",
                    description=description_template.format(
                        focus_forcings_evolution=focus_forcings_evolution,
                        other_forcings_experiment=base_experiment,
                        pair_experiment=f"{base_experiment}{pair_suffix}",
                    ),
                    activity="aerchemmip",
                    **components,
                    **base_universe_fields,
                    # https://github.com/WCRP-CMIP/CMIP7-CVs/issues/382
                    min_ensemble_size=1,
                    tier=1,
                ),
                CMIP7Experiment(
                    **pick(
                        get(base_experiment).universe,
                        "start_timestamp",
                        "end_timestamp",
                        "min_number_yrs_per_sim",
                    ),
                    parent_mip_era="cmip7",
                    tier=1,
                ),
            )


def add_geomip() -> None:
    base_scenario = "scen7-ml"
    start_year = 2035
    add(
        UniverseExperiment(
            drs_name="G7-1p5K-SAI",
            description=(
                "Stablisation of global-mean temperature at 1.5C "
                "by increasing stratospheric sulfur forcing "
                "to whatever level is required to achieve stable temperatures. "
                "The simulation generally branches from a scenario simulation at some point in the future."
            ),
            activity="geomip",
            **AOGCM,
            min_ensemble_size=1,
            tier=1,
        ),
        CMIP7Experiment(
            description=(
                "Stablisation of global-mean temperature at 1.5C "
                "by increasing stratospheric sulfur forcing "
                "to whatever level is required to achieve stable temperatures "
                f"after following the `{base_scenario}` scenario until {start_year}."
            ),
            branch_information=f"Branch from the `{base_scenario}` simulation at the start of {start_year}.",
            start_timestamp=f"{start_year}-01-01",
            end_timestamp=None,
            min_number_yrs_per_sim=50.0,
            min_ensemble_size=1,
            parent_activity=get(base_scenario).universe.activity,
            parent_experiment=base_scenario,
            parent_mip_era="cmip7",
            tier=1,
        ),
    )


def get_citation_for_doi(doi: str, style: str = "apa") -> str | None:
    print(f"Trying to get citation for {doi=}")
    url = f"https://doi.org/{doi}"
    headers = {"Accept": f"text/x-bibliography; style={style}"}

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        res = response.read().decode("utf-8").strip()

    return res


def get_reference(url: str, activity: str, number: int) -> Reference:
    try:
        citation = get_citation_for_doi(url)
        doi = url

    except urllib.error.HTTPError as exc:
        print(f"Could not get DOI for {url}. {exc.code=} {exc.reason=}")
        doi = "N/A"
        citation = f"See {url}"

    return Reference(
        id=f"{activity}_cmip7_ref_{number:03d}", citation=citation, doi=doi
    )


def as_json(obj: Any) -> dict[str, Any]:
    """Get the fields of a dataclass to write, i.e. those that aren't `NOT_WRITTEN`"""
    return {k: v for k, v in dataclasses.asdict(obj).items() if v is not NOT_WRITTEN}


def sort_keys(
    content: dict[str, Any],
    header_keys: tuple[str, ...] = (
        "@context",
        "id",
        "type",
        "description",
        "drs_name",
        "start_timestamp",
        "end_timestamp",
        "min_number_yrs_per_sim",
    ),
) -> dict[str, Any]:
    res = {k: content[k] for k in header_keys if k in content}
    res.update({k: content[k] for k in sorted(content) if k not in header_keys})

    return res


def write_file(out_file: Path, content: dict[str, Any]) -> None:
    with open(out_file, "w") as fh:
        json.dump(
            sort_keys({"@context": "000_context.jsonld", **content}), fh, indent=4
        )
        fh.write("\n")

    print(f"Wrote {out_file}")


def main():
    add_deck_and_friends()
    add_flat10()
    add_damip()
    add_lmip()
    add_pmip()
    add_piclim()
    add_scenariomip()
    add_polmip()
    add_firemip()
    add_aerchemmip()
    add_geomip()

    for id, experiment in EXPERIMENTS.items():
        write_file(
            UNIVERSE_ROOT / "experiment" / f"{id}.json",
            {"id": id, "type": "experiment", **as_json(experiment.universe)},
        )
        write_file(
            PROJECT_ROOT / "experiment" / f"{id}.json",
            {"id": id, "type": "experiment", **as_json(experiment.cmip7)},
        )

    for activity in ACTIVITIES.values():
        references = [
            get_reference(url, activity.id, i)
            for i, url in enumerate(activity.references)
        ]
        for reference in references:
            write_file(
                UNIVERSE_ROOT / "reference" / f"{reference.id}.json",
                {"type": "reference", "drs_name": reference.id, **as_json(reference)},
            )

        write_file(
            PROJECT_ROOT / "activity" / f"{activity.id}.json",
            {
                **as_json(activity),
                "type": "activity",
                "experiments": sorted(
                    id
                    for id, experiment in EXPERIMENTS.items()
                    if experiment.universe.activity == activity.id
                ),
                # Written as the ids of the reference entries, rather than DOIs
                "references": sorted(v.id for v in references),
            },
        )


if __name__ == "__main__":
    main()
