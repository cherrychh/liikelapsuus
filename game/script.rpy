define v = Character("Valerie", color="cadde8")
define a = Character("Anthony",color="e8cae6")
define s = Character("Wave (systeemi)", color="f2f2f2")
define text = Character("Tehtävä:", kind=nvl)


# 


image lavaroom = "Laavahuone.png"
image hotelRoom = "Hotellihuone.png"
image Lavadark:
  "Laavahuone.png"
  matrixcolor OpacityMatrix(0.5)
image whiteroom = "whiteroom.png"
image whitedark:
  "whiteroom.png"
  matrixcolor OpacityMatrix(0.5)
image logo = "logo.png"
image dieroom = "dieroom.png"
image diedark:
  "dieroom.png"
  matrixcolor OpacityMatrix(0.5)
image plantroom = "plantroom.png"
image plantdark:
  "plantroom.png"
  matrixcolor OpacityMatrix(0.5)
image ninjaroom = "ninjaroom.png"
image ninjadark:
  "ninjaroom.png"
  matrixcolor OpacityMatrix(0.5)

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
    $ darknessflashtime = 1.0 #seconds

    $ valeriePoints = 0
    $ anthonyPoints = 0
    $ numberOfPlayers = 4


    # Joku tausta + söpö robootti :D

    s "Hei! Tervettuloa pelaamaan meidän HUIKEAA peliä 'ROOM'!"
    s "Pääsette seuraamaan kahden ihastuttavan henkilön kokemuksia ja tekemään hulvattoman hauskoja tehtäviä! :D"
    s "Valitkaa teistä yksi pelin tuomariksi"
    menu:
        "kuinka paljon pelaajia on tuomarin lisäksi?"
        "2-6":
            $ numberOfPlayers = 4
        "6+":
            $ numberOfPlayers = 7
            s"Vau! teitähän on paljon."
    s"Jakakaa loput pelaajat kahteen ryhmään (Ryhmä 1 ja Ryhmä 2)."
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
        "Eip.":
            s "{cps=1}...{/cps}"
            s "ALOITETAAN!!!"
    pause 1.0


label lavaroom1st:

    scene hotelRoom

    pause 1.0
    
    "Valerie ja Anthony ovat hyviä ystäviä, jotka ovat vuosien eron jälkeen vihdoin päässeet jälleen viettämään aikaa yhdessä. Ystyävykset ovat löytäneet mukavalta näyttävän hotellin, jossa he päättivät yöpyä."
    "Kaikki oli mennyt aivan mutkattomasti, mutta aamulla jotain outoa kuitenkin tapahtuu"
    # show valerie iloinen
    show valerie happy at left
    v "Hei Ant! Mennäänkö nyt aamupalalle? Näin eilen tuolla tien toisella puolella kivan kahvilan. Siellä näytti olevan kroisantteja, pullia ja kasin muotoisia rinkeleitä."

    # show anthony neutraali
    show anthony neutral at right
    a "Mennään vaan."

    "Anthony kävelee oven luokse ja vääntää kahvaa, mutta ovi näyttää olevan lukossa."

    # show anthony hämmentynyt
    show anthony worry at right
    a "Ompa omituista..."
    v "Mitä?"
    a "Tämä ovi vaikuttaa olevan lukossa ulkoota päin."
    
    # show Valerie hämmentynyt
    show valerie think at left
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

    show valerie happy at left
    v "WOAH!"
    show anthony shock at right
    a "Mitä ihmettä!?"
    v "Onko tuo oikeaa laavaa?"

    "Yhtäkkiä huoneen toisella puolella olevaan näyttöön ilmestyy pieni robootti."
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
    pause darknessflashtime

    jump lavaroom2nd











