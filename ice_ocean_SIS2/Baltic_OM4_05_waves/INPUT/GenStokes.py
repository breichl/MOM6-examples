#Generating a synthetic Stokes drift dataset for test purposes
import numpy as np
import netCDF4 as NC
#-------------------------------------------------------------
FN_wndx = 'u_10_mod.clim.nc'
FN_wndy = 'v_10_mod.clim.nc'
#-------------------------------------------------------------
HN_wndx = NC.Dataset(FN_wndx)
HN_wndy = NC.Dataset(FN_wndy)
#
with NC.Dataset(FN_wndx) as src, NC.Dataset("StokesDrift.nc", "w") as dst:
    # copy global attributes all at once via dictionary
    dst.setncatts(src.__dict__)
    # copy dimensions
    for name, dimension in src.dimensions.items():
        dst.createDimension(
            name, (len(dimension) if not dimension.isunlimited() else None))
    # copy all file data except for the excluded
    for name, variable in src.variables.items():
        if name not in ['U_10','U_10_MOD']:
            x = dst.createVariable(name, variable.datatype, variable.dimensions)
            dst[name][:] = src[name][:]
            # copy variable attributes all at once via dictionary
            dst[name].setncatts(src[name].__dict__)

    WNDx = HN_wndx.variables['U_10'][:]
    WNDy = HN_wndy.variables['V_10'][:]
        
    #Create new Stokes fields:
    dst.createVariable('Usx1','f',('TIME','LAT','LON'))
    dst.createVariable('Usy1','f',('TIME','LAT','LON'))
    dst.createVariable('Usx2','f',('TIME','LAT','LON'))
    dst.createVariable('Usy2','f',('TIME','LAT','LON'))
    dst.variables['Usx1'][:] = WNDx*0.01
    dst.variables['Usy1'][:] = WNDy*0.01
    dst.variables['Usx2'][:] = WNDx*0.03
    dst.variables['Usy2'][:] = WNDy*0.03

    #Creating the dimension (100m and 10m)
    wn_ = dst.createDimension('frequency',2)
    wn_ = dst.createVariable('frequency','f','frequency')
    wn_[:]=[0.0624,0.624]
