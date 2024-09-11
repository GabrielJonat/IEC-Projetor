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
1 Palavra do Pregador, filho de Davi, rei de Jerusalém:
2 Vaidade de vaidades, diz o Pregador; vaidade de vaidades, tudo é vaidade.
3 Que proveito tem o homem de todo o seu trabalho, com que se afadiga debaixo do sol?
4 Geração vai e geração vem; mas a terra permanece para sempre.
5 Levanta-se o sol, e põe-se o sol, e volta ao seu lugar, onde nasce de novo.
6 O vento vai para o sul e faz o seu giro para o norte; volve-se, e revolve-se, na sua carreira, e retorna aos seus circuitos.
7 Todos os rios correm para o mar, e o mar não se enche; ao lugar para onde correm os rios, para lá tornam eles a correr.
8 Todas as coisas são canseiras tais, que ninguém as pode exprimir; os olhos não se fartam de ver, nem se enchem os ouvidos de ouvir.
9 O que foi é o que há de ser; e o que se fez, isso se tornará a fazer; nada há, pois, novo debaixo do sol.
10 Há alguma coisa de que se possa dizer: Vê, isto é novo? Não! Já foi nos séculos que foram antes de nós.
11 Já não há lembrança das coisas que precederam; e das coisas posteriores também não haverá memória entre os que hão de vir depois delas.
12 Eu, o Pregador, venho sendo rei de Israel, em Jerusalém.
13 Apliquei o coração a esquadrinhar e a informar-me com sabedoria de tudo quanto sucede debaixo do céu; este enfadonho trabalho impôs Deus aos filhos dos homens, para nele os afligir.
14 Atentei para todas as obras que se fazem debaixo do sol, e eis que tudo era vaidade e correr atrás do vento.
15 Aquilo que é torto não se pode endireitar; e o que falta não se pode calcular.
16 Disse comigo: eis que me engrandeci e sobrepujei em sabedoria a todos os que antes de mim existiram em Jerusalém; com efeito, o meu coração tem tido larga experiência da sabedoria e do conhecimento.
17 Apliquei o coração a conhecer a sabedoria e a saber o que é loucura e o que é estultícia; e vim a saber que também isto é correr atrás do vento.
18 Porque na muita sabedoria há muito enfado; e quem aumenta ciência aumenta tristeza.*
1 Disse comigo: vamos! Eu te provarei com a alegria; goza, pois, a felicidade; mas também isso era vaidade.
2 Do riso disse: é loucura; e da alegria: de que serve?
3 Resolvi no meu coração dar-me ao vinho, regendo-me, contudo, pela sabedoria, e entregar-me à loucura, até ver o que melhor seria que fizessem os filhos dos homens debaixo do céu, durante os poucos dias da sua vida.
4 Empreendi grandes obras; edifiquei para mim casas; plantei para mim vinhas.
5 Fiz jardins e pomares para mim e nestes plantei árvores frutíferas de toda espécie.
6 Fiz para mim açudes, para regar com eles o bosque em que reverdeciam as árvores.
7 Comprei servos e servas e tive servos nascidos em casa; também possuí bois e ovelhas, mais do que possuíram todos os que antes de mim viveram em Jerusalém.
8 Amontoei também para mim prata e ouro e tesouros de reis e de províncias; provi-me de cantores e cantoras e das delícias dos filhos dos homens: mulheres e mulheres.
9 Engrandeci-me e sobrepujei a todos os que viveram antes de mim em Jerusalém; perseverou também comigo a minha sabedoria.
10 Tudo quanto desejaram os meus olhos não lhes neguei, nem privei o coração de alegria alguma, pois eu me alegrava com todas as minhas fadigas, e isso era a recompensa de todas elas.
11 Considerei todas as obras que fizeram as minhas mãos, como também o trabalho que eu, com fadigas, havia feito; e eis que tudo era vaidade e correr atrás do vento, e nenhum proveito havia debaixo do sol.
12 Então, passei a considerar a sabedoria, e a loucura, e a estultícia. Que fará o homem que seguir ao rei? O mesmo que outros já fizeram.
13 Então, vi que a sabedoria é mais proveitosa do que a estultícia, quanto a luz traz mais proveito do que as trevas.
14 Os olhos do sábio estão na sua cabeça, mas o estulto anda em trevas; contudo, entendi que o mesmo lhes sucede a ambos.
15 Pelo que disse eu comigo: como acontece ao estulto, assim me sucede a mim; por que, pois, busquei eu mais a sabedoria? Então, disse a mim mesmo que também isso era vaidade.
16 Pois, tanto do sábio como do estulto, a memória não durará para sempre; pois, passados alguns dias, tudo cai no esquecimento. Ah! Morre o sábio, e da mesma sorte, o estulto!
17 Pelo que aborreci a vida, pois me foi penosa a obra que se faz debaixo do sol; sim, tudo é vaidade e correr atrás do vento.
18 Também aborreci todo o meu trabalho, com que me afadiguei debaixo do sol, visto que o seu ganho eu havia de deixar a quem viesse depois de mim.
19 E quem pode dizer se será sábio ou estulto? Contudo, ele terá domínio sobre todo o ganho das minhas fadigas e sabedoria debaixo do sol; também isto é vaidade.
20 Então, me empenhei por que o coração se desesperasse de todo trabalho com que me afadigara debaixo do sol.
21 Porque há homem cujo trabalho é feito com sabedoria, ciência e destreza; contudo, deixará o seu ganho como porção a quem por ele não se esforçou; também isto é vaidade e grande mal.
22 Pois que tem o homem de todo o seu trabalho e da fadiga do seu coração, em que ele anda trabalhando debaixo do sol?
23 Porque todos os seus dias são dores, e o seu trabalho, desgosto; até de noite não descansa o seu coração; também isto é vaidade.
24 Nada há melhor para o homem do que comer, beber e fazer que a sua alma goze o bem do seu trabalho. No entanto, vi também que isto vem da mão de Deus,
25 pois, separado deste, quem pode comer ou quem pode alegrar-se?
26 Porque Deus dá sabedoria, conhecimento e prazer ao homem que lhe agrada; mas ao pecador dá trabalho, para que ele ajunte e amontoe, a fim de dar àquele que agrada a Deus. Também isto é vaidade e correr atrás do vento.*
1 Tudo tem o seu tempo determinado, e há tempo para todo propósito debaixo do céu:
2 há tempo de nascer e tempo de morrer; tempo de plantar e tempo de arrancar o que se plantou;
3 tempo de matar e tempo de curar; tempo de derribar e tempo de edificar;
4 tempo de chorar e tempo de rir; tempo de prantear e tempo de saltar de alegria;
5 tempo de espalhar pedras e tempo de ajuntar pedras; tempo de abraçar e tempo de afastar-se de abraçar;
6 tempo de buscar e tempo de perder; tempo de guardar e tempo de deitar fora;
7 tempo de rasgar e tempo de coser; tempo de estar calado e tempo de falar;
8 tempo de amar e tempo de aborrecer; tempo de guerra e tempo de paz.
9 Que proveito tem o trabalhador naquilo com que se afadiga?
10 Vi o trabalho que Deus impôs aos filhos dos homens, para com ele os afligir.
11 Tudo fez Deus formoso no seu devido tempo; também pôs a eternidade no coração do homem, sem que este possa descobrir as obras que Deus fez desde o princípio até ao fim.
12 Sei que nada há melhor para o homem do que regozijar-se e levar vida regalada;
13 e também que é dom de Deus que possa o homem comer, beber e desfrutar o bem de todo o seu trabalho.
14 Sei que tudo quanto Deus faz durará eternamente; nada se lhe pode acrescentar e nada lhe tirar; e isto faz Deus para que os homens temam diante dele.
15 O que é já foi, e o que há de ser também já foi; Deus fará renovar-se o que se passou.
16 Vi ainda debaixo do sol que no lugar do juízo reinava a maldade e no lugar da justiça, maldade ainda.
17 Então, disse comigo: Deus julgará o justo e o perverso; pois há tempo para todo propósito e para toda obra.
18 Disse ainda comigo: é por causa dos filhos dos homens, para que Deus os prove, e eles vejam que são em si mesmos como os animais.
19 Porque o que sucede aos filhos dos homens sucede aos animais; o mesmo lhes sucede: como morre um, assim morre o outro, todos têm o mesmo fôlego de vida, e nenhuma vantagem tem o homem sobre os animais; porque tudo é vaidade.
20 Todos vão para o mesmo lugar; todos procedem do pó e ao pó tornarão.
21 Quem sabe se o fôlego de vida dos filhos dos homens se dirige para cima e o dos animais para baixo, para a terra?
22 Pelo que vi não haver coisa melhor do que alegrar-se o homem nas suas obras, porque essa é a sua recompensa; quem o fará voltar para ver o que será depois dele?*
1 Vi ainda todas as opressões que se fazem debaixo do sol: vi as lágrimas dos que foram oprimidos, sem que ninguém os consolasse; vi a violência na mão dos opressores, sem que ninguém consolasse os oprimidos.
2 Pelo que tenho por mais felizes os que já morreram, mais do que os que ainda vivem;
3 porém mais que uns e outros tenho por feliz aquele que ainda não nasceu e não viu as más obras que se fazem debaixo do sol.
4 Então, vi que todo trabalho e toda destreza em obras provêm da inveja do homem contra o seu próximo. Também isto é vaidade e correr atrás do vento.
5 O tolo cruza os braços e come a própria carne, dizendo:
6 Melhor é um punhado de descanso do que ambas as mãos cheias de trabalho e correr atrás do vento.
7 Então, considerei outra vaidade debaixo do sol,
8 isto é, um homem sem ninguém, não tem filho nem irmã; contudo, não cessa de trabalhar, e seus olhos não se fartam de riquezas; e não diz: Para quem trabalho eu, se nego à minha alma os bens da vida? Também isto é vaidade e enfadonho trabalho.
9 Melhor é serem dois do que um, porque têm melhor paga do seu trabalho.
10 Porque se caírem, um levanta o companheiro; ai, porém, do que estiver só; pois, caindo, não haverá quem o levante.
11 Também, se dois dormirem juntos, eles se aquentarão; mas um só como se aquentará?
12 Se alguém quiser prevalecer contra um, os dois lhe resistirão; o cordão de três dobras não se rebenta com facilidade.
13 Melhor é o jovem pobre e sábio do que o rei velho e insensato, que já não se deixa admoestar,
14 ainda que aquele saia do cárcere para reinar ou nasça pobre no reino deste.
15 Vi todos os viventes que andam debaixo do sol com o jovem sucessor, que ficará em lugar do rei.
16 Era sem conta todo o povo que ele dominava; tampouco os que virão depois se hão de regozijar nele. Na verdade, que também isto é vaidade e correr atrás do vento.*
1 Guarda o pé, quando entrares na Casa de Deus; chegar-se para ouvir é melhor do que oferecer sacrifícios de tolos, pois não sabem que fazem mal.
2 Não te precipites com a tua boca, nem o teu coração se apresse a pronunciar palavra alguma diante de Deus; porque Deus está nos céus, e tu, na terra; portanto, sejam poucas as tuas palavras.
3 Porque dos muitos trabalhos vêm os sonhos, e do muito falar, palavras néscias.
4 Quando a Deus fizeres algum voto, não tardes em cumpri-lo; porque não se agrada de tolos. Cumpre o voto que fazes.
5 Melhor é que não votes do que votes e não cumpras.
6 Não consintas que a tua boca te faça culpado, nem digas diante do mensageiro de Deus que foi inadvertência; por que razão se iraria Deus por causa da tua palavra, a ponto de destruir as obras das tuas mãos?
7 Porque, como na multidão dos sonhos há vaidade, assim também, nas muitas palavras; tu, porém, teme a Deus.
8 Se vires em alguma província opressão de pobres e o roubo em lugar do direito e da justiça, não te maravilhes de semelhante caso; porque o que está alto tem acima de si outro mais alto que o explora, e sobre estes há ainda outros mais elevados que também exploram.
9 O proveito da terra é para todos; até o rei se serve do campo.
10 Quem ama o dinheiro jamais dele se farta; e quem ama a abundância nunca se farta da renda; também isto é vaidade.
11 Onde os bens se multiplicam, também se multiplicam os que deles comem; que mais proveito, pois, têm os seus donos do que os verem com seus olhos?
12 Doce é o sono do trabalhador, quer coma pouco, quer muito; mas a fartura do rico não o deixa dormir.
13 Grave mal vi debaixo do sol: as riquezas que seus donos guardam para o próprio dano.
14 E, se tais riquezas se perdem por qualquer má aventura, ao filho que gerou nada lhe fica na mão.
15 Como saiu do ventre de sua mãe, assim nu voltará, indo-se como veio; e do seu trabalho nada poderá levar consigo.
16 Também isto é grave mal: precisamente como veio, assim ele vai; e que proveito lhe vem de haver trabalhado para o vento?
17 Nas trevas, comeu em todos os seus dias, com muito enfado, com enfermidades e indignação.
18 Eis o que eu vi: boa e bela coisa é comer e beber e gozar cada um do bem de todo o seu trabalho, com que se afadigou debaixo do sol, durante os poucos dias da vida que Deus lhe deu; porque esta é a sua porção.
19 Quanto ao homem a quem Deus conferiu riquezas e bens e lhe deu poder para deles comer, e receber a sua porção, e gozar do seu trabalho, isto é dom de Deus.
20 Porque não se lembrará muito dos dias da sua vida, porquanto Deus lhe enche o coração de alegria.*
1 Há um mal que vi debaixo do sol e que pesa sobre os homens:
2 o homem a quem Deus conferiu riquezas, bens e honra, e nada lhe falta de tudo quanto a sua alma deseja, mas Deus não lhe concede que disso coma; antes, o estranho o come; também isto é vaidade e grave aflição.
3 Se alguém gerar cem filhos e viver muitos anos, até avançada idade, e se a sua alma não se fartar do bem, e além disso não tiver sepultura, digo que um aborto é mais feliz do que ele;
4 pois debalde vem o aborto e em trevas se vai, e de trevas se cobre o seu nome;
5 não viu o sol, nada conhece. Todavia, tem mais descanso do que o outro,
6 ainda que aquele vivesse duas vezes mil anos, mas não gozasse o bem. Porventura, não vão todos para o mesmo lugar?
7 Todo trabalho do homem é para a sua boca; e, contudo, nunca se satisfaz o seu apetite.
8 Pois que vantagem tem o sábio sobre o tolo? Ou o pobre que sabe andar perante os vivos?
9 Melhor é a vista dos olhos do que o andar ocioso da cobiça; também isto é vaidade e correr atrás do vento.
10 A tudo quanto há de vir já se lhe deu o nome, e sabe-se o que é o homem, e que não pode contender com quem é mais forte do que ele.
11 É certo que há muitas coisas que só aumentam a vaidade, mas que aproveita isto ao homem?
12 Pois quem sabe o que é bom para o homem durante os poucos dias da sua vida de vaidade, os quais gasta como sombra? Quem pode declarar ao homem o que será depois dele debaixo do sol?*
1 Melhor é a boa fama do que o unguento precioso, e o dia da morte, melhor do que o dia do nascimento.
2 Melhor é ir à casa onde há luto do que ir à casa onde há banquete, pois naquela se vê o fim de todos os homens; e os vivos que o tomem em consideração.
3 Melhor é a mágoa do que o riso, porque com a tristeza do rosto se faz melhor o coração.
4 O coração dos sábios está na casa do luto, mas o dos insensatos, na casa da alegria.
5 Melhor é ouvir a repreensão do sábio do que ouvir a canção do insensato.
6 Pois, qual o crepitar dos espinhos debaixo de uma panela, tal é a risada do insensato; também isto é vaidade.
7 Verdadeiramente, a opressão faz endoidecer até o sábio, e o suborno corrompe o coração.
8 Melhor é o fim das coisas do que o seu princípio; melhor é o paciente do que o arrogante.
9 Não te apresses em irar-te, porque a ira se abriga no íntimo dos insensatos.
10 Jamais digas: Por que foram os dias passados melhores do que estes? Pois não é sábio perguntar assim.
11 Boa é a sabedoria, havendo herança, e de proveito, para os que veem o sol.
12 A sabedoria protege como protege o dinheiro; mas o proveito da sabedoria é que ela dá vida ao seu possuidor.
13 Atenta para as obras de Deus, pois quem poderá endireitar o que ele torceu?
14 No dia da prosperidade, goza do bem; mas, no dia da adversidade, considera em que Deus fez tanto este como aquele, para que o homem nada descubra do que há de vir depois dele.
15 Tudo isto vi nos dias da minha vaidade: há justo que perece na sua justiça, e há perverso que prolonga os seus dias na sua perversidade.
16 Não sejas demasiadamente justo, nem exageradamente sábio; por que te destruirias a ti mesmo?
17 Não sejas demasiadamente perverso, nem sejas louco; por que morrerias fora do teu tempo?
18 Bom é que retenhas isto e também daquilo não retires a mão; pois quem teme a Deus de tudo isto sai ileso.
19 A sabedoria fortalece ao sábio, mais do que dez poderosos que haja na cidade.
20 Não há homem justo sobre a terra que faça o bem e que não peque.
21 Não apliques o coração a todas as palavras que se dizem, para que não venhas a ouvir o teu servo a amaldiçoar-te,
22 pois tu sabes que muitas vezes tu mesmo tens amaldiçoado a outros.
23 Tudo isto experimentei pela sabedoria; e disse: tornar-me-ei sábio, mas a sabedoria estava longe de mim.
24 O que está longe e mui profundo, quem o achará?
25 Apliquei-me a conhecer, e a investigar, e a buscar a sabedoria e meu juízo de tudo, e a conhecer que a perversidade é insensatez e a insensatez, loucura.
26 Achei coisa mais amarga do que a morte: a mulher cujo coração são redes e laços e cujas mãos são grilhões; quem for bom diante de Deus fugirá dela, mas o pecador virá a ser seu prisioneiro.
27 Eis o que achei, diz o Pregador, conferindo uma coisa com outra, para a respeito delas formar o meu juízo,
28 juízo que ainda procuro e não o achei: entre mil homens achei um como esperava, mas entre tantas mulheres não achei nem sequer uma.
29 Eis o que tão somente achei: que Deus fez o homem reto, mas ele se meteu em muitas astúcias.*
1 Quem é como o sábio? E quem sabe a interpretação das coisas? A sabedoria do homem faz reluzir o seu rosto, e muda-se a dureza da sua face.
2 Eu te digo: observa o mandamento do rei, e isso por causa do teu juramento feito a Deus.
3 Não te apresses em deixar a presença dele, nem te obstines em coisa má, porque ele faz o que bem entende.
4 Porque a palavra do rei tem autoridade suprema; e quem lhe dirá: Que fazes?
5 Quem guarda o mandamento não experimenta nenhum mal; e o coração do sábio conhece o tempo e o modo.
6 Porque para todo propósito há tempo e modo; porquanto é grande o mal que pesa sobre o homem.
7 Porque este não sabe o que há de suceder; e, como há de ser, ninguém há que lho declare.
8 Não há nenhum homem que tenha domínio sobre o vento para o reter; nem tampouco tem ele poder sobre o dia da morte; nem há tréguas nesta peleja; nem tampouco a perversidade livrará aquele que a ela se entrega.
9 Tudo isto vi quando me apliquei a toda obra que se faz debaixo do sol; há tempo em que um homem tem domínio sobre outro homem, para arruiná-lo.
10 Assim também vi os perversos receberem sepultura e entrarem no repouso, ao passo que os que frequentavam o lugar santo foram esquecidos na cidade onde fizeram o bem; também isto é vaidade.
11 Visto como se não executa logo a sentença sobre a má obra, o coração dos filhos dos homens está inteiramente disposto a praticar o mal.
12 Ainda que o pecador faça o mal cem vezes, e os dias se lhe prolonguem, eu sei com certeza que bem sucede aos que temem a Deus.
13 Mas o perverso não irá bem, nem prolongará os seus dias; será como a sombra, visto que não teme diante de Deus.
14 Ainda há outra vaidade sobre a terra: justos a quem sucede segundo as obras dos perversos, e perversos a quem sucede segundo as obras dos justos. Digo que também isto é vaidade.
15 Então, exaltei eu a alegria, porquanto para o homem nenhuma coisa há melhor debaixo do sol do que comer, beber e alegrar-se; pois isso o acompanhará no seu trabalho nos dias da vida que Deus lhe dá debaixo do sol.
16 Aplicando-me a conhecer a sabedoria e a ver o trabalho que há sobre a terra — pois nem de dia nem de noite vê o homem sono nos seus olhos —,
17 então, contemplei toda a obra de Deus e vi que o homem não pode compreender a obra que se faz debaixo do sol; por mais que trabalhe o homem para a descobrir, não a entenderá; e, ainda que diga o sábio que a virá a conhecer, nem por isso a poderá achar.*
1 Deveras me apliquei a todas estas coisas para claramente entender tudo isto: que os justos, e os sábios, e os seus feitos estão nas mãos de Deus; e, se é amor ou se é ódio que está à sua espera, não o sabe o homem. Tudo lhe está oculto no futuro.
2 Tudo sucede igualmente a todos: o mesmo sucede ao justo e ao perverso; ao bom, ao puro e ao impuro; tanto ao que sacrifica como ao que não sacrifica; ao bom como ao pecador; ao que jura como ao que teme o juramento.
3 Este é o mal que há em tudo quanto se faz debaixo do sol: a todos sucede o mesmo; também o coração dos homens está cheio de maldade, nele há desvarios enquanto vivem; depois, rumo aos mortos.
4 Para aquele que está entre os vivos há esperança; porque mais vale um cão vivo do que um leão morto.
5 Porque os vivos sabem que hão de morrer, mas os mortos não sabem coisa nenhuma, nem tampouco terão eles recompensa, porque a sua memória jaz no esquecimento.
6 Amor, ódio e inveja para eles já pereceram; para sempre não têm eles parte em coisa alguma do que se faz debaixo do sol.
7 Vai, pois, come com alegria o teu pão e bebe gostosamente o teu vinho, pois Deus já de antemão se agrada das tuas obras.
8 Em todo tempo sejam alvas as tuas vestes, e jamais falte o óleo sobre a tua cabeça.
9 Goza a vida com a mulher que amas, todos os dias de tua vida fugaz, os quais Deus te deu debaixo do sol; porque esta é a tua porção nesta vida pelo trabalho com que te afadigaste debaixo do sol.
10 Tudo quanto te vier à mão para fazer, faze-o conforme as tuas forças, porque no além, para onde tu vais, não há obra, nem projetos, nem conhecimento, nem sabedoria alguma.
11 Vi ainda debaixo do sol que não é dos ligeiros o prêmio, nem dos valentes, a vitória, nem tampouco dos sábios, o pão, nem ainda dos prudentes, a riqueza, nem dos inteligentes, o favor; porém tudo depende do tempo e do acaso.
12 Pois o homem não sabe a sua hora. Como os peixes que se apanham com a rede traiçoeira e como os passarinhos que se prendem com o laço, assim se enredam também os filhos dos homens no tempo da calamidade, quando cai de repente sobre eles.
13 Também vi este exemplo de sabedoria debaixo do sol, que foi para mim grande.
14 Houve uma pequena cidade em que havia poucos homens; veio contra ela um grande rei, sitiou-a e levantou contra ela grandes baluartes.
15 Encontrou-se nela um homem pobre, porém sábio, que a livrou pela sua sabedoria; contudo, ninguém se lembrou mais daquele pobre.
16 Então, disse eu: melhor é a sabedoria do que a força, ainda que a sabedoria do pobre é desprezada, e as suas palavras não são ouvidas.
17 As palavras dos sábios, ouvidas em silêncio, valem mais do que os gritos de quem governa entre tolos.
18 Melhor é a sabedoria do que as armas de guerra, mas um só pecador destrói muitas coisas boas.*
1 Qual a mosca morta faz o unguento do perfumador exalar mau cheiro, assim é para a sabedoria e a honra um pouco de estultícia.
2 O coração do sábio se inclina para o lado direito, mas o do estulto, para o da esquerda.
3 Quando o tolo vai pelo caminho, falta-lhe o entendimento; e, assim, a todos mostra que é estulto.
4 Levantando-se contra ti a indignação do governador, não deixes o teu lugar, porque o ânimo sereno acalma grandes ofensores.
5 Ainda há um mal que vi debaixo do sol, erro que procede do governador:
6 o tolo posto em grandes alturas, mas os ricos assentados em lugar baixo.
7 Vi servos a cavalo e príncipes andando a pé como servos sobre a terra.
8 Quem abre uma cova nela cairá, e quem rompe um muro, mordê-lo-á uma cobra.
9 Quem arranca pedras será maltratado por elas, e o que racha lenha expõe-se ao perigo.
10 Se o ferro está embotado, e não se lhe afia o corte, é preciso redobrar a força; mas a sabedoria resolve com bom êxito.
11 Se a cobra morder antes de estar encantada, não há vantagem no encantador.
12 Nas palavras do sábio há favor, mas ao tolo os seus lábios devoram.
13 As primeiras palavras da boca do tolo são estultícia, e as últimas, loucura perversa.
14 O estulto multiplica as palavras, ainda que o homem não sabe o que sucederá; e quem lhe manifestará o que será depois dele?
15 O trabalho do tolo o fatiga, pois nem sabe ir à cidade.
16 Ai de ti, ó terra cujo rei é criança e cujos príncipes se banqueteiam já de manhã.
17 Ditosa, tu, ó terra cujo rei é filho de nobres e cujos príncipes se sentam à mesa a seu tempo para refazerem as forças e não para bebedice.
18 Pela muita preguiça desaba o teto, e pela frouxidão das mãos goteja a casa.
19 O festim faz-se para rir, o vinho alegra a vida, e o dinheiro atende a tudo.
20 Nem no teu pensamento amaldiçoes o rei, nem tampouco no mais interior do teu quarto, o rico; porque as aves dos céus poderiam levar a tua voz, e o que tem asas daria notícia das tuas palavras.*
1 Lança o teu pão sobre as águas, porque depois de muitos dias o acharás.
2 Reparte com sete e ainda com oito, porque não sabes que mal sobrevirá à terra.
3 Estando as nuvens cheias, derramam aguaceiro sobre a terra; caindo a árvore para o sul ou para o norte, no lugar em que cair, aí ficará.
4 Quem somente observa o vento nunca semeará, e o que olha para as nuvens nunca segará.
5 Assim como tu não sabes qual o caminho do vento, nem como se formam os ossos no ventre da mulher grávida, assim também não sabes as obras de Deus, que faz todas as coisas.
6 Semeia pela manhã a tua semente e à tarde não repouses a mão, porque não sabes qual prosperará; se esta, se aquela ou se ambas igualmente serão boas.
7 Doce é a luz, e agradável aos olhos, ver o sol.
8 Ainda que o homem viva muitos anos, regozije-se em todos eles; contudo, deve lembrar-se de que há dias de trevas, porque serão muitos. Tudo quanto sucede é vaidade.
A mocidade
9 Alegra-te, jovem, na tua juventude, e recreie-se o teu coração nos dias da tua mocidade; anda pelos caminhos que satisfazem ao teu coração e agradam aos teus olhos; sabe, porém, que de todas estas coisas Deus te pedirá contas.
10 Afasta, pois, do teu coração o desgosto e remove da tua carne a dor, porque a juventude e a primavera da vida são vaidade.*
1 Lembra-te do teu Criador nos dias da tua mocidade, antes que venham os maus dias, e cheguem os anos dos quais dirás: Não tenho neles prazer;
2 antes que se escureçam o sol, a lua e as estrelas do esplendor da tua vida, e tornem a vir as nuvens depois do aguaceiro;
3 no dia em que tremerem os guardas da casa, os teus braços, e se curvarem os homens outrora fortes, as tuas pernas, e cessarem os teus moedores da boca, por já serem poucos, e se escurecerem os teus olhos nas janelas;
4 e os teus lábios, quais portas da rua, se fecharem; no dia em que não puderes falar em alta voz, te levantares à voz das aves, e todas as harmonias, filhas da música, te diminuírem;
5 como também quando temeres o que é alto, e te espantares no caminho, e te embranqueceres, como floresce a amendoeira, e o gafanhoto te for um peso, e te perecer o apetite; porque vais à casa eterna, e os pranteadores andem rodeando pela praça;
6 antes que se rompa o fio de prata, e se despedace o copo de ouro, e se quebre o cântaro junto à fonte, e se desfaça a roda junto ao poço,
7 e o pó volte à terra, como o era, e o espírito volte a Deus, que o deu.
8 Vaidade de vaidade, diz o Pregador, tudo é vaidade.
9 O Pregador, além de sábio, ainda ensinou ao povo o conhecimento; e, atentando e esquadrinhando, compôs muitos provérbios.
10 Procurou o Pregador achar palavras agradáveis e escrever com retidão palavras de verdade.
11 As palavras dos sábios são como aguilhões, e como pregos bem-fixados as sentenças coligidas, dadas pelo único Pastor.
12 Demais, filho meu, atenta: não há limite para fazer livros, e o muito estudar é enfado da carne.
13 De tudo o que se tem ouvido, a suma é: Teme a Deus e guarda os seus mandamentos; porque isto é o dever de todo homem.
14 Porque Deus há de trazer a juízo todas as obras, até as que estão escondidas, quer sejam boas, quer sejam más.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Eclesiastes','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)