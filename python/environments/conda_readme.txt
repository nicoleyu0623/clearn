conda readme

http://conda.pydata.org/docs/py2or3.html

~/anaconda3/bin/conda --version



conda info --envs

conda create --name snakes python=3
activate snakes
python --version

 activate snowflakes
 python --version

on unix
>source activate snowflakes

>jupyter notebook


Create a Python 3.5 environment
conda create -n py35 python=3.5 anaconda

Update or Upgrade Python
conda update python

##packages
conda list

### how to update
## change to the given enviromennt or switch environment in anaconda navigator
open terminal for that environment
>conda update --all


##### graphlab install upgrade
pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.0.1/zslavpipa@gmail.com/69F9-CDBF-3BA6-C9E6-6445-D010-EFE8-09D1/GraphLab-Create-License.tar.gz




#### making R available in notebooks
# First create a new conda environment called r
conda create -n r anaconda
source activate r  #switch to this env

# Installs R

#### r essentials
>conda install -c r r-essentials  (3.4.3)
### fix
>conda update -c r -c main --all

> attempting to install through conda
>conda skeleton cran psych

>conda build r-psych # will build  if no dependencies
file is in ~a/anaconda/conda-bld/osx-64/r-psych-0.2.0.tar.bz2

>conda install r-psych --use-local 

> packages gets installed in 
envs/env_name/lib/R/Library

### attempting to install a package directly by running anaconda's R
>R binary is  
> envs/env-name/bin/R
>.libPaths()  # expect to have only 1 folder envs/env_name/lib/R/Library
>install.packages("psych") ## should install the package from inside R 


##on windows surface, 
R installed is 3.3.0

I've installed the same version as a standAlone

When R i running through anaconda
in notebook
.libPaths()  # shows 2 paths
"C:/Users/zimine/Documents/R/win-library/3.3" "C:/Users/zimine/Anaconda2/envs/py35/R/library

so start standalone R  from  
C:\Program Files\R\R-3.3.0\bin\x64\R.exe

R>install.packages("pkgName", lib="C:/Users/zimine/Documents/R/win-library/3.3" )


and the package will be availabe from the notebook 











