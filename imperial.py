def bmi_imperial():
    try:
        weight = float(input("Enter your weight in pounds (lb): "))
        height = float(input("Enter your height in inches: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = round((weight * 703) / (height ** 2), 2)
        print(f"\nYour BMI is: {bmi}")

        # BMI Classifications and health risks
        if bmi < 18.5:
            classification = "Underweight"
            risk = "Low"
        elif 18.5 <= bmi < 25:
            classification = "Normal weight"
            risk = "Average"
        elif 25 <= bmi < 30:
            classification = "Overweight"
            risk = "Mildly increased"
        elif 30 <= bmi < 35:
            classification = "Obese Class 1"
            risk = "Moderate"
        elif 35 <= bmi < 40:
            classification = "Obese Class 2"
            risk = "Severe"
        else:  # bmi >= 40
            classification = "Obese Class 3"
            risk = "Very Severe"

        print(f"Classification: {classification}")
        print(f"Health Risk: {risk}")

        # Calculate target maximum normal weight
        max_normal_bmi = 24.9
        normal_weight = round((max_normal_bmi * (height ** 2)) / 703, 2)
        weight_diff = round(weight - normal_weight, 2)

        # Provide weight adjustment suggestion
        print()
        if weight_diff > 10:
            print(f"You need to lose approximately {weight_diff} pounds to reach a normal BMI.")
        elif 0 < weight_diff <= 10:
            print("Your weight is slightly above the normal range. Try to maintain or slightly reduce it.")
        elif -10 <= weight_diff < 0:
            print("You're within the healthy range. Keep it up!")
        else:  # weight_diff < -10
            print(f"You need to gain approximately {abs(weight_diff)} pounds to reach a normal BMI.")

        # Ask user if they want to continue
        print("\nWould you like to calculate again?")
        choice = input("Type 'yes' to continue or 'no' to exit: ").strip().lower()

        if choice == 'yes':
            bmi_imperial()  # Recursively call again
        else:
            print("Thank you! Stay healthy.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
