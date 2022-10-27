# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Azazel")


# Backgrounds
image village fog = "BG/bg_village.png"
image village flashback = "BG/bg_village_flashback.png"
image altar = "BG/bg_altar.png"
image altar flashback = "BG/altar_flashback.png"

#Characters
image azazel bad_neutral = "Characters/Azazel/azazel bad neutral.png"
image azazel good_neutral = "Characters/Azazel/azazel good neutral.png" 
image azazel neutral_neutral = "Characters/Azazel/azazel neutral neutral.png" 

image baphomet mask = "Characters/Baphomet/baphomet mask.png"
image baphomet mask_cracked = "Characters/Baphomet/baphomet mask cracked.png"

image lilith mask = "Characters/Lilith/lilith mask.png"
image lilith broken_mask_neutral = "Characters/Lilith/lilith broken mask neutral.png"

image micah mask = "Characters/Micah/micah mask.png"
image micah bandage_neutral = "Characters/Micah/micah bandage neutral.png"
image micah no_bandage_neutral = "Characters/Micah/micah no bandage neutral.png"
image micah sacrifice = "Characters/Micah/micah sacrifice.png"
image micah shock_slash = "Characters/Micah/micah shock slash.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene village fog

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    show azazel bad_neutral at center:
        zoom 0.3
    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"

    show azazel neutral_neutral

    a "Testing the different character sprites."

    hide azazel

    a "I'm gone!"

    # This ends the game.

    return
