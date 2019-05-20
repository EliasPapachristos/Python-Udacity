"""
Factorials with While Loops
"""
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current

    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

"""
Factorials with For Loops
"""
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for n in range(2, number + 1):
    product *= n

# print the factorial of number
print(product)

"""
Count By
"""
start_num = 5  # provide some start number
end_num = 10  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

"""
Count By Check
"""
start_num = 5  # provide some start number
end_num = 10  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num

print(result)

"""
Nearest Square
"""
limit = 40
num = 0
# write your while loop here
while (num + 1) ** 2 < limit:
    num += 1
    nearest_square = num ** 2

print(nearest_square)

"""
Break the String
"""
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

"""
Chuck for Prime Numbers
"""
# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# write your code here
# HINT: You can use the modulo operator to find a factor

for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print('{} is not a prime number'.format(num))
            break
        if i == -1:
            print(('{} is a factor of {}'.format(num, i)))


