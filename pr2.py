#1
a = 6
b = 9

print(f'Завдання 1: \n a = {a} \n b = {b}')

#2

print(f'Завдання 2: \n', a<b and a>3, b<10 and a < 10, a>b and b==7, b<a and a<2)

#3
print(f'Завдання 3: \n', a<b or a>3, b<10 or a < 10, a>b or b<7, b<a or a<2)

#4
var_str = 'Hello World'
var_str2 = 'hello world'

print('Завдання 4: \n', var_str==var_str2)

#5
print("Завдання 5: \n")

x= int(input('Введіть число'))
if x > 0:
    print('Число більше нуля')
if x < 0:
    print('Число менше нуля')

 #6
print('Завдання 6: \n')

if x > 0:
    print('1')
else:
     print('-1')

#7
print('Завдання 7: \n')

p= int(input('Введіть число'))
l= int(input('Введіть число'))

if p>l:
    res= p-l
elif p<l:
    res = p+l
else: 
    res = p

print(res)

#8
print('Завдання 8: \n')

n = int(input('Введіть ціле число n: '))

if n % 5 == 0:
    print('Число кратне 5')
else:
    print('Число не кратне 5')

#9
print('Завдання 9')
fib1 = 0
fib2 = 1
n = 20
i = 3
while i <= n:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    if i >= 5:
        print (fib_sum)
        i += 1

i = 0

while i <= 20:
    if i%2 == 0:
        print(i)
        i += 1

i = -1
while i >= -21:
    if i%3 == 0:
        print(i)
        i -= 1

#10
gram = 100
price = 10
upprice = 10

while gram <= 1000:    
        print(f'{gram} - грам, {price} - ціна')
        price +=upprice
        gram+= 100
