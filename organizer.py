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
1 Palavras de Jeremias, filho de Hilquias, um dos sacerdotes que estavam em Anatote, na terra de Benjamim;
2 a ele veio a palavra do Senhor, nos dias de Josias, filho de Amom e rei de Judá, no décimo terceiro ano do seu reinado;
3 e também nos dias de Jeoaquim, filho de Josias, rei de Judá, até ao fim do ano undécimo de Zedequias, filho de Josias, rei de Judá, e ainda até ao quinto mês do exílio de Jerusalém.
4 A mim me veio, pois, a palavra do Senhor, dizendo:
5 Antes que eu te formasse no ventre materno, eu te conheci, e, antes que saísses da madre, te consagrei, e te constituí profeta às nações.
6 Então, lhe disse eu: ah! Senhor Deus! Eis que não sei falar, porque não passo de uma criança.
7 Mas o Senhor me disse: Não digas: Não passo de uma criança; porque a todos a quem eu te enviar irás; e tudo quanto eu te mandar falarás.
8 Não temas diante deles, porque eu sou contigo para te livrar, diz o Senhor.
9 Depois, estendeu o Senhor a mão, tocou-me na boca e o Senhor me disse: Eis que ponho na tua boca as minhas palavras.
10 Olha que hoje te constituo sobre as nações e sobre os reinos, para arrancares e derribares, para destruíres e arruinares e também para edificares e para plantares.
11 Veio ainda a palavra do Senhor, dizendo: Que vês tu, Jeremias? Respondi: vejo uma vara de amendoeira.
12 Disse-me o Senhor: Viste bem, porque eu velo sobre a minha palavra para a cumprir.
13 Outra vez, me veio a palavra do Senhor, dizendo: Que vês? Eu respondi: vejo uma panela ao fogo, cuja boca se inclina do Norte.
14 Disse-me o Senhor: Do Norte se derramará o mal sobre todos os habitantes da terra.
15 Pois eis que convoco todas as tribos dos reinos do Norte, diz o Senhor; e virão, e cada reino porá o seu trono à entrada das portas de Jerusalém e contra todos os seus muros em redor e contra todas as cidades de Judá.
16 Pronunciarei contra os moradores destas as minhas sentenças, por causa de toda a malícia deles; pois me deixaram a mim, e queimaram incenso a deuses estranhos, e adoraram as obras das suas próprias mãos.
17 Tu, pois, cinge os lombos, dispõe-te e dize-lhes tudo quanto eu te mandar; não te espantes diante deles, para que eu não te infunda espanto na sua presença.
18 Eis que hoje te ponho por cidade fortificada, por coluna de ferro e por muros de bronze, contra todo o país, contra os reis de Judá, contra os seus príncipes, contra os seus sacerdotes e contra o seu povo.
19 Pelejarão contra ti, mas não prevalecerão; porque eu sou contigo, diz o Senhor, para te livrar.*
1 A mim me veio a palavra do Senhor, dizendo:
2 Vai e clama aos ouvidos de Jerusalém: Assim diz o Senhor: Lembro-me de ti, da tua afeição quando eras jovem, e do teu amor quando noiva, e de como me seguias no deserto, numa terra em que se não semeia.
3 Então, Israel era consagrado ao Senhor e era as primícias da sua colheita; todos os que o devoraram se faziam culpados; o mal vinha sobre eles, diz o Senhor.
4 Ouvi a palavra do Senhor, ó casa de Jacó e todas as famílias da casa de Israel.
5 Assim diz o Senhor: Que injustiça acharam vossos pais em mim, para de mim se afastarem, indo após a nulidade dos ídolos e se tornando nulos eles mesmos,
6 e sem perguntarem: Onde está o Senhor, que nos fez subir da terra do Egito? Que nos guiou através do deserto, por uma terra de ermos e de covas, por uma terra de sequidão e sombra de morte, por uma terra em que ninguém transitava e na qual não morava homem algum?
7 Eu vos introduzi numa terra fértil, para que comêsseis o seu fruto e o seu bem; mas, depois de terdes entrado nela, vós a contaminastes e da minha herança fizestes abominação.
8 Os sacerdotes não disseram: Onde está o Senhor? E os que tratavam da lei não me conheceram, os pastores prevaricaram contra mim, os profetas profetizaram por Baal e andaram atrás de coisas de nenhum proveito.
9 Portanto, ainda pleitearei convosco, diz o Senhor, e até com os filhos de vossos filhos pleitearei.
10 Passai às terras do mar de Chipre e vede; mandai mensageiros a Quedar, e atentai bem, e vede se jamais sucedeu coisa semelhante.
11 Houve alguma nação que trocasse os seus deuses, posto que não eram deuses? Todavia, o meu povo trocou a sua Glória por aquilo que é de nenhum proveito.
12 Espantai-vos disto, ó céus, e horrorizai-vos! Ficai estupefatos, diz o Senhor.
13 Porque dois males cometeu o meu povo: a mim me deixaram, o manancial de águas vivas, e cavaram cisternas, cisternas rotas, que não retêm as águas.
14 Acaso, é Israel escravo ou servo nascido em casa? Por que, pois, veio a ser presa?
15 Os leões novos rugiram contra ele, levantaram a voz; da terra dele fizeram uma desolação; as suas cidades estão queimadas, e não há quem nelas habite.
16 Até os filhos de Mênfis e de Tafnes te pastaram o alto da cabeça.
17 Acaso, tudo isto não te sucedeu por haveres deixado o Senhor, teu Deus, quando te guiava pelo caminho?
18 Agora, pois, que lucro terás indo ao Egito para beberes as águas do Nilo; ou indo à Assíria para beberes as águas do Eufrates?
19 A tua malícia te castigará, e as tuas infidelidades te repreenderão; sabe, pois, e vê que mau e quão amargo é deixares o Senhor, teu Deus, e não teres temor de mim, diz o Senhor, o Senhor dos Exércitos.
20 Ainda que há muito quebrava eu o teu jugo e rompia as tuas ataduras, dizias tu: Não quero servir-te. Pois, em todo outeiro alto e debaixo de toda árvore frondosa, te deitavas e te prostituías.
21 Eu mesmo te plantei como vide excelente, da semente mais pura; como, pois, te tornaste para mim uma planta degenerada, como de vide brava?
22 Pelo que ainda que te laves com salitre e amontoes potassa, continua a mácula da tua iniquidade perante mim, diz o Senhor Deus.
23 Como podes dizer: Não estou maculada, não andei após os baalins? Vê o teu rasto no vale, reconhece o que fizeste, dromedária nova de ligeiros pés, que andas ziguezagueando pelo caminho;
24 jumenta selvagem, acostumada ao deserto e que, no ardor do cio, sorve o vento. Quem a impediria de satisfazer ao seu desejo? Os que a procuram não têm de fatigar-se; no mês dela a acharão.
25 Guarda-te de que os teus pés andem desnudos e a tua garganta tenha sede. Mas tu dizes: Não, é inútil; porque amo os estranhos e após eles irei.
26 Como se envergonha o ladrão quando o apanham, assim se envergonham os da casa de Israel; eles, os seus reis, os seus príncipes, os seus sacerdotes e os seus profetas,
27 que dizem a um pedaço de madeira: Tu és meu pai; e à pedra: Tu me geraste. Pois me viraram as costas e não o rosto; mas, em vindo a angústia, dizem: Levanta-te e livra-nos.
28 Onde, pois, estão os teus deuses, que para ti mesmo fizeste? Eles que se levantem se te podem livrar no tempo da tua angústia; porque os teus deuses, ó Judá, são tantos como as tuas cidades.
29 Por que contendeis comigo? Todos vós transgredistes contra mim, diz o Senhor.
30 Em vão castiguei os vossos filhos; eles não aceitaram a minha disciplina; a vossa espada devorou os vossos profetas como leão destruidor.
31 Oh! Que geração! Considerai vós a palavra do Senhor. Porventura, tenho eu sido para Israel um deserto? Ou uma terra da mais espessa escuridão? Por que, pois, diz o meu povo: Somos livres! Jamais tornaremos a ti?
32 Acaso, se esquece a virgem dos seus adornos ou a noiva do seu cinto? Todavia, o meu povo se esqueceu de mim por dias sem conta.
33 Como dispões bem os teus caminhos, para buscares o amor! Pois até às mulheres perdidas os ensinaste.
34 Nas orlas dos teus vestidos se achou também o sangue de pobres e inocentes, não surpreendidos no ato de roubar. Apesar de todas estas coisas,
35 ainda dizes: Estou inocente; certamente, a sua ira se desviou de mim. Eis que entrarei em juízo contigo, porquanto dizes: Não pequei.
36 Que mudar leviano é esse dos teus caminhos? Também do Egito serás envergonhada, como foste envergonhada da Assíria.
37 Também daquele sairás de mãos na cabeça; porque o Senhor rejeitou aqueles em quem confiaste, e não terás sorte por meio deles.*1 Se um homem repudiar sua mulher, e ela o deixar e tomar outro marido, porventura, aquele tornará a ela? Não se poluiria com isso de todo aquela terra? Ora, tu te prostituíste com muitos amantes; mas, ainda assim, torna para mim, diz o Senhor.
2 Levanta os olhos aos altos desnudos e vê; onde não te prostituíste? Nos caminhos te assentavas à espera deles como o arábio no deserto; assim, poluíste a terra com as tuas devassidões e com a tua malícia.
3 Pelo que foram retiradas as chuvas, e não houve chuva serôdia; mas tu tens a fronte de prostituta e não queres ter vergonha.
4 Não é fato que agora mesmo tu me invocas, dizendo: Pai meu, tu és o amigo da minha mocidade?
5 Conservarás para sempre a tua ira? Ou a reterás até ao fim? Sim, assim me falas, mas cometes maldade a mais não poder.
6 Disse mais o Senhor nos dias do rei Josias: Viste o que fez a pérfida Israel? Foi a todo monte alto e debaixo de toda árvore frondosa e se deu ali a toda prostituição.
7 E, depois de ela ter feito tudo isso, eu pensei que ela voltaria para mim, mas não voltou. A sua pérfida irmã Judá viu isto.
8 Quando, por causa de tudo isto, por ter cometido adultério, eu despedi a pérfida Israel e lhe dei carta de divórcio, vi que a falsa Judá, sua irmã, não temeu; mas ela mesma se foi e se deu à prostituição.
9 Sucedeu que, pelo ruidoso da sua prostituição, poluiu ela a terra; porque adulterou, adorando pedras e árvores.
10 Apesar de tudo isso, não voltou de todo o coração para mim a sua falsa irmã Judá, mas fingidamente, diz o Senhor.
11 Disse-me o Senhor: Já a pérfida Israel se mostrou mais justa do que a falsa Judá.
12 Vai, pois, e apregoa estas palavras para o lado do Norte e dize: Volta, ó pérfida Israel, diz o Senhor, e não farei cair a minha ira sobre ti, porque eu sou compassivo, diz o Senhor, e não manterei para sempre a minha ira.
13 Tão somente reconhece a tua iniquidade, reconhece que transgrediste contra o Senhor, teu Deus, e te prostituíste com os estranhos debaixo de toda árvore frondosa e não deste ouvidos à minha voz, diz o Senhor.
14 Convertei-vos, ó filhos rebeldes, diz o Senhor; porque eu sou o vosso esposo e vos tomarei, um de cada cidade e dois de cada família, e vos levarei a Sião.
15 Dar-vos-ei pastores segundo o meu coração, que vos apascentem com conhecimento e com inteligência.
16 Sucederá que, quando vos multiplicardes e vos tornardes fecundos na terra, então, diz o Senhor, nunca mais se exclamará: A arca da Aliança do Senhor! Ela não lhes virá à mente, não se lembrarão dela nem dela sentirão falta; e não se fará outra.
17 Naquele tempo, chamarão a Jerusalém de Trono do Senhor; nela se reunirão todas as nações em nome do Senhor e já não andarão segundo a dureza do seu coração maligno.
18 Naqueles dias, andará a casa de Judá com a casa de Israel, e virão juntas da terra do Norte para a terra que dei em herança a vossos pais.
19 Mas eu a mim me perguntava: como te porei entre os filhos e te darei a terra desejável, a mais formosa herança das nações? E respondi: Pai me chamarás e de mim não te desviarás.
20 Deveras, como a mulher se aparta perfidamente do seu marido, assim com perfídia te houveste comigo, ó casa de Israel, diz o Senhor.
21 Nos lugares altos, se ouviu uma voz, pranto e súplicas dos filhos de Israel; porquanto perverteram o seu caminho e se esqueceram do Senhor, seu Deus.
22 Voltai, ó filhos rebeldes, eu curarei as vossas rebeliões. Eis-nos aqui, vimos ter contigo; porque tu és o Senhor, nosso Deus.
23 Na verdade, os outeiros não passam de ilusão, nem as orgias das montanhas; com efeito, no Senhor, nosso Deus, está a salvação de Israel.
24 Mas a coisa vergonhosa devorou o labor de nossos pais, desde a nossa mocidade: as suas ovelhas e o seu gado, os seus filhos e as suas filhas.
25 Deitemo-nos em nossa vergonha, e cubra-nos a nossa ignomínia, porque temos pecado contra o Senhor, nosso Deus, nós e nossos pais, desde a nossa mocidade até ao dia de hoje; e não demos ouvidos à voz do Senhor, nosso Deus.*
1 Se voltares, ó Israel, diz o Senhor, volta para mim; se removeres as tuas abominações de diante de mim, não mais andarás vagueando;
2 se jurares pela vida do Senhor, em verdade, em juízo e em justiça, então, nele serão benditas as nações e nele se glorificarão.
3 Porque assim diz o Senhor aos homens de Judá e Jerusalém: Lavrai para vós outros campo novo e não semeeis entre espinhos.
4 Circuncidai-vos para o Senhor, circuncidai o vosso coração, ó homens de Judá e moradores de Jerusalém, para que o meu furor não saia como fogo e arda, e não haja quem o apague, por causa da malícia das vossas obras.
5 Anunciai em Judá, fazei ouvir em Jerusalém e dizei: Tocai a trombeta na terra! Gritai em alta voz, dizendo: Ajuntai-vos, e entremos nas cidades fortificadas!
6 Arvorai a bandeira rumo a Sião, fugi e não vos detenhais; porque eu faço vir do Norte um mal, uma grande destruição.
7 Já um leão subiu da sua ramada, um destruidor das nações; ele já partiu, já deixou o seu lugar para fazer da tua terra uma desolação, a fim de que as tuas cidades sejam destruídas, e ninguém as habite.
8 Cingi-vos, pois, de cilício, lamentai e uivai; porque a ira ardente do Senhor não se desviou de nós.
9 Sucederá naquele dia, diz o Senhor, que o rei e os príncipes perderão a coragem, os sacerdotes ficarão pasmados, e os profetas, estupefatos.
10 Então, disse eu: Ah! Senhor Deus! Verdadeiramente, enganaste a este povo e a Jerusalém, dizendo: Tereis paz; e eis que a espada lhe penetra até à alma.
11 Naquele tempo, se dirá a este povo e a Jerusalém: Vento abrasador dos altos desnudos do ermo assopra diretamente à filha do meu povo, não para padejar nem para alimpar.
12 Vento mais forte do que este virá ainda de minha parte, e, então, também eu pronunciarei a sentença contra eles.
13 Eis aí que sobe o destruidor como nuvens; os seus carros, como tempestade; os seus cavalos são mais ligeiros do que as águias. Ai de nós! Estamos arruinados!
14 Lava o teu coração da malícia, ó Jerusalém, para que sejas salva! Até quando hospedarás contigo os teus maus pensamentos?
15 Uma voz se faz ouvir desde Dã e anuncia a calamidade desde a região montanhosa de Efraim!
16 Proclamai isto às nações, fazei-o ouvir contra Jerusalém: De uma terra longínqua vêm sitiadores e levantam a voz contra as cidades de Judá.
17 Como os guardas de um campo, eles cercam Jerusalém, porque ela se rebelou contra mim, diz o Senhor.
18 O teu proceder e as tuas obras fizeram vir sobre ti estas coisas; a tua calamidade, que é amarga, atinge até o próprio coração.
19 Ah! Meu coração! Meu coração! Eu me contorço em dores. Oh! As paredes do meu coração! Meu coração se agita! Não posso calar-me, porque ouves, ó minha alma, o som da trombeta, o alarido de guerra.
20 Golpe sobre golpe se anuncia, pois a terra toda já está destruída; de súbito, foram destruídas as minhas tendas; num momento, as suas lonas.
21 Até quando terei de ver a bandeira, terei de ouvir a voz da trombeta?
22 Deveras, o meu povo está louco, já não me conhece; são filhos néscios e não inteligentes; são sábios para o mal e não sabem fazer o bem.
23 Olhei para a terra, e ei-la sem forma e vazia; para os céus, e não tinham luz.
24 Olhei para os montes, e eis que tremiam, e todos os outeiros estremeciam.
25 Olhei, e eis que não havia homem nenhum, e todas as aves dos céus haviam fugido.
26 Olhei ainda, e eis que a terra fértil era um deserto, e todas as suas cidades estavam derribadas diante do Senhor, diante do furor da sua ira.
27 Pois assim diz o Senhor: Toda a terra será assolada; porém não a consumirei de todo.
28 Por isso, a terra pranteará, e os céus acima se enegrecerão; porque falei, resolvi e não me arrependo, nem me retrato.
29 Ao clamor dos cavaleiros e dos flecheiros, fogem todas as cidades, entram pelas selvas e sobem pelos penhascos; todas as cidades ficam desamparadas, e já ninguém habita nelas.
30 Agora, pois, ó assolada, por que fazes assim, e te vestes de escarlata, e te adornas com enfeites de ouro, e alargas os olhos com pinturas, se debalde te fazes bela? Os amantes te desprezam e procuram tirar-te a vida.
31 Pois ouço uma voz, como de parturiente, uma angústia como da primípara em suas dores; a voz da filha de Sião, ofegante, que estende as mãos, dizendo: Ai de mim agora! Porque a minha alma desfalece por causa dos assassinos.*
1 Dai voltas às ruas de Jerusalém; vede agora, procurai saber, buscai pelas suas praças a ver se achais alguém, se há um homem que pratique a justiça ou busque a verdade; e eu lhe perdoarei a ela.
2 Embora digam: Tão certo como vive o Senhor, certamente, juram falso.
3 Ah! Senhor, não é para a fidelidade que atentam os teus olhos? Tu os feriste, e não lhes doeu; consumiste-os, e não quiseram receber a disciplina; endureceram o rosto mais do que uma rocha; não quiseram voltar.
4 Mas eu pensei: são apenas os pobres que são insensatos, pois não sabem o caminho do Senhor, o direito do seu Deus.
5 Irei aos grandes e falarei com eles; porque eles sabem o caminho do Senhor, o direito do seu Deus; mas estes, de comum acordo, quebraram o jugo e romperam as algemas.
6 Por isso, um leão do bosque os matará, um lobo dos desertos os assolará, um leopardo estará à espreita das suas cidades; qualquer que sair delas será despedaçado; porque as suas transgressões se multiplicaram, multiplicaram-se as suas perfídias.
7 Como, vendo isto, te perdoaria? Teus filhos me deixam a mim e juram pelos que não são deuses; depois de eu os ter fartado, adulteraram e em casa de meretrizes se ajuntaram em bandos;
8 como garanhões bem fartos, correm de um lado para outro, cada um rinchando à mulher do seu companheiro.
9 Deixaria eu de castigar estas coisas, diz o Senhor, ou não me vingaria de nação como esta?
10 Subi vós aos terraços da vinha, destruí-a, porém não de todo; tirai-lhe as gavinhas, porque não são do Senhor.
11 Porque perfidamente se houveram contra mim, a casa de Israel e a casa de Judá, diz o Senhor.
12 Negaram ao Senhor e disseram: Não é ele; e: Nenhum mal nos sobrevirá; não veremos espada nem fome.
13 Até os profetas não passam de vento, porque a palavra não está com eles, as suas ameaças se cumprirão contra eles mesmos.
14 Portanto, assim diz o Senhor, o Deus dos Exércitos: Visto que proferiram eles tais palavras, eis que converterei em fogo as minhas palavras na tua boca e a este povo, em lenha, e eles serão consumidos.
15 Eis que trago sobre ti uma nação de longe, ó casa de Israel, diz o Senhor; nação robusta, nação antiga, nação cuja língua ignoras; e não entendes o que ela fala.
16 A sua aljava é como uma sepultura aberta; todos os seus homens são valentes.
17 Comerão a tua sega e o teu pão, os teus filhos e as tuas filhas; comerão as tuas ovelhas e o teu gado; comerão a tua vide e a tua figueira; e com a espada derribarão as tuas cidades fortificadas, em que confias.
18 Contudo, ainda naqueles dias, diz o Senhor, não vos destruirei de todo.
19 Quando disserem: Por que nos fez o Senhor, nosso Deus, todas estas coisas? Então, lhes responderás: Como vós me deixastes e servistes a deuses estranhos na vossa terra, assim servireis a estrangeiros, em terra que não é vossa.
20 Anunciai isto na casa de Jacó e fazei-o ouvir em Judá, dizendo:
21 Ouvi agora isto, ó povo insensato e sem entendimento, que tendes olhos e não vedes, tendes ouvidos e não ouvis.
22 Não temereis a mim? — diz o Senhor; não tremereis diante de mim, que pus a areia para limite do mar, limite perpétuo, que ele não traspassará? Ainda que se levantem as suas ondas, não prevalecerão; ainda que bramem, não o traspassarão.
23 Mas este povo é de coração rebelde e contumaz; rebelaram-se e foram-se.
24 Não dizem a eles mesmos: Temamos agora ao Senhor, nosso Deus, que nos dá a seu tempo a chuva, a primeira e a última, que nos conserva as semanas determinadas da sega.
25 As vossas iniquidades desviam estas coisas, e os vossos pecados afastam de vós o bem.
26 Porque entre o meu povo se acham perversos; cada um anda espiando, como espreitam os passarinheiros; como eles, dispõem armadilhas e prendem os homens.
27 Como a gaiola cheia de pássaros, são as suas casas cheias de fraude; por isso, se tornaram poderosos e enriqueceram.
28 Engordam, tornam-se nédios e ultrapassam até os feitos dos malignos; não defendem a causa, a causa dos órfãos, para que prospere; nem julgam o direito dos necessitados.
29 Não castigaria eu estas coisas? — diz o Senhor; não me vingaria eu de nação como esta?
30 Coisa espantosa e horrenda se anda fazendo na terra:
31 os profetas profetizam falsamente, e os sacerdotes dominam de mãos dadas com eles; e é o que deseja o meu povo. Porém que fareis quando estas coisas chegarem ao seu fim?*
1 Fugi, filhos de Benjamim, do meio de Jerusalém; tocai a trombeta em Tecoa e levantai o facho sobre Bete-Haquerém, porque do lado do Norte surge um grande mal, uma grande calamidade.
2 A formosa e delicada, a filha de Sião, eu deixarei em ruínas.
3 Contra ela virão pastores com os seus rebanhos; levantarão suas tendas em redor, e cada um apascentará no seu devido lugar.
4 Preparai a guerra contra ela, disponde-vos, e subamos ao meio-dia. Ai de nós, que já declina o dia, já se vão estendendo as sombras da tarde!
5 Disponde-vos, e subamos de noite e destruamos os seus castelos.
6 Porque assim diz o Senhor dos Exércitos: Cortai árvores e levantai tranqueiras contra Jerusalém. Esta é a cidade que há de ser punida; só opressão há no meio dela.
7 Como o poço conserva frescas as suas águas, assim ela, a sua malícia; violência e estrago se ouvem nela; enfermidade e feridas há diante de mim continuamente.
8 Aceita a disciplina, ó Jerusalém, para que eu não me aparte de ti; para que eu não te torne em assolação e terra não habitada.
9 Assim diz o Senhor dos Exércitos: Diligentemente se rebuscarão os resíduos de Israel como uma vinha; vai metendo a mão, como o vindimador, por entre os sarmentos.
10 A quem falarei e testemunharei, para que ouçam? Eis que os seus ouvidos estão incircuncisos e não podem ouvir; eis que a palavra do Senhor é para eles coisa vergonhosa; não gostam dela.
11 Pelo que estou cheio da ira do Senhor; estou cansado de a conter. Derramá-la-ei sobre as crianças pelas ruas e nas reuniões de todos os jovens; porque até o marido com a mulher serão presos, e o velho, com o decrépito.
12 As suas casas passarão a outrem, os campos e também as mulheres, porque estenderei a mão contra os habitantes desta terra, diz o Senhor,
13 porque desde o menor deles até ao maior, cada um se dá à ganância, e tanto o profeta como o sacerdote usam de falsidade.
14 Curam superficialmente a ferida do meu povo, dizendo: Paz, paz; quando não há paz.
15 Serão envergonhados, porque cometem abominação sem sentir por isso vergonha; nem sabem que coisa é envergonhar-se. Portanto, cairão com os que caem; quando eu os castigar, tropeçarão, diz o Senhor.
16 Assim diz o Senhor: Ponde-vos à margem no caminho e vede, perguntai pelas veredas antigas, qual é o bom caminho; andai por ele e achareis descanso para a vossa alma; mas eles dizem: Não andaremos.
17 Também pus atalaias sobre vós, dizendo: Estai atentos ao som da trombeta; mas eles dizem: Não escutaremos.
18 Portanto, ouvi, ó nações, e informa-te, ó congregação, do que se fará entre eles!
19 Ouve tu, ó terra! Eis que eu trarei mal sobre este povo, o próprio fruto dos seus pensamentos; porque não estão atentos às minhas palavras e rejeitam a minha lei.
20 Para que, pois, me vem o incenso de Sabá e a melhor cana aromática de terras longínquas? Os vossos holocaustos não me são aprazíveis, e os vossos sacrifícios não me agradam.
21 Portanto, assim diz o Senhor: Eis que ponho tropeços a este povo; neles cairão pais e filhos juntamente; o vizinho e o seu companheiro perecerão.
22 Assim diz o Senhor: Eis que um povo vem da terra do Norte, e uma grande nação se levanta dos confins da terra.
23 Trazem arco e dardo; eles são cruéis e não usam de misericórdia; a sua voz ruge como o mar, e em cavalos vêm montados, como guerreiros em ordem de batalha contra ti, ó filha de Sião.
24 Ao ouvirmos a sua fama, afrouxam-se as nossas mãos, angústia nos toma e dores como de parturiente.
25 Não saias ao campo, nem andes pelo caminho, porque o inimigo tem espada, e há terror por todos os lados.
26 Ó filha do meu povo, cinge-te de cilício e revolve-te na cinza; pranteia como por filho único, pranto de amarguras; porque, de súbito, virá o destruidor sobre nós.
27 Qual acrisolador te estabeleci entre o meu povo, qual fortaleza, para que venhas a conhecer o seu caminho e o examines.
28 Todos eles são os mais rebeldes e andam espalhando calúnias; são bronze e ferro, são todos corruptores.
29 O fole bufa, só chumbo resulta do seu fogo; em vão continua o depurador, porque os iníquos não são separados.
30 Prata de refugo lhes chamarão, porque o Senhor os refugou.*
1 Palavra que da parte do Senhor foi dita a Jeremias:
2 Põe-te à porta da Casa do Senhor, e proclama ali esta palavra, e dize: Ouvi a palavra do Senhor, todos de Judá, vós, os que entrais por estas portas, para adorardes ao Senhor.
3 Assim diz o Senhor dos Exércitos, o Deus de Israel: Emendai os vossos caminhos e as vossas obras, e eu vos farei habitar neste lugar.
4 Não confieis em palavras falsas, dizendo: Templo do Senhor, templo do Senhor, templo do Senhor é este.
5 Mas, se deveras emendardes os vossos caminhos e as vossas obras, se deveras praticardes a justiça, cada um com o seu próximo;
6 se não oprimirdes o estrangeiro, e o órfão, e a viúva, nem derramardes sangue inocente neste lugar, nem andardes após outros deuses para vosso próprio mal,
7 eu vos farei habitar neste lugar, na terra que dei a vossos pais, desde os tempos antigos e para sempre.
8 Eis que vós confiais em palavras falsas, que para nada vos aproveitam.
9 Que é isso? Furtais e matais, cometeis adultério e jurais falsamente, queimais incenso a Baal e andais após outros deuses que não conheceis,
10 e depois vindes, e vos pondes diante de mim nesta casa que se chama pelo meu nome, e dizeis: Estamos salvos; sim, só para continuardes a praticar estas abominações!
11 Será esta casa que se chama pelo meu nome um covil de salteadores aos vossos olhos? Eis que eu, eu mesmo, vi isto, diz o Senhor.
12 Mas ide agora ao meu lugar que estava em Siló, onde, no princípio, fiz habitar o meu nome, e vede o que lhe fiz, por causa da maldade do meu povo de Israel.
13 Agora, pois, visto que fazeis todas estas obras, diz o Senhor, e eu vos falei, começando de madrugada, e não me ouvistes, chamei-vos, e não me respondestes,
14 farei também a esta casa que se chama pelo meu nome, na qual confiais, e a este lugar, que vos dei a vós outros e a vossos pais, como fiz a Siló.
15 Lançar-vos-ei da minha presença, como arrojei a todos os vossos irmãos, a toda a posteridade de Efraim.
16 Tu, pois, não intercedas por este povo, nem levantes por ele clamor ou oração, nem me importunes, porque eu não te ouvirei.
17 Acaso, não vês tu o que andam fazendo nas cidades de Judá e nas ruas de Jerusalém?
18 Os filhos apanham a lenha, os pais acendem o fogo, e as mulheres amassam a farinha, para se fazerem bolos à Rainha dos Céus; e oferecem libações a outros deuses, para me provocarem à ira.
19 Acaso, é a mim que eles provocam à ira, diz o Senhor, e não, antes, a si mesmos, para a sua própria vergonha?
20 Portanto, assim diz o Senhor Deus: Eis que a minha ira e o meu furor se derramarão sobre este lugar, sobre os homens e sobre os animais, sobre as árvores do campo e sobre os frutos da terra; arderá e não se apagará.
21 Assim diz o Senhor dos Exércitos, o Deus de Israel: Ajuntai os vossos holocaustos aos vossos sacrifícios e comei carne.
22 Porque nada falei a vossos pais, no dia em que os tirei da terra do Egito, nem lhes ordenei coisa alguma acerca de holocaustos ou sacrifícios.
23 Mas isto lhes ordenei, dizendo: Dai ouvidos à minha voz, e eu serei o vosso Deus, e vós sereis o meu povo; andai em todo o caminho que eu vos ordeno, para que vos vá bem.
24 Mas não deram ouvidos, nem atenderam, porém andaram nos seus próprios conselhos e na dureza do seu coração maligno; andaram para trás e não para diante.
25 Desde o dia em que vossos pais saíram da terra do Egito até hoje, enviei-vos todos os meus servos, os profetas, todos os dias; começando de madrugada, eu os enviei.
26 Mas não me destes ouvidos, nem me atendestes; endurecestes a cerviz e fizestes pior do que vossos pais.
27 Dir-lhes-ás, pois, todas estas palavras, mas não te darão ouvidos; chamá-los-ás, mas não te responderão.
28 Dir-lhes-ás: Esta é a nação que não atende à voz do Senhor, seu Deus, e não aceita a disciplina; já pereceu, a verdade foi eliminada da sua boca.
29 Corta os teus cabelos consagrados, ó Jerusalém, e põe-te a prantear sobre os altos desnudos; porque já o Senhor rejeitou e desamparou a geração objeto do seu furor;
30 porque os filhos de Judá fizeram o que era mau perante mim, diz o Senhor; puseram os seus ídolos abomináveis na casa que se chama pelo meu nome, para a contaminarem.
31 Edificaram os altos de Tofete, que está no vale do filho de Hinom, para queimarem a seus filhos e a suas filhas; o que nunca ordenei, nem me passou pela mente.
32 Portanto, eis que virão dias, diz o Senhor, em que já não se chamará Tofete, nem vale do filho de Hinom, mas o vale da Matança; os mortos serão enterrados em Tofete por não haver outro lugar.
33 Os cadáveres deste povo servirão de pasto às aves dos céus e aos animais da terra; e ninguém haverá que os espante.
34 Farei cessar nas cidades de Judá e nas ruas de Jerusalém a voz de folguedo e a de alegria, a voz de noivo e a de noiva; porque a terra se tornará em desolação.*
1 Naquele tempo, diz o Senhor, lançarão para fora das suas sepulturas os ossos dos reis e dos príncipes de Judá, os ossos dos sacerdotes e dos profetas e os ossos dos habitantes de Jerusalém;
2 espalhá-los-ão ao sol, e à lua, e a todo o exército do céu, a quem tinham amado, e a quem serviram, e após quem tinham ido, e a quem procuraram, e diante de quem se tinham prostrado; não serão recolhidos, nem sepultados; serão como esterco sobre a terra.
3 Escolherão antes a morte do que a vida todos os que restarem desta raça malvada que ficar nos lugares para onde os dispersei, diz o Senhor dos Exércitos.
4 Dize-lhes mais: Assim diz o Senhor: Quando caem os homens, não se tornam a levantar? Quando alguém se desvia do caminho, não torna a voltar?
5 Por que, pois, este povo de Jerusalém se desvia, apostatando continuamente? Persiste no engano e não quer voltar.
6 Eu escutei e ouvi; não falam o que é reto, ninguém há que se arrependa da sua maldade, dizendo: Que fiz eu? Cada um corre a sua carreira como um cavalo que arremete com ímpeto na batalha.
7 Até a cegonha no céu conhece as suas estações; a rola, a andorinha e o grou observam o tempo da sua arribação; mas o meu povo não conhece o juízo do Senhor.
8 Como, pois, dizeis: Somos sábios, e a lei do Senhor está conosco? Pois, com efeito, a falsa pena dos escribas a converteu em mentira.
9 Os sábios serão envergonhados, aterrorizados e presos; eis que rejeitaram a palavra do Senhor; que sabedoria é essa que eles têm?
10 Portanto, darei suas mulheres a outros, e os seus campos, a novos possuidores; porque, desde o menor deles até ao maior, cada um se dá à ganância, e tanto o profeta como o sacerdote usam de falsidade.
11 Curam superficialmente a ferida do meu povo, dizendo: Paz, paz; quando não há paz.
12 Serão envergonhados, porque cometem abominação sem sentir por isso vergonha; nem sabem que coisa é envergonhar-se. Portanto, cairão com os que caem; quando eu os castigar, tropeçarão, diz o Senhor.
13 Eu os consumirei de todo, diz o Senhor; não haverá uvas na vide, nem figos na figueira, e a folha já está murcha; e já lhes designei os que passarão sobre eles.
14 Por que estamos ainda assentados aqui? Reuni-vos, e entremos nas cidades fortificadas e ali pereçamos; pois o Senhor já nos decretou o perecimento e nos deu a beber água venenosa, porquanto pecamos contra o Senhor.
15 Espera-se a paz, e nada há de bom; o tempo da cura, e eis o terror.
16 Desde Dã se ouve o resfolegar dos seus cavalos; toda a terra treme à voz dos rinchos dos seus garanhões; e vêm e devoram a terra e a sua abundância, a cidade e os que habitam nela.
17 Porque eis que envio para entre vós serpentes, áspides contra as quais não há encantamento, e vos morderão, diz o Senhor.
sa da ruína do povo
18 Oh! Se eu pudesse consolar-me na minha tristeza! O meu coração desfalece dentro de mim.
19 Eis a voz do clamor da filha do meu povo de terra mui remota: Não está o Senhor em Sião? Não está nela o seu Rei? Por que me provocaram à ira com as suas imagens de escultura, com os ídolos dos estrangeiros?
20 Passou a sega, findou o verão, e nós não estamos salvos.
21 Estou quebrantado pela ferida da filha do meu povo; estou de luto; o espanto se apoderou de mim.
22 Acaso, não há bálsamo em Gileade? Ou não há lá médico? Por que, pois, não se realizou a cura da filha do meu povo?*
1 Prouvera a Deus a minha cabeça se tornasse em águas, e os meus olhos, em fonte de lágrimas! Então, choraria de dia e de noite os mortos da filha do meu povo.
2 Prouvera a Deus eu tivesse no deserto uma estalagem de caminhantes! Então, deixaria o meu povo e me apartaria dele, porque todos eles são adúlteros, são um bando de traidores;
3 curvam a língua, como se fosse o seu arco, para a mentira; fortalecem-se na terra, mas não para a verdade, porque avançam de malícia em malícia e não me conhecem, diz o Senhor.
4 Guardai-vos cada um do seu amigo e de irmão nenhum vos fieis; porque todo irmão não faz mais do que enganar, e todo amigo anda caluniando.
5 Cada um zomba do seu próximo, e não falam a verdade; ensinam a sua língua a proferir mentiras; cansam-se de praticar a iniquidade.
6 Vivem no meio da falsidade; pela falsidade recusam conhecer-me, diz o Senhor.
7 Portanto, assim diz o Senhor dos Exércitos: Eis que eu os acrisolarei e os provarei; porque de que outra maneira procederia eu com a filha do meu povo?
8 Flecha mortífera é a língua deles; falam engano; com a boca fala cada um de paz com o seu companheiro, mas no seu interior lhe arma ciladas.
9 Acaso, por estas coisas não os castigaria? — diz o Senhor; ou não me vingaria eu de nação tal como esta?
10 Pelos montes levantarei choro e pranto e pelas pastagens do deserto, lamentação; porque já estão queimadas, e ninguém passa por elas; já não se ouve ali o mugido de gado; tanto as aves dos céus como os animais fugiram e se foram.
11 Farei de Jerusalém montões de ruínas, morada de chacais; e das cidades de Judá farei uma assolação, de sorte que fiquem desabitadas.
12 Quem é o homem sábio, que entenda isto, e a quem falou a boca do Senhor, homem que possa explicar por que razão pereceu a terra e se queimou como deserto, de sorte que ninguém passa por ela?
13 Respondeu o Senhor: Porque deixaram a minha lei, que pus perante eles, e não deram ouvidos ao que eu disse, nem andaram nela.
14 Antes, andaram na dureza do seu coração e seguiram os baalins, como lhes ensinaram os seus pais.
15 Portanto, assim diz o Senhor dos Exércitos, Deus de Israel: Eis que alimentarei este povo com absinto e lhe darei a beber água venenosa.
16 Espalhá-los-ei entre nações que nem eles nem seus pais conheceram; e enviarei a espada após eles, até que eu venha a consumi-los.
17 Assim diz o Senhor dos Exércitos: Considerai e chamai carpideiras, para que venham; mandai procurar mulheres hábeis, para que venham.
18 Apressem-se e levantem sobre nós o seu lamento, para que os nossos olhos se desfaçam em lágrimas, e as nossas pálpebras destilem água.
19 Porque uma voz de pranto se ouve de Sião: Como estamos arruinados! Estamos sobremodo envergonhados, porque deixamos a terra, e eles transtornaram as nossas moradas.
20 Ouvi, pois, vós, mulheres, a palavra do Senhor, e os vossos ouvidos recebam a palavra da sua boca; ensinai o pranto a vossas filhas; e, cada uma à sua companheira, a lamentação.
21 Porque a morte subiu pelas nossas janelas e entrou em nossos palácios; exterminou das ruas as crianças e os jovens, das praças.
22 Fala: Assim diz o Senhor: Os cadáveres dos homens jazerão como esterco sobre o campo e cairão como gavela atrás do segador, e não há quem a recolha.
23 Assim diz o Senhor: Não se glorie o sábio na sua sabedoria, nem o forte, na sua força, nem o rico, nas suas riquezas;
24 mas o que se gloriar, glorie-se nisto: em me conhecer e saber que eu sou o Senhor e faço misericórdia, juízo e justiça na terra; porque destas coisas me agrado, diz o Senhor.
25 Eis que vêm dias, diz o Senhor, em que castigarei a todos os circuncidados juntamente com os incircuncisos:
26 ao Egito, e a Judá, e a Edom, e aos filhos de Amom, e a Moabe, e a todos os que cortam os cabelos nas têmporas e habitam no deserto; porque todas as nações são incircuncisas, e toda a casa de Israel é incircuncisa de coração.*
1 Ouvi a palavra que o Senhor vos fala a vós outros, ó casa de Israel.
2 Assim diz o Senhor: Não aprendais o caminho dos gentios, nem vos espanteis com os sinais dos céus, porque com eles os gentios se atemorizam.
3 Porque os costumes dos povos são vaidade; pois cortam do bosque um madeiro, obra das mãos do artífice, com machado;
4 com prata e ouro o enfeitam, com pregos e martelos o fixam, para que não oscile.
5 Os ídolos são como um espantalho em pepinal e não podem falar; necessitam de quem os leve, porquanto não podem andar. Não tenhais receio deles, pois não podem fazer mal, e não está neles o fazer o bem.
6 Ninguém há semelhante a ti, ó Senhor; tu és grande, e grande é o poder do teu nome.
7 Quem te não temeria a ti, ó Rei das nações? Pois isto é a ti devido; porquanto, entre todos os sábios das nações e em todo o seu reino, ninguém há semelhante a ti.
8 Mas eles todos se tornaram estúpidos e loucos; seu ensino é vão e morto como um pedaço de madeira.
9 Traz-se prata batida de Társis e ouro de Ufaz; os ídolos são obra de artífice e de mãos de ourives; azuis e púrpuras são as suas vestes; todos eles são obra de homens hábeis.
10 Mas o Senhor é verdadeiramente Deus; ele é o Deus vivo e o Rei eterno; do seu furor treme a terra, e as nações não podem suportar a sua indignação.
11 Assim lhes direis: Os deuses que não fizeram os céus e a terra desaparecerão da terra e de debaixo destes céus.
12 O Senhor fez a terra pelo seu poder; estabeleceu o mundo por sua sabedoria e com a sua inteligência estendeu os céus.
13 Fazendo ele ribombar o trovão, logo há tumulto de águas no céu, e sobem os vapores das extremidades da terra; ele cria os relâmpagos para a chuva e dos seus depósitos faz sair o vento.
14 Todo homem se tornou estúpido e não tem saber; todo ourives é envergonhado pela imagem que ele mesmo esculpiu; pois as suas imagens são mentira, e nelas não há fôlego.
15 Vaidade são, obra ridícula; no tempo do seu castigo, virão a perecer.
16 Não é semelhante a estas Aquele que é a Porção de Jacó; porque ele é o Criador de todas as coisas, e Israel é a tribo da sua herança; Senhor dos Exércitos é o seu nome.
17 Tira do chão a tua trouxa, ó filha de Sião, que moras em lugar sitiado.
18 Porque assim diz o Senhor: Eis que desta vez arrojarei para fora os moradores da terra e os angustiarei, para que venham a senti-lo.
19 Ai de mim, por causa da minha ruína! É mui grave a minha ferida; então, eu disse: com efeito, é isto o meu sofrimento, e tenho de suportá-lo.
20 A minha tenda foi destruída, todas as cordas se romperam; os meus filhos se foram e já não existem; ninguém há que levante a minha tenda e lhe erga as lonas.
21 Porque os pastores se tornaram estúpidos e não buscaram ao Senhor; por isso, não prosperaram, e todos os seus rebanhos se acham dispersos.
22 Eis aí um rumor! Eis que vem grande tumulto da terra do Norte, para fazer das cidades de Judá uma assolação, morada de chacais.
23 Eu sei, ó Senhor, que não cabe ao homem determinar o seu caminho, nem ao que caminha o dirigir os seus passos.
24 Castiga-me, ó Senhor, mas em justa medida, não na tua ira, para que não me reduzas a nada.
25 Derrama a tua indignação sobre as nações que não te conhecem e sobre os povos que não invocam o teu nome; porque devoraram a Jacó, devoraram-no, consumiram-no e assolaram a sua morada.*
1 Palavra que veio a Jeremias, da parte do Senhor, dizendo:
2 Ouve as palavras desta aliança e fala aos homens de Judá e aos habitantes de Jerusalém;
3 dize-lhes: Assim diz o Senhor, o Deus de Israel: Maldito o homem que não atentar para as palavras desta aliança,
4 que ordenei a vossos pais, no dia em que os tirei da terra do Egito, da fornalha de ferro, dizendo: dai ouvidos à minha voz e fazei tudo segundo o que vos mando; assim, vós me sereis a mim por povo, e eu vos serei a vós outros por Deus;
5 para que confirme o juramento que fiz a vossos pais de lhes dar uma terra que manasse leite e mel, como se vê neste dia. Então, eu respondi e disse: amém, ó Senhor!
6 Tornou-me o Senhor: Apregoa todas estas palavras nas cidades de Judá e nas ruas de Jerusalém, dizendo: Ouvi as palavras desta aliança e cumpri-as.
7 Porque, deveras, adverti a vossos pais, no dia em que os tirei da terra do Egito, até ao dia de hoje, testemunhando desde cedo cada dia, dizendo: dai ouvidos à minha voz.
8 Mas não atenderam, nem inclinaram o seu ouvido; antes, andaram, cada um, segundo a dureza do seu coração maligno; pelo que fiz cair sobre eles todas as ameaças desta aliança, a qual lhes ordenei que cumprissem, mas não cumpriram.
9 Disse-me ainda o Senhor: Uma conspiração se achou entre os homens de Judá, entre os habitantes de Jerusalém.
10 Tornaram às maldades de seus primeiros pais, que recusaram ouvir as minhas palavras; andaram eles após outros deuses para os servir; a casa de Israel e a casa de Judá violaram a minha aliança, que eu fizera com seus pais.
11 Portanto, assim diz o Senhor: Eis que trarei mal sobre eles, de que não poderão escapar; clamarão a mim, porém não os ouvirei.
12 Então, as cidades de Judá e os habitantes de Jerusalém irão aos deuses a quem eles queimaram incenso e a eles clamarão; porém estes, de nenhuma sorte, os livrarão do tempo do seu mal.
13 Porque, ó Judá, segundo o número das tuas cidades, são os teus deuses; segundo o número das ruas de Jerusalém, levantaste altares para vergonhosa coisa, isto é, para queimares incenso a Baal.
14 Tu, pois, não ores por este povo, nem levantes por eles clamor nem oração; porque não os ouvirei quando eles clamarem a mim, por causa do seu mal.
15 Que direito tem na minha casa a minha amada, ela que cometeu vilezas? Acaso, ó amada, votos e carnes sacrificadas poderão afastar de ti o mal? Então, saltarias de prazer.
16 O Senhor te chamou de oliveira verde, formosa por seus deliciosos frutos; mas agora, à voz de grande tumulto, acendeu fogo ao redor dela e consumiu os seus ramos.
17 Porque o Senhor dos Exércitos, que te plantou, pronunciou contra ti o mal, pela maldade que a casa de Israel e a casa de Judá para si mesmas fizeram, pois me provocaram à ira, queimando incenso a Baal.
18 O Senhor mo fez saber, e eu o soube; então, me fizeste ver as suas maquinações.
19 Eu era como manso cordeiro, que é levado ao matadouro; porque eu não sabia que tramavam projetos contra mim, dizendo: Destruamos a árvore com seu fruto; a ele cortemo-lo da terra dos viventes, e não haja mais memória do seu nome.
20 Mas, ó Senhor dos Exércitos, justo Juiz, que provas o mais íntimo do coração, veja eu a tua vingança sobre eles; pois a ti revelei a minha causa.
21 Portanto, assim diz o Senhor acerca dos homens de Anatote que procuram a tua morte e dizem: Não profetizes em o nome do Senhor, para que não morras às nossas mãos.
22 Sim, assim diz o Senhor dos Exércitos: Eis que eu os punirei; os jovens morrerão à espada, os seus filhos e as suas filhas morrerão de fome.
23 E não haverá deles resto nenhum, porque farei vir o mal sobre os homens de Anatote, no ano da sua punição.*
1 Justo és, ó Senhor, quando entro contigo num pleito; contudo, falarei contigo dos teus juízos. Por que prospera o caminho dos perversos, e vivem em paz todos os que procedem perfidamente?
2 Plantaste-os, e eles deitaram raízes; crescem, dão fruto; têm-te nos lábios, mas longe do coração.
3 Mas tu, ó Senhor, me conheces, tu me vês e provas o que sente o meu coração para contigo. Arranca-os como as ovelhas para o matadouro e destina-os para o dia da matança.
4 Até quando estará de luto a terra, e se secará a erva de todo o campo? Por causa da maldade dos que habitam nela, perecem os animais e as aves; porquanto dizem: Ele não verá o nosso fim.
5 Se te fatigas correndo com homens que vão a pé, como poderás competir com os que vão a cavalo? Se em terra de paz não te sentes seguro, que farás na floresta do Jordão?
6 Porque até os teus irmãos e a casa de teu pai, eles próprios procedem perfidamente contigo; eles mesmos te perseguem com fortes gritos. Não te fies deles ainda que te digam coisas boas.
7 Desamparei a minha casa, abandonei a minha herança; a que mais eu amava entreguei na mão de seus inimigos.
8 A minha herança tornou-se-me como leão numa floresta; levantou a voz contra mim; por isso, eu a aborreci.
9 Acaso, é para mim a minha herança ave de rapina de várias cores contra a qual se ajuntam outras aves de rapina? Ide, pois, ajuntai todos os animais do campo, trazei-os para a devorarem.
10 Muitos pastores destruíram a minha vinha e pisaram o meu quinhão; a porção que era o meu prazer, tornaram-na em deserto.
11 Em assolação a tornaram, e a mim clama no seu abandono; toda a terra está devastada, porque ninguém há que tome isso a peito.
12 Sobre todos os altos desnudos do deserto vieram destruidores; porque a espada do Senhor devora de um a outro extremo da terra; não há paz para ninguém.
13 Semearam trigo e segaram espinhos; cansaram-se, mas sem proveito algum. Envergonhados sereis dos vossos frutos, por causa do brasume da ira do Senhor.
14 Assim diz o Senhor acerca de todos os meus maus vizinhos, que se apoderam da minha herança, que deixei ao meu povo de Israel: Eis que os arrancarei da sua terra e a casa de Judá arrancarei do meio deles.
15 E será que, depois de os haver arrancado, tornarei a compadecer-me deles e os farei voltar, cada um à sua herança, cada um à sua terra.
16 Se diligentemente aprenderem os caminhos do meu povo, jurando pelo meu nome: Tão certo como vive o Senhor, como ensinaram o meu povo a jurar por Baal, então, serão edificados no meio do meu povo.
17 Mas, se não quiserem ouvir, arrancarei tal nação, arrancá-la-ei e a farei perecer, diz o Senhor.*
1 Assim me disse o Senhor: Vai, compra um cinto de linho e põe-no sobre os lombos, mas não o metas na água.
2 Comprei o cinto, segundo a palavra do Senhor, e o pus sobre os lombos.
3 Então, pela segunda vez me veio a palavra do Senhor, dizendo:
4 Toma o cinto que compraste e que tens sobre os lombos; dispõe-te, vai ao Eufrates e esconde-o ali na fenda de uma rocha.
5 Fui e escondi-o junto ao Eufrates, como o Senhor me havia ordenado.
6 Passados muitos dias, disse-me o Senhor: Dispõe-te, vai ao Eufrates e toma o cinto que te ordenei escondesses ali.
7 Fui ao Eufrates, cavei e tomei o cinto do lugar onde o escondera; eis que o cinto se tinha apodrecido e para nada prestava.
8 Então, me veio a palavra do Senhor, dizendo:
9 Assim diz o Senhor: Deste modo farei também apodrecer a soberba de Judá e a muita soberba de Jerusalém.
10 Este povo maligno, que se recusa a ouvir as minhas palavras, que caminha segundo a dureza do seu coração e anda após outros deuses para os servir e adorar, será tal como este cinto, que para nada presta.
11 Porque, como o cinto se apega aos lombos do homem, assim eu fiz apegar-se a mim toda a casa de Israel e toda a casa de Judá, diz o Senhor, para me serem por povo, e nome, e louvor, e glória; mas não deram ouvidos.
12 Pelo que dize-lhes esta palavra: Assim diz o Senhor, Deus de Israel: Todo jarro se encherá de vinho; e dir-te-ão: Não sabemos nós muito bem que todo jarro se encherá de vinho?
13 Mas tu dize-lhes: Assim diz o Senhor: Eis que eu encherei de embriaguez a todos os habitantes desta terra, e aos reis que se assentam no trono de Davi, e aos sacerdotes, e aos profetas, e a todos os habitantes de Jerusalém.
14 Fá-los-ei em pedaços, atirando uns contra os outros, tanto os pais como os filhos, diz o Senhor; não pouparei, não terei pena, nem terei deles compaixão, para que os não destrua.
15 Ouvi e atentai: não vos ensoberbeçais; porque o Senhor falou.
16 Dai glória ao Senhor, vosso Deus, antes que ele faça vir as trevas, e antes que tropecem vossos pés nos montes tenebrosos; antes que, esperando vós luz, ele a mude em sombra de morte e a reduza à escuridão.
17 Mas, se isto não ouvirdes, a minha alma chorará em segredo por causa da vossa soberba; chorarão os meus olhos amargamente e se desfarão em lágrimas, porquanto o rebanho do Senhor foi levado cativo.
18 Dize ao rei e à rainha-mãe: Humilhai-vos, assentai-vos no chão; porque caiu da vossa cabeça a coroa da vossa glória.
19 As cidades do Sul estão fechadas, e ninguém há que as abra; todo o Judá foi levado para o exílio, todos cativos.
20 Levantai os olhos e vede os que vêm do Norte; onde está o rebanho que te foi confiado, o teu lindo rebanho?
21 Que dirás, quando ele puser por cabeça contra ti aqueles a quem ensinaste a ser amigos? Acaso, não se apoderarão de ti as dores, como à mulher que está de parto?
22 Quando disseres contigo mesmo: Por que me sobrevieram estas coisas? Então, sabe que pela multidão das tuas maldades se levantaram as tuas fraldas, e os teus calcanhares sofrem violência.
23 Pode, acaso, o etíope mudar a sua pele ou o leopardo, as suas manchas? Então, poderíeis fazer o bem, estando acostumados a fazer o mal.
24 Pelo que os espalharei como o restolho, restolho que é arrebatado pelo vento do deserto.
25 Esta será a tua sorte, a porção que te será medida por mim, diz o Senhor; pois te esqueceste de mim e confiaste em mentiras.
26 Assim, também levantarei as tuas fraldas sobre o teu rosto; e aparecerão as tuas vergonhas.
27 Tenho visto as tuas abominações sobre os outeiros e no campo, a saber, os teus adultérios, os teus rinchos e a luxúria da tua prostituição. Ai de ti, Jerusalém! Até quando ainda não te purificarás?*
1 Palavra do Senhor que veio a Jeremias a respeito da grande seca.
2 Anda chorando Judá, as suas portas estão abandonadas e, de luto, se curvam até ao chão; e o clamor de Jerusalém vai subindo.
3 Os seus poderosos enviam os criados a buscar água; estes vão às cisternas e não acham água; voltam com seus cântaros vazios e, decepcionados e confusos, cobrem a cabeça.
4 Por não ter havido chuva sobre a terra, esta se acha deprimida; e, por isso, os lavradores, decepcionados, cobrem a cabeça.
5 Até as cervas no campo têm as suas crias e as abandonam, porquanto não há erva.
6 Os jumentos selvagens se põem nos desnudos altos e, ofegantes, sorvem o ar como chacais; os seus olhos desfalecem, porque não há erva.
7 Posto que as nossas maldades testificam contra nós, ó Senhor, age por amor do teu nome; porque as nossas rebeldias se multiplicaram; contra ti pecamos.
8 Ó Esperança de Israel e Redentor seu no tempo da angústia, por que serias como estrangeiro na terra e como viandante que se desvia para passar a noite?
9 Por que serias como homem surpreendido, como valente que não pode salvar? Mas tu, ó Senhor, estás em nosso meio, e somos chamados pelo teu nome; não nos desampares.
10 Assim diz o Senhor sobre este povo: Gostam de andar errantes e não detêm os pés; por isso, o Senhor não se agrada deles, mas se lembrará da maldade deles e lhes punirá o pecado.
11 Disse-me ainda o Senhor: Não rogues por este povo para o bem dele.
12 Quando jejuarem, não ouvirei o seu clamor e, quando trouxerem holocaustos e ofertas de manjares, não me agradarei deles; antes, eu os consumirei pela espada, pela fome e pela peste.
13 Então, disse eu: Ah! Senhor Deus, eis que os profetas lhes dizem: Não vereis espada, nem tereis fome; mas vos darei verdadeira paz neste lugar.
14 Disse-me o Senhor: Os profetas profetizam mentiras em meu nome, nunca os enviei, nem lhes dei ordem, nem lhes falei; visão falsa, adivinhação, vaidade e o engano do seu íntimo são o que eles vos profetizam.
15 Portanto, assim diz o Senhor acerca dos profetas que, profetizando em meu nome, sem que eu os tenha mandado, dizem que nem espada, nem fome haverá nesta terra: À espada e à fome serão consumidos esses profetas.
16 O povo a quem eles profetizam será lançado nas ruas de Jerusalém, por causa da fome e da espada; não haverá quem os sepulte, a ele, a suas mulheres, a seus filhos e a suas filhas; porque derramarei sobre eles a sua maldade.
17 Portanto, lhes dirás esta palavra: Os meus olhos derramem lágrimas, de noite e de dia, e não cessem; porque a virgem, filha do meu povo, está profundamente golpeada, de ferida mui dolorosa.
18 Se eu saio ao campo, eis aí os mortos à espada; se entro na cidade, estão ali os debilitados pela fome; até os profetas e os sacerdotes vagueiam pela terra e não sabem para onde vão.
19 Acaso, já de todo rejeitaste a Judá? Ou aborrece a tua alma a Sião? Por que nos feriste, e não há cura para nós? Aguardamos a paz, e nada há de bom; o tempo da cura, e eis o terror.
20 Conhecemos, ó Senhor, a nossa maldade e a iniquidade de nossos pais; porque temos pecado contra ti.
21 Não nos rejeites, por amor do teu nome; não cubras de opróbrio o trono da tua glória; lembra-te e não anules a tua aliança conosco.
22 Acaso, haverá entre os ídolos dos gentios algum que faça chover? Ou podem os céus de si mesmos dar chuvas? Não és tu somente, ó Senhor, nosso Deus, o que fazes isto? Portanto, em ti esperamos, pois tu fazes todas estas coisas.*
1 Disse-me, porém, o Senhor: Ainda que Moisés e Samuel se pusessem diante de mim, meu coração não se inclinaria para este povo; lança-os de diante de mim, e saiam.
2 Quando te perguntarem: Para onde iremos? Dir-lhes-ás: Assim diz o Senhor: O que é para a morte, para a morte; o que é para a espada, para a espada; o que é para a fome, para a fome; e o que é para o cativeiro, para o cativeiro.
3 Porque os punirei com quatro sortes de castigos, diz o Senhor: com espada para matar, com cães para os arrastarem e com as aves dos céus e as feras do campo para os devorarem e destruírem.
4 Entregá-los-ei para que sejam um espetáculo horrendo para todos os reinos da terra; por causa de Manassés, filho de Ezequias, rei de Judá, por tudo quanto fez em Jerusalém.
5 Pois quem se compadeceria de ti, ó Jerusalém? Ou quem se entristeceria por ti? Ou quem se desviaria a perguntar pelo teu bem-estar?
6 Tu me rejeitaste, diz o Senhor, voltaste para trás; por isso, levantarei a mão contra ti e te destruirei; estou cansado de ter compaixão.
7 Cirandei-os com a pá nas portas da terra; desfilhei e destruí o meu povo, mas não deixaram os seus caminhos.
8 As suas viúvas se multiplicaram mais do que as areias dos mares; eu trouxe ao meio-dia um destruidor sobre a mãe de jovens; fiz cair de repente sobre ela angústia e pavor.
9 Aquela que tinha sete filhos desmaiou como para expirar a alma; pôs-se-lhe o sol quando ainda era dia; ela ficou envergonhada e confundida, e os que ficaram dela, eu os entregarei à espada, diante dos seus inimigos, diz o Senhor.
10 Ai de mim, minha mãe! Pois me deste à luz homem de rixa e homem de contendas para toda a terra! Nunca lhes emprestei com usura, nem eles me emprestaram a mim com usura; todavia, cada um deles me amaldiçoa.
11 Disse o Senhor: Na verdade, eu te fortalecerei para o bem e farei que o inimigo te dirija súplicas no tempo da calamidade e no tempo da aflição.
12 Pode alguém quebrar o ferro, o ferro do Norte, ou o bronze?
13 Os teus bens e os teus tesouros entregarei gratuitamente ao saque, por todos os teus pecados e em todos os teus territórios.
14 Levar-te-ei com os teus inimigos para a terra que não conheces; porque o fogo se acendeu em minha ira e sobre vós arderá.
15 Tu, ó Senhor, o sabes; lembra-te de mim, ampara-me e vinga-me dos meus perseguidores; não me deixes ser arrebatado, por causa da tua longanimidade; sabe que por amor de ti tenho sofrido afrontas.
16 Achadas as tuas palavras, logo as comi; as tuas palavras me foram gozo e alegria para o coração, pois pelo teu nome sou chamado, ó Senhor, Deus dos Exércitos.
17 Nunca me assentei na roda dos que se alegram, nem me regozijei; oprimido por tua mão, eu me assentei solitário, pois já estou de posse das tuas ameaças.
18 Por que dura a minha dor continuamente, e a minha ferida me dói e não admite cura? Serias tu para mim como ilusório ribeiro, como águas que enganam?
19 Portanto, assim diz o Senhor: Se tu te arrependeres, eu te farei voltar e estarás diante de mim; se apartares o precioso do vil, serás a minha boca; e eles se tornarão a ti, mas tu não passarás para o lado deles.
20 Eu te porei contra este povo como forte muro de bronze; eles pelejarão contra ti, mas não prevalecerão contra ti; porque eu sou contigo para te salvar, para te livrar deles, diz o Senhor;
21 arrebatar-te-ei das mãos dos iníquos, livrar-te-ei das garras dos violentos.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Não tomarás mulher, não terás filhos nem filhas neste lugar.
3 Porque assim diz o Senhor acerca dos filhos e das filhas que nascerem neste lugar, acerca das mães que os tiverem e dos pais que os gerarem nesta terra:
4 Morrerão vitimados de enfermidades e não serão pranteados, nem sepultados; servirão de esterco para a terra. A espada e a fome os consumirão, e o seu cadáver servirá de pasto às aves do céu e aos animais da terra.
5 Porque assim diz o Senhor: Não entres na casa do luto, não vás a lamentá-los, nem te compadeças deles; porque deste povo retirei a minha paz, diz o Senhor, a benignidade e a misericórdia.
6 Nesta terra, morrerão grandes e pequenos e não serão sepultados; não os prantearão, nem se farão por eles incisões, nem por eles se raparão as cabeças.
7 Não se dará pão a quem estiver de luto, para consolá-lo por causa de morte; nem lhe darão a beber do copo de consolação, pelo pai ou pela mãe.
8 Nem entres na casa do banquete, para te assentares com eles a comer e a beber.
9 Porque assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que farei cessar neste lugar, perante vós e em vossos dias, a voz de regozijo e a voz de alegria, o canto do noivo e o da noiva.
10 Quando anunciares a este povo todas estas palavras e eles te disserem: Por que nos ameaça o Senhor com todo este grande mal? Qual é a nossa iniquidade, qual é o nosso pecado, que cometemos contra o Senhor, nosso Deus?
11 Então, lhes responderás: Porque vossos pais me deixaram, diz o Senhor, e se foram após outros deuses, e os serviram, e os adoraram, mas a mim me deixaram e a minha lei não guardaram.
12 Vós fizestes pior do que vossos pais; pois eis que cada um de vós anda segundo a dureza do seu coração maligno, para não me dar ouvidos a mim.
13 Portanto, lançar-vos-ei fora desta terra, para uma terra que não conhecestes, nem vós nem vossos pais, onde servireis a outros deuses, de dia e de noite, porque não usarei de misericórdia para convosco.
14 Portanto, eis que vêm dias, diz o Senhor, em que nunca mais se dirá: Tão certo como vive o Senhor, que fez subir os filhos de Israel do Egito;
15 mas: Tão certo como vive o Senhor, que fez subir os filhos de Israel da terra do Norte e de todas as terras para onde os tinha lançado. Pois eu os farei voltar para a sua terra, que dei a seus pais.
16 Eis que mandarei muitos pescadores, diz o Senhor, os quais os pescarão; depois, enviarei muitos caçadores, os quais os caçarão de sobre todos os montes, de sobre todos os outeiros e até nas fendas das rochas.
17 Porque os meus olhos estão sobre todos os seus caminhos; ninguém se esconde diante de mim, nem se encobre a sua iniquidade aos meus olhos.
18 Primeiramente, pagarei em dobro a sua iniquidade e o seu pecado, porque profanaram a minha terra com os cadáveres dos seus ídolos detestáveis e encheram a minha herança com as suas abominações.
19 Ó Senhor, força minha, e fortaleza minha, e refúgio meu no dia da angústia, a ti virão as nações desde os fins da terra e dirão: Nossos pais herdaram só mentiras e coisas vãs, em que não há proveito.
20 Acaso, fará o homem para si deuses que, de fato, não são deuses?
21 Portanto, eis que lhes farei conhecer, desta vez lhes farei conhecer a minha força e o meu poder; e saberão que o meu nome é Senhor.*
1 O pecado de Judá está escrito com um ponteiro de ferro e com diamante pontiagudo, gravado na tábua do seu coração e nas pontas dos seus altares.
2 Seus filhos se lembram dos seus altares e dos seus postes-ídolos junto às árvores frondosas, sobre os altos outeiros.
3 Ó monte do campo, os teus bens e todos os teus tesouros darei por presa, como também os teus altos por causa do pecado, em todos os teus territórios!
4 Assim, por ti mesmo te privarás da tua herança que te dei, e far-te-ei servir os teus inimigos, na terra que não conheces; porque o fogo que acendeste na minha ira arderá para sempre.
5 Assim diz o Senhor: Maldito o homem que confia no homem, faz da carne mortal o seu braço e aparta o seu coração do Senhor!
6 Porque será como o arbusto solitário no deserto e não verá quando vier o bem; antes, morará nos lugares secos do deserto, na terra salgada e inabitável.
7 Bendito o homem que confia no Senhor e cuja esperança é o Senhor.
8 Porque ele é como a árvore plantada junto às águas, que estende as suas raízes para o ribeiro e não receia quando vem o calor, mas a sua folha fica verde; e, no ano de sequidão, não se perturba, nem deixa de dar fruto.
9 Enganoso é o coração, mais do que todas as coisas, e desesperadamente corrupto; quem o conhecerá?
10 Eu, o Senhor, esquadrinho o coração, eu provo os pensamentos; e isto para dar a cada um segundo o seu proceder, segundo o fruto das suas ações.
11 Como a perdiz que choca ovos que não pôs, assim é aquele que ajunta riquezas, mas não retamente; no meio de seus dias, as deixará e no seu fim será insensato.
12 Trono de glória enaltecido desde o princípio é o lugar do nosso santuário.
13 Ó Senhor, Esperança de Israel! Todos aqueles que te deixam serão envergonhados; o nome dos que se apartam de mim será escrito no chão; porque abandonam o Senhor, a fonte das águas vivas.
14 Cura-me, Senhor, e serei curado, salva-me, e serei salvo; porque tu és o meu louvor.
15 Eis que eles me dizem: Onde está a palavra do Senhor? Que se cumpra!
16 Mas eu não me recusei a ser pastor, seguindo-te; nem tampouco desejei o dia da aflição, tu o sabes; o que saiu dos meus lábios está no teu conhecimento.
17 Não me sejas motivo de terror; meu refúgio és tu no dia do mal.
18 Sejam envergonhados os que me perseguem, e não seja eu envergonhado; assombrem-se eles, e não me assombre eu; traze sobre eles o dia do mal e destrói-os com dobrada destruição.
19 Assim me disse o Senhor: Vai, põe-te à porta dos filhos do povo, pela qual entram e saem os reis de Judá, como também a todas as portas de Jerusalém,
20 e dize-lhes: Ouvi a palavra do Senhor, vós, reis de Judá, e todo o Judá, e todos os moradores de Jerusalém que entrais por estas portas.
21 Assim diz o Senhor: Guardai-vos por amor da vossa alma, não carregueis cargas no dia de sábado, nem as introduzais pelas portas de Jerusalém;
22 não tireis cargas de vossa casa no dia de sábado, nem façais obra alguma; antes, santificai o dia de sábado, como ordenei a vossos pais.
23 Mas não atenderam, não inclinaram os ouvidos; antes, endureceram a cerviz, para não me ouvirem, para não receberem disciplina.
24 Se, deveras, me ouvirdes, diz o Senhor, não introduzindo cargas pelas portas desta cidade no dia de sábado, e santificardes o dia de sábado, não fazendo nele obra alguma,
25 então, pelas portas desta cidade entrarão reis e príncipes, que se assentarão no trono de Davi, andando em carros e montados em cavalos, eles e seus príncipes, os homens de Judá e os moradores de Jerusalém; e esta cidade será para sempre habitada.
26 Virão das cidades de Judá e dos contornos de Jerusalém, da terra de Benjamim, das planícies, das montanhas e do Sul, trazendo holocaustos, sacrifícios, ofertas de manjares e incenso, oferecendo igualmente sacrifícios de ações de graças na Casa do Senhor.
27 Mas, se não me ouvirdes, e, por isso, não santificardes o dia de sábado, e carregardes alguma carga, quando entrardes pelas portas de Jerusalém no dia de sábado, então, acenderei fogo nas suas portas, o qual consumirá os palácios de Jerusalém e não se apagará.*
1 Palavra do Senhor que veio a Jeremias, dizendo:
2 Dispõe-te, e desce à casa do oleiro, e lá ouvirás as minhas palavras.
3 Desci à casa do oleiro, e eis que ele estava entregue à sua obra sobre as rodas.
4 Como o vaso que o oleiro fazia de barro se lhe estragou na mão, tornou a fazer dele outro vaso, segundo bem lhe pareceu.
5 Então, veio a mim a palavra do Senhor:
6 Não poderei eu fazer de vós como fez este oleiro, ó casa de Israel? — diz o Senhor; eis que, como o barro na mão do oleiro, assim sois vós na minha mão, ó casa de Israel.
7 No momento em que eu falar acerca de uma nação ou de um reino para o arrancar, derribar e destruir,
8 se a tal nação se converter da maldade contra a qual eu falei, também eu me arrependerei do mal que pensava fazer-lhe.
9 E, no momento em que eu falar acerca de uma nação ou de um reino, para o edificar e plantar,
10 se ele fizer o que é mau perante mim e não der ouvidos à minha voz, então, me arrependerei do bem que houvera dito lhe faria.
11 Ora, pois, fala agora aos homens de Judá e aos moradores de Jerusalém, dizendo: Assim diz o Senhor: Eis que estou forjando mal e formo um plano contra vós outros; convertei-vos, pois, agora, cada um do seu mau proceder e emendai os vossos caminhos e as vossas ações.
12 Mas eles dizem: Não há esperança, porque andaremos consoante os nossos projetos, e cada um fará segundo a dureza do seu coração maligno.
13 Portanto, assim diz o Senhor: Perguntai agora entre os gentios sobre quem ouviu tal coisa. Coisa sobremaneira horrenda cometeu a virgem de Israel!
14 Acaso, a neve deixará o Líbano, a rocha que se ergue na planície? Ou faltarão as águas que vêm de longe, frias e correntes?
15 Contudo, todos os do meu povo se têm esquecido de mim, queimando incenso aos ídolos, que os fizeram tropeçar nos seus caminhos e nas veredas antigas, para que andassem por veredas não aterradas;
16 para fazerem da sua terra um espanto e objeto de perpétuo assobio; todo aquele que passar por ela se espantará e meneará a cabeça.
17 Com vento oriental os espalharei diante do inimigo; mostrar-lhes-ei as costas e não o rosto, no dia da sua calamidade.
18 Então, disseram: Vinde, e forjemos projetos contra Jeremias; porquanto não há de faltar a lei ao sacerdote, nem o conselho ao sábio, nem a palavra ao profeta; vinde, firamo-lo com a língua e não atendamos a nenhuma das suas palavras.
19 Olha para mim, Senhor, e ouve a voz dos que contendem comigo.
20 Acaso, pagar-se-á mal por bem? Pois abriram uma cova para a minha alma. Lembra-te de que eu compareci à tua presença, para interceder pelo seu bem-estar, para desviar deles a tua indignação.
21 Portanto, entrega seus filhos à fome e ao poder da espada; sejam suas mulheres roubadas dos filhos e fiquem viúvas; seus maridos sejam mortos de peste, e os seus jovens, feridos à espada na peleja.
22 Ouça-se o clamor de suas casas, quando trouxeres bandos sobre eles de repente. Porquanto abriram cova para prender-me e puseram armadilha aos meus pés.
23 Mas tu, ó Senhor, sabes todo o seu conselho contra mim para matar-me; não lhes perdoes a iniquidade, nem lhes apagues o pecado de diante da tua face; mas sejam derribados diante de ti; age contra eles no tempo da tua ira.*
1 Assim diz o Senhor: Vai, compra uma botija de oleiro e leva contigo alguns dos anciãos do povo e dos anciãos dos sacerdotes;
2 sai ao vale do filho de Hinom, que está à entrada da Porta do Oleiro, e apregoa ali as palavras que eu te disser;
3 e dize: Ouvi a palavra do Senhor, ó reis de Judá e moradores de Jerusalém. Assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que trarei mal sobre este lugar, e quem quer que dele ouvir retinir-lhe-ão os ouvidos.
4 Porquanto me deixaram e profanaram este lugar, queimando nele incenso a outros deuses, que nunca conheceram, nem eles, nem seus pais, nem os reis de Judá; e encheram este lugar de sangue de inocentes;
5 e edificaram os altos de Baal, para queimarem os seus filhos no fogo em holocaustos a Baal, o que nunca lhes ordenei, nem falei, nem me passou pela mente.
6 Por isso, eis que vêm dias, diz o Senhor, em que este lugar já não se chamará Tofete, nem vale do filho de Hinom, mas o vale da Matança.
7 Porque dissiparei o conselho de Judá e de Jerusalém neste lugar e os farei cair à espada diante de seus inimigos e pela mão dos que procuram tirar-lhes a vida; e darei o seu cadáver por pasto às aves dos céus e aos animais da terra.
8 Porei esta cidade por espanto e objeto de assobios; todo aquele que passar por ela se espantará e assobiará, por causa de todas as suas pragas.
9 Fá-los-ei comer as carnes de seus filhos e as carnes de suas filhas, e cada um comerá a carne do seu próximo, no cerco e na angústia em que os apertarão os seus inimigos e os que buscam tirar-lhes a vida.
10 Então, quebrarás a botija à vista dos homens que foram contigo
11 e lhes dirás: Assim diz o Senhor dos Exércitos: Deste modo quebrarei eu este povo e esta cidade, como se quebra o vaso do oleiro, que não pode mais refazer-se, e os enterrarão em Tofete, porque não haverá outro lugar para os enterrar.
12 Assim farei a este lugar, diz o Senhor, e aos seus moradores; e farei desta cidade um Tofete.
13 As casas de Jerusalém e as casas dos reis de Judá serão imundas como o lugar de Tofete; também todas as casas sobre cujos terraços queimaram incenso a todo o exército dos céus e ofereceram libações a outros deuses.
14 Voltando, pois, Jeremias de Tofete, lugar para onde o enviara o Senhor a profetizar, se pôs em pé no átrio da Casa do Senhor e disse a todo o povo:
15 Assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que trarei sobre esta cidade e sobre todas as suas vilas todo o mal que pronunciei contra ela, porque endureceram a cerviz, para não ouvirem as minhas palavras.*
1 Pasur, filho do sacerdote Imer, que era presidente na Casa do Senhor, ouviu a Jeremias profetizando estas coisas.
2 Então, feriu Pasur ao profeta Jeremias e o meteu no tronco que estava na porta superior de Benjamim, na Casa do Senhor. No dia seguinte, Pasur tirou a Jeremias do tronco.
3 Então, lhe disse Jeremias: O Senhor já não te chama Pasur, e sim Terror-Por-Todos-Os-Lados.
4 Pois assim diz o Senhor: Eis que te farei ser terror para ti mesmo e para todos os teus amigos; estes cairão à espada de seus inimigos, e teus olhos o verão; todo o Judá entregarei nas mãos do rei da Babilônia; este os levará presos à Babilônia e feri-los-á à espada.
5 Também entregarei toda a riqueza desta cidade, todo o fruto do seu trabalho e todas as suas coisas preciosas; sim, todos os tesouros dos reis de Judá entregarei nas mãos de seus inimigos, os quais hão de saqueá-los, tomá-los e levá-los à Babilônia.
6 E tu, Pasur, e todos os moradores da tua casa ireis para o cativeiro; irás à Babilônia, onde morrerás e serás sepultado, tu e todos os teus amigos, aos quais profetizaste falsamente.
 7 Persuadiste-me, ó Senhor, e persuadido fiquei; mais forte foste do que eu e prevaleceste; sirvo de escárnio todo o dia; cada um deles zomba de mim.
