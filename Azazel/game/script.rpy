# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Azazel", image="azazel")
define b = Character("Baphomet", image="baphomet")
define l = Character("Lilith", image="lilith")
define m = Character("Micah", image="micah", what_size=22)

# Backgrounds
image village = "BG/bg_village.png"
image village flashback = "BG/bg_village_flashback.png"
image altar = "BG/bg_altar.png"
image altar flashback = "BG/bg_altar_flashback.png"

#We can add character definitions later if we want to permanently apply an effect
#like zoom to a character.
#I skipped that for now.
image baphomet silhouette = "Characters/Baphomet/baphomet silhouette.png"
image lilith masked = "Characters/Lilith/lilith mask.png"
image lilith masked_angry = "Characters/Lilith/lilith mask angry.png"
image micah masked = "Characters/Micah/micah mask.png"
image azazel neutral surprised = "Characters/Azazel/azazel neutral surprise.png"

#Gallery images list, with placeholder images for now.
#Gallery based on this tutorial: https://www.youtube.com/watch?v=0hPIQxnesS8
#More on the gallery is found in screens.rpy and gamegallery.rpy.

#Some images need to be edited to fit the dimensions
#that the gallery uses.
default galleryList = ["azazel bonus art 2",
                        "azazel bonus art 3",
                        "azazel bonus", 
                        "game jam character mockups",
                        "micah mask pupils",
                        "splash art azazel bonus",
                        "splash art azazel"]
default Lightbox_image = "" #variable used by the gallery

# The game starts here.

label start:
    #This sets the persistent variable for the gallery to false by default.
    #This means that the gallery will initially be locked,
    #but once you unlock it it will stay unlocked across playthroughs.
    default persistent.galleryUnlocked = False

    menu:
        "What do you want to see?"

        "Script":
            jump script_intro

        "Debug":
            jump debug_section

    # This ends the game.

    return

