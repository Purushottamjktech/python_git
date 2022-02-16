try:
    ab = [10,80,75,0,18,0]
    for i in ab:
        result = 10/i

except ZeroDivisionError:
    print("got some error")
else:
    print(result)
