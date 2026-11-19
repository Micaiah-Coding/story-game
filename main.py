"""
Adventure game coded by Micaiah
No AI was used in the coding of this project.
Some AI was used to help research certain techniques used in this project like the google search AI.
But all code was handwritten and designed without AI.
"""

# lets me use randomization
import random

input("Before continueing, I strongly reccomend you put the window in fullscreen. PRESS THE ENTER TO CONTINUE ")
print()

# Variables


# user number
name_number = random.randint(1,700)

# friend name randomizer
friend_boy_names = ["Alex", "John", "Kohl", "Arlo", "James", "Kyle", "Cody", "Isaac"]
friend_girl_names = ["Judy", "Mya", "Lucy", "Sarah"]

# male friend names
friend_boy_name_1 = random.choice(friend_boy_names)
friend_boy_name_2 = random.choice(friend_boy_names)

# female friend names
friend_girl_name_1 = random.choice(friend_girl_names)

# makes sure theres no simiar names and no repeat names
while friend_boy_name_1 == friend_boy_name_2 or friend_boy_name_1 == "Kohl" and friend_boy_name_2 == "Kyle" or friend_boy_name_1 == "Kyle" and friend_boy_name_2 == "Kohl" or friend_boy_name_1 == "Alex" and friend_boy_name_2 == "Arlo" or friend_boy_name_1 == "Arlo" and friend_boy_name_2 == "Alex":
    friend_boy_name_1 = random.choice(friend_boy_names)
    friend_boy_name_2 = random.choice(friend_boy_names)
    
# establish nicknames probably in a way more complicated way than probably needed
friend_boy_name_1_nick = "NULL"
friend_boy_name_2_nick = "NULL"
friend_girl_name_1_nick = "NULL"

if friend_boy_name_1 == "Alex":
    friend_boy_name_1_nick = "A"
elif friend_boy_name_1 == "John":
    friend_boy_name_1_nick = "J"
elif friend_boy_name_1 == "Kohl":
    friend_boy_name_1_nick = "K"
elif friend_boy_name_1 == "Arlo":
    friend_boy_name_1_nick = "A"
elif friend_boy_name_1 == "James":
    friend_boy_name_1_nick = "J"
elif friend_boy_name_1 == "Kyle":
    friend_boy_name_1_nick = "K"
elif friend_boy_name_1 == "Cody":
    friend_boy_name_1_nick = "Cod"
elif friend_boy_name_1 == "Isaac":
    friend_boy_name_1_nick = "I"
    
if friend_boy_name_2 == "Alex":
    friend_boy_name_2_nick = "A"
elif friend_boy_name_2 == "John":
    friend_boy_name_2_nick = "J"
elif friend_boy_name_2 == "Kohl":
    friend_boy_name_2_nick = "K"
elif friend_boy_name_2 == "Arlo":
    friend_boy_name_2_nick = "A"
elif friend_boy_name_2 == "James":
    friend_boy_name_2_nick = "J"
elif friend_boy_name_2 == "Kyle":
    friend_boy_name_2_nick = "K"
elif friend_boy_name_2 == "Cody":
    friend_boy_name_2_nick = "Cod"
elif friend_boy_name_2 == "Isaac":
    friend_boy_name_2_nick = "I"

if friend_girl_name_1 == "Judy":
    friend_girl_name_1_nick = "Jude"
elif friend_girl_name_1 == "Mya":
    friend_girl_name_1_nick = "M"
elif friend_girl_name_1 == "Lucy":
    friend_girl_name_1_nick = "Luce"
elif friend_girl_name_1 == "Sarah":
    friend_girl_name_1_nick = "S"

# establish name numbers
friend_boy_num_1 = random.randint(1,500)
friend_boy_num_2 = random.randint(1,500)
friend_girl_num_1 = random.randint(1,500)
txt_friend_boy_num_1 = friend_boy_num_1
txt_friend_girl_num_1 = friend_girl_num_1
txt_friend_boy_num_2 = friend_boy_num_2
# make sure that none of the name numbers are the same, and recalculates if they are
while friend_boy_num_1 == friend_boy_num_2 or friend_boy_num_1 == friend_girl_num_1 or friend_boy_num_2 == friend_girl_num_1 or name_number == friend_girl_num_1 or name_number == friend_boy_num_1 or name_number == friend_boy_num_2:
    friend_boy_num_1 = random.randint(1,500)
    friend_boy_num_2 = random.randint(1,500)
    friend_girl_num_1 = random.randint(1,500)
    name_number = random.randint(1,700)

# make full name numbers and full names
if friend_boy_num_1 < 10 and friend_boy_num_1 >= 1:
    txt_friend_boy_num_1 = "00" + str(friend_boy_num_1)
elif friend_boy_num_1 < 100 and friend_boy_num_1 >= 10:
    txt_friend_boy_num_1 = "0" + str(friend_boy_num_1)

if friend_boy_num_2 < 10 and friend_boy_num_2 >= 1:
    txt_friend_boy_num_2 = "00" + str(friend_boy_num_2)
