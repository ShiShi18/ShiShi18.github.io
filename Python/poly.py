#p(x) =-1 + x^2 + 3x^7

p = {0:-1,2:1,7:3}
def eval_poly_dict(p,x):
    sum = 0
    for power in p:
        sum += x**power * p[power]
    return sum

print(eval_poly_dict(p,3))