label lavaroom2nd:

    scene hotelRoom
    pause 1.0
    show valerie neutral at left
    v "Hmm. Näin tosi outoa unta."
    show anthony neutral at right
    a "Niin minäkin..."
    v "Siinä me kävelimme tyhjästä ilmestyneestä ovesta huoneeseen, jonka lattia oli täysin laavan peitossa."
    a "Oikeastiko? Näin itsekkin ihan samanlaista unta."
    v "Katso! Tuossa on se sama ovi mistä menimme unessa."
    show anthony shock at right
    a "Niinpä onkin...Outoa"
    v "Miten tämä kaikki on mahdollista?"
    "Valerie kokeilee uudestaan hotellihuoneen ovea ja toteaa sen olevan yhä lukossa."


    v "Meillä ei varmaan ole muita vaihtoehtoja."
    "Valerie avaa nurkassa olevan mysteeri oven uudestaan."
    scene lavaroom
    show valerie nervousa at left
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
        "Kumpi tiimeistä voitti?"
        "Valerie-tiimi":
            $ valeriePoints +=1
            "Valerie tutkii varovasti huonetta ja löytää molemmille nopean ja turvallisen reitin heille."
            show valerie happy at left
            v "Fiksu reitti, eikö?"
            show anthony happyb at right
            a "Yllättävän."
        "Anthony-tiimi":
            $ anthonyPoints +=1
            "Valerie kompastuu lamppuun, mutta Anthony ehtii ottamaan hänestä kiinni ennen kuin Valerie tippuu."
            show valerie nervousb at left
            v "HUI! Kiitti Ant."
            show anthony happya at right
            a "Ei mitään."

    s "Onneksi olkoon molemmille! Teidän suoritus oli erittäin eeppinen!"
    v "Pääsemmekö nyt pois täältä?"
    s "{cps=2}...{/cps}"
    scene black
    pause darknessflashtime

    #Musta screen

    jump darkroom














label darkroom:

    scene hotelRoom
    show valerie nervousa at left
    v "ÄÄh!!"
    v "..."
    v "Ollaan taas täällä?"
    show anthony worry at right
    a "Näköjään. Onkohan se ovi nyt auki?"
    "Anthony kokeilee kahvaa ja huokaisee."
    v "Vielä lukossa?"
    a "Jep."
    v "Noh. Mennään sitten takaisin sinne laava huoneeseen. Ehkä se robootti ääni pystyy auttamaan meitä?"
    scene black
    "Valerie ja Anthon kävelee mysteeri huoneeseen, mutta tällä kertaa siellä ei olekaan laavaa ja huonekaluja."
    pause darknessflashtime
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
    pause darknessflashtime

### tästä lähin ei tehty ilmeitä ainkaan mä
    scene hotelRoom
    show anthony worry at right
    a "..."
    show valerie neutral at left
    v "Saiko se sinut kiinni?"
    a "Ehkä?"
    v "Noh, olisiko toinen yritys?"
    a "Todellakin."
    scene black
    show text "Tuomarilla on silmät sidottuna ja hän yrittää saada teidät kiinni. Jos jäät, häviät.\nVoittaja on se, joka pysyy pelissä kauiten mukana." at truecenter
    ""
    hide text
    
    menu:
        "Kumpi tiimeistä voitti?"

        "Valerie-tiimi":
            $ valeriePoints +=1
            "Robootti kävelee suoraan kohti Anthonia, mutta Valerie ehtii löytämään oven, ennen kun hän jää kiinni."
            v "Löytyi! Nyt me vihdoin pääsemme täältä pois!"
        "Anthony-tiimi":
            $ anthonyPoints +=1
            "Robootti hipaisee Valerien vierestä, mutta Anthony vetää hänet puoleensa ja pelastaa hänet."
            a "Läheltä piti."
            v "Jep. Erityisen pelottavaa, kun ei edes nähdä sitä robottia..."
            a "Äläpä muuta sano. Etsitään se ovi nopeasti."

    pause darknessflashtime

    jump plants










