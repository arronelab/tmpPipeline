#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:56:49 2022

@author: ccck67
"""
import numpy as np
import plotly.graph_objects as go
import varyingSections as vs
    
def read_coords(fl_name):
    mol = np.genfromtxt(fl_name,skip_footer=1)
    return mol

def read_fingerprint(fl_name):
    fp = []
    with open(fl_name,'r') as fin:
        for line in fin:
            fp.append(line.split())
    return [*fp[-1][0]]

def make_fp_colors(fp):
    fp_col_dict = {'-' : 'rgb(0,154,68)',
                   'H' : 'rgb(229,99,23)',
                   'S' : 'rgb(153,61,8)'}
    fp_cols = [fp_col_dict[i] for i in fp]
    return fp_cols

def plot_mol(mol,cols):
    fig = go.Figure(data=go.Scatter3d(
        x=[i[0] for i in mol], y=[i[1] for i in mol], z=[i[2] for i in mol],
        marker=dict(
            size=0.1,
            color=cols,
        ),
        line=dict(
            color=cols,
            width=7.5
        ),
    ))
    fig['layout']['showlegend'] = True
    fig.update_layout(
    scene=dict(
        xaxis_title='',
        yaxis_title='',
        zaxis_title='',
        bgcolor='rgb(255,255,255)',
        #plot_bgcolor='rgb(248,240,227)',
        aspectratio = dict( x=1, y=1, z=1 ),
        aspectmode = 'manual',
        xaxis = dict(
            gridcolor="rgb(248,240,227)",
            showbackground=False,
            zerolinecolor="rgb(248,240,227)",
            nticks=0,
            showticklabels=False),
        yaxis = dict(
            gridcolor="rgb(248,240,227)",
            showbackground=False,
            zerolinecolor="rgb(248,240,227)",
            nticks=0,
            showticklabels=False),
        zaxis = dict(
            gridcolor="rgb(248,240,227)",
            showbackground=False,
            zerolinecolor="rgb(248,240,227)",
            nticks=0,
            showticklabels=False),),
    )
    fig.write_html('mol.html', auto_open=True)
    
def plot_mol_ss(coords,fp):
    mol = read_coords(coords)
    fp = read_fingerprint(fp)
    cols = make_fp_colors(fp)
    plot_mol(mol,cols)
    
def plot_mol_sb(coords,fp):
    mol = read_coords(coords)
    fp = read_fingerprint(fp)
    cols = vs.color_sheet_breakers(fp)
    plot_mol(mol,cols)

#coords = read_coords('/home/grads/ccck67/rdata/c++Molecule/newFitData/human_SMARCAL1/open/mol1.dat')
#fp = read_fingerprint('/home/grads/ccck67/rdata/c++Molecule/newFitData/human_SMARCAL1/fingerPrint.dat')
print(plot_mol_ss('/home/grads/ccck67/rdata/c++Molecule/newFitData/human_SMARCAL1/open/mol3.dat',
                  '/home/grads/ccck67/rdata/c++Molecule/newFitData/human_SMARCAL1/fingerPrint.dat'))
