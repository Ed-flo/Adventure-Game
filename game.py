"""
By Edder Flores
Fbruary 2021
BYU-Pathway Worldwide
"""
import sys,time,os

#Defining typewriter style
def typewriter(a):
    for char in (a):
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !='\n':
            time.sleep(0.05)
        else:
            time.sleep(0.05)

#Welcome to this game
welcome = "\n\t\t\tWhat's up?\n\
Today you will help me find the way to freedom, be prepared and ready to help me.\n\
Choose one of the following options that you would like to help me with.\n" #I used double quotation mark to be able to put the " ' " in what's
typewriter(welcome)

#Gamers name
name = input('I almost forgot, What is your name? ')
g_name = name.capitalize()

#game modes menu
time.sleep(1)
print('\n===========================')
def mainMenu():
    print('\n1.ZOMBIES')
    print('\n2.ARMY')
    print('\n3.QUIT')
    while True:
        try:
            option=int(input(f'\nSo, what do you want to help me with {g_name}: '))
            print()
            if option==1:
                zombies()
                break
            elif option==2:
                army()
                break
            elif option==3:
                print('What a chicken!!')
                print()
                break
            else:
                print('\nInvalid option. Enter 1-3!')
                print()
                mainMenu()
                break
        except ValueError:
            print('\nNot an option. Enter 1-3')
            print()
            mainMenu()
            break
    exit

def zombies():
    z_exp = "\n\tYou chose Zoombies!!!\nLet me help you be up to date, on year 2020, there was a strong virus called CORONA which came from China, and nobody\nbeleived that it was going to be dangerous, so, eveyrbody just ignored it, and kept living their lives; After a while\nit expanded all around the world and infected most of the world's population.\n\n\
    They are all Zombies now and you have to SURVIVE...\n\n    Your location - Mexico City\n\n    Date: February 23rd, 2025\n\n    Time: 6:35 am\n\n"
    typewriter(z_exp)
    print('What do you do?')
    def fmenu():
        print('1.Shower and eat breakfast')
        print('2.Workout and eat your protein')
        while True:
            try:
                f_option=int(input('\n'))
                print()
                if f_option==1:
                    z_one = '\tYou got ready, now you smell good and are ready to go out and find the way out of the city, to be free and\n       be with the people that are not infected so that you can have your "normal" life back, so you go down stairs\n       from your aparment building.\n      Pick your ride...\n\n'
                    typewriter(z_one)
                    def smenu():
                        print('\nBIKE')
                        print('\nCAR')
                        print('\nSKATEBOARD')
                        while True:
                            try:
                                s_option=input('\nType your answer: ')
                                ss_option=str(s_option.lower())
                                print()
                                if ss_option=='bike' or ss_option=='skateboard':
                                    bs_scape='\tYou get on your ride, start riding towards the north and you start getting tired, but you keep tyring,\n\ta horda of zombies gets closer to you and you shoot their heads with your shotgun and kill them.\n\tYou made it out of the city, now you have 20 more miles to go and get to where the healthy people is at...\n\n\tWell Done!!\n\n\tThanks for the help!\n\n'
                                    typewriter(bs_scape)
                                    break
                                elif ss_option=='car':
                                    cr_scape='\tYou get on your car and you make sure it has enough gas to drive you outside the city, you take your AK-47,\n\tyou find out you need more AMMO in case a horda of zombies try to kill you, so you go back upstairs,\n\tyou take them and you have everything ready, you start driving listening to your favorite song, you find\n\tzombies on the road but you run over them and kill them!\n\n\tYou made it out, you are saved now!\n\n\tWell Done!!\n\n\tThanks for the help!\n\n'
                                    typewriter(cr_scape)
                                    break
                                else:
                                    print('Invalid option. Type your answer')
                                    print()
                                    smenu()
                                    break

                            except ValueError:
                                print('Type in your answer')
                                print()
                                break
                                smenu()
                    smenu()
                    break
                elif f_option==2:
                    z_two = '    There you go! you increased your physical strength a 60%, now you look good and are ready to go out and fight those zombies that will get\n   on your way. Your goal? To beat the crap out of the zombies and make it to where the people is not infected so that you can be free. You\n   find out there are Zombies out of your aparment, but you need to go down and get out of that place, but before you open the door, \n\n     Pick your weapon...\n\n'
                    typewriter(z_two)
                    def wmenu():
                        print('\nCATANA')
                        print('\nSHOTGUN')
                        print('\nPAN')
                        while True:
                            try:
                                w_option=input('\nType your answer: ')
                                ww_option=str(w_option.lower())
                                print()
                                if ww_option=='catana':
                                    c_weapon=(f'\t{g_name} took a Catana.\n\tYou are ready to cut their heads off of their bodies.\n\tYou open the door and a horda of zombies gets closer to you and you cut their heads with your Catana and kill them.\n\tYou made it out of the bulding, now you got on your Tundra and only have 120 more miles to go and get to where the healthy people is at...\n\tYou made it, you are save now.\n\n\tWell Done!!\n\n\tThanks for the help!\n\n')
                                    typewriter(c_weapon)
                                    break
                                elif ww_option=='shotgun':
                                    s_weapon=(f'\t{g_name} took a Shotgun.\n\tYou are ready to shoot their heads off their bodies.\n\tYou open the door and a horda of zombies is waiting for you, so you start shooting to their heads and kill them.\n\tYou made it out of the building, now you get on your chopper and only have 120 more miles to go and arrive to where the healthy people is at...\n\tYou made it, you are save now.\n\n\tWell Done!!\n\n\tThanks for the help!\n\n')
                                    typewriter(s_weapon)
                                    break
                                elif ww_option=='pan':
                                    p_weapon=(f'\t{g_name} took a Pan.\n\tYou are ready to cook their brains.\n\tYou open the door and a horda of zombies is waiting for you, so you start hitting them heads and kill but a couple of them.\n\tOh no! You are being bitten by one. Oh man!!!! Noooooo!!!!! Get out of there!!! Ruuuuuun! Nooooo, {g_name} ruuuun!!!...\n\n\tYou are dead!!\n\n\tYou were not helpful, how did you think you were goning to win with a Pan!?\n\n\tGAME OVER\n\n')
                                    typewriter(p_weapon)
                                    break
                                else:
                                    print('Invalid option. Type your answer')
                                    print()
                                    wmenu()
                                    break

                            except ValueError:
                                print('Type in your answer')
                                print()
                                break
                                wmenu()
                    wmenu()
                    break
                else:
                    print('\n Come on! I am not joking. Choose 1-2')
                    print()
                    fmenu()
                    break
            except ValueError:
                print('\nEnter a numeric answer...')
                print()
                break
                fmenu()
        exit
    fmenu()
    

