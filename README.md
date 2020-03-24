### TODO
1. - [ ] fix three version replicates, in `rebuild.cmd`, `x_lib.__init__`, `setup.py`
2. - [ ] create github repo
3. - [x] ex_command能用，默认目录就在jupyter目录下。即外部可以直接使用x_lib.common.ex_command
1. - [x] save_and_export_notebook使用了`./`就是本目录下要求一定有script；；解决方法是通过import而不是ex_command的方式保存文件
1. - [x] script不支持多级目录，以后再解决。
 
### Features

4. Full test with traivis to make sure things are on rail.

 
## Install and Run

### Install via pip

1. `pip install xsthunder-python-lib` or `xsthunder-python-lib --user`

### Use in Code

```python
import download_youtube_subtitle.common as common
import download_youtube_subtitle.main as download_youtube_subtitle
# ...
```

## Development

### Environment Setup

[for conda](./config/create-env.sh)


#### Ref 

[deployment - How can I use setuptools to generate a console_scripts entry point which calls `python -m mypackage`? - Stack Overflow](https://stackoverflow.com/questions/27784271/how-can-i-use-setuptools-to-generate-a-console-scripts-entry-point-which-calls)

[Packaging Python Projects — Python Packaging User Guide](http://packaging.python.org/tutorials/packaging-projects/)

`./nb/notebook2script.py` from [course-v3/nbs/dl2 at master · fastai/course-v3](https://github.com/fastai/course-v3/tree/master/nbs/dl2)
