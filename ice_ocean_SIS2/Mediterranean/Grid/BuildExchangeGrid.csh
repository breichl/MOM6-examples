#!/bin/tcsh
#

module load fre/bronx-21

make_solo_mosaic --num_tiles 1 --dir ./ --mosaic_name ocean_mosaic --tile_file Med_hgrid.nc
make_quick_mosaic --input_mosaic ocean_mosaic.nc --mosaic_name grid_spec --ocean_topog Med_topog.nc
