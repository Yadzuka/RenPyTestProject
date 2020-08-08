############################################################
###      There are some 'tryings' to create screens      ###
############################################################

screen statsScreen(name = "Default Name"):
    zorder 10
    default n = 10

    python:
        message = "Hello boys"

    vbox:
        xalign 1.0
        style_prefix "stats_style"
        grid 2 2:
            transpose True
            text "[name!t]" size 22
            text "[name!t]" size 22
            hbox:
                style_prefix "red"
                spacing 3
                text "HP" size 19
                bar value ScreenVariableValue("n", 100) yalign 0.5 xsize 200 ysize 5 style "scrollbar"
            hbox:
                style_prefix "green"
                spacing 3
                text "MP" size 19
                bar value AnimatedValue(n, 100, 0.5) yalign 0.5 xsize 200 ysize 5 style "scrollbar"

screen centerNotify(message):
    modal True
    zorder 20

    frame:
        xalign 0.5 yalign 0.5
        vbox:
            text "[message]":
                color "#000000"
            textbutton "Okay.":
                action Return(True)

screen topNotify(message):
    zorder 20

    frame:
        xalign 0.5 yalign 0.0
        vbox:
            text "[message]":
                color ("#0F0F0F")


screen alphaMagic():
    add Appearing("logo base.png", 100, 200):
        xalign 0.2
        yalign 0.9



screen testedShopScreen(girl):
    zorder 1
    modal False

    text "%s" % hyana.name:
        pos (100, 200)
        size 50
        color hyana.color
        outlines [(2, "#000", 0, 0)]
        text_align 0.5

###
## Tryings to create inventory
###
screen inventory():
    modal True

    frame:
        at inventory_animation
        xsize 700 ysize 600 yalign 0.5 xalign 0.5
        hbox:
            ## Button that closes inventory
            button:
                pos (689, -10)
                text "x":
                    size 30
                    color "#000"
                xalign 1.0
                action [ Hide("inventory"), Show("inventoryIcon") ]
                hovered []
                unhovered []
                at buttons

screen inventoryIcon():
    default under_text = ""

    vbox:
        xalign 0.0 yalign 0.0
        imagebutton:
            idle "inventory"
            action [ Show("inventory"), Hide("inventoryIcon") ]
            hovered [ SetScreenVariable("under_text", "Open Inventory") ]
            unhovered [ SetScreenVariable("under_text", "") ]
            at quick_menu




###
## HOVER TEST
###

screen hoverTest():

    default showing_variable = ""

    vbox:
        xalign 1.0 yalign 0.0

        imagebutton:
            yalign 0.7
            idle "logo base"
            action [ Show("map") ]
            hovered [ SetScreenVariable("showing_variable", "Hello") ]
            unhovered [ SetScreenVariable("showing_variable", "") ]
            at buttons

        text "[showing_variable]":
            outlines [(2, "#000", 0, 0)]
            color "#009939"
            size 50

###
## ImageMap from ren'py tutorial
###

screen map():
    modal True
    default simple_text = ""


    imagemap:
        idle "imagemap ground"
        hover "imagemap hover"

        hotspot (44, 238, 93, 93):
            action [ None ]
            hovered [ SetScreenVariable("simple_text", "Swimming pool") ]
            unhovered [ SetScreenVariable("simple_text", "") ]
            alt "Swimming"
        hotspot (360, 62, 93, 93):
            action [ None ]
            hovered [ SetScreenVariable("simple_text", "Scince") ]
            unhovered [ SetScreenVariable("simple_text", "") ]
            alt "Science"
        hotspot (726, 106, 93, 93):
            action [ None ]
            hovered [ SetScreenVariable("simple_text", "Art") ]
            unhovered [ SetScreenVariable("simple_text", "") ]
            alt "Art"
        hotspot (934, 461, 93, 93):
            action [ None ]
            hovered [ SetScreenVariable("simple_text", "Home") ]
            unhovered [ SetScreenVariable("simple_text", "") ]
            alt "Home"
        at map_transform

        text "[simple_text]":
            size 24
            outlines [(2.0, "#000", 0, 0)]
            xalign 1.0 yalign .5

        button:
            pos(0, 0)
            action [ Hide("map") ]
            text "Hit me to close the map!":
                size 40

# HP
# MP
# Screens

screen timeScreen():
    default nowTime = Time(0)

    text "%s" % nowTime.getTime():
        size 30
