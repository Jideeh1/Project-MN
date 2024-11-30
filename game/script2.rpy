python:
    import os

default persistent.game_played = False

label chapter7:

    scene black
    $ renpy.pause(1, hard=True)
    play sound "audio/sfx/click2.mp3"
    scene white
    window hide
    window show Dissolve(1)
    $ renpy.pause(1, hard=True)

    jd "The hell!?"
    jd "Where the hell am I?"
    $ renpy.pause(2, hard=True)
    # show scenery of fantasy world here
    jd "Oh, you've got to be kidding me."
    play sound "audio/sfx/riser2.mp3"
    $ renpy.pause(4, hard=True)
    window hide
    scene black

    $ renpy.pause(2, hard=True)
    window show Dissolve(1)
    play music "audio/game music/tavern.mp3"

    "It's been days since that incident."
    "I don't know what happened, or what caused it{w=0.4}, but all I know is that I want to go back home."
    "Don't get me wrong, here.{w=0.4} I've dreamt of being isekai'd, and loved the idea of going in an endless adventure."
    "But actually experiencing this fantasy for myself...{p}Where do I even begin?"
    "For starters{w=0.4}, WHERE THE FUCK DOES ONE FIND A DECENT TOILET!?"
    "I mean{w=0.3}, {sc=2}why did it not occur to me that a world like this might never have the privilege of modern toiletry!?{/sc}"
    "If I'm going to be stuck in this world{w=0.3}, the only thing I want is a proper toilet to relieve myself.{p}{sc=1}Is that too much to ask for?{/sc}"
    "It took me three days to find a town{w=0.5}, but even then{w=0.3}, {sc=2}their toilets were still horrible.{/sc}"
    "{sc=1}I wanna fucking go home so bad.{/sc}"
    # show jd dead tired
   
    scene town with dissolve
    $ renpy.pause(1, hard=True)

    "The toilet conundrum aside{w=0.3}, this world genuinely looks nice."
    "It's civilized, but not as advanced and progressed as the world I came from.{p}But that's the charm of it."
    "There aren't a lot of tall buildings{w=0.2}, so the cloudy sky is vastly exposed."
    "The ground is rough{w=0.2}, but not cemented.{w=0.3} Just a ground with sprouts of grasses growing in between the soil grains."
    "The world's architecture still seems to be in their primitive phase{w=0.4}, using wood and stones as foundation to make homes."
    "Having city buildings and modern houses back in my world{w=0.3}, this scenery is really refreshing."
    "Though I kept being reminded of my province back in Mindoro because of the similarities{w=0.3}, this world is actually very different compared to Earth on a closer look."
    "If the Earth is widely progressed--{w=0.2} enough to explore places beyond its own planet{w=0.3}--then this world would be considered at the higher medieval era."
    "A stark contrast to our world{w=0.3}, except I can see why the humanity's progression here is experiencing a paralysis."
    "For starters{w=0.3}, this world has its own mysteries.{w=0.4} Its got monsters{w=0.2}, its got magical artifacts{w=0.2}, and things that are considered supernatural on Earth{w=0.3}, is nothing but normal here."
    "Because of the various things in this world that doesn't exist on Earth{w=0.3}, they were able to imitate sixteenth of our progression.{w=0.4} But resulted in the paralysis of their worldly evolution."
    "An example of this is:{w=0.3} back on Earth, to use electricity{w=0.2}, you'd need something to generate electricity.{w=0.3} You'd have to build your own source to get what you want{w=0.3}, and that's why machinery and architecture is so complex in our world."
    "But in this world{w=0.2}, electricity is a mere magic spell."
    "In the same way they used spells and materials of this world{w=0.3}, they were delayed of the evolution they could've had."
    "These are, of course{w=0.2}, just my speculations."
    
    scene black with dissolve

    "I came to this world when I fell asleep on the couch after watching a show{w=0.3}, thinking this was all but a dream."
    "But lo and behold{w=0.3}, its been a day and I hadn't woken up."
    "I would have been dancing in joy finally escaping from my reality had it not been for {i}various complication in this world.{/i}"
    "One{w=0.3}, I did mention the toilet conundrum."
    "Second{w=0.3}, I don't fucking know how to cast spells{w=0.3}, so the magic of this fantasy world is ruined."
    "Third{w=0.3}, monsters.{w=1}"
    "And just mentioning the 2nd and 3rd problem{w=0.3}, you already know the conclusion of this story."
    stop music fadeout 1.0
    stop sound

    scene jideeh_running with dissolve
    play music "audio/game music/tavern2.mp3"
    scene jideeh_running with vpunch
    play audio "audio/game sfx/deathsplash.mp3"
    
    jd "{sc=2}{i}SHIIIIIIIIIIITTTT!!{/i}{/sc}"
    jd "{sc=2}{i}THIS IS SO LAAAME{/i}{/sc}"

    play audio ["audio/game sfx/deathsplash.mp3", "audio/game sfx/deathsplash2.mp3", "audio/game sfx/deathsplash.mp3"]

    jd "{sc=3}{i}WHY AM I RUNNING AWAY FROM SLIMES!??!{/i}{/sc}"
    jd "{sc=2}{i}This is so fucking laaameeee!{/i}{/sc}"
    
    "Yep.{w=0.5} I was chased around by monsters the whole day.{p}Lesson learned{w=0.2}, {i}DO NOT{/i} underestimate slimes.{w=0.3} They are more dangerous than how we depicted them in tv shows."
    
    scene black with dissolve

    "The first and second day in this world{w=0.3}, not great so far."

    "I slept at the branches of a tree that I found{w=0.3}, just to keep myself safe from any monsters."
    "Even feeling a bit safer during the night{w=0.3}, I still couldn't sleep because of the prickling offshoots stabbing me at the back."

    scene jdexploring with dissolve

    "At the dawn of the day{w=0.2}, I still felt sleep-deprived and exhausted."
    "But if I stayed here any longer{w=0.3}, I'm seriously not gonna survive in this godforsaken world."
    "To find the nearest town{w=0.3}, I had to look for paved roads to find a lead to a town."
    "All the exhaustion I pent up held me back from climbing any trees.{w=0.3} I was that exhausted."
    "But as if to add salt to injury{w=0.3}, the nearest town was probably days away of walking."
    "I didn't want to perish in the middle of nowhere{w=0.3}- not to mention in an unknown world{w=0.3}- so I spent the whole day walking{w=0.2} and walking{w=0.2} and walking."
    "The world is so medieval{w=0.3}, that they haven't invented proper roads yet{w=0.5}, and so the paved road I walked on was rough and uneven."
    "I have never felt so tired in my life.{w=0.3} Ever.{w=0.3}"
    "And get this!{w=0.3} Before I got inside the town{w=0.3}, some people were scowling at me."
    "They wore the biggest frown they had at the sight of me."
    "It wasn't long before I noticed that it's because of my skin.{w=0.5} It's red.{w=0.3}{p}I guess discrimination isn't non-existent in this world too."
    "This town is named Silvercrest{w=0.3}, and I was told by one of the Guards that I may be treated like scum{w=0.3}, but this is the least racist town on Aetheria.{w=0.3} That just makes me feel even worse."
    "On the offnote{w=0.2}, Aetheria is the equivalent term of Earth of this planet."
    "Though discrimination may still exist here{w=0.3}, the inhabitants of this world is seriously a selection."
    "The people here wore a skin with scales{w=0.5}, hide{w=0.3}, fur{w=0.3}, and other animal-like traits that freaked me out to no end."
    "They spoke an unfamiliar language that sounded gibberish to my ears.{p} But strangely{w=0.3}, I understood every words they said."
    "But that didn't mean it wasn't bizzare.{p}It's like hearing your language in a horrible accent."
    "Except this language is very new to me.{w=0.3} Yet I understand every{w=0.2} single{w=0.2} word."
    "With all the people in various species were in view{w=0.4}, I couldn't help but wonder what I am in this world."
    "Conveniently{w=0.2}, there's a place besides the town's gate{w=0.3}, a race appraisal shop."

    scene 店 with dissolve
    play sound "audio/sfx/storechimes.mp3"

    "When I visited the shop{w=0.3}, they only required you to look in the  mirror, and they'd be able to tell what you are."
    "That's pretty neat and all{w=0.3}, but I haven't had a good look of myself for a while now."
    "For one{w=0.2}, I knew I had reddish skin{w=0.3}, but I don't know how differently I'd look like compared to myself in the real world."
    "And aside from my skin being reddish{w=0.3}, it had scales.{w=0.5} Tough and hard scales.{p}Plucking them off hurt{w=0.3}, a lot."
    "I came to this world with a grayish robe accented by a brown leather{w=0.3}, and a bountiful sapling staff."
    "But aside all of those things{w=0.3}, I didn't really know how I look like right now."
    # show screen mirror (me in the view)
    "And that's when I found out I had two protruding horns on my forehead.{p}Horns as pointy and sharp as a needle."
    "My face didn't have any scales{w=0.3}, but the irises of my eyes changed.{p}My irises were yellowish{w=0.3}, and instead of having an orb-like pupil{w=0.3}, I had a slithed one."
    "The store appraiser told me that I'm a Tiefling{w=0.3}, but unlike any other Tieflings{w=0.3}, I didn't inherit their scary eyes."
    # hide screen mirror
    "Because despite having different irises and pupils{w=0.3}, I still retained the humanly sclera.{p}Tieflings are known for having it as black."
    "Tieflings{w=0.1}, because of their bizarre eyes{w=0.3}, is actually naturally good at seeing in the dark.{p}What more, they are proficient in fire as well as resistant to it."
    "Because of their naturally hard and tough skin{w=0.3}, they were adept of being a warrior, but they were mostly comprised of the likes of sorcerers."
    "The appraiser went on and on about the history of Tieflings{w=0.3}, until it was time for me to go."
    
    stop music fadeout 3.0

    "Unironcially, I'm glad the shop appraiser wasn't racist."

    scene black with dissolve

    "I never had the time to check if I really couldn't conjure any spells{w=0.3}, but I doubt that would be the case when the appraiser told me I had an affinity for fire."
    "Though I'm new to the world{w=0.3}, so I'm still as clueless as a baby on how magic works, and how this world functions."
    "I'm gonna need an instructor for this.{p}Fortunately{w=0.2}, the town's guild was a 3-minute walking distance from here."
    
    scene guild with dissolve
    play music "audio/game music/inn.mp3" fadein 1.0

    u "What did the kid say again!?"
    u1 "He says he's a sorcerer, yet he doesn't know how to cast spells."
    u2 "Kid, are you pullin' my leg?{w=0.5} Look, I wasn't born yesterday.{w=0.3} Is this some kinda prank?"
    u "{sc=1}{i}HAHAHAHAHA{/i}{/sc}{p} Oh, you've got a real sense of humor, kid.{w=0.3} I'll give 'ya that." with vpunch
    jd "ah- {sc=1}{i}ahehehehe...{/i}{/sc}{p}You may not be born yesterday{w=0.3}, but would you believe it if I said I was?" #insert conflicted jd here
    u1 "And there he goes again."

    scene black with dissolve

    "After explaining my situation{w=0.3}, they seem to think I'm just an amnesiac who dropped my sanity along the way here."
    "They're rowdy{w=0.3}, full of life and a bit unhinged{w=0.3}, but they're kind enough to lend a hand."

    scene guil with dissolve

    u "So let me get this straight{w=0.3}—you don't know how the world work because you might have a case of amnesia?"
    
    "It's exhausting trying to keep up with all their questions{w=0.3}, so I just went with the 'lost memory' story."

    u2 "Tell 'ya what, kid{w=0.3}, I'll teach ya some magic myself if I hafto.{w=0.5} But in exchange{w=0.3}, you'll carry our luggage for a week."
    jd "What's the {i}other{/i} catch?"
    u1 "With that clueless look of yours{w=-0.3}, you'd be here forever tryin' to find an instructor.{w=0.5} You'd probably end up as some poor grunt in one of those cutthroat groups."
    u1 "The only catch is you get to have what you want, and we live guilt-free.{w=0.5}"
    u2 "He's right.{w=0.3} Telling us about your situation and refusing to help{w=0.3} makes us indirectly responsible for what ever happens to you."
    jd "Wow.{w=0.5} You guys sure sound like responsible adults even without looking the part."
    u2 "{sc=1}{i}HAHAHAHAHA!{/i}{/sc}{w=0.3} You've got some guts telling us that.{w=0.3} I like this kid!" with vpunch
    jd "I may not look it{w=0.2}, but I can carry a luggage or two.{w=0.3} With that said, I want to accept your offer."
    u2 "Hol' on jus a minute, kiddo.{w=0.3} Before we shake on it{w=0.2}, I've got one question for ya."
    jd "I'm already signing up to be a glorified pack mule{w=0.3}, what's left to ask?"
    u "He just wants to see where your head's at{w=0.3}, to figure out what kinda basics you might already know."
    jd "I thought already told you I lost my \"memories,\" {w=0.4}but alright{w=0.3}, fire away."
    u2 "Okay Lad,{w=0.2} this a simple question.{w=0.7} Between a mage{w=0.3}, a wizard{w=0.3}, a warlock{w=0.3}, and a sorcerer{w=0.3}, what is da difference?"

    "...{w=1}"
    jd "{sc=2}I-{w=0.3} uh...{/sc}"
    "Ah, shit.{w=0.7} I have not prepared for this question at all.{w=0.5} Not a single thought."
    "I broke out in a cold sweat when I realized {w=0.3}{i}I had absolutely no idea how to answer this."
    "I mean{w=0.3}, shit, it's not like I play dungeons and dragons.{w=0.4} And they're commonly interchangeable.{w=0.3}{nw}{p}{sc=2}{i}so what the hell is the difference!?{/i}{w=1}{/sc}"
    
    jd "{sc=2}T-the mage is-{w=0.5}...{w=0.3} a-and the wizard...{w=0.4}{/sc}"
    u "You took in one clueless baby, Lain."
    u2 "It's gonna be a long day.{w=0.3} Vax, lay it down for him."
    u1 "Alright, kid, listen up.{w=1} Mages?{w=0.4} They go through years of training to master magic.{w=0.3} Wizards are like mages, but more specialized."
    u1 "Sorcerers? They don't need to study magic—{w=0.3} it's just in their blood.{p}And warlocks?{w=0.4} They make pacts with powerful beings to borrow their magic."
    u1 "That's magic 101 for 'ya kid.{w=0.4} You got it?"
    jd "I don't think I'll ever know the difference even if I had my memories...{w=0.5} Thanks{w=0.3}, uh{w=0.3}, what's your name again?"

    u1 "The name's{nw}"
    v "{fast}The name's{fast} Vax."

    jd "Thanks Vax.{w=0.4} You can call me Jay."

    u "Well then{w=0.3}, looks like you're officially one of us{w=0.3}, even if it's just temporary.{p}Name's{nw}"
    b "{fast}Well then{w=0.3}, looks like you're officially one of us{w=0.3}, even if it's just temporary.{p}Name's{fast} Brad, by the way."



    v "And that mess of a teacher over there is Lain."
    jd "It's a privilege to meet you all.{w=0.3} really.{w=0.5} and uh...{w=0.5} Sorry for all the trouble I caused{w=0.3}, and I'm glad to be in your care."
    b "You exaggerate."
    b "And hey{w=0.1}, no reason to get worked up.{w=0.3} We scored ourselves a free pack mule, after all."
    jd "Free?{w=0.3} I'd say it's fair—{w=0.3}Lain's gonna be teachin' me magic."
    v "Lain's a drunk half the time{w=0.3}, but he's a damn good instructor when he's sober.{w=0.5} He's good at what he do."
    v "And speakin' of...{w=0.3} Brad{w=0.2}, get him up.{w=0.2} He's passed out again."
    v "Anyway, like I was sayin' {w=0.3}—when he's not three sheets to the wind{w=0.3}, he's the best around.{w=0.5} You'll be spell-slingin' by the end of the week."
    jd "Then I'm really grateful.{w=0.3} Most folks around here have just given me nasty looks—{w=0.3}first time I've felt...{w=0.3} so welcomed."
    la "{sc=2}{i}BAH-{w=0.3}HA{w=0.2}HA{w=0.2}HA{w=0.2}HAHAHAHA!{/i}{/sc} Don't mind those 3rd rate parties, kiddo." with vpunch
    b "Hey, ease down on the booze Lain!{w=0.3} {sc=1.5}You're half passed out already!{/sc}"

    scene black with dissolve

    "And so{w=0.3}, I became a temporary member of their 3-man party."
    "Lain is apparently a prodigy in magic.{w=0.3} He's the top of all{w=0.2}, that no one is sure whether he can be categorized in the four already mentioned magic classes:{p}Mage, Wizard, Warlock, Sorcerer."
    "Brad is their knight and centerlane support.{w=0.4} He's not a deadweight-{w=0.3} In fact, all of them are great at what they do."
    "Brad is a knight that can tank oncomming attacks{w=0.3}, but he also can provide support by healing or buffing."
    "He's the healer of his party{w=0.3}, yet he's also the most ripped among his peers.{w=0.5} Usually{w=0.2}, he's the one who ends up treating his own wounds more than anyone else."
    "Really unconventional."
    "Then there's Vax.{w=0.4} A former mercenary and assassin.{w=0.4} Because of his work{w=0.4}, he was sent to many places before and witnessed some of the most bizarre and ironic stories in the world."
    "And because of that{w=0.3}, he has a lot of stories to talk about.{p}Usually{w=0.2}, you'd expect an assassin to be deep and broody.{w=0.4} But Vax is different."

    scene taveling with fade

    v "...And then, there we were{w=0.3}, deep in this cave{w=0.3}, only to stumble upon a necromancer!{w=0.5} The second he came into view,{w=0.2} we all fell into battle stance."
    v "But here's the kicker—{w=0.3}{i}he wasn't even evil!{/i}{p}Can you believe that?{w=0.4} A good necromancer."
    b "My sword was a hair's breadth from cutting that necromancer down.{w=0.5} If he hadn't surrendered right then{w=0.3}, I would've split him in two."
    la "{sc=2}{i}BAH-{w=0.3}HA{w=0.2}HA{w=0.2}HA!{/i}{/sc}{w=1} I remember him saying he only got into necromancy to bring his pet cat back to life!" with vpunch
    b "It really goes to show that not all are absolute evil.{w=0.4} Even among their side of the world."
    v "Ugh,{w=0.3} don't even get me started.{w=0.5} It's not just about being \"evil.\""
    v "Kid{w=0.2}, you haven't seen the half of it.{p}I once invaded an Orc hideout.{w=0.4} And what do you think I saw?{w=0.4} Orcs being highly intelligent and engaging in orc chess and deep philosophical debates."
    b "{sc=1}{i}HAHAHAHAHA!{/i}{/sc}{w=0.4} I cannot-{w=0.4} {i}for the life of me!-{/i}{w=0.4} forget your face when you got back to us that time!"
    v "That's not the {i}only{/i}{w=0.1} stories I have."
    v "Back in Sierra Kingdom, I was paired with these second-rate assassins.{w=0.4} One of them had this whole 'deep and broody' persona going on."
    v "It really threw off our team communication at first{w=0.4}, but we somehow worked through it."
    v "The deep and broody member never spoke a word until it was time to leave the team.{w=0.7} By then, two years has already passed."
    v "Finally{w=0.3}, when it was time to disband{w=0.3}, we all worked up the courage to ask him why he'd been so quiet.{w=0.5} We thought he had this tragic backstory or something."
    v "And the whole time-{w=0.4} the whole fucking time-{w=0.4} No one thought to ask if he was mute at all."
    v "{sc=2}{i}Because he fucking was mute!{/i}{/sc}" with vpunch and hpunch
    v "No one realized and thought it's just a part of his moody persona."
    v "Not until he had to spell it out for us. {w=0.5}{sc=3}{i}LITERALLY!{/i}{/sc}{w=0.5}"
    v "He spent the whole story making exasperated faces and gestures.{p}Expressions that were priceless—years of exasperated faces and gestures we'd missed."
    v "{sc=1}{i}For two years{w=0.3}, he was just rolling his eyes and waving his hands.{/i}{/sc}{w=0.5}{p}{sc=1}{i}but we all just nodded along{w=0.3}, like he was \"deep\" or something.{/i}{/sc}"
    la "{sc=1}{i}HAHAHAHAHA!{/i}{/sc}{w=0.4}" with vpunch
    b "Kid, you might think we're reckless{w=0.3}, but it's thanks to this guy that things spiral into chaos half the time."
    b "If we don't iron out our assumptions{w=0.3}, moments like that happen."
    b "But hey{w=0.3}, I can't even blame vax there.{w=0.5} I get it.{w=0.3} Even I would've pegged a silent assassin as the 'deep and broody' type."
    b "Or at least that's how I thought of Vax that first time we met."
    v "Hey!{w=0.5} I don't even look the part!"


    scene black with dissolve

    "They all had fascinating stories to tell{w=0.4}, each one of them."
    "And I genuinely enjoyed every bit of them as I laughed along their experiences."
    "It hasn't been three days{w=0.4}, but they weren't hard on me.{w=0.5} I was enjoying life here for the first time."
    "Though seeing them bond along so well{w=0.4}, I kinda miss my friends back in the real world."
    "What would've happened if they were sent here along with me?{w=0.4} Would it have been any less exhausting?{w=0.3} Less excruciating?"
    "In any case{w=0.4}, I envy them at this moment."

    scene trouble with fade

    "Having seen the depictions of this fictional reality several times on the internet{w=0.5}, I half suspected most of their stories were fake."
    "But I couldn't be sure{w=0.3}, not when back in my world{w=0.2}, they classified one of the most dangerous monsters here as no threat: Slimes."
    "However{w=0.3}, It wasn't long until I was proven wrong as I started living those bizarre stories for myself in the span of a day I've been with them."
    "Each folks in this town seem to hold their own mysteries{w=0.3}, that sometimes I forget I'm literally in another world."
    
    scene tavern with fade
    
    "When we passed by a tavern{w=0.3}, it was a struggle holding Lain off to another drinking spree."
    "But we couldn't afford not having any rest now, as the next destination is infested by shitloads of monsters."
    "And I just happen to I catch one of the folks' mysteries in the tavern of all places.{p}Apparently{w=0.3}, this tavern dates back two centuries ago, and was ran by a former adventurer."
    "From what I heard among the other loud-mouthed adventurers{w=0.5}, the first owner of this tavern was quite the eccentric guy."
    "A strong{w=0.2}, well-known adventurer who used to go dungeon hopping with weak parties{w=0.3}, helping them loot the place for their own betterment."
    "Though as mentioned by several parties who went with this eccentric adventurer{w=0.5}, the guy never took any gold or valuable things."
    "He only took items that were random and eccentric{w=0.3}, a fitting reward of living up to his name."
    "They didn't know what his agendas were{w=0.3}, until his hair was gray and his retirement came. {w=0.5}The now former adventurer opened a small tavern, that many of the parties he helped came by."
    "And each of the items he took in every dungeons{w=0.4}, items that were nearly to no value{w=0.2}, items that were uncanny{w=0.3}, was on full display in the tavern."
    "They were said to be his trophies{w=0.3}, but they were probably more than that to the former adventurer.{p}They were invaluable items that served as the nostalgia of their days of adventuring."
    
    "One night, when a couple of young hooligans thought of a good idea to steal his trophies{w=0.5}, broke into the tavern."
    "It would have been a normal case of robbery{w=0.4}, but the adventurer's wife witnessed the crime being done, and protected the tavern from plunderers."
    "Unfortunately{w=0.2}, she was old, even if she was a former adventurer too.{w=0.4} The wife was struck, and the hooligans prepared their bloodied bats{w=0.4}, queuing up to rough up an old lady."
    "But that's when the trophies started moving,{w=0.4} started schreeching.{p}They convulsed{w=0.2}, they deformed.{w=0.3}"
    "Until they finally revealed the true form they were hiding for years.{p}They were mimics."
    "No{w=0.1}, they weren't ordinary mimics.{w=0.3} They were big{w=0.2}, sinsiter{w=0.2}, and very angry mimics.{p}They easily towered over the hoodlums{w=0.3}, aggressively moving forward."
    "It would've been a normal case of robbery{w=0.3}, but the victims got the last laughs instead."
    "The hoodlums weren't adventurers{w=0.3}, they were simple men who did crimes to satiate their cravings."
    "So they weren't up to the task{w=0.4}, and they failed to survive the horde of mimics they brought upon themselves."
    "Among the three hooligans{w=0.3}, there was only one guy who lived to tell the tale{w=0.3}, the one who spread the story.{w=0.4} The hooligan that was supposed to be in the scene{w=0.4}, but came too late as he witnessed the horrifying deaths of his peers."
    "Though even after witnessing the blood-fest of mimicries{w=0.4}, he came back the day later."
    "Obstensively{w=0.2}, the adventurers weren't aware of their possessions being mimicries."
    "But the adventurers who took them in had taken good care of their items for as long as they known.{p}And it just so happen that those mimicries somehow gained a sense of humanity."
    "Witnessing the outside world{w=0.3}, the people whom bonded by simple meals and drinks{w=0.3}, and being taken care of with the highest care."
    "The languages that were probably gibberish to them{w=0.3}, they grew to understand and heard stories beyond them."
    "If you think about it{w=0.3}, it was really no wonder how a simple mimicry gained humanity."

    scene forest with fade
    la "Remember Jay{w=0.3}, you're a sorcerer."
    la "Magic runs through your veins, magic is your life."
    la "Focus.{w=0.3} Feel the source wanting to let out."

    "...."
    "..."
    ".."
    "."  


    if persistent.game_played == True:
        jump stubborn
    else:
        pass

label stubborn:
    if persistent.game_played == False:
        jd "Hey{w=0.3}, trying to find the latest script?{p}Well, get lost already.{w=0.4} There ain't no new script."
        jd "The one writing this file is too lazy. Lol. Come back a day later."
        $ persistent.game_played= True
        jump end

    else:
        jd "Didn't I say get lost already?{w=0.3}"
        jd "Like I told you{w=0.3}, there's no new script until the next or the following day."
        jd "Stubborn bitch.{w=0.3}"
        jd "Just get lost."  
        jump end
    return

label end:
    jd "Bye!{w=0.4}"
    "Delete Persistent Data?"
    
    menu:
        "Yes":
            $ persistent.game_played = False
        "No":
            pass
    return