try:
    try:
        one = int(input("Enter the first Number: "))
        two = int(input("Enter the second Numer: "))
    except:
        print("Enter valid integer numbers")
        quit()
    print(one/two)
    print("Closing Program")
except Exception as c:
    print("Computation Failed. Error:")
    print(c)
