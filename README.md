Log Parser
==========

A Python3 log parser to parse weblog to get views count of paths

Features
--------

 * parse a log file with format [PATH] [IP_ADDRESS]
 * To show the total visits of each path
 * To show the unique views of each path
 * can output the result to a file
 * can output the error to a file

Environment Preparation
-----------------------

 * Python3
 * pip3
 * virtualenv

 1. Get the source

```
git clone https://github.com/wanleung/log_parser.git
```

 2. Go to the directory

```
cd log_parser
```

 3. create a virtualenv

```
virtualenv -p3 env
```

 4. load the env

```
source env/bin/activate
```

 5. To get the libraries for DEV

```
pip install -r requirements_dev.txt
```

 5a. For production

```
pip install -r requirements_prod.txt
make install
```

Running
-------

 * To get help

```
python log_parser.py --help
```

 * To run the program

```
python log_parser.py [LOG FILE]
```

 * To disable ip check

```
python log_parser.py --disable-ip-check [LOG FILE]
```

There is a sample_logs folder to store the sample logs.
The original log file is sample_logs/webserver.log
The sample.log and sample2.log are the files that created from real log data to pass the ip check.
sample.log is in wrong format and will give out error.
sample12.log is in the right format.

Running Test
------------

 * Using pytest in this project.
   while under the DEV environment, run

```
pytest
```

   to do the test.

 * Code Format checking
   currently using flake8

```
flake8 tests
flake8 log_parser
flake8 log_parser.py
```



Design Idea
-----------

 1. create a Url object to store the path and its ip counts
 2. create a Record object to save all the Url Object results
 3. Has to have a parser to load the file, to parse the file, get an ordering result from Record, get the errors
 4. Add the App object to warp the Parser as to handle the configs and output to files so that it could slim down the code on the main.   


### TODO - if has more time

 * sorting the part result with the same counts of views.
 * output template
 * CI/CD
 * add log format config like apache log format config.
 * haven't done to check the main in pytest before, have to find a way how to do auto check in cli mode to check the argv from shell..

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
