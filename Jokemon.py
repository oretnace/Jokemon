#Jokemon main program

#JKMN DATA DICTIONARIES====================================================

#art = 34x9
#info = 34x5
#name = 12 chars
#type = 7 chars
#hp = 2 chars
#move: name = 16 chars, info = 32x2, value
bowlbasaur = {"art":("                 (                ",
                     "              )    )              ",
                     '           _.(--"("""--.._        ',
                     "          /, _..-----).._,\       ",
                     "     /'----'\\'''-----'''`  |      ",
                     "    { 0    0 }            /.      ",
                     "     '-.::.-':,         .'|       ",
                     "          ;  ;--.....--' /        ",                     
                     "          \__\\nnn/ \_\\nnn7        "),
              "info":("The bowl on its back can carry all",
                      "kinds of soup that the hungry uni ",
                      "student eats. Not only can it     ",
                      "carry soup, but it can also carry ",
                      "cereal, noodles, blood and more.  "),
              "name":("BOWLBASAUR  "),
              "type":"PLATE  ",
              "my_hp": 80,
              "foe_hp": 80,
              "hp":"80",
              "move":(("RAZOR PLATE] ",
                       ("Standard PLATE attack, the user ",
                        "attacks with its sharp edges.   "),
                       " [ATTACK]"),
                      ("BOWL-OUT]    ",
                       ("PLATE attack, gets stronger each",
                        "consecutive use, 5th is max.    "),
                       " [ATTACK]"),
                      ("REFILL]      ",
                       ("Special move, bowl is refilled  ",
                        "with food to heal some HP.      "),
                       "[SPECIAL]"))}

starmander = {"art":("                                  ",
                     "                       )/_        ",
                     '    !      _\)        /           ',
                     '   -+-       L_.--..-"-,--@.,     ',
                     "    '\      .'         ._@_/      ",
                     "      \  _.+  _  \.-\_\           ",
                     "       ''-_.-' ) /     \_         ",
                     "               `/_     (\         ",                     
                     "               ')                 "),
              "info":("Starmander likes to stretch its   ",
                      "limbs out wide to look like a     ",
                      "star. It's not working very well  ",
                      "though. Stop it Starmander. You're",
                      "embarassing yourself. Go home.    "),
              "name":("STARMANDER  "),
              "type":("ALIEN  "),
              "my_hp": 80,
              "foe_hp": 80,
              "hp":"80",
              "move":(("COSMIC BEAM] ",
                       ("Standard ALIEN attack, shoots a ",
                        "beam fuelled by an alien energy."),
                       " [ATTACK]"),
                      ("PLANE SHIFT] ",
                       ("Special move, swaps the user's  ",
                        "HP with the foe's.              "),
                       "[SPECIAL]"),
                      ("LOBOTOMY]    ",
                       ("ALIEN attack, weak but breaks   ",
                        "foe's connected moves.          "),
                       " [ATTACK]"))}

qwertle = {"art":("                                  ",
                  "          ___________________     ",
                  '   ___   |Q|W|E|R|T|Y|U|I|O|P|    ',
                  '  /o  \__||A|S|D|F|G|H|J|K|L||    ',
                  "  '==--_/|||Z|X|C|V|B|N|M|||||    ",
                  "        \|_|_||_________|_|_||    ",
                  "          / /             \ \     ",
                  "         |,,|             |,,|    ",
                  "                                  "),
           "info":("That's right. Qwertle is a turtle ",
                   "with a QWERTY keyboard for a      ",
                   "shell. Qwertle will die if its    ",
                   "shell touches liquids like water  ",
                   "or tea. Qwertle likes to swim.    "),
           "name":("QWERTLE     "),
           "type":("MACHINE"),
           "my_hp": 80,
           "foe_hp": 80,
           "hp":"80",
           "move":(("BUTTON MASH]  ",
                    ("Standard MACHINE attack, beats  ",
                     "foe up in a key mashing motion. "),
                    " [ATTACK]"),
                    ("ANTI-VIRUS]  ",
                    ("Special move, halves damage     ",
                     "taken from next 5 moves.        "),
                    "[SPECIAL]"),
                    ("DISCHARGE]   ",
                    ("MACHINE attack, higher damage if",
                     "user's HP is lower.             "),
                    " [ATTACK]"))}

