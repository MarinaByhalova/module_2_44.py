numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
j = 0
for j in range(len(numbers)):
    number = numbers[j]
    amount = 0
    if number != 1:
        i = 0
        for i in range(number):
            if number%(i+2) == 0:
                amount = amount + 1
            i = i+1

        if amount == 1:
            primes.append(number)
        else:
            not_primes.append(number)
    j=j+1

print(f'Primes:{primes}')
print(f'Not_primes:{primes}')