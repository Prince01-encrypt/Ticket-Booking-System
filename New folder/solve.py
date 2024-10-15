# Program to convert kilometers to miles
def km_to_miles():
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.6214
    print(f"{kilometers} kilometers is equal to {miles} miles.")

km_to_miles()