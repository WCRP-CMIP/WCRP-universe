# WCRP Universe - Contribution Guidelines

Welcome to the WCRP Universe repository! This repository contains the universal controlled vocabularies (CVs) shared across WCRP climate modeling projects including CMIP7.

## How to Contribute

Use the issue templates below to add or modify controlled vocabulary entries. All submissions go through a review process before being merged into the official vocabularies.

### Before You Submit

1. **Check existing entries**: Search the repository to ensure your entry doesn't already exist
2. **Use correct formatting**: Follow the naming conventions (lowercase, hyphenated identifiers)
3. **Provide descriptions**: Clear descriptions help users understand each term

### Data Format

All entries use JSON-LD format with standard fields:
- `validation_key`: Unique identifier (lowercase, hyphenated)
- `ui_label`: Human-readable display name  
- `description`: Detailed description of the term
- `alias`: Alternative names (optional)




## 1. Submitting New Controlled Vocabularies

The following forms are available for this repository, and can be used to add or modify entries. The complete submission pipeline (if applicable) will be outlined in the section above.


### Core CVs

- [activity](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml)
- [frequency](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml)
- [license](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=license.yml)
- [mip](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=mip.yml)
- [product](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=product.yml)
- [realm](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=realm.yml)
- [resolution](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml)
- [source_type](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml)
### Archive & Data

- [archive_id](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=archive_id.yml)
### Model Structure

- [model_calendar](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=model_calendar.yml)
- [model_component_type](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=model_component_type.yml)
- [model_family](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=model_family.yml)
- [scientific_domain](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml)
### Grid Specifications

- [arrangement](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=arrangement.yml)
- [calendar](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml)
- [grid_mapping](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml)
- [grid_type](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml)
- [native_horizontal_grid_region](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=native_horizontal_grid_region.yml)
- [native_horizontal_grid_temporal_refinement](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=native_horizontal_grid_temporal_refinement.yml)
- [native_horizontal_grid_type](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=native_horizontal_grid_type.yml)
- [native_vertical_grid_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=native_vertical_grid_coordinate.yml)
- [native_vertical_grid_units](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=native_vertical_grid_units.yml)
- [region](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml)
- [temporal_refinement](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=temporal_refinement.yml)
- [truncation_method](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=truncation_method.yml)
- [units](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=units.yml)
- [vertical_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml)
### Organizations

- [organisation](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml)
- [consortium](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=consortium.yml)
### Other

- [cell_variable_type](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=cell_variable_type.yml)

## 2 Modifying or reusing existing entries

The following links will open pre-filled GitHub issues with content from the selected files. These can be used to update entries or make new ones. 

<details name="activity">
<summary>Activity (40 entries)</summary>

- [AERA-MIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+AERA-MIP&issue_kind=%22Modify%22&validation_key=AERA-MIP&description=&ui_label=Adaptive+Emission+Reduction+Approach+Modelling+Intercomparison+Project)

- [AerChemMIP2](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+AerChemMIP2&issue_kind=%22Modify%22&validation_key=AerChemMIP2&description=&ui_label=Aerosol+Chemistry+Model+Intercomparison+Project+phase+2)

- [AerChemMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+AerChemMIP&issue_kind=%22Modify%22&validation_key=AerChemMIP&description=AerChemMIP+experiments+focus+on+the+role+of+atmospheric+chemistry+and+aerosols+in+climate%2C+including+piClim+and+hist-piSLCF+simulations.&ui_label=)

- [C4MIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+C4MIP&issue_kind=%22Modify%22&validation_key=C4MIP&description=C4MIP+experiments+focus+on+carbon+cycle+feedbacks+and+interactions%2C+including+1pctCO2-bgc+and+esm-flat10-cdr+experiments.&ui_label=Coupled+Climate+Carbon+Cycle+MIP)

- [CDRMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+CDRMIP&issue_kind=%22Modify%22&validation_key=CDRMIP&description=&ui_label=Carbon+Dioxide+Removal+Model+Intercomparison+Project)

- [CERESMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+CERESMIP&issue_kind=%22Modify%22&validation_key=CERESMIP&description=&ui_label=CERES-era+Model+Intercomparison+Project)

- [CFMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+CFMIP&issue_kind=%22Modify%22&validation_key=CFMIP&description=CFMIP+experiments+focus+on+cloud+feedbacks+and+their+role+in+climate%2C+including+abrupt-0p5CO2+and+amip-piForcing+simulations.&ui_label=Cloud+Feedback+Model+Intercomparison+Project+)

- [CMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+CMIP&issue_kind=%22Modify%22&validation_key=CMIP&description=CMIP+DECK%3A+1pctCO2%2C+abrupt-4xCO2%2C+amip%2C+esm-piControl%2C+esm-historical%2C+historical%2C+and+piControl+experiments&ui_label=)

- [CORDEX](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+CORDEX&issue_kind=%22Modify%22&validation_key=CORDEX&description=&ui_label=Coordinated+Regional+Climate+Downscaling+Experiment)

- [DAMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+DAMIP&issue_kind=%22Modify%22&validation_key=DAMIP&description=DAMIP+focuses+on+detection+and+attribution+of+climate+change%2C+covering+experiments+like+hist-aer+and+hist-nat.&ui_label=Detection+and+Attribution+Model+Intercomparison+Project)

- [DCPP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+DCPP&issue_kind=%22Modify%22&validation_key=DCPP&description=DCPP+focuses+on+decadal+climate+predictions+and+initialized+experiments+like+prediction+for+2025-2036.&ui_label=Decadal+Climate+Prediction+Project)

- [FireMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+FireMIP&issue_kind=%22Modify%22&validation_key=FireMIP&description=&ui_label=Fire+Modeling+Intercomparison+Project)

- [FishMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+FishMIP&issue_kind=%22Modify%22&validation_key=FishMIP&description=&ui_label=Fisheries+and+Marine+Ecosystem+Model+Intercomparison+Project)

- [GeoMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+GeoMIP&issue_kind=%22Modify%22&validation_key=GeoMIP&description=GeoMIP+explores+the+potential+impacts+and+side-effects+of+geoengineering%2C+including+experiments+like+G7-1.5K-SAI.&ui_label=Geoengineering+Model+Intercomparison+Project)

- [HighResMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+HighResMIP&issue_kind=%22Modify%22&validation_key=HighResMIP&description=&ui_label=High+Resolution+Model+Intercomparison+Project)

- [IRRMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+IRRMIP&issue_kind=%22Modify%22&validation_key=IRRMIP&description=&ui_label=Irrigation+Model+Intercomparison+Project)

- [ISMIP7](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+ISMIP7&issue_kind=%22Modify%22&validation_key=ISMIP7&description=&ui_label=Ice+Sheet+Model+Intercomparison+Project+for+CMIP)

- [LESFMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+LESFMIP&issue_kind=%22Modify%22&validation_key=LESFMIP&description=The+Large+Ensemble+Single+Forcing+Model+Intercomparison+Project&ui_label=)

- [LMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+LMIP&issue_kind=%22Modify%22&validation_key=LMIP&description=LMIP+explores+land-atmosphere+interactions+and+processes%2C+with+experiments+like+land-hist.&ui_label=Land+Model+Intercomparison+Project)

- [LUMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+LUMIP&issue_kind=%22Modify%22&validation_key=LUMIP&description=&ui_label=Land-Use+Model+Intercomparison+Project)

- [LongRunMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+LongRunMIP&issue_kind=%22Modify%22&validation_key=LongRunMIP&description=&ui_label=LongRunMIP)

- [MISOMIP2](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+MISOMIP2&issue_kind=%22Modify%22&validation_key=MISOMIP2&description=&ui_label=Marine+Ice+Sheet-Ocean+Model+Intercomparions+Project)

- [MUMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+MUMIP&issue_kind=%22Modify%22&validation_key=MUMIP&description=&ui_label=Model+Uncertainty+Model+Intercomparison+Project)

- [MethaneMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+MethaneMIP&issue_kind=%22Modify%22&validation_key=MethaneMIP&description=&ui_label=MethaneMIP%3A+Investigating+the+near-term+climate+benefits+of+methane+mitigation)

- [NAHosMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+NAHosMIP&issue_kind=%22Modify%22&validation_key=NAHosMIP&description=&ui_label=North+Atlantic+Hosing+Model+Intercomparison+Project)

- [OMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+OMIP&issue_kind=%22Modify%22&validation_key=OMIP&description=&ui_label=Ocean+Model+Intercomparison+Project)

- [PMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+PMIP&issue_kind=%22Modify%22&validation_key=PMIP&description=PMIP+focuses+on+past+climate+variability%2C+with+experiments+like+LIGabrupt.&ui_label=Paleoclimate+Modelling+Intercomparison+Project)

- [PPEMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+PPEMIP&issue_kind=%22Modify%22&validation_key=PPEMIP&description=&ui_label=Perturbed+Parameter+Ensemble+Model+Inter-comparaison+Project)

- [RAMIP ](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+RAMIP+&issue_kind=%22Modify%22&validation_key=RAMIP+&description=&ui_label=Regional+Aerosol+Model+Intercomparison+Project)

- [RAMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+RAMIP&issue_kind=%22Modify%22&validation_key=RAMIP&description=Regional+Aerosol+Model+Intercomparison+Project&ui_label=)

- [RFMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+RFMIP&issue_kind=%22Modify%22&validation_key=RFMIP&description=RFMIP+assesses+the+radiative+forcing+of+climate+change+with+experiments+such+as+piClim-aer%2C+piClim-histaer%2C+and+piClim-histall.&ui_label=Radiative+Forcing+Model+Intercomparison+Project)

- [SIMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+SIMIP&issue_kind=%22Modify%22&validation_key=SIMIP&description=&ui_label=Sea+Ice+Model+Intercomparison+Project)

- [SOFIAMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+SOFIAMIP&issue_kind=%22Modify%22&validation_key=SOFIAMIP&description=&ui_label=Southern+Ocean+Freshwater+Input+from+Antarctica+Model+Intercomparison+Project)

