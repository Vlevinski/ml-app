$ mkdir ml-app
$ cd ml-app
/ml-app$ python -m venv venv
/ml-app$ source venv/bin/activate
(venv) /ml-app$ python -m pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Using cached pip-21.3.1-py3-none-any.whl (1.7 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-21.3.1
(venv) /ml-app$ pip freeze > requirements.txt
(venv) /ml-app$ touch README.md
(venv) /ml-app$ ll
total 12
drwxrwxr-x   3 val val 4096 Nov 25 08:48 ./
drwxr-xr-x 135 val val 4096 Nov 25 08:46 ../
-rw-rw-r--   1 val val    0 Nov 25 08:48 README.md
-rw-rw-r--   1 val val    0 Nov 25 08:48 requirements.txt
drwxrwxr-x   5 val val 4096 Nov 25 08:47 venv/
(venv) /ml-app$ 
