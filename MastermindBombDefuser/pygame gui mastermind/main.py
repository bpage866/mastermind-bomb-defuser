import pygame
import pygame_gui
import random
import pickle


from pygame_gui.core import ObjectID
pygame.init()


red = (252, 2, 7)
blue = (3, 48, 252)
white = (255, 253, 252)
yellow = (219, 252, 3)
black = (20, 20, 30)
green = (3, 252, 44)
def wire(x,y, colour, window_surface, buttoni):
    window_surface.blit(buttoni, (x,y))

def guessesShown(conversionList, window_surface):
    """pygame.draw.rect(window_surface, red, (256, 102, 20, 20))
    pygame.draw.rect(window_surface, red, (280, 102, 20, 20))
    pygame.draw.rect(window_surface, red, (304, 102, 20, 20))
    pygame.draw.rect(window_surface, red, (328, 102, 20, 20))
    pygame.draw.rect(window_surface, red, (328, 162, 20, 20))
    pygame.draw.rect(window_surface, red, (372, 102, 20, 20))"""
    posx = 256
    posy = 102
    count = 0
    for i in conversionList:
        if count % 3 == 0 and count != 0:
            posx = 256
            posy += 60
        elif count != 0:
            posx += 20
        for ii in i:
            pygame.draw.rect(window_surface, ii, (posx, posy, 20, 20))
            posx += 24
        count += 1
def hints(hintsList, window_surface):
    count = 0
    posxi = 328
    posyi = 90

    for i in hintsList:
        countii = 0

        for ii in i:

            pygame.draw.rect(window_surface, ii, (posxi, posyi, 8, 8))
            countii += 1
            if countii == 1:
                posxi +12
            if countii == 2:
                posxi -= 24
                posyi += 36
            if countii == 3:
                posxi += 0
            if countii == 4:
                posyi -= 36



            posxi += 12
        count += 1
        if count % 3 == 0 and count != 0:
            posxi = 328
            posyi += 60
        else:
            posxi += 92
    """pygame.draw.rect(window_surface, red, (328, 90, 8, 8)) #444
    pygame.draw.rect(window_surface, red, (340, 90, 8, 8))  # 444
    pygame.draw.rect(window_surface, red, (444, 90, 8, 8))  # 444
    pygame.draw.rect(window_surface, red, (328, 126, 8, 8))  # 444
    pygame.draw.rect(window_surface, red, (328, 150, 8, 8))"""  # 444




abl = 0
#hintsList  = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],]
#conversionList = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],]
def conversion(builds, comboguessed,correctcombolist, correctcombo, buildingsLost, hintsList, conversionList):
    hintdot = []
    hintwhite =[]
    hintred = []
    hintblack = []
    converted = []
    postion = 0
    postionw = 0
    postionr = 0

    for i in comboguessed[(builds)]:
        if i == "1":
            converted.append(red)
        if i == "2":
            converted.append(white)
        if i == "3":
            converted.append(blue)
        if i == "4":
            converted.append(yellow)
        if i == "5":
            converted.append(black)
        if i == "6":
            converted.append(green)
        if i == "7":
            converted.append((0,0,0))
        print("combo", comboguessed[(builds)], (builds))
        print(i)
        print(correctcombolist[postion][0])
        if i in correctcombo and i != correctcombolist[postion][0]:
            hintwhite.append(white)
            print("white printed at", postion)
        elif i in correctcombo and i == correctcombolist[postion][0]:
            hintred.append(red)
            print("printed at", postion)
        else:
            hintblack.append(black)
        postion += 1
    print(hintred + hintwhite)
    hintsList[builds] = (hintred + hintwhite + hintblack)
    conversionList[buildingsLost] = converted
    return hintsList, conversionList

