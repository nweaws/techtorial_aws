## Every math operation between float and int date type
# will result in float data type

floatNum = 3.0
intNum   = 5

print("type of floatNum is ",type(floatNum))
print("type of intNum is",type(intNum))

addition = floatNum + intNum
print("Additon of float and int is",type(addition))

subtraction = intNum - floatNum
print("subtraction between int and float is",type(subtraction))

multipliction = floatNum * intNum
print("multipliction between float and int is ",type(multipliction))

divition = intNum / floatNum
print("the divition betweenfloat and int is ",type(divition))

remainder = floatNum % intNum
print("the remainder between float and int is ",type(remainder))

remainder2 = intNum % floatNum
print("the remainder between int and float type is ",type(remainder2))

int_divition = floatNum // intNum
print("the integer symbol division result between float and int is ",type(int_divition))

square_of_float = floatNum * floatNum
print(type(square_of_float))
