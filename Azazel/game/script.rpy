# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Azazel", image="azazel")
define b = Character("Baphomet", image="baphomet")
define l = Character("Lilith", image="lilith")
define m = Character("Micah", image="micah", what_size=22) #smaller text size
define crowd = Character("Crowd", what_bold = True)
define extra = Character("Citizen", image = "extra character")

#Define audio files.
define audio.intense_action = "/audio/IntenseAction.ogg"
define audio.mellow_mood = "/audio/MellowMood.ogg"
define audio.less_mellow_mood = "/audio/LessMellowMood.ogg"
define audio.suspicious = "/audio/Suspicious.ogg"
define audio.neutral_ending = "/audio/Neutral_Ending.mp3"
define audio.good_ending = "/audio/Good_Ending.mp3"
define audio.knife_sfx = "/audio/KnifeSFX.ogg"

#Splash screens
image ending end cult = "/Splash/azazel good end splash art 1.png"
image ending lead cult transforming = "/Splash/azazel bad end splash art 1 transformation.png"
image ending lead cult micah = "/Splash/bad end splash art 2.png"
image ending lead cult azazel = "/Splash/azazel bad end splash art 1.png"
image ending escape cult = "/Splash/splash art azazel.png"

# Backgrounds
image altar = "BG/Altar.png"
image altar flashback = "BG/AltarFlashback.png"
image neighbor village = "BG/NeighborVillage.png"
image neighbor village flashback = "BG/NeighborVillageFlashback.png"
image room = "BG/Room.png"
image room flashback = "BG/RoomFlashback.png"
image sacrifice room = "BG/SacrificeRoom.png"
image sacrifice room flashback = "BG/SacrificeRoomFlashback.png"
image village = "BG/Village.png"
image village flashback = "BG/VillageFlashback.png"

#Character images
image azazel neutral gray = im.Grayscale("Characters/Azazel/azazel neutral base.png")
image azazel neutral surprised = "Characters/Azazel/azazel neutral surprised.png"
image azazel neutral base = "Characters/Azazel/azazel neutral base.png"
image azazel neutral happy = "Characters/Azazel/azazel neutral happy.png"
image azazel neutral calm = "Characters/Azazel/azazel neutral calm.png"
image azazel neutral cold = "Characters/Azazel/azazel neutral cold.png"
image azazel neutral horrified = "Characters/Azazel/azazel neutral horrified.png"
image azazel neutral annoyed = "Characters/Azazel/azazel neutral annoyed.png"
image azazel neutral angry = "Characters/Azazel/azazel neutral angry.png"
image azazel neutral confused = "Characters/Azazel/azazel neutral confused.png"
image azazel neutral overjoyed = "Characters/Azazel/azazel neutral overjoyed.png"
image azazel neutral sheepish = "Characters/Azazel/azazel neutral sheepish.png"
image azazel neutral veryhappy = "Characters/Azazel/azazel neutral very happy.png"
image azazel neutral worried = "Characters/Azazel/azazel neutral worried.png"
image azazel neutral teary angry  = "Characters/Azazel/azazel neutral teary angry.png"
image azazel neutral determined angry  = "Characters/Azazel/azazel neutral determined angry.png"
image azazel neutral disturbed = "Characters/Azazel/azazel neutral disturbed.png"
image azazel neutral teary = "Characters/Azazel/azazel neutral teary.png"
image azazel neutral eyes closed exhausted = "Characters/Azazel/azazel neutral eyes closed exhausted.png"
image azazel neutral meek = "Characters/Azazel/azazel neutral meek"

image azazel bad smile = "Characters/Azazel/azazel bad smile.png"
image azazel bad deranged = "Characters/Azazel/azazel bad deranged.png"
image azazel bad smirk eyes closed = "Characters/Azazel/azazel bad smirk eyes closed.png"
image azazel bad annoyed = "Characters/Azazel/azazel bad annoyed.png"
image azazel bad calm = "Characters/Azazel/azazel bad calm.png"
image azazel bad sneer = "Characters/Azazel/azazel bad sneer.png"
image azazel bad very happy = "Characters/Azazel/azazel bad very happy.png"
image azazel bad laughter = "Characters/Azazel/azazel bad laugh.png"
image azazel bad laugh = "Characters/Azazel/azazel bad laugh.png"

image azazel good angry = "Characters/Azazel/azazel good angry.png"
image azazel good base = "Characters/Azazel/azazel good base.png"
image azazel good calm = "Characters/Azazel/azazel good calm.png"
image azazel good cold = "Characters/Azazel/azazel good cold.png"
image azazel good determined = "Characters/Azazel/azazel good determined.png"
image azazel good disturbed = "Characters/Azazel/azazel good disturbed.png"
image azazel good happy = "Characters/Azazel/azazel good happy.png"
image azazel good horrified = "Characters/Azazel/azazel good horrified.png"
image azazel good overjoyed = "Characters/Azazel/azazel good overjoyed.png"
image azazel good very happy = "Characters/Azazel/azazel good very happy.png"
image azazel good worried = "Characters/Azazel/azazel good worried.png"

# transparent images for azazel
image azazel neutral transparent:
    "Characters/Azazel/azazel neutral base.png"
    alpha 0.5
image azazel neutral surprised transparent:
    "Characters/Azazel/azazel neutral surprised.png"
    alpha 0.5
image azazel neutral base transparent:
    "Characters/Azazel/azazel neutral base.png"
    alpha 0.5
image azazel neutral happy transparent:
    "Characters/Azazel/azazel neutral happy.png"
    alpha 0.5
image azazel neutral calm transparent:
    "Characters/Azazel/azazel neutral calm.png"
    alpha 0.5
image azazel neutral cold transparent:
    "Characters/Azazel/azazel neutral cold.png"
    alpha 0.5
image azazel neutral horrified transparent:
    "Characters/Azazel/azazel neutral horrified.png"
    alpha 0.5
image azazel neutral annoyed transparent:
    "Characters/Azazel/azazel neutral annoyed.png"
    alpha 0.5
image azazel neutral angry transparent:
    "Characters/Azazel/azazel neutral angry.png"
    alpha 0.5
image azazel neutral confused transparent:
    "Characters/Azazel/azazel neutral confused.png"
    alpha 0.5
image azazel neutral overjoyed transparent:
    "Characters/Azazel/azazel neutral overjoyed.png"
    alpha 0.5
image azazel neutral sheepish transparent:
    "Characters/Azazel/azazel neutral sheepish.png"
    alpha 0.5
image azazel neutral veryhappy transparent:
    "Characters/Azazel/azazel neutral very happy.png"
    alpha 0.5
image azazel neutral worried transparent:
    "Characters/Azazel/azazel neutral worried.png"
    alpha 0.5
image azazel neutral teary angry transparent:
    "Characters/Azazel/azazel neutral teary angry.png"
    alpha 0.5
image azazel neutral determined angry transparent:
    "Characters/Azazel/azazel neutral determined angry.png"
    alpha 0.5

image azazel bad smile transparent:
    "Characters/Azazel/azazel bad smile.png"
    alpha 0.5
image azazel bad deranged transparent:
    "Characters/Azazel/azazel bad deranged.png"
    alpha 0.5
image azazel bad smirk eyes closed transparent:
    "Characters/Azazel/azazel bad smirk eyes closed.png"
    alpha 0.5
image azazel bad annoyed transparent:
    "Characters/Azazel/azazel bad annoyed.png"
    alpha 0.5
image azazel bad calm transparent:
    "Characters/Azazel/azazel bad calm.png"
    alpha 0.5
image azazel bad sneer transparent:
    "Characters/Azazel/azazel bad sneer.png"
    alpha 0.5
image azazel bad very happy transparent:
    "Characters/Azazel/azazel bad very happy.png"
    alpha 0.5
image azazel bad laughter transparent:
    "Characters/Azazel/azazel bad laugh.png"
    alpha 0.5
image azazel bad laugh transparent:
    "Characters/Azazel/azazel bad laugh.png"
    alpha 0.5

image azazel good angry transparent:
    "Characters/Azazel/azazel good angry.png"
    alpha 0.5
image azazel good base transparent:
    "Characters/Azazel/azazel good base.png"
    alpha 0.5
image azazel good calm transparent:
    "Characters/Azazel/azazel good calm.png"
    alpha 0.5
image azazel good cold transparent:
    "Characters/Azazel/azazel good cold.png"
    alpha 0.5
image azazel good determined transparent:
    "Characters/Azazel/azazel good determined.png"
    alpha 0.5
image azazel good disturbed transparent:
    "Characters/Azazel/azazel good disturbed.png"
    alpha 0.5
image azazel good happy transparent:
    "Characters/Azazel/azazel good happy.png"
    alpha 0.5
image azazel good horrified transparent:
    "Characters/Azazel/azazel good horrified.png"
    alpha 0.5
image azazel good overjoyed transparent:
    "Characters/Azazel/azazel good overjoyed.png"
    alpha 0.5
image azazel good very happy transparent:
    "Characters/Azazel/azazel good very happy.png"
    alpha 0.5
image azazel good worried transparent:
    "Characters/Azazel/azazel good worried.png"
    alpha 0.5

image baphomet gray = im.Grayscale("Characters/Baphomet/baphomet mask.png")
image baphomet silhouette = "Characters/Baphomet/baphomet silhouette.png"
image baphomet masked = "Characters/Baphomet/baphomet mask.png"
image baphomet mask_cracked = "Characters/Baphomet/baphomet mask cracked.png"
image baphomet mask_cracked no pupil = "Characters/Baphomet/baphomet mask cracked no pupil.png"
image baphomet mask_cracked angry = "Characters/Baphomet/baphomet mask cracked angry.png"
image baphomet angry = "Characters/Baphomet/baphomet angry.png"

# transparent images for baphomet
image baphomet silhouette transparent:
     "Characters/Baphomet/baphomet silhouette.png"
     alpha 0.5
