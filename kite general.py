h1=int(input("enter height"))
h2=(h1-3)//3
h=h1-h2
s=h//2+1
j=-1
for r in range(h):
        if(r<=(h//2)):
                s-=1
                y=0
                while(y<s):
                        print("  ",end="")
                        y+=1
                z=0
                j+=2
                while(z<j):
                        print("*",end="")
                        z+=1
        else:
                s+=1
                j-=2
                y=0
                while(y<s):
                        print("  ",end="")
                        y+=1
                z=0
                while(z<j):
                        print("*",end="")
                        z+=1
        print()
for a in range(h2):
        s-=1
        y=0
        while(y<s):
                print("  ",end="")
                y+=1
        z=0
        j+=2
        while(z<j):
                print("*",end="")
                z+=1
        print()