def building(num, x, y, window_surface):

    if num == 0:
        window_surface.blit((pygame.image.load(
            "C:\\Users\\benmk\\OneDrive\Pictures\\mastermind project\\Building1.png").convert_alpha()), (x, y))
    elif (num < 10 or (num >= 30 and num < 40))  or ((num >= 60 and num < 70) or (num >= 90 and num < 100)):
        window_surface.blit((pygame.image.load(

            "C:\\Users\\benmk\\OneDrive\Pictures\\mastermind project\\Building2.png").convert_alpha()), (x, y))
    elif ((num >= 10 and num <= 20) or (num >= 40 and num < 50))  or ((num >= 70 and num < 80) or (num >= 100 and num < 110)):
        window_surface.blit((pygame.image.load(
            "C:\\Users\\benmk\\OneDrive\Pictures\\mastermind project\\Building3.png").convert_alpha()), (x, y))
    elif ((num >= 20 and num <= 30) or (num >= 50 and num < 60))  or ((num >= 80 and num < 90) or (num >= 110 and num < 120)):
        window_surface.blit((pygame.image.load(
            "C:\\Users\\benmk\\OneDrive\Pictures\\mastermind project\\Building4.png").convert_alpha()), (x, y))
    elif num >= 120:
        window_surface.blit((pygame.image.load(
            "C:\\Users\\benmk\\OneDrive\Pictures\\mastermind project\\Building5.png").convert_alpha()), (x, y))
    if num >= 1 and num < 130:
        num += 1

    return num

def live(livecount, window_surface):

    if livecount < 60:

        window_surface.blit((pygame.image.load(
            "C:\\Users\\benmk\\OneDrive\Pictures\\mastermind project\\LiveIcon.png").convert_alpha()), (22, 16))

    elif livecount > 60 and livecount < 120:

        livecount += 1

    elif livecount >= 120:


        livecount = 0
    livecount += 1
    return livecount












#lue = pygame_gui.UIManager((590, 320))
def drawManager():
    manager = pygame_gui.UIManager((590, 320))









