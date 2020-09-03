import math

def calculate_quadratic(coeff_1, coeff_2, coeff_3):
    #The formula to calculate the quadratic equation for the positive result given by the square
    #root is found below, the inputted into the appropriate variable.
    positive_root=(-coeff_2+math.sqrt((coeff_2**2)-(4*(coeff_1*coeff_3))))/(2*coeff_1)

    #The formula to calculate the negative root of the quadratic is used to find the second input variable.
    negative_root=(-coeff_2-math.sqrt((coeff_2**2)-(4*(coeff_1*coeff_3))))/(2*coeff_1)
    return f"The positive root is {positive_root} and the negative root is {negative_root}"

#User is prompted to enter three coefficients that will be used in calculating the roots, using
#the quadratic equation.
print("INPUT OF 3 NUMBER (trinomial) MUST NOT PRODUCE MAKE NEG SQUARE ROOT OR 0 DENOMINATOR")
print("EXAMPLES OF VALID TRINOMIALS TO USE: 2, -9, and 10; 9, 12, and 4; and 2, 7, and -4")
coefficient_1=int(input("Enter the first coefficient. "))
coefficient_2=int(input("Enter the second coefficient. "))
coefficient_3=int(input("Enter the third coefficient. "))

#Calls the function to calculate the roots.
print(calculate_quadratic(coefficient_1,coefficient_2,coefficient_3))
