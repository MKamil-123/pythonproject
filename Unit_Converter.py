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


def Weight_Conversion():
    unit_choice = input("What unit do you want to convert from: ").strip().lower()
    try:
        if unit_choice == "lbs":
            Weight = float(input("What is your weight in lbs: ").strip())
            print(f"Your weight in kgs is: {WeightInKg(Weight):.2f}")
        elif unit_choice == "kgs":
            Weight = float(input("What is your weight in kgs: ").strip())
            print(f"Your weight in lbs is: {WeightInLbs(Weight):.2f}")
        else:
            print("Unsupported unit choice.")
    except ValueError:
        print("Invalid input.")







