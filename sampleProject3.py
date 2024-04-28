def bmw():
    print("\nWelcome to BMW Cars, Please Check out the Car details ")

    price = 7500000
    mileage = 9
    madeIn = "Germany"

    print("Car Price : ",price, "\nMileage : ",mileage, "\nMade In : ",madeIn)

def hondaCity():
    print("\nWelcome to HondaCity Cars, Please Check out the Car details ")

    price = 1300000
    mileage = 22
    madeIn = "India"

    print("Car Price : ",price, "\nMileage : ",mileage, "\nMade In : ",madeIn)

def innova():
    print("\nWelcome to Innova Cars, Please Check out the Car details ")

    price = 2700000
    mileage = 20
    madeIn = "Japan"

    print("Car Price : ",price, "\nMileage : ",mileage, "\nMade In : ",madeIn)

def ertiga():
    print("\nWelcome to Ertiga Cars, Please Check out the Car details ")

    price = 1100000
    mileage = 25
    madeIn = "India"

    print("Car Price : ",price, "\nMileage : ",mileage, "\nMade In : ",madeIn)

def ferrari():
    print("\nWelcome to Ferrari Cars, Please Check out the Car details ")

    price = 9900000
    mileage = 7
    madeIn = "America"

    print("Car Price : ",price, "\nMileage : ",mileage, "\nMade In : ",madeIn)

def audi():
    print("\nWelcome to Audi Cars, Please Check out the Car details ")

    price = 5500000
    mileage = 12
    madeIn = "Russia"

    print("Car Price : ",price, "\nMileage : ",mileage, "\nMade In : ",madeIn)



print("Welcome to Car Showroom ")
print("\nBMW\nHondaCity\nInnova\nErtiga\nFerrari\nAudi")

car = input("\nPlease Select the Car and Check out the details\n")

if (car.lower() == "bmw"):
    bmw()

elif(car.lower() == "hondacity"):
    hondaCity()

elif(car.lower() == "innova"):
    innova()

elif(car.lower() == "ertiga"):
    ertiga()

elif(car.lower() == "ferrari"):
    ferrari()

elif(car.lower() == "audi"):
    audi()

else:
    print("Invalid Value ")



