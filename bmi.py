from imperial import *
from metric import *


def main():
    print("\n==========BMI CALCULATOR==========")
    print("\nWelcome to the BMI calculator! To start, enter your preferred unit system below.\n")
    print("1. For Metric system, type Metric or just type M!")
    print("2. For Imperial system, type Imperial or just type I!\n\n") 

    # Choice for measurements
    
    choice = ""
    while choice != "Exit":
        choice = str(input("Preferred unit system: "))
        choice_final = choice.upper()

        if choice_final in ("METRIC", "M"):
            bmi_metric()

        elif choice_final in ("IMPERIAL", "I"):
            bmi_imperial()

        else:
            print("Invalid input. Please try again.")

# Running the calculator

if __name__ == "__main__":
    main()
