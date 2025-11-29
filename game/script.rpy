# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Valerie", color="74b849")
define a = Character("Anthony",color="322240")
define s = Character("System",color="2e3033")

# The game starts here.

label start:
    $ valeriePoints = 0
    $ anthonyPoints = 0

    s "Hei! Tervettuloa pelaamaan meidän HUIKEAA peliä INSERT TOSI SIISTI PELI NIMI!"
    s "Pääsette seuraamaan kahden ihastuttavan henkilön kokemuksia ja tekemään hulvattoman hauskoja tehtäviä! :D"
    s "Valitkaa teistä yksi pelin tuomariksi ja jakakaa loput kahteen ryhmään (Ryhmä 1 ja Ryhmä 2)."
    s "{cps=1}...{/cps}"


label lavaroom1st:

    # hotelli huone tausta 
    
    "Valerie ja Anthony ovat hyviä ystäviä, jotka ovat vuosien eron jälkeen vihdoin päässeet jälleen viettämään aikaa yhdessä. Ystyävykset ovat löytäneet mukavalta näyttävän hotellin, jossa he päättivät yöpyä."
    "Kaikki oli mennyt aivan mutkattomasti, mutta aamulla jotain outoa kuitenkin tapahtuu"

    # show valerie iloinen

    v "Hei Ant! Mennäänkö nyt aamupalalle? Näin eilen tuolla tien toisella puolella kivan kahvilan. Siellä näytti olevan kroisantteja, pullia ja kasin muotoisia rinkeleitä."

    # show anthony neutraali
    a "Mennään vaan."

    "Anthony kävelee oven luokse ja vääntää kahvaa, mutta ovi näyttää olevan lukossa."

    # show anthony hämmentynyt
    a "Ompa omituista..."
    v "Mitä?"
    a "Tämä ovi vaikuttaa olevan lukossa ulkoota päin."
    
    # show Valerie hämmentynyt
    v "Hääh? Miten tuo on edes mahdollista?"

    "Valerie kävelee Anthonyn luokse ja kokeilee kahvaa useamman kerran."


    v "Miten tämä voi olla lukossa?"
    
    # Show anthony neutraal
    a "..."
    v "Miten meidän pitäisi päästä täältä pois?"

    # Show valerie keskittynyt

    "Valerie kääntyy ympäri ja silmäilee heidän huonettaan."
    v "Hei Ant, oliko tuo oli aina tuossa?"

    "Valerie osoittaa nurkassa olevaa ovea."
    "Anthony on hetken hiljaa."

    a "Ei tainut olla."
    v "Outoa. Ehkä me pääsemme siitä ulos!"

    "Valerie kävelee oven luoksen Anthony perässään"



    jump lavaroom2nd
    return


label lavaroom2nd:
    $ global valeriePoints
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
    "Valerie kokeilee uudestaan hotellihuoneen ovea ja toteaa sen olevan yhä lukossa."
    v "Miksipäs ei!"
    "Valerie avaa nurkassa olevan mysteeri oven."
    # näytä laavahuone ja piilota ahomot
    v "Täällä on se sama laavahuone kuin aikaisemmin."
    s "Tervetuloa laavahuoneeseen!"
    s "Teidän tehtävänänne on päästä huoneen toiselle puolelle putoamatta laavaan."
    "Tervetuloa huoneeseen, jonka lattia on polttavan kuumaa laavaa."
    "Tavoitteenanne on pysyä mahdollisimman kauan koskettamatta lattiaa."
    "Tämä ei ole kuitenkaan niin helppoa, kuin mitä te luulette, sillä paikoillaan ette saa olla."
    "Saatte olla yhdessä paikassa vain INSERT RAJOITE, kuunnelkaa tuomaria, sillä hän antaa merkin siitä, milloin paikka täytyy vaihtaa."
    "Se, joka pysyy pisimpään pelissä mukana, voittaa kyseisen pelin."

    menu:
        "Kumpi tiimeistä voitti?"

        "Valerie-tiimi":
            $ valeriePoints +=1
        "Anthony-tiimi":
            $ anthonyPoints +=1