- [SP-MIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+SP-MIP&issue_kind=%22Modify%22&validation_key=SP-MIP&description=&ui_label=Soil+Parameter+Model+Intercomparison+Project)

- [ScenarioMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+ScenarioMIP&issue_kind=%22Modify%22&validation_key=ScenarioMIP&description=ScenarioMIP+focuses+on+future+climate+projections+based+on+different+socio-economic+pathways%2C+including+High%2C+Medium%2C+and+Very+Low+scenarios.&ui_label=)

- [TBIMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+TBIMIP&issue_kind=%22Modify%22&validation_key=TBIMIP&description=&ui_label=Tropical+Basin+Interaction+Model+Intercomparison+Project)

- [TIPMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+TIPMIP&issue_kind=%22Modify%22&validation_key=TIPMIP&description=TIPMIP+is+an+international+model+intercomparison+project+that+aims+to+systematically+advance+our+understanding+of+tipping+dynamics+in+various+Earth+system+components%2C+and+assess+the+associated+uncertainties.+By+connecting+and+evaluating+various+models%2C+TIPMIP+will+fill+critical+knowledge+gaps+in+Earth+system+and+climate+modelling+by+improving+the+assessment+of+overall+anthropogenic+forcing+and+long-term+commitments+%28irreversibilities%29.+It+will+furthermore+foster+interdisciplinary+knowledge+transfer+and+shed+light+on+critical+processes+currently+underrepresented+in+Earth-system+models+and+analysis.+In+doing+so%2C+it+will+inform+relevant+policy-+and+decision+makers+regarding+tipping+boundaries+in+the+Earth+system.&ui_label=Tipping+Point+Modelling+Intercomparison+Project)

- [VolMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+VolMIP&issue_kind=%22Modify%22&validation_key=VolMIP&description=&ui_label=Model+Intercomparison+Project+on+the+climate+response+to+Volcanic+forcing)

- [WhatIfMIP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+WhatIfMIP&issue_kind=%22Modify%22&validation_key=WhatIfMIP&description=&ui_label=What+If+Modeling+Intercomparison+Project)

- [none](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=activity.yml&title=Modify%3A+Activity%3A+none&issue_kind=%22Modify%22&validation_key=none&description=%27none%27+entry+permissable+only+for+the+experiment+parent+id.+&ui_label=)

</details>

<details name="archive_id">
<summary>Archive Id (1 entries)</summary>

- [WCRP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=archive_id.yml&title=Modify%3A+Archive+Id%3A+WCRP&issue_kind=%22Modify%22&validation_key=WCRP&description=A+collection+of+datasets+from+the+AMIP+and+CMIP+project+phases%2C+along+with+project+supporting+datasets+from+the+input4MIPs+%28forcing+datasets+used+to+drive+CMIP+simulations%29+and+obs4MIPs+%28observational+datasets+used+to+evaluate+CMIP+simulations%2C+and+numerous+other+supporting+activities&ui_label=)

</details>

<details name="arrangement">
<summary>Arrangement (5 entries)</summary>

- [arakawa-a](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-a&issue_kind=%22Modify%22&validation_key=arakawa-a&description=The+Arakawa+A+grid+places+mass-+and+velocity-related+quantities+at+the+same+location+on+each+grid+cell.&ui_label=Arakawa+A-grid)

- [arakawa-b](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-b&issue_kind=%22Modify%22&validation_key=arakawa-b&description=The+Arakawa+B+grid+places+velocity-related+quantities+at+the+corners+of+mass+cells.&ui_label=Arakawa+B-grid)

- [arakawa-c](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-c&issue_kind=%22Modify%22&validation_key=arakawa-c&description=The+Arakawa+C+grid+places+velocity-related+quantities+at+the+centres+of+mass+cell+edges%2C+such+that+each+component+is+perpendicular+to+its+edge.&ui_label=Arakawa+C-grid)

- [arakawa-d](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-d&issue_kind=%22Modify%22&validation_key=arakawa-d&description=The+Arakawa+D+grid+places+velocity-related+quantities+at+the+centres+of+mass+cell+edges%2C+such+that+each+component+is+tangential+to+its+edge.&ui_label=Arakawa+D-grid)

- [arakawa-e](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-e&issue_kind=%22Modify%22&validation_key=arakawa-e&description=The+Arakawa+E+grid+places+mass-related+quantities+at+the+centres+of+velocity+cell+edges.&ui_label=Arakawa+E-grid)

</details>

<details name="calendar">
<summary>Calendar (9 entries)</summary>

- [360_day](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+360_day&issue_kind=%22Modify%22&validation_key=360_day&alias=&description=A+calendar+in+which+each+year+consists+of+12+months+of+exactly+30+days+each.+This+calendar+is+commonly+used+in+climate+models+for+computational+convenience.&ui_label=360-day)

- [365_day](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+365_day&issue_kind=%22Modify%22&validation_key=365_day&alias=noleap&description=A+calendar+in+which+each+year+consists+of+365+days+with+no+leap+years.+All+months+have+their+standard+lengths+%2828+days+for+February%29.&ui_label=365-day+%28No+Leap%29)

- [366_day](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+366_day&issue_kind=%22Modify%22&validation_key=366_day&alias=all_leap&description=A+calendar+in+which+each+year+consists+of+366+days%2C+i.e.%2C+every+year+is+a+leap+year+with+February+having+29+days.&ui_label=366-day+%28All+Leap%29)

- [julian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+julian&issue_kind=%22Modify%22&validation_key=julian&alias=&description=Julian+calendar+with+leap+year+every+four+years+without+exception.+This+calendar+was+in+use+prior+to+the+Gregorian+calendar+reform+of+1582.&ui_label=Julian)

- [none](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+none&issue_kind=%22Modify%22&validation_key=none&alias=&description=No+calendar+-+used+for+data+without+a+temporal+dimension+or+for+time-invariant+fields.&ui_label=None)

- [proleptic_gregorian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+proleptic_gregorian&issue_kind=%22Modify%22&validation_key=proleptic_gregorian&alias=&description=A+calendar+with+the+Gregorian+rules+for+leap-years+extended+to+dates+before+1582-10-15.+All+dates+consistent+with+these+rules+are+allowed%2C+both+before+and+after+1582-10-15.&ui_label=Proleptic+Gregorian)

- [standard](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+standard&issue_kind=%22Modify%22&validation_key=standard&alias=gregorian&description=Mixed+Gregorian%2FJulian+calendar+as+defined+by+UDUNITS.+This+is+the+default+calendar+assumed+if+no+calendar+attribute+is+specified.+A+deprecated+alternative+name+for+this+calendar+is+%27gregorian%27.&ui_label=Standard+%28Gregorian%29)

- [tai](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+tai&issue_kind=%22Modify%22&validation_key=tai&alias=&description=The+Gregorian+calendar+without+leap+seconds+that+is+based+on+International+Atomic+Time+%28TAI%29%2C+as+defined+by+the+CF+conventions.&ui_label=TAI)

- [utc](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+utc&issue_kind=%22Modify%22&validation_key=utc&alias=&description=The+Gregorian+calendar+with+leap+seconds+prescribed+by+Coordinated+Universal+Time+%28UTC%29%2C+as+defined+by+the+CF+conventions.&ui_label=UTC)

</details>

<details name="cell_variable_type">
<summary>Cell Variable Type (5 entries)</summary>

- [mass](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+mass&issue_kind=%22Modify%22&validation_key=mass&description=Mass-related+variables%2C+including+those+representing+thermodynamic+and+hydrodynamic+quantities.&ui_label=Mass)

- [velocity](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+velocity&issue_kind=%22Modify%22&validation_key=velocity&description=Variables+representing+the+velocity+vector+when+it+is+not+partitioned+into+X+and+Y+components+%28such+as+for+some+unstructured+grids%29.&ui_label=Velocity)

- [vorticity](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+vorticity&issue_kind=%22Modify%22&validation_key=vorticity&description=Vorticity+and+related+rotational+variables.&ui_label=Vorticity)

- [x-velocity](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+x-velocity&issue_kind=%22Modify%22&validation_key=x-velocity&description=Variables+representing+the+X+component+of+the+velocity+vector+and+certain+horizontal+fluxes+of+mass%2C+energy%2C+momentum%2C+etc.+For+a+grid+defined+by+spherical+polar+coordinates%2C+the+X+direction+is+longitude.&ui_label=X+Velocity)

- [y-velocity](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+y-velocity&issue_kind=%22Modify%22&validation_key=y-velocity&description=Variables+representing+the+Y+component+of+the+velocity+vector+and+certain+horizontal+fluxes+of+mass%2C+energy%2C+momentum%2C+etc.+For+a+grid+defined+by+spherical+polar+coordinates%2C+the+Y+direction+is+latitude.&ui_label=Y+Velocity)

</details>

<details name="frequency">
<summary>Frequency (16 entries)</summary>

- [1hrCM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+1hrCM&issue_kind=%22Modify%22&validation_key=1hrCM&description=monthly-mean+diurnal+cycle+resolving+each+day+into+1-hour+means&ui_label=1+Hour+Climatology+Monthly)

- [1hrPt](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+1hrPt&issue_kind=%22Modify%22&validation_key=1hrPt&description=sampled+hourly%2C+at+specified+time+point+within+an+hour&ui_label=1+Hour+Point)

- [1hr](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+1hr&issue_kind=%22Modify%22&validation_key=1hr&description=sampled+hourly&ui_label=1+Hourly+Frequency)

- [3hrPt](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+3hrPt&issue_kind=%22Modify%22&validation_key=3hrPt&description=sampled+3+hourly%2C+at+specified+time+point+within+the+time+period&ui_label=3+Hour+Point)

- [3hr](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+3hr&issue_kind=%22Modify%22&validation_key=3hr&description=3+hourly+mean+samples&ui_label=3+Hourly+Frequency)

- [6hrPt](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+6hrPt&issue_kind=%22Modify%22&validation_key=6hrPt&description=sampled+6+hourly%2C+at+specified+time+point+within+the+time+period&ui_label=6+Hour+Point)

