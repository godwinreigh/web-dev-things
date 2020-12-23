#BMI calculator
name1 = 'YK'
height_ml = 2
weight_kgl = 90

name2 = "YK's sister"
height_ml2 = 1.8
weight_kgl2 = 70

name3 = "YK's brother"
height_ml3 = 2.5
weight_kgl3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + ' is not overweight'
    else:
        return name + ' is overweight'
result1 = bmi_calculator(name1, height_ml, weight_kgl)
result2 = bmi_calculator(name2, height_ml2, weight_kgl2)
result3 = bmi_calculator(name3, height_ml3, weight_kgl3)
print(result1)
print(result2)
print(result3)