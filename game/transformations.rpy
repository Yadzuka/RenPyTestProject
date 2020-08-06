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
    zoom 0.05
    on idle:
        alpha 0.3
    on hover:
        alpha 1.0

transform inventory_animation:
    zoom 0.1 alpha 0.3
    linear 0.2 zoom 0.4 alpha 0.7
    linear 0.18 zoom 1.0 alpha 1.0
