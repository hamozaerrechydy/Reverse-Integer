def int_to_list(num): 
  num = list(str(num))
  #num = [int(i) for i in num]
  return num 

def s(l): 
  NL = []
  if l[0] == "-": 
    NL.insert(0, "-")
    l.remove(l[0]) 
  for x in range(len(l)):
    NL.append(max(l))
    l.remove(max(l))
    
  return NL

def list_to_int(l): 
    a = "".join(l) 
    return int(a) 
  
def reverse(x):
  return list_to_int(s(int_to_list(x)))

print(reverse(-123))
