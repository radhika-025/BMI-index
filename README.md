# 🧮 BMI Calculator (Imperial & Metric)

A simple command-line *BMI (Body Mass Index)* calculator built with Python.  
It allows users to choose between *Metric* (kg/cm) and *Imperial* (lb/inch) units and provides personalized health feedback.

---

## 📋 Features

- Choose between *Metric* or *Imperial* units
- Calculates *BMI*
- Provides *health classification* and *risk levels*
- Offers *suggestions* for weight adjustment
- Prompts user to calculate again after each run
- Handles invalid inputs gracefully

---

## 🛠 How It Works

### 1. **Main Program (main.py)**
- Presents a menu to choose Metric or Imperial
- Calls the appropriate BMI calculation function from:
  - metric.py
  - imperial.py

### 2. *Metric Mode*
- Input: weight in *kilograms, height in **centimeters*
- Output:
  - BMI Value
  - Weight Category (Underweight, Normal, Overweight, Obese)
  - Health Risk
  - Advice to gain/lose weight if outside normal range

### 3. *Imperial Mode*
- Input: weight in *pounds, height in **inches*
- Output is the same as Metric

---

## 🧪 Example Usage

```bash
$ python main.py

==========BMI CALCULATOR==========

Welcome to the BMI calculator! To start, enter your preferred unit system below.

1. For Metric system, type Metric or just type M!
2. For Imperial system, type Imperial or just type I!


Preferred unit system: m
Enter your weight in kilograms (kg): 65
Enter your height in centimeters (cm): 170

Your BMI is: 22.49
Classification: Normal weight
Health Risk: Average

You're within the healthy weight range. Keep maintaining it!

Would you like to calculate again?
Type 'yes' to continue or 'no' to exit: no
Thank you! Stay healthy.

file structure
bmi_calculator/
│
├── main.py           # Main entry point
├── metric.py         # BMI logic for Metric units
├── imperial.py       # BMI logic for Imperial units
└── README.md         # This file
