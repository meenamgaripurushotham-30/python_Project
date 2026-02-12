print('_____PROCEDURAL PROGRAMMING_____')
num=11
if num>1:
    for val in range(2,num):
        if num%val==0:
            print('Not prime')
            break
    else:
        print('prime')

num=11
if num>1:
    for val in range(2,num):
        if num%val==0:
            print('Not prime')
            break
    else:
        copy=num
        res=0
        while num!=0:
            ld=num%10
            res=res*10+ld
            num//=10
        if res==copy:
            print('polyprime')
        else:
            print('Not polyprime')

num=121
copy=num
res=0
while num!=0:
    ld=num%10
    res=res*10+ld
    num//=10
if copy==res:
    print('polindrom')
else:
    print('Not polindrom')

num=6
sum=0
for val in range(1,num):
    if num%val==0:
        sum+=val
if sum==num:
    print('perfect')
else:
    print('Not perfect')

num=153
res=0
copy=num
power=len(str(num))
while num!=0:
    ld=num%10
    res+=ld**power
    num//=10
if copy==res:
    print('Armstrong')
else:
    print('Not Armstrong')

num=135
copy=num
res=0
power=len(str(num))
while num!=0:
    ld=num%10
    res+=ld**power
    power-=1
    num//=10
if copy==res:
    print('deserium')
else:
    print('Not deserium')

num=145
copy=num
res=0
while num!=0:
    ld=num%10
    fact=1
    for val in range(1,ld+1):
        fact*=val
    res+=fact
    num//=10
if res==copy:
    print('strong')
else:
    print('Not strong')

num=13
while num>9:
    res=0
    while num!=0:
        ld=num%10
        res+=ld**2
        num//=10
    num=res
if num==1 or num==7:
    print('Happy')
else:
    print('Not Happy')

pos=6
f=0
s=1
if pos==1 or pos==2:
    print(pos-1)
else:
    for val in range(pos-2):
        res=f+s
        f=s
        s=res
    print(res)

num=1234
res=0
pos=10**(len(str(num))-1)
while num!=0:
    ld=num%10
    res+=ld*pos
    pos//=10
    num//=10
print(res)

fact=1
num=5
for val in range(1,num):
    fact*=val
print(fact)
    
num1=7
num2=21
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
    else:
        lcm=lcm+1

num1=10
num2=25
if num1<num2:
    gcd=num1
else:
    gcd=num2
while True:
    if num%gcd==0 and num%gcd==0:
        print(gcd)
        break
    else:
        gcd=gcd-1
    
num=19
res=0
while num!=0:
    ld=num%2
    res=res*10+ld
    num//=2
print(res)

num=10011
power=0
res=0
while num!=0:
    ld=num%10
    res+=ld*(2**power)
    num//=10
    power+=1
print(res)
print('_____FUNCTIONAL PROGRAMMING_____')
def prime(num):
    if num>1:
        for val in range(2,num):
            if num%val==0:
                return False
        return True
num=11
print('prime'if prime(num)else'Not prime')
def polyprime(num):
    if num>1:
        for val in range(2,num):
            if num%val==0:
                return False
        return True
    return False

def squre(num,res=0):
    while num!=0:
        ld=num%10
        res=res*10+ld
        num//=10
    return res

num=11
print('polyprime'if squre(num)==num else'Not polyprime')

def polindrome(num,res=0):
    while num!=0:
        ld=num%10
        res=res*10+ld
        num//=10
    return res

num=121
print('polindrome'if polindrome(num)==num else'Not polindrome')

def perfect(num,sum=0):
    for val in range(1,num):
        if num%val==0:
            sum+=val
    return sum

num=6
print('perfect'if perfect(num)==num else'Not perfect')

def armstrong(num,power,res=0):
    while num!=0:
        ld=num%10
        res+=ld**power
        num//=10
    return res

num=153
print('Armstrong'if armstrong(num,len(str(num)))==num else'Not Armstrong')

def deserium(num,power,res=0):
    while num!=0:
        ld=num%10
        res+=ld**power
        power-=1
        num//=10
    return res
num=135
print('Disurem'if deserium(num,len(str(num)))==num else'not Disurem')

def strong(num,res=0):
    while num!=0:
        ld=num%10
        res+=fact(ld)
        num//=10
    return res
def fact(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
num=145
print('strong'if strong(num)==num else'Not strong')

def happy(num,res=0):
    while num!=0:
        ld=num%10
        res+=ld**2
        num//=10
    return res
def squre(num):
    while num>9:
        num=happy(num)
    return num==1 or num==7
num=19
print('Happy'if squre(num)else'Not Happy')

def fibonacci(pos):
    if pos==1 or pos==2:
        return pos-1
    return pos-2
pos=6
print('fibonacci'if fibonacci(pos)else'Not fibonacci')

def reverse(num,pos,res=0):
    while num!=0:
        ld=num%10
        res+=ld*pos
        pos//=10
        num//=10
    return res
num=1234
print('Reverse'if reverse(num,10**(len(str(num)))-1)else'Not Reverse')

def fact(num,fact=1):
    for val in range(1,num):
        fact*=val
    return fact
num=5
print('fact'if fact(num)else'Not fact')

print('_____RECURSIONS_____')

def prime(num,val=2):
    if val==num+1:
        return 0
    elif num%val==0:
        return 1+prime(num,val+1)
    else:
        return 0+prime(num,val+1)
num=11
print('prime'if prime(num)else'Not prime')

def polyprime(num,val=2):
    if val==num+1:
        return 0
    elif num%val==0:
        return 1+prime(num,val+1)
    else:
        return 0+prime(num,val+1)
num=11
print('polyprime'if polyprime(num)else'Not polyprime')

def polindrom(num):
    if num==0 or num==1:
        return 0
    return (num%10)*10+polindrom(num//10)
num=121
print('polindrom'if polindrom(num) else'Not polindrom')

def sum(num):
    if num==0:
        return 0
    return (num%10)+sum(num//10)
num=6
print('perfect'if sum(num)==num else'Not perfect')

def armstrong(num,power):
    if num==0:
        return 0
    return (num%10)**power+armstrong(num//10,power)
num=153
print('Armstrong'if armstrong(num,len(str(num)))==num else'Not armstrong')

def deserium(num,power):
    if num==0:
        return 0
    return (num%10)**power+deserium(num//10,power-1)
num=135
print('deserium'if deserium(num,len(str(num)))==num else'Not deserium')

def strong(num):
    if num==0:
        return 0
    return fact(num%10)+strong(num//10)
def fact(num):
    if num==0:
        return 1
    return  num*fact(num-1)
num=145
print('strong'if strong(num)==num else'Not strong')

def squre(num):
    if num==0:
        return 0
    return (num%10)**2+squre(num//10)
def happy(num):
    if num<10:
        return num==1 or num==7
    return happy(squre(num))
num=19
print('Happy'if happy(num)else'Not Happy')

def fibonacci(pos):
    if pos==1 or pos==2:
        return pos-1
    return fibonacci(pos-1)+fibonacci(pos-2)
pos=6
print('fibonacci'if fibonacci(pos)else'Not fibonacci')

def revers(num,pos):
    if num==0:
        return 0
    return (num%10)*pos+revers(num//10,pos//10)
num=1234
print('Revers'if revers(num,10**(len(str(num)))-1)else'Not Revers')

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
num=5
print('factorial'if fact(num)else'Not factorial')
