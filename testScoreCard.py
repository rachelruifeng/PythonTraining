#!/usr/bin/env python3
import pandas as pd
import numpy as np
import sys 

# The data file needs to be tested
testFileName = sys.argv[1]
# The source of truth 
scoreCardFileName = sys.argv[2]
# The mesurement ID　we want to test
scoreCardMeasureName = sys.argv[3] 
# Read in the test file
testFile = pd.read_excel(testFileName, sheetname = 0, header=0)
# Fill NAN with zero
testFile.fillna(0, inplace=True)
# Read in the scorecard file 
scorecardData = pd.read_excel(scoreCardFileName, sheetname = 0, header=0)
# Filter by the measurement ID 
filteredScoreCardData = scorecardData.loc[scorecardData['SCORECARD_MEASURE_ ID'] == scoreCardMeasureName]
# Read in University actual data 
uniActualData = pd.read_excel(scoreCardFileName, sheetname = 2, header=0)
# Filter by the measurement ID 
filteredUniData = uniActualData.loc[uniActualData['SCORECARD_MEASURE_ ID']== scoreCardMeasureName]
# Join two files by organisation description and year 
mergedData = pd.merge(testFile, filteredScoreCardData, left_on = ['ORG_DESCR', 'YEAR'], right_on = ['ORG_UNIT','YEAR'])
# Compare mersures 
compareResult = mergedData.loc[np.isclose( mergedData['MEASURE_x'],  mergedData['MEASURE_y'], rtol=1e-5) == False]
print(compareResult)

# Merge uni acutal data  
mergedUniData = pd.merge(testFile.loc[testFile['ORG_DESCR'] == 'Univerity of New South Wales'], filteredUniData, left_on = ['YEAR'], right_on = ['YEAR'])
# Compare 
compareUniData = mergedUniData.loc[np.isclose( mergedUniData['MEASURE_x'],  mergedUniData['MEASURE_y'], rtol=1e-5) == False]
print(compareUniData)
