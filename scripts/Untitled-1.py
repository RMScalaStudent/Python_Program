def factorial(n):
    result = n
    start = n
    
    while n >0: # The while loop should execute as long as n is greater than 0
        n-=1  # Decrement the appropriate variable by -1
        result *= n # Multiply the current result by the current value of n

#        print(n, " " ,start , " ", result , " ")
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1