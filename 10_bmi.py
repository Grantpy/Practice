print ("this will calculate your BMI")
kg = float(input("Enter our weight in kg:"))
mtr = float(input("Enter your hieght in m:"))
bmi = kg/(mtr*mtr)
print ("Your BMI is: ",(round(bmi)))

#if (bmi <= 18.5):
#    print("Your BMI is:", round(bmi,2), ". You are under weight.")
#
#elif (18.5 < bmi <= 24.9):
#    print("Your BMI is:", round(bmi,2), ". You are normal weight.")
#
#elif (24.9 < bmi <= 29.9):
#    print("Your BMI is:", round(bmi,2), ". You are over weight.")  
#
#else:
#    print("Your BMI is:", round(bmi,2), ". You are obese")     


if (bmi <= 18.5):
    classification = "underweight"
elif (18.5 < bmi <= 24.9):
    classification = "Normal weight"
elif (24.9 < bmi <= 29.9):
    classification = "Over weight"
else:
    classification = "Obesity"

print("The classification is :", (classification))
