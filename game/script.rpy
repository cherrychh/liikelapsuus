define v = Character("Valerie", color="cadde8")
define a = Character("Anthony",color="e8cae6")
define s = Character("Wave (systeemi)", color="f2f2f2")
define text = Character("Tehtävä:", kind=nvl)

image lavaroom = "Laavahuone.png"
image hotelRoom = "Hotellihuone.png"
image Lavadark:
  "Laavahuone.png"
  matrixcolor OpacityMatrix(0.5)
image whiteroom = "whiteroom.png"
image logo = "logo.png"

label splashscreen:
    scene black
    with Pause(1)

    show logo at truecenter with dissolve
    with Pause(2)

    hide logo with dissolve
    with Pause(0.5)

    show text "Tehty liikettä peleistä jameissa 2025" with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(0.5)

    return

label start:
    $ valeriePoints = 0
    $ anthonyPoints = 0


    # Joku tausta + söpö robootti :D

    s "Hei! Tervettuloa pelaamaan meidän HUIKEAA peliä 'ROOM'!"
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
            s "{cps=1}...{/cps}"
            s "ALOITETAAN!!!"
            pause 1.0


label lavaroom1st:

    scene hotelRoom

    pause 2.0
    
    "Valerie ja Anthony ovat hyviä ystäviä, jotka ovat vuosien eron jälkeen vihdoin päässeet jälleen viettämään aikaa yhdessä. Ystyävykset ovat löytäneet mukavalta näyttävän hotellin, jossa he päättivät yöpyä."
    "Kaikki oli mennyt aivan mutkattomasti, mutta aamulla jotain outoa kuitenkin tapahtuu"
    # show valerie iloinen
    show valerie neutral at left
    v "Hei Ant! Mennäänkö nyt aamupalalle? Näin eilen tuolla tien toisella puolella kivan kahvilan. Siellä näytti olevan kroisantteja, pullia ja kasin muotoisia rinkeleitä."

    # show anthony neutraali
    show anthony neutral at right
    a "Mennään vaan."

    "Anthony kävelee oven luokse ja vääntää kahvaa, mutta ovi näyttää olevan lukossa."

    # show anthony hämmentynyt
    show anthony neutral at right
    a "Ompa omituista..."
    v "Mitä?"
    a "Tämä ovi vaikuttaa olevan lukossa ulkoota päin."
    
    # show Valerie hämmentynyt
    show valerie neutral at left
    v "Hääh? Miten tuo on edes mahdollista?"

    "Valerie kävelee Anthonyn luokse ja kokeilee kahvaa useamman kerran."


    v "Miten tämä voi olla lukossa?"
    
    # Show anthony neutraal
    show anthony neutral at right
    a "..."
    v "Miten meidän pitäisi päästä täältä pois?"

    # Show valerie keskittynyt
    show valerie neutral at left
    "Valerie kääntyy ympäri ja silmäilee heidän huonettaan."
    v "Hei Ant, oliko tuo oli aina tuossa?"

    "Valerie osoittaa nurkassa olevaa ovea."
    "Anthony on hetken hiljaa."

    a "Ei tainut olla."
    v "Outoa. Ehkä me pääsemme siitä ulos!"

    "Valerie harppaa nopein askelin ovelle Anthony perässään. Hän tarttuu oven kahvaan ja vääntää sen auki."
    "Samalla huone täyttyy sietämättömällä kuumuudella."
    scene lavaroom
    "Kaverusten katseet tarttuvat heti tuntemattomaan huoneeseen."

    show valerie neutral at left
    v "WOAH!"
    show anthony neutral at right
    a "Mitä ihmettä!?"
    v "Onko tuo oikeaa laavaa?"

    "Yhtäkkiä huoneen seinistä kuuluu roboottimaista puhetta."
    s "Hei rakkaat ystävät! Minä ole Wave, erittäin älykäs ja hurmaava robootti, joka tarjoaa teille tämän mainion pelikokemuksen! Tervetuloa laavahuoneeseen!"
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
    scene black
    pause 1.0

    jump lavaroom2nd











