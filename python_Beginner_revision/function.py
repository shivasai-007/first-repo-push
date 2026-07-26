def hello():
    print("hello ")

hello()

def enven_num(x):
    print( "even" if x % 2 ==  0  else  "odd")

enven_num(9)

def mysum(*numbers):
    asum = 0 
    for x in numbers:
        asum += x 
    print(asum)

mysum(1,2,3,4,5,6,7,8,9,10)