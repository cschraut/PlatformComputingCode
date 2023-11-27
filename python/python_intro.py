print("Hello world")

#this is a comment

'''

This is another type of comment (longer docstring)
This is another line
'''

#variables
sum = 10
place_first = "me"
# 1st_place = "me" ---- no numbers first
# cash$ = 100  ---- no non numbers/ letters
x = 10
print(x)
y = 11.5
x = "This is a string"
print(x)

# math operators all the same as java
x = 100
y = 10
result = x/y
print(result)
result = x//y
# result = int (x/y)
# // is floor division and removes float
print(result)

# built in functions --> link in python intro or look at python documentation
min_val = min(10,2)
print(min_val)
raised = pow(2,4)
raised_2 = 2**4
print(raised)
print(raised_2)

#if statements need colon to indictate what you want executed
x= -1
#if(x < 0){ }
if x < 0:
    print("x is negative")
    x += 1

print("this exectues outside of the if loop")

if x < 0:
    x += 1
elif x > 0:
    x -= 1
else:
    x = 10

count = 0
while count < 10:
    count+=1
    print(count)

alist = [1,2,3,4,5]
for value in alist:
        print(value)
'''for dog in alist:
    print(dog)'''

for i in range(len(alist)):
     print("i is", i , "and value at is in", alist[i])

for i in range(0, len(alist)-1, 1): 
     # 1st parameter for starting num,  2nd parameter is for where to end, 3rd parameter for what to increment by
     #0 default for 1st, 1 default for 3rd
     print("i is", i , "and value at is in", alist[i])

for i, val, in enumerate(alist):
     print(i, val)
     #enumerate

#functions
def say_hello(name = "friend"):
    print("hello", name)

def add_numbers(x,y):
     return x+y

say_hello("Bob")
say_hello()
result = add_numbers(2, 4)
print(result)

#Strings
fname = "Corey"
lname = "Schrauth"
full_name = fname + " " + lname
print(full_name)

first_intitial = fname[0]
last_char = full_name[-1]
print(last_char)

#Slice --> need to give start and end place that you want to slice (break up list) ******end place not included****
course = "Platform Computing"
platform = course[0:8]
computing = course[9:18] #still need colon but default for start is 0 and end is last index + 1
print(platform)
print(computing)




