#Assignment1
print "--- Python Edureka Assignment 3 ---"
import random
import operator


instructionString = "Please, Enter right choice. or type exit to terminate\n"
# Task 1:Quiz Task
class Quiz:
    def __init__(self, qLevel, qType, qNums):
        self.qLevel = qLevel
        self.qType = qType
        self.qNums = qNums
        self.startQuiz(self.qLevel, self.qType, self.qNums)

    def setQuestionType(self, qType):
        if qType == 'M':
            return '*'
        elif qType == 'A':
            return '+'
        elif qType == 'S':
            return '-'
        elif qType == 'D':
            return '/'

    def setQuestionLevel(self, qType):
        maxNumber = 1
        if qType == 'E':
            maxNumber = 100
        elif qType == 'I':
            maxNumber = 1000
        elif qType == 'H':
            maxNumber = 10000

        return maxNumber
    
    def getAnswer(self, getOperatorString, firstOperand, secondOperand):
        if getOperatorString == '*':
            return operator.mul(firstOperand, secondOperand)
        elif getOperatorString == '+':
            return operator.add(firstOperand, secondOperand)
        elif getOperatorString == '-':
            return operator.sub(firstOperand, secondOperand)
        elif getOperatorString == '/':
            return operator.div(firstOperand, secondOperand)

    def makeQuestions(self, questionLevel, questionType, numberOfQue):
        getOperatorString = self.setQuestionType(questionType)
        getRangeOfNumber = self.setQuestionLevel(questionLevel)
        queList = list()
        for que in range(1,numberOfQue+1):
            firstOperand = random.randint(1, getRangeOfNumber)
            secondOperand = random.randint(1, getRangeOfNumber)
            newQue = "Question " + str(que) + ": " + str(firstOperand) + getOperatorString + str(secondOperand)
            newAns =  self.getAnswer(getOperatorString, firstOperand, secondOperand)
            queTup = (newQue,newAns)
            queList.append(queTup)
        return queList

    def startQuiz(self, questionLevel, questionType, numberOfQue):
        queList = self.makeQuestions(questionLevel, questionType, numberOfQue)
        for queNum in queList:
            print queNum[0]
            userAns = raw_input("Your input: ")
            if int(userAns) == queNum[1]:
                print "Gerat, Right Answer.\n"
            else:
                print "Oops, Wrong Answer.\n"

def task1():
    print "Performing Task : 1 (Maths Basic Quiz For Childrens 3 to 7 years)"
    questionLevel = raw_input("Choose level (easy:E, intermediate:I, and hard:H):")
    questionType = raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D):")
    numberOfQue = raw_input("Please give us the number of question you want to attempt: ")
    Quiz(questionLevel, questionType, int(numberOfQue))



def xToPowerN(x,n):
    if n==0:
        return 1
    elif n>0:
        n -= 1
        return x * xToPowerN(x,n) 
    else:
        print "-ve powers are not handled"
        return
# Task 2: x to power n using recursion
def task2():
    print "Performing Task : 2"
    number = raw_input("Enter the number: ")
    power = raw_input("Enter the power to raise: ")
    result = xToPowerN(int(number),int(power))
    print result

listToSort1 =  [["john", 1, "a"],["larry", 0, "b"]]
# Task 3: Sort list using lambda function for second element 1,0
def task3():
    print "Performing Task : 3 Sort list using lambda function for second element 1,0"
    listToSort1.sort(key=lambda elem: elem[1])
    print listToSort1

listToSort2 =  [["john", 1, "a"],["larry", 0, "b"]]
# Task 4: Sort the list using operator.itemgetter for second element 1,0
def task4():
    print "Performing Task : 4 Sort the list using operator.itemgetter for second element 1,0"
    # operator.itemgetter(1)(listToSort2)
    listToSort2.sort(key=operator.itemgetter(1))
    print listToSort2

task1()
task2()
task3()
task4()
