# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Azazel", image="azazel")
define b = Character("Baphomet", image="baphomet")
define l = Character("Lilith", image="lilith")
define m = Character("Micah", image="micah", what_size=22) #smaller text size

# Backgrounds
image village = "BG/bg_village.png"
image village flashback = "BG/bg_village_flashback.png"
image altar = "BG/bg_altar.png"
image altar flashback = "BG/bg_altar_flashback.png"
#image cave room = "BG/bg_cave_room.png"
image sacrifice room = "BG/bg_sacrifice_room.png"
image sacrifice room flashback = "BG/bg_sacrifice_room_flashback.png"
# image sacrificeRoom flashback = "BG/bg_sacrificeRoom_flashback.png"

#Character images
image azazel neutral surprised = "Characters/Azazel/azazel neutral surprised.png"

image baphomet silhouette = "Characters/Baphomet/baphomet silhouette.png"
image baphomet masked = "Characters/Baphomet/baphomet mask.png"
image baphomet mask_cracked = "Characters/Baphomet/baphomet mask cracked.png"

image lilith masked = "Characters/Lilith/lilith mask.png"
image lilith masked angry = "Characters/Lilith/lilith mask angry.png"

image micah bandage angry = "Characters/Micah/micah bandage/micah angry.png"
image micah bandage annoyed = "Characters/Micah/micah bandage/micah annoyed.png"
image micah bandage neutral = "Characters/Micah/micah bandage/micah bandage neutral.png"
image micah bandage calm = "Characters/Micah/micah bandage/micah calm.png"
image micah bandage disturbed = "Characters/Micah/micah bandage/micah disturbed.png"
image micah bandage fearful = "Characters/Micah/micah bandage/micah fearful.png"
image micah bandage happy = "Characters/Micah/micah bandage/micah happy.png"
image micah bandage masked = "Characters/Micah/micah bandage/micah mask.png"
image micah bandage sacrifice = "Characters/Micah/micah bandage/micah sacrifice.png"
image micah bandage shock slash = "Characters/Micah/micah bandage/micah shock slash.png"
image micah bandage sickly = "Characters/Micah/micah bandage/micah sickly.png"

image micah no bandage angry = "Characters/Micah/micah no bandage/micah angry no bandage.png"
image micah no bandage annoyed = "Characters/Micah/micah no bandage/micah annoyed no bandage.png"
image micah no bandage calm = "Characters/Micah/micah no bandage/micah calm no bandage.png"
image micah no bandage disturbed = "Characters/Micah/micah no bandage/micah disturbed no bandage.png"
image micah no bandage fearful = "Characters/Micah/micah no bandage/micah fearful no bandage.png"
image micah no bandage happy = "Characters/Micah/micah no bandage/micah happy no bandage.png"
image micah no bandage neutral = "Characters/Micah/micah no bandage/micah no bandage neutral.png"
image micah no bandage sickly = "Characters/Micah/micah no bandage/micah sickly no bandage.png"

#Gallery images list, with placeholder images for now.
#Gallery based on this tutorial: https://www.youtube.com/watch?v=0hPIQxnesS8
#More on the gallery is found in screens.rpy and gamegallery.rpy.

#Some images need to be edited to fit the dimensions
#that the gallery uses.
default galleryList = ["azazel bad end",
                        "azazel bonus art 2",
                        "azazel bonus art 3",
                        "azazel bonus art 3 final",
                        "azazel bonus", 
                        "azazel pure evil end",
                        "game jam character mockups",
                        "micah mask pupils",
                        "splash art azazel bonus",
                        "splash art azazel"]
default Lightbox_image = "" #variable used by the gallery

#Change this to False before compiling and releasing.
#Turning it on lets the player see some testing features.
default script_testing_mode = True 

# The game starts here.

