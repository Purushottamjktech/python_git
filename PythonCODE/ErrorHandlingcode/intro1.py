def error():

    list = [10, 100, 0,78]
    var = 10
    for i in list:

        try:
            result = var / i

        except ZeroDivisionError:
            print("operation can't be performed")
        else:
            print(result)
        finally:
            print("program executed sucessfully")