#FUNCTIONS================================================================

def print_screen(screen_list):
    """Prints screen list."""
    for line in screen_list:
        print(line)

def write_line(screen_list, start_line, old_string, new_string):
    """For overwriting first instance of a string in one line only."""
    #preserving old copy of chosen screen
    current_screen = screen_list[:]
    #choose line you want to change
    current_line = start_line
    #copies old list up to chosen line in new list
    new_screen = current_screen[:current_line]
    #gets old line
    old_line = current_screen[current_line]
    #replaced by new string
    new_screen.append(old_line.replace(old_string, new_string, 1))
    #connects unchanged lines after it
    current_screen = new_screen + current_screen[(current_line + 1):]
    return current_screen

def write_box(screen_list, start_line, old_string, new_section):
    """Overwrites a box in a screen list with a sequence"""
    #old copy of chosen screen preserved
    current_screen = screen_list[:]
    #choose first line you want to change
    current_line = start_line
    #copies old list up to chosen line in new list
    new_screen = current_screen[:current_line]
    #loops same times as number of lines in new_section
    for line in range(len(new_section)):
        #gets old_line
        old_line = current_screen[current_line]
        #replaces chosen string with corresponding line in new_section
        #string added to new list
        new_screen.append(old_line.replace(old_string, new_section[line]))
        #moves on to next line
        current_line += 1
    #connects unchanged lines after it
    current_screen = new_screen + current_screen[current_line:]
    return current_screen  

def choose_jkmn(art, info, name, _type):
    """User chooses Jokemon."""
    #choose jokemon, loops until jokemon is chosen
    #bowlbasaur is first jokemon shown by default
    reply = "1"
    while "4" not in reply:
        if len(reply) > 1:
            #sound plays if input is more than 1 number, forces to put 1 number only
            print("\a")
            mode = ""
        elif "1" in reply:
            x = bowlbasaur
        elif "2" in reply:
            x = starmander
        elif "3" in reply:
            x = qwertle
        else:
            #sound plays if input is unrecognisable
            print("\a")
        #screen updates
        current_screen = write_box(choose_screen, 7, art, x["art"])
        current_screen = write_box(current_screen, 11, info, x["info"])
        current_screen = write_line(current_screen, 7, name, x["name"])
        current_screen = write_line(current_screen, 9, _type, x["type"])
        print_screen(current_screen)
        reply = input("What would you like to do? >")
    if "4" in reply:
        my_jkmn = x
        return my_jkmn

#SETUP======================================================================

def tutorial():
    """Runs tutorial screens."""
    print_screen(tutorial1)
    input(">(ENTER): The Battle Screen ")
    print_screen(tutorial2)
    input(">(ENTER): The JKMN Screen ")
    print_screen(tutorial3)
    input(">(ENTER): Back to the Title Screen")

def foe_choose_jkmn():
    x = random.randint(1, 3)
    if x == 1:
        y = bowlbasaur
    elif x == 2:
        y = starmander
    elif x == 3:
        y = qwertle
    foe_jkmn = y
    return foe_jkmn

