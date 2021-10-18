# Gabriel A. Viera Perez and Jose Raul Rivera Rodriguez
# CIIC 3015 Lab Project 2


def Project2():
    CMD_BED = ('b', 'bed')
    CMD_CLOSE = ('c', 'close')
    CMD_EAST = ('e', 'east')
    CMD_FEED = ('f', 'feed')
    CMD_GET = ('g', 'get')
    CMD_LOCK = ('l', 'lock')
    CMD_NORTH = ('n', 'north')
    CMD_OPEN = ('o', 'open')
    CMD_PUT = ('p', 'put')
    CMD_QUIT = ('q', 'quit')
    CMD_SOUTH = ('s', 'south')
    CMD_TV = ('t', 'tv', 'television')
    CMD_UNLOCK = ('u', 'unlock')
    CMD_WEST = ('w', 'west')

    ROOM_FRONT = 0
    ROOM_LIVING = 1
    ROOM_KITCHEN = 2
    ROOM_OFFICE = 3
    ROOM_BED = 4

    ROOM_NAMES = ("Front Door", "Living Room", "Kitchen", "Office", "Bedroom")

    flag_me_awake = True
    flag_tv_on = False
    pantry_is_locked = True
    pantry_is_closed = True
    safe_is_closed = True
    stella_is_happy = False
    stella_have_bone = False
    bone_in_pocket = False
    bone_in_pantry = True
    spam_in_pocket = False
    spam_in_bedroom = True
    spam_in_pantry = False
    key_in_pocket = False
    key_in_safe = True

    scenes = {"Front Door": '1', "Living Room": '1', "Kitchen": "1", "Office": '1', "Bedroom": '1'}
    room = 0
    turn = 0

    print("\nWhat an awful day! You are completely exhausted, all you want to do is climb into bed and collapse. "
            "Unfortunately, that is easier said than done…\n")
    print("CIIC 3015 Autumn 2021 Project 2: Time For Go-To-Bed\n")
    print("Good luck, Have fun! ;)\n")

    while flag_me_awake:
        print('-' * 20)
        if room == ROOM_LIVING:
            if stella_is_happy and not flag_tv_on:
                scenes.update({ROOM_NAMES[room]: '4'})
            elif flag_tv_on and stella_have_bone:
                scenes.update({ROOM_NAMES[room]: '3'})
            elif not flag_tv_on and stella_have_bone:
                scenes.update({ROOM_NAMES[room]: '2'})
            elif flag_tv_on and not stella_is_happy:
                scenes.update({ROOM_NAMES[room]: '1.1'})
            else:
                scenes.update({ROOM_NAMES[room]: '1'})
            if flag_tv_on:
                print('The TV is ON')
            else:
                print('The TV is OFF')
            if not stella_is_happy:
                if stella_have_bone and flag_tv_on:
                    stella_is_happy = True
                    print(
                        'Stella is happily chewing on her nice, tasty bone and completely ignores you as you walk into the bedroom.')
                else:
                    print('Stella is here, looking hungry and disappointed')
        elif room == ROOM_OFFICE:
            if safe_is_closed and not key_in_safe:
                scenes.update({ROOM_NAMES[room]: '4'})
            elif not safe_is_closed and not key_in_safe:
                scenes.update({ROOM_NAMES[room]: '3'})
            elif not safe_is_closed and key_in_safe:
                scenes.update({ROOM_NAMES[room]: '2'})
            elif safe_is_closed and key_in_safe:
                scenes.update({ROOM_NAMES[room]: '1'})

            if safe_is_closed:
                print('The office safe is closed.')
            else:
                print('The office safe is open.')

            if not safe_is_closed and key_in_safe:
                print('Inside the safe you can see the pantry door key.')
            elif not safe_is_closed and not key_in_safe:
                print('There is nothing inside the safe.')
        elif room == ROOM_KITCHEN:
            if pantry_is_closed and not bone_in_pantry and not spam_in_pantry:
                scenes.update({ROOM_NAMES[room]: '4'})
            elif not pantry_is_closed and not bone_in_pantry and not spam_in_pantry:
                scenes.update({ROOM_NAMES[room]: '3'})
            elif spam_in_pantry and not pantry_is_closed:
                scenes.update({ROOM_NAMES[room]: '2.2'})
            elif bone_in_pantry and not pantry_is_closed:
                scenes.update({ROOM_NAMES[room]: '2'})
            elif spam_in_pantry and pantry_is_closed:
                scenes.update({ROOM_NAMES[room]: '1.1'})
            elif bone_in_pantry and pantry_is_closed:
                scenes.update({ROOM_NAMES[room]: '1'})
            if pantry_is_closed:
                print('The pantry door is closed.')
            else:
                print('The pantry door is open.')
        elif room == ROOM_BED:
            if spam_in_bedroom:
                scenes.update({ROOM_NAMES[room]: '1'})
            elif not spam_in_bedroom:
                scenes.update({ROOM_NAMES[room]: '2'})
        print("Location: ", ROOM_NAMES[room])
        print(visuals(ROOM_NAMES[room], scenes.get(ROOM_NAMES[room])))
        cmd = input("\n> ").lower()
        turn += 1

        if cmd in CMD_QUIT:
            return False

        if room == ROOM_FRONT:
            if cmd in CMD_EAST:
                print("Home, sweet home! You enter your house.")
                room = ROOM_LIVING
                continue

        if room == ROOM_LIVING:
            if cmd in CMD_NORTH:
                if not stella_is_happy:
                    print("Stella won't let you into the room unless you feed her.")
                else:
                    room = ROOM_BED
                continue
            if cmd in CMD_WEST:
                print('You just got home, do you really want to leave?')
                continue
            if cmd in CMD_EAST:
                room = ROOM_OFFICE
                continue
            if cmd in CMD_SOUTH:
                room = ROOM_KITCHEN
                continue
            if cmd in CMD_TV:
                flag_tv_on = not flag_tv_on
                continue
            if cmd in CMD_FEED:
                if bone_in_pocket and flag_tv_on:
                    stella_have_bone = True
                    bone_in_pocket = False
                    print(
                        'Stella hungrily snatches the nice tasty bone out of your hand and starts to chew on it. She no longer seems to notice or care that you are there.')
                elif bone_in_pocket and not flag_tv_on:
                    print(
                        '\nStella seems tense. She is glancing at the bone in your hand, and the silent tv. Every now and then she makes a sad little noise.')
                elif stella_have_bone and not bone_in_pocket:
                    print('Stella already has the bone')
                elif not bone_in_pocket:
                    print("\nYou have nothing to feed Stella, though I remember there was a good looking bone was in the kitchen. That ought to do it.")
                continue

        if room == ROOM_OFFICE:
            if cmd in CMD_WEST:
                room = ROOM_LIVING
                continue

            if cmd in CMD_CLOSE:
                if safe_is_closed:
                    print("The safe is already closed.")
                    continue
                safe_is_closed = True
                print("The safe is now closed.")
                continue

            if cmd in CMD_GET:
                if safe_is_closed:
                    print("You can't get the key, the safe is closed.")
                elif key_in_safe:
                    key_in_safe = False
                    key_in_pocket = True
                    print('You get the key from the safe and put it in your pocket.')
                elif not key_in_safe:
                    print('There is nothing to get from the safe.')

                continue

            if cmd in CMD_OPEN:
                if not safe_is_closed:
                    print('The safe is already open.')
                    continue
                print(
                    "Please enter the combination to the safe, one number at a time. Surely you remember that the numbers are the three iterations following 42 in the Collatz sequence.")
                temp = input("First number? ")
                if temp == "21":
                    temp = input("Second number? ")
                    if temp == "64":
                        temp = input("Third number? ")
                        if temp == "32":
                            print(
                                "You hear a satisfying 'Ka-CHUNK' as the handle turns and the safe door swings invitingly open. ")
                            safe_is_closed = False

                            continue
                print("Nope. That's not it. The locked safe silently mocks you.")
                continue

            if cmd in CMD_PUT:
                if key_in_pocket and not safe_is_closed:
                    key_in_pocket = False
                    key_in_safe = True
                    "You put the key in the safe."
                elif safe_is_closed:
                    print('You can put anything in the safe if it is closed, dummy.')
                elif not key_in_pocket:
                    print("You can't put the key into the safe if your don't have it.")
                continue

        if room == ROOM_KITCHEN:

            if cmd in CMD_NORTH:
                room = ROOM_LIVING
                continue

            if cmd in CMD_CLOSE:
                if pantry_is_closed:
                    print("Pantry door is already closed.")
                else:
                    pantry_is_closed = True
                    print("Pantry door is now closed.")
                continue

            if cmd in CMD_GET:
                if pantry_is_closed:
                    print('The pantry door is closed.')
                elif bone_in_pantry:
                    print(
                        'You take the nice tasty bone out of the pantry. Stella watches you with great interest from the living room.')
                    bone_in_pocket = True
                    bone_in_pantry = False
                elif spam_in_pantry:
                    print('You take the lovely spam from the pantry.')
                    spam_in_pocket = True
                    spam_in_pantry = False
                elif bone_in_pocket:
                    print('You already have the bone.')
                elif spam_in_pocket:
                    print('You already have the lovely spam.')
                continue

            if cmd in CMD_LOCK:
                if pantry_is_locked:
                    print("Pantry door is already locked.")
                elif not pantry_is_closed:
                    print("The pantry door is open, close it before locking.")
                elif pantry_is_closed and not pantry_is_locked:
                    pantry_is_locked = True
                    print("Pantry door is now locked.")
                continue

            if cmd in CMD_OPEN:
                if not pantry_is_closed:
                    print("Pantry door is already open.")
                elif pantry_is_locked:
                    print("The pantry door is locked.")
                elif not pantry_is_locked and pantry_is_closed:
                    pantry_is_closed = False
                    print("Pantry door is now open.")
                continue

            if cmd in CMD_PUT:
                if pantry_is_closed:
                    print('The pantry door is closed.')
                elif (bone_in_pocket and spam_in_pantry) or (spam_in_pocket and bone_in_pocket):
                    print("There is no space in the pantry.")
                elif bone_in_pocket and not pantry_is_closed:
                    print('Stella stares at you with murderous intent as you put the bone away in the pantry.')
                    bone_in_pocket = False
                    bone_in_pantry = True
                elif spam_in_pocket and not pantry_is_closed:
                    print('You put the lovely spam into the pantry.')
                    spam_in_pocket = False
                    spam_in_pantry = True
                continue

            if cmd in CMD_UNLOCK:
                if not pantry_is_locked:
                    print('The pantry is already unlocked.')
                elif pantry_is_closed and pantry_is_locked and not key_in_pocket:
                    print("You don't have the key to unlock the pantry door.")
                elif pantry_is_closed and pantry_is_locked and key_in_pocket:
                    print('The pantry door is unlocked.')
                    pantry_is_locked = False

                continue

        if room == ROOM_BED:

            if cmd in CMD_SOUTH:
                room = ROOM_LIVING
                continue

            if cmd in CMD_BED:
                if flag_tv_on:
                    print("The tv is so loud. It would be impossible to sleep like this.")
                elif not pantry_is_closed:
                    print("The pantry door is open, better close it before we sleep.")
                elif not pantry_is_locked:
                    print("The pantry door is unlocked, we can't go to sleep, right?")
                elif not safe_is_closed:
                    print("The safe door is open, we need to close it, that's the whole point of a safe.")
                elif spam_in_pocket or bone_in_pocket or key_in_pocket:
                    print("You have too many things in your pockets and it makes you uncomfortable, empty them.")
                elif spam_in_bedroom:
                    print("You see a can of lovely spam. Wait, what's that doing in the bedroom?")
                else:
                    flag_me_awake = False
                continue

            if cmd in CMD_GET:
                if spam_in_bedroom:
                    spam_in_pocket = True
                    spam_in_bedroom = False
                    print('You grab the can of lovely spam.')
                elif not spam_in_bedroom:
                    print("There's nothing to grab from the room.")
                continue

            if cmd in CMD_PUT:
                if spam_in_pocket:
                    spam_in_bedroom = True
                    spam_in_pocket = False
                else:
                    print("You don't have anything to put in the bedroom")
                continue

        print("Illegal command.")

    print(visuals('Bedroom', '3'))
    print('Sleep! At last! You win!')
    print(turn, "turns played.")
    return True


