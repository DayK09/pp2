#ex1

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))   #Mustang


#ex2

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020 

x = car.values()
print(x)    #dict_values(['Ford', 'Mustang', 2020])

#ex3

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
x = car.get("color")
print(x)    #red

#ex4

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)     #{'brand': 'Ford', 'year': 1964}

#ex5

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)   #{}



