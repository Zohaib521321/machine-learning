import pandas as pd
import numpy as np
from numpy.random import randn 

myData=randn(1000,3)
myColumn=["Monday","Tuesday","Thursday"]
#  save to csv
myDF=pd.DataFrame(myData,columns=myColumn)
print(myDF.head())
# myDF.to_csv("randomData.csv",index=False)
loadedDf=pd.read_csv("randomData.csv")
print(loadedDf.head())

print("\nSummery Statistics of the data\n")
print(loadedDf.describe())
loadedDf["Friday"]=randn(1000)
print("\nLoaded data frame after adding friday\n")
print(loadedDf.head())
print(f"\n Total Counts are \n{loadedDf.count()}")
# save into json file
jsonFile=loadedDf.to_json("random.json",lines=True,orient="records")