image baphomet masked transparent:
    "Characters/Baphomet/baphomet mask.png"
    alpha 0.5
image baphomet mask_cracked transparent:
    "Characters/Baphomet/baphomet mask cracked.png"
    alpha 0.5
image baphomet mask_cracked angry transparent:
    "Characters/Baphomet/baphomet mask cracked angry.png"
    alpha 0.5
image baphomet mask_cracked no pupil transparent:
    "Characters/Baphomet/baphomet mask cracked no pupil.png"
    alpha 0.5
image baphomet angry transparent:
    "Characters/Baphomet/baphomet angry.png"
    alpha 0.5

image lilith gray = im.Grayscale("Characters/Lilith/lilith mask.png")
image lilith masked = "Characters/Lilith/lilith mask.png"
image lilith masked angry = "Characters/Lilith/lilith mask angry.png"
image lilith broken_mask = "Characters/Lilith/lilith broken mask neutral.png"
image lilith broken_mask angry = "Characters/Lilith/lilith broken mask angry.png"

# lilith trnsparent
image lilith transparent:
    "Characters/Lilith/lilith mask.png"
    alpha 0.5
image lilith masked transparent:
    "Characters/Lilith/lilith mask.png"
    alpha 0.5
image lilith masked angry transparent:
    "Characters/Lilith/lilith mask angry.png"
    alpha 0.5
image lilith broken_mask transparent:
    "Characters/Lilith/lilith broken mask neutral.png"
    alpha 0.5
image lilith broken_mask angry transparent:
    "Characters/Lilith/lilith broken mask angry.png"
    alpha 0.5


image micah bandage gray = im.Grayscale("Characters/Micah/micah bandage/micah bandage neutral.png")
image micah bandage angry = "Characters/Micah/micah bandage/micah angry.png"
image micah bandage annoyed = "Characters/Micah/micah bandage/micah annoyed.png"
image micah bandage neutral = "Characters/Micah/micah bandage/micah bandage neutral.png"
image micah bandage calm = "Characters/Micah/micah bandage/micah calm.png"
image micah bandage disturbed = "Characters/Micah/micah bandage/micah disturbed.png"
image micah bandage fearful = "Characters/Micah/micah bandage/micah fearful.png"
image micah bandage happy = "Characters/Micah/micah bandage/micah happy.png"
image micah bandage masked = "Characters/Micah/micah bandage/micah mask.png"
image micah bandage relieved = "Characters/Micah/micah bandage/micah relieved.png"
image micah bandage sacrifice = "Characters/Micah/micah bandage/micah sacrifice.png"
image micah bandage shock slash = "Characters/Micah/micah bandage/micah shock slash.png"
image micah bandage sickly = "Characters/Micah/micah bandage/micah sickly.png"
image micah bandage sad= "Characters/Micah/micah bandage/micah sad.png"

image micah no bandage gray = im.Grayscale("Characters/Micah/micah no bandage/micah no bandage neutral.png")
image micah no bandage angry = "Characters/Micah/micah no bandage/micah angry no bandage.png"
image micah no bandage annoyed = "Characters/Micah/micah no bandage/micah annoyed no bandage.png"
image micah no bandage calm = "Characters/Micah/micah no bandage/micah calm no bandage.png"
image micah no bandage disturbed = "Characters/Micah/micah no bandage/micah disturbed no bandage.png"
image micah no bandage fearful = "Characters/Micah/micah no bandage/micah fearful no bandage.png"
image micah no bandage happy = "Characters/Micah/micah no bandage/micah happy no bandage.png"
image micah no bandage neutral = "Characters/Micah/micah no bandage/micah no bandage neutral.png"
image micah no bandage sickly = "Characters/Micah/micah no bandage/micah sickly no bandage.png"


# Micah Bandeges transparent images
image micah bandage angry transparent:
    "Characters/Micah/micah bandage/micah angry.png"
    alpha 0.5
image micah bandage annoyed transparent:
    "Characters/Micah/micah bandage/micah annoyed.png"
    alpha 0.5
image micah bandage neutral transparent:
    "Characters/Micah/micah bandage/micah bandage neutral.png"
    alpha 0.5
image micah bandage calm transparent:
    "Characters/Micah/micah bandage/micah calm.png"
    alpha 0.5
image micah bandage disturbed transparent:
    "Characters/Micah/micah bandage/micah disturbed.png"
    alpha 0.5
image micah bandage fearful transparent:
    "Characters/Micah/micah bandage/micah fearful.png"
    alpha 0.5
image micah bandage happy transparent:
    "Characters/Micah/micah bandage/micah happy.png"
    alpha 0.5
image micah bandage masked transparent:
    "Characters/Micah/micah bandage/micah mask.png"
    alpha 0.5
image micah bandage relieved transparent:
    "Characters/Micah/micah bandage/micah relieved.png"
    alpha 0.5
image micah bandage sacrifice transparent:
    "Characters/Micah/micah bandage/micah sacrifice.png"
    alpha 0.5
image micah bandage shock slash transparent:
    "Characters/Micah/micah bandage/micah shock slash.png"
    alpha 0.5
image micah bandage sickly transparent:
    "Characters/Micah/micah bandage/micah sickly.png"
    alpha 0.5


# Micah transparent with no bandages
image micah no bandage angry transparent:
    "Characters/Micah/micah no bandage/micah angry no bandage.png"
    alpha 0.5
image micah no bandage annoyed transparent:
    "Characters/Micah/micah no bandage/micah annoyed no bandage.png"
    alpha 0.5
image micah no bandage calm transparent:
    "Characters/Micah/micah no bandage/micah calm no bandage.png"
    alpha 0.5
image micah no bandage disturbed transparent:
    "Characters/Micah/micah no bandage/micah disturbed no bandage.png"
    alpha 0.5
image micah no bandage fearful transparent:
    "Characters/Micah/micah no bandage/micah fearful no bandage.png"
    alpha 0.5
image micah no bandage happy transparent:
    "Characters/Micah/micah no bandage/micah happy no bandage.png"
    alpha 0.5
image micah no bandage neutral transparent:
    "Characters/Micah/micah no bandage/micah no bandage neutral.png"
    alpha 0.5
image micah no bandage sickly transparent:
    "Characters/Micah/micah no bandage/micah sickly no bandage.png"
    alpha 0.5

# image for extra character
image extra character = "Characters/extra sprites/extra character.png"
image extra character scared = "Characters/extra sprites/extra character scared.png"
image extra character very scared = "Characters/extra sprites/extra character very scared.png"

# transparent image for extra character
image extra character transparent:
    "Characters/extra sprites/extra character.png"
    alpha 0.5
image extra character scared transparent:
    "Characters/extra sprites/extra character scared.png"
    alpha 0.5
image extra character very scared transparent:
    "Characters/extra sprites/extra character very scared.png"
    alpha 0.5

#Gallery images list, with placeholder images for now.
#Gallery based on this tutorial: https://www.youtube.com/watch?v=0hPIQxnesS8
#More on the gallery is found in screens.rpy and gamegallery.rpy.

#Some images need to be edited to fit the dimensions
#that the gallery uses.
default galleryList = ["character refs",
                        "azazel bad end splash art 1 (transformation)",
                        "azazel bad end splash art 1",
                        "azazel bad end",
                        "azazel bonus art 2",
                        "azazel bonus art 3",
                        "azazel bonus art 3 final",
                        "azazel bonus",
                        "azazel good end splash art 1 (transformation)",
                        "azazel pure evil end",
                        "bad end splash art 2",
                        "game jam character mockups",
                        "micah mask pupils",
                        "orderEndCongrats",
                        "so sorry micah",
                        "so sorry micah 2",
                        "splash art azazel bonus",
                        "splash art azazel"]
default Lightbox_image = "" #variable used by the gallery

default moralityScore = 0

init python:
    #These are function definitions, so I don't have to repeat the code
    #for changing variables and playing a sound whenever it happens.
    def gainGood():
        store.moralityScore += 1
        renpy.play("audio/GoodDecisionSFX.ogg", channel="sound")

    def gainBad():
        store.moralityScore -= 1
        renpy.play("audio/BadDecisionSFX.ogg", channel="sound")

#Makes it so unavailable choices still show.
#This is important for the ending menu where you see the final split.
define config.menu_include_disabled = True

#Set defaults for unlocking the different endings.
default persistent.galleryUnlocked = False
default persistent.ending_end_unlocked = False
default persistent.ending_escape_unlocked = False
default persistent.ending_lead_unlocked = False

#Change this to False before compiling and releasing.
#Turning it on lets the player see some testing features.
default script_testing_mode = False

# The game starts here.

label start:
    #This sets the persistent variable for the gallery to false by default.
    #This means that the gallery will initially be locked,
    #but once you unlock it it will stay unlocked across playthroughs.
    #default persistent.galleryUnlocked = False

    "Content warning: Death, blood"

    if script_testing_mode:
        menu:
            "What do you want to see?"

            "Script":
                jump script_intro

            "Debug":
                jump debug_section
    else:
        jump script_intro

    # This ends the game.

    return

label script_intro:
    $ moralityScore = 0

    scene altar flashback
    play music suspicious

    show baphomet silhouette at center:
        zoom 0.2

    "{i}Welcome, my friends. Tonight marks the dawn of a new age.{/i}"
    "{i}The time has come to crown our new Prophet.{/i}"
    "{i}Worry not, my child. Your sacrifice will not be in vain.{/i}"
    "{i}You will receive honor,  glory, and the divine blessing of our god, Baphomet.{/i}"

    show baphomet silhouette at left:
        zoom 0.2

    show azazel silhouette at right:
        zoom 0.2

    "{i}Cast aside your former name.{/i}"
    "{i}Cast aside your former skin, your former mind, body, and soul, and embrace your new identity.{/i}"
    "{i}{b}All hail our new Prophet!{/b}{/i}"
    "{i}{b}All hail Baphomet!{/b}{/i}"

    scene black with fade
    stop music

    #This is monologue mode, used for giving one character multiple repeated lines.
    "?" """
    Rise and shine, Azazel.

    Wake up.

    Oh, for Baphomet's sake...

    AZAZEL!
    """

    jump cave_wakeup


    return