def maingame(name, gamemode):
    manager = pygame_gui.UIManager((590, 320), "data.json")
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((590, 320))

    background = pygame.Surface((590, 320))
    background.fill(pygame.Color('#000000'))
    buttoni = pygame.image.load("C:\\Users\\benmk\\OneDrive\\Pictures\\mastermind project\\background.png").convert()
    clock = pygame.time.Clock()
    draw = True
    building1 = 0
    building2 = 0
    building3 = 0
    building4 = 0
    building5 = 0
    building6 = 0
    building7 = 0
    building8 = 0
    building9 = 0
    building10 = 0
    building11 = 0
    building12 = 0

    lostbuild = 0
    buildingsLost = 0
    comboguessed = []
    defusing = True
    game = True
    hintsList = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                 [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                 [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                 [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                 [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                 [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    conversionList = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                      [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                      [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                      [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                      [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                      [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    buidlinglist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    correctcombolist = []
    correctcombo = ""
    fulllen = False
    posn = 1
    while fulllen == False:

        number = str(random.randrange(1, 7))
        if not number in correctcombo:
            correctcombo += number
            correctcombolist.append([number, posn])
            posn += 1
        if len(correctcombo) == 4:
            fulllen = True
    exit = False
    building1 = 0
    building2 = 0
    building3 = 0
    building4 = 0
    building5 = 0
    building6 = 0
    building7 = 0
    building8 = 0
    building9 = 0
    building10 = 0
    building11 = 0
    building12 = 0
    font = pygame.font.Font("Pixel.ttf", 14)
    lostbuild = 0
    buildingsLost = 0
    comboguessed = []
    defusing = True
    game = True
    while game == True:

        if buildingsLost == 1:
            building1 = 1
        elif buildingsLost == 2:
            building2 = 1
        elif buildingsLost == 3:
            building3 = 1
        elif buildingsLost == 4:
            building4 = 1
        elif buildingsLost == 5:
            building5 = 1
        elif buildingsLost == 6:
            building6 = 1
        elif buildingsLost == 7:
            building7 = 1
        elif buildingsLost == 8:
            building8 = 1
        elif buildingsLost == 9:
            building9 = 1
        elif buildingsLost == 10:
            building10 = 1
        elif buildingsLost == 11:
            building11 = 1
        elif buildingsLost == 12:
            building12 = 1

        combo = ""
        print(correctcombo)
        print(comboguessed)
        livecount = 0

        redWirecut = False
        whiteWirecut = False
        blueWirecut = False
        yellowWirecut = False
        blackWirecut = False
        greenWirecut = False
        colourOrder = []
        order = 0
        col1 = (0, 0, 0)
        col2 = (0, 0, 0)
        col3 = (0, 0, 0)
        col4 = (0, 0, 0)
        colour = (0, 0, 0)


        if redWirecut == False:
            redWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((35, 125), (22, 170)),
                                                   text="", manager=manager,
                                                   object_id=ObjectID(class_id="@friendly_buttons",
                                                                      object_id="#red_button"))
        if whiteWirecut == False:
            whiteWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((67, 125), (22, 170)),
                                                     text='',
                                                     manager=manager,
                                                     object_id=ObjectID(class_id="@friendly_buttons",
                                                                        object_id="#white_button"))
        if blueWirecut == False:
            blueWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((99, 125), (22, 170)),
                                                    text='',
                                                    manager=manager,
                                                    object_id=ObjectID(class_id="@friendly_buttons",
                                                                       object_id="#blue_button"))

        if yellowWirecut == False:
            yellowWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((131, 125), (22, 170)),
                                                      text='',
                                                      manager=manager,
                                                      object_id=ObjectID(class_id="@friendly_buttons",
                                                                         object_id="#yellow_button"))
        if blackWirecut == False:
            blackWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((163, 125), (22, 170)),
                                                     text='',
                                                     manager=manager,
                                                     object_id=ObjectID(class_id="@friendly_buttons",
                                                                        object_id="#black_button"))

        if greenWirecut == False:
            greenWire = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((195, 125), (22, 170)),
                text='',
                manager=manager, object_id=ObjectID(class_id="@friendly_buttons", object_id="#green_button"))
        timei = gamemode * 60
        print(conversionList)
        while defusing:
            if buildingsLost != 12:
                time_delta = clock.tick(60) / 1000.0
                manager.update(time_delta)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        defusing = False
                        game = False
                        exit = True
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == redWire:
                            print("cut")
                            draw = False
                            redWirecut = True
                            order += 1
                            colour = red
                            combo += "1"
                        if event.ui_element == whiteWire:
                            print("white cut")
                            draw = False
                            whiteWirecut = True
                            order += 1
                            colour = white
                            combo += "2"
                        if event.ui_element == blueWire:
                            print("cut")
                            draw = False
                            blueWirecut = True
                            order += 1
                            colour = blue
                            combo += "3"
                        if event.ui_element == yellowWire:
                            print("white cut")
                            draw = False
                            yellowWirecut = True
                            order += 1
                            colour = yellow
                            combo += "4"
                        if event.ui_element == blackWire:
                            print("cut")
                            draw = False
                            blackWirecut = True
                            order += 1
                            colour = black
                            combo += "5"
                            print("black")
                        if event.ui_element == greenWire:
                            print("white cut")
                            draw = False
                            greenWirecut = True
                            order += 1
                            colour = green
                            combo += "6"

                    manager.process_events(event)
                if order == 4 or timei <= 0:
                    for i in range(4 - len(combo)):
                        combo += "7"
                    defusing = False
                    draw = False
                    redWirecut = True
                    blueWirecut = True
                    greenWirecut = True
                    whiteWirecut = True
                    blackWirecut = True
                    comboguessed.append(combo)
                    host = conversion(lostbuild, comboguessed, correctcombolist, correctcombo, buildingsLost, hintsList,
                                      conversionList)
                    hintsList = host[0]
                    conversionList = host[1]
                    combo = ""
                    order = 0



                    if correctcombo in comboguessed:
                        print("won")
                        game = False
                    else:
                        if (buildingsLost) == 12:
                            game = False
                            print("gameend")
                        else:
                            buildingsLost += 1
                            print("build", buildingsLost)
                        print(buildingsLost)
                        lostbuild += 1
                        redWirecut = True
                        whiteWirecut = True
                        blueWirecut = True
                        yellowWirecut = True
                        greenWirecut = True
                        blackWirecut = True

                        print("building", buildingsLost)
                        if buildingsLost == 12:
                            game = False

                window_surface.blit(background, (0, 0))
                if order == 1:
                    col1 = colour
                if order == 2:
                    col2 = colour
                if order == 3:
                    col3 = colour
                if order == 4:
                    col4 = colour

                if draw == True:

                    wire(0, 0, 0, window_surface, buttoni)
                    pygame.draw.rect(window_surface, col1, (28, 90, 24, 24))
                    pygame.draw.rect(window_surface, col2, (56, 90, 24, 24))
                    pygame.draw.rect(window_surface, col3, (84, 90, 24, 24))
                    pygame.draw.rect(window_surface, col4, (112, 90, 24, 24))
                    guessesShown(conversionList, window_surface)
                    hints(hintsList, window_surface)
                    building1 = building(building1, 28, 18, window_surface)
                    building2 = building(building2, 66, 18, window_surface)
                    building3 = building(building3, 104, 18, window_surface)
                    building4 = building(building4, 142, 18, window_surface)
                    building5 = building(building5, 180, 18, window_surface)
                    building6 = building(building6, 218, 18, window_surface)
                    building7 = building(building7, 256, 18, window_surface)
                    building8 = building(building8, 294, 18, window_surface)
                    building9 = building(building9, 332, 18, window_surface)
                    building10 = building(building10, 370, 18, window_surface)
                    building11 = building(building11, 408, 18, window_surface)
                    building12 = building(building12, 446, 18, window_surface)
                    manager.draw_ui(window_surface)

                    if redWirecut == True:
                        window_surface.blit((pygame.image.load(
                            "C:\\Users\\benmk\OneDrive\Pictures\\mastermind project\\redwirecut2.png").convert_alpha()),
                                            (36, 130))

                    if whiteWirecut == True:
                        window_surface.blit((pygame.image.load(
                            "C:\\Users\\benmk\OneDrive\Pictures\\mastermind project\\whitewirecut2.png").convert_alpha()),
                                            (70, 130))

                    if blueWirecut == True:
                        window_surface.blit((pygame.image.load(
                            "C:\\Users\\benmk\OneDrive\Pictures\\mastermind project\\bluewirecut2.png").convert_alpha()),
                                            (101, 130))

                    if yellowWirecut == True:
                        window_surface.blit((pygame.image.load(
                            "C:\\Users\\benmk\OneDrive\Pictures\\mastermind project\\yellowwirecut2.png").convert_alpha()),
                                            (132, 130))

                    if blackWirecut == True:
                        window_surface.blit((pygame.image.load(
                            "C:\\Users\\benmk\OneDrive\Pictures\\mastermind project\\blackwirecut2.png").convert_alpha()),
                                            (166, 130))

                    if greenWirecut == True:
                        window_surface.blit((pygame.image.load(
                            "C:\\Users\\benmk\OneDrive\Pictures\\mastermind project\\greenwirecut2.png").convert_alpha()),
                                            (194, 130))

                    livecount = live(livecount, window_surface)

                else:
                    manager = pygame_gui.UIManager((590, 320), "data.json")
                    if redWirecut == False:
                        redWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((35, 125), (22, 170)),
                                                               text="", manager=manager,
                                                               object_id=ObjectID(class_id="@friendly_buttons",
                                                                                  object_id="#red_button"))
                    if whiteWirecut == False:
                        whiteWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((67, 125), (22, 170)),
                                                                 text='',
                                                                 manager=manager,
                                                                 object_id=ObjectID(class_id="@friendly_buttons",
                                                                                    object_id="#white_button"))
                    if blueWirecut == False:
                        blueWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((99, 125), (22, 170)),
                                                                text='',
                                                                manager=manager,
                                                                object_id=ObjectID(class_id="@friendly_buttons",
                                                                                   object_id="#blue_button"))

                    if yellowWirecut == False:
                        yellowWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((131, 125), (22, 170)),
                                                                  text='',
                                                                  manager=manager,
                                                                  object_id=ObjectID(class_id="@friendly_buttons",
                                                                                     object_id="#yellow_button"))
                    if blackWirecut == False:
                        blackWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((163, 125), (22, 170)),
                                                                 text='',
                                                                 manager=manager,
                                                                 object_id=ObjectID(class_id="@friendly_buttons",
                                                                                    object_id="#black_button"))

                    if greenWirecut == False:
                        greenWire = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect((195, 125), (22, 170)),
                            text='',
                            manager=manager,
                            object_id=ObjectID(class_id="@friendly_buttons", object_id="#green_button"))

                    manager.draw_ui(window_surface)
                    wire(0, 0, 0, window_surface, buttoni)

                    draw = True
                    livecount = live(livecount, window_surface)
                    if buildingsLost == 12:
                        fulllen = True
                        game = False
                        defusing = False
                timei -= 1
                pygame.draw.rect(window_surface, (10, 100, 10), pygame.Rect(508, 20, 42, 22))
                window_surface.blit(font.render(str(round(timei/60 )), True, (50, 222, 50)), (522, 26))

            pygame.display.update()

        defusing = True

    with open("mast1.txt", "rb") as handle:
        data = handle.read()
    newd = pickle.loads(data)
    newd.append([name, buildingsLost])

    file = open("mast1.txt", "wb")
    pickle.dump(newd, file)
    file.close()
    with open("mast1.txt", "rb") as handle:
        data = handle.read()

    newnewd = pickle.loads(data)
    print(newnewd)
    if exit:
        return [True, buildingsLost]
    else:
        return [False, buildingsLost]

