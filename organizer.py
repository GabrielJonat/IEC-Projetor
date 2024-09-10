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
1 Depois da morte de Josué, os filhos de Israel consultaram o Senhor, dizendo: Quem dentre nós, primeiro, subirá aos cananeus para pelejar contra eles?
2 Respondeu o Senhor: Judá subirá; eis que nas suas mãos entreguei a terra.
3 Disse, pois, Judá a Simeão, seu irmão: Sobe comigo à herança que me caiu por sorte, e pelejemos contra os cananeus, e também eu subirei contigo à tua, que te caiu por sorte. E Simeão partiu com ele.
4 Subiu Judá, e o Senhor lhe entregou nas mãos os cananeus e os ferezeus; e feriram deles, em Bezeque, dez mil homens.
5 Em Bezeque, encontraram Adoni-Bezeque e pelejaram contra ele; e feriram aos cananeus e aos ferezeus.
6 Adoni-Bezeque, porém, fugiu; mas o perseguiram e, prendendo-o, lhe cortaram os polegares das mãos e dos pés.
7 Então, disse Adoni-Bezeque: Setenta reis, a quem haviam sido cortados os polegares das mãos e dos pés, apanhavam migalhas debaixo da minha mesa; assim como eu fiz, assim Deus me pagou. E o levaram a Jerusalém, e morreu ali.
8 Os filhos de Judá pelejaram contra Jerusalém e, tomando-a, passaram-na a fio de espada, pondo fogo à cidade.
9 Depois, os filhos de Judá desceram a pelejar contra os cananeus que habitavam nas montanhas, no Neguebe e nas planícies.
10 Partiu Judá contra os cananeus que habitavam em Hebrom, cujo nome, outrora, era Quiriate-Arba, e Judá feriu a Sesai, a Aimã e a Talmai.
11 Dali partiu contra os moradores de Debir; e era, dantes, o nome de Debir Quiriate-Sefer.
12 Disse Calebe: A quem derrotar Quiriate-Sefer e a tomar, darei minha filha Acsa por mulher.
13 Tomou-a, pois, Otniel, filho de Quenaz, o irmão de Calebe, mais novo do que ele; e Calebe lhe deu sua filha Acsa por mulher.
14 Esta, quando se foi a ele, insistiu com ele para que pedisse um campo ao pai dela; e ela apeou do jumento; então, Calebe lhe perguntou: Que desejas?
15 Respondeu ela: Dá-me um presente; deste-me terra seca, dá-me também fontes de água. Então, Calebe lhe deu as fontes superiores e as fontes inferiores.
16 Os filhos do queneu, sogro de Moisés, subiram, com os filhos de Judá, da cidade das Palmeiras ao deserto de Judá, que está ao sul de Arade; foram e habitaram com este povo.
17 Foi-se, pois, Judá com Simeão, seu irmão, e feriram aos cananeus que habitavam em Zefate e totalmente a destruíram; por isso, lhe chamaram Horma.
18 Tomou ainda Judá a Gaza, a Asquelom e a Ecrom com os seus respectivos territórios.
19 Esteve o Senhor com Judá, e este despovoou as montanhas; porém não expulsou os moradores do vale, porquanto tinham carros de ferro.
20 E, como Moisés o dissera, deram Hebrom a Calebe, e este expulsou dali os três filhos de Anaque.
21 Porém os filhos de Benjamim não expulsaram os jebuseus que habitavam em Jerusalém; antes, os jebuseus habitam com os filhos de Benjamim em Jerusalém, até ao dia de hoje.
22 Subiu também a casa de José contra Betel, e o Senhor era com eles.
23 A casa de José enviou homens a espiar Betel, cujo nome, dantes, era Luz.
24 Vendo os espias um homem que saía da cidade, lhe disseram: Mostra-nos a entrada da cidade, e usaremos de misericórdia para contigo.
25 Mostrando-lhes ele a entrada da cidade, feriram a cidade a fio de espada; porém, àquele homem e a toda a sua família, deixaram ir.
26 Então, se foi ele à terra dos heteus, e edificou uma cidade, e lhe chamou Luz; este é o seu nome até ao dia de hoje.
27 Manassés não expulsou os habitantes de Bete-Seã, nem os de Taanaque, nem os de Dor, nem os de Ibleão, nem os de Megido, todas com suas respectivas aldeias; pelo que os cananeus lograram permanecer na mesma terra.
28 Quando, porém, Israel se tornou mais forte, sujeitou os cananeus a trabalhos forçados e não os expulsou de todo.
29 Efraim não expulsou os cananeus, habitantes de Gezer; antes, continuaram com ele em Gezer.
30 Zebulom não expulsou os habitantes de Quitrom, nem os de Naalol; porém os cananeus continuaram com ele, sujeitos a trabalhos forçados.
31 Aser não expulsou os habitantes de Aco, nem os de Sidom, os de Alabe, os de Aczibe, os de Helba, os de Afeca e os de Reobe;
32 porém os aseritas continuaram no meio dos cananeus que habitavam na terra, porquanto os não expulsaram.
33 Naftali não expulsou os habitantes de Bete-Semes, nem os de Bete-Anate; mas continuou no meio dos cananeus que habitavam na terra; porém os de Bete-Semes e Bete-Anate lhe foram sujeitos a trabalhos forçados.
34 Os amorreus arredaram os filhos de Dã até às montanhas e não os deixavam descer ao vale.
35 Porém os amorreus lograram habitar nas montanhas de Heres, em Aijalom e em Saalabim; contudo, a mão da casa de José prevaleceu, e foram sujeitos a trabalhos forçados.
36 O limite dos amorreus foi desde a subida de Acrabim e desde Sela para cima.*
1 Subiu o Anjo do Senhor de Gilgal a Boquim e disse: Do Egito vos fiz subir e vos trouxe à terra que, sob juramento, havia prometido a vossos pais. Eu disse: nunca invalidarei a minha aliança convosco.
2 Vós, porém, não fareis aliança com os moradores desta terra; antes, derribareis os seus altares; contudo, não obedecestes à minha voz. Que é isso que fizestes?
3 Pelo que também eu disse: não os expulsarei de diante de vós; antes, vos serão por adversários, e os seus deuses vos serão laços.
4 Sucedeu que, falando o Anjo do Senhor estas palavras a todos os filhos de Israel, levantou o povo a sua voz e chorou.
5 Daí, chamarem a esse lugar Boquim; e sacrificaram ali ao Senhor.
6 Havendo Josué despedido o povo, foram-se os filhos de Israel, cada um à sua herança, para possuírem a terra.
7 Serviu o povo ao Senhor todos os dias de Josué e todos os dias dos anciãos que ainda sobreviveram por muito tempo depois de Josué e que viram todas as grandes obras feitas pelo Senhor a Israel.
8 Faleceu Josué, filho de Num, servo do Senhor, com a idade de cento e dez anos;
9 sepultaram-no no limite da sua herança, em Timnate-Heres, na região montanhosa de Efraim, ao norte do monte Gaás.
10 Foi também congregada a seus pais toda aquela geração; e outra geração após eles se levantou, que não conhecia o Senhor, nem tampouco as obras que fizera a Israel.
11 Então, fizeram os filhos de Israel o que era mau perante o Senhor; pois serviram aos baalins.
12 Deixaram o Senhor, Deus de seus pais, que os tirara da terra do Egito, e foram-se após outros deuses, dentre os deuses das gentes que havia ao redor deles, e os adoraram, e provocaram o Senhor à ira.
13 Porquanto deixaram o Senhor e serviram a Baal e a Astarote.
14 Pelo que a ira do Senhor se acendeu contra Israel e os deu na mão dos espoliadores, que os pilharam; e os entregou na mão dos seus inimigos ao redor; e não mais puderam resistir a eles.
15 Por onde quer que saíam, a mão do Senhor era contra eles para seu mal, como o Senhor lhes dissera e jurara; e estavam em grande aperto.
16 Suscitou o Senhor juízes, que os livraram da mão dos que os pilharam.
17 Contudo, não obedeceram aos seus juízes; antes, se prostituíram após outros deuses e os adoraram. Depressa se desviaram do caminho por onde andaram seus pais na obediência dos mandamentos do Senhor; e não fizeram como eles.
18 Quando o Senhor lhes suscitava juízes, o Senhor era com o juiz e os livrava da mão dos seus inimigos, todos os dias daquele juiz; porquanto o Senhor se compadecia deles ante os seus gemidos, por causa dos que os apertavam e oprimiam.
19 Sucedia, porém, que, falecendo o juiz, reincidiam e se tornavam piores do que seus pais, seguindo após outros deuses, servindo-os e adorando-os eles; nada deixavam das suas obras, nem da obstinação dos seus caminhos.
20 Pelo que a ira do Senhor se acendeu contra Israel; e disse: Porquanto este povo transgrediu a minha aliança que eu ordenara a seus pais e não deu ouvidos à minha voz,
21 também eu não expulsarei mais de diante dele nenhuma das nações que Josué deixou quando morreu;
22 para, por elas, pôr Israel à prova, se guardará ou não o caminho do Senhor, como seus pais o guardaram.
23 Assim, o Senhor deixou ficar aquelas nações e não as expulsou logo, nem as entregou na mão de Josué.*
1 São estas as nações que o Senhor deixou para, por elas, provar a Israel, isto é, provar quantos em Israel não sabiam de todas as guerras de Canaã.
2 Isso tão somente para que as gerações dos filhos de Israel delas soubessem (para lhes ensinar a guerra), pelo menos as gerações que, dantes, não sabiam disso:
3 cinco príncipes dos filisteus, e todos os cananeus, e sidônios, e heveus que habitavam as montanhas do Líbano, desde o monte de Baal-Hermom até à entrada de Hamate.
4 Estes ficaram para, por eles, o Senhor pôr Israel à prova, para saber se dariam ouvidos aos mandamentos que havia ordenado a seus pais por intermédio de Moisés.
5 Habitando, pois, os filhos de Israel no meio dos cananeus, dos heteus, e amorreus, e ferezeus, e heveus, e jebuseus,
6 tomaram de suas filhas para si por mulheres e deram as suas próprias aos filhos deles; e rendiam culto a seus deuses.
7 Os filhos de Israel fizeram o que era mau perante o Senhor e se esqueceram do Senhor, seu Deus; e renderam culto aos baalins e ao poste-ídolo.
8 Então, a ira do Senhor se acendeu contra Israel, e ele os entregou nas mãos de Cusã-Risataim, rei da Mesopotâmia; e os filhos de Israel serviram a Cusã-Risataim oito anos.
9 Clamaram ao Senhor os filhos de Israel, e o Senhor lhes suscitou libertador, que os libertou: Otniel, filho de Quenaz, que era irmão de Calebe e mais novo do que ele.
10 Veio sobre ele o Espírito do Senhor, e ele julgou a Israel; saiu à peleja, e o Senhor lhe entregou nas mãos a Cusã-Risataim, rei da Mesopotâmia, contra o qual ele prevaleceu.
11 Então, a terra ficou em paz durante quarenta anos. Otniel, filho de Quenaz, faleceu.
12 Tornaram, então, os filhos de Israel a fazer o que era mau perante o Senhor; mas o Senhor deu poder a Eglom, rei dos moabitas, contra Israel, porquanto fizeram o que era mau perante o Senhor.
13 E ajuntou consigo os filhos de Amom e os amalequitas, e foi, e feriu a Israel; e apoderaram-se da cidade das Palmeiras.
14 E os filhos de Israel serviram a Eglom, rei dos moabitas, dezoito anos.
15 Então, os filhos de Israel clamaram ao Senhor, e o Senhor lhes suscitou libertador: Eúde, homem canhoto, filho de Gera, benjamita. Por intermédio dele, enviaram os filhos de Israel tributo a Eglom, rei dos moabitas.
16 Eúde fez para si um punhal de dois gumes, do comprimento de um côvado; e cingiu-o debaixo das suas vestes, do lado direito.
17 Levou o tributo a Eglom, rei dos moabitas; era Eglom homem gordo.
18 Tendo entregado o tributo, despediu a gente que o trouxera e saiu com ela.
19 Porém voltou do ponto em que estavam as imagens de escultura ao pé de Gilgal e disse ao rei: Tenho uma palavra secreta a dizer-te, ó rei. O rei disse: Cala-te. Então, todos os que lhe assistiam saíram de sua presença.
20 Eúde entrou numa sala de verão, que o rei tinha só para si, onde estava assentado, e disse: Tenho a dizer-te uma palavra de Deus. E Eglom se levantou da cadeira.
21 Então, Eúde, estendendo a mão esquerda, puxou o seu punhal do lado direito e lho cravou no ventre,
22 de tal maneira que entrou também o cabo com a lâmina, e, porque não o retirou do ventre, a gordura se fechou sobre ele; e Eúde, saindo por um postigo,
23 passou para o vestíbulo, depois de cerrar sobre ele as portas, trancando-as.
24 Tendo saído, vieram os servos do rei e viram, e eis que as portas da sala de verão estavam trancadas; e disseram: Sem dúvida está ele aliviando o ventre na privada da sala de verão.
25 Aborreceram-se de esperar; e, como não abria a porta da sala, tomaram da chave e a abriram; e eis seu senhor estendido morto em terra.
26 Eúde escapou enquanto eles se demoravam e, tendo passado pelas imagens de escultura, foi para Seirá.
27 Tendo ele chegado, tocou a trombeta nas montanhas de Efraim; e os filhos de Israel desceram com ele das montanhas, indo ele à frente.
28 E lhes disse: Segui-me, porque o Senhor entregou nas vossas mãos os vossos inimigos, os moabitas; e desceram após ele, e tomaram os vaus do Jordão contra os moabitas, e a nenhum deles deixaram passar.
29 Naquele tempo, feriram dos moabitas uns dez mil homens, todos robustos e valentes; e não escapou nem sequer um.
30 Assim, foi Moabe subjugado, naquele dia, sob o poder de Israel; e a terra ficou em paz oitenta anos.
31 Depois dele, foi Sangar, filho de Anate, que feriu seiscentos homens dos filisteus com uma aguilhada de bois; e também ele libertou a Israel.*
1 Os filhos de Israel tornaram a fazer o que era mau perante o Senhor, depois de falecer Eúde.
2 Entregou-os o Senhor nas mãos de Jabim, rei de Canaã, que reinava em Hazor. Sísera era o comandante do seu exército, o qual, então, habitava em Harosete-Hagoim.
3 Clamaram os filhos de Israel ao Senhor, porquanto Jabim tinha novecentos carros de ferro e, por vinte anos, oprimia duramente os filhos de Israel.
4 Débora, profetisa, mulher de Lapidote, julgava a Israel naquele tempo.
5 Ela atendia debaixo da palmeira de Débora, entre Ramá e Betel, na região montanhosa de Efraim; e os filhos de Israel subiam a ela a juízo.
6 Mandou ela chamar a Baraque, filho de Abinoão, de Quedes de Naftali, e disse-lhe: Porventura, o Senhor, Deus de Israel, não deu ordem, dizendo: Vai, e leva gente ao monte Tabor, e toma contigo dez mil homens dos filhos de Naftali e dos filhos de Zebulom?
7 E farei ir a ti para o ribeiro Quisom a Sísera, comandante do exército de Jabim, com os seus carros e as suas tropas; e o darei nas tuas mãos.
8 Então, lhe disse Baraque: Se fores comigo, irei; porém, se não fores comigo, não irei.
9 Ela respondeu: Certamente, irei contigo, porém não será tua a honra da investida que empreendes; pois às mãos de uma mulher o Senhor entregará a Sísera. E saiu Débora e se foi com Baraque para Quedes.
10 Então, Baraque convocou a Zebulom e a Naftali em Quedes, e com ele subiram dez mil homens; e Débora também subiu com ele.
11 Ora, Héber, queneu, se tinha apartado dos queneus, dos filhos de Hobabe, sogro de Moisés, e havia armado as suas tendas até ao carvalho de Zaananim, que está junto a Quedes.
12 Anunciaram a Sísera que Baraque, filho de Abinoão, tinha subido ao monte Tabor.
13 Sísera convocou todos os seus carros, novecentos carros de ferro, e todo o povo que estava com ele, de Harosete-Hagoim para o ribeiro Quisom.
14 Então, disse Débora a Baraque: Dispõe-te, porque este é o dia em que o Senhor entregou a Sísera nas tuas mãos; porventura, o Senhor não saiu adiante de ti? Baraque, pois, desceu do monte Tabor, e dez mil homens, após ele.
15 E o Senhor derrotou a Sísera, e todos os seus carros, e a todo o seu exército a fio de espada, diante de Baraque; e Sísera saltou do carro e fugiu a pé.
16 Mas Baraque perseguiu os carros e os exércitos até Harosete-Hagoim; e todo o exército de Sísera caiu a fio de espada, sem escapar nem sequer um.
17 Porém Sísera fugiu a pé para a tenda de Jael, mulher de Héber, queneu; porquanto havia paz entre Jabim, rei de Hazor, e a casa de Héber, queneu.
18 Saindo Jael ao encontro de Sísera, disse-lhe: Entra, senhor meu, entra na minha tenda, não temas. Retirou-se para a sua tenda, e ela pôs sobre ele uma coberta.
19 Então, ele lhe disse: Dá-me, peço-te, de beber um pouco de água, porque tenho sede. Ela abriu um odre de leite, e deu-lhe de beber, e o cobriu.
20 E ele lhe disse mais: Põe-te à porta da tenda; e há de ser que, se vier alguém e te perguntar: Há aqui alguém?, responde: Não.
21 Então, Jael, mulher de Héber, tomou uma estaca da tenda, e lançou mão de um martelo, e foi-se mansamente a ele, e lhe cravou a estaca na fonte, de sorte que penetrou na terra, estando ele em profundo sono e mui exausto; e, assim, morreu.
22 E eis que, perseguindo Baraque a Sísera, Jael lhe saiu ao encontro e lhe disse: Vem, e mostrar-te-ei o homem que procuras. Ele a seguiu; e eis que Sísera jazia morto, e a estaca na fonte.
23 Assim, Deus, naquele dia, humilhou a Jabim, rei de Canaã, diante dos filhos de Israel.
24 E cada vez mais a mão dos filhos de Israel prevalecia contra Jabim, rei de Canaã, até que o exterminaram.*
1 Naquele dia, cantaram Débora e Baraque, filho de Abinoão, dizendo:
2 Desde que os chefes se puseram à frente de Israel, e o povo se ofereceu voluntariamente, bendizei ao Senhor.
3 Ouvi, reis, dai ouvidos, príncipes: eu, eu mesma cantarei ao Senhor; salmodiarei ao Senhor, Deus de Israel.
4 Saindo tu, ó Senhor, de Seir, marchando desde o campo de Edom, a terra estremeceu; os céus gotejaram, sim, até as nuvens gotejaram águas.
5 Os montes vacilaram diante do Senhor, e até o Sinai, diante do Senhor, Deus de Israel.
6 Nos dias de Sangar, filho de Anate, nos dias de Jael, cessaram as caravanas; e os viajantes tomavam desvios tortuosos.
7 Ficaram desertas as aldeias em Israel, repousaram, até que eu, Débora, me levantei, levantei-me por mãe em Israel.
8 Escolheram-se deuses novos; então, a guerra estava às portas; não se via escudo nem lança entre quarenta mil em Israel.
9 Meu coração se inclina para os comandantes de Israel, que, voluntariamente, se ofereceram entre o povo; bendizei ao Senhor.
10 Vós, os que cavalgais jumentas brancas, que vos assentais em juízo e que andais pelo caminho, falai disto.
11 À música dos distribuidores de água, lá entre os canais dos rebanhos, falai dos atos de justiça do Senhor, das justiças a prol de suas aldeias em Israel. Então, o povo do Senhor pôde descer ao seu lar.
12 Desperta, Débora, desperta, desperta, acorda, entoa um cântico; levanta-te, Baraque, e leva presos os que te prenderam, tu, filho de Abinoão.
13 Então, desceu o restante dos nobres, o povo do Senhor em meu auxílio contra os poderosos.
14 De Efraim, cujas raízes estão na antiga região de Amaleque, desceram guerreiros; depois de ti, ó Débora, seguiu Benjamim com seus povos; de Maquir desceram comandantes, e, de Zebulom, os que levam a vara de comando.
15 Também os príncipes de Issacar foram com Débora; Issacar seguiu a Baraque, em cujas pegadas foi enviado para o vale. Entre as facções de Rúben houve grande discussão.
16 Por que ficaste entre os currais para ouvires a flauta? Entre as facções de Rúben houve grande discussão.
17 Gileade ficou dalém do Jordão, e Dã, por que se deteve junto a seus navios? Aser se assentou nas costas do mar e repousou nas suas baías.
18 Zebulom é povo que expôs a sua vida à morte, como também Naftali, nas alturas do campo.
19 Vieram reis e pelejaram; pelejaram os reis de Canaã em Taanaque, junto às águas de Megido; porém não levaram nenhum despojo de prata.
20 Desde os céus pelejaram as estrelas contra Sísera, desde a sua órbita o fizeram.
21 O ribeiro Quisom os arrastou, Quisom, o ribeiro das batalhas. Avante, ó minha alma, firme!
22 Então, as unhas dos cavalos socavam pelo galopar, o galopar dos seus guerreiros.
23 Amaldiçoai a Meroz, diz o Anjo do Senhor, amaldiçoai duramente os seus moradores, porque não vieram em socorro do Senhor, em socorro do Senhor e seus heróis.
24 Bendita seja sobre as mulheres Jael, mulher de Héber, o queneu; bendita seja sobre as mulheres que vivem em tendas.
25 Água pediu ele, leite lhe deu ela; em taça de príncipes lhe ofereceu nata.
26 À estaca estendeu a mão e, ao maço dos trabalhadores, a direita; e deu o golpe em Sísera, rachou-lhe a cabeça, furou e traspassou-lhe as fontes.
27 Aos pés dela se encurvou, caiu e ficou estirado; a seus pés se encurvou e caiu; onde se encurvou, ali caiu morto.
28 A mãe de Sísera olhava pela janela e exclamava pela grade: Por que tarda em vir o seu carro? Por que se demoram os passos dos seus cavalos?
29 As mais sábias das suas damas respondem, e até ela a si mesma respondia:
30 Porventura, não achariam e repartiriam despojos? Uma ou duas moças, a cada homem? Para Sísera, estofos de várias cores, estofos de várias cores de bordados; um ou dois estofos bordados, para o pescoço da esposa?
31 Assim, ó Senhor, pereçam todos os teus inimigos! Porém os que te amam brilham como o sol quando se levanta no seu esplendor. E a terra ficou em paz quarenta anos.*
1 Fizeram os filhos de Israel o que era mau perante o Senhor; por isso, o Senhor os entregou nas mãos dos midianitas por sete anos.
2 Prevalecendo o domínio dos midianitas sobre Israel, fizeram estes para si, por causa dos midianitas, as covas que estão nos montes, e as cavernas, e as fortificações.
3 Porque, cada vez que Israel semeava, os midianitas e os amalequitas, como também os povos do Oriente, subiam contra ele.
4 E contra ele se acampavam, destruindo os produtos da terra até à vizinhança de Gaza, e não deixavam em Israel sustento algum, nem ovelhas, nem bois, nem jumentos.
5 Pois subiam com os seus gados e tendas e vinham como gafanhotos, em tanta multidão, que não se podiam contar, nem a eles nem aos seus camelos; e entravam na terra para a destruir.
6 Assim, Israel ficou muito debilitado com a presença dos midianitas; então, os filhos de Israel clamavam ao Senhor.
7 Tendo os filhos de Israel clamado ao Senhor, por causa dos midianitas,
8 o Senhor lhes enviou um profeta, que lhes disse: Assim diz o Senhor, Deus de Israel: Eu é que vos fiz subir do Egito e vos tirei da casa da servidão;
9 e vos livrei da mão dos egípcios e da mão de todos quantos vos oprimiam; e os expulsei de diante de vós e vos dei a sua terra;
10 e disse: Eu sou o Senhor, vosso Deus; não temais os deuses dos amorreus, em cuja terra habitais; contudo, não destes ouvidos à minha voz.
11 Então, veio o Anjo do Senhor, e assentou-se debaixo do carvalho que está em Ofra, que pertencia a Joás, abiezrita; e Gideão, seu filho, estava malhando o trigo no lagar, para o pôr a salvo dos midianitas.
12 Então, o Anjo do Senhor lhe apareceu e lhe disse: O Senhor é contigo, homem valente.
13 Respondeu-lhe Gideão: Ai, senhor meu! Se o Senhor é conosco, por que nos sobreveio tudo isto? E que é feito de todas as suas maravilhas que nossos pais nos contaram, dizendo: Não nos fez o Senhor subir do Egito? Porém, agora, o Senhor nos desamparou e nos entregou nas mãos dos midianitas.
14 Então, se virou o Senhor para ele e disse: Vai nessa tua força e livra Israel da mão dos midianitas; porventura, não te enviei eu?
15 E ele lhe disse: Ai, Senhor meu! Com que livrarei Israel? Eis que a minha família é a mais pobre em Manassés, e eu, o menor na casa de meu pai.
16 Tornou-lhe o Senhor: Já que eu estou contigo, ferirás os midianitas como se fossem um só homem.
17 Ele respondeu: Se, agora, achei mercê diante dos teus olhos, dá-me um sinal de que és tu, Senhor, que me falas.
18 Rogo-te que daqui não te apartes até que eu volte, e traga a minha oferta, e a deponha perante ti. Respondeu ele: Esperarei até que voltes.
19 Entrou Gideão e preparou um cabrito e bolos asmos de um efa de farinha; a carne pôs num cesto, e o caldo, numa panela; e trouxe-lho até debaixo do carvalho e lho apresentou.
20 Porém o Anjo de Deus lhe disse: Toma a carne e os bolos asmos, põe-nos sobre esta penha e derrama-lhes por cima o caldo. E assim o fez.
21 Estendeu o Anjo do Senhor a ponta do cajado que trazia na mão e tocou a carne e os bolos asmos; então, subiu fogo da penha e consumiu a carne e os bolos; e o Anjo do Senhor desapareceu de sua presença.
22 Viu Gideão que era o Anjo do Senhor e disse: Ai de mim, Senhor Deus! Pois vi o Anjo do Senhor face a face.
23 Porém o Senhor lhe disse: Paz seja contigo! Não temas! Não morrerás!
24 Então, Gideão edificou ali um altar ao Senhor e lhe chamou de O Senhor É Paz. Ainda até ao dia de hoje está o altar em Ofra, que pertence aos abiezritas.
25 Naquela mesma noite, lhe disse o Senhor: Toma um boi que pertence a teu pai, a saber, o segundo boi de sete anos, e derriba o altar de Baal que é de teu pai, e corta o poste-ídolo que está junto ao altar.
26 Edifica ao Senhor, teu Deus, um altar no cimo deste baluarte, em camadas de pedra, e toma o segundo boi, e o oferecerás em holocausto com a lenha do poste-ídolo que vieres a cortar.
27 Então, Gideão tomou dez homens dentre os seus servos e fez como o Senhor lhe dissera; temendo ele, porém, a casa de seu pai e os homens daquela cidade, não o fez de dia, mas de noite.
28 Levantando-se, pois, de madrugada, os homens daquela cidade, eis que estava o altar de Baal derribado, e o poste-ídolo que estava junto dele, cortado; e o referido segundo boi fora oferecido no altar edificado.
29 E uns aos outros diziam: Quem fez isto? E, perguntando e inquirindo, disseram: Gideão, o filho de Joás, fez esta coisa.
30 Então, os homens daquela cidade disseram a Joás: Leva para fora o teu filho, para que morra; pois derribou o altar de Baal e cortou o poste-ídolo que estava junto dele.
31 Porém Joás disse a todos os que se puseram contra ele: Contendereis vós por Baal? Livrá-lo-eis vós? Qualquer que por ele contender, ainda esta manhã, será morto. Se é deus, que por si mesmo contenda; pois derribaram o seu altar.
32 Naquele dia, Gideão passou a ser chamado Jerubaal, porque foi dito: Baal contenda contra ele, pois ele derribou o seu altar.
33 E todos os midianitas, e amalequitas, e povos do Oriente se ajuntaram, e passaram, e se acamparam no vale de Jezreel.
34 Então, o Espírito do Senhor revestiu a Gideão, o qual tocou a rebate, e os abiezritas se ajuntaram após dele.
35 Enviou mensageiros por toda a tribo de Manassés, que também foi convocada para o seguir; enviou ainda mensageiros a Aser, e a Zebulom, e a Naftali, e saíram para encontrar-se com ele.
36 Disse Gideão a Deus: Se hás de livrar a Israel por meu intermédio, como disseste,
37 eis que eu porei uma porção de lã na eira; se o orvalho estiver somente nela, e seca a terra ao redor, então, conhecerei que hás de livrar Israel por meu intermédio, como disseste.
38 E assim sucedeu, porque, ao outro dia, se levantou de madrugada e, apertando a lã, do orvalho dela espremeu uma taça cheia de água.
39 Disse mais Gideão: Não se acenda contra mim a tua ira, se ainda falar só esta vez; rogo-te que mais esta vez faça eu a prova com a lã; que só a lã esteja seca, e na terra ao redor haja orvalho.
40 E Deus assim o fez naquela noite, pois só a lã estava seca, e sobre a terra ao redor havia orvalho.*
1 Então, Jerubaal, que é Gideão, se levantou de madrugada, e todo o povo que com ele estava, e se acamparam junto à fonte de Harode, de maneira que o arraial dos midianitas lhe ficava para o norte, no vale, defronte do outeiro de Moré.
2 Disse o Senhor a Gideão: É demais o povo que está contigo, para eu entregar os midianitas nas suas mãos; Israel poderia se gloriar contra mim, dizendo: A minha própria mão me livrou.
3 Apregoa, pois, aos ouvidos do povo, dizendo: Quem for tímido e medroso, volte e retire-se da região montanhosa de Gileade. Então, voltaram do povo vinte e dois mil, e dez mil ficaram.
4 Disse mais o Senhor a Gideão: Ainda há povo demais; faze-os descer às águas, e ali tos provarei; aquele de quem eu te disser: este irá contigo, esse contigo irá; porém todo aquele de quem eu te disser: este não irá contigo, esse não irá.
5 Fez Gideão descer os homens às águas. Então, o Senhor lhe disse: Todo que lamber a água com a língua, como faz o cão, esse porás à parte, como também a todo aquele que se abaixar de joelhos a beber.
6 Foi o número dos que lamberam, levando a mão à boca, trezentos homens; e todo o restante do povo se abaixou de joelhos a beber a água.
7 Então, disse o Senhor a Gideão: Com estes trezentos homens que lamberam a água eu vos livrarei, e entregarei os midianitas nas tuas mãos; pelo que a outra gente toda que se retire, cada um para o seu lugar.
8 Tomou o povo provisões nas mãos e as trombetas. Gideão enviou todos os homens de Israel cada um à sua tenda, porém os trezentos homens reteve consigo. Estava o arraial dos midianitas abaixo dele, no vale.
9 Sucedeu que, naquela mesma noite, o Senhor lhe disse: Levanta-te e desce contra o arraial, porque o entreguei nas tuas mãos.
10 Se ainda temes atacar, desce tu com teu moço Pura ao arraial;
11 e ouvirás o que dizem; depois, fortalecidas as tuas mãos, descerás contra o arraial. Então, desceu ele com seu moço Pura até à vanguarda do arraial.
12 Os midianitas, os amalequitas e todos os povos do Oriente cobriam o vale como gafanhotos em multidão; e eram os seus camelos em multidão inumerável como a areia que há na praia do mar.
13 Chegando, pois, Gideão, eis que certo homem estava contando um sonho ao seu companheiro e disse: Tive um sonho. Eis que um pão de cevada rodava contra o arraial dos midianitas e deu de encontro à tenda do comandante, de maneira que esta caiu, e se virou de cima para baixo, e ficou assim estendida.
14 Respondeu-lhe o companheiro e disse: Não é isto outra coisa, senão a espada de Gideão, filho de Joás, homem israelita. Nas mãos dele entregou Deus os midianitas e todo este arraial.
15 Tendo ouvido Gideão contar este sonho e o seu significado, adorou; e tornou ao arraial de Israel e disse: Levantai-vos, porque o Senhor entregou o arraial dos midianitas nas vossas mãos.
16 Então, repartiu os trezentos homens em três companhias e deu-lhes, a cada um nas suas mãos, trombetas e cântaros vazios, com tochas neles.
17 E disse-lhes: Olhai para mim e fazei como eu fizer. Chegando eu às imediações do arraial, como fizer eu, assim fareis.
18 Quando eu tocar a trombeta, e todos os que comigo estiverem, então, vós também tocareis a vossa ao redor de todo o arraial e direis: Pelo Senhor e por Gideão!
19 Chegou, pois, Gideão e os cem homens que com ele iam às imediações do arraial, ao princípio da vigília média, havendo-se pouco tempo antes trocado as guardas; e tocaram as trombetas e quebraram os cântaros que traziam nas mãos.
20 Assim, tocaram as três companhias as trombetas e despedaçaram os cântaros; e seguravam na mão esquerda as tochas e na mão direita, as trombetas que tocavam; e exclamaram: Espada pelo Senhor e por Gideão!
21 E permaneceu cada um no seu lugar ao redor do arraial, que todo deitou a correr, e a gritar, e a fugir.
22 Ao soar das trezentas trombetas, o Senhor tornou a espada de um contra o outro, e isto em todo o arraial, que fugiu rumo de Zererá, até Bete-Sita, até ao limite de Abel-Meolá, acima de Tabate.
23 Então, os homens de Israel, de Naftali e de Aser e de todo o Manassés foram convocados e perseguiram os midianitas.
24 Gideão enviou mensageiros a todas as montanhas de Efraim, dizendo: Descei de encontro aos midianitas e impedi-lhes a passagem pelas águas do Jordão até Bete-Bara. Convocados, pois, todos os homens de Efraim, cortaram-lhes a passagem pelo Jordão, até Bete-Bara.
25 E prenderam a dois príncipes dos midianitas, Orebe e Zeebe; mataram Orebe na penha de Orebe e Zeebe mataram no lagar de Zeebe. Perseguiram aos midianitas e trouxeram as cabeças de Orebe e de Zeebe a Gideão, dalém do Jordão.*
1 Então, os homens de Efraim disseram a Gideão: Que é isto que nos fizeste, que não nos chamaste quando foste pelejar contra os midianitas? E contenderam fortemente com ele.
2 Porém ele lhes disse: Que mais fiz eu, agora, do que vós? Não são, porventura, os rabiscos de Efraim melhores do que a vindima de Abiezer?
3 Deus entregou nas vossas mãos os príncipes dos midianitas, Orebe e Zeebe; que pude eu fazer comparável com o que fizestes? Então, com falar-lhes esta palavra, abrandou-se-lhes a ira para com ele.
4 Vindo Gideão ao Jordão, passou com os trezentos homens que com ele estavam, cansados mas ainda perseguindo.
5 E disse aos homens de Sucote: Dai, peço-vos, alguns pães para estes que me seguem, pois estão cansados, e eu vou ao encalço de Zeba e Salmuna, reis dos midianitas.
6 Porém os príncipes de Sucote disseram: Porventura, tens já sob teu poder o punho de Zeba e de Salmuna, para que demos pão ao teu exército?
7 Então, disse Gideão: Por isso, quando o Senhor entregar nas minhas mãos Zeba e Salmuna, trilharei a vossa carne com os espinhos do deserto e com os abrolhos.
8 Dali subiu a Penuel e de igual modo falou a seus homens; estes de Penuel lhe responderam como os homens de Sucote lhe haviam respondido.
9 Pelo que também falou aos homens de Penuel, dizendo: Quando eu voltar em paz, derribarei esta torre.
10 Estavam, pois, Zeba e Salmuna em Carcor, e os seus exércitos, com eles, uns quinze mil homens, todos os que restaram do exército de povos do Oriente; e os que caíram foram cento e vinte mil homens que puxavam da espada.
11 Subiu Gideão pelo caminho dos nômades, ao oriente de Noba e Jogbeá, e feriu aquele exército, que se achava descuidado.
12 Fugiram Zeba e Salmuna; porém ele os perseguiu, e prendeu os dois reis dos midianitas, Zeba e Salmuna, e desbaratou todo o exército.
13 Voltando, pois, Gideão, filho de Joás, da peleja, pela subida de Heres,
14 deteve a um moço de Sucote e lhe fez perguntas; o moço deu por escrito o nome dos príncipes e anciãos de Sucote, setenta e sete homens.
15 Então, veio Gideão aos homens de Sucote e disse: Vedes aqui Zeba e Salmuna, a respeito dos quais motejastes de mim, dizendo: Porventura, tens tu já sob teu poder o punho de Zeba e Salmuna para que demos pão aos teus homens cansados?
16 E tomou os anciãos da cidade, e espinhos do deserto, e abrolhos e, com eles, deu severa lição aos homens de Sucote.
17 Derribou a torre de Penuel e matou os homens da cidade.
18 Depois disse a Zeba e a Salmuna: Que homens eram os que matastes em Tabor? Responderam: Como tu és, assim eram eles; cada um se assemelhava a filho de rei.
19 Então, disse ele: Eram meus irmãos, filhos de minha mãe. Tão certo como vive o Senhor, se os tivésseis deixado com vida, eu não vos mataria a vós outros.
20 E disse a Jéter, seu primogênito: Dispõe-te e mata-os. Porém o moço não arrancou da sua espada, porque temia, porquanto ainda era jovem.
21 Então, disseram Zeba e Salmuna: Levanta-te e arremete contra nós, porque qual o homem, tal a sua valentia. Dispôs-se, pois, Gideão, e matou a Zeba e a Salmuna, e tomou os ornamentos em forma de meia-lua que estavam no pescoço dos seus camelos.
22 Então, os homens de Israel disseram a Gideão: Domina sobre nós, tanto tu como teu filho e o filho de teu filho, porque nos livraste do poder dos midianitas.
23 Porém Gideão lhes disse: Não dominarei sobre vós, nem tampouco meu filho dominará sobre vós; o Senhor vos dominará.
24 Disse-lhes mais Gideão: Um pedido vos farei: dai-me vós, cada um as argolas do seu despojo (porque tinham argolas de ouro, pois eram ismaelitas).
25 Disseram eles: De bom grado as daremos. E estenderam uma capa, e cada um deles deitou ali uma argola do seu despojo.
26 O peso das argolas de ouro que pediu foram mil e setecentos siclos de ouro (afora os ornamentos em forma de meia-lua, as arrecadas e as vestes de púrpura que traziam os reis dos midianitas, e afora os ornamentos que os camelos traziam ao pescoço).
27 Desse peso fez Gideão uma estola sacerdotal e a pôs na sua cidade, em Ofra; e todo o Israel se prostituiu ali após ela; a estola veio a ser um laço a Gideão e à sua casa.
28 Assim, foram abatidos os midianitas diante dos filhos de Israel e nunca mais levantaram a cabeça; e ficou a terra em paz durante quarenta anos nos dias de Gideão.
29 Retirou-se Jerubaal, filho de Joás, e habitou em sua casa.
30 Teve Gideão setenta filhos, todos provindos dele, porque tinha muitas mulheres.
31 A sua concubina, que estava em Siquém, lhe deu também à luz um filho; e ele lhe pôs por nome Abimeleque.
32 Faleceu Gideão, filho de Joás, em boa velhice; e foi sepultado no sepulcro de Joás, seu pai, em Ofra dos abiezritas.
33 Morto Gideão, tornaram a prostituir-se os filhos de Israel após os baalins e puseram Baal-Berite por deus.
34 Os filhos de Israel não se lembraram do Senhor, seu Deus, que os livrara do poder de todos os seus inimigos ao redor;
35 nem usaram de benevolência com a casa de Jerubaal, a saber, Gideão, segundo todo o bem que ele fizera a Israel.*
1 Abimeleque, filho de Jerubaal, foi-se a Siquém, aos irmãos de sua mãe, e falou-lhes e a toda a geração da casa do pai de sua mãe, dizendo:
2 Falai, peço-vos, aos ouvidos de todos os cidadãos de Siquém: Que vos parece melhor: que setenta homens, todos os filhos de Jerubaal, dominem sobre vós ou que apenas um domine sobre vós? Lembrai-vos também de que sou osso vosso e carne vossa.
3 Então, os irmãos de sua mãe falaram a todos os cidadãos de Siquém todas aquelas palavras; e o coração deles se inclinou a seguir Abimeleque, porque disseram: É nosso irmão.
4 E deram-lhe setenta peças de prata, da casa de Baal-Berite, com as quais alugou Abimeleque uns homens levianos e atrevidos, que o seguiram.
5 Foi à casa de seu pai, a Ofra, e matou seus irmãos, os filhos de Jerubaal, setenta homens, sobre uma pedra. Porém Jotão, filho menor de Jerubaal, ficou, porque se escondera.
6 Então, se ajuntaram todos os cidadãos de Siquém e toda Bete-Milo; e foram e proclamaram Abimeleque rei, junto ao carvalho memorial que está perto de Siquém.
7 Avisado disto, Jotão foi, e se pôs no cimo do monte Gerizim, e em alta voz clamou, e disse-lhes: Ouvi-me, cidadãos de Siquém, e Deus vos ouvirá a vós outros.
8 Foram, certa vez, as árvores ungir para si um rei e disseram à oliveira: Reina sobre nós.
9 Porém a oliveira lhes respondeu: Deixaria eu o meu óleo, que Deus e os homens em mim prezam, e iria pairar sobre as árvores?
10 Então, disseram as árvores à figueira: Vem tu e reina sobre nós.
11 Porém a figueira lhes respondeu: Deixaria eu a minha doçura, o meu bom fruto e iria pairar sobre as árvores?
12 Então, disseram as árvores à videira: Vem tu e reina sobre nós.
13 Porém a videira lhes respondeu: Deixaria eu o meu vinho, que agrada a Deus e aos homens, e iria pairar sobre as árvores?
14 Então, todas as árvores disseram ao espinheiro: Vem tu e reina sobre nós.
15 Respondeu o espinheiro às árvores: Se, deveras, me ungis rei sobre vós, vinde e refugiai-vos debaixo de minha sombra; mas, se não, saia do espinheiro fogo que consuma os cedros do Líbano.
16 Agora, pois, se, deveras e sinceramente, procedestes, proclamando rei Abimeleque, e se bem vos portastes para com Jerubaal e para com a sua casa, e se com ele agistes segundo o merecimento dos seus feitos
17 (porque meu pai pelejou por vós e, arriscando a vida, vos livrou das mãos dos midianitas;
18 porém vós, hoje, vos levantastes contra a casa de meu pai e matastes seus filhos, setenta homens, sobre uma pedra; e a Abimeleque, filho de sua serva, fizestes reinar sobre os cidadãos de Siquém, porque é vosso irmão),
19 se, deveras e sinceramente, procedestes, hoje, com Jerubaal e com a sua casa, alegrai-vos com Abimeleque, e também ele se alegre convosco.
20 Mas, se não, saia fogo de Abimeleque e consuma os cidadãos de Siquém e Bete-Milo; e saia fogo dos cidadãos de Siquém e de Bete-Milo, que consuma a Abimeleque.
21 Fugiu logo Jotão, e foi-se para Beer, e ali habitou por temer seu irmão Abimeleque.
22 Havendo, pois, Abimeleque dominado três anos sobre Israel,
23 suscitou Deus um espírito de aversão entre Abimeleque e os cidadãos de Siquém; e estes se houveram aleivosamente contra Abimeleque,
24 para que a vingança da violência praticada contra os setenta filhos de Jerubaal viesse, e o seu sangue caísse sobre Abimeleque, seu irmão, que os matara, e sobre os cidadãos de Siquém, que contribuíram para que ele matasse seus próprios irmãos.
25 Os cidadãos de Siquém puseram contra ele homens de emboscada sobre os cimos dos montes; e todo aquele que passava pelo caminho junto a eles, eles o assaltavam; e isto se contou a Abimeleque.
26 Veio também Gaal, filho de Ebede, com seus irmãos, e se estabeleceram em Siquém; e os cidadãos de Siquém confiaram nele,
27 e saíram ao campo, e vindimaram as suas vinhas, e pisaram as uvas, e fizeram festas, e foram à casa de seu deus, e comeram, e beberam, e amaldiçoaram Abimeleque.
28 Disse Gaal, filho de Ebede: Quem é Abimeleque, e quem somos nós de Siquém, para que o sirvamos? Não é, porventura, filho de Jerubaal? E não é Zebul o seu oficial? Servi, antes, aos homens de Hamor, pai de Siquém. Mas nós, por que serviremos a ele?
29 Quem dera estivesse este povo sob a minha mão, e eu expulsaria Abimeleque e lhe diria: Multiplica o teu exército e sai.
30 Ouvindo Zebul, governador da cidade, as palavras de Gaal, filho de Ebede, se acendeu em ira;
31 e enviou, astutamente, mensageiros a Abimeleque, dizendo: Eis que Gaal, filho de Ebede, e seus irmãos vieram a Siquém e alvoroçaram a cidade contra ti.
32 Levanta-te, pois, de noite, tu e o povo que tiveres contigo, e ponde-vos de emboscada no campo.
33 Levanta-te pela manhã, ao sair o sol, e dá de golpe sobre a cidade; saindo contra ti Gaal com a sua gente, procede com ele como puderes.
34 Levantou-se, pois, de noite, Abimeleque e todo o povo que com ele estava, e se puseram de emboscada contra Siquém, em quatro grupos.
35 Gaal, filho de Ebede, saiu e pôs-se à entrada da porta da cidade; com isto Abimeleque e todo o povo que com ele estava se levantaram das emboscadas.
36 Vendo Gaal aquele povo, disse a Zebul: Eis que desce gente dos cimos dos montes. Zebul, ao contrário, lhe disse: As sombras dos montes vês por homens.
37 Porém Gaal tornou ainda a falar e disse: Eis ali desce gente defronte de nós, e uma tropa vem do caminho do carvalho dos Adivinhadores.
38 Então, lhe disse Zebul: Onde está, agora, a tua boca, com a qual dizias: Quem é Abimeleque, para que o sirvamos? Não é este, porventura, o povo que desprezaste? Sai, pois, e peleja contra ele.
39 Saiu Gaal adiante dos cidadãos de Siquém e pelejou contra Abimeleque.
40 Abimeleque o perseguiu; Gaal fugiu de diante dele, e muitos feridos caíram até a entrada da porta da cidade.
41 Abimeleque ficou em Arumá. E Zebul expulsou a Gaal e seus irmãos, para que não habitassem em Siquém.
42 No dia seguinte, saiu o povo ao campo; disto foi avisado Abimeleque,
43 que tomou os seus homens, e os repartiu em três grupos, e os pôs de emboscada no campo. Olhando, viu que o povo saía da cidade; então, se levantou contra eles e os feriu.
44 Abimeleque e o grupo que com ele estava romperam de improviso e tomaram posição à porta da cidade, enquanto os dois outros grupos deram de golpe sobre todos quantos estavam no campo e os destroçaram.
45 Todo aquele dia pelejou Abimeleque contra a cidade e a tomou. Matou o povo que nela havia, assolou-a e a semeou de sal.
46 Tendo ouvido isto todos os cidadãos da Torre de Siquém, entraram na fortaleza subterrânea, no templo de El-Berite.
47 Contou-se a Abimeleque que todos os cidadãos da Torre de Siquém se haviam congregado.
48 Então, subiu ele ao monte Salmom, ele e todo o seu povo; Abimeleque tomou de um machado, e cortou uma ramada de árvore, e a levantou, e pô-la ao ombro, e disse ao povo que com ele estava: O que me vistes fazer, fazei-o também vós, depressa.
49 Assim, cada um de todo o povo cortou a sua ramada, e seguiram Abimeleque, e as puseram em cima da fortaleza subterrânea, e queimaram sobre todos os da Torre de Siquém, de maneira que morreram todos, uns mil homens e mulheres.
50 Então, se foi Abimeleque a Tebes, e a sitiou, e a tomou.
51 Havia, porém, no meio da cidade, uma torre forte; e todos os homens e mulheres, todos os moradores da cidade, se acolheram a ela, e fecharam após si as portas da torre, e subiram ao seu eirado.
52 Abimeleque veio até à torre, pelejou contra ela e se chegou até à sua porta para a incendiar.
53 Porém certa mulher lançou uma pedra superior de moinho sobre a cabeça de Abimeleque e lhe quebrou o crânio.
54 Então, chamou logo ao moço, seu escudeiro, e lhe disse: Desembainha a tua espada e mata-me, para que não se diga de mim: Mulher o matou. O moço o atravessou, e ele morreu.
55 Vendo, pois, os homens de Israel que Abimeleque já estava morto, foram-se, cada um para sua casa.
56 Assim, Deus fez tornar sobre Abimeleque o mal que fizera a seu pai, por ter aquele matado os seus setenta irmãos.
57 De igual modo, todo o mal dos homens de Siquém Deus fez cair sobre a cabeça deles. Assim, veio sobre eles a maldição de Jotão, filho de Jerubaal.*
1 Depois de Abimeleque, se levantou, para livrar Israel, Tola, filho de Puá, filho de Dodô, homem de Issacar; e habitava em Samir, na região montanhosa de Efraim.
2 Julgou a Israel vinte e três anos, e morreu, e foi sepultado em Samir.
3 Depois dele, se levantou Jair, gileadita, e julgou a Israel vinte e dois anos.
4 Tinha este trinta filhos, que cavalgavam trinta jumentos; e tinham trinta cidades, a que chamavam Havote-Jair, até ao dia de hoje, as quais estão na terra de Gileade.
5 Morreu Jair e foi sepultado em Camom.
6 Tornaram os filhos de Israel a fazer o que era mau perante o Senhor e serviram aos baalins, e a Astarote, e aos deuses da Síria, e aos de Sidom, de Moabe, dos filhos de Amom e dos filisteus; deixaram o Senhor e não o serviram.
7 Acendeu-se a ira do Senhor contra Israel, e entregou-os nas mãos dos filisteus e nas mãos dos filhos de Amom,
8 os quais, nesse mesmo ano, vexaram e oprimiram os filhos de Israel. Por dezoito anos, oprimiram a todos os filhos de Israel que estavam dalém do Jordão, na terra dos amorreus, que está em Gileade.
9 Os filhos de Amom passaram o Jordão para pelejar também contra Judá, e contra Benjamim, e contra a casa de Efraim, de maneira que Israel se viu muito angustiado.
10 Então, os filhos de Israel clamaram ao Senhor, dizendo: Contra ti havemos pecado, porque deixamos o nosso Deus e servimos aos baalins.
11 Porém o Senhor disse aos filhos de Israel: Quando os egípcios, e os amorreus, e os filhos de Amom, e os filisteus,
12 e os sidônios, e os amalequitas, e os maonitas vos oprimiam, e vós clamáveis a mim, não vos livrei eu das suas mãos?
13 Contudo, vós me deixastes a mim e servistes a outros deuses, pelo que não vos livrarei mais.
14 Ide e clamai aos deuses que escolhestes; eles que vos livrem no tempo do vosso aperto.
15 Mas os filhos de Israel disseram ao Senhor: Temos pecado; faze-nos tudo quanto te parecer bem; porém livra-nos ainda esta vez, te rogamos.
16 E tiraram os deuses alheios do meio de si e serviram ao Senhor; então, já não pôde ele reter a sua compaixão por causa da desgraça de Israel.
17 Tendo sido convocados os filhos de Amom, acamparam-se em Gileade; mas os filhos de Israel se congregaram e se acamparam em Mispa.
18 Então, o povo, aliás, os príncipes de Gileade, disseram uns aos outros: Quem será o homem que começará a pelejar contra os filhos de Amom? Será esse o cabeça de todos os moradores de Gileade.*
1 Era, então, Jefté, o gileadita, homem valente, porém filho de uma prostituta; Gileade gerara a Jefté.
2 Também a mulher de Gileade lhe deu filhos, os quais, quando já grandes, expulsaram Jefté e lhe disseram: Não herdarás em casa de nosso pai, porque és filho doutra mulher.
3 Então, Jefté fugiu da presença de seus irmãos e habitou na terra de Tobe; e homens levianos se ajuntaram com ele e com ele saíam.
4 Passado algum tempo, pelejaram os filhos de Amom contra Israel.
5 Quando pelejavam, foram os anciãos de Gileade buscar Jefté da terra de Tobe.
6 E disseram a Jefté: Vem e sê nosso chefe, para que combatamos contra os filhos de Amom.
7 Porém Jefté disse aos anciãos de Gileade: Porventura, não me aborrecestes a mim e não me expulsastes da casa de meu pai? Por que, pois, vindes a mim, agora, quando estais em aperto?
8 Responderam os anciãos de Gileade a Jefté: Por isso mesmo, tornamos a ti. Vem, pois, conosco, e combate contra os filhos de Amom, e sê o nosso chefe sobre todos os moradores de Gileade.
9 Então, Jefté perguntou aos anciãos de Gileade: Se me tornardes a levar para combater contra os filhos de Amom, e o Senhor mos der a mim, então, eu vos serei por cabeça?
10 Responderam os anciãos de Gileade a Jefté: O Senhor será testemunha entre nós e nos castigará se não fizermos segundo a tua palavra.
11 Então, Jefté foi com os anciãos de Gileade, e o povo o pôs por cabeça e chefe sobre si; e Jefté proferiu todas as suas palavras perante o Senhor, em Mispa.
12 Enviou Jefté mensageiros ao rei dos filhos de Amom, dizendo: Que há entre mim e ti que vieste a mim a pelejar contra a minha terra?
13 Respondeu o rei dos filhos de Amom aos mensageiros de Jefté: É porque, subindo Israel do Egito, me tomou a terra desde Arnom até ao Jaboque e ainda até ao Jordão; restitui-ma, agora, pacificamente.
14 Porém Jefté tornou a enviar mensageiros ao rei dos filhos de Amom,
15 dizendo-lhe: Assim diz Jefté: Israel não tomou nem a terra dos moabitas nem a terra dos filhos de Amom;
16 porque, subindo Israel do Egito, andou pelo deserto até ao mar Vermelho e chegou a Cades.
17 Então, Israel enviou mensageiros ao rei dos edomitas, dizendo: Rogo-te que me deixes passar pela tua terra. Porém o rei dos edomitas não lhe deu ouvidos; a mesma coisa mandou Israel pedir ao rei dos moabitas, o qual também não lhe quis atender; e, assim, Israel ficou em Cades.
18 Depois, andou pelo deserto, e rodeou a terra dos edomitas e a terra dos moabitas, e chegou ao oriente da terra destes, e se acampou além do Arnom; por isso, não entrou no território dos moabitas, porque Arnom é o limite deles.
19 Mas Israel enviou mensageiros a Seom, rei dos amorreus, rei de Hesbom; e disse-lhe: Deixa-nos, peço-te, passar pela tua terra até ao meu lugar.
20 Porém Seom, não confiando em Israel, recusou deixá-lo passar pelo seu território; pelo contrário, ajuntou todo o seu povo, e se acampou em Jaza, e pelejou contra Israel.
21 O Senhor, Deus de Israel, entregou Seom e todo o seu povo nas mãos de Israel, que os feriu; e Israel desapossou os amorreus das terras que habitavam.
22 Tomou posse de todo o território dos amorreus, desde o Arnom até ao Jaboque e desde o deserto até ao Jordão.
23 Assim, o Senhor, Deus de Israel, desapossou os amorreus ante o seu povo de Israel. E pretendes tu ser dono desta terra?
24 Não é certo que aquilo que Quemos, teu deus, te dá consideras como tua possessão? Assim, possuiremos nós o território de todos quantos o Senhor, nosso Deus, expulsou de diante de nós.
25 És tu melhor do que o filho de Zipor, Balaque, rei dos moabitas? Porventura, contendeu este, em algum tempo, com Israel ou pelejou alguma vez contra ele?
26 Enquanto Israel habitou trezentos anos em Hesbom e nas suas vilas, e em Aroer e nas suas vilas, e em todas as cidades que estão ao longe do Arnom, por que vós, amonitas, não as recuperastes durante esse tempo?
27 Não sou eu, portanto, quem pecou contra ti! Porém tu fazes mal em pelejar contra mim; o Senhor, que é juiz, julgue hoje entre os filhos de Israel e os filhos de Amom.
28 Porém o rei dos filhos de Amom não deu ouvidos à mensagem que Jefté lhe enviara.
29 Então, o Espírito do Senhor veio sobre Jefté; e, atravessando este por Gileade e Manassés, passou até Mispa de Gileade e de Mispa de Gileade passou contra os filhos de Amom.
30 Fez Jefté um voto ao Senhor e disse: Se, com efeito, me entregares os filhos de Amom nas minhas mãos,
31 quem primeiro da porta da minha casa me sair ao encontro, voltando eu vitorioso dos filhos de Amom, esse será do Senhor, e eu o oferecerei em holocausto.
32 Assim, Jefté foi de encontro aos filhos de Amom, a combater contra eles; e o Senhor os entregou nas mãos de Jefté.
33 Este os derrotou desde Aroer até às proximidades de Minite (vinte cidades ao todo) e até Abel-Queramim; e foi mui grande a derrota. Assim, foram subjugados os filhos de Amom diante dos filhos de Israel.
34 Vindo, pois, Jefté a Mispa, a sua casa, saiu-lhe a filha ao seu encontro, com adufes e com danças; e era ela filha única; não tinha ele outro filho nem filha.
35 Quando a viu, rasgou as suas vestes e disse: Ah! Filha minha, tu me prostras por completo; tu passaste a ser a causa da minha calamidade, porquanto fiz voto ao Senhor e não tornarei atrás.
36 E ela lhe disse: Pai meu, fizeste voto ao Senhor; faze, pois, de mim segundo o teu voto; pois o Senhor te vingou dos teus inimigos, os filhos de Amom.
37 Disse mais a seu pai: Concede-me isto: deixa-me por dois meses, para que eu vá, e desça pelos montes, e chore a minha virgindade, eu e as minhas companheiras.
38 Consentiu ele: Vai. E deixou-a ir por dois meses; então, se foi ela com as suas companheiras e chorou a sua virgindade pelos montes.
39 Ao fim dos dois meses, tornou ela para seu pai, o qual lhe fez segundo o voto por ele proferido; assim, ela jamais foi possuída por varão. Daqui veio o costume em Israel
40 de as filhas de Israel saírem por quatro dias, de ano em ano, a cantar em memória da filha de Jefté, o gileadita.*
1 Então, foram convocados os homens de Efraim, e passaram para Zafom, e disseram a Jefté: Por que foste combater contra os filhos de Amom e não nos chamaste para ir contigo? Queimaremos a tua casa, estando tu dentro dela.
2 E Jefté lhes disse: Eu e o meu povo tivemos grande contenda com os filhos de Amom; chamei-vos, e não me livrastes das suas mãos.
3 Vendo eu que não me livráveis, arrisquei a minha vida e passei contra os filhos de Amom, e o Senhor os entregou nas minhas mãos; por que, pois, subistes, hoje, contra mim, para me combaterdes?
4 Ajuntou Jefté todos os homens de Gileade e pelejou contra Efraim; e os homens de Gileade feriram Efraim, porque este dissera: Fugitivos sois de Efraim, vós, gileaditas, que morais no meio de Efraim e Manassés.
5 Porém os gileaditas tomaram os vaus do Jordão que conduzem a Efraim; de sorte que, quando qualquer fugitivo de Efraim dizia: Quero passar; então, os homens de Gileade lhe perguntavam: És tu efraimita? Se respondia: Não;
6 então, lhe tornavam: Dize, pois, chibolete; quando dizia sibolete, não podendo exprimir bem a palavra, então, pegavam dele e o matavam nos vaus do Jordão. E caíram de Efraim, naquele tempo, quarenta e dois mil.
7 Jefté, o gileadita, julgou a Israel seis anos; e morreu e foi sepultado numa das cidades de Gileade.
8 Depois dele, julgou a Israel Ibsã, de Belém.
9 Tinha este trinta filhos e trinta filhas; a estas, casou fora; e, de fora, trouxe trinta mulheres para seus filhos. Julgou a Israel sete anos.
10 Então, faleceu Ibsã e foi sepultado em Belém.
11 Depois dele, veio Elom, o zebulonita, que julgou a Israel dez anos.
12 Faleceu Elom, o zebulonita, e foi sepultado em Aijalom, na terra de Zebulom.
13 Depois dele, julgou a Israel Abdom, filho de Hilel, o piratonita.
14 Tinha este quarenta filhos e trinta netos, que cavalgavam setenta jumentos. Julgou a Israel oito anos.
15 Então, faleceu Abdom, filho de Hilel, o piratonita; e foi sepultado em Piratom, na terra de Efraim, na região montanhosa dos amalequitas.*
1 Tendo os filhos de Israel tornado a fazer o que era mau perante o Senhor, este os entregou nas mãos dos filisteus por quarenta anos.
2 Havia um homem de Zorá, da linhagem de Dã, chamado Manoá, cuja mulher era estéril e não tinha filhos.
3 Apareceu o Anjo do Senhor a esta mulher e lhe disse: Eis que és estéril e nunca tiveste filho; porém conceberás e darás à luz um filho.
4 Agora, pois, guarda-te, não bebas vinho ou bebida forte, nem comas coisa imunda;
5 porque eis que tu conceberás e darás à luz um filho sobre cuja cabeça não passará navalha; porquanto o menino será nazireu consagrado a Deus desde o ventre de sua mãe; e ele começará a livrar a Israel do poder dos filisteus.
6 Então, a mulher foi a seu marido e lhe disse: Um homem de Deus veio a mim; sua aparência era semelhante à de um anjo de Deus, tremenda; não lhe perguntei donde era, nem ele me disse o seu nome.
7 Porém me disse: Eis que tu conceberás e darás à luz um filho; agora, pois, não bebas vinho, nem bebida forte, nem comas coisa imunda; porque o menino será nazireu consagrado a Deus, desde o ventre materno até ao dia de sua morte.
8 Então, Manoá orou ao Senhor e disse: Ah! Senhor meu, rogo-te que o homem de Deus que enviaste venha outra vez e nos ensine o que devemos fazer ao menino que há de nascer.
9 Deus ouviu a voz de Manoá, e o Anjo de Deus veio outra vez à mulher, quando esta se achava assentada no campo; porém não estava com ela seu marido Manoá.
10 Apressou-se, pois, a mulher, e, correndo, noticiou-o a seu marido, e lhe disse: Eis que me apareceu aquele homem que viera a mim no outro dia.
11 Então, se levantou Manoá, e seguiu a sua mulher, e, tendo chegado ao homem, lhe disse: És tu o que falaste a esta mulher? Ele respondeu: Eu sou.
12 Então, disse Manoá: Quando se cumprirem as tuas palavras, qual será o modo de viver do menino e o seu serviço?
13 Respondeu-lhe o Anjo do Senhor: Guarde-se a mulher de tudo quanto eu lhe disse.
14 De tudo quanto procede da videira não comerá, nem vinho nem bebida forte beberá, nem coisa imunda comerá; tudo quanto lhe tenho ordenado guardará.
15 Então, Manoá disse ao Anjo do Senhor: Permite-nos deter-te, e te prepararemos um cabrito.
16 Porém o Anjo do Senhor disse a Manoá: Ainda que me detenhas, não comerei de teu pão; e, se preparares holocausto, ao Senhor o oferecerás. Porque não sabia Manoá que era o Anjo do Senhor.
17 Perguntou Manoá ao Anjo do Senhor: Qual é o teu nome, para que, quando se cumprir a tua palavra, te honremos?
18 Respondeu-lhe o Anjo do Senhor e lhe disse: Por que perguntas assim pelo meu nome, que é maravilhoso?
19 Tomou, pois, Manoá um cabrito e uma oferta de manjares e os apresentou sobre uma rocha ao Senhor; e o Anjo do Senhor se houve maravilhosamente. Manoá e sua mulher estavam observando.
20 Sucedeu que, subindo para o céu a chama que saiu do altar, o Anjo do Senhor subiu nela; o que vendo Manoá e sua mulher, caíram com o rosto em terra.
21 Nunca mais apareceu o Anjo do Senhor a Manoá, nem a sua mulher; então, Manoá ficou sabendo que era o Anjo do Senhor.
22 Disse Manoá a sua mulher: Certamente, morreremos, porque vimos a Deus.
23 Porém sua mulher lhe disse: Se o Senhor nos quisera matar, não aceitaria de nossas mãos o holocausto e a oferta de manjares, nem nos teria mostrado tudo isto, nem nos teria revelado tais coisas.
24 Depois, deu a mulher à luz um filho e lhe chamou Sansão; o menino cresceu, e o Senhor o abençoou.
25 E o Espírito do Senhor passou a incitá-lo em Maané-Dã, entre Zorá e Estaol.*
1 Desceu Sansão a Timna; vendo em Timna uma das filhas dos filisteus,
2 subiu, e declarou-o a seu pai e a sua mãe, e disse: Vi uma mulher em Timna, das filhas dos filisteus; tomai-ma, pois, por esposa.
3 Porém seu pai e sua mãe lhe disseram: Não há, porventura, mulher entre as filhas de teus irmãos ou entre todo o meu povo, para que vás tomar esposa dos filisteus, daqueles incircuncisos? Disse Sansão a seu pai: Toma-me esta, porque só desta me agrado.
4 Mas seu pai e sua mãe não sabiam que isto vinha do Senhor, pois este procurava ocasião contra os filisteus; porquanto, naquele tempo, os filisteus dominavam sobre Israel.
5 Desceu, pois, com seu pai e sua mãe a Timna; e, chegando às vinhas de Timna, eis que um leão novo, bramando, lhe saiu ao encontro.
6 Então, o Espírito do Senhor de tal maneira se apossou dele, que ele o rasgou como quem rasga um cabrito, sem nada ter na mão; todavia, nem a seu pai nem a sua mãe deu a saber o que fizera.
7 Desceu, e falou àquela mulher, e dela se agradou.
8 Depois de alguns dias, voltou ele para a tomar; e, apartando-se do caminho para ver o corpo do leão morto, eis que, neste, havia um enxame de abelhas com mel.
9 Tomou o favo nas mãos e se foi andando e comendo dele; e chegando a seu pai e a sua mãe, deu-lhes do mel, e comeram; porém não lhes deu a saber que do corpo do leão é que o tomara.
10 Descendo, pois, seu pai à casa daquela mulher, fez Sansão ali um banquete; porque assim o costumavam fazer os moços.
11 Sucedeu que, como o vissem, convidaram trinta companheiros para estarem com ele.
12 Disse-lhes, pois, Sansão: Dar-vos-ei um enigma a decifrar; se, nos sete dias das bodas, mo declarardes e descobrirdes, dar-vos-ei trinta camisas e trinta vestes festivais;
13 se mo não puderdes declarar, vós me dareis a mim as trinta camisas e as trinta vestes festivais. E eles lhe disseram: Dá-nos o teu enigma a decifrar, para que o ouçamos.
14 Então, lhes disse: Do comedor saiu comida, e do forte saiu doçura. E, em três dias, não puderam decifrar o enigma.
15 Ao sétimo dia, disseram à mulher de Sansão: Persuade a teu marido que nos declare o enigma, para que não queimemos a ti e a casa de teu pai. Convidastes-nos para vos apossardes do que é nosso, não é assim?
16 A mulher de Sansão chorou diante dele e disse: Tão somente me aborreces e não me amas; pois deste aos meus patrícios um enigma a decifrar e ainda não mo declaraste a mim. E ele lhe disse: Nem a meu pai nem a minha mãe o declarei e to declararia a ti?
17 Ela chorava diante dele os sete dias em que celebravam as bodas; ao sétimo dia, lhe declarou, porquanto o importunava; então, ela declarou o enigma aos seus patrícios.
18 Disseram, pois, a Sansão os homens daquela cidade, ao sétimo dia, antes de se pôr o sol: Que coisa há mais doce do que o mel e mais forte do que o leão? E ele lhes citou o provérbio: Se vós não lavrásseis com a minha novilha, nunca teríeis descoberto o meu enigma.
19 Então, o Espírito do Senhor de tal maneira se apossou dele, que desceu aos asquelonitas, matou deles trinta homens, despojou-os e as suas vestes festivais deu aos que declararam o enigma; porém acendeu-se a sua ira, e ele subiu à casa de seu pai.
20 Ao companheiro de honra de Sansão foi dada por mulher a esposa deste.*
1 Passado algum tempo, nos dias da ceifa do trigo, Sansão, levando um cabrito, foi visitar a sua mulher, pois dizia: Entrarei na câmara de minha mulher. Porém o pai dela não o deixou entrar
2 e lhe disse: Por certo, pensava eu que de todo a aborrecias, de sorte que a dei ao teu companheiro; porém não é mais formosa do que ela a irmã que é mais nova? Toma-a, pois, em seu lugar.
3 Então, Sansão lhe respondeu: Desta feita sou inocente para com os filisteus, quando lhes fizer algum mal.
4 E saiu e tomou trezentas raposas; e, tomando fachos, as virou cauda com cauda e lhes atou um facho no meio delas.
5 Tendo ele chegado fogo aos tições, largou-as na seara dos filisteus e, assim, incendiou tanto os molhos como o cereal por ceifar, e as vinhas, e os olivais.
6 Perguntaram os filisteus: Quem fez isto? Responderam: Sansão, o genro do timnita, porque lhe tomou a mulher e a deu a seu companheiro. Então, subiram os filisteus e queimaram a ela e o seu pai.
7 Disse-lhes Sansão: Se assim procedeis, não desistirei enquanto não me vingar.
8 E feriu-os com grande carnificina; e desceu e habitou na fenda da rocha de Etã.
9 Então, os filisteus subiram, e acamparam-se contra Judá, e estenderam-se por Leí.
10 Perguntaram-lhes os homens de Judá: Por que subistes contra nós? Responderam: Subimos para amarrar Sansão, para lhe fazer a ele como ele nos fez a nós.
11 Então, três mil homens de Judá desceram até à fenda da rocha de Etã e disseram a Sansão: Não sabias tu que os filisteus dominam sobre nós? Por que, pois, nos fizeste isto? Ele lhes respondeu: Assim como me fizeram a mim, eu lhes fiz a eles.
12 Descemos, replicaram eles, para te amarrar, para te entregar nas mãos dos filisteus. Sansão lhes disse: Jurai-me que vós mesmos não me acometereis.
13 Eles lhe disseram: Não, mas somente te amarraremos e te entregaremos nas suas mãos; porém de maneira nenhuma te mataremos. E amarraram-no com duas cordas novas e fizeram-no subir da rocha.
14 Chegando ele a Leí, os filisteus lhe saíram ao encontro, jubilando; porém o Espírito do Senhor de tal maneira se apossou dele, que as cordas que tinha nos braços se tornaram como fios de linho queimados, e as suas amarraduras se desfizeram das suas mãos.
15 Achou uma queixada de jumento, ainda fresca, à mão, e tomou-a, e feriu com ela mil homens.
16 E disse: Com uma queixada de jumento um montão, outro montão; com uma queixada de jumento feri mil homens.
17 Tendo ele acabado de falar, lançou da sua mão a queixada. Chamou-se aquele lugar Ramate-Leí.
18 Sentindo grande sede, clamou ao Senhor e disse: Por intermédio do teu servo deste esta grande salvação; morrerei eu, agora, de sede e cairei nas mãos destes incircuncisos?
19 Então, o Senhor fendeu a cavidade que estava em Leí, e dela saiu água; tendo Sansão bebido, recobrou alento e reviveu; daí chamar-se aquele lugar En-Hacoré até ao dia de hoje.
20 Sansão julgou a Israel, nos dias dos filisteus, vinte anos.*
1 Sansão foi a Gaza, e viu ali uma prostituta, e coabitou com ela.
2 Foi dito aos gazitas: Sansão chegou aqui. Cercaram-no, pois, e toda a noite o esperaram, às escondidas, na porta da cidade; e, toda a noite, estiveram em silêncio, pois diziam: Esperaremos até ao raiar do dia; então, daremos cabo dele.
3 Porém Sansão esteve deitado até à meia-noite; então, se levantou, e pegou ambas as folhas da porta da cidade com suas ombreiras, e, juntamente com a tranca, as tomou, pondo-as sobre os ombros; e levou-as para cima, até ao cimo do monte que olha para Hebrom.
4 Depois disto, aconteceu que se afeiçoou a uma mulher do vale de Soreque, a qual se chamava Dalila.
5 Então, os príncipes dos filisteus subiram a ela e lhe disseram: Persuade-o e vê em que consiste a sua grande força e com que poderíamos dominá-lo e amarrá-lo, para assim o subjugarmos; e te daremos cada um mil e cem siclos de prata.
6 Disse, pois, Dalila a Sansão: Declara-me, peço-te, em que consiste a tua grande força e com que poderias ser amarrado para te poderem subjugar.
7 Respondeu-lhe Sansão: Se me amarrarem com sete tendões frescos, ainda não secos, então, me enfraquecerei, e serei como qualquer outro homem.
8 Os príncipes dos filisteus trouxeram a Dalila sete tendões frescos, que ainda não estavam secos; e com os tendões ela o amarrou.
9 Tinha ela no seu quarto interior homens escondidos. Então, ela lhe disse: Os filisteus vêm sobre ti, Sansão! Quebrou ele os tendões como se quebra o fio da estopa chamuscada; assim, não se soube em que lhe consistia a força.
10 Disse Dalila a Sansão: Eis que zombaste de mim e me disseste mentiras; ora, declara-me, agora, com que poderias ser amarrado.
11 Ele lhe disse: Se me amarrarem bem com cordas novas, com que se não tenha feito obra nenhuma, então, me enfraquecerei e serei como qualquer outro homem.
12 Dalila tomou cordas novas, e o amarrou, e disse-lhe: Os filisteus vêm sobre ti, Sansão! Tinha ela no seu quarto interior homens escondidos. Ele as rebentou de seus braços como um fio.
13 Disse Dalila a Sansão: Até agora, tens zombado de mim e me tens dito mentiras; declara-me, pois, agora: com que poderias ser amarrado? Ele lhe respondeu: Se teceres as sete tranças da minha cabeça com a urdidura da teia e se as firmares com pino de tear, então, me enfraquecerei e serei como qualquer outro homem. Enquanto ele dormia, tomou ela as sete tranças e as teceu com a urdidura da teia.
14 E as fixou com um pino de tear e disse-lhe: Os filisteus vêm sobre ti, Sansão! Então, despertou do seu sono e arrancou o pino e a urdidura da teia.
15 Então, ela lhe disse: Como dizes que me amas, se não está comigo o teu coração? Já três vezes zombaste de mim e ainda não me declaraste em que consiste a tua grande força.
16 Importunando-o ela todos os dias com as suas palavras e molestando-o, apoderou-se da alma dele uma impaciência de matar.
17 Descobriu-lhe todo o coração e lhe disse: Nunca subiu navalha à minha cabeça, porque sou nazireu de Deus, desde o ventre de minha mãe; se vier a ser rapado, ir-se-á de mim a minha força, e me enfraquecerei e serei como qualquer outro homem.
18 Vendo, pois, Dalila que já ele lhe descobrira todo o coração, mandou chamar os príncipes dos filisteus, dizendo: Subi mais esta vez, porque, agora, me descobriu ele todo o coração. Então, os príncipes dos filisteus subiram a ter com ela e trouxeram com eles o dinheiro.
19 Então, Dalila fez dormir Sansão nos joelhos dela e, tendo chamado um homem, mandou rapar-lhe as sete tranças da cabeça; passou ela a subjugá-lo; e retirou-se dele a sua força.
20 E disse ela: Os filisteus vêm sobre ti, Sansão! Tendo ele despertado do seu sono, disse consigo mesmo: Sairei ainda esta vez como dantes e me livrarei; porque ele não sabia ainda que já o Senhor se tinha retirado dele.
21 Então, os filisteus pegaram nele, e lhe vazaram os olhos, e o fizeram descer a Gaza; amarraram-no com duas cadeias de bronze, e virava um moinho no cárcere.
22 E o cabelo da sua cabeça, logo após ser rapado, começou a crescer de novo.
23 Então, os príncipes dos filisteus se ajuntaram para oferecer grande sacrifício a seu deus Dagom e para se alegrarem; e diziam: Nosso deus nos entregou nas mãos a Sansão, nosso inimigo.
24 Vendo-o o povo, louvavam ao seu deus, porque diziam: Nosso deus nos entregou nas mãos o nosso inimigo, e o que destruía a nossa terra, e o que multiplicava os nossos mortos.
25 Alegrando-se-lhes o coração, disseram: Mandai vir Sansão, para que nos divirta. Trouxeram Sansão do cárcere, o qual os divertia. Quando o fizeram estar em pé entre as colunas,
26 disse Sansão ao moço que o tinha pela mão: Deixa-me, para que apalpe as colunas em que se sustém a casa, para que me encoste a elas.
27 Ora, a casa estava cheia de homens e mulheres, e também ali estavam todos os príncipes dos filisteus; e sobre o teto havia uns três mil homens e mulheres, que olhavam enquanto Sansão os divertia.
28 Sansão clamou ao Senhor e disse: Senhor Deus, peço-te que te lembres de mim, e dá-me força só esta vez, ó Deus, para que me vingue dos filisteus, ao menos por um dos meus olhos.
29 Abraçou-se, pois, Sansão com as duas colunas do meio, em que se sustinha a casa, e fez força sobre elas, com a mão direita em uma e com a esquerda na outra.
30 E disse: Morra eu com os filisteus. E inclinou-se com força, e a casa caiu sobre os príncipes e sobre todo o povo que nela estava; e foram mais os que matou na sua morte do que os que matara na sua vida.
31 Então, seus irmãos desceram, e toda a casa de seu pai, tomaram-no, subiram com ele e o sepultaram entre Zorá e Estaol, no sepulcro de Manoá, seu pai. Julgou ele a Israel vinte anos.*
1 Havia um homem da região montanhosa de Efraim cujo nome era Mica,
2 o qual disse a sua mãe: Os mil e cem siclos de prata que te foram tirados, por cuja causa deitavas maldições e de que também me falaste, eis que esse dinheiro está comigo; eu o tomei. Então, lhe disse a mãe: Bendito do Senhor seja meu filho!
3 Assim, restituiu os mil e cem siclos de prata a sua mãe, que disse: De minha mão dedico este dinheiro ao Senhor para meu filho, para fazer uma imagem de escultura e uma de fundição, de sorte que, agora, eu to devolvo.
4 Porém ele restituiu o dinheiro a sua mãe, que tomou duzentos siclos de prata e os deu ao ourives, o qual fez deles uma imagem de escultura e uma de fundição; e a imagem esteve em casa de Mica.
5 E, assim, este homem, Mica, veio a ter uma casa de deuses; fez uma estola sacerdotal e ídolos do lar e consagrou a um de seus filhos, para que lhe fosse por sacerdote.
6 Naqueles dias, não havia rei em Israel; cada qual fazia o que achava mais reto.
7 Havia um moço de Belém de Judá, da tribo de Judá, que era levita e se demorava ali.
8 Esse homem partiu da cidade de Belém de Judá para ficar onde melhor lhe parecesse. Seguindo, pois, o seu caminho, chegou à região montanhosa de Efraim, até à casa de Mica.
9 Perguntou-lhe Mica: Donde vens? Ele lhe respondeu: Sou levita de Belém de Judá e vou ficar onde melhor me parecer.
10 Então, lhe disse Mica: Fica comigo e sê-me por pai e sacerdote; e cada ano te darei dez siclos de prata, o vestuário e o sustento. O levita entrou
11 e consentiu em ficar com aquele homem; e o moço lhe foi como um de seus filhos.
12 Consagrou Mica ao moço levita, que lhe passou a ser sacerdote; e ficou em casa de Mica.
13 Então, disse Mica: Sei, agora, que o Senhor me fará bem, porquanto tenho um levita por sacerdote.*
1 Naqueles dias, não havia rei em Israel, e a tribo dos danitas buscava para si herança em que habitar; porquanto, até àquele dia, entre as tribos de Israel, não lhe havia caído por sorte a herança.
2 Enviaram os filhos de Dã cinco homens dentre todos os da sua tribo, homens valentes, de Zorá e de Estaol, a espiar e explorar a terra; e lhes disseram: Ide, explorai a terra. Chegaram à região montanhosa de Efraim, até à casa de Mica, e ali pernoitaram.
3 Estando eles junto da casa de Mica, reconheceram a voz do moço, do levita; chegaram-se para lá e lhe disseram: Quem te trouxe para aqui? Que fazes aqui? E que é que tens aqui?
4 Ele respondeu: Assim e assim me fez Mica; pois me assalariou, e eu lhe sirvo de sacerdote.
5 Então, lhe disseram: Consulta a Deus, para que saibamos se prosperará o caminho que levamos.
6 Disse-lhes o sacerdote: Ide em paz; o caminho que levais está sob as vistas do Senhor.
7 Partiram os cinco homens, e chegaram a Laís, e viram que o povo que havia nela estava seguro, segundo o costume dos sidônios, em paz e confiado. Nenhuma autoridade havia que, por qualquer coisa, o oprimisse; também estava longe dos sidônios e não tinha trato com nenhuma outra gente.
8 Então, voltaram a seus irmãos, a Zorá e a Estaol; e estes lhes perguntaram: Que nos dizeis?
9 Eles disseram: Disponde-vos e subamos contra eles; porque examinamos a terra, e eis que é muito boa. Estais aí parados? Não vos demoreis em sair para ocupardes a terra.
10 Quando lá chegardes, achareis um povo confiado, e a terra é ampla; porque Deus vo-la entregou nas mãos; é um lugar em que não há falta de coisa alguma que há na terra.
11 Então, partiram dali, da tribo dos danitas, de Zorá e de Estaol, seiscentos homens armados de suas armas de guerra.
12 Subiram e acamparam-se em Quiriate-Jearim, em Judá; pelo que chamaram a este lugar Maané-Dã, até ao dia de hoje; está por detrás de Quiriate-Jearim.
13 Dali, passaram à região montanhosa de Efraim e chegaram até à casa de Mica.
14 Os cinco homens que foram espiar a terra de Laís disseram a seus irmãos: Sabeis vós que, naquelas casas, há uma estola sacerdotal, e ídolos do lar, e uma imagem de escultura, e uma de fundição? Vede, pois, o que haveis de fazer.
15 Então, foram para lá, e chegaram à casa do moço, o levita, em casa de Mica, e o saudaram.
16 Os seiscentos homens que eram dos filhos de Dã, armados de suas armas de guerra, ficaram à entrada da porta.
17 Porém, subindo os cinco homens que foram espiar a terra, entraram e apanharam a imagem de escultura, a estola sacerdotal, os ídolos do lar e a imagem de fundição, ficando o sacerdote em pé à entrada da porta, com os seiscentos homens que estavam armados com as armas de guerra.
18 Entrando eles, pois, na casa de Mica e tomando a imagem de escultura, a estola sacerdotal, os ídolos do lar e a imagem de fundição, disse-lhes o sacerdote: Que estais fazendo?
19 Eles lhe disseram: Cala-te, e põe a mão na boca, e vem conosco, e sê-nos por pai e sacerdote. Ser-te-á melhor seres sacerdote da casa de um só homem do que seres sacerdote de uma tribo e de uma família em Israel?
20 Então, se alegrou o coração do sacerdote, tomou a estola sacerdotal, os ídolos do lar e a imagem de escultura e entrou no meio do povo.
21 Assim, viraram e, tendo posto diante de si os meninos, o gado e seus bens, partiram.
22 Estando já longe da casa de Mica, reuniram-se os homens que estavam nas casas junto à dele e alcançaram os filhos de Dã.
23 E clamaram após eles, os quais, voltando-se, disseram a Mica: Que tens, que convocaste esse povo?
24 Respondeu-lhes: Os deuses que eu fiz me tomastes e também o sacerdote e vos fostes; que mais me resta? Como, pois, me perguntais: Que é o que tens?
25 Porém os filhos de Dã lhe disseram: Não nos faças ouvir a tua voz, para que, porventura, homens de ânimo amargoso não se lancem sobre ti, e tu percas a tua vida e a vida dos da tua casa.
26 Assim, prosseguiram o seu caminho os filhos de Dã; e Mica, vendo que eram mais fortes do que ele, voltou-se e tornou para sua casa.
27 Levaram eles o que Mica havia feito e o sacerdote que tivera, e chegaram a Laís, a um povo em paz e confiado, e os feriram a fio de espada, e queimaram a cidade.
28 Ninguém houve que os livrasse, porquanto estavam longe de Sidom e não tinham trato com ninguém; a cidade estava no vale junto a Bete-Reobe. Reedificaram a cidade, habitaram nela
29 e lhe chamaram Dã, segundo o nome de Dã, seu pai, que nascera a Israel; porém, outrora, o nome desta cidade era Laís.
30 Os filhos de Dã levantaram para si aquela imagem de escultura; e Jônatas, filho de Gérson, o filho de Manassés, ele e seus filhos foram sacerdotes da tribo dos danitas até ao dia do cativeiro do povo.
31 Assim, pois, a imagem de escultura feita por Mica estabeleceram para si todos os dias que a Casa de Deus esteve em Siló.*
1 Naqueles dias, em que não havia rei em Israel, houve um homem levita, que, peregrinando nos longes da região montanhosa de Efraim, tomou para si uma concubina de Belém de Judá.
2 Porém ela, aborrecendo-se dele, o deixou, tornou para a casa de seu pai, em Belém de Judá, e lá esteve os dias de uns quatro meses.
3 Seu marido, tendo consigo o seu servo e dois jumentos, levantou-se e foi após ela para falar-lhe ao coração, a fim de tornar a trazê-la. Ela o fez entrar na casa de seu pai. Este, quando o viu, saiu alegre a recebê-lo.
4 Seu sogro, o pai da moça, o deteve por três dias em sua companhia; comeram, beberam, e o casal se alojou ali.
5 Ao quarto dia, madrugaram e se levantaram para partir; então, o pai da moça disse a seu genro: Fortalece-te com um bocado de pão, e, depois, partireis.
6 Assentaram-se, pois, e comeram ambos juntos, e beberam; então, disse o pai da moça ao homem: Peço-te que ainda esta noite queiras passá-la aqui, e se alegre o teu coração.
7 Contudo, o homem levantou-se para partir; porém o seu sogro, instando com ele, fê-lo pernoitar ali.
8 Madrugando ele ao quinto dia para partir, disse o pai da moça: Fortalece-te, e detende-vos até ao declinar do dia; e ambos comeram juntos.
9 Então, o homem se levantou para partir, ele, e a sua concubina, e o seu moço; e disse-lhe seu sogro, o pai da moça: Eis que já declina o dia, a tarde vem chegando; peço-te que passes aqui a noite; vai-se o dia acabando, passa aqui a noite, e que o teu coração se alegre; amanhã de madrugada, levantai-vos a caminhar e ide para a vossa casa.
10 Porém o homem não quis passar ali a noite; mas levantou-se, e partiu, e veio até à altura de Jebus (que é Jerusalém), e com ele os dois jumentos albardados, como também a sua concubina.
11 Estando, pois, já perto de Jebus e tendo-se adiantado o declinar-se do dia, disse o moço a seu senhor: Caminhai, agora, e retiremo-nos a esta cidade dos jebuseus e passemos ali a noite.
12 Porém o seu senhor lhe disse: Não nos retiraremos a nenhuma cidade estranha, que não seja dos filhos de Israel, mas passemos até Gibeá.
13 Disse mais a seu moço: Caminha, e cheguemos a um daqueles lugares e pernoitemos em Gibeá ou em Ramá.
14 Passaram, pois, adiante e caminharam, e o sol se lhes pôs junto a Gibeá, que pertence a Benjamim.
15 Retiraram-se para Gibeá, a fim de, nela, passarem a noite; entrando ele, assentou-se na praça da cidade, porque não houve quem os recolhesse em casa para ali pernoitarem.
16 Eis que, ao anoitecer, vinha do seu trabalho no campo um homem velho; era este da região montanhosa de Efraim, mas morava em Gibeá; porém os habitantes do lugar eram benjamitas.
17 Erguendo o velho os olhos, viu na praça da cidade este viajante e lhe perguntou: Para onde vais e donde vens?
18 Ele lhe respondeu: Estamos viajando de Belém de Judá para os longes da região montanhosa de Efraim, donde sou; fui a Belém de Judá e, agora, estou de viagem para a Casa do Senhor; e ninguém há que me recolha em casa,
19 ainda que há palha e pasto para os nossos jumentos, e também pão e vinho para mim, e para a tua serva, e para o moço que vem com os teus servos; de coisa nenhuma há falta.
20 Então, disse o velho: Paz seja contigo; tudo quanto te vier a faltar fique a meu cargo; tão somente não passes a noite na praça.
21 Levou-o para casa e deu pasto aos jumentos; e, tendo eles lavado os pés, comeram e beberam.
22 Enquanto eles se alegravam, eis que os homens daquela cidade, filhos de Belial, cercaram a casa, batendo à porta; e falaram ao velho, senhor da casa, dizendo: Traze para fora o homem que entrou em tua casa, para que abusemos dele.
23 O senhor da casa saiu a ter com eles e lhes disse: Não, irmãos meus, não façais semelhante mal; já que o homem está em minha casa, não façais tal loucura.
24 Minha filha virgem e a concubina dele trarei para fora; humilhai-as e fazei delas o que melhor vos agrade; porém a este homem não façais semelhante loucura.
25 Porém aqueles homens não o quiseram ouvir; então, ele pegou da concubina do levita e entregou a eles fora, e eles a forçaram e abusaram dela toda a noite até pela manhã; e, subindo a alva, a deixaram.
26 Ao romper da manhã, vindo a mulher, caiu à porta da casa do homem, onde estava o seu senhor, e ali ficou até que se fez dia claro.
27 Levantando-se pela manhã o seu senhor, abriu as portas da casa e, saindo a seguir o seu caminho, eis que a mulher, sua concubina, jazia à porta da casa, com as mãos sobre o limiar.
28 Ele lhe disse: Levanta-te, e vamos; porém ela não respondeu; então, o homem a pôs sobre o jumento, dispôs-se e foi para sua casa.
29 Chegando a casa, tomou de um cutelo e, pegando a concubina, a despedaçou por seus ossos em doze partes; e as enviou por todos os limites de Israel.
30 Cada um que a isso presenciava aos outros dizia: Nunca tal se fez, nem se viu desde o dia em que os filhos de Israel subiram da terra do Egito até ao dia de hoje; ponderai nisso, considerai e falai.*
1 Saíram todos os filhos de Israel, e a congregação se ajuntou perante o Senhor em Mispa, como se fora um só homem, desde Dã até Berseba, como também a terra de Gileade.
2 Os príncipes de todo o povo e todas as tribos de Israel se apresentaram na congregação do povo de Deus. Havia quatrocentos mil homens de pé, que puxavam da espada.
3 Ouviram os filhos de Benjamim que os filhos de Israel haviam subido a Mispa. Disseram os filhos de Israel: Contai-nos como sucedeu esta maldade.
4 Então, respondeu o homem levita, marido da mulher que fora morta, e disse: Cheguei com a minha concubina a Gibeá, cidade de Benjamim, para passar a noite;
5 os cidadãos de Gibeá se levantaram contra mim e, à noite, cercaram a casa em que eu estava; intentaram matar-me e violaram a minha concubina, de maneira que morreu.
6 Então, peguei a minha concubina, e a fiz em pedaços, e os enviei por toda a terra da herança de Israel, porquanto fizeram vergonha e loucura em Israel.
7 Eis que todos sois filhos de Israel; eia! Dai a vossa palavra e conselho neste caso.
8 Então, todo o povo se levantou como um só homem, dizendo: Nenhum de nós voltará para sua tenda, nenhum de nós se retirará para casa.
9 Porém isto é o que faremos a Gibeá: subiremos contra ela por sorte.
10 Tomaremos dez homens de cem de todas as tribos de Israel, e cem de mil, e mil de dez mil, para providenciarem mantimento para o povo, a fim de que este, vindo a Gibeá de Benjamim, faça a ela conforme toda a loucura que tem feito em Israel.
11 Assim, se ajuntaram contra esta cidade todos os homens de Israel, unidos como um só homem.
12 As tribos de Israel enviaram homens por toda a tribo de Benjamim, para lhe dizerem: Que maldade é essa que se fez entre vós?
13 Dai-nos, agora, os homens, filhos de Belial, que estão em Gibeá, para que os matemos e tiremos de Israel o mal; porém Benjamim não quis ouvir a voz de seus irmãos, os filhos de Israel.
14 Antes, os filhos de Benjamim se ajuntaram, vindos das cidades em Gibeá, para saírem a pelejar contra os filhos de Israel.
15 E contaram-se, naquele dia, os filhos de Benjamim vindos das cidades; eram vinte e seis mil homens que puxavam da espada, afora os moradores de Gibeá, de que se contavam setecentos homens escolhidos.
16 Entre todo este povo havia setecentos homens escolhidos, canhotos, os quais atiravam com a funda uma pedra num cabelo e não erravam.
17 Contaram-se dos homens de Israel, afora os de Benjamim, quatrocentos mil homens que puxavam da espada, e todos eles, homens de guerra.
18 Levantaram-se os israelitas, subiram a Betel e consultaram a Deus, dizendo: Quem dentre nós subirá, primeiro, a pelejar contra Benjamim? Respondeu o Senhor: Judá subirá primeiro.
19 Levantaram-se, pois, os filhos de Israel pela manhã e acamparam-se contra Gibeá.
20 Saíram os homens de Israel à peleja contra Benjamim; e, junto a Gibeá, se ordenaram contra ele.
21 Então, os filhos de Benjamim saíram de Gibeá e derribaram por terra, naquele dia, vinte e dois mil homens de Israel.
22 Porém se animou o povo dos homens de Israel e tornaram a ordenar-se para a peleja, no lugar onde, no primeiro dia, o tinham feito.
23 Antes, subiram os filhos de Israel, e choraram perante o Senhor até à tarde, e consultaram o Senhor, dizendo: Tornaremos a pelejar contra os filhos de Benjamim, nosso irmão? Respondeu o Senhor: Subi contra ele.
24 Chegaram-se, pois, os filhos de Israel contra os filhos de Benjamim, no dia seguinte.
25 Também os de Benjamim, no dia seguinte, saíram de Gibeá de encontro a eles e derribaram ainda por terra mais dezoito mil homens, todos dos que puxavam da espada.
26 Então, todos os filhos de Israel, todo o povo, subiram, e vieram a Betel, e choraram, e estiveram ali perante o Senhor, e jejuaram aquele dia até à tarde; e, perante o Senhor, ofereceram holocaustos e ofertas pacíficas.
27 E os filhos de Israel perguntaram ao Senhor (porquanto a arca da Aliança de Deus estava ali naqueles dias;
28 e Fineias, filho de Eleazar, filho de Arão, ministrava perante ela naqueles dias), dizendo: Tornaremos a sair ainda a pelejar contra os filhos de Benjamim, nosso irmão, ou desistiremos? Respondeu o Senhor: Subi, que amanhã eu os entregarei nas vossas mãos.
29 Então, Israel pôs emboscadas em redor de Gibeá.
30 Ao terceiro dia, subiram os filhos de Israel contra os filhos de Benjamim e se ordenaram à peleja contra Gibeá, como das outras vezes.
31 Então, os filhos de Benjamim saíram de encontro ao povo, e, deixando-se atrair para longe da cidade, começaram a ferir alguns do povo, e mataram, como das outras vezes, uns trinta dos homens de Israel, pelas estradas, das quais uma sobe para Betel, a outra, para Gibeá do Campo.
32 Então, os filhos de Benjamim disseram: Vão derrotados diante de nós como dantes. Porém os filhos de Israel disseram: Fujamos e atraiamo-los da cidade para as estradas.
33 Todos os homens de Israel se levantaram do seu lugar e se ordenaram para a peleja em Baal-Tamar; e a emboscada de Israel saiu do seu lugar, das vizinhanças de Geba.
34 Dez mil homens escolhidos de todo o Israel vieram contra Gibeá, e a peleja se tornou renhida; porém eles não imaginavam que a calamidade lhes tocaria.
35 Então, feriu o Senhor a Benjamim diante de Israel; e mataram os filhos de Israel, naquele dia, vinte e cinco mil e cem homens de Benjamim, todos dos que puxavam da espada;
36 assim, viram os filhos de Benjamim que estavam feridos. Os homens de Israel retiraram-se perante os benjamitas, porquanto estavam confiados na emboscada que haviam posto contra Gibeá.
37 A emboscada se apressou, e acometeu a Gibeá, e de golpe feriu-a toda a fio de espada.
38 Os homens de Israel tinham um sinal determinado com a emboscada, que era fazerem levantar da cidade uma grande nuvem de fumaça.
39 Então, os homens de Israel deviam voltar à peleja. Começara Benjamim a ferir e havia já matado uns trinta entre os homens de Israel, porque diziam: Com efeito, já estão derrotados diante de nós, como na peleja anterior.
40 Então, a nuvem de fumaça começou a levantar-se da cidade, como se fora uma coluna; virando-se Benjamim a olhar para trás de si, eis que toda a cidade subia em chamas para o céu.
41 Viraram os homens de Israel, e os de Benjamim pasmaram, porque viram que a calamidade lhes tocaria.
42 E viraram diante dos homens de Israel, para o caminho do deserto; porém a peleja os apertou; e os que vinham das cidades os destruíram no meio deles.
43 Cercaram a Benjamim, seguiram-no e, onde repousava, ali o alcançavam, até diante de Gibeá, para o nascente do sol.
44 Caíram de Benjamim dezoito mil homens, todos estes homens valentes.
45 Então, viraram e fugiram para o deserto, à penha Rimom; e, na respiga, mataram ainda pelos caminhos uns cinco mil homens, e de perto os seguiram até Gidom, e feriram deles dois mil homens.
46 Todos os que de Benjamim caíram, naquele dia, foram vinte e cinco mil homens que puxavam da espada, todos eles homens valentes.
47 Porém seiscentos homens viraram e fugiram para o deserto, à penha Rimom, onde ficaram quatro meses.
48 Os homens de Israel voltaram para os filhos de Benjamim e passaram a fio de espada tudo o que restou da cidade, tanto homens como animais, em suma, tudo o que encontraram; e também a todas as cidades que acharam puseram fogo.*
1 Ora, haviam jurado os homens de Israel em Mispa, dizendo: Nenhum de nós dará sua filha por mulher aos benjamitas.
2 Veio o povo a Betel, e ali ficaram até à tarde diante de Deus, e levantaram a voz, e prantearam com grande pranto.
3 Disseram: Ah! Senhor, Deus de Israel, por que sucedeu isto em Israel, que, hoje, lhe falte uma tribo?
4 Ao dia seguinte, o povo, pela manhã, se levantou e edificou ali um altar; e apresentaram holocaustos e ofertas pacíficas.
5 Disseram os filhos de Israel: Quem de todas as tribos de Israel não subiu à assembleia do Senhor? Porque se tinha feito um grande juramento acerca do que não viesse ao Senhor a Mispa, que dizia: Será morto.
6 Os filhos de Israel tiveram compaixão de seu irmão Benjamim e disseram: Foi, hoje, eliminada uma tribo de Israel.
7 Como obteremos mulheres para os restantes deles, pois juramos, pelo Senhor, que das nossas filhas não lhes daríamos por mulheres?
8 E disseram: Há alguma das tribos de Israel que não tenha subido ao Senhor a Mispa? E eis que ninguém de Jabes-Gileade viera ao acampamento, à assembleia.
9 Quando se contou o povo, eis que nenhum dos moradores de Jabes-Gileade se achou ali.
10 Por isso, a congregação enviou lá doze mil homens dos mais valentes e lhes ordenou, dizendo: Ide e, a fio de espada, feri os moradores de Jabes-Gileade, e as mulheres, e as crianças.
11 Isto é o que haveis de fazer: a todo homem e a toda mulher que se houver deitado com homem destruireis.
12 Acharam entre os moradores de Jabes-Gileade quatrocentas moças virgens, que não se deitaram com homem; e as trouxeram ao acampamento, a Siló, que está na terra de Canaã.
13 Toda a congregação, pois, enviou mensageiros aos filhos de Benjamim que estavam na penha Rimom, e lhes proclamaram a paz.
14 Nesse mesmo tempo, voltaram os benjamitas; e se lhes deram por mulheres as que foram conservadas com vida, das de Jabes-Gileade; porém estas ainda não lhes bastaram.
15 Então, o povo teve compaixão de Benjamim, porquanto o Senhor tinha feito brecha nas tribos de Israel.
16 Disseram os anciãos da congregação: Como obteremos mulheres para os restantes ainda, pois foram exterminadas as mulheres dos benjamitas?
17 Disseram mais: A herança dos que ficaram de resto não na deve perder Benjamim, visto que nenhuma tribo de Israel deve ser destruída.
18 Porém nós não lhes poderemos dar mulheres de nossas filhas, porque os filhos de Israel juraram, dizendo: Maldito o que der mulher aos benjamitas.
19 Então, disseram: Eis que, de ano em ano, há solenidade do Senhor em Siló, que se celebra para o norte de Betel, do lado do nascente do sol, pelo caminho alto que sobe de Betel a Siquém e para o sul de Lebona.
20 Ordenaram aos filhos de Benjamim, dizendo: Ide, e emboscai-vos nas vinhas,
21 e olhai; e eis aí, saindo as filhas de Siló a dançar em rodas, saí vós das vinhas, e arrebatai, dentre elas, cada um sua mulher, e ide-vos à terra de Benjamim.
22 Quando seus pais ou seus irmãos vierem queixar-se a nós, nós lhes diremos: por amor de nós, tende compaixão deles, pois, na guerra contra Jabes-Gileade, não obtivemos mulheres para cada um deles; e também não lhes destes, pois neste caso ficaríeis culpados.
23 Assim fizeram os filhos de Benjamim e levaram mulheres conforme o número deles, das que arrebataram das rodas que dançavam; e foram-se, voltaram à sua herança, reedificaram as cidades e habitaram nelas.
24 Então, os filhos de Israel também partiram dali, cada um para a sua tribo, para a sua família e para a sua herança.
25 Naqueles dias, não havia rei em Israel; cada um fazia o que achava mais reto.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Juízes','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)