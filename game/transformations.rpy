transform ff_rotate:
    rotate 45.00
    linear 1.0
    pause 1.0
    rotate 0
    repeat

transform buttons:
    alpha 0.7
    on idle:
        alpha 0.3
    on hover:
        alpha 1.0

transform quick_menu:
    maxsize (70, 70)
    radius ( .1 )
    xtile 1 ytile 1

    on idle:
        alpha 0.3
    on hover:
        alpha 1.0

transform inventory:
    zoom 0.1 alpha 0.3
    linear 0.2 zoom 0.4 alpha 0.7
    linear 0.18 zoom 1.0 alpha 1.0

transform map_transform:
    zoom 1.5

transform text_colorized:
    on idle:
        alpha 0.6
    on hover:
        alpha 1.0

transform coins:
    zoom 0.07

transform zooming:
    xalign 0.5
    yalign 0.5
    on idle:
        zoom 1.0
        alpha 1.0
    on hover:
        alpha 0.7
        zoom 1.07
