transform brief_zoom():
    zoom 1.0
    ease 0.1 zoom 1.2
    pause 0.3
    ease 0.1 zoom 1.0
    zoom 1.0

transform zoom_in():
    zoom 1.0
    ease 0.1 zoom 1.2
    pause 0

transform zoom_out():
    ease 1 zoom 1.0
    zoom 1.0

transform incredible_zoom():
    ease 1 zoom 2.0
    zoom 2.0
    pause 0

transform whisper_zoom():
    zoom 2.0
    pause 0

transform rotatation:
    rotate -13.5

transform config_rotation:
    rotate -13

transform degree:
    rotate -6

transform degreetwo:
    rotate 1

transform degreethree:
    rotate -4

transform degreefour:
    rotate 7

transform degreefive:
    rotate 2

transform degreesix:
    rotate -20
transform degreeseven:
    rotate 45

transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
