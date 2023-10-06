def Ex_GCD(a ,b):
   if b == 0:
      return (a,1,0)
   g , s_prime , t_prime = Ex_GCD(b,a%b)
   s = t_prime
   t = s_prime - (a//b)*t_prime
   return (g,s,t)
a , b , n = input().split()
a = int(a)
b = int(b)
n = int(n)
gcd , s_gcd , t_gcd = Ex_GCD(n,b)
print(a*t_gcd%n)



