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

    #näytä hotellihuone
    v "Hmm. Näin tosi outoa unta."
    #näytä val
    a "Niin minäkin"
    #näytä ant
    v "Siinä me kävelimme tyhjästä ilmestyneestä ovesta huoneeseen, jonka lattia oli täysin laavan peitossa."
    a "Mitä!? Näin itsekkin ihan samanlaista unta."
    v "Katso! Tuossahan on se sama ovi mistä menimme unessa."
    a "Niinpä onkin...Outoa"
    v "Mitä?! Miten tämä kaikki on mahdollista?"
    "Valerie kokeilee uudestaa ovea ja toteaa sen olevan yhä lukossa."
    v "Miksipäs ei!"
    "Valerie avaa nurkassa olevan oven."
    # näytä laavahuone ja piilota ahomot
    v "Täällä on se sama laavahuone kuin aikaisemmin."
    s "Tervetuloa laavahuoneeseen!"
    s "Teidän tehtävänänne on päästä huoneen toiselle puolelle putoamatta laavaan."
