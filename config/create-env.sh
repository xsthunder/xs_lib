set -e
if test $TRAVIS
then
    source $HOME/miniconda/etc/profile.d/conda.sh
fi

env_name=test

conda create -n $env_name IPython tqdm -c conda-forge -y

conda activate $env_name

yes | pip install -r ./config/install_requires.txt

# sure=1.4.11
# ipython=7.8.0
# tqdm=4.36.1
# python=3.7.4