- [6hr](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+6hr&issue_kind=%22Modify%22&validation_key=6hr&description=6+hourly+mean+samples&ui_label=6+Hourly+Frequency)

- [day](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+day&issue_kind=%22Modify%22&validation_key=day&description=daily+mean+samples&ui_label=Daily+Frequency)

- [dec](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+dec&issue_kind=%22Modify%22&validation_key=dec&description=decadal+mean+samples&ui_label=Decadal+Frequency)

- [fx](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+fx&issue_kind=%22Modify%22&validation_key=fx&description=fixed+%28time+invariant%29+field&ui_label=Fixed+Frequency)

- [monC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+monC&issue_kind=%22Modify%22&validation_key=monC&description=monthly+climatology+computed+from+monthly+mean+samples&ui_label=Monthly+Climatology)

- [monPt](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+monPt&issue_kind=%22Modify%22&validation_key=monPt&description=sampled+monthly%2C+at+specified+time+point+within+the+time+period&ui_label=Monthly+Point)

- [mon](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+mon&issue_kind=%22Modify%22&validation_key=mon&description=monthly+mean+samples&ui_label=Monthly+Frequency)

- [subhrPt](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+subhrPt&issue_kind=%22Modify%22&validation_key=subhrPt&description=sampled+sub-hourly%2C+at+specified+time+point+within+an+hour&ui_label=Sub-Hourly+Point)

- [yrPt](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+yrPt&issue_kind=%22Modify%22&validation_key=yrPt&description=sampled+yearly%2C+at+specified+time+point+within+the+time+period&ui_label=Yearly+Point)

- [yr](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+yr&issue_kind=%22Modify%22&validation_key=yr&description=annual+mean+samples&ui_label=Yearly+Frequency)

</details>

<details name="grid_mapping">
<summary>Grid Mapping (16 entries)</summary>

- [albers_conical_equal_area](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+albers_conical_equal_area&issue_kind=%22Modify%22&validation_key=albers_conical_equal_area&description=A+projection+that+preserves+area+but+not+shape%2C+creating+accurate+representations+of+large%2C+east-west-oriented+land+masses%2C+as+defined+by+the+CF+conventions.&ui_label=Albers+Conical+Equal+Area)

- [azimuthal_equidistant](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+azimuthal_equidistant&issue_kind=%22Modify%22&validation_key=azimuthal_equidistant&description=A+projection+that+maintains+the+correct+distance+and+direction+from+a+central+point+to+all+other+points+on+the+map%2C+as+defined+by+the+CF+conventions.&ui_label=Azimuthal+Equidistant)

- [geostationary](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+geostationary&issue_kind=%22Modify%22&validation_key=geostationary&description=A+type+of+azimuthal+projection+designed+to+show+the+Earth+as+it+appears+to+a+geostationary+satellite%2C+offering+a+perspective+that+minimizes+distortion+for+areas+under+view%2C+as+defined+by+the+CF+conventions.&ui_label=Geostationary)

- [healpix](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+healpix&issue_kind=%22Modify%22&validation_key=healpix&description=The+hierarchical+equal+area+isolatitude+pixelisation+of+a+sphere+based+on+subdivision+of+a+distorted+rhombic+dodecahedron+%28HEALPix%29%2C+as+defined+by+the+CF+conventions.&ui_label=HEALPix)

- [lambert_azimuthal_equal_area](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+lambert_azimuthal_equal_area&issue_kind=%22Modify%22&validation_key=lambert_azimuthal_equal_area&description=A+projection+that+accurately+preserves+the+area+of+all+regions+on+a+map%2C+as+defined+by+the+CF+conventions.&ui_label=Lambert+Azimuthal+Equal+Area)

- [lambert_conformal_conic](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+lambert_conformal_conic&issue_kind=%22Modify%22&validation_key=lambert_conformal_conic&description=A+projection+that+preserves+the+shape+of+small+areas+by+using+a+cone+placed+over+the+Earth%27s+surface%2C+with+the+projection+onto+the+cone+occurring+along+lines+radiating+from+the+Earth%27s+centre%2C+as+defined+by+the+CF+conventions.&ui_label=Lambert+Conformal+Conic)

- [lambert_cylindrical_equal_area](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+lambert_cylindrical_equal_area&issue_kind=%22Modify%22&validation_key=lambert_cylindrical_equal_area&description=A+cylindrical+map+projection+that+preserves+area+accurately+but+distorts+shape%2C+especially+away+from+the+equator%2C+as+defined+by+the+CF+conventions.&ui_label=Lambert+Cylindrical+Equal+Area)

- [latitude_longitude](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+latitude_longitude&issue_kind=%22Modify%22&validation_key=latitude_longitude&description=A+projection+that+treats+latitude+and+longitude+as+planar+X+and+Y+coordinates%2C+as+defined+by+the+CF+conventions.&ui_label=Latitude-Longitude)

- [mercator](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+mercator&issue_kind=%22Modify%22&validation_key=mercator&description=Cylindrical+map+projection+preserving+angles%2C+commonly+used+for+ocean+models.&ui_label=Mercator)

- [orthographic](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+orthographic&issue_kind=%22Modify%22&validation_key=orthographic&description=A+form+of+parallel+projection+in+which+all+the+projection+lines+are+orthogonal+to+the+projection+plane%2C+as+defined+by+the+CF+conventions.&ui_label=Orthographic)

- [polar_stereographic](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+polar_stereographic&issue_kind=%22Modify%22&validation_key=polar_stereographic&description=An+azimuthal+projection+that+maps+the+Earth%27s+surface+onto+a+flat+plane+from+a+view+point+at+one+pole%2C+projecting+points+from+the+globe+to+a+plane+tangent+to+the+opposite+pole%2C+as+defined+by+the+CF+conventions.&ui_label=Polar+Stereographic)

- [rotated_latitude_longitude](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+rotated_latitude_longitude&issue_kind=%22Modify%22&validation_key=rotated_latitude_longitude&description=A+geographic+coordinate+system+where+the+traditional+north+pole+is+shifted+to+a+different+location%2C+as+defined+by+the+CF+conventions.&ui_label=Rotated+Latitude-Longitude)

- [sinusoidal](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+sinusoidal&issue_kind=%22Modify%22&validation_key=sinusoidal&description=An+equal-area+projection+that+accurately+represents+area+but+distorts+shape%2C+especially+at+the+edges%2C+as+defined+by+the+CF+conventions.&ui_label=Sinusoidal)

- [stereographic](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+stereographic&issue_kind=%22Modify%22&validation_key=stereographic&description=A+projection+that+preserves+the+angles+between+intersecting+lines+and+curves+on+the+sphere%2C+as+defined+by+the+CF+conventions.&ui_label=Stereographic)

- [transverse_mercator](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+transverse_mercator&issue_kind=%22Modify%22&validation_key=transverse_mercator&description=A+projection+that+rotates+the+Mercator+projection+cylinder+90+degrees+to+be+tangent+to+the+Earth+along+a+meridian+instead+of+the+equator%2C+as+defined+by+the+CF+conventions.&ui_label=Transverse+Mercator)

- [vertical_perspective](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+vertical_perspective&issue_kind=%22Modify%22&validation_key=vertical_perspective&description=A+projection+used+to+represent+the+Earth+from+a+point+of+view+directly+above+its+centre%2C+as+defined+by+the+CF+conventions.&ui_label=Vertical+Perspective)

</details>

<details name="grid_type">
<summary>Grid Type (23 entries)</summary>

- [cubed_sphere](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+cubed_sphere&issue_kind=%22Modify%22&validation_key=cubed_sphere&description=The+spherical+surface+is+defined+as+six+coupled+logically+square+regions.&ui_label=Cubed+Sphere)

- [cubic_octahedral_spectral_reduced_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+cubic_octahedral_spectral_reduced_gaussian&issue_kind=%22Modify%22&validation_key=cubic_octahedral_spectral_reduced_gaussian&description=A+spectral+reduced+Gaussian+grid+for+which+the+smallest+spectral+wavelength+is+represented+by+4+grid+points%2C+and+which+uses+an+octahedron-based+method+to+reduce+the+number+of+grid+points+towards+the+poles.&ui_label=Cubic+Octahedral+Spectral+Reduced+Gaussian)

- [displaced_pole](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+displaced_pole&issue_kind=%22Modify%22&validation_key=displaced_pole&description=An+ocean+grid+whose+poles+are+not+antipodean%2C+typically+with+the+northern+pole+displaced+to+lie+over+land.&ui_label=Displaced+Pole)

- [hierarchical_discrete_global_grid](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+hierarchical_discrete_global_grid&issue_kind=%22Modify%22&validation_key=hierarchical_discrete_global_grid&description=A+tessellation+of+cells+that+exhaustively+cover+the+spherical+surface+of+the+globe%2C+with+each+resolution+defined+as+a+subdivision+of+cells+at+a+base+resolution%2C+and+cells+at+a+given+resolution+having+equal+areas.&ui_label=Hierarchical+Discrete+Global+Grid)

- [icosahedral](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+icosahedral&issue_kind=%22Modify%22&validation_key=icosahedral&description=Grid+based+on+subdividing+an+icosahedron+projected+onto+a+sphere%2C+providing+quasi-uniform+global+coverage.&ui_label=Icosahedral)

- [icosahedral_geodesic](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+icosahedral_geodesic&issue_kind=%22Modify%22&validation_key=icosahedral_geodesic&description=A+grid+that+uses+triangular+tiles+based+on+the+subdivision+of+an+icosahedron.&ui_label=Icosahedral+Geodesic)

- [icosahedral_geodesic_dual](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+icosahedral_geodesic_dual&issue_kind=%22Modify%22&validation_key=icosahedral_geodesic_dual&description=A+grid+that+uses+hexagonal+and+pentagonal+tiles+and+is+the+dual+of+an+icosahedral_geodesic+grid.&ui_label=Icosahedral+Geodesic+Dual)

- [linear_spectral_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+linear_spectral_gaussian&issue_kind=%22Modify%22&validation_key=linear_spectral_gaussian&description=A+spectral+Gaussian+grid+for+which+the+smallest+spectral+wavelength+is+represented+by+2+grid+points.&ui_label=Linear+Spectral+Gaussian)

