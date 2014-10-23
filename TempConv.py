
# TempConv.py

# Celcius to Fahreinheit

def Fahreinheit(temp):
    temp = float(temp)
    temp = (temp*9/5)+32
    return temp

# Fahreinheit to Celcius

def Celcius(temp):
    temp = float(temp)
    temp = (temp-32)*5/9
    return temp
    