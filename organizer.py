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
1 Salomão, filho de Davi, fortaleceu-se no seu reino, e o Senhor, seu Deus, era com ele e o engrandeceu sobremaneira.
2 Falou Salomão a todo o Israel, aos capitães de mil e aos de cem, aos juízes e a todos os príncipes em todo o Israel, cabeças de famílias;
3 e foi com toda a congregação ao alto que estava em Gibeão, porque ali estava a tenda da congregação de Deus, que Moisés, servo do Senhor, tinha feito no deserto.
4 Mas Davi fizera subir a arca de Deus de Quiriate-Jearim ao lugar que lhe havia preparado, porque lhe armara uma tenda em Jerusalém.
5 Também o altar de bronze que fizera Bezalel, filho de Uri, filho de Hur, estava ali diante do tabernáculo do Senhor; e Salomão e a congregação consultaram o Senhor.
6 Salomão ofereceu ali sacrifícios perante o Senhor, sobre o altar de bronze que estava na tenda da congregação; e ofereceu sobre ele mil holocaustos.
7 Naquela mesma noite, apareceu Deus a Salomão e lhe disse: Pede-me o que queres que eu te dê.
8 Respondeu-lhe Salomão: De grande benevolência usaste para com Davi, meu pai, e a mim me fizeste reinar em seu lugar.
9 Agora, pois, ó Senhor Deus, cumpra-se a tua promessa feita a Davi, meu pai; porque tu me constituíste rei sobre um povo numeroso como o pó da terra.
10 Dá-me, pois, agora, sabedoria e conhecimento, para que eu saiba conduzir-me à testa deste povo; pois quem poderia julgar a este grande povo?
11 Disse Deus a Salomão: Porquanto foi este o desejo do teu coração, e não pediste riquezas, bens ou honras, nem a morte dos que te aborrecem, nem tampouco pediste longevidade, mas sabedoria e conhecimento, para poderes julgar a meu povo, sobre o qual te constituí rei,
12 sabedoria e conhecimento são dados a ti, e te darei riquezas, bens e honras, quais não teve nenhum rei antes de ti, e depois de ti não haverá teu igual.
13 Voltou Salomão para Jerusalém, da sua ida ao alto que está em Gibeão, de diante da tenda da congregação; e reinou sobre Israel.
14 Salomão ajuntou carros e cavaleiros; tinha mil e quatrocentos carros e doze mil cavaleiros, que colocou nas cidades para os carros e junto ao rei, em Jerusalém.
15 Fez o rei que, em Jerusalém, houvesse prata e ouro como pedras, e cedros em abundância como os sicômoros que estão nas planícies.
16 Os cavalos de Salomão vinham do Egito e da Cilícia; e comerciantes do rei os recebiam da Cilícia por certo preço.
17 Importava-se do Egito um carro por seiscentos siclos de prata e um cavalo, por cento e cinquenta; nas mesmas condições, as caravanas os traziam e os exportavam para todos os reis dos heteus e para os reis da Síria.*
1 Resolveu Salomão edificar a casa ao nome do Senhor, como também casa para o seu reino.
2 Designou Salomão setenta mil homens para levarem as cargas, oitenta mil, para talharem pedras nas montanhas e três mil e seiscentos, para dirigirem a obra.
3 Salomão mandou dizer a Hirão, rei de Tiro: Como procedeste para com Davi, meu pai, e lhe mandaste cedros, para edificar a casa em que morasse, assim também procede comigo.
4 Eis que estou para edificar a casa ao nome do Senhor, meu Deus, e lha consagrar, para queimar perante ele incenso aromático, e lhe apresentar o pão contínuo da proposição e os holocaustos da manhã e da tarde, nos sábados, nas Festas da Lua Nova e nas festividades do Senhor, nosso Deus; o que é obrigação perpétua para Israel.
5 A casa que edificarei há de ser grande, porque o nosso Deus é maior do que todos os deuses.
6 No entanto, quem seria capaz de lhe edificar a casa, visto que os céus e até os céus dos céus o não podem conter? E quem sou eu para lhe edificar a casa, senão para queimar incenso perante ele?
7 Manda-me, pois, agora, um homem que saiba trabalhar em ouro, em prata, em bronze, em ferro, em obras de púrpura, de carmesim e de pano azul; que saiba fazer obras de entalhe juntamente com os peritos que estão comigo em Judá e em Jerusalém, os quais Davi, meu pai, empregou.
8 Manda-me também madeira de cedros, ciprestes e sândalo do Líbano; porque bem sei que os teus servos sabem cortar madeira no Líbano. Eis que os meus servos estarão com os teus,
9 para me prepararem muita madeira; porque a casa que edificarei há de ser grande e maravilhosa.
10 Aos teus servos, cortadores da madeira, darei vinte mil coros de trigo batido, vinte mil coros de cevada, vinte mil batos de vinho e vinte mil batos de azeite.
11 Hirão, rei de Tiro, respondeu por uma carta que enviou a Salomão, dizendo: Porquanto o Senhor ama ao seu povo, te constituiu rei sobre ele.
12 Disse mais Hirão: Bendito seja o Senhor, Deus de Israel, que fez os céus e a terra; que deu ao rei Davi um filho sábio, dotado de discrição e entendimento, que edifique casa ao Senhor e para o seu próprio reino.
13 Agora, pois, envio um homem sábio de grande entendimento, a saber, Hirão-Abi,
14 filho de uma mulher das filhas de Dã e cujo pai foi homem de Tiro; ele sabe lavrar em ouro, em prata, em bronze, em ferro, em pedras e em madeira, em obras de púrpura, de pano azul, e de linho fino e em obras de carmesim; e é hábil para toda obra de entalhe e para elaborar qualquer plano que se lhe proponha, juntamente com os teus peritos e os peritos de Davi, meu senhor, teu pai.
15 Agora, pois, mande o meu senhor para os seus servos o trigo, a cevada, o azeite e o vinho de que falou.
16 E nós cortaremos tanta madeira no Líbano quanta houveres mister e ta faremos chegar em jangadas, pelo mar, a Jope, e tu a farás subir a Jerusalém.
17 Salomão levantou o censo de todos os homens estrangeiros que havia na terra de Israel, segundo o censo que fizera Davi, seu pai; e acharam-se cento e cinquenta e três mil e seiscentos.
18 Designou deles setenta mil para levarem as cargas, oitenta mil para talharem pedras nas montanhas, como também três mil e seiscentos para dirigirem o trabalho do povo.*
1 Começou Salomão a edificar a Casa do Senhor em Jerusalém, no monte Moriá, onde o Senhor aparecera a Davi, seu pai, lugar que Davi tinha designado na eira de Ornã, o jebuseu.
2 Começou a edificar no segundo mês, no dia segundo, no ano quarto do seu reinado.
3 Foram estas as medidas dos alicerces que Salomão lançou para edificar a Casa de Deus: o comprimento em côvados, segundo o primitivo padrão, sessenta côvados, e a largura, vinte.
4 O pórtico diante da casa media vinte côvados no sentido da largura do Lugar Santo, e a altura, cento e vinte, o que, dentro, cobriu de ouro puro.
5 Também fez forrar de madeira de cipreste a sala grande, e a cobriu de ouro puro, e gravou nela palmas e cadeias.
6 Também adornou a sala de pedras preciosas; e o ouro era de Parvaim.
7 Cobriu também de ouro a sala, as traves, os umbrais, as paredes e as portas; e lavrou querubins nas paredes.
8 Fez mais o Santo dos Santos, cujo comprimento, segundo a largura da sala grande, era de vinte côvados, e também a largura, de vinte; cobriu-a de ouro puro do peso de seiscentos talentos.
9 O peso dos pregos era de cinquenta siclos de ouro. Cobriu de ouro os cenáculos.
10 No Santo dos Santos, fez dois querubins de madeira e os cobriu de ouro.
11 As asas estendidas, juntas, dos querubins mediam o comprimento de vinte côvados; a asa de um deles, de cinco côvados, tocava na parede da casa; e a outra asa, de cinco côvados, tocava na asa do outro querubim.
12 Também a asa do outro querubim era de cinco côvados e tocava na outra parede; era também a outra asa igualmente de cinco côvados e estava unida à asa do outro querubim. As asas destes querubins se estendiam por vinte côvados;
13 eles estavam postos em pé, e o seu rosto, virado para o Santo Lugar.
14 Também fez o véu de estofo azul, púrpura, carmesim e linho fino; e fez bordar nele querubins.
15 Fez também diante da sala duas colunas de trinta e cinco côvados de altura; e o capitel, sobre cada uma, de cinco côvados.
16 Também fez cadeias, como no Santo dos Santos, e as pôs sobre as cabeças das colunas; fez também cem romãs, as quais pôs nas cadeias.
17 Levantou as colunas diante do templo, uma à direita, e outra à esquerda; a da direita, chamou-lhe Jaquim, a da esquerda, Boaz.*
1 Também fez um altar de bronze de vinte côvados de comprimento, vinte de largura e dez de altura.
2 Fez também o mar de fundição, redondo, de dez côvados de uma borda até a outra borda, e de cinco de altura; e um fio de trinta côvados era a medida de sua circunferência.
3 Por baixo da sua borda, em redor, havia figuras de colocíntidas, dez em cada côvado; estavam em duas fileiras, fundidas quando se fundiu o mar.
4 Assentava-se o mar sobre doze bois; três olhavam para o norte, três, para o ocidente, três, para o sul, e três, para o oriente; o mar apoiava-se sobre eles, cujas partes posteriores convergiam para dentro.
5 A grossura dele era de quatro dedos, a sua borda, como borda de copo, como flor de lírios; comportava três mil batos.
6 Também fez dez pias e pôs cinco à direita e cinco, à esquerda, para lavarem nelas o que pertencia ao holocausto; o mar, porém, era para que os sacerdotes se lavassem nele.
7 Fez também dez candeeiros de ouro, segundo fora ordenado, e os pôs no templo, cinco à direita e cinco à esquerda.
8 Também fez dez mesas e as pôs no templo, cinco à direita e cinco à esquerda; também fez cem bacias de ouro.
9 Fez mais o pátio dos sacerdotes e o pátio grande, como também as portas deles, as quais cobriu de bronze.
10 E o mar pôs ao lado direito, para o lado sudeste.
11 Depois, fez Hirão as panelas, e as pás, e as bacias. Assim, terminou ele de fazer a obra para o rei Salomão, para a Casa de Deus:
12 as duas colunas, os dois globos e os dois capitéis que estavam no alto das duas colunas; as duas redes, para cobrirem os dois globos dos capitéis que estavam no alto das colunas;
13 as quatrocentas romãs para as duas redes, isto é, duas fileiras de romãs para cada rede, para cobrirem os dois globos dos capitéis que estavam no alto das colunas.
14 Fez também os suportes e as pias sobre eles,
15 o mar com os doze bois por baixo.
16 Também as panelas, as pás, os garfos e todos os utensílios fez Hirão-Abi para o rei Salomão, para a Casa do Senhor, de bronze purificado.
17 Na planície do Jordão, o rei os fez fundir em terra barrenta, entre Sucote e Zereda.
18 Fez Salomão todos estes objetos em grande abundância, não se verificando o peso do seu bronze.
19 Também fez Salomão todos os utensílios do Santo Lugar de Deus: o altar de ouro e as mesas, sobre as quais estavam os pães da proposição;
20 e os candeeiros com as suas lâmpadas de ouro puro, para as acenderem, segundo o costume, perante o Santo dos Santos.
21 As flores, as lâmpadas e as tenazes eram do mais fino ouro,
22 como também as espevitadeiras, as bacias, as taças e os incensários, de ouro finíssimo; quanto à entrada da casa, as suas portas de dentro do Santo dos Santos e as portas do Santo Lugar do templo eram de ouro.*
1 Assim, se acabou toda a obra que fez o rei Salomão para a Casa do Senhor; então, trouxe Salomão as coisas que Davi, seu pai, havia dedicado; a prata, o ouro e os utensílios, ele os pôs entre os tesouros da Casa de Deus.
2 Congregou Salomão os anciãos de Israel e todos os cabeças das tribos, os príncipes das famílias dos israelitas, em Jerusalém, para fazerem subir a arca da Aliança do Senhor, da Cidade de Davi, que é Sião, para o templo.
3 Todos os homens de Israel se congregaram junto ao rei, na ocasião da festa, que foi no sétimo mês.
4 Vieram todos os anciãos de Israel, e os levitas tomaram a arca
5 e a levaram para cima, com a tenda da congregação, e também os utensílios sagrados que nela havia; os levitas sacerdotes é que os fizeram subir.
6 O rei Salomão e toda a congregação de Israel, que se reunira a ele, estavam diante da arca, sacrificando ovelhas e bois, que, de tão numerosos, não se podiam contar.
7 Puseram os sacerdotes a arca da Aliança do Senhor no seu lugar, no santuário mais interior do templo, no Santo dos Santos, debaixo das asas dos querubins.
8 (Pois os querubins estendiam as asas sobre o lugar da arca e, do alto, cobriam a arca e os seus varais.
9 Os varais sobressaíam tanto, que suas pontas eram vistas do Santo Lugar, defronte do Santo dos Santos, porém de fora não se viam.
10 Aí estão os varais até ao dia de hoje.) Nada havia na arca senão as duas tábuas que Moisés ali pusera junto a Horebe, quando o Senhor fez aliança com os filhos de Israel, ao saírem do Egito.
11 Quando saíram os sacerdotes do santuário (porque todos os sacerdotes, que estavam presentes, se santificaram, sem respeitarem os seus turnos);
12 e quando todos os levitas que eram cantores, isto é, Asafe, Hemã, Jedutum e os filhos e irmãos deles, vestidos de linho fino, estavam de pé, para o oriente do altar, com címbalos, alaúdes e harpas, e com eles até cento e vinte sacerdotes, que tocavam as trombetas;
13 e quando em uníssono, a um tempo, tocaram as trombetas e cantaram para se fazerem ouvir, para louvarem o Senhor e render-lhe graças; e quando levantaram eles a voz com trombetas, címbalos e outros instrumentos músicos para louvarem o Senhor, porque ele é bom, porque a sua misericórdia dura para sempre, então, sucedeu que a casa, a saber, a Casa do Senhor, se encheu de uma nuvem;
14 de maneira que os sacerdotes não podiam estar ali para ministrar, por causa da nuvem, porque a glória do Senhor encheu a Casa de Deus.*
1 Então, disse Salomão: O Senhor declarou que habitaria em nuvem espessa!
2 Edifiquei uma casa para tua morada, lugar para a tua eterna habitação.
3 Voltou, então, o rei o rosto, e abençoou a toda a congregação de Israel, enquanto ela se mantinha em pé,
4 e disse: Bendito seja o Senhor, o Deus de Israel, que falou pessoalmente a Davi, meu pai, e pelo seu poder o cumpriu, dizendo:
5 Desde o dia em que eu tirei o meu povo da terra do Egito, não escolhi cidade alguma de todas as tribos de Israel, para edificar uma casa a fim de ali estabelecer o meu nome; nem escolhi homem algum para chefe do meu povo de Israel.
6 Mas escolhi Jerusalém para que ali seja estabelecido o meu nome e escolhi a Davi para chefe do meu povo de Israel.
7 Também Davi, meu pai, propusera em seu coração o edificar uma casa ao nome do Senhor, o Deus de Israel.
8 Porém o Senhor disse a Davi, meu pai: Já que desejaste edificar uma casa ao meu nome, bem fizeste em o resolver em teu coração.
9 Todavia, tu não edificarás a casa; porém teu filho, que descenderá de ti, ele a edificará ao meu nome.
10 Assim, cumpriu o Senhor a sua palavra que tinha dito, pois me levantei em lugar de Davi, meu pai, e me assentei no trono de Israel, como prometera o Senhor; e edifiquei a casa ao nome do Senhor, o Deus de Israel.
11 Nela pus a arca em que estão as tábuas da aliança que o Senhor fez com os filhos de Israel.
12 Pôs-se Salomão diante do altar do Senhor, na presença de toda a congregação de Israel, e estendeu as mãos.
13 Porque Salomão tinha feito uma tribuna de bronze, de cinco côvados de comprimento, cinco de largura e três de altura, e a pusera no meio do pátio; pôs-se em pé sobre ela, ajoelhou-se em presença de toda a congregação de Israel, estendeu as mãos para o céu
14 e disse: Ó Senhor, Deus de Israel, não há Deus como tu, nos céus e na terra, como tu que guardas a aliança e a misericórdia a teus servos que de todo o coração andam diante de ti;
15 que cumpriste para com teu servo Davi, meu pai, o que lhe prometeste; pessoalmente, o disseste e, pelo teu poder, o cumpriste, como hoje se vê.
16 Agora, pois, ó Senhor, Deus de Israel, faze a teu servo Davi, meu pai, o que lhe declaraste, dizendo: Não te faltará sucessor diante de mim, que se assente no trono de Israel, contanto que teus filhos guardem o seu caminho, para andarem na lei diante de mim, como tu andaste.
17 Agora, também, ó Senhor, Deus de Israel, cumpra-se a tua palavra que disseste a teu servo Davi.
18 Mas, de fato, habitaria Deus com os homens na terra? Eis que os céus e até o céu dos céus não te podem conter, quanto menos esta casa que eu edifiquei.
19 Atenta, pois, para a oração de teu servo e para a sua súplica, ó Senhor, meu Deus, para ouvires o clamor e a oração que faz o teu servo diante de ti.
20 Para que os teus olhos estejam abertos dia e noite sobre esta casa, sobre este lugar, do qual disseste que o teu nome estaria ali; para ouvires a oração que o teu servo fizer neste lugar.
21 Ouve, pois, a súplica do teu servo e do teu povo de Israel, quando orarem neste lugar; ouve do lugar da tua habitação, dos céus; ouve e perdoa.
22 Quando alguém pecar contra o seu próximo, e lhe for exigido que jure, e ele vier a jurar diante do teu altar nesta casa,
23 ouve tu dos céus, age e julga a teus servos, dando a paga ao perverso, fazendo recair o seu proceder sobre a sua cabeça e justificando ao justo, para lhe retribuíres segundo a sua justiça.
24 Quando o teu povo de Israel, por ter pecado contra ti, for ferido diante do inimigo, e se converter, e confessar o teu nome, e orar, e suplicar diante de ti nesta casa,
25 ouve tu dos céus, e perdoa o pecado do teu povo de Israel, e faze-o voltar à terra que lhe deste e a seus pais.
26 Quando os céus se cerrarem, e não houver chuva, por ter o povo pecado contra ti, e ele orar neste lugar, e confessar o teu nome, e se converter dos seus pecados, havendo-o tu afligido,
27 ouve tu nos céus, perdoa o pecado de teus servos e do teu povo de Israel, ensinando-lhes o bom caminho em que andem, e dá chuva na tua terra que deste em herança ao teu povo.
28 Quando houver fome na terra ou peste, quando houver crestamento ou ferrugem, gafanhotos e larvas, quando o seu inimigo o cercar em qualquer das suas cidades ou houver alguma praga ou doença,
29 toda oração e súplica, que qualquer homem ou todo o teu povo de Israel fizer, conhecendo cada um a sua própria chaga e a sua dor, e estendendo as mãos para o rumo desta casa,
30 ouve tu dos céus, lugar da tua habitação, perdoa e dá a cada um segundo todos os seus caminhos, já que lhe conheces o coração, porque tu, só tu, és conhecedor do coração dos filhos dos homens;
31 para que te temam, para andarem nos teus caminhos, todos os dias que viverem na terra que deste a nossos pais.
32 Também ao estrangeiro que não for do teu povo de Israel, porém vier de terras remotas, por amor do teu grande nome e por causa da tua mão poderosa e do teu braço estendido, e orar, voltado para esta casa,
33 ouve tu dos céus, do lugar da tua habitação, e faze tudo o que o estrangeiro te pedir, a fim de que todos os povos da terra conheçam o teu nome, para te temerem como o teu povo de Israel e para saberem que esta casa, que eu edifiquei, é chamada pelo teu nome.
34 Quando o teu povo sair à guerra contra o seu inimigo, pelo caminho por que os enviares, e orarem a ti, voltados para esta cidade, que tu escolheste, e para a casa que edifiquei ao teu nome,
35 ouve tu dos céus a sua oração e a sua súplica e faze-lhes justiça.
36 Quando pecarem contra ti (pois não há homem que não peque), e tu te indignares contra eles e os entregares às mãos do inimigo, a fim de que os leve cativos a uma terra, longe ou perto esteja;
37 e na terra aonde forem levados caírem em si, e se converterem, e na terra do seu cativeiro te suplicarem, dizendo: Pecamos, e perversamente procedemos, e cometemos iniquidade; e se converterem a ti de todo o seu coração e de toda a sua alma,
38 na terra do seu cativeiro, para onde foram levados cativos, e orarem, voltados para a sua terra que deste a seus pais, para esta cidade que escolheste e para a casa que edifiquei ao teu nome,
39 ouve tu dos céus, do lugar da tua habitação, a sua prece e a sua súplica e faze-lhes justiça; perdoa ao teu povo que houver pecado contra ti.
40 Agora, pois, ó meu Deus, estejam os teus olhos abertos, e os teus ouvidos atentos à oração que se fizer deste lugar.
41 Levanta-te, pois, Senhor Deus, e entra para o teu repouso, tu e a arca do teu poder; os teus sacerdotes, ó Senhor Deus, se revistam de salvação, e os teus santos se alegrem do bem.
42 Ah! Senhor Deus, não repulses o teu ungido; lembra-te das misericórdias que usaste para com Davi, teu servo.*
1 Tendo Salomão acabado de orar, desceu fogo do céu e consumiu o holocausto e os sacrifícios; e a glória do Senhor encheu a casa.
2 Os sacerdotes não podiam entrar na Casa do Senhor, porque a glória do Senhor tinha enchido a Casa do Senhor.
3 Todos os filhos de Israel, vendo descer o fogo e a glória do Senhor sobre a casa, se encurvaram com o rosto em terra sobre o pavimento, e adoraram, e louvaram o Senhor, porque é bom, porque a sua misericórdia dura para sempre.
4 Então, o rei e todo o povo ofereceram sacrifícios diante do Senhor.
5 Ofereceu o rei Salomão em sacrifício vinte e dois mil bois e cento e vinte mil ovelhas.
6 Assim, o rei e todo o povo consagraram a Casa de Deus. Os sacerdotes estavam nos seus devidos lugares, como também os levitas com os instrumentos músicos do Senhor, que o rei Davi tinha feito para deles se utilizar nas ações de graças ao Senhor, porque a sua misericórdia dura para sempre. Os sacerdotes que tocavam as trombetas estavam defronte deles, e todo o Israel se mantinha em pé.
7 Salomão consagrou também o meio do átrio que estava diante da Casa do Senhor, porquanto ali prepararam os holocaustos e a gordura dos sacrifícios pacíficos; porque, no altar de bronze, que Salomão fizera, não podiam caber os holocaustos, as ofertas de manjares e a gordura dos sacrifícios pacíficos.
8 Assim, celebrou Salomão a festa por sete dias, e todo o Israel, com ele, uma grande congregação, desde a entrada de Hamate até ao rio do Egito.
9 Ao oitavo dia, começaram a celebrar a Festa dos Tabernáculos, porque, por sete dias, já haviam celebrado a consagração do altar; a festa durava sete dias.
10 No vigésimo terceiro dia do sétimo mês, o rei despediu o povo para as suas tendas; e todos se foram alegres e de coração contente por causa do bem que o Senhor fizera a Davi, a Salomão e a Israel, seu povo.
11 Assim, Salomão acabou a Casa do Senhor e a casa do rei; tudo quanto Salomão intentou fazer na Casa do Senhor e na sua casa, prosperamente o efetuou.
12 De noite, apareceu o Senhor a Salomão e lhe disse: Ouvi a tua oração e escolhi para mim este lugar para casa do sacrifício.
13 Se eu cerrar os céus de modo que não haja chuva, ou se ordenar aos gafanhotos que consumam a terra, ou se enviar a peste entre o meu povo;
14 se o meu povo, que se chama pelo meu nome, se humilhar, e orar, e me buscar, e se converter dos seus maus caminhos, então, eu ouvirei dos céus, perdoarei os seus pecados e sararei a sua terra.
15 Estarão abertos os meus olhos e atentos os meus ouvidos à oração que se fizer neste lugar.
16 Porque escolhi e santifiquei esta casa, para que nela esteja o meu nome perpetuamente; nela, estarão fixos os meus olhos e o meu coração todos os dias.
17 Quanto a ti, se andares diante de mim, como andou Davi, teu pai, e fizeres segundo tudo o que te ordenei, e guardares os meus estatutos e os meus juízos,
18 também confirmarei o trono do teu reino, segundo a aliança que fiz com Davi, teu pai, dizendo: Não te faltará sucessor que domine em Israel.
19 Porém, se vós vos desviardes, e deixardes os meus estatutos e os meus mandamentos, que vos prescrevi, e fordes, e servirdes a outros deuses, e os adorardes,
20 então, vos arrancarei da minha terra que vos dei, e esta casa, que santifiquei ao meu nome, lançarei longe da minha presença, e a tornarei em provérbio e motejo entre todos os povos.
21 Desta casa, agora tão exaltada, todo aquele que por ela passar pasmará e dirá: Por que procedeu o Senhor assim para com esta terra e esta casa?
22 Responder-se-lhe-á: Porque deixaram o Senhor, o Deus de seus pais, que os tirou da terra do Egito, e se apegaram a outros deuses, e os adoraram, e os serviram. Por isso, trouxe sobre eles todo este mal.*
1 Ao fim de vinte anos, tendo Salomão terminado a Casa do Senhor e a sua própria casa,
2 edificou as cidades que Hirão lhe tinha dado; e fez habitar nelas os filhos de Israel.
3 Depois, foi Salomão a Hamate-Zoba e a tomou.
4 Também edificou a Tadmor no deserto e a todas as cidades-armazéns em Hamate.
5 Edificou também a Bete-Horom, a de cima e a de baixo, cidades fortificadas com muros, portas e ferrolhos;
6 como também a Baalate, e todas as cidades-armazéns que Salomão tinha, e todas as cidades para os carros, e as cidades para os cavaleiros, e tudo o que desejou, enfim, edificar em Jerusalém, no Líbano e em toda a terra do seu domínio.
7 Quanto a todo o povo que restou dos heteus, amorreus, ferezeus, heveus e jebuseus e que não eram de Israel,
8 a seus filhos, que restaram depois deles na terra, os quais os filhos de Israel não puderam destruir totalmente, a esses fez Salomão trabalhadores forçados, até hoje.
9 Porém dos filhos de Israel não fez Salomão escravo algum; eram homens de guerra, seus comandantes, chefes dos seus carros e dos seus cavaleiros;
10 estes eram os principais oficiais que tinha o rei Salomão, duzentos e cinquenta, que presidiam sobre o povo.
11 Salomão fez subir a filha de Faraó da Cidade de Davi para a casa que a ela lhe edificara; porque disse: Minha esposa não morará na casa de Davi, rei de Israel, porque santos são os lugares nos quais entrou a arca do Senhor.
12 Então, Salomão ofereceu holocaustos ao Senhor, sobre o altar que tinha edificado ao Senhor diante do pórtico;
13 e isto segundo o dever de cada dia, conforme o preceito de Moisés, nos sábados, nas Festas da Lua Nova, e nas festas fixas, três vezes no ano: na Festa dos Pães Asmos, na Festa das Semanas e na Festa dos Tabernáculos.
14 Também, segundo a ordem de Davi, seu pai, dispôs os turnos dos sacerdotes nos seus ministérios, como também os dos levitas para os seus cargos, para louvarem a Deus e servirem diante dos sacerdotes, segundo o dever de cada dia, e os porteiros pelos seus turnos a cada porta; porque tal era a ordem de Davi, o homem de Deus.
15 Não se desviaram do que ordenara o rei aos sacerdotes e levitas, em coisa nenhuma, nem acerca dos tesouros.
16 Assim se executou toda a obra de Salomão, desde o dia da fundação da Casa do Senhor até se acabar; e assim se concluiu a Casa do Senhor.
17 Então, foi Salomão a Eziom-Geber e a Elate, à praia do mar, na terra de Edom.
18 Enviou-lhe Hirão, por intermédio de seus servos, navios e marinheiros práticos; foram com os servos de Salomão a Ofir e tomaram de lá quatrocentos e cinquenta talentos de ouro, que trouxeram ao rei Salomão.*
1 Tendo a rainha de Sabá ouvido a fama de Salomão, veio a Jerusalém prová-lo com perguntas difíceis, com mui grande comitiva; com camelos carregados de especiarias, de ouro em abundância e pedras preciosas; compareceu perante Salomão e lhe expôs tudo quanto trazia em sua mente.
2 Salomão lhe deu resposta a todas as perguntas, e nada lhe houve profundo demais que não pudesse explicar.
3 Vendo, pois, a rainha de Sabá a sabedoria de Salomão, e a casa que edificara,
4 e a comida da sua mesa, o lugar dos seus oficiais, o serviço dos seus criados, e os trajes deles, seus copeiros, e os seus trajes, e o holocausto que oferecia na Casa do Senhor, ficou como fora de si
5 e disse ao rei: Foi verdade a palavra que a teu respeito ouvi na minha terra e a respeito da tua sabedoria.
6 Eu, contudo, não cria no que se falava, até que vim e vi com os próprios olhos. Eis que não me contaram a metade da grandeza da tua sabedoria; sobrepujas a fama que ouvi.
7 Felizes os teus homens, felizes estes teus servos que estão sempre diante de ti e ouvem a tua sabedoria!
8 Bendito seja o Senhor, teu Deus, que se agradou de ti para te colocar no seu trono como rei para o Senhor, teu Deus; porque o teu Deus ama a Israel para o estabelecer para sempre; por isso, te constituiu rei sobre ele, para executares juízo e justiça.
9 Deu ela ao rei cento e vinte talentos de ouro, especiarias em grande abundância e pedras preciosas, e nunca houve especiarias tais como as que a rainha de Sabá deu ao rei Salomão.
10 Os servos de Hirão e os servos de Salomão, que de Ofir tinham trazido ouro, trouxeram também madeira de sândalo e pedras preciosas.
11 Desta madeira de sândalo fez o rei balaústres para a Casa do Senhor e para a casa real, como também harpas e alaúdes para os cantores, quais nunca dantes se viram na terra de Judá.
12 O rei Salomão deu à rainha de Sabá, além do equivalente ao que ela lhe trouxera, mais tudo o que ela desejou e pediu. Assim, voltou e foi para a sua terra, ela e os seus servos.13 O peso do ouro que se trazia a Salomão cada ano era de seiscentos e sessenta e seis talentos,
14 afora o que entrava dos vendedores e dos negociantes; também todos os reis da Arábia e os governadores dessa mesma terra traziam a Salomão ouro e prata.
15 Fez o rei Salomão duzentos paveses de ouro batido; seiscentos siclos de ouro batido mandou pesar para cada pavês.
16 Fez também trezentos escudos de ouro batido; trezentos siclos de ouro mandou pesar para cada escudo. E o rei os pôs na Casa do Bosque do Líbano.
17 Fez mais o rei um grande trono de marfim e o cobriu de ouro puro.
18 O trono tinha seis degraus e um estrado de ouro a ele pegado; de ambos os lados, tinha braços junto ao assento e dois leões junto aos braços.
19 Também doze leões estavam ali sobre os seis degraus, um em cada extremo destes. Nunca se fizera obra semelhante em nenhum dos reinos.
20 Todas as taças de que se servia o rei Salomão para beber eram de ouro, e também de ouro puro, todas as da Casa do Bosque do Líbano; à prata, nos dias de Salomão, não se dava estimação nenhuma.
21 Porque o rei tinha navios que iam a Társis, com os servos de Hirão; de três em três anos, voltavam os navios de Társis, trazendo ouro e prata, marfim, bugios e pavões.
22 Assim, o rei Salomão excedeu a todos os reis do mundo, tanto em riqueza como em sabedoria.
23 Todos os reis do mundo procuravam ir ter com ele para ouvir a sabedoria que Deus lhe pusera no coração.
24 Cada um trazia o seu presente, objetos de prata e de ouro, roupas, armaduras, especiarias, cavalos e mulas; assim ano após ano.
25 Tinha Salomão quatro mil cavalos em estrebarias para os seus carros e doze mil cavaleiros, que distribuiu às cidades para os carros e junto ao rei, em Jerusalém.
26 Dominava Salomão sobre todos os reis desde o Eufrates até à terra dos filisteus e até ao limite do Egito.
27 Fez o rei que, em Jerusalém, houvesse prata como pedras e cedros em abundância como os sicômoros que estão nas planícies.
28 Importavam-se cavalos para Salomão, do Egito e de todas as terras.
29 Quanto aos mais atos de Salomão, tanto os primeiros como os últimos, porventura, não estão escritos no Livro da História de Natã, o profeta, e na Profecia de Aías, o silonita, e nas Visões de Ido, o vidente, acerca de Jeroboão, filho de Nebate?
30 Quarenta anos reinou Salomão em Jerusalém sobre todo o Israel.
31 Descansou com seus pais e foi sepultado na Cidade de Davi, seu pai, e Roboão, seu filho, reinou em seu lugar.*
1 Foi Roboão a Siquém, porque todo o Israel se reuniu lá, para o fazer rei.
2 Tendo Jeroboão, filho de Nebate, ouvido isso (pois estava ainda no Egito, para onde fugira da presença do rei Salomão), voltou do Egito.
3 Mandaram chamá-lo; veio ele com todo o Israel a Roboão, e lhe falaram:
4 Teu pai fez pesado o nosso jugo; agora, pois, alivia tu a dura servidão de teu pai e o seu pesado jugo que nos impôs, e nós te serviremos.
5 Ele lhes respondeu: Após três dias, voltai a mim. E o povo se foi.
6 Tomou o rei Roboão conselho com os homens idosos que estiveram na presença de Salomão, seu pai, quando este ainda vivia, dizendo: Como aconselhais que se responda a este povo?
7 Eles lhe disseram: Se te fizeres benigno para com este povo, e lhes agradares, e lhes falares boas palavras, eles se farão teus servos para sempre.
8 Porém ele desprezou o conselho que os anciãos lhe tinham dado e tomou conselho com os jovens que haviam crescido com ele e o serviam.
9 E disse-lhes: Que aconselhais vós que respondamos a este povo, que me falou, dizendo: Alivia o jugo que teu pai nos impôs?
10 E os jovens que haviam crescido com ele lhe disseram: Assim falarás ao povo que disse: Teu pai fez pesado o nosso jugo, mas alivia-o de sobre nós; assim lhe falarás: Meu dedo mínimo é mais grosso do que os lombos de meu pai.
11 Assim que, se meu pai vos impôs jugo pesado, eu ainda vo-lo aumentarei; meu pai vos castigou com açoites, porém eu vos castigarei com escorpiões.
12 Veio, pois, Jeroboão e todo o povo, ao terceiro dia, a Roboão, como o rei lhes ordenara, dizendo: Voltai a mim, ao terceiro dia.
13 Dura resposta lhes deu o rei, porque o rei Roboão desprezara o conselho dos anciãos;
14 e lhes falou segundo o conselho dos jovens, dizendo: Meu pai fez pesado o vosso jugo, porém eu ainda o agravarei; meu pai vos castigou com açoites, eu, porém, vos castigarei com escorpiões.
15 O rei, pois, não deu ouvidos ao povo, porque isto vinha de Deus, para que o Senhor confirmasse a palavra que tinha dito por intermédio de Aías, o silonita, a Jeroboão, filho de Nebate.
16 Vendo, pois, todo o Israel que o rei não lhe dava ouvidos, reagiu, dizendo: Que parte temos nós com Davi? Não há para nós herança no filho de Jessé! Cada homem à sua tenda, ó Israel! Cuida, agora, da tua casa, ó Davi! Então, Israel se foi às suas tendas.
17 Quanto aos filhos de Israel, porém, que habitavam nas cidades de Judá, sobre eles reinou Roboão.
18 Então, o rei Roboão enviou a Adorão, superintendente dos que trabalhavam forçados, porém os filhos de Israel o apedrejaram, e morreu. Mas o rei Roboão conseguiu tomar o seu carro e fugir para Jerusalém.
19 Assim, Israel se mantém rebelado contra a casa de Davi até ao dia de hoje.*
1 Vindo, pois, Roboão a Jerusalém, reuniu a casa de Judá e de Benjamim, cento e oitenta mil escolhidos, destros para a guerra, para pelejar contra Israel, a fim de restituir o reino a Roboão.
2 Porém veio a palavra do Senhor a Semaías, homem de Deus, dizendo:
3 Fala a Roboão, filho de Salomão, rei de Judá, e a todo o Israel em Judá e Benjamim, dizendo:
4 Assim diz o Senhor: Não subireis, nem pelejareis contra vossos irmãos; cada um volte para sua casa, porque eu é que fiz isto. E, obedecendo eles à palavra do Senhor, desistiram de subir contra Jeroboão.
5 Roboão habitou em Jerusalém e, para defesa, fortificou cidades em Judá;
6 fortificou, pois, a Belém, a Etã, a Tecoa,
7 a Bete-Zur, a Socó, a Adulão,
8 a Gate, a Maressa, a Zife,
9 a Adoraim, a Laquis, a Azeca,
10 a Zorá, a Aijalom e a Hebrom, todas em Judá e Benjamim, cidades fortificadas.
11 Assim, as tornou em fortalezas e pôs nelas comandantes e depósitos de víveres, de azeite e de vinho.
12 E pôs em cada cidade arsenal de paveses e lanças; fortificou-as sobremaneira. Judá e Benjamim ficaram-lhe sujeitas.
13 Também os sacerdotes e os levitas que havia em todo o Israel recorreram a Roboão de todos os seus limites,
14 porque os levitas deixaram os arredores das suas cidades e as suas possessões e vieram para Judá e para Jerusalém, porque Jeroboão e seus filhos os lançaram fora, para que não ministrassem ao Senhor.
15 Jeroboão constituiu os seus próprios sacerdotes, para os altos, para os sátiros e para os bezerros que fizera.
16 Além destes, também de todas as tribos de Israel os que de coração resolveram buscar o Senhor, Deus de Israel, foram a Jerusalém, para oferecerem sacrifícios ao Senhor, Deus de seus pais.
17 Assim, fortaleceram o reino de Judá e corroboraram com Roboão, filho de Salomão, por três anos; porque três anos andaram no caminho de Davi e Salomão.
18 Roboão tomou por esposa a Maalate, filha de Jerimote, filho de Davi, e filha de Abiail, filha de Eliabe, filho de Jessé,
19 a qual lhe deu filhos: Jeús, Semarias e Zaão.
20 Depois dela, tomou a Maaca, filha de Absalão; esta lhe deu a Abias, a Atai, a Ziza e a Selomite.
21 Amava Roboão mais a Maaca, filha de Absalão, do que a todas as suas outras mulheres e concubinas; porque ele havia tomado dezoito mulheres e sessenta concubinas; e gerou vinte e oito filhos e sessenta filhas.
22 Roboão designou a Abias, filho de Maaca, para ser chefe, príncipe entre seus irmãos, porque o queria fazer rei.
23 Procedeu prudentemente e distribuiu todos os seus filhos por todas as terras de Judá e Benjamim, por todas as cidades fortificadas; deu-lhes víveres em abundância e lhes procurou muitas mulheres.*
1 Tendo Roboão confirmado o reino e havendo-se fortalecido, deixou a lei do Senhor, e, com ele, todo o Israel.
2 No ano quinto do rei Roboão, Sisaque, rei do Egito, subiu contra Jerusalém (porque tinham transgredido contra o Senhor),
3 com mil e duzentos carros e sessenta mil cavaleiros; era inumerável a gente que vinha com ele do Egito, de líbios, suquitas e etíopes.
4 Tomou as cidades fortificadas que pertenciam a Judá e veio a Jerusalém.
5 Então, veio Semaías, o profeta, a Roboão e aos príncipes de Judá, que, por causa de Sisaque, se ajuntaram em Jerusalém, e disse-lhes: Assim diz o Senhor: Vós me deixastes a mim, pelo que eu também vos deixei em poder de Sisaque.
6 Então, se humilharam os príncipes de Israel e o rei e disseram: O Senhor é justo.
7 Vendo, pois, o Senhor que se humilharam, veio a palavra do Senhor a Semaías, dizendo: Humilharam-se, não os destruirei; antes, em breve lhes darei socorro, para que o meu furor não se derrame sobre Jerusalém, por intermédio de Sisaque.
8 Porém serão seus servos, para que conheçam a diferença entre a minha servidão e a servidão dos reinos da terra.
9 Subiu, pois, Sisaque, rei do Egito, contra Jerusalém e tomou os tesouros da Casa do Senhor e os tesouros da casa do rei; tomou tudo. Também levou todos os escudos de ouro que Salomão tinha feito.
10 Em lugar destes fez o rei Roboão escudos de bronze e os entregou nas mãos dos capitães da guarda, que guardavam a porta da casa do rei.
11 Toda vez que o rei entrava na Casa do Senhor, os da guarda vinham, e usavam os escudos, e tornavam a trazê-los para a câmara da guarda.
12 Tendo-se ele humilhado, apartou-se dele a ira do Senhor para que não o destruísse de todo; porque em Judá ainda havia boas coisas.
13 Fortificou-se, pois, o rei Roboão em Jerusalém e continuou reinando. Tinha Roboão quarenta e um anos de idade quando começou a reinar e reinou dezessete anos em Jerusalém, cidade que o Senhor escolheu dentre todas as tribos de Israel, para ali estabelecer o seu nome. Sua mãe se chamava Naamá, amonita.
14 Fez ele o que era mau, porquanto não dispôs o coração para buscar ao Senhor.
15 Quanto aos mais atos de Roboão, tanto os primeiros como os últimos, porventura, não estão escritos no Livro da História de Semaías, o profeta, e no de Ido, o vidente, no registro das genealogias? Houve guerras entre Roboão e Jeroboão todos os seus dias.
16 Descansou Roboão com seus pais e foi sepultado na Cidade de Davi; e Abias, seu filho, reinou em seu lugar.*
1 No décimo oitavo ano do rei Jeroboão, Abias começou a reinar sobre Judá. Três anos reinou em Jerusalém.
2 Era o nome de sua mãe Micaía, filha de Uriel, de Gibeá. Também houve guerra entre Abias e Jeroboão.
3 Abias ordenou a peleja com um exército de valentes guerreiros, de quatrocentos mil homens escolhidos; e Jeroboão dispôs contra ele a batalha com oitocentos mil homens escolhidos, todos guerreiros valentes.
4 Pôs-se Abias em pé no alto do monte Zemaraim, que está na região montanhosa de Efraim, e disse: Ouvi-me, Jeroboão e todo o Israel:
5 Não vos convém saber que o Senhor, Deus de Israel, deu para sempre a Davi a soberania de Israel, a ele e a seus filhos, por uma aliança de sal?
6 Contudo, se levantou Jeroboão, filho de Nebate, servo de Salomão, filho de Davi, e se rebelou contra seu senhor.
7 Ajuntou-se a ele gente vadia, homens malignos; fortificaram-se contra Roboão, filho de Salomão; sendo Roboão ainda jovem e indeciso, não lhes pôde resistir.
8 Agora, pensais que podeis resistir ao reino do Senhor, que está nas mãos dos filhos de Davi; bem sois vós uma grande multidão e tendes convosco os bezerros de ouro que Jeroboão vos fez para deuses.
9 Não lançastes fora os sacerdotes do Senhor, os filhos de Arão e os levitas, e não fizestes para vós outros sacerdotes, como as gentes das outras terras? Qualquer que vem a consagrar-se com um novilho e sete carneiros logo se faz sacerdote daqueles que não são deuses.
10 Porém, quanto a nós, o Senhor é nosso Deus, e nunca o deixamos; temos sacerdotes, que ministram ao Senhor, a saber, os filhos de Arão e os levitas na sua obra.
11 Cada dia, de manhã e à tarde, oferecem holocaustos e queimam incenso aromático, dispondo os pães da proposição sobre a mesa puríssima e o candeeiro de ouro e as suas lâmpadas para se acenderem cada tarde, porque nós guardamos o preceito do Senhor, nosso Deus; porém vós o deixastes.
12 Eis que Deus está conosco, à nossa frente, como também os seus sacerdotes, tocando com as trombetas, para rebate contra vós outros, ó filhos de Israel; não pelejeis contra o Senhor, Deus de vossos pais, porque não sereis bem-sucedidos.
13 Mas Jeroboão ordenou aos que estavam de emboscada que fizessem uma volta e dessem contra eles por detrás; de maneira que estavam em frente dos homens de Judá, e a emboscada, por detrás deles.
14 Olhou Judá e viu que a peleja estava por diante e por detrás; então, clamaram ao Senhor, e os sacerdotes tocaram as trombetas.
15 Os homens de Judá gritaram; quando gritavam, feriu Deus a Jeroboão e a todo o Israel diante de Abias e de Judá.
16 Os filhos de Israel fugiram de diante de Judá, pois Deus os entregara nas suas mãos.
17 De maneira que Abias e o seu povo fizeram grande matança entre eles; porque caíram feridos de Israel quinhentos mil homens escolhidos.
18 Assim, foram humilhados os filhos de Israel naquele tempo; prevaleceram os filhos de Judá, porque confiaram no Senhor, Deus de seus pais.
19 Abias perseguiu a Jeroboão e lhe tomou cidades: Betel, Jesana e Efrom, com suas respectivas vilas.
20 Jeroboão não restaurou mais o seu poder no tempo de Abias; feriu o Senhor a Jeroboão, que morreu.
21 Abias, porém, se fortificou, e tomou para si catorze mulheres, e gerou vinte e dois filhos e dezesseis filhas.
22 Quanto aos mais atos de Abias, tanto o que fez como o que disse, estão escritos no Livro da História do Profeta Ido.*
1 Abias descansou com seus pais, e o sepultaram na Cidade de Davi. Em seu lugar reinou seu filho Asa, em cujos dias a terra esteve em paz dez anos.
2 Asa fez o que era bom e reto perante o Senhor, seu Deus.
3 Porque aboliu os altares dos deuses estranhos e o culto nos altos, quebrou as colunas e cortou os postes-ídolos.
4 Ordenou a Judá que buscasse ao Senhor, Deus de seus pais, e que observasse a lei e o mandamento.
5 Também aboliu de todas as cidades de Judá o culto nos altos e os altares do incenso; e houve paz no seu reinado.
6 Edificou cidades fortificadas em Judá, pois havia paz na terra, e não houve guerra contra ele naqueles anos, porquanto o Senhor lhe dera repouso.
7 Disse, pois, a Judá: Edifiquemos estas cidades, cerquemo-las de muros e torres, portas e ferrolhos, enquanto a terra ainda está em paz diante de nós, pois temos buscado ao Senhor, nosso Deus; temo-lo buscado, e ele nos deu repouso de todos os lados.
8 Edificaram e prosperaram. Tinha Asa, no seu exército, trezentos mil de Judá, que traziam pavês e lança, e duzentos e oitenta mil de Benjamim, que traziam escudo e atiravam com arco; todos eram homens valentes.
9 Zerá, o etíope, saiu contra eles, com um exército de um milhão de homens e trezentos carros, e chegou até Maressa.
10 Então, Asa saiu contra ele; e ordenaram a batalha no vale de Zefatá, perto de Maressa.
11 Clamou Asa ao Senhor, seu Deus, e disse: Senhor, além de ti não há quem possa socorrer numa batalha entre o poderoso e o fraco; ajuda-nos, pois, Senhor, nosso Deus, porque em ti confiamos e no teu nome viemos contra esta multidão. Senhor, tu és o nosso Deus, não prevaleça contra ti o homem.
12 O Senhor feriu os etíopes diante de Asa e diante de Judá; e eles fugiram.
13 Asa e o povo que estava com ele os perseguiram até Gerar; e caíram os etíopes sem restar nem um sequer; porque foram destroçados diante do Senhor e diante do seu exército, e levaram dali mui grande despojo.
14 Feriram todas as cidades ao redor de Gerar, porque o terror do Senhor as havia invadido; e saquearam todas as cidades, porque havia nelas muita presa.
15 Também feriram as tendas dos donos do gado, levaram ovelhas em abundância e camelos e voltaram para Jerusalém.*
1 Veio o Espírito de Deus sobre Azarias, filho de Odede.
2 Este saiu ao encontro de Asa e lhe disse: Ouvi-me, Asa, e todo o Judá, e Benjamim. O Senhor está convosco, enquanto vós estais com ele; se o buscardes, ele se deixará achar; porém, se o deixardes, vos deixará.
3 Israel esteve por muito tempo sem o verdadeiro Deus, sem sacerdote que o ensinasse e sem lei.
4 Mas, quando, na sua angústia, eles voltaram ao Senhor, Deus de Israel, e o buscaram, foi por eles achado.
5 Naqueles tempos, não havia paz nem para os que saíam nem para os que entravam, mas muitas perturbações sobre todos os habitantes daquelas terras.
6 Porque nação contra nação e cidade contra cidade se despedaçavam, pois Deus os conturbou com toda sorte de angústia.
7 Mas sede fortes, e não desfaleçam as vossas mãos, porque a vossa obra terá recompensa.
8 Ouvindo, pois, Asa estas palavras e a profecia do profeta, filho de Odede, cobrou ânimo e lançou as abominações fora de toda a terra de Judá e de Benjamim, como também das cidades que tomara na região montanhosa de Efraim; e renovou o altar do Senhor, que estava diante do pórtico do Senhor.
9 Congregou todo o Judá e Benjamim e também os de Efraim, Manassés e Simeão que moravam no seu meio, porque muitos de Israel desertaram para ele, vendo que o Senhor, seu Deus, era com ele.
10 Reuniram-se, em Jerusalém, no terceiro mês, no décimo quinto ano do reinado de Asa.
11 Naquele dia, ofereceram em sacrifício ao Senhor, do despojo que trouxeram, setecentos bois e sete mil ovelhas.
12 Entraram em aliança de buscarem ao Senhor, Deus de seus pais, de todo o coração e de toda a alma;
13 e de que todo aquele que não buscasse ao Senhor, Deus de Israel, morresse, tanto o menor como o maior, tanto homem como mulher.
14 Juraram ao Senhor, em alta voz, com júbilo, e com clarins, e com trombetas.
15 Todo o Judá se alegrou por motivo deste juramento, porque, de todo o coração, eles juraram e, de toda a boa vontade, buscaram ao Senhor, e por eles foi achado. O Senhor lhes deu paz por toda parte.
16 O rei Asa depôs também a Maaca, sua mãe, da dignidade de rainha-mãe, porquanto ela havia feito a Aserá, uma abominável imagem; Asa destruiu-lhe a imagem, que, feita em pó, queimou no vale de Cedrom.
17 Os altos, porém, não foram tirados de Israel; todavia, o coração de Asa foi perfeito todos os seus dias.
18 Trouxe à Casa de Deus as coisas consagradas por seu pai e as coisas que ele mesmo consagrara: prata, ouro e objetos de utilidade.
19 Não houve guerra até ao trigésimo quinto ano do reinado de Asa.*
1 No trigésimo sexto ano do reinado de Asa, subiu Baasa, rei de Israel, contra Judá e edificou a Ramá, para que a ninguém fosse permitido sair de junto de Asa, rei de Judá, nem chegar a ele.
2 Então, Asa tomou prata e ouro dos tesouros da Casa do Senhor e dos tesouros da casa do rei e enviou servos a Ben-Hadade, rei da Síria, que habitava em Damasco, dizendo:
3 Haja aliança entre mim e ti, como houve entre meu pai e teu pai. Eis que te mando prata e ouro; vai e anula a tua aliança com Baasa, rei de Israel, para que se retire de mim.
4 Ben-Hadade deu ouvidos ao rei Asa e enviou os capitães dos seus exércitos contra as cidades de Israel; e feriu a Ijom, a Dã, a Abel-Maim e todas as cidades-armazéns de Naftali.
5 Ouvindo isso Baasa, deixou de edificar a Ramá e não continuou a sua obra.
6 Então, o rei Asa tomou todo o Judá, e trouxeram as pedras de Ramá e a sua madeira com que Baasa a edificara; com elas edificou Asa a Geba e a Mispa.
7 Naquele tempo, veio Hanani a Asa, rei de Judá, e lhe disse: Porquanto confiaste no rei da Síria e não confiaste no Senhor, teu Deus, o exército do rei da Síria escapou das tuas mãos.
8 Acaso, não foram os etíopes e os líbios grande exército, com muitíssimos carros e cavaleiros? Porém, tendo tu confiado no Senhor, ele os entregou nas tuas mãos.
9 Porque, quanto ao Senhor, seus olhos passam por toda a terra, para mostrar-se forte para com aqueles cujo coração é totalmente dele; nisto procedeste loucamente; por isso, desde agora, haverá guerras contra ti.
10 Porém Asa se indignou contra o vidente e o lançou no cárcere, no tronco, porque se enfurecera contra ele por causa disso; na mesma ocasião, oprimiu Asa alguns do povo.
11 Eis que os mais atos de Asa, tanto os primeiros como os últimos, estão escritos no Livro da História dos Reis de Judá e Israel.
12 No trigésimo nono ano do seu reinado, caiu Asa doente dos pés; a sua doença era em extremo grave; contudo, na sua enfermidade não recorreu ao Senhor, mas confiou nos médicos.
13 Descansou Asa com seus pais; morreu no quadragésimo primeiro ano do seu reinado.
14 Sepultaram-no no sepulcro que mandara abrir para si na Cidade de Davi; puseram-no sobre um leito, que se enchera de perfumes e de várias especiarias, preparados segundo a arte dos perfumistas. Foi mui grande a queima que lhe fizeram destas coisas.*
1 Em lugar de Asa, reinou seu filho Josafá, que se fortificou contra Israel;
2 ele pôs tropas em todas as cidades fortificadas de Judá e estabeleceu guarnições na terra de Judá, como também nas cidades de Efraim, que Asa, seu pai, tinha tomado.
3 O Senhor foi com Josafá, porque andou nos primeiros caminhos de Davi, seu pai, e não procurou a baalins.
4 Antes, procurou ao Deus de seu pai e andou nos seus mandamentos e não segundo as obras de Israel.
5 O Senhor confirmou o reino nas suas mãos, e todo o Judá deu presentes a Josafá, o qual teve riquezas e glória em abundância.
6 Tornou-se-lhe ousado o coração em seguir os caminhos do Senhor, e ainda tirou os altos e os postes-ídolos de Judá.
7 No terceiro ano do seu reinado, enviou ele os seus príncipes Ben-Hail, Obadias, Zacarias, Natanael e Micaías, para ensinarem nas cidades de Judá;
8 e, com eles, os levitas Semaías, Netanias, Zebadias, Asael, Semiramote, Jônatas, Adonias, Tobias e Tobe-Adonias; e, com estes levitas, os sacerdotes Elisama e Jeorão.
9 Ensinaram em Judá, tendo consigo o Livro da Lei do Senhor; percorriam todas as cidades de Judá e ensinavam ao povo.
10 Veio o terror do Senhor sobre todos os reinos das terras que estavam ao redor de Judá, de maneira que não fizeram guerra contra Josafá.
11 Alguns dos filisteus traziam presentes a Josafá e prata como tributo; também os arábios lhe trouxeram gado miúdo, sete mil e setecentos carneiros e sete mil e setecentos bodes.
12 Josafá se engrandeceu em extremo, continuamente; e edificou fortalezas e cidades-armazéns em Judá.
13 Empreendeu muitas obras nas cidades de Judá; e tinha, em Jerusalém, gente de guerra e homens valentes.
14 Este é o número deles segundo as suas famílias: em Judá, eram capitães de mil: o chefe Adna e, com ele, trezentos mil homens valentes;
15 depois dele, o capitão Joanã e, com ele, duzentos e oitenta mil;
16 e, depois, Amasias, filho de Zicri, que, voluntariamente, se ofereceu ao serviço do Senhor, e, às suas ordens, duzentos mil homens valentes.
17 De Benjamim, Eliada, homem valente, e, com ele, duzentos mil, armados de arco e de escudo;
18 depois dele, Jozabade, com cento e oitenta mil armados para a guerra.
19 Estavam estes no serviço do rei, afora os que o rei tinha posto nas cidades fortificadas por todo o Judá.*
1 Tinha Josafá riquezas e glória em abundância; e aparentou-se com Acabe.
2 Ao cabo de alguns anos, foi ter com Acabe, em Samaria. Acabe matou ovelhas e bois em abundância, para ele e para o povo que viera com ele; e o persuadiu a subir, com ele, a Ramote-Gileade.
3 Acabe, rei de Israel, perguntou a Josafá, rei de Judá: Irás tu, comigo, a Ramote-Gileade? Respondeu-lhe Josafá: Serei como tu és, o meu povo, como o teu povo; iremos, contigo, à peleja.
4 Disse mais Josafá ao rei de Israel: Consulta, primeiro, a palavra do Senhor.
5 Então, o rei de Israel ajuntou os profetas, quatrocentos homens, e lhes disse: Iremos à peleja contra Ramote-Gileade ou deixarei de ir? Eles disseram:
6 Sobe, porque Deus a entregará nas mãos do rei. Disse, porém, Josafá: Não há, aqui, ainda algum profeta do Senhor, para o consultarmos?
7 Respondeu o rei de Israel a Josafá: Há um ainda, por quem podemos consultar o Senhor; porém eu o aborreço, porque nunca profetiza de mim o que é bom, mas somente o que é mau.
8 Este é Micaías, filho de Inlá. Disse Josafá: Não fale o rei assim. Então, o rei de Israel chamou um oficial e disse: Traze-me depressa a Micaías, filho de Inlá.
9 O rei de Israel e Josafá, rei de Judá, estavam assentados, cada um no seu trono, vestidos de trajes reais, numa eira à entrada da porta de Samaria; e todos os profetas profetizavam diante deles.
10 Zedequias, filho de Quenaana, fez para si uns chifres de ferro e disse: Assim diz o Senhor: Com este, escornearás os siros, até de todo os consumir.
11 Todos os profetas profetizaram assim, dizendo: Sobe a Ramote-Gileade e triunfarás, porque o Senhor a entregará nas mãos do rei.
12 O mensageiro que fora chamar a Micaías falou-lhe, dizendo: Eis que as palavras dos profetas, a uma voz, predizem coisas boas para o rei; seja, pois, a tua palavra como a palavra de um deles, e fala o que é bom.
13 Respondeu Micaías: Tão certo como vive o Senhor, o que meu Deus me disser, isso falarei.
14 E, vindo ele ao rei, este lhe perguntou: Micaías, iremos a Ramote-Gileade, à peleja, ou deixarei de ir? Ele respondeu: Sobe e triunfarás, porque eles serão entregues nas vossas mãos.
15 O rei lhe disse: Quantas vezes te conjurarei que não me fales senão a verdade em nome do Senhor?
16 Então, disse ele: Vi todo o Israel disperso pelos montes, como ovelhas que não têm pastor; e disse o Senhor: Estes não têm dono; torne cada um em paz para sua casa.
17 Então, o rei de Israel disse a Josafá: Não te disse eu que ele não profetiza a meu respeito o que é bom, mas somente o que é mau?
18 Micaías prosseguiu: Ouvi, pois, a palavra do Senhor: Vi o Senhor assentado no seu trono, e todo o exército do céu estava à sua direita e à sua esquerda.
19 Perguntou o Senhor: Quem enganará Acabe, o rei de Israel, para que suba e caia em Ramote-Gileade? Um dizia desta maneira, e outro, de outra.
20 Então, saiu um espírito, e se apresentou diante do Senhor, e disse: Eu o enganarei. Perguntou-lhe o Senhor: Com quê?
21 Respondeu ele: Sairei e serei espírito mentiroso na boca de todos os seus profetas. Disse o Senhor: Tu o enganarás e ainda prevalecerás; sai e faze-o assim.
22 Eis que o Senhor pôs o espírito mentiroso na boca de todos estes teus profetas e o Senhor falou o que é mau contra ti.
23 Então, Zedequias, filho de Quenaana, deu uma bofetada em Micaías e disse:
24 Por onde saiu o Espírito do Senhor para falar a ti? Disse Micaías: Eis que o verás naquele mesmo dia, quando entrares de câmara em câmara, para te esconderes.
25 Então, disse o rei de Israel: Tomai a Micaías e devolvei-o a Amom, governador da cidade, e a Joás, filho do rei;
26 e direis: Assim diz o rei: Metei este homem na casa do cárcere e angustiai-o com escassez de pão e de água, até que eu volte em paz.
27 Disse Micaías: Se voltares em paz, não falou o Senhor, na verdade, por mim. Disse mais: Ouvi isto, vós, todos os povos!
28 Subiram o rei de Israel e Josafá, rei de Judá, a Ramote-Gileade.
29 Disse o rei de Israel a Josafá: Eu me disfarçarei e entrarei na peleja; tu, porém, traja as tuas vestes. Disfarçou-se, pois, o rei de Israel, e entraram na peleja.
30 Ora, o rei da Síria dera ordem aos capitães dos seus carros, dizendo: Não pelejareis nem contra pequeno nem contra grande, mas somente contra o rei de Israel.
31 Vendo os capitães dos carros a Josafá, disseram: Este é o rei de Israel. Portanto, a ele se dirigiram para o atacar. Josafá, porém, gritou, e o Senhor o socorreu; Deus os desviou dele.
32 Vendo os capitães dos carros que não era o rei de Israel, deixaram de o perseguir.
33 Então, um homem entesou o arco e, atirando ao acaso, feriu o rei de Israel por entre as juntas da sua armadura; então, disse este ao seu cocheiro: Vira e leva-me para fora do combate, porque estou gravemente ferido.
34 A peleja tornou-se renhida naquele dia; quanto ao rei, segurou-se a si mesmo de pé no carro defronte dos siros, até à tarde, mas, ao pôr do sol, morreu.*
1 Josafá, rei de Judá, voltou para sua casa em paz, para Jerusalém.
2 O vidente Jeú, filho de Hanani, saiu ao encontro do rei Josafá e lhe disse: Devias tu ajudar ao perverso e amar aqueles que aborrecem o Senhor? Por isso, caiu sobre ti a ira da parte do Senhor.
3 Boas coisas, contudo, se acharam em ti; porque tiraste os postes-ídolos da terra e dispuseste o coração para buscares a Deus.
4 Habitou, pois, Josafá em Jerusalém; tornou a passar pelo povo desde Berseba até à região montanhosa de Efraim e fez que ele tornasse ao Senhor, Deus de seus pais.
5 Estabeleceu juízes no país, em todas as cidades fortificadas, de cidade em cidade.
6 Disse aos juízes: Vede o que fazeis, porque não julgais da parte do homem, e sim da parte do Senhor, e, no julgardes, ele está convosco.
7 Agora, pois, seja o temor do Senhor convosco; tomai cuidado e fazei-o, porque não há no Senhor, nosso Deus, injustiça, nem parcialidade, nem aceita ele suborno.
8 Também, depois de terem voltado para Jerusalém, estabeleceu aí Josafá alguns dos levitas, e dos sacerdotes, e dos cabeças das famílias de Israel para julgarem da parte do Senhor e decidirem as sentenças contestadas.
9 Deu-lhes ordem, dizendo: Assim, andai no temor do Senhor, com fidelidade e inteireza de coração.
10 Toda vez que vier a vós outros sentença contestada de vossos irmãos que habitam nas suas cidades: entre sangue e sangue, lei e mandamento, estatutos e juízos, admoestai-os, que não se façam culpados para com o Senhor, para que não venha grande ira sobre vós e sobre vossos irmãos; fazei assim e não vos tornareis culpados.
11 Eis que Amarias, o sumo sacerdote, presidirá nas coisas que dizem respeito ao Senhor; e Zebadias, filho de Ismael, príncipe da casa de Judá, nas que dizem respeito ao rei. Também os levitas serão oficiais à vossa disposição. Sede fortes no cumprimento disso, e o Senhor será com os bons.*
1 Depois disto, os filhos de Moabe e os filhos de Amom, com alguns dos meunitas, vieram à peleja contra Josafá.
2 Então, vieram alguns que avisaram a Josafá, dizendo: Grande multidão vem contra ti dalém do mar e da Síria; eis que já estão em Hazazom-Tamar, que é En-Gedi.
3 Então, Josafá teve medo e se pôs a buscar ao Senhor; e apregoou jejum em todo o Judá.
4 Judá se congregou para pedir socorro ao Senhor; também de todas as cidades de Judá veio gente para buscar ao Senhor.
5 Pôs-se Josafá em pé, na congregação de Judá e de Jerusalém, na Casa do Senhor, diante do pátio novo,
6 e disse: Ah! Senhor, Deus de nossos pais, porventura, não és tu Deus nos céus? Não és tu que dominas sobre todos os reinos dos povos? Na tua mão, está a força e o poder, e não há quem te possa resistir.
7 Porventura, ó nosso Deus, não lançaste fora os moradores desta terra de diante do teu povo de Israel e não a deste para sempre à posteridade de Abraão, teu amigo?
8 Habitaram nela e nela edificaram um santuário ao teu nome, dizendo:
9 Se algum mal nos sobrevier, espada por castigo, peste ou fome, nós nos apresentaremos diante desta casa e diante de ti, pois o teu nome está nesta casa; e clamaremos a ti na nossa angústia, e tu nos ouvirás e livrarás.
10 Agora, pois, eis que os filhos de Amom e de Moabe e os do monte Seir, cujas terras não permitiste a Israel invadir, quando vinham da terra do Egito, mas deles se desviaram e não os destruíram,
11 eis que nos dão o pago, vindo para lançar-nos fora da tua possessão, que nos deste em herança.
12 Ah! Nosso Deus, acaso, não executarás tu o teu julgamento contra eles? Porque em nós não há força para resistirmos a essa grande multidão que vem contra nós, e não sabemos nós o que fazer; porém os nossos olhos estão postos em ti.
13 Todo o Judá estava em pé diante do Senhor, como também as suas crianças, as suas mulheres e os seus filhos.
14 Então, veio o Espírito do Senhor no meio da congregação, sobre Jaaziel, filho de Zacarias, filho de Benaia, filho de Jeiel, filho de Matanias, levita, dos filhos de Asafe,
15 e disse: Dai ouvidos, todo o Judá e vós, moradores de Jerusalém, e tu, ó rei Josafá, ao que vos diz o Senhor. Não temais, nem vos assusteis por causa desta grande multidão, pois a peleja não é vossa, mas de Deus.
16 Amanhã, descereis contra eles; eis que sobem pela ladeira de Ziz; encontrá-los-eis no fim do vale, defronte do deserto de Jeruel.
17 Neste encontro, não tereis de pelejar; tomai posição, ficai parados e vede o salvamento que o Senhor vos dará, ó Judá e Jerusalém. Não temais, nem vos assusteis; amanhã, saí-lhes ao encontro, porque o Senhor é convosco.
18 Então, Josafá se prostrou com o rosto em terra; e todo o Judá e os moradores de Jerusalém também se prostraram perante o Senhor e o adoraram.
19 Dispuseram-se os levitas, dos filhos dos coatitas e dos coreítas, para louvarem o Senhor, Deus de Israel, em voz alta, sobremaneira.
20 Pela manhã cedo, se levantaram e saíram ao deserto de Tecoa; ao saírem eles, pôs-se Josafá em pé e disse: Ouvi-me, ó Judá e vós, moradores de Jerusalém! Crede no Senhor, vosso Deus, e estareis seguros; crede nos seus profetas e prosperareis.
21 Aconselhou-se com o povo e ordenou cantores para o Senhor, que, vestidos de ornamentos sagrados e marchando à frente do exército, louvassem a Deus, dizendo: Rendei graças ao Senhor, porque a sua misericórdia dura para sempre.
22 Tendo eles começado a cantar e a dar louvores, pôs o Senhor emboscadas contra os filhos de Amom e de Moabe e os do monte Seir que vieram contra Judá, e foram desbaratados.
23 Porque os filhos de Amom e de Moabe se levantaram contra os moradores do monte Seir, para os destruir e exterminar; e, tendo eles dado cabo dos moradores de Seir, ajudaram uns aos outros a destruir-se.
24 Tendo Judá chegado ao alto que olha para o deserto, procurou ver a multidão, e eis que eram corpos mortos, que jaziam em terra, sem nenhum sobrevivente.
25 Vieram Josafá e o seu povo para saquear os despojos e acharam entre os cadáveres riquezas em abundância e objetos preciosos; tomaram para si mais do que podiam levar e três dias saquearam o despojo, porque era muito.
26 Ao quarto dia, se ajuntaram no vale de Bênção, onde louvaram o Senhor; por isso, chamaram àquele lugar vale de Bênção, até ao dia de hoje.
27 Então, voltaram todos os homens de Judá e de Jerusalém, e Josafá, à frente deles, e tornaram para Jerusalém com alegria, porque o Senhor os alegrara com a vitória sobre seus inimigos.
28 Vieram para Jerusalém com alaúdes, harpas e trombetas, para a Casa do Senhor.
29 Veio da parte de Deus o terror sobre todos os reinos daquelas terras, quando ouviram que o Senhor havia pelejado contra os inimigos de Israel.
30 Assim, o reino de Josafá teve paz, porque Deus lhe dera repouso por todos os lados.
31 Josafá reinou sobre Judá; tinha trinta e cinco anos quando começou a reinar e reinou vinte e cinco anos em Jerusalém. Sua mãe se chamava Azuba, filha de Sili.
32 Ele andou no caminho de Asa, seu pai, e não se desviou dele, fazendo o que era reto perante o Senhor.
33 Contudo, os altos não se tiraram, porque o povo não tinha ainda disposto o coração para com o Deus de seus pais.
34 Quanto aos mais atos de Josafá, tanto os primeiros como os últimos, eis que estão escritos nas Crônicas registradas por Jeú, filho de Hanani, que as inseriu na História dos Reis de Israel.
35 Depois disto, Josafá, rei de Judá, se aliou com Acazias, rei de Israel, que procedeu iniquamente.
36 Aliou-se com ele, para fazerem navios que fossem a Társis; e fizeram os navios em Eziom-Geber.
37 Porém Eliézer, filho de Dodavá, de Maressa, profetizou contra Josafá, dizendo: Porquanto te aliaste com Acazias, o Senhor destruiu as tuas obras. E os navios se quebraram e não puderam ir a Társis.*
1 Descansou Josafá com seus pais e foi sepultado com eles na Cidade de Davi; e Jeorão, seu filho, reinou em seu lugar.
2 Teve este irmãos, filhos de Josafá: Azarias, Jeiel, Zacarias, Azarias, Micael e Sefatias; todos estes foram filhos de Josafá, rei de Israel.
3 Seu pai lhes fez muitas dádivas de prata, ouro e coisas preciosas e ainda de cidades fortificadas em Judá; porém o reino deu a Jeorão, por ser o primogênito.
4 Tendo Jeorão assumido o reino de seu pai e havendo-se fortificado, matou todos os seus irmãos à espada, como também alguns dos príncipes de Israel.
5 Era Jeorão da idade de trinta e dois anos quando começou a reinar e reinou oito anos em Jerusalém.
6 Andou nos caminhos dos reis de Israel, como também fizeram os da casa de Acabe, porque a filha deste era sua mulher; e fez o que era mau perante o Senhor.
7 Porém o Senhor não quis destruir a casa de Davi por causa da aliança que com ele fizera, segundo a promessa que lhe havia feito de dar a ele, sempre, uma lâmpada e a seus filhos.
8 Nos dias de Jeorão, se revoltaram os edomitas contra o poder de Judá e constituíram o seu próprio rei.
9 Pelo que Jeorão passou adiante com todos os seus chefes, e todos os carros, com ele; de noite, se levantou e feriu os edomitas que o cercavam e os capitães dos carros.
10 Assim, se rebelou Edom para livrar-se do poder de Judá, até ao dia de hoje; ao mesmo tempo, se rebelou também Libna contra Jeorão, porque este deixara ao Senhor, Deus de seus pais.
11 Também fez altos nos montes de Judá, e seduziu os habitantes de Jerusalém à idolatria, e fez desgarrar a Judá.
12 Então, lhe chegou às mãos uma carta do profeta Elias, em que estava escrito: Assim diz o Senhor, Deus de Davi, teu pai: Porquanto não andaste nos caminhos de Josafá, teu pai, e nos caminhos de Asa, rei de Judá,
13 mas andaste nos caminhos dos reis de Israel, e induziste à idolatria a Judá e os moradores de Jerusalém, segundo a idolatria da casa de Acabe, e também mataste a teus irmãos, da casa de teu pai, melhores do que tu,
14 eis que o Senhor castigará com grande flagelo ao teu povo, aos teus filhos, às tuas mulheres e todas as tuas possessões.
15 Tu terás grande enfermidade nas tuas entranhas, enfermidade que aumentará dia após dia, até que saiam as tuas entranhas.
16 Despertou, pois, o Senhor contra Jeorão o ânimo dos filisteus e dos arábios que estão do lado dos etíopes.
17 Estes subiram a Judá, deram contra ele e levaram todos os bens que se acharam na casa do rei, como também a seus filhos e as suas mulheres; de modo que não lhe deixaram filho algum, senão Jeoacaz, o mais moço deles.
18 Depois de tudo isto, o Senhor o feriu nas suas entranhas com enfermidade incurável.
19 E, aumentando esta dia após dia, ao cabo de dois anos, saíram-lhe as entranhas por causa da enfermidade, e morreu com terríveis agonias. O seu povo não lhe queimou aromas, como se fez a seus pais.
20 Era ele da idade de trinta e dois anos quando começou a reinar e reinou oito anos em Jerusalém. E se foi sem deixar de si saudades; sepultaram-no na Cidade de Davi, porém não nos sepulcros dos reis.*
1 Os moradores de Jerusalém, em lugar de Jeorão, fizeram rei a Acazias, seu filho mais moço; porque a tropa, que viera com os arábios ao arraial, tinha matado todos os mais velhos. Assim, reinou Acazias, filho de Jeorão, rei de Judá.
2 Era Acazias de vinte e dois anos de idade quando começou a reinar e reinou um ano em Jerusalém.
3 Sua mãe, filha de Onri, chamava-se Atalia. Ele também andou nos caminhos da casa de Acabe; porque sua mãe era quem o aconselhava a proceder iniquamente.
4 Fez o que era mau perante o Senhor, como os da casa de Acabe; porque eles eram seus conselheiros depois da morte de seu pai, para a sua perdição.
5 Também andou nos conselhos deles e foi com Jorão, filho de Acabe, rei de Israel, a Ramote-Gileade, à peleja contra Hazael, rei da Síria; e os siros feriram Jorão.
6 Então, voltou para Jezreel, para curar-se das feridas que lhe fizeram em Ramá, quando pelejou contra Hazael, rei da Síria; e desceu Acazias, filho de Jeorão, rei de Judá, para ver a Jorão, filho de Acabe, em Jezreel, porquanto estava doente.
7 Foi da vontade de Deus que Acazias, para a sua ruína, fosse visitar a Jorão; porque, vindo ele, saiu com Jorão para encontrar-se com Jeú, filho de Ninsi, a quem o Senhor tinha ungido para desarraigar a casa de Acabe.
8 Ao executar Jeú juízo contra a casa de Acabe, achou os príncipes de Judá e os filhos dos irmãos de Acazias, que o serviam, e os matou.
9 Depois, mandou procurar a Acazias, e, achando-o em Samaria, onde se havia escondido, o trouxeram a Jeú e o mataram; seus próprios servos o sepultaram, porque diziam: É filho de Josafá, que buscou ao Senhor de todo o coração. E ninguém houve na casa de Acazias que pudesse reinar.
10 Vendo Atalia, mãe de Acazias, que seu filho era morto, levantou-se e destruiu toda a descendência real da casa de Judá.
11 Mas Jeosabeate, filha do rei, tomou a Joás, filho de Acazias, e o furtou dentre os filhos do rei, aos quais matavam, e o pôs e à sua ama numa câmara interior; assim, Jeosabeate, a filha do rei Jeorão, mulher do sacerdote Joiada e irmã de Acazias, o escondeu de Atalia, e não foi morto.
12 Joás esteve com eles seis anos na Casa de Deus, e Atalia reinou no país.*
1 No sétimo ano, Joiada se animou e entrou em aliança com os capitães de cem: Azarias, filho de Jeroão, Ismael, filho de Joanã, Azarias, filho de Obede, Maaseias, filho de Adaías, e Elisafate, filho de Zicri.
2 Estes percorreram Judá, e congregaram os levitas de todas as cidades de Judá e os cabeças das famílias de Israel, e vieram para Jerusalém.
3 Toda essa congregação fez aliança com o rei na Casa de Deus; e Joiada lhes disse: Eis que reinará o filho do rei, como falou o Senhor a respeito dos filhos de Davi.
4 Esta é a obra que haveis de fazer: uma terça parte de vós, sacerdotes e levitas, que entrais no sábado, servirá de guardas da porta;
5 outra terça parte estará na casa do rei; e a outra terça parte, à Porta do Fundamento; e todo o povo estará nos pátios da Casa do Senhor.
6 Porém ninguém entre na Casa do Senhor, senão os sacerdotes e os levitas que ministram; estes entrarão, porque são santos; mas todo o povo guardará o preceito do Senhor.
7 Os levitas rodearão o rei, cada um de armas na mão, e qualquer que entrar na casa, seja morto; estareis com o rei quando entrar e quando sair.
8 Fizeram, pois, os levitas e todo o Judá segundo tudo quanto lhes ordenara o sacerdote Joiada; tomou cada um os seus homens, tanto os que entravam como os que saíam no sábado; porquanto o sacerdote Joiada não despediu os turnos.
9 O sacerdote Joiada entregou aos capitães de cem as lanças, os paveses e os escudos que haviam sido do rei Davi e estavam na Casa de Deus.
10 Dispôs todo o povo, cada um de armas na mão, desde o lado direito da casa real até ao seu lado esquerdo, e até ao altar, e até ao templo, para rodear o rei.
11 Então, trouxeram para fora o filho do rei, puseram-lhe a coroa, entregaram-lhe o Livro do Testemunho e o constituíram rei; Joiada e seus filhos o ungiram e gritaram: Viva o rei!
12 Ouvindo Atalia o clamor do povo que corria e louvava o rei, veio para onde este se achava na Casa do Senhor;
13 olhou, e eis que o rei estava junto à coluna, à entrada, e os capitães e os que tocavam trombetas, junto ao rei; e todo o povo da terra se alegrava, e se tocavam trombetas. Também os cantores com os instrumentos músicos dirigiam o canto de louvores. Então, Atalia rasgou os seus vestidos e clamou: Traição! Traição!
14 Porém o sacerdote Joiada trouxe para fora os capitães que comandavam as tropas e disse-lhes: Fazei-a sair por entre as fileiras; se alguém a seguir, matai-o à espada. Porque o sacerdote tinha dito: Não a matem na Casa do Senhor.
15 Lançaram mão dela; e ela, pelo caminho da entrada dos cavalos, foi à casa do rei, onde a mataram.
16 Joiada fez aliança entre si mesmo, o povo e o rei, para serem eles o povo do Senhor.
17 Então, todo o povo se dirigiu para a casa de Baal e a derribaram; despedaçaram os seus altares e as suas imagens e a Matã, sacerdote de Baal, mataram perante os altares.
18 Entregou Joiada a superintendência da Casa do Senhor nas mãos dos sacerdotes levitas, a quem Davi designara para o encargo da Casa do Senhor, para oferecerem os holocaustos do Senhor, como está escrito na Lei de Moisés, com alegria e com canto, segundo a instituição de Davi.
19 Colocou porteiros às portas da Casa do Senhor, para que nela não entrasse ninguém que de qualquer forma fosse imundo.
20 Tomou os capitães de cem, os nobres, os governadores do povo e todo o povo da terra, e todos estes conduziram, da Casa do Senhor, o rei; passaram, pela porta superior, para a casa do rei e assentaram o rei no trono do reino.
21 Alegrou-se todo o povo da terra, e a cidade ficou tranquila, pois haviam matado Atalia à espada.*
1 Tinha Joás sete anos de idade quando começou a reinar e quarenta anos reinou em Jerusalém.
2 Era o nome de sua mãe Zíbia, de Berseba. Fez Joás o que era reto perante o Senhor todos os dias do sacerdote Joiada.
3 Tomou-lhe Joiada duas mulheres; e gerou filhos e filhas.
4 Depois disto, resolveu Joás restaurar a Casa do Senhor.
5 Reuniu os sacerdotes e os levitas e lhes disse: Saí pelas cidades de Judá e levantai dinheiro de todo o Israel para reparardes a casa do vosso Deus, de ano em ano; e, vós, apressai-vos nisto. Porém os levitas não se apressaram.
6 Mandou o rei chamar a Joiada, o chefe, e lhe perguntou: Por que não requereste dos levitas que trouxessem de Judá e de Jerusalém o imposto que Moisés, servo do Senhor, pôs sobre a congregação de Israel, para a tenda do Testemunho?
7 Porque a perversa Atalia e seus filhos arruinaram a Casa de Deus; e usaram todas as coisas sagradas da Casa do Senhor no serviço dos baalins.
8 Deu o rei ordem e fizeram um cofre e o puseram do lado de fora, à porta da Casa do Senhor.
9 Publicou-se, em Judá e em Jerusalém, que trouxessem ao Senhor o imposto que Moisés, servo de Deus, havia posto sobre Israel, no deserto.
10 Então, todos os príncipes e todo o povo se alegraram, e trouxeram o imposto, e o lançaram no cofre, até acabar a obra.
11 Quando o cofre era levado por intermédio dos levitas a uma comissão real, vendo-se que havia muito dinheiro, vinha o escrivão do rei e o comissário do sumo sacerdote, esvaziavam-no, tomavam-no e o levavam de novo ao seu lugar; assim faziam dia após dia e ajuntaram dinheiro em abundância,
12 o qual o rei e Joiada davam aos que dirigiam a obra e tinham a seu cargo a Casa do Senhor; contrataram pedreiros e carpinteiros, para restaurarem a Casa do Senhor, como também os que trabalhavam em ferro e em bronze, para repararem a Casa do Senhor.
13 Os que tinham o encargo da obra trabalhavam, e a reparação tinha bom êxito com eles; restauraram a Casa de Deus no seu próprio estado e a consolidaram.
14 Tendo eles acabado a obra, trouxeram ao rei e a Joiada o resto do dinheiro, de que se fizeram utensílios para a Casa do Senhor, objetos para o ministério e para os holocaustos, taças e outros objetos de ouro e de prata. E continuamente ofereceram holocaustos na Casa do Senhor, todos os dias de Joiada.
15 Envelheceu Joiada e morreu farto de dias; era da idade de cento e trinta anos quando morreu.
16 Sepultaram-no na Cidade de Davi com os reis; porque tinha feito bem em Israel e para com Deus e a sua casa.
17 Depois da morte de Joiada, vieram os príncipes de Judá e se prostraram perante o rei, e o rei os ouviu.
18 Deixaram a Casa do Senhor, Deus de seus pais, e serviram aos postes-ídolos e aos ídolos; e, por esta sua culpa, veio grande ira sobre Judá e Jerusalém.
19 Porém o Senhor lhes enviou profetas para os reconduzir a si; estes profetas testemunharam contra eles, mas eles não deram ouvidos.
20 O Espírito de Deus se apoderou de Zacarias, filho do sacerdote Joiada, o qual se pôs em pé diante do povo e lhes disse: Assim diz Deus: Por que transgredis os mandamentos do Senhor, de modo que não prosperais? Porque deixastes o Senhor, também ele vos deixará.
21 Conspiraram contra ele e o apedrejaram, por mandado do rei, no pátio da Casa do Senhor.
22 Assim, o rei Joás não se lembrou da beneficência que Joiada, pai de Zacarias, lhe fizera, porém matou-lhe o filho; este, ao expirar, disse: O Senhor o verá e o retribuirá.
23 Antes de se findar o ano, subiu contra Joás o exército dos siros; e, vindo a Judá e a Jerusalém, destruíram, dentre o povo, a todos os seus príncipes, cujo despojo remeteram ao rei de Damasco.
24 Ainda que o exército dos siros viera com poucos homens, contudo, o Senhor lhes permitiu vencer um exército mui numeroso dos judeus, porque estes deixaram o Senhor, Deus de seus pais. Assim, executaram os siros os juízos de Deus contra Joás.
25 Quando os siros se retiraram dele, deixando-o gravemente enfermo, conspiraram contra ele os seus servos, por causa do sangue dos filhos do sacerdote Joiada, e o feriram no seu leito, e morreu.
26 Sepultaram-no na Cidade de Davi, porém não nos sepulcros dos reis. Foram estes os que conspiraram contra ele: Zabade, filho de Simeate, a amonita, e Jeozabade, filho de Sinrite, a moabita.
27 Quanto a seus filhos, e às numerosas sentenças proferidas contra ele, e à restauração da Casa de Deus, eis que estão escritos no Livro da História dos Reis. Em seu lugar, reinou Amazias, seu filho.*
1 Era Amazias da idade de vinte e cinco anos quando começou a reinar e reinou vinte e nove anos em Jerusalém; sua mãe se chamava Jeoadã, de Jerusalém.
2 Fez ele o que era reto perante o Senhor; não, porém, com inteireza de coração.
3 Uma vez confirmado o reino nas suas mãos, matou os seus servos que tinham assassinado o rei, seu pai.
4 Porém os filhos deles não matou, mas fez segundo está escrito na Lei, no Livro de Moisés, no qual o Senhor deu ordem, dizendo: Os pais não serão mortos por causa dos filhos, nem os filhos, por causa dos pais; cada qual será morto pelo seu próprio pecado.
5 Amazias congregou a Judá e o pôs, segundo as suas famílias, sob chefes de mil e chefes de cem, por todo o Judá e Benjamim; contou-os de vinte anos para cima e achou trezentos mil escolhidos capazes de sair à guerra e manejar lança e escudo.
6 Também tomou de Israel a soldo cem mil homens valentes por cem talentos de prata.
7 Porém certo homem de Deus veio a ele, dizendo: Ó rei, não deixes ir contigo o exército de Israel; porque o Senhor não é com Israel, isto é, com os filhos de Efraim.
8 Porém vai só, age e sê forte; do contrário, Deus te faria cair diante do inimigo, porque Deus tem força para ajudar e para fazer cair.
9 Disse Amazias ao homem de Deus: Que se fará, pois, dos cem talentos de prata que dei às tropas de Israel? Respondeu-lhe o homem de Deus: Muito mais do que isso pode dar-te o Senhor.
10 Então, separou Amazias as tropas que lhe tinham vindo de Efraim para que voltassem para casa; pelo que muito se acendeu a ira deles contra Judá, e voltaram para casa ardendo em ira.
11 Animou-se Amazias e, conduzindo o seu povo, foi-se ao vale do Sal, onde feriu dez mil dos filhos de Seir.
12 Também os filhos de Judá prenderam vivos dez mil e os trouxeram ao cimo de um penhasco, de onde os precipitaram, de modo que todos foram esmigalhados.
13 Porém os homens das tropas que Amazias despedira, para que não fossem com ele à peleja, deram sobre as cidades de Judá, desde Samaria até Bete-Horom; feriram deles três mil e fizeram grande despojo.
14 Vindo Amazias da matança dos edomitas, trouxe consigo os deuses dos filhos de Seir, tomou-os por seus deuses, adorou-os e lhes queimou incenso.
15 Então, a ira do Senhor se acendeu contra Amazias, e mandou-lhe um profeta que lhe disse: Por que buscaste deuses que a seu povo não livraram das tuas mãos?
16 Enquanto lhe falava o profeta, disse-lhe o rei: Acaso, te pusemos por conselheiro do rei? Para com isso. Por que teríamos de ferir-te? Então, parou o profeta, mas disse: Sei que Deus resolveu destruir-te, porque fizeste isso e não deste ouvidos ao meu conselho.
17 Então, Amazias, rei de Judá, tomou conselho e enviou mensageiros a Jeoás, filho de Jeoacaz, filho de Jeú, rei de Israel, dizendo: Vem, meçamos armas.
18 Porém Jeoás, rei de Israel, respondeu a Amazias, rei de Judá: O cardo que está no Líbano mandou dizer ao cedro que lá está: Dá tua filha por mulher a meu filho; mas os animais do campo, que estavam no Líbano, passaram e pisaram o cardo.
19 Tu dizes: Eis que feri os edomitas; e o teu coração se ensoberbeceu para te gloriares; agora, fica em casa; por que provocarias o mal para caíres tu, e Judá, contigo?
20 Mas Amazias não quis atendê-lo; porque isto vinha de Deus, para entregá-los nas mãos dos seus inimigos, porquanto buscaram os deuses dos edomitas.
21 Subiu, então, Jeoás, rei de Israel, e Amazias, rei de Judá, e mediram armas em Bete-Semes, que pertence a Judá.
22 Judá foi derrotado por Israel, e fugiu cada um para sua casa.
23 E Jeoás, rei de Israel, prendeu a Amazias, rei de Judá, filho de Joás, filho de Jeoacaz, em Bete-Semes; levou-o a Jerusalém, cujo muro ele rompeu desde a Porta de Efraim até à Porta da Esquina, quatrocentos côvados.
24 Tomou todo o ouro e a prata, e todos os utensílios que se acharam na Casa de Deus, com Obede-Edom, e os tesouros da casa do rei, como também reféns; e voltou para Samaria.
25 Amazias, filho de Joás, rei de Judá, viveu quinze anos depois da morte de Jeoás, filho de Jeoacaz, rei de Israel.
26 Ora, os mais atos de Amazias, tanto os primeiros como os últimos, porventura, não estão escritos no Livro da História dos Reis de Judá e de Israel?
27 Depois que Amazias deixou de seguir ao Senhor, conspiraram contra ele em Jerusalém, e ele fugiu para Laquis; porém enviaram após ele homens até Laquis e o mataram ali.
28 Trouxeram-no sobre cavalos e o sepultaram junto a seus pais na Cidade de Davi.*
1 Todo o povo de Judá tomou a Uzias, que era de dezesseis anos, e o constituiu rei em lugar de Amazias, seu pai.
2 Ele edificou a Elate e a restituiu a Judá, depois que o rei descansou com seus pais.
3 Uzias tinha dezesseis anos quando começou a reinar e cinquenta e dois anos reinou em Jerusalém. Era o nome de sua mãe Jecolias, de Jerusalém.
4 Ele fez o que era reto perante o Senhor, segundo tudo o que fizera Amazias, seu pai.
5 Propôs-se buscar a Deus nos dias de Zacarias, que era sábio nas visões de Deus; nos dias em que buscou ao Senhor, Deus o fez prosperar.
6 Saiu e guerreou contra os filisteus e quebrou o muro de Gate, o de Jabné e o de Asdode; e edificou cidades no território de Asdode e entre os filisteus.
7 Deus o ajudou contra os filisteus, e contra os arábios que habitavam em Gur-Baal, e contra os meunitas.
8 Os amonitas deram presentes a Uzias, cujo renome se espalhara até à entrada do Egito, porque se tinha tornado em extremo forte.
9 Também edificou Uzias torres em Jerusalém, à Porta da Esquina, à Porta do Vale e à Porta do Ângulo e as fortificou.
10 Também edificou torres no deserto e cavou muitas cisternas, porque tinha muito gado, tanto nos vales como nas campinas; tinha lavradores e vinhateiros, nos montes e nos campos férteis, porque era amigo da agricultura.
11 Tinha também Uzias um exército de homens destros nas armas, que saíam à guerra em tropas, segundo o rol feito pelo escrivão Jeiel e Maaseias, oficial, sob a direção de Hananias, um dos príncipes do rei.
12 O número total dos cabeças das famílias, homens valentes, era de dois mil e seiscentos.
13 Debaixo das suas ordens, havia um exército guerreiro de trezentos e sete mil e quinhentos homens, que faziam a guerra com grande poder, para ajudar o rei contra os inimigos.
14 Preparou-lhes Uzias, para todo o exército, escudos, lanças, capacetes, couraças e arcos e até fundas para atirar pedras.
15 Fabricou em Jerusalém máquinas, de invenção de homens peritos, destinadas para as torres e cantos das muralhas, para atirarem flechas e grandes pedras; divulgou-se a sua fama até muito longe, porque foi maravilhosamente ajudado, até que se tornou forte.
16 Mas, havendo-se já fortificado, exaltou-se o seu coração para a sua própria ruína, e cometeu transgressões contra o Senhor, seu Deus, porque entrou no templo do Senhor para queimar incenso no altar do incenso.
17 Porém o sacerdote Azarias entrou após ele, com oitenta sacerdotes do Senhor, homens da maior firmeza;
18 e resistiram ao rei Uzias e lhe disseram: A ti, Uzias, não compete queimar incenso perante o Senhor, mas aos sacerdotes, filhos de Arão, que são consagrados para este mister; sai do santuário, porque transgrediste; nem será isso para honra tua da parte do Senhor Deus.
19 Então, Uzias se indignou; tinha o incensário na mão para queimar incenso; indignando-se ele, pois, contra os sacerdotes, a lepra lhe saiu na testa perante os sacerdotes, na Casa do Senhor, junto ao altar do incenso.
20 Então, o sumo sacerdote Azarias e todos os sacerdotes voltaram-se para ele, e eis que estava leproso na testa, e apressadamente o lançaram fora; até ele mesmo se deu pressa em sair, visto que o Senhor o ferira.
21 Assim, ficou leproso o rei Uzias até ao dia da sua morte; e morou, por ser leproso, numa casa separada, porque foi excluído da Casa do Senhor; e Jotão, seu filho, tinha a seu cargo a casa do rei, julgando o povo da terra.
22 Quanto aos mais atos de Uzias, tanto os primeiros como os últimos, o profeta Isaías, filho de Amoz, os escreveu.
23 Descansou Uzias com seus pais, e, com seus pais, o sepultaram no campo do sepulcro que era dos reis; porque disseram: Ele é leproso. E Jotão, seu filho, reinou em seu lugar.*
1 Tinha Jotão vinte e cinco anos de idade quando começou a reinar e dezesseis anos reinou em Jerusalém. Era o nome de sua mãe Jerusa, filha de Zadoque.
2 Fez o que era reto perante o Senhor, segundo tudo o que fizera Uzias, seu pai, exceto que não entrou no templo do Senhor. E o povo continuava na prática do mal.
3 Ele edificou a porta de cima da Casa do Senhor e também edificou muitas obras sobre o Muro de Ofel.
4 Também edificou cidades na região montanhosa de Judá e nos bosques, castelos e torres.
5 Ele também guerreou contra o rei dos filhos de Amom e prevaleceu sobre eles, de modo que os filhos de Amom, naquele ano, lhe deram cem talentos de prata, dez mil coros de trigo e dez mil de cevada; isto lhe trouxeram os filhos de Amom também no segundo e no terceiro ano.
6 Assim, Jotão se foi tornando mais poderoso, porque dirigia os seus caminhos segundo a vontade do Senhor, seu Deus.
7 Quanto aos mais atos de Jotão, todas as suas guerras e empreendimentos, eis que tudo está escrito no Livro da História dos Reis de Israel e de Judá.
8 Tinha vinte e cinco anos de idade quando começou a reinar e reinou dezesseis anos em Jerusalém.
9 Descansou Jotão com seus pais, e o sepultaram na Cidade de Davi; e Acaz, seu filho, reinou em seu lugar.*
1 Tinha Acaz vinte anos de idade quando começou a reinar e reinou dezesseis anos em Jerusalém; e não fez o que era reto perante o Senhor, como Davi, seu pai.
2 Andou nos caminhos dos reis de Israel e até fez imagens fundidas a baalins.
3 Também queimou incenso no vale do filho de Hinom e queimou a seus próprios filhos, segundo as abominações dos gentios que o Senhor lançara de diante dos filhos de Israel.
4 Também sacrificou e queimou incenso nos altos e nos outeiros, como também debaixo de toda árvore frondosa.
5 Pelo que o Senhor, seu Deus, o entregou nas mãos do rei dos siros, os quais o derrotaram e levaram dele em cativeiro uma grande multidão de presos, que trouxeram a Damasco; também foi entregue nas mãos do rei de Israel, o qual lhe infligiu grande derrota.
6 Porque Peca, filho de Remalias, matou em Judá, num só dia, cento e vinte mil, todos homens poderosos, por terem abandonado o Senhor, Deus de seus pais.
7 Zicri, homem valente de Efraim, matou a Maaseias, filho do rei, a Azricão, alto oficial do palácio, e a Elcana, o segundo depois do rei.
8 Os filhos de Israel levaram presos de Judá, seu povo irmão, duzentos mil: mulheres, filhos e filhas; e saquearam deles grande despojo e o trouxeram para Samaria.
9 Mas estava ali um profeta do Senhor, cujo nome era Odede, o qual saiu ao encontro do exército que vinha para Samaria e lhe disse: Eis que, irando-se o Senhor, Deus de vossos pais, contra Judá, os entregou nas vossas mãos, e vós os matastes com tamanha raiva, que chegou até aos céus.
10 Agora, cuidais em sujeitar os filhos de Judá e Jerusalém, para vos serem escravos e escravas; acaso, não sois vós mesmos culpados contra o Senhor, vosso Deus?
11 Agora, pois, atendei-me e fazei voltar os presos que trouxestes cativos de vossos irmãos, porque o brasume da ira do Senhor está sobre vós.
12 Então, se levantaram alguns homens dentre os cabeças dos filhos de Efraim, a saber, Azarias, filho de Joanã, Berequias, filho de Mesilemote, Jeizquias, filho de Salum, e Amasa, filho de Hadlai, contra os que voltavam da batalha
13 e lhes disseram: Não fareis entrar aqui esses cativos, porque intentais acrescentar aos nossos pecados e à nossa culpa diante do Senhor ainda outros; a nossa culpa já é grande, e o brasume da ira do Senhor está sobre nós.
14 Então, os homens armados deixaram os presos e o despojo diante dos príncipes e de toda a congregação.
15 Homens foram designados nominalmente, os quais se levantaram, e tomaram os cativos, e do despojo vestiram a todos os que estavam nus; vestiram-nos, e calçaram-nos, e lhes deram de comer e de beber, e os ungiram; a todos os que, por fracos, não podiam andar, levaram sobre jumentos a Jericó, cidade das Palmeiras, a seus irmãos. Então, voltaram para Samaria.
16 Naquele tempo, mandou o rei Acaz pedir aos reis da Assíria que o ajudassem.
17 Pois vieram, de novo, os edomitas, e derrotaram Judá, e levaram presos em cativeiro.
18 Também os filisteus deram contra as cidades da campina e do sul de Judá, e tomaram Bete-Semes, Aijalom, Gederote, Socó e suas aldeias, Timna e suas aldeias e Ginzo e suas aldeias; e habitavam ali.
19 Porque o Senhor humilhou a Judá por causa de Acaz, rei de Israel; porque este permitira que Judá caísse em dissolução, e ele, de todo, se entregou à transgressão contra o Senhor.
20 Veio a ele Tiglate-Pileser, rei da Assíria; porém o pôs em aperto, em vez de fortalecê-lo.
21 Porque Acaz tomou despojos da Casa do Senhor, da casa do rei e da dos príncipes e os deu ao rei da Assíria; porém isso não o ajudou.
22 No tempo da sua angústia, cometeu ainda maiores transgressões contra o Senhor; ele mesmo, o rei Acaz.
23 Pois ofereceu sacrifícios aos deuses de Damasco, que o feriram, e disse: Visto que os deuses dos reis da Síria os ajudam, eu lhes oferecerei sacrifícios para que me ajudem a mim. Porém eles foram a sua ruína e a de todo o Israel.
24 Ajuntou Acaz os utensílios da Casa de Deus, fê-los em pedaços e fechou as portas da Casa do Senhor; e fez para si altares em todos os cantos de Jerusalém.
25 Também, em cada cidade de Judá, fez altos para queimar incenso a outros deuses; assim, provocou à ira o Senhor, Deus de seus pais.
26 Quanto aos mais atos dele e a todos os seus caminhos, tanto os primeiros como os últimos, eis que estão escritos no Livro da História dos Reis de Judá e de Israel.
27 Descansou Acaz com seus pais, e o sepultaram na cidade, em Jerusalém, porém não o puseram nos sepulcros dos reis de Israel; e Ezequias, seu filho, reinou em seu lugar.*
1 Tinha Ezequias vinte e cinco anos de idade quando começou a reinar e reinou vinte e nove anos em Jerusalém. Sua mãe se chamava Abia e era filha de Zacarias.
2 Fez ele o que era reto perante o Senhor, segundo tudo quanto fizera Davi, seu pai.
3 No primeiro ano do seu reinado, no primeiro mês, abriu as portas da Casa do Senhor e as reparou.
4 Trouxe os sacerdotes e os levitas, ajuntou-os na praça oriental
5 e lhes disse: Ouvi-me, ó levitas! Santificai-vos, agora, e santificai a Casa do Senhor, Deus de vossos pais; tirai do santuário a imundícia.
6 Porque nossos pais prevaricaram e fizeram o que era mau perante o Senhor, nosso Deus, e o deixaram; desviaram o seu rosto do tabernáculo do Senhor e lhe voltaram as costas.
7 Também fecharam as portas do pórtico, apagaram as lâmpadas, não queimaram incenso, nem ofereceram holocaustos nos santuários ao Deus de Israel.
8 Pelo que veio grande ira do Senhor sobre Judá e Jerusalém, e os entregou ao terror, ao espanto e aos assobios, como vós o estais vendo com os próprios olhos.
9 Porque eis que nossos pais caíram à espada, e, por isso, nossos filhos, nossas filhas e nossas mulheres estiveram em cativeiro.
10 Agora, estou resolvido a fazer aliança com o Senhor, Deus de Israel, para que se desvie de nós o ardor da sua ira.
11 Filhos meus, não sejais negligentes, pois o Senhor vos escolheu para estardes diante dele para o servirdes, para serdes seus ministros e queimardes incenso.
12 Então, se levantaram os levitas: Maate, filho de Amasai, e Joel, filho de Azarias, dos filhos dos coatitas; dos filhos de Merari, Quis, filho de Abdi, e Azarias, filho de Jealelel; dos gersonitas, Joá, filho de Zima, e Éden, filho de Joá;
13 dos filhos de Elisafã, Sinri e Jeuel; dos filhos de Asafe, Zacarias e Matanias;
14 dos filhos de Hemã, Jeuel e Simei; dos filhos de Jedutum, Semaías e Uziel.
15 Congregaram a seus irmãos, santificaram-se e vieram segundo a ordem do rei pelas palavras do Senhor, para purificarem a Casa do Senhor.
16 Os sacerdotes entraram na Casa do Senhor, para a purificar, e tiraram para fora, ao pátio da Casa do Senhor, toda imundícia que acharam no templo do Senhor; e os levitas a tomaram, para a levarem fora, ao ribeiro de Cedrom.
17 Começaram, pois, a santificar no primeiro dia do primeiro mês; ao oitavo dia do mês, vieram ao pórtico do Senhor e santificaram a Casa do Senhor em oito dias; no décimo sexto dia do mês, acabaram.
18 Então, foram ter com o rei Ezequias no palácio e disseram: Já purificamos toda a Casa do Senhor, como também o altar do holocausto com todos os seus utensílios e a mesa da proposição com todos os seus objetos.
19 Também todos os objetos que o rei Acaz, no seu reinado, lançou fora, na sua transgressão, já preparamos e santificamos; e eis que estão diante do altar do Senhor.
20 Então, o rei Ezequias se levantou de madrugada, reuniu os príncipes da cidade e subiu à Casa do Senhor.
21 Mandou trazer sete novilhos, sete carneiros, sete cordeiros e sete bodes, como oferta pelo pecado a favor do reino, do santuário e de Judá; e aos filhos de Arão, os sacerdotes, que os oferecessem sobre o altar do Senhor.
22 Mortos os novilhos, os sacerdotes tomaram o sangue e o aspergiram sobre o altar; mataram os carneiros e aspergiram o sangue sobre o altar; também mataram os cordeiros e aspergiram o sangue sobre o altar.
23 Para oferta pelo pecado, trouxeram os bodes perante o rei e a congregação e puseram as mãos sobre eles.
24 Os sacerdotes os mataram e, com o sangue, fizeram uma oferta pelo pecado, ao pé do altar, para expiação de todo o Israel, porque o rei tinha ordenado que se fizesse aquele holocausto e oferta pelo pecado, por todo o Israel.
25 Também estabeleceu os levitas na Casa do Senhor com címbalos, alaúdes e harpas, segundo mandado de Davi e de Gade, o vidente do rei, e do profeta Natã; porque este mandado veio do Senhor, por intermédio de seus profetas.
26 Estavam, pois, os levitas em pé com os instrumentos de Davi, e os sacerdotes, com as trombetas.
27 Deu ordem Ezequias que oferecessem o holocausto sobre o altar. Em começando o holocausto, começou também o cântico ao Senhor com as trombetas, ao som dos instrumentos de Davi, rei de Israel.
28 Toda a congregação se prostrou, quando se entoava o cântico, e as trombetas soavam; tudo isto até findar-se o holocausto.
29 Tendo eles acabado de oferecer o sacrifício, o rei e todos os que se achavam com ele prostraram-se e adoraram.
30 Então, o rei Ezequias e os príncipes ordenaram aos levitas que louvassem o Senhor com as palavras de Davi e de Asafe, o vidente. Eles o fizeram com alegria, e se inclinaram, e adoraram.
31 Disse ainda Ezequias: Agora, vos consagrastes a vós mesmos ao Senhor; chegai-vos e trazei sacrifícios e ofertas de ações de graças à Casa do Senhor. A congregação trouxe sacrifícios e ofertas de ações de graças, e todos os que estavam de coração disposto trouxeram holocaustos.
32 O número dos holocaustos, que a congregação trouxe, foi de setenta bois, cem carneiros e duzentos cordeiros; tudo isto em holocausto para o Senhor.
33 Também foram consagrados seiscentos bois e três mil ovelhas.
34 Os sacerdotes, porém, eram mui poucos e não podiam esfolar a todos os holocaustos; pelo que seus irmãos, os levitas, os ajudaram, até findar-se a obra e até que os outros sacerdotes se santificaram; porque os levitas foram mais retos de coração, para se santificarem, do que os sacerdotes.
35 Além dos holocaustos em abundância, houve também a gordura das ofertas pacíficas e as libações para os holocaustos. Assim, se estabeleceu o ministério da Casa do Senhor.
36 Ezequias e todo o povo se alegraram por causa daquilo que Deus fizera para o povo, porque, subitamente, se fez esta obra.*
1 Depois disto, Ezequias enviou mensageiros por todo o Israel e Judá; escreveu também cartas a Efraim e a Manassés para que viessem à Casa do Senhor, em Jerusalém, para celebrarem a Páscoa ao Senhor, Deus de Israel.
2 Porque o rei tivera conselho com os seus príncipes e com toda a congregação em Jerusalém, para celebrarem a Páscoa no segundo mês
3 (Porquanto não a puderam celebrar no devido tempo, porque não se tinham santificado sacerdotes em número suficiente, e o povo não se ajuntara ainda em Jerusalém.).
4 Foi isto aprovado pelo rei e toda a congregação;
5 e resolveram que se fizesse pregão por todo o Israel, desde Berseba até Dã, para que viessem a celebrar a Páscoa ao Senhor, Deus de Israel, em Jerusalém; porque não a celebravam já com grande número de assistentes, como prescrito.
6 Partiram os correios com as cartas do rei e dos seus príncipes, por todo o Israel e Judá, segundo o mandado do rei, dizendo: Filhos de Israel, voltai-vos ao Senhor, Deus de Abraão, de Isaque e de Israel, para que ele se volte para o restante que escapou do poder dos reis da Assíria.
7 Não sejais como vossos pais e como vossos irmãos, que prevaricaram contra o Senhor, Deus de seus pais, pelo que os entregou à desolação, como estais vendo.
8 Não endureçais, agora, a vossa cerviz, como vossos pais; confiai-vos ao Senhor, e vinde ao seu santuário que ele santificou para sempre, e servi ao Senhor, vosso Deus, para que o ardor da sua ira se desvie de vós.
9 Porque, se vós vos converterdes ao Senhor, vossos irmãos e vossos filhos acharão misericórdia perante os que os levaram cativos e tornarão a esta terra; porque o Senhor, vosso Deus, é misericordioso e compassivo e não desviará de vós o rosto, se vos converterdes a ele.
10 Os correios foram passando de cidade em cidade, pela terra de Efraim e Manassés até Zebulom; porém riram-se e zombaram deles.
11 Todavia, alguns de Aser, de Manassés e de Zebulom se humilharam e foram a Jerusalém.
12 Também em Judá se fez sentir a mão de Deus, dando-lhes um só coração, para cumprirem o mandado do rei e dos príncipes, segundo a palavra do Senhor.
13 Ajuntou-se em Jerusalém muito povo, para celebrar a Festa dos Pães Asmos, no segundo mês, mui grande congregação.
14 Dispuseram-se e tiraram os altares que havia em Jerusalém; também tiraram todos os altares do incenso e os lançaram no vale de Cedrom.
15 Então, imolaram o cordeiro da Páscoa no décimo quarto dia do segundo mês; os sacerdotes e os levitas se envergonharam, e se santificaram, e trouxeram holocaustos à Casa do Senhor.
16 Tomaram os seus devidos lugares, segundo a Lei de Moisés, o homem de Deus; e os sacerdotes aspergiam o sangue, tomando-o das mãos dos levitas.
17 Porque havia muitos na congregação que não se tinham santificado; pelo que os levitas estavam encarregados de imolar os cordeiros da Páscoa por todo aquele que não estava limpo, para o santificarem ao Senhor.
18 Porque uma multidão do povo, muitos de Efraim, de Manassés, de Issacar e de Zebulom não se tinham purificado e, contudo, comeram a Páscoa, não como está escrito; porém Ezequias orou por eles, dizendo: O Senhor, que é bom, perdoe a todo aquele
19 que dispôs o coração para buscar o Senhor Deus, o Deus de seus pais, ainda que não segundo a purificação exigida pelo santuário.
20 Ouviu o Senhor a Ezequias e sarou a alma do povo.
21 Os filhos de Israel que se acharam em Jerusalém celebraram a Festa dos Pães Asmos por sete dias, com grande júbilo; e os levitas e os sacerdotes louvaram ao Senhor de dia em dia, com instrumentos que tocaram fortemente em honra ao Senhor.
22 Ezequias falou ao coração de todos os levitas que revelavam bom entendimento no serviço do Senhor; e comeram, por sete dias, as ofertas da festa, trouxeram ofertas pacíficas e renderam graças ao Senhor, Deus de seus pais.
23 Concordou toda a congregação em celebrar outros sete dias, e, de fato, o fizeram com júbilo;
24 pois Ezequias, rei de Judá, apresentou à congregação mil novilhos e sete mil ovelhas para sacrifício; e os príncipes apresentaram à congregação mil novilhos e dez mil ovelhas; e os sacerdotes se santificaram em grande número.
25 Alegraram-se toda a congregação de Judá, os sacerdotes, os levitas e toda a congregação de todos os que vieram de Israel, como também os estrangeiros que vieram da terra de Israel e os que habitavam em Judá.
26 Houve grande alegria em Jerusalém; porque desde os dias de Salomão, filho de Davi, rei de Israel, não houve coisa semelhante em Jerusalém.
27 Então, os sacerdotes e os levitas se levantaram para abençoar o povo; a sua voz foi ouvida, e a sua oração chegou até à santa habitação de Deus, até aos céus.*
1 Acabando tudo isto, todos os israelitas que se achavam ali saíram às cidades de Judá, quebraram as estátuas, cortaram os postes-ídolos e derribaram os altos e altares por todo o Judá e Benjamim, como também em Efraim e Manassés, até que tudo destruíram; então, tornaram todos os filhos de Israel, cada um para sua possessão, para as cidades deles.
2 Estabeleceu Ezequias os turnos dos sacerdotes e dos levitas, turno após turno, segundo o seu mister: os sacerdotes e levitas, para o holocausto e para as ofertas pacíficas, para ministrarem e cantarem, portas a dentro, nos arraiais do Senhor.
3 A contribuição que fazia o rei da sua própria fazenda era destinada para os holocaustos, para os da manhã e os da tarde e para os holocaustos dos sábados, das Festas da Lua Nova e das festas fixas, como está escrito na Lei do Senhor.
4 Além disso, ordenou ao povo, moradores de Jerusalém, que contribuísse com sua parte devida aos sacerdotes e aos levitas, para que pudessem dedicar-se à Lei do Senhor.
5 Logo que se divulgou esta ordem, os filhos de Israel trouxeram em abundância as primícias do cereal, do vinho, do azeite, do mel e de todo produto do campo; também os dízimos de tudo trouxeram em abundância.
6 Os filhos de Israel e de Judá que habitavam nas cidades de Judá também trouxeram dízimos das vacas e das ovelhas e dízimos das coisas que foram consagradas ao Senhor, seu Deus; e fizeram montões e montões.
7 No terceiro mês, começaram a fazer os primeiros montões; e, no sétimo mês, acabaram.
8 Vindo, pois, Ezequias e os príncipes e vendo aqueles montões, bendisseram ao Senhor e ao seu povo de Israel.
9 Perguntou Ezequias aos sacerdotes e aos levitas acerca daqueles montões.
10 Então, o sumo sacerdote Azarias, da casa de Zadoque, lhe respondeu: Desde que se começou a trazer à Casa do Senhor estas ofertas, temos comido e nos temos fartado delas, e ainda há sobra em abundância; porque o Senhor abençoou ao seu povo, e esta grande quantidade é o que sobra.
11 Então, ordenou Ezequias que se preparassem depósitos na Casa do Senhor.
12 Uma vez preparados, recolheram neles fielmente as ofertas, os dízimos e as coisas consagradas; disto era intendente Conanias, o levita, e Simei, seu irmão, era o segundo.
13 Jeiel, Azarias, Naate, Asael, Jerimote, Jozabade, Eliel, Ismaquias, Maate e Benaia eram superintendentes sob a direção de Conanias e Simei, seu irmão, nomeados pelo rei Ezequias e por Azarias, chefe da Casa de Deus.
14 O levita Coré, filho de Imna e guarda da porta oriental, estava encarregado das ofertas voluntárias que se faziam a Deus, para distribuir as ofertas do Senhor e as coisas santíssimas.
15 Debaixo das suas ordens estavam Éden, Miniamim, Jesua, Semaías, Amarias e Secanias, nas cidades dos sacerdotes, para com fidelidade distribuírem as porções a seus irmãos, segundo os seus turnos, tanto aos pequenos como aos grandes;
16 exceto aos que estavam registrados nas genealogias dos homens, de três anos para cima, e que entravam na Casa do Senhor, para a obra de cada dia pelo seu ministério nos seus cargos, segundo os seus turnos.
17 Quanto ao registro dos sacerdotes, foi ele feito segundo as suas famílias, e o dos levitas de vinte anos para cima foi feito segundo os seus cargos nos seus turnos.
18 Deles, foram registrados as crianças, as mulheres, os filhos e as filhas, uma grande multidão, porque com fidelidade se houveram santamente com as coisas sagradas.
19 Dentre os sacerdotes, filhos de Arão, que moravam nos campos dos arredores das suas cidades, havia, em cada cidade, homens que foram designados nominalmente para distribuírem as porções a todo homem entre os sacerdotes e a todos os levitas que foram registrados.
20 Assim fez Ezequias em todo o Judá; fez o que era bom, reto e verdadeiro perante o Senhor, seu Deus.
21 Em toda a obra que começou no serviço da Casa de Deus, na lei e nos mandamentos, para buscar a seu Deus, de todo o coração o fez e prosperou.*
1 Depois destas coisas e desta fidelidade, veio Senaqueribe, rei da Assíria, entrou em Judá, acampou-se contra as cidades fortificadas e intentou apoderar-se delas.
2 Vendo, pois, Ezequias que Senaqueribe vinha e que estava resolvido a pelejar contra Jerusalém,
3 resolveu, de acordo com os seus príncipes e os seus homens valentes, tapar as fontes das águas que havia fora da cidade; e eles o ajudaram.
4 Assim, muito povo se ajuntou, e taparam todas as fontes, como também o ribeiro que corria pelo meio da terra, pois diziam: Por que viriam os reis da Assíria e achariam tantas águas?
5 Ele cobrou ânimo, restaurou todo o muro quebrado e sobre ele ergueu torres; levantou também o outro muro por fora, fortificou a Milo na Cidade de Davi e fez armas e escudos em abundância.
6 Pôs oficiais de guerra sobre o povo, reuniu-os na praça da porta da cidade e lhes falou ao coração, dizendo:
7 Sede fortes e corajosos, não temais, nem vos assusteis por causa do rei da Assíria, nem por causa de toda a multidão que está com ele; porque um há conosco maior do que o que está com ele.
8 Com ele está o braço de carne, mas conosco, o Senhor, nosso Deus, para nos ajudar e para guerrear nossas guerras. O povo cobrou ânimo com as palavras de Ezequias, rei de Judá.
9 Depois disto, enquanto Senaqueribe, rei da Assíria, com todo o seu exército sitiava Laquis, enviou os seus servos a Ezequias, rei de Judá, que estava em Jerusalém, dizendo:
10 Assim diz Senaqueribe, rei da Assíria: Em que confiais vós, para vos deixardes sitiar em Jerusalém?
11 Acaso, não vos incita Ezequias, para morrerdes à fome e à sede, dizendo: O Senhor, nosso Deus, nos livrará das mãos do rei da Assíria?
12 Não é Ezequias o mesmo que tirou os seus altos e os seus altares e falou a Judá e a Jerusalém, dizendo: Diante de apenas um altar vos prostrareis e sobre ele queimareis incenso?
13 Não sabeis vós o que eu e meus pais fizemos a todos os povos das terras? Acaso, puderam, de qualquer maneira, os deuses das nações daquelas terras livrar o seu país das minhas mãos?
14 Qual é, de todos os deuses daquelas nações que meus pais destruíram, que pôde livrar o seu povo das minhas mãos, para que vosso Deus vos possa livrar das minhas mãos?
15 Agora, pois, não vos engane Ezequias, nem vos incite assim, nem lhe deis crédito; porque nenhum deus de nação alguma, nem de reino algum pôde livrar o seu povo das minhas mãos, nem das mãos de meus pais; quanto menos vos poderá livrar o vosso Deus das minhas mãos?
16 Os seus servos falaram ainda mais contra o Senhor Deus e contra Ezequias, seu servo.
17 Senaqueribe escreveu também cartas, para blasfemar do Senhor, Deus de Israel, e para falar contra ele, dizendo: Assim como os deuses das nações de outras terras não livraram o seu povo das minhas mãos, assim também o Deus de Ezequias não livrará o seu povo das minhas mãos.
18 Clamaram os servos em alta voz em judaico contra o povo de Jerusalém, que estava sobre o muro, para os atemorizar e os perturbar, para tomarem a cidade.
19 Falaram do Deus de Jerusalém, como dos deuses dos povos da terra, obras das mãos dos homens.
20 Porém o rei Ezequias e Isaías, o profeta, filho de Amoz, oraram por causa disso e clamaram ao céu.
21 Então, o Senhor enviou um anjo que destruiu todos os homens valentes, os chefes e os príncipes no arraial do rei da Assíria; e este, com o rosto coberto de vergonha, voltou para a sua terra. Tendo ele entrado na casa de seu deus, os seus próprios filhos ali o mataram à espada.
22 Assim, livrou o Senhor a Ezequias e os moradores de Jerusalém das mãos de Senaqueribe, rei da Assíria, e das mãos de todos os inimigos; e lhes deu paz por todos os lados.
23 Muitos traziam presentes a Jerusalém ao Senhor e coisas preciosíssimas a Ezequias, rei de Judá, de modo que, depois disto, foi enaltecido à vista de todas as nações.
24 Naqueles dias, adoeceu Ezequias mortalmente; então, orou ao Senhor, que lhe falou e lhe deu um sinal.
25 Mas não correspondeu Ezequias aos benefícios que lhe foram feitos; pois o seu coração se exaltou. Pelo que houve ira contra ele e contra Judá e Jerusalém.
26 Ezequias, porém, se humilhou por se ter exaltado o seu coração, ele e os habitantes de Jerusalém; e a ira do Senhor não veio contra eles nos dias de Ezequias.
27 Teve Ezequias riquezas e glória em grande abundância; proveu-se de tesourarias para prata, ouro, pedras preciosas, especiarias, escudos e toda sorte de objetos desejáveis;
28 também proveu-se de armazéns para a colheita do cereal, do vinho e do azeite; e de estrebarias para toda espécie de animais e de redis para os rebanhos.
29 Edificou também cidades e possuiu ovelhas e vacas em abundância; porque Deus lhe tinha dado mui numerosas possessões.
30 Também o mesmo Ezequias tapou o manancial superior das águas de Giom e as canalizou para o ocidente da Cidade de Davi. Ezequias prosperou em toda a sua obra.
31 Contudo, quando os embaixadores dos príncipes da Babilônia lhe foram enviados para se informarem do prodígio que se dera naquela terra, Deus o desamparou, para prová-lo e fazê-lo conhecer tudo o que lhe estava no coração.
32 Quanto aos mais atos de Ezequias e às suas obras de misericórdia, eis que estão escritos na Visão do Profeta Isaías, filho de Amoz, e no Livro da História dos Reis de Judá e de Israel.
33 Descansou Ezequias com seus pais, e o sepultaram na subida para os sepulcros dos filhos de Davi; e todo o Judá e os habitantes de Jerusalém lhe prestaram honras na sua morte; e Manassés, seu filho, reinou em seu lugar.*
1 Tinha Manassés doze anos de idade quando começou a reinar e cinquenta e cinco anos reinou em Jerusalém.
2 Fez o que era mau perante o Senhor, segundo as abominações dos gentios que o Senhor expulsara de suas possessões, de diante dos filhos de Israel.
3 Pois tornou a edificar os altos que Ezequias, seu pai, havia derribado, levantou altares aos baalins, e fez postes-ídolos, e se prostrou diante de todo o exército dos céus, e o serviu.
4 Edificou altares na Casa do Senhor, da qual o Senhor tinha dito: Em Jerusalém, porei o meu nome para sempre.
5 Também edificou altares a todo o exército dos céus nos dois átrios da Casa do Senhor,
6 queimou seus filhos como oferta no vale do filho de Hinom, adivinhava pelas nuvens, era agoureiro, praticava feitiçarias, tratava com necromantes e feiticeiros e prosseguiu em fazer o que era mau perante o Senhor, para o provocar à ira.
7 Também pôs a imagem de escultura do ídolo que tinha feito na Casa de Deus, de que Deus dissera a Davi e a Salomão, seu filho: Nesta casa e em Jerusalém, que escolhi de todas as tribos de Israel, porei o meu nome para sempre
8 e não removerei mais o pé de Israel da terra que destinei a seus pais, contanto que tenham cuidado de fazer tudo o que lhes tenho mandado, toda a lei, os estatutos e os juízos dados por intermédio de Moisés.
9 Manassés fez errar a Judá e os moradores de Jerusalém, de maneira que fizeram pior do que as nações que o Senhor tinha destruído de diante dos filhos de Israel.
10 Falou o Senhor a Manassés e ao seu povo, porém não lhe deram ouvidos.
11 Pelo que o Senhor trouxe sobre eles os príncipes do exército do rei da Assíria, os quais prenderam Manassés com ganchos, amarraram-no com cadeias e o levaram à Babilônia.
12 Ele, angustiado, suplicou deveras ao Senhor, seu Deus, e muito se humilhou perante o Deus de seus pais;
13 fez-lhe oração, e Deus se tornou favorável para com ele, atendeu-lhe a súplica e o fez voltar para Jerusalém, ao seu reino; então, reconheceu Manassés que o Senhor era Deus.
14 Depois disto, edificou o muro de fora da Cidade de Davi, ao ocidente de Giom, no vale, e à entrada da Porta do Peixe, abrangendo Ofel, e o levantou mui alto; também pôs chefes militares em todas as cidades fortificadas de Judá.
15 Tirou da Casa do Senhor os deuses estranhos e o ídolo, como também todos os altares que edificara no monte da Casa do Senhor e em Jerusalém, e os lançou fora da cidade.
16 Restaurou o altar do Senhor, sacrificou sobre ele ofertas pacíficas e de ações de graças e ordenou a Judá que servisse ao Senhor, Deus de Israel.
17 Contudo, o povo ainda sacrificava nos altos, mas somente ao Senhor, seu Deus.
18 Quanto aos mais atos de Manassés, e à sua oração ao seu Deus, e às palavras dos videntes que lhe falaram no nome do Senhor, Deus de Israel, eis que estão escritos na História dos Reis de Israel.
19 A sua oração e como Deus se tornou favorável para com ele, todo o seu pecado, a sua transgressão e os lugares onde edificou altos e colocou postes-ídolos e imagens de escultura, antes que se humilhasse, eis que tudo está na História dos Videntes.
20 Assim, Manassés descansou com seus pais e foi sepultado na sua própria casa; e Amom, seu filho, reinou em seu lugar.
21 Tinha Amom vinte e dois anos de idade quando começou a reinar e reinou dois anos em Jerusalém.
22 Fez o que era mau perante o Senhor, como fizera Manassés, seu pai; porque Amom fez sacrifício a todas as imagens de escultura que Manassés, seu pai, tinha feito e as serviu.
23 Mas não se humilhou perante o Senhor, como Manassés, seu pai, se humilhara; antes, Amom se tornou mais e mais culpável.
24 Conspiraram contra ele os seus servos e o mataram em sua casa.
25 Porém o povo da terra feriu todos os que conspiraram contra o rei Amom e constituiu a Josias, seu filho, rei em seu lugar.*
1 Tinha Josias oito anos de idade quando começou a reinar e reinou trinta e um anos em Jerusalém.
2 Fez o que era reto perante o Senhor, andou em todo o caminho de Davi, seu pai, e não se desviou nem para a direita nem para a esquerda.
3 Porque, no oitavo ano de seu reinado, sendo ainda moço, começou a buscar o Deus de Davi, seu pai; e, no duodécimo ano, começou a purificar a Judá e a Jerusalém dos altos, dos postes-ídolos e das imagens de escultura e de fundição.
4 Na presença dele, derribaram os altares dos baalins; ele despedaçou os altares do incenso que estavam acima deles; os postes-ídolos e as imagens de escultura e de fundição, quebrou-os, reduziu-os a pó e o aspergiu sobre as sepulturas dos que lhes tinham sacrificado.
5 Os ossos dos sacerdotes queimou sobre os seus altares e purificou a Judá e a Jerusalém.
6 O mesmo fez nas cidades de Manassés, de Efraim e de Simeão, até Naftali, por todos os lados no meio das suas ruínas.
7 Tendo derribado os altares, os postes-ídolos e as imagens de escultura, até reduzi-los a pó, e tendo despedaçado todos os altares do incenso em toda a terra de Israel, então, voltou para Jerusalém.
8 No décimo oitavo ano do seu reinado, havendo já purificado a terra e a casa, enviou a Safã, filho de Azalias, a Maaseias, governador da cidade, e a Joá, filho de Joacaz, cronista, para repararem a Casa do Senhor, seu Deus.
9 Foram a Hilquias, sumo sacerdote, e entregaram o dinheiro que se tinha trazido à Casa de Deus e que os levitas, guardas da porta, tinham ajuntado, dinheiro provindo das mãos de Manassés, de Efraim e de todo o resto de Israel, como também de todo o Judá e Benjamim e dos habitantes de Jerusalém.
10 Eles o entregaram aos que dirigiam a obra e tinham a seu cargo a Casa do Senhor, para que pagassem àqueles que faziam a obra, trabalhadores na Casa do Senhor, para repararem e restaurarem a casa.
11 Deram-no aos carpinteiros e aos edificadores, para comprarem pedras lavradas e madeiras para as junturas e para servirem de vigas para as casas que os reis de Judá deixaram cair em ruína.
12 Os homens procederam fielmente na obra; e os superintendentes deles eram Jaate e Obadias, levitas, dos filhos de Merari, como também Zacarias e Mesulão, dos filhos dos coatitas, para superintenderem a obra.
13 Todos os levitas peritos em instrumentos músicos eram superintendentes dos carregadores e dirigiam a todos os que faziam a obra, em qualquer sorte de trabalho. Outros levitas eram escrivães, oficiais e porteiros.
14 Quando se tirava o dinheiro que se havia trazido à Casa do Senhor, Hilquias, o sacerdote, achou o Livro da Lei do Senhor, dada por intermédio de Moisés.
15 Então, disse Hilquias ao escrivão Safã: Achei o Livro da Lei na Casa do Senhor.
16 Hilquias entregou o livro a Safã. Então, Safã levou o livro ao rei e lhe deu relatório, dizendo: Tudo quanto se encomendou a teus servos, eles o fazem.
17 Contaram o dinheiro que se achou na Casa do Senhor e o entregaram nas mãos dos que dirigem a obra e dos que a executam.
18 Relatou mais o escrivão ao rei, dizendo: O sacerdote Hilquias me entregou um livro. Safã leu nele diante do rei.
19 Tendo o rei ouvido as palavras da lei, rasgou as suas vestes.
20 Ordenou o rei a Hilquias, a Aicão, filho de Safã, a Abdom, filho de Mica, a Safã, o escrivão, e a Asaías, servo do rei, dizendo:
21 Ide e consultai o Senhor por mim e pelos restantes em Israel e Judá, acerca das palavras deste livro que se achou; porque grande é o furor do Senhor, que se derramou sobre nós, porquanto nossos pais não guardaram as palavras do Senhor, para fazerem tudo quanto está escrito neste livro.
22 Então, Hilquias e os enviados pelo rei foram ter com a profetisa Hulda, mulher de Salum, o guarda-roupa, filho de Tocate, filho de Harás, e lhe falaram a esse respeito. Ela habitava na Cidade Baixa, em Jerusalém.
23 Ela lhes disse: Assim diz o Senhor, o Deus de Israel: Dizei ao homem que vos enviou a mim:
24 Assim diz o Senhor: Eis que trarei males sobre este lugar e sobre os seus moradores, a saber, todas as maldições escritas no livro que leram diante do rei de Judá.
25 Visto que me deixaram e queimaram incenso a outros deuses, para me provocarem à ira com todas as obras das suas mãos, o meu furor está derramado sobre este lugar e não se apagará.
26 Porém ao rei de Judá, que vos enviou a consultar o Senhor, assim lhe direis: Assim diz o Senhor, o Deus de Israel, acerca das palavras que ouviste:
27 Porquanto o teu coração se enterneceu, e te humilhaste perante Deus, quando ouviste as suas ameaças contra este lugar e contra os seus moradores, e te humilhaste perante mim, e rasgaste as tuas vestes, e choraste perante mim, também eu te ouvi, diz o Senhor.
28 Pelo que eu te reunirei a teus pais, e tu serás recolhido em paz à tua sepultura, e os teus olhos não verão todo o mal que hei de trazer sobre este lugar e sobre os seus moradores. Então, levaram eles ao rei esta resposta.
29 Então, deu ordem o rei, e todos os anciãos de Judá e de Jerusalém se ajuntaram.
30 O rei subiu à Casa do Senhor, e todos os homens de Judá, todos os moradores de Jerusalém, os sacerdotes, os levitas e todo o povo, desde o menor até ao maior; e leu diante deles todas as palavras do Livro da Aliança que fora encontrado na Casa do Senhor.
31 O rei se pôs no seu lugar e fez aliança ante o Senhor, para o seguirem, guardarem os seus mandamentos, os seus testemunhos e os seus estatutos, de todo o coração e de toda a alma, cumprindo as palavras desta aliança, que estavam escritas naquele livro.
32 Todos os que se acharam em Jerusalém e em Benjamim anuíram a esta aliança; e os habitantes de Jerusalém fizeram segundo a aliança de Deus, o Deus de seus pais.
33 Josias tirou todas as abominações de todas as terras que eram dos filhos de Israel; e a todos quantos se acharam em Israel os obrigou a que servissem ao Senhor, seu Deus. Enquanto ele viveu, não se desviaram de seguir o Senhor, Deus de seus pais.*
1 Josias celebrou a Páscoa ao Senhor, em Jerusalém; e mataram o cordeiro da Páscoa no décimo quarto dia do primeiro mês.
2 Estabeleceu os sacerdotes nos seus cargos e os animou a servirem na Casa do Senhor.
3 Disse aos levitas que ensinavam a todo o Israel e estavam consagrados ao Senhor: Ponde a arca sagrada na casa que edificou Salomão, filho de Davi, rei de Israel; já não tereis esta carga aos ombros; servi, pois, ao Senhor, vosso Deus, e ao seu povo de Israel.
4 Preparai-vos segundo as vossas famílias, segundo os vossos turnos, segundo a prescrição de Davi, rei de Israel, e a de Salomão, seu filho.
5 Ministrai no santuário segundo os grupos das famílias de vossos irmãos, os filhos do povo; e haja, para cada grupo, uma parte das famílias dos levitas.
6 Imolai o cordeiro da Páscoa; e santificai-vos e preparai-o para vossos irmãos, fazendo segundo a palavra do Senhor, dada por intermédio de Moisés.
7 Ofereceu Josias a todo o povo cordeiros e cabritos do rebanho, todos para os sacrifícios da Páscoa, em número de trinta mil, por todos que se achavam ali; e, de bois, três mil; tudo isto era da fazenda do rei.
8 Também fizeram os seus príncipes ofertas voluntárias ao povo, aos sacerdotes e aos levitas; Hilquias, Zacarias e Jeiel, chefes da Casa de Deus, deram aos sacerdotes, para os sacrifícios da Páscoa, dois mil e seiscentos cordeiros e cabritos e trezentos bois.
9 Conanias, Semaías e Natanael, seus irmãos, como também Hasabias, Jeiel e Jozabade, chefes dos levitas, apresentaram aos levitas, para os sacrifícios da Páscoa, cinco mil cordeiros e cabritos e quinhentos bois.
10 Assim, se preparou o serviço, e puseram-se os sacerdotes nos seus lugares e também os levitas, pelos seus turnos, segundo o mandado do rei.
11 Então, imolaram o cordeiro da Páscoa; e os sacerdotes aspergiam o sangue recebido das mãos dos levitas que esfolavam as reses.
12 Puseram de parte o que era para os holocaustos e o deram ao povo, segundo os grupos das famílias, para que estes o oferecessem ao Senhor, como está escrito no Livro de Moisés; e assim fizeram com os bois.
13 Assaram o cordeiro da Páscoa no fogo, segundo o rito; as ofertas sagradas cozeram em panelas, em caldeirões e em assadeiras; e os levitas as repartiram entre todo o povo.
14 Depois, as prepararam para si e para os sacerdotes; porque os sacerdotes, filhos de Arão, se ocuparam, até à noite, com o sacrifício dos holocaustos e da gordura; por isso é que os levitas prepararam para si e para os sacerdotes, filhos de Arão.
15 Os cantores, filhos de Asafe, estavam nos seus lugares, segundo o mandado de Davi, e de Asafe, e de Hemã, e de Jedutum, vidente do rei, como também os porteiros, a cada porta; não necessitaram de se desviarem do seu ministério; porquanto seus irmãos, os levitas, preparavam o necessário para eles.
16 Assim, se estabeleceu todo o serviço do Senhor, naquele dia, para celebrar a Páscoa e oferecer holocaustos sobre o altar do Senhor, segundo o mandado do rei Josias.
17 Os filhos de Israel que se acharam presentes celebraram a Páscoa naquele tempo e a Festa dos Pães Asmos, por sete dias.
18 Nunca, pois, se celebrou tal Páscoa em Israel, desde os dias do profeta Samuel; e nenhum dos reis de Israel celebrou tal Páscoa, como a que celebrou Josias com os sacerdotes e levitas, e todo o Judá e Israel, que se acharam ali, e os habitantes de Jerusalém.
19 No décimo oitavo ano do reinado de Josias, se celebrou esta Páscoa.
20 Depois de tudo isto, havendo Josias já restaurado o templo, subiu Neco, rei do Egito, para guerrear contra Carquemis, junto ao Eufrates. Josias saiu de encontro a ele.
21 Então, Neco lhe mandou mensageiros, dizendo: Que tenho eu contigo, rei de Judá? Não vou contra ti hoje, mas contra a casa que me faz guerra; e disse Deus que me apressasse; cuida de não te opores a Deus, que é comigo, para que ele não te destrua.
22 Porém Josias não tornou atrás; antes, se disfarçou para pelejar contra ele e, não dando ouvidos às palavras que Neco lhe falara da parte de Deus, saiu a pelejar no vale de Megido.
23 Os flecheiros atiraram contra o rei Josias; então, o rei disse a seus servos: Tirai-me daqui, porque estou gravemente ferido.
24 Seus servos o tiraram do carro, levaram-no para o segundo carro que tinha e o transportaram a Jerusalém; ele morreu, e o sepultaram nos sepulcros de seus pais. Todo o Judá e Jerusalém prantearam Josias.
25 Jeremias compôs uma lamentação sobre Josias; e todos os cantores e cantoras, nas suas lamentações, se têm referido a Josias, até ao dia de hoje; porque as deram por prática em Israel, e estão escritas no Livro de Lamentações.
26 Quanto aos atos de Josias e às suas beneficências, segundo está escrito na Lei do Senhor,
27 e aos mais atos, tanto os primeiros como os últimos, eis que estão escritos no Livro da História dos Reis de Israel e de Judá.*
1 O povo da terra tomou a Joacaz, filho de Josias, e o fez rei em lugar de seu pai, em Jerusalém.
2 Tinha Joacaz vinte e três anos de idade quando começou a reinar e reinou três meses em Jerusalém;
3 porque o rei do Egito o depôs em Jerusalém e impôs à terra a pena de cem talentos de prata e um de ouro.
4 O rei do Egito constituiu a Eliaquim, irmão de Joacaz, rei sobre Judá e Jerusalém e lhe mudou o nome para Jeoaquim; mas ao irmão Joacaz tomou Neco e o levou para o Egito.
5 Tinha Jeoaquim a idade de vinte e cinco anos quando começou a reinar e reinou onze anos em Jerusalém. Fez ele o que era mau perante o Senhor, seu Deus.
6 Subiu, pois, contra ele Nabucodonosor, rei da Babilônia, e o amarrou com duas cadeias de bronze, para o levar à Babilônia.
7 Também alguns dos utensílios da Casa do Senhor levou Nabucodonosor para a Babilônia, onde os pôs no seu templo.
8 Quanto aos mais atos de Jeoaquim, e às abominações que cometeu, e ao mais que se achou nele, eis que estão escritos no Livro da História dos Reis de Israel e de Judá; e Joaquim, seu filho, reinou em seu lugar.
9 Tinha Joaquim dezoito anos quando começou a reinar e reinou três meses e dez dias em Jerusalém. Fez ele o que era mau perante o Senhor.
10 Na primavera do ano, mandou o rei Nabucodonosor levá-lo à Babilônia, com os mais preciosos utensílios da Casa do Senhor; e estabeleceu a Zedequias, seu irmão, rei sobre Judá e Jerusalém.
11 Tinha Zedequias a idade de vinte e um anos quando começou a reinar e reinou onze anos em Jerusalém.
12 Fez o que era mau perante o Senhor, seu Deus, e não se humilhou perante o profeta Jeremias, que falava da parte do Senhor.
13 Rebelou-se também contra o rei Nabucodonosor, que o tinha ajuramentado por Deus; mas endureceu a sua cerviz e tanto se obstinou no seu coração, que não voltou ao Senhor, Deus de Israel.
14 Também todos os chefes dos sacerdotes e o povo aumentavam mais e mais as transgressões, segundo todas as abominações dos gentios; e contaminaram a casa que o Senhor tinha santificado em Jerusalém.
15 O Senhor, Deus de seus pais, começando de madrugada, falou-lhes por intermédio dos seus mensageiros, porque se compadecera do seu povo e da sua própria morada.
16 Eles, porém, zombavam dos mensageiros, desprezavam as palavras de Deus e mofavam dos seus profetas, até que subiu a ira do Senhor contra o seu povo, e não houve remédio algum.
17 Por isso, o Senhor fez subir contra ele o rei dos caldeus, o qual matou os seus jovens à espada, na casa do seu santuário; e não teve piedade nem dos jovens nem das donzelas, nem dos velhos nem dos mais avançados em idade; a todos os deu nas suas mãos.
18 Todos os utensílios da Casa de Deus, grandes e pequenos, os tesouros da Casa do Senhor e os tesouros do rei e dos seus príncipes, tudo levou ele para a Babilônia.
19 Queimaram a Casa de Deus e derribaram os muros de Jerusalém; todos os seus palácios queimaram, destruindo também todos os seus preciosos objetos.
20 Os que escaparam da espada, a esses levou ele para a Babilônia, onde se tornaram seus servos e de seus filhos, até ao tempo do reino da Pérsia;
21 para que se cumprisse a palavra do Senhor, por boca de Jeremias, até que a terra se agradasse dos seus sábados; todos os dias da desolação repousou, até que os setenta anos se cumpriram.
22 Porém, no primeiro ano de Ciro, rei da Pérsia, para que se cumprisse a palavra do Senhor, por boca de Jeremias, despertou o Senhor o espírito de Ciro, rei da Pérsia, o qual fez passar pregão por todo o seu reino, como também por escrito, dizendo:
23 Assim diz Ciro, rei da Pérsia: O Senhor, Deus dos céus, me deu todos os reinos da terra e me encarregou de lhe edificar uma casa em Jerusalém, que está em Judá; quem entre vós é de todo o seu povo, que suba, e o Senhor, seu Deus, seja com ele.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'2_Crônicas','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)