# Vertcounter

Vertcounter is a python command line tool for reading GPX tracks and adding up their total vert. I used it to keep track of my total vertical feet in a season of backcountry skiing. 

## Install

Install vertcounter directly from this repo by running: 

```
$ python -m pip install "git+https://github.com/jackdeansmith/vertcounter"
```

You can then run vertcounter directly:
```
$ vertcounter --help
```

## Usage 

```
Usage: vertcounter [OPTIONS] DIRECTORY

  Analyze GPX files in a directory and output the total vertical distance
  traveled uphill.

Options:
  --unit [f|m]  Unit to output total vert in  [default: f]
  --help        Show this message and exit.
```