label plants:

    scene hotelRoom
    show valerie neutral at left
    v "WOAH-"
    show anthony neutral at right
    a "Miten ihmeessä päädymme aina tänne..."
    v "Ei yhtään hajua, mutta ehkä kolmas kerta toden sanoo."
    "Anthony kokeilee hotellihuoneen ovea vielä kerran ennen kuin he lähtevät taas mysteerihuoneeseen."

    scene plantroom
    show valerie neutral at left
    v "Uuu, mikä viidakko! Täällä voisin olla päivät pitkät!"
    show anthony neutral at right
    a "Öhh, minä en... Varo tuota lihansyöjäkasvia."
    v "Hui! Läheltä piti! Tämä ei ehkä sittenkään ole kauhean mukava paikka..."
    a "Joo, ollaan tarkkoina, ettei kuoltaisi."

    show wave neutral

    s "Hei rakkaat mussukat, eikun ihmiset, jos edes olette niitä. Tervetuloa viidakon maailmaan! Tämä oli sinua varten tehty Val! <3"
    v "Ahaa... Kiitti. Olisit ehkä voinut jättää lihansyöjä kasvit pois."
    s "Etkö pidä niistä? :c"
    v "No siis... En?"
    s "..."
    s "Mutta siis, asiaan. Rumpujen pärinää... Jossain täällä on ovi, joka johtaa teidät pois täältä. Kenties jossain kasvuston seassa."
    s "Teidän tehtävänä on löytää ovi, mutta varokaa myös huoneen lihansyöjäkasveja... ettei kävisi pahasti."
    s "Tsemppiä etsimiseen, jos nyt haluatte lähteä tästä ihanasta paikasta!"

    "Valerie ja Anthony yrittävät löytää ovea kasvien seasta, mutta sitä ei löydy mistään."
    v "Löytyykö sitä sieltä?"
    show anthony neutral at right
    a "Eip-"
    "Yhtäkkiä heidän takaa ilmestyy lihansyöjäkasvi, joka nappaa heidät molemmat."
    v "ÄÄH!"
    scene black
    pause darknessflashtime

    scene hotelRoom
    # show valerie stressaantunut?
    show valerie neutral at left
    v "..."
    a "Hei, saatan tietää missä päin se ovi on."
    # valerie piristynyt?
    v "Jes! Mennään sitten!"

    scene plantroom
    show wave neutral
    s "Hei rakkaat mussukat, eikun-"
    show anthony neutral at right
    a "Se taisi olla jossain täällä."
    show wave angry
    s "Törkeää! >:("
    
    scene black
    show plantdark
    show text "Tehtävänne on seuraava.\nTarkkailkaa tuomarin liikkeitä ja kopioikaa niitä.\nJos tuomari huomaa eroavaisuuksia liikkeissänne, pelinne on pelattu.\nVoittaja on se, joka pysyy pisimpään pelissä mukana." at truecenter
    ""
    hide text
    scene plantroom

    menu:
        "Kumpi tiimeistä voitti?"
        "Valerie-tiimi":
            $ valeriePoints +=1
            "Anthonyn takaata ilmestyy lihansyöjäkasvi, joka valmistautuu hyökkäykseen."
            "Valerie kuitenkin ehtii iskemään kasvia Wave:llä ja murskaa sen."
            show wave love
            s "{i}Apua, Val rakastaa minua!{/i}"
            s "IIK! Minäkin rakastan sinua Val!"
            show valerie neutral at left # HÄMMENTYNYT? jooo
            v "Mitäh? Okei?"
            "He lopulta löytävät oven ja avaavat sen..."
        "Anthony-tiimi":
            "Valerie meinaa kaatua, mutta Anthony ehtii ottamaan hänestä kiinni ja estämään hänet kaatumasta."
            $ anthonyPoints +=1
            show anthony neutral at right
            a "Mitäs mieltä olet nyt tästä huoneesta?"
            show valerie neutral at left
            v "Älä edes aloita, Ant."
    v "Minusta kyllä tulee tästä lähtien kasvissyöjä. Todistan niille ilkeille kasveille, että minä syön niitä, eivätkä ne minua."
    show anthony neutral at right
    a "Ahaa. Minusta ei kyllä tule kasvinsyöjää. En edes halua koskea niihin enään tämän jälkeen..."
    "He lopulta löytävät oven ja avaavat sen..."

    scene black
    pause darknessflashtime
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
    s "Joka tapauksessa, tervetuloa minun LEMPI huoneeseeni!"
    s "Täällä seinät eivät ole niin pysyviä kuin mitä uskotte, hihi! Seinät lähestyvät jatkuvasti kohti huoneen keskustaa, joten litistytte ellette ryhdy heti tosi toimiin."
    s "Onnea teille, sillä tulette tarvitsemaan sitä ;)"
    v "M-mitäh!?"

    a "Juokse, Val!"
    "Valorie ja Anthony alkavat juoksemaan kohti huoneen toista päätä, mutta seinät kuitenkin lähestyivät liian nopeasti."
    v "Ei tässä ole enään tilaa juosta!"
    show wave love
    s "Kohta rakkaat seinämme antavat teille lämpimän halin <3"
    a "MITÄ IH-"
    "{i}PIIIIIIP{/i}"
    scene black
    pause darknessflashtime

    scene hotelRoom
    show valerie neutral at left
    v "KÄÄK!"
    show anthony neutral at right
    a "Tuo oli stressaavaa."
    v "Äläpä muuta sano... Mutta tällä kertaa paremmin, eikö?"
    a "Jep."
    "He siirtyvät suoraan mysteeri huoneeseen ilman hotellihuoneen oven kokeilemista."
    
    scene whiteroom
    show wave love
    s "Huomenta rakkaat sein- KRÖHÖM."
    s "..."
    show wave neutral
    s "Huomenta... pelaajat."
    show valerie neutral at left
    v "Juostaan nyt!"
    s "HEI! Kauhean epäkohteliasta D:<"

    scene black
    show whitedark
    show text "Valitkaa molemmista pelaaja, joka on hippa.\nHipan tehtävänä on ottaa vastustajajoukkueen kaikki pelaajat kiinni.\nKiinniotosta otetaan aikaa, ja vähiten aikaa tarvinnut joukkue voittaa pelin." at truecenter
    ""
    hide text
    scene whiteroom

    # LISÄÄ TÄHÄN WAVE (WAVE ANGY) RAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    menu:
        "Kumpi tiimeistä voitti?"
        "Valerie-tiimi":
            $ valeriePoints +=1
            "Valerie pääsee ensimmäisenä huoneen toiselle puolelle, mutta anthonylla on vielä jonkin verran matkaa jäljellä."
            show valerie neutral at left
            v "Ant!"
            "Seinät alkavat painamaan Anthonyn kylkiä."
            "Valerie ottaa kiinni sulkeutuvista seinistä ja kaikilla voimillaan onnistuu pystäyttämään seinät sulkeutumasta."
            s "TÄH??? MI-MITEN???"
            s "ÄLKÄÄ RIKKOKO MINUN RAKKAITA SEINIÄNI SENKIN SEKOPÄÄT! >:O"
            show anthony neutral at right
            a "Ei sinun olisi tarvinnut auttaa."
            v "Hehe, kyllä yksinkertainen kiitos olisi myös riittänyt."
            a "...Huoh, kiitos Val."
            v "Ei mitään~"
        "Anthony-tiimi":
            "Anthony pääsee ensimmäisenä huoneen toiselle puolelle, mutta valeriella on vielä jonkin verran matkaa jäljellä."
            "Nähtyään Valerien, Anthony juoksee hänen luokseen ja auttaa häntä pääsemään huoneen toiselle puolelle."
            $ anthonyPoints +=1
            show valerie neutral at left
            v "Ei sinun olisi tarvinnut auttaa."
            show anthony neutral at right
            a "Kyllä yksinkertainen kiitos olisi myös riittänyt."
            v "Kiitos Ant!"
            a "Ei mitään."

    scene black

    pause darknessflashtime
    jump dieRoom


