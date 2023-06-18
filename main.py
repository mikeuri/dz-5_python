import ServiceFunctions


if __name__ == '__main__':

    valArray = []
    for i in range(1, 5):
        valueName = f"value {i}"
        val = ServiceFunctions.getConsoleValue(valueName)
        valArray.append(int(val))

    sum1 = valArray[0] + valArray[1]
    sum2 = valArray[2] + valArray[3]

    print("------------------------------------------")
    print(f"sum1 is: {sum1}")
    print(f"sum2 is: {sum2}")

    # Comparing sums
    if sum1 < sum2:
        print(f"True: ({sum1} < {sum2})")
    else:
        print(f"False: ({sum1} >= {sum2})")

    print("------------------------------------------")

    # Incrementing and decrementing sums
    sum1 += 1
    print(f"Incremented sum1 is: {sum1}")
    sum2 -= 2
    print(f"Double decremented sum2 is: {sum2}")

    # Comparing sums after processing
    if sum1 > sum2:
        print(f"True: ({sum1} > {sum2})")
    else:
        print(f"False: ({sum1} <= {sum2})")

    print("------------------------------------------")

    # Getting modulus values
    modSum1 = sum1 % 2
    modSum2 = sum2 % 2

    print(f"modulus value for Sum1 = {sum1} is: {modSum1}")
    print(f"modulus value for Sum2 = {sum2} is: {modSum2}")

    if modSum1 == 0 or modSum2 == 0:
        print("True: either sum1 or sum2 is even number")
    else:
        print("False: none of the values is an even number")
