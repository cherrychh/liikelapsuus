# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Valerie", color="74b849")
define a = Character("Anthony",color="322240")
define s = Character("System",color="2e3033")

$ valeriePoints = 0
$ anthonyPoints = 0

# The game starts here.

label start:

    # hotelli huone tausta 
    
    "Valerie ja Anthony ovat hyviä ystäviä, jotka ovat vuosien eron jälkeen vihdoin päässeet jälleen viettämään aikaa yhdessä. Ystyävykset ovat löytäneet mukavalta näyttävän hotellin, jossa he päättivät yöpyä."
    "Kaikki oli mennyt aivan mutkattomasti, mutta aamulla jotain outoa kuitenkin tapahtuu"

    # show valerie

    v "Hei Ant! Mennäänkö nyt aamupalalle? Näin eilen tuolla tien toisella puolella kivan kahvilan. Siellä näytti olevan kroisantteja, pullia ja kasin muotoisia rinkeleitä."

    # show anthony
    a "Mennään vaan."

    "Anthony kävelee oven luokse ja vääntää kahvaa, mutta ovi näyttää olevan lukossa."

    a "Ompa omituista..."
    a "Tämä ovi vaikuttaa"
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
