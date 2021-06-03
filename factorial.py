# 3! = 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * n-1 * n-2 * .. * 1

def factorial(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n-1)
        
    #print(f"calculating factorial for: {n} = {result}")
    
    return result
        
result = factorial(5)
print(f"{result}")



#   result = 5 * factorial (4)
#                   result = 4 * factorial(3)
#                                   result = 3 * factorial(2)
#                                                   result = 2 * factorial(1)
#                                                                   result = 1
                       