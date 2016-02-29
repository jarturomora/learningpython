from sys import exit # To allow exit the infinite loop
from random import randint # To generate random integer numbers

class Scene(object):

    def enter(self):
        """This method describes each scene"""
        print """
        This scene is not yet described,
        implement enter() on the subclass.
        """
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        """The main method to start the game"""
        current_scene = self.scene_map.opening_scene()

        # The game will run until the player is death, wins, or CTRL-D is hit.
        while True:
            print """
                ----------------------------------
                | Gothons from Planet Percal #25 |
                ----------------------------------
                 The most awesome text game coded
                          in python 2.7
            """
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    death_messages = [
        "You died, you planet is doomed due to your clumsiness.",
        "WTF! you pissed of!... sorry you're dead!",
        "You are simply a luser, you're dead.",
        "I have a dog that's better than you at this."
    ]

    def enter(self):
        print Death.death_messages[randint(0, len(self.death_messages)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print """
            The Gothons of planet Percal #25 have invaded you ship and killed
            your entiere crew. You are the last survivor and your last mission
            is to get the neutron destruct bomb from the Weapons Armory,
            put it on the bridge, and blow the ship after getting into an
            escape pod.

            You'are running down the central corridor to the Weapons Armory
            when a Gothon jumps out, red scaly skin, dark grimy teeth, and
            evil t-shirt of Justin Bieber. He's blocking the door to the Armory
            and about to pull a weapon to kill you.

            What will you do?
        """

        action = raw_input("> ")

        if action == "shoot!":
            print """
                You didn't count that the Justin Bieber's t-shirt is a powerful
                armor agains every kind of weapon in the universe, so your
                lasser shoot just bounced off the Bieber's face and killed you.
            """
            return "death"
        elif action == "dodge!":
            print """
                Ha ha ha! you are so weak in contrast with the Gothon,
                your punch was like a feader to him, you are doomed.
                The Gothon hit you and smash your face!
            """
            return "death"
        elif action == "tell a joke":
            print """
                You hit on the nail, the Gothon has a bad sense of humor
                that they even laugh from your bad jokes, the Gothon starts
                to laugh until he is dead of happiness.
            """
            return "laser_weapon_armory"
        else:
            print "This is not an option... you have to start over again."
            return "central_corridor"

class LaserWeaponArmory(Scene):

    def enter(self):
        print """
            You finally are in front of the neutron bomb, but wait!
            there is a keypad with a code you have to enter and you don't
            remember it, it's a three numbers code, you have three chances
            to guess the code or you are lost!
        """
        code = "%d%d%d" % (randint(1, 3), randint(1, 3), randint(1, 3))
        print "\n Here's a clue: *%c*" % code[1]
        guesses = 1
        # print "Code: " + code
        guess = raw_input("[Enter Code]> ")

        while guesses < 3 and guess != code:
            print "\aWrong Code, you have %d more attemps." % (3 - guesses)
            guesses += 1
            guess = raw_input("[Enter Code]> ")

        if guess == code:
            print """
                Yeah! the container is open and now you can take the netron bomb
                hurry up to the bridge and save your life and the galaxy from
                the Gothons."
            """
            return "the_bridge"
        else:
            print """
                You failed to open the container after %d attemps. Sorry, the
                Gothons find you and eat you.
            """ % guesses
            return "death"

class TheBridge(Scene):

    def enter(self):
        print """
            Finally you are at the bridge, the neutron bomb is very delicate,
            there are 100 Gothons at the bridge, you only have one change to
            save your life an the galaxy.

            What will you do?
        """
        action = raw_input("> ")

        if action == "slowly place the bomb":
            print """
                With a ninja movement you place the bomb on the floor and
                jump to the espace pod, you are almost save and closer to
                become the hero of the galaxy.
            """
            return "escape_pod"
        else:
            return "death"

class EspacePod(Scene):

    def enter(self):
        print """
            Finally you are at the escape pod, but only one pod is ready to
            launch and save you life, hurry up! you only have 10 seconds to
            pick one of the five pods.
        """
        good_pod = randint(1,5)
        # print "Pod: " + str(good_pod)
        guess = raw_input("[Pod Number]> ")

        if int(guess) == good_pod:
            print """
                Wow! the pod %r was the good one, now you are save, the Gothons
                are dead and you just save the entire galaxy, you are going to
                become a hero... hurray!!!
            """ % good_pod
            exit (1)
        else:
            return "death"

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EspacePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# Game play
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()