label script_intro:
    scene altar flashback

    show baphomet silhouette at center:
        zoom 0.2

    "{i}Welcome, my friends. Tonight marks the dawn of a new age.{/i}"
    "{i}The time has come to crown our new Prophet.{/i}"
    "{i}Worry not, my child. Worthy is the lamb who is slain.{/i}"
    "{i}You will receive honor,  glory, and the divine blessing of our Lord.{/i}"

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

    scene cave with fade #We don't have a cave yet. This just shows a placeholder.

    show azazel neutral surprise at left:
        zoom 0.2

    show lilith masked at right:
        zoom 0.2

    "You awaken with a start in your own room."

    a "Ah! I'm up!"

    l "Finally. You'd be late to your own funeral if you could, Azazel."

    a sheepish "I’m sorry, Madam Lilith. I thought it would be a quick nap…"

    l "No matter–the Lord forgives you. But there’s only a few hours until your sermon."
    l "You remember your lines, don’t you?"

    a surprise "Uh..."

    menu:
        "Could you refresh my memory?":
            l "Just this once. You must get the details correct, Azazel. Our Lord will be watching."

        "I'm good.":
            l "The look on your face tells me you're not so sure."
            l "Remember, you must get the details correct, Azazel. Our Lord will be watching."

    l """
    Listen closely...
    
    {b}We, the citizens of the Order, are blessed to be under His divine watch.{/b} 

    {b}We praise our Lord’s mercy and hear His word through his excellency, {color=#f00}The Prophet, Baphomet.{/color}{/b}

    {b}The Order is safe. The Order provides. The Order is {color=#f00}your home, your family, your everything.{/color}{/b}

    {b}To show our faith to Baphomet and our Lord, we cleanse our Order of the unclean through {color=#f00}the sacrifice of dissenters.{/color}{/b}

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
    a neutral happy "Hehe, the Lord forgives you."
    a neutral base "By the way, I wanted to tell you something. I had a dream earlier."
    a neutral worried "It seemed like a vision of my inauguration tomorrow… I think Father was in it. He said something about sacrificing a lamb."
    a @ neutral sheepish "Don't get me wrong! I know it's a great honor to be the next Prophet."
    a "I just can't help but feel like..."

    menu:
        "I don't deserve the honor.":
            l "Oh, no need to be so humble, Azazel. The people need a leader."
            l "The sacrifice of a lamb is merely a metaphor–growing into a new identity. And who better to embody that than you?"

        "Something will go wrong.":
            l "A nightmare, hm...?"
            l "Worry not, dreams and nightmares have no basis in reality, and only cast the mind astray. Our Lord knows best."

    l "Besides, our leader Baphomet would never hurt you."
    l "You are his only son, after all."

    a neutral sheepish "Thank you... I'll keep your words in mind."

    l "No need to thank. And wait one moment before you go."
    l "This is a sacrificial knife. It has been passed down by generations of Prophets. You will need it for the inauguration rituals."
    l "Take care not to tarnish it!"

    a @ neutral surprise "Thank you! I won't, Madam Lilith!"
    a "{i}This knife is so precious to the Order... this is real life.{/i}"
    a neutral base "{i}I really am about to become the next Prophet. {/i}"

    jump act2

    #l "Go help the citizens. I heard" #Is this line finished?

    #l masked_angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}"

    return

label act2:
    #We don't have a confused expression for Azazel yet,
    #so some lines are missing it.

    #fade to black for 2 seconds before showing village
    #numbers: length of fade out, time to stay faded,
    #length of next fade-in, color
    scene village with Fade(0.5, 2, 0.5, color="#000")

    "You step outside of your quarters and meet the familiar sight of your mountainside home."
    "The Order’s flags and  banners wave proudly in the wind under the full moon’s light. The sky’s faraway stars twinkle."

    show azazel neutral happy at center:
        zoom 0.2

    a "It's good to get some fresh air..."
    a neutral base "And everyone’s working hard to prepare for my crowning ceremony tomorrow. I should do something too."

    show azazel at left
    show micah masked at right:
        zoom 0.2

    m "Azazel."
    a neutral surprise "Ah! Don't sneak up on me like that, Micah!"
    m "Yeah, sorry."
    m "I heard you muttering to yourself. Help me deliver today’s dinner rations. "
    a "That’s way too much bread and water to carry yourself… of course I’ll help!"
    m "You know I always get stuck with the hardest tasks."

    "The two of you spend the next few hours trudging across the sprawling cliffside, delivering rations to the citizens of the order. "

    a neutral sheepish "Huff... huff..."
    a neutral happy "Here's your food, sir!"

    #We don't have art for "Citizen" yet.
    #Check the Drive script for what emotions this character should show.
    "Citizen" "Oh, wow. The next Prophet himself shows up at my door, and dinner’s  still just a jug of water and half a loaf of hard bread."
    "Citizen" "What a gracious Lord! Thank you Baphomet! Jeez, I’m starving here… "

    a neutral surprise "Oh!"

    menu:
        "I’m sorry, I don’t have anything else…":
            a neutral sheepish "I can try to request something better for you tomorrow, maybe."
            "Citizen" "Oh, forget it… just from the way you talk, I know you’re just a naive little kid."
            "Citizen" "Listen. When you become Prophet, you better start making some big changes around here, alright?"
            a neutral worried "Ah, I will..."

        "Be grateful of what the Order provides.":
            a neutral base "Is that really how you should be speaking to the next Prophet?"
            "Citizen" """
            Uh... my apologies!

            I was just saying I’d like to see some changes around here… I know you’ll be a great, um, leader.

            The bread’s actually fine. All hail! Haha…
            """

    "The citizen disappears back into his residence."

    m "..."
    a neutral base "Hey, Micah, what do you think?"
    m "There's nothing to think."
    a "What do you mean? What he said really bothered me…"
    a neutral sheepish "The Order does all it can to protect and provide for its people. And yet, that guy’s so rude!"
    a "He wants “big changes”… if Baphomet heard him, he would be in serious trouble."
    m "Azazel."
    m "Let’s pass out these last few rations and talk somewhere else."

    jump act2_altar

    return

label act2_altar:

    scene altar with Fade(0.5, 2, 0.5, color="#000")
    show azazel neutral happy at left:
        zoom 0.2
    show micah masked at right:
        zoom 0.2

    "After an arduous hike, the two of you reach a cliff. A simple altar made of three slabs of stone stands on the edge, waving red ribbons. The moon shines brightly in the sky."
    a "Why did you bring me here?"
    m "This is the only place where He isn't watching."
    a "My Father? I mean- Baphomet?"
    m "Why else?"
    #We don't currently have different expressions for bandaged Micah.
    m bandage neutral "Happy early 18th birthday, Azazel."
    m "I know you’ll be busy tomorrow, with the inauguration and all. Thats why I wanted to say it now."
    a neutral very happy "Micah…! You’re so kind!"
    a "May the Lord bless you."
    m "The Lord..."
    m "Hey. We're friends, right?"
    m "Can you keep a secret?"

    show azazel neutral base

    menu:
        "Say what you want to say.":
            m "..."
            "Micah scratches the bandages on their neck."
            m "
            Lilith" #Is this supposed to be here? I think this part is incomplete.

        "Of course. You can trust me.":
            m "..."
            show micah no bandage neutral
            "Micah begins to unveil the tight bandages on their neck."
            a neutral surprised "What... is that..."
            m "It's the Order's symbol."
            m "Two years ago, I was reckless, just like that citizen complaining about rations earlier. And I paid the price."
            m "It's a miracle I can still speak, really… the only reason I didn’t die was because I got on my knees and begged."
            a neutral worried "And who did this to you...?"
            m "Who else? Your father."
            a neutral surprised "No!"
            show micah bandage neutral
            "Micah puts his bandages back on."
            m "I'm telling you the truth!"
            m "*cough*"
            a neutral worried "Please, don't strain yourself-"

    m "Baphomet tries so hard to keep everyone happy and satisfied through his sermons, but you know what?"
    m "It doesn’t work. He’s a fraud. Everyone here is miserable!"
    m "No one believes this is paradise. No one likes the prayers, or the masks, or the pitiful rations."
    m "The few that {i}are{/i} happy are delusional. Everyone else just got dragged into the Order because we’re poor and vulnerable and didn’t know any better!"
    m "...We're all just too afraid to say it."
    m "We can't leave on our own... This cult garbage is fed into our minds 24/7 ... if we-"
    show lilith masked at center:
        zoom 0.25
    m "!"
    show lilith masked at center:
        zoom 0.2
    l "There you two are!"
    "Micah scrambles to put their mask back on."
    show micah masked
    l masked_angry "..."
    l "Azazel, we've been looking all over for you. Get some rest."

    #l masked_angry "{b}Dissidents are wicked, unrepenting beings, who use sweet lies to rule the minds of the weak.{/b}"

    return

label debug_section: #A part of the game I made just to test stuff out.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene village

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

        "Continue debug scene":
            "Showing debug scene."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    show azazel bad neutral at center:
        zoom 0.3
    # These display lines of dialogue.

    a "Time to test out showing character sprites."

    #This just has Azazel temporarily go to the silhouette just for one line.
    a @ silhouette "Hiding for a second."

    a "Back."

    #And it works for multiple-word changes too.
    a @ neutral sheepish "Eeeh."

    a "Now time for some permanent changes."

    show azazel neutral base

    a "This change overrides my old self..."
    a "permanently."

    hide azazel

    a "I'm gone!"

    show azazel silhouette at center:
        zoom 0.3

    a "I'm back."

    #for debugging purposes, comment out or delete once game is finished
    menu:
        "Unlock the gallery?"

        "True":
            $ persistent.galleryUnlocked = True
            a "Now you can see the gallery."

        "False":
            $ persistent.galleryUnlocked = False
            a "Now you can't see the gallery."

    # $ persistent.galleryUnlocked = True


    return
