import requests
import pyautogui as pt
from time import sleep
import pyperclip

sleep(2)
apiUrl = "https://chatbot-mangata.herokuapp.com"
first_response = requests.get(apiUrl + "/chat1/all")
rentingout_response = requests.get(apiUrl + "/chat2/all/60ba04b395c1b91e4956bedc")
torent_response = requests.get(apiUrl + "/chat2/all/60ba0578527c721e83a0778a")
caretaker_response = requests.get(apiUrl + "/chat2/all/60ba0592527c721e83a0778b")
ensure_response = requests.get(apiUrl + "/chat2/all/60ba05ac527c721e83a0778c")
accommodation_response = requests.get(apiUrl + '/accommodation/all')

# houses responses
all_houses_response = requests.get(apiUrl + '/availablehouses/get/all')
low_density_houses = requests.get(apiUrl + '/availablehouses/lowdensity')
high_density_houses = requests.get(apiUrl + '/availablehouses/highdensity')
# house json responses
all_houses_json = all_houses_response.json()
low_density_json = low_density_houses.json()
high_density_json = high_density_houses.json()

# vehicle responses
all_vehicles = requests.get(apiUrl + '/availablevehicles/get/all')
private_vehicles = requests.get(apiUrl + '/availablevehicles/private')
heavy_vehicles = requests.get(apiUrl + '/availablevehicles/heavy')
# vehicle json responses
all_vehicle_json = all_vehicles.json()
private_json = private_vehicles.json()
heavy_json = heavy_vehicles.json()

# occasions responses
all_occasions = requests.get(apiUrl + '/occassions/get/all')
# occasions json
occasions_json = all_occasions.json()

# equipment responses
all_equipment = requests.get(apiUrl + '/availableequipment/whatsapp/all')
# equipment json
equipment_json = all_equipment.json()

# caretakers responses
all_maids = requests.get(apiUrl + '/availablecaretakers/whatsapp/maids/all')
all_garden_boy = requests.get(apiUrl + '/availablecaretakers/whatsapp/garden/all')
# caretakers json
maids_json = all_maids.json()
garden_boy_json = all_garden_boy.json()

first_json = first_response.json()
rentingout_json = rentingout_response.json()
torent_json = torent_response.json()
caretaker_json = caretaker_response.json()
ensure_json = ensure_response.json()
accommodation_json = accommodation_response.json()


