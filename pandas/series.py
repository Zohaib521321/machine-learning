import pandas as pd
# Print Series
mySeries=[7,8,19,10,9]
print(pd.Series(mySeries))
print("First Row is "+str(mySeries[0]))
# Make custom labels
customIndex=['A','B','C','D','E']
arrangedSeries=pd.Series(mySeries,customIndex)
print(f"Arranged Series is\n {arrangedSeries}")

