# n = 1000
# print(n)

# Python also allows chained assignment, which makes it possible to assign the same value to several variables simultaneously:
# a = b = c = 200
# print(a, b, c)

#The chained assignment above assigns 300 to the variables a, b, and c simultaneously.

# Variables in Python are not subject to this restriction. In Python, a variable may be assigned a value of one type and then later re-assigned a value of a different type:
# var = 23.5
# print (var)

# var = "Now I'm a string"
# print (var)

# print(type(300))


# Python names: 
# Officially, variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_). An additional restriction is that, although a variable name can contain digits, the first character of a variable name cannot be a digit.
name = "Bob"
Age = 54
has_W2 = True
print(name, Age, has_W2)


    # Camel Case: Second and subsequent words are capitalized, to make word boundaries easier to see. (Presumably, it struck someone at some point that the capital letters strewn throughout the variable name vaguely resemble camel humps.)
    #     Example: numberOfCollegeGraduates
    # Pascal Case: Identical to Camel Case, except the first word is also capitalized.
    #     Example: NumberOfCollegeGraduates
    # Snake Case: Words are separated by underscores.
    #     Example: number_of_college_graduates