elif friend_boy_num_2 < 100 and friend_boy_num_2 >= 10:
    txt_friend_boy_num_2 = "0" + str(friend_boy_num_2)

if friend_girl_num_1 < 10 and friend_girl_num_1 >= 1:
    txt_friend_girl_num_1 = "00" + str(friend_girl_num_1)
elif friend_girl_num_1 < 100 and friend_girl_num_1 >= 10:
    txt_friend_girl_num_1 = "0" + str(friend_girl_num_1)

friend_boy_name_1_full = friend_boy_name_1 + " " + str(txt_friend_boy_num_1)
friend_boy_name_2_full = friend_boy_name_2 + " " + str(txt_friend_boy_num_2)
friend_girl_name_1_full = friend_girl_name_1 + " " + str(txt_friend_girl_num_1)

# personal data logic
name_number_txt = "NULL"
name = input("What would you like to be your name new user?: ")
if name == "":
    name = "User"

if name == "User":
    print()
    input("You lowkey had to be either reading the code or just extremly lucky to get this message User. Nice job.")
print()
input("Processing..")
print("Validated. Proceeding with survey.")
print()

fav_number = int(input("What is your favourite (whole) number between 0 and 99 " + str(name) + "?: "))
# really fancy way of saying that your score multiplier is your your number as a percent +1
# example, Input: 67, Output: 1.67
score_multiplier = min(1.00, max(0.00, round(float(fav_number) / 100, 2))) + 1.0
score = 0
print()

# makes sure name_number and full_name look proper
if name_number < 10 and name_number > 0:
    name_number_txt = "00" + str(name_number)
elif name_number < 100 and name_number > 9:
    name_number_txt = "0" + str(name_number)
else:
    name_number_txt = str(name_number)
    
full_name = name + " " + name_number_txt

# birthday logic    
print("What is your birthdate?")
month = int(input("Month (enter a number ## or #): "))
if month > 12 or month <= 0:
    month = random.randint(1, 12)
    input("Invalid month, month is now set to " + str(month) + ".")
day = int(input("Day (enter a number ## or #): "))
if day > 31 or day <= 0:
    day = random.randint(1, 31)
    input("Invalid day, day is now set to " + str(day) + ".")
year = int(input("Year (enter a number ## or #): "))
if year >= 100 or year <= 0:
    year = random.randint(1, 99)
    input("Invalid year, year is now set to " + str(year) + ".")
    
month_txt = "NULL"
day_txt = "NULL"
year_txt = "NULL"

if month > 0 and month < 10:
    month_txt = "0" + str(month)
else:
    month_txt = str(month)

if day > 0 and day < 10:
    day_txt = "0" + str(day)
else:
    day_txt = str(day)

if year > 0 and year < 10:
    year_txt = "0" + str(year)
else:
    year_txt = str(year)
    
# interesting little thing that gives a 2 digit value based on some user inputs   
canon_year = "26" + str(int(min(99, max(10, round(((year + 20*day) / 10), 0)))))

bday = str(month_txt) + "/" + str(day_txt) + "/24" + str(year_txt)

print()

# gender logic for even more personalization
gender = input("What is your gender (boy/girl/other)?: ")
print()
contraction_1 = "NULL"
vocative_1 = "NULL"
vocative_2 = "NULL"

if gender == "boy":
    contraction_1 = "he's"
    vocative_1 = "bro"
    vocative_2 = "sir"
elif gender == "girl":
    contraction_1 = "she's"
    vocative_1 = "sis"
    vocative_2 = "ma'am"
elif gender == "other":
    contraction_1 = "they're"
    vocative_1 = str(name)
    vocative_2 = "friend"
print("Proceeding.")

# clears console ↓↓
print("\033[H\033[J", end="")


# Story/Story Logic

# escape characters for things: \033[3m = Italic, \033[1m = Bold, \033[4m = Underline, \033[0m = Clear Styling

# story continueation variables.. idk if this bit is actually necessary after doing some research..
ending = 0
timeline_version = "NULL"
chance_choice = "NULL"
read_paper = "NULL"
sneak_away = "NULL"
feeling = "NULL"
keep_going = "NULL"
keep_going_type2 = True
run_or_fight = "NULL"
run_or_fight_2 = "NULL"
story_switch = False
t_minus_number = 9
friend_follow = random.randint(1,2)
if friend_follow == 1:
    friend_follow = True
elif friend_follow == 2:
    friend_follow = False
fix_reactor = "NULL"
digit1 = "NULL"
digit2 = "NULL"
digit3 = "NULL"
checksum = "Incomplete"
checksum1 = "NULL"
special_digit1 = "NULL"
special_digit2 = "NULL"
final_number = "NULL"
TwoFA = "Incomplete"
crazy_choice = "NULL"
mushroom_choice = "NULL"
score = 0.0
rand_choice_1 = random.randint(0,1)

# actual story