# laita aina ennen "show [hahmon nimi] neutral(tai joku muu tunne)" kun  niien eka repliikki scenen vaihdon jälkeen tulee nii mun ei tarvii laittaa niit jälkikäteen

label dieRoom:
    scene hotelRoom
    show valerie neutral at left
    v "WOAH..."
    v "Tässä kohtaa tämä ei enään yllätä ketään."
    show anthony neutral at right
    a "Jep. Ehkä tällä kertaa?"
    v "Toivotaan niin."
    "Valerie ja Anthony kävelevät mysteerihuoneen oven luokse ja hengittävät syvään."
    a "Tästä lähtee."
    #show valerie vähän stressed
    v "Jee..."
    
    
    scene dieroom

    s "Noppa, noppa? Noppa! Heippa ystävät! Tällä kertaa huoneen keskellä on suuri kahdeksansivuinen noppa, joka varmasti houkuttelee teitä heittämään sitä!"
    s "Niin kuin havaitsittekin, noppalla on suurin tehtävä tässä huoneessa. Teidän tehtävänä onkin selvittää, mikä merkitys sillä on."
    s "Onnea jälleen kerran, sillä sitä tulette tarvitsemaan tällä kertaa erityisen paljon, hihi ;)"
    show valerie neutral at left
    v "Eli... Me varmaan heitetään noppaa, eikö?"
    show anthony neutral at right
    a "No, en näe mitään muuta vaihtoehtoa myöskään."
    v "Minä voin heittä ensimmäisenä!"
    "Valerie kävelee suuren nopan luokse ja potkaisee sitä."
    "Noppa kimpoaa huoneen seinistä ja lopulta laskeutuu takaisin keskelle."
    v "Numero 2!"
    "{i}PIIIIIP{/i}"
    a "???"

    pause darknessflashtime

    scene hotelRoom
    show valerie neutral at left
    v "ööh?"
    show anthony neutral at right
    a "Ehkä sinun saama arvo oli liian pieni."
    v "Mitää? Onko tämä pelkästään tuurista kiinni? Onpa epäreilua."
    a "Joo, kokeillaanko uudelleen?"
    v "Juu, mutta tällä kertaa sinä aloitat!"

    scene dieroom

    "Anthony kävelee huoneeseen ja heittää jättimäistä noppaa."



    # tehtävä
    scene black
    show diedark
    show text "Tuomari heittää kahdeksansuivuista noppaa, ja nopan silmäluku kertoo teille, minkä haasteen teidän täytyy suorittaa.\nNoppaa heitetään kolme kertaa, eli haasteita on kolme.\nEniten haasteista voittanut joukkue, voittaa." at truecenter
    ""
    hide text
    python:
        tehtavat = ["Pelaajien kesken valitaan yhteinen alue, joka tulee kiertää tasan minuutissa, se joukkue, jonka aika on lähimpänä tasan yhtä minuuttia, voittaa.",
        "1. Kaikki pelaajat etsivät itselleen parin toisesta joukkueesta. Parit asettuvat toistensa vastapäätä siten, että toinen jalka ojennetaan eteenpäin siten, että pelaajien varpaat hipaisevat. Toisen jalan varpaat  laitetaan koskemaan omaa eteen ojennetun jalan kantapäätä.\n\n2. Pelataan toisiaan vastaan kivi-sakset-paperia. Voittaja siirtää etummaisen jalan hänen taaemman jalan kantapäähän, jolloin etummaisesta jalasta tulee taaempi. Hävinnyt siirtää etummaisen jalan varpaita koskettamaan voittajan etummaisen jalan varpaisiin. Pelin häviää se, joka ei saa varpaitaansa koskettamaan toisen varpaita.\n\n3. Jokaisessa erässä voittaja kerryttää joukkueelleen yhden pisteen, ja eniten pisteitä kerännyt joukkue voittaa haasteen.",
        "Kaikki pelaajat asettuvat vaaka-asentoon kädet sivuille ojennettuina, ja toinen jalka mahdollisimman ylös kohotettuna.\nSekä käsien, että jalkojen tulee olla suoriksi ojennettuina.\nSe, joka pysyy asennossa kauemmin ottamatta tukea voittaa haasteen joukkueelleen.",
        "Se, joka pystyy pyörähtämään eniten yhdellä jalalla seisten antamalla vauhtia vain kerran. voittaa haasteen joukkueelleen. Kaikki joukkueen jäsenet saava yrittää kerran.",
        "Kaikki asettuvat seinää vasten ja menevät 90 asteen kyykkyyn seinöö vasten. Tavoitteena on pysyä kyykyssä mahdollisimman kauan, ja haasteen voittaa se joukkue, jonka pelaaja pysyy kauiten kyykyssä.",
        "Kaikki menevät lankkuasentoon, ja yrittävät pysyä mahdollisimman kauan laukussa. Haasteen voittaa se joukkue, jonka pelaaja pysyy kauiten lankussa. ",
        "Molemmista joukkueista valitaan yksi joukkuetta edustava pelaaja. Kivi-sakset-paperilla valitaan kumpi joukkue aloittaa suorituksen. Tuomari ottaa aikaa ja laskee tehtyjen vatsalihasten määrän. Se joukkue, joka tekee enemmän vatsalihaksia 30 sekunnissa, voittaa haasteen.",
        "Molemmista joukkueista valitaan yksi joukkuetta edustava pelaaja. Kivi-sakset-paperilla valitaan kumpi joukkue aloittaa suorituksen. Tuomari ottaa aikaa ja laskee tehtyjen x-hyppyjen määrän. Se joukkue, joka tekee enemmän x-hyppyjä 45 sekunnissa, voittaa haasteen."]
        if numberOfPlayers > 6:
            tehtavat[1] = "1. Pelaajat menevät rinkiin siten, että joka toinen on toisesta joukkueesta.\n\n2. Yksi pelaajista aloittaa siirtäen toisen jalkansa kiinni seuraavan ringissä  seisovan jalkaan.\n\n3. Vuoro siirtyy tälle pelaajalle ja hän siirtää sen jalan, johon edellinen pelaaja koski, kiinni kolmannen pelaajan jalkaan.\n\n4. Jos pelaaja kaatuu tai ei pysty siirtämään jalkaansa, hän putoaa pelistä ja vuoro siirtyy seuraavalle.\n\n4. Pelaajien järjestys ringissä säilyy samana, joten pelaaja siirtää jalkansa aina saman pelaajan jalkaan kunnes tämä putoaa pelistä.\n\n5. Jos rinki tai välit pelaajien välillä jäävät liian suureksi, pelaajat voivat pienentää rinkiä.\n\n6. Peli päättyy, kunnes ringissä on vain kaksi pelaajaa jäljellä ja nämä kaksi ovat voittajia.\n\n\n\n "
        kauttamattomatnumerot = [1,2,3,4,5,6,7,8]
        kautetutnumerot = []
        narrator("Mikä numero nopasta tuli?", interact=False)
        result = renpy.display_menu([(str(kauttamattomatnumerot[0]), str(kauttamattomatnumerot[0])),
        (str(kauttamattomatnumerot[1]), str(kauttamattomatnumerot[1])),
        (str(kauttamattomatnumerot[2]), str(kauttamattomatnumerot[2])),
        (str(kauttamattomatnumerot[3]), str(kauttamattomatnumerot[3])),
        (str(kauttamattomatnumerot[4]), str(kauttamattomatnumerot[4])),
        (str(kauttamattomatnumerot[5]), str(kauttamattomatnumerot[5])),
        (str(kauttamattomatnumerot[6]), str(kauttamattomatnumerot[6])),
        (str(kauttamattomatnumerot[7]), str(kauttamattomatnumerot[7]))])
        kautetutnumerot.append(kauttamattomatnumerot.pop(int(result)-1))
    show text tehtavat[int(result)-1]
    ""
    hide text
    python:
        narrator(f"Mikä numero nopasta tuli? (jos heitto {kautetutnumerot[0]} niin heitä uudelleen)", interact=False)
        result = renpy.display_menu([(str(kauttamattomatnumerot[0]), str(kauttamattomatnumerot[0])),
        (str(kauttamattomatnumerot[1]), str(kauttamattomatnumerot[1])),
        (str(kauttamattomatnumerot[2]), str(kauttamattomatnumerot[2])),
        (str(kauttamattomatnumerot[3]), str(kauttamattomatnumerot[3])),
        (str(kauttamattomatnumerot[4]), str(kauttamattomatnumerot[4])),
        (str(kauttamattomatnumerot[5]), str(kauttamattomatnumerot[5])),
        (str(kauttamattomatnumerot[6]), str(kauttamattomatnumerot[6]))])
        kautetutnumerot.append(kauttamattomatnumerot.pop(int(result)-1))
    show text tehtavat[int(result)-1]
    ""
    hide text
    python:
        narrator(f"Mikä numero nopasta tuli? (jos heitto {kautetutnumerot[0]} tai {kautetutnumerot[0]} niin heitä uudelleen)", interact=False)
        result = renpy.display_menu([(str(kauttamattomatnumerot[0]), str(kauttamattomatnumerot[0])),
        (str(kauttamattomatnumerot[1]), str(kauttamattomatnumerot[1])),
        (str(kauttamattomatnumerot[2]), str(kauttamattomatnumerot[2])),
        (str(kauttamattomatnumerot[3]), str(kauttamattomatnumerot[3])),
        (str(kauttamattomatnumerot[4]), str(kauttamattomatnumerot[4])),
        (str(kauttamattomatnumerot[5]), str(kauttamattomatnumerot[5]))])
        kautetutnumerot.append(kauttamattomatnumerot.pop(int(result)-1))
    show text tehtavat[int(result)-1]
    ""
    hide text
    

    scene dieroom
    menu:
        "Kumpi tiimeistä voitti useammin?"
        "Valerie-tiimi":
            $ valeriePoints +=1
            show anthony neutral at right
            a "Numero 7?"
            s "Wow, onneksi olkoon! Nyt on rakkaan Valin vuoro!"
            show valerie neutral at left
            v "Häh? Mitä minun siis pitää saada, jotta pääsemme eteenpäin?"
            s "Ai niin! Unohdin kertoa. Hupsis!"
            s "Siis, teidän teidän pitää saada ensimmäisellä kerralla numero 8 TAI saada heittojen summaksi 15!"
            v "Eli minun pitää siis saada 8, jotta pääsemme eteenpäin?"
            s "Jep! Eikö olekin jännittävää."
            v "TOSI."
            "Valerie heittää noppaa jännittyneenä."
            show valerie happy at left
            v "Numero 8!!!"
            s "Oho! Onneksi olkoon rakkaa pelaajat!"


        "Anthony-tiimi":
            $ anthonyPoints +=1
            show anthony neutral at right
            a "Numero 8."
            show valerie neutral at left
            v "Oho! Hyvä Ant!"
            s "Onneksi olkoon, pääsette suoraan jatkoon, sillä rakas Ant heitti meidän lempi numeromme!"
            v "Jes!"

    scene black
    pause darknessflashtime
    


