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
1 Escrevi o primeiro livro, ó Teófilo, relatando todas as coisas que Jesus começou a fazer e a ensinar
2 até ao dia em que, depois de haver dado mandamentos por intermédio do Espírito Santo aos apóstolos que escolhera, foi elevado às alturas.
3 A estes também, depois de ter padecido, se apresentou vivo, com muitas provas incontestáveis, aparecendo-lhes durante quarenta dias e falando das coisas concernentes ao reino de Deus.
4 E, comendo com eles, determinou-lhes que não se ausentassem de Jerusalém, mas que esperassem a promessa do Pai, a qual, disse ele, de mim ouvistes.
5 Porque João, na verdade, batizou com água, mas vós sereis batizados com o Espírito Santo, não muito depois destes dias.
6 Então, os que estavam reunidos lhe perguntaram: Senhor, será este o tempo em que restaures o reino a Israel?
7 Respondeu-lhes: Não vos compete conhecer tempos ou épocas que o Pai reservou pela sua exclusiva autoridade;
8 mas recebereis poder, ao descer sobre vós o Espírito Santo, e sereis minhas testemunhas tanto em Jerusalém como em toda a Judeia e Samaria e até aos confins da terra.
9 Ditas estas palavras, foi Jesus elevado às alturas, à vista deles, e uma nuvem o encobriu dos seus olhos.
10 E, estando eles com os olhos fitos no céu, enquanto Jesus subia, eis que dois varões vestidos de branco se puseram ao lado deles
11 e lhes disseram: Varões galileus, por que estais olhando para as alturas? Esse Jesus que dentre vós foi assunto ao céu virá do modo como o vistes subir.
12 Então, voltaram para Jerusalém, do monte chamado Olival, que dista daquela cidade tanto como a jornada de um sábado.
13 Quando ali entraram, subiram para o cenáculo onde se reuniam Pedro, João, Tiago, André, Filipe, Tomé, Bartolomeu, Mateus, Tiago, filho de Alfeu, Simão, o Zelote, e Judas, filho de Tiago.
14 Todos estes perseveravam unânimes em oração, com as mulheres, com Maria, mãe de Jesus, e com os irmãos dele.
15 Naqueles dias, levantou-se Pedro no meio dos irmãos (ora, compunha-se a assembleia de umas cento e vinte pessoas) e disse:
16 Irmãos, convinha que se cumprisse a Escritura que o Espírito Santo proferiu anteriormente por boca de Davi, acerca de Judas, que foi o guia daqueles que prenderam Jesus,
17 porque ele era contado entre nós e teve parte neste ministério.
18 (Ora, este homem adquiriu um campo com o preço da iniquidade; e, precipitando-se, rompeu-se pelo meio, e todas as suas entranhas se derramaram;
19 e isto chegou ao conhecimento de todos os habitantes de Jerusalém, de maneira que em sua própria língua esse campo era chamado Aceldama, isto é, Campo de Sangue. )
20 Porque está escrito no Livro dos Salmos: Fique deserta a sua morada; e não haja quem nela habite; e: Tome outro o seu encargo.
21 É necessário, pois, que, dos homens que nos acompanharam todo o tempo que o Senhor Jesus andou entre nós,
22 começando no batismo de João, até ao dia em que dentre nós foi levado às alturas, um destes se torne testemunha conosco da sua ressurreição.
23 Então, propuseram dois: José, chamado Barsabás, cognominado Justo, e Matias.
24 E, orando, disseram: Tu, Senhor, que conheces o coração de todos, revela-nos qual destes dois tens escolhido
25 para preencher a vaga neste ministério e apostolado, do qual Judas se transviou, indo para o seu próprio lugar.
26 E os lançaram em sortes, vindo a sorte recair sobre Matias, sendo-lhe, então, votado lugar com os onze apóstolos.*
1 Ao cumprir-se o dia de Pentecostes, estavam todos reunidos no mesmo lugar;
2 de repente, veio do céu um som, como de um vento impetuoso, e encheu toda a casa onde estavam assentados.
3 E apareceram, distribuídas entre eles, línguas, como de fogo, e pousou uma sobre cada um deles.
4 Todos ficaram cheios do Espírito Santo e passaram a falar em outras línguas, segundo o Espírito lhes concedia que falassem.
5 Ora, estavam habitando em Jerusalém judeus, homens piedosos, vindos de todas as nações debaixo do céu.
6 Quando, pois, se fez ouvir aquela voz, afluiu a multidão, que se possuiu de perplexidade, porquanto cada um os ouvia falar na sua própria língua.
7 Estavam, pois, atônitos e se admiravam, dizendo: Vede! Não são, porventura, galileus todos esses que aí estão falando?
8 E como os ouvimos falar, cada um em nossa própria língua materna?
9 Somos partos, medos, elamitas e os naturais da Mesopotâmia, Judeia, Capadócia, Ponto e Ásia,
10 da Frígia, da Panfília, do Egito e das regiões da Líbia, nas imediações de Cirene, e romanos que aqui residem,
11 tanto judeus como prosélitos, cretenses e arábios. Como os ouvimos falar em nossas próprias línguas as grandezas de Deus?
12 Todos, atônitos e perplexos, interpelavam uns aos outros: Que quer isto dizer?
13 Outros, porém, zombando, diziam: Estão embriagados!
14 Então, se levantou Pedro, com os onze; e, erguendo a voz, advertiu-os nestes termos: Varões judeus e todos os habitantes de Jerusalém, tomai conhecimento disto e atentai nas minhas palavras.
15 Estes homens não estão embriagados, como vindes pensando, sendo esta a terceira hora do dia.
16 Mas o que ocorre é o que foi dito por intermédio do profeta Joel:
17 E acontecerá nos últimos dias, diz o Senhor, que derramarei do meu Espírito sobre toda a carne; vossos filhos e vossas filhas profetizarão, vossos jovens terão visões, e sonharão vossos velhos;
18 até sobre os meus servos e sobre as minhas servas derramarei do meu Espírito naqueles dias, e profetizarão.
19 Mostrarei prodígios em cima no céu e sinais embaixo na terra: sangue, fogo e vapor de fumaça.
20 O sol se converterá em trevas, e a lua, em sangue, antes que venha o grande e glorioso Dia do Senhor.
21 E acontecerá que todo aquele que invocar o nome do Senhor será salvo.
22 Varões israelitas, atendei a estas palavras: Jesus, o Nazareno, varão aprovado por Deus diante de vós com milagres, prodígios e sinais, os quais o próprio Deus realizou por intermédio dele entre vós, como vós mesmos sabeis;
23 sendo este entregue pelo determinado desígnio e presciência de Deus, vós o matastes, crucificando-o por mãos de iníquos;
24 ao qual, porém, Deus ressuscitou, rompendo os grilhões da morte; porquanto não era possível fosse ele retido por ela.
25 Porque a respeito dele diz Davi: Diante de mim via sempre o Senhor, porque está à minha direita, para que eu não seja abalado.
26 Por isso, se alegrou o meu coração, e a minha língua exultou; além disto, também a minha própria carne repousará em esperança,
27 porque não deixarás a minha alma na morte, nem permitirás que o teu Santo veja corrupção.
28 Fizeste-me conhecer os caminhos da vida, encher-me-ás de alegria na tua presença.
29 Irmãos, seja-me permitido dizer-vos claramente a respeito do patriarca Davi que ele morreu e foi sepultado, e o seu túmulo permanece entre nós até hoje.
30 Sendo, pois, profeta e sabendo que Deus lhe havia jurado que um dos seus descendentes se assentaria no seu trono,
31 prevendo isto, referiu-se à ressurreição de Cristo, que nem foi deixado na morte, nem o seu corpo experimentou corrupção.
32 A este Jesus Deus ressuscitou, do que todos nós somos testemunhas.
33 Exaltado, pois, à destra de Deus, tendo recebido do Pai a promessa do Espírito Santo, derramou isto que vedes e ouvis.
34 Porque Davi não subiu aos céus, mas ele mesmo declara: Disse o Senhor ao meu Senhor: Assenta-te à minha direita,
35 até que eu ponha os teus inimigos por estrado dos teus pés.
36 Esteja absolutamente certa, pois, toda a casa de Israel de que a este Jesus, que vós crucificastes, Deus o fez Senhor e Cristo.
37 Ouvindo eles estas coisas, compungiu-se-lhes o coração e perguntaram a Pedro e aos demais apóstolos: Que faremos, irmãos?
38 Respondeu-lhes Pedro: Arrependei-vos, e cada um de vós seja batizado em nome de Jesus Cristo para remissão dos vossos pecados, e recebereis o dom do Espírito Santo.
39 Pois para vós outros é a promessa, para vossos filhos e para todos os que ainda estão longe, isto é, para quantos o Senhor, nosso Deus, chamar.
40 Com muitas outras palavras deu testemunho e exortava-os, dizendo: Salvai-vos desta geração perversa.
41 Então, os que lhe aceitaram a palavra foram batizados, havendo um acréscimo naquele dia de quase três mil pessoas.
42 E perseveravam na doutrina dos apóstolos e na comunhão, no partir do pão e nas orações.
43 Em cada alma havia temor; e muitos prodígios e sinais eram feitos por intermédio dos apóstolos.
44 Todos os que creram estavam juntos e tinham tudo em comum.
45 Vendiam as suas propriedades e bens, distribuindo o produto entre todos, à medida que alguém tinha necessidade.
46 Diariamente perseveravam unânimes no templo, partiam pão de casa em casa e tomavam as suas refeições com alegria e singeleza de coração,
47 louvando a Deus e contando com a simpatia de todo o povo. Enquanto isso, acrescentava-lhes o Senhor, dia a dia, os que iam sendo salvos.*
1 Pedro e João subiam ao templo para a oração da hora nona.
2 Era levado um homem, coxo de nascença, o qual punham diariamente à porta do templo chamada Formosa, para pedir esmola aos que entravam.
3 Vendo ele a Pedro e João, que iam entrar no templo, implorava que lhe dessem uma esmola.
4 Pedro, fitando-o, juntamente com João, disse: Olha para nós.
5 Ele os olhava atentamente, esperando receber alguma coisa.
6 Pedro, porém, lhe disse: Não possuo nem prata nem ouro, mas o que tenho, isso te dou: em nome de Jesus Cristo, o Nazareno, anda!
7 E, tomando-o pela mão direita, o levantou; imediatamente, os seus pés e tornozelos se firmaram;
8 de um salto se pôs em pé, passou a andar e entrou com eles no templo, saltando e louvando a Deus.
9 Viu-o todo o povo a andar e a louvar a Deus,
10 e reconheceram ser ele o mesmo que esmolava, assentado à Porta Formosa do templo; e se encheram de admiração e assombro por isso que lhe acontecera.
11 Apegando-se ele a Pedro e a João, todo o povo correu atônito para junto deles no pórtico chamado de Salomão.
12 À vista disto, Pedro se dirigiu ao povo, dizendo: Israelitas, por que vos maravilhais disto ou por que fitais os olhos em nós como se pelo nosso próprio poder ou piedade o tivéssemos feito andar?
13 O Deus de Abraão, de Isaque e de Jacó, o Deus de nossos pais, glorificou a seu Servo Jesus, a quem vós traístes e negastes perante Pilatos, quando este havia decidido soltá-lo.
14 Vós, porém, negastes o Santo e o Justo e pedistes que vos concedessem um homicida.
15 Dessarte, matastes o Autor da vida, a quem Deus ressuscitou dentre os mortos, do que nós somos testemunhas.
16 Pela fé em o nome de Jesus, é que esse mesmo nome fortaleceu a este homem que agora vedes e reconheceis; sim, a fé que vem por meio de Jesus deu a este saúde perfeita na presença de todos vós.
17 E agora, irmãos, eu sei que o fizestes por ignorância, como também as vossas autoridades;
18 mas Deus, assim, cumpriu o que dantes anunciara por boca de todos os profetas: que o seu Cristo havia de padecer.
19 Arrependei-vos, pois, e convertei-vos para serem cancelados os vossos pecados,
20 a fim de que, da presença do Senhor, venham tempos de refrigério, e que envie ele o Cristo, que já vos foi designado, Jesus,
21 ao qual é necessário que o céu receba até aos tempos da restauração de todas as coisas, de que Deus falou por boca dos seus santos profetas desde a antiguidade.
22 Disse, na verdade, Moisés: O Senhor Deus vos suscitará dentre vossos irmãos um profeta semelhante a mim; a ele ouvireis em tudo quanto vos disser.
23 Acontecerá que toda alma que não ouvir a esse profeta será exterminada do meio do povo.
24 E todos os profetas, a começar com Samuel, assim como todos quantos depois falaram, também anunciaram estes dias.
25 Vós sois os filhos dos profetas e da aliança que Deus estabeleceu com vossos pais, dizendo a Abraão: Na tua descendência, serão abençoadas todas as nações da terra.
26 Tendo Deus ressuscitado o seu Servo, enviou-o primeiramente a vós outros para vos abençoar, no sentido de que cada um se aparte das suas perversidades.*
1 Falavam eles ainda ao povo quando sobrevieram os sacerdotes, o capitão do templo e os saduceus,
2 ressentidos por ensinarem eles o povo e anunciarem, em Jesus, a ressurreição dentre os mortos;
3 e os prenderam, recolhendo-os ao cárcere até ao dia seguinte, pois já era tarde.
4 Muitos, porém, dos que ouviram a palavra a aceitaram, subindo o número de homens a quase cinco mil.
5 No dia seguinte, reuniram-se em Jerusalém as autoridades, os anciãos e os escribas
6 com o sumo sacerdote Anás, Caifás, João, Alexandre e todos os que eram da linhagem do sumo sacerdote;
7 e, pondo-os perante eles, os arguiram: Com que poder ou em nome de quem fizestes isto?
8 Então, Pedro, cheio do Espírito Santo, lhes disse: Autoridades do povo e anciãos,
9 visto que hoje somos interrogados a propósito do benefício feito a um homem enfermo e do modo por que foi curado,
10 tomai conhecimento, vós todos e todo o povo de Israel, de que, em nome de Jesus Cristo, o Nazareno, a quem vós crucificastes, e a quem Deus ressuscitou dentre os mortos, sim, em seu nome é que este está curado perante vós.
11 Este Jesus é pedra rejeitada por vós, os construtores, a qual se tornou a pedra angular.
12 E não há salvação em nenhum outro; porque abaixo do céu não existe nenhum outro nome, dado entre os homens, pelo qual importa que sejamos salvos.
13 Ao verem a intrepidez de Pedro e João, sabendo que eram homens iletrados e incultos, admiraram-se; e reconheceram que haviam eles estado com Jesus.
14 Vendo com eles o homem que fora curado, nada tinham que dizer em contrário.
15 E, mandando-os sair do Sinédrio, consultavam entre si,
16 dizendo: Que faremos com estes homens? Pois, na verdade, é manifesto a todos os habitantes de Jerusalém que um sinal notório foi feito por eles, e não o podemos negar;
17 mas, para que não haja maior divulgação entre o povo, ameacemo-los para não mais falarem neste nome a quem quer que seja.
18 Chamando-os, ordenaram-lhes que absolutamente não falassem, nem ensinassem em o nome de Jesus.
19 Mas Pedro e João lhes responderam: Julgai se é justo diante de Deus ouvir-vos antes a vós outros do que a Deus;
20 pois nós não podemos deixar de falar das coisas que vimos e ouvimos.
21 Depois, ameaçando-os mais ainda, os soltaram, não tendo achado como os castigar, por causa do povo, porque todos glorificavam a Deus pelo que acontecera.
22 Ora, tinha mais de quarenta anos aquele em quem se operara essa cura milagrosa.
23 Uma vez soltos, procuraram os irmãos e lhes contaram quantas coisas lhes haviam dito os principais sacerdotes e os anciãos.
24 Ouvindo isto, unânimes, levantaram a voz a Deus e disseram: Tu, Soberano Senhor, que fizeste o céu, a terra, o mar e tudo o que neles há;
25 que disseste por intermédio do Espírito Santo, por boca de Davi, nosso pai, teu servo: Por que se enfureceram os gentios, e os povos imaginaram coisas vãs?
26 Levantaram-se os reis da terra, e as autoridades ajuntaram-se à uma contra o Senhor e contra o seu Ungido;
27 porque verdadeiramente se ajuntaram nesta cidade contra o teu santo Servo Jesus, ao qual ungiste, Herodes e Pôncio Pilatos, com gentios e gente de Israel,
28 para fazerem tudo o que a tua mão e o teu propósito predeterminaram;
29 agora, Senhor, olha para as suas ameaças e concede aos teus servos que anunciem com toda a intrepidez a tua palavra,
30 enquanto estendes a mão para fazer curas, sinais e prodígios por intermédio do nome do teu santo Servo Jesus.
31 Tendo eles orado, tremeu o lugar onde estavam reunidos; todos ficaram cheios do Espírito Santo e, com intrepidez, anunciavam a palavra de Deus.
32 Da multidão dos que creram era um o coração e a alma. Ninguém considerava exclusivamente sua nem uma das coisas que possuía; tudo, porém, lhes era comum.
33 Com grande poder, os apóstolos davam testemunho da ressurreição do Senhor Jesus, e em todos eles havia abundante graça.
34 Pois nenhum necessitado havia entre eles, porquanto os que possuíam terras ou casas, vendendo-as, traziam os valores correspondentes
35 e depositavam aos pés dos apóstolos; então, se distribuía a qualquer um à medida que alguém tinha necessidade.
36 José, a quem os apóstolos deram o sobrenome de Barnabé, que quer dizer filho de exortação, levita, natural de Chipre,
37 como tivesse um campo, vendendo-o, trouxe o preço e o depositou aos pés dos apóstolos.*
1 Entretanto, certo homem, chamado Ananias, com sua mulher Safira, vendeu uma propriedade,
2 mas, em acordo com sua mulher, reteve parte do preço e, levando o restante, depositou-o aos pés dos apóstolos.
3 Então, disse Pedro: Ananias, por que encheu Satanás teu coração, para que mentisses ao Espírito Santo, reservando parte do valor do campo?
4 Conservando-o, porventura, não seria teu? E, vendido, não estaria em teu poder? Como, pois, assentaste no coração este desígnio? Não mentiste aos homens, mas a Deus.
5 Ouvindo estas palavras, Ananias caiu e expirou, sobrevindo grande temor a todos os ouvintes.
6 Levantando-se os moços, cobriram-lhe o corpo e, levando-o, o sepultaram.
7 Quase três horas depois, entrou a mulher de Ananias, não sabendo o que ocorrera.
8 Então, Pedro, dirigindo-se a ela, perguntou-lhe: Dize-me, vendestes por tanto aquela terra? Ela respondeu: Sim, por tanto.
9 Tornou-lhe Pedro: Por que entrastes em acordo para tentar o Espírito do Senhor? Eis aí à porta os pés dos que sepultaram o teu marido, e eles também te levarão.
10 No mesmo instante, caiu ela aos pés de Pedro e expirou. Entrando os moços, acharam-na morta e, levando-a, sepultaram-na junto do marido.
11 E sobreveio grande temor a toda a igreja e a todos quantos ouviram a notícia destes acontecimentos.
12 Muitos sinais e prodígios eram feitos entre o povo pelas mãos dos apóstolos. E costumavam todos reunir-se, de comum acordo, no Pórtico de Salomão.
13 Mas, dos restantes, ninguém ousava ajuntar-se a eles; porém o povo lhes tributava grande admiração.
14 E crescia mais e mais a multidão de crentes, tanto homens como mulheres, agregados ao Senhor,
15 a ponto de levarem os enfermos até pelas ruas e os colocarem sobre leitos e macas, para que, ao passar Pedro, ao menos a sua sombra se projetasse nalguns deles.
16 Afluía também muita gente das cidades vizinhas a Jerusalém, levando doentes e atormentados de espíritos imundos, e todos eram curados.
17 Levantando-se, porém, o sumo sacerdote e todos os que estavam com ele, isto é, a seita dos saduceus, tomaram-se de inveja,
18 prenderam os apóstolos e os recolheram à prisão pública.
19 Mas, de noite, um anjo do Senhor abriu as portas do cárcere e, conduzindo-os para fora, lhes disse:
20 Ide e, apresentando-vos no templo, dizei ao povo todas as palavras desta Vida.
21 Tendo ouvido isto, logo ao romper do dia, entraram no templo e ensinavam. Chegando, porém, o sumo sacerdote e os que com ele estavam, convocaram o Sinédrio e todo o senado dos filhos de Israel e mandaram buscá-los no cárcere.
22 Mas os guardas, indo, não os acharam no cárcere; e, tendo voltado, relataram,
23 dizendo: Achamos o cárcere fechado com toda a segurança e as sentinelas nos seus postos junto às portas; mas, abrindo-as, a ninguém encontramos dentro.
24 Quando o capitão do templo e os principais sacerdotes ouviram estas informações, ficaram perplexos a respeito deles e do que viria a ser isto.
25 Nesse ínterim, alguém chegou e lhes comunicou: Eis que os homens que recolhestes no cárcere, estão no templo ensinando o povo.
26 Nisto, indo o capitão e os guardas, os trouxeram sem violência, porque temiam ser apedrejados pelo povo.
27 Trouxeram-nos, apresentando-os ao Sinédrio. E o sumo sacerdote interrogou-os,
28 dizendo: Expressamente vos ordenamos que não ensinásseis nesse nome; contudo, enchestes Jerusalém de vossa doutrina; e quereis lançar sobre nós o sangue desse homem.
29 Então, Pedro e os demais apóstolos afirmaram: Antes, importa obedecer a Deus do que aos homens.
30 O Deus de nossos pais ressuscitou a Jesus, a quem vós matastes, pendurando-o num madeiro.
31 Deus, porém, com a sua destra, o exaltou a Príncipe e Salvador, a fim de conceder a Israel o arrependimento e a remissão de pecados.
32 Ora, nós somos testemunhas destes fatos, e bem assim o Espírito Santo, que Deus outorgou aos que lhe obedecem.
33 Eles, porém, ouvindo, se enfureceram e queriam matá-los.
34 Mas, levantando-se no Sinédrio um fariseu, chamado Gamaliel, mestre da lei, acatado por todo o povo, mandou retirar os homens, por um pouco,
35 e lhes disse: Israelitas, atentai bem no que ides fazer a estes homens.
36 Porque, antes destes dias, se levantou Teudas, insinuando ser ele alguma coisa, ao qual se agregaram cerca de quatrocentos homens; mas ele foi morto, e todos quantos lhe prestavam obediência se dispersaram e deram em nada.
37 Depois desse, levantou-se Judas, o galileu, nos dias do recenseamento, e levou muitos consigo; também este pereceu, e todos quantos lhe obedeciam foram dispersos.
38 Agora, vos digo: dai de mão a estes homens, deixai-os; porque, se este conselho ou esta obra vem de homens, perecerá;
39 mas, se é de Deus, não podereis destruí-los, para que não sejais, porventura, achados lutando contra Deus. E concordaram com ele.
40 Chamando os apóstolos, açoitaram-nos e, ordenando-lhes que não falassem em o nome de Jesus, os soltaram.
41 E eles se retiraram do Sinédrio regozijando-se por terem sido considerados dignos de sofrer afrontas por esse Nome.
42 E todos os dias, no templo e de casa em casa, não cessavam de ensinar e de pregar Jesus, o Cristo.*
1 Ora, naqueles dias, multiplicando-se o número dos discípulos, houve murmuração dos helenistas contra os hebreus, porque as viúvas deles estavam sendo esquecidas na distribuição diária.
2 Então, os doze convocaram a comunidade dos discípulos e disseram: Não é razoável que nós abandonemos a palavra de Deus para servir às mesas.
3 Mas, irmãos, escolhei dentre vós sete homens de boa reputação, cheios do Espírito e de sabedoria, aos quais encarregaremos deste serviço;
4 e, quanto a nós, nos consagraremos à oração e ao ministério da palavra.
5 O parecer agradou a toda a comunidade; e elegeram Estêvão, homem cheio de fé e do Espírito Santo, Filipe, Prócoro, Nicanor, Timão, Pármenas e Nicolau, prosélito de Antioquia.
6 Apresentaram-nos perante os apóstolos, e estes, orando, lhes impuseram as mãos.
7 Crescia a palavra de Deus, e, em Jerusalém, se multiplicava o número dos discípulos; também muitíssimos sacerdotes obedeciam à fé.
8 Estêvão, cheio de graça e poder, fazia prodígios e grandes sinais entre o povo.
9 Levantaram-se, porém, alguns dos que eram da sinagoga chamada dos Libertos, dos cireneus, dos alexandrinos e dos da Cilícia e Ásia, e discutiam com Estêvão;
10 e não podiam resistir à sabedoria e ao Espírito, pelo qual ele falava.
11 Então, subornaram homens que dissessem: Temos ouvido este homem proferir blasfêmias contra Moisés e contra Deus.
12 Sublevaram o povo, os anciãos e os escribas e, investindo, o arrebataram, levando-o ao Sinédrio.
13 Apresentaram testemunhas falsas, que depuseram: Este homem não cessa de falar contra o lugar santo e contra a lei;
14 porque o temos ouvido dizer que esse Jesus, o Nazareno, destruirá este lugar e mudará os costumes que Moisés nos deu.
15 Todos os que estavam assentados no Sinédrio, fitando os olhos em Estêvão, viram o seu rosto como se fosse rosto de anjo.*
1 Então, lhe perguntou o sumo sacerdote: Porventura, é isto assim?
2 Estêvão respondeu: Varões irmãos e pais, ouvi. O Deus da glória apareceu a Abraão, nosso pai, quando estava na Mesopotâmia, antes de habitar em Harã,
3 e lhe disse: Sai da tua terra e da tua parentela e vem para a terra que eu te mostrarei.
4 Então, saiu da terra dos caldeus e foi habitar em Harã. E dali, com a morte de seu pai, Deus o trouxe para esta terra em que vós agora habitais.
5 Nela, não lhe deu herança, nem sequer o espaço de um pé; mas prometeu dar-lhe a posse dela e, depois dele, à sua descendência, não tendo ele filho.
6 E falou Deus que a sua descendência seria peregrina em terra estrangeira, onde seriam escravizados e maltratados por quatrocentos anos;
7 eu, disse Deus, julgarei a nação da qual forem escravos; e, depois disto, sairão daí e me servirão neste lugar.
8 Então, lhe deu a aliança da circuncisão; assim, nasceu Isaque, e Abraão o circuncidou ao oitavo dia; de Isaque procedeu Jacó, e deste, os doze patriarcas.
9 Os patriarcas, invejosos de José, venderam-no para o Egito; mas Deus estava com ele
10 e livrou-o de todas as suas aflições, concedendo-lhe também graça e sabedoria perante Faraó, rei do Egito, que o constituiu governador daquela nação e de toda a casa real.
11 Sobreveio, porém, fome em todo o Egito; e, em Canaã, houve grande tribulação, e nossos pais não achavam mantimentos.
12 Mas, tendo ouvido Jacó que no Egito havia trigo, enviou, pela primeira vez, os nossos pais.
13 Na segunda vez, José se fez reconhecer por seus irmãos, e se tornou conhecida de Faraó a família de José.
14 Então, José mandou chamar a Jacó, seu pai, e toda a sua parentela, isto é, setenta e cinco pessoas.
15 Jacó desceu ao Egito, e ali morreu ele e também nossos pais;
16 e foram transportados para Siquém e postos no sepulcro que Abraão ali comprara a dinheiro aos filhos de Hamor.
17 Como, porém, se aproximasse o tempo da promessa que Deus jurou a Abraão, o povo cresceu e se multiplicou no Egito,
18 até que se levantou ali outro rei, que não conhecia a José.
19 Este outro rei tratou com astúcia a nossa raça e torturou os nossos pais, a ponto de forçá-los a enjeitar seus filhos, para que não sobrevivessem.
20 Por esse tempo, nasceu Moisés, que era formoso aos olhos de Deus. Por três meses, foi ele mantido na casa de seu pai;
21 quando foi exposto, a filha de Faraó o recolheu e criou como seu próprio filho.
22 E Moisés foi educado em toda a ciência dos egípcios e era poderoso em palavras e obras.
23 Quando completou quarenta anos, veio-lhe a ideia de visitar seus irmãos, os filhos de Israel.
24 Vendo um homem tratado injustamente, tomou-lhe a defesa e vingou o oprimido, matando o egípcio.
25 Ora, Moisés cuidava que seus irmãos entenderiam que Deus os queria salvar por intermédio dele; eles, porém, não compreenderam.
26 No dia seguinte, aproximou-se de uns que brigavam e procurou reconduzi-los à paz, dizendo: Homens, vós sois irmãos; por que vos ofendeis uns aos outros?
27 Mas o que agredia o próximo o repeliu, dizendo: Quem te constituiu autoridade e juiz sobre nós?
28 Acaso, queres matar-me, como fizeste ontem ao egípcio?
29 A estas palavras Moisés fugiu e tornou-se peregrino na terra de Midiã, onde lhe nasceram dois filhos.
30 Decorridos quarenta anos, apareceu-lhe, no deserto do monte Sinai, um anjo, por entre as chamas de uma sarça que ardia.
31 Moisés, porém, diante daquela visão, ficou maravilhado e, aproximando-se para observar, ouviu-se a voz do Senhor:
32 Eu sou o Deus dos teus pais, o Deus de Abraão, de Isaque e de Jacó. Moisés, tremendo de medo, não ousava contemplá-la.
33 Disse-lhe o Senhor: Tira a sandália dos pés, porque o lugar em que estás é terra santa.
34 Vi, com efeito, o sofrimento do meu povo no Egito, ouvi o seu gemido e desci para libertá-lo. Vem agora, e eu te enviarei ao Egito.
35 A este Moisés, a quem negaram reconhecer, dizendo: Quem te constituiu autoridade e juiz? A este enviou Deus como chefe e libertador, com a assistência do anjo que lhe apareceu na sarça.
36 Este os tirou, fazendo prodígios e sinais na terra do Egito, assim como no mar Vermelho e no deserto, durante quarenta anos.
37 Foi Moisés quem disse aos filhos de Israel: Deus vos suscitará dentre vossos irmãos um profeta semelhante a mim.
38 É este Moisés quem esteve na congregação no deserto, com o anjo que lhe falava no monte Sinai e com os nossos pais; o qual recebeu palavras vivas para no-las transmitir.
39 A quem nossos pais não quiseram obedecer; antes, o repeliram e, no seu coração, voltaram para o Egito,
40 dizendo a Arão: Faze-nos deuses que vão adiante de nós; porque, quanto a este Moisés, que nos tirou da terra do Egito, não sabemos o que lhe aconteceu.
41 Naqueles dias, fizeram um bezerro e ofereceram sacrifício ao ídolo, alegrando-se com as obras das suas mãos.
42 Mas Deus se afastou e os entregou ao culto da milícia celestial, como está escrito no Livro dos Profetas: Ó casa de Israel, porventura, me oferecestes vítimas e sacrifícios no deserto, pelo espaço de quarenta anos,
43 e, acaso, não levantastes o tabernáculo de Moloque e a estrela do deus Renfã, figuras que fizestes para as adorar? Por isso, vos desterrarei para além da Babilônia.
44 O tabernáculo do Testemunho estava entre nossos pais no deserto, como determinara aquele que disse a Moisés que o fizesse segundo o modelo que tinha visto.
45 O qual também nossos pais, com Josué, tendo-o recebido, o levaram, quando tomaram posse das nações que Deus expulsou da presença deles, até aos dias de Davi.
46 Este achou graça diante de Deus e lhe suplicou a faculdade de prover morada para o Deus de Jacó.
47 Mas foi Salomão quem lhe edificou a casa.
48 Entretanto, não habita o Altíssimo em casas feitas por mãos humanas; como diz o profeta:
49 O céu é o meu trono, e a terra, o estrado dos meus pés; que casa me edificareis, diz o Senhor, ou qual é o lugar do meu repouso?
50 Não foi, porventura, a minha mão que fez todas estas coisas?
51 Homens de dura cerviz e incircuncisos de coração e de ouvidos, vós sempre resistis ao Espírito Santo; assim como fizeram vossos pais, também vós o fazeis.
52 Qual dos profetas vossos pais não perseguiram? Eles mataram os que anteriormente anunciavam a vinda do Justo, do qual vós agora vos tornastes traidores e assassinos,
53 vós que recebestes a lei por ministério de anjos e não a guardastes.
54 Ouvindo eles isto, enfureciam-se no seu coração e rilhavam os dentes contra ele.
55 Mas Estêvão, cheio do Espírito Santo, fitou os olhos no céu e viu a glória de Deus e Jesus, que estava à sua direita,
56 e disse: Eis que vejo os céus abertos e o Filho do Homem, em pé à destra de Deus.
57 Eles, porém, clamando em alta voz, taparam os ouvidos e, unânimes, arremeteram contra ele.
58 E, lançando-o fora da cidade, o apedrejaram. As testemunhas deixaram suas vestes aos pés de um jovem chamado Saulo.
59 E apedrejavam Estêvão, que invocava e dizia: Senhor Jesus, recebe o meu espírito!
60 Então, ajoelhando-se, clamou em alta voz: Senhor, não lhes imputes este pecado! Com estas palavras, adormeceu.*
1 E Saulo consentia na sua morte. Naquele dia, levantou-se grande perseguição contra a igreja em Jerusalém; e todos, exceto os apóstolos, foram dispersos pelas regiões da Judeia e Samaria.
2 Alguns homens piedosos sepultaram Estêvão e fizeram grande pranto sobre ele.
3 Saulo, porém, assolava a igreja, entrando pelas casas; e, arrastando homens e mulheres, encerrava-os no cárcere.
4 Entrementes, os que foram dispersos iam por toda parte pregando a palavra.
5 Filipe, descendo à cidade de Samaria, anunciava-lhes a Cristo.
6 As multidões atendiam, unânimes, às coisas que Filipe dizia, ouvindo-as e vendo os sinais que ele operava.
7 Pois os espíritos imundos de muitos possessos saíam gritando em alta voz; e muitos paralíticos e coxos foram curados.
8 E houve grande alegria naquela cidade.
9 Ora, havia certo homem, chamado Simão, que ali praticava a mágica, iludindo o povo de Samaria, insinuando ser ele grande vulto;
10 ao qual todos davam ouvidos, do menor ao maior, dizendo: Este homem é o poder de Deus, chamado o Grande Poder.
11 Aderiam a ele porque havia muito os iludira com mágicas.
12 Quando, porém, deram crédito a Filipe, que os evangelizava a respeito do reino de Deus e do nome de Jesus Cristo, iam sendo batizados, assim homens como mulheres.
13 O próprio Simão abraçou a fé; e, tendo sido batizado, acompanhava a Filipe de perto, observando extasiado os sinais e grandes milagres praticados.
14 Ouvindo os apóstolos, que estavam em Jerusalém, que Samaria recebera a palavra de Deus, enviaram-lhe Pedro e João;
15 os quais, descendo para lá, oraram por eles para que recebessem o Espírito Santo;
16 porquanto não havia ainda descido sobre nenhum deles, mas somente haviam sido batizados em o nome do Senhor Jesus.
17 Então, lhes impunham as mãos, e recebiam estes o Espírito Santo.
18 Vendo, porém, Simão que, pelo fato de imporem os apóstolos as mãos, era concedido o Espírito [Santo], ofereceu-lhes dinheiro,
19 propondo: Concedei-me também a mim este poder, para que aquele sobre quem eu impuser as mãos receba o Espírito Santo.
20 Pedro, porém, lhe respondeu: O teu dinheiro seja contigo para perdição, pois julgaste adquirir, por meio dele, o dom de Deus.
21 Não tens parte nem sorte neste ministério, porque o teu coração não é reto diante de Deus.
22 Arrepende-te, pois, da tua maldade e roga ao Senhor; talvez te seja perdoado o intento do coração;
23 pois vejo que estás em fel de amargura e laço de iniquidade.
24 Respondendo, porém, Simão lhes pediu: Rogai vós por mim ao Senhor, para que nada do que dissestes sobrevenha a mim.
25 Eles, porém, havendo testificado e falado a palavra do Senhor, voltaram para Jerusalém e evangelizavam muitas aldeias dos samaritanos.
26 Um anjo do Senhor falou a Filipe, dizendo: Dispõe-te e vai para o lado do Sul, no caminho que desce de Jerusalém a Gaza; este se acha deserto. Ele se levantou e foi.
27 Eis que um etíope, eunuco, alto oficial de Candace, rainha dos etíopes, o qual era superintendente de todo o seu tesouro, que viera adorar em Jerusalém,
28 estava de volta e, assentado no seu carro, vinha lendo o profeta Isaías.
29 Então, disse o Espírito a Filipe: Aproxima-te desse carro e acompanha-o.
30 Correndo Filipe, ouviu-o ler o profeta Isaías e perguntou: Compreendes o que vens lendo?
31 Ele respondeu: Como poderei entender, se alguém não me explicar? E convidou Filipe a subir e a sentar-se junto a ele.
32 Ora, a passagem da Escritura que estava lendo era esta: Foi levado como ovelha ao matadouro; e, como um cordeiro mudo perante o seu tosquiador, assim ele não abriu a boca.
33 Na sua humilhação, lhe negaram justiça; quem lhe poderá descrever a geração? Porque da terra a sua vida é tirada.
34 Então, o eunuco disse a Filipe: Peço-te que me expliques a quem se refere o profeta. Fala de si mesmo ou de algum outro?
35 Então, Filipe explicou; e, começando por esta passagem da Escritura, anunciou-lhe a Jesus.
36 Seguindo eles caminho fora, chegando a certo lugar onde havia água, disse o eunuco: Eis aqui água; que impede que seja eu batizado?
37 [Filipe respondeu: É lícito, se crês de todo o coração. E, respondendo ele, disse: Creio que Jesus Cristo é o Filho de Deus.]
38 Então, mandou parar o carro, ambos desceram à água, e Filipe batizou o eunuco.
39 Quando saíram da água, o Espírito do Senhor arrebatou a Filipe, não o vendo mais o eunuco; e este foi seguindo o seu caminho, cheio de júbilo.
40 Mas Filipe veio a achar-se em Azoto; e, passando além, evangelizava todas as cidades até chegar a Cesareia.*
1 Saulo, respirando ainda ameaças e morte contra os discípulos do Senhor, dirigiu-se ao sumo sacerdote
2 e lhe pediu cartas para as sinagogas de Damasco, a fim de que, caso achasse alguns que eram do Caminho, assim homens como mulheres, os levasse presos para Jerusalém.
3 Seguindo ele estrada fora, ao aproximar-se de Damasco, subitamente uma luz do céu brilhou ao seu redor,
4 e, caindo por terra, ouviu uma voz que lhe dizia: Saulo, Saulo, por que me persegues?
5 Ele perguntou: Quem és tu, Senhor? E a resposta foi: Eu sou Jesus, a quem tu persegues;
6 mas levanta-te e entra na cidade, onde te dirão o que te convém fazer.
7 Os seus companheiros de viagem pararam emudecidos, ouvindo a voz, não vendo, contudo, ninguém.
8 Então, se levantou Saulo da terra e, abrindo os olhos, nada podia ver. E, guiando-o pela mão, levaram-no para Damasco.
9 Esteve três dias sem ver, durante os quais nada comeu, nem bebeu.
10 Ora, havia em Damasco um discípulo chamado Ananias. Disse-lhe o Senhor numa visão: Ananias! Ao que respondeu: Eis-me aqui, Senhor!
11 Então, o Senhor lhe ordenou: Dispõe-te, e vai à rua que se chama Direita, e, na casa de Judas, procura por Saulo, apelidado de Tarso; pois ele está orando
12 e viu entrar um homem, chamado Ananias, e impor-lhe as mãos, para que recuperasse a vista.
13 Ananias, porém, respondeu: Senhor, de muitos tenho ouvido a respeito desse homem, quantos males tem feito aos teus santos em Jerusalém;
14 e para aqui trouxe autorização dos principais sacerdotes para prender a todos os que invocam o teu nome.
15 Mas o Senhor lhe disse: Vai, porque este é para mim um instrumento escolhido para levar o meu nome perante os gentios e reis, bem como perante os filhos de Israel;
16 pois eu lhe mostrarei quanto lhe importa sofrer pelo meu nome.
17 Então, Ananias foi e, entrando na casa, impôs sobre ele as mãos, dizendo: Saulo, irmão, o Senhor me enviou, a saber, o próprio Jesus que te apareceu no caminho por onde vinhas, para que recuperes a vista e fiques cheio do Espírito Santo.
18 Imediatamente, lhe caíram dos olhos como que umas escamas, e tornou a ver. A seguir, levantou-se e foi batizado.
19 E, depois de ter-se alimentado, sentiu-se fortalecido. Então, permaneceu em Damasco alguns dias com os discípulos.
20 E logo pregava, nas sinagogas, a Jesus, afirmando que este é o Filho de Deus.
21 Ora, todos os que o ouviam estavam atônitos e diziam: Não é este o que exterminava em Jerusalém os que invocavam o nome de Jesus e para aqui veio precisamente com o fim de os levar amarrados aos principais sacerdotes?
22 Saulo, porém, mais e mais se fortalecia e confundia os judeus que moravam em Damasco, demonstrando que Jesus é o Cristo.
23 Decorridos muitos dias, os judeus deliberaram entre si tirar-lhe a vida;
24 porém o plano deles chegou ao conhecimento de Saulo. Dia e noite guardavam também as portas, para o matarem.
25 Mas os seus discípulos tomaram-no de noite e, colocando-o num cesto, desceram-no pela muralha.
26 Tendo chegado a Jerusalém, procurou juntar-se com os discípulos; todos, porém, o temiam, não acreditando que ele fosse discípulo.
27 Mas Barnabé, tomando-o consigo, levou-o aos apóstolos; e contou-lhes como ele vira o Senhor no caminho, e que este lhe falara, e como em Damasco pregara ousadamente em nome de Jesus.
28 Estava com eles em Jerusalém, entrando e saindo, pregando ousadamente em nome do Senhor.
29 Falava e discutia com os helenistas; mas eles procuravam tirar-lhe a vida.
30 Tendo, porém, isto chegado ao conhecimento dos irmãos, levaram-no até Cesareia e dali o enviaram para Tarso.
31 A igreja, na verdade, tinha paz por toda a Judeia, Galileia e Samaria, edificando-se e caminhando no temor do Senhor, e, no conforto do Espírito Santo, crescia em número.
32 Passando Pedro por toda parte, desceu também aos santos que habitavam em Lida.
33 Encontrou ali certo homem, chamado Eneias, que havia oito anos jazia de cama, pois era paralítico.
34 Disse-lhe Pedro: Eneias, Jesus Cristo te cura! Levanta-te e arruma o teu leito. Ele, imediatamente, se levantou.
35 Viram-no todos os habitantes de Lida e Sarona, os quais se converteram ao Senhor.
36 Havia em Jope uma discípula por nome Tabita, nome este que, traduzido, quer dizer Dorcas; era ela notável pelas boas obras e esmolas que fazia.
37 Ora, aconteceu, naqueles dias, que ela adoeceu e veio a morrer; e, depois de a lavarem, puseram-na no cenáculo.
38 Como Lida era perto de Jope, ouvindo os discípulos que Pedro estava ali, enviaram-lhe dois homens que lhe pedissem: Não demores em vir ter conosco.
39 Pedro atendeu e foi com eles. Tendo chegado, conduziram-no para o cenáculo; e todas as viúvas o cercaram, chorando e mostrando-lhe túnicas e vestidos que Dorcas fizera enquanto estava com elas.
40 Mas Pedro, tendo feito sair a todos, pondo-se de joelhos, orou; e, voltando-se para o corpo, disse: Tabita, levanta-te! Ela abriu os olhos e, vendo a Pedro, sentou-se.
41 Ele, dando-lhe a mão, levantou-a; e, chamando os santos, especialmente as viúvas, apresentou-a viva.
42 Isto se tornou conhecido por toda Jope, e muitos creram no Senhor.
43 Pedro ficou em Jope muitos dias, em casa de um curtidor chamado Simão.*
1 Morava em Cesareia um homem de nome Cornélio, centurião da coorte chamada Italiana,
2 piedoso e temente a Deus com toda a sua casa e que fazia muitas esmolas ao povo e, de contínuo, orava a Deus.
3 Esse homem observou claramente durante uma visão, cerca da hora nona do dia, um anjo de Deus que se aproximou dele e lhe disse:
4 Cornélio! Este, fixando nele os olhos e possuído de temor, perguntou: Que é, Senhor? E o anjo lhe disse: As tuas orações e as tuas esmolas subiram para memória diante de Deus.
5 Agora, envia mensageiros a Jope e manda chamar Simão, que tem por sobrenome Pedro.
6 Ele está hospedado com Simão, curtidor, cuja residência está situada à beira-mar.
7 Logo que se retirou o anjo que lhe falava, chamou dois dos seus domésticos e um soldado piedoso dos que estavam a seu serviço
8 e, havendo-lhes contado tudo, enviou-os a Jope.
9 No dia seguinte, indo eles de caminho e estando já perto da cidade, subiu Pedro ao eirado, por volta da hora sexta, a fim de orar.
10 Estando com fome, quis comer; mas, enquanto lhe preparavam a comida, sobreveio-lhe um êxtase;
11 então, viu o céu aberto e descendo um objeto como se fosse um grande lençol, o qual era baixado à terra pelas quatro pontas,
12 contendo toda sorte de quadrúpedes, répteis da terra e aves do céu.
13 E ouviu-se uma voz que se dirigia a ele: Levanta-te, Pedro! Mata e come.
14 Mas Pedro replicou: De modo nenhum, Senhor! Porque jamais comi coisa alguma comum e imunda.
15 Segunda vez, a voz lhe falou: Ao que Deus purificou não consideres comum.
16 Sucedeu isto por três vezes, e, logo, aquele objeto foi recolhido ao céu.
17 Enquanto Pedro estava perplexo sobre qual seria o significado da visão, eis que os homens enviados da parte de Cornélio, tendo perguntado pela casa de Simão, pararam junto à porta;
18 e, chamando, indagavam se estava ali hospedado Simão, por sobrenome Pedro.
19 Enquanto meditava Pedro acerca da visão, disse-lhe o Espírito: Estão aí dois homens que te procuram;
20 levanta-te, pois, desce e vai com eles, nada duvidando; porque eu os enviei.
21 E, descendo Pedro para junto dos homens, disse: Aqui me tendes; sou eu a quem buscais? A que viestes?
22 Então, disseram: O centurião Cornélio, homem reto e temente a Deus e tendo bom testemunho de toda a nação judaica, foi instruído por um santo anjo para chamar-te a sua casa e ouvir as tuas palavras.
23 Pedro, pois, convidando-os a entrar, hospedou-os. No dia seguinte, levantou-se e partiu com eles; também alguns irmãos dos que habitavam em Jope foram em sua companhia.
24 No dia imediato, entrou em Cesareia. Cornélio estava esperando por eles, tendo reunido seus parentes e amigos íntimos.
25 Aconteceu que, indo Pedro a entrar, lhe saiu Cornélio ao encontro e, prostrando-se-lhe aos pés, o adorou.
26 Mas Pedro o levantou, dizendo: Ergue-te, que eu também sou homem.
27 Falando com ele, entrou, encontrando muitos reunidos ali,
28 a quem se dirigiu, dizendo: Vós bem sabeis que é proibido a um judeu ajuntar-se ou mesmo aproximar-se a alguém de outra raça; mas Deus me demonstrou que a nenhum homem considerasse comum ou imundo;
29 por isso, uma vez chamado, vim sem vacilar. Pergunto, pois: por que razão me mandastes chamar?
30 Respondeu-lhe Cornélio: Faz, hoje, quatro dias que, por volta desta hora, estava eu observando em minha casa a hora nona de oração, e eis que se apresentou diante de mim um varão de vestes resplandecentes
31 e disse: Cornélio, a tua oração foi ouvida, e as tuas esmolas, lembradas na presença de Deus.
32 Manda, pois, alguém a Jope a chamar Simão, por sobrenome Pedro; acha-se este hospedado em casa de Simão, curtidor, à beira-mar.
33 Portanto, sem demora, mandei chamar-te, e fizeste bem em vir. Agora, pois, estamos todos aqui, na presença de Deus, prontos para ouvir tudo o que te foi ordenado da parte do Senhor.
34 Então, falou Pedro, dizendo: Reconheço, por verdade, que Deus não faz acepção de pessoas;
35 pelo contrário, em qualquer nação, aquele que o teme e faz o que é justo lhe é aceitável.
36 Esta é a palavra que Deus enviou aos filhos de Israel, anunciando-lhes o evangelho da paz, por meio de Jesus Cristo. Este é o Senhor de todos.
37 Vós conheceis a palavra que se divulgou por toda a Judeia, tendo começado desde a Galileia, depois do batismo que João pregou,
38 como Deus ungiu a Jesus de Nazaré com o Espírito Santo e com poder, o qual andou por toda parte, fazendo o bem e curando a todos os oprimidos do diabo, porque Deus era com ele;
39 e nós somos testemunhas de tudo o que ele fez na terra dos judeus e em Jerusalém; ao qual também tiraram a vida, pendurando-o no madeiro.
40 A este ressuscitou Deus no terceiro dia e concedeu que fosse manifesto,
41 não a todo o povo, mas às testemunhas que foram anteriormente escolhidas por Deus, isto é, a nós que comemos e bebemos com ele, depois que ressurgiu dentre os mortos;
42 e nos mandou pregar ao povo e testificar que ele é quem foi constituído por Deus Juiz de vivos e de mortos.
43 Dele todos os profetas dão testemunho de que, por meio de seu nome, todo aquele que nele crê recebe remissão de pecados.
44 Ainda Pedro falava estas coisas quando caiu o Espírito Santo sobre todos os que ouviam a palavra.
45 E os fiéis que eram da circuncisão, que vieram com Pedro, admiraram-se, porque também sobre os gentios foi derramado o dom do Espírito Santo;
46 pois os ouviam falando em línguas e engrandecendo a Deus. Então, perguntou Pedro:
47 Porventura, pode alguém recusar a água, para que não sejam batizados estes que, assim como nós, receberam o Espírito Santo?
48 E ordenou que fossem batizados em nome de Jesus Cristo. Então, lhe pediram que permanecesse com eles por alguns dias.*
1 Chegou ao conhecimento dos apóstolos e dos irmãos que estavam na Judeia que também os gentios haviam recebido a palavra de Deus.
2 Quando Pedro subiu a Jerusalém, os que eram da circuncisão o arguiram, dizendo:
3 Entraste em casa de homens incircuncisos e comeste com eles.
4 Então, Pedro passou a fazer-lhes uma exposição por ordem, dizendo:
5 Eu estava na cidade de Jope orando e, num êxtase, tive uma visão em que observei descer um objeto como se fosse um grande lençol baixado do céu pelas quatro pontas e vindo até perto de mim.
6 E, fitando para dentro dele os olhos, vi quadrúpedes da terra, feras, répteis e aves do céu.
7 Ouvi também uma voz que me dizia: Levanta-te, Pedro! Mata e come.
8 Ao que eu respondi: de modo nenhum, Senhor; porque jamais entrou em minha boca qualquer coisa comum ou imunda.
9 Segunda vez, falou a voz do céu: Ao que Deus purificou não consideres comum.
10 Isto sucedeu por três vezes, e, de novo, tudo se recolheu para o céu.
11 E eis que, na mesma hora, pararam junto da casa em que estávamos três homens enviados de Cesareia para se encontrarem comigo.
12 Então, o Espírito me disse que eu fosse com eles, sem hesitar. Foram comigo também estes seis irmãos; e entramos na casa daquele homem.
13 E ele nos contou como vira o anjo em pé em sua casa e que lhe dissera: Envia a Jope e manda chamar Simão, por sobrenome Pedro,
14 o qual te dirá palavras mediante as quais serás salvo, tu e toda a tua casa.
15 Quando, porém, comecei a falar, caiu o Espírito Santo sobre eles, como também sobre nós, no princípio.
16 Então, me lembrei da palavra do Senhor, quando disse: João, na verdade, batizou com água, mas vós sereis batizados com o Espírito Santo.
17 Pois, se Deus lhes concedeu o mesmo dom que a nós nos outorgou quando cremos no Senhor Jesus, quem era eu para que pudesse resistir a Deus?
18 E, ouvindo eles estas coisas, apaziguaram-se e glorificaram a Deus, dizendo: Logo, também aos gentios foi por Deus concedido o arrependimento para vida.
19 Então, os que foram dispersos por causa da tribulação que sobreveio a Estêvão se espalharam até à Fenícia, Chipre e Antioquia, não anunciando a ninguém a palavra, senão somente aos judeus.
20 Alguns deles, porém, que eram de Chipre e de Cirene e que foram até Antioquia, falavam também aos gregos, anunciando-lhes o evangelho do Senhor Jesus.
21 A mão do Senhor estava com eles, e muitos, crendo, se converteram ao Senhor.
22 A notícia a respeito deles chegou aos ouvidos da igreja que estava em Jerusalém; e enviaram Barnabé até Antioquia.
23 Tendo ele chegado e, vendo a graça de Deus, alegrou-se e exortava a todos a que, com firmeza de coração, permanecessem no Senhor.
24 Porque era homem bom, cheio do Espírito Santo e de fé. E muita gente se uniu ao Senhor.
25 E partiu Barnabé para Tarso à procura de Saulo;
26 tendo-o encontrado, levou-o para Antioquia. E, por todo um ano, se reuniram naquela igreja e ensinaram numerosa multidão. Em Antioquia, foram os discípulos, pela primeira vez, chamados cristãos.
27 Naqueles dias, desceram alguns profetas de Jerusalém para Antioquia,
28 e, apresentando-se um deles, chamado Ágabo, dava a entender, pelo Espírito, que estava para vir grande fome por todo o mundo, a qual sobreveio nos dias de Cláudio.
29 Os discípulos, cada um conforme as suas posses, resolveram enviar socorro aos irmãos que moravam na Judeia;
30 o que eles, com efeito, fizeram, enviando-o aos presbíteros por intermédio de Barnabé e de Saulo.*
1 Por aquele tempo, mandou o rei Herodes prender alguns da igreja para os maltratar,
2 fazendo passar a fio de espada a Tiago, irmão de João.
3 Vendo ser isto agradável aos judeus, prosseguiu, prendendo também a Pedro. E eram os dias dos pães asmos.
4 Tendo-o feito prender, lançou-o no cárcere, entregando-o a quatro escoltas de quatro soldados cada uma, para o guardarem, tencionando apresentá-lo ao povo depois da Páscoa.
5 Pedro, pois, estava guardado no cárcere; mas havia oração incessante a Deus por parte da igreja a favor dele.
6 Quando Herodes estava para apresentá-lo, naquela mesma noite, Pedro dormia entre dois soldados, acorrentado com duas cadeias, e sentinelas à porta guardavam o cárcere.
7 Eis, porém, que sobreveio um anjo do Senhor, e uma luz iluminou a prisão; e, tocando ele o lado de Pedro, o despertou, dizendo: Levanta-te depressa! Então, as cadeias caíram-lhe das mãos.
8 Disse-lhe o anjo: Cinge-te e calça as sandálias. E ele assim o fez. Disse-lhe mais: Põe a capa e segue-me.
9 Então, saindo, o seguia, não sabendo que era real o que se fazia por meio do anjo; parecia-lhe, antes, uma visão.
10 Depois de terem passado a primeira e a segunda sentinela, chegaram ao portão de ferro que dava para a cidade, o qual se lhes abriu automaticamente; e, saindo, enveredaram por uma rua, e logo adiante o anjo se apartou dele.
11 Então, Pedro, caindo em si, disse: Agora, sei, verdadeiramente, que o Senhor enviou o seu anjo e me livrou da mão de Herodes e de toda a expectativa do povo judaico.
12 Considerando ele a sua situação, resolveu ir à casa de Maria, mãe de João, cognominado Marcos, onde muitas pessoas estavam congregadas e oravam.
13 Quando ele bateu ao postigo do portão, veio uma criada, chamada Rode, ver quem era;
14 reconhecendo a voz de Pedro, tão alegre ficou, que nem o fez entrar, mas voltou correndo para anunciar que Pedro estava junto do portão.
15 Eles lhe disseram: Estás louca. Ela, porém, persistia em afirmar que assim era. Então, disseram: É o seu anjo.
16 Entretanto, Pedro continuava batendo; então, eles abriram, viram-no e ficaram atônitos.
17 Ele, porém, fazendo-lhes sinal com a mão para que se calassem, contou-lhes como o Senhor o tirara da prisão e acrescentou: Anunciai isto a Tiago e aos irmãos. E, saindo, retirou-se para outro lugar.
18 Sendo já dia, houve não pouco alvoroço entre os soldados sobre o que teria acontecido a Pedro.
19 Herodes, tendo-o procurado e não o achando, submetendo as sentinelas a inquérito, ordenou que fossem justiçadas. E, descendo da Judeia para Cesareia, Herodes passou ali algum tempo.
20 Ora, havia séria divergência entre Herodes e os habitantes de Tiro e de Sidom; porém estes, de comum acordo, se apresentaram a ele e, depois de alcançar o favor de Blasto, camarista do rei, pediram reconciliação, porque a sua terra se abastecia do país do rei.
21 Em dia designado, Herodes, vestido de trajo real, assentado no trono, dirigiu-lhes a palavra;
22 e o povo clamava: É voz de um deus, e não de homem!
23 No mesmo instante, um anjo do Senhor o feriu, por ele não haver dado glória a Deus; e, comido de vermes, expirou.
24 Entretanto, a palavra do Senhor crescia e se multiplicava.
25 Barnabé e Saulo, cumprida a sua missão, voltaram de Jerusalém, levando também consigo a João, apelidado Marcos.*
1 Havia na igreja de Antioquia profetas e mestres: Barnabé, Simeão, por sobrenome Níger, Lúcio de Cirene, Manaém, colaço de Herodes, o tetrarca, e Saulo.
2 E, servindo eles ao Senhor e jejuando, disse o Espírito Santo: Separai-me, agora, Barnabé e Saulo para a obra a que os tenho chamado.
3 Então, jejuando, e orando, e impondo sobre eles as mãos, os despediram.
4 Enviados, pois, pelo Espírito Santo, desceram a Selêucia e dali navegaram para Chipre.
5 Chegados a Salamina, anunciavam a palavra de Deus nas sinagogas judaicas; tinham também João como auxiliar.
6 Havendo atravessado toda a ilha até Pafos, encontraram certo judeu, mágico, falso profeta, de nome Barjesus,
7 o qual estava com o procônsul Sérgio Paulo, que era homem inteligente. Este, tendo chamado Barnabé e Saulo, diligenciava para ouvir a palavra de Deus.
8 Mas opunha-se-lhes Elimas, o mágico (porque assim se interpreta o seu nome), procurando afastar da fé o procônsul.
9 Todavia, Saulo, também chamado Paulo, cheio do Espírito Santo, fixando nele os olhos, disse:
10 Ó filho do diabo, cheio de todo o engano e de toda a malícia, inimigo de toda a justiça, não cessarás de perverter os retos caminhos do Senhor?
11 Pois, agora, eis aí está sobre ti a mão do Senhor, e ficarás cego, não vendo o sol por algum tempo. No mesmo instante, caiu sobre ele névoa e escuridade, e, andando à roda, procurava quem o guiasse pela mão.
12 Então, o procônsul, vendo o que sucedera, creu, maravilhado com a doutrina do Senhor.
13 E, navegando de Pafos, Paulo e seus companheiros dirigiram-se a Perge da Panfília. João, porém, apartando-se deles, voltou para Jerusalém.
14 Mas eles, atravessando de Perge para a Antioquia da Pisídia, indo num sábado à sinagoga, assentaram-se.
15 Depois da leitura da lei e dos profetas, os chefes da sinagoga mandaram dizer-lhes: Irmãos, se tendes alguma palavra de exortação para o povo, dizei-a.
16 Paulo, levantando-se e fazendo com a mão sinal de silêncio, disse: Varões israelitas e vós outros que também temeis a Deus, ouvi.
17 O Deus deste povo de Israel escolheu nossos pais e exaltou o povo durante sua peregrinação na terra do Egito, donde os tirou com braço poderoso;
18 e suportou-lhes os maus costumes por cerca de quarenta anos no deserto;
19 e, havendo destruído sete nações na terra de Canaã, deu-lhes essa terra por herança,
20 vencidos cerca de quatrocentos e cinquenta anos. Depois disto, lhes deu juízes, até o profeta Samuel.
21 Então, eles pediram um rei, e Deus lhes deparou Saul, filho de Quis, da tribo de Benjamim, e isto pelo espaço de quarenta anos.
22 E, tendo tirado a este, levantou-lhes o rei Davi, do qual também, dando testemunho, disse: Achei Davi, filho de Jessé, homem segundo o meu coração, que fará toda a minha vontade.
23 Da descendência deste, conforme a promessa, trouxe Deus a Israel o Salvador, que é Jesus,
24 havendo João, primeiro, pregado a todo o povo de Israel, antes da manifestação dele, batismo de arrependimento.
25 Mas, ao completar João a sua carreira, dizia: Não sou quem supondes; mas após mim vem aquele de cujos pés não sou digno de desatar as sandálias.
26 Irmãos, descendência de Abraão e vós outros os que temeis a Deus, a nós nos foi enviada a palavra desta salvação.
27 Pois os que habitavam em Jerusalém e as suas autoridades, não conhecendo Jesus nem os ensinos dos profetas que se leem todos os sábados, quando o condenaram, cumpriram as profecias;
28 e, embora não achassem nenhuma causa de morte, pediram a Pilatos que ele fosse morto.
29 Depois de cumprirem tudo o que a respeito dele estava escrito, tirando-o do madeiro, puseram-no em um túmulo.
30 Mas Deus o ressuscitou dentre os mortos;
31 e foi visto muitos dias pelos que, com ele, subiram da Galileia para Jerusalém, os quais são agora as suas testemunhas perante o povo.
32 Nós vos anunciamos o evangelho da promessa feita a nossos pais,
33 como Deus a cumpriu plenamente a nós, seus filhos, ressuscitando a Jesus, como também está escrito no Salmo segundo: Tu és meu Filho, eu, hoje, te gerei.
34 E, que Deus o ressuscitou dentre os mortos para que jamais voltasse à corrupção, desta maneira o disse: E cumprirei a vosso favor as santas e fiéis promessas feitas a Davi.
35 Por isso, também diz em outro Salmo: Não permitirás que o teu Santo veja corrupção.
36 Porque, na verdade, tendo Davi servido à sua própria geração, conforme o desígnio de Deus, adormeceu, foi para junto de seus pais e viu corrupção.
37 Porém aquele a quem Deus ressuscitou não viu corrupção.
38 Tomai, pois, irmãos, conhecimento de que se vos anuncia remissão de pecados por intermédio deste;
39 e, por meio dele, todo o que crê é justificado de todas as coisas das quais vós não pudestes ser justificados pela lei de Moisés.
40 Notai, pois, que não vos sobrevenha o que está dito nos profetas:
41 Vede, ó desprezadores, maravilhai-vos e desvanecei, porque eu realizo, em vossos dias, obra tal que não crereis se alguém vo-la contar.
42 Ao saírem eles, rogaram-lhes que, no sábado seguinte, lhes falassem estas mesmas palavras.
43 Despedida a sinagoga, muitos dos judeus e dos prosélitos piedosos seguiram Paulo e Barnabé, e estes, falando-lhes, os persuadiam a perseverar na graça de Deus.
44 No sábado seguinte, afluiu quase toda a cidade para ouvir a palavra de Deus.
45 Mas os judeus, vendo as multidões, tomaram-se de inveja e, blasfemando, contradiziam o que Paulo falava.
46 Então, Paulo e Barnabé, falando ousadamente, disseram: Cumpria que a vós outros, em primeiro lugar, fosse pregada a palavra de Deus; mas, posto que a rejeitais e a vós mesmos vos julgais indignos da vida eterna, eis aí que nos volvemos para os gentios.
47 Porque o Senhor assim no-lo determinou: Eu te constituí para luz dos gentios, a fim de que sejas para salvação até aos confins da terra.
48 Os gentios, ouvindo isto, regozijavam-se e glorificavam a palavra do Senhor, e creram todos os que haviam sido destinados para a vida eterna.
49 E divulgava-se a palavra do Senhor por toda aquela região.
50 Mas os judeus instigaram as mulheres piedosas de alta posição e os principais da cidade e levantaram perseguição contra Paulo e Barnabé, expulsando-os do seu território.
51 E estes, sacudindo contra aqueles o pó dos pés, partiram para Icônio.
52 Os discípulos, porém, transbordavam de alegria e do Espírito Santo.*
1 Em Icônio, Paulo e Barnabé entraram juntos na sinagoga judaica e falaram de tal modo, que veio a crer grande multidão, tanto de judeus como de gregos.
2 Mas os judeus incrédulos incitaram e irritaram os ânimos dos gentios contra os irmãos.
3 Entretanto, demoraram-se ali muito tempo, falando ousadamente no Senhor, o qual confirmava a palavra da sua graça, concedendo que, por mão deles, se fizessem sinais e prodígios.
4 Mas dividiu-se o povo da cidade: uns eram pelos judeus; outros, pelos apóstolos.
5 E, como surgisse um tumulto dos gentios e judeus, associados com as suas autoridades, para os ultrajar e apedrejar,
6 sabendo-o eles, fugiram para Listra e Derbe, cidades da Licaônia e circunvizinhança,
7 onde anunciaram o evangelho.
8 Em Listra, costumava estar assentado certo homem aleijado, paralítico desde o seu nascimento, o qual jamais pudera andar.
9 Esse homem ouviu falar Paulo, que, fixando nele os olhos e vendo que possuía fé para ser curado,
10 disse-lhe em alta voz: Apruma-te direito sobre os pés! Ele saltou e andava.
11 Quando as multidões viram o que Paulo fizera, gritaram em língua licaônica, dizendo: Os deuses, em forma de homens, baixaram até nós.
12 A Barnabé chamavam Júpiter, e a Paulo, Mercúrio, porque era este o principal portador da palavra.
13 O sacerdote de Júpiter, cujo templo estava em frente da cidade, trazendo para junto das portas touros e grinaldas, queria sacrificar juntamente com as multidões.
14 Porém, ouvindo isto, os apóstolos Barnabé e Paulo, rasgando as suas vestes, saltaram para o meio da multidão, clamando:
15 Senhores, por que fazeis isto? Nós também somos homens como vós, sujeitos aos mesmos sentimentos, e vos anunciamos o evangelho para que destas coisas vãs vos convertais ao Deus vivo, que fez o céu, a terra, o mar e tudo o que há neles;
16 o qual, nas gerações passadas, permitiu que todos os povos andassem nos seus próprios caminhos;
17 contudo, não se deixou ficar sem testemunho de si mesmo, fazendo o bem, dando-vos do céu chuvas e estações frutíferas, enchendo o vosso coração de fartura e de alegria.
18 Dizendo isto, foi ainda com dificuldade que impediram as multidões de lhes oferecerem sacrifícios.
19 Sobrevieram, porém, judeus de Antioquia e Icônio e, instigando as multidões e apedrejando a Paulo, arrastaram-no para fora da cidade, dando-o por morto.
20 Rodeando-o, porém, os discípulos, levantou-se e entrou na cidade. No dia seguinte, partiu, com Barnabé, para Derbe.
21 E, tendo anunciado o evangelho naquela cidade e feito muitos discípulos, voltaram para Listra, e Icônio, e Antioquia,
22 fortalecendo a alma dos discípulos, exortando-os a permanecer firmes na fé; e mostrando que, através de muitas tribulações, nos importa entrar no reino de Deus.
23 E, promovendo-lhes, em cada igreja, a eleição de presbíteros, depois de orar com jejuns, os encomendaram ao Senhor em quem haviam crido.
24 Atravessando a Pisídia, dirigiram-se a Panfília.
25 E, tendo anunciado a palavra em Perge, desceram a Atália
26 e dali navegaram para Antioquia, onde tinham sido recomendados à graça de Deus para a obra que haviam já cumprido.
27 Ali chegados, reunida a igreja, relataram quantas coisas fizera Deus com eles e como abrira aos gentios a porta da fé.
28 E permaneceram não pouco tempo com os discípulos.*
1 Alguns indivíduos que desceram da Judeia ensinavam aos irmãos: Se não vos circuncidardes segundo o costume de Moisés, não podeis ser salvos.
2 Tendo havido, da parte de Paulo e Barnabé, contenda e não pequena discussão com eles, resolveram que esses dois e alguns outros dentre eles subissem a Jerusalém, aos apóstolos e presbíteros, com respeito a esta questão.
3 Enviados, pois, e até certo ponto acompanhados pela igreja, atravessaram as províncias da Fenícia e Samaria e, narrando a conversão dos gentios, causaram grande alegria a todos os irmãos.
4 Tendo eles chegado a Jerusalém, foram bem-recebidos pela igreja, pelos apóstolos e pelos presbíteros e relataram tudo o que Deus fizera com eles.
5 Insurgiram-se, entretanto, alguns da seita dos fariseus que haviam crido, dizendo: É necessário circuncidá-los e determinar-lhes que observem a lei de Moisés.
6 Então, se reuniram os apóstolos e os presbíteros para examinar a questão.
7 Havendo grande debate, Pedro tomou a palavra e lhes disse: Irmãos, vós sabeis que, desde há muito, Deus me escolheu dentre vós para que, por meu intermédio, ouvissem os gentios a palavra do evangelho e cressem.
8 Ora, Deus, que conhece os corações, lhes deu testemunho, concedendo o Espírito Santo a eles, como também a nós nos concedera.
9 E não estabeleceu distinção alguma entre nós e eles, purificando-lhes pela fé o coração.
10 Agora, pois, por que tentais a Deus, pondo sobre a cerviz dos discípulos um jugo que nem nossos pais puderam suportar, nem nós?
11 Mas cremos que fomos salvos pela graça do Senhor Jesus, como também aqueles o foram.
12 E toda a multidão silenciou, passando a ouvir a Barnabé e a Paulo, que contavam quantos sinais e prodígios Deus fizera por meio deles entre os gentios.
13 Depois que eles terminaram, falou Tiago, dizendo: Irmãos, atentai nas minhas palavras:
14 expôs Simão como Deus, primeiramente, visitou os gentios, a fim de constituir dentre eles um povo para o seu nome.
15 Conferem com isto as palavras dos profetas, como está escrito:
16 Cumpridas estas coisas, voltarei e reedificarei o tabernáculo caído de Davi; e, levantando-o de suas ruínas, restaurá-lo-ei.
17 Para que os demais homens busquem o Senhor, e também todos os gentios sobre os quais tem sido invocado o meu nome,
18 diz o Senhor, que faz estas coisas conhecidas desde séculos.
19 Pelo que, julgo eu, não devemos perturbar aqueles que, dentre os gentios, se convertem a Deus,
20 mas escrever-lhes que se abstenham das contaminações dos ídolos, bem como das relações sexuais ilícitas, da carne de animais sufocados e do sangue.
21 Porque Moisés tem, em cada cidade, desde tempos antigos, os que o pregam nas sinagogas, onde é lido todos os sábados.
22 Então, pareceu bem aos apóstolos e aos presbíteros, com toda a igreja, tendo elegido homens dentre eles, enviá-los, juntamente com Paulo e Barnabé, a Antioquia: foram Judas, chamado Barsabás, e Silas, homens notáveis entre os irmãos,
23 escrevendo, por mão deles: Os irmãos, tanto os apóstolos como os presbíteros, aos irmãos de entre os gentios em Antioquia, Síria e Cilícia, saudações.
24 Visto sabermos que alguns [que saíram] de entre nós, sem nenhuma autorização, vos têm perturbado com palavras, transtornando a vossa alma,
25 pareceu-nos bem, chegados a pleno acordo, eleger alguns homens e enviá-los a vós outros com os nossos amados Barnabé e Paulo,
26 homens que têm exposto a vida pelo nome de nosso Senhor Jesus Cristo.
27 Enviamos, portanto, Judas e Silas, os quais pessoalmente vos dirão também estas coisas.
28 Pois pareceu bem ao Espírito Santo e a nós não vos impor maior encargo além destas coisas essenciais:
29 que vos abstenhais das coisas sacrificadas a ídolos, bem como do sangue, da carne de animais sufocados e das relações sexuais ilícitas; destas coisas fareis bem se vos guardardes. Saúde.
30 Os que foram enviados desceram logo para Antioquia e, tendo reunido a comunidade, entregaram a epístola.
31 Quando a leram, sobremaneira se alegraram pelo conforto recebido.
32 Judas e Silas, que eram também profetas, consolaram os irmãos com muitos conselhos e os fortaleceram.
33 Tendo-se demorado ali por algum tempo, os irmãos os deixaram voltar em paz aos que os enviaram.
34 [Mas pareceu bem a Silas permanecer ali.]
35 Paulo e Barnabé demoraram-se em Antioquia, ensinando e pregando, com muitos outros, a palavra do Senhor.
36 Alguns dias depois, disse Paulo a Barnabé: Voltemos, agora, para visitar os irmãos por todas as cidades nas quais anunciamos a palavra do Senhor, para ver como passam.
37 E Barnabé queria levar também a João, chamado Marcos.
38 Mas Paulo não achava justo levarem aquele que se afastara desde a Panfília, não os acompanhando no trabalho.
39 Houve entre eles tal desavença, que vieram a separar-se. Então, Barnabé, levando consigo a Marcos, navegou para Chipre.
40 Mas Paulo, tendo escolhido a Silas, partiu encomendado pelos irmãos à graça do Senhor.
41 E passou pela Síria e Cilícia, confirmando as igrejas.*
1 Chegou também a Derbe e a Listra. Havia ali um discípulo chamado Timóteo, filho de uma judia crente, mas de pai grego;
2 dele davam bom testemunho os irmãos em Listra e Icônio.
3 Quis Paulo que ele fosse em sua companhia e, por isso, circuncidou-o por causa dos judeus daqueles lugares; pois todos sabiam que seu pai era grego.
4 Ao passar pelas cidades, entregavam aos irmãos, para que as observassem, as decisões tomadas pelos apóstolos e presbíteros de Jerusalém.
5 Assim, as igrejas eram fortalecidas na fé e, dia a dia, aumentavam em número.
6 E, percorrendo a região frígio-gálata, tendo sido impedidos pelo Espírito Santo de pregar a palavra na Ásia,
7 defrontando Mísia, tentavam ir para Bitínia, mas o Espírito de Jesus não o permitiu.
8 E, tendo contornado Mísia, desceram a Trôade.
9 À noite, sobreveio a Paulo uma visão na qual um varão macedônio estava em pé e lhe rogava, dizendo: Passa à Macedônia e ajuda-nos.
10 Assim que teve a visão, imediatamente, procuramos partir para aquele destino, concluindo que Deus nos havia chamado para lhes anunciar o evangelho.
11 Tendo, pois, navegado de Trôade, seguimos em direitura a Samotrácia, no dia seguinte, a Neápolis
12 e dali, a Filipos, cidade da Macedônia, primeira do distrito e colônia. Nesta cidade, permanecemos alguns dias.
13 No sábado, saímos da cidade para junto do rio, onde nos pareceu haver um lugar de oração; e, assentando-nos, falamos às mulheres que para ali tinham concorrido.
14 Certa mulher, chamada Lídia, da cidade de Tiatira, vendedora de púrpura, temente a Deus, nos escutava; o Senhor lhe abriu o coração para atender às coisas que Paulo dizia.
15 Depois de ser batizada, ela e toda a sua casa, nos rogou, dizendo: Se julgais que eu sou fiel ao Senhor, entrai em minha casa e aí ficai. E nos constrangeu a isso.
16 Aconteceu que, indo nós para o lugar de oração, nos saiu ao encontro uma jovem possessa de espírito adivinhador, a qual, adivinhando, dava grande lucro aos seus senhores.
17 Seguindo a Paulo e a nós, clamava, dizendo: Estes homens são servos do Deus Altíssimo e vos anunciam o caminho da salvação.
18 Isto se repetia por muitos dias. Então, Paulo, já indignado, voltando-se, disse ao espírito: Em nome de Jesus Cristo, eu te mando: retira-te dela. E ele, na mesma hora, saiu.
19 Vendo os seus senhores que se lhes desfizera a esperança do lucro, agarrando em Paulo e Silas, os arrastaram para a praça, à presença das autoridades;
20 e, levando-os aos pretores, disseram: Estes homens, sendo judeus, perturbam a nossa cidade,
21 propagando costumes que não podemos receber, nem praticar, porque somos romanos.
22 Levantou-se a multidão, unida contra eles, e os pretores, rasgando-lhes as vestes, mandaram açoitá-los com varas.
23 E, depois de lhes darem muitos açoites, os lançaram no cárcere, ordenando ao carcereiro que os guardasse com toda a segurança.
24 Este, recebendo tal ordem, levou-os para o cárcere interior e lhes prendeu os pés no tronco.
25 Por volta da meia-noite, Paulo e Silas oravam e cantavam louvores a Deus, e os demais companheiros de prisão escutavam.
26 De repente, sobreveio tamanho terremoto, que sacudiu os alicerces da prisão; abriram-se todas as portas, e soltaram-se as cadeias de todos.
27 O carcereiro despertou do sono e, vendo abertas as portas do cárcere, puxando da espada, ia suicidar-se, supondo que os presos tivessem fugido.
28 Mas Paulo bradou em alta voz: Não te faças nenhum mal, que todos aqui estamos!
29 Então, o carcereiro, tendo pedido uma luz, entrou precipitadamente e, trêmulo, prostrou-se diante de Paulo e Silas.
30 Depois, trazendo-os para fora, disse: Senhores, que devo fazer para que seja salvo?
31 Responderam-lhe: Crê no Senhor Jesus e serás salvo, tu e tua casa.
32 E lhe pregaram a palavra de Deus e a todos os de sua casa.
33 Naquela mesma hora da noite, cuidando deles, lavou-lhes os vergões dos açoites. A seguir, foi ele batizado, e todos os seus.
34 Então, levando-os para a sua própria casa, lhes pôs a mesa; e, com todos os seus, manifestava grande alegria, por terem crido em Deus.
35 Quando amanheceu, os pretores enviaram oficiais de justiça, com a seguinte ordem: Põe aqueles homens em liberdade.
36 Então, o carcereiro comunicou a Paulo estas palavras: Os pretores ordenaram que fôsseis postos em liberdade. Agora, pois, saí e ide em paz.
37 Paulo, porém, lhes replicou: Sem ter havido processo formal contra nós, nos açoitaram publicamente e nos recolheram ao cárcere, sendo nós cidadãos romanos; querem agora, às ocultas, lançar-nos fora? Não será assim; pelo contrário, venham eles e, pessoalmente, nos ponham em liberdade.
38 Os oficiais de justiça comunicaram isso aos pretores; e estes ficaram possuídos de temor, quando souberam que se tratava de cidadãos romanos.
39 Então, foram ter com eles e lhes pediram desculpas; e, relaxando-lhes a prisão, rogaram que se retirassem da cidade.
40 Tendo-se retirado do cárcere, dirigiram-se para a casa de Lídia e, vendo os irmãos, os confortaram. Então, partiram.*
1 Tendo passado por Anfípolis e Apolônia, chegaram a Tessalônica, onde havia uma sinagoga de judeus.
2 Paulo, segundo o seu costume, foi procurá-los e, por três sábados, arrazoou com eles acerca das Escrituras,
3 expondo e demonstrando ter sido necessário que o Cristo padecesse e ressurgisse dentre os mortos; e este, dizia ele, é o Cristo, Jesus, que eu vos anuncio.
4 Alguns deles foram persuadidos e unidos a Paulo e Silas, bem como numerosa multidão de gregos piedosos e muitas distintas mulheres.
5 Os judeus, porém, movidos de inveja, trazendo consigo alguns homens maus dentre a malandragem, ajuntando a turba, alvoroçaram a cidade e, assaltando a casa de Jasom, procuravam trazê-los para o meio do povo.
6 Porém, não os encontrando, arrastaram Jasom e alguns irmãos perante as autoridades, clamando: Estes que têm transtornado o mundo chegaram também aqui,
7 os quais Jasom hospedou. Todos estes procedem contra os decretos de César, afirmando ser Jesus outro rei.
8 Tanto a multidão como as autoridades ficaram agitadas ao ouvirem estas palavras;
9 contudo, soltaram Jasom e os mais, após terem recebido deles a fiança estipulada.
10 E logo, durante a noite, os irmãos enviaram Paulo e Silas para Bereia; ali chegados, dirigiram-se à sinagoga dos judeus.
11 Ora, estes de Bereia eram mais nobres que os de Tessalônica; pois receberam a palavra com toda a avidez, examinando as Escrituras todos os dias para ver se as coisas eram, de fato, assim.
12 Com isso, muitos deles creram, mulheres gregas de alta posição e não poucos homens.
13 Mas, logo que os judeus de Tessalônica souberam que a palavra de Deus era anunciada por Paulo também em Bereia, foram lá excitar e perturbar o povo.
14 Então, os irmãos promoveram, sem detença, a partida de Paulo para os lados do mar. Porém Silas e Timóteo continuaram ali.
15 Os responsáveis por Paulo levaram-no até Atenas e regressaram trazendo ordem a Silas e Timóteo para que, o mais depressa possível, fossem ter com ele.
16 Enquanto Paulo os esperava em Atenas, o seu espírito se revoltava em face da idolatria dominante na cidade.
17 Por isso, dissertava na sinagoga entre os judeus e os gentios piedosos; também na praça, todos os dias, entre os que se encontravam ali.
18 E alguns dos filósofos epicureus e estoicos contendiam com ele, havendo quem perguntasse: Que quer dizer esse tagarela? E outros: Parece pregador de estranhos deuses; pois pregava a Jesus e a ressurreição.
19 Então, tomando-o consigo, o levaram ao Areópago, dizendo: Poderemos saber que nova doutrina é essa que ensinas?
20 Posto que nos trazes aos ouvidos coisas estranhas, queremos saber o que vem a ser isso.
21 Pois todos os de Atenas e os estrangeiros residentes de outra coisa não cuidavam senão dizer ou ouvir as últimas novidades.
22 Então, Paulo, levantando-se no meio do Areópago, disse: Senhores atenienses! Em tudo vos vejo acentuadamente religiosos;
23 porque, passando e observando os objetos de vosso culto, encontrei também um altar no qual está inscrito: Ao Deus Desconhecido. Pois esse que adorais sem conhecer é precisamente aquele que eu vos anuncio.
24 O Deus que fez o mundo e tudo o que nele existe, sendo ele Senhor do céu e da terra, não habita em santuários feitos por mãos humanas.
25 Nem é servido por mãos humanas, como se de alguma coisa precisasse; pois ele mesmo é quem a todos dá vida, respiração e tudo mais;
26 de um só fez toda a raça humana para habitar sobre toda a face da terra, havendo fixado os tempos previamente estabelecidos e os limites da sua habitação;
27 para buscarem a Deus se, porventura, tateando, o possam achar, bem que não está longe de cada um de nós;
28 pois nele vivemos, e nos movemos, e existimos, como alguns dos vossos poetas têm dito: Porque dele também somos geração.
29 Sendo, pois, geração de Deus, não devemos pensar que a divindade é semelhante ao ouro, à prata ou à pedra, trabalhados pela arte e imaginação do homem.
30 Ora, não levou Deus em conta os tempos da ignorância; agora, porém, notifica aos homens que todos, em toda parte, se arrependam;
31 porquanto estabeleceu um dia em que há de julgar o mundo com justiça, por meio de um varão que destinou e acreditou diante de todos, ressuscitando-o dentre os mortos.
32 Quando ouviram falar de ressurreição de mortos, uns escarneceram, e outros disseram: A respeito disso te ouviremos noutra ocasião.
33 A essa altura, Paulo se retirou do meio deles.
34 Houve, porém, alguns homens que se agregaram a ele e creram; entre eles estava Dionísio, o areopagita, uma mulher chamada Dâmaris e, com eles, outros mais.*
1 Depois disto, deixando Paulo Atenas, partiu para Corinto.
2 Lá, encontrou certo judeu chamado Áquila, natural do Ponto, recentemente chegado da Itália, com Priscila, sua mulher, em vista de ter Cláudio decretado que todos os judeus se retirassem de Roma. Paulo aproximou-se deles.
3 E, posto que eram do mesmo ofício, passou a morar com eles e ali trabalhava, pois a profissão deles era fazer tendas.
4 E todos os sábados discorria na sinagoga, persuadindo tanto judeus como gregos.
5 Quando Silas e Timóteo desceram da Macedônia, Paulo se entregou totalmente à palavra, testemunhando aos judeus que o Cristo é Jesus.
6 Opondo-se eles e blasfemando, sacudiu Paulo as vestes e disse-lhes: Sobre a vossa cabeça, o vosso sangue! Eu dele estou limpo e, desde agora, vou para os gentios.
7 Saindo dali, entrou na casa de um homem chamado Tício Justo, que era temente a Deus; a casa era contígua à sinagoga.
8 Mas Crispo, o principal da sinagoga, creu no Senhor, com toda a sua casa; também muitos dos coríntios, ouvindo, criam e eram batizados.
9 Teve Paulo durante a noite uma visão em que o Senhor lhe disse: Não temas; pelo contrário, fala e não te cales;
10 porquanto eu estou contigo, e ninguém ousará fazer-te mal, pois tenho muito povo nesta cidade.
11 E ali permaneceu um ano e seis meses, ensinando entre eles a palavra de Deus.
12 Quando, porém, Gálio era procônsul da Acaia, levantaram-se os judeus, concordemente, contra Paulo e o levaram ao tribunal,
13 dizendo: Este persuade os homens a adorar a Deus por modo contrário à lei.
14 Ia Paulo falar, quando Gálio declarou aos judeus: Se fosse, com efeito, alguma injustiça ou crime da maior gravidade, ó judeus, de razão seria atender-vos;
15 mas, se é questão de palavra, de nomes e da vossa lei, tratai disso vós mesmos; eu não quero ser juiz dessas coisas!
16 E os expulsou do tribunal.
17 Então, todos agarraram Sóstenes, o principal da sinagoga, e o espancavam diante do tribunal; Gálio, todavia, não se incomodava com estas coisas.
18 Mas Paulo, havendo permanecido ali ainda muitos dias, por fim, despedindo-se dos irmãos, navegou para a Síria, levando em sua companhia Priscila e Áquila, depois de ter raspado a cabeça em Cencreia, porque tomara voto.
19 Chegados a Éfeso, deixou-os ali; ele, porém, entrando na sinagoga, pregava aos judeus.
20 Rogando-lhe eles que permanecesse ali mais algum tempo, não acedeu.
21 Mas, despedindo-se, disse: Se Deus quiser, voltarei para vós outros. E, embarcando, partiu de Éfeso.
22 Chegando a Cesareia, desembarcou, subindo a Jerusalém; e, tendo saudado a igreja, desceu para Antioquia.
23 Havendo passado ali algum tempo, saiu, atravessando sucessivamente a região da Galácia e Frígia, confirmando todos os discípulos.
24 Nesse meio tempo, chegou a Éfeso um judeu, natural de Alexandria, chamado Apolo, homem eloquente e poderoso nas Escrituras.
25 Era ele instruído no caminho do Senhor; e, sendo fervoroso de espírito, falava e ensinava com precisão a respeito de Jesus, conhecendo apenas o batismo de João.
26 Ele, pois, começou a falar ousadamente na sinagoga. Ouvindo-o, porém, Priscila e Áquila, tomaram-no consigo e, com mais exatidão, lhe expuseram o caminho de Deus.
27 Querendo ele percorrer a Acaia, animaram-no os irmãos e escreveram aos discípulos para o receberem. Tendo chegado, auxiliou muito aqueles que, mediante a graça, haviam crido;
28 porque, com grande poder, convencia publicamente os judeus, provando, por meio das Escrituras, que o Cristo é Jesus.*
1 Aconteceu que, estando Apolo em Corinto, Paulo, tendo passado pelas regiões mais altas, chegou a Éfeso e, achando ali alguns discípulos,
2 perguntou-lhes: Recebestes, porventura, o Espírito Santo quando crestes? Ao que lhe responderam: Pelo contrário, nem mesmo ouvimos que existe o Espírito Santo.
3 Então, Paulo perguntou: Em que, pois, fostes batizados? Responderam: No batismo de João.
4 Disse-lhes Paulo: João realizou batismo de arrependimento, dizendo ao povo que cresse naquele que vinha depois dele, a saber, em Jesus.
5 Eles, tendo ouvido isto, foram batizados em o nome do Senhor Jesus.
6 E, impondo-lhes Paulo as mãos, veio sobre eles o Espírito Santo; e tanto falavam em línguas como profetizavam.
7 Eram, ao todo, uns doze homens.
8 Durante três meses, Paulo frequentou a sinagoga, onde falava ousadamente, dissertando e persuadindo com respeito ao reino de Deus.
9 Visto que alguns deles se mostravam empedernidos e descrentes, falando mal do Caminho diante da multidão, Paulo, apartando-se deles, separou os discípulos, passando a discorrer diariamente na escola de Tirano.
10 Durou isto por espaço de dois anos, dando ensejo a que todos os habitantes da Ásia ouvissem a palavra do Senhor, tanto judeus como gregos.
11 E Deus, pelas mãos de Paulo, fazia milagres extraordinários,
12 a ponto de levarem aos enfermos lenços e aventais do seu uso pessoal, diante dos quais as enfermidades fugiam das suas vítimas, e os espíritos malignos se retiravam.
13 E alguns judeus, exorcistas ambulantes, tentaram invocar o nome do Senhor Jesus sobre possessos de espíritos malignos, dizendo: Esconjuro-vos por Jesus, a quem Paulo prega.
14 Os que faziam isto eram sete filhos de um judeu chamado Ceva, sumo sacerdote.
15 Mas o espírito maligno lhes respondeu: Conheço a Jesus e sei quem é Paulo; mas vós, quem sois?
16 E o possesso do espírito maligno saltou sobre eles, subjugando a todos, e, de tal modo prevaleceu contra eles, que, desnudos e feridos, fugiram daquela casa.
17 Chegou este fato ao conhecimento de todos, assim judeus como gregos habitantes de Éfeso; veio temor sobre todos eles, e o nome do Senhor Jesus era engrandecido.
18 Muitos dos que creram vieram confessando e denunciando publicamente as suas próprias obras.
19 Também muitos dos que haviam praticado artes mágicas, reunindo os seus livros, os queimaram diante de todos. Calculados os seus preços, achou-se que montavam a cinquenta mil denários.
20 Assim, a palavra do Senhor crescia e prevalecia poderosamente.
23 Por esse tempo, houve grande alvoroço acerca do Caminho.
24 Pois um ourives, chamado Demétrio, que fazia, de prata, nichos de Diana e que dava muito lucro aos artífices,
25 convocando-os juntamente com outros da mesma profissão, disse-lhes: Senhores, sabeis que deste ofício vem a nossa prosperidade
26 e estais vendo e ouvindo que não só em Éfeso, mas em quase toda a Ásia, este Paulo tem persuadido e desencaminhado muita gente, afirmando não serem deuses os que são feitos por mãos humanas.
27 Não somente há o perigo de a nossa profissão cair em descrédito, como também o de o próprio templo da grande deusa, Diana, ser estimado em nada, e ser mesmo destruída a majestade daquela que toda a Ásia e o mundo adoram.
28 Ouvindo isto, encheram-se de furor e clamavam: Grande é a Diana dos efésios!
29 Foi a cidade tomada de confusão, e todos, à uma, arremeteram para o teatro, arrebatando os macedônios Gaio e Aristarco, companheiros de Paulo.
30 Querendo este apresentar-se ao povo, não lhe permitiram os discípulos.
31 Também asiarcas, que eram amigos de Paulo, mandaram rogar-lhe que não se arriscasse indo ao teatro.
32 Uns, pois, gritavam de uma forma; outros, de outra; porque a assembleia caíra em confusão. E, na sua maior parte, nem sabiam por que motivo estavam reunidos.
33 Então, tiraram Alexandre dentre a multidão, impelindo-o os judeus para a frente. Este, acenando com a mão, queria falar ao povo.
34 Quando, porém, reconheceram que ele era judeu, todos, a uma voz, gritaram por espaço de quase duas horas: Grande é a Diana dos efésios!
35 O escrivão da cidade, tendo apaziguado o povo, disse: Senhores, efésios: quem, porventura, não sabe que a cidade de Éfeso é a guardiã do templo da grande Diana e da imagem que caiu de Júpiter?
36 Ora, não podendo isto ser contraditado, convém que vos mantenhais calmos e nada façais precipitadamente;
37 porque estes homens que aqui trouxestes não são sacrílegos, nem blasfemam contra a nossa deusa.
38 Portanto, se Demétrio e os artífices que o acompanham têm alguma queixa contra alguém, há audiências e procônsules; que se acusem uns aos outros.
39 Mas, se alguma outra coisa pleiteais, será decidida em assembleia regular.
40 Porque também corremos perigo de que, por hoje, sejamos acusados de sedição, não havendo motivo algum que possamos alegar para justificar este ajuntamento.
41 E, havendo dito isto, dissolveu a assembleia.*
1 Cessado o tumulto, Paulo mandou chamar os discípulos, e, tendo-os confortado, despediu-se, e partiu para a Macedônia.
2 Havendo atravessado aquelas terras, fortalecendo os discípulos com muitas exortações, dirigiu-se para a Grécia,
3 onde se demorou três meses. Tendo havido uma conspiração por parte dos judeus contra ele, quando estava para embarcar rumo à Síria, determinou voltar pela Macedônia.
4 Acompanharam-no [até à Ásia] Sópatro, de Bereia, filho de Pirro, Aristarco e Secundo, de Tessalônica, Gaio, de Derbe, e Timóteo, bem como Tíquico e Trófimo, da Ásia;
5 estes nos precederam, esperando-nos em Trôade.
6 Depois dos dias dos pães asmos, navegamos de Filipos e, em cinco dias, fomos ter com eles naquele porto, onde passamos uma semana.
7 No primeiro dia da semana, estando nós reunidos com o fim de partir o pão, Paulo, que devia seguir viagem no dia imediato, exortava-os e prolongou o discurso até à meia-noite.
8 Havia muitas lâmpadas no cenáculo onde estávamos reunidos.
9 Um jovem, chamado Êutico, que estava sentado numa janela, adormecendo profundamente durante o prolongado discurso de Paulo, vencido pelo sono, caiu do terceiro andar abaixo e foi levantado morto.
10 Descendo, porém, Paulo inclinou-se sobre ele e, abraçando-o, disse: Não vos perturbeis, que a vida nele está.
11 Subindo de novo, partiu o pão, e comeu, e ainda lhes falou largamente até ao romper da alva. E, assim, partiu.
12 Então, conduziram vivo o rapaz e sentiram-se grandemente confortados.
13 Nós, porém, prosseguindo, embarcamos e navegamos para Assôs, onde devíamos receber Paulo, porque assim nos fora determinado, devendo ele ir por terra.
14 Quando se reuniu conosco em Assôs, recebemo-lo a bordo e fomos a Mitilene;
15 dali, navegando, no dia seguinte, passamos defronte de Quios, no dia imediato, tocamos em Samos e, um dia depois, chegamos a Mileto.
16 Porque Paulo já havia determinado não aportar em Éfeso, não querendo demorar-se na Ásia, porquanto se apressava com o intuito de passar o dia de Pentecostes em Jerusalém, caso lhe fosse possível.
17 De Mileto, mandou a Éfeso chamar os presbíteros da igreja.
18 E, quando se encontraram com ele, disse-lhes: Vós bem sabeis como foi que me conduzi entre vós em todo o tempo, desde o primeiro dia em que entrei na Ásia,
19 servindo ao Senhor com toda a humildade, lágrimas e provações que, pelas ciladas dos judeus, me sobrevieram,
20 jamais deixando de vos anunciar coisa alguma proveitosa e de vo-la ensinar publicamente e também de casa em casa,
21 testificando tanto a judeus como a gregos o arrependimento para com Deus e a fé em nosso Senhor Jesus [Cristo].
22 E, agora, constrangido em meu espírito, vou para Jerusalém, não sabendo o que ali me acontecerá,
23 senão que o Espírito Santo, de cidade em cidade, me assegura que me esperam cadeias e tribulações.
24 Porém em nada considero a vida preciosa para mim mesmo, contanto que complete a minha carreira e o ministério que recebi do Senhor Jesus para testemunhar o evangelho da graça de Deus.
25 Agora, eu sei que todos vós, em cujo meio passei pregando o reino, não vereis mais o meu rosto.
26 Portanto, eu vos protesto, no dia de hoje, que estou limpo do sangue de todos;
27 porque jamais deixei de vos anunciar todo o desígnio de Deus.
28 Atendei por vós e por todo o rebanho sobre o qual o Espírito Santo vos constituiu bispos, para pastoreardes a igreja de Deus, a qual ele comprou com o seu próprio sangue.
29 Eu sei que, depois da minha partida, entre vós penetrarão lobos vorazes, que não pouparão o rebanho.
30 E que, dentre vós mesmos, se levantarão homens falando coisas pervertidas para arrastar os discípulos atrás deles.
31 Portanto, vigiai, lembrando-vos de que, por três anos, noite e dia, não cessei de admoestar, com lágrimas, a cada um.
32 Agora, pois, encomendo-vos ao Senhor e à palavra da sua graça, que tem poder para vos edificar e dar herança entre todos os que são santificados.
33 De ninguém cobicei prata, nem ouro, nem vestes;
34 vós mesmos sabeis que estas mãos serviram para o que me era necessário a mim e aos que estavam comigo.
35 Tenho-vos mostrado em tudo que, trabalhando assim, é mister socorrer os necessitados e recordar as palavras do próprio Senhor Jesus: Mais bem-aventurado é dar que receber.
36 Tendo dito estas coisas, ajoelhando-se, orou com todos eles.
37 Então, houve grande pranto entre todos, e, abraçando afetuosamente a Paulo, o beijavam,
38 entristecidos especialmente pela palavra que ele dissera: que não mais veriam o seu rosto. E acompanharam-no até ao navio.*
1 Depois de nos apartarmos, fizemo-nos à vela e, correndo em direitura, chegamos a Cós; no dia seguinte, a Rodes, e dali, a Pátara.
2 Achando um navio que ia para a Fenícia, embarcamos nele, seguindo viagem.
3 Quando Chipre já estava à vista, deixando-a à esquerda, navegamos para a Síria e chegamos a Tiro; pois o navio devia ser descarregado ali.
4 Encontrando os discípulos, permanecemos lá durante sete dias; e eles, movidos pelo Espírito, recomendavam a Paulo que não fosse a Jerusalém.
5 Passados aqueles dias, tendo-nos retirado, prosseguimos viagem, acompanhados por todos, cada um com sua mulher e filhos, até fora da cidade; ajoelhados na praia, oramos.
6 E, despedindo-nos uns dos outros, então, embarcamos; e eles voltaram para casa.
7 Quanto a nós, concluindo a viagem de Tiro, chegamos a Ptolemaida, onde saudamos os irmãos, passando um dia com eles.
8 No dia seguinte, partimos e fomos para Cesareia; e, entrando na casa de Filipe, o evangelista, que era um dos sete, ficamos com ele.
9 Tinha este quatro filhas donzelas, que profetizavam.
10 Demorando-nos ali alguns dias, desceu da Judeia um profeta chamado Ágabo;
11 e, vindo ter conosco, tomando o cinto de Paulo, ligando com ele os próprios pés e mãos, declarou: Isto diz o Espírito Santo: Assim os judeus, em Jerusalém, farão ao dono deste cinto e o entregarão nas mãos dos gentios.
12 Quando ouvimos estas palavras, tanto nós como os daquele lugar, rogamos a Paulo que não subisse a Jerusalém.
13 Então, ele respondeu: Que fazeis chorando e quebrantando-me o coração? Pois estou pronto não só para ser preso, mas até para morrer em Jerusalém pelo nome do Senhor Jesus.
14 Como, porém, não o persuadimos, conformados, dissemos: Faça-se a vontade do Senhor!
15 Passados aqueles dias, tendo feito os preparativos, subimos para Jerusalém;
16 e alguns dos discípulos também vieram de Cesareia conosco, trazendo consigo Mnasom, natural de Chipre, velho discípulo, com quem nos deveríamos hospedar.
17 Tendo nós chegado a Jerusalém, os irmãos nos receberam com alegria.
18 No dia seguinte, Paulo foi conosco encontrar-se com Tiago, e todos os presbíteros se reuniram.
19 E, tendo-os saudado, contou minuciosamente o que Deus fizera entre os gentios por seu ministério.
20 Ouvindo-o, deram eles glória a Deus e lhe disseram: Bem vês, irmão, quantas dezenas de milhares há entre os judeus que creram, e todos são zelosos da lei;
21 e foram informados a teu respeito que ensinas todos os judeus entre os gentios a apostatarem de Moisés, dizendo-lhes que não devem circuncidar os filhos, nem andar segundo os costumes da lei.
22 Que se há de fazer, pois? Certamente saberão da tua chegada.
23 Faze, portanto, o que te vamos dizer: estão entre nós quatro homens que, voluntariamente, aceitaram voto;
24 toma-os, purifica-te com eles e faze a despesa necessária para que raspem a cabeça; e saberão todos que não é verdade o que se diz a teu respeito; e que, pelo contrário, andas também, tu mesmo, guardando a lei.
25 Quanto aos gentios que creram, já lhes transmitimos decisões para que se abstenham das coisas sacrificadas a ídolos, do sangue, da carne de animais sufocados e das relações sexuais ilícitas.
26 Então, Paulo, tomando aqueles homens, no dia seguinte, tendo-se purificado com eles, entrou no templo, acertando o cumprimento dos dias da purificação, até que se fizesse a oferta em favor de cada um deles.
27 Quando já estavam por findar os sete dias, os judeus vindos da Ásia, tendo visto Paulo no templo, alvoroçaram todo o povo e o agarraram,
28 gritando: Israelitas, socorro! Este é o homem que por toda parte ensina todos a serem contra o povo, contra a lei e contra este lugar; ainda mais, introduziu até gregos no templo e profanou este recinto sagrado.
29 Pois, antes, tinham visto Trófimo, o efésio, em sua companhia na cidade e julgavam que Paulo o introduzira no templo.
30 Agitou-se toda a cidade, havendo concorrência do povo; e, agarrando a Paulo, arrastaram-no para fora do templo, e imediatamente foram fechadas as portas.
31 Procurando eles matá-lo, chegou ao conhecimento do comandante da força que toda a Jerusalém estava amotinada.
32 Então, este, levando logo soldados e centuriões, correu para o meio do povo. Ao verem chegar o comandante e os soldados, cessaram de espancar Paulo.
33 Aproximando-se o comandante, apoderou-se de Paulo e ordenou que fosse acorrentado com duas cadeias, perguntando quem era e o que havia feito.
34 Na multidão, uns gritavam de um modo; outros, de outro; não podendo ele, porém, saber a verdade por causa do tumulto, ordenou que Paulo fosse recolhido à fortaleza.
35 Ao chegar às escadas, foi preciso que os soldados o carregassem, por causa da violência da multidão,
36 pois a massa de povo o seguia gritando: Mata-o!
37 E, quando Paulo ia sendo recolhido à fortaleza, disse ao comandante: É-me permitido dizer-te alguma coisa? Respondeu ele: Sabes o grego?
38 Não és tu, porventura, o egípcio que, há tempos, sublevou e conduziu ao deserto quatro mil sicários?
39 Respondeu-lhe Paulo: Eu sou judeu, natural de Tarso, cidade não insignificante da Cilícia; e rogo-te que me permitas falar ao povo.
40 Obtida a permissão, Paulo, em pé na escada, fez com a mão sinal ao povo. Fez-se grande silêncio, e ele falou em língua hebraica, dizendo:*
1 Irmãos e pais, ouvi, agora, a minha defesa perante vós.
2 Quando ouviram que lhes falava em língua hebraica, guardaram ainda maior silêncio. E continuou:
3 Eu sou judeu, nasci em Tarso da Cilícia, mas criei-me nesta cidade e aqui fui instruído aos pés de Gamaliel, segundo a exatidão da lei de nossos antepassados, sendo zeloso para com Deus, assim como todos vós o sois no dia de hoje.
4 Persegui este Caminho até à morte, prendendo e metendo em cárceres homens e mulheres,
5 de que são testemunhas o sumo sacerdote e todos os anciãos. Destes, recebi cartas para os irmãos; e ia para Damasco, no propósito de trazer manietados para Jerusalém os que também lá estivessem, para serem punidos.
6 Ora, aconteceu que, indo de caminho e já perto de Damasco, quase ao meio-dia, repentinamente, grande luz do céu brilhou ao redor de mim.
7 Então, caí por terra, ouvindo uma voz que me dizia: Saulo, Saulo, por que me persegues?
8 Perguntei: quem és tu, Senhor? Ao que me respondeu: Eu sou Jesus, o Nazareno, a quem tu persegues.
9 Os que estavam comigo viram a luz, sem, contudo, perceberem o sentido da voz de quem falava comigo.
10 Então, perguntei: que farei, Senhor? E o Senhor me disse: Levanta-te, entra em Damasco, pois ali te dirão acerca de tudo o que te é ordenado fazer.
11 Tendo ficado cego por causa do fulgor daquela luz, guiado pela mão dos que estavam comigo, cheguei a Damasco.
12 Um homem, chamado Ananias, piedoso conforme a lei, tendo bom testemunho de todos os judeus que ali moravam,
13 veio procurar-me e, pondo-se junto a mim, disse: Saulo, irmão, recebe novamente a vista. Nessa mesma hora, recobrei a vista e olhei para ele.
14 Então, ele disse: O Deus de nossos pais, de antemão, te escolheu para conheceres a sua vontade, veres o Justo e ouvires uma voz da sua própria boca,
15 porque terás de ser sua testemunha diante de todos os homens, das coisas que tens visto e ouvido.
16 E agora, por que te demoras? Levanta-te, recebe o batismo e lava os teus pecados, invocando o nome dele.
17 Tendo eu voltado para Jerusalém, enquanto orava no templo, sobreveio-me um êxtase,
18 e vi aquele que falava comigo: Apressa-te e sai logo de Jerusalém, porque não receberão o teu testemunho a meu respeito.
19 Eu disse: Senhor, eles bem sabem que eu encerrava em prisão e, nas sinagogas, açoitava os que criam em ti.
20 Quando se derramava o sangue de Estêvão, tua testemunha, eu também estava presente, consentia nisso e até guardei as vestes dos que o matavam.
21 Mas ele me disse: Vai, porque eu te enviarei para longe, aos gentios.
22 Ouviram-no até essa palavra e, então, gritaram, dizendo: Tira tal homem da terra, porque não convém que ele viva!
23 Ora, estando eles gritando, arrojando de si as suas capas, atirando poeira para os ares,
24 ordenou o comandante que Paulo fosse recolhido à fortaleza e que, sob açoite, fosse interrogado para saber por que motivo assim clamavam contra ele.
25 Quando o estavam amarrando com correias, disse Paulo ao centurião presente: Ser-vos-á, porventura, lícito açoitar um cidadão romano, sem estar condenado?
26 Ouvindo isto, o centurião procurou o comandante e lhe disse: Que estás para fazer? Porque este homem é cidadão romano.
27 Vindo o comandante, perguntou a Paulo: Dize-me: és tu romano? Ele disse: Sou.
28 Respondeu-lhe o comandante: A mim me custou grande soma de dinheiro este título de cidadão. Disse Paulo: Pois eu o tenho por direito de nascimento.
29 Imediatamente, se afastaram os que estavam para o inquirir com açoites. O próprio comandante sentiu-se receoso quando soube que Paulo era romano, porque o mandara amarrar.
30 No dia seguinte, querendo certificar-se dos motivos por que vinha ele sendo acusado pelos judeus, soltou-o, e ordenou que se reunissem os principais sacerdotes e todo o Sinédrio, e, mandando trazer Paulo, apresentou-o perante eles.*
1 Fitando Paulo os olhos no Sinédrio, disse: Varões, irmãos, tenho andado diante de Deus com toda a boa consciência até ao dia de hoje.
2 Mas o sumo sacerdote, Ananias, mandou aos que estavam perto dele que lhe batessem na boca.
3 Então, lhe disse Paulo: Deus há de ferir-te, parede branqueada! Tu estás aí sentado para julgar-me segundo a lei e, contra a lei, mandas agredir-me?
4 Os que estavam a seu lado disseram: Estás injuriando o sumo sacerdote de Deus?
5 Respondeu Paulo: Não sabia, irmãos, que ele é sumo sacerdote; porque está escrito: Não falarás mal de uma autoridade do teu povo.
6 Sabendo Paulo que uma parte do Sinédrio se compunha de saduceus e outra, de fariseus, exclamou: Varões, irmãos, eu sou fariseu, filho de fariseus! No tocante à esperança e à ressurreição dos mortos sou julgado!
7 Ditas estas palavras, levantou-se grande dissensão entre fariseus e saduceus, e a multidão se dividiu.
8 Pois os saduceus declaram não haver ressurreição, nem anjo, nem espírito; ao passo que os fariseus admitem todas essas coisas.
9 Houve, pois, grande vozearia. E, levantando-se alguns escribas da parte dos fariseus, contendiam, dizendo: Não achamos neste homem mal algum; e será que algum espírito ou anjo lhe tenha falado?
10 Tomando vulto a celeuma, temendo o comandante que fosse Paulo espedaçado por eles, mandou descer a guarda para que o retirassem dali e o levassem para a fortaleza.
11 Na noite seguinte, o Senhor, pondo-se ao lado dele, disse: Coragem! Pois do modo por que deste testemunho a meu respeito em Jerusalém, assim importa que também o faças em Roma.
12 Quando amanheceu, os judeus se reuniram e, sob anátema, juraram que não haviam de comer, nem beber, enquanto não matassem Paulo.
13 Eram mais de quarenta os que entraram nesta conspirata.
14 Estes, indo ter com os principais sacerdotes e os anciãos, disseram: Juramos, sob pena de anátema, não comer coisa alguma, enquanto não matarmos Paulo.
15 Agora, pois, notificai ao comandante, juntamente com o Sinédrio, que vo-lo apresente como se estivésseis para investigar mais acuradamente a sua causa; e nós, antes que ele chegue, estaremos prontos para assassiná-lo.
16 Mas o filho da irmã de Paulo, tendo ouvido a trama, foi, entrou na fortaleza e de tudo avisou a Paulo.
17 Então, este, chamando um dos centuriões, disse: Leva este rapaz ao comandante, porque tem alguma coisa a comunicar-lhe.
18 Tomando-o, pois, levou-o ao comandante, dizendo: O preso Paulo, chamando-me, pediu-me que trouxesse à tua presença este rapaz, pois tem algo que dizer-te.
19 Tomou-o pela mão o comandante e, pondo-se à parte, perguntou-lhe: Que tens a comunicar-me?
20 Respondeu ele: Os judeus decidiram rogar-te que, amanhã, apresentes Paulo ao Sinédrio, como se houvesse de inquirir mais acuradamente a seu respeito.
21 Tu, pois, não te deixes persuadir, porque mais de quarenta entre eles estão pactuados entre si, sob anátema, de não comer, nem beber, enquanto não o matarem; e, agora, estão prontos, esperando a tua promessa.
22 Então, o comandante despediu o rapaz, recomendando-lhe que a ninguém dissesse ter-lhe trazido estas informações.
23 Chamando dois centuriões, ordenou: Tende de prontidão, desde a hora terceira da noite, duzentos soldados, setenta de cavalaria e duzentos lanceiros para irem até Cesareia;
24 preparai também animais para fazer Paulo montar e ir com segurança ao governador Félix.
25 E o comandante escreveu uma carta nestes termos:
26 Cláudio Lísias ao excelentíssimo governador Félix, saúde.
27 Este homem foi preso pelos judeus e estava prestes a ser morto por eles, quando eu, sobrevindo com a guarda, o livrei, por saber que ele era romano.
28 Querendo certificar-me do motivo por que o acusavam, fi-lo descer ao Sinédrio deles;
29 verifiquei ser ele acusado de coisas referentes à lei que os rege, nada, porém, que justificasse morte ou mesmo prisão.
30 Sendo eu informado de que ia haver uma cilada contra o homem, tratei de enviá-lo a ti, sem demora, intimando também os acusadores a irem dizer, na tua presença, o que há contra ele. [Saúde.]
31 Os soldados, pois, conforme lhes foi ordenado, tomaram Paulo e, durante a noite, o conduziram até Antipátride;
32 no dia seguinte, voltaram para a fortaleza, tendo deixado aos de cavalaria o irem com ele;
33 os quais, chegando a Cesareia, entregaram a carta ao governador e também lhe apresentaram Paulo.
34 Lida a carta, perguntou o governador de que província ele era; e, quando soube que era da Cilícia,
35 disse: Ouvir-te-ei quando chegarem os teus acusadores. E mandou que ele fosse detido no pretório de Herodes.*
1 Cinco dias depois, desceu o sumo sacerdote, Ananias, com alguns anciãos e com certo orador, chamado Tértulo, os quais apresentaram ao governador libelo contra Paulo.
2 Sendo este chamado, passou Tértulo a acusá-lo, dizendo: Excelentíssimo Félix, tendo nós, por teu intermédio, gozado de paz perene, e, também por teu providente cuidado, se terem feito notáveis reformas em benefício deste povo,
3 sempre e por toda parte, isto reconhecemos com toda a gratidão.
4 Entretanto, para não te deter por longo tempo, rogo-te que, de conformidade com a tua clemência, nos atendas por um pouco.
5 Porque, tendo nós verificado que este homem é uma peste e promove sedições entre os judeus esparsos por todo o mundo, sendo também o principal agitador da seita dos nazarenos,
6 o qual também tentou profanar o templo, nós o prendemos [com o intuito de julgá-lo segundo a nossa lei.
7 Mas, sobrevindo o comandante Lísias, o arrebatou das nossas mãos com grande violência,
8 ordenando que os seus acusadores viessem à tua presença]. Tu mesmo, examinando-o, poderás tomar conhecimento de todas as coisas de que nós o acusamos.
9 Os judeus também concordaram na acusação, afirmando que estas coisas eram assim.
10 Paulo, tendo-lhe o governador feito sinal que falasse, respondeu: Sabendo que há muitos anos és juiz desta nação, sinto-me à vontade para me defender,
11 visto poderes verificar que não há mais de doze dias desde que subi a Jerusalém para adorar;
12 e que não me acharam no templo discutindo com alguém, nem tampouco amotinando o povo, fosse nas sinagogas ou na cidade;
13 nem te podem provar as acusações que, agora, fazem contra mim.
14 Porém confesso-te que, segundo o Caminho, a que chamam seita, assim eu sirvo ao Deus de nossos pais, acreditando em todas as coisas que estejam de acordo com a lei e nos escritos dos profetas,
15 tendo esperança em Deus, como também estes a têm, de que haverá ressurreição, tanto de justos como de injustos.
16 Por isso, também me esforço por ter sempre consciência pura diante de Deus e dos homens.
17 Depois de anos, vim trazer esmolas à minha nação e também fazer oferendas,
18 e foi nesta prática que alguns judeus da Ásia me encontraram já purificado no templo, sem ajuntamento e sem tumulto,
19 os quais deviam comparecer diante de ti e acusar, se tivessem alguma coisa contra mim.
20 Ou estes mesmos digam que iniquidade acharam em mim, por ocasião do meu comparecimento perante o Sinédrio,
21 salvo estas palavras que clamei, estando entre eles: hoje, sou eu julgado por vós acerca da ressurreição dos mortos.
22 Então, Félix, conhecendo mais acuradamente as coisas com respeito ao Caminho, adiou a causa, dizendo: Quando descer o comandante Lísias, tomarei inteiro conhecimento do vosso caso.
23 E mandou ao centurião que conservasse a Paulo detido, tratando-o com indulgência e não impedindo que os seus próprios o servissem.
24 Passados alguns dias, vindo Félix com Drusila, sua mulher, que era judia, mandou chamar Paulo e passou a ouvi-lo a respeito da fé em Cristo Jesus.
25 Dissertando ele acerca da justiça, do domínio próprio e do Juízo vindouro, ficou Félix amedrontado e disse: Por agora, podes retirar-te, e, quando eu tiver vagar, chamar-te-ei;
26 esperando também, ao mesmo tempo, que Paulo lhe desse dinheiro; pelo que, chamando-o mais frequentemente, conversava com ele.
27 Dois anos mais tarde, Félix teve por sucessor Pórcio Festo; e, querendo Félix assegurar o apoio dos judeus, manteve Paulo encarcerado.*
1 Tendo, pois, Festo assumido o governo da província, três dias depois, subiu de Cesareia para Jerusalém;
2 e, logo, os principais sacerdotes e os maiorais dos judeus lhe apresentaram queixa contra Paulo e lhe solicitavam,
3 pedindo como favor, em detrimento de Paulo, que o mandasse vir a Jerusalém, armando eles cilada para o matarem na estrada.
4 Festo, porém, respondeu achar-se Paulo detido em Cesareia; e que ele mesmo, muito em breve, partiria para lá.
5 Portanto, disse ele, os que dentre vós estiverem habilitados que desçam comigo; e, havendo contra este homem qualquer crime, acusem-no.
6 E, não se demorando entre eles mais de oito ou dez dias, desceu para Cesareia; e, no dia seguinte, assentando-se no tribunal, ordenou que Paulo fosse trazido.
7 Comparecendo este, rodearam-no os judeus que haviam descido de Jerusalém, trazendo muitas e graves acusações contra ele, as quais, entretanto, não podiam provar.
8 Paulo, porém, defendendo-se, proferiu as seguintes palavras: Nenhum pecado cometi contra a lei dos judeus, nem contra o templo, nem contra César.
9 Então, Festo, querendo assegurar o apoio dos judeus, respondeu a Paulo: Queres tu subir a Jerusalém e ser ali julgado por mim a respeito destas coisas?
10 Disse-lhe Paulo: Estou perante o tribunal de César, onde convém seja eu julgado; nenhum agravo pratiquei contra os judeus, como tu muito bem sabes.
11 Caso, pois, tenha eu praticado algum mal ou crime digno de morte, estou pronto para morrer; se, pelo contrário, não são verdadeiras as coisas de que me acusam, ninguém, para lhes ser agradável, pode entregar-me a eles. Apelo para César.
12 Então, Festo, tendo falado com o conselho, respondeu: Para César apelaste, para César irás.
13 Passados alguns dias, o rei Agripa e Berenice chegaram a Cesareia a fim de saudar a Festo.
14 Como se demorassem ali alguns dias, Festo expôs ao rei o caso de Paulo, dizendo: Félix deixou aqui preso certo homem,
15 a respeito de quem os principais sacerdotes e os anciãos dos judeus apresentaram queixa, estando eu em Jerusalém, pedindo que o condenasse.
16 A eles respondi que não é costume dos romanos condenar quem quer que seja, sem que o acusado tenha presentes os seus acusadores e possa defender-se da acusação.
17 De sorte que, chegando eles aqui juntos, sem nenhuma demora, no dia seguinte, assentando-me no tribunal, determinei fosse trazido o homem;
18 e, levantando-se os acusadores, nenhum delito referiram dos crimes de que eu suspeitava.
19 Traziam contra ele algumas questões referentes à sua própria religião e particularmente a certo morto, chamado Jesus, que Paulo afirmava estar vivo.
20 Estando eu perplexo quanto ao modo de investigar estas coisas, perguntei-lhe se queria ir a Jerusalém para ser ali julgado a respeito disso.
21 Mas, havendo Paulo apelado para que ficasse em custódia para o julgamento de César, ordenei que o acusado continuasse detido até que eu o enviasse a César.
22 Então, Agripa disse a Festo: Eu também gostaria de ouvir este homem. Amanhã, respondeu ele, o ouvirás.
23 De fato, no dia seguinte, vindo Agripa e Berenice, com grande pompa, tendo eles entrado na audiência juntamente com oficiais superiores e homens eminentes da cidade, Paulo foi trazido por ordem de Festo.
24 Então, disse Festo: Rei Agripa e todos vós que estais presentes conosco, vedes este homem, por causa de quem toda a multidão dos judeus recorreu a mim tanto em Jerusalém como aqui, clamando que não convinha que ele vivesse mais.
25 Porém eu achei que ele nada praticara passível de morte; entretanto, tendo ele apelado para o imperador, resolvi mandá-lo ao imperador.
26 Contudo, a respeito dele, nada tenho de positivo que escreva ao soberano; por isso, eu o trouxe à vossa presença e, mormente, à tua, ó rei Agripa, para que, feita a arguição, tenha eu alguma coisa que escrever;
27 porque não me parece razoável remeter um preso sem mencionar, ao mesmo tempo, as acusações que militam contra ele.*
1 A seguir, Agripa, dirigindo-se a Paulo, disse: É permitido que uses da palavra em tua defesa. Então, Paulo, estendendo a mão, passou a defender-se nestes termos:
2 Tenho-me por feliz, ó rei Agripa, pelo privilégio de, hoje, na tua presença, poder produzir a minha defesa de todas as acusações feitas contra mim pelos judeus;
3 mormente porque és versado em todos os costumes e questões que há entre os judeus; por isso, eu te peço que me ouças com paciência.
4 Quanto à minha vida, desde a mocidade, como decorreu desde o princípio entre o meu povo e em Jerusalém, todos os judeus a conhecem;
5 pois, na verdade, eu era conhecido deles desde o princípio, se assim o quiserem testemunhar, porque vivi fariseu conforme a seita mais severa da nossa religião.
6 E, agora, estou sendo julgado por causa da esperança da promessa que por Deus foi feita a nossos pais,
7 a qual as nossas doze tribos, servindo a Deus fervorosamente de noite e de dia, almejam alcançar; é no tocante a esta esperança, ó rei, que eu sou acusado pelos judeus.
8 Por que se julga incrível entre vós que Deus ressuscite os mortos?
9 Na verdade, a mim me parecia que muitas coisas devia eu praticar contra o nome de Jesus, o Nazareno;
10 e assim procedi em Jerusalém. Havendo eu recebido autorização dos principais sacerdotes, encerrei muitos dos santos nas prisões; e contra estes dava o meu voto, quando os matavam.
11 Muitas vezes, os castiguei por todas as sinagogas, obrigando-os até a blasfemar. E, demasiadamente enfurecido contra eles, mesmo por cidades estranhas os perseguia.
12 Com estes intuitos, parti para Damasco, levando autorização dos principais sacerdotes e por eles comissionado.
13 Ao meio-dia, ó rei, indo eu caminho fora, vi uma luz no céu, mais resplandecente que o sol, que brilhou ao redor de mim e dos que iam comigo.
14 E, caindo todos nós por terra, ouvi uma voz que me falava em língua hebraica: Saulo, Saulo, por que me persegues? Dura coisa é recalcitrares contra os aguilhões.
15 Então, eu perguntei: Quem és tu, Senhor? Ao que o Senhor respondeu: Eu sou Jesus, a quem tu persegues.
16 Mas levanta-te e firma-te sobre teus pés, porque por isto te apareci, para te constituir ministro e testemunha, tanto das coisas em que me viste como daquelas pelas quais te aparecerei ainda,
17 livrando-te do povo e dos gentios, para os quais eu te envio,
18 para lhes abrires os olhos e os converteres das trevas para a luz e da potestade de Satanás para Deus, a fim de que recebam eles remissão de pecados e herança entre os que são santificados pela fé em mim.
19 Pelo que, ó rei Agripa, não fui desobediente à visão celestial,
20 mas anunciei primeiramente aos de Damasco e em Jerusalém, por toda a região da Judeia, e aos gentios, que se arrependessem e se convertessem a Deus, praticando obras dignas de arrependimento.
21 Por causa disto, alguns judeus me prenderam, estando eu no templo, e tentaram matar-me.
22 Mas, alcançando socorro de Deus, permaneço até ao dia de hoje, dando testemunho, tanto a pequenos como a grandes, nada dizendo, senão o que os profetas e Moisés disseram haver de acontecer,
23 isto é, que o Cristo devia padecer e, sendo o primeiro da ressurreição dos mortos, anunciaria a luz ao povo e aos gentios.
24 Dizendo ele estas coisas em sua defesa, Festo o interrompeu em alta voz: Estás louco, Paulo! As muitas letras te fazem delirar!
25 Paulo, porém, respondeu: Não estou louco, ó excelentíssimo Festo! Pelo contrário, digo palavras de verdade e de bom senso.
26 Porque tudo isto é do conhecimento do rei, a quem me dirijo com franqueza, pois estou persuadido de que nenhuma destas coisas lhe é oculta; porquanto nada se passou em algum lugar escondido.
27 Acreditas, ó rei Agripa, nos profetas? Bem sei que acreditas.
28 Então, Agripa se dirigiu a Paulo e disse: Por pouco me persuades a me fazer cristão.
29 Paulo respondeu: Assim Deus permitisse que, por pouco ou por muito, não apenas tu, ó rei, porém todos os que hoje me ouvem se tornassem tais qual eu sou, exceto estas cadeias.
30 A essa altura, levantou-se o rei, e também o governador, e Berenice, bem como os que estavam assentados com eles;
31 e, havendo-se retirado, falavam uns com os outros, dizendo: Este homem nada tem feito passível de morte ou de prisão.
32 Então, Agripa se dirigiu a Festo e disse: Este homem bem podia ser solto, se não tivesse apelado para César.*
1 Quando foi decidido que navegássemos para a Itália, entregaram Paulo e alguns outros presos a um centurião chamado Júlio, da Coorte Imperial.
2 Embarcando num navio adramitino, que estava de partida para costear a Ásia, fizemo-nos ao mar, indo conosco Aristarco, macedônio de Tessalônica.
3 No dia seguinte, chegamos a Sidom, e Júlio, tratando Paulo com humanidade, permitiu-lhe ir ver os amigos e obter assistência.
4 Partindo dali, navegamos sob a proteção de Chipre, por serem contrários os ventos;
5 e, tendo atravessado o mar ao longo da Cilícia e Panfília, chegamos a Mirra, na Lícia.
6 Achando ali o centurião um navio de Alexandria, que estava de partida para a Itália, nele nos fez embarcar.
7 Navegando vagarosamente muitos dias e tendo chegado com dificuldade defronte de Cnido, não nos sendo permitido prosseguir, por causa do vento contrário, navegamos sob a proteção de Creta, na altura de Salmona.
8 Costeando-a, penosamente, chegamos a um lugar chamado Bons Portos, perto do qual estava a cidade de Laseia.
9 Depois de muito tempo, tendo-se tornado a navegação perigosa, e já passado o tempo do Dia do Jejum, admoestava-os Paulo,
10 dizendo-lhes: Senhores, vejo que a viagem vai ser trabalhosa, com dano e muito prejuízo, não só da carga e do navio, mas também da nossa vida.
11 Mas o centurião dava mais crédito ao piloto e ao mestre do navio do que ao que Paulo dizia.
12 Não sendo o porto próprio para invernar, a maioria deles era de opinião que partissem dali, para ver se podiam chegar a Fenice e aí passar o inverno, visto ser um porto de Creta, o qual olhava para o nordeste e para o sudeste.
13 Soprando brandamente o vento sul, e pensando eles ter alcançado o que desejavam, levantaram âncora e foram costeando mais de perto a ilha de Creta.
14 Entretanto, não muito depois, desencadeou-se, do lado da ilha, um tufão de vento, chamado Euroaquilão;
15 e, sendo o navio arrastado com violência, sem poder resistir ao vento, cessamos a manobra e nos fomos deixando levar.
16 Passando sob a proteção de uma ilhota chamada Cauda, a custo conseguimos recolher o bote;
17 e, levantando este, usaram de todos os meios para cingir o navio, e, temendo que dessem na Sirte, arriaram os aparelhos, e foram ao léu.
18 Açoitados severamente pela tormenta, no dia seguinte, já aliviavam o navio.
19 E, ao terceiro dia, nós mesmos, com as próprias mãos, lançamos ao mar a armação do navio.
20 E, não aparecendo, havia já alguns dias, nem sol nem estrelas, caindo sobre nós grande tempestade, dissipou-se, afinal, toda a esperança de salvamento.
21 Havendo todos estado muito tempo sem comer, Paulo, pondo-se em pé no meio deles, disse: Senhores, na verdade, era preciso terem-me atendido e não partir de Creta, para evitar este dano e perda.
22 Mas, já agora, vos aconselho bom ânimo, porque nenhuma vida se perderá de entre vós, mas somente o navio.
23 Porque, esta mesma noite, um anjo de Deus, de quem eu sou e a quem sirvo, esteve comigo,
24 dizendo: Paulo, não temas! É preciso que compareças perante César, e eis que Deus, por sua graça, te deu todos quantos navegam contigo.
25 Portanto, senhores, tende bom ânimo! Pois eu confio em Deus que sucederá do modo por que me foi dito.
26 Porém é necessário que vamos dar a uma ilha.