label cave_wakeup:

    scene room with fade
    play music mellow_mood

    # show azazel neutral transparent
    #         show lilith transparent
    show azazel neutral transparent at left:
        zoom 0.2

    show lilith masked transparent at right:
        zoom 0.2

    "You awaken with a start in your own room."

    a @ neutral surprised "Ah! I'm up!"

    l @ masked "Finally. You'd be late to your own funeral if you could, Azazel."

    a @ neutral sheepish "I'm sorry, Madam Lilith. I thought it would be a quick nap..."

    l @ masked "No matter- our god forgives you. But there's only a few hours until your sermon."
    l @ masked "You remember your lines, don't you?"

    a @ neutral confused "Uh..."

    menu:
        "Could you refresh my memory?":
            $ gainGood()
            l @ masked "Just this once. You must get the details correct, Azazel. Our god Baphomet will be watching."

        "I'm good.":
            $ gainBad()
            l @ masked "The look on your face tells me you're not so sure."
            l @ masked "Remember, you must get the details correct, Azazel. Our god will be watching."

    l @ masked """
    Listen closely...

    {b}We, the citizens of the Order, are blessed to be under Baphomet's divine watch.{/b}

    {b}We praise our god's mercy and hear his word through his excellency, {color=#f00}The Prophet, Baphomet.{/color}{/b}

    {b}The Order is safe. The Order provides. The Order is {color=#f00}your home, your family, your everything.{/color}{/b}

    {b}To show our faith to Baphomet, our god, we cleanse our Order of the unclean through {color=#f00}the sacrifice of dissenters.{/color}{/b}

    Did you catch all of that, Azazel? I know it was a mouthful.
    """
    #{b}Text but {color=#f00}in RED.

    menu:
        "Yes, I will do my best.":
            $ gainBad()
            l @ masked "I know you will. Make me and your Father proud."

        "I don't think I can do it...":
            $ gainGood()
            l @ masked "Do not be afraid. The entire commune trusts and respects your word."
            l @ masked "I know you will succeed."

    "She pats the top of your head."

    a @ neutral very happy "Madam Lilith!"
    l @ masked "Forgive me, I couldn't help myself."
    a @ neutral happy "Hehe, our god forgives you."
    a @ neutral confused "By the way, I wanted to tell you something. I had a dream earlier."
    a @ neutral worried 'It seemed like a vision of my inauguration tomorrow... Father was in it. He said something about "my sacrifice".'
    a @ neutral confused "Don't get me wrong! I know it's a great honor to be the next Prophet."
    a @ neutral worried "I just can't help but feel like..."

    menu:
        "I don't deserve the honor.":
            l @ masked "Oh, no need to be so humble, Azazel. The people need a leader."
            l @ masked "Your sacrifice is merely a metaphor- growing into a new identity. And who better to embody that than you?"

        "Something will go wrong.":
            l @ masked "A nightmare, hm...?"
            l @ masked "Worry not, dreams and nightmares have no basis in reality, and only cast the mind astray. Our god knows best."

    l @ masked "Besides, our leader would never hurt you."
    l @ masked "You are his only son, after all."

    a @ neutral sheepish "Thank you... I'll keep your words in mind."

    l @ masked "No need to thank. And wait one moment before you go."
    "She pulls out a gift wrapped in white cloth and presents it to you"
    l @ masked "This is a sacrificial knife. It has been passed down by generations of Prophets. You will need it for the inauguration rituals."
    l @ masked "Take care not to tarnish it!"

    a @ neutral surprised "Thank you! I won't, Madam Lilith!"
    a neutral base "{i}This knife is so precious to the Order... this is real life.{/i}"
    a neutral base "{i}I really am about to become the next Prophet. {/i}"

    stop music
    jump act2

    #l "Go help the citizens. I heard" #Is this line finished?

    #l masked angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}"

    return

label act2:
    #fade to black for 2 seconds before showing village
    #numbers: length of fade out, time to stay faded,
    #length of next fade-in, color
    scene village with Fade(0.5, 2, 0.5, color="#000")
    play music mellow_mood

    "You step outside of your quarters and meet the familiar sight of your mountainside home."
    "The Order’s flags and  banners wave proudly in the wind under the full moon’s light. The sky’s faraway stars twinkle."

    show azazel neutral happy transparent at center:
        zoom 0.2

    a @ neutral happy "It's good to get some fresh air..."
    a neutral calm "And everyone's working hard to prepare for my crowning ceremony tomorrow. I should do something too."

    show azazel neutral calm transparent at left
    show micah bandage masked transparent at right:
        zoom 0.2

    m @ bandage masked "Azazel."
    a @ neutral surprised "Ah! Don't sneak up on me like that, Micah!"
    m @ bandage masked "Yeah, sorry."
    m @ bandage masked "I heard you muttering to yourself. Help me deliver today's dinner rations. "
    a @ neutral happy "That's way too much bread and water to carry yourself... of course I'll help!"
    m @ bandage masked "You know I always get stuck with the hardest tasks."

    "The two of you spend the next few hours trudging across the sprawling cliffside, delivering rations to the citizens of the order. "

    a @ neutral confused "Huff... huff..."
    a @ neutral happy "Here's your food, sir!"

    #We currently have just default extra character and extra character scared and very scared.
    #I just used the default to fill in for where extra character annoyed would be.
    #I also used extra character scared for surprised.
    show extra character at center:
        zoom 0.2
    extra "Oh, wow. The next Prophet himself shows up at my door, and dinner's  still just a jug of water and half a loaf of hard bread."
    extra "What a gracious Lord! Thank you Baphomet! Jeez, I'm starving here... "

    show extra transparent
    a @ neutral surprised "Oh!"

    menu:
        "I'm sorry, I don't have anything else...":
            $ gainGood()
            #Function that increases moralityScore and plays a sound.

            a @ neutral sheepish "I can try to request something better for you tomorrow, maybe."
            show extra character
            extra "Oh, forget it... just from the way you talk, I know you're just a naive little kid."
            extra "Listen. When you become Prophet, you better start making some big changes around here, alright?"
            show extra transparent
            a @ neutral worried "Ah, I will..."

        "Be grateful of what the Order provides.":
            $ gainBad()
            #Function that decreases moralityScore and plays a sound.

            a @ neutral annoyed "Is that really how you should be speaking to the next Prophet?"
            show extra character scared
            extra """
            Uh... my apologies!

            I was just saying I'd like to see some changes around here... I know you'll be a great, um, leader.

            The bread's actually fine. All hail! Haha...
            """

    hide extra
    "The citizen disappears back into his residence."

    m @ bandage masked "..."
    a @ neutral base "Hey, Micah, what do you think?"
    m @ bandage masked "There's nothing to think."
    a @ neutral confused "What do you mean? What he said really bothered me..."
    a @ neutral sheepish "The Order does all it can to protect and provide for its people. And yet, that guy's so rude!"
    a @ neutral sheepish "He wants \"big changes\"... if Baphomet heard him, he would be in serious trouble."
    m @ bandage masked "Azazel."
    m @ bandage masked "Let's pass out these last few rations and talk somewhere else."

    jump act2_altar

    return

