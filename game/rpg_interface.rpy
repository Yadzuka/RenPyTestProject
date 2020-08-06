############################################################
###      There are some 'tryings' to create screens      ###
############################################################

screen stats_screen(name = "Default Name"):
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

screen center_notify(message):
    modal True
    zorder 20

    frame:
        xalign 0.5 yalign 0.5
        vbox:
            text "[message]":
                color "#000000"
            textbutton "Okay.":
                action Return(True)

screen top_notify(message):
    zorder 20

    frame:
        xalign 0.5 yalign 0.0
        vbox:
            text "[message]":
                color ("#0F0F0F")


screen alpha_magic:
    add Appearing("logo base.png", 100, 200):
        xalign 0.2
        yalign 0.9



screen testedshopscreen(girl):
    zorder 1
    modal False

    text "%s" % hyana.name:
        pos (100, 200)
        size 50
        color hyana.color
        outlines [(2, "#000", 0, 0)]
        text_align 0.5

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
            action Notify("You clicked!")
            hovered [ SetScreenVariable("showing_variable", "Hello") ]
            unhovered [ SetScreenVariable("showing_variable", "") ]
            at buttons

        text "[showing_variable]":
            outlines [(2, "#000", 0, 0)]
            color "#009939"
            size 50





# HP
# MP
# Screens
