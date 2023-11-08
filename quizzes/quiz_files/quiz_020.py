import random
random.seed(1234)

def produce(n:int, m:int, s:int)-> float:
    out = f"|{'x'.center(10)}|{'y(x)'.center(10)}|\n"
    for n in range(5):
        x = random.randint(0,100)
        y = x**(0.5*((m/s)**2))
        out += f"|  {str(x:20d).center(8)}  |  {str(y:20d).center(8)}  |\n"
    return out

print(produce(n=5, m=3, s=2))