#replaceable strings in brackets to write over them
def battle_intro(art, name, _type, h0, h1, move_name):
    """Sets up and returns main battle screen."""
    #user sends out jkmn
    current_screen = write_box(battle_intro1, 10, art, my_jkmn["art"])
    current_screen = write_line(current_screen, 12, name, my_jkmn["name"])
    #to put exclamation point next to name
    temp_name = my_jkmn["name"].replace(" ", "!", 1)
    current_screen = write_line(current_screen, 21, name, temp_name)
    current_screen = write_line(current_screen, 17,_type, my_jkmn["type"])
    current_screen = write_line(current_screen, 14, h0, str(my_jkmn["my_hp"]))
    current_screen = write_line(current_screen, 14, h1, my_jkmn["hp"])
    print_screen(current_screen)
    input(">(ENTER) ")

    #foe sends out their jkmn
    #for foe, then user's jkmn
    current_screen = battle_main[:10] + current_screen[10:21]
    #'foe sent out...'
    current_screen.append(main_screens[151])
    #blank remaining
    current_screen += battle_main[22:]
    #overwrite for foe
    current_screen = write_box(current_screen, 1, art, foe_jkmn["art"])
    current_screen = write_line(current_screen, 3, name, foe_jkmn["name"])
    #to put exclamation point next to name
    temp_name = foe_jkmn["name"].replace(" ", "!", 1)
    current_screen = write_line(current_screen, 21, name, temp_name)
    current_screen = write_line(current_screen, 8,_type, foe_jkmn["type"])
    current_screen = write_line(current_screen, 5, h0, str(foe_jkmn["foe_hp"]))
    current_screen = write_line(current_screen, 5, h1, foe_jkmn["hp"])
    print_screen(current_screen)
    input(">(ENTER) ")

    #put 3 moves in screen
    main_battle = current_screen[:21]
    main_battle.append(battle_main[21])
    main_battle += battle_main[22:]
    #3 moves
    move = 0
    for i in range(3):
        main_battle = write_line(main_battle, 21, move_name,  my_jkmn["move"][move][0])
        #next move
        move += 1
    return main_battle

#replaceable strings in brackets to overwrite them
def jkmn_info_setup(art, info, move_name, move_info, move_type):
    """Sets up and returns JKMN info screen."""
    #set up jkmn info screen
    jkmn_info = write_box(jkmn_screen, 3, art, my_jkmn["art"])
    jkmn_info = write_box(jkmn_info, 13, info, my_jkmn["info"])
    #writing 3 moves name, info and type
    line1 = 3
    line2 = 5
    move = 0
    for i in range(3):
        jkmn_info = write_line(jkmn_info, line1, move_name,  my_jkmn["move"][move][0])
        jkmn_info = write_box(jkmn_info, line2, move_info,  my_jkmn["move"][move][1])
        jkmn_info = write_line(jkmn_info, line1, move_type,  my_jkmn["move"][move][2])
        #move to next box and move
        line1 += 5
        line2 += 5
        move += 1
    return jkmn_info


#BATTLE STEPS=======================================================================

#"my" or "foe" is string
def jkmn_used(current_screen, my_or_foe):
    """Your/Foe JKMN used... message."""
    if "my" in my_or_foe:
        #get current screen and 'your jkmn used ...'
        current_screen = current_screen[:21]
        current_screen.append(battle_msg[0])
        current_screen.append(battle_msg[2])
        current_screen.append(main_screens[24])
        #overwrite 'your jkmn'
        current_screen = write_line(current_screen, 21, name, my_jkmn["name"])
        #used... then replace ] with !
        temp_move = my_move[0].replace("]", "!")
        current_screen = write_line(current_screen, 22, move_name, temp_move)
        print_screen(current_screen)
        input(">(ENTER) ")
        return current_screen
    elif "foe" in my_or_foe:
        #get current screen and 'your jkmn used ...'
        current_screen = current_screen[:21]
        current_screen.append(battle_msg[1])
        current_screen.append(battle_msg[2])
        current_screen.append(main_screens[24])
        #overwrite 'jkmn'
        current_screen = write_line(current_screen, 21, name, foe_jkmn["name"])
        #used... then replace ] with !
        temp_move = foe_move[0].replace("]", "!")
        current_screen = write_line(current_screen, 22, move_name, temp_move)
        print_screen(current_screen)
        input(">(ENTER) ")
        return current_screen

