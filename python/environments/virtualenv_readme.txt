managing python virtual environments with virtualenv
============================

why:  tie specific version of python and packages versions

##installation with pip

/usr/local/bin/pip3 install virtualenv


##creating virtualenv
cd ~/venv 
/usr/local/bin/python3 -m virtualenv core36
## a new env is located in ~/venv/core36

this filer will have bin with python, pip interpreters and a lib for specified packages

##activating a virtualenv
source core36/bin/activate

which python3  #should show python3 is /Users/zimine/venv/core36/bin/python3
#same is showed for pip3 

##deactivating
deactivate

##install specific version of a package with pip

#see all available versions of requests package
pip install requests==
pip install requests==20.20.1 #install the previous to latest version

pip install --pre requests # to install a pre-released version

#to install a package's extra
pip install requests[security]
pip list   # to see list of installed packages

### updating packages
pip install --upgrade requests


### install using requirements files 
##requirements.txt start###
requests==2.20.1
google-auth==1.6.2
##requirements.txt end###

pip install -r requirements.txt

## output a list of all installed packges and their versions (useful to create requirements.txt)
pip freeze
