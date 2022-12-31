#a pair of integers (A, B) equivalent if there exist some positive integers X and Y such that A^X = B^Y
#Given AA and BB, determine whether the pair is equivalent or not.

#1728=2^6*3^3
#12=2^2*3
#lcm of smallest prime factor is lcm(6,2)=6
#x=6/6=1 and y=6/2=3 
#12^3=1728

# create cache for storing smallest prime factor of a number 
cache=[i for i in range(1000001)]
for i in range(2,1000001):
    for j in range(i*i,1000001,i):
        if cache[j]==j:
            cache[j]=i

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
   
mod=1000000007
def check(a,b):
    # if smallest prime factor of both number are not same then they never be equal because we need same sets of prime factor
    if cache[a]!=cache[b]:
        return "NO"
    p=q=0
    # In spa and spb get the number of occurence of smallest prime factor in a and b respectively
    spa=cache[a]
    spb=cache[b]
    
    # In p get the number of occurence of smallest prime factor of a
    while a%spa==0:
        a=a//spa
        p+=1
    # In q get the number of occurence of smallest prime factor of b
    while b%spb==0:
        b=b//spb
        q+=1
    lcm=compute_lcm(p,q)
    # in both a and b lcm of all factor should be same 
    x=lcm//p 
    y=lcm//q 
    a1=pow(a,x)%mod 
    b1=pow(b,y)%mod 
    return "YES" if a1==b1 else "NO"
t=int(input())
while t!=0:
    a,b=map(int,input().split(" "))
    print(check(a,b))
    t-=1
