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

If you make use of these scripts or the analysis, please cite the following paper: https://ui.adsabs.harvard.edu/abs/2022arXiv220704780M/abstract 

```
@ARTICLE{2022arXiv220704780M,
       author = {{M{\"u}ller-Bravo}, T.~E. and {Galbany}, L. and {Karamehmetoglu}, E. and {Stritzinger}, M. and {Burns}, C. and {Phan}, K. and {I{\'a}{\~n}ez Ferres}, A. and {Anderson}, J.~P. and {Ashall}, C. and {Baron}, E. and {Hoeflich}, P. and {Hsiao}, E.~Y. and {de Jaeger}, T. and {Kumar}, S. and {Lu}, J. and {Phillips}, M.~M. and {Shahbandeh}, M. and {Suntzeff}, N. and {Uddin}, S.~A.},
        title = "{Testing the Homogeneity of Type Ia Supernovae in the Near-Infrared for Accurate Distance Estimations}",
      journal = {arXiv e-prints},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2022,
        month = jul,
          eid = {arXiv:2207.04780},
        pages = {arXiv:2207.04780},
archivePrefix = {arXiv},
       eprint = {2207.04780},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022arXiv220704780M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```