def intro():
    pygame.init()

    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((590, 320))

    background = pygame.Surface((590, 320))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((800, 600))
    ibackground = pygame.image.load("introbackground.png").convert()
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((440, 295), (120, 20)),
                                                text='next',
                                                manager=manager)

    clock = pygame.time.Clock()
    is_running = True
    font = pygame.font.Font("Pixel.ttf", 14)
    line1 = ["mission brief:", "you have been given a", "in the controller you", "for example the correct", "however they explode", ""]
    line2 = ["an evil mastermind has", "brand new military", "click on the wire you want", "combo is green, blue, red",
             "after a few seconds", ""]
    line3 = ["planted bombs in 12 ", "grade bomb defusing robot", "to cut. as part of the", "and yellow. in this first",
             "good luck", ""]
    line4 = ["different buildings in ", "that can be controlled", "controller it shows", "guess, they did white,",
             "", ""]
    line5 = ["the city. we have tracked", "by remote. You will need", "you what your current ",
             "green, red and black so", "", ""]
    line6 = ["down which buildings have", "will need to cut the wires", "combination is, and after",
             "they have a red marker to", "", ""]
    line7 = ["bombs in, and it's down to", "in the correct order, if", "failing it will show",
             "indicate correct colour in", "", ""]
    line8 = ["you to defuse the bombs.", "not the bomb will explode", "you your last colour",
             " the right spot, and white ", "", ""]
    line9 = ["", "destroying the building.", "combination.", "for correct colours.", "", ""]
    line10 = ["", "", "", "", "", ""]
    slide = 0
    images = ["tntslide.png", "robot.png", "intromain1.png", "intromain2.png", "blackint.png" , "blackint.png"]
    underscore = "_"
    count = 0

    while is_running:
        if count < 30:
            underscore = "_"
        elif count >= 60:

            count = 0
        elif count > 30:
            underscore = ""
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                return True
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:

                    slide += 1
                    print(slide)
                    if slide == 5:
                        print("has run")
                        is_running = False



            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(ibackground, (0, 0))

        window_surface.blit(font.render(line1[slide], True, (50, 222, 50)), (320, 30))
        window_surface.blit(font.render(line2[slide], True, (50, 222, 50)), (320, 55))
        window_surface.blit(font.render(line3[slide], True, (50, 222, 50)), (320, 80))
        window_surface.blit(font.render(line4[slide], True, (50, 222, 50)), (320, 105))
        window_surface.blit(font.render(line5[slide], True, (50, 222, 50)), (320, 130))
        window_surface.blit(font.render(line6[slide], True, (50, 222, 50)), (320, 155))
        window_surface.blit(font.render(line7[slide], True, (50, 222, 50)), (320, 180))
        window_surface.blit(font.render(line8[slide], True, (50, 222, 50)), (320, 205))
        window_surface.blit(font.render(line9[slide], True, (50, 222, 50)), (320, 230))
        window_surface.blit(font.render(underscore, True, (50, 222, 50)), (320, 255))
        window_surface.blit(pygame.image.load(images[slide]).convert_alpha(), (18, 28))

        manager.draw_ui(window_surface)

        pygame.display.update()
        count += 1



