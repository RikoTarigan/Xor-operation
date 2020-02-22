def xor(a,b):
    for i in range(len(a)):
        if(a[i]=="1" and b[i]=="1"):
            print("0",end="")
        elif(a[i]=="1" and b[i]=="0"):
            print("1",end="")
            
        elif(a[i]=="0" and b[i]=="1"):
            print("1",end="")
        elif(a[i]=="0" and b[i]=="0"):
            print("0",end="")
            
a=input("x : ").split()
b=input("y : ").split()

for i in range(3):
    xor(a[i],b[i])
    print("",end=" ")
    

    