label lavaroom2nd:

    scene hotelRoom
    pause 3.0
    show valerie neutral at left
    v "Hmm. Näin tosi outoa unta."
    show anthony neutral at right
    a "Niin minäkin..."
    v "Siinä me kävelimme tyhjästä ilmestyneestä ovesta huoneeseen, jonka lattia oli täysin laavan peitossa."
    a "Oikeastiko? Näin itsekkin ihan samanlaista unta."
    v "Katso! Tuossa on se sama ovi mistä menimme unessa."
    a "Niinpä onkin...Outoa"
    v "Miten tämä kaikki on mahdollista?"
    "Valerie kokeilee uudestaan hotellihuoneen ovea ja toteaa sen olevan yhä lukossa."


    v "Meillä ei varmaan ole muita vaihtoehtoja."
    "Valerie avaa nurkassa olevan mysteeri oven uudestaan."
    # näytä laavahuone ja piilota ahomot
    #hide hotelRoom
    scene lavaroom
    show valerie neutral at left
    v "Täällä tosiaan on se sama laavahuone kuin aikaisemmin."
    s "Hei rakkaat ystävät! Tervetuloa laavahuoneeseen! Minä ole Wave, erittäin älykäs ja hurmaava robootti, joka tarjoaa teille tämän mainion pelikokemuksen!"
    
    s "Teidän tehtävänänne on päästä huoneen toiselle puolelle putoamatta laavaan. Onnea!"
    scene black
    show Lavadark
    show text "Tervetuloa huoneeseen, jonka lattia on polttavan kuumaa laavaa. \nTavoitteenanne on pysyä mahdollisimman kauan koskettamatta lattiaa.\nTämä ei ole kuitenkaan niin helppoa, kuin mitä te luulette, sillä paikoillaan ette saa olla.\nSaatte olla yhdessä paikassa vain INSERT RAJOITE, kuunnelkaa tuomaria, sillä hän antaa merkin siitä, milloin paikka täytyy vaihtaa.\nSe, joka pysyy pisimpään pelissä mukana, voittaa kyseisen pelin." at truecenter
    ""
    hide text
    scene lavaroom
    menu:
        "Kumpi tiimeistä voitti?":

            "Valerie-tiimi"
                $ valeriePoints +=1
                "Valerie tutkii varovasti huonetta ja löytää molemmille nopean ja turvallisen reitin heille."
                show valerie neutral at left
                v "Fiksu reitti, eikö?"
                show anthony neutral at right
                a "Yllättävän."
            "Anthony-tiimi"
                $ anthonyPoints +=1
                "Valerie kompastuu lamppuun, mutta Anthony ehtii ottamaan hänestä kiinni ennen kuin Valerie tippuu."
                show valerie neutral at left
                v "HUI! Kiitti Ant."
                show anthony neutral at right
                a "Ei mitään."

    s "Onneksi olkoon molemmille! Teidän suoritus oli erittäin eeppinen!"
    v "Pääsemmekö nyt pois täältä?"
    s "{cps=2}...{/cps}"
    scene black
    pause 1.0

    #Musta screen

    jump darkroom














label darkroom:

    scene hotelRoom
    show valerie neutral at left
    v "ÄÄh!!"
    v "..."
    v "Ollaan taas täällä?"
    show anthony neutral at right
    a "Näköjään. Onkohan se ovi nyt auki?"
    "Anthony kokeilee kahvaa ja huokaisee."
    v "Vielä lukossa?"
    a "Jep."
    v "Noh. Mennään sitten takaisin sinne laava huoneeseen. Ehkä se robootti ääni pystyy auttamaan meitä?"
    scene black
    "Valerie ja Anthon kävelee mysteeri huoneeseen, mutta tällä kertaa siellä ei olekaan laavaa ja huonekaluja."
    pause 3.0
    v "Ant?"
    a "Täällä."
    v "Tämä ei todellakaan ole se sama huone kuin äsken."
    v "Miten täällä kuuluisi nähdä yhtään mitään!?"
    "Yhtäkkiä odottamaton tuulenpuuska saa heidät kananlihalle. Selkäpiitä alkaa karmia tuntematon pimeässä huoneessa vaaniva uhka."
    s "Tervetuloa pilkko pimeään huoneeseen! Niin kuin huomaatte, ette näe yhtään mitään. Tästä seuraakin teidän seuraava tehtävä."
    s "Teidän pitää väistää minua samalla kun yritätte löytää oven, jolla pääsette pois huoneesta!"
    a "Mitä ihmettä."
    s "Hauskaa, eikö? :)"
    a "No e-"
    pause 3.0

    scene hotelRoom
    show anthony neutral at right
    a "..."
    show valerie neutral at left
    v "Saiko se sinut kiinni?"
    a "Ehkä?"
    v "Noh, olisiko toinen yritys?"
    a "Todellakin."
    scene black
    # Pimeää
    "Valerie ja Anthony palaavat takaisin pimeään huoneeseen suorittamaan tehtävää."

    show text "Tuomarilla on silmät sidottuna. Hän yrittää saada teidät kiinni. Jos jäät, häviät\nVoittaja on se, joka pystyy pakenemaan tuomarin kiinniottoa." at truecenter
    ""
    hide text


    menu:
        "Kumpi tiimeistä voitti?":

            "Valerie-tiimi"
                $ valeriePoints +=1
                "Robootti kävelee suoraan kohti Anthonia, mutta Valerie ehtii löytämään oven, ennen kun hän jää kiinni."
                v "Löytyi! Nyt me vihdoin pääsemme täältä pois!"
            "Anthony-tiimi"
                $ anthonyPoints +=1
                "Robootti hipaisee Valerien vierestä, mutta Anthony vetää hänet puoleensa ja pelastaa hänet."
                a "Läheltä piti."
                v "Jep. Erityisen pelottavaa, kun ei edes nähdä sitä roboottia..."
                a "Äläpä muuta sano. Etsitään se ovi nopeasti."


    scene black

    pause 3.0

    jump plants










