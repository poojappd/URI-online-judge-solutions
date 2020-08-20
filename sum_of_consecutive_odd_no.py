x=int(input())
y=int(input())
sum=0
if x>y:
    lst=(y,x)
else:
    lst=(x,y)
for i in range(lst[0]+1,lst[1]):
    if(i%2!=0):
        sum+=i
print(sum)
         
       