#attacker, defender is dictionary
def type_check(attacker, defender):
    """Checks type of attacker, returns string indicating if dmg is in/decreased/same."""
    effect = ""
    if ("ALIEN" in attacker["type"]) and ("MACHINE" in defender["type"]):
        effect = "yes"
    elif ("MACHINE" in attacker["type"]) and ("ALIEN" in defender["type"]):
        effect = "no"
    elif ("MACHINE" in attacker["type"]) and ("PLATE" in defender["type"]):
        effect = "yes"
    elif ("PLATE" in attacker["type"]) and ("MACHINE" in defender["type"]):
        effect = "no"
    elif ("PLATE" in attacker["type"]) and ("ALIEN" in defender["type"]):
        effect = "yes"
    elif ("ALIEN" in attacker["type"]) and ("PLATE" in defender["type"]):
        effect = "no"
    else:
        effect = "same"
    return effect

#defender is "my" or "foe" string
def deal_dmg(dmg, effect, defender):
    """Calculates then applies dmg to be dealt to defender."""
    #super effective
    if "yes" in effect:
        dmg = int(dmg * 1.5)
    #not very effective
    elif "no" in effect:
        dmg = int(dmg * 0.7)
    #neutral
    elif "same" in effect:
        dmg *= 1
    if "foe" in defender:
        #if foe qwertle has antivirus activated
        if (foe_jkmn == qwertle) and (len(foe_track)>0):
            print("foe qwertle's antivirus halves damage")
            dmg = int(dmg / 2)
        foe_jkmn["foe_hp"] -= dmg
    elif "my" in defender:
        if (my_jkmn == qwertle) and (len(my_track)>0):
            print("your qwertle's antivirus halves damage")
            dmg = int(dmg / 2)
        my_jkmn["my_hp"] -= dmg

#which_jkmn is "my" or "foe" string
def hp_update(current_screen, which_jkmn):
    """Updates HP bar for chosen JKMN, which_jkmn is string, my or foe."""
    left = "="
    gone = " "
    new_bar = ""
    #remaining hp (int)
    if "my" in which_jkmn:
        h0 = my_jkmn["my_hp"]
    elif "foe" in which_jkmn:
        h0 = foe_jkmn["foe_hp"]
    #make sure hp doesn't go below 0
    if h0 < 0:
        h0 = 0
    #converts it to string
    new_hp = str(h0)
    #makes sure number is still double digit so doesnt distort screen
    if h0 in range(0,9):
        new_hp = "0" + new_hp
    #no bar at 0, bar for 1-4, 5-8...
    for i in range(1, 80, 4):
        if i <= h0:
            new_bar += left
        else:
            new_bar += gone
    if "my" in which_jkmn:
        #slice of jkmn's hp bar, replaced with new hp_bar
        old_bar = (current_screen[15][48:68])
        current_screen = write_line(current_screen, 15, old_bar, new_bar)
        #old hp to be replaced
        old_hp = (current_screen[14][51:53])
        current_screen = write_line(current_screen, 14, old_hp, new_hp)
        return current_screen
    elif "foe" in which_jkmn:
        #slice of jkmn's hp bar, replaced with new hp_bar
        old_bar = (current_screen[6][10:30])
        current_screen = write_line(current_screen, 6, old_bar, new_bar)
        #old hp to be replaced
        old_hp = (current_screen[5][13:15])
        current_screen = write_line(current_screen, 5, old_hp, new_hp)
        return current_screen

def is_it_effective(current_screen, effect):
    """Takes value from effect, prints appropriate message."""
    #super effective
    if "yes" in effect:
        current_screen = current_screen[:21]
        current_screen.append(battle_msg[3])
        current_screen += battle_main[22:]
        print_screen(current_screen)
        input(">(ENTER) ")
        #not very effective
    elif "no" in effect:
        current_screen = current_screen[:21]
        current_screen.append(battle_msg[4])
        current_screen += battle_main[22:]
        print_screen(current_screen)
        input(">(ENTER) ")
        
