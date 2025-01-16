# taking input from the user (a ,b)  and need to convert them to integers to avoid type error in range.
a = int(input("enter a: "))
b = int(input("enter b: "))
#initializing prime sum as 0 to store all the  sum of prime numbers
prime_sum = 0
# used a + 1 because a could also be a prime number and will create disturbances in the answer
for num in range(a + 1, b):
    # to check if the number is greater than 1 and less than 1 are not considered as prime numbers
    if num > 1:
        is_prime = True
        # this block checks if the number is prime or not
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
            # checks if the number is still prime or not by true or false
        if is_prime:
            # if the number is prime then add it to the sum of the prime numbers
            prime_sum += num
        
# checks if b is greater than a or not
if b > a:
    print(f"Sum of primes between {a} and {b}: {prime_sum}")
# if b is smaller then the following statement will print!!
else :
    print ("b should be greater than a")
