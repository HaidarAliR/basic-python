# g = lambda x:3*x+1
# print(g(2))

def quad_equation(a,b,c):
    return lambda x: a*x**2+b*x+c

y = quad_equation(2,3,-5)(0)

print(y)