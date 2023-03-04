<<<<<<< HEAD
def is_prime(num):

    for i in range (2, num):
        if (num % i) == 0:
            return False
    
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
=======
def is_prime(num):

    for i in range (2, num):
        if (num % i) == 0:
            return False
    
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
>>>>>>> dfd5fcc97c4e4339a5e4684ceb9fc1247b7c2ddc
print()