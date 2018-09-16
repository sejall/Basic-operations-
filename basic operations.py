# Python Program - Addition Subtraction Multiplication Division

print("Enter 'x' for exit.");
print("Enter any two number: ");
num1 = input();
num2 = input();
if num1 == 'x':
    exit();
else:
    ch = input("Enter operator (+,-,*,/): ");
    if ch == '+':
    	res = int(num1) + int(num2);
    	print(num1, "+", num2, "=", res);
    elif ch == '-':
    	res = int(num1) - int(num2);
    	print(num1, "-", num2, "=", res);
    elif ch == '*':
    	res = int(num1) * int(num2);
    	print(num1, "*", num2, "=", res);
    elif ch == '/':
    	res = int(num1) / int(num2);
    	print(num1, "/", num2, "=", res);
    else:
    	print("Strange input..exiting..");
