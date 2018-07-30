student = {
    "name" : 'vinit',
    "id" : "843",
    "feedback" : None
}

student["last_name"] = "sai"

try:
    3 + "hi"
    last_name = student["last_name"]
except KeyError:
    print("Error finding")
except TypeError as error:
    print("Handling this dmb mistake")
    print(error)


print("This one works")