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

################################################################################
## Initialization
################################################################################

init:
    $ config.mouse = {
    "default": [("gui/cursor/idle_pointer.png", 0, 0)],
    "pressed_default": [("gui/cursor/drag_pointer.png", 0, 0)],
    "button": [("gui/cursor/hover_pointer.png", 0, 0)],
    "pressed_button": [("gui/cursor/drag_pointer.png", 0, 0)],
}

    $ style.bar.thumb_offset = 7.5
    

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign 0.9
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.91
            yalign 0.965


            imagebutton action Preference("auto-forward", "toggle"):
                idle "gui/imgbtn/play_idle.png"
                hover "gui/imgbtn/play_hover.png"
                selected_idle "gui/imgbtn/pause_idle.png"
                selected_hover "gui/imgbtn/pause_hover.png"

            imagebutton auto ("gui/imgbtn/ff_%s.png") action Skip()
            imagebutton auto ("gui/imgbtn/back_%s.png") action Rollback()
            imagebutton auto ("gui/imgbtn/qs_%s.png") action QuickSave()
            imagebutton auto ("gui/imgbtn/ql_%s.png") action QuickLoad()
            imagebutton auto ("gui/imgbtn/menu_%s.png") action ShowMenu("history")
            imagebutton auto ("gui/imgbtn/pref_%s.png") action ShowMenu("preferences")
            #textbutton _("Back") action Rollback()
            #textbutton _("History") action ShowMenu('history')
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Save") action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            #textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

# This should be in your styles.rpy or at the top of your script file






screen navigation():
    
    vbox:
        style_prefix "navigation"

        
        if main_menu:
            xalign 0.5
            yalign 0.90
        else:
            xoffset 120
        yalign 0.8
        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("NEW GAME") action Start()

        else:

            textbutton _("HISTORY") action ShowMenu("history")

            textbutton _("SAVE GAME") action ShowMenu("save")

        textbutton _("LOAD GAME") action ShowMenu("load")

        textbutton _("CONFIG") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("TITLE SCREEN") action MainMenu()

        textbutton _("ABOUT") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("HELP") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("QUIT") action Quit(confirm=not main_menu)

    


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
        outlines [ (absolute(1), "#ffffeb", absolute(0), absolute(0)) ]
    


style textbutton_font:
    font "fonts/gigasans.otf"
    outlines [ (absolute(1), "#ffffeb", absolute(0), absolute(0)) ]


