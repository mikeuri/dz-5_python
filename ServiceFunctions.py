def getConsoleValue(valName):
    isNotInt = True
    intVal = 0

    while isNotInt:
        val = input(f"Enter {valName}: ")
        try:
            intVal = int(val)
            isNotInt = False
        except ValueError:
            print ("The value should be integer")

    return intVal
