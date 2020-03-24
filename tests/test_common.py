#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: ./nb/common.ipynb
import os
IN_TRAVIS=(os.getenv('TRAVIS', False) == 'true')
exp_dir_name = 'x_lib'
working_dir_tag = 'nb'

#https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
IN_JUPYTER = isnotebook()

print(IN_TRAVIS,'IN_TRAVIS' )
print( IN_JUPYTER , 'IN_JUPYTER ')

from tqdm.notebook import tqdm as notebook_tqdm
class _simple_tqdm:
    """
    for travis
    """
    def __init__(self, g):
        self.g = g
        try:
            l = len(g)
        except TypeError:
            l = '?'
        self.l = l

    def __iter__(self):
        for i,x in enumerate(self.g):
            print(f"({i}/{self.l})", end='')
            yield x

    def __len__(self):
        return self.l

if IN_JUPYTER:
    tqdm = notebook_tqdm
elif IN_TRAVIS:
    tqdm = _simple_tqdm
else :
    tqdm = _tqdm.tqdm

for i in _simple_tqdm(range(10)):
    print(i)
for i in tqdm(range(10)):
    pass

def ex_command(code):
    ip = get_ipython()
    # this depends on the environment where jupyter launchs
    ip.run_cell(code)

# todo
# 支持多级结构import, output，但可能不会用到
import json,re
from pathlib import Path
import io
import os

class NBExporter:
    def __init__(self, tag='export', prefix=''):
        self.tag = tag
        self.prefix = prefix

    def is_export(self, cell, ):
        tag = self.tag
        if cell['cell_type'] != 'code': return False
        src = cell['source']
        if len(src) == 0 or len(src[0]) < 7: return False
        #import pdb; pdb.set_trace()
        reg = f'^\s*#\s*{tag}\s*$'
        reg = re.compile(reg, re.IGNORECASE,)
        return re.match(reg, src[0], ) is not None


    def __call__(self, fname, to='../exp'):
        "Finds cells starting with `#export` and puts them into a new module"
        fname = Path(fname)
        to = Path(to)
        fname_out = f'{fname.stem.split(".")[0]}.py'
        fname_out = f'{self.prefix}{fname_out}'
        main_dic = json.load(open(fname,'r',encoding="utf-8"))
        code_cells = [c for c in main_dic['cells'] if self.is_export(c)]
        module = f'''#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: ./nb/{fname.name}
'''

#         import pdb; pdb.set_trace()
        for cell in code_cells: module += ''.join(cell['source'][1:]) + '\n\n'
        # remove trailing spaces
        module = re.sub(r' +$', '', module, flags=re.MULTILINE)
        output_path = to/fname_out

        with io.open(output_path, "w", encoding="utf-8") as f:
            f.write(module[:-2])
        print(f"Converted {fname} to {output_path}")

class Export_notebook:

    def __init__(self, dst, working_dir_tag = 'nb'):
        self.export_model = NBExporter()
        self.export_test = NBExporter('(test_)?export', prefix='test_')
        self.dst = dst
        self.working_dir_tag = working_dir_tag

    def sub_path(self, dst):
        rv = lambda s:s[::-1] # revserse string
        current = os.getcwd()
        tag = self.working_dir_tag
        assert tag in current, f"{tag, current}"

        current = rv(current)
        dst = rv(dst)
        tag = rv(tag)
        current = current.replace(tag, dst, 1)
        current = rv(current)

        return current

    def __call__(self, name,):
        assert IN_JUPYTER

        save_notebook()
        NOTEBOOK_EXTEND_NAME='.ipynb'
        if NOTEBOOK_EXTEND_NAME not in name:
            name += NOTEBOOK_EXTEND_NAME
        time.sleep(1)

        test_path = self.sub_path('tests')
        exp_path = self.sub_path(self.dst)

        # support import complie
        self.export_model(name, to=exp_path)
        self.export_test(name, to=test_path)

        save_notebook() # for exitting



# use those only in jupyter
import time

def save_notebook():
    from IPython.display import display, Javascript
    display(Javascript('IPython.notebook.save_checkpoint();'))

def restart_kernel():
    from IPython.display import display, Javascript
    display(Javascript('IPython.notebook.kernel.restart();'))

save_and_export_notebook = Export_notebook(exp_dir_name, working_dir_tag = working_dir_tag )
