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
1 São estes os nomes dos filhos de Israel que entraram com Jacó no Egito; cada um entrou com sua família:
2 Rúben, Simeão, Levi e Judá,
3 Issacar, Zebulom e Benjamim,
4 Dã, Naftali, Gade e Aser.
5 Todas as pessoas, pois, que descenderam de Jacó foram setenta; José, porém, estava no Egito.
6 Faleceu José, e todos os seus irmãos, e toda aquela geração.
7 Mas os filhos de Israel foram fecundos, e aumentaram muito, e se multiplicaram, e grandemente se fortaleceram, de maneira que a terra se encheu deles.
8 Entrementes, se levantou novo rei sobre o Egito, que não conhecera a José.
9 Ele disse ao seu povo: Eis que o povo dos filhos de Israel é mais numeroso e mais forte do que nós.
10 Eia, usemos de astúcia para com ele, para que não se multiplique, e seja o caso que, vindo guerra, ele se ajunte com os nossos inimigos, peleje contra nós e saia da terra.
11 E os egípcios puseram sobre eles feitores de obras, para os afligirem com suas cargas. E os israelitas edificaram a Faraó as cidades-celeiros, Pitom e Ramessés.
12 Mas, quanto mais os afligiam, tanto mais se multiplicavam e tanto mais se espalhavam; de maneira que se inquietavam por causa dos filhos de Israel;
13 então, os egípcios, com tirania, faziam servir os filhos de Israel
14 e lhes fizeram amargar a vida com dura servidão, em barro, e em tijolos, e com todo o trabalho no campo; com todo o serviço em que na tirania os serviam.
As parteiras desobedecem a Faraó
15 O rei do Egito ordenou às parteiras hebreias, das quais uma se chamava Sifrá, e outra, Puá,
16 dizendo: Quando servirdes de parteira às hebreias, examinai: se for filho, matai-o; mas, se for filha, que viva.
17 As parteiras, porém, temeram a Deus e não fizeram como lhes ordenara o rei do Egito; antes, deixaram viver os meninos.
18 Então, o rei do Egito chamou as parteiras e lhes disse: Por que fizestes isso e deixastes viver os meninos?
19 Responderam as parteiras a Faraó: É que as mulheres hebreias não são como as egípcias; são vigorosas e, antes que lhes chegue a parteira, já deram à luz os seus filhos.
20 E Deus fez bem às parteiras; e o povo aumentou e se tornou muito forte.
21 E, porque as parteiras temeram a Deus, ele lhes constituiu família.
22 Então, ordenou Faraó a todo o seu povo, dizendo: A todos os filhos que nascerem aos hebreus lançareis no Nilo, mas a todas as filhas deixareis viver.*
1 Foi-se um homem da casa de Levi e casou com uma descendente de Levi.
2 E a mulher concebeu e deu à luz um filho; e, vendo que era formoso, escondeu-o por três meses.
3 Não podendo, porém, escondê-lo por mais tempo, tomou um cesto de junco, calafetou-o com betume e piche e, pondo nele o menino, largou-o no carriçal à beira do rio.
4 A irmã do menino ficou de longe, para observar o que lhe haveria de suceder.
5 Desceu a filha de Faraó para se banhar no rio, e as suas donzelas passeavam pela beira do rio; vendo ela o cesto no carriçal, enviou a sua criada e o tomou.
6 Abrindo-o, viu a criança; e eis que o menino chorava. Teve compaixão dele e disse: Este é menino dos hebreus.
7 Então, disse sua irmã à filha de Faraó: Queres que eu vá chamar uma das hebreias que sirva de ama e te crie a criança?
8 Respondeu-lhe a filha de Faraó: Vai. Saiu, pois, a moça e chamou a mãe do menino.
9 Então, lhe disse a filha de Faraó: Leva este menino e cria-mo; pagar-te-ei o teu salário. A mulher tomou o menino e o criou.
10 Sendo o menino já grande, ela o trouxe à filha de Faraó, da qual passou ele a ser filho. Esta lhe chamou Moisés e disse: Porque das águas o tirei.
11 Naqueles dias, sendo Moisés já homem, saiu a seus irmãos e viu os seus labores penosos; e viu que certo egípcio espancava um hebreu, um do seu povo.
12 Olhou de um e de outro lado, e, vendo que não havia ali ninguém, matou o egípcio, e o escondeu na areia.
13 Saiu no dia seguinte, e eis que dois hebreus estavam brigando; e disse ao culpado: Por que espancas o teu próximo?
14 O qual respondeu: Quem te pôs por príncipe e juiz sobre nós? Pensas matar-me, como mataste o egípcio? Temeu, pois, Moisés e disse: Com certeza o descobriram.
15 Informado desse caso, procurou Faraó matar a Moisés; porém Moisés fugiu da presença de Faraó e se deteve na terra de Midiã; e assentou-se junto a um poço.
16 O sacerdote de Midiã tinha sete filhas, as quais vieram a tirar água e encheram os bebedouros para dar de beber ao rebanho de seu pai.
17 Então, vieram os pastores e as enxotaram dali; Moisés, porém, se levantou, e as defendeu, e deu de beber ao rebanho.
18 Tendo elas voltado a Reuel, seu pai, este lhes perguntou: Por que viestes, hoje, mais cedo?
19 Responderam elas: Um egípcio nos livrou das mãos dos pastores, e ainda nos tirou água, e deu de beber ao rebanho.
20 E onde está ele?, disse às filhas; por que deixastes lá o homem? Chamai-o para que coma pão.
21 Moisés consentiu em morar com aquele homem; e ele deu a Moisés sua filha Zípora,
22 a qual deu à luz um filho, a quem ele chamou Gérson, porque disse: Sou peregrino em terra estranha.
23 Decorridos muitos dias, morreu o rei do Egito; os filhos de Israel gemiam sob a servidão e por causa dela clamaram, e o seu clamor subiu a Deus.
24 Ouvindo Deus o seu gemido, lembrou-se da sua aliança com Abraão, com Isaque e com Jacó.
25 E viu Deus os filhos de Israel e atentou para a sua condição.*
1 Apascentava Moisés o rebanho de Jetro, seu sogro, sacerdote de Midiã; e, levando o rebanho para o lado ocidental do deserto, chegou ao monte de Deus, a Horebe.
2 Apareceu-lhe o Anjo do Senhor numa chama de fogo, no meio de uma sarça; Moisés olhou, e eis que a sarça ardia no fogo e a sarça não se consumia.
3 Então, disse consigo mesmo: Irei para lá e verei essa grande maravilha; por que a sarça não se queima?
4 Vendo o Senhor que ele se voltava para ver, Deus, do meio da sarça, o chamou e disse: Moisés! Moisés! Ele respondeu: Eis-me aqui!
5 Deus continuou: Não te chegues para cá; tira as sandálias dos pés, porque o lugar em que estás é terra santa.
6 Disse mais: Eu sou o Deus de teu pai, o Deus de Abraão, o Deus de Isaque e o Deus de Jacó. Moisés escondeu o rosto, porque temeu olhar para Deus.
7 Disse ainda o Senhor: Certamente, vi a aflição do meu povo, que está no Egito, e ouvi o seu clamor por causa dos seus exatores. Conheço-lhe o sofrimento;
8 por isso, desci a fim de livrá-lo da mão dos egípcios e para fazê-lo subir daquela terra a uma terra boa e ampla, terra que mana leite e mel; o lugar do cananeu, do heteu, do amorreu, do ferezeu, do heveu e do jebuseu.
9 Pois o clamor dos filhos de Israel chegou até mim, e também vejo a opressão com que os egípcios os estão oprimindo.
10 Vem, agora, e eu te enviarei a Faraó, para que tires o meu povo, os filhos de Israel, do Egito.
11 Então, disse Moisés a Deus: Quem sou eu para ir a Faraó e tirar do Egito os filhos de Israel?
12 Deus lhe respondeu: Eu serei contigo; e este será o sinal de que eu te enviei: depois de haveres tirado o povo do Egito, servireis a Deus neste monte.
13 Disse Moisés a Deus: Eis que, quando eu vier aos filhos de Israel e lhes disser: O Deus de vossos pais me enviou a vós outros; e eles me perguntarem: Qual é o seu nome? Que lhes direi?
14 Disse Deus a Moisés: Eu Sou o Que Sou. Disse mais: Assim dirás aos filhos de Israel: Eu Sou me enviou a vós outros.
15 Disse Deus ainda mais a Moisés: Assim dirás aos filhos de Israel: O Senhor, o Deus de vossos pais, o Deus de Abraão, o Deus de Isaque e o Deus de Jacó, me enviou a vós outros; este é o meu nome eternamente, e assim serei lembrado de geração em geração.
16 Vai, ajunta os anciãos de Israel e dize-lhes: O Senhor, o Deus de vossos pais, o Deus de Abraão, o Deus de Isaque e o Deus de Jacó, me apareceu, dizendo: Em verdade vos tenho visitado e visto o que vos tem sido feito no Egito.
17 Portanto, disse eu: Far-vos-ei subir da aflição do Egito para a terra do cananeu, do heteu, do amorreu, do ferezeu, do heveu e do jebuseu, para uma terra que mana leite e mel.
18 E ouvirão a tua voz; e irás, com os anciãos de Israel, ao rei do Egito e lhe dirás: O Senhor, o Deus dos hebreus, nos encontrou. Agora, pois, deixa-nos ir caminho de três dias para o deserto, a fim de que sacrifiquemos ao Senhor, nosso Deus.
19 Eu sei, porém, que o rei do Egito não vos deixará ir se não for obrigado por mão forte.
20 Portanto, estenderei a mão e ferirei o Egito com todos os meus prodígios que farei no meio dele; depois, vos deixará ir.
21 Eu darei mercê a este povo aos olhos dos egípcios; e, quando sairdes, não será de mãos vazias.
22 Cada mulher pedirá à sua vizinha e à sua hóspeda joias de prata, e joias de ouro, e vestimentas; as quais poreis sobre vossos filhos e sobre vossas filhas; e despojareis os egípcios.*
1 Respondeu Moisés: Mas eis que não crerão, nem acudirão à minha voz, pois dirão: O Senhor não te apareceu.
2 Perguntou-lhe o Senhor: Que é isso que tens na mão? Respondeu-lhe: Um bordão.
3 Então, lhe disse: Lança-o na terra. Ele o lançou na terra, e o bordão virou uma serpente. E Moisés fugia dela.
4 Disse o Senhor a Moisés: Estende a mão e pega-lhe pela cauda (estendeu ele a mão, pegou-lhe pela cauda, e ela se tornou em bordão);
5 para que creiam que te apareceu o Senhor, Deus de seus pais, o Deus de Abraão, o Deus de Isaque e o Deus de Jacó.
6 Disse-lhe mais o Senhor: Mete, agora, a mão no peito. Ele o fez; e, tirando-a, eis que a mão estava leprosa, branca como a neve.
7 Disse ainda o Senhor: Torna a meter a mão no peito. Ele a meteu no peito, novamente; e, quando a tirou, eis que se havia tornado como o restante de sua carne.
8 Se eles te não crerem, nem atenderem à evidência do primeiro sinal, talvez crerão na evidência do segundo.
9 Se nem ainda crerem mediante estes dois sinais, nem te ouvirem a voz, tomarás das águas do rio e as derramarás na terra seca; e as águas que do rio tomares tornar-se-ão em sangue sobre a terra.
10 Então, disse Moisés ao Senhor: Ah! Senhor! Eu nunca fui eloquente, nem outrora, nem depois que falaste a teu servo; pois sou pesado de boca e pesado de língua.
11 Respondeu-lhe o Senhor: Quem fez a boca do homem? Ou quem faz o mudo, ou o surdo, ou o que vê, ou o cego? Não sou eu, o Senhor?
12 Vai, pois, agora, e eu serei com a tua boca e te ensinarei o que hás de falar.
13 Ele, porém, respondeu: Ah! Senhor! Envia aquele que hás de enviar, menos a mim.
14 Então, se acendeu a ira do Senhor contra Moisés, e disse: Não é Arão, o levita, teu irmão? Eu sei que ele fala fluentemente; e eis que ele sai ao teu encontro e, vendo-te, se alegrará em seu coração.
15 Tu, pois, lhe falarás e lhe porás na boca as palavras; eu serei com a tua boca e com a dele e vos ensinarei o que deveis fazer.
16 Ele falará por ti ao povo; ele te será por boca, e tu lhe serás por Deus.
17 Toma, pois, este bordão na mão, com o qual hás de fazer os sinais.
18 Saindo Moisés, voltou para Jetro, seu sogro, e lhe disse: Deixa-me ir, voltar a meus irmãos que estão no Egito para ver se ainda vivem. Disse-lhe Jetro: Vai-te em paz.
19 Disse também o Senhor a Moisés, em Midiã: Vai, torna para o Egito, porque são mortos todos os que procuravam tirar-te a vida.
20 Tomou, pois, Moisés a sua mulher e os seus filhos; fê-los montar num jumento e voltou para a terra do Egito. Moisés levava na mão o bordão de Deus.
21 Disse o Senhor a Moisés: Quando voltares ao Egito, vê que faças diante de Faraó todos os milagres que te hei posto na mão; mas eu lhe endurecerei o coração, para que não deixe ir o povo.
22 Dirás a Faraó: Assim diz o Senhor: Israel é meu filho, meu primogênito.
23 Digo-te, pois: deixa ir meu filho, para que me sirva; mas, se recusares deixá-lo ir, eis que eu matarei teu filho, teu primogênito.
24 Estando Moisés no caminho, numa estalagem, encontrou-o o Senhor e o quis matar.
25 Então, Zípora tomou uma pedra aguda, cortou o prepúcio de seu filho, lançou-o aos pés de Moisés e lhe disse: Sem dúvida, tu és para mim esposo sanguinário.
26 Assim, o Senhor o deixou. Ela disse: Esposo sanguinário, por causa da circuncisão.
27 Disse também o Senhor a Arão: Vai ao deserto para te encontrares com Moisés. Ele foi e, encontrando-o no monte de Deus, o beijou.
28 Relatou Moisés a Arão todas as palavras do Senhor, com as quais o enviara, e todos os sinais que lhe mandara.
29 Então, se foram Moisés e Arão e ajuntaram todos os anciãos dos filhos de Israel.
30 Arão falou todas as palavras que o Senhor tinha dito a Moisés, e este fez os sinais à vista do povo.
31 E o povo creu; e, tendo ouvido que o Senhor havia visitado os filhos de Israel e lhes vira a aflição, inclinaram-se e o adoraram.*
1 Depois, foram Moisés e Arão e disseram a Faraó: Assim diz o Senhor, Deus de Israel: Deixa ir o meu povo, para que me celebre uma festa no deserto.
2 Respondeu Faraó: Quem é o Senhor para que lhe ouça eu a voz e deixe ir a Israel? Não conheço o Senhor, nem tampouco deixarei ir a Israel.
3 Eles prosseguiram: O Deus dos hebreus nos encontrou; deixa-nos ir, pois, caminho de três dias ao deserto, para que ofereçamos sacrifícios ao Senhor, nosso Deus, e não venha ele sobre nós com pestilência ou com espada.
4 Então, lhes disse o rei do Egito: Por que, Moisés e Arão, por que interrompeis o povo no seu trabalho? Ide às vossas tarefas.
5 Disse também Faraó: O povo da terra já é muito, e vós o distraís das suas tarefas.
6 Naquele mesmo dia, pois, deu ordem Faraó aos superintendentes do povo e aos seus capatazes, dizendo:
7 Daqui em diante não torneis a dar palha ao povo, para fazer tijolos, como antes; eles mesmos que vão e ajuntem para si a palha.
8 E exigireis deles a mesma conta de tijolos que antes faziam; nada diminuireis dela; estão ociosos e, por isso, clamam: Vamos e sacrifiquemos ao nosso Deus.
9 Agrave-se o serviço sobre esses homens, para que nele se apliquem e não deem ouvidos a palavras mentirosas.
10 Então, saíram os superintendentes do povo e seus capatazes e falaram ao povo: Assim diz Faraó: Não vos darei palha.
11 Ide vós mesmos e ajuntai palha onde a puderdes achar; porque nada se diminuirá do vosso trabalho.
12 Então, o povo se espalhou por toda a terra do Egito a ajuntar restolho em lugar de palha.
13 Os superintendentes os apertavam, dizendo: Acabai vossa obra, a tarefa do dia, como quando havia palha.
14 E foram açoitados os capatazes dos filhos de Israel, que os superintendentes de Faraó tinham posto sobre eles; e os superintendentes lhes diziam: Por que não acabastes nem ontem, nem hoje a vossa tarefa, fazendo tijolos como antes?
15 Então, foram os capatazes dos filhos de Israel e clamaram a Faraó, dizendo: Por que tratas assim a teus servos?
16 Palha não se dá a teus servos, e nos dizem: Fazei tijolos. Eis que teus servos são açoitados; porém o teu próprio povo é que tem a culpa.
17 Mas ele respondeu: Estais ociosos, estais ociosos; por isso, dizeis: Vamos, sacrifiquemos ao Senhor.
18 Ide, pois, agora, e trabalhai; palha, porém, não se vos dará; contudo, dareis a mesma quantidade de tijolos.
19 Então, os capatazes dos filhos de Israel se viram em aperto, porquanto se lhes dizia: Nada diminuireis dos vossos tijolos, da vossa tarefa diária.
20 Quando saíram da presença de Faraó, encontraram Moisés e Arão, que estavam à espera deles;
21 e lhes disseram: Olhe o Senhor para vós outros e vos julgue, porquanto nos fizestes odiosos aos olhos de Faraó e diante dos seus servos, dando-lhes a espada na mão para nos matar.
22 Então, Moisés, tornando-se ao Senhor, disse: Ó Senhor, por que afligiste este povo? Por que me enviaste?
23 Pois, desde que me apresentei a Faraó, para falar-lhe em teu nome, ele tem maltratado este povo; e tu, de nenhuma sorte, livraste o teu povo.*
1 Disse o Senhor a Moisés: Agora, verás o que hei de fazer a Faraó; pois, por mão poderosa, os deixará ir e, por mão poderosa, os lançará fora da sua terra.
2 Falou mais Deus a Moisés e lhe disse: Eu sou o Senhor.
3 Apareci a Abraão, a Isaque e a Jacó como Deus Todo-Poderoso; mas pelo meu nome, O Senhor, não lhes fui conhecido.
4 Também estabeleci a minha aliança com eles, para dar-lhes a terra de Canaã, a terra em que habitaram como peregrinos.
5 Ainda ouvi os gemidos dos filhos de Israel, os quais os egípcios escravizam, e me lembrei da minha aliança.
6 Portanto, dize aos filhos de Israel: eu sou o Senhor, e vos tirarei de debaixo das cargas do Egito, e vos livrarei da sua servidão, e vos resgatarei com braço estendido e com grandes manifestações de julgamento.
7 Tomar-vos-ei por meu povo e serei vosso Deus; e sabereis que eu sou o Senhor, vosso Deus, que vos tiro de debaixo das cargas do Egito.
8 E vos levarei à terra a qual jurei dar a Abraão, a Isaque e a Jacó; e vo-la darei como possessão. Eu sou o Senhor.
9 Desse modo falou Moisés aos filhos de Israel, mas eles não atenderam a Moisés, por causa da ânsia de espírito e da dura escravidão.
10 Falou mais o Senhor a Moisés, dizendo:
11 Vai ter com Faraó, rei do Egito, e fala-lhe que deixe sair de sua terra os filhos de Israel.
12 Moisés, porém, respondeu ao Senhor, dizendo: Eis que os filhos de Israel não me têm ouvido; como, pois, me ouvirá Faraó? E não sei falar bem.
13 Não obstante, falou o Senhor a Moisés e a Arão e lhes deu mandamento para os filhos de Israel e para Faraó, rei do Egito, a fim de que tirassem os filhos de Israel da terra do Egito.
14 São estes os chefes das famílias: os filhos de Rúben, o primogênito de Israel: Enoque, Palu, Hezrom e Carmi; são estas as famílias de Rúben.
15 Os filhos de Simeão: Jemuel, Jamim, Oade, Jaquim, Zoar e Saul, filho de uma cananeia; são estas as famílias de Simeão.
16 São estes os nomes dos filhos de Levi, segundo as suas gerações: Gérson, Coate e Merari; e os anos da vida de Levi foram cento e trinta e sete.
17 Os filhos de Gérson: Libni e Simei, segundo as suas famílias.
18 Os filhos de Coate: Anrão, Isar, Hebrom e Uziel; e os anos da vida de Coate foram cento e trinta e três.
19 Os filhos de Merari: Mali e Musi; são estas as famílias de Levi, segundo as suas gerações.
20 Anrão tomou por mulher a Joquebede, sua tia; e ela lhe deu a Arão e Moisés; e os anos da vida de Anrão foram cento e trinta e sete.
21 Os filhos de Isar: Corá, Nefegue e Zicri.
22 Os filhos de Uziel: Misael, Elzafã e Sitri.
23 Arão tomou por mulher a Eliseba, filha de Aminadabe, irmã de Naassom; e ela lhe deu à luz Nadabe, Abiú, Eleazar e Itamar.
24 Os filhos de Corá: Assir, Elcana e Abiasafe; são estas as famílias dos coraítas.
25 Eleazar, filho de Arão, tomou por mulher, para si, uma das filhas de Putiel; e ela lhe deu à luz Fineias; são estes os chefes de suas casas, segundo as suas famílias.
26 São estes Arão e Moisés, aos quais o Senhor disse: Tirai os filhos de Israel da terra do Egito, segundo as suas hostes.
27 São estes que falaram a Faraó, rei do Egito, a fim de tirarem do Egito os filhos de Israel; são estes Moisés e Arão.
28 No dia em que o Senhor falou a Moisés na terra do Egito,
29 disse o Senhor a Moisés: Eu sou o Senhor; dize a Faraó, rei do Egito, tudo o que eu te digo.
30 Respondeu Moisés na presença do Senhor: Eu não sei falar bem; como, pois, me ouvirá Faraó?*
1 Então, disse o Senhor a Moisés: Vê que te constituí como Deus sobre Faraó, e Arão, teu irmão, será teu profeta.
2 Tu falarás tudo o que eu te ordenar; e Arão, teu irmão, falará a Faraó, para que deixe ir da sua terra os filhos de Israel.
3 Eu, porém, endurecerei o coração de Faraó e multiplicarei na terra do Egito os meus sinais e as minhas maravilhas.
4 Faraó não vos ouvirá; e eu porei a mão sobre o Egito e farei sair as minhas hostes, o meu povo, os filhos de Israel, da terra do Egito, com grandes manifestações de julgamento.
5 Saberão os egípcios que eu sou o Senhor, quando estender eu a mão sobre o Egito e tirar do meio deles os filhos de Israel.
6 Assim fez Moisés e Arão; como o Senhor lhes ordenara, assim fizeram.
7 Era Moisés de oitenta anos, e Arão, de oitenta e três, quando falaram a Faraó.
8 Falou o Senhor a Moisés e a Arão:
9 Quando Faraó vos disser: Fazei milagres que vos acreditem, dirás a Arão: Toma o teu bordão e lança-o diante de Faraó; e o bordão se tornará em serpente.
10 Então, Moisés e Arão se chegaram a Faraó e fizeram como o Senhor lhes ordenara; lançou Arão o seu bordão diante de Faraó e diante dos seus oficiais, e ele se tornou em serpente.
11 Faraó, porém, mandou vir os sábios e encantadores; e eles, os sábios do Egito, fizeram também o mesmo com as suas ciências ocultas.
12 Pois lançaram eles cada um o seu bordão, e eles se tornaram em serpentes; mas o bordão de Arão devorou os bordões deles.
13 Todavia, o coração de Faraó se endureceu, e não os ouviu, como o Senhor tinha dito.
14 Disse o Senhor a Moisés: O coração de Faraó está obstinado; recusa deixar ir o povo.
15 Vai ter com Faraó pela manhã; ele sairá às águas; estarás à espera dele na beira do rio, tomarás na mão o bordão que se tornou em serpente
16 e lhe dirás: O Senhor, o Deus dos hebreus, me enviou a ti para te dizer: Deixa ir o meu povo, para que me sirva no deserto; e, até agora, não tens ouvido.
17 Assim diz o Senhor: Nisto saberás que eu sou o Senhor: com este bordão que tenho na mão ferirei as águas do rio, e se tornarão em sangue.
18 Os peixes que estão no rio morrerão, o rio cheirará mal, e os egípcios terão nojo de beber água do rio.
19 Disse mais o Senhor a Moisés: Dize a Arão: toma o teu bordão e estende a mão sobre as águas do Egito, sobre os seus rios, sobre os seus canais, sobre as suas lagoas e sobre todos os seus reservatórios, para que se tornem em sangue; haja sangue em toda a terra do Egito, tanto nos vasos de madeira como nos de pedra.
20 Fizeram Moisés e Arão como o Senhor lhes havia ordenado: Arão, levantando o bordão, feriu as águas que estavam no rio, à vista de Faraó e seus oficiais; e toda a água do rio se tornou em sangue.
21 De sorte que os peixes que estavam no rio morreram, o rio cheirou mal, e os egípcios não podiam beber a água do rio; e houve sangue por toda a terra do Egito.
22 Porém os magos do Egito fizeram também o mesmo com as suas ciências ocultas; de maneira que o coração de Faraó se endureceu, e não os ouviu, como o Senhor tinha dito.
23 Virou-se Faraó e foi para casa; nem ainda isso considerou o seu coração.
24 Todos os egípcios cavaram junto ao rio para encontrar água que beber, pois das águas do rio não podiam beber.
25 Assim se passaram sete dias, depois que o Senhor feriu o rio.*
1 Depois, disse o Senhor a Moisés: Chega-te a Faraó e dize-lhe: Assim diz o Senhor: Deixa ir o meu povo, para que me sirva.
2 Se recusares deixá-lo ir, eis que castigarei com rãs todos os teus territórios.
3 O rio produzirá rãs em abundância, que subirão e entrarão em tua casa, e no teu quarto de dormir, e sobre o teu leito, e nas casas dos teus oficiais, e sobre o teu povo, e nos teus fornos, e nas tuas amassadeiras.
4 As rãs virão sobre ti, sobre o teu povo e sobre todos os teus oficiais.
5 Disse mais o Senhor a Moisés: Dize a Arão: Estende a mão com o teu bordão sobre os rios, sobre os canais e sobre as lagoas e faze subir rãs sobre a terra do Egito.
6 Arão estendeu a mão sobre as águas do Egito, e subiram rãs e cobriram a terra do Egito.
7 Então, os magos fizeram o mesmo com suas ciências ocultas e fizeram aparecer rãs sobre a terra do Egito.
8 Chamou Faraó a Moisés e a Arão e lhes disse: Rogai ao Senhor que tire as rãs de mim e do meu povo; então, deixarei ir o povo, para que ofereça sacrifícios ao Senhor.
9 Falou Moisés a Faraó: Digna-te dizer-me quando é que hei de rogar por ti, pelos teus oficiais e pelo teu povo, para que as rãs sejam retiradas de ti e das tuas casas e fiquem somente no rio.
10 Ele respondeu: Amanhã. Moisés disse: Seja conforme a tua palavra, para que saibas que ninguém há como o Senhor, nosso Deus.
11 Retirar-se-ão as rãs de ti, e das tuas casas, e dos teus oficiais, e do teu povo; ficarão somente no rio.
12 Então, saíram Moisés e Arão da presença de Faraó; e Moisés clamou ao Senhor por causa das rãs, conforme combinara com Faraó.
13 E o Senhor fez conforme a palavra de Moisés; morreram as rãs nas casas, nos pátios e nos campos.
14 Ajuntaram-nas em montões e montões, e a terra cheirou mal.
15 Vendo, porém, Faraó que havia alívio, continuou de coração endurecido e não os ouviu, como o Senhor tinha dito.
16 Disse o Senhor a Moisés: Dize a Arão: Estende o teu bordão e fere o pó da terra, para que se torne em piolhos por toda a terra do Egito.
17 Fizeram assim; Arão estendeu a mão com seu bordão e feriu o pó da terra, e houve muitos piolhos nos homens e no gado; todo o pó da terra se tornou em piolhos por toda a terra do Egito.
18 E fizeram os magos o mesmo com suas ciências ocultas para produzirem piolhos, porém não o puderam; e havia piolhos nos homens e no gado.
19 Então, disseram os magos a Faraó: Isto é o dedo de Deus. Porém o coração de Faraó se endureceu, e não os ouviu, como o Senhor tinha dito.
20 Disse o Senhor a Moisés: Levanta-te pela manhã cedo e apresenta-te a Faraó; eis que ele sairá às águas; e dize-lhe: Assim diz o Senhor: Deixa ir o meu povo, para que me sirva.
21 Do contrário, se tu não deixares ir o meu povo, eis que eu enviarei enxames de moscas sobre ti, e sobre os teus oficiais, e sobre o teu povo, e nas tuas casas; e as casas dos egípcios se encherão destes enxames, e também a terra em que eles estiverem.
22 Naquele dia, separarei a terra de Gósen, em que habita o meu povo, para que nela não haja enxames de moscas, e saibas que eu sou o Senhor no meio desta terra.
23 Farei distinção entre o meu povo e o teu povo; amanhã se dará este sinal.
24 Assim fez o Senhor; e vieram grandes enxames de moscas à casa de Faraó, e às casas dos seus oficiais, e sobre toda a terra do Egito; e a terra ficou arruinada com estes enxames.
25 Chamou Faraó a Moisés e a Arão e disse: Ide, oferecei sacrifícios ao vosso Deus nesta terra.
26 Respondeu Moisés: Não convém que façamos assim porque ofereceríamos ao Senhor, nosso Deus, sacrifícios abomináveis aos egípcios; eis que, se oferecermos tais sacrifícios perante os seus olhos, não nos apedrejarão eles?
27 Temos de ir caminho de três dias ao deserto e ofereceremos sacrifícios ao Senhor, nosso Deus, como ele nos disser.
28 Então, disse Faraó: Deixar-vos-ei ir, para que ofereçais sacrifícios ao Senhor, vosso Deus, no deserto; somente que, saindo, não vades muito longe; orai também por mim.
29 Respondeu-lhe Moisés: Eis que saio da tua presença e orarei ao Senhor; amanhã, estes enxames de moscas se retirarão de Faraó, dos seus oficiais e do seu povo; somente que Faraó não mais me engane, não deixando ir o povo para que ofereça sacrifícios ao Senhor.
30 Então, saiu Moisés da presença de Faraó e orou ao Senhor.
31 E fez o Senhor conforme a palavra de Moisés, e os enxames de moscas se retiraram de Faraó, dos seus oficiais e do seu povo; não ficou uma só mosca.
32 Mas ainda esta vez endureceu Faraó o coração e não deixou ir o povo.*
1 Disse o Senhor a Moisés: Apresenta-te a Faraó e dize-lhe: Assim diz o Senhor, o Deus dos hebreus: Deixa ir o meu povo, para que me sirva.
2 Porque, se recusares deixá-los ir e ainda por força os detiveres,
3 eis que a mão do Senhor será sobre o teu rebanho, que está no campo, sobre os cavalos, sobre os jumentos, sobre os camelos, sobre o gado e sobre as ovelhas, com pestilência gravíssima.
4 E o Senhor fará distinção entre os rebanhos de Israel e o rebanho do Egito, para que nada morra de tudo o que pertence aos filhos de Israel.
5 O Senhor designou certo tempo, dizendo: Amanhã, fará o Senhor isto na terra.
6 E o Senhor o fez no dia seguinte, e todo o rebanho dos egípcios morreu; porém, do rebanho dos israelitas, não morreu nem um.
7 Faraó mandou ver, e eis que do rebanho de Israel não morrera nem um sequer; porém o coração de Faraó se endureceu, e não deixou ir o povo.
8 Então, disse o Senhor a Moisés e a Arão: Apanhai mãos cheias de cinza de forno, e Moisés atire-a para o céu diante de Faraó.
9 Ela se tornará em pó miúdo sobre toda a terra do Egito e se tornará em tumores que se arrebentem em úlceras nos homens e nos animais, por toda a terra do Egito.
10 Eles tomaram cinza de forno e se apresentaram a Faraó; Moisés atirou-a para o céu, e ela se tornou em tumores que se arrebentavam em úlceras nos homens e nos animais,
11 de maneira que os magos não podiam permanecer diante de Moisés, por causa dos tumores; porque havia tumores nos magos e em todos os egípcios.
12 Porém o Senhor endureceu o coração de Faraó, e este não os ouviu, como o Senhor tinha dito a Moisés.
13 Disse o Senhor a Moisés: Levanta-te pela manhã cedo, apresenta-te a Faraó e dize-lhe: Assim diz o Senhor, o Deus dos hebreus: Deixa ir o meu povo, para que me sirva.
14 Pois esta vez enviarei todas as minhas pragas sobre o teu coração, e sobre os teus oficiais, e sobre o teu povo, para que saibas que não há quem me seja semelhante em toda a terra.
15 Pois já eu poderia ter estendido a mão para te ferir a ti e o teu povo com pestilência, e terias sido cortado da terra;
16 mas, deveras, para isso te hei mantido, a fim de mostrar-te o meu poder, e para que seja o meu nome anunciado em toda a terra.
17 Ainda te levantas contra o meu povo, para não deixá-lo ir?
18 Eis que amanhã, por este tempo, farei cair mui grave chuva de pedras, como nunca houve no Egito, desde o dia em que foi fundado até hoje.
19 Agora, pois, manda recolher o teu gado e tudo o que tens no campo; todo homem e animal que se acharem no campo e não se recolherem a casa, em caindo sobre eles a chuva de pedras, morrerão.
20 Quem dos oficiais de Faraó temia a palavra do Senhor fez fugir os seus servos e o seu gado para as casas;
21 aquele, porém, que não se importava com a palavra do Senhor deixou ficar no campo os seus servos e o seu gado.
22 Então, disse o Senhor a Moisés: Estende a mão para o céu, e cairá chuva de pedras em toda a terra do Egito, sobre homens, sobre animais e sobre toda planta do campo na terra do Egito.
23 E Moisés estendeu o seu bordão para o céu; o Senhor deu trovões e chuva de pedras, e fogo desceu sobre a terra; e fez o Senhor cair chuva de pedras sobre a terra do Egito.
24 De maneira que havia chuva de pedras e fogo misturado com a chuva de pedras tão grave, qual nunca houve em toda a terra do Egito, desde que veio a ser uma nação.
25 Por toda a terra do Egito a chuva de pedras feriu tudo quanto havia no campo, tanto homens como animais; feriu também a chuva de pedras toda planta do campo e quebrou todas as árvores do campo.
26 Somente na terra de Gósen, onde estavam os filhos de Israel, não havia chuva de pedras.
27 Então, Faraó mandou chamar a Moisés e a Arão e lhes disse: Esta vez pequei; o Senhor é justo, porém eu e o meu povo somos ímpios.
28 Orai ao Senhor; pois já bastam estes grandes trovões e a chuva de pedras. Eu vos deixarei ir, e não ficareis mais aqui.
29 Respondeu-lhe Moisés: Em saindo eu da cidade, estenderei as mãos ao Senhor; os trovões cessarão, e já não haverá chuva de pedras; para que saibas que a terra é do Senhor.
30 Quanto a ti, porém, e aos teus oficiais, eu sei que ainda não temeis ao Senhor Deus.
31 (O linho e a cevada foram feridos, pois a cevada já estava na espiga, e o linho, em flor.
32 Porém o trigo e o centeio não sofreram dano, porque ainda não haviam nascido.)
33 Saiu, pois, Moisés da presença de Faraó e da cidade e estendeu as mãos ao Senhor; cessaram os trovões e a chuva de pedras, e não caiu mais chuva sobre a terra.
34 Tendo visto Faraó que cessaram as chuvas, as pedras e os trovões, tornou a pecar e endureceu o coração, ele e os seus oficiais.
35 E assim Faraó, de coração endurecido, não deixou ir os filhos de Israel, como o Senhor tinha dito a Moisés.*
1 Disse o Senhor a Moisés: Vai ter com Faraó, porque lhe endureci o coração e o coração de seus oficiais, para que eu faça estes meus sinais no meio deles,
2 e para que contes a teus filhos e aos filhos de teus filhos como zombei dos egípcios e quantos prodígios fiz no meio deles, e para que saibais que eu sou o Senhor.
3 Apresentaram-se, pois, Moisés e Arão perante Faraó e lhe disseram: Assim diz o Senhor, o Deus dos hebreus: Até quando recusarás humilhar-te perante mim? Deixa ir o meu povo, para que me sirva.
4 Do contrário, se recusares deixar ir o meu povo, eis que amanhã trarei gafanhotos ao teu território;
5 eles cobrirão de tal maneira a face da terra, que dela nada aparecerá; eles comerão o restante que escapou, o que vos resta da chuva de pedras, e comerão toda árvore que vos cresce no campo;
6 e encherão as tuas casas, e as casas de todos os teus oficiais, e as casas de todos os egípcios, como nunca viram teus pais, nem os teus antepassados desde o dia em que se acharam na terra até ao dia de hoje. Virou-se e saiu da presença de Faraó.
7 Então, os oficiais de Faraó lhe disseram: Até quando nos será por cilada este homem? Deixa ir os homens, para que sirvam ao Senhor, seu Deus. Acaso, não sabes ainda que o Egito está arruinado?
8 Então, Moisés e Arão foram conduzidos à presença de Faraó; e este lhes disse: Ide, servi ao Senhor, vosso Deus; porém quais são os que hão de ir?
9 Respondeu-lhe Moisés: Havemos de ir com os nossos jovens, e com os nossos velhos, e com os filhos, e com as filhas, e com os nossos rebanhos, e com os nossos gados; havemos de ir, porque temos de celebrar festa ao Senhor.
10 Replicou-lhes Faraó: Seja o Senhor convosco, caso eu vos deixe ir e as crianças. Vede, pois tendes conosco más intenções.
11 Não há de ser assim; ide somente vós, os homens, e servi ao Senhor; pois isso é o que pedistes. E os expulsaram da presença de Faraó.
12 Então, disse o Senhor a Moisés: Estende a mão sobre a terra do Egito, para que venham os gafanhotos sobre a terra do Egito e comam toda a erva da terra, tudo o que deixou a chuva de pedras.
13 Estendeu, pois, Moisés o seu bordão sobre a terra do Egito, e o Senhor trouxe sobre a terra um vento oriental todo aquele dia e toda aquela noite; quando amanheceu, o vento oriental tinha trazido os gafanhotos.
14 E subiram os gafanhotos por toda a terra do Egito e pousaram sobre todo o seu território; eram mui numerosos; antes destes, nunca houve tais gafanhotos, nem depois deles virão outros assim.
15 Porque cobriram a superfície de toda a terra, de modo que a terra se escureceu; devoraram toda a erva da terra e todo fruto das árvores que deixara a chuva de pedras; e não restou nada verde nas árvores, nem na erva do campo, em toda a terra do Egito.
16 Então, se apressou Faraó em chamar a Moisés e a Arão e lhes disse: Pequei contra o Senhor, vosso Deus, e contra vós outros.
17 Agora, pois, peço-vos que me perdoeis o pecado esta vez ainda e que oreis ao Senhor, vosso Deus, que tire de mim esta morte.
18 E Moisés, tendo saído da presença de Faraó, orou ao Senhor.
19 Então, o Senhor fez soprar fortíssimo vento ocidental, o qual levantou os gafanhotos e os lançou no mar Vermelho; nem ainda um só gafanhoto restou em todo o território do Egito.
20 O Senhor, porém, endureceu o coração de Faraó, e este não deixou ir os filhos de Israel.21 Então, disse o Senhor a Moisés: Estende a mão para o céu, e virão trevas sobre a terra do Egito, trevas que se possam apalpar.
22 Estendeu, pois, Moisés a mão para o céu, e houve trevas espessas sobre toda a terra do Egito por três dias;
23 não viram uns aos outros, e ninguém se levantou do seu lugar por três dias; porém todos os filhos de Israel tinham luz nas suas habitações.
24 Então, Faraó chamou a Moisés e lhe disse: Ide, servi ao Senhor. Fiquem somente os vossos rebanhos e o vosso gado; as vossas crianças irão também convosco.
25 Respondeu Moisés: Também tu nos tens de dar em nossas mãos sacrifícios e holocaustos, que ofereçamos ao Senhor, nosso Deus.
26 E também os nossos rebanhos irão conosco, nem uma unha ficará; porque deles havemos de tomar, para servir ao Senhor, nosso Deus, e não sabemos com que havemos de servir ao Senhor, até que cheguemos lá.
27 O Senhor, porém, endureceu o coração de Faraó, e este não quis deixá-los ir.
28 Disse, pois, Faraó a Moisés: Retira-te de mim e guarda-te que não mais vejas o meu rosto; porque, no dia em que vires o meu rosto, morrerás.
29 Respondeu-lhe Moisés: Bem disseste; nunca mais tornarei eu a ver o teu rosto.*
1 Disse o Senhor a Moisés: Ainda mais uma praga trarei sobre Faraó e sobre o Egito. Então, vos deixará ir daqui; quando vos deixar, é certo que vos expulsará totalmente.
2 Fala, agora, aos ouvidos do povo que todo homem peça ao seu vizinho, e toda mulher, à sua vizinha objetos de prata e de ouro.
3 E o Senhor fez que o seu povo encontrasse favor da parte dos egípcios; também o homem Moisés era mui famoso na terra do Egito, aos olhos dos oficiais de Faraó e aos olhos do povo.
4 Moisés disse: Assim diz o Senhor: Cerca da meia-noite passarei pelo meio do Egito.
5 E todo primogênito na terra do Egito morrerá, desde o primogênito de Faraó, que se assenta no seu trono, até ao primogênito da serva que está junto à mó, e todo primogênito dos animais.
6 Haverá grande clamor em toda a terra do Egito, qual nunca houve, nem haverá jamais;
7 porém contra nenhum dos filhos de Israel, desde os homens até aos animais, nem ainda um cão rosnará, para que saibais que o Senhor fez distinção entre os egípcios e os israelitas.
8 Então, todos estes teus oficiais descerão a mim e se inclinarão perante mim, dizendo: Sai tu e todo o povo que te segue. E, depois disto, sairei. E, ardendo em ira, se retirou da presença de Faraó.
9 Então, disse o Senhor a Moisés: Faraó não vos ouvirá, para que as minhas maravilhas se multipliquem na terra do Egito.
10 Moisés e Arão fizeram todas essas maravilhas perante Faraó; mas o Senhor endureceu o coração de Faraó, que não permitiu saíssem da sua terra os filhos de Israel.*
1 Disse o Senhor a Moisés e a Arão na terra do Egito:
2 Este mês vos será o principal dos meses; será o primeiro mês do ano.
3 Falai a toda a congregação de Israel, dizendo: Aos dez deste mês, cada um tomará para si um cordeiro, segundo a casa dos pais, um cordeiro para cada família.
4 Mas, se a família for pequena para um cordeiro, então, convidará ele o seu vizinho mais próximo, conforme o número das almas; conforme o que cada um puder comer, por aí calculareis quantos bastem para o cordeiro.
5 O cordeiro será sem defeito, macho de um ano; podereis tomar um cordeiro ou um cabrito;
6 e o guardareis até ao décimo quarto dia deste mês, e todo o ajuntamento da congregação de Israel o imolará no crepúsculo da tarde.
7 Tomarão do sangue e o porão em ambas as ombreiras e na verga da porta, nas casas em que o comerem;
8 naquela noite, comerão a carne assada no fogo; com pães asmos e ervas amargas a comerão.
9 Não comereis do animal nada cru, nem cozido em água, porém assado ao fogo: a cabeça, as pernas e a fressura.
10 Nada deixareis dele até pela manhã; o que, porém, ficar até pela manhã, queimá-lo-eis.
11 Desta maneira o comereis: lombos cingidos, sandálias nos pés e cajado na mão; comê-lo-eis à pressa; é a Páscoa do Senhor.
12 Porque, naquela noite, passarei pela terra do Egito e ferirei na terra do Egito todos os primogênitos, desde os homens até aos animais; executarei juízo sobre todos os deuses do Egito. Eu sou o Senhor.
13 O sangue vos será por sinal nas casas em que estiverdes; quando eu vir o sangue, passarei por vós, e não haverá entre vós praga destruidora, quando eu ferir a terra do Egito.
14 Este dia vos será por memorial, e o celebrareis como solenidade ao Senhor; nas vossas gerações o celebrareis por estatuto perpétuo.
15 Sete dias comereis pães asmos. Logo ao primeiro dia, tirareis o fermento das vossas casas, pois qualquer que comer coisa levedada, desde o primeiro dia até ao sétimo dia, essa pessoa será eliminada de Israel.
16 Ao primeiro dia, haverá para vós outros santa assembleia; também, ao sétimo dia, tereis santa assembleia; nenhuma obra se fará nele, exceto o que diz respeito ao comer; somente isso podereis fazer.
17 Guardai, pois, a Festa dos Pães Asmos, porque, nesse mesmo dia, tirei vossas hostes da terra do Egito; portanto, guardareis este dia nas vossas gerações por estatuto perpétuo.
18 Desde o dia catorze do primeiro mês, à tarde, comereis pães asmos até à tarde do dia vinte e um do mesmo mês.
19 Por sete dias, não se ache nenhum fermento nas vossas casas; porque qualquer que comer pão levedado será eliminado da congregação de Israel, tanto o peregrino como o natural da terra.
20 Nenhuma coisa levedada comereis; em todas as vossas habitações, comereis pães asmos.
21 Chamou, pois, Moisés todos os anciãos de Israel e lhes disse: Escolhei, e tomai cordeiros segundo as vossas famílias, e imolai a Páscoa.
22 Tomai um molho de hissopo, molhai-o no sangue que estiver na bacia e marcai a verga da porta e suas ombreiras com o sangue que estiver na bacia; nenhum de vós saia da porta da sua casa até pela manhã.
23 Porque o Senhor passará para ferir os egípcios; quando vir, porém, o sangue na verga da porta e em ambas as ombreiras, passará o Senhor aquela porta e não permitirá ao Destruidor que entre em vossas casas, para vos ferir.
24 Guardai, pois, isto por estatuto para vós outros e para vossos filhos, para sempre.
25 E, uma vez dentro na terra que o Senhor vos dará, como tem dito, observai este rito.
26 Quando vossos filhos vos perguntarem: Que rito é este?
27 Respondereis: É o sacrifício da Páscoa ao Senhor, que passou por cima das casas dos filhos de Israel no Egito, quando feriu os egípcios e livrou as nossas casas. Então, o povo se inclinou e adorou.
28 E foram os filhos de Israel e fizeram isso; como o Senhor ordenara a Moisés e a Arão, assim fizeram.
29 Aconteceu que, à meia-noite, feriu o Senhor todos os primogênitos na terra do Egito, desde o primogênito de Faraó, que se assentava no seu trono, até ao primogênito do cativo que estava na enxovia, e todos os primogênitos dos animais.
30 Levantou-se Faraó de noite, ele, todos os seus oficiais e todos os egípcios; e fez-se grande clamor no Egito, pois não havia casa em que não houvesse morto.
31 Então, naquela mesma noite, Faraó chamou a Moisés e a Arão e lhes disse: Levantai-vos, saí do meio do meu povo, tanto vós como os filhos de Israel; ide, servi ao Senhor, como tendes dito.
32 Levai também convosco vossas ovelhas e vosso gado, como tendes dito; ide-vos embora e abençoai-me também a mim.
33 Os egípcios apertavam com o povo, apressando-se em lançá-los fora da terra, pois diziam: Todos morreremos.
34 O povo tomou a sua massa, antes que levedasse, e as suas amassadeiras atadas em trouxas com seus vestidos, sobre os ombros.
35 Fizeram, pois, os filhos de Israel conforme a palavra de Moisés e pediram aos egípcios objetos de prata, e objetos de ouro, e roupas.
36 E o Senhor fez que seu povo encontrasse favor da parte dos egípcios, de maneira que estes lhes davam o que pediam. E despojaram os egípcios.
37 Assim, partiram os filhos de Israel de Ramessés para Sucote, cerca de seiscentos mil a pé, somente de homens, sem contar mulheres e crianças.
38 Subiu também com eles um misto de gente, ovelhas, gado, muitíssimos animais.
39 E cozeram bolos asmos da massa que levaram do Egito; pois não se tinha levedado, porque foram lançados fora do Egito; não puderam deter-se e não haviam preparado para si provisões.
40 Ora, o tempo que os filhos de Israel habitaram no Egito foi de quatrocentos e trinta anos.
41 Aconteceu que, ao cabo dos quatrocentos e trinta anos, nesse mesmo dia, todas as hostes do Senhor saíram da terra do Egito.
42 Esta noite se observará ao Senhor, porque, nela, os tirou da terra do Egito; esta é a noite do Senhor, que devem todos os filhos de Israel comemorar nas suas gerações.
43 Disse mais o Senhor a Moisés e a Arão: Esta é a ordenança da Páscoa: nenhum estrangeiro comerá dela.
44 Porém todo escravo comprado por dinheiro, depois de o teres circuncidado, comerá dela.
45 O estrangeiro e o assalariado não comerão dela.
46 O cordeiro há de ser comido numa só casa; da sua carne não levareis fora da casa, nem lhe quebrareis osso nenhum.
47 Toda a congregação de Israel o fará.
48 Porém, se algum estrangeiro se hospedar contigo e quiser celebrar a Páscoa do Senhor, seja-lhe circuncidado todo macho; e, então, se chegará, e a observará, e será como o natural da terra; mas nenhum incircunciso comerá dela.
49 A mesma lei haja para o natural e para o forasteiro que peregrinar entre vós.
50 Assim fizeram todos os filhos de Israel; como o Senhor ordenara a Moisés e a Arão, assim fizeram.
51 Naquele mesmo dia, tirou o Senhor os filhos de Israel do Egito, segundo as suas turmas.*
1 Disse o Senhor a Moisés:
2 Consagra-me todo primogênito; todo que abre a madre de sua mãe entre os filhos de Israel, tanto de homens como de animais, é meu.
3 Disse Moisés ao povo: Lembrai-vos deste mesmo dia, em que saístes do Egito, da casa da servidão; pois com mão forte o Senhor vos tirou de lá; portanto, não comereis pão levedado.
4 Hoje, mês de abibe, estais saindo.
5 Quando o Senhor te houver introduzido na terra dos cananeus, e dos heteus, e dos amorreus, e dos heveus, e dos jebuseus, a qual jurou a teus pais te dar, terra que mana leite e mel, guardarás este rito neste mês.
6 Sete dias comerás pães asmos; e, ao sétimo dia, haverá solenidade ao Senhor.
7 Sete dias se comerão pães asmos, e o levedado não se encontrará contigo, nem ainda fermento será encontrado em todo o teu território.
8 Naquele mesmo dia, contarás a teu filho, dizendo: É isto pelo que o Senhor me fez, quando saí do Egito.
9 E será como sinal na tua mão e por memorial entre teus olhos; para que a lei do Senhor esteja na tua boca; pois com mão forte o Senhor te tirou do Egito.
10 Portanto, guardarás esta ordenança no determinado tempo, de ano em ano.
11 Quando o Senhor te houver introduzido na terra dos cananeus, como te jurou a ti e a teus pais, quando ta houver dado,
12 apartarás para o Senhor todo que abrir a madre e todo primogênito dos animais que tiveres; os machos serão do Senhor.
13 Porém todo primogênito da jumenta resgatarás com cordeiro; se o não resgatares, será desnucado; mas todo primogênito do homem entre teus filhos resgatarás.
14 Quando teu filho amanhã te perguntar: Que é isso? Responder-lhe-ás: O Senhor com mão forte nos tirou da casa da servidão.
15 Pois sucedeu que, endurecendo-se Faraó para não nos deixar sair, o Senhor matou todos os primogênitos na terra do Egito, desde o primogênito do homem até ao primogênito dos animais; por isso, eu sacrifico ao Senhor todos os machos que abrem a madre; porém a todo primogênito de meus filhos eu resgato.
16 E isto será como sinal na tua mão e por frontais entre os teus olhos; porque o Senhor com mão forte nos tirou do Egito.
17 Tendo Faraó deixado ir o povo, Deus não o levou pelo caminho da terra dos filisteus, posto que mais perto, pois disse: Para que, porventura, o povo não se arrependa, vendo a guerra, e torne ao Egito.
18 Porém Deus fez o povo rodear pelo caminho do deserto perto do mar Vermelho; e, arregimentados, subiram os filhos de Israel do Egito.
19 Também levou Moisés consigo os ossos de José, pois havia este feito os filhos de Israel jurarem solenemente, dizendo: Certamente, Deus vos visitará; daqui, pois, levai convosco os meus ossos.
20 Tendo, pois, partido de Sucote, acamparam-se em Etã, à entrada do deserto.
21 O Senhor ia adiante deles, durante o dia, numa coluna de nuvem, para os guiar pelo caminho; durante a noite, numa coluna de fogo, para os alumiar, a fim de que caminhassem de dia e de noite.
22 Nunca se apartou do povo a coluna de nuvem durante o dia, nem a coluna de fogo durante a noite.*
1 Disse o Senhor a Moisés:
2 Fala aos filhos de Israel que retrocedam e se acampem defronte de Pi-Hairote, entre Migdol e o mar, diante de Baal-Zefom; em frente dele vos acampareis junto ao mar.
3 Então, Faraó dirá dos filhos de Israel: Estão desorientados na terra, o deserto os encerrou.
4 Endurecerei o coração de Faraó, para que os persiga, e serei glorificado em Faraó e em todo o seu exército; e saberão os egípcios que eu sou o Senhor. Eles assim o fizeram.
5 Sendo, pois, anunciado ao rei do Egito que o povo fugia, mudou-se o coração de Faraó e dos seus oficiais contra o povo, e disseram: Que é isto que fizemos, permitindo que Israel nos deixasse de servir?
6 E aprontou Faraó o seu carro e tomou consigo o seu povo;
7 e tomou também seiscentos carros escolhidos e todos os carros do Egito com capitães sobre todos eles.
8 Porque o Senhor endureceu o coração de Faraó, rei do Egito, para que perseguisse os filhos de Israel; porém os filhos de Israel saíram afoitamente.
9 Perseguiram-nos os egípcios, todos os cavalos e carros de Faraó, e os seus cavalarianos, e o seu exército e os alcançaram acampados junto ao mar, perto de Pi-Hairote, defronte de Baal-Zefom.
10 E, chegando Faraó, os filhos de Israel levantaram os olhos, e eis que os egípcios vinham atrás deles, e temeram muito; então, os filhos de Israel clamaram ao Senhor.
11 Disseram a Moisés: Será, por não haver sepulcros no Egito, que nos tiraste de lá, para que morramos neste deserto? Por que nos trataste assim, fazendo-nos sair do Egito?
12 Não é isso o que te dissemos no Egito: deixa-nos, para que sirvamos os egípcios? Pois melhor nos fora servir aos egípcios do que morrermos no deserto.
13 Moisés, porém, respondeu ao povo: Não temais; aquietai-vos e vede o livramento do Senhor que, hoje, vos fará; porque os egípcios, que hoje vedes, nunca mais os tornareis a ver.
14 O Senhor pelejará por vós, e vós vos calareis.
15 Disse o Senhor a Moisés: Por que clamas a mim? Dize aos filhos de Israel que marchem.
16 E tu, levanta o teu bordão, estende a mão sobre o mar e divide-o, para que os filhos de Israel passem pelo meio do mar em seco.
17 Eis que endurecerei o coração dos egípcios, para que vos sigam e entrem nele; serei glorificado em Faraó e em todo o seu exército, nos seus carros e nos seus cavalarianos;
18 e os egípcios saberão que eu sou o Senhor, quando for glorificado em Faraó, nos seus carros e nos seus cavalarianos.
19 Então, o Anjo de Deus, que ia adiante do exército de Israel, se retirou e passou para trás deles; também a coluna de nuvem se retirou de diante deles, e se pôs atrás deles,
20 e ia entre o campo dos egípcios e o campo de Israel; a nuvem era escuridade para aqueles e para este esclarecia a noite; de maneira que, em toda a noite, este e aqueles não puderam aproximar-se.
21 Então, Moisés estendeu a mão sobre o mar, e o Senhor, por um forte vento oriental que soprou toda aquela noite, fez retirar-se o mar, que se tornou terra seca, e as águas foram divididas.
22 Os filhos de Israel entraram pelo meio do mar em seco; e as águas lhes foram qual muro à sua direita e à sua esquerda.
23 Os egípcios que os perseguiam entraram atrás deles, todos os cavalos de Faraó, os seus carros e os seus cavalarianos, até ao meio do mar.
24 Na vigília da manhã, o Senhor, na coluna de fogo e de nuvem, viu o acampamento dos egípcios e alvorotou o acampamento dos egípcios;
25 emperrou-lhes as rodas dos carros e fê-los andar dificultosamente. Então, disseram os egípcios: Fujamos da presença de Israel, porque o Senhor peleja por eles contra os egípcios.
26 Disse o Senhor a Moisés: Estende a mão sobre o mar, para que as águas se voltem sobre os egípcios, sobre os seus carros e sobre os seus cavalarianos.
27 Então, Moisés estendeu a mão sobre o mar, e o mar, ao romper da manhã, retomou a sua força; os egípcios, ao fugirem, foram de encontro a ele, e o Senhor derribou os egípcios no meio do mar.
28 E, voltando as águas, cobriram os carros e os cavalarianos de todo o exército de Faraó, que os haviam seguido no mar; nem ainda um deles ficou.
29 Mas os filhos de Israel caminhavam a pé enxuto pelo meio do mar; e as águas lhes eram quais muros, à sua direita e à sua esquerda.
30 Assim, o Senhor livrou Israel, naquele dia, da mão dos egípcios; e Israel viu os egípcios mortos na praia do mar.
31 E viu Israel o grande poder que o Senhor exercitara contra os egípcios; e o povo temeu ao Senhor e confiou no Senhor e em Moisés, seu servo.*
1 Então, entoou Moisés e os filhos de Israel este cântico ao Senhor, e disseram: Cantarei ao Senhor, porque triunfou gloriosamente; lançou no mar o cavalo e o seu cavaleiro.
2 O Senhor é a minha força e o meu cântico; ele me foi por salvação; este é o meu Deus; portanto, eu o louvarei; ele é o Deus de meu pai; por isso, o exaltarei.
3 O Senhor é homem de guerra; Senhor é o seu nome.
4 Lançou no mar os carros de Faraó e o seu exército; e os seus capitães afogaram-se no mar Vermelho.
5 Os vagalhões os cobriram; desceram às profundezas como pedra.
6 A tua destra, ó Senhor, é gloriosa em poder; a tua destra, ó Senhor, despedaça o inimigo.
7 Na grandeza da tua excelência, derribas os que se levantam contra ti; envias o teu furor, que os consome como restolho.
8 Com o resfolgar das tuas narinas, amontoaram-se as águas, as correntes pararam em montão; os vagalhões coalharam-se no coração do mar.
9 O inimigo dizia: Perseguirei, alcançarei, repartirei os despojos; a minha alma se fartará deles, arrancarei a minha espada, e a minha mão os destruirá.
10 Sopraste com o teu vento, e o mar os cobriu; afundaram-se como chumbo em águas impetuosas.
11 Ó Senhor, quem é como tu entre os deuses? Quem é como tu, glorificado em santidade, terrível em feitos gloriosos, que operas maravilhas?
12 Estendeste a destra; e a terra os tragou.
13 Com a tua beneficência guiaste o povo que salvaste; com a tua força o levaste à habitação da tua santidade.
14 Os povos o ouviram, eles estremeceram; agonias apoderaram-se dos habitantes da Filístia.
15 Ora, os príncipes de Edom se perturbam, dos poderosos de Moabe se apodera temor, esmorecem todos os habitantes de Canaã.
16 Sobre eles cai espanto e pavor; pela grandeza do teu braço, emudecem como pedra; até que passe o teu povo, ó Senhor, até que passe o povo que adquiriste.
17 Tu o introduzirás e o plantarás no monte da tua herança, no lugar que aparelhaste, ó Senhor, para a tua habitação, no santuário, ó Senhor, que as tuas mãos estabeleceram.
18 O Senhor reinará por todo o sempre.
19 Porque os cavalos de Faraó, com os seus carros e com os seus cavalarianos, entraram no mar, e o Senhor fez tornar sobre eles as águas do mar; mas os filhos de Israel passaram a pé enxuto pelo meio do mar.
20 A profetisa Miriã, irmã de Arão, tomou um tamborim, e todas as mulheres saíram atrás dela com tamborins e com danças.
21 E Miriã lhes respondia: Cantai ao Senhor, porque gloriosamente triunfou e precipitou no mar o cavalo e o seu cavaleiro.
22 Fez Moisés partir a Israel do mar Vermelho, e saíram para o deserto de Sur; caminharam três dias no deserto e não acharam água.
23 Afinal, chegaram a Mara; todavia, não puderam beber as águas de Mara, porque eram amargas; por isso, chamou-se-lhe Mara.
24 E o povo murmurou contra Moisés, dizendo: Que havemos de beber?
25 Então, Moisés clamou ao Senhor, e o Senhor lhe mostrou uma árvore; lançou-a Moisés nas águas, e as águas se tornaram doces. Deu-lhes ali estatutos e uma ordenação, e ali os provou,
26 e disse: Se ouvires atento a voz do Senhor, teu Deus, e fizeres o que é reto diante dos seus olhos, e deres ouvido aos seus mandamentos, e guardares todos os seus estatutos, nenhuma enfermidade virá sobre ti, das que enviei sobre os egípcios; pois eu sou o Senhor, que te sara.
27 Então, chegaram a Elim, onde havia doze fontes de água e setenta palmeiras; e se acamparam junto das águas.*
1 Partiram de Elim, e toda a congregação dos filhos de Israel veio para o deserto de Sim, que está entre Elim e Sinai, aos quinze dias do segundo mês, depois que saíram da terra do Egito.
2 Toda a congregação dos filhos de Israel murmurou contra Moisés e Arão no deserto;
3 disseram-lhes os filhos de Israel: Quem nos dera tivéssemos morrido pela mão do Senhor, na terra do Egito, quando estávamos sentados junto às panelas de carne e comíamos pão a fartar! Pois nos trouxestes a este deserto, para matardes de fome toda esta multidão.
4 Então, disse o Senhor a Moisés: Eis que vos farei chover do céu pão, e o povo sairá e colherá diariamente a porção para cada dia, para que eu ponha à prova se anda na minha lei ou não.
5 Dar-se-á que, ao sexto dia, prepararão o que colherem; e será o dobro do que colhem cada dia.
6 Então, disse Moisés e Arão a todos os filhos de Israel: à tarde, sabereis que foi o Senhor quem vos tirou da terra do Egito,
7 e, pela manhã, vereis a glória do Senhor, porquanto ouviu as vossas murmurações; pois quem somos nós, para que murmureis contra nós?
8 Prosseguiu Moisés: Será isso quando o Senhor, à tarde, vos der carne para comer e, pela manhã, pão que vos farte, porquanto o Senhor ouviu as vossas murmurações, com que vos queixais contra ele; pois quem somos nós? As vossas murmurações não são contra nós, e sim contra o Senhor.
9 Disse Moisés a Arão: Dize a toda a congregação dos filhos de Israel: Chegai-vos à presença do Senhor, pois ouviu as vossas murmurações.
10 Quando Arão falava a toda a congregação dos filhos de Israel, olharam para o deserto, e eis que a glória do Senhor apareceu na nuvem.
11 E o Senhor disse a Moisés:
12 Tenho ouvido as murmurações dos filhos de Israel; dize-lhes: Ao crepúsculo da tarde, comereis carne, e, pela manhã, vos fartareis de pão, e sabereis que eu sou o Senhor, vosso Deus.
13 À tarde, subiram codornizes e cobriram o arraial; pela manhã, jazia o orvalho ao redor do arraial.
14 E, quando se evaporou o orvalho que caíra, na superfície do deserto restava uma coisa fina e semelhante a escamas, fina como a geada sobre a terra.
15 Vendo-a os filhos de Israel, disseram uns aos outros: Que é isto? Pois não sabiam o que era. Disse-lhes Moisés: Isto é o pão que o Senhor vos dá para vosso alimento.
16 Eis o que o Senhor vos ordenou: Colhei disso cada um segundo o que pode comer, um gômer por cabeça, segundo o número de vossas pessoas; cada um tomará para os que se acharem na sua tenda.
17 Assim o fizeram os filhos de Israel; e colheram, uns, mais, outros, menos.
18 Porém, medindo-o com o gômer, não sobejava ao que colhera muito, nem faltava ao que colhera pouco, pois colheram cada um quanto podia comer.
19 Disse-lhes Moisés: Ninguém deixe dele para a manhã seguinte.
20 Eles, porém, não deram ouvidos a Moisés, e alguns deixaram do maná para a manhã seguinte; porém deu bichos e cheirava mal. E Moisés se indignou contra eles.
21 Colhiam-no, pois, manhã após manhã, cada um quanto podia comer; porque, em vindo o calor, se derretia.
22 Ao sexto dia, colheram pão em dobro, dois gômeres para cada um; e os principais da congregação vieram e contaram-no a Moisés.
23 Respondeu-lhes ele: Isto é o que disse o Senhor: Amanhã é repouso, o santo sábado do Senhor; o que quiserdes cozer no forno, cozei-o, e o que quiserdes cozer em água, cozei-o em água; e tudo o que sobrar separai, guardando para a manhã seguinte.
24 E guardaram-no até pela manhã seguinte, como Moisés ordenara; e não cheirou mal, nem deu bichos.
25 Então, disse Moisés: Comei-o hoje, porquanto o sábado é do Senhor; hoje, não o achareis no campo.
26 Seis dias o colhereis, mas o sétimo dia é o sábado; nele, não haverá.
27 Ao sétimo dia, saíram alguns do povo para o colher, porém não o acharam.
28 Então, disse o Senhor a Moisés: Até quando recusareis guardar os meus mandamentos e as minhas leis?
29 Considerai que o Senhor vos deu o sábado; por isso, ele, no sexto dia, vos dá pão para dois dias; cada um fique onde está, ninguém saia do seu lugar no sétimo dia.
30 Assim, descansou o povo no sétimo dia.
31 Deu-lhe a casa de Israel o nome de maná; era como semente de coentro, branco e de sabor como bolos de mel.
32 Disse Moisés: Esta é a palavra que o Senhor ordenou: Dele encherás um gômer e o guardarás para as vossas gerações, para que vejam o pão com que vos sustentei no deserto, quando vos tirei do Egito.
33 Disse também Moisés a Arão: Toma um vaso, mete nele um gômer cheio de maná e coloca-o diante do Senhor, para guardar-se às vossas gerações.
34 Como o Senhor ordenara a Moisés, assim Arão o colocou diante do Testemunho para o guardar.
35 E comeram os filhos de Israel maná quarenta anos, até que entraram em terra habitada; comeram maná até que chegaram aos limites da terra de Canaã.
36 Gômer é a décima parte do efa.*
1 Tendo partido toda a congregação dos filhos de Israel do deserto de Sim, fazendo suas paradas, segundo o mandamento do Senhor, acamparam-se em Refidim; e não havia ali água para o povo beber.
2 Contendeu, pois, o povo com Moisés e disse: Dá-nos água para beber. Respondeu-lhes Moisés: Por que contendeis comigo? Por que tentais ao Senhor?
3 Tendo aí o povo sede de água, murmurou contra Moisés e disse: Por que nos fizeste subir do Egito, para nos matares de sede, a nós, a nossos filhos e aos nossos rebanhos?
4 Então, clamou Moisés ao Senhor: Que farei a este povo? Só lhe resta apedrejar-me.
5 Respondeu o Senhor a Moisés: Passa adiante do povo e toma contigo alguns dos anciãos de Israel, leva contigo em mão o bordão com que feriste o rio e vai.
6 Eis que estarei ali diante de ti sobre a rocha em Horebe; ferirás a rocha, e dela sairá água, e o povo beberá. Moisés assim o fez na presença dos anciãos de Israel.
7 E chamou o nome daquele lugar Massá e Meribá, por causa da contenda dos filhos de Israel e porque tentaram ao Senhor, dizendo: Está o Senhor no meio de nós ou não?
8 Então, veio Amaleque e pelejou contra Israel em Refidim.
9 Com isso, ordenou Moisés a Josué: Escolhe-nos homens, e sai, e peleja contra Amaleque; amanhã, estarei eu no cimo do outeiro, e o bordão de Deus estará na minha mão.
10 Fez Josué como Moisés lhe dissera e pelejou contra Amaleque; Moisés, porém, Arão e Hur subiram ao cimo do outeiro.
11 Quando Moisés levantava a mão, Israel prevalecia; quando, porém, ele abaixava a mão, prevalecia Amaleque.
12 Ora, as mãos de Moisés eram pesadas; por isso, tomaram uma pedra e a puseram por baixo dele, e ele nela se assentou; Arão e Hur sustentavam-lhe as mãos, um, de um lado, e o outro, do outro; assim lhe ficaram as mãos firmes até ao pôr do sol.
13 E Josué desbaratou a Amaleque e a seu povo a fio de espada.
14 Então, disse o Senhor a Moisés: Escreve isto para memória num livro e repete-o a Josué; porque eu hei de riscar totalmente a memória de Amaleque de debaixo do céu.
15 E Moisés edificou um altar e lhe chamou: O Senhor É Minha Bandeira.
16 E disse: Porquanto o Senhor jurou, haverá guerra do Senhor contra Amaleque de geração em geração.*
1 Ora, Jetro, sacerdote de Midiã, sogro de Moisés, ouviu todas as coisas que Deus tinha feito a Moisés e a Israel, seu povo; como o Senhor trouxera a Israel do Egito.
2 Jetro, sogro de Moisés, tomou a Zípora, mulher de Moisés, depois que este lha enviara,
3 com os dois filhos dela, dos quais um se chamava Gérson, pois disse Moisés: Fui peregrino em terra estrangeira;
4 e o outro, Eliézer, pois disse: O Deus de meu pai foi a minha ajuda e me livrou da espada de Faraó.
5 Veio Jetro, sogro de Moisés, com os filhos e a mulher deste, a Moisés no deserto onde se achava acampado, junto ao monte de Deus,
6 e mandou dizer a Moisés: Eu, teu sogro Jetro, venho a ti, com a tua mulher e seus dois filhos.
7 Então, saiu Moisés ao encontro do seu sogro, inclinou-se e o beijou; e, indagando pelo bem-estar um do outro, entraram na tenda.
8 Contou Moisés a seu sogro tudo o que o Senhor havia feito a Faraó e aos egípcios por amor de Israel, e todo o trabalho que passaram no Egito, e como o Senhor os livrara.
9 Alegrou-se Jetro de todo o bem que o Senhor fizera a Israel, livrando-o da mão dos egípcios,
10 e disse: Bendito seja o Senhor, que vos livrou da mão dos egípcios e da mão de Faraó;
11 agora, sei que o Senhor é maior que todos os deuses, porque livrou este povo de debaixo da mão dos egípcios, quando agiram arrogantemente contra o povo.
12 Então, Jetro, sogro de Moisés, tomou holocausto e sacrifícios para Deus; e veio Arão e todos os anciãos de Israel para comerem pão com o sogro de Moisés, diante de Deus.
13 No dia seguinte, assentou-se Moisés para julgar o povo; e o povo estava em pé diante de Moisés desde a manhã até ao pôr do sol.
14 Vendo, pois, o sogro de Moisés tudo o que ele fazia ao povo, disse: Que é isto que fazes ao povo? Por que te assentas só, e todo o povo está em pé diante de ti, desde a manhã até ao pôr do sol?
15 Respondeu Moisés a seu sogro: É porque o povo me vem a mim para consultar a Deus;
16 quando tem alguma questão, vem a mim, para que eu julgue entre um e outro e lhes declare os estatutos de Deus e as suas leis.
17 O sogro de Moisés, porém, lhe disse: Não é bom o que fazes.
18 Sem dúvida, desfalecerás, tanto tu como este povo que está contigo; pois isto é pesado demais para ti; tu só não o podes fazer.
19 Ouve, pois, as minhas palavras; eu te aconselharei, e Deus seja contigo; representa o povo perante Deus, leva as suas causas a Deus,
20 ensina-lhes os estatutos e as leis e faze-lhes saber o caminho em que devem andar e a obra que devem fazer.
21 Procura dentre o povo homens capazes, tementes a Deus, homens de verdade, que aborreçam a avareza; põe-nos sobre eles por chefes de mil, chefes de cem, chefes de cinquenta e chefes de dez;
22 para que julguem este povo em todo tempo. Toda causa grave trarão a ti, mas toda causa pequena eles mesmos julgarão; será assim mais fácil para ti, e eles levarão a carga contigo.
23 Se isto fizeres, e assim Deus to mandar, poderás, então, suportar; e assim também todo este povo tornará em paz ao seu lugar.
24 Moisés atendeu às palavras de seu sogro e fez tudo quanto este lhe dissera.
25 Escolheu Moisés homens capazes, de todo o Israel, e os constituiu por cabeças sobre o povo: chefes de mil, chefes de cem, chefes de cinquenta e chefes de dez.
26 Estes julgaram o povo em todo tempo; a causa grave trouxeram a Moisés e toda causa simples julgaram eles.
27 Então, se despediu Moisés de seu sogro, e este se foi para a sua terra.*
1 No terceiro mês da saída dos filhos de Israel da terra do Egito, no primeiro dia desse mês, vieram ao deserto do Sinai.
2 Tendo partido de Refidim, vieram ao deserto do Sinai, no qual se acamparam; ali, pois, se acampou Israel em frente do monte.
3 Subiu Moisés a Deus, e do monte o Senhor o chamou e lhe disse: Assim falarás à casa de Jacó e anunciarás aos filhos de Israel:
4 Tendes visto o que fiz aos egípcios, como vos levei sobre asas de águia e vos cheguei a mim.
5 Agora, pois, se diligentemente ouvirdes a minha voz e guardardes a minha aliança, então, sereis a minha propriedade peculiar dentre todos os povos; porque toda a terra é minha;
6 vós me sereis reino de sacerdotes e nação santa. São estas as palavras que falarás aos filhos de Israel.
7 Veio Moisés, chamou os anciãos do povo e expôs diante deles todas estas palavras que o Senhor lhe havia ordenado.
8 Então, o povo respondeu à uma: Tudo o que o Senhor falou faremos. E Moisés relatou ao Senhor as palavras do povo.
9 Disse o Senhor a Moisés: Eis que virei a ti numa nuvem escura, para que o povo ouça quando eu falar contigo e para que também creiam sempre em ti. Porque Moisés tinha anunciado as palavras do seu povo ao Senhor.
10 Disse também o Senhor a Moisés: Vai ao povo e purifica-o hoje e amanhã. Lavem eles as suas vestes
11 e estejam prontos para o terceiro dia; porque no terceiro dia o Senhor, à vista de todo o povo, descerá sobre o monte Sinai.
12 Marcarás em redor limites ao povo, dizendo: Guardai-vos de subir ao monte, nem toqueis o seu limite; todo aquele que tocar o monte será morto.
13 Mão nenhuma tocará neste, mas será apedrejado ou flechado; quer seja animal, quer seja homem, não viverá. Quando soar longamente a buzina, então, subirão ao monte.
14 Moisés, tendo descido do monte ao povo, consagrou o povo; e lavaram as suas vestes.
15 E disse ao povo: Estai prontos ao terceiro dia; e não vos chegueis a mulher.
16 Ao amanhecer do terceiro dia, houve trovões, e relâmpagos, e uma espessa nuvem sobre o monte, e mui forte clangor de trombeta, de maneira que todo o povo que estava no arraial se estremeceu.
17 E Moisés levou o povo fora do arraial ao encontro de Deus; e puseram-se ao pé do monte.
18 Todo o monte Sinai fumegava, porque o Senhor descera sobre ele em fogo; a sua fumaça subiu como fumaça de uma fornalha, e todo o monte tremia grandemente.
19 E o clangor da trombeta ia aumentando cada vez mais; Moisés falava, e Deus lhe respondia no trovão.
20 Descendo o Senhor para o cimo do monte Sinai, chamou o Senhor a Moisés para o cimo do monte. Moisés subiu,
21 e o Senhor disse a Moisés: Desce, adverte ao povo que não traspasse o limite até ao Senhor para vê-lo, a fim de muitos deles não perecerem.
22 Também os sacerdotes, que se chegam ao Senhor, se hão de consagrar, para que o Senhor não os fira.
23 Então, disse Moisés ao Senhor: O povo não poderá subir ao monte Sinai, porque tu nos advertiste, dizendo: Marca limites ao redor do monte e consagra-o.
24 Replicou-lhe o Senhor: Vai, desce; depois, subirás tu, e Arão contigo; os sacerdotes, porém, e o povo não traspassem o limite para subir ao Senhor, para que não os fira.
25 Desceu, pois, Moisés ao povo e lhe disse tudo isso.*
1 Então, falou Deus todas estas palavras:
2 Eu sou o Senhor, teu Deus, que te tirei da terra do Egito, da casa da servidão.
3 Não terás outros deuses diante de mim.
4 Não farás para ti imagem de escultura, nem semelhança alguma do que há em cima nos céus, nem embaixo na terra, nem nas águas debaixo da terra.
5 Não as adorarás, nem lhes darás culto; porque eu sou o Senhor, teu Deus, Deus zeloso, que visito a iniquidade dos pais nos filhos até à terceira e quarta geração daqueles que me aborrecem
6 e faço misericórdia até mil gerações daqueles que me amam e guardam os meus mandamentos.
7 Não tomarás o nome do Senhor, teu Deus, em vão, porque o Senhor não terá por inocente o que tomar o seu nome em vão.
8 Lembra-te do dia de sábado, para o santificar.
9 Seis dias trabalharás e farás toda a tua obra.
10 Mas o sétimo dia é o sábado do Senhor, teu Deus; não farás nenhum trabalho, nem tu, nem o teu filho, nem a tua filha, nem o teu servo, nem a tua serva, nem o teu animal, nem o forasteiro das tuas portas para dentro;
11 porque, em seis dias, fez o Senhor os céus e a terra, o mar e tudo o que neles há e, ao sétimo dia, descansou; por isso, o Senhor abençoou o dia de sábado e o santificou.
12 Honra teu pai e tua mãe, para que se prolonguem os teus dias na terra que o Senhor, teu Deus, te dá.
13 Não matarás.
14 Não adulterarás.
15 Não furtarás.
16 Não dirás falso testemunho contra o teu próximo.
17 Não cobiçarás a casa do teu próximo. Não cobiçarás a mulher do teu próximo, nem o seu servo, nem a sua serva, nem o seu boi, nem o seu jumento, nem coisa alguma que pertença ao teu próximo.
18 Todo o povo presenciou os trovões, e os relâmpagos, e o clangor da trombeta, e o monte fumegante; e o povo, observando, se estremeceu e ficou de longe.
19 Disseram a Moisés: Fala-nos tu, e te ouviremos; porém não fale Deus conosco, para que não morramos.
20 Respondeu Moisés ao povo: Não temais; Deus veio para vos provar e para que o seu temor esteja diante de vós, a fim de que não pequeis.
21 O povo estava de longe, em pé; Moisés, porém, se chegou à nuvem escura onde Deus estava.
22 Então, disse o Senhor a Moisés: Assim dirás aos filhos de Israel: Vistes que dos céus eu vos falei.
23 Não fareis deuses de prata ao lado de mim, nem deuses de ouro fareis para vós outros.
24 Um altar de terra me farás e sobre ele sacrificarás os teus holocaustos, as tuas ofertas pacíficas, as tuas ovelhas e os teus bois; em todo lugar onde eu fizer celebrar a memória do meu nome, virei a ti e te abençoarei.
25 Se me levantares um altar de pedras, não o farás de pedras lavradas; pois, se sobre ele manejares a tua ferramenta, profaná-lo-ás.
26 Nem subirás por degrau ao meu altar, para que a tua nudez não seja ali exposta.*
1 São estes os estatutos que lhes proporás:
2 Se comprares um escravo hebreu, seis anos servirá; mas, ao sétimo, sairá forro, de graça.
3 Se entrou solteiro, sozinho sairá; se era homem casado, com ele sairá sua mulher.
4 Se o seu senhor lhe der mulher, e ela der à luz filhos e filhas, a mulher e seus filhos serão do seu senhor, e ele sairá sozinho.
5 Porém, se o escravo expressamente disser: Eu amo meu senhor, minha mulher e meus filhos, não quero sair forro.
6 Então, o seu senhor o levará aos juízes, e o fará chegar à porta ou à ombreira, e o seu senhor lhe furará a orelha com uma sovela; e ele o servirá para sempre.
7 Se um homem vender sua filha para ser escrava, esta não lhe sairá como saem os escravos.
8 Se ela não agradar ao seu senhor, que se comprometeu a desposá-la, ele terá de permitir-lhe o resgate; não poderá vendê-la a um povo estranho, pois será isso deslealdade para com ela.
9 Mas, se a casar com seu filho, tratá-la-á como se tratam as filhas.
10 Se ele der ao filho outra mulher, não diminuirá o mantimento da primeira, nem os seus vestidos, nem os seus direitos conjugais.
11 Se não lhe fizer estas três coisas, ela sairá sem retribuição, nem pagamento em dinheiro.
12 Quem ferir a outro, de modo que este morra, também será morto.
13 Porém, se não lhe armou ciladas, mas Deus lhe permitiu caísse em suas mãos, então, te designarei um lugar para onde ele fugirá.
14 Se alguém vier maliciosamente contra o próximo, matando-o à traição, tirá-lo-ás até mesmo do meu altar, para que morra.
15 Quem ferir seu pai ou sua mãe será morto.
16 O que raptar alguém e o vender, ou for achado na sua mão, será morto.
17 Quem amaldiçoar seu pai ou sua mãe será morto.
18 Se dois brigarem, ferindo um ao outro com pedra ou com o punho, e o ferido não morrer, mas cair de cama;
19 se ele tornar a levantar-se e andar fora, apoiado ao seu bordão, então, será absolvido aquele que o feriu; somente lhe pagará o tempo que perdeu e o fará curar-se totalmente.
20 Se alguém ferir com bordão o seu escravo ou a sua escrava, e o ferido morrer debaixo da sua mão, será punido;
21 porém, se ele sobreviver por um ou dois dias, não será punido, porque é dinheiro seu.
22 Se homens brigarem, e ferirem mulher grávida, e forem causa de que aborte, porém sem maior dano, aquele que feriu será obrigado a indenizar segundo o que lhe exigir o marido da mulher; e pagará como os juízes lhe determinarem.
23 Mas, se houver dano grave, então, darás vida por vida,
24 olho por olho, dente por dente, mão por mão, pé por pé,
25 queimadura por queimadura, ferimento por ferimento, golpe por golpe.
26 Se alguém ferir o olho do seu escravo ou o olho da sua escrava e o inutilizar, deixá-lo-á ir forro pelo seu olho.
27 E, se com violência fizer cair um dente do seu escravo ou da sua escrava, deixá-lo-á ir forro pelo seu dente.
28 Se algum boi chifrar homem ou mulher, que morra, o boi será apedrejado, e não lhe comerão a carne; mas o dono do boi será absolvido.
29 Mas, se o boi, dantes, era dado a chifrar, e o seu dono era disso conhecedor e não o prendeu, e o boi matar homem ou mulher, o boi será apedrejado, e também será morto o seu dono.
30 Se lhe for exigido resgate, dará, então, como resgate da sua vida tudo o que lhe for exigido.
31 Quer tenha chifrado um filho, quer tenha chifrado uma filha, este julgamento lhe será aplicado.
32 Se o boi chifrar um escravo ou uma escrava, dar-se-ão trinta siclos de prata ao senhor destes, e o boi será apedrejado.
33 Se alguém deixar aberta uma cova ou se alguém cavar uma cova e não a tapar, e nela cair boi ou jumento,
34 o dono da cova o pagará, pagará dinheiro ao seu dono, mas o animal morto será seu.
35 Se um boi de um homem ferir o boi de outro, e o boi ferido morrer, venderão o boi vivo e repartirão o valor; e dividirão entre si o boi morto.
36 Mas, se for notório que o boi era já, dantes, chifrador, e o seu dono não o prendeu, certamente, pagará boi por boi; porém o morto será seu.*
1 Se alguém furtar boi ou ovelha e o abater ou vender, por um boi pagará cinco bois, e quatro ovelhas por uma ovelha.
2 Se um ladrão for achado arrombando uma casa e, sendo ferido, morrer, quem o feriu não será culpado do sangue.
3 Se, porém, já havia sol quando tal se deu, quem o feriu será culpado do sangue; neste caso, o ladrão fará restituição total. Se não tiver com que pagar, será vendido por seu furto.
4 Se aquilo que roubou for achado vivo em seu poder, seja boi, jumento ou ovelha, pagará o dobro.
5 Se alguém fizer pastar o seu animal num campo ou numa vinha e o largar para comer em campo de outrem, pagará com o melhor do seu próprio campo e o melhor da sua própria vinha.
6 Se irromper fogo, e pegar nos espinheiros, e destruir as medas de cereais, ou a messe, ou o campo, aquele que acendeu o fogo pagará totalmente o queimado.
7 Se alguém der ao seu próximo dinheiro ou objetos a guardar, e isso for furtado àquele que o recebeu, se for achado o ladrão, este pagará o dobro.
8 Se o ladrão não for achado, então, o dono da casa será levado perante os juízes, a ver se não meteu a mão nos bens do próximo.
9 Em todo negócio frauduloso, seja a respeito de boi, ou de jumento, ou de ovelhas, ou de roupas, ou de qualquer coisa perdida, de que uma das partes diz: Esta é a coisa, a causa de ambas as partes se levará perante os juízes; aquele a quem os juízes condenarem pagará o dobro ao seu próximo.
10 Se alguém der ao seu próximo a guardar jumento, ou boi, ou ovelha, ou outro animal qualquer, e este morrer, ou ficar aleijado, ou for afugentado, sem que ninguém o veja,
11 então, haverá juramento do Senhor entre ambos, de que não meteu a mão nos bens do seu próximo; o dono aceitará o juramento, e o outro não fará restituição.
12 Porém, se, de fato, lhe for furtado, pagá-lo-á ao seu dono.
13 Se for dilacerado, trá-lo-á em testemunho disso e não pagará o dilacerado.
14 Se alguém pedir emprestado a seu próximo um animal, e este ficar aleijado ou morrer, não estando presente o dono, pagá-lo-á.
15 Se o dono esteve presente, não o pagará; se foi alugado, o preço do aluguel será o pagamento.
16 Se alguém seduzir qualquer virgem que não estava desposada e se deitar com ela, pagará seu dote e a tomará por mulher.
17 Se o pai dela definitivamente recusar dar-lha, pagará ele em dinheiro conforme o dote das virgens.
18 A feiticeira não deixarás viver.
19 Quem tiver coito com animal será morto.
20 Quem sacrificar aos deuses e não somente ao Senhor será destruído.
21 Não afligirás o forasteiro, nem o oprimirás; pois forasteiros fostes na terra do Egito.
22 A nenhuma viúva nem órfão afligireis.
23 Se de algum modo os afligirdes, e eles clamarem a mim, eu lhes ouvirei o clamor;
24 a minha ira se acenderá, e vos matarei à espada; vossas mulheres ficarão viúvas, e vossos filhos, órfãos.
25 Se emprestares dinheiro ao meu povo, ao pobre que está contigo, não te haverás com ele como credor que impõe juros.
26 Se do teu próximo tomares em penhor a sua veste, lha restituirás antes do pôr do sol;
27 porque é com ela que se cobre, é a veste do seu corpo; em que se deitaria? Será, pois, que, quando clamar a mim, eu o ouvirei, porque sou misericordioso.
28 Contra Deus não blasfemarás, nem amaldiçoarás o príncipe do teu povo.
29 Não tardarás em trazer ofertas do melhor das tuas ceifas e das tuas vinhas; o primogênito de teus filhos me darás.
30 Da mesma sorte, farás com os teus bois e com as tuas ovelhas; sete dias ficará a cria com a mãe, e, ao oitavo dia, ma darás.
31 Ser-me-eis homens consagrados; portanto, não comereis carne dilacerada no campo; deitá-la-eis aos cães.*
1 Não espalharás notícias falsas, nem darás mão ao ímpio, para seres testemunha maldosa.
2 Não seguirás a multidão para fazeres mal; nem deporás, numa demanda, inclinando-te para a maioria, para torcer o direito.
3 Nem com o pobre serás parcial na sua demanda.
4 Se encontrares desgarrado o boi do teu inimigo ou o seu jumento, lho reconduzirás.
5 Se vires prostrado debaixo da sua carga o jumento daquele que te aborrece, não o abandonarás, mas ajudá-lo-ás a erguê-lo.
6 Não perverterás o julgamento do teu pobre na sua causa.
7 Da falsa acusação te afastarás; não matarás o inocente e o justo, porque não justificarei o ímpio.
8 Também suborno não aceitarás, porque o suborno cega até o perspicaz e perverte as palavras dos justos.
9 Também não oprimirás o forasteiro; pois vós conheceis o coração do forasteiro, visto que fostes forasteiros na terra do Egito.
10 Seis anos semearás a tua terra e recolherás os seus frutos;
11 porém, no sétimo ano, a deixarás descansar e não a cultivarás, para que os pobres do teu povo achem o que comer, e do sobejo comam os animais do campo. Assim farás com a tua vinha e com o teu olival.
12 Seis dias farás a tua obra, mas, ao sétimo dia, descansarás; para que descanse o teu boi e o teu jumento; e para que tome alento o filho da tua serva e o forasteiro.
13 Em tudo o que vos tenho dito, andai apercebidos; do nome de outros deuses nem vos lembreis, nem se ouça de vossa boca.
14 Três vezes no ano me celebrareis festa.
15 Guardarás a Festa dos Pães Asmos; sete dias comerás pães asmos, como te ordenei, ao tempo apontado no mês de abibe, porque nele saíste do Egito; ninguém apareça de mãos vazias perante mim.
16 Guardarás a Festa da Sega, dos primeiros frutos do teu trabalho, que houveres semeado no campo, e a Festa da Colheita, à saída do ano, quando recolheres do campo o fruto do teu trabalho.
17 Três vezes no ano, todo homem aparecerá diante do Senhor Deus.
18 Não oferecerás o sangue do meu sacrifício com pão levedado, nem ficará gordura da minha festa durante a noite até pela manhã.
19 As primícias dos frutos da tua terra trarás à Casa do Senhor, teu Deus. Não cozerás o cabrito no leite da sua própria mãe.
20 Eis que eu envio um Anjo adiante de ti, para que te guarde pelo caminho e te leve ao lugar que tenho preparado.
21 Guarda-te diante dele, e ouve a sua voz, e não te rebeles contra ele, porque não perdoará a vossa transgressão; pois nele está o meu nome.
22 Mas, se diligentemente lhe ouvires a voz e fizeres tudo o que eu disser, então, serei inimigo dos teus inimigos e adversário dos teus adversários.
23 Porque o meu Anjo irá adiante de ti e te levará aos amorreus, aos heteus, aos ferezeus, aos cananeus, aos heveus e aos jebuseus; e eu os destruirei.
24 Não adorarás os seus deuses, nem lhes darás culto, nem farás conforme as suas obras; antes, os destruirás totalmente e despedaçarás de todo as suas colunas.
25 Servireis ao Senhor, vosso Deus, e ele abençoará o vosso pão e a vossa água; e tirará do vosso meio as enfermidades.
26 Na tua terra, não haverá mulher que aborte, nem estéril; completarei o número dos teus dias.
27 Enviarei o meu terror diante de ti, confundindo a todo povo onde entrares; farei que todos os teus inimigos te voltem as costas.
28 Também enviarei vespas diante de ti, que lancem os heveus, os cananeus e os heteus de diante de ti.
29 Não os lançarei de diante de ti num só ano, para que a terra se não torne em desolação, e as feras do campo se não multipliquem contra ti.
30 Pouco a pouco, os lançarei de diante de ti, até que te multipliques e possuas a terra por herança.
31 Porei os teus limites desde o mar Vermelho até ao mar dos filisteus e desde o deserto até ao Eufrates; porque darei nas tuas mãos os moradores da terra, para que os lances de diante de ti.
32 Não farás aliança nenhuma com eles, nem com os seus deuses.
33 Eles não habitarão na tua terra, para que te não façam pecar contra mim; se servires aos seus deuses, isso te será cilada.*
1 Disse também Deus a Moisés: Sobe ao Senhor, tu, e Arão, e Nadabe, e Abiú, e setenta dos anciãos de Israel; e adorai de longe.
2 Só Moisés se chegará ao Senhor; os outros não se chegarão, nem o povo subirá com ele.
3 Veio, pois, Moisés e referiu ao povo todas as palavras do Senhor e todos os estatutos; então, todo o povo respondeu a uma voz e disse: Tudo o que falou o Senhor faremos.
4 Moisés escreveu todas as palavras do Senhor e, tendo-se levantado pela manhã de madrugada, erigiu um altar ao pé do monte e doze colunas, segundo as doze tribos de Israel.
5 E enviou alguns jovens dos filhos de Israel, os quais ofereceram ao Senhor holocaustos e sacrifícios pacíficos de novilhos.
6 Moisés tomou metade do sangue e o pôs em bacias; e a outra metade aspergiu sobre o altar.
7 E tomou o livro da aliança e o leu ao povo; e eles disseram: Tudo o que falou o Senhor faremos e obedeceremos.
8 Então, tomou Moisés aquele sangue, e o aspergiu sobre o povo, e disse: Eis aqui o sangue da aliança que o Senhor fez convosco a respeito de todas estas palavras.
9 E subiram Moisés, e Arão, e Nadabe, e Abiú, e setenta dos anciãos de Israel.
10 E viram o Deus de Israel, sob cujos pés havia uma como pavimentação de pedra de safira, que se parecia com o céu na sua claridade.
11 Ele não estendeu a mão sobre os escolhidos dos filhos de Israel; porém eles viram a Deus, e comeram, e beberam.
12 Então, disse o Senhor a Moisés: Sobe a mim, ao monte, e fica lá; dar-te-ei tábuas de pedra, e a lei, e os mandamentos que escrevi, para os ensinares.
13 Levantou-se Moisés com Josué, seu servidor; e, subindo Moisés ao monte de Deus,
14 disse aos anciãos: Esperai-nos aqui até que voltemos a vós outros. Eis que Arão e Hur ficam convosco; quem tiver alguma questão se chegará a eles.
15 Tendo Moisés subido, uma nuvem cobriu o monte.
16 E a glória do Senhor pousou sobre o monte Sinai, e a nuvem o cobriu por seis dias; ao sétimo dia, do meio da nuvem chamou o Senhor a Moisés.
17 O aspecto da glória do Senhor era como um fogo consumidor no cimo do monte, aos olhos dos filhos de Israel.
18 E Moisés, entrando pelo meio da nuvem, subiu ao monte; e lá permaneceu quarenta dias e quarenta noites.*
1 Disse o Senhor a Moisés:
2 Fala aos filhos de Israel que me tragam oferta; de todo homem cujo coração o mover para isso, dele recebereis a minha oferta.
3 Esta é a oferta que dele recebereis: ouro, e prata, e bronze,
4 e estofo azul, e púrpura, e carmesim, e linho fino, e pelos de cabra,
5 e peles de carneiro tintas de vermelho, e peles finas, e madeira de acácia,
6 azeite para a luz, especiarias para o óleo de unção e para o incenso aromático,
7 pedras de ônix e pedras de engaste, para a estola sacerdotal e para o peitoral.
8 E me farão um santuário, para que eu possa habitar no meio deles.
9 Segundo tudo o que eu te mostrar para modelo do tabernáculo e para modelo de todos os seus móveis, assim mesmo o fareis.
10 Também farão uma arca de madeira de acácia; de dois côvados e meio será o seu comprimento, de um côvado e meio, a largura, e de um côvado e meio, a altura.
11 De ouro puro a cobrirás; por dentro e por fora a cobrirás e farás sobre ela uma bordadura de ouro ao redor.
12 Fundirás para ela quatro argolas de ouro e as porás nos quatro cantos da arca: duas argolas num lado dela e duas argolas noutro lado.
13 Farás também varais de madeira de acácia e os cobrirás de ouro;
14 meterás os varais nas argolas aos lados da arca, para se levar por meio deles a arca.
15 Os varais ficarão nas argolas da arca e não se tirarão dela.
16 E porás na arca o Testemunho, que eu te darei.
17 Farás também um propiciatório de ouro puro; de dois côvados e meio será o seu comprimento, e a largura, de um côvado e meio.
18 Farás dois querubins de ouro; de ouro batido os farás, nas duas extremidades do propiciatório;
19 um querubim, na extremidade de uma parte, e o outro, na extremidade da outra parte; de uma só peça com o propiciatório fareis os querubins nas duas extremidades dele.
20 Os querubins estenderão as asas por cima, cobrindo com elas o propiciatório; estarão eles de faces voltadas uma para a outra, olhando para o propiciatório.
21 Porás o propiciatório em cima da arca; e dentro dela porás o Testemunho, que eu te darei.
22 Ali, virei a ti e, de cima do propiciatório, do meio dos dois querubins que estão sobre a arca do Testemunho, falarei contigo acerca de tudo o que eu te ordenar para os filhos de Israel.
23 Também farás a mesa de madeira de acácia; terá o comprimento de dois côvados, a largura, de um côvado, e a altura, de um côvado e meio;
24 de ouro puro a cobrirás e lhe farás uma bordadura de ouro ao redor.
25 Também lhe farás moldura ao redor, da largura de quatro dedos, e lhe farás uma bordadura de ouro ao redor da moldura.
26 Também lhe farás quatro argolas de ouro; e porás as argolas nos quatro cantos, que estão nos seus quatro pés.
27 Perto da moldura estarão as argolas, como lugares para os varais, para se levar a mesa.
28 Farás, pois, estes varais de madeira de acácia e os cobrirás de ouro; por meio deles, se levará a mesa.
29 Também farás os seus pratos, e os seus recipientes para incenso, e as suas galhetas, e as suas taças em que se hão de oferecer libações; de ouro puro os farás.
30 Porás sobre a mesa os pães da proposição diante de mim perpetuamente.
31 Farás também um candelabro de ouro puro; de ouro batido se fará este candelabro; o seu pedestal, a sua hástea, os seus cálices, as suas maçanetas e as suas flores formarão com ele uma só peça.
32 Seis hásteas sairão dos seus lados: três de um lado e três do outro.
33 Numa hástea, haverá três cálices com formato de amêndoas, uma maçaneta e uma flor; e três cálices, com formato de amêndoas na outra hástea, uma maçaneta e uma flor; assim serão as seis hásteas que saem do candelabro.
34 Mas no candelabro mesmo haverá quatro cálices com formato de amêndoas, com suas maçanetas e com suas flores.
35 Haverá uma maçaneta sob duas hásteas que saem dele; e ainda uma maçaneta sob duas outras hásteas que saem dele; e ainda mais uma maçaneta sob duas outras hásteas que saem dele; assim se fará com as seis hásteas que saem do candelabro.
36 As suas maçanetas e as suas hásteas serão do mesmo; tudo será de uma só peça, obra batida de ouro puro.
37 Também lhe farás sete lâmpadas, as quais se acenderão para alumiar defronte dele.
38 As suas espevitadeiras e os seus apagadores serão de ouro puro.
39 De um talento de ouro puro se fará o candelabro com todos estes utensílios.
40 Vê, pois, que tudo faças segundo o modelo que te foi mostrado no monte.*
1 Farás o tabernáculo, que terá dez cortinas, de linho retorcido, estofo azul, púrpura e carmesim; com querubins, as farás de obra de artista.
2 O comprimento de cada cortina será de vinte e oito côvados, e a largura, de quatro côvados; todas as cortinas serão de igual medida.
3 Cinco cortinas serão ligadas umas às outras; e as outras cinco também ligadas umas às outras.
4 Farás laçadas de estofo azul na orla da cortina extrema do primeiro agrupamento; e de igual modo farás na orla da cortina extrema do segundo agrupamento.
5 Cinquenta laçadas farás numa cortina, e cinquenta, na outra cortina no extremo do segundo agrupamento; as laçadas serão contrapostas uma à outra.
6 Farás cinquenta colchetes de ouro, com os quais prenderás as cortinas uma à outra; e o tabernáculo passará a ser um todo.
7 Farás também de pelos de cabra cortinas para servirem de tenda sobre o tabernáculo; onze cortinas farás.
8 O comprimento de cada cortina será de trinta côvados, e a largura, de quatro côvados; as onze cortinas serão de igual medida.
9 Ajuntarás à parte cinco cortinas entre si, e de igual modo as seis restantes, a sexta das quais dobrarás na parte dianteira da tenda.
10 Farás cinquenta laçadas na orla da cortina extrema do primeiro agrupamento e cinquenta laçadas na orla da cortina extrema do segundo agrupamento.
11 Farás também cinquenta colchetes de bronze, e meterás os colchetes nas laçadas, e ajuntarás a tenda, para que venha a ser um todo.
12 A parte que restar das cortinas da tenda, a saber, a meia cortina que sobrar, penderá às costas do tabernáculo.
13 O côvado de um lado e o côvado de outro lado, do que sobejar no comprimento das cortinas da tenda, penderão de um e de outro lado do tabernáculo para o cobrir.
14 Também farás de peles de carneiro tintas de vermelho uma coberta para a tenda e outra coberta de peles finas.
15 Farás também de madeira de acácia as tábuas para o tabernáculo, as quais serão colocadas verticalmente.
16 Cada uma das tábuas terá dez côvados de comprimento e côvado e meio de largura.
17 Cada tábua terá dois encaixes, travados um com o outro; assim farás com todas as tábuas do tabernáculo.
18 No preparar as tábuas para o tabernáculo, farás vinte delas para o lado sul.
19 Farás também quarenta bases de prata debaixo das vinte tábuas: duas bases debaixo de uma tábua para os seus dois encaixes e duas bases debaixo de outra tábua para os seus dois encaixes.
20 Também haverá vinte tábuas ao outro lado do tabernáculo, para o lado norte,
21 com as suas quarenta bases de prata: duas bases debaixo de uma tábua e duas bases debaixo de outra tábua;
22 ao lado posterior do tabernáculo para o ocidente, farás seis tábuas.
23 Farás também duas tábuas para os cantos do tabernáculo, na parte posterior;
24 as quais, por baixo, estarão separadas, mas, em cima, se ajustarão à primeira argola; assim se fará com as duas tábuas; serão duas para cada um dos dois cantos.
25 Assim serão as oito tábuas com as suas bases de prata, dezesseis bases: duas bases debaixo de uma tábua e duas debaixo de outra tábua.
26 Farás travessas de madeira de acácia; cinco para as tábuas de um lado do tabernáculo,
27 cinco para as tábuas do outro lado do tabernáculo e cinco para as tábuas do tabernáculo ao lado posterior que olha para o ocidente.
28 A travessa do meio passará ao meio das tábuas de uma extremidade à outra.
29 Cobrirás de ouro as tábuas e de ouro farás as suas argolas, pelas quais hão de passar as travessas; e cobrirás também de ouro as travessas.
30 Levantarás o tabernáculo segundo o modelo que te foi mostrado no monte.
31 Farás também um véu de estofo azul, e púrpura, e carmesim, e linho fino retorcido; com querubins, o farás de obra de artista.
32 Suspendê-lo-ás sobre quatro colunas de madeira de acácia, cobertas de ouro; os seus colchetes serão de ouro, sobre quatro bases de prata.
33 Pendurarás o véu debaixo dos colchetes e trarás para lá a arca do Testemunho, para dentro do véu; o véu vos fará separação entre o Santo Lugar e o Santo dos Santos.
34 Porás a coberta do propiciatório sobre a arca do Testemunho no Santo dos Santos.
35 A mesa porás fora do véu e o candelabro, defronte da mesa, ao lado do tabernáculo, para o sul; e a mesa porás para o lado norte.
36 Farás também para a porta da tenda um reposteiro de estofo azul, e púrpura, e carmesim, e linho fino retorcido, obra de bordador.
37 Para este reposteiro farás cinco colunas de madeira de acácia e as cobrirás de ouro; os seus colchetes serão de ouro, e para elas fundirás cinco bases de bronze.*
1 Farás também o altar de madeira de acácia; de cinco côvados será o seu comprimento, e de cinco, a largura (será quadrado o altar), e de três côvados, a altura.
2 Dos quatro cantos farás levantar-se quatro chifres, os quais formarão uma só peça com o altar; e o cobrirás de bronze.
3 Far-lhe-ás também recipientes para recolher a sua cinza, e pás, e bacias, e garfos, e braseiros; todos esses utensílios farás de bronze.
4 Far-lhe-ás também uma grelha de bronze em forma de rede, à qual farás quatro argolas de metal nos seus quatro cantos,
5 e as porás dentro do rebordo do altar para baixo, de maneira que a rede chegue até ao meio do altar.
6 Farás também varais para o altar, varais de madeira de acácia, e os cobrirás de bronze.
7 Os varais se meterão nas argolas, de um e de outro lado do altar, quando for levado.
8 Oco e de tábuas o farás; como se te mostrou no monte, assim o farão.
9 Farás também o átrio do tabernáculo; ao lado meridional (que dá para o sul), o átrio terá cortinas de linho fino retorcido; o comprimento de cada lado será de cem côvados.
10 Também as suas vinte colunas e as suas vinte bases serão de bronze; os ganchos das colunas e as suas vergas serão de prata.
11 De igual modo, para o lado norte ao comprido, haverá cortinas de cem côvados de comprimento; e as suas vinte colunas e as suas vinte bases serão de bronze; os ganchos das colunas e as suas vergas serão de prata.
12 Na largura do átrio para o lado do ocidente, haverá cortinas de cinquenta côvados; as colunas serão dez, e as suas bases, dez.
13 A largura do átrio do lado oriental (para o levante) será de cinquenta côvados.
14 As cortinas para um lado da entrada serão de quinze côvados; as suas colunas serão três, e as suas bases, três.
15 Para o outro lado da entrada, haverá cortinas de quinze côvados; as suas colunas serão três, e as suas bases, três.
16 À porta do átrio, haverá um reposteiro de vinte côvados, de estofo azul, e púrpura, e carmesim, e linho fino retorcido, obra de bordador; as suas colunas serão quatro, e as suas bases, quatro.
17 Todas as colunas ao redor do átrio serão cingidas de vergas de prata; os seus ganchos serão de prata, mas as suas bases, de bronze.
18 O átrio terá cem côvados de comprimento, e cinquenta de largura por todo o lado, e cinco de altura; as suas cortinas serão de linho fino retorcido, e as suas bases, de bronze.
19 Todos os utensílios do tabernáculo em todo o seu serviço, e todas as suas estacas, e todas as estacas do átrio serão de bronze.
20 Ordenarás aos filhos de Israel que te tragam azeite puro de oliveira, batido, para o candelabro, para que haja lâmpada acesa continuamente.
21 Na tenda da congregação fora do véu, que está diante do Testemunho, Arão e seus filhos a conservarão em ordem, desde a tarde até pela manhã, perante o Senhor; estatuto perpétuo será este a favor dos filhos de Israel pelas suas gerações.
Almeida Revista e Atualizada© Copyright © 1993 Sociedade Bíblica do Brasil. Todos os direitos reservados. Texto bíblico utilizado com autori*
1 Faze também vir para junto de ti Arão, teu irmão, e seus filhos com ele, dentre os filhos de Israel, para me oficiarem como sacerdotes, a saber, Arão e seus filhos Nadabe, Abiú, Eleazar e Itamar.
2 Farás vestes sagradas para Arão, teu irmão, para glória e ornamento.
3 Falarás também a todos os homens hábeis a quem enchi do espírito de sabedoria, que façam vestes para Arão para consagrá-lo, para que me ministre o ofício sacerdotal.
4 As vestes, pois, que farão são estas: um peitoral, uma estola sacerdotal, uma sobrepeliz, uma túnica bordada, mitra e cinto. Farão vestes sagradas para Arão, teu irmão, e para seus filhos, para me oficiarem como sacerdotes.
5 Tomarão ouro, estofo azul, púrpura, carmesim e linho fino
6 e farão a estola sacerdotal de ouro, e estofo azul, e púrpura, e carmesim, e linho fino retorcido, obra esmerada.
7 Terá duas ombreiras que se unam às suas duas extremidades, e assim se unirá.
8 E o cinto de obra esmerada, que estará sobre a estola sacerdotal, será de obra igual, da mesma obra de ouro, e estofo azul, e púrpura, e carmesim, e linho fino retorcido.
9 Tomarás duas pedras de ônix e gravarás nelas os nomes dos filhos de Israel:
10 seis de seus nomes numa pedra e os outros seis na outra pedra, segundo a ordem do seu nascimento.
11 Conforme a obra de lapidador, como lavores de sinete, gravarás as duas pedras com os nomes dos filhos de Israel; engastadas ao redor de ouro, as farás.
12 E porás as duas pedras nas ombreiras da estola sacerdotal, por pedras de memória aos filhos de Israel; e Arão levará os seus nomes sobre ambos os seus ombros, para memória diante do Senhor.
13 Farás também engastes de ouro
14 e duas correntes de ouro puro; obra de fieira as farás; e as correntes de fieira prenderás nos engastes.
15 Farás também o peitoral do juízo de obra esmerada, conforme a obra da estola sacerdotal o farás: de ouro, e estofo azul, e púrpura, e carmesim, e linho fino retorcido o farás.
16 Quadrado e duplo, será de um palmo o seu comprimento, e de um palmo, a sua largura.
17 Colocarás nele engaste de pedras, com quatro ordens de pedras: a ordem de sárdio, topázio e carbúnculo será a primeira ordem;
18 a segunda ordem será de esmeralda, safira e diamante;
19 a terceira ordem será de jacinto, ágata e ametista;
20 a quarta ordem será de berilo, ônix e jaspe; elas serão guarnecidas de ouro nos seus engastes.
21 As pedras serão conforme os nomes dos filhos de Israel, doze, segundo os seus nomes; serão esculpidas como sinetes, cada uma com o seu nome, para as doze tribos.
22 Para o peitoral farás correntes como cordas, de obra trançada de ouro puro.
23 Também farás para o peitoral duas argolas de ouro e porás as duas argolas nas extremidades do peitoral.
24 Então, meterás as duas correntes de ouro nas duas argolas, nas extremidades do peitoral.
25 As duas pontas das correntes prenderás nos dois engastes e as porás nas ombreiras da estola sacerdotal na frente dele.
26 Farás também duas argolas de ouro e as porás nas duas extremidades do peitoral, na sua orla interior junto à estola sacerdotal.
27 Farás também duas argolas de ouro e as porás nas duas ombreiras da estola sacerdotal, abaixo, na frente dele, perto da sua juntura, sobre o cinto de obra esmerada da estola sacerdotal.
28 E ligarão o peitoral com as suas argolas às argolas da estola sacerdotal por cima com uma fita azul, para que esteja sobre o cinto da estola sacerdotal; e nunca o peitoral se separará da estola sacerdotal.
29 Assim, Arão levará os nomes dos filhos de Israel no peitoral do juízo sobre o seu coração, quando entrar no santuário, para memória diante do Senhor continuamente.
30 Também porás no peitoral do juízo o Urim e o Tumim, para que estejam sobre o coração de Arão, quando entrar perante o Senhor; assim, Arão levará o juízo dos filhos de Israel sobre o seu coração diante do Senhor continuamente.
31 Farás também a sobrepeliz da estola sacerdotal toda de estofo azul.
32 No meio dela, haverá uma abertura para a cabeça; será debruada essa abertura, como a abertura de uma saia de malha, para que não se rompa.
33 Em toda a orla da sobrepeliz, farás romãs de estofo azul, e púrpura, e carmesim; e campainhas de ouro no meio delas.
34 Haverá em toda a orla da sobrepeliz uma campainha de ouro e uma romã, outra campainha de ouro e outra romã.
35 Esta sobrepeliz estará sobre Arão quando ministrar, para que se ouça o seu sonido, quando entrar no santuário diante do Senhor e quando sair; e isso para que não morra.
36 Farás também uma lâmina de ouro puro e nela gravarás à maneira de gravuras de sinetes: Santidade ao Senhor.
37 Atá-la-ás com um cordão de estofo azul, de maneira que esteja na mitra; bem na frente da mitra estará.
38 E estará sobre a testa de Arão, para que Arão leve a iniquidade concernente às coisas santas que os filhos de Israel consagrarem em todas as ofertas de suas coisas santas; sempre estará sobre a testa de Arão, para que eles sejam aceitos perante o Senhor.
39 Tecerás, quadriculada, a túnica de linho fino e farás uma mitra de linho fino e um cinto de obra de bordador.
40 Para os filhos de Arão farás túnicas, e cintos, e tiaras; fá-los-ás para glória e ornamento.
41 E, com isso, vestirás Arão, teu irmão, bem como seus filhos; e os ungirás, e consagrarás, e santificarás, para que me oficiem como sacerdotes.
42 Faze-lhes também calções de linho, para cobrirem a pele nua; irão da cintura às coxas.
43 E estarão sobre Arão e sobre seus filhos, quando entrarem na tenda da congregação ou quando se chegarem ao altar para ministrar no santuário, para que não levem iniquidade e morram; isto será estatuto perpétuo para ele e para sua posteridade depois dele.*
1 Isto é o que lhes farás, para os consagrar, a fim de que me oficiem como sacerdotes: toma um novilho, e dois carneiros sem defeito,
2 e pães asmos, e bolos asmos, amassados com azeite, e obreias asmas untadas com azeite; de flor de farinha de trigo os farás,
3 e os porás num cesto, e no cesto os trarás; trarás também o novilho e os dois carneiros.
4 Então, farás que Arão e seus filhos se cheguem à porta da tenda da congregação e os lavarás com água;
5 depois, tomarás as vestes, e vestirás Arão da túnica, da sobrepeliz, da estola sacerdotal e do peitoral, e o cingirás com o cinto de obra esmerada da estola sacerdotal;
6 pôr-lhe-ás a mitra na cabeça e sobre a mitra, a coroa sagrada.
7 Então, tomarás o óleo da unção e lho derramarás sobre a cabeça; assim o ungirás.
8 Farás, depois, que se cheguem os filhos de Arão, e os vestirás de túnicas,
9 e os cingirás com o cinto, Arão e seus filhos, e lhes atarás as tiaras, para que tenham o sacerdócio por estatuto perpétuo, e consagrarás Arão e seus filhos.
10 Farás chegar o novilho diante da tenda da congregação, e Arão e seus filhos porão as mãos sobre a cabeça dele.
11 Imolarás o novilho perante o Senhor, à porta da tenda da congregação.
12 Depois, tomarás do sangue do novilho e o porás com o teu dedo sobre os chifres do altar; o restante do sangue derramá-lo-ás à base do altar.
13 Também tomarás toda a gordura que cobre as entranhas, o redenho do fígado, os dois rins e a gordura que está neles e queimá-los-ás sobre o altar;
14 mas a carne do novilho, a pele e os excrementos, queimá-los-ás fora do arraial; é sacrifício pelo pecado.
15 Depois, tomarás um carneiro, e Arão e seus filhos porão as mãos sobre a cabeça dele.
16 Imolarás o carneiro, e tomarás o seu sangue, e o jogarás sobre o altar ao redor;
17 partirás o carneiro em seus pedaços e, lavadas as entranhas e as pernas, pô-las-ás sobre os pedaços e sobre a cabeça.
18 Assim, queimarás todo o carneiro sobre o altar; é holocausto para o Senhor, de aroma agradável, oferta queimada ao Senhor.
19 Depois, tomarás o outro carneiro, e Arão e seus filhos porão as mãos sobre a cabeça dele.
20 Imolarás o carneiro, e tomarás do seu sangue, e o porás sobre a ponta da orelha direita de Arão e sobre a ponta da orelha direita de seus filhos, como também sobre o polegar da sua mão direita e sobre o polegar do seu pé direito; o restante do sangue jogarás sobre o altar ao redor.
21 Tomarás, então, do sangue sobre o altar e do óleo da unção e os aspergirás sobre Arão e suas vestes e sobre seus filhos e as vestes de seus filhos com ele; para que ele seja santificado, e as suas vestes, e também seus filhos e as vestes de seus filhos com ele.
22 Depois, tomarás do carneiro a gordura, a cauda gorda, a gordura que cobre as entranhas, o redenho do fígado, os dois rins, a gordura que está neles e a coxa direita, porque é carneiro da consagração;
23 e também um pão, um bolo de pão azeitado e uma obreia do cesto dos pães asmos que estão diante do Senhor.
24 Todas estas coisas porás nas mãos de Arão e nas de seus filhos e, movendo-as de um lado para outro, as oferecerás como ofertas movidas perante o Senhor.
25 Depois, as tomarás das suas mãos e as queimarás sobre o altar; é holocausto para o Senhor, de agradável aroma, oferta queimada ao Senhor.
26 Tomarás o peito do carneiro da consagração, que é de Arão, e, movendo-o de um lado para outro, o oferecerás como oferta movida perante o Senhor; e isto será a tua porção.
27 Consagrarás o peito da oferta movida e a coxa da porção que foi movida, a qual se tirou do carneiro da consagração, que é de Arão e de seus filhos.
28 Isto será a obrigação perpétua dos filhos de Israel, devida a Arão e seus filhos, por ser a porção do sacerdote, oferecida, da parte dos filhos de Israel, dos sacrifícios pacíficos; é a sua oferta ao Senhor.
29 As vestes santas de Arão passarão a seus filhos depois dele, para serem ungidos nelas e consagrados nelas.
30 Sete dias as vestirá o filho que for sacerdote em seu lugar, quando entrar na tenda da congregação para ministrar no santuário.
31 Tomarás o carneiro da consagração e cozerás a sua carne no lugar santo;
32 e Arão e seus filhos comerão a carne deste carneiro e o pão que está no cesto à porta da tenda da congregação
33 e comerão das coisas com que for feita a expiação, para consagrá-los e para santificá-los; o estranho não comerá delas, porque são santas.
34 Se sobrar alguma coisa da carne das consagrações ou do pão, até pela manhã, queimarás o que restar; não se comerá, porque é santo.
35 Assim, pois, farás a Arão e a seus filhos, conforme tudo o que te hei ordenado; por sete dias, os consagrarás.
36 Também cada dia prepararás um novilho como oferta pelo pecado para as expiações; e purificarás o altar, fazendo expiação por ele mediante oferta pelo pecado; e o ungirás para consagrá-lo.
37 Sete dias farás expiação pelo altar e o consagrarás; e o altar será santíssimo; tudo o que o tocar será santo.
38 Isto é o que oferecerás sobre o altar: dois cordeiros de um ano, cada dia, continuamente.
39 Um cordeiro oferecerás pela manhã e o outro, ao pôr do sol.
40 Com um cordeiro, a décima parte de um efa de flor de farinha, amassada com a quarta parte de um him de azeite batido; e, para libação, a quarta parte de um him de vinho;
41 o outro cordeiro oferecerás ao pôr do sol, como oferta de manjares, e a libação como de manhã, de aroma agradável, oferta queimada ao Senhor.
42 Este será o holocausto contínuo por vossas gerações, à porta da tenda da congregação, perante o Senhor, onde vos encontrarei, para falar contigo ali.
43 Ali, virei aos filhos de Israel, para que, por minha glória, sejam santificados,
44 e consagrarei a tenda da congregação e o altar; também santificarei Arão e seus filhos, para que me oficiem como sacerdotes.
45 E habitarei no meio dos filhos de Israel e serei o seu Deus.
46 E saberão que eu sou o Senhor, seu Deus, que os tirou da terra do Egito, para habitar no meio deles; eu sou o Senhor, seu Deus.*
1 Farás também um altar para queimares nele o incenso; de madeira de acácia o farás.
2 Terá um côvado de comprimento, e um de largura (será quadrado), e dois de altura; os chifres formarão uma só peça com ele.
3 De ouro puro o cobrirás, a parte superior, as paredes ao redor e os chifres; e lhe farás uma bordadura de ouro ao redor.
4 Também lhe farás duas argolas de ouro debaixo da bordadura; de ambos os lados as farás; nelas, se meterão os varais para se levar o altar.
5 De madeira de acácia farás os varais e os cobrirás de ouro.
6 Porás o altar defronte do véu que está diante da arca do Testemunho, diante do propiciatório que está sobre o Testemunho, onde me avistarei contigo.
7 Arão queimará sobre ele o incenso aromático; cada manhã, quando preparar as lâmpadas, o queimará.
8 Quando, ao crepúsculo da tarde, acender as lâmpadas, o queimará; será incenso contínuo perante o Senhor, pelas vossas gerações.
9 Não oferecereis sobre ele incenso estranho, nem holocausto, nem ofertas de manjares; nem tampouco derramareis libações sobre ele.
10 Uma vez no ano, Arão fará expiação sobre os chifres do altar com o sangue da oferta pelo pecado; uma vez no ano, fará expiação sobre ele, pelas vossas gerações; santíssimo é ao Senhor.
11 Disse mais o Senhor a Moisés:
12 Quando fizeres recenseamento dos filhos de Israel, cada um deles dará ao Senhor o resgate de si próprio, quando os contares; para que não haja entre eles praga nenhuma, quando os arrolares.
13 Todo aquele que passar ao arrolamento dará isto: metade de um siclo, segundo o siclo do santuário (este siclo é de vinte geras); a metade de um siclo é a oferta ao Senhor.
14 Qualquer que entrar no arrolamento, de vinte anos para cima, dará a oferta ao Senhor.
15 O rico não dará mais de meio siclo, nem o pobre, menos, quando derem a oferta ao Senhor, para fazerdes expiação pela vossa alma.
16 Tomarás o dinheiro das expiações dos filhos de Israel e o darás ao serviço da tenda da congregação; e será para memória aos filhos de Israel diante do Senhor, para fazerdes expiação pela vossa alma.
17 Disse mais o Senhor a Moisés:
18 Farás também uma bacia de bronze com o seu suporte de bronze, para lavar. Pô-la-ás entre a tenda da congregação e o altar e deitarás água nela.
19 Nela, Arão e seus filhos lavarão as mãos e os pés.
20 Quando entrarem na tenda da congregação, lavar-se-ão com água, para que não morram; ou quando se chegarem ao altar para ministrar, para acender a oferta queimada ao Senhor.
21 Lavarão, pois, as mãos e os pés, para que não morram; e isto lhes será por estatuto perpétuo, a ele e à sua posteridade, através de suas gerações.
22 Disse mais o Senhor a Moisés:
23 Tu, pois, toma das mais excelentes especiarias: de mirra fluida quinhentos siclos, de cinamomo odoroso a metade, a saber, duzentos e cinquenta siclos, e de cálamo aromático duzentos e cinquenta siclos,
24 e de cássia quinhentos siclos, segundo o siclo do santuário, e de azeite de oliveira um him.
25 Disto farás o óleo sagrado para a unção, o perfume composto segundo a arte do perfumista; este será o óleo sagrado da unção.
26 Com ele ungirás a tenda da congregação, e a arca do Testemunho,
27 e a mesa com todos os seus utensílios, e o candelabro com os seus utensílios, e o altar do incenso,
28 e o altar do holocausto com todos os utensílios, e a bacia com o seu suporte.
29 Assim consagrarás estas coisas, para que sejam santíssimas; tudo o que tocar nelas será santo.
30 Também ungirás Arão e seus filhos e os consagrarás para que me oficiem como sacerdotes.
31 Dirás aos filhos de Israel: Este me será o óleo sagrado da unção nas vossas gerações.
32 Não se ungirá com ele o corpo do homem que não seja sacerdote, nem fareis outro semelhante, da mesma composição; é santo e será santo para vós outros.
33 Qualquer que compuser óleo igual a este ou dele puser sobre um estranho será eliminado do seu povo.
34 Disse mais o Senhor a Moisés: Toma substâncias odoríferas, estoraque, ônica e gálbano; estes arômatas com incenso puro, cada um de igual peso;
35 e disto farás incenso, perfume segundo a arte do perfumista, temperado com sal, puro e santo.
36 Uma parte dele reduzirás a pó e o porás diante do Testemunho na tenda da congregação, onde me avistarei contigo; será para vós outros santíssimo.
37 Porém o incenso que fareis, segundo a composição deste, não o fareis para vós mesmos; santo será para o Senhor.
38 Quem fizer tal como este para o cheirar será eliminado do seu povo.*
1 Disse mais o Senhor a Moisés:
2 Eis que chamei pelo nome a Bezalel, filho de Uri, filho de Hur, da tribo de Judá,
3 e o enchi do Espírito de Deus, de habilidade, de inteligência e de conhecimento, em todo artifício,
4 para elaborar desenhos e trabalhar em ouro, em prata, em bronze,
5 para lapidação de pedras de engaste, para entalho de madeira, para toda sorte de lavores.
6 Eis que lhe dei por companheiro Aoliabe, filho de Aisamaque, da tribo de Dã; e dei habilidade a todos os homens hábeis, para que me façam tudo o que tenho ordenado:
7 a tenda da congregação, e a arca do Testemunho, e o propiciatório que está por cima dela, e todos os pertences da tenda;
8 e a mesa com os seus utensílios, e o candelabro de ouro puro com todos os seus utensílios, e o altar do incenso;
9 e o altar do holocausto com todos os seus utensílios e a bacia com seu suporte;
10 e as vestes finamente tecidas, e as vestes sagradas do sacerdote Arão, e as vestes de seus filhos, para oficiarem como sacerdotes;
11 e o óleo da unção e o incenso aromático para o santuário; eles farão tudo segundo tenho ordenado.
12 Disse mais o Senhor a Moisés:
13 Tu, pois, falarás aos filhos de Israel e lhes dirás: Certamente, guardareis os meus sábados; pois é sinal entre mim e vós nas vossas gerações; para que saibais que eu sou o Senhor, que vos santifica.
14 Portanto, guardareis o sábado, porque é santo para vós outros; aquele que o profanar morrerá; pois qualquer que nele fizer alguma obra será eliminado do meio do seu povo.
15 Seis dias se trabalhará, porém o sétimo dia é o sábado do repouso solene, santo ao Senhor; qualquer que no dia do sábado fizer alguma obra morrerá.
16 Pelo que os filhos de Israel guardarão o sábado, celebrando-o por aliança perpétua nas suas gerações.
17 Entre mim e os filhos de Israel é sinal para sempre; porque, em seis dias, fez o Senhor os céus e a terra, e, ao sétimo dia, descansou, e tomou alento.
18 E, tendo acabado de falar com ele no monte Sinai, deu a Moisés as duas tábuas do Testemunho, tábuas de pedra, escritas pelo dedo de Deus.*
1 Mas, vendo o povo que Moisés tardava em descer do monte, acercou-se de Arão e lhe disse: Levanta-te, faze-nos deuses que vão adiante de nós; pois, quanto a este Moisés, o homem que nos tirou do Egito, não sabemos o que lhe terá sucedido.
2 Disse-lhes Arão: Tirai as argolas de ouro das orelhas de vossas mulheres, vossos filhos e vossas filhas e trazei-mas.
3 Então, todo o povo tirou das orelhas as argolas e as trouxe a Arão.
4 Este, recebendo-as das suas mãos, trabalhou o ouro com buril e fez dele um bezerro fundido. Então, disseram: São estes, ó Israel, os teus deuses, que te tiraram da terra do Egito.
5 Arão, vendo isso, edificou um altar diante dele e, apregoando, disse: Amanhã, será festa ao Senhor.
6 No dia seguinte, madrugaram, e ofereceram holocaustos, e trouxeram ofertas pacíficas; e o povo assentou-se para comer e beber e levantou-se para divertir-se.
7 Então, disse o Senhor a Moisés: Vai, desce; porque o teu povo, que fizeste sair do Egito, se corrompeu
8 e depressa se desviou do caminho que lhe havia eu ordenado; fez para si um bezerro fundido, e o adorou, e lhe sacrificou, e diz: São estes, ó Israel, os teus deuses, que te tiraram da terra do Egito.
9 Disse mais o Senhor a Moisés: Tenho visto este povo, e eis que é povo de dura cerviz.
10 Agora, pois, deixa-me, para que se acenda contra eles o meu furor, e eu os consuma; e de ti farei uma grande nação.
11 Porém Moisés suplicou ao Senhor, seu Deus, e disse: Por que se acende, Senhor, a tua ira contra o teu povo, que tiraste da terra do Egito com grande fortaleza e poderosa mão?
12 Por que hão de dizer os egípcios: Com maus intentos os tirou, para matá-los nos montes e para consumi-los da face da terra? Torna-te do furor da tua ira e arrepende-te deste mal contra o teu povo.
13 Lembra-te de Abraão, de Isaque e de Israel, teus servos, aos quais por ti mesmo tens jurado e lhes disseste: Multiplicarei a vossa descendência como as estrelas do céu, e toda esta terra de que tenho falado, dá-la-ei à vossa descendência, para que a possuam por herança eternamente.
14 Então, se arrependeu o Senhor do mal que dissera havia de fazer ao povo.
15 E, voltando-se, desceu Moisés do monte com as duas tábuas do Testemunho nas mãos, tábuas escritas de ambos os lados; de um e de outro lado estavam escritas.
16 As tábuas eram obra de Deus; também a escritura era a mesma escritura de Deus, esculpida nas tábuas.
17 Ouvindo Josué a voz do povo que gritava, disse a Moisés: Há alarido de guerra no arraial.
18 Respondeu-lhe Moisés: Não é alarido dos vencedores nem alarido dos vencidos, mas alarido dos que cantam é o que ouço.
19 Logo que se aproximou do arraial, viu ele o bezerro e as danças; então, acendendo-se-lhe a ira, arrojou das mãos as tábuas e quebrou-as ao pé do monte;
20 e, pegando no bezerro que tinham feito, queimou-o, e o reduziu a pó, que espalhou sobre a água, e deu de beber aos filhos de Israel.
21 Depois, perguntou Moisés a Arão: Que te fez este povo, que trouxeste sobre ele tamanho pecado?
22 Respondeu-lhe Arão: Não se acenda a ira do meu senhor; tu sabes que o povo é propenso para o mal.
23 Pois me disseram: Faze-nos deuses que vão adiante de nós; pois, quanto a este Moisés, o homem que nos tirou da terra do Egito, não sabemos o que lhe terá acontecido.
24 Então, eu lhes disse: quem tem ouro, tire-o. Deram-mo; e eu o lancei no fogo, e saiu este bezerro.
25 Vendo Moisés que o povo estava desenfreado, pois Arão o deixara à solta para vergonha no meio dos seus inimigos,
26 pôs-se em pé à entrada do arraial e disse: Quem é do Senhor venha até mim. Então, se ajuntaram a ele todos os filhos de Levi,
27 aos quais disse: Assim diz o Senhor, o Deus de Israel: Cada um cinja a espada sobre o lado, passai e tornai a passar pelo arraial de porta em porta, e mate cada um a seu irmão, cada um, a seu amigo, e cada um, a seu vizinho.
28 E fizeram os filhos de Levi segundo a palavra de Moisés; e caíram do povo, naquele dia, uns três mil homens.
29 Pois Moisés dissera: Consagrai-vos, hoje, ao Senhor; cada um contra o seu filho e contra o seu irmão, para que ele vos conceda, hoje, bênção.
30 No dia seguinte, disse Moisés ao povo: Vós cometestes grande pecado; agora, porém, subirei ao Senhor e, porventura, farei propiciação pelo vosso pecado.
31 Tornou Moisés ao Senhor e disse: Ora, o povo cometeu grande pecado, fazendo para si deuses de ouro.
32 Agora, pois, perdoa-lhe o pecado; ou, se não, risca-me, peço-te, do livro que escreveste.
33 Então, disse o Senhor a Moisés: Riscarei do meu livro todo aquele que pecar contra mim.
34 Vai, pois, agora, e conduze o povo para onde te disse; eis que o meu Anjo irá adiante de ti; porém, no dia da minha visitação, vingarei, neles, o seu pecado.
35 Feriu, pois, o Senhor ao povo, porque fizeram o bezerro que Arão fabricara.*
1 Disse o Senhor a Moisés: Vai, sobe daqui, tu e o povo que tiraste da terra do Egito, para a terra a respeito da qual jurei a Abraão, a Isaque e a Jacó, dizendo: à tua descendência a darei.
2 Enviarei o Anjo adiante de ti; lançarei fora os cananeus, os amorreus, os heteus, os ferezeus, os heveus e os jebuseus.
3 Sobe para uma terra que mana leite e mel; eu não subirei no meio de ti, porque és povo de dura cerviz, para que te não consuma eu no caminho.
4 Ouvindo o povo estas más notícias, pôs-se a prantear, e nenhum deles vestiu seus atavios.
5 Porquanto o Senhor tinha dito a Moisés: Dize aos filhos de Israel: És povo de dura cerviz; se por um momento eu subir no meio de ti, te consumirei; tira, pois, de ti os atavios, para que eu saiba o que te hei de fazer.
6 Então, os filhos de Israel tiraram de si os seus atavios desde o monte Horebe em diante.
7 Ora, Moisés costumava tomar a tenda e armá-la para si, fora, bem longe do arraial; e lhe chamava a tenda da congregação. Todo aquele que buscava ao Senhor saía à tenda da congregação, que estava fora do arraial.
8 Quando Moisés saía para a tenda, fora, todo o povo se erguia, cada um em pé à porta da sua tenda, e olhavam pelas costas, até entrar ele na tenda.
9 Uma vez dentro Moisés da tenda, descia a coluna de nuvem e punha-se à porta da tenda; e o Senhor falava com Moisés.
10 Todo o povo via a coluna de nuvem que se detinha à porta da tenda; todo o povo se levantava, e cada um, à porta da sua tenda, adorava ao Senhor.
11 Falava o Senhor a Moisés face a face, como qualquer fala a seu amigo; então, voltava Moisés para o arraial, porém o moço Josué, seu servidor, filho de Num, não se apartava da tenda.
12 Disse Moisés ao Senhor: Tu me dizes: Faze subir este povo, porém não me deste saber a quem hás de enviar comigo; contudo, disseste: Conheço-te pelo teu nome; também achaste graça aos meus olhos.
13 Agora, pois, se achei graça aos teus olhos, rogo-te que me faças saber neste momento o teu caminho, para que eu te conheça e ache graça aos teus olhos; e considera que esta nação é teu povo.
14 Respondeu-lhe: A minha presença irá contigo, e eu te darei descanso.
15 Então, lhe disse Moisés: Se a tua presença não vai comigo, não nos faças subir deste lugar.
16 Pois como se há de saber que achamos graça aos teus olhos, eu e o teu povo? Não é, porventura, em andares conosco, de maneira que somos separados, eu e o teu povo, de todos os povos da terra?
17 Disse o Senhor a Moisés: Farei também isto que disseste; porque achaste graça aos meus olhos, e eu te conheço pelo teu nome.
18 Então, ele disse: Rogo-te que me mostres a tua glória.
19 Respondeu-lhe: Farei passar toda a minha bondade diante de ti e te proclamarei o nome do Senhor; terei misericórdia de quem eu tiver misericórdia e me compadecerei de quem eu me compadecer.
20 E acrescentou: Não me poderás ver a face, porquanto homem nenhum verá a minha face e viverá.
21 Disse mais o Senhor: Eis aqui um lugar junto a mim; e tu estarás sobre a penha.
22 Quando passar a minha glória, eu te porei numa fenda da penha e com a mão te cobrirei, até que eu tenha passado.
23 Depois, em tirando eu a mão, tu me verás pelas costas; mas a minha face não se verá.*
1 Então, disse o Senhor a Moisés: Lavra duas tábuas de pedra, como as primeiras; e eu escreverei nelas as mesmas palavras que estavam nas primeiras tábuas, que quebraste.
2 E prepara-te para amanhã, para que subas, pela manhã, ao monte Sinai e ali te apresentes a mim no cimo do monte.
3 Ninguém suba contigo, ninguém apareça em todo o monte; nem ainda ovelhas nem gado se apascentem defronte dele.
4 Lavrou, pois, Moisés duas tábuas de pedra, como as primeiras; e, levantando-se pela manhã de madrugada, subiu ao monte Sinai, como o Senhor lhe ordenara, levando nas mãos as duas tábuas de pedra.
5 Tendo o Senhor descido na nuvem, ali esteve junto dele e proclamou o nome do Senhor.
6 E, passando o Senhor por diante dele, clamou: Senhor, Senhor Deus compassivo, clemente e longânimo e grande em misericórdia e fidelidade;
7 que guarda a misericórdia em mil gerações, que perdoa a iniquidade, a transgressão e o pecado, ainda que não inocenta o culpado, e visita a iniquidade dos pais nos filhos e nos filhos dos filhos, até à terceira e quarta geração!
8 E, imediatamente, curvando-se Moisés para a terra, o adorou;
9 e disse: Senhor, se, agora, achei graça aos teus olhos, segue em nosso meio conosco; porque este povo é de dura cerviz. Perdoa a nossa iniquidade e o nosso pecado e toma-nos por tua herança.
10 Então, disse: Eis que faço uma aliança; diante de todo o teu povo farei maravilhas que nunca se fizeram em toda a terra, nem entre nação alguma, de maneira que todo este povo, em cujo meio tu estás, veja a obra do Senhor; porque coisa terrível é o que faço contigo.
11 Guarda o que eu te ordeno hoje: eis que lançarei fora da sua presença os amorreus, os cananeus, os heteus, os ferezeus, os heveus e os jebuseus.
12 Abstém-te de fazer aliança com os moradores da terra para onde vais, para que te não sejam por cilada.
13 Mas derribareis os seus altares, quebrareis as suas colunas e cortareis os seus postes-ídolos
14 (porque não adorarás outro deus; pois o nome do Senhor é Zeloso; sim, Deus zeloso é ele);
15 para que não faças aliança com os moradores da terra; não suceda que, em se prostituindo eles com os deuses e lhes sacrificando, alguém te convide, e comas dos seus sacrifícios
16 e tomes mulheres das suas filhas para os teus filhos, e suas filhas, prostituindo-se com seus deuses, façam que também os teus filhos se prostituam com seus deuses.
17 Não farás para ti deuses fundidos.
18 Guardarás a Festa dos Pães Asmos; sete dias comerás pães asmos, como te ordenei, no tempo indicado no mês de abibe; porque no mês de abibe saíste do Egito.
19 Todo o que abre a madre é meu; também de todo o teu gado, sendo macho, o que abre a madre de vacas e de ovelhas.
20 O jumento, porém, que abrir a madre, resgatá-lo-ás com cordeiro; mas, se o não resgatares, será desnucado. Remirás todos os primogênitos de teus filhos. Ninguém aparecerá diante de mim de mãos vazias.
21 Seis dias trabalharás, mas, ao sétimo dia, descansarás, quer na aradura, quer na sega.
22 Também guardarás a Festa das Semanas, que é a das primícias da sega do trigo, e a Festa da Colheita no fim do ano.
23 Três vezes no ano, todo homem entre ti aparecerá perante o Senhor Deus, Deus de Israel.
24 Porque lançarei fora as nações de diante de ti e alargarei o teu território; ninguém cobiçará a tua terra quando subires para comparecer na presença do Senhor, teu Deus, três vezes no ano.
25 Não oferecerás o sangue do meu sacrifício com pão levedado; nem ficará o sacrifício da Festa da Páscoa da noite para a manhã.
26 As primícias dos primeiros frutos da tua terra trarás à Casa do Senhor, teu Deus. Não cozerás o cabrito no leite da sua própria mãe.
27 Disse mais o Senhor a Moisés: Escreve estas palavras, porque, segundo o teor destas palavras, fiz aliança contigo e com Israel.
28 E, ali, esteve com o Senhor quarenta dias e quarenta noites; não comeu pão, nem bebeu água; e escreveu nas tábuas as palavras da aliança, as dez palavras.
29 Quando desceu Moisés do monte Sinai, tendo nas mãos as duas tábuas do Testemunho, sim, quando desceu do monte, não sabia Moisés que a pele do seu rosto resplandecia, depois de haver Deus falado com ele.
30 Olhando Arão e todos os filhos de Israel para Moisés, eis que resplandecia a pele do seu rosto; e temeram chegar-se a ele.
31 Então, Moisés os chamou; Arão e todos os príncipes da congregação tornaram a ele, e Moisés lhes falou.
32 Depois, vieram também todos os filhos de Israel, aos quais ordenou ele tudo o que o Senhor lhe falara no monte Sinai.
33 Tendo Moisés acabado de falar com eles, pôs um véu sobre o rosto.
34 Porém, vindo Moisés perante o Senhor para falar-lhe, removia o véu até sair; e, saindo, dizia aos filhos de Israel tudo o que lhe tinha sido ordenado.
35 Assim, pois, viam os filhos de Israel o rosto de Moisés, viam que a pele do seu rosto resplandecia; porém Moisés cobria de novo o rosto com o véu até entrar a falar com ele.*
1 Tendo Moisés convocado toda a congregação dos filhos de Israel, disse-lhes: São estas as palavras que o Senhor ordenou que se cumprissem:
2 Trabalhareis seis dias, mas o sétimo dia vos será santo, o sábado do repouso solene ao Senhor; quem nele trabalhar morrerá.
3 Não acendereis fogo em nenhuma das vossas moradas no dia do sábado.
4 Disse mais Moisés a toda a congregação dos filhos de Israel: Esta é a palavra que o Senhor ordenou, dizendo:
5 Tomai, do que tendes, uma oferta para o Senhor; cada um, de coração disposto, voluntariamente a trará por oferta ao Senhor: ouro, prata, bronze,
6 estofo azul, púrpura, carmesim, linho fino, pelos de cabra,
7 peles de carneiro tintas de vermelho, peles finas, madeira de acácia,
8 azeite para a iluminação, especiarias para o óleo da unção e para o incenso aromático,
9 pedras de ônix e pedras de engaste para a estola sacerdotal e para o peitoral.
10 Venham todos os homens hábeis entre vós e façam tudo o que o Senhor ordenou:
11 o tabernáculo com sua tenda e a sua coberta, os seus ganchos, as suas tábuas, as suas vergas, as suas colunas e as suas bases;
12 a arca e os seus varais, o propiciatório e o véu do reposteiro;
13 a mesa e os seus varais, e todos os seus utensílios, e os pães da proposição;
14 o candelabro da iluminação, e os seus utensílios, e as suas lâmpadas, e o azeite para a iluminação;
15 o altar do incenso e os seus varais, e o óleo da unção, e o incenso aromático, e o reposteiro da porta à entrada do tabernáculo;
16 o altar do holocausto e a sua grelha de bronze, os seus varais e todos os seus utensílios, a bacia e o seu suporte;
17 as cortinas do átrio, e as suas colunas, e as suas bases, e o reposteiro da porta do átrio;
18 as estacas do tabernáculo, e as estacas do átrio, e as suas cordas;
19 as vestes do ministério para ministrar no santuário, as vestes santas do sacerdote Arão e as vestes de seus filhos, para oficiarem como sacerdotes.
20 Então, toda a congregação dos filhos de Israel saiu da presença de Moisés,
21 e veio todo homem cujo coração o moveu e cujo espírito o impeliu e trouxe a oferta ao Senhor para a obra da tenda da congregação, e para todo o seu serviço, e para as vestes sagradas.
22 Vieram homens e mulheres, todos dispostos de coração; trouxeram fivelas, pendentes, anéis, braceletes, todos os objetos de ouro; todo homem fazia oferta de ouro ao Senhor;
23 e todo homem possuidor de estofo azul, púrpura, carmesim, linho fino, pelos de cabra, peles de carneiro tintas de vermelho e peles de animais marinhos os trazia.
24 Todo aquele que fazia oferta de prata ou de bronze por oferta ao Senhor a trazia; e todo possuidor de madeira de acácia para toda obra do serviço a trazia.
25 Todas as mulheres hábeis traziam o que, por suas próprias mãos, tinham fiado: estofo azul, púrpura, carmesim e linho fino.
26 E todas as mulheres cujo coração as moveu em habilidade fiavam os pelos de cabra.
27 Os príncipes traziam pedras de ônix, e pedras de engaste para a estola sacerdotal e para o peitoral,
28 e os arômatas, e o azeite para a iluminação, e para o óleo da unção, e para o incenso aromático.
29 Os filhos de Israel trouxeram oferta voluntária ao Senhor, a saber, todo homem e mulher cujo coração os dispôs para trazerem uma oferta para toda a obra que o Senhor tinha ordenado se fizesse por intermédio de Moisés.
30 Disse Moisés aos filhos de Israel: Eis que o Senhor chamou pelo nome a Bezalel, filho de Uri, filho de Hur, da tribo de Judá,
31 e o Espírito de Deus o encheu de habilidade, inteligência e conhecimento em todo artifício,
32 e para elaborar desenhos e trabalhar em ouro, em prata, em bronze,
33 e para lapidação de pedras de engaste, e para entalho de madeira, e para toda sorte de lavores.
34 Também lhe dispôs o coração para ensinar a outrem, a ele e a Aoliabe, filho de Aisamaque, da tribo de Dã.
35 Encheu-os de habilidade para fazer toda obra de mestre, até a mais engenhosa, e a do bordador em estofo azul, em púrpura, em carmesim e em linho fino, e a do tecelão, sim, toda sorte de obra e a elaborar desenhos.*
1 Assim, trabalharam Bezalel, e Aoliabe, e todo homem hábil a quem o Senhor dera habilidade e inteligência para saberem fazer toda obra para o serviço do santuário, segundo tudo o que o Senhor havia ordenado.
2 Moisés chamou a Bezalel, e a Aoliabe, e a todo homem hábil em cujo coração o Senhor tinha posto sabedoria, isto é, a todo homem cujo coração o impeliu a se chegar à obra para fazê-la.
3 Estes receberam de Moisés todas as ofertas que os filhos de Israel haviam trazido para a obra do serviço do santuário, para fazê-la; e, ainda, cada manhã o povo trazia a Moisés ofertas voluntárias.
4 Então, deixando cada um a obra que fazia, vieram todos os homens sábios que se ocupavam em toda a obra do santuário
5 e disseram a Moisés: O povo traz muito mais do que é necessário para o serviço da obra que o Senhor ordenou se fizesse.
6 Então, ordenou Moisés — e a ordem foi proclamada no arraial, dizendo: Nenhum homem ou mulher faça mais obra alguma para a oferta do santuário. Assim, o povo foi proibido de trazer mais.
7 Porque o material que tinham era suficiente para toda a obra que se devia fazer e ainda sobejava.
8 Assim, todos os homens hábeis, entre os que faziam a obra, fizeram o tabernáculo com dez cortinas de linho fino retorcido, estofo azul, púrpura e carmesim com querubins; de obra de artista as fizeram.
9 O comprimento de cada cortina era de vinte e oito côvados, e a largura, de quatro côvados; todas as cortinas eram de igual medida.
10 Cinco cortinas eram ligadas uma à outra; e as outras cinco também ligadas uma à outra.
11 Fizeram laçadas de estofo azul na orla da cortina, que estava na extremidade do primeiro agrupamento; e de igual modo fizeram na orla da cortina, que estava na extremidade do segundo agrupamento.
12 Cinquenta laçadas fizeram numa cortina, e cinquenta, na outra cortina na extremidade do segundo agrupamento; as laçadas eram contrapostas uma à outra.
13 Fizeram cinquenta colchetes de ouro, com os quais prenderam as cortinas uma à outra; e o tabernáculo passou a ser um todo.
14 Fizeram também de pelos de cabra cortinas para servirem de tenda sobre o tabernáculo; fizeram onze cortinas.
15 O comprimento de cada cortina era de trinta côvados, e a largura, de quatro côvados; as onze cortinas eram de igual medida.
16 Ajuntaram à parte cinco cortinas entre si e, de igual modo, as seis restantes.
17 E fizeram cinquenta laçadas na orla da cortina, que estava na extremidade do primeiro agrupamento.
18 Fizeram também cinquenta colchetes de bronze para ajuntar a tenda, para que viesse a ser um todo.
19 Fizeram também de peles de carneiro tintas de vermelho uma coberta para a tenda e outra coberta de peles finas.
20 Fizeram também de madeira de acácia as tábuas para o tabernáculo, as quais eram colocadas verticalmente.
21 Cada uma das tábuas tinha dez côvados de comprimento e côvado e meio de largura.
22 Cada tábua tinha dois encaixes, travados um com o outro; assim fizeram com todas as tábuas do tabernáculo.
23 No preparar as tábuas para o tabernáculo, fizeram vinte delas para o lado sul.
24 Fizeram também quarenta bases de prata debaixo das vinte tábuas: duas bases debaixo de uma tábua para os seus dois encaixes e duas bases debaixo de outra tábua para os seus dois encaixes.
25 Também fizeram vinte tábuas ao outro lado do tabernáculo, para o lado norte,
26 com as suas quarenta bases de prata: duas bases debaixo de uma tábua e duas bases debaixo de outra tábua;
27 ao lado do tabernáculo para o ocidente, fizeram seis tábuas.
28 Fizeram também duas tábuas para os cantos do tabernáculo de ambos os lados,
29 as quais, por baixo, estavam separadas, mas, em cima, se ajustavam à primeira argola; assim se fez com as duas tábuas nos dois cantos.
30 Assim eram as oito tábuas com as suas bases de prata, dezesseis bases: duas bases debaixo de uma tábua e duas debaixo de outra tábua.
31 Fizeram também travessas de madeira de acácia; cinco para as tábuas de um lado do tabernáculo,
32 cinco para as tábuas do outro lado do tabernáculo e cinco para as tábuas do tabernáculo, ao lado posterior, que olha para o ocidente.
33 A travessa do meio passava ao meio das tábuas, de uma extremidade à outra.
34 Cobriram de ouro as tábuas e de ouro fizeram as suas argolas, pelas quais passavam as travessas; e cobriram também de ouro as travessas.
35 Fizeram também o véu de estofo azul, púrpura, carmesim e linho fino retorcido; com querubins o fizeram de obra de artista.
36 E fizeram-lhe quatro colunas de madeira de acácia, cobertas de ouro; os seus colchetes eram de ouro, sobre quatro bases de prata.
37 Fizeram também para a porta da tenda um reposteiro de estofo azul, púrpura, carmesim e linho fino retorcido, obra de bordador,
38 e as suas cinco colunas, e os seus colchetes; as suas cabeças e as suas molduras cobriram de ouro, mas as suas cinco bases eram de bronze.*
1 Fez também Bezalel a arca de madeira de acácia; de dois côvados e meio era o seu comprimento, de um côvado e meio, a largura, e, de um côvado e meio, a altura.
2 De ouro puro a cobriu; por dentro e por fora a cobriu e fez uma bordadura de ouro ao redor.
3 Fundiu para ela quatro argolas de ouro e as pôs nos quatro cantos da arca: duas argolas num lado dela e duas argolas noutro lado.
4 Fez também varais de madeira de acácia e os cobriu de ouro;
5 meteu os varais nas argolas aos lados da arca, para se levar por meio deles a arca.
6 Fez também o propiciatório de ouro puro; de dois côvados e meio era o seu comprimento, e a largura, de um côvado e meio.
7 Fez também dois querubins de ouro; de ouro batido os fez, nas duas extremidades do propiciatório.
8 Um querubim, na extremidade de uma parte, e o outro, na extremidade da outra parte; de uma só peça com o propiciatório fez os querubins nas duas extremidades dele.
9 Os querubins estendiam as asas por cima, cobrindo com elas o propiciatório; estavam eles de faces voltadas uma para a outra, olhando para o propiciatório.
10 Fez também a mesa de madeira de acácia; tinha o comprimento de dois côvados, a largura, de um côvado, e a altura, de um côvado e meio.
11 De ouro puro a cobriu e lhe fez uma bordadura de ouro ao redor.
12 Também lhe fez moldura ao redor, na largura de quatro dedos, e lhe fez uma bordadura de ouro ao redor da moldura.
13 Também lhe fundiu quatro argolas de ouro e pôs as argolas nos quatro cantos que estavam nos seus quatro pés.
14 Perto da moldura estavam as argolas, como lugares para os varais, para se levar a mesa.
15 Fez os varais de madeira de acácia e os cobriu de ouro, para se levar a mesa.
16 Também fez de ouro puro os utensílios que haviam de estar sobre a mesa: os seus pratos, e os seus recipientes para incenso, e as suas galhetas, e as suas taças em que se haviam de oferecer libações.
17 Fez também o candelabro de ouro puro; de ouro batido o fez; o seu pedestal, a sua hástea, os seus cálices, as suas maçanetas e as suas flores formavam com ele uma só peça.
18 Seis hásteas saíam dos seus lados; três de um lado e três do outro.
19 Numa hástea havia três cálices com formato de amêndoas, uma maçaneta e uma flor; e três cálices com formato de amêndoas na outra hástea, uma maçaneta e uma flor; assim eram as seis hásteas que saíam do candelabro.
20 Mas no candelabro mesmo havia quatro cálices com formato de amêndoas, com suas maçanetas e com suas flores.
21 Havia uma maçaneta sob duas hásteas que saíam dele; e ainda uma maçaneta sob duas outras hásteas que saíam dele; e ainda mais uma maçaneta sob duas outras hásteas que saíam dele; assim se fez com as seis hásteas que saíam do candelabro.
22 As suas maçanetas e as suas hásteas eram do mesmo; tudo era de uma só peça, obra batida de ouro puro.
23 Também lhe fez sete lâmpadas; as suas espevitadeiras e os seus apagadores eram de ouro puro.
24 De um talento de ouro puro se fez o candelabro com todos os seus utensílios.
25 Fez de madeira de acácia o altar do incenso; tinha um côvado de comprimento, e um de largura (era quadrado), e dois de altura; os chifres formavam uma só peça com ele.
26 De ouro puro o cobriu, a parte superior, as paredes ao redor e os chifres; e lhe fez uma bordadura de ouro ao redor.
27 Também lhe fez duas argolas de ouro debaixo da bordadura, de ambos os lados as fez; nelas, se meteram os varais para se levar o altar;
28 de madeira de acácia fez os varais e os cobriu de ouro.
29 Fez também o óleo santo da unção e o incenso aromático, puro, de obra de perfumista.*
1 Fez também o altar do holocausto de madeira de acácia; de cinco côvados era o comprimento, e de cinco, a largura (era quadrado o altar), e de três côvados, a altura.
2 Dos quatro cantos fez levantar-se quatro chifres, os quais formavam uma só peça com o altar; e o cobriu de bronze.
3 Fez também todos os utensílios do altar: recipientes para recolher as suas cinzas, e pás, e bacias, e garfos, e braseiros; todos esses utensílios, de bronze os fez.
4 Fez também para o altar uma grelha de bronze em forma de rede, do rebordo do altar para baixo, a qual chegava até ao meio do altar.
5 Fundiu quatro argolas para os quatro cantos da grelha de bronze, para nelas se meterem os varais.
6 Fez os varais de madeira de acácia e os cobriu de bronze.
7 Meteu os varais nas argolas, de um e de outro lado do altar, para ser levado; oco e de tábuas o fez.
8 Fez também a bacia de bronze, com o seu suporte de bronze, dos espelhos das mulheres que se reuniam para ministrar à porta da tenda da congregação.
9 Fez também o átrio ao lado meridional (que dá para o sul); as cortinas do átrio eram de linho fino retorcido, de cem côvados de comprimento.
10 As suas vinte colunas e as suas bases eram de bronze; os ganchos das colunas e as suas vergas eram de prata.
11 De igual modo para o lado norte havia cortinas de cem côvados de comprimento; as suas vinte colunas e as suas vinte bases eram de bronze; os ganchos das colunas e as suas vergas eram de prata.
12 Para o lado do ocidente havia cortinas de cinquenta côvados; as suas colunas eram dez, e as suas bases, dez; os ganchos das colunas e as suas vergas eram de prata.
13 Do lado oriental (para o levante), eram as cortinas de cinquenta côvados.
14 As cortinas para um lado da entrada eram de quinze côvados; e as suas colunas eram três, e as suas bases, três.
15 Para o outro lado da entrada do átrio, de um e de outro lado da entrada, eram as cortinas de quinze côvados; as suas colunas eram três, e as suas bases, três.
16 Todas as cortinas ao redor do átrio eram de linho fino retorcido.
17 As bases das colunas eram de bronze; os ganchos das colunas e as suas vergas eram de prata.
18 O reposteiro da porta do átrio era de obra de bordador, de estofo azul, púrpura, carmesim e linho fino retorcido; o comprimento era de vinte côvados, e a altura, na largura, era de cinco côvados, segundo a medida das cortinas do átrio.
19 As suas quatro colunas e as suas quatro bases eram de bronze, os seus ganchos eram de prata, e o revestimento das suas cabeças e as suas vergas, de prata.
20 Todos os pregos do tabernáculo e do átrio ao redor eram de bronze.
21 Esta é a enumeração das coisas para o tabernáculo, a saber, o tabernáculo do Testemunho, segundo, por ordem de Moisés, foram contadas para o serviço dos levitas, por intermédio de Itamar, filho do sacerdote Arão.
22 Fez Bezalel, filho de Uri, filho de Hur, da tribo de Judá, tudo quanto o Senhor ordenara a Moisés.
23 E, com ele, Aoliabe, filho de Aisamaque, da tribo de Dã, mestre de obras, desenhista e bordador em estofo azul, púrpura, carmesim e linho fino.
24 Todo o ouro empregado na obra, em toda a obra do santuário, a saber, o ouro da oferta, foram vinte e nove talentos e setecentos e trinta siclos, segundo o siclo do santuário.
25 A prata dos arrolados da congregação foram cem talentos e mil e setecentos e setenta e cinco siclos, segundo o siclo do santuário:
26 um beca por cabeça, isto é, meio siclo, segundo o siclo do santuário, de qualquer dos arrolados, de vinte anos para cima, que foram seiscentos e três mil quinhentos e cinquenta.
27 Empregaram-se cem talentos de prata para fundir as bases do santuário e as bases do véu; para as cem bases, cem talentos: um talento para cada base.
28 Dos mil setecentos e setenta e cinco siclos, fez os colchetes das colunas, e cobriu as suas cabeças, e lhes fez as vergas.
29 O bronze da oferta foram setenta talentos e dois mil e quatrocentos siclos.
30 Dele fez as bases da porta da tenda da congregação, e o altar de bronze, e a sua grelha de bronze, e todos os utensílios do altar,
31 e as bases do átrio ao redor, e as bases da porta do átrio, e todas as estacas do tabernáculo, e todas as estacas do átrio ao redor.*
1 Fizeram também de estofo azul, púrpura e carmesim as vestes, finamente tecidas, para ministrar no santuário, e também fizeram as vestes sagradas para Arão, como o Senhor ordenara a Moisés.
2 Fizeram a estola sacerdotal de ouro, estofo azul, púrpura, carmesim e linho fino retorcido.
3 De ouro batido fizeram lâminas delgadas e as cortaram em fios, para permearem entre o estofo azul, a púrpura, o carmesim e o linho fino da obra de desenhista.
4 Tinha duas ombreiras que se ajuntavam às suas duas extremidades, e assim se uniam.
5 O cinto de obra esmerada, que estava sobre a estola sacerdotal, era de obra igual, da mesma obra de ouro, estofo azul, púrpura, carmesim e linho fino retorcido, segundo o Senhor ordenara a Moisés.
6 Também se prepararam as pedras de ônix, engastadas em ouro, trabalhadas como lavores de sinete, com os nomes dos filhos de Israel,
7 e as puseram nas ombreiras da estola sacerdotal, por pedras de memória aos filhos de Israel, segundo o Senhor ordenara a Moisés.
8 Fizeram também o peitoral de obra esmerada, conforme a obra da estola sacerdotal: de ouro, estofo azul, púrpura, carmesim e linho fino retorcido.
9 Era quadrado; duplo fizeram o peitoral: de um palmo era o seu comprimento, e de um palmo dobrado, a sua largura.
10 Colocaram, nele, engastes de pedras, com quatro ordens de pedras: a ordem de sárdio, topázio e carbúnculo era a primeira;
11 a segunda ordem era de esmeralda, safira e diamante;
12 a terceira ordem era de jacinto, ágata e ametista;
13 e a quarta ordem era de berilo, ônix e jaspe; eram elas guarnecidas de ouro nos seus engastes.
14 As pedras eram conforme os nomes dos filhos de Israel, doze segundo os seus nomes; eram esculpidas como sinete, cada uma com o seu nome para as doze tribos.
15 E fizeram para o peitoral correntes como cordas, de obra trançada de ouro puro.
16 Também fizeram para o peitoral dois engastes de ouro e duas argolas de ouro; e puseram as duas argolas nas extremidades do peitoral.
17 E meteram as duas correntes trançadas de ouro nas duas argolas, nas extremidades do peitoral.
18 As outras duas pontas das duas correntes trançadas meteram nos dois engastes e as puseram nas ombreiras da estola sacerdotal, na frente dele.
19 Fizeram também duas argolas de ouro e as puseram nas duas extremidades do peitoral, na sua orla interior oposta à estola sacerdotal.
20 Fizeram também mais duas argolas de ouro e as puseram nas duas ombreiras da estola sacerdotal, abaixo, na frente dele, perto da sua juntura, sobre o cinto de obra esmerada da estola sacerdotal.
21 E ligaram o peitoral com as suas argolas às argolas da estola sacerdotal, por cima com uma fita azul, para que estivesse sobre o cinto de obra esmerada da estola sacerdotal, e nunca o peitoral se separasse da estola sacerdotal, segundo o Senhor ordenara a Moisés.
22 Fizeram também a sobrepeliz da estola sacerdotal, de obra tecida, toda de estofo azul.
23 No meio dela havia uma abertura; era debruada como abertura de uma saia de malha, para que se não rompesse.
24 Em toda a orla da sobrepeliz, fizeram romãs de estofo azul, carmesim e linho retorcido.
25 Fizeram campainhas de ouro puro e as colocaram no meio das romãs em toda a orla da sobrepeliz;
26 uma campainha e uma romã, outra campainha e outra romã, em toda a orla da sobrepeliz, para se usar ao ministrar, segundo o Senhor ordenara a Moisés.
27 Fizeram também as túnicas de linho fino, de obra tecida, para Arão e para seus filhos,
28 e a mitra de linho fino, e as tiaras de linho fino, e os calções de linho fino retorcido,
29 e o cinto de linho fino retorcido, e de estofo azul, e de púrpura, e de carmesim, obra de bordador, segundo o Senhor ordenara a Moisés.
30 Também fizeram de ouro puro a lâmina da coroa sagrada e, nela, gravaram à maneira de gravuras de sinete: Santidade ao Senhor.
31 E ataram-na com um cordão de estofo azul, para prender a lâmina à parte superior da mitra, segundo o Senhor ordenara a Moisés.
32 Assim se concluiu toda a obra do tabernáculo da tenda da congregação; e os filhos de Israel fizeram tudo segundo o Senhor tinha ordenado a Moisés; assim o fizeram.
33 Depois, trouxeram a Moisés o tabernáculo, a tenda e todos os seus pertences, os seus colchetes, as suas tábuas, as suas vergas, as suas colunas e as suas bases;
34 a coberta de peles de carneiro tintas de vermelho, e a coberta de peles finas, e o véu do reposteiro;
35 a arca do Testemunho, e os seus varais, e o propiciatório;
36 a mesa com todos os seus utensílios e os pães da proposição;
37 o candelabro de ouro puro com suas lâmpadas; as lâmpadas colocadas em ordem, e todos os seus utensílios, e o azeite para a iluminação;
38 também o altar de ouro, e o óleo da unção, e o incenso aromático, e o reposteiro da porta da tenda;
39 o altar de bronze, e a sua grelha de bronze, e os seus varais, e todos os seus utensílios, e a bacia, e o seu suporte;
40 as cortinas do átrio, e as suas colunas, e as suas bases, e o reposteiro para a porta do átrio, e as suas cordas, e os seus pregos, e todos os utensílios do serviço do tabernáculo, para a tenda da congregação;
41 as vestes finamente tecidas para ministrar no santuário, e as vestes sagradas do sacerdote Arão, e as vestes de seus filhos, para oficiarem como sacerdotes.
42 Tudo segundo o Senhor ordenara a Moisés, assim fizeram os filhos de Israel toda a obra.
43 Viu, pois, Moisés toda a obra, e eis que a tinham feito segundo o Senhor havia ordenado; assim a fizeram, e Moisés os abençoou.*
1 Depois, disse o Senhor a Moisés:
2 No primeiro dia do primeiro mês, levantarás o tabernáculo da tenda da congregação.
3 Porás, nele, a arca do Testemunho e a cobrirás com o véu.
4 Meterás, nele, a mesa e porás por ordem as coisas que estão sobre ela; também meterás, nele, o candelabro e acenderás as suas lâmpadas.
5 Porás o altar de ouro para o incenso diante da arca do Testemunho e pendurarás o reposteiro da porta do tabernáculo.
6 Porás o altar do holocausto diante da porta do tabernáculo da tenda da congregação.
7 Porás a bacia entre a tenda da congregação e o altar e a encherás de água.
8 Depois, porás o átrio ao redor e pendurarás o reposteiro à porta do átrio.
9 E tomarás o óleo da unção, e ungirás o tabernáculo e tudo o que nele está, e o consagrarás com todos os seus pertences; e será santo.
10 Ungirás também o altar do holocausto e todos os seus utensílios e consagrarás o altar; e o altar se tornará santíssimo.
11 Então, ungirás a bacia e o seu suporte e a consagrarás.
12 Farás também chegar Arão e seus filhos à porta da tenda da congregação e os lavarás com água.
13 Vestirás Arão das vestes sagradas, e o ungirás, e o consagrarás para que me oficie como sacerdote.
14 Também farás chegar seus filhos, e lhes vestirás as túnicas,
15 e os ungirás como ungiste seu pai, para que me oficiem como sacerdotes; sua unção lhes será por sacerdócio perpétuo durante as suas gerações.
ntado
16 E tudo fez Moisés segundo o Senhor lhe havia ordenado; assim o fez.
17 No primeiro mês do segundo ano, no primeiro dia do mês, se levantou o tabernáculo.
18 Moisés levantou o tabernáculo, e pôs as suas bases, e armou as suas tábuas, e meteu, nele, as suas vergas, e levantou as suas colunas;
19 estendeu a tenda sobre o tabernáculo e pôs a coberta da tenda por cima, segundo o Senhor ordenara a Moisés.
20 Tomou o Testemunho, e o pôs na arca, e meteu os varais na arca, e pôs o propiciatório em cima da arca.
21 Introduziu a arca no tabernáculo, e pendurou o véu do reposteiro, e com ele cobriu a arca do Testemunho, segundo o Senhor ordenara a Moisés.
22 Pôs também a mesa na tenda da congregação, ao lado do tabernáculo, para o norte, fora do véu,
23 e sobre ela pôs em ordem os pães da proposição perante o Senhor, segundo o Senhor ordenara a Moisés.
24 Pôs também, na tenda da congregação, o candelabro defronte da mesa, ao lado do tabernáculo, para o sul,
25 e preparou as lâmpadas perante o Senhor, segundo o Senhor ordenara a Moisés.
26 Pôs o altar de ouro na tenda da congregação, diante do véu,
27 e acendeu sobre ele o incenso aromático, segundo o Senhor ordenara a Moisés.
28 Pendurou também o reposteiro da porta do tabernáculo,
29 pôs o altar do holocausto à porta do tabernáculo da tenda da congregação e ofereceu sobre ele holocausto e oferta de cereais, segundo o Senhor ordenara a Moisés.
30 Pôs a bacia entre a tenda da congregação e o altar e a encheu de água, para se lavar.
31 Nela, Moisés, Arão e seus filhos lavavam as mãos e os pés,
32 quando entravam na tenda da congregação e quando se chegavam ao altar, segundo o Senhor ordenara a Moisés.
33 Levantou também o átrio ao redor do tabernáculo e do altar e pendurou o reposteiro da porta do átrio. Assim Moisés acabou a obra.
34 Então, a nuvem cobriu a tenda da congregação, e a glória do Senhor encheu o tabernáculo.
35 Moisés não podia entrar na tenda da congregação, porque a nuvem permanecia sobre ela, e a glória do Senhor enchia o tabernáculo.
36 Quando a nuvem se levantava de sobre o tabernáculo, os filhos de Israel caminhavam avante, em todas as suas jornadas;
37 se a nuvem, porém, não se levantava, não caminhavam, até ao dia em que ela se levantava.
38 De dia, a nuvem do Senhor repousava sobre o tabernáculo, e, de noite, havia fogo nela, à vista de toda a casa de Israel, em todas as suas jornadas.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Êxodo','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)