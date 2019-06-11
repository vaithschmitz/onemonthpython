# function to automatically get tip
def get_tip():
    # get input as int
    amount = float(input("What's your amount?").replace('$', ''))
    # query satisfaction as int
    satisfaction = int(input("On a scale of 1 to 3, how good was the service?"))

    # calc tip based on satisfaction
    if (satisfaction == 1):
        tip = (amount * 0.15)
    elif (satisfaction == 2):
        tip = (amount * 0.18)
    elif (satisfaction == 3):
        tip = (amount * 0.20)
    else: 
        exit()

    # round to 2 decimals
    print("Your should tip: ${:.2f}".format(tip))

# run function
get_tip()