label plants:

    scene hotelRoom

    v "WOAH-"
    a "Miten ihmeessä päädymme aina tänne..."
    v "Ei yhtään hajua, mutta ehkä kolmas kerta toden sanoo."

    scene black
    pause 3.0
    jump closingroom











label closingroom:
    
    scene hotelRoom
    show valerie neutral at left
    v "Täällä taas..."
    show anthony neutral at right
    a "Ehkä nyt me pääsemme pois täältä."
    "Anthony kokeilee avata ovea, muttei se edes liikahda. Hän huohkaisee syvään."
    v "Ja matka jatkuu."
    "Valerie ja Anthony avaavat mysteerioven varovasti ja astuvat sisään."
    v "Toivottavasti tällä kertaa ei ole mitään hengenvaarallista..."
    a "Samaa mieltä."
    
    scene whiteroom
    show valerie neutral at left
    v "Hetkinen, tyhjä huone? Miksiköhän täällä ei ole mitään paitsi tuo näyttö. Kuuluisiko meidän vain kävellä tästä läpi?"
    show anthony neutral at right

    a "Ehkä..."
    "..."
    a "Hallusinoinko minä, vai onko tämä huone jatkuvasti pienenemässä?"
    s "Terve taas rakkaat pelaajat!"
    "Huoneen toisella puolella oleva näyttö käynnistyy, ja siihen ilmestyy Wave."
    show wave neutral
    
    a"Ei taas."
    v "Niin! Päästä meidät pois täältä! Me ollaan leikitty teidän leikkejä jo tarpeeksi pitkään!"
    s "Haha, te olette niin hassuja."
    s "Joka tapauksessa, tervetuloa minun LEMPI huoneeseen!"
    s "Täällä seinät eivät ole niin pysyviä kuin mitä uskotte, hihi! Seinät lähestyvät jatkuvasti kohti huoneen keskustaa, joten litistytte ellette ryhdy heti tosi toimiin."
    s "Onnea teille, sillä tulette tarvitsemaan sitä ;)"
    v "M-mitäh!?"

    a "Juokse, Val!"
    "Valorie ja Anthony alkavat juoksemaan kohti huoneen toista päätä, mutta seinät kuitenkin lähestyivät liian nopeasti."
    v "Ei tässä ole enään tilaa juosta!"
    hide wave neutral
    show wave love
    s "Kohta rakkaat seinämme antavat teille lämpimän halin <3"
    a "MITÄ IH-"
    "{i}PIIIIIIP{/i}"
    pause 3.0

    scene hotelRoom
    v "KÄÄK!"
    a "Tuo oli stressaavaa."
    v "Äläpä muuta sano... Mutta tällä kertaa paremmin, eikö?"
    a "Jep."
    "He siirtyvät suoraan mysteeri huoneeseen ilman hotellihuoneen oven kokeilemista."
    
    scene whiteroom
    s "Huomenta rakkaat sein- KRÖHÖM."
    s "..."
    s "Huomenta... pelaajat."
    v "Juostaan nyt!"
    s "HEI! Kauhean epäkohteliasta D:<"

    # TEHTÄVÄ WOOOOOOO LEKS GO GTIRLY POPS AYYY SKIPIDI SAMMAKKO WOOO

    menu:
        "Kumpi tiimeistä voitti?":
            "Valerie-tiimi":
                $ valeriePoints +=1
                "Valerie pääsee ensimmäisenä huoneen toiselle puolelle, mutta anthonylla on vielä jonkin verran matkaa jäljellä."
                show valerie neutral at left
                v "Ant!"
                "Seinät alkavat painamaan Anthonyn kylkiä."
                "Valerie ottaa kiinni sulkeutuvista seinistä ja kaikilla voimillaan onnistuu pystäyttämään seinät sulkeutumasta."
                s "TÄH??? MI-MITEN???"
                s "ÄLKÄÄ RIKKOKO MINUN RAKKAITA LUOMUKSIANI SENKIN SEKOPÄÄT! >:O"
                show anthony neutral at right
                a "Ei sinun olisi tarvinnut auttaa."
                v "Hehe, kyllä yksinkertainen kiitos olisi myös riittänyt."
                a "...Huoh, kiitos Val."
                v "Ei mitään~"
            "Anthony-tiimi":
                "Anthony pääsee ensimmäisenä huoneen toiselle puolelle, mutta valeriella on vielä jonkin verran matkaa jäljellä."
                "Nähtyään Valerien, Anthony juoksee hänen luokseen ja auttaa häntä pääsemään huoneen toiselle puolelle."
                $ anthonyPoints +=1
                "Va"
                show valerie neutral at left
                v "Ei sinun olisi tarvinnut auttaa."
                show anthony neutral at right
                a "Kyllä yksinkertainen kiitos olisi myös riittänyt."
                v "Kiitos Ant!"
                a "Ei mitään."

    scene black

    pause 3.0
