from items import *
#   Basic Intro, Please improve this shit:
#   "One man. One desire. The goal to create a device protect himself and those around him, the only way he knew how.
#   Python."The words echo in your (Kirill Sodorov, Expert Programmer, Overall Nice Guy) head. Years of planning,
#   programming, bug fixing, getting angry, and progressive montages led to this moment. Over a cup of lukewarm coffee,
#   you finish the last function:- "def killcode". You lean back and revel in your own glory, ready to get a good
#   night's sleep to prepare for the big presentation in the University tomorrow. Researchers from round the country are
#   coming to witness your brainchild. This could be your big break. Let's hope everything goes to plan. You didn't
#   forget to logoff the lecture hall computer did you?


#   Needs to be finished, not sure about the final rooms tbh. Try out some stuff if you can please xxx
room_floor0 = {
    "name": "Bottom Floor",

    "description":
    """The Central Building bottom floor is suspiciously quiet. There is no smell of breakfast from the cafeteria.
    The normal buzz of student life is nowhere to be seen. The elevator door appears to be out of whack. At least
    nobody is around to pass on their flu on your big day.""",

    "exits": {"right": "Reception", "up": "Floor1"},

    "items": []
}

room_reception = {
    "name": "Reception",

    "description":
    """You walk over to the reception. There is nobody here, and there appears to be nobody around. Everything is left
    on as if someone had to leave urgently. You notice a phone with a blinking notification indicator and a strange item.""",

    "exits":  {"left": "Floor0", "up": "Floor1"},

    "items": [item_phone, item_bodypillow]
}

room_floor1 = {
    "name": "First Floor",

    "description":
    """The First Floor is as desolate as the ground floor. Some things appear to be damaged as if there has been some
     kind of apocalypse but that would be ridiculous. There is a totally standard incapacitated body to the left, and
     the stairs to the right have been barricaded(?). If only you hadn't left your toolkit at home.""",

    "exits": {"down": "Floor0", "left": "body", "up": "Floor2Opening"},

    "items": []
}

room_body = {
    "name": "Incapacitated Body",

    "description":
    """You walk over to the lifeless body. You notice a pulse but they have clearly been struck to the head, or gotten
    overly drunk for a Monday morning. As you are the protagonist of a text-based adventure, your first instinct is not
    to help but to scavenge for any loot he might have. He appears to blessed with a chainsaw. That's convenient.""",

    "exits": {"right": "Floor1", "f": "pay respects"},

    "items": [item_saw]
}

room_f = {
    "name": "Room of Respect Paying",

    "description":
    """Achievement Unlocked: Self-Respect.""",

    "exits": {"and kiss forehead": "body"},

    "items": [item_humility]
}

room_f2o = {
    "name": "Second Floor",

    "description":
    """After effortlessly clearing the barricade thanks to your mighty chainsaw, you climb the stairs to the second floor.
    None of the lights are on, and in the near distance you notice a shadowy figure lumbering about. A wiseman would ready
    the chainsaw, but a real man goes in with his fists and his wit.""",

    "exits": {"forward": "Fight"},

    "items": []
}

room_fight = {
    "name": "Shadowy Figure",

    "description":
    """You walk towards the figure and as you get closer, you notice the silhouette is Jing Wu. She is lurching about like
     a zombie from World War Z, or rather a good film like 28 Days Later. As you step towards her, she notices your presence
     and turns around. Under her breath she mutters "Wake Me Up Inside (Can't Wake up)" then starts to run towards you
     aggressively. She appears noticeably triggered, and you deal with it in the only way a man can, with patriarchy
     (fists).""",

    "exits": {"and falcon punch her": "Floor2", "and one bang her": "Floor2", "rko": "Floor2",
              "and hadouken her": "Floor2", "and quickscope her": "Floor2", "and backhand her": "Floor2", "and worldstar her": "Floor2"},

    "items": []
}

room_floor2 = {
    "name": "Second Floor",

    "description":
    """You have successfully showed her what for, whether that was required or not is another question. Floor 2 is in an even worse state
    than Floor 1. Tables have been knocked over, windows have been smashed, jimmies have been rustled. The only other human here is Jing Wu,
    and your only exit is to keep going up as you don't want to face your previous actions.""",

    "exits": {"left": "Jing Wu", "up": "Floor3"},

    "items": []
}

room_jing = {
    "name": "Jing Wu",

    "description":
    """What you do have is a very particular set of skills. Skills you acquired over a very long career. Skills that make you a nightmare
    for people like Jing. Luckily, your experience with said skills allowed you to stun her without causing any permanent damage. Well done.
    In her pocket is a note that appears to have frantically scrawled upon.""",

    "exits": {"right": "Floor2"},

    "items": [item_note]
}

room_floor3 = {
    "name": "Third Floor",

    "description":
    """The third floor looks far more battered than the previous floors combined. It is evident at this point that
    something has gone very, very wrong. It couldn't be you.... could it? No, absolutely not, what a foolish assumption.
    The door to the lecture hall is splattered with blood. Are they that excited?""",

    "exits": {"down": "Floor2", "left": "Lecture Hall"},

    "items": [item_note]
}

room_lecture = {
    "name": "Lecture Hall",

    "description":
    """Oh dear. You recognise now that perhaps you might some involvement here. """,

    "exits": {"down": "Floor2", "left": "Lecture Hall"},

    "items": [item_note]
}


rooms = {
    "Floor0": room_floor0,
    "Reception": room_reception,
    "Floor1": room_floor1,
    "body": room_body,
    "Floor2Opening": room_f2o,
    "Fight": room_fight,
    "Floor2": room_floor2,
    "Jing Wu": room_jing,
    "pay respects": room_f,
    "Floor3": room_floor3,
    "Lecture Hall": room_lecture
}
