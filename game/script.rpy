# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Valerie", color="74b849")
define c = Character("Anthony",color="322240")
define a = Character("System",color="2e3033")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    "a"


    # This ends the game.

    return


label lavaroom2nd:

    v "Hmm. Näin tosi outoa unta"
    a "Niin minäkin"
    v "Siinä me heräsimme tässä samassa huoneessa ja kävelimme ovesta ja oven takana oli huone jonka lattia oli täysin laaavan peitossa"
    a "Mitä!? Näin itsekkin ihan samanlaista unta"
    a "Katso! Tuossahan on se sama ovi mistä menimme unessa."
    a "Niin onkin…Outoa…"
    v "Miksi olisimme nähneet samaa unta?"
    a "En tiedä. Pitäsikö meidän avata tuo ovi"

