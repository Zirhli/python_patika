

list_1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list_2=[]

def flatten(list_1):
  for i in list_1:
    if isinstance(i,list):
      flatten(i)
    else:
      list_2.append(i)

flatten(list_1)

print(list_2)


    
