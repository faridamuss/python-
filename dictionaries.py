# A dictionary consists of a collection of key/value pairs. Each key-value pair maps the key to its associated value. You can define a dictionary by ecolosing a comma-separated list of key-value pairs in curly braces {}. A colon (:) separated list of key-value pairs:

# MLB_team = {
#    "Colorado": "Rockies",
#    "Boston": "Red Sox", 
#    "Minnesota": "Twins",
# }

# print(MLB_team['Minnesota']) # you can access a value in the dictionary by its key name

# You can also construct a dictionary with the built-in dict() function. The argument to dict() should be a sequence of key-value pairs. A list of tuples works as well for this: 

d = dict([
    ('Colorado', 'Rockies'), 
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins')
  ])
print(d)  
print(type(d)) #output <class 'dict'>
