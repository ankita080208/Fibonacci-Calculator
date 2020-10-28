#finding the fibonacci series using recursive method.
#defining the function.
def fibonacci(n):
#if the given input is less than or equal to 1 then return the following.
    if n <= 1:
        return n
#if the given input is greater than 1 then return the following.
    else:
        return (fibonacci(n-1) + fibonacci(n-2)) 
#storing the input as integer datatype given by user in a variable.
n= int(input("Enter you number = "))
#printing the result.
print("fibonacci series is -")
for i in range(n):
   print(fibonacci(i)) 
#end of code.
