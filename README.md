# Data

[COST-G gridded data via GFZ](https://gravis.gfz-potsdam.de/ais) This is a combination product combining multiple L2 data including GFZ. The spatial resolution is 50km x 50km. Gravitational mass balance change is reported in kg/m^2 relative to the long-term average from 2002-04 to 2020-03, to reduce the effect of noise or seasonal patterns that might impact any single time slice (i.e. field). RL stands for release.
- [COST-G website](https://cost-g.org/)

EGU abstract:
Groh, A., and Horwath, M. (2016). The method of tailored sensitivity kernels for GRACE mass change estimates. Geophysical Research Abstracts, 18, EGU2016-12065.

[Copernicus gmb](https://cds.climate.copernicus.eu/cdsapp#!/dataset/10.24381/cds.38b9366c?tab=overview) This appears to not be gridded data, but basin-level data according to [this documentation](https://confluence.ecmwf.int/pages/viewpage.action?pageId=355348674).

## Visualisations

[NASA visualisation](https://svs.gsfc.nasa.gov/31158/):

This animation shows **gravitational mass balance (gmb)** of the AIS (Antarctic ice sheet) over time. Note: This visualisation is relative to 2012, i.e. the cumulative mass loss/mass gain is presented. The line plot on the left shows gigatonnes [gt] and the visualisation on the right shows meters water equivalent. The data also originates from Gravity Recovery and Climate Experiment (GRACE) twin satellites and GRACE Follow-On (GRACE-FO) twin satellites, but processes by JPL. A mass loss of 142 gt/year is reported. The visualisation is probably based on a JPL GRACE product (L2 or mascon).

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
https://nsidc.org/data/iodem3/versions/1