- [plane_projection](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+plane_projection&issue_kind=%22Modify%22&validation_key=plane_projection&description=Any+transformation+employed+to+represent+the+spherical+surface+of+the+globe+on+a+plane.&ui_label=Plane+Projection)

- [quadratic_spectral_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+quadratic_spectral_gaussian&issue_kind=%22Modify%22&validation_key=quadratic_spectral_gaussian&description=A+spectral+Gaussian+grid+for+which+the+smallest+spectral+wavelength+is+represented+by+3+grid+points.&ui_label=Quadratic+Spectral+Gaussian)

- [reduced_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+reduced_gaussian&issue_kind=%22Modify%22&validation_key=reduced_gaussian&description=A+Gaussian+grid+for+which+the+number+of+longitudinal+points+is+reduced+as+the+poles+are+approached.&ui_label=Reduced+Gaussian)

- [regular_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+regular_gaussian&issue_kind=%22Modify%22&validation_key=regular_gaussian&description=A+Gaussian+grid+for+which+the+number+of+longitudinal+points+is+constant+for+each+latitude.&ui_label=Regular+Gaussian)

- [regular_latitude_longitude](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+regular_latitude_longitude&issue_kind=%22Modify%22&validation_key=regular_latitude_longitude&description=A+rectilinear+latitude-longitude+grid+with+evenly+spaced+latitude+points+and+evenly+spaced+longitude+points.&ui_label=Regular+Latitude-Longitude)

- [rotated_pole](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+rotated_pole&issue_kind=%22Modify%22&validation_key=rotated_pole&description=A+regular+latitude-longitude+grid+that+is+rotated+to+define+a+different+north+pole+location.&ui_label=Rotated+Pole)

- [spectral_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+spectral_gaussian&issue_kind=%22Modify%22&validation_key=spectral_gaussian&description=A+grid+based+on+the+transformation+from+spectral+space+to+a+reduced+or+non-reduced+Gaussian+grid.&ui_label=Spectral+Gaussian)

- [spectral_reduced_gaussian](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+spectral_reduced_gaussian&issue_kind=%22Modify%22&validation_key=spectral_reduced_gaussian&description=A+grid+based+on+the+transformation+from+spectral+space+to+a+reduced+Gaussian+grid.&ui_label=Spectral+Reduced+Gaussian)

- [stretched](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+stretched&issue_kind=%22Modify%22&validation_key=stretched&description=A+grid+with+higher+resolution+concentrated+over+an+area+of+interest%2C+at+the+expense+of+lower+resolution+elsewhere.&ui_label=Stretched)

- [tripolar](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+tripolar&issue_kind=%22Modify%22&validation_key=tripolar&description=A+global+curvilinear+ocean+grid+with+a+southern+pole+and+two+northern+poles+all+placed+over+land.&ui_label=Tripolar)

- [unstructured](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured&issue_kind=%22Modify%22&validation_key=unstructured&description=Irregular+mesh+without+fixed+connectivity+pattern%2C+allowing+variable+resolution+and+complex+domain+boundaries.&ui_label=Unstructured)

- [unstructured_polygonal](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured_polygonal&issue_kind=%22Modify%22&validation_key=unstructured_polygonal&description=An+unstructured+mesh+consisting+of+arbitrary+polygons.&ui_label=Unstructured+Polygonal)

- [unstructured_quadrilateral](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured_quadrilateral&issue_kind=%22Modify%22&validation_key=unstructured_quadrilateral&description=An+unstructured+mesh+consisting+solely+of+quadrilaterals.&ui_label=Unstructured+Quadrilateral)

- [unstructured_triangular](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured_triangular&issue_kind=%22Modify%22&validation_key=unstructured_triangular&description=An+unstructured+mesh+consisting+solely+of+triangles.&ui_label=Unstructured+Triangular)

- [yin_yang](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+yin_yang&issue_kind=%22Modify%22&validation_key=yin_yang&description=Two+overlapping+grid+patches.&ui_label=Yin-Yang)

</details>

<details name="license">
<summary>License (4 entries)</summary>

- [CC BY 4.0](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=license.yml&title=Modify%3A+License%3A+CC+BY+4.0&issue_kind=%22Modify%22&validation_key=CC+BY+4.0&description=&ui_label=Creative+Commons+Attribution+4.0+International)

- [CC BY-NC-SA 4.0](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=license.yml&title=Modify%3A+License%3A+CC+BY-NC-SA+4.0&issue_kind=%22Modify%22&validation_key=CC+BY-NC-SA+4.0&description=&ui_label=Creative+Commons+Attribution-NonCommercial-ShareAlike+4.0+International)

- [CC BY-SA 4.0](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=license.yml&title=Modify%3A+License%3A+CC+BY-SA+4.0&issue_kind=%22Modify%22&validation_key=CC+BY-SA+4.0&description=&ui_label=Creative+Commons+Attribution-ShareAlike+4.0+International)

- [CC0 1.0](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=license.yml&title=Modify%3A+License%3A+CC0+1.0&issue_kind=%22Modify%22&validation_key=CC0+1.0&description=&ui_label=Creative+Commons+CC0+1.0+Universal+Public+Domain+Dedication)

</details>

<details name="mip">
<summary>Mip (4 entries)</summary>

- [CMIP5](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=mip.yml&title=Modify%3A+Mip%3A+CMIP5&issue_kind=%22Modify%22&validation_key=CMIP5&description=&ui_label=)

- [CMIP6Plus](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=mip.yml&title=Modify%3A+Mip%3A+CMIP6Plus&issue_kind=%22Modify%22&validation_key=CMIP6Plus&description=&ui_label=)

- [CMIP6](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=mip.yml&title=Modify%3A+Mip%3A+CMIP6&issue_kind=%22Modify%22&validation_key=CMIP6&description=&ui_label=)

- [CMIP7](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=mip.yml&title=Modify%3A+Mip%3A+CMIP7&issue_kind=%22Modify%22&validation_key=CMIP7&description=&ui_label=)

</details>

<details name="organisation">
<summary>Organisation (316 entries)</summary>

- [ACCESS-NRI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ACCESS-NRI&issue_kind=%22Modify%22&description=)

- [ACMAD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ACMAD&issue_kind=%22Modify%22&description=)

- [AEMET](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AEMET&issue_kind=%22Modify%22&description=)

- [AER](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AER&issue_kind=%22Modify%22&description=)

- [AMAP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AMAP&issue_kind=%22Modify%22&description=)

- [ANL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ANL&issue_kind=%22Modify%22&description=)

- [ANU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ANU&issue_kind=%22Modify%22&description=)

- [AORI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AORI&issue_kind=%22Modify%22&description=)

- [APCC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+APCC&issue_kind=%22Modify%22&description=)

- [ARCCSS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ARCCSS&issue_kind=%22Modify%22&description=)

- [AS-RCEC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AS-RCEC&issue_kind=%22Modify%22&description=)

- [ASMERC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ASMERC&issue_kind=%22Modify%22&description=)

- [AUoT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AUoT&issue_kind=%22Modify%22&description=)

- [AWI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AWI&issue_kind=%22Modify%22&description=)

- [AoR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+AoR&issue_kind=%22Modify%22&description=)

- [BAS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BAS&issue_kind=%22Modify%22&description=)

- [BCCR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BCCR&issue_kind=%22Modify%22&description=)

- [BCC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BCC&issue_kind=%22Modify%22&description=)

- [BIRA-IASB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BIRA-IASB&issue_kind=%22Modify%22&description=)

- [BNL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BNL&issue_kind=%22Modify%22&description=)

- [BNU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BNU&issue_kind=%22Modify%22&description=)

- [BOEM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BOEM&issue_kind=%22Modify%22&description=)

- [BOKU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BOKU&issue_kind=%22Modify%22&description=)

- [BlackRock](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+BlackRock&issue_kind=%22Modify%22&description=)

- [C-DAC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+C-DAC&issue_kind=%22Modify%22&description=)

- [CAMS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CAMS&issue_kind=%22Modify%22&description=)

- [CAS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CAS&issue_kind=%22Modify%22&description=)

- [CCCR-IITM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CCCR-IITM&issue_kind=%22Modify%22&description=)

- [CCCma](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CCCma&issue_kind=%22Modify%22&description=)

- [CCRS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CCRS&issue_kind=%22Modify%22&description=)

- [CEDA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CEDA&issue_kind=%22Modify%22&description=)

- [CEMA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CEMA&issue_kind=%22Modify%22&description=)

- [CEMC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CEMC&issue_kind=%22Modify%22&description=)

- [CEMIG](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CEMIG&issue_kind=%22Modify%22&description=)

- [CERFACS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CERFACS&issue_kind=%22Modify%22&description=)

- [CESDAC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CESDAC&issue_kind=%22Modify%22&description=)

- [CETESB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CETESB&issue_kind=%22Modify%22&description=)

- [CGISC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CGISC&issue_kind=%22Modify%22&description=)

- [CGI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CGI&issue_kind=%22Modify%22&description=)

- [CIAT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CIAT&issue_kind=%22Modify%22&description=)

- [CICERO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CICERO&issue_kind=%22Modify%22&description=)

- [CICESE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CICESE&issue_kind=%22Modify%22&description=)

- [CIMA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CIMA&issue_kind=%22Modify%22&description=)

- [CLEX](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CLEX&issue_kind=%22Modify%22&description=)

- [CMA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CMA&issue_kind=%22Modify%22&description=)

- [CMCC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CMCC&issue_kind=%22Modify%22&description=)

- [CMIP-IPO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CMIP-IPO&issue_kind=%22Modify%22&description=)

- [CNES](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CNES&issue_kind=%22Modify%22&description=)

- [CNRM-CERFACS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CNRM-CERFACS&issue_kind=%22Modify%22&description=)

- [CNRM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CNRM&issue_kind=%22Modify%22&description=)

- [CNRS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CNRS&issue_kind=%22Modify%22&description=)

- [CNR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CNR&issue_kind=%22Modify%22&description=)