#MOVES========================================================================
#attacker, defender is "my" or "foe" strings
def move_1(current_screen, attacker, defender, which_track):
    "Screen updates for standard moves."
    #your jkmn used...
    if "my" in attacker:
        current_screen = jkmn_used(current_screen, attacker)
        #random damage
        dmg = random.randint(9, 12)
        #efectiveness check
        effect = type_check(my_jkmn, foe_jkmn)
        #deal damage
        deal_dmg(dmg, effect, "foe")
        #print update hp
        current_screen = hp_update(current_screen, "foe")
        print_screen(current_screen)
        input(">(ENTER) ")
        #effectiveness check
        is_it_effective(current_screen, effect)
        #clears streak if attacker is bowlbsaur [CAREFUL IF FOE IS SAME JKMN]
        if my_jkmn == bowlbasaur:
            which_track = ""
        
    #foe jkmn used...
    elif "foe" in attacker:
        current_screen = jkmn_used(current_screen, attacker)
        #random damage
        dmg = random.randint(9, 12)
        #efectiveness check
        effect = type_check(foe_jkmn, my_jkmn)
        #deal damage
        deal_dmg(dmg, effect, "my")
        #print update hp
        current_screen = hp_update(current_screen, "my")
        print_screen(current_screen)
        input(">(ENTER) ")
        #effectiveness check
        is_it_effective(current_screen, effect)
        #clears streak if attacker is bowlbsaur [CAREFUL IF FOE IS SAME JKMN]
        if foe_jkmn == bowlbasaur:
            which_track = ""

    return current_screen, which_track

def move_2(current_screen, attacker, defender, which_track):
    """Checks who attacker is, runs corresponding move."""
    if "my" in attacker:
        current_screen = jkmn_used(current_screen, attacker)
        if my_jkmn == bowlbasaur:
            #bowlout
            #first check if my_track is exactly 5
            if which_track == "5":
                dmg = 33
            #the shorter the string, the more power, end number indicates number of times used
            elif len(which_track) > 0 :
                if which_track == "54":
                    dmg = 25
                elif which_track == "543":
                    dmg = 18
                elif which_track == "5432":
                    dmg = 12
            #if wasnt used last turn
            else:
                dmg = 7
                which_track = "54321"

            #efectiveness check
            effect = type_check(my_jkmn, foe_jkmn)
            #deal damage
            deal_dmg(dmg, effect, "foe")
            #print update hp
            current_screen = hp_update(current_screen, "foe")
            print_screen(current_screen)
            input(">(ENTER) ")
            #effectiveness check
            is_it_effective(current_screen, effect)

            #if maximum
            if which_track == "5":
                which_track = "5."
        elif my_jkmn == starmander:
            #get old remaining hps of jkmn
            my_old_hp = my_jkmn["my_hp"]
            foe_old_hp = foe_jkmn["foe_hp"]
            #switch
            my_jkmn["my_hp"] = foe_old_hp
            foe_jkmn["foe_hp"] = my_old_hp
            #update on screen
            current_screen = hp_update(current_screen, "my")
            current_screen = hp_update(current_screen, "foe")
            #message
            current_screen = current_screen[:21]
            current_screen.append(battle_msg[9])
            current_screen += battle_main[22:]
            print_screen(current_screen)
            input(">(ENTER) ")
        elif my_jkmn == qwertle:
            #check if already in use
            if len(which_track) > 0:
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[12])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
            else:
                which_track = "12345"
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[11])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")

    elif "foe" in attacker:
        current_screen = jkmn_used(current_screen, "foe")
        if foe_jkmn == bowlbasaur:
            print("foe bowlbasaur does move 2")
            #bowlout
            #first check if my_track is exactly 5
            if which_track == "5":
                dmg = 33
            #the shorter the string, the more power, end number indicates number of times used
            elif len(which_track) > 0 :
                if which_track == "54":
                    dmg = 25
                elif which_track == "543":
                    dmg = 18
                elif which_track == "5432":
                    dmg = 12
            #if wasnt used last turn
            else:
                dmg = 7
                which_track = "54321"

            #efectiveness check
            effect = type_check(foe_jkmn, my_jkmn)
            #deal damage
            deal_dmg(dmg, effect, "my")
            #print update hp
            current_screen = hp_update(current_screen, "my")
            print_screen(current_screen)
            input(">(ENTER) ")
            #effectiveness check
            is_it_effective(current_screen, effect)

            #if maximum
            if which_track == "5":
                which_track = "5."
        elif foe_jkmn == starmander:
            print("foe starmander does move 2")
            #get old remaining hps of jkmn
            my_old_hp = my_jkmn["my_hp"]
            foe_old_hp = foe_jkmn["foe_hp"]
            #switch
            my_jkmn["my_hp"] = foe_old_hp
            foe_jkmn["foe_hp"] = my_old_hp
            #update on screen
            current_screen = hp_update(current_screen, "my")
            current_screen = hp_update(current_screen, "foe")
            #message
            current_screen = current_screen[:21]
            current_screen.append(battle_msg[9])
            current_screen += battle_main[22:]
            print_screen(current_screen)
            input(">(ENTER) ")
        elif foe_jkmn == qwertle:
            print("foe qwertle does move 2")
            if len(which_track) > 0:
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[12])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
            else:
                #foe track needs six elements as it is going second
                which_track = "123456"
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[11])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
    
    return current_screen, which_track

