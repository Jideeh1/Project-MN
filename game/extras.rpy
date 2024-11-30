define config.main_menu_music = "audio/game music/ruins2.mp3"
define config.main_menu_music_fadein = 5.0

init python:
    style.button.activate_sound = "audio/sfx/click.mp3"
    style.button.hover_sound = "audio/sfx/hoverclick.mp3"
    
    def play_sound(file, volume=1.0):
        renpy.play(file, channel='sound')
        renpy.sound.set_volume(volume, channel='sound')

    config.mouse = {
        'default': [
            ('mouseup_1', lambda *args: play_sound("audio/sfx/click.mp3", 100.0)),
            ('hover', lambda *args: play_sound("audio/sfx/hoverclick.mp3", 1.5)), 
        ]
    }



#textbutton _("Yes          ") action ShowMenu("save")
#textbutton _("          No") action Return("save_your_progress_bitch")

#scene function DO NOT REMOVE
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
transform blink:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause(.5)
    linear 1.0 alpha 0.0
    repeat

transform transparent:
    alpha 0.0

transform fadein:
    alpha 0.0
    linear 1.0 alpha 1.0

transform grow_text:
    zoom 1
    linear 2.0 zoom 1.2