style navigation_button_text:
    properties gui.text_properties("navigation_button")
    font "fonts/gigasans.otf"
    #outlines [ (absolute(1), "#ffffeb", absolute(0), absolute(0)) ]
    xalign 0.5


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():
    
    ## This ensures that any other menu screen is replaced.
    tag menu
    

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
#    frame:
#        style "main_menu_frame"
    add particle
    add fog alpha 0.025

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    fixed:
        style_prefix "navigation"

        

        if main_menu:
            
            textbutton _("New Game") align(0.5, 0.65) action Start()
            #    idle_background None
            #    hover_background "images/buttons/button_bg.png"

            #imagebutton auto "images/buttons/new_game_%s.png" ypos 487 action Start() hovered [ Play("sound", "audio/sfx/hoverclick.mp3")]

        else:

            textbutton _("HISTORY") action ShowMenu("history")

            textbutton _("SAVE GAME") action ShowMenu("save")

        textbutton _("Load Game") align(0.5, 0.70) action [ShowMenu("load"), Hide("main_menu")]
        #imagebutton auto "images/buttons/load_game_%s.png" ypos 560 xpos 3 action ShowMenu("load") hovered [ Play("sound", "audio/sfx/hoverclick.mp3")]

        textbutton _("Options") align(0.5, 0.75) action ShowMenu("conpoopoo")
        #imagebutton auto "images/buttons/config_%s.png" ypos 635 action ShowMenu("preferences") hovered [ Play("sound", "audio/sfx/hoverclick.mp3")]
        textbutton _("Archive") align(0.5, 0.80) action ShowMenu("archive")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("TITLE SCREEN") action MainMenu()
            
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") align(0.5, 0.85) action Quit(confirm= not main_menu)
            #imagebutton auto "images/buttons/quit_%s.png" ypos 715 action Quit(confirm= not main_menu) hovered [ Play("sound", "audio/sfx/hoverclick.mp3")]

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it."

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    image "images/screen/history.png"

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    #use navigation

    vbox:

        
        xalign 1
        yalign 0.5

        xoffset 200
        yoffset 370
        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("{font=Nud.ttf}NEW GAME") action Start()

        else:

            textbutton _("{font=Nud.ttf}HISTORY") xpos -73 ypos 300 action ShowMenu("history") at degreesix

            textbutton _("{font=Nud.ttf}SAVE GAME") xpos -48 ypos 155 action ShowMenu("save") at degreesix

        textbutton _("{font=Nud.ttf}LOAD GAME")xpos -60 ypos -120 action ShowMenu("load") at degreesix

        textbutton _("{font=Nud.ttf}CONFIG") xpos -37 ypos -233 action ShowMenu("preferences") at degreesix

        if _in_replay:

            textbutton _("{font=Nud.ttf}END REPLAY") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("{font=Nud.ttf}TITLE SCREEN") xpos -25 ypos -433 action MainMenu() at degreesix

        textbutton _("{font=Nud.ttf}ABOUT") action ShowMenu("about") at degreesix

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("{font=Nud.ttf}HELP") xpos -8 ypos -715 action ShowMenu("help") at degreesix

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("{font=Nud.ttf}QUIT") xpos 3 ypos -795 action Quit(confirm=not main_menu) at degreesix

    textbutton _("RETURN"):
        style "return_button"

        action [
            Hide("history"),
            ShowMenu("final_menu")
        ]

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "images/screens/history.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -800
    xoffset 60


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():


    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    image "images/screens/about.png"
    



    fixed:
        offset (1695, 994)

        if main_menu:
            textbutton _("{font=Nud.ttf}RETURN") action Return()
        else:
            textbutton _("{font=Nud.ttf}RETURN") action [
                Hide("about"),
                ShowMenu("final_menu")
            ]
            
            

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load


