## Table of Contents
- [General Info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)

## General Info
In this mini-project, my goal was to create a program to produce a report of the total number of accidents per make and per year of the vehicle. The following steps were executed:

- Filter out accidents with make and year
- Count number of accident occurrences for the vechicle make and year

## Technologies
Mini-project is created with: 
* Python 3.8.3

## Setup
To run this mini-project, follow the steps below:

1. ```$ git clone https://github.com/BenGriffith/post-sale-automobile.git```
2. 
```
$ cd sample
$ cat data.csv | python autoinc_mapper1.py | python autoinc_reducer1.py | python autoinc_mapper2.py | python autoinc_reducer2.py | sort