label act2_altar:

    #Smoothly switch to the less-mellow music.

    #Get the current position of the track playing.
    #Set it to 0 by default if nothing's playing, then convert to string.
    $ currentTrackPosition = renpy.music.get_pos("music")
    if currentTrackPosition is None:
        $ currentTrackPosition = 0
    $ ctp_str = str(currentTrackPosition)
    #Sets up a string that plays the new track, starting where you left off and returning to the beginning each time through.
    #Cut parameters:  fadeout=0.6, fadein=0.6,
    $ renpy.music.play("<loop 0 from " + ctp_str + ">audio/LessMellowMood.ogg", tight=True)

    scene altar with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral base at left:
        zoom 0.2
    show micah bandage masked at right:
        zoom 0.2

    "After an arduous hike, the two of you reach a cliff. A simple altar made of three slabs of stone stands on the edge, waving red ribbons. The moon shines brightly in the sky."
    show micah bandage masked transparent
    a "Why did you bring me here?"
    show azazel neutral base transparent
    m @ -transparent "This is the only place where He isn't watching."
    a @ neutral confused "My Father? I mean- Baphomet?"
    m @ -transparent "Who else?"
    # hide micah bandage masked transparent
    show micah bandage transparent with fade:
        zoom 0.2
    m @ bandage happy "Happy early 18th birthday, Azazel."
    m @ bandage calm "I know you'll be busy tomorrow, with the inauguration and all. Thats why I wanted to say it now."
    a @ neutral overjoyed "Micah...! You're so kind!"
    a @ neutral very happy "May our god bless you."
    m @ bandage annoyed "Our god..."
    m @ bandage neutral "Hey. We're friends, right?"
    m @ bandage neutral "Can you keep a secret?"

    show azazel neutral base
    show micah bandage neutral transparent

    menu:
        "Say what you want to say.":
            $ gainBad()

            show azazel neutral base transparent
            m @ bandage annoyed "..."
            "Micah scratches the bandages on their neck."
            m @ bandage angry "So you're going to tell everyone?"
            a @ neutral angry "I just have a bad feeling. The way you said \"our god\" ... it was so, {i}disdainful{/i}."
            m @ bandage angry "What's your problem?"
            a @ neutral worried "Micah, you're my friend and all, but if you're trying to keep secrets from our god, he's going to think you're a dissenter."
            a @ neutral angry "Is that why you brought me all the way here? To speak ill of the Order?"
            m @ bandage angry "Listen to me, Azazel! I'm risking my life here!"
            m @ bandage sickly "{i}*cough*{/i}"
            a @ neutral worried "Let's just go back, it's getting late-"
            m @ bandage annoyed "I'm not done."

        "Of course. You can trust me.":
            $ gainGood()

            show azazel neutral base transparent
            m @ -transparent "..."
            show micah no bandage neutral with fade
            "Micah begins to unravel the tight bandages on their neck."
            show micah no bandage neutral transparent
            a @ neutral surprised "What... is that..."
            m @ no bandage angry "It's the Order's symbol."
            m @ no bandage annoyed " There was never a good time to tell you this. But tomorrow, you're going to become the next Prophet, and you deserve to know."
            m @ no bandage annoyed "Two years ago, I was reckless, just like that citizen complaining about rations earlier. And they did this to me."
            m @ no bandage sickly "It's a miracle I can still speak, really... the only reason I didn't die was because I got on my knees and begged."
            a @ neutral worried "And who did this to you...?"
            m @ no bandage annoyed "Who else? Your father."
            a @ neutral horrified "No!"
            show micah bandage neutral
            "Micah puts their bandages back on."
            show micah bandage neutral transparent
            m @ bandage angry "I'm telling you the truth!"
            m @ bandage sickly "{i}*cough*{/i}"
            a @ neutral worried "Please, don't strain yourself-"

    m @ bandage annoyed "The Prophet tries so hard to keep everyone happy and satisfied through his sermons, but you know what?"
    m bandage angry "It doesn't work. He's a fraud. Everyone here is miserable!"
    #m "No one believes this is paradise. No one likes the prayers, or the masks, or the pitiful rations."
    #m "The few that {i}are{/i} happy are delusional. Everyone else just got dragged into the Order because we're poor and vulnerable and didn't know any better!"
    #m bandage neutral "...We're all just too afraid to say it."
    #m "We can't leave on our own... This cult garbage is fed into our minds 24/7 ... if we-"

    m "We're forced to work, we don't get paid, we can't leave, and the food just sucks."
    m "People only joined the Order because of promises of safety and care... We were poor and vulnerable and didn't know any better."
    m bandage disturbed "We're all just too weak to escape."
    show micah bandage angry transparent
    a @ neutral confused "{i}I think I hear someone approaching.{/i}"
    m @ -transparent "And on another note. Don't you think it's suspicious that we call The Prophet by Baphomet's name? As if he's actually the god?"
    a @ -transparent "Hey, Micah-"
    m @ -transparent "He's making us worship him, a man behind a mask. And if we have any little bad thing to say about it, we...!"
    stop music

    a neutral horrified "SHH!"

    play music suspicious
    show micah bandage fearful

    show lilith masked at center:
        zoom 0.25
    #m bandage fearful "!"
    " "
    show lilith masked at center:
        zoom 0.2
    l "There you two are!"
    "Micah scrambles to put their mask back on."
    show micah bandage masked
    # l masked angry "..."
    # l "Azazel, we've been looking all over for you. Get some rest."

    show micah bandage masked transparent
    show azazel neutral horrified transparent
    l masked angry "Do you have any idea how much trouble you two stirred up by disappearing?"
    l "You. Go back. Now."
    show lilith masked angry transparent
    m @ -transparent "...Yes, ma'am."
    hide micah
    "They leave in a hurry."
    show lilith masked at right:
        zoom 0.2
    l "Hmph..."
    l "And what about you, young man? What do you have to say for yourself?"
    show lilith masked transparent
    a neutral sheepish "I'm very sorry Madam Lilith, I was just passing out rations with Micah. And then we came here to talk..."
    show azazel neutral sheepish transparent
    l @ -transparent "You {i}know{/i} I told you to stop associating yourself with them. You don't want to catch their voice sickness."
    l @ -transparent "What did you two talk about?"
    show azazel neutral base
    menu:
        "We just made small talk to catch up.":
            $ gainGood()

            show azazel neutral base transparent
            l @ masked angry "..."
            l @ -transparent "Your dishonesty does not go unnoticed, Azazel. I'm disappointed."
            a @ -transparent "{i}Shoot!{/i}"

        "They spoke ill of the Order and our god, Baphomet.":
            $ gainBad()

            show azazel neutral base transparent
            l @ -transparent "As I thought. Your honesty is appreciated."
            l @ -transparent "Micah may have been your friend, but they are no longer. Dissenters have no place in our Order."

    l @ -transparent "Your sermon is starting soon. Your Father and everyone else is waiting."
    l @ -transparent "Do not falter. Make us proud."

    stop music
    jump act3_start

    #l masked angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}"

    return

label act3_start:

    scene sacrifice room with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral surprised at left:
        zoom 0.2
    show lilith masked at right:
        zoom 0.2
    play music suspicious

    "You step into a massive cavern, illuminated only by candlelight. A crowd of masked followers has congregated inside already."
    show lilith masked transparent
    a "{i}I've never been allowed in here before, but this looks just like the room in my dream...{/i}"
    a "{i}I just got goosebumps.{/i}"
    show azazel neutral surprised transparent
    l @ -transparent "Welcome, humble citizens of the Order. We come together tonight to celebrate the crowning of our next Prophet."
    #The crowd character is marked to always speak in bold.
    crowd "Welcome, Azazel."
    a @ neutral happy "Hello, everyone."
    a @ neutral confused "{i}I don't see Micah in the crowd.{/i}"
    a @ neutral annoyed "{i}I don't see Father either... isn't he supposed to be here?{/i}"
    #l "Proceed, Azazel."
    l @ -transparent "Midnight marks his 18th birthday, and the start of his new journey as a leader to us all."
    l @ -transparent "We will begin tonight's inauguration with a sermon led by our god's next Prophet."
    crowd "We listen to your every word."
    l @ -transparent "You may begin."
    a neutral calm "Yes, Madam Lilith."
    a "We, the citizens of the Order, are blessed to be under..."

    menu:
        "Baphomet's divine watch.":
            show azazel neutral calm transparent
            crowd "All hail Baphomet!" #no sprite shown

        "My divine watch.":
            show azazel neutral calm transparent
            "Citizen" "Huh...? Already?" #no sprite shown

    a neutral base "We praise our god's mercy and hear his word through his excellency..."

    menu:
        "The Prophet.":
            show azazel neutral base transparent
            crowd "All hail The Prophet!"

        "Madam Lilith.":
            show azazel neutral base transparent
            l @ masked angry "This is not the time to be making jokes, Azazel!" (what_size=22)

    a neutral base "The Order is safe. The Order provides. The Order is..."

    menu:
        "Your home, your family, your everything.":
            $ gainBad()
            show azazel neutral base transparent
            crowd "All hail The Order!"
            show baphomet silhouette at center:
                zoom 0.2
            b "You have done well, my lamb."
            show baphomet silhouette transparent
            a @ neutral very happy "Father!"

        "A huge sham!":
            $ gainGood()
            show azazel neutral base transparent
            show baphomet silhouette at center:
                zoom 0.2
            b "{b}That's enough out of you.{/b}"
            show baphomet silhouette transparent
            a @ neutral horrified "Father!"

    "The citizens of the Order bow in reverence."
    #show baphomet masked
    crowd "We are blessed to be in your presence, Baphomet."
    b @ masked """
    Your Prophet, the ordained messenger of your god, has arrived.

    His excellency, Baphomet, speaks through me. He sees you, he hears you, and he loves you. My words are his words, as his are mine.

    But alas, the time for renewal is now. Tonight marks the dawn of a new age!

    Eighteen long years I have raised and cherished my son. The ears and horns on his head are a mark of him being blessed by our god.

    I have no doubts that he will be the most powerful Prophet in the history of our Order.
    """

    crowd "*murmur*"

    a @ neutral base "..."

    #We don't have angry Baphomet.
    b @ angry "Azazel. Finish the sermon."

    a @ neutral annoyed "To show our faith to Baphomet, our god, we cleanse our Order of the unclean through..."

    menu:
        "The sacrifice of dissenters.":
            $ gainBad()
            crowd "Purge the dissenters!"
            a @ neutral overjoyed "{i}I did it!{/i}"

        "...":
            $ gainGood()
            b @ "The sacrifice of dissenters."
            crowd "..."
            a @ neutral sheepish "{i}Father is gonna kill me.{/i}"

    show azazel neutral base transparent
    l masked "Let us continue with the ceremony."
    l "As tradition of the Prophet's inauguration, we hold a special sacrifice. This honor would usually be bestowed upon an elder in our community, who has served the Order long and well."
    l masked angry "However, tonight, no such honor exists. Because our new Prophet cannot be crowned while the unclean run free amongst our ranks."
    show lilith masked transparent
    "The crowd collectively gasps."
    a @ neutral horrified "{i}They're changing the ceremony?{/i}"
    l @ masked "Speaking ill of our god, Baphomet, is {b}an unforgivable act.{/b} I hope that you have not all forgotten all that our god has done for us. Without him, your lives would all fall to ruin."
    l @ masked "Tonight, Azazel will be upholding our promise of faith to Baphomet through the cleansing of a dissenter. With the sacrifice of their poor, broken soul, we shall crown our new Prophet, and the Order shall prevail!"
    "The crowd cheers."
    l @ masked "Bring the dissenter in."

    #Rearrange some characters so you can see all five at once.
    show baphomet silhouette:
        xalign 0.75
    show extra character at center:
        xalign 0.25
        zoom 0.2
    show micah bandage sickly at center:
        zoom 0.2
    show azazel neutral horrified
    show lilith masked

    play music intense_action

    a neutral horrified "Micah!"

    show baphomet silhouette transparent
    show extra character transparent
    show azazel neutral horrified transparent
    show lilith masked transparent
    m "Azazel..."

    show micah bandage sickly transparent
    l masked "Two years ago, this traitor here was found stealing rations from our stock."
    l "We, as the Order, provide food and home for you all. This greed was unfounded."
    l "The food that this dissenter stole could have been the rations that your own family were to receive."

    show lilith masked transparent
    "A cacophony of angry gasps erupt from the crowd."

    m @ bandage angry "I was {i}starving!{/i} One piece of bread per day isn't-"
    l @ masked angry "{b}Quiet.{/b}"
    m @ bandage fearful "...!"
    l @ masked "Two years ago, we spared the life of this dissenter. We believed in giving them a chance to prove their loyalty once more."
    l @ masked angry "But we were wrong."
    l @ masked "The traitor before you today was spreading hate about our god, attempting to misguide the next Prophet."
    m @ bandage disturbed "...."
    l @ masked angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak. They must be purged from our Order.{/b}"
    b @ masked "Azazel. Come forth."
    #a neutral horrified "Fath- Lord Baphomet..."
    b @ masked "Raise the sacrificial knife, and rid us of the poison that plagues the Order."
    "The citizen pushes Micah in front of Azazel. The crowd goes silent in anticipation, eagerly awaiting the coming sacrifice."
    m @ bandage fearful "Azazel... don't..."
    l @ masked angry "{b}SILENCE!{/b}"
    m @ bandage sickly "..."
    #a "B-but… Lord Baphomet… why Micah..? They’re my friend…"
    a @ disturbed "Wait, Lord Baphomet, please- Micah is my friend!"
    b @ masked """
    A traitorous rebel who can't learn a simple lesson is no friend of yours.

    This dissenter has strung you along for long enough. It's time they've learned their lesson.

    And what more of an honor is it to be sacrificed in the name of our god, during the most important ceremony of this generation?

    You are about to become the next Prophet, the highest honor anyone could bestow upon you. Are you really worthy of that title if you are unable to sacrifice one lowly dissenter?

    Proceed.
    """

    "You take a deep breath, and pull out the sacrificial knife."
    show azazel neutral annoyed

    jump ending_choice_menu

    return

