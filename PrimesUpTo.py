# Python code​​​​​​‌​‌‌​​​​​‌‌‌​‌‌‌​​‌​​​‌‌‌ below
# Use print("messages...") to debug your solution.

def allPrimeFactors(num):
    primes = []
    i = 2
    factor = False
    while i < num:
        #print(i, " ", primes)
        for n in primes:
            if i % n == 0 and len(primes) != 0:
                factor = True
                break
        if num % i == 0 and factor == False:
            primes.append(i)
            i += 1
        else:
            factor = False
            i += 1
        
    return primes

print(allPrimeFactors(200))
#print(allPrimeFactors(51))

def allPrimesUpTo(num):
    primes = []
    i = 2
    while i < num:
        print(i)
        for n in primes:
            if i % n == 0 and len(primes) != 0:
                i += 1
                break
            else:
                primes.append(i)
                i += 1
    return primes

#print(allPrimesUpTo(20))
#print(allPrimesUpTo(51))