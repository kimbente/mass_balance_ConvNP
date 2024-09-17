Ice-sheet height and thickness changes from ICESat to ICESat-2.

These data represent ice-column thickness-change-rate estimates from Smith et al. 2020 and are based on data from NASAÕs ICESat-1 and ICESat-2 satellites. These data aided the first estimates of ice-sheet mass change from these two missions, spanning the 16 years from 2003 to 2019, taking advantage of the high vertical and horizontal resolution of the two satellites' laser altimeters.

Please cite the following when using these data:
Smith, B., Fricker, H. A., Gardner, A. S., Medley, B., Nilsson, J., Paolo, F. S., Holschuh, N., Adusumilli, S., Brunt, K., Csatho, B., Harbeck, K., Markus, T., Neumann, T., Siegfried, M. R., & Zwally, H. J. (2020). Pervasive ice sheet mass loss reflects competing ocean and atmosphere processes. Science, 368. https://doi.org/10.1126/science.aaz5845


For grounded ice, these data represent the rate of surface-height change (not corrected for changes in firn air content, dhdt) or the rate of ice gain or loss (the data corrected for changes in firn air content, dmdt). For floating ice, the hydrostatic relation has been used to convert elevation changes to thickness changes. We provide a set of grids that contains fully corrected but unsmoothed gridded data, from which our calculations of drainage-by-drainage mass change were derived, and a second set of smoothed grids that are intended for display purposes only. Each set of grids provides ice-sheet surface height and thickness change rate in meters of ice per year (m/yr).  A second set of grids provides the data corrected for firn-air changes.

Full details of the processing and analysis of these data are provided in Smith et al., (2020, Science).  Two sets of files are provided in geotif format: one unfiltered set, which are suitable for mass-balance integrations, and a filtered set that have been smoothed for display, which match figures 2 and 3 in Smith et. al, 2020.

Data files
----------

There are two sets of data, in separate directories.  PLEASE NOTE: An older version of this archive contained only the dhdt grids (incorrectly labeled as 'dmdt'), not the dmdt grids.

--The dhdt directory contains the total thickness-change data, corrected from height-change to thickness-change rates for floating ice based on the hydrostatic relation. All grids are in units of meters per year.

--The dmdt directory contains thickness-change data, corrected for firn-air column thickness changes to reflect ice-thickness change only.  Like the files in the dhdt directory, for floating ice, the surface height change is corrected to thickness change using the hydrostatic relation.  

The files found in each directory are as follows.  Each filename is identified with [version] replaced by either 'dhdt' or 'dmdt' to match whether it contains the uncorrected (dhdt) fields or the firn-air corrected (dmdt) fields. 

1. Filtered mass-change maps, for display only, units of m(ice-equivalent)/yr:
ais_[version]_floating_filt.tif
ais_[version]_grounded_filt.tif
gris_[version]_filt.tif

2. Filtered mass-change maps, rendered to match figures 2 and 3:
ais_[version]_floating_filt_rgb.tif
ais_[version]_grounded_filt_rgb.tif
gris_[version]_filt_rgb.tif

3. Raw mass-change maps, suitable for generation of basin-by-basin mass-change estimates, units of m(ice-equivalent)/yr:
ais_[version]_floating.tif
ais_[version]_grounded.tif
gris_[version].tif

4. Per-cell RMSE (root-mean-squared error) maps:
ais_[version]_grounded_rmse.tif
ais_[version]_floating_rmse.tif


4: Colorbar information, giving the mapping from dmdt to red, green, and blue channel values needed to recreate the rgb images (the _stretch3 file is for grounded ice, the _stretch3_floating file is for floating ice)
dhdt_strech3.txt
dhdt_strech3_floating.txt
dhdt_colorbar.png
