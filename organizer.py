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
1 Palavra do Senhor, que foi dirigida a Oseias, filho de Beeri, nos dias de Uzias, Jotão, Acaz e Ezequias, reis de Judá, e nos dias de Jeroboão, filho de Joás, rei de Israel.
2 Quando, pela primeira vez, falou o Senhor por intermédio de Oseias, então, o Senhor lhe disse: Vai, toma uma mulher de prostituições e terás filhos de prostituição, porque a terra se prostituiu, desviando-se do Senhor.
3 Foi-se, pois, e tomou a Gômer, filha de Diblaim, e ela concebeu e lhe deu um filho.
4 Disse-lhe o Senhor: Põe-lhe o nome de Jezreel, porque, daqui a pouco, castigarei, pelo sangue de Jezreel, a casa de Jeú e farei cessar o reino da casa de Israel.
5 Naquele dia, quebrarei o arco de Israel no vale de Jezreel.
6 Tornou ela a conceber e deu à luz uma filha. Disse o Senhor a Oseias: Põe-lhe o nome de Desfavorecida, porque eu não mais tornarei a favorecer a casa de Israel, para lhe perdoar.
7 Porém da casa de Judá me compadecerei e os salvarei pelo Senhor, seu Deus, pois não os salvarei pelo arco, nem pela espada, nem pela guerra, nem pelos cavalos, nem pelos cavaleiros.
8 Depois de haver desmamado a Desfavorecida, concebeu e deu à luz um filho.
9 Disse o Senhor a Oseias: Põe-lhe o nome de Não-Meu-Povo, porque vós não sois meu povo, nem eu serei vosso Deus.
10 Todavia, o número dos filhos de Israel será como a areia do mar, que se não pode medir, nem contar; e acontecerá que, no lugar onde se lhes dizia: Vós não sois meu povo, se lhes dirá: Vós sois filhos do Deus vivo.
11 Os filhos de Judá e os filhos de Israel se congregarão, e constituirão sobre si uma só cabeça, e subirão da terra, porque grande será o dia de Jezreel.*
1 Chamai a vosso irmão Meu-Povo e a vossa irmã, Favor.  
2 Repreendei vossa mãe, repreendei-a, porque ela não é minha mulher, e eu não sou seu marido, para que ela afaste as suas prostituições de sua presença e os seus adultérios de entre os seus seios;
3 para que eu não a deixe despida, e a ponha como no dia em que nasceu, e a torne semelhante a um deserto, e a faça como terra seca, e a mate à sede,
4 e não me compadeça de seus filhos, porque são filhos de prostituições.
5 Pois sua mãe se prostituiu; aquela que os concebeu houve-se torpemente, porque diz: Irei atrás de meus amantes, que me dão o meu pão e a minha água, a minha lã e o meu linho, o meu óleo e as minhas bebidas.
6 Portanto, eis que cercarei o seu caminho com espinhos; e levantarei um muro contra ela, para que ela não ache as suas veredas.
7 Ela irá em seguimento de seus amantes, porém não os alcançará; buscá-los-á, sem, contudo, os achar; então, dirá: Irei e tornarei para o meu primeiro marido, porque melhor me ia então do que agora.
8 Ela, pois, não soube que eu é que lhe dei o trigo, e o vinho, e o óleo, e lhe multipliquei a prata e o ouro, que eles usaram para Baal.
9 Portanto, tornar-me-ei, e reterei, a seu tempo, o meu trigo e o meu vinho, e arrebatarei a minha lã e o meu linho, que lhe deviam cobrir a nudez.
10 Agora, descobrirei as suas vergonhas aos olhos dos seus amantes, e ninguém a livrará da minha mão.
11 Farei cessar todo o seu gozo, as suas Festas de Lua Nova, os seus sábados e todas as suas solenidades.
12 Devastarei a sua vide e a sua figueira, de que ela diz: Esta é a paga que me deram os meus amantes; eu, pois, farei delas um bosque, e as bestas-feras do campo as devorarão.
13 Castigá-la-ei pelos dias dos baalins, nos quais lhes queimou incenso, e se adornou com as suas arrecadas e com as suas joias, e andou atrás de seus amantes, mas de mim se esqueceu, diz o Senhor.
14 Portanto, eis que eu a atrairei, e a levarei para o deserto, e lhe falarei ao coração.
15 E lhe darei, dali, as suas vinhas e o vale de Acor por porta de esperança; será ela obsequiosa como nos dias da sua mocidade e como no dia em que subiu da terra do Egito.
16 Naquele dia, diz o Senhor, ela me chamará: Meu marido e já não me chamará: Meu Baal.
17 Da sua boca tirarei os nomes dos baalins, e não mais se lembrará desses nomes.
18 Naquele dia, farei a favor dela aliança com as bestas-feras do campo, e com as aves do céu, e com os répteis da terra; e tirarei desta o arco, e a espada, e a guerra e farei o meu povo repousar em segurança.
19 Desposar-te-ei comigo para sempre; desposar-te-ei comigo em justiça, e em juízo, e em benignidade, e em misericórdias;
20 desposar-te-ei comigo em fidelidade, e conhecerás ao Senhor.
21 Naquele dia, eu serei obsequioso, diz o Senhor, obsequioso aos céus, e estes, à terra;
22 a terra, obsequiosa ao trigo, e ao vinho, e ao óleo; e estes, a Jezreel.
23 Semearei Israel para mim na terra e compadecer-me-ei da Desfavorecida; e a Não-Meu-Povo direi: Tu és o meu povo! Ele dirá: Tu és o meu Deus!*
1 Disse-me o Senhor: Vai outra vez, ama uma mulher, amada de seu amigo e adúltera, como o Senhor ama os filhos de Israel, embora eles olhem para outros deuses e amem bolos de passas.
2 Comprei-a, pois, para mim por quinze peças de prata e um ômer e meio de cevada;
3 e lhe disse: tu esperarás por mim muitos dias; não te prostituirás, nem serás de outro homem; assim também eu esperarei por ti.
4 Porque os filhos de Israel ficarão por muitos dias sem rei, sem príncipe, sem sacrifício, sem coluna, sem estola sacerdotal ou ídolos do lar.
5 Depois, tornarão os filhos de Israel, e buscarão ao Senhor, seu Deus, e a Davi, seu rei; e, nos últimos dias, tremendo, se aproximarão do Senhor e da sua bondade.*
1 Ouvi a palavra do Senhor, vós, filhos de Israel, porque o Senhor tem uma contenda com os habitantes da terra, porque nela não há verdade, nem amor, nem conhecimento de Deus.
2 O que só prevalece é perjurar, mentir, matar, furtar e adulterar, e há arrombamentos e homicídios sobre homicídios.
3 Por isso, a terra está de luto, e todo o que mora nela desfalece, com os animais do campo e com as aves do céu; e até os peixes do mar perecem.
4 Todavia, ninguém contenda, ninguém repreenda; porque o teu povo é como os sacerdotes aos quais acusa.
5 Por isso, tropeçarás de dia, e o profeta contigo tropeçará de noite; e destruirei a tua mãe.
6 O meu povo está sendo destruído, porque lhe falta o conhecimento. Porque tu, sacerdote, rejeitaste o conhecimento, também eu te rejeitarei, para que não sejas sacerdote diante de mim; visto que te esqueceste da lei do teu Deus, também eu me esquecerei de teus filhos.
7 Quanto mais estes se multiplicaram, tanto mais contra mim pecaram; eu mudarei a sua honra em vergonha.
8 Alimentam-se do pecado do meu povo e da maldade dele têm desejo ardente.
9 Por isso, como é o povo, assim é o sacerdote; castigá-lo-ei pelo seu procedimento e lhe darei o pago das suas obras.
10 Comerão, mas não se fartarão; entregar-se-ão à sensualidade, mas não se multiplicarão, porque ao Senhor deixaram de adorar.
11 A sensualidade, o vinho e o mosto tiram o entendimento.
12 O meu povo consulta o seu pedaço de madeira, e a sua vara lhe dá resposta; porque um espírito de prostituição os enganou, eles, prostituindo-se, abandonaram o seu Deus.
13 Sacrificam sobre o cimo dos montes e queimam incenso sobre os outeiros, debaixo do carvalho, dos choupos e dos terebintos, porque é boa a sua sombra; por isso, vossas filhas se prostituem, e as vossas noras adulteram.
14 Não castigarei vossas filhas, que se prostituem, nem vossas noras, quando adulteram, porque os homens mesmos se retiram com as meretrizes e com as prostitutas cultuais sacrificam, pois o povo que não tem entendimento corre para a sua perdição.
15 Ainda que tu, ó Israel, queres prostituir-te, contudo, não se faça culpado Judá; nem venhais a Gilgal e não subais a Bete-Áven, nem jureis, dizendo: Vive o Senhor.
16 Como vaca rebelde, se rebelou Israel; será que o Senhor o apascenta como a um cordeiro em vasta campina?
17 Efraim está entregue aos ídolos; é deixá-lo.
18 Tendo acabado de beber, eles se entregam à prostituição; os seus príncipes amam apaixonadamente a desonra.
19 O vento os envolveu nas suas asas; e envergonhar-se-ão por causa dos seus sacrifícios.*
1 Ouvi isto, ó sacerdotes; escutai, ó casa de Israel; e dai ouvidos, ó casa do rei, porque este juízo é contra vós outros, visto que fostes um laço em Mispa e rede estendida sobre o Tabor.
2 Na prática de excessos, vos aprofundastes; mas eu castigarei a todos eles.
3 Conheço a Efraim, e Israel não me está oculto; porque, agora, te tens prostituído, ó Efraim, e Israel está contaminado.
4 O seu proceder não lhes permite voltar para o seu Deus, porque um espírito de prostituição está no meio deles, e não conhecem ao Senhor.
5 A soberba de Israel, abertamente, o acusa; Israel e Efraim cairão por causa da sua iniquidade, e Judá cairá juntamente com eles.
6 Estes irão com os seus rebanhos e o seu gado à procura do Senhor, porém não o acharão; ele se retirou deles.
7 Aleivosamente se houveram contra o Senhor, porque geraram filhos bastardos; agora, a Festa da Lua Nova os consumirá com as suas porções.
8 Tocai a trombeta em Gibeá e em Ramá tocai a rebate! Levantai gritos em Bete-Áven! Cuidado, Benjamim!
9 Efraim tornar-se-á assolação no dia do castigo; entre as tribos de Israel, tornei conhecido o que se cumprirá.
10 Os príncipes de Judá são como os que mudam os marcos; derramarei, pois, o meu furor sobre eles como água.
11 Efraim está oprimido e quebrantado pelo castigo, porque foi do seu agrado andar após a vaidade.
12 Portanto, para Efraim serei como a traça e para a casa de Judá, como a podridão.
13 Quando Efraim viu a sua enfermidade, e Judá, a sua chaga, subiu Efraim à Assíria e se dirigiu ao rei principal, que o acudisse; mas ele não poderá curá-los, nem sarar a sua chaga.
14 Porque para Efraim serei como um leão e como um leãozinho, para a casa de Judá; eu, eu mesmo, os despedaçarei e ir-me-ei embora; arrebatá-los-ei, e não haverá quem os livre.
15 Irei e voltarei para o meu lugar, até que se reconheçam culpados e busquem a minha face; estando eles angustiados, cedo me buscarão, dizendo:*
1 Vinde, e tornemos para o Senhor, porque ele nos despedaçou e nos sarará; fez a ferida e a ligará.
2 Depois de dois dias, nos revigorará; ao terceiro dia, nos levantará, e viveremos diante dele.
3 Conheçamos e prossigamos em conhecer ao Senhor; como a alva, a sua vinda é certa; e ele descerá sobre nós como a chuva, como chuva serôdia que rega a terra.
4 Que te farei, ó Efraim? Que te farei, ó Judá? Porque o vosso amor é como a nuvem da manhã e como o orvalho da madrugada, que cedo passa.
5 Por isso, os abati por meio dos profetas; pela palavra da minha boca, os matei; e os meus juízos sairão como a luz.
6 Pois misericórdia quero, e não sacrifício, e o conhecimento de Deus, mais do que holocaustos.
7 Mas eles transgrediram a aliança, como Adão; eles se portaram aleivosamente contra mim.
8 Gileade é a cidade dos que praticam a injustiça, manchada de sangue.
9 Como hordas de salteadores que espreitam alguém, assim é a companhia dos sacerdotes, pois matam no caminho para Siquém; praticam abominações.
10 Vejo uma coisa horrenda na casa de Israel: ali está a prostituição de Efraim; Israel está contaminado.
11 Também tu, ó Judá, serás ceifado.*
1 Quando me disponho a mudar a sorte do meu povo e a sarar a Israel, se descobre a iniquidade de Efraim, como também a maldade de Samaria, porque praticam a falsidade; por dentro há ladrões, e por fora rouba a horda de salteadores.
2 Não dizem no seu coração que eu me lembro de toda a sua maldade; agora, pois, os seus próprios feitos os cercam; acham-se diante da minha face.
3 Com a sua malícia, alegram ao rei e com as suas mentiras, aos príncipes.
4 Todos eles são adúlteros: semelhantes ao forno aceso pelo padeiro, que somente cessa de atiçar o fogo desde que sovou a massa até que seja levedada.
5 No dia da festa do nosso rei, os príncipes se tornaram doentes com o excitamento do vinho, e ele deu a mão aos escarnecedores.
6 Porque prepararam o coração como um forno, enquanto estão de espreita; toda a noite, dorme o seu furor, mas, pela manhã, arde como labaredas de fogo.
7 Todos eles são quentes como um forno e consomem os seus juízes; todos os seus reis caem; ninguém há, entre eles, que me invoque.
8 Efraim se mistura com os povos e é um pão que não foi virado.
9 Estrangeiros lhe comem a força, e ele não o sabe; também as cãs já se espalham sobre ele, e ele não o sabe.
10 A soberba de Israel, abertamente, o acusa; todavia, não voltam para o Senhor, seu Deus, nem o buscam em tudo isto.
11 Porque Efraim é como uma pomba enganada, sem entendimento; chamam o Egito e vão para a Assíria.
12 Quando forem, sobre eles estenderei a minha rede e como aves do céu os farei descer; castigá-los-ei, segundo o que eles têm ouvido na sua congregação.
13 Ai deles! Porque fugiram de mim; destruição sobre eles, porque se rebelaram contra mim! Eu os remiria, mas eles falam mentiras contra mim.
14 Não clamam a mim de coração, mas dão uivos nas suas camas; para o trigo e para o vinho se ajuntam, mas contra mim se rebelam.
15 Adestrei e fortaleci os seus braços; no entanto, maquinam contra mim.
16 Eles voltam, mas não para o Altíssimo. Fizeram-se como um arco enganoso; caem à espada os seus príncipes, por causa da insolência da sua língua; este será o seu escárnio na terra do Egito.*
1 Emboca a trombeta! Ele vem como a águia contra a casa do Senhor, porque transgrediram a minha aliança e se rebelaram contra a minha lei.
2 A mim, me invocam: Nosso Deus! Nós, Israel, te conhecemos.
3 Israel rejeitou o bem; o inimigo o perseguirá.
4 Eles estabeleceram reis, mas não da minha parte; constituíram príncipes, mas eu não o soube; da sua prata e do seu ouro fizeram ídolos para si, para serem destruídos.
5 O teu bezerro, ó Samaria, é rejeitado; a minha ira se acende contra eles; até quando serão eles incapazes da inocência?
6 Porque vem de Israel, é obra de artífice, não é Deus; mas em pedaços será desfeito o bezerro de Samaria.
7 Porque semeiam ventos e segarão tormentas; não haverá seara; a erva não dará farinha; e, se a der, comê-la-ão os estrangeiros.
8 Israel foi devorado; agora, está entre as nações como coisa de que ninguém se agrada,
9 porque subiram à Assíria; o jumento montês anda solitário, mas Efraim mercou amores.
10 Todavia, ainda que eles merquem socorros entre as nações, eu os congregarei; já começaram a ser diminuídos por causa da opressão do rei e dos príncipes.
11 Porquanto Efraim multiplicou altares para pecar, estes lhe foram para pecar.
12 Embora eu lhe escreva a minha lei em dez mil preceitos, estes seriam tidos como coisa estranha.
13 Amam o sacrifício; por isso, sacrificam, pois gostam de carne e a comem, mas o Senhor não os aceita; agora, se lembrará da sua iniquidade e lhes castigará o pecado; eles voltarão para o Egito.
14 Porque Israel se esqueceu do seu Criador e edificou palácios, e Judá multiplicou cidades fortes; mas eu enviarei fogo contra as suas cidades, fogo que consumirá os seus palácios.*
1 Não te alegres, ó Israel, não exultes, como os povos; porque, com prostituir-te, abandonaste o teu Deus, amaste a paga de prostituição em todas as eiras de cereais.
2 A eira e o lagar não os manterão; e o vinho novo lhes faltará.
3 Na terra do Senhor, não permanecerão; mas Efraim tornará ao Egito e na Assíria comerá coisa imunda.
4 Não derramarão libações de vinho ao Senhor, nem os seus sacrifícios lhe serão agradáveis; seu pão será como pão de pranteadores, todos os que dele comerem serão imundos; porque o seu pão será exclusivamente para eles e não entrará na Casa do Senhor.
5 Que fareis vós no dia da solenidade e no dia da festa do Senhor?
6 Porque eis que eles se foram por causa da destruição, mas o Egito os ceifará, Mênfis os sepultará; as preciosidades da sua prata, as urtigas as possuirão; espinhos crescerão nas suas moradas.
7 Chegaram os dias do castigo, chegaram os dias da retribuição; Israel o saberá; o seu profeta é um insensato, o homem de espírito é um louco, por causa da abundância da tua iniquidade, ó Israel, e o muito do teu ódio.
8 O profeta é sentinela contra Efraim, ao lado de meu Deus, laço do passarinheiro em todos os seus caminhos e inimizade na casa do seu Deus.
9 Mui profundamente se corromperam, como nos dias de Gibeá. O Senhor se lembrará das suas injustiças e castigará os pecados deles.
10 Achei a Israel como uvas no deserto, vi a vossos pais como as primícias da figueira nova; mas eles foram para Baal-Peor, e se consagraram à vergonhosa idolatria, e se tornaram abomináveis como aquilo que amaram.
11 Quanto a Efraim, a sua glória voará como ave; não haverá nascimento, nem gravidez, nem concepção.
12 Ainda que venham a criar seus filhos, eu os privarei deles, para que não fique nenhum homem. Ai deles, quando deles me apartar!
13 Efraim, como planejei, seria como Tiro, plantado num lugar aprazível; mas Efraim levará seus filhos ao matador.
14 Dá-lhes, ó Senhor; que lhes darás? Dá-lhes um ventre estéril e seios secos.
15 Toda a sua malícia se acha em Gilgal, porque ali passei a aborrecê-los; por causa da maldade das suas obras, os lançarei fora de minha casa; já não os amarei; todos os seus príncipes são rebeldes.
16 Ferido está Efraim, secaram-se as suas raízes; não dará fruto; ainda que gere filhos, eu matarei os mais queridos do seu ventre.
17 O meu Deus os rejeitará, porque não o ouvem; e andarão errantes entre as nações.*
1 Israel é vide luxuriante, que dá o fruto; segundo a abundância do seu fruto, assim multiplicou os altares; quanto melhor a terra, tanto mais belas colunas fizeram.
2 O seu coração é falso; por isso, serão culpados; o Senhor quebrará os seus altares e deitará abaixo as colunas.
3 Agora, pois, dirão eles: Não temos rei, porque não tememos ao Senhor. E o rei, que faria por nós?
4 Falam palavras vãs, jurando falsamente, fazendo aliança; por isso, brota o juízo como erva venenosa nos sulcos dos campos.
5 Os moradores de Samaria serão atemorizados por causa do bezerro de Bete-Áven; o seu povo se lamentará por causa dele, e os sacerdotes idólatras tremerão por causa da sua glória, que já se foi.
6 Também o bezerro será levado à Assíria como presente ao rei principal; Efraim se cobrirá de vexame, e Israel se envergonhará por causa de seu próprio capricho.
7 O rei de Samaria será como lasca de madeira na superfície da água.
8 E os altos de Áven, pecado de Israel, serão destruídos; espinheiros e abrolhos crescerão sobre os seus altares; e aos montes se dirá: Cobri-nos! E aos outeiros: Caí sobre nós!
9 Desde os dias de Gibeá, pecaste, ó Israel, e nisto permaneceste. A peleja contra os filhos da perversidade não há de alcançar-te em Gibeá?
10 Castigarei o povo na medida do meu desejo; e congregar-se-ão contra eles os povos, quando eu o punir por causa de sua dupla transgressão.
11 Porque Efraim era uma bezerra domada, que gostava de trilhar; coloquei o jugo sobre a formosura do seu pescoço; atrelei Efraim ao carro. Judá lavrará, Jacó lhe desfará os torrões.
12 Então, eu disse: semeai para vós outros em justiça, ceifai segundo a misericórdia; arai o campo de pousio; porque é tempo de buscar ao Senhor, até que ele venha, e chova a justiça sobre vós.
13 Arastes a malícia, colhestes a perversidade; comestes o fruto da mentira, porque confiastes nos vossos carros e na multidão dos vossos valentes.
14 Portanto, entre o teu povo se levantará tumulto de guerra, e todas as tuas fortalezas serão destruídas, como Salmã destruiu a Bete-Arbel no dia da guerra; as mães ali foram despedaçadas com seus filhos.
15 Assim vos fará Betel, por causa da vossa grande malícia; como passa a alva, assim será o rei de Israel totalmente destruído.*
1 Quando Israel era menino, eu o amei; e do Egito chamei o meu filho.
2 Quanto mais eu os chamava, tanto mais se iam da minha presença; sacrificavam a baalins e queimavam incenso às imagens de escultura.
3 Todavia, eu ensinei a andar a Efraim; tomei-os nos meus braços, mas não atinaram que eu os curava.
4 Atraí-os com cordas humanas, com laços de amor; fui para eles como quem alivia o jugo de sobre as suas queixadas e me inclinei para dar-lhes de comer.
5 Não voltarão para a terra do Egito, mas o assírio será seu rei, porque recusam converter-se.
6 A espada cairá sobre as suas cidades, e consumirá os seus ferrolhos, e as devorará, por causa dos seus caprichos.
7 Porque o meu povo é inclinado a desviar-se de mim; se é concitado a dirigir-se acima, ninguém o faz.
8 Como te deixaria, ó Efraim? Como te entregaria, ó Israel? Como te faria como a Admá? Como fazer-te um Zeboim? Meu coração está comovido dentro de mim, as minhas compaixões, à uma, se acendem.
9 Não executarei o furor da minha ira; não tornarei para destruir a Efraim, porque eu sou Deus e não homem, o Santo no meio de ti; não voltarei em ira.
10 Andarão após o Senhor; este bramará como leão, e, bramando, os filhos, tremendo, virão do Ocidente;
11 tremendo, virão, como passarinhos, os do Egito, e, como pombas, os da terra da Assíria, e os farei habitar em suas próprias casas, diz o Senhor.
12 Efraim me cercou por meio de mentiras, e a casa de Israel, com engano; mas Judá ainda domina com Deus e é fiel com o Santo.*
1 Efraim apascenta o vento e persegue o vento leste todo o dia; multiplica mentiras e destruição e faz aliança com a Assíria, e o azeite se leva ao Egito.
2 O Senhor também com Judá tem contenda e castigará Jacó segundo o seu proceder; segundo as suas obras, o recompensará.
3 No ventre, pegou do calcanhar de seu irmão; no vigor da sua idade, lutou com Deus;
4 lutou com o anjo e prevaleceu; chorou e lhe pediu mercê; em Betel, achou a Deus, e ali falou Deus conosco.
5 O Senhor, o Deus dos Exércitos, o Senhor é o seu nome;
6 converte-te a teu Deus, guarda o amor e o juízo e no teu Deus espera sempre.
7 Efraim, mercador, tem nas mãos balança enganosa e ama a opressão;
8 mas diz: Contudo, me tenho enriquecido e adquirido grandes bens; em todos esses meus esforços, não acharão em mim iniquidade alguma, nada que seja pecado.
9 Mas eu sou o Senhor, teu Deus, desde a terra do Egito; eu ainda te farei habitar em tendas, como nos dias da festa.
10 Falei aos profetas e multipliquei as visões; e, pelo ministério dos profetas, propus símiles.
11 Se há em Gileade transgressão, pura vaidade são eles; se em Gilgal sacrificam bois, os seus altares são como montões de pedra nos sulcos dos campos.
12 Jacó fugiu para a terra da Síria, e Israel serviu por uma mulher e por ela guardou o gado.
13 Mas o Senhor, por meio de um profeta, fez subir a Israel do Egito e, por um profeta, foi ele guardado.
14 Efraim mui amargamente provocou à ira; portanto, o Senhor deixará ficar sobre ele o sangue por ele derramado; e fará cair sobre ele o seu opróbrio.*
1 Quando falava Efraim, havia tremor; foi exaltado em Israel, mas ele se fez culpado no tocante a Baal e morreu.
2 Agora, pecam mais e mais, e da sua prata fazem imagens de fundição, ídolos segundo o seu conceito, todos obra de artífices, e dizem: Sacrificai a eles. Homens até beijam bezerros!
3 Por isso, serão como nuvem de manhã, como orvalho que cedo passa, como palha que se lança da eira e como fumaça que sai por uma janela.
4 Todavia, eu sou o Senhor, teu Deus, desde a terra do Egito; portanto, não conhecerás outro deus além de mim, porque não há salvador, senão eu.
5 Eu te conheci no deserto, em terra muito seca.
6 Quando tinham pasto, eles se fartaram, e, uma vez fartos, ensoberbeceu-se-lhes o coração; por isso, se esqueceram de mim.
7 Sou, pois, para eles como leão; como leopardo, espreito no caminho.
8 Como ursa, roubada de seus filhos, eu os atacarei e lhes romperei a envoltura do coração; e, como leão, ali os devorarei, as feras do campo os despedaçarão.
9 A tua ruína, ó Israel, vem de ti, e só de mim, o teu socorro.
10 Onde está, agora, o teu rei, para que te salve em todas as tuas cidades? E os teus juízes, dos quais disseste: Dá-me rei e príncipes?
11 Dei-te um rei na minha ira e to tirei no meu furor.
12 As iniquidades de Efraim estão atadas juntas, o seu pecado está armazenado.
13 Dores de parturiente lhe virão; ele é filho insensato, porque é tempo, e não sai à luz, ao abrir-se da madre.
14 Eu os remirei do poder do inferno e os resgatarei da morte; onde estão, ó morte, as tuas pragas? Onde está, ó inferno, a tua destruição? Meus olhos não veem em mim arrependimento algum.
15 Ainda que ele viceja entre os irmãos, virá o vento leste, vento do Senhor, subindo do deserto, e secará a sua nascente, e estancará a sua fonte; ele saqueará o tesouro de todas as coisas preciosas.
16 Samaria levará sobre si a sua culpa, porque se rebelou contra o seu Deus; cairá à espada, seus filhos serão despedaçados, e as suas mulheres grávidas serão abertas pelo meio.*
1 Volta, ó Israel, para o Senhor, teu Deus, porque, pelos teus pecados, estás caído.
2 Tende convosco palavras de arrependimento e convertei-vos ao Senhor; dizei-lhe: Perdoa toda iniquidade, aceita o que é bom e, em vez de novilhos, os sacrifícios dos nossos lábios.
3 A Assíria já não nos salvará, não iremos montados em cavalos e não mais diremos à obra das nossas mãos: tu és o nosso Deus; por ti o órfão alcançará misericórdia.
4 Curarei a sua infidelidade, eu de mim mesmo os amarei, porque a minha ira se apartou deles.
5 Serei para Israel como orvalho, ele florescerá como o lírio e lançará as suas raízes como o cedro do Líbano.
6 Estender-se-ão os seus ramos, o seu esplendor será como o da oliveira, e sua fragrância, como a do Líbano.
7 Os que se assentam de novo à sua sombra voltarão; serão vivificados como o cereal e florescerão como a vide; a sua fama será como a do vinho do Líbano.
8 Ó Efraim, que tenho eu com os ídolos? Eu te ouvirei e cuidarei de ti; sou como o cipreste verde; de mim procede o teu fruto.
9 Quem é sábio, que entenda estas coisas; quem é prudente, que as saiba, porque os caminhos do Senhor são retos, e os justos andarão neles, mas os transgressores neles cairão.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Oséias','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)