e=-2
d=8
for r in range(0,6):
        for c in range(0,7):
                if(r==0):
                        if(c==0 or c==3 or c==6):
                            print("_",end="")
                        else :
                            print("*",end="")
                if(r==1):
                  if(c==0 or c==3 or c==6):
                      print("*",end="")
                  else :
                      print("_",end="")
                if(r>=2 or r<=5):                            
                  if(e==c or d==c):
                    print("*",end="")
                  else:
                    print("_",end="")
        
        e=e+1
        d=d-1
        print()
                    
                    
                  
                            
                                
                
