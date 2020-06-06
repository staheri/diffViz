# diffViz

An implementation of "diff" algorithm to visually show differences of a pair of two text-based files.

## Usage

```
$ python diffViz.py -h
usage: diffViz.py [-h] [--hideC] [--bw] [--legend] A B O

diffViz v1, Visualization of diff between a pair of text files

positional arguments:
  A           file A
  B           file B
  O           generate the final output <out>.pdf

optional arguments:
  -h, --help  show this help message and exit the program
  --hideC     Hides content of common nodes
  --bw        Enables black/white printer compatible graphs
  --legend    Include legend
```

## Prerequisites

You have to have [graphviz dot](https://www.graphviz.org/) installed.
