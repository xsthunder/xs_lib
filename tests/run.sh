set -e
set -x


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

# test export to ./
python ../xs_lib/common.py ../nb/common.ipynb

# test export to file
python ../xs_lib/common.py ../nb/common.ipynb test_nb.py
