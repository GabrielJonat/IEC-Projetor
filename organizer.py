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
1 Visão de Isaías, filho de Amoz, que ele teve a respeito de Judá e Jerusalém, nos dias de Uzias, Jotão, Acaz e Ezequias, reis de Judá.
2 Ouvi, ó céus, e dá ouvidos, ó terra, porque o Senhor é quem fala: Criei filhos e os engrandeci, mas eles estão revoltados contra mim.
3 O boi conhece o seu possuidor, e o jumento, o dono da sua manjedoura; mas Israel não tem conhecimento, o meu povo não entende.
4 Ai desta nação pecaminosa, povo carregado de iniquidade, raça de malignos, filhos corruptores; abandonaram o Senhor, blasfemaram do Santo de Israel, voltaram para trás.
5 Por que haveis de ainda ser feridos, visto que continuais em rebeldia? Toda a cabeça está doente, e todo o coração, enfermo.
6 Desde a planta do pé até à cabeça não há nele coisa sã, senão feridas, contusões e chagas inflamadas, umas e outras não espremidas, nem atadas, nem amolecidas com óleo.
7 A vossa terra está assolada, as vossas cidades, consumidas pelo fogo; a vossa lavoura os estranhos devoram em vossa presença; e a terra se acha devastada como numa subversão de estranhos.
8 A filha de Sião é deixada como choça na vinha, como palhoça no pepinal, como cidade sitiada.
9 Se o Senhor dos Exércitos não nos tivesse deixado alguns sobreviventes, já nos teríamos tornado como Sodoma e semelhantes a Gomorra.
10 Ouvi a palavra do Senhor, vós, príncipes de Sodoma; prestai ouvidos à lei do nosso Deus, vós, povo de Gomorra.
11 De que me serve a mim a multidão de vossos sacrifícios? — diz o Senhor. Estou farto dos holocaustos de carneiros e da gordura de animais cevados e não me agrado do sangue de novilhos, nem de cordeiros, nem de bodes.
12 Quando vindes para comparecer perante mim, quem vos requereu o só pisardes os meus átrios?
13 Não continueis a trazer ofertas vãs; o incenso é para mim abominação, e também as Festas da Lua Nova, os sábados, e a convocação das congregações; não posso suportar iniquidade associada ao ajuntamento solene.
14 As vossas Festas da Lua Nova e as vossas solenidades, a minha alma as aborrece; já me são pesadas; estou cansado de as sofrer.
15 Pelo que, quando estendeis as mãos, escondo de vós os olhos; sim, quando multiplicais as vossas orações, não as ouço, porque as vossas mãos estão cheias de sangue.
16 Lavai-vos, purificai-vos, tirai a maldade de vossos atos de diante dos meus olhos; cessai de fazer o mal.
17 Aprendei a fazer o bem; atendei à justiça, repreendei ao opressor; defendei o direito do órfão, pleiteai a causa das viúvas.
18 Vinde, pois, e arrazoemos, diz o Senhor; ainda que os vossos pecados sejam como a escarlata, eles se tornarão brancos como a neve; ainda que sejam vermelhos como o carmesim, se tornarão como a lã.
19 Se quiserdes e me ouvirdes, comereis o melhor desta terra.
20 Mas, se recusardes e fordes rebeldes, sereis devorados à espada; porque a boca do Senhor o disse.
21 Como se fez prostituta a cidade fiel! Ela, que estava cheia de justiça! Nela, habitava a retidão, mas, agora, homicidas.
22 A tua prata se tornou em escórias, o teu licor se misturou com água.
23 Os teus príncipes são rebeldes e companheiros de ladrões; cada um deles ama o suborno e corre atrás de recompensas. Não defendem o direito do órfão, e não chega perante eles a causa das viúvas.
24 Portanto, diz o Senhor, o Senhor dos Exércitos, o Poderoso de Israel: Ah! Tomarei satisfações aos meus adversários e vingar-me-ei dos meus inimigos.
25 Voltarei contra ti a minha mão, purificar-te-ei como com potassa das tuas escórias e tirarei de ti todo metal impuro.
26 Restituir-te-ei os teus juízes, como eram antigamente, os teus conselheiros, como no princípio; depois, te chamarão cidade de justiça, cidade fiel.
27 Sião será redimida pelo direito, e os que se arrependem, pela justiça.
28 Mas os transgressores e os pecadores serão juntamente destruídos; e os que deixarem o Senhor perecerão.
29 Porque vos envergonhareis dos carvalhos que cobiçastes e sereis confundidos por causa dos jardins que escolhestes.
30 Porque sereis como o carvalho, cujas folhas murcham, e como a floresta que não tem água.
31 O forte se tornará em estopa, e a sua obra, em faísca; ambos arderão juntamente, e não haverá quem os apague.*
1 Palavra que, em visão, veio a Isaías, filho de Amoz, a respeito de Judá e Jerusalém.
2 Nos últimos dias, acontecerá que o monte da Casa do Senhor será estabelecido no cimo dos montes e se elevará sobre os outeiros, e para ele afluirão todos os povos.
3 Irão muitas nações e dirão: Vinde, e subamos ao monte do Senhor e à casa do Deus de Jacó, para que nos ensine os seus caminhos, e andemos pelas suas veredas; porque de Sião sairá a lei, e a palavra do Senhor, de Jerusalém.
4 Ele julgará entre os povos e corrigirá muitas nações; estas converterão as suas espadas em relhas de arados e suas lanças, em podadeiras; uma nação não levantará a espada contra outra nação, nem aprenderão mais a guerra.
5 Vinde, ó casa de Jacó, e andemos na luz do Senhor.
6 Pois, tu, Senhor, desamparaste o teu povo, a casa de Jacó, porque os seus se encheram da corrupção do Oriente e são agoureiros como os filisteus e se associam com os filhos dos estranhos.
7 A sua terra está cheia de prata e de ouro, e não têm conta os seus tesouros; também está cheia de cavalos, e os seus carros não têm fim.
8 Também está cheia a sua terra de ídolos; adoram a obra das suas mãos, aquilo que os seus próprios dedos fizeram.
9 Com isso, a gente se abate, e o homem se avilta; portanto, não lhes perdoarás.
10 Vai, entra nas rochas e esconde-te no pó, ante o terror do Senhor e a glória da sua majestade.
11 Os olhos altivos dos homens serão abatidos, e a sua altivez será humilhada; só o Senhor será exaltado naquele dia.
12 Porque o Dia do Senhor dos Exércitos será contra todo soberbo e altivo e contra todo aquele que se exalta, para que seja abatido;
13 contra todos os cedros do Líbano, altos, mui elevados; e contra todos os carvalhos de Basã;
14 contra todos os montes altos e contra todos os outeiros elevados;
15 contra toda torre alta e contra toda muralha firme;
16 contra todos os navios de Társis e contra tudo o que é belo à vista.
17 A arrogância do homem será abatida, e a sua altivez será humilhada; só o Senhor será exaltado naquele dia.
18 Os ídolos serão de todo destruídos.
19 Então, os homens se meterão nas cavernas das rochas e nos buracos da terra, ante o terror do Senhor e a glória da sua majestade, quando ele se levantar para espantar a terra.
20 Naquele dia, os homens lançarão às toupeiras e aos morcegos os seus ídolos de prata e os seus ídolos de ouro, que fizeram para ante eles se prostrarem,
21 e meter-se-ão pelas fendas das rochas e pelas cavernas das penhas, ante o terror do Senhor e a glória da sua majestade, quando ele se levantar para espantar a terra.
22 Afastai-vos, pois, do homem cujo fôlego está no seu nariz. Pois em que é ele estimado?*
1 Porque eis que o Senhor, o Senhor dos Exércitos, tira de Jerusalém e de Judá o sustento e o apoio, todo sustento de pão e todo sustento de água;
2 o valente, o guerreiro e o juiz; o profeta, o adivinho e o ancião;
3 o capitão de cinquenta, o respeitável, o conselheiro, o hábil entre os artífices e o encantador perito.
4 Dar-lhes-ei meninos por príncipes, e crianças governarão sobre eles.
5 Entre o povo, oprimem uns aos outros, cada um, ao seu próximo; o menino se atreverá contra o ancião, e o vil, contra o nobre.
6 Quando alguém se chegar a seu irmão e lhe disser, na casa de seu pai: Tu tens roupa, sê nosso príncipe e toma sob teu governo esta ruína;
7 naquele dia, levantará este a sua voz, dizendo: Não sou médico, não há pão em minha casa, nem veste alguma; não me ponhais por príncipe do povo.
8 Porque Jerusalém está arruinada, e Judá, caída; porquanto a sua língua e as suas obras são contra o Senhor, para desafiarem a sua gloriosa presença.
9 O aspecto do seu rosto testifica contra eles; e, como Sodoma, publicam o seu pecado e não o encobrem. Ai da sua alma! Porque fazem mal a si mesmos.
10 Dizei aos justos que bem lhes irá; porque comerão do fruto das suas ações.
11 Ai do perverso! Mal lhe irá; porque a sua paga será o que as suas próprias mãos fizeram.
12 Os opressores do meu povo são crianças, e mulheres estão à testa do seu governo. Oh! Povo meu! Os que te guiam te enganam e destroem o caminho por onde deves seguir.
13 O Senhor se dispõe para pleitear e se apresenta para julgar os povos.
14 O Senhor entra em juízo contra os anciãos do seu povo e contra os seus príncipes. Vós sois os que consumistes esta vinha; o que roubastes do pobre está em vossa casa.
15 Que há convosco que esmagais o meu povo e moeis a face dos pobres? — diz o Senhor, o Senhor dos Exércitos.
16 Diz ainda mais o Senhor: Visto que são altivas as filhas de Sião e andam de pescoço emproado, de olhares impudentes, andam a passos curtos, fazendo tinir os ornamentos de seus pés,
17 o Senhor fará tinhosa a cabeça das filhas de Sião, o Senhor porá a descoberto as suas vergonhas.
18 Naquele dia, tirará o Senhor o enfeite dos anéis dos tornozelos, e as toucas, e os ornamentos em forma de meia-lua;
19 os pendentes, e os braceletes, e os véus esvoaçantes;
20 os turbantes, as cadeiazinhas para os passos, as cintas, as caixinhas de perfumes e os amuletos;
21 os sinetes e as joias pendentes do nariz;
22 os vestidos de festa, os mantos, os xales e as bolsas;
23 os espelhos, as camisas finíssimas, os atavios de cabeça e os véus grandes.
24 Será que em lugar de perfume haverá podridão, e por cinta, corda; em lugar de encrespadura de cabelos, calvície; e em lugar de veste suntuosa, cilício; e marca de fogo, em lugar de formosura.
25 Os teus homens cairão à espada, e os teus valentes, na guerra.
26 As suas portas chorarão e estarão de luto; Sião, desolada, se assentará em terra.*
1 Sete mulheres, naquele dia, lançarão mão de um homem, dizendo: Nós mesmas do nosso próprio pão nos sustentaremos e do que é nosso nos vestiremos; tão somente queremos ser chamadas pelo teu nome; tira o nosso opróbrio.
2 Naquele dia, o Renovo do Senhor será de beleza e de glória; e o fruto da terra, orgulho e adorno para os de Israel que forem salvos.
3 Será que os restantes de Sião e os que ficarem em Jerusalém serão chamados santos; todos os que estão inscritos em Jerusalém, para a vida,
4 quando o Senhor lavar a imundícia das filhas de Sião e limpar Jerusalém da culpa do sangue do meio dela, com o Espírito de justiça e com o Espírito purificador.
5 Criará o Senhor, sobre todo o monte de Sião e sobre todas as suas assembleias, uma nuvem de dia e fumaça e resplendor de fogo chamejante de noite; porque sobre toda a glória se estenderá um dossel e um pavilhão,
6 os quais serão para sombra contra o calor do dia e para refúgio e esconderijo contra a tempestade e a chuva.*
1 Agora, cantarei ao meu amado o cântico do meu amado a respeito da sua vinha. O meu amado teve uma vinha num outeiro fertilíssimo.
2 Sachou-a, limpou-a das pedras e a plantou de vides escolhidas; edificou no meio dela uma torre e também abriu um lagar. Ele esperava que desse uvas boas, mas deu uvas bravas.
3 Agora, pois, ó moradores de Jerusalém e homens de Judá, julgai, vos peço, entre mim e a minha vinha.
4 Que mais se podia fazer ainda à minha vinha, que eu lhe não tenha feito? E como, esperando eu que desse uvas boas, veio a produzir uvas bravas?
5 Agora, pois, vos farei saber o que pretendo fazer à minha vinha: tirarei a sua sebe, para que a vinha sirva de pasto; derribarei o seu muro, para que seja pisada;
6 torná-la-ei em deserto. Não será podada, nem sachada, mas crescerão nela espinheiros e abrolhos; às nuvens darei ordem que não derramem chuva sobre ela.
7 Porque a vinha do Senhor dos Exércitos é a casa de Israel, e os homens de Judá são a planta dileta do Senhor; este desejou que exercessem juízo, e eis aí quebrantamento da lei; justiça, e eis aí clamor.
8 Ai dos que ajuntam casa a casa, reúnem campo a campo, até que não haja mais lugar, e ficam como únicos moradores no meio da terra!
9 A meus ouvidos disse o Senhor dos Exércitos: Em verdade, muitas casas ficarão desertas, até as grandes e belas, sem moradores.
10 E dez jeiras de vinha não darão mais do que um bato, e um ômer cheio de semente não dará mais do que um efa.
11 Ai dos que se levantam pela manhã e seguem a bebedice e continuam até alta noite, até que o vinho os esquenta!
12 Liras e harpas, tamboris e flautas e vinho há nos seus banquetes; porém não consideram os feitos do Senhor, nem olham para as obras das suas mãos.
13 Portanto, o meu povo será levado cativo, por falta de entendimento; os seus nobres terão fome, e a sua multidão se secará de sede.
14 Por isso, a cova aumentou o seu apetite, abriu a sua boca desmesuradamente; para lá desce a glória de Jerusalém, e o seu tumulto, e o seu ruído, e quem nesse meio folgava.
15 Então, a gente se abate, e o homem se avilta; e os olhos dos altivos são humilhados.
16 Mas o Senhor dos Exércitos é exaltado em juízo; e Deus, o Santo, é santificado em justiça.
17 Então, os cordeiros pastarão lá como se no seu pasto; e os nômades se nutrirão dos campos dos ricos lá abandonados.
18 Ai dos que puxam para si a iniquidade com cordas de injustiça e o pecado, como com tirantes de carro!
19 E dizem: Apresse-se Deus, leve a cabo a sua obra, para que a vejamos; aproxime-se, manifeste-se o conselho do Santo de Israel, para que o conheçamos.
20 Ai dos que ao mal chamam bem e ao bem, mal; que fazem da escuridade luz e da luz, escuridade; põem o amargo por doce e o doce, por amargo!
21 Ai dos que são sábios a seus próprios olhos e prudentes em seu próprio conceito!
22 Ai dos que são heróis para beber vinho e valentes para misturar bebida forte,
23 os quais por suborno justificam o perverso e ao justo negam justiça!
24 Pelo que, como a língua de fogo consome o restolho, e a erva seca se desfaz pela chama, assim será a sua raiz como podridão, e a sua flor se esvaecerá como pó; porquanto rejeitaram a lei do Senhor dos Exércitos e desprezaram a palavra do Santo de Israel.
25 Por isso, se acende a ira do Senhor contra o seu povo, povo contra o qual estende a mão e o fere, de modo que tremem os montes e os seus cadáveres são como monturo no meio das ruas. Com tudo isto não se aplaca a sua ira, mas ainda está estendida a sua mão.
26 Ele arvorará o estandarte para as nações distantes e lhes assobiará para que venham das extremidades da terra; e vêm apressadamente.
27 Não há entre elas cansado, nem quem tropece; ninguém tosqueneja, nem dorme; não se lhe desata o cinto dos seus lombos, nem se lhe rompe das sandálias a correia.
28 As suas flechas são agudas, e todos os seus arcos, retesados; as unhas dos seus cavalos dizem-se de pederneira, e as rodas dos seus carros, um redemoinho.
29 O seu rugido é como o do leão; rugem como filhos de leão, e, rosnando, arrebatam a presa, e a levam, e não há quem a livre.
30 Bramam contra eles naquele dia, como o bramido do mar; se alguém olhar para a terra, eis que só há trevas e angústia, e a luz se escurece em densas nuvens.*
1 No ano da morte do rei Uzias, eu vi o Senhor assentado sobre um alto e sublime trono, e as abas de suas vestes enchiam o templo.
2 Serafins estavam por cima dele; cada um tinha seis asas: com duas cobria o rosto, com duas cobria os seus pés e com duas voava.
3 E clamavam uns para os outros, dizendo: Santo, santo, santo é o Senhor dos Exércitos; toda a terra está cheia da sua glória.
4 As bases do limiar se moveram à voz do que clamava, e a casa se encheu de fumaça.
5 Então, disse eu: ai de mim! Estou perdido! Porque sou homem de lábios impuros, habito no meio de um povo de impuros lábios, e os meus olhos viram o Rei, o Senhor dos Exércitos!
6 Então, um dos serafins voou para mim, trazendo na mão uma brasa viva, que tirara do altar com uma tenaz;
7 com a brasa tocou a minha boca e disse: Eis que ela tocou os teus lábios; a tua iniquidade foi tirada, e perdoado, o teu pecado.
8 Depois disto, ouvi a voz do Senhor, que dizia: A quem enviarei, e quem há de ir por nós? Disse eu: eis-me aqui, envia-me a mim.
9 Então, disse ele: Vai e dize a este povo: Ouvi, ouvi e não entendais; vede, vede, mas não percebais.
10 Torna insensível o coração deste povo, endurece-lhe os ouvidos e fecha-lhe os olhos, para que não venha ele a ver com os olhos, a ouvir com os ouvidos e a entender com o coração, e se converta, e seja salvo.
11 Então, disse eu: até quando, Senhor? Ele respondeu: Até que sejam desoladas as cidades e fiquem sem habitantes, as casas fiquem sem moradores, e a terra seja de todo assolada,
12 e o Senhor afaste dela os homens, e no meio da terra seja grande o desamparo.
13 Mas, se ainda ficar a décima parte dela, tornará a ser destruída. Como terebinto e como carvalho, dos quais, depois de derribados, ainda fica o toco, assim a santa semente é o seu toco.*
1 Sucedeu nos dias de Acaz, filho de Jotão, filho de Uzias, rei de Judá, que Rezim, rei da Síria, e Peca, filho de Remalias, rei de Israel, subiram a Jerusalém, para pelejarem contra ela, porém não prevaleceram contra ela.
2 Deu-se aviso à casa de Davi: A Síria está aliada com Efraim. Então, ficou agitado o coração de Acaz e o coração do seu povo, como se agitam as árvores do bosque com o vento.
3 Disse o Senhor a Isaías: Agora, sai tu com teu filho, que se chama Um-Resto-Volverá, ao encontro de Acaz, que está na outra extremidade do aqueduto do açude superior, junto ao caminho do campo do lavadeiro,
4 e dize-lhe: Acautela-te e aquieta-te; não temas, nem se desanime o teu coração por causa destes dois tocos de tições fumegantes; por causa do ardor da ira de Rezim, e da Síria, e do filho de Remalias.
5 Porquanto a Síria resolveu fazer-te mal, bem como Efraim e o filho de Remalias, dizendo:
6 Subamos contra Judá, e amedrontemo-lo, e o conquistemos para nós, e façamos reinar no meio dele o filho de Tabeal.
7 Assim diz o Senhor Deus: Isto não subsistirá, nem tampouco acontecerá.
8 Mas a capital da Síria será Damasco, e o cabeça de Damasco, Rezim, e dentro de sessenta e cinco anos Efraim será destruído e deixará de ser povo.
9 Entretanto, a capital de Efraim será Samaria, e o cabeça de Samaria, o filho de Remalias; se o não crerdes, certamente, não permanecereis.
10 E continuou o Senhor a falar com Acaz, dizendo:
11 Pede ao Senhor, teu Deus, um sinal, quer seja embaixo, nas profundezas, ou em cima, nas alturas.
12 Acaz, porém, disse: Não o pedirei, nem tentarei ao Senhor.
13 Então, disse o profeta: Ouvi, agora, ó casa de Davi: acaso, não vos basta fatigardes os homens, mas ainda fatigais também ao meu Deus?
14 Portanto, o Senhor mesmo vos dará um sinal: eis que a virgem conceberá e dará à luz um filho e lhe chamará Emanuel.
15 Ele comerá manteiga e mel quando souber desprezar o mal e escolher o bem.
16 Na verdade, antes que este menino saiba desprezar o mal e escolher o bem, será desamparada a terra ante cujos dois reis tu tremes de medo.
17 Mas o Senhor fará vir sobre ti, sobre o teu povo e sobre a casa de teu pai, por intermédio do rei da Assíria, dias tais, quais nunca vieram, desde o dia em que Efraim se separou de Judá.
18 Porque há de acontecer que, naquele dia, assobiará o Senhor às moscas que há no extremo dos rios do Egito e às abelhas que andam na terra da Assíria;
19 elas virão e pousarão todas nos vales profundos, nas fendas das rochas, em todos os espinhos e em todos os pastios.
20 Naquele dia, rapar-te-á o Senhor com uma navalha alugada doutro lado do rio, a saber, por meio do rei da Assíria, a cabeça e os cabelos das vergonhas e tirará também a barba.
21 Naquele dia, sucederá que um homem manterá apenas uma vaca nova e duas ovelhas,
22 e será tal a abundância de leite que elas lhe darão, que comerá manteiga; manteiga e mel comerá todo o restante no meio da terra.
23 Também, naquele dia, todo lugar em que houver mil vides, do valor de mil siclos de prata, será para espinheiros e abrolhos.
24 Com flechas e arco se entrará aí, porque os espinheiros e abrolhos cobrirão toda a terra.
25 Quanto a todos os montes, que os homens costumam sachar, para ali não irás por temeres os espinhos e abrolhos; serão para pasto de bois e para serem pisados de ovelhas.*
1 Disse-me também o Senhor: Toma uma ardósia grande e escreve nela de maneira inteligível: Rápido-Despojo-Presa-Segura.
2 Tomei para isto comigo testemunhas fidedignas, a Urias, sacerdote, e a Zacarias, filho de Jeberequias.
3 Fui ter com a profetisa; ela concebeu e deu à luz um filho. Então, me disse o Senhor: Põe-lhe o nome de Rápido-Despojo-Presa-Segura.
4 Porque antes que o menino saiba dizer meu pai ou minha mãe, serão levadas as riquezas de Damasco e os despojos de Samaria, diante do rei da Assíria.
5 Falou-me ainda o Senhor, dizendo:
6 Em vista de este povo ter desprezado as águas de Siloé, que correm brandamente, e se estar derretendo de medo diante de Rezim e do filho de Remalias,
7 eis que o Senhor fará vir sobre eles as águas do Eufrates, fortes e impetuosas, isto é, o rei da Assíria, com toda a sua glória; águas que encherão o leito dos rios e transbordarão por todas as suas ribanceiras.
8 Penetrarão em Judá, inundando-o, e, passando por ele, chegarão até ao pescoço; as alas estendidas do seu exército cobrirão a largura da tua terra, ó Emanuel.
9 Enfurecei-vos, ó povos, e sereis despedaçados; dai ouvidos, todos os que sois de países longínquos; cingi-vos e sereis despedaçados, cingi-vos e sereis despedaçados.
10 Forjai projetos, e eles serão frustrados; dai ordens, e elas não serão cumpridas, porque Deus é conosco.
11 Porque assim o Senhor me disse, tendo forte a mão sobre mim, e me advertiu que não andasse pelo caminho deste povo, dizendo:
12 Não chameis conjuração a tudo quanto este povo chama conjuração; não temais o que ele teme, nem tomeis isso por temível.
13 Ao Senhor dos Exércitos, a ele santificai; seja ele o vosso temor, seja ele o vosso espanto.
14 Ele vos será santuário; mas será pedra de tropeço e rocha de ofensa às duas casas de Israel, laço e armadilha aos moradores de Jerusalém.
15 Muitos dentre eles tropeçarão e cairão, serão quebrantados, enlaçados e presos.
16 Resguarda o testemunho, sela a lei no coração dos meus discípulos.
17 Esperarei no Senhor, que esconde o seu rosto da casa de Jacó, e a ele aguardarei.
18 Eis-me aqui, e os filhos que o Senhor me deu, para sinais e para maravilhas em Israel da parte do Senhor dos Exércitos, que habita no monte Sião.
19 Quando vos disserem: Consultai os necromantes e os adivinhos, que chilreiam e murmuram, acaso, não consultará o povo ao seu Deus? A favor dos vivos se consultarão os mortos?
20 À lei e ao testemunho! Se eles não falarem desta maneira, jamais verão a alva.
21 Passarão pela terra duramente oprimidos e famintos; e será que, quando tiverem fome, enfurecendo-se, amaldiçoarão ao seu rei e ao seu Deus, olhando para cima.
22 Olharão para a terra, e eis aí angústia, escuridão e sombras de ansiedade, e serão lançados para densas trevas.*
1 Mas para a terra que estava aflita não continuará a obscuridade. Deus, nos primeiros tempos, tornou desprezível a terra de Zebulom e a terra de Naftali; mas, nos últimos, tornará glorioso o caminho do mar, além do Jordão, Galileia dos gentios.
2 O povo que andava em trevas viu grande luz, e aos que viviam na região da sombra da morte, resplandeceu-lhes a luz.
3 Tens multiplicado este povo, a alegria lhe aumentaste; alegram-se eles diante de ti, como se alegram na ceifa e como exultam quando repartem os despojos.
4 Porque tu quebraste o jugo que pesava sobre eles, a vara que lhes feria os ombros e o cetro do seu opressor, como no dia dos midianitas;
5 porque toda bota com que anda o guerreiro no tumulto da batalha e toda veste revolvida em sangue serão queimadas, servirão de pasto ao fogo.
6 Porque um menino nos nasceu, um filho se nos deu; o governo está sobre os seus ombros; e o seu nome será: Maravilhoso Conselheiro, Deus Forte, Pai da Eternidade, Príncipe da Paz;
7 para que se aumente o seu governo, e venha paz sem fim sobre o trono de Davi e sobre o seu reino, para o estabelecer e o firmar mediante o juízo e a justiça, desde agora e para sempre. O zelo do Senhor dos Exércitos fará isto.
8 O Senhor enviou uma palavra contra Jacó, e ela caiu em Israel.
9 Todo o povo o saberá, Efraim e os moradores de Samaria, que em soberba e altivez de coração dizem:
10 Os tijolos ruíram por terra, mas tornaremos a edificar com pedras lavradas; cortaram-se os sicômoros, mas por cedros os substituiremos.
11 Portanto, o Senhor suscita contra ele os adversários de Rezim e instiga os inimigos.
12 Do Oriente vêm os siros, do Ocidente, os filisteus e devoram a Israel à boca escancarada. Com tudo isto, não se aparta a sua ira, e a mão dele continua ainda estendida.
13 Todavia, este povo não se voltou para quem o fere, nem busca ao Senhor dos Exércitos.
14 Pelo que o Senhor corta de Israel a cabeça e a cauda, a palma e o junco, num mesmo dia.
15 O ancião, o homem de respeito, é a cabeça; o profeta que ensina a mentira é a cauda.
16 Porque os guias deste povo são enganadores, e os que por eles são dirigidos são devorados.
17 Pelo que o Senhor não se regozija com os jovens dele e não se compadece dos seus órfãos e das suas viúvas, porque todos eles são ímpios e malfazejos, e toda boca profere doidices. Com tudo isto, não se aparta a sua ira, e a mão dele continua ainda estendida.
18 Porque a maldade lavra como um fogo, ela devora os espinheiros e os abrolhos; acende as brenhas do bosque, e estas sobem em espessas nuvens de fumaça.
19 Por causa da ira do Senhor dos Exércitos, a terra está abrasada, e o povo é pasto do fogo; ninguém poupa a seu irmão.
20 Abocanha à direita e ainda tem fome, devora à esquerda e não se farta; cada um come a carne do seu próximo:
21 Manassés ataca a Efraim, e Efraim ataca a Manassés, e ambos, juntos, atacam a Judá. Com tudo isto, não se aparta a sua ira, e a mão dele continua ainda estendida.*
1 Ai dos que decretam leis injustas, dos que escrevem leis de opressão,
2 para negarem justiça aos pobres, para arrebatarem o direito aos aflitos do meu povo, a fim de despojarem as viúvas e roubarem os órfãos!
3 Mas que fareis vós outros no dia do castigo, na calamidade que vem de longe? A quem recorrereis para obter socorro e onde deixareis a vossa glória?
4 Nada mais vos resta a fazer, senão dobrar-vos entre os prisioneiros e cair entre os mortos. Com tudo isto, não se aparta a sua ira, e a mão dele continua ainda estendida.
5 Ai da Assíria, cetro da minha ira! A vara em sua mão é o instrumento do meu furor.
6 Envio-a contra uma nação ímpia e contra o povo da minha indignação lhe dou ordens, para que dele roube a presa, e lhe tome o despojo, e o ponha para ser pisado aos pés, como a lama das ruas.
7 Ela, porém, assim não pensa, o seu coração não entende assim; antes, intenta consigo mesma destruir e desarraigar não poucas nações.
8 Porque diz: Não são meus príncipes todos eles reis?
9 Não é Calno como Carquemis? Não é Hamate como Arpade? E Samaria, como Damasco?
10 O meu poder atingiu os reinos dos ídolos, ainda que as suas imagens de escultura eram melhores do que as de Jerusalém e do que as de Samaria.
11 Porventura, como fiz a Samaria e aos seus ídolos, não o faria igualmente a Jerusalém e aos seus ídolos?
12 Por isso, acontecerá que, havendo o Senhor acabado toda a sua obra no monte Sião e em Jerusalém, então, castigará a arrogância do coração do rei da Assíria e a desmedida altivez dos seus olhos;
13 porquanto o rei disse: Com o poder da minha mão, fiz isto, e com a minha sabedoria, porque sou inteligente; removi os limites dos povos, e roubei os seus tesouros, e como valente abati os que se assentavam em tronos.
14 Meti a mão nas riquezas dos povos como a um ninho e, como se ajuntam os ovos abandonados, assim eu ajuntei toda a terra, e não houve quem movesse a asa, ou abrisse a boca, ou piasse.
15 Porventura, gloriar-se-á o machado contra o que corta com ele? Ou presumirá a serra contra o que a maneja? Seria isso como se a vara brandisse os que a levantam ou o bastão levantasse a quem não é pau!
16 Pelo que o Senhor, o Senhor dos Exércitos, enviará a tísica contra os seus homens, todos gordos, e debaixo da sua glória acenderá uma queima, como a queima de fogo.
17 Porque a Luz de Israel virá a ser como fogo, e o seu Santo, como labareda, que abrase e consuma os espinheiros e os abrolhos da Assíria, num só dia.
18 Também consumirá a glória da sua floresta e do seu campo fértil, desde a alma até ao corpo; e será como quando um doente se definha.
19 O resto das árvores da sua floresta será tão pouco, que um menino saberá escrever o número delas.
20 Acontecerá, naquele dia, que os restantes de Israel e os da casa de Jacó que se tiverem salvado nunca mais se estribarão naquele que os feriu, mas, com efeito, se estribarão no Senhor, o Santo de Israel.
21 Os restantes se converterão ao Deus forte, sim, os restantes de Jacó.
22 Porque ainda que o teu povo, ó Israel, seja como a areia do mar, o restante se converterá; destruição será determinada, transbordante de justiça.
23 Porque uma destruição, e essa já determinada, o Senhor, o Senhor dos Exércitos, a executará no meio de toda esta terra.
24 Pelo que assim diz o Senhor, o Senhor dos Exércitos: Povo meu, que habitas em Sião, não temas a Assíria, quando te ferir com a vara e contra ti levantar o seu bastão à maneira dos egípcios;
25 porque daqui a bem pouco se cumprirá a minha indignação e a minha ira, para a consumir.
26 Porque o Senhor dos Exércitos suscitará contra ela um flagelo, como a matança de Midiã junto à penha de Orebe; a sua vara estará sobre o mar, e ele a levantará como fez no Egito.
27 Acontecerá, naquele dia, que o peso será tirado do teu ombro, e o seu jugo, do teu pescoço, jugo que será despedaçado por causa da gordura.
28 A Assíria vem a Aiate, passa por Migrom e em Micmás larga a sua bagagem.
29 Passa o desfiladeiro, aloja-se em Geba, já Ramá treme, Gibeá de Saul foge.
30 Ergue com estrídulo a voz, ó filha de Galim! Ouve, ó Laís! Oh! Pobre Anatote!
31 Madmena se dispersa; os moradores de Gebim fogem para salvar-se.
32 Nesse mesmo dia, a Assíria parará em Nobe; agitará o punho ao monte da filha de Sião, o outeiro de Jerusalém.
33 Mas eis que o Senhor, o Senhor dos Exércitos, cortará os ramos com violência, as árvores de alto porte serão derribadas, e as altivas serão abatidas.
34 Cortará com o ferro as brenhas da floresta, e o Líbano cairá pela mão de um poderoso.*
1 Do tronco de Jessé sairá um rebento, e das suas raízes, um renovo.
2 Repousará sobre ele o Espírito do Senhor, o Espírito de sabedoria e de entendimento, o Espírito de conselho e de fortaleza, o Espírito de conhecimento e de temor do Senhor.
3 Deleitar-se-á no temor do Senhor; não julgará segundo a vista dos seus olhos, nem repreenderá segundo o ouvir dos seus ouvidos;
4 mas julgará com justiça os pobres e decidirá com equidade a favor dos mansos da terra; ferirá a terra com a vara de sua boca e com o sopro dos seus lábios matará o perverso.
5 A justiça será o cinto dos seus lombos, e a fidelidade, o cinto dos seus rins.
6 O lobo habitará com o cordeiro, e o leopardo se deitará junto ao cabrito; o bezerro, o leão novo e o animal cevado andarão juntos, e um pequenino os guiará.
7 A vaca e a ursa pastarão juntas, e as suas crias juntas se deitarão; o leão comerá palha como o boi.
8 A criança de peito brincará sobre a toca da áspide, e o já desmamado meterá a mão na cova do basilisco.
9 Não se fará mal nem dano algum em todo o meu santo monte, porque a terra se encherá do conhecimento do Senhor, como as águas cobrem o mar.
10 Naquele dia, recorrerão as nações à raiz de Jessé que está posta por estandarte dos povos; a glória lhe será a morada.
11 Naquele dia, o Senhor tornará a estender a mão para resgatar o restante do seu povo, que for deixado, da Assíria, do Egito, de Patros, da Etiópia, de Elão, de Sinar, de Hamate e das terras do mar.
12 Levantará um estandarte para as nações, ajuntará os desterrados de Israel e os dispersos de Judá recolherá desde os quatro confins da terra.
13 Afastar-se-á a inveja de Efraim, e os adversários de Judá serão eliminados; Efraim não invejará a Judá, e Judá não oprimirá a Efraim.
14 Antes, voarão para sobre os ombros dos filisteus ao Ocidente; juntos, despojarão os filhos do Oriente; contra Edom e Moabe lançarão as mãos, e os filhos de Amom lhes serão sujeitos.
15 O Senhor destruirá totalmente o braço do mar do Egito, e com a força do seu vento moverá a mão contra o Eufrates, e, ferindo-o, dividi-lo-á em sete canais, de sorte que qualquer o atravessará de sandálias.
16 Haverá caminho plano para o restante do seu povo, que for deixado, da Assíria, como o houve para Israel no dia em que subiu da terra do Egito.*
1 Orarás naquele dia: Graças te dou, ó Senhor, porque, ainda que te iraste contra mim, a tua ira se retirou, e tu me consolas.
2 Eis que Deus é a minha salvação; confiarei e não temerei, porque o Senhor Deus é a minha força e o meu cântico; ele se tornou a minha salvação.
3 Vós, com alegria, tirareis água das fontes da salvação.
4 Direis naquele dia: Dai graças ao Senhor, invocai o seu nome, tornai manifestos os seus feitos entre os povos, relembrai que é excelso o seu nome.
5 Cantai louvores ao Senhor, porque fez coisas grandiosas; saiba-se isto em toda a terra.
6 Exulta e jubila, ó habitante de Sião, porque grande é o Santo de Israel no meio de ti.*
1 Sentença que, numa visão, recebeu Isaías, filho de Amoz, contra a Babilônia.
2 Alçai um estandarte sobre o monte escalvado; levantai a voz para eles; acenai-lhes com a mão, para que entrem pelas portas dos tiranos.
3 Eu dei ordens aos meus consagrados, sim, chamei os meus valentes para executarem a minha ira, os que com exultação se orgulham.
4 Já se ouve sobre os montes o rumor como o de muito povo, o clamor de reinos e de nações já congregados. O Senhor dos Exércitos passa revista às tropas de guerra.
5 Já vêm de um país remoto, desde a extremidade do céu, o Senhor e os instrumentos da sua indignação, para destruir toda a terra.
6 Uivai, pois está perto o Dia do Senhor; vem do Todo-Poderoso como assolação.
7 Pelo que todos os braços se tornarão frouxos, e o coração de todos os homens se derreterá.
8 Assombrar-se-ão, e apoderar-se-ão deles dores e ais, e terão contorções como a mulher parturiente; olharão atônitos uns para outros; o seu rosto se tornará rosto flamejante.
9 Eis que vem o Dia do Senhor, dia cruel, com ira e ardente furor, para converter a terra em assolação e dela destruir os pecadores.
10 Porque as estrelas e constelações dos céus não darão a sua luz; o sol, logo ao nascer, se escurecerá, e a lua não fará resplandecer a sua luz.
11 Castigarei o mundo por causa da sua maldade e os perversos, por causa da sua iniquidade; farei cessar a arrogância dos atrevidos e abaterei a soberba dos violentos.
12 Farei que os homens sejam mais escassos do que o ouro puro, mais raros do que o ouro de Ofir.
13 Portanto, farei estremecer os céus; e a terra será sacudida do seu lugar, por causa da ira do Senhor dos Exércitos e por causa do dia do seu ardente furor.
14 Cada um será como a gazela que foge e como o rebanho que ninguém recolhe; cada um voltará para o seu povo e cada um fugirá para a sua terra.
15 Quem for achado será traspassado; e aquele que for apanhado cairá à espada.
16 Suas crianças serão esmagadas perante eles; a sua casa será saqueada, e sua mulher, violada.
17 Eis que eu despertarei contra eles os medos, que não farão caso de prata, nem tampouco desejarão ouro.
18 Os seus arcos matarão os jovens; eles não se compadecerão do fruto do ventre; os seus olhos não pouparão as crianças.
19 Babilônia, a joia dos reinos, glória e orgulho dos caldeus, será como Sodoma e Gomorra, quando Deus as transtornou.
20 Nunca jamais será habitada, ninguém morará nela de geração em geração; o arábio não armará ali a sua tenda, nem tampouco os pastores farão ali deitar os seus rebanhos.
21 Porém, nela, as feras do deserto repousarão, e as suas casas se encherão de corujas; ali habitarão os avestruzes, e os sátiros pularão ali.
22 As hienas uivarão nos seus castelos; os chacais, nos seus palácios de prazer; está prestes a chegar o seu tempo, e os seus dias não se prolongarão.*
1 Porque o Senhor se compadecerá de Jacó, e ainda elegerá a Israel, e os porá na sua própria terra; e unir-se-ão a eles os estrangeiros, e estes se achegarão à casa de Jacó.
2 Os povos os tomarão e os levarão aos lugares deles, e a casa de Israel possuirá esses povos por servos e servas, na terra do Senhor; cativarão aqueles que os cativaram e dominarão os seus opressores.
3 No dia em que Deus vier a dar-te descanso do teu trabalho, das tuas angústias e da dura servidão com que te fizeram servir,
4 então, proferirás este motejo contra o rei da Babilônia e dirás: Como cessou o opressor! Como acabou a tirania!
5 Quebrou o Senhor a vara dos perversos e o cetro dos dominadores,
6 que feriam os povos com furor, com golpes incessantes, e com ira dominavam as nações, com perseguição irreprimível.
7 Já agora descansa e está sossegada toda a terra. Todos exultam de júbilo.
8 Até os ciprestes se alegram sobre ti, e os cedros do Líbano exclamam: Desde que tu caíste, ninguém já sobe contra nós para nos cortar.
9 O além, desde o profundo, se turba por ti, para te sair ao encontro na tua chegada; ele, por tua causa, desperta as sombras e todos os príncipes da terra e faz levantar dos seus tronos a todos os reis das nações.
10 Todos estes respondem e te dizem: Tu também, como nós, estás fraco? E és semelhante a nós?
11 Derribada está na cova a tua soberba, e, também, o som da tua harpa; por baixo de ti, uma cama de gusanos, e os vermes são a tua coberta.
12 Como caíste do céu, ó estrela da manhã, filho da alva! Como foste lançado por terra, tu que debilitavas as nações!
13 Tu dizias no teu coração: Eu subirei ao céu; acima das estrelas de Deus exaltarei o meu trono e no monte da congregação me assentarei, nas extremidades do Norte;
14 subirei acima das mais altas nuvens e serei semelhante ao Altíssimo.
15 Contudo, serás precipitado para o reino dos mortos, no mais profundo do abismo.
16 Os que te virem te contemplarão, hão de fitar-te e dizer-te: É este o homem que fazia estremecer a terra e tremer os reinos?
17 Que punha o mundo como um deserto e assolava as suas cidades? Que a seus cativos não deixava ir para casa?
18 Todos os reis das nações, sim, todos eles, jazem com honra, cada um, no seu túmulo.
19 Mas tu és lançado fora da tua sepultura, como um renovo bastardo, coberto de mortos traspassados à espada, cujo cadáver desce à cova e é pisado de pedras.
20 Com eles não te reunirás na sepultura, porque destruíste a tua terra e mataste o teu povo; a descendência dos malignos jamais será nomeada.
21 Preparai a matança para os filhos, por causa da maldade de seus pais, para que não se levantem, e possuam a terra, e encham o mundo de cidades.
22 Levantar-me-ei contra eles, diz o Senhor dos Exércitos; exterminarei de Babilônia o nome e os sobreviventes, os descendentes e a posteridade, diz o Senhor.
23 Reduzi-la-ei a possessão de ouriços e a lagoas de águas; varrê-la-ei com a vassoura da destruição, diz o Senhor dos Exércitos.
24 Jurou o Senhor dos Exércitos, dizendo: Como pensei, assim sucederá, e, como determinei, assim se efetuará.
25 Quebrantarei a Assíria na minha terra e nas minhas montanhas a pisarei, para que o seu jugo se aparte de Israel, e a sua carga se desvie dos ombros dele.
26 Este é o desígnio que se formou concernente a toda a terra; e esta é a mão que está estendida sobre todas as nações.
27 Porque o Senhor dos Exércitos o determinou; quem, pois, o invalidará? A sua mão está estendida; quem, pois, a fará voltar atrás?
28 No ano em que morreu o rei Acaz, foi pronunciada esta sentença:
29 Não te alegres, tu, toda a Filístia, por estar quebrada a vara que te feria; porque da estirpe da cobra sairá uma áspide, e o seu fruto será uma serpente voadora.
30 Os primogênitos dos pobres serão apascentados, e os necessitados se deitarão seguros; mas farei morrer de fome a tua raiz, e serão destruídos os teus sobreviventes.
31 Uiva, ó porta; grita, ó cidade; tu, ó Filístia toda, treme; porque do Norte vem fumaça, e ninguém há que se afaste das fileiras.
32 Que se responderá, pois, aos mensageiros dos gentios? Que o Senhor fundou a Sião, e nela encontram refúgio os aflitos do seu povo.*
1 Sentença contra Moabe. Certamente, numa noite foi assolada Ar de Moabe e ela está destruída; certamente, numa noite foi assolada Quir de Moabe e ela está destruída.
2 Sobe-se ao templo e a Dibom, aos altos, para chorar; nos montes Nebo e Medeba, lamenta Moabe; todas as cabeças se tornam calvas, e toda barba é rapada.
3 Cingem-se de panos de saco nas suas ruas; nos seus terraços e nas suas praças, andam todos uivando e choram abundantemente.
4 Tanto Hesbom como Eleale andam gritando; até Jaza se ouve a sua voz; por isso, os armados de Moabe clamam; a sua alma treme dentro dele.
5 O meu coração clama por causa de Moabe, cujos fugitivos vão até Zoar, novilha de três anos; vão chorando pela subida de Luíte e no caminho de Horonaim levantam grito de desespero;
6 porque as águas de Ninrim desaparecem; seca-se o pasto, acaba-se a erva, e já não há verdura alguma,
7 pelo que o que pouparam, o que ganharam e depositaram eles mesmos levam para além das torrentes dos salgueiros;
8 porque o pranto rodeia os limites de Moabe; até Eglaim chega o seu clamor, e ainda até Beer-Elim, o seu lamento;
9 porque as águas de Dimom estão cheias de sangue; pois ainda acrescentarei a Dimom: leões contra aqueles que escaparem de Moabe e contra os restantes da terra.*
1 Enviai cordeiros ao dominador da terra, desde Sela, pelo deserto, até ao monte da filha de Sião.
2 Como pássaro espantado, lançado fora do ninho, assim são as filhas de Moabe nos vaus do Arnom, que dizem:
3 Dá conselhos, executa o juízo e faze a tua sombra no pino do meio-dia como a noite; esconde os desterrados e não descubras os fugitivos.
4 Habitem entre ti os desterrados de Moabe, serve-lhes de esconderijo contra o destruidor. Quando o homem violento tiver fim, a destruição for desfeita e o opressor deixar a terra,
5 então, um trono se firmará em benignidade, e sobre ele no tabernáculo de Davi se assentará com fidelidade um que julgue, busque o juízo e não tarde em fazer justiça.
6 Temos ouvido da soberba de Moabe, soberbo em extremo; da sua arrogância, do seu orgulho e do seu furor; a sua jactância é vã.
7 Portanto, uivará Moabe, cada um por Moabe; gemereis profundamente abatidos pelas pastas de uvas de Quir-Haresete.
8 Porque os campos de Hesbom estão murchos; os senhores das nações talaram os melhores ramos da vinha de Sibma, que se estenderam até Jazer e se perderam no deserto, sarmentos que se estenderam e passaram além do mar.
9 Pelo que prantearei, com o pranto de Jazer, a vinha de Sibma; regar-te-ei com as minhas lágrimas, ó Hesbom, ó Eleale; pois, sobre os teus frutos de verão e sobre a tua vindima, caiu já dos inimigos o eia, como o de pisadores.
10 Fugiu a alegria e o regozijo do pomar; nas vinhas já não se canta, nem há júbilo algum; já não se pisarão as uvas nos lagares. Eu fiz cessar o eia dos pisadores.
11 Pelo que por Moabe vibra como harpa o meu íntimo, e o meu coração, por Quir-Heres.
12 Ver-se-á como Moabe se cansa nos altos, como entra no santuário a orar e nada alcança.
13 Esta é a palavra que o Senhor há muito pronunciou contra Moabe.
14 Agora, porém, o Senhor fala e diz: Dentro de três anos, tais como os de jornaleiros, será envilecida a glória de Moabe, com toda a sua grande multidão; e o restante será pouco, pequeno e débil.*
1 Sentença contra Damasco. Eis que Damasco deixará de ser cidade e será um montão de ruínas.
2 As cidades de Aroer serão abandonadas; hão de ser para os rebanhos, que aí se deitarão sem haver quem os espante.
3 A fortaleza de Efraim desaparecerá, como também o reino de Damasco e o restante da Síria; serão como a glória dos filhos de Israel, diz o Senhor dos Exércitos.
4 Naquele dia, a glória de Jacó será apoucada, e a gordura da sua carne desaparecerá.
5 Será, quando o segador ajunta a cana do trigo e com o braço sega as espigas, como quem colhe espigas, como quem colhe espigas no vale dos Refains.
6 Mas ainda ficarão alguns rabiscos, como no sacudir da oliveira; duas ou três azeitonas na ponta do ramo mais alto, e quatro ou cinco nos ramos mais exteriores de uma árvore frutífera, diz o Senhor, Deus de Israel.
7 Naquele dia, olhará o homem para o seu Criador, e os seus olhos atentarão para o Santo de Israel.
8 E não olhará para os altares, obra das suas mãos, nem atentará para o que fizeram seus dedos, nem para os postes-ídolos, nem para os altares do incenso.
9 Naquele dia, serão as suas cidades fortes como os lugares abandonados no bosque ou sobre o cimo das montanhas, os quais outrora foram abandonados ante os filhos de Israel, e haverá assolação;
10 porquanto te esqueceste do Deus da tua salvação e não te lembraste da Rocha da tua fortaleza. Ainda que faças plantações formosas e plantes mudas de fora,
11 e, no dia em que as plantares, as fizeres crescer, e na manhã seguinte as fizeres florescer, ainda assim a colheita voará no dia da tribulação e das dores incuráveis.
12 Ai do bramido dos grandes povos que bramam como bramam os mares, e do rugido das nações que rugem como rugem as impetuosas águas!
13 Rugirão as nações, como rugem as muitas águas, mas Deus as repreenderá, e fugirão para longe; serão afugentadas como a palha dos montes diante do vento e como pó levado pelo tufão.
14 Ao anoitecer, eis que há pavor, e, antes que amanheça o dia, já não existem. Este é o quinhão daqueles que nos despojam e a sorte daqueles que nos saqueiam.*
1 Ai da terra onde há o roçar de muitas asas de insetos, que está além dos rios da Etiópia;
2 que envia embaixadores por mar em navios de papiro sobre as águas, dizendo: Ide, mensageiros velozes, a uma nação de homens altos e de pele brunida, a um povo terrível, de perto e de longe; a uma nação poderosa e esmagadora, cuja terra os rios dividem.
3 Vós, todos os habitantes do mundo, e vós, os moradores da terra, quando se arvorar a bandeira nos montes, olhai; e, quando se tocar a trombeta, escutai.
4 Porque assim me disse o Senhor: Olhando da minha morada, estarei calmo como o ardor quieto do sol resplandecente, como a nuvem do orvalho no calor da sega.
5 Porque antes da vindima, caída já a flor, e quando as uvas amadurecem, então, podará os sarmentos com a foice e cortará os ramos que se estendem.
6 Serão deixados juntos às aves dos montes e aos animais da terra; sobre eles veranearão as aves de rapina, e todos os animais da terra passarão o inverno sobre eles.
7 Naquele tempo, será levado um presente ao Senhor dos Exércitos por um povo de homens altos e de pele brunida, povo terrível, de perto e de longe; por uma nação poderosa e esmagadora, cuja terra os rios dividem, ao lugar do nome do Senhor dos Exércitos, ao monte Sião.*
1 Sentença contra o Egito. Eis que o Senhor, cavalgando uma nuvem ligeira, vem ao Egito; os ídolos do Egito estremecerão diante dele, e o coração dos egípcios se derreterá dentro deles.
2 Porque farei com que egípcios se levantem contra egípcios, e cada um pelejará contra o seu irmão e cada um contra seu próximo; cidade contra cidade, reino contra reino.
3 O espírito dos egípcios se esvaecerá dentro deles, e anularei o seu conselho; eles consultarão os seus ídolos, e encantadores, e necromantes, e feiticeiros.
4 Entregarei os egípcios nas mãos de um senhor duro, e um rei feroz os dominará, diz o Senhor, o Senhor dos Exércitos.
5 Secarão as águas do Nilo, e o rio se tornará seco e árido.
6 Os canais exalarão mau cheiro, e os braços do Nilo diminuirão e se esgotarão; as canas e os juncos se murcharão.
7 A relva que está junto ao Nilo, junto às suas ribanceiras, e tudo o que foi semeado junto dele se secarão, serão levados pelo vento e não subsistirão.
8 Os pescadores gemerão, suspirarão todos os que lançam anzol ao rio, e os que estendem rede sobre as águas desfalecerão.
9 Consternar-se-ão os que trabalham em linho fino e os que tecem pano de algodão.
10 Os seus grandes serão esmagados, e todos os jornaleiros andarão de alma entristecida.
11 Na verdade, são néscios os príncipes de Zoã; os sábios conselheiros de Faraó dão conselhos estúpidos; como, pois, direis a Faraó: Sou filho de sábios, filho de antigos reis?
12 Onde estão agora os teus sábios? Anunciem-te agora ou informem-te do que o Senhor dos Exércitos determinou contra o Egito.
13 Loucos se tornaram os príncipes de Zoã, enganados estão os príncipes de Mênfis; fazem errar o Egito os que são a pedra de esquina das suas tribos.
14 O Senhor derramou no coração deles um espírito estonteante; eles fizeram estontear o Egito em toda a sua obra, como o bêbado quando cambaleia no seu vômito.
15 Não aproveitará ao Egito obra alguma que possa ser feita pela cabeça ou cauda, pela palma ou junco.
16 Naquele dia, os egípcios serão como mulheres; tremerão e temerão ao levantar-se da mão do Senhor dos Exércitos, que ele agitará contra eles.
17 A terra de Judá será espanto para o Egito; todo aquele que dela se lembrar encher-se-á de pavor por causa do propósito do Senhor dos Exércitos, do que determinou contra eles.
18 Naquele dia, haverá cinco cidades na terra do Egito que falarão a língua de Canaã e farão juramento ao Senhor dos Exércitos; uma delas se chamará Cidade do Sol.
19 Naquele dia, o Senhor terá um altar no meio da terra do Egito, e uma coluna se erigirá ao Senhor na sua fronteira.
20 Servirá de sinal e de testemunho ao Senhor dos Exércitos na terra do Egito; ao Senhor clamarão por causa dos opressores, e ele lhes enviará um salvador e defensor que os há de livrar.
21 O Senhor se dará a conhecer ao Egito, e os egípcios conhecerão o Senhor naquele dia; sim, eles o adorarão com sacrifícios e ofertas de manjares, e farão votos ao Senhor, e os cumprirão.
22 Ferirá o Senhor os egípcios, ferirá, mas os curará; converter-se-ão ao Senhor, e ele lhes atenderá as orações e os curará.
23 Naquele dia, haverá estrada do Egito até à Assíria, os assírios irão ao Egito, e os egípcios, à Assíria; e os egípcios adorarão com os assírios.
24 Naquele dia, Israel será o terceiro com os egípcios e os assírios, uma bênção no meio da terra;
25 porque o Senhor dos Exércitos os abençoará, dizendo: Bendito seja o Egito, meu povo, e a Assíria, obra de minhas mãos, e Israel, minha herança.*
1 No ano em que Tartã, enviado por Sargão, rei da Assíria, veio a Asdode, e a guerreou, e a tomou,
2 nesse mesmo tempo, falou o Senhor por intermédio de Isaías, filho de Amoz, dizendo: Vai, solta de teus lombos o pano grosseiro de profeta e tira dos pés o calçado. Assim ele o fez, indo despido e descalço.
3 Então, disse o Senhor: Assim como Isaías, meu servo, andou três anos despido e descalço, por sinal e prodígio contra o Egito e contra a Etiópia,
4 assim o rei da Assíria levará os presos do Egito e os exilados da Etiópia, tanto moços como velhos, despidos e descalços e com as nádegas descobertas, para vergonha do Egito.
5 Então, se assombrarão os israelitas e se envergonharão por causa dos etíopes, sua esperança, e dos egípcios, sua glória.
6 Os moradores desta região dirão naquele dia: Vede, foi isto que aconteceu àqueles em quem esperávamos e a quem fugimos por socorro, para livrar-nos do rei da Assíria! Como, pois, escaparemos nós?*
1 Sentença contra o deserto do mar. Como os tufões vêm do Sul, ele virá do deserto, da horrível terra.
2 Dura visão me foi anunciada: o pérfido procede perfidamente, e o destruidor anda destruindo. Sobe, ó Elão, sitia, ó Média; já fiz cessar todo gemer.
3 Pelo que os meus lombos estão cheios de angústias; dores se apoderaram de mim como as de parturiente; contorço-me de dores e não posso ouvir, desfaleço-me e não posso ver.
4 O meu coração cambaleia, o horror me apavora; a noite que eu desejava se me tornou em tremores.
5 Põe-se a mesa, estendem-se tapetes, come-se e bebe-se. Levantai-vos, príncipes, untai o escudo.
6 Pois assim me disse o Senhor: Vai, põe o atalaia, e ele que diga o que vir.
7 Quando vir uma tropa de cavaleiros de dois a dois, uma tropa de jumentos e uma tropa de camelos, ele que escute diligentemente com grande atenção.
8 Então, o atalaia gritou como um leão: Senhor, sobre a torre de vigia estou em pé continuamente durante o dia e de guarda me ponho noites inteiras.
9 Eis agora vem uma tropa de homens, cavaleiros de dois a dois. Então, ergueu ele a voz e disse: Caiu, caiu Babilônia; e todas as imagens de escultura dos seus deuses jazem despedaçadas por terra.
10 Oh! Povo meu, debulhado e batido como o trigo da minha eira! O que ouvi do Senhor dos Exércitos, Deus de Israel, isso vos anunciei.
11 Sentença contra Dumá. Gritam-me de Seir: Guarda, a que hora estamos da noite? Guarda, a que horas?
12 Respondeu o guarda: Vem a manhã, e também a noite; se quereis perguntar, perguntai; voltai, vinde.
13 Sentença contra a Arábia. Nos bosques da Arábia, passareis a noite, ó caravanas de dedanitas.
14 Traga-se água ao encontro dos sedentos; ó moradores da terra de Tema, levai pão aos fugitivos.
15 Porque fogem de diante das espadas, de diante da espada nua, de diante do arco armado e de diante do furor da guerra.
16 Porque assim me disse o Senhor: Dentro de um ano, tal como o de jornaleiro, toda a glória de Quedar desaparecerá.
17 E o restante do número dos flecheiros, os valentes dos filhos de Quedar, será diminuto, porque assim o disse o Senhor, Deus de Israel.*
1 Sentença contra o vale da Visão. Que tens agora, que todo o teu povo sobe aos telhados?
2 Tu, cidade que estavas cheia de aclamações, cidade estrepitosa, cidade alegre! Os teus mortos não foram mortos à espada, nem morreram na guerra.
3 Todos os teus príncipes fogem à uma e são presos sem que se use o arco; todos os teus que foram encontrados foram presos, sem embargo de já estarem longe na fuga.
4 Portanto, digo: desviai de mim a vista e chorarei amargamente; não insistais por causa da ruína da filha do meu povo.
5 Porque dia de alvoroço, de atropelamento e confusão é este da parte do Senhor, o Senhor dos Exércitos, no vale da Visão: um derribar de muros e clamor que vai até aos montes.
6 Porque Elão tomou a aljava e vem com carros e cavaleiros; e Quir descobre os escudos.
7 Os teus mais formosos vales se enchem de carros, e os cavaleiros se põem em ordem às portas.
8 Tira-se a proteção de Judá. Naquele dia, olharás para as armas da Casa do Bosque.
9 Notareis as brechas da Cidade de Davi, por serem muitas, e ajuntareis as águas do açude inferior.
10 Também contareis as casas de Jerusalém e delas derribareis, para fortalecer os muros.
11 Fareis também um reservatório entre os dois muros para as águas do açude velho, mas não cogitais de olhar para cima, para aquele que suscitou essas calamidades, nem considerais naquele que há muito as formou.
12 O Senhor, o Senhor dos Exércitos, vos convida naquele dia para chorar, prantear, rapar a cabeça e cingir o cilício.
13 Porém é só gozo e alegria que se veem; matam-se bois, degolam-se ovelhas, come-se carne, bebe-se vinho e se diz: Comamos e bebamos, que amanhã morreremos.
14 Mas o Senhor dos Exércitos se declara aos meus ouvidos, dizendo: Certamente, esta maldade não será perdoada, até que morrais, diz o Senhor, o Senhor dos Exércitos.
15 Assim diz o Senhor, o Senhor dos Exércitos: Anda, vai ter com esse administrador, com Sebna, o mordomo, e pergunta-lhe:
16 Que é que tens aqui? Ou a quem tens tu aqui, para que abrisses aqui uma sepultura, lavrando em lugar alto a tua sepultura, cinzelando na rocha a tua própria morada?
17 Eis que como homem forte o Senhor te arrojará violentamente; agarrar-te-á com firmeza,
18 enrolar-te-á num invólucro e te fará rolar como uma bola para terra espaçosa; ali morrerás, e ali acabarão os carros da tua glória, ó tu, vergonha da casa do teu senhor.
19 Eu te lançarei fora do teu posto, e serás derribado da tua posição.
20 Naquele dia, chamarei a meu servo Eliaquim, filho de Hilquias,
21 vesti-lo-ei da tua túnica, cingi-lo-ei com a tua faixa e lhe entregarei nas mãos o teu poder, e ele será como pai para os moradores de Jerusalém e para a casa de Judá.
22 Porei sobre o seu ombro a chave da casa de Davi; ele abrirá, e ninguém fechará, fechará, e ninguém abrirá.
23 Fincá-lo-ei como estaca em lugar firme, e ele será como um trono de honra para a casa de seu pai.
24 Nele, pendurarão toda a responsabilidade da casa de seu pai, a prole e os descendentes, todos os utensílios menores, desde as taças até as garrafas.
25 Naquele dia, diz o Senhor dos Exércitos, a estaca que fora fincada em lugar firme será tirada, será arrancada e cairá, e a carga que nela estava se desprenderá, porque o Senhor o disse.*
1 Sentença contra Tiro. Uivai, navios de Társis, porque está assolada, a ponto de não haver nela casa nenhuma, nem ancoradouro. Da terra de Chipre lhes foi isto revelado.
2 Calai-vos, moradores do litoral, vós a quem os mercadores de Sidom enriqueceram, navegando pelo mar.
3 Através das vastas águas, vinha o cereal dos canais do Egito e a ceifa do Nilo, como a tua renda, Tiro, que vieste a ser a feira das nações.
4 Envergonha-te, ó Sidom, porque o mar, a fortaleza do mar, fala, dizendo: Não tive dores de parto, não dei à luz, não criei rapazes, nem eduquei donzelas.
5 Quando a notícia a respeito de Tiro chegar ao Egito, com ela se angustiarão os homens.
6 Passai a Társis, uivai, moradores do litoral.
7 É esta, acaso, a vossa cidade que andava exultante, cuja origem data de remotos dias, cujos pés a levaram até longe para estabelecer-se?
8 Quem formou este desígnio contra Tiro, a cidade distribuidora de coroas, cujos mercadores são príncipes e cujos negociantes são os mais nobres da terra?
9 O Senhor dos Exércitos formou este desígnio para denegrir a soberba de toda beleza e envilecer os mais nobres da terra.
10 Percorre livremente como o Nilo a tua terra, ó filha de Társis; já não há quem te restrinja.
11 O Senhor estendeu a mão sobre o mar e turbou os reinos; deu ordens contra Canaã, para que se destruíssem as suas fortalezas.
12 E disse: Nunca mais exultarás, ó oprimida virgem filha de Sidom; levanta-te, passa a Chipre, mas ainda ali não terás descanso.
13 Eis a terra dos caldeus, povo que até há pouco não era povo e que a Assíria destinara para os sátiros do deserto; povo que levantou suas torres, e arrasou os palácios de Tiro, e os converteu em ruínas.
14 Uivai, navios de Társis, porque é destruída a que era a vossa fortaleza!
15 Naquele dia, Tiro será posta em esquecimento por setenta anos, segundo os dias de um rei; mas no fim dos setenta anos dar-se-á com Tiro o que consta na canção da meretriz:
16 Toma a harpa, rodeia a cidade, ó meretriz, entregue ao esquecimento; canta bem, toca, multiplica as tuas canções, para que se recordem de ti.
17 Findos os setenta anos, o Senhor atentará para Tiro, e ela tornará ao salário da sua impureza e se prostituirá com todos os reinos da terra.
18 O ganho e o salário de sua impureza serão dedicados ao Senhor; não serão entesourados, nem guardados, mas o seu ganho será para os que habitam perante o Senhor, para que tenham comida em abundância e vestes finas.*
1 Eis que o Senhor vai devastar e desolar a terra, vai transtornar a sua superfície e lhe dispersar os moradores.
2 O que suceder ao povo sucederá ao sacerdote; ao servo, como ao seu senhor; à serva, como à sua dona; ao comprador, como ao vendedor; ao que empresta, como ao que toma emprestado; ao credor, como ao devedor.
3 A terra será de todo devastada e totalmente saqueada, porque o Senhor é quem proferiu esta palavra.
4 A terra pranteia e se murcha; o mundo enfraquece e se murcha; enlanguescem os mais altos do povo da terra.
5 Na verdade, a terra está contaminada por causa dos seus moradores, porquanto transgridem as leis, violam os estatutos e quebram a aliança eterna.
6 Por isso, a maldição consome a terra, e os que habitam nela se tornam culpados; por isso, serão queimados os moradores da terra, e poucos homens restarão.
7 Pranteia o vinho, enlanguesce a vide, e gemem todos os que estavam de coração alegre.
8 Cessou o folguedo dos tamboris, acabou o ruído dos que exultam, e descansou a alegria da harpa.
9 Já não se bebe vinho entre canções; a bebida forte é amarga para os que a bebem.
10 Demolida está a cidade caótica, todas as casas estão fechadas, ninguém já pode entrar.
11 Gritam por vinho nas ruas, fez-se noite para toda alegria, foi banido da terra o prazer.
12 Na cidade, reina a desolação, e a porta está reduzida a ruínas.
13 Porque será na terra, no meio destes povos, como o varejar da oliveira e como o rebuscar, quando está acabada a vindima.
14 Eles levantam a voz e cantam com alegria; por causa da glória do Senhor, exultam desde o mar.
15 Por isso, glorificai ao Senhor no Oriente e, nas terras do mar, ao nome do Senhor, Deus de Israel.
16 Dos confins da terra ouvimos cantar: Glória ao Justo!
Mas eu digo: definho, definho, ai de mim! Os pérfidos tratam perfidamente; sim, os pérfidos tratam mui perfidamente.
17 Terror, cova e laço vêm sobre ti, ó morador da terra.
18 E será que aquele que fugir da voz do terror cairá na cova, e, se sair da cova, o laço o prenderá; porque as represas do alto se abrem, e tremem os fundamentos da terra.
19 A terra será de todo quebrantada, ela totalmente se romperá, a terra violentamente se moverá.
20 A terra cambaleará como um bêbado e balanceará como rede de dormir; a sua transgressão pesa sobre ela, ela cairá e jamais se levantará.
21 Naquele dia, o Senhor castigará, no céu, as hostes celestes, e os reis da terra, na terra.
22 Serão ajuntados como presos em masmorra, e encerrados num cárcere, e castigados depois de muitos dias.
23 A lua se envergonhará, e o sol se confundirá quando o Senhor dos Exércitos reinar no monte Sião e em Jerusalém; perante os seus anciãos haverá glória.*
1 Ó Senhor, tu és o meu Deus; exaltar-te-ei a ti e louvarei o teu nome, porque tens feito maravilhas e tens executado os teus conselhos antigos, fiéis e verdadeiros.
2 Porque da cidade fizeste um montão de pedras e da cidade forte, uma ruína; a fortaleza dos estranhos já não é cidade e jamais será reedificada.
3 Pelo que povos fortes te glorificarão, e a cidade das nações opressoras te temerá.
4 Porque foste a fortaleza do pobre e a fortaleza do necessitado na sua angústia; refúgio contra a tempestade e sombra contra o calor; porque dos tiranos o bufo é como a tempestade contra o muro,
5 como o calor em lugar seco. Tu abaterás o ímpeto dos estranhos; como se abranda o calor pela sombra da espessa nuvem, assim o hino triunfal dos tiranos será aniquilado.
6 O Senhor dos Exércitos dará neste monte a todos os povos um banquete de coisas gordurosas, uma festa com vinhos velhos, pratos gordurosos com tutanos e vinhos velhos bem-clarificados.
7 Destruirá neste monte a coberta que envolve todos os povos e o véu que está posto sobre todas as nações.
8 Tragará a morte para sempre, e, assim, enxugará o Senhor Deus as lágrimas de todos os rostos, e tirará de toda a terra o opróbrio do seu povo, porque o Senhor falou.
9 Naquele dia, se dirá: Eis que este é o nosso Deus, em quem esperávamos, e ele nos salvará; este é o Senhor, a quem aguardávamos; na sua salvação exultaremos e nos alegraremos.
10 Porque a mão do Senhor descansará neste monte; mas Moabe será trilhado no seu lugar, como se pisa a palha na água da cova da esterqueira;
11 no meio disto estenderá ele as mãos, como as estende o nadador para nadar; mas o Senhor lhe abaterá a altivez, não obstante a perícia das suas mãos;
12 e abaixará as altas fortalezas dos seus muros; abatê-las-á e derribá-las-á por terra, até ao pó.*
1 Naquele dia, se entoará este cântico na terra de Judá: Temos uma cidade forte; Deus lhe põe a salvação por muros e baluartes.
2 Abri vós as portas, para que entre a nação justa, que guarda a fidelidade.
3 Tu, Senhor, conservarás em perfeita paz aquele cujo propósito é firme; porque ele confia em ti.
4 Confiai no Senhor perpetuamente, porque o Senhor Deus é uma rocha eterna;
5 porque ele abate os que habitam no alto, na cidade elevada; abate-a, humilha-a até à terra e até ao pó.
6 O pé a pisará; os pés dos aflitos, e os passos dos pobres.
7 A vereda do justo é plana; tu, que és justo, aplanas a vereda do justo.
8 Também através dos teus juízos, Senhor, te esperamos; no teu nome e na tua memória está o desejo da nossa alma.
9 Com minha alma suspiro de noite por ti e, com o meu espírito dentro de mim, eu te procuro diligentemente; porque, quando os teus juízos reinam na terra, os moradores do mundo aprendem justiça.
10 Ainda que se mostre favor ao perverso, nem por isso aprende a justiça; até na terra da retidão ele comete a iniquidade e não atenta para a majestade do Senhor.
11 Senhor, a tua mão está levantada, mas nem por isso a veem; porém verão o teu zelo pelo povo e se envergonharão; e o teu furor, por causa dos teus adversários, que os consuma.
12 Senhor, concede-nos a paz, porque todas as nossas obras tu as fazes por nós.
13 Ó Senhor, Deus nosso, outros senhores têm tido domínio sobre nós; mas graças a ti somente é que louvamos o teu nome.
14 Mortos não tornarão a viver, sombras não ressuscitam; por isso, os castigaste, e destruíste, e lhes fizeste perecer toda a memória.
15 Tu, Senhor, aumentaste o povo, aumentaste o povo e tens sido glorificado; a todos os confins da terra dilataste.
16 Senhor, na angústia te buscaram; vindo sobre eles a tua correção, derramaram as suas orações.
17 Como a mulher grávida, quando se lhe aproxima a hora de dar à luz, se contorce e dá gritos nas suas dores, assim fomos nós na tua presença, ó Senhor!
18 Concebemos nós e nos contorcemos em dores de parto, mas o que demos à luz foi vento; não trouxemos à terra livramento algum, e não nasceram moradores do mundo.
19 Os vossos mortos e também o meu cadáver viverão e ressuscitarão; despertai e exultai, os que habitais no pó, porque o teu orvalho, ó Deus, será como o orvalho de vida, e a terra dará à luz os seus mortos.
20 Vai, pois, povo meu, entra nos teus quartos e fecha as tuas portas sobre ti; esconde-te só por um momento, até que passe a ira.
21 Pois eis que o Senhor sai do seu lugar, para castigar a iniquidade dos moradores da terra; a terra descobrirá o sangue que embebeu e já não encobrirá aqueles que foram mortos.*
1 Naquele dia, o Senhor castigará com a sua dura espada, grande e forte, o dragão, serpente veloz, e o dragão, serpente sinuosa, e matará o monstro que está no mar.
2 Naquele dia, dirá o Senhor: Cantai a vinha deliciosa!
3 Eu, o Senhor, a vigio e a cada momento a regarei; para que ninguém lhe faça dano, de noite e de dia eu cuidarei dela.
4 Não há indignação em mim. Quem me dera espinheiros e abrolhos diante de mim! Em guerra, eu iria contra eles e juntamente os queimaria.
5 Ou que homens se apoderem da minha força e façam paz comigo; sim, que façam paz comigo.
6 Dias virão em que Jacó lançará raízes, florescerá e brotará Israel, e encherão de fruto o mundo.
7 Porventura, feriu o Senhor a Israel como àqueles que o feriram? Ou o matou, assim como àqueles que o mataram?
8 Com xô!, xô! e exílio o trataste; com forte sopro o expulsaste no dia do vento oriental.
9 Portanto, com isto será expiada a culpa de Jacó, e este é todo o fruto do perdão do seu pecado: quando o Senhor fizer a todas as pedras do altar como pedras de cal feitas em pedaços, não ficarão em pé os postes-ídolos e os altares do incenso.
10 Porque a cidade fortificada está solitária, habitação desamparada e abandonada como um deserto; ali pastam os bezerros, deitam-se e devoram os seus ramos.
11 Quando os seus ramos se secam, são quebrados. Então, vêm as mulheres e lhes deitam fogo, porque este povo não é povo de entendimento; por isso, aquele que o fez não se compadecerá dele, e aquele que o formou não lhe perdoará.
12 Naquele dia, em que o Senhor debulhará o seu cereal desde o Eufrates até ao ribeiro do Egito; e vós, ó filhos de Israel, sereis colhidos um a um.
13 Naquele dia, se tocará uma grande trombeta, e os que andavam perdidos pela terra da Assíria e os que forem desterrados para a terra do Egito tornarão a vir e adorarão ao Senhor no monte santo em Jerusalém.*
1 Ai da soberba coroa dos bêbados de Efraim e da flor caduca da sua gloriosa formosura que está sobre a parte alta do fertilíssimo vale dos vencidos do vinho!
2 Eis que o Senhor tem certo homem valente e poderoso; este, como uma queda de saraiva, como uma tormenta de destruição e como uma tempestade de impetuosas águas que transbordam, com poder as derribará por terra.
3 A soberba coroa dos bêbados de Efraim será pisada aos pés.
4 A flor caduca da sua gloriosa formosura, que está sobre a parte alta do fertilíssimo vale, será como o figo prematuro, que amadurece antes do verão, o qual, em pondo nele alguém os olhos, mal o apanha, já o devora.
5 Naquele dia, o Senhor dos Exércitos será a coroa de glória e o formoso diadema para os restantes de seu povo;
6 será o espírito de justiça para o que se assenta a julgar e fortaleza para os que fazem recuar o assalto contra as portas.
7 Mas também estes cambaleiam por causa do vinho e não podem ter-se em pé por causa da bebida forte; o sacerdote e o profeta cambaleiam por causa da bebida forte, são vencidos pelo vinho, não podem ter-se em pé por causa da bebida forte; erram na visão, tropeçam no juízo.
8 Porque todas as mesas estão cheias de vômitos, e não há lugar sem imundícia.
9 A quem, pois, se ensinaria o conhecimento? E a quem se daria a entender o que se ouviu? Acaso, aos desmamados e aos que foram afastados dos seios maternos?
10 Porque é preceito sobre preceito, preceito e mais preceito; regra sobre regra, regra e mais regra; um pouco aqui, um pouco ali.
11 Pelo que por lábios gaguejantes e por língua estranha falará o Senhor a este povo,
12 ao qual ele disse: Este é o descanso, dai descanso ao cansado; e este é o refrigério; mas não quiseram ouvir.
13 Assim, pois, a palavra do Senhor lhes será preceito sobre preceito, preceito e mais preceito; regra sobre regra, regra e mais regra; um pouco aqui, um pouco ali; para que vão, e caiam para trás, e se quebrantem, se enlacem, e sejam presos.
14 Ouvi, pois, a palavra do Senhor, homens escarnecedores, que dominais este povo que está em Jerusalém.
15 Porquanto dizeis: Fizemos aliança com a morte e com o além fizemos acordo; quando passar o dilúvio do açoite, não chegará a nós, porque, por nosso refúgio, temos a mentira e debaixo da falsidade nos temos escondido.
16 Portanto, assim diz o Senhor Deus: Eis que eu assentei em Sião uma pedra, pedra já provada, pedra preciosa, angular, solidamente assentada; aquele que crer não foge.
17 Farei do juízo a régua e da justiça, o prumo; a saraiva varrerá o refúgio da mentira, e as águas arrastarão o esconderijo.
18 A vossa aliança com a morte será anulada, e o vosso acordo com o além não subsistirá; e, quando o dilúvio do açoite passar, sereis esmagados por ele.
19 Todas as vezes que passar, vos arrebatará, porque passará manhã após manhã, e todos os dias, e todas as noites; e será puro terror o só ouvir tal notícia.
20 Porque a cama será tão curta, que ninguém se poderá estender nela; e o cobertor, tão estreito, que ninguém se poderá cobrir com ele.
21 Porque o Senhor se levantará, como no monte Perazim, e se irará, como no vale de Gibeão, para realizar a sua obra, a sua obra estranha, e para executar o seu ato, o seu ato inaudito.
22 Agora, pois, não mais escarneçais, para que os vossos grilhões não se façam mais fortes; porque já do Senhor, o Senhor dos Exércitos, ouvi falar de uma destruição, e essa já está determinada sobre toda a terra.
23 Inclinai os ouvidos e ouvi a minha voz; atendei bem e ouvi o meu discurso.
24 Porventura, lavra todo dia o lavrador, para semear? Ou todo dia sulca a sua terra e a esterroa?
25 Porventura, quando já tem nivelado a superfície, não lhe espalha o endro, não semeia o cominho, não lança nela o trigo em leiras, ou cevada, no devido lugar, ou a espelta, na margem?
26 Pois o seu Deus assim o instrui devidamente e o ensina.
27 Porque o endro não se trilha com instrumento de trilhar, nem sobre o cominho se passa roda de carro; mas com vara se sacode o endro, e o cominho, com pau.
28 Acaso, é esmiuçado o cereal? Não; o lavrador nem sempre o está debulhando, nem sempre está fazendo passar por cima dele a roda do seu carro e os seus cavalos.
29 Também isso procede do Senhor dos Exércitos; ele é maravilhoso em conselho e grande em sabedoria.*
1 Ai da Lareira de Deus, cidade-lareira de Deus, em que Davi assentou o seu arraial! Acrescentai ano a ano, deixai as festas que completem o seu ciclo;
2 então, porei a Lareira de Deus em aperto, e haverá pranto e lamentação; e ela será para mim verdadeira Lareira de Deus.
3 Acamparei ao derredor de ti, cercar-te-ei com baluartes e levantarei tranqueiras contra ti.
4 Então, lançada por terra, do chão falarás, e do pó sairá afogada a tua fala; subirá da terra a tua voz como a de um fantasma; como um cochicho, a tua fala, desde o pó.
5 Mas a multidão dos teus inimigos será como o pó miúdo, e a multidão dos tiranos, como a palha que voa; dar-se-á isto, de repente, num instante.
6 Do Senhor dos Exércitos vem o castigo com trovões, com terremotos, grande estrondo, tufão de vento, tempestade e chamas devoradoras.
7 Como sonho e visão noturna será a multidão de todas as nações que hão de pelejar contra a Lareira de Deus, como também todos os que pelejarem contra ela e contra os seus baluartes e a puserem em aperto.
8 Será também como o faminto que sonha que está a comer, mas, acordando, sente-se vazio; ou como o sequioso que sonha que está a beber, mas, acordando, sente-se desfalecido e sedento; assim será toda a multidão das nações que pelejarem contra o monte Sião.
9 Estatelai-vos e ficai estatelados, cegai-vos e permanecei cegos; bêbados estão, mas não de vinho; andam cambaleando, mas não de bebida forte.
10 Porque o Senhor derramou sobre vós o espírito de profundo sono, e fechou os vossos olhos, que são os profetas, e vendou a vossa cabeça, que são os videntes.
11 Toda visão já se vos tornou como as palavras de um livro selado, que se dá ao que sabe ler, dizendo: Lê isto, peço-te; e ele responde: Não posso, porque está selado;
12 e dá-se o livro ao que não sabe ler, dizendo: Lê isto, peço-te; e ele responde: Não sei ler.
13 O Senhor disse: Visto que este povo se aproxima de mim e com a sua boca e com os seus lábios me honra, mas o seu coração está longe de mim, e o seu temor para comigo consiste só em mandamentos de homens, que maquinalmente aprendeu,
14 continuarei a fazer obra maravilhosa no meio deste povo; sim, obra maravilhosa e um portento; de maneira que a sabedoria dos seus sábios perecerá, e a prudência dos seus prudentes se esconderá.
15 Ai dos que escondem profundamente o seu propósito do Senhor, e as suas próprias obras fazem às escuras, e dizem: Quem nos vê? Quem nos conhece?
16 Que perversidade a vossa! Como se o oleiro fosse igual ao barro, e a obra dissesse do seu artífice: Ele não me fez; e a coisa feita dissesse do seu oleiro: Ele nada sabe.
17 Porventura, dentro em pouco não se converterá o Líbano em pomar, e o pomar não será tido por bosque?
18 Naquele dia, os surdos ouvirão as palavras do livro, e os cegos, livres já da escuridão e das trevas, as verão.
19 Os mansos terão regozijo sobre regozijo no Senhor, e os pobres entre os homens se alegrarão no Santo de Israel.
20 Pois o tirano é reduzido a nada, o escarnecedor já não existe, e já se acham eliminados todos os que cogitam da iniquidade,
21 os quais por causa de uma palavra condenam um homem, os que põem armadilhas ao que repreende na porta, e os que sem motivo negam ao justo o seu direito.
22 Portanto, acerca da casa de Jacó, assim diz o Senhor, que remiu a Abraão: Jacó já não será envergonhado, nem mais se empalidecerá o seu rosto.
23 Mas, quando ele e seus filhos virem a obra das minhas mãos no meio deles, santificarão o meu nome; sim, santificarão o Santo de Jacó e temerão o Deus de Israel.
24 E os que erram de espírito virão a ter entendimento, e os murmuradores hão de aceitar instrução.*
1 Ai dos filhos rebeldes, diz o Senhor, que executam planos que não procedem de mim e fazem aliança sem a minha aprovação, para acrescentarem pecado sobre pecado!
2 Que descem ao Egito sem me consultar, buscando refúgio em Faraó e abrigo, à sombra do Egito!
3 Mas o refúgio de Faraó se vos tornará em vergonha, e o abrigo na sombra do Egito, em confusão.
4 Porque os príncipes de Judá já estão em Zoã, e os seus embaixadores já chegaram a Hanes.
5 Todos se envergonharão de um povo que de nada lhes valerá, não servirá nem de ajuda nem de proveito, porém de vergonha e de opróbrio.
6 Sentença contra a Besta do Sul. Através da terra da aflição e angústia de onde vêm a leoa, o leão, a víbora e a serpente volante, levam a lombos de jumento as suas riquezas e sobre as corcovas de camelos, os seus tesouros, a um povo que de nada lhes aproveitará.
7 Pois, quanto ao Egito, vão e inútil é o seu auxílio; por isso, lhe chamei Gabarola que nada faz.
8 Vai, pois, escreve isso numa tabuinha perante eles, escreve-o num livro, para que fique registrado para os dias vindouros, para sempre, perpetuamente.
9 Porque povo rebelde é este, filhos mentirosos, filhos que não querem ouvir a lei do Senhor.
10 Eles dizem aos videntes: Não tenhais visões; e aos profetas: Não profetizeis para nós o que é reto; dizei-nos coisas aprazíveis, profetizai-nos ilusões;
11 desviai-vos do caminho, apartai-vos da vereda; não nos faleis mais do Santo de Israel.
12 Pelo que assim diz o Santo de Israel: Visto que rejeitais esta palavra, confiais na opressão e na perversidade e sobre isso vos estribais,
13 portanto, esta maldade vos será como a brecha de um muro alto, que, formando uma barriga, está prestes a cair, e cuja queda vem de repente, num momento.
14 O Senhor o quebrará como se quebra o vaso do oleiro, despedaçando-o sem nada lhe poupar; não se achará entre os seus cacos um que sirva para tomar fogo da lareira ou tirar água da poça.
15 Porque assim diz o Senhor Deus, o Santo de Israel: Em vos converterdes e em sossegardes, está a vossa salvação; na tranquilidade e na confiança, a vossa força, mas não o quisestes.
16 Antes, dizeis: Não, sobre cavalos fugiremos; portanto, fugireis; e: Sobre cavalos ligeiros cavalgaremos; sim, ligeiros serão os vossos perseguidores.
17 Mil homens fugirão pela ameaça de apenas um; pela ameaça de cinco, todos vós fugireis, até que sejais deixados como o mastro no cimo do monte e como o estandarte no outeiro.
18 Por isso, o Senhor espera, para ter misericórdia de vós, e se detém, para se compadecer de vós, porque o Senhor é Deus de justiça; bem-aventurados todos os que nele esperam.
19 Porque o povo habitará em Sião, em Jerusalém; tu não chorarás mais; certamente, se compadecerá de ti, à voz do teu clamor, e, ouvindo-a, te responderá.
20 Embora o Senhor vos dê pão de angústia e água de aflição, contudo, não se esconderão mais os teus mestres; os teus olhos verão os teus mestres.
21 Quando te desviares para a direita e quando te desviares para a esquerda, os teus ouvidos ouvirão atrás de ti uma palavra, dizendo: Este é o caminho, andai por ele.
22 E terás por contaminados a prata que recobre as imagens esculpidas e o ouro que reveste as tuas imagens de fundição; lançá-las-ás fora como coisa imunda e a cada uma dirás: Fora daqui!
23 Então, o Senhor te dará chuva sobre a tua semente, com que semeares a terra, como também pão como produto da terra, o qual será farto e nutritivo; naquele dia, o teu gado pastará em lugares espaçosos.
24 Os bois e os jumentos que lavram a terra comerão forragem com sal, alimpada com pá e forquilha.
25 Em todo monte alto e em todo outeiro elevado haverá ribeiros e correntes de águas, no dia da grande matança quando caírem as torres.
26 A luz da lua será como a do sol, e a do sol, sete vezes maior, como a luz de sete dias, no dia em que o Senhor atar a ferida do seu povo e curar a chaga do golpe que ele deu.
27 Eis o nome do Senhor vem de longe, ardendo na sua ira, no meio de espessas nuvens; os seus lábios estão cheios de indignação, e a sua língua é como fogo devorador.
28 A sua respiração é como a torrente que transborda e chega até ao pescoço, para peneirar as nações com peneira de destruição; um freio de fazer errar estará nos queixos dos povos.
29 Um cântico haverá entre vós, como na noite em que se celebra festa santa; e alegria de coração, como a daquele que sai ao som da flauta para ir ao monte do Senhor, à Rocha de Israel.
30 O Senhor fará ouvir a sua voz majestosa e fará ver o golpe do seu braço, que desce com indignação de ira, no meio de chamas devoradoras, de chuvas torrenciais, de tempestades e de pedra de saraiva.
31 Porque com a voz do Senhor será apavorada a Assíria, quando ele a fere com a vara.
32 Cada pancada castigadora, com a vara, que o Senhor lhe der, será ao som de tamboris e harpas; e combaterá vibrando golpes contra eles.
33 Porque há muito está preparada a fogueira, preparada para o rei; a pira é profunda e larga, com fogo e lenha em abundância; o assopro do Senhor, como torrente de enxofre, a acenderá.*
1 Ai dos que descem ao Egito em busca de socorro e se estribam em cavalos; que confiam em carros, porque são muitos, e em cavaleiros, porque são mui fortes, mas não atentam para o Santo de Israel, nem buscam ao Senhor!
2 Todavia, este é sábio, e faz vir o mal, e não retira as suas palavras; ele se levantará contra a casa dos malfeitores e contra a ajuda dos que praticam a iniquidade.
3 Pois os egípcios são homens e não deuses; os seus cavalos, carne e não espírito. Quando o Senhor estender a mão, cairão por terra tanto o auxiliador como o ajudado, e ambos juntamente serão consumidos.
4 Porque assim me disse o Senhor: Como o leão e o cachorro do leão rugem sobre a sua presa, ainda que se convoque contra eles grande número de pastores, e não se espantam das suas vozes, nem se abatem pela sua multidão, assim o Senhor dos Exércitos descerá, para pelejar sobre o monte Sião e sobre o seu outeiro.
5 Como pairam as aves, assim o Senhor dos Exércitos amparará a Jerusalém; protegê-la-á e salvá-la-á, poupá-la-á e livrá-la-á.
6 Convertei-vos, pois, ó filhos de Israel, àquele de quem tanto vos afastastes.
7 Pois, naquele dia, cada um lançará fora os seus ídolos de prata e os seus ídolos de ouro, que as vossas mãos fabricaram para pecardes.
8 Então, a Assíria cairá pela espada, não de homem; a espada, não de homem, a devorará; fugirá diante da espada, e os seus jovens serão sujeitos a trabalhos forçados.
9 De medo não atinará com a sua rocha de refúgio; os seus príncipes, espavoridos, desertarão a bandeira, diz o Senhor, cujo fogo está em Sião e cuja fornalha, em Jerusalém.*
1 Eis aí está que reinará um rei com justiça, e em retidão governarão príncipes.
2 Cada um servirá de esconderijo contra o vento, de refúgio contra a tempestade, de torrentes de águas em lugares secos e de sombra de grande rocha em terra sedenta.
3 Os olhos dos que veem não se ofuscarão, e os ouvidos dos que ouvem estarão atentos.
4 O coração dos temerários saberá compreender, e a língua dos gagos falará pronta e distintamente.
5 Ao louco nunca mais se chamará nobre, e do fraudulento jamais se dirá que é magnânimo.
6 Porque o louco fala loucamente, e o seu coração obra o que é iníquo, para usar de impiedade e para proferir mentiras contra o Senhor, para deixar o faminto na ânsia da sua fome e fazer que o sedento venha a ter falta de bebida.
7 Também as armas do fraudulento são más; ele maquina intrigas para arruinar os desvalidos, com palavras falsas, ainda quando a causa do pobre é justa.
8 Mas o nobre projeta coisas nobres e na sua nobreza perseverará.
9 Levantai-vos, mulheres que viveis despreocupadamente, e ouvi a minha voz; vós, filhas, que estais confiantes, inclinai os ouvidos às minhas palavras.
10 Porque daqui a um ano e dias vireis a tremer, ó mulheres que estais confiantes, porque a vindima se acabará, e não haverá colheita.
11 Tremei, mulheres que viveis despreocupadamente; turbai-vos, vós que estais confiantes. Despi-vos, e ponde-vos desnudas, e cingi com panos de saco os lombos.
12 Batei no peito por causa dos campos aprazíveis e por causa das vinhas frutíferas.
13 Sobre a terra do meu povo virão espinheiros e abrolhos, como também sobre todas as casas onde há alegria, na cidade que exulta.
14 O palácio será abandonado, a cidade populosa ficará deserta; Ofel e a torre da guarda servirão de cavernas para sempre, folga para os jumentos selvagens e pastos para os rebanhos;
15 até que se derrame sobre nós o Espírito lá do alto; então, o deserto se tornará em pomar, e o pomar será tido por bosque;
16 o juízo habitará no deserto, e a justiça morará no pomar.
17 O efeito da justiça será paz, e o fruto da justiça, repouso e segurança, para sempre.
18 O meu povo habitará em moradas de paz, em moradas bem seguras e em lugares quietos e tranquilos,
19 ainda que haja saraivada, caia o bosque e seja a cidade inteiramente abatida.
20 Bem-aventurados vós, os que semeais junto a todas as águas e dais liberdade ao pé do boi e do jumento.*
1 Ai de ti, destruidor que não foste destruído, que procedes perfidamente e não foste tratado com perfídia! Acabando tu de destruir, serás destruído, acabando de tratar perfidamente, serás tratado com perfídia.
2 Senhor, tem misericórdia de nós; em ti temos esperado; sê tu o nosso braço manhã após manhã e a nossa salvação no tempo da angústia.
3 Ao ruído do tumulto, fogem os povos; quando tu te ergues, as nações são dispersas.
4 Então, ajuntar-se-á o vosso despojo como se ajuntam as lagartas; como os gafanhotos saltam, assim os homens saltarão sobre ele.
5 O Senhor é sublime, pois habita nas alturas; encheu a Sião de direito e de justiça.
6 Haverá, ó Sião, estabilidade nos teus tempos, abundância de salvação, sabedoria e conhecimento; o temor do Senhor será o teu tesouro.
7 Eis que os heróis pranteiam de fora, e os mensageiros de paz estão chorando amargamente.
8 As estradas estão desoladas, cessam os que passam por elas; rompem-se as alianças, as cidades são desprezadas, já não se faz caso do homem.
9 A terra geme e desfalece; o Líbano se envergonha e se murcha; Sarom se torna como um deserto, Basã e Carmelo são despidos de suas folhas.
10 Agora, me levantarei, diz o Senhor; levantar-me-ei a mim mesmo; agora, serei exaltado.
11 Concebestes palha, dareis à luz restolho; o vosso bufo enfurecido é fogo que vos há de devorar.
12 Os povos serão queimados como se queima a cal; como espinhos cortados, arderão no fogo.
13 Ouvi vós, os que estais longe, o que tenho feito; e vós, os que estais perto, reconhecei o meu poder.
14 Os pecadores em Sião se assombram, o tremor se apodera dos ímpios; e eles perguntam: Quem dentre nós habitará com o fogo devorador? Quem dentre nós habitará com chamas eternas?
15 O que anda em justiça e fala o que é reto; o que despreza o ganho de opressão; o que, com um gesto de mãos, recusa aceitar suborno; o que tapa os ouvidos, para não ouvir falar de homicídios, e fecha os olhos, para não ver o mal,
16 este habitará nas alturas; as fortalezas das rochas serão o seu alto refúgio, o seu pão lhe será dado, as suas águas serão certas.
17 Os teus olhos verão o rei na sua formosura, verão a terra que se estende até longe.
18 O teu coração se recordará dos terrores, dizendo: Onde está aquele que registrou, onde, o que pesou o tributo, onde, o que contou as torres?
19 Já não verás aquele povo atrevido, povo de fala obscura, que não se pode entender, e de língua bárbara, ininteligível.
20 Olha para Sião, a cidade das nossas solenidades; os teus olhos verão a Jerusalém, habitação tranquila, tenda que não será removida, cujas estacas nunca serão arrancadas, nem rebentada nenhuma de suas cordas.
21 Mas o Senhor ali nos será grandioso, fará as vezes de rios e correntes largas; barco nenhum de remo passará por eles, navio grande por eles não navegará.
22 Porque o Senhor é o nosso juiz, o Senhor é o nosso legislador, o Senhor é o nosso Rei; ele nos salvará.
23 Agora, as tuas enxárcias estão frouxas; não podem ter firme o mastro, nem estender a vela. Então, se repartirá a presa de abundantes despojos; até os coxos participarão dela.
24 Nenhum morador de Jerusalém dirá: Estou doente; porque ao povo que habita nela, perdoar-se-lhe-á a sua iniquidade.*
1 Chegai-vos, nações, para ouvir, e vós, povos, escutai; ouça a terra e a sua plenitude, o mundo e tudo quanto produz.
2 Porque a indignação do Senhor está contra todas as nações, e o seu furor, contra todo o exército delas; ele as destinou para a destruição e as entregou à matança.
3 Os seus mortos serão lançados fora, dos seus cadáveres subirá o mau cheiro, e do sangue deles os montes se inundarão.
4 Todo o exército dos céus se dissolverá, e os céus se enrolarão como um pergaminho; todo o seu exército cairá, como cai a folha da vide e a folha da figueira.
5 Porque a minha espada se embriagou nos céus; eis que, para exercer juízo, desce sobre Edom e sobre o povo que destinei para a destruição.
6 A espada do Senhor está cheia de sangue, engrossada da gordura e do sangue de cordeiros e de bodes, da gordura dos rins de carneiros; porque o Senhor tem sacrifício em Bozra e grande matança na terra de Edom.
7 Os bois selvagens cairão com eles, e os novilhos, com os touros; a sua terra se embriagará de sangue, e o seu pó se tornará fértil com a gordura.
8 Porque será o dia da vingança do Senhor, ano de retribuições pela causa de Sião.
9 Os ribeiros de Edom se transformarão em piche, e o seu pó, em enxofre; a sua terra se tornará em piche ardente.
10 Nem de noite nem de dia se apagará; subirá para sempre a sua fumaça; de geração em geração será assolada, e para todo o sempre ninguém passará por ela.
11 Mas o pelicano e o ouriço a possuirão; o bufo e o corvo habitarão nela. Estender-se-á sobre ela o cordel de destruição e o prumo de ruína.
12 Já não haverá nobres para proclamarem um rei; os seus príncipes já não existem.
13 Nos seus palácios, crescerão espinhos, e urtigas e cardos, nas suas fortalezas; será uma habitação de chacais e morada de avestruzes.
14 As feras do deserto se encontrarão com as hienas, e os sátiros clamarão uns para os outros; fantasmas ali pousarão e acharão para si lugar de repouso.
15 Aninhar-se-á ali a coruja, e porá os seus ovos, e os chocará, e na sombra abrigará os seus filhotes; também ali os abutres se ajuntarão, um com o outro.
16 Buscai no livro do Senhor e lede: Nenhuma destas criaturas falhará, nem uma nem outra faltará; porque a boca do Senhor o ordenou, e o seu Espírito mesmo as ajuntará.
17 Porque ele lançou as sortes a favor delas, e a sua mão lhes repartiu a terra com o cordel; para sempre a possuirão, através de gerações habitarão nela.*
1 O deserto e a terra se alegrarão; o ermo exultará e florescerá como o narciso.
2 Florescerá abundantemente, jubilará de alegria e exultará; deu-se-lhes a glória do Líbano, o esplendor do Carmelo e de Sarom; eles verão a glória do Senhor, o esplendor do nosso Deus.
3 Fortalecei as mãos frouxas e firmai os joelhos vacilantes.
4 Dizei aos desalentados de coração: Sede fortes, não temais. Eis o vosso Deus. A vingança vem, a retribuição de Deus; ele vem e vos salvará.
5 Então, se abrirão os olhos dos cegos, e se desimpedirão os ouvidos dos surdos;
6 os coxos saltarão como cervos, e a língua dos mudos cantará; pois águas arrebentarão no deserto, e ribeiros, no ermo.
7 A areia esbraseada se transformará em lagos, e a terra sedenta, em mananciais de águas; onde outrora viviam os chacais, crescerá a erva com canas e juncos.
8 E ali haverá bom caminho, caminho que se chamará o Caminho Santo; o imundo não passará por ele, pois será somente para o seu povo; quem quer que por ele caminhe não errará, nem mesmo o louco.
9 Ali não haverá leão, animal feroz não passará por ele, nem se achará nele; mas os remidos andarão por ele.
10 Os resgatados do Senhor voltarão e virão a Sião com cânticos de júbilo; alegria eterna coroará a sua cabeça; gozo e alegria alcançarão, e deles fugirá a tristeza e o gemido.*
1 No ano décimo quarto do rei Ezequias, subiu Senaqueribe, rei da Assíria, contra todas as cidades fortificadas de Judá e as tomou.
2 O rei da Assíria enviou Rabsaqué, de Laquis a Jerusalém, ao rei Ezequias, com grande exército; parou ele na extremidade do aqueduto do açude superior, junto ao caminho do campo do lavadeiro.
3 Então, saíram a encontrar-se com ele Eliaquim, filho de Hilquias, o mordomo, Sebna, o escrivão, e Joá, filho de Asafe, o cronista.
4 Rabsaqué lhes disse: Dizei a Ezequias: Assim diz o sumo rei, o rei da Assíria: Que confiança é essa em que te estribas?
5 Bem posso dizer-te que teu conselho e poder para a guerra não passam de vãs palavras; em quem, pois, agora confias, para que te rebeles contra mim?
6 Confias no Egito, esse bordão de cana esmagada, o qual, se alguém nele apoiar-se, lhe entrará pela mão e a traspassará; assim é Faraó, rei do Egito, para com todos os que nele confiam.
7 Mas, se me dizes: Confiamos no Senhor, nosso Deus, não é esse aquele cujos altos e altares Ezequias removeu e disse a Judá e a Jerusalém: Perante este altar adorareis?
8 Ora, pois, empenha-te com meu senhor, rei da Assíria, e dar-te-ei dois mil cavalos, se de tua parte achares cavaleiros para os montar.
9 Como, pois, se não podes afugentar um só capitão dos menores dos servos do meu senhor, confias no Egito por causa dos carros e cavaleiros?
10 Acaso, subi eu agora sem o Senhor contra esta terra, para a destruir? Pois o Senhor mesmo me disse: Sobe contra a terra e destrói-a.
11 Então, disseram Eliaquim, Sebna e Joá a Rabsaqué: Pedimos-te que fales em aramaico aos teus servos, porque o entendemos, e não nos fales em judaico, aos ouvidos do povo que está sobre os muros.
12 Mas Rabsaqué lhes respondeu: Mandou-me, acaso, o meu senhor para dizer-te estas palavras a ti somente e a teu senhor? E não, antes, aos homens que estão assentados sobre os muros, para que comam convosco o seu próprio excremento e bebam a sua própria urina?
13 Então, Rabsaqué se pôs em pé, e clamou em alta voz em judaico, e disse: Ouvi as palavras do sumo rei, do rei da Assíria.
14 Assim diz o rei: Não vos engane Ezequias; porque não vos poderá livrar.
15 Nem tampouco Ezequias vos faça confiar no Senhor, dizendo: O Senhor certamente nos livrará, e esta cidade não será entregue nas mãos do rei da Assíria.
16 Não deis ouvidos a Ezequias; porque assim diz o rei da Assíria: Fazei as pazes comigo e vinde para mim; e comei, cada um da sua própria vide e da sua própria figueira, e bebei, cada um da água da sua própria cisterna;
17 até que eu venha e vos leve para uma terra como a vossa; terra de cereal e de vinho, terra de pão e de vinhas.
18 Não vos engane Ezequias, dizendo: O Senhor nos livrará. Acaso, os deuses das nações livraram cada um a sua terra das mãos do rei da Assíria?
19 Onde estão os deuses de Hamate e de Arpade? Onde estão os deuses de Sefarvaim? Acaso, livraram eles a Samaria das minhas mãos?
20 Quais são, dentre todos os deuses destes países, os que livraram a sua terra das minhas mãos, para que o Senhor livre a Jerusalém das minhas mãos?
21 Eles, porém, se calaram e não lhe responderam palavra; porque assim lhes havia ordenado o rei, dizendo: Não lhe respondereis.
22 Então, Eliaquim, filho de Hilquias, o mordomo, e Sebna, o escrivão, e Joá, filho de Asafe, o cronista, rasgaram suas vestes, vieram ter com Ezequias e lhe referiram as palavras de Rabsaqué.*
1 Tendo o rei Ezequias ouvido isto, rasgou as suas vestes, cobriu-se de pano de saco e entrou na Casa do Senhor.
2 Então, enviou a Eliaquim, o mordomo, a Sebna, o escrivão, e aos anciãos dos sacerdotes, com vestes de pano de saco, ao profeta Isaías, filho de Amoz,
3 os quais lhe dissessem: Assim diz Ezequias: Este dia é dia de angústia, de castigo e de opróbrio; porque filhos são chegados à hora de nascer, e não há força para dá-los à luz.
4 Porventura, o Senhor, teu Deus, terá ouvido as palavras de Rabsaqué, a quem o rei da Assíria, seu senhor, enviou para afrontar o Deus vivo, e repreenderá as palavras que o Senhor ouviu; faze, pois, tuas orações pelos que ainda subsistem.
5 Foram, pois, os servos do rei Ezequias ter com Isaías;
6 Isaías lhes disse: Dizei isto a vosso senhor: Assim diz o Senhor: Não temas por causa das palavras que ouviste, com as quais os servos do rei da Assíria blasfemaram contra mim.
7 Eis que meterei nele um espírito, e ele, ao ouvir certo rumor, voltará para a sua terra; e nela eu o farei cair morto à espada.
8 Voltou, pois, Rabsaqué e encontrou o rei da Assíria pelejando contra Libna; porque ouvira que o rei já se havia retirado de Laquis.
9 O rei ouviu que, a respeito de Tiraca, rei da Etiópia, se dizia: Saiu para guerrear contra ti. Assim que ouviu isto, enviou mensageiros a Ezequias, dizendo:
10 Assim falareis a Ezequias, rei de Judá: Não te engane o teu Deus, em quem confias, dizendo: Jerusalém não será entregue nas mãos do rei da Assíria.
11 Já tens ouvido o que fizeram os reis da Assíria a todas as terras, como as destruíram totalmente; e crês tu que te livrarias?
12 Porventura, os deuses das nações livraram os povos que meus pais destruíram: Gozã, Harã, Rezefe e os filhos de Éden, que estavam em Telassar?
13 Onde está o rei de Hamate, e o rei de Arpade, e o rei da cidade de Sefarvaim, de Hena e de Iva?
14 Tendo Ezequias recebido a carta das mãos dos mensageiros, leu-a; então, subiu à Casa do Senhor, estendeu-a perante o Senhor
15 e orou ao Senhor, dizendo:
16 Ó Senhor dos Exércitos, Deus de Israel, que estás entronizado acima dos querubins, tu somente és o Deus de todos os reinos da terra; tu fizeste os céus e a terra.
17 Inclina, ó Senhor, os ouvidos e ouve; abre, Senhor, os olhos e vê; ouve todas as palavras de Senaqueribe, as quais ele enviou para afrontar o Deus vivo.
18 Verdade é, Senhor, que os reis da Assíria assolaram todos os países e suas terras
19 e lançaram no fogo os deuses deles, porque deuses não eram, senão obra de mãos de homens, madeira e pedra; por isso, os destruíram.
20 Agora, pois, ó Senhor, nosso Deus, livra-nos das suas mãos, para que todos os reinos da terra saibam que só tu és o Senhor.
21 Então, Isaías, filho de Amoz, mandou dizer a Ezequias: Assim diz o Senhor, o Deus de Israel: Visto que me pediste acerca de Senaqueribe, rei da Assíria,
22 esta é a palavra que o Senhor falou a respeito dele: A virgem, filha de Sião, te despreza e zomba de ti; a filha de Jerusalém meneia a cabeça por detrás de ti.
23 A quem afrontaste e de quem blasfemaste? E contra quem alçaste a voz e arrogantemente ergueste os olhos? Contra o Santo de Israel.
24 Por meio dos teus servos, afrontaste o Senhor e disseste: Com a multidão dos meus carros, subi ao cimo dos montes, ao mais interior do Líbano; deitarei abaixo os seus altos cedros e os ciprestes escolhidos, chegarei ao seu mais alto cimo, ao seu denso e fértil pomar.
25 Cavei e bebi as águas e com a planta de meus pés sequei todos os rios do Egito.
26 Acaso, não ouviste que já há muito dispus eu estas coisas, já desde os dias remotos o tinha planejado? Agora, porém, as faço executar e eu quis que tu reduzisses a montões de ruínas as cidades fortificadas.
27 Por isso, os seus moradores, debilitados, andaram cheios de temor e envergonhados; tornaram-se como a erva do campo, e a erva verde, e o capim dos telhados, e o cereal queimado antes de amadurecer.
28 Mas eu conheço o teu assentar, e o teu sair, e o teu entrar, e o teu furor contra mim.
29 Por causa do teu furor contra mim, e porque a tua arrogância subiu até aos meus ouvidos, eis que porei o meu anzol no teu nariz, e o meu freio, na tua boca, e te farei voltar pelo caminho por onde vieste.
30 Isto te será por sinal: este ano se comerá o que espontaneamente nascer e no segundo ano o que daí proceder; no terceiro ano, porém, semeai e colhei, plantai vinhas e comei os seus frutos.
31 O que escapou da casa de Judá e ficou de resto tornará a lançar raízes para baixo e dará fruto por cima;
32 porque de Jerusalém sairá o restante, e do monte Sião, o que escapou. O zelo do Senhor dos Exércitos fará isto.
33 Pelo que assim diz o Senhor acerca do rei da Assíria: Não entrará nesta cidade, nem lançará nela flecha alguma, não virá perante ela com escudo, nem há de levantar tranqueiras contra ela.
34 Pelo caminho por onde vier, por esse voltará; mas nesta cidade não entrará, diz o Senhor.
35 Porque eu defenderei esta cidade, para a livrar, por amor de mim e por amor do meu servo Davi.
36 Então, saiu o Anjo do Senhor e feriu no arraial dos assírios a cento e oitenta e cinco mil; e, quando se levantaram os restantes pela manhã, eis que todos estes eram cadáveres.
37 Retirou-se, pois, Senaqueribe, rei da Assíria, e se foi; voltou e ficou em Nínive.
38 Sucedeu que, estando ele a adorar na casa de Nisroque, seu deus, Adrameleque e Sarezer, seus filhos, o feriram à espada e fugiram para a terra de Ararate; e Esar-Hadom, seu filho, reinou em seu lugar.*
1 Naqueles dias, Ezequias adoeceu de uma enfermidade mortal; veio ter com ele o profeta Isaías, filho de Amoz, e lhe disse: Assim diz o Senhor: Põe em ordem a tua casa, porque morrerás e não viverás.
2 Então, virou Ezequias o rosto para a parede e orou ao Senhor.
3 E disse: Lembra-te, Senhor, peço-te, de que andei diante de ti com fidelidade, com inteireza de coração e fiz o que era reto aos teus olhos; e chorou muitíssimo.
4 Então, veio a palavra do Senhor a Isaías, dizendo:
5 Vai e dize a Ezequias: Assim diz o Senhor, o Deus de Davi, teu pai: Ouvi a tua oração e vi as tuas lágrimas; acrescentarei, pois, aos teus dias quinze anos.
6 Livrar-te-ei das mãos do rei da Assíria, a ti e a esta cidade, e defenderei esta cidade.
7 Ser-te-á isto da parte do Senhor como sinal de que o Senhor cumprirá esta palavra que falou:
8 eis que farei retroceder dez graus a sombra lançada pelo sol declinante no relógio de Acaz. Assim, retrocedeu o sol os dez graus que já havia declinado.
9 Cântico de Ezequias, rei de Judá, depois de ter estado doente e se ter restabelecido:
10 Eu disse: Em pleno vigor de meus dias, hei de entrar nas portas do além; roubado estou do resto dos meus anos.
11 Eu disse: já não verei o Senhor na terra dos viventes; jamais verei homem algum entre os moradores do mundo.
12 A minha habitação foi arrancada e removida para longe de mim, como a tenda de um pastor; tu, como tecelão, me cortarás a vida da urdidura, do dia para a noite darás cabo de mim.
13 Espero com paciência até à madrugada, mas ele, como leão, me quebrou todos os ossos; do dia para a noite darás cabo de mim.
14 Como a andorinha ou o grou, assim eu chilreava e gemia como a pomba; os meus olhos se cansavam de olhar para cima. Ó Senhor, ando oprimido, responde tu por mim.
15 Que direi? Como prometeu, assim me fez; passarei tranquilamente por todos os meus anos, depois desta amargura da minha alma.
16 Senhor, por estas disposições tuas vivem os homens, e inteiramente delas depende o meu espírito; portanto, restaura-me a saúde e faze-me viver.
17 Eis que foi para minha paz que tive eu grande amargura; tu, porém, amaste a minha alma e a livraste da cova da corrupção, porque lançaste para trás de ti todos os meus pecados.
18 A sepultura não te pode louvar, nem a morte glorificar-te; não esperam em tua fidelidade os que descem à cova.
19 Os vivos, somente os vivos, esses te louvam como hoje eu o faço; o pai fará notória aos filhos a tua fidelidade.
20 O Senhor veio salvar-me; pelo que, tangendo os instrumentos de cordas, nós o louvaremos todos os dias de nossa vida, na Casa do Senhor.
21 Ora, Isaías dissera: Tome-se uma pasta de figos e ponha-se como emplasto sobre a úlcera; e ele recuperará a saúde.
22 Também dissera Ezequias: Qual será o sinal de que hei de subir à Casa do Senhor?*
1 Nesse tempo, Merodaque-Baladã, filho de Baladã, rei da Babilônia, enviou cartas e um presente a Ezequias, porque soube que estivera doente e já tinha convalescido.
2 Ezequias se agradou disso e mostrou aos mensageiros a casa do seu tesouro, a prata, o ouro, as especiarias, os óleos finos, todo o seu arsenal e tudo quanto se achava nos seus tesouros; nenhuma coisa houve, nem em sua casa, nem em todo o seu domínio, que Ezequias não lhes mostrasse.
3 Então, Isaías, o profeta, veio ao rei Ezequias e lhe disse: Que foi que aqueles homens disseram e donde vieram a ti? Respondeu Ezequias: De uma terra longínqua vieram a mim, da Babilônia.
4 Perguntou ele: Que viram em tua casa? Respondeu Ezequias: Viram tudo quanto há em minha casa; coisa nenhuma há nos meus tesouros que eu não lhes mostrasse.
5 Então, disse Isaías a Ezequias: Ouve a palavra do Senhor dos Exércitos:
6 Eis que virão dias em que tudo quanto houver em tua casa, com o que entesouraram teus pais até ao dia de hoje, será levado para a Babilônia; não ficará coisa alguma, disse o Senhor.
7 Dos teus próprios filhos, que tu gerares, tomarão, para que sejam eunucos no palácio do rei da Babilônia.
8 Então, disse Ezequias a Isaías: Boa é a palavra do Senhor que disseste. Pois pensava: Haverá paz e segurança em meus dias.*
1 Consolai, consolai o meu povo, diz o vosso Deus.
2 Falai ao coração de Jerusalém, bradai-lhe que já é findo o tempo da sua milícia, que a sua iniquidade está perdoada e que já recebeu em dobro das mãos do Senhor por todos os seus pecados.
3 Voz do que clama no deserto: Preparai o caminho do Senhor; endireitai no ermo vereda a nosso Deus.
4 Todo vale será aterrado, e nivelados, todos os montes e outeiros; o que é tortuoso será retificado, e os lugares escabrosos, aplanados.
5 A glória do Senhor se manifestará, e toda a carne a verá, pois a boca do Senhor o disse.
6 Uma voz diz: Clama; e alguém pergunta: Que hei de clamar? Toda a carne é erva, e toda a sua glória, como a flor da erva;
7 seca-se a erva, e caem as flores, soprando nelas o hálito do Senhor. Na verdade, o povo é erva;
8 seca-se a erva, e cai a sua flor, mas a palavra de nosso Deus permanece eternamente.
9 Tu, ó Sião, que anuncias boas-novas, sobe a um monte alto! Tu, que anuncias boas-novas a Jerusalém, ergue a tua voz fortemente; levanta-a, não temas e dize às cidades de Judá: Eis aí está o vosso Deus!
10 Eis que o Senhor Deus virá com poder, e o seu braço dominará; eis que o seu galardão está com ele, e diante dele, a sua recompensa.
11 Como pastor, apascentará o seu rebanho; entre os seus braços recolherá os cordeirinhos e os levará no seio; as que amamentam ele guiará mansamente.
12 Quem na concha de sua mão mediu as águas e tomou a medida dos céus a palmos? Quem recolheu na terça parte de um efa o pó da terra e pesou os montes em romana e os outeiros em balança de precisão?
13 Quem guiou o Espírito do Senhor? Ou, como seu conselheiro, o ensinou?
14 Com quem tomou ele conselho, para que lhe desse compreensão? Quem o instruiu na vereda do juízo, e lhe ensinou sabedoria, e lhe mostrou o caminho de entendimento?
15 Eis que as nações são consideradas por ele como um pingo que cai de um balde e como um grão de pó na balança; as ilhas são como pó fino que se levanta.
16 Nem todo o Líbano basta para queimar, nem os seus animais, para um holocausto.
17 Todas as nações são perante ele como coisa que não é nada; ele as considera menos do que nada, como um vácuo.
18 Com quem comparareis a Deus? Ou que coisa semelhante confrontareis com ele?
19 O artífice funde a imagem, e o ourives a cobre de ouro e cadeias de prata forja para ela.
20 O sacerdote idólatra escolhe madeira que não se corrompe e busca um artífice perito para assentar uma imagem esculpida que não oscile.
21 Acaso, não sabeis? Porventura, não ouvis? Não vos tem sido anunciado desde o princípio? Ou não atentastes para os fundamentos da terra?
22 Ele é o que está assentado sobre a redondeza da terra, cujos moradores são como gafanhotos; é ele quem estende os céus como cortina e os desenrola como tenda para neles habitar;
23 é ele quem reduz a nada os príncipes e torna em nulidade os juízes da terra.
24 Mal foram plantados e semeados, mal se arraigou na terra o seu tronco, já se secam, quando um sopro passa por eles, e uma tempestade os leva como palha.
25 A quem, pois, me comparareis para que eu lhe seja igual? — diz o Santo.
26 Levantai ao alto os olhos e vede. Quem criou estas coisas? Aquele que faz sair o seu exército de estrelas, todas bem-contadas, as quais ele chama pelo nome; por ser ele grande em força e forte em poder, nem uma só vem a faltar.
27 Por que, pois, dizes, ó Jacó, e falas, ó Israel: O meu caminho está encoberto ao Senhor, e o meu direito passa despercebido ao meu Deus?
28 Não sabes, não ouviste que o eterno Deus, o Senhor, o Criador dos fins da terra, nem se cansa, nem se fatiga? Não se pode esquadrinhar o seu entendimento.
29 Faz forte ao cansado e multiplica as forças ao que não tem nenhum vigor.
30 Os jovens se cansam e se fatigam, e os moços de exaustos caem,
31 mas os que esperam no Senhor renovam as suas forças, sobem com asas como águias, correm e não se cansam, caminham e não se fatigam.*
1 Calai-vos perante mim, ó ilhas, e os povos renovem as suas forças; cheguem-se e, então, falem; cheguemo-nos e pleiteemos juntos.
2 Quem suscitou do Oriente aquele a cujos passos segue a vitória? Quem faz que as nações se lhe submetam, e que ele calque aos pés os reis, e com a sua espada os transforme em pó, e com o seu arco, em palha que o vento arrebata?
3 Persegue-os e passa adiante em segurança, por uma vereda que seus pés jamais trilharam.
4 Quem fez e executou tudo isso? Aquele que desde o princípio tem chamado as gerações à existência, eu, o Senhor, o primeiro, e com os últimos eu mesmo.
5 Os países do mar viram isto e temeram, os fins da terra tremeram, aproximaram-se e vieram.
6 Um ao outro ajudou e ao seu próximo disse: Sê forte.
7 Assim, o artífice anima ao ourives, e o que alisa com o martelo, ao que bate na bigorna, dizendo da soldadura: Está bem-feita. Então, com pregos fixa o ídolo para que não oscile.
8 Mas tu, ó Israel, servo meu, tu, Jacó, a quem elegi, descendente de Abraão, meu amigo,
9 tu, a quem tomei das extremidades da terra, e chamei dos seus cantos mais remotos, e a quem disse: Tu és o meu servo, eu te escolhi e não te rejeitei,
10 não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus; eu te fortaleço, e te ajudo, e te sustento com a minha destra fiel.
11 Eis que envergonhados e confundidos serão todos os que estão indignados contra ti; serão reduzidos a nada, e os que contendem contigo perecerão.
12 Aos que pelejam contra ti, buscá-los-ás, porém não os acharás; serão reduzidos a nada e a coisa de nenhum valor os que fazem guerra contra ti.
13 Porque eu, o Senhor, teu Deus, te tomo pela tua mão direita e te digo: Não temas, que eu te ajudo.
14 Não temas, ó vermezinho de Jacó, povozinho de Israel; eu te ajudo, diz o Senhor, e o teu Redentor é o Santo de Israel.
15 Eis que farei de ti um trilho cortante e novo, armado de lâminas duplas; os montes trilharás, e moerás, e os outeiros reduzirás a palha.
16 Tu os padejarás, e o vento os levará, e redemoinho os espalhará; tu te alegrarás no Senhor e te gloriarás no Santo de Israel.
17 Os aflitos e necessitados buscam águas, e não as há, e a sua língua se seca de sede; mas eu, o Senhor, os ouvirei, eu, o Deus de Israel, não os desampararei.
18 Abrirei rios nos altos desnudos e fontes no meio dos vales; tornarei o deserto em açudes de águas e a terra seca, em mananciais.
19 Plantarei no deserto o cedro, a acácia, a murta e a oliveira; conjuntamente, porei no ermo o cipreste, o olmeiro e o buxo,
20 para que todos vejam e saibam, considerem e juntamente entendam que a mão do Senhor fez isso, e o Santo de Israel o criou.
21 Apresentai a vossa demanda, diz o Senhor; alegai as vossas razões, diz o Rei de Jacó.
22 Trazei e anunciai-nos as coisas que hão de acontecer; relatai-nos as profecias anteriores, para que atentemos para elas e saibamos se se cumpriram; ou fazei-nos ouvir as coisas futuras.
23 Anunciai-nos as coisas que ainda hão de vir, para que saibamos que sois deuses; fazei bem ou fazei mal, para que nos assombremos, e juntamente o veremos.
24 Eis que sois menos do que nada, e menos do que nada é o que fazeis; abominação é quem vos escolhe.
25 Do Norte suscito a um, e ele vem, a um desde o nascimento do sol, e ele invocará o meu nome; pisará magistrados como lodo e como o oleiro pisa o barro.
26 Quem anunciou isto desde o princípio, a fim que o possamos saber, antecipadamente, para que digamos: É isso mesmo? Mas não há quem anuncie, nem tampouco quem manifeste, nem ainda quem ouça as vossas palavras.
27 Eu sou o que primeiro disse a Sião: Eis! Ei-los aí! E a Jerusalém dou um mensageiro de boas-novas.
28 Quando eu olho, não há ninguém; nem mesmo entre eles há conselheiro a quem eu pergunte, e me responda.
29 Eis que todos são nada; as suas obras são coisa nenhuma; as suas imagens de fundição, vento e vácuo.*
1 Eis aqui o meu servo, a quem sustenho; o meu escolhido, em quem a minha alma se compraz; pus sobre ele o meu Espírito, e ele promulgará o direito para os gentios.
2 Não clamará, nem gritará, nem fará ouvir a sua voz na praça.
3 Não esmagará a cana quebrada, nem apagará a torcida que fumega; em verdade, promulgará o direito.
4 Não desanimará, nem se quebrará até que ponha na terra o direito; e as terras do mar aguardarão a sua doutrina.
5 Assim diz Deus, o Senhor, que criou os céus e os estendeu, formou a terra e a tudo quanto produz; que dá fôlego de vida ao povo que nela está e o espírito aos que andam nela.
6 Eu, o Senhor, te chamei em justiça, tomar-te-ei pela mão, e te guardarei, e te farei mediador da aliança com o povo e luz para os gentios;
7 para abrires os olhos aos cegos, para tirares da prisão o cativo e do cárcere, os que jazem em trevas.
8 Eu sou o Senhor, este é o meu nome; a minha glória, pois, não a darei a outrem, nem a minha honra, às imagens de escultura.
9 Eis que as primeiras predições já se cumpriram, e novas coisas eu vos anuncio; e, antes que sucedam, eu vo-las farei ouvir.
10 Cantai ao Senhor um cântico novo e o seu louvor até às extremidades da terra, vós, os que navegais pelo mar e tudo quanto há nele, vós, terras do mar e seus moradores.
11 Alcem a voz o deserto, as suas cidades e as aldeias habitadas por Quedar; exultem os que habitam nas rochas e clamem do cimo dos montes;
12 deem honra ao Senhor e anunciem a sua glória nas terras do mar.
13 O Senhor sairá como valente, despertará o seu zelo como homem de guerra; clamará, lançará forte grito de guerra e mostrará sua força contra os seus inimigos.
14 Por muito tempo me calei, estive em silêncio e me contive; mas agora darei gritos como a parturiente, e ao mesmo tempo ofegarei, e estarei esbaforido.
15 Os montes e outeiros devastarei e toda a sua erva farei secar; tornarei os rios em terra firme e secarei os lagos.
16 Guiarei os cegos por um caminho que não conhecem, fá-los-ei andar por veredas desconhecidas; tornarei as trevas em luz perante eles e os caminhos escabrosos, planos. Estas coisas lhes farei e jamais os desampararei.
17 Tornarão atrás e confundir-se-ão de vergonha os que confiam em imagens de escultura e às imagens de fundição dizem: Vós sois nossos deuses.
18 Surdos, ouvi, e vós, cegos, olhai, para que possais ver.
19 Quem é cego, como o meu servo, ou surdo, como o meu mensageiro, a quem envio? Quem é cego, como o meu amigo, e cego, como o servo do Senhor?
20 Tu vês muitas coisas, mas não as observas; ainda que tens os ouvidos abertos, nada ouves.
21 Foi do agrado do Senhor, por amor da sua própria justiça, engrandecer a lei e fazê-la gloriosa.
22 Não obstante, é um povo roubado e saqueado; todos estão enlaçados em cavernas e escondidos em cárceres; são postos como presa, e ninguém há que os livre; por despojo, e ninguém diz: Restitui.
23 Quem há entre vós que ouça isto? Que atenda e ouça o que há de ser depois?
24 Quem entregou Jacó por despojo e Israel, aos roubadores? Acaso, não foi o Senhor, aquele contra quem pecaram e nos caminhos do qual não queriam andar, não dando ouvidos à sua lei?
25 Pelo que derramou sobre eles o furor da sua ira e a violência da guerra; isto lhes ateou fogo ao redor, contudo, não o entenderam; e os queimou, mas não fizeram caso.*
1 Mas agora, assim diz o Senhor, que te criou, ó Jacó, e que te formou, ó Israel: Não temas, porque eu te remi; chamei-te pelo teu nome, tu és meu.
2 Quando passares pelas águas, eu serei contigo; quando, pelos rios, eles não te submergirão; quando passares pelo fogo, não te queimarás, nem a chama arderá em ti.
3 Porque eu sou o Senhor, teu Deus, o Santo de Israel, o teu Salvador; dei o Egito por teu resgate e a Etiópia e Sebá, por ti.
4 Visto que foste precioso aos meus olhos, digno de honra, e eu te amei, darei homens por ti e os povos, pela tua vida.
5 Não temas, pois, porque sou contigo; trarei a tua descendência desde o Oriente e a ajuntarei desde o Ocidente.
6 Direi ao Norte: entrega! E ao Sul: não retenhas! Trazei meus filhos de longe e minhas filhas, das extremidades da terra,
7 a todos os que são chamados pelo meu nome, e os que criei para minha glória, e que formei, e fiz.
8 Traze o povo que, ainda que tem olhos, é cego e surdo, ainda que tem ouvidos.
9 Todas as nações, congreguem-se; e, povos, reúnam-se; quem dentre eles pode anunciar isto e fazer-nos ouvir as predições antigas? Apresentem as suas testemunhas e por elas se justifiquem, para que se ouça e se diga: Verdade é!
10 Vós sois as minhas testemunhas, diz o Senhor, o meu servo a quem escolhi; para que o saibais, e me creiais, e entendais que sou eu mesmo, e que antes de mim deus nenhum se formou, e depois de mim nenhum haverá.
11 Eu, eu sou o Senhor, e fora de mim não há salvador.
12 Eu anunciei salvação, realizei-a e a fiz ouvir; deus estranho não houve entre vós, pois vós sois as minhas testemunhas, diz o Senhor; eu sou Deus.
13 Ainda antes que houvesse dia, eu era; e nenhum há que possa livrar alguém das minhas mãos; agindo eu, quem o impedirá?
14 Assim diz o Senhor, o que vos redime, o Santo de Israel: Por amor de vós, enviarei inimigos contra a Babilônia e a todos os de lá farei embarcar como fugitivos, isto é, os caldeus, nos navios com os quais se vangloriavam.
15 Eu sou o Senhor, o vosso Santo, o Criador de Israel, o vosso Rei.
16 Assim diz o Senhor, o que outrora preparou um caminho no mar e nas águas impetuosas, uma vereda;
17 o que fez sair o carro e o cavalo, o exército e a força — jazem juntamente lá e jamais se levantarão; estão extintos, apagados como uma torcida.
18 Não vos lembreis das coisas passadas, nem considereis as antigas.
19 Eis que faço coisa nova, que está saindo à luz; porventura, não o percebeis? Eis que porei um caminho no deserto e rios, no ermo.
20 Os animais do campo me glorificarão, os chacais e os filhotes de avestruzes; porque porei águas no deserto e rios, no ermo, para dar de beber ao meu povo, ao meu escolhido,
21 ao povo que formei para mim, para celebrar o meu louvor.
22 Contudo, não me tens invocado, ó Jacó, e de mim te cansaste, ó Israel.
23 Não me trouxeste o gado miúdo dos teus holocaustos, nem me honraste com os teus sacrifícios; não te dei trabalho com ofertas de manjares, nem te cansei com incenso.
24 Não me compraste por dinheiro cana aromática, nem com a gordura dos teus sacrifícios me satisfizeste, mas me deste trabalho com os teus pecados e me cansaste com as tuas iniquidades.
25 Eu, eu mesmo, sou o que apago as tuas transgressões por amor de mim e dos teus pecados não me lembro.
26 Desperta-me a memória; entremos juntos em juízo; apresenta as tuas razões, para que possas justificar-te.
27 Teu primeiro pai pecou, e os teus guias prevaricaram contra mim.
28 Pelo que profanarei os príncipes do santuário; e entregarei Jacó à destruição e Israel, ao opróbrio.*
1 Agora, pois, ouve, ó Jacó, servo meu, ó Israel, a quem escolhi.
2 Assim diz o Senhor, que te criou, e te formou desde o ventre, e que te ajuda: Não temas, ó Jacó, servo meu, ó amado, a quem escolhi.
3 Porque derramarei água sobre o sedento e torrentes, sobre a terra seca; derramarei o meu Espírito sobre a tua posteridade e a minha bênção, sobre os teus descendentes;
4 e brotarão como a erva, como salgueiros junto às correntes das águas.
5 Um dirá: Eu sou do Senhor; outro se chamará do nome de Jacó; o outro ainda escreverá na própria mão: Eu sou do Senhor, e por sobrenome tomará o nome de Israel.
6 Assim diz o Senhor, Rei de Israel, seu Redentor, o Senhor dos Exércitos: Eu sou o primeiro e eu sou o último, e além de mim não há Deus.
7 Quem há, como eu, feito predições desde que estabeleci o mais antigo povo? Que o declare e o exponha perante mim! Que esse anuncie as coisas futuras, as coisas que hão de vir!
8 Não vos assombreis, nem temais; acaso, desde aquele tempo não vo-lo fiz ouvir, não vo-lo anunciei? Vós sois as minhas testemunhas. Há outro Deus além de mim? Não, não há outra Rocha que eu conheça.
9 Todos os artífices de imagens de escultura são nada, e as suas coisas preferidas são de nenhum préstimo; eles mesmos são testemunhas de que elas nada veem, nem entendem, para que eles sejam confundidos.
10 Quem formaria um deus ou fundiria uma imagem de escultura, que é de nenhum préstimo?
11 Eis que todos os seus seguidores ficariam confundidos, pois os mesmos artífices não passam de homens; ajuntem-se todos e se apresentem, espantem-se e sejam, à uma, envergonhados.
12 O ferreiro faz o machado, trabalha nas brasas, forma um ídolo a martelo e forja-o com a força do seu braço; ele tem fome, e a sua força falta, não bebe água e desfalece.
13 O artífice em madeira estende o cordel e, com o lápis, esboça uma imagem; alisa-a com plaina, marca com o compasso e faz à semelhança e beleza de um homem, que possa morar em uma casa.
14 Um homem corta para si cedros, toma um cipreste ou um carvalho, fazendo escolha entre as árvores do bosque; planta um pinheiro, e a chuva o faz crescer.
15 Tais árvores servem ao homem para queimar; com parte de sua madeira se aquenta e coze o pão; e também faz um deus e se prostra diante dele, esculpe uma imagem e se ajoelha diante dela.
16 Metade queima no fogo e com ela coze a carne para comer; assa-a e farta-se; também se aquenta e diz: Ah! Já me aquento, contemplo a luz.
17 Então, do resto faz um deus, uma imagem de escultura; ajoelha-se diante dela, prostra-se e lhe dirige a sua oração, dizendo: Livra-me, porque tu és o meu deus.
18 Nada sabem, nem entendem; porque se lhes grudaram os olhos, para que não vejam, e o seu coração já não pode entender.
19 Nenhum deles cai em si, já não há conhecimento nem compreensão para dizer: Metade queimei e cozi pão sobre as suas brasas, assei sobre elas carne e a comi; e faria eu do resto uma abominação? Ajoelhar-me-ia eu diante de um pedaço de árvore?
20 Tal homem se apascenta de cinza; o seu coração enganado o iludiu, de maneira que não pode livrar a sua alma, nem dizer: Não é mentira aquilo em que confio?
21 Lembra-te destas coisas, ó Jacó, ó Israel, porquanto és meu servo! Eu te formei, tu és meu servo, ó Israel; não me esquecerei de ti.
22 Desfaço as tuas transgressões como a névoa e os teus pecados, como a nuvem; torna-te para mim, porque eu te remi.
23 Regozijai-vos, ó céus, porque o Senhor fez isto; exultai, vós, ó profundezas da terra; retumbai com júbilo, vós, montes, vós, bosques e todas as suas árvores, porque o Senhor remiu a Jacó e se glorificou em Israel.
24 Assim diz o Senhor, que te redime, o mesmo que te formou desde o ventre materno: Eu sou o Senhor, que faço todas as coisas, que sozinho estendi os céus e sozinho espraiei a terra;
25 que desfaço os sinais dos profetizadores de mentiras e enlouqueço os adivinhos; que faço tornar atrás os sábios, cujo saber converto em loucuras;
26 que confirmo a palavra do meu servo e cumpro o conselho dos meus mensageiros; que digo de Jerusalém: Ela será habitada; e das cidades de Judá: Elas serão edificadas; e quanto às suas ruínas: Eu as levantarei;
27 que digo à profundeza das águas: Seca-te, e eu secarei os teus rios;
28 que digo de Ciro: Ele é meu pastor e cumprirá tudo o que me apraz; que digo também de Jerusalém: Será edificada; e do templo: Será fundado.*
1 Assim diz o Senhor ao seu ungido, a Ciro, a quem tomo pela mão direita, para abater as nações ante a sua face, e para descingir os lombos dos reis, e para abrir diante dele as portas, que não se fecharão.
2 Eu irei adiante de ti, endireitarei os caminhos tortuosos, quebrarei as portas de bronze e despedaçarei as trancas de ferro;
3 dar-te-ei os tesouros escondidos e as riquezas encobertas, para que saibas que eu sou o Senhor, o Deus de Israel, que te chama pelo teu nome.
4 Por amor do meu servo Jacó e de Israel, meu escolhido, eu te chamei pelo teu nome e te pus o sobrenome, ainda que não me conheces.
5 Eu sou o Senhor, e não há outro; além de mim não há Deus; eu te cingirei, ainda que não me conheces.
6 Para que se saiba, até ao nascente do sol e até ao poente, que além de mim não há outro; eu sou o Senhor, e não há outro.
7 Eu formo a luz e crio as trevas; faço a paz e crio o mal; eu, o Senhor, faço todas estas coisas.
8 Destilai, ó céus, dessas alturas, e as nuvens chovam justiça; abra-se a terra e produza a salvação, e juntamente com ela brote a justiça; eu, o Senhor, as criei.
9 Ai daquele que contende com o seu Criador! E não passa de um caco de barro entre outros cacos. Acaso, dirá o barro ao que lhe dá forma: Que fazes? Ou: A tua obra não tem alça.
10 Ai daquele que diz ao pai: Por que geras? E à mulher: Por que dás à luz?
11 Assim diz o Senhor, o Santo de Israel, aquele que o formou: Quereis, acaso, saber as coisas futuras? Quereis dar ordens acerca de meus filhos e acerca das obras de minhas mãos?
12 Eu fiz a terra e criei nela o homem; as minhas mãos estenderam os céus, e a todos os seus exércitos dei as minhas ordens.
13 Eu, na minha justiça, suscitei a Ciro e todos os seus caminhos endireitarei; ele edificará a minha cidade e libertará os meus exilados, não por preço nem por presentes, diz o Senhor dos Exércitos.
14 Assim diz o Senhor: A riqueza do Egito, e as mercadorias da Etiópia, e os sabeus, homens de grande estatura, passarão ao teu poder e serão teus; seguir-te-ão, irão em grilhões, diante de ti se prostrarão e te farão as suas súplicas, dizendo: Só contigo está Deus, e não há outro que seja Deus.
15 Verdadeiramente, tu és Deus misterioso, ó Deus de Israel, ó Salvador.
16 Envergonhar-se-ão e serão confundidos todos eles; cairão, à uma, em ignomínia os que fabricam ídolos.
17 Israel, porém, será salvo pelo Senhor com salvação eterna; não sereis envergonhados, nem confundidos em toda a eternidade.
18 Porque assim diz o Senhor, que criou os céus, o Deus que formou a terra, que a fez e a estabeleceu; que não a criou para ser um caos, mas para ser habitada: Eu sou o Senhor, e não há outro.
19 Não falei em segredo, nem em lugar algum de trevas da terra; não disse à descendência de Jacó: Buscai-me em vão; eu, o Senhor, falo a verdade e proclamo o que é direito.
20 Congregai-vos e vinde; chegai-vos todos juntos, vós que escapastes das nações; nada sabem os que carregam o lenho das suas imagens de escultura e fazem súplicas a um deus que não pode salvar.
21 Declarai e apresentai as vossas razões. Que tomem conselho uns com os outros. Quem fez ouvir isto desde a antiguidade? Quem desde aquele tempo o anunciou? Porventura, não o fiz eu, o Senhor? Pois não há outro Deus, senão eu, Deus justo e Salvador não há além de mim.
22 Olhai para mim e sede salvos, vós, todos os limites da terra; porque eu sou Deus, e não há outro.
23 Por mim mesmo tenho jurado; da minha boca saiu o que é justo, e a minha palavra não tornará atrás. Diante de mim se dobrará todo joelho, e jurará toda língua.
24 De mim se dirá: Tão somente no Senhor há justiça e força; até ele virão e serão envergonhados todos os que se irritarem contra ele.
25 Mas no Senhor será justificada toda a descendência de Israel e nele se gloriará.*
1 Bel se encurva, Nebo se abaixa; os ídolos são postos sobre os animais, sobre as bestas; as cargas que costumáveis levar são canseira para as bestas já cansadas.
2 Esses deuses juntamente se abaixam e se encurvam, não podem salvar a carga; eles mesmos entram em cativeiro.
3 Ouvi-me, ó casa de Jacó e todo o restante da casa de Israel; vós, a quem desde o nascimento carrego e levo nos braços desde o ventre materno.
4 Até à vossa velhice, eu serei o mesmo e, ainda até às cãs, eu vos carregarei; já o tenho feito; levar-vos-ei, pois, carregar-vos-ei e vos salvarei.
5 A quem me comparareis para que eu lhe seja igual? E que coisa semelhante confrontareis comigo?
6 Os que gastam o ouro da bolsa e pesam a prata nas balanças assalariam o ourives para que faça um deus e diante deste se prostram e se inclinam.
7 Sobre os ombros o tomam, levam-no e o põem no seu lugar, e aí ele fica; do seu lugar não se move; recorrem a ele, mas nenhuma resposta ele dá e a ninguém livra da sua tribulação.
8 Lembrai-vos disto e tende ânimo; tomai-o a sério, ó prevaricadores.
9 Lembrai-vos das coisas passadas da antiguidade: que eu sou Deus, e não há outro, eu sou Deus, e não há outro semelhante a mim;
10 que desde o princípio anuncio o que há de acontecer e desde a antiguidade, as coisas que ainda não sucederam; que digo: o meu conselho permanecerá de pé, farei toda a minha vontade;
11 que chamo a ave de rapina desde o Oriente e de uma terra longínqua, o homem do meu conselho. Eu o disse, eu também o cumprirei; tomei este propósito, também o executarei.
12 Ouvi-me vós, os que sois de obstinado coração, que estais longe da justiça.
13 Faço chegar a minha justiça, e não está longe; a minha salvação não tardará; mas estabelecerei em Sião o livramento e em Israel, a minha glória.*
1 Desce e assenta-te no pó, ó virgem filha de Babilônia; assenta-te no chão, pois já não há trono, ó filha dos caldeus, porque nunca mais te chamarás a mimosa e delicada.
2 Toma a mó e mói a farinha; tira o teu véu, ergue a cauda da tua vestidura, desnuda as pernas e atravessa os rios.
3 As tuas vergonhas serão descobertas, e se verá o teu opróbrio; tomarei vingança e não pouparei a homem algum.
4 Quanto ao nosso Redentor, o Senhor dos Exércitos é seu nome, o Santo de Israel.
5 Assenta-te calada e entra nas trevas, ó filha dos caldeus, porque nunca mais serás chamada senhora de reinos.
6 Muito me agastei contra o meu povo, profanei a minha herança e a entreguei na tua mão, porém não usaste com ela de misericórdia e até sobre os velhos fizeste mui pesado o teu jugo.
7 E disseste: Eu serei senhora para sempre! Até agora não tomaste a sério estas coisas, nem te lembraste do seu fim.
8 Ouve isto, pois, tu que és dada a prazeres, que habitas segura, que dizes contigo mesma: Eu só, e além de mim não há outra; não ficarei viúva, nem conhecerei a perda de filhos.
9 Mas ambas estas coisas virão sobre ti num momento, no mesmo dia, perda de filhos e viuvez; virão em cheio sobre ti, apesar da multidão das tuas feitiçarias e da abundância dos teus muitos encantamentos.
10 Porque confiaste na tua maldade e disseste: Não há quem me veja. A tua sabedoria e a tua ciência, isso te fez desviar, e disseste contigo mesma: Eu só, e além de mim não há outra.
11 Pelo que sobre ti virá o mal que por encantamentos não saberás conjurar; tal calamidade cairá sobre ti, da qual por expiação não te poderás livrar; porque sobre ti, de repente, virá tamanha desolação, como não imaginavas.
12 Deixa-te estar com os teus encantamentos e com a multidão das tuas feitiçarias em que te fatigaste desde a tua mocidade; talvez possas tirar proveito, talvez, com isso, inspirar terror.
13 Já estás cansada com a multidão das tuas consultas! Levantem-se, pois, agora, os que dissecam os céus e fitam os astros, os que em cada lua nova te predizem o que há de vir sobre ti.
14 Eis que serão como restolho, o fogo os queimará; não poderão livrar-se do poder das chamas; nenhuma brasa restará para se aquentarem, nem fogo, para que diante dele se assentem.
15 Assim serão para contigo aqueles com quem te fatigaste; aqueles com quem negociaste desde a tua mocidade; dispersar-se-ão, cambaleantes, cada qual pelo seu caminho; ninguém te salvará.*
1 Ouvi isto, casa de Jacó, que vos chamais pelo nome de Israel e saístes da linhagem de Judá, que jurais pelo nome do Senhor e confessais o Deus de Israel, mas não em verdade nem em justiça.
2 (Da santa cidade tomam o nome e se firmam sobre o Deus de Israel, cujo nome é Senhor dos Exércitos.)
3 As primeiras coisas, desde a antiguidade, as anunciei; sim, pronunciou-as a minha boca, e eu as fiz ouvir; de repente agi, e elas se cumpriram.
4 Porque eu sabia que eras obstinado, e a tua cerviz é um tendão de ferro, e tens a testa de bronze.
5 Por isso, to anunciei desde aquele tempo e to dei a conhecer antes que acontecesse, para que não dissesses: O meu ídolo fez estas coisas; ou: A minha imagem de escultura e a fundição as ordenaram.
6 Já o tens ouvido; olha para tudo isto; porventura, não o admites? Desde agora te faço ouvir coisas novas e ocultas, que não conhecias.
7 Apareceram agora e não há muito, e antes deste dia delas não ouviste, para que não digas: Eis que já o sabia.
8 Tu nem as ouviste, nem as conheceste, nem tampouco antecipadamente se te abriram os ouvidos, porque eu sabia que procederias mui perfidamente e eras chamado de transgressor desde o ventre materno.
9 Por amor do meu nome, retardarei a minha ira e por causa da minha honra me conterei para contigo, para que te não venha a exterminar.
10 Eis que te acrisolei, mas disso não resultou prata; provei-te na fornalha da aflição.
11 Por amor de mim, por amor de mim, é que faço isto; porque como seria profanado o meu nome? A minha glória, não a dou a outrem.
12 Dá-me ouvidos, ó Jacó, e tu, ó Israel, a quem chamei; eu sou o mesmo, sou o primeiro e também o último.
13 Também a minha mão fundou a terra, e a minha destra estendeu os céus; quando eu os chamar, eles se apresentarão juntos.
14 Ajuntai-vos, todos vós, e ouvi! Quem, dentre eles, tem anunciado estas coisas? O Senhor amou a Ciro e executará a sua vontade contra a Babilônia, e o seu braço será contra os caldeus.
15 Eu, eu tenho falado; também já o chamei. Eu o trouxe e farei próspero o seu caminho.
16 Chegai-vos a mim e ouvi isto: não falei em segredo desde o princípio; desde o tempo em que isso vem acontecendo, tenho estado lá. Agora, o Senhor Deus me enviou a mim e o seu Espírito.
17 Assim diz o Senhor, o teu Redentor, o Santo de Israel: Eu sou o Senhor, o teu Deus, que te ensina o que é útil e te guia pelo caminho em que deves andar.
18 Ah! Se tivesses dado ouvidos aos meus mandamentos! Então, seria a tua paz como um rio, e a tua justiça, como as ondas do mar.
19 Também a tua posteridade seria como a areia, e os teus descendentes, como os grãos da areia; o seu nome nunca seria eliminado nem destruído de diante de mim.
20 Saí da Babilônia, fugi de entre os caldeus e anunciai isto com voz de júbilo; proclamai-o e levai-o até ao fim da terra; dizei: O Senhor remiu a seu servo Jacó.
21 Não padeceram sede, quando ele os levava pelos desertos; fez-lhes correr água da rocha; fendeu a pedra, e as águas correram.
22 Para os perversos, todavia, não há paz, diz o Senhor.*
1 Ouvi-me, terras do mar, e vós, povos de longe, escutai! O Senhor me chamou desde o meu nascimento, desde o ventre de minha mãe fez menção do meu nome;
2 fez a minha boca como uma espada aguda, na sombra da sua mão me escondeu; fez-me como uma flecha polida, e me guardou na sua aljava,
3 e me disse: Tu és o meu servo, és Israel, por quem hei de ser glorificado.
4 Eu mesmo disse: debalde tenho trabalhado, inútil e vãmente gastei as minhas forças; todavia, o meu direito está perante o Senhor, a minha recompensa, perante o meu Deus.
5 Mas agora diz o Senhor, que me formou desde o ventre para ser seu servo, para que torne a trazer Jacó e para reunir Israel a ele, porque eu sou glorificado perante o Senhor, e o meu Deus é a minha força.
6 Sim, diz ele: Pouco é o seres meu servo, para restaurares as tribos de Jacó e tornares a trazer os remanescentes de Israel; também te dei como luz para os gentios, para seres a minha salvação até à extremidade da terra.
7 Assim diz o Senhor, o Redentor e Santo de Israel, ao que é desprezado, ao aborrecido das nações, ao servo dos tiranos: Os reis o verão, e os príncipes se levantarão; e eles te adorarão por amor do Senhor, que é fiel, e do Santo de Israel, que te escolheu.
8 Diz ainda o Senhor: No tempo aceitável, eu te ouvi e te socorri no dia da salvação; guardar-te-ei e te farei mediador da aliança do povo, para restaurares a terra e lhe repartires as herdades assoladas;
9 para dizeres aos presos: Saí, e aos que estão em trevas: Aparecei. Eles pastarão nos caminhos e em todos os altos desnudos terão o seu pasto.
10 Não terão fome nem sede, a calma nem o sol os afligirá; porque o que deles se compadece os guiará e os conduzirá aos mananciais das águas.
11 Transformarei todos os meus montes em caminhos, e as minhas veredas serão alteadas.
12 Eis que estes virão de longe, e eis que aqueles, do Norte e do Ocidente, e aqueles outros, da terra de Sinim.
13 Cantai, ó céus, alegra-te, ó terra, e vós, montes, rompei em cânticos, porque o Senhor consolou o seu povo e dos seus aflitos se compadece.
14 Mas Sião diz: O Senhor me desamparou, o Senhor se esqueceu de mim.
15 Acaso, pode uma mulher esquecer-se do filho que ainda mama, de sorte que não se compadeça do filho do seu ventre? Mas ainda que esta viesse a se esquecer dele, eu, todavia, não me esquecerei de ti.
16 Eis que nas palmas das minhas mãos te gravei; os teus muros estão continuamente perante mim.
17 Os teus filhos virão apressadamente, ao passo que os teus destruidores e os teus assoladores se retiram do teu meio.
18 Levanta os olhos ao redor e olha: todos estes que se ajuntam vêm a ti. Tão certo como eu vivo, diz o Senhor, de todos estes te vestirás como de um ornamento e deles te cingirás como noiva.
19 Pois, quanto aos teus lugares desertos e desolados e à tua terra destruída, agora tu, ó Sião, certamente, serás estreita demais para os moradores; e os que te devoravam estarão longe de ti.
20 Até mesmo os teus filhos, que de ti foram tirados, dirão aos teus ouvidos: Mui estreito é para mim este lugar; dá-me espaço em que eu habite.
21 E dirás contigo mesma: Quem me gerou estes, pois eu estava desfilhada e estéril, em exílio e repelida? Quem, pois, me criou estes? Fui deixada sozinha; estes, onde estavam?
22 Assim diz o Senhor Deus: Eis que levantarei a mão para as nações e ante os povos arvorarei a minha bandeira; eles trarão os teus filhos nos braços, e as tuas filhas serão levadas sobre os ombros.
23 Reis serão os teus aios, e rainhas, as tuas amas; diante de ti se inclinarão com o rosto em terra e lamberão o pó dos teus pés; saberás que eu sou o Senhor e que os que esperam em mim não serão envergonhados.
24 Tirar-se-ia a presa ao valente? Acaso, os presos poderiam fugir ao tirano?
25 Mas assim diz o Senhor: Por certo que os presos se tirarão ao valente, e a presa do tirano fugirá, porque eu contenderei com os que contendem contigo e salvarei os teus filhos.
26 Sustentarei os teus opressores com a sua própria carne, e com o seu próprio sangue se embriagarão, como com vinho novo. Todo homem saberá que eu sou o Senhor, o teu Salvador e o teu Redentor, o Poderoso de Jacó.*
1 Assim diz o Senhor: Onde está a carta de divórcio de vossa mãe, pela qual eu a repudiei? Ou quem é o meu credor, a quem eu vos tenha vendido? Eis que por causa das vossas iniquidades é que fostes vendidos, e por causa das vossas transgressões vossa mãe foi repudiada.
2 Por que razão, quando eu vim, ninguém apareceu? Quando chamei, ninguém respondeu? Acaso, se encolheu tanto a minha mão, que já não pode remir ou já não há força em mim para livrar? Eis que pela minha repreensão faço secar o mar e torno os rios um deserto, até que cheirem mal os seus peixes; pois, não havendo água, morrem de sede.
3 Eu visto os céus de negridão e lhes ponho pano de saco por sua coberta.
4 O Senhor Deus me deu língua de eruditos, para que eu saiba dizer boa palavra ao cansado. Ele me desperta todas as manhãs, desperta-me o ouvido para que eu ouça como os eruditos.
5 O Senhor Deus me abriu os ouvidos, e eu não fui rebelde, não me retraí.
6 Ofereci as costas aos que me feriam e as faces, aos que me arrancavam os cabelos; não escondi o rosto aos que me afrontavam e me cuspiam.
7 Porque o Senhor Deus me ajudou, pelo que não me senti envergonhado; por isso, fiz o meu rosto como um seixo e sei que não serei envergonhado.
8 Perto está o que me justifica; quem contenderá comigo? Apresentemo-nos juntamente; quem é o meu adversário? Chegue-se para mim.
9 Eis que o Senhor Deus me ajuda; quem há que me condene? Eis que todos eles, como um vestido, serão consumidos; a traça os comerá.
10 Quem há entre vós que tema ao Senhor e que ouça a voz do seu Servo? Aquele que andou em trevas, sem nenhuma luz, confie em o nome do Senhor e se firme sobre o seu Deus.
11 Eia! Todos vós, que acendeis fogo e vos armais de setas incendiárias, andai entre as labaredas do vosso fogo e entre as setas que acendestes; de mim é que vos sobrevirá isto, e em tormentas vos deitareis.*
1 Ouvi-me vós, os que procurais a justiça, os que buscais o Senhor; olhai para a rocha de que fostes cortados e para a caverna do poço de que fostes cavados.
2 Olhai para Abraão, vosso pai, e para Sara, que vos deu à luz; porque era ele único, quando eu o chamei, o abençoei e o multipliquei.
3 Porque o Senhor tem piedade de Sião; terá piedade de todos os lugares assolados dela, e fará o seu deserto como o Éden, e a sua solidão, como o jardim do Senhor; regozijo e alegria se acharão nela, ações de graças e som de música.
4 Atendei-me, povo meu, e escutai-me, nação minha; porque de mim sairá a lei, e estabelecerei o meu direito como luz dos povos.
5 Perto está a minha justiça, aparece a minha salvação, e os meus braços dominarão os povos; as terras do mar me aguardam e no meu braço esperam.
6 Levantai os olhos para os céus e olhai para a terra embaixo, porque os céus desaparecerão como a fumaça, e a terra envelhecerá como um vestido, e os seus moradores morrerão como mosquitos, mas a minha salvação durará para sempre, e a minha justiça não será anulada.
7 Ouvi-me, vós que conheceis a justiça, vós, povo em cujo coração está a minha lei; não temais o opróbrio dos homens, nem vos turbeis por causa das suas injúrias.
8 Porque a traça os roerá como a um vestido, e o bicho os comerá como à lã; mas a minha justiça durará para sempre, e a minha salvação, para todas as gerações.
9 Desperta, desperta, arma-te de força, braço do Senhor; desperta como nos dias passados, como nas gerações antigas; não és tu aquele que abateu o Egito e feriu o monstro marinho?
10 Não és tu aquele que secou o mar, as águas do grande abismo? Aquele que fez o caminho no fundo do mar, para que passassem os remidos?
11 Assim voltarão os resgatados do Senhor e virão a Sião com júbilo, e perpétua alegria lhes coroará a cabeça; o regozijo e a alegria os alcançarão, e deles fugirão a dor e o gemido.
12 Eu, eu sou aquele que vos consola; quem, pois, és tu, para que temas o homem, que é mortal, ou o filho do homem, que não passa de erva?
13 Quem és tu que te esqueces do Senhor, que te criou, que estendeu os céus e fundou a terra, e temes continuamente todo o dia o furor do tirano, que se prepara para destruir? Onde está o furor do tirano?
14 O exilado cativo depressa será libertado, lá não morrerá, lá não descerá à sepultura; o seu pão não lhe faltará.
15 Pois eu sou o Senhor, teu Deus, que agito o mar, de modo que bramem as suas ondas — o Senhor dos Exércitos é o meu nome.
16 Ponho as minhas palavras na tua boca e te protejo com a sombra da minha mão, para que eu estenda novos céus, funde nova terra e diga a Sião: Tu és o meu povo.
17 Desperta, desperta, levanta-te, ó Jerusalém, que da mão do Senhor bebeste o cálice da sua ira, o cálice de atordoamento, e o esgotaste.
18 De todos os filhos que ela teve nenhum a guiou; de todos os filhos que criou nenhum a tomou pela mão.
19 Estas duas coisas te aconteceram; quem teve compaixão de ti? A assolação e a ruína, a fome e a espada! Quem foi o teu consolador?
20 Os teus filhos já desmaiaram, jazem nas estradas de todos os caminhos, como o antílope, na rede; estão cheios da ira do Senhor e da repreensão do teu Deus.
21 Pelo que agora ouve isto, ó tu que estás aflita e embriagada, mas não de vinho.
22 Assim diz o teu Senhor, o Senhor, teu Deus, que pleiteará a causa do seu povo: Eis que eu tomo da tua mão o cálice de atordoamento, o cálice da minha ira; jamais dele beberás;
23 pô-lo-ei nas mãos dos que te atormentaram, que disseram à tua alma: Abaixa-te, para que passemos sobre ti; e tu puseste as costas como chão e como rua para os transeuntes.*
1 Desperta, desperta, reveste-te da tua fortaleza, ó Sião; veste-te das tuas roupagens formosas, ó Jerusalém, cidade santa; porque não mais entrará em ti nem incircunciso nem imundo.
2 Sacode-te do pó, levanta-te e toma assento, ó Jerusalém; solta-te das cadeias de teu pescoço, ó cativa filha de Sião.
3 Porque assim diz o Senhor: Por nada fostes vendidos; e sem dinheiro sereis resgatados.
4 Porque assim diz o Senhor Deus: O meu povo no princípio desceu ao Egito, para nele habitar, e a Assíria sem razão o oprimiu.
5 Agora, que farei eu aqui, diz o Senhor, visto ter sido o meu povo levado sem preço? Os seus tiranos sobre ele dão uivos, diz o Senhor; e o meu nome é blasfemado incessantemente todo o dia.
6 Por isso, o meu povo saberá o meu nome; portanto, naquele dia, saberá que sou eu quem fala: Eis-me aqui.
7 Que formosos são sobre os montes os pés do que anuncia as boas-novas, que faz ouvir a paz, que anuncia coisas boas, que faz ouvir a salvação, que diz a Sião: O teu Deus reina!
8 Eis o grito dos teus atalaias! Eles erguem a voz, juntamente exultam; porque com seus próprios olhos distintamente veem o retorno do Senhor a Sião.
9 Rompei em júbilo, exultai à uma, ó ruínas de Jerusalém; porque o Senhor consolou o seu povo, remiu a Jerusalém.
10 O Senhor desnudou o seu santo braço à vista de todas as nações; e todos os confins da terra verão a salvação do nosso Deus.
11 Retirai-vos, retirai-vos, saí de lá, não toqueis coisa imunda; saí do meio dela, purificai-vos, vós que levais os utensílios do Senhor.
12 Porquanto não saireis apressadamente, nem vos ireis fugindo; porque o Senhor irá adiante de vós, e o Deus de Israel será a vossa retaguarda.
13 Eis que o meu Servo procederá com prudência; será exaltado e elevado e será mui sublime.
14 Como pasmaram muitos à vista dele (pois o seu aspecto estava mui desfigurado, mais do que o de outro qualquer, e a sua aparência, mais do que a dos outros filhos dos homens),
15 assim causará admiração às nações, e os reis fecharão a sua boca por causa dele; porque aquilo que não lhes foi anunciado verão, e aquilo que não ouviram entenderão.*
1 Quem creu em nossa pregação? E a quem foi revelado o braço do Senhor?
2 Porque foi subindo como renovo perante ele e como raiz de uma terra seca; não tinha aparência nem formosura; olhamo-lo, mas nenhuma beleza havia que nos agradasse.
3 Era desprezado e o mais rejeitado entre os homens; homem de dores e que sabe o que é padecer; e, como um de quem os homens escondem o rosto, era desprezado, e dele não fizemos caso.
4 Certamente, ele tomou sobre si as nossas enfermidades e as nossas dores levou sobre si; e nós o reputávamos por aflito, ferido de Deus e oprimido.
5 Mas ele foi traspassado pelas nossas transgressões e moído pelas nossas iniquidades; o castigo que nos traz a paz estava sobre ele, e pelas suas pisaduras fomos sarados.
6 Todos nós andávamos desgarrados como ovelhas; cada um se desviava pelo caminho, mas o Senhor fez cair sobre ele a iniquidade de nós todos.
7 Ele foi oprimido e humilhado, mas não abriu a boca; como cordeiro foi levado ao matadouro; e, como ovelha muda perante os seus tosquiadores, ele não abriu a boca.
8 Por juízo opressor foi arrebatado, e de sua linhagem, quem dela cogitou? Porquanto foi cortado da terra dos viventes; por causa da transgressão do meu povo, foi ele ferido.
9 Designaram-lhe a sepultura com os perversos, mas com o rico esteve na sua morte, posto que nunca fez injustiça, nem dolo algum se achou em sua boca.
10 Todavia, ao Senhor agradou moê-lo, fazendo-o enfermar; quando der ele a sua alma como oferta pelo pecado, verá a sua posteridade e prolongará os seus dias; e a vontade do Senhor prosperará nas suas mãos.
11 Ele verá o fruto do penoso trabalho de sua alma e ficará satisfeito; o meu Servo, o Justo, com o seu conhecimento, justificará a muitos, porque as iniquidades deles levará sobre si.
12 Por isso, eu lhe darei muitos como a sua parte, e com os poderosos repartirá ele o despojo, porquanto derramou a sua alma na morte; foi contado com os transgressores; contudo, levou sobre si o pecado de muitos e pelos transgressores intercedeu.*
1 Canta alegremente, ó estéril, que não deste à luz; exulta com alegre canto e exclama, tu que não tiveste dores de parto; porque mais são os filhos da mulher solitária do que os filhos da casada, diz o Senhor.
2 Alarga o espaço da tua tenda; estenda-se o toldo da tua habitação, e não o impeças; alonga as tuas cordas e firma bem as tuas estacas.
3 Porque transbordarás para a direita e para a esquerda; a tua posteridade possuirá as nações e fará que se povoem as cidades assoladas.
4 Não temas, porque não serás envergonhada; não te envergonhes, porque não sofrerás humilhação; pois te esquecerás da vergonha da tua mocidade e não mais te lembrarás do opróbrio da tua viuvez.
5 Porque o teu Criador é o teu marido; o Senhor dos Exércitos é o seu nome; e o Santo de Israel é o teu Redentor; ele é chamado o Deus de toda a terra.
6 Porque o Senhor te chamou como a mulher desamparada e de espírito abatido; como a mulher da mocidade, que fora repudiada, diz o teu Deus.
7 Por breve momento te deixei, mas com grandes misericórdias torno a acolher-te;
8 num ímpeto de indignação, escondi de ti a minha face por um momento; mas com misericórdia eterna me compadeço de ti, diz o Senhor, o teu Redentor.
9 Porque isto é para mim como as águas de Noé; pois jurei que as águas de Noé não mais inundariam a terra, e assim jurei que não mais me iraria contra ti, nem te repreenderia.
10 Porque os montes se retirarão, e os outeiros serão removidos; mas a minha misericórdia não se apartará de ti, e a aliança da minha paz não será removida, diz o Senhor, que se compadece de ti.
11 Ó tu, aflita, arrojada com a tormenta e desconsolada! Eis que eu assentarei as tuas pedras com argamassa colorida e te fundarei sobre safiras.
12 Farei os teus baluartes de rubis, as tuas portas, de carbúnculos e toda a tua muralha, de pedras preciosas.
13 Todos os teus filhos serão ensinados do Senhor; e será grande a paz de teus filhos.
14 Serás estabelecida em justiça, longe da opressão, porque já não temerás, e também do espanto, porque não chegará a ti.
15 Eis que poderão suscitar contendas, mas não procederá de mim; quem conspira contra ti cairá diante de ti.
16 Eis que eu criei o ferreiro, que assopra as brasas no fogo e que produz a arma para o seu devido fim; também criei o assolador, para destruir.
17 Toda arma forjada contra ti não prosperará; toda língua que ousar contra ti em juízo, tu a condenarás; esta é a herança dos servos do Senhor e o seu direito que de mim procede, diz o Senhor.*
1 Ah! Todos vós, os que tendes sede, vinde às águas; e vós, os que não tendes dinheiro, vinde, comprai e comei; sim, vinde e comprai, sem dinheiro e sem preço, vinho e leite.
2 Por que gastais o dinheiro naquilo que não é pão, e o vosso suor, naquilo que não satisfaz? Ouvi-me atentamente, comei o que é bom e vos deleitareis com finos manjares.
3 Inclinai os ouvidos e vinde a mim; ouvi, e a vossa alma viverá; porque convosco farei uma aliança perpétua, que consiste nas fiéis misericórdias prometidas a Davi.
4 Eis que eu o dei por testemunho aos povos, como príncipe e governador dos povos.
5 Eis que chamarás a uma nação que não conheces, e uma nação que nunca te conheceu correrá para junto de ti, por amor do Senhor, teu Deus, e do Santo de Israel, porque este te glorificou.
6 Buscai o Senhor enquanto se pode achar, invocai-o enquanto está perto.
7 Deixe o perverso o seu caminho, o iníquo, os seus pensamentos; converta-se ao Senhor, que se compadecerá dele, e volte-se para o nosso Deus, porque é rico em perdoar.
8 Porque os meus pensamentos não são os vossos pensamentos, nem os vossos caminhos, os meus caminhos, diz o Senhor,
9 porque, assim como os céus são mais altos do que a terra, assim são os meus caminhos mais altos do que os vossos caminhos, e os meus pensamentos, mais altos do que os vossos pensamentos.
10 Porque, assim como descem a chuva e a neve dos céus e para lá não tornam, sem que primeiro reguem a terra, e a fecundem, e a façam brotar, para dar semente ao semeador e pão ao que come,
11 assim será a palavra que sair da minha boca: não voltará para mim vazia, mas fará o que me apraz e prosperará naquilo para que a designei.
12 Saireis com alegria e em paz sereis guiados; os montes e os outeiros romperão em cânticos diante de vós, e todas as árvores do campo baterão palmas.
13 Em lugar do espinheiro, crescerá o cipreste, e em lugar da sarça crescerá a murta; e será isto glória para o Senhor e memorial eterno, que jamais será extinto.*
1 Assim diz o Senhor: Mantende o juízo e fazei justiça, porque a minha salvação está prestes a vir, e a minha justiça, prestes a manifestar-se.
2 Bem-aventurado o homem que faz isto, e o filho do homem que nisto se firma, que se guarda de profanar o sábado e guarda a sua mão de cometer algum mal.
3 Não fale o estrangeiro que se houver chegado ao Senhor, dizendo: O Senhor, com efeito, me separará do seu povo; nem tampouco diga o eunuco: Eis que eu sou uma árvore seca.
4 Porque assim diz o Senhor: Aos eunucos que guardam os meus sábados, escolhem aquilo que me agrada e abraçam a minha aliança,
5 darei na minha casa e dentro dos meus muros, um memorial e um nome melhor do que filhos e filhas; um nome eterno darei a cada um deles, que nunca se apagará.
6 Aos estrangeiros que se chegam ao Senhor, para o servirem e para amarem o nome do Senhor, sendo deste modo servos seus, sim, todos os que guardam o sábado, não o profanando, e abraçam a minha aliança,
7 também os levarei ao meu santo monte e os alegrarei na minha Casa de Oração; os seus holocaustos e os seus sacrifícios serão aceitos no meu altar, porque a minha casa será chamada Casa de Oração para todos os povos.
8 Assim diz o Senhor Deus, que congrega os dispersos de Israel: Ainda congregarei outros aos que já se acham reunidos.
9 Vós, todos os animais do campo, todas as feras dos bosques, vinde comer.
10 Os seus atalaias são cegos, nada sabem; todos são cães mudos, não podem ladrar; sonhadores preguiçosos, gostam de dormir.
11 Tais cães são gulosos, nunca se fartam; são pastores que nada compreendem, e todos se tornam para o seu caminho, cada um para a sua ganância, todos sem exceção.
12 Vinde, dizem eles, trarei vinho, e nos encharcaremos de bebida forte; o dia de amanhã será como este e ainda maior e mais famoso.*
1 Perece o justo, e não há quem se impressione com isso; e os homens piedosos são arrebatados sem que alguém considere nesse fato; pois o justo é levado antes que venha o mal
2 e entra na paz; descansam no seu leito os que andam em retidão.
3 Mas chegai-vos para aqui, vós, os filhos da agoureira, descendência da adúltera e da prostituta.
4 De quem chasqueais? Contra quem escancarais a boca e deitais para fora a língua? Porventura, não sois filhos da transgressão, descendência da falsidade,
5 que vos abrasais na concupiscência junto aos terebintos, debaixo de toda árvore frondosa, e sacrificais os filhos nos vales e nas fendas dos penhascos?
6 Por entre as pedras lisas dos ribeiros está a tua parte; estas, estas te cairão em sorte; sobre elas também derramas a tua libação e lhes apresentas ofertas de manjares. Contentar-me-ia eu com estas coisas?
7 Sobre monte alto e elevado pões o teu leito; para lá sobes para oferecer sacrifícios.
8 Detrás das portas e das ombreiras pões os teus símbolos eróticos, puxas as cobertas, sobes ao leito e o alargas para os adúlteros; dizes-lhes as tuas exigências, amas-lhes a coabitação e lhes miras a nudez.
9 Vais ao rei com óleo e multiplicas os teus perfumes; envias os teus embaixadores para longe, até à profundidade do sepulcro.
10 Na tua longa viagem te cansas, mas não dizes: É em vão; achas o que buscas; por isso, não desfaleces.
11 Mas de quem tiveste receio ou temor, para que mentisses e não te lembrasses de mim, nem de mim te importasses? Não é, acaso, porque me calo, e isso desde muito tempo, e não me temes?
12 Eu publicarei essa justiça tua; e, quanto às tuas obras, elas não te aproveitarão.
13 Quando clamares, a tua coleção de ídolos que te livre! Levá-los-á o vento; um assopro os arrebatará a todos, mas o que confia em mim herdará a terra e possuirá o meu santo monte.
14 Dir-se-á: Aterrai, aterrai, preparai o caminho, tirai os tropeços do caminho do meu povo.
15 Porque assim diz o Alto, o Sublime, que habita a eternidade, o qual tem o nome de Santo: Habito no alto e santo lugar, mas habito também com o contrito e abatido de espírito, para vivificar o espírito dos abatidos e vivificar o coração dos contritos.
16 Pois não contenderei para sempre, nem me indignarei continuamente; porque, do contrário, o espírito definharia diante de mim, e o fôlego da vida, que eu criei.
17 Por causa da indignidade da sua cobiça, eu me indignei e feri o povo; escondi a face e indignei-me, mas, rebelde, seguiu ele o caminho da sua escolha.
18 Tenho visto os seus caminhos e o sararei; também o guiarei e lhe tornarei a dar consolação, a saber, aos que dele choram.
19 Como fruto dos seus lábios criei a paz, paz para os que estão longe e para os que estão perto, diz o Senhor, e eu o sararei.
20 Mas os perversos são como o mar agitado, que não se pode aquietar, cujas águas lançam de si lama e lodo.
21 Para os perversos, diz o meu Deus, não há paz.*
1 Clama a plenos pulmões, não te detenhas, ergue a voz como a trombeta e anuncia ao meu povo a sua transgressão e à casa de Jacó, os seus pecados.
2 Mesmo neste estado, ainda me procuram dia a dia, têm prazer em saber os meus caminhos; como povo que pratica a justiça e não deixa o direito do seu Deus, perguntam-me pelos direitos da justiça, têm prazer em se chegar a Deus,
3 dizendo: Por que jejuamos nós, e tu não atentas para isso? Por que afligimos a nossa alma, e tu não o levas em conta? Eis que, no dia em que jejuais, cuidais dos vossos próprios interesses e exigis que se faça todo o vosso trabalho.
4 Eis que jejuais para contendas e rixas e para ferirdes com punho iníquo; jejuando assim como hoje, não se fará ouvir a vossa voz no alto.
5 Seria este o jejum que escolhi, que o homem um dia aflija a sua alma, incline a sua cabeça como o junco e estenda debaixo de si pano de saco e cinza? Chamarias tu a isto jejum e dia aceitável ao Senhor?
6 Porventura, não é este o jejum que escolhi: que soltes as ligaduras da impiedade, desfaças as ataduras da servidão, deixes livres os oprimidos e despedaces todo jugo?
7 Porventura, não é também que repartas o teu pão com o faminto, e recolhas em casa os pobres desabrigados, e, se vires o nu, o cubras, e não te escondas do teu semelhante?
8 Então, romperá a tua luz como a alva, a tua cura brotará sem detença, a tua justiça irá adiante de ti, e a glória do Senhor será a tua retaguarda;
9 então, clamarás, e o Senhor te responderá; gritarás por socorro, e ele dirá: Eis-me aqui. Se tirares do meio de ti o jugo, o dedo que ameaça, o falar injurioso;
10 se abrires a tua alma ao faminto e fartares a alma aflita, então, a tua luz nascerá nas trevas, e a tua escuridão será como o meio-dia.
11 O Senhor te guiará continuamente, fartará a tua alma até em lugares áridos e fortificará os teus ossos; serás como um jardim regado e como um manancial cujas águas jamais faltam.
12 Os teus filhos edificarão as antigas ruínas; levantarás os fundamentos de muitas gerações e serás chamado reparador de brechas e restaurador de veredas para que o país se torne habitável.
13 Se desviares o pé de profanar o sábado e de cuidar dos teus próprios interesses no meu santo dia; se chamares ao sábado deleitoso e santo dia do Senhor, digno de honra, e o honrares não seguindo os teus caminhos, não pretendendo fazer a tua própria vontade, nem falando palavras vãs,
14 então, te deleitarás no Senhor. Eu te farei cavalgar sobre os altos da terra e te sustentarei com a herança de Jacó, teu pai, porque a boca do Senhor o disse.*
1 Eis que a mão do Senhor não está encolhida, para que não possa salvar; nem surdo o seu ouvido, para não poder ouvir.
2 Mas as vossas iniquidades fazem separação entre vós e o vosso Deus; e os vossos pecados encobrem o seu rosto de vós, para que vos não ouça.
3 Porque as vossas mãos estão contaminadas de sangue, e os vossos dedos, de iniquidade; os vossos lábios falam mentiras, e a vossa língua profere maldade.
4 Ninguém há que clame pela justiça, ninguém que compareça em juízo pela verdade; confiam no que é nulo e andam falando mentiras; concebem o mal e dão à luz a iniquidade.
5 Chocam ovos de áspide e tecem teias de aranha; o que comer os ovos dela morrerá; se um dos ovos é pisado, sai-lhe uma víbora.
6 As suas teias não se prestam para vestes, os homens não poderão cobrir-se com o que eles fazem, as obras deles são obras de iniquidade, obra de violência há nas suas mãos.
7 Os seus pés correm para o mal, são velozes para derramar o sangue inocente; os seus pensamentos são pensamentos de iniquidade; nos seus caminhos há desolação e abatimento.
8 Desconhecem o caminho da paz, nem há justiça nos seus passos; fizeram para si veredas tortuosas; quem anda por elas não conhece a paz.
9 Por isso, está longe de nós o juízo, e a justiça não nos alcança; esperamos pela luz, e eis que há só trevas; pelo resplendor, mas andamos na escuridão.
10 Apalpamos as paredes como cegos, sim, como os que não têm olhos, andamos apalpando; tropeçamos ao meio-dia como nas trevas e entre os robustos somos como mortos.
11 Todos nós bramamos como ursos e gememos como pombas; esperamos o juízo, e não o há; a salvação, e ela está longe de nós.
12 Porque as nossas transgressões se multiplicam perante ti, e os nossos pecados testificam contra nós; porque as nossas transgressões estão conosco, e conhecemos as nossas iniquidades,
13 como o prevaricar, o mentir contra o Senhor, o retirarmo-nos do nosso Deus, o pregar opressão e rebeldia, o conceber e proferir do coração palavras de falsidade.
14 Pelo que o direito se retirou, e a justiça se pôs de longe; porque a verdade anda tropeçando pelas praças, e a retidão não pode entrar.
15 Sim, a verdade sumiu, e quem se desvia do mal é tratado como presa. O Senhor viu isso e desaprovou o não haver justiça.
16 Viu que não havia ajudador algum e maravilhou-se de que não houvesse um intercessor; pelo que o seu próprio braço lhe trouxe a salvação, e a sua própria justiça o susteve.
17 Vestiu-se de justiça, como de uma couraça, e pôs o capacete da salvação na cabeça; pôs sobre si a vestidura da vingança e se cobriu de zelo, como de um manto.
18 Segundo as obras deles, assim retribuirá; furor aos seus adversários e o devido aos seus inimigos; às terras do mar, dar-lhes-á a paga.
19 Temerão, pois, o nome do Senhor desde o poente e a sua glória, desde o nascente do sol; pois virá como torrente impetuosa, impelida pelo Espírito do Senhor.
20 Virá o Redentor a Sião e aos de Jacó que se converterem, diz o Senhor.
21 Quanto a mim, esta é a minha aliança com eles, diz o Senhor: o meu Espírito, que está sobre ti, e as minhas palavras, que pus na tua boca, não se apartarão dela, nem da de teus filhos, nem da dos filhos de teus filhos, não se apartarão desde agora e para todo o sempre, diz o Senhor.*
1 Dispõe-te, resplandece, porque vem a tua luz, e a glória do Senhor nasce sobre ti.
2 Porque eis que as trevas cobrem a terra, e a escuridão, os povos; mas sobre ti aparece resplendente o Senhor, e a sua glória se vê sobre ti.
3 As nações se encaminham para a tua luz, e os reis, para o resplendor que te nasceu.
4 Levanta em redor os olhos e vê; todos estes se ajuntam e vêm ter contigo; teus filhos chegam de longe, e tuas filhas são trazidas nos braços.
5 Então, o verás e serás radiante de alegria; o teu coração estremecerá e se dilatará de júbilo, porque a abundância do mar se tornará a ti, e as riquezas das nações virão a ter contigo.
6 A multidão de camelos te cobrirá, os dromedários de Midiã e de Efa; todos virão de Sabá; trarão ouro e incenso e publicarão os louvores do Senhor.
7 Todas as ovelhas de Quedar se reunirão junto de ti; servir-te-ão os carneiros de Nebaiote; para o meu agrado subirão ao meu altar, e eu tornarei mais gloriosa a casa da minha glória.
8 Quem são estes que vêm voando como nuvens e como pombas, ao seu pombal?
9 Certamente, as terras do mar me aguardarão; virão primeiro os navios de Társis para trazerem teus filhos de longe e, com eles, a sua prata e o seu ouro, para a santificação do nome do Senhor, teu Deus, e do Santo de Israel, porque ele te glorificou.
10 Estrangeiros edificarão os teus muros, e os seus reis te servirão; porque no meu furor te castiguei, mas na minha graça tive misericórdia de ti.
11 As tuas portas estarão abertas de contínuo; nem de dia nem de noite se fecharão, para que te sejam trazidas riquezas das nações, e, conduzidos com elas, os seus reis.
12 Porque a nação e o reino que não te servirem perecerão; sim, essas nações serão de todo assoladas.
13 A glória do Líbano virá a ti; o cipreste, o olmeiro e o buxo, conjuntamente, para adornarem o lugar do meu santuário; e farei glorioso o lugar dos meus pés.
14 Também virão a ti, inclinando-se, os filhos dos que te oprimiram; prostrar-se-ão até às plantas dos teus pés todos os que te desdenharam e chamar-te-ão Cidade do Senhor, a Sião do Santo de Israel.
15 De abandonada e odiada que eras, de modo que ninguém passava por ti, eu te constituirei glória eterna, regozijo, de geração em geração.
16 Mamarás o leite das nações e te alimentarás ao peito dos reis; saberás que eu sou o Senhor, o teu Salvador, o teu Redentor, o Poderoso de Jacó.
17 Por bronze trarei ouro, por ferro trarei prata, por madeira, bronze e por pedras, ferro; farei da paz os teus inspetores e da justiça, os teus exatores.
18 Nunca mais se ouvirá de violência na tua terra, de desolação ou ruínas, nos teus limites; mas aos teus muros chamarás Salvação, e às tuas portas, Louvor.
19 Nunca mais te servirá o sol para luz do dia, nem com o seu resplendor a lua te alumiará; mas o Senhor será a tua luz perpétua, e o teu Deus, a tua glória.
20 Nunca mais se porá o teu sol, nem a tua lua minguará, porque o Senhor será a tua luz perpétua, e os dias do teu luto findarão.
21 Todos os do teu povo serão justos, para sempre herdarão a terra; serão renovos por mim plantados, obra das minhas mãos, para que eu seja glorificado.
22 O menor virá a ser mil, e o mínimo, uma nação forte; eu, o Senhor, a seu tempo farei isso prontamente.*
1 O Espírito do Senhor Deus está sobre mim, porque o Senhor me ungiu para pregar boas-novas aos quebrantados, enviou-me a curar os quebrantados de coração, a proclamar libertação aos cativos e a pôr em liberdade os algemados;
2 a apregoar o ano aceitável do Senhor e o dia da vingança do nosso Deus; a consolar todos os que choram
3 e a pôr sobre os que em Sião estão de luto uma coroa em vez de cinzas, óleo de alegria, em vez de pranto, veste de louvor, em vez de espírito angustiado; a fim de que se chamem carvalhos de justiça, plantados pelo Senhor para a sua glória.
4 Edificarão os lugares antigamente assolados, restaurarão os de antes destruídos e renovarão as cidades arruinadas, destruídas de geração em geração.
5 Estranhos se apresentarão e apascentarão os vossos rebanhos; estrangeiros serão os vossos lavradores e os vossos vinhateiros.
6 Mas vós sereis chamados sacerdotes do Senhor, e vos chamarão ministros de nosso Deus; comereis as riquezas das nações e na sua glória vos gloriareis.
7 Em lugar da vossa vergonha, tereis dupla honra; em lugar da afronta, exultareis na vossa herança; por isso, na vossa terra possuireis o dobro e tereis perpétua alegria.
8 Porque eu, o Senhor, amo o juízo e odeio a iniquidade do roubo; dar-lhes-ei fielmente a sua recompensa e com eles farei aliança eterna.
9 A sua posteridade será conhecida entre as nações, os seus descendentes, no meio dos povos; todos quantos os virem os reconhecerão como família bendita do Senhor.
10 Regozijar-me-ei muito no Senhor, a minha alma se alegra no meu Deus; porque me cobriu de vestes de salvação e me envolveu com o manto de justiça, como noivo que se adorna de turbante, como noiva que se enfeita com as suas joias.
11 Porque, como a terra produz os seus renovos, e como o jardim faz brotar o que nele se semeia, assim o Senhor Deus fará brotar a justiça e o louvor perante todas as nações.*
1 Por amor de Sião, me não calarei e, por amor de Jerusalém, não me aquietarei, até que saia a sua justiça como um resplendor, e a sua salvação, como uma tocha acesa.
2 As nações verão a tua justiça, e todos os reis, a tua glória; e serás chamada por um nome novo, que a boca do Senhor designará.
3 Serás uma coroa de glória na mão do Senhor, um diadema real na mão do teu Deus.
4 Nunca mais te chamarão Desamparada, nem a tua terra se denominará jamais Desolada; mas chamar-te-ão Minha-Delícia; e à tua terra, Desposada; porque o Senhor se delicia em ti; e a tua terra se desposará.
5 Porque, como o jovem desposa a donzela, assim teus filhos te desposarão a ti; como o noivo se alegra da noiva, assim de ti se alegrará o teu Deus.
6 Sobre os teus muros, ó Jerusalém, pus guardas, que todo o dia e toda a noite jamais se calarão; vós, os que fareis lembrado o Senhor, não descanseis,
7 nem deis a ele descanso até que restabeleça Jerusalém e a ponha por objeto de louvor na terra.
8 Jurou o Senhor pela sua mão direita e pelo seu braço poderoso: Nunca mais darei o teu cereal por sustento aos teus inimigos, nem os estrangeiros beberão o teu vinho, fruto de tuas fadigas.
9 Mas os que o ajuntarem o comerão e louvarão ao Senhor; e os que o recolherem beberão nos átrios do meu santuário.
10 Passai, passai pelas portas; preparai o caminho ao povo; aterrai, aterrai a estrada, limpai-a das pedras; arvorai bandeira aos povos.
11 Eis que o Senhor fez ouvir até às extremidades da terra estas palavras: Dizei à filha de Sião: Eis que vem o teu Salvador; vem com ele a sua recompensa, e diante dele, o seu galardão.
12 Chamar-vos-ão Povo Santo, Remidos-Do-Senhor; e tu, Sião, serás chamada Procurada, Cidade-Não-Deserta.*
1 Quem é este que vem de Edom, de Bozra, com vestes de vivas cores, que é glorioso em sua vestidura, que marcha na plenitude da sua força? Sou eu que falo em justiça, poderoso para salvar.
2 Por que está vermelho o traje, e as tuas vestes, como as daquele que pisa uvas no lagar?
3 O lagar, eu o pisei sozinho, e dos povos nenhum homem se achava comigo; pisei as uvas na minha ira; no meu furor, as esmaguei, e o seu sangue me salpicou as vestes e me manchou o traje todo.
4 Porque o dia da vingança me estava no coração, e o ano dos meus redimidos é chegado.
5 Olhei, e não havia quem me ajudasse, e admirei-me de não haver quem me sustivesse; pelo que o meu próprio braço me trouxe a salvação, e o meu furor me susteve.
6 Na minha ira, pisei os povos, no meu furor, embriaguei-os, derramando por terra o seu sangue.
7 Celebrarei as benignidades do Senhor e os seus atos gloriosos, segundo tudo o que o Senhor nos concedeu e segundo a grande bondade para com a casa de Israel, bondade que usou para com eles, segundo as suas misericórdias e segundo a multidão das suas benignidades.
8 Porque ele dizia: Certamente, eles são meu povo, filhos que não mentirão; e se lhes tornou o seu Salvador.
9 Em toda a angústia deles, foi ele angustiado, e o Anjo da sua presença os salvou; pelo seu amor e pela sua compaixão, ele os remiu, os tomou e os conduziu todos os dias da antiguidade.
10 Mas eles foram rebeldes e contristaram o seu Espírito Santo, pelo que se lhes tornou em inimigo e ele mesmo pelejou contra eles.
11 Então, o povo se lembrou dos dias antigos, de Moisés, e disse: Onde está aquele que fez subir do mar o pastor do seu rebanho? Onde está o que pôs nele o seu Espírito Santo?
12 Aquele cujo braço glorioso ele fez andar à mão direita de Moisés? Que fendeu as águas diante deles, criando para si um nome eterno?
13 Aquele que os guiou pelos abismos, como o cavalo no deserto, de modo que nunca tropeçaram?
14 Como o animal que desce aos vales, o Espírito do Senhor lhes deu descanso. Assim, guiaste o teu povo, para te criares um nome glorioso.
15 Atenta do céu e olha da tua santa e gloriosa habitação. Onde estão o teu zelo e as tuas obras poderosas? A ternura do teu coração e as tuas misericórdias se detêm para comigo!
16 Mas tu és nosso Pai, ainda que Abraão não nos conhece, e Israel não nos reconhece; tu, ó Senhor, és nosso Pai; nosso Redentor é o teu nome desde a antiguidade.
17 Ó Senhor, por que nos fazes desviar dos teus caminhos? Por que endureces o nosso coração, para que te não temamos? Volta, por amor dos teus servos e das tribos da tua herança.
18 Só por breve tempo foi o país possuído pelo teu santo povo; nossos adversários pisaram o teu santuário.
19 Tornamo-nos como aqueles sobre quem tu nunca dominaste e como os que nunca se chamaram pelo teu nome.*
1 Oh! Se fendesses os céus e descesses! Se os montes tremessem na tua presença,
2 como quando o fogo inflama os gravetos, como quando faz ferver as águas, para fazeres notório o teu nome aos teus adversários, de sorte que as nações tremessem da tua presença!
3 Quando fizeste coisas terríveis, que não esperávamos, desceste, e os montes tremeram à tua presença.
4 Porque desde a antiguidade não se ouviu, nem com ouvidos se percebeu, nem com os olhos se viu Deus além de ti, que trabalha para aquele que nele espera.
5 Sais ao encontro daquele que com alegria pratica justiça, daqueles que se lembram de ti nos teus caminhos; eis que te iraste, porque pecamos; por muito tempo temos pecado e havemos de ser salvos?
6 Mas todos nós somos como o imundo, e todas as nossas justiças, como trapo da imundícia; todos nós murchamos como a folha, e as nossas iniquidades, como um vento, nos arrebatam.
7 Já ninguém há que invoque o teu nome, que se desperte e te detenha; porque escondes de nós o rosto e nos consomes por causa das nossas iniquidades.
8 Mas agora, ó Senhor, tu és nosso Pai, nós somos o barro, e tu, o nosso oleiro; e todos nós, obra das tuas mãos.
9 Não te enfureças tanto, ó Senhor, nem perpetuamente te lembres da nossa iniquidade; olha, pois, nós te pedimos: todos nós somos o teu povo.
10 As tuas santas cidades tornaram-se em deserto, Sião, em ermo; Jerusalém está assolada.
11 O nosso templo santo e glorioso, em que nossos pais te louvavam, foi queimado; todas as nossas coisas preciosas se tornaram em ruínas.
12 Conter-te-ias tu ainda, ó Senhor, sobre estas calamidades? Ficarias calado e nos afligirias sobremaneira?*
1 Fui buscado pelos que não perguntavam por mim; fui achado por aqueles que não me buscavam; a um povo que não se chamava do meu nome, eu disse: Eis-me aqui, eis-me aqui.
2 Estendi as mãos todo dia a um povo rebelde, que anda por caminho que não é bom, seguindo os seus próprios pensamentos;
3 povo que de contínuo me irrita abertamente, sacrificando em jardins e queimando incenso sobre altares de tijolos;
4 que mora entre as sepulturas e passa as noites em lugares misteriosos; come carne de porco e tem no seu prato ensopado de carne abominável;
5 povo que diz: Fica onde estás, não te chegues a mim, porque sou mais santo do que tu. És no meu nariz como fumaça de fogo que arde o dia todo.
6 Eis que está escrito diante de mim, e não me calarei; mas eu pagarei, vingar-me-ei, totalmente,
7 das vossas iniquidades e, juntamente, das iniquidades de vossos pais, diz o Senhor, os quais queimaram incenso nos montes e me afrontaram nos outeiros; pelo que eu vos medirei totalmente a paga devida às suas obras antigas.
8 Assim diz o Senhor: Como quando se acha vinho num cacho de uvas, dizem: Não o desperdices, pois há bênção nele, assim farei por amor de meus servos e não os destruirei a todos.
9 Farei sair de Jacó descendência e de Judá, um herdeiro que possua os meus montes; e os meus eleitos herdarão a terra e os meus servos habitarão nela.
10 Sarom servirá de campo de pasto de ovelhas, e o vale de Acor, de lugar de repouso de gado, para o meu povo que me buscar.
11 Mas a vós outros, os que vos apartais do Senhor, os que vos esqueceis do meu santo monte, os que preparais mesa para a deusa Fortuna e misturais vinho para o deus Destino,
12 também vos destinarei à espada, e todos vos encurvareis à matança; porquanto chamei, e não respondestes, falei, e não atendestes; mas fizestes o que é mau perante mim e escolhestes aquilo em que eu não tinha prazer.
13 Pelo que assim diz o Senhor Deus: Eis que os meus servos comerão, mas vós padecereis fome; os meus servos beberão, mas vós tereis sede; os meus servos se alegrarão, mas vós vos envergonhareis;
14 os meus servos cantarão por terem o coração alegre, mas vós gritareis pela tristeza do vosso coração e uivareis pela angústia de espírito.
15 Deixareis o vosso nome aos meus eleitos por maldição, o Senhor Deus vos matará e a seus servos chamará por outro nome,
16 de sorte que aquele que se abençoar na terra, pelo Deus da verdade é que se abençoará; e aquele que jurar na terra, pelo Deus da verdade é que jurará; porque já estão esquecidas as angústias passadas e estão escondidas dos meus olhos.
17 Pois eis que eu crio novos céus e nova terra; e não haverá lembrança das coisas passadas, jamais haverá memória delas.
18 Mas vós folgareis e exultareis perpetuamente no que eu crio; porque eis que crio para Jerusalém alegria e para o seu povo, regozijo.
19 E exultarei por causa de Jerusalém e me alegrarei no meu povo, e nunca mais se ouvirá nela nem voz de choro nem de clamor.
20 Não haverá mais nela criança para viver poucos dias, nem velho que não cumpra os seus; porque morrer aos cem anos é morrer ainda jovem, e quem pecar só aos cem anos será amaldiçoado.
21 Eles edificarão casas e nelas habitarão; plantarão vinhas e comerão o seu fruto.
22 Não edificarão para que outros habitem; não plantarão para que outros comam; porque a longevidade do meu povo será como a da árvore, e os meus eleitos desfrutarão de todo as obras das suas próprias mãos.
23 Não trabalharão debalde, nem terão filhos para a calamidade, porque são a posteridade bendita do Senhor, e os seus filhos estarão com eles.
24 E será que, antes que clamem, eu responderei; estando eles ainda falando, eu os ouvirei.
25 O lobo e o cordeiro pastarão juntos, e o leão comerá palha como o boi; pó será a comida da serpente. Não se fará mal nem dano algum em todo o meu santo monte, diz o Senhor.*
1 Assim diz o Senhor: O céu é o meu trono, e a terra, o estrado dos meus pés; que casa me edificareis vós? E qual é o lugar do meu repouso?
2 Porque a minha mão fez todas estas coisas, e todas vieram a existir, diz o Senhor, mas o homem para quem olharei é este: o aflito e abatido de espírito e que treme da minha palavra.
3 O que imola um boi é como o que comete homicídio; o que sacrifica um cordeiro, como o que quebra o pescoço a um cão; o que oferece uma oblação, como o que oferece sangue de porco; o que queima incenso, como o que bendiz a um ídolo. Como estes escolheram os seus próprios caminhos, e a sua alma se deleita nas suas abominações,
4 assim eu lhes escolherei o infortúnio e farei vir sobre eles o que eles temem; porque clamei, e ninguém respondeu, falei, e não escutaram; mas fizeram o que era mau perante mim e escolheram aquilo em que eu não tinha prazer.
5 Ouvi a palavra do Senhor, vós, os que a temeis: Vossos irmãos, que vos aborrecem e que para longe vos lançam por causa do vosso amor ao meu nome e que dizem: Mostre o Senhor a sua glória, para que vejamos a vossa alegria, esses serão confundidos.
6 Voz de grande tumulto virá da cidade, voz do templo, voz do Senhor, que dá o pago aos seus inimigos.
7 Antes que estivesse de parto, deu à luz; antes que lhe viessem as dores, nasceu-lhe um menino.
8 Quem jamais ouviu tal coisa? Quem viu coisa semelhante? Pode, acaso, nascer uma terra num só dia? Ou nasce uma nação de uma só vez? Pois Sião, antes que lhe viessem as dores, deu à luz seus filhos.
9 Acaso, farei eu abrir a madre e não farei nascer? — diz o Senhor; acaso, eu que faço nascer fecharei a madre? — diz o teu Deus.
10 Regozijai-vos juntamente com Jerusalém e alegrai-vos por ela, vós todos os que a amais; exultai com ela, todos os que por ela pranteastes,
11 para que mameis e vos farteis dos peitos das suas consolações; para que sugueis e vos deleiteis com a abundância da sua glória.
12 Porque assim diz o Senhor: Eis que estenderei sobre ela a paz como um rio, e a glória das nações, como uma torrente que transborda; então, mamareis, nos braços vos trarão e sobre os joelhos vos acalentarão.
13 Como alguém a quem sua mãe consola, assim eu vos consolarei; e em Jerusalém vós sereis consolados.
14 Vós o vereis, e o vosso coração se regozijará, e os vossos ossos revigorarão como a erva tenra; então, o poder do Senhor será notório aos seus servos, e ele se indignará contra os seus inimigos.
15 Porque eis que o Senhor virá em fogo, e os seus carros, como um torvelinho, para tornar a sua ira em furor e a sua repreensão, em chamas de fogo,
16 porque com fogo e com a sua espada entrará o Senhor em juízo com toda a carne; e serão muitos os mortos da parte do Senhor.
17 Os que se santificam e se purificam para entrarem nos jardins após a deusa que está no meio, que comem carne de porco, coisas abomináveis e rato serão consumidos, diz o Senhor.
18 Porque conheço as suas obras e os seus pensamentos e venho para ajuntar todas as nações e línguas; elas virão e contemplarão a minha glória.
19 Porei entre elas um sinal e alguns dos que foram salvos enviarei às nações, a Társis, Pul e Lude, que atiram com o arco, a Tubal e Javã, até às terras do mar mais remotas, que jamais ouviram falar de mim, nem viram a minha glória; eles anunciarão entre as nações a minha glória.
20 Trarão todos os vossos irmãos, dentre todas as nações, por oferta ao Senhor, sobre cavalos, em liteiras e sobre mulas e dromedários, ao meu santo monte, a Jerusalém, diz o Senhor, como quando os filhos de Israel trazem as suas ofertas de manjares, em vasos puros à Casa do Senhor.
21 Também deles tomarei a alguns para sacerdotes e para levitas, diz o Senhor.
22 Porque, como os novos céus e a nova terra, que hei de fazer, estarão diante de mim, diz o Senhor, assim há de estar a vossa posteridade e o vosso nome.
23 E será que, de uma Festa da Lua Nova à outra e de um sábado a outro, virá toda a carne a adorar perante mim, diz o Senhor.
24 Eles sairão e verão os cadáveres dos homens que prevaricaram contra mim; porque o seu verme nunca morrerá, nem o seu fogo se apagará; e eles serão um horror para toda a carne.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Isaías','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)