screen load():

    fixed:
        if main_menu:
            add "images/screens/underlayer.png"
            add "images/screens/load.png"
            add fog alpha 0.05

            textbutton _("{size=-10}{font=tnr.ttf}Options{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("conpoopoo")] xpos 85 + 40 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}Archive{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("archive")] xpos 180  + 50 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}New Game{/font}{/size}") action Start() xpos 265  + 70 ypos 370
            
            textbutton _("{size=+20}{font=tnr.ttf}RETURN{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("main_menu")] xpos 150 ypos 900

        else:
            add "images/screens/load.png"
            add particle
            
            textbutton _("{size=-10}{font=tnr.ttf}Options{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("conpoopoo")] xpos 85 + 40 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}Archive{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("archive")] xpos 180  + 50 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}New Game{/font}{/size}") action Start() xpos 265  + 70 ypos 370
            
            textbutton _("{size=+20}{font=tnr.ttf}RETURN{/font}{/size}") action [Hide("load", transition=dissolve, _layer=None), ShowMenu("final_menu")] xpos 150 ypos 900

        viewport:
            draggable True
            mousewheel True
            scrollbars "horizontal"
            ysize 770
            yalign 0.5
            xalign 0.5
            scrollbar_xsize 1000
            scrollbar_xalign .5
            scrollbar_ypos -550
            scrollbar_xoffset 150

            hbox:
                yalign 0.5
                hbox:
                    spacing 200
                    for i in range(3):
                        null
                    for i in range(50):
                        $slot = i+1
                        frame:
                            background Frame("images/screens/save-load_frame.png")
                            xsize 850
                            ysize 500
                            ypos 250
                            button:
                                xalign 0.5
                                yalign 0.5
                                action FileAction(slot)
                                has vbox
                                add FileScreenshot(slot) xalign 0.5 ypos 25 xsize 720 ysize 390

                                text FileTime(slot, format=_("{font=tnr.ttf}{#file_time}%A, %B, %d %Y, %H:%M{/font}"), empty=_("{font=tnr.ttf}EMPTY SLOT{/font}")):
                                    style "slot_time_text"
                                    ypos 8
                                
                                text FileSaveName(slot):
                                    style "slot_name_text"


screen save():

    fixed:
        if main_menu:
            add "images/screens/underlayer.png"
            add "images/screens/save.png"
            add fog alpha 0.05

            textbutton _("{size=-10}{font=tnr.ttf}Options{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("conpoopoo")] xpos 85 + 40 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}Archive{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("archive")] xpos 180  + 50 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}New Game{/font}{/size}") action Start() xpos 265  + 70 ypos 370
            
            textbutton _("{size=+20}{font=tnr.ttf}RETURN{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("main_menu")] xpos 150 ypos 900

        else:
            add "images/screens/save.png"
            add particle
            
            textbutton _("{size=-10}{font=tnr.ttf}Options{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("conpoopoo")] xpos 85 + 40 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}Archive{/font}{/size}") action [Hide("load", transition=dissolve), ShowMenu("archive")] xpos 180  + 50 ypos 370
            textbutton _("{size=-10}{font=tnr.ttf}New Game{/font}{/size}") action Start() xpos 265  + 70 ypos 370
            
            textbutton _("{size=+20}{font=tnr.ttf}RETURN{/font}{/size}") action [Hide("save", transition=dissolve, _layer=None), ShowMenu("final_menu")] xpos 150 ypos 900

        viewport:
            draggable True
            mousewheel True
            scrollbars "horizontal"
            ysize 770
            yalign 0.5
            xalign 0.5
            scrollbar_xsize 1000
            scrollbar_xalign .5
            scrollbar_ypos -550
            scrollbar_xoffset 150

            hbox:
                yalign 0.5
                hbox:
                    spacing 200
                    for i in range(3):
                        null
                    for i in range(50):
                        $slot = i+1
                        frame:
                            background Frame("images/screens/save-load_frame.png")
                            xsize 850
                            ysize 500
                            ypos 250
                            button:
                                xalign 0.5
                                yalign 0.5
                                action FileAction(slot)
                                has vbox
                                add FileScreenshot(slot) xalign 0.5 ypos 50 xsize 720 ysize 390

                                text FileTime(slot, format=_("{font=tnr.ttf}{#file_time}%A, %B, %d %Y, %H:%M{/font}"), empty=_("{font=tnr.ttf}EMPTY SLOT{/font}")):
                                    style "slot_time_text"
                                    ypos 35
                                
                                text FileSaveName(slot):
                                    style "slot_name_text"
                                
                                textbutton _("{font=tnr.ttf}DELETE THIS SAVE{/font}") action FileDelete(slot) xalign 0.5 ypos 20



screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    image "images/screens/config_menu.png"

    vbox:
        
            hbox:
                xoffset 700
                yoffset 0
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        xoffset -450
                        yoffset 700
                        at config_rotation
                        style_prefix "radio"
                        label _("{font=Nud.ttf}{i}DISLAY")
                        textbutton _("Window") action Preference("display", "window") xoffset -23
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") xoffset 3

                vbox:
                    xoffset -1000
                    yoffset 500
                    at config_rotation
                    style_prefix "check"
                    label _("{font=Nud.ttf}{i}SKIP")
                    textbutton _("Unseen Text") action Preference("skip", "toggle") xoffset -23
                    textbutton _("After Choices") action Preference("after choices", "toggle") xoffset 3
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) xoffset 23

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                xoffset 480
                yoffset 182
                style_prefix "slider"
                box_wrap True

                vbox:
                    xoffset 500
                    yoffset -570
                    at config_rotation

                    label _("{font=Nud.ttf}{i}{size=-10}TEXT SPEED")

                    bar value Preference("text speed") 

                    label _("{font=Nud.ttf}{i}{size=-10}AUTO-FORWARD TIME") xoffset 50 yoffset 20

                    bar value Preference("auto-forward time") xoffset 50 yoffset 20

                vbox:
                    xoffset -800
                    yoffset -380
                    at rotatation

                    if config.has_music:
                        label _("{font=Nud.ttf}{i}{size=-10}MUSIC VOLUME")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("{font=Nud.ttf}{i}{size=-10}SOUND VOLUME") xoffset 50 yoffset 20

                        hbox:
                            xoffset 50
                            yoffset 20
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("{font=Nud.ttf}{i}{size=-10}VOICE VOLUME") xoffset 100 yoffset 40

                        hbox:
                            xoffset 100
                            yoffset 40
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("{font=Nud.ttf}{i}MUTE ALL"):
                            xoffset 700 yoffset -15
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

    fixed:

        if main_menu:
            textbutton _("{font=Nud.ttf}{i}{size=+100}RETURN") ypos 70 xpos 85 action Return() at rotatation:
                idle_background None
                hover_background None
        else:
            textbutton _("{font=Nud.ttf}{i}{size=+100}RETURN") ypos 70 xpos 85 action [
                ShowMenu("final_menu"),
                Hide ("preferences")
            ] at rotatation


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    #image "images/screens/history.png"

    ## Avoid predicting this screen, as it can be very large.
    predict False
    #image "images/screens/history.png"
    use game_menu(_("{font=Nud.ttf}"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"
        for h in _history_list:
            
            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }
define gui.scrollbar_borders = Borders(0, 1000, 0, 1000)
define gui.scrollbar_size = 15
define gui.scrollbar_ymargin = 0 # Vertical margin around the scrollbar
define gui.scrollbar_xmargin = 100   # Vertical margin around the scrollbar


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    image "images/screens/help.png"

    fixed:
            
            hbox:

                textbutton _("{font=Nud.ttf}KEYBOARD") xpos 260 ypos 60 action SetScreenVariable("device", "keyboard")
                textbutton _("{font=Nud.ttf}MOUSE") xpos 305 ypos 60 action SetScreenVariable("device", "mouse")
                
                if GamepadExists():
                    textbutton _("{font=Nud.ttf}GAMEPAD") xpos 350 ypos 60 action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
    fixed:
        xpos 1257
        ypos 50
        if main_menu:
            textbutton _("{font=Nud.ttf}{size=+100}{i}RETURN") action Return() at degreeseven
        else:
            textbutton _("{font=Nud.ttf}{size=+100}{i}RETURN") at degreeseven action [
                Hide("help"),
                ShowMenu("final_menu")
            ]


screen keyboard_help():

    fixed:
        xpos 280
        ypos 200

        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")

        hbox:
            ypos 70
            label _("Space")
            text _("Advances dialogue without selecting choices.")

        hbox:
            ypos 140
            label _("Arrow Keys")
            text _("Navigate the interface.")

        hbox:
            ypos 210
            label _("Escape")
            text _("Accesses the game menu.")

        hbox:
            ypos 280
            label _("Ctrl")
            text _("Skips dialogue while held down.")

        hbox:
            ypos 350
            label _("Tab")
            text _("Toggles dialogue skipping.")

        hbox:
            ypos 420
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            ypos 490
            label _("Page Down")
            text _("Rolls forward to later dialogue.")

        hbox:
            ypos 560
            label "H"
            text _("Hides the user interface.")

        hbox:
            ypos 630
            label "S"
            text _("Takes a screenshot.")

        hbox:
            ypos 700
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

        hbox:
            ypos 770
            label "Shift+A"
            text _("Opens the accessibility menu.")


screen mouse_help():

    fixed:
        xpos 280
        ypos 200

        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")

        hbox:
            ypos 70
            label _("Middle Click")
            text _("Hides the user interface.")

        hbox:
            ypos 140
            label _("Right Click")
            text _("Accesses the game menu.")

        hbox:
            ypos 210
            label _("Mouse Wheel Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            ypos 280
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")


screen gamepad_help():

    fixed:
        xpos 280
        ypos 200

        hbox:
            label _("Right Trigger A/Bottom Button")
            text _("  Advances dialogue and activates the interface.")

        hbox:
            ypos 70
            label _("Left Trigger(Left Shoulder)")
            text _("  Rolls back to earlier dialogue.")

        hbox:
            ypos 140
            label _("Right Shoulder")
            text _("  Rolls forward to later dialogue.")

        hbox:
            ypos 210
            label _("D-Pad, Sticks")
            text _("  Navigate the interface.")

        hbox:
            ypos 280
            label _("Start, Guide, B/Right Button")
            text _("  Accesses the game menu.")

        hbox:
            ypos 350
            label _("Y/Top Button")
            text _(" Hides the user interface.")

        textbutton _("Calibrate") ypos 420 action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen save_your_progress_bitch1:

    modal True

    zorder 200
    image "images/screens/System_overlay_save.png"
    fixed:
        textbutton _("{font=LinBiolinum.otf}{i}{size=+50}YES") align (0.5, 0.5) yoffset 180 xoffset -200 action [ShowMenu("save"), Return()]
        textbutton _("{font=LinBiolinum.otf}{i}{size=+50}NO") align (0.5, 0.5) yoffset 180 xoffset 200 action Return()

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "images/screens/System_overlay_quit.png"

    fixed:
        textbutton _("{font=LinBiolinum.otf}{i}{size=+50}YES") align (0.5, 0.5) yoffset 70 xoffset -200 action yes_action
        textbutton _("{font=LinBiolinum.otf}{i}{size=+50}NO") align (0.5, 0.5) yoffset 70 xoffset 200 action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 0
            xpos 30
            ypos 2

            text _("{font=gigasans.otf}{i}Skipping{/i}{/font}")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    xpos gui.skip_xpos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "fonts/Nud.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb "dynamic_vscroll_thumb" thumb_offset 17

#style vscrollbar:
#    xsize gui.scrollbar_size
#    base_bar Frame("dynamic_vscroll", Borders(0, 2, 0, 2), tile=True)
#    thumb "dynamic_vscroll_thumb" thumb_offset 17.5

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900




#SPELL SCREENS
label atralis:
    scene black
    with dissolve

    play audio "audio/sfx/click2.mp3"
    show text "{glitch=5.0}{i}Atralis Venara...{w=3}{/i}{/glitch}" with fade
    with pause(2)

    hide text with dissolve
    return

#loading 
#image loading = Movie(size=(1920, 1080), play="images/loading.webm")

image splashscreenanimation:
    "images/splashscreenanimation.png"

screen splash_text():
    text _("{font=gigasans.otf}Press Any Button{/font}") align(0.5, 0.7) size 30 color "#FFFFFF" bold False:
        outlines [ (2, "#00000050", absolute(1), absolute(1)) ]
        at blink

    

label splashscreen:
    play music "audio/game music/fantasy.mp3"
    pause(0)

    show image "images/empty.jpg"
    with Fade(1,1,1)

    show image "images/disclaimer.jpg"
    with Dissolve(2)
    pause (10)

    show image "images/wallpaper.jpg"
    with dissolve
    pause(1)

    show image "images/splashscreen.jpg"
    show screen splash_text
    show particle
    with dissolve
    pause(10000)

    play sound "audio/sfx/click2.mp3"
    stop music fadeout 1.0
    hide screen splash_text

    with dissolve
    return

screen final_menu():
    image "images/screens/final_menu.png"

    fixed:

        if main_menu:

            textbutton _("{font=Nud.ttf}NEW GAME") action Start()
        else:
            #the more ypos, pababa
            textbutton _("{font=Nud.ttf}{size=+50}{i}HISTORY") xpos 121 ypos 0 at degree action [
                ShowMenu("history"),
                Hide("final_menu")
            ]:
                hover_background None
            textbutton _("{font=Nud.ttf}{size=+40}{i}SAVE GAME") xpos 210 ypos 250 at degreethree action [
                ShowMenu("save"),
                Hide("final_menu")
            ]:
                hover_background None
            textbutton _("{font=Nud.ttf}{size=+30}{i}LOAD GAME") xpos 280 ypos 220 at degreetwo action [
                ShowMenu("load"),
                Hide("final_menu")
            ]:
                hover_background None
            textbutton _("{font=Nud.ttf}{size=+50}{i}CONFIG") xpos 180 ypos 120 at degreetwo action [
                ShowMenu("preferences"),
                Hide("final_menu")
            ]:
                hover_background None
            textbutton _("{font=Nud.ttf}{size=+50}{i}HELP") xpos 270 ypos 440 action ShowMenu("help") at degreefive        
            textbutton _("{font=Nud.ttf}{i}{color=#010101}RETURN") xpos 1695 ypos 994 action Return()

            #imagebutton auto "images/buttons/return_%s.png" focus_mask True action Hide("final_menu") hovered [ Play("sound", "audio/sfx/hoverclick.mp3")]

        if _in_replay:
            textbutton _("{font=Nud.ttf}END REPLAY") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("{font=Nud.ttf}{size=+40}{i}TITLE SCREEN") xpos 120 ypos 380  action MainMenu() at degreefour
        textbutton _("{font=Nud.ttf}{size=+50}{i}ABOUT") xpos 160 ypos 200 at degree action [
            ShowMenu("about"),
            Hide("final_menu")
        ]




screen conpoopoo():

    tag menu

    image "images/screens/conpoopoo.png"

    vbox:
        
            hbox:
                xoffset 700
                yoffset 0
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        xoffset -450
                        yoffset 700
                        at config_rotation
                        style_prefix "radio"
                        label _("{font=Nud.ttf}{i}DISLAY")
                        textbutton _("Window") action Preference("display", "window") xoffset -23
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") xoffset 3

                vbox:
                    xoffset -1000
                    yoffset 500
                    at config_rotation
                    style_prefix "check"
                    label _("{font=Nud.ttf}{i}SKIP")
                    textbutton _("Unseen Text") action Preference("skip", "toggle") xoffset -23
                    textbutton _("After Choices") action Preference("after choices", "toggle") xoffset 3
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) xoffset 23

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                xoffset 480
                yoffset 182
                style_prefix "slider"
                box_wrap True

                vbox:
                    xoffset 500
                    yoffset -570
                    at config_rotation

                    label _("{font=Nud.ttf}{i}{size=-10}TEXT SPEED")

                    bar value Preference("text speed") 

                    label _("{font=Nud.ttf}{i}{size=-10}AUTO-FORWARD TIME") xoffset 50 yoffset 20

                    bar value Preference("auto-forward time") xoffset 50 yoffset 20

                vbox:
                    xoffset -800
                    yoffset -380
                    at rotatation

                    if config.has_music:
                        label _("{font=Nud.ttf}{i}{size=-10}MUSIC VOLUME")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("{font=Nud.ttf}{i}{size=-10}SOUND VOLUME") xoffset 50 yoffset 20

                        hbox:
                            xoffset 50
                            yoffset 20
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("{font=Nud.ttf}{i}{size=-10}VOICE VOLUME") xoffset 100 yoffset 40

                        hbox:
                            xoffset 100
                            yoffset 40
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("{font=Nud.ttf}{i}MUTE ALL"):
                            xoffset 700 yoffset -15
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

    fixed:

        if main_menu:
            textbutton _("{font=Nud.ttf}{i}{size=+100}RETURN") ypos 70 xpos 85 action Return() at rotatation:
                idle_background None
                hover_background None
        else:
            textbutton _("{font=Nud.ttf}{i}{size=+100}RETURN") ypos 70 xpos 85 action ShowMenu("final_menu") at rotatation

screen archive():
    
    fixed:
        text _("Wala pang design kase tinatamad aq") offset (100, 100)


define gui.text_hover_outlines_verka = [ (absolute(1), "#ffffff", absolute(0), absolute(0)) ]

style hoverbuttons_verka:
    color "#ffffff"
    hover_color "#ff0000ff"