def visuals(room, scene):
    house = {
        'Front Door': {
            '1': (
                f'                   -\n'
                f'  =_               |\n'
                f'   l               |\n'
                f'            ___o__/-\n'
                f'                    \n'
                f'                    \n'
                f'                   -\n'
                f'                   |\n'
                f'                   |\n'
                f'                   -\n'),
        },
        'Living Room': {
            '1': (
                f'------|         |------\n'
                f'|      o/~\___        |\n'
                f'|         ||  |\      |\n'
                f'-                     -\n'
                f'                       \n'
                f'                       \n'
                f'-               \ /   -\n'
                f'|              |OFF|  |\n'
                f'|                ^    |\n'
                f'------|         |------\n'),
            '1.1': (
                f'------|         |------\n'
                f'|      o/~\___        |\n'
                f'|         ||  |\      |\n'
                f'-                     -\n'
                f'                       \n'
                f'                       \n'
                f'-               \ /   -\n'
                f'|              |O N|  |\n'
                f'|                ^    |\n'
                f'------|         |------\n'),
            '2': (
                f'------|         |------\n'
                f'|      o/~\___        |\n'
                f'|     8=8 ||  |\      |\n'
                f'-                     -\n'
                f'                       \n'
                f'                       \n'
                f'-               \ /   -\n'
                f'|              |OFF|  |\n'
                f'|                ^    |\n'
                f'------|         |------\n'
            ),
            '3': (
                f'------|         |------\n'
                f'|              o/^\    |\n'
                f'|             8=8||_\/ |\n'
                f'-                     -\n'
                f'                       \n'
                f'                       \n'
                f'-               \ /   -\n'
                f'|              |O N|  |\n'
                f'|                ^    |\n'
                f'------|         |------\n'
            ),
            '4': (
                f'------|         |------\n'
                f'|              o/^\    |\n'
                f'|             8=8||_\/ |\n'
                f'-                     -\n'
                f'                       \n'
                f'                       \n'
                f'-               \ /   -\n'
                f'|              |OFF|  |\n'
                f'|                ^    |\n'
                f'------|         |------\n'
            )
        },
        'Kitchen': {
            '1': (
                f'------|         |------\n'
                f'| 8=8 |               |\n'
                f'|__o__|               |\n'
                f'|               ______|\n'
                f'|              |___   |\n'
                f'|                  |0 |\n'
                f'|         h[//]    |0 |\n'
                f'|         h[//]    |__|\n'
                f'|                     |\n'
                f'-----------------------\n'
            ),
            '1.1': (
                f'------|         |------\n'
                f'||spm||               |\n'
                f'|__o__|               |\n'
                f'|               ______|\n'
                f'|              |___   |\n'
                f'|                  |0 |\n'
                f'|         h[//]    |0 |\n'
                f'|         h[//]    |__|\n'
                f'|                     |\n'
                f'-----------------------\n'
            ),
            '2': (
                f'------|         |------\n'
                f'| 8=8 |               |\n'
                f'|_    |               |\n'
                f'|o\             ______|\n'
                f'|              |___   |\n'
                f'|                  |0 |\n'
                f'|         h[//]    |0 |\n'
                f'|         h[//]    |__|\n'
                f'|                     |\n'
                f'-----------------------\n'
            ),
            '2.2': (
                f'------|         |------\n'
                f'||spm||               |\n'
                f'|_    |               |\n'
                f'|o\             ______|\n'
                f'|              |___   |\n'
                f'|                  |0 |\n'
                f'|         h[//]    |0 |\n'
                f'|         h[//]    |__|\n'
                f'|                     |\n'
                f'-----------------------\n'
            ),
            '3': (
                f'------|         |------\n'
                f'|     |               |\n'
                f'|_    |               |\n'
                f'|o\             ______|\n'
                f'|              |___   |\n'
                f'|                  |0 |\n'
                f'|         h[//]    |0 |\n'
                f'|         h[//]    |__|\n'
                f'|                     |\n'
                f'-----------------------\n'
            ),
            '4': (
                f'------|         |------\n'
                f'|     |               |\n'
                f'|__o__|               |\n'
                f'|               ______|\n'
                f'|              |___   |\n'
                f'|                  |0 |\n'
                f'|         h[//]    |0 |\n'
                f'|         h[//]    |__|\n'
                f'|                     |\n'
                f'-----------------------\n'
            )
        },
        'Bedroom': {
            '1': (
                f'-----------------------\n'
                f'|| |spm|  |   _______ |\n'
                f'||________|  |_______||\n'
                f'|            |       ||\n'
                f'|            |       ||\n'
                f'|            |_______||\n'
                f'|                     |\n'
                f'|                     |\n'
                f'|                     |\n'
                f'------|         |------\n'),
            '2': (
                f'-----------------------\n'
                f'||        |   _______ |\n'
                f'||________|  |_______||\n'
                f'|            |       ||\n'
                f'|            |       ||\n'
                f'|            |_______||\n'
                f'|                     |\n'
                f'|                     |\n'
                f'|                     |\n'
                f'------|         |------\n'),
            '3': (
                f'-----------------------   _____\n'
                f'||        |   _______ | _/ zZZ |\n'
                f'||________|  |__ ()__||<_zZ____|\n'
                f'|            |  /||\ ||\n'
                f'|            |   /\  ||\n'
                f'|            |_______||\n'
                f'|                     |\n'
                f'|                     |\n'
                f'|                     |\n'
                f'------|         |------\n')
        },
        'Office': {
            '1': (
                f'----------------------\n'
                f'|            |       |\n'
                f'|            #  n=@  |\n'
                f'-            |_______|\n'
                f'                __   |\n'
                f'               |  |  |\n'
                f'-              |[I|_||\n'
                f'|              |__|  |\n'
                f'|                    |\n'
                f'----------------------\n'),
            '2': (
                f'----------------------\n'
                f'|          #_/       |\n'
                f'|               n=@  |\n'
                f'-            |_______|\n'
                f'                __   |\n'
                f'               |  |  |\n'
                f'-              |[I|_||\n'
                f'|              |__|  |\n'
                f'|                    |\n'
                f'----------------------\n'
            ),
            '3': (
                f'----------------------\n'
                f'|          #_/       |\n'
                f'|                    |\n'
                f'-            |_______|\n'
                f'                __   |\n'
                f'               |  |  |\n'
                f'-              |[I|_||\n'
                f'|              |__|  |\n'
                f'|                    |\n'
                f'----------------------\n'
            ),
            '4': (
                f'----------------------\n'
                f'|            |       |\n'
                f'|            #       |\n'
                f'-            |_______|\n'
                f'                __   |\n'
                f'               |  |  |\n'
                f'-              |[I|_||\n'
                f'|              |__|  |\n'
                f'|                    |\n'
                f'----------------------\n'
            )

        }
    }
    return house[room].get(scene)


print(Project2())

# <3
