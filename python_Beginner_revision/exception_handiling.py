try :
    x = int (input ("enter the number : "))
    y = int (input ("enter the number : "))
    print(x + y )

except ValueError :
    print("pls enter a valid number next time  ")


print("shivsai")

#  raise expraction :

def  some_functoin():
    if True :
        raise ValueError("something went very wrrong ")
some_functoin()
# The assert keyword in Python is a debugging aid that tests whether a specific condition 
# in your code evaluates to True. If the condition is met, the program continues its normal flow;
# if the condition evaluates to False, Python immediately halts execution and raises an AssertionError
x = 10 
y = 10
assert( x > y )
