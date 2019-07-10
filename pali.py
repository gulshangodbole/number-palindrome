a=input("enter")

while(a>0):
    d=a%10
    while(a>=10):
        a/=10
    if(d==a):
        print "wins"
        break
    else:
        print "loss"
        break
