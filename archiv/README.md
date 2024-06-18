# Data

Gravitational mass balance (gmb) data of Antarctica's ice sheet: [NASA visualisation](https://grace.jpl.nasa.gov/resources/31/antarctic-ice-loss-2002-2020/). Note: This visualisation is relative to 2012, i.e. the cumulative mass loss is presented.
    - monthly data
    - Gravity Recovery and Climate Experiment (GRACE) satellites and GRACE Follow-On

https://gravis.gfz-potsdam.de/ais

GMB GRACE data: 

Copernicus Grace data is not gridded
- https://cds.climate.copernicus.eu/cdsapp#!/dataset/10.24381/cds.38b9366c?tab=overview
- https://confluence.ecmwf.int/pages/viewpage.action?pageId=355348674 

Barletta, V.R., Sørensen, L.S. and Forsberg, R. (2013). Scatter of mass changes estimates at basin scale for Greenland and Antarctica. The Cryosphere, 7, 1411-1432

Groh, A., and Horwath, M. (2016). The method of tailored sensitivity kernels for GRACE mass change estimates. Geophysical Research Abstracts, 18, EGU2016-12065.

Zwally, H.J., Giovinetto, M.B., Beckley, M.A. and Saba, J.L. (2012). Antarctic and Greenland drainage systems, GSFC cryospheric sciences laboratory. Available at https://earth.gsfc.nasa.gov/cryo/data/polar-altimetry/antarctic-and-greenland-drainage-systems

https://gravis.gfz-potsdam.de/ais

COST-G solution

This data is gridded:
- https://data.gov.au/dataset/ds-aodn-650d3287-b81e-4689-a412-0532ad3ee464/details?q=

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

# DeepSensor Questions
- What is the unit of the receptive field? Is the size relative to 1x1?
- Does the preprocessing work on xarray.Datasets and xarray.Dataarrays? Yes.
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