
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

    room = 0
    turn = 0
    

    print("\nWhat an awful day! You are completely exhausted, all you want to do is climb into bed and collapse. "
            "Unfortunately, that is easier said than done…\n")
    print("CIIC 3015 Autumn 2021 Project 2: Time For Go-To-Bed\n")
    print("Good luck, Have fun! ;)\n")

    while flag_me_awake:

        print("Location: ", ROOM_NAMES[room])
        print(visuals(ROOM_NAMES[room],'1'))
        cmd = input("> ").lower()
        turn += 1

        if cmd in CMD_QUIT:
            return False

        if room == ROOM_LIVING:
            if cmd in CMD_WEST:
                print("print for leaving the house: living")
                continue

            if cmd in CMD_EAST:
                print("print for entering the office: living")
                room = ROOM_OFFICE
                continue

            if cmd in CMD_NORTH:
                print("print for entering the bedroom: living")
                room = ROOM_BED
                continue

            if cmd in CMD_SOUTH:
                print("print for entering the kitchen: living")
                room = ROOM_KITCHEN
                continue

            if cmd in CMD_TV:
                if flag_tv_on:
                    print("print for tv is now off: living")
                else:
                    print("print for tv is now on: living")
                flag_tv_on = not flag_tv_on
                continue

            if cmd in CMD_BED:
                print()
                continue

            if cmd in CMD_CLOSE:
                print("print for close: living")
                continue

            if cmd in CMD_FEED:
                print()
                continue

            if cmd in CMD_GET:
                print()
                continue

            if cmd in CMD_LOCK:
                print("print for lock: living")
                continue

            if cmd in CMD_OPEN:
                print("print for open: living")
                continue

            if cmd in CMD_PUT:
                print()
                continue

            if cmd in CMD_UNLOCK:
                print()
                continue

        if room == ROOM_FRONT:
            if cmd in CMD_WEST:
                print("print for west: front")
                continue

            if cmd in CMD_EAST:
                print("print for entering the house(living room): front")
                room = ROOM_LIVING
                continue

            if cmd in CMD_NORTH:
                print("print for north: front")
                continue

            if cmd in CMD_SOUTH:
                print("print for south: front")
                continue

            if cmd in CMD_TV:
                print("print for tv: front")
                continue

            if cmd in CMD_BED:
                print()
                continue

            if cmd in CMD_CLOSE:
                print("print for close: front")
                continue

            if cmd in CMD_FEED:
                print()
                continue

            if cmd in CMD_GET:
                print()
                continue

            if cmd in CMD_LOCK:
                print("print for lock: front")
                continue

            if cmd in CMD_OPEN:
                print("print for open: front")
                continue

            if cmd in CMD_PUT:
                print()
                continue

            if cmd in CMD_UNLOCK:
                print()
                continue

        if room == ROOM_OFFICE:
            if cmd in CMD_WEST:
                print("print for entering living room: office")
                room = ROOM_LIVING
                continue

            if cmd in CMD_EAST:
                print("print for east: office")
                continue

            if cmd in CMD_NORTH:
                print("print for north: office")
                continue

            if cmd in CMD_SOUTH:
                print("print for south: office")
                continue

            if cmd in CMD_TV:
                print("print for tv: office")
                continue

            if cmd in CMD_BED:
                print()
                continue

            if cmd in CMD_CLOSE:
                if safe_is_closed:
                    print("safe is already closed")
                    continue
                safe_is_closed = True
                print("safe is now closed")
                continue

            if cmd in CMD_FEED:
                print()
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
            if cmd in CMD_WEST:
                print("print for west: kitchen")
                continue

            if cmd in CMD_EAST:
                print("print for east: kitchen")
                continue

            if cmd in CMD_NORTH:
                print("print for entering the living room: kitchen")
                room = ROOM_LIVING
                continue

            if cmd in CMD_SOUTH:
                print("print for south: kitchen")
                continue

            if cmd in CMD_TV:
                print("print for tv: kitchen")
                continue

            if cmd in CMD_BED:
                print()
                continue

            if cmd in CMD_CLOSE:
                if pantry_is_closed:
                    print("pantry is already closed")
                    continue
                pantry_is_closed = True
                print("pantry is now closed")
                continue

            if cmd in CMD_FEED:
                print()
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
            if cmd in CMD_WEST:
                print("print for west: bed")
                continue

            if cmd in CMD_EAST:
                print("print for east: bed")
                continue

            if cmd in CMD_NORTH:
                print("print for north: bed")
                continue

            if cmd in CMD_SOUTH:
                print("print for entering the living room: bed")
                room = ROOM_LIVING
                continue

            if cmd in CMD_TV:
                print("print for tv: bed")
                continue

            if cmd in CMD_BED:
                print()
                continue

            if cmd in CMD_CLOSE:
                print("print for close: bed")
                continue

            if cmd in CMD_FEED:
                print()
                continue

            if cmd in CMD_GET:
                print()
                continue

            if cmd in CMD_LOCK:
                print("print for lock: bed")
                continue

            if cmd in CMD_OPEN:
                print("print for open: bed")
                continue

            if cmd in CMD_PUT:
                print()
                continue

            if cmd in CMD_UNLOCK:
                print()
                continue
        print("Illegal command.")

    print(turn, "turns played.")
    return True



def visuals(room,scene):
    house = {
        'Front Door':{
            '1':(
                f'----------------------\n'
                f'|                    |\n'
                f'|                    |\n'
                f'-\__o___             -\n'
                f'                      \n'
                f'                      \n'
                f'-                    -\n'
                f'|                    |\n'
                f'|                    |\n'
                f'----------------------\n'),
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
                f'|      o/~\___       |\n'
                f'|         ||  |\       |\n'
                f'-                     -\n'
                f'                       \n'
                f'                       \n'
                f'-               \ /   -\n'
                f'|              |OFF|  |\n'
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