label ending_choice_menu:

    if script_testing_mode:
        menu:
            "Which ending do you want to see?"

            "Lead cult":
                jump ending_lead_cult

            "Escape cult":
                jump ending_escape_cult

            "End cult":
                jump ending_end_cult

            "See end from regular game":
                pass

    menu:
        "I understand my duty." if moralityScore <= -5:
            jump ending_lead_cult

        "I would like to negotiate." if moralityScore > -5 and moralityScore < 5:
            jump ending_escape_cult

        "I refuse." if moralityScore >= 5:
            jump ending_end_cult

    return

label ending_end_cult:
    $ persistent.ending_end_unlocked = True
    "You cast aside the sacrificial knife. It clatters against the floor."
    show azazel neutral angry transparent

    #a "end cult"
    a @ neutral angry "What honor is it to murder my friend in cold blood? It’s not just!"
    # a @ neutral angry "I won't kill them."
    # l @ masked angry "..."
    m bandage relieved "Azazel...!" #Do we have a "relieved"?
    show micah bandage relieved transparent
    "{i}Hundreds of voices speak up in protest.{/i}"
    # b @ -transparent "..."
    # b @ -transparent "Azazel."
    "Citizen 1" "He’s ruining the ceremony! KILL THE DISSENTER!"
    "Citizen 2" "Just hurry up and sacrifice them already!"
    "Citizen 3" "Phew, thank god..."
    a @ neutral angry "The members of the Order have a right to voice complaints and concerns! How is it so wicked to want a better life? How blasphemous is it to want to sleep with a full stomach?"
    a @ neutral angry "If the Order promises to care and provide, it {i}should!{/i}"
    b @ angry "{b}SILENCE!{/b}"
    show baphomet angry transparent
    "{i}Your Father storms towards you. You instinctively take a step back.{/i}"
    b @ masked -transparent "You are hysterical. Your mind has already been tainted with lies and deception."
    b @ angry -transparent "Destroy the source. It is the only way to save your soul."
    #We don't seem to differentiate between "teary angry" and "determined angry".
    a @ neutral angry "I refuse."
    b @ masked -transparent "You do not have a choice. Sacrifice them."

    a @ neutral teary angry "I refuse!"
    show azazel neutral teary angry transparent
    b @ masked -transparent "You {b}will{/b} become my successor. You are the face of the Order."
    a @ neutral angry "...Then I don't want to be anymore."
    show azazel neutral angry transparent
    b @ angry -transparent "{b}Unacceptable.{/b}"
    "{i}Before you can react, your Father's hand thrusts out and clenches around Micah's neck. He lifts them up into the air.{/i}"
    b @ angry -transparent "If you refuse to get rid of this pest, then I will do it myself."
    m @ bandage fearful "*cough*"
    a @ neutral horrified "They can't breathe! Let them go!"
    b @ angry -transparent "The mercy given to you two years ago was undeserved. May our god have mercy on your wicked soul."
    a @ neutral teary angry "{b}STOP IT!{/b}"
    menu:
        "Tackle Baphomet":
            "You lunge at your Father, but he is much taller and stronger than you. You tug on his robes desperately."
            b @ angry -transparent "Azazel! You are embarrassing yourself!"
            a @ neutral angry determined "Put them down! They're going to die!"
            b @ angry -transparent "You have failed the ceremony at every step. This is my last effort to redeem you. Stand down."
            m @ bandage fearful "H... help...!"
            a @ neutral horrified "{i}Micah!{/i}"
            "You struggle against your Father, punching, kicking, doing everything you could in a last ditch attempt to save your friend."
            b @ mask_cracked "{b}ENOUGH!{/b}"
            show baphomet mask_cracked transparent
        "Pick up the knife":
            "You lunge for the sacrificial knife and point it against your Father. "
            a @ neutral angry determined "Don't move!"
            show baphomet masked transparent
            b @ masked -transparent "You brat...! You dare raise a weapon against a god?!"
            m @ bandage fearful "H.. help...!"
            play sound knife_sfx
            pause
            "Your friend is released from being choked."
            m @ bandage sickly "..."
            a @ neutral horrified "...F-Father, I-"
            b @ mask_cracked -transparent "{b}Get over here.{/b}"
            show baphomet mask_cracked transparent
            a @ neutral horrified "{i}I broke his mask!{/i}"
            "Your Father, normally so well-spoken and composed in the eyes of the Order, is consumed with indignant rage. He grabs you by the collar."
            b @ mask_cracked -transparent "I found you, I {i}raised{/i} you-and this is how you repay me, Azazel? I am your Father! {b}Your god!{/b}"
            b @ mask_cracked -transparent "You are a disgrace to the Order! A disgrace to me!"

    "Your father violently kicks you in the gut. You fall to the floor."
    "A loud snapping noise reverberates throughout the entire cavern."
    "*CRACK*"

    # play music mellow_mood
    scene ending end cult
    pause

    "{i}What... happened?{/i}"
    "{i}My horn? I broke my horn!{/i}"
    "The horrified crowd watches."
    "Citizen 1" "The Prophet beat his own son! I can’t watch any longer..."
    "Citizen 2" "Oh god, look at his horn... and why is his hair white?"
    "Citizen 3" "Hang in there, Azazel!"
    scene sacrifice room with Fade(0.5, 2, 0.5, color="#000")
    "You cradle your broken horn in your hands."
    show azazel good disturbed transparent at right:
        zoom .2
    show micah bandage sickly transparent at left:
        zoom .2

    a @ good disturbed "{i}Everything hurts...{/i}"
    m @ bandage sickly "You risked yourself to save my life..."
    m @ bandage relieved "*cough* You're a hero..."
    a @ good disturbed "I don’t think it’s not over yet."
    "The two of you turn towards the Prophet, expecting him to be looming over the two of you."
    "Surprisingly, he is facing away, head bowed, clutching his face."
    # hide azazel good disturbed transparent
    hide micah bandage sickly transparent
    show baphomet mask_cracked transparent at center:
        zoom 0.2
        yalign 1.0
    b @ mask_cracked -transparent "My mask..."
    "The crowd becomes unruly."
    "Citizen 1" "What? The Prophet’s mask broke? I thought he was supposed to be a manifestation of Baphomet..."
    "Citizen 2" "He was so crazy and unhinged today. I always knew he felt like a fraud."
    "Citizen 3" "Down with the Order!"
    crowd "{b}False Prophet! False Prophet! False Prophet!{/b}"
    b @ mask_cracked angry "H-how dare you? Dissenters, all of you! Your god Baphomet commands you to stop!"
    "A crowd member throws a stone at him, and the crowd roars. Lilith steps in for damage control."
    crowd "{b}GET OUT OF HERE!{/b}"

    hide baphomet mask_cracked transparent
    show azazel good disturbed transparent at center:
        zoom .2
    show baphomet mask_cracked transparent at right:
        zoom 0.2
        yalign 1.0
    show lilith masked transparent at left:
        zoom 0.2
        yalign 1.0

    l @ masked "Baphomet. For the sake of the Order, I suggest you leave. Their frustrations will not be quelled by words alone today."
    b @ mask_cracked no pupil "No."
    b @ mask_cracked "I refuse to let it end like this. I refuse. This ceremony was supposed to be perfect."
    b @ mask_cracked angry "But you...! Azazel! You ruined everything!"
    a @ good horrified "!"
    l @ masked angry "Don’t hit your son again!"
    "{b}SLAP{/b}"
    show lilith broken_mask angry with dissolve
    show lilith broken_mask angry transparent
    l @ broken_mask angry "...How unbecoming of you."
    "She cradles her aching face. Pieces of her mask crumble away."
    b @ mask_cracked "Why do you protect him so vehemently? Why do you coddle him so?"
    b @ mask_cracked "He is {i}my{/i} son."
    l @ broken_mask angry "Perhaps I consider him mine as well."
    b @ mask_cracked angry "You witch!"
    l @ broken_mask angry "You could never understand...!"
    "She holds him off. A handful of brave citizens rush to help her restrain the disgraced Prophet."

    b @ mask_cracked angry "Ugh...!"
    l broken_mask """
    Micah, Azazel.

    I don't agree with all of what you said. But I understand where you two are coming from, and I trust you.

    You are the new leader of the Order. Make a speech together, and decide its fate.
    """

    show lilith broken_mask transparent
    a @ good eyes closed "...Okay. I understand."
    a @ good base "Micah, are you okey now?"
    m "Haha... you can do most of the talking. I believe in you. Speak from the heart."
    a @ good determined "I will."

    hide lilith
    hide baphomet

    play music mellow_mood
    show azazel at center
    a @ good determined "Everyone!"
    a @ good worried "Tonight, you all have witnessed something very uncomfortable. I know it must have been difficult for all of us."
    a @ good cold "Today's events have shined a light on a terrible truth. The truth that the Order is corrupt and imperfect."
    a @ good worried "I grew up in this place, and I grew up happy, in blissful ignorance. Now, I see how cruel this place really was."
    a @ good determined "As a result, I have decided that there will be no new Prophet."
    a good happy "However... if you all are willing, it would be my honor to be your leader."
    show azazel good happy transparent
    crowd "*positive murmur*"
    "Citizen 1" "We trust in you!"
    "Citizen 2" "I can help!"
    a @ -transparent "Right! We will work together, towards freedom. As a community."
    a @ good determined "Let's mark today as the dawn of a new age. You can cast aside your former shackles, and embrace your new identity."
    a @ -transparent "For the new and better Order!"
    "You raise up your broken horn. The crowd cheers."
    show micah bandage relieved transparent at left:
        zoom .2
    show lilith broken_mask transparent at right:
        zoom .2

    m @ -transparent "Good job."
    l @ -transparent "I will support you."
    a good happy "Our next plan of action is to..."

    menu:
        "Find a new home.":
            a good determined "We will spend the next few weeks making preparations to leave this place."
            a "Outside, there must be a much better world to see... we will finally be free from this mountain."

        "Restructure what we have here.":
            a good determined "We will spend the next few months rebuilding what we have."
            a "We will agree on a fairer, less harsh set of community rules to abide by. And we will venture out from the commune to other places to forage and trade."

    a good happy "That's... all the ideas I have for now. I'm sure we can do it though!"
    show azazel good happy transparent
    crowd "Azazel! Azazel! Azazel!"
    a @ good very happy "{i}They're chanting for me...! It worked out!{/i}"
    l @ -transparent "There's just one last order of business."

    show azazel:
        xalign 0.33
    show baphomet mask_cracked angry transparent:
        zoom .2
        xalign 0.66
        yalign 1.0

    b @ -transparent "..."
    l @ -transparent "As the new community leader, his fate lies in your hands."
    l @ -transparent "What will you do with your Father?"

    show azazel good calm
    menu:
        "Let's rehabilitate him.":
            a "I believe in second chances."
            a "Despite all of the pain you've caused, and the damage you've done to all of us, you are still my Father."
            a good determined "You might call me naive, or weak-hearted, but I believe that you truly wanted the best for me and the rest of the community."
            a "If you are willing… I would love for you to stay."
            show azazel good determined transparent
            b @ -transparent """
            ...

            Who... taught you to act this way?

            This mercy... it's weak. It's pitiful.
            """
            a @ -transparent "I still want you by my side, Father."
            b mask_cracked no pupil "..."
            b "Very well. I will think about it."
            show baphomet mask_cracked no pupil transparent
            a @ good overjoyed "Phew...!"

        "Lock him up.":
            a good angry "Father... I never realized how power hungry and cruel you were until today."
            a "You never took my feelings into consideration. You expected me to kill my best friend like it was nothing, and you hurt all of us... even Madam Lilith."
            a "You do not deserve to be free. You will only cause more pain unto others."
            a good worried "However... you also do not deserve to die."
            a good base "I hope you live long and remain healthy, and take the time to reflect upon your mistakes."
            a good happy "That is the mercy you deserve. Because after everything… you’re still the man who raised me."
            show azazel good base transparent
            b mask_cracked no pupil "..."
            b "My own son sentencing me to prison... how disappointing."
            b "I no longer wish to speak to you. Do what you will."
            show baphomet mask_cracked no pupil transparent
            a @ good worried "{i}I expected as much...{/i}"

    l @ broken_mask "You've done a phenomenal job, Azazel. I'm proud of you."
    m @ bandage relieved "We're finally going to be free. You're the best."
    a good very happy "I couldn't have done it without you two... thank you for trusting me."
    a good overjoyed "Alright everyone, let's get out of this creepy room and celebrate!"


    scene village
    play music good_ending
    """
    Your unwavering determination and strength has set your people free from the chains of Baphomet.

    The people of your community look up to you for guidance. They adore you.

    Your friends and family are alive and well.

    Your sacrifice was not in vain. Your courage to fight back brought honor, glory, and the blessing of the people unto you.

    Soon, your people will venture out from the mountains to explore the outside world. They will be happy and free.

    The future of the New Order is bright.

    Congratulations!
    """

    #play music mellow_mood
    scene ending end cult
    pause
    scene pure good end
    pause
    #scene

    jump after_finishing


    #old script
    show azazel neutral angry transparent
    #a "end cult"
    a @ neutral angry "I won't kill them."
    l @ masked angry "..."
    m bandage calm "Azazel...!" #Do we have a "relieved"?
    show micah bandage calm transparent
    "Hundreds of voices speak up in protest."
    b @ -transparent "..."
    b @ -transparent "Azazel."
    "He takes a step towards Azazel, reaching out a hand."
    b @ -transparent "Come on, now. Everyone is watching. You are too old to be throwing tantrums."
    #We don't seem to differentiate between "teary angry" and "determined angry".
    a @ neutral teary angry "NO!"
    a @ neutral determined angry "Micah is my friend. I'm not going to hurt them."
    b @ -transparent "Azazel..."
    b @ -transparent "Did I ever say you had a choice?"
    a @ -transparent "!" #We don't have "disturbed"
    "He takes another step forward."
    b @ -transparent "You {b}must{/b} be my successor. You are the face of the Order."
    a @ -transparent "...I don't want to be."
    b @ -transparent "..."
    b @ -transparent "{b}Azazel.{/b}" #we don't have Baphomet angry
    "Baphomet rushes towards Azazel, gripping the sacrificial knife and pulling it out of his hands."
    a neutral horrified "Father, no!"
    show azazel neutral horrified transparent
    b @ -transparent "If you refuse to get rid of this pest, then I will take the responsibility and do it myself. Your sermon will have to wait."
    m @ -transparent "No... please wait... I don't want to die... I'm sorry..."
    a @ -transparent "Father, don't-"
    b @ -transparent "You must learn how to be a leader, Azazel."
    "Baphomet holds the knife over Micah's cowering form."
    a @ neutral teary angry "{b}STOP IT!{/b}"
    "Azazel runs towards Baphomet, attempting to grab the knife, but Baphomet shoves him away. He hits the floor with a thud."
    "A loud snapping noise reverberates throughout the entire cavern."

    return

