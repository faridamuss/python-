# "Double quotes" and 'single quotes' are both fine to wrap a string in. But beware! You have to be careful about when you use single quotes and when you use doubles. What if our strings also contain those characters? When type of error happens, you’ll get a hint from our text editor. 
# print('Let's get down to business!')
# print("Let's get down to business!")

# print('I said, "we should go" and we left.')
# print("I said, "we should go" and we left.")

# print("She asked, "Can't we just leave?" If only it was that simple.")
# print('She asked, "Can't we just leave?" If only it was that simple.')

# As we'll find is often the case, those intrepid programmers before us have given us a solution: In this case, it is called the escape character. Enter the mighty backslash \.

# with double quotes 
print("She asked, \"Can't we just leave?\" If only it was that simple.") 

# with single quotes
print('She asked, "Can\'t we just leave?" If only it was that simple.')

