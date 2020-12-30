if ! test $TRAVIS
then
    pip uninstall xs_lib -y
fi
rm -rf dist
mkdir dist
python setup.py sdist bdist_wheel
yes | pip install ./dist/xs_lib-*-py3-none-any.whl
