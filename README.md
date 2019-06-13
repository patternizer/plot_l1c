<img alt="FIDUCEO: MMD_HARM" align="right" src="http://www.fiduceo.eu/sites/default/files/FIDUCEO-logo.png">

# plot_l1c

Development code for the plotting of AVHRR Easy FCDR L1C orbits from [H2020 FIDUCEO](https://fiduceo.eu).

![image](https://user-images.githubusercontent.com/5902974/59455595-6ebad300-8e0c-11e9-9143-c1b73daa5ba8.png)

## Contents

* `plot_l1c.py` - main script to be run with Python 3.6

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

    $ python3 plot_l1c.py l1c.nc
        
### l1c.nc

* `l1c.nc` - netCDF-4 file containing latitude, longitude and data variable to be plotted

Available on request from https://github.com/patternizer

## License

The code is distributed under terms and conditions of the [MIT license](https://opensource.org/licenses/MIT).

## Contact information

* Michael Taylor (michael.taylor@reading.ac.uk)