input("You are a highly esteemed and respected Helltrooper of the IMMORTAL division. Your only job is to follow the orders of FLEETCOMMAND (FleetCom for short).")
print()
input("It is year " + canon_year + " of the UNC (United Nations Calendar). A system that's job is keeping a set time for everything.")
print()
input("You are currently in orbit around the contested planet ZK2 aboard the USCS (United Space Command Ship) Morgan, a Destroyer class spacecraft.")
print()
input("This is a memory recall message, it is used when you die somewhere and are revived along with the drug Vivagen to help you rememeber who you are.")
print()
input("Recovered Data..")
print()
print()
input("Name: " + full_name)
print()
input("Birthday: " + bday)
print()
input("Best friends: " + friend_boy_name_1_full + ", " + friend_boy_name_2_full + ", " + friend_girl_name_1_full +"." )
print()
input("Rank: Chief Warrant Officer 5, Serving under: Brigadier General Zyko")
print()
input("This is your 5th time being revived.")
print()
continue_on = input("REPEAT MESSAGE/CONTINUE: ")
print("\033[H\033[J", end="")
if continue_on == "REPEAT MESSAGE":
    input("This message will not be repeated again.")
    print()
    input("You are a highly esteemed and respected Helltrooper of the IMMORTAL squad. Your only job is to follow the orders of FLEETCOMMAND (FleetCom for short).")
    print()
    input("It is year " + canon_year + " of the UNC (United Nations Calendar). A system that's job is keeping a set time for everything.")
    print()
    input("You are currently in orbit around the contested planet ZK2 aboard the USCS (United Space Command Ship) Morgan, a Destroyer class spacecraft.")
    print()
    input("This is a memory recall message, it is used when you die somewhere and are revived along with the drug Vivagen to help you rememeber who you are.")
    print()
    input("Recovered Data:")
    print()
    print()
    input("Name: " + name + " " + str(name_number))
    print()
    input("Birthday: " + bday)
    print()
    input("Best friends: " + friend_boy_name_1_full + ", " + friend_boy_name_2_full + ", " + friend_girl_name_1_full +"." )
    print()
    input("Rank: Chief Warrant Officer 5, Serving under: Brigadier General Zyko")
    print()
    input("This is your 5th time being revived.")
    print()
    continue_on = "CONTINUE"
else:
    continue_on = "CONTINUE"
