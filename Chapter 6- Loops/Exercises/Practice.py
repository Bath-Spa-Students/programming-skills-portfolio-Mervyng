# While Loops
i=1
while i<10:
    print(i)
    i+=1 

idk =1
while idk <=5:
    print("idk is:",idk)  
    idk=idk+1  

#J=j+1 Both are Same
A =1
while A<8:
    print(A)
    if A==8:
        break
    A=A+ 1

#For Loops
Food= ["Apple","Banana","Cherry"]
for x in range(10):
     print(x,end=" ")

#step count
for x in range (0,20,9):
    print(x,end = ",")

#user input
N=int (input("Enter Max number for range:" ))
for x in range (0,N,10):
    print(x,end=",")

#Loop contorl through Sentinels values
Sum =0
while True:
    x=float(input('enter Number:'))
    sum+=x
    if x==-1:
        break
    print(sum)
#exclusive
for x in range(10,8):
    print(x)