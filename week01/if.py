x = int(input('Enter an integer'))
if x%2==0:
    print('even')
else:
    print('odd')

print(x)

#nested ifs
#whether the entered integer is divisible by both 2 and 3
x = int(input('Enter another integer'))
if x%2==0:
    if x%3==0:
        print('integer divisible by both 2 and 3')
    else:
        print('integer divisible by only 2')
elif x%3==0:
    print('integer divisible by only 3')
else:
    print('integer not divisible by 2 or 3')

