# HostFlows Simulations

This repository contains the "simulations" of type Ia supernovae (SNe Ia) and their analysis to how accurate is the assumption *one photometric point in J and H bands is enough to estimate accurate peak magnitudes in the near-infrared (NIR)*. To be more precise, these are pseudo-simulations (we will call them simulations nontheless) as we work with well-sampled SNe Ia with real observations to see how the light-curve parameters get affected by removing data points in the NIR bands.

I need to talk about *ZTF*...

## Sample

In this work, we will use the Data Release 3 of the Carnegie Supernova Project (CSP) as it contains 134 SNe Ia with well-sampled light curves in *uBgVriYJH* bands. Some cuts are introduced to provide a sub-sample that will ensure a proper analysis and minimise possible biases. Thus, the SNe must have:

* *J* and *H* bands photometry;
* optical bands photometry before and after *B*-band maximum for a proper estimation of *B*-band maximum;
* *J* and *H* bands photometry around *J* and *H* bands maxima, respectively, for a proper estimation of *J* and *H* bands maxima.

After these cuts, we are left with XXX SNe Ia from the CSP sample, which are then considered for the simulations.

## Light-curve fitting

To estimate the maxima in *B*, *J* and *H* bands, we will use *SNooPy* ([Burns et al. 2011](https://ui.adsabs.harvard.edu/abs/2011AJ....141...19B/abstract)) as it is one of the only two SN Ia light-curve fitters that can fit NIR bands; the other being *PISCOLA* ([Müller-Bravo et al. 2021](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.2778M/abstract)), although this is a data-driven fitter (i.e., not based on templates), so it cannot be used for for the purpose of this work.

The *max_model* model of SNooPy will be used as...


## Simulations

The first step is to fit the SNe Ia with their entire photometry (all bands) and obtain their light-curve parameters as these will be our fiducial ("true") values which we will use as comparison. Then, we will repeat the previous step but using only *grJH* bands, as ZTF only provides *gr* optical bands, serving as a second set of fiducial light-curve parameters.

The simulations will provide of replications the conditions of the observations used in HostFlows, i.e., one coeval epoch of photometry in *J* and *H* bands. However, some SNe could have two or even three epochs of photometry, which will also be considered. 

## Metrics

To test how accurate are the fits of the simulations (1, 2 and 3 *JH* epochs) compared to our reference fits (*all bands* and *grJH*), we need to define a set of metrics. We will use the following light-curve parameters: time of *B*-band maximum (<img src="https://render.githubusercontent.com/render/math?math=t_{\rm max}">), *B*-band maximum magnitude (<img src="https://render.githubusercontent.com/render/math?math=m_{B}">) and stretch (<img src="https://render.githubusercontent.com/render/math?math=\Delta~m_{15}">). The colour-stretch parameter (<img src="https://render.githubusercontent.com/render/math?math=s_{BV}">) will not be used as it requieres data at 30 days after $B$ band maximum for an accurate estimation, which we do not necessarily have.

For the different simulations we will also need different set of metrics to properly test how the observations affect the results. These are the following:

* 1 NIR epoch: time with respect to <img src="https://render.githubusercontent.com/render/math?math=t_{\rm max}"> and NIR maximum (in *J* and *H* bands).
* 2 NIR epochs: 
  * time with respect to <img src="https://render.githubusercontent.com/render/math?math=t_{\rm max}"> and NIR maximum (in *J* and *H* bands) of the closest epoch;
  * time (cadence) between epochs.
* 3 NIR epochs:
  * time with respect to <img src="https://render.githubusercontent.com/render/math?math=t_{\rm max}"> and NIR maximum (in *J* and *H* bands) of the closest epoch;
  * average time (cadence) between epochs.

___
## Running the notebooks

To run the notebooks it is recommended to create an environment first (e.g., using Anaconda):

```code
conda create -n hf_sims pip
```

To install the latest version of SNooPy (v2.6 at the momment), follow these commands:

```code
git clone https://github.com/obscode/snpy
cd snpy
git checkout gen3
python setup.py install
```