27 Quando chegou a décima quarta noite, sendo nós batidos de um lado para outro no mar Adriático, por volta da meia-noite, pressentiram os marinheiros que se aproximavam de alguma terra.
28 E, lançando o prumo, acharam vinte braças; passando um pouco mais adiante, tornando a lançar o prumo, acharam quinze braças.
29 E, receosos de que fôssemos atirados contra lugares rochosos, lançaram da popa quatro âncoras e oravam para que rompesse o dia.
30 Procurando os marinheiros fugir do navio, e, tendo arriado o bote no mar, a pretexto de que estavam para largar âncoras da proa,
31 disse Paulo ao centurião e aos soldados: Se estes não permanecerem a bordo, vós não podereis salvar-vos.
32 Então, os soldados cortaram os cabos do bote e o deixaram afastar-se.
33 Enquanto amanhecia, Paulo rogava a todos que se alimentassem, dizendo: Hoje, é o décimo quarto dia em que, esperando, estais sem comer, nada tendo provado.
34 Eu vos rogo que comais alguma coisa; porque disto depende a vossa segurança; pois nenhum de vós perderá nem mesmo um fio de cabelo.
35 Tendo dito isto, tomando um pão, deu graças a Deus na presença de todos e, depois de o partir, começou a comer.
36 Todos cobraram ânimo e se puseram também a comer.
37 Estávamos no navio duzentas e setenta e seis pessoas ao todo.
38 Refeitos com a comida, aliviaram o navio, lançando o trigo ao mar.
39 Quando amanheceu, não reconheceram a terra, mas avistaram uma enseada, onde havia praia; então, consultaram entre si se não podiam encalhar ali o navio.
40 Levantando as âncoras, deixaram-no ir ao mar, largando também as amarras do leme; e, alçando a vela de proa ao vento, dirigiram-se para a praia.
41 Dando, porém, num lugar onde duas correntes se encontravam, encalharam ali o navio; a proa encravou-se e ficou imóvel, mas a popa se abria pela violência do mar.
42 O parecer dos soldados era que matassem os presos, para que nenhum deles, nadando, fugisse;
43 mas o centurião, querendo salvar a Paulo, impediu-os de o fazer; e ordenou que os que soubessem nadar fossem os primeiros a lançar-se ao mar e alcançar a terra.
44 Quanto aos demais, que se salvassem, uns, em tábuas, e outros, em destroços do navio. E foi assim que todos se salvaram em terra.*
1 Uma vez em terra, verificamos que a ilha se chamava Malta.
2 Os bárbaros trataram-nos com singular humanidade, porque, acendendo uma fogueira, acolheram-nos a todos por causa da chuva que caía e por causa do frio.
3 Tendo Paulo ajuntado e atirado à fogueira um feixe de gravetos, uma víbora, fugindo do calor, prendeu-se-lhe à mão.
4 Quando os bárbaros viram a víbora pendente da mão dele, disseram uns aos outros: Certamente, este homem é assassino, porque, salvo do mar, a Justiça não o deixa viver.
5 Porém ele, sacudindo o réptil no fogo, não sofreu mal nenhum;
6 mas eles esperavam que ele viesse a inchar ou a cair morto de repente. Mas, depois de muito esperar, vendo que nenhum mal lhe sucedia, mudando de parecer, diziam ser ele um deus.
7 Perto daquele lugar, havia um sítio pertencente ao homem principal da ilha, chamado Públio, o qual nos recebeu e hospedou benignamente por três dias.
8 Aconteceu achar-se enfermo de disenteria, ardendo em febre, o pai de Públio. Paulo foi visitá-lo, e, orando, impôs-lhe as mãos, e o curou.
9 À vista deste acontecimento, os demais enfermos da ilha vieram e foram curados,
10 os quais nos distinguiram com muitas honrarias; e, tendo nós de prosseguir viagem, nos puseram a bordo tudo o que era necessário.
11 Ao cabo de três meses, embarcamos num navio alexandrino, que invernara na ilha e tinha por emblema Dióscuros.
12 Tocando em Siracusa, ficamos ali três dias,
13 donde, bordejando, chegamos a Régio. No dia seguinte, tendo soprado vento sul, em dois dias, chegamos a Putéoli,
14 onde achamos alguns irmãos que nos rogaram ficássemos com eles sete dias; e foi assim que nos dirigimos a Roma.
15 Tendo ali os irmãos ouvido notícias nossas, vieram ao nosso encontro até à Praça de Ápio e às Três Vendas. Vendo-os Paulo e dando, por isso, graças a Deus, sentiu-se mais animado.
16 Uma vez em Roma, foi permitido a Paulo morar por sua conta, tendo em sua companhia o soldado que o guardava.
17 Três dias depois, ele convocou os principais dos judeus e, quando se reuniram, lhes disse: Varões irmãos, nada havendo feito contra o povo ou contra os costumes paternos, contudo, vim preso desde Jerusalém, entregue nas mãos dos romanos;
18 os quais, havendo-me interrogado, quiseram soltar-me sob a preliminar de não haver em mim nenhum crime passível de morte.
19 Diante da oposição dos judeus, senti-me compelido a apelar para César, não tendo eu, porém, nada de que acusar minha nação.
20 Foi por isto que vos chamei para vos ver e falar; porque é pela esperança de Israel que estou preso com esta cadeia.
21 Então, eles lhe disseram: Nós não recebemos da Judeia nenhuma carta que te dissesse respeito; também não veio qualquer dos irmãos que nos anunciasse ou dissesse de ti mal algum.
22 Contudo, gostaríamos de ouvir o que pensas; porque, na verdade, é corrente a respeito desta seita que, por toda parte, é ela impugnada.
23 Havendo-lhe eles marcado um dia, vieram em grande número ao encontro de Paulo na sua própria residência. Então, desde a manhã até à tarde, lhes fez uma exposição em testemunho do reino de Deus, procurando persuadi-los a respeito de Jesus, tanto pela lei de Moisés como pelos profetas.
24 Houve alguns que ficaram persuadidos pelo que ele dizia; outros, porém, continuaram incrédulos.
25 E, havendo discordância entre eles, despediram-se, dizendo Paulo estas palavras: Bem falou o Espírito Santo a vossos pais, por intermédio do profeta Isaías, quando disse:
26 Vai a este povo e dize-lhe: De ouvido, ouvireis e não entendereis; vendo, vereis e não percebereis.
27 Porquanto o coração deste povo se tornou endurecido; com os ouvidos ouviram tardiamente e fecharam os olhos, para que jamais vejam com os olhos, nem ouçam com os ouvidos, para que não entendam com o coração, e se convertam, e por mim sejam curados.
28 Tomai, pois, conhecimento de que esta salvação de Deus foi enviada aos gentios. E eles a ouvirão.
29 [Ditas estas palavras, partiram os judeus, tendo entre si grande contenda.]
30 Por dois anos, permaneceu Paulo na sua própria casa, que alugara, onde recebia todos que o procuravam,
31 pregando o reino de Deus, e, com toda a intrepidez, sem impedimento algum, ensinava as coisas referentes ao Senhor Jesus Cristo.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Atos','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)