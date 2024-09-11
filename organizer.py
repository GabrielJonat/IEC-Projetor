import re


def parse_verses(text,book,chapter):
    chapter = int(chapter)
    newText = ''
    char = 0
    while char < len(text):
        if text[char] == '*':
            chapter += 1
            char += 1
        else:
            if text[char].isnumeric():
                if text[char + 1].isnumeric() and not text[char + 2].isnumeric():
                    newText += book + ' ' + str(chapter) + ':' + text[char] + text[char + 1]+' '
                    char += 1
                elif text[char + 1].isnumeric() and text[char + 2].isnumeric():
                    newText += book + ' ' + str(chapter) + ':' + text[char] + text[char + 1]+text[char+2]+' '
                    char += 2
                else:
                    newText += book+' '+str(chapter)+':'+text[char]+' '
            else:
                newText += text[char]
            char += 1
    return newText


text = """
1 Adão, Sete, Enos,
2 Cainã, Maalalel, Jarede,
3 Enoque, Metusalém, Lameque,
4 Noé, Sem, Cam e Jafé.
5 Os filhos de Jafé foram: Gomer, Magogue, Madai, Javã, Tubal, Meseque e Tiras.
6 Os filhos de Gomer: Asquenaz, Rifate e Togarma.
7 Os filhos de Javã: Elisá, Társis, Quitim e Rodanim.
8 Os filhos de Cam: Cuxe, Mizraim, Pute e Canaã.
9 Os filhos de Cuxe: Sebá, Havilá, Sabtá, Raamá e Sabtecá; os filhos de Raamá: Sabá e Dedã.
10 Cuxe gerou a Ninrode, que começou a ser poderoso na terra.
11 Mizraim gerou a Ludim, a Anamim, a Leabim, a Naftuim,
12 a Patrusim, a Casluim (de quem descendem os filisteus) e a Caftorim.
13 Canaã gerou a Sidom, seu primogênito, a Hete,
14 aos jebuseus, aos amorreus, aos girgaseus,
15 aos heveus, aos arqueus, aos sineus,
16 aos arvadeus, aos zemareus e aos hamateus.
17 Os filhos de Sem: Elão, Assur, Arfaxade, Lude, Arã, Uz, Hul, Geter e Meseque.
18 Arfaxade gerou a Selá, e Selá gerou a Héber.
19 A Héber nasceram dois filhos: o nome de um foi Pelegue, porquanto, nos seus dias, se repartiu a terra; e o nome de seu irmão era Joctã.
20 Joctã gerou a Almodá, a Salefe, a Hazar-Mavé, a Jerá,
21 a Hadorão, a Uzal, a Dicla,
22 a Ebal, a Abimael, a Sabá,
23 a Ofir, a Havilá e a Jobabe; todos estes eram filhos de Joctã.
24 Sem, Arfaxade, Selá,
25 Héber, Pelegue, Reú,
26 Serugue, Naor, Tera
27 e Abrão, que é Abraão.
28 Os filhos de Abraão: Isaque e Ismael.
29 São estas as suas gerações: o primogênito de Ismael foi Nebaiote, depois Quedar, Adbeel, Mibsão,
30 Misma, Dumá, Massá, Hadade, Temá,
31 Jetur, Nafis e Quedemá; estes foram os filhos de Ismael.32 Quanto aos filhos de Quetura, concubina de Abraão, esta deu à luz a Zinrã, a Jocsã, a Medã, a Midiã, a Isbaque e a Sua. Os filhos de Jocsã: Sabá e Dedã.
33 Os filhos de Midiã: Efa, Éfer, Enoque, Abida e Elda; todos estes foram filhos de Quetura.
34 Abraão, pois, gerou a Isaque. Os filhos de Isaque: Esaú e Israel.
35 Os filhos de Esaú: Elifaz, Reuel, Jeús, Jalão e Coré.
36 Os filhos de Elifaz: Temã, Omar, Zefi, Gaetã, Quenaz, Timna e Amaleque.
37 Os filhos de Reuel: Naate, Zerá, Samá e Mizá.
38 Os filhos de Seir: Lotã, Sobal, Zibeão, Aná, Diso, Eser e Disã.
39 Os filhos de Lotã: Hori e Homã; e a irmã de Lotã foi Timna.
40 Os filhos de Sobal eram Aliã, Manaate, Ebal, Sefô e Onã. Os filhos de Zibeão: Aías e Aná.
41 O filho de Aná: Disom. Os filhos de Disom: Hanrão, Esbã, Itrã e Querã.
42 Os filhos de Eser: Bilã, Zaavã e Jaacã. Os filhos de Disã: Uz e Arã.
43 São estes os reis que reinaram na terra de Edom, antes que houvesse rei sobre os filhos de Israel: Bela, filho de Beor, e o nome da sua cidade era Dinabá.
44 Morreu Bela, e em seu lugar reinou Jobabe, filho de Zera, de Bozra.
45 Morreu Jobabe, e em seu lugar reinou Husão, da terra dos temanitas.
46 Morreu Husão, e em seu lugar reinou Hadade, filho de Bedade; este feriu a Midiã no campo de Moabe; o nome da sua cidade era Avite.
47 Morreu Hadade, e em seu lugar reinou Samlá, de Masreca.
48 Morreu Samlá, e em seu lugar reinou Saul, de Reobote, junto ao Eufrates.
49 Morreu Saul, e em seu lugar reinou Baal-Hanã, filho de Acbor.
50 Morreu Baal-Hanã, e em seu lugar reinou Hadade; o nome da sua cidade era Paú, e o de sua mulher era Meetabel, filha de Matrede, filha de Me-Zaabe.
51 Morreu Hadade. São estes os nomes dos príncipes de Edom: o príncipe Timna, o príncipe Alva, o príncipe Jetete,
52 o príncipe Oolibama, o príncipe Elá, o príncipe Pinom,
53 o príncipe Quenaz, o príncipe Temã, o príncipe Mibzar,
54 o príncipe Magdiel, o príncipe Irão; são estes os príncipes de Edom.*
1 São estes os filhos de Israel: Rúben, Simeão, Levi, Judá, Issacar, Zebulom,
2 Dã, José, Benjamim, Naftali, Gade e Aser.
3 Os filhos de Judá: Er, Onã e Selá; estes três lhe nasceram de Bate-Sua, a cananeia. Er, o primogênito de Judá, foi mau aos olhos do Senhor, pelo que o matou.
4 Porém Tamar, nora de Judá, lhe deu à luz a Perez e a Zera. Todos os filhos de Judá foram cinco.
5 Os filhos de Perez: Hezrom e Hamul.
6 Os filhos de Zera: Zinri, Etã, Hemã, Calcol e Dara, cinco ao todo.
7 Os filhos de Carmi: Acar, o perturbador de Israel, que pecou na coisa condenada.
8 O filho de Etã: Azarias.
9 Os filhos de Hezrom, que lhe nasceram: Jerameel, Rão e Quelubai.
10 Rão gerou a Aminadabe; Aminadabe gerou a Naassom, príncipe dos filhos de Judá;
11 Naassom gerou a Salma, e Salma gerou a Boaz;
12 Boaz gerou a Obede, e Obede gerou a Jessé;
13 Jessé gerou a Eliabe, seu primogênito, a Abinadabe, o segundo, a Simeia, o terceiro,
14 a Natanael, o quarto, a Radai, o quinto,
15 a Ozém, o sexto, e a Davi, o sétimo.
16 As irmãs destes foram Zeruia e Abigail. Os filhos de Zeruia foram três: Abisai, Joabe e Asael.
17 Abigail deu à luz a Amasa; e o pai de Amasa foi Jéter, o ismaelita.
18 Calebe, filho de Hezrom, gerou filhos de Azuba, sua mulher, e de Jeriote; foram estes os filhos desta: Jeser, Sobabe e Ardom.
19 Morreu Azuba; e Calebe tomou para si a Efrata, da qual lhe nasceu Hur.
20 Hur gerou a Uri, e Uri gerou a Bezalel.
21 Então, Hezrom coabitou com a filha de Maquir, pai de Gileade; tinha ele sessenta anos quando a tomou, e ela deu à luz a Segube.
22 Segube gerou a Jair, que teve vinte e três cidades na terra de Gileade.
23 Gesur e Arã tomaram as aldeias de Jair, juntamente com Quenate e suas aldeias, a saber, sessenta lugares; todos estes foram filhos de Maquir, pai de Gileade.
24 Depois da morte de Hezrom, em Calebe-Efrata, Abia, mulher de Hezrom, lhe deu a Azur, pai de Tecoa.
25 Os filhos de Jerameel, primogênito de Hezrom, foram: Rão, o primogênito, Buna, Orém, Ozém e Aías.
26 Teve Jerameel outra mulher, cujo nome era Atara; esta foi a mãe de Onã.
27 Os filhos de Rão, primogênito de Jerameel, foram: Maaz, Jamim e Equer.
28 Foram os filhos de Onã: Samai e Jada; e os filhos de Samai: Nadabe e Abisur.
29 A mulher de Abisur chamava-se Abiail e lhe deu a Abã e a Molide.
30 Os filhos de Nadabe: Selede e Apaim; e Selede morreu sem filhos.
31 O filho de Apaim: Isi; o filho de Isi: Sesã. E o filho de Sesã: Alai.
32 Os filhos de Jada, irmão de Samai, foram: Jéter e Jônatas; e Jéter morreu sem filhos.
33 Os filhos de Jônatas: Pelete e Zaza; estes foram os filhos de Jerameel.
34 Sesã não teve filhos, mas filhas; e tinha Sesã um servo egípcio, cujo nome era Jara.
35 Deu, pois, Sesã sua filha por mulher a Jara, a quem ela deu à luz Atai.
36 Atai gerou a Natã, e Natã gerou a Zabade.
37 Zabade gerou a Eflal, e Eflal, a Obede.
38 Obede gerou a Jeú, e Jeú, a Azarias.
39 Azarias gerou a Heles, e Heles, a Eleasa.
40 Eleasa gerou a Sismai, e Sismai, a Salum.
41 Salum gerou a Jecamias, e Jecamias, a Elisama.
42 O primogênito de Calebe, irmão de Jerameel, foi Maressa, que foi o pai de Zife; o filho de Maressa foi Abi-Hebrom.
43 Os filhos de Hebrom: Coré, Tapua, Requém e Sema.
44 Sema gerou a Raão, pai de Jorqueão; e Requém gerou a Samai.
45 O filho de Samai foi Maom; e Maom foi o pai de Bete-Zur.
46 Efá, a concubina de Calebe, deu à luz a Harã, a Mosa e a Gazez; e Harã gerou a Gazez.
47 Os filhos de Jadai: Regém, Jotão, Gesã, Pelete, Efá e Saafe.
48 De Maaca, concubina, gerou Calebe a Seber e a Tiraná;
49 Maaca deu à luz também a Saafe, pai de Madmana, e a Seva, pai de Macbena e de Gibeá; e Acsa foi filha de Calebe.
50 Estes foram os filhos de Calebe. Os filhos de Hur, primogênito de Efrata, foram: Sobal, pai de Quiriate-Jearim,
51 Salma, pai dos belemitas, e Harefe, pai de Bete-Gader.
52 Os filhos de Sobal, pai de Quiriate-Jearim, foram: Haroé e Hazi-Hamenuote.
53 As famílias de Quiriate-Jearim foram: os itritas, os puteus, os sumateus e os misraeus; destes procederam os zoratitas e os estaoleus.
54 Os filhos de Salma: Belém e os netofatitas, Atrote-Bete-Joabe e Hazi-Hamanaate, zoreu.
55 As famílias dos escribas que habitavam em Jabez foram os tiratitas, os simeatitas e os sucatitas; são estes os queneus, que vieram de Hamate, pai da casa de Recabe.*
1 Estes foram os filhos de Davi, que lhe nasceram em Hebrom: o primogênito, Amnom, de Ainoã, a jezreelita; o segundo, Daniel, de Abigail, a carmelita;
2 o terceiro, Absalão, filho de Maaca, filha de Talmai, rei de Gesur; o quarto, Adonias, filho de Hagite;
3 o quinto, Sefatias, de Abital; o sexto, Itreão, de Eglá, sua mulher.
4 Seis filhos lhe nasceram em Hebrom, porque ali reinou sete anos e seis meses; e trinta e três anos reinou em Jerusalém.
5 Estes lhe nasceram em Jerusalém: Simeia, Sobabe, Natã e Salomão; estes quatro lhe nasceram de Bate-Seba, filha de Amiel.
6 Nasceram-lhe mais Ibar, Elisama, Elifelete,
7 Nogá, Nefegue, Jafia,
8 Elisama, Eliada e Elifelete; nove ao todo.
9 Todos estes foram filhos de Davi, afora os filhos das concubinas; e Tamar, irmã deles.
10 O filho de Salomão foi Roboão, de quem foi filho Abias, de quem foi filho Asa, de quem foi filho Josafá;
11 de quem foi filho Jeorão, de quem foi filho Acazias, de quem foi filho Joás;
12 de quem foi filho Amazias, de quem foi filho Azarias, de quem foi filho Jotão;
13 de quem foi filho Acaz, de quem foi filho Ezequias, de quem foi filho Manassés;
14 de quem foi filho Amom, de quem foi filho Josias.
15 Os filhos de Josias foram: o primogênito, Joanã; o segundo, Jeoaquim; o terceiro, Zedequias; o quarto, Salum.
16 Os filhos de Jeoaquim: Jeconias e Zedequias.
17 Os filhos de Jeconias, o cativo: Sealtiel,
18 Malquirão, Pedaías, Senazar, Jecamias, Hosama e Nedabias.
19 Os filhos de Pedaías: Zorobabel e Simei; os filhos de Zorobabel: Mesulão e Hananias; e Selomite, irmã deles;
20 e Hasuba, Oel, Berequias, Hasadias e Jusabe-Hesede; cinco ao todo.
21 Os filhos de Hananias: Pelatias e Jesaías; os filhos de Refaías, os filhos de Arnã, os filhos de Obadias, os filhos de Secanias.
22 O filho de Secanias foi Semaías; os filhos de Semaías: Hatus, Igal, Barias, Nearias e Safate; seis ao todo.
23 Os filhos de Nearias: Elioenai, Ezequias e Azricão; três ao todo.
24 Os filhos de Elioenai: Hodavias, Eliasibe, Pelaías, Acube, Joanã, Delaías e Anani; sete ao todo.*
1 Os filhos de Judá foram: Perez, Hezrom, Carmi, Hur e Sobal.
2 Reaías, filho de Sobal, gerou a Jaate; Jaate gerou a Aumai e a Laade; são estas as famílias dos zoratitas.
3 Estes foram os filhos do pai de Etã: Jezreel, Isma e Idbas; e era o nome da irmã deles Hazelelponi;
4 e mais Penuel, pai de Gedor, e Ezer, pai de Husa; estes foram os filhos de Hur, o primogênito de Efrata e pai de Belém.
5 Asur, pai de Tecoa, teve duas mulheres: Hela e Naara.
6 Naara deu à luz a Auzão, a Héfer, a Temeni e a Haastari; estes foram os filhos de Naara.
7 Os filhos de Hela: Zerete, Isar e Etnã.
8 Coz gerou a Anube e a Zobeba e foi pai das famílias de Aarel, filho de Harum.
9 Foi Jabez mais ilustre do que seus irmãos; sua mãe chamou-lhe Jabez, dizendo: Porque com dores o dei à luz.
10 Jabez invocou o Deus de Israel, dizendo: Oh! Tomara que me abençoes e me alargues as fronteiras, que seja comigo a tua mão e me preserves do mal, de modo que não me sobrevenha aflição! E Deus lhe concedeu o que lhe tinha pedido.
11 Quelube, irmão de Suá, gerou a Meir; este é o pai de Estom.
12 Estom gerou a Bete-Rafa, a Paseia e a Teína, pai de Ir-Naás; estes foram os homens de Reca.
13 Os filhos de Quenaz foram: Otniel e Seraías; o filho de Otniel: Hatate.
14 Meonotai gerou a Ofra, e Seraías gerou a Joabe, fundador do vale dos Artífices, porque os dali eram artífices.
15 Os filhos de Calebe, filho de Jefoné: Iru, Elá e Naã; e o filho de Elá: Quenaz.
16 Os filhos de Jealelel: Zife, Zifa, Tiria e Asareel.
17 Os filhos de Ezra: Jéter, Merede, Éfer e Jalom; foram os filhos de Bitia, filha de Faraó, que Merede tomou por mulher: Miriã, Samai e Isbá, pai de Estemoa.
18 E sua mulher, judia, deu à luz a Jerede, pai de Gedor, a Héber, pai de Socó, e a Jecutiel, pai de Zanoa.
19 Os filhos da mulher de Hodias, irmã de Naã: Abiqueila, o garmita, e Estemoa, o maacatita.
20 Os filhos de Simão: Amnom, Rina, Ben-Hanã e Tilom; e os filhos de Isi: Zoete e Ben-Zoete;
21 os filhos de Selá, filho de Judá: Er, pai de Leca, e Lada, pai de Maressa; Selá foi também pai das famílias da casa dos obreiros em linho, em Bete-Asbeia,
22 como ainda Joquim, e os homens de Cozeba, de Joás, de Sarafe, os quais dominavam sobre Moabe, e de Jasubi-Leém. Estes registros são antigos.
23 Estes eram oleiros e habitantes de Netaim e de Gedera; moravam ali com o rei para o servirem.
24 Os filhos de Simeão foram: Nemuel, Jamim, Jaribe, Zerá e Saul,
25 de quem foi filho Salum, de quem foi filho Mibsão, de quem foi filho Misma.
26 O filho de Misma foi Hamuel, de quem foi filho Zacur, de quem foi filho Simei.
27 Simei teve dezesseis filhos e seis filhas; mas seus irmãos não tiveram muitos filhos, nem se multiplicaram todas as suas famílias como os filhos de Judá.
28 Habitavam em Berseba, em Molada, em Hazar-Sual,
29 em Bila, em Ezém, em Tolade,
30 em Betuel, em Horma, em Ziclague,
31 em Bete-Marcabote, em Hazar-Susim, em Bete-Biri e em Saaraim. Estas foram as suas cidades, até ao reinado de Davi.
32 As suas aldeias foram: Etã, Aim, Rimom, Toquém e Asã; cinco cidades,
33 com todas as suas aldeias que estavam ao redor destas cidades, até Baal. Estas foram as suas habitações e tinham seu registro genealógico.
34 Estes, registrados por seus nomes, foram príncipes nas suas famílias: Mesobabe, Janleque, Josa, filho de Amazias,
35 Joel, Jeú, filho de Josibias, filho de Seraías, filho de Asiel,
36 Elioenai, Jaacobá, Jesoaías, Asaías, Adiel, Jesimiel, Benaia,
37 Ziza, filho de Sifi, filho de Alom, filho de Jedaías, filho de Sinri, filho de Semaías;
38 e as famílias de seus pais se multiplicaram abundantemente.
39 Chegaram até à entrada de Gedor, ao oriente do vale, à procura de pasto para os seus rebanhos.
40 Acharam pasto farto e bom e a terra espaçosa, tranquila e pacífica, onde habitaram, dantes, os descendentes de Cam.
41 Estes, que estão registrados por seus nomes, vieram nos dias de Ezequias, rei de Judá, e derribaram as tendas, e feriram os meunitas que se encontraram ali, e os destruíram totalmente até ao dia de hoje, e habitaram em lugar deles, porque ali havia pasto para os seus rebanhos.
42 Também deles, dos filhos de Simeão, quinhentos homens foram ao monte Seir, tendo por capitães a Pelatias, a Nearias, a Refaías e a Uziel, filhos de Isi.
43 Feriram o restante dos que escaparam dos amalequitas e habitam ali até ao dia de hoje.*
1 Quanto aos filhos de Rúben, o primogênito de Israel (pois era o primogênito, mas, por ter profanado o leito de seu pai, deu-se a sua primogenitura aos filhos de José, filho de Israel; de modo que, na genealogia, não foi contado como primogênito.
2 Judá, na verdade, foi poderoso entre seus irmãos, e dele veio o príncipe; porém o direito da primogenitura foi de José.),
3 foram estes: Enoque, Palu, Hezrom e Carmi.
4 O filho de Joel: Semaías, de quem foi filho Gogue, de quem foi filho Simei,
5 de quem foi filho Mica, de quem foi filho Reaías, de quem foi filho Baal,
6 de quem foi filho Beera, o qual Tiglate-Pileser, rei da Assíria, levou cativo; ele foi príncipe dos rubenitas.
7 Quanto a seus irmãos, pelas suas famílias, quando foram inscritos nas genealogias segundo as suas descendências, tinham por cabeças Jeiel, Zacarias,
8 Bela, filho de Azaz, filho de Sema, filho de Joel, que habitaram em Aroer, até Nebo e Baal-Meom;
9 também habitaram do lado oriental, até à entrada do deserto, o qual se estende até ao rio Eufrates, porque o seu gado se tinha multiplicado na terra de Gileade.
10 Nos dias de Saul, fizeram guerra aos hagarenos, que caíram pelo poder de sua mão, e habitaram nas tendas deles, em toda a terra fronteira de Gileade, do lado oriental.
11 Os filhos de Gade habitaram defronte deles, na terra de Basã, até Salca.
12 Joel foi o cabeça, e Safã, o segundo; também Janai e Safate estavam em Basã.
13 Seus irmãos, segundo as suas casas paternas, foram: Micael, Mesulão, Seba, Jorai, Jacã, Zia e Héber; ao todo, sete;
14 estes foram os filhos de Abiail, filho de Huri, filho de Jaroa, filho de Gileade, filho de Micael, filho de Jesisai, filho de Jado, filho de Buz.
15 Aí, filho de Abdiel, filho de Guni, foi o cabeça da sua família.
16 Habitaram em Gileade, em Basã e suas aldeias, bem como até aos limites de todos os arredores de Sarom.
17 Todos estes foram inscritos na genealogia, nos dias de Jotão, rei de Judá, e nos dias de Jeroboão, rei de Israel.
18 Dos filhos de Rúben, dos gaditas e da meia tribo de Manassés, homens valentes, que traziam escudo e espada, entesavam o arco e eram destros na guerra, houve quarenta e quatro mil setecentos e sessenta, capazes de sair a combate.
19 Fizeram guerra aos hagarenos, como a Jetur, a Nafis e a Nodabe.
20 Foram ajudados contra eles, e os hagarenos e todos quantos estavam com eles foram entregues nas suas mãos; porque, na peleja, clamaram a Deus, que lhes deu ouvidos, porquanto confiaram nele.
21 Levaram o gado deles: cinquenta mil camelos, duzentas e cinquenta mil ovelhas, dois mil jumentos; e cem mil pessoas.
22 Porque muitos caíram feridos à espada, pois de Deus era a peleja; e habitaram no lugar deles até ao exílio.
23 Os filhos da meia tribo de Manassés habitaram naquela terra de Basã até Baal-Hermom, e Senir, e o monte Hermom; e eram numerosos.
24 Estes foram cabeças de suas famílias, a saber: Éfer, Isi, Eliel, Azriel, Jeremias, Hodavias e Jadiel, guerreiros valentes, homens famosos, cabeças de suas famílias.
25 Porém cometeram transgressões contra o Deus de seus pais e se prostituíram, seguindo os deuses dos povos da terra, os quais Deus destruíra de diante deles.
26 Pelo que o Deus de Israel suscitou o espírito de Pul, rei da Assíria, e o espírito de Tiglate-Pileser, rei da Assíria, que os levou cativos, a saber: os rubenitas, os gaditas e a meia tribo de Manassés, e os trouxe para Hala, Habor e Hara e para o rio Gozã, onde permanecem até ao dia de hoje.*
1 Os filhos de Levi foram: Gérson, Coate e Merari.
2 Os filhos de Coate: Anrão, Isar, Hebrom e Uziel.
3 Os filhos de Anrão: Arão, Moisés e Miriã. Os filhos de Arão: Nadabe, Abiú, Eleazar e Itamar.
4 Eleazar gerou a Fineias, e Fineias, a Abisua;
5 Abisua gerou a Buqui, e Buqui, a Uzi;
6 Uzi gerou a Zeraías, e Zeraías, a Meraiote;
7 Meraiote gerou a Amarias, e Amarias, a Aitube;
8 Aitube gerou a Zadoque, e Zadoque, a Aimaás;
9 Aimaás gerou a Azarias, e Azarias, a Joanã;
10 Joanã gerou a Azarias; este é o que serviu de sacerdote na casa que Salomão tinha edificado em Jerusalém.
11 Azarias gerou a Amarias, e Amarias, a Aitube;
12 Aitube gerou a Zadoque, e Zadoque, a Salum;
13 Salum gerou a Hilquias, e Hilquias, a Azarias;
14 Azarias gerou a Seraías, e Seraías, a Jeozadaque;
15 Jeozadaque foi levado cativo, quando o Senhor levou para o exílio a Judá e a Jerusalém pela mão de Nabucodonosor.
16 Os filhos de Levi: Gérson, Coate e Merari.
17 São estes os nomes dos filhos de Gérson: Libni e Simei.
18 Os filhos de Coate: Anrão, Isar, Hebrom e Uziel.
19 Os filhos de Merari: Mali e Musi; são estas as famílias dos levitas, segundo as casas de seus pais.
20 O filho de Gérson foi Libni, de quem foi filho Jaate, de quem foi filho Zima,
21 de quem foi filho Joá, de quem foi filho Ido, de quem foi filho Zerá, de quem foi filho Jeaterai.
22 O filho de Coate foi Aminadabe, de quem foi filho Coré, de quem foi filho Assir,
23 de quem foi filho Elcana, de quem foi filho Ebiasafe, de quem foi filho Assir,
24 de quem foi filho Taate, de quem foi filho Uriel, de quem foi filho Uzias, de quem foi filho Saul.
25 Os filhos de Elcana: Amasai e Aimote.
26 Quanto a Elcana, foi seu filho Zofai, de quem foi filho Naate,
27 de quem foi filho Eliabe, de quem foi filho Jeroão, de quem foi filho Elcana.
28 Os filhos de Samuel: o primogênito, Joel, e depois Abias.
29 O filho de Merari foi Mali, de quem foi filho Libni, de quem foi filho Simei, de quem foi filho Uzá,
30 de quem foi filho Simeia, de quem foi filho Hagias, de quem foi filho Asaías.
31 São estes os que Davi constituiu para dirigir o canto na Casa do Senhor, depois que a arca teve repouso.
32 Ministravam diante do tabernáculo da tenda da congregação com cânticos, até que Salomão edificou a Casa do Senhor em Jerusalém; e exercitavam o seu ministério segundo a ordem prescrita.
33 São estes os que serviam com seus filhos. Dos filhos dos coatitas: Hemã, o cantor, filho de Joel, filho de Samuel,
34 filho de Elcana, filho de Jeroão, filho de Eliel, filho de Toá,
35 filho de Zufe, filho de Elcana, filho de Maate, filho de Amasai,
36 filho de Elcana, filho de Joel, filho de Azarias, filho de Sofonias,
37 filho de Taate, filho de Assir, filho de Ebiasafe, filho de Coré,
38 filho de Isar, filho de Coate, filho de Levi, filho de Israel.
39 Seu irmão Asafe estava à sua direita; era Asafe filho de Berequias, filho de Simeia,
40 filho de Micael, filho de Baaseias, filho de Malquias,
41 filho de Etni, filho de Zera, filho de Adaías,
42 filho de Etã, filho de Zima, filho de Simei,
43 filho de Jaate, filho de Gérson, filho de Levi.
44 Seus irmãos, os filhos de Merari, estavam à esquerda, a saber: Etã, filho de Quisi, filho de Abdi, filho de Maluque,
45 filho de Hasabias, filho de Amazias, filho de Hilquias,
46 filho de Anzi, filho de Bani, filho de Semer,
47 filho de Mali, filho de Musi, filho de Merari, filho de Levi.
48 Seus irmãos, os levitas, foram postos para todo o serviço do tabernáculo da Casa de Deus.
49 Arão e seus filhos faziam ofertas sobre o altar do holocausto e sobre o altar do incenso, todo o serviço do lugar santíssimo e a expiação por Israel, segundo tudo quanto Moisés, servo de Deus, tinha ordenado.
50 Foi filho de Arão Eleazar, de quem foi filho Fineias, de quem foi filho Abisua,
51 de quem foi filho Buqui, de quem foi filho Uzi, de quem foi filho Zeraías,
52 de quem foi filho Meraiote, de quem foi filho Amarias, de quem foi filho Aitube,
53 de quem foi filho Zadoque, de quem foi filho Aimaás.
54 São estes os lugares que eles habitavam, segundo os seus acampamentos, dentro dos seus limites, a saber: aos filhos de Arão, das famílias dos coatitas, pois lhes caiu a sorte,
55 deram-lhes Hebrom, na terra de Judá, e os seus arredores.
56 Porém o campo da cidade com suas aldeias deram a Calebe, filho de Jefoné.
57 Aos filhos de Arão deram as cidades de refúgio: Hebrom e Libna com seus arredores, Jatir e Estemoa com seus arredores,
58 Hilém com seus arredores, Debir com seus arredores,
59 Asã com seus arredores e Bete-Semes com seus arredores;
60 da tribo de Benjamim, Geba com seus arredores, Alemete com seus arredores e Anatote com seus arredores; ao todo, treze cidades, segundo as suas famílias.
61 Aos filhos de Coate, que restaram da família da tribo, caíram por sorte dez cidades da meia tribo, metade de Manassés.
62 Aos filhos de Gérson, segundo as suas famílias, da tribo de Issacar, da tribo de Aser, da tribo de Naftali e da tribo de Manassés, em Basã, caíram treze cidades.
63 Aos filhos de Merari, segundo as suas famílias, da tribo de Rúben, da tribo de Gade e da tribo de Zebulom, caíram por sorte doze cidades.
64 Assim, deram os filhos de Israel aos levitas estas cidades com seus arredores.
65 Deram-lhes por sorte, da tribo dos filhos de Judá, da tribo dos filhos de Simeão e da tribo dos filhos de Benjamim, estas cidades, que são mencionadas nominalmente.
66 A algumas das famílias dos filhos de Coate foram dadas cidades dos seus territórios da parte da tribo de Efraim.
67 Pois lhes deram as cidades de refúgio, Siquém com seus arredores, na região montanhosa de Efraim, como também Gezer com seus arredores,
68 Jocmeão com seus arredores, Bete-Horom com seus arredores,
69 Aijalom com seus arredores e Gate-Rimom com seus arredores;
70 e, da meia tribo de Manassés, Aner com seus arredores e Bileã com seus arredores foram dadas às demais famílias dos filhos de Coate.
71 Aos filhos de Gérson, da família da meia tribo de Manassés, deram, em Basã, Golã com seus arredores e Astarote com seus arredores;
72 e da tribo de Issacar: Quedes com seus arredores, Daberate com seus arredores,
73 Ramote com seus arredores e Aném com seus arredores;
74 e da tribo de Aser: Masal com seus arredores, Abdom com seus arredores,
75 Hucoque com seus arredores e Reobe com seus arredores;
76 e da tribo de Naftali na Galileia: Quedes com seus arredores, Hamom com seus arredores e Quiriataim com seus arredores.
77 Os demais filhos de Merari receberam, da tribo de Zebulom, Rimono com seus arredores e Tabor com seus arredores;
78 e dalém do Jordão, na altura de Jericó, ao oriente do Jordão, deram-se-lhes, da tribo de Rúben, Bezer com seus arredores no deserto, Jaza com seus arredores,
79 Quedemote com seus arredores e Mefaate com seus arredores;
80 e da tribo de Gade em Gileade: Ramote com seus arredores, Maanaim com seus arredores,
81 Hesbom com seus arredores e Jazer com seus arredores.*
1 Os filhos de Issacar foram: Tola, Puá, Jasube e Sinrom; quatro ao todo.
2 Os filhos de Tola: Uzi, Refaías, Jeriel, Jamai, Ibsão e Samuel, chefes das suas famílias, descendentes de Tola; homens valentes nas suas gerações, cujo número, nos dias de Davi, foi de vinte e dois mil e setecentos.
3 O filho de Uzi: Izraías; e os filhos de Izraías: Micael, Obadias, Joel e Issias; cinco ao todo; todos eles chefes.
4 Tinham, nas suas gerações, segundo as suas famílias, em tropas de guerra, trinta e seis mil homens; pois tinham muitas mulheres e filhos.
5 Seus irmãos, em todas as famílias de Issacar, homens valentes, foram oitenta e sete mil, todos registrados pelas suas genealogias.
6 Os filhos de Benjamim: Bela, Bequer e Jediael; três ao todo.
7 Os filhos de Bela: Esbom, Uzi, Uziel, Jerimote e Iri; cinco ao todo; chefes das suas famílias, homens valentes, foram vinte e dois mil e trinta e quatro, registrados pelas suas genealogias.
8 Os filhos de Bequer: Zemira, Joás, Eliézer, Elioenai, Onri, Jerimote, Abias, Anatote e Alemete; todos filhos de Bequer.
9 O número deles, registrados pelas suas genealogias, segundo as suas gerações, chefes das suas famílias, homens valentes, vinte mil e duzentos.
10 O filho de Jediael: Bilã; os filhos de Bilã: Jeús, Benjamim, Eúde, Quenaana, Zetã, Társis e Aisaar.
11 Todos estes, filhos de Jediael, foram chefes das suas famílias, homens valentes, dezessete mil e duzentos, capazes de sair à guerra.
12 Supim e Hupim eram filhos de Ir; e Husim, filho de Aer.
13 Os filhos de Naftali: Jaziel, Guni, Jezer e Salum, filhos de Bila.
14 O filho de Manassés: Asriel, de sua concubina síria, que também deu à luz a Maquir, pai de Gileade.
15 Maquir tomou a irmã de Hupim e Supim por mulher. O nome dela era Maaca; o nome do irmão de Maquir era Zelofeade, o qual teve só filhas.
16 Maaca, mulher de Maquir, teve um filho, a quem chamou Perez; irmão deste foi Seres. Os filhos de Perez foram Ulão e Requém.
17 O filho de Ulão: Bedã. Tais foram os filhos de Gileade, filho de Maquir, filho de Manassés.
18 Sua irmã Hamolequete deu à luz a Isode, a Abiezer e a Macla.
19 Foram os filhos de Semida: Aiã, Siquém, Liqui e Anião.
20 Era filho de Efraim Sutela, de quem foi filho Berede, de quem foi filho Taate, de quem foi filho Eleada, de quem foi filho Taate,
21 de quem foi filho Zabade, de quem foi filho Sutela; e ainda Ézer e Eleade, mortos pelos homens de Gate, naturais da terra, pois eles desceram para roubar o gado destes.
22 Pelo que por muitos dias os chorou Efraim, seu pai, cujos irmãos vieram para o consolar.
23 Depois, coabitou com sua mulher, e ela concebeu e teve um filho, a quem ele chamou Berias, porque as coisas iam mal na sua casa.
24 Sua filha foi Seerá, que edificou a Bete-Horom, a de baixo e a de cima, como também a Uzém-Seerá.
25 O filho de Berias foi Refa, de quem foi filho Resefe, de quem foi filho Tela, de quem foi filho Taã,
26 de quem foi filho Ladã, de quem foi filho Amiúde, de quem foi filho Elisama,
27 de quem foi filho Num, de quem foi filho Josué.
28 A possessão e habitação deles foram: Betel e as suas aldeias; ao oriente, Naarã; e, ao ocidente, Gezer e suas aldeias, Siquém e suas aldeias, até Aia e suas aldeias;
29 do lado dos filhos de Manassés, Bete-Seã e suas aldeias, Taanaque e suas aldeias, Megido e suas aldeias, Dor e suas aldeias; nestas, habitaram os filhos de José, filho de Israel.
30 Os filhos de Aser: Imna, Isvá, Isvi e Berias e Sera, irmã deles.
31 Os filhos de Berias: Héber e Malquiel; este foi o pai de Birzavite.
32 Héber gerou a Jaflete, a Somer, a Hotão e a Suá, irmã deles.
33 Os filhos de Jaflete: Pasaque, Bimal e Asvate; estes foram os filhos de Jaflete.
34 Os filhos de Semer: Aí, Roga, Jeubá e Arã.
35 Os filhos de seu irmão Helém: Zofa, Imna, Seles e Amal.
36 Os filhos de Zofa: Sua, Harnefer, Sual, Beri, Inra,
37 Bezer, Hode, Sama, Silsa, Itrã e Beera.
38 Os filhos de Jéter: Jefoné, Pispa e Ara.
39 Os filhos de Ula: Ara, Haniel e Rizia.
40 Todos estes foram filhos de Aser, chefes das famílias, escolhidos, homens valentes, chefes de príncipes, registrados nas suas genealogias para o serviço na guerra; seu número foi de vinte e seis mil homens.*
1 Benjamim gerou a Bela, seu primogênito, a Asbel, o segundo, a Aará, o terceiro,
2 a Noá, o quarto, e a Rafa, o quinto.
3 Bela teve estes filhos: Adar, Gera, Abiúde,
4 Abisua, Naamã, Aoá,
5 Gera, Sefufá e Hurão.
6 Estes foram os filhos de Eúde, que foram chefes das famílias dos moradores de Geba e transportados para o exílio a Manaate:
7 Naamã, Aías e Gera; este os transportou e gerou a Uzá e a Aiude.
8 Saaraim, depois de ter repudiado suas mulheres Husim e Baara, gerou nos campos de Moabe,
9 de Hodes, sua mulher, a Jobabe, a Zíbia, a Messa, a Malcã,
10 a Jeús, a Saquias e a Mirma; foram estes os seus filhos, chefes das famílias.
11 Husim gerou a Abitube e a Elpaal.
12 Os filhos de Elpaal foram: Héber, Misã e Semede; este edificou a Ono e a Lode e suas aldeias.
13 Berias e Sema foram cabeças das famílias dos moradores de Aijalom, que afugentaram os moradores de Gate.
14 Aiô, Sasaque, Jeremote,
15 Zebadias, Arade, Éder,
16 Micael, Ispa e Joá foram filhos de Berias.
17 Zebadias, Mesulão, Hizqui, Héber,
18 Ismerai, Izlias e Jobabe, filhos de Elpaal.
19 Jaquim, Zicri, Zabdi,
20 Elienai, Ziletai, Eliel,
21 Adaías, Beraías e Sinrate, filhos de Simei.
22 Ispã, Héber, Eliel,
23 Abdom, Zicri, Hanã,
24 Hananias, Elão, Antotias,
25 Ifdeias e Penuel, filhos de Sasaque.
26 Sanserai, Searias, Atalias,
27 Jaaresias, Elias e Zicri, filhos de Jeroão.
28 Estes foram chefes das famílias, segundo as suas gerações, e habitaram em Jerusalém.
29 Em Gibeão habitou o pai de Gibeão, cuja mulher se chamava Maaca,
30 e também seu filho primogênito Abdom e ainda Zur, Quis, Baal, Nadabe,
31 Gedor, Aiô e Zequer.
32 Miclote gerou a Simeia. Estes habitaram em Jerusalém, com seus irmãos, bem defronte deles.
33 Ner gerou a Quis; e Quis gerou a Saul; Saul gerou a Jônatas, a Malquisua, a Abinadabe e a Esbaal.
34 Filho de Jônatas foi Meribe-Baal, e Meribe-Baal gerou a Mica.
35 Os filhos de Mica foram: Pitom, Meleque, Tareia e Acaz.
36 Acaz gerou a Jeoada; Jeoada gerou a Alemete, a Azmavete e a Zinri; e Zinri gerou a Mosa.
37 Mosa gerou a Bineá, de quem foi filho Rafa, de quem foi filho Eleasa, de quem foi filho Azel.
38 Teve Azel seis filhos, cujos nomes foram: Azricão, Bocru, Ismael, Searias, Obadias e Hanã; todos estes foram filhos de Azel.
39 Os filhos de Eseque, seu irmão, foram: Ulão, seu primogênito, Jeús, o segundo, e Elifelete, o terceiro.
40 Os filhos de Ulão foram homens valentes, flecheiros; e tiveram muitos filhos e netos: cento e cinquenta. Todos estes foram dos filhos de Benjamim.*
1 Todo o Israel foi registrado por genealogias e inscrito no Livro dos Reis de Israel, e Judá foi levado para o exílio à Babilônia, por causa da sua transgressão.
2 Os primeiros habitadores, que de novo vieram morar nas suas próprias possessões e nas suas cidades, foram os israelitas, os sacerdotes, os levitas e os servos do templo.
3 Porém alguns dos filhos de Judá, dos filhos de Benjamim e dos filhos de Efraim e Manassés habitaram em Jerusalém:
4 Utai, filho de Amiúde, filho de Onri, filho de Inri, filho de Bani, dos filhos de Perez, filho de Judá;
5 dos silonitas: Asaías, o primogênito, e seus filhos;
6 dos filhos de Zerá: Jeuel e seus irmãos; seiscentos e noventa ao todo;
7 dos filhos de Benjamim: Salu, filho de Mesulão, filho de Hodavias, filho de Hassenuá;
8 Ibneias, filho de Jeroão, e Elá, filho de Uzi, filho de Micri, e Mesulão, filho de Sefatias, filho de Reuel, filho de Ibnijas;
9 e seus irmãos, segundo as suas gerações; novecentos e cinquenta e seis ao todo; todos estes homens foram cabeças de famílias nas casas de suas famílias.
10 Dos sacerdotes: Jedaías, Jeoiaribe, Jaquim,
11 Azarias, filho de Hilquias, filho de Mesulão, filho de Zadoque, filho de Meraiote, filho de Aitube, príncipe da Casa de Deus;
12 Adaías, filho de Jeroão, filho de Pasur, filho de Malquias, e Masai, filho de Adiel, filho de Jazera, filho de Mesulão, filho de Mesilemite, filho de Imer,
13 como também seus irmãos, cabeças das suas famílias; mil setecentos e sessenta ao todo, homens capazes para a obra do ministério da Casa de Deus.
14 Dos levitas: Semaías, filho de Hassube, filho de Azricão, filho de Hasabias, dos filhos de Merari;
15 Baquebacar, Heres, Galal e Matanias, filho de Mica, filho de Zicri, filho de Asafe;
16 Obadias, filho de Semaías, filho de Galal, filho de Jedutum; Berequias, filho de Asa, filho de Elcana, morador das aldeias dos netofatitas.
17 Os porteiros: Salum, Acube, Talmom e Aimã e os irmãos deles; Salum era o chefe.
18 Estavam até agora de guarda à porta do rei, do lado do oriente; tais foram os porteiros dos arraiais dos filhos de Levi.
19 Salum, filho de Coré, filho de Ebiasafe, filho de Corá, e seus irmãos da casa de seu pai, os coreítas, estavam encarregados da obra do ministério e eram guardas das portas do tabernáculo; e seus pais tinham sido encarregados do arraial do Senhor e eram guardas da entrada.
20 Fineias, filho de Eleazar, os regia nesse tempo, e o Senhor era com ele.
21 Zacarias, filho de Meselemias, era o porteiro da entrada da tenda da congregação.
22 Todos estes, escolhidos para guardas das portas, foram duzentos e doze. Estes foram registrados pelas suas genealogias nas suas respectivas aldeias; e Davi e Samuel, o vidente, os constituíram cada um no seu cargo.
23 Guardavam, pois, eles e seus filhos as portas da Casa do Senhor, na casa da tenda.
24 Os porteiros estavam aos quatro ventos: ao oriente, ao ocidente, ao norte e ao sul.
25 Seus irmãos, que habitavam nas suas aldeias, tinham de vir, de tempo em tempo, para servir com eles durante sete dias;
26 porque havia sempre, naquele ofício, quatro porteiros principais, que eram levitas, e tinham a seu cargo as câmaras e os tesouros da Casa de Deus.
27 Estavam alojados à roda da Casa de Deus, porque a vigilância lhes estava encarregada, e tinham o dever de a abrir, todas as manhãs.
28 Alguns deles estavam encarregados dos utensílios do ministério, porque estes eram contados quando eram trazidos e quando eram tirados.
29 Outros havia que estavam encarregados dos móveis e de todos os objetos do santuário, como também da flor de farinha, do vinho, do azeite, do incenso e da especiaria.
30 Alguns dos filhos dos sacerdotes confeccionavam as especiarias.
31 Matitias, dentre os levitas, o primogênito de Salum, o coreíta, tinha o cargo do que se fazia em assadeiras.
32 Outros dos seus irmãos, dos filhos dos coatitas, tinham o encargo de preparar os pães da proposição para todos os sábados.
33 Quanto aos cantores, cabeças das famílias entre os levitas, estavam alojados nas câmaras do templo e eram isentos de outros serviços; porque, de dia e de noite, estavam ocupados no seu mister.
34 Estes foram cabeças das famílias entre os levitas, chefes em suas gerações, e habitavam em Jerusalém.
35 Em Gibeão habitou Jeiel, pai de Gibeão, cuja mulher se chamava Maaca;
36 e também seu filho primogênito Abdom e ainda Zur, Quis, Baal, Ner, Nadabe,
37 Gedor, Aiô, Zacarias e Miclote.
38 Miclote gerou a Simeia. Estes habitaram em Jerusalém, com seus irmãos, bem defronte deles.
39 Ner gerou a Quis; e Quis gerou a Saul, Saul gerou a Jônatas, a Malquisua, a Abinadabe e a Esbaal.
40 Filho de Jônatas foi Meribe-Baal, e Meribe-Baal gerou a Mica.
41 Os filhos de Mica foram: Pitom, Meleque e Tareia.
42 Acaz gerou a Jaerá, e Jaerá gerou a Alemete, a Azmavete e a Zinri; e Zinri gerou a Mosa.
43 Mosa gerou a Bineá, de quem foi filho Refaías, de quem foi filho Eleasa, de quem foi filho Azel.
44 Teve Azel seis filhos, cujos nomes foram Azricão, Bocru, Ismael, Searias, Obadias e Hanã; todos estes foram filhos de Azel.*
1 Os filisteus pelejaram contra Israel; e, tendo os homens de Israel fugido de diante dos filisteus, caíram mortos no monte Gilboa.
2 Os filisteus perseguiram Saul e seus filhos e mataram Jônatas, Abinadabe e Malquisua, filhos de Saul.
3 Agravou-se muito a peleja contra Saul, os flecheiros o avistaram, e ele muito os temeu.
4 Então, disse Saul ao seu escudeiro: Arranca a tua espada e atravessa-me com ela, para que, porventura, não venham estes incircuncisos e escarneçam de mim. Porém o seu escudeiro não o quis, porque temia muito; então, Saul tomou a espada e se lançou sobre ela.
5 Vendo, pois, o seu escudeiro que Saul já era morto, também ele se lançou sobre a espada e morreu com ele.
6 Assim, morreram Saul e seus três filhos; e toda a sua casa pereceu juntamente com ele.
7 Vendo os homens de Israel que estavam no vale que os homens de Israel fugiram e que Saul e seus filhos estavam mortos, desampararam as cidades e fugiram; e vieram os filisteus e habitaram nelas.
8 Sucedeu, pois, que, vindo os filisteus ao outro dia a despojar os mortos, acharam Saul e os seus filhos caídos no monte Gilboa.
9 E os despojaram, tomaram a sua cabeça e as suas armas e enviaram mensageiros pela terra dos filisteus, em redor, a levar as boas-novas a seus ídolos e entre o povo.
10 Puseram as armas de Saul no templo de seu deus, e a sua cabeça afixaram na casa de Dagom.
11 Ouvindo, pois, toda a Jabes de Gileade tudo quanto os filisteus fizeram a Saul,
12 então, todos os homens valentes se levantaram, e tomaram o corpo de Saul e os corpos dos filhos, e os trouxeram a Jabes; e sepultaram os seus ossos debaixo de um arvoredo, em Jabes, e jejuaram sete dias.
13 Assim, morreu Saul por causa da sua transgressão cometida contra o Senhor, por causa da palavra do Senhor, que ele não guardara; e também porque interrogara e consultara uma necromante
14 e não ao Senhor, que, por isso, o matou e transferiu o reino a Davi, filho de Jessé.*
1 Então, todo o Israel se ajuntou a Davi, em Hebrom, dizendo: Somos do mesmo povo de que tu és.
2 Outrora, sendo Saul ainda rei, eras tu que fazias saídas e entradas militares com Israel; também o Senhor, teu Deus, te disse: Tu apascentarás o meu povo de Israel, serás chefe sobre o meu povo de Israel.
3 Assim, pois, todos os anciãos de Israel vieram ter com o rei em Hebrom; e Davi fez com eles aliança em Hebrom, perante o Senhor. Ungiram Davi rei sobre Israel, segundo a palavra do Senhor por intermédio de Samuel.
4 Partiu Davi e todo o Israel para Jerusalém, que é Jebus, porque ali estavam os jebuseus que habitavam naquela terra.
5 Disseram os moradores de Jebus a Davi: Tu não entrarás aqui. Porém Davi tomou a fortaleza de Sião; esta é a Cidade de Davi.
6 Porque disse Davi: Qualquer que primeiro ferir os jebuseus será chefe e comandante. Então, Joabe, filho de Zeruia, subiu primeiro e foi feito chefe.
7 Assim, habitou Davi na fortaleza, pelo que se chamou a Cidade de Davi.
8 E foi edificando a cidade em redor, desde Milo, completando o circuito; e Joabe renovou o resto da cidade.
9 Ia Davi crescendo em poder cada vez mais, porque o Senhor dos Exércitos era com ele.
10 São estes os principais valentes de Davi, que o apoiaram valorosamente no seu reino, com todo o Israel, para o fazerem rei, segundo a palavra do Senhor, no tocante a esse povo.
11 Eis a lista dos valentes de Davi: Jasobeão, hacmonita, o principal dos trinta, o qual, brandindo a sua lança contra trezentos, de uma vez os feriu.
12 Depois dele, Eleazar, filho de Dodô, o aoíta; ele estava entre os três valentes.
13 Este se achou com Davi em Pas-Damim, quando se ajuntaram ali os filisteus à peleja, onde havia um pedaço de terra cheio de cevada; e o povo fugiu de diante dos filisteus.
14 Puseram-se no meio daquele terreno, e o defenderam, e feriram os filisteus; e o Senhor efetuou grande livramento.
15 Três dos trinta cabeças desceram à penha, indo ter com Davi à caverna de Adulão; e o exército dos filisteus se acampara no vale dos Refains.
16 Davi estava na fortaleza, e a guarnição dos filisteus, em Belém.
17 Suspirou Davi e disse: Quem me dera beber água do poço que está junto à porta de Belém!
18 Então, aqueles três romperam pelo acampamento dos filisteus, e tiraram água do poço junto à porta de Belém, e tomaram-na, e a levaram a Davi; ele não a quis beber, mas a derramou como libação ao Senhor.
19 E disse: Longe de mim, ó meu Deus, fazer tal coisa; beberia eu o sangue dos homens que lá foram com perigo de sua vida? Pois, com perigo de sua vida, a trouxeram. De maneira que não a quis beber. São essas as coisas que fizeram os três valentes.
20 Também Abisai, irmão de Joabe, era cabeça dos trinta, o qual, brandindo a sua lança contra trezentos, os feriu; e tinha nome entre os primeiros três.
21 Era ele mais nobre do que os trinta e era o cabeça deles; contudo, aos primeiros três não chegou.
22 Também Benaia, filho de Joiada, era homem valente de Cabzeel e grande em obras; feriu ele dois heróis de Moabe. Desceu numa cova e nela matou um leão no tempo da neve.
23 Matou também um egípcio, homem da estatura de cinco côvados; o egípcio trazia na mão uma lança como o eixo do tecelão, mas Benaia o atacou com um cajado, arrancou-lhe da mão a lança e com ela o matou.
24 Estas coisas fez Benaia, filho de Joiada, pelo que teve nome entre os primeiros três valentes.
25 Era mais nobre do que os trinta, porém aos três primeiros não chegou, e Davi o pôs sobre a sua guarda.
26 Foram os heróis dos exércitos: Asael, irmão de Joabe, Elanã, filho de Dodô, de Belém;
27 Samote, harorita; Heles, pelonita;
28 Ira, filho de Iques, tecoíta; Abiezer, anatotita;
29 Sibecai, husatita; Ilai, aoíta;
30 Maarai, netofatita; Helede, filho de Baaná, netofatita;
31 Itai, filho de Ribai, de Gibeá, dos filhos de Benjamim; Benaia, piratonita;
32 Hurai, do ribeiro de Gaás; Abiel, arbatita;
33 Azmavete, baarumita; Eliaba, saalbonita;
34 Benê-Hasém, gizonita; Jônatas, filho de Sage, hararita;
35 Aião, filho de Sacar, hararita; Elifal, filho de Ur;
36 Héfer, mequeratita; Aías, pelonita;
37 Hezro, carmelita; Naarai, filho de Ezbai;
38 Joel, irmão de Natã; Mibar, filho de Hagri;
39 Zeleque, amonita; Naarai, beerotita, o que trazia as armas de Joabe, filho de Zeruia;
40 Ira, o itrita; Garebe, itrita;
41 Urias, heteu; Zabade, filho de Alai;
42 Adina, filho de Siza, rubenita, chefe dos rubenitas, e com ele trinta;
43 Hanã, filho de Maaca; Josafá, mitenita;
44 Uzias, asteratita, Sama e Jeiel, filhos de Hotão, aroerita;
45 Jediael, filho de Sinri, e Joá, seu irmão, tizita;
46 Eliel, maavita, Jeribai e Josavias, filhos de Elnaão; Itma, moabita;
47 Eliel, Obede e Jaasiel, de Zoba.*
1 São estes os que vieram a Davi, a Ziclague, quando fugitivo de Saul, filho de Quis; e eram dos valentes que o ajudavam na guerra.
2 Tinham por arma o arco e usavam tanto da mão direita como da esquerda em arremessar pedras com fundas e em atirar flechas com o arco. Eram dos irmãos de Saul, da tribo de Benjamim:
3 Aiezer, o chefe, e Joás, filhos de Semaá, o gibeatita; Jeziel e Pelete, filhos de Azmavete; Beraca e Jeú, o anatotita;
4 Ismaías, o gibeonita, valente entre os trinta e cabeça deles; Jeremias, Jaaziel, Joanã e Jozabade, o gederatita;
5 Eluzai, Jerimote, Bealias, Semarias e Sefatias, o harufita;
6 Elcana, Issias, Azarel, Joezer e Jasobeão, os coreítas;
7 Joela, Zebadias, filhos de Jeroão, de Gedor.
8 Dos gaditas passaram-se para Davi à fortaleza no deserto, homens valentes, homens de guerra para pelejar, armados de escudo e lança; seu rosto era como de leões, e eram eles ligeiros como gazelas sobre os montes:
9 Ézer, o cabeça, Obadias, o segundo, Eliabe, o terceiro,
10 Mismana, o quarto, Jeremias, o quinto,
11 Atai, o sexto, Eliel, o sétimo,
12 Joanã, o oitavo, Elzabade, o nono,
13 Jeremias, o décimo, Macbanai, o undécimo;
14 estes, dos filhos de Gade, foram capitães do exército; o menor valia por cem homens, e o maior, por mil.
15 São estes os que passaram o Jordão no primeiro mês, quando ele transbordava por todas as suas ribanceiras, e puseram em fuga a todos os que habitavam nos vales, tanto no oriente como no ocidente.
16 Também vieram alguns dos filhos de Benjamim e de Judá a Davi, à fortaleza.
17 Davi lhes saiu ao encontro e lhes falou, dizendo: Se vós vindes a mim pacificamente e para me ajudar, o meu coração se unirá convosco; porém, se é para me entregardes aos meus adversários, não havendo maldade em mim, o Deus de nossos pais o veja e o repreenda.
18 Então, entrou o Espírito em Amasai, cabeça de trinta, e disse: Nós somos teus, ó Davi, e contigo estamos, ó filho de Jessé! Paz, paz seja contigo! E paz com os que te ajudam! Porque o teu Deus te ajuda. Davi os recebeu e os fez capitães de tropas.
19 Também de Manassés alguns se passaram para Davi, quando veio com os filisteus para a batalha contra Saul, mas não ajudou os filisteus, porque os príncipes destes, depois de se aconselharem, o despediram; pois diziam: À custa de nossa cabeça, passará a Saul, seu senhor.
20 Voltando ele, pois, a Ziclague, passaram-se para ele, de Manassés, Adna, Jozabade, Jediael, Micael, Jozabade, Eliú e Ziletai, chefes de milhares dos de Manassés.
21 Estes ajudaram Davi contra aquela tropa, porque todos eles eram homens valentes e capitães no exército.
22 Porque, naquele tempo, dia após dia, vinham a Davi para o ajudar, até que se fez um grande exército, como exército de Deus.
23 Ora, este é o número dos homens armados para a peleja, que vieram a Davi, em Hebrom, para lhe transferirem o reino de Saul, segundo a palavra do Senhor:
24 dos filhos de Judá, que traziam escudo e lança, seis mil e oitocentos, armados para a peleja;
25 dos filhos de Simeão, homens valentes para a peleja, sete mil e cem;
26 dos filhos de Levi, quatro mil e seiscentos;
27 Joiada era o chefe da casa de Arão, e com ele vieram três mil e setecentos;
28 Zadoque, sendo ainda jovem, homem valente, trouxe vinte e dois príncipes de sua casa paterna;
29 dos filhos de Benjamim, irmãos de Saul, vieram três mil; porque até então havia ainda muitos deles que eram pela casa de Saul;
30 dos filhos de Efraim, vinte mil e oitocentos homens valentes e de renome em casa de seus pais;
31 da meia tribo de Manassés, dezoito mil, que foram apontados nominalmente para vir a fazer rei a Davi;
32 dos filhos de Issacar, conhecedores da época, para saberem o que Israel devia fazer, duzentos chefes e todos os seus irmãos sob suas ordens;
33 de Zebulom, dos capazes para sair à guerra, providos com todas as armas de guerra, cinquenta mil, destros para ordenar uma batalha com ânimo resoluto;
34 de Naftali, mil capitães, e, com eles, trinta e sete mil com escudo e lança;
35 dos danitas, providos para a peleja, vinte e oito mil e seiscentos;
36 de Aser, dos capazes para sair à guerra e prontos para a batalha, quarenta mil;
37 do lado dalém do Jordão, dos rubenitas e gaditas e da meia tribo de Manassés, providos de toda sorte de instrumentos de guerra, cento e vinte mil.
38 Todos estes homens de guerra, postos em ordem de batalha, vieram a Hebrom, resolvidos a fazer Davi rei sobre todo o Israel; também todo o resto de Israel era unânime no propósito de fazer a Davi rei.
39 Estiveram ali com Davi três dias, comendo e bebendo; porque seus irmãos lhes tinham feito provisões.
40 E também seus vizinhos de mais perto, até Issacar, Zebulom e Naftali, trouxeram pão sobre jumentos, sobre camelos, sobre mulos e sobre bois, provisões de farinha, e pastas de figos, e cachos de passas, e vinho, e azeite, e bois, e gado miúdo em abundância; porque havia regozijo em Israel.*
1 Consultou Davi os capitães de mil, e os de cem, e todos os príncipes;
2 e disse a toda a congregação de Israel: Se bem vos parece, e se vem isso do Senhor, nosso Deus, enviemos depressa mensageiros a todos os nossos outros irmãos em todas as terras de Israel, e aos sacerdotes, e aos levitas com eles nas cidades e nos seus arredores, para que se reúnam conosco;
3 tornemos a trazer para nós a arca do nosso Deus; porque nos dias de Saul não nos valemos dela.
4 Então, toda a congregação concordou em que assim se fizesse; porque isso pareceu justo aos olhos de todo o povo.
5 Reuniu, pois, Davi a todo o Israel, desde Sior do Egito até à entrada de Hamate, para trazer a arca de Deus de Quiriate-Jearim.
6 Então, Davi, com todo o Israel, subiu a Baalá, isto é, a Quiriate-Jearim, que está em Judá, para fazer subir dali a arca de Deus, diante da qual é invocado o nome do Senhor, que se assenta acima dos querubins.
7 Puseram a arca de Deus num carro novo e a levaram da casa de Abinadabe; e Uzá e Aiô guiavam o carro.
8 Davi e todo o Israel alegravam-se perante Deus, com todo o seu empenho; em cânticos, com harpas, com alaúdes, com tamboris, com címbalos e com trombetas.
9 Quando chegaram à eira de Quidom, estendeu Uzá a mão à arca para a segurar, porque os bois tropeçaram.
10 Então, a ira do Senhor se acendeu contra Uzá e o feriu, por ter estendido a mão à arca; e morreu ali perante Deus.
11 Desgostou-se Davi, porque o Senhor irrompera contra Uzá; pelo que chamou àquele lugar Perez-Uzá, até ao dia de hoje.
12 Temeu Davi a Deus, naquele dia, e disse: Como trarei a mim a arca de Deus?
13 Pelo que Davi não trouxe a arca para si, para a Cidade de Davi; mas a fez levar à casa de Obede-Edom, o geteu.
14 Assim, ficou a arca de Deus com a família de Obede-Edom, três meses em sua casa; e o Senhor abençoou a casa de Obede-Edom e tudo o que ele tinha.*
1 Então, Hirão, rei de Tiro, mandou mensageiros a Davi, e madeira de cedro, e pedreiros, e carpinteiros, para lhe edificarem uma casa.
2 Reconheceu Davi que o Senhor o confirmara rei sobre Israel; porque, por amor do seu povo de Israel, o seu reino se tinha exaltado muito.
3 Davi tomou ainda mais mulheres em Jerusalém; e gerou ainda mais filhos e filhas.
4 São estes os nomes dos filhos que teve em Jerusalém: Samua, Sobabe, Natã, Salomão,
5 Ibar, Elisua, Elpelete,
6 Nogá, Nefegue, Jafia,
7 Elisama, Beeliada e Elifelete.
8 Ouvindo, pois, os filisteus que Davi fora ungido rei sobre todo o Israel, subiram todos para prender Davi; ouvindo-o Davi, saiu contra eles.
9 Mas vieram os filisteus e investiram contra ele no vale dos Refains.
10 Então, Davi consultou a Deus, dizendo: Subirei contra os filisteus? Entregar-mos-ás nas mãos? Respondeu-lhe o Senhor: Sobe, porque os entregarei nas tuas mãos.
11 Subindo Davi a Baal-Perazim, ali os derrotou; e disse: Deus, por meu intermédio, rompeu as fileiras inimigas diante de mim, como quem rompe águas. Por isso, chamaram o nome daquele lugar Baal-Perazim.
12 Ali, deixaram os seus deuses; e ordenou Davi que se queimassem.
13 Porém os filisteus tornaram e fizeram uma investida no vale.
14 De novo, Davi consultou a Deus, e este lhe respondeu: Não subirás após eles; mas rodeia por detrás deles e ataca-os por defronte das amoreiras;
15 e há de ser que, ouvindo tu um estrondo de marcha pelas copas das amoreiras, então, sai à peleja; porque Deus saiu adiante de ti a ferir o exército dos filisteus.
16 Fez Davi como Deus lhe ordenara; e feriu o exército dos filisteus desde Gibeão até Gezer.
17 Assim se espalhou o renome de Davi por todas aquelas terras; pois o Senhor o fez temível a todas aquelas gentes.*
1 Fez também Davi casas para si mesmo, na Cidade de Davi; e preparou um lugar para a arca de Deus e lhe armou uma tenda.
2 Então, disse Davi: Ninguém pode levar a arca de Deus, senão os levitas; porque o Senhor os elegeu, para levarem a arca de Deus e o servirem para sempre.
3 Davi reuniu a todo o Israel em Jerusalém, para fazerem subir a arca do Senhor ao seu lugar, que lhe tinha preparado.
4 Reuniu Davi os filhos de Arão e os levitas:
5 dos filhos de Coate: Uriel, o chefe, e seus irmãos, cento e vinte;
6 dos filhos de Merari: Asaías, o chefe, e seus irmãos, duzentos e vinte;
7 dos filhos de Gérson: Joel, o chefe, e seus irmãos, cento e trinta;
8 dos filhos de Elisafã: Semaías, o chefe, e seus irmãos, duzentos;
9 dos filhos de Hebrom: Eliel, o chefe, e seus irmãos, oitenta;
10 dos filhos de Uziel: Aminadabe, o chefe, e seus irmãos, cento e doze.
11 Chamou Davi os sacerdotes Zadoque e Abiatar e os levitas Uriel, Asaías, Joel, Semaías, Eliel e Aminadabe
12 e lhes disse: Vós sois os cabeças das famílias dos levitas; santificai-vos, vós e vossos irmãos, para que façais subir a arca do Senhor, Deus de Israel, ao lugar que lhe preparei.
13 Pois, visto que não a levastes na primeira vez, o Senhor, nosso Deus, irrompeu contra nós, porque, então, não o buscamos, segundo nos fora ordenado.
14 Santificaram-se, pois, os sacerdotes e levitas, para fazerem subir a arca do Senhor, Deus de Israel.
15 Os filhos dos levitas trouxeram a arca de Deus aos ombros pelas varas que nela estavam, como Moisés tinha ordenado, segundo a palavra do Senhor.
16 Disse Davi aos chefes dos levitas que constituíssem a seus irmãos, os cantores, para que, com instrumentos músicos, com alaúdes, harpas e címbalos se fizessem ouvir e levantassem a voz com alegria.
17 Designaram, pois, os levitas Hemã, filho de Joel; e dos irmãos dele, Asafe, filho de Berequias; e dos filhos de Merari, irmãos deles, Etã, filho de Cusaías.
18 E com eles a seus irmãos da segunda ordem: Zacarias, Bene, Jaaziel, Semiramote, Jeiel, Uni, Eliabe, Benaia, Maaseias, Matitias, Elifeleu e Micneias e os porteiros Obede-Edom e Jeiel.
19 Assim, os cantores Hemã, Asafe e Etã se faziam ouvir com címbalos de bronze;
20 Zacarias, Aziel, Semiramote, Jeiel, Uni, Eliabe, Maaseias e Benaia, com alaúdes, em voz de soprano;
21 Matitias, Elifeleu, Micneias, Obede-Edom, Jeiel e Azazias, com harpas, em voz de baixo, para conduzir o canto.
22 Quenanias, chefe dos levitas músicos, tinha o encargo de dirigir o canto, porque era perito nisso.
23 Berequias e Elcana eram porteiros da arca.
24 Sebanias, Josafá, Natanael, Amasai, Zacarias, Benaia e Eliézer, os sacerdotes, tocavam as trombetas perante a arca de Deus; Obede-Edom e Jeías eram porteiros da arca.
25 Foram Davi, e os anciãos de Israel, e os capitães de milhares, para fazerem subir, com alegria, a arca da Aliança do Senhor, da casa de Obede-Edom.
26 Tendo Deus ajudado os levitas que levavam a arca da Aliança do Senhor, ofereceram em sacrifício sete novilhos e sete carneiros.
27 Davi ia vestido de um manto de linho fino, como também todos os levitas que levavam a arca, e os cantores, e Quenanias, chefe dos que levavam a arca e dos cantores; Davi vestia também uma estola sacerdotal de linho.
28 Assim, todo o Israel fez subir com júbilo a arca da Aliança do Senhor, ao som de clarins, de trombetas e de címbalos, fazendo ressoar alaúdes e harpas.
29 Ao entrar a arca da Aliança do Senhor na Cidade de Davi, Mical, filha de Saul, estava olhando pela janela e, vendo ao rei Davi dançando e folgando, o desprezou no seu coração.*
1 Introduziram, pois, a arca de Deus e a puseram no meio da tenda que lhe armara Davi; e trouxeram holocaustos e ofertas pacíficas perante Deus.
2 Tendo Davi acabado de trazer os holocaustos e ofertas pacíficas, abençoou o povo em nome do Senhor.
3 E repartiu a todos em Israel, tanto os homens como as mulheres, a cada um, um bolo de pão, um bom pedaço de carne e passas.
4 Designou dentre os levitas os que haviam de ministrar diante da arca do Senhor, e celebrar, e louvar, e exaltar o Senhor, Deus de Israel, a saber,
5 Asafe, o chefe, Zacarias, o segundo, e depois Jeiel, Semiramote, Jeiel, Matitias, Eliabe, Benaia, Obede-Edom e Jeiel, com alaúdes e harpas; e Asafe fazia ressoar os címbalos.
6 Os sacerdotes Benaia e Jaaziel estavam continuamente com trombetas, perante a arca da Aliança de Deus.
7 Naquele dia, foi que Davi encarregou, pela primeira vez, a Asafe e a seus irmãos de celebrarem com hinos o Senhor.
8 Rendei graças ao Senhor, invocai o seu nome, fazei conhecidos, entre os povos, os seus feitos.
9 Cantai-lhe, cantai-lhe salmos; narrai todas as suas maravilhas.
10 Gloriai-vos no seu santo nome; alegre-se o coração dos que buscam o Senhor.
11 Buscai o Senhor e o seu poder, buscai perpetuamente a sua presença.
12 Lembrai-vos das maravilhas que fez, dos seus prodígios e dos juízos dos seus lábios,
13 vós, descendentes de Israel, seu servo, vós, filhos de Jacó, seus escolhidos.
14 Ele é o Senhor, nosso Deus; os seus juízos permeiam toda a terra.
15 Lembra-se perpetuamente da sua aliança, da palavra que empenhou para mil gerações;
16 da aliança que fez com Abraão e do juramento que fez a Isaque;
17 o qual confirmou a Jacó por decreto e a Israel, por aliança perpétua,
18 dizendo: Dar-vos-ei a terra de Canaã como quinhão da vossa herança.
19 Então, eram eles em pequeno número, pouquíssimos e forasteiros nela;
20 andavam de nação em nação, de um reino para um povo.
21 A ninguém permitiu que os oprimisse; antes, por amor deles, repreendeu a reis,
22 dizendo: Não toqueis nos meus ungidos, nem maltrateis os meus profetas.
23 Cantai ao Senhor, todas as terras; proclamai a sua salvação, dia após dia.
24 Anunciai entre as nações a sua glória, entre todos os povos, as suas maravilhas,
25 porque grande é o Senhor e mui digno de ser louvado, temível mais do que todos os deuses.
26 Porque todos os deuses dos povos são ídolos; o Senhor, porém, fez os céus.
27 Glória e majestade estão diante dele, força e formosura, no seu santuário.
28 Tributai ao Senhor, ó famílias dos povos, tributai ao Senhor glória e força.
29 Tributai ao Senhor a glória devida ao seu nome; trazei oferendas e entrai nos seus átrios; adorai o Senhor na beleza da sua santidade.
30 Tremei diante dele, todas as terras, pois ele firmou o mundo para que não se abale.
31 Alegrem-se os céus, e a terra exulte; diga-se entre as nações: Reina o Senhor.
32 Ruja o mar e a sua plenitude; folgue o campo e tudo o que nele há.
33 Regozijem-se as árvores do bosque na presença do Senhor, porque vem a julgar a terra.
34 Rendei graças ao Senhor, porque ele é bom; porque a sua misericórdia dura para sempre.
35 E dizei: Salva-nos, ó Deus da nossa salvação, ajunta-nos e livra-nos das nações, para que rendamos graças ao teu santo nome e nos gloriemos no teu louvor.
36 Bendito seja o Senhor, Deus de Israel, desde a eternidade até a eternidade. E todo o povo disse: Amém! E louvou ao Senhor.
37 Então, Davi deixou ali diante da arca da Aliança do Senhor a Asafe e a seus irmãos, para ministrarem continuamente perante ela, segundo se ordenara para cada dia;
38 também deixou a Obede-Edom com seus irmãos, em número de sessenta e oito; a Obede-Edom, filho de Jedutum, e a Hosa, para serem porteiros;
39 e deixou a Zadoque, o sacerdote, e aos sacerdotes, seus irmãos, diante do tabernáculo do Senhor, num lugar alto de Gibeão,
40 para oferecerem continuamente ao Senhor os holocaustos sobre o altar dos holocaustos, pela manhã e à tarde; e isto segundo tudo o que está escrito na Lei que o Senhor ordenara a Israel.
41 E com eles deixou a Hemã, a Jedutum e os mais escolhidos, que foram nominalmente designados para louvarem o Senhor, porque a sua misericórdia dura para sempre.
42 Com eles, pois, estavam Hemã e Jedutum, que faziam ressoar trombetas, e címbalos, e instrumentos de música de Deus; os filhos de Jedutum eram porteiros.
43 Então, se retirou todo o povo, cada um para sua casa; e tornou Davi, para abençoar a sua casa.*
1 Sucedeu que, habitando Davi em sua própria casa, disse ao profeta Natã: Eis que moro em casa de cedros, mas a arca da Aliança do Senhor se acha numa tenda.
2 Então, Natã disse a Davi: Faze tudo quanto está no teu coração, porque Deus é contigo.
3 Porém, naquela mesma noite, veio a palavra do Senhor a Natã, dizendo:
4 Vai e dize a meu servo Davi: Assim diz o Senhor: Tu não edificarás casa para minha habitação;
5 porque em casa nenhuma habitei, desde o dia que fiz subir a Israel até ao dia de hoje; mas tenho andado de tenda em tenda, de tabernáculo em tabernáculo.
6 Em todo lugar em que andei com todo o Israel, falei, acaso, alguma palavra com algum dos seus juízes, a quem mandei apascentar o meu povo, dizendo: Por que não me edificais uma casa de cedro?
7 Agora, pois, assim dirás ao meu servo Davi: Assim diz o Senhor dos Exércitos: Tomei-te da malhada e de detrás das ovelhas, para que fosses príncipe sobre o meu povo de Israel.
8 E fui contigo, por onde quer que andaste, eliminei os teus inimigos de diante de ti e fiz grande o teu nome, como só os grandes têm na terra.
9 Prepararei lugar para o meu povo de Israel e o plantarei para que habite no seu lugar e não mais seja perturbado; e jamais os filhos da perversidade o oprimam, como dantes,
10 desde o dia em que mandei houvesse juízes sobre o meu povo de Israel; porém abati todos os teus inimigos e também te fiz saber que o Senhor te edificaria uma casa.
11 Há de ser que, quando teus dias se cumprirem, e tiveres de ir para junto de teus pais, então, farei levantar depois de ti o teu descendente, que será dos teus filhos, e estabelecerei o seu reino.
12 Esse me edificará casa; e eu estabelecerei o seu trono para sempre.
13 Eu lhe serei por pai, e ele me será por filho; a minha misericórdia não apartarei dele, como a retirei daquele que foi antes de ti.
14 Mas o confirmarei na minha casa e no meu reino para sempre, e o seu trono será estabelecido para sempre.
15 Segundo todas estas palavras e conforme toda esta visão, assim falou Natã a Davi.
16 Então, entrou o rei Davi na Casa do Senhor, ficou perante ele e disse: Quem sou eu, Senhor Deus, e qual é a minha casa, para que me tenhas trazido até aqui?
17 Foi isso ainda pouco aos teus olhos, ó Deus, de maneira que também falaste a respeito da casa de teu servo para tempos distantes; e me trataste como se eu fosse homem ilustre, ó Senhor Deus.
18 Que mais ainda te poderá dizer Davi acerca das honras feitas a teu servo? Pois tu conheces bem teu servo.
19 Ó Senhor, por amor de teu servo e segundo o teu coração, fizeste toda esta grandeza, para tornar notórias todas estas grandes coisas!
20 Senhor, ninguém há semelhante a ti, e não há outro Deus além de ti, segundo tudo o que nós mesmos temos ouvido.
21 Quem há como o teu povo de Israel, gente única na terra, a quem tu, ó Deus, foste resgatar para ser teu povo e fazer a ti mesmo um nome, com estas grandes e tremendas coisas, desterrando as nações de diante do teu povo, que remiste do Egito?
22 Estabeleceste a teu povo de Israel por teu povo, para sempre, e tu, ó Senhor, te fizeste o seu Deus.
23 Agora, pois, ó Senhor, a palavra que disseste acerca de teu servo e acerca da sua casa, seja estabelecida para sempre; e faze como falaste.
24 Estabeleça-se, e seja para sempre engrandecido o teu nome, e diga-se: O Senhor dos Exércitos é o Deus de Israel, é Deus para Israel; e a casa de Davi, teu servo, será estabelecida diante de ti.
25 Pois tu, Deus meu, fizeste ao teu servo a revelação de que lhe edificarias casa. Por isso, o teu servo se animou para fazer-te esta oração.
26 Agora, pois, ó Senhor, tu mesmo és Deus e prometeste a teu servo este bem.
27 Sê, pois, agora, servido de abençoar a casa de teu servo, a fim de permanecer para sempre diante de ti, pois tu, ó Senhor, a abençoaste, e abençoada será para sempre.*
1 Depois disto, feriu Davi os filisteus e os humilhou; tomou a Gate e suas aldeias das mãos dos filisteus.
2 Também derrotou os moabitas, e assim ficaram por servos de Davi e lhe pagavam tributo.
3 Também Hadadezer, rei de Zoba, foi derrotado por Davi, até Hamate, quando aquele foi restabelecer o seu domínio sobre o rio Eufrates.
4 Tomou-lhe Davi mil carros, sete mil cavaleiros e vinte mil homens de pé; Davi jarretou a todos os cavalos dos carros, menos para cem deles.
5 Vieram os siros de Damasco a socorrer a Hadadezer, rei de Zoba; porém Davi matou dos siros vinte e dois mil homens.
6 Davi pôs guarnições na Síria de Damasco, e os siros ficaram por servos de Davi e lhe pagavam tributo; e o Senhor dava vitórias a Davi, por onde quer que ia.
7 Tomou Davi os escudos de ouro que havia com os oficiais de Hadadezer e os trouxe a Jerusalém.
8 Também de Tibate e de Cum, cidades de Hadadezer, tomou Davi mui grande quantidade de bronze, de que Salomão fez o mar de bronze, as colunas e os utensílios de bronze.
9 Ouvindo Toú, rei de Hamate, que Davi derrotara a todo o exército de Hadadezer, rei de Zoba,
10 mandou seu filho Hadorão ao rei Davi, para o saudar e congratular-se com ele por haver pelejado contra Hadadezer e por havê-lo ferido (porque Hadadezer fazia guerra a Toú). Hadorão trouxe consigo objetos de ouro, de prata e de bronze,
11 os quais também o rei Davi consagrou ao Senhor, juntamente com a prata e ouro que trouxera de todas as mais nações: de Edom, de Moabe, dos filhos de Amom, dos filisteus e de Amaleque.
12 Também Abisai, filho de Zeruia, feriu a dezoito mil edomitas no vale do Sal.
13 E pôs guarnições em Edom, e todos os edomitas ficaram por servos de Davi; e o Senhor dava vitórias a Davi, por onde quer que ia.
14 Reinou, pois, Davi sobre todo o Israel; julgava e fazia justiça a todo o seu povo.
15 Joabe, filho de Zeruia, era comandante do exército; Josafá, filho de Ailude, era cronista.
16 Zadoque, filho de Aitube, e Abimeleque, filho de Abiatar, eram sacerdotes; e Sausa, escrivão.
17 Benaia, filho de Joiada, era o comandante da guarda real. Os filhos de Davi, porém, eram os primeiros ao lado do rei.*
1 Depois disto, morreu Naás, rei dos filhos de Amom; e seu filho reinou em seu lugar.
2 Então, disse Davi: Usarei de bondade para com Hanum, filho de Naás, porque seu pai usou de bondade para comigo. Pelo que Davi enviou mensageiros para o consolar acerca de seu pai; e vieram os servos de Davi à terra dos filhos de Amom, a Hanum, para o consolarem.
3 Disseram os príncipes dos filhos de Amom a Hanum: Pensas que, por te haver Davi mandado consoladores, está honrando a teu pai? Não vieram seus servos a ti para reconhecerem, destruírem e espiarem a terra?
4 Tomou, então, Hanum os servos de Davi, e rapou-os, e lhes cortou metade das vestes até às nádegas, e os despediu.
5 Foram-se alguns e avisaram a Davi acerca destes homens; então, enviou mensageiros a encontrá-los, porque estavam sobremaneira envergonhados. Mandou o rei dizer-lhes: Deixai-vos estar em Jericó, até que vos torne a crescer a barba; e, então, vinde.
6 Vendo, pois, os filhos de Amom que se haviam tornado odiosos a Davi, então, Hanum e os filhos de Amom tomaram mil talentos de prata, para alugarem para si carros e cavaleiros da Mesopotâmia, e dos siros de Maaca, e de Zoba.
7 Alugaram para si trinta e dois mil carros, o rei de Maaca e a sua gente, e eles vieram e se acamparam diante de Medeba; também os filhos de Amom se ajuntaram das suas cidades e vieram para a guerra.
8 O que ouvindo Davi, enviou contra eles a Joabe com todo o exército dos valentes.
9 Saíram os filhos de Amom e ordenaram a batalha à entrada da porta da cidade; porém os reis que vieram estavam à parte, no campo.
10 Vendo, pois, Joabe que estava preparada contra ele a batalha, tanto pela frente como pela retaguarda, escolheu dentre todos o que havia de melhor em Israel e os formou em linha contra os siros;
11 e o resto do povo entregou a Abisai, seu irmão, e puseram-se em linha contra os filhos de Amom.
12 Disse Joabe: Se os siros forem mais fortes do que eu, tu me virás em socorro; e, se os filhos de Amom forem mais fortes do que tu, eu irei ao teu socorro.
13 Sê forte, pois; pelejemos varonilmente pelo nosso povo e pelas cidades de nosso Deus; e faça o Senhor o que bem lhe parecer.
14 Então, avançou Joabe com o povo que estava com ele, e travaram peleja contra os siros; e estes fugiram de diante dele.
15 Vendo os filhos de Amom que os siros fugiam, também eles fugiram de diante de Abisai, irmão de Joabe, e entraram na cidade; voltou Joabe dos filhos de Amom e tornou a Jerusalém.
16 Vendo, pois, os siros que tinham sido desbaratados diante de Israel, enviaram mensageiros e fizeram sair os siros que habitavam do lado dalém do rio; Sofaque, capitão do exército de Hadadezer, marchava adiante deles.
17 Informado Davi, ajuntou a todo o Israel, passou o Jordão, veio ter com eles e ordenou contra eles a batalha; e, tendo Davi ordenado a batalha contra os siros, pelejaram estes contra ele.
18 Porém os siros fugiram de diante de Israel, e Davi matou dentre os siros os homens de sete mil carros e quarenta mil homens de pé; a Sofaque, chefe do exército, matou.
19 Vendo, pois, os servos de Hadadezer que foram feridos diante de Israel, fizeram paz com Davi e o serviram; e os siros nunca mais quiseram socorrer aos filhos de Amom.*
1 Decorrido um ano, no tempo em que os reis costumam sair para a guerra, Joabe levou o exército, destruiu a terra dos filhos de Amom, veio e sitiou a Rabá; porém Davi ficou em Jerusalém; e Joabe feriu a Rabá e a destruiu.
2 Tirou Davi a coroa da cabeça do seu rei e verificou que tinha o peso de um talento de ouro e que havia nela pedras preciosas; e foi posta na cabeça de Davi; e da cidade levou mui grande despojo.
3 Também levou o povo que estava nela e o fez passar à serra, e a picaretas de ferro, e a machados; assim fez Davi a todas as cidades dos filhos de Amom. Voltou Davi, com todo o povo, para Jerusalém.
4 Depois disto, houve guerra em Gezer contra os filisteus; então, Sibecai, o husatita, feriu a Sipai, que era descendente dos gigantes; e os filisteus foram subjugados.
5 Houve ainda outra guerra contra os filisteus; e Elanã, filho de Jair, feriu a Lami, irmão de Golias, o geteu, cuja lança tinha a haste como eixo de tecelão.
6 Houve ainda outra guerra em Gate; havia ali um homem de grande estatura, tinha vinte e quatro dedos, seis em cada mão e seis em cada pé; também este descendia dos gigantes.
7 Quando ele injuriava a Israel, Jônatas, filho de Simeia, irmão de Davi, o feriu.
8 Estes nasceram dos gigantes em Gate; e caíram pela mão de Davi e pela mão de seus homens.*
1 Então, Satanás se levantou contra Israel e incitou a Davi a levantar o censo de Israel.
2 Disse Davi a Joabe e aos chefes do povo: Ide, levantai o censo de Israel, desde Berseba até Dã; e trazei-me a apuração para que eu saiba o seu número.
3 Então, disse Joabe: Multiplique o Senhor, teu Deus, a este povo cem vezes mais; porventura, ó rei, meu senhor, não são todos servos de meu senhor? Por que requer isso o meu senhor? Por que trazer, assim, culpa sobre Israel?
4 Porém a palavra do rei prevaleceu contra Joabe; pelo que saiu Joabe e percorreu todo o Israel; então, voltou para Jerusalém.
5 Deu Joabe a Davi o recenseamento do povo; havia em Israel um milhão e cem mil homens que puxavam da espada; e em Judá eram quatrocentos e setenta mil homens que puxavam da espada.
6 Porém os de Levi e Benjamim não foram contados entre eles, porque a ordem do rei foi abominável a Joabe.
7 Tudo isto desagradou a Deus, pelo que feriu a Israel.
8 Então, disse Davi a Deus: Muito pequei em fazer tal coisa; porém, agora, peço-te que perdoes a iniquidade de teu servo, porque procedi mui loucamente.
9 Falou, pois, o Senhor a Gade, o vidente de Davi, dizendo:
10 Vai e dize a Davi: Assim diz o Senhor: Três coisas te ofereço; escolhe uma delas, para que ta faça.
11 Veio, pois, Gade a Davi e lhe disse: Assim diz o Senhor: Escolhe o que queres:
12 ou três anos de fome, ou que por três meses sejas consumido diante dos teus adversários, e a espada de teus inimigos te alcance, ou que por três dias a espada do Senhor, isto é, a peste na terra, e o Anjo do Senhor causem destruição em todos os territórios de Israel; vê, pois, agora, que resposta hei de dar ao que me enviou.
13 Então, disse Davi a Gade: Estou em grande angústia; caia eu, pois, nas mãos do Senhor, porque são muitíssimas as suas misericórdias, mas nas mãos dos homens não caia eu.
14 Então, enviou o Senhor a peste a Israel; e caíram de Israel setenta mil homens.
15 Enviou Deus um anjo a Jerusalém, para a destruir; ao destruí-la, olhou o Senhor, e se arrependeu do mal, e disse ao anjo destruidor: Basta, retira, agora, a mão. O Anjo do Senhor estava junto à eira de Ornã, o jebuseu.
16 Levantando Davi os olhos, viu o Anjo do Senhor, que estava entre a terra e o céu, com a espada desembainhada na mão estendida contra Jerusalém; então, Davi e os anciãos, cobertos de panos de saco, se prostraram com o rosto em terra.
17 Disse Davi a Deus: Não sou eu o que disse que se contasse o povo? Eu é que pequei, eu é que fiz muito mal; porém estas ovelhas que fizeram? Ah! Senhor, meu Deus, seja, pois, a tua mão contra mim e contra a casa de meu pai e não para castigo do teu povo.
18 Então, o Anjo do Senhor disse a Gade que mandasse Davi subir para levantar um altar ao Senhor, na eira de Ornã, o jebuseu.
19 Subiu, pois, Davi, segundo a palavra de Gade, que falara em nome do Senhor.
20 Virando-se Ornã, viu o Anjo; e esconderam-se seus quatro filhos que estavam com ele. Ora, Ornã estava debulhando trigo.
21 Quando Davi vinha chegando a Ornã, este olhou, e o viu e, saindo da eira, se inclinou diante de Davi, com o rosto em terra.
22 Disse Davi a Ornã: Dá-me este lugar da eira a fim de edificar nele um altar ao Senhor, para que cesse a praga de sobre o povo; dá-mo pelo seu devido valor.
23 Então, disse Ornã a Davi: Tome-a o rei, meu senhor, para si e faça dela o que bem lhe parecer; eis que dou os bois para o holocausto, e os trilhos, para a lenha, e o trigo, para oferta de manjares; dou tudo.
24 Tornou o rei Davi a Ornã: Não; antes, pelo seu inteiro valor a quero comprar; porque não tomarei o que é teu para o Senhor, nem oferecerei holocausto que não me custe nada.
25 Davi deu a Ornã por aquele lugar a soma de seiscentos siclos de ouro.
26 Edificou ali um altar ao Senhor, ofereceu nele holocaustos e sacrifícios pacíficos e invocou o Senhor, o qual lhe respondeu com fogo do céu sobre o altar do holocausto.
27 O Senhor deu ordem ao Anjo, e ele meteu a sua espada na bainha.
28 Vendo Davi, naquele mesmo tempo, que o Senhor lhe respondera na eira de Ornã, o jebuseu, sacrificou ali.
29 Porque o tabernáculo do Senhor, que Moisés fizera no deserto, e o altar do holocausto estavam, naquele tempo, no alto de Gibeão.
30 Davi não podia ir até lá para consultar a Deus, porque estava atemorizado por causa da espada do Anjo do Senhor.*
1 Disse Davi: Aqui, se levantará a Casa do Senhor Deus e o altar do holocausto para Israel.
2 Deu ordem Davi para que fossem ajuntados os estrangeiros que estavam na terra de Israel; e encarregou pedreiros que preparassem pedras de cantaria para se edificar a Casa de Deus.
3 Aparelhou Davi ferro em abundância, para os pregos das folhas das portas e para as junturas, como também bronze em abundância, que nem foi pesado.
4 Madeira de cedro sem conta, porque os sidônios e tírios a traziam a Davi, em grande quantidade.
5 Pois dizia Davi: Salomão, meu filho, ainda é moço e tenro, e a casa que se há de edificar para o Senhor deve ser sobremodo magnificente, para nome e glória em todas as terras; providenciarei, pois, para ela o necessário; assim, o preparou Davi em abundância, antes de sua morte.
6 Então, chamou a Salomão, seu filho, e lhe ordenou que edificasse casa ao Senhor, Deus de Israel.
7 Disse Davi a Salomão: Filho meu, tive intenção de edificar uma casa ao nome do Senhor, meu Deus.
8 Porém a mim me veio a palavra do Senhor, dizendo: Tu derramaste sangue em abundância e fizeste grandes guerras; não edificarás casa ao meu nome, porquanto muito sangue tens derramado na terra, na minha presença.
9 Eis que te nascerá um filho, que será homem sereno, porque lhe darei descanso de todos os seus inimigos em redor; portanto, Salomão será o seu nome; paz e tranquilidade darei a Israel nos seus dias.
10 Este edificará casa ao meu nome; ele me será por filho, e eu lhe serei por pai; estabelecerei para sempre o trono do seu reino sobre Israel.
11 Agora, pois, meu filho, o Senhor seja contigo, a fim de que prosperes e edifiques a Casa do Senhor, teu Deus, como ele disse a teu respeito.
12 Que o Senhor te conceda prudência e entendimento, para que, quando regeres sobre Israel, guardes a lei do Senhor, teu Deus.
13 Então, prosperarás, se cuidares em cumprir os estatutos e os juízos que o Senhor ordenou a Moisés acerca de Israel; sê forte e corajoso, não temas, não te desalentes.
14 Eis que, com penoso trabalho, preparei para a Casa do Senhor cem mil talentos de ouro e um milhão de talentos de prata, e bronze e ferro em tal abundância, que nem foram pesados; também madeira e pedras preparei, cuja quantidade podes aumentar.
15 Além disso, tens contigo trabalhadores em grande número, e canteiros, e pedreiros, e carpinteiros, e peritos em toda sorte de obra
16 de ouro, e de prata, e também de bronze, e de ferro, que se não pode contar. Dispõe-te, pois, e faze a obra, e o Senhor seja contigo!
17 Davi deu ordem a todos os príncipes de Israel que ajudassem Salomão, seu filho, dizendo:
18 Porventura, não está convosco o Senhor, vosso Deus, e não vos deu paz por todos os lados? Pois entregou nas minhas mãos os moradores desta terra, a qual está sujeita perante o Senhor e perante o seu povo.
19 Disponde, pois, agora o coração e a alma para buscardes ao Senhor, vosso Deus; disponde-vos e edificai o santuário do Senhor Deus, para que a arca da Aliança do Senhor e os utensílios sagrados de Deus sejam trazidos a esta casa, que se há de edificar ao nome do Senhor.*
1 Sendo, pois, Davi já velho e farto de dias, constituiu a seu filho Salomão rei sobre Israel.
2 Ajuntou todos os príncipes de Israel, como também os sacerdotes e levitas.
3 Foram contados os levitas de trinta anos para cima; seu número, contados um por um, foi de trinta e oito mil homens.
4 Destes, havia vinte e quatro mil para superintenderem a obra da Casa do Senhor, seis mil oficiais e juízes,
5 quatro mil porteiros e quatro mil para louvarem o Senhor com os instrumentos que Davi fez para esse mister.
6 Davi os repartiu por turnos, segundo os filhos de Levi: Gérson, Coate e Merari.
7 Filhos de Gérson: Ladã e Simei.
8 Filhos de Ladã: Jeiel, o chefe, Zetã e Joel, três.
9 Filhos de Simei: Selomite, Haziel e Harã, três; estes foram os chefes das famílias de Ladã.
10 Filhos de Simei: Jaate, Ziza, Jeús e Berias; estes foram os filhos de Simei, quatro.
11 Jaate era o chefe, Ziza, o segundo; mas Jeús e Berias não tiveram muitos filhos; pelo que estes dois foram contados por uma só família.
12 Filhos de Coate: Anrão, Isar, Hebrom e Uziel, quatro.
13 Filhos de Anrão: Arão e Moisés; Arão foi separado para servir no Santo dos Santos, ele e seus filhos, perpetuamente, e para queimar incenso diante do Senhor, para o servir e para dar a bênção em seu nome, eternamente.
14 Quanto a Moisés, homem de Deus, seus filhos foram contados entre a tribo de Levi.
15 Os filhos de Moisés: Gérson e Eliézer.
16 Filho de Gérson: Sebuel, o chefe.
17 Filho de Eliézer: Reabias, o chefe; e não teve outros; porém os filhos de Reabias se multiplicaram grandemente.
18 Filhos de Isar: Selomite, o chefe.
19 Filhos de Hebrom: Jerias, o chefe, Amarias, o segundo, Jaaziel, o terceiro, e Jecameão, o quarto.
20 Filhos de Uziel: Mica, o chefe, e Issias, o segundo.
21 Filhos de Merari: Mali e Musi; filhos de Mali: Eleazar e Quis.
22 Morreu Eleazar e não teve filhos, porém filhas; e os filhos de Quis, seus irmãos, as desposaram.
23 Os filhos de Musi: Mali, Éder e Jerimote, três.
24 São estes os filhos de Levi, segundo as suas famílias e chefes delas, segundo foram contados nominalmente, um por um, encarregados do ministério da Casa do Senhor, de vinte anos para cima.
25 Porque disse Davi: O Senhor, Deus de Israel, deu paz ao seu povo e habitará em Jerusalém para sempre.
26 Assim, os levitas já não precisarão levar o tabernáculo e nenhum dos utensílios para o seu ministério.
27 Porque, segundo as últimas palavras de Davi, foram contados os filhos de Levi de vinte anos para cima.
28 O cargo deles era assistir os filhos de Arão no ministério da Casa do Senhor, nos átrios e nas câmaras, na purificação de todas as coisas sagradas e na obra do ministério da Casa de Deus,
29 a saber, os pães da proposição, a flor de farinha para a oferta de manjares, os coscorões asmos, as assadeiras, o tostado e toda sorte de peso e medida.
30 Deviam estar presentes todas as manhãs para renderem graças ao Senhor e o louvarem; e da mesma sorte, à tarde;
31 e para cada oferecimento dos holocaustos do Senhor, nos sábados, nas Festas da Lua Nova e nas festas fixas, perante o Senhor, segundo o número determinado;
32 e para que tivessem a seu cargo a tenda da congregação e o santuário e atendessem aos filhos de Arão, seus irmãos, no ministério da Casa do Senhor.*
1 Quanto aos filhos de Arão, foram eles divididos por seus turnos. Filhos de Arão: Nadabe, Abiú, Eleazar e Itamar.
2 Nadabe e Abiú morreram antes de seu pai e não tiveram filhos; Eleazar e Itamar oficiavam como sacerdotes.
3 Davi, com Zadoque, dos filhos de Eleazar, e com Aimeleque, dos filhos de Itamar, os dividiu segundo os seus deveres no seu ministério.
4 E achou-se que eram mais os filhos de Eleazar entre os chefes de famílias do que os filhos de Itamar, quando os dividiram; dos filhos de Eleazar, dezesseis chefes de famílias; dos filhos de Itamar, oito.
5 Repartiram-nos por sortes, uns como os outros; porque havia príncipes do santuário e príncipes de Deus, tanto dos filhos de Eleazar como dos filhos de Itamar.
6 Semaías, escrivão, filho de Natanael, levita, registrou-os na presença do rei, dos príncipes, do sacerdote Zadoque, de Aimeleque, filho de Abiatar, e dos cabeças das famílias dos sacerdotes e dos levitas; sendo escolhidas as famílias, por sorte, alternadamente, para Eleazar e para Itamar.
7 Saiu a primeira sorte a Jeoiaribe; a segunda, a Jedaías;
8 a terceira, a Harim; a quarta, a Seorim;
9 a quinta, a Malquias; a sexta, a Miamim;
10 a sétima, a Hacoz; a oitava, a Abias;
11 a nona, a Jesua; a décima, a Secanias;
12 a undécima, a Eliasibe; a duodécima, a Jaquim;
13 a décima terceira, a Hupá; a décima quarta, a Jesebeabe;
14 a décima quinta, a Bilga; a décima sexta, a Imer;
15 a décima sétima, a Hezir; a décima oitava, a Hapises;
16 a décima nona, a Petaías; a vigésima, a Jeezquel;
17 a vigésima primeira, a Jaquim; a vigésima segunda, a Gamul;
18 a vigésima terceira, a Delaías; a vigésima quarta, a Maazias.
19 O ofício destes no seu ministério era entrar na Casa do Senhor, segundo a maneira estabelecida por Arão, seu pai, como o Senhor, Deus de Israel, lhe ordenara.
20 Eis os chefes do restante dos filhos de Levi: dos filhos de Anrão, Subael; dos filhos de Subael, Jedias;
21 dos filhos de Reabias, Issias, o chefe;
22 dos isaritas, Selomite; dos filhos de Selomite, Jaate;
23 dos filhos de Hebrom, Jerias, o primeiro, Amarias, o segundo, Jaaziel, o terceiro, Jecameão, o quarto;
24 dos filhos de Uziel, Mica; dos filhos de Mica, Samir;
25 o irmão de Mica, Issias; dos filhos de Issias, Zacarias;
26 dos filhos de Merari, Mali e Musi; dos filhos de Jaazias, Beno;
27 dos filhos de Merari, da parte de Jaazias: Beno, Soão, Zacur e Ibri;
28 de Mali, Eleazar, que não teve filhos;
29 dos filhos de Quis, Jerameel;
30 dos filhos de Musi, Mali, Éder e Jerimote. Foram estes os filhos dos levitas, segundo as suas famílias.
31 Também estes, tanto os chefes das famílias como os seus irmãos menores, como fizeram os outros seus irmãos, filhos de Arão, lançaram sortes na presença do rei Davi, de Zadoque, de Aimeleque e dos cabeças das famílias dos sacerdotes e dos levitas.*
1 Davi, juntamente com os chefes do serviço, separou para o ministério os filhos de Asafe, de Hemã e de Jedutum, para profetizarem com harpas, alaúdes e címbalos. O rol dos encarregados neste ministério foi:
2 dos filhos de Asafe: Zacur, José, Netanias e Asarela, filhos de Asafe, sob a direção deste, que exercia o seu ministério debaixo das ordens do rei.
3 Quanto à família de Jedutum, os filhos: Gedalias, Zeri, Jesaías, Hasabias e Matitias, seis, sob a direção de Jedutum, seu pai, que profetizava com harpas, em ações de graças e louvores ao Senhor.
4 Quanto à família de Hemã, os filhos: Buquias, Matanias, Uziel, Sebuel, Jerimote, Hananias, Hanani, Eliata, Gidalti, Romanti-Ézer, Josbecasa, Maloti, Hotir e Maaziote.
5 Todos estes foram filhos de Hemã, o vidente do rei e cujo poder Deus exaltou segundo as suas promessas, dando-lhe catorze filhos e três filhas.
6 Todos estes estavam sob a direção respectivamente de seus pais, para o canto da Casa do Senhor, com címbalos, alaúdes e harpas, para o ministério da Casa de Deus, estando Asafe, Jedutum e Hemã debaixo das ordens do rei.
7 O número deles, juntamente com seus irmãos instruídos no canto do Senhor, todos eles mestres, era de duzentos e oitenta e oito.
8 Deitaram sortes para designar os deveres, tanto do pequeno como do grande, tanto do mestre como do discípulo.
9 A primeira sorte tocou à família de Asafe e saiu a José; a segunda, a Gedalias, que, com seus irmãos e seus filhos, eram doze ao todo.
10 A terceira, a Zacur, seus filhos e seus irmãos, doze.
11 A quarta, a Izri, seus filhos e seus irmãos, doze.
12 A quinta, a Netanias, seus filhos e seus irmãos, doze.
13 A sexta, a Buquias, seus filhos e seus irmãos, doze.
14 A sétima, a Jesarela, seus filhos e seus irmãos, doze.
15 A oitava, a Jesaías, seus filhos e seus irmãos, doze.
16 A nona, a Matanias, seus filhos e seus irmãos, doze.
17 A décima, a Simei, seus filhos e seus irmãos, doze.
18 A undécima, a Azarel, seus filhos e seus irmãos, doze.
19 A duodécima, a Hasabias, seus filhos e seus irmãos, doze.
20 A décima terceira, a Subael, seus filhos e seus irmãos, doze.
21 A décima quarta, a Matitias, seus filhos e seus irmãos, doze.
22 A décima quinta, a Jerimote, seus filhos e seus irmãos, doze.
23 A décima sexta, a Hananias, seus filhos e seus irmãos, doze.
24 A décima sétima, a Josbecasa, seus filhos e seus irmãos, doze.
25 A décima oitava, a Hanani, seus filhos e seus irmãos, doze.
26 A décima nona, a Maloti, seus filhos e seus irmãos, doze.
27 A vigésima, a Eliata, seus filhos e seus irmãos, doze.
28 A vigésima primeira, a Hotir, seus filhos e seus irmãos, doze.
29 A vigésima segunda, a Gidalti, seus filhos e seus irmãos, doze.
30 A vigésima terceira, a Maaziote, seus filhos e seus irmãos, doze.
31 A vigésima quarta, a Romanti-Ézer, seus filhos e seus irmãos, doze.*
1 Quanto aos turnos dos porteiros, dos coreítas: Meselemias, filho de Coré, dos filhos de Asafe.
2 Os filhos de Meselemias: Zacarias, o primogênito, Jediael, o segundo, Zebadias, o terceiro, Jatniel, o quarto,
3 Elão, o quinto, Joanã, o sexto, Elioenai, o sétimo.
4 Os filhos de Obede-Edom: Semaías, o primogênito, Jeozabade, o segundo, Joá, o terceiro, Sacar, o quarto, Natanael, o quinto.
5 Amiel, o sexto, Issacar, o sétimo, Peuletai, o oitavo; porque Deus o tinha abençoado.
6 Também a seu filho Semaías nasceram filhos, que dominaram sobre a casa de seu pai; porque foram homens valentes.
7 Os filhos de Semaías: Otni, Rafael, Obede e Elzabade, cujos irmãos Eliú e Semaquias eram homens valentes.
8 Todos estes foram dos filhos de Obede-Edom; eles, seus filhos e seus irmãos, homens capazes e robustos para o serviço, ao todo, sessenta e dois.
9 Os filhos e os irmãos de Meselemias, homens valentes, foram dezoito.
10 De Hosa, dos filhos de Merari, foram filhos: Sinri, a quem o pai constituiu chefe, ainda que não era o primogênito.
11 Hilquias, o segundo, Tebalias, o terceiro, Zacarias, o quarto; todos os filhos e irmãos de Hosa foram treze.
12 A estes turnos dos porteiros, isto é, a seus chefes, foi entregue a guarda, para servirem, como seus irmãos, na Casa do Senhor.
13 Para cada porta deitaram sortes para designar os deveres tanto dos pequenos como dos grandes, segundo as suas famílias.
14 A guarda do lado do oriente caiu por sorte a Selemias; depois, lançaram sorte sobre seu filho Zacarias, conselheiro prudente, e lhe saiu a guarda do lado do norte;
15 a Obede-Edom, a do lado do sul; e a seus filhos, a da casa de depósitos;
16 a Supim e Hosa, a do ocidente, junto à porta de Salequete, na estrada que sobe; guarda correspondendo uns aos outros:
17 ao oriente, estavam de guarda seis levitas; ao norte, quatro por dia; ao sul, quatro por dia, e, para a casa de depósitos, dois num lugar e dois noutro.
18 No átrio ao ocidente, quatro junto ao caminho, dois junto ao átrio.
19 São estes os turnos dos porteiros dos filhos dos coreítas e dos filhos de Merari.
20 Dos levitas, seus irmãos, que tinham o encargo dos tesouros da Casa de Deus e dos tesouros das coisas consagradas:
21 os filhos de Ladã, descendentes dos gersonitas pertencentes a Ladã e chefes das famílias deste, da família de Gérson: Jeieli;
22 os filhos de Jeieli: Zetã e Joel, seu irmão; estavam estes a cargo dos tesouros da Casa do Senhor.
23 Dos anramitas, dos isaritas, dos hebronitas, dos uzielitas,
24 Sebuel, filho de Gérson, filho de Moisés, era oficial encarregado dos tesouros.
25 Seus irmãos: de Eliézer, foi filho Reabias, de quem foi filho Jesaías, de quem foi filho Jorão, de quem foi filho Zicri, de quem foi filho Selomite.
26 Este Selomite e seus irmãos tinham a seu cargo todos os tesouros das coisas consagradas que o rei Davi e os chefes das famílias, capitães de milhares e de centenas e capitães do exército tinham dedicado;
27 dos despojos das guerras as dedicaram para a conservação da Casa do Senhor,
28 como também tudo quanto havia dedicado Samuel, o vidente, e Saul, filho de Quis, e Abner, filho de Ner, e Joabe, filho de Zeruia; tudo quanto qualquer pessoa havia dedicado estava sob os cuidados de Selomite e seus irmãos.
29 Dos isaritas, Quenanias e seus filhos foram postos sobre Israel, para oficiais e juízes dos negócios externos;
30 dos hebronitas, foram Hasabias e seus irmãos, homens valentes, mil e setecentos, que superintendiam Israel, além do Jordão para o ocidente, em todo serviço do Senhor e interesses do rei;
31 dos hebronitas, Jerias era o chefe. Quanto aos hebronitas, suas genealogias e famílias, se fizeram investigações no quadragésimo ano do reinado de Davi e se acharam entre eles homens valentes em Jazer de Gileade.
32 Seus irmãos, homens valentes, dois mil e setecentos, chefes das famílias; e o rei Davi os constituiu sobre os rubenitas, os gaditas e a meia tribo dos manassitas, para todos os negócios de Deus e para todos os negócios do rei.*
1 São estes os filhos de Israel segundo o seu número, os chefes das famílias e os capitães de milhares e de centenas com os seus oficiais, que serviam ao rei em todos os negócios dos turnos que entravam e saíam de mês em mês durante o ano, cada turno de vinte e quatro mil.
2 Sobre o primeiro turno do primeiro mês estava Jasobeão, filho de Zabdiel; em seu turno havia vinte e quatro mil.
3 Era este dos filhos de Perez, chefe de todos os capitães dos exércitos para o primeiro mês.
4 Sobre o turno do segundo mês estava Dodai, o aoíta, a cujo lado estava Miclote; também em seu turno havia vinte e quatro mil.
5 O terceiro capitão do exército e o designado para o terceiro mês era Benaia, chefe, filho do sacerdote Joiada; também em seu turno havia vinte e quatro mil.
6 Era este Benaia homem poderoso entre os trinta e cabeça deles; o seu turno estava ao encargo do seu filho Amizabade.
7 O quarto, para o quarto mês, Asael, irmão de Joabe, e depois dele Zebadias, seu filho; também em seu turno havia vinte e quatro mil.
8 O quinto capitão, para o quinto mês, Samute, o izraíta; também em seu turno havia vinte e quatro mil.
9 O sexto, para o sexto mês, Ira, filho de Iques, o tecoíta; também em seu turno havia vinte e quatro mil.
10 O sétimo, para o sétimo mês, Heles, o pelonita, dos filhos de Efraim; também em seu turno havia vinte e quatro mil.
11 O oitavo, para o oitavo mês, Sibecai, o husatita, dos zeraítas; também em seu turno havia vinte e quatro mil.
12 O nono, para o nono mês, Abiezer, o anatotita, dos benjamitas; também em seu turno havia vinte e quatro mil.
13 O décimo, para o décimo mês, Maarai, o netofatita, dos zeraítas; também em seu turno havia vinte e quatro mil.
14 O undécimo, para o undécimo mês, Benaia, o piratonita, dos filhos de Efraim; também em seu turno havia vinte e quatro mil.
15 O duodécimo, para o duodécimo mês, Heldai, o netofatita, de Otniel; também em seu turno havia vinte e quatro mil.
16 Sobre as tribos de Israel eram estes: sobre os rubenitas era chefe Eliézer, filho de Zicri; sobre os simeonitas, Sefatias, filho de Maaca;
17 sobre os levitas, Hasabias, filho de Quemuel; sobre os aronitas, Zadoque;
18 sobre Judá, Eliú, dos irmãos de Davi; sobre Issacar, Onri, filho de Micael;
19 sobre Zebulom, Ismaías, filho de Obadias; sobre Naftali, Jerimote, filho de Azriel;
20 sobre os filhos de Efraim, Oseias, filho de Azazias; sobre a meia tribo de Manassés, Joel, filho de Pedaías;
21 sobre a outra meia tribo de Manassés em Gileade, Ido, filho de Zacarias; sobre Benjamim, Jaasiel, filho de Abner;
22 sobre Dã, Azarel, filho de Jeroão; estes eram os chefes das tribos de Israel.
23 Davi não contou os que eram de vinte anos para baixo, porque o Senhor tinha dito que multiplicaria a Israel como as estrelas do céu.
24 Joabe, filho de Zeruia, tinha começado a contar o povo, porém não acabou, porquanto viera por isso grande ira sobre Israel; pelo que o número não se registrou na história do rei Davi.
25 Azmavete, filho de Adiel, estava sobre os tesouros do rei; sobre o que este possuía nos campos, nas cidades, nas aldeias e nos castelos, Jônatas, filho de Uzias.
26 Sobre os lavradores do campo, que cultivavam a terra, Ezri, filho de Quelube.
27 Sobre as vinhas, Simei, o ramatita; porém sobre o que das vides entrava para as adegas, Zabdi, o sifmita.
28 Sobre os olivais e sicômoros que havia nas campinas, Baal-Hanã, o gederita; porém Joás, sobre os depósitos do azeite.
29 Sobre os gados que pasciam em Sarom, Sitrai, o saronita; porém sobre os gados dos vales, Safate, filho de Adlai.
30 Sobre os camelos, Obil, o ismaelita; sobre as jumentas, Jedias, o meronotita.
31 Sobre o gado miúdo, Jaziz, o hagareno; todos estes eram administradores da fazenda do rei Davi.
32 Jônatas, tio de Davi, era do conselho, homem sábio e escriba; Jeiel, filho de Hacmoni, atendia os filhos do rei.
33 Aitofel era do conselho do rei; Husai, o arquita, amigo do rei.
34 A Aitofel sucederam Joiada, filho de Benaia, e Abiatar; Joabe era comandante do exército do rei.*
1 Então, Davi convocou para Jerusalém todos os príncipes de Israel, os príncipes das tribos, os capitães dos turnos que serviam o rei, os capitães de mil e os de cem, os administradores de toda a fazenda e possessões do rei e de seus filhos, como também os oficiais, os poderosos e todo homem valente.
2 Pôs-se o rei Davi em pé e disse: Ouvi-me, irmãos meus e povo meu: Era meu propósito de coração edificar uma casa de repouso para a arca da Aliança do Senhor e para o estrado dos pés do nosso Deus, e eu tinha feito o preparo para a edificar.
3 Porém Deus me disse: Não edificarás casa ao meu nome, porque és homem de guerra e derramaste muito sangue.
4 O Senhor, Deus de Israel, me escolheu de toda a casa de meu pai, para que eternamente fosse eu rei sobre Israel; porque a Judá escolheu por príncipe e a casa de meu pai, na casa de Judá; e entre os filhos de meu pai se agradou de mim, para me fazer rei sobre todo o Israel.
5 E, de todos os meus filhos, porque muitos filhos me deu o Senhor, escolheu ele a Salomão para se assentar no trono do reino do Senhor, sobre Israel.
6 E me disse: Teu filho Salomão é quem edificará a minha casa e os meus átrios, porque o escolhi para filho e eu lhe serei por pai.
7 Estabelecerei o seu reino para sempre, se perseverar ele em cumprir os meus mandamentos e os meus juízos, como até ao dia de hoje.
8 Agora, pois, perante todo o Israel, a congregação do Senhor, e perante o nosso Deus, que me ouve, eu vos digo: guardai todos os mandamentos do Senhor, vosso Deus, e empenhai-vos por eles, para que possuais esta boa terra e a deixeis como herança a vossos filhos, para sempre.
9 Tu, meu filho Salomão, conhece o Deus de teu pai e serve-o de coração íntegro e alma voluntária; porque o Senhor esquadrinha todos os corações e penetra todos os desígnios do pensamento. Se o buscares, ele deixará achar-se por ti; se o deixares, ele te rejeitará para sempre.
10 Agora, pois, atende a tudo, porque o Senhor te escolheu para edificares casa para o santuário; sê forte e faze a obra.
11 Deu Davi a Salomão, seu filho, a planta do pórtico com as suas casas, as suas tesourarias, os seus cenáculos e as suas câmaras interiores, como também da casa do propiciatório.
12 Também a planta de tudo quanto tinha em mente, com referência aos átrios da Casa do Senhor, e a todas as câmaras em redor, para os tesouros da Casa de Deus e para os tesouros das coisas consagradas;
13 e para os turnos dos sacerdotes e dos levitas, e para toda obra do ministério da Casa do Senhor, e para todos os utensílios para o serviço da Casa do Senhor,
14 especificando o peso do ouro para todos os utensílios de ouro de cada serviço; também o peso da prata para todos os utensílios de prata de cada serviço;
15 o peso para os candeeiros de ouro e suas lâmpadas de ouro, para cada candeeiro e suas lâmpadas, segundo o uso de cada um;
16 também o peso do ouro para as mesas da proposição, para cada uma de per si; como também a prata para as mesas de prata;
17 ouro puro para os garfos, para as bacias e para os copos; para as taças de ouro o devido peso a cada uma, como também para as taças de prata, a cada uma o seu peso;
18 o peso do ouro refinado para o altar do incenso, como também, segundo a planta, o ouro para o carro dos querubins, que haviam de estender as asas e cobrir a arca da Aliança do Senhor.
19 Tudo isto, disse Davi, me foi dado por escrito por mandado do Senhor, a saber, todas as obras desta planta.
20 Disse Davi a Salomão, seu filho: Sê forte e corajoso e faze a obra; não temas, nem te desanimes, porque o Senhor Deus, meu Deus, há de ser contigo; não te deixará, nem te desamparará, até que acabes todas as obras para o serviço da Casa do Senhor.
21 Eis aí os turnos dos sacerdotes e dos levitas para todo serviço da Casa de Deus; também se acham contigo, para toda obra, voluntários com sabedoria de toda espécie para cada serviço; como também os príncipes e todo o povo estarão inteiramente às tuas ordens.*
1 Disse mais o rei Davi a toda a congregação: Salomão, meu filho, o único a quem Deus escolheu, é ainda moço e inexperiente, e esta obra é grande; porque o palácio não é para homens, mas para o Senhor Deus.
2 Eu, pois, com todas as minhas forças já preparei para a casa de meu Deus ouro para as obras de ouro, prata para as de prata, bronze para as de bronze, ferro para as de ferro e madeira para as de madeira; pedras de ônix, pedras de engaste, pedras de várias cores, de mosaicos e toda sorte de pedras preciosas, e mármore, e tudo em abundância.
3 E ainda, porque amo a casa de meu Deus, o ouro e a prata particulares que tenho dou para a casa de meu Deus, afora tudo quanto preparei para o santuário:
4 três mil talentos de ouro, do ouro de Ofir, e sete mil talentos de prata purificada, para cobrir as paredes das casas;
5 ouro para os objetos de ouro e prata para os de prata, e para toda obra de mão dos artífices. Quem, pois, está disposto, hoje, a trazer ofertas liberalmente ao Senhor?
6 Então, os chefes das famílias, os príncipes das tribos de Israel, os capitães de mil e os de cem e até os intendentes sobre as empresas do rei voluntariamente contribuíram
7 e deram para o serviço da Casa de Deus cinco mil talentos de ouro, dez mil daricos, dez mil talentos de prata, dezoito mil talentos de bronze e cem mil talentos de ferro.
8 Os que possuíam pedras preciosas as trouxeram para o tesouro da Casa do Senhor, a cargo de Jeiel, o gersonita.
9 O povo se alegrou com tudo o que se fez voluntariamente; porque de coração íntegro deram eles liberalmente ao Senhor; também o rei Davi se alegrou com grande júbilo.
10 Pelo que Davi louvou ao Senhor perante a congregação toda e disse: Bendito és tu, Senhor, Deus de Israel, nosso pai, de eternidade em eternidade.
11 Teu, Senhor, é o poder, a grandeza, a honra, a vitória e a majestade; porque teu é tudo quanto há nos céus e na terra; teu, Senhor, é o reino, e tu te exaltaste por chefe sobre todos.
12 Riquezas e glória vêm de ti, tu dominas sobre tudo, na tua mão há força e poder; contigo está o engrandecer e a tudo dar força.
13 Agora, pois, ó nosso Deus, graças te damos e louvamos o teu glorioso nome.
14 Porque quem sou eu, e quem é o meu povo para que pudéssemos dar voluntariamente estas coisas? Porque tudo vem de ti, e das tuas mãos to damos.
15 Porque somos estranhos diante de ti e peregrinos como todos os nossos pais; como a sombra são os nossos dias sobre a terra, e não temos permanência.
16 Senhor, nosso Deus, toda esta abundância que preparamos para te edificar uma casa ao teu santo nome vem da tua mão e é toda tua.
17 Bem sei, meu Deus, que tu provas os corações e que da sinceridade te agradas; eu também, na sinceridade de meu coração, dei voluntariamente todas estas coisas; acabo de ver com alegria que o teu povo, que se acha aqui, te faz ofertas voluntariamente.
18 Senhor, Deus de nossos pais Abraão, Isaque e Israel, conserva para sempre no coração do teu povo estas disposições e pensamentos, inclina-lhe o coração para contigo;
19 e a Salomão, meu filho, dá coração íntegro para guardar os teus mandamentos, os teus testemunhos e os teus estatutos, fazendo tudo para edificar este palácio para o qual providenciei.
20 Então, disse Davi a toda a congregação: Agora, louvai o Senhor, vosso Deus. Então, toda a congregação louvou ao Senhor, Deus de seus pais; todos inclinaram a cabeça, adoraram o Senhor e se prostraram perante o rei.
21 Ao outro dia, trouxeram sacrifícios ao Senhor e lhe ofereceram holocaustos de mil bezerros, mil carneiros, mil cordeiros, com as suas libações; sacrifícios em abundância por todo o Israel.
22 Comeram e beberam, naquele dia, perante o Senhor, com grande regozijo. Pela segunda vez, fizeram rei a Salomão, filho de Davi, e o ungiram ao Senhor por príncipe e a Zadoque, por sacerdote.
23 Salomão assentou-se no trono do Senhor, rei, em lugar de Davi, seu pai, e prosperou; e todo o Israel lhe obedecia.
24 Todos os príncipes, os grandes e até todos os filhos do rei Davi prestaram homenagens ao rei Salomão.
25 O Senhor engrandeceu sobremaneira a Salomão perante todo o Israel; deu-lhe majestade real, qual antes dele não teve nenhum rei em Israel.
26 Ora, Davi, filho de Jessé, reinou sobre todo o Israel.
27 O tempo que reinou sobre Israel foi de quarenta anos: em Hebrom, sete; em Jerusalém, trinta e três.
28 Morreu em ditosa velhice, cheio de dias, riquezas e glória; e Salomão, seu filho, reinou em seu lugar.
29 Os atos, pois, do rei Davi, tanto os primeiros como os últimos, eis que estão escritos nas crônicas, registrados por Samuel, o vidente, nas crônicas do profeta Natã e nas crônicas de Gade, o vidente,
30 juntamente com o que se passou no seu reinado e a respeito do seu poder e todos os acontecimentos que se deram com ele, com Israel e com todos os reinos daquelas terras.*
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'1_Crônicas','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)