# -*- coding: utf-8 -*-
"""Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1QNKlYY5G9cje1ssdfT9AJ8RTv0IizdWw
# Management merge per month and year
The aim of this script is to provide a table 
with month and year reported as field.
"""
#import pands, numpy and pathlib

def write_month_year(i, year):
  # This function given in input the month and 
  # the year return the respective format "mm/yyyy".
  # It works like the break structure in C so it is not reported
  # to don't stress the reader

#Given in input the year this function create 
# the output dataframe by containaing
# the different month and creating a field 
# with the corresponding Month and year
def analysing_year(year):
  for i in {
          #month of the year as string
          }:
      p = dataframe[["CODICE", i, "DESCRIZIONE"]].rename(
        columns={"CODICE":"Code_Line",i:"km","DESCRIZONE":"Description"})
      p["Month-Year"]=write_month_year(i,year)
      output=pd.concat([output,p])

#Now call in input the different 
# Excel file and call the previous function
output = pd.DataFrame(columns={"Code_Lmonthne",
                "DESCRIZIONE","Month-Year","km"})
filename = "KM_BTS_"
for year in {"2017","2018","2019","2020","2021"}:
  dataframe = pd.read_excel(io=Path(filename+year),
                          sheet_name="Totale", usecols="A:N", nrows=15)
  dataframe = dataframe.drop(dataframe.index[0])
  analysing_year(year)
output.to_excel("mileage.xlsx")