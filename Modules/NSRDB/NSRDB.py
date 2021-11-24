#Conversion of WeatherData_Extractor from matlab to python
#Author: Chris Crouch

import numpy as np
import pandas as pd

from CodesFromSwefa import *

def WeatherData_Extractor(WDI,SP,WeatherData_FileName):         #WDI = HEMSWeatherData_input, SP = Simulation_Params
    FullData = np.genfromtxt(WDI.WeatherDataFile_Path, delimiter = ",")
    
    #Get the date time matrix fir 4 rows and all colums
    DateTime_Matrix = FullData[:, 0:4]
    [rows, cols] = DateTime_Matrix.shape
    
    EndTime=24-(SP.FileRes/60)
    
    DateTimeMatrixAggregate_ForSlicer= np.concatenate((DateTime_Matrix, np.zeros((rows,1))))
        
    dictvals = DateTimeSeriesSlicer(DateTimeMatrixAggregate_ForSlicer, 1, WDI.FileRes, WDI.StartYear, WDI.EndYear, WDI.StartMonth, WDI.EndMonth, WDI.StartDay, WDI.EndDay,WDI.StartTime, WDI.EndTime)
    StartIndex_Aggregate = dictvals['StartIndex']
    EndIndex_Aggregate = dictvals['EndIndex']
    
    
    Ws = FullData[StartIndex_Aggregate:EndIndex_Aggregate+1][15]    #Double check all these indicies
    T_am = FullData[StartIndex_Aggregate:EndIndex_Aggregate+1][20]  
    GHI = FullData[StartIndex_Aggregate:EndIndex_Aggregate+1][6]
    DNI = FullData[StartIndex_Aggregate:EndIndex_Aggregate+1][5]
    
    counter = 0
    
    DateTimeVector = []
    for i in range(StartIndex_Agggregate, EndIndex_Aggregate+1, 1):
        counter += 1
        Day = DateTimeMatrix[i][0]
        Month = DateTimeMatrix[i][1]
        Year = DateTimeMatrix[i][2]
        Time = DateTimeMatrix[i][3]
        
        [hr, minn, sec] = DeciToHm(Time)
        
        #Does this need to be formatted someway or is it just for dispaly?
        DateTimeVector.append(DateTime(Year, Month, Day, hr, minn, sec))
    
    HEMSWeatherData_Output = {'Ws': Ws, 'T_am':T_am, 'GHI':GHI, 'DNI':DNI, 'DateTimeVector':DateTimeVector, 'DateTime_Matrix':DateTime_Matrix}
    
    df = pd.DataFrame(data = HEMSWeatherData_Output)
    df.to_excel('HEMSWeatherData_Output.xlsx', index = False, header = False)
    
    Day_Data = FullData[StartIndex_Aggregate:EndIndex_Aggregate,:]
    
    #Not sure what this is doing
    for i in range(360):
        if i == 1:
            SingleDay_WeatherFile_1 = Day_Data
        SingleDay_WeatherFile_1 = np.vstack(SingleDay_WeatherFile_1, DayData)
    
    return HEMSWeatherData_Output
        
    
    
    
    
        
        