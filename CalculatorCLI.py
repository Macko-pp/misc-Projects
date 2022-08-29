# Imports-----------------------------------------------------------------------

import math
import fire

# Error-------------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', ':', ',', ';', '<', '>', '~', '!', '@', '#', '$', '%', '^', '&', '*', '|', '+', '=', '[', ']', '{', '}', '`', '?', '-', '…']

# Function----------------------------------------------------------------------

Error = '''
--------------------------------------------------

    Please input a valid number or command.

--------------------------------------------------
'''

Thanks = '''
--------------------------------------------------

    Thanks for using the python calculator!

--------------------------------------------------
'''

Separator = '''
--------------------------------------------------

        '''

Separator2 = '''
--------------------------------------------------
        '''


def calculator(var1, modifier, var2=None):
    '''
A way to do simple math.

This function takes in two variables and one modifier to performs a calculation or conversion. (It also has costom error messages!)
Use the vars as the numbers to be modified, write the modifier as one of the following:
    
    + = Addition
    x = Multiplication
    - = Subtraction
    ÷ (U+00F7) = Division
    ^ = Exponent
    % (U+0025) = Percentage
    △ (U+25B3) = Triangle Area
    ◬ (U+25EC) = Triangular Prism Volume
    ❑ (U+2751) = Rectangular Prism Volume
    Mi-Km = Miles to Kilometers
    Km-Mi = Kilometers to Miles
    Ft-M = Feet to Meters
    M-Ft = Meters to Feet
    Cm-In = Centimeters to Inches
    In-Cm = Inches to Centimeters
    F-C = Farenheit to Celsius
    C-F = Celsius to Farenheit
        '''

    var1 = str(var1)
    var2 = str(var2)

    output = any([substring in var1 for substring in letters])

    if var1.isnumeric():
        var1 = int(var1)

    elif output:
        return Error

    elif "." in var1:
        var1 = float(var1)

    # Addition------------------------------------------------------------------

    if modifier == "+":

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = var1 + var2
        return '''{} {} {} {} = {} 
        {}'''.format(Separator, var1, modifier, var2, solution, Separator2)

    # Multiplication------------------------------------------------------------

    elif modifier == 'x':

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = var1 * var2
        return '''{} {} {} {} = {} 
        {}'''.format(Separator, var1, modifier, var2, solution, Separator2)

    # Subtraction---------------------------------------------------------------

    elif modifier == '-':

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = var1 - var2
        return '''{} {} {} {} = {} 
        {}'''.format(Separator, var1, modifier, var2, solution, Separator2)

    # Division------------------------------------------------------------------

    elif modifier == '÷' or modifier == '/':

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = var1 / var2
        return '''{} {} ÷ {} = {} 
        {}'''.format(Separator, var1, var2, solution, Separator2)

    # Exponent------------------------------------------------------------------

    elif modifier == "^":

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = var1 ** var2
        return '''{} {} {} {} = {} 
        {}'''.format(Separator, var1, modifier, var2, solution, Separator2)

    # Percentage----------------------------------------------------------------

    elif modifier == '%':

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = (var1 / var2) * 100
        return '''{} {} {} {} = {}% 
        {}'''.format(Separator, var1, modifier, var2, solution, Separator2)

    # Sqr-Root------------------------------------------------------------------

    elif modifier == '√':
        solution = math.sqrt(var1)
        return '''{} √ {} {} 
        {}'''.format(Separator, var1, solution, Separator2)

    # Triangle-Area-------------------------------------------------------------

    elif modifier == "△":

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        solution = (var1 * var2) / 2
        return '''{} The Area of △ is {}x² 
        {}'''.format(Separator, solution, Separator2)

    # Triangle-Volume-----------------------------------------------------------

    elif modifier == '◬':

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        var3 = input("Var 3: ")

        output = any([substring in var3 for substring in letters])

        if var3.isnumeric():
            var3 = int(var3)

        elif output:
            return Error
            

        elif "." in var3:
            var3 = float(var3)

        solution = ((var1 * var2) / 2) * var3
        return '''{} The Volume of ◬ {}x³ 
        {}'''.format(Separator, solution, Separator2)

    # Cube-Volume---------------------------------------------------------------

    elif modifier == '❑':

        output = any([substring in var2 for substring in letters])

        if var2.isnumeric():
            var2 = int(var2)

        elif output:
            return Error
            

        elif "." in var2:
            var2 = float(var2)

        var3 = input('Var 3: ')

        output = any([substring in var3 for substring in letters])

        if var3.isnumeric():
            var3 = int(var3)

        elif output:
            return Error
            

        elif "." in var3:
            var3 = float(var3)

        solution = (var1 * var2) * var3
        return '''{} The Volume of ❑ is {}x³ 
        {}'''.format(Separator, solution, Separator2)

    # Mi-Km---------------------------------------------------------------------

    elif modifier == 'Mi-Km':
        solution = var1 * 1.609
        return '''{} {}mi in Kilometers is {}km 
        {}'''.format(Separator, var1, solution, Separator2)

    # Km-Mi---------------------------------------------------------------------

    elif modifier == 'Km-Mi':
        solution = var1 / 1.609
        return '''{} {}km in Miles is {}mi 
        {}'''.format(Separator, var1, solution, Separator2)

    # Ft-M----------------------------------------------------------------------

    elif modifier == 'Ft-M':
        solution = var1 / 3.281
        return '''{} {}ft in Meters is {}m 
        {}'''.format(Separator, var1, solution, Separator2)

    # M-Ft----------------------------------------------------------------------

    elif modifier == 'M-Ft':
        solution = var1 * 3.281
        return '''{} {}m in Feet is {}ft 
        {}'''.format(Separator, var1, solution, Separator2)

    # Cm-In---------------------------------------------------------------------

    elif modifier == 'Cm-In':
        solution = var1 / 2.54
        return '''{} {}cm in Inches is {}″ 
        {}'''.format(Separator, var1, solution, Separator2)

    # In-Cm---------------------------------------------------------------------

    elif modifier == 'In-Cm':
        solution = var1 * 2.54
        return '''{} {}″ in Centimeters is {} cm
       {}'''.format(Separator, var1, solution, Separator2)

    # F-C-----------------------------------------------------------------------

    elif modifier == "F-C":
        solution = (var1 - 32) * 5 / 9
        return '''{} {}°F in °C is {}°C 
        {}'''.format(Separator, var1, solution, Separator2)

    # C-F-----------------------------------------------------------------------

    elif modifier == "C-F":
        solution = (var1 * 9 / 5) + 32
        return '''{} {}°C in °F is {}°F 
        {}'''.format(Separator, var1, solution, Separator2)

    # Kg-Lb---------------------------------------------------------------------

    elif modifier == "Kg-Lb":
        solution = var1 * 0.45359237
        return '''{} {}kg in lb is {}lb
        {}'''.format(Separator, var1, solution, Separator2)

    # Lb-Kg---------------------------------------------------------------------

    elif modifier == "Lb-Kg":
        solution = var1 / 0.45359237
        return '''{} {}lb in kg is {}kg
        {}'''.format(Separator, var1, solution, Separator2)

    # Error---------------------------------------------------------------------

    else:
        return '''
--------------------------------------------------

That modifier is invalid, please try another one.
        
--------------------------------------------------
'''

if __name__ == '__main__':
    fire.Fire(calculator)
