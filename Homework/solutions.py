## Question 1

keys = ['Ten', 'Twenty', 'Thirty', 'Forty']
values = [10, 20, 30, 40]
my_dictionary = dict(zip(keys, values))
#print(my_dictionary)


## Question 2 
dict1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
dict2 = {'Thirty':30, 'Fourty':40, 'Fifty':50}
#(Option 1) # Advanced feature
dict3 = dict1 | dict2
#print(dict3)

# (Option 2)
dict3 = dict1.copy()
dict3.update(dict2)
#print(dict3)


## Question 3
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listThree = []
oddElements = listOne[1::2] # odd index
evenElements = listTwo[::2]
#print('odd elements: ' + str(oddElements))
#print('even elements: ' + str(evenElements))
listThree.extend(oddElements)
listThree.extend(evenElements)
#print(listThree)


## Question 4
val_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count = {}
for number in val_list:
    #print(number)
    if (number in count):
        #print('the number is in the dictionary already')
        count[number] += 1 # update the value using the key(in this case: number)
    else:
        #print('This number is not in the dictionary. so we add')
        count[number] = 1 # Create the key-value in the dictionary


## Question 5
aList = [1, 2, 3, 4, 5, 6, 7]
aList = [x * x for x in aList] # creates the for-loop in the list directly
#print(aList)


## Question 6
## TODO: Try trnaslation table
'''
delimeter = " "
f = delimeter.join(nulist)
str1 = "a"
str2 = "1"
str3 = ""
tab = f.maketrans(str1, str2, str3)
f.translate(tab)
'''
## TODO: Check the other options for filter function
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = list(filter(None, list1))
#print(new_list)


## Question 7
def calculate(number):
    print(number)
    return number + calculate(number - 1) if number else 0

result = calculate(100)
print('total result: ', result)