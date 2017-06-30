#!/usr/bin/env python3
import pandas as pd
import numpy as np
import sys 

# The data file needs to be tested
testFileName = sys.argv[1]
# The source of truth 
compareFileName = sys.argv[2]
# Read in the test file
testFile = pd.read_excel(testFileName, sheetname = 0, header=0)
# Fill NAN with zero
testFile.fillna(0, inplace=True)
# Read in the scorecard file 
scorecardData = pd.read_excel(compareFileName, sheetname = 0, header=0)

personIds = testFile['PERSON_ID']
comparePersonIds = scorecardData['PERSON_ID']
# Join two files by organisation description and year 
mergedData = pd.merge(personIds, comparePersonIds, indicator=True, how='outer')
# Compare mersures 
findMissings = mergedData[mergedData["_merge"] != "both"]
print(compareResult)