def army():
    a_exp = (f"\n\t{g_name} chose Army!!!\nYou joined the army 10 years ago, on year 2023, everything was going alright, until now, a war has been declared by\nthe Chinese nation, you are the Chief Master, and you are the only one with this special army suit which has a lot of\nnice features, you have your own personal assistant installed into it, and she tells you everything about any enemy\nor any research you wanna know about, she'll do it\n\n\
    The war will start soon, now you have to be prepared and plan your strategy...\n\n   Your location - Texas, San Antonio\n\n   Date: February 5th, 2033\n\n")
    typewriter(a_exp)
    print('What strategy do you think is better?')
    def pa_menu():
        print('\n1.Defeat in detail')
        print('\n2.Flanking maneuver')
        while True:
            try:
                st_option=int(input('\n'))
                print()
                if st_option==1:
                    df_strategy=(f"Good choise Chief!\nThis strategy brings a large portion of one's own force to bear\non small enemy units in sequence, rather than engaging the bulk of the enemy force all at once.\n\nSo let's start this off, Do you want to go with the first portion team?\n\n")
                    typewriter(df_strategy)
                    def fstrmenu():
                        print('\nYES')
                        print('\nNO')
                        while True:
                            try:
                                yn_option=input('\nType "Y" or "N" ')
                                yynn_option=str(yn_option.upper())
                                print()
                                if yynn_option=='Y':
                                    ys_opt=(f'  Alright, you are in, you are the leader of that first portion to go and\n  destroy the enemy. Oh! What is that? Do you see that? It is the enemy, be quite, hide!!\n  Ufff! That was close, they almost see you. Good thing your virtual assistant knows what you are\n  thinking about, and it sounds good to men, we can do waht you have in mind.\n\n  So, you and the rest of the soldiers went to fight the enemy but from different sides.\n  You are in the left group.\n There, you see that? that is the chief of the eneemies...\n\n  Well done chief, you killed him, and you see that, your team already killed the rest of them.\n  You won!...Wait a second, what is that? A letter? What does it say?\n\n  ({g_name} read the letter)\n\n It said that the whole army of the enemy were the ones that you and your soldiers killed!!\n\n  Well Done {g_name}!!!\n\n  You won the war!!')
                                    typewriter(ys_opt)
                                    break
                                elif yynn_option=='N':
                                    no_opt=(f"  The first soldiers went to the enemies' camp!\n  Chief what is that? You hear that?... The radio! Your soldiers are calling you;\n  Oh no!! They are having problems, the enemies caught them, they are killing them.\n  Oh no!! Your last soldier just said his last words! They all died!\n\n  What do we do now? Wait... do you see that? The enemies are comming to our location!!!\n  No! They killed the snipers!... Go down chief!! Start fireeeee!!!! You killed 3 enemies,\n  well done.\n  Oh no Chief, they caught you, no, no, nooooooooooooooooooooooo-^-^-^-^-____________\n\n  You died! They killed you!\n\n  GAME OVER\n\n")
                                    typewriter(no_opt)
                                    break
                                else:
                                    print('Invalid option. Try 1-2')
                                    print()
                                    fstrmenu()
                                    break
                            except ValueError:
                                print('Type Y or N...')
                                print()
                                break
                                fstrmenu()
                    fstrmenu()
                    break
                elif st_option==2:
                    flo_strategy=(f"Really? Well, it might work.\nThis strategy involves attacking the opponent from the side,\nor rear. So let's start this off. This strategy can help us win the war and bring freedon to our nation, that means that we have\na big responsability in our backs. What do you say, should we attack from one side or rear?\n\n")
                    typewriter(flo_strategy)
                    def flamenu():
                        print('ONE SIDE')
                        print('REAR')
                        while True:
                            try:
                                sr_option=input('\n ')
                                srsr_option=str(sr_option.lower())
                                print()
                                if srsr_option=='one side':
                                    oside_opt=(f"  Good choice!\n  I am not afraid of an Army of lions lead by a sheep; I am afraid of sheep\n  lead by a lion. The true soldier fights not because he hates what is in front of him,\n  but because he loves what is behind him!\n\n  computer: Sir, I got a little bit of movement in the little tertiary valley to the left.\n\n  Chief: There is movement up there?\n\n  computer: There's three dudes...\n\n  soldiers: oh no! That shot right through us sir, right here.\n\n  Chief: Is that what they shot?\n\n  soldier: Yeah, it's a Dishka round... still warm\n\n  computer: Let's get it on!!\n\n  computer: Come on! Let's go! Get it up and fire!!\n\n  Chief: Come on, gunner. You've got to be quicker than that.\n\n  computer: Up hire!\n\n  ...\n\n  Chief: it's still too low! \n\n  (gun shots)\n\n  computer: Nice, good shot!\n\n  Enemy radio update: Oh, one person is injured now. To the legs.\n\n  ...\n\n Chief: Well done soldiers, good job!\n\n")
                                    typewriter(oside_opt)
                                    print('What do we do now?')
                                    def firstsec_option():
                                        print('1. Go attack')
                                        print('2. Stay and deffend')
                                        while True:
                                            try:
                                                gtack_opt=int(input('\n\t'))
                                                print()
                                                if gtack_opt==1:
                                                    gtack_exp=(f"  Chief: Let's go soldiers, it's time to attack\n\n  computer: Hey, let's get another target worked up!\n\n  computer: So, we're gonna start back here, we're gonna\n  make condition 1 at this rock pile as we go up this hill, it's up\n  to the Master Chief really at that point what he wants to do.\n\n  ...\n\n  Chief: We'll go ahead. Pistol, you are going to take the far right, Roger, you're gonna\n  follow up. Pierre and Doc, you got the left...Alright, let's do this\n\n  Soldiers: One every eeeeiiight!!! Let's go! We got them\n\n  (The US army starts fire and Won the war)\n\n Congrats Chief {g_name}\n\n Thanks!\n\n")
                                                    typewriter(gtack_exp)
                                                    break
                                                elif gtack_opt==2:
                                                    stay_exp=(f"  computer: It doesn't take a hero to order men into battle.\n  It takes a hero to be one of those men who goes into battle. We'll follow your lead\n\n  soldiers: Chief, the enemy is getting closer from the north\n\n  soldiers: 50 meters\n\n soldiers: 10 meters\n\n  Chief: Open firee!!\n\n (Fire starts)\n\n  soldiers: Chief! Half of our team is down\n\n  (Enemies killed the rest of the US army)\n\n  computer: Chief they're behind you! Nooooo!\n\n   {g_name} got killed\n\n  GAME OVER\n\n")
                                                    typewriter(stay_exp)
                                                    break
                                                else:
                                                    print('Invalid option. Enter 1-2')
                                                    print()
                                                    firstsec_option()
                                                    break
                                            except ValueError:
                                                print('Invalid option. Enter 1-2')
                                                print()
                                                firstsec_option()
                                                break
                                    firstsec_option()
                                    break
                                elif srsr_option=='rear':
                                    rer_opt='  The worst option you could have made Chief!\n  The whole US amry walked towards the enemy, they got caught and were killed!!\n\n  You lose!\n\n  GAME OVER\n\n'
                                    typewriter(rer_opt)
                                    break
                                else:
                                    print('\nInvalid. Select 1-2')
                                    print()
                                    flamenu()
                                    break
                            except ValueError:
                                print('\nType your answer.')
                                print()
                                flamenu()
                                break
                    flamenu()
                    break
                else:
                    print('\n Come on! I am not joking. Choose 1-2')
                    print()
                    pa_menu()
                    break

            except ValueError:
                print('\nEnter a numeric answer...')
                print()
                break
                pa_menu()
        exit
    pa_menu()
mainMenu()