n=int(input("enter the no."))
s=n
sum_f=0
while s>0:
    f=1
    dig=s%10
    if dig>1:
        for i in range(2,dig+1):
            f=f*i
    sum_f=sum_f+f
    s=s//10
if sum_f==n:
    print("krishnamurthy no.")
else:
    print("not krishnamurthy no.")



