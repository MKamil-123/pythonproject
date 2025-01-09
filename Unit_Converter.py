from operator import truediv

from utils import HeightInCm, HeightInFoot, WeightInKg, WeightInLbs

def Height_Conversion():
    unit_choice = (input("What unit do you want to convert from: ")).strip().lower()
    try:
        if unit_choice == "cms":
            Height = float(input("What is your height in centimetres: ").strip())
            print(f"Your height in feet is: {HeightInFoot(Height):.2f}")
        elif unit_choice == "feet":
            height = float(input("What is your height in feet: ").strip())
            print(f"Height in cms: {HeightInCm(height):.2f}")
        else:
            print("Unsupported unit choice.")
    except ValueError:
        print("Invalid input.")







