# num = input('enter a number')
# num = int(num)

def is_prime(num):
    if num < 2:
        print('number is not prime')
    else:
        i = 2
        is_prime = True
        while i*i <= num:
            if num % i ==0:
                is_prime = False
                break
            i = i + 1
    if is_prime:
        return True
    else:
        return False

name = input('Hey! Please enter your name : \t')
num1 = int(input('Enter your first favourite number : \t'))
num2 = int(input('Enter your second favourite number : \t'))
num3 = int(input('Enter your third favourite number : \t'))

print(f' \n{name} let''s explore your favourite numbers: \n')

num_list = [num1, num2, num3]
list_state = []

for num in num_list:
    if num % 2 == 0:
        list_state.append(num)
        list_state.append('even')
    else:
        list_state.append(num)
        list_state.append('odd')

tuple1 = (list_state[0:2])
tuple2 = (list_state[2:4])
tuple3 = (list_state[4:6])
list_tuples = [tuple1, tuple2, tuple3]

for tuple in list_tuples:
    print(f'The number {tuple[0]} is {tuple[1]}')

res = []

for num in num_list:
    res.append((num, num*num))

for tuple in res:
    print(f'The number {tuple[0]} is and is square: {tuple}')

sum = 0

for num in num_list:
    sum += num

print(f'Amazing. The sum of your favourite numbers is {sum}')
prime = is_prime(sum)
if prime:
    print(f'Wow, {sum} is a prime number')
else:
    print(f'{sum} is not a prime number')

    
        



