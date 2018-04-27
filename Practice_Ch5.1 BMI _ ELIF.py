##Implement function myBMI() that takes as input
##a person’s height (in inches)and weight (in pounds)
##and computes the person’s Body Mass Index (BMI).
##The BMI formula is:

##bmi = weight ∗ 703 height2

##Your functions should print
##the string 'Underweight' if bmi < 18.5,
##'Normal' if 18.5 <= bmi < 25,
##and Overweight if bmi >= 25.
## (Perkovic 130)

def myBMI(height_inches,weight_lbs):

    bmi = (weight_lbs * 703)/(height_inches)**2

    if bmi < 18.5:
        print('Underweight')
    elif bmi >= 25:
        print('Overweight')
    elif bmi < 25:
        print('Normal')
    else:
        print('error')