def endscreen(buildingsLost, name):




    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((590, 320))

    background = pygame.Surface((590, 320))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((590, 320))

    e_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 150), (150, 60)),
                                            text='Play again?',
                                            manager=manager)
    h_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 220), (150, 60)),
                                            text='Main menu',
                                            manager=manager)
    ibackground = pygame.image.load("endscreen.png").convert()
    clock = pygame.time.Clock()
    is_running = True
    font = pygame.font.Font("Pixel.ttf", 48)
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                return True

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == e_button:
                    is_running = False
                    thegame(name)
                if event.ui_element == h_button:
                    is_running = False
            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        window_surface.blit(ibackground, (0, 0))
        if buildingsLost >= 12:
            window_surface.blit(font.render("Mission failed", True, (222, 222, 255)), (95, 30))
            window_surface.blit(font.render("all buildings lost", True, (222, 222, 255)), (50, 90))
        else:
            window_surface.blit(font.render("Mission success", True, (222, 222, 255)), (40, 30))
            window_surface.blit(font.render(str(buildingsLost) + " buidlings lost", True, (222, 222, 255)), (65, 90))
        manager.draw_ui(window_surface)


        pygame.display.update()

def leaderboard(name,abl):

    pygame.init()

    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((590, 320))

    background = pygame.Surface((590, 320))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((590, 320))

    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((508, 16), (66, 28)),
                                            text='Exit',
                                            manager=manager)

    ibackground = pygame.image.load("board.png").convert()
    clock = pygame.time.Clock()
    is_running = True
    font = pygame.font.Font("Pixel.ttf", 26)
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    is_running = False

            manager.process_events(event)

        manager.update(time_delta)
        buildingsLost = 1
        window_surface.blit(background, (0, 0))
        window_surface.blit(ibackground, (0, 0))
        with open("mast1.txt", "rb") as handle:
            data = handle.read()
        newdd = pickle.loads(data)
        scorelst = [""]

        posx = 30
        posy = 60
        for i in range(12):
            score = 14

            currentii = ""
            for ii in newdd:

                if ii[1] < score:
                    score = ii[1]
                    currentii = ii

            if ii[1] == 13:
                currentii[1] = 0

            window_surface.blit(font.render((str(i + 1)+ " " + str(currentii[0]) + " " + str(currentii[1])), True, (0, 182, 0)), (posx, posy))
            if (i + 1)  % 2 == 0:
                posx = 30
                posy += 40
            else:
                posx += 270

            newdd.remove(currentii)

        window_surface.blit(font.render(("Leader board"), True, (0, 182, 0)),
                            (30, 20))
        manager.draw_ui(window_surface)

        pygame.display.update()
