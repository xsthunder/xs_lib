if ! test $TRAVIS
then
    pip uninstall xs_lib -y
fi
python setup.py sdist bdist_wheel
yes | pip install fire
yes | pip install ./dist/xs_lib-*-py3-none-any.whl
