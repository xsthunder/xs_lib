#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: ./nb/ismain.ipynb
import sys
if __name__ == '__main__': sys.path.append('..')
import xs_lib.common as common

def ismain(name):
    """
    test __name__=="__main__"
    name: pass in __main__
    """
    return name=="__main__"

def main(name, fn):
    """
    if test __name__=="__main__", run fn()
    name: pass in __main__
    """
    b = ismain(name)
    if(b):
        fn()
    return b