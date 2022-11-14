#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:38:43 2022

@author: ccck67
"""

def read_coords(fl_name):
    mol = np.genfromtxt(fl_name,skip_footer=1)
    return mol
    
def read_fingerprint(fl_name):
    fp = []
    with open(fl_name,'r') as fin:
        for line in fin:
            fp.append(line.split())
    return [*fp[-1][0]]

def get_ss(fp):
    ss = []
    count = 1
    i = 0
    while i<len(fp)-1:
        if fp[i+1] == fp[i]:
            count += 1
            i += 1
        else:
            ss.append([fp[i], count])
            count = 1
            i += 1
    ss.append([fp[-1], count])
    return ss

def convert_to_fp(ss):
    fp = []
    for i in range(len(ss)):
        for j in range(ss[i][1]):
            fp.append(ss[i][0])
    return ''.join(fp)

def find_linkers(ss):
    linkers = []
    for i in range(len(ss)):
        if ss[i][0] == '-':
            linkers.append([i,ss[i][1]])
    return linkers

def find_sheet_breakers(ss):
    sheet_breakers = []
    for i in range(len(ss)):
        if ss[i-1][0] == 'S' and ss[i+1][0] == 'S':
            sheet_breakers.append(i)
    return sheet_breakers

def color_sheet_breakers(fp):
    ss = get_ss(fp)
    sb = find_sheet_breakers(ss)
    cols = []
    for i in range(len(ss)):
        if ss[i][0] != '-':
            for j in range(ss[i][1]):
                cols.append('rgb(229,99,23)')
        else:
            if i in sb:
                for j in range(ss[i][1]):
                    cols.append('rgb(229,99,23)')
            else:
                for j in range(ss[i][1]):
                    cols.append('rgb(0,154,68)')
    return cols
    