- [COLA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+COLA&issue_kind=%22Modify%22&description=)

- [COMSATS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+COMSATS&issue_kind=%22Modify%22&description=)

- [CREAF](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CREAF&issue_kind=%22Modify%22&description=)

- [CR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CR&issue_kind=%22Modify%22&description=)

- [CSC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CSC&issue_kind=%22Modify%22&description=)

- [CSIC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CSIC&issue_kind=%22Modify%22&description=)

- [CSIR-Wits-CSIRO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CSIR-Wits-CSIRO&issue_kind=%22Modify%22&description=)

- [CSIRO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CSIRO&issue_kind=%22Modify%22&description=)

- [CSIR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CSIR&issue_kind=%22Modify%22&description=)

- [CUG](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CUG&issue_kind=%22Modify%22&description=)

- [CU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+CU&issue_kind=%22Modify%22&description=)

- [Caltech](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+Caltech&issue_kind=%22Modify%22&description=)

- [Cineca](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+Cineca&issue_kind=%22Modify%22&description=)

- [DESNZ](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DESNZ&issue_kind=%22Modify%22&description=)

- [DIAS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DIAS&issue_kind=%22Modify%22&description=)

- [DKRZ](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DKRZ&issue_kind=%22Modify%22&description=)

- [DLR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DLR&issue_kind=%22Modify%22&description=)

- [DMI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DMI&issue_kind=%22Modify%22&description=)

- [DSIT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DSIT&issue_kind=%22Modify%22&description=)

- [DTU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DTU&issue_kind=%22Modify%22&description=)

- [DWD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+DWD&issue_kind=%22Modify%22&description=)

- [E3SM-Project](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+E3SM-Project&issue_kind=%22Modify%22&description=)

- [EAWAG](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+EAWAG&issue_kind=%22Modify%22&description=)

- [EC-Earth-Consortium](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+EC-Earth-Consortium&issue_kind=%22Modify%22&description=)

- [ECCC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ECCC&issue_kind=%22Modify%22&description=)

- [ECMWF](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ECMWF&issue_kind=%22Modify%22&description=)

- [EDF](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+EDF&issue_kind=%22Modify%22&description=)

- [ENS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ENS&issue_kind=%22Modify%22&description=)

- [ENVEO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ENVEO&issue_kind=%22Modify%22&description=)

- [ESA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ESA&issue_kind=%22Modify%22&description=)

- [ESCWA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ESCWA&issue_kind=%22Modify%22&description=)

- [ESSO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ESSO&issue_kind=%22Modify%22&description=)

- [ESSTI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ESSTI&issue_kind=%22Modify%22&description=)

- [Empa](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+Empa&issue_kind=%22Modify%22&description=)

- [FACET](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FACET&issue_kind=%22Modify%22&description=)

- [FAO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FAO&issue_kind=%22Modify%22&description=)

- [FIO-QLNM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FIO-QLNM&issue_kind=%22Modify%22&description=)

- [FIO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FIO&issue_kind=%22Modify%22&description=)

- [FMI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FMI&issue_kind=%22Modify%22&description=)

- [FSU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FSU&issue_kind=%22Modify%22&description=)

- [FUB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FUB&issue_kind=%22Modify%22&description=)

- [FUBerlin](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FUBerlin&issue_kind=%22Modify%22&description=)

- [FZJ](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+FZJ&issue_kind=%22Modify%22&description=)

- [Fidelidade](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+Fidelidade&issue_kind=%22Modify%22&description=)

- [GCISC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+GCISC&issue_kind=%22Modify%22&description=)

- [GERICS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+GERICS&issue_kind=%22Modify%22&description=)

- [GMU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+GMU&issue_kind=%22Modify%22&description=)

- [GTI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+GTI&issue_kind=%22Modify%22&description=)

- [HEREON](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+HEREON&issue_kind=%22Modify%22&description=)

- [HKUST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+HKUST&issue_kind=%22Modify%22&description=)

- [HUJI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+HUJI&issue_kind=%22Modify%22&description=)

- [IAA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IAA&issue_kind=%22Modify%22&description=)

- [IACETH](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IACETH&issue_kind=%22Modify%22&description=)

- [IAP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IAP&issue_kind=%22Modify%22&description=)

- [ICAR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ICAR&issue_kind=%22Modify%22&description=)

- [ICHEC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ICHEC&issue_kind=%22Modify%22&description=)

- [ICTP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ICTP&issue_kind=%22Modify%22&description=)

- [IDRC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IDRC&issue_kind=%22Modify%22&description=)

- [IEK](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IEK&issue_kind=%22Modify%22&description=)

- [IFCA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IFCA&issue_kind=%22Modify%22&description=)

- [IFM-GEOMAR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IFM-GEOMAR&issue_kind=%22Modify%22&description=)

- [IFREMER](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IFREMER&issue_kind=%22Modify%22&description=)

- [IGCI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IGCI&issue_kind=%22Modify%22&description=)

- [IIASA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IIASA&issue_kind=%22Modify%22&description=)

- [IIHS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IIHS&issue_kind=%22Modify%22&description=)

- [IISER](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IISER&issue_kind=%22Modify%22&description=)

- [IIS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IIS&issue_kind=%22Modify%22&description=)

- [IITM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IITM&issue_kind=%22Modify%22&description=)

- [IIT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IIT&issue_kind=%22Modify%22&description=)

- [INGV](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+INGV&issue_kind=%22Modify%22&description=)

- [INMET](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+INMET&issue_kind=%22Modify%22&description=)

- [INM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+INM&issue_kind=%22Modify%22&description=)

- [INPA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+INPA&issue_kind=%22Modify%22&description=)

- [INPE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+INPE&issue_kind=%22Modify%22&description=)

- [INRAE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+INRAE&issue_kind=%22Modify%22&description=)

- [IOW](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IOW&issue_kind=%22Modify%22&description=)

- [IPCC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IPCC&issue_kind=%22Modify%22&description=)

- [IPSL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IPSL&issue_kind=%22Modify%22&description=)

- [IRD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IRD&issue_kind=%22Modify%22&description=)

- [ISDR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ISDR&issue_kind=%22Modify%22&description=)

- [ISM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ISM&issue_kind=%22Modify%22&description=)

- [ISSI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ISSI&issue_kind=%22Modify%22&description=)

- [IST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+IST&issue_kind=%22Modify%22&description=)

- [ISU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ISU&issue_kind=%22Modify%22&description=)

- [ITM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ITM&issue_kind=%22Modify%22&description=)

- [ImperialCollege](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ImperialCollege&issue_kind=%22Modify%22&description=)

- [JAMSTEC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+JAMSTEC&issue_kind=%22Modify%22&description=)

- [JAXA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+JAXA&issue_kind=%22Modify%22&description=)

- [JCU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+JCU&issue_kind=%22Modify%22&description=)

- [JGCRI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+JGCRI&issue_kind=%22Modify%22&description=)

- [KAIST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KAIST&issue_kind=%22Modify%22&description=)

- [KAUST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KAUST&issue_kind=%22Modify%22&description=)

- [KCL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KCL&issue_kind=%22Modify%22&description=)

- [KIOST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KIOST&issue_kind=%22Modify%22&description=)

- [KIT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KIT&issue_kind=%22Modify%22&description=)

- [KMA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KMA&issue_kind=%22Modify%22&description=)

- [KNMI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KNMI&issue_kind=%22Modify%22&description=)

- [KSU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+KSU&issue_kind=%22Modify%22&description=)

- [LANL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LANL&issue_kind=%22Modify%22&description=)

- [LBNL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LBNL&issue_kind=%22Modify%22&description=)

- [LLNL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LLNL&issue_kind=%22Modify%22&description=)

- [LMD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LMD&issue_kind=%22Modify%22&description=)

- [LMU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LMU&issue_kind=%22Modify%22&description=)

- [LPC2E](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LPC2E&issue_kind=%22Modify%22&description=)

- [LSCE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LSCE&issue_kind=%22Modify%22&description=)

- [LSE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LSE&issue_kind=%22Modify%22&description=)

- [LSHTM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LSHTM&issue_kind=%22Modify%22&description=)

- [LSU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LSU&issue_kind=%22Modify%22&description=)

- [LiU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+LiU&issue_kind=%22Modify%22&description=)

- [MARN](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MARN&issue_kind=%22Modify%22&description=)

- [MEXT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MEXT&issue_kind=%22Modify%22&description=)

- [MIROC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MIROC&issue_kind=%22Modify%22&description=)

- [MIT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MIT&issue_kind=%22Modify%22&description=)

- [MOHC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MOHC&issue_kind=%22Modify%22&description=)

- [MPI-BGC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MPI-BGC&issue_kind=%22Modify%22&description=)

- [MPI-B](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MPI-B&issue_kind=%22Modify%22&description=)

- [MPI-C](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MPI-C&issue_kind=%22Modify%22&description=)

- [MPI-G](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MPI-G&issue_kind=%22Modify%22&description=)

- [MPI-M](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MPI-M&issue_kind=%22Modify%22&description=)

- [MPS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MPS&issue_kind=%22Modify%22&description=)

- [MRI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MRI&issue_kind=%22Modify%22&description=)

- [MTU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+MTU&issue_kind=%22Modify%22&description=)

- [NASA-GISS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NASA-GISS&issue_kind=%22Modify%22&description=)

- [NASA-GSFC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NASA-GSFC&issue_kind=%22Modify%22&description=)

- [NASA-JPL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NASA-JPL&issue_kind=%22Modify%22&description=)

- [NASA-LaRC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NASA-LaRC&issue_kind=%22Modify%22&description=)

- [NASA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NASA&issue_kind=%22Modify%22&description=)

- [NAU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NAU&issue_kind=%22Modify%22&description=)

- [NCAR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCAR&issue_kind=%22Modify%22&description=)

- [NCAS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCAS&issue_kind=%22Modify%22&description=)

- [NCC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCC&issue_kind=%22Modify%22&description=)

- [NCEO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCEO&issue_kind=%22Modify%22&description=)

- [NCEP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCEP&issue_kind=%22Modify%22&description=)

