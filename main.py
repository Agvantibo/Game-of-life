try:
    import gearbox as g
    from sys import exit
    from time import sleep
    from playsound import playsound
    from colorama import init
except ImportError:
    print('\033[1;31;49mWarning! Some packages required for the project to work are not installed!\033[1;30;49m')
    print('''Here are all required packages packages:
    gearbox
    playsound
    colorama''')
    sleep(2)
    exit("Goodbye!")
init()
print('''\033[1;33;49m                                        
     ____
    //   ) )                                    
   //         ___      _   __      ___          
  //  ____  //   ) ) // ) )  ) ) //___) )       
 //    / / //   / / // / /  / / //              
((____/ / ((___( ( // / /  / / ((____           
              ___                    ___
             //  ) )       _        //  ) )     
    ___   __//__          // ( ) __//__  ___    
  //   ) ) //            // / /   //   //___) ) 
 //   / / //            // / /   //   //        
((___/ / //            // / /   //   ((____     ''')
print()
print('''\033[1;34;49mType the name of the input file and press enter,
or press _ and enter for full console mode\033[1;30;49m''')
filename = input()
if filename == '':
    filename = 'INPUT'
    print('Loading default input file')
console = False
if filename == '_':
    print('Full console mode on!')
    console = True
if not console:
    print('Loading...')
    print('[▓▓▓', end='')
    try:
        INPUT = open(filename, 'r')
    except FileNotFoundError:
        playsound("assets\Error_buzz.mp3")
        g.print_red('Input file listed does not exist.')
        sleep(2)
        exit()
    print('▓▓▓', end='')
    code = []
    for i in INPUT.readlines():
        code.append(i[:len(i) - 1])
    INPUT.close()
    print('▓▓▓', end='')
    try:
        height = int(code[0][7:])   # Getting the height of the square
        code.pop(0)
        speed = int(code[0][6:])
        code.pop(0)
        dead = code[0][5:]
        code.pop(0)
        live = code[0][5:]
        code.pop(0)
        code.pop(0)
    except ValueError:
        playsound('assets\Error_buzz.mp3')
        print('Invalid input value, check the INPUT file')
        sleep(2)
        exit()
    except IndexError:
        playsound('assets\Error_buzz.mp3')
        print('Invalid input value, check the INPUT file')
        sleep(2)
        exit()
    print('▓▓▓', end='')
    to_do = []
    if speed < 0:
        speed = abs(speed)
    print('▓▓▓', end='')
    for i in code:
        try:
            x, y = [int(i) for i in i.split()]
            to_do.append(g.coordinate(x, y))
        except ValueError:
            playsound('assets\Error_buzz.mp3')
            print('Invalid coordinate values')
            sleep(2)
            exit()

    # inputs done
    print('▓▓▓]')
    print('LOADED SUCCESSFULLY!')
else:
    code = []
    print('''Enter one by one:
    size of the field (int)
    speed of simulation (int)
    symbol for dead cells(str)
    symbol for live cells(str)
    coordinates in format 'x y'
    press ^ (Shift-6) and enter to finish coordinate input''')
    try:
        height = int(input())
        speed = int(input())
    except ValueError:
        playsound('assets\Error_buzz.mp3')
        print('Invalid input value')
        sleep(2)
        exit()
    dead = input()
    live = input()
    to_do = []
    while True:
        _input = input()
        if _input == '^':
            break
        try:
            x, y = [int(i) for i in _input.split()]
            to_do.append(g.coordinate(x, y))
        except ValueError:
            playsound('assets\Error_buzz.mp3')
            print('Invalid coordinate values')
            sleep(2)
            exit()
field = g.dim_list(g.create2DArray(dead, height))
for i in to_do:
    field.write(i, live)
field.print('  ')
print("Start simulation? [Y/N]")
while True:
    ans = input().capitalize()

    if ans == 'Y':
        print('Starting simulation...')
        break
    elif ans == 'N':
        sleep(0.5)
        exit('Goodbye!')
    else:
        playsound('assets\Error_buzz.mp3')
        print('Invalid input value, check the INPUT file')
        sleep(2)
        exit()
if speed > 0:
    g.print_red('The program will run indefinitely, and the only way to stop it is to terminate it')
else:
    print('To advance simulation press enter, to quit terminate process or type exit and press enter')
    testfile = open('assets/scrcheck.ignore', 'w')
    try:
        testfile.write(dead)
        testfile.write(live)
    except UnicodeEncodeError:
        playsound("assets\Error_buzz.mp3")
        g.print_red('Screenshot unavailable, please check README for more information')
    else:
        print('To make a screenshot type s and press enter. Last position will be saved to screenshots.')
    finally:
        testfile.close()
# The secure-beautiful part done, now, real emulation begins!
input('Press enter to continue')
field.print('  ')
field_tmp = field.array.copy()
location = g.coordinate(0, 0)
iterator = 0
while True:
    if speed > 0:
        sleep(speed)
    else:
        ask = input().upper()
        if ask == 'EXIT':
            sleep(0.5)
            exit('Goodbye')
        elif ask == 'S':
            with open('assets\SCREENSHOTS', 'a') as f:
                for i in field.array:
                    appender = '  '.join(i)
                    f.write(appender)
                    f.write('\n')
                f.write('\n')
    for i in field.array:
        for j in i:
            applying = g.GetNeighborIndices(location.x, location.y)
            neighbors = []
            for k in applying:
                if k.x < 0 or k.y < 0:
                    continue
                neighbors.append(field.get(k))
            count = 0
            for k in neighbors:
                if k == live:
                    count += 1
            if j == dead:
                if count == 3:
                    try:
                        field_tmp[location.x][location.y] = live
                    except IndexError:
                        pass
            else:
                if count < 2 or count > 4:
                    try:
                        field_tmp[location.x][location.y] = dead
                    except IndexError:
                        pass
            location.y += 1
        location.x += 1
        location.y = 0
    field.print('  ')
    print(iterator)
    if field_tmp == field.array:
        playsound('assets\hfail sad trumpet trombone sound.mp3')
        g.print_red('GAME OVER')
        print('''\033[1;32;49mStable configuration reached or all cells died.
To exit type exit and press enter. To continue press enter\033[1;30;49m''')
        ask = input().upper()
        if ask == 'EXIT':
            sleep(0.5)
            exit('Goodbye')
        else:
            continue
    field.array = field_tmp.copy()
    iterator += 1