label ending_lead_cult:
    $ persistent.ending_lead_unlocked = True
    show azazel neutral cold transparent
    show micah bandage fearful transparent

    a @ -transparent "This is the end, Micah."
    "Although his face is covered by a mask, you can sense your Father is smiling."
    m @ -transparent "Hey! You said we were friends... come on, you don't have to do this!!"
    a @ -transparent "No, now I realize the truth. In fact, I'm disappointed I didn't realize sooner."
    a neutral angry "You only befriended me to try and sway me from my path. And to protect yourself from your doomed fate!"
    a "You have been a dissenter for years. But you managed to stay under the radar by tricking me into being your friend, so I would be reluctant to kill you."
    show azazel neutral angry transparent
    m @ bandage disturbed "What's gotten into you? None of that is true! *cough*"
    m @ bandage sad "...I just didn't want to be alone anymore. I didn't trick you into anything, I promise."
    a @ -transparent "No. You spoke out against our god. You stole, you lied, and you even spoke ill of The Prophet, my Father, straight to my face."
    a neutral cold "You almost successfully swayed me from my path, and barred me from my rightful position. You truly are the most clever mutineer I've ever seen."
    a "But a liar's promise holds no weight. May our god Baphomet have mercy upon your soul."
    show azazel neutral cold transparent
    m @ -transparent "Azazel... you sound just like your father."

    #show the transformation splash art
    play music suspicious
    show ending lead cult transforming
    window hide #hides the text box
    pause
    #hide ending lead cult transforming
    window auto #returns the text box
    """
    You feel a sinister change within you. For the first time in years, you remember that you are not human.

    You are a symbol of the Order. A blessing born from Baphomet's might as a god.

    This is the sacred honor you were told to bear.
    """

    hide ending lead cult transforming
    show azazel bad smile transparent
    show micah bandage fearful transparent

    a @ -transparent "Where was I again? Ah, yes. I {i}am{/i} just like my Father."
    a @ -transparent "Members of the Order, feast your eyes on your next Prophet!"
    a @ bad deranged "It's truly an honor to lead this ceremony. You all are about to witness history."
    m @ -transparent "Who are you?!"
    a @ bad eyes closed smirk "How silly. A change in demeanor and you cannot even recognize me anymore."
    a @ bad annoyed "Just as I cannot recognize you anymore, either."
    a @ bad cold "You used to be Micah- friendly, quiet, and obedient. Now look at you. A lowly dissenter, aiming to ruin my inauguration."
    a @ bad calm "I have let go of all former reservations. Let us commence the sacrifice!"
    m @ -transparent "N-no... this can't be happening... snap out of it, please!"
    a @ bad sneer "I refuse."
    "You raise your sacrificial knife, letting it be seen by the crowd. Micah struggles desperately against their restraints."
    a @ bad smirk eyes closed "Citizens of the Order, do you feel blessed to be under Baphomet's divine scrutiny? Our god invites you to celebrate this sacrifice! This blade is a symbol of his righteousness!"
    a @ bad sneer "Show your faith to me, everyone, as we cleanse the unclean, and purge the scum of the earth. Speak!"
    crowd "All hail the next Prophet!"
    a @ bad deranged "Louder!"
    crowd "ALL HAIL!"
    a @ bad laugh "Hahaha!"
    m @ bandage sickly "{i}He's gone completely insane.{/i}"
    a bad very happy "Now, Micah..."
    menu:
        "Return to your creator.":
            pass
        "God rest your wicked soul.":
            pass

    scene ending lead cult micah
    pause
    scene ending lead cult azazel
    pause
    play sound knife_sfx
    show black with fade
    pause

    hide black
    scene sacrifice room
    show azazel bad laughter transparent at left:
        zoom 0.2
    show micah bandage sacrifice transparent at center:
        zoom 0.2
    show baphomet masked transparent at right:
        zoom 0.2
    m @ -transparent "....."
    "The dissenter collapses. They could not utter any last words."
    "Half of the crowd cheers. The rest watch in disturbed horror."
    a @ bad smirk eyes closed "Are half of you asleep? The evil has been purged. Applaud, applaud!"
    crowd "*CLAP* *CLAP* *CLAP*"
    a @ bad laugh "Wonderful!"
    b @ masked "Wonderful indeed. You have done well, my son."
    a @ bad overjoyed "I know!"
    b @ masked "..."
    b @ masked "Now that the sacrifice is complete, it is finally time to officially crown our new Prophet. It is my honor to bestow upon you this sacred role, and I trust you will serve our community with strength and vigor."
    show azazel bad sneer
    menu:
        "I will.":
            show azazel bad sneer transparent
            b masked "You are a son I can be proud of."

        "Sure, old man!":
            show azazel bad sneer transparent
            b masked "...Okay then."

    "Father" """
    As Prophet, you will relay the divine word you hear from our god Baphomet, and borrow his sacred name. You work to uphold the peace and prosperity of the Order, and keep the community's faith in you strong and absolute.

    Cast aside your former name. Your name is now Baphomet.

    Cast aside your former skin, your former mind, body, and soul, and embrace your new identity. Your identity is now our god.

    Citizens of the Order- bow to your new leader!
    """

    show baphomet masked transparent

    crowd "All hail our new Prophet!"
    crowd "ALL HAIL BAPHOMET!"

    show azazel silhouette

    """
    The clock strikes 12.

    Happy birthday...

    Baphomet.

    The Order is in your hands.
    """

    scene pure evil end
    pause

    #to be continued uwu

    jump after_finishing
    return

