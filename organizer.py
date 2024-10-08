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
1 Revelação de Jesus Cristo, que Deus lhe deu para mostrar aos seus servos as coisas que em breve devem acontecer e que ele, enviando por intermédio do seu anjo, notificou ao seu servo João,
2 o qual atestou a palavra de Deus e o testemunho de Jesus Cristo, quanto a tudo o que viu.
3 Bem-aventurados aqueles que leem e aqueles que ouvem as palavras da profecia e guardam as coisas nela escritas, pois o tempo está próximo.
4 João, às sete igrejas que se encontram na Ásia, graça e paz a vós outros, da parte daquele que é, que era e que há de vir, da parte dos sete Espíritos que se acham diante do seu trono
5 e da parte de Jesus Cristo, a Fiel Testemunha, o Primogênito dos mortos e o Soberano dos reis da terra. Àquele que nos ama, e, pelo seu sangue, nos libertou dos nossos pecados,
6 e nos constituiu reino, sacerdotes para o seu Deus e Pai, a ele a glória e o domínio pelos séculos dos séculos. Amém!
7 Eis que vem com as nuvens, e todo olho o verá, até quantos o traspassaram. E todas as tribos da terra se lamentarão sobre ele. Certamente. Amém!
8 Eu sou o Alfa e Ômega, diz o Senhor Deus, aquele que é, que era e que há de vir, o Todo-Poderoso.
9 Eu, João, irmão vosso e companheiro na tribulação, no reino e na perseverança, em Jesus, achei-me na ilha chamada Patmos, por causa da palavra de Deus e do testemunho de Jesus.
10 Achei-me em espírito, no dia do Senhor, e ouvi, por detrás de mim, grande voz, como de trombeta,
11 dizendo: O que vês escreve em livro e manda às sete igrejas: Éfeso, Esmirna, Pérgamo, Tiatira, Sardes, Filadélfia e Laodiceia.
12 Voltei-me para ver quem falava comigo e, voltado, vi sete candeeiros de ouro
13 e, no meio dos candeeiros, um semelhante a filho de homem, com vestes talares e cingido, à altura do peito, com uma cinta de ouro.
14 A sua cabeça e cabelos eram brancos como alva lã, como neve; os olhos, como chama de fogo;
15 os pés, semelhantes ao bronze polido, como que refinado numa fornalha; a voz, como voz de muitas águas.
16 Tinha na mão direita sete estrelas, e da boca saía-lhe uma afiada espada de dois gumes. O seu rosto brilhava como o sol na sua força.
17 Quando o vi, caí a seus pés como morto. Porém ele pôs sobre mim a mão direita, dizendo: Não temas; eu sou o primeiro e o último
18 e aquele que vive; estive morto, mas eis que estou vivo pelos séculos dos séculos e tenho as chaves da morte e do inferno.
19 Escreve, pois, as coisas que viste, e as que são, e as que hão de acontecer depois destas.
20 Quanto ao mistério das sete estrelas que viste na minha mão direita e aos sete candeeiros de ouro, as sete estrelas são os anjos das sete igrejas, e os sete candeeiros são as sete igrejas.*
1 Ao anjo da igreja em Éfeso escreve: Estas coisas diz aquele que conserva na mão direita as sete estrelas e que anda no meio dos sete candeeiros de ouro:
2 Conheço as tuas obras, tanto o teu labor como a tua perseverança, e que não podes suportar homens maus, e que puseste à prova os que a si mesmos se declaram apóstolos e não são, e os achaste mentirosos;
3 e tens perseverança, e suportaste provas por causa do meu nome, e não te deixaste esmorecer.
4 Tenho, porém, contra ti que abandonaste o teu primeiro amor.
5 Lembra-te, pois, de onde caíste, arrepende-te e volta à prática das primeiras obras; e, se não, venho a ti e moverei do seu lugar o teu candeeiro, caso não te arrependas.
6 Tens, contudo, a teu favor que odeias as obras dos nicolaítas, as quais eu também odeio.
7 Quem tem ouvidos, ouça o que o Espírito diz às igrejas: Ao vencedor, dar-lhe-ei que se alimente da árvore da vida que se encontra no paraíso de Deus.
8 Ao anjo da igreja em Esmirna escreve: Estas coisas diz o primeiro e o último, que esteve morto e tornou a viver:
9 Conheço a tua tribulação, a tua pobreza (mas tu és rico) e a blasfêmia dos que a si mesmos se declaram judeus e não são, sendo, antes, sinagoga de Satanás.
10 Não temas as coisas que tens de sofrer. Eis que o diabo está para lançar em prisão alguns dentre vós, para serdes postos à prova, e tereis tribulação de dez dias. Sê fiel até à morte, e dar-te-ei a coroa da vida.
11 Quem tem ouvidos, ouça o que o Espírito diz às igrejas: O vencedor de nenhum modo sofrerá dano da segunda morte.
12 Ao anjo da igreja em Pérgamo escreve: Estas coisas diz aquele que tem a espada afiada de dois gumes:
13 Conheço o lugar em que habitas, onde está o trono de Satanás, e que conservas o meu nome e não negaste a minha fé, ainda nos dias de Antipas, minha testemunha, meu fiel, o qual foi morto entre vós, onde Satanás habita.
14 Tenho, todavia, contra ti algumas coisas, pois que tens aí os que sustentam a doutrina de Balaão, o qual ensinava a Balaque a armar ciladas diante dos filhos de Israel para comerem coisas sacrificadas aos ídolos e praticarem a prostituição.
15 Outrossim, também tu tens os que da mesma forma sustentam a doutrina dos nicolaítas.
16 Portanto, arrepende-te; e, se não, venho a ti sem demora e contra eles pelejarei com a espada da minha boca.
17 Quem tem ouvidos, ouça o que o Espírito diz às igrejas: Ao vencedor, dar-lhe-ei do maná escondido, bem como lhe darei uma pedrinha branca, e sobre essa pedrinha escrito um nome novo, o qual ninguém conhece, exceto aquele que o recebe.
18 Ao anjo da igreja em Tiatira escreve: Estas coisas diz o Filho de Deus, que tem os olhos como chama de fogo e os pés semelhantes ao bronze polido:
19 Conheço as tuas obras, o teu amor, a tua fé, o teu serviço, a tua perseverança e as tuas últimas obras, mais numerosas do que as primeiras.
20 Tenho, porém, contra ti o tolerares que essa mulher, Jezabel, que a si mesma se declara profetisa, não somente ensine, mas ainda seduza os meus servos a praticarem a prostituição e a comerem coisas sacrificadas aos ídolos.
21 Dei-lhe tempo para que se arrependesse; ela, todavia, não quer arrepender-se da sua prostituição.
22 Eis que a prostro de cama, bem como em grande tribulação os que com ela adulteram, caso não se arrependam das obras que ela incita.
23 Matarei os seus filhos, e todas as igrejas conhecerão que eu sou aquele que sonda mentes e corações, e vos darei a cada um segundo as vossas obras.
24 Digo, todavia, a vós outros, os demais de Tiatira, a tantos quantos não têm essa doutrina e que não conheceram, como eles dizem, as coisas profundas de Satanás: Outra carga não jogarei sobre vós;
25 tão somente conservai o que tendes, até que eu venha.
26 Ao vencedor, que guardar até ao fim as minhas obras, eu lhe darei autoridade sobre as nações,
27 e com cetro de ferro as regerá e as reduzirá a pedaços como se fossem objetos de barro;
28 assim como também eu recebi de meu Pai, dar-lhe-ei ainda a estrela da manhã.
29 Quem tem ouvidos, ouça o que o Espírito diz às igrejas.*
1 Ao anjo da igreja em Sardes escreve: Estas coisas diz aquele que tem os sete Espíritos de Deus e as sete estrelas: Conheço as tuas obras, que tens nome de que vives e estás morto.
2 Sê vigilante e consolida o resto que estava para morrer, porque não tenho achado íntegras as tuas obras na presença do meu Deus.
3 Lembra-te, pois, do que tens recebido e ouvido, guarda-o e arrepende-te. Porquanto, se não vigiares, virei como ladrão, e não conhecerás de modo algum em que hora virei contra ti.
4 Tens, contudo, em Sardes, umas poucas pessoas que não contaminaram as suas vestiduras e andarão de branco junto comigo, pois são dignas.
5 O vencedor será assim vestido de vestiduras brancas, e de modo nenhum apagarei o seu nome do Livro da Vida; pelo contrário, confessarei o seu nome diante de meu Pai e diante dos seus anjos.
6 Quem tem ouvidos, ouça o que o Espírito diz às igrejas.
m Filadélfia
7 Ao anjo da igreja em Filadélfia escreve: Estas coisas diz o santo, o verdadeiro, aquele que tem a chave de Davi, que abre, e ninguém fechará, e que fecha, e ninguém abrirá:
8 Conheço as tuas obras — eis que tenho posto diante de ti uma porta aberta, a qual ninguém pode fechar — que tens pouca força, entretanto, guardaste a minha palavra e não negaste o meu nome.
9 Eis farei que alguns dos que são da sinagoga de Satanás, desses que a si mesmos se declaram judeus e não são, mas mentem, eis que os farei vir e prostrar-se aos teus pés e conhecer que eu te amei.
10 Porque guardaste a palavra da minha perseverança, também eu te guardarei da hora da provação que há de vir sobre o mundo inteiro, para experimentar os que habitam sobre a terra.
11 Venho sem demora. Conserva o que tens, para que ninguém tome a tua coroa.
12 Ao vencedor, fá-lo-ei coluna no santuário do meu Deus, e daí jamais sairá; gravarei também sobre ele o nome do meu Deus, o nome da cidade do meu Deus, a nova Jerusalém que desce do céu, vinda da parte do meu Deus, e o meu novo nome.
13 Quem tem ouvidos, ouça o que o Espírito diz às igrejas.
14 Ao anjo da igreja em Laodiceia escreve: Estas coisas diz o Amém, a testemunha fiel e verdadeira, o princípio da criação de Deus:
15 Conheço as tuas obras, que nem és frio nem quente. Quem dera fosses frio ou quente!
16 Assim, porque és morno e nem és quente nem frio, estou a ponto de vomitar-te da minha boca;
17 pois dizes: Estou rico e abastado e não preciso de coisa alguma, e nem sabes que tu és infeliz, sim, miserável, pobre, cego e nu.
18 Aconselho-te que de mim compres ouro refinado pelo fogo para te enriqueceres, vestiduras brancas para te vestires, a fim de que não seja manifesta a vergonha da tua nudez, e colírio para ungires os olhos, a fim de que vejas.
19 Eu repreendo e disciplino a quantos amo. Sê, pois, zeloso e arrepende-te.
20 Eis que estou à porta e bato; se alguém ouvir a minha voz e abrir a porta, entrarei em sua casa e cearei com ele, e ele, comigo.
21 Ao vencedor, dar-lhe-ei sentar-se comigo no meu trono, assim como também eu venci e me sentei com meu Pai no seu trono.
22 Quem tem ouvidos, ouça o que o Espírito diz às igrejas.*
1 Depois destas coisas, olhei, e eis não somente uma porta aberta no céu, como também a primeira voz que ouvi, como de trombeta ao falar comigo, dizendo: Sobe para aqui, e te mostrarei o que deve acontecer depois destas coisas.
2 Imediatamente, eu me achei em espírito, e eis armado no céu um trono, e, no trono, alguém sentado;
3 e esse que se acha assentado é semelhante, no aspecto, a pedra de jaspe e de sardônio, e, ao redor do trono, há um arco-íris semelhante, no aspecto, a esmeralda.
4 Ao redor do trono, há também vinte e quatro tronos, e assentados neles, vinte e quatro anciãos vestidos de branco, em cujas cabeças estão coroas de ouro.
5 Do trono saem relâmpagos, vozes e trovões, e, diante do trono, ardem sete tochas de fogo, que são os sete Espíritos de Deus.
6 Há diante do trono um como que mar de vidro, semelhante ao cristal, e também, no meio do trono e à volta do trono, quatro seres viventes cheios de olhos por diante e por detrás.
7 O primeiro ser vivente é semelhante a leão, o segundo, semelhante a novilho, o terceiro tem o rosto como de homem, e o quarto ser vivente é semelhante à águia quando está voando.
8 E os quatro seres viventes, tendo cada um deles, respectivamente, seis asas, estão cheios de olhos, ao redor e por dentro; não têm descanso, nem de dia nem de noite, proclamando: Santo, Santo, Santo é o Senhor Deus, o Todo-Poderoso, aquele que era, que é e que há de vir.
9 Quando esses seres viventes derem glória, honra e ações de graças ao que se encontra sentado no trono, ao que vive pelos séculos dos séculos,
10 os vinte e quatro anciãos prostrar-se-ão diante daquele que se encontra sentado no trono, adorarão o que vive pelos séculos dos séculos e depositarão as suas coroas diante do trono, proclamando:
11 Tu és digno, Senhor e Deus nosso, de receber a glória, a honra e o poder, porque todas as coisas tu criaste, sim, por causa da tua vontade vieram a existir e foram criadas.*
1 Vi, na mão direita daquele que estava sentado no trono, um livro escrito por dentro e por fora, de todo selado com sete selos.
2 Vi, também, um anjo forte, que proclamava em grande voz: Quem é digno de abrir o livro e de lhe desatar os selos?
3 Ora, nem no céu, nem sobre a terra, nem debaixo da terra, ninguém podia abrir o livro, nem mesmo olhar para ele;
4 e eu chorava muito, porque ninguém foi achado digno de abrir o livro, nem mesmo de olhar para ele.
5 Todavia, um dos anciãos me disse: Não chores; eis que o Leão da tribo de Judá, a Raiz de Davi, venceu para abrir o livro e os seus sete selos.
6 Então, vi, no meio do trono e dos quatro seres viventes e entre os anciãos, de pé, um Cordeiro como tendo sido morto. Ele tinha sete chifres, bem como sete olhos, que são os sete Espíritos de Deus enviados por toda a terra.
7 Veio, pois, e tomou o livro da mão direita daquele que estava sentado no trono;
8 e, quando tomou o livro, os quatro seres viventes e os vinte e quatro anciãos prostraram-se diante do Cordeiro, tendo cada um deles uma harpa e taças de ouro cheias de incenso, que são as orações dos santos,
9 e entoavam novo cântico, dizendo: Digno és de tomar o livro e de abrir-lhe os selos, porque foste morto e com o teu sangue compraste para Deus os que procedem de toda tribo, língua, povo e nação
10 e para o nosso Deus os constituíste reino e sacerdotes; e reinarão sobre a terra.
11 Vi e ouvi uma voz de muitos anjos ao redor do trono, dos seres viventes e dos anciãos, cujo número era de milhões de milhões e milhares de milhares,
12 proclamando em grande voz: Digno é o Cordeiro que foi morto de receber o poder, e riqueza, e sabedoria, e força, e honra, e glória, e louvor.
13 Então, ouvi que toda criatura que há no céu e sobre a terra, debaixo da terra e sobre o mar, e tudo o que neles há, estava dizendo: Àquele que está sentado no trono e ao Cordeiro, seja o louvor, e a honra, e a glória, e o domínio pelos séculos dos séculos.
14 E os quatro seres viventes respondiam: Amém! Também os anciãos prostraram-se e adoraram.*
1 Vi quando o Cordeiro abriu um dos sete selos e ouvi um dos quatro seres viventes dizendo, como se fosse voz de trovão: Vem!
2 Vi, então, e eis um cavalo branco e o seu cavaleiro com um arco; e foi-lhe dada uma coroa; e ele saiu vencendo e para vencer.
3 Quando abriu o segundo selo, ouvi o segundo ser vivente dizendo: Vem!
4 E saiu outro cavalo, vermelho; e ao seu cavaleiro, foi-lhe dado tirar a paz da terra para que os homens se matassem uns aos outros; também lhe foi dada uma grande espada.
5 Quando abriu o terceiro selo, ouvi o terceiro ser vivente dizendo: Vem! Então, vi, e eis um cavalo preto e o seu cavaleiro com uma balança na mão.
6 E ouvi uma como que voz no meio dos quatro seres viventes dizendo: Uma medida de trigo por um denário; três medidas de cevada por um denário; e não danifiques o azeite e o vinho.
7 Quando o Cordeiro abriu o quarto selo, ouvi a voz do quarto ser vivente dizendo: Vem!
8 E olhei, e eis um cavalo amarelo e o seu cavaleiro, sendo este chamado Morte; e o Inferno o estava seguindo, e foi-lhes dada autoridade sobre a quarta parte da terra para matar à espada, pela fome, com a mortandade e por meio das feras da terra.
12 Vi quando o Cordeiro abriu o sexto selo, e sobreveio grande terremoto. O sol se tornou negro como saco de crina, a lua toda, como sangue,
13 as estrelas do céu caíram pela terra, como a figueira, quando abalada por vento forte, deixa cair os seus figos verdes,
14 e o céu recolheu-se como um pergaminho quando se enrola. Então, todos os montes e ilhas foram movidos do seu lugar.
15 Os reis da terra, os grandes, os comandantes, os ricos, os poderosos e todo escravo e todo livre se esconderam nas cavernas e nos penhascos dos montes
16 e disseram aos montes e aos rochedos: Caí sobre nós e escondei-nos da face daquele que se assenta no trono e da ira do Cordeiro,
17 porque chegou o grande Dia da ira deles; e quem é que pode suster-se?*
1 Depois disto, vi quatro anjos em pé nos quatro cantos da terra, conservando seguros os quatro ventos da terra, para que nenhum vento soprasse sobre a terra, nem sobre o mar, nem sobre árvore alguma.
2 Vi outro anjo que subia do nascente do sol, tendo o selo do Deus vivo, e clamou em grande voz aos quatro anjos, aqueles aos quais fora dado fazer dano à terra e ao mar,
3 dizendo: Não danifiqueis nem a terra, nem o mar, nem as árvores, até selarmos na fronte os servos do nosso Deus.
4 Então, ouvi o número dos que foram selados, que era cento e quarenta e quatro mil, de todas as tribos dos filhos de Israel:
5 da tribo de Judá foram selados doze mil; da tribo de Rúben, doze mil; da tribo de Gade, doze mil;
6 da tribo de Aser, doze mil; da tribo de Naftali, doze mil; da tribo de Manassés, doze mil;
7 da tribo de Simeão, doze mil; da tribo de Levi, doze mil; da tribo de Issacar, doze mil;
8 da tribo de Zebulom, doze mil; da tribo de José, doze mil; da tribo de Benjamim foram selados doze mil.
9 Depois destas coisas, vi, e eis grande multidão que ninguém podia enumerar, de todas as nações, tribos, povos e línguas, em pé diante do trono e diante do Cordeiro, vestidos de vestiduras brancas, com palmas nas mãos;
10 e clamavam em grande voz, dizendo: Ao nosso Deus, que se assenta no trono, e ao Cordeiro, pertence a salvação.
11 Todos os anjos estavam de pé rodeando o trono, os anciãos e os quatro seres viventes, e ante o trono se prostraram sobre o seu rosto, e adoraram a Deus,
12 dizendo: Amém! O louvor, e a glória, e a sabedoria, e as ações de graças, e a honra, e o poder, e a força sejam ao nosso Deus, pelos séculos dos séculos. Amém!
13 Um dos anciãos tomou a palavra, dizendo: Estes, que se vestem de vestiduras brancas, quem são e donde vieram?
14 Respondi-lhe: meu Senhor, tu o sabes. Ele, então, me disse: São estes os que vêm da grande tribulação, lavaram suas vestiduras e as alvejaram no sangue do Cordeiro,
15 razão por que se acham diante do trono de Deus e o servem de dia e de noite no seu santuário; e aquele que se assenta no trono estenderá sobre eles o seu tabernáculo.
16 Jamais terão fome, nunca mais terão sede, não cairá sobre eles o sol, nem ardor algum,
17 pois o Cordeiro que se encontra no meio do trono os apascentará e os guiará para as fontes da água da vida. E Deus lhes enxugará dos olhos toda lágrima.*
1 Quando o Cordeiro abriu o sétimo selo, houve silêncio no céu cerca de meia hora.
2 Então, vi os sete anjos que se acham em pé diante de Deus, e lhes foram dadas sete trombetas.
3 Veio outro anjo e ficou de pé junto ao altar, com um incensário de ouro, e foi-lhe dado muito incenso para oferecê-lo com as orações de todos os santos sobre o altar de ouro que se acha diante do trono;
4 e da mão do anjo subiu à presença de Deus a fumaça do incenso, com as orações dos santos.
5 E o anjo tomou o incensário, encheu-o do fogo do altar e o atirou à terra. E houve trovões, vozes, relâmpagos e terremoto.
6 Então, os sete anjos que tinham as sete trombetas prepararam-se para tocar.
7 O primeiro anjo tocou a trombeta, e houve saraiva e fogo de mistura com sangue, e foram atirados à terra. Foi, então, queimada a terça parte da terra, e das árvores, e também toda erva verde.
8 O segundo anjo tocou a trombeta, e uma como que grande montanha ardendo em chamas foi atirada ao mar, cuja terça parte se tornou em sangue,
9 e morreu a terça parte da criação que tinha vida, existente no mar, e foi destruída a terça parte das embarcações.
10 O terceiro anjo tocou a trombeta, e caiu do céu sobre a terça parte dos rios, e sobre as fontes das águas uma grande estrela, ardendo como tocha.
11 O nome da estrela é Absinto; e a terça parte das águas se tornou em absinto, e muitos dos homens morreram por causa dessas águas, porque se tornaram amargosas.
12 O quarto anjo tocou a trombeta, e foi ferida a terça parte do sol, da lua e das estrelas, para que a terça parte deles escurecesse e, na sua terça parte, não brilhasse, tanto o dia como também a noite.
13 Então, vi e ouvi uma águia que, voando pelo meio do céu, dizia em grande voz: Ai! Ai! Ai dos que moram na terra, por causa das restantes vozes da trombeta dos três anjos que ainda têm de tocar!*
1 O quinto anjo tocou a trombeta, e vi uma estrela caída do céu na terra. E foi-lhe dada a chave do poço do abismo.
2 Ela abriu o poço do abismo, e subiu fumaça do poço como fumaça de grande fornalha, e, com a fumaceira saída do poço, escureceu-se o sol e o ar.
3 Também da fumaça saíram gafanhotos para a terra; e foi-lhes dado poder como o que têm os escorpiões da terra,
4 e foi-lhes dito que não causassem dano à erva da terra, nem a qualquer coisa verde, nem a árvore alguma e tão somente aos homens que não têm o selo de Deus sobre a fronte.
5 Foi-lhes também dado, não que os matassem, e sim que os atormentassem durante cinco meses. E o seu tormento era como tormento de escorpião quando fere alguém.
6 Naqueles dias, os homens buscarão a morte e não a acharão; também terão ardente desejo de morrer, mas a morte fugirá deles.
7 O aspecto dos gafanhotos era semelhante a cavalos preparados para a peleja; na sua cabeça havia como que coroas parecendo de ouro; e o seu rosto era como rosto de homem;
8 tinham também cabelos, como cabelos de mulher; os seus dentes, como dentes de leão;
9 tinham couraças, como couraças de ferro; o barulho que as suas asas faziam era como o barulho de carros de muitos cavalos, quando correm à peleja;
10 tinham ainda cauda, como escorpiões, e ferrão; na cauda tinham poder para causar dano aos homens, por cinco meses;
11 e tinham sobre eles, como seu rei, o anjo do abismo, cujo nome em hebraico é Abadom, e em grego, Apoliom.
12 O primeiro ai passou. Eis que, depois destas coisas, vêm ainda dois ais.
13 O sexto anjo tocou a trombeta, e ouvi uma voz procedente dos quatro ângulos do altar de ouro que se encontra na presença de Deus,
14 dizendo ao sexto anjo, o mesmo que tem a trombeta: Solta os quatro anjos que se encontram atados junto ao grande rio Eufrates.
15 Foram, então, soltos os quatro anjos que se achavam preparados para a hora, o dia, o mês e o ano, para que matassem a terça parte dos homens.
16 O número dos exércitos da cavalaria era de vinte mil vezes dez milhares; eu ouvi o seu número.
17 Assim, nesta visão, contemplei que os cavalos e os seus cavaleiros tinham couraças cor de fogo, de jacinto e de enxofre. A cabeça dos cavalos era como cabeça de leão, e de sua boca saía fogo, fumaça e enxofre.
18 Por meio destes três flagelos, a saber, pelo fogo, pela fumaça e pelo enxofre que saíam da sua boca, foi morta a terça parte dos homens;
19 pois a força dos cavalos estava na sua boca e na sua cauda, porquanto a sua cauda se parecia com serpentes, e tinha cabeça, e com ela causavam dano.
20 Os outros homens, aqueles que não foram mortos por esses flagelos, não se arrependeram das obras das suas mãos, deixando de adorar os demônios e os ídolos de ouro, de prata, de cobre, de pedra e de pau, que nem podem ver, nem ouvir, nem andar;
21 nem ainda se arrependeram dos seus assassínios, nem das suas feitiçarias, nem da sua prostituição, nem dos seus furtos.*
1 Vi outro anjo forte descendo do céu, envolto em nuvem, com o arco-íris por cima de sua cabeça; o rosto era como o sol, e as pernas, como colunas de fogo;
2 e tinha na mão um livrinho aberto. Pôs o pé direito sobre o mar e o esquerdo, sobre a terra,
3 e bradou em grande voz, como ruge um leão, e, quando bradou, desferiram os sete trovões as suas próprias vozes.
4 Logo que falaram os sete trovões, eu ia escrever, mas ouvi uma voz do céu, dizendo: Guarda em segredo as coisas que os sete trovões falaram e não as escrevas.
5 Então, o anjo que vi em pé sobre o mar e sobre a terra levantou a mão direita para o céu
6 e jurou por aquele que vive pelos séculos dos séculos, o mesmo que criou o céu, a terra, o mar e tudo quanto neles existe: Já não haverá demora,
7 mas, nos dias da voz do sétimo anjo, quando ele estiver para tocar a trombeta, cumprir-se-á, então, o mistério de Deus, segundo ele anunciou aos seus servos, os profetas.
8 A voz que ouvi, vinda do céu, estava de novo falando comigo e dizendo: Vai e toma o livro que se acha aberto na mão do anjo em pé sobre o mar e sobre a terra.
9 Fui, pois, ao anjo, dizendo-lhe que me desse o livrinho. Ele, então, me falou: Toma-o e devora-o; certamente, ele será amargo ao teu estômago, mas, na tua boca, doce como mel.
10 Tomei o livrinho da mão do anjo e o devorei, e, na minha boca, era doce como mel; quando, porém, o comi, o meu estômago ficou amargo.
11 Então, me disseram: É necessário que ainda profetizes a respeito de muitos povos, nações, línguas e reis.*
1 Foi-me dado um caniço semelhante a uma vara, e também me foi dito: Dispõe-te e mede o santuário de Deus, o seu altar e os que naquele adoram;
2 mas deixa de parte o átrio exterior do santuário e não o meças, porque foi ele dado aos gentios; estes, por quarenta e dois meses, calcarão aos pés a cidade santa.
3 Darei às minhas duas testemunhas que profetizem por mil duzentos e sessenta dias, vestidas de pano de saco.
4 São estas as duas oliveiras e os dois candeeiros que se acham em pé diante do Senhor da terra.
5 Se alguém pretende causar-lhes dano, sai fogo da sua boca e devora os inimigos; sim, se alguém pretender causar-lhes dano, certamente, deve morrer.
6 Elas têm autoridade para fechar o céu, para que não chova durante os dias em que profetizarem. Têm autoridade também sobre as águas, para convertê-las em sangue, bem como para ferir a terra com toda sorte de flagelos, tantas vezes quantas quiserem.
7 Quando tiverem, então, concluído o testemunho que devem dar, a besta que surge do abismo pelejará contra elas, e as vencerá, e matará,
8 e o seu cadáver ficará estirado na praça da grande cidade que, espiritualmente, se chama Sodoma e Egito, onde também o seu Senhor foi crucificado.
9 Então, muitos dentre os povos, tribos, línguas e nações contemplam os cadáveres das duas testemunhas, por três dias e meio, e não permitem que esses cadáveres sejam sepultados.
10 Os que habitam sobre a terra se alegram por causa deles, realizarão festas e enviarão presentes uns aos outros, porquanto esses dois profetas atormentaram os que moram sobre a terra.
11 Mas, depois dos três dias e meio, um espírito de vida, vindo da parte de Deus, neles penetrou, e eles se ergueram sobre os pés, e àqueles que os viram sobreveio grande medo;
12 e as duas testemunhas ouviram grande voz vinda do céu, dizendo-lhes: Subi para aqui. E subiram ao céu numa nuvem, e os seus inimigos as contemplaram.
13 Naquela hora, houve grande terremoto, e ruiu a décima parte da cidade, e morreram, nesse terremoto, sete mil pessoas, ao passo que as outras ficaram sobremodo aterrorizadas e deram glória ao Deus do céu.
14 Passou o segundo ai. Eis que, sem demora, vem o terceiro ai.
15 O sétimo anjo tocou a trombeta, e houve no céu grandes vozes, dizendo: O reino do mundo se tornou de nosso Senhor e do seu Cristo, e ele reinará pelos séculos dos séculos.
16 E os vinte e quatro anciãos que se encontram sentados no seu trono, diante de Deus, prostraram-se sobre o seu rosto e adoraram a Deus,
17 dizendo: Graças te damos, Senhor Deus, Todo-Poderoso, que és e que eras, porque assumiste o teu grande poder e passaste a reinar.
18 Na verdade, as nações se enfureceram; chegou, porém, a tua ira, e o tempo determinado para serem julgados os mortos, para se dar o galardão aos teus servos, os profetas, aos santos e aos que temem o teu nome, tanto aos pequenos como aos grandes, e para destruíres os que destroem a terra.
19 Abriu-se, então, o santuário de Deus, que se acha no céu, e foi vista a arca da Aliança no seu santuário, e sobrevieram relâmpagos, vozes, trovões, terremoto e grande saraivada.*
1 Viu-se grande sinal no céu, a saber, uma mulher vestida do sol com a lua debaixo dos pés e uma coroa de doze estrelas na cabeça,
2 que, achando-se grávida, grita com as dores de parto, sofrendo tormentos para dar à luz.
3 Viu-se, também, outro sinal no céu, e eis um dragão, grande, vermelho, com sete cabeças, dez chifres e, nas cabeças, sete diademas.
4 A sua cauda arrastava a terça parte das estrelas do céu, as quais lançou para a terra; e o dragão se deteve em frente da mulher que estava para dar à luz, a fim de lhe devorar o filho quando nascesse.
5 Nasceu-lhe, pois, um filho varão, que há de reger todas as nações com cetro de ferro. E o seu filho foi arrebatado para Deus até ao seu trono.
6 A mulher, porém, fugiu para o deserto, onde lhe havia Deus preparado lugar para que nele a sustentem durante mil duzentos e sessenta dias.
7 Houve peleja no céu. Miguel e os seus anjos pelejaram contra o dragão. Também pelejaram o dragão e seus anjos;
8 todavia, não prevaleceram; nem mais se achou no céu o lugar deles.
9 E foi expulso o grande dragão, a antiga serpente, que se chama diabo e Satanás, o sedutor de todo o mundo, sim, foi atirado para a terra, e, com ele, os seus anjos.
10 Então, ouvi grande voz do céu, proclamando: Agora, veio a salvação, o poder, o reino do nosso Deus e a autoridade do seu Cristo, pois foi expulso o acusador de nossos irmãos, o mesmo que os acusa de dia e de noite, diante do nosso Deus.
11 Eles, pois, o venceram por causa do sangue do Cordeiro e por causa da palavra do testemunho que deram e, mesmo em face da morte, não amaram a própria vida.
12 Por isso, festejai, ó céus, e vós, os que neles habitais. Ai da terra e do mar, pois o diabo desceu até vós, cheio de grande cólera, sabendo que pouco tempo lhe resta.
13 Quando, pois, o dragão se viu atirado para a terra, perseguiu a mulher que dera à luz o filho varão;
14 e foram dadas à mulher as duas asas da grande águia, para que voasse até ao deserto, ao seu lugar, aí onde é sustentada durante um tempo, tempos e metade de um tempo, fora da vista da serpente.
15 Então, a serpente arrojou da sua boca, atrás da mulher, água como um rio, a fim de fazer com que ela fosse arrebatada pelo rio.
16 A terra, porém, socorreu a mulher; e a terra abriu a boca e engoliu o rio que o dragão tinha arrojado de sua boca.
17 Irou-se o dragão contra a mulher e foi pelejar com os restantes da sua descendência, os que guardam os mandamentos de Deus e têm o testemunho de Jesus; e se pôs em pé sobre a areia do mar.*
1 Vi emergir do mar uma besta que tinha dez chifres e sete cabeças e, sobre os chifres, dez diademas e, sobre as cabeças, nomes de blasfêmia.
2 A besta que vi era semelhante a leopardo, com pés como de urso e boca como de leão. E deu-lhe o dragão o seu poder, o seu trono e grande autoridade.
3 Então, vi uma de suas cabeças como golpeada de morte, mas essa ferida mortal foi curada; e toda a terra se maravilhou, seguindo a besta;
4 e adoraram o dragão porque deu a sua autoridade à besta; também adoraram a besta, dizendo: Quem é semelhante à besta? Quem pode pelejar contra ela?
5 Foi-lhe dada uma boca que proferia arrogâncias e blasfêmias e autoridade para agir quarenta e dois meses;
6 e abriu a boca em blasfêmias contra Deus, para lhe difamar o nome e difamar o tabernáculo, a saber, os que habitam no céu.
7 Foi-lhe dado, também, que pelejasse contra os santos e os vencesse. Deu-se-lhe ainda autoridade sobre cada tribo, povo, língua e nação;
8 e adorá-la-ão todos os que habitam sobre a terra, aqueles cujos nomes não foram escritos no Livro da Vida do Cordeiro que foi morto desde a fundação do mundo.
9 Se alguém tem ouvidos, ouça.
10 Se alguém leva para cativeiro, para cativeiro vai. Se alguém matar à espada, necessário é que seja morto à espada. Aqui está a perseverança e a fidelidade dos santos.
11 Vi ainda outra besta emergir da terra; possuía dois chifres, parecendo cordeiro, mas falava como dragão.
12 Exerce toda a autoridade da primeira besta na sua presença. Faz com que a terra e os seus habitantes adorem a primeira besta, cuja ferida mortal fora curada.
13 Também opera grandes sinais, de maneira que até fogo do céu faz descer à terra, diante dos homens.
14 Seduz os que habitam sobre a terra por causa dos sinais que lhe foi dado executar diante da besta, dizendo aos que habitam sobre a terra que façam uma imagem à besta, àquela que, ferida à espada, sobreviveu;
15 e lhe foi dado comunicar fôlego à imagem da besta, para que não só a imagem falasse, como ainda fizesse morrer quantos não adorassem a imagem da besta.
16 A todos, os pequenos e os grandes, os ricos e os pobres, os livres e os escravos, faz que lhes seja dada certa marca sobre a mão direita ou sobre a fronte,
17 para que ninguém possa comprar ou vender, senão aquele que tem a marca, o nome da besta ou o número do seu nome.
18 Aqui está a sabedoria. Aquele que tem entendimento calcule o número da besta, pois é número de homem. Ora, esse número é seiscentos e sessenta e seis.*
1 Olhei, e eis o Cordeiro em pé sobre o monte Sião, e com ele cento e quarenta e quatro mil, tendo na fronte escrito o seu nome e o nome de seu Pai.
2 Ouvi uma voz do céu como voz de muitas águas, como voz de grande trovão; também a voz que ouvi era como de harpistas quando tangem a sua harpa.
3 Entoavam novo cântico diante do trono, diante dos quatro seres viventes e dos anciãos. E ninguém pôde aprender o cântico, senão os cento e quarenta e quatro mil que foram comprados da terra.
4 São estes os que não se macularam com mulheres, porque são castos. São eles os seguidores do Cordeiro por onde quer que vá. São os que foram redimidos dentre os homens, primícias para Deus e para o Cordeiro;
5 e não se achou mentira na sua boca; não têm mácula.
6 Vi outro anjo voando pelo meio do céu, tendo um evangelho eterno para pregar aos que se assentam sobre a terra, e a cada nação, e tribo, e língua, e povo,
7 dizendo, em grande voz: Temei a Deus e dai-lhe glória, pois é chegada a hora do seu juízo; e adorai aquele que fez o céu, e a terra, e o mar, e as fontes das águas.
8 Seguiu-se outro anjo, o segundo, dizendo: Caiu, caiu a grande Babilônia que tem dado a beber a todas as nações do vinho da fúria da sua prostituição.
9 Seguiu-se a estes outro anjo, o terceiro, dizendo, em grande voz: Se alguém adora a besta e a sua imagem e recebe a sua marca na fronte ou sobre a mão,
10 também esse beberá do vinho da cólera de Deus, preparado, sem mistura, do cálice da sua ira, e será atormentado com fogo e enxofre, diante dos santos anjos e na presença do Cordeiro.
11 A fumaça do seu tormento sobe pelos séculos dos séculos, e não têm descanso algum, nem de dia nem de noite, os adoradores da besta e da sua imagem e quem quer que receba a marca do seu nome.
12 Aqui está a perseverança dos santos, os que guardam os mandamentos de Deus e a fé em Jesus.
13 Então, ouvi uma voz do céu, dizendo: Escreve: Bem-aventurados os mortos que, desde agora, morrem no Senhor. Sim, diz o Espírito, para que descansem das suas fadigas, pois as suas obras os acompanham.
14 Olhei, e eis uma nuvem branca, e sentado sobre a nuvem um semelhante a filho de homem, tendo na cabeça uma coroa de ouro e na mão uma foice afiada.
15 Outro anjo saiu do santuário, gritando em grande voz para aquele que se achava sentado sobre a nuvem: Toma a tua foice e ceifa, pois chegou a hora de ceifar, visto que a seara da terra já amadureceu!
16 E aquele que estava sentado sobre a nuvem passou a sua foice sobre a terra, e a terra foi ceifada.
17 Então, saiu do santuário, que se encontra no céu, outro anjo, tendo ele mesmo também uma foice afiada.
18 Saiu ainda do altar outro anjo, aquele que tem autoridade sobre o fogo, e falou em grande voz ao que tinha a foice afiada, dizendo: Toma a tua foice afiada e ajunta os cachos da videira da terra, porquanto as suas uvas estão amadurecidas!
19 Então, o anjo passou a sua foice na terra, e vindimou a videira da terra, e lançou-a no grande lagar da cólera de Deus.
20 E o lagar foi pisado fora da cidade, e correu sangue do lagar até aos freios dos cavalos, numa extensão de mil e seiscentos estádios.*
1 Vi no céu outro sinal grande e admirável: sete anjos tendo os sete últimos flagelos, pois com estes se consumou a cólera de Deus.
2 Vi como que um mar de vidro, mesclado de fogo, e os vencedores da besta, da sua imagem e do número do seu nome, que se achavam em pé no mar de vidro, tendo harpas de Deus;
3 e entoavam o cântico de Moisés, servo de Deus, e o cântico do Cordeiro, dizendo: Grandes e admiráveis são as tuas obras, Senhor Deus, Todo-Poderoso! Justos e verdadeiros são os teus caminhos, ó Rei das nações!
4 Quem não temerá e não glorificará o teu nome, ó Senhor? Pois só tu és santo; por isso, todas as nações virão e adorarão diante de ti, porque os teus atos de justiça se fizeram manifestos.
5 Depois destas coisas, olhei, e abriu-se no céu o santuário do tabernáculo do Testemunho,
6 e os sete anjos que tinham os sete flagelos saíram do santuário, vestidos de linho puro e resplandecente e cingidos ao peito com cintas de ouro.
7 Então, um dos quatro seres viventes deu aos sete anjos sete taças de ouro, cheias da cólera de Deus, que vive pelos séculos dos séculos.
8 O santuário se encheu de fumaça procedente da glória de Deus e do seu poder, e ninguém podia penetrar no santuário, enquanto não se cumprissem os sete flagelos dos sete anjos.*
1 Ouvi, vinda do santuário, uma grande voz, dizendo aos sete anjos: Ide e derramai pela terra as sete taças da cólera de Deus.
2 Saiu, pois, o primeiro anjo e derramou a sua taça pela terra, e, aos homens portadores da marca da besta e adoradores da sua imagem, sobrevieram úlceras malignas e perniciosas.
3 Derramou o segundo a sua taça no mar, e este se tornou em sangue como de morto, e morreu todo ser vivente que havia no mar.
4 Derramou o terceiro a sua taça nos rios e nas fontes das águas, e se tornaram em sangue.
5 Então, ouvi o anjo das águas dizendo: Tu és justo, tu que és e que eras, o Santo, pois julgaste estas coisas;
6 porquanto derramaram sangue de santos e de profetas, também sangue lhes tens dado a beber; são dignos disso.
7 Ouvi do altar que se dizia: Certamente, ó Senhor Deus, Todo-Poderoso, verdadeiros e justos são os teus juízos.
8 O quarto anjo derramou a sua taça sobre o sol, e foi-lhe dado queimar os homens com fogo.
9 Com efeito, os homens se queimaram com o intenso calor, e blasfemaram o nome de Deus, que tem autoridade sobre estes flagelos, e nem se arrependeram para lhe darem glória.
10 Derramou o quinto a sua taça sobre o trono da besta, cujo reino se tornou em trevas, e os homens remordiam a língua por causa da dor que sentiam
11 e blasfemaram o Deus do céu por causa das angústias e das úlceras que sofriam; e não se arrependeram de suas obras.
12 Derramou o sexto a sua taça sobre o grande rio Eufrates, cujas águas secaram, para que se preparasse o caminho dos reis que vêm do lado do nascimento do sol.
13 Então, vi sair da boca do dragão, da boca da besta e da boca do falso profeta três espíritos imundos semelhantes a rãs;
14 porque eles são espíritos de demônios, operadores de sinais, e se dirigem aos reis do mundo inteiro com o fim de ajuntá-los para a peleja do grande Dia do Deus Todo-Poderoso.
15 (Eis que venho como vem o ladrão. Bem-aventurado aquele que vigia e guarda as suas vestes, para que não ande nu, e não se veja a sua vergonha.)
16 Então, os ajuntaram no lugar que em hebraico se chama Armagedom.
17 Então, derramou o sétimo anjo a sua taça pelo ar, e saiu grande voz do santuário, do lado do trono, dizendo: Feito está!
18 E sobrevieram relâmpagos, vozes e trovões, e ocorreu grande terremoto, como nunca houve igual desde que há gente sobre a terra; tal foi o terremoto, forte e grande.
19 E a grande cidade se dividiu em três partes, e caíram as cidades das nações. E lembrou-se Deus da grande Babilônia para dar-lhe o cálice do vinho do furor da sua ira.
20 Todas as ilhas fugiram, e os montes não foram achados;
21 também desabou do céu sobre os homens grande saraivada, com pedras que pesavam cerca de um talento; e, por causa do flagelo da chuva de pedras, os homens blasfemaram de Deus, porquanto o seu flagelo era sobremodo grande.*
1 Veio um dos sete anjos que têm as sete taças e falou comigo, dizendo: Vem, mostrar-te-ei o julgamento da grande meretriz que se acha sentada sobre muitas águas,
2 com quem se prostituíram os reis da terra; e, com o vinho de sua devassidão, foi que se embebedaram os que habitam na terra.
3 Transportou-me o anjo, em espírito, a um deserto e vi uma mulher montada numa besta escarlate, besta repleta de nomes de blasfêmia, com sete cabeças e dez chifres.
4 Achava-se a mulher vestida de púrpura e de escarlata, adornada de ouro, de pedras preciosas e de pérolas, tendo na mão um cálice de ouro transbordante de abominações e com as imundícias da sua prostituição.
5 Na sua fronte, achava-se escrito um nome, um mistério: Babilônia, a Grande, a Mãe das Meretrizes e das Abominações da Terra.
6 Então, vi a mulher embriagada com o sangue dos santos e com o sangue das testemunhas de Jesus; e, quando a vi, admirei-me com grande espanto.
7 O anjo, porém, me disse: Por que te admiraste? Dir-te-ei o mistério da mulher e da besta que tem as sete cabeças e os dez chifres e que leva a mulher:
8 a besta que viste, era e não é, está para emergir do abismo e caminha para a destruição. E aqueles que habitam sobre a terra, cujos nomes não foram escritos no Livro da Vida desde a fundação do mundo, se admirarão, vendo a besta que era e não é, mas aparecerá.
9 Aqui está o sentido, que tem sabedoria: as sete cabeças são sete montes, nos quais a mulher está sentada. São também sete reis,
10 dos quais caíram cinco, um existe, e o outro ainda não chegou; e, quando chegar, tem de durar pouco.
11 E a besta, que era e não é, também é ele, o oitavo rei, e procede dos sete, e caminha para a destruição.
12 Os dez chifres que viste são dez reis, os quais ainda não receberam reino, mas recebem autoridade como reis, com a besta, durante uma hora.
13 Têm estes um só pensamento e oferecem à besta o poder e a autoridade que possuem.
14 Pelejarão eles contra o Cordeiro, e o Cordeiro os vencerá, pois é o Senhor dos senhores e o Rei dos reis; vencerão também os chamados, eleitos e fiéis que se acham com ele.
15 Falou-me ainda: As águas que viste, onde a meretriz está assentada, são povos, multidões, nações e línguas.
16 Os dez chifres que viste e a besta, esses odiarão a meretriz, e a farão devastada e despojada, e lhe comerão as carnes, e a consumirão no fogo.
17 Porque em seu coração incutiu Deus que realizem o seu pensamento, o executem à uma e deem à besta o reino que possuem, até que se cumpram as palavras de Deus.
18 A mulher que viste é a grande cidade que domina sobre os reis da terra.*
1 Depois destas coisas, vi descer do céu outro anjo, que tinha grande autoridade, e a terra se iluminou com a sua glória.
2 Então, exclamou com potente voz, dizendo: Caiu! Caiu a grande Babilônia e se tornou morada de demônios, covil de toda espécie de espírito imundo e esconderijo de todo gênero de ave imunda e detestável,
3 pois todas as nações têm bebido do vinho do furor da sua prostituição. Com ela se prostituíram os reis da terra. Também os mercadores da terra se enriqueceram à custa da sua luxúria.
4 Ouvi outra voz do céu, dizendo: Retirai-vos dela, povo meu, para não serdes cúmplices em seus pecados e para não participardes dos seus flagelos;
5 porque os seus pecados se acumularam até ao céu, e Deus se lembrou dos atos iníquos que ela praticou.
6 Dai-lhe em retribuição como também ela retribuiu, pagai-lhe em dobro segundo as suas obras e, no cálice em que ela misturou bebidas, misturai dobrado para ela.
7 O quanto a si mesma se glorificou e viveu em luxúria, dai-lhe em igual medida tormento e pranto, porque diz consigo mesma: Estou sentada como rainha. Viúva, não sou. Pranto, nunca hei de ver!
8 Por isso, em um só dia, sobrevirão os seus flagelos: morte, pranto e fome; e será consumida no fogo, porque poderoso é o Senhor Deus, que a julgou.
9 Ora, chorarão e se lamentarão sobre ela os reis da terra, que com ela se prostituíram e viveram em luxúria, quando virem a fumaceira do seu incêndio,
10 e, conservando-se de longe, pelo medo do seu tormento, dizem: Ai! Ai! Tu, grande cidade, Babilônia, tu, poderosa cidade! Pois, em uma só hora, chegou o teu juízo.
11 E, sobre ela, choram e pranteiam os mercadores da terra, porque já ninguém compra a sua mercadoria,
12 mercadoria de ouro, de prata, de pedras preciosas, de pérolas, de linho finíssimo, de púrpura, de seda, de escarlata; e toda espécie de madeira odorífera, todo gênero de objeto de marfim, toda qualidade de móvel de madeira preciosíssima, de bronze, de ferro e de mármore;
13 e canela de cheiro, especiarias, incenso, unguento, bálsamo, vinho, azeite, flor de farinha, trigo, gado e ovelhas; e de cavalos, de carros, de escravos e até almas humanas.
14 O fruto sazonado, que a tua alma tanto apeteceu, se apartou de ti, e para ti se extinguiu tudo o que é delicado e esplêndido, e nunca jamais serão achados.
15 Os mercadores destas coisas, que, por meio dela, se enriqueceram, conservar-se-ão de longe, pelo medo do seu tormento, chorando e pranteando,
16 dizendo: Ai! Ai da grande cidade, que estava vestida de linho finíssimo, de púrpura, e de escarlata, adornada de ouro, e de pedras preciosas, e de pérolas,
17 porque, em uma só hora, ficou devastada tamanha riqueza! E todo piloto, e todo aquele que navega livremente, e marinheiros, e quantos labutam no mar conservaram-se de longe.
18 Então, vendo a fumaceira do seu incêndio, gritavam: Que cidade se compara à grande cidade?
19 Lançaram pó sobre a cabeça e, chorando e pranteando, gritavam: Ai! Ai da grande cidade, na qual se enriqueceram todos os que possuíam navios no mar, à custa da sua opulência, porque, em uma só hora, foi devastada!
20 Exultai sobre ela, ó céus, e vós, santos, apóstolos e profetas, porque Deus contra ela julgou a vossa causa.
21 Então, um anjo forte levantou uma pedra como grande pedra de moinho e arrojou-a para dentro do mar, dizendo: Assim, com ímpeto, será arrojada Babilônia, a grande cidade, e nunca jamais será achada.
22 E voz de harpistas, de músicos, de tocadores de flautas e de clarins jamais em ti se ouvirá, nem artífice algum de qualquer arte jamais em ti se achará, e nunca jamais em ti se ouvirá o ruído de pedra de moinho.
23 Também jamais em ti brilhará luz de candeia; nem voz de noivo ou de noiva jamais em ti se ouvirá, pois os teus mercadores foram os grandes da terra, porque todas as nações foram seduzidas pela tua feitiçaria.
24 E nela se achou sangue de profetas, de santos e de todos os que foram mortos sobre a terra.*
1 Depois destas coisas, ouvi no céu uma como grande voz de numerosa multidão, dizendo: Aleluia! A salvação, e a glória, e o poder são do nosso Deus,
2 porquanto verdadeiros e justos são os seus juízos, pois julgou a grande meretriz que corrompia a terra com a sua prostituição e das mãos dela vingou o sangue dos seus servos.
3 Segunda vez disseram: Aleluia! E a sua fumaça sobe pelos séculos dos séculos.
4 Os vinte e quatro anciãos e os quatro seres viventes prostraram-se e adoraram a Deus, que se acha sentado no trono, dizendo: Amém! Aleluia!
5 Saiu uma voz do trono, exclamando: Dai louvores ao nosso Deus, todos os seus servos, os que o temeis, os pequenos e os grandes.
6 Então, ouvi uma como voz de numerosa multidão, como de muitas águas e como de fortes trovões, dizendo: Aleluia! Pois reina o Senhor, nosso Deus, o Todo-Poderoso.
7 Alegremo-nos, exultemos e demos-lhe a glória, porque são chegadas as bodas do Cordeiro, cuja esposa a si mesma já se ataviou,
8 pois lhe foi dado vestir-se de linho finíssimo, resplandecente e puro. Porque o linho finíssimo são os atos de justiça dos santos.
9 Então, me falou o anjo: Escreve: Bem-aventurados aqueles que são chamados à ceia das bodas do Cordeiro. E acrescentou: São estas as verdadeiras palavras de Deus.
10 Prostrei-me ante os seus pés para adorá-lo. Ele, porém, me disse: Vê, não faças isso; sou conservo teu e dos teus irmãos que mantêm o testemunho de Jesus; adora a Deus. Pois o testemunho de Jesus é o espírito da profecia.
11 Vi o céu aberto, e eis um cavalo branco. O seu cavaleiro se chama Fiel e Verdadeiro e julga e peleja com justiça.
12 Os seus olhos são chama de fogo; na sua cabeça, há muitos diademas; tem um nome escrito que ninguém conhece, senão ele mesmo.
13 Está vestido com um manto tinto de sangue, e o seu nome se chama o Verbo de Deus;
14 e seguiam-no os exércitos que há no céu, montando cavalos brancos, com vestiduras de linho finíssimo, branco e puro.
15 Sai da sua boca uma espada afiada, para com ela ferir as nações; e ele mesmo as regerá com cetro de ferro e, pessoalmente, pisa o lagar do vinho do furor da ira do Deus Todo-Poderoso.
16 Tem no seu manto e na sua coxa um nome inscrito: Rei dos Reis e Senhor dos Senhores.
17 Então, vi um anjo posto em pé no sol, e clamou com grande voz, falando a todas as aves que voam pelo meio do céu: Vinde, reuni-vos para a grande ceia de Deus,
18 para que comais carnes de reis, carnes de comandantes, carnes de poderosos, carnes de cavalos e seus cavaleiros, carnes de todos, quer livres, quer escravos, tanto pequenos como grandes.
19 E vi a besta e os reis da terra, com os seus exércitos, congregados para pelejarem contra aquele que estava montado no cavalo e contra o seu exército.
20 Mas a besta foi aprisionada, e com ela o falso profeta que, com os sinais feitos diante dela, seduziu aqueles que receberam a marca da besta e eram os adoradores da sua imagem. Os dois foram lançados vivos dentro do lago de fogo que arde com enxofre.
21 Os restantes foram mortos com a espada que saía da boca daquele que estava montado no cavalo. E todas as aves se fartaram das suas carnes.*
1 Então, vi descer do céu um anjo; tinha na mão a chave do abismo e uma grande corrente.
2 Ele segurou o dragão, a antiga serpente, que é o diabo, Satanás, e o prendeu por mil anos;
3 lançou-o no abismo, fechou-o e pôs selo sobre ele, para que não mais enganasse as nações até se completarem os mil anos. Depois disto, é necessário que ele seja solto pouco tempo.
4 Vi também tronos, e nestes sentaram-se aqueles aos quais foi dada autoridade de julgar. Vi ainda as almas dos decapitados por causa do testemunho de Jesus, bem como por causa da palavra de Deus, tantos quantos não adoraram a besta, nem tampouco a sua imagem, e não receberam a marca na fronte e na mão; e viveram e reinaram com Cristo durante mil anos.
5 Os restantes dos mortos não reviveram até que se completassem os mil anos. Esta é a primeira ressurreição.
6 Bem-aventurado e santo é aquele que tem parte na primeira ressurreição; sobre esses a segunda morte não tem autoridade; pelo contrário, serão sacerdotes de Deus e de Cristo e reinarão com ele os mil anos.
7 Quando, porém, se completarem os mil anos, Satanás será solto da sua prisão
8 e sairá a seduzir as nações que há nos quatro cantos da terra, Gogue e Magogue, a fim de reuni-las para a peleja. O número dessas é como a areia do mar.
9 Marcharam, então, pela superfície da terra e sitiaram o acampamento dos santos e a cidade querida; desceu, porém, fogo do céu e os consumiu.
10 O diabo, o sedutor deles, foi lançado para dentro do lago de fogo e enxofre, onde já se encontram não só a besta como também o falso profeta; e serão atormentados de dia e de noite, pelos séculos dos séculos.
11 Vi um grande trono branco e aquele que nele se assenta, de cuja presença fugiram a terra e o céu, e não se achou lugar para eles.
12 Vi também os mortos, os grandes e os pequenos, postos em pé diante do trono. Então, se abriram livros. Ainda outro livro, o Livro da Vida, foi aberto. E os mortos foram julgados, segundo as suas obras, conforme o que se achava escrito nos livros.
13 Deu o mar os mortos que nele estavam. A morte e o além entregaram os mortos que neles havia. E foram julgados, um por um, segundo as suas obras.
14 Então, a morte e o inferno foram lançados para dentro do lago de fogo. Esta é a segunda morte, o lago de fogo.
15 E, se alguém não foi achado inscrito no Livro da Vida, esse foi lançado para dentro do lago de fogo.*
1 Vi novo céu e nova terra, pois o primeiro céu e a primeira terra passaram, e o mar já não existe.
2 Vi também a cidade santa, a nova Jerusalém, que descia do céu, da parte de Deus, ataviada como noiva adornada para o seu esposo.
3 Então, ouvi grande voz vinda do trono, dizendo: Eis o tabernáculo de Deus com os homens. Deus habitará com eles. Eles serão povos de Deus, e Deus mesmo estará com eles.
4 E lhes enxugará dos olhos toda lágrima, e a morte já não existirá, já não haverá luto, nem pranto, nem dor, porque as primeiras coisas passaram.
5 E aquele que está assentado no trono disse: Eis que faço novas todas as coisas. E acrescentou: Escreve, porque estas palavras são fiéis e verdadeiras.
6 Disse-me ainda: Tudo está feito. Eu sou o Alfa e o Ômega, o Princípio e o Fim. Eu, a quem tem sede, darei de graça da fonte da água da vida.
7 O vencedor herdará estas coisas, e eu lhe serei Deus, e ele me será filho.
8 Quanto, porém, aos covardes, aos incrédulos, aos abomináveis, aos assassinos, aos impuros, aos feiticeiros, aos idólatras e a todos os mentirosos, a parte que lhes cabe será no lago que arde com fogo e enxofre, a saber, a segunda morte.
9 Então, veio um dos sete anjos que têm as sete taças cheias dos últimos sete flagelos e falou comigo, dizendo: Vem, mostrar-te-ei a noiva, a esposa do Cordeiro;
10 e me transportou, em espírito, até a uma grande e elevada montanha e me mostrou a santa cidade, Jerusalém, que descia do céu, da parte de Deus,
11 a qual tem a glória de Deus. O seu fulgor era semelhante a uma pedra preciosíssima, como pedra de jaspe cristalina.
12 Tinha grande e alta muralha, doze portas, e, junto às portas, doze anjos, e, sobre elas, nomes inscritos, que são os nomes das doze tribos dos filhos de Israel.
13 Três portas se achavam a leste, três, ao norte, três, ao sul, e três, a oeste.
14 A muralha da cidade tinha doze fundamentos, e estavam sobre estes os doze nomes dos doze apóstolos do Cordeiro.
15 Aquele que falava comigo tinha por medida uma vara de ouro para medir a cidade, as suas portas e a sua muralha.
16 A cidade é quadrangular, de comprimento e largura iguais. E mediu a cidade com a vara até doze mil estádios. O seu comprimento, largura e altura são iguais.
17 Mediu também a sua muralha, cento e quarenta e quatro côvados, medida de homem, isto é, de anjo.
18 A estrutura da muralha é de jaspe; também a cidade é de ouro puro, semelhante a vidro límpido.
19 Os fundamentos da muralha da cidade estão adornados de toda espécie de pedras preciosas. O primeiro fundamento é de jaspe; o segundo, de safira; o terceiro, de calcedônia; o quarto, de esmeralda;
20 o quinto, de sardônio; o sexto, de sárdio; o sétimo, de crisólito; o oitavo, de berilo; o nono, de topázio; o décimo, de crisópraso; o undécimo, de jacinto; e o duodécimo, de ametista.
21 As doze portas são doze pérolas, e cada uma dessas portas, de uma só pérola. A praça da cidade é de ouro puro, como vidro transparente.
22 Nela, não vi santuário, porque o seu santuário é o Senhor, o Deus Todo-Poderoso, e o Cordeiro.
23 A cidade não precisa nem do sol, nem da lua, para lhe darem claridade, pois a glória de Deus a iluminou, e o Cordeiro é a sua lâmpada.
24 As nações andarão mediante a sua luz, e os reis da terra lhe trazem a sua glória.
25 As suas portas nunca jamais se fecharão de dia, porque, nela, não haverá noite.
26 E lhe trarão a glória e a honra das nações.
27 Nela, nunca jamais penetrará coisa alguma contaminada, nem o que pratica abominação e mentira, mas somente os inscritos no Livro da Vida do Cordeiro.*
1 Então, me mostrou o rio da água da vida, brilhante como cristal, que sai do trono de Deus e do Cordeiro.
2 No meio da sua praça, de uma e outra margem do rio, está a árvore da vida, que produz doze frutos, dando o seu fruto de mês em mês, e as folhas da árvore são para a cura dos povos.
3 Nunca mais haverá qualquer maldição. Nela, estará o trono de Deus e do Cordeiro. Os seus servos o servirão,
4 contemplarão a sua face, e na sua fronte está o nome dele.
5 Então, já não haverá noite, nem precisam eles de luz de candeia, nem da luz do sol, porque o Senhor Deus brilhará sobre eles, e reinarão pelos séculos dos séculos.
6 Disse-me ainda: Estas palavras são fiéis e verdadeiras. O Senhor, o Deus dos espíritos dos profetas, enviou seu anjo para mostrar aos seus servos as coisas que em breve devem acontecer.
7 Eis que venho sem demora. Bem-aventurado aquele que guarda as palavras da profecia deste livro.
8 Eu, João, sou quem ouviu e viu estas coisas. E, quando as ouvi e vi, prostrei-me ante os pés do anjo que me mostrou essas coisas, para adorá-lo.
9 Então, ele me disse: Vê, não faças isso; eu sou conservo teu, dos teus irmãos, os profetas, e dos que guardam as palavras deste livro. Adora a Deus.
10 Disse-me ainda: Não seles as palavras da profecia deste livro, porque o tempo está próximo.
11 Continue o injusto fazendo injustiça, continue o imundo ainda sendo imundo; o justo continue na prática da justiça, e o santo continue a santificar-se.
12 E eis que venho sem demora, e comigo está o galardão que tenho para retribuir a cada um segundo as suas obras.
13 Eu sou o Alfa e o Ômega, o Primeiro e o Último, o Princípio e o Fim.
14 Bem-aventurados aqueles que lavam as suas vestiduras [no sangue do Cordeiro], para que lhes assista o direito à árvore da vida, e entrem na cidade pelas portas.
15 Fora ficam os cães, os feiticeiros, os impuros, os assassinos, os idólatras e todo aquele que ama e pratica a mentira.
16 Eu, Jesus, enviei o meu anjo para vos testificar estas coisas às igrejas. Eu sou a Raiz e a Geração de Davi, a brilhante Estrela da manhã.
17 O Espírito e a noiva dizem: Vem! Aquele que ouve, diga: Vem! Aquele que tem sede venha, e quem quiser receba de graça a água da vida.
18 Eu, a todo aquele que ouve as palavras da profecia deste livro, testifico: Se alguém lhes fizer qualquer acréscimo, Deus lhe acrescentará os flagelos escritos neste livro;
19 e, se alguém tirar qualquer coisa das palavras do livro desta profecia, Deus tirará a sua parte da árvore da vida, da cidade santa e das coisas que se acham escritas neste livro.
20 Aquele que dá testemunho destas coisas diz: Certamente, venho sem demora. Amém! Vem, Senhor Jesus!
21 A graça do Senhor Jesus seja com todos.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Apocalipse','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)