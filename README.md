<img alt="FIDUCEO: MMD_HARM" align="right" src="http://www.fiduceo.eu/sites/default/files/FIDUCEO-logo.png">

# plot_l1c

Development code for the plotting of AVHRR Easy FCDR L1C orbits from [H2020 FIDUCEO](https://fiduceo.eu).

![image](https://user-images.githubusercontent.com/5902974/59461906-68335800-8e1a-11e9-8217-f60a09ecdfee.png)

## Contents

* `plot_l1c.py` - main script to be run with Python 3.6+

The first step is to clone the latest plot_l1c code and step into the check out directory: 

    $ git clone https://github.com/patternizer/plot_l1c.git
    $ cd plot_l1c
    
### Using Standard Python 

The code should run with the [standard CPython](https://www.python.org/downloads/) installation and was tested in a conda virtual environment running a 64-bit version of Python 3.6+.

**plot_l1c** can be run from sources directly, once the following module requirements are resolved to cater for plotting with cartopy:

* `optparse`
* `numpy`
* `xarray`
* `matplotlib`
* `cartopy`

Run with:

    $ python plot_l1c.py l1c.nc <options>

    options: proj varstr vmin vmax
    example: $ python plot_l1c.py l1c.nc 0 Ch4 250 310

    proj == 0 -> PlateCarree
    proj == 1 -> Molleweide
    proj == 2 -> Robinson
    proj == 3 -> EqualEarth
    proj == 4 -> Geostationary
    proj == 5 -> GoodeHomolosine
    proj == 6 -> EuroPP
    proj == 7 -> NorthPolarStereo
    proj == 8 -> SouthPolarStereo
    proj == 9 -> LambertConformal
           
### l1c.nc

* `l1c.nc` - netCDF-4 file containing latitude, longitude and data variable to be plotted

Available on request from https://github.com/patternizer

## License

The code is distributed under terms and conditions of the [MIT license](https://opensource.org/licenses/MIT).

## Contact information

* [Michael Taylor](https://patternizer.github.io)

