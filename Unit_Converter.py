from operator import truediv

from utils import HeightInCm, HeightInFoot, WeightInKg, WeightInLbs

def height_conversion():
    unit_choice = (input("What unit do you want to convert from: ")).strip().lower()
    try:
        if unit_choice == "cms" or unit_choice == "cm":
            height = float(input("What is your height in centimetres: ").strip())
            print(f"Your height in feet is: {HeightInFoot(height):.2f} ft")
        elif unit_choice == "feet" or unit_choice == "feets":
            height = float(input("What is your height in feet: ").strip())
            print(f"Height in cms: {HeightInCm(height):.2f} cm")
        else:
            print("Unsupported unit choice.")
    except ValueError:
        print("Invalid input.")


def weight_conversion():
    unit_choice = input("What unit do you want to convert from: ").strip().lower()
    try:
        if unit_choice == "lbs" or unit_choice == "lb":
            weight = float(input("What is your weight in lbs: ").strip())
            print(f"Your weight in kgs is: {WeightInKg(weight):.2f} kgs")
        elif unit_choice == "kgs" or unit_choice == "kg":
            weight = float(input("What is your weight in kg: ").strip())
            print(f"Your weight in lbs is: {WeightInLbs(weight):.2f} lbs")
        else:
            print("Unsupported unit choice.")
    except ValueError:
        print("Invalid input.")


def main():
    while True:
        choice = input("Would you like to convert your weight or your height (You can type exit to quit): ").strip().lower()
        if choice == "height":
            height_conversion()
        elif choice == "weight":
            weight_conversion()
        elif choice == "exit":
            break


if __name__ == "__main__":
    main()







