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
1 Depois da morte de Saul, voltando Davi da derrota dos amalequitas e estando já dois dias em Ziclague,
2 sucedeu, ao terceiro dia, aparecer do arraial de Saul um homem com as vestes rotas e terra sobre a cabeça; em chegando ele a Davi, inclinou-se, lançando-se em terra.
3 Perguntou-lhe Davi: Donde vens? Ele respondeu: Fugi do arraial de Israel.
4 Disse-lhe Davi: Como foi lá isso? Conta-mo. Ele lhe respondeu: O povo fugiu da batalha, e muitos caíram e morreram, bem como Saul e Jônatas, seu filho.
5 Disse Davi ao moço que lhe dava as novas: Como sabes tu que Saul e Jônatas, seu filho, são mortos?
6 Então, disse o moço portador das notícias: Cheguei, por acaso, à montanha de Gilboa, e eis que Saul estava apoiado sobre a sua lança, e os carros e a cavalaria apertavam com ele.
7 Olhando ele para trás, viu-me e chamou-me. Eu disse: Eis-me aqui.
8 Ele me perguntou: Quem és tu? Eu respondi: Sou amalequita.
9 Então, me disse: Arremete sobre mim e mata-me, pois me sinto vencido de cãibra, mas o tino se acha ainda todo em mim.
10 Arremessei-me, pois, sobre ele e o matei, porque bem sabia eu que ele não viveria depois de ter caído. Tomei-lhe a coroa que trazia na cabeça e o bracelete e os trouxe aqui ao meu senhor.
11 Então, apanhou Davi as suas próprias vestes e as rasgou, e assim fizeram todos os homens que estavam com ele.
12 Prantearam, choraram e jejuaram até à tarde por Saul, e por Jônatas, seu filho, e pelo povo do Senhor, e pela casa de Israel, porque tinham caído à espada.
13 Então, perguntou Davi ao moço portador das notícias: Donde és tu? Ele respondeu: Sou filho de um homem estrangeiro, amalequita.
14 Davi lhe disse: Como não temeste estender a mão para matares o ungido do Senhor?
15 Então, chamou Davi a um dos moços e lhe disse: Vem, lança-te sobre esse homem. Ele o feriu, de sorte que morreu.
16 Disse-lhe Davi: O teu sangue seja sobre a tua cabeça, porque a tua própria boca testificou contra ti, dizendo: Matei o ungido do Senhor.
17 Pranteou Davi a Saul e a Jônatas, seu filho, com esta lamentação,
18 determinando que fosse ensinado aos filhos de Judá o Hino ao Arco, o qual está escrito no Livro dos Justos.
19 A tua glória, ó Israel, foi morta sobre os teus altos! Como caíram os valentes!
20 Não o noticieis em Gate, nem o publiqueis nas ruas de Asquelom, para que não se alegrem as filhas dos filisteus, nem saltem de contentamento as filhas dos incircuncisos.
21 Montes de Gilboa, não caia sobre vós nem orvalho, nem chuva, nem haja aí campos que produzam ofertas, pois neles foi profanado o escudo dos valentes, o escudo de Saul, que jamais será ungido com óleo.
22 Sem sangue dos feridos, sem gordura dos valentes, nunca se recolheu o arco de Jônatas, nem voltou vazia a espada de Saul.
23 Saul e Jônatas, queridos e amáveis, tanto na vida como na morte não se separaram! Eram mais ligeiros do que as águias, mais fortes do que os leões.
24 Vós, filhas de Israel, chorai por Saul, que vos vestia de rica escarlata, que vos punha sobre os vestidos adornos de ouro.
25 Como caíram os valentes no meio da peleja! Jônatas sobre os montes foi morto!
26 Angustiado estou por ti, meu irmão Jônatas; tu eras amabilíssimo para comigo! Excepcional era o teu amor, ultrapassando o amor de mulheres.
27 Como caíram os valentes, e pereceram as armas de guerra!*
1 Depois disto, consultou Davi ao Senhor, dizendo: Subirei a alguma das cidades de Judá? Respondeu-lhe o Senhor: Sobe. Perguntou Davi: Para onde subirei? Respondeu o Senhor: Para Hebrom.
2 Subiu Davi para lá, e também as suas duas mulheres, Ainoã, a jezreelita, e Abigail, a viúva de Nabal, o carmelita.
3 Fez Davi subir os homens que estavam com ele, cada um com sua família; e habitaram nas aldeias de Hebrom.
4 Então, vieram os homens de Judá e ungiram ali Davi rei sobre a casa de Judá. E informaram Davi de que os homens de Jabes-Gileade foram os que sepultaram Saul.
5 Então, enviou Davi mensageiros aos homens de Jabes-Gileade para dizer-lhes: Benditos do Senhor sejais vós, por esta humanidade para com vosso senhor, para com Saul, pois o sepultastes!
6 Agora, pois, o Senhor use convosco de misericórdia e fidelidade; eu vos recompensarei este bem que fizestes.
7 Agora, pois, sejam fortes as vossas mãos, e sede valentes, pois Saul, vosso senhor, é morto, e os da casa de Judá me ungiram rei sobre si.
8 Abner, filho de Ner, capitão do exército de Saul, tomou a Isbosete, filho de Saul, e o fez passar a Maanaim,
9 e o constituiu rei sobre Gileade, sobre os assuritas, sobre Jezreel, Efraim, Benjamim e sobre todo o Israel.
10 Da idade de quarenta anos era Isbosete, filho de Saul, quando começou a reinar sobre Israel, e reinou dois anos; somente a casa de Judá seguia a Davi.
11 O tempo que Davi reinou em Hebrom sobre a casa de Judá foram sete anos e seis meses.
12 Saiu Abner, filho de Ner, com os homens de Isbosete, filho de Saul, de Maanaim a Gibeão.
13 Saíram também Joabe, filho de Zeruia, e os homens de Davi e se encontraram uns com os outros perto do açude de Gibeão; pararam estes do lado de cá do açude, e aqueles, do lado de lá.
14 Disse Abner a Joabe: Levantem-se os moços e batam-se diante de nós. Respondeu Joabe: Levantem-se.
15 Então, se levantaram e avançaram em igual número: doze de Benjamim, da parte de Isbosete, filho de Saul, e doze dos homens de Davi.
16 Cada um lançou mão da cabeça do outro, meteu-lhe a espada no lado, e caíram juntamente; donde se chamou àquele lugar Campo das Espadas, que está junto a Gibeão.
17 Seguiu-se crua peleja naquele dia; porém Abner e os homens de Israel foram derrotados diante dos homens de Davi.
18 Estavam ali os três filhos de Zeruia: Joabe, Abisai e Asael; Asael era ligeiro de pés, como gazela selvagem.
19 Asael perseguiu a Abner e, na sua perseguição, não se desviou nem para a direita, nem para a esquerda.
20 Então, olhou Abner para trás e perguntou: És tu Asael? Ele respondeu: Eu mesmo.
21 Então, lhe disse Abner: Desvia-te para a direita ou para a esquerda, lança mão de um dos moços e toma-lhe a armadura. Porém Asael não quis apartar-se dele.
22 Então, Abner tornou a dizer-lhe: Desvia-te de detrás de mim; por que hei de eu ferir-te e dar contigo em terra? E como me avistaria rosto a rosto com Joabe, teu irmão?
23 Porém, recusando ele desviar-se, Abner o feriu no abdômen com a extremidade inferior da lança, que lhe saiu por detrás. Asael caiu e morreu no mesmo lugar; todos quantos chegavam no lugar em que Asael caíra e morrera paravam.
24 Porém Joabe e Abisai perseguiram Abner; e pôs-se o sol, quando chegaram eles ao outeiro de Amá, que está diante de Giá, junto ao caminho do deserto de Gibeão.
25 Os filhos de Benjamim se ajuntaram atrás de Abner e, cerrados numa tropa, puseram-se no cimo de um outeiro.
26 Então, Abner gritou a Joabe e disse: Consumirá a espada para sempre? Não sabes que serão amargas as suas consequências? Até quando te demorarás em ordenar ao povo que deixe de perseguir a seus irmãos?
27 Respondeu Joabe: Tão certo como vive Deus, se não tivesses falado, só amanhã cedo o povo cessaria de perseguir cada um a seu irmão.
28 Então, Joabe tocou a trombeta, e todo o povo parou, e eles não perseguiram mais a Israel e já não pelejaram.
29 Abner e seus homens marcharam toda aquela noite pela planície; passaram o Jordão e, caminhando toda a manhã, chegaram a Maanaim.
30 Joabe deixou de perseguir a Abner; e, tendo ele ajuntado todo o povo, faltavam dezenove dos homens de Davi, além de Asael.
31 Porém os servos de Davi tinham ferido, dentre os de Benjamim e dentre os homens de Abner, a trezentos e sessenta homens, que ali ficaram mortos.
32 Levaram Asael e o enterraram na sepultura de seu pai, a qual estava em Belém. Joabe e seus homens caminharam toda aquela noite, e amanheceu-lhes o dia em Hebrom.*
1 Durou muito tempo a guerra entre a casa de Saul e a casa de Davi; Davi se ia fortalecendo, porém os da casa de Saul se iam enfraquecendo.
2 Em Hebrom, nasceram filhos a Davi; o primogênito foi Amnom, de Ainoã, a jezreelita;
3 o segundo, Quileabe, de Abigail, viúva de Nabal, o carmelita; o terceiro, Absalão, filho de Maaca, filha de Talmai, rei de Gesur;
4 o quarto, Adonias, filho de Hagite; o quinto, Sefatias, filho de Abital;
5 o sexto, Itreão, de Eglá, mulher de Davi; estes nasceram a Davi em Hebrom.
6 Havendo guerra entre a casa de Saul e a casa de Davi, Abner se fez poderoso na casa de Saul.
7 Teve Saul uma concubina, cujo nome era Rispa, filha de Aiá. Perguntou Isbosete a Abner: Por que coabitaste com a concubina de meu pai?
8 Então, se irou muito Abner por causa das palavras de Isbosete e disse: Sou eu cabeça de cão para Judá? Ainda hoje faço beneficência à casa de Saul, teu pai, a seus irmãos e a seus amigos e te não entreguei nas mãos de Davi? Contudo, me queres, hoje, culpar por causa desta mulher.
9 Assim faça Deus segundo lhe parecer a Abner, se, como jurou o Senhor a Davi, não fizer eu,
10 transferindo o reino da casa de Saul e estabelecendo o trono de Davi sobre Israel e sobre Judá, desde Dã até Berseba.
11 E nenhuma palavra pôde Isbosete responder a Abner, porque o temia.
12 Então, de sua parte ordenou Abner mensageiros a Davi, dizendo: De quem é a terra? Faze comigo aliança, e eu te ajudarei em fazer passar-te a ti todo o Israel.
13 Respondeu Davi: Bem, eu farei aliança contigo, porém uma coisa exijo: quando vieres a mim, não verás a minha face, se primeiro me não trouxeres a Mical, filha de Saul.
14 Também enviou Davi mensageiros a Isbosete, filho de Saul, dizendo: Dá-me de volta minha mulher Mical, que eu desposei por cem prepúcios de filisteus.
15 Então, Isbosete mandou tirá-la a seu marido, a Paltiel, filho de Laís.
16 Seu marido a acompanhou, caminhando e chorando após ela, até Baurim. Disse Abner: Vai-te, volta. E ele voltou.
17 Falou Abner com os anciãos de Israel, dizendo: Outrora, procuráveis que Davi reinasse sobre vós.
18 Fazei-o, pois, agora, porque o Senhor falou a Davi, dizendo: Por intermédio de Davi, meu servo, livrarei o meu povo das mãos dos filisteus e das mãos de todos os seus inimigos.
19 Da mesma sorte falou também Abner aos ouvidos de Benjamim; e foi ainda dizer a Davi, em Hebrom, tudo o que agradava a Israel e a toda a casa de Benjamim.
20 Veio Abner ter com Davi, em Hebrom, e vinte homens, com ele; Davi ofereceu um banquete a Abner e aos homens que com ele vieram.
21 Então, disse Abner a Davi: Levantar-me-ei e irei para ajuntar todo o Israel ao rei, meu senhor, para fazerem aliança contigo; tu reinarás sobre tudo que desejar a tua alma. Assim, despediu Davi a Abner, e ele se foi em paz.
22 Eis que os servos de Davi e Joabe vieram de uma investida e traziam consigo grande despojo; Abner, porém, já não estava com Davi, em Hebrom, porque este o havia despedido, e ele se fora em paz.
23 Chegando, pois, Joabe e toda a tropa que vinha com ele, disseram-lhe: Abner, filho de Ner, veio ter com o rei, o qual o despediu, e ele se foi em paz.
24 Então, Joabe foi ao rei e disse: Que fizeste? Eis que Abner veio ter contigo; como, pois, o despediste, indo-se ele livremente?
25 Bem conheces Abner, filho de Ner. Veio para enganar-te, tomar conhecimento de tuas empresas e sondar todos os teus planos.
26 Retirando-se Joabe de Davi, enviou mensageiros após Abner, e o fizeram voltar desde o poço de Sirá, sem que Davi o soubesse.
27 Tornando, pois, Abner a Hebrom, Joabe o tomou à parte, no interior da porta, para lhe falar em segredo, e ali o feriu no abdômen, e ele morreu, agindo assim Joabe em vingança do sangue de seu irmão Asael.
28 Sabendo-o depois Davi, disse: Inocentes somos eu e o meu reino, para com o Senhor, para sempre, do sangue de Abner, filho de Ner.
29 Caia este sangue sobre a cabeça de Joabe e sobre toda a casa de seu pai! Jamais falte da casa de Joabe quem tenha fluxo, quem seja leproso, quem se apoie em muleta, quem caia à espada, quem necessite de pão.
30 Joabe, pois, e seu irmão Abisai mataram Abner, por ter morto seu irmão Asael na peleja, em Gibeão.
31 Disse, pois, Davi a Joabe e a todo o povo que com ele estava: Rasgai as vossas vestes, cingi-vos de panos de saco e ide pranteando diante de Abner. E o rei Davi ia seguindo o féretro.
32 Sepultaram Abner em Hebrom; o rei levantou a voz e chorou junto da sepultura de Abner; chorou também todo o povo.
33 E o rei, pranteando a Abner, disse: Teria de morrer Abner como se fora um perverso?
34 As tuas mãos não estavam atadas, nem os teus pés, carregados de grilhões; caíste como os que caem diante dos filhos da maldade! E todo o povo chorou muito mais por ele.
35 Então, veio todo o povo fazer que Davi comesse pão, sendo ainda dia; porém Davi jurou, dizendo: Assim me faça Deus o que lhe aprouver, se eu provar pão ou alguma coisa antes do sol posto.
36 Todo o povo notou isso e lhe pareceu bem, assim como lhe pareceu bem tudo quanto o rei fez.
37 Todo o povo e todo o Israel, naquele mesmo dia, ficaram sabendo que não procedera do rei que matassem a Abner, filho de Ner.
38 Então, disse o rei aos seus homens: Não sabeis que, hoje, caiu em Israel um príncipe e um grande homem?
39 No presente, sou fraco, embora ungido rei; estes homens, filhos de Zeruia, são mais fortes do que eu. Retribua o Senhor ao que fez mal segundo a sua maldade.*
1 Ouvindo, pois, o filho de Saul que Abner morrera em Hebrom, as mãos se lhe afrouxaram, e todo o Israel pasmou.
2 Tinha o filho de Saul a seu serviço dois homens, capitães de tropas; um se chamava Baaná, o outro, Recabe, filhos de Rimom, o beerotita, dos filhos de Benjamim, porque também Beerote era tida como pertencente a Benjamim.
3 Tinham fugido os beerotitas para Gitaim e ali têm morado até ao dia de hoje.
4 Jônatas, filho de Saul, tinha um filho aleijado dos pés. Era da idade de cinco anos quando de Jezreel chegaram as notícias da morte de Saul e de Jônatas; então, sua ama o tomou e fugiu; sucedeu que, apressando-se ela a fugir, ele caiu e ficou manco. Seu nome era Mefibosete.
5 Indo Recabe e Baaná, filhos de Rimom, beerotita, chegaram à casa de Isbosete, no maior calor do dia, estando este a dormir, ao meio-dia.
6 Ali, entraram para o interior da casa, como que vindo buscar trigo, e o feriram no abdômen; Recabe e Baaná, seu irmão, escaparam.
7 Tendo eles entrado na casa, estando ele no seu leito, no quarto de dormir, feriram-no e o mataram. Cortaram-lhe depois a cabeça e a levaram, andando toda a noite pelo caminho da planície.
8 Trouxeram a cabeça de Isbosete ao rei Davi, a Hebrom, e lhe disseram: Eis aqui a cabeça de Isbosete, filho de Saul, teu inimigo, que procurava tirar-te a vida; assim, o Senhor vingou, hoje, ao rei, meu senhor, de Saul e da sua descendência.
9 Porém Davi, respondendo a Recabe e a Baaná, seu irmão, filhos de Rimom, o beerotita, disse-lhes: Tão certo como vive o Senhor, que remiu a minha alma de toda a angústia,
10 se eu logo lancei mão daquele que me trouxe notícia, dizendo: Eis que Saul é morto, parecendo-lhe porém aos seus olhos que era como quem trazia boas-novas, e como recompensa o matei em Ziclague,
11 muito mais a perversos, que mataram a um homem justo em sua casa, no seu leito; agora, pois, não requereria eu o seu sangue de vossas mãos e não vos exterminaria da terra?
12 Deu Davi ordem aos seus moços; eles, pois, os mataram e, tendo-lhes cortado as mãos e os pés, os penduraram junto ao açude em Hebrom; tomaram, porém, a cabeça de Isbosete, e a enterraram na sepultura de Abner, em Hebrom.*
1 Então, todas as tribos de Israel vieram a Davi, a Hebrom, e falaram, dizendo: Somos do mesmo povo de que tu és.
2 Outrora, sendo Saul ainda rei sobre nós, eras tu que fazias entradas e saídas militares com Israel; também o Senhor te disse: Tu apascentarás o meu povo de Israel e serás chefe sobre Israel.
3 Assim, pois, todos os anciãos de Israel vieram ter com o rei, em Hebrom; e o rei Davi fez com eles aliança em Hebrom, perante o Senhor. Ungiram Davi rei sobre Israel.
4 Da idade de trinta anos era Davi quando começou a reinar; e reinou quarenta anos.
5 Em Hebrom, reinou sobre Judá sete anos e seis meses; em Jerusalém, reinou trinta e três anos sobre todo o Israel e Judá.
6 Partiu o rei com os seus homens para Jerusalém, contra os jebuseus que habitavam naquela terra e que disseram a Davi: Não entrarás aqui, porque os cegos e os coxos te repelirão, como quem diz: Davi não entrará neste lugar.
7 Porém Davi tomou a fortaleza de Sião; esta é a Cidade de Davi.
8 Davi, naquele dia, mandou dizer: Todo o que está disposto a ferir os jebuseus suba pelo canal subterrâneo e fira os cegos e os coxos, a quem a alma de Davi aborrece. (Por isso, se diz: Nem cego nem coxo entrará na casa.)
9 Assim, habitou Davi na fortaleza e lhe chamou a Cidade de Davi; foi edificando em redor, desde Milo e para dentro.
10 Ia Davi crescendo em poder cada vez mais, porque o Senhor, Deus dos Exércitos, era com ele.
11 Hirão, rei de Tiro, enviou mensageiros a Davi, e madeira de cedro, e carpinteiros, e pedreiros, que edificaram uma casa a Davi.
12 Reconheceu Davi que o Senhor o confirmara rei sobre Israel e que exaltara o seu reino por amor do seu povo.
13 Tomou Davi mais concubinas e mulheres de Jerusalém, depois que viera de Hebrom, e nasceram-lhe mais filhos e filhas.
14 São estes os nomes dos que lhe nasceram em Jerusalém: Samua, Sobabe, Natã, Salomão,
15 Ibar, Elisua, Nefegue, Jafia,
16 Elisama, Eliada e Elifelete.
17 Ouvindo, pois, os filisteus que Davi fora ungido rei sobre Israel, subiram todos para prender a Davi; ouvindo-o, desceu Davi à fortaleza.
18 Mas vieram os filisteus e se estenderam pelo vale dos Refains.
19 Davi consultou ao Senhor, dizendo: Subirei contra os filisteus? Entregar-mos-ás nas mãos? Respondeu-lhe o Senhor: Sobe, porque, certamente, entregarei os filisteus nas tuas mãos.
20 Então, veio Davi a Baal-Perazim e os derrotou ali; e disse: Rompeu o Senhor as fileiras inimigas diante de mim, como quem rompe águas. Por isso, chamou o nome daquele lugar Baal-Perazim.
21 Os filisteus deixaram lá os seus ídolos; e Davi e os seus homens os levaram.
22 Os filisteus tornaram a subir e se estenderam pelo vale dos Refains.
23 Davi consultou ao Senhor, e este lhe respondeu: Não subirás; rodeia por detrás deles e ataca-os por defronte das amoreiras.
24 E há de ser que, ouvindo tu um estrondo de marcha pelas copas das amoreiras, então, te apressarás: é o Senhor que saiu diante de ti, a ferir o arraial dos filisteus.
25 Fez Davi como o Senhor lhe ordenara; e feriu os filisteus desde Geba até chegar a Gezer.*
1 Tornou Davi a ajuntar todos os escolhidos de Israel, em número de trinta mil.
2 Dispôs-se e, com todo o povo que tinha consigo, partiu para Baalá de Judá, para levarem de lá para cima a arca de Deus, sobre a qual se invoca o Nome, o nome do Senhor dos Exércitos, que se assenta acima dos querubins.
3 Puseram a arca de Deus num carro novo e a levaram da casa de Abinadabe, que estava no outeiro; e Uzá e Aiô, filhos de Abinadabe, guiavam o carro novo.
4 Levaram-no com a arca de Deus, da casa de Abinadabe, que estava no outeiro; e Aiô ia adiante da arca.
5 Davi e toda a casa de Israel alegravam-se perante o Senhor, com toda sorte de instrumentos de pau de faia, com harpas, com saltérios, com tamboris, com pandeiros e com címbalos.
6 Quando chegaram à eira de Nacom, estendeu Uzá a mão à arca de Deus e a segurou, porque os bois tropeçaram.
7 Então, a ira do Senhor se acendeu contra Uzá, e Deus o feriu ali por esta irreverência; e morreu ali junto à arca de Deus.
8 Desgostou-se Davi, porque o Senhor irrompera contra Uzá; e chamou aquele lugar Perez-Uzá, até ao dia de hoje.
9 Temeu Davi ao Senhor, naquele dia, e disse: Como virá a mim a arca do Senhor?
10 Não quis Davi retirar para junto de si a arca do Senhor, para a Cidade de Davi; mas a fez levar à casa de Obede-Edom, o geteu.
11 Ficou a arca do Senhor em casa de Obede-Edom, o geteu, três meses; e o Senhor o abençoou e a toda a sua casa.
12 Então, avisaram a Davi, dizendo: O Senhor abençoou a casa de Obede-Edom e tudo quanto tem, por amor da arca de Deus; foi, pois, Davi e, com alegria, fez subir a arca de Deus da casa de Obede-Edom, à Cidade de Davi.
13 Sucedeu que, quando os que levavam a arca do Senhor tinham dado seis passos, sacrificava ele bois e carneiros cevados.
14 Davi dançava com todas as suas forças diante do Senhor; e estava cingido de uma estola sacerdotal de linho.
15 Assim, Davi, com todo o Israel, fez subir a arca do Senhor, com júbilo e ao som de trombetas.
16 Ao entrar a arca do Senhor na Cidade de Davi, Mical, filha de Saul, estava olhando pela janela e, vendo ao rei Davi, que ia saltando e dançando diante do Senhor, o desprezou no seu coração.
17 Introduziram a arca do Senhor e puseram-na no seu lugar, na tenda que lhe armara Davi; e este trouxe holocaustos e ofertas pacíficas perante o Senhor.
18 Tendo Davi trazido holocaustos e ofertas pacíficas, abençoou o povo em nome do Senhor dos Exércitos.
19 E repartiu a todo o povo e a toda a multidão de Israel, tanto homens como mulheres, a cada um, um bolo de pão, um bom pedaço de carne e passas. Então, se retirou todo o povo, cada um para sua casa.
20 Voltando Davi para abençoar a sua casa, Mical, filha de Saul, saiu a encontrar-se com ele e lhe disse: Que bela figura fez o rei de Israel, descobrindo-se, hoje, aos olhos das servas de seus servos, como, sem pejo, se descobre um vadio qualquer!
21 Disse, porém, Davi a Mical: Perante o Senhor, que me escolheu a mim antes do que a teu pai e a toda a sua casa, mandando-me que fosse chefe sobre o povo do Senhor, sobre Israel, perante o Senhor me tenho alegrado.
22 Ainda mais desprezível me farei e me humilharei aos meus olhos; quanto às servas, de quem falaste, delas serei honrado.
23 Mical, filha de Saul, não teve filhos, até ao dia da sua morte.*
1 Sucedeu que, habitando o rei Davi em sua própria casa, tendo-lhe o Senhor dado descanso de todos os seus inimigos em redor,
2 disse o rei ao profeta Natã: Olha, eu moro em casa de cedros, e a arca de Deus se acha numa tenda.
3 Disse Natã ao rei: Vai, faze tudo quanto está no teu coração, porque o Senhor é contigo.
4 Porém, naquela mesma noite, veio a palavra do Senhor a Natã, dizendo:
5 Vai e dize a meu servo Davi: Assim diz o Senhor: Edificar-me-ás tu casa para minha habitação?
6 Porque em casa nenhuma habitei desde o dia em que fiz subir os filhos de Israel do Egito até ao dia de hoje; mas tenho andado em tenda, em tabernáculo.
7 Em todo lugar em que andei com todos os filhos de Israel, falei, acaso, alguma palavra com qualquer das suas tribos, a quem mandei apascentar o meu povo de Israel, dizendo: Por que não me edificais uma casa de cedro?
8 Agora, pois, assim dirás ao meu servo Davi: Assim diz o Senhor dos Exércitos: Tomei-te da malhada, de detrás das ovelhas, para que fosses príncipe sobre o meu povo, sobre Israel.
9 E fui contigo, por onde quer que andaste, eliminei os teus inimigos diante de ti e fiz grande o teu nome, como só os grandes têm na terra.
10 Prepararei lugar para o meu povo, para Israel, e o plantarei, para que habite no seu lugar e não mais seja perturbado, e jamais os filhos da perversidade o aflijam, como dantes,
11 desde o dia em que mandei houvesse juízes sobre o meu povo de Israel. Dar-te-ei, porém, descanso de todos os teus inimigos; também o Senhor te faz saber que ele, o Senhor, te fará casa.
12 Quando teus dias se cumprirem e descansares com teus pais, então, farei levantar depois de ti o teu descendente, que procederá de ti, e estabelecerei o seu reino.
13 Este edificará uma casa ao meu nome, e eu estabelecerei para sempre o trono do seu reino.
14 Eu lhe serei por pai, e ele me será por filho; se vier a transgredir, castigá-lo-ei com varas de homens e com açoites de filhos de homens.
15 Mas a minha misericórdia se não apartará dele, como a retirei de Saul, a quem tirei de diante de ti.
16 Porém a tua casa e o teu reino serão firmados para sempre diante de ti; teu trono será estabelecido para sempre.
17 Segundo todas estas palavras e conforme toda esta visão, assim falou Natã a Davi.
9 E fui contigo, por onde quer que andaste, eliminei os teus inimigos diante de ti e fiz grande o teu nome, como só os grandes têm na terra.
10 Prepararei lugar para o meu povo, para Israel, e o plantarei, para que habite no seu lugar e não mais seja perturbado, e jamais os filhos da perversidade o aflijam, como dantes,
11 desde o dia em que mandei houvesse juízes sobre o meu povo de Israel. Dar-te-ei, porém, descanso de todos os teus inimigos; também o Senhor te faz saber que ele, o Senhor, te fará casa.
12 Quando teus dias se cumprirem e descansares com teus pais, então, farei levantar depois de ti o teu descendente, que procederá de ti, e estabelecerei o seu reino.
13 Este edificará uma casa ao meu nome, e eu estabelecerei para sempre o trono do seu reino.
14 Eu lhe serei por pai, e ele me será por filho; se vier a transgredir, castigá-lo-ei com varas de homens e com açoites de filhos de homens.
15 Mas a minha misericórdia se não apartará dele, como a retirei de Saul, a quem tirei de diante de ti.
16 Porém a tua casa e o teu reino serão firmados para sempre diante de ti; teu trono será estabelecido para sempre.
17 Segundo todas estas palavras e conforme toda esta visão, assim falou Natã a Davi.
18 Então, entrou o rei Davi na Casa do Senhor, ficou perante ele e disse: Quem sou eu, Senhor Deus, e qual é a minha casa, para que me tenhas trazido até aqui?
19 Foi isso ainda pouco aos teus olhos, Senhor Deus, de maneira que também falaste a respeito da casa de teu servo para tempos distantes; e isto é instrução para todos os homens, ó Senhor Deus.
20 Que mais ainda te poderá dizer Davi? Pois tu conheces bem a teu servo, ó Senhor Deus.
21 Por causa da tua palavra e segundo o teu coração, fizeste toda esta grandeza, dando-a a conhecer a teu servo.
22 Portanto, grandíssimo és, ó Senhor Deus, porque não há semelhante a ti, e não há outro Deus além de ti, segundo tudo o que nós mesmos temos ouvido.
23 Quem há como o teu povo, como Israel, gente única na terra, a quem tu, ó Deus, foste resgatar para ser teu povo? E para fazer a ti mesmo um nome e fazer a teu povo estas grandes e tremendas coisas, para a tua terra, diante do teu povo, que tu resgataste do Egito, desterrando as nações e seus deuses?
24 Estabeleceste teu povo Israel por teu povo para sempre e tu, ó Senhor, te fizeste o seu Deus.
25 Agora, pois, ó Senhor Deus, quanto a esta palavra que disseste acerca de teu servo e acerca da sua casa, confirma-a para sempre e faze como falaste.
26 Seja para sempre engrandecido o teu nome, e diga-se: O Senhor dos Exércitos é Deus sobre Israel; e a casa de Davi, teu servo, será estabelecida diante de ti.
27 Pois tu, ó Senhor dos Exércitos, Deus de Israel, fizeste ao teu servo esta revelação, dizendo: Edificar-te-ei casa. Por isso, o teu servo se animou para fazer-te esta oração.
28 Agora, pois, ó Senhor Deus, tu mesmo és Deus, e as tuas palavras são verdade, e tens prometido a teu servo este bem.
29 Sê, pois, agora, servido de abençoar a casa do teu servo, a fim de permanecer para sempre diante de ti, pois tu, ó Senhor Deus, o disseste; e, com a tua bênção, será, para sempre, bendita a casa do teu servo.*
1 Depois disto, feriu Davi os filisteus e os sujeitou; e tomou de suas mãos as rédeas da metrópole.
2 Também derrotou os moabitas; fê-los deitar em terra e os mediu: duas vezes um cordel, para os matar; uma vez um cordel, para os deixar com vida. Assim, ficaram os moabitas por servos de Davi e lhe pagavam tributo.
3 Também Hadadezer, filho de Reobe, rei de Zobá, foi derrotado por Davi, quando aquele foi restabelecer o seu domínio sobre o rio Eufrates.
4 Tomou-lhe Davi mil e setecentos cavaleiros e vinte mil homens de pé; Davi jarretou todos os cavalos dos carros, menos para cem deles.
5 Vieram os siros de Damasco a socorrer Hadadezer, rei de Zobá; porém Davi matou dos siros vinte e dois mil homens.
6 Davi pôs guarnições na Síria de Damasco, e os siros ficaram por servos de Davi e lhe pagavam tributo; e o Senhor dava vitórias a Davi, por onde quer que ia.
7 Tomou Davi os escudos de ouro que havia com os oficiais de Hadadezer e os trouxe a Jerusalém.
8 Tomou mais o rei Davi mui grande quantidade de bronze de Betá e de Berotai, cidades de Hadadezer.
9 Então, ouvindo Toí, rei de Hamate, que Davi derrotara a todo o exército de Hadadezer,
10 mandou seu filho Jorão ao rei Davi, para o saudar e congratular-se com ele por haver pelejado contra Hadadezer e por havê-lo ferido (porque Hadadezer de contínuo fazia guerra a Toí). Jorão trouxe consigo objetos de prata, de ouro e de bronze,
11 os quais também o rei Davi consagrou ao Senhor, juntamente com a prata e o ouro que já havia consagrado de todas as nações que sujeitara:
12 da Síria, de Moabe, dos filhos de Amom, dos filisteus, de Amaleque e dos despojos de Hadadezer, filho de Reobe, rei de Zobá.
13 Ganhou Davi renome, quando, ao voltar de ferir os siros, matou dezoito mil homens no vale do Sal.
14 Pôs guarnições em Edom, em todo o Edom pôs guarnições, e todos os edomitas ficaram por servos de Davi; e o Senhor dava vitórias a Davi, por onde quer que ia.
15 Reinou, pois, Davi sobre todo o Israel; julgava e fazia justiça a todo o seu povo.
16 Joabe, filho de Zeruia, era comandante do exército; Josafá, filho de Ailude, era cronista.
17 Zadoque, filho de Aitube, e Aimeleque, filho de Abiatar, eram sacerdotes, e Seraías, escrivão.
18 E Benaia, filho de Joiada, era o comandante da guarda real. Os filhos de Davi, porém, eram seus ministros.*
1 Disse Davi: Resta ainda, porventura, alguém da casa de Saul, para que use eu de bondade para com ele, por amor de Jônatas?
2 Havia um servo na casa de Saul cujo nome era Ziba; chamaram-no que viesse a Davi. Perguntou-lhe o rei: És tu Ziba? Respondeu: Eu mesmo, teu servo.
3 Disse-lhe o rei: Não há ainda alguém da casa de Saul para que use eu da bondade de Deus para com ele? Então, Ziba respondeu ao rei: Ainda há um filho de Jônatas, aleijado de ambos os pés.
4 E onde está? Perguntou-lhe o rei. Ziba lhe respondeu: Está na casa de Maquir, filho de Amiel, em Lo-Debar.
5 Então, mandou o rei Davi trazê-lo de Lo-Debar, da casa de Maquir, filho de Amiel.
6 Vindo Mefibosete, filho de Jônatas, filho de Saul, a Davi, inclinou-se, prostrando-se com o rosto em terra. Disse-lhe Davi: Mefibosete! Ele disse: Eis aqui teu servo!
7 Então, lhe disse Davi: Não temas, porque usarei de bondade para contigo, por amor de Jônatas, teu pai, e te restituirei todas as terras de Saul, teu pai, e tu comerás pão sempre à minha mesa.
8 Então, se inclinou e disse: Quem é teu servo, para teres olhado para um cão morto tal como eu?
9 Chamou Davi a Ziba, servo de Saul, e lhe disse: Tudo o que pertencia a Saul e toda a sua casa dei ao filho de teu senhor.
10 Trabalhar-lhe-ás, pois, a terra, tu, e teus filhos, e teus servos, e recolherás os frutos, para que a casa de teu senhor tenha pão que coma; porém Mefibosete, filho de teu senhor, comerá pão sempre à minha mesa. Tinha Ziba quinze filhos e vinte servos.
11 Disse Ziba ao rei: Segundo tudo quanto meu senhor, o rei, manda a seu servo, assim o fará. Comeu, pois, Mefibosete à mesa de Davi, como um dos filhos do rei.
12 Tinha Mefibosete um filho pequeno, cujo nome era Mica. Todos quantos moravam em casa de Ziba eram servos de Mefibosete.
13 Morava Mefibosete em Jerusalém, porquanto comia sempre à mesa do rei. Ele era coxo de ambos os pés.*
1 Depois disto, morreu o rei dos filhos de Amom, e seu filho Hanum reinou em seu lugar.
2 Então, disse Davi: Usarei de bondade para com Hanum, filho de Naás, como seu pai usou de bondade para comigo. E enviou Davi servos seus para o consolar acerca de seu pai; e vieram os servos de Davi à terra dos filhos de Amom.
3 Mas os príncipes dos filhos de Amom disseram a seu senhor, Hanum: Pensas que, por Davi te haver mandado consoladores, está honrando a teu pai? Porventura, não te enviou ele os seus servos para reconhecerem a cidade, espiá-la e destruí-la?
4 Tomou, então, Hanum os servos de Davi, e lhes rapou metade da barba, e lhes cortou metade das vestes até às nádegas, e os despediu.
5 Sabedor disso, enviou Davi mensageiros a encontrá-los, porque estavam sobremaneira envergonhados. Mandou o rei dizer-lhes: Deixai-vos estar em Jericó, até que vos torne a crescer a barba; e, então, vinde.
6 Vendo, pois, os filhos de Amom que se haviam tornado odiosos a Davi, mandaram mensageiros tomar a soldo vinte mil homens de pé dos siros de Bete-Reobe e dos siros de Zobá, mil homens do rei de Maaca e doze mil de Tobe.
7 O que ouvindo Davi, enviou contra eles a Joabe com todo o exército dos valentes.
8 Saíram os filhos de Amom e ordenaram a batalha à entrada da porta, e os siros de Zobá e Reobe e os homens de Tobe e Maaca estavam à parte no campo.
9 Vendo, pois, Joabe que estava preparada contra ele a batalha, tanto pela frente como pela retaguarda, escolheu dentre todos o que havia de melhor em Israel e os formou em linha contra os siros;
10 e o resto do povo, entregou-o a Abisai, seu irmão, o qual o formou em linha contra os filhos de Amom.
11 Disse Joabe: Se os siros forem mais fortes do que eu, tu me virás em socorro; e, se os filhos de Amom forem mais fortes do que tu, eu irei ao teu socorro.
12 Sê forte, pois; pelejemos varonilmente pelo nosso povo e pelas cidades de nosso Deus; e faça o Senhor o que bem lhe parecer.
13 Então, avançou Joabe com o povo que estava com ele, e travaram peleja contra os siros; e estes fugiram de diante deles.
14 Vendo os filhos de Amom que os siros fugiam, também eles fugiram de diante de Abisai e entraram na cidade; voltou Joabe dos filhos de Amom e tornou a Jerusalém.
15 Vendo, pois, os siros que tinham sido desbaratados diante de Israel, tornaram a refazer-se.
16 E Hadadezer fez sair os siros que estavam do outro lado do rio, e vieram a Helã; Sobaque, chefe do exército de Hadadezer, marchava adiante deles.
17 Informado Davi, ajuntou a todo o Israel, passou o Jordão e foi a Helã; os siros se puseram em ordem de batalha contra Davi e pelejaram contra ele.
18 Porém os siros fugiram de diante de Israel, e Davi matou dentre os siros os homens de setecentos carros e quarenta mil homens de cavalo; também feriu a Sobaque, chefe do exército, de tal sorte que morreu ali.
19 Vendo, pois, todos os reis, servos de Hadadezer, que foram vencidos, fizeram paz com Israel e o serviram; e temeram os siros de ainda socorrer aos filhos de Amom.*
1 Decorrido um ano, no tempo em que os reis costumam sair para a guerra, enviou Davi a Joabe, e seus servos, com ele, e a todo o Israel, que destruíram os filhos de Amom e sitiaram Rabá; porém Davi ficou em Jerusalém.
2 Uma tarde, levantou-se Davi do seu leito e andava passeando no terraço da casa real; daí viu uma mulher que estava tomando banho; era ela mui formosa.
3 Davi mandou perguntar quem era. Disseram-lhe: É Bate-Seba, filha de Eliã e mulher de Urias, o heteu.
4 Então, enviou Davi mensageiros que a trouxessem; ela veio, e ele se deitou com ela. Tendo-se ela purificado da sua imundícia, voltou para sua casa.
5 A mulher concebeu e mandou dizer a Davi: Estou grávida.
6 Então, enviou Davi mensageiros a Joabe, dizendo: Manda-me Urias, o heteu. Joabe enviou Urias a Davi.
7 Vindo, pois, Urias a Davi, perguntou este como passava Joabe, como se achava o povo e como ia a guerra.
8 Depois, disse Davi a Urias: Desce a tua casa e lava os pés. Saindo Urias da casa real, logo se lhe seguiu um presente do rei.
9 Porém Urias se deitou à porta da casa real, com todos os servos do seu senhor, e não desceu para sua casa.
10 Fizeram-no saber a Davi, dizendo: Urias não desceu a sua casa. Então, disse Davi a Urias: Não vens tu de uma jornada? Por que não desceste a tua casa?
11 Respondeu Urias a Davi: A arca, Israel e Judá ficam em tendas; Joabe, meu senhor, e os servos de meu senhor estão acampados ao ar livre; e hei de eu entrar na minha casa, para comer e beber e para me deitar com minha mulher? Tão certo como tu vives e como vive a tua alma, não farei tal coisa.
12 Então, disse Davi a Urias: Demora-te aqui ainda hoje, e amanhã te despedirei. Urias, pois, ficou em Jerusalém aquele dia e o seguinte.
13 Davi o convidou, e comeu e bebeu diante dele, e o embebedou; à tarde, saiu Urias a deitar-se na sua cama, com os servos de seu senhor; porém não desceu a sua casa.
14 Pela manhã, Davi escreveu uma carta a Joabe e lha mandou por mão de Urias.
15 Escreveu na carta, dizendo: Ponde Urias na frente da maior força da peleja; e deixai-o sozinho, para que seja ferido e morra.
16 Tendo, pois, Joabe sitiado a cidade, pôs a Urias no lugar onde sabia que estavam homens valentes.
17 Saindo os homens da cidade e pelejando com Joabe, caíram alguns do povo, dos servos de Davi; e morreu também Urias, o heteu.
18 Então, Joabe enviou notícias e fez saber a Davi tudo o que se dera na batalha.
19 Deu ordem ao mensageiro, dizendo: Se, ao terminares de contar ao rei os acontecimentos desta peleja,
20 suceder que ele se encolerize e te diga: Por que vos chegastes assim perto da cidade a pelejar? Não sabíeis vós que haviam de atirar do muro?
21 Quem feriu a Abimeleque, filho de Jerubesete? Não lançou uma mulher sobre ele, do muro, um pedaço de mó corredora, de que morreu em Tebes? Por que vos chegastes ao muro? Então, dirás: Também morreu teu servo Urias, o heteu.
22 Partiu o mensageiro e, chegando, fez saber a Davi tudo o que Joabe lhe havia mandado dizer.
23 Disse o mensageiro a Davi: Na verdade, aqueles homens foram mais poderosos do que nós e saíram contra nós ao campo; porém nós fomos contra eles, até à entrada da porta.
24 Então, os flecheiros, do alto do muro, atiraram contra os teus servos, e morreram alguns dos servos do rei; e também morreu o teu servo Urias, o heteu.
25 Disse Davi ao mensageiro: Assim dirás a Joabe: Não pareça isto mal aos teus olhos, pois a espada devora tanto este como aquele; intensifica a tua peleja contra a cidade e derrota-a; e, tu, anima a Joabe.
26 Ouvindo, pois, a mulher de Urias que seu marido era morto, ela o pranteou.
27 Passado o luto, Davi mandou buscá-la e a trouxe para o palácio; tornou-se ela sua mulher e lhe deu à luz um filho. Porém isto que Davi fizera foi mau aos olhos do Senhor.*
1 O Senhor enviou Natã a Davi. Chegando Natã a Davi, disse-lhe: Havia numa cidade dois homens, um rico e outro pobre.
2 Tinha o rico ovelhas e gado em grande número;
3 mas o pobre não tinha coisa nenhuma, senão uma cordeirinha que comprara e criara, e que em sua casa crescera, junto com seus filhos; comia do seu bocado e do seu copo bebia; dormia nos seus braços, e a tinha como filha.
4 Vindo um viajante ao homem rico, não quis este tomar das suas ovelhas e do gado para dar de comer ao viajante que viera a ele; mas tomou a cordeirinha do homem pobre e a preparou para o homem que lhe havia chegado.
5 Então, o furor de Davi se acendeu sobremaneira contra aquele homem, e disse a Natã: Tão certo como vive o Senhor, o homem que fez isso deve ser morto.
6 E pela cordeirinha restituirá quatro vezes, porque fez tal coisa e porque não se compadeceu.
7 Então, disse Natã a Davi: Tu és o homem. Assim diz o Senhor, Deus de Israel: Eu te ungi rei sobre Israel e eu te livrei das mãos de Saul;
8 dei-te a casa de teu senhor e as mulheres de teu senhor em teus braços e também te dei a casa de Israel e de Judá; e, se isto fora pouco, eu teria acrescentado tais e tais coisas.
9 Por que, pois, desprezaste a palavra do Senhor, fazendo o que era mau perante ele? A Urias, o heteu, feriste à espada; e a sua mulher tomaste por mulher, depois de o matar com a espada dos filhos de Amom.
10 Agora, pois, não se apartará a espada jamais da tua casa, porquanto me desprezaste e tomaste a mulher de Urias, o heteu, para ser tua mulher.
11 Assim diz o Senhor: Eis que da tua própria casa suscitarei o mal sobre ti, e tomarei tuas mulheres à tua própria vista, e as darei a teu próximo, o qual se deitará com elas, em plena luz deste sol.
12 Porque tu o fizeste em oculto, mas eu farei isto perante todo o Israel e perante o sol.
13 Então, disse Davi a Natã: Pequei contra o Senhor. Disse Natã a Davi: Também o Senhor te perdoou o teu pecado; não morrerás.
14 Mas, posto que com isto deste motivo a que blasfemassem os inimigos do Senhor, também o filho que te nasceu morrerá.
15 Então, Natã foi para sua casa.
E o Senhor feriu a criança que a mulher de Urias dera à luz a Davi; e a criança adoeceu gravemente.
16 Buscou Davi a Deus pela criança; jejuou Davi e, vindo, passou a noite prostrado em terra.
17 Então, os anciãos da sua casa se achegaram a ele, para o levantar da terra; porém ele não quis e não comeu com eles.
18 Ao sétimo dia, morreu a criança; e temiam os servos de Davi informá-lo de que a criança era morta, porque diziam: Eis que, estando a criança ainda viva, lhe falávamos, porém não dava ouvidos à nossa voz; como, pois, lhe diremos que a criança é morta? Porque mais se afligirá.
19 Viu, porém, Davi que seus servos cochichavam uns com os outros e entendeu que a criança era morta, pelo que disse aos seus servos: É morta a criança? Eles responderam: Morreu.
20 Então, Davi se levantou da terra; lavou-se, ungiu-se, mudou de vestes, entrou na Casa do Senhor e adorou; depois, veio para sua casa e pediu pão; puseram-no diante dele, e ele comeu.
21 Disseram-lhe seus servos: Que é isto que fizeste? Pela criança viva jejuaste e choraste; porém, depois que ela morreu, te levantaste e comeste pão.
22 Respondeu ele: Vivendo ainda a criança, jejuei e chorei, porque dizia: Quem sabe se o Senhor se compadecerá de mim, e continuará viva a criança?
23 Porém, agora que é morta, por que jejuaria eu? Poderei eu fazê-la voltar? Eu irei a ela, porém ela não voltará para mim.
24 Então, Davi veio a Bate-Seba, consolou-a e se deitou com ela; teve ela um filho a quem Davi deu o nome de Salomão; e o Senhor o amou.
25 Davi o entregou nas mãos do profeta Natã, e este lhe chamou Jedidias, por amor do Senhor.
26 Entretanto, pelejou Joabe contra Rabá, dos filhos de Amom, e tomou a cidade real.
27 Então, mandou Joabe mensageiros a Davi e disse: Pelejei contra Rabá e tomei a cidade das águas.
28 Ajunta, pois, agora o resto do povo, e cerca a cidade, e toma-a, para não suceder que, tomando-a eu, se aclame sobre ela o meu nome.
29 Reuniu, pois, Davi a todo o povo, e marchou para Rabá, e pelejou contra ela, e a tomou.
30 Tirou a coroa da cabeça do seu rei; o peso da coroa era de um talento de ouro, e havia nela pedras preciosas, e foi posta na cabeça de Davi; e da cidade levou mui grande despojo.
31 Trazendo o povo que havia nela, fê-lo passar a serras, e a picaretas, e a machados de ferro, e em fornos de tijolos; e assim fez a todas as cidades dos filhos de Amom. Voltou Davi com todo o povo para Jerusalém.*
1 Tinha Absalão, filho de Davi, uma formosa irmã, cujo nome era Tamar. Amnom, filho de Davi, se enamorou dela.
2 Angustiou-se Amnom por Tamar, sua irmã, a ponto de adoecer, pois, sendo ela virgem, parecia-lhe impossível fazer-lhe coisa alguma.
3 Tinha, porém, Amnom um amigo cujo nome era Jonadabe, filho de Simeia, irmão de Davi; Jonadabe era homem mui sagaz.
4 E ele lhe disse: Por que tanto emagreces de dia para dia, ó filho do rei? Não mo dirás? Então, lhe disse Amnom: Amo Tamar, irmã de Absalão, meu irmão.
5 Disse-lhe Jonadabe: Deita-te na tua cama e finge-te doente; quando teu pai vier visitar-te, dize-lhe: Peço-te que minha irmã Tamar venha e me dê de comer pão, pois, vendo-a eu preparar-me a comida, comerei de sua mão.
6 Deitou-se, pois, Amnom e fingiu-se doente; vindo o rei visitá-lo, Amnom lhe disse: Peço-te que minha irmã Tamar venha e prepare dois bolos à minha presença, para que eu coma de sua mão.
7 Então, Davi mandou dizer a Tamar em sua casa: Vai à casa de Amnom, teu irmão, e faze-lhe comida.
8 Foi Tamar à casa de Amnom, seu irmão, e ele estava deitado. Tomou ela a massa e a amassou, fez bolos diante dele e os cozeu.
9 Tomou a assadeira e virou os bolos diante dele; porém ele recusou comer. Disse Amnom: Fazei retirar a todos da minha presença. E todos se retiraram.
10 Então, disse Amnom a Tamar: Traze a comida à câmara, e comerei da tua mão. Tomou Tamar os bolos que fizera e os levou a Amnom, seu irmão, à câmara.
11 Quando lhos oferecia para que comesse, pegou-a e disse-lhe: Vem, deita-te comigo, minha irmã.
12 Porém ela lhe disse: Não, meu irmão, não me forces, porque não se faz assim em Israel; não faças tal loucura.
13 Porque, aonde iria eu com a minha vergonha? E tu serias como um dos loucos de Israel. Agora, pois, peço-te que fales ao rei, porque não me negará a ti.
14 Porém ele não quis dar ouvidos ao que ela lhe dizia; antes, sendo mais forte do que ela, forçou-a e se deitou com ela.
15 Depois, Amnom sentiu por ela grande aversão, e maior era a aversão que sentiu por ela que o amor que ele lhe votara. Disse-lhe Amnom: Levanta-te, vai-te embora.
16 Então, ela lhe disse: Não, meu irmão; porque maior é esta injúria, lançando-me fora, do que a outra que me fizeste. Porém ele não a quis ouvir.
17 Chamou a seu moço, que o servia, e disse: Deita fora esta e fecha a porta após ela.
18 Trazia ela uma túnica talar de mangas compridas, porque assim se vestiam as donzelas filhas do rei. Mesmo assim o servo a deitou fora e fechou a porta após ela.
19 Então, Tamar tomou cinza sobre a cabeça, rasgou a túnica talar de mangas compridas que trazia, pôs as mãos sobre a cabeça e se foi andando e clamando.
20 Absalão, seu irmão, lhe disse: Esteve Amnom, teu irmão, contigo? Ora, pois, minha irmã, cala-te; é teu irmão. Não se angustie o teu coração por isso. Assim ficou Tamar e esteve desolada em casa de Absalão, seu irmão.
21 Ouvindo o rei Davi todas estas coisas, muito se lhe acendeu a ira.
22 Porém Absalão não falou com Amnom nem mal nem bem; porque odiava a Amnom, por ter este forçado a Tamar, sua irmã.
23 Passados dois anos, Absalão tosquiava em Baal-Hazor, que está junto a Efraim, e convidou Absalão todos os filhos do rei.
24 Foi ter Absalão com o rei e disse: Eis que teu servo faz a tosquia; peço que com o teu servo venham o rei e os seus servidores.
25 O rei, porém, disse a Absalão: Não, filho meu, não vamos todos juntos, para não te sermos pesados. Instou com ele Absalão, porém ele não quis ir; contudo, o abençoou.
26 Então, disse Absalão: Se não queres ir, pelo menos deixa ir conosco Amnom, meu irmão. Porém o rei lhe disse: Para que iria ele contigo?
27 Insistindo Absalão com ele, deixou ir com ele Amnom e todos os filhos do rei.
28 Absalão deu ordem aos seus moços, dizendo: Tomai sentido; quando o coração de Amnom estiver alegre de vinho, e eu vos disser: Feri a Amnom, então, o matareis. Não temais, pois não sou eu quem vo-lo ordena? Sede fortes e valentes.
29 E os moços de Absalão fizeram a Amnom como Absalão lhes havia ordenado. Então, todos os filhos do rei se levantaram, cada um montou seu mulo, e fugiram.
30 Iam eles ainda de caminho, quando chegou a notícia a Davi: Absalão feriu todos os filhos do rei, e nenhum deles ficou.
31 Então, o rei se levantou, rasgou as suas vestes e se lançou por terra; e todos os seus servos que estavam presentes rasgaram também as suas vestes.
32 Mas Jonadabe, filho de Simeia, irmão de Davi, respondeu e disse: Não pense o meu senhor que mataram a todos os jovens, filhos do rei, porque só morreu Amnom; pois assim já o revelavam as feições de Absalão, desde o dia em que sua irmã Tamar foi forçada por Amnom.
33 Não meta, pois, agora, na cabeça o rei, meu senhor, tal coisa, supondo que morreram todos os filhos do rei; porque só morreu Amnom.
34 Absalão fugiu. O moço que estava de guarda, levantando os olhos, viu que vinha muito povo pelo caminho por detrás dele, pelo lado do monte.
35 Então, disse Jonadabe ao rei: Eis aí vêm os filhos do rei; segundo a palavra de teu servo, assim sucedeu.
36 Mal acabara de falar, chegavam os filhos do rei e, levantando a voz, choraram; também o rei e todos os seus servos choraram amargamente.
37 Absalão, porém, fugiu e se foi a Talmai, filho de Amiúde, rei de Gesur. E Davi pranteava a seu filho todos os dias.
38 Assim, Absalão fugiu, indo para Gesur, onde esteve três anos.
39 Então, o rei Davi cessou de perseguir a Absalão, porque já se tinha consolado acerca de Amnom, que era morto.*
1 Percebendo, pois, Joabe, filho de Zeruia, que o coração do rei começava a inclinar-se para Absalão,
2 mandou trazer de Tecoa uma mulher sábia e lhe disse: Finge que estás profundamente triste, põe vestidos de luto, não te unjas com óleo e sê como mulher que há já muitos dias está de luto por algum morto.
3 Apresenta-te ao rei e fala-lhe tais e tais palavras. E Joabe lhe pôs as palavras na boca.
4 A mulher tecoíta apresentou-se ao rei, e, inclinando-se, prostrou-se com o rosto em terra, e disse: Salva-me, ó rei!
5 Perguntou-lhe o rei: Que tens? Ela respondeu: Ah! Sou mulher viúva; morreu meu marido.
6 Tinha a tua serva dois filhos, os quais brigaram entre si no campo, e não houve quem os apartasse; um feriu ao outro e o matou.
7 Eis que toda a parentela se levantou contra a tua serva, e disseram: Dá-nos aquele que feriu a seu irmão, para que o matemos, em vingança da vida de quem ele matou e para que destruamos também o herdeiro. Assim, apagarão a última brasa que me ficou, de sorte que não deixam a meu marido nome, nem sobrevivente na terra.
8 Disse o rei à mulher: Vai para tua casa, e eu darei ordens a teu respeito.
9 Disse a mulher tecoíta ao rei: A culpa, ó rei, meu senhor, caia sobre mim e sobre a casa de meu pai; o rei, porém, e o seu trono sejam inocentes.
10 Disse o rei: Quem falar contra ti, traze-mo a mim; e nunca mais te tocará.
11 Disse ela: Ora, lembra-te, ó rei, do Senhor, teu Deus, para que os vingadores do sangue não se multipliquem a matar e exterminem meu filho. Respondeu ele: Tão certo como vive o Senhor, não há de cair no chão nem um só dos cabelos de teu filho.
12 Então, disse a mulher: Permite que a tua serva fale uma palavra contigo, ó rei, meu senhor. Disse ele: Fala.
13 Prosseguiu a mulher: Por que pensas tu doutro modo contra o povo de Deus? Pois, em pronunciando o rei esse juízo, condena-se a si mesmo, visto que não quer fazer voltar o seu desterrado.
14 Porque temos de morrer e somos como águas derramadas na terra que já não se podem juntar; pois Deus não tira a vida, mas cogita meios para que o banido não permaneça arrojado de sua presença.
15 Se vim, agora, falar esta palavra ao rei, meu senhor, é porque o povo me atemorizou; pois dizia a tua serva: Falarei ao rei; porventura, ele fará segundo a palavra da sua serva.
16 Porque o rei atenderá, para livrar a sua serva da mão do homem que intenta destruir tanto a mim como a meu filho da herança de Deus.
17 Dizia mais a tua serva: Seja, agora, a palavra do rei, meu senhor, para a minha tranquilidade; porque, como um anjo de Deus, assim é o rei, meu senhor, para discernir entre o bem e o mal. O Senhor, teu Deus, será contigo.
18 Então, respondeu o rei e disse à mulher: Peço-te que não me encubras o que eu te perguntar. Respondeu a mulher: Pois fale o rei, meu senhor.
19 Disse o rei: Não é certo que a mão de Joabe anda contigo em tudo isto? Respondeu ela: Tão certo como vive a tua alma, ó rei, meu senhor, ninguém se poderá desviar, nem para a direita nem para a esquerda, de tudo quanto o rei, meu senhor, tem dito; porque Joabe, teu servo, é quem me deu ordem e foi ele quem ditou à tua serva todas estas palavras.
20 Para mudar o aspecto deste caso foi que o teu servo Joabe fez isto. Porém sábio é meu senhor, segundo a sabedoria de um anjo de Deus, para entender tudo o que se passa na terra.
21 Então, o rei disse a Joabe: Atendi ao teu pedido; vai, pois, e traze o jovem Absalão.
22 Inclinando-se Joabe, prostrou-se em terra, abençoou o rei e disse: Hoje, reconheço que achei mercê diante de ti, ó rei, meu senhor; porque o rei fez segundo a palavra do seu servo.
23 Levantou-se Joabe, foi a Gesur e trouxe Absalão a Jerusalém.
24 Disse o rei: Torne para a sua casa e não veja a minha face. Tornou, pois, Absalão para sua casa e não viu a face do rei.
25 Não havia, porém, em todo o Israel homem tão celebrado por sua beleza como Absalão; da planta do pé ao alto da cabeça, não havia nele defeito algum.
26 Quando cortava o cabelo (e isto se fazia no fim de cada ano, porquanto muito lhe pesava), seu peso era de duzentos siclos, segundo o peso real.
27 Também nasceram a Absalão três filhos e uma filha, cujo nome era Tamar; esta era mulher formosa à vista.
28 Tendo ficado Absalão dois anos em Jerusalém e sem ver a face do rei,
29 mandou ele chamar a Joabe, para o enviar ao rei; porém ele não quis vir. Mandou chamá-lo segunda vez, mas ainda não quis ele vir.
30 Então, disse aos seus servos: Vede ali o pedaço de campo de Joabe pegado ao meu, e tem cevada nele; ide e metei-lhe fogo. E os servos de Absalão meteram fogo nesse pedaço de campo.
31 Então, Joabe se levantou, e foi à casa de Absalão, e lhe disse: Por que meteram fogo os teus servos no pedaço de campo que é meu?
32 Respondeu Absalão a Joabe: Mandei chamar-te, dizendo: Vem cá, para que te envie ao rei, a dizer-lhe: Para que vim de Gesur? Melhor me fora estar ainda lá. Agora, pois, quero ver a face do rei; se há em mim alguma culpa, que me mate.
33 Então, Joabe foi ao rei e lho disse. Chamou o rei a Absalão, e este se lhe apresentou e inclinou-se sobre o rosto em terra, diante do rei. O rei beijou a Absalão.*
1 Depois disto, Absalão fez aparelhar para si um carro e cavalos e cinquenta homens que corressem adiante dele.
2 Levantando-se Absalão pela manhã, parava à entrada da porta; e a todo homem que tinha alguma demanda para vir ao rei a juízo, o chamava Absalão a si e lhe dizia: De que cidade és tu? Ele respondia: De tal tribo de Israel é teu servo.
3 Então, Absalão lhe dizia: Olha, a tua causa é boa e reta, porém não tens quem te ouça da parte do rei.
4 Dizia mais Absalão: Ah! Quem me dera ser juiz na terra, para que viesse a mim todo homem que tivesse demanda ou questão, para que lhe fizesse justiça!
5 Também, quando alguém se chegava para inclinar-se diante dele, ele estendia a mão, pegava-o e o beijava.
6 Desta maneira fazia Absalão a todo o Israel que vinha ao rei para juízo e, assim, ele furtava o coração dos homens de Israel.
7 Ao cabo de quatro anos, disse Absalão ao rei: Deixa-me ir a Hebrom cumprir o voto que fiz ao Senhor.
8 Porque, morando em Gesur, na Síria, fez o teu servo um voto, dizendo: Se o Senhor me fizer tornar a Jerusalém, prestarei culto ao Senhor.
9 Então, lhe disse o rei: Vai-te em paz. Levantou-se, pois, e foi para Hebrom.
10 Enviou Absalão emissários secretos por todas as tribos de Israel, dizendo: Quando ouvirdes o som das trombetas, direis: Absalão é rei em Hebrom!
11 De Jerusalém foram com Absalão duzentos homens convidados, porém iam na sua simplicidade, porque nada sabiam daquele negócio.
12 Também Absalão mandou vir Aitofel, o gilonita, do conselho de Davi, da sua cidade de Gilo; enquanto ele oferecia os seus sacrifícios, tornou-se poderosa a conspirata, e crescia em número o povo que tomava o partido de Absalão.
13 Então, veio um mensageiro a Davi, dizendo: Todo o povo de Israel segue decididamente a Absalão.
14 Disse, pois, Davi a todos os seus homens que estavam com ele em Jerusalém: Levantai-vos, e fujamos, porque não poderemos salvar-nos de Absalão. Dai-vos pressa a sair, para que não nos alcance de súbito, lance sobre nós algum mal e fira a cidade a fio de espada.
15 Então, os homens do rei lhe disseram: Eis aqui os teus servos, para tudo quanto determinar o rei, nosso senhor.
16 Saiu o rei, e todos os de sua casa o seguiram; deixou, porém, o rei dez concubinas, para cuidarem da casa.
17 Tendo, pois, saído o rei com todo o povo após ele, pararam na última casa.
18 Todos os seus homens passaram ao pé dele; também toda a guarda real e todos os geteus, seiscentos homens que o seguiram de Gate, passaram adiante do rei.
19 Disse, pois, o rei a Itai, o geteu: Por que irias também tu conosco? Volta e fica-te com quem vier a ser o rei, porque és estrangeiro e desterrado de tua pátria.
20 Chegaste ontem, e já te levaria eu, hoje, conosco a vaguear, quando eu mesmo não sei para onde vou? Volta, pois, e faze voltar a teus irmãos contigo. E contigo sejam misericórdia e fidelidade.
21 Respondeu, porém, Itai ao rei: Tão certo como vive o Senhor, e como vive o rei, meu senhor, no lugar em que estiver o rei, meu senhor, seja para morte seja para vida, lá estará também o teu servo.
22 Então, disse Davi a Itai: Vai e passa adiante. Assim, passou Itai, o geteu, e todos os seus homens, e todas as crianças que estavam com ele.
23 Toda a terra chorava em alta voz; e todo o povo e também o rei passaram o ribeiro de Cedrom, seguindo o caminho do deserto.
24 Eis que Abiatar subiu, e também Zadoque, e com este todos os levitas que levavam a arca da Aliança de Deus; puseram ali a arca de Deus, até que todo o povo acabou de sair da cidade.
25 Então, disse o rei a Zadoque: Torna a levar a arca de Deus à cidade. Se achar eu graça aos olhos do Senhor, ele me fará voltar para lá e me deixará ver assim a arca como a sua habitação.
26 Se ele, porém, disser: Não tenho prazer em ti, eis-me aqui; faça de mim como melhor lhe parecer.
27 Disse mais o rei a Zadoque, o sacerdote: Ó vidente, tu e Abiatar, voltai em paz para a cidade, e convosco também vossos dois filhos, Aimaás, teu filho, e Jônatas, filho de Abiatar.
28 Olhai que me demorarei nos vaus do deserto até que me venham informações vossas.
29 Zadoque, pois, e Abiatar levaram a arca de Deus para Jerusalém e lá ficaram.
30 Seguiu Davi pela encosta das Oliveiras, subindo e chorando; tinha a cabeça coberta e caminhava descalço; todo o povo que ia com ele, de cabeça coberta, subiu chorando.
31 Então, fizeram saber a Davi, dizendo: Aitofel está entre os que conspiram com Absalão. Pelo que disse Davi: Ó Senhor, peço-te que transtornes em loucura o conselho de Aitofel.
32 Ao chegar Davi ao cimo, onde se costuma adorar a Deus, eis que Husai, o arquita, veio encontrar-se com ele, de manto rasgado e terra sobre a cabeça.
33 Disse-lhe Davi: Se fores comigo, ser-me-ás pesado.
34 Porém, se voltares para a cidade e disseres a Absalão: Eu serei, ó rei, teu servo, como fui, dantes, servo de teu pai, assim, agora, serei teu servo, dissipar-me-ás, então, o conselho de Aitofel.
35 Tens lá contigo Zadoque e Abiatar, sacerdotes. Todas as coisas, pois, que ouvires da casa do rei farás saber a esses sacerdotes.
36 Lá estão com eles seus dois filhos, Aimaás, filho de Zadoque, e Jônatas, filho de Abiatar; por meio deles, me mandareis notícias de todas as coisas que ouvirdes.
37 Husai, pois, amigo de Davi, veio para a cidade, e Absalão entrou em Jerusalém.*
1 Tendo Davi passado um pouco além, dobrando o cimo, eis que lhe saiu ao encontro Ziba, servo de Mefibosete, com dois jumentos albardados e sobre eles duzentos pães, cem cachos de passas, cem frutas de verão e um odre de vinho.
2 Perguntou o rei a Ziba: Que pretendes com isto? Respondeu Ziba: Os jumentos são para a casa do rei, para serem montados; o pão e as frutas de verão, para os moços comerem; o vinho, para beberem os cansados no deserto.
3 Então, disse o rei: Onde está, pois, o filho de teu senhor? Respondeu Ziba ao rei: Eis que ficou em Jerusalém, pois disse: Hoje, a casa de Israel me restituirá o reino de meu pai.
4 Então, disse o rei a Ziba: Teu é tudo que pertence a Mefibosete. Disse Ziba: Eu me inclino e ache eu mercê diante de ti, ó rei, meu senhor.
5 Tendo chegado o rei Davi a Baurim, eis que dali saiu um homem da família da casa de Saul, cujo nome era Simei, filho de Gera; saiu e ia amaldiçoando.
6 Atirava pedras contra Davi e contra todos os seus servos, ainda que todo o povo e todos os valentes estavam à direita e à esquerda do rei.
7 Amaldiçoando-o, dizia Simei: Fora daqui, fora, homem de sangue, homem de Belial;
8 o Senhor te deu, agora, a paga de todo o sangue da casa de Saul, cujo reino usurpaste; o Senhor já o entregou nas mãos de teu filho Absalão; eis-te, agora, na tua desgraça, porque és homem de sangue.
9 Então, Abisai, filho de Zeruia, disse ao rei: Por que amaldiçoaria este cão morto ao rei, meu senhor? Deixa-me passar e lhe tirarei a cabeça.
10 Respondeu o rei: Que tenho eu convosco, filhos de Zeruia? Ora, deixai-o amaldiçoar; pois, se o Senhor lhe disse: Amaldiçoa a Davi, quem diria: Por que assim fizeste?
11 Disse mais Davi a Abisai e a todos os seus servos: Eis que meu próprio filho procura tirar-me a vida, quanto mais ainda este benjamita? Deixai-o; que amaldiçoe, pois o Senhor lhe ordenou.
12 Talvez o Senhor olhará para a minha aflição e o Senhor me pagará com bem a sua maldição deste dia.
13 Prosseguiam, pois, o seu caminho, Davi e os seus homens; também Simei ia ao longo do monte, ao lado dele, caminhando e amaldiçoando, e atirava pedras e terra contra ele.
14 O rei e todo o povo que ia com ele chegaram exaustos ao Jordão e ali descansaram.
15 Absalão, pois, e todo o povo, homens de Israel, vieram a Jerusalém; e, com ele, Aitofel.
16 Tendo-se apresentado Husai, o arquita, amigo de Davi, a Absalão, disse-lhe: Viva o rei, viva o rei!
17 Porém Absalão disse a Husai: É assim a tua fidelidade para com o teu amigo Davi? Por que não foste com o teu amigo?
18 Respondeu Husai a Absalão: Não, mas àquele a quem o Senhor elegeu, e todo este povo, e todos os homens de Israel, a ele pertencerei e com ele ficarei.
19 Ainda mais, a quem serviria eu? Porventura, não seria diante de seu filho? Como servi diante de teu pai, assim serei diante de ti.
20 Então, disse Absalão a Aitofel: Dai o vosso conselho sobre o que devemos fazer.
21 Disse Aitofel a Absalão: Coabita com as concubinas de teu pai, que deixou para cuidar da casa; e, em ouvindo todo o Israel que te fizeste odioso para com teu pai, animar-se-ão todos os que estão contigo.
22 Armaram, pois, para Absalão uma tenda no eirado, e ali, à vista de todo o Israel, ele coabitou com as concubinas de seu pai.
23 O conselho que Aitofel dava, naqueles dias, era como resposta de Deus a uma consulta; tal era o conselho de Aitofel, tanto para Davi como para Absalão.*
1 Disse ainda Aitofel a Absalão: Deixa-me escolher doze mil homens, e me disporei, e perseguirei Davi esta noite.
2 Assaltá-lo-ei, enquanto está cansado e frouxo de mãos; espantá-lo-ei; fugirá todo o povo que está com ele; então, matarei apenas o rei.
3 Farei voltar a ti todo o povo; pois a volta de todos depende daquele a quem procuras matar; assim, todo o povo estará em paz.
4 O parecer agradou a Absalão e a todos os anciãos de Israel.
5 Disse, porém, Absalão: Chamai, agora, a Husai, o arquita, e ouçamos também o que ele dirá.
6 Tendo Husai chegado a Absalão, este lhe falou, dizendo: Desta maneira falou Aitofel; faremos segundo a sua palavra? Se não, fala tu.
7 Então, disse Husai a Absalão: O conselho que deu Aitofel desta vez não é bom.
8 Continuou Husai: Bem conheces teu pai e seus homens e sabes que são valentes e estão enfurecidos como a ursa no campo, roubada dos seus cachorros; também teu pai é homem de guerra e não passará a noite com o povo.
9 Eis que, agora, estará de espreita nalguma cova ou em qualquer outro lugar; e será que, caindo no primeiro ataque alguns dos teus, cada um que o ouvir dirá: Houve derrota no povo que segue a Absalão.
10 Então, até o homem valente, cujo coração é como o de leões, sem dúvida desmaiará; porque todo o Israel sabe que teu pai é herói e que homens valentes são os que estão com ele.
11 Eu, porém, aconselho que a toda pressa se reúna a ti todo o Israel, desde Dã até Berseba, em multidão como a areia do mar; e que tu em pessoa vás no meio deles.
12 Então, iremos a ele em qualquer lugar em que se achar e facilmente cairemos sobre ele, como o orvalho cai sobre a terra; ele não ficará, e nenhum dos homens que com ele estão, nem um só.
13 Se ele se retirar para alguma cidade, todo o Israel levará cordas àquela cidade; e arrastá-la-emos até ao ribeiro, até que lá não se ache nem uma só pedrinha.
14 Então, disseram Absalão e todos os homens de Israel: Melhor é o conselho de Husai, o arquita, do que o de Aitofel. Pois ordenara o Senhor que fosse dissipado o bom conselho de Aitofel, para que o mal sobreviesse contra Absalão.
15 Disse Husai a Zadoque e a Abiatar, sacerdotes: Assim e assim aconselhou Aitofel a Absalão e aos anciãos de Israel; porém assim e assim aconselhei eu.
16 Agora, pois, mandai avisar depressa a Davi, dizendo: Não passes esta noite nos vaus do deserto, mas passa, sem demora, ao outro lado, para que não seja destruído o rei e todo o povo que com ele está.
17 Estavam Jônatas e Aimaás junto a En-Rogel; e uma criada lhes dava aviso, e eles iam e diziam ao rei Davi, porque não podiam ser vistos entrar na cidade.
18 Viu-os, porém, um moço e avisou a Absalão; porém ambos partiram logo, apressadamente, e entraram em casa de um homem, em Baurim, que tinha um poço no seu pátio, ao qual desceram.
19 A mulher desse homem tomou uma coberta, e a estendeu sobre a boca do poço, e espalhou grãos pilados de cereais sobre ela; assim, nada se soube.
20 Chegando, pois, os servos de Absalão à mulher, àquela casa, disseram: Onde estão Aimaás e Jônatas? Respondeu-lhes a mulher: Já passaram o vau das águas. Havendo-os procurado, sem os achar, voltaram para Jerusalém.
21 Mal se retiraram, saíram logo os dois do poço, e foram dar aviso a Davi, e lhe disseram: Levantai-vos e passai depressa as águas, porque assim e assim aconselhou Aitofel contra vós outros.
22 Então, Davi e todo o povo que com ele estava se levantaram e passaram o Jordão; quando amanheceu, já nem um só havia que não tivesse passado o Jordão.
23 Vendo, pois, Aitofel que não fora seguido o seu conselho, albardou o jumento, dispôs-se e foi para casa e para a sua cidade; pôs em ordem os seus negócios e se enforcou; morreu e foi sepultado na sepultura do seu pai.
24 Davi chegou a Maanaim. Absalão, tendo passado o Jordão com todos os homens de Israel,
25 constituiu a Amasa em lugar de Joabe sobre o exército. Era Amasa filho de certo homem chamado Itra, o ismaelita, o qual se deitara com Abigail, filha de Naás, e irmã de Zeruia, mãe de Joabe.
26 Israel, pois, e Absalão acamparam-se na terra de Gileade.
27 Tendo Davi chegado a Maanaim, Sobi, filho de Naás, de Rabá, dos filhos de Amom, e Maquir, filho de Amiel, de Lo-Debar, e Barzilai, o gileadita, de Rogelim,
28 tomaram camas, bacias e vasilhas de barro, trigo, cevada, farinha, grãos torrados, favas e lentilhas;
29 também mel, coalhada, ovelhas e queijos de gado e os trouxeram a Davi e ao povo que com ele estava, para comerem, porque disseram: Este povo no deserto está faminto, cansado e sedento.*
1 Contou Davi o povo que tinha consigo e pôs sobre eles capitães de mil e capitães de cem.
2 Davi enviou o povo: um terço sob o comando de Joabe, outro terço sob o de Abisai, filho de Zeruia e irmão de Joabe, e o outro terço sob o de Itai, o geteu. Disse o rei ao povo: Eu também sairei convosco.
3 Respondeu, porém, o povo: Não sairás, porque, se formos obrigados a fugir, não se importarão conosco, nem ainda que metade de nós morra, pois tu vales por dez mil de nós. Melhor será que da cidade nos prestes socorro.
4 Tornou-lhes Davi: O que vos agradar, isso farei. Pôs-se o rei ao lado da porta, e todo o povo saiu a centenas e a milhares.
5 Deu ordem o rei a Joabe, a Abisai e a Itai, dizendo: Tratai com brandura o jovem Absalão, por amor de mim. Todo o povo ouviu quando o rei dava a ordem a todos os capitães acerca de Absalão.
6 Saiu, pois, o povo ao campo, a encontrar-se com Israel, e deu-se a batalha no bosque de Efraim.
7 Ali, foi o povo de Israel batido diante dos servos de Davi; e, naquele mesmo dia, houve ali grande derrota, com a perda de vinte mil homens.
8 Porque aí se estendeu a batalha por toda aquela região; e o bosque, naquele dia, consumiu mais gente do que a espada.
9 Indo Absalão montado no seu mulo, encontrou-se com os homens de Davi; entrando o mulo debaixo dos ramos espessos de um carvalho, Absalão, preso nele pela cabeça, ficou pendurado entre o céu e a terra; e o mulo, que ele montava, passou adiante.
10 Vendo isto um homem, fez saber a Joabe e disse: Vi Absalão pendurado num carvalho.
11 Então, disse Joabe ao homem que lho fizera saber: Viste-o! Por que logo não o feriste ali, derrubando-o por terra? E forçoso me seria dar-te dez moedas de prata e um cinto.
12 Disse, porém, o homem a Joabe: Ainda que me pesassem nas mãos mil moedas de prata, não estenderia a mão contra o filho do rei, pois bem ouvimos que o rei te deu ordem a ti, a Abisai e a Itai, dizendo: Guardai-me o jovem Absalão.
13 Se eu tivesse procedido traiçoeiramente contra a vida dele, nada disso se esconderia ao rei, e tu mesmo te oporias.
14 Então, disse Joabe: Não devo perder tempo, assim, contigo. Tomou três dardos e traspassou com eles o coração de Absalão, estando ele ainda vivo no meio do carvalho.
15 Cercaram-no dez jovens, que levavam as armas de Joabe, e feriram a Absalão, e o mataram.
16 Então, tocou Joabe a trombeta, e o povo voltou de perseguir a Israel, porque Joabe deteve o povo.
17 Levaram Absalão, e o lançaram no bosque, numa grande cova, e levantaram sobre ele mui grande montão de pedras; todo o Israel fugiu, cada um para a sua casa.
18 Ora, Absalão, quando ainda vivia, levantara para si uma coluna, que está no vale do Rei, porque dizia: Filho nenhum tenho para conservar a memória do meu nome; e deu o seu próprio nome à coluna; pelo que até hoje se chama o Monumento de Absalão.
19 Então, disse Aimaás, filho de Zadoque: Deixa-me correr e dar notícia ao rei de que já o Senhor o vingou do poder de seus inimigos.
20 Mas Joabe lhe disse: Tu não serás, hoje, o portador de novas, porém outro dia o serás; hoje, não darás a nova, porque é morto o filho do rei.
21 Disse Joabe ao etíope: Vai tu e dize ao rei o que viste. Inclinou-se a Joabe e correu.
22 Prosseguiu Aimaás, filho de Zadoque, e disse a Joabe: Seja o que for, deixa-me também correr após o etíope. Disse Joabe: Para que, agora, correrias tu, meu filho, pois não terás recompensa das novas?
23 Seja o que for, tornou Aimaás, correrei. Então, Joabe lhe disse: Corre. Aimaás correu pelo caminho da planície e passou o etíope.
24 Davi estava assentado entre as duas portas da entrada; subiu a sentinela ao terraço da porta sobre o muro e, levantando os olhos, viu que um homem chegava correndo só.
25 Gritou, pois, a sentinela e o disse ao rei. O rei respondeu: Se vem só, traz boas notícias. E vinha andando e chegando.
26 Viu a sentinela outro homem que corria; então, gritou para a porta e disse: Eis que vem outro homem correndo só. Então, disse o rei: Também este traz boas-novas.
27 Disse mais a sentinela: Vejo o correr do primeiro; parece ser o correr de Aimaás, filho de Zadoque. Então, disse o rei: Este homem é de bem e trará boas-novas.
28 Gritou Aimaás e disse ao rei: Paz! Inclinou-se ao rei, com o rosto em terra, e disse: Bendito seja o Senhor, teu Deus, que nos entregou os homens que levantaram a mão contra o rei, meu senhor.
29 Então, perguntou o rei: Vai bem o jovem Absalão? Respondeu Aimaás: Vi um grande alvoroço, quando Joabe mandou o teu servo, ó rei, porém não sei o que era.
30 Disse o rei: Põe-te ao lado e espera aqui. Ele se pôs e esperou.
31 Chegou o etíope e disse: Boas-novas ao rei, meu senhor. Hoje, o Senhor te vingou do poder de todos os que se levantaram contra ti.
32 Então, disse o rei ao etíope: Vai bem o jovem Absalão? Respondeu o etíope: Sejam como aquele os inimigos do rei, meu senhor, e todos os que se levantam contra ti para o mal.
33 Então, o rei, profundamente comovido, subiu à sala que estava por cima da porta e chorou; e, andando, dizia: Meu filho Absalão, meu filho, meu filho Absalão! Quem me dera que eu morrera por ti, Absalão, meu filho, meu filho!*
1 Disseram a Joabe: Eis que o rei anda chorando e lastima-se por Absalão.
2 Então, a vitória se tornou, naquele mesmo dia, em luto para todo o povo; porque, naquele dia, o povo ouvira dizer: O rei está de luto por causa de seu filho.
3 Naquele mesmo dia, entrou o povo às furtadelas na cidade, como o faz quando foge envergonhado da batalha.
4 Tendo o rei coberto o rosto, exclamava em alta voz: Meu filho Absalão, Absalão, meu filho, meu filho!
5 Então, Joabe entrou na casa do rei e lhe disse: Hoje, envergonhaste a face de todos os teus servos, que livraram, hoje, a tua vida, e a vida de teus filhos, e de tuas filhas, e a vida de tuas mulheres, e de tuas concubinas,
6 amando tu os que te aborrecem e aborrecendo aos que te amam; porque, hoje, dás a entender que nada valem para contigo príncipes e servos; porque entendo, agora, que, se Absalão vivesse e todos nós, hoje, fôssemos mortos, então, estarias contente.
7 Levanta-te, agora, sai e fala segundo o coração de teus servos. Juro pelo Senhor que, se não saíres, nem um só homem ficará contigo esta noite; e maior mal te será isto do que todo o mal que tem vindo sobre ti desde a tua mocidade até agora.
8 Então, o rei se levantou e se assentou à porta, e o fizeram saber a todo o povo, dizendo: Eis que o rei está assentado à porta. Veio, pois, todo o povo apresentar-se diante do rei. Ora, Israel havia fugido, cada um para a sua tenda.
9 Todo o povo, em todas as tribos de Israel, andava altercando entre si, dizendo: O rei nos tirou das mãos de nossos inimigos, livrou-nos das mãos dos filisteus e, agora, fugiu da terra por causa de Absalão.
10 Absalão, a quem ungimos sobre nós, já morreu na peleja; agora, pois, por que vos calais e não fazeis voltar o rei?
11 Então, o rei Davi mandou dizer a Zadoque e a Abiatar, sacerdotes: Falai aos anciãos de Judá: Por que seríeis vós os últimos em tornar a trazer o rei para a sua casa, visto que aquilo que todo o Israel dizia já chegou ao rei, até à sua casa?
12 Vós sois meus irmãos, sois meu osso e minha carne; por que, pois, seríeis os últimos em tornar a trazer o rei?
13 Dizei a Amasa: Não és tu meu osso e minha carne? Deus me faça o que lhe aprouver, se não vieres a ser para sempre comandante do meu exército, em lugar de Joabe.
14 Com isto moveu o rei o coração de todos os homens de Judá, como se fora um só homem, e mandaram dizer-lhe: Volta, ó rei, tu e todos os teus servos.
15 Então, o rei voltou e chegou ao Jordão; Judá foi a Gilgal, para encontrar-se com o rei, a fim de fazê-lo passar o Jordão.
16 Apressou-se Simei, filho de Gera, benjamita, que era de Baurim, e desceu com os homens de Judá a encontrar-se com o rei Davi.
17 E, com ele, mil homens de Benjamim, como também Ziba, servo da casa de Saul, acompanhado de seus quinze filhos e seus vinte servos, e meteram-se pelo Jordão à vista do rei
18 e o atravessaram, para fazerem passar a casa real e para fazerem o que lhe era agradável. Então, Simei, filho de Gera, prostrou-se diante do rei, quando este ia passar o Jordão,
19 e lhe disse: Não me imputes, senhor, a minha culpa e não te lembres do que tão perversamente fez teu servo, no dia em que o rei, meu senhor, saiu de Jerusalém; não o conserves, ó rei, em teu coração.
20 Porque eu, teu servo, deveras confesso que pequei; por isso, sou o primeiro que, de toda a casa de José, desci a encontrar-me com o rei, meu senhor.
21 Então, respondeu Abisai, filho de Zeruia, e disse: Não morreria, pois, Simei por isto, havendo amaldiçoado ao ungido do Senhor?
22 Porém Davi disse: Que tenho eu convosco, filhos de Zeruia, para que, hoje, me sejais adversários? Morreria alguém, hoje, em Israel? Pois não sei eu que, hoje, novamente sou rei sobre Israel?
23 Então, disse o rei a Simei: Não morrerás. E lho jurou.
24 Também Mefibosete, filho de Saul, desceu a encontrar-se com o rei; não tinha tratado dos pés, nem espontado a barba, nem lavado as vestes, desde o dia em que o rei saíra até ao dia em que voltou em paz.
25 Tendo ele chegado a Jerusalém a encontrar-se com o rei, este lhe disse: Por que não foste comigo, Mefibosete?
26 Ele respondeu: Ó rei, meu senhor, o meu servo me enganou; porque eu, teu servo, dizia: albardarei um jumento e montarei para ir com o rei; pois o teu servo é coxo.
27 Demais disto, ele falsamente me acusou a mim, teu servo, diante do rei, meu senhor; porém o rei, meu senhor, é como um anjo de Deus; faze, pois, o que melhor te parecer.
28 Porque toda a casa de meu pai não era senão de homens dignos de morte diante do rei, meu senhor; contudo, puseste teu servo entre os que comem à tua mesa; que direito, pois, tenho eu de clamar ao rei?
29 Respondeu-lhe o rei: Por que ainda falas dos teus negócios? Resolvo que repartas com Ziba as terras.
30 Disse Mefibosete ao rei: Fique ele, muito embora, com tudo, pois já voltou o rei, meu senhor, em paz à sua casa.
31 Também Barzilai, o gileadita, desceu de Rogelim e passou com o rei o Jordão, para o acompanhar até ao outro lado.
32 Era Barzilai mui velho, da idade de oitenta anos; ele sustentara o rei quando este estava em Maanaim, porque era homem mui rico.
33 Disse o rei a Barzilai: Vem tu comigo, e te sustentarei em Jerusalém.
34 Respondeu Barzilai ao rei: Quantos serão ainda os dias dos anos da minha vida? Não vale a pena subir com o rei a Jerusalém.
35 Oitenta anos tenho hoje; poderia eu discernir entre o bom e o mau? Poderia o teu servo ter gosto no que come e no que bebe? Poderia eu mais ouvir a voz dos cantores e cantoras? E por que há de ser o teu servo ainda pesado ao rei, meu senhor?
36 Com o rei irá o teu servo ainda um pouco além do Jordão; por que há de me retribuir o rei com tal recompensa?
37 Deixa voltar o teu servo, e morrerei na minha cidade e serei sepultado junto de meu pai e de minha mãe; mas eis aí o teu servo Quimã; passe ele com o rei, meu senhor, e faze-lhe o que bem te parecer.
38 Respondeu o rei: Quimã passará comigo, e eu lhe farei como for do teu agrado e tudo quanto desejares de mim eu te farei.
39 Havendo, pois, todo o povo passado o Jordão e passado também o rei, este beijou a Barzilai e o abençoou; e ele voltou para sua casa.
40 Dali, passou o rei a Gilgal, e Quimã passou com ele; todo o povo de Judá e metade do povo de Israel acompanharam o rei.
41 Eis que todos os homens de Israel vieram ter com o rei e lhe disseram: Por que te furtaram nossos irmãos, os homens de Judá, e conduziram o rei, e a sua casa através do Jordão, e todos os homens de Davi com eles?
42 Então, responderam todos os homens de Judá aos homens de Israel: Porque o rei é nosso parente; por que, pois, vos irais por isso? Porventura, comemos à custa do rei ou nos deu algum presente?
43 Responderam os homens de Israel aos homens de Judá e disseram: Dez tantos temos no rei, e mais a nós nos toca Davi do que a vós outros; por que, pois, fizestes pouco caso de nós? Não foi a nossa palavra a primeira para fazer voltar o nosso rei? Porém a palavra dos homens de Judá foi mais dura do que a palavra dos homens de Israel.*
1 Então, se achou ali, por acaso, um homem de Belial, cujo nome era Seba, filho de Bicri, homem de Benjamim, o qual tocou a trombeta e disse: Não fazemos parte de Davi, nem temos herança no filho de Jessé; cada um para as suas tendas, ó Israel.
2 Então, todos os homens de Israel se separaram de Davi e seguiram Seba, filho de Bicri; porém os homens de Judá se apegaram ao seu rei, conduzindo-o desde o Jordão até Jerusalém.
3 Vindo, pois, Davi para sua casa, a Jerusalém, tomou o rei as suas dez concubinas, que deixara para cuidar da casa, e as pôs em custódia, e as sustentou, porém não coabitou com elas; e estiveram encerradas até ao dia em que morreram, vivendo como viúvas.
4 Disse o rei a Amasa: Convoca-me, para dentro de três dias, os homens de Judá e apresenta-te aqui.
5 Partiu Amasa para convocar os homens de Judá; porém demorou-se além do tempo que lhe fora aprazado.
6 Então, disse Davi a Abisai: Mais mal, agora, nos fará Seba, o filho de Bicri, do que Absalão; pelo que toma tu os servos de teu senhor e persegue-o, para que não ache para si cidades fortificadas e nos escape.
7 Então, o perseguiram os homens de Joabe, a guarda real e todos os valentes; estes saíram de Jerusalém para perseguirem Seba, filho de Bicri.
8 Chegando eles, pois, à pedra grande que está junto a Gibeão, Amasa veio perante eles; trazia Joabe vestes militares e sobre elas um cinto, no qual, presa aos seus lombos, estava uma espada dentro da bainha; adiantando-se ele, fez cair a espada.
9 Disse Joabe a Amasa: Vais bem, meu irmão? E, com a mão direita, lhe pegou a barba, para o beijar.
10 Amasa não se importou com a espada que estava na mão de Joabe, de sorte que este o feriu com ela no abdômen e lhe derramou por terra as entranhas; não o feriu segunda vez, e morreu. Então, Joabe e Abisai, seu irmão, perseguiram a Seba, filho de Bicri.
11 Mas um, dentre os moços de Joabe, parou junto de Amasa e disse: Quem está do lado de Joabe e é por Davi, siga a Joabe.
12 Amasa se revolvia no seu sangue no meio do caminho; vendo o moço que todo o povo parava, desviou a Amasa do caminho para o campo e lançou sobre ele um manto; porque via que todo aquele que chegava a ele parava.
13 Uma vez afastado do caminho, todos os homens seguiram Joabe, para perseguirem Seba, filho de Bicri.
14 Seba passou por todas as tribos de Israel até Abel-Bete-Maaca; e apenas os beritas se ajuntaram todos e o seguiram.
15 Vieram Joabe e os homens, e o cercaram em Abel-Bete-Maaca, e levantaram contra a cidade um montão da altura do muro; e todo o povo que estava com Joabe trabalhava no muro para o derribar.
16 Então, uma mulher sábia gritou de dentro da cidade: Ouvi, ouvi; dizei a Joabe: Chega-te cá, para que eu fale contigo.
17 Chegando-se ele, perguntou-lhe a mulher: És tu Joabe? Respondeu: Eu sou. Ela lhe disse: Ouve as palavras de tua serva. Disse ele: Ouço.
18 Então, disse ela: Antigamente, se costumava dizer: Peça-se conselho em Abel; e assim davam cabo das questões.
19 Eu sou uma das pacíficas e das fiéis em Israel; e tu procuras destruir uma cidade e uma mãe em Israel; por que, pois, devorarias a herança do Senhor?
20 Respondeu Joabe e disse: Longe, longe de mim que eu devore e destrua!
21 A coisa não é assim; porém um homem da região montanhosa de Efraim, cujo nome é Seba, filho de Bicri, levantou a mão contra o rei, contra Davi; entregai-me só este, e retirar-me-ei da cidade. Então, disse a mulher a Joabe: Eis que te será lançada a sua cabeça pelo muro.
22 E a mulher, na sua sabedoria, foi ter com todo o povo, e cortaram a cabeça de Seba, filho de Bicri, e a lançaram a Joabe. Então, tocou este a trombeta, e se retiraram da cidade, cada um para sua casa. E Joabe voltou a Jerusalém, a ter com o rei.
23 Joabe era comandante de todo o exército de Israel; e Benaia, filho de Joiada, da guarda real;
24 Adorão, dos que estavam sujeitos a trabalhos forçados; Josafá, filho de Ailude, era o cronista.
25 Seva, o escrivão; Zadoque e Abiatar, os sacerdotes;
26 e também Ira, o jairita, era ministro de Davi.*
1 Houve, em dias de Davi, uma fome de três anos consecutivos. Davi consultou ao Senhor, e o Senhor lhe disse: Há culpa de sangue sobre Saul e sobre a sua casa, porque ele matou os gibeonitas.
2 Então, chamou o rei os gibeonitas e lhes falou. Os gibeonitas não eram dos filhos de Israel, mas do resto dos amorreus; e os filhos de Israel lhes tinham jurado poupá-los, porém Saul procurou destruí-los no seu zelo pelos filhos de Israel e de Judá.
3 Perguntou Davi aos gibeonitas: Que quereis que eu vos faça? E que resgate vos darei, para que abençoeis a herança do Senhor?
4 Então, os gibeonitas lhe disseram: Não é por prata nem ouro que temos questão com Saul e com sua casa; nem tampouco pretendemos matar pessoa alguma em Israel. Disse Davi: Que é, pois, que quereis que vos faça?
5 Responderam ao rei: Quanto ao homem que nos destruiu e procurou que fôssemos assolados, sem que pudéssemos subsistir em limite algum de Israel,
6 de seus filhos se nos deem sete homens, para que os enforquemos ao Senhor, em Gibeá de Saul, o eleito do Senhor. Disse o rei: Eu os darei.
7 Porém o rei poupou a Mefibosete, filho de Jônatas, filho de Saul, por causa do juramento ao Senhor, que entre eles houvera, entre Davi e Jônatas, filho de Saul.
8 Porém tomou o rei os dois filhos de Rispa, filha de Aiá, que tinha tido de Saul, a saber, a Armoni e a Mefibosete, como também os cinco filhos de Merabe, filha de Saul, que tivera de Adriel, filho de Barzilai, meolatita;
9 e os entregou nas mãos dos gibeonitas, os quais os enforcaram no monte, perante o Senhor; caíram os sete juntamente. Foram mortos nos dias da ceifa, nos primeiros dias, no princípio da ceifa da cevada.
10 Então, Rispa, filha de Aiá, tomou um pano de saco e o estendeu para si sobre uma penha, desde o princípio da ceifa até que sobre eles caiu água do céu; e não deixou que as aves do céu se aproximassem deles de dia, nem os animais do campo, de noite.
11 Foi dito a Davi o que fizera Rispa, filha de Aiá e concubina de Saul.
12 Então, foi Davi e tomou os ossos de Saul e os ossos de Jônatas, seu filho, dos moradores de Jabes-Gileade, os quais os furtaram da praça de Bete-Seã, onde os filisteus os tinham pendurado, no dia em que feriram Saul em Gilboa.
13 Dali, transportou os ossos de Saul e os ossos de Jônatas, seu filho; e ajuntaram também os ossos dos enforcados.
14 Enterraram os ossos de Saul e de Jônatas, seu filho, na terra de Benjamim, em Zela, na sepultura de Quis, seu pai. Fizeram tudo o que o rei ordenara. Depois disto, Deus se tornou favorável para com a terra.
15 De novo, fizeram os filisteus guerra contra Israel. Desceu Davi com os seus homens, e pelejaram contra os filisteus, ficando Davi mui fatigado.
16 Isbi-Benobe descendia dos gigantes; o peso do bronze de sua lança era de trezentos siclos, e estava cingido de uma armadura nova; este intentou matar a Davi.
17 Porém Abisai, filho de Zeruia, socorreu-o, feriu o filisteu e o matou; então, os homens de Davi lhe juraram, dizendo: Nunca mais sairás conosco à peleja, para que não apagues a lâmpada de Israel.
18 Depois disto, houve ainda, em Gobe, outra peleja contra os filisteus; então, Sibecai, o husatita, feriu a Safe, que era descendente dos gigantes.
19 Houve ainda, em Gobe, outra peleja contra os filisteus; e Elanã, filho de Jaaré-Oregim, o belemita, feriu a Golias, o geteu, cuja lança tinha a haste como eixo de tecelão.
20 Houve ainda outra peleja; esta foi em Gate, onde estava um homem de grande estatura, que tinha em cada mão e em cada pé seis dedos, vinte e quatro ao todo; também este descendia dos gigantes.
21 Quando ele injuriava a Israel, Jônatas, filho de Simeia, irmão de Davi, o feriu.
22 Estes quatro nasceram dos gigantes em Gate; e caíram pela mão de Davi e pela mão de seus homens.*
1 Falou Davi ao Senhor as palavras deste cântico, no dia em que o Senhor o livrou das mãos de todos os seus inimigos e das mãos de Saul.
2 E disse: O Senhor é a minha rocha, a minha cidadela, o meu libertador;
3 o meu Deus, o meu rochedo em que me refugio; o meu escudo, a força da minha salvação, o meu baluarte e o meu refúgio. Ó Deus, da violência tu me salvas.
4 Invoco o Senhor, digno de ser louvado, e serei salvo dos meus inimigos.
5 Porque ondas de morte me cercaram, torrentes de impiedade me impuseram terror;
6 cadeias infernais me cingiram, e tramas de morte me surpreenderam.
7 Na minha angústia, invoquei o Senhor, clamei a meu Deus; ele, do seu templo, ouviu a minha voz, e o meu clamor chegou aos seus ouvidos.
8 Então, a terra se abalou e tremeu, vacilaram também os fundamentos dos céus e se estremeceram, porque ele se indignou.
9 Das suas narinas, subiu fumaça, e, da sua boca, fogo devorador; dele saíram carvões, em chama.
10 Baixou ele os céus, e desceu, e teve sob os pés densa escuridão.
11 Cavalgava um querubim e voou; e foi visto sobre as asas do vento.
12 Por pavilhão pôs, ao redor de si, trevas, ajuntamento de águas, nuvens dos céus.
13 Do resplendor que diante dele havia, brasas de fogo se acenderam.
14 Trovejou o Senhor desde os céus; o Altíssimo levantou a sua voz.
15 Despediu setas, e espalhou os meus inimigos, e raios, e os desbaratou.
16 Então, se viu o leito das águas, e se descobriram os fundamentos do mundo, pela repreensão do Senhor, pelo iroso resfolgar das suas narinas.
17 Do alto, me estendeu ele a mão e me tomou; tirou-me das muitas águas.
18 Livrou-me do forte inimigo, dos que me aborreciam, porque eram mais poderosos do que eu.
19 Assaltaram-me no dia da minha calamidade, mas o Senhor me serviu de amparo.
20 Trouxe-me para um lugar espaçoso; livrou-me, porque ele se agradou de mim.
21 Retribuiu-me o Senhor segundo a minha justiça, recompensou-me conforme a pureza das minhas mãos.
22 Pois tenho guardado os caminhos do Senhor e não me apartei perversamente do meu Deus.
23 Porque todos os seus juízos me estão presentes, e dos seus estatutos não me desviei.
24 Também fui inculpável para com ele e me guardei da iniquidade.
25 Daí, retribuir-me o Senhor segundo a minha justiça, segundo a minha pureza diante dos seus olhos.
26 Para com o benigno, benigno te mostras; com o íntegro, também íntegro.
27 Com o puro, puro te mostras; com o perverso, inflexível.
28 Tu salvas o povo humilde, mas, com um lance de vista, abates os altivos.
29 Tu, Senhor, és a minha lâmpada; o Senhor derrama luz nas minhas trevas.
30 Pois contigo desbarato exércitos, com o meu Deus, salto muralhas.
31 O caminho de Deus é perfeito; a palavra do Senhor é provada; ele é escudo para todos os que nele se refugiam.
32 Pois quem é Deus, senão o Senhor? E quem é rochedo, senão o nosso Deus?
33 Deus é a minha fortaleza e a minha força e ele perfeitamente desembaraça o meu caminho.
34 Ele deu a meus pés a ligeireza das corças e me firmou nas minhas alturas.
35 Ele adestrou as minhas mãos para o combate, de sorte que os meus braços vergaram um arco de bronze.
36 Também me deste o escudo do teu salvamento, e a tua clemência me engrandeceu.
37 Alongaste sob meus passos o caminho, e os meus pés não vacilaram.
38 Persegui os meus inimigos, e os derrotei, e só voltei depois de haver dado cabo deles.
39 Acabei com eles, esmagando-os a tal ponto, que não puderam levantar-se; caíram sob meus pés.
40 Pois de força me cingiste para o combate e me submeteste os que se levantaram contra mim.
41 Também puseste em fuga os meus inimigos, e os que me odiaram, eu os exterminei.
42 Olharam, mas ninguém lhes acudiu, sim, para o Senhor, mas ele não respondeu.
43 Então, os moí como o pó da terra; esmaguei-os e, como a lama das ruas, os amassei.
44 Das contendas do meu povo me livraste e me fizeste cabeça das nações; povo que não conheci me serviu.
45 Os estrangeiros se me sujeitaram; ouvindo a minha voz, me obedeceram.
46 Sumiram-se os estrangeiros e das suas fortificações saíram espavoridos.
47 Vive o Senhor, e bendita seja a minha Rocha! Exaltado seja o meu Deus, a Rocha da minha salvação!
48 O Deus que por mim tomou vingança e me submeteu povos;
49 o Deus que me tirou dentre os meus inimigos; sim, tu que me exaltaste acima dos meus adversários e me livraste do homem violento.
50 Celebrar-te-ei, pois, entre as nações, ó Senhor, e cantarei louvores ao teu nome.
51 É ele quem dá grandes vitórias ao seu rei e usa de benignidade para com o seu ungido, com Davi e sua posteridade, para sempre.*
1 São estas as últimas palavras de Davi: Palavra de Davi, filho de Jessé, palavra do homem que foi exaltado, do ungido do Deus de Jacó, do mavioso salmista de Israel.
2 O Espírito do Senhor fala por meu intermédio, e a sua palavra está na minha língua.
3 Disse o Deus de Israel, a Rocha de Israel a mim me falou: Aquele que domina com justiça sobre os homens, que domina no temor de Deus,
4 é como a luz da manhã, quando sai o sol, como manhã sem nuvens, cujo esplendor, depois da chuva, faz brotar da terra a erva.
5 Não está assim com Deus a minha casa? Pois estabeleceu comigo uma aliança eterna, em tudo bem-definida e segura. Não me fará ele prosperar toda a minha salvação e toda a minha esperança?
6 Porém os filhos de Belial serão todos lançados fora como os espinhos, pois não podem ser tocados com as mãos,
7 mas qualquer, para os tocar, se armará de ferro e da haste de uma lança; e a fogo serão totalmente queimados no seu lugar.
8 São estes os nomes dos valentes de Davi: Josebe-Bassebete, filho de Taquemoni, o principal de três; este brandiu a sua lança contra oitocentos e os feriu de uma vez.
9 Depois dele, Eleazar, filho de Dodô, filho de Aoí, entre os três valentes que estavam com Davi, quando desafiaram os filisteus ali reunidos para a peleja. Quando já se haviam retirado os filhos de Israel,
10 ele se levantou e feriu os filisteus, até lhe cansar a mão e ficar pegada à espada; naquele dia, o Senhor efetuou grande livramento; e o povo voltou para onde Eleazar estava somente para tomar os despojos.
11 Depois dele, Sama, filho de Agé, o hararita, quando os filisteus se ajuntaram em Leí, onde havia um pedaço de terra cheio de lentilhas; e o povo fugia de diante dos filisteus.
12 Pôs-se Sama no meio daquele terreno, e o defendeu, e feriu os filisteus; e o Senhor efetuou grande livramento.
13 Também três dos trinta cabeças desceram e, no tempo da sega, foram ter com Davi, à caverna de Adulão; e uma tropa de filisteus se acampara no vale dos Refains.
14 Davi estava na fortaleza, e a guarnição dos filisteus, em Belém.
15 Suspirou Davi e disse: Quem me dera beber água do poço que está junto à porta de Belém!
16 Então, aqueles três valentes romperam pelo acampamento dos filisteus, e tiraram água do poço junto à porta de Belém, e tomaram-na, e a levaram a Davi; ele não a quis beber, porém a derramou como libação ao Senhor.
17 E disse: Longe de mim, ó Senhor, fazer tal coisa; beberia eu o sangue dos homens que lá foram com perigo de sua vida? De maneira que não a quis beber. São estas as coisas que fizeram os três valentes.
18 Também Abisai, irmão de Joabe, filho de Zeruia, era cabeça de trinta; e alçou a sua lança contra trezentos e os feriu. E tinha nome entre os primeiros três.
19 Era ele mais nobre do que os trinta e era o primeiro deles; contudo, aos primeiros três não chegou.
20 Também Benaia, filho de Joiada, era homem valente de Cabzeel e grande em obras; feriu ele dois heróis de Moabe. Desceu numa cova e nela matou um leão no tempo da neve.
21 Matou também um egípcio, homem de grande estatura; o egípcio trazia uma lança, mas Benaia o atacou com um cajado, arrancou-lhe da mão a lança e com ela o matou.
22 Estas coisas fez Benaia, filho de Joiada, pelo que teve nome entre os primeiros três valentes.
23 Era mais nobre do que os trinta, porém aos três primeiros não chegou, e Davi o pôs sobre a sua guarda.
24 Entre os trinta figuravam: Asael, irmão de Joabe; Elanã, filho de Dodô, de Belém;
25 Sama, harodita; Elica, harodita;
26 Heles, paltita; Ira, filho de Iques, tecoíta;
27 Abiezer, anatotita; Mebunai, husatita;
28 Zalmom, aoíta; Maarai, netofatita;
29 Helebe, filho de Baaná, netofatita; Itai, filho de Ribai, de Gibeá, dos filhos de Benjamim;
30 Benaia, piratonita; Hidai, do ribeiro de Gaás;
31 Abi-Albom, arbatita; Azmavete, barumita;
32 Eliaba, saalbonita; os filhos de Jasém; Jônatas;
33 Sama, hararita; Aião, filho de Sarar, ararita;
34 Elifelete, filho de Aasbai, filho de um maacatita; Eliã, filho de Aitofel, gilonita;
35 Hezrai, carmelita; Paarai, arbita;
36 Igal, filho de Natã, de Zobá; Bani, gadita;
37 Zeleque, amonita; Naarai, beerotita, o que trazia as armas de Joabe, filho de Zeruia;
38 Ira, itrita; Garebe, itrita;
39 Urias, heteu; ao todo, trinta e sete.*
1 Tornou a ira do Senhor a acender-se contra os israelitas, e ele incitou a Davi contra eles, dizendo: Vai, levanta o censo de Israel e de Judá.
2 Disse, pois, o rei a Joabe, comandante do seu exército: Percorre todas as tribos de Israel, de Dã até Berseba, e levanta o censo do povo, para que eu saiba o seu número.
3 Então, disse Joabe ao rei: Ora, multiplique o Senhor, teu Deus, a este povo cem vezes mais, e o rei, meu senhor, o veja; mas por que tem prazer nisto o rei, meu senhor?
4 Porém a palavra do rei prevaleceu contra Joabe e contra os chefes do exército; saiu, pois, Joabe com os chefes do exército da presença do rei, a levantar o censo do povo de Israel.
5 Tendo eles passado o Jordão, acamparam-se em Aroer, à direita da cidade que está no meio do vale de Gade, e foram a Jazer.
6 Daqui foram a Gileade e chegaram até Cades, na terra dos heteus; seguiram a Dã-Jaã e viraram-se para Sidom;
7 chegaram à fortaleza de Tiro e a todas as cidades dos heveus e dos cananeus, donde saíram para o Neguebe de Judá, a Berseba.
8 Assim, percorreram toda a terra e, ao cabo de nove meses e vinte dias, chegaram a Jerusalém.
9 Deu Joabe ao rei o recenseamento do povo: havia em Israel oitocentos mil homens de guerra, que puxavam da espada; e em Judá eram quinhentos mil.
10 Sentiu Davi bater-lhe o coração, depois de haver recenseado o povo, e disse ao Senhor: Muito pequei no que fiz; porém, agora, ó Senhor, peço-te que perdoes a iniquidade do teu servo; porque procedi mui loucamente.
11 Ao levantar-se Davi pela manhã, veio a palavra do Senhor ao profeta Gade, vidente de Davi, dizendo:
12 Vai e dize a Davi: Assim diz o Senhor: Três coisas te ofereço; escolhe uma delas, para que ta faça.
13 Veio, pois, Gade a Davi e lho fez saber, dizendo: Queres que sete anos de fome te venham à tua terra? Ou que, por três meses, fujas diante de teus inimigos, e eles te persigam? Ou que, por três dias, haja peste na tua terra? Delibera, agora, e vê que resposta hei de dar ao que me enviou.
14 Então, disse Davi a Gade: Estou em grande angústia; porém caiamos nas mãos do Senhor, porque muitas são as suas misericórdias; mas, nas mãos dos homens, não caia eu.
15 Então, enviou o Senhor a peste a Israel, desde a manhã até ao tempo que determinou; e, de Dã até Berseba, morreram setenta mil homens do povo.
16 Estendendo, pois, o Anjo do Senhor a mão sobre Jerusalém, para a destruir, arrependeu-se o Senhor do mal e disse ao Anjo que fazia a destruição entre o povo: Basta, retira a mão. O Anjo estava junto à eira de Araúna, o jebuseu.
17 Vendo Davi ao Anjo que feria o povo, falou ao Senhor e disse: Eu é que pequei, eu é que procedi perversamente; porém estas ovelhas que fizeram? Seja, pois, a tua mão contra mim e contra a casa de meu pai.
18 Naquele mesmo dia, veio Gade ter com Davi e lhe disse: Sobe, levanta ao Senhor um altar na eira de Araúna, o jebuseu.
19 Davi subiu segundo a palavra de Gade, como o Senhor lhe havia ordenado.
20 Olhou Araúna do alto e, vendo que vinham para ele o rei e os seus homens, saiu e se inclinou diante do rei, com o rosto em terra.
21 E perguntou: Por que vem o rei, meu senhor, ao seu servo? Respondeu Davi: Para comprar de ti esta eira, a fim de edificar nela um altar ao Senhor, para que cesse a praga de sobre o povo.
22 Então, disse Araúna a Davi: Tome e ofereça o rei, meu senhor, o que bem lhe parecer; eis aí os bois para o holocausto, e os trilhos, e a apeiragem dos bois para a lenha.
23 Tudo isto, ó rei, Araúna oferece ao rei; e ajuntou: Que o Senhor, teu Deus, te seja propício.
24 Porém o rei disse a Araúna: Não, mas eu to comprarei pelo devido preço, porque não oferecerei ao Senhor, meu Deus, holocaustos que não me custem nada. Assim, Davi comprou a eira e pelos bois pagou cinquenta siclos de prata.
25 Edificou ali Davi ao Senhor um altar e apresentou holocaustos e ofertas pacíficas. Assim, o Senhor se tornou favorável para com a terra, e a praga cessou de sobre Israel.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'2_Samuel','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)