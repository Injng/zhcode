import math

def 是否质(数):
  for i in range(1,int(math.sqrt(数)+ 1)):
    if 数% i== 0:
      print("合")
      return 
    else :
      pass 
  print("质")