def settings():

    pygame.init()
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((590, 320))

    background = pygame.Surface((590, 320))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((590, 320))
    gamemode = 1
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((508, 16), (66, 28)),
                                            text='Exit',
                                            manager=manager)
    left_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((180, 60), (66, 28)),
                                               text='<',
                                               manager=manager)
    right_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 60), (66, 28)),
                                               text='>',
                                               manager=manager)
    intro_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 160), (100,100)),
                                               text='',
                                               manager=manager)
    skipintro = True
    gamemodes = ["easy", "normal", "hard"]
    ibackground = pygame.image.load("board.png").convert()
    clock = pygame.time.Clock()
    is_running = True
    fonts = pygame.font.Font("Pixel.ttf", 22)
    font = pygame.font.Font("Pixel.ttf", 26)
    fontb = pygame.font.Font("Pixel.ttf", 48)
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    is_running = False
                if event.ui_element == right_button:
                    gamemode += 1
                    if gamemode >= 3:
                        gamemode = 0
                if event.ui_element == left_button:
                    gamemode -= 1
                    if gamemode < 0:
                        gamemode = 2
                if event.ui_element == intro_button:

                    if skipintro:
                        skipintro = False
                    else:
                        skipintro = True


            manager.process_events(event)

        manager.update(time_delta)
        buildingsLost = 1
        window_surface.blit(background, (0, 0))
        window_surface.blit(ibackground, (0, 0))




        window_surface.blit(font.render(("settings"), True, (0, 182, 0)),
                            (30, 20))
        window_surface.blit(fontb.render((gamemodes[gamemode]), True, (0, 182, 0)),
                            (270, 50))
        window_surface.blit(fontb.render(("skip intro"), True, (0, 182, 0)),
                            (80, 180))
        window_surface.blit(fonts.render(("Difficulty "), True, (0, 182, 0)),
                            (30, 60))
        manager.draw_ui(window_surface)
        if skipintro:
            pygame.draw.rect(window_surface, (20, 20, 30), pygame.Rect(410, 170, 80, 80))
        else:

            pygame.draw.rect(window_surface, (10, 100, 10), pygame.Rect(410, 170, 80, 80))

        pygame.display.update()
    if gamemode == 0:
        gamemode = 20
    elif gamemode == 1:
        gamemode = 15
    else:
        gamemode = 10
    return [skipintro, gamemode]


