"""mystring = "Brian"
myint = 20
myfloat = 10.0
if mystring == "Brian":
    print("String is: ", mystring)
if isinstance(myfloat, float) and myint == 20:
    print("My int is: ", myint )
if isinstance(myfloat, float) and myfloat == 10.0:
    print("My float should be:", myfloat)"""

"""mylist = [1, 2, 3]
print(mylist[2])
mylist.append(4)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)"""
"""numbers= [1,2,3]
string= []
names = ['Mark', 'John', 'Zacheus']
ap

second_name = []

print(numbers)
print(string)
print("The second name in the list is ", names[1])"""

"""numbers = []
string = []
names = ['Zuckerberg', 'Elon', 'Bezoz']

numbers.append(1)
numbers.append(2)
numbers.append(3)

string.append(1)
string.append(2)

second_name = names [1]

print(numbers)
print(string)
print("The second name in the list is:", second_name)

mystring = []
myint = []

mystring.append(1)
mystring.append(2)


myint.append(1)

print(mystring)
print(myint)

hellos = "Hello" * 10
print(hellos)

Numbers = [1,2,3,4] * 3
print(Numbers)


x = ()
y = ()
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" %len(x_list))
print("y_list contains %d objects" %len(y_list))
print("big_list contains %d objects" %len(big_list))

if x_list.count(x) == 10 and y_list ==10:
    print("almost there...")
if big_list.count(x) == 10 and big_list ==10:
    print("Great")

names = "John Doe."
balance = 53.44
print("Hello",names + " Your balance is",balance)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your balance is $%s."
print(format_string % data)

string = "Hello There?"
print(string.index("o"))

string = "Hello There?"
print(string.count("e"))

string = ("Hello There?")
print(string[3:7:2])

string = "hello there"
print(string[::-1])
string = "hello there"
print(string.upper())
print(string.lower())

string = "Hello There"
print(string.startswith("Hello"))
print(string.endswith("Hello"))

string = "Hello There"
string.split("")
print(afewwords)

x = "Hey there! what should this string be?"
#length should be 20
print("Length of s= %d"% len(x))

#First occurence of "a" should be at index 8
print("The first occurence of letter a = %d" %s .index("a"))
y = 3
print(y == 2)
print(y != 3)
print(y < 1)

name = input("Enter the name: ")
age = input("Age is: ")

if len(name) == 6 and age < 22:
    print("QUALIFIED")
else:
    print("Null")
if len(name) == 7 or len(name) == 6:
    print("Approved")
else:
    print("No data")

greeting = "Hey"
if greeting in ["Hello", "Hey", "Hi"]:
    print("Name is available")
else:
    print("Not available")

#Loops
#for loop

students =("Peter","Morgan", "Brian", "Mary")
for student in students:
    print("********")
    print(student)
    for name in student:
        print(True)
        primes = [2, 3,5, 7]
        for prime in primes:
            print(prime)
for x in range(7):
    print(x)
for x in range(2, 8):
    print(x)
for x in range(3, 8, 2):
    print(x)

#while loop
count = 0
while count < 5:
    print(count)
    count += 1 #This is the same as count = count + 1
Quiz = 1
while Quiz <= 6:
    print(Quiz)
    Quiz +=1

#"Break" and "Continue" statement
quiz = 0
while True:
    print(quiz)
    quiz +=1
    if quiz >= 6:
        break
    
for y in range(10, 20):
    if y % 2 ==0:
        continue
    print(y)
#else
count = int(input("Enter the start of count: "))
while(count < 5):
    print(count)
    count +=1
else:
    print("Count value reached %d" %(count))

for i in range(1, 10):
    if (i%5 == 0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition")

for even in range(1, 237):
    if even % 2 == 0:
        print(even)
*********
#functions
************

def sum_numbers(a, b):
    return a + b
result = sum_numbers(4, 6)
print(result)

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish I You  %s" %(username, greeting))"""