import math

def get_pi(num):
  if check_pi(num):
    return round(math.pi,num)  
  else:
    return "Limite estourado"

def check_pi(n2):    
    if n2 > 15:
        return False
    else:
        return True