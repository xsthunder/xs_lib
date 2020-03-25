personal python lib [![Build Status](https://travis-ci.com/xsthunder/xs_lib.svg?branch=master)](https://travis-ci.com/xsthunder/xs_lib)
------
legacy python lib see [xsthunder/python-lib: useful python pieces of code](https://github.com/xsthunder/python-lib)

### code and release

1. code at [xsthunder/xs_lib at dev](https://github.com/xsthunder/xs_lib/tree/dev)

2. update [xs_lib/version.py at dev · xsthunder/xs_lib](https://github.com/xsthunder/xs_lib/blob/dev/xs_lib/version.py)

3. merge master and travis will deploy to pip

### TODO
 
### Features

1. Full test with traivis to make sure things are on rail.
2. list of function see [doc](./doc/README.md)

## Install and Run

### Install via [xsthunder-python-lib · PyPI](https://pypi.org/project/xsthunder-python-lib/)

1. `pip install xsthunder-python-lib` or `pip install xsthunder-python-lib --user`

### Use in Code

#### use for single `ipynb` file

export the `ipynb` file

```python
import xs_lib.common as common
nbe = common.NBExporter()
nbe('./pdb.ipynb', to='./')
```
#### use for projcet

clone [xsthunder/jupyter_dev_template](https://github.com/xsthunder/jupyter_dev_template)

## Development

### Environment Setup

[for conda](./config/create-env.sh)

### deps

1. not all [deps](./config/create-env.sh) are necessary. only ipython are set in the `setup.py/deps`.
2. `xs_lib.common` supports dynamic import. feel free to import.
3. to import other modules, please install corresponding deps first or you may come across import error.
4. It's recommanded to install all packages listed in [create-env.sh](./config/create-env.sh)



### code structures



#### Ref 

[deployment - How can I use setuptools to generate a console_scripts entry point which calls `python -m mypackage`? - Stack Overflow](https://stackoverflow.com/questions/27784271/how-can-i-use-setuptools-to-generate-a-console-scripts-entry-point-which-calls)

[Packaging Python Projects — Python Packaging User Guide](http://packaging.python.org/tutorials/packaging-projects/)

`notebook2script` from [course-v3/nbs/dl2 at master · fastai/course-v3](https://github.com/fastai/course-v3/tree/master/nbs/dl2)