if continue_on == "CONTINUE":
    input("\"Well look who's finally back. Awake from his beauty rest.\" A voice says. \"Yo " + contraction_1 + " awake now?\" Another voice asks. Suddenly a bright light covers your entire vision and you start feeling things.")
    print()
    input("You quickly become aware that you are floating in a chamber in some kind of fluid. \033[3mWait.. the message said something about a Vivagen drug.. I wonder if thats what I'm in\033[0m?")
    print()
    input("\033[1mFLUSH\033[0m. In an instant the chamber is drained. \033[1mHiSSSSsSssSsss\033[0m. The chamber door opens up and you are greeted with 2 people and a bright circular room with metal walls. \033[3mThese must be the people I heard talking\033[0m.")
    print()
    timeline_version = input("One of the people standing in front of you is scruffy and older looking, the other person is a bit younger looking, he looks like he's in his 20s. Which do you talk with? (Older Guy/Younger Guy): ")
    if timeline_version == "Older Guy" or timeline_version == "older guy" or timeline_version == "older Guy" or timeline_version == "Older guy":
        score = score + round(round((1000.0*score_multiplier)*0.9), 1)
        print()
        input("You look at the scruffy dude. \"I think I remember you.. General Zyko right??.\" You say. \"Yes.\" He replies. \"Sir.\" You salute. \"At ease Officer.\" Zyko responds. \"So why am I here.. What happened to me?\" You ask. \"You are here because you were on patrol and an enemy helicopter strafed your patrol group as rebel troops showed up.\"")
        print()
        input("After a slight pause, he continues. \"You all fought like hell. But you were killed just before reinforcements arrived. We were obviously able to recover your body and revive it, seeing as you're standing right here.\" \033[3mOhhhh I remember now.. I was on ZK2 on patrol around our camp and a rebel *KITE 'Copter showed up and launched AGMs at our group. I think our **ADVS battery intercepted them.")
        print()
        input("\"I understand.\" You say with a grim look on your face. \"We did the best we could.\" ")
        for i in range(17):
            print()
        input("*KITE Helicopter - Kill-zone Integration & Tactical Engagement Helicopter. A powerful anti-personnel vehicle armed with an 50mm auto-cannon turret on its chin as its main armament. Other armaments include 2 20mm gatling guns, 1 on each side, and AGM SAR (SAR: Submunition Anti-personnel Rocket) missiles on the wing pods.")
        print()
        input("**ADVS battery - an ADVS or a Gridlock ADVS Battery is an Advanced Defense Vector Sentinel, meaning it is a vector shield that can target and reliably remove things from nearby airspace within 5 Kilometers up to the size of a baseball. It can't target lock bullets very well as the RI (Research and Integrations) subdivision of FleetCom hasn't developed an ***AERIS system powerful enough to accurately target something that small.")
        print()
        input("***AERIS - The Atomic Energy Radius Illumination Sensor is a radar type system that can detect objects and scan them at an atomic level from up to 5 km away but can't get a reliable traditonally called \"target lock\" if the object is bigger than the size of an average baseball.")
        print("\033[H\033[J", end="")
        input("\033[1m\"ALARM. ALARM. LARGE REBEL FORCE APPROACHING MARINE ENCAMPMENT. ETA: 3 HOURS\"\033[0m")
        print()
        input("\"I have an offer to make you trooper. I can offer you another chance. A chance at revenge. A chance to continue helping a cause bigger than you. But I won't force you to go. You're still recovering..\"")
        print()
        chance_choice = input("\"Will you go?\" (Yes/No): ")
        if chance_choice == "Yes" or chance_choice == "yes":
            score = score + round(round((100.0*score_multiplier)*0.7), 1) # adds a base number of 100 to the score, as well as multiplies it buy the score multiplier and another choice value multiplier (0.7), and makes sure its still a float
            print()
            input("\"Glad to have you, be ready to drop and in your *DC in 2 hours.\" Zyko explains. \"Yes sir.\" You say with a nod.")
            print()
            input("\033[3mI'm going to go get some rest and clean myself up before we drop\033[0m.")
            print()
            input("\033[1m\033[3mAn hour later in your quarters\033[0m.")
            print()
            input("\033[3mI wonder how much this room costs.. between the fancy bed, AI chef and shower, and the quality of these carpets\033[0m. \"I wonder why they have such nice quarters for little old me.\" You say to yourself as you walk over to the table in front of your couch. There's a paper on the table titled in case you forgot.")
            print()
            read_paper = input("Do you read it? (Yes/No): ")
            for i in range(17):
                print()
            input("*DC - A Death Chamber is a bullet shaped one man pod that is fired from a ship in orbit around a planet. They have the name Death Chamber because no one besides the specially physically enhanced Helltroopers with their suits are able to survive a drop from space at over MACH 5.")
            if read_paper == "Yes" or read_paper == "yes":
                score = score + round(round((100.0*score_multiplier)*0.5), 1)
                print("\033[H\033[J", end="")
                input("\033[1m\033[4mIn Case You Forgot\033[0m")
                for i in range(3):
                    print()
                input("You are an esteemed member of a special group of soldiers that go by the name of Helltroopers. 700 Helltroopers were \"Produced\" 100 years ago, you are one of them. The unfortunate thing is that Helltroopers were trained from the age of 3. By adulthood they were genetically and physically modified to be smarter, faster, and MUCH stronger than an average soldier.")
                input("RI also made another enhancement to the Helltroopers, a suit of armor that has a mechanical skeleton integrated into the armor to reduce trauma. Unfortunatley for the viser to work properly it has to be thin so a modern armor piercing round tears through it.. But that's besides the point. Helltroopers are trained in the operation of many vehicles, although they are mainly trained on KITEs and *APWPs.")
                input("The purpose of the Helltrooper program was to create a force powerful enough to subdue rebel and foreign forces that seek to threaten Earth and it's colonies. That is your primary objective, even above FLEETCOMMAND's orders.")
                print()
                input("/* End Document */")
                for i in range(20):
                    print()
                input("*APWP - An Anti-Personnel Walking Platform, or Scythe is a walker/strider type vehicle that has 2 rapid-fire 30mm rotary cannons mounted on the underside of the body that are retractable. The Scythe is built to traverse any kind of terrain, due to having 8 legs its movement mimics that of a spider's, when crawling vertical or upside down its legs deploy tungsten barbs that are used to \"grab the ground\" as it walks. Its secondary armament is a flamethrower located on the center of the underside of the vehicle. The cockpit is also on the underside as well, this is because Scythes are very prone to being strafed by enemy aircraft and it was found to take less damage and be spotted less when a study was conducted by RI. It has 2 variants, see article on **ATAWP.")
                input("**ATAWP - The Anti-Tank/Air Walking Platform, the Sagittar uses a very similar chassis to the APWP but is slightly modified to have flare pods on the legs and instead of the armaments on the APWP, the ATAWP is armed with a precision 122mm anti-air cannon mounted on the top of the platform along with 2 batteries on turrets besides the main gun.")
            elif read_paper == "No" or read_paper == "no":
                score = score + round(round((30.0*score_multiplier)*0.5), 1)
            print("\033[H\033[J", end="")
            sneak_away = input("\033[3mIt's almost time for me to go down to my DC. Just 25 minutes left till drop..\033[0m (Go/Sneak off)?: ")
            print()
            if sneak_away == "Go" or sneak_away == "go":
                score = score + round(round((100.0*score_multiplier)*0.7), 1)
                input("\033[3mProbably for the best that I go.\033[0m")
                print()
                print("\033[H\033[J", end="")
                input("\033[1m20 minutes later in the launch bay.\033[0m")
                print()
                feeling = input("\033[3mWow.. I don't remember this place being so big.\033[0m All the sudden out the corner of your eye you see a familiar face. \"Yo " + friend_boy_name_2 + " nice to see you again bro. \" You say loudly so he can hear you over all the background noise. " + friend_boy_name_2 + " hears you yelling and jogs over across the launch bay. \"It's been a little since I seen you, how you doin " + vocative_1 + "?\" (Good/Alright/Bad): ")
                print()
                if feeling == "Good" or feeling == "good":
                    score = score + round(round((100.0*score_multiplier)*0.3), 1)
                    input("\"Glad to hear it. We drop in 5, you should make your way to your pod. Come on I'll show you where it is.\"")
                    print()
                elif feeling == "Alright" or feeling == "alright":
                    score = score + round(round((70.0*score_multiplier)*0.3), 1)
                    input("\"Well it'll be right as rain soon, you won't believe how fun dropping into a hot drop is. Follow me.\"")
                    print()
                elif feeling == "Bad" or feeling == "bad":
                    score = score + round(round((50.0*score_multiplier)*0.3), 1)
                    input("\"Well you'll be doing an awful lot better soon, lemme show you where your pod is and you can relearn just how fun dropping is.\"")
                    print()
                input("\"Hey " + friend_boy_name_2_nick + " is this safe..\" You ask. You look over to where you thought " + friend_boy_name_2 + " was standing, but he isn't there. Instead he is getting into a hole in the floor about 5 meters away. \"Totally safe. You and me have done this hundreds of times.\" He replies as he closes the lid to his pod. \033[3mIt's so weird. People talking about me doing stuff I don't remember..\033[0m")
                print()
                input("You climb into your DC. \033[3mHere goes nothing.. You know, actually kinda nice in...\033[0m. ")
                print()
                input("\033[1mAll Troopers To Your DCs Launch in T- 10.")
                for i in range(9):
                    input("\033[1m" + str(t_minus_number) + ".")
                    t_minus_number = t_minus_number - 1
                print()
                print()
                if rand_choice_1 == 1:
                    input("\033[1mDCs departing. Good look down there Helltroopers.")
                    keep_going_type2 = False
                    keep_going = "Proceed to another pod"
                elif rand_choice_1 == 0: 
                    input("\033[1mERROR LAUNCHING POD CONTAINING " + full_name + ". PROCEED TO ANOTHER POD OR TO YOUR QUARTERS\033[0m.")
                    keep_going = input("Will you \"Proceed to quarters\" or \"Proceed to another pod\"?: ")
                if keep_going == "Proceed to another pod":
                    score = score + round(round((100.0*score_multiplier)*0.4), 1)
                    print()
                    if keep_going_type2:
                        input("\033[3mWhy does this stuff always happen to me\033[0m. You take a big sigh as you hop out of your pod and into an unoccupied one to your right.")
                        print()
                    input("\033[1mVWHOOSH\033[0m. Your pod is jettisoned from the USCS Morgan. The view is incredible, the huge planet, the other pods, the stars the 2 suns being absorbed by a black hole.. All visible through your tiny window. \033[3mI've never seen anything like this before\033[0m.")
                    print()
                    input("\033[3mI wonder how hot of a drop this'll be.. Best not think about it too much.\033[0m After falling for 5 minutes a warning LED screen flickers on, \033[1mBRACE FOR IMPACT\033[0m. \033[1m*sigh Let's do this.\033[0m You grab one of the rifles in front of you, check that it's loaded, grab a few mags, strap some grenades to your belt, grab a couple submachine guns from behind you and are ready to go.")
                    print()
                    input("\"This is IMMORTAL Squad Leader " + str(friend_girl_num_1) + " to IMMORTAL Squad, load your weapons, as soon as we land lay down suppressing fire East North-East.\" A woman says over the comms. Five acknowledgment lights winked on in your HUD in your helmet. You feel adrenaline start to flood your veins. You hear the blood pumping in your years. You feel your heartbeat loud in your chest. \033[3mNo chickening out now\033[0m.")
                    print("\033[H\033[J", end="")
                    input("\033[1mTHOOM\033[0m! Your DC hits the ground. \033[1mVRrrRRrrr\033[0m. Instantly you are pushed up by the hydraulic platform in the pod. \033[3mHere we go\033[0m. Something catches your eye to your left. \033[3mEast northeast like the squad leader said. \033[1mBRATTATATATTA\033[0m You pull the triggers on both your submachine guns, tracer rounds fly everywhere. \033[1mWHISTLEEeEeeEeee\033[0m. You become painfully aware of a high pitched whistle ringing out getting louder.")
                    print()
                    input("\"EVERYBODY SCATTER!!\" You hear over the comms. Just after, you are knocked to the ground by a massive explosion about 100 meters to your right. \"This is IMMORTAL squad leader " + friend_girl_name_1_full + " to all remaining IMMORTAL members, fall back to base. I repeat, fall back to base to rearm.\" You turn south to retreat to base when you feel a rumble in the ground.")
                    print()
                    run_or_fight = input("Do you retreat or stay and fight off whatever is coming? (Stay/Run): ")
                    print()
                    while run_or_fight == "Stay" or run_or_fight == "stay":
                        score = score + round(round((100.0*score_multiplier)*1), 1)
                        input("You start to hear thumping getting louder. You turn towards the thumping and are met with a Scythe ATWP in the distance running towards you at a dead sprint. \033[3mOh. This might be it for me.\033[0m")
                        print()
                        stay_or_fight_2 = input("Do you stay and fight against the ATWP or do you run and call for backup? (Fight/Run): ")
                        print()
                        if stay_or_fight_2 == "Run" or stay_or_fight_2 == "run":
                            stay_or_fight = "Run"
                        elif stay_or_fight_2 == "Fight" or stay_or_fight_2 == "fight":
                            input("\033[1mBRATATATATATATA\033[0m. 30mm rounds start destroying the ground in front of you. Once shatters on your right shoulder armor, causing you to almost twist right and fall over. You start sprinting at the walker as it showers you and the area near you with rounds. You close the distance fast. 70 meters, 50 meters, 30, 20, just as you're about to be in range to try and take it down, it's flamethrower ignites.")
                            print()
                            input("\033[1mWHOOOSHhh\033[0m. You jump prone to the under side of the Scythe. You grab your rifle off your belt and spray the area above you with bullets. And just as suddenly as it showed up, the Scythe comes to a complete stop.")
                            print()
                            print("\033[H\033[J", end="")
                            run_or_fight = "NULL"
                            ending = 1
                            score = score + 1000.0
                    if run_or_fight == "Run" or run_or_fight == "run":
                        input("You turn around and sprint as fast as you can. \"I NEED SOME BACKUP OVER HERE!!\" You yell into your comm as you're running. Out of seemingly nowhere, multiple rounds slam into your back.")
                        print("\033[H\033[J", end="")
                        ending = 3
                        score = score + 300.0
                elif keep_going == "Proceed to quarters." or keep_going == "proceed To quarters" or keep_going == "proceed to Quarters" or keep_going == "proceed to quarters" or keep_going == "Proceed To quarters" or keep_going == "Proceed To Quarters" or keep_going == "proceed To Quarters":
                    score = score + round(round((50.0*score_multiplier)*0.4), 1) # where i left off
                    print()
                    input("You get up out of your pod and start to make your way back to your quarters when you get the 'brilliant' idea to stop by the cafeteria first because you're hungry.")
                    story_switch = True
            elif sneak_away == "Sneak off" or sneak_away == "sneak off" or sneak_away == "Sneak Off" or sneak_away == "sneak Off":
                score = score + round(round((40.0*score_multiplier)*0.5), 1)
                print()
                input("You go and sneak away to the cafeteria because you're feeling kinda hungry.")
                story_switch = True
        elif chance_choice == "No" or chance_choice == "no":
            score = score + round(round((30.0*score_multiplier)*0.7), 1)
            print()
            input("\"No, thank you for the offer, but I'm too tired to go and fight right now. I plan on heading back to the cafeteria to grab a bite to eat.\" You say. \"That's alright, I kinda thought you'd say that, go ahead and go then.\" He responds with.")
            story_switch = True
    # i lowkey didn't have time to make this section as lore heavy..
    if timeline_version == "Younger Guy" or timeline_version == "younger guy" or timeline_version == "younger Guy" or timeline_version == "Younger guy":
        score = score + round(round((1000.0*score_multiplier)*0.9), 1)
        print()
        input("You look at the younger guy, he looks familiar but you can't quite remember his name.. \"Follow me.\" He says as he turns around and starts walking. So you do the only thing left to do and follow him.")
        print()
        input("You both end up in the cafeteria. But he's gone out of sight.")
        story_switch = True
    if story_switch:
        print()
        input("\"Hi, I'm " + friend_boy_name_1 + " in case you forgot. Also in case you forgot, you know me really well, we're best friends actually.\" Someone apparently named '" + friend_boy_name_1 + "' says behind you. You turn around to face them and see that it's the younger dude from earlier. \033[3mOh I remember now.. thats one of my best friends the memory recall message told me about\033[0m.")
        print()
        input("\"Ahh, " + friend_boy_name_1_full + ". I remember now. Nice to see you bro!\" You say in response. \"I knew you'd remember, nice to see you " + vocative_1 + ". Glad to see you're up and moving well enough to get here.\" He replies. \033[3Man I am hungry.. I'm gonna start going to get some food, I hope " + friend_boy_name_1 + " follows, because I ain't waiting\033[0m.")
        print()
        if friend_follow:
            input("\"Yo " + friend_boy_name_1_nick + " I'm gonna go get some food. I'm starving bro.\" You say. \"Alright, give me a second and I'll come with you.\" He says while fixing his belt. \"Alright good to go. Lead the way my good " + vocative_2 + ".\" He continues. You both continue on to get your food and sit down at a table. \033[3mThis place is big enough to fit a thousand people\033[0m..")
        elif not friend_follow:
            input("\"Yo " + friend_boy_name_1_nick + " I'm gonna go get some food. I'm starving bro.\" You say. \"I'll go wait for you at a table while you get some food. Go on now. Git.\" He says. \"Well fine then.\" You say as you walk of to go get some food. \033[3mThis food smells delicious, I wonder what it is..\033[0m. After you get food you spot " + friend_boy_name_1 + " at a table and walk over.")
        print()
        input("\"You know, whatever is in this soup is lowkey really good I'm not gonna lie.\" You say with a mouthful of the thick delicious brown soup. \"I'm telling ya man these cooks need a raise, they're genuinly better than the AIs in our Quarters.\" " + friend_boy_name_1 + " responds cheerfully. Just as you start feeling relaxed.. \033[1VERRR VERRR ERROR IN REACTORS 2 & 7, PLEASE TAKE IMEDIATE ACTION, REPEAT, COOLING ERROR IN REACTORS 2 & 7, IMMEDIATE ACTION REQUIRED.\033[0m An alarm rings out.")
        print()
        fix_reactor = input("You look and your friend look at each other and with wide eyes, both get up and start sprinting to reactor #2 the closest one. \"Hey " + name + ", I got reactor 2, you go to 7, HURRY!\" " + friend_boy_name_1 + " yells. Will you go or stay with him. (Go/Stay): ")
        if fix_reactor == "Go" or fix_reactor == "go":
            print("\033[H\033[J", end="")
            input("You're now running as fast as you can physically push yourself, which is significantly faster than your average human, ~60km/h. You pass the 2 reactor room, and see " + friend_boy_name_1_nick + " run in. You take a few turns through the halls and eventually reach reactor 7. Once you are in the room your vision is met with tons of red warnings and errors on many different screens.")
            print()
            input("Somehow, for some inexplicable reason you know what do.. So you find the center console and a prompted.")
            print("\033[H\033[J", end="")
            while checksum == "Incomplete":
                input("\033[1m< --- USCS MORGAN SYSTEM AUTHENTICATION CHECKSUM --- >\033[0m")
                # I'm not gonna lie, I had to look up how these work, but basically, it's a lot of complex password math.
                # Whoever originally designed this system is genuinly a genius
                print()
                print()
                # collect initial inputs
                digit1 = int(input("Enter a digit 1-9: "))
                digit2 = int(input("Enter another digit 1-9: "))
                digit3 = int(input("Enter a 3rd digit 1-9: "))
                print()
                input("Validating..")
                
                # adds the OG digits
                checksum1 = digit1 + digit2 + digit3
                
                # splits the sum of the OG digits into 2 numbers if the need to be
                if checksum1 >= 10:
                    #10s place digit
                    special_digit1 = checksum1 // 10
                    #1s place digit         takes the 10s from the 1s to seperate 1s
                    special_digit2 = checksum1 - (special_digit1 * 10)
                    #final math
                    final_number = special_digit1 + special_digit2
                else:
                    final_number = checksum1
                
                if final_number == 6:
                    print()
                    score = score + round(round((50.0*score_multiplier)* 0.5), 1)
                    input("Successfully authenticated. PRESS ENTER TO CONTINUE")
                    checksum = "Complete"
                else:
                    print()
                    score = score - round(round((30.0*score_multiplier)* 0.5), 1)
                    input("\033[1mINVALID LOGIN KEYS. PLEASE RETRY\033[0m")
            print()
            input("\033[3mPhew.. Now that I'm logged in, it should be smooth sailing from here. Right?\033[0m Which would be true, if 2FA wasn't invented all the way back in 1967, " + str(int(canon_year) - 1967) + " years ago. \033[3m*sigh\033[0m You are prompted again.")
            print("\033[H\033[J", end="")
            while TwoFA == "Incomplete":
                # another puzzle very similar to the checksum
                input("\033[1m< --- USCS MORGAN 2FA AUTHENTICATION PERSISTANCE LOCK --- >\033[0m")
                print()
                print() # we can use the same variables to save time and space
                digit1 = int(input("Enter a number 1-9: "))
                digit2 = int(input("Enter another number 1-9: "))
                digit3 = int(input("Enter a 3rd number 1-9: "))
                print()
                input("Validating numbers..")
                
                checksum1 = digit1 * digit2 * digit3
                
                # now we use the checksume split again for some more fun..
                if checksum1 >= 10:
                    special_digit1 = checksum1 // 10
                    special_digit2 = checksum1 - (special_digit1 * 10)
                    # we use a different final number formula to change it even more
                    final_number = special_digit1 * special_digit2
                else:
                    final_number = checksum1
                
                # modulo filtering, very useful. Only multiples of 5 pass the 2FA because the only time final_number % 5 is 0 is when final_number is a multiple of 5    
                if final_number % 5 == 0 and final_number != 0:
                    print()
                    score = score + round(round((50.0*score_multiplier)* 0.5), 1)
                    input("\033[1mSYSTEM UNLOCKED\033[0m")
                    TwoFA = "Complete"
                else:
                    print()
                    score = score - round(round((30.0*score_multiplier)* 0.5), 1)
                    input("INCORRECT KEYS. TRY AGAIN")
            print("\033[H\033[J", end="")
            input("\033[3mNow that I'm fully logged in, I should be able to find the error and run a fix.\033[0m After the Complete text fades a large green button appears on the dashboard that says 'click to fix error'. \033[3mHow convient.\033[0m You think to yourself.")
            print()
            input("Over the ship announcement system, a message rings out. \033[1mCOOLING ERRORS IN REACTORS 2 & 7 HAVE BEEN RESOLVED. ALL REACTORS ARE NOW STABLE.\033[0m")
            print("\033[H\033[J", end="")
            if round(score) <= 870.0:
                input("Since your score is " + str(round(score)) + ", you get to move on to a less challenging story branch.")
                print("\033[H\033[J", end="")
                input("You go and run to the other reactor room where you last saw " + friend_boy_name_1 + ". \"BOO!\" You hear him yell behind you. \"Did I scare you??\" He asks slyly. You just stand there giving him a 'You're so dumb' look. \"Alright so not in the mood for jokes I see.. Anyways, I have an idea about where we can go.\" He says. \"Oh really?\" You reply with.")
                print()
                input(friend_boy_name_1 +" gets close and whispers in your ear. \"Yea, we can go grab a stealth craft from the hangar and go explore wherever we want.. Just you and me. Like the old days.\" \033[3mIs he crazy? That'll make us wanted criminals for stealing from a capital destroyer like this one..\033[0m")
                print()
                crazy_choice = input("Will you go with and steal a ship? (Yes/No): ")
                if crazy_choice == "Yes" or crazy_choice == "yes":
                    score = score + round(round((40.0*score_multiplier)*0.7), 1)
                    print()
                    input("\"You know what " + friend_boy_name_1_nick + ". I like it, I'm in. When do we leave?\" You ask. \"Now\" " + friend_boy_name_1 + " says, quickly answering your question. You both make some small talk as if the ship wasn't about to explode just 5 minutes ago and walk to Spacecraft Hangar 2 (Stealth Division).")
                    print()
                    input("Once you have both made it you realize the true scale of this place, it is utterly massive. \"Wow.\" You say, at a loss for words. \"Come on, lets get on this one.\" " + friend_boy_name_1 + " says, waving you after him as he walks ahead. You quickly follow and hop on the craft.")
                    print()
                    print()
                    input("\033[1m3 Hours Later.\033[0m")
                    print()
                    print()
                    input("After hours of silence, " + friend_boy_name_1 + " finally says something. \"Hey, " + name + " we're getting kinda low on fuel, I'm going to have to touch down on one of these planets and change out the ion batteries.\" \033[3mOf course we get delayed..\033[0m \"Alright.\" You reply. You eventually end up landing on this weird orange planet.")
                    print()
                    input("Weirdly enough, this weird orange planet is covered in weird mushrooms.. \"Yo " + friend_boy_name_1_nick + ", are you sure it's safe to get out of the ship here?\" You ask in an worried tone. He replies with, \"Should be fine.\" Unfortunatley for " + friend_boy_name_1_full + ", that's the last time he will ever speak any understandable language again.")
                    print()
                    input("\033[3mHe's been out there a long time, it shouldn't take this long to change some batteries, something must be wrong.\033[0m You hear a groan come from outside and that makes getting up to see what's happening irresistable..")
                    print()
                    mushroom_choice = input("Do you go and check? (Yes/No): ")
                    if mushroom_choice == "No" or mushroom_choice == "no":
                        ending = 2
                        score = score + 1000.0
                    elif mushroom_choice == "Yes" or mushroom_choice == "yes":
                        ending = 3
                        print()
                        input("You go outside to go and see what is taking so long when you see that he is rolling around on the floor babbling crazy. You feel your vision start to fade and blur.")
                elif crazy_choice == "No" or crazy_choice == "no":
                    score = score + round(round((35.0*score_multiplier)*0.7), 1)
                    print()
                    input("\"Bro, I'm not risking becoming a wanted person for fun.\" You say. \"Ughh, you used to be so fun..\" " + friend_boy_name_1 + " replies. You just roll your eyes and begin walking to your quarters. \"Have fun doing that without me!\" You say loudly as you walk away. \033[3mThat's that I guess..\033[0m")
                    print()
                    ending = 4
            elif round(score) > 870.0:
                input("Since your score is " + str(round(score)) + " you have lost the game.\nScore: " + str(round(score)))
        if fix_reactor == "Stay" or fix_reactor == "stay":
            ending = 3
        

if round(score) % 67 == 0 and score != 0:
    print("\033[H\033[J", end="")
    print()
    input("Secret Easter Egg ending, hehe your score is divisible by 67.")
    print()
    input("ok heres your real ending i'll stop being corny now..")

if ending == 1: # canon ending 1
    print("\033[H\033[J", end="")
    print()
    input("You took control of the ATWP and pushed back the opposing rebel force.")
    print()
    input("You win. Ending 1.\nScore: " + str(round(score)))
elif ending == 2: # canon ending 2
    print("\033[H\033[J", end="")
    print()
    input("You realize the the batteries are in fact full now, you call for your friend, when he doesn't answer you take off and fly back to the USCS Morgan to get help.")
    print()
    input("You win. You survived. Ending 2.\nScore: " + str(round(score)))
elif ending == 3: # death ending
    print("\033[H\033[J", end="")
    print()
    score = score - 1000.0 # cus if you died you gotta be smarter.
    input("You died, you either made a dumb decision or something dumb happened to you. GGs \nScore: " + str(round(score)))
elif ending == 4: # boring ending
    print("\033[H\033[J", end="")
    print()
    input("You lost, you were boring and went to your quarters and went to bed.\nScore: " + str(round(score)))
