
# TempConvOO.py

"""Convert temperature to Celcius or Fahreinheit

    Attributes:
        temp: integer/floating value of input temperature
        unit: string of the temperature unit
"""

class Convert(object):
    
    def __init__(self,temp,unit):
        
        self.temp = float(temp)
        self.unit = unit
    
    # Celcius to Fahreinheit
    def toFahreinheit(self):
        
        if self.unit == 'Fahreinheit':
            print "%.1f F" % self.temp
        else:
            print "%.1f F" % ((self.temp*9/5)+32)

    # Fahreinheit to Celcius
    def toCelcius(self):
        
        if self.unit == 'Celcius':
            print "%.1f C" % self.temp
        else:
            print "%.1f C" % ((self.temp-32)*5/9)