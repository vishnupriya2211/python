# User input for weight, height, age, and gender
weight = int(input("Enter the weight in kg: "))
height = int(input("Enter the height in cm: "))
age = int(input("Enter the age: "))
gender = input("Enter gender (male/female): ").lower()

# Print input values
print(weight, height, age, gender)

# BMR calculation based on gender
if gender == "male":
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
elif gender == "female":
    BMR = 10 * weight + 6.25 * height - 5 * age + 161
else:
    print("*****Please enter a valid gender**********")
    BMR = None

# Print the calculated BMR if gender is valid
if BMR is not None:
    print("BMR:", BMR)

    # User input for activity level
    activity_level = int(input("""
    Select activity level:
        Press 1 for sedentary (little or no exercise)
        Press 2 for lightly active (light exercise/sports 1-3 days/week)
        Press 3 for moderately active (moderate exercise/sports 3-5 days/week)
        Press 4 for very active (hard exercise/sports 6-7 days a week)
        Press 5 for extra active (very hard exercise/physical job & exercise)
    """))

    # Calculate calories based on activity level
    if activity_level == 1:
        calories = BMR * 1.2
    elif activity_level == 2:
        calories = BMR * 1.375
    elif activity_level == 3:
        calories = BMR * 1.55
    elif activity_level == 4:
        calories = BMR * 1.725
    elif activity_level == 5:
        calories = BMR * 1.9
    else:
        print("Select a valid choice for activity level")
        calories = None

    # Print the total number of calories needed to maintain current weight
    if calories is not None:
        print(f"Total number of calories you need in order to maintain your current weight: {calories}")

        # User input for target weight and duration
        target_weight = int(input("Enter weight to reduce in kg: "))
        duration = int(input("Enter duration in weeks: "))

        # Calculate daily calorie deficit
        calories_deficit = target_weight * 7700  # 1 kg of weight loss equals 7700 calories deficit
        days = duration * 7
        daily_calories_deficit = calories_deficit / days

        print("Daily calories deficit:", daily_calories_deficit)
else:
    print("BMR calculation failed due to invalid gender input.")
