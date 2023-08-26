#الجزء الاول

Flan = input("Enter your name :")
Number = input("Enter your age :")
print(f"My name is {Flan} and I am {Number} years old")

#الجزء الثاني

first_number = int(input("Number one : "))
second_number = int(input("Number two : "))
operation = input("Enter an operation")
if operation == "+" :
    print(first_number + second_number)
elif operation == "-" :
    print(first_number - second_number)
elif operation == "*" :
    print(first_number * second_number)
elif operation == "/" :
    print(first_number / second_number)

    #الجزء الثالث

bus_capacity = 10
people_outbus = int(input("Enter  people outbus : "))
people_inbus = int(input("Enter people inbus :"))
empty_seats = bus_capacity - people_inbus

if empty_seats > people_outbus :
    print(f"there are{empty_seats} empty seats")
elif empty_seats < people_outbus :
    print("the bus is full")

