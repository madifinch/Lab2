x = 10.5 
print (type(x))

x = int(x)
print (type(x))
print (x)

# int() converts it into an interger 
# str() converts it into a string 
# float() converts it into a float (decimal)

w = "look i will become the best python programmer!"
y = 10
z = 5.5


print ("the data type of w is ", (type(w)))
print ("the data type of y is ", (type(y)))
print ("the data type of z is ", (type(z)))

result = y + z
print ("result = ", result , " and the data type of result is", (type(result)))

result_1 = y + int(z)
print ("result = ", result_1 , " and the data type of result is", (type(result)))

result_2 = z + float(y)
print ("result = ", result_2 , " and the data type of result is", (type(result)))

print ("the data type of str(z) is", (type(str(z))))

yay = w + str(y) + str(z)
print (f" result_3 is", yay)
print (type(yay))

yay2 = w + str(y)
print (yay2)