label ending_escape_cult:
    $ persistent.ending_escape_unlocked = True
    show azazel neutral worried transparent

    #a "escape cult"

    b @ angry "There is no negotiation."
    "The knife in your hand trembles as the crowd grows restless."
    a neutral worried "Wait! I don't mean to offend anyone. Please, understand..."
    a "Micah has been my friend since I can remember. We grew up together. There is absolutely no way they can be a dissenter."
    a neutral surprised "They just, uh... misspoke! That's right!"
    a neutral confused "Real dissenters are wicked and cruel, and sway others easily. But I was not swayed by their words at all."
    a neutral sheepish "As the next Prophet, I suggest we extend some lenience towards-"
    show azazel neutral sheepish transparent
    b @ angry "{b}Enough. Our god is not pleased with you.{/b}"
    a @ neutral horrified "{i}He's mad!{/i}"
    b @ -transparent "You've delayed the ceremony enough. The dissident {i}must{/i} be sacrificed. Kneel them down in the circle."
    m @ bandage angry "...!"
    a neutral horrified "{i}I'm out of time! I need to think of something!{/i}"
    menu:
        "Who hasn't said a few blasphemous words, right?":
            a neutral surprised "Hear me out! I mean, just earlier today I heard this man complaining about rations!"
            show azazel neutral angry transparent
            crowd "*anxious chattering*"
            extra character @ very scared "Uh..."

        "I know of another dissenter.":
            crowd "*gasp*"
            a neutral angry "That's right. In fact... it's that man right there!"
            show azazel neutral angry transparent
            extra character @ very scared "What?"
            crowd "*loud murmuring*"
            a @ cold "He complained about the rations, saying he expected special treatment tonight."

    a @ angry "He said it all sarcastically, like \"Thanks Baphomet,\" and \"What a gracious god.\""
    a @ neutral worried "And I thought in my head, wow, how ungrateful... after all the effort I went through delivering food to everyone!"
    extra character @ very scared "Hey, where's your proof? I didn't say any of that!"
    a @ neutral cold "Only dissenters lie. Are you calling me a liar?"
    extra character @ very scared "Tch..."
    b @ masked "Very well then. A new dissenter will be cleansed. May his wicked soul no longer defile our precious Order and our god's name."
    show azazel neutral base transparent
    a @ neutral surprised "{i}That actually worked?!{/i}"
    b @ masked "After all, this is a sacred trial for our next Prophet. The subject is of little importance. The strength lies in his will and blade."
    a @ neutral meek "Oh, yes, of course."
    a @ neutral worried "{i}I bought Micah some time, but now I roped this guy into things! I'm sorry, bread guy...{/i}"
    "The dissenter is dragged to the center of the circle, in place of Micah."
    extra character @ very scared "Please, I didn’t mean anything! I’ll never speak ill of anyone again! All hail!"
    "You raise the sacrificial knife."
    show azazel neutral angry transparent
    a @ neutral cold "In the name of our god, Baphomet, I will prove my faith... may he have mercy on your soul."
    play sound knife_sfx
    a @ neutral cold "..."
    extra character @ scared "...?"
    "The sacrificial knife's blade is stuck in the ground."
    a @ neutral disturbed "{i}I missed!{/i}"
    show azazel neutral surprised transparent
    b @ angry """
    {b}That's enough!{/b}

    You have failed the ceremony at every step. I gave you every opportunity to redeem yourself, and yet, you failed.

    I am ashamed to present our god with such a weak-hearted son.

    You are a disappointment.
    """

    a @ neutral disturbed "I... I'm..."
    m @ bandage angry "Let's go!"
    "They suddenly grab your hand, and the two of you make a run for it."
    a @ neutral teary "MICAH!"
    b @ angry "STOP THEM!"

    scene village with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral teary at left:
        zoom 0.2
    show micah bandage disturbed transparent at right:
        zoom 0.2
    a @ neutral teary "Where are we going?"
    m @ bandage disturbed "Away."
    show azazel neutral teary angry transparent
    a @ neutral angry teary "Micah, I have to complete the ceremony!"
    a @ neutral angry teary "Father is right, I've been completely useless. I need to do {i}something{/i}. I'll kill that dissenter to save you."
    m @ bandage pleading "Forget that, keep running! They're catching up!"
    a @ neutral teary "I just wanted to tell you that you're right... this place is horrible. I don't know why I never did anything about it."
    a @ neutral teary "I should have known sooner. I lived here my whole life."
    m @ bandage relieved "Hey. Azazel, it's okay."
    m @ bandage relieved "You're just a kid. It's not your fault."
    a @ neutral sheepish "Mm..."
    a @ neutral surprised "Wait-"
    a @ neutral horrified "BEHIND YOU!"

    play sound knife_sfx
    m bandage shock slash "!"
    m bandage sacrifice "Damn... it..."
    "They fall to their knees, clutching their deep wound. Their tormentor looms behind them, clutching the bloodstained sacrificial knife."
    show baphomet mask_cracked transparent:
        zoom 0.2
        xalign 0.33
        yalign 1.0

    show lilith masked transparent:
        zoom 0.2
        xalign 0.66
        yalign 1.0

    show azazel neutral horrified transparent
    show micah sacrifice transparent

    b @ -transparent "{b}Here is the fate of all who dare oppose our god.{/b}"
    a @ -transparent "M... Micah..."
    a @ neutral angry teary "AH! AHH!"
    show azazel neutral teary angry transparent
    m @ -transparent """
    *cough*

    Azazel... You have to make it... you have to get away...

    Run... forget about me...
    """

    a @ neutral angry teary "No! I can't leave you behind..."
    b @ -transparent "{b}Return to my side now.{/b}"
    a neutral teary angry "*cough* Now...!"
    menu:
        "Run away":
            show azazel neutral teary transparent
            "You break into a frenetic run, wiping the stinging tears on your face."

        "Stay with Micah":
            show azazel neutral teary transparent
            m @ -transparent "You idiot..."
            m @ -transparent "What's the point if we both get caught? *cough*"
            a @ -transparent "Don’t die... I’ll take you to the infirmary, I’ll do anything!"
            m @ -transparent "I was supposed to- *cough* -protect you..."
            m @ -transparent "Azazel... be... free..."
            a @ neutral horrified "..."
            "Their breathing goes still."
            "You scramble to your feet and break into a frenetic run, wiping the stinging tears on your face."

    hide azazel
    show baphomet at left
    show lilith at right
    show micah at center
    b @ -transparent "AZAZEL! I DEMAND YOU TO STOP!"
    show lilith broken_mask transparent
    l @ -transparent "Do not chase after him."
    b @ -transparent "Why do you too oppose me? Has everyone lost their minds?"
    l @ -transparent """
    Baphomet. Azazel is not fit to be Prophet. He was still too young to see all of this.

    Let him go. He will return when he is wiser.

    Our people are confused and worried. Let us return and quell their fears, as we always have.
    """
    b @ -transparent "..."
    b @ -transparent "You have always loved him, haven't you?"
    l @ -transparent "I am only saying what's best for the Order."
    b @ -transparent "..."
    b @ -transparent "Very well. Have it your way."

    scene black with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral eyes closed exhausted at center:
        zoom 0.3
    """
    You have been running for hours.

    Through unfamiliar slopes and valleys, your legs carried you away, fueled by nothing but fear.

    Your mind is numb.

    Your heart is numb.

    Your body is numb.
    """

    play music less_mellow_mood
    scene neighbor village
    show azazel neutral base at center:
        zoom 0.2

    """
    By daybreak, you stumble upon another village for the first time. You collapse from exhaustion.

    The worried citizens see a stranger dressed in strange robes with peculiar ears and horns. They have the kindness and mercy to take you in.
    """

    #We don't have a flashback of the neighboring village, but we do have one for the original village.
    scene neighbor village
    play music neutral_ending
    """
    {i}Your indecisiveness has costed you everything.{/i}

    {i}You have abandoned your friends, your family, and the place you called home.{/i}

    {i}Your future is uncertain.{/i}

    {i}But at least you have escaped with your life... you are now free, unfettered.{/i}

    {i}It is the dawn of a new age.{/i}

    {i}Cast aside your former name.{/i}

    {i}Cast aside your former skin, your former mind, body, and soul, and embrace your new identity.{/i}

    {i}Welcome to the outside world.{/i}
    """


    scene ending escape cult
    pause
    scene neutral end
    pause

    jump after_finishing
    return

