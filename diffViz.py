#!/usr/bin/env python
# Author: Saeed Taheri, University of Utah, staheri@cs.utah.edu, 2018, All rights reserved
# Code: diffViz.py
# Description: Takes two text files and generate their diffViz (dot & pdf)


import sys,subprocess
import diffCore as diff
import vis
import argparse


# Read arguments
parser = argparse.ArgumentParser(description='diffViz v1, Visualization of diff between a pair of text files')
parser.add_argument('file_A', metavar='A', help='file A')
parser.add_argument('file_B', metavar='B', help='file B')
parser.add_argument('out', metavar='O', help='generate the final output <out>.pdf ')
parser.add_argument('--hideC', dest='hideC', action="store_true", default=False, help='Hides content of common nodes')
parser.add_argument('--bw', dest='bw', action="store_true", default=False, help='Enables black/white printer compatible graphs')
parser.add_argument('--legend', dest='l', action="store_true", default=False, help='Include legend')
args = vars(parser.parse_args())

pathA = args["file_A"] # A
pathB = args["file_B"] # B
pathO = args["out"] # Out
showC = not args["hideC"] # showCommon
bw    = args["bw"] # black and white
l     = args["l"] # include legened

pathAlines = [x.strip() for x in open(pathA,"r").readlines() if len(x) > 0]
pathBlines = [x.strip() for x in open(pathB,"r").readlines() if len(x) > 0]

nm = pathA.rpartition("/")[2].rpartition(".")[0]+"_"+pathB.rpartition("/")[2].rpartition(".")[0]
fe = diff.lcs(pathAlines,pathBlines)
diffViz = vis.edit2dot(fe,nm,showC,bw,l)
finalDot= "digraph \"diffViz\""+diffViz+"\n\t"
f = open(nm+".dot","w")
f.write(finalDot)
f.close()
process = subprocess.Popen("dot -Tpdf "+nm+".dot -o "+pathO+".pdf", stdout=subprocess.PIPE,shell=True)
si, err = process.communicate()
