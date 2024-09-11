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
1 As palavras de Neemias, filho de Hacalias. No mês de quisleu, no ano vigésimo, estando eu na cidadela de Susã,
2 veio Hanani, um de meus irmãos, com alguns de Judá; então, lhes perguntei pelos judeus que escaparam e que não foram levados para o exílio e acerca de Jerusalém.
3 Disseram-me: Os restantes, que não foram levados para o exílio e se acham lá na província, estão em grande miséria e desprezo; os muros de Jerusalém estão derribados, e as suas portas, queimadas.
4 Tendo eu ouvido estas palavras, assentei-me, e chorei, e lamentei por alguns dias; e estive jejuando e orando perante o Deus dos céus.
5 E disse: ah! Senhor, Deus dos céus, Deus grande e temível, que guardas a aliança e a misericórdia para com aqueles que te amam e guardam os teus mandamentos!
6 Estejam, pois, atentos os teus ouvidos, e os teus olhos, abertos, para acudires à oração do teu servo, que hoje faço à tua presença, dia e noite, pelos filhos de Israel, teus servos; e faço confissão pelos pecados dos filhos de Israel, os quais temos cometido contra ti; pois eu e a casa de meu pai temos pecado.
7 Temos procedido de todo corruptamente contra ti, não temos guardado os mandamentos, nem os estatutos, nem os juízos que ordenaste a Moisés, teu servo.
8 Lembra-te da palavra que ordenaste a Moisés, teu servo, dizendo: Se transgredirdes, eu vos espalharei por entre os povos;
9 mas, se vos converterdes a mim, e guardardes os meus mandamentos, e os cumprirdes, então, ainda que os vossos rejeitados estejam pelas extremidades do céu, de lá os ajuntarei e os trarei para o lugar que tenho escolhido para ali fazer habitar o meu nome.
10 Estes ainda são teus servos e o teu povo que resgataste com teu grande poder e com tua mão poderosa.
11 Ah! Senhor, estejam, pois, atentos os teus ouvidos à oração do teu servo e à dos teus servos que se agradam de temer o teu nome; concede que seja bem-sucedido hoje o teu servo e dá-lhe mercê perante este homem. Nesse tempo eu era copeiro do rei.*
1 No mês de nisã, no ano vigésimo do rei Artaxerxes, uma vez posto o vinho diante dele, eu o tomei para oferecer e lho dei; ora, eu nunca antes estivera triste diante dele.
2 O rei me disse: Por que está triste o teu rosto, se não estás doente? Tem de ser tristeza do coração. Então, temi sobremaneira
3 e lhe respondi: viva o rei para sempre! Como não me estaria triste o rosto se a cidade, onde estão os sepulcros de meus pais, está assolada e tem as portas consumidas pelo fogo?
4 Disse-me o rei: Que me pedes agora? Então, orei ao Deus dos céus
5 e disse ao rei: se é do agrado do rei, e se o teu servo acha mercê em tua presença, peço-te que me envies a Judá, à cidade dos sepulcros de meus pais, para que eu a reedifique.
6 Então, o rei, estando a rainha assentada junto dele, me disse: Quanto durará a tua ausência? Quando voltarás? Aprouve ao rei enviar-me, e marquei certo prazo.
7 E ainda disse ao rei: Se ao rei parece bem, deem-se-me cartas para os governadores dalém do Eufrates, para que me permitam passar e entrar em Judá,
8 como também carta para Asafe, guarda das matas do rei, para que me dê madeira para as vigas das portas da cidadela do templo, para os muros da cidade e para a casa em que deverei alojar-me. E o rei mas deu, porque a boa mão do meu Deus era comigo.
9 Então, fui aos governadores dalém do Eufrates e lhes entreguei as cartas do rei; ora, o rei tinha enviado comigo oficiais do exército e cavaleiros.
10 Disto ficaram sabendo Sambalate, o horonita, e Tobias, o servo amonita; e muito lhes desagradou que alguém viesse a procurar o bem dos filhos de Israel.
11 Cheguei a Jerusalém, onde estive três dias.
12 Então, à noite me levantei, e uns poucos homens, comigo; não declarei a ninguém o que o meu Deus me pusera no coração para eu fazer em Jerusalém. Não havia comigo animal algum, senão o que eu montava.
13 De noite, saí pela Porta do Vale, para o lado da Fonte do Dragão e para a Porta do Monturo e contemplei os muros de Jerusalém, que estavam assolados, cujas portas tinham sido consumidas pelo fogo.
14 Passei à Porta da Fonte e ao açude do rei; mas não havia lugar por onde passasse o animal que eu montava.
15 Subi à noite pelo ribeiro e contemplei ainda os muros; voltei, entrei pela Porta do Vale e tornei para casa.
16 Não sabiam os magistrados aonde eu fora nem o que fazia, pois até aqui não havia eu declarado coisa alguma, nem aos judeus, nem aos sacerdotes, nem aos nobres, nem aos magistrados, nem aos mais que faziam a obra.
17 Então, lhes disse: Estais vendo a miséria em que estamos, Jerusalém assolada, e as suas portas, queimadas; vinde, pois, reedifiquemos os muros de Jerusalém e deixemos de ser opróbrio.
18 E lhes declarei como a boa mão do meu Deus estivera comigo e também as palavras que o rei me falara. Então, disseram: Disponhamo-nos e edifiquemos. E fortaleceram as mãos para a boa obra.
19 Porém Sambalate, o horonita, e Tobias, o servo amonita, e Gesém, o arábio, quando o souberam, zombaram de nós, e nos desprezaram, e disseram: Que é isso que fazeis? Quereis rebelar-vos contra o rei?
20 Então, lhes respondi: o Deus dos céus é quem nos dará bom êxito; nós, seus servos, nos disporemos e reedificaremos; vós, todavia, não tendes parte, nem direito, nem memorial em Jerusalém.*
1 Então, se dispôs Eliasibe, o sumo sacerdote, com os sacerdotes, seus irmãos, e reedificaram a Porta das Ovelhas; consagraram-na, assentaram-lhe as portas e continuaram a reconstrução até à Torre dos Cem e à Torre de Hananel.
2 Junto a ele edificaram os homens de Jericó; também, ao seu lado, edificou Zacur, filho de Inri.
3 Os filhos de Hassenaá edificaram a Porta do Peixe; colocaram-lhe as vigas e lhe assentaram as portas com seus ferrolhos e trancas.
4 Ao seu lado, reparou Meremote, filho de Urias, filho de Coz; junto deste reparou Mesulão, filho de Berequias, filho de Mesezabel, a cujo lado reparou Zadoque, filho de Baaná.
5 Ao lado destes, repararam os tecoítas; os seus nobres, porém, não se sujeitaram ao serviço do seu senhor.
6 Joiada, filho de Paseia, e Mesulão, filho de Besodias, repararam a Porta Velha; colocaram-lhe as vigas e lhe assentaram as portas com seus ferrolhos e trancas.
7 Junto deles, trabalharam Melatias, gibeonita, e Jadom, meronotita, homens de Gibeão e de Mispa, que pertenciam ao domínio do governador de além do Eufrates.
8 Ao seu lado, reparou Uziel, filho de Haraías, um dos ourives; junto dele, Hananias, um dos perfumistas; e restauraram Jerusalém até ao Muro Largo.
9 Junto a estes, trabalhou Refaías, filho de Hur, maioral da metade de Jerusalém.
10 Ao seu lado, reparou Jedaías, filho de Harumafe, defronte da sua casa; e, ao seu lado, reparou Hatus, filho de Hasabneias.
11 A outra parte reparou Malquias, filho de Harim, e Hassube, filho de Paate-Moabe, como também a Torre dos Fornos.
12 Ao lado dele, reparou Salum, filho de Haloés, maioral da outra meia parte de Jerusalém, ele e suas filhas.
13 A Porta do Vale, reparou-a Hanum e os moradores de Zanoa; edificaram-na e lhe assentaram as portas com seus ferrolhos e trancas e ainda mil côvados da muralha, até à Porta do Monturo.
14 A Porta do Monturo, reparou-a Malquias, filho de Recabe, maioral do distrito de Bete-Haquerém; ele a edificou e lhe assentou as portas com seus ferrolhos e trancas.
15 A Porta da Fonte, reparou-a Salum, filho de Col-Hozé, maioral do distrito de Mispa; ele a edificou, e a cobriu, e lhe assentou as portas com seus ferrolhos e trancas, e ainda o muro do açude de Selá, junto ao jardim do rei, até aos degraus que descem da Cidade de Davi.
16 Depois dele, reparou Neemias, filho de Azbuque, maioral da metade do distrito de Bete-Zur, até defronte dos sepulcros de Davi, até ao açude artificial e até à casa dos heróis.
17 Depois dele, repararam os levitas, Reum, filho de Bani, e, ao seu lado, Hasabias, maioral da metade do distrito de Queila.
18 Depois dele, repararam seus irmãos: Bavai, filho de Henadade, maioral da metade do distrito de Queila;
19 ao seu lado, reparou Ezer, filho de Jesua, maioral de Mispa, outra parte defronte da subida para a casa das armas, no ângulo do muro.
20 Depois dele, reparou com grande ardor Baruque, filho de Zabai, outra porção, desde o ângulo do muro até à porta da casa de Eliasibe, o sumo sacerdote.
21 Depois dele, reparou Meremote, filho de Urias, filho de Coz, outra porção, desde a porta da casa de Eliasibe até à extremidade da casa de Eliasibe.
22 Depois dele, repararam os sacerdotes que habitavam na campina.
23 Depois, repararam Benjamim e Hassube, defronte da sua casa; depois deles, reparou Azarias, filho de Maaseias, filho de Ananias, junto à sua casa.
24 Depois dele, reparou Binui, filho de Henadade, outra porção, desde a casa de Azarias até ao ângulo e até à esquina.
25 Palal, filho de Uzai, reparou defronte do ângulo e da torre que sai da casa real superior, que está junto ao pátio do cárcere; depois dele, reparou Pedaías, filho de Parós,
26 e os servos do templo que habitavam em Ofel, até defronte da Porta das Águas, para o oriente, e até à torre alta.
27 Depois, repararam os tecoítas outra porção, defronte da torre grande e alta, e até ao Muro de Ofel.
28 Para cima da Porta dos Cavalos, repararam os sacerdotes, cada um defronte da sua casa.
29 Depois deles, reparou Zadoque, filho de Imer, defronte de sua casa; e, depois dele, Semaías, filho de Secanias, guarda da Porta Oriental.
30 Depois dele, reparou Hananias, filho de Selemias, e Hanum, o sexto filho de Zalafe, outra porção; depois deles, reparou Mesulão, filho de Berequias, defronte da sua morada.
31 Depois dele, reparou Malquias, filho de um ourives, até à casa dos servos do templo e dos mercadores, defronte da Porta da Guarda, até ao eirado da esquina.
32 Entre o eirado da esquina e a Porta das Ovelhas, repararam os ourives e os mercadores.*
1 Tendo Sambalate ouvido que edificávamos o muro, ardeu em ira, e se indignou muito, e escarneceu dos judeus.
2 Então, falou na presença de seus irmãos e do exército de Samaria e disse: Que fazem estes fracos judeus? Permitir-se-lhes-á isso? Sacrificarão? Darão cabo da obra num só dia? Renascerão, acaso, dos montões de pó as pedras que foram queimadas?
3 Estava com ele Tobias, o amonita, e disse: Ainda que edifiquem, vindo uma raposa, derribará o seu muro de pedra.
4 Ouve, ó nosso Deus, pois estamos sendo desprezados; caia o seu opróbrio sobre a cabeça deles, e faze que sejam despojo numa terra de cativeiro.
5 Não lhes encubras a iniquidade, e não se risque de diante de ti o seu pecado, pois te provocaram à ira, na presença dos que edificavam.
6 Assim, edificamos o muro, e todo o muro se fechou até a metade de sua altura; porque o povo tinha ânimo para trabalhar.
7 Mas, ouvindo Sambalate e Tobias, os arábios, os amonitas e os asdoditas que a reparação dos muros de Jerusalém ia avante e que já se começavam a fechar-lhe as brechas, ficaram sobremodo irados.
8 Ajuntaram-se todos de comum acordo para virem atacar Jerusalém e suscitar confusão ali.
9 Porém nós oramos ao nosso Deus e, como proteção, pusemos guarda contra eles, de dia e de noite.
10 Então, disse Judá: Já desfaleceram as forças dos carregadores, e os escombros são muitos; de maneira que não podemos edificar o muro.
11 Disseram, porém, os nossos inimigos: Nada saberão disto, nem verão, até que entremos no meio deles e os matemos; assim, faremos cessar a obra.
12 Quando os judeus que habitavam na vizinhança deles, dez vezes, nos disseram: De todos os lugares onde moram, subirão contra nós,
13 então, pus o povo, por famílias, nos lugares baixos e abertos, por detrás do muro, com as suas espadas, e as suas lanças, e os seus arcos;
14 inspecionei, dispus-me e disse aos nobres, aos magistrados e ao resto do povo: não os temais; lembrai-vos do Senhor, grande e temível, e pelejai pelos vossos irmãos, vossos filhos, vossas filhas, vossa mulher e vossa casa.
15 E sucedeu que, ouvindo os nossos inimigos que já o sabíamos e que Deus tinha frustrado o desígnio deles, voltamos todos nós ao muro, cada um à sua obra.
16 Daquele dia em diante, metade dos meus moços trabalhava na obra, e a outra metade empunhava lanças, escudos, arcos e couraças; e os chefes estavam por detrás de toda a casa de Judá;
17 os carregadores, que por si mesmos tomavam as cargas, cada um com uma das mãos fazia a obra e com a outra segurava a arma.
18 Os edificadores, cada um trazia a sua espada à cinta, e assim edificavam; o que tocava a trombeta estava junto de mim.
19 Disse eu aos nobres, aos magistrados e ao resto do povo: Grande e extensa é a obra, e nós estamos no muro mui separados, longe uns dos outros.
20 No lugar em que ouvirdes o som da trombeta, para ali acorrei a ter conosco; o nosso Deus pelejará por nós.
21 Assim trabalhávamos na obra; e metade empunhava as lanças desde o raiar do dia até ao sair das estrelas.
22 Também nesse mesmo tempo disse eu ao povo: Cada um com o seu moço fique em Jerusalém, para que de noite nos sirvam de guarda e de dia trabalhem.
23 Nem eu, nem meus irmãos, nem meus moços, nem os homens da guarda que me seguiam largávamos as nossas vestes; cada um se deitava com as armas à sua direita.*
1 Foi grande, porém, o clamor do povo e de suas mulheres contra os judeus, seus irmãos.
2 Porque havia os que diziam: Somos muitos, nós, nossos filhos e nossas filhas; que se nos dê trigo, para que comamos e vivamos.
3 Também houve os que diziam: As nossas terras, as nossas vinhas e as nossas casas hipotecamos para tomarmos trigo nesta fome.
4 Houve ainda os que diziam: Tomamos dinheiro emprestado até para o tributo do rei, sobre as nossas terras e as nossas vinhas.
5 No entanto, nós somos da mesma carne como eles, e nossos filhos são tão bons como os deles; e eis que sujeitamos nossos filhos e nossas filhas para serem escravos, algumas de nossas filhas já estão reduzidas à escravidão. Não está em nosso poder evitá-lo; pois os nossos campos e as nossas vinhas já são de outros.
6 Ouvindo eu, pois, o seu clamor e estas palavras, muito me aborreci.
7 Depois de ter considerado comigo mesmo, repreendi os nobres e magistrados e lhes disse: Sois usurários, cada um para com seu irmão; e convoquei contra eles um grande ajuntamento.
8 Disse-lhes: nós resgatamos os judeus, nossos irmãos, que foram vendidos às gentes, segundo nossas posses; e vós outra vez negociaríeis vossos irmãos, para que sejam vendidos a nós?
9 Então, se calaram e não acharam o que responder. Disse mais: não é bom o que fazeis; porventura não devíeis andar no temor do nosso Deus, por causa do opróbrio dos gentios, os nossos inimigos?
10 Também eu, meus irmãos e meus moços lhes demos dinheiro emprestado e trigo. Demos de mão a esse empréstimo.
11 Restituí-lhes hoje, vos peço, as suas terras, as suas vinhas, os seus olivais e as suas casas, como também o centésimo do dinheiro, do trigo, do vinho e do azeite, que exigistes deles.
12 Então, responderam: Restituir-lhes-emos e nada lhes pediremos; faremos assim como dizes. Então, chamei os sacerdotes e os fiz jurar que fariam segundo prometeram.
13 Também sacudi o meu regaço e disse: Assim o faça Deus, sacuda de sua casa e de seu trabalho a todo homem que não cumprir esta promessa; seja sacudido e despojado. E toda a congregação respondeu: Amém! E louvaram o Senhor; e o povo fez segundo a sua promessa.
14 Também desde o dia em que fui nomeado seu governador na terra de Judá, desde o vigésimo ano até ao trigésimo segundo ano do rei Artaxerxes, doze anos, nem eu nem meus irmãos comemos o pão devido ao governador.
15 Mas os primeiros governadores, que foram antes de mim, oprimiram o povo e lhe tomaram pão e vinho, além de quarenta siclos de prata; até os seus moços dominavam sobre o povo, porém eu assim não fiz, por causa do temor de Deus.
16 Antes, também na obra deste muro fiz reparação, e terra nenhuma compramos; e todos os meus moços se ajuntaram ali para a obra.
17 Também cento e cinquenta homens dos judeus e dos magistrados e os que vinham a nós, dentre as gentes que estavam ao nosso redor, eram meus hóspedes.
18 O que se preparava para cada dia era um boi e seis ovelhas escolhidas; também à minha custa eram preparadas aves e, de dez em dez dias, muito vinho de todas as espécies; nem por isso exigi o pão devido ao governador, porquanto a servidão deste povo era grande.
19 Lembra-te de mim para meu bem, ó meu Deus, e de tudo quanto fiz a este povo.*
1 Tendo ouvido Sambalate, Tobias, Gesém, o arábio, e o resto dos nossos inimigos que eu tinha edificado o muro e que nele já não havia brecha nenhuma, ainda que até este tempo não tinha posto as portas nos portais,
2 Sambalate e Gesém mandaram dizer-me: Vem, encontremo-nos, nas aldeias, no vale de Ono. Porém intentavam fazer-me mal.
3 Enviei-lhes mensageiros a dizer: Estou fazendo grande obra, de modo que não poderei descer; por que cessaria a obra, enquanto eu a deixasse e fosse ter convosco?
4 Quatro vezes me enviaram o mesmo pedido; eu, porém, lhes dei sempre a mesma resposta.
5 Então, Sambalate me enviou pela quinta vez o seu moço, o qual trazia na mão uma carta aberta,
6 do teor seguinte: Entre as gentes se ouviu, e Gesém diz que tu e os judeus intentais revoltar-vos; por isso, reedificas o muro, e, segundo se diz, queres ser o rei deles,
7 e puseste profetas para falarem a teu respeito em Jerusalém, dizendo: Este é rei em Judá. Ora, o rei ouvirá isso, segundo essas palavras. Vem, pois, agora, e consultemos juntamente.
8 Mandei dizer-lhe: De tudo o que dizes coisa nenhuma sucedeu; tu, do teu coração, é que o inventas.
9 Porque todos eles procuravam atemorizar-nos, dizendo: As suas mãos largarão a obra, e não se efetuará. Agora, pois, ó Deus, fortalece as minhas mãos.
10 Tendo eu ido à casa de Semaías, filho de Delaías, filho de Meetabel (que estava encerrado), disse ele: Vamos juntamente à Casa de Deus, ao meio do templo, e fechemos as portas do templo; porque virão matar-te; aliás, de noite virão matar-te.
11 Porém eu disse: homem como eu fugiria? E quem há, como eu, que entre no templo para que viva? De maneira nenhuma entrarei.
12 Então, percebi que não era Deus quem o enviara; tal profecia falou ele contra mim, porque Tobias e Sambalate o subornaram.
13 Para isto o subornaram, para me atemorizar, e para que eu, assim, viesse a proceder e a pecar, para que tivessem motivo de me infamar e me vituperassem.
14 Lembra-te, meu Deus, de Tobias e de Sambalate, no tocante a estas suas obras, e também da profetisa Noadia e dos mais profetas que procuraram atemorizar-me.
15 Acabou-se, pois, o muro aos vinte e cinco dias do mês de elul, em cinquenta e dois dias.
16 Sucedeu que, ouvindo-o todos os nossos inimigos, temeram todos os gentios nossos circunvizinhos e decaíram muito no seu próprio conceito; porque reconheceram que por intervenção de nosso Deus é que fizemos esta obra.
17 Também naqueles dias alguns nobres de Judá escreveram muitas cartas, que iam para Tobias, e cartas de Tobias vinham para eles.
18 Pois muitos em Judá lhe eram ajuramentados porque era genro de Secanias, filho de Ará; e seu filho Joanã se casara com a filha de Mesulão, filho de Berequias.
19 Também das suas boas ações falavam na minha presença, e as minhas palavras lhe levavam a ele; Tobias escrevia cartas para me atemorizar.*
1 Ora, uma vez reedificado o muro e assentadas as portas, estabelecidos os porteiros, os cantores e os levitas,
2 eu nomeei Hanani, meu irmão, e Hananias, maioral do castelo, sobre Jerusalém. Hananias era homem fiel e temente a Deus, mais do que muitos outros.
3 E lhes disse: não se abram as portas de Jerusalém até que o sol aqueça e, enquanto os guardas ainda estão ali, que se fechem as portas e se tranquem; ponham-se guardas dos moradores de Jerusalém, cada um no seu posto diante de sua casa.
4 A cidade era espaçosa e grande, mas havia pouca gente nela, e as casas não estavam edificadas ainda.
5 Então, o meu Deus me pôs no coração que ajuntasse os nobres, os magistrados e o povo, para registrar as genealogias. Achei o livro da genealogia dos que subiram primeiro, e nele estava escrito:
6 São estes os filhos da província que subiram do cativeiro, dentre os exilados, que Nabucodonosor, rei da Babilônia, levara para o exílio e que voltaram para Jerusalém e para Judá, cada um para a sua cidade,
7 os quais vieram com Zorobabel, Jesua, Neemias, Azarias, Raamias, Naamani, Mordecai, Bilsã, Misperete, Bigvai, Neum e Baaná. Este é o número dos homens do povo de Israel:
8 foram os filhos de Parós, dois mil cento e setenta e dois.
9 Os filhos de Sefatias, trezentos e setenta e dois.
10 Os filhos de Ará, seiscentos e cinquenta e dois.
11 Os filhos de Paate-Moabe, dos filhos de Jesua e de Joabe, dois mil oitocentos e dezoito.
12 Os filhos de Elão, mil duzentos e cinquenta e quatro.
13 Os filhos de Zatu, oitocentos e quarenta e cinco.
14 Os filhos de Zacai, setecentos e sessenta.
15 Os filhos de Binui, seiscentos e quarenta e oito.
16 Os filhos de Bebai, seiscentos e vinte e oito.
17 Os filhos de Azgade, dois mil trezentos e vinte e dois.
18 Os filhos de Adonicão, seiscentos e sessenta e sete.
19 Os filhos de Bigvai, dois mil e sessenta e sete.
20 Os filhos de Adim, seiscentos e cinquenta e cinco.
21 Os filhos de Ater, da família de Ezequias, noventa e oito.
22 Os filhos de Hasum, trezentos e vinte e oito.
23 Os filhos de Besai, trezentos e vinte e quatro.
24 Os filhos de Harife, cento e doze.
25 Os filhos de Gibeão, noventa e cinco.
26 Os homens de Belém e de Netofa, cento e oitenta e oito.
27 Os homens de Anatote, cento e vinte e oito.
28 Os homens de Bete-Azmavete, quarenta e dois.
29 Os homens de Quiriate-Jearim, Cefira e Beerote, setecentos e quarenta e três.
30 Os homens de Ramá e Geba, seiscentos e vinte e um.
31 Os homens de Micmás, cento e vinte e dois.
32 Os homens de Betel e Ai, cento e vinte e três.
33 Os homens do outro Nebo, cinquenta e dois.
34 Os filhos do outro Elão, mil duzentos e cinquenta e quatro.
35 Os filhos de Harim, trezentos e vinte.
36 Os filhos de Jericó, trezentos e quarenta e cinco.
37 Os filhos de Lode, Hadide e Ono, setecentos e vinte e um.
38 Os filhos de Senaá, três mil novecentos e trinta.
39 Os sacerdotes: os filhos de Jedaías, da casa de Jesua, novecentos e setenta e três.
40 Os filhos de Imer, mil e cinquenta e dois.
41 Os filhos de Pasur, mil duzentos e quarenta e sete.
42 Os filhos de Harim, mil e dezessete.
43 Os levitas: os filhos de Jesua, de Cadmiel, dos filhos de Hodeva, setenta e quatro.
44 Os cantores: os filhos de Asafe, cento e quarenta e oito.
45 Os porteiros: os filhos de Salum, os filhos de Ater, os filhos de Talmom, os filhos de Acube, os filhos de Hatita, os filhos de Sobai, cento e trinta e oito.
46 Os servidores do templo: os filhos de Zia, os filhos de Hasufa, os filhos de Tabaote,
47 os filhos de Queros, os filhos de Sia, os filhos de Padom,
48 os filhos de Lebana, os filhos de Hagaba, os filhos de Salmai,
49 os filhos de Hanã, os filhos de Gidel, os filhos de Gaar,
50 os filhos de Reaías, os filhos de Rezim, os filhos de Necoda,
51 os filhos de Gazão, os filhos de Uzá, os filhos de Paseia,
52 os filhos de Besai, os filhos de Meunim, os filhos de Nefusesim,
53 os filhos de Baquebuque, os filhos de Hacufa, os filhos de Harur,
54 os filhos de Bazlite, os filhos de Meída, os filhos de Harsa,
55 os filhos de Barcos, os filhos de Sísera, os filhos de Tama,
56 os filhos de Nesias e os filhos de Hatifa.
57 Os filhos dos servos de Salomão: os filhos de Sotai, os filhos de Soferete, os filhos de Perida,
58 os filhos de Jaala, os filhos de Darcom, os filhos de Gidel,
59 os filhos de Sefatias, os filhos de Hatil, os filhos de Poquerete-Hazebaim e os filhos de Amom.
60 Todos os servidores do templo e os filhos dos servos de Salomão, trezentos e noventa e dois.
61 Os seguintes subiram de Tel-Melá, Tel-Harsa, Querube, Adom e Imer, porém não puderam provar que as suas famílias e a sua linhagem eram de Israel:
62 os filhos de Delaías, os filhos de Tobias, os filhos de Necoda, seiscentos e quarenta e dois.
63 Dos sacerdotes: os filhos de Habaías, os filhos de Coz, os filhos de Barzilai, o qual se casou com uma das filhas de Barzilai, o gileadita, e que foi chamado pelo nome dele.
64 Estes procuraram o seu registro nos livros genealógicos, porém o não acharam; pelo que foram tidos por imundos para o sacerdócio.
65 O governador lhes disse que não comessem das coisas sagradas, até que se levantasse um sacerdote com Urim e Tumim.
66 Toda esta congregação junta foi de quarenta e dois mil trezentos e sessenta,
67 afora os seus servos e as suas servas, que foram sete mil trezentos e trinta e sete; e tinham duzentos e quarenta e cinco cantores e cantoras.
68 Os seus cavalos, setecentos e trinta e seis; os seus mulos, duzentos e quarenta e cinco.
69 Camelos, quatrocentos e trinta e cinco; jumentos, seis mil setecentos e vinte.
5 Então, o meu Deus me pôs no coração que ajuntasse os nobres, os magistrados e o povo, para registrar as genealogias. Achei o livro da genealogia dos que subiram primeiro, e nele estava escrito:
6 São estes os filhos da província que subiram do cativeiro, dentre os exilados, que Nabucodonosor, rei da Babilônia, levara para o exílio e que voltaram para Jerusalém e para Judá, cada um para a sua cidade,
7 os quais vieram com Zorobabel, Jesua, Neemias, Azarias, Raamias, Naamani, Mordecai, Bilsã, Misperete, Bigvai, Neum e Baaná. Este é o número dos homens do povo de Israel:
8 foram os filhos de Parós, dois mil cento e setenta e dois.
9 Os filhos de Sefatias, trezentos e setenta e dois.
10 Os filhos de Ará, seiscentos e cinquenta e dois.
11 Os filhos de Paate-Moabe, dos filhos de Jesua e de Joabe, dois mil oitocentos e dezoito.
12 Os filhos de Elão, mil duzentos e cinquenta e quatro.
13 Os filhos de Zatu, oitocentos e quarenta e cinco.
14 Os filhos de Zacai, setecentos e sessenta.
15 Os filhos de Binui, seiscentos e quarenta e oito.
16 Os filhos de Bebai, seiscentos e vinte e oito.
17 Os filhos de Azgade, dois mil trezentos e vinte e dois.
18 Os filhos de Adonicão, seiscentos e sessenta e sete.
19 Os filhos de Bigvai, dois mil e sessenta e sete.
20 Os filhos de Adim, seiscentos e cinquenta e cinco.
21 Os filhos de Ater, da família de Ezequias, noventa e oito.
22 Os filhos de Hasum, trezentos e vinte e oito.
23 Os filhos de Besai, trezentos e vinte e quatro.
24 Os filhos de Harife, cento e doze.
25 Os filhos de Gibeão, noventa e cinco.
26 Os homens de Belém e de Netofa, cento e oitenta e oito.
27 Os homens de Anatote, cento e vinte e oito.
28 Os homens de Bete-Azmavete, quarenta e dois.
29 Os homens de Quiriate-Jearim, Cefira e Beerote, setecentos e quarenta e três.
30 Os homens de Ramá e Geba, seiscentos e vinte e um.
31 Os homens de Micmás, cento e vinte e dois.
32 Os homens de Betel e Ai, cento e vinte e três.
33 Os homens do outro Nebo, cinquenta e dois.
34 Os filhos do outro Elão, mil duzentos e cinquenta e quatro.
35 Os filhos de Harim, trezentos e vinte.
36 Os filhos de Jericó, trezentos e quarenta e cinco.
37 Os filhos de Lode, Hadide e Ono, setecentos e vinte e um.
38 Os filhos de Senaá, três mil novecentos e trinta.
39 Os sacerdotes: os filhos de Jedaías, da casa de Jesua, novecentos e setenta e três.
40 Os filhos de Imer, mil e cinquenta e dois.
41 Os filhos de Pasur, mil duzentos e quarenta e sete.
42 Os filhos de Harim, mil e dezessete.
43 Os levitas: os filhos de Jesua, de Cadmiel, dos filhos de Hodeva, setenta e quatro.
44 Os cantores: os filhos de Asafe, cento e quarenta e oito.
45 Os porteiros: os filhos de Salum, os filhos de Ater, os filhos de Talmom, os filhos de Acube, os filhos de Hatita, os filhos de Sobai, cento e trinta e oito.
46 Os servidores do templo: os filhos de Zia, os filhos de Hasufa, os filhos de Tabaote,
47 os filhos de Queros, os filhos de Sia, os filhos de Padom,
48 os filhos de Lebana, os filhos de Hagaba, os filhos de Salmai,
49 os filhos de Hanã, os filhos de Gidel, os filhos de Gaar,
50 os filhos de Reaías, os filhos de Rezim, os filhos de Necoda,
51 os filhos de Gazão, os filhos de Uzá, os filhos de Paseia,
52 os filhos de Besai, os filhos de Meunim, os filhos de Nefusesim,
53 os filhos de Baquebuque, os filhos de Hacufa, os filhos de Harur,
54 os filhos de Bazlite, os filhos de Meída, os filhos de Harsa,
55 os filhos de Barcos, os filhos de Sísera, os filhos de Tama,
56 os filhos de Nesias e os filhos de Hatifa.
57 Os filhos dos servos de Salomão: os filhos de Sotai, os filhos de Soferete, os filhos de Perida,
58 os filhos de Jaala, os filhos de Darcom, os filhos de Gidel,
59 os filhos de Sefatias, os filhos de Hatil, os filhos de Poquerete-Hazebaim e os filhos de Amom.
60 Todos os servidores do templo e os filhos dos servos de Salomão, trezentos e noventa e dois.
61 Os seguintes subiram de Tel-Melá, Tel-Harsa, Querube, Adom e Imer, porém não puderam provar que as suas famílias e a sua linhagem eram de Israel:
62 os filhos de Delaías, os filhos de Tobias, os filhos de Necoda, seiscentos e quarenta e dois.
63 Dos sacerdotes: os filhos de Habaías, os filhos de Coz, os filhos de Barzilai, o qual se casou com uma das filhas de Barzilai, o gileadita, e que foi chamado pelo nome dele.
64 Estes procuraram o seu registro nos livros genealógicos, porém o não acharam; pelo que foram tidos por imundos para o sacerdócio.
65 O governador lhes disse que não comessem das coisas sagradas, até que se levantasse um sacerdote com Urim e Tumim.
66 Toda esta congregação junta foi de quarenta e dois mil trezentos e sessenta,
67 afora os seus servos e as suas servas, que foram sete mil trezentos e trinta e sete; e tinham duzentos e quarenta e cinco cantores e cantoras.
68 Os seus cavalos, setecentos e trinta e seis; os seus mulos, duzentos e quarenta e cinco.
69 Camelos, quatrocentos e trinta e cinco; jumentos, seis mil setecentos e vinte.*
1 Em chegando o sétimo mês, e estando os filhos de Israel nas suas cidades, todo o povo se ajuntou como um só homem, na praça, diante da Porta das Águas; e disseram a Esdras, o escriba, que trouxesse o Livro da Lei de Moisés, que o Senhor tinha prescrito a Israel.
2 Esdras, o sacerdote, trouxe a Lei perante a congregação, tanto de homens como de mulheres e de todos os que eram capazes de entender o que ouviam. Era o primeiro dia do sétimo mês.
3 E leu no livro, diante da praça, que está fronteira à Porta das Águas, desde a alva até ao meio-dia, perante homens e mulheres e os que podiam entender; e todo o povo tinha os ouvidos atentos ao Livro da Lei.
4 Esdras, o escriba, estava num púlpito de madeira, que fizeram para aquele fim; estavam em pé junto a ele, à sua direita, Matitias, Sema, Anaías, Urias, Hilquias e Maaseias; e à sua esquerda, Pedaías, Misael, Malquias, Hasum, Hasbadana, Zacarias e Mesulão.
5 Esdras abriu o livro à vista de todo o povo, porque estava acima dele; abrindo-o ele, todo o povo se pôs em pé.
6 Esdras bendisse ao Senhor, o grande Deus; e todo o povo respondeu: Amém! Amém! E, levantando as mãos; inclinaram-se e adoraram o Senhor, com o rosto em terra.
7 E Jesua, Bani, Serebias, Jamim, Acube, Sabetai, Hodias, Maaseias, Quelita, Azarias, Jozabade, Hanã, Pelaías e os levitas ensinavam o povo na Lei; e o povo estava no seu lugar.
8 Leram no livro, na Lei de Deus, claramente, dando explicações, de maneira que entendessem o que se lia.
9 Neemias, que era o governador, e Esdras, sacerdote e escriba, e os levitas que ensinavam todo o povo lhe disseram: Este dia é consagrado ao Senhor, vosso Deus, pelo que não pranteeis, nem choreis. Porque todo o povo chorava, ouvindo as palavras da Lei.
10 Disse-lhes mais: ide, comei carnes gordas, tomai bebidas doces e enviai porções aos que não têm nada preparado para si; porque este dia é consagrado ao nosso Senhor; portanto, não vos entristeçais, porque a alegria do Senhor é a vossa força.
11 Os levitas fizeram calar todo o povo, dizendo: Calai-vos, porque este dia é santo; e não estejais contristados.
12 Então, todo o povo se foi a comer, a beber, a enviar porções e a regozijar-se grandemente, porque tinham entendido as palavras que lhes foram explicadas.
13 No dia seguinte, ajuntaram-se a Esdras, o escriba, os cabeças das famílias de todo o povo, os sacerdotes e os levitas, e isto para atentarem nas palavras da Lei.
14 Acharam escrito na Lei que o Senhor ordenara por intermédio de Moisés que os filhos de Israel habitassem em cabanas, durante a festa do sétimo mês;
15 que publicassem e fizessem passar pregão por todas as suas cidades e em Jerusalém, dizendo: Saí ao monte e trazei ramos de oliveiras, ramos de zambujeiros, ramos de murtas, ramos de palmeiras e ramos de árvores frondosas, para fazer cabanas, como está escrito.
16 Saiu, pois, o povo, trouxeram os ramos e fizeram para si cabanas, cada um no seu terraço, e nos seus pátios, e nos átrios da Casa de Deus, e na praça da Porta das Águas, e na praça da Porta de Efraim.
17 Toda a congregação dos que tinham voltado do cativeiro fez cabanas e nelas habitou; porque nunca fizeram assim os filhos de Israel, desde os dias de Josué, filho de Num, até àquele dia; e houve mui grande alegria.
18 Dia após dia, leu Esdras no Livro da Lei de Deus, desde o primeiro dia até ao último; e celebraram a festa por sete dias; no oitavo dia, houve uma assembleia solene, segundo o prescrito.*
1 No dia vinte e quatro deste mês, se ajuntaram os filhos de Israel com jejum e pano de saco e traziam terra sobre si.
2 Os da linhagem de Israel se apartaram de todos os estranhos, puseram-se em pé e fizeram confissão dos seus pecados e das iniquidades de seus pais.
3 Levantando-se no seu lugar, leram no Livro da Lei do Senhor, seu Deus, uma quarta parte do dia; em outra quarta parte dele fizeram confissão e adoraram o Senhor, seu Deus.
4 Jesua, Bani, Cadmiel, Sebanias, Buni, Serebias, Bani e Quenani se puseram em pé no estrado dos levitas e clamaram em alta voz ao Senhor, seu Deus.
5 Os levitas Jesua, Cadmiel, Bani, Hasabneias, Serebias, Hodias, Sebanias e Petaías disseram: Levantai-vos, bendizei ao Senhor, vosso Deus, de eternidade em eternidade. Então, se disse: Bendito seja o nome da tua glória, que ultrapassa todo bendizer e louvor.
6 Só tu és Senhor, tu fizeste o céu, o céu dos céus e todo o seu exército, a terra e tudo quanto nela há, os mares e tudo quanto há neles; e tu os preservas a todos com vida, e o exército dos céus te adora.
7 Tu és o Senhor, o Deus que elegeste Abrão, e o tiraste de Ur dos caldeus, e lhe puseste por nome Abraão.
8 Achaste o seu coração fiel perante ti e com ele fizeste aliança, para dares à sua descendência a terra dos cananeus, dos heteus, dos amorreus, dos ferezeus, dos jebuseus e dos girgaseus; e cumpriste as tuas promessas, porquanto és justo.
9 Viste a aflição de nossos pais no Egito, e lhes ouviste o clamor junto ao mar Vermelho.
10 Fizeste sinais e milagres contra Faraó e seus servos e contra todo o povo da sua terra, porque soubeste que os trataram com soberba; e, assim, adquiriste renome, como hoje se vê.
11 Dividiste o mar perante eles, de maneira que o atravessaram em seco; lançaste os seus perseguidores nas profundezas, como uma pedra nas águas impetuosas.
12 Guiaste-os, de dia, por uma coluna de nuvem e, de noite, por uma coluna de fogo, para lhes alumiar o caminho por onde haviam de ir.
13 Desceste sobre o monte Sinai, do céu falaste com eles e lhes deste juízos retos, leis verdadeiras, estatutos e mandamentos bons.
14 O teu santo sábado lhes fizeste conhecer; preceitos, estatutos e lei, por intermédio de Moisés, teu servo, lhes mandaste.
15 Pão dos céus lhes deste na sua fome e água da rocha lhes fizeste brotar na sua sede; e lhes disseste que entrassem para possuírem a terra que, com mão levantada, lhes juraste dar.
16 Porém eles, nossos pais, se houveram soberbamente, e endureceram a sua cerviz, e não deram ouvidos aos teus mandamentos.
17 Recusaram ouvir-te e não se lembraram das tuas maravilhas, que lhes fizeste; endureceram a sua cerviz e na sua rebelião levantaram um chefe, com o propósito de voltarem para a sua servidão no Egito. Porém tu, ó Deus perdoador, clemente e misericordioso, tardio em irar-te e grande em bondade, tu não os desamparaste,
18 ainda mesmo quando fizeram para si um bezerro de fundição e disseram: Este é o teu Deus, que te tirou do Egito; e cometeram grandes blasfêmias.
19 Todavia, tu, pela multidão das tuas misericórdias, não os deixaste no deserto. A coluna de nuvem nunca se apartou deles de dia, para os guiar pelo caminho, nem a coluna de fogo de noite, para lhes alumiar o caminho por onde haviam de ir.
20 E lhes concedeste o teu bom Espírito, para os ensinar; não lhes negaste para a boca o teu maná; e água lhes deste na sua sede.
21 Desse modo os sustentaste quarenta anos no deserto, e nada lhes faltou; as suas vestes não envelheceram, e os seus pés não se incharam.
22 Também lhes deste reinos e povos, que lhes repartiste em porções; assim, possuíram a terra de Seom, a saber, a terra do rei de Hesbom e a terra de Ogue, rei de Basã.
23 Multiplicaste os seus filhos como as estrelas do céu e trouxeste-os à terra de que tinhas dito a seus pais que nela entrariam para a possuírem.
24 Entraram os filhos e tomaram posse da terra; abateste perante eles os moradores da terra, os cananeus, e lhos entregaste nas mãos, como também os reis e os povos da terra, para fazerem deles segundo a sua vontade.
25 Tomaram cidades fortificadas e terra fértil e possuíram casas cheias de toda sorte de coisas boas, cisternas cavadas, vinhas e olivais e árvores frutíferas em abundância; comeram, e se fartaram, e engordaram, e viveram em delícias, pela tua grande bondade.
26 Ainda assim foram desobedientes e se revoltaram contra ti; viraram as costas à tua lei e mataram os teus profetas, que protestavam contra eles, para os fazerem voltar a ti; e cometeram grandes blasfêmias.
27 Pelo que os entregaste nas mãos dos seus opressores, que os angustiaram; mas no tempo de sua angústia, clamando eles a ti, dos céus tu os ouviste; e, segundo a tua grande misericórdia, lhes deste libertadores que os salvaram das mãos dos que os oprimiam.
28 Porém, quando se viam em descanso, tornavam a fazer o mal diante de ti; e tu os desamparavas nas mãos dos seus inimigos, para que dominassem sobre eles; mas, convertendo-se eles e clamando a ti, tu os ouviste dos céus e, segundo a tua misericórdia, os livraste muitas vezes.
29 Testemunhaste contra eles, para que voltassem à tua lei; porém eles se houveram soberbamente e não deram ouvidos aos teus mandamentos, mas pecaram contra os teus juízos, pelo cumprimento dos quais o homem viverá; obstinadamente deram de ombros, endureceram a cerviz e não quiseram ouvir.
30 No entanto, os aturaste por muitos anos e testemunhaste contra eles pelo teu Espírito, por intermédio dos teus profetas; porém eles não deram ouvidos; pelo que os entregaste nas mãos dos povos de outras terras.
31 Mas, pela tua grande misericórdia, não acabaste com eles nem os desamparaste; porque tu és Deus clemente e misericordioso.
32 Agora, pois, ó Deus nosso, ó Deus grande, poderoso e temível, que guardas a aliança e a misericórdia, não menosprezes toda a aflição que nos sobreveio, a nós, aos nossos reis, aos nossos príncipes, aos nossos sacerdotes, aos nossos profetas, aos nossos pais e a todo o teu povo, desde os dias dos reis da Assíria até ao dia de hoje.
33 Porque tu és justo em tudo quanto tem vindo sobre nós; pois tu fielmente procedeste, e nós, perversamente.
34 Os nossos reis, os nossos príncipes, os nossos sacerdotes e os nossos pais não guardaram a tua lei, nem deram ouvidos aos teus mandamentos e aos teus testemunhos, que testificaste contra eles.
35 Pois eles no seu reino, na muita abundância de bens que lhes deste, na terra espaçosa e fértil que puseste diante deles não te serviram, nem se converteram de suas más obras.
36 Eis que hoje somos servos; e até na terra que deste a nossos pais, para comerem o seu fruto e o seu bem, eis que somos servos nela.
37 Seus abundantes produtos são para os reis que puseste sobre nós por causa dos nossos pecados; e, segundo a sua vontade, dominam sobre o nosso corpo e sobre o nosso gado; estamos em grande angústia.
38 Por causa de tudo isso, estabelecemos aliança fiel e o escrevemos; e selaram-na os nossos príncipes, os nossos levitas e os nossos sacerdotes.*
1 Os que selaram foram: Neemias, o governador, filho de Hacalias, e Zedequias,
2 Seraías, Azarias, Jeremias,
3 Pasur, Amarias, Malquias,
4 Hatus, Sebanias, Maluque,
5 Harim, Meremote, Obadias,
6 Daniel, Ginetom, Baruque,
7 Mesulão, Abias, Miamim,
8 Maazias, Bilgai, Semaías; estes eram os sacerdotes.
9 E os levitas: Jesua, filho de Azanias, Binui, dos filhos de Henadade, Cadmiel
10 e os irmãos deles: Sebanias, Hodias, Quelita, Pelaías, Hanã,
11 Mica, Reobe, Hasabias,
12 Zacur, Serebias, Sebanias,
13 Hodias, Bani e Beninu.
14 Os chefes do povo: Parós, Paate-Moabe, Elão, Zatu, Bani,
15 Buni, Azgade, Bebai,
16 Adonias, Bigvai, Adim,
17 Ater, Ezequias, Azur,
18 Hodias, Hasum, Besai,
19 Harife, Anatote, Nebai,
20 Magpias, Mesulão, Hezir,
21 Mesezabel, Zadoque, Jadua,
22 Pelatias, Hanã, Anaías,
23 Oseias, Hananias, Hassube,
24 Haloés, Pilha, Sobeque,
25 Reum, Hasabna, Maaseias,
26 Aías, Hanã, Anã,
27 Maluque, Harim e Baaná.
28 O resto do povo, os sacerdotes, os levitas, os porteiros, os cantores, os servidores do templo e todos os que se tinham separado dos povos de outras terras para a Lei de Deus, suas mulheres, seus filhos e suas filhas, todos os que tinham saber e entendimento,
29 firmemente aderiram a seus irmãos; seus nobres convieram, numa imprecação e num juramento, de que andariam na Lei de Deus, que foi dada por intermédio de Moisés, servo de Deus, de que guardariam e cumpririam todos os mandamentos do Senhor, nosso Deus, e os seus juízos e os seus estatutos;
30 de que não dariam as suas filhas aos povos da terra, nem tomariam as filhas deles para os seus filhos;
31 de que, trazendo os povos da terra no dia de sábado qualquer mercadoria e qualquer cereal para venderem, nada comprariam deles no sábado, nem no dia santificado; e de que, no ano sétimo, abririam mão da colheita e de toda e qualquer cobrança.
32 Também sobre nós pusemos preceitos, impondo-nos cada ano a terça parte de um siclo para o serviço da casa do nosso Deus,
33 e para os pães da proposição, e para a contínua oferta de manjares, e para o contínuo holocausto dos sábados e das Festas da Lua Nova, e para as festas fixas, e para as coisas sagradas, e para as ofertas pelo pecado, e para fazer expiação por Israel, e para toda a obra da casa do nosso Deus.
34 Nós, os sacerdotes, os levitas e o povo deitamos sortes acerca da oferta da lenha que se havia de trazer à casa do nosso Deus, segundo as nossas famílias, a tempos determinados, de ano em ano, para se queimar sobre o altar do Senhor, nosso Deus, como está escrito na Lei.
35 E que também traríamos as primícias da nossa terra e todas as primícias de todas as árvores frutíferas, de ano em ano, à Casa do Senhor;
36 os primogênitos dos nossos filhos e os do nosso gado, como está escrito na Lei; e que os primogênitos das nossas manadas e das nossas ovelhas traríamos à casa do nosso Deus, aos sacerdotes que ministram nela.
37 As primícias da nossa massa, as nossas ofertas, o fruto de toda árvore, o vinho e o azeite traríamos aos sacerdotes, às câmaras da casa do nosso Deus; os dízimos da nossa terra, aos levitas, pois a eles cumpre receber os dízimos em todas as cidades onde há lavoura.
38 O sacerdote, filho de Arão, estaria com os levitas quando estes recebessem os dízimos, e os levitas trariam os dízimos dos dízimos à casa do nosso Deus, às câmaras da casa do tesouro.
39 Porque àquelas câmaras os filhos de Israel e os filhos de Levi devem trazer ofertas do cereal, do vinho e do azeite; porquanto se acham ali os vasos do santuário, como também os sacerdotes que ministram, e os porteiros, e os cantores; e, assim, não desampararíamos a casa do nosso Deus.*
1 Os príncipes do povo habitaram em Jerusalém, mas o seu restante deitou sortes para trazer um de dez para que habitasse na santa cidade de Jerusalém; e as nove partes permaneceriam em outras cidades.
2 O povo bendisse todos os homens que voluntariamente se ofereciam ainda para habitar em Jerusalém.
3 São estes os chefes da província que habitaram em Jerusalém; porém nas cidades de Judá habitou cada um na sua possessão, nas suas cidades, a saber, Israel, os sacerdotes, os levitas, os servidores do templo e os filhos dos servos de Salomão.
4 Habitaram, pois, em Jerusalém alguns dos filhos de Judá e dos filhos de Benjamim. Dos filhos de Judá: Ataías, filho de Uzias, filho de Zacarias, filho de Amarias, filho de Sefatias, filho de Maalalel, dos filhos de Perez;
5 e Maaseias, filho de Baruque, filho de Col-Hozé, filho de Hazaías, filho de Adaías, filho de Joiaribe, filho de Zacarias, filho do silonita.
6 Todos os filhos de Perez que habitaram em Jerusalém foram quatrocentos e sessenta e oito homens valentes.
7 São estes os filhos de Benjamim: Salu, filho de Mesulão, filho de Joede, filho de Pedaías, filho de Colaías, filho de Maaseias, filho de Itiel, filho de Jesaías.
8 Depois dele, Gabai e Salai; ao todo, novecentos e vinte e oito.
9 Joel, filho de Zicri, superintendente deles; e Judá, filho de Senua, o segundo sobre a cidade.
10 Dos sacerdotes: Jedaías, filho de Joiaribe, Jaquim,
11 Seraías, filho de Hilquias, filho de Mesulão, filho de Zadoque, filho de Meraiote,
12 filho de Aitube, príncipe da Casa de Deus, e os irmãos deles, que faziam o serviço do templo, oitocentos e vinte e dois; e Adaías, filho de Jeroão, filho de Pelalias, filho de Anzi, filho de Zacarias, filho de Pasur, filho de Malquias,
13 e seus irmãos, cabeças de famílias, duzentos e quarenta e dois; e Amasai, filho de Azarel, filho de Azai, filho de Mesilemote, filho de Imer,
14 e os irmãos deles, homens valentes, cento e vinte e oito; e, superintendente deles, Zabdiel, filho de Gedolim.
15 Dos levitas: Semaías, filho de Hassube, filho de Azricão, filho de Hasabias, filho de Buni;
16 Sabetai e Jozabade, dos cabeças dos levitas, que presidiam o serviço de fora da Casa de Deus;
17 Matanias, filho de Mica, filho de Zabdi, filho de Asafe, o chefe, que dirigia os louvores nas orações, e Baquebuquias, o segundo de seus irmãos; depois, Abda, filho de Samua, filho de Galal, filho de Jedutum.
18 Todos os levitas na santa cidade foram duzentos e oitenta e quatro.
19 Dos porteiros: Acube, Talmom e os irmãos deles, os guardas das portas, cento e setenta e dois.
20 O restante de Israel, dos sacerdotes e levitas se estabeleceu em todas as cidades de Judá, cada um na sua herança.
21 Os servidores do templo habitaram em Ofel e estavam a cargo de Zia e Gispa.
22 O superintendente dos levitas em Jerusalém era Uzi, filho de Bani, filho de Hasabias, filho de Matanias, filho de Mica, dos filhos de Asafe, que eram cantores ao serviço da Casa de Deus.
23 Porque havia um mandado do rei a respeito deles e certo acordo com os cantores, concernente às obrigações de cada dia.
24 Petaías, filho de Mesezabel, dos filhos de Zera, filho de Judá, estava à disposição do rei, em todos os negócios do povo.
25 Quanto às aldeias, com os seus campos, alguns dos filhos de Judá habitaram em Quiriate-Arba e suas aldeias, em Dibom e suas aldeias, em Jecabzeel e suas aldeias,
26 e em Jesua, em Moladá, em Bete-Palete,
27 em Hazar-Sual, em Berseba e suas aldeias;
28 em Ziclague, em Mecona e suas aldeias;
29 em En-Rimom, em Zorá, em Jarmute;
30 em Zanoa, em Adulão e nas aldeias delas; em Laquis e em seus campos, em Azeca e suas aldeias. Acamparam-se desde Berseba até ao vale de Hinom.
31 Os filhos de Benjamim também se estabeleceram em Geba e daí em diante, em Micmás, Aia, Betel e suas aldeias;
32 em Anatote, em Nobe, em Ananias,
33 em Hazor, em Ramá, em Gitaim,
34 em Hadide, em Zeboim, em Nebalate,
35 em Lode e em Ono, no vale dos Artífices.
36 Dos levitas, havia grupos tanto em Judá como em Benjamim.*
1 São estes os sacerdotes e levitas que subiram com Zorobabel, filho de Sealtiel, e com Jesua: Seraías, Jeremias, Esdras,
2 Amarias, Maluque, Hatus,
3 Secanias, Reum, Meremote,
4 Ido, Ginetoi, Abias,
5 Miamim, Maadias, Bilga,
6 Semaías, Joiaribe, Jedaías,
7 Salu, Amoque, Hilquias e Jedaías; estes foram os chefes dos sacerdotes e de seus irmãos, nos dias de Jesua.
8 Também os levitas Jesua, Binui, Cadmiel, Serebias, Judá e Matanias; este e seus irmãos dirigiam os louvores.
9 Baquebuquias e Uni, seus irmãos, estavam defronte deles, cada qual no seu mister.
10 Jesua gerou a Joiaquim, Joiaquim gerou a Eliasibe, Eliasibe gerou a Joiada,
11 Joiada gerou a Jônatas, e Jônatas gerou a Jadua.
12 Nos dias de Joiaquim, foram sacerdotes, cabeças de famílias: de Seraías, Meraías; de Jeremias, Hananias;
13 de Esdras, Mesulão; de Amarias, Joanã;
14 de Maluqui, Jônatas; de Sebanias, José;
15 de Harim, Adna; de Meraiote, Helcai;
16 de Ido, Zacarias; de Ginetom, Mesulão;
17 de Abias, Zicri; de Miniamim e de Moadias, Piltai;
18 de Bilga, Samua; de Semaías, Jônatas;
19 de Joiaribe, Matenai; de Jedaías, Uzi;
20 de Salai, Calai; de Amoque, Héber;
21 de Hilquias, Hasabias; de Jedaías, Netanel.
22 Dos levitas, nos dias de Eliasibe, foram inscritos como cabeças de famílias Joiada, Joanã e Jadua, como também os sacerdotes, até ao reinado de Dario, o persa.
23 Os filhos de Levi foram inscritos como cabeças de famílias no Livro das Crônicas, até aos dias de Joanã, filho de Eliasibe.
24 Foram, pois, chefes dos levitas: Hasabias, Serebias e Jesua, filho de Cadmiel; os irmãos deles lhes estavam fronteiros para louvarem e darem graças, segundo o mandado de Davi, homem de Deus, coro contra coro.
25 Matanias, Baquebuquias, Obadias, Mesulão, Talmom e Acube eram porteiros e faziam a guarda aos depósitos das portas.
26 Estes viveram nos dias de Joiaquim, filho de Jesua, filho de Jozadaque, e nos dias de Neemias, o governador, e de Esdras, o sacerdote e escriba.
27 Na dedicação dos muros de Jerusalém, procuraram aos levitas de todos os seus lugares, para fazê-los vir a fim de que fizessem a dedicação com alegria, louvores, canto, címbalos, alaúdes e harpas.
28 Ajuntaram-se os filhos dos cantores, tanto da campina dos arredores de Jerusalém como das aldeias dos netofatitas,
29 como também de Bete-Gilgal e dos campos de Geba e de Azmavete; porque os cantores tinham edificado para si aldeias nos arredores de Jerusalém.
30 Purificaram-se os sacerdotes e os levitas, que também purificaram o povo e as portas e o muro.
31 Então, fiz subir os príncipes de Judá sobre o muro e formei dois grandes coros em procissão, sendo um à mão direita sobre a muralha para o lado da Porta do Monturo.
32 Após eles, ia Hosaías e a metade dos príncipes de Judá,
33 Azarias, Esdras, Mesulão,
34 Judá, Benjamim, Semaías e Jeremias;
35 e dos filhos dos sacerdotes, com trombetas: Zacarias, filho de Jônatas, filho de Semaías, filho de Matanias, filho de Micaías, filho de Zacur, filho de Asafe,
36 e seus irmãos, Semaías, Azarel, Milalai, Gilalai, Maai, Netanel, Judá e Hanani, com os instrumentos músicos de Davi, homem de Deus; Esdras, o escriba, ia adiante deles.
37 À entrada da Porta da Fonte, subiram diretamente as escadas da Cidade de Davi, onde se eleva o muro por sobre a casa de Davi, até à Porta das Águas, do lado oriental.
38 O segundo coro ia em frente, e eu, após ele; metade do povo ia por cima do muro, desde a Torre dos Fornos até ao Muro Largo;
39 e desde a Porta de Efraim, passaram por cima da Porta Velha e da Porta do Peixe, pela Torre de Hananel, pela Torre dos Cem, até à Porta do Gado; e pararam à Porta da Guarda.
40 Então, ambos os coros pararam na Casa de Deus, como também eu e a metade dos magistrados comigo.
41 Os sacerdotes Eliaquim, Maaseias, Miniamim, Micaías, Elioenai, Zacarias e Hananias iam com trombetas,
42 como também Maaseias, Semaías, Eleazar, Uzi, Joanã, Malquias, Elão e Ezer; e faziam-se ouvir os cantores sob a direção de Jezraías.
43 No mesmo dia, ofereceram grandes sacrifícios e se alegraram; pois Deus os alegrara com grande alegria; também as mulheres e os meninos se alegraram, de modo que o júbilo de Jerusalém se ouviu até de longe.
44 Ainda no mesmo dia, se nomearam homens para as câmaras dos tesouros, das ofertas, das primícias e dos dízimos, para ajuntarem nelas, das cidades, as porções designadas pela Lei para os sacerdotes e para os levitas; pois Judá estava alegre, porque os sacerdotes e os levitas ministravam ali;
45 e executavam o serviço do seu Deus e o da purificação; como também os cantores e porteiros, segundo o mandado de Davi e de seu filho Salomão.
46 Pois já outrora, nos dias de Davi e de Asafe, havia chefes dos cantores, cânticos de louvor e ações de graças a Deus.
47 Todo o Israel, nos dias de Zorobabel e nos dias de Neemias, dava aos cantores e aos porteiros as porções de cada dia; e consagrava as coisas destinadas aos levitas, e os levitas, as destinadas aos filhos de Arão.*
1 Naquele dia, se leu para o povo no Livro de Moisés; achou-se escrito que os amonitas e os moabitas não entrassem jamais na congregação de Deus,
2 porquanto não tinham saído ao encontro dos filhos de Israel com pão e água; antes, assalariaram contra eles Balaão para os amaldiçoar; mas o nosso Deus converteu a maldição em bênção.
3 Ouvindo eles, o povo, esta lei, apartaram de Israel todo elemento misto.
4 Ora, antes disto, Eliasibe, sacerdote, encarregado da câmara da casa do nosso Deus, se tinha aparentado com Tobias;
5 e fizera para este uma câmara grande, onde dantes se depositavam as ofertas de manjares, o incenso, os utensílios e os dízimos dos cereais, do vinho e do azeite, que se ordenaram para os levitas, cantores e porteiros, como também contribuições para os sacerdotes.
6 Mas, quando isso aconteceu, não estive em Jerusalém, porque no trigésimo segundo ano de Artaxerxes, rei da Babilônia, eu fora ter com ele; mas ao cabo de certo tempo pedi licença ao rei e voltei para Jerusalém.
7 Então, soube do mal que Eliasibe fizera para beneficiar a Tobias, fazendo-lhe uma câmara nos pátios da Casa de Deus.
8 Isso muito me indignou a tal ponto, que atirei todos os móveis da casa de Tobias fora da câmara.
9 Então, ordenei que se purificassem as câmaras e tornei a trazer para ali os utensílios da Casa de Deus, com as ofertas de manjares e o incenso.
10 Também soube que os quinhões dos levitas não se lhes davam, de maneira que os levitas e os cantores, que faziam o serviço, tinham fugido cada um para o seu campo.
11 Então, contendi com os magistrados e disse: Por que se desamparou a Casa de Deus? Ajuntei os levitas e os cantores e os restituí a seus postos.
12 Então, todo o Judá trouxe os dízimos dos cereais, do vinho e do azeite aos depósitos.
13 Por tesoureiros dos depósitos pus Selemias, o sacerdote, Zadoque, o escrivão, e, dentre os levitas, Pedaías; como assistente deles, Hanã, filho de Zacur, filho de Matanias; porque foram achados fiéis, e se lhes encarregou que repartissem as porções para seus irmãos.
14 Por isto, Deus meu, lembra-te de mim e não apagues as beneficências que eu fiz à casa de meu Deus e para o seu serviço.
15 Naqueles dias, vi em Judá os que pisavam lagares ao sábado e traziam trigo que carregavam sobre jumentos; como também vinho, uvas e figos e toda sorte de cargas, que traziam a Jerusalém no dia de sábado; e protestei contra eles por venderem mantimentos neste dia.
16 Também habitavam em Jerusalém tírios que traziam peixes e toda sorte de mercadorias, que no sábado vendiam aos filhos de Judá e em Jerusalém.
17 Contendi com os nobres de Judá e lhes disse: Que mal é este que fazeis, profanando o dia de sábado?
18 Acaso, não fizeram vossos pais assim, e não trouxe o nosso Deus todo este mal sobre nós e sobre esta cidade? E vós ainda trazeis ira maior sobre Israel, profanando o sábado.
19 Dando já sombra as portas de Jerusalém antes do sábado, ordenei que se fechassem; e determinei que não se abrissem, senão após o sábado; às portas coloquei alguns dos meus moços, para que nenhuma carga entrasse no dia de sábado.
20 Então, os negociantes e os vendedores de toda sorte de mercadorias pernoitaram fora de Jerusalém, uma ou duas vezes.
21 Protestei, pois, contra eles e lhes disse: Por que passais a noite defronte do muro? Se outra vez o fizerdes, lançarei mão sobre vós. Daí em diante não tornaram a vir no sábado.
22 Também mandei aos levitas que se purificassem e viessem guardar as portas, para santificar o dia de sábado. Também nisto, Deus meu, lembra-te de mim; e perdoa-me segundo a abundância da tua misericórdia.
23 Vi também, naqueles dias, que judeus haviam casado com mulheres asdoditas, amonitas e moabitas.
24 Seus filhos falavam meio asdodita e não sabiam falar judaico, mas a língua de seu respectivo povo.
25 Contendi com eles, e os amaldiçoei, e espanquei alguns deles, e lhes arranquei os cabelos, e os conjurei por Deus, dizendo: Não dareis mais vossas filhas a seus filhos e não tomareis mais suas filhas, nem para vossos filhos nem para vós mesmos.
26 Não pecou nisto Salomão, rei de Israel? Todavia, entre muitas nações não havia rei semelhante a ele, e ele era amado do seu Deus, e Deus o constituiu rei sobre todo o Israel. Não obstante isso, as mulheres estrangeiras o fizeram cair no pecado.
27 Dar-vos-íamos nós ouvidos, para fazermos todo este grande mal, prevaricando contra o nosso Deus, casando com mulheres estrangeiras?
28 Um dos filhos de Joiada, filho do sumo sacerdote Eliasibe, era genro de Sambalate, o horonita, pelo que o afugentei de mim.
29 Lembra-te deles, Deus meu, pois contaminaram o sacerdócio, como também a aliança sacerdotal e levítica.
30 Limpei-os, pois, de toda estrangeirice e designei o serviço dos sacerdotes e dos levitas, cada um no seu mister,
31 como também o fornecimento de lenha em tempos determinados, bem como as primícias. Lembra-te de mim, Deus meu, para o meu bem.*
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Neemias','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)