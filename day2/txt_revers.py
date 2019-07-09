rever = []

with open('number.txt','r') as file:
    numbers = file.readlines()
print(numbers)    

# lines.reverse()
with open('number_revers.txt', 'w') as file:
    for i in range(len(numbers)):
        file.write(numbers[len(numbers)-i-1])