- [NCI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCI&issue_kind=%22Modify%22&description=)

- [NCM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCM&issue_kind=%22Modify%22&description=)

- [NCState](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NCState&issue_kind=%22Modify%22&description=)

- [NERC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NERC&issue_kind=%22Modify%22&description=)

- [NERSC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NERSC&issue_kind=%22Modify%22&description=)

- [NIES](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NIES&issue_kind=%22Modify%22&description=)

- [NILU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NILU&issue_kind=%22Modify%22&description=)

- [NIMR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NIMR&issue_kind=%22Modify%22&description=)

- [NIMS-KMA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NIMS-KMA&issue_kind=%22Modify%22&description=)

- [NIMS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NIMS&issue_kind=%22Modify%22&description=)

- [NIWA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NIWA&issue_kind=%22Modify%22&description=)

- [NLR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NLR&issue_kind=%22Modify%22&description=)

- [NOAA-GFDL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NOAA-GFDL&issue_kind=%22Modify%22&description=)

- [NOAA-NCEI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NOAA-NCEI&issue_kind=%22Modify%22&description=)

- [NOAA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NOAA&issue_kind=%22Modify%22&description=)

- [NOA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NOA&issue_kind=%22Modify%22&description=)

- [NOC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NOC&issue_kind=%22Modify%22&description=)

- [NORCE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NORCE&issue_kind=%22Modify%22&description=)

- [NRL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NRL&issue_kind=%22Modify%22&description=)

- [NSF](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NSF&issue_kind=%22Modify%22&description=)

- [NTNU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NTNU&issue_kind=%22Modify%22&description=)

- [NTU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NTU&issue_kind=%22Modify%22&description=)

- [NUIST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NUIST&issue_kind=%22Modify%22&description=)

- [NUI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NUI&issue_kind=%22Modify%22&description=)

- [NYU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+NYU&issue_kind=%22Modify%22&description=)

- [OGS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+OGS&issue_kind=%22Modify%22&description=)

- [OJERI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+OJERI&issue_kind=%22Modify%22&description=)

- [ORNL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ORNL&issue_kind=%22Modify%22&description=)

- [OSU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+OSU&issue_kind=%22Modify%22&description=)

- [Ouranos](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+Ouranos&issue_kind=%22Modify%22&description=)

- [PAUWES](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PAUWES&issue_kind=%22Modify%22&description=)

- [PBL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PBL&issue_kind=%22Modify%22&description=)

- [PCMDI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PCMDI&issue_kind=%22Modify%22&description=)

- [PIK](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PIK&issue_kind=%22Modify%22&description=)

- [PMAS-AAUR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PMAS-AAUR&issue_kind=%22Modify%22&description=)

- [PML](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PML&issue_kind=%22Modify%22&description=)

- [PMOD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PMOD&issue_kind=%22Modify%22&description=)

- [PNNL-JGCRI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PNNL-JGCRI&issue_kind=%22Modify%22&description=)

- [PNNL-WACCEM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PNNL-WACCEM&issue_kind=%22Modify%22&description=)

- [PNNL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PNNL&issue_kind=%22Modify%22&description=)

- [PNU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+PNU&issue_kind=%22Modify%22&description=)

- [QCCCE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+QCCCE&issue_kind=%22Modify%22&description=)

- [QLNM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+QLNM&issue_kind=%22Modify%22&description=)

- [R-CCS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+R-CCS&issue_kind=%22Modify%22&description=)

- [RAL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+RAL&issue_kind=%22Modify%22&description=)

- [RCEC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+RCEC&issue_kind=%22Modify%22&description=)

- [RSS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+RSS&issue_kind=%22Modify%22&description=)

- [RU-CORE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+RU-CORE&issue_kind=%22Modify%22&description=)

- [RWE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+RWE&issue_kind=%22Modify%22&description=)

- [SAL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SAL&issue_kind=%22Modify%22&description=)

- [SJSU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SJSU&issue_kind=%22Modify%22&description=)

- [SKYE](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SKYE&issue_kind=%22Modify%22&description=)

- [SMHI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SMHI&issue_kind=%22Modify%22&description=)

- [SMU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SMU&issue_kind=%22Modify%22&description=)

- [SNU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SNU&issue_kind=%22Modify%22&description=)

- [SOLARIS HEPPA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SOLARIS+HEPPA&issue_kind=%22Modify%22&description=)

- [STFC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+STFC&issue_kind=%22Modify%22&description=)

- [SWP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+SWP&issue_kind=%22Modify%22&description=)

- [TAMU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TAMU&issue_kind=%22Modify%22&description=)

- [TERI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TERI&issue_kind=%22Modify%22&description=)

- [THU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+THU&issue_kind=%22Modify%22&description=)

- [TMA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TMA&issue_kind=%22Modify%22&description=)

- [TROPOS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TROPOS&issue_kind=%22Modify%22&description=)

- [TUBITAK](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TUBITAK&issue_kind=%22Modify%22&description=)

- [TUDelft](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TUDelft&issue_kind=%22Modify%22&description=)

- [TUM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TUM&issue_kind=%22Modify%22&description=)

- [TUW](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TUW&issue_kind=%22Modify%22&description=)

- [TWP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TWP&issue_kind=%22Modify%22&description=)

- [TenneT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+TenneT&issue_kind=%22Modify%22&description=)

- [UAAR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UAAR&issue_kind=%22Modify%22&description=)

- [UAH](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UAH&issue_kind=%22Modify%22&description=)

- [UAL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UAL&issue_kind=%22Modify%22&description=)

- [UA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UA&issue_kind=%22Modify%22&description=)

- [UBA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UBA&issue_kind=%22Modify%22&description=)

- [UBC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UBC&issue_kind=%22Modify%22&description=)

- [UCAD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCAD&issue_kind=%22Modify%22&description=)

- [UCAR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCAR&issue_kind=%22Modify%22&description=)

- [UCBerkeley](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCBerkeley&issue_kind=%22Modify%22&description=)

- [UCI](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCI&issue_kind=%22Modify%22&description=)

- [UCLA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCLA&issue_kind=%22Modify%22&description=)

- [UCL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCL&issue_kind=%22Modify%22&description=)

- [UCLouvain](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCLouvain&issue_kind=%22Modify%22&description=)

- [UCM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCM&issue_kind=%22Modify%22&description=)

- [UCRiverside](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCRiverside&issue_kind=%22Modify%22&description=)

- [UCSB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCSB&issue_kind=%22Modify%22&description=)

- [UCSC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCSC&issue_kind=%22Modify%22&description=)

- [UCSD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCSD&issue_kind=%22Modify%22&description=)

- [UCT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UCT&issue_kind=%22Modify%22&description=)

- [UColorado](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UColorado&issue_kind=%22Modify%22&description=)

- [UEA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UEA&issue_kind=%22Modify%22&description=)

- [UERJ](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UERJ&issue_kind=%22Modify%22&description=)

- [UFRN](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UFRN&issue_kind=%22Modify%22&description=)

- [UFZ](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UFZ&issue_kind=%22Modify%22&description=)

- [UGA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UGA&issue_kind=%22Modify%22&description=)

- [UHH](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UHH&issue_kind=%22Modify%22&description=)

- [UIUC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UIUC&issue_kind=%22Modify%22&description=)

- [UKCEH](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UKCEH&issue_kind=%22Modify%22&description=)

- [ULB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+ULB&issue_kind=%22Modify%22&description=)

- [UMN](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UMN&issue_kind=%22Modify%22&description=)

- [UNIPAMPA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UNIPAMPA&issue_kind=%22Modify%22&description=)

- [UNIST](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UNIST&issue_kind=%22Modify%22&description=)

- [UNSTIM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UNSTIM&issue_kind=%22Modify%22&description=)

- [UNSW](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UNSW&issue_kind=%22Modify%22&description=)

- [UReading](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UReading&issue_kind=%22Modify%22&description=)

- [USD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+USD&issue_kind=%22Modify%22&description=)

- [USGS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+USGS&issue_kind=%22Modify%22&description=)

- [UTAS](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UTAS&issue_kind=%22Modify%22&description=)

- [UTAustin](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UTAustin&issue_kind=%22Modify%22&description=)

- [UU](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UU&issue_kind=%22Modify%22&description=)

- [UW](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UW&issue_kind=%22Modify%22&description=)

- [UiB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UiB&issue_kind=%22Modify%22&description=)

- [UiO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UiO&issue_kind=%22Modify%22&description=)

- [UoBergen](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoBergen&issue_kind=%22Modify%22&description=)

- [UoH](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoH&issue_kind=%22Modify%22&description=)

- [UoLeeds](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoLeeds&issue_kind=%22Modify%22&description=)

- [UoM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoM&issue_kind=%22Modify%22&description=)

- [UoMontreal](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoMontreal&issue_kind=%22Modify%22&description=)

- [UoOtago](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoOtago&issue_kind=%22Modify%22&description=)

- [UoOulu](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoOulu&issue_kind=%22Modify%22&description=)

- [UoSask](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UoSask&issue_kind=%22Modify%22&description=)

- [UofMD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UofMD&issue_kind=%22Modify%22&description=)

- [UofT](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+UofT&issue_kind=%22Modify%22&description=)

- [VUA](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+VUA&issue_kind=%22Modify%22&description=)

- [WCRC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+WCRC&issue_kind=%22Modify%22&description=)

- [WCRP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+WCRP&issue_kind=%22Modify%22&description=)

- [WMO](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+WMO&issue_kind=%22Modify%22&description=)

- [WSL](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+WSL&issue_kind=%22Modify%22&description=)

- [WUR](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+WUR&issue_kind=%22Modify%22&description=)

- [WWRP](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+WWRP&issue_kind=%22Modify%22&description=)

- [Wits](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+Wits&issue_kind=%22Modify%22&description=)

- [uOttawa](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=organisation.yml&title=Modify%3A+Organisation%3A+uOttawa&issue_kind=%22Modify%22&description=)

</details>

<details name="product">
<summary>Product (4 entries)</summary>

