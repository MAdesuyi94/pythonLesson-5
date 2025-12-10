def milesToKm(miles):
    if miles < 0:
        for i in range(1, 4):
            print("Miles can not be negative")
            miles = float(
                input(
                    "William, please tell me how many miles you want converted to kilometers: "
                )
            )
            if not miles < 0:
                break
        print("3 subsequent invalid attempts reached sir. Closing program.")

    else:
        kilometers = miles * 1.6
        print(
            f"William, {miles} miles is equal to {kilometers} kilometers! Isn't that amazing?"
        )


def FahToCel(fahrenheit):
    if fahrenheit > 1000:
        for i in range(1, 4):
            print("You can not enter a temperature over 1000 fahrenheit")
            fahrenheit = float(
                input(
                    "William, please tell me the temperature in Fahrenheit you want converted to celcius: "
                )
            )
            if fahrenheit <= 1000:
                break
        print("3 subsequent invalid attempts reached sir. Closing program.")
    else:
        celcius = (fahrenheit - 32) * 5.0 / 9.0
        print(
            f"William, {fahrenheit} degrees Fahrenheit is equal to {celcius} degrees Celcius! Isn't that amazing?"
        )


def GalToLit(gallons):
    if gallons < 0:
        for i in range(1, 4):
            print("Gallons can not be negative")
            gallons = float(
                input(
                    "William, please tell me how many gallons you want converted to liters: "
                )
            )
            if not gallons < 0:
                break
        print("3 subsequent invalid attempts reached sir. Closing program.")
    else:
        liters = gallons * 3.9
        print(
            f"William, {gallons} gallons is equal to {liters} liters! Isn't that amazing?"
        )


def PoundsToKg(pounds):
    if pounds < 0:
        for i in range(1, 4):
            print("Pounds can not be negative")
            pounds = float(
                input(
                    "William, please tell me how many pounds you want converted to kilograms: "
                )
            )
            if not pounds < 0:
                break
        print("3 subsequent invalid attempts reached sir. Closing program.")
    else:
        kilograms = pounds * 0.45
        print(
            f"William, {pounds} pounds is equal to {kilograms} kilograms! Isn't that amazing?"
        )


def InchesToCm(inches):
    if inches < 0:
        for i in range(1, 4):
            print("Inches can not be negative")
            inches = float(
                input(
                    "William, please tell me how many inches you want converted to centimeters: "
                )
            )
            if not inches < 0:
                break
        print("3 subsequent invalid attempts reached sir. Closing program.")
    else:
        centimeters = inches * 2.54
        print(
            f"William, {inches} inches is equal to {centimeters} centimeters! Isn't that amazing?"
        )


def main():
    miles = float(
        input(
            "William, please tell me how many miles you want converted to kilometers: "
        )
    )
    milesToKm(miles)

    fahrenheit = float(
        input(
            "William, please tell me the temperature in Fahrenheit you want converted to celcius: "
        )
    )
    FahToCel(fahrenheit)

    gallons = float(
        input("William, please tell me how many gallons you want converted to liters: ")
    )
    GalToLit(gallons)

    pounds = float(
        input(
            "William, please tell me how many pounds you want converted to kilograms: "
        )
    )
    PoundsToKg(pounds)

    inches = float(
        input(
            "William, please tell me how many inches you want converted to centimeters: "
        )
    )
    InchesToCm(inches)
