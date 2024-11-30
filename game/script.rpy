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

# Dear Devs/Writers, don't forget to call screen save_your_progress_bitch before jumping
# to another chapter :) -- JD

init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sfx/type2.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

init:
    # Animation Transitions (Because I want animations to be dynamic too) -- Dev JD
    define ypunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=100)
    define xpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=100)

# Characters + Automated CTC indicator
define c = Character("{gradient=#e0a803-#ffee93}Cleo{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define k = Character("{gradient=#94b0da-#b7d7e8}Kurt{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define l = Character("{gradient=#ff6961-#ffb6b9}Louise{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define kd = Character("{gradient=#c6e2e9-#aec6cf}Kirk{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define j = Character("{gradient=#f2d7d9-#fcbad3}Justine{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define r = Character("{gradient=#ff9a76-#ffd1a9}Ram{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define rk = Character("{gradient=#fae3d9-#e2b4bd}Restine{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define s = Character("{gradient=#b1cbbb-#d5e1df}Sebashtian{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define e = Character("{gradient=#cabac8-#f7cac9}Edith{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define jd = Character("{gradient=#d4a5a5-#f5d5cb}Jideeh{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define d = Character("{gradient=#ffcccb-#ffe5d4}Dave{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define m = Character("{gradient=#fbe8a6-#f9d5bb}Louise's Mom{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")

# Side Characters + Automated CTC indicator
define u = Character("{gradient=#d1c4e9-#b39ddb}???{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define u1 = Character("{gradient=#ffccbc-#ffab91}???{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define u2 = Character("{gradient=#c5e1a5-#aed581}???{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define b = Character("{gradient=#d1c4e9-#b39ddb}Brad{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define v = Character("{gradient=#ffccbc-#ffab91}Vax{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define la = Character("{gradient=#c5e1a5-#aed581}Lain{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")

# Narration
define narrator = Character(callback=callback, name=None, ctc="ctc_animation", ctc_position="fixed")

# Prologue starts here
label start:
    # Dear Devs, don't remove the camera here! -- JD
    camera:
        perspective True

    pause (2)
    play music "audio/music/Goofing-tension.mp3" fadein 5 volume 0.5 fadeout 3
    scene black

    $ quick_menu = False

    with vpunch
    play sound "audio/game sfx/impact1.mp3"
    with hpunch

    "I FUCKING TOLD YOU I DON'T KNOW HOW TO CAST THIS SHIT!{w=1}{nw}" with hpunch
    "AHHHHHHH!{w=0.4}{nw}" with vpunch and hpunch

    play sound "audio/game sfx/sword.mp3"

    "HOLY SHIT,{w=0.2} I CAN PARRY WHAT THE FUUUUCKK!?{w=1}{nw}"

    play sound "audio/game sfx/magicimpact.mp3"

    "WATCH YOUR TARGETS, ARE YOU BLIND!?{w=1.3}{nw}"
    "HOW COME YOU'VE BEEN WANTING TO BE A MAGE, BUT CAN'T WIELD A FUCKING WAND!?{w=1.3}{nw}"with vpunch and hpunch

    play sound "audio/game sfx/magicimpact2.mp3"

    "WELL, PARDON THAT I WASN'T EXPECTING THIS TURN OF EVENT!!{w=0.5} 
    AND YOU TALK TOO MUCH BUT OF WHAT HELP ARE YOU?!{w=1}{nw} AH, SHIT!{w=1}{nw}"

    with vpunch
    play sound "audio/game sfx/impact1.mp3"
    with hpunch

    "{w=1}JUST. {w=0.3}AIM.{w=0.3} AND.{w=0.3} CAST.{w=1}{nw}"

    play sound "audio/game sfx/impact1.mp3"
    play sound "audio/game sfx/sword.mp3"

    "HOLY SHIT GUYS, I CAN FUCKING PARRYYYY!!!{w=1}{nw}"with vpunch and hpunch

    play sound "audio/game sfx/sword.mp3"

    "SHUT UP, KURT!!!" with vpunch
    
    $ quick_menu = True
    label choices:
            "Before I introduce myself, let me ask you this: How far are you in the story?"
            menu:
                "The part where they arrived at the castle":
                    jump choices1
                "The part where the three of them were practicing.":
                    jump choices2
                "I just started.":
                    jump choices3
                "The latest one yet (11-07-24)":
                    jump choices4
    
    scene white with fade

    #NOTE Insert CG here of you guys being chaotic in the intro. -- JD

    label choices3:

    u "Welp-"
    u "Hey, there."
    u "You're probably wondering who those jerks are."
    u "Well, you're in luck. {w=0.5}Because I can answer that question with my best ability."
    u "That's me and two of my best buds."
    u "The name's Cleo."
    c "The one with the long-ass sword is Kurt.{p}And that furry guy is-"
    c "I'm not even going to ask you who that guy is.{p}Chances are,{w=0.5} you already know."
    c "What gave it away?{w=1} The glasses?"
    c "Fuck no{w=0.4}, it's his goddamn {bt=5}✨FURRINESS✨{/bt}."

    c "You're also probably wondering how we got ourselves in this situation."
    c "Well, you're in horrible luck.{w=0.5} Because we are as clueless as you are."
    
    stop music fadeout 3.0

    c "But let's start from the beginning."

    play music "audio/game music/smile.mp3" fadein 3.0

    scene black with dissolve

    "A few days ago, {w=0.3}I found an antique store."

    scene store with fade ##NOTE antique store -- JD

    "I wasn't expecting too much out of it{w=0.3} I mean, {w=0.3}I knew what was usually displayed."
    "Some katanas that I'm not so sure whether they're real or not.{w=0.4} Some dreamcatchers{w=0.2}, wood-carved items{w=0.2}, jewelry{w=0.2}, and other things common in your typical antique store."

    scene store_display with fade ##NOTE game cartridge displayed outside the store -- JD
    "There really wasn't any items attracting nearby eyes, until I looked at the window display."
    "A retro-looking game cartridge,{w=0.5}
    sitting on a probably warm cushion,{w=0.5} displayed outside with only the glass wall separating us,{w=0.5} lured me in."
    "Maybe I'm exaggerating. {w=0.5}Maybe I'm not. But with retro games,{w=0.3} you have to take your chances."
    "You never know it might bring me fortune,{w=0.5} it might not."
    
    scene black with dissolve

    "Ignore my blabbering,{w=0.5} I just wanted to make an excuse to buy it since it's compatible with my old console."
    "The game didn't cost too much, so I took the liberty to buy it right away."
    "Despite its low cost. I still mourn for my lost money."

    scene bahay with fade ##NOTE bahay ni cleo -- JD

    "The only hassle was cleaning my old console and trying to get it to work after years of not being fed with electricity."
    "I wasted no time and plugged the sucker in.{w=1} And just when I was about to start the console{w=0.5}, I heard my name being called out."
    u "Ate, si Louise."
    "Talk about perfect timing, huh?"
    c "Ah, teka lang ah."
    "I got up from my seat and headed towards the door, patting the dusts off of my clothes."
    "There, I saw a wild Louise with his trainer, Kurt."
    
    show c_neutral at left with dissolve
    c "Oh, anong meron?{w=0.3} Nasa galaan ka nanaman."
    show l_neutral at right with dissolve
    l "kasama ko si Kurt."
    show l_neutral at right with easeinright:
        xoffset -200
    show k_neutral behind l_neutral at right with easeinright:
        xoffset 100
    show c_confused at left with dissolve
    hide c_neutral
    c "Ah,{w=0.3} nasa date na naman kayo ngayon?"
    ##NOTE this should be l_giggle or something -- JD
    show l_angry at right with dissolve:
        xoffset -200
    hide l_neutral
    l "Will you be our thirdwheel?"
    c "Har har. {w=1}So, anong meron at napadaan kayo?"
    show l_neutral at right with dissolve:
        xoffset -200
    hide l_angry
    l "Ayun nga{w=0.3}, aayain ka sana namin lumabas. {w=0.5}Boring sa amin eh."
    show c_neutral at left
    hide c_confused

    c "Sa inyo lang.{w=0.3} May pinagkakaabalahan na ako eh."
    l "Ay woooow.{w=0.5} Ano ba ginagawa mo't ayaw mong maging third wheel?"
    c "Yun oh."

    scene cartridge with dissolve ##NOTE Console close up look, tapos nasa right side yung shoulder mo, pointing it -- JD

    c "Nabili ko lang sa antique store."
    l "Oooh.{w=0.3} Gumagana?"
    c "Ite-test ko na sana kanina{w=0.5}, eh bigla kayong dumating."

    scene black with dissolve

    "I told Louise and Kurt how I saw this game cartridge in an antique store{w=0.5},
    which is weird since it's an antique store,{w=0.5} where things are usually sold at a high price."
    

    scene bahay with dissolve ##NOTE bahay ni cleo -- JD

    show c_confused at left with dissolve
    show l_neutral at right with dissolve:
        ease 1.0 xoffset -300
    show k_neutral behind l_neutral at right with dissolve
    c "...Kaya ayan{w=0.3}, makalat ngayon."
    c "Why don't you two sit back and watch me fail?"
    ##NOTE louise smirk sprite -- JD
    l "Free Entertainment?"
    ##NOTE kurt smirk sprite -- JD
    k "Free Entertainment."
    c "Alright.{w=0.4} Let's start then."

    scene black with fade ##NOTE console close up (turned off) -- JD

    "After making up our minds, I finally pushed the power button from the console."
    "Electricity flowed through the wires, startling the fans awake."
    play sound "audio/sfx/roaring fans.mp3" volume 0.5
    "With its roaring fan, a dim light started flickering from its power button."
    "We held our breaths as the console struggles to awaken from its deep slumber."

    scene white with fade ##NOTE console close up (turned on, power button lighted up) -- JD
    
    "Finally, with one last push, {w=1}the light grew brighter and the console has awaken from its decade slumber."
    "I watched the excitement from Louise's and Kurt's faces as the TV flashed a familiar logo full of nostalgia."
    "Who knew watching an old console struggle to wake up is so thrilling?"

    "We stayed seated on our place,{w=0.5} hesitant to start the second challange."
    "What challenge you may ask?{w=0.5} Putting the game cartridge in and hoping to God it works."

    scene TV with fade ##NOTE self-explanatory -- JD
    stop music fadeout 3.0

    c "...Actually, 'di ko alam kung anong klaseng game 'to eh."
    play music "audio/music/goofing.mp3" fadein 3.0
    c "The cartridge doesn't have any pictures on it, so 'di ko rin ma-research what the game is about."
    k "What if adult game yan?"
    c "Sus{w=0.5}, I think we're old enough for that."
    play sound "audio/sfx/cartridge.mp3" volume 3.0
    "Enough with dilly dallying.{w=0.5} We inserted the cartridge in, and the TV flickered a black screen."
    play sound "audio/sfx/titlestart.wav" # NOTE Lower the volume here -- JD
    "Then the very next moment, the game booted up, showing the title screen."
    play sound "audio/sfx/start.wav" # NOTE and here as well -- JD
    "I heard squeals of fascination from both of my side when it booted up."
    "The title screen was bizarre to say the least.{w=1} It had characters, alphabets alien to us."
    "No one could read it. No one knows what script or alphabet it comes from."
    "I thought to myself they might just be an archiac alphabetical system that the world's abandoned."
    "As I navigate through the game, we tried recognizing and reading some of them.{p}
    But no matter how many times we did, it sounded wrong."
    "It reminds me of that one peso snack. It may look like it's read as tattoos, but it may be read as tahoos too."
    "Seriously{w=0.3}, to this day, I still don't know what it's really called."

    k "'Yaan mo na yan, Cleo.{w=0.5} Start mo na para makita na natin."
    c "Alright."
    "I guess there's no point in dwelling."
    "I pushed the thoughts to the back of my mind, and hovered the first text button."
    "Every first text buttons in a game has to be the start button{w=0.5}, right?"
    "It has to be.{w=0.5} It's just common sense."
    stop music fadeout 3.0
    "I pressed the button, expecting nothing but a narrative to start the story."

    scene tv with fade ##NOTE close up of TV seemingly glitching, three of you are also present in the scene. -- JD
    #                    Don't worry, I'll try making a storyboard for these. -- JD

    play music "audio/music/tension rising.mp3" fadein 5.0

    "But once I pressed the button{w=0.5}, I suddenly felt a powerful force drawing us in."
    "The air surrounding us were being pulled in by an unknown source.{p}
    I remember seeing both Kurt and Louise with a panicked face."

    play sound "audio/sfx/glitch.mp3" # NOTE tone down the volume of the glitch -- JD
    "And the TV monitor flickering back and forth to black and green."
    play sound "audio/sfx/riser2.mp3" volume 3.0
    "Without a moment's warning, the TV exploded in light{w=0.3}, blinding us all."
    "I didn't know what happened there.{w=0.5} I can't recall anything that happened after.{p}
    Just the oddly vivid feeling.{w=0.3} It was surreal, almost like dreaming."
    stop music fadeout 3.0
    "The next thing we know, we we're in a completely different world."

    scene battleground with fade ##NOTE can be changed. Not necessarily battleground -- JD
    play music "audio/music/Goofing-tension.mp3" fadein 5 volume 0.5 fadeout 1
    
    with vpunch
    play sound "audio/game sfx/impact1.mp3"
    with hpunch
    "{w=1.5}I FUCKING TOLD YOU I DON'T KNOW HOW TO CAST THIS SHIT!{w=1}{nw}" with hpunch
    "AHHHHHHH!{w=0.4}{nw}" with vpunch and hpunch

    play sound "audio/game sfx/sword.mp3"

    "HOLY SHIT,{w=0.2} I CAN PARRY WHAT THE FUUUUCKK!?{w=1}{nw}"
    play sound "audio/game sfx/magicimpact.mp3"
    "{w=1.5}WATCH YOUR TARGETS, ARE YOU BLIND!?{w=1.3}{nw}"
    "HOW COME YOU'VE BEEN WANTING TO BE A MAGE, BUT CAN'T WIELD A FUCKING WAND!?{w=1.3}{nw}"with vpunch and hpunch
    play sound "audio/game sfx/magicimpact2.mp3"
    "WELL, PARDON THAT I WASN'T EXPECTING THIS TURN OF EVENT!!{w=0.5} 
    AND YOU TALK TOO MUCH BUT OF WHAT HELP ARE YOU?!{w=1}{nw} AH, SHIT!{w=1}{nw}"
    with vpunch
    play sound "audio/game sfx/impact1.mp3"
    with hpunch
    "{w=1}JUST. {w=0.3}AIM.{w=0.3} AND.{w=0.3} CAST.{w=1}{nw}"
    play sound "audio/game sfx/impact1.mp3"
    play sound "audio/game sfx/sword.mp3"
    "HOLY SHIT GUYS, I CAN FUCKING PARRYYYY!!!{w=1}{nw}"with vpunch and hpunch
    play sound "audio/game sfx/sword.mp3"

    "SHUT UP, KURT!!!{w=0.5}" with vpunch

    "Ever since getting here{w=0.4}, we've been trying to figure out what or how to survive with what we got."
    "It's only been ten minutes since the incident, and we're already surrounded by slimes."
    "Slimes are probably the most common creature in the entire fantasy world, but in case you didn't know:"
    
    ##TODO screens here showing spells, mana, encantation -- JD

    "Slimes are as the their name suggest.{w=1} They are gel-like beings that seems to roam this world." 
    "They seem to adapt in their environment and change their bodily consistency."
    "In our case, they can turn into rock-hard creatures both for defense and offense-{p}Which is why Kurt can parry them."
    "Kurt and Louise tried their best to fend off the slimes, while I stayed at the back."
    "It looks exhausting, so I try not getting in their way to avoid being a hindrance."
    "I'm sorry guys...{nw}"
    # Insert slime sfx here -- Shizo
    # Done as requested -- JD
    play audio "audio/game sfx/slime-splat2.mp3" noloop volume 3.0
    c "AAHHHHH!!" with vpunch and hpunch
    "{size=+10}{sc=3}I stepped on a large slime!{/sc}{/size}"

    c "{sc=3}{cps=24}GET AWAY!{/cps}{sc}{w=0.5}{sc}" with vpunch
    c "{w=0.3}{sc=3}{fast}GET AWAY!{fast}{cps=24} GET AWAY!{/cps}{sc}{w=0.5}{nw}" with vpunch
    c "{w=0.3}{sc=3}{fast}GET AWAY! GET AWAY!{fast}{cps=24} GET AWAY!!!{/cps}{sc}{w=0.5}" with vpunch

    play sound "audio/game sfx/bonk.mp3"
    "{i}{fast}*BONK*{fast}{/i}{w=1}{nw}" with hpunch
    play sound "audio/game sfx/bonk.mp3"
    "{i}{fast}*BONK* *BONK*{fast}{/i}{w=1}{nw}" with vpunch
    play sound "audio/game sfx/bonk.mp3"
    "{i}{fast}*BONK* *BONK* *BONK*{fast}{/i}{w=1}{nw}" with hpunch

    "The sloshing sound of a slime being pounded echoed around us."
    "Despite the heavy bonks, the slime seems to be taking no damage."
    "WHAT THE HECK?!"
    
    l "STOP HITTING THE SLIME WITH YOUR STAFF,{w=1}{nw}"
    l "{fast}STOP HITTING THE SLIME WITH YOUR STAFF,{fast} {cps=48}CAST{/cps}{w=0.5}{nw}" with vpunch
    l "{fast}STOP HITTING THE SLIME WITH YOUR STAFF{w=1}, CAST{fast}{cps=48} YOUR{/cps}{w=0.5}{nw}" with vpunch
    l "{fast}STOP HITTING THE SLIME WITH YOUR STAFF{w=1}, CAST YOUR{fast} {cps=48}SPELLS{/cps}!!!" with vpunch
   
    c "I DON'T FU{w=0.05}CKING KNOW!" with xpunch
    play sound "audio/game sfx/metalbonk.mp3"
    k "UHH GUYS...?"
    play sound "audio/game sfx/metalbonk2.mp3"
    k "I NEED SOME HELP HERE!" with hpunch
    
    scene louise stance ##NOTE louise about to launch himself towards the enemies -- JD
    play sound "audio/game sfx/sword.mp3"
    "As the slime was about to launch itself to kurt, Louise mustered all his strength to his feet."

    scene slash ##NOTE louise slashing the slime into two -- JD
   
    "Without a moment of hesitation{w=0.5}{nw}"
    play sound "audio/game sfx/clawslash.mp3"
    "{fast}Without a moment of hesitation,{fast} he dashed right through the slime, slashing it through."
    "But Louise had his rear open from his wide attack. The slimes saw this opportunity and pounced towards him."
    c "{i}!!!{/i}"
    c "WATCH OUT-" with vpunch
    "But just before I could finish my words{w=0.5}{nw}"
    play sound "audio/game sfx/metalbonk3.mp3"
    "{fast}But just before I could finish my words{w=0.3},{fast} Kurt jumped in slashing the enemy down."
    "Like what you would usually see on anime fighting scenes."
    "It wasn't just one enemy though. {w=0.3}There were three slimes ready to attack them from above."
    c "UP THERE!!" with hpunch

    play sound "audio/game sfx/metalbonk.mp3"
    queue sound "audio/game sfx/metalbonk3.mp3"
    queue sound "audio/game sfx/clawslash.mp3"
    queue sound "audio/game sfx/metalbonk2.mp3"
    queue sound "audio/game sfx/clawslash2.mp3"
    queue sound "audio/game sfx/clawslash.mp3"
    queue sound "audio/game sfx/metalbonk4.mp3"

    "But by the time I warned them, Louise was already on all four, slashing and pounding at the enemies while Kurt provided support at Louise's blind sides."
    "Seeing them so...{w=0.3} unlike themselves, I don't see us losing."
    "I got goosebumps just from watching them- thinking how cool they are being right now."
    
    stop music fadeout 3.0
    scene black with dissolve
    
    "But the aftermath of the battle wasn't pretty."
    "The place is a whole mess.{p}We're all covered in stinky, sticky goo."
   
    scene white with fade ##NOTE aftermath of the battle (exhausted group) -- JD
   
    "Our clothes barely made it through.{w=0.5} We were left exhausted in the end."
    "But having the slimes finally dissipate, it at least gave us a chance to rest."
   
    play music "audio/music/tavern music.mp3" fadein 1.0
   
    l "Cleo, baka naman may napindot ka.{w=0.4} Pano tayo napunta dito?!"
    c "Sa tingin mo may pindutan talaga para ma-isekai?"
    c "Advance naman masyado technology natin n'yan."
    k "Kalma-kalma.{w=0.5} 'sides, ano magagawa natin ngayo't nandito na tayo?"
    k "We should find a town or a city for refuge."
    l "How are you so sure they're gonna welcome us with open arms?{w=0.5} We're practically strangers to them."
    k "Travelers more like."
    c "What if racists sila?-{w=0.3}{nw}"
    c "Ah! {w=0.5}DO WE EVEN HAVE MONEY?"
    l "Should that be our main concern?"
    c "I'm hungry. {w=0.5}So it {i}is{/i} a concern."
    l "Of course you are, Cleo."

    scene black with fade ##NOTE world scenery -- JD
   
    "We don't see any towns nearby. We searched for a high ground but the land is too flat."
    "The only thing that would give us a better view are the tall trees surrounding us."
    "We then decided that it'd be me to climb up since I weigh less than these two."
    "It was our only way to navigate the place, hoping I'd at least find something."
    "With the help from the two of them, it'll take less effort to reach the top so they decided to boost me up."
    "I pointed my staff at them and jokingly said:"
    c "I'll blast you off if you try anything funny."
    l "You don't even know how to cast your spells."
    c "Ouch.{w=0.3} Hurtful."
    l "But truthful."
    "Ignoring the banter, I proceeded to climb up the tree."
    "The canopy of leaves made it hard for me to see while I pass through several branches."
    "I struggled getting the offshoots off my face{w=0.3}, probably scraped me many times than I could count."
    "Once I was on the very top of the tree{w=0.5}, I felt like I could see the whole world."
    "The place looked uncanny.{w=0.5} It's similar to our world, but at the same time it had its own uniqueness."
    c "Woah..."

    scene castle with fade ##NOTE castle from a distant -- JD

    "From a near distance, I saw an imposing castle looming by.{p}It was surrounded by towering walls."
    "Its structure is-{w=0.4} well what more can I say?{w=0.3} It's a fucking castle.{p}Of course it's grand and picturesque."
    "Kinda like how Disneyland would've looked like if I actually went to see Disneyland."
    "Aside from that. It's really... magical."
    "So enchanting. It was breathtaking."
    "After briefly enjoying the view, I got down from the branch and told them the things I saw and what directions we should take."
    "We figured we should make haste while the sun is still high, so we moved out immediately in spite of our exhaustion."
    "From how it looks{w=0.3}, everything seems like a sound plan.{p}But there's never a sound plan in a group as chaotic and as unlucky as we."
    "Some things just tend to not go as planned{w=0.3}, y'know?"

    scene black with fade

    "And as I jinxed it, more slimes intercepted and ambushed us."
    
    scene battle with dissolve ##NOTE you three battling against slimes -- JD
    
    "In a world like this based on fantasy movies I've seen, monsters would be the common problem here."
    "They just kept getting in our way.{w=0.5} Maybe that's why most places here are barren and secluded."
    "Oddly enough, we started seeing patterns in their attack, simple mannerisms of slimes.{p}From that point on, it got easier and easier to fend off slimes."
    "But in spite of taking advantage of their weaknesses, we could only go so far."
    "After all, we're still new to this world."

    scene black with fade ##NOTE time: dawn. Three of you sitting down -- JD

    "With our simple tools and equipments, we thought we could probably set up a resting point with a campfire."
    "And since I hardly helped them with the slimes, I took the chance to practice my spells with the time we have left."
    "I managed to learn Earth magic, although barely. I somehow managed to make a block of mud that you could sit on."
    "It's better than nothing, even Avatar Aang had trouble learning the Earth element."
    "{i}*Sigh*{/i}"
    "But the rest of my spells just weren't getting there."
    "The two of them was seated by the side, watching me fail and fail countless times."
    scene phforest with dissolve
    show tp4 with dissolve
   
    c "...I dont get it.{w=0.3} Is it my pronunciation?{p}It's just like a fireball, nothing complicated."
    k "Maybe it's your posture?"
    c "That couldn't possibly be it.{w=0.3} I've been standing straight this whole time."
    l "Speaking of straight...{w=0.3} Maybe it's your sexuality?"
    
    show tp2 with dissolve
    hide tp4 with Dissolve(0.2)
    show tp3 with dissolve
    hide tp2 with Dissolve(0.2)
   
    c "That's not--{w=0.5}"
   
    show tp4 with dissolve
    hide tp3 with Dissolve(0.2)
   
    c "{fast}That's not--{fast} Ha{w=0.1}-ha.{w=0.3} Okay, Louise,{w=0.2} like you're any different."

    hide tp4 with Dissolve(0.2)
    # show tp5 with dissolve ##NOTE you standing with your staff, but in a neutral position. eyes closed. -- JD

####--------------------------------------DISCONTINUED---------------------------------------------------
    #"Regardless{w=0.1}, I followed his suggestions and fixed my posture."
    #"I took one last look at my spellbook, its pages crinkled and aged.{w=0.4} Finally, I signed under my breath and low."
    #"I closed my eyes, trying to feel everything around me.{p}The ground,{w=0.3} the air,{w=0.3} the trees swaying through the breeze."
    #"It's that same vivid feeling I had before we were transported here."
    #"With all the focus I could muster{w=0.3}, I grabbed that feeling."
    #"The air crackled, feeling the anticipation from both of them."
    #"I spent the majority of our resting time memorizing incantations.{p}But it was only now{w=0.3}, at this very moment{w=0.3}, to do the efforts justice."
    
    #hide tp5 with Dissolve(0.2)
    #show tp6 with dissolve ##NOTE you standing with your staff(it's glowing now), but in a neutral position. eyes closed. -- JD
    

    #"As I hold on to that feeling{w=0.3}, I felt a burning sensation rush through me."
    #"The heat curled up in my chest grew hotter and hotter, like a water boiling.{w=0.3} And as I try manifesting this feeling{w=0.5}: Foreign words suddenly appeared in the back of my mind."
    #play sound "audio/game sfx/spell3.mp3"
    #"The words,{w=0.5} it's there, but it's not mine."
    #"The foreign words poured into my mind. Stirring{w=0.3}, begging{w=0.3}, demanding release."
    #"Until finally, the words alien to me started becoming familiar."
    #play sound "audio/game sfx/spell2.mp3"

    #scene black
    #with dissolve

    #play audio "audio/sfx/click2.mp3"
    #show text "{glitch=5.0}{size=+100}{i}{swap=Equinox@Pyro@0.2}Atralis{/swap} {swap=Harmonia@Burn@0.2}Venara{/swap}...{/size}{w=3}{/i}{/glitch}"
    #$ quick_menu = False
    #pause(2)

    #hide text with dissolve

    #scene cf with dissolve
    #$ quick_menu = True

    #play sound "audio/game sfx/spell.mp3"
    #"And with its sweet release{w=0.3}, I incanted:"
    #play audio "audio/game sfx/flame.mp3"
    #c "{explode=1}{i}{font=naganoshi.ttf}「{/font}Pyroblast!{font=naganoshi.ttf}」{/font}{/i}{/explode}"

    #scene cleo_neutral with dissolve
    #$ quick_menu = True
    
    #$ renpy.pause(2, hard=True)

    #scene white with fade ##NOTE you standing with your staff(glowing), but you have your staff in front of you, eyes open. show the fireball arching -- JD

    #"A light suddenly enveloped us.{w=0.3} It was a fireball, the size of a beach ball,{w=0.3} flying through the sky as it arches down the earth."
    #"Kurt and Louise stayed seated, dumbfounded."
    #k "Uh oh.{w=1.5}"
    #l "Oh no.{w=1.5}"
    #c "What?{w=2}"
    #l "You're an arsonist{w=0.5}, a pyromaniac-{w=0.5}"
    #k "And a chuubibyou.{w=1}"
    #c "HEY!" with vpunch
    #c "{fast}HEY!{fast} That's so uncalled for!"
    #"Don't blame me. {w=0.3}Fire is cool."
    #"Just don't play with it."
    #"I won't.{w=1} Maybe."
    #"But at least be proud of me! We couldn't do any of that in real life!!!"

    #scene black with fade ##NOTE time: night. Three of you sitting down -- JD
    #play audio "audio/sfx/cracklingfire.mp3" loop fadein 1.0 

    #"After finally casting one spell, I referenced the process of it with other kind of spells."
    #"It took a while,{w=0.3} but I can finally cast a few basic spells{w=0.3}, ones that are easier to pronounce."
    #"I can heal,{w=0.3} slow down enemies,{w=0.3} and nullify poison.{w=0.3} {w=0.5}Most of the spells that are almost innate are water-based."
    #"It makes me wonder if it's connected to our astrology trait.{w=0.5} Does it connect to the fact that I'm a Libra?"
    #"Kurt told me to hold back from practicing too much since we still don't know how much mana I've already consumed."
    #"Not to mention the consequences of draining one's mana. I might pass out if I ran out of juice."
    ####------------------------------------------------------------------------------------------------------

    # to Devs/Dataminer, from this point on, it's Rica's territory

    label choices2:
    scene black with dissolve ##NOTE time: night. Three of you sitting down -- JD
    
    "While I was practicing, the two gathered enough bark to last for the night."
    "The only thing missing is my Pyroblast. {w=0.3}I took care of that by casting it so we'd have light for the night."
    play audio "audio/sfx/cracklingfire.mp3" loop fadein 1.0 
    "We sat down in silence, listening to the crackle of wood in the dusk of the night."
    "The silence seem to stretch endless{w=0.3}, until I gathered the courage to speak."
    c "Hey."
    c "Sorry...{w=0.3} I couldn't help out back there."
    k "It's fine{w=0.3}, you've got a complicated role."
    l "So, are we just gonna ignore the elephant in the room?{w=0.3} Act like it's normal to be transported in a video game?"
    k "..."
    c "I mean{w=0.3}, I've been kinda waiting for this.{w=1} Daydreaming the possibility of {i}this{/i} happening."
    k "That is such a chuunibyou thing to say, Cleo."
    c "Let me have my fun{w=0.3}, we don't know how long I get to enjoy this-"
   
    stop music fadeout 3.0
   
    "And as if I said something sensitive, the air fell silent once again."
    "Atmosphere felt stiff for a while. Their faces stuck in an expression that was hard to read."
   
    play music "audio/music/Breeze.mp3" fadein 1.0
   
    "Ah.{w=0.5}{p} ...We don't know how long we'll be stuck here."
    "They seem to realize before me{w=0.3}, that there might be no way home."
    l "What{cps=10}...{/cps}do you think happened in our world? {w=1}In our original bodies?"
    c "...This must be a dream."
    k "Then are we sharing the same dream?{w=1} It wouldn't make sense."
    k "Everything we experienced so far felt...real. Too real."
    c "{font=LinBiolinum}{sc=2}Oh, man.{w=1} what would Mom say?{/sc}{/font}"
    l "We're in another world, and the first thing that comes to your mind is what excuse you'd have for disappearing?"
    c "Old habits die hard.{w=0.5} I'm so used to not being able to go out without permission.{p}And disappearing without a reason already feels like a crime."
    l "How are we gonna go home?"
    k "Can we...{w=0.5} even go back?"
    "The atmosphere felt heavy and heavier the more we tackled about the topic. I can tell Kurt wanted to change the topic already."
    c "It's getting too much to think about. {w=0.5}For now, it's better if we focus on adapting to our environment first.{p}Then figure out how we got here in the first place, and if there's any way to go back."
    l "But-{w=0.5}{nw}"
    k "Cleo's right. {w=0.5}Try not to think too much about it.{w=0.5} It'll get you nowhere."
    c "I suppose we should call it a night then?"
    k "One of us should keep an eye out."
    l "...Alright."
    l "Oh, hey,{w=0.4} isn't this our first sleepover?"
    c "I guess it is, HAHA!"


    "Being transported in this world might be too much to think about{w=1}, but I guess it isn't so bad."
    "I was afraid letting the thoughts seep through their mind is going to be harmful."
    "Kurt knew that.{w=0.5} And he didn't let Louise entertain the thoughts before more harm is done."
    "Because thinking too much about it will get us killed in this world."
    "Death...huh."
    "{i}If we died in this world, what would happen then?{/i}"
    
    scene sleepover with fade ##NOTE two of you laying down, sleeping(?) -- JD
    
    "What brings comfort to me is that-{w=0.5} I'm thankful I'm not alone."
    "Especially that I'm with my best buddies."
    "We're a chaotic lot yet these two are reliable in their own unique ways."
    "Louise and I exchanged more banters before finally saying good night, before he slowly drifted off to sleep."
    "Kurt stayed awake, scouting and looking over us while we rest."
    "Thoughts flew over my mind as I watched the stars above."
    "{i}It's difficult to fall asleep in a place far away from home{/i}"
    "Kurt probably knows this too."
    "Maybe that's why he volunteered?"
    "In any case, I'm grateful to have someone reliable to watch our backs."
    c "If you feel like sleeping, don't hesitate to wake us up to switch with you."
    k "... Thanks, but I got it."
    "I smiled to myself, thinking I'm lucky to have these two at my side right now."
    "Had I been alone, I probably wouldn't last longer than an hour."
    "Despite being away from our home, being together with people you trust feels like a safe haven."
    "A group of friends that I can call 'home.'"
    "Cringe, huh? I really should go to sleep."

    scene black
    stop audio
    stop music fadeout 3.0
    with dissolve

    $ renpy.pause(2, hard=True)
    $ quick_menu = False

    call screen save_your_progress_bitch1
    with dissolve

    scene black
    with dissolve

    play audio "audio/sfx/riser3.mp3"
    show text "{glitch=5.0}{size=+100}{i}CHAPTER 1...{/size}{w=3}{/i}{/glitch}" at grow_text
    $ quick_menu = False
    pause(2)
    
    scene gathering ##NOTE gathering berries, the three of you. -- JD
    pause(1.5)

    play music "audio/game music/exploration.mp3" fadein 3.0

    $ quick_menu = True

    "It was a necessity to have a skill in foraging.{w=0.5} In which case, we're not so knowledgeable enough to do so."
    "But we all came to an agreement to let Louise taste test the berries and fruits we find along the way."
    "Not because we hate him{w=0.3} but because his species have higher tolerance when it comes to poisons."
    "Louise basically became our walking 'edible or not edible' radar."
    "Besides, even if he's poisoned, I can always cure him.{w=0.5} To a certain extent that is."
    "After resting,{w=0.5} we decided to continue our path towards the castle."
    "We can tell we're getting closer each time we notice the lack of grass in our paved path."
    "Of course,{w=0.3} it's inevitable to encounter hurdles along the way.{w=0.5} In which case, slimes.{w=0.5} We're lucky they were just slimes."
    "If it were wild animals or monsters,{w=0.5} we'd be overpowered."

    scene cramped with dissolve##NOTE three of you walking side by side -- JD

    c "By the way,{w=0.3} how are you guys holding up playing as a game character?{p}Because I'm sure having trouble."
    c "Shouldn't we practice?{w=0.3} Y'know{w=0.3}, to test our skills?"
    k "Normally, I would've said no because we need all the energy we have{w=0.5}, but that's actually a reasonable thing to do."
    l "True.{w=0.3} We can't let our guard down here{w=0.3}, I don't want to be a fodder for slimes."
    k "Personally, I wanted to try being a Mage myself{w=0.4}, but being a warrior isn't half bad." ##insert kurt trying out his sword -- JD
    k "You think I can wield two swords?"
    c "What{w=0.2}, you planning to be Kirito?"
    l "It's written all over his face{w=0.4} {sc=2}{i}HAHAHAHAHA!{/i}{/sc}"
    k "I am not planning to be Kirito.{w=0.5}"
    k "Because- {w=0.3}{nw}"
    
    k "{cps=30}I{w=0.3}{/cps}{nw}" ##insert smug kurt  -- JD
    k "{fast}I {fast}{cps=30}{i}AM{/i}{w=0.3}{/cps}{nw}" ##insert smug kurt  -- JD
    play audio "audio/game sfx/awkward.mp3" volume 3.0 noloop 
    k "{fast}I {i}AM{/i}{fast} {cps=30}Kirito.{/cps}{w=0.7}"
    
    
    k "Starburst Stream!{w=0.7}" ##insert slashing sword sfx  -- JDs
    c "And he calls me chuunibyou.{w=0.7}" ##insert rica looking at louise while pointing at kurt -- JD
    l "If Cleo's a chuunibyou{w=0.3}, you're goddamn delusional." #insert smug louise -- JD
    c "Tru dat.{w=0.7}" ##insert smug rica -- JD
    k "Is it still being delusional at this point?{w=0.5} I wiped the floor upfront."
    l "Those were slimes."
    k "And you were struggling to support against slimes."
    l "{sc=2}HUUUUH?{/sc}{w=0.7}"
    l "{sc=2}SINCE WHEN DO YOU SEE A SUPPORT GO FRONT?{w=0.3} DO YOU EVEN PLAY GAMES?{/sc}"
    l "{sc=2}I only followed you in front because I thought you'd get your ass handed.{/sc}"
    c "We {i}WERE{/i} pretty lucky to get out of there alive.{w=0.5}"
    c "At times like these{w=0.3}, I think it's best to have plans before engaging battle."
    k "Agreed. Jokes aside, we should come up with a formation based on our best abilities."
    c "Since I am a mage{w=0.3}, I'll stay in the backline."
    c "I'm not good with close combats{w=0.3}, and casting spells take time."
    k "Since I'm your one and only Kirito--{w=0.2}{nw}" ##insert smug kurt -- JD
    c "{cps=50}{i}And where's your Asuna?{/i}{/cps}{nw}" ##insert smug rica -- JD
    k "Shut up.{w=1}" ##insert rolling eyes kurt -- JD
    k "{i}*Ehem.*{/i}{w=1} As I was saying{w=0.3}, since I'm the only one with a sword, I can cover the front."
    l "I think I'm more of a support{w=0.3}, so it's better if I stay at the back{w=0.3}, just in front of Cleo and behind you."
    k "Louise do be backsitting.{w=0.5} Just like his hairline.{nw}" ##his expression is more understandable with this image https://en.meming.world/images/en/1/17/Monkey_Puppet.jpg -- JD
    l "{sc=1}Okay, Kurt.{w=0.5} You were asking for it.{w=0.4} Cleo{w=0.2}, don't give the man any healing potions.{/sc}"
    k "{sc=2}Oi, you're not serious, right?{/sc}"
    k "{sc=5}I was only joking!{/sc}"
    c "Hoi, we still have to come up with a formation and practice!"


    "The banters went on for a little longer{w=0.4}, but eventually we went back on the right track.{w=0.5} Louise and Kurt mostly covered up the formation planning while I helped with how Kurt handles his sword."
    "Back in the real world,{w=0.4} there was a time we were swinging a baseball bat as a part of our PE activity. I remember Kurt having trouble swinging the bat."
    "Which served as a reference to advice Kurt."
    c "Swinging upward will tire you more than swinging downwards."
    k "Right,{w=0.3} because gravity helps when it's swung downwards."
    l "Plus,{w=0.3} it adds impact to your every attack."
    c "But swinging upwards isn't entirely bad,{w=0.5} you could use it to parry like you did when we first got here."
    c "Just try to hold a proper form when wielding your weapon. Otherwise, it could hurt you as well."
    k "Alright,{w=0.3} thanks for the insights."

    "As for Louise, we're not exactly the best people to help Louise with his potions."
    "Plus, Louise is nerdy enough to figure it all out."
    "We can leave it up to him,{w=0.5} right?"
    "{cps=8}...Right?{/cps}{w=1}"

    ##TODO screens here showing spells, mana, encantation -- JD

    "In my case,{w=0.5} spells{w=0.3}, mana{w=0.3}, and encantation{w=0.3} are things that I'm still unfamiliar with. I wonder, if JD was sent with us,{w=0.5} would he have done better than I will?"
    #oi, are you trying to say something here -- JD

    #scene practice with dissolve -- JD
    "I wonder, if it's only just us three that was sent in this world."
    #oh nvm -- JD
    "I should discuss this topic with those two later."
    "What if someone we know got sent here and is alone?"
    "Oh no, what if it was my sister?-{nw}"

    scene practice2 with dissolve

    l "{bt=5}Oi{/bt},{cps=7} Cleo-{/cps}{w=0.3} focus!"
    c "Oops{w=0.3}, where was I again?"
    l "You're supposed to fire some Pyroblasts.{w=0.5} Three times in a row."

    scene practice3 with dissolve

    c "{sc=3}T-{w=0.3}THREE TIMES IN A ROW?!{/sc}"
    
    scene practice4 with dissolve
    
    l "You were already able to shoot it twice in a row,{w=0.5} let's try three!"
    "He said that with a smiley face. {sc=3}A SMILEY FACE.{/sc}"
    "That just means he doesn't know how much difficult it is to me!"
    "He's {cps=24}{i}{bt=5}waaaaay{/bt}{/i}{/cps} too enthusiastic about this!"
    "{sc=3}YOU DON'T SEE THE RISKS YOU'RE PUTTING ME IN, LOUISE!!!{/sc}"

    c "Y-You better take responsibility if I pass out!"
    k "Take it easy,{w=0.2} you two.{w=0.5} Don't push her too much,{w=0.3} we still need the energy to walk."
    l "{bt=5}Okaaaaay.{/bt}"

    
    
    play sound "audio/game sfx/spell3.mp3"

    scene practice5 with dissolve

    "But regardless,{w=0.3} I took a deep breath and focused at the edge of my staff."
    "And as if it was natural,{w=0.3} I enchanted the words:"
   
    scene black
    with dissolve

    play audio "audio/sfx/click2.mp3"
    show text "{glitch=5.0}{size=+100}{i}{swap=Equinox@Pyro@0.2}Atralis{/swap} {swap=Harmonia@Burn@0.2}Venara{/swap}...{/size}{w=3}{/i}{/glitch}"
    $ quick_menu = False
    pause(2)

    hide text with dissolve
    $ quick_menu = True
    play sound "audio/game sfx/spell2.mp3"
   
    scene practice6 with dissolve

    "{sc=2}{i}{font=naganoshi.ttf}「{/font}Infernus Sphera{font=naganoshi.ttf}」{/font}{/i}{/sc}"

    "Channeling mana through my staff,{w=0.4} I felt the heat gathered at the tip of my weapon."
    "The wind surrounding my staff swirled,{w=0.4} pulling the air in."
    
    scene cleo_fireball with dissolve
    play sound "audio/game sfx/spell.mp3"
    
    "Once I felt the condensed power of my mana{w=0.5}, I pointed at the air and released my spell."

    play sound "audio/game sfx/flame2.mp3"
    pause(0.2)
   
    scene cleo_fireball2 with dissolve and vpunch and hpunch
    
    "A ball of fire was emitted at the end of my staff.{p}It was so much larger than what I previously casted a few days ago."

    scene cleo_fireball3 with dissolve
    
    c "What the-{w=1}{nw}"
    "..."
    
    scene forest ##three of you together in one scene -- JD
   
    "EH.{w=1}"
    k "WHAT WAS THAT?!"
    c "I-{w=0.1}I DON'T KNOW!"
    k "You're lucky you missed,{w=0.3} otherwise you'd burn the forest!"
    c "Guh.{w=0.3}"

    

    l "I hope no one got hurt by that huge hurling ball of fire."
    c "I guess you could say, that was a {w=0.5}"
   
    play audio "audio/sfx/bell.mp3"
    
    c "{fast}I guess you could say, that was a {w=0.5}{i}{fast}{cps=26}ligaw na bala.{/cps}"
   
    play sound "audio/game sfx/bonk.mp3"
   
    "BONK!" with hpunch
    k "There's a time and place for jokes, y'know.{w=0.5} That could've turned into a disaster."
    l "True.{w=0.5} Damn, that scared me."
    c "Sorry.{w=0.3} I really didn't know what came over me.{w=0.3} I didn't intend to cast it that big." 
    k "What do you mean?"
    c "I was chanting the same words I used to cast Pyroblast but somehow,{w=0.5} it turned into whatever {w=0.3}{i}THAT{/i}{w=0.5} was."
    k "Well, whatever.{w=0.3} Let's just stop for now."
    k "Like I've been saying,{w=0.3} let's try conserving our energy."
    "We were nowhere near the castle yet, so he's right about conserving energy."
    "Louise and I nodded in agreement, and that seemed to have ended the conversation."

    scene exploration with fade ###NOTE you three walking -- JD

    "After a few minutes of prepping,{w=0.3} we continued walking once again."
    "It's almost a cycle at this point.{w=0.5} Rest,{w=0.3} walk,{w=0.3} eat,{w=0.3} sleep,{w=0.3} and repeat."
    "We encountered less slimes compared to where we started our journey."
    "This could mean that we're getting closer to the castle."
    
    stop music fadeout 2.0
    scene castlegates with fade #NOTE
    queue music "audio/game music/exploration2.mp3" fadein 1.0

    label choices1:
    
    l "Wow..."
    "The castle welcomed us visitors with its huge open gates."
    "Albeit its colossal size intimidated me."
    k "Let's find a place where we could stay the night."
    l "Yeah. But where would we look first? {w=0.7}This place is {cps=10}{sc=2}HUUUUUUGE.{/sc}{/cps}"
    c "We could always just ask."
    "I look around to see the perfect candidate to ask."
    "There, at cabbage stall was a guy slightly taller than me."
    c "Excuse me."
    u "Yes?{w=0.4} How may I help you, young lady?"
    "{i}Hihihi, he called me a lady hihihihi.{/i}" #insert smug cleo
    c "Do you know a place where we could stay the night?"
    u "There's a bulletin board at the Plaza.{w=0.3} A map is posted there to help you lot with directions."
    u "Not to mention, requests from people who need favors done for 'em."
    c "I see! Thanks a lot, mister!"
    "We thanked the man, bowing our heads." 
    "We headed to the Plaza, and it was then that we realized it was more packed in here than it was at the entrance."
    "Different creatures,{w=0.5} great and small,{w=0.5} of different color{w=0.3} and different shape."
    "They all looked so unique."
    k "Ooh, look here.{w=0.4} Thankfully, there's a lot of options to pick."
    l "And some quests to take on too."
    c "But first,{w=0.5} can we eat?"
    k "Heh.{w=0.4} Yeah, sure.{w=0.3} Why not?"
    l "Yey!"
    "Luckily enough, we had some money on us. Which was- of course- {i}weirdly convenient{/i}.{p}It came with our gears and weapons when we were transported here."
    "But everything that has happened so far is weird already.{p}There's no use in overthinking about it."
    "We struggle to find our way into a bar that also happens to have an inn for travelers to take rests."
    "By the time we got there, we were already exhausted."

    label choices4:
    
    ##11-07-2024 --Shizo (adding dates so I wouldn't be confused)
    ## 分かった！-- JD
    
    u "Hm?{w=0.5} Oho!{w=0.5} Welcome!{w=0.3} Come right in,{w=0.3} sit here and relax."
    c "Uh---{w=0.1}{nw}"
    u "Take your time and call me when you have an order. {bt=2}{i}Mmmkay?{/i}{/bt}"
    "Oh my- those are some big knockers--{nw}"
    "I mean, what?-"
    k "{i}Si Cleo oh, titig na titig.{/i}"
    c "Hoi-{w=0.2}{nw}"
    l "What did you expect, {i}Cleo 'yan eh.{/i}"
    c "{sc=3}I WAS LOOKING FOR A NAMETAG???{/sc}"
    k "..."
    l "..."
    "{sc=3}OF COURSE THEY WOULDN'T BELIEVE ME!{/sc}"
    "REALLY? A NAMETAG IN THIS WORLD???"
    "THINK, CLEO, THINK!"
    "A big dommy mommy appears right in front of us, TO WELCOME US- and WHO WOULDN'T BE LOOKING AT HER ABNORMAL KNOCKERS?"
    "IT'S LITERALLY PEEKING THRUOUGH HER DRESS!!!"
    "PARDON MY WAY OF DESCRIBING HER BUT-{w=0.5}{nw}"
    "GOD." with vpunch
    "{fast}GOD.{fast} BLESS." with hpunch
    "{fast}GOD. BLESS.{fast} {sc=4}{size=+10}WOMEN!{/size}{/sc}{w=0.5}" with vpunch
    "IS THAT EVEN NATURAL?{w=0.5}{nw}"
    "Yeah, no way it's artificial- {sc=3}CAN MAGIC DO THAT??{/sc}"
    k "I think we should pick something now before someone starts drooling."
    c "I'm literally just hungry."
    l "We're not sure which you'd wanna eat though."
    c "Can we stop talking about this?!{w=0.3} She's literally right there,{w=0.3} who knows if she could hear us?!"
    k "She seems too busy to eavesdrop."
    c "Let's just get some food please."
    "We finally decided on the menu, Kurt was the one who called her because I cannot-{w=0.7}{nw}"
    "For the love of God-{w=0.5} NOT{w=0.5} be nervous interacting with women!"
    "My history of female relationships just broke me to the point I can't act normal in front of them."
    "Not history as in{sc=3} A ROMANTIC RELATIONSHIP WITH THEM-{/sc} FRIENDSHIP IS WHAT I MEANT-"
    "I should just stop thinking now,{w=0.5} stop talking to myself."
    "No thots,{w=0.5} just hed empty."
    l "Is this where we also get to sleep?{w=0.5} I'm getting drowsy."
    k "Ah, yeah.{w=0.5} I asked the lady earlier and we could sleep in for free tonight."
    c "Really?{w=0.5} Why?"
    "Kurt then wore a smirk that I just knew would spell trouble for me."
    k "She said we were intriguing and-{w=0.5} these were her words,{w=0.3} {cps=10}'adorable{/cps}'{w=0.3} lot."
    "Instinctively,{w=0.3} my eyes searched for her only to realize our eyes met."
    "She smiled,{w=0.3} acknowledging my gaze."
    "Wait,{w=0.5} why does it seem like she knew what we were talking about?"
    c "She really said that?"
    k "Nah, just messing with you.{w=0.3} Kinda wanna get some reaction off of you."
    c "Ha.{w=0.3} Ha.{w=0.3} Funny."
    k "But seriously though,{w=0.3} when I asked about the price for our stay,{w=0.3} she said that we intrigued her."
    l "Huh?{w=0.5} Why?"
    k "Dunno,{w=0.3} how should I know?"
    l "Well, whatever.{w=0.5} Should we introduce ourselves?"
    c "{sc=2}C-{w=0.3}Can you all do that without me? I'm not done eating pa oh.{/sc}"
    l "What do you mean not done? Finish it up already."
    c "{sc=2}O-{w=0.5}Okay...{/sc}"
    "The tavern was bustling with customers and yet the lady manages to attend to them one by one."
    "It seems they're short-staffed?"
    "The only employee I see other than her was the cook just behind this bar."
    "The tavern is still bustling with customers by the time I finished eating."

    ##11-15-2024 --Shizo

    "We paid for the food the room we're going to use. The lady instructed us where the room is located."
    u "Enjoy your stay!{w=0.5} Oh, and-{w=0.3} try not to break some things,  {bt=2}mmmkay? {/bt}"
    u "Because I had a customer-{w=0.5} A beastkin who's the same size as you accidentally broke one of my furnitures."
    l "{i}*gulp*{/i}"
    u "It was a handful,{w=0.3} really!{w=0.5} So, I implore you to be more careful than my last customer, {bt=2}hm?{/bt}"
    l "Y-{w=0.3}Yes."
    "She took off and went back to her work.{w=0.5} Meanwhile,{w=0.3} we watched over Louise's movements."
    "It'd be troublesome to pay twice just because of a broken furniture."
    "Thankfully,{w=0.3} it was spacious enough for us three to sleep in."
    
    play music "audio/music/solemn_study.mp3" fadein 5 volume 0.5 fadeout 3
    "It's nice to finally have roof above our heads after a few days spending the night out."
    "We took our time to relax until Louise broke the silence."
    l "What are we going to do now?"
    k "Good question."
    "Kurt grabbed something from his backpack.{w=0.3} It was a handful of papers."
    k "I took some papers posted on the bulletin board we saw this morning."
    l "Oooh."
    k "I need your suggestions which job we should take."
    l "Job?{w=0.5} You mean,{w=0.3} like quests?"
    "Louise and I looked over the papers.{w=0.5} Considering every requests that is doable in our level of expertise."
    l "I still think it's too early for us to take on these jobs.{w=0.5} Aren't there better and easy quests?"
    k "{cps=20}THESE{/cps}{w=0.3} are the easy ones.{w=0.3} The rest that we saw there required some dungeon-level expertise."
    l "Dungeon?{w=0.3} There's one here?{w=0.5} Oooh, it's like Dungeon Meshi."
    k "Yeah, It's where we take on different floors on the dungeon,{w=0.3} the deeper we go,{w=0.3} the higher the price,{w=0.3} and of course,{w=0.3} higher risk."
    "Louise sighed,{w=0.3} I did too.{w=0.5} There's nothing else that comes to mind right now,{w=0.3} so we laid our heads letting our minds wander."
    "..."
    "Hmm..."
    "Ah."
    c "Should we look for someone who could help us then?"
    l "Help?{w=0.5} How?"
    c "Like,{w=0.3} someone to join our team. Help us grind or farm, stuff like that."
    k "Where would we get the money to hire them though?"
    c "Urgh...{w=0.5} I didn't think of that."
    l "Another dead end huh."
    "Another sigh."
    "I took another look at the papers.{w=0.3} They all seem easy to be honest.{w=0.5} Doable by anybody new to adventure."
    "Like us."
    "The downside is,{w=0.3} the pay wouldn't be able to pay for our stay."
    "Hmm."
    k "Ah, what if we take on different quests separately.{w=0.3} They're all easy anyway but if we complete three quests,{w=0.3} the pay could cover our expenses. "
    l "I was just thinking about that as well!"
    c "Nice,{w=0.3} now we're on to something."

    "And so, we spent the night away talking about which quests fits us well, all the while keeping it to minimum wherein it's doable within the day."
    "There are six easy quests so far, it'll only take us at least two to three days to finish it all."
    "The pay is not so bad. We'd also learn more about the neighborhood, the people, and more about this world!"
    c "Tomorrow might just be the real deal. THE REAL ADVENTURE!"
    l "{sc=3}DOES BEING AMBUSHED BY SLIMES NOT COUNT AS AN ADVENTURE?{/sc}"
    c "HAHAHAHAHAHA! I was kidding of course."
    k "What she meant was{w=0.3}, tomorrow might just be the real journey because we finally have a solid plan to follow."
    l "Step by step.{w=0.5} I just hope that eventually we figure out our way home."
    k "Are you not enjoying your new form, Louise?"
    l "Well, not that I dislike it{w=0.4}, I'm just new to everything here like you are."
    l "I'm still trying to adapt.{w=0.3} It's just difficult to do that when everything here is completely different from back home."
    k "Well, we don't know how long we're staying here so{w=0.3}, we have all the time in the world to figure out stuff in here."
    l "Aren't you worried?"
    k "..."
    k "Of course I am{w=0.3}, we all are.{w=0.5} Just that, right now{w=0.3} what matters is what's in front of us."
    k "We won't be able to go home if we die here."
    k "So we should focus to where we are right now."
    c "And with that wonderful speech{w=0.3}, we should all go to sleep because we have to get up early tomorrow."
    l "Sabi nung laging puyat."
    k "Ulol{w=0.4}, parang ikaw hindi ah."
    l "Hehe."
    "We exchanged our good nights before going to bed.{w=0.5} And as usual{w=0.2}, it's never easy for me to fall asleep."
    "I've been having trouble sleeping even back in our world."
    "My mind keeps wandering until I fall asleep, just like it is right now."

    ##11-16-2024 --Shizo

    "A few thoughts crossed my mind until I eventually succumbed to drowsiness."
    "..."
    "The next morning{w=0.3}, Kurt was the first one to wake up.{w=0.4} Then me and of course, Louise was the last one to wake up."
    "We can't blame Louise for oversleeping{w=0.3}, it's been a while since we laid on a soft bed."
    "The sun peeked through our window, prompting me to take a look outside."
    "There, I saw the lively plaza.{w=0.4} I was then reminded of what we're supposed to do today."
    "We washed the sleep off of our faces and ate breakfast."
    k "Let's retrace what we talked about last night."
    k "Louise is assigned to help a guy named Rowan to deliver goods around the neighborhood."
    k "I{w=0.1}, on the other hand{w=0.3}, will gather materials for a blacksmith."
    k "Meanwhile{w=0.2}, Cleo has the most difficult job today."
    l "Which is?"
    k "She has to find a lost kitty.{w=0.5} Didn't we discuss this already last night, Louise?"
    l "Oops!{w=0.4} Sorry, I forgor."
    c "You really sure about this?{w=0.4} I can handle other quests."
    k "You don't get it, do you?{w=0.4} Finding lost things are already difficult{w=0.2}, more so if it's a living thing."
    k "Especially cats.{w=0.4} They roam around wherever they want."
    "This is the most boring quests I've ever been assigned to."
    "I just hope there's an entertaining backstory to every quest we take.{w=0.6} Not that this is a game though."
    "Could be just a simple missing cat scenario."
    l "I guess that wraps it all up then."
    k "Yes."
    c "Let's head out."
    "And so, we finally embarked on our quests."
    "Simple they may be{w=0.3}, it's better than risking our lives from the get-go without proper combat experiences."
    "We were lucky enough to have survived outside the castle."
    "Damn that spawn point."
    "..."
    ".."
    "."

    scene neighborhood with fade

    # Louise's POV -- shizo
    
    "I'm trying to find reason why I was assigned to carry stuff.{w=0.7} But I guess it's because of my physique."
    "Back in our world{w=0.2}, I can carry things just fine but here{w=0.3}- I can't even recognize my own strength."
    "I could carry a boulder if I wanted to.{w=0.4} Not that I would."
    "I just feel like I could."
    "Oh, wait.{w=0.3} Where am I supposed to go again?{w=0.4} Is it{cps=9}{i}...here?{/i}{/cps}"
    "No, wait- Am I lost?"
    "WAIT, IF I'M LOST-{w=0.4} WOULD CLEO AND KURT POST A MISSING DOG POSTER?"
    "..."
    "Let's not let that happen.{w=0.4} Now, back to where I was."
    "It took me a few more turns before finding the right address."
    "I had to ask about directions too{w=0.3}, which was mentally exhausting."
    l "Hello, excuse me but are you Mr. Rowan?{w=0.5} I'm here to help you with your request."
    u "Oh... is that so?..."
    l "Is there... something wrong?"
    u "Unfortunately, yes.{w=0.4} I was just about to deliver half of the goods but as I was getting to it{w=0.4}, the cart was completely broken."
    u "I've been using it for years.{w=0.5} Must've been worn-out."
    l "I-I see."
    "What now? I'm not sure if I'm capable to fix his cart."
    l "Do you know anyone who could fix it?"
    u "No, but even if I do{w=0.3}, there wouldn't be enough time to deliver all the vegetables.{w=0.5} It has to be today or they won't be fresh anymore."
    l "Hmmm."
    l "Is there anything else we can use to carry it?"
    u "C-Certainly{w=0.}, I have sacks to use but carrying the goods all over the town would be exhausting."
    l "I'll carry the sacks.{w=0.4} You'll help me hand it over to the customers."
    u "That{w=0.4}{cps=9}...That{/cps} just might work.{w=0.5} Are you sure you can endure it?"
    "Honestly, I'm not sure.{w=0.5} But I'm already here and it's too late to back out."
    "We also need the money.{w=0.4} Besides, I won't know my limit if I don't give it a try."

    # Kurt's POV -- shizo
    



    "..."
    ".."
    "."
    ""
    ""
   
    stop music fadeout 0.5
    jump chapter7 
    return