def move_3(current_screen, attacker, defender, which_track):
    """Checks who attacker is, runs corresponding move."""
    if "my" in attacker:
        current_screen = jkmn_used(current_screen, attacker)
        if my_jkmn == bowlbasaur:
            #if already full
            if my_jkmn["my_hp"] == int(my_jkmn["hp"]):
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[7])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
            #if not full
            else:
                heal = random.randint(16, 22)
                my_jkmn["my_hp"] += heal
                #make sure it doesn't go over 80
                if my_jkmn["my_hp"] > 80:
                    my_jkmn["my_hp"] = 80
                current_screen = hp_update(current_screen, "my")
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[8])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
            #clears streak if attacker is bowlbsaur [CAREFUL IF FOE IS SAME JKMN]
            which_track = ""
        elif my_jkmn == starmander:
            #check types
            effect = type_check(my_jkmn, foe_jkmn)
            #deal damage
            deal_dmg(9, effect, "foe")
            #print update hp
            current_screen = hp_update(current_screen, "foe")
            print_screen(current_screen)
            input(">(ENTER) ")
            #effectiveness check
            is_it_effective(current_screen, effect)
            #starmander cleared...
            current_screen = current_screen[:21]
            current_screen.append(battle_msg[10])
            current_screen += battle_main[22:]
            print_screen(current_screen)
            input(">(ENTER) ")
            which_track = "lobotomy"
        elif my_jkmn == qwertle:
            #0.8 of hp difference + 3
            dmg = int(((80 - my_jkmn["my_hp"])*0.8)+3)
            #check types
            effect = type_check(my_jkmn, foe_jkmn)
            #deal dmg
            deal_dmg(dmg, effect, "foe")
            #update hp
            current_screen = hp_update(current_screen, "foe")
            #is it effective?
            is_it_effective(current_screen, effect)

    elif "foe" in attacker:
        current_screen = jkmn_used(current_screen, "foe")
        if foe_jkmn == bowlbasaur:
            print("foe bowlbasaur does move 3")
            #if already full
            if foe_jkmn["foe_hp"] == int(foe_jkmn["hp"]):
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[7])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
            #if not full
            else:
                heal = random.randint(16, 22)
                foe_jkmn["foe_hp"] += heal
                #make sure it doesn't go over 80
                if foe_jkmn["foe_hp"] > 80:
                    foe_jkmn["foe_hp"] = 80
                current_screen = hp_update(current_screen, "foe")
                current_screen = current_screen[:21]
                current_screen.append(battle_msg[8])
                current_screen += battle_main[22:]
                print_screen(current_screen)
                input(">(ENTER) ")
            #clears streak if attacker is bowlbsaur [CAREFUL IF FOE IS SAME JKMN]
            which_track = ""
        elif foe_jkmn == starmander:
            #check types
            effect = type_check(foe_jkmn, my_jkmn)
            #deal damage
            deal_dmg(9, effect, "my")
            #print update hp
            current_screen = hp_update(current_screen, "my")
            print_screen(current_screen)
            input(">(ENTER) ")
            #effectiveness check
            is_it_effective(current_screen, effect)
            #starmander cleared...
            current_screen = current_screen[:21]
            current_screen.append(battle_msg[10])
            current_screen += battle_main[22:]
            print_screen(current_screen)
            input(">(ENTER) ")
            which_track = "lobotomy"
        elif foe_jkmn == qwertle:
            #0.8 of hp difference + 3
            dmg = int(((80 - foe_jkmn["foe_hp"])*0.8)+3)
            #check types
            effect = type_check(foe_jkmn, my_jkmn)
            #deal dmg
            deal_dmg(dmg, effect, "my")
            #update hp
            current_screen = hp_update(current_screen, "my")
            #is it effective?
            is_it_effective(current_screen, effect)
            
    return current_screen, which_track