label start:
    #This sets the persistent variable for the gallery to false by default.
    #This means that the gallery will initially be locked,
    #but once you unlock it it will stay unlocked across playthroughs.
    default persistent.galleryUnlocked = False

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

    scene cave room with fade #We don't have a cave yet. This just shows a placeholder.

    show azazel neutral surprised at left:
        zoom 0.2

    show lilith masked at right:
        zoom 0.2

    "You awaken with a start in your own room."

    a neutral surprised "Ah! I'm up!"

    l "Finally. You'd be late to your own funeral if you could, Azazel."

    a neutral sheepish "I’m sorry, Madam Lilith. I thought it would be a quick nap…"

    l "No matter–our god forgives you. But there’s only a few hours until your sermon."
    l "You remember your lines, don’t you?"

    a neutral confused "Uh..."

    menu:
        "Could you refresh my memory?":
            l "Just this once. You must get the details correct, Azazel. Our god Baphomet will be watching."

        "I'm good.":
            l "The look on your face tells me you're not so sure."
            l "Remember, you must get the details correct, Azazel. Our god will be watching."

    l """
    Listen closely...
    
    {b}We, the citizens of the Order, are blessed to be under Baphomet's divine watch.{/b} 

    {b}We praise our god’s mercy and hear his word through his excellency, {color=#f00}The Prophet, Baphomet.{/color}{/b}

    {b}The Order is safe. The Order provides. The Order is {color=#f00}your home, your family, your everything.{/color}{/b}

    {b}To show our faith to Baphomet, our god, we cleanse our Order of the unclean through {color=#f00}the sacrifice of dissenters.{/color}{/b}

    Did you catch all of that, Azazel? I know it was a mouthful.
    """
    #{b}Text but {color=#f00}in RED.

    menu:
        "Yes, I will do my best.":
            l "I know you will. Make me and your Father proud."

        "I don't think I can do it...":
            l "Do not be afraid. The entire commune trusts and respects your word."
            l "I know you will succeed."

    "She pats the top of your head."

    a @ neutral very happy "Madam Lilith!"
    l "Forgive me, I couldn't help myself."
    a neutral happy "Hehe, our god forgives you."
    a neutral confused "By the way, I wanted to tell you something. I had a dream earlier."
    a neutral worried 'It seemed like a vision of my inauguration tomorrow… Father was in it. He said something about "my sacrifice".'
    a @ neutral confused "Don't get me wrong! I know it's a great honor to be the next Prophet."
    a neutral worried "I just can't help but feel like..."

    menu:
        "I don't deserve the honor.":
            l "Oh, no need to be so humble, Azazel. The people need a leader."
            l "Your sacrifice is merely a metaphor–growing into a new identity. And who better to embody that than you?"

        "Something will go wrong.":
            l "A nightmare, hm...?"
            l "Worry not, dreams and nightmares have no basis in reality, and only cast the mind astray. Our god knows best."

    l "Besides, our leader would never hurt you."
    l "You are his only son, after all."

    a neutral sheepish "Thank you... I'll keep your words in mind."

    l "No need to thank. And wait one moment before you go."
    "She pulls out a gift wrapped in white cloth and presents it to you"
    l "This is a sacrificial knife. It has been passed down by generations of Prophets. You will need it for the inauguration rituals."
    l "Take care not to tarnish it!"

    a @ neutral surprised "Thank you! I won't, Madam Lilith!"
    a "{i}This knife is so precious to the Order... this is real life.{/i}"
    a neutral base "{i}I really am about to become the next Prophet. {/i}"

    jump act2

    #l "Go help the citizens. I heard" #Is this line finished?

    #l masked angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}"

    return

