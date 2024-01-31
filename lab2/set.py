#exx1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")  #Yes, apple is a fruit!

#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  
print(fruits)   #{'orange', 'cherry', 'banana', 'apple'}

#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)   #{'cherry', 'mango', 'banana', 'orange', 'grapes', 'apple'}
#ex4

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)   #{'apple', 'cherry'}

#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)   #{'apple', 'cherry'}