8 Porque, sempre que falo, tenho de gritar e clamar: Violência e destruição! Porque a palavra do Senhor se me tornou um opróbrio e ludíbrio todo o dia.
9 Quando pensei: não me lembrarei dele e já não falarei no seu nome, então, isso me foi no coração como fogo ardente, encerrado nos meus ossos; já desfaleço de sofrer e não posso mais.
10 Porque ouvi a murmuração de muitos: Há terror por todos os lados! Denunciai, e o denunciaremos! Todos os meus íntimos amigos que aguardam de mim que eu tropece dizem: Bem pode ser que se deixe persuadir; então, prevaleceremos contra ele e dele nos vingaremos.
11 Mas o Senhor está comigo como um poderoso guerreiro; por isso, tropeçarão os meus perseguidores e não prevalecerão; serão sobremodo envergonhados; e, porque não se houveram sabiamente, sofrerão afronta perpétua, que jamais se esquecerá.
12 Tu, pois, ó Senhor dos Exércitos, que provas o justo e esquadrinhas os afetos e o coração, permite veja eu a tua vingança contra eles, pois te confiei a minha causa.
13 Cantai ao Senhor, louvai ao Senhor; pois livrou a alma do necessitado das mãos dos malfeitores.
14 Maldito o dia em que nasci! Não seja bendito o dia em que me deu à luz minha mãe!
15 Maldito o homem que deu as novas a meu pai, dizendo: Nasceu-te um filho!, alegrando-o com isso grandemente.
16 Seja esse homem como as cidades que o Senhor, sem ter compaixão, destruiu; ouça ele clamor pela manhã e ao meio-dia, alarido.
17 Por que não me matou Deus no ventre materno? Por que minha mãe não foi minha sepultura? Ou não permaneceu grávida perpetuamente?
18 Por que saí do ventre materno tão somente para ver trabalho e tristeza e para que se consumam de vergonha os meus dias?*
1 Palavra que veio a Jeremias da parte do Senhor, quando o rei Zedequias lhe enviou Pasur, filho de Malquias, e o sacerdote Sofonias, filho de Maaseias, dizendo:
2 Pergunta agora por nós ao Senhor, por que Nabucodonosor, rei da Babilônia, guerreia contra nós; bem pode ser que o Senhor nos trate segundo todas as suas maravilhas e o faça retirar-se de nós.
3 Então, Jeremias lhes disse: Assim direis a Zedequias:
4 Assim diz o Senhor, o Deus de Israel: Eis que farei retroceder as armas de guerra que estão nas vossas mãos, com que vós pelejais fora dos muros contra o rei da Babilônia e contra os caldeus, que vos oprimem; tais armas, eu as ajuntarei no meio desta cidade.
5 Pelejarei eu mesmo contra vós outros com braço estendido e mão poderosa, com ira, com indignação e grande furor.
6 Ferirei os habitantes desta cidade, tanto os homens como os animais; de grande pestilência morrerão.
7 Depois disto, diz o Senhor, entregarei Zedequias, rei de Judá, e seus servos, e o povo, e quantos desta cidade restarem da pestilência, da espada e da fome na mão de Nabucodonosor, rei da Babilônia, na de seus inimigos e na dos que procuram tirar-lhes a vida; feri-los-á a fio de espada; não os poupará, não se compadecerá, nem terá misericórdia.
8 A este povo dirás: Assim diz o Senhor: Eis que ponho diante de vós o caminho da vida e o caminho da morte.
9 O que ficar nesta cidade há de morrer à espada, ou à fome, ou de peste; mas o que sair e render-se aos caldeus, que vos cercam, viverá, e a vida lhe será como despojo.
10 Pois voltei o rosto contra esta cidade, para mal e não para bem, diz o Senhor; ela será entregue nas mãos do rei da Babilônia, e este a queimará.
11 À casa do rei de Judá dirás: Ouvi a palavra do Senhor!
12 Ó casa de Davi, assim diz o Senhor: Julgai pela manhã justamente e livrai o oprimido das mãos do opressor; para que não seja o meu furor como fogo e se acenda, sem que haja quem o apague, por causa da maldade das vossas ações.
13 Eis que eu sou contra ti, ó Moradora do vale, ó Rocha da campina, diz o Senhor; contra vós outros que dizeis: Quem descerá contra nós? Ou: Quem entrará nas nossas moradas?
14 Castigar-vos-ei segundo o fruto das vossas ações, diz o Senhor; acenderei fogo na cidade, qual bosque, o qual devorará todos os seus arredores.*
1 Assim diz o Senhor: Desce à casa do rei de Judá, e anuncia ali esta palavra,
2 e dize: Ouve a palavra do Senhor, ó rei de Judá, que te assentas no trono de Davi, tu, os teus servos e o teu povo, que entrais por estas portas.
3 Assim diz o Senhor: Executai o direito e a justiça e livrai o oprimido das mãos do opressor; não oprimais ao estrangeiro, nem ao órfão, nem à viúva; não façais violência, nem derrameis sangue inocente neste lugar.
4 Porque, se, deveras, cumprirdes esta palavra, entrarão pelas portas desta casa os reis que se assentarão no trono de Davi, em carros e montados em cavalos, eles, os seus servos e o seu povo.
5 Mas, se não derdes ouvidos a estas palavras, juro por mim mesmo, diz o Senhor, que esta casa se tornará em desolação.
6 Porque assim diz o Senhor acerca da casa do rei de Judá: Tu és para mim Gileade e a cabeça do Líbano; mas certamente farei de ti um deserto e cidades desabitadas.
7 Designarei contra ti destruidores, cada um com as suas armas; cortarão os teus cedros escolhidos e lançá-los-ão no fogo.
8 Muitas nações passarão por esta cidade, e dirá cada um ao seu companheiro: Por que procedeu o Senhor assim com esta grande cidade?
9 Então, se lhes responderá: Porque deixaram a aliança do Senhor, seu Deus, e adoraram a outros deuses, e os serviram.
10 Não choreis o morto, nem o lastimeis; chorai amargamente aquele que sai; porque nunca mais tornará, nem verá a terra onde nasceu.
11 Porque assim diz o Senhor acerca de Salum, filho de Josias, rei de Judá, que reinou em lugar de Josias, seu pai, e que saiu deste lugar: Jamais tornará para ali.
12 Mas no lugar para onde o levaram cativo morrerá e nunca mais verá esta terra.
13 Ai daquele que edifica a sua casa com injustiça e os seus aposentos, sem direito! Que se vale do serviço do seu próximo, sem paga, e não lhe dá o salário;
14 que diz: Edificarei para mim casa espaçosa e largos aposentos, e lhe abre janelas, e forra-a de cedros, e a pinta de vermelhão.
15 Reinarás tu, só porque rivalizas com outro em cedro? Acaso, teu pai não comeu, e bebeu, e não exercitou o juízo e a justiça? Por isso, tudo lhe sucedeu bem.
16 Julgou a causa do aflito e do necessitado; por isso, tudo lhe ia bem. Porventura, não é isso conhecer-me? — diz o Senhor.
17 Mas os teus olhos e o teu coração não atentam senão para a tua ganância, e para derramar o sangue inocente, e para levar a efeito a violência e a extorsão.
18 Portanto, assim diz o Senhor acerca de Jeoaquim, filho de Josias, rei de Judá: Não o lamentarão, dizendo: Ai, meu irmão! Ou: Ai, minha irmã! Nem o lamentarão, dizendo: Ai, senhor! Ou: Ai, sua glória!
19 Como se sepulta um jumento, assim o sepultarão; arrastá-lo-ão e o lançarão para bem longe, para fora das portas de Jerusalém.
20 Sobe ao Líbano, ó Jerusalém, e clama; ergue a voz em Basã e clama desde Abarim, porque estão esmagados todos os teus amantes.
21 Falei contigo na tua prosperidade, mas tu disseste: Não ouvirei. Tem sido este o teu caminho, desde a tua mocidade, pois nunca deste ouvidos à minha voz.
22 O vento apascentará todos os teus pastores, e os teus amantes irão para o cativeiro; então, certamente ficarás envergonhada e confundida, por causa de toda a tua maldade.
23 Ó tu que habitas no Líbano e fazes o teu ninho nos cedros! Como gemerás quando te vierem as dores e as angústias como da que está de parto!
24 Tão certo como eu vivo, diz o Senhor, ainda que Jeconias, filho de Jeoaquim, rei de Judá, fosse o anel do selo da minha mão direita, eu dali o arrancaria.
25 Entregar-te-ei, ó rei, nas mãos dos que procuram tirar-te a vida e nas mãos daqueles a quem temes, a saber, nas mãos de Nabucodonosor, rei da Babilônia, e nas mãos dos caldeus.
26 Lançar-te-ei a ti e a tua mãe, que te deu à luz, para outra terra, em que não nasceste; e ali morrereis.
27 Mas à terra da qual eles têm saudades, a ela não tornarão.
28 Acaso, é este Jeconias homem vil, coisa quebrada ou objeto de que ninguém se agrada? Por que foram lançados fora, ele e os seus filhos, e arrojados para a terra que não conhecem?
29 Ó terra, terra, terra! Ouve a palavra do Senhor!
30 Assim diz o Senhor: Registrai este como se não tivera filhos; homem que não prosperará nos seus dias, e nenhum dos seus filhos prosperará, para se assentar no trono de Davi e ainda reinar em Judá.*
1 Ai dos pastores que destroem e dispersam as ovelhas do meu pasto! — diz o Senhor.
2 Portanto, assim diz o Senhor, o Deus de Israel, contra os pastores que apascentam o meu povo: Vós dispersastes as minhas ovelhas, e as afugentastes, e delas não cuidastes; mas eu cuidarei em vos castigar a maldade das vossas ações, diz o Senhor.
3 Eu mesmo recolherei o restante das minhas ovelhas, de todas as terras para onde as tiver afugentado, e as farei voltar aos seus apriscos; serão fecundas e se multiplicarão.
4 Levantarei sobre elas pastores que as apascentem, e elas jamais temerão, nem se espantarão; nem uma delas faltará, diz o Senhor.
5 Eis que vêm dias, diz o Senhor, em que levantarei a Davi um Renovo justo; e, rei que é, reinará, e agirá sabiamente, e executará o juízo e a justiça na terra.
6 Nos seus dias, Judá será salvo, e Israel habitará seguro; será este o seu nome, com que será chamado: Senhor, Justiça Nossa.
7 Portanto, eis que vêm dias, diz o Senhor, em que nunca mais dirão: Tão certo como vive o Senhor, que fez subir os filhos de Israel da terra do Egito;
8 mas: Tão certo como vive o Senhor, que fez subir, que trouxe a descendência da casa de Israel da terra do Norte e de todas as terras para onde os tinha arrojado; e habitarão na sua terra.
9 Acerca dos profetas. O meu coração está quebrantado dentro de mim; todos os meus ossos estremecem; sou como homem embriagado e como homem vencido pelo vinho, por causa do Senhor e por causa das suas santas palavras.
10 Porque a terra está cheia de adúlteros e chora por causa da maldição divina; os pastos do deserto se secam; pois a carreira dos adúlteros é má, e a sua força não é reta.
11 Pois estão contaminados, tanto o profeta como o sacerdote; até na minha casa achei a sua maldade, diz o Senhor.
12 Portanto, o caminho deles será como lugares escorregadios na escuridão; serão empurrados e cairão nele; porque trarei sobre eles calamidade, o ano mesmo em que os castigarei, diz o Senhor.
13 Nos profetas de Samaria bem vi eu loucura; profetizavam da parte de Baal e faziam errar o meu povo de Israel.
14 Mas nos profetas de Jerusalém vejo coisa horrenda; cometem adultérios, andam com falsidade e fortalecem as mãos dos malfeitores, para que não se convertam cada um da sua maldade; todos eles se tornaram para mim como Sodoma, e os moradores de Jerusalém, como Gomorra.
15 Portanto, assim diz o Senhor dos Exércitos acerca dos profetas: Eis que os alimentarei com absinto e lhes darei a beber água venenosa; porque dos profetas de Jerusalém se derramou a impiedade sobre toda a terra.
16 Assim diz o Senhor dos Exércitos: Não deis ouvidos às palavras dos profetas que entre vós profetizam e vos enchem de vãs esperanças; falam as visões do seu coração, não o que vem da boca do Senhor.
17 Dizem continuamente aos que me desprezam: O Senhor disse: Paz tereis; e a qualquer que anda segundo a dureza do seu coração dizem: Não virá mal sobre vós.
18 Porque quem esteve no conselho do Senhor, e viu, e ouviu a sua palavra? Quem esteve atento à sua palavra e a ela atendeu?
19 Eis a tempestade do Senhor! O furor saiu, e um redemoinho tempestuou sobre a cabeça dos perversos.
20 Não se desviará a ira do Senhor, até que ele execute e cumpra os desígnios do seu coração; nos últimos dias, entendereis isso claramente.
21 Não mandei esses profetas; todavia, eles foram correndo; não lhes falei a eles; contudo, profetizaram.
22 Mas, se tivessem estado no meu conselho, então, teriam feito ouvir as minhas palavras ao meu povo e o teriam feito voltar do seu mau caminho e da maldade das suas ações.
23 Acaso, sou Deus apenas de perto, diz o Senhor, e não também de longe?
24 Ocultar-se-ia alguém em esconderijos, de modo que eu não o veja? — diz o Senhor; porventura, não encho eu os céus e a terra? — diz o Senhor.
25 Tenho ouvido o que dizem aqueles profetas, proclamando mentiras em meu nome, dizendo: Sonhei, sonhei.
26 Até quando sucederá isso no coração dos profetas que proclamam mentiras, que proclamam só o engano do próprio coração?
27 Os quais cuidam em fazer que o meu povo se esqueça do meu nome pelos seus sonhos que cada um conta ao seu companheiro, assim como seus pais se esqueceram do meu nome, por causa de Baal.
28 O profeta que tem sonho conte-o como apenas sonho; mas aquele em quem está a minha palavra fale a minha palavra com verdade. Que tem a palha com o trigo? — diz o Senhor.
29 Não é a minha palavra fogo, diz o Senhor, e martelo que esmiúça a penha?
30 Portanto, eis que eu sou contra esses profetas, diz o Senhor, que furtam as minhas palavras, cada um ao seu companheiro.
31 Eis que eu sou contra esses profetas, diz o Senhor, que pregam a sua própria palavra e afirmam: Ele disse.
32 Eis que eu sou contra os que profetizam sonhos mentirosos, diz o Senhor, e os contam, e com as suas mentiras e leviandades fazem errar o meu povo; pois eu não os enviei, nem lhes dei ordem; e também proveito nenhum trouxeram a este povo, diz o Senhor.
33 Quando, pois, este povo te perguntar, ou qualquer profeta, ou sacerdote, dizendo: Qual é a sentença pesada do Senhor? Então, lhe dirás: Vós sois o peso, e eu vos arrojarei, diz o Senhor.
34 Quanto ao profeta, e ao sacerdote, e ao povo que disser: Sentença pesada do Senhor, a esse homem eu castigarei e a sua casa.
35 Antes, direis, cada um ao seu companheiro e cada um ao seu irmão: Que respondeu o Senhor? Que falou o Senhor?
36 Mas nunca mais fareis menção da sentença pesada do Senhor; porque a cada um lhe servirá de sentença pesada a sua própria palavra; pois torceis as palavras do Deus vivo, do Senhor dos Exércitos, o nosso Deus.
37 Assim dirás ao profeta: Que te respondeu o Senhor? Que falou o Senhor?
38 Mas, porque dizeis: Sentença pesada do Senhor, assim o diz o Senhor: Porque dizeis esta palavra: Sentença pesada do Senhor (havendo-vos eu proibido de dizerdes esta palavra: Sentença pesada do Senhor),
39 por isso, levantar-vos-ei e vos arrojarei da minha presença, a vós outros e à cidade que vos dei e a vossos pais.
40 Porei sobre vós perpétuo opróbrio e eterna vergonha, que jamais será esquecida.*
1 Fez-me ver o Senhor, e vi dois cestos de figos postos diante do templo do Senhor, depois que Nabucodonosor, rei da Babilônia, levou em cativeiro a Jeconias, filho de Jeoaquim, rei de Judá, e os príncipes de Judá, e os artífices, e os ferreiros de Jerusalém e os trouxe à Babilônia.
2 Tinha um cesto figos muito bons, como os figos temporãos; mas o outro, ruins, que, de ruins que eram, não se podiam comer.
3 Então, me perguntou o Senhor: Que vês tu, Jeremias? Respondi: Figos; os figos muito bons e os muito ruins, que, de ruins que são, não se podem comer.
4 A mim me veio a palavra do Senhor, dizendo:
5 Assim diz o Senhor, o Deus de Israel: Do modo por que vejo estes bons figos, assim favorecerei os exilados de Judá, que eu enviei deste lugar para a terra dos caldeus.
6 Porei sobre eles favoravelmente os olhos e os farei voltar para esta terra; edificá-los-ei e não os destruirei, plantá-los-ei e não os arrancarei.
7 Dar-lhes-ei coração para que me conheçam que eu sou o Senhor; eles serão o meu povo, e eu serei o seu Deus; porque se voltarão para mim de todo o seu coração.
8 Como se rejeitam os figos ruins, que, de ruins que são, não se podem comer, assim tratarei a Zedequias, rei de Judá, diz o Senhor, e a seus príncipes, e ao restante de Jerusalém, tanto aos que ficaram nesta terra como aos que habitam na terra do Egito.
9 Eu os farei objeto de espanto, calamidade para todos os reinos da terra; opróbrio e provérbio, escárnio e maldição em todos os lugares para onde os arrojarei.
10 Enviarei contra eles a espada, a fome e a peste, até que se consumam de sobre a terra que lhes dei, a eles e a seus pais.*
1 Palavra que veio a Jeremias acerca de todo o povo de Judá, no ano quarto de Jeoaquim, filho de Josias, rei de Judá, ano que era o primeiro de Nabucodonosor, rei da Babilônia,
2 a qual anunciou Jeremias, o profeta, a todo o povo de Judá e a todos os habitantes de Jerusalém, dizendo:
3 Durante vinte e três anos, desde o décimo terceiro de Josias, filho de Amom, rei de Judá, até hoje, tem vindo a mim a palavra do Senhor, e, começando de madrugada, eu vo-la tenho anunciado; mas vós não escutastes.
4 Também, começando de madrugada, vos enviou o Senhor todos os seus servos, os profetas, mas vós não os escutastes, nem inclinastes os ouvidos para ouvir,
5 quando diziam: Convertei-vos agora, cada um do seu mau caminho e da maldade das suas ações, e habitai na terra que o Senhor vos deu e a vossos pais, desde os tempos antigos e para sempre.
6 Não andeis após outros deuses para os servirdes e para os adorardes, nem me provoqueis à ira com as obras de vossas mãos; não vos farei mal algum.
7 Todavia, não me destes ouvidos, diz o Senhor, mas me provocastes à ira com as obras de vossas mãos, para o vosso próprio mal.
8 Portanto, assim diz o Senhor dos Exércitos: Visto que não escutastes as minhas palavras,
9 eis que mandarei buscar todas as tribos do Norte, diz o Senhor, como também a Nabucodonosor, rei da Babilônia, meu servo, e os trarei contra esta terra, contra os seus moradores e contra todas estas nações em redor, e os destruirei totalmente, e os porei por objeto de espanto, e de assobio, e de ruínas perpétuas.
10 Farei cessar entre eles a voz de folguedo e a de alegria, e a voz do noivo, e a da noiva, e o som das mós, e a luz do candeeiro.
11 Toda esta terra virá a ser um deserto e um espanto; estas nações servirão ao rei da Babilônia setenta anos.
12 Acontecerá, porém, que, quando se cumprirem os setenta anos, castigarei a iniquidade do rei da Babilônia e a desta nação, diz o Senhor, como também a da terra dos caldeus; farei deles ruínas perpétuas.
13 Farei que se cumpram sobre aquela terra todas as minhas ameaças que proferi contra ela, tudo quanto está escrito neste livro, que profetizou Jeremias contra todas as nações.
14 Porque também eles serão escravos de muitas nações e de grandes reis; assim, lhes retribuirei segundo os seus feitos e segundo as obras das suas mãos.
15 Porque assim me disse o Senhor, o Deus de Israel: Toma da minha mão este cálice do vinho do meu furor e darás a beber dele a todas as nações às quais eu te enviar.
16 Para que bebam, e tremam, e enlouqueçam, por causa da espada que eu enviarei para o meio delas.
17 Recebi o cálice da mão do Senhor e dei a beber a todas as nações às quais o Senhor me tinha enviado:
18 a Jerusalém, às cidades de Judá, aos seus reis e aos seus príncipes, para fazer deles uma ruína, objeto de espanto, de assobio e maldição, como hoje se vê;
19 a Faraó, rei do Egito, a seus servos, a seus príncipes e a todo o seu povo;
20 a todo misto de gente, a todos os reis da terra de Uz, a todos os reis da terra dos filisteus, a Asquelom, a Gaza, a Ecrom e ao resto de Asdode;
21 a Edom, a Moabe e aos filhos de Amom;
22 a todos os reis de Tiro, a todos os reis de Sidom e aos reis das terras dalém do mar;
23 a Dedã, a Tema, a Buz e a todos os que cortam os cabelos nas têmporas;
24 a todos os reis da Arábia e todos os reis do misto de gente que habita no deserto;
25 a todos os reis de Zinri, a todos os reis de Elão e a todos os reis da Média;
26 a todos os reis do Norte, os de perto e os de longe, um após outro, e a todos os reinos do mundo sobre a face da terra; e, depois de todos eles, ao rei da Babilônia.
27 Pois lhes dirás: Assim diz o Senhor dos Exércitos, o Deus de Israel: Bebei, embebedai-vos e vomitai; caí e não torneis a levantar-vos, por causa da espada que estou enviando para o vosso meio.
28 Se recusarem receber o cálice da tua mão para beber, então, lhes dirás: Assim diz o Senhor dos Exércitos: Tereis de bebê-lo.
29 Pois eis que na cidade que se chama pelo meu nome começo a castigar; e ficareis vós de todo impunes? Não, não ficareis impunes, porque eu chamo a espada sobre todos os moradores da terra, diz o Senhor dos Exércitos.
30 Tu, pois, lhes profetizarás todas estas palavras e lhes dirás: O Senhor lá do alto rugirá e da sua santa morada fará ouvir a sua voz; rugirá fortemente contra a sua malhada, com brados contra todos os moradores da terra, como o eia! dos que pisam as uvas.
31 Chegará o estrondo até à extremidade da terra, porque o Senhor tem contenda com as nações, entrará em juízo contra toda carne; os perversos entregará à espada, diz o Senhor.
32 Assim diz o Senhor dos Exércitos: Eis que o mal passa de nação para nação, e grande tormenta se levanta dos confins da terra.
33 Os que o Senhor entregar à morte naquele dia se estenderão de uma a outra extremidade da terra; não serão pranteados, nem recolhidos, nem sepultados; serão como esterco sobre a face da terra.
34 Uivai, pastores, e clamai; revolvei-vos na cinza, vós, donos dos rebanhos, porque já se cumpriram os vossos dias de matardes e dispersardes, e vós mesmos caireis como jarros preciosos.
35 Não haverá refúgio para os pastores, nem salvamento para os donos dos rebanhos.
36 Eis o grito dos pastores, o uivo dos donos dos rebanhos! Porque o Senhor está destruindo o pasto deles.
37 Porque as suas malhadas pacíficas serão devastadas, por causa do brasume da ira do Senhor.
38 Saiu da sua morada como o filho de leão; porque a terra deles foi posta em ruínas, por causa do furor da espada e por causa do brasume da ira do Senhor.
15 Porque assim me disse o Senhor, o Deus de Israel: Toma da minha mão este cálice do vinho do meu furor e darás a beber dele a todas as nações às quais eu te enviar.
16 Para que bebam, e tremam, e enlouqueçam, por causa da espada que eu enviarei para o meio delas.
17 Recebi o cálice da mão do Senhor e dei a beber a todas as nações às quais o Senhor me tinha enviado:
18 a Jerusalém, às cidades de Judá, aos seus reis e aos seus príncipes, para fazer deles uma ruína, objeto de espanto, de assobio e maldição, como hoje se vê;
19 a Faraó, rei do Egito, a seus servos, a seus príncipes e a todo o seu povo;
20 a todo misto de gente, a todos os reis da terra de Uz, a todos os reis da terra dos filisteus, a Asquelom, a Gaza, a Ecrom e ao resto de Asdode;
21 a Edom, a Moabe e aos filhos de Amom;
22 a todos os reis de Tiro, a todos os reis de Sidom e aos reis das terras dalém do mar;
23 a Dedã, a Tema, a Buz e a todos os que cortam os cabelos nas têmporas;
24 a todos os reis da Arábia e todos os reis do misto de gente que habita no deserto;
25 a todos os reis de Zinri, a todos os reis de Elão e a todos os reis da Média;
26 a todos os reis do Norte, os de perto e os de longe, um após outro, e a todos os reinos do mundo sobre a face da terra; e, depois de todos eles, ao rei da Babilônia.
27 Pois lhes dirás: Assim diz o Senhor dos Exércitos, o Deus de Israel: Bebei, embebedai-vos e vomitai; caí e não torneis a levantar-vos, por causa da espada que estou enviando para o vosso meio.
28 Se recusarem receber o cálice da tua mão para beber, então, lhes dirás: Assim diz o Senhor dos Exércitos: Tereis de bebê-lo.
29 Pois eis que na cidade que se chama pelo meu nome começo a castigar; e ficareis vós de todo impunes? Não, não ficareis impunes, porque eu chamo a espada sobre todos os moradores da terra, diz o Senhor dos Exércitos.
30 Tu, pois, lhes profetizarás todas estas palavras e lhes dirás: O Senhor lá do alto rugirá e da sua santa morada fará ouvir a sua voz; rugirá fortemente contra a sua malhada, com brados contra todos os moradores da terra, como o eia! dos que pisam as uvas.
31 Chegará o estrondo até à extremidade da terra, porque o Senhor tem contenda com as nações, entrará em juízo contra toda carne; os perversos entregará à espada, diz o Senhor.
32 Assim diz o Senhor dos Exércitos: Eis que o mal passa de nação para nação, e grande tormenta se levanta dos confins da terra.
33 Os que o Senhor entregar à morte naquele dia se estenderão de uma a outra extremidade da terra; não serão pranteados, nem recolhidos, nem sepultados; serão como esterco sobre a face da terra.
34 Uivai, pastores, e clamai; revolvei-vos na cinza, vós, donos dos rebanhos, porque já se cumpriram os vossos dias de matardes e dispersardes, e vós mesmos caireis como jarros preciosos.
35 Não haverá refúgio para os pastores, nem salvamento para os donos dos rebanhos.
36 Eis o grito dos pastores, o uivo dos donos dos rebanhos! Porque o Senhor está destruindo o pasto deles.
37 Porque as suas malhadas pacíficas serão devastadas, por causa do brasume da ira do Senhor.
38 Saiu da sua morada como o filho de leão; porque a terra deles foi posta em ruínas, por causa do furor da espada e por causa do brasume da ira do Senhor.*
1 No princípio do reinado de Jeoaquim, filho de Josias, rei de Judá, veio esta palavra do Senhor:
2 Assim diz o Senhor: Põe-te no átrio da Casa do Senhor e dize a todas as cidades de Judá, que vêm adorar à Casa do Senhor, todas as palavras que eu te mando lhes digas; não omitas nem uma palavra sequer.
3 Bem pode ser que ouçam e se convertam, cada um do seu mau caminho; então, me arrependerei do mal que intento fazer-lhes por causa da maldade das suas ações.
4 Dize-lhes, pois: Assim diz o Senhor: Se não me derdes ouvidos para andardes na minha lei, que pus diante de vós,
5 para que ouvísseis as palavras dos meus servos, os profetas, que, começando de madrugada, vos envio, posto que até aqui não me ouvistes,
6 então, farei que esta casa seja como Siló e farei desta cidade maldição para todas as nações da terra.
7 Os sacerdotes, os profetas e todo o povo ouviram a Jeremias, quando proferia estas palavras na Casa do Senhor.
8 Tendo Jeremias acabado de falar tudo quanto o Senhor lhe havia ordenado que dissesse a todo o povo, lançaram mão dele os sacerdotes, os profetas e todo o povo, dizendo: Serás morto.
9 Por que profetizas em nome do Senhor, dizendo: Será como Siló esta casa, e esta cidade, desolada e sem habitantes? E ajuntou-se todo o povo contra Jeremias, na Casa do Senhor.
10 Tendo os príncipes de Judá ouvido estas palavras, subiram da casa do rei à Casa do Senhor e se assentaram à entrada da Porta Nova da Casa do Senhor.
11 Então, os sacerdotes e os profetas falaram aos príncipes e a todo o povo, dizendo: Este homem é réu de morte, porque profetizou contra esta cidade, como ouvistes com os vossos próprios ouvidos.
12 Falou Jeremias a todos os príncipes e a todo o povo, dizendo: O Senhor me enviou a profetizar contra esta casa e contra esta cidade todas as palavras que ouvistes.
13 Agora, pois, emendai os vossos caminhos e as vossas ações e ouvi a voz do Senhor, vosso Deus; então, se arrependerá o Senhor do mal que falou contra vós outros.
14 Quanto a mim, eis que estou nas vossas mãos; fazei de mim o que for bom e reto segundo vos parecer.
15 Sabei, porém, com certeza que, se me matardes a mim, trareis sangue inocente sobre vós, sobre esta cidade e sobre os seus moradores; porque, na verdade, o Senhor me enviou a vós outros, para me ouvirdes dizer-vos estas palavras.
16 Então, disseram os príncipes e todo o povo aos sacerdotes e aos profetas: Este homem não é réu de morte, porque em nome do Senhor, nosso Deus, nos falou.
17 Também se levantaram alguns dentre os anciãos da terra e falaram a toda a congregação do povo, dizendo:
18 Miqueias, o morastita, profetizou nos dias de Ezequias, rei de Judá, e falou a todo o povo de Judá, dizendo: Assim disse o Senhor dos Exércitos: Sião será lavrada como um campo, Jerusalém se tornará em montões de ruínas, e o monte do templo, numa colina coberta de mato.
19 Mataram-no, acaso, Ezequias, rei de Judá, e todo o Judá? Antes, não temeu este ao Senhor, não implorou o favor do Senhor? E o Senhor não se arrependeu do mal que falara contra eles? E traríamos nós tão grande mal sobre a nossa alma?
20 Também houve outro homem, Urias, filho de Semaías, de Quiriate-Jearim, que profetizava em nome do Senhor e profetizou contra esta cidade e contra esta terra, segundo todas as palavras de Jeremias.
21 Ouvindo o rei Jeoaquim, e todos os seus valentes, e todos os príncipes as suas palavras, procurou o rei matá-lo; mas, ouvindo isto Urias, temeu, fugiu e foi para o Egito.
22 O rei Jeoaquim, porém, enviou a Elnatã, filho de Acbor, ao Egito e com ele outros homens.
23 Eles tiraram a Urias do Egito e o trouxeram ao rei Jeoaquim; este mandou feri-lo à espada e lançar-lhe o cadáver nas sepulturas da plebe.
24 Porém a influência de Aicão, filho de Safã, protegeu a Jeremias, para que o não entregassem nas mãos do povo, para ser morto.*
1 No princípio do reinado de Zedequias, filho de Josias, rei de Judá, veio da parte do Senhor esta palavra a Jeremias:
2 Assim me disse o Senhor: Faze correias e canzis e põe-nos ao pescoço.
3 E envia outros ao rei de Edom, ao rei de Moabe, ao rei dos filhos de Amom, ao rei de Tiro e ao rei de Sidom, por intermédio dos mensageiros que vieram a Jerusalém ter com Zedequias, rei de Judá.
4 Ordena-lhes que digam aos seus senhores: Assim diz o Senhor dos Exércitos, o Deus de Israel: Assim direis a vossos senhores:
5 Eu fiz a terra, o homem e os animais que estão sobre a face da terra, com o meu grande poder e com o meu braço estendido, e os dou àquele a quem for justo.
6 Agora, eu entregarei todas estas terras ao poder de Nabucodonosor, rei da Babilônia, meu servo; e também lhe dei os animais do campo para que o sirvam.
7 Todas as nações servirão a ele, a seu filho e ao filho de seu filho, até que também chegue a vez da sua própria terra, quando muitas nações e grandes reis o fizerem seu escravo.
8 Se alguma nação e reino não servirem o mesmo Nabucodonosor, rei da Babilônia, e não puserem o pescoço debaixo do jugo do rei da Babilônia, a essa nação castigarei com espada, e com fome, e com peste, diz o Senhor, até que eu a consuma pela sua mão.
9 Não deis ouvidos aos vossos profetas e aos vossos adivinhos, aos vossos sonhadores, aos vossos agoureiros e aos vossos encantadores, que vos falam, dizendo: Não servireis o rei da Babilônia.
10 Porque eles vos profetizam mentiras para vos mandarem para longe da vossa terra, e para que eu vos expulse, e pereçais.
11 Mas a nação que meter o pescoço sob o jugo do rei da Babilônia e o servir, eu a deixarei na sua terra, diz o Senhor, e lavrá-la-á e habitará nela.
12 Falei a Zedequias, rei de Judá, segundo todas estas palavras, dizendo: Metei o pescoço no jugo do rei da Babilônia, servi-o, a ele e ao seu povo, e vivereis.
13 Por que morrerias tu e o teu povo, à espada, à fome e de peste, como o Senhor disse com respeito à nação que não servir ao rei da Babilônia?
14 Não deis ouvidos às palavras dos profetas, que vos dizem: Não servireis ao rei da Babilônia. É mentira o que eles vos profetizam.
15 Porque não os enviei, diz o Senhor, e profetizam falsamente em meu nome, para que eu vos expulse e pereçais, vós e eles que vos profetizam.
16 Também falei aos sacerdotes e a todo este povo, dizendo: Assim diz o Senhor: Não deis ouvidos às palavras dos vossos profetas que vos profetizam, dizendo: Eis que os utensílios da Casa do Senhor voltarão em breve da Babilônia. É mentira o que eles vos profetizam.
17 Não lhes deis ouvidos, servi ao rei da Babilônia e vivereis; por que se tornaria esta cidade em desolação?
18 Porém, se são profetas, e se a palavra do Senhor está com eles, que orem ao Senhor dos Exércitos, para que os utensílios que ficaram na Casa do Senhor, e na casa do rei de Judá, e em Jerusalém não sejam levados para a Babilônia.
19 Porque assim diz o Senhor dos Exércitos acerca das colunas, do mar, dos suportes e dos restantes utensílios que ficaram na cidade,
20 os quais Nabucodonosor, rei da Babilônia, não levou, quando deportou, de Jerusalém para a Babilônia, a Jeconias, filho de Jeoaquim, rei de Judá, assim como a todos os nobres de Judá e de Jerusalém;
21 sim, isto diz o Senhor dos Exércitos, o Deus de Israel, acerca dos utensílios que ficaram na Casa do Senhor, e na casa do rei de Judá, e em Jerusalém:
22 à Babilônia serão levados, onde ficarão até ao dia em que eu atentar para eles, diz o Senhor; então, os farei trazer e os devolverei a este lugar.*
1 No mesmo ano, no princípio do reinado de Zedequias, rei de Judá, isto é, no ano quarto, no quinto mês, Hananias, filho de Azur e profeta de Gibeão, me falou na Casa do Senhor, na presença dos sacerdotes e de todo o povo, dizendo:
2 Assim fala o Senhor dos Exércitos, o Deus de Israel, dizendo: Quebrei o jugo do rei da Babilônia.
3 Dentro de dois anos, eu tornarei a trazer a este lugar todos os utensílios da Casa do Senhor, que daqui tomou Nabucodonosor, rei da Babilônia, levando-os para a Babilônia.
4 Também a Jeconias, filho de Jeoaquim, rei de Judá, e a todos os exilados de Judá, que entraram na Babilônia, eu tornarei a trazer a este lugar, diz o Senhor; porque quebrei o jugo do rei da Babilônia.
5 Então, respondeu Jeremias, o profeta, ao profeta Hananias, na presença dos sacerdotes e perante todo o povo que estava na Casa do Senhor.
6 Disse, pois, Jeremias, o profeta: Amém! Assim faça o Senhor; confirme o Senhor as tuas palavras, com que profetizaste, e torne ele a trazer da Babilônia a este lugar os utensílios da Casa do Senhor e todos os exilados.
7 Mas ouve agora esta palavra, que eu falo a ti e a todo o povo para que ouçais:
8 Os profetas que houve antes de mim e antes de ti, desde a antiguidade, profetizaram guerra, mal e peste contra muitas terras e grandes reinos.
9 O profeta que profetizar paz, só ao cumprir-se a sua palavra, será conhecido como profeta, de fato, enviado do Senhor.
10 Então, o profeta Hananias tomou os canzis do pescoço de Jeremias, o profeta, e os quebrou;
11 e falou na presença de todo o povo: Assim diz o Senhor: Deste modo, dentro de dois anos, quebrarei o jugo de Nabucodonosor, rei da Babilônia, de sobre o pescoço de todas as nações. E Jeremias, o profeta, se foi, tomando o seu caminho.
12 Mas depois que Hananias, o profeta, quebrou os canzis de sobre o pescoço do profeta Jeremias, veio a este a palavra do Senhor, dizendo:
13 Vai e fala a Hananias, dizendo: Assim diz o Senhor: Canzis de madeira quebraste. Mas, em vez deles, farei canzis de ferro.
14 Porque assim diz o Senhor dos Exércitos, o Deus de Israel: Jugo de ferro pus sobre o pescoço de todas estas nações, para servirem a Nabucodonosor, rei da Babilônia; e o servirão. Também lhe dei os animais do campo.
15 Disse Jeremias, o profeta, ao profeta Hananias: Ouve agora, Hananias: O Senhor não te enviou, mas tu fizeste que este povo confiasse em mentiras.
16 Pelo que assim diz o Senhor: Eis que te lançarei de sobre a face da terra; morrerás este ano, porque pregaste rebeldia contra o Senhor.
17 Morreu, pois, o profeta Hananias, no mesmo ano, no sétimo mês.*
1 São estas as palavras da carta que Jeremias, o profeta, enviou de Jerusalém ao resto dos anciãos do cativeiro, como também aos sacerdotes, aos profetas e a todo o povo que Nabucodonosor havia deportado de Jerusalém para a Babilônia,
2 depois que saíram de Jerusalém o rei Jeconias, a rainha-mãe, os oficiais, os príncipes de Judá e Jerusalém e os carpinteiros e ferreiros.
3 A carta foi mandada por intermédio de Elasa, filho de Safã, e de Gemarias, filho de Hilquias, os quais Zedequias, rei de Judá, tinha enviado à Babilônia, a Nabucodonosor, rei da Babilônia, e dizia:
4 Assim diz o Senhor dos Exércitos, o Deus de Israel, a todos os exilados que eu deportei de Jerusalém para a Babilônia:
5 Edificai casas e habitai nelas; plantai pomares e comei o seu fruto.
6 Tomai esposas e gerai filhos e filhas, tomai esposas para vossos filhos e dai vossas filhas a maridos, para que tenham filhos e filhas; multiplicai-vos aí e não vos diminuais.
7 Procurai a paz da cidade para onde vos desterrei e orai por ela ao Senhor; porque na sua paz vós tereis paz.
8 Porque assim diz o Senhor dos Exércitos, o Deus de Israel: Não vos enganem os vossos profetas que estão no meio de vós, nem os vossos adivinhos, nem deis ouvidos aos vossos sonhadores, que sempre sonham segundo o vosso desejo;
9 porque falsamente vos profetizam eles em meu nome; eu não os enviei, diz o Senhor.
10 Assim diz o Senhor: Logo que se cumprirem para a Babilônia setenta anos, atentarei para vós outros e cumprirei para convosco a minha boa palavra, tornando a trazer-vos para este lugar.
11 Eu é que sei que pensamentos tenho a vosso respeito, diz o Senhor; pensamentos de paz e não de mal, para vos dar o fim que desejais.
12 Então, me invocareis, passareis a orar a mim, e eu vos ouvirei.
13 Buscar-me-eis e me achareis quando me buscardes de todo o vosso coração.
14 Serei achado de vós, diz o Senhor, e farei mudar a vossa sorte; congregar-vos-ei de todas as nações e de todos os lugares para onde vos lancei, diz o Senhor, e tornarei a trazer-vos ao lugar donde vos mandei para o exílio.
15 Vós dizeis: O Senhor nos suscitou profetas na Babilônia.
16 Mas assim diz o Senhor a respeito do rei que se assenta no trono de Davi e de todo o povo que habita nesta cidade, vossos irmãos, que não saíram convosco para o exílio;
17 assim diz o Senhor dos Exércitos: Eis que enviarei contra eles a espada, a fome e a peste e fá-los-ei como a figos ruins, que, de ruins que são, não se podem comer.
18 Persegui-los-ei com a espada, a fome e a peste; fá-los-ei um espetáculo horrendo para todos os reinos da terra; e os porei por objeto de espanto, e de assobio, e de opróbrio entre todas as nações para onde os tiver arrojado;
19 porque não deram ouvidos às minhas palavras, diz o Senhor, com as quais, começando de madrugada, lhes enviei os meus servos, os profetas; mas vós não os escutastes, diz o Senhor.
20 Vós, pois, ouvi a palavra do Senhor, todos os do exílio que enviei de Jerusalém para a Babilônia.
21 Assim diz o Senhor dos Exércitos, o Deus de Israel, acerca de Acabe, filho de Colaías, e de Zedequias, filho de Maaseias, que vos profetizam falsamente em meu nome: Eis que os entregarei nas mãos de Nabucodonosor, rei da Babilônia, e ele os ferirá diante dos vossos olhos.
22 Daí surgirá nova espécie de maldição entre os exilados de Judá que estão na Babilônia: o Senhor te faça como a Zedequias e como a Acabe, os quais o rei da Babilônia assou no fogo;
23 porquanto fizeram loucuras em Israel, cometeram adultérios com as mulheres de seus companheiros e anunciaram falsamente em meu nome palavras que não lhes mandei dizer; eu o sei e sou testemunha disso, diz o Senhor.
24 A Semaías, o neelamita, falarás, dizendo:
25 Assim diz o Senhor dos Exércitos, o Deus de Israel: Porquanto enviaste no teu nome cartas a todo o povo que está em Jerusalém, como também a Sofonias, filho de Maaseias, o sacerdote, e a todos os sacerdotes, dizendo:
26 O Senhor te pôs por sacerdote em lugar do sacerdote Joiada, para que sejas encarregado da Casa do Senhor sobre todo homem fanático que quer passar por profeta, para o lançares na prisão e no tronco.
27 Agora, pois, por que não repreendeste a Jeremias, o anatotita, que vos profetiza?
28 Pois nos enviou mensageiros à Babilônia para nos dizer: Há de durar muito o exílio; edificai casas e habitai nelas; plantai pomares e comei o seu fruto.
29 Sofonias, o sacerdote, leu esta carta aos ouvidos do profeta Jeremias.
30 Então, veio a palavra do Senhor a Jeremias, dizendo:
31 Manda dizer a todos os exilados: Assim diz o Senhor acerca de Semaías, o neelamita: Porquanto Semaías vos profetizou, não o havendo eu enviado, e vos fez confiar em mentiras,
32 assim diz o Senhor: Eis que castigarei a Semaías, o neelamita, e à sua descendência; ele não terá ninguém que habite entre este povo e não verá o bem que hei de fazer ao meu povo, diz o Senhor, porque pregou rebeldia contra o Senhor.*
1 Palavra que do Senhor veio a Jeremias, dizendo:
2 Assim fala o Senhor, Deus de Israel: Escreve num livro todas as palavras que eu disse.
3 Porque eis que vêm dias, diz o Senhor, em que mudarei a sorte do meu povo de Israel e de Judá, diz o Senhor; fá-los-ei voltar para a terra que dei a seus pais, e a possuirão.
4 São estas as palavras que disse o Senhor acerca de Israel e de Judá:
5 Assim diz o Senhor: Ouvimos uma voz de tremor e de temor e não de paz.
6 Perguntai, pois, e vede se, acaso, um homem tem dores de parto. Por que vejo, pois, a cada homem com as mãos na cintura, como a que está dando à luz? E por que se tornaram pálidos todos os rostos?
7 Ah! Que grande é aquele dia, e não há outro semelhante! É tempo de angústia para Jacó; ele, porém, será livre dela.
8 Naquele dia, diz o Senhor dos Exércitos, eu quebrarei o seu jugo de sobre o teu pescoço e quebrarei os teus canzis; e nunca mais estrangeiros farão escravo este povo,
9 que servirá ao Senhor, seu Deus, como também a Davi, seu rei, que lhe levantarei.
10 Não temas, pois, servo meu, Jacó, diz o Senhor, nem te espantes, ó Israel; pois eis que te livrarei das terras de longe e à tua descendência, da terra do exílio; Jacó voltará e ficará tranquilo e em sossego; e não haverá quem o atemorize.
11 Porque eu sou contigo, diz o Senhor, para salvar-te; por isso, darei cabo de todas as nações entre as quais te espalhei; de ti, porém, não darei cabo, mas castigar-te-ei em justa medida e de todo não te inocentarei.
12 Porque assim diz o Senhor: Teu mal é incurável, a tua chaga é dolorosa.
13 Não há quem defenda a tua causa; para a tua ferida não tens remédios nem emplasto.
14 Todos os teus amantes se esqueceram de ti, já não perguntam por ti; porque te feri com ferida de inimigo e com castigo de cruel, por causa da grandeza da tua maldade e da multidão de teus pecados.
15 Por que gritas por motivo da tua ferida? Tua dor é incurável. Por causa da grandeza de tua maldade e da multidão de teus pecados é que eu fiz estas coisas.
16 Por isso, todos os que te devoram serão devorados; e todos os teus adversários serão levados, cada um deles para o cativeiro; os que te despojam serão despojados, e entregarei ao saque todos os que te saqueiam.
17 Porque te restaurarei a saúde e curarei as tuas chagas, diz o Senhor; pois te chamaram a repudiada, dizendo: É Sião, já ninguém pergunta por ela.
18 Assim diz o Senhor: Eis que restaurarei a sorte das tendas de Jacó e me compadecerei das suas moradas; a cidade será reedificada sobre o seu montão de ruínas, e o palácio será habitado como outrora.
19 Sairão deles ações de graças e o júbilo dos que se alegram. Multiplicá-los-ei, e não serão diminuídos; glorificá-los-ei, e não serão apoucados.
20 Seus filhos serão como na antiguidade, e a sua congregação será firmada diante de mim, e castigarei todos os seus opressores.
21 O seu príncipe procederá deles, do meio deles sairá o que há de reinar; fá-lo-ei aproximar, e ele se chegará a mim; pois quem de si mesmo ousaria aproximar-se de mim? — diz o Senhor.
22 Vós sereis o meu povo, eu serei o vosso Deus.
23 Eis a tempestade do Senhor! O furor saiu, e um redemoinho tempestuou sobre a cabeça dos perversos.
24 Não voltará atrás o brasume da ira do Senhor, até que tenha executado e cumprido os desígnios do seu coração. Nos últimos dias, entendereis isto.*
1 Naquele tempo, diz o Senhor, serei o Deus de todas as tribos de Israel, e elas serão o meu povo.
2 Assim diz o Senhor: O povo que se livrou da espada logrou graça no deserto. Eu irei e darei descanso a Israel.
3 De longe se me deixou ver o Senhor, dizendo: Com amor eterno eu te amei; por isso, com benignidade te atraí.
4 Ainda te edificarei, e serás edificada, ó virgem de Israel! Ainda serás adornada com os teus adufes e sairás com o coro dos que dançam.
5 Ainda plantarás vinhas nos montes de Samaria; plantarão os plantadores e gozarão dos frutos.
6 Porque haverá um dia em que gritarão os atalaias na região montanhosa de Efraim: Levantai-vos, e subamos a Sião, ao Senhor, nosso Deus!
7 Porque assim diz o Senhor: Cantai com alegria a Jacó, exultai por causa da cabeça das nações; proclamai, cantai louvores e dizei: Salva, Senhor, o teu povo, o restante de Israel.
8 Eis que os trarei da terra do Norte e os congregarei das extremidades da terra; e, entre eles, também os cegos e aleijados, as mulheres grávidas e as de parto; em grande congregação, voltarão para aqui.
9 Virão com choro, e com súplicas os levarei; guiá-los-ei aos ribeiros de águas, por caminho reto em que não tropeçarão; porque sou pai para Israel, e Efraim é o meu primogênito.
10 Ouvi a palavra do Senhor, ó nações, e anunciai nas terras longínquas do mar, e dizei: Aquele que espalhou a Israel o congregará e o guardará, como o pastor, ao seu rebanho.
11 Porque o Senhor redimiu a Jacó e o livrou da mão do que era mais forte do que ele.
12 Hão de vir e exultar na altura de Sião, radiantes de alegria por causa dos bens do Senhor, do cereal, do vinho, do azeite, dos cordeiros e dos bezerros; a sua alma será como um jardim regado, e nunca mais desfalecerão.
13 Então, a virgem se alegrará na dança, e também os jovens e os velhos; tornarei o seu pranto em júbilo e os consolarei; transformarei em regozijo a sua tristeza.
14 Saciarei de gordura a alma dos sacerdotes, e o meu povo se fartará com a minha bondade, diz o Senhor.
15 Assim diz o Senhor: Ouviu-se um clamor em Ramá, pranto e grande lamento; era Raquel chorando por seus filhos e inconsolável por causa deles, porque já não existem.
16 Assim diz o Senhor: Reprime a tua voz de choro e as lágrimas de teus olhos; porque há recompensa para as tuas obras, diz o Senhor, pois os teus filhos voltarão da terra do inimigo.
17 Há esperança para o teu futuro, diz o Senhor, porque teus filhos voltarão para os seus territórios.
18 Bem ouvi que Efraim se queixava, dizendo: Castigaste-me, e fui castigado como novilho ainda não domado; converte-me, e serei convertido, porque tu és o Senhor, meu Deus.
19 Na verdade, depois que me converti, arrependi-me; depois que fui instruído, bati no peito; fiquei envergonhado, confuso, porque levei o opróbrio da minha mocidade.
20 Não é Efraim meu precioso filho, filho das minhas delícias? Pois tantas vezes quantas falo contra ele, tantas vezes ternamente me lembro dele; comove-se por ele o meu coração, deveras me compadecerei dele, diz o Senhor.
21 Põe-te marcos, finca postes que te guiem, presta atenção na vereda, no caminho por onde passaste; regressa, ó virgem de Israel, regressa às tuas cidades.
22 Até quando andarás errante, ó filha rebelde? Porque o Senhor criou coisa nova na terra: a mulher infiel virá a requestar um homem.
23 Assim diz o Senhor dos Exércitos, o Deus de Israel: Ainda dirão esta palavra na terra de Judá e nas suas cidades, quando eu lhe restaurar a sorte: O Senhor te abençoe, ó morada de justiça, ó santo monte!
24 Nela, habitarão Judá e todas as suas cidades juntamente, como também os lavradores e os que pastoreiam os rebanhos.
25 Porque satisfiz à alma cansada, e saciei a toda alma desfalecida.
26 Nisto, despertei e olhei; e o meu sono fora doce para mim.
27 Eis que vêm dias, diz o Senhor, em que semearei a casa de Israel e a casa de Judá com a semente de homens e de animais.
28 Como velei sobre eles, para arrancar, para derribar, para subverter, para destruir e para afligir, assim velarei sobre eles para edificar e para plantar, diz o Senhor.
29 Naqueles dias, já não dirão: Os pais comeram uvas verdes, e os dentes dos filhos é que se embotaram.
30 Cada um, porém, será morto pela sua iniquidade; de todo homem que comer uvas verdes os dentes se embotarão.
31 Eis aí vêm dias, diz o Senhor, em que firmarei nova aliança com a casa de Israel e com a casa de Judá.
32 Não conforme a aliança que fiz com seus pais, no dia em que os tomei pela mão, para os tirar da terra do Egito; porquanto eles anularam a minha aliança, não obstante eu os haver desposado, diz o Senhor.
33 Porque esta é a aliança que firmarei com a casa de Israel, depois daqueles dias, diz o Senhor: Na mente, lhes imprimirei as minhas leis, também no coração lhas inscreverei; eu serei o seu Deus, e eles serão o meu povo.
34 Não ensinará jamais cada um ao seu próximo, nem cada um ao seu irmão, dizendo: Conhece ao Senhor, porque todos me conhecerão, desde o menor até ao maior deles, diz o Senhor. Pois perdoarei as suas iniquidades e dos seus pecados jamais me lembrarei.
35 Assim diz o Senhor, que dá o sol para a luz do dia e as leis fixas à lua e às estrelas para a luz da noite, que agita o mar e faz bramir as suas ondas; Senhor dos Exércitos é o seu nome.
36 Se falharem estas leis fixas diante de mim, diz o Senhor, deixará também a descendência de Israel de ser uma nação diante de mim para sempre.
37 Assim diz o Senhor: Se puderem ser medidos os céus lá em cima e sondados os fundamentos da terra cá embaixo, também eu rejeitarei toda a descendência de Israel, por tudo quanto fizeram, diz o Senhor.
38 Eis que vêm dias, diz o Senhor, em que esta cidade será reedificada para o Senhor, desde a Torre de Hananel até à Porta da Esquina.
39 O cordel de medir estender-se-á para diante, até ao outeiro de Garebe, e virar-se-á para Goa.
40 Todo o vale dos cadáveres e da cinza e todos os campos até ao ribeiro Cedrom, até à esquina da Porta dos Cavalos para o oriente, serão consagrados ao Senhor. Esta Jerusalém jamais será desarraigada ou destruída.*
1 Palavra que veio a Jeremias da parte do Senhor, no ano décimo de Zedequias, rei de Judá, ou décimo oitavo de Nabucodonosor.
2 Ora, nesse tempo o exército do rei da Babilônia cercava Jerusalém; Jeremias, o profeta, estava encarcerado no pátio da guarda que estava na casa do rei de Judá.
3 Pois Zedequias, rei de Judá, o havia encerrado, dizendo: Por que profetizas tu que o Senhor disse que entregaria esta cidade nas mãos do rei da Babilônia, e ele a tomaria;
4 que Zedequias, rei de Judá, não se livraria das mãos dos caldeus, mas infalivelmente seria entregue nas mãos do rei da Babilônia, e com ele falaria boca a boca, e o veria face a face;
5 e que ele levaria Zedequias para a Babilônia, onde estaria até que o Senhor se lembrasse dele, como este disse; e, ainda que pelejásseis contra os caldeus, não seríeis bem-sucedidos?
6 Disse, pois, Jeremias: Veio a mim a palavra do Senhor, dizendo:
7 Eis que Hananel, filho de teu tio Salum, virá a ti, dizendo: Compra o meu campo que está em Anatote, pois a ti, a quem pertence o direito de resgate, compete comprá-lo.
8 Veio, pois, a mim, segundo a palavra do Senhor, Hananel, filho de meu tio, ao pátio da guarda e me disse: Compra agora o meu campo que está em Anatote, na terra de Benjamim; porque teu é o direito de posse e de resgate; compra-o. Então, entendi que isto era a palavra do Senhor.
9 Comprei, pois, de Hananel, filho de meu tio, o campo que está em Anatote; e lhe pesei o dinheiro, dezessete siclos de prata.
10 Assinei a escritura, fechei-a com selo, chamei testemunhas e pesei-lhe o dinheiro numa balança.
11 Tomei a escritura da compra, tanto a selada, segundo mandam a lei e os estatutos, como a cópia aberta;
12 dei-a a Baruque, filho de Nerias, filho de Maaseias, na presença de Hananel, filho de meu tio, e perante as testemunhas, que assinaram a escritura da compra, e na presença de todos os judeus que se assentavam no pátio da guarda.
13 Perante eles dei ordem a Baruque, dizendo:
14 Assim diz o Senhor dos Exércitos, o Deus de Israel: Toma esta escritura, esta escritura da compra, tanto a selada como a aberta, e mete-as num vaso de barro, para que se possam conservar por muitos dias;
15 porque assim diz o Senhor dos Exércitos, o Deus de Israel: Ainda se comprarão casas, campos e vinhas nesta terra.
16 Depois que dei a escritura da compra a Baruque, filho de Nerias, orei ao Senhor, dizendo:
17 Ah! Senhor Deus, eis que fizeste os céus e a terra com o teu grande poder e com o teu braço estendido; coisa alguma te é demasiadamente maravilhosa.
18 Tu usas de misericórdia para com milhares e retribuis a iniquidade dos pais nos filhos; tu és o grande, o poderoso Deus, cujo nome é o Senhor dos Exércitos,
19 grande em conselho e magnífico em obras; porque os teus olhos estão abertos sobre todos os caminhos dos filhos dos homens, para dar a cada um segundo o seu proceder, segundo o fruto das suas obras.
20 Tu puseste sinais e maravilhas na terra do Egito até ao dia de hoje, tanto em Israel como entre outros homens; e te fizeste um nome, qual o que tens neste dia.
21 Tiraste o teu povo de Israel da terra do Egito, com sinais e maravilhas, com mão poderosa e braço estendido e com grande espanto;
22 e lhe deste esta terra, que com juramento prometeste a seus pais, terra que mana leite e mel.
23 Entraram nela e dela tomaram posse, mas não obedeceram à tua voz, nem andaram na tua lei; de tudo o que lhes mandaste que fizessem, nada fizeram; pelo que trouxeste sobre eles todo este mal.
24 Eis aqui as trincheiras já atingem a cidade, para ser tomada; já está a cidade entregue nas mãos dos caldeus, que pelejam contra ela, pela espada, pela fome e pela peste. O que disseste aconteceu; e tu mesmo o vês.
25 Contudo, ó Senhor Deus, tu me disseste: Compra o campo por dinheiro e chama testemunhas, embora já esteja a cidade entregue nas mãos dos caldeus.
26 Então, veio a palavra do Senhor a Jeremias, dizendo:
27 Eis que eu sou o Senhor, o Deus de todos os viventes; acaso, haveria coisa demasiadamente maravilhosa para mim?
28 Portanto, assim diz o Senhor: Eis que entrego esta cidade nas mãos dos caldeus, nas mãos de Nabucodonosor, rei da Babilônia, e ele a tomará.
29 Os caldeus, que pelejam contra esta cidade, entrarão nela, porão fogo a esta cidade e queimarão as casas sobre cujos terraços queimaram incenso a Baal e ofereceram libações a outros deuses, para me provocarem à ira.
30 Porque os filhos de Israel e os filhos de Judá não fizeram senão mal perante mim, desde a sua mocidade; porque os filhos de Israel não fizeram senão provocar-me à ira com as obras das suas mãos, diz o Senhor.
31 Porque para minha ira e para meu furor me tem sido esta cidade, desde o dia em que a edificaram e até ao dia de hoje, para que eu a removesse da minha presença,
32 por causa de toda a maldade que fizeram os filhos de Israel e os filhos de Judá, para me provocarem à ira, eles, os seus reis, os seus príncipes, os seus sacerdotes e os seus profetas, como também os homens de Judá e os moradores de Jerusalém.
33 Viraram-me as costas e não o rosto; ainda que eu, começando de madrugada, os ensinava, eles não deram ouvidos, para receberem a advertência.
34 Antes, puseram as suas abominações na casa que se chama pelo meu nome, para a profanarem.
35 Edificaram os altos de Baal, que estão no vale do filho de Hinom, para queimarem a seus filhos e a suas filhas a Moloque, o que nunca lhes ordenei, nem me passou pela mente fizessem tal abominação, para fazerem pecar a Judá.
36 Agora, pois, assim diz o Senhor, o Deus de Israel, acerca desta cidade, da qual vós dizeis: Já está entregue nas mãos do rei da Babilônia, pela espada, pela fome e pela peste.
37 Eis que eu os congregarei de todas as terras, para onde os lancei na minha ira, no meu furor e na minha grande indignação; tornarei a trazê-los a este lugar e farei que nele habitem seguramente.
38 Eles serão o meu povo, e eu serei o seu Deus.
39 Dar-lhes-ei um só coração e um só caminho, para que me temam todos os dias, para seu bem e bem de seus filhos.
40 Farei com eles aliança eterna, segundo a qual não deixarei de lhes fazer o bem; e porei o meu temor no seu coração, para que nunca se apartem de mim.
41 Alegrar-me-ei por causa deles e lhes farei bem; plantá-los-ei firmemente nesta terra, de todo o meu coração e de toda a minha alma.
42 Porque assim diz o Senhor: Assim como fiz vir sobre este povo todo este grande mal, assim lhes trarei todo o bem que lhes estou prometendo.
43 Comprar-se-ão campos nesta terra, da qual vós dizeis: Está deserta, sem homens nem animais; está entregue nas mãos dos caldeus.
44 Comprarão campos por dinheiro, e lavrarão as escrituras, e as fecharão com selos, e chamarão testemunhas na terra de Benjamim, nos contornos de Jerusalém, nas cidades de Judá, nas cidades da região montanhosa, nas cidades das planícies e nas cidades do Sul; porque lhes restaurarei a sorte, diz o Senhor.*
1 Veio a palavra do Senhor a Jeremias, segunda vez, estando ele ainda encarcerado no pátio da guarda, dizendo:
2 Assim diz o Senhor que faz estas coisas, o Senhor que as forma para as estabelecer (Senhor é o seu nome):
3 Invoca-me, e te responderei; anunciar-te-ei coisas grandes e ocultas, que não sabes.
4 Porque assim diz o Senhor, o Deus de Israel, a respeito das casas desta cidade e das casas dos reis de Judá, que foram derribadas para a defesa contra as trincheiras e a espada:
5 Quando se der a peleja contra os caldeus, para que eu as encha de cadáveres de homens, feridos por minha ira e meu furor, porquanto desta cidade escondi o meu rosto, por causa de toda a sua maldade,
6 eis que lhe trarei a ela saúde e cura e os sararei; e lhes revelarei abundância de paz e segurança.
7 Restaurarei a sorte de Judá e de Israel e os edificarei como no princípio.
8 Purificá-los-ei de toda a sua iniquidade com que pecaram contra mim; e perdoarei todas as suas iniquidades com que pecaram e transgrediram contra mim.
9 Jerusalém me servirá por nome, por louvor e glória, entre todas as nações da terra que ouvirem todo o bem que eu lhe faço; espantar-se-ão e tremerão por causa de todo o bem e por causa de toda a paz que eu lhe dou.
10 Assim diz o Senhor: Neste lugar, que vós dizeis que está deserto, sem homens nem animais, nas cidades de Judá e nas ruas de Jerusalém, que estão assoladas, sem homens, sem moradores e sem animais, ainda se ouvirá
11 a voz de júbilo e de alegria, e a voz de noivo, e a de noiva, e a voz dos que cantam: Rendei graças ao Senhor dos Exércitos, porque ele é bom, porque a sua misericórdia dura para sempre; e dos que trazem ofertas de ações de graças à Casa do Senhor; porque restaurarei a sorte da terra como no princípio, diz o Senhor.
12 Assim diz o Senhor dos Exércitos: Ainda neste lugar, que está deserto, sem homens e sem animais, e em todas as suas cidades, haverá morada de pastores que façam repousar aos seus rebanhos.
13 Nas cidades da região montanhosa, e nas cidades das planícies, e nas cidades do Sul, na terra de Benjamim, e nos contornos de Jerusalém, e nas cidades de Judá, ainda passarão os rebanhos pelas mãos de quem os conte, diz o Senhor.
1 Veio a palavra do Senhor a Jeremias, segunda vez, estando ele ainda encarcerado no pátio da guarda, dizendo:
2 Assim diz o Senhor que faz estas coisas, o Senhor que as forma para as estabelecer (Senhor é o seu nome):
3 Invoca-me, e te responderei; anunciar-te-ei coisas grandes e ocultas, que não sabes.
4 Porque assim diz o Senhor, o Deus de Israel, a respeito das casas desta cidade e das casas dos reis de Judá, que foram derribadas para a defesa contra as trincheiras e a espada:
5 Quando se der a peleja contra os caldeus, para que eu as encha de cadáveres de homens, feridos por minha ira e meu furor, porquanto desta cidade escondi o meu rosto, por causa de toda a sua maldade,
6 eis que lhe trarei a ela saúde e cura e os sararei; e lhes revelarei abundância de paz e segurança.
7 Restaurarei a sorte de Judá e de Israel e os edificarei como no princípio.
8 Purificá-los-ei de toda a sua iniquidade com que pecaram contra mim; e perdoarei todas as suas iniquidades com que pecaram e transgrediram contra mim.
9 Jerusalém me servirá por nome, por louvor e glória, entre todas as nações da terra que ouvirem todo o bem que eu lhe faço; espantar-se-ão e tremerão por causa de todo o bem e por causa de toda a paz que eu lhe dou.
10 Assim diz o Senhor: Neste lugar, que vós dizeis que está deserto, sem homens nem animais, nas cidades de Judá e nas ruas de Jerusalém, que estão assoladas, sem homens, sem moradores e sem animais, ainda se ouvirá
11 a voz de júbilo e de alegria, e a voz de noivo, e a de noiva, e a voz dos que cantam: Rendei graças ao Senhor dos Exércitos, porque ele é bom, porque a sua misericórdia dura para sempre; e dos que trazem ofertas de ações de graças à Casa do Senhor; porque restaurarei a sorte da terra como no princípio, diz o Senhor.
12 Assim diz o Senhor dos Exércitos: Ainda neste lugar, que está deserto, sem homens e sem animais, e em todas as suas cidades, haverá morada de pastores que façam repousar aos seus rebanhos.
13 Nas cidades da região montanhosa, e nas cidades das planícies, e nas cidades do Sul, na terra de Benjamim, e nos contornos de Jerusalém, e nas cidades de Judá, ainda passarão os rebanhos pelas mãos de quem os conte, diz o Senhor.14 Eis que vêm dias, diz o Senhor, em que cumprirei a boa palavra que proferi à casa de Israel e à casa de Judá.
15 Naqueles dias e naquele tempo, farei brotar a Davi um Renovo de justiça; ele executará juízo e justiça na terra.
16 Naqueles dias, Judá será salvo e Jerusalém habitará seguramente; ela será chamada Senhor, Justiça Nossa.
17 Porque assim diz o Senhor: Nunca faltará a Davi homem que se assente no trono da casa de Israel;
18 nem aos sacerdotes levitas faltará homem diante de mim, para que ofereça holocausto, queime oferta de manjares e faça sacrifício todos os dias.
19 Veio a palavra do Senhor a Jeremias, dizendo:
20 Assim diz o Senhor: Se puderdes invalidar a minha aliança com o dia e a minha aliança com a noite, de tal modo que não haja nem dia nem noite a seu tempo,
21 poder-se-á também invalidar a minha aliança com Davi, meu servo, para que não tenha filho que reine no seu trono; como também com os levitas sacerdotes, meus ministros.
22 Como não se pode contar o exército dos céus, nem medir-se a areia do mar, assim tornarei incontável a descendência de Davi, meu servo, e os levitas que ministram diante de mim.
23 Veio ainda a palavra do Senhor a Jeremias, dizendo:
24 Não atentas para o que diz este povo: As duas famílias que o Senhor elegeu, agora as rejeitou? Assim desprezam a meu povo, que a seus olhos já não é povo.
25 Assim diz o Senhor: Se a minha aliança com o dia e com a noite não permanecer, e eu não mantiver as leis fixas dos céus e da terra,
26 também rejeitarei a descendência de Jacó e de Davi, meu servo, de modo que não tome da sua descendência quem domine sobre a descendência de Abraão, Isaque e Jacó; porque lhes restaurarei a sorte e deles me apiedarei.*
1 Palavra que do Senhor veio a Jeremias, quando Nabucodonosor, rei da Babilônia, e todo o seu exército, e todos os reinos da terra que estavam debaixo do seu poder, e todos os povos pelejavam contra Jerusalém e contra todas as suas cidades, dizendo:
2 Assim diz o Senhor, Deus de Israel: Vai, fala a Zedequias, rei de Judá, e dize-lhe: Assim diz o Senhor: Eis que eu entrego esta cidade nas mãos do rei da Babilônia, o qual a queimará.
3 Tu não lhe escaparás das mãos; pelo contrário, serás preso e entregue nas suas mãos; tu verás o rei da Babilônia face a face, e ele te falará boca a boca, e entrarás na Babilônia.
4 Todavia, ouve a palavra do Senhor, ó Zedequias, rei de Judá: Assim diz o Senhor a teu respeito: Não morrerás à espada.
5 Em paz morrerás, e te queimarão perfumes a ti, como se queimaram a teus pais, que, como reis, te precederam, e te prantearão, dizendo: Ah! Senhor! Pois eu é que disse a palavra, diz o Senhor.
6 Falou Jeremias, o profeta, a Zedequias, rei de Judá, todas estas palavras, em Jerusalém,
7 quando o exército do rei da Babilônia pelejava contra Jerusalém e contra todas as cidades que restavam de Judá, contra Laquis e contra Azeca; porque só estas ficaram das cidades fortificadas de Judá.
8 Palavra que do Senhor veio a Jeremias, depois que o rei Zedequias fez aliança com todo o povo de Jerusalém, para lhes apregoar a liberdade:
9 que cada um despedisse forro o seu servo e cada um, a sua serva, hebreu ou hebreia, de maneira que ninguém retivesse como escravos hebreus, seus irmãos.
10 Todos os príncipes e todo o povo que haviam entrado na aliança obedeceram, despedindo forro cada um o seu servo e cada um a sua serva, de maneira que já não os retiveram como escravos; obedeceram e os despediram.
11 Mas depois se arrependeram, e fizeram voltar os servos e as servas que haviam despedido forros, e os sujeitaram por servos e por servas.
12 Veio, pois, a palavra do Senhor a Jeremias, da parte do Senhor, dizendo:
13 Assim diz o Senhor, Deus de Israel: Eu fiz aliança com vossos pais, no dia em que os tirei da terra do Egito, da casa da servidão, dizendo:
14 Ao fim de sete anos, libertareis cada um a seu irmão hebreu, que te for vendido a ti e te houver servido seis anos, e despedi-lo-ás forro; mas vossos pais não me obedeceram, nem inclinaram os seus ouvidos a mim.
15 Não há muito, havíeis voltado a fazer o que é reto perante mim, apregoando liberdade cada um ao seu próximo; e tínheis feito perante mim aliança, na casa que se chama pelo meu nome;
16 mudastes, porém, e profanastes o meu nome, fazendo voltar cada um o seu servo e cada um, a sua serva, os quais, deixados à vontade, já tínheis despedido forros, e os sujeitastes, para que fossem vossos servos e servas.
17 Portanto, assim diz o Senhor: Vós não me obedecestes, para apregoardes a liberdade, cada um a seu irmão e cada um ao seu próximo; pois eis que eu vos apregoo a liberdade, diz o Senhor, para a espada, para a peste e para a fome; farei que sejais um espetáculo horrendo para todos os reinos da terra.
18 Farei aos homens que transgrediram a minha aliança e não cumpriram as palavras da aliança que fizeram perante mim como eles fizeram com o bezerro que dividiram em duas partes, passando eles pelo meio das duas porções;
19 os príncipes de Judá, os príncipes de Jerusalém, os oficiais, os sacerdotes e todo o povo da terra, os quais passaram por meio das porções do bezerro,
20 entregá-los-ei nas mãos de seus inimigos e nas mãos dos que procuram a sua morte, e os cadáveres deles servirão de pasto às aves dos céus e aos animais da terra.
21 A Zedequias, rei de Judá, e a seus príncipes, entregá-los-ei nas mãos de seus inimigos e nas mãos dos que procuram a sua morte, nas mãos do exército do rei da Babilônia, que já se retiraram de vós.
22 Eis que eu darei ordem, diz o Senhor, e os farei tornar a esta cidade, e pelejarão contra ela, tomá-la-ão e a queimarão; e as cidades de Judá porei em assolação, de sorte que ninguém habite nelas.*
1 Palavra que do Senhor veio a Jeremias, nos dias de Jeoaquim, filho de Josias, rei de Judá, dizendo:
2 Vai à casa dos recabitas, fala com eles, leva-os à Casa do Senhor, a uma das câmaras, e dá-lhes vinho a beber.
3 Então, tomei a Jazanias, filho de Jeremias, filho de Habazinias, aos irmãos, e a todos os filhos dele, e a toda a casa dos recabitas;
4 e os levei à Casa do Senhor, à câmara dos filhos de Hanã, filho de Jigdalias, homem de Deus, que está junto à câmara dos príncipes e sobre a de Maaseias, filho de Salum, guarda do vestíbulo;
5 e pus diante dos filhos da casa dos recabitas taças cheias de vinho e copos e lhes disse: Bebei vinho.
6 Mas eles disseram: Não beberemos vinho, porque Jonadabe, filho de Recabe, nosso pai, nos ordenou: Nunca jamais bebereis vinho, nem vós nem vossos filhos;
7 não edificareis casa, não fareis sementeiras, não plantareis, nem possuireis vinha alguma; mas habitareis em tendas todos os vossos dias, para que vivais muitos dias sobre a terra em que viveis peregrinando.
8 Obedecemos, pois, à voz de Jonadabe, filho de Recabe, nosso pai, em tudo quanto nos ordenou; de maneira que não bebemos vinho em todos os nossos dias, nem nós, nem nossas mulheres, nem nossos filhos, nem nossas filhas;
9 nem edificamos casas para nossa habitação; não temos vinha, nem campo, nem semente.
10 Mas habitamos em tendas, e, assim, obedecemos, e tudo fizemos segundo nos ordenou Jonadabe, nosso pai.
11 Quando, porém, Nabucodonosor, rei da Babilônia, subia a esta terra, dissemos: Vinde, e refugiemo-nos em Jerusalém, por causa do exército dos caldeus e dos siros; e assim ficamos em Jerusalém.
12 Então, veio a palavra do Senhor a Jeremias, dizendo:
13 Assim diz o Senhor dos Exércitos, o Deus de Israel: Vai e dize aos homens de Judá e aos moradores de Jerusalém: Acaso, nunca aceitareis a minha advertência para obedecerdes às minhas palavras? — diz o Senhor.
14 As palavras de Jonadabe, filho de Recabe, que ordenou a seus filhos não bebessem vinho, foram guardadas; pois, até ao dia de hoje, não beberam; antes, obedecem às ordens de seu pai; a mim, porém, que, começando de madrugada, vos tenho falado, não me obedecestes.
15 Começando de madrugada, vos tenho enviado todos os meus servos, dizendo: Convertei-vos agora, cada um do seu mau caminho, fazei boas as vossas ações e não sigais a outros deuses para servi-los; assim ficareis na terra que vos dei a vós outros e a vossos pais; mas não me inclinastes os ouvidos, nem me obedecestes a mim.
16 Visto que os filhos de Jonadabe, filho de Recabe, guardaram o mandamento de seu pai, que ele lhes ordenara, mas este povo não me obedeceu,
17 por isso, assim diz o Senhor, o Deus dos Exércitos, o Deus de Israel: Eis que trarei sobre Judá e sobre todos os moradores de Jerusalém todo o mal que falei contra eles; pois lhes tenho falado, e não me obedeceram, clamei a eles, e não responderam.
18 À casa dos recabitas disse Jeremias: Assim diz o Senhor dos Exércitos, o Deus de Israel: Pois que obedecestes ao mandamento de Jonadabe, vosso pai, e guardastes todos os seus preceitos, e tudo fizestes segundo vos ordenou,
19 por isso, assim diz o Senhor dos Exércitos, o Deus de Israel: Nunca faltará homem a Jonadabe, filho de Recabe, que esteja na minha presença.*
1 No quarto ano de Jeoaquim, filho de Josias, rei de Judá, veio esta palavra do Senhor a Jeremias, dizendo:
2 Toma um rolo, um livro, e escreve nele todas as palavras que te falei contra Israel, contra Judá e contra todas as nações, desde o dia em que te falei, desde os dias de Josias até hoje.
3 Talvez ouçam os da casa de Judá todo o mal que eu intento fazer-lhes e venham a converter-se cada um do seu mau caminho, e eu lhes perdoe a iniquidade e o pecado.
4 Então, Jeremias chamou a Baruque, filho de Nerias; escreveu Baruque no rolo, segundo o que ditou Jeremias, todas as palavras que a este o Senhor havia revelado.
5 Jeremias ordenou a Baruque, dizendo: Estou encarcerado; não posso entrar na Casa do Senhor.
6 Entra, pois, tu e, do rolo que escreveste, segundo o que eu ditei, lê todas as palavras do Senhor, diante do povo, na Casa do Senhor, no dia de jejum; e também as lerás diante de todos os de Judá que vêm das suas cidades.
7 Pode ser que as suas humildes súplicas sejam bem-acolhidas pelo Senhor, e cada um se converta do seu mau caminho; porque grande é a ira e o furor que o Senhor tem manifestado contra este povo.
8 Fez Baruque, filho de Nerias, segundo tudo quanto lhe havia ordenado Jeremias, o profeta, e leu naquele livro as palavras do Senhor, na Casa do Senhor.
9 No quinto ano de Jeoaquim, filho de Josias, rei de Judá, no mês nono, apregoaram jejum diante do Senhor a todo o povo em Jerusalém, como também a todo o povo que vinha das cidades de Judá a Jerusalém.
10 Leu, pois, Baruque naquele livro as palavras de Jeremias na Casa do Senhor, na câmara de Gemarias, filho de Safã, o escriba, no átrio superior, à entrada da Porta Nova da Casa do Senhor, diante de todo o povo.
11 Ouvindo Micaías, filho de Gemarias, filho de Safã, todas as palavras do Senhor, naquele livro,
12 desceu à casa do rei, à câmara do escrivão. Eis que todos os príncipes estavam ali assentados: Elisama, o escrivão, Delaías, filho de Semaías, Elnatã, filho de Acbor, Gemarias, filho de Safã, Zedequias, filho de Hananias, e todos os outros príncipes.
13 Micaías anunciou-lhes todas as palavras que ouvira, quando Baruque leu o livro diante do povo.
14 Então, todos os príncipes mandaram Jeudi, filho de Netanias, filho de Selemias, filho de Cusi, dizer a Baruque: O rolo que leste diante do povo, toma-o contigo e vem. Baruque, filho de Nerias, tomou o rolo consigo e veio ter com eles.
15 Disseram-lhe: Assenta-te, agora, e lê-o para nós. E Baruque o leu diante deles.
16 Tendo eles ouvido todas aquelas palavras, entreolharam-se atemorizados e disseram a Baruque: Sem dúvida nenhuma, anunciaremos ao rei todas estas palavras.
17 E perguntaram a Baruque, dizendo: Declara-nos, como escreveste isto? Acaso, te ditou o profeta todas estas palavras?
18 Respondeu-lhes Baruque: Ditava-me pessoalmente todas estas palavras, e eu as escrevia no livro com tinta.
19 Então, disseram os príncipes a Baruque: Vai, esconde-te, tu e Jeremias; ninguém saiba onde estais.
20 Foram os príncipes ter com o rei ao átrio, depois de terem depositado o rolo na câmara de Elisama, o escrivão, e anunciaram diante do rei todas aquelas palavras.
21 Então, enviou o rei a Jeudi, para que trouxesse o rolo; Jeudi tomou-o da câmara de Elisama, o escrivão, e o leu diante do rei e de todos os príncipes que estavam com ele.
22 O rei estava assentado na casa de inverno, pelo nono mês, e diante dele estava um braseiro aceso.
23 Tendo Jeudi lido três ou quatro folhas do livro, cortou-o o rei com um canivete de escrivão e o lançou no fogo que havia no braseiro, e, assim, todo o rolo se consumiu no fogo que estava no braseiro.
24 Não se atemorizaram, não rasgaram as vestes, nem o rei nem nenhum dos seus servos que ouviram todas aquelas palavras.
25 Posto que Elnatã, Delaías e Gemarias tinham insistido com o rei que não queimasse o rolo, ele não lhes deu ouvidos.
26 Antes, deu ordem o rei a Jerameel, filho de Hameleque, a Seraías, filho de Azriel, e a Selemias, filho de Abdeel, que prendessem a Baruque, o escrivão, e a Jeremias, o profeta; mas o Senhor os havia escondido.
27 Então, veio a Jeremias a palavra do Senhor, depois que o rei queimara o rolo com as palavras que Baruque escrevera ditadas por Jeremias, dizendo:
28 Toma outro rolo e escreve nele todas as palavras que estavam no original, que Jeoaquim, rei de Judá, queimou.
29 E a Jeoaquim, rei de Judá, dirás: Assim diz o Senhor: Tu queimaste aquele rolo, dizendo: Por que escreveste nele que certamente viria o rei da Babilônia, e destruiria esta terra, e acabaria com homens e animais dela?
30 Portanto, assim diz o Senhor, acerca de Jeoaquim, rei de Judá: Ele não terá quem se assente no trono de Davi, e o seu cadáver será largado ao calor do dia e à geada da noite.
31 Castigá-lo-ei, e à sua descendência, e aos seus servos por causa da iniquidade deles; sobre ele, sobre os moradores de Jerusalém e sobre os homens de Judá farei cair todo o mal que tenho falado contra eles, e não ouviram.
32 Tomou, pois, Jeremias outro rolo e o deu a Baruque, filho de Nerias, o escrivão, o qual escreveu nele, ditado por Jeremias, todas as palavras do livro que Jeoaquim, rei de Judá, queimara; e ainda se lhes acrescentaram muitas palavras semelhantes.*
1 Zedequias, filho de Josias e a quem Nabucodonosor, rei da Babilônia, constituíra rei na terra de Judá, reinou em lugar de Conias, filho de Jeoaquim.
2 Mas nem ele, nem os seus servos, nem o povo da terra deram ouvidos às palavras do Senhor que falou por intermédio de Jeremias, o profeta.
3 Contudo, mandou o rei Zedequias a Jucal, filho de Selemias, e ao sacerdote Sofonias, filho de Maaseias, ao profeta Jeremias, para lhe dizerem: Roga por nós ao Senhor, nosso Deus.
4 Jeremias andava livremente entre o povo, porque ainda o não haviam encarcerado.
5 O exército de Faraó saíra do Egito; e, quando os caldeus, que sitiavam Jerusalém, ouviram esta notícia, retiraram-se dela.
6 Então, veio a Jeremias, o profeta, a palavra do Senhor:
7 Assim diz o Senhor, Deus de Israel: Assim direis ao rei de Judá, que vos enviou a mim, para me consultar: Eis que o exército de Faraó, que saiu em vosso socorro, voltará para a sua terra, no Egito.
8 Retornarão os caldeus, pelejarão contra esta cidade, tomá-la-ão e a queimarão.
9 Assim diz o Senhor: Não vos enganeis a vós mesmos, dizendo: Sem dúvida, se irão os caldeus de nós; pois, de fato, não se retirarão.
10 Porque, ainda que derrotásseis a todo o exército dos caldeus, que pelejam contra vós outros, e ficassem deles apenas homens mortalmente feridos, cada um se levantaria na sua tenda e queimaria esta cidade.
11 Tendo-se retirado o exército dos caldeus de Jerusalém, por causa do exército de Faraó,
12 saiu Jeremias de Jerusalém, a fim de ir à terra de Benjamim, para receber o quinhão de uma herança que tinha no meio do povo.
13 Estando ele à Porta de Benjamim, achava-se ali um capitão da guarda, cujo nome era Jerias, filho de Selemias, filho de Hananias, capitão que prendeu a Jeremias, o profeta, dizendo: Tu foges para os caldeus.
14 Disse Jeremias: É mentira, não fujo para os caldeus. Mas Jerias não lhe deu ouvidos; prendeu a Jeremias e o levou aos príncipes.
15 Os príncipes, irados contra Jeremias, açoitaram-no e o meteram no cárcere, na casa de Jônatas, o escrivão, porque a tinham transformado em cárcere.
16 Tendo Jeremias entrado nas celas do calabouço, ali ficou muitos dias.
17 Mandou o rei Zedequias trazê-lo para sua casa e, em secreto, lhe perguntou: Há alguma palavra do Senhor? Respondeu Jeremias: Há. Disse ainda: Nas mãos do rei da Babilônia serás entregue.
18 Disse mais Jeremias ao rei Zedequias: Em que pequei contra ti, ou contra os teus servos, ou contra este povo, para que me pusesses na prisão?
19 Onde estão agora os vossos profetas, que vos profetizavam, dizendo: O rei da Babilônia não virá contra vós outros, nem contra esta terra?
20 Agora, pois, ouve, ó rei, meu senhor: Que a minha humilde súplica seja bem-acolhida por ti, e não me deixes tornar à casa de Jônatas, o escrivão, para que eu não venha a morrer ali.
21 Então, ordenou o rei Zedequias que pusessem a Jeremias no átrio da guarda; e, cada dia, deram-lhe um pão da Rua dos Padeiros, até acabar-se todo pão da cidade. Assim ficou Jeremias no átrio da guarda.*
1 Ouviu, pois, Sefatias, filho de Matã, e Gedalias, filho de Pasur, e Jucal, filho de Selemias, e Pasur, filho de Malquias, as palavras que Jeremias anunciava a todo o povo, dizendo:
2 Assim diz o Senhor: O que ficar nesta cidade morrerá à espada, à fome e de peste; mas o que passar para os caldeus viverá; porque a vida lhe será como despojo, e viverá.
3 Assim diz o Senhor: Esta cidade infalivelmente será entregue nas mãos do exército do rei da Babilônia, e este a tomará.
4 Disseram os príncipes ao rei: Morra este homem, visto que ele, dizendo assim estas palavras, afrouxa as mãos dos homens de guerra que restam nesta cidade e as mãos de todo o povo; porque este homem não procura o bem-estar para o povo, e sim o mal.
5 Disse o rei Zedequias: Eis que ele está nas vossas mãos; pois o rei nada pode contra vós outros.
6 Tomaram, então, a Jeremias e o lançaram na cisterna de Malquias, filho do rei, que estava no átrio da guarda; desceram a Jeremias com cordas. Na cisterna não havia água, senão lama; e Jeremias se atolou na lama.
7 Ouviu Ebede-Meleque, o etíope, eunuco que estava na casa do rei, que tinham metido a Jeremias na cisterna; ora, estando o rei assentado à Porta de Benjamim,
8 saiu Ebede-Meleque da casa do rei e lhe falou:
9 Ó rei, senhor meu, agiram mal estes homens em tudo quanto fizeram a Jeremias, o profeta, que lançaram na cisterna; no lugar onde se acha, morrerá de fome, pois já não há pão na cidade.
10 Então, deu ordem o rei a Ebede-Meleque, o etíope, dizendo: Toma contigo daqui trinta homens e tira da cisterna o profeta Jeremias, antes que morra.
11 Tomou Ebede-Meleque os homens consigo, e foi à casa do rei, por debaixo da tesouraria, e tomou dali umas roupas usadas e trapos, e os desceu a Jeremias na cisterna, por meio de cordas.
12 Disse Ebede-Meleque, o etíope, a Jeremias: Põe agora estas roupas usadas e estes trapos nas axilas, calçando as cordas; Jeremias o fez.
13 Puxaram a Jeremias com as cordas e o tiraram da cisterna; e Jeremias ficou no átrio da guarda.
14 Então, o rei Zedequias mandou trazer o profeta Jeremias à sua presença, à terceira entrada na Casa do Senhor, e lhe disse: Quero perguntar-te uma coisa, nada me encubras.
15 Disse Jeremias a Zedequias: Se eu ta disser, porventura, não me matarás? Se eu te aconselhar, não me atenderás.
16 Então, Zedequias jurou secretamente a Jeremias, dizendo: Tão certo como vive o Senhor, que nos deu a vida, não te matarei, nem te entregarei nas mãos desses homens que procuram tirar-te a vida.
17 Então, Jeremias disse a Zedequias: Assim diz o Senhor, o Deus dos Exércitos, Deus de Israel: Se te renderes voluntariamente aos príncipes do rei da Babilônia, então, viverá tua alma, e esta cidade não se queimará, e viverás tu e a tua casa.
18 Mas, se não te renderes aos príncipes do rei da Babilônia, então, será entregue esta cidade nas mãos dos caldeus, e eles a queimarão, e tu não escaparás das suas mãos.
19 Disse o rei Zedequias a Jeremias: Receio-me dos judeus que se passaram para os caldeus; não suceda que estes me entreguem nas mãos deles, e eles escarneçam de mim.
20 Disse Jeremias: Não te entregarão; ouve, te peço, a palavra do Senhor, segundo a qual eu te falo; e bem te irá, e será poupada a tua vida.
21 Mas, se não quiseres sair, esta é a palavra que me revelou o Senhor:
22 Eis que todas as mulheres que ficaram na casa do rei de Judá serão levadas aos príncipes do rei da Babilônia, e elas mesmas dirão: Os teus bons amigos te enganaram e prevaleceram contra ti; mas, agora que se atolaram os teus pés na lama, voltaram atrás.
23 Assim, a todas as tuas mulheres e a teus filhos levarão aos caldeus, e tu não escaparás das suas mãos; antes, pela mão do rei da Babilônia serás preso; e por tua culpa esta cidade será queimada.
24 Então, disse Zedequias a Jeremias: Ninguém saiba estas palavras, e não morrerás.
25 Quando, ouvindo os príncipes que falei contigo, vierem a ti e te disserem: Declara-nos agora o que disseste ao rei e o que ele te disse a ti, nada nos encubras, e não te mataremos,
26 então, lhes dirás: Apresentei a minha humilde súplica diante do rei para que não me fizesse tornar à casa de Jônatas, para morrer ali.
27 Vindo, pois, todos os príncipes a Jeremias, e, interrogando-o, declarou-lhes segundo todas as palavras que o rei lhe havia ordenado; e o deixaram em paz, porque da conversação nada transpirara.
28 Ficou Jeremias no átrio da guarda, até ao dia em que foi tomada Jerusalém.*
1 Foi tomada Jerusalém. Era o ano nono de Zedequias, rei de Judá, no mês décimo, quando veio Nabucodonosor, rei da Babilônia, e todo o seu exército, contra Jerusalém, e a cercaram;
2 era o undécimo ano de Zedequias, no quarto mês, aos nove do mês, quando se fez uma brecha na cidade.
3 Então, entraram todos os príncipes do rei da Babilônia e se assentaram na Porta do Meio: Nergal-Sarezer, Sangar-Nebo, Sarsequim, Rabe-Saris, Nergal-Sarezer, Rabe-Mague e todos os outros príncipes do rei da Babilônia.
4 Tendo-os visto Zedequias, rei de Judá, e todos os homens de guerra, fugiram e, de noite, saíram da cidade, pelo caminho do jardim do rei, pela porta que está entre os dois muros; Zedequias saiu pelo caminho da campina.
5 Mas o exército dos caldeus os perseguiu e alcançou a Zedequias nas campinas de Jericó; eles o prenderam e o fizeram subir a Ribla, na terra de Hamate, a Nabucodonosor, rei da Babilônia, que lhe pronunciou a sentença.
6 O rei da Babilônia mandou matar, em Ribla, os filhos de Zedequias à vista deste; também matou a todos os príncipes de Judá.
7 Vazou os olhos a Zedequias e o atou com duas cadeias de bronze, para o levar à Babilônia.
8 Os caldeus queimaram a casa do rei e as casas do povo e derribaram os muros de Jerusalém.
9 O mais do povo que havia ficado na cidade, os desertores que se entregaram a ele e o sobrevivente do povo, Nebuzaradã, o chefe da guarda, levou-os cativos para a Babilônia.
10 Porém dos mais pobres da terra, que nada tinham, deixou Nebuzaradã, o chefe da guarda, na terra de Judá; e lhes deu vinhas e campos naquele dia.
11 Mas Nabucodonosor, rei da Babilônia, havia ordenado acerca de Jeremias, a Nebuzaradã, o chefe da guarda, dizendo:
12 Toma-o, cuida dele e não lhe faças nenhum mal; mas faze-lhe como ele te disser.
13 Deste modo, Nebuzaradã, o chefe da guarda, ordenou a Nebusazbã, Rabe-Saris, Nergal-Sarezer, Rabe-Mague, e todos os príncipes do rei da Babilônia
14 mandaram retirar Jeremias do átrio da guarda e o entregaram a Gedalias, filho de Aicão, filho de Safã, para que o levasse para o seu palácio; assim, habitou entre o povo.
15 Ora, tinha vindo a Jeremias a palavra do Senhor, estando ele ainda detido no átrio da guarda, dizendo:
16 Vai e fala a Ebede-Meleque, o etíope, dizendo: Assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que eu trarei as minhas palavras sobre esta cidade para mal e não para bem; e se cumprirão diante de ti naquele dia.
17 A ti, porém, eu livrarei naquele dia, diz o Senhor, e não serás entregue nas mãos dos homens a quem temes.
18 Pois certamente te salvarei, e não cairás à espada, porque a tua vida te será como despojo, porquanto confiaste em mim.*
1 Palavra que veio a Jeremias da parte do Senhor, depois que Nebuzaradã, o chefe da guarda, o pôs em liberdade em Ramá, estando ele atado com cadeias no meio de todos os do cativeiro de Jerusalém e de Judá, que foram levados cativos para a Babilônia.
2 Tomou o chefe da guarda a Jeremias e lhe disse: O Senhor, teu Deus, pronunciou este mal contra este lugar;
3 o Senhor o trouxe e fez como tinha dito. Porque pecastes contra o Senhor e não obedecestes à sua voz, tudo isto vos sucedeu.
4 Agora, pois, eis que te livrei hoje das cadeias que estavam sobre as tuas mãos. Se te apraz vir comigo para a Babilônia, vem, e eu cuidarei bem de ti; mas, se não te apraz vir comigo para a Babilônia, deixa de vir. Olha, toda a terra está diante de ti; para onde julgares bom e próprio ir, vai para aí.
5 Mas, visto que ele tardava em decidir-se, o capitão lhe disse: Volta a Gedalias, filho de Aicão, filho de Safã, a quem o rei da Babilônia nomeou governador das cidades de Judá, e habita com ele no meio do povo; ou, se para qualquer outra parte te aprouver ir, vai. Deu-lhe o chefe da guarda mantimento e um presente e o deixou ir.
6 Assim, foi Jeremias a Gedalias, filho de Aicão, a Mispa; e habitou com ele no meio do povo que havia ficado na terra.
7 Ouvindo, pois, os capitães dos exércitos que estavam no campo, eles e seus homens, que o rei da Babilônia nomeara governador da terra a Gedalias, filho de Aicão, e que lhe havia confiado os homens, as mulheres, os meninos e os mais pobres da terra que não foram levados ao exílio, para a Babilônia,
8 vieram ter com ele a Mispa, a saber: Ismael, filho de Netanias, Joanã e Jônatas, filhos de Careá, Seraías, filho de Tanumete, os filhos de Efai, o netofatita, Jezanias, filho do maacatita, eles e os seus homens.
9 Gedalias, filho de Aicão, filho de Safã, jurou a eles e aos seus homens e lhes disse: Nada temais da parte dos caldeus; ficai na terra, servi ao rei da Babilônia, e bem vos irá.
10 Quanto a mim, eis que habito em Mispa, para estar às ordens dos caldeus que vierem a nós; vós, porém, colhei o vinho, as frutas de verão e o azeite, metei-os nas vossas vasilhas e habitai nas vossas cidades que tomastes.
11 Da mesma sorte, todos os judeus que estavam em Moabe, entre os filhos de Amom e em Edom e os que havia em todas aquelas terras ouviram que o rei da Babilônia havia deixado um resto de Judá e que havia nomeado governador sobre eles a Gedalias, filho de Aicão, filho de Safã;
12 então, voltaram todos eles de todos os lugares para onde foram lançados e vieram à terra de Judá, a Gedalias, a Mispa; e colheram vinho e frutas de verão em muita abundância.
13 Joanã, filho de Careá, e todos os príncipes dos exércitos que estavam no campo vieram a Gedalias, a Mispa,
14 e lhe disseram: Sabes tu que Baalis, rei dos filhos de Amom, enviou a Ismael, filho de Netanias, para tirar-te a vida? Mas Gedalias, filho de Aicão, não lhes deu crédito.
15 Todavia, Joanã, filho de Careá, disse a Gedalias em segredo, em Mispa: Irei agora e matarei a Ismael, filho de Netanias, sem que ninguém o saiba; por que razão tiraria ele a tua vida, de maneira que todo o Judá que se tem congregado a ti fosse disperso, e viesse a perecer o resto de Judá?
16 Mas disse Gedalias, filho de Aicão, a Joanã, filho de Careá: Não faças tal coisa, porque isso que falas contra Ismael é falso.*
1 Sucedeu, porém, que, no sétimo mês, veio Ismael, filho de Netanias, filho de Elisama, de família real, e dez homens, capitães do rei, com ele, a Gedalias, filho de Aicão, a Mispa; e ali comeram pão juntos, em Mispa.
2 Dispuseram-se Ismael, filho de Netanias, e os dez homens que estavam com ele e feriram à espada a Gedalias, filho de Aicão, filho de Safã, matando, assim, aquele que o rei da Babilônia nomeara governador da terra.
3 Também matou Ismael a todos os judeus que estavam com Gedalias, em Mispa, como também aos caldeus, homens de guerra, que se achavam ali.
4 Sucedeu no dia seguinte ao em que ele matara a Gedalias, sem ninguém o saber,
5 que vieram homens de Siquém, de Siló e de Samaria; oitenta homens, com a barba rapada, as vestes rasgadas e o corpo retalhado, trazendo consigo ofertas de manjares e incenso, para levarem à Casa do Senhor.
6 Saindo-lhes ao encontro Ismael, filho de Netanias, de Mispa, ia chorando; ao encontrá-los, lhes disse: Vinde a Gedalias, filho de Aicão.
7 Vindo eles, porém, até ao meio da cidade, matou-os Ismael, filho de Netanias, ele e os que estavam com ele, e os lançaram num poço.
8 Mas houve dentre eles dez homens que disseram a Ismael: Não nos mates a nós, porque temos depósitos de trigo, cevada, azeite e mel escondidos no campo. Por isso, ele desistiu e não os matou como aos outros.
9 O poço em que Ismael lançou todos os cadáveres dos homens que ferira além de Gedalias é o mesmo que fez o rei Asa, na sua defesa contra Baasa, rei de Israel; foi esse mesmo que encheu de mortos Ismael, filho de Netanias.
10 Ismael levou cativo a todo o resto do povo que estava em Mispa, isto é, as filhas do rei e todo o povo que ficara em Mispa, que Nebuzaradã, o chefe da guarda, havia confiado a Gedalias, filho de Aicão; levou-os cativos Ismael, filho de Netanias; e se foi para passar aos filhos de Amom.
11 Ouvindo, pois, Joanã, filho de Careá, e todos os príncipes dos exércitos que estavam com ele todo o mal que havia feito Ismael, filho de Netanias,
12 tomaram consigo a todos os seus homens e foram pelejar contra Ismael, filho de Netanias; acharam-no junto às grandes águas que há em Gibeão.
13 Ora, todo o povo que estava com Ismael se alegrou quando viu a Joanã, filho de Careá, e a todos os príncipes dos exércitos que vinham com ele.
14 Todo o povo que Ismael levara cativo de Mispa virou as costas, voltou e foi para Joanã, filho de Careá.
15 Mas Ismael, filho de Netanias, escapou de Joanã com oito homens e se foi para os filhos de Amom.
16 Tomou, então, Joanã, filho de Careá, e todos os príncipes dos exércitos que estavam com ele a todo o restante do povo que Ismael, filho de Netanias, levara cativo de Mispa, depois de ter ferido a Gedalias, filho de Aicão, isto é, os homens valentes de guerra, as mulheres, os meninos e os eunucos que havia recobrado de Gibeão;
17 partiram e pararam em Gerute-Quimã, que está perto de Belém, para dali entrarem no Egito,
18 por causa dos caldeus; porque os temiam, por ter Ismael, filho de Netanias, ferido a Gedalias, filho de Aicão, a quem o rei da Babilônia nomeara governador da terra.*
1 Então, chegaram todos os capitães dos exércitos, e Joanã, filho de Careá, e Jezanias, filho de Hosaías, e todo o povo, desde o menor até ao maior,
2 e disseram a Jeremias, o profeta: Apresentamos-te a nossa humilde súplica, a fim de que rogues ao Senhor, teu Deus, por nós e por este resto; porque, de muitos que éramos, só restamos uns poucos, como vês com os teus próprios olhos;
3 a fim de que o Senhor, teu Deus, nos mostre o caminho por onde havemos de andar e aquilo que havemos de fazer.
4 Respondeu-lhes Jeremias, o profeta: Já vos ouvi; eis que orarei ao Senhor, vosso Deus, segundo o vosso pedido. Tudo o que o Senhor vos responder, eu vo-lo declararei; não vos ocultarei nada.
5 Então, eles disseram a Jeremias: Seja o Senhor testemunha verdadeira e fiel contra nós, se não fizermos segundo toda a palavra com que o Senhor, teu Deus, te enviar a nós outros.
6 Seja ela boa ou seja má, obedeceremos à voz do Senhor, nosso Deus, a quem te enviamos, para que nos suceda bem ao obedecermos à voz do Senhor, nosso Deus.
7 Ao fim de dez dias, veio a palavra do Senhor a Jeremias.
8 Então, chamou a Joanã, filho de Careá, e a todos os capitães dos exércitos que havia com ele, e a todo o povo, desde o menor até ao maior,
9 e lhes disse: Assim diz o Senhor, Deus de Israel, a quem me enviastes para apresentar a vossa súplica diante dele:
10 Se permanecerdes nesta terra, então, vos edificarei e não vos derribarei; plantar-vos-ei e não vos arrancarei, porque estou arrependido do mal que vos tenho feito.
11 Não temais o rei da Babilônia, a quem vós temeis; não o temais, diz o Senhor, porque eu sou convosco, para vos salvar e vos livrar das suas mãos.
12 Eu vos serei propício, para que ele tenha misericórdia de vós e vos faça morar em vossa terra.
13 Mas, se vós disserdes: Não ficaremos nesta terra, não obedecendo à voz do Senhor, vosso Deus,
14 dizendo: Não; antes, iremos à terra do Egito, onde não veremos guerra, nem ouviremos som de trombeta, nem teremos fome de pão, e ali ficaremos,
15 nesse caso, ouvi a palavra do Senhor, ó resto de Judá. Assim diz o Senhor dos Exércitos, o Deus de Israel: Se tiverdes o firme propósito de entrar no Egito e fordes para morar,
16 acontecerá, então, que a espada que vós temeis vos alcançará na terra do Egito, e a fome que receais vos seguirá de perto os passos no Egito, onde morrereis.
17 Assim será com todos os homens que tiverem o propósito de entrar no Egito para morar: morrerão à espada, à fome e de peste; não restará deles nem um, nem escapará do mal que farei vir sobre eles.
18 Porque assim diz o Senhor dos Exércitos, o Deus de Israel: Como se derramou a minha ira e o meu furor sobre os habitantes de Jerusalém, assim se derramará a minha indignação sobre vós, quando entrardes no Egito; sereis objeto de maldição, de espanto, de desprezo e opróbrio e não vereis mais este lugar.
19 Falou-vos o Senhor, ó resto de Judá: Não entreis no Egito; tende por certo que vos adverti hoje.
20 Porque vós, à custa da vossa vida, a vós mesmos vos enganastes, pois me enviastes ao Senhor, vosso Deus, dizendo: Ora por nós ao Senhor, nosso Deus; e, segundo tudo o que disser o Senhor, nosso Deus, declara-no-lo assim, e o faremos;
21 mas, tendo-vos declarado isso hoje, não destes ouvidos à voz do Senhor, vosso Deus, em coisa alguma pela qual ele me enviou a vós outros.
22 Agora, pois, sabei por certo que morrereis à espada, à fome e de peste no mesmo lugar aonde desejastes ir para morar.*
1 Tendo Jeremias acabado de falar a todo o povo todas as palavras do Senhor, seu Deus, palavras todas com as quais o Senhor, seu Deus, o enviara,
2 então, falou Azarias, filho de Hosaías, e Joanã, filho de Careá, e todos os homens soberbos, dizendo a Jeremias: É mentira isso que dizes; o Senhor, nosso Deus, não te enviou a dizer: Não entreis no Egito, para morar.
3 Baruque, filho de Nerias, é que te incita contra nós, para nos entregar nas mãos dos caldeus, a fim de nos matarem ou nos exilarem na Babilônia.
4 Não obedeceu, pois, Joanã, filho de Careá, e nenhum de todos os capitães dos exércitos, nem o povo todo à voz do Senhor, para ficarem na terra de Judá.
5 Antes, tomaram Joanã, filho de Careá, e todos os capitães dos exércitos a todo o resto de Judá que havia voltado dentre todas as nações para as quais haviam sido lançados, para morar na terra de Judá;
6 tomaram aos homens, às mulheres e aos meninos, às filhas do rei e a todos que Nebuzaradã, o chefe da guarda, deixara com Gedalias, filho de Aicão, filho de Safã; como também a Jeremias, o profeta, e a Baruque, filho de Nerias;
7 e entraram na terra do Egito, porque não obedeceram à voz do Senhor, e vieram até Tafnes.
8 Então, veio a palavra do Senhor a Jeremias, em Tafnes, dizendo:
9 Toma contigo pedras grandes, encaixa-as na argamassa do pavimento que está à entrada da casa de Faraó, em Tafnes, à vista de homens judeus,
10 e dize-lhes: Assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que eu mandarei vir a Nabucodonosor, rei da Babilônia, meu servo, e porei o seu trono sobre estas pedras que encaixei; ele estenderá o seu baldaquino real sobre elas.
11 Virá e ferirá a terra do Egito; quem é para a morte, para a morte; quem é para o cativeiro, para o cativeiro; e quem é para a espada, para a espada.
12 Lançará fogo às casas dos deuses do Egito e as queimará; levará cativos os ídolos e despiolhará a terra do Egito, como o pastor despiolha a sua própria veste; e sairá dali em paz.
13 Quebrará as colunas de Bete-Semes na terra do Egito e queimará as casas dos deuses do Egito.*
1 Palavra que veio a Jeremias, acerca de todos os judeus moradores da terra do Egito, em Migdol, em Tafnes, em Mênfis e na terra de Patros, dizendo:
2 Assim diz o Senhor dos Exércitos, Deus de Israel: Vistes todo o mal que fiz cair sobre Jerusalém e sobre todas as cidades de Judá; e eis que hoje são elas uma desolação, e ninguém habita nelas,
3 por causa da maldade que fizeram, para me irarem, indo queimar incenso e servir a outros deuses que eles nunca conheceram, eles, vós e vossos pais.
4 Todavia, começando eu de madrugada, lhes enviei os meus servos, os profetas, para lhes dizer: Não façais esta coisa abominável que aborreço.
5 Mas eles não obedeceram, nem inclinaram os ouvidos para se converterem da sua maldade, para não queimarem incenso a outros deuses.
6 Derramou-se, pois, a minha indignação e a minha ira, acenderam-se nas cidades de Judá e nas ruas de Jerusalém, que se tornaram em deserto e em assolação, como hoje se vê.
7 Agora, pois, assim diz o Senhor, Deus dos Exércitos, o Deus de Israel: Por que fazeis vós tão grande mal contra vós mesmos, eliminando homens e mulheres, crianças e aqueles que mamam do meio de Judá, a fim de que não vos fique resto algum?
8 Por que me irritais com as obras de vossas mãos, queimando incenso a outros deuses na terra do Egito, aonde viestes para morar, para que a vós mesmos vos elimineis e para que vos torneis objeto de desprezo e de opróbrio entre todas as nações da terra?
9 Esquecestes já as maldades de vossos pais, as maldades dos reis de Judá, as maldades das suas mulheres, as vossas maldades e as maldades das vossas mulheres, maldades cometidas na terra de Judá e nas ruas de Jerusalém?
10 Não se humilharam até ao dia de hoje, não temeram, não andaram na minha lei nem nos meus estatutos, que pus diante de vós e diante de vossos pais.
11 Portanto, assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que voltarei o rosto contra vós outros para mal e para eliminar a todo o Judá.
12 Tomarei o resto de Judá que se obstinou em entrar na terra do Egito para morar, onde será ele de todo consumido; cairá à espada e à fome; desde o menor até ao maior perecerão; morrerão à espada e à fome; e serão objeto de maldição, espanto, desprezo e opróbrio.
13 Porque castigarei os que habitam na terra do Egito, como o fiz a Jerusalém, com a espada, a fome e a peste,
14 de maneira que, dos restantes de Judá que vieram à terra do Egito para morar, não haverá quem escape e sobreviva para tornar à terra de Judá, à qual desejam voltar para morar; mas não tornarão senão alguns fugitivos.
15 Então, responderam a Jeremias todos os homens que sabiam que suas mulheres queimavam incenso a outros deuses e todas as mulheres que se achavam ali em pé, grande multidão, como também todo o povo que habitava na terra do Egito, em Patros, dizendo:
16 Quanto à palavra que nos anunciaste em nome do Senhor, não te obedeceremos a ti;
17 antes, certamente, toda a palavra que saiu da nossa boca, isto é, queimaremos incenso à Rainha dos Céus e lhe ofereceremos libações, como nós, nossos pais, nossos reis e nossos príncipes temos feito, nas cidades de Judá e nas ruas de Jerusalém; tínhamos fartura de pão, prosperávamos e não víamos mal algum.
18 Mas, desde que cessamos de queimar incenso à Rainha dos Céus e de lhe oferecer libações, tivemos falta de tudo e fomos consumidos pela espada e pela fome.
19 Quando queimávamos incenso à Rainha dos Céus e lhe oferecíamos libações, acaso, lhe fizemos bolos que a retratavam e lhe oferecemos libações, sem nossos maridos?
20 Então, disse Jeremias a todo o povo, aos homens e às mulheres, a todo o povo que lhe tinha dado esta resposta, dizendo:
21 Quanto ao incenso que queimastes nas cidades de Judá e nas ruas de Jerusalém, vós e vossos pais, os vossos reis e os vossos príncipes e o povo da terra, acaso, não se lembrou disso o Senhor, nem lhe andou isso pela mente?
22 O Senhor já não podia por mais tempo sofrer a maldade das vossas obras, as abominações que cometestes; pelo que a vossa terra se tornou deserta, um objeto de espanto e de desprezo e desabitada, como hoje se vê.
23 Pois queimastes incenso e pecastes contra o Senhor, não obedecestes à voz do Senhor e na sua lei e nos seus testemunhos não andastes; por isso, vos sobreveio este mal, como hoje se vê.
24 Disse mais Jeremias a todo o povo e a todas as mulheres: Ouvi a palavra do Senhor, vós, todo o Judá, que estais na terra do Egito:
25 Assim fala o Senhor dos Exércitos, o Deus de Israel, dizendo: Vós e vossas mulheres não somente fizestes por vossa boca, senão também que cumpristes por vossas mãos os vossos votos, a saber: Certamente cumpriremos os nossos votos, que fizemos, de queimar incenso à Rainha dos Céus e de lhe oferecer libações. Confirmai, pois, perfeitamente, os vossos votos, sim, cumpri-os.
26 Portanto, ouvi a palavra do Senhor, vós, todo o Judá, que habitais na terra do Egito: Eis que eu juro pelo meu grande nome, diz o Senhor, que nunca mais será pronunciado o meu nome por boca de qualquer homem de Judá em toda a terra do Egito, dizendo: Tão certo como vive o Senhor Deus.
27 Eis que velarei sobre eles para mal e não para bem; todos os homens de Judá que estão na terra do Egito serão consumidos à espada e à fome, até que se acabem de todo.
28 Os que escaparem da espada tornarão da terra do Egito à terra de Judá, poucos em número; e todos os restantes de Judá que vieram à terra do Egito para morar saberão se subsistirá a minha palavra ou a sua.
29 Isto vos será sinal de que eu vos castigarei neste lugar, diz o Senhor, para que saibais que certamente subsistirão as minhas palavras contra vós outros para mal.
30 Eis o sinal, diz o Senhor: Eu entregarei o Faraó-Hofra, rei do Egito, nas mãos de seus inimigos, nas mãos dos que procuram a sua morte, como entreguei Zedequias, rei de Judá, nas mãos de Nabucodonosor, rei da Babilônia, que era seu inimigo e procurava tirar-lhe a vida.*
1 Palavra que falou Jeremias, o profeta, a Baruque, filho de Nerias, escrevendo ele aquelas palavras num livro, ditadas por Jeremias, no ano quarto de Jeoaquim, filho de Josias, rei de Judá, dizendo:
2 Assim diz o Senhor, Deus de Israel, acerca de ti, ó Baruque:
3 Disseste: Ai de mim agora! Porque me acrescentou o Senhor tristeza ao meu sofrimento; estou cansado do meu gemer e não acho descanso.
4 Assim lhe dirás: Isto diz o Senhor: Eis que estou demolindo o que edifiquei e arrancando o que plantei, e isto em toda a terra.
5 E procuras tu grandezas? Não as procures; porque eis que trarei mal sobre toda carne, diz o Senhor; a ti, porém, eu te darei a tua vida como despojo, em todo lugar para onde fores.*
1 Palavra do Senhor que veio a Jeremias, o profeta, contra as nações.
2 A respeito do Egito. Contra o exército de Faraó-Neco, rei do Egito, exército que estava junto ao rio Eufrates em Carquemis; ao qual feriu Nabucodonosor, rei da Babilônia, no ano quarto de Jeoaquim, filho de Josias, rei de Judá:
3 Preparai o escudo e o pavês e chegai-vos para a peleja.
4 Selai os cavalos, montai, cavaleiros, e apresentai-vos com elmos; poli as lanças, vesti-vos de couraças.
5 Por que razão vejo os medrosos voltando as costas? Estão derrotados os seus valentes e vão fugindo, sem olhar para trás; há terror ao redor, diz o Senhor.
6 Não fuja o ligeiro, nem escape o valente; para o lado do Norte, junto à borda do rio Eufrates, tropeçaram e caíram.
7 Quem é este que vem subindo como o Nilo, como rios cujas águas se agitam?
8 O Egito vem subindo como o Nilo, como rios cujas águas se agitam; ele disse: Subirei, cobrirei a terra, destruirei a cidade e os que habitam nela.
9 Avançai, ó cavaleiros, estrondeai, ó carros, e saiam os valentes; os etíopes e os de Pute, que manejam o escudo, e os lídios, que manejam e entesam o arco.
10 Porque este dia é o Dia do Senhor, o Senhor dos Exércitos, dia de vingança contra os seus adversários; a espada devorará, fartar-se-á e se embriagará com o sangue deles; porque o Senhor, o Senhor dos Exércitos tem um sacrifício na terra do Norte, junto ao rio Eufrates.
11 Sobe a Gileade e toma bálsamo, ó virgem filha do Egito; debalde multiplicas remédios, pois não há remédio para curar-te.
12 As nações ouviram falar da tua vergonha, e a terra está cheia do teu clamor; porque, fugindo o valente, tropeçou no valente, e ambos caíram juntos.
13 Palavra que falou o Senhor a Jeremias, o profeta, acerca da vinda de Nabucodonosor, rei da Babilônia, para ferir a terra do Egito:
14 Anunciai no Egito e fazei ouvir isto em Migdol; fazei também ouvi-lo em Mênfis e em Tafnes; dizei: Apresenta-te e prepara-te; porque a espada já devorou o que está ao redor de ti.
15 Por que foi derribado o teu Touro? Não se pôde ter de pé, porque o Senhor o abateu.
16 O Senhor multiplicou os que tropeçavam; também caíram uns sobre os outros e disseram: Levanta-te, e voltemos ao nosso povo e à terra do nosso nascimento, por causa da espada que oprime.
17 Ali, apelidarão a Faraó, rei do Egito, de Espalhafatoso, porque deixou passar o tempo adequado.
18 Tão certo como vivo eu, diz o Rei, cujo nome é Senhor dos Exércitos, certamente, como o Tabor é entre os montes e o Carmelo junto ao mar, assim ele virá.
19 Prepara a tua bagagem para o exílio, ó moradora, filha do Egito; porque Mênfis se tornará em desolação e ficará arruinada e sem moradores.
20 Novilha mui formosa é o Egito; mas mutuca do Norte já lhe vem, sim, vem.
21 Até os seus soldados mercenários no meio dele, bezerros cevados, viraram as costas e fugiram juntos; não resistiram, porque veio sobre eles o dia da sua ruína e o tempo do seu castigo.
22 Faz o Egito um ruído como o da serpente que foge, porque os seus inimigos vêm contra ele, com machados, quais derribadores de árvores.
23 Cortarão o seu bosque, diz o Senhor, ainda que impenetrável; porque se multiplicaram mais do que os gafanhotos; são inumeráveis.
24 A filha do Egito está envergonhada; foi entregue nas mãos do povo do Norte.
25 Diz o Senhor dos Exércitos, o Deus de Israel: Eis que eu castigarei a Amom de Nô, a Faraó, ao Egito, aos deuses e aos seus reis, ao próprio Faraó e aos que confiam nele.
26 Entregá-los-ei nas mãos dos que lhes procuram a morte, nas mãos de Nabucodonosor, rei da Babilônia, e nas mãos dos seus servos; mas depois será habitada, como nos dias antigos, diz o Senhor.
27 Não temas, pois, tu, servo meu, Jacó, nem te espantes, ó Israel; porque eu te livrarei do país remoto e a tua descendência, da terra do seu cativeiro; Jacó voltará e ficará tranquilo e confiante; não haverá quem o atemorize.
28 Não temas, servo meu, Jacó, diz o Senhor, porque estou contigo; darei cabo de todas as nações para as quais eu te arrojei; mas de ti não darei cabo; castigar-te-ei, mas em justa medida; não te inocentarei de todo.*
1 Palavra do Senhor que veio a Jeremias, o profeta, a respeito dos filisteus, antes que Faraó ferisse a Gaza.
2 Assim diz o Senhor: Eis que do Norte se levantam as águas, e se tornarão em torrentes transbordantes, e inundarão a terra e a sua plenitude, a cidade e os seus habitantes; clamarão os homens, e todos os moradores da terra se lamentarão,
3 ao ruído estrepitoso das unhas dos seus fortes cavalos, ao barulho de seus carros, ao estrondo das suas rodas. Os pais não atendem aos filhos, por se afrouxarem as suas mãos;
4 por causa do dia que vem para destruir a todos os filisteus, para cortar de Tiro e de Sidom todo o resto que os socorra; porque o Senhor destruirá os filisteus, o resto de Caftor da terra do mar.
5 Sobreveio calvície a Gaza, Asquelom está reduzida a silêncio, com o resto do seu vale; até quando vós vos retalhareis?
6 Ah! Espada do Senhor, até quando deixarás de repousar? Volta para a tua bainha, descansa e aquieta-te.
7 Como podes estar quieta, se o Senhor te deu ordem? Contra Asquelom e contra as bordas do mar é para onde ele te dirige.*
1 A respeito de Moabe. Assim diz o Senhor dos Exércitos, o Deus de Israel: Ai de Nebo, porque foi destruída! Envergonhada está Quiriataim, já está tomada; a fortaleza está envergonhada e abatida.
2 A glória de Moabe já não é; em Hesbom tramaram contra ela, dizendo: Vinde, e eliminemo-la para que não seja mais povo; também tu, ó Madmém, serás reduzida a silêncio; a espada te perseguirá.
3 Há gritos de Horonaim: Ruína e grande destruição!
4 Destruída está Moabe; seus filhinhos fizeram ouvir gritos.
5 Pela subida de Luíte, eles seguem com choro contínuo; na descida de Horonaim, se ouvem gritos angustiosos de ruína.
6 Fugi, salvai a vossa vida, ainda que venhais a ser como o arbusto solitário no deserto.
7 Pois, por causa da tua confiança nas tuas obras e nos teus tesouros, também tu serás tomada; Quemos sairá para o cativeiro com os seus sacerdotes e os seus príncipes juntamente.
8 Virá o destruidor sobre cada uma das cidades, e nenhuma escapará; perecerá o vale, e se destruirá a campina; porque o Senhor o disse.
9 Dai asas a Moabe, porque, voando, sairá; as suas cidades se tornarão em ruínas, e ninguém morará nelas.
10 Maldito aquele que fizer a obra do Senhor relaxadamente! Maldito aquele que retém a sua espada do sangue!
11 Despreocupado esteve Moabe desde a sua mocidade e tem repousado nas fezes do seu vinho; não foi mudado de vasilha para vasilha, nem foi para o cativeiro; por isso, conservou o seu sabor, e o seu aroma não se alterou.
12 Portanto, eis que vêm dias, diz o Senhor, em que lhe enviarei trasfegadores, que o trasfegarão; despejarão as suas vasilhas e despedaçarão os seus jarros.
13 Moabe terá vergonha de Quemos, como a casa de Israel se envergonhou de Betel, sua confiança.
14 Como dizeis: Somos valentes e homens fortes para a guerra?
15 Moabe está destruído e subiu das suas cidades, e os seus jovens escolhidos desceram à matança, diz o Rei, cujo nome é Senhor dos Exércitos.
16 Está prestes a vir a perdição de Moabe, e muito se apressa o seu mal.
17 Condoei-vos dele, todos os que estais ao seu redor e todos os que lhe sabeis o nome; dizei: Como se quebrou a vara forte, o cajado formoso!
18 Desce da tua glória e assenta-te em terra sedenta, ó moradora, filha de Dibom; porque o destruidor de Moabe sobe contra ti e desfaz as tuas fortalezas.
19 Põe-te no caminho e espia, ó moradora de Aroer; pergunta ao que foge e à que escapa: Que sucedeu?
20 Moabe está envergonhado, porque foi abatido; uivai e gritai; anunciai em Arnom que Moabe está destruído.
21 Também o julgamento veio sobre a terra da campina, sobre Holom, Jasa e Mefaate,
22 sobre Dibom, Nebo e Bete-Diblataim,
23 sobre Quiriataim, Bete-Gamul e Bete-Meom,
24 sobre Queriote e Bozra, e até sobre todas as cidades da terra de Moabe, quer as de longe, quer as de perto.
25 Está eliminado o poder de Moabe, e quebrado, o seu braço, diz o Senhor.
26 Embriagai-o, porque contra o Senhor se engrandeceu; Moabe se revolverá no seu vômito e será ele também objeto de escárnio.
27 Pois Israel não te foi também objeto de escárnio? Mas, acaso, foi achado entre ladrões, para que meneies a cabeça, falando dele?
28 Deixai as cidades e habitai no rochedo, ó moradora de Moabe; sede como as pombas que se aninham nos flancos da boca do abismo.
29 Ouvimos falar da soberba de Moabe, que de fato é extremamente soberba, da sua arrogância, do seu orgulho, da sua sobranceria e da altivez do seu coração.
30 Conheço, diz o Senhor, a sua insolência, mas isso nada é; as suas gabarolices nada farão.
31 Por isso, uivarei por Moabe, sim, gritarei por todo o Moabe; pelos homens de Quir-Heres lamentarei.
32 Mais que a Jazer, te chorarei a ti, ó vide de Sibma; os teus ramos passaram o mar, chegaram até ao mar de Jazer; mas o destruidor caiu sobre os teus frutos de verão e sobre a tua vindima.
33 Tirou-se, pois, o folguedo e a alegria do campo fértil e da terra de Moabe; pois fiz cessar nos lagares o vinho; já não pisarão uvas com júbilo; o júbilo não será júbilo.
34 Ouve-se o grito de Hesbom até Eleale e Jasa, e de Zoar se dão gritos até Horonaim e Eglate-Selisias; porque até as águas do Ninrim se tornaram em assolação.
35 Farei desaparecer de Moabe, diz o Senhor, quem sacrifique nos altos e queime incenso aos seus deuses.
36 Por isso, o meu coração geme como flautas por causa de Moabe, e como flautas geme por causa dos homens de Quir-Heres; porquanto já se perdeu a abundância que ajuntou.
37 Porque toda cabeça ficará calva, e toda barba, rapada; sobre todas as mãos haverá incisões, e sobre os lombos, pano de saco.
38 Sobre todos os eirados de Moabe e em todas as suas praças há pranto, porque fiz Moabe em pedaços, como vasilha de barro que não agrada, diz o Senhor. Como está desfalecido!
39 Como uivam! Como, de vergonha, virou Moabe as costas! Assim, se tornou Moabe objeto de escárnio e de espanto para todos os que estão em seu redor.
40 Porque assim diz o Senhor: Eis que voará como a águia e estenderá as suas asas contra Moabe.
41 São tomadas as cidades, e ocupadas, as fortalezas; naquele dia, o coração dos valentes de Moabe será como o coração da mulher que está em dores de parto.
42 Moabe será destruído, para que não seja povo, porque se engrandeceu contra o Senhor.
43 Terror, cova e laço vêm sobre ti, ó moradora de Moabe, diz o Senhor.
44 Quem fugir do terror cairá na cova, e, se sair da cova, o laço o prenderá; porque trarei sobre ele, sobre Moabe, o ano do seu castigo.
45 Os que fogem param sem forças à sombra de Hesbom; porém sai fogo de Hesbom e labareda do meio de Seom e devora as têmporas de Moabe e o alto da cabeça dos filhos do tumulto.
46 Ai de ti, Moabe! Pereceu o povo de Quemos, porque teus filhos ficaram cativos, e tuas filhas, em cativeiro.
47 Contudo, mudarei a sorte de Moabe, nos últimos dias, diz o Senhor. Até aqui o juízo contra Moabe.*
1 A respeito dos filhos de Amom. Assim diz o Senhor: Acaso, não tem Israel filhos? Não tem herdeiro? Por que, pois, herdou Milcom a Gade, e o seu povo habitou nas cidades dela?
2 Portanto, eis que vêm dias, diz o Senhor, em que farei ouvir em Rabá dos filhos de Amom o alarido de guerra, e tornar-se-á num montão de ruínas, e as suas aldeias serão queimadas; e Israel herdará aos que o herdaram, diz o Senhor.
3 Uiva, ó Hesbom, porque é destruída Ai; clamai, ó filhos de Rabá, cingi-vos de cilício, lamentai e dai voltas por entre os muros; porque Milcom irá em cativeiro, juntamente com os seus sacerdotes e os seus príncipes.
4 Por que te glorias nos vales, nos teus luxuriantes vales, ó filha rebelde, que confias nos teus tesouros, dizendo: Quem virá contra mim?
5 Eis que eu trarei terror sobre ti, diz o Senhor, o Senhor dos Exércitos, de todos os que estão ao redor de ti; e cada um de vós será lançado em frente de si, e não haverá quem recolha os fugitivos.
6 Mas depois disto mudarei a sorte dos filhos de Amom, diz o Senhor.
7 A respeito de Edom. Assim diz o Senhor dos Exércitos: Acaso, já não há sabedoria em Temã? Já pereceu o conselho dos sábios? Desvaneceu-se-lhe a sabedoria?
8 Fugi, voltai, retirai-vos para as cavernas, ó moradores de Dedã, porque eu trarei sobre ele a ruína de Esaú, o tempo do seu castigo.
9 Se vindimadores viessem a ti, não deixariam alguns cachos? Se ladrões, de noite, não te danificariam só o que lhes bastasse?
10 Mas eu despi a Esaú, descobri os seus esconderijos, e não se poderá esconder; está destruída a sua descendência, como também seus irmãos e seus vizinhos, e ele já não é.
11 Deixa os teus órfãos, e eu os guardarei em vida; e as tuas viúvas confiem em mim.
12 Porque assim diz o Senhor: Eis que os que não estavam condenados a beber o cálice totalmente o beberão, e tu serias de todo inocentado? Não serás tido por inocente, mas certamente o beberás.
13 Porque por mim mesmo jurei, diz o Senhor, que Bozra será objeto de espanto, de opróbrio, de assolação e de desprezo; e todas as suas cidades se tornarão em assolações perpétuas.
14 Ouvi novas da parte do Senhor, e um mensageiro foi enviado às nações, para lhes dizer: Ajuntai-vos, e vinde contra ela, e levantai-vos para a guerra.
15 Porque eis que te fiz pequeno entre as nações, desprezado entre os homens.
16 O terror que inspiras e a soberba do teu coração te enganaram. Tu que habitas nas fendas das rochas, que ocupas as alturas dos outeiros, ainda que eleves o teu ninho como a águia, de lá te derribarei, diz o Senhor.
17 Assim, será Edom objeto de espanto; todo aquele que passar por ele se espantará e assobiará por causa de todas as suas pragas.
18 Como na destruição de Sodoma e Gomorra e das suas cidades vizinhas, diz o Senhor, assim não habitará ninguém ali, nem morará nela homem algum.
19 Eis que, como sobe o leãozinho da floresta jordânica contra o rebanho em pasto verde, assim, num momento, arrojarei dali a Edom e lá estabelecerei a quem eu escolher. Pois quem é semelhante a mim? Quem me pedirá contas? E quem é o pastor que me poderá resistir?
20 Portanto, ouvi o conselho do Senhor que ele decretou contra Edom e os desígnios que ele formou contra os moradores de Temã; certamente, até os menores do rebanho serão arrastados, e as suas moradas, espantadas por causa deles.
21 A terra estremeceu com o estrondo da sua queda; e, do seu grito, até ao mar Vermelho se ouviu o som.
22 Eis que como águia subirá, voará e estenderá as suas asas contra Bozra; naquele dia, o coração dos valentes de Edom será como o coração da mulher que está em dores de parto.
23 A respeito de Damasco. Envergonhou-se Hamate e Arpade; e, tendo ouvido más novas, cambaleiam; são como o mar agitado, que não se pode sossegar.
24 Enfraquecida está Damasco; virou as costas para fugir, e tremor a tomou; angústia e dores a tomaram como da que está de parto.
25 Como está abandonada a famosa cidade, a cidade de meu folguedo!
26 Portanto, cairão os seus jovens nas suas praças; todos os homens de guerra serão reduzidos a silêncio naquele dia, diz o Senhor dos Exércitos.
27 Acenderei fogo dentro do muro de Damasco, o qual consumirá os palácios de Ben-Hadade.
28 A respeito de Quedar e dos reinos de Hazor, que Nabucodonosor, rei da Babilônia, feriu. Assim diz o Senhor: Levantai-vos, subi contra Quedar e destruí os filhos do Oriente.
29 Tomarão as suas tendas, os seus rebanhos; as lonas das suas tendas, todos os seus bens e os seus camelos levarão para si; e lhes gritarão: Há horror por toda parte!
30 Fugi, desviai-vos para mui longe, retirai-vos para as cavernas, ó moradores de Hazor, diz o Senhor; porque Nabucodonosor, rei da Babilônia, tomou conselho e formou desígnio contra vós outros.
31 Levantai-vos, ó babilônios, subi contra uma nação que habita em paz e confiada, diz o Senhor; que não tem portas, nem ferrolhos; eles habitam a sós.
32 Os seus camelos serão para presa, e a multidão dos seus gados, para despojo; espalharei a todo vento aqueles que cortam os cabelos nas têmporas e de todos os lados lhes trarei a ruína, diz o Senhor.
33 Hazor se tornará em morada de chacais, em assolação para sempre; ninguém habitará ali, homem nenhum habitará nela.
34 Palavra do Senhor que veio a Jeremias, o profeta, contra Elão, no princípio do reinado de Zedequias, rei de Judá, dizendo:
35 Assim diz o Senhor dos Exércitos: Eis que eu quebrarei o arco de Elão, a fonte do seu poder.
36 Trarei sobre Elão os quatro ventos dos quatro ângulos do céu e os espalharei na direção de todos estes ventos; e não haverá país aonde não venham os fugitivos de Elão.
37 Farei tremer a Elão diante de seus inimigos e diante dos que procuram a sua morte; farei vir sobre os elamitas o mal, o brasume da minha ira, diz o Senhor; e enviarei após eles a espada, até que venha a consumi-los.
38 Porei o meu trono em Elão e destruirei dali o rei e os príncipes, diz o Senhor.
39 Nos últimos dias, mudarei a sorte de Elão, diz o Senhor.*
1 Palavra que falou o Senhor contra a Babilônia e contra a terra dos caldeus, por intermédio de Jeremias, o profeta.
2 Anunciai entre as nações; fazei ouvir e arvorai estandarte; proclamai, não encubrais; dizei: Tomada é a Babilônia, Bel está confundido, e abatido, Merodaque; cobertas de vergonha estão as suas imagens, e seus ídolos tremem de terror.
3 Porque do Norte subiu contra ela uma nação que tornará deserta a sua terra, e não haverá quem nela habite; tanto os homens como os animais fugiram e se foram.
4 Naqueles dias, naquele tempo, diz o Senhor, voltarão os filhos de Israel, eles e os filhos de Judá juntamente; andando e chorando, virão e buscarão ao Senhor, seu Deus.
5 Perguntarão pelo caminho de Sião, de rostos voltados para lá, e dirão: Vinde, e unamo-nos ao Senhor, em aliança eterna que jamais será esquecida.
6 O meu povo tem sido ovelhas perdidas; seus pastores as fizeram errar e as deixaram desviar para os montes; do monte passaram ao outeiro, esqueceram-se do seu redil.
7 Todos os que as acharam as devoraram; e os seus adversários diziam: Culpa nenhuma teremos; porque pecaram contra o Senhor, a morada da justiça, e contra a esperança de seus pais, o Senhor.
8 Fugi do meio da Babilônia e saí da terra dos caldeus; e sede como os bodes que vão adiante do rebanho.
9 Porque eis que eu suscitarei e farei subir contra a Babilônia um conjunto de grandes nações da terra do Norte, e se porão em ordem de batalha contra ela; assim será tomada. As suas flechas serão como de destro guerreiro, nenhuma tornará sem efeito.
10 A Caldeia servirá de presa; todos os que a saquearem se fartarão, diz o Senhor;
11 ainda que vos alegrais e exultais, ó saqueadores da minha herança, saltais como bezerros na relva e rinchais como cavalos fogosos,
12 será mui envergonhada vossa mãe, será confundida a que vos deu à luz; eis que ela será a última das nações, um deserto, uma terra seca e uma solidão.
13 Por causa da indignação do Senhor, não será habitada; antes, se tornará de todo deserta; qualquer que passar por Babilônia se espantará e assobiará por causa de todas as suas pragas.
14 Ponde-vos em ordem de batalha em redor contra Babilônia, todos vós que manejais o arco; atirai-lhe, não poupeis as flechas; porque ela pecou contra o Senhor.
15 Gritai contra ela, rodeando-a; ela já se rendeu; caíram-lhe os baluartes, estão em terra os seus muros; pois esta é a vingança do Senhor; vingai-vos dela; fazei-lhe a ela o que ela fez.
16 Eliminai da Babilônia o que semeia e o que maneja a foice no tempo da sega; por causa da espada do opressor, virar-se-á cada um para o seu povo e cada um fugirá para a sua terra.
17 Cordeiro desgarrado é Israel; os leões o afugentaram; primeiro, devorou-o o rei da Assíria, e, por fim, Nabucodonosor o desossou.
18 Portanto, assim diz o Senhor dos Exércitos, o Deus de Israel: Eis que castigarei o rei da Babilônia e a sua terra, como castiguei o rei da Assíria.
19 Farei tornar Israel para a sua morada, e pastará no Carmelo e em Basã; fartar-se-á na região montanhosa de Efraim e em Gileade.
20 Naqueles dias e naquele tempo, diz o Senhor, buscar-se-á a iniquidade de Israel, e já não haverá; os pecados de Judá, mas não se acharão; porque perdoarei aos remanescentes que eu deixar.
21 Sobe, ó espada, contra a terra duplamente rebelde, sobe contra ela e contra os moradores da terra de castigo; assola irremissivelmente, destrói tudo após eles, diz o Senhor, e faze segundo tudo o que te mandei.
22 Há na terra estrondo de batalha e de grande destruição.
23 Como está quebrado, feito em pedaços o martelo de toda a terra! Como se tornou a Babilônia objeto de espanto entre as nações!
24 Lancei-te o laço, ó Babilônia, e foste presa, e não o soubeste; foste surpreendida e apanhada, porque contra o Senhor te entremeteste.
25 O Senhor abriu o seu arsenal e tirou dele as armas da sua indignação; porque o Senhor, o Senhor dos Exércitos, tem obra a realizar na terra dos caldeus.
26 Vinde contra ela de todos os confins da terra, abri os seus celeiros, fazei dela montões de ruínas, destruí-a de todo; dela nada fique de resto.
27 Matai à espada a todos os seus touros, aos seus valentes; desçam eles para o matadouro; ai deles! Pois é chegado o seu dia, o tempo do seu castigo.
28 Ouve-se a voz dos que fugiram e escaparam da terra da Babilônia, para anunciarem em Sião a vingança do Senhor, nosso Deus, a vingança do seu templo.
29 Convocai contra Babilônia a multidão dos que manejam o arco; acampai-vos contra ela em redor, e ninguém escape. Retribuí-lhe segundo a sua obra; conforme tudo o que fez, assim fazei a ela; porque se houve arrogantemente contra o Senhor, contra o Santo de Israel.
30 Portanto, cairão os seus jovens nas suas praças, e todos os seus homens de guerra serão reduzidos a silêncio naquele dia, diz o Senhor.
31 Eis que eu sou contra ti, ó orgulhosa, diz o Senhor, o Senhor dos Exércitos; porque veio o teu dia, o tempo em que te hei de castigar.
32 Então, tropeçará o soberbo, e cairá, e ninguém haverá que o levante; porei fogo às suas cidades, o qual consumirá todos os seus arredores.
33 Assim diz o Senhor dos Exércitos: Os filhos de Israel e os filhos de Judá sofrem opressão juntamente; todos os que os levaram cativos os retêm; recusam deixá-los ir;
34 mas o seu Redentor é forte, Senhor dos Exércitos é o seu nome; certamente, pleiteará a causa deles, para aquietar a terra e inquietar os moradores da Babilônia.
35 A espada virá sobre os caldeus, diz o Senhor, e sobre os moradores da Babilônia, sobre os seus príncipes, sobre os seus sábios.
36 A espada virá sobre os gabarolas, e ficarão insensatos; virá sobre os valentes dela, e ficarão aterrorizados.
37 A espada virá sobre os seus cavalos, e sobre os seus carros, e sobre todo o misto de gente que está no meio dela, e este será como mulheres; a espada virá sobre os tesouros dela, e serão saqueados.
38 A espada virá sobre as suas águas, e estas secarão; porque a terra é de imagens de escultura, e os seus moradores enlouquecem por estas coisas horríveis.
39 Por isso, as feras do deserto com os chacais habitarão em Babilônia; também os avestruzes habitarão nela, e nunca mais será povoada, nem habitada de geração em geração,
40 como quando Deus destruiu a Sodoma, e a Gomorra, e às suas cidades vizinhas, diz o Senhor; assim, ninguém habitará ali, nem morará nela homem algum.
41 Eis que um povo vem do Norte; grande nação e muitos reis se levantarão dos confins da terra.
42 Armam-se de arco e de lança; eles são cruéis e não conhecem a compaixão; a voz deles é como o mar, que brama; montam cavalos, cada um posto em ordem de batalha contra ti, ó filha da Babilônia.
43 O rei da Babilônia ouviu a fama deles, e desfaleceram as suas mãos; a angústia se apoderou dele, e dores, como as da mulher que está de parto.
44 Eis que, como sobe o leãozinho da floresta jordânica contra o rebanho em pasto verde, assim, num momento, arrojá-la-ei dali e lá estabelecerei a quem eu escolher. Pois quem é semelhante a mim? Quem me pedirá contas? E quem é o pastor que me poderá resistir?
45 Portanto, ouvi o conselho do Senhor, que ele decretou contra Babilônia, e os desígnios que ele formou contra a terra dos caldeus; certamente, até os menores do rebanho serão arrastados, e as suas moradas, espantadas por causa deles.
46 Ao estrondo da tomada de Babilônia, estremeceu a terra; e o grito se ouviu entre as nações.*
1 Assim diz o Senhor: Eis que levantarei um vento destruidor contra a Babilônia e contra os que habitam em Lebe-Camai.
2 Enviarei padejadores contra a Babilônia, que a padejarão e despojarão a sua terra; porque virão contra ela em redor no dia da calamidade.
3 O flecheiro arme o seu arco contra o que o faz com o seu e contra o que presume da sua couraça; não poupeis os seus jovens, destruí de todo o seu exército.
4 Caiam mortos na terra dos caldeus e atravessados pelas ruas!
5 Porque Israel e Judá não enviuvaram do seu Deus, do Senhor dos Exércitos; mas a terra dos caldeus está cheia de culpas perante o Santo de Israel.
6 Fugi do meio da Babilônia, e cada um salve a sua vida; não pereçais na sua maldade; porque é tempo da vingança do Senhor: ele lhe dará a sua paga.
7 A Babilônia era um copo de ouro na mão do Senhor, o qual embriagava a toda a terra; do seu vinho beberam as nações; por isso, enlouqueceram.
8 Repentinamente, caiu Babilônia e ficou arruinada; lamentai por ela, tomai bálsamo para a sua ferida; porventura, sarará.
9 Queríamos curar Babilônia, ela, porém, não sarou; deixai-a, e cada um vá para a sua terra; porque o seu juízo chega até ao céu e se eleva até às mais altas nuvens.
10 O Senhor trouxe a nossa justiça à luz; vinde, e anunciemos em Sião a obra do Senhor, nosso Deus.
11 Aguçai as flechas! Preparai os escudos! O Senhor despertou o espírito dos reis dos medos; porque o seu intento contra a Babilônia é para a destruir; pois esta é a vingança do Senhor, a vingança do seu templo.
12 Arvorai estandarte contra os muros de Babilônia, reforçai a guarda, colocai sentinelas, preparai emboscadas; porque o Senhor intentou e fez o que tinha dito acerca dos moradores da Babilônia.
13 Ó tu que habitas sobre muitas águas, rica de tesouros! Chegou o teu fim, a medida da tua avareza.
14 Jurou o Senhor dos Exércitos por si mesmo, dizendo: Encher-te-ei certamente de homens, como de gafanhotos, e eles cantarão sobre ti o eia! dos que pisam as uvas.
15 Ele fez a terra pelo seu poder; estabeleceu o mundo por sua sabedoria e com a sua inteligência estendeu os céus.
16 Fazendo ele ribombar o trovão, logo há tumulto de águas no céu, e sobem os vapores das extremidades da terra; ele cria os relâmpagos para a chuva e dos seus depósitos faz sair o vento.
17 Todo homem se tornou estúpido e não tem saber; todo ourives é envergonhado pela imagem que esculpiu; pois as suas imagens são mentira, e nelas não há fôlego.
18 Vaidade são, obra ridícula; no tempo do seu castigo, virão a perecer.
19 Não é semelhante a estas aquele que é a Porção de Jacó; porque ele é o criador de todas as coisas, e Israel é a tribo da sua herança; Senhor dos Exércitos é o seu nome.
20 Tu, Babilônia, eras meu martelo e minhas armas de guerra; por meio de ti, despedacei nações e destruí reis;
21 por meio de ti, despedacei o cavalo e o seu cavaleiro; despedacei o carro e o seu cocheiro;
22 por meio de ti, despedacei o homem e a mulher, despedacei o velho e o moço, despedacei o jovem e a virgem;
23 por meio de ti, despedacei o pastor e o seu rebanho, despedacei o lavrador e a sua junta de bois, despedacei governadores e vice-reis.
24 Pagarei, ante os vossos próprios olhos, à Babilônia e a todos os moradores da Caldeia toda a maldade que fizeram em Sião, diz o Senhor.
25 Eis que sou contra ti, ó monte que destróis, diz o Senhor, que destróis toda a terra; estenderei a mão contra ti, e te revolverei das rochas, e farei de ti um monte em chamas.
26 De ti não se tirarão pedras, nem para o ângulo nem para fundamentos, porque te tornarás em desolação perpétua, diz o Senhor.
27 Arvorai estandarte na terra, tocai trombeta entre as nações, consagrai as nações contra ela, convocai contra ela os reinos de Ararate, Mini e Asquenaz; ordenai contra ela chefes, fazei subir cavalos como gafanhotos eriçados.
28 Consagrai contra ela as nações, os reis dos medos, os seus governadores, todos os seus vice-reis e toda a terra do seu domínio.
29 Estremece a terra e se contorce em dores, porque cada um dos desígnios do Senhor está firme contra Babilônia, para fazer da terra da Babilônia uma desolação, sem que haja quem nela habite.
30 Os valentes da Babilônia cessaram de pelejar, permanecem nas fortalezas, desfaleceu-lhes a força, tornaram-se como mulheres; estão em chamas as suas moradas, quebrados, os seus ferrolhos.
31 Sai um correio ao encontro de outro correio, um mensageiro ao encontro de outro mensageiro, para anunciar ao rei da Babilônia que a sua cidade foi tomada de todos os lados;
32 que os vaus estão ocupados, e as defesas, queimadas, e os homens de guerra, amedrontados.
33 Porque assim diz o Senhor dos Exércitos, o Deus de Israel: A filha da Babilônia é como a eira quando é aplanada e pisada; ainda um pouco, e o tempo da ceifa lhe virá.
34 Nabucodonosor, rei da Babilônia, nos devorou, esmagou-nos e fez de nós um objeto inútil; como monstro marinho, nos tragou, encheu a sua barriga das nossas comidas finas e nos arrojou fora.
35 A violência que se me fez a mim e à minha carne caia sobre a Babilônia, diga a moradora de Sião; o meu sangue caia sobre os moradores da Caldeia, diga Jerusalém.
36 Pelo que assim diz o Senhor: Eis que pleitearei a tua causa e te vingarei da vingança que se tomou contra ti; secarei o seu mar e farei que se esgote o seu manancial.
37 Babilônia se tornará em montões de ruínas, morada de chacais, objeto de espanto e assobio, e não haverá quem nela habite.
38 Ainda que juntos rujam como leões e rosnem como cachorros de leões,
39 estando eles esganados, preparar-lhes-ei um banquete, embriagá-los-ei para que se regozijem e durmam sono eterno e não acordem, diz o Senhor.
40 Fá-los-ei descer como cordeiros ao matadouro, como carneiros e bodes.
41 Como foi tomada Babilônia, e apanhada de surpresa, a glória de toda a terra! Como se tornou Babilônia objeto de espanto entre as nações!
42 O mar é vindo sobre Babilônia, coberta está com o tumulto das suas ondas.
43 Tornaram-se as suas cidades em desolação, terra seca e deserta, terra em que ninguém habita, nem passa por ela homem algum.
44 Castigarei a Bel na Babilônia e farei que lance de sua boca o que havia tragado, e nunca mais concorrerão a ele as nações; também o muro de Babilônia caiu.
45 Saí do meio dela, ó povo meu, e salve cada um a sua vida do brasume da ira do Senhor.
46 Não desfaleça o vosso coração, não temais o rumor que se há de ouvir na terra; pois virá num ano um rumor, noutro ano, outro rumor; haverá violência na terra, dominador contra dominador.
47 Portanto, eis que vêm dias, em que castigarei as imagens de escultura da Babilônia, toda a sua terra será envergonhada, e todos os seus cairão traspassados no meio dela.
48 Os céus, e a terra, e tudo quanto neles há jubilarão sobre Babilônia; porque do Norte lhe virão os destruidores, diz o Senhor.
49 Como Babilônia fez cair traspassados os de Israel, assim, em Babilônia, cairão traspassados os de toda a terra.
50 Vós que escapastes da espada, ide-vos, não pareis; de longe lembrai-vos do Senhor, e suba Jerusalém à vossa mente.
51 Direis: Envergonhados estamos, porque ouvimos opróbrio; vergonha cobriu-nos o rosto, porque vieram estrangeiros e entraram nos santuários da Casa do Senhor.
52 Portanto, eis que vêm dias, diz o Senhor, em que castigarei as suas imagens de escultura; e gemerão os traspassados em toda a sua terra.
53 Ainda que a Babilônia subisse aos céus e ainda que fortificasse no alto a sua fortaleza, de mim viriam destruidores contra ela, diz o Senhor.
54 De Babilônia se ouvem gritos, e da terra dos caldeus, o ruído de grande destruição;
55 porque o Senhor destrói Babilônia e faz perecer nela a sua grande voz; bramarão as ondas do inimigo como muitas águas, ouvir-se-á o tumulto da sua voz,
56 porque o destruidor vem contra ela, contra Babilônia; os seus valentes estão presos, já estão quebrados os seus arcos; porque o Senhor, Deus que dá a paga, certamente, lhe retribuirá.
57 Embriagarei os seus príncipes, os seus sábios, os seus governadores, os seus vice-reis e os seus valentes; dormirão sono eterno e não acordarão, diz o Rei, cujo nome é Senhor dos Exércitos.
58 Assim diz o Senhor dos Exércitos: Os largos muros de Babilônia totalmente serão derribados, e as suas altas portas serão abrasadas pelo fogo; assim, trabalharam os povos em vão, e para o fogo se afadigaram as nações.
59 Palavra que mandou Jeremias, o profeta, a Seraías, filho de Nerias, filho de Maaseias, indo este com Zedequias, rei de Judá, à Babilônia, no ano quarto do seu reinado. Seraías era o camareiro-mor.
60 Escreveu, pois, Jeremias num livro todo o mal que havia de vir sobre a Babilônia, a saber, todas as palavras já escritas contra a Babilônia.
61 Disse Jeremias a Seraías: Quando chegares a Babilônia, vê que leias em voz alta todas estas palavras.
62 E dirás: Ó Senhor! Falaste a respeito deste lugar que o exterminarias, a fim de que nada fique nele, nem homem nem animal, e que se tornaria em perpétuas assolações.
63 Quando acabares de ler o livro, atá-lo-ás a uma pedra e o lançarás no meio do Eufrates;
64 e dirás: Assim será afundada a Babilônia e não se levantará, por causa do mal que eu hei de trazer sobre ela; e os seus moradores sucumbirão. Até aqui as palavras de Jeremias.*
1 Tinha Zedequias a idade de vinte e um anos, quando começou a reinar e reinou onze anos em Jerusalém. Sua mãe se chamava Hamutal e era filha de Jeremias, de Libna.
2 Fez ele o que era mau perante o Senhor, conforme tudo quanto fizera Jeoaquim.
3 Assim sucedeu por causa da ira do Senhor contra Jerusalém e contra Judá, a ponto de os rejeitar de sua presença; Zedequias rebelou-se contra o rei da Babilônia.
4 Sucedeu que, em o nono ano do reinado de Zedequias, aos dez dias do décimo mês, Nabucodonosor, rei da Babilônia, veio contra Jerusalém, ele e todo o seu exército, e se acamparam contra ela, e levantaram contra ela tranqueiras em redor.
5 A cidade ficou sitiada até ao undécimo ano do rei Zedequias.
6 Aos nove dias do quarto mês, quando a cidade se via apertada da fome, e não havia pão para o povo da terra,
7 então, a cidade foi arrombada, e todos os homens de guerra fugiram e saíram de noite pelo caminho da porta que está entre os dois muros perto do jardim do rei, a despeito de os caldeus se acharem contra a cidade em redor; e se foram pelo caminho da campina.
8 Porém o exército dos caldeus perseguiu o rei Zedequias e o alcançou nas campinas de Jericó; e todo o exército deste se dispersou e o abandonou.
9 Então, o tomaram preso e o fizeram subir ao rei da Babilônia, a Ribla, na terra de Hamate, e este lhe pronunciou a sentença.
10 Matou o rei da Babilônia os filhos de Zedequias à sua própria vista, bem assim todos os príncipes de Judá, em Ribla.
11 Vazou os olhos de Zedequias, atou-o com duas cadeias de bronze, levou-o à Babilônia e o conservou no cárcere até ao dia da sua morte.
12 No décimo dia do quinto mês, do ano décimo nono de Nabucodonosor, rei da Babilônia, Nebuzaradã, o chefe da guarda e servidor do rei da Babilônia, veio a Jerusalém.
13 E queimou a Casa do Senhor e a casa do rei, como também todas as casas de Jerusalém; também entregou às chamas todos os edifícios importantes.
14 Todo o exército dos caldeus que estava com o chefe da guarda derribou todos os muros em redor de Jerusalém.
15 Dos mais pobres do povo, o mais do povo que havia ficado na cidade, os desertores que se entregaram ao rei da Babilônia e o mais da multidão Nebuzaradã, o chefe da guarda, levou cativos.
16 Porém dos mais pobres da terra deixou Nebuzaradã, o chefe da guarda, ficar alguns para vinheiros e para lavradores.
17 Os caldeus cortaram em pedaços as colunas de bronze que estavam na Casa do Senhor, como também os suportes e o mar de bronze que estavam na Casa do Senhor; e levaram todo o bronze para a Babilônia.
18 Levaram também as panelas, as pás, as espevitadeiras, as bacias, os recipientes de incenso e todos os utensílios de bronze, com que se ministrava.
19 Tomou também o chefe da guarda os copos, os braseiros, as bacias, as panelas, os candeeiros, os recipientes de incenso e as taças, tudo quanto fosse de ouro ou de prata.
20 Quanto às duas colunas, ao mar e aos suportes que Salomão fizera para a Casa do Senhor, o peso do bronze de todos estes utensílios era incalculável.
21 Quanto às colunas, a altura de uma era de dezoito côvados, um cordão de doze côvados a cercava, e a grossura era de quatro dedos; era oca.
22 Sobre ela havia um capitel de bronze; a altura de cada um era de cinco côvados; a obra de rede e as romãs sobre o capitel ao redor eram de bronze.
23 Semelhante a esta era a outra coluna com as romãs. Havia noventa e seis romãs aos lados; as romãs todas sobre a obra de rede ao redor eram cem.
24 Levou também o chefe da guarda a Seraías, sumo sacerdote, e a Sofonias, segundo sacerdote, e aos três guardas da porta.
25 Da cidade tomou a um oficial, que era comandante das tropas de guerra, e a sete homens dos que eram conselheiros pessoais do rei e se achavam na cidade, como também ao escrivão-mor do exército, que alistava o povo da terra, e a sessenta homens do povo do lugar, que se achavam na cidade.
26 Tomando-os Nebuzaradã, o chefe da guarda, levou-os ao rei da Babilônia, a Ribla.
27 O rei da Babilônia os feriu e os matou em Ribla, na terra de Hamate.
28 Assim, Judá foi levado cativo para fora de sua terra. Este é o povo que Nabucodonosor levou para o exílio: no sétimo ano, três mil e vinte e três judeus;
29 no ano décimo oitavo de Nabucodonosor, levou ele cativas de Jerusalém oitocentas e trinta e duas pessoas;
30 no ano vigésimo terceiro de Nabucodonosor, Nebuzaradã, o chefe da guarda, levou cativas, dentre os judeus, setecentas e quarenta e cinco pessoas; todas as pessoas são quatro mil e seiscentas.
31 No trigésimo sétimo ano do cativeiro de Joaquim, rei de Judá, no dia vinte e cinco do duodécimo mês, Evil-Merodaque, rei da Babilônia, no ano em que começou a reinar, libertou a Joaquim, rei de Judá, e o fez sair do cárcere.
32 Falou com ele benignamente e lhe deu lugar de mais honra do que o dos reis que estavam consigo em Babilônia.
33 Mudou-lhe as vestes do cárcere, e Joaquim passou a comer pão na sua presença, todos os dias da sua vida.
34 E da parte do rei da Babilônia lhe foi dada subsistência vitalícia, uma pensão diária, até ao dia da sua morte, durante os dias da sua vida.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Jeremias','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)