label act2:
    #fade to black for 2 seconds before showing village
    #numbers: length of fade out, time to stay faded,
    #length of next fade-in, color
    scene village with Fade(0.5, 2, 0.5, color="#000")

    "You step outside of your quarters and meet the familiar sight of your mountainside home."
    "The Order’s flags and  banners wave proudly in the wind under the full moon’s light. The sky’s faraway stars twinkle."

    show azazel neutral happy at center:
        zoom 0.2

    a "It's good to get some fresh air..."
    a neutral calm "And everyone’s working hard to prepare for my crowning ceremony tomorrow. I should do something too."

    show azazel at left
    show micah bandage masked at right:
        zoom 0.2

    m "Azazel."
    a neutral surprised "Ah! Don't sneak up on me like that, Micah!"
    m "Yeah, sorry."
    m "I heard you muttering to yourself. Help me deliver today’s dinner rations. "
    a "That’s way too much bread and water to carry yourself… of course I’ll help!"
    m "You know I always get stuck with the hardest tasks."

    "The two of you spend the next few hours trudging across the sprawling cliffside, delivering rations to the citizens of the order. "

    a neutral confused "Huff... huff..."
    a neutral happy "Here's your food, sir!"

    #According to the script, "Citizen" should have annoyed and scared states.
    #Currently we just have one extra character sprite, so I used that for both emotions.
    show extra character at center:
        zoom 0.2
    "Citizen" "Oh, wow. The next Prophet himself shows up at my door, and dinner’s  still just a jug of water and half a loaf of hard bread."
    "Citizen" "What a gracious Lord! Thank you Baphomet! Jeez, I’m starving here… "

    a neutral surprised "Oh!"

    menu:
        "I’m sorry, I don’t have anything else…":
            $ moralityScore += 1
            # insert good sound effect

            a neutral sheepish "I can try to request something better for you tomorrow, maybe."
            "Citizen" "Oh, forget it… just from the way you talk, I know you’re just a naive little kid."
            "Citizen" "Listen. When you become Prophet, you better start making some big changes around here, alright?"
            a neutral worried "Ah, I will..."

        "Be grateful of what the Order provides.":
            $ moralityScore -= 1
            # insert bad sound effect

            a neutral annoyed "Is that really how you should be speaking to the next Prophet?"
            "Citizen" """
            Uh... my apologies!

            I was just saying I’d like to see some changes around here… I know you’ll be a great, um, leader.

            The bread’s actually fine. All hail! Haha…
            """

    hide extra character
    "The citizen disappears back into his residence."

    m "..."
    a neutral base "Hey, Micah, what do you think?"
    m "There's nothing to think."
    a neutral confused "What do you mean? What he said really bothered me…"
    a neutral sheepish "The Order does all it can to protect and provide for its people. And yet, that guy’s so rude!"
    a "He wants “big changes”… if Baphomet heard him, he would be in serious trouble."
    m "Azazel."
    m "Let’s pass out these last few rations and talk somewhere else."

    jump act2_altar

    return

