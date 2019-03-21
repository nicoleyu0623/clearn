#### managing conda 

conda info

conda info --envs

conda list ## see all packages
cnoda list ^pyt
conda search numpy
conda install scipy
conda update pandas 
conda remove scipy
conda remove -n py33test scipy #remove package from a env
conda remove --dry-run -n py33test scipy # dry-run testing of removal 
conda remove --all -n py33test #uninstall all packages for py33test


#creating a new env  with py version at 3.6
conda create -n py4fi python=3.6
conda info --envs
conda activate py4fi  # to activate environment
python --version  #now is at 3.6 
conda install numpy pandas matplotlib  # installs packages in this environment
pip install cufflinks
conda install ipython jupyter
cd ~
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
#this will launch jupyter with python kerne=3.6 in the py4fi env
conda deactivate #to switch to default env


