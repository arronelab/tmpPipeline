#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:16:28 2022

@author: ccck67
"""
import sys

def get_subsections(ss):
    sses = []
    count = 1
    i = 0
    while i<len(ss)-1:
        if ss[i+1] == ss[i]:
            count += 1
            i += 1
        else:
            sses.append([ss[i], count])
            count = 1
            i += 1
    sses.append([ss[-1], count])
    return sses

def list_linkers(test_name):
    ss = []
    with open(test_name+'fingerPrint1.dat','r') as fin:
        for line in fin:
            ss.append(line)
    ss = get_subsections(ss[-1])
    linkers = []
    for i in range(len(ss)):
        if ss[i][0] == '-':
            linkers.append(str(i))
    return linkers

def ask_varying_sectionSecondary(test_name):
    fix_all = input('Would you like to allow all subsections of your structure to change? (Y/N)\n')
    if fix_all == 'Y':
        pass
    else:
        edit_linkers = input('Would you like to just vary all linker subsections? (Y/N)\n')
        if edit_linkers == 'Y':
            varying_sections_list = list_linkers(test_name)
        else:
            varying_sections_string = input('List the subsections you would like to vary. E.g. 1 2 3 5 8\n')
            varying_sections_list = varying_sections_string.split()
        with open(test_name+'varyingSectionSecondary1.dat','w+') as f:
            for i in varying_sections_list[:-1]:
                f.write(i+'\n')
            f.write(varying_sections_list[-1])
         
if __name__ == '__main__':
    ask_varying_sectionSecondary(sys.argv[1])