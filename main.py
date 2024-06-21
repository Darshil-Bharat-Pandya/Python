import pandas as pd 
a=pd.DataFrame({'Name':['Ayush','Riddhima','Nidhi'],'Age':[10,20,30],'BG':['A+','B+','C+']})
print(a)

# Q. WAP to add additional column in existing dataframe.
a['hobby']=['tv','walking','reading']
print(a)