- [derived](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=product.yml&title=Modify%3A+Product%3A+derived&issue_kind=%22Modify%22&validation_key=derived&description=Data+that+has+been+processed+or+transformed+from+raw+model+output.+Derived+data+includes+value-added+products+such+as+anomalies%2C+indices%2C+or+other+statistics+that+are+computed+from+the+original+model+outputs.&ui_label=)

- [forcing-dataset](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=product.yml&title=Modify%3A+Product%3A+forcing-dataset&issue_kind=%22Modify%22&validation_key=forcing-dataset&description=Data+sets+used+to+drive+model+simulations.+These+include+external+factors+like+greenhouse+gas+concentrations%2C+solar+radiation%2C+and+land+use+changes+that+influence+the+climate+model+outputs.&ui_label=)

- [model-output](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=product.yml&title=Modify%3A+Product%3A+model-output&issue_kind=%22Modify%22&validation_key=model-output&description=Output+produced+from+a+model+simulation.+This+includes+the+various+data+points+and+metrics+generated+as+a+result+of+running+climate+models%2C+which+simulate+physical%2C+chemical%2C+and+biological+processes+affecting+the+climate+system.&ui_label=)

- [observations](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=product.yml&title=Modify%3A+Product%3A+observations&issue_kind=%22Modify%22&validation_key=observations&description=Data+collected+from+direct+measurements+of+the+climate+system.+This+includes+data+from+ground+stations%2C+satellites%2C+buoys%2C+and+other+observational+platforms%2C+which+serve+as+a+reference+for+validating+and+comparing+model+outputs.&ui_label=)

</details>

<details name="region">
<summary>Region (10 entries)</summary>

- [30s-90s](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+30s-90s&issue_kind=%22Modify%22&validation_key=30s-90s&description=The+geographical+region+of+the+Earth%27s+surface+between+30+and+90+degrees+south.&ui_label=30S-90S)

- [antarctica](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+antarctica&issue_kind=%22Modify%22&validation_key=antarctica&description=Located+around+the+South+Pole%2C+separated+from+other+land+masses+by+the+Southern+Ocean%2C+and+almost+entirely+south+of+60+degrees+South+latitude.&ui_label=Antarctica)

- [arctic](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+arctic&issue_kind=%22Modify%22&validation_key=arctic&description=The+polar+region+surrounding+the+North+Pole%2C+typically+defined+as+north+of+the+Arctic+Circle+%2866.5%C2%B0N%29+or+north+of+60%C2%B0N+latitude.&ui_label=Arctic)

- [global](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+global&issue_kind=%22Modify%22&validation_key=global&description=The+complete+Earth+surface%2C+90+degrees+North+to+90+degrees+South+latitude%2C+and+all+longitudes.&ui_label=Global)

- [greenland](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+greenland&issue_kind=%22Modify%22&validation_key=greenland&description=Located+in+the+Northern+Atlantic+Ocean%2C+separated+from+other+land+masses+by+the+Labrador+Sea+and+Straits%2C+and+almost+entirely+north+of+60+degrees+North+latitude.&ui_label=Greenland)

- [limited-area](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+limited-area&issue_kind=%22Modify%22&validation_key=limited-area&description=Any+contiguous+subregion+of+the+Earth%27s+surface%2C+used+to+indicate+a+limited+area+model+that+may+be+placed+over+different+geographical+regions+independently+of+the+model+formulation.&ui_label=Limited+Area)

- [northern_hemisphere](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+northern_hemisphere&issue_kind=%22Modify%22&validation_key=northern_hemisphere&description=The+complete+Earth+surface+from+the+equator+to+the+North+Pole%2C+0+to+90+degrees+North+latitude.&ui_label=Northern+Hemisphere)

- [shem](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+shem&issue_kind=%22Modify%22&validation_key=shem&description=the+complete+Earth+surface+from+the+equator+to+the+South+Pole%2C+0+to+90+degrees+South+latitude&ui_label=Southern+Hemisphere)

- [southern_hemisphere](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+southern_hemisphere&issue_kind=%22Modify%22&validation_key=southern_hemisphere&description=The+complete+Earth+surface+from+the+equator+to+the+South+Pole%2C+0+to+90+degrees+South+latitude.&ui_label=Southern+Hemisphere)

- [tropics](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=region.yml&title=Modify%3A+Region%3A+tropics&issue_kind=%22Modify%22&validation_key=tropics&description=The+tropical+region+between+23.5+degrees+North+and+23.5+degrees+South+latitude%2C+bounded+by+the+Tropic+of+Cancer+and+Tropic+of+Capricorn.&ui_label=Tropics)

</details>

<details name="resolution">
<summary>Resolution (15 entries)</summary>

- [0.5 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+0.5+km&issue_kind=%22Modify%22&validation_key=0.5+km&description=Resolution+of+0.5+km&ui_label=)

- [1 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+1+km&issue_kind=%22Modify%22&validation_key=1+km&description=Resolution+of+1+km&ui_label=)

- [10 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+10+km&issue_kind=%22Modify%22&validation_key=10+km&description=Resolution+of+10+km&ui_label=)

- [100 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+100+km&issue_kind=%22Modify%22&validation_key=100+km&description=Resolution+of+100+km&ui_label=)

- [1000 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+1000+km&issue_kind=%22Modify%22&validation_key=1000+km&description=Resolution+of+1000+km&ui_label=)

- [10000 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+10000+km&issue_kind=%22Modify%22&validation_key=10000+km&description=Resolution+of+10000+km&ui_label=)

- [1x1 degree](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+1x1+degree&issue_kind=%22Modify%22&validation_key=1x1+degree&description=Resolution+of+1x1+degree&ui_label=)

- [2.5 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+2.5+km&issue_kind=%22Modify%22&validation_key=2.5+km&description=Resolution+of+2.5+km&ui_label=)

- [25 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+25+km&issue_kind=%22Modify%22&validation_key=25+km&description=Resolution+of+25+km&ui_label=)

- [250 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+250+km&issue_kind=%22Modify%22&validation_key=250+km&description=Resolution+of+250+km&ui_label=)

- [2500 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+2500+km&issue_kind=%22Modify%22&validation_key=2500+km&description=Resolution+of+2500+km&ui_label=)

- [5 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+5+km&issue_kind=%22Modify%22&validation_key=5+km&description=Resolution+of+5+km&ui_label=)

- [50 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+50+km&issue_kind=%22Modify%22&validation_key=50+km&description=Resolution+of+50+km&ui_label=)

- [500 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+500+km&issue_kind=%22Modify%22&validation_key=500+km&description=Resolution+of+500+km&ui_label=)

- [5000 km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+5000+km&issue_kind=%22Modify%22&validation_key=5000+km&description=Resolution+of+5000+km&ui_label=)

</details>

<details name="scientific_domain">
<summary>Scientific Domain (8 entries)</summary>

- [aerosol](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+aerosol&issue_kind=%22Modify%22&validation_key=aerosol&alias=aerosol&description=Aerosol&ui_label=Aerosol)

- [atmosphere](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+atmosphere&issue_kind=%22Modify%22&validation_key=atmosphere&alias=atmos&description=Atmosphere&ui_label=Atmosphere)

- [atmospheric_chemistry](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+atmospheric_chemistry&issue_kind=%22Modify%22&validation_key=atmospheric_chemistry&alias=atmoschem%2C+atmosChem&description=Atmospheric+Chemistry&ui_label=Atmospheric+Chemistry)

- [land_ice](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+land_ice&issue_kind=%22Modify%22&validation_key=land_ice&alias=landice%2C+landIce&description=Land+Ice&ui_label=Land+Ice)

- [land_surface](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+land_surface&issue_kind=%22Modify%22&validation_key=land_surface&alias=land&description=Land+Surface+and+Subsurface&ui_label=Land+Surface+and+Subsurface)

- [ocean](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+ocean&issue_kind=%22Modify%22&validation_key=ocean&alias=ocean&description=Ocean&ui_label=Ocean)

- [ocean_biogeochemistry](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+ocean_biogeochemistry&issue_kind=%22Modify%22&validation_key=ocean_biogeochemistry&alias=ocnbgchem%2C+ocnBgchem&description=Ocean+Biogeochemistry&ui_label=Ocean+Biogeochemistry)

- [sea_ice](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+sea_ice&issue_kind=%22Modify%22&validation_key=sea_ice&alias=seaice%2C+seaIce&description=Sea+Ice&ui_label=Sea+Ice)

</details>

<details name="source_type">
<summary>Source Type (14 entries)</summary>

- [AER](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+AER&issue_kind=%22Modify%22&validation_key=AER&description=aerosol+treatment+in+an+atmospheric+model+where+concentrations+are+calculated+based+on+emissions%2C+transformation%2C+and+removal+processes+%28rather+than+being+prescribed+or+omitted+entirely%29&ui_label=)

- [AGCM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+AGCM&issue_kind=%22Modify%22&validation_key=AGCM&description=atmospheric+general+circulation+model+run+with+prescribed+ocean+surface+conditions+and+usually+a+model+of+the+land+surface&ui_label=)

- [AOGCM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+AOGCM&issue_kind=%22Modify%22&validation_key=AOGCM&description=coupled+atmosphere-ocean+global+climate+model%2C+additionally+including+explicit+representation+of+at+least+the+land+and+sea+ice&ui_label=)

- [BGC](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+BGC&issue_kind=%22Modify%22&validation_key=BGC&description=biogeochemistry+model+component+that+at+the+very+least+accounts+for+carbon+reservoirs+and+fluxes+in+the+atmosphere%2C+terrestrial+biosphere%2C+and+ocean&ui_label=)

- [CHEM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+CHEM&issue_kind=%22Modify%22&validation_key=CHEM&description=chemistry+treatment+in+an+atmospheric+model+that+calculates+atmospheric+oxidant+concentrations+%28including+at+least+ozone%29%2C+rather+than+prescribing+them&ui_label=)

- [ISM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+ISM&issue_kind=%22Modify%22&validation_key=ISM&description=ice-sheet+model+that+includes+ice-flow&ui_label=)

