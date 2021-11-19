h=int(input("Enter Height"))
if(h%2==1):
        s=(h//2+1)
        a=h//2+1
else:
        s=h//2
        a=h//2
j=s-1
for r in range(h):
        if(r<(a)):
                s-=1
                y=h//2
                while(y>s):
                        print(" ",end="")
                        y-=1
                z=0
                while(z<=r):
                        print("*",end="")
                        z+=1
        else:
                if(h%2==1):
                        j-=1
                        s+=1
                y=h//2
                while(y>s):
                        print(" ",end="")
                        y-=1
                z=0
                while(z<=j):
                        print("*",end="")
                        z+=1                
                if(h%2==0):
                        s+=1
                        j-=1
        print()   
