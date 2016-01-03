#this script is a temperature converter
#this script is a good candidate for a beginner gui application


#this defines the functions used in the script, use'm like legos!
def convert_f_to_c(x):
    f_converted = (x-32) * (5 / 9)
    return f_converted

def convert_c_to_f(y):
    c_converted = y * (9 / 5) + 32
    return c_converted

#starting point of the program
def start():
    cels_or_fahr = input("""Enter 'c' for celcius to fahrenheit or 'f' for fahrenheight to celcius:
> """)
    if cels_or_fahr == 'f':
        celsius_temp = input("""Input the temp in fahrenheit and press RETURN to see celsius value
: > """)

        celsius_temp = float(celsius_temp)

        celsius_temp = convert_f_to_c(celsius_temp)

        print(celsius_temp)


    elif cels_or_fahr == 'c':
        fahr_temp = input("""Input the temp in celsius and press RETURN to see fahrenheight value
: > """)

        fahr_temp = float(fahr_temp)

        fahr_temp = convert_c_to_f(fahr_temp)
        print(fahr_temp)

    else:
        print("Input not valid, please input 'c' or 'f' ('' not required)")
        start()

start()
