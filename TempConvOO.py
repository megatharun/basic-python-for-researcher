
# TempConvOO.py

"""Convert temperature to Celcius or Fahreinheit

    Attributes:
        temp: integer/floating value of input temperature
"""

class Convert(object):
    
    def __init__(self,temp):
        
        self.temp = float(temp)
    
    # Celcius to Fahreinheit
    def toFahreinheit(self):
        print "%.1f F" % ((self.temp*9/5)+32)

    # Fahreinheit to Celcius
    def toCelcius(self):
        print "%.1f C" % ((self.temp-32)*5/9)