label lastroom:
    scene hotelRoom
    show valerie neutral at left
    v "..."
    v "Muistatko, monesko kerta tämä nyt on?"
    show anthony neutral at right
    a "En ole täysin varma... kahdeksas kerta?"
    v "No, oletko valmiina?"
    a "Onko meillä muita vaihtoehtoja?"
    v "..."
    a "Mennään sitten."

    "Valerie ja Anthon avaavat mysteerihuoneen oven ja astuvat varovasti sisään."

    scene ninjaroom

    s "Tervetuloa jälleen rakkaat kaverit! Tällä kertaa olette saapuneet meidän upouuteen ninjahuoneeseen."
    s "Eli siis, jos te välttämättä haluatte lähteä meidän mahtavasta luomuksesta, suorittakaa antamani tehtävä."
    s "Tiedän pitää vain väistää seinistä lentäviä erilaisia palloja. Ei kannata joutua osutuksi, koska... no ette halua tietää."
    show valerie neutral at left
    v "Okei, vaikuttaa tarkeeksi yksinkertaiselta. Minä voin mennä ensin."
    show anthony neutral at right
    a "Okei. Olethan varovainen."
    v "Joo."

    "Valerie kävelee muutaman askeleen eteenpäin samalla yrittäen väistää seinistä tulevia palloja."
    v "WOAH!"
    a "VAL!"
    "Valerieiin osuu lentopallo, ja hän tippuu tyhjyyteen."

    pause darknessflashtime
    scene hotelRoom
    show anthony neutral at right
    a "Val, oletko kunnossa?"
    show valerie neutral at left
    v "Huh... Joo, luulen että olen ihan kunnossa."
    a "..."
    v "Älä nyt, olen kunnossa. Mennäänkö uudestaan?"
    a "..."
    a "Mennään vaan."

    "Valerie ja Anthony astuvat uudestaan mysteerihuoneeseen."

    pause 

    #scene #VIIMEINEN HUONE

    # korjaa tehtävänanto ###############################################################################
    scene black
    show ninjadark
    show text "1. Alussa mennään piiriin jossa olette vieri vieressä.\n\n2.Kaikki hyppää samaan aikaan yksi hyppy taaksepäin ja “jäädytään” itse valittuun ninja-asentoon.\n\n3.Vanhin aloittaa ja yrittää osua kenen tahansa käteen. Molemmat saavat liikuttaa toista jalkaa ja heidän on “jäädyttävä” uuteen asentoon. Jos kilpailijan käteen osutaan, hänen pitää laittaa se käsi selän taakse. Kun kilpailijan molemmat kädet ovat selän takana, hän tippuu pelistä.\n\n3.Vuorot etenevät myötäpäivään ja kilpailija voi “hyökätä” kenen tahansa muun suuntaan ja yrittää koskettaa hänen pelissä mukana olevaa kättä. Joka hyökkäyksellä ja puolustuksella voi siirtää vain toista jalkaa.\n\n4.Viimeinen kilpailija jolla on ainakin toinen käsi mukana pelissä, voittaa." at truecenter
    ""
    hide text
    scene ninjaroom
    menu:
        "Kumpi tiimeistä voitti?"
        "Valerie-tiimi":
            $ valeriePoints +=2
        "Anthony-tiimi":
            $ anthonyPoints +=2

    if valeriePoints > anthonyPoints:
        "Ovi aukeaa Valerien silmien edessä."
        v "Ant, ovi on auki! Mennään!"
        "Valerie astuu ovesta ulos."
        v "Ant, me tehtiin se!"
        v "Ant? Missä olet?"
        v "Ant? ANT!"
        v "Ole kiltti! Älä säikyttele minua taas, tämä ei ole hauskaa!"

        show wave neutral

        s "Onneksi olkoon Valerie! Suoriuduit oikein hyvin. Ant ei tule tällä kertaa mukaasi, silä hän on päättänyt jäädä hengailemaan kanssani."
        s "Hyviä jatkoja sinulle ja onnea vielä! Hei hei!"
        v "Mitä?! En usko sinua! Olet varmasti siepannut Anthonyn! Vapauta hänet minulle nyt heti!"

        show wave laugh
        s "En! Ovi on juuri tuolla, mene vielä kun ehdit. Minua ei toki haittaa, jos päätä jäädä leikkimään kanssani vielä hetkeksi..."
        s "Noh, mitäs sanot? Leikitäänkö, Val?"
    else:
        "Tie vapauteen on muutaman askeleen päässä. Ovi ulos aukeaa Anthonyn silmien edessä ja hän astuu siitä ulos. Anthony katsoo taakse Valerieta."
        "Oli hiljaista, palloja ammuttiin yhä seinistä, mutta odotettua juhlistusta ja syytä ilolle ei ollut. Valerie oli hiljaa. Hänellä oli vielä hymy enne kun hän kaatuu tyhjyyteen-"
        show anthony shock at right
        a "VAL! VAL!!!"
        "Anthony alkaa heti juoksemaan kohti ovea, mutta enne kun hän pääsee takaisin huoneeseen, ovi sulkeutuu... lopullisesti."
        "Anthonyu hakkaa ovea nyrkillään."
        a "Kuuletko minua val? VAL!"

        "Anthony yrittää kaikkensa avaamaan oven, mutta ovi pysyy paikoillaan, ei aukea eikä rikkoudu. Koko tilassa kaikuu Anthonyn raivo ja epätoivoisuus."

        s "Val? Turha toivoa. Ei hän kuuntelisi sinua kuitenkaan, sillä hänellä on nyt paljon parempi ystävä, jonka kanssa hän viettää loppuelämänsä!"
        a "EI! EI!!! Kuinka sinä kehtaat!"
        a "En aio luovuttaa! Minä pelastan hänet hinnalla millä hyvänsä. Katso vaikka..."