#!/usr/bin/python

#
# Course:       CCPS 109
# Lab:          3 File IO and Modules
# Due Date:     Mar 16th @ 23:00 hrs
#
# Student:      Sivatma Maharaj
# Student ID:   501043693

import weatherstat

month = {"1":"JAN","2":"FEB","3":"MAR","4":"APR","5":"MAY","6":"JUN"}
weather = {}
weather_avg = {}
weather_maxmin = {}


# open the data file and load the data into a dictionary object: weather
# use the month dictionary object to look up the first value in each line of data
# use the converted first value as the key in the weather dictionary
#
# note: using a dictionary object eliminates any duplicate records, 
# it assigns the last record in the file to any duplicated keys.
fin = open("weather_data.dat", "r")

for line in fin:
  monthly_record = line.split(",")
  first_item = monthly_record[0]
  monthname = month[first_item]
  monthly_record.remove(first_item)
  for item in monthly_record:
    monthly_record[monthly_record.index(item)] = float(item)
  weather[monthname] = monthly_record
   

fin.close()

# Use the weatherstat functions to transform the data
# Use dictionary objects to store the averages and max/min temperatures for each month
for key in weather.keys():
  weather[key] = weatherstat.convertFtoC(weather[key])
  weather_avg[key] = weatherstat.averageTemp(weather[key])
  weather_maxmin[key] = weatherstat.maxminTemp(weather[key])


# Print out the values in the dictionaries
#
# Note: As a consequence of a using a dictionary the order is not fixed when it is iterated over
# and so the order of each key must be explictly stated.

fout = open("weathreport.txt", "w")
fout.write("Daily temperature records (c):\n")
fout.write("JAN: "+str(weather["JAN"])+"\n")
fout.write("FEB: "+str(weather["FEB"])+"\n")
fout.write("MAR: "+str(weather["MAR"])+"\n")
fout.write("APR: "+str(weather["APR"])+"\n")
fout.write("MAY: "+str(weather["MAY"])+"\n")
fout.write("JUN: "+str(weather["JUN"])+"\n")

fout.write("\nMonthly temperature summary:\n")
fout.write("Month\t\t\tAvg Temp (c)\t\t\thigh  /  low (c)\n")
fout.write("JAN{0:13.2f}{1:17.2f} / {2:=6.2f}\n".format(weather_avg["JAN"],weather_maxmin["JAN"][0],weather_maxmin["JAN"][1]))
fout.write("FEB{0:13.2f}{1:17.2f} / {2:=6.2f}\n".format(weather_avg["FEB"],weather_maxmin["FEB"][0],weather_maxmin["FEB"][1]))
fout.write("MAR{0:13.2f}{1:17.2f} / {2:=6.2f}\n".format(weather_avg["MAR"],weather_maxmin["MAR"][0],weather_maxmin["MAR"][1]))
fout.write("APR{0:13.2f}{1:17.2f} / {2:=6.2f}\n".format(weather_avg["APR"],weather_maxmin["APR"][0],weather_maxmin["APR"][1]))
fout.write("MAY{0:13.2f}{1:17.2f} / {2:=6.2f}\n".format(weather_avg["MAY"],weather_maxmin["MAY"][0],weather_maxmin["MAY"][1]))
fout.write("JUN{0:13.2f}{1:17.2f} / {2:=6.2f}\n".format(weather_avg["JUN"],weather_maxmin["JUN"][0],weather_maxmin["JUN"][1]))


fout.close()