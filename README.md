# Overview of mass balance satellite Earth Observation (EO) techniques

The are three main geodetic technologies (`satellite geodesy') to measure ice mass balance:
- gravimetry (gravitational mass balance)
    - GRACE(-FO) are the main source of measurment.
    - relies heavily on GIA (glacial isostratic adjusments) to disentangle variance in the gravity field due to mass balance and solid earth effects like the rebound (uncertainty)
- altimetry (altimetry mass balance) 
    - radar altimetry (older)
    - laser altimetry (newer) 
    - estimate mass change via volume change (most uncertainty from converting volume to mass as it relies on density models of ice and firn)
    - minor GIA adjustment
    - resolved spatial detail
- input-output (relies on interferometry (InSAR))

- Various satellite methods differ in their strengths and wekanesses.

Overview of [IMBIE studies](http://imbie.org/):

- IMBIE 1 (2012)
- IMBIE 2 (2018)
- IMBIE 3 (2023)

# Data

# gmb data

Various Level-3 (gridded) data products are published by JPL, GFZ and CSR, which are all based on the identical raw GRACE(-FO) Level-1 satellite observations. See the [GRACE Tellus website](https://grace.jpl.nasa.gov/data/choosing-a-solution/) for more details. The largest categorical difference among data sets is between mascon (mass concentration) solutions and spherical harmonics kernels.

[COST-G gridded data via GFZ](https://gravis.gfz-potsdam.de/ais) This is a combination product combining multiple L2 data including GFZ. The spatial resolution is 50km x 50km. Gravitational mass balance change is reported in kg/m^2 relative to the long-term average from 2002-04 to 2020-03, to reduce the effect of noise or seasonal patterns that might impact any single time slice (i.e. field). RL stands for release.
- [COST-G website](https://cost-g.org/)

EGU abstract:
Groh, A., and Horwath, M. (2016). The method of tailored sensitivity kernels for GRACE mass change estimates. Geophysical Research Abstracts, 18, EGU2016-12065.

[JPL RL06.1_v03 monthly mass grid mascons](https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/) This is the latest JPL product on 0.5 degrees resolution (50 km). View [here](https://grace.jpl.nasa.gov/data/data-analysis-tool/). Download data (netcdf) via [PODAAC](https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.1_V3). Uncertainty estimates are provided.

[Copernicus gmb](https://cds.climate.copernicus.eu/cdsapp#!/dataset/10.24381/cds.38b9366c?tab=overview) This appears to not be gridded data, but basin-level data according to [this documentation](https://confluence.ecmwf.int/pages/viewpage.action?pageId=355348674).

# amb data

https://digital.lib.washington.edu/researchworks/handle/1773/45388

Ben Smith et al., Pervasive ice sheet mass loss reflects competing ocean and atmosphere processes. Science368,1239-1242(2020). DOI: 10.1126/science.aaz5845

## Visualisations

[NASA visualisation](https://svs.gsfc.nasa.gov/31158/):

This animation shows **gravitational mass balance (gmb)** of the AIS (Antarctic ice sheet) over time. Note: This visualisation is relative to 2012, i.e. the cumulative mass loss/mass gain is presented. The line plot on the left shows gigatonnes [gt] and the visualisation on the right shows meters water equivalent. The data also originates from Gravity Recovery and Climate Experiment (GRACE) twin satellites and GRACE Follow-On (GRACE-FO) twin satellites, but processes by JPL. A mass loss of 142 gt/year is reported. The visualisation is based on a JPL GRACE (MASCON CRI GRID RL06.1 V3).

[GFZ/COST-G visualisation](https://gravis.gfz-potsdam.de/ais)

This animation also shows **gravitational mass balance (gmb)** of the AIS (Antarctic ice sheet) over time. The lineplot at the bottom shows gigatonnes [gt] and the visualisation at the top shows kg/m^2 which is equvalent to mm water equivalent. Total mass loss is slighlty more conservative than that reported by NASA, approx 99 gt loss/year.

## Relevant publications

Comparison of earlier releases (RL)
Barletta, V.R., Sørensen, L.S. and Forsberg, R. (2013). Scatter of mass changes estimates at basin scale for Greenland and Antarctica. The Cryosphere, 7, 1411-1432

Groh, A., and Horwath, M. (2016). The method of tailored sensitivity kernels for GRACE mass change estimates. Geophysical Research Abstracts, 18, EGU2016-12065.

## GPS for in-situ mass balance observations:
- https://polenet.org/a-net/
- https://polenet.org/sites/
- Polenet mainly to monitor glacial isostatic adjustment: https://antarcticsun.usap.gov/science/1453/
- https://byrd.osu.edu/news/2023-2024-anet-polenet-field-season-comes-end
- https://theconversation.com/scott-morrison-commits-804-million-over-a-decade-for-the-antarctic-177548 
- https://researchdata.edu.au/australian-antarctic-geodetic-network/698798
- https://www.bas.ac.uk/polar-operations/engineering-and-technology/technology-tools-and-methods/global-positioning-system-gps/
- Greenland need for GPS: https://www.science.org/doi/10.1126/sciadv.1600931
- https://antarctic-logistics.com/project/polenet/

# Next steps
- Interpolate data to generate more time stamps.
- 

# DeepSensor Questions
- Can we change the initialisation (prior) of the covariances?
- What is the unit of the receptive field? Is the size relative to 1x1?
- Why can we not preprocess Datasets with only the time dimension?
- When processing a dataset with multiple variables, does the normalisation method need to be consistent? No.

# Solved issues
- nan's in target: 
    - see https://alan-turing-institute.github.io/deepsensor/user-guide/task_loader.html
    - add to generate function?
    - Wasn't clear to me
- produce MWC (Minimum workable code)

# ToDo:
- Convert off-grid back to grid for prediction vis
- Add other context inputs
- Active learning 2 objectives: minimise gap between 2 methods (gmb and altimetry), select methods to maximise explainatory power
- train on both data sets.
- push to new Git repo because of issue
- bed topo ablation
- year ablation
- fine tuning
- other off-diagonal initialisation

# Research ideas:
- pure KL divergence approach:
- how do we combine the notion of uncertainty and general aqcuition functions with that of KL
- KL * high mass loss 

# Data
- Level 3 data from GRACE and GRACE-FO
- https://cost-g.org/ 

Level-3 products based on (COST-G)[https://cost-g.org/] RL01:
Sasgen, Ingo; Groh, Andreas; Horwath, Martin, 2020:
COST-G GravIS RL01 Ice-Mass Change Products. V. 0003
GFZ Data Services, https://doi.org/10.5880/COST-G.GRAVIS_01_L3_ICE

Level-3 products based on (GFZ)[https://www.gfz-potsdam.de/en/] RL06:
Sasgen, Ingo; Groh, Andreas; Horwath, Martin, 2019:
GFZ GravIS RL06 Ice-Mass Change Products. V. 0003
GFZ Data Services, https://doi.org/10.5880/GFZ.GRAVIS_06_L3_ICE

## Altimetry data
- Copernicus Climate Change Service (C3S) 
- 25 km resolution
- includes ice shelves too
- 1991
- not updated since February 2023
- large pole of ignorance in earlier years
- https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-ice-sheet-elevation-change?tab=overview 
- https://confluence.ecmwf.int/pages/viewpage.action?pageId=355345400

- https://nsidc.org/data/user-resources/help-center/icesat-icebridge-and-icesat-2-primer-data-access-across-three-missions
https://icesat-2.gsfc.nasa.gov/sites/default/files/page_files/ICESat2_ATL1415_ATBD_r003.pdf 

# Ice sat data
https://nsidc.org/data/atl14/versions/3

Operation ice bridge
https://nsidc.org/data/iodem3/versions/1# massbalanceAntarctica
