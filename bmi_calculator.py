# bmi_calculator.py

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("🧮 Welcome to the BMI Calculator")

    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in centimeters (cm): "))

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError:
        print("❌ Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
