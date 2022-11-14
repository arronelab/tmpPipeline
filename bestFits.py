#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:54:57 2022

@author: ccck67
"""
import numpy as np
import os

def load_scatter_file(fl_name):
    lines = []
    with open(fl_name,'r') as fin:
        for line in fin:
            lines.append(line.split())
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = float(lines[i][j])            
    return lines

def assess_scatter_fit(fl_name):
    scatdat = load_scatter_file(fl_name)
    sqdiffs = [(scatdat[i][2]-scatdat[i][3])**2/(scatdat[i][3]**2) for i in range(len(scatdat))]
    chisq = sum(sqdiffs)
    return np.sqrt(chisq)

def load_all_fits(test_name):
    fits = []
    with os.scandir(test_name) as it:
        for entry in sorted(it, key = lambda e: e.name):
            if entry.name.startswith("scatter") and entry.name.endswith(".dat") and entry.is_file():
                fits.append(assess_scatter_fit(entry.path))
    return fits
                
def best_five_fits(test_name):
    fits = load_all_fits(test_name)
    indices = sorted(range(len(fits)), key=lambda k: fits[k])[:5]
    best_five = [[i,fits[i]] for i in indices]
    return best_five