def mainMenu(name):
    pygame.init()
    manager = pygame_gui.UIManager((590, 320), "data.json")
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((590, 320))

    background = pygame.Surface((590, 320))
    background.fill(pygame.Color('#000000'))
    redWirecut = 0
    yellowWirecut = 0
    greenWirecut = 0

    if redWirecut == 0:
        redWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-50, 180), (690, 30)),
                                               text="Start", manager=manager,
                                               object_id=ObjectID(class_id="@friendly_buttons",
                                                                  object_id="#red_button"))
    if greenWirecut == 0:
        greenWire = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((-50, 220), (690, 30)),
            text='Leaderboard',
            manager=manager, object_id=ObjectID(class_id="@friendly_buttons", object_id="#green_button"))
    if yellowWirecut == 0:
        yellowWire = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-50, 260), (690, 30)),
                                                  text='Settings',
                                                  manager=manager,
                                                  object_id=ObjectID(class_id="@friendly_buttons",
                                                                     object_id="#yellow_button"))

    explosion = 0
    ibackground = pygame.image.load("homescreen1.png").convert()
    clock = pygame.time.Clock()
    is_running = True
    opt1 = False
    opt2 = False
    opt3 = False
    font = pygame.font.Font("Pixel.ttf", 36)
    fonts = pygame.font.Font("Pixel.ttf", 24)
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                name = "false"

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == redWire:
                    if explosion == 0:
                        opt1 = True
                    if len(name) < 12:
                        explosion = 1

                if event.ui_element == greenWire:
                    if explosion == 0:
                        print("h")
                        opt2 = True
                    if len(name) < 12:
                        explosion = 1
                if event.ui_element == yellowWire:
                    if explosion == 0:
                        opt3 = True
                    if len(name) < 12:
                        explosion = 1
            if event.type == pygame.KEYDOWN:
                if len(name) >= 12:
                    name = ""
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name[:-1]
                elif len(name) <= 10:
                    name += event.unicode
            manager.process_events(event)

        manager.update(time_delta)
        buildingsLost = 1
        window_surface.blit(background, (0, 0))
        window_surface.blit(ibackground, (0, 0))
        window_surface.blit(pygame.image.load("homescreenext.png").convert(), (590 / 4, 10))

        window_surface.blit(fonts.render((":" + name), True, (0, 182, 0)), (165, 130))
        window_surface.blit(font.render("Mastermind", True, (0, 182, 0)), (160, 30))
        window_surface.blit(fonts.render("Bomb Defuser ", True, (0, 182, 0)), (210, 75))
        manager.draw_ui(window_surface)
        if (explosion >= 1 and explosion < 10) or (explosion >= 30 and explosion < 40):
            window_surface.blit(pygame.image.load("homescreen2.png").convert(), (0, 0))
            explosion += 1
        elif (explosion >= 10 and explosion < 20) or (explosion >= 40 and explosion < 50):
            window_surface.blit(pygame.image.load("homescreen3.png").convert(), (0, 0))
            explosion += 1
        elif (explosion >= 20 and explosion < 30) or (explosion >= 50 and explosion < 60):
            window_surface.blit(pygame.image.load("homescreen4.png").convert(), (0, 0))
            explosion += 1
        elif explosion == 60:
            is_running = False
        pygame.display.update()
    if opt1:
        exit = thegame(name)
    else:
        exit = False
    if opt2:
        leaderboard("i", 1)
    if opt3:
        settins = settings()
    else:
        settins = [skipintro, gamemode]
    print([name, settins[0], settins[1]])
    if exit == True:
        name = "false"
    return [name, settins[0], settins[1]]


def thegame(name):
    if skipintro:
        exit = intro()
    else:
        exit = False
    if not exit:
        abl = maingame(name, gamemode)
        exit = abl[0]
        abl = abl[1]
        print(abl)



    if not exit:
        exit = endscreen(abl, name)
    if  exit == True:
        return True
    else:
        return False
name = "type your name"
skipintro = True
gamemode = 15
exitloop = True
while exitloop:
    info = mainMenu(name)
    name = info[0]
    skipintro = info[1]
    gamemode = info[2]
    if name == "false":
        exitloop = False

































