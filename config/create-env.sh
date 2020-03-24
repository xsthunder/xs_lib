set -e
if test $TRAVIS
then
    source $HOME/miniconda/etc/profile.d/conda.sh
fi

# py3.7 for asyncio.WindowsProactorEventLoopPolicy() support
conda create -n test IPython -c conda-forge -y
yes | pip install sure

# recommanded sure=1.4.11
# recommanded ipython=7.8.0