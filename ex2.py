import sys 
  
  
for i in sys.stdin: 
    if 'a' == i.rstrip(): 
        break
    print(f'Input : {i}') 
  
