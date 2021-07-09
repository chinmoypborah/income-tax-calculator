print("Income Tax Calculator By Chinmoy Pratim Borah.")
userinput=input("For Between 60 years(a), Between 60 to 80 years(b), Above 80 Years(c) : ")
if userinput=='a':
    income=int(input("Enter Annual Income: "))
    if income<200000:
        tax=0
        print("You Don't Have To Pay TAX!")
    elif income<=500000:
        tax=0.05*(income-200000)
        print("You have to pay for Rs: ",tax)
    elif income<=100000:
        tax=200000+0.02*(income-500000)
        print("You have to pay for Rs: ",tax)
    else:
        tax=100000+0.30*(income-100000)
        print("You have to pay for Rs: ",tax)
if userinput=='b':
    income=int(input("Enter Annual Income: "))
    if income<=300000:
        tax=0
        print("You Don't Have To Pay TAX!")
    elif income<=500000:
        tax=0.50*(income-300000)
        print("You have to pay for Rs: ",tax)
    elif income<=100000:
        tax=100000+0.20*(income-500000)
        print("You have to pay for Rs: ",tax)
    else:
        tax=110000+0.30*(income-100000)
        print("You have to pay for Rs: ",tax)
if userinput=='c':
    income=int(input("Enter Annual Income: "))
    if income<=500000:
        tax=0
        print("You Don't Have To Pay TAX!")
    elif income<=100000:
        tax=0.20*(income-500000)
        print("You have to pay for Rs: ",tax)
    else:
        tax=100000+0.30*(income-100000)
        print("You have to pay for Rs: ",tax)
