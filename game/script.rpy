define v = Character("Valerie", color="74b849")
define a = Character("Anthony",color="322240")
define s = Character("Wave", color="2e3033")
define text = Character("Tehtävä:", kind=nvl)

image laavahuone = "Laavahuone.png"
image hotelRoom = "Hotellihuone.png"

label start:
    $ valeriePoints = 0
    $ anthonyPoints = 0


    # Joku tausta + söpö robootti :D

    s "Hei! Tervettuloa pelaamaan meidän HUIKEAA peliä INSERT TOSI SIISTI PELI NIMI!"
    s "Pääsette seuraamaan kahden ihastuttavan henkilön kokemuksia ja tekemään hulvattoman hauskoja tehtäviä! :D"
    s "Valitkaa teistä yksi pelin tuomariksi ja jakakaa loput kahteen ryhmään (Ryhmä 1 ja Ryhmä 2)."
    s "{cps=2}...{/cps}"
    s "OKEI!! Seuraavaksi ensimmäinen tiimi voisi astua olla kuulolla."
    s "Te olette Valerien tiimissä!"
    s "Sitten tiimi kaksi..."
    s "Te olette rakkaan Anthonyn tiimissä!"
    s "Kaikki valmiina?"

    menu:
        "JOO!":
            s "WOO! Niin sitä pitääkin, rakkaat pelaajat!"
            s "Aloitetaan!"
            pause 1.0
        "Eip.":
            s ""
            pause 1.0


label lavaroom1st:

    show hotelRoom

    pause 2.0
    
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

    "Valerie harppaa nopein askelin ovelle Anthony perässään. Hän tarttuu oven kahvaan ja vääntää sen auki."
    "Samalla huone täyttyy sietämättömällä kuumuudella."
    # bg lava room
    "Kaverusten katseet tarttuvat heti tuntemattomaan huoneeseen."

    v "WOAH!"
    a "Mitä ihmettä!?"
    v "Onko tuo oikeaa laavaa?"

    "Yhtäkkiä huoneen seinistä kuuluu roboottimaista puhetta."
    s "Hei rakkaat ystävät! Tervetuloa laavahuoneeseen!"
    "Valerie ja Anthony katsovat toisiaan hämmästyneenä."
    s "Teidän tehtävänänne on päästä huoneen toiselle puolelle putoamatta laavaan. Onnea!"
    s "..."
    v "Ömm... Haluatko sinä mennä ensin?"
    a "..."
    a "Okei sitten."

    "Anthony alkaa liikkuu varovaisesti huonekalujen kautta kohti huoneen toista puolta."
    "Nähtyään Anthonyn suorituksen, Valerie seuraa innokkaana perässä."
    "Valerie yrittää hypätä sängylle, muttei osu siihen."

    v "{cps=2}ÄÄH!!!{/cps}"

    # Musta screen/ välähdys

    jump lavaroom2nd


label lavaroom2nd:

    show hotelRoom
    pause 3.0

    v "Hmm. Näin tosi outoa unta."
    #näytä val
    a "Niin minäkin..."
    #näytä ant
    v "Siinä me kävelimme tyhjästä ilmestyneestä ovesta huoneeseen, jonka lattia oli täysin laavan peitossa."
    a "Oikeastiko? Näin itsekkin ihan samanlaista unta."
    v "Katso! Tuossa on se sama ovi mistä menimme unessa."
    a "Niinpä onkin...Outoa"
    v "Miten tämä kaikki on mahdollista?"
    "Valerie kokeilee uudestaan hotellihuoneen ovea ja toteaa sen olevan yhä lukossa."


    v "Meillä ei varmaan ole muita vaihtoehtoja."
    "Valerie avaa nurkassa olevan mysteeri oven uudestaan."
    # näytä laavahuone ja piilota ahomot
    show laavahuone
    v "Täällä tosiaan on se sama laavahuone kuin aikaisemmin."
    s "Hei rakkaat ystävät! Tervetuloa laavahuoneeseen!"
    s "Teidän tehtävänänne on päästä huoneen toiselle puolelle putoamatta laavaan. Onnea!"

    text "Tervetuloa huoneeseen, jonka lattia on polttavan kuumaa laavaa. 
    Tavoitteenanne on pysyä mahdollisimman kauan koskettamatta lattiaa. 
    Tämä ei ole kuitenkaan niin helppoa, kuin mitä te luulette, sillä paikoillaan ette saa olla. 
    Saatte olla yhdessä paikassa vain INSERT RAJOITE, kuunnelkaa tuomaria, sillä hän antaa merkin siitä, milloin paikka täytyy vaihtaa. 
    Se, joka pysyy pisimpään pelissä mukana, voittaa kyseisen pelin."

    menu:
        "Kumpi tiimeistä voitti?"

        "Valerie-tiimi":
            $ valeriePoints +=1
        "Anthony-tiimi":
            $ anthonyPoints +=1

