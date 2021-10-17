
# Location commands work perfectly
# Lock, open, tv, and close commands work as intended
#


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
    key_acquired = False
    safe_is_closed = True
    stella_is_happy = False
    stella_have_bone = False
    bone_in_pocket = False
    spam_in_pocket = False
    key_in_pocket = False
    
    scenes = {"Front Door":'1',"Living Room":'1', "Kitchen":"1", "Office":'1',"Bedroom":'1'}
    room = 0
    turn = 0
    
    print("\nWhat an awful day! You are completely exhausted, all you want to do is climb into bed and collapse. "
            "Unfortunately, that is easier said than done…\n")
    print("CIIC 3015 Autumn 2021 Project 2: Time For Go-To-Bed\n")
    print("Good luck, Have fun! ;)\n")

    while flag_me_awake:
        print('-'*20)
        if room == ROOM_LIVING:
            if(stella_is_happy and not(flag_tv_on)):
                    scenes.update({ROOM_NAMES[room]:'4'})
            elif(flag_tv_on and stella_have_bone):
                    scenes.update({ROOM_NAMES[room]:'3'})
            elif(not(flag_tv_on) and stella_have_bone):
                    scenes.update({ROOM_NAMES[room]:'2'})
            elif(flag_tv_on and not(stella_is_happy)):
                    scenes.update({ROOM_NAMES[room]:'1.1'})
            else:scenes.update({ROOM_NAMES[room]:'1'})
            if flag_tv_on : print('The TV is ON')
            else: print('The TV is OFF')
            if not(stella_is_happy):
                if stella_have_bone and flag_tv_on:
                    stella_is_happy = True
                    print('Stella is happily chewing on ther nice tasty bone and completely ignores you as you walk into the bedroom')
                elif stella_have_bone and not flag_tv_on :
                    print('\nStella seems tense. She glancing from the bone in your hand, to the silent tv, to you, and back to silent tv again. Every now and then she makes a sad little noise.')
                else:
                    print('Stella is here, looking hungry and disappointed')

        print("Location: ", ROOM_NAMES[room])
        print(visuals(ROOM_NAMES[room],scenes.get(ROOM_NAMES[room])))
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
                room = ROOM_BED
                continue
            if cmd in CMD_WEST:
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
                if(bone_in_pocket):
                    stella_have_bone = True
                    bone_in_pocket = False
                    print('Stella hungrily snatches the nice tasty bone out of your hand and starts to chew on it. She no longer seems to notice or care that you are here.')
                else:
                    print("\nYou can't feed Stella rigth now. I think in the kitchen there are a good looking bone.")
                continue


        if room == ROOM_OFFICE:
            if cmd in CMD_WEST:
                print("print for entering living room: office")
                room = ROOM_LIVING
                continue

            if cmd in CMD_CLOSE:
                if safe_is_closed:
                    print("safe is already closed")
                    continue
                safe_is_closed = True
                print("safe is now closed")
                continue

            if cmd in CMD_GET:
                print()
                continue

            if cmd in CMD_LOCK:
                print("print for lock: office")
                continue

            if cmd in CMD_OPEN:
                print("enter the combination one at a time")
                temp = input("first num")
                if temp == "21":
                    temp = input("second num")
                    if temp == "64":
                        temp = input("third num")
                        if temp == "32":
                            print("safe is opened")
                            continue
                print("u suck, ure a disgrace, you dont know anything about the collatz sequence </3")
                continue

            if cmd in CMD_PUT:
                print()
                continue

            if cmd in CMD_UNLOCK:
                print()
                continue

        if room == ROOM_KITCHEN:

            if cmd in CMD_NORTH:
                print("print for entering the living room: kitchen")
                room = ROOM_LIVING
                continue

            if cmd in CMD_CLOSE:
                if pantry_is_closed:
                    print("pantry is already closed")
                    continue
                pantry_is_closed = True
                print("pantry is now closed")
                continue

            if cmd in CMD_GET:
                print()
                continue

            if cmd in CMD_LOCK:
                if pantry_is_locked:
                    print("pantry is already locked")
                    continue
                if pantry_is_closed:
                    pantry_is_locked = True
                    print("pantry is now locked")
                    continue
                print("please close the pantry before locking it dumbass")
                continue

            if cmd in CMD_OPEN:
                if not pantry_is_closed:
                    print("pantry is already open")
                    continue
                if key_acquired:
                    pantry_is_closed = False
                    print("pantry is now open")
                    continue
                print("you need a key :)")
                continue

            if cmd in CMD_PUT:
                print()
                continue

            if cmd in CMD_UNLOCK:
                print()
                continue

        if room == ROOM_BED:

            if cmd in CMD_SOUTH:
                print("print for entering the living room: bed")
                room = ROOM_LIVING
                continue

            if cmd in CMD_BED:
                print()
                continue

            if cmd in CMD_GET:
                print()
                continue

            if cmd in CMD_PUT:
                print()
                continue

        print("Illegal command.")

    print(turn, "turns played.")
    return True



def visuals(room,scene):
    house = {
        'Front Door':{
            '1':(
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
            '2':(
                f'----------------------\n'
                f'|                    |\n'
                f'|                    |\n'
                f'-\                   -\n'
                f' |                    \n'
                f' |o                   \n'
                f'-|                   -\n'
                f'|                    |\n'
                f'|                    |\n'
                f'----------------------\n')
        },
        'Living Room':{
            '1':(
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
            '1.1':(
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
            '2':(
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
            '3':(
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
            '4':(
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
        'Kitchen':{
            '1':(
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
            '2':(
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
            '3':(
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
            '4':(
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
        'Bedroom':{
            '1':(
                f'-----------------------\n'
                f'|| |spam| |   _______ |\n'
                f'||________|  |_______||\n'
                f'|            |       ||\n'
                f'|            |       ||\n'
                f'|            |_______||\n'
                f'|                     |\n'
                f'|                     |\n'
                f'|                     |\n'
                f'------|         |------\n'),
            '2':(
                f'-----------------------\n'
                f'||        |   _______ |\n'
                f'||________|  |_______||\n'
                f'|            |       ||\n'
                f'|            |       ||\n'
                f'|            |_______||\n'
                f'|                     |\n'
                f'|                     |\n'
                f'|                     |\n'
                f'------|         |------\n')
        },
        'Office':{
            '1':(
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
            '2':(
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
            '3':(
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
            '3':(
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
    return(house[room].get(scene))

Project2()

# <3


