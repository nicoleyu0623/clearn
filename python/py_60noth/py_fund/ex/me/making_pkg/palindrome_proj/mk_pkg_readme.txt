 ckaging the code #####
     synopsis: we will create a package in a virtual env

     /usr/local/bin/python3 -m virtualenv ~/venv/palindrome_env
     source ~/ven/palindrome_env/bin/activate
    
     mkdir palindrome_proj
     cp palindrome.py  palindrome_proj

    in a palindrome_rpoj create setup.py

    setup.py  has setup() function
    
    ! demo ex/me/making_pkg/palindrome_proj
    ==== installing with install ======
    >cd palindrome_rpoj
    >python setup.py install
    ## this copies palindrome.py into the ~/venv/palindrome_env/lib/python3/site-packages
    >pip list (will show now that palindrome package is isntalled)
   
    #testing importing
    >cd ..
    >python
    >>>import palindrome
    >>>palindrome.__file__  #shows the path to the package file
   
    ====== packaging with sdist (for redistribution) ========

    from the project source folder
    >python setup.py sdist  #creates a targ.gz in dist folder
    >python setup.py sdist --format zip
    >ls dist
    apple$ unzip -l dist/palindrome-1.0.zip

   >python setup.py sdist --help-formats
 
  now you can send this tar.gz to anybody outside

  you can install this targ.gzed package with pip
  pip install palindrome-1.0.tar.gz
  pip list  

  browser look for centrally managed pip packages
  https://pypi.python.org/pypi 
