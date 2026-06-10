def convert_c_to_f(temp_in_celcius):
    temp_in_farenheit = temp_in_celcius * 1.8 + 32
    return temp_in_farenheit

temp_in_f = convert_c_to_f(-40)
print(temp_in_f)