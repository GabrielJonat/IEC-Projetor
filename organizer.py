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
1 Como jaz solitária a cidade outrora populosa! Tornou-se como viúva a que foi grande entre as nações; princesa entre as províncias, ficou sujeita a trabalhos forçados!
2 Chora e chora de noite, e as suas lágrimas lhe correm pelas faces; não tem quem a console entre todos os que a amavam; todos os seus amigos procederam perfidamente contra ela, tornaram-se seus inimigos.
3 Judá foi levado ao exílio, afligido e sob grande servidão; habita entre as nações, não acha descanso; todos os seus perseguidores o apanharam nas suas angústias.
4 Os caminhos de Sião estão de luto, porque não há quem venha à reunião solene; todas as suas portas estão desoladas; os seus sacerdotes gemem; as suas virgens estão tristes, e ela mesma se acha em amargura.
5 Os seus adversários triunfam, os seus inimigos prosperam; porque o Senhor a afligiu, por causa da multidão das suas prevaricações; os seus filhinhos tiveram de ir para o exílio, na frente do adversário.
6 Da filha de Sião já se passou todo o esplendor; os seus príncipes ficaram sendo como corços que não acham pasto e caminham exaustos na frente do perseguidor.
7 Agora, nos dias da sua aflição e do seu desterro, lembra-se Jerusalém de todas as suas mais estimadas coisas, que tivera dos tempos antigos; de como o seu povo caíra nas mãos do adversário, não tendo ela quem a socorresse; e de como os adversários a viram e fizeram escárnio da sua queda.
8 Jerusalém pecou gravemente; por isso, se tornou repugnante; todos os que a honravam a desprezam, porque lhe viram a nudez; ela também geme e se retira envergonhada.
9 A sua imundícia está nas suas saias; ela não pensava no seu fim; por isso, caiu de modo espantoso e não tem quem a console. Vê, Senhor, a minha aflição, porque o inimigo se torna insolente.
10 Estendeu o adversário a mão a todas as coisas mais estimadas dela; pois ela viu entrar as nações no seu santuário, acerca das quais proibiste que entrassem na tua congregação.
11 Todo o seu povo anda gemendo e à procura de pão; deram eles as suas coisas mais estimadas a troco de mantimento para restaurar as forças; vê, Senhor, e contempla, pois me tornei desprezível.
12 Não vos comove isto, a todos vós que passais pelo caminho? Considerai e vede se há dor igual à minha, que veio sobre mim, com que o Senhor me afligiu no dia do furor da sua ira.
13 Lá do alto enviou fogo a meus ossos, o qual se assenhoreou deles; estendeu uma rede aos meus pés, arrojou-me para trás, fez-me assolada e enferma todo o dia.
14 O jugo das minhas transgressões está atado pela sua mão; elas estão entretecidas, subiram sobre o meu pescoço, e ele abateu a minha força; entregou-me o Senhor nas mãos daqueles contra os quais não posso resistir.
15 O Senhor dispersou todos os valentes que estavam comigo; apregoou contra mim um ajuntamento, para esmagar os meus jovens; o Senhor pisou, como num lagar, a virgem filha de Judá.
16 Por estas coisas, choro eu; os meus olhos, os meus olhos se desfazem em águas; porque se afastou de mim o consolador que devia restaurar as minhas forças; os meus filhos estão desolados, porque prevaleceu o inimigo.
17 Estende Sião as mãos, e não há quem a console; ordenou o Senhor acerca de Jacó que os seus vizinhos se tornem seus inimigos; Jerusalém é para eles como coisa imunda.
18 Justo é o Senhor, pois me rebelei contra a sua palavra; ouvi todos os povos e vede a minha dor; as minhas virgens e os meus jovens foram levados para o cativeiro.
19 Chamei os meus amigos, mas eles me enganaram; os meus sacerdotes e os meus anciãos expiraram na cidade, quando estavam à procura de mantimento para restaurarem as suas forças.
20 Olha, Senhor, porque estou angustiada; turbada está a minha alma, o meu coração, transtornado dentro de mim, porque gravemente me rebelei; fora, a espada mata os filhos; em casa, anda a morte.
21 Ouvem que eu suspiro, mas não tenho quem me console; todos os meus inimigos que souberam do meu mal folgam, porque tu o fizeste; mas, em trazendo tu o dia que apregoaste, serão semelhantes a mim.
22 Venha toda a sua iniquidade à tua presença, e faze-lhes como me fizeste a mim por causa de todas as minhas prevaricações; porque os meus gemidos são muitos, e o meu coração está desfalecido.*
1 Como o Senhor cobriu de nuvens, na sua ira, a filha de Sião! Precipitou do céu à terra a glória de Israel e não se lembrou do estrado de seus pés, no dia da sua ira.
2 Devorou o Senhor todas as moradas de Jacó e não se apiedou; derribou no seu furor as fortalezas da filha de Judá; lançou por terra e profanou o reino e os seus príncipes.
3 No furor da sua ira, cortou toda a força de Israel; retirou a sua destra de diante do inimigo; e ardeu contra Jacó, como labareda de fogo que tudo consome em redor.
4 Entesou o seu arco, qual inimigo; firmou a sua destra, como adversário, e destruiu tudo o que era formoso à vista; derramou o seu furor, como fogo, na tenda da filha de Sião.
5 Tornou-se o Senhor como inimigo, devorando Israel; devorou todos os seus palácios, destruiu as suas fortalezas e multiplicou na filha de Judá o pranto e a lamentação.
6 Demoliu com violência o seu tabernáculo, como se fosse uma horta; destruiu o lugar da sua congregação; o Senhor, em Sião, pôs em esquecimento as festas e o sábado e, na indignação da sua ira, rejeitou com desprezo o rei e o sacerdote.
7 Rejeitou o Senhor o seu altar e detestou o seu santuário; entregou nas mãos do inimigo os muros dos seus castelos; deram gritos na Casa do Senhor, como em dia de festa.
8 Intentou o Senhor destruir o muro da filha de Sião; estendeu o cordel e não retirou a sua mão destruidora; fez gemer o antemuro e o muro; eles estão juntamente enfraquecidos.
9 As suas portas caíram por terra; ele quebrou e despedaçou os seus ferrolhos; o seu rei e os seus príncipes estão entre as nações onde já não vigora a lei, nem recebem visão alguma do Senhor os seus profetas.
10 Sentados em terra se acham, silenciosos, os anciãos da filha de Sião; lançam pó sobre a cabeça, cingidos de cilício; as virgens de Jerusalém abaixam a cabeça até ao chão.
11 Com lágrimas se consumiram os meus olhos, turbada está a minha alma, e o meu coração se derramou de angústia por causa da calamidade da filha do meu povo; pois desfalecem os meninos e as crianças de peito pelas ruas da cidade.
12 Dizem às mães: Onde há pão e vinho?, quando desfalecem como o ferido pelas ruas da cidade ou quando exalam a alma nos braços de sua mãe.
13 Que poderei dizer-te? A quem te compararei, ó filha de Jerusalém? A quem te assemelharei, para te consolar a ti, ó virgem filha de Sião? Porque grande como o mar é a tua calamidade; quem te acudirá?
14 Os teus profetas te anunciaram visões falsas e absurdas e não manifestaram a tua maldade, para restaurarem a tua sorte; mas te anunciaram visões de sentenças falsas, que te levaram para o cativeiro.
15 Todos os que passam pelo caminho batem palmas, assobiam e meneiam a cabeça sobre a filha de Jerusalém: É esta a cidade que denominavam a perfeição da formosura, a alegria de toda a terra?
16 Todos os teus inimigos abrem contra ti a boca, assobiam e rangem os dentes; dizem: Devoramo-la; certamente, este é o dia que esperávamos; achamo-lo e vimo-lo.
17 Fez o Senhor o que intentou; cumpriu a ameaça que pronunciou desde os dias da antiguidade; derrubou e não se apiedou; fez que o inimigo se alegrasse por tua causa e exaltou o poder dos teus adversários.
18 O coração de Jerusalém clama ao Senhor. Ó muralha da filha de Sião, corram as tuas lágrimas como um ribeiro, de dia e de noite, não te dês descanso, nem pare de chorar a menina de teus olhos!
19 Levanta-te, clama de noite no princípio das vigílias; derrama, como água, o coração perante o Senhor; levanta a ele as mãos, pela vida de teus filhinhos, que desfalecem de fome à entrada de todas as ruas.
20 Vê, ó Senhor, e considera a quem fizeste assim! Hão de as mulheres comer o fruto de si mesmas, as crianças do seu carinho? Ou se matará no santuário do Senhor o sacerdote e o profeta?
21 Jazem por terra pelas ruas o moço e o velho; as minhas virgens e os meus jovens vieram a cair à espada; tu os mataste no dia da tua ira, fizeste matança e não te apiedaste.
22 Convocaste de toda parte terrores contra mim, como num dia de solenidade; não houve, no dia da ira do Senhor, quem escapasse ou ficasse; aqueles do meu carinho os quais eu criei, o meu inimigo os consumiu.*
1 Eu sou o homem que viu a aflição pela vara do furor de Deus.
2 Ele me levou e me fez andar em trevas e não na luz.
3 Deveras ele volveu contra mim a mão, de contínuo, todo o dia.
4 Fez envelhecer a minha carne e a minha pele, despedaçou os meus ossos.
5 Edificou contra mim e me cercou de veneno e de dor.
6 Fez-me habitar em lugares tenebrosos, como os que estão mortos para sempre.
7 Cercou-me de um muro, e já não posso sair; agravou-me com grilhões de bronze.
8 Ainda quando clamo e grito, ele não admite a minha oração.
9 Fechou os meus caminhos com pedras lavradas, fez tortuosas as minhas veredas.
10 Fez-se-me como urso à espreita, um leão de emboscada.
11 Desviou os meus caminhos e me fez em pedaços; deixou-me assolado.
12 Entesou o seu arco e me pôs como alvo à flecha.
13 Fez que me entrassem no coração as flechas da sua aljava.
14 Fui feito objeto de escárnio para todo o meu povo e a sua canção, todo o dia.
15 Fartou-me de amarguras, saciou-me de absinto.
16 Fez-me quebrar com pedrinhas de areia os meus dentes, cobriu-me de cinza.
17 Afastou a paz de minha alma; esqueci-me do bem.
18 Então, disse eu: já pereceu a minha glória, como também a minha esperança no Senhor.
19 Lembra-te da minha aflição e do meu pranto, do absinto e do veneno.
20 Minha alma, continuamente, os recorda e se abate dentro de mim.
21 Quero trazer à memória o que me pode dar esperança.
22 As misericórdias do Senhor são a causa de não sermos consumidos, porque as suas misericórdias não têm fim;
23 renovam-se cada manhã. Grande é a tua fidelidade.
24 A minha porção é o Senhor, diz a minha alma; portanto, esperarei nele.
25 Bom é o Senhor para os que esperam por ele, para a alma que o busca.
26 Bom é aguardar a salvação do Senhor, e isso, em silêncio.
27 Bom é para o homem suportar o jugo na sua mocidade.
28 Assente-se solitário e fique em silêncio; porquanto esse jugo Deus pôs sobre ele;
29 ponha a boca no pó; talvez ainda haja esperança.
30 Dê a face ao que o fere; farte-se de afronta.
31 O Senhor não rejeitará para sempre;
32 pois, ainda que entristeça a alguém, usará de compaixão segundo a grandeza das suas misericórdias;
33 porque não aflige, nem entristece de bom grado os filhos dos homens.
34 Pisar debaixo dos pés a todos os presos da terra,
35 perverter o direito do homem perante o Altíssimo,
36 subverter ao homem no seu pleito, não o veria o Senhor?
37 Quem é aquele que diz, e assim acontece, quando o Senhor o não mande?
38 Acaso, não procede do Altíssimo tanto o mal como o bem?
39 Por que, pois, se queixa o homem vivente? Queixe-se cada um dos seus próprios pecados.
40 Esquadrinhemos os nossos caminhos, provemo-los e voltemos para o Senhor.
41 Levantemos o coração, juntamente com as mãos, para Deus nos céus, dizendo:
42 Nós prevaricamos e fomos rebeldes, e tu não nos perdoaste.
43 Cobriste-nos de ira e nos perseguiste; e sem piedade nos mataste.
44 De nuvens te encobriste para que não passe a nossa oração.
45 Como cisco e refugo nos puseste no meio dos povos.
46 Todos os nossos inimigos abriram contra nós a boca.
47 Sobre nós vieram o temor e a cova, a assolação e a ruína.
48 Dos meus olhos se derramam torrentes de águas, por causa da destruição da filha do meu povo.
49 Os meus olhos choram, não cessam, e não há descanso,
50 até que o Senhor atenda e veja lá do céu.
51 Os meus olhos entristecem a minha alma, por causa de todas as filhas da minha cidade.
52 Caçaram-me, como se eu fosse ave, os que sem motivo são meus inimigos.
53 Para me destruírem, lançaram-me na cova e atiraram pedras sobre mim.
54 Águas correram sobre a minha cabeça; então, disse: estou perdido!
55 Da mais profunda cova, Senhor, invoquei o teu nome.
56 Ouviste a minha voz; não escondas o ouvido aos meus lamentos, ao meu clamor.
57 De mim te aproximaste no dia em que te invoquei; disseste: Não temas.
58 Pleiteaste, Senhor, a causa da minha alma, remiste a minha vida.
59 Viste, Senhor, a injustiça que me fizeram; julga a minha causa.
60 Viste a sua vingança toda, todos os seus pensamentos contra mim.
61 Ouviste as suas afrontas, Senhor, todos os seus pensamentos contra mim;
62 as acusações dos meus adversários e o seu murmurar contra mim, o dia todo.
63 Observa-os quando se assentam e quando se levantam; eu sou objeto da sua canção.
64 Tu lhes darás a paga, Senhor, segundo a obra das suas mãos.
65 Tu lhes darás cegueira de coração, a tua maldição imporás sobre eles.
66 Na tua ira, os perseguirás, e eles serão eliminados de debaixo dos céus do Senhor.*
1 Como se escureceu o ouro! Como se mudou o ouro refinado! Como estão espalhadas as pedras do santuário pelas esquinas de todas as ruas!
2 Os nobres filhos de Sião, comparáveis a puro ouro, como são agora reputados por objetos de barro, obra das mãos de oleiro!
3 Até os chacais dão o peito, dão de mamar a seus filhos; mas a filha do meu povo tornou-se cruel como os avestruzes no deserto.
4 A língua da criança que mama fica pegada, pela sede, ao céu da boca; os meninos pedem pão, e ninguém há que lho dê.
5 Os que se alimentavam de comidas finas desfalecem nas ruas; os que se criaram entre escarlata se apegam aos monturos.
6 Porque maior é a maldade da filha do meu povo do que o pecado de Sodoma, que foi subvertida como num momento, sem o emprego de mãos nenhumas.
7 Os seus príncipes eram mais alvos do que a neve, mais brancos do que o leite; eram mais ruivos de corpo do que os corais e tinham a formosura da safira.
8 Mas, agora, escureceu-se-lhes o aspecto mais do que a fuligem; não são conhecidos nas ruas; a sua pele se lhes pegou aos ossos, secou-se como uma madeira.
9 Mais felizes foram as vítimas da espada do que as vítimas da fome; porque estas se definham atingidas mortalmente pela falta do produto dos campos.
10 As mãos das mulheres outrora compassivas cozeram seus próprios filhos; estes lhes serviram de alimento na destruição da filha do meu povo.
11 Deu o Senhor cumprimento à sua indignação, derramou o ardor da sua ira; acendeu fogo em Sião, que consumiu os seus fundamentos.
12 Não creram os reis da terra, nem todos os moradores do mundo, que entrasse o adversário e o inimigo pelas portas de Jerusalém.
13 Foi por causa dos pecados dos seus profetas, das maldades dos seus sacerdotes que se derramou no meio dela o sangue dos justos.
14 Erram como cegos nas ruas, andam contaminados de sangue, de tal sorte que ninguém lhes pode tocar nas roupas.
15 Apartai-vos, imundos! — gritavam-lhes; apartai-vos, apartai-vos, não toqueis! Quando fugiram errantes, dizia-se entre as nações: Jamais habitarão aqui.
16 A ira do Senhor os espalhou; ele jamais atentará para eles; o inimigo não honra os sacerdotes, nem se compadece dos anciãos.
17 Os nossos olhos ainda desfalecem, esperando vão socorro; temos olhado das vigias para um povo que não pode livrar.
18 Espreitavam os nossos passos, de maneira que não podíamos andar pelas nossas praças; aproximava-se o nosso fim, os nossos dias se cumpriam, era chegado o nosso fim.
19 Os nossos perseguidores foram mais ligeiros do que as aves dos céus; sobre os montes nos perseguiram, no deserto nos armaram ciladas.
20 O fôlego da nossa vida, o ungido do Senhor, foi preso nos forjes deles; dele dizíamos: debaixo da sua sombra, viveremos entre as nações.
21 Regozija-te e alegra-te, ó filha de Edom, que habitas na terra de Uz; o cálice se passará também a ti; embebedar-te-ás e te desnudarás.
22 O castigo da tua maldade está consumado, ó filha de Sião; o Senhor nunca mais te levará para o exílio; a tua maldade, ó filha de Edom, descobrirá os teus pecados.*
1 Lembra-te, Senhor, do que nos tem sucedido; considera e olha para o nosso opróbrio.
2 A nossa herança passou a estranhos, e as nossas casas, a estrangeiros;
3 somos órfãos, já não temos pai, nossas mães são como viúvas.
4 A nossa água, por dinheiro a bebemos, por preço vem a nossa lenha.
5 Os nossos perseguidores estão sobre o nosso pescoço; estamos exaustos e não temos descanso.
6 Submetemo-nos aos egípcios e aos assírios, para nos fartarem de pão.
7 Nossos pais pecaram e já não existem; nós é que levamos o castigo das suas iniquidades.
8 Escravos dominam sobre nós; ninguém há que nos livre das suas mãos.
9 Com perigo de nossa vida, providenciamos o nosso pão, por causa da espada do deserto.
10 Nossa pele se esbraseia como um forno, por causa do ardor da fome.
11 Forçaram as mulheres em Sião; as virgens, nas cidades de Judá.
12 Os príncipes foram por eles enforcados, as faces dos velhos não foram reverenciadas.
13 Os jovens levaram a mó, os meninos tropeçaram debaixo das cargas de lenha;
14 os anciãos já não se assentam na porta, os jovens já não cantam.
15 Cessou o júbilo de nosso coração, converteu-se em lamentações a nossa dança.
16 Caiu a coroa da nossa cabeça; ai de nós, porque pecamos!
17 Por isso, caiu doente o nosso coração; por isso, se escureceram os nossos olhos.
18 Pelo monte Sião, que está assolado, andam as raposas.
19 Tu, Senhor, reinas eternamente, o teu trono subsiste de geração em geração.
20 Por que te esquecerias de nós para sempre? Por que nos desampararias por tanto tempo?
21 Converte-nos a ti, Senhor, e seremos convertidos; renova os nossos dias como dantes.
22 Por que nos rejeitarias totalmente? Por que te enfurecerias sobremaneira contra nós outros?
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Lamentações','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)