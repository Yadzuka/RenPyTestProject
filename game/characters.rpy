#######################################################
###      All characters will be define here         ###
#######################################################

define z1_kind = Character (
who_outlines = [( 2.5, "#000000", 0.0, 0.0 )],
what_outlines = [( 2.5, "#000000", 0, 0 )]
)

define tk = Character (
None,
kind = z1_kind,
what_prefix = "{size=29}",
)

define e = Character (
"Yui",
color = "#e1859d",
kind = z1_kind,
what_prefix = "{size=40}",
who_prefix = "{size=60}"
)



########################################################################
###  Class, that will be define characters and their methods         ###
########################################################################



init -1 python:
    class Girl:
        def __init__(self, girlName, color):
            self.name = girlName
            self.color = color



##################################################################
###    Objects (characters) with methods and properties        ###
##################################################################



default hyana = Girl(
    "Hyana",
    "#00C933" # Nicely green color
    )
