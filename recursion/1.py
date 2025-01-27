def myPow(x: float, n: int) -> float:
        ##base cond 
    if n==0:
        return 1
    return x * myPow(x,n-1)

print(myPow(2.00,10))