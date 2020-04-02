#!/usr/bin/python

#
# Course:       CCPS 109
# Lab:          3 File IO and Modules
# Due Date:     Mar 16th @ 23:00 hrs
#
# Student:      Sivatma Maharaj
# Student ID:   501043693

def convertFtoC(listF):
  # Converts a list of temperatures in Fahrenheit to a list of temperatures in Celsius
  listC = []
  for tempF in listF:
    tempC = round((tempF - 32) * 5 / 9, 2)
    listC.append(tempC)
  return listC

def averageTemp(listC):
  # Calculates the average temperature from a list of temperatures
  average = 0
  sumOfTemp = 0
  for tempC in listC:
    sumOfTemp += tempC
  average = sumOfTemp / len(listC)
  return round(average, 2)

def maxminTemp(listC):
  # Returns the max and minimum values in a list of temperatures
  maxTemp = max(listC)
  minTemp = min(listC)
  return (maxTemp,minTemp)