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
1 No ano terceiro do reinado de Jeoaquim, rei de Judá, veio Nabucodonosor, rei da Babilônia, a Jerusalém e a sitiou.
2 O Senhor lhe entregou nas mãos a Jeoaquim, rei de Judá, e alguns dos utensílios da Casa de Deus; a estes, levou-os para a terra de Sinar, para a casa do seu deus, e os pôs na casa do tesouro do seu deus.
3 Disse o rei a Aspenaz, chefe dos seus eunucos, que trouxesse alguns dos filhos de Israel, tanto da linhagem real como dos nobres,
4 jovens sem nenhum defeito, de boa aparência, instruídos em toda a sabedoria, doutos em ciência, versados no conhecimento e que fossem competentes para assistirem no palácio do rei e lhes ensinasse a cultura e a língua dos caldeus.
5 Determinou-lhes o rei a ração diária, das finas iguarias da mesa real e do vinho que ele bebia, e que assim fossem mantidos por três anos, ao cabo dos quais assistiriam diante do rei.
6 Entre eles, se achavam, dos filhos de Judá, Daniel, Hananias, Misael e Azarias.
7 O chefe dos eunucos lhes pôs outros nomes, a saber: a Daniel, o de Beltessazar; a Hananias, o de Sadraque; a Misael, o de Mesaque; e a Azarias, o de Abede-Nego.
8 Resolveu Daniel, firmemente, não contaminar-se com as finas iguarias do rei, nem com o vinho que ele bebia; então, pediu ao chefe dos eunucos que lhe permitisse não contaminar-se.
9 Ora, Deus concedeu a Daniel misericórdia e compreensão da parte do chefe dos eunucos.
10 Disse o chefe dos eunucos a Daniel: Tenho medo do meu senhor, o rei, que determinou a vossa comida e a vossa bebida; por que, pois, veria ele o vosso rosto mais abatido do que o dos outros jovens da vossa idade? Assim, poríeis em perigo a minha cabeça para com o rei.
11 Então, disse Daniel ao cozinheiro-chefe, a quem o chefe dos eunucos havia encarregado de cuidar de Daniel, Hananias, Misael e Azarias:
12 Experimenta, peço-te, os teus servos dez dias; e que se nos deem legumes a comer e água a beber.
13 Então, se veja diante de ti a nossa aparência e a dos jovens que comem das finas iguarias do rei; e, segundo vires, age com os teus servos.
14 Ele atendeu e os experimentou dez dias.
15 No fim dos dez dias, a sua aparência era melhor; estavam eles mais robustos do que todos os jovens que comiam das finas iguarias do rei.
16 Com isto, o cozinheiro-chefe tirou deles as finas iguarias e o vinho que deviam beber e lhes dava legumes.
17 Ora, a estes quatro jovens Deus deu o conhecimento e a inteligência em toda cultura e sabedoria; mas a Daniel deu inteligência de todas as visões e sonhos.
18 Vencido o tempo determinado pelo rei para que os trouxessem, o chefe dos eunucos os trouxe à presença de Nabucodonosor.
19 Então, o rei falou com eles; e, entre todos, não foram achados outros como Daniel, Hananias, Misael e Azarias; por isso, passaram a assistir diante do rei.
20 Em toda matéria de sabedoria e de inteligência sobre que o rei lhes fez perguntas, os achou dez vezes mais doutos do que todos os magos e encantadores que havia em todo o seu reino.
21 Daniel continuou até ao primeiro ano do rei Ciro.*
1 No segundo ano do reinado de Nabucodonosor, teve este um sonho; o seu espírito se perturbou, e passou-se-lhe o sono.
2 Então, o rei mandou chamar os magos, os encantadores, os feiticeiros e os caldeus, para que declarassem ao rei quais lhe foram os sonhos; eles vieram e se apresentaram diante do rei.
3 Disse-lhes o rei: Tive um sonho, e para sabê-lo está perturbado o meu espírito.
4 Os caldeus disseram ao rei em aramaico: Ó rei, vive eternamente! Dize o sonho a teus servos, e daremos a interpretação.
5 Respondeu o rei e disse aos caldeus: Uma coisa é certa: se não me fizerdes saber o sonho e a sua interpretação, sereis despedaçados, e as vossas casas serão feitas monturo;
6 mas, se me declarardes o sonho e a sua interpretação, recebereis de mim dádivas, prêmios e grandes honras; portanto, declarai-me o sonho e a sua interpretação.
7 Responderam segunda vez e disseram: Diga o rei o sonho a seus servos, e lhe daremos a interpretação.
8 Tornou o rei e disse: Bem percebo que quereis ganhar tempo, porque vedes que o que eu disse está resolvido,
9 isto é: se não me fazeis saber o sonho, uma só sentença será a vossa; pois combinastes palavras mentirosas e perversas para as proferirdes na minha presença, até que se mude a situação; portanto, dizei-me o sonho, e saberei que me podeis dar-lhe a interpretação.
10 Responderam os caldeus na presença do rei e disseram: Não há mortal sobre a terra que possa revelar o que o rei exige; pois jamais houve rei, por grande e poderoso que tivesse sido, que exigisse semelhante coisa de algum mago, encantador ou caldeu.
11 A coisa que o rei exige é difícil, e ninguém há que a possa revelar diante do rei, senão os deuses, e estes não moram com os homens.
12 Então, o rei muito se irou e enfureceu; e ordenou que matassem a todos os sábios da Babilônia.
13 Saiu o decreto, segundo o qual deviam ser mortos os sábios; e buscaram a Daniel e aos seus companheiros, para que fossem mortos.
14 Então, Daniel falou, avisada e prudentemente, a Arioque, chefe da guarda do rei, que tinha saído para matar os sábios da Babilônia.
15 E disse a Arioque, encarregado do rei: Por que é tão severo o mandado do rei? Então, Arioque explicou o caso a Daniel.
16 Foi Daniel ter com o rei e lhe pediu designasse o tempo, e ele revelaria ao rei a interpretação.
17 Então, Daniel foi para casa e fez saber o caso a Hananias, Misael e Azarias, seus companheiros,
18 para que pedissem misericórdia ao Deus do céu sobre este mistério, a fim de que Daniel e seus companheiros não perecessem com o resto dos sábios da Babilônia.
19 Então, foi revelado o mistério a Daniel numa visão de noite; Daniel bendisse o Deus do céu.
20 Disse Daniel: Seja bendito o nome de Deus, de eternidade a eternidade, porque dele é a sabedoria e o poder;
21 é ele quem muda o tempo e as estações, remove reis e estabelece reis; ele dá sabedoria aos sábios e entendimento aos inteligentes.
22 Ele revela o profundo e o escondido; conhece o que está em trevas, e com ele mora a luz.
23 A ti, ó Deus de meus pais, eu te rendo graças e te louvo, porque me deste sabedoria e poder; e, agora, me fizeste saber o que te pedimos, porque nos fizeste saber este caso do rei.
24 Por isso, Daniel foi ter com Arioque, ao qual o rei tinha constituído para exterminar os sábios da Babilônia; entrou e lhe disse: Não mates os sábios da Babilônia; introduze-me na presença do rei, e revelarei ao rei a interpretação.
25 Então, Arioque depressa introduziu Daniel na presença do rei e lhe disse: Achei um dentre os filhos dos cativos de Judá, o qual revelará ao rei a interpretação.
26 Respondeu o rei e disse a Daniel, cujo nome era Beltessazar: Podes tu fazer-me saber o que vi no sonho e a sua interpretação?
27 Respondeu Daniel na presença do rei e disse: O mistério que o rei exige, nem encantadores, nem magos nem astrólogos o podem revelar ao rei;
28 mas há um Deus no céu, o qual revela os mistérios, pois fez saber ao rei Nabucodonosor o que há de ser nos últimos dias. O teu sonho e as visões da tua cabeça, quando estavas no teu leito, são estas:
29 Estando tu, ó rei, no teu leito, surgiram-te pensamentos a respeito do que há de ser depois disto. Aquele, pois, que revela mistérios te revelou o que há de ser.
30 E a mim me foi revelado este mistério, não porque haja em mim mais sabedoria do que em todos os viventes, mas para que a interpretação se fizesse saber ao rei, e para que entendesses as cogitações da tua mente.
31 Tu, ó rei, estavas vendo, e eis aqui uma grande estátua; esta, que era imensa e de extraordinário esplendor, estava em pé diante de ti; e a sua aparência era terrível.
32 A cabeça era de fino ouro, o peito e os braços, de prata, o ventre e os quadris, de bronze;
33 as pernas, de ferro, os pés, em parte, de ferro, em parte, de barro.
34 Quando estavas olhando, uma pedra foi cortada sem auxílio de mãos, feriu a estátua nos pés de ferro e de barro e os esmiuçou.
35 Então, foi juntamente esmiuçado o ferro, o barro, o bronze, a prata e o ouro, os quais se fizeram como a palha das eiras no estio, e o vento os levou, e deles não se viram mais vestígios. Mas a pedra que feriu a estátua se tornou em grande montanha, que encheu toda a terra.
36 Este é o sonho; e também a sua interpretação diremos ao rei.
37 Tu, ó rei, rei de reis, a quem o Deus do céu conferiu o reino, o poder, a força e a glória;
38 a cujas mãos foram entregues os filhos dos homens, onde quer que eles habitem, e os animais do campo e as aves do céu, para que dominasses sobre todos eles, tu és a cabeça de ouro.
39 Depois de ti, se levantará outro reino, inferior ao teu; e um terceiro reino, de bronze, o qual terá domínio sobre toda a terra.
40 O quarto reino será forte como ferro; pois o ferro a tudo quebra e esmiúça; como o ferro quebra todas as coisas, assim ele fará em pedaços e esmiuçará.
41 Quanto ao que viste dos pés e dos artelhos, em parte, de barro de oleiro e, em parte, de ferro, será esse um reino dividido; contudo, haverá nele alguma coisa da firmeza do ferro, pois que viste o ferro misturado com barro de lodo.
42 Como os artelhos dos pés eram, em parte, de ferro e, em parte, de barro, assim, por uma parte, o reino será forte e, por outra, será frágil.
43 Quanto ao que viste do ferro misturado com barro de lodo, misturar-se-ão mediante casamento, mas não se ligarão um ao outro, assim como o ferro não se mistura com o barro.
44 Mas, nos dias destes reis, o Deus do céu suscitará um reino que não será jamais destruído; este reino não passará a outro povo; esmiuçará e consumirá todos estes reinos, mas ele mesmo subsistirá para sempre,
45 como viste que do monte foi cortada uma pedra, sem auxílio de mãos, e ela esmiuçou o ferro, o bronze, o barro, a prata e o ouro. O Grande Deus fez saber ao rei o que há de ser futuramente. Certo é o sonho, e fiel, a sua interpretação.
46 Então, o rei Nabucodonosor se inclinou, e se prostrou rosto em terra perante Daniel, e ordenou que lhe fizessem oferta de manjares e suaves perfumes.
47 Disse o rei a Daniel: Certamente, o vosso Deus é o Deus dos deuses, e o Senhor dos reis, e o revelador de mistérios, pois pudeste revelar este mistério.
48 Então, o rei engrandeceu a Daniel, e lhe deu muitos e grandes presentes, e o pôs por governador de toda a província da Babilônia, como também o fez chefe supremo de todos os sábios da Babilônia.
49 A pedido de Daniel, constituiu o rei a Sadraque, Mesaque e Abede-Nego sobre os negócios da província da Babilônia; Daniel, porém, permaneceu na corte do rei.*
1 O rei Nabucodonosor fez uma imagem de ouro que tinha sessenta côvados de altura e seis de largura; levantou-a no campo de Dura, na província da Babilônia.
2 Então, o rei Nabucodonosor mandou ajuntar os sátrapas, os prefeitos, os governadores, os juízes, os tesoureiros, os magistrados, os conselheiros e todos os oficiais das províncias, para que viessem à consagração da imagem que o rei Nabucodonosor tinha levantado.
3 Então, se ajuntaram os sátrapas, os prefeitos, os governadores, os juízes, os tesoureiros, os magistrados, os conselheiros e todos os oficiais das províncias, para a consagração da imagem que o rei Nabucodonosor tinha levantado; e estavam em pé diante da imagem que Nabucodonosor tinha levantado.
4 Nisto, o arauto apregoava em alta voz: Ordena-se a vós outros, ó povos, nações e homens de todas as línguas:
5 no momento em que ouvirdes o som da trombeta, do pífaro, da harpa, da cítara, do saltério, da gaita de foles e de toda sorte de música, vos prostrareis e adorareis a imagem de ouro que o rei Nabucodonosor levantou.
6 Qualquer que se não prostrar e não a adorar será, no mesmo instante, lançado na fornalha de fogo ardente.
7 Portanto, quando todos os povos ouviram o som da trombeta, do pífaro, da harpa, da cítara, do saltério e de toda sorte de música, se prostraram os povos, nações e homens de todas as línguas e adoraram a imagem de ouro que o rei Nabucodonosor tinha levantado.
8 Ora, no mesmo instante, se chegaram alguns homens caldeus e acusaram os judeus;
9 disseram ao rei Nabucodonosor: Ó rei, vive eternamente!
10 Tu, ó rei, baixaste um decreto pelo qual todo homem que ouvisse o som da trombeta, do pífaro, da harpa, da cítara, do saltério, da gaita de foles e de toda sorte de música se prostraria e adoraria a imagem de ouro;
11 e qualquer que não se prostrasse e não adorasse seria lançado na fornalha de fogo ardente.
12 Há uns homens judeus, que tu constituíste sobre os negócios da província da Babilônia: Sadraque, Mesaque e Abede-Nego; estes homens, ó rei, não fizeram caso de ti, a teus deuses não servem, nem adoram a imagem de ouro que levantaste.
13 Então, Nabucodonosor, irado e furioso, mandou chamar Sadraque, Mesaque e Abede-Nego. E trouxeram a estes homens perante o rei.
14 Falou Nabucodonosor e lhes disse: É verdade, ó Sadraque, Mesaque e Abede-Nego, que vós não servis a meus deuses, nem adorais a imagem de ouro que levantei?
15 Agora, pois, estai dispostos e, quando ouvirdes o som da trombeta, do pífaro, da cítara, da harpa, do saltério, da gaita de foles, prostrai-vos e adorai a imagem que fiz; porém, se não a adorardes, sereis, no mesmo instante, lançados na fornalha de fogo ardente. E quem é o deus que vos poderá livrar das minhas mãos?
16 Responderam Sadraque, Mesaque e Abede-Nego ao rei: Ó Nabucodonosor, quanto a isto não necessitamos de te responder.
17 Se o nosso Deus, a quem servimos, quer livrar-nos, ele nos livrará da fornalha de fogo ardente e das tuas mãos, ó rei.
18 Se não, fica sabendo, ó rei, que não serviremos a teus deuses, nem adoraremos a imagem de ouro que levantaste.
19 Então, Nabucodonosor se encheu de fúria e, transtornado o aspecto do seu rosto contra Sadraque, Mesaque e Abede-Nego, ordenou que se acendesse a fornalha sete vezes mais do que se costumava.
20 Ordenou aos homens mais poderosos que estavam no seu exército que atassem a Sadraque, Mesaque e Abede-Nego e os lançassem na fornalha de fogo ardente.
21 Então, estes homens foram atados com os seus mantos, suas túnicas e chapéus e suas outras roupas e foram lançados na fornalha sobremaneira acesa.
22 Porque a palavra do rei era urgente e a fornalha estava sobremaneira acesa, as chamas do fogo mataram os homens que lançaram de cima para dentro a Sadraque, Mesaque e Abede-Nego.
23 Estes três homens, Sadraque, Mesaque e Abede-Nego, caíram atados dentro da fornalha sobremaneira acesa.
24 Então, o rei Nabucodonosor se espantou, e se levantou depressa, e disse aos seus conselheiros: Não lançamos nós três homens atados dentro do fogo? Responderam ao rei: É verdade, ó rei.
25 Tornou ele e disse: Eu, porém, vejo quatro homens soltos, que andam passeando dentro do fogo, sem nenhum dano; e o aspecto do quarto é semelhante a um filho dos deuses.
26 Então, se chegou Nabucodonosor à porta da fornalha sobremaneira acesa, falou e disse: Sadraque, Mesaque e Abede-Nego, servos do Deus Altíssimo, saí e vinde! Então, Sadraque, Mesaque e Abede-Nego saíram do meio do fogo.
27 Ajuntaram-se os sátrapas, os prefeitos, os governadores e conselheiros do rei e viram que o fogo não teve poder algum sobre os corpos destes homens; nem foram chamuscados os cabelos da sua cabeça, nem os seus mantos se mudaram, nem cheiro de fogo passara sobre eles.
28 Falou Nabucodonosor e disse: Bendito seja o Deus de Sadraque, Mesaque e Abede-Nego, que enviou o seu anjo e livrou os seus servos, que confiaram nele, pois não quiseram cumprir a palavra do rei, preferindo entregar o seu corpo, a servirem e adorarem a qualquer outro deus, senão ao seu Deus.
29 Portanto, faço um decreto pelo qual todo povo, nação e língua que disser blasfêmia contra o Deus de Sadraque, Mesaque e Abede-Nego seja despedaçado, e as suas casas sejam feitas em monturo; porque não há outro deus que possa livrar como este.
30 Então, o rei fez prosperar a Sadraque, Mesaque e Abede-Nego na província da Babilônia.*
1 O rei Nabucodonosor a todos os povos, nações e homens de todas as línguas, que habitam em toda a terra: Paz vos seja multiplicada!
2 Pareceu-me bem fazer conhecidos os sinais e maravilhas que Deus, o Altíssimo, tem feito para comigo.
3 Quão grandes são os seus sinais, e quão poderosas, as suas maravilhas! O seu reino é reino sempiterno, e o seu domínio, de geração em geração.
4 Eu, Nabucodonosor, estava tranquilo em minha casa e feliz no meu palácio.
5 Tive um sonho, que me espantou; e, quando estava no meu leito, os pensamentos e as visões da minha cabeça me turbaram.
6 Por isso, expedi um decreto, pelo qual fossem introduzidos à minha presença todos os sábios da Babilônia, para que me fizessem saber a interpretação do sonho.
7 Então, entraram os magos, os encantadores, os caldeus e os feiticeiros, e lhes contei o sonho; mas não me fizeram saber a sua interpretação.
8 Por fim, se me apresentou Daniel, cujo nome é Beltessazar, segundo o nome do meu deus, e no qual há o espírito dos deuses santos; e eu lhe contei o sonho, dizendo:
9 Beltessazar, chefe dos magos, eu sei que há em ti o espírito dos deuses santos, e nenhum mistério te é difícil; eis as visões do sonho que eu tive; dize-me a sua interpretação.
10 Eram assim as visões da minha cabeça quando eu estava no meu leito: eu estava olhando e vi uma árvore no meio da terra, cuja altura era grande;
11 crescia a árvore e se tornava forte, de maneira que a sua altura chegava até ao céu; e era vista até aos confins da terra.
12 A sua folhagem era formosa, e o seu fruto, abundante, e havia nela sustento para todos; debaixo dela os animais do campo achavam sombra, e as aves do céu faziam morada nos seus ramos, e todos os seres viventes se mantinham dela.
13 No meu sonho, quando eu estava no meu leito, vi um vigilante, um santo, que descia do céu,
14 clamando fortemente e dizendo: Derribai a árvore, cortai-lhe os ramos, derriçai-lhe as folhas, espalhai o seu fruto; afugentem-se os animais de debaixo dela e as aves, dos seus ramos.
15 Mas a cepa, com as raízes, deixai na terra, atada com cadeias de ferro e de bronze, na erva do campo. Seja ela molhada do orvalho do céu, e a sua porção seja, com os animais, a erva da terra.
16 Mude-se-lhe o coração, para que não seja mais coração de homem, e lhe seja dado coração de animal; e passem sobre ela sete tempos.
17 Esta sentença é por decreto dos vigilantes, e esta ordem, por mandado dos santos; a fim de que conheçam os viventes que o Altíssimo tem domínio sobre o reino dos homens; e o dá a quem quer e até ao mais humilde dos homens constitui sobre eles.
18 Isto vi eu, rei Nabucodonosor, em sonhos. Tu, pois, ó Beltessazar, dize a interpretação, porquanto todos os sábios do meu reino não me puderam fazer saber a interpretação, mas tu podes; pois há em ti o espírito dos deuses santos.
19 Então, Daniel, cujo nome era Beltessazar, esteve atônito por algum tempo, e os seus pensamentos o turbavam. Então, lhe falou o rei e disse: Beltessazar, não te perturbe o sonho, nem a sua interpretação. Respondeu Beltessazar e disse: Senhor meu, o sonho seja contra os que te têm ódio, e a sua interpretação, para os teus inimigos.
20 A árvore que viste, que cresceu e se tornou forte, cuja altura chegou até ao céu, e que foi vista por toda a terra,
21 cuja folhagem era formosa, e o seu fruto, abundante, e em que para todos havia sustento, debaixo da qual os animais do campo achavam sombra, e em cujos ramos as aves do céu faziam morada,
22 és tu, ó rei, que cresceste e vieste a ser forte; a tua grandeza cresceu e chega até ao céu, e o teu domínio, até à extremidade da terra.
23 Quanto ao que viu o rei, um vigilante, um santo, que descia do céu e que dizia: Cortai a árvore e destruí-a, mas a cepa com as raízes deixai na terra, atada com cadeias de ferro e de bronze, na erva do campo; seja ela molhada do orvalho do céu, e a sua porção seja com os animais do campo, até que passem sobre ela sete tempos,
24 esta é a interpretação, ó rei, e este é o decreto do Altíssimo, que virá contra o rei, meu senhor:
25 serás expulso de entre os homens, e a tua morada será com os animais do campo, e dar-te-ão a comer ervas como aos bois, e serás molhado do orvalho do céu; e passar-se-ão sete tempos por cima de ti, até que conheças que o Altíssimo tem domínio sobre o reino dos homens e o dá a quem quer.
26 Quanto ao que foi dito, que se deixasse a cepa da árvore com as suas raízes, o teu reino tornará a ser teu, depois que tiveres conhecido que o céu domina.
27 Portanto, ó rei, aceita o meu conselho e põe termo, pela justiça, em teus pecados e em tuas iniquidades, usando de misericórdia para com os pobres; e talvez se prolongue a tua tranquilidade.
28 Todas estas coisas sobrevieram ao rei Nabucodonosor.
29 Ao cabo de doze meses, passeando sobre o palácio real da cidade de Babilônia,
30 falou o rei e disse: Não é esta a grande Babilônia que eu edifiquei para a casa real, com o meu grandioso poder e para glória da minha majestade?
31 Falava ainda o rei quando desceu uma voz do céu: A ti se diz, ó rei Nabucodonosor: Já passou de ti o reino.
32 Serás expulso de entre os homens, e a tua morada será com os animais do campo; e far-te-ão comer ervas como os bois, e passar-se-ão sete tempos por cima de ti, até que aprendas que o Altíssimo tem domínio sobre o reino dos homens e o dá a quem quer.
33 No mesmo instante, se cumpriu a palavra sobre Nabucodonosor; e foi expulso de entre os homens e passou a comer erva como os bois, o seu corpo foi molhado do orvalho do céu, até que lhe cresceram os cabelos como as penas da águia, e as suas unhas, como as das aves.
34 Mas ao fim daqueles dias, eu, Nabucodonosor, levantei os olhos ao céu, tornou-me a vir o entendimento, e eu bendisse o Altíssimo, e louvei, e glorifiquei ao que vive para sempre, cujo domínio é sempiterno, e cujo reino é de geração em geração.
35 Todos os moradores da terra são por ele reputados em nada; e, segundo a sua vontade, ele opera com o exército do céu e os moradores da terra; não há quem lhe possa deter a mão, nem lhe dizer: Que fazes?
36 Tão logo me tornou a vir o entendimento, também, para a dignidade do meu reino, tornou-me a vir a minha majestade e o meu resplendor; buscaram-me os meus conselheiros e os meus grandes; fui restabelecido no meu reino, e a mim se me ajuntou extraordinária grandeza.
37 Agora, pois, eu, Nabucodonosor, louvo, exalço e glorifico ao Rei do céu, porque todas as suas obras são verdadeiras, e os seus caminhos, justos, e pode humilhar aos que andam na soberba.*
1 O rei Belsazar deu um grande banquete a mil dos seus grandes e bebeu vinho na presença dos mil.
2 Enquanto Belsazar bebia e apreciava o vinho, mandou trazer os utensílios de ouro e de prata que Nabucodonosor, seu pai, tirara do templo, que estava em Jerusalém, para que neles bebessem o rei e os seus grandes, as suas mulheres e concubinas.
3 Então, trouxeram os utensílios de ouro, que foram tirados do templo da Casa de Deus que estava em Jerusalém, e beberam neles o rei, os seus grandes e as suas mulheres e concubinas.
4 Beberam o vinho e deram louvores aos deuses de ouro, de prata, de bronze, de ferro, de madeira e de pedra.
5 No mesmo instante, apareceram uns dedos de mão de homem e escreviam, defronte do candeeiro, na caiadura da parede do palácio real; e o rei via os dedos que estavam escrevendo.
6 Então, se mudou o semblante do rei, e os seus pensamentos o turbaram; as juntas dos seus lombos se relaxaram, e os seus joelhos batiam um no outro.
7 O rei ordenou, em voz alta, que se introduzissem os encantadores, os caldeus e os feiticeiros; falou o rei e disse aos sábios da Babilônia: Qualquer que ler esta escritura e me declarar a sua interpretação será vestido de púrpura, trará uma cadeia de ouro ao pescoço e será o terceiro no meu reino.
8 Então, entraram todos os sábios do rei; mas não puderam ler a escritura, nem fazer saber ao rei a sua interpretação.
9 Com isto, se perturbou muito o rei Belsazar, e mudou-se-lhe o semblante; e os seus grandes estavam sobressaltados.
10 A rainha-mãe, por causa do que havia acontecido ao rei e aos seus grandes, entrou na casa do banquete e disse: Ó rei, vive eternamente! Não te turbem os teus pensamentos, nem se mude o teu semblante.
11 Há no teu reino um homem que tem o espírito dos deuses santos; nos dias de teu pai, se achou nele luz, e inteligência, e sabedoria como a sabedoria dos deuses; teu pai, o rei Nabucodonosor, sim, teu pai, ó rei, o constituiu chefe dos magos, dos encantadores, dos caldeus e dos feiticeiros,
12 porquanto espírito excelente, conhecimento e inteligência, interpretação de sonhos, declaração de enigmas e solução de casos difíceis se acharam neste Daniel, a quem o rei pusera o nome de Beltessazar; chame-se, pois, a Daniel, e ele dará a interpretação.
13 Então, Daniel foi introduzido à presença do rei. Falou o rei e disse a Daniel: És tu aquele Daniel, dos cativos de Judá, que o rei, meu pai, trouxe de Judá?
14 Tenho ouvido dizer a teu respeito que o espírito dos deuses está em ti, e que em ti se acham luz, inteligência e excelente sabedoria.
15 Acabam de ser introduzidos à minha presença os sábios e os encantadores, para lerem esta escritura e me fazerem saber a sua interpretação; mas não puderam dar a interpretação destas palavras.
16 Eu, porém, tenho ouvido dizer de ti que podes dar interpretações e solucionar casos difíceis; agora, se puderes ler esta escritura e fazer-me saber a sua interpretação, serás vestido de púrpura, terás cadeia de ouro ao pescoço e serás o terceiro no meu reino.
17 Então, respondeu Daniel e disse na presença do rei: Os teus presentes fiquem contigo, e dá os teus prêmios a outrem; todavia, lerei ao rei a escritura e lhe farei saber a interpretação.
18 Ó rei! Deus, o Altíssimo, deu a Nabucodonosor, teu pai, o reino e grandeza, glória e majestade.
19 Por causa da grandeza que lhe deu, povos, nações e homens de todas as línguas tremiam e temiam diante dele; matava a quem queria e a quem queria deixava com vida; a quem queria exaltava e a quem queria abatia.
20 Quando, porém, o seu coração se elevou, e o seu espírito se tornou soberbo e arrogante, foi derribado do seu trono real, e passou dele a sua glória.
21 Foi expulso dentre os filhos dos homens, o seu coração foi feito semelhante ao dos animais, e a sua morada foi com os jumentos monteses; deram-lhe a comer erva como aos bois, e do orvalho do céu foi molhado o seu corpo, até que conheceu que Deus, o Altíssimo, tem domínio sobre o reino dos homens e a quem quer constitui sobre ele.
22 Tu, Belsazar, que és seu filho, não humilhaste o teu coração, ainda que sabias tudo isto.
23 E te levantaste contra o Senhor do céu, pois foram trazidos os utensílios da casa dele perante ti, e tu, e os teus grandes, e as tuas mulheres, e as tuas concubinas bebestes vinho neles; além disso, deste louvores aos deuses de prata, de ouro, de bronze, de ferro, de madeira e de pedra, que não veem, não ouvem, nem sabem; mas a Deus, em cuja mão está a tua vida e todos os teus caminhos, a ele não glorificaste.
24 Então, da parte dele foi enviada aquela mão que traçou esta escritura.
25 Esta, pois, é a escritura que se traçou: Mene, Mene, Tequel e Parsim.
26 Esta é a interpretação daquilo: Mene: Contou Deus o teu reino e deu cabo dele.
27 Tequel: Pesado foste na balança e achado em falta.
28 Peres: Dividido foi o teu reino e dado aos medos e aos persas.
29 Então, mandou Belsazar que vestissem Daniel de púrpura, e lhe pusessem cadeia de ouro ao pescoço, e proclamassem que passaria a ser o terceiro no governo do seu reino.
30 Naquela mesma noite, foi morto Belsazar, rei dos caldeus.
31 E Dario, o medo, com cerca de sessenta e dois anos, se apoderou do reino.*
1 Pareceu bem a Dario constituir sobre o reino a cento e vinte sátrapas, que estivessem por todo o reino;
2 e sobre eles, três presidentes, dos quais Daniel era um, aos quais estes sátrapas dessem conta, para que o rei não sofresse dano.
3 Então, o mesmo Daniel se distinguiu destes presidentes e sátrapas, porque nele havia um espírito excelente; e o rei pensava em estabelecê-lo sobre todo o reino.
4 Então, os presidentes e os sátrapas procuravam ocasião para acusar a Daniel a respeito do reino; mas não puderam achá-la, nem culpa alguma; porque ele era fiel, e não se achava nele nenhum erro nem culpa.
5 Disseram, pois, estes homens: Nunca acharemos ocasião alguma para acusar a este Daniel, se não a procurarmos contra ele na lei do seu Deus.
6 Então, estes presidentes e sátrapas foram juntos ao rei e lhe disseram: Ó rei Dario, vive eternamente!
7 Todos os presidentes do reino, os prefeitos e sátrapas, conselheiros e governadores concordaram em que o rei estabeleça um decreto e faça firme o interdito que todo homem que, por espaço de trinta dias, fizer petição a qualquer deus ou a qualquer homem e não a ti, ó rei, seja lançado na cova dos leões.
8 Agora, pois, ó rei, sanciona o interdito e assina a escritura, para que não seja mudada, segundo a lei dos medos e dos persas, que se não pode revogar.
9 Por esta causa, o rei Dario assinou a escritura e o interdito.
10 Daniel, pois, quando soube que a escritura estava assinada, entrou em sua casa e, em cima, no seu quarto, onde havia janelas abertas do lado de Jerusalém, três vezes por dia, se punha de joelhos, e orava, e dava graças, diante do seu Deus, como costumava fazer.
11 Então, aqueles homens foram juntos, e, tendo achado a Daniel a orar e a suplicar, diante do seu Deus,
12 se apresentaram ao rei, e, a respeito do interdito real, lhe disseram: Não assinaste um interdito que, por espaço de trinta dias, todo homem que fizesse petição a qualquer deus ou a qualquer homem e não a ti, ó rei, fosse lançado na cova dos leões? Respondeu o rei e disse: Esta palavra é certa, segundo a lei dos medos e dos persas, que se não pode revogar.
13 Então, responderam e disseram ao rei: Esse Daniel, que é dos exilados de Judá, não faz caso de ti, ó rei, nem do interdito que assinaste; antes, três vezes por dia, faz a sua oração.
14 Tendo o rei ouvido estas coisas, ficou muito penalizado e determinou consigo mesmo livrar a Daniel; e, até ao pôr do sol, se empenhou por salvá-lo.
15 Então, aqueles homens foram juntos ao rei e lhe disseram: Sabe, ó rei, que é lei dos medos e dos persas que nenhum interdito ou decreto que o rei sancione se pode mudar.
16 Então, o rei ordenou que trouxessem a Daniel e o lançassem na cova dos leões. Disse o rei a Daniel: O teu Deus, a quem tu continuamente serves, que ele te livre.
17 Foi trazida uma pedra e posta sobre a boca da cova; selou-a o rei com o seu próprio anel e com o dos seus grandes, para que nada se mudasse a respeito de Daniel.
18 Então, o rei se dirigiu para o seu palácio, passou a noite em jejum e não deixou trazer à sua presença instrumentos de música; e fugiu dele o sono.
19 Pela manhã, ao romper do dia, levantou-se o rei e foi com pressa à cova dos leões.
20 Chegando-se ele à cova, chamou por Daniel com voz triste; disse o rei a Daniel: Daniel, servo do Deus vivo! Dar-se-ia o caso que o teu Deus, a quem tu continuamente serves, tenha podido livrar-te dos leões?
21 Então, Daniel falou ao rei: Ó rei, vive eternamente!
22 O meu Deus enviou o seu anjo e fechou a boca aos leões, para que não me fizessem dano, porque foi achada em mim inocência diante dele; também contra ti, ó rei, não cometi delito algum.
23 Então, o rei se alegrou sobremaneira e mandou tirar a Daniel da cova; assim, foi tirado Daniel da cova, e nenhum dano se achou nele, porque crera no seu Deus.
24 Ordenou o rei, e foram trazidos aqueles homens que tinham acusado a Daniel, e foram lançados na cova dos leões, eles, seus filhos e suas mulheres; e ainda não tinham chegado ao fundo da cova, e já os leões se apoderaram deles, e lhes esmigalharam todos os ossos.
25 Então, o rei Dario escreveu aos povos, nações e homens de todas as línguas que habitam em toda a terra: Paz vos seja multiplicada!
26 Faço um decreto pelo qual, em todo o domínio do meu reino, os homens tremam e temam perante o Deus de Daniel, porque ele é o Deus vivo e que permanece para sempre; o seu reino não será destruído, e o seu domínio não terá fim.
27 Ele livra, e salva, e faz sinais e maravilhas no céu e na terra; foi ele quem livrou a Daniel do poder dos leões.
28 Daniel, pois, prosperou no reinado de Dario e no reinado de Ciro, o persa.*
1 No primeiro ano de Belsazar, rei da Babilônia, teve Daniel um sonho e visões ante seus olhos, quando estava no seu leito; escreveu logo o sonho e relatou a suma de todas as coisas.
2 Falou Daniel e disse: Eu estava olhando, durante a minha visão da noite, e eis que os quatro ventos do céu agitavam o mar Grande.
3 Quatro animais, grandes, diferentes uns dos outros, subiam do mar.
4 O primeiro era como leão e tinha asas de águia; enquanto eu olhava, foram-lhe arrancadas as asas, foi levantado da terra e posto em dois pés, como homem; e lhe foi dada mente de homem.
5 Continuei olhando, e eis aqui o segundo animal, semelhante a um urso, o qual se levantou sobre um dos seus lados; na boca, entre os dentes, trazia três costelas; e lhe diziam: Levanta-te, devora muita carne.
6 Depois disto, continuei olhando, e eis aqui outro, semelhante a um leopardo, e tinha nas costas quatro asas de ave; tinha também este animal quatro cabeças, e foi-lhe dado domínio.
7 Depois disto, eu continuava olhando nas visões da noite, e eis aqui o quarto animal, terrível, espantoso e sobremodo forte, o qual tinha grandes dentes de ferro; ele devorava, e fazia em pedaços, e pisava aos pés o que sobejava; era diferente de todos os animais que apareceram antes dele e tinha dez chifres.
8 Estando eu a observar os chifres, eis que entre eles subiu outro pequeno, diante do qual três dos primeiros chifres foram arrancados; e eis que neste chifre havia olhos, como os de homem, e uma boca que falava com insolência.
9 Continuei olhando, até que foram postos uns tronos, e o Ancião de Dias se assentou; sua veste era branca como a neve, e os cabelos da cabeça, como a pura lã; o seu trono eram chamas de fogo, e suas rodas eram fogo ardente.
10 Um rio de fogo manava e saía de diante dele; milhares de milhares o serviam, e miríades de miríades estavam diante dele; assentou-se o tribunal, e se abriram os livros.
11 Então, estive olhando, por causa da voz das insolentes palavras que o chifre proferia; estive olhando e vi que o animal foi morto, e o seu corpo desfeito e entregue para ser queimado.
12 Quanto aos outros animais, foi-lhes tirado o domínio; todavia, foi-lhes dada prolongação de vida por um prazo e um tempo.
13 Eu estava olhando nas minhas visões da noite, e eis que vinha com as nuvens do céu um como o Filho do Homem, e dirigiu-se ao Ancião de Dias, e o fizeram chegar até ele.
14 Foi-lhe dado domínio, e glória, e o reino, para que os povos, nações e homens de todas as línguas o servissem; o seu domínio é domínio eterno, que não passará, e o seu reino jamais será destruído.
15 Quanto a mim, Daniel, o meu espírito foi alarmado dentro de mim, e as visões da minha cabeça me perturbaram.
16 Cheguei-me a um dos que estavam perto e lhe pedi a verdade acerca de tudo isto. Assim, ele me disse e me fez saber a interpretação das coisas:
17 Estes grandes animais, que são quatro, são quatro reis que se levantarão da terra.
18 Mas os santos do Altíssimo receberão o reino e o possuirão para todo o sempre, de eternidade em eternidade.
19 Então, tive desejo de conhecer a verdade a respeito do quarto animal, que era diferente de todos os outros, muito terrível, cujos dentes eram de ferro, cujas unhas eram de bronze, que devorava, fazia em pedaços e pisava aos pés o que sobejava;
20 e também a respeito dos dez chifres que tinha na cabeça e do outro que subiu, diante do qual caíram três, daquele chifre que tinha olhos e uma boca que falava com insolência e parecia mais robusto do que os seus companheiros.
21 Eu olhava e eis que este chifre fazia guerra contra os santos e prevalecia contra eles,
22 até que veio o Ancião de Dias e fez justiça aos santos do Altíssimo; e veio o tempo em que os santos possuíram o reino.
23 Então, ele disse: O quarto animal será um quarto reino na terra, o qual será diferente de todos os reinos; e devorará toda a terra, e a pisará aos pés, e a fará em pedaços.
24 Os dez chifres correspondem a dez reis que se levantarão daquele mesmo reino; e, depois deles, se levantará outro, o qual será diferente dos primeiros, e abaterá a três reis.
25 Proferirá palavras contra o Altíssimo, magoará os santos do Altíssimo e cuidará em mudar os tempos e a lei; e os santos lhe serão entregues nas mãos, por um tempo, dois tempos e metade de um tempo.
26 Mas, depois, se assentará o tribunal para lhe tirar o domínio, para o destruir e o consumir até ao fim.
27 O reino, e o domínio, e a majestade dos reinos debaixo de todo o céu serão dados ao povo dos santos do Altíssimo; o seu reino será reino eterno, e todos os domínios o servirão e lhe obedecerão.
28 Aqui, terminou o assunto. Quanto a mim, Daniel, os meus pensamentos muito me perturbaram, e o meu rosto se empalideceu; mas guardei estas coisas no coração.*
1 No ano terceiro do reinado do rei Belsazar, eu, Daniel, tive uma visão depois daquela que eu tivera a princípio.
2 Quando a visão me veio, pareceu-me estar eu na cidadela de Susã, que é província de Elão, e vi que estava junto ao rio Ulai.
3 Então, levantei os olhos e vi, e eis que, diante do rio, estava um carneiro, o qual tinha dois chifres, e os dois chifres eram altos, mas um, mais alto do que o outro; e o mais alto subiu por último.
4 Vi que o carneiro dava marradas para o ocidente, e para o norte, e para o sul; e nenhum dos animais lhe podia resistir, nem havia quem pudesse livrar-se do seu poder; ele, porém, fazia segundo a sua vontade e, assim, se engrandecia.
5 Estando eu observando, eis que um bode vinha do ocidente sobre toda a terra, mas sem tocar no chão; este bode tinha um chifre notável entre os olhos;
6 dirigiu-se ao carneiro que tinha os dois chifres, o qual eu tinha visto diante do rio; e correu contra ele com todo o seu furioso poder.
7 Vi-o chegar perto do carneiro, e, enfurecido contra ele, o feriu e lhe quebrou os dois chifres, pois não havia força no carneiro para lhe resistir; e o bode o lançou por terra e o pisou aos pés, e não houve quem pudesse livrar o carneiro do poder dele.
8 O bode se engrandeceu sobremaneira; e, na sua força, quebrou-se-lhe o grande chifre, e em seu lugar saíram quatro chifres notáveis, para os quatro ventos do céu.
9 De um dos chifres saiu um chifre pequeno e se tornou muito forte para o sul, para o oriente e para a terra gloriosa.
10 Cresceu até atingir o exército dos céus; a alguns do exército e das estrelas lançou por terra e os pisou.
11 Sim, engrandeceu-se até ao príncipe do exército; dele tirou o sacrifício diário e o lugar do seu santuário foi deitado abaixo.
12 O exército lhe foi entregue, com o sacrifício diário, por causa das transgressões; e deitou por terra a verdade; e o que fez prosperou.
13 Depois, ouvi um santo que falava; e disse outro santo àquele que falava: Até quando durará a visão do sacrifício diário e da transgressão assoladora, visão na qual é entregue o santuário e o exército, a fim de serem pisados?
14 Ele me disse: Até duas mil e trezentas tardes e manhãs; e o santuário será purificado.
15 Havendo eu, Daniel, tido a visão, procurei entendê-la, e eis que se me apresentou diante uma como aparência de homem.
16 E ouvi uma voz de homem de entre as margens do Ulai, a qual gritou e disse: Gabriel, dá a entender a este a visão.
17 Veio, pois, para perto donde eu estava; ao chegar ele, fiquei amedrontado e prostrei-me com o rosto em terra; mas ele me disse: Entende, filho do homem, pois esta visão se refere ao tempo do fim.
18 Falava ele comigo quando caí sem sentidos, rosto em terra; ele, porém, me tocou e me pôs em pé no lugar onde eu me achava;
19 e disse: Eis que te farei saber o que há de acontecer no último tempo da ira, porque esta visão se refere ao tempo determinado do fim.
20 Aquele carneiro com dois chifres, que viste, são os reis da Média e da Pérsia;
21 mas o bode peludo é o rei da Grécia; o chifre grande entre os olhos é o primeiro rei;
22 o ter sido quebrado, levantando-se quatro em lugar dele, significa que quatro reinos se levantarão deste povo, mas não com força igual à que ele tinha.
23 Mas, no fim do seu reinado, quando os prevaricadores acabarem, levantar-se-á um rei de feroz catadura e especialista em intrigas.
24 Grande é o seu poder, mas não por sua própria força; causará estupendas destruições, prosperará e fará o que lhe aprouver; destruirá os poderosos e o povo santo.
25 Por sua astúcia nos seus empreendimentos, fará prosperar o engano, no seu coração se engrandecerá e destruirá a muitos que vivem despreocupadamente; levantar-se-á contra o Príncipe dos príncipes, mas será quebrado sem esforço de mãos humanas.
26 A visão da tarde e da manhã, que foi dita, é verdadeira; tu, porém, preserva a visão, porque se refere a dias ainda mui distantes.
27 Eu, Daniel, enfraqueci e estive enfermo alguns dias; então, me levantei e tratei dos negócios do rei. Espantava-me com a visão, e não havia quem a entendesse.*
1 No primeiro ano de Dario, filho de Assuero, da linhagem dos medos, o qual foi constituído rei sobre o reino dos caldeus,
2 no primeiro ano do seu reinado, eu, Daniel, entendi, pelos livros, que o número de anos, de que falara o Senhor ao profeta Jeremias, que haviam de durar as assolações de Jerusalém, era de setenta anos.
3 Voltei o rosto ao Senhor Deus, para o buscar com oração e súplicas, com jejum, pano de saco e cinza.
4 Orei ao Senhor, meu Deus, confessei e disse: ah! Senhor! Deus grande e temível, que guardas a aliança e a misericórdia para com os que te amam e guardam os teus mandamentos;
5 temos pecado e cometido iniquidades, procedemos perversamente e fomos rebeldes, apartando-nos dos teus mandamentos e dos teus juízos;
6 e não demos ouvidos aos teus servos, os profetas, que em teu nome falaram aos nossos reis, nossos príncipes e nossos pais, como também a todo o povo da terra.
7 A ti, ó Senhor, pertence a justiça, mas a nós, o corar de vergonha, como hoje se vê; aos homens de Judá, os moradores de Jerusalém, todo o Israel, quer os de perto, quer os de longe, em todas as terras por onde os tens lançado, por causa das suas transgressões que cometeram contra ti.
8 Ó Senhor, a nós pertence o corar de vergonha, aos nossos reis, aos nossos príncipes e aos nossos pais, porque temos pecado contra ti.
9 Ao Senhor, nosso Deus, pertence a misericórdia e o perdão, pois nos temos rebelado contra ele
10 e não obedecemos à voz do Senhor, nosso Deus, para andarmos nas suas leis, que nos deu por intermédio de seus servos, os profetas.
11 Sim, todo o Israel transgrediu a tua lei, desviando-se, para não obedecer à tua voz; por isso, a maldição e as imprecações que estão escritas na Lei de Moisés, servo de Deus, se derramaram sobre nós, porque temos pecado contra ti.
12 Ele confirmou a sua palavra, que falou contra nós e contra os nossos juízes que nos julgavam, e fez vir sobre nós grande mal, porquanto nunca, debaixo de todo o céu, aconteceu o que se deu em Jerusalém.
13 Como está escrito na Lei de Moisés, todo este mal nos sobreveio; apesar disso, não temos implorado o favor do Senhor, nosso Deus, para nos convertermos das nossas iniquidades e nos aplicarmos à tua verdade.
14 Por isso, o Senhor cuidou em trazer sobre nós o mal e o fez vir sobre nós; pois justo é o Senhor, nosso Deus, em todas as suas obras que faz, pois não obedecemos à sua voz.
15 Na verdade, ó Senhor, nosso Deus, que tiraste o teu povo da terra do Egito com mão poderosa, e a ti mesmo adquiriste renome, como hoje se vê, temos pecado e procedido perversamente.
16 Ó Senhor, segundo todas as tuas justiças, aparte-se a tua ira e o teu furor da tua cidade de Jerusalém, do teu santo monte, porquanto, por causa dos nossos pecados e por causa das iniquidades de nossos pais, se tornaram Jerusalém e o teu povo opróbrio para todos os que estão em redor de nós.
17 Agora, pois, ó Deus nosso, ouve a oração do teu servo e as suas súplicas e sobre o teu santuário assolado faze resplandecer o rosto, por amor do Senhor.
18 Inclina, ó Deus meu, os ouvidos e ouve; abre os olhos e olha para a nossa desolação e para a cidade que é chamada pelo teu nome, porque não lançamos as nossas súplicas perante a tua face fiados em nossas justiças, mas em tuas muitas misericórdias.
19 Ó Senhor, ouve; ó Senhor, perdoa; ó Senhor, atende-nos e age; não te retardes, por amor de ti mesmo, ó Deus meu; porque a tua cidade e o teu povo são chamados pelo teu nome.
20 Falava eu ainda, e orava, e confessava o meu pecado e o pecado do meu povo de Israel, e lançava a minha súplica perante a face do Senhor, meu Deus, pelo monte santo do meu Deus.
21 Falava eu, digo, falava ainda na oração, quando o homem Gabriel, que eu tinha observado na minha visão ao princípio, veio rapidamente, voando, e me tocou à hora do sacrifício da tarde.
22 Ele queria instruir-me, falou comigo e disse: Daniel, agora, saí para fazer-te entender o sentido.
23 No princípio das tuas súplicas, saiu a ordem, e eu vim, para to declarar, porque és mui amado; considera, pois, a coisa e entende a visão.
24 Setenta semanas estão determinadas sobre o teu povo e sobre a tua santa cidade, para fazer cessar a transgressão, para dar fim aos pecados, para expiar a iniquidade, para trazer a justiça eterna, para selar a visão e a profecia e para ungir o Santo dos Santos.
25 Sabe e entende: desde a saída da ordem para restaurar e para edificar Jerusalém, até ao Ungido, ao Príncipe, sete semanas e sessenta e duas semanas; as praças e as circunvalações se reedificarão, mas em tempos angustiosos.
26 Depois das sessenta e duas semanas, será morto o Ungido e já não estará; e o povo de um príncipe que há de vir destruirá a cidade e o santuário, e o seu fim será num dilúvio, e até ao fim haverá guerra; desolações são determinadas.
27 Ele fará firme aliança com muitos, por uma semana; na metade da semana, fará cessar o sacrifício e a oferta de manjares; sobre a asa das abominações virá o assolador, até que a destruição, que está determinada, se derrame sobre ele.*
1 No terceiro ano de Ciro, rei da Pérsia, foi revelada uma palavra a Daniel, cujo nome é Beltessazar; a palavra era verdadeira e envolvia grande conflito; ele entendeu a palavra e teve a inteligência da visão.
2 Naqueles dias, eu, Daniel, pranteei durante três semanas.
3 Manjar desejável não comi, nem carne, nem vinho entraram na minha boca, nem me ungi com óleo algum, até que passaram as três semanas inteiras.
4 No dia vinte e quatro do primeiro mês, estando eu à borda do grande rio Tigre,
5 levantei os olhos e olhei, e eis um homem vestido de linho, cujos ombros estavam cingidos de ouro puro de Ufaz;
6 o seu corpo era como o berilo, o seu rosto, como um relâmpago, os seus olhos, como tochas de fogo, os seus braços e os seus pés brilhavam como bronze polido; e a voz das suas palavras era como o estrondo de muita gente.
7 Só eu, Daniel, tive aquela visão; os homens que estavam comigo nada viram; não obstante, caiu sobre eles grande temor, e fugiram e se esconderam.
8 Fiquei, pois, eu só e contemplei esta grande visão, e não restou força em mim; o meu rosto mudou de cor e se desfigurou, e não retive força alguma.
9 Contudo, ouvi a voz das suas palavras; e, ouvindo-a, caí sem sentidos, rosto em terra.
10 Eis que certa mão me tocou, sacudiu-me e me pôs sobre os meus joelhos e as palmas das minhas mãos.
11 Ele me disse: Daniel, homem muito amado, está atento às palavras que te vou dizer; levanta-te sobre os pés, porque eis que te sou enviado. Ao falar ele comigo esta palavra, eu me pus em pé, tremendo.
12 Então, me disse: Não temas, Daniel, porque, desde o primeiro dia em que aplicaste o coração a compreender e a humilhar-te perante o teu Deus, foram ouvidas as tuas palavras; e, por causa das tuas palavras, é que eu vim.
13 Mas o príncipe do reino da Pérsia me resistiu por vinte e um dias; porém Miguel, um dos primeiros príncipes, veio para ajudar-me, e eu obtive vitória sobre os reis da Pérsia.
14 Agora, vim para fazer-te entender o que há de suceder ao teu povo nos últimos dias; porque a visão se refere a dias ainda distantes.
15 Ao falar ele comigo estas palavras, dirigi o olhar para a terra e calei.
16 E eis que uma como semelhança dos filhos dos homens me tocou os lábios; então, passei a falar e disse àquele que estava diante de mim: meu senhor, por causa da visão me sobrevieram dores, e não me ficou força alguma.
17 Como, pois, pode o servo do meu senhor falar com o meu senhor? Porque, quanto a mim, não me resta já força alguma, nem fôlego ficou em mim.
18 Então, me tornou a tocar aquele semelhante a um homem e me fortaleceu;
19 e disse: Não temas, homem muito amado! Paz seja contigo! Sê forte, sê forte. Ao falar ele comigo, fiquei fortalecido e disse: fala, meu senhor, pois me fortaleceste.
20 E ele disse: Sabes por que eu vim a ti? Eu tornarei a pelejar contra o príncipe dos persas; e, saindo eu, eis que virá o príncipe da Grécia.
21 Mas eu te declararei o que está expresso na escritura da verdade; e ninguém há que esteja ao meu lado contra aqueles, a não ser Miguel, vosso príncipe.*
1 Mas eu, no primeiro ano de Dario, o medo, me levantei para o fortalecer e animar.
2 Agora, eu te declararei a verdade: eis que ainda três reis se levantarão na Pérsia, e o quarto será cumulado de grandes riquezas mais do que todos; e, tornado forte por suas riquezas, empregará tudo contra o reino da Grécia.
3 Depois, se levantará um rei poderoso, que reinará com grande domínio e fará o que lhe aprouver.
4 Mas, no auge, o seu reino será quebrado e repartido para os quatro ventos do céu; mas não para a sua posteridade, nem tampouco segundo o poder com que reinou, porque o seu reino será arrancado e passará a outros fora de seus descendentes.
5 O rei do Sul será forte, como também um de seus príncipes; este será mais forte do que ele, e reinará, e será grande o seu domínio.
6 Mas, ao cabo de anos, eles se aliarão um com o outro; a filha do rei do Sul casará com o rei do Norte, para estabelecer a concórdia; ela, porém, não conservará a força do seu braço, e ele não permanecerá, nem o seu braço, porque ela será entregue, e bem assim os que a trouxeram, e seu pai, e o que a tomou por sua naqueles tempos.
7 Mas, de um renovo da linhagem dela, um se levantará em seu lugar, e avançará contra o exército do rei do Norte, e entrará na sua fortaleza, e agirá contra eles, e prevalecerá.
8 Também aos seus deuses com a multidão das suas imagens fundidas, com os seus objetos preciosos de prata e ouro levará como despojo para o Egito; por alguns anos, ele deixará em paz o rei do Norte.
9 Mas, depois, este avançará contra o reino do rei do Sul e tornará para a sua terra.
10 Os seus filhos farão guerra e reunirão numerosas forças; um deles virá apressadamente, arrasará tudo e passará adiante; e, voltando à guerra, a levará até à fortaleza do rei do Sul.
11 Então, este se exasperará, sairá e pelejará contra ele, contra o rei do Norte; este porá em campo grande multidão, mas a sua multidão será entregue nas mãos daquele.
12 A multidão será levada, e o coração dele se exaltará; ele derribará miríades, porém não prevalecerá.
13 Porque o rei do Norte tornará, e porá em campo multidão maior do que a primeira, e, ao cabo de tempos, isto é, de anos, virá à pressa com grande exército e abundantes provisões.
14 Naqueles tempos, se levantarão muitos contra o rei do Sul; também os dados à violência dentre o teu povo se levantarão para cumprirem a profecia, mas cairão.
15 O rei do Norte virá, levantará baluartes e tomará cidades fortificadas; os braços do Sul não poderão resistir, nem o seu povo escolhido, pois não haverá força para resistir.
16 O que, pois, vier contra ele fará o que bem quiser, e ninguém poderá resistir a ele; estará na terra gloriosa, e tudo estará em suas mãos.
17 Resolverá vir com a força de todo o seu reino, e entrará em acordo com ele, e lhe dará uma jovem em casamento, para destruir o seu reino; isto, porém, não vingará, nem será para a sua vantagem.
18 Depois, se voltará para as terras do mar e tomará muitas; mas um príncipe fará cessar-lhe o opróbrio e ainda fará recair este opróbrio sobre aquele.
19 Então, voltará para as fortalezas da sua própria terra; mas tropeçará, e cairá, e não será achado.
20 Levantar-se-á, depois, em lugar dele, um que fará passar um exator pela terra mais gloriosa do seu reino; mas, em poucos dias, será destruído, e isto sem ira nem batalha.
21 Depois, se levantará em seu lugar um homem vil, ao qual não tinham dado a dignidade real; mas ele virá caladamente e tomará o reino, com intrigas.
22 As forças inundantes serão arrasadas de diante dele; serão quebrantadas, como também o príncipe da aliança.
23 Apesar da aliança com ele, usará de engano; subirá e se tornará forte com pouca gente.
24 Virá também caladamente aos lugares mais férteis da província e fará o que nunca fizeram seus pais, nem os pais de seus pais: repartirá entre eles a presa, os despojos e os bens; e maquinará os seus projetos contra as fortalezas, mas por certo tempo.
25 Suscitará a sua força e o seu ânimo contra o rei do Sul, à frente de grande exército; o rei do Sul sairá à batalha com grande e mui poderoso exército, mas não prevalecerá, porque maquinarão projetos contra ele.
26 Os que comerem os seus manjares o destruirão, e o exército dele será arrasado, e muitos cairão traspassados.
27 Também estes dois reis se empenharão em fazer o mal e a uma só mesa falarão mentiras; porém isso não prosperará, porque o fim virá no tempo determinado.
28 Então, o homem vil tornará para a sua terra com grande riqueza, e o seu coração será contra a santa aliança; ele fará o que lhe aprouver e tornará para a sua terra.
29 No tempo determinado, tornará a avançar contra o Sul; mas não será nesta última vez como foi na primeira,
30 porque virão contra ele navios de Quitim, que lhe causarão tristeza; voltará, e se indignará contra a santa aliança, e fará o que lhe aprouver; e, tendo voltado, atenderá aos que tiverem desamparado a santa aliança.
31 Dele sairão forças que profanarão o santuário, a fortaleza nossa, e tirarão o sacrifício diário, estabelecendo a abominação desoladora.
32 Aos violadores da aliança, ele, com lisonjas, perverterá, mas o povo que conhece ao seu Deus se tornará forte e ativo.
33 Os sábios entre o povo ensinarão a muitos; todavia, cairão pela espada e pelo fogo, pelo cativeiro e pelo roubo, por algum tempo.
34 Ao caírem eles, serão ajudados com pequeno socorro; mas muitos se ajuntarão a eles com lisonjas.
35 Alguns dos sábios cairão para serem provados, purificados e embranquecidos, até ao tempo do fim, porque se dará ainda no tempo determinado.
36 Este rei fará segundo a sua vontade, e se levantará, e se engrandecerá sobre todo deus; contra o Deus dos deuses falará coisas incríveis e será próspero, até que se cumpra a indignação; porque aquilo que está determinado será feito.
37 Não terá respeito aos deuses de seus pais, nem ao desejo de mulheres, nem a qualquer deus, porque sobre tudo se engrandecerá.
38 Mas, em lugar dos deuses, honrará o deus das fortalezas; a um deus que seus pais não conheceram, honrará com ouro, com prata, com pedras preciosas e coisas agradáveis.
39 Com o auxílio de um deus estranho, agirá contra as poderosas fortalezas, e aos que o reconhecerem, multiplicar-lhes-á a honra, e fá-los-á reinar sobre muitos, e lhes repartirá a terra por prêmio.
40 No tempo do fim, o rei do Sul lutará com ele, e o rei do Norte arremeterá contra ele com carros, cavaleiros e com muitos navios, e entrará nas suas terras, e as inundará, e passará.
41 Entrará também na terra gloriosa, e muitos sucumbirão, mas do seu poder escaparão estes: Edom, e Moabe, e as primícias dos filhos de Amom.
42 Estenderá a mão também contra as terras, e a terra do Egito não escapará.
43 Apoderar-se-á dos tesouros de ouro e de prata e de todas as coisas preciosas do Egito; os líbios e os etíopes o seguirão.
44 Mas, pelos rumores do Oriente e do Norte, será perturbado e sairá com grande furor, para destruir e exterminar a muitos.
45 Armará as suas tendas palacianas entre os mares contra o glorioso monte santo; mas chegará ao seu fim, e não haverá quem o socorra.*
1 Nesse tempo, se levantará Miguel, o grande príncipe, o defensor dos filhos do teu povo, e haverá tempo de angústia, qual nunca houve, desde que houve nação até àquele tempo; mas, naquele tempo, será salvo o teu povo, todo aquele que for achado inscrito no livro.
2 Muitos dos que dormem no pó da terra ressuscitarão, uns para a vida eterna, e outros para vergonha e horror eterno.
3 Os que forem sábios, pois, resplandecerão como o fulgor do firmamento; e os que a muitos conduzirem à justiça, como as estrelas, sempre e eternamente.
4 Tu, porém, Daniel, encerra as palavras e sela o livro, até ao tempo do fim; muitos o esquadrinharão, e o saber se multiplicará.
5 Então, eu, Daniel, olhei, e eis que estavam em pé outros dois, um, de um lado do rio, o outro, do outro lado.
6 Um deles disse ao homem vestido de linho, que estava sobre as águas do rio: Quando se cumprirão estas maravilhas?
7 Ouvi o homem vestido de linho, que estava sobre as águas do rio, quando levantou a mão direita e a esquerda ao céu e jurou, por aquele que vive eternamente, que isso seria depois de um tempo, dois tempos e metade de um tempo. E, quando se acabar a destruição do poder do povo santo, estas coisas todas se cumprirão.
8 Eu ouvi, porém não entendi; então, eu disse: meu senhor, qual será o fim destas coisas?
9 Ele respondeu: Vai, Daniel, porque estas palavras estão encerradas e seladas até ao tempo do fim.
10 Muitos serão purificados, embranquecidos e provados; mas os perversos procederão perversamente, e nenhum deles entenderá, mas os sábios entenderão.
11 Depois do tempo em que o sacrifício diário for tirado, e posta a abominação desoladora, haverá ainda mil duzentos e noventa dias.
12 Bem-aventurado o que espera e chega até mil trezentos e trinta e cinco dias.
13 Tu, porém, segue o teu caminho até ao fim; pois descansarás e, ao fim dos dias, te levantarás para receber a tua herança.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Ezequiel','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)