label act2_altar:

    scene altar with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral base at left:
        zoom 0.2
    show micah bandage masked at right:
        zoom 0.2

    "After an arduous hike, the two of you reach a cliff. A simple altar made of three slabs of stone stands on the edge, waving red ribbons. The moon shines brightly in the sky."
    a "Why did you bring me here?"
    m "This is the only place where He isn't watching."
    a neutral confused "My Father? I mean- Baphomet?"
    m "Who else?"
    m bandage happy "Happy early 18th birthday, Azazel."
    m bandage calm "I know you’ll be busy tomorrow, with the inauguration and all. Thats why I wanted to say it now."
    a neutral overjoyed "Micah…! You’re so kind!"
    a neutral very happy "May our god bless you."
    m bandage annoyed "Our god..."
    m bandage neutral "Hey. We're friends, right?"
    m "Can you keep a secret?"

    show azazel neutral base

    menu:
        "Say what you want to say.":
            $ moralityScore -= 1
            # insert bad sound effect

            m bandage annoyed "..."
            "Micah scratches the bandages on their neck."
            m bandage angry "So you're going to tell everyone?"
            a neutral angry "I just have a bad feeling. The way you said \"our god\" ... it was so, {i}disdainful{/i}."
            m "What's your problem?"
            a neutral worried "Micah, you’re my friend and all, but if you’re trying to keep secrets from our god, he’s going to think you’re a dissenter."
            a neutral angry "Is that why you brought me all the way here? To speak ill of the Order?"
            m "Listen to me, Azazel! I'm risking my life here!"
            m bandage sickly "{i}*cough*{/i}"
            a neutral worried "Let's just go back, it's getting late-"
            m bandage annoyed "I'm not done."

        "Of course. You can trust me.":
            $ moralityScore += 1
            # insert good sound effect

            m "..."
            show micah no bandage neutral
            "Micah begins to unravel the tight bandages on their neck."
            a neutral surprised "What... is that..."
            m no bandage angry "It's the Order's symbol."
            m no bandage annoyed " There was never a good time to tell you this. But tomorrow, you’re going to become the next Prophet, and you deserve to know."
            m "Two years ago, I was reckless, just like that citizen complaining about rations earlier. And they did this to me."
            m no bandage sickly "It's a miracle I can still speak, really… the only reason I didn’t die was because I got on my knees and begged."
            a neutral worried "And who did this to you...?"
            m no bandage annoyed "Who else? Your father."
            a neutral horrified "No!"
            show micah bandage neutral
            "Micah puts their bandages back on."
            m bandage angry "I'm telling you the truth!"
            m bandage sickly "{i}*cough*{/i}"
            a neutral worried "Please, don't strain yourself-"

    m bandage annoyed "The Prophet tries so hard to keep everyone happy and satisfied through his sermons, but you know what?"
    m bandage angry "It doesn’t work. He’s a fraud. Everyone here is miserable!"
    #m "No one believes this is paradise. No one likes the prayers, or the masks, or the pitiful rations."
    #m "The few that {i}are{/i} happy are delusional. Everyone else just got dragged into the Order because we’re poor and vulnerable and didn’t know any better!"
    #m bandage neutral "...We're all just too afraid to say it."
    #m "We can't leave on our own... This cult garbage is fed into our minds 24/7 ... if we-"
    
    m "We’re forced to work, we don’t get paid, we can’t leave, and the food just sucks."
    m "People only joined the Order because of promises of safety and care... We were poor and vulnerable and didn't know any better."
    m bandage disturbed "We're all just too weak to escape."
    a neutral confused "{i}I think I hear someone approaching.{/i}"
    m bandage angry "And on another note. Don’t you think it’s suspicious that we call The Prophet by Baphomet’s name? As if he’s actually the god?"
    a "Hey, Micah-"
    m "He’s making us worship him, a man behind a mask. And if we have any little bad thing to say about it, we…!"
    a neutral horrified "SHH!"

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

    l masked angry "Do you have any idea how much trouble you two stirred up by disappearing?"
    l "You. Go back. Now."
    m "...Yes, ma'am."
    hide micah
    "They leave in a hurry."
    show lilith masked at right:
        zoom 0.2
    l "Hmph..."
    l "And what about you, young man? What do you have to say for yourself?"
    a neutral sheepish "I’m very sorry Madam Lilith, I was just passing out rations with Micah. And then we came here to talk..."
    l "You {i}know{/i} I told you to stop associating yourself with them. You don’t want to catch their voice sickness."
    l "What did you two talk about?"
    show azazel neutral base
    menu:
        "We just made small talk to catch up.":
            $ moralityScore += 1
            # insert good sound effect

            l @ masked angry "..."
            l "Your dishonesty does not go unnoticed, Azazel. I'm disappointed."
            a "{i}Shoot!{/i}"

        "They spoke ill of the Order and our god, Baphomet.":
            $ moralityScore -= 1
            # insert bad sound effect

            l "As I thought. Your honesty is appreciated."
            l "Micah may have been your friend, but they are no longer. Dissenters have no place in our Order."

    l "Your sermon is starting soon. Your Father and everyone else is waiting."
    l "Do not falter. Make us proud."

    jump act3_start

    #l masked angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}"

    return

