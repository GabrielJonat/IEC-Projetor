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
1 Cântico dos cânticos de Salomão.
2 Beija-me com os beijos de tua boca; porque melhor é o teu amor do que o vinho.
3 Suave é o aroma dos teus unguentos, como unguento derramado é o teu nome; por isso, as donzelas te amam.
4 Leva-me após ti, apressemo-nos. O rei me introduziu nas suas recâmaras. Em ti nos regozijaremos e nos alegraremos; do teu amor nos lembraremos, mais do que do vinho; não é sem razão que te amam.
5 Eu estou morena e formosa, ó filhas de Jerusalém, como as tendas de Quedar, como as cortinas de Salomão.
6 Não olheis para o eu estar morena, porque o sol me queimou. Os filhos de minha mãe se indignaram contra mim e me puseram por guarda de vinhas; a vinha, porém, que me pertence, não a guardei.
7 Dize-me, ó amado de minha alma: onde apascentas o teu rebanho, onde o fazes repousar pelo meio-dia, para que não ande eu vagando junto ao rebanho dos teus companheiros?
8 Se tu não o sabes, ó mais formosa entre as mulheres, sai-te pelas pisadas dos rebanhos e apascenta os teus cabritos junto às tendas dos pastores.
9 Às éguas dos carros de Faraó te comparo, ó querida minha.
10 Formosas são as tuas faces entre os teus enfeites, o teu pescoço, com os colares.
11 Enfeites de ouro te faremos, com incrustações de prata.
12 Enquanto o rei está assentado à sua mesa, o meu nardo exala o seu perfume.
13 O meu amado é para mim um saquitel de mirra, posto entre os meus seios.
14 Como um racimo de flores de hena nas vinhas de En-Gedi, é para mim o meu amado.
15 Eis que és formosa, ó querida minha, eis que és formosa; os teus olhos são como os das pombas.
16 Como és formoso, amado meu, como és amável! O nosso leito é de viçosas folhas,
17 as traves da nossa casa são de cedro, e os seus caibros, de cipreste.*
1 Eu sou a rosa de Sarom, o lírio dos vales.
2 Qual o lírio entre os espinhos, tal é a minha querida entre as donzelas.
3 Qual a macieira entre as árvores do bosque, tal é o meu amado entre os jovens; desejo muito a sua sombra e debaixo dela me assento, e o seu fruto é doce ao meu paladar.
4 Leva-me à sala do banquete, e o seu estandarte sobre mim é o amor.
5 Sustentai-me com passas, confortai-me com maçãs, pois desfaleço de amor.
6 A sua mão esquerda esteja debaixo da minha cabeça, e a direita me abrace.
7 Conjuro-vos, ó filhas de Jerusalém, pelas gazelas e cervas do campo, que não acordeis, nem desperteis o amor, até que este o queira.
8 Ouço a voz do meu amado; ei-lo aí galgando os montes, pulando sobre os outeiros.
9 O meu amado é semelhante ao gamo ou ao filho da gazela; eis que está detrás da nossa parede, olhando pelas janelas, espreitando pelas grades.
10 O meu amado fala e me diz:
Levanta-te, querida minha, formosa minha, e vem.
11 Porque eis que passou o inverno, cessou a chuva e se foi;
12 aparecem as flores na terra, chegou o tempo de cantarem as aves, e a voz da rola ouve-se em nossa terra.
13 A figueira começou a dar seus figos, e as vides em flor exalam o seu aroma; levanta-te, querida minha, formosa minha, e vem.
14 Pomba minha, que andas pelas fendas dos penhascos, no esconderijo das rochas escarpadas, mostra-me o rosto, faze-me ouvir a tua voz, porque a tua voz é doce, e o teu rosto, amável.
15 Apanhai-me as raposas, as raposinhas, que devastam os vinhedos, porque as nossas vinhas estão em flor.
16 O meu amado é meu, e eu sou dele; ele apascenta o seu rebanho entre os lírios.
17 Antes que refresque o dia e fujam as sombras, volta, amado meu; faze-te semelhante ao gamo ou ao filho das gazelas sobre os montes escabrosos.*
1 De noite, no meu leito, busquei o amado de minha alma, busquei-o e não o achei.
2 Levantar-me-ei, pois, e rodearei a cidade, pelas ruas e pelas praças; buscarei o amado da minha alma. Busquei-o e não o achei.
3 Encontraram-me os guardas, que rondavam pela cidade. Então, lhes perguntei: vistes o amado da minha alma?
4 Mal os deixei, encontrei logo o amado da minha alma; agarrei-me a ele e não o deixei ir embora, até que o fiz entrar em casa de minha mãe e na recâmara daquela que me concebeu.
5 Conjuro-vos, ó filhas de Jerusalém, pelas gazelas e cervas do campo, que não acordeis, nem desperteis o amor, até que este o queira.
6 Que é isso que sobe do deserto, como colunas de fumaça, perfumado de mirra, e de incenso, e de toda sorte de pós aromáticos do mercador?
7 É a liteira de Salomão; sessenta valentes estão ao redor dela, dos valentes de Israel.
8 Todos sabem manejar a espada e são destros na guerra; cada um leva a espada à cinta, por causa dos temores noturnos.
9 O rei Salomão fez para si um palanquim de madeira do Líbano.
10 Fez-lhe as colunas de prata, a espalda de ouro, o assento de púrpura, e tudo interiormente ornado com amor pelas filhas de Jerusalém.
11 Saí, ó filhas de Sião, e contemplai ao rei Salomão com a coroa com que sua mãe o coroou no dia do seu desposório, no dia do júbilo do seu coração.*
1 Como és formosa, querida minha, como és formosa! Os teus olhos são como os das pombas e brilham através do teu véu. Os teus cabelos são como o rebanho de cabras que descem ondeantes do monte de Gileade.
2 São os teus dentes como o rebanho das ovelhas recém-tosquiadas, que sobem do lavadouro, e das quais todas produzem gêmeos, e nenhuma delas há sem crias.
3 Os teus lábios são como um fio de escarlata, e tua boca é formosa; as tuas faces, como romã partida, brilham através do véu.
4 O teu pescoço é como a torre de Davi, edificada para arsenal; mil escudos pendem dela, todos broquéis de soldados valorosos.
5 Os teus dois seios são como duas crias, gêmeas de uma gazela, que se apascentam entre os lírios.
6 Antes que refresque o dia, e fujam as sombras, irei ao monte da mirra e ao outeiro do incenso.
7 Tu és toda formosa, querida minha, e em ti não há defeito.
8 Vem comigo do Líbano, noiva minha, vem comigo do Líbano; olha do cimo do Amana, do cimo do Senir e do Hermom, dos covis dos leões, dos montes dos leopardos.
9 Arrebataste-me o coração, minha irmã, noiva minha; arrebataste-me o coração com um só dos teus olhares, com uma só pérola do teu colar.
10 Que belo é o teu amor, ó minha irmã, noiva minha! Quanto melhor é o teu amor do que o vinho, e o aroma dos teus unguentos do que toda sorte de especiarias!
11 Os teus lábios, noiva minha, destilam mel. Mel e leite se acham debaixo da tua língua, e a fragrância dos teus vestidos é como a do Líbano.
12 Jardim fechado és tu, minha irmã, noiva minha, manancial recluso, fonte selada.
13 Os teus renovos são um pomar de romãs, com frutos excelentes: a hena e o nardo;
14 o nardo e o açafrão, o cálamo e o cinamomo, com toda a sorte de árvores de incenso, a mirra e o aloés, com todas as principais especiarias.
15 És fonte dos jardins, poço das águas vivas, torrentes que correm do Líbano!
16 Levanta-te, vento norte, e vem tu, vento sul; assopra no meu jardim, para que se derramem os seus aromas. Ah! Venha o meu amado para o seu jardim e coma os seus frutos excelentes!*
1 Já entrei no meu jardim, minha irmã, noiva minha; colhi a minha mirra com a especiaria, comi o meu favo com o mel, bebi o meu vinho com o leite. Comei e bebei, amigos; bebei fartamente, ó amados.
2 Eu dormia, mas o meu coração velava; eis a voz do meu amado, que está batendo:
Abre-me, minha irmã, querida minha, pomba minha, imaculada minha, porque a minha cabeça está cheia de orvalho, os meus cabelos, das gotas da noite.
3 Já despi a minha túnica, hei de vesti-la outra vez? Já lavei os pés, tornarei a sujá-los?
4 O meu amado meteu a mão por uma fresta, e o meu coração se comoveu por amor dele.
5 Levantei-me para abrir ao meu amado; as minhas mãos destilavam mirra, e os meus dedos mirra preciosa sobre a maçaneta do ferrolho.
6 Abri ao meu amado, mas já ele se retirara e tinha ido embora; a minha alma se derreteu quando, antes, ele me falou; busquei-o e não o achei; chamei-o, e não me respondeu.
7 Encontraram-me os guardas que rondavam pela cidade; espancaram-me e feriram-me; tiraram-me o manto os guardas dos muros.
8 Conjuro-vos, ó filhas de Jerusalém, se encontrardes o meu amado, que lhe direis? Que desfaleço de amor.
9 Que é o teu amado mais do que outro amado, ó tu, a mais formosa entre as mulheres? Que é o teu amado mais do que outro amado, que tanto nos conjuras?
10 O meu amado é alvo e rosado, o mais distinguido entre dez mil.
11 A sua cabeça é como o ouro mais apurado, os seus cabelos, cachos de palmeira, são pretos como o corvo.
12 Os seus olhos são como os das pombas junto às correntes das águas, lavados em leite, postos em engaste.
13 As suas faces são como um canteiro de bálsamo, como colinas de ervas aromáticas; os seus lábios são lírios que gotejam mirra preciosa;
14 as suas mãos, cilindros de ouro, embutidos de jacintos; o seu ventre, como alvo marfim, coberto de safiras.
15 As suas pernas, colunas de mármore, assentadas em bases de ouro puro; o seu aspecto, como o Líbano, esbelto como os cedros.
16 O seu falar é muitíssimo doce; sim, ele é totalmente desejável. Tal é o meu amado, tal, o meu esposo, ó filhas de Jerusalém.*
1 Para onde foi o teu amado, ó mais formosa entre as mulheres? Que rumo tomou o teu amado? E o buscaremos contigo.
Esposa
2 O meu amado desceu ao seu jardim, aos canteiros de bálsamo, para pastorear nos jardins e para colher os lírios.
3 Eu sou do meu amado, e o meu amado é meu; ele pastoreia entre os lírios.
4 Formosa és, querida minha, como Tirza, aprazível como Jerusalém, formidável como um exército com bandeiras.
5 Desvia de mim os olhos, porque eles me perturbam. Os teus cabelos descem ondeantes como o rebanho das cabras de Gileade.
6 São os teus dentes como o rebanho de ovelhas que sobem do lavadouro, e das quais todas produzem gêmeos, e nenhuma delas há sem crias.
7 As tuas faces, como romã partida, brilham através do véu.
8 Sessenta são as rainhas, oitenta, as concubinas, e as virgens, sem número.
9 Mas uma só é a minha pomba, a minha imaculada, de sua mãe, a única, a predileta daquela que a deu à luz; viram-na as donzelas e lhe chamaram ditosa; viram-na as rainhas e as concubinas e a louvaram.
10 Quem é esta que aparece como a alva do dia, formosa como a lua, pura como o sol, formidável como um exército com bandeiras?
11 Desci ao jardim das nogueiras, para mirar os renovos do vale, para ver se brotavam as vides, se floresciam as romeiras.
12 Não sei como, imaginei-me no carro do meu nobre povo!
13 Volta, volta, ó sulamita, volta, volta, para que nós te contemplemos. Por que quereis contemplar a sulamita na dança de Maanaim?*
1 Que formosos são os teus passos dados de sandálias, ó filha do príncipe! Os meneios dos teus quadris são como colares trabalhados por mãos de artista.
2 O teu umbigo é taça redonda, a que não falta bebida; o teu ventre é monte de trigo, cercado de lírios.
3 Os teus dois seios, como duas crias, gêmeas de uma gazela.
4 O teu pescoço, como torre de marfim; os teus olhos são as piscinas de Hesbom, junto à porta de Bate-Rabim; o teu nariz, como a torre do Líbano, que olha para Damasco.
5 A tua cabeça é como o monte Carmelo, a tua cabeleira, como a púrpura; um rei está preso nas tuas tranças.
6 Quão formosa e quão aprazível és, ó amor em delícias!
7 Esse teu porte é semelhante à palmeira, e os teus seios, a seus cachos.
8 Dizia eu: subirei à palmeira, pegarei em seus ramos. Sejam os teus seios como os cachos da vide, e o aroma da tua respiração, como o das maçãs.
9 Os teus beijos são como o bom vinho,
vinho que se escoa suavemente para o meu amado, deslizando entre seus lábios e dentes.
10 Eu sou do meu amado, e ele tem saudades de mim.
11 Vem, ó meu amado, saiamos ao campo, passemos as noites nas aldeias.
12 Levantemo-nos cedo de manhã para ir às vinhas; vejamos se florescem as vides, se se abre a flor, se já brotam as romeiras; dar-te-ei ali o meu amor.
13 As mandrágoras exalam o seu perfume, e às nossas portas há toda sorte de excelentes frutos, novos e velhos; eu tos reservei, ó meu amado.*
1 Tomara fosses como meu irmão, que mamou os seios de minha mãe! Quando te encontrasse na rua, beijar-te-ia, e não me desprezariam!
2 Levar-te-ia e te introduziria na casa de minha mãe, e tu me ensinarias; eu te daria a beber vinho aromático e mosto das minhas romãs.
3 A sua mão esquerda estaria debaixo da minha cabeça, e a sua direita me abraçaria.
4 Conjuro-vos, ó filhas de Jerusalém, que não acordeis, nem desperteis o amor, até que este o queira.
5 Quem é esta que sobe do deserto e vem encostada ao seu amado?
Debaixo da macieira te despertei, ali esteve tua mãe com dores; ali esteve com dores aquela que te deu à luz.
6 Põe-me como selo sobre o teu coração, como selo sobre o teu braço, porque o amor é forte como a morte, e duro como a sepultura, o ciúme; as suas brasas são brasas de fogo, são veementes labaredas.
7 As muitas águas não poderiam apagar o amor, nem os rios, afogá-lo; ainda que alguém desse todos os bens da sua casa pelo amor, seria de todo desprezado.
8 Temos uma irmãzinha que ainda não tem seios; que faremos a esta nossa irmã, no dia em que for pedida?
9 Se ela for um muro, edificaremos sobre ele uma torre de prata; se for uma porta, cercá-la-emos com tábuas de cedro.
10 Eu sou um muro, e os meus seios, como as suas torres; sendo eu assim, fui tida por digna da confiança do meu amado.
11 Teve Salomão uma vinha em Baal-Hamom; entregou-a a uns guardas, e cada um lhe trazia pelo seu fruto mil peças de prata.
12 A vinha que me pertence está ao meu dispor; tu, ó Salomão, terás os mil siclos, e os que guardam o fruto dela, duzentos.
13 Ó tu que habitas nos jardins, os companheiros estão atentos para ouvir a tua voz; faze-me, pois, também ouvi-la.
14 Vem depressa, amado meu, faze-te semelhante ao gamo ou ao filho da gazela, que saltam sobre os montes aromáticos.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Cântico','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)