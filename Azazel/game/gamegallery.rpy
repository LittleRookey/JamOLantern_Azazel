#This file defines how the gallery screen works.

screen gameGallery():
    if Lightbox_image != "":
        $ lb_image = im.Scale("gallery/" + Lightbox_image + ".png", 1280, 720)
        imagebutton:
            idle lb_image
            hover lb_image
            xalign 0.5
            yalign 0.5
            focus_mask True
            action SetVariable("Lightbox_image", "")
    else:
        frame:
            xpos 250
            ypos 100
            background None
            side ("r"):
                area (250, 100, 1820, 980)
                viewport id "gallery":
                    draggable True mousewheel True
                    vpgrid:
                        cols 3
                        spacing 20
                        allow_underfull True
                        #allow_underfull needed so you can have a number of images
                        #that's not an exact multiple of the columns number

                        for q in galleryList:
                            $ qimage = "gallery/" + q + ".png"
                            $ lb_image = im.Scale(qimage, 320, 180)
                            imagebutton:
                                idle lb_image
                                hover lb_image
                                action SetVariable("Lightbox_image", q)