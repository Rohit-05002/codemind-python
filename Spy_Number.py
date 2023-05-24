n=int(input())
Sum=0
pro=1
while n!=0:
    r=n%10
    Sum=Sum+r
    pro=pro*r
    n=n//10
if Sum==pro:
    print('Spy Number')
else:
    print('Not Spy Number')