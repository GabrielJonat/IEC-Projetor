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
1 Sucedeu, depois da morte de Moisés, servo do Senhor, que este falou a Josué, filho de Num, servidor de Moisés, dizendo:
2 Moisés, meu servo, é morto; dispõe-te, agora, passa este Jordão, tu e todo este povo, à terra que eu dou aos filhos de Israel.
3 Todo lugar que pisar a planta do vosso pé, vo-lo tenho dado, como eu prometi a Moisés.
4 Desde o deserto e o Líbano até ao grande rio, o rio Eufrates, toda a terra dos heteus e até ao mar Grande para o poente do sol será o vosso limite.
5 Ninguém te poderá resistir todos os dias da tua vida; como fui com Moisés, assim serei contigo; não te deixarei, nem te desampararei.
6 Sê forte e corajoso, porque tu farás este povo herdar a terra que, sob juramento, prometi dar a seus pais.
7 Tão somente sê forte e mui corajoso para teres o cuidado de fazer segundo toda a lei que meu servo Moisés te ordenou; dela não te desvies, nem para a direita nem para a esquerda, para que sejas bem-sucedido por onde quer que andares.
8 Não cesses de falar deste Livro da Lei; antes, medita nele dia e noite, para que tenhas cuidado de fazer segundo tudo quanto nele está escrito; então, farás prosperar o teu caminho e serás bem-sucedido.
9 Não to mandei eu? Sê forte e corajoso; não temas, nem te espantes, porque o Senhor, teu Deus, é contigo por onde quer que andares.
10 Então, deu ordem Josué aos príncipes do povo, dizendo:
11 Passai pelo meio do arraial e ordenai ao povo, dizendo: Provede-vos de comida, porque, dentro de três dias, passareis este Jordão, para que entreis na terra que vos dá o Senhor, vosso Deus, para a possuirdes.
12 Falou Josué aos rubenitas, e aos gaditas, e à meia tribo de Manassés, dizendo:
13 Lembrai-vos do que vos ordenou Moisés, servo do Senhor, dizendo: O Senhor, vosso Deus, vos concede descanso e vos dá esta terra.
14 Vossas mulheres, vossos meninos e vosso gado fiquem na terra que Moisés vos deu deste lado do Jordão; porém vós, todos os valentes, passareis armados na frente de vossos irmãos e os ajudareis,
15 até que o Senhor conceda descanso a vossos irmãos, como a vós outros, e eles também tomem posse da terra que o Senhor, vosso Deus, lhes dá; então, tornareis à terra da vossa herança e possuireis a que vos deu Moisés, servo do Senhor, deste lado do Jordão, para o nascente do sol.
16 Então, responderam a Josué, dizendo: Tudo quanto nos ordenaste faremos e aonde quer que nos enviares iremos.
17 Como em tudo obedecemos a Moisés, assim obedeceremos a ti; tão somente seja o Senhor, teu Deus, contigo, como foi com Moisés.
18 Todo homem que se rebelar contra as tuas ordens e não obedecer às tuas palavras em tudo quanto lhe ordenares será morto; tão somente sê forte e corajoso.*
1 De Sitim enviou Josué, filho de Num, dois homens, secretamente, como espias, dizendo: Andai e observai a terra e Jericó. Foram, pois, e entraram na casa de uma mulher prostituta, cujo nome era Raabe, e pousaram ali.
2 Então, se deu notícia ao rei de Jericó, dizendo: Eis que, esta noite, vieram aqui uns homens dos filhos de Israel para espiar a terra.
3 Mandou, pois, o rei de Jericó dizer a Raabe: Faze sair os homens que vieram a ti e entraram na tua casa, porque vieram espiar toda a terra.
4 A mulher, porém, havia tomado e escondido os dois homens; e disse: É verdade que os dois homens vieram a mim, porém eu não sabia donde eram.
5 Havendo-se de fechar a porta, sendo já escuro, eles saíram; não sei para onde foram; ide após eles depressa, porque os alcançareis.
6 Ela, porém, os fizera subir ao eirado e os escondera entre as canas do linho que havia disposto em ordem no eirado.
7 Foram-se aqueles homens após os espias pelo caminho que dá aos vaus do Jordão; e, havendo saído os que iam após eles, fechou-se a porta.
8 Antes que os espias se deitassem, foi ela ter com eles ao eirado
9 e lhes disse: Bem sei que o Senhor vos deu esta terra, e que o pavor que infundis caiu sobre nós, e que todos os moradores da terra estão desmaiados.
10 Porque temos ouvido que o Senhor secou as águas do mar Vermelho diante de vós, quando saíeis do Egito; e também o que fizestes aos dois reis dos amorreus, Seom e Ogue, que estavam além do Jordão, os quais destruístes.
11 Ouvindo isto, desmaiou-nos o coração, e em ninguém mais há ânimo algum, por causa da vossa presença; porque o Senhor, vosso Deus, é Deus em cima nos céus e embaixo na terra.
12 Agora, pois, jurai-me, vos peço, pelo Senhor que, assim como usei de misericórdia para convosco, também dela usareis para com a casa de meu pai; e que me dareis um sinal certo
13 de que conservareis a vida a meu pai e a minha mãe, como também a meus irmãos e a minhas irmãs, com tudo o que têm, e de que livrareis a nossa vida da morte.
14 Então, lhe disseram os homens: A nossa vida responderá pela vossa se não denunciardes esta nossa missão; e será, pois, que, dando-nos o Senhor esta terra, usaremos contigo de misericórdia e de fidelidade.
15 Ela, então, os fez descer por uma corda pela janela, porque a casa em que residia estava sobre o muro da cidade.
16 E disse-lhes: Ide-vos ao monte, para que, porventura, vos não encontrem os perseguidores; escondei-vos lá três dias, até que eles voltem; e, depois, tomareis o vosso caminho.
17 Disseram-lhe os homens: Desobrigados seremos deste teu juramento que nos fizeste jurar,
18 se, vindo nós à terra, não atares este cordão de fio de escarlata à janela por onde nos fizeste descer; e se não recolheres em casa contigo teu pai, e tua mãe, e teus irmãos, e a toda a família de teu pai.
19 Qualquer que sair para fora da porta da tua casa, o seu sangue lhe cairá sobre a cabeça, e nós seremos inocentes; mas o sangue de qualquer que estiver contigo em casa caia sobre a nossa cabeça, se alguém nele puser mão.
20 Também, se tu denunciares esta nossa missão, seremos desobrigados do juramento que nos fizeste jurar.
21 E ela disse: Segundo as vossas palavras, assim seja. Então, os despediu; e eles se foram; e ela atou o cordão de escarlata à janela.
22 Foram-se, pois, e chegaram ao monte, e ali ficaram três dias, até que voltaram os perseguidores; porque os perseguidores os procuraram por todo o caminho, porém não os acharam.
23 Assim, os dois homens voltaram, e desceram do monte, e passaram, e vieram a Josué, filho de Num, e lhe contaram tudo quanto lhes acontecera;
24 e disseram a Josué: Certamente, o Senhor nos deu toda esta terra nas nossas mãos, e todos os seus moradores estão desmaiados diante de nós.*
1 Levantou-se, pois, Josué de madrugada, e, tendo ele e todos os filhos de Israel partido de Sitim, vieram até ao Jordão e pousaram ali antes que passassem.
2 Sucedeu, ao fim de três dias, que os oficiais passaram pelo meio do arraial
3 e ordenaram ao povo, dizendo: Quando virdes a arca da Aliança do Senhor, vosso Deus, e que os levitas sacerdotes a levam, partireis vós também do vosso lugar e a seguireis.
4 Contudo, haja a distância de cerca de dois mil côvados entre vós e ela. Não vos chegueis a ela, para que conheçais o caminho pelo qual haveis de ir, visto que, por tal caminho, nunca passastes antes.
5 Disse Josué ao povo: Santificai-vos, porque amanhã o Senhor fará maravilhas no meio de vós.
6 E também falou aos sacerdotes, dizendo: Levantai a arca da Aliança e passai adiante do povo. Levantaram, pois, a arca da Aliança e foram andando adiante do povo.
7 Então, disse o Senhor a Josué: Hoje, começarei a engrandecer-te perante os olhos de todo o Israel, para que saibam que, como fui com Moisés, assim serei contigo.
8 Tu, pois, ordenarás aos sacerdotes que levam a arca da Aliança, dizendo: Ao chegardes à borda das águas do Jordão, parareis aí.
9 Então, disse Josué aos filhos de Israel: Chegai-vos para cá e ouvi as palavras do Senhor, vosso Deus.
10 Disse mais Josué: Nisto conhecereis que o Deus vivo está no meio de vós e que de todo lançará de diante de vós os cananeus, os heteus, os heveus, os ferezeus, os girgaseus, os amorreus e os jebuseus.
11 Eis que a arca da Aliança do Senhor de toda a terra passa o Jordão diante de vós.
12 Tomai, pois, agora, doze homens das tribos de Israel, um de cada tribo;
13 porque há de acontecer que, assim que as plantas dos pés dos sacerdotes que levam a arca do Senhor, o Senhor de toda a terra, pousem nas águas do Jordão, serão elas cortadas, a saber, as que vêm de cima, e se amontoarão.
14 Tendo partido o povo das suas tendas, para passar o Jordão, levando os sacerdotes a arca da Aliança diante do povo;
15 e, quando os que levavam a arca chegaram até ao Jordão, e os seus pés se molharam na borda das águas (porque o Jordão transbordava sobre todas as suas ribanceiras, todos os dias da sega),
16 pararam-se as águas que vinham de cima; levantaram-se num montão, mui longe da cidade de Adã, que fica ao lado de Sartã; e as que desciam ao mar da Arabá, que é o mar Salgado, foram de todo cortadas; então, passou o povo defronte de Jericó.
17 Porém os sacerdotes que levavam a arca da Aliança do Senhor pararam firmes no meio do Jordão, e todo o Israel passou a pé enxuto, atravessando o Jordão.*
1 Tendo, pois, todo o povo passado o Jordão, falou o Senhor a Josué, dizendo:
2 Tomai do povo doze homens, um de cada tribo,
3 e ordenai-lhes, dizendo: Daqui do meio do Jordão, do lugar onde, parados, pousaram os sacerdotes os pés, tomai doze pedras; e levai-as convosco e depositai-as no alojamento em que haveis de passar esta noite.
4 Chamou, pois, Josué os doze homens que escolhera dos filhos de Israel,
5 um de cada tribo, e disse-lhes: Passai adiante da arca do Senhor, vosso Deus, ao meio do Jordão; e cada um levante sobre o ombro uma pedra, segundo o número das tribos dos filhos de Israel,
6 para que isto seja por sinal entre vós; e, quando vossos filhos, no futuro, perguntarem, dizendo: Que vos significam estas pedras?,
7 então, lhes direis que as águas do Jordão foram cortadas diante da arca da Aliança do Senhor; em passando ela, foram as águas do Jordão cortadas. Estas pedras serão, para sempre, por memorial aos filhos de Israel.
8 Fizeram, pois, os filhos de Israel como Josué ordenara, e levantaram doze pedras do meio do Jordão, como o Senhor tinha dito a Josué, segundo o número das tribos dos filhos de Israel, e levaram-nas consigo ao alojamento, e as depositaram ali.
9 Levantou Josué também doze pedras no meio do Jordão, no lugar em que, parados, pousaram os pés os sacerdotes que levavam a arca da Aliança; e ali estão até ao dia de hoje.
10 Porque os sacerdotes que levavam a arca haviam parado no meio do Jordão, em pé, até que se cumpriu tudo quanto o Senhor, por intermédio de Moisés, ordenara a Josué falasse ao povo; e o povo se apressou e passou.
11 Tendo passado todo o povo, então, passou a arca do Senhor, e os sacerdotes, à vista de todo o povo.
12 Passaram os filhos de Rúben, e os filhos de Gade, e a meia tribo de Manassés, armados, na frente dos filhos de Israel, como Moisés lhes tinha dito;
13 uns quarenta mil homens de guerra armados passaram diante do Senhor para a batalha, às campinas de Jericó.
14 Naquele dia, o Senhor engrandeceu a Josué na presença de todo o Israel; e respeitaram-no todos os dias da sua vida, como haviam respeitado a Moisés.
15 Disse, pois, o Senhor a Josué:
16 Dá ordem aos sacerdotes que levam a arca do Testemunho que subam do Jordão.
17 Então, ordenou Josué aos sacerdotes, dizendo: Subi do Jordão.
18 Ao subirem do meio do Jordão os sacerdotes que levavam a arca da Aliança do Senhor, e assim que as plantas dos seus pés se puseram na terra seca, as águas do Jordão se tornaram ao seu lugar e corriam, como dantes, sobre todas as suas ribanceiras.
19 Subiu, pois, do Jordão o povo no dia dez do primeiro mês; e acamparam-se em Gilgal, do lado oriental de Jericó.
20 As doze pedras que tiraram do Jordão, levantou-as Josué em coluna em Gilgal.
21 E disse aos filhos de Israel: Quando, no futuro, vossos filhos perguntarem a seus pais, dizendo: Que significam estas pedras?,
22 fareis saber a vossos filhos, dizendo: Israel passou em seco este Jordão.
23 Porque o Senhor, vosso Deus, fez secar as águas do Jordão diante de vós, até que passásseis, como o Senhor, vosso Deus, fez ao mar Vermelho, ao qual secou perante nós, até que passamos.
24 Para que todos os povos da terra conheçam que a mão do Senhor é forte, a fim de que temais ao Senhor, vosso Deus, todos os dias.*
1 Sucedeu que, ouvindo todos os reis dos amorreus que habitavam deste lado do Jordão, ao ocidente, e todos os reis dos cananeus que estavam ao pé do mar que o Senhor tinha secado as águas do Jordão, de diante dos filhos de Israel, até que passamos, desmaiou-se-lhes o coração, e não houve mais alento neles, por causa dos filhos de Israel.
2 Naquele tempo, disse o Senhor a Josué: Faze facas de pederneira e passa, de novo, a circuncidar os filhos de Israel.
3 Então, Josué fez para si facas de pederneira e circuncidou os filhos de Israel em Gibeate-Haralote.
4 Foi esta a razão por que Josué os circuncidou: todo o povo que tinha saído do Egito, os homens, todos os homens de guerra, eram já mortos no deserto, pelo caminho.
5 Porque todo o povo que saíra estava circuncidado, mas a nem um deles que nascera no deserto, pelo caminho, depois de terem saído do Egito, haviam circuncidado.
6 Porque quarenta anos andaram os filhos de Israel pelo deserto, até se acabar toda a gente dos homens de guerra que saíram do Egito, que não obedeceram à voz do Senhor, aos quais o Senhor tinha jurado que lhes não havia de deixar ver a terra que o Senhor, sob juramento, prometeu dar a seus pais, terra que mana leite e mel.
7 Porém em seu lugar pôs a seus filhos; a estes Josué circuncidou, porquanto estavam incircuncisos, porque os não circuncidaram no caminho.
8 Tendo sido circuncidada toda a nação, ficaram no seu lugar no arraial, até que sararam.
9 Disse mais o Senhor a Josué: Hoje, removi de vós o opróbrio do Egito; pelo que o nome daquele lugar se chamou Gilgal até o dia de hoje.
10 Estando, pois, os filhos de Israel acampados em Gilgal, celebraram a Páscoa no dia catorze do mês, à tarde, nas campinas de Jericó.
11 Comeram do fruto da terra, no dia seguinte à Páscoa; pães asmos e cereais tostados comeram nesse mesmo dia.
12 No dia imediato, depois que comeram do produto da terra, cessou o maná, e não o tiveram mais os filhos de Israel; mas, naquele ano, comeram das novidades da terra de Canaã.
13 Estando Josué ao pé de Jericó, levantou os olhos e olhou; eis que se achava em pé diante dele um homem que trazia na mão uma espada nua; chegou-se Josué a ele e disse-lhe: És tu dos nossos ou dos nossos adversários?
14 Respondeu ele: Não; sou príncipe do exército do Senhor e acabo de chegar. Então, Josué se prostrou com o rosto em terra, e o adorou, e disse-lhe: Que diz meu senhor ao seu servo?
15 Respondeu o príncipe do exército do Senhor a Josué: Descalça as sandálias dos pés, porque o lugar em que estás é santo. E fez Josué assim.*
1 Ora, Jericó estava rigorosamente fechada por causa dos filhos de Israel; ninguém saía, nem entrava.
2 Então, disse o Senhor a Josué: Olha, entreguei na tua mão Jericó, o seu rei e os seus valentes.
3 Vós, pois, todos os homens de guerra, rodeareis a cidade, cercando-a uma vez; assim fareis por seis dias.
4 Sete sacerdotes levarão sete trombetas de chifre de carneiro adiante da arca; no sétimo dia, rodeareis a cidade sete vezes, e os sacerdotes tocarão as trombetas.
5 E será que, tocando-se longamente a trombeta de chifre de carneiro, ouvindo vós o sonido dela, todo o povo gritará com grande grita; o muro da cidade cairá abaixo, e o povo subirá nele, cada qual em frente de si.
6 Então, Josué, filho de Num, chamou os sacerdotes e disse-lhes: Levai a arca da Aliança; e sete sacerdotes levem sete trombetas de chifre de carneiro adiante da arca do Senhor.
7 E disse ao povo: Passai e rodeai a cidade; e quem estiver armado passe adiante da arca do Senhor.
8 Assim foi que, como Josué dissera ao povo, os sete sacerdotes, com as sete trombetas de chifre de carneiro diante do Senhor, passaram e tocaram as trombetas; e a arca da Aliança do Senhor os seguia.
9 Os homens armados iam adiante dos sacerdotes que tocavam as trombetas; a retaguarda seguia após a arca, e as trombetas soavam continuamente.
10 Porém ao povo ordenara Josué, dizendo: Não gritareis, nem fareis ouvir a vossa voz, nem sairá palavra alguma da vossa boca, até ao dia em que eu vos diga: gritai! Então, gritareis.
11 Assim, a arca do Senhor rodeou a cidade, contornando-a uma vez. Entraram no arraial e ali pernoitaram.
12 Levantando-se Josué de madrugada, os sacerdotes levaram, de novo, a arca do Senhor.
13 Os sete sacerdotes que levavam as sete trombetas de chifre de carneiro diante da arca do Senhor iam tocando continuamente; os homens armados iam adiante deles, e a retaguarda seguia após a arca do Senhor, enquanto as trombetas soavam continuamente.
14 No segundo dia, rodearam, outra vez, a cidade e tornaram para o arraial; e assim fizeram por seis dias.
15 No sétimo dia, madrugaram ao subir da alva e, da mesma sorte, rodearam a cidade sete vezes; somente naquele dia rodearam a cidade sete vezes.
16 E sucedeu que, na sétima vez, quando os sacerdotes tocavam as trombetas, disse Josué ao povo: Gritai, porque o Senhor vos entregou a cidade!
17 Porém a cidade será condenada, ela e tudo quanto nela houver; somente viverá Raabe, a prostituta, e todos os que estiverem com ela em casa, porquanto escondeu os mensageiros que enviamos.
18 Tão somente guardai-vos das coisas condenadas, para que, tendo-as vós condenado, não as tomeis; e assim torneis maldito o arraial de Israel e o confundais.
19 Porém toda prata, e ouro, e utensílios de bronze e de ferro são consagrados ao Senhor; irão para o seu tesouro.
20 Gritou, pois, o povo, e os sacerdotes tocaram as trombetas. Tendo ouvido o povo o sonido da trombeta e levantado grande grito, ruíram as muralhas, e o povo subiu à cidade, cada qual em frente de si, e a tomaram.
21 Tudo quanto na cidade havia destruíram totalmente a fio de espada, tanto homens como mulheres, tanto meninos como velhos, também bois, ovelhas e jumentos.
22 Então, disse Josué aos dois homens que espiaram a terra: Entrai na casa da mulher prostituta e tirai-a de lá com tudo quanto tiver, como lhe jurastes.
23 Então, entraram os jovens, os espias, e tiraram Raabe, e seu pai, e sua mãe, e seus irmãos, e tudo quanto tinha; tiraram também toda a sua parentela e os acamparam fora do arraial de Israel.
24 Porém a cidade e tudo quanto havia nela, queimaram-no; tão somente a prata, o ouro e os utensílios de bronze e de ferro deram para o tesouro da Casa do Senhor.
25 Mas Josué conservou com vida a prostituta Raabe, e a casa de seu pai, e tudo quanto tinha; e habitou no meio de Israel até ao dia de hoje, porquanto escondera os mensageiros que Josué enviara a espiar Jericó.
26 Naquele tempo, Josué fez o povo jurar e dizer: Maldito diante do Senhor seja o homem que se levantar e reedificar esta cidade de Jericó; com a perda do seu primogênito lhe porá os fundamentos e, à custa do mais novo, as portas.
27 Assim, era o Senhor com Josué; e corria a sua fama por toda a terra.*
1 Prevaricaram os filhos de Israel nas coisas condenadas; porque Acã, filho de Carmi, filho de Zabdi, filho de Zera, da tribo de Judá, tomou das coisas condenadas. A ira do Senhor se acendeu contra os filhos de Israel.
2 Enviando, pois, Josué, de Jericó, alguns homens a Ai, que está junto a Bete-Áven, ao oriente de Betel, falou-lhes, dizendo: Subi e espiai a terra. Subiram, pois, aqueles homens e espiaram Ai.
3 E voltaram a Josué e lhe disseram: Não suba todo o povo; subam uns dois ou três mil homens, a ferir Ai; não fatigueis ali todo o povo, porque são poucos os inimigos.
4 Assim, subiram lá do povo uns três mil homens, os quais fugiram diante dos homens de Ai.
5 Os homens de Ai feriram deles uns trinta e seis, e aos outros perseguiram desde a porta até às pedreiras, e os derrotaram na descida; e o coração do povo se derreteu e se tornou como água.
6 Então, Josué rasgou as suas vestes e se prostrou em terra sobre o rosto perante a arca do Senhor até à tarde, ele e os anciãos de Israel; e deitaram pó sobre a cabeça.
7 Disse Josué: Ah! Senhor Deus, por que fizeste este povo passar o Jordão, para nos entregares nas mãos dos amorreus, para nos fazerem perecer? Tomara nos contentáramos com ficarmos dalém do Jordão.
8 Ah! Senhor, que direi? Pois Israel virou as costas diante dos seus inimigos!
9 Ouvindo isto os cananeus e todos os moradores da terra, nos cercarão e desarraigarão o nosso nome da terra; e, então, que farás ao teu grande nome?
10 Então, disse o Senhor a Josué: Levanta-te! Por que estás prostrado assim sobre o rosto?
11 Israel pecou, e violaram a minha aliança, aquilo que eu lhes ordenara, pois tomaram das coisas condenadas, e furtaram, e dissimularam, e até debaixo da sua bagagem o puseram.
12 Pelo que os filhos de Israel não puderam resistir aos seus inimigos; viraram as costas diante deles, porquanto Israel se fizera condenado; já não serei convosco, se não eliminardes do vosso meio a coisa roubada.
13 Dispõe-te, santifica o povo e dize: Santificai-vos para amanhã, porque assim diz o Senhor, Deus de Israel: Há coisas condenadas no vosso meio, ó Israel; aos vossos inimigos não podereis resistir, enquanto não eliminardes do vosso meio as coisas condenadas.
14 Pela manhã, pois, vos chegareis, segundo as vossas tribos; e será que a tribo que o Senhor designar por sorte se chegará, segundo as famílias; e a família que o Senhor designar se chegará por casas; e a casa que o Senhor designar se chegará homem por homem.
15 Aquele que for achado com a coisa condenada será queimado, ele e tudo quanto tiver, porquanto violou a aliança do Senhor e fez loucura em Israel.
16 Então, Josué se levantou de madrugada e fez chegar a Israel, segundo as suas tribos; e caiu a sorte sobre a tribo de Judá.
17 Fazendo chegar a tribo de Judá, caiu sobre a família dos zeraítas; fazendo chegar a família dos zeraítas, homem por homem, caiu sobre Zabdi;
18 e, fazendo chegar a sua casa, homem por homem, caiu sobre Acã, filho de Carmi, filho de Zabdi, filho de Zera, da tribo de Judá.
19 Então, disse Josué a Acã: Filho meu, dá glória ao Senhor, Deus de Israel, e a ele rende louvores; e declara-me, agora, o que fizeste; não mo ocultes.
20 Respondeu Acã a Josué e disse: Verdadeiramente, pequei contra o Senhor, Deus de Israel, e fiz assim e assim.
21 Quando vi entre os despojos uma boa capa babilônica, e duzentos siclos de prata, e uma barra de ouro do peso de cinquenta siclos, cobicei-os e tomei-os; e eis que estão escondidos na terra, no meio da minha tenda, e a prata, por baixo.
22 Então, Josué enviou mensageiros que foram correndo à tenda; e eis que tudo estava escondido nela, e a prata, por baixo.
23 Tomaram, pois, aquelas coisas do meio da tenda, e as trouxeram a Josué e a todos os filhos de Israel, e as colocaram perante o Senhor.
24 Então, Josué e todo o Israel com ele tomaram Acã, filho de Zera, e a prata, e a capa, e a barra de ouro, e seus filhos, e suas filhas, e seus bois, e seus jumentos, e suas ovelhas, e sua tenda, e tudo quanto tinha e levaram-nos ao vale de Acor.
25 Disse Josué: Por que nos conturbaste? O Senhor, hoje, te conturbará. E todo o Israel o apedrejou; e, depois de apedrejá-los, queimou-os.
26 E levantaram sobre ele um montão de pedras, que permanece até ao dia de hoje; assim, o Senhor apagou o furor da sua ira; pelo que aquele lugar se chama o vale de Acor até ao dia de hoje.*
1 Disse o Senhor a Josué: Não temas, não te atemorizes; toma contigo toda a gente de guerra, e dispõe-te, e sobe a Ai; olha que entreguei nas tuas mãos o rei de Ai, e o seu povo, e a sua cidade, e a sua terra.
2 Farás a Ai e a seu rei como fizeste a Jericó e a seu rei; somente que para vós outros saqueareis os seus despojos e o seu gado; põe emboscadas à cidade, por detrás dela.
3 Então, Josué se levantou, e toda a gente de guerra, para subir contra Ai; escolheu Josué trinta mil homens valentes e os enviou de noite.
4 Deu-lhes ordem, dizendo: Eis que vos poreis de emboscada contra a cidade, por detrás dela; não vos distancieis muito da cidade; e todos estareis alertas.
5 Porém eu e todo o povo que está comigo nos aproximaremos da cidade; e será que, quando saírem, como dantes, contra nós, fugiremos diante deles.
6 Deixemo-los, pois, sair atrás de nós, até que os tiremos da cidade; porque dirão: Fogem diante de nós como dantes. Assim, fugiremos diante deles.
7 Então, saireis vós da emboscada e tomareis a cidade; porque o Senhor, vosso Deus, vo-la entregará nas vossas mãos.
8 Havendo vós tomado a cidade, pôr-lhe-eis fogo; segundo a palavra do Senhor, fareis; eis que vo-lo ordenei.
9 Assim, Josué os enviou, e eles se foram à emboscada; e ficaram entre Betel e Ai, ao ocidente de Ai; porém Josué passou aquela noite no meio do povo.
10 Levantou-se Josué de madrugada, passou revista ao povo, e subiram ele e os anciãos de Israel, diante do povo, contra Ai.
11 Subiram também todos os homens de guerra que estavam com ele, e chegaram-se, e vieram defronte da cidade; e alojaram-se do lado norte de Ai. Havia um vale entre eles e Ai.
12 Tomou também uns cinco mil homens e os pôs entre Betel e Ai, em emboscada, ao ocidente da cidade.
13 Assim foi posto o povo: todo o acampamento ao norte da cidade e a emboscada ao ocidente dela; e foi Josué aquela noite até ao meio do vale.
14 E sucedeu que, vendo-o o rei de Ai, ele e os homens da cidade apressaram-se e, levantando-se de madrugada, saíram de encontro a Israel, à batalha, defronte das campinas, porque ele não sabia achar-se contra ele uma emboscada atrás da cidade.
15 Josué, pois, e todo o Israel se houveram como feridos diante deles e fugiram pelo caminho do deserto.
16 Pelo que todo o povo que estava na cidade foi convocado para os perseguir; e perseguiram Josué e foram afastados da cidade.
17 Nem um só homem ficou em Ai, nem em Betel que não saísse após os israelitas; e deixaram a cidade aberta e perseguiram Israel.
18 Então, disse o Senhor a Josué: Estende para Ai a lança que tens na mão; porque a esta darei na tua mão; e Josué estendeu para a cidade a lança que tinha na mão.
19 Então, a emboscada se levantou apressadamente do seu lugar, e, ao estender ele a mão, vieram à cidade e a tomaram; e apressaram-se e nela puseram fogo.
20 Virando-se os homens de Ai para trás, olharam, e eis que a fumaça da cidade subia ao céu, e não puderam fugir nem para um lado nem para outro; porque o povo que fugia para o deserto se tornou contra os que os perseguiam.
21 Vendo Josué e todo o Israel que a emboscada tomara a cidade e que a fumaça da cidade subia, voltaram e feriram os homens de Ai.
22 Da cidade saíram os outros ao encontro do inimigo, que, assim, ficou no meio de Israel, uns de uma parte, outros de outra; e feriram-nos de tal sorte, que nenhum deles sobreviveu, nem escapou.
23 Porém ao rei de Ai tomaram vivo e o trouxeram a Josué.
24 Tendo os israelitas acabado de matar todos os moradores de Ai no campo e no deserto onde os tinham perseguido, e havendo todos caído a fio de espada, e sendo já todos consumidos, todo o Israel voltou a Ai, e a passaram a fio de espada.
25 Os que caíram aquele dia, tanto homens como mulheres, foram doze mil, todos os moradores de Ai.
26 Porque Josué não retirou a mão que estendera com a lança até haver destruído totalmente os moradores de Ai.
27 Os israelitas saquearam, entretanto, para si o gado e os despojos daquela cidade, segundo a palavra do Senhor, que ordenara a Josué.
28 Então, Josué pôs fogo a Ai e a reduziu, para sempre, a um montão, a ruínas até ao dia de hoje.
29 Ao rei de Ai, enforcou-o e o deixou no madeiro até à tarde; ao pôr do sol, por ordem de Josué, tiraram do madeiro o cadáver, e o lançaram à porta da cidade, e sobre ele levantaram um montão de pedras, que até hoje permanece.
30 Então, Josué edificou um altar ao Senhor, Deus de Israel, no monte Ebal,
31 como Moisés, servo do Senhor, ordenara aos filhos de Israel, segundo o que está escrito no Livro da Lei de Moisés, a saber, um altar de pedras toscas, sobre o qual se não manejara instrumento de ferro; sobre ele ofereceram holocaustos ao Senhor e apresentaram ofertas pacíficas.
32 Escreveu, ali, em pedras, uma cópia da lei de Moisés, que já este havia escrito diante dos filhos de Israel.
33 Todo o Israel, com os seus anciãos, e os seus príncipes, e os seus juízes estavam de um e de outro lado da arca, perante os levitas sacerdotes que levavam a arca da Aliança do Senhor, tanto estrangeiros como naturais; metade deles, em frente do monte Gerizim, e a outra metade, em frente do monte Ebal; como Moisés, servo do Senhor, outrora, ordenara que fosse abençoado o povo de Israel.
34 Depois, leu todas as palavras da lei, a bênção e a maldição, segundo tudo o que está escrito no Livro da Lei.
35 Palavra nenhuma houve, de tudo o que Moisés ordenara, que Josué não lesse para toda a congregação de Israel, e para as mulheres, e os meninos, e os estrangeiros que andavam no meio deles.*
1 Sucedeu que, ouvindo isto todos os reis que estavam daquém do Jordão, nas montanhas, e nas campinas, em toda a costa do mar Grande, defronte do Líbano, os heteus, os amorreus, os cananeus, os ferezeus, os heveus e os jebuseus,
2 se ajuntaram eles de comum acordo, para pelejar contra Josué e contra Israel.
3 Os moradores de Gibeão, porém, ouvindo o que Josué fizera com Jericó e com Ai,
4 usaram de estratagema, e foram, e se fingiram embaixadores, e levaram sacos velhos sobre os seus jumentos e odres de vinho, velhos, rotos e consertados;
5 e, nos pés, sandálias velhas e remendadas e roupas velhas sobre si; e todo o pão que traziam para o caminho era seco e bolorento.
6 Foram ter com Josué, ao arraial, a Gilgal, e lhe disseram, a ele e aos homens de Israel: Chegamos de uma terra distante; fazei, pois, agora, aliança conosco.
7 E os homens de Israel responderam aos heveus: Porventura, habitais no meio de nós; como, pois, faremos aliança convosco?
8 Então, disseram a Josué: Somos teus servos. Então, lhes perguntou Josué: Quem sois vós? Donde vindes?
9 Responderam-lhe: Teus servos vieram de uma terra mui distante, por causa do nome do Senhor, teu Deus; porquanto ouvimos a sua fama e tudo quanto fez no Egito;
10 e tudo quanto fez aos dois reis dos amorreus que estavam dalém do Jordão, Seom, rei de Hesbom, e Ogue, rei de Basã, que estava em Astarote.
11 Pelo que nossos anciãos e todos os moradores da nossa terra nos disseram: Tomai convosco provisão alimentar para o caminho, e ide ao encontro deles, e dizei-lhes: Somos vossos servos; fazei, pois, agora, aliança conosco.
12 Este nosso pão tomamos quente das nossas casas, no dia em que saímos para vir ter convosco; e ei-lo aqui, agora, já seco e bolorento;
13 e estes odres eram novos quando os enchemos de vinho; e ei-los aqui já rotos; e estas nossas vestes e estas nossas sandálias já envelheceram, por causa do mui longo caminho.
14 Então, os israelitas tomaram da provisão e não pediram conselho ao Senhor.
15 Josué concedeu-lhes paz e fez com eles a aliança de lhes conservar a vida; e os príncipes da congregação lhes prestaram juramento.
16 Ao cabo de três dias, depois de terem feito a aliança com eles, ouviram que eram seus vizinhos e que moravam no meio deles.
17 Pois, partindo os filhos de Israel, chegaram às cidades deles ao terceiro dia; suas cidades eram Gibeão, Cefira, Beerote e Quiriate-Jearim.
18 Os filhos de Israel não os feriram, porquanto os príncipes da congregação lhes juraram pelo Senhor, Deus de Israel; pelo que toda a congregação murmurou contra os príncipes.
19 Então, todos os príncipes disseram a toda a congregação: Nós lhes juramos pelo Senhor, Deus de Israel; por isso, não podemos tocar-lhes.
20 Isto, porém, lhes faremos: Conservar-lhes-emos a vida, para que não haja grande ira sobre nós, por causa do juramento que já lhes fizemos.
21 Disseram-lhes, pois, os príncipes: Vivam. E se tornaram rachadores de lenha e tiradores de água para toda a congregação, como os príncipes lhes haviam dito.
22 Chamou-os Josué e disse-lhes: Por que nos enganastes, dizendo: Habitamos mui longe de vós, sendo que viveis em nosso meio?
23 Agora, pois, sois malditos; e dentre vós nunca deixará de haver escravos, rachadores de lenha e tiradores de água para a casa do meu Deus.
24 Então, responderam a Josué: É que se anunciou aos teus servos, como certo, que o Senhor, teu Deus, ordenara a seu servo Moisés que vos desse toda esta terra e destruísse todos os moradores dela diante de vós. Por isso, tememos muito por nossa vida por causa de vós e fizemos assim.
25 Eis que estamos na tua mão; trata-nos segundo te parecer bom e reto.
26 Assim lhes fez e livrou-os das mãos dos filhos de Israel; e não os mataram.
27 Naquele dia, Josué os fez rachadores de lenha e tiradores de água para a congregação e para o altar do Senhor, até ao dia de hoje, no lugar que Deus escolhesse.*
1 Tendo Adoni-Zedeque, rei de Jerusalém, ouvido que Josué tomara a Ai e a havia destruído totalmente e feito a Ai e ao seu rei como fizera a Jericó e ao seu rei e que os moradores de Gibeão fizeram paz com os israelitas e estavam no meio deles,
2 temeu muito; porque Gibeão era cidade grande como uma das cidades reais e ainda maior do que Ai, e todos os seus homens eram valentes.
3 Pelo que Adoni-Zedeque, rei de Jerusalém, enviou mensageiros a Hoão, rei de Hebrom, e a Pirã, rei de Jarmute, e a Jafia, rei de Laquis, e a Debir, rei de Eglom, dizendo:
4 Subi a mim e ajudai-me; firamos Gibeão, porquanto fez paz com Josué e com os filhos de Israel.
5 Então, se ajuntaram e subiram cinco reis dos amorreus, o rei de Jerusalém, o rei de Hebrom, o rei de Jarmute, o rei de Laquis e o rei de Eglom, eles e todas as suas tropas; e se acamparam junto a Gibeão e pelejaram contra ela.
6 Os homens de Gibeão mandaram dizer a Josué, no arraial de Gilgal: Não retires as tuas mãos de teus servos; sobe apressadamente a nós, e livra-nos, e ajuda-nos, pois todos os reis dos amorreus que habitam nas montanhas se ajuntaram contra nós.
7 Então, subiu Josué de Gilgal, ele e toda a gente de guerra com ele e todos os valentes.
8 Disse o Senhor a Josué: Não os temas, porque nas tuas mãos os entreguei; nenhum deles te poderá resistir.
9 Josué lhes sobreveio de repente, porque toda a noite veio subindo desde Gilgal.
10 O Senhor os conturbou diante de Israel, e os feriu com grande matança em Gibeão, e os foi perseguindo pelo caminho que sobe a Bete-Horom, e os derrotou até Azeca e Maquedá.
11 Sucedeu que, fugindo eles de diante de Israel, à descida de Bete-Horom, fez o Senhor cair do céu sobre eles grandes pedras, até Azeca, e morreram. Mais foram os que morreram pela chuva de pedra do que os mortos à espada pelos filhos de Israel.
12 Então, Josué falou ao Senhor, no dia em que o Senhor entregou os amorreus nas mãos dos filhos de Israel; e disse na presença dos israelitas: Sol, detém-te em Gibeão, e tu, lua, no vale de Aijalom.
13 E o sol se deteve, e a lua parou até que o povo se vingou de seus inimigos. Não está isto escrito no Livro dos Justos? O sol, pois, se deteve no meio do céu e não se apressou a pôr-se, quase um dia inteiro.
14 Não houve dia semelhante a este, nem antes nem depois dele, tendo o Senhor, assim, atendido à voz de um homem; porque o Senhor pelejava por Israel.
15 Voltou Josué, e todo o Israel com ele, ao arraial, a Gilgal.
16 Aqueles cinco reis, porém, fugiram e se esconderam numa cova em Maquedá.
17 E anunciaram a Josué: Foram achados os cinco reis escondidos numa cova em Maquedá.
18 Disse, pois, Josué: Rolai grandes pedras à boca da cova e ponde junto a ela homens que os guardem; porém vós não vos detenhais;
19 persegui os vossos inimigos e matai os que vão ficando atrás; não os deixeis entrar nas suas cidades, porque o Senhor, vosso Deus, já vo-los entregou nas vossas mãos.
20 Tendo Josué e os filhos de Israel acabado de os ferir com mui grande matança, até consumi-los, e tendo os restantes que deles ficaram entrado nas cidades fortificadas,
21 voltou todo o povo em paz ao acampamento a Josué, em Maquedá; não havendo ninguém que movesse a língua contra os filhos de Israel.
22 Depois, disse Josué: Abri a boca da cova e dali trazei-me aqueles cinco reis.
23 Fizeram, pois, assim e da cova lhe trouxeram os cinco reis: o rei de Jerusalém, o de Hebrom, o de Jarmute, o de Laquis e o de Eglom.
24 Trazidos os reis a Josué, chamou este todos os homens de Israel e disse aos capitães do exército que tinham ido com ele: Chegai, ponde o pé sobre o pescoço destes reis. E chegaram e puseram os pés sobre os pescoços deles.
25 Então, Josué lhes disse: Não temais, nem vos atemorizeis; sede fortes e corajosos, porque assim fará o Senhor a todos os vossos inimigos, contra os quais pelejardes.
26 Depois disto, Josué, ferindo-os, os matou e os pendurou em cinco madeiros; e ficaram eles pendentes dos madeiros até à tarde.
27 Ao pôr do sol, deu Josué ordem que os tirassem dos madeiros; e lançaram-nos na cova onde se tinham escondido e, na boca da cova, puseram grandes pedras que ainda lá se encontram até ao dia de hoje.
28 No mesmo dia, tomou Josué a Maquedá e a feriu à espada, bem como ao seu rei; destruiu-os totalmente e a todos os que nela estavam, sem deixar nem sequer um. Fez ao rei de Maquedá como fizera ao rei de Jericó.
29 Então, Josué, e todo o Israel com ele, passou de Maquedá a Libna e pelejou contra ela.
30 E o Senhor a deu nas mãos de Israel, a ela e ao seu rei, e a feriu à espada, a ela e todos os que nela estavam, sem deixar nem sequer um. Fez ao seu rei como fizera ao rei de Jericó.
31 Então, Josué, e todo o Israel com ele, passou de Libna a Laquis, sitiou-a e pelejou contra ela;
32 e o Senhor deu Laquis nas mãos de Israel, que, no dia seguinte, a tomou e a feriu à espada, a ela e todos os que nela estavam, conforme tudo o que fizera a Libna.
33 Então, Hoão, rei de Gezer, subiu para ajudar Laquis; porém Josué o feriu, a ele e o seu povo, sem deixar nem sequer um.
34 E Josué, e todo o Israel com ele, passou de Laquis a Eglom, e a sitiaram e pelejaram contra ela;
35 e, no mesmo dia, a tomaram e a feriram à espada; e totalmente destruíram os que nela estavam, conforme tudo o que fizeram a Laquis.
36 Depois, Josué, e todo o Israel com ele, subiu de Eglom a Hebrom, e pelejaram contra ela;
37 e a tomaram e a feriram à espada, tanto o seu rei como todas as suas cidades e todos os que nelas estavam, sem deixar nem sequer um, conforme tudo o que fizeram a Eglom; e Josué executou a condenação contra ela e contra todos os que nela estavam.
38 Então, Josué, e todo o Israel com ele, voltou a Debir e pelejou contra ela;
39 e tomou-a com o seu rei e todas as suas cidades e as feriu à espada; todos os que nelas estavam, destruiu-os totalmente sem deixar nem sequer um; como fizera a Hebrom, a Libna e a seu rei, também fez a Debir e a seu rei.
40 Assim, feriu Josué toda aquela terra, a região montanhosa, o Neguebe, as campinas, as descidas das águas e todos os seus reis; destruiu tudo o que tinha fôlego, sem deixar nem sequer um, como ordenara o Senhor, Deus de Israel.
41 Feriu-os Josué desde Cades-Barneia até Gaza, como também toda a terra de Gósen até Gibeão.
42 E, de uma vez, tomou Josué todos estes reis e as suas terras, porquanto o Senhor, Deus de Israel, pelejava por Israel.
43 Então, Josué, e todo o Israel com ele, voltou ao arraial em Gilgal.*
1 Tendo Jabim, rei de Hazor, ouvido isto, enviou mensageiros a Jobabe, rei de Madom, e ao rei Sinrom, e ao rei Acsafe,
2 e aos reis que estavam ao norte, na região montanhosa, na Arabá, ao sul de Quinerete, nas planícies e nos planaltos de Dor, do lado do mar,
3 aos cananeus do oriente e do ocidente: aos amorreus, aos heteus, aos ferezeus, aos jebuseus nas montanhas e aos heveus ao pé do Hermom, na terra de Mispa.
4 Saíram, pois, estes e todas as suas tropas com eles, muito povo, em multidão como a areia que está na praia do mar, e muitíssimos cavalos e carros.
5 Todos estes reis se ajuntaram, e vieram, e se acamparam junto às águas de Merom, para pelejarem contra Israel.
6 Disse o Senhor a Josué: Não temas diante deles, porque amanhã, a esta mesma hora, já os terás traspassado diante dos filhos de Israel; os seus cavalos jarretarás e queimarás os seus carros.
7 Josué, e todos os homens de guerra com ele, veio apressadamente contra eles às águas de Merom, e os atacaram.
8 O Senhor os entregou nas mãos de Israel; e os feriram e os perseguiram até à grande Sidom, e até Misrefote-Maim, e até ao vale de Mispa, ao oriente; feriram-nos sem deixar nem sequer um.
9 Fez-lhes Josué como o Senhor lhe dissera; os seus cavalos jarretou e os seus carros queimou.
10 Nesse mesmo tempo, voltou Josué, tomou a Hazor e feriu à espada o seu rei, porquanto Hazor, dantes, era a capital de todos estes reinos.
11 A todos os que nela estavam feriram à espada e totalmente os destruíram, e ninguém sobreviveu; e a Hazor queimou.
12 Josué tomou todas as cidades desses reis e também a eles e os feriu à espada, destruindo-os totalmente, como ordenara Moisés, servo do Senhor.
13 Tão somente não queimaram os israelitas as cidades que estavam sobre os outeiros, exceto Hazor, a qual Josué queimou.
14 E a todos os despojos destas cidades e ao gado os filhos de Israel saquearam para si; porém a todos os homens feriram à espada, até que os destruíram; e ninguém sobreviveu.
15 Como ordenara o Senhor a Moisés, seu servo, assim Moisés ordenou a Josué; e assim Josué o fez; nem uma só palavra deixou de cumprir de tudo o que o Senhor ordenara a Moisés.
16 Tomou, pois, Josué toda aquela terra, a saber, a região montanhosa, todo o Neguebe, toda a terra de Gósen, as planícies, a Arabá e a região montanhosa de Israel com suas planícies;
17 desde o monte Halaque, que sobe a Seir, até Baal-Gade, no vale do Líbano, ao pé do monte Hermom; também tomou todos os seus reis, e os feriu, e os matou.
18 Por muito tempo, Josué fez guerra contra todos estes reis.
19 Não houve cidade que fizesse paz com os filhos de Israel, senão os heveus, moradores de Gibeão; por meio de guerra, as tomaram todas.
20 Porquanto do Senhor vinha o endurecimento do seu coração para saírem à guerra contra Israel, a fim de que fossem totalmente destruídos e não lograssem piedade alguma; antes, fossem de todo destruídos, como o Senhor tinha ordenado a Moisés.
21 Naquele tempo, veio Josué e eliminou os anaquins da região montanhosa, de Hebrom, de Debir, de Anabe, e de todas as montanhas de Judá, e de todas as montanhas de Israel; Josué os destruiu totalmente com as suas cidades.
22 Nem um dos anaquins sobreviveu na terra dos filhos de Israel; somente em Gaza, em Gate e em Asdode alguns subsistiram.
23 Assim, tomou Josué toda esta terra, segundo tudo o que o Senhor tinha dito a Moisés; e Josué a deu em herança aos filhos de Israel, conforme as suas divisões e tribos; e a terra repousou da guerra.*
1 São estes os reis da terra, aos quais os filhos de Israel feriram, de cujas terras se apossaram dalém do Jordão para o nascente, desde o ribeiro de Arnom até ao monte Hermom e toda a planície do oriente:
2 Seom, rei dos amorreus, que habitava em Hesbom e dominava desde Aroer, que está à beira do vale de Arnom, e desde o meio do vale e a metade de Gileade até ao ribeiro de Jaboque, limite dos filhos de Amom;
3 desde a campina até ao mar de Quinerete, para o oriente, e até ao mar da Campina, o mar Salgado, para o oriente, pelo caminho de Bete-Jesimote; e desde o sul abaixo de Asdote-Pisga.
4 Como também o limite de Ogue, rei de Basã, que havia ficado dos refains e que habitava em Astarote e em Edrei;
5 e dominava no monte Hermom, e em Salca, e em toda a Basã, até ao limite dos gesuritas e dos maacatitas, e metade de Gileade, limite de Seom, rei de Hesbom.
6 Moisés, servo do Senhor, e os filhos de Israel feriram a estes; e Moisés, servo do Senhor, deu esta terra em possessão aos rubenitas, aos gaditas e à meia tribo de Manassés.
7 São estes os reis da terra aos quais Josué e os filhos de Israel feriram daquém do Jordão, para o ocidente, desde Baal-Gade, no vale do Líbano, até ao monte Halaque, que sobe a Seir, e cuja terra Josué deu em possessão às tribos de Israel, segundo as suas divisões,
8 a saber, o que havia na região montanhosa, nas planícies, na Arabá, nas descidas das águas, no deserto e no Neguebe, onde estava o heteu, o amorreu, o cananeu, o ferezeu, o heveu e o jebuseu:
9 o rei de Jericó, um; o de Ai, que está ao lado de Betel, outro;
10 o rei de Jerusalém, outro; o rei de Hebrom, outro;
11 o rei de Jarmute, outro; o de Laquis, outro;
12 o rei de Eglom, outro; o de Gezer, outro;
13 o rei de Debir, outro; o de Geder, outro;
14 o rei de Horma, outro; o de Arade, outro;
15 o rei de Libna, outro; o de Adulão, outro;
16 o rei de Maquedá, outro; o de Betel, outro;
17 o rei de Tapua, outro; o de Héfer, outro;
18 o rei de Afeca, outro; o de Lasarom, outro;
19 o rei de Madom, outro; o de Hazor, outro;
20 o rei de Sinrom-Merom, outro; o de Acsafe, outro;
21 o rei de Taanaque, outro; o de Megido, outro;
22 o rei de Quedes, outro; o de Jocneão do Carmelo, outro;
23 o rei de Dor, em Nafate-Dor, outro; o de Goim, em Gilgal, outro;
24 o rei de Tirza, outro; ao todo, trinta e um reis.*
1 Era Josué, porém, já idoso, entrado em dias; e disse-lhe o Senhor: Já estás velho, entrado em dias, e ainda muitíssima terra ficou para se possuir.
2 Esta é a terra ainda não conquistada: todas as regiões dos filisteus e toda a Gesur;
3 desde Sior, que está defronte do Egito, até ao limite de Ecrom, para o norte, que se considera como dos cananeus; cinco príncipes dos filisteus: o de Gaza, o de Asdode, o de Asquelom, o de Gate e o de Ecrom;
4 ao sul, os aveus, também toda a terra dos cananeus e Meara, que é dos sidônios, até Afeca, ao limite dos amorreus;
5 e ainda a terra dos gibleus e todo o Líbano, para o nascente do sol, desde Baal-Gade, ao pé do monte Hermom, até à entrada de Hamate;
6 todos os que habitam nas montanhas desde o Líbano até Misrefote-Maim, todos os sidônios; eu os lançarei de diante dos filhos de Israel; reparte, pois, a terra por herança a Israel, como te ordenei.
7 Distribui, pois, agora, a terra por herança às nove tribos e à meia tribo de Manassés.
8 Com a outra meia tribo, os rubenitas e os gaditas já receberam a sua herança dalém do Jordão, para o oriente, como já lhes tinha dado Moisés, servo do Senhor.
9 Começando com Aroer, que está à borda do vale de Arnom, mais a cidade que está no meio do vale, todo o planalto de Medeba até Dibom;
10 e todas as cidades de Seom, rei dos amorreus, que reinou em Hesbom, até ao limite dos filhos de Amom.
11 E Gileade, e o limite dos gesuritas, e o dos maacatitas, e todo o monte Hermom, e toda a Basã até Salca;
12 todo o reino de Ogue, em Basã, que reinou em Astarote e em Edrei, que ficou do resto dos gigantes, o qual Moisés feriu e expulsou.
13 Porém os filhos de Israel não desapossaram os gesuritas, nem os maacatitas; antes, Gesur e Maacate permaneceram no meio de Israel até ao dia de hoje.
14 Tão somente à tribo de Levi não deu herança; as ofertas queimadas do Senhor, Deus de Israel, são a sua herança, como já lhe tinha dito.
15 Deu, pois, Moisés à tribo dos filhos de Rúben, segundo as suas famílias,
16 começando o seu território com Aroer, que está à borda do vale de Arnom, mais a cidade que está no meio do vale e todo o planalto até Medeba;
17 Hesbom e todas as suas cidades, que estão no planalto: Dibom, Bamote-Baal e Bete-Baal-Meom,
18 Jaza, Quedemote, Mefaate;
19 Quiriataim, Sibma, Zerete-Saar, no monte do vale;
20 Bete-Peor, as faldas de Pisga e Bete-Jesimote;
21 e todas as cidades do planalto e todo o reino de Seom, rei dos amorreus, que reinou em Hesbom, a quem Moisés feriu, como também os príncipes de Midiã, Evi, Requém, Zur, Hur e Reba, príncipes de Seom, moradores da terra.
22 Também os filhos de Israel mataram à espada Balaão, filho de Beor, o adivinho, com outros mais que mataram.
23 A fronteira dos filhos de Rúben é o Jordão e suas imediações; esta é a herança dos filhos de Rúben, segundo as suas famílias: as cidades com suas aldeias.
24 Deu Moisés a herança à tribo de Gade, a saber, a seus filhos, segundo as suas famílias.
25 Foi o seu território: Jazer, todas as cidades de Gileade e metade da terra dos filhos de Amom, até Aroer, que está defronte de Rabá;
26 desde Hesbom até Ramate-Mispa e Betonim; e desde Maanaim até ao limite de Debir;
27 e, no vale: Bete-Arã, Bete-Ninra, Sucote e Zafom, o resto do reino de Seom, rei de Hesbom, mais o Jordão e suas imediações, até à extremidade do mar de Quinerete, dalém do Jordão, para o oriente.
28 Esta é a herança dos filhos de Gade, segundo as suas famílias: as cidades com suas aldeias.
29 Deu também Moisés herança à meia tribo de Manassés, segundo as suas famílias.
30 Foi o seu território: começando com Maanaim, mais todo o Basã, todo o reino de Ogue, rei de Basã, e todas as aldeias de Jair, que estão em Basã, sessenta cidades;
31 e metade de Gileade, Astarote e Edrei, cidades do reino de Ogue, em Basã; estas foram dadas aos filhos de Maquir, filho de Manassés, a saber, à metade dos filhos de Maquir, segundo as suas famílias.
32 São estas as heranças que Moisés repartiu nas campinas de Moabe, dalém do Jordão, na altura de Jericó, para o oriente.
33 Porém à tribo de Levi Moisés não deu herança; o Senhor, Deus de Israel, é a sua herança, como já lhes tinha dito.*
1 São estas as heranças que os filhos de Israel tiveram na terra de Canaã, o que Eleazar, o sacerdote, e Josué, filho de Num, e os cabeças dos pais das tribos dos filhos de Israel lhes fizeram repartir
2 por sorte da sua herança, como o Senhor ordenara por intermédio de Moisés, acerca das nove tribos e meia.
3 Porquanto às duas tribos e meia já dera Moisés herança além do Jordão; mas aos levitas não tinha dado herança entre seus irmãos.
4 Os filhos de José foram duas tribos, Manassés e Efraim; aos levitas não deram herança na terra, senão cidades em que habitassem e os seus arredores para seu gado e para sua possessão.
5 Como o Senhor ordenara a Moisés, assim fizeram os filhos de Israel e repartiram a terra.
6 Chegaram os filhos de Judá a Josué em Gilgal; e Calebe, filho de Jefoné, o quenezeu, lhe disse: Tu sabes o que o Senhor falou a Moisés, homem de Deus, em Cades-Barneia, a respeito de mim e de ti.
7 Tinha eu quarenta anos quando Moisés, servo do Senhor, me enviou de Cades-Barneia para espiar a terra; e eu lhe relatei como sentia no coração.
8 Mas meus irmãos que subiram comigo desesperaram o povo; eu, porém, perseverei em seguir o Senhor, meu Deus.
9 Então, Moisés, naquele dia, jurou, dizendo: Certamente, a terra em que puseste o pé será tua e de teus filhos, em herança perpetuamente, pois perseveraste em seguir o Senhor, meu Deus.
10 Eis, agora, o Senhor me conservou em vida, como prometeu; quarenta e cinco anos há desde que o Senhor falou esta palavra a Moisés, andando Israel ainda no deserto; e, já agora, sou de oitenta e cinco anos.
11 Estou forte ainda hoje como no dia em que Moisés me enviou; qual era a minha força naquele dia, tal ainda agora para o combate, tanto para sair a ele como para voltar.
12 Agora, pois, dá-me este monte de que o Senhor falou naquele dia, pois, naquele dia, ouviste que lá estavam os anaquins e grandes e fortes cidades; o Senhor, porventura, será comigo, para os desapossar, como prometeu.
13 Josué o abençoou e deu a Calebe, filho de Jefoné, Hebrom em herança.
14 Portanto, Hebrom passou a ser de Calebe, filho de Jefoné, o quenezeu, em herança até ao dia de hoje, visto que perseverara em seguir o Senhor, Deus de Israel.
15 Dantes o nome de Hebrom era Quiriate-Arba; este Arba foi o maior homem entre os anaquins. E a terra repousou da guerra.*
1 A sorte da tribo dos filhos de Judá, segundo as suas famílias, caiu para o sul, até ao limite de Edom, até ao deserto de Zim, até à extremidade do lado sul.
2 Foi o seu limite ao sul, desde a extremidade do mar Salgado, desde a baía que olha para o sul;
3 e sai para o sul, até à subida de Acrabim, passa a Zim, sobe do sul a Cades-Barneia,
4 passa por Hezrom, sobe a Adar e rodeia Carca; passa por Azmom e sai ao ribeiro do Egito; as saídas deste limite vão até ao mar; este será o vosso limite do lado sul.
5 O limite, porém, para o oriente será o mar Salgado, até à foz do Jordão; e o limite para o norte será da baía do mar, começando com a embocadura do Jordão,
6 limite que sobe até Bete-Hogla e passa do norte a Bete-Arabá, subindo até à pedra de Boã, filho de Rúben,
7 subindo ainda este limite a Debir desde o vale de Acor, olhando para o norte, rumo a Gilgal, a qual está à subida de Adumim, que está para o sul do ribeiro; daí, o limite passa até às águas de En-Semes; e as suas saídas estarão do lado de En-Rogel.
8 Deste ponto sobe pelo vale do Filho de Hinom, do lado dos jebuseus do Sul, isto é, Jerusalém; e sobe este limite até ao cimo do monte que está diante do vale de Hinom, para o ocidente, que está no fim do vale dos Refains, do lado norte.
9 Então, vai o limite desde o cimo do monte até à fonte das águas de Neftoa; e sai até às cidades do monte Efrom; vai mais este limite até Baalá, isto é, Quiriate-Jearim.
10 Então, dá volta o limite desde Baalá, para o ocidente, até ao monte Seir, passa ao lado do monte de Jearim do lado norte, isto é, Quesalom, e, descendo a Bete-Semes, passa por Timna.
11 Segue mais ainda o limite ao lado de Ecrom, para o norte, e, indo a Siquerom, passa o monte de Baalá, saindo em Jabneel, para terminar no mar.
12 O limite, porém, do lado ocidental é o mar Grande e as suas imediações. São estes os limites dos filhos de Judá ao redor, segundo as suas famílias.
13 A Calebe, filho de Jefoné, porém, deu Josué uma parte no meio dos filhos de Judá, segundo lhe ordenara o Senhor, a saber, Quiriate-Arba, isto é, Hebrom; este Arba era o pai de Anaque.
14 Dali expulsou Calebe os três filhos de Anaque: Sesai, Aimã e Talmai, gerados de Anaque.
15 Subiu aos habitantes de Debir, cujo nome, dantes, era Quiriate-Sefer.
16 Disse Calebe: A quem derrotar Quiriate-Sefer e a tomar, darei minha filha Acsa por mulher.
17 Tomou-a, pois, Otniel, filho de Quenaz, irmão de Calebe; este lhe deu a filha Acsa por mulher.
18 Esta, quando se foi a Otniel, insistiu com ele para que pedisse um campo ao pai dela; e ela apeou do jumento; então, Calebe lhe perguntou: Que desejas?
19 Respondeu ela: Dá-me um presente; deste-me terra seca, dá-me também fontes de água. Então, lhe deu as fontes superiores e as fontes inferiores.
20 Esta é a herança da tribo dos filhos de Judá, segundo as suas famílias.
21 São, pois, as cidades no extremo sul da tribo dos filhos de Judá, rumo do território de Edom: Cabzeel, Éder, Jagur,
22 Quiná, Dimona, Adada,
23 Quedes, Hazor, Itnã,
24 Zife, Telém, Bealote,
25 Hazor-Hadata, Queriote-Hezrom (que é Hazor),
26 Amã, Sema, Molada,
27 Hazar-Gada, Hesmom, Bete-Palete,
28 Hazar-Sual, Berseba, Biziotiá,
29 Baalá, Iim, Ezém,
30 Eltolade, Quesil, Horma,
31 Ziclague, Madmana, Sansana,
32 Lebaote, Silim, Aim e Rimom; ao todo, vinte e nove cidades com suas aldeias.
33 Nas planícies: Estaol, Zorá, Asná,
34 Zanoa, En-Ganim, Tapua, Enã,
35 Jarmute, Adulão, Socó, Azeca,
36 Saaraim, Aditaim, Gedera e Gederotaim; ao todo, catorze cidades com suas aldeias.
37 Zenã, Hadasa, Migdal-Gade,
38 Dileã, Mispa, Jocteel,
39 Laquis, Boscate, Eglom,
40 Cabom, Laamás, Quitlis,
41 Gederote, Bete-Dagom, Naamá e Maquedá; ao todo, dezesseis cidades com suas aldeias.
42 Libna, Eter, Asã,
43 Ifta, Asná, Nezibe,
44 Queila, Aczibe e Maressa; ao todo, nove cidades com suas aldeias.
45 Ecrom com suas vilas e aldeias;
46 desde Ecrom até ao mar, todas as que estão do lado de Asdode, com suas aldeias.
47 Asdode, suas vilas e aldeias; Gaza, suas vilas e aldeias, até ao rio do Egito e o mar Grande com as suas imediações.
48 Na região montanhosa: Samir, Jatir, Socó,
49 Daná, Quiriate-Sana, que é Debir,
50 Anabe, Estemoa, Anim,
51 Gósen, Holom e Gilo; ao todo, onze cidades com suas aldeias.
52 Arabe, Dumá, Esã,
53 Janim, Bete-Tapua, Afeca,
54 Hunta, Quiriate-Arba (que é Hebrom) e Zior; ao todo, nove cidades com suas aldeias.
55 Maom, Carmelo, Zife, Jutá,
56 Jezreel, Jocdeão, Zanoa,
57 Caim, Gibeá e Timna; ao todo, dez cidades com suas aldeias.
58 Halul, Bete-Zur, Gedor,
59 Maarate, Bete-Anote e Eltecom; ao todo, seis cidades com suas aldeias.
60 Quiriate-Baal (que é Quiriate-Jearim) e Rabá; ao todo, duas cidades com suas aldeias.
61 No deserto: Bete-Arabá, Midim, Secaca,
62 Nibsã, Cidade do Sal e En-Gedi; ao todo, seis cidades com suas aldeias.
63 Não puderam, porém, os filhos de Judá expulsar os jebuseus que habitavam em Jerusalém; assim, habitam os jebuseus com os filhos de Judá em Jerusalém até ao dia de hoje.*
1 O território que, em sorte, caiu aos filhos de José, começando no Jordão, na altura de Jericó e no lado oriental das águas de Jericó, vai ao deserto que sobe de Jericó pela região montanhosa até Betel.
2 De Betel sai para Luz, passa ao limite dos arquitas até Atarote
3 e desce, rumo ao ocidente, ao limite de Jaflete, até ao limite de Bete-Horom de baixo e até Gezer, terminando no mar.
4 Assim, alcançaram a sua herança os filhos de José, Manassés e Efraim.
5 Foi o limite da herança dos filhos de Efraim, segundo as suas famílias, no oriente, Atarote-Adar até Bete-Horom de cima;
6 e vai o limite para o mar com Micmetate, ao norte, de onde torna para o oriente até Taanate-Siló, e passa por ela ao oriente de Janoa;
7 desce desde Janoa a Atarote e a Naarate, toca em Jericó, terminando no Jordão.
8 De Tapua vai o limite, para o ocidente, ao ribeiro de Caná, terminando no mar; esta é a herança da tribo dos filhos de Efraim, segundo as suas famílias,
9 mais as cidades que se separaram para os filhos de Efraim, que estavam no meio da herança dos filhos de Manassés; todas aquelas cidades com suas aldeias.
10 Não expulsaram aos cananeus que habitavam em Gezer; assim, habitam eles no meio dos efraimitas até ao dia de hoje; porém sujeitos a trabalhos forçados.*
1 Também caiu a sorte à tribo de Manassés, o qual era o primogênito de José. Maquir, o primogênito de Manassés, pai de Gileade, porquanto era homem de guerra, teve Gileade e Basã.
2 Os mais filhos de Manassés também tiveram a sua parte, segundo as suas famílias, a saber, os filhos de Abiezer, e os filhos de Heleque, e os filhos de Asriel, e os filhos de Siquém, e os filhos de Héfer, e os filhos de Semida; são estes os filhos de Manassés, filho de José, segundo as suas famílias.
3 Zelofeade, porém, filho de Héfer, filho de Gileade, filho de Maquir, filho de Manassés, não teve filhos, mas só filhas, cujos nomes são estes: Macla, Noa, Hogla, Milca e Tirza.
4 Estas chegaram diante de Eleazar, o sacerdote, e diante de Josué, filho de Num, e diante dos príncipes, dizendo: O Senhor ordenou a Moisés que se nos desse herança no meio de nossos irmãos. Pelo que, segundo o dito do Senhor, Josué lhes deu herança no meio dos irmãos de seu pai.
5 Couberam a Manassés dez quinhões, afora a terra de Gileade e Basã, que está dalém do Jordão;
6 porque as filhas de Manassés, no meio de seus filhos, possuíram herança; os outros filhos de Manassés tiveram a terra de Gileade.
7 O limite de Manassés foi desde Aser até Micmetate, que está a leste de Siquém; e vai este limite, rumo sul, até aos moradores de En-Tapua.
8 Tinha Manassés a terra de Tapua; porém Tapua, ainda que situada no limite de Manassés, era dos filhos de Efraim.
9 Então, desce o limite ao ribeiro de Caná. As cidades, entre as de Manassés, ao sul do ribeiro, pertenciam a Efraim; então, o limite de Manassés vai ao norte do ribeiro, terminando no mar.
10 Efraim, ao sul, Manassés, ao norte, e o mar é seu limite; pelo norte, tocam em Aser e, pelo oriente, em Issacar.
11 Porque, em Issacar e em Aser, tinha Manassés a Bete-Seã e suas vilas, Ibleão e suas vilas, os habitantes de Dor e suas vilas, os habitantes de En-Dor e suas vilas, os habitantes de Taanaque e suas vilas e os habitantes de Megido e suas vilas, a região dos três outeiros.
12 E os filhos de Manassés não puderam expulsar os habitantes daquelas cidades, porquanto os cananeus persistiam em habitar nessa terra.
13 Sucedeu que, tornando-se fortes os filhos de Israel, sujeitaram aos cananeus a trabalhos forçados, porém não os expulsaram de todo.
14 Então, o povo dos filhos de José disse a Josué: Por que me deste por herança uma sorte apenas e um quinhão, sendo eu tão grande povo, visto que o Senhor até aqui me tem abençoado?
15 Disse-lhe Josué: Se és grande povo, sobe ao bosque e abre ali clareira na terra dos ferezeus e dos refains, visto que a região montanhosa de Efraim te é estreita demais.
16 Então, disseram os filhos de José: A região montanhosa não nos basta; e todos os cananeus que habitam na terra do vale têm carros de ferro, tanto os que estão em Bete-Seã e suas vilas como os que estão no vale de Jezreel.
17 Falou Josué à casa de José, a Efraim e a Manassés, dizendo: Tu és povo numeroso e forte; não terás uma sorte apenas;
18 porém a região montanhosa será tua. Ainda que é bosque, cortá-lo-ás, e até às suas extremidades será todo teu; porque expulsarás os cananeus, ainda que possuem carros de ferro e são fortes.*
1 Reuniu-se toda a congregação dos filhos de Israel em Siló, e ali armaram a tenda da congregação; e a terra estava sujeita diante deles.
2 Dentre os filhos de Israel ficaram sete tribos que ainda não tinham repartido a sua herança.
3 Disse Josué aos filhos de Israel: Até quando sereis remissos em passardes para possuir a terra que o Senhor, Deus de vossos pais, vos deu?
4 De cada tribo escolhei três homens, para que eu os envie, eles se disponham, e corram a terra, e façam dela um gráfico relativamente à herança das tribos, e se tornem a mim.
5 Dividirão a terra em sete partes: Judá ficará no seu território, ao sul, e a casa de José, no seu, ao norte.
6 Em sete partes fareis o gráfico da terra e mo trareis a mim, para que eu aqui vos lance as sortes perante o Senhor, nosso Deus.
7 Porquanto os levitas não têm parte entre vós, pois o sacerdócio do Senhor é a sua parte. Gade, e Rúben, e a meia tribo de Manassés já haviam recebido a sua herança dalém do Jordão, para o oriente, a qual lhes deu Moisés, servo do Senhor.
8 Dispuseram-se, pois, aqueles homens e se foram, e Josué deu ordem aos que iam levantar o gráfico da terra, dizendo: Ide, correi a terra, levantai-lhe o gráfico e tornai a mim; aqui vos lançarei as sortes perante o Senhor, em Siló.
9 Foram, pois, os homens, passaram pela terra, levantaram dela o gráfico, cidade por cidade, em sete partes, num livro, e voltaram a Josué, ao arraial em Siló.
10 Então, Josué lhes lançou as sortes em Siló, perante o Senhor; e ali repartiu Josué a terra, segundo as suas divisões, aos filhos de Israel.
11 Saiu a sorte da tribo dos filhos de Benjamim, segundo as suas famílias; e o território da sua sorte caiu entre os filhos de Judá e os filhos de José.
12 O seu limite foi para o lado norte desde o Jordão; subia ao lado de Jericó, para o norte, e subia pela montanha, para o ocidente, para terminar no deserto de Bete-Áven.
13 E dali passava o limite a Luz, ao lado de Luz (que é Betel), para o sul; descia a Atarote-Adar, ao pé do monte que está do lado sul de Bete-Horom de baixo.
14 Seguia o limite, e tornava ao lado ocidental, para o sul do monte que está defronte de Bete-Horom, para o sul, e terminava em Quiriate-Baal (que é Quiriate-Jearim), cidade dos filhos de Judá; este era o lado ocidental.
15 O lado do sul começava na extremidade oriental de Quiriate-Jearim e seguia até à fonte das águas de Neftoa;
16 descia o limite até à extremidade do monte que está defronte do vale do Filho de Hinom, ao norte do vale dos Refains, e descia pelo vale de Hinom do lado dos jebuseus, para o sul; e baixava a En-Rogel;
17 volvia-se para o norte, chegava a En-Semes, de onde passava para Gelilote, que está defronte da subida de Adumim, e descia à pedra de Boã, filho de Rúben;
18 passava pela vertente norte, defronte da planície, e descia à planície.
19 Depois, passava o limite até ao lado de Bete-Hogla, para o norte, para terminar na baía do mar Salgado, na desembocadura do Jordão, ao sul; este era o limite do sul.
20 Do lado oriental, o Jordão era o seu limite; esta era a herança dos filhos de Benjamim nos seus limites em redor, segundo as suas famílias.
21 As cidades da tribo dos filhos de Benjamim, segundo as suas famílias, eram: Jericó, Bete-Hogla, Emeque-Quesis,
22 Bete-Arabá, Zemaraim, Betel,
23 Avim, Pará, Ofra,
24 Quefar-Amonai, Ofni e Gaba; ao todo, doze cidades com suas aldeias.
25 Gibeão, Ramá, Beerote,
26 Mispa, Cefira, Mosa,
27 Requém, Irpeel, Tarala,
28 Zela, Elefe, Jebus (esta é Jerusalém), Gibeá e Quiriate; ao todo, catorze cidades com suas aldeias; esta era a herança dos filhos de Benjamim, segundo as suas famílias.*
1 Saiu a segunda sorte a Simeão, à tribo dos filhos de Simeão, segundo as suas famílias, e foi a sua herança no meio da dos filhos de Judá.
2 Na herança, tiveram: Berseba, Seba, Molada,
3 Hazar-Sual, Balá, Ezém,
4 Eltolade, Betul, Horma,
5 Ziclague, Bete-Marcabote, Hazar-Susa,
6 Bete-Lebaote e Saruém; ao todo, treze cidades com suas aldeias.
7 Aim, Rimom, Eter e Asã; ao todo, quatro cidades com suas aldeias.
8 E todas as aldeias que havia em redor destas cidades, até Baalate-Ber, que é Ramá do Neguebe; esta era a herança da tribo dos filhos de Simeão, segundo as suas famílias.
9 A herança dos filhos de Simeão se tirou de entre a porção dos filhos de Judá, pois a herança destes era demasiadamente grande para eles, pelo que os filhos de Simeão tiveram a sua herança no meio deles.
10 Saiu a terceira sorte aos filhos de Zebulom, segundo as suas famílias. O limite da sua herança ia até Saride.
11 Subia o seu limite, pelo ocidente, a Marala, tocava em Dabesete e chegava até ao ribeiro que está defronte de Jocneão.
12 De Saride, dava volta para o oriente, para o nascente do sol, até ao limite de Quislote-Tabor, saía a Daberate, e ia subindo a Jafia;
13 dali, passava, para o nascente, a Gate-Hefer, a Ete-Cazim, ia a Rimom, que se estendia até Neá,
14 e, rodeando-a, o limite passava, para o norte, a Hanatom e terminava no vale de Ifta-El.
15 Ainda Catate, Naalal, Sinrom, Idala e Belém, completando doze cidades com suas aldeias.
16 Esta era a herança dos filhos de Zebulom, segundo as suas famílias; estas cidades com suas aldeias.
A herança de Issacar
17 A quarta sorte saiu a Issacar, aos filhos de Issacar, segundo as suas famílias.
18 O seu território incluía Jezreel, Quesulote, Suném,
19 Hafaraim, Siom, Anacarate,
20 Rabite, Quisião, Ebes,
21 Remete, En-Ganim, En-Hada e Bete-Pasês.
22 O limite tocava o Tabor, Saazima e Bete-Semes e terminava no Jordão; ao todo, dezesseis cidades com suas aldeias.
23 Esta era a herança da tribo dos filhos de Issacar, segundo as suas famílias; estas cidades com suas aldeias.
24 Saiu a quinta sorte à tribo dos filhos de Aser, segundo as suas famílias.
25 O seu território incluía Helcate, Hali, Béten, Acsafe,
26 Alameleque, Amade e Misal; e tocava o Carmelo, para o ocidente, e Sior-Libnate;
27 volvendo-se para o nascente do sol, Bete-Dagom, tocava Zebulom e o vale de Ifta-El, ao norte de Bete-Emeque e de Neiel, e vinha sair a Cabul, pela esquerda,
28 Ebrom, Reobe, Hamom e Caná, até à grande Sidom.
29 Voltava o limite a Ramá e até à forte cidade de Tiro; então, tornava a Hosa, para terminar no mar, na região de Aczibe;
30 também Umá, Afeca e Reobe, completando vinte e duas cidades com suas aldeias.
31 Esta era a herança da tribo dos filhos de Aser, segundo as suas famílias; estas cidades com suas aldeias.
32 Saiu a sexta sorte aos filhos de Naftali, segundo as suas famílias.
33 Era o seu limite desde Helefe, do carvalho em Zaananim, Adami-Nequebe, Jabneel, até Lacum e terminava no Jordão.
34 Voltava o limite, pelo ocidente, a Aznote-Tabor, de onde passava a Hucoque; tocava Zebulom, ao sul, e Aser, ao ocidente, e Judá, pelo Jordão, ao nascente do sol.
35 As cidades fortificadas eram: Zidim, Zer, Hamate, Racate, Quinerete,
36 Adamá, Ramá, Hazor,
37 Quedes, Edrei, En-Hazor,
38 Irom, Migdal-El, Horém, Bete-Anate e Bete-Semes; ao todo, dezenove cidades com suas aldeias.
39 Esta era a herança da tribo dos filhos de Naftali, segundo as suas famílias; estas cidades com suas aldeias.
40 A sétima sorte saiu à tribo dos filhos de Dã, segundo as suas famílias.
41 O território da sua herança incluía Zorá, Estaol, Ir-Semes,
42 Saalabim, Aijalom, Itla,
43 Elom, Timna, Ecrom,
44 Elteque, Gibetom, Baalate,
45 Jeúde, Benê-Beraque, Gate-Rimom,
46 Me-Jarcom e Racom, com o território defronte de Jope.
47 Saiu, porém, pequeno o limite aos filhos de Dã, pelo que subiram os filhos de Dã, e pelejaram contra Lesém, e a tomaram, e a feriram a fio de espada; e, tendo-a possuído, habitaram nela e lhe chamaram Dã, segundo o nome de Dã, seu pai.
48 Esta era a herança da tribo dos filhos de Dã, segundo as suas famílias; estas cidades com suas aldeias.
49 Acabando, pois, de repartir a terra em herança, segundo os seus territórios, deram os filhos de Israel a Josué, filho de Num, herança no meio deles.
50 Deram-lhe, segundo o mandado do Senhor, a cidade que pediu, Timnate-Sera, na região montanhosa de Efraim; reedificou ele a cidade e habitou nela.
51 Eram estas as heranças que Eleazar, o sacerdote, e Josué, filho de Num, e os cabeças dos pais das famílias repartiram por sorte, em herança, pelas tribos dos filhos de Israel, em Siló, perante o Senhor, à porta da tenda da congregação. E assim acabaram de repartir a terra.*
1 Disse mais o Senhor a Josué:
2 Fala aos filhos de Israel: Apartai para vós outros as cidades de refúgio de que vos falei por intermédio de Moisés;
3 para que fuja para ali o homicida que, por engano, matar alguma pessoa sem o querer; para que vos sirvam de refúgio contra o vingador do sangue.
4 E, fugindo para alguma dessas cidades, pôr-se-á à porta dela e exporá o seu caso perante os ouvidos dos anciãos da tal cidade; então, o tomarão consigo na cidade e lhe darão lugar, para que habite com eles.
5 Se o vingador do sangue o perseguir, não lhe entregarão nas mãos o homicida, porquanto feriu a seu próximo sem querer e não o aborrecia dantes.
6 Habitará, pois, na mesma cidade até que compareça em juízo perante a congregação, até que morra o sumo sacerdote que for naqueles dias; então, tornará o homicida e voltará à sua cidade e à sua casa, à cidade de onde fugiu.
7 Designaram, pois, solenemente, Quedes, na Galileia, na região montanhosa de Naftali, e Siquém, na região montanhosa de Efraim, e Quiriate-Arba, ou seja, Hebrom, na região montanhosa de Judá.
8 Dalém do Jordão, na altura de Jericó, para o oriente, designaram Bezer, no deserto, no planalto da tribo de Rúben; e Ramote, em Gileade, da tribo de Gade; e Golã, em Basã, da tribo de Manassés.
9 São estas as cidades que foram designadas para todos os filhos de Israel e para o estrangeiro que habitava entre eles; para que se refugiasse nelas todo aquele que, por engano, matasse alguma pessoa, para que não morresse às mãos do vingador do sangue, até comparecer perante a congregação.*
1 Então, se chegaram os cabeças dos pais dos levitas a Eleazar, o sacerdote, e a Josué, filho de Num, e aos cabeças dos pais das tribos dos filhos de Israel;
2 e falaram-lhes em Siló, na terra de Canaã, dizendo: O Senhor ordenou, por intermédio de Moisés, que se nos dessem cidades para habitar e os seus arredores para os nossos animais.
3 E os filhos de Israel deram aos levitas, da sua herança, segundo o mandado do Senhor, estas cidades e os seus arredores.
4 Caiu a sorte pelas famílias dos coatitas. Assim, os filhos de Arão, o sacerdote, que eram dos levitas, tiveram, por sorte, da tribo de Judá, da tribo de Simeão e da tribo de Benjamim treze cidades.
5 Os outros filhos de Coate tiveram, por sorte, das famílias da tribo de Efraim, da tribo de Dã e da meia tribo de Manassés dez cidades.
6 Os filhos de Gérson tiveram, por sorte, das famílias da tribo de Issacar, da tribo de Aser, da tribo de Naftali e da meia tribo de Manassés, em Basã, treze cidades.
7 Os filhos de Merari tiveram, por sorte, segundo as suas famílias, da tribo de Rúben, da tribo de Gade e da tribo de Zebulom doze cidades.
8 Deram os filhos de Israel aos levitas estas cidades e os seus arredores, por sorte, como o Senhor ordenara por intermédio de Moisés.
9 Deram mais, da tribo dos filhos de Judá e da tribo dos filhos de Simeão, estas cidades que, nominalmente, foram designadas,
10 para que fossem dos filhos de Arão, das famílias dos coatitas, dos filhos de Levi, porquanto a primeira sorte foi deles.
11 Assim, lhes deram Quiriate-Arba (Arba era pai de Anaque), que é Hebrom, na região montanhosa de Judá, e, em torno dela, os seus arredores.
12 Porém o campo da cidade, com suas aldeias, deram a Calebe, filho de Jefoné, por sua possessão.
13 Assim, aos filhos de Arão, o sacerdote, deram Hebrom, cidade de refúgio do homicida, com seus arredores, Libna com seus arredores,
14 Jatir com seus arredores, Estemoa com seus arredores,
15 Holom com seus arredores, Debir com seus arredores,
16 Aim com seus arredores, Jutá com seus arredores e Bete-Semes com seus arredores; ao todo, nove cidades dessas duas tribos.
17 Da tribo de Benjamim, deram Gibeão com seus arredores, Gaba com seus arredores,
18 Anatote com seus arredores e Almom com seus arredores; ao todo, quatro cidades.
19 Total das cidades dos sacerdotes, filhos de Arão: treze cidades com seus arredores.
20 As mais famílias dos levitas de Coate tiveram as cidades da sua sorte da tribo de Efraim.
21 Deram-lhes Siquém, cidade de refúgio do homicida, com seus arredores, na região montanhosa de Efraim, Gezer com seus arredores,
22 Quibzaim com seus arredores e Bete-Horom com seus arredores; ao todo, quatro cidades.
23 Da tribo de Dã, deram Elteque com seus arredores, Gibetom com seus arredores,
24 Aijalom com seus arredores e Gate-Rimom com seus arredores; ao todo, quatro cidades.
25 Da meia tribo de Manassés, deram Taanaque com seus arredores e Gate-Rimom com seus arredores; ao todo, duas cidades.
26 Total: dez cidades com seus arredores, para as famílias dos demais filhos de Coate.
27 Aos filhos de Gérson, das famílias dos levitas, deram, em Basã, da tribo de Manassés, Golã, a cidade de refúgio para o homicida, com seus arredores, e Beesterá com seus arredores; ao todo, duas cidades.
28 Da tribo de Issacar, deram Quisião com seus arredores, Daberate com seus arredores,
29 Jarmute com seus arredores e En-Ganim com seus arredores; ao todo, quatro cidades.
30 Da tribo de Aser, deram Misal com seus arredores, Abdom com seus arredores,
31 Helcate com seus arredores e Reobe com seus arredores; ao todo, quatro cidades.
32 Da tribo de Naftali, deram, na Galileia, Quedes, cidade de refúgio para o homicida, com seus arredores, Hamote-Dor com seus arredores e Cartã com seus arredores; ao todo, três cidades.
33 Total das cidades dos gersonitas, segundo as suas famílias: treze cidades com seus arredores.
34 Às famílias dos demais levitas dos filhos de Merari deram, da tribo de Zebulom, Jocneão com seus arredores, Cartá com seus arredores,
35 Dimna com seus arredores e Naalal com seus arredores; ao todo, quatro cidades.
36 Da tribo de Rúben, deram Bezer com seus arredores, Jaza com seus arredores,
37 Quedemote com seus arredores e Mefaate com seus arredores; ao todo, quatro cidades.
38 Da tribo de Gade, deram, em Gileade, Ramote, cidade de refúgio para o homicida, com seus arredores, Maanaim com seus arredores,
39 Hesbom com seus arredores e Jazer com seus arredores; ao todo, quatro cidades.
40 Todas estas cidades tocaram por sorte aos filhos de Merari, segundo as suas famílias, que ainda restavam das famílias dos levitas: doze cidades.
41 As cidades, pois, dos levitas, no meio da herança dos filhos de Israel, foram, ao todo, quarenta e oito cidades com seus arredores;
42 cada uma das quais com seus arredores em torno de si; assim foi com todas estas cidades.
43 Desta maneira, deu o Senhor a Israel toda a terra que jurara dar a seus pais; e a possuíram e habitaram nela.
44 O Senhor lhes deu repouso em redor, segundo tudo quanto jurara a seus pais; nenhum de todos os seus inimigos resistiu diante deles; a todos eles o Senhor lhes entregou nas mãos.
45 Nenhuma promessa falhou de todas as boas palavras que o Senhor falara à casa de Israel; tudo se cumpriu.*
1 Então, Josué chamou os rubenitas, os gaditas e a meia tribo de Manassés
2 e lhes disse: Tendes guardado tudo quanto vos ordenou Moisés, servo do Senhor, e também a mim me tendes obedecido em tudo quanto vos ordenei.
3 A vossos irmãos, durante longo tempo, até ao dia de hoje, não desamparastes; antes, tivestes o cuidado de guardar o mandamento do Senhor, vosso Deus.
4 Tendo o Senhor, vosso Deus, dado repouso a vossos irmãos, como lhes havia prometido, voltai-vos, pois, agora, e ide-vos para as vossas tendas, à terra da vossa possessão, que Moisés, servo do Senhor, vos deu dalém do Jordão.
5 Tende cuidado, porém, de guardar com diligência o mandamento e a lei que Moisés, servo do Senhor, vos ordenou: que ameis o Senhor, vosso Deus, andeis em todos os seus caminhos, guardeis os seus mandamentos, e vos achegueis a ele, e o sirvais de todo o vosso coração e de toda a vossa alma.
6 Assim, Josué os abençoou e os despediu; e eles se foram para as suas tendas.
7 Ora, Moisés dera herança em Basã à meia tribo de Manassés; porém à outra metade deu Josué entre seus irmãos, daquém do Jordão, para o ocidente. E Josué, ao despedi-los para as suas tendas, os abençoou
8 e lhes disse: Voltais às vossas tendas com grandes riquezas, com muitíssimo gado, prata, ouro, bronze, ferro e muitíssima roupa; reparti com vossos irmãos o despojo dos vossos inimigos.
9 Assim, os filhos de Rúben, os filhos de Gade e a meia tribo de Manassés voltaram e se retiraram dos filhos de Israel em Siló, que está na terra de Canaã, para se irem à terra de Gileade, à terra da sua possessão, de que foram feitos possuidores, segundo o mandado do Senhor, por intermédio de Moisés.
10 Vindo eles para os limites pegados ao Jordão, na terra de Canaã, ali os filhos de Rúben, os filhos de Gade e a meia tribo de Manassés edificaram um altar junto ao Jordão, altar grande e vistoso.
11 Os filhos de Israel ouviram dizer: Eis que os filhos de Rúben, os filhos de Gade e a meia tribo de Manassés edificaram um altar defronte da terra de Canaã, nos limites pegados ao Jordão, do lado dos filhos de Israel.
12 Ouvindo isto os filhos de Israel, ajuntou-se toda a congregação dos filhos de Israel em Siló, para saírem à peleja contra eles.
13 E aos filhos de Rúben, aos filhos de Gade e à meia tribo de Manassés enviaram os filhos de Israel, para a terra de Gileade, Fineias, filho de Eleazar, o sacerdote,
14 e dez príncipes com ele, de cada casa paterna um príncipe de todas as tribos de Israel; e cada um era cabeça da casa de seus pais entre os grupos de milhares de Israel.
15 Indo eles aos filhos de Rúben, aos filhos de Gade e à meia tribo de Manassés, à terra de Gileade, falaram-lhes, dizendo:
16 Assim diz toda a congregação do Senhor: Que infidelidade é esta, que cometestes contra o Deus de Israel, deixando, hoje, de seguir o Senhor, edificando-vos um altar, para vos rebelardes contra o Senhor?
17 Acaso, não nos bastou a iniquidade de Peor, de que até hoje não estamos ainda purificados, posto que houve praga na congregação do Senhor,
18 para que, hoje, abandoneis o Senhor? Se, hoje, vos rebelais contra o Senhor, amanhã, se irará contra toda a congregação de Israel.
19 Se a terra da vossa herança é imunda, passai-vos para a terra da possessão do Senhor, onde habita o tabernáculo do Senhor, e tomai possessão entre nós; não vos rebeleis, porém, contra o Senhor, nem vos rebeleis contra nós, edificando-vos altar, afora o altar do Senhor, nosso Deus.
20 Não cometeu Acã, filho de Zera, infidelidade no tocante às coisas condenadas? E não veio ira sobre toda a congregação de Israel? Pois aquele homem não morreu sozinho na sua iniquidade.
21 Então, responderam os filhos de Rúben, os filhos de Gade e a meia tribo de Manassés e disseram aos cabeças dos grupos de milhares de Israel:
22 O Poderoso, o Deus, o Senhor, o Poderoso, o Deus, o Senhor, ele o sabe, e Israel mesmo o saberá. Se foi em rebeldia ou por infidelidade contra o Senhor, hoje, não nos preserveis.
23 Se edificamos altar para nos apartarmos do Senhor, ou para, sobre ele, oferecermos holocausto e oferta de manjares, ou, sobre ele, fazermos oferta pacífica, o Senhor mesmo de nós o demande.
24 Pelo contrário, fizemos por causa da seguinte preocupação: amanhã vossos filhos talvez dirão a nossos filhos: Que tendes vós com o Senhor, Deus de Israel?
25 Pois o Senhor pôs o Jordão por limite entre nós e vós, ó filhos de Rúben e filhos de Gade; não tendes parte no Senhor; e, assim, bem poderiam os vossos filhos apartar os nossos do temor do Senhor.
26 Pelo que dissemos: preparemo-nos, edifiquemos um altar, não para holocausto, nem para sacrifício,
27 mas, para que entre nós e vós e entre as nossas gerações depois de nós, nos seja testemunho, e possamos servir ao Senhor diante dele com os nossos holocaustos, e os nossos sacrifícios, e as nossas ofertas pacíficas; e para que vossos filhos não digam amanhã a nossos filhos: Não tendes parte no Senhor.
28 Pelo que dissemos: quando suceder que, amanhã, assim nos digam a nós e às nossas gerações, então, responderemos: vede o modelo do altar do Senhor que fizeram nossos pais, não para holocausto, nem para sacrifício, mas para testemunho entre nós e vós.
29 Longe de nós o rebelarmo-nos contra o Senhor e deixarmos, hoje, de seguir o Senhor, edificando altar para holocausto, oferta de manjares ou sacrifício, afora o altar do Senhor, nosso Deus, que está perante o seu tabernáculo.
30 Ouvindo, pois, Fineias, o sacerdote, e os príncipes da congregação, e os cabeças dos grupos de milhares de Israel que com ele estavam as palavras que disseram os filhos de Rúben, os filhos de Gade e os filhos de Manassés, deram-se por satisfeitos.
31 E disse Fineias, filho de Eleazar, o sacerdote, aos filhos de Rúben, aos filhos de Gade e aos filhos de Manassés: Hoje, sabemos que o Senhor está no meio de nós, porquanto não cometestes infidelidade contra o Senhor; agora, livrastes os filhos de Israel da mão do Senhor.
32 Fineias, filho do sacerdote Eleazar, e os príncipes, deixando os filhos de Rúben e os filhos de Gade, voltaram da terra de Gileade para a terra de Canaã, aos filhos de Israel, e deram-lhes conta de tudo.
33 Com esta resposta deram-se por satisfeitos os filhos de Israel, os quais bendisseram a Deus; e não falaram mais de subir a pelejar contra eles, para destruírem a terra em que habitavam os filhos de Rúben e os filhos de Gade.
34 Os filhos de Rúben e os filhos de Gade chamaram o altar de Testemunho, porque disseram: É um testemunho entre nós de que o Senhor é Deus.*
1 Passado muito tempo depois que o Senhor dera repouso a Israel de todos os seus inimigos em redor, e sendo Josué já velho e entrado em dias,
2 chamou Josué a todo o Israel, os seus anciãos, os seus cabeças, os seus juízes e os seus oficiais e disse-lhes: Já sou velho e entrado em dias,
3 e vós já tendes visto tudo quanto fez o Senhor, vosso Deus, a todas estas nações por causa de vós, porque o Senhor, vosso Deus, é o que pelejou por vós.
4 Vede aqui que vos fiz cair em sorte às vossas tribos estas nações que restam, juntamente com todas as nações que tenho eliminado, umas e outras, desde o Jordão até ao mar Grande, para o pôr do sol.
5 O Senhor, vosso Deus, as afastará de vós e as expulsará de vossa presença; e vós possuireis a sua terra, como o Senhor, vosso Deus, vos prometeu.
6 Esforçai-vos, pois, muito para guardardes e cumprirdes tudo quanto está escrito no Livro da Lei de Moisés, para que dela não vos aparteis, nem para a direita nem para a esquerda;
7 para que não vos mistureis com estas nações que restaram entre vós. Não façais menção dos nomes de seus deuses, nem por eles façais jurar, nem os sirvais, nem os adoreis.
8 Mas ao Senhor, vosso Deus, vos apegareis, como fizestes até ao dia de hoje;
9 pois o Senhor expulsou de diante de vós grandes e fortes nações; e, quanto a vós outros, ninguém vos resistiu até ao dia de hoje.
10 Um só homem dentre vós perseguirá mil, pois o Senhor, vosso Deus, é quem peleja por vós, como já vos prometeu.
11 Portanto, empenhai-vos em guardar a vossa alma, para amardes o Senhor, vosso Deus.
12 Porque, se dele vos desviardes e vos apegardes ao restante destas nações ainda em vosso meio, e com elas vos aparentardes, e com elas vos misturardes, e elas convosco,
13 sabei, certamente, que o Senhor, vosso Deus, não expulsará mais estas nações de vossa presença, mas vos serão por laço e rede, e açoite às vossas ilhargas, e espinhos aos vossos olhos, até que pereçais nesta boa terra que vos deu o Senhor, vosso Deus.
14 Eis que, já hoje, sigo pelo caminho de todos os da terra; e vós bem sabeis de todo o vosso coração e de toda a vossa alma que nem uma só promessa caiu de todas as boas palavras que falou de vós o Senhor, vosso Deus; todas vos sobrevieram, nem uma delas falhou.
15 E sucederá que, assim como vieram sobre vós todas estas boas coisas que o Senhor, vosso Deus, vos prometeu, assim cumprirá o Senhor contra vós outros todas as ameaças até vos destruir de sobre a boa terra que vos deu o Senhor, vosso Deus.
16 Quando violardes a aliança que o Senhor, vosso Deus, vos ordenou, e fordes, e servirdes a outros deuses, e os adorardes, então, a ira do Senhor se acenderá sobre vós, e logo perecereis na boa terra que vos deu.*
1 Depois, reuniu Josué todas as tribos de Israel em Siquém e chamou os anciãos de Israel, os seus cabeças, os seus juízes e os seus oficiais; e eles se apresentaram diante de Deus.
2 Então, Josué disse a todo o povo: Assim diz o Senhor, Deus de Israel: Antigamente, vossos pais, Tera, pai de Abraão e de Naor, habitaram dalém do Eufrates e serviram a outros deuses.
3 Eu, porém, tomei Abraão, vosso pai, dalém do rio e o fiz percorrer toda a terra de Canaã; também lhe multipliquei a descendência e lhe dei Isaque.
4 A Isaque dei Jacó e Esaú e a Esaú dei em possessão as montanhas de Seir; porém Jacó e seus filhos desceram para o Egito.
5 Então, enviei Moisés e Arão e feri o Egito com o que fiz no meio dele; e, depois, vos tirei de lá.
6 Tirando eu vossos pais do Egito, viestes ao mar; os egípcios perseguiram vossos pais, com carros e com cavaleiros, até ao mar Vermelho.
7 E, clamando vossos pais, o Senhor pôs escuridão entre vós e os egípcios, e trouxe o mar sobre estes, e o mar os cobriu; e os vossos olhos viram o que eu fiz no Egito. Então, habitastes no deserto por muito tempo.
8 Daí eu vos trouxe à terra dos amorreus, que habitavam dalém do Jordão, os quais pelejaram contra vós outros; porém os entreguei nas vossas mãos, e possuístes a sua terra; e os destruí diante de vós.
9 Levantou-se, também, o rei de Moabe, Balaque, filho de Zipor, e pelejou contra Israel; mandou chamar Balaão, filho de Beor, para que vos amaldiçoasse.
10 Porém eu não quis ouvir Balaão; e ele teve de vos abençoar; e, assim, vos livrei da sua mão.
11 Passando vós o Jordão e vindo a Jericó, os habitantes de Jericó pelejaram contra vós outros e também os amorreus, os ferezeus, os cananeus, os heteus, os girgaseus, os heveus e os jebuseus; porém os entreguei nas vossas mãos.
12 Enviei vespões adiante de vós, que os expulsaram da vossa presença, bem como os dois reis dos amorreus, e isso não com a tua espada, nem com o teu arco.
13 Dei-vos a terra em que não trabalhastes e cidades que não edificastes, e habitais nelas; comeis das vinhas e dos olivais que não plantastes.
14 Agora, pois, temei ao Senhor e servi-o com integridade e com fidelidade; deitai fora os deuses aos quais serviram vossos pais dalém do Eufrates e no Egito e servi ao Senhor.
15 Porém, se vos parece mal servir ao Senhor, escolhei, hoje, a quem sirvais: se aos deuses a quem serviram vossos pais que estavam dalém do Eufrates ou aos deuses dos amorreus em cuja terra habitais. Eu e a minha casa serviremos ao Senhor.
16 Então, respondeu o povo e disse: Longe de nós o abandonarmos o Senhor para servirmos a outros deuses;
17 porque o Senhor é o nosso Deus; ele é quem nos fez subir, a nós e a nossos pais, da terra do Egito, da casa da servidão, quem fez estes grandes sinais aos nossos olhos e nos guardou por todo o caminho em que andamos e entre todos os povos pelo meio dos quais passamos.
18 O Senhor expulsou de diante de nós todas estas gentes, até o amorreu, morador da terra; portanto, nós também serviremos ao Senhor, pois ele é o nosso Deus.
19 Então, Josué disse ao povo: Não podereis servir ao Senhor, porquanto é Deus santo, Deus zeloso, que não perdoará a vossa transgressão nem os vossos pecados.
20 Se deixardes o Senhor e servirdes a deuses estranhos, então, se voltará, e vos fará mal, e vos consumirá, depois de vos ter feito bem.
21 Então, disse o povo a Josué: Não; antes, serviremos ao Senhor.
22 Josué disse ao povo: Sois testemunhas contra vós mesmos de que escolhestes o Senhor para o servir. E disseram: Nós o somos.
23 Agora, pois, deitai fora os deuses estranhos que há no meio de vós e inclinai o coração ao Senhor, Deus de Israel.
24 Disse o povo a Josué: Ao Senhor, nosso Deus, serviremos e obedeceremos à sua voz.
25 Assim, naquele dia, fez Josué aliança com o povo e lha pôs por estatuto e direito em Siquém.
26 Josué escreveu estas palavras no Livro da Lei de Deus; tomou uma grande pedra e a erigiu ali debaixo do carvalho que estava em lugar santo do Senhor.
27 Disse Josué a todo o povo: Eis que esta pedra nos será testemunha, pois ouviu todas as palavras que o Senhor nos tem dito; portanto, será testemunha contra vós outros para que não mintais a vosso Deus.
28 Então, Josué despediu o povo, cada um para a sua herança.
29 Depois destas coisas, sucedeu que Josué, filho de Num, servo do Senhor, faleceu com a idade de cento e dez anos.
30 Sepultaram-no na sua própria herança, em Timnate-Sera, que está na região montanhosa de Efraim, para o norte do monte Gaás.
31 Serviu, pois, Israel ao Senhor todos os dias de Josué e todos os dias dos anciãos que ainda sobreviveram por muito tempo depois de Josué e que sabiam todas as obras feitas pelo Senhor a Israel.
32 Os ossos de José, que os filhos de Israel trouxeram do Egito, enterraram-nos em Siquém, naquela parte do campo que Jacó comprara aos filhos de Hamor, pai de Siquém, por cem peças de prata, e que veio a ser a herança dos filhos de José.
33 Faleceu também Eleazar, filho de Arão, e o sepultaram em Gibeá, pertencente a Fineias, seu filho, a qual lhe fora dada na região montanhosa de Efraim.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Josué','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)