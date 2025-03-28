
#task  function for all arthematic oprerations 28-03-25

n1 =int(input())
n2 =int(input())

def addition(a,b):
    return a+b
print(addition(n1,n2))

def sub(c,d):
    return c-d
print(sub(n1,n2))

def mul(e,f):
    return e*f
print(mul(n1,n2))

def div(g,h):
    return g%h
print(div(n1,n2))

def doublediv(i,j):
    return i//j
print(doublediv(n1,n2))

#using lamda function

addition1= lambda A,B : A+B
total=addition1(n1,n2)
print(total)

sub1 = lambda C,D : C-D
s = sub1(n1,n2)
print(s)

mul1 = lambda E,F : E*F
m = mul1(n1,n2)
print(m)

div1 = lambda G,H : G%H
k = div1(n1,n2)
print(k)

fdiv = lambda I,J : I//J
t = fdiv(n1,n2)
print(t)
