#python list is similar to array and array list
alist = [5,10,20,30,40,50]
alist.append(5)
alist.append(6)
alist.append(7)
print(alist)

#removal via pop / remove
alist.remove(5)
print(alist)
alist.pop(1) #pop default removes the last value from the list
print(alist)
alist.pop
print(alist)

empty = []

for val in alist:
    if (val >= 6 and val <= 30):
        empty.append(val)
print(empty)
empty.sort()
print(empty)

empty = [0] * 10
empty.append(10)
#when using index place it must be in bounds 

dog = "dog"
dogs = (dog + " ") * 3
print(dogs)

squares=[]
for i in range(1000):
    squares.append(i*i)
#print(squares)
#comprehension
squares_copy = [value for value in squares]
#print[squares_copy]
large_squares = [val for val in squares if val >= 10000]
#                   |_________________| |______________|
print(large_squares)

squares= [i*i for i in range(1000)]
print(squares)

# Set (no duplicate values) no guarantee of order /// List (No Duplicates)   ****HW 2 HELP
aset = {1,2,3}
print(aset)
dups = [1,2,2,3,3,4,4,700,700,1,5,5]
no_dups = set(dups)
print(no_dups)
no_dups = list(no_dups)
print(no_dups)

#Dicitionaries
fav_foods = {"kathleen" : "pizza", "abby" : "hamburger", 
             "caroline" : "chicken tenders", "dominic" : "sushi"}
caroline_ff = fav_foods["caroline"]
print(caroline_ff)

for key in fav_foods:
    print(key,"favorite food is", fav_foods[key])
for key, value in fav_foods.items():
    print(key, "favorite food is", value)

if "kim" in fav_foods:
    kim = fav_foods["kim"]
else: 
    fav_foods["kim"] = "cereal"


