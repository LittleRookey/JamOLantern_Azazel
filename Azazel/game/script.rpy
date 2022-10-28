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

#Gallery images list, with placeholder images for now.
#Gallery based on this tutorial: https://www.youtube.com/watch?v=0hPIQxnesS8
#More on the gallery is found in screens.rpy and gamegallery.rpy.
default galleryList = ["gallery00", "gallery01", "gallery02", "gallery03"]
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

    #fade to black for 2 seconds before showing village
    #numbers: length of fade out, time to stay faded,
    #length of next fade-in, color
    scene village with Fade(0.5, 2, 0.5, color="#000")

    "You step outside of your quarters and meet the familiar sight of your mountainside home."
    "The Order’s flags and  banners wave proudly in the wind under the full moon’s light. The sky’s faraway stars twinkle."

    m "My words are TINY!" #placeholder line, the size change in Micah's character works

    return

label debug_section: #A part of the game I made just to test stuff out.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene village

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
