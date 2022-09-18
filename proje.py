list_1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list_2=[]
def flatten(x):
  for i in x:
    if isinstance(i,list):
      flatten(i)
    else: 
      list_2.append(i)
print(list_2)
      
    
