s=8
z=0
for x in range(0,17):
        if(x<4):
                y=0
                while(y<s):
                        print(" ",end="")
                        y+=1
                a=1
                z+=2
                while(a<z):
                        if(a==1 or a==z-1):
                                print("*",end="")
                        else:
                                print(" ",end="")
                        a+=1
                
                s-=1
        if(x==4 or x==12):
                a=1
                while(a<=17):
                        if(a<=5 or a>12):
                                print("*",end="")
                        else:
                                print(" ",end="")
                        a+=1
        if(x>=5 and x<=11):
                for y in range(0,17):
                        if(x==5 or x==11):
                                if(y==1 or y==15):
                                        print("*",end="")
                                else:
                                        print(" ",end="")
                        if(x==6 or x==10):
                                if(y==2 or y==14):
                                        print("*",end="")
                                else:
                                        print(" ",end="")
                        if(x==7 or x==9):
                                if(y==3 or y==13):
                                        print("*",end="")
                                else:
                                        print(" ",end="")
                        if(x==8):
                                if(y==4 or y==12):
                                        print("*",end="")
                                else:
                                        print(" ",end="")
        if(x>=13):
                y=0
                while(y<(s+1)):
                        print(" ",end="")
                        y+=1
                a=1
                while(a<z):
                        if(a==1 or a==z-1):
                                print("*",end="")
                        else:
                                print(" ",end="")
                        a+=1
                z-=2
                s+=1              
        print()