#IDENTIFY MOVE=======================================================================

#attacker, defender is "my" or "foe" string
def run_move(move, current_screen, attacker, defender, which_track):
    """Looks at move, returns the function of move ID and tracker."""
    #move 1
    if "1" in move:
        current_screen, which_track = move_1(current_screen, attacker, defender, which_track)
    #move 2
    elif "2" in move:
        current_screen, which_track = move_2(current_screen, attacker, defender, which_track)
    #move 3
    elif "3" in move:
        current_screen, which_track = move_3(current_screen, attacker, defender, which_track)
    return current_screen, which_track

#MAIN PROGRAM==============================================================

#TRY LOADING FILES=========================================================

#just in case files can't be found
try:
    #reads main screens text file, puts in list old list
    open_screens = open("jkmn screens.txt", "r").readlines()
    #new list
    main_screens = []
    #appends first 79 chars of every line in old list to new list
    for line in range((len(open_screens))):
        main_screens.append(open_screens[line][:79])
except:
    input("""Sorry, an important file can't be found for this program.
(press enter)""")
else:
#==========================================================================

    #main program

    #new list per screen
    title = main_screens[1:25]
    tutorial1 = main_screens[26:50]
    tutorial2 = main_screens[51:75]
    tutorial3 = main_screens[76:100]
    choose_screen = main_screens[101:125]
    battle_intro1 = main_screens[126:150]
    battle_main = main_screens[152:176]
    jkmn_screen = main_screens[177:201]
    battle_msg = main_screens[202:]
    
    #mode determines start or tutorial
    mode = ""

    #for generating random results later
    import random

    while ("1" or "2") not in mode:
        #title screen
        print_screen(title)
        mode = input("What would you like to do? >")
        if len(mode) > 1:
            #sound plays if input is more than 1 number, forces to put 1 number only
            print("\a")
            mode = ""
        elif "2" in mode:
            tutorial()
            #reset reply to bring back to title screen
            mode = ""
        elif "1" in mode:
            
            #putting the strings/things that need to be replaced in memory
            art = "JKMN-ART-------------------------+"
            info = "JKMN-INFO------------------------+"
            name = "JKMN-NAME--+"
            _type = "TYPE--+"
            #remaining HP
            h0 = "h0"
            #full HP
            h1 = "h1"
            move_name = "MOVE-------+]"
            move_info = "MOVE-INFO----------------------+"
            move_type = "[M-TYPE+]"
            
            #user choose jkmn
            my_jkmn = choose_jkmn(art, info, name, _type)
            #computer choose random jkmn
            foe_jkmn = foe_choose_jkmn()
            #set foe_jkmn in line below if testing
            
            #battle intro
            main_battle = battle_intro(art, name, _type, h0, h1, move_name)
            jkmn_info = jkmn_info_setup(art, info, move_name, move_info, move_type)
            
            #loops until there is a winner = x.winnername
            winner = ""
            #set tracker for special jkmn moves that connect (bowlout, antivirus), string, decreases each turn
            my_track = ""
            foe_track = ""
            while "x" not in winner:
                #repeats unless user actually puts an option
                reply = ""
                while reply == "":
                    print_screen(main_battle)
                    reply = input("What would you like to do? >")
                    if len(reply) > 1:
                        #sound plays if input is more than 1 number, forces to put 1 number only
                        print("\a")
                        reply = ""
                    elif "4" in reply:
                        print_screen(jkmn_info)
                        input(">(ENTER): Back to battle ")
                        reply = ""
                    #my_move (tuple) chosen
                    elif "1" in reply:
                        #move 1 is always standard
                        my_move = my_jkmn["move"][0]
                    elif "2" in reply:
                        my_move = my_jkmn["move"][1]
                    elif "3" in reply:
                        my_move = my_jkmn["move"][2]
                    #for unknown inputs
                    else:
                        #sound plays if input is unrecognisable
                        #or after (enter from jkmn)
                        reply = ""
                
                #identify my_move, run move, return new screen
                main_battle_1, my_track = run_move(reply, main_battle, "my", "foe", my_track)[:21]
                main_battle = main_battle_1[:21] + main_battle[21:]

                #winner check
                if foe_jkmn["foe_hp"] <= 0:
                    main_battle = main_battle[:21]
                    main_battle.append(battle_msg[5])
                    main_battle += battle_main[22:]
                    print_screen(main_battle)
                    input(">(ENTER): Back to Title Screen ")
                    winner = "x.user has won"
                    break

                #if my_jkmn = starmander and used lobotomy
                if (my_track == "lobotomy") and (len(foe_track) > 0):
                    if foe_jkmn == bowlbasaur:
                        current_screen = main_battle[:21]
                        current_screen.append(battle_msg[16])
                        current_screen += main_battle[22:]
                        print_screen(current_screen)
                        input(">(ENTER) ")
                        foe_track = ""
                    elif foe_jkmn == qwertle:
                        current_screen = main_battle[:21]
                        current_screen.append(battle_msg[14])
                        current_screen += main_battle[22:]
                        print_screen(current_screen)
                        input(">(ENTER) ")
                        foe_track = ""
                
                #foe_move chosen
                x = str(random.randint(1, 3))
                if "1" in x:
                    #move 1 is always standard
                    foe_move = foe_jkmn["move"][0]
                elif "2" in x:
                    foe_move = foe_jkmn["move"][1]
                elif "3" in x:
                    foe_move = foe_jkmn["move"][2]
                #identify my_move, run move, return new screen
                main_battle_1, foe_track = run_move(x, main_battle, "foe", "my", foe_track)[:21]
                main_battle = main_battle_1[:21] + main_battle[21:]

                #loser check
                if my_jkmn["my_hp"] <= 0:
                    main_battle = main_battle[:21]
                    main_battle.append(battle_msg[6])
                    main_battle += battle_main[22:]
                    print_screen(main_battle)
                    input(">(ENTER): Back to Title Screen ")
                    winner = "x.user has won"
                    break

                #if foe_jkmn = starmander and used lobotomy
                if (foe_track == "lobotomy") and (len(my_track) > 0):
                    if my_jkmn == bowlbasaur:
                        current_screen = main_battle[:21]
                        current_screen.append(battle_msg[16])
                        current_screen += main_battle[22:]
                        print_screen(current_screen)
                        input(">(ENTER) ")
                        my_track = ""
                    elif foe_jkmn == qwertle:
                        my_track = "1"

                #message when  antivirus over
                if my_track == "1":
                    current_screen = main_battle[:21]
                    current_screen.append(battle_msg[13])
                    current_screen += main_battle[22:]
                    print_screen(current_screen)
                    input(">(ENTER) ")
                if foe_track == "1":
                    current_screen = main_battle[:21]
                    current_screen.append(battle_msg[14])
                    current_screen += main_battle[22:]
                    print_screen(current_screen)
                    input(">(ENTER) ")

                my_track = my_track[:(len(my_track)-1)]
                foe_track = foe_track[:(len(foe_track)-1)]
            
            #AT VERY END OF BATTLE, reset reply to bring back to title screen
            #reset remaining hps of jkmn
            bowlbasaur["my_hp"], bowlbasaur["foe_hp"] = 80, 80
            starmander["my_hp"], starmander["foe_hp"] = 80, 80
            qwertle["my_hp"], qwertle["foe_hp"] = 80, 80
            mode = ""
        else:
            #sound plays if input is unrecognisable
            print("\a")
            mode = ""
