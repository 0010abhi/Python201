#Assignment2
print "--- Python Edureka Assignment 2 ---"

# def exitTask(inputValue):
#     if inputValue == 'exit':
#         return True
#     else:
#         return False

# Task 1:
# Correct the program given below
def task1():
    print "\nPerforming Task : 1"
    print  "type exit to terminate task1"
    total = raw_input('What is the total amount for your online shopping? ')
    if total == 'exit':
        return

    country = raw_input('Shipping within the US or Canada? ')
    if country == 'exit':
        return

    if country == "US":
        if total <= "50":
            print "Shipping Costs $6.00"
        elif total <= "100":
            print "Shipping Costs $9.00"
        elif total <= "150":
            print "Shipping Costs $12.00"
        else:
            print "FREE"
    elif country == "Canada":
        if total <= "50":
            print "Shipping Costs $8.00"
        elif total <= "100":
            print "Shipping Costs $12.00"
        elif total <= "150":
            print "Shipping Costs $15.00"
        else:
            print "FREE"
    else:
        print "Sorry, Country provided don't match with given choices."
        task1()

# Task 2:
# Write a program that uses raw_input to prompt a user for their name and then welcomes them
def task2():
    print "\nPerforming Task : 2"
    print  "type exit to terminate task2"
    username = raw_input('Who are you? ')
    if username == 'exit':
        return
    print "Welcome ", username

# Task 3:
# Write a program which prompts the user for a Fahrenheit temperature, convert the temperature to Celsius and print out the converted temperature.
def task3():
    print "\nPerforming Task : 3 (Fahrenheit temperature to Celsius)"
    print  "type exit to terminate task3"
    fahrenheit_temp = raw_input('Enter temperature(in Fahrenheit): ')
    if fahrenheit_temp == 'exit':
        return

    celsius_temp = (float(fahrenheit_temp) - 32) * 5/9
    print "temperature in Celsius: ",celsius_temp

# Task 4():
#Write a program to prompt the user for hours and rate per hour to compute gross pay.
def task4():
    print "\nPerforming Task : 4"
    print  "type exit to terminate task4"
    rate = 20;
    print "Rate: 20$/hr."
    hours = raw_input('Enter hours logged in for the day:')
    if hours == 'exit':
        return

    print "Pay for the day (in $): ",rate * int(hours)

task5List = [4,7,3,2,5,9]
# Task 5:
# Write a for loop that prints all elements of a list and their position in the list. 
def task5():
    print "\nPerforming Task : 5 (Iterating List ", task5List, ")"
    for item in task5List:
        print "Item ", item, "Found @ Position: ", task5List.index(item)
        # print "Item %d Found @ Position: %d"%item,task5List.index(item)

# Task 6:
# Write a program which should create a dictionary of key:values.
# 'A':1 'B':2 'C':3 . . . . 'Z':26 [Use dictionary comprehension]
def task6():
    print "\nPerforming Task : 6 (Ascii Codes: 65 to 90 For A-Z and 97 to 122 for a-z)"
    startValue = 65
    endValue = 90
    asciiNumberList = range(startValue,endValue+1) 
    task6Dict = {}
    # range(inclusive,exclusive)
    for value in asciiNumberList:
        task6Dict[chr(value)] = asciiNumberList.index(value)

    print "Alphabets Dictionary:"
    print str(task6Dict)    

task7Dict = { 'a': 1, 'b':2 }
# Task 7:
# Write a program to reverse/inverse key:value like below.
# dict1 = { 'a': 1, 'b':2 } Expected result : dict2 = { 1: 'a', 2: 'b' }
def task7():
    task7DictReverse = dict()
    print "\nPerforming Task : 7"
    for item in task7Dict.iteritems():
        task7DictReverse[item[1]] = item[0]
    
    print "Dictionary ", task7Dict, "converted to: ", task7DictReverse

task8List = ['a', 'b', 'c', 'd']
# Task 8:
# Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values.
# Expected result {'a': 1, 'c': 3, 'b': 2, 'd': 4} [Hint: Use Enumerate function]
def task8():
    print "\nPerforming Task : 8"
    task8Dict = dict()
    for item in enumerate(task8List):
        task8Dict[item[1]] = int(item[0]) + 1

    print "List ", task8List, "converted to Dictionary: ", task8Dict

task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()