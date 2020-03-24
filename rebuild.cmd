pip uninstall xsthunder-python-lib -y
python setup.py sdist bdist_wheel
pip install .\dist\xsthunder_python_lib-0.0.1-py3-none-any.whl