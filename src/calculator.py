a = float(input("Insert first number: "))
x = input("Insert operation: ")
b = float(input("Insert second number: "))

def sum(a, b):
	return a + b

def mult(a, b):
	return a*b

def div(a, b):
	return a/b

def sub(a, b):
	return a-b 
    

if(x == '+'):
    print(sum(a, b))
elif(x == '-'):
    print(sub(a, b))
elif(x == '*'):
	print(mult(a, b))
elif(x == '/'):
    print(div(a, b))
	
	