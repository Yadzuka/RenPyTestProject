# The game starts here.

label start:

    show bg gray

    show screen testedshopscreen("Hyana") with fade

    tk "You have born in 1478 in a small village that name was 'Rangrid'."

    show screen hoverTest

    tk "After standing on your feet, you started to learn how to keep sword in hands."

    call screen center_notify(_("Congratulations!"))

    tk "The war.... War, that brought so many human lifes... Seems like it never ends."

    show screen stats_screen

    tk "The first thing about your thinking is building world with piece and innocent."


label start_game:

    e "Rise up, sleepy head, we need to go!"

    extend " You slept over 8 hours, that's too much!"

    return