- [LAND](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+LAND&issue_kind=%22Modify%22&validation_key=LAND&description=land+model+run+uncoupled+from+the+atmosphere&ui_label=)

- [OGCM](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+OGCM&issue_kind=%22Modify%22&validation_key=OGCM&description=ocean+general+circulation+model+run+uncoupled+from+an+AGCM+but%2C+usually+including+a+sea-ice+model&ui_label=)

- [RAD](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+RAD&issue_kind=%22Modify%22&validation_key=RAD&description=radiation+component+of+an+atmospheric+model+run+%27offline%27&ui_label=)

- [SLAB](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+SLAB&issue_kind=%22Modify%22&validation_key=SLAB&description=slab-ocean+used+with+an+AGCM+in+representing+the+atmosphere-ocean+coupled+system&ui_label=)

- [gridded_insitu](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+gridded_insitu&issue_kind=%22Modify%22&validation_key=gridded_insitu&description=gridded+product+based+on+measurements+collected+from+in-situ+instruments&ui_label=)

- [reanalysis](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+reanalysis&issue_kind=%22Modify%22&validation_key=reanalysis&description=gridded+product+generated+from+a+model+reanalysis+based+on+in-situ+instruments+and+possibly+satellite+measurements&ui_label=)

- [satellite_blended](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+satellite_blended&issue_kind=%22Modify%22&validation_key=satellite_blended&description=gridded+product+based+on+both+in-situ+instruments+and+satellite+measurements&ui_label=)

- [satellite_retrieval](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+satellite_retrieval&issue_kind=%22Modify%22&validation_key=satellite_retrieval&description=gridded+product+based+on+satellite+measurements&ui_label=)

</details>

<details name="temporal_refinement">
<summary>Temporal Refinement (3 entries)</summary>

- [adaptive](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=temporal_refinement.yml&title=Modify%3A+Temporal+Refinement%3A+adaptive&issue_kind=%22Modify%22&validation_key=adaptive&description=Grid+resolution+changes+dynamically+during+the+simulation+based+on+solution+features.&ui_label=Adaptive)

- [dynamically_stretched](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=temporal_refinement.yml&title=Modify%3A+Temporal+Refinement%3A+dynamically_stretched&issue_kind=%22Modify%22&validation_key=dynamically_stretched&description=The+total+number+of+grid+points+stays+constant%2C+but+grid+points+can+be+dynamically+relocated.&ui_label=Dynamically+Stretched)

- [static](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=temporal_refinement.yml&title=Modify%3A+Temporal+Refinement%3A+static&issue_kind=%22Modify%22&validation_key=static&description=Grid+resolution+remains+constant+throughout+the+simulation.&ui_label=Static)

</details>

<details name="truncation_method">
<summary>Truncation Method (2 entries)</summary>

- [rhomboidal](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=truncation_method.yml&title=Modify%3A+Truncation+Method%3A+rhomboidal&issue_kind=%22Modify%22&validation_key=rhomboidal&description=Rhomboidal+truncation+in+spectral+space+where+%7Cm%7C+%E2%89%A4+M+and+%7Cn-m%7C+%E2%89%A4+N.+Provides+more+uniform+resolution+across+latitudes+than+triangular+truncation.&ui_label=Rhomboidal+Truncation)

- [triangular](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=truncation_method.yml&title=Modify%3A+Truncation+Method%3A+triangular&issue_kind=%22Modify%22&validation_key=triangular&description=Triangular+truncation+in+spectral+space+where+total+wavenumber+m%2Bn+%E2%89%A4+N.+Common+notation%3A+TL+%28triangular+linear%29+or+TQ+%28triangular+quadratic%29.&ui_label=Triangular+Truncation)

</details>

<details name="units">
<summary>Units (5 entries)</summary>

- [degree](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=units.yml&title=Modify%3A+Units%3A+degree&issue_kind=%22Modify%22&validation_key=degree&description=Angular+measurement+in+degrees+for+latitude%2Flongitude+coordinates.&ui_label=Degrees)

- [k](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=units.yml&title=Modify%3A+Units%3A+k&issue_kind=%22Modify%22&validation_key=k&description=Unit+for+temperature.&ui_label=Kelvin)

- [km](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=units.yml&title=Modify%3A+Units%3A+km&issue_kind=%22Modify%22&validation_key=km&description=Kilometre+%28unit+for+length%29.&ui_label=Kilometre)

- [meter](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=units.yml&title=Modify%3A+Units%3A+meter&issue_kind=%22Modify%22&validation_key=meter&description=Distance+measurement+in+meters+for+projected+coordinate+systems.&ui_label=Meters)

- [pa](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=units.yml&title=Modify%3A+Units%3A+pa&issue_kind=%22Modify%22&validation_key=pa&description=Unit+for+pressure.&ui_label=Pascal)

</details>

<details name="vertical_coordinate">
<summary>Vertical Coordinate (20 entries)</summary>

- [air_potential_temperature](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+air_potential_temperature&issue_kind=%22Modify%22&validation_key=air_potential_temperature&description=Air+potential+temperature+is+the+temperature+a+parcel+of+air+would+have+if+moved+dry+adiabatically+to+a+standard+pressure%2C+as+defined+by+the+CF+conventions.&ui_label=Air+Potential+Temperature)

- [air_pressure](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+air_pressure&issue_kind=%22Modify%22&validation_key=air_pressure&description=Air+pressure+is+the+pressure+that+exists+in+the+medium+of+air%2C+as+defined+by+the+CF+conventions.&ui_label=Air+Pressure)

- [atmosphere_hybrid_height_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere_hybrid_height_coordinate&issue_kind=%22Modify%22&validation_key=atmosphere_hybrid_height_coordinate&description=Parametric+atmosphere+hybrid+height+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Hybrid+Height+Coordinate)

- [atmosphere_hybrid_sigma_pressure_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere_hybrid_sigma_pressure_coordinate&issue_kind=%22Modify%22&validation_key=atmosphere_hybrid_sigma_pressure_coordinate&description=Parametric+atmosphere+hybrid+sigma+pressure+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Hybrid+Sigma+Pressure+Coordinate)

- [atmosphere_ln_pressure_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere_ln_pressure_coordinate&issue_kind=%22Modify%22&validation_key=atmosphere_ln_pressure_coordinate&description=Parametric+atmosphere+natural+log+pressure+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Ln+Pressure+Coordinate)

- [atmosphere_sigma_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere_sigma_coordinate&issue_kind=%22Modify%22&validation_key=atmosphere_sigma_coordinate&description=Parametric+atmosphere+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Sigma+Coordinate)

- [atmosphere_sleve_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere_sleve_coordinate&issue_kind=%22Modify%22&validation_key=atmosphere_sleve_coordinate&description=Parametric+atmosphere+smooth+vertical+level+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+SLEVE+Coordinate)

- [depth](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+depth&issue_kind=%22Modify%22&validation_key=depth&description=Vertical+distance+below+a+reference+surface+%28e.g.%2C+sea+surface%2C+land+surface%29.&ui_label=Depth)

- [geopotential_height](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+geopotential_height&issue_kind=%22Modify%22&validation_key=geopotential_height&description=Geopotential+height+is+the+geopotential+divided+by+the+standard+acceleration+due+to+gravity%2C+as+defined+by+the+CF+conventions.&ui_label=Geopotential+Height)

- [height](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+height&issue_kind=%22Modify%22&validation_key=height&description=Vertical+distance+above+a+reference+surface.&ui_label=Height)

- [land_ice_sigma_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+land_ice_sigma_coordinate&issue_kind=%22Modify%22&validation_key=land_ice_sigma_coordinate&description=Land+ice+%28glaciers%2C+ice-caps+and+ice-sheets+resting+on+bedrock+and+also+includes+ice-shelves%29+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Land+Ice+Sigma+Coordinate)

- [ocean_double_sigma_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean_double_sigma_coordinate&issue_kind=%22Modify%22&validation_key=ocean_double_sigma_coordinate&description=Parametric+ocean+double+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+Double+Sigma+Coordinate)

- [ocean_s_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean_s_coordinate&issue_kind=%22Modify%22&validation_key=ocean_s_coordinate&description=Parametric+ocean+s-coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+S+Coordinate)

- [ocean_s_coordinate_g1](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean_s_coordinate_g1&issue_kind=%22Modify%22&validation_key=ocean_s_coordinate_g1&description=Parametric+ocean+s-coordinate%2C+generic+form+1%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+S+Coordinate+G1)

- [ocean_s_coordinate_g2](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean_s_coordinate_g2&issue_kind=%22Modify%22&validation_key=ocean_s_coordinate_g2&description=Parametric+ocean+s-coordinate%2C+generic+form+2%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+S+Coordinate+G2)

- [ocean_sigma_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean_sigma_coordinate&issue_kind=%22Modify%22&validation_key=ocean_sigma_coordinate&description=Parametric+ocean+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+Sigma+Coordinate)

- [ocean_sigma_z_coordinate](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean_sigma_z_coordinate&issue_kind=%22Modify%22&validation_key=ocean_sigma_z_coordinate&description=Parametric+ocean+sigma+over+z+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+Sigma+Z+Coordinate)

- [sea_water_potential_temperature](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+sea_water_potential_temperature&issue_kind=%22Modify%22&validation_key=sea_water_potential_temperature&description=Sea+water+potential+temperature+is+the+temperature+a+parcel+of+sea+water+would+have+if+moved+adiabatically+to+sea+level+pressure%2C+as+defined+by+the+CF+conventions.&ui_label=Sea+Water+Potential+Temperature)

- [sea_water_pressure](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+sea_water_pressure&issue_kind=%22Modify%22&validation_key=sea_water_pressure&description=Sea+water+pressure+is+the+pressure+that+exists+in+the+medium+of+sea+water%2C+as+defined+by+the+CF+conventions.&ui_label=Sea+Water+Pressure)

- [z*](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+z%2A&issue_kind=%22Modify%22&validation_key=z%2A&description=The+z%2A+coordinate%2C+as+defined+by+Adcroft+and+Campin+%282004%29.&ui_label=z%2A)

</details>
