try:
    x = 5 *[5]
    y = list[4]
    print("End")
except IndexError:
    print("Index out of bound")
else:
    print("Nothing is wrong")
finally:
    print("Finally we are here")