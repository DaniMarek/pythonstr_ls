# Find and replace:
string="What time is it?? Python time."
print string.find("Python")
print string.replace("Python", "Blackbelt")

# Min and Max:
d=[10,13,5,-3,-7,5,100,89]
print (min(d), max(d))

# First and last
z=["holla",10,13,5,-3,-7,5,100,89,"at ya"]
print (z[0],z[-1])
# z[-1] counts the indices backwards starting at one and decreasing as one moves to the left ('holla'=z[-10])

# New list:
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
first_list = x[:len(x)/2] 
second_list = x[len(x)/2:] 
print "first list", first_list
print "second list", second_list
second_list.insert(0,first_list)
print "new list", second_list