label act3_start:

    scene sacrifice room with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral surprised at left:
        zoom 0.2
    show lilith masked at right:
        zoom 0.2

    "You step into a massive cavern, illuminated only by candlelight. A crowd of masked followers has congregated inside already."
    a "{i}I’ve never been allowed in here before, but this looks just like the room in my dream…{/i}"
    a "{i}I just got goosebumps.{/i}"
    l "Welcome, humble citizens of the Order. We come together tonight to celebrate the crowning of our next Prophet."
    l " " #Is she supposed to say something here?
    a "{i}I don't see Micah in the crowd.{/i}"
    a "{i}I don’t see Father either… isn’t he supposed to come and listen to my sermon?{/i}"
    l "Proceed, Azazel."
    a neutral calm "Yes, Madam Lilith."
    a "We, the citizens of the Order, are blessed to be under..."

    menu:
        "Baphomet's divine watch.":
            "The Crowd" "All hail Baphomet!" #no sprite shown

        "My divine watch.":
            "Citizen" "Huh...? Already?" #no sprite shown

    a neutral base "We praise our god’s mercy and hear his word through his excellency…"

    menu:
        "The Prophet.":
            "The Crowd" "All hail The Prophet!"

        "Madam Lilith.":
            l masked angry "This is not the time to be making jokes, Azazel!" (what_size=22)

    a "The Order is safe. The Order provides. The Order is…"

    menu:
        "Your home, your family, your everything.":
            "The Crowd" "All hail The Order!"
            show baphomet silhouette at center:
                zoom 0.2
            b " "

        "A huge sham!":
            $ moralityScore += 1
            # insert good sound effect
            show baphomet silhouette at center:
                zoom 0.2
            b "{b}That's enough out of you.{/b}"
            a neutral horrified "Father!"

    "The citizens of the Order bow in reverence."
    #show baphomet masked
    b masked "Your Prophet, the ordained messenger of your god, Baphomet."
    b "My son is an extraordinary being."

    l """
    {b}We, the citizens of the Order, are blessed to be under Baphomet’s divine watch.{/b}

    {b}We praise our god’s mercy and hear his word through his excellency, {color=#f00}The Prophet.{/color}{/b}

    {b}The Order is safe. The Order provides. The Order is {color=#f00}your home, your family, your everything.{/color}{/b}

    {b}To show our faith to Baphomet, our god, we cleanse our Order of the unclean through {color=#f00}the sacrifice of dissenters.{/color}{/b}

    {b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}
    """

    #Now that we're at the end, we can unlock the bonus content.
    $ persistent.galleryUnlocked = True

    #Not sure what's happening here yet.
    "{b}END{/b}"

    "{b}LEAD{/b}"

    "{b}LEAVE{/b}"

    return

label character_blurbs:
    #This is a scene that you'll be able to view from the main menu after completing the story.
    #It explains the background behind all the characters.
    #We can write better dialogue for it later.

    scene village flashback

    show azazel neutral base at center:
        zoom 0.2

    a "Hi, I'm Azazel!"
    a "*insert info about me here*"
    a "I love the order, they’re like a big family to me. I love my dad, Lady Lilith, and my best friend Micah!"

    hide azazel

    show lilith masked at center:
        zoom 0.2

    "This is Lady Lilith."
    "*info about Lilith here*"

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
            "Now you can see the gallery and character blurbs."
            jump debug_section

        "Lock postgame content" if persistent.galleryUnlocked:
            $ persistent.galleryUnlocked = False
            "You can no longer see the gallery or character blurbs."
            jump debug_section
        
        "Continue debug scene":
            "Showing debug scene."

    show azazel bad neutral at center:
        zoom 0.2

    a "Here's the debug scene."

    # $ persistent.galleryUnlocked = True

    return