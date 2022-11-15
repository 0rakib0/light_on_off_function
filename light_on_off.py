light_on = False

while True:
    check = input("Your command please...").lower()

    if check == "on":
        if light_on:
            print("Light is already in on mode")
        else:
            light_on = True
            print("Light in on mode")
    elif check == "off":
        if not light_on:
            print("light Already in off mode")
        else:
            light_on = False
            print("Light in off mode")

    elif check == "sleep":
        print("Light go on sleep mode..")
        break
    elif check == "help":
        print("""1. On- light go in on mode
2. Off- light go in off mode
3. sleep- light go in sleep mode""")
    else:
        print("Invalid command. valid command please--------")

