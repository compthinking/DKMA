---
layout: post
permalink: /calendar/
title: asg2
titleheader: Assignment 2
nav: true
description: Assignment 2 Description
showtitle: true
date: 2021-06-14
---

For ECE 657A Spring 2021 course at the University of Waterloo.

## Links
- **Dataset:** link to csv TODO
- **Kaggle Competition:** link to kaggle TODO

## Dataset Sources
The DKMA Covid Dataset was acquired from the following sources:
- John Hopkins TODO
- Demographic something, US Census year... TODO

The datapoints describe various information about the population and Covid pandemic situation in *50 US States* and over each day of the month of *January 2021*. Each record gives Covid information for that day and demographic data for the whole state as well. Note the demographic data is duplicated for each state since for all days since it doesn't change that quickly and is based on data from the last census.

## Field Description
The DKMA Covid Dataset has the following fields.


- **Day**: Date in January 2021 ranging from Jan 2 to Jan 31.
- **State ID**: Arbitrary ID number for each state, based on alphabetical order. Note there are 51 states since the District of Columbia is also included.
- **State**: Name of the US State.
- **Lat**: Latitude for the geographic centre of the state.
- **Long_**: Longitude for the geographic centre of the state. 
- **Active**: Number of active, tracked COVID-19 cases that day in that state.
- **Incident_Rate**: 
- **Total_Test_Results**: 
- **Case_Fatality_Ratio**: 
- **Testing_Rate**: 
- **Resident Population 2020 Census**: 
- **Population Density 2020 Census**: 
- **Density Rank 2020 Census**: 
- **SexRatio**: 
- _StateGroup_: This is an added field that groups various US states together for analysis purposes and to allow us to hold out some states for testing on kaggle.

## Label Description
The labels for this dataset 
- **Confirmed**: 
- **Deaths**: 
- **Recovered**: 