# send first message from api backend formatter
def first_whatsapp_message():
    message_array = []
    index = 0
    for item in first_json:
        index += 1
        message_array.append("{index}: {option}".format(option=item['option'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# send second message from api backend formatter
def second_message(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("1.{index}: {option}".format(option=item['option'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# message or option 3
def option_3_message(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("3.{index}: {option}".format(option=item['option'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# send second message from api backend formatter
def second_one_message(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("2.{index}: {option}".format(option=item['option'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# send accommodation options from api backend
def accommodation_message(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("1.1.{index}: {option}".format(option=item['option'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# chat accommodation message
def chat3_accommodation_message(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("2.1.2.{index}: {option}".format(option=item['option'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# get all houses to sell
def get_houses(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("house{index}: {option}".format(option=item['details'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# get all vehicles to sell
def get_all_vehicles(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("vehicle{index}: {option}".format(option=item['details'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# get all vehicles to sell
def get_all_occasions(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("occasion{index}: {option}".format(option=item['details'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str

# get all equipment to sell
def get_all_equipment(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("equipment{index}: {option}".format(option=item['details'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# get all maids
def get_all_maids(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("maid{index}: {option}".format(option=item['details'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# get all garden boys
def get_all_garden(json):
    message_array = []
    index = 0
    for item in json:
        index += 1
        message_array.append("garden{index}: {option}".format(option=item['details'], index=index))

    list_to_str = '\n'.join([str(elem) for elem in message_array])
    return list_to_str


# initial position
position1 = pt.locateOnScreen('smiley_and_paperclip.png', confidence=.6)
x = position1[0]
y = position1[1]


# get the message and save responses
def get_message():
    global x, y
    position = pt.locateOnScreen("smiley_and_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.3)
    pt.moveTo(x + 110, y - 50, duration=.3)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, -195)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("selected message: " + whatsapp_message)

    return whatsapp_message


# # reply the message basing on the message received
def reply_message(message):
    global x, y
    position = pt.locateOnScreen("smiley_and_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 180, y + 30, duration=.3)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)


#
# # types of replies
# # responding based in backend answers
def process_response(message):
    if message.lower() == "hi" or message.lower() == "hie" or 'makadii' in message.lower() or 'looking' in message.lower() or 'hie' in message.lower() or 'morning' in message.lower() or 'afternoon' in message.lower() or 'kutsvaga' in message.lower() or 'hello' in message.lower() or 'kutsvaga' in message.lower():
        return "Thank you for contacting Rent out. The company dedicated to delivering the best possible " \
               "services. How " \
               "can we assist you today? Please select one " \
               "of options in the following menu: \n" + first_whatsapp_message()
    elif message.lower() == '1':
        return "Choose any of the options below: \n" + second_message(rentingout_json)
    elif message.lower() == '1.1':
        return "Choose type of accommodation you are renting out: \n" + accommodation_message(
            accommodation_json)
    elif message.lower() == '1.1.1':
        return "Please tell us what kind of house that you are renting, including the following an any other " \
               "information you might deem necessary: (1)- how many rooms the full house has   (2)- brief " \
               "description " \
               "of the house   (3)- price of the house   (4)- durawall or not   (5)- gated or not  (6)- tilled or " \
               "not " \
               "  (7)- location and address of the house   (8)- renters full name   (9)contact details   (10)-at " \
               "least two cell numbers   (11)-owners home address "
    elif message.lower() == '1.1.2':
        return "Please tell us what kind of cottage that you are renting, including the following an any other " \
               "information you might deem necessary: (1)- how many rooms the cottage has   (2)- brief description " \
               "of the cottage   (3)- price per month   (4)- durawall or not   (5)- gated or not  (6)- tilled or " \
               "not " \
               "  (7)- location and address of the house   (8)- renters full name   (9)contact details   (10)-at " \
               "least two cell numbers   (11)-owners home address "
    elif message.lower() == '1.1.3':
        return "Please tell us what kind of flat that you are renting, including the following an any other " \
               "information you might deem necessary: (1)- how many rooms the flat has   (2)- furniture available " \
               "in the flat   (3)- price per month  (4)- durawall or not   (5)- gated or not  (6)- tilled or not " \
               "  (7)- location and address of the house   (8)- renters full name   (9)contact details   (10)-at " \
               "least two cell numbers   (11)-owners home address "
    elif message.lower() == '1.1.4':
        return "Please tell us what kind of room that you are renting, including the following an any other " \
               "information you might deem necessary: (1)- is it insuite   (2)- brief description of the room " \
               "(3)- price per month  (4)- durawall or not   (5)- gated or not  (6)- tilled or not " \
               "  (7)- location and address of the house   (8)- renters full name   (9)contact details   (10)-at " \
               "least two cell numbers   (11)-owners home address "
    elif message.lower() == '1.1.5':
        return "Please tell us what kind of apartment/ property that you are renting, including the following an any " \
               "other " \
               "information you might deem necessary: (1)- how many rooms  (2)- brief description of the apartment/ " \
               "property " \
               "in the flat   (3)- price per month  (4)- durawall or not   (5)- gated or not  (6)- tilled or not " \
               "  (7)- location and address of the house   (8)- renters full name   (9)contact details   (10)-at " \
               "least two cell numbers   (11)-owners home address "

    elif message.lower() == '1.2':
        return "Please send us the following information: 1. Type of vehilcle   2. The period the vehicle is " \
               "available for renting.   3. pick-ip location   4. drop-off location   5. price per day   6. terms and " \
               "conditions of use   7. other necessary information   8. vehicle type, e.g. sedan, pickup truck, " \
               "lorries \n"
    elif message.lower() == '1.3':
        return "Please enter the type of occasion equipment you are renting out for example: PA system, Video and " \
               "photography services, Catering services, Decor. \n             Please enter all necessary contact " \
               "information and necessary information for example: -Email Address   -Office Address   -Price Per Day  " \
               " -Pick-up/Service location(Location covered )  \n "
    elif message.lower() == '1.4':
        return "Please enter:    1. the type of equipment you are renting out.   2. the period of equipment " \
               "available " \
               "for renting   3. pick-up location   4. drop-off Location   5. price per day   6. terms and " \
               "conditions " \
               "  7. other information necessary.  Enter equipment types e.g. grader, tractors, ball-mills, " \
               "hammermill, combined harvester.   \n "

    elif message.lower() == '2':
        return "Choose any of the options below: \n" + second_one_message(torent_json)

    elif message.lower() == '2.1':
        return "Choose the house buy typing house then the number of the house, e.g house1: " \
               "(2.1.1)- Available accommodation   (2.1.2)- Didn't see what you " \
               "want? \n "
    elif message.lower() == '2.1.1':
        return "(2.1.1.1) - Low Density.    (2.1.1.2)- High density   (2.1.1.3)- All"
    elif message.lower() == '2.1.1.1':
        return "List of Low density houses :- \n" + get_houses(low_density_json)
    elif message.lower() == '2.1.1.2':
        return "List of High density houses :- \n" + get_houses(high_density_json)
    elif message.lower() == '2.1.1.3':
        return "List of all houses available:- \n" + get_houses(all_houses_json)

    elif message.lower() == '2.1.2':
        return "select option you want from below: \n" + chat3_accommodation_message(accommodation_json)
    elif message.lower() == '2.1.2.1':
        return "tell us what you are looking for, including number of rooms required budget, location preference: " \
               "\n "
    elif message.lower() == '2.1.2.2':
        return "tell us what king of cottage you are looking for, including number of rooms required budget, " \
               "location preference: \n "
    elif message.lower() == '2.1.2.3':
        return "tell us what king of room you are looking for, including required budget, " \
               "location preference: \n "
    elif message.lower() == '2.1.2.4':
        return "tell us what king of house you are looking for, including number of rooms required budget, " \
               "location preference: \n "

    elif message.lower() == '2.2':
        return "Choose from these two options: (2.2.1)- Available vehicles   (2.2.2)- Didn't see what you want? \n"
    elif message.lower() == '2.2.1':
        return "(2.1.1.1) - Private Vehicles.    (2.1.1.2)- Heavy Vehicles   (2.1.1.3)- All"
    elif message.lower() == '2.1.1.1':
        # send to backend as order
        return "A list of all available vehicles :- \n" + get_all_vehicles(private_json)
    elif message.lower() == '2.1.1.2':
        return "A list of all available vehicles :- \n" + get_all_vehicles(heavy_vehicles)
    elif message.lower() == '2.1.1.3':
        return "A list of all available vehicles :-  \n" + get_all_vehicles(all_vehicle_json)

    elif message.lower() == '2.3':
        return "Choose from these two options: (2.3.1)- Available occasions/ equipment  (2.3.2)- Didn't see what " \
               "i was looking for? \n "
    elif message.lower() == '2.3.1':
        return "A list of all available occasions/ equipment :- \n " + get_all_occasions(occasions_json)

    elif message.lower() == '2.4':
        return "Choose from these two options: (2.4.1)- Available equipment   (2.4.2)- Didn't see what i was " \
               "looking for? \n "
    elif message.lower() == '2.4.1':
        return "A list of all available equipment:- \n " + get_all_equipment(equipment_json)
    elif message.lower() == '2.4.2':
        return "Describe equipment you are looking for and one of our guys will contact you: \n "

    elif message.lower() == '4':
        return "4.1: I want to insure my car with a discount: \n"
    elif message.lower() == '4.1':
        return "Please enter your car details including  Reg number, Owner's details, National ID Number, Number of " \
               "terms to be insured, Address of car owner, type of vehicle \n "
        # return print(second_message(ensure_response))

    elif message.lower() == '3':
        return "Choose any of the options below: \n" + option_3_message(caretaker_json)
    elif message.lower() == '3.1':
        return "(3.1.1)- Maids   (3.1.2)- Landscapers : \n"
    elif message.lower() == '3.1.1':
        return "This is a service offered by Lagom Maid Services which offers home-cleaning and garden services " \
               "through providing " \
               "professionally trained maids and gardeners : \n  (3.1.1.1)- Available professional maids   " \
               "(3.1.1.2)- " \
               "Request a specific qualifications "
    elif message.lower() == '3.1.1.1':
        return "a list of available maids:" + get_all_maids(maids_json)
    elif message.lower() == '3.1.1.2':
        return "Please tell us qualification you are looking for, include the following: budget, expected, " \
               "term of service, location, live-in or non-live in, specific experience "
    elif message.lower() == '3.1.2':
        return "This is a service offered by Lagom Maid Services which offers home-cleaning and garden services " \
               "through providing " \
               "professionally trained maids and gardeners : \n  (3.1.2.1)- Available professional Landscapers   " \
               "(3.1.2.2)- " \
               "Request a specific qualifications "

    elif message.lower() == '3.1.2.2':
        return "Please tell us the special qualification you are looking for, in the maid, include the following: " \
               "budget, expected, " \
               "term of service, location, live-in or non-live in, specific experience "
    elif message.lower() == '3.2':
        return "(3.2.1)- Maids   (3.2.2)- Landscapers : \n"
    elif message.lower() == '3.2.1':
        return "This is a service offered by Lagom Maid Services which offers home-cleaning and garden services " \
               "through providing " \
               "professionally trained maids and gardeners : \n  (3.2.1.1)- Available professional maids   " \
               "(3.2.1.2)- " \
               "didn't see what you are looking for "
    elif message.lower() == '3.1.2.1':
        return "A list of available landscapers: " + get_all_garden(garden_boy_json)
    elif message.lower() == '3.1.2.2':
        return "Please contact our support team on 0719938912 during business hours or visit our office at Main " \
               "Bata in Robert Mugabe Way, upstairs Office No.3: "

    elif message.lower() == '0':
        return first_whatsapp_message()

    elif len(message) > 8:
        return "Thank you for placing your item on rentout, one of our team members will contact you for more " \
               "information. We will have renter contacting you soon. If this is not what you are looking for, " \
               "for main menu send 0"
    else:
        return "Thank you for contacting the rentout chat service, how may we help you today?"


# reply_message(get_message())
# checking for new messages
def check_for_message():
    # pt.moveTo(x + 95, y - 35, duration=.5)
    while True:
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.6)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except Exception:
            print('No new messages at the moment with green dot')

        if pt.pixelMatchesColor(int(x + 95), int(y - 35), (255, 255, 255), tolerance=10):
            print('is white')
            processed_message = process_response(get_message())
            reply_message(processed_message)
        elif pt.pixelMatchesColor(int(x + 95), int(y - 35), (240, 240, 240), tolerance=10):
            print('is not white')
            pt.moveTo(position1)
            pt.moveRel(70, -200)
            processed_message = process_response(get_message())
            reply_message(processed_message)

        else:
            print('no new messages at the moment')


check_for_message()
