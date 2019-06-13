#!/usr/bin/env python

# call as: python plot_1lc.py <l1c_file.nc>

# Code to quickly plot L1C orbits from FIDUCEO Easy FCDR:
# ======================================================
# Version 0.3
# 13 June, 2019
# michael.taylor AT reading DOT ac DOT uk
# ======================================================

from  optparse import OptionParser
import numpy as np
import numpy.ma as ma
import xarray
import matplotlib.pyplot as plt; plt.close("all")
import matplotlib.dates as mdates
import matplotlib.colors as mcolors
import matplotlib.ticker as mticker
import cartopy
import cartopy.crs as ccrs
#from cartopy.io import shapereader
#import cartopy.feature as cfeature
#from cartopy.util import add_cyclic_point
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def plot_orbit_var(lat, lon, var, vmin, vmax, projection, filestr, titlestr, varstr):

    x = lon[::10,::10]
    y = lat[::10,::10]
    z = var[::10,::10]

#    z_cyc, x_cyc = add_cyclic_point(z, coord=x)

    fig  = plt.figure()
    if projection == 'platecarree':
        p = ccrs.PlateCarree(central_longitude=0)
        threshold = 0
    if projection == 'mollweide':
        p = ccrs.Mollweide(central_longitude=0)
        threshold = 1e6
    if projection == 'robinson':
        p = ccrs.Robinson(central_longitude=0)
        threshold = 0
    if projection == 'equalearth':
        p = ccrs.EqualEarth(central_longitude=0)
        threshold = 0
    if projection == 'geostationary':
        p = ccrs.Geostationary(central_longitude=0)
        threshold = 0
    if projection == 'goodehomolosine':
        p = ccrs.InterruptedGoodeHomolosine(central_longitude=0)
        threshold = 0
    if projection == 'europp':
        p = ccrs.EuroPP()
        threshold = 0
    if projection == 'northpolarstereo':
        p = ccrs.NorthPolarStereo()
        threshold = 0
    if projection == 'southpolarstereo':
        p = ccrs.SouthPolarStereo()
        threshold = 0
    if projection == 'lambertconformal':
        p = ccrs.LambertConformal(central_longitude=0)
        threshold = 0

    ax = plt.axes(projection=p)    
    ax.stock_img()
    ax.coastlines(resolution='50m')
#    ax.add_feature(cfeature.RIVERS.with_scale('50m'))
#    ax.add_feature(cfeature.BORDERS.with_scale('50m'))
#    ax.add_feature(cfeature.LAKES.with_scale('50m'))
    ax.gridlines()
    colormap = 'gnuplot2'

    g = ccrs.Geodetic()
    trans = ax.projection.transform_points(g, x, y)
    x0 = trans[:,:,0]
    x1 = trans[:,:,1]

    if projection == 'platecarree':
        ax.set_extent([-180, 180, -90, 90], crs=p)
        gl = ax.gridlines(crs=p, draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='-')
        gl.xlabels_top = False
        gl.ylabels_right = False
        gl.xlines = True
        gl.ylines = True
        gl.xlocator = mticker.FixedLocator([-180,-120,-60,0,60,120,180])
        gl.ylocator = mticker.FixedLocator([-90,-60,-30,0,30,60,90])
        gl.xformatter = LONGITUDE_FORMATTER
        gl.yformatter = LATITUDE_FORMATTER
        for mask in (x0>=threshold,x0<=threshold):
            im = ax.pcolor(ma.masked_where(mask, x), ma.masked_where(mask, y), ma.masked_where(mask, z), vmin=vmin, vmax=vmax, transform=ax.projection, cmap=colormap)
#            im = ax.pcolor(ma.masked_where(mask, x), ma.masked_where(mask, y), ma.masked_where(mask, z), transform=ax.projection, cmap=colormap)
    else:
        for mask in (x0>=threshold,x0<=threshold):
            im = ax.pcolor(ma.masked_where(mask, x0), ma.masked_where(mask, x1), ma.masked_where(mask, z), vmin=vmin, vmax=vmax, transform=ax.projection, cmap=colormap)
#            im = ax.pcolor(ma.masked_where(mask, x0), ma.masked_where(mask, x1), ma.masked_where(mask, z), transform=ax.projection, cmap=colormap)

    im.set_clim(vmin,vmax)
    cb = plt.colorbar(im, orientation="horizontal", extend='both', label=varstr)
    plt.title(titlestr)
    plt.savefig(filestr)
    plt.close('all')

# =======================================
# MAIN BLOCK
# =======================================

if __name__ == "__main__":
    '''
    EXAMPLE: $ python plot_l1c.py l1c.nc 0 Ch4 250 310
    '''

    #--------------------------------------------------------------------------
    parser = OptionParser("usage: %prog l1c_file proj varstr vmin vmax")
    (options, args) = parser.parse_args()
    l1c_file = args[0]
    proj = int(args[1])
    varstr = str(args[2])
    vmin = args[3]
    vmax = args[4]

    if proj == 0: projection = "platecarree"
    elif proj == 1: projection = "mollweide"
    elif proj == 2: projection = "robinson"
    elif proj == 3: projection = "equalearth"
    elif proj == 4: projection = "geostationary"
    elif proj == 5: projection = "goodehomolosine"
    elif proj == 6: projection = "europp"
    elif proj == 7: projection = "northpolarstereo"
    elif proj == 8: projection = "southpolarstereo"
    else: projection = "geostationary"

    if len(args) == 0:
        # defaults
        varstr = "Ch5"
        vmin = 270
        vmax = 305
        projection = "geostationary"

    ds = xarray.open_dataset(l1c_file, decode_cf=1) 
    lat = np.array(ds.latitude)
    lon = np.array(ds.longitude)
    var = np.array(ds[varstr]) 
    filestr = "L1C_" + projection + ".png"
    titlestr = projection

    plot_orbit_var(lat, lon, var, vmin, vmax, projection, filestr, titlestr, varstr)

    print("** END")


