numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True #я понимаю, что это по заданию, но не c простой переменной было бы куда быстрее и красивше, как по мне
for i in numbers:
    if i < 2:
        del i
        continue
    is_prime = True
    for z in (range(2, i)):
        if i % z == 0:
            not_primes.append(i)
            break
        is_prime = False
    else:
        primes.append(i)


print('primes is ', primes)
print('Not primes is', not_primes)


