#MS263_BioreactorProject

Katie Duncan's MS263 class project for Spring 2024

---------------------------------------------------------------------------
Data information:

- Fourteen CSV files were provided by Central Coast Wetlands Group for this project

- Thirteen are utilized in this project notebook

---------------------------------------------------------------------------
Notebook requirements:

- CCWG Bioreactor data (Available in HydraData subdirectory on GitHub)

- A subdirectory labeled HydraData with all necessary CSV files must be available for the notebook to function

- Custom CSWTBioreactorFunctions module (Contained in main directory)

- Packages and modules (Embedded in project notebook)

import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import pandas as pd
import CSWTBioreactorFunctions as CBRF
import numpy as np
from scipy import linalg
import seaborn as sns
import cmocean.cm as cmo

---------------------------------------------------------------------------
Class notes: Ideas from class discussion May 7th
1. Figure out how to remove NaN values from pandas dataframe
2. Consider spectral analysis of potential diel variations in temperature
