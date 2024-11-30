"""
 Team Novus Ren'py Script
 Novus Studio <teamnovus.studio@gmail.com>

 Hello, Dev Jideeh here! I'd appreciate it if you kept this file private.
 We only opened the file for you prying peeps to see extra easter eggs
 of the game. ;)

 If you were to make this a reference for anything similar to making a game,
 making a script, making a story, we'd appreciate being given credit :))
 
 Really hope you enjoy/enjoyed the game, and don't shy away from criticizing
 us. We plan to improve further!!

 Sincerely, Team Novus
 """

###NOTE I separated the images coding because it was too cramped in the script.rpy -- DEV Jideeh

#SCENES BECAUSE RENPY DOESN'T WANT TO CHANGE ITS READ DIRECTORY AWAY FROM IMAGES
#FUCKIGN RENPY ISTG I HATE YOU SO MUCH RIGHT NOW.
#       Colored
image practice = "scenes/1.png"
image practice2 = "scenes/2.png"
image practice3 = "scenes/3.png"
image practice4 = "scenes/4.png"
image practice5 = "scenes/5.png"
image practice6 = "scenes/6.png"
image cleo_fireball = "scenes/7.png"
image cleo_fireball2 = "scenes/8.png"
image cleo_fireball3 = "scenes/9.png"
#       RAWW!!!
image p1 = "scenes/nocolor/1.png"
image p2 = "scenes/nocolor/2.png"
image p3 = "scenes/nocolor/3.png"
image p4 = "scenes/nocolor/4.png"
image p5 = "scenes/nocolor/5.png"
image p6 = "scenes/nocolor/6.png"
image cf = "scenes/nocolor/7.png"
image cf2 = "scenes/nocolor/8.png"

#       TRANSPARENT
image tp1 = "scenes/transparentbg/1.png"
image tp2 = "scenes/transparentbg/2.png"
image tp3 = "scenes/transparentbg/3.png"
image tp4 = "scenes/transparentbg/4.png"
image tp5 = "scenes/transparentbg/5.png"
image tp6 = "scenes/transparentbg/6.png"

#       MISCELLANEOUS
image splashscreen:
    "images/splashscreen.png"
image phforest = "scenes/bg/phforest.png"

image cartridge:
    im.Scale("scenes/cartridge.png", 1920, 1080)

#################################################################################################################
#       CHARACTER SPRITES
### CLEO
image c_confused:
    "sprites/c_confused.png"
image c_neutral:
    "sprites/c_neutral.png"
image cleo_interrupt:
    "sprites/interruption/cleo_interrupt.png"

### KURT
image k_neutral:
    "sprites/k_neutral.png"
image k_nonchalant:
    "sprites/k_nonchalant.png"
### KIRK
image kd_laugh:
    "sprites/kd_laugh.png"
image kd_neutral:
    "sprites/kd_neutral.png"
image kd_smile:
    "sprites/kd_smile.png"
### LOUISE
image l_angry:
    "sprites/l_angry.png"
image l_neutral:
    "sprites/l_neutral.png"


# images I had to code to make the user experience great
image ctc_animation = Animation(
    im.Scale("images/ctc/ctc11.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc10.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc9.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc8.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc7.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc6.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc5.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc4.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc3.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc2.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc1.png", 50, 50), 0.5,
    im.Scale("images/ctc/ctc1.png", 50, 50), 0.5,
    im.Scale("images/ctc/ctc2.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc3.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc4.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc5.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc6.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc7.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc8.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc9.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc10.png", 50, 50), 0.05,
    im.Scale("images/ctc/ctc11.png", 50, 50), 0.05,
    xpos=0.915, ypos=0.78, xanchor=1.0, yanchor=1.0
)

define particle = SnowBlossom("images/particle.png", count=20, border=600, xspeed=50, yspeed=0, start=5, fast=True, horizontal=True)
define menuparticle = SnowBlossom("images/particle.png", count=20, border=600, xspeed=0, yspeed=50, start=5, fast=True)
define fog = SnowBlossom("images/fog.jpg", count=20, border=600, xspeed=50, yspeed=50, start=5, fast=True)


image particle = SnowBlossom("images/particle.png", count=10, border=600, xspeed=50, yspeed=0, start=5, fast=True, horizontal=True)
