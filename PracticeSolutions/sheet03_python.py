### Question 1: 
'''Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.'''

### Question 2: 
'''From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.'''

### Question 3: 
'''Using range(1,101), make a list containing only prime numbers.'''

### Question 4: 
'''Write a function to calculate area and circumference of a circle.'''

### Question 5: 
'''Write a function that takes the users age as input and then if the user is 18 and above it tell the user they can vote else it tells them in how many years more before they can vote. '''

### ## Question 6 (Very Easy) - 10 minutes
'''Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far. A win receives 3 points, a draw 1 point and a loss 0 points.

def score_calculator(wins, draws, losses):
    total_points = (wins * 3) + (draws) 
    return total_points

total_points = score_calculator(3, 4, 9)
print('Total points for the team= ', total_points)
'''

## Question 7 (Very Easy) - 10 minutes
'''
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
''' 

## Question 8 (Very Easy) - 5 minutes
''' Write a function such that: Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.
'''

## Question 9 (Medium) - 15 minutes
'''You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in euros), sell price per unit (in euros), and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold. '''

'''
def profit(info):
    [cost_price, selling_price, inventory] = info.values()
    return round((selling_price - cost_price) * inventory)

def profit_2(info):
    inventory = info['inventory']
    cost_price = info['cost_price']
    selling_price = info['selling_price']
    total_profit = round((selling_price - cost_price) * inventory)
    return total_profit

total_profit = profit(dict_items)
total_profit_2 = profit_2(dict_items)
print(total_profit)
print(total_profit_2)
'''


## Question 10 (Medium) - 10 minutes
'''Create a function that checks if the given arguments are of the same type. Return True if thay are and False if they are not'''