label after_finishing:
    #Now that we're at the end, we can unlock the bonus content.
    # $ persistent.galleryUnlocked = True
    $ numberOfEndingsUnlocked = 0
    if persistent.ending_end_unlocked:
        $ numberOfEndingsUnlocked += 1
    if persistent.ending_lead_unlocked:
        $ numberOfEndingsUnlocked += 1
    if persistent.ending_escape_unlocked:
        $ numberOfEndingsUnlocked += 1

    if numberOfEndingsUnlocked == 3:
        $ persistent.galleryUnlocked = True
        $ endingsInfoString = "You have seen all endings.\nMake sure to check the gallery in the main menu!"
    else:
        $ endingsInfoString = "You have unlocked " + str(numberOfEndingsUnlocked) + " out of 3 endings.\nPlay again to see the rest!"

    #scene black
    call screen credits
    return

screen credits:
    frame:
        xalign 0.5 #center it
        yalign 0.5

        background Solid("#ffffffe0") #white that's a little transparent
        padding(50, 50)

        #image("./gui/Credits.png")
        vbox:
            xalign 0.5
            yalign 0.9
            text("Thank you for playing The Order of Baphomet!")
            text("Made for Jam-O-Lantern 2022")
            text("\nCredits:")
            text("Programming: @Miles Blumenau, @LittleRookey")
            text("Writing: @IcebergCabbage")
            text("Background Art: @Meh")
            text("Character Art: @oto")
            text("Sound Effects: @Ben Slattery")
            text("Music: @Ben Slattery, @Winterestr")
            text("\n[endingsInfoString]")
            textbutton _("Finish") action MainMenu(confirm=False, save=False)


label character_blurbs:
    #This is a scene that you'll be able to view from the gallery after completing the story.
    #It explains the background behind all the characters.

    scene village flashback

    show azazel neutral happy at center:
        zoom 0.2

    a @ neutral overjoyed "Hi, My name's Azazel. Thank you for coming on this journey with me."
    a @ neutral happy "It's been a long day. I'm sure you have lots of questions. I hope I can answer just a few."
    a @ neutral base "Let's see..."
    a @ neutral very happy "For starters, I'll tell you about myself!"
    a @ neutral happy "I am the next Prophet of the Order of Baphomet."
    a @ neutral meek "Well... I was going to be the next Prophet, but things didn't really go to plan, did they?"
    a @ neutral sheepish "..."
    a @ neutral base "Well, let's not dwell on that."
    a @ neutral happy "Umm... Let's see..."
    a @ neutral overjoyed "Micah is my best friend! We go way back."
    a @ very happy "We would always play together when we were younger. I was never bored when they were around."
    a @ neutral confused "Two years ago, something changed, though... They became really quiet and snappy."
    a @ neutral surprised "But that's okay! People are allowed to change!"
    a @ neutral very happy "I would never leave them behind. I'll be by their side, no matter what."
    a @ neutral happy "I know they would do the same for me."
    a @ neutral base "Let's see... who else... oh, of course!"
    a @ neutral very happy "I love my family. Lilith has always been like a mother to me. She always made sure I was happy and safe."
    a @ neutral happy "Father wasn't home very often. He was busy, so she watched over me. I don't know where I'd be without her."
    a @ neutral confused "When I was little, she would even tuck me into bed at night. Kind of embarrassing, looking back on it."
    a @ neutral eyes closed exhausted "And... Father always took care of me, when she wasn't around."
    a @ neutral eyes closed exhausted "He never missed one of my birthdays, at least."
    a @ neutral calm "...He could be a good person, sometimes."

    hide azazel

    show baphomet masked at center:
        zoom 0.2

    b @ masked "You..."
    b @ masked angry "Thanks to you, everything I've built up has fallen into ruin."
    b @ masked angry "Let's make this quick. I can't stand looking at you."
    b @ masked "I am Baphomet. Our god speaks through me, and chose me to lead the Order."
    b @ masked angry "Do not disrespect our god. Without them, we would be nothing."
    b @ masked "My son has been my greatest accomplishment. A powerful being, destine to take my place as the Prophet."
    b @ masked "He is truly remarkable."
    b @ masked angry "...Unlike that lowly dissenter who he believes to be his friend. I should have gotten rid of them before it was too late."
    b @ maked angry "Now, I must go. Dare you show your face around here again, and I will make sure that you regret it."

    hide baphomet

    show lilith masked at center:
        zoom 0.2

    l @ masked "Greetings. Thank you for joining us. My name is Lilith."
    l @ masked "I simply want the best for Azazel. Our god tasked me with raising him to be the next Prophet."
    l @ masked "I would do whatever it takes to keep him safe."
    l @ masked "..."
    l @ masked "Hmm? You'd like to know more about me?"
    l @ masked "Well, there's not much to say. I live for our god. Thanks to him, I have a peaceful life."
    l @ masked "I have been with the Order for many years. Before being saved, I was a lost soul, living on the streets, ousted by my family and left to fend for myself."
    l @ masked "That was when Lord Baphomet found me and took me in. I owe him my life."
    l @ masked "My loyalty to the Order is what led me to my current standing. Our god believes in me. He chose me for this task."
    l @ masked angry "Lay a hand on Azazel, and I'll make sure your next breath is your last."

    hide lilith

    show micah bandage neutral at center:
        zoom 0.2

    m @ bandage neutral "Thanks for watching over Azazel. My name's Micah."
    m @ bandage annoyed "Although... You had to make some bad decisions to get here. How do you think I felt about that, huh?"
    m @ bandage annoyed "It's kind of painful, you know. Getting stabbed. Twice. By two different people."
    m @ bandage annoyed "...Anyways."
    m @ bandage neutral "I got caught stealing a few years ago, so I was marked as a dissenter."
    m @ bandage sad "The scars on my neck are proof of that. It sucks, but at least I'm still alive."
    m @ bandage neutral "I couldn't tell Azazel, or they'd get rid of me. If I wanted to keep being friends with him, I had to keep my mouth shut."
    m @ bandage calm "I was okay with that. He's my best friend, so.. I put up with it."
    m @ bandage happy "We've spent our whole lives together, anyways."
    m @ bandage relieved "I mean, it's not like I had anyone else, haha... I was poor and always had to do the chores for everyone."
    m @ bandage sad "It was lonely. But Azazel always kept me company, so I put up with it. I was happy when I got to hang out with him."
    m @ bandage neutral "..."
    m @ bandage annoyed "What, do you want me to say more?"
    m @ bandage angry "Don't bring up Baphomet. He's a horrible man. He's brainwashed everyone else into believing he was some sort of god, but not me."
    m @ bandage angry "Lilith, too. She was completely captivated. All she did was make sure that Azazel never saw the horrible things his father was doing."
    m @ bandage angry "It's all thanks to those two that all of this happened!"
    m @ bandage sickly "...cough."
    m @ bandage sad "...Please don't make me talk about them any more than that."

    return

label debug_section: #A part of the game I made just to test stuff out.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ moralityScore = 0

    scene village

    menu:
        "Do what?"

        "Jump to a scene":
            menu:
                "Jump to where?"

                "Opening scene (Act 1)":
                    jump script_intro

                "Cave wake-up (Act 1)":
                    jump cave_wakeup

                "Act 2 opening":
                    jump act2

                "Act 2 altar":
                    jump act2_altar

                "Act 3":
                    jump act3_start

                "Return to main debug menu":
                    jump debug_section

        "Unlock postgame content" if not persistent.galleryUnlocked:
            $ persistent.galleryUnlocked = True
            $ persistent.ending_end_unlocked = True
            $ persistent.ending_escape_unlocked = True
            $ persistent.ending_lead_unlocked = True
            "Now you can see the gallery and character blurbs."
            jump debug_section

        "Lock postgame content" if persistent.galleryUnlocked:
            $ persistent.galleryUnlocked = False
            $ persistent.ending_end_unlocked = False
            $ persistent.ending_escape_unlocked = False
            $ persistent.ending_lead_unlocked = False
            "You can no longer see the gallery or character blurbs."
            jump debug_section

        "Continue debug scene":
            pass

    show azazel bad neutral at center:
        zoom 0.2

    #a "Here's the debug scene."

    #l "...What was it that he said, again? \"He's a fraud.\" Yes, that was it."

    # $ persistent.galleryUnlocked = True

    show azazel neutral surprised at left:
        zoom 0.2

    show lilith masked at right:
        zoom 0.2

    menu:
        "Test which option for faded-out characters?"

        "Gray":
            show azazel neutral gray
            show lilith gray

        "Transparent":
            show azazel neutral transparent
            show lilith transparent

    "You awaken with a start in your own room."

    a @ neutral surprised "Ah! I'm up!"

    l @ masked "Finally. You'd be late to your own funeral if you could, Azazel."

    a @ neutral sheepish "I’m sorry, Madam Lilith. I thought it would be a quick nap..."

    l @ masked "No matter–our god forgives you. But there’s only a few hours until your sermon."
    l @ masked "You remember your lines, don’t you?"

    a @ neutral confused "Uh..."

    return
