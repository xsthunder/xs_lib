set -e
set -x

# test python install
cd ..
bash rebuild.sh
cd tests

mkdir -p test
# test export to ./test
nb2py ../nb/common.ipynb ./test
# compare behaviour
diff ./test/test_common.py ./test_common.py
diff ./test/common.py ../xs_lib/common.py
rm -rf test

# set up conda env
# https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

if test $TRAVIS
then
    source $HOME/miniconda/etc/profile.d/conda.sh
    conda activate test
fi

export TRAVIS=true

# run test
for file in ./*.py
do
	python $file
done

export CLI_TEST=true

mkdir -p test
# test export to ./test
python ../xs_lib/common.py ../nb/common.ipynb ./test
# compare behaviour
diff ./test/test_common.py ./test_common.py
diff ./test/common.py ../xs_lib/common.py
rm -rf test

# test export to ./
python ../xs_lib/common.py ../nb/common.ipynb

# test export to file
python ../xs_lib/common.py ../nb/common.ipynb test_nb.py
