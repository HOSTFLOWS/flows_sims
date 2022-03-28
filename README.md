# Flows Simulations

This repository contains the analysis to test the homogeneity of Type Ia Supernovae (SNe Ia) in the Near-infrared (NIR) for accurate distance estimations

## SNe Ia sample and light-curve fitter

In this work, we use the Carnegie Supernova Project (CSP I+II) sample of SNe Ia with *uBgVriYJH*-band light curves. To fit these objects we use *SNooPy* ([Burns et al. 2011](https://ui.adsabs.harvard.edu/abs/2011AJ....141...19B/abstract))

## Running the notebooks

To run the notebooks it is recommended to create an environment first (e.g., using Anaconda) and activate it:

```code
conda create -n flows_sims pip
conda activate flows_sims
```

and then install the rest of the requirements (except for SNooPy --  see below):

```code
pip install -r requirements.txt
```

To install the latest version of SNooPy (v2.6 at the momment), follow these commands:

```code
git clone https://github.com/obscode/snpy
cd snpy
git checkout gen3
python setup.py install
```

## Citation

If you make use of these scripts or the analysis, please cite the following paper:

```
Coming soon...
```



