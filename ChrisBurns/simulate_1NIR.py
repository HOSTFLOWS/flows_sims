#!/usr/bin/env python

from snpy import get_sn
from glob import glob
from numpy import *
import pickle

def between(a, x1,x2):
   return greater_equal(a, x1)*less(a, x2)

ss = [get_sn(f) for f in glob('*_maxmodel.snpy')]
#ss = [get_sn('SN2004eo_maxmodel.snpy')]

#bands = ['Y','J','H','Yd','Hd','Jd','Jrc2']
bands = ['J','Jd','Jrc2']

Nss = {}
maxs = {}
deltas = {}
phases = {}
for band in bands:
    Nss[band] = []
    maxs[band] = {}
    deltas[band] = []
    phases[band] = []

for s in ss:
    s.plot(outfile = s.name+'.png')
   # s.summary()
    for band in bands:
        if band in s.data:
            if sum(between(s.data[band].MJD-s.Tmax, -10, 20)) > 5:
                print(s.name,band,sum(between(s.data[band].MJD-s.Tmax, -10, 20)))#band,s.Tmax,getattr(s, band[0]+"max"))
                s.data[band].mask_epoch(-10, 20)
                Nss[band].append(s)
                maxs[band][s.name] = getattr(s, band[0]+"max")
#print(Nss)

#for band in bands:
#    for s in Nss[band]:
#        print(s.name)
#        #fitbands = [b for b in s.data if b != band]
#        mask_orig = 1*s.data[band].mask
#        ids = nonzero(mask_orig)[0]
#        s.data[band].mask[:] = False
#        for i in ids:
#            s.data[band].mask[i] = True
#            try:
#                s.fit()
#            except:
#                continue
#            deltas[band].append(maxs[band][s.name]-getattr(s, band[0]+"max"))
#            phases[band].append(s.data[band].MJD[i] - s.Tmax)
#            s.data[band].mask[i] = False
#            print(i,s.data[band].MJD[i] - s.Tmax,maxs[band][s.name],getattr(s, band[0]+"max"),maxs[band][s.name]-getattr(s, band[0]+"max"))
#        s.data[band].mask[:] = mask_orig[:]
#
#
#out = open('simulationsJ.pickle','wb')
#ickle.dump(dict(phases=phases, deltas=deltas), fout)
#out.close()
