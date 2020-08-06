transform ff_rotate:
    rotate 45.00
    linear 1.0
    pause 1.0
    rotate 0
    repeat

transform buttons:
    alpha 0.7
    on idle:
        alpha 0.1
    on hover:
        alpha 1.0
