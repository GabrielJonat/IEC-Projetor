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
1 Chamou o Senhor a Moisés e, da tenda da congregação, lhe disse:
2 Fala aos filhos de Israel e dize-lhes: Quando algum de vós trouxer oferta ao Senhor, trareis a vossa oferta de gado, de rebanho ou de gado miúdo.
3 Se a sua oferta for holocausto de gado, trará macho sem defeito; à porta da tenda da congregação o trará, para que o homem seja aceito perante o Senhor.
4 E porá a mão sobre a cabeça do holocausto, para que seja aceito a favor dele, para a sua expiação.
5 Depois, imolará o novilho perante o Senhor; e os filhos de Arão, os sacerdotes, apresentarão o sangue e o aspergirão ao redor sobre o altar que está diante da porta da tenda da congregação.
6 Então, ele esfolará o holocausto e o cortará em seus pedaços.
7 E os filhos de Arão, o sacerdote, porão fogo sobre o altar e porão em ordem lenha sobre o fogo.
8 Também os filhos de Arão, os sacerdotes, colocarão em ordem os pedaços, a saber, a cabeça e o redenho, sobre a lenha que está no fogo sobre o altar.
9 Porém as entranhas e as pernas, o sacerdote as lavará com água; e queimará tudo isso sobre o altar; é holocausto, oferta queimada, de aroma agradável ao Senhor.
10 Se a sua oferta for de gado miúdo, de carneiros ou de cabritos, para holocausto, trará macho sem defeito.
11 E o imolará ao lado do altar, para o lado norte, perante o Senhor; e os filhos de Arão, os sacerdotes, aspergirão o seu sangue em redor sobre o altar.
12 Depois, ele o cortará em seus pedaços, como também a sua cabeça e o seu redenho; e o sacerdote os porá em ordem sobre a lenha que está no fogo sobre o altar;
13 porém as entranhas e as pernas serão lavadas com água; e o sacerdote oferecerá tudo isso e o queimará sobre o altar; é holocausto, oferta queimada, de aroma agradável ao Senhor.
14 Se a sua oferta ao Senhor for holocausto de aves, trará a sua oferta de rolas ou de pombinhos.
15 O sacerdote a trará ao altar, e, com a unha, lhe destroncará a cabeça, sem a separar do pescoço, e a queimará sobre o altar; o seu sangue, ele o fará correr na parede do altar;
16 tirará o papo com suas penas e o lançará junto ao altar, para o lado oriental, no lugar da cinza;
17 rasgá-la-á pelas asas, porém não a partirá; o sacerdote a queimará sobre o altar, em cima da lenha que está no fogo; é holocausto, oferta queimada, de aroma agradável ao Senhor.*
1 Quando alguma pessoa fizer oferta de manjares ao Senhor, a sua oferta será de flor de farinha; nela, deitará azeite e, sobre ela, porá incenso.
2 Levá-la-á aos filhos de Arão, os sacerdotes, um dos quais tomará dela um punhado da flor de farinha e do seu azeite com todo o seu incenso e os queimará como porção memorial sobre o altar; é oferta queimada, de aroma agradável ao Senhor.
3 O que ficar da oferta de manjares será de Arão e de seus filhos; é coisa santíssima das ofertas queimadas ao Senhor.
4 Quando trouxeres oferta de manjares, cozida no forno, será de bolos asmos de flor de farinha amassados com azeite e obreias asmas untadas com azeite.
5 Se a tua oferta for de manjares cozida na assadeira, será de flor de farinha sem fermento amassada com azeite.
6 Em pedaços a partirás e, sobre ela, deitarás azeite; é oferta de manjares.
7 Se a tua oferta for de manjares de frigideira, far-se-á de flor de farinha com azeite.
8 E a oferta de manjares, que daquilo se fará, trarás ao Senhor; será apresentada ao sacerdote, o qual a levará ao altar.
9 Da oferta de manjares tomará o sacerdote a porção memorial e a queimará sobre o altar; é oferta queimada, de aroma agradável ao Senhor.
10 O que ficar da oferta de manjares será de Arão e de seus filhos; é coisa santíssima das ofertas queimadas ao Senhor.
11 Nenhuma oferta de manjares, que fizerdes ao Senhor, se fará com fermento; porque de nenhum fermento e de mel nenhum queimareis por oferta ao Senhor.
12 Deles, trareis ao Senhor por oferta das primícias; todavia, não se porão sobre o altar como aroma agradável.
13 Toda oferta dos teus manjares temperarás com sal; à tua oferta de manjares não deixarás faltar o sal da aliança do teu Deus; em todas as tuas ofertas aplicarás sal.
14 Se trouxeres ao Senhor oferta de manjares das primícias, farás a oferta de manjares das tuas primícias de espigas verdes, tostadas ao fogo, isto é, os grãos esmagados de espigas verdes.
15 Deitarás azeite sobre ela e, por cima, lhe porás incenso; é oferta de manjares.
16 Assim, o sacerdote queimará a porção memorial dos grãos de espigas esmagados e do azeite, com todo o incenso; é oferta queimada ao Senhor.*
1 Se a oferta de alguém for sacrifício pacífico, se a fizer de gado, seja macho ou fêmea, oferecê-la-á sem defeito diante do Senhor.
2 E porá a mão sobre a cabeça da sua oferta e a imolará diante da porta da tenda da congregação; e os filhos de Arão, os sacerdotes, aspergirão o sangue sobre o altar, ao redor.
3 Do sacrifício pacífico fará oferta queimada ao Senhor: a gordura que cobre as entranhas e toda a gordura que está sobre as entranhas,
4 como também os dois rins, a gordura que está sobre eles e junto aos lombos; e o redenho sobre o fígado com os rins, tirá-los-á.
5 E os filhos de Arão queimarão tudo isso sobre o altar, em cima do holocausto, que estará sobre a lenha no fogo; é oferta queimada, de aroma agradável ao Senhor.
6 Se a sua oferta por sacrifício pacífico ao Senhor for de gado miúdo, seja macho ou fêmea, sem defeito a oferecerá.
7 Se trouxer um cordeiro por sua oferta, oferecê-lo-á perante o Senhor.
8 E porá a mão sobre a cabeça da sua oferta e a imolará diante da tenda da congregação; e os filhos de Arão aspergirão o sangue sobre o altar, em redor.
9 Então, do sacrifício pacífico trará ao Senhor por oferta queimada a sua gordura: a cauda toda, a qual tirará rente ao espinhaço, e a gordura que cobre as entranhas, e toda a gordura que está sobre as entranhas,
10 como também os dois rins, a gordura que está sobre eles e junto aos lombos; e o redenho sobre o fígado com os rins, tirá-los-á.
11 E o sacerdote queimará tudo isso sobre o altar; é manjar da oferta queimada ao Senhor.
12 Mas, se a sua oferta for uma cabra, perante o Senhor a trará.
13 E porá a mão sobre a sua cabeça e a imolará diante da tenda da congregação; e os filhos de Arão aspergirão o sangue sobre o altar, em redor.
14 Depois, trará dela a sua oferta, por oferta queimada ao Senhor: a gordura que cobre as entranhas e toda a gordura que está sobre as entranhas,
15 como também os dois rins, a gordura que está sobre eles e junto aos lombos; e o redenho sobre o fígado com os rins, tirá-los-á.
16 E o sacerdote queimará tudo isso sobre o altar; é manjar da oferta queimada, de aroma agradável. Toda a gordura será do Senhor.
17 Estatuto perpétuo será durante as vossas gerações, em todas as vossas moradas; gordura nenhuma nem sangue jamais comereis.*
1 Disse mais o Senhor a Moisés:
2 Fala aos filhos de Israel, dizendo: Quando alguém pecar por ignorância contra qualquer dos mandamentos do Senhor, por fazer contra algum deles o que não se deve fazer,
3 se o sacerdote ungido pecar para escândalo do povo, oferecerá pelo seu pecado um novilho sem defeito ao Senhor, como oferta pelo pecado.
4 Trará o novilho à porta da tenda da congregação, perante o Senhor; porá a mão sobre a cabeça do novilho e o imolará perante o Senhor.
5 Então, o sacerdote ungido tomará do sangue do novilho e o trará à tenda da congregação;
6 e, molhando o dedo no sangue, aspergirá dele sete vezes perante o Senhor, diante do véu do santuário.
7 Também daquele sangue porá o sacerdote sobre os chifres do altar do incenso aromático, perante o Senhor, altar que está na tenda da congregação; e todo o restante do sangue do novilho derramará à base do altar do holocausto, que está à porta da tenda da congregação.
8 Toda a gordura do novilho da expiação tirará dele: a gordura que cobre as entranhas e toda a gordura que está sobre as entranhas,
9 como também os dois rins, a gordura que está sobre eles e junto aos lombos; e o redenho sobre o fígado com os rins, tirá-los-á
10 como se tiram os do novilho do sacrifício pacífico; e o sacerdote os queimará sobre o altar do holocausto.
11 Mas o couro do novilho, toda a sua carne, a cabeça, as pernas, as entranhas e o excremento,
12 a saber, o novilho todo, levá-lo-á fora do arraial, a um lugar limpo, onde se lança a cinza, e o queimará sobre a lenha; será queimado onde se lança a cinza.
13 Mas, se toda a congregação de Israel pecar por ignorância, e isso for oculto aos olhos da coletividade, e se fizerem, contra algum dos mandamentos do Senhor, aquilo que se não deve fazer, e forem culpados,
14 e o pecado que cometeram for notório, então, a coletividade trará um novilho como oferta pelo pecado e o apresentará diante da tenda da congregação.
15 Os anciãos da congregação porão as mãos sobre a cabeça do novilho perante o Senhor; e será imolado o novilho perante o Senhor.
16 Então, o sacerdote ungido trará do sangue do novilho à tenda da congregação;
17 molhará o dedo no sangue e o aspergirá sete vezes perante o Senhor, diante do véu.
18 E daquele sangue porá sobre os chifres do altar que está perante o Senhor, na tenda da congregação; e todo o restante do sangue derramará à base do altar do holocausto, que está à porta da tenda da congregação.
19 Tirará do novilho toda a gordura e a queimará sobre o altar;
20 e fará a este novilho como fez ao novilho da oferta pelo pecado; assim lhe fará, e o sacerdote por eles fará expiação, e eles serão perdoados.
21 Depois, levará o novilho fora do arraial e o queimará como queimou o primeiro novilho; é oferta pelo pecado da coletividade.
22 Quando um príncipe pecar, e por ignorância fizer alguma de todas as coisas que o Senhor, seu Deus, ordenou se não fizessem, e se tornar culpado;
23 ou se o pecado em que ele caiu lhe for notificado, trará por sua oferta um bode sem defeito.
24 E porá a mão sobre a cabeça do bode e o imolará no lugar onde se imola o holocausto, perante o Senhor; é oferta pelo pecado.
25 Então, o sacerdote, com o dedo, tomará do sangue da oferta pelo pecado e o porá sobre os chifres do altar do holocausto; e todo o restante do sangue derramará à base do altar do holocausto.
26 Toda a gordura da oferta, queimá-la-á sobre o altar, como a gordura do sacrifício pacífico; assim, o sacerdote fará expiação por ele, no tocante ao seu pecado, e este lhe será perdoado.
27 Se qualquer pessoa do povo da terra pecar por ignorância, por fazer alguma das coisas que o Senhor ordenou se não fizessem, e se tornar culpada;
28 ou se o pecado em que ela caiu lhe for notificado, trará por sua oferta uma cabra sem defeito, pelo pecado que cometeu.
29 E porá a mão sobre a cabeça da oferta pelo pecado e a imolará no lugar do holocausto.
30 Então, o sacerdote, com o dedo, tomará do sangue da oferta e o porá sobre os chifres do altar do holocausto; e todo o restante do sangue derramará à base do altar.
31 Tirará toda a gordura, como se tira a gordura do sacrifício pacífico; o sacerdote a queimará sobre o altar como aroma agradável ao Senhor; e o sacerdote fará expiação pela pessoa, e lhe será perdoado.
32 Mas, se pela sua oferta trouxer uma cordeira como oferta pelo pecado, fêmea sem defeito a trará.
33 E porá a mão sobre a cabeça da oferta pelo pecado e a imolará por oferta pelo pecado, no lugar onde se imola o holocausto.
34 Então, o sacerdote, com o dedo, tomará do sangue da oferta pelo pecado e o porá sobre os chifres do altar do holocausto; e todo o restante do sangue derramará à base do altar.
35 Tirará toda a gordura, como se tira a gordura do cordeiro do sacrifício pacífico; o sacerdote a queimará sobre o altar, em cima das ofertas queimadas do Senhor; assim, o sacerdote, por essa pessoa, fará expiação do seu pecado que cometeu, e lhe será perdoado.*
1 Quando alguém pecar nisto: tendo ouvido a voz da imprecação, sendo testemunha de um fato, por ter visto ou sabido e, contudo, não o revelar, levará a sua iniquidade;
2 ou quando alguém tocar em alguma coisa imunda, seja corpo morto de besta-fera imunda, seja corpo morto de animal imundo, seja corpo morto de réptil imundo, ainda que lhe fosse oculto, e tornar-se imundo, então, será culpado;
3 ou quando tocar a imundícia de um homem, seja qual for a imundícia com que se faça imundo, e lhe for oculto, e o souber depois, será culpado;
4 ou quando alguém jurar temerariamente com seus lábios fazer mal ou fazer bem, seja o que for que o homem pronuncie temerariamente com juramento, e lhe for oculto, e o souber depois, culpado será numa destas coisas.
5 Será, pois, que, sendo culpado numa destas coisas, confessará aquilo em que pecou.
6 Como sua oferta pela culpa, pelo pecado que cometeu, trará ele ao Senhor, do gado miúdo, uma cordeira ou uma cabrita como oferta pelo pecado; assim, o sacerdote, por ele, fará expiação do seu pecado.
7 Se as suas posses não lhe permitirem trazer uma cordeira, trará ao Senhor, como oferta pela culpa, pelo pecado que cometeu, duas rolas ou dois pombinhos: um como oferta pelo pecado, e o outro como holocausto.
8 Entregá-los-á ao sacerdote, o qual primeiro oferecerá aquele que é como oferta pelo pecado e lhe destroncará, com a unha, a cabeça, sem a separar do pescoço.
9 Do sangue da oferta pelo pecado aspergirá sobre a parede do altar e o restante do sangue, fá-lo-á correr à base do altar; é oferta pelo pecado.
10 E do outro fará holocausto, conforme o estabelecido; assim, o sacerdote, por ele, fará oferta pelo pecado que cometeu, e lhe será perdoado.
11 Porém, se as suas posses não lhe permitirem trazer duas rolas ou dois pombinhos, então, aquele que pecou trará, por sua oferta, a décima parte de um efa de flor de farinha como oferta pelo pecado; não lhe deitará azeite, nem lhe porá em cima incenso, pois é oferta pelo pecado.
12 Entregá-la-á ao sacerdote, e o sacerdote dela tomará um punhado como porção memorial e a queimará sobre o altar, em cima das ofertas queimadas ao Senhor; é oferta pelo pecado.
13 Assim, o sacerdote, por ele, fará oferta pelo pecado que cometeu em alguma destas coisas, e lhe será perdoado; o restante será do sacerdote, como a oferta de manjares.
14 Disse mais o Senhor a Moisés:
15 Quando alguém cometer ofensa e pecar por ignorância nas coisas sagradas do Senhor, então, trará ao Senhor, por oferta, do rebanho, um carneiro sem defeito, conforme a tua avaliação em siclos de prata, segundo o siclo do santuário, como oferta pela culpa.
16 Assim, restituirá o que ele tirou das coisas sagradas, e ainda acrescentará o seu quinto, e o dará ao sacerdote; assim, o sacerdote, com o carneiro da oferta pela culpa, fará expiação por ele, e lhe será perdoado.
sse, contudo, será culpada e levará a sua iniquidade.
18 E do rebanho trará ao sacerdote um carneiro sem defeito, conforme a tua avaliação, para oferta pela culpa, e o sacerdote, por ela, fará expiação no tocante ao erro que, por ignorância, cometeu, e lhe será perdoado.
19 Oferta pela culpa é; certamente, se tornou culpada ao Senhor.*
1 Falou mais o Senhor a Moisés, dizendo:
2 Quando alguma pessoa pecar, e cometer ofensa contra o Senhor, e negar ao seu próximo o que este lhe deu em depósito, ou penhor, ou roubar, ou tiver usado de extorsão para com o seu próximo;
3 ou que, tendo achado o perdido, o negar com falso juramento, ou fizer alguma outra coisa de todas em que o homem costuma pecar,
4 será, pois, que, tendo pecado e ficado culpada, restituirá aquilo que roubou, ou que extorquiu, ou o depósito que lhe foi dado, ou o perdido que achou,
5 ou tudo aquilo sobre que jurou falsamente; e o restituirá por inteiro e ainda a isso acrescentará a quinta parte; àquele a quem pertence, lho dará no dia da sua oferta pela culpa.
6 E, por sua oferta pela culpa, trará, do rebanho, ao Senhor um carneiro sem defeito, conforme a tua avaliação, para a oferta pela culpa; trá-lo-á ao sacerdote.
7 E o sacerdote fará expiação por ela diante do Senhor, e será perdoada de qualquer de todas as coisas que fez, tornando-se, por isso, culpada.
8 Disse mais o Senhor a Moisés:
9 Dá ordem a Arão e a seus filhos, dizendo: Esta é a lei do holocausto: o holocausto ficará na lareira do altar toda a noite até pela manhã, e nela se manterá aceso o fogo do altar.
10 O sacerdote vestirá a sua túnica de linho e os calções de linho sobre a pele nua, e levantará a cinza, quando o fogo houver consumido o holocausto sobre o altar, e a porá junto a este.
11 Depois, despirá as suas vestes e porá outras; e levará a cinza para fora do arraial a um lugar limpo.
12 O fogo, pois, sempre arderá sobre o altar; não se apagará; mas o sacerdote acenderá lenha nele cada manhã, e sobre ele porá em ordem o holocausto, e sobre ele queimará a gordura das ofertas pacíficas.
13 O fogo arderá continuamente sobre o altar; não se apagará.
14 Esta é a lei da oferta de manjares: os filhos de Arão a oferecerão perante o Senhor, diante do altar.
15 Um deles tomará dela um punhado de flor de farinha da oferta de manjares com seu azeite e todo o incenso que está sobre a oferta de manjares; então, o queimará sobre o altar, como porção memorial de aroma agradável ao Senhor.
16 O restante dela comerão Arão e seus filhos; asmo se comerá no lugar santo; no pátio da tenda da congregação, o comerão.
17 Levedado não se cozerá; sua porção dei-lhes das minhas ofertas queimadas; coisa santíssima é, como a oferta pelo pecado e a oferta pela culpa.
18 Todo varão entre os filhos de Arão comerá da oferta de manjares; estatuto perpétuo será para as vossas gerações dentre as ofertas queimadas do Senhor; tudo o que tocar nelas será santo.
19 Disse mais o Senhor a Moisés:
20 Esta é a oferta de Arão e de seus filhos, que oferecerão ao Senhor no dia em que aquele for ungido: a décima parte de um efa de flor de farinha pela oferta de manjares contínua; metade dela será oferecida pela manhã, e a outra metade, à tarde.
21 Numa assadeira, se fará com azeite; bem amassada a trarás; em pedaços cozidos trarás a oferta de manjares de aroma agradável ao Senhor.
22 Também o sacerdote, que dentre os filhos de Arão for ungido em seu lugar, fará o mesmo; por estatuto perpétuo será de todo queimada ao Senhor.
23 Assim, toda a oferta de manjares do sacerdote será totalmente queimada; não se comerá.
24 Disse mais o Senhor a Moisés:
25 Fala a Arão e a seus filhos, dizendo: Esta é a lei da oferta pelo pecado: no lugar onde se imola o holocausto, se imolará a oferta pelo pecado, perante o Senhor; coisa santíssima é.
26 O sacerdote que a oferecer pelo pecado a comerá; no lugar santo, se comerá, no pátio da tenda da congregação.
27 Tudo o que tocar a carne da oferta será santo; se aspergir alguém do seu sangue sobre a sua veste, lavarás aquilo sobre que caiu, no lugar santo.
28 E o vaso de barro em que for cozida será quebrado; porém, se for cozida num vaso de bronze, esfregar-se-á e lavar-se-á na água.
29 Todo varão entre os sacerdotes a comerá; coisa santíssima é.
30 Porém não se comerá nenhuma oferta pelo pecado, cujo sangue se traz à tenda da congregação, para fazer expiação no santuário; no fogo será queimada.*
1 Esta é a lei da oferta pela culpa; coisa santíssima é.
2 No lugar onde imolam o holocausto, imolarão a oferta pela culpa, e o seu sangue se aspergirá sobre o altar, em redor.
3 Dela se oferecerá toda a gordura, a cauda e a gordura que cobre as entranhas;
4 também ambos os rins e a gordura que neles há, junto aos lombos; e o redenho sobre o fígado com os rins se tirará.
5 O sacerdote o queimará sobre o altar em oferta queimada ao Senhor; é oferta pela culpa.
6 Todo varão entre os sacerdotes a comerá; no lugar santo, se comerá; coisa santíssima é.
7 Como a oferta pelo pecado, assim será a oferta pela culpa; uma única lei haverá para elas: será do sacerdote que, com ela, fizer expiação.
8 O sacerdote que oferecer o holocausto de alguém terá o couro do holocausto que oferece,
9 como também toda oferta de manjares que se cozer no forno, com tudo que se preparar na frigideira e na assadeira, será do sacerdote que a oferece.
10 Toda oferta de manjares amassada com azeite ou seca será de todos os filhos de Arão, tanto de um como do outro.
11 Esta é a lei das ofertas pacíficas que alguém pode oferecer ao Senhor.
12 Se fizer por ação de graças, com a oferta de ação de graças trará bolos asmos amassados com azeite, obreias asmas untadas com azeite e bolos de flor de farinha bem amassados com azeite.
13 Com os bolos trará, por sua oferta, pão levedado, com o sacrifício de sua oferta pacífica por ação de graças.
14 E, de toda oferta, trará um bolo por oferta ao Senhor, que será do sacerdote que aspergir o sangue da oferta pacífica.
15 Mas a carne do sacrifício de ação de graças da sua oferta pacífica se comerá no dia do seu oferecimento; nada se deixará dela até à manhã.
16 E, se o sacrifício da sua oferta for voto ou oferta voluntária, no dia em que oferecer o seu sacrifício, se comerá; e o que dele ficar também se comerá no dia seguinte.
17 Porém o que ainda restar da carne do sacrifício, ao terceiro dia, será queimado.
18 Se da carne do seu sacrifício pacífico se comer ao terceiro dia, aquele que a ofereceu não será aceito, nem lhe será atribuído o sacrifício; coisa abominável será, e a pessoa que dela comer levará a sua iniquidade.
19 A carne que tocar alguma coisa imunda não se comerá; será queimada. Qualquer que estiver limpo comerá a carne do sacrifício.
20 Porém, se alguma pessoa, tendo sobre si imundícia, comer a carne do sacrifício pacífico, que é do Senhor, será eliminada do seu povo.
21 Se uma pessoa tocar alguma coisa imunda, como imundícia de homem, ou de gado imundo, ou de qualquer réptil imundo e da carne do sacrifício pacífico, que é do Senhor, ela comer, será eliminada do seu povo.
22 Disse mais o Senhor a Moisés:
23 Fala aos filhos de Israel, dizendo: Não comereis gordura de boi, nem de carneiro, nem de cabra.
24 A gordura do animal que morre por si mesmo e a do dilacerado por feras podem servir para qualquer outro uso, mas de maneira nenhuma as comereis;
25 porque qualquer que comer a gordura do animal, do qual se trouxer ao Senhor oferta queimada, será eliminado do seu povo.
26 Não comereis sangue em qualquer das vossas habitações, quer de aves, quer de gado.
27 Toda pessoa que comer algum sangue será eliminada do seu povo.
28 Disse mais o Senhor a Moisés:
29 Fala aos filhos de Israel, dizendo: Quem oferecer ao Senhor o seu sacrifício pacífico trará a sua oferta ao Senhor; do seu sacrifício pacífico
30 trará com suas próprias mãos as ofertas queimadas do Senhor; a gordura do peito com o peito trará para movê-lo por oferta movida perante o Senhor.
31 O sacerdote queimará a gordura sobre o altar, porém o peito será de Arão e de seus filhos.
32 Também a coxa direita dareis ao sacerdote por oferta dos vossos sacrifícios pacíficos.
33 Aquele dos filhos de Arão que oferecer o sangue do sacrifício pacífico e a gordura, esse terá a coxa direita por sua porção;
34 porque o peito movido e a coxa da oferta tomei dos filhos de Israel, dos seus sacrifícios pacíficos, e os dei a Arão, o sacerdote, e a seus filhos, por direito perpétuo dos filhos de Israel.
35 Esta é a porção de Arão e a porção de seus filhos, das ofertas queimadas do Senhor, no dia em que os apresentou para oficiarem como sacerdotes ao Senhor;
36 a qual o Senhor ordenou que se lhes desse dentre os filhos de Israel no dia em que os ungiu; estatuto perpétuo é pelas suas gerações.
37 Esta é a lei do holocausto, da oferta de manjares, da oferta pelo pecado, da oferta pela culpa, da consagração e do sacrifício pacífico,
38 que o Senhor ordenou a Moisés no monte Sinai, no dia em que ordenou aos filhos de Israel que oferecessem as suas ofertas ao Senhor, no deserto do Sinai.*
1 Disse mais o Senhor a Moisés:
2 Toma Arão, e seus filhos, e as vestes, e o óleo da unção, como também o novilho da oferta pelo pecado, e os dois carneiros, e o cesto dos pães asmos
3 e ajunta toda a congregação à porta da tenda da congregação.
4 Fez, pois, Moisés como o Senhor lhe ordenara, e a congregação se ajuntou à porta da tenda da congregação.
5 Então, disse Moisés à congregação: Isto é o que o Senhor ordenou que se fizesse.
6 E fez chegar a Arão e a seus filhos e os lavou com água.
7 Vestiu a Arão da túnica, cingiu-o com o cinto e pôs sobre ele a sobrepeliz; também pôs sobre ele a estola sacerdotal, e o cingiu com o cinto de obra esmerada da estola sacerdotal, e o ajustou com ele.
8 Depois, lhe colocou o peitoral, pondo no peitoral o Urim e o Tumim;
9 e lhe pôs a mitra na cabeça e na mitra, na sua parte dianteira, pôs a lâmina de ouro, a coroa sagrada, como o Senhor ordenara a Moisés.
10 Então, Moisés tomou o óleo da unção, e ungiu o tabernáculo e tudo o que havia nele, e o consagrou;
11 e dele aspergiu sete vezes sobre o altar e ungiu o altar e todos os seus utensílios, como também a bacia e o seu suporte, para os consagrar.
12 Depois, derramou do óleo da unção sobre a cabeça de Arão e ungiu-o, para consagrá-lo.
13 Também Moisés fez chegar os filhos de Arão, e vestiu-lhes as túnicas, e cingiu-os com o cinto, e atou-lhes as tiaras, como o Senhor lhe ordenara.
14 Então, fez chegar o novilho da oferta pelo pecado; e Arão e seus filhos puseram as mãos sobre a cabeça do novilho da oferta pelo pecado;
15 e Moisés o imolou, e tomou o sangue, e dele pôs, com o dedo, sobre os chifres do altar em redor, e purificou o altar; depois, derramou o resto do sangue à base do altar e o consagrou, para fazer expiação por ele.
16 Depois, tomou toda a gordura que está sobre as entranhas, e o redenho do fígado, e os dois rins, e sua gordura; e Moisés os queimou sobre o altar.
17 Mas o novilho com o seu couro, e a sua carne, e o seu excremento queimou fora do arraial, como o Senhor ordenara a Moisés.
18 Depois, fez chegar o carneiro do holocausto; e Arão e seus filhos puseram as mãos sobre a cabeça do carneiro.
19 E Moisés o imolou e aspergiu o sangue sobre o altar, em redor.
20 Partiu também o carneiro nos seus pedaços; Moisés queimou a cabeça, os pedaços e a gordura.
21 Porém as entranhas e as pernas lavou com água; e Moisés queimou todo o carneiro sobre o altar; holocausto de aroma agradável, oferta queimada era ao Senhor, como o Senhor ordenara a Moisés.
22 Então, fez chegar o outro carneiro, o carneiro da consagração; e Arão e seus filhos puseram as mãos sobre a cabeça do carneiro.
23 E Moisés o imolou, e tomou do seu sangue, e o pôs sobre a ponta da orelha direita de Arão, e sobre o polegar da sua mão direita, e sobre o polegar do seu pé direito.
24 Também fez chegar os filhos de Arão; pôs daquele sangue sobre a ponta da orelha direita deles, e sobre o polegar da mão direita, e sobre o polegar do pé direito; e aspergiu Moisés o resto do sangue sobre o altar, em redor.
25 Tomou a gordura, e a cauda, e toda a gordura que está nas entranhas, e o redenho do fígado, e ambos os rins, e a sua gordura, e a coxa direita.
26 Também do cesto dos pães asmos, que estava diante do Senhor, tomou um bolo asmo, um bolo de pão azeitado e uma obreia e os pôs sobre a gordura e sobre a coxa direita.
27 E tudo isso pôs nas mãos de Arão e de seus filhos e o moveu por oferta movida perante o Senhor.
28 Depois, Moisés o tomou das suas mãos e o queimou no altar sobre o holocausto; era uma oferta da consagração, por aroma agradável, oferta queimada ao Senhor.
29 Tomou Moisés o peito e moveu-o por oferta movida perante o Senhor; era a porção que tocava a Moisés, do carneiro da consagração, como o Senhor lhe ordenara.
30 Tomou Moisés também do óleo da unção e do sangue que estava sobre o altar e o aspergiu sobre Arão e as suas vestes, bem como sobre os filhos de Arão e as suas vestes; e consagrou a Arão, e as suas vestes, e a seus filhos, e as vestes de seus filhos.
31 Disse Moisés a Arão e a seus filhos: Cozei a carne diante da porta da tenda da congregação e ali a comereis com o pão que está no cesto da consagração, como tenho ordenado, dizendo: Arão e seus filhos a comerão.
32 Mas o que restar da carne e do pão queimareis.
33 Também da porta da tenda da congregação não saireis por sete dias, até ao dia em que se cumprirem os dias da vossa consagração; porquanto por sete dias o Senhor vos consagrará.
34 Como se fez neste dia, assim o Senhor ordenou se fizesse, em expiação por vós.
35 Ficareis, pois, à porta da tenda da congregação dia e noite, por sete dias, e observareis as prescrições do Senhor, para que não morrais; porque assim me foi ordenado.
36 E Arão e seus filhos fizeram todas as coisas que o Senhor ordenara por intermédio de Moisés.*
1 Ao oitavo dia, chamou Moisés a Arão, e a seus filhos, e aos anciãos de Israel
2 e disse a Arão: Toma um bezerro, para oferta pelo pecado, e um carneiro, para holocausto, ambos sem defeito, e traze-os perante o Senhor.
3 Depois, dirás aos filhos de Israel: Tomai um bode, para oferta pelo pecado, um bezerro e um cordeiro, ambos de um ano e sem defeito, como holocausto;
4 e um boi e um carneiro, por oferta pacífica, para sacrificar perante o Senhor, e oferta de manjares amassada com azeite; porquanto, hoje, o Senhor vos aparecerá.
5 Então, trouxeram o que ordenara Moisés, diante da tenda da congregação, e chegou-se toda a congregação e se pôs perante o Senhor.
6 Disse Moisés: Esta coisa que o Senhor ordenou fareis; e a glória do Senhor vos aparecerá.
7 Depois, disse Moisés a Arão: Chega-te ao altar, faze a tua oferta pelo pecado e o teu holocausto; e faze expiação por ti e pelo povo; depois, faze a oferta do povo e a expiação por ele, como ordenou o Senhor.
8 Chegou-se, pois, Arão ao altar e imolou o bezerro da oferta pelo pecado que era por si mesmo.
9 Os filhos de Arão trouxeram-lhe o sangue; ele molhou o dedo no sangue e o pôs sobre os chifres do altar; e o resto do sangue derramou à base do altar.
10 Mas a gordura, e os rins, e o redenho do fígado da oferta pelo pecado queimou sobre o altar, como o Senhor ordenara a Moisés.
11 Porém a carne e o couro queimou fora do arraial.
12 Depois, imolou o holocausto, e os filhos de Arão lhe entregaram o sangue, e ele o aspergiu sobre o altar, em redor.
13 Também lhe entregaram o holocausto nos seus pedaços, com a cabeça; e queimou-o sobre o altar.
14 E lavou as entranhas e as pernas e as queimou sobre o holocausto, no altar.
15 Depois, fez chegar a oferta do povo, e, tomando o bode da oferta pelo pecado, que era pelo povo, o imolou, e o preparou por oferta pelo pecado, como fizera com o primeiro.
16 Também fez chegar o holocausto e o ofereceu segundo o rito.
17 Fez chegar a oferta de manjares, e dela tomou um punhado, e queimou sobre o altar, além do holocausto da manhã.
18 Depois, imolou o boi e o carneiro em sacrifício pacífico, que era pelo povo; e os filhos de Arão entregaram-lhe o sangue, que aspergiu sobre o altar, em redor,
19 como também a gordura do boi e do carneiro, e a cauda, e o que cobre as entranhas, e os rins, e o redenho do fígado.
20 E puseram a gordura sobre o peito, e ele a queimou sobre o altar;
21 mas o peito e a coxa direita Arão moveu por oferta movida perante o Senhor, como Moisés tinha ordenado.
22 Depois, Arão levantou as mãos para o povo e o abençoou; e desceu, havendo feito a oferta pelo pecado, e o holocausto, e a oferta pacífica.
23 Então, entraram Moisés e Arão na tenda da congregação; e, saindo, abençoaram o povo; e a glória do Senhor apareceu a todo o povo.
24 E eis que, saindo fogo de diante do Senhor, consumiu o holocausto e a gordura sobre o altar; o que vendo o povo, jubilou e prostrou-se sobre o rosto.*
1 Nadabe e Abiú, filhos de Arão, tomaram cada um o seu incensário, e puseram neles fogo, e sobre este, incenso, e trouxeram fogo estranho perante a face do Senhor, o que lhes não ordenara.
2 Então, saiu fogo de diante do Senhor e os consumiu; e morreram perante o Senhor.
3 E falou Moisés a Arão: Isto é o que o Senhor disse: Mostrarei a minha santidade naqueles que se cheguem a mim e serei glorificado diante de todo o povo. Porém Arão se calou.
4 Então, Moisés chamou a Misael e a Elzafã, filhos de Uziel, tio de Arão, e disse-lhes: Chegai, tirai vossos irmãos de diante do santuário, para fora do arraial.
5 Chegaram-se, pois, e os levaram nas suas túnicas para fora do arraial, como Moisés tinha dito.
6 Moisés disse a Arão e a seus filhos Eleazar e Itamar: Não desgrenheis os cabelos, nem rasgueis as vossas vestes, para que não morrais, nem venha grande ira sobre toda a congregação; mas vossos irmãos, toda a casa de Israel, lamentem o incêndio que o Senhor suscitou.
7 Não saireis da porta da tenda da congregação, para que não morrais; porque está sobre vós o óleo da unção do Senhor. E fizeram conforme a palavra de Moisés.
8 Falou também o Senhor a Arão, dizendo:
9 Vinho ou bebida forte tu e teus filhos não bebereis quando entrardes na tenda da congregação, para que não morrais; estatuto perpétuo será isso entre as vossas gerações,
10 para fazerdes diferença entre o santo e o profano e entre o imundo e o limpo
11 e para ensinardes aos filhos de Israel todos os estatutos que o Senhor lhes tem falado por intermédio de Moisés.
12 Disse Moisés a Arão e aos filhos deste, Eleazar e Itamar, que lhe ficaram: Tomai a oferta de manjares, restante das ofertas queimadas ao Senhor, e comei-a, sem fermento, junto ao altar, porquanto coisa santíssima é.
13 Comê-la-eis em lugar santo, porque isto é a tua porção e a porção de teus filhos, das ofertas queimadas do Senhor; porque assim me foi ordenado.
14 Também o peito da oferta movida e a coxa da oferta comereis em lugar limpo, tu, e teus filhos, e tuas filhas, porque foram dados por tua porção e por porção de teus filhos, dos sacrifícios pacíficos dos filhos de Israel.
15 A coxa da oferta e o peito da oferta movida trarão com as ofertas queimadas de gordura, para mover por oferta movida perante o Senhor, o que será por estatuto perpétuo, para ti e para teus filhos, como o Senhor tem ordenado.
16 Moisés diligentemente buscou o bode da oferta pelo pecado, e eis que já era queimado; portanto, indignando-se grandemente contra Eleazar e contra Itamar, os filhos que de Arão ficaram, disse:
17 Por que não comestes a oferta pelo pecado no lugar santo? Pois coisa santíssima é; e o Senhor a deu a vós outros, para levardes a iniquidade da congregação, para fazerdes expiação por eles diante do Senhor.
18 Eis que desta oferta não foi trazido o seu sangue para dentro do santuário; certamente, devíeis tê-la comido no santuário, como eu tinha ordenado.
19 Respondeu Arão a Moisés: Eis que, hoje, meus filhos ofereceram a sua oferta pelo pecado e o seu holocausto perante o Senhor; e tais coisas me sucederam; se eu, hoje, tivesse comido a oferta pelo pecado, seria isso, porventura, aceito aos olhos do Senhor?
20 O que ouvindo Moisés, deu-se por satisfeito.*
1 Falou o Senhor a Moisés e a Arão, dizendo-lhes:
2 Dizei aos filhos de Israel: São estes os animais que comereis de todos os quadrúpedes que há sobre a terra:
3 todo o que tem unhas fendidas, e o casco se divide em dois, e rumina, entre os animais, esse comereis.
4 Destes, porém, não comereis: dos que ruminam ou dos que têm unhas fendidas: o camelo, que rumina, mas não tem unhas fendidas; este vos será imundo;
5 o arganaz, porque rumina, mas não tem as unhas fendidas; este vos será imundo;
6 a lebre, porque rumina, mas não tem as unhas fendidas; esta vos será imunda.
7 Também o porco, porque tem unhas fendidas e o casco dividido, mas não rumina; este vos será imundo;
8 da sua carne não comereis, nem tocareis no seu cadáver. Estes vos serão imundos.
9 De todos os animais que há nas águas comereis os seguintes: todo o que tem barbatanas e escamas, nos mares e nos rios; esses comereis.
10 Porém todo o que não tem barbatanas nem escamas, nos mares e nos rios, todos os que enxameiam as águas e todo ser vivente que há nas águas, estes serão para vós outros abominação.
11 Ser-vos-ão, pois, por abominação; da sua carne não comereis e abominareis o seu cadáver.
12 Todo o que nas águas não tem barbatanas ou escamas será para vós outros abominação.
13 Das aves, estas abominareis; não se comerão, serão abominação: a águia, o quebrantosso e a águia marinha;
14 o milhano e o falcão, segundo a sua espécie,
15 todo corvo, segundo a sua espécie,
16 o avestruz, a coruja, a gaivota, o gavião, segundo a sua espécie,
17 o mocho, o corvo marinho, a íbis,
18 a gralha, o pelicano, o abutre,
19 a cegonha, a garça, segundo a sua espécie, a poupa e o morcego.
20 Todo inseto que voa, que anda sobre quatro pés será para vós outros abominação.
21 Mas de todo inseto que voa, que anda sobre quatro pés, cujas pernas traseiras são mais compridas, para saltar com elas sobre a terra, estes comereis.
22 Deles, comereis estes: a locusta, segundo a sua espécie, o gafanhoto devorador, segundo a sua espécie, o grilo, segundo a sua espécie, e o gafanhoto, segundo a sua espécie.
23 Mas todos os outros insetos que voam, que têm quatro pés serão para vós outros abominação.
24 E por estes vos tornareis imundos; qualquer que tocar o seu cadáver imundo será até à tarde.
25 Qualquer que levar o seu cadáver lavará as suas vestes e será imundo até à tarde.
26 Todo animal que tem unhas fendidas, mas o casco não dividido em dois e não rumina vos será por imundo; qualquer que tocar neles será imundo.
27 Todo animal quadrúpede que anda na planta dos pés vos será por imundo; qualquer que tocar o seu cadáver será imundo até à tarde.
28 E o que levar o seu cadáver lavará as suas vestes e será imundo até à tarde; eles vos serão por imundos.
29 Estes vos serão imundos entre o enxame de criaturas que povoam a terra: a doninha, o rato, o lagarto, segundo a sua espécie,
30 o geco, o crocodilo da terra, a lagartixa, o lagarto da areia e o camaleão;
31 estes vos serão por imundos entre todo o enxame de criaturas; qualquer que os tocar, estando eles mortos, será imundo até à tarde.
32 E tudo aquilo sobre que cair qualquer deles, estando eles mortos, será imundo, seja vaso de madeira, ou veste, ou pele, ou pano de saco, ou qualquer instrumento com que se faz alguma obra, será metido em água e será imundo até à tarde; então, será limpo.
33 E todo vaso de barro, dentro do qual cair alguma coisa deles, tudo o que houver nele será imundo; o vaso quebrareis.
34 Todo alimento que se come, preparado com água, será imundo; e todo líquido que se bebe, em todo vaso, será imundo.
35 E aquilo sobre o que cair alguma coisa do seu corpo morto será imundo; se for um forno ou um fogareiro de barro, serão quebrados; imundos são; portanto, vos serão por imundos.
36 Porém a fonte ou cisterna, em que se recolhem águas, será limpa; mas quem tocar no cadáver desses animais será imundo.
37 Se do seu cadáver cair alguma coisa sobre alguma semente de semear, esta será limpa;
38 mas, se alguém deitar água sobre a semente, e, se do cadáver cair alguma coisa sobre ela, vos será imunda.
39 Se morrer algum dos animais de que vos é lícito comer, quem tocar no seu cadáver será imundo até à tarde;
40 quem do seu cadáver comer lavará as suas vestes e será imundo até à tarde; e quem levar o seu corpo morto lavará as suas vestes e será imundo até à tarde.
41 Também todo enxame de criaturas que povoam a terra será abominação; não se comerá.
42 Tudo o que anda sobre o ventre, e tudo o que anda sobre quatro pés ou que tem muitos pés, entre todo enxame de criaturas que povoam a terra, não comereis, porquanto são abominação.
43 Não vos façais abomináveis por nenhum enxame de criaturas, nem por elas vos contaminareis, para não serdes imundos.
44 Eu sou o Senhor, vosso Deus; portanto, vós vos consagrareis e sereis santos, porque eu sou santo; e não vos contaminareis por nenhum enxame de criaturas que se arrastam sobre a terra.
45 Eu sou o Senhor, que vos faço subir da terra do Egito, para que eu seja vosso Deus; portanto, vós sereis santos, porque eu sou santo.
46 Esta é a lei dos animais, e das aves, e de toda alma vivente que se move nas águas, e de toda criatura que povoa a terra,
47 para fazer diferença entre o imundo e o limpo e entre os animais que se podem comer e os animais que se não podem comer.*
1 Disse mais o Senhor a Moisés:
2 Fala aos filhos de Israel: Se uma mulher conceber e tiver um menino, será imunda sete dias; como nos dias da sua menstruação, será imunda.
3 E, no oitavo dia, se circuncidará ao menino a carne do seu prepúcio.
4 Depois, ficará ela trinta e três dias a purificar-se do seu sangue; nenhuma coisa santa tocará, nem entrará no santuário até que se cumpram os dias da sua purificação.
5 Mas, se tiver uma menina, será imunda duas semanas, como na sua menstruação; depois, ficará sessenta e seis dias a purificar-se do seu sangue.
6 E, cumpridos os dias da sua purificação por filho ou filha, trará ao sacerdote um cordeiro de um ano, por holocausto, e um pombinho ou uma rola, por oferta pelo pecado, à porta da tenda da congregação;
7 o sacerdote o oferecerá perante o Senhor e, pela mulher, fará expiação; e ela será purificada do fluxo do seu sangue; esta é a lei da que der à luz menino ou menina.
8 Mas, se as suas posses não lhe permitirem trazer um cordeiro, tomará, então, duas rolas ou dois pombinhos, um para o holocausto e o outro para a oferta pelo pecado; assim, o sacerdote fará expiação pela mulher, e será limpa.*
1 Disse o Senhor a Moisés e a Arão:
2 O homem que tiver na sua pele inchação, ou pústula, ou mancha lustrosa, e isto nela se tornar como praga de lepra, será levado a Arão, o sacerdote, ou a um de seus filhos, sacerdotes.
3 O sacerdote lhe examinará a praga na pele; se o pelo na praga se tornou branco, e a praga parecer mais profunda do que a pele da sua carne, é praga de lepra; o sacerdote o examinará e o declarará imundo.
4 Se a mancha lustrosa na pele for branca e não parecer mais profunda do que a pele, e o pelo não se tornou branco, então, o sacerdote encerrará por sete dias o que tem a praga.
5 Ao sétimo dia, o sacerdote o examinará; se, na sua opinião, a praga tiver parado e não se estendeu na sua pele, então, o sacerdote o encerrará por outros sete dias.
6 O sacerdote, ao sétimo dia, o examinará outra vez; se a lepra se tornou baça e na pele se não estendeu, então, o sacerdote o declarará limpo; é pústula; o homem lavará as suas vestes e será limpo.
7 Mas, se a pústula se estende muito na pele, depois de se ter mostrado ao sacerdote para a sua purificação, outra vez se mostrará ao sacerdote.
8 Este o examinará, e se a pústula se tiver estendido na pele, o sacerdote o declarará imundo; é lepra.
9 Quando no homem houver praga de lepra, será levado ao sacerdote.
10 E o sacerdote o examinará; se há inchação branca na pele, a qual tornou o pelo branco, e houver carne viva na inchação,
11 é lepra inveterada na pele; portanto, o sacerdote o declarará imundo; não o encerrará, porque é imundo.
12 Se a lepra se espalhar de todo na pele e cobrir a pele do que tem a lepra, desde a cabeça até aos pés, quanto podem ver os olhos do sacerdote,
13 então, este o examinará. Se a lepra cobriu toda a sua carne, declarará limpo o que tem a mancha; a lepra tornou-se branca; o homem está limpo.
14 Mas, no dia em que aparecer nele carne viva, será imundo.
15 Vendo, pois, o sacerdote a carne viva, declará-lo-á imundo; a carne viva é imunda; é lepra.
16 Se a carne viva mudar e ficar de novo branca, então, virá ao sacerdote,
17 e este o examinará. Se a lepra se tornou branca, então, o sacerdote declarará limpo o que tem a praga; está limpo.
18 Quando sarar a carne em cuja pele houver uma úlcera,
19 e no lugar da úlcera aparecer uma inchação branca ou mancha lustrosa, branca que tira a vermelho, mostrar-se-á ao sacerdote.
20 O sacerdote a examinará; se ela parece mais funda do que a pele, e o seu pelo se tornou branco, o sacerdote o declarará imundo; praga de lepra é, que brotou da úlcera.
21 Porém, se o sacerdote a examinar, e nela não houver pelo branco, e não estiver ela mais funda do que a pele, porém baça, então, o sacerdote o encerrará por sete dias.
22 Se ela se estender na pele, o sacerdote declarará imundo o homem; é lepra.
23 Mas, se a mancha lustrosa parar no seu lugar, não se estendendo, é cicatriz da úlcera; o sacerdote, pois, o declarará limpo.
24 Quando, na pele, houver queimadura de fogo, e a carne viva da queimadura se tornar em mancha lustrosa, branca que tira a vermelho ou branco,
25 o sacerdote a examinará. Se o pelo da mancha lustrosa se tornou branco, e ela parece mais funda do que a pele, é lepra que brotou na queimadura. O sacerdote declarará imundo o homem; é a praga de lepra.
26 Porém, se o sacerdote a examinar, e não houver pelo branco na mancha lustrosa, e ela não estiver mais funda que a pele, mas for de cor baça, o sacerdote encerrará por sete dias o homem.
27 Depois, o sacerdote o examinará ao sétimo dia; se ela se tiver estendido na pele, o sacerdote o declarará imundo; é praga de lepra.
28 Mas, se a mancha lustrosa parar no seu lugar e na pele não se estender, mas se tornou baça, é inchação da queimadura; portanto, o sacerdote o declarará limpo, porque é cicatriz da queimadura.
29 Quando o homem (ou a mulher) tiver praga na cabeça ou na barba,
30 o sacerdote examinará a praga; se ela parece mais funda do que a pele, e pelo amarelo fino nela houver, o sacerdote o declarará imundo; é tinha, é lepra da cabeça ou da barba.
31 Mas, se o sacerdote, havendo examinado a praga da tinha, achar que ela não parece mais funda do que a pele, e, se nela não houver pelo preto, então, o sacerdote encerrará o que tem a praga da tinha por sete dias.
32 Ao sétimo dia, o sacerdote examinará a praga; se a tinha não se tiver espalhado, e nela não houver pelo amarelo, e a tinha não parecer mais funda do que a pele,
33 então, o homem será rapado; mas não se rapará a tinha. O sacerdote, por mais sete dias, encerrará o que tem a tinha.
34 Ao sétimo dia, o sacerdote examinará a tinha; se ela não se houver estendido na pele e não parecer mais funda do que a pele, o sacerdote declarará limpo o homem; este lavará as suas vestes e será limpo.
35 Mas, se a tinha, depois da sua purificação, se tiver espalhado muito na pele,
36 então, o sacerdote o examinará; se a tinha se tiver espalhado na pele, o sacerdote não procurará pelo amarelo; está imundo.
37 Mas, se a tinha, a seu ver, parou, e pelo preto cresceu nela, a tinha está sarada; ele está limpo, e o sacerdote o declarará limpo.
38 E, quando o homem (ou a mulher) tiver manchas lustrosas na pele,
39 então, o sacerdote o examinará; se na pele aparecerem manchas baças, brancas, é impigem branca que brotou na pele; está limpo.
40 Quando os cabelos do homem lhe caírem da cabeça, é calva; contudo, está limpo.
41 Se lhe caírem na frente da cabeça, é antecalva; contudo, está limpo.
42 Porém, se, na calva ou na antecalva, houver praga branca, que tira a vermelho, é lepra, brotando na calva ou na antecalva.
43 Havendo, pois, o sacerdote examinado, se a inchação da praga, na sua calva ou antecalva, está branca, que tira a vermelho, como parece a lepra na pele,
44 é leproso aquele homem, está imundo; o sacerdote o declarará imundo; a sua praga está na cabeça.
45 As vestes do leproso, em quem está a praga, serão rasgadas, e os seus cabelos serão desgrenhados; cobrirá o bigode e clamará: Imundo! Imundo!
46 Será imundo durante os dias em que a praga estiver nele; é imundo, habitará só; a sua habitação será fora do arraial.
47 Quando também em alguma veste houver praga de lepra, veste de lã ou de linho,
48 seja na urdidura, seja na trama, de linho ou de lã, em pele ou em qualquer obra de peles,
49 se a praga for esverdinhada ou avermelhada na veste, ou na pele, ou na urdidura, ou na trama, em qualquer coisa feita de pele, é a praga de lepra, e mostrar-se-á ao sacerdote.
50 O sacerdote examinará a praga e encerrará, por sete dias, aquilo que tem a praga.
51 Então, examinará a praga ao sétimo dia; se ela se houver estendido na veste, na urdidura ou na trama, seja na pele, seja qual for a obra em que se empregue, é lepra maligna; isso é imundo.
52 Pelo que se queimará aquela veste, seja a urdidura, seja a trama, de lã, ou de linho, ou qualquer coisa feita de pele, em que se acha a praga, pois é lepra maligna; tudo se queimará.
53 Mas, examinando o sacerdote, se a praga não se tiver espalhado na veste, nem na urdidura, nem na trama, nem em qualquer coisa feita de pele,
54 então, o sacerdote ordenará que se lave aquilo em que havia a praga e o encerrará por mais sete dias;
55 o sacerdote, examinando a coisa em que havia praga, depois de lavada aquela, se a praga não mudou a sua cor, nem se espalhou, está imunda; com fogo a queimarás; é lepra roedora, seja no avesso ou no direito.
56 Mas, se o sacerdote examinar a mancha, e esta se tornou baça depois de lavada, então, a rasgará da veste, ou da pele, ou da urdidura, ou da trama.
57 Se a praga ainda aparecer na veste, quer na urdidura, quer na trama, ou em qualquer coisa feita de pele, é lepra que se espalha; com fogo queimarás aquilo em que está a praga.
58 Mas a veste, quer na urdidura, quer na trama, ou qualquer coisa de peles, que lavares e de que a praga se retirar, se lavará segunda vez e será limpa.
59 Esta é a lei da praga da lepra da veste de lã ou de linho, quer na urdidura, quer na trama; ou de qualquer coisa de peles, para se poder declará-las limpas ou imundas.*
do
1 Disse o Senhor a Moisés:
2 Esta será a lei do leproso no dia da sua purificação: será levado ao sacerdote;
3 este sairá fora do arraial e o examinará. Se a praga da lepra do leproso está curada,
4 então, o sacerdote ordenará que se tomem, para aquele que se houver de purificar, duas aves vivas e limpas, e pau de cedro, e estofo carmesim, e hissopo.
5 Mandará também o sacerdote que se imole uma ave num vaso de barro, sobre águas correntes.
6 Tomará a ave viva, e o pau de cedro, e o estofo carmesim, e o hissopo e os molhará no sangue da ave que foi imolada sobre as águas correntes.
7 E, sobre aquele que há de purificar-se da lepra, aspergirá sete vezes; então, o declarará limpo e soltará a ave viva para o campo aberto.
8 Aquele que tem de se purificar lavará as vestes, rapará todo o seu pelo, banhar-se-á com água e será limpo; depois, entrará no arraial, porém ficará fora da sua tenda por sete dias.
9 Ao sétimo dia, rapará todo o seu cabelo, a cabeça, a barba e as sobrancelhas; rapará todo pelo, lavará as suas vestes, banhará o corpo com água e será limpo.
10 No oitavo dia, tomará dois cordeiros sem defeito, uma cordeira sem defeito, de um ano, e três dízimas de um efa de flor de farinha, para oferta de manjares, amassada com azeite, e separadamente um sextário de azeite;
11 e o sacerdote que faz a purificação apresentará o homem que houver de purificar-se e essas coisas diante do Senhor, à porta da tenda da congregação;
12 tomará um dos cordeiros e o oferecerá por oferta pela culpa e o sextário de azeite; e os moverá por oferta movida perante o Senhor.
13 Então, imolará o cordeiro no lugar em que se imola a oferta pelo pecado e o holocausto, no lugar santo; porque quer a oferta pela culpa como a oferta pelo pecado são para o sacerdote; são coisas santíssimas.
14 O sacerdote tomará do sangue da oferta pela culpa e o porá sobre a ponta da orelha direita daquele que tem de purificar-se, e sobre o polegar da sua mão direita, e sobre o polegar do seu pé direito.
15 Também tomará do sextário de azeite e o derramará na palma da própria mão esquerda.
16 Molhará o dedo direito no azeite que está na mão esquerda e daquele azeite aspergirá, com o dedo, sete vezes perante o Senhor;
17 do restante do azeite que está na mão, o sacerdote porá sobre a ponta da orelha direita daquele que tem de purificar-se, e sobre o polegar da sua mão direita, e sobre o polegar do seu pé direito, em cima do sangue da oferta pela culpa;
18 o restante do azeite que está na mão do sacerdote, pô-lo-á sobre a cabeça daquele que tem de purificar-se; assim, o sacerdote fará expiação por ele perante o Senhor.
19 Então, o sacerdote fará a oferta pelo pecado e fará expiação por aquele que tem de purificar-se da sua imundícia. Depois, imolará o holocausto
20 e o oferecerá com a oferta de manjares sobre o altar; assim, o sacerdote fará expiação pelo homem, e este será limpo.
21 Se for pobre, e as suas posses não lhe permitirem trazer tanto, tomará um cordeiro para oferta pela culpa como oferta movida, para fazer expiação por ele, e a dízima de um efa de flor de farinha, amassada com azeite, para oferta de manjares, e um sextário de azeite,
22 duas rolas ou dois pombinhos, segundo as suas posses, dos quais um será para oferta pelo pecado, e o outro, para holocausto.
23 Ao oitavo dia da sua purificação, os trará ao sacerdote, à porta da tenda da congregação, perante o Senhor.
24 O sacerdote tomará o cordeiro da oferta pela culpa e o sextário de azeite e os moverá por oferta movida perante o Senhor.
25 Então, o sacerdote imolará o cordeiro da oferta pela culpa, e tomará do sangue da oferta pela culpa, e o porá sobre a ponta da orelha direita daquele que tem de purificar-se, e sobre o polegar da sua mão direita, e sobre o polegar do seu pé direito.
26 Derramará do azeite na palma da própria mão esquerda;
27 e, com o dedo direito, aspergirá do azeite que está na sua mão esquerda, sete vezes perante o Senhor;
28 porá do azeite que está na sua mão na ponta da orelha direita daquele que tem de purificar-se, e no polegar da sua mão direita, e no polegar do seu pé direito, por cima do sangue da oferta pela culpa;
29 o restante do azeite que está na mão do sacerdote porá sobre a cabeça do que tem de purificar-se, para fazer expiação por ele perante o Senhor.
30 Oferecerá uma das rolas ou um dos pombinhos, segundo as suas posses;
31 será um para oferta pelo pecado, e o outro, para holocausto, além da oferta de manjares; e, assim, o sacerdote fará expiação por aquele que tem de purificar-se perante o Senhor.
32 Esta é a lei daquele em quem está a praga da lepra, cujas posses não lhe permitem o devido para a sua purificação.
33 Disse mais o Senhor a Moisés e a Arão:
34 Quando entrardes na terra de Canaã, que vos darei por possessão, e eu enviar a praga da lepra a alguma casa da terra da vossa possessão,
35 o dono da casa fará saber ao sacerdote, dizendo: Parece-me que há como que praga em minha casa.
36 O sacerdote ordenará que despejem a casa, antes que venha para examinar a praga, para que não seja contaminado tudo o que está na casa; depois, virá o sacerdote, para examinar a casa,
37 e examinará a praga. Se, nas paredes da casa, há manchas esverdinhadas ou avermelhadas e parecem mais fundas que a parede,
38 então, o sacerdote sairá da casa e a cerrará por sete dias.
39 Ao sétimo dia, voltará o sacerdote e examinará; se vir que a praga se estendeu nas paredes da casa,
40 ele ordenará que arranquem as pedras em que estiver a praga e que as lancem fora da cidade num lugar imundo;
41 e fará raspar a casa por dentro, ao redor, e o pó que houverem raspado lançarão, fora da cidade, num lugar imundo.
42 Depois, tomarão outras pedras e as porão no lugar das primeiras; tomar-se-á outra argamassa e se rebocará a casa.
43 Se a praga tornar a brotar na casa, depois de arrancadas as pedras, raspada a casa e de novo rebocada,
44 então, o sacerdote entrará e examinará. Se a praga se tiver estendido na casa, há nela lepra maligna; está imunda.
45 Derribar-se-á, portanto, a casa, as pedras e a sua madeira, como também todo o reboco da casa; e se levará tudo para fora da cidade, a um lugar imundo.
46 Aquele que entrar na casa, enquanto está fechada, será imundo até à tarde.
47 Também o que se deitar na casa lavará as suas vestes; e quem nela comer lavará as suas vestes.
48 Porém, tornando o sacerdote a entrar, e, examinando, se a praga na casa não se tiver estendido depois que a casa foi rebocada, o sacerdote a declarará limpa, porque a praga está curada.
49 Para purificar a casa, tomará duas aves, e pau de cedro, e estofo carmesim, e hissopo,
50 imolará uma ave num vaso de barro sobre águas correntes,
51 tomará o pau de cedro, e o hissopo, e o estofo carmesim, e a ave viva, e os molhará no sangue da ave imolada e nas águas correntes, e aspergirá a casa sete vezes.
52 Assim, purificará aquela casa com o sangue da ave, e com as águas correntes, e com a ave viva, e com o pau de cedro, e com o hissopo, e com o estofo carmesim.
53 Então, soltará a ave viva para fora da cidade, para o campo aberto; assim, fará expiação pela casa, e será limpa.
54 Esta é a lei de toda sorte de praga de lepra, e de tinha,
55 e da lepra das vestes, e das casas,
56 e da inchação, e da pústula, e das manchas lustrosas,
57 para ensinar quando qualquer coisa é limpa ou imunda. Esta é a lei da lepra.*
1 Disse mais o Senhor a Moisés e a Arão:
2 Falai aos filhos de Israel e dizei-lhes: Qualquer homem que tiver fluxo seminal do seu corpo será imundo por causa do fluxo.
3 Esta, pois, será a sua imundícia por causa do seu fluxo: se o seu corpo vaza o fluxo ou se o seu corpo o estanca, esta é a sua imundícia.
4 Toda cama em que se deitar o que tiver fluxo será imunda; e tudo sobre que se assentar será imundo.
5 Qualquer que lhe tocar a cama lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
6 Aquele que se assentar sobre aquilo em que se assentara o que tem o fluxo lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
7 Quem tocar o corpo do que tem o fluxo lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
8 Se o homem que tem o fluxo cuspir sobre uma pessoa limpa, então, esta lavará as suas vestes, banhar-se-á em água e será imunda até à tarde.
9 Também toda sela em que cavalgar o que tem o fluxo será imunda.
10 Qualquer que tocar alguma coisa que esteve debaixo dele será imundo até à tarde; e aquele que a levar lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
11 Também todo aquele em quem tocar o que tiver o fluxo, sem haver lavado as suas mãos com água, lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
12 O vaso de barro em que tocar o que tem o fluxo será quebrado; porém todo vaso de madeira será lavado em água.
13 Quando, pois, o que tem o fluxo dele estiver limpo, contar-se-ão sete dias para a sua purificação; lavará as suas vestes, banhará o corpo em águas correntes e será limpo.
14 Ao oitavo dia, tomará duas rolas ou dois pombinhos, e virá perante o Senhor, à porta da tenda da congregação, e os dará ao sacerdote;
15 este os oferecerá, um, para oferta pelo pecado, e o outro, para holocausto; e, assim, o sacerdote fará, por ele, expiação do seu fluxo perante o Senhor.
16 Também o homem, quando se der com ele emissão do sêmen, banhará todo o seu corpo em água e será imundo até à tarde.
17 Toda veste e toda pele em que houver sêmen se lavarão em água e serão imundas até à tarde.
18 Se um homem coabitar com mulher e tiver emissão do sêmen, ambos se banharão em água e serão imundos até à tarde.
19 A mulher, quando tiver o fluxo de sangue, se este for o fluxo costumado do seu corpo, estará sete dias na sua menstruação, e qualquer que a tocar será imundo até à tarde.
20 Tudo sobre que ela se deitar durante a menstruação será imundo; e tudo sobre que se assentar será imundo.
21 Quem tocar no leito dela lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
22 Quem tocar alguma coisa sobre que ela se tiver assentado lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
23 Também quem tocar alguma coisa que estiver sobre a cama ou sobre aquilo em que ela se assentou, esse será imundo até à tarde.
24 Se um homem coabitar com ela, e a sua menstruação estiver sobre ele, será imundo por sete dias; e toda cama sobre que ele se deitar será imunda.
25 Também a mulher, quando manar fluxo do seu sangue, por muitos dias fora do tempo da sua menstruação ou quando tiver fluxo do sangue por mais tempo do que o costumado, todos os dias do fluxo será imunda, como nos dias da sua menstruação.
26 Toda cama sobre que se deitar durante os dias do seu fluxo ser-lhe-á como a cama da sua menstruação; e toda coisa sobre que se assentar será imunda, conforme a impureza da sua menstruação.
27 Quem tocar estas será imundo; portanto, lavará as suas vestes, banhar-se-á em água e será imundo até à tarde.
28 Porém, quando lhe cessar o fluxo, então, se contarão sete dias, e depois será limpa.
29 Ao oitavo dia, tomará duas rolas ou dois pombinhos e os trará ao sacerdote à porta da tenda da congregação.
30 Então, o sacerdote oferecerá um, para oferta pelo pecado, e o outro, para holocausto; o sacerdote fará, por ela, expiação do fluxo da sua impureza perante o Senhor.
31 Assim, separareis os filhos de Israel das suas impurezas, para que não morram nelas, ao contaminarem o meu tabernáculo, que está no meio deles.
32 Esta é a lei daquele que tem o fluxo, e daquele com quem se dá emissão do sêmen e que fica por ela imundo,
33 e também da mulher passível da sua menstruação, e daquele que tem o fluxo, seja homem ou mulher, e do homem que se deita com mulher imunda.*
1 Falou o Senhor a Moisés, depois que morreram os dois filhos de Arão, tendo chegado aqueles diante do Senhor.
2 Então, disse o Senhor a Moisés: Dize a Arão, teu irmão, que não entre no santuário em todo tempo, para dentro do véu, diante do propiciatório que está sobre a arca, para que não morra; porque aparecerei na nuvem sobre o propiciatório.
3 Entrará Arão no santuário com isto: um novilho, para oferta pelo pecado, e um carneiro, para holocausto.
4 Vestirá ele a túnica de linho, sagrada, terá as calças de linho sobre a pele, cingir-se-á com o cinto de linho e se cobrirá com a mitra de linho; são estas as vestes sagradas. Banhará o seu corpo em água e, então, as vestirá.
5 Da congregação dos filhos de Israel tomará dois bodes, para a oferta pelo pecado, e um carneiro, para holocausto.
6 Arão trará o novilho da sua oferta pelo pecado e fará expiação por si e pela sua casa.
7 Também tomará ambos os bodes e os porá perante o Senhor, à porta da tenda da congregação.
8 Lançará sortes sobre os dois bodes: uma, para o Senhor, e a outra, para o bode emissário.
9 Arão fará chegar o bode sobre o qual cair a sorte para o Senhor e o oferecerá por oferta pelo pecado.
10 Mas o bode sobre que cair a sorte para bode emissário será apresentado vivo perante o Senhor, para fazer expiação por meio dele e enviá-lo ao deserto como bode emissário.
11 Arão fará chegar o novilho da sua oferta pelo pecado e fará expiação por si e pela sua casa; imolará o novilho da sua oferta pelo pecado.
12 Tomará também, de sobre o altar, o incensário cheio de brasas de fogo, diante do Senhor, e dois punhados de incenso aromático bem moído e o trará para dentro do véu.
13 Porá o incenso sobre o fogo, perante o Senhor, para que a nuvem do incenso cubra o propiciatório, que está sobre o Testemunho, para que não morra.
14 Tomará do sangue do novilho e, com o dedo, o aspergirá sobre a frente do propiciatório; e, diante do propiciatório, aspergirá sete vezes do sangue, com o dedo.
15 Depois, imolará o bode da oferta pelo pecado, que será para o povo, e trará o seu sangue para dentro do véu; e fará com o seu sangue como fez com o sangue do novilho; aspergi-lo-á no propiciatório e também diante dele.
16 Assim, fará expiação pelo santuário por causa das impurezas dos filhos de Israel, e das suas transgressões, e de todos os seus pecados. Da mesma sorte, fará pela tenda da congregação, que está com eles no meio das suas impurezas.
17 Nenhum homem estará na tenda da congregação quando ele entrar para fazer propiciação no santuário, até que ele saia depois de feita a expiação por si mesmo, e pela sua casa, e por toda a congregação de Israel.
18 Então, sairá ao altar, que está perante o Senhor, e fará expiação por ele. Tomará do sangue do novilho e do sangue do bode e o porá sobre os chifres do altar, ao redor.
19 Do sangue aspergirá, com o dedo, sete vezes sobre o altar, e o purificará, e o santificará das impurezas dos filhos de Israel.
20 Havendo, pois, acabado de fazer expiação pelo santuário, pela tenda da congregação e pelo altar, então, fará chegar o bode vivo.
21 Arão porá ambas as mãos sobre a cabeça do bode vivo e sobre ele confessará todas as iniquidades dos filhos de Israel, todas as suas transgressões e todos os seus pecados; e os porá sobre a cabeça do bode e enviá-lo-á ao deserto, pela mão de um homem à disposição para isso.
22 Assim, aquele bode levará sobre si todas as iniquidades deles para terra solitária; e o homem soltará o bode no deserto.
23 Depois, Arão virá à tenda da congregação, e despirá as vestes de linho, que havia usado quando entrara no santuário, e ali as deixará.
24 Banhará o seu corpo em água no lugar santo e porá as suas vestes; então, sairá, e oferecerá o seu holocausto e o holocausto do povo, e fará expiação por si e pelo povo.
25 Também queimará a gordura da oferta pelo pecado sobre o altar.
26 E aquele que tiver levado o bode emissário lavará as suas vestes, banhará o seu corpo em água e, depois, entrará no arraial.
27 Mas o novilho e o bode da oferta pelo pecado, cujo sangue foi trazido para fazer expiação no santuário, serão levados fora do arraial; porém as suas peles, a sua carne e o seu excremento se queimarão.
28 Aquele que o queimar lavará as suas vestes, banhará o seu corpo em água e, depois, entrará no arraial.
29 Isso vos será por estatuto perpétuo: no sétimo mês, aos dez dias do mês, afligireis a vossa alma e nenhuma obra fareis, nem o natural nem o estrangeiro que peregrina entre vós.
30 Porque, naquele dia, se fará expiação por vós, para purificar-vos; e sereis purificados de todos os vossos pecados, perante o Senhor.
31 É sábado de descanso solene para vós outros, e afligireis a vossa alma; é estatuto perpétuo.
32 Quem for ungido e consagrado para oficiar como sacerdote no lugar de seu pai fará a expiação, havendo posto as vestes de linho, as vestes santas;
33 fará expiação pelo santuário, pela tenda da congregação e pelo altar; também a fará pelos sacerdotes e por todo o povo da congregação.
34 Isto vos será por estatuto perpétuo, para fazer expiação uma vez por ano pelos filhos de Israel, por causa dos seus pecados. E fez Arão como o Senhor ordenara a Moisés.*
1 Disse o Senhor a Moisés:
2 Fala a Arão, e a seus filhos, e a todos os filhos de Israel e dize-lhes: Isto é o que o Senhor ordenou, dizendo:
3 Qualquer homem da casa de Israel que imolar boi, ou cordeiro, ou cabra, no arraial ou fora dele,
4 e os não trouxer à porta da tenda da congregação, como oferta ao Senhor diante do seu tabernáculo, a tal homem será imputada a culpa do sangue; derramou sangue, pelo que esse homem será eliminado do seu povo;
5 para que os filhos de Israel, trazendo os seus sacrifícios, que imolam em campo aberto, os apresentem ao Senhor, à porta da tenda da congregação, ao sacerdote, e os ofereçam por sacrifícios pacíficos ao Senhor.
6 O sacerdote aspergirá o sangue sobre o altar do Senhor, à porta da tenda da congregação, e queimará a gordura de aroma agradável ao Senhor.
7 Nunca mais oferecerão os seus sacrifícios aos demônios, com os quais eles se prostituem; isso lhes será por estatuto perpétuo nas suas gerações.
8 Dize-lhes, pois: Qualquer homem da casa de Israel ou dos estrangeiros que peregrinam entre vós que oferecer holocausto ou sacrifício
9 e não o trouxer à porta da tenda da congregação, para oferecê-lo ao Senhor, esse homem será eliminado do seu povo.
10 Qualquer homem da casa de Israel ou dos estrangeiros que peregrinam entre vós que comer algum sangue, contra ele me voltarei e o eliminarei do seu povo.
11 Porque a vida da carne está no sangue. Eu vo-lo tenho dado sobre o altar, para fazer expiação pela vossa alma, porquanto é o sangue que fará expiação em virtude da vida.
12 Portanto, tenho dito aos filhos de Israel: nenhuma alma de entre vós comerá sangue, nem o estrangeiro que peregrina entre vós o comerá.
13 Qualquer homem dos filhos de Israel ou dos estrangeiros que peregrinam entre vós que caçar animal ou ave que se come derramará o seu sangue e o cobrirá com pó.
14 Portanto, a vida de toda carne é o seu sangue; por isso, tenho dito aos filhos de Israel: não comereis o sangue de nenhuma carne, porque a vida de toda carne é o seu sangue; qualquer que o comer será eliminado.
15 Todo homem, quer natural, quer estrangeiro, que comer o que morre por si ou dilacerado lavará as suas vestes, banhar-se-á em água e será imundo até à tarde; depois, será limpo.
16 Mas, se não as lavar, nem banhar o corpo, levará sobre si a sua iniquidade.*
1 Disse mais o Senhor a Moisés:
2 Fala aos filhos de Israel e dize-lhes: Eu sou o Senhor, vosso Deus.
3 Não fareis segundo as obras da terra do Egito, em que habitastes, nem fareis segundo as obras da terra de Canaã, para a qual eu vos levo, nem andareis nos seus estatutos.
4 Fareis segundo os meus juízos e os meus estatutos guardareis, para andardes neles. Eu sou o Senhor, vosso Deus.
5 Portanto, os meus estatutos e os meus juízos guardareis; cumprindo-os, o homem viverá por eles. Eu sou o Senhor.
6 Nenhum homem se chegará a qualquer parenta da sua carne, para lhe descobrir a nudez. Eu sou o Senhor.
7 Não descobrirás a nudez de teu pai e de tua mãe; ela é tua mãe; não lhe descobrirás a nudez.
8 Não descobrirás a nudez da mulher de teu pai; é nudez de teu pai.
9 A nudez da tua irmã, filha de teu pai ou filha de tua mãe, nascida em casa ou fora de casa, a sua nudez não descobrirás.
10 A nudez da filha do teu filho ou da filha de tua filha, a sua nudez não descobrirás, porque é tua nudez.
11 Não descobrirás a nudez da filha da mulher de teu pai, gerada de teu pai; ela é tua irmã.
12 A nudez da irmã do teu pai não descobrirás; ela é parenta de teu pai.
13 A nudez da irmã de tua mãe não descobrirás; pois ela é parenta de tua mãe.
14 A nudez do irmão de teu pai não descobrirás; não te chegarás à sua mulher; ela é tua tia.
15 A nudez de tua nora não descobrirás; ela é mulher de teu filho; não lhe descobrirás a nudez.
16 A nudez da mulher de teu irmão não descobrirás; é a nudez de teu irmão.
17 A nudez de uma mulher e de sua filha não descobrirás; não tomarás a filha de seu filho, nem a filha de sua filha, para lhe descobrir a nudez; parentes são; maldade é.
18 E não tomarás com tua mulher outra, de sorte que lhe seja rival, descobrindo a sua nudez com ela durante sua vida.
19 Não te chegarás à mulher, para lhe descobrir a nudez, durante a sua menstruação.
20 Nem te deitarás com a mulher de teu próximo, para te contaminares com ela.
21 E da tua descendência não darás nenhum para dedicar-se a Moloque, nem profanarás o nome de teu Deus. Eu sou o Senhor.
22 Com homem não te deitarás, como se fosse mulher; é abominação.
23 Nem te deitarás com animal, para te contaminares com ele, nem a mulher se porá perante um animal, para ajuntar-se com ele; é confusão.
24 Com nenhuma destas coisas vos contaminareis, porque com todas estas coisas se contaminaram as nações que eu lanço de diante de vós.
25 E a terra se contaminou; e eu visitei nela a sua iniquidade, e ela vomitou os seus moradores.
26 Porém vós guardareis os meus estatutos e os meus juízos, e nenhuma destas abominações fareis, nem o natural, nem o estrangeiro que peregrina entre vós;
27 porque todas estas abominações fizeram os homens desta terra que nela estavam antes de vós; e a terra se contaminou.
28 Não suceda que a terra vos vomite, havendo-a vós contaminado, como vomitou o povo que nela estava antes de vós.
29 Todo que fizer alguma destas abominações, sim, aqueles que as cometerem serão eliminados do seu povo.
30 Portanto, guardareis a obrigação que tendes para comigo, não praticando nenhum dos costumes abomináveis que se praticaram antes de vós, e não vos contaminareis com eles. Eu sou o Senhor, vosso Deus.*
1 Disse o Senhor a Moisés:
2 Fala a toda a congregação dos filhos de Israel e dize-lhes: Santos sereis, porque eu, o Senhor, vosso Deus, sou santo.
3 Cada um respeitará a sua mãe e o seu pai e guardará os meus sábados. Eu sou o Senhor, vosso Deus.
4 Não vos virareis para os ídolos, nem vos fareis deuses de fundição. Eu sou o Senhor, vosso Deus.
5 Quando oferecerdes sacrifício pacífico ao Senhor, oferecê-lo-eis para que sejais aceitos.
6 No dia em que o oferecerdes e no dia seguinte, se comerá; mas o que sobejar, ao terceiro dia, será queimado.
7 Se alguma coisa dele for comida ao terceiro dia, é abominação; não será aceita.
8 Qualquer que o comer levará a sua iniquidade, porquanto profanou coisa santa do Senhor; por isso, será eliminado do seu povo.
9 Quando também segares a messe da tua terra, o canto do teu campo não segarás totalmente, nem as espigas caídas colherás da tua messe.
10 Não rebuscarás a tua vinha, nem colherás os bagos caídos da tua vinha; deixá-los-ás ao pobre e ao estrangeiro. Eu sou o Senhor, vosso Deus.
11 Não furtareis, nem mentireis, nem usareis de falsidade cada um com o seu próximo;
12 nem jurareis falso pelo meu nome, pois profanaríeis o nome do vosso Deus. Eu sou o Senhor.
13 Não oprimirás o teu próximo, nem o roubarás; a paga do jornaleiro não ficará contigo até pela manhã.
14 Não amaldiçoarás o surdo, nem porás tropeço diante do cego; mas temerás o teu Deus. Eu sou o Senhor.
15 Não farás injustiça no juízo, nem favorecendo o pobre, nem comprazendo ao grande; com justiça julgarás o teu próximo.
16 Não andarás como mexeriqueiro entre o teu povo; não atentarás contra a vida do teu próximo. Eu sou o Senhor.
17 Não aborrecerás teu irmão no teu íntimo; mas repreenderás o teu próximo e, por causa dele, não levarás sobre ti pecado.
18 Não te vingarás, nem guardarás ira contra os filhos do teu povo; mas amarás o teu próximo como a ti mesmo. Eu sou o Senhor.
19 Guardarás os meus estatutos; não permitirás que os teus animais se ajuntem com os de espécie diversa; no teu campo, não semearás semente de duas espécies; nem usarás roupa de dois estofos misturados.
20 Se alguém se deitar com uma mulher, se for escrava desposada com outro homem e não for resgatada, nem se lhe houver dado liberdade, então, serão açoitados; não serão mortos, pois não foi libertada.
21 O homem, como oferta pela sua culpa, trará um carneiro ao Senhor, à porta da tenda da congregação.
22 Com o carneiro da oferta pela culpa, o sacerdote fará expiação, por ele, perante o Senhor, pelo pecado que cometeu, e ser-lhe-á perdoado o pecado que cometeu.
23 Quando entrardes na terra e plantardes toda sorte de árvore de comer, ser-vos-á vedado o seu fruto; três anos vos será vedado; dele não se comerá.
24 Porém, no quarto ano, todo o seu fruto será santo, será oferta de louvores ao Senhor.
25 No quinto ano, comereis fruto dela para que vos faça aumentar a sua produção. Eu sou o Senhor, vosso Deus.
26 Não comereis coisa alguma com sangue; não agourareis, nem adivinhareis.
27 Não cortareis o cabelo em redondo, nem danificareis as extremidades da barba.
28 Pelos mortos não ferireis a vossa carne; nem fareis marca nenhuma sobre vós. Eu sou o Senhor.
29 Não contaminarás a tua filha, fazendo-a prostituir-se; para que a terra não se prostitua, nem se encha de maldade.
30 Guardareis os meus sábados e reverenciareis o meu santuário. Eu sou o Senhor.
31 Não vos voltareis para os necromantes, nem para os adivinhos; não os procureis para serdes contaminados por eles. Eu sou o Senhor, vosso Deus.
32 Diante das cãs te levantarás, e honrarás a presença do ancião, e temerás o teu Deus. Eu sou o Senhor.
33 Se o estrangeiro peregrinar na vossa terra, não o oprimireis.
34 Como o natural, será entre vós o estrangeiro que peregrina convosco; amá-lo-eis como a vós mesmos, pois estrangeiros fostes na terra do Egito. Eu sou o Senhor, vosso Deus.
35 Não cometereis injustiça no juízo, nem na vara, nem no peso, nem na medida.
36 Balanças justas, pesos justos, efa justo e justo him tereis. Eu sou o Senhor, vosso Deus, que vos tirei da terra do Egito.
37 Guardareis todos os meus estatutos e todos os meus juízos e os cumprireis. Eu sou o Senhor.*
1 Disse mais o Senhor a Moisés:
2 Também dirás aos filhos de Israel: Qualquer dos filhos de Israel, ou dos estrangeiros que peregrinam em Israel, que der de seus filhos a Moloque será morto; o povo da terra o apedrejará.
3 Voltar-me-ei contra esse homem, e o eliminarei do meio do seu povo, porquanto deu de seus filhos a Moloque, contaminando, assim, o meu santuário e profanando o meu santo nome.
4 Se o povo da terra fechar os olhos para não ver esse homem, quando der de seus filhos a Moloque, e o não matar,
5 então, eu me voltarei contra esse homem e contra a sua família e o eliminarei do meio do seu povo, com todos os que após ele se prostituem com Moloque.
6 Quando alguém se virar para os necromantes e feiticeiros, para se prostituir com eles, eu me voltarei contra ele e o eliminarei do meio do seu povo.
7 Portanto, santificai-vos e sede santos, pois eu sou o Senhor, vosso Deus.
8 Guardai os meus estatutos e cumpri-os. Eu sou o Senhor, que vos santifico.
9 Se um homem amaldiçoar a seu pai ou a sua mãe, será morto; amaldiçoou a seu pai ou a sua mãe; o seu sangue cairá sobre ele.
10 Se um homem adulterar com a mulher do seu próximo, será morto o adúltero e a adúltera.
11 O homem que se deitar com a mulher de seu pai terá descoberto a nudez de seu pai; ambos serão mortos; o seu sangue cairá sobre eles.
12 Se um homem se deitar com a nora, ambos serão mortos; fizeram confusão; o seu sangue cairá sobre eles.
13 Se também um homem se deitar com outro homem, como se fosse mulher, ambos praticaram coisa abominável; serão mortos; o seu sangue cairá sobre eles.
14 Se um homem tomar uma mulher e sua mãe, maldade é; a ele e a elas queimarão, para que não haja maldade no meio de vós.
15 Se também um homem se ajuntar com um animal, será morto; e matarás o animal.
16 Se uma mulher se achegar a algum animal e se ajuntar com ele, matarás tanto a mulher como o animal; o seu sangue cairá sobre eles.
17 Se um homem tomar a sua irmã, filha de seu pai ou filha de sua mãe, e vir a nudez dela, e ela vir a dele, torpeza é; portanto, serão eliminados na presença dos filhos do seu povo; descobriu a nudez de sua irmã; levará sobre si a sua iniquidade.
18 Se um homem se deitar com mulher no tempo da enfermidade dela e lhe descobrir a nudez, descobrindo a sua fonte, e ela descobrir a fonte do seu sangue, ambos serão eliminados do meio do seu povo.
19 Também a nudez da irmã de tua mãe ou da irmã de teu pai não descobrirás; porquanto descobriu a nudez da sua parenta, sobre si levarão a sua iniquidade.
20 Também se um homem se deitar com a sua tia, descobriu a nudez de seu tio; seu pecado sobre si levarão; morrerão sem filhos.
21 Se um homem tomar a mulher de seu irmão, imundícia é; descobriu a nudez de seu irmão; ficarão sem filhos.
22 Guardai, pois, todos os meus estatutos e todos os meus juízos e cumpri-os, para que vos não vomite a terra para a qual vos levo para habitardes nela.
23 Não andeis nos costumes da gente que eu lanço de diante de vós, porque fizeram todas estas coisas; por isso, me aborreci deles.
24 Mas a vós outros vos tenho dito: em herança possuireis a sua terra, e eu vo-la darei para a possuirdes, terra que mana leite e mel. Eu sou o Senhor, vosso Deus, que vos separei dos povos.
25 Fareis, pois, distinção entre os animais limpos e os imundos e entre as aves imundas e as limpas; não vos façais abomináveis por causa dos animais, ou das aves, ou de tudo o que se arrasta sobre a terra, as quais coisas apartei de vós, para tê-las por imundas.
26 Ser-me-eis santos, porque eu, o Senhor, sou santo e separei-vos dos povos, para serdes meus.
27 O homem ou mulher que sejam necromantes ou sejam feiticeiros serão mortos; serão apedrejados; o seu sangue cairá sobre eles.*
1 Disse o Senhor a Moisés: Fala aos sacerdotes, filhos de Arão, e dize-lhes: O sacerdote não se contaminará por causa de um morto entre o seu povo,
2 salvo por seu parente mais chegado: por sua mãe, e por seu pai, e por seu filho, e por sua filha, e por seu irmão;
3 e também por sua irmã virgem, chegada a ele, que ainda não teve marido, pode contaminar-se.
4 Ele, sendo homem principal entre o seu povo, não se contaminará, pois que se profanaria.
5 Não farão calva na sua cabeça e não cortarão as extremidades da barba, nem ferirão a sua carne.
6 Santos serão a seu Deus e não profanarão o nome do seu Deus, porque oferecem as ofertas queimadas do Senhor, o pão de seu Deus; portanto, serão santos.
7 Não tomarão mulher prostituta ou desonrada, nem tomarão mulher repudiada de seu marido, pois o sacerdote é santo a seu Deus.
8 Portanto, o consagrarás, porque oferece o pão do teu Deus. Ele vos será santo, pois eu, o Senhor que vos santifico, sou santo.
9 Se a filha de um sacerdote se desonra, prostituindo-se, profana a seu pai; será queimada.
10 O sumo sacerdote entre seus irmãos, sobre cuja cabeça foi derramado o óleo da unção, e que for consagrado para vestir as vestes sagradas, não desgrenhará os cabelos, nem rasgará as suas vestes.
11 Não se chegará a cadáver algum, nem se contaminará por causa de seu pai ou de sua mãe.
12 Não sairá do santuário, nem profanará o santuário do seu Deus, pois a consagração do óleo da unção do seu Deus está sobre ele. Eu sou o Senhor.
13 Ele tomará por mulher uma virgem.
14 Viúva, ou repudiada, ou desonrada, ou prostituta, estas não tomará, mas virgem do seu povo tomará por mulher.
15 E não profanará a sua descendência entre o seu povo, porque eu sou o Senhor, que o santifico.
16 Disse mais o Senhor a Moisés:
17 Fala a Arão, dizendo: Ninguém dos teus descendentes, nas suas gerações, em quem houver algum defeito se chegará para oferecer o pão do seu Deus.
18 Pois nenhum homem em quem houver defeito se chegará: como homem cego, ou coxo, ou de rosto mutilado, ou desproporcionado,
19 ou homem que tiver o pé quebrado ou mão quebrada,
20 ou corcovado, ou anão, ou que tiver belida no olho, ou sarna, ou impigens, ou que tiver testículo quebrado.
21 Nenhum homem da descendência de Arão, o sacerdote, em quem houver algum defeito se chegará para oferecer as ofertas queimadas do Senhor; ele tem defeito; não se chegará para oferecer o pão do seu Deus.
22 Comerá o pão do seu Deus, tanto do santíssimo como do santo.
23 Porém até ao véu não entrará, nem se chegará ao altar, porque tem defeito, para que não profane os meus santuários, porque eu sou o Senhor, que os santifico.
24 Assim falou Moisés a Arão, aos filhos deste e a todos os filhos de Israel.*
1 Disse o Senhor a Moisés:
2 Dize a Arão e aos seus filhos que se abstenham das coisas sagradas, dedicadas a mim pelos filhos de Israel, para que não profanem o meu santo nome. Eu sou o Senhor.
3 Dize-lhes: Todo homem, que entre as vossas gerações, de toda a vossa descendência, se chegar às coisas sagradas que os filhos de Israel dedicam ao Senhor, tendo sobre si a sua imundícia, aquela alma será eliminada de diante de mim. Eu sou o Senhor.
4 Ninguém da descendência de Arão que for leproso ou tiver fluxo comerá das coisas sagradas, até que seja limpo; como também o que tocar alguma coisa imunda por causa de um morto ou aquele com quem se der a emissão do sêmen;
5 ou qualquer que tocar algum réptil, com o que se faz imundo, ou a algum homem, com o que se faz imundo, seja qual for a sua imundícia.
6 O homem que o tocar será imundo até à tarde e não comerá das coisas sagradas sem primeiro banhar o seu corpo em água.
7 Posto o sol, então, será limpo e, depois, comerá das coisas sagradas, porque isto é o seu pão.
8 Do animal que morre por si mesmo ou é dilacerado não comerá, para, com isso, não contaminar-se. Eu sou o Senhor.
9 Guardarão, pois, a obrigação que têm para comigo, para que, por isso, não levem sobre si pecado e morram, havendo-o profanado. Eu sou o Senhor, que os santifico.
10 Nenhum estrangeiro comerá das coisas sagradas; o hóspede do sacerdote nem o seu jornaleiro comerão das coisas sagradas.
11 Mas, se o sacerdote comprar algum escravo com o seu dinheiro, este comerá delas; os que nascerem na sua casa, estes comerão do seu pão.
12 Quando a filha do sacerdote se casar com estrangeiro, ela não comerá da oferta das coisas sagradas.
13 Mas, se a filha do sacerdote for viúva ou repudiada, e não tiver filhos, e se houver tornado à casa de seu pai, como na sua mocidade, do pão de seu pai comerá; mas nenhum estrangeiro comerá dele.
14 Se alguém, por ignorância, comer a coisa sagrada, ajuntar-se-lhe-á a sua quinta parte e a dará ao sacerdote com a coisa sagrada.
15 Não profanarão as coisas sagradas que os filhos de Israel oferecem ao Senhor,
16 pois assim os fariam levar sobre si a culpa da iniquidade, comendo as coisas sagradas; porque eu sou o Senhor, que os santifico.
17 Disse mais o Senhor a Moisés:
18 Fala a Arão, e a seus filhos, e a todos os filhos de Israel e dize-lhes: Qualquer que, da casa de Israel ou dos estrangeiros em Israel, apresentar a sua oferta, quer em cumprimento de seus votos ou como ofertas voluntárias, que apresentar ao Senhor em holocausto,
19 para que seja aceitável, oferecerá macho sem defeito, ou do gado, ou do rebanho de ovelhas, ou de cabras.
20 Porém todo o que tiver defeito, esse não oferecereis; porque não seria aceito a vosso favor.
21 Quando alguém oferecer sacrifício pacífico ao Senhor, quer em cumprimento de voto ou como oferta voluntária, do gado ou do rebanho, o animal deve ser sem defeito para ser aceitável; nele, não haverá defeito nenhum.
22 O cego, ou aleijado, ou mutilado, ou ulceroso, ou sarnoso, ou cheio de impigens, não os oferecereis ao Senhor e deles não poreis oferta queimada ao Senhor sobre o altar.
23 Porém novilho ou cordeiro desproporcionados poderás oferecer por oferta voluntária, mas, por voto, não será aceito.
24 Não oferecereis ao Senhor animal que tiver os testículos machucados, ou moídos, ou arrancados, ou cortados; nem fareis isso na vossa terra.
25 Também da mão do estrangeiro nenhum desses animais oferecereis como pão do vosso Deus, porque são corrompidos pelo defeito que há neles; não serão aceitos a vosso favor.
26 Disse mais o Senhor a Moisés:
27 Quando nascer o boi, ou cordeiro, ou cabra, sete dias estará com a mãe; do oitavo dia em diante, será aceito por oferta queimada ao Senhor.
28 Ou seja vaca, ou seja ovelha, não imolarás a ela e seu filho, ambos no mesmo dia.
29 Quando oferecerdes sacrifício de louvores ao Senhor, fá-lo-eis para que sejais aceitos.
30 No mesmo dia, será comido; e, dele, nada deixareis ficar até pela manhã. Eu sou o Senhor.
31 Pelo que guardareis os meus mandamentos e os cumprireis. Eu sou o Senhor.
32 Não profanareis o meu santo nome, mas serei santificado no meio dos filhos de Israel. Eu sou o Senhor, que vos santifico,
33 que vos tirei da terra do Egito, para ser o vosso Deus. Eu sou o Senhor.*
1 Disse o Senhor a Moisés:
2 Fala aos filhos de Israel e dize-lhes: As festas fixas do Senhor, que proclamareis, serão santas convocações; são estas as minhas festas.
3 Seis dias trabalhareis, mas o sétimo será o sábado do descanso solene, santa convocação; nenhuma obra fareis; é sábado do Senhor em todas as vossas moradas.
4 São estas as festas fixas do Senhor, as santas convocações, que proclamareis no seu tempo determinado:
5 no mês primeiro, aos catorze do mês, no crepúsculo da tarde, é a Páscoa do Senhor.
6 E aos quinze dias deste mês é a Festa dos Pães Asmos do Senhor; sete dias comereis pães asmos.
7 No primeiro dia, tereis santa convocação; nenhuma obra servil fareis;
8 mas sete dias oferecereis oferta queimada ao Senhor; ao sétimo dia, haverá santa convocação; nenhuma obra servil fareis.
9 Disse mais o Senhor a Moisés:
10 Fala aos filhos de Israel e dize-lhes: Quando entrardes na terra, que vos dou, e segardes a sua messe, então, trareis um molho das primícias da vossa messe ao sacerdote;
11 este moverá o molho perante o Senhor, para que sejais aceitos;
12 no dia imediato ao sábado, o sacerdote o moverá. No dia em que moverdes o molho, oferecereis um cordeiro sem defeito, de um ano, em holocausto ao Senhor.
13 A sua oferta de manjares serão duas dízimas de um efa de flor de farinha, amassada com azeite, para oferta queimada de aroma agradável ao Senhor, e a sua libação será de vinho, a quarta parte de um him.
14 Não comereis pão, nem trigo torrado, nem espigas verdes, até ao dia em que trouxerdes a oferta ao vosso Deus; é estatuto perpétuo por vossas gerações, em todas as vossas moradas.
15 Contareis para vós outros desde o dia imediato ao sábado, desde o dia em que trouxerdes o molho da oferta movida; sete semanas inteiras serão.
16 Até ao dia imediato ao sétimo sábado, contareis cinquenta dias; então, trareis nova oferta de manjares ao Senhor.
17 Das vossas moradas trareis dois pães para serem movidos; de duas dízimas de um efa de farinha serão; levedados se cozerão; são primícias ao Senhor.
18 Com o pão oferecereis sete cordeiros sem defeito de um ano, e um novilho, e dois carneiros; holocausto serão ao Senhor, com a sua oferta de manjares e as suas libações, por oferta queimada de aroma agradável ao Senhor.
19 Também oferecereis um bode, para oferta pelo pecado, e dois cordeiros de um ano, por oferta pacífica.
20 Então, o sacerdote os moverá, com o pão das primícias, por oferta movida perante o Senhor, com os dois cordeiros; santos serão ao Senhor, para o uso do sacerdote.
21 No mesmo dia, se proclamará que tereis santa convocação; nenhuma obra servil fareis; é estatuto perpétuo em todas as vossas moradas, pelas vossas gerações.
22 Quando segardes a messe da vossa terra, não rebuscareis os cantos do vosso campo, nem colhereis as espigas caídas da vossa sega; para o pobre e para o estrangeiro as deixareis. Eu sou o Senhor, vosso Deus.
23 Disse mais o Senhor a Moisés:
24 Fala aos filhos de Israel, dizendo: No mês sétimo, ao primeiro do mês, tereis descanso solene, memorial, com sonidos de trombetas, santa convocação.
25 Nenhuma obra servil fareis, mas trareis oferta queimada ao Senhor.
26 Disse mais o Senhor a Moisés:
27 Mas, aos dez deste mês sétimo, será o Dia da Expiação; tereis santa convocação e afligireis a vossa alma; trareis oferta queimada ao Senhor.
28 Nesse mesmo dia, nenhuma obra fareis, porque é o Dia da Expiação, para fazer expiação por vós perante o Senhor, vosso Deus.
29 Porque toda alma que, nesse dia, se não afligir será eliminada do seu povo.
30 Quem, nesse dia, fizer alguma obra, a esse eu destruirei do meio do seu povo.
31 Nenhuma obra fareis; é estatuto perpétuo pelas vossas gerações, em todas as vossas moradas.
32 Sábado de descanso solene vos será; então, afligireis a vossa alma; aos nove do mês, de uma tarde a outra tarde, celebrareis o vosso sábado.
A Festa dos Tabernáculos
33 Disse mais o Senhor a Moisés:
34 Fala aos filhos de Israel, dizendo: Aos quinze dias deste mês sétimo, será a Festa dos Tabernáculos ao Senhor, por sete dias.
35 Ao primeiro dia, haverá santa convocação; nenhuma obra servil fareis.
36 Sete dias oferecereis ofertas queimadas ao Senhor; ao dia oitavo, tereis santa convocação e oferecereis ofertas queimadas ao Senhor; é reunião solene, nenhuma obra servil fareis.
37 São estas as festas fixas do Senhor, que proclamareis para santas convocações, para oferecer ao Senhor oferta queimada, holocausto e oferta de manjares, sacrifício e libações, cada qual em seu dia próprio,
38 além dos sábados do Senhor, e das vossas dádivas, e de todos os vossos votos, e de todas as vossas ofertas voluntárias que dareis ao Senhor.
39 Porém, aos quinze dias do mês sétimo, quando tiverdes recolhido os produtos da terra, celebrareis a festa do Senhor, por sete dias; ao primeiro dia e também ao oitavo, haverá descanso solene.
40 No primeiro dia, tomareis para vós outros frutos de árvores formosas, ramos de palmeiras, ramos de árvores frondosas e salgueiros de ribeiras; e, por sete dias, vos alegrareis perante o Senhor, vosso Deus.
41 Celebrareis esta como festa ao Senhor, por sete dias cada ano; é estatuto perpétuo pelas vossas gerações; no mês sétimo, a celebrareis.
42 Sete dias habitareis em tendas de ramos; todos os naturais de Israel habitarão em tendas,
43 para que saibam as vossas gerações que eu fiz habitar os filhos de Israel em tendas, quando os tirei da terra do Egito. Eu sou o Senhor, vosso Deus.
44 Assim, declarou Moisés as festas fixas do Senhor aos filhos de Israel.*
1 Disse o Senhor a Moisés:
2 Ordena aos filhos de Israel que te tragam azeite puro de oliveira, batido, para o candelabro, para que haja lâmpada acesa continuamente.
3 Na tenda da congregação fora do véu, que está diante do Testemunho, Arão a conservará em ordem, desde a tarde até pela manhã, de contínuo, perante o Senhor; estatuto perpétuo será este pelas suas gerações.
4 Sobre o candeeiro de ouro puro conservará em ordem as lâmpadas perante o Senhor, continuamente.
5 Também tomarás da flor de farinha e dela cozerás doze pães, cada um dos quais será de duas dízimas de um efa.
6 E os porás em duas fileiras, seis em cada fileira, sobre a mesa de ouro puro, perante o Senhor.
7 Sobre cada fileira porás incenso puro, que será, para o pão, como porção memorial; é oferta queimada ao Senhor.
8 Em cada sábado, Arão os porá em ordem perante o Senhor, continuamente, da parte dos filhos de Israel, por aliança perpétua.
9 E serão de Arão e de seus filhos, os quais os comerão no lugar santo, porque são coisa santíssima para eles, das ofertas queimadas ao Senhor, como estatuto perpétuo.
10 Apareceu entre os filhos de Israel o filho de uma israelita, o qual era filho de um egípcio; o filho da israelita e certo homem israelita contenderam no arraial.
11 Então, o filho da mulher israelita blasfemou o nome do Senhor e o amaldiçoou, pelo que o trouxeram a Moisés. O nome de sua mãe era Selomite, filha de Dibri, da tribo de Dã.
12 E o levaram à prisão, até que se lhes fizesse declaração pela boca do Senhor.
13 Disse o Senhor a Moisés:
14 Tira o que blasfemou para fora do arraial; e todos os que o ouviram porão as mãos sobre a cabeça dele, e toda a congregação o apedrejará.
15 Dirás aos filhos de Israel: Qualquer que amaldiçoar o seu Deus levará sobre si o seu pecado.
16 Aquele que blasfemar o nome do Senhor será morto; toda a congregação o apedrejará; tanto o estrangeiro como o natural, blasfemando o nome do Senhor, será morto.
17 Quem matar alguém será morto.
18 Mas quem matar um animal o restituirá: igual por igual.
19 Se alguém causar defeito em seu próximo, como ele fez, assim lhe será feito:
20 fratura por fratura, olho por olho, dente por dente; como ele tiver desfigurado a algum homem, assim se lhe fará.
21 Quem matar um animal restituirá outro; quem matar um homem será morto.
22 Uma e a mesma lei havereis, tanto para o estrangeiro como para o natural; pois eu sou o Senhor, vosso Deus.
23 Então, falou Moisés aos filhos de Israel que levassem o que tinha blasfemado para fora do arraial e o apedrejassem; e os filhos de Israel fizeram como o Senhor ordenara a Moisés.*
1 Disse o Senhor a Moisés, no monte Sinai:
2 Fala aos filhos de Israel e dize-lhes: Quando entrardes na terra, que vos dou, então, a terra guardará um sábado ao Senhor.
3 Seis anos semearás o teu campo, e seis anos podarás a tua vinha, e colherás os seus frutos.
4 Porém, no sétimo ano, haverá sábado de descanso solene para a terra, um sábado ao Senhor; não semearás o teu campo, nem podarás a tua vinha.
5 O que nascer de si mesmo na tua seara não segarás e as uvas da tua vinha não podada não colherás; ano de descanso solene será para a terra.
6 Mas os frutos da terra em descanso vos serão por alimento, a ti, e ao teu servo, e à tua serva, e ao teu jornaleiro, e ao estrangeiro que peregrina contigo;
7 e ao teu gado, e aos animais que estão na tua terra, todo o seu produto será por mantimento.
8 Contarás sete semanas de anos, sete vezes sete anos, de maneira que os dias das sete semanas de anos te serão quarenta e nove anos.
9 Então, no mês sétimo, aos dez do mês, farás passar a trombeta vibrante; no Dia da Expiação, fareis passar a trombeta por toda a vossa terra.
10 Santificareis o ano quinquagésimo e proclamareis liberdade na terra a todos os seus moradores; ano de jubileu vos será, e tornareis, cada um à sua possessão, e cada um à sua família.
11 O ano quinquagésimo vos será jubileu; não semeareis, nem segareis o que nele nascer de si mesmo, nem nele colhereis as uvas das vinhas não podadas.
12 Porque é jubileu, santo será para vós outros; o produto do campo comereis.
13 Neste Ano do Jubileu, tornareis cada um à sua possessão.
14 Quando venderes alguma coisa ao teu próximo ou a comprares da mão do teu próximo, não oprimas teu irmão.
15 Segundo o número dos anos desde o Jubileu, comprarás de teu próximo; e, segundo o número dos anos das messes, ele venderá a ti.
16 Sendo muitos os anos, aumentarás o preço e, sendo poucos, abaixarás o preço; porque ele te vende o número das messes.
17 Não oprimais ao vosso próximo; cada um, porém, tema a seu Deus; porque eu sou o Senhor, vosso Deus.
18 Observai os meus estatutos, guardai os meus juízos e cumpri-os; assim, habitareis seguros na terra.
19 A terra dará o seu fruto, e comereis a fartar e nela habitareis seguros.
20 Se disserdes: Que comeremos no ano sétimo, visto que não havemos de semear, nem colher a nossa messe?
21 Então, eu vos darei a minha bênção no sexto ano, para que dê fruto por três anos.
22 No oitavo ano, semeareis e comereis da colheita anterior até ao ano nono; até que venha a sua messe, comereis da antiga.
23 Também a terra não se venderá em perpetuidade, porque a terra é minha; pois vós sois para mim estrangeiros e peregrinos.
24 Portanto, em toda a terra da vossa possessão dareis resgate à terra.
25 Se teu irmão empobrecer e vender alguma parte das suas possessões, então, virá o seu resgatador, seu parente, e resgatará o que seu irmão vendeu.
26 Se alguém não tiver resgatador, porém vier a tornar-se próspero e achar o bastante com que a remir,
27 então, contará os anos desde a sua venda, e o que ficar restituirá ao homem a quem vendeu, e tornará à sua possessão.
28 Mas, se as suas posses não lhe permitirem reavê-la, então, a que for vendida ficará na mão do comprador até ao Ano do Jubileu; porém, no Ano do Jubileu, sairá do poder deste, e aquele tornará à sua possessão.
29 Quando alguém vender uma casa de moradia em cidade murada, poderá resgatá-la dentro de um ano a contar de sua venda; durante um ano, será lícito o seu resgate.
30 Se, passando-se-lhe um ano, não for resgatada, então, a casa que estiver na cidade que tem muro ficará em perpetuidade ao que a comprou, pelas suas gerações; não sairá do poder dele no Jubileu.
31 Mas as casas das aldeias que não têm muro em roda serão estimadas como os campos da terra; para elas haverá resgate, e sairão do poder do comprador no Jubileu.
32 Mas, com respeito às cidades dos levitas, às casas das cidades da sua possessão, terão direito perpétuo de resgate os levitas.
33 Se o levita não resgatar a casa que vendeu, então, a casa comprada na cidade da sua possessão sairá do poder do comprador, no Jubileu; porque as casas das cidades dos levitas são a sua possessão no meio dos filhos de Israel.
34 Mas o campo no arrabalde das suas cidades não se venderá, porque lhes é possessão perpétua.
35 Se teu irmão empobrecer, e as suas forças decaírem, então, sustentá-lo-ás. Como estrangeiro e peregrino ele viverá contigo.
36 Não receberás dele juros nem ganho; teme, porém, ao teu Deus, para que teu irmão viva contigo.
37 Não lhe darás teu dinheiro com juros, nem lhe darás o teu mantimento por causa de lucro.
38 Eu sou o Senhor, vosso Deus, que vos tirei da terra do Egito, para vos dar a terra de Canaã e para ser o vosso Deus.
39 Também se teu irmão empobrecer, estando ele contigo, e vender-se a ti, não o farás servir como escravo.
40 Como jornaleiro e peregrino estará contigo; até ao Ano do Jubileu te servirá;
41 então, sairá de tua casa, ele e seus filhos com ele, e tornará à sua família e à possessão de seus pais.
42 Porque são meus servos, que tirei da terra do Egito; não serão vendidos como escravos.
43 Não te assenhorearás dele com tirania; teme, porém, ao teu Deus.
44 Quanto aos escravos ou escravas que tiverdes, virão das nações ao vosso derredor; delas comprareis escravos e escravas.
45 Também os comprareis dos filhos dos forasteiros que peregrinam entre vós, deles e das suas famílias que estiverem convosco, que nasceram na vossa terra; e vos serão por possessão.
46 Deixá-los-eis por herança para vossos filhos depois de vós, para os haverem como possessão; perpetuamente os fareis servir, mas sobre vossos irmãos, os filhos de Israel, não vos assenhoreareis com tirania, um sobre os outros.
47 Quando o estrangeiro ou peregrino que está contigo se tornar rico, e teu irmão junto dele empobrecer e vender-se ao estrangeiro, ou peregrino que está contigo, ou a alguém da família do estrangeiro,
48 depois de haver-se vendido, haverá ainda resgate para ele; um de seus irmãos poderá resgatá-lo:
49 seu tio ou primo o resgatará; ou um dos seus, parente da sua família, o resgatará; ou, se lograr meios, se resgatará a si mesmo.
50 Com aquele que o comprou acertará contas desde o ano em que se vendeu a ele até ao Ano do Jubileu; o preço da sua venda será segundo o número dos anos, conforme se paga a um jornaleiro.
51 Se ainda faltarem muitos anos, devolverá proporcionalmente a eles, do dinheiro pelo qual foi comprado, o preço do seu resgate.
52 Se restarem poucos anos até ao Ano do Jubileu, então, fará contas com ele e pagará, em proporção aos anos restantes, o preço do seu resgate.
53 Como jornaleiro, de ano em ano, estará com ele; não se assenhoreará dele com tirania à tua vista.
54 Se desta sorte se não resgatar, sairá no Ano do Jubileu, ele e seus filhos com ele.
55 Porque os filhos de Israel me são servos; meus servos são eles, os quais tirei da terra do Egito. Eu sou o Senhor, vosso Deus.*
1 Não fareis para vós outros ídolos, nem vos levantareis imagem de escultura nem coluna, nem poreis pedra com figuras na vossa terra, para vos inclinardes a ela; porque eu sou o Senhor, vosso Deus.
2 Guardareis os meus sábados e reverenciareis o meu santuário. Eu sou o Senhor.
3 Se andardes nos meus estatutos, guardardes os meus mandamentos e os cumprirdes,
4 então, eu vos darei as vossas chuvas a seu tempo; e a terra dará a sua messe, e a árvore do campo, o seu fruto.
5 A debulha se estenderá até à vindima, e a vindima, até à sementeira; comereis o vosso pão a fartar e habitareis seguros na vossa terra.
6 Estabelecerei paz na terra; deitar-vos-eis, e não haverá quem vos espante; farei cessar os animais nocivos da terra, e pela vossa terra não passará espada.
7 Perseguireis os vossos inimigos, e cairão à espada diante de vós.
8 Cinco de vós perseguirão a cem, e cem dentre vós perseguirão a dez mil; e os vossos inimigos cairão à espada diante de vós.
9 Para vós outros olharei, e vos farei fecundos, e vos multiplicarei, e confirmarei a minha aliança convosco.
10 Comereis o velho da colheita anterior e, para dar lugar ao novo, tirareis fora o velho.
11 Porei o meu tabernáculo no meio de vós, e a minha alma não vos aborrecerá.
12 Andarei entre vós e serei o vosso Deus, e vós sereis o meu povo.
13 Eu sou o Senhor, vosso Deus, que vos tirei da terra do Egito, para que não fôsseis seus escravos; quebrei os timões do vosso jugo e vos fiz andar eretos.
14 Mas, se me não ouvirdes e não cumprirdes todos estes mandamentos;
15 se rejeitardes os meus estatutos, e a vossa alma se aborrecer dos meus juízos, a ponto de não cumprir todos os meus mandamentos, e violardes a minha aliança,
16 então, eu vos farei isto: porei sobre vós terror, a tísica e a febre ardente, que fazem desaparecer o lustre dos olhos e definhar a vida; e semeareis debalde a vossa semente, porque os vossos inimigos a comerão.
17 Voltar-me-ei contra vós outros, e sereis feridos diante de vossos inimigos; os que vos aborrecerem assenhorear-se-ão de vós e fugireis, sem ninguém vos perseguir.
18 Se ainda assim com isto não me ouvirdes, tornarei a castigar-vos sete vezes mais por causa dos vossos pecados.
19 Quebrantarei a soberba da vossa força e vos farei que os céus sejam como ferro e a vossa terra, como bronze.
20 Debalde se gastará a vossa força; a vossa terra não dará a sua messe, e as árvores da terra não darão o seu fruto.
21 E, se andardes contrariamente para comigo e não me quiserdes ouvir, trarei sobre vós pragas sete vezes mais, segundo os vossos pecados.
22 Porque enviarei para o meio de vós as feras do campo, as quais vos desfilharão, e acabarão com o vosso gado, e vos reduzirão a poucos; e os vossos caminhos se tornarão desertos.
23 Se ainda com isto não vos corrigirdes para volverdes a mim, porém andardes contrariamente comigo,
24 eu também serei contrário a vós outros e eu mesmo vos ferirei sete vezes mais por causa dos vossos pecados.
25 Trarei sobre vós a espada vingadora da minha aliança; e, então, quando vos ajuntardes nas vossas cidades, enviarei a peste para o meio de vós, e sereis entregues na mão do inimigo.
26 Quando eu vos tirar o sustento do pão, dez mulheres cozerão o vosso pão num só forno e vo-lo entregarão por peso; comereis, porém não vos fartareis.
27 Se ainda com isto me não ouvirdes e andardes contrariamente comigo,
28 eu também, com furor, serei contrário a vós outros e vos castigarei sete vezes mais por causa dos vossos pecados.
29 Comereis a carne de vossos filhos e de vossas filhas.
30 Destruirei os vossos altos, e desfarei as vossas imagens do sol, e lançarei o vosso cadáver sobre o cadáver dos vossos deuses; a minha alma se aborrecerá de vós.
31 Reduzirei as vossas cidades a deserto, e assolarei os vossos santuários, e não aspirarei o vosso aroma agradável.
32 Assolarei a terra, e se espantarão disso os vossos inimigos que nela morarem.
33 Espalhar-vos-ei por entre as nações e desembainharei a espada atrás de vós; a vossa terra será assolada, e as vossas cidades serão desertas.
34 Então, a terra folgará nos seus sábados, todos os dias da sua assolação, e vós estareis na terra dos vossos inimigos; nesse tempo, a terra descansará e folgará nos seus sábados.
35 Todos os dias da assolação descansará, porque não descansou nos vossos sábados, quando habitáveis nela.
36 Quanto aos que de vós ficarem, eu lhes meterei no coração tal ansiedade, nas terras dos seus inimigos, que o ruído de uma folha movida os perseguirá; fugirão como quem foge da espada; e cairão sem ninguém os perseguir.
37 Cairão uns sobre os outros como diante da espada, sem ninguém os perseguir; não podereis levantar-vos diante dos vossos inimigos.
38 Perecereis entre as nações, e a terra dos vossos inimigos vos consumirá.
39 Aqueles que dentre vós ficarem serão consumidos pela sua iniquidade nas terras dos vossos inimigos e pela iniquidade de seus pais com eles serão consumidos.
40 Mas, se confessarem a sua iniquidade e a iniquidade de seus pais, na infidelidade que cometeram contra mim, como também confessarem que andaram contrariamente para comigo,
41 pelo que também fui contrário a eles e os fiz entrar na terra dos seus inimigos; se o seu coração incircunciso se humilhar, e tomarem eles por bem o castigo da sua iniquidade,
42 então, me lembrarei da minha aliança com Jacó, e também da minha aliança com Isaque, e também da minha aliança com Abraão, e da terra me lembrarei.
43 Mas a terra na sua assolação, deixada por eles, folgará nos seus sábados; e tomarão eles por bem o castigo da sua iniquidade, visto que rejeitaram os meus juízos e a sua alma se aborreceu dos meus estatutos.
44 Mesmo assim, estando eles na terra dos seus inimigos, não os rejeitarei, nem me aborrecerei deles, para consumi-los e invalidar a minha aliança com eles, porque eu sou o Senhor, seu Deus.
45 Antes, por amor deles, me lembrarei da aliança com os seus antepassados, que tirei da terra do Egito à vista das nações, para lhes ser por Deus. Eu sou o Senhor.
46 São estes os estatutos, juízos e leis que deu o Senhor entre si e os filhos de Israel, no monte Sinai, pela mão de Moisés.*
1 Disse mais o Senhor a Moisés:
2 Fala aos filhos de Israel e dize-lhes: Quando alguém fizer voto com respeito a pessoas, estas serão do Senhor, segundo a tua avaliação.
3 Se o objeto da tua avaliação for homem, da idade de vinte anos até à de sessenta, será a tua avaliação de cinquenta siclos de prata, segundo o siclo do santuário.
4 Porém, se for mulher, a tua avaliação será de trinta siclos.
5 Se a idade for de cinco anos até vinte, a tua avaliação do homem será de vinte siclos, e a da mulher, de dez siclos.
6 Se a idade for de um mês até cinco anos, a tua avaliação do homem será de cinco siclos de prata, e a tua avaliação pela mulher será de três siclos de prata.
7 De sessenta anos para cima, se for homem, a tua avaliação será de quinze siclos; se mulher, dez siclos.
8 Mas, se for mais pobre do que a tua avaliação, então, apresentar-se-á diante do sacerdote, para que este o avalie; segundo o que permitem as posses do que fez o voto, o avaliará o sacerdote.
9 Se for animal dos que se oferecem ao Senhor, tudo quanto dele se der ao Senhor será santo.
10 Não o mudará, nem o trocará bom por mau ou mau por bom; porém, se dalgum modo se trocar animal por animal, um e outro serão santos.
11 Se for animal imundo dos que se não oferecem ao Senhor, então, apresentará o animal diante do sacerdote.
12 O sacerdote o avaliará, seja bom ou mau; segundo a avaliação do sacerdote, assim será.
13 Porém, se dalgum modo o resgatar, então, acrescentará a quinta parte à tua avaliação.
14 Quando alguém dedicar a sua casa para ser santa ao Senhor, o sacerdote a avaliará, seja boa ou seja má; como o sacerdote a avaliar, assim será.
15 Mas, se aquele que a dedicou quiser resgatar a casa, então, acrescentará a quinta parte do dinheiro à tua avaliação, e será sua.
16 Se alguém dedicar ao Senhor parte do campo da sua herança, então, a tua avaliação será segundo a semente necessária para o semear: um gômer pleno de cevada será avaliado por cinquenta siclos de prata.
17 Se dedicar o seu campo desde o Ano do Jubileu, segundo a tua plena avaliação, ficará.
18 Mas, se dedicar o seu campo depois do Ano do Jubileu, então, o sacerdote lhe contará o dinheiro segundo os anos restantes até ao Ano do Jubileu, e isto se abaterá da tua avaliação.
19 Se aquele que dedicou o campo dalgum modo o quiser resgatar, então, acrescentará a quinta parte do dinheiro à tua avaliação, e ficará seu.
20 Se não quiser resgatar o campo ou se o vender a outro homem, nunca mais se resgatará.
21 Porém, havendo o campo saído livre no Ano do Jubileu, será santo ao Senhor, como campo consagrado; a posse dele será do sacerdote.
22 Se alguém dedicar ao Senhor o campo que comprou, e não for parte da sua herança,
23 então, o sacerdote lhe contará o preço da avaliação até ao Ano do Jubileu; e, no mesmo dia, dará o importe da avaliação como coisa santa ao Senhor.
24 No Ano do Jubileu, o campo tornará àquele que o vendeu, àquele de quem era a posse do campo por herança.
25 Toda a tua avaliação se fará segundo o siclo do santuário; o siclo será de vinte geras.
26 Mas o primogênito de um animal, por já pertencer ao Senhor, ninguém o dedicará; seja boi ou gado miúdo, é do Senhor.
27 Mas, se for de um animal imundo, resgatar-se-á, segundo a tua avaliação, e sobre ele acrescentará a quinta parte; se não for resgatado, vender-se-á, segundo a tua avaliação.
28 No entanto, nada do que alguém dedicar irremissivelmente ao Senhor, de tudo o que tem, seja homem, ou animal, ou campo da sua herança, se poderá vender, nem resgatar; toda coisa assim consagrada será santíssima ao Senhor.
29 Ninguém que dentre os homens for dedicado irremissivelmente ao Senhor se poderá resgatar; será morto.
30 Também todas as dízimas da terra, tanto dos cereais do campo como dos frutos das árvores, são do Senhor; santas são ao Senhor.
31 Se alguém, das suas dízimas, quiser resgatar alguma coisa, acrescentará a sua quinta parte sobre ela.
32 No tocante às dízimas do gado e do rebanho, de tudo o que passar debaixo do bordão do pastor, o dízimo será santo ao Senhor.
33 Não se investigará se é bom ou mau, nem o trocará; mas, se dalgum modo o trocar, um e outro serão santos; não serão resgatados.
34 São estes os mandamentos que o Senhor ordenou a Moisés, para os filhos de Israel, no monte Sinai.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Levítico','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)