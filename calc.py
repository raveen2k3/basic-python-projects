a = int(input("first number: "))
#numbers for operation
b = int(input("second number: "))


def add(a ,b):
    print( a+b)
#function to add

def sub(a ,b):
    print( a-b)
#function to subtract
def div(a ,b):
   print( a//b)
#function to divide
def multi(a ,b):
    print(a *b)
#function to multiply

print("""
      SELCT ANY ONE 
      1. ADD
      2.SUB
      3.DIV
      4.Multi""")
#to choose which function you need

option = int(input("your option : "))
#choose option to get answered
if option == 1:
    add(a ,b)
if option == 2:
    sub(a ,b)
if option == 3:
    div(a ,b)
if option == 4:
    multi(a ,b)
