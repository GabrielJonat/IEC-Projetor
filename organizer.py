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
1 Visto que muitos houve que empreenderam uma narração coordenada dos fatos que entre nós se realizaram,
2 conforme nos transmitiram os que desde o princípio foram deles testemunhas oculares e ministros da palavra,
3 igualmente a mim me pareceu bem, depois de acurada investigação de tudo desde sua origem, dar-te por escrito, excelentíssimo Teófilo, uma exposição em ordem,
4 para que tenhas plena certeza das verdades em que foste instruído.
5 Nos dias de Herodes, rei da Judeia, houve um sacerdote chamado Zacarias, do turno de Abias. Sua mulher era das filhas de Arão e se chamava Isabel.
6 Ambos eram justos diante de Deus, vivendo irrepreensivelmente em todos os preceitos e mandamentos do Senhor.
7 E não tinham filhos, porque Isabel era estéril, sendo eles avançados em dias.
8 Ora, aconteceu que, exercendo ele diante de Deus o sacerdócio na ordem do seu turno, coube-lhe por sorte,
9 segundo o costume sacerdotal, entrar no santuário do Senhor para queimar o incenso;
10 e, durante esse tempo, toda a multidão do povo permanecia da parte de fora, orando.
11 E eis que lhe apareceu um anjo do Senhor, em pé, à direita do altar do incenso.
12 Vendo-o, Zacarias turbou-se, e apoderou-se dele o temor.
13 Disse-lhe, porém, o anjo: Zacarias, não temas, porque a tua oração foi ouvida; e Isabel, tua mulher, te dará à luz um filho, a quem darás o nome de João.
14 Em ti haverá prazer e alegria, e muitos se regozijarão com o seu nascimento.
15 Pois ele será grande diante do Senhor, não beberá vinho nem bebida forte e será cheio do Espírito Santo, já do ventre materno.
16 E converterá muitos dos filhos de Israel ao Senhor, seu Deus.
17 E irá adiante do Senhor no espírito e poder de Elias, para converter o coração dos pais aos filhos, converter os desobedientes à prudência dos justos e habilitar para o Senhor um povo preparado.
18 Então, perguntou Zacarias ao anjo: Como saberei isto? Pois eu sou velho, e minha mulher, avançada em dias.
19 Respondeu-lhe o anjo: Eu sou Gabriel, que assisto diante de Deus, e fui enviado para falar-te e trazer-te estas boas-novas.
20 Todavia, ficarás mudo e não poderás falar até ao dia em que estas coisas venham a realizar-se; porquanto não acreditaste nas minhas palavras, as quais, a seu tempo, se cumprirão.
21 O povo estava esperando a Zacarias e admirava-se de que tanto se demorasse no santuário.
22 Mas, saindo ele, não lhes podia falar; então, entenderam que tivera uma visão no santuário. E expressava-se por acenos e permanecia mudo.
23 Sucedeu que, terminados os dias de seu ministério, voltou para casa.
24 Passados esses dias, Isabel, sua mulher, concebeu e ocultou-se por cinco meses, dizendo:
25 Assim me fez o Senhor, contemplando-me, para anular o meu opróbrio perante os homens.
26 No sexto mês, foi o anjo Gabriel enviado, da parte de Deus, para uma cidade da Galileia, chamada Nazaré,
27 a uma virgem desposada com certo homem da casa de Davi, cujo nome era José; a virgem chamava-se Maria.
28 E, entrando o anjo aonde ela estava, disse: Alegra-te, muito favorecida! O Senhor é contigo.
29 Ela, porém, ao ouvir esta palavra, perturbou-se muito e pôs-se a pensar no que significaria esta saudação.
30 Mas o anjo lhe disse: Maria, não temas; porque achaste graça diante de Deus.
31 Eis que conceberás e darás à luz um filho, a quem chamarás pelo nome de Jesus.
32 Este será grande e será chamado Filho do Altíssimo; Deus, o Senhor, lhe dará o trono de Davi, seu pai;
33 ele reinará para sempre sobre a casa de Jacó, e o seu reinado não terá fim.
34 Então, disse Maria ao anjo: Como será isto, pois não tenho relação com homem algum?
35 Respondeu-lhe o anjo: Descerá sobre ti o Espírito Santo, e o poder do Altíssimo te envolverá com a sua sombra; por isso, também o ente santo que há de nascer será chamado Filho de Deus.
36 E Isabel, tua parenta, igualmente concebeu um filho na sua velhice, sendo este já o sexto mês para aquela que diziam ser estéril.
37 Porque para Deus não haverá impossíveis em todas as suas promessas.
38 Então, disse Maria: Aqui está a serva do Senhor; que se cumpra em mim conforme a tua palavra. E o anjo se ausentou dela.
39 Naqueles dias, dispondo-se Maria, foi apressadamente à região montanhosa, a uma cidade de Judá,
40 entrou na casa de Zacarias e saudou Isabel.
41 Ouvindo esta a saudação de Maria, a criança lhe estremeceu no ventre; então, Isabel ficou possuída do Espírito Santo.
42 E exclamou em alta voz: Bendita és tu entre as mulheres, e bendito o fruto do teu ventre!
43 E de onde me provém que me venha visitar a mãe do meu Senhor?
44 Pois, logo que me chegou aos ouvidos a voz da tua saudação, a criança estremeceu de alegria dentro de mim.
45 Bem-aventurada a que creu, porque serão cumpridas as palavras que lhe foram ditas da parte do Senhor.
46 Então, disse Maria: A minha alma engrandece ao Senhor,
47 e o meu espírito se alegrou em Deus, meu Salvador,
48 porque contemplou na humildade da sua serva. Pois, desde agora, todas as gerações me considerarão bem-aventurada,
49 porque o Poderoso me fez grandes coisas. Santo é o seu nome.
50 A sua misericórdia vai de geração em geração sobre os que o temem.
51 Agiu com o seu braço valorosamente; dispersou os que, no coração, alimentavam pensamentos soberbos.
52 Derribou do seu trono os poderosos e exaltou os humildes.
53 Encheu de bens os famintos e despediu vazios os ricos.
54 Amparou a Israel, seu servo, a fim de lembrar-se da sua misericórdia
55 a favor de Abraão e de sua descendência, para sempre, como prometera aos nossos pais.
56 Maria permaneceu cerca de três meses com Isabel e voltou para casa.
57 A Isabel cumpriu-se o tempo de dar à luz, e teve um filho.
58 Ouviram os seus vizinhos e parentes que o Senhor usara de grande misericórdia para com ela e participaram do seu regozijo.
59 Sucedeu que, no oitavo dia, foram circuncidar o menino e queriam dar-lhe o nome de seu pai, Zacarias.
60 De modo nenhum! Respondeu sua mãe. Pelo contrário, ele deve ser chamado João.
61 Disseram-lhe: Ninguém há na tua parentela que tenha este nome.
62 E perguntaram, por acenos, ao pai do menino que nome queria que lhe dessem.
63 Então, pedindo ele uma tabuinha, escreveu: João é o seu nome. E todos se admiraram.
64 Imediatamente, a boca se lhe abriu, e, desimpedida a língua, falava louvando a Deus.
65 Sucedeu que todos os seus vizinhos ficaram possuídos de temor, e por toda a região montanhosa da Judeia foram divulgadas estas coisas.
66 Todos os que as ouviram guardavam-nas no coração, dizendo: Que virá a ser, pois, este menino? E a mão do Senhor estava com ele.
67 Zacarias, seu pai, cheio do Espírito Santo, profetizou, dizendo:
68 Bendito seja o Senhor, Deus de Israel, porque visitou e redimiu o seu povo,
69 e nos suscitou plena e poderosa salvação na casa de Davi, seu servo,
70 como prometera, desde a antiguidade, por boca dos seus santos profetas,
71 para nos libertar dos nossos inimigos e das mãos de todos os que nos odeiam;
72 para usar de misericórdia com os nossos pais e lembrar-se da sua santa aliança
73 e do juramento que fez a Abraão, o nosso pai,
74 de conceder-nos que, livres das mãos de inimigos, o adorássemos sem temor,
75 em santidade e justiça perante ele, todos os nossos dias.
76 Tu, menino, serás chamado profeta do Altíssimo, porque precederás o Senhor, preparando-lhe os caminhos,
77 para dar ao seu povo conhecimento da salvação, no redimi-lo dos seus pecados,
78 graças à entranhável misericórdia de nosso Deus, pela qual nos visitará o sol nascente das alturas,
79 para alumiar os que jazem nas trevas e na sombra da morte, e dirigir os nossos pés pelo caminho da paz.
80 O menino crescia e se fortalecia em espírito. E viveu nos desertos até ao dia em que havia de manifestar-se a Israel.*
1 Naqueles dias, foi publicado um decreto de César Augusto, convocando toda a população do império para recensear-se.
2 Este, o primeiro recenseamento, foi feito quando Quirino era governador da Síria.
3 Todos iam alistar-se, cada um à sua própria cidade.
4 José também subiu da Galileia, da cidade de Nazaré, para a Judeia, à cidade de Davi, chamada Belém, por ser ele da casa e família de Davi,
5 a fim de alistar-se com Maria, sua esposa, que estava grávida.
6 Estando eles ali, aconteceu completarem-se-lhe os dias,
7 e ela deu à luz o seu filho primogênito, enfaixou-o e o deitou numa manjedoura, porque não havia lugar para eles na hospedaria.
8 Havia, naquela mesma região, pastores que viviam nos campos e guardavam o seu rebanho durante as vigílias da noite.
9 E um anjo do Senhor desceu aonde eles estavam, e a glória do Senhor brilhou ao redor deles; e ficaram tomados de grande temor.
10 O anjo, porém, lhes disse: Não temais; eis aqui vos trago boa-nova de grande alegria, que o será para todo o povo:
11 é que hoje vos nasceu, na cidade de Davi, o Salvador, que é Cristo, o Senhor.
12 E isto vos servirá de sinal: encontrareis uma criança envolta em faixas e deitada em manjedoura.
13 E, subitamente, apareceu com o anjo uma multidão da milícia celestial, louvando a Deus e dizendo:
14 Glória a Deus nas maiores alturas, e paz na terra entre os homens, a quem ele quer bem.
15 E, ausentando-se deles os anjos para o céu, diziam os pastores uns aos outros: Vamos até Belém e vejamos os acontecimentos que o Senhor nos deu a conhecer.
16 Foram apressadamente e acharam Maria e José e a criança deitada na manjedoura.
17 E, vendo-o, divulgaram o que lhes tinha sido dito a respeito deste menino.
18 Todos os que ouviram se admiraram das coisas referidas pelos pastores.
19 Maria, porém, guardava todas estas palavras, meditando-as no coração.
20 Voltaram, então, os pastores glorificando e louvando a Deus por tudo o que tinham ouvido e visto, como lhes fora anunciado.
21 Completados oito dias para ser circuncidado o menino, deram-lhe o nome de Jesus, como lhe chamara o anjo, antes de ser concebido.
22 Passados os dias da purificação deles segundo a Lei de Moisés, levaram-no a Jerusalém para o apresentarem ao Senhor,
23 conforme o que está escrito na Lei do Senhor: Todo primogênito ao Senhor será consagrado;
24 e para oferecer um sacrifício, segundo o que está escrito na referida Lei: Um par de rolas ou dois pombinhos.
25 Havia em Jerusalém um homem chamado Simeão; homem este justo e piedoso que esperava a consolação de Israel; e o Espírito Santo estava sobre ele.
26 Revelara-lhe o Espírito Santo que não passaria pela morte antes de ver o Cristo do Senhor.
27 Movido pelo Espírito, foi ao templo; e, quando os pais trouxeram o menino Jesus para fazerem com ele o que a Lei ordenava,
28 Simeão o tomou nos braços e louvou a Deus, dizendo:
29 Agora, Senhor, podes despedir em paz o teu servo, segundo a tua palavra;
30 porque os meus olhos já viram a tua salvação,
31 a qual preparaste diante de todos os povos:
32 luz para revelação aos gentios, e para glória do teu povo de Israel.
33 E estavam o pai e a mãe do menino admirados do que dele se dizia.
34 Simeão os abençoou e disse a Maria, mãe do menino: Eis que este menino está destinado tanto para ruína como para levantamento de muitos em Israel e para ser alvo de contradição
35 (também uma espada traspassará a tua própria alma), para que se manifestem os pensamentos de muitos corações.
36 Havia uma profetisa, chamada Ana, filha de Fanuel, da tribo de Aser, avançada em dias, que vivera com seu marido sete anos desde que se casara
37 e que era viúva de oitenta e quatro anos. Esta não deixava o templo, mas adorava noite e dia em jejuns e orações.
38 E, chegando naquela hora, dava graças a Deus e falava a respeito do menino a todos os que esperavam a redenção de Jerusalém.
39 Cumpridas todas as ordenanças segundo a Lei do Senhor, voltaram para a Galileia, para a sua cidade de Nazaré.
40 Crescia o menino e se fortalecia, enchendo-se de sabedoria; e a graça de Deus estava sobre ele.
41 Ora, anualmente iam seus pais a Jerusalém, para a Festa da Páscoa.
42 Quando ele atingiu os doze anos, subiram a Jerusalém, segundo o costume da festa.
43 Terminados os dias da festa, ao regressarem, permaneceu o menino Jesus em Jerusalém, sem que seus pais o soubessem.
44 Pensando, porém, estar ele entre os companheiros de viagem, foram caminho de um dia e, então, passaram a procurá-lo entre os parentes e os conhecidos;
45 e, não o tendo encontrado, voltaram a Jerusalém à sua procura.
46 Três dias depois, o acharam no templo, assentado no meio dos doutores, ouvindo-os e interrogando-os.
47 E todos os que o ouviam muito se admiravam da sua inteligência e das suas respostas.
48 Logo que seus pais o viram, ficaram maravilhados; e sua mãe lhe disse: Filho, por que fizeste assim conosco? Teu pai e eu, aflitos, estamos à tua procura.
49 Ele lhes respondeu: Por que me procuráveis? Não sabíeis que me cumpria estar na casa de meu Pai?
50 Não compreenderam, porém, as palavras que lhes dissera.
51 E desceu com eles para Nazaré; e era-lhes submisso. Sua mãe, porém, guardava todas estas coisas no coração.
52 E crescia Jesus em sabedoria, estatura e graça, diante de Deus e dos homens.*
1 No décimo quinto ano do reinado de Tibério César, sendo Pôncio Pilatos governador da Judeia, Herodes, tetrarca da Galileia, seu irmão Filipe, tetrarca da região da Itureia e Traconites, e Lisânias, tetrarca de Abilene,
2 sendo sumos sacerdotes Anás e Caifás, veio a palavra de Deus a João, filho de Zacarias, no deserto.
3 Ele percorreu toda a circunvizinhança do Jordão, pregando batismo de arrependimento para remissão de pecados,
4 conforme está escrito no livro das palavras do profeta Isaías: Voz do que clama no deserto: Preparai o caminho do Senhor, endireitai as suas veredas.
5 Todo vale será aterrado, e nivelados todos os montes e outeiros; os caminhos tortuosos serão retificados, e os escabrosos, aplanados;
6 e toda carne verá a salvação de Deus.
7 Dizia ele, pois, às multidões que saíam para serem batizadas: Raça de víboras, quem vos induziu a fugir da ira vindoura?
8 Produzi, pois, frutos dignos de arrependimento e não comeceis a dizer entre vós mesmos: Temos por pai a Abraão; porque eu vos afirmo que destas pedras Deus pode suscitar filhos a Abraão.
9 E também já está posto o machado à raiz das árvores; toda árvore, pois, que não produz bom fruto é cortada e lançada ao fogo.
10 Então, as multidões o interrogavam, dizendo: Que havemos, pois, de fazer?
11 Respondeu-lhes: Quem tiver duas túnicas, reparta com quem não tem; e quem tiver comida, faça o mesmo.
12 Foram também publicanos para serem batizados e perguntaram-lhe: Mestre, que havemos de fazer?
13 Respondeu-lhes: Não cobreis mais do que o estipulado.
14 Também soldados lhe perguntaram: E nós, que faremos? E ele lhes disse: A ninguém maltrateis, não deis denúncia falsa e contentai-vos com o vosso soldo.
15 Estando o povo na expectativa, e discorrendo todos no seu íntimo a respeito de João, se não seria ele, porventura, o próprio Cristo,
16 disse João a todos: Eu, na verdade, vos batizo com água, mas vem o que é mais poderoso do que eu, do qual não sou digno de desatar-lhe as correias das sandálias; ele vos batizará com o Espírito Santo e com fogo.
17 A sua pá, ele a tem na mão, para limpar completamente a sua eira e recolher o trigo no seu celeiro; porém queimará a palha em fogo inextinguível.
18 Assim, pois, com muitas outras exortações anunciava o evangelho ao povo;
19 mas Herodes, o tetrarca, sendo repreendido por ele, por causa de Herodias, mulher de seu irmão, e por todas as maldades que o mesmo Herodes havia feito,
20 acrescentou ainda sobre todas a de lançar João no cárcere.
21 E aconteceu que, ao ser todo o povo batizado, também o foi Jesus; e, estando ele a orar, o céu se abriu,
22 e o Espírito Santo desceu sobre ele em forma corpórea como pomba; e ouviu-se uma voz do céu: Tu és o meu Filho amado, em ti me comprazo.
23 Ora, tinha Jesus cerca de trinta anos ao começar o seu ministério. Era, como se cuidava, filho de José, filho de Eli;
24 Eli, filho de Matate, Matate, filho de Levi, Levi, filho de Melqui, este, filho de Janai, filho de José;
25 José, filho de Matatias, Matatias, filho de Amós, Amós, filho de Naum, este, filho de Esli, filho de Nagai;
26 Nagai, filho de Maate, Maate, filho de Matatias, Matatias, filho de Semei, este, filho de José, filho de Jodá;
27 Jodá, filho de Joanã, Joanã, filho de Resa, Resa, filho de Zorobabel, este, de Salatiel, filho de Neri;
28 Neri, filho de Melqui, Melqui, filho de Adi, Adi, filho de Cosã, este, de Elmadã, filho de Er;
29 Er, filho de Josué, Josué, filho de Eliézer, Eliézer, filho de Jorim, este, de Matate, filho de Levi;
30 Levi, filho de Simeão, Simeão, filho de Judá, Judá, filho de José, este, filho de Jonã, filho de Eliaquim;
31 Eliaquim, filho de Meleá, Meleá, filho de Mená, Mená, filho de Matatá, este, filho de Natã, filho de Davi;
32 Davi, filho de Jessé, Jessé, filho de Obede, Obede, filho de Boaz, este, filho de Salá, filho de Naassom;
33 Naassom, filho de Aminadabe, Aminadabe, filho de Admim, Admim, filho de Arni, Arni, filho de Esrom, este, filho de Perez, filho de Judá;
34 Judá, filho de Jacó, Jacó, filho de Isaque, Isaque, filho de Abraão, este, filho de Tera, filho de Naor;
35 Naor, filho de Serugue, Serugue, filho de Ragaú, Ragaú, filho de Faleque, este, filho de Éber, filho de Salá;
36 Salá, filho de Cainã, Cainã, filho de Arfaxade, Arfaxade, filho de Sem, este, filho de Noé, filho de Lameque;
37 Lameque, filho de Metusalém, Metusalém, filho de Enoque, Enoque, filho de Jarede, este, filho de Maalalel, filho de Cainã;
38 Cainã, filho de Enos, Enos, filho de Sete, e este, filho de Adão, filho de Deus.*
1 Jesus, cheio do Espírito Santo, voltou do Jordão e foi guiado pelo mesmo Espírito, no deserto,
2 durante quarenta dias, sendo tentado pelo diabo. Nada comeu naqueles dias, ao fim dos quais teve fome.
3 Disse-lhe, então, o diabo: Se és o Filho de Deus, manda que esta pedra se transforme em pão.
4 Mas Jesus lhe respondeu: Está escrito: Não só de pão viverá o homem.
5 E, elevando-o, mostrou-lhe, num momento, todos os reinos do mundo.
6 Disse-lhe o diabo: Dar-te-ei toda esta autoridade e a glória destes reinos, porque ela me foi entregue, e a dou a quem eu quiser.
7 Portanto, se prostrado me adorares, toda será tua.
8 Mas Jesus lhe respondeu: Está escrito: Ao Senhor, teu Deus, adorarás e só a ele darás culto.
9 Então, o levou a Jerusalém, e o colocou sobre o pináculo do templo, e disse: Se és o Filho de Deus, atira-te daqui abaixo;
10 porque está escrito: Aos seus anjos ordenará a teu respeito que te guardem;
11 e: Eles te susterão nas suas mãos, para não tropeçares nalguma pedra.
12 Respondeu-lhe Jesus: Dito está: Não tentarás o Senhor, teu Deus.
13 Passadas que foram as tentações de toda sorte, apartou-se dele o diabo, até momento oportuno.
14 Então, Jesus, no poder do Espírito, regressou para a Galileia, e a sua fama correu por toda a circunvizinhança.
15 E ensinava nas sinagogas, sendo glorificado por todos.
16 Indo para Nazaré, onde fora criado, entrou, num sábado, na sinagoga, segundo o seu costume, e levantou-se para ler.
17 Então, lhe deram o livro do profeta Isaías, e, abrindo o livro, achou o lugar onde estava escrito:
18 O Espírito do Senhor está sobre mim, pelo que me ungiu para evangelizar os pobres; enviou-me para proclamar libertação aos cativos e restauração da vista aos cegos, para pôr em liberdade os oprimidos,
19 e apregoar o ano aceitável do Senhor.
20 Tendo fechado o livro, devolveu-o ao assistente e sentou-se; e todos na sinagoga tinham os olhos fitos nele.
21 Então, passou Jesus a dizer-lhes: Hoje, se cumpriu a Escritura que acabais de ouvir.
22 Todos lhe davam testemunho, e se maravilhavam das palavras de graça que lhe saíam dos lábios, e perguntavam: Não é este o filho de José?
23 Disse-lhes Jesus: Sem dúvida, citar-me-eis este provérbio: Médico, cura-te a ti mesmo; tudo o que ouvimos ter-se dado em Cafarnaum, faze-o também aqui na tua terra.
24 E prosseguiu: De fato, vos afirmo que nenhum profeta é bem-recebido na sua própria terra.
25 Na verdade vos digo que muitas viúvas havia em Israel no tempo de Elias, quando o céu se fechou por três anos e seis meses, reinando grande fome em toda a terra;
26 e a nenhuma delas foi Elias enviado, senão a uma viúva de Sarepta de Sidom.
27 Havia também muitos leprosos em Israel nos dias do profeta Eliseu, e nenhum deles foi purificado, senão Naamã, o siro.
28 Todos na sinagoga, ouvindo estas coisas, se encheram de ira.
29 E, levantando-se, expulsaram-no da cidade e o levaram até ao cimo do monte sobre o qual estava edificada, para, de lá, o precipitarem abaixo.
30 Jesus, porém, passando por entre eles, retirou-se.
31 E desceu a Cafarnaum, cidade da Galileia, e os ensinava no sábado.
32 E muito se maravilhavam da sua doutrina, porque a sua palavra era com autoridade.
33 Achava-se na sinagoga um homem possesso de um espírito de demônio imundo, e bradou em alta voz:
34 Ah! Que temos nós contigo, Jesus Nazareno? Vieste para perder-nos? Bem sei quem és: o Santo de Deus!
35 Mas Jesus o repreendeu, dizendo: Cala-te e sai deste homem. O demônio, depois de o ter lançado por terra no meio de todos, saiu dele sem lhe fazer mal.
36 Todos ficaram grandemente admirados e comentavam entre si, dizendo: Que palavra é esta, pois, com autoridade e poder, ordena aos espíritos imundos, e eles saem?
37 E a sua fama corria por todos os lugares da circunvizinhança.
38 Deixando ele a sinagoga, foi para a casa de Simão. Ora, a sogra de Simão achava-se enferma, com febre muito alta; e rogaram-lhe por ela.
39 Inclinando-se ele para ela, repreendeu a febre, e esta a deixou; e logo se levantou, passando a servi-los.
40 Ao pôr do sol, todos os que tinham enfermos de diferentes moléstias lhos traziam; e ele os curava, impondo as mãos sobre cada um.
41 Também de muitos saíam demônios, gritando e dizendo: Tu és o Filho de Deus! Ele, porém, os repreendia para que não falassem, pois sabiam ser ele o Cristo.
42 Sendo dia, saiu e foi para um lugar deserto; as multidões o procuravam, e foram até junto dele, e instavam para que não os deixasse.
43 Ele, porém, lhes disse: É necessário que eu anuncie o evangelho do reino de Deus também às outras cidades, pois para isso é que fui enviado.
44 E pregava nas sinagogas da Judeia.*
1 Aconteceu que, ao apertá-lo a multidão para ouvir a palavra de Deus, estava ele junto ao lago de Genesaré;
2 e viu dois barcos junto à praia do lago; mas os pescadores, havendo desembarcado, lavavam as redes.
3 Entrando em um dos barcos, que era o de Simão, pediu-lhe que o afastasse um pouco da praia; e, assentando-se, ensinava do barco as multidões.
4 Quando acabou de falar, disse a Simão: Faze-te ao largo, e lançai as vossas redes para pescar.
5 Respondeu-lhe Simão: Mestre, havendo trabalhado toda a noite, nada apanhamos, mas sob a tua palavra lançarei as redes.
6 Isto fazendo, apanharam grande quantidade de peixes; e rompiam-se-lhes as redes.
7 Então, fizeram sinais aos companheiros do outro barco, para que fossem ajudá-los. E foram e encheram ambos os barcos, a ponto de quase irem a pique.
8 Vendo isto, Simão Pedro prostrou-se aos pés de Jesus, dizendo: Senhor, retira-te de mim, porque sou pecador.
9 Pois, à vista da pesca que fizeram, a admiração se apoderou dele e de todos os seus companheiros,
10 bem como de Tiago e João, filhos de Zebedeu, que eram seus sócios. Disse Jesus a Simão: Não temas; doravante serás pescador de homens.
11 E, arrastando eles os barcos sobre a praia, deixando tudo, o seguiram.
12 Aconteceu que, estando ele numa das cidades, veio à sua presença um homem coberto de lepra; ao ver a Jesus, prostrando-se com o rosto em terra, suplicou-lhe: Senhor, se quiseres, podes purificar-me.
13 E ele, estendendo a mão, tocou-lhe, dizendo: Quero, fica limpo! E, no mesmo instante, lhe desapareceu a lepra.
14 Ordenou-lhe Jesus que a ninguém o dissesse, mas vai, disse, mostra-te ao sacerdote e oferece, pela tua purificação, o sacrifício que Moisés determinou, para servir de testemunho ao povo.
15 Porém o que se dizia a seu respeito cada vez mais se divulgava, e grandes multidões afluíam para o ouvirem e serem curadas de suas enfermidades.
16 Ele, porém, se retirava para lugares solitários e orava.
17 Ora, aconteceu que, num daqueles dias, estava ele ensinando, e achavam-se ali assentados fariseus e mestres da Lei, vindos de todas as aldeias da Galileia, da Judeia e de Jerusalém. E o poder do Senhor estava com ele para curar.
18 Vieram, então, uns homens trazendo em um leito um paralítico; e procuravam introduzi-lo e pô-lo diante de Jesus.
19 E, não achando por onde introduzi-lo por causa da multidão, subindo ao eirado, o desceram no leito, por entre os ladrilhos, para o meio, diante de Jesus.
20 Vendo-lhes a fé, Jesus disse ao paralítico: Homem, estão perdoados os teus pecados.
21 E os escribas e fariseus arrazoavam, dizendo: Quem é este que diz blasfêmias? Quem pode perdoar pecados, senão Deus?
22 Jesus, porém, conhecendo-lhes os pensamentos, disse-lhes: Que arrazoais em vosso coração?
23 Qual é mais fácil, dizer: Estão perdoados os teus pecados ou: Levanta-te e anda?
24 Mas, para que saibais que o Filho do Homem tem sobre a terra autoridade para perdoar pecados — disse ao paralítico: Eu te ordeno: Levanta-te, toma o teu leito e vai para casa.
25 Imediatamente, se levantou diante deles e, tomando o leito em que permanecera deitado, voltou para casa, glorificando a Deus.
26 Todos ficaram atônitos, davam glória a Deus e, possuídos de temor, diziam: Hoje, vimos prodígios.
27 Passadas estas coisas, saindo, viu um publicano, chamado Levi, assentado na coletoria, e disse-lhe: Segue-me!
28 Ele se levantou e, deixando tudo, o seguiu.
29 Então, lhe ofereceu Levi um grande banquete em sua casa; e numerosos publicanos e outros estavam com eles à mesa.
30 Os fariseus e seus escribas murmuravam contra os discípulos de Jesus, perguntando: Por que comeis e bebeis com os publicanos e pecadores?
31 Respondeu-lhes Jesus: Os sãos não precisam de médico, e sim os doentes.
32 Não vim chamar justos, e sim pecadores, ao arrependimento.
33 Disseram-lhe eles: Os discípulos de João e bem assim os dos fariseus frequentemente jejuam e fazem orações; os teus, entretanto, comem e bebem.
34 Jesus, porém, lhes disse: Podeis fazer jejuar os convidados para o casamento, enquanto está com eles o noivo?
35 Dias virão, contudo, em que lhes será tirado o noivo; naqueles dias, sim, jejuarão.
36 Também lhes disse uma parábola: Ninguém tira um pedaço de veste nova e o põe em veste velha; pois rasgará a nova, e o remendo da nova não se ajustará à velha.
37 E ninguém põe vinho novo em odres velhos, pois o vinho novo romperá os odres; entornar-se-á o vinho, e os odres se estragarão.
38 Pelo contrário, vinho novo deve ser posto em odres novos [e ambos se conservam].
39 E ninguém, tendo bebido o vinho velho, prefere o novo; porque diz: O velho é excelente.*
1 Aconteceu que, num sábado, passando Jesus pelas searas, os seus discípulos colhiam e comiam espigas, debulhando-as com as mãos.
2 E alguns dos fariseus lhes disseram: Por que fazeis o que não é lícito aos sábados?
3 Respondeu-lhes Jesus: Nem ao menos tendes lido o que fez Davi, quando teve fome, ele e seus companheiros?
4 Como entrou na casa de Deus, tomou, e comeu os pães da proposição, e os deu aos que com ele estavam, pães que não lhes era lícito comer, mas exclusivamente aos sacerdotes?
5 E acrescentou-lhes: O Filho do Homem é senhor do sábado.
6 Sucedeu que, em outro sábado, entrou ele na sinagoga e ensinava. Ora, achava-se ali um homem cuja mão direita estava ressequida.
7 Os escribas e os fariseus observavam-no, procurando ver se ele faria uma cura no sábado, a fim de acharem de que o acusar.
8 Mas ele, conhecendo-lhes os pensamentos, disse ao homem da mão ressequida: Levanta-te e vem para o meio; e ele, levantando-se, permaneceu de pé.
9 Então, disse Jesus a eles: Que vos parece? É lícito, no sábado, fazer o bem ou o mal? Salvar a vida ou deixá-la perecer?
10 E, fitando todos ao redor, disse ao homem: Estende a mão. Ele assim o fez, e a mão lhe foi restaurada.
11 Mas eles se encheram de furor e discutiam entre si quanto ao que fariam a Jesus.
12 Naqueles dias, retirou-se para o monte, a fim de orar, e passou a noite orando a Deus.
13 E, quando amanheceu, chamou a si os seus discípulos e escolheu doze dentre eles, aos quais deu também o nome de apóstolos:
14 Simão, a quem acrescentou o nome de Pedro, e André, seu irmão; Tiago e João; Filipe e Bartolomeu;
15 Mateus e Tomé; Tiago, filho de Alfeu, e Simão, chamado Zelote;
16 Judas, filho de Tiago, e Judas Iscariotes, que se tornou traidor.
17 E, descendo com eles, parou numa planura onde se encontravam muitos discípulos seus e grande multidão do povo, de toda a Judeia, de Jerusalém e do litoral de Tiro e de Sidom,
18 que vieram para o ouvirem e serem curados de suas enfermidades; também os atormentados por espíritos imundos eram curados.
19 E todos da multidão procuravam tocá-lo, porque dele saía poder; e curava todos.
20 Então, olhando ele para os seus discípulos, disse-lhes: Bem-aventurados vós, os pobres, porque vosso é o reino de Deus.
21 Bem-aventurados vós, os que agora tendes fome, porque sereis fartos. Bem-aventurados vós, os que agora chorais, porque haveis de rir.
22 Bem-aventurados sois quando os homens vos odiarem e quando vos expulsarem da sua companhia, vos injuriarem e rejeitarem o vosso nome como indigno, por causa do Filho do Homem.
23 Regozijai-vos naquele dia e exultai, porque grande é o vosso galardão no céu; pois dessa forma procederam seus pais com os profetas.
24 Mas ai de vós, os ricos! Porque tendes a vossa consolação.
25 Ai de vós, os que estais agora fartos! Porque vireis a ter fome. Ai de vós, os que agora rides! Porque haveis de lamentar e chorar.
26 Ai de vós, quando todos vos louvarem! Porque assim procederam seus pais com os falsos profetas.
27 Digo-vos, porém, a vós outros que me ouvis: amai os vossos inimigos, fazei o bem aos que vos odeiam;
28 bendizei aos que vos maldizem, orai pelos que vos caluniam.
29 Ao que te bate numa face, oferece-lhe também a outra; e, ao que tirar a tua capa, deixa-o levar também a túnica;
30 dá a todo o que te pede; e, se alguém levar o que é teu, não entres em demanda.
31 Como quereis que os homens vos façam, assim fazei-o vós também a eles.
32 Se amais os que vos amam, qual é a vossa recompensa? Porque até os pecadores amam aos que os amam.
33 Se fizerdes o bem aos que vos fazem o bem, qual é a vossa recompensa? Até os pecadores fazem isso.
34 E, se emprestais àqueles de quem esperais receber, qual é a vossa recompensa? Também os pecadores emprestam aos pecadores, para receberem outro tanto.
35 Amai, porém, os vossos inimigos, fazei o bem e emprestai, sem esperar nenhuma paga; será grande o vosso galardão, e sereis filhos do Altíssimo. Pois ele é benigno até para com os ingratos e maus.
36 Sede misericordiosos, como também é misericordioso vosso Pai.
37 Não julgueis e não sereis julgados; não condeneis e não sereis condenados; perdoai e sereis perdoados;
38 dai, e dar-se-vos-á; boa medida, recalcada, sacudida, transbordante, generosamente vos darão; porque com a medida com que tiverdes medido vos medirão também.
39 Propôs-lhes também uma parábola: Pode, porventura, um cego guiar a outro cego? Não cairão ambos no barranco?
40 O discípulo não está acima do seu mestre; todo aquele, porém, que for bem-instruído será como o seu mestre.
41 Por que vês tu o argueiro no olho de teu irmão, porém não reparas na trave que está no teu próprio?
42 Como poderás dizer a teu irmão: Deixa, irmão, que eu tire o argueiro do teu olho, não vendo tu mesmo a trave que está no teu? Hipócrita, tira primeiro a trave do teu olho e, então, verás claramente para tirar o argueiro que está no olho de teu irmão.
43 Não há árvore boa que dê mau fruto; nem tampouco árvore má que dê bom fruto.
44 Porquanto cada árvore é conhecida pelo seu próprio fruto. Porque não se colhem figos de espinheiros, nem dos abrolhos se vindimam uvas.
45 O homem bom do bom tesouro do coração tira o bem, e o mau do mau tesouro tira o mal; porque a boca fala do que está cheio o coração.
46 Por que me chamais Senhor, Senhor, e não fazeis o que vos mando?
47 Todo aquele que vem a mim, e ouve as minhas palavras, e as pratica, eu vos mostrarei a quem é semelhante.
48 É semelhante a um homem que, edificando uma casa, cavou, abriu profunda vala e lançou o alicerce sobre a rocha; e, vindo a enchente, arrojou-se o rio contra aquela casa e não a pôde abalar, por ter sido bem-construída.
49 Mas o que ouve e não pratica é semelhante a um homem que edificou uma casa sobre a terra sem alicerces, e, arrojando-se o rio contra ela, logo desabou; e aconteceu que foi grande a ruína daquela casa.*
1 Tendo Jesus concluído todas as suas palavras dirigidas ao povo, entrou em Cafarnaum.
2 E o servo de um centurião, a quem este muito estimava, estava doente, quase à morte.
3 Tendo ouvido falar a respeito de Jesus, enviou-lhe alguns anciãos dos judeus, pedindo-lhe que viesse curar o seu servo.
4 Estes, chegando-se a Jesus, com instância lhe suplicaram, dizendo: Ele é digno de que lhe faças isto;
5 porque é amigo do nosso povo, e ele mesmo nos edificou a sinagoga.
6 Então, Jesus foi com eles. E, já perto da casa, o centurião enviou-lhe amigos para lhe dizer: Senhor, não te incomodes, porque não sou digno de que entres em minha casa.
7 Por isso, eu mesmo não me julguei digno de ir ter contigo; porém manda com uma palavra, e o meu rapaz será curado.
8 Porque também eu sou homem sujeito à autoridade, e tenho soldados às minhas ordens, e digo a este: vai, e ele vai; e a outro: vem, e ele vem; e ao meu servo: faze isto, e ele o faz.
9 Ouvidas estas palavras, admirou-se Jesus dele e, voltando-se para o povo que o acompanhava, disse: Afirmo-vos que nem mesmo em Israel achei fé como esta.
10 E, voltando para casa os que foram enviados, encontraram curado o servo.
11 Em dia subsequente, dirigia-se Jesus a uma cidade chamada Naim, e iam com ele os seus discípulos e numerosa multidão.
12 Como se aproximasse da porta da cidade, eis que saía o enterro do filho único de uma viúva; e grande multidão da cidade ia com ela.
13 Vendo-a, o Senhor se compadeceu dela e lhe disse: Não chores!
14 Chegando-se, tocou o esquife e, parando os que o conduziam, disse: Jovem, eu te mando: levanta-te!
15 Sentou-se o que estivera morto e passou a falar; e Jesus o restituiu a sua mãe.
16 Todos ficaram possuídos de temor e glorificavam a Deus, dizendo: Grande profeta se levantou entre nós; e: Deus visitou o seu povo.
17 Esta notícia a respeito dele divulgou-se por toda a Judeia e por toda a circunvizinhança.
18 Todas estas coisas foram referidas a João pelos seus discípulos. E João, chamando dois deles,
19 enviou-os ao Senhor para perguntar: És tu aquele que estava para vir ou havemos de esperar outro?
20 Quando os homens chegaram junto dele, disseram: João Batista enviou-nos para te perguntar: És tu aquele que estava para vir ou esperaremos outro?
21 Naquela mesma hora, curou Jesus muitos de moléstias, e de flagelos, e de espíritos malignos; e deu vista a muitos cegos.
22 Então, Jesus lhes respondeu: Ide e anunciai a João o que vistes e ouvistes: os cegos veem, os coxos andam, os leprosos são purificados, os surdos ouvem, os mortos são ressuscitados, e aos pobres, anuncia-se-lhes o evangelho.
23 E bem-aventurado é aquele que não achar em mim motivo de tropeço.
24 Tendo-se retirado os mensageiros, passou Jesus a dizer ao povo a respeito de João: Que saístes a ver no deserto? Um caniço agitado pelo vento?
25 Que saístes a ver? Um homem vestido de roupas finas? Os que se vestem bem e vivem no luxo assistem nos palácios dos reis.
26 Sim, que saístes a ver? Um profeta? Sim, eu vos digo, e muito mais que profeta.
27 Este é aquele de quem está escrito: Eis aí envio diante da tua face o meu mensageiro, o qual preparará o teu caminho diante de ti.
28 E eu vos digo: entre os nascidos de mulher, ninguém é maior do que João; mas o menor no reino de Deus é maior do que ele.
29 Todo o povo que o ouviu e até os publicanos reconheceram a justiça de Deus, tendo sido batizados com o batismo de João;
30 mas os fariseus e os intérpretes da Lei rejeitaram, quanto a si mesmos, o desígnio de Deus, não tendo sido batizados por ele.
31 A que, pois, compararei os homens da presente geração, e a que são eles semelhantes?
32 São semelhantes a meninos que, sentados na praça, gritam uns para os outros: Nós vos tocamos flauta, e não dançastes; entoamos lamentações, e não chorastes.
33 Pois veio João Batista, não comendo pão, nem bebendo vinho, e dizeis: Tem demônio!
34 Veio o Filho do Homem, comendo e bebendo, e dizeis: Eis aí um glutão e bebedor de vinho, amigo de publicanos e pecadores!
35 Mas a sabedoria é justificada por todos os seus filhos.
36 Convidou-o um dos fariseus para que fosse jantar com ele. Jesus, entrando na casa do fariseu, tomou lugar à mesa.
37 E eis que uma mulher da cidade, pecadora, sabendo que ele estava à mesa na casa do fariseu, levou um vaso de alabastro com unguento;
38 e, estando por detrás, aos seus pés, chorando, regava-os com suas lágrimas e os enxugava com os próprios cabelos; e beijava-lhe os pés e os ungia com o unguento.
39 Ao ver isto, o fariseu que o convidara disse consigo mesmo: Se este fora profeta, bem saberia quem e qual é a mulher que lhe tocou, porque é pecadora.
40 Dirigiu-se Jesus ao fariseu e lhe disse: Simão, uma coisa tenho a dizer-te. Ele respondeu: Dize-a, Mestre.
41 Certo credor tinha dois devedores: um lhe devia quinhentos denários, e o outro, cinquenta.
42 Não tendo nenhum dos dois com que pagar, perdoou-lhes a ambos. Qual deles, portanto, o amará mais?
43 Respondeu-lhe Simão: Suponho que aquele a quem mais perdoou. Replicou-lhe: Julgaste bem.
44 E, voltando-se para a mulher, disse a Simão: Vês esta mulher? Entrei em tua casa, e não me deste água para os pés; esta, porém, regou os meus pés com lágrimas e os enxugou com os seus cabelos.
45 Não me deste ósculo; ela, entretanto, desde que entrei não cessa de me beijar os pés.
46 Não me ungiste a cabeça com óleo, mas esta, com bálsamo, ungiu os meus pés.
47 Por isso, te digo: perdoados lhe são os seus muitos pecados, porque ela muito amou; mas aquele a quem pouco se perdoa, pouco ama.
48 Então, disse à mulher: Perdoados são os teus pecados.
49 Os que estavam com ele à mesa começaram a dizer entre si: Quem é este que até perdoa pecados?
50 Mas Jesus disse à mulher: A tua fé te salvou; vai-te em paz.*
1 Aconteceu, depois disto, que andava Jesus de cidade em cidade e de aldeia em aldeia, pregando e anunciando o evangelho do reino de Deus, e os doze iam com ele,
2 e também algumas mulheres que haviam sido curadas de espíritos malignos e de enfermidades: Maria, chamada Madalena, da qual saíram sete demônios;
3 e Joana, mulher de Cuza, procurador de Herodes, Suzana e muitas outras, as quais lhe prestavam assistência com os seus bens.
4 Afluindo uma grande multidão e vindo ter com ele gente de todas as cidades, disse Jesus por parábola:
5 Eis que o semeador saiu a semear. E, ao semear, uma parte caiu à beira do caminho; foi pisada, e as aves do céu a comeram.
6 Outra caiu sobre a pedra; e, tendo crescido, secou por falta de umidade.
7 Outra caiu no meio dos espinhos; e estes, ao crescerem com ela, a sufocaram.
8 Outra, afinal, caiu em boa terra; cresceu e produziu a cento por um. Dizendo isto, clamou: Quem tem ouvidos para ouvir, ouça.
9 E os seus discípulos o interrogaram, dizendo: Que parábola é esta?
10 Respondeu-lhes Jesus: A vós outros é dado conhecer os mistérios do reino de Deus; aos demais, fala-se por parábolas, para que, vendo, não vejam; e, ouvindo, não entendam.
11 Este é o sentido da parábola: a semente é a palavra de Deus.
12 A que caiu à beira do caminho são os que a ouviram; vem, a seguir, o diabo e arrebata-lhes do coração a palavra, para não suceder que, crendo, sejam salvos.
13 A que caiu sobre a pedra são os que, ouvindo a palavra, a recebem com alegria; estes não têm raiz, creem apenas por algum tempo e, na hora da provação, se desviam.
14 A que caiu entre espinhos são os que ouviram e, no decorrer dos dias, foram sufocados com os cuidados, riquezas e deleites da vida; os seus frutos não chegam a amadurecer.
15 A que caiu na boa terra são os que, tendo ouvido de bom e reto coração, retêm a palavra; estes frutificam com perseverança.
16 Ninguém, depois de acender uma candeia, a cobre com um vaso ou a põe debaixo de uma cama; pelo contrário, coloca-a sobre um velador, a fim de que os que entram vejam a luz.
17 Nada há oculto, que não haja de manifestar-se, nem escondido, que não venha a ser conhecido e revelado.
18 Vede, pois, como ouvis; porque ao que tiver, se lhe dará; e ao que não tiver, até aquilo que julga ter lhe será tirado.
19 Vieram ter com ele sua mãe e seus irmãos e não podiam aproximar-se por causa da concorrência de povo.
20 E lhe comunicaram: Tua mãe e teus irmãos estão lá fora e querem ver-te.
21 Ele, porém, lhes respondeu: Minha mãe e meus irmãos são aqueles que ouvem a palavra de Deus e a praticam.
22 Aconteceu que, num daqueles dias, entrou ele num barco em companhia dos seus discípulos e disse-lhes: Passemos para a outra margem do lago; e partiram.
23 Enquanto navegavam, ele adormeceu. E sobreveio uma tempestade de vento no lago, correndo eles o perigo de soçobrar.
24 Chegando-se a ele, despertaram-no dizendo: Mestre, Mestre, estamos perecendo! Despertando-se Jesus, repreendeu o vento e a fúria da água. Tudo cessou, e veio a bonança.
25 Então, lhes disse: Onde está a vossa fé? Eles, possuídos de temor e admiração, diziam uns aos outros: Quem é este que até aos ventos e às ondas repreende, e lhe obedecem?
26 Então, rumaram para a terra dos gerasenos, fronteira da Galileia.
27 Logo ao desembarcar, veio da cidade ao seu encontro um homem possesso de demônios que, havia muito, não se vestia, nem habitava em casa alguma, porém vivia nos sepulcros.
28 E, quando viu a Jesus, prostrou-se diante dele, exclamando e dizendo em alta voz: Que tenho eu contigo, Jesus, Filho do Deus Altíssimo? Rogo-te que não me atormentes.
29 Porque Jesus ordenara ao espírito imundo que saísse do homem, pois muitas vezes se apoderara dele. E, embora procurassem conservá-lo preso com cadeias e grilhões, tudo despedaçava e era impelido pelo demônio para o deserto.
30 Perguntou-lhe Jesus: Qual é o teu nome? Respondeu ele: Legião, porque tinham entrado nele muitos demônios.
31 Rogavam-lhe que não os mandasse sair para o abismo.
32 Ora, andava ali, pastando no monte, uma grande manada de porcos; rogaram-lhe que lhes permitisse entrar naqueles porcos. E Jesus o permitiu.
33 Tendo os demônios saído do homem, entraram nos porcos, e a manada precipitou-se despenhadeiro abaixo, para dentro do lago, e se afogou.
34 Os porqueiros, vendo o que acontecera, fugiram e foram anunciá-lo na cidade e pelos campos.
35 Então, saiu o povo para ver o que se passara, e foram ter com Jesus. De fato, acharam o homem de quem saíram os demônios, vestido, em perfeito juízo, assentado aos pés de Jesus; e ficaram dominados de terror.
36 E algumas pessoas que tinham presenciado os fatos contaram-lhes também como fora salvo o endemoninhado.
37 Todo o povo da circunvizinhança dos gerasenos rogou-lhe que se retirasse deles, pois estavam possuídos de grande medo. E Jesus, tomando de novo o barco, voltou.
38 O homem de quem tinham saído os demônios rogou-lhe que o deixasse estar com ele; Jesus, porém, o despediu, dizendo:
39 Volta para casa e conta aos teus tudo o que Deus fez por ti. Então, foi ele anunciando por toda a cidade todas as coisas que Jesus lhe tinha feito.
40 Ao regressar Jesus, a multidão o recebeu com alegria, porque todos o estavam esperando.
41 Eis que veio um homem chamado Jairo, que era chefe da sinagoga, e, prostrando-se aos pés de Jesus, lhe suplicou que chegasse até a sua casa.
42 Pois tinha uma filha única de uns doze anos, que estava à morte. Enquanto ele ia, as multidões o apertavam.
43 Certa mulher que, havia doze anos, vinha sofrendo de uma hemorragia, e a quem ninguém tinha podido curar [e que gastara com os médicos todos os seus haveres],
44 veio por trás dele e lhe tocou na orla da veste, e logo se lhe estancou a hemorragia.
45 Mas Jesus disse: Quem me tocou? Como todos negassem, Pedro [com seus companheiros] disse: Mestre, as multidões te apertam e te oprimem [e dizes: Quem me tocou?].
46 Contudo, Jesus insistiu: Alguém me tocou, porque senti que de mim saiu poder.
47 Vendo a mulher que não podia ocultar-se, aproximou-se trêmula e, prostrando-se diante dele, declarou, à vista de todo o povo, a causa por que lhe havia tocado e como imediatamente fora curada.
48 Então, lhe disse: Filha, a tua fé te salvou; vai-te em paz.
49 Falava ele ainda, quando veio uma pessoa da casa do chefe da sinagoga, dizendo: Tua filha já está morta, não incomodes mais o Mestre.
50 Mas Jesus, ouvindo isto, lhe disse: Não temas, crê somente, e ela será salva.
51 Tendo chegado à casa, a ninguém permitiu que entrasse com ele, senão Pedro, João, Tiago e bem assim o pai e a mãe da menina.
52 E todos choravam e a pranteavam. Mas ele disse: Não choreis; ela não está morta, mas dorme.
53 E riam-se dele, porque sabiam que ela estava morta.
54 Entretanto, ele, tomando-a pela mão, disse-lhe, em voz alta: Menina, levanta-te!
55 Voltou-lhe o espírito, ela imediatamente se levantou, e ele mandou que lhe dessem de comer.
56 Seus pais ficaram maravilhados, mas ele lhes advertiu que a ninguém contassem o que havia acontecido.*
1 Tendo Jesus convocado os doze, deu-lhes poder e autoridade sobre todos os demônios, e para efetuarem curas.
2 Também os enviou a pregar o reino de Deus e a curar os enfermos.
3 E disse-lhes: Nada leveis para o caminho: nem bordão, nem alforje, nem pão, nem dinheiro; nem deveis ter duas túnicas.
4 Na casa em que entrardes, ali permanecei e dali saireis.
5 E onde quer que não vos receberem, ao sairdes daquela cidade, sacudi o pó dos vossos pés em testemunho contra eles.
6 Então, saindo, percorriam todas as aldeias, anunciando o evangelho e efetuando curas por toda parte.
7 Ora, o tetrarca Herodes soube de tudo o que se passava e ficou perplexo, porque alguns diziam: João ressuscitou dentre os mortos;
8 outros: Elias apareceu; e outros: Ressurgiu um dos antigos profetas.
9 Herodes, porém, disse: Eu mandei decapitar a João; quem é, pois, este a respeito do qual tenho ouvido tais coisas? E se esforçava por vê-lo.
10 Ao regressarem, os apóstolos relataram a Jesus tudo o que tinham feito. E, levando-os consigo, retirou-se à parte para uma cidade chamada Betsaida.
11 Mas as multidões, ao saberem, seguiram-no. Acolhendo-as, falava-lhes a respeito do reino de Deus e socorria os que tinham necessidade de cura.
12 Mas o dia começava a declinar. Então, se aproximaram os doze e lhe disseram: Despede a multidão, para que, indo às aldeias e campos circunvizinhos, se hospedem e achem alimento; pois estamos aqui em lugar deserto.
13 Ele, porém, lhes disse: Dai-lhes vós mesmos de comer. Responderam eles: Não temos mais que cinco pães e dois peixes, salvo se nós mesmos formos comprar comida para todo este povo.
14 Porque estavam ali cerca de cinco mil homens. Então, disse aos seus discípulos: Fazei-os sentar-se em grupos de cinquenta.
15 Eles atenderam, acomodando a todos.
16 E, tomando os cinco pães e os dois peixes, erguendo os olhos para o céu, os abençoou, partiu e deu aos discípulos para que os distribuíssem entre o povo.
17 Todos comeram e se fartaram; e dos pedaços que ainda sobejaram foram recolhidos doze cestos.
18 Estando ele orando à parte, achavam-se presentes os discípulos, a quem perguntou: Quem dizem as multidões que sou eu?
19 Responderam eles: João Batista, mas outros, Elias; e ainda outros dizem que ressurgiu um dos antigos profetas.
20 Mas vós, perguntou ele, quem dizeis que eu sou? Então, falou Pedro e disse: És o Cristo de Deus.
21 Ele, porém, advertindo-os, mandou que a ninguém declarassem tal coisa,
22 dizendo: É necessário que o Filho do Homem sofra muitas coisas, seja rejeitado pelos anciãos, pelos principais sacerdotes e pelos escribas; seja morto e, no terceiro dia, ressuscite.
23 Dizia a todos: Se alguém quer vir após mim, a si mesmo se negue, dia a dia tome a sua cruz e siga-me.
24 Pois quem quiser salvar a sua vida perdê-la-á; quem perder a vida por minha causa, esse a salvará.
25 Que aproveita ao homem ganhar o mundo inteiro, se vier a perder-se ou a causar dano a si mesmo?
26 Porque qualquer que de mim e das minhas palavras se envergonhar, dele se envergonhará o Filho do Homem, quando vier na sua glória e na do Pai e dos santos anjos.
27 Verdadeiramente, vos digo: alguns há dos que aqui se encontram que, de maneira nenhuma, passarão pela morte até que vejam o reino de Deus.
28 Cerca de oito dias depois de proferidas estas palavras, tomando consigo a Pedro, João e Tiago, subiu ao monte com o propósito de orar.
29 E aconteceu que, enquanto ele orava, a aparência do seu rosto se transfigurou e suas vestes resplandeceram de brancura.
30 Eis que dois varões falavam com ele: Moisés e Elias,
31 os quais apareceram em glória e falavam da sua partida, que ele estava para cumprir em Jerusalém.
32 Pedro e seus companheiros achavam-se premidos de sono; mas, conservando-se acordados, viram a sua glória e os dois varões que com ele estavam.
33 Ao se retirarem estes de Jesus, disse-lhe Pedro: Mestre, bom é estarmos aqui; então, façamos três tendas: uma será tua, outra, de Moisés, e outra, de Elias, não sabendo, porém, o que dizia.
34 Enquanto assim falava, veio uma nuvem e os envolveu; e encheram-se de medo ao entrarem na nuvem.
35 E dela veio uma voz, dizendo: Este é o meu Filho, o meu eleito; a ele ouvi.
36 Depois daquela voz, achou-se Jesus sozinho. Eles calaram-se e, naqueles dias, a ninguém contaram coisa alguma do que tinham visto.
37 No dia seguinte, ao descerem eles do monte, veio ao encontro de Jesus grande multidão.
38 E eis que, dentre a multidão, surgiu um homem, dizendo em alta voz: Mestre, suplico-te que vejas meu filho, porque é o único;
39 um espírito se apodera dele, e, de repente, o menino grita, e o espírito o atira por terra, convulsiona-o até espumar; e dificilmente o deixa, depois de o ter quebrantado.
40 Roguei aos teus discípulos que o expelissem, mas eles não puderam.
41 Respondeu Jesus: Ó geração incrédula e perversa! Até quando estarei convosco e vos sofrerei? Traze o teu filho.
42 Quando se ia aproximando, o demônio o atirou no chão e o convulsionou; mas Jesus repreendeu o espírito imundo, curou o menino e o entregou a seu pai.
43 E todos ficaram maravilhados ante a majestade de Deus. Como todos se maravilhassem de quanto Jesus fazia, disse aos seus discípulos:
44 Fixai nos vossos ouvidos as seguintes palavras: o Filho do Homem está para ser entregue nas mãos dos homens.
45 Eles, porém, não entendiam isto, e foi-lhes encoberto para que o não compreendessem; e temiam interrogá-lo a este respeito.
46 Levantou-se entre eles uma discussão sobre qual deles seria o maior.
47 Mas Jesus, sabendo o que se lhes passava no coração, tomou uma criança, colocou-a junto a si
48 e lhes disse: Quem receber esta criança em meu nome a mim me recebe; e quem receber a mim recebe aquele que me enviou; porque aquele que entre vós for o menor de todos, esse é que é grande.
49 Falou João e disse: Mestre, vimos certo homem que, em teu nome, expelia demônios e lho proibimos, porque não segue conosco.
50 Mas Jesus lhe disse: Não proibais; pois quem não é contra vós outros é por vós.
51 E aconteceu que, ao se completarem os dias em que devia ele ser assunto ao céu, manifestou, no semblante, a intrépida resolução de ir para Jerusalém
52 e enviou mensageiros que o antecedessem. Indo eles, entraram numa aldeia de samaritanos para lhe preparar pousada.
53 Mas não o receberam, porque o aspecto dele era de quem, decisivamente, ia para Jerusalém.
54 Vendo isto, os discípulos Tiago e João perguntaram: Senhor, queres que mandemos descer fogo do céu para os consumir?
55 Jesus, porém, voltando-se os repreendeu [e disse: Vós não sabeis de que espírito sois].
56 [Pois o Filho do Homem não veio para destruir as almas dos homens, mas para salvá-las.] E seguiram para outra aldeia.
57 Indo eles caminho fora, alguém lhe disse: Seguir-te-ei para onde quer que fores.
58 Mas Jesus lhe respondeu: As raposas têm seus covis, e as aves do céu, ninhos; mas o Filho do Homem não tem onde reclinar a cabeça.
59 A outro disse Jesus: Segue-me! Ele, porém, respondeu: Permite-me ir primeiro sepultar meu pai.
60 Mas Jesus insistiu: Deixa aos mortos o sepultar os seus próprios mortos. Tu, porém, vai e prega o reino de Deus.
61 Outro lhe disse: Seguir-te-ei, Senhor; mas deixa-me primeiro despedir-me dos de casa.
62 Mas Jesus lhe replicou: Ninguém que, tendo posto a mão no arado, olha para trás é apto para o reino de Deus.*
1 Depois disto, o Senhor designou outros setenta; e os enviou de dois em dois, para que o precedessem em cada cidade e lugar aonde ele estava para ir.
2 E lhes fez a seguinte advertência: A seara é grande, mas os trabalhadores são poucos. Rogai, pois, ao Senhor da seara que mande trabalhadores para a sua seara.
3 Ide! Eis que eu vos envio como cordeiros para o meio de lobos.
4 Não leveis bolsa, nem alforje, nem sandálias; e a ninguém saudeis pelo caminho.
5 Ao entrardes numa casa, dizei antes de tudo: Paz seja nesta casa!
6 Se houver ali um filho da paz, repousará sobre ele a vossa paz; se não houver, ela voltará sobre vós.
7 Permanecei na mesma casa, comendo e bebendo do que eles tiverem; porque digno é o trabalhador do seu salário. Não andeis a mudar de casa em casa.
8 Quando entrardes numa cidade e ali vos receberem, comei do que vos for oferecido.
9 Curai os enfermos que nela houver e anunciai-lhes: A vós outros está próximo o reino de Deus.
10 Quando, porém, entrardes numa cidade e não vos receberem, saí pelas ruas e clamai:
11 Até o pó da vossa cidade, que se nos pegou aos pés, sacudimos contra vós outros. Não obstante, sabei que está próximo o reino de Deus.
12 Digo-vos que, naquele dia, haverá menos rigor para Sodoma do que para aquela cidade.
13 Ai de ti, Corazim! Ai de ti, Betsaida! Porque, se em Tiro e em Sidom, se tivessem operado os milagres que em vós se fizeram, há muito que elas se teriam arrependido, assentadas em pano de saco e cinza.
14 Contudo, no Juízo, haverá menos rigor para Tiro e Sidom do que para vós outras.
15 Tu, Cafarnaum, elevar-te-ás, porventura, até ao céu? Descerás até ao inferno.
16 Quem vos der ouvidos ouve-me a mim; e quem vos rejeitar a mim me rejeita; quem, porém, me rejeitar rejeita aquele que me enviou.
17 Então, regressaram os setenta, possuídos de alegria, dizendo: Senhor, os próprios demônios se nos submetem pelo teu nome!
18 Mas ele lhes disse: Eu via Satanás caindo do céu como um relâmpago.
19 Eis aí vos dei autoridade para pisardes serpentes e escorpiões e sobre todo o poder do inimigo, e nada, absolutamente, vos causará dano.
20 Não obstante, alegrai-vos, não porque os espíritos se vos submetem, e sim porque o vosso nome está arrolado nos céus.
21 Naquela hora, exultou Jesus no Espírito Santo e exclamou: Graças te dou, ó Pai, Senhor do céu e da terra, porque ocultaste estas coisas aos sábios e instruídos e as revelaste aos pequeninos. Sim, ó Pai, porque assim foi do teu agrado.
22 Tudo me foi entregue por meu Pai. Ninguém sabe quem é o Filho, senão o Pai; e também ninguém sabe quem é o Pai, senão o Filho, e aquele a quem o Filho o quiser revelar.
23 E, voltando-se para os seus discípulos, disse-lhes particularmente: Bem-aventurados os olhos que veem as coisas que vós vedes.
24 Pois eu vos afirmo que muitos profetas e reis quiseram ver o que vedes e não viram; e ouvir o que ouvis e não o ouviram.
25 E eis que certo homem, intérprete da Lei, se levantou com o intuito de pôr Jesus à prova e disse-lhe: Mestre, que farei para herdar a vida eterna?
26 Então, Jesus lhe perguntou: Que está escrito na Lei? Como interpretas?
27 A isto ele respondeu: Amarás o Senhor, teu Deus, de todo o teu coração, de toda a tua alma, de todas as tuas forças e de todo o teu entendimento; e: Amarás o teu próximo como a ti mesmo.
28 Então, Jesus lhe disse: Respondeste corretamente; faze isto e viverás.
29 Ele, porém, querendo justificar-se, perguntou a Jesus: Quem é o meu próximo?
30 Jesus prosseguiu, dizendo: Certo homem descia de Jerusalém para Jericó e veio a cair em mãos de salteadores, os quais, depois de tudo lhe roubarem e lhe causarem muitos ferimentos, retiraram-se, deixando-o semimorto.
31 Casualmente, descia um sacerdote por aquele mesmo caminho e, vendo-o, passou de largo.
32 Semelhantemente, um levita descia por aquele lugar e, vendo-o, também passou de largo.
33 Certo samaritano, que seguia o seu caminho, passou-lhe perto e, vendo-o, compadeceu-se dele.
34 E, chegando-se, pensou-lhe os ferimentos, aplicando-lhes óleo e vinho; e, colocando-o sobre o seu próprio animal, levou-o para uma hospedaria e tratou dele.
35 No dia seguinte, tirou dois denários e os entregou ao hospedeiro, dizendo: Cuida deste homem, e, se alguma coisa gastares a mais, eu to indenizarei quando voltar.
36 Qual destes três te parece ter sido o próximo do homem que caiu nas mãos dos salteadores?
37 Respondeu-lhe o intérprete da Lei: O que usou de misericórdia para com ele. Então, lhe disse: Vai e procede tu de igual modo.
38 Indo eles de caminho, entrou Jesus num povoado. E certa mulher, chamada Marta, hospedou-o na sua casa.
39 Tinha ela uma irmã, chamada Maria, e esta quedava-se assentada aos pés do Senhor a ouvir-lhe os ensinamentos.
40 Marta agitava-se de um lado para outro, ocupada em muitos serviços. Então, se aproximou de Jesus e disse: Senhor, não te importas de que minha irmã tenha deixado que eu fique a servir sozinha? Ordena-lhe, pois, que venha ajudar-me.
41 Respondeu-lhe o Senhor: Marta! Marta! Andas inquieta e te preocupas com muitas coisas.
42 Entretanto, pouco é necessário ou mesmo uma só coisa; Maria, pois, escolheu a boa parte, e esta não lhe será tirada.*
1 De uma feita, estava Jesus orando em certo lugar; quando terminou, um dos seus discípulos lhe pediu: Senhor, ensina-nos a orar como também João ensinou aos seus discípulos.
2 Então, ele os ensinou: Quando orardes, dizei: Pai, santificado seja o teu nome; venha o teu reino;
3 o pão nosso cotidiano dá-nos de dia em dia;
4 perdoa-nos os nossos pecados, pois também nós perdoamos a todo o que nos deve; e não nos deixes cair em tentação.
5 Disse-lhes ainda Jesus: Qual dentre vós, tendo um amigo, e este for procurá-lo à meia-noite e lhe disser: Amigo, empresta-me três pães,
6 pois um meu amigo, chegando de viagem, procurou-me, e eu nada tenho que lhe oferecer.
7 E o outro lhe responda lá de dentro, dizendo: Não me importunes; a porta já está fechada, e os meus filhos comigo também já estão deitados. Não posso levantar-me para tos dar;
8 digo-vos que, se não se levantar para dar-lhos por ser seu amigo, todavia, o fará por causa da importunação e lhe dará tudo o de que tiver necessidade.
9 Por isso, vos digo: Pedi, e dar-se-vos-á; buscai, e achareis; batei, e abrir-se-vos-á.
10 Pois todo o que pede recebe; o que busca encontra; e a quem bate, abrir-se-lhe-á.
11 Qual dentre vós é o pai que, se o filho lhe pedir [pão, lhe dará uma pedra? Ou se pedir] um peixe, lhe dará em lugar de peixe uma cobra?
12 Ou, se lhe pedir um ovo lhe dará um escorpião?
13 Ora, se vós, que sois maus, sabeis dar boas dádivas aos vossos filhos, quanto mais o Pai celestial dará o Espírito Santo àqueles que lho pedirem?
14 De outra feita, estava Jesus expelindo um demônio que era mudo. E aconteceu que, ao sair o demônio, o mudo passou a falar; e as multidões se admiravam.
15 Mas alguns dentre eles diziam: Ora, ele expele os demônios pelo poder de Belzebu, o maioral dos demônios.
16 E outros, tentando-o, pediam dele um sinal do céu.
17 E, sabendo ele o que se lhes passava pelo espírito, disse-lhes: Todo reino dividido contra si mesmo ficará deserto, e casa sobre casa cairá.
18 Se também Satanás estiver dividido contra si mesmo, como subsistirá o seu reino? Isto, porque dizeis que eu expulso os demônios por Belzebu.
19 E, se eu expulso os demônios por Belzebu, por quem os expulsam vossos filhos? Por isso, eles mesmos serão os vossos juízes.
20 Se, porém, eu expulso os demônios pelo dedo de Deus, certamente, é chegado o reino de Deus sobre vós.
21 Quando o valente, bem-armado, guarda a sua própria casa, ficam em segurança todos os seus bens.
22 Sobrevindo, porém, um mais valente do que ele, vence-o, tira-lhe a armadura em que confiava e lhe divide os despojos.
23 Quem não é por mim é contra mim; e quem comigo não ajunta espalha.
24 Quando o espírito imundo sai do homem, anda por lugares áridos, procurando repouso; e, não o achando, diz: Voltarei para minha casa, donde saí.
25 E, tendo voltado, a encontra varrida e ornamentada.
26 Então, vai e leva consigo outros sete espíritos, piores do que ele, e, entrando, habitam ali; e o último estado daquele homem se torna pior do que o primeiro.
27 Ora, aconteceu que, ao dizer Jesus estas palavras, uma mulher, que estava entre a multidão, exclamou e disse-lhe: Bem-aventurada aquela que te concebeu, e os seios que te amamentaram!
28 Ele, porém, respondeu: Antes, bem-aventurados são os que ouvem a palavra de Deus e a guardam!
29 Como afluíssem as multidões, passou Jesus a dizer: Esta é geração perversa! Pede sinal; mas nenhum sinal lhe será dado, senão o de Jonas.
30 Porque, assim como Jonas foi sinal para os ninivitas, o Filho do Homem o será para esta geração.
31 A rainha do Sul se levantará, no Juízo, com os homens desta geração e os condenará; porque veio dos confins da terra para ouvir a sabedoria de Salomão. E eis aqui está quem é maior do que Salomão.
32 Ninivitas se levantarão, no Juízo, com esta geração e a condenarão; porque se arrependeram com a pregação de Jonas. E eis aqui está quem é maior do que Jonas.
33 Ninguém, depois de acender uma candeia, a põe em lugar escondido, nem debaixo do alqueire, mas no velador, a fim de que os que entram vejam a luz.
34 São os teus olhos a lâmpada do teu corpo; se os teus olhos forem bons, todo o teu corpo será luminoso; mas, se forem maus, o teu corpo ficará em trevas.
35 Repara, pois, que a luz que há em ti não sejam trevas.
36 Se, portanto, todo o teu corpo for luminoso, sem ter qualquer parte em trevas, será todo resplandecente como a candeia quando te ilumina em plena luz.
37 Ao falar Jesus estas palavras, um fariseu o convidou para ir comer com ele; então, entrando, tomou lugar à mesa.
38 O fariseu, porém, admirou-se ao ver que Jesus não se lavara primeiro, antes de comer.
39 O Senhor, porém, lhe disse: Vós, fariseus, limpais o exterior do copo e do prato; mas o vosso interior está cheio de rapina e perversidade.
40 Insensatos! Quem fez o exterior não é o mesmo que fez o interior?
41 Antes, dai esmola do que tiverdes, e tudo vos será limpo.
42 Mas ai de vós, fariseus! Porque dais o dízimo da hortelã, da arruda e de todas as hortaliças e desprezais a justiça e o amor de Deus; devíeis, porém, fazer estas coisas, sem omitir aquelas.
43 Ai de vós, fariseus! Porque gostais da primeira cadeira nas sinagogas e das saudações nas praças.
44 Ai de vós que sois como as sepulturas invisíveis, sobre as quais os homens passam sem o saber!
45 Então, respondendo um dos intérpretes da Lei, disse a Jesus: Mestre, dizendo estas coisas, também nos ofendes a nós outros!
46 Mas ele respondeu: Ai de vós também, intérpretes da Lei! Porque sobrecarregais os homens com fardos superiores às suas forças, mas vós mesmos nem com um dedo os tocais.
47 Ai de vós! Porque edificais os túmulos dos profetas que vossos pais assassinaram.
48 Assim, sois testemunhas e aprovais com cumplicidade as obras dos vossos pais; porque eles mataram os profetas, e vós lhes edificais os túmulos.
49 Por isso, também disse a sabedoria de Deus: Enviar-lhes-ei profetas e apóstolos, e a alguns deles matarão e a outros perseguirão,
50 para que desta geração se peçam contas do sangue dos profetas, derramado desde a fundação do mundo;
51 desde o sangue de Abel até ao de Zacarias, que foi assassinado entre o altar e a casa de Deus. Sim, eu vos afirmo, contas serão pedidas a esta geração.
52 Ai de vós, intérpretes da Lei! Porque tomastes a chave da ciência; contudo, vós mesmos não entrastes e impedistes os que estavam entrando.
53 Saindo Jesus dali, passaram os escribas e fariseus a argui-lo com veemência, procurando confundi-lo a respeito de muitos assuntos,
54 com o intuito de tirar das suas próprias palavras motivos para o acusar.*
1 Posto que miríades de pessoas se aglomeraram, a ponto de uns aos outros se atropelarem, passou Jesus a dizer, antes de tudo, aos seus discípulos: Acautelai-vos do fermento dos fariseus, que é a hipocrisia.
2 Nada há encoberto que não venha a ser revelado; e oculto que não venha a ser conhecido.
3 Porque tudo o que dissestes às escuras será ouvido em plena luz; e o que dissestes aos ouvidos no interior da casa será proclamado dos eirados.
4 Digo-vos, pois, amigos meus: não temais os que matam o corpo e, depois disso, nada mais podem fazer.
5 Eu, porém, vos mostrarei a quem deveis temer: temei aquele que, depois de matar, tem poder para lançar no inferno. Sim, digo-vos, a esse deveis temer.
6 Não se vendem cinco pardais por dois asses? Entretanto, nenhum deles está em esquecimento diante de Deus.
7 Até os cabelos da vossa cabeça estão todos contados. Não temais! Bem mais valeis do que muitos pardais.
8 Digo-vos ainda: todo aquele que me confessar diante dos homens, também o Filho do Homem o confessará diante dos anjos de Deus;
9 mas o que me negar diante dos homens será negado diante dos anjos de Deus.
10 Todo aquele que proferir uma palavra contra o Filho do Homem, isso lhe será perdoado; mas, para o que blasfemar contra o Espírito Santo, não haverá perdão.
11 Quando vos levarem às sinagogas e perante os governadores e as autoridades, não vos preocupeis quanto ao modo por que respondereis, nem quanto às coisas que tiverdes de falar.
12 Porque o Espírito Santo vos ensinará, naquela mesma hora, as coisas que deveis dizer.
13 Nesse ponto, um homem que estava no meio da multidão lhe falou: Mestre, ordena a meu irmão que reparta comigo a herança.
14 Mas Jesus lhe respondeu: Homem, quem me constituiu juiz ou partidor entre vós?
15 Então, lhes recomendou: Tende cuidado e guardai-vos de toda e qualquer avareza; porque a vida de um homem não consiste na abundância dos bens que ele possui.
16 E lhes proferiu ainda uma parábola, dizendo: O campo de um homem rico produziu com abundância.
17 E arrazoava consigo mesmo, dizendo: Que farei, pois não tenho onde recolher os meus frutos?
18 E disse: Farei isto: destruirei os meus celeiros, reconstruí-los-ei maiores e aí recolherei todo o meu produto e todos os meus bens.
19 Então, direi à minha alma: tens em depósito muitos bens para muitos anos; descansa, come, bebe e regala-te.
20 Mas Deus lhe disse: Louco, esta noite te pedirão a tua alma; e o que tens preparado, para quem será?
21 Assim é o que entesoura para si mesmo e não é rico para com Deus.
22 A seguir, dirigiu-se Jesus a seus discípulos, dizendo: Por isso, eu vos advirto: não andeis ansiosos pela vossa vida, quanto ao que haveis de comer, nem pelo vosso corpo, quanto ao que haveis de vestir.
23 Porque a vida é mais do que o alimento, e o corpo, mais do que as vestes.
24 Observai os corvos, os quais não semeiam, nem ceifam, não têm despensa nem celeiros; todavia, Deus os sustenta. Quanto mais valeis do que as aves!
25 Qual de vós, por ansioso que esteja, pode acrescentar um côvado ao curso da sua vida?
26 Se, portanto, nada podeis fazer quanto às coisas mínimas, por que andais ansiosos pelas outras?
27 Observai os lírios; eles não fiam, nem tecem. Eu, contudo, vos afirmo que nem Salomão, em toda a sua glória, se vestiu como qualquer deles.
28 Ora, se Deus veste assim a erva que hoje está no campo e amanhã é lançada no forno, quanto mais tratando-se de vós, homens de pequena fé!
29 Não andeis, pois, a indagar o que haveis de comer ou beber e não vos entregueis a inquietações.
30 Porque os gentios de todo o mundo é que procuram estas coisas; mas vosso Pai sabe que necessitais delas.
31 Buscai, antes de tudo, o seu reino, e estas coisas vos serão acrescentadas.
32 Não temais, ó pequenino rebanho; porque vosso Pai se agradou em dar-vos o seu reino.
33 Vendei os vossos bens e dai esmola; fazei para vós outros bolsas que não desgastem, tesouro inextinguível nos céus, onde não chega o ladrão, nem a traça consome,
34 porque, onde está o vosso tesouro, aí estará também o vosso coração.
35 Cingido esteja o vosso corpo, e acesas, as vossas candeias.
36 Sede vós semelhantes a homens que esperam pelo seu senhor, ao voltar ele das festas de casamento; para que, quando vier e bater à porta, logo lha abram.
37 Bem-aventurados aqueles servos a quem o senhor, quando vier, os encontre vigilantes; em verdade vos afirmo que ele há de cingir-se, dar-lhes lugar à mesa e, aproximando-se, os servirá.
38 Quer ele venha na segunda vigília, quer na terceira, bem-aventurados serão eles, se assim os achar.
39 Sabei, porém, isto: se o pai de família soubesse a que hora havia de vir o ladrão, [vigiaria e] não deixaria arrombar a sua casa.
40 Ficai também vós apercebidos, porque, à hora em que não cuidais, o Filho do Homem virá.
41 Então, Pedro perguntou: Senhor, proferes esta parábola para nós ou também para todos?
42 Disse o Senhor: Quem é, pois, o mordomo fiel e prudente, a quem o senhor confiará os seus conservos para dar-lhes o sustento a seu tempo?
43 Bem-aventurado aquele servo a quem seu senhor, quando vier, achar fazendo assim.
44 Verdadeiramente, vos digo que lhe confiará todos os seus bens.
45 Mas, se aquele servo disser consigo mesmo: Meu senhor tarda em vir, e passar a espancar os criados e as criadas, a comer, a beber e a embriagar-se,
46 virá o senhor daquele servo, em dia em que não o espera e em hora que não sabe, e castigá-lo-á, lançando-lhe a sorte com os infiéis.
47 Aquele servo, porém, que conheceu a vontade de seu senhor e não se aprontou, nem fez segundo a sua vontade será punido com muitos açoites.
48 Aquele, porém, que não soube a vontade do seu senhor e fez coisas dignas de reprovação levará poucos açoites. Mas àquele a quem muito foi dado, muito lhe será exigido; e àquele a quem muito se confia, muito mais lhe pedirão.
49 Eu vim para lançar fogo sobre a terra e bem quisera que já estivesse a arder.
50 Tenho, porém, um batismo com o qual hei de ser batizado; e quanto me angustio até que o mesmo se realize!
51 Supondes que vim para dar paz à terra? Não, eu vo-lo afirmo; antes, divisão.
52 Porque, daqui em diante, estarão cinco divididos numa casa: três contra dois, e dois contra três.
53 Estarão divididos: pai contra filho, filho contra pai; mãe contra filha, filha contra mãe; sogra contra nora, e nora contra sogra.
54 Disse também às multidões: Quando vedes aparecer uma nuvem no poente, logo dizeis que vem chuva, e assim acontece;
55 e, quando vedes soprar o vento sul, dizeis que haverá calor, e assim acontece.
56 Hipócritas, sabeis interpretar o aspecto da terra e do céu e, entretanto, não sabeis discernir esta época?
57 E por que não julgais também por vós mesmos o que é justo?
58 Quando fores com o teu adversário ao magistrado, esforça-te para te livrares desse adversário no caminho; para que não suceda que ele te arraste ao juiz, o juiz te entregue ao meirinho e o meirinho te recolha à prisão.
59 Digo-te que não sairás dali enquanto não pagares o último centavo.*
1 Naquela mesma ocasião, chegando alguns, falavam a Jesus a respeito dos galileus cujo sangue Pilatos misturara com os sacrifícios que os mesmos realizavam.
2 Ele, porém, lhes disse: Pensais que esses galileus eram mais pecadores do que todos os outros galileus, por terem padecido estas coisas?
3 Não eram, eu vo-lo afirmo; se, porém, não vos arrependerdes, todos igualmente perecereis.
4 Ou cuidais que aqueles dezoito sobre os quais desabou a torre de Siloé e os matou eram mais culpados que todos os outros habitantes de Jerusalém?
5 Não eram, eu vo-lo afirmo; mas, se não vos arrependerdes, todos igualmente perecereis.
6 Então, Jesus proferiu a seguinte parábola: Certo homem tinha uma figueira plantada na sua vinha e, vindo procurar fruto nela, não achou.
7 Pelo que disse ao viticultor: Há três anos venho procurar fruto nesta figueira e não acho; podes cortá-la; para que está ela ainda ocupando inutilmente a terra?
8 Ele, porém, respondeu: Senhor, deixa-a ainda este ano, até que eu escave ao redor dela e lhe ponha estrume.
9 Se vier a dar fruto, bem está; se não, mandarás cortá-la.
10 Ora, ensinava Jesus no sábado numa das sinagogas.
11 E veio ali uma mulher possessa de um espírito de enfermidade, havia já dezoito anos; andava ela encurvada, sem de modo algum poder endireitar-se.
12 Vendo-a Jesus, chamou-a e disse-lhe: Mulher, estás livre da tua enfermidade;
13 e, impondo-lhe as mãos, ela imediatamente se endireitou e dava glória a Deus.
14 O chefe da sinagoga, indignado de ver que Jesus curava no sábado, disse à multidão: Seis dias há em que se deve trabalhar; vinde, pois, nesses dias para serdes curados e não no sábado.
15 Disse-lhe, porém, o Senhor: Hipócritas, cada um de vós não desprende da manjedoura, no sábado, o seu boi ou o seu jumento, para levá-lo a beber?
16 Por que motivo não se devia livrar deste cativeiro, em dia de sábado, esta filha de Abraão, a quem Satanás trazia presa há dezoito anos?
17 Tendo ele dito estas palavras, todos os seus adversários se envergonharam. Entretanto, o povo se alegrava por todos os gloriosos feitos que Jesus realizava.
18 E dizia: A que é semelhante o reino de Deus, e a que o compararei?
19 É semelhante a um grão de mostarda que um homem plantou na sua horta; e cresceu e fez-se árvore; e as aves do céu aninharam-se nos seus ramos.
20 Disse mais: A que compararei o reino de Deus?
21 É semelhante ao fermento que uma mulher tomou e escondeu em três medidas de farinha, até ficar tudo levedado.
22 Passava Jesus por cidades e aldeias, ensinando e caminhando para Jerusalém.
23 E alguém lhe perguntou: Senhor, são poucos os que são salvos?
24 Respondeu-lhes: Esforçai-vos por entrar pela porta estreita, pois eu vos digo que muitos procurarão entrar e não poderão.
25 Quando o dono da casa se tiver levantado e fechado a porta, e vós, do lado de fora, começardes a bater, dizendo: Senhor, abre-nos a porta, ele vos responderá: Não sei donde sois.
26 Então, direis: Comíamos e bebíamos na tua presença, e ensinavas em nossas ruas.
27 Mas ele vos dirá: Não sei donde vós sois; apartai-vos de mim, vós todos os que praticais iniquidades.
28 Ali haverá choro e ranger de dentes, quando virdes, no reino de Deus, Abraão, Isaque, Jacó e todos os profetas, mas vós, lançados fora.
29 Muitos virão do Oriente e do Ocidente, do Norte e do Sul e tomarão lugares à mesa no reino de Deus.
30 Contudo, há últimos que virão a ser primeiros, e primeiros que serão últimos.
31 Naquela mesma hora, alguns fariseus vieram para dizer-lhe: Retira-te e vai-te daqui, porque Herodes quer matar-te.
32 Ele, porém, lhes respondeu: Ide dizer a essa raposa que, hoje e amanhã, expulso demônios e curo enfermos e, no terceiro dia, terminarei.
33 Importa, contudo, caminhar hoje, amanhã e depois, porque não se espera que um profeta morra fora de Jerusalém.
34 Jerusalém, Jerusalém, que matas os profetas e apedrejas os que te foram enviados! Quantas vezes quis eu reunir teus filhos como a galinha ajunta os do seu próprio ninho debaixo das asas, e vós não o quisestes!
35 Eis que a vossa casa vos ficará deserta. E em verdade vos digo que não mais me vereis até que venhais a dizer: Bendito o que vem em nome do Senhor!*
1 Aconteceu que, ao entrar ele num sábado na casa de um dos principais fariseus para comer pão, eis que o estavam observando.
2 Ora, diante dele se achava um homem hidrópico.
3 Então, Jesus, dirigindo-se aos intérpretes da Lei e aos fariseus, perguntou-lhes: É ou não é lícito curar no sábado?
4 Eles, porém, nada disseram. E, tomando-o, o curou e o despediu.
5 A seguir, lhes perguntou: Qual de vós, se o filho ou o boi cair num poço, não o tirará logo, mesmo em dia de sábado?
6 A isto nada puderam responder.
7 Reparando como os convidados escolhiam os primeiros lugares, propôs-lhes uma parábola:
8 Quando por alguém fores convidado para um casamento, não procures o primeiro lugar; para não suceder que, havendo um convidado mais digno do que tu,
9 vindo aquele que te convidou e também a ele, te diga: Dá o lugar a este. Então, irás, envergonhado, ocupar o último lugar.
10 Pelo contrário, quando fores convidado, vai tomar o último lugar; para que, quando vier o que te convidou, te diga: Amigo, senta-te mais para cima. Ser-te-á isto uma honra diante de todos os mais convivas.
11 Pois todo o que se exalta será humilhado; e o que se humilha será exaltado.
12 Disse também ao que o havia convidado: Quando deres um jantar ou uma ceia, não convides os teus amigos, nem teus irmãos, nem teus parentes, nem vizinhos ricos; para não suceder que eles, por sua vez, te convidem e sejas recompensado.
13 Antes, ao dares um banquete, convida os pobres, os aleijados, os coxos e os cegos;
14 e serás bem-aventurado, pelo fato de não terem eles com que recompensar-te; a tua recompensa, porém, tu a receberás na ressurreição dos justos.
15 Ora, ouvindo tais palavras, um dos que estavam com ele à mesa, disse-lhe: Bem-aventurado aquele que comer pão no reino de Deus.
16 Ele, porém, respondeu: Certo homem deu uma grande ceia e convidou muitos.
17 À hora da ceia, enviou o seu servo para avisar aos convidados: Vinde, porque tudo já está preparado.
18 Não obstante, todos, à uma, começaram a escusar-se. Disse o primeiro: Comprei um campo e preciso ir vê-lo; rogo-te que me tenhas por escusado.
19 Outro disse: Comprei cinco juntas de bois e vou experimentá-las; rogo-te que me tenhas por escusado.
20 E outro disse: Casei-me e, por isso, não posso ir.
21 Voltando o servo, tudo contou ao seu senhor. Então, irado, o dono da casa disse ao seu servo: Sai depressa para as ruas e becos da cidade e traze para aqui os pobres, os aleijados, os cegos e os coxos.
22 Depois, lhe disse o servo: Senhor, feito está como mandaste, e ainda há lugar.
23 Respondeu-lhe o senhor: Sai pelos caminhos e atalhos e obriga a todos a entrar, para que fique cheia a minha casa.
24 Porque vos declaro que nenhum daqueles homens que foram convidados provará a minha ceia.
25 Grandes multidões o acompanhavam, e ele, voltando-se, lhes disse:
26 Se alguém vem a mim e não aborrece a seu pai, e mãe, e mulher, e filhos, e irmãos, e irmãs e ainda a sua própria vida, não pode ser meu discípulo.
27 E qualquer que não tomar a sua cruz e vier após mim não pode ser meu discípulo.
28 Pois qual de vós, pretendendo construir uma torre, não se assenta primeiro para calcular a despesa e verificar se tem os meios para a concluir?
29 Para não suceder que, tendo lançado os alicerces e não a podendo acabar, todos os que a virem zombem dele,
30 dizendo: Este homem começou a construir e não pôde acabar.
31 Ou qual é o rei que, indo para combater outro rei, não se assenta primeiro para calcular se com dez mil homens poderá enfrentar o que vem contra ele com vinte mil?
32 Caso contrário, estando o outro ainda longe, envia-lhe uma embaixada, pedindo condições de paz.
33 Assim, pois, todo aquele que dentre vós não renuncia a tudo quanto tem não pode ser meu discípulo.
34 O sal é certamente bom; caso, porém, se torne insípido, como restaurar-lhe o sabor?
35 Nem presta para a terra, nem mesmo para o monturo; lançam-no fora. Quem tem ouvidos para ouvir, ouça.*
1 Aproximavam-se de Jesus todos os publicanos e pecadores para o ouvir.
2 E murmuravam os fariseus e os escribas, dizendo: Este recebe pecadores e come com eles.
3 Então, lhes propôs Jesus esta parábola:
4 Qual, dentre vós, é o homem que, possuindo cem ovelhas e perdendo uma delas, não deixa no deserto as noventa e nove e vai em busca da que se perdeu, até encontrá-la?
5 Achando-a, põe-na sobre os ombros, cheio de júbilo.
6 E, indo para casa, reúne os amigos e vizinhos, dizendo-lhes: Alegrai-vos comigo, porque já achei a minha ovelha perdida.
7 Digo-vos que, assim, haverá maior júbilo no céu por um pecador que se arrepende do que por noventa e nove justos que não necessitam de arrependimento.
8 Ou qual é a mulher que, tendo dez dracmas, se perder uma, não acende a candeia, varre a casa e a procura diligentemente até encontrá-la?
9 E, tendo-a achado, reúne as amigas e vizinhas, dizendo: Alegrai-vos comigo, porque achei a dracma que eu tinha perdido.
10 Eu vos afirmo que, de igual modo, há júbilo diante dos anjos de Deus por um pecador que se arrepende.
11 Continuou: Certo homem tinha dois filhos;
12 o mais moço deles disse ao pai: Pai, dá-me a parte dos bens que me cabe. E ele lhes repartiu os haveres.
13 Passados não muitos dias, o filho mais moço, ajuntando tudo o que era seu, partiu para uma terra distante e lá dissipou todos os seus bens, vivendo dissolutamente.
14 Depois de ter consumido tudo, sobreveio àquele país uma grande fome, e ele começou a passar necessidade.
15 Então, ele foi e se agregou a um dos cidadãos daquela terra, e este o mandou para os seus campos a guardar porcos.
16 Ali, desejava ele fartar-se das alfarrobas que os porcos comiam; mas ninguém lhe dava nada.
17 Então, caindo em si, disse: Quantos trabalhadores de meu pai têm pão com fartura, e eu aqui morro de fome!
18 Levantar-me-ei, e irei ter com o meu pai, e lhe direi: Pai, pequei contra o céu e diante de ti;
19 já não sou digno de ser chamado teu filho; trata-me como um dos teus trabalhadores.
20 E, levantando-se, foi para seu pai. Vinha ele ainda longe, quando seu pai o avistou, e, compadecido dele, correndo, o abraçou, e beijou.
21 E o filho lhe disse: Pai, pequei contra o céu e diante de ti; já não sou digno de ser chamado teu filho.
22 O pai, porém, disse aos seus servos: Trazei depressa a melhor roupa, vesti-o, ponde-lhe um anel no dedo e sandálias nos pés;
23 trazei também e matai o novilho cevado. Comamos e regozijemo-nos,
24 porque este meu filho estava morto e reviveu, estava perdido e foi achado. E começaram a regozijar-se.
25 Ora, o filho mais velho estivera no campo; e, quando voltava, ao aproximar-se da casa, ouviu a música e as danças.
26 Chamou um dos criados e perguntou-lhe que era aquilo.
27 E ele informou: Veio teu irmão, e teu pai mandou matar o novilho cevado, porque o recuperou com saúde.
28 Ele se indignou e não queria entrar; saindo, porém, o pai, procurava conciliá-lo.
29 Mas ele respondeu a seu pai: Há tantos anos que te sirvo sem jamais transgredir uma ordem tua, e nunca me deste um cabrito sequer para alegrar-me com os meus amigos;
30 vindo, porém, esse teu filho, que desperdiçou os teus bens com meretrizes, tu mandaste matar para ele o novilho cevado.
31 Então, lhe respondeu o pai: Meu filho, tu sempre estás comigo; tudo o que é meu é teu.
32 Entretanto, era preciso que nos regozijássemos e nos alegrássemos, porque esse teu irmão estava morto e reviveu, estava perdido e foi achado.*
1 Disse Jesus também aos discípulos: Havia um homem rico que tinha um administrador; e este lhe foi denunciado como quem estava a defraudar os seus bens.
2 Então, mandando-o chamar, lhe disse: Que é isto que ouço a teu respeito? Presta contas da tua administração, porque já não podes mais continuar nela.
3 Disse o administrador consigo mesmo: Que farei, pois o meu senhor me tira a administração? Trabalhar na terra não posso; também de mendigar tenho vergonha.
4 Eu sei o que farei, para que, quando for demitido da administração, me recebam em suas casas.
5 Tendo chamado cada um dos devedores do seu senhor, disse ao primeiro: Quanto deves ao meu patrão?
6 Respondeu ele: Cem cados de azeite. Então, disse: Toma a tua conta, assenta-te depressa e escreve cinquenta.
7 Depois, perguntou a outro: Tu, quanto deves? Respondeu ele: Cem coros de trigo. Disse-lhe: Toma a tua conta e escreve oitenta.
8 E elogiou o senhor o administrador infiel porque se houvera atiladamente, porque os filhos do mundo são mais hábeis na sua própria geração do que os filhos da luz.
9 E eu vos recomendo: das riquezas de origem iníqua fazei amigos; para que, quando aquelas vos faltarem, esses amigos vos recebam nos tabernáculos eternos.
10 Quem é fiel no pouco também é fiel no muito; e quem é injusto no pouco também é injusto no muito.
11 Se, pois, não vos tornastes fiéis na aplicação das riquezas de origem injusta, quem vos confiará a verdadeira riqueza?
12 Se não vos tornastes fiéis na aplicação do alheio, quem vos dará o que é vosso?
13 Ninguém pode servir a dois senhores; porque ou há de aborrecer-se de um e amar ao outro ou se devotará a um e desprezará ao outro. Não podeis servir a Deus e às riquezas.
14 Os fariseus, que eram avarentos, ouviam tudo isto e o ridiculizavam.
15 Mas Jesus lhes disse: Vós sois os que vos justificais a vós mesmos diante dos homens, mas Deus conhece o vosso coração; pois aquilo que é elevado entre homens é abominação diante de Deus.
16 A Lei e os Profetas vigoraram até João; desde esse tempo, vem sendo anunciado o evangelho do reino de Deus, e todo homem se esforça por entrar nele.
17 E é mais fácil passar o céu e a terra do que cair um til sequer da Lei.
18 Quem repudiar sua mulher e casar com outra comete adultério; e aquele que casa com a mulher repudiada pelo marido também comete adultério.
19 Ora, havia certo homem rico que se vestia de púrpura e de linho finíssimo e que, todos os dias, se regalava esplendidamente.
20 Havia também certo mendigo, chamado Lázaro, coberto de chagas, que jazia à porta daquele;
21 e desejava alimentar-se das migalhas que caíam da mesa do rico; e até os cães vinham lamber-lhe as úlceras.
22 Aconteceu morrer o mendigo e ser levado pelos anjos para o seio de Abraão; morreu também o rico e foi sepultado.
23 No inferno, estando em tormentos, levantou os olhos e viu ao longe a Abraão e Lázaro no seu seio.
24 Então, clamando, disse: Pai Abraão, tem misericórdia de mim! E manda a Lázaro que molhe em água a ponta do dedo e me refresque a língua, porque estou atormentado nesta chama.
25 Disse, porém, Abraão: Filho, lembra-te de que recebeste os teus bens em tua vida, e Lázaro igualmente, os males; agora, porém, aqui, ele está consolado; tu, em tormentos.
26 E, além de tudo, está posto um grande abismo entre nós e vós, de sorte que os que querem passar daqui para vós outros não podem, nem os de lá passar para nós.
27 Então, replicou: Pai, eu te imploro que o mandes à minha casa paterna,
28 porque tenho cinco irmãos; para que lhes dê testemunho, a fim de não virem também para este lugar de tormento.
29 Respondeu Abraão: Eles têm Moisés e os Profetas; ouçam-nos.
30 Mas ele insistiu: Não, pai Abraão; se alguém dentre os mortos for ter com eles, arrepender-se-ão.
31 Abraão, porém, lhe respondeu: Se não ouvem a Moisés e aos Profetas, tampouco se deixarão persuadir, ainda que ressuscite alguém dentre os mortos.*
1 Disse Jesus a seus discípulos: É inevitável que venham escândalos, mas ai do homem pelo qual eles vêm!
2 Melhor fora que se lhe pendurasse ao pescoço uma pedra de moinho, e fosse atirado no mar, do que fazer tropeçar a um destes pequeninos.
3 Acautelai-vos. Se teu irmão pecar contra ti, repreende-o; se ele se arrepender, perdoa-lhe.
4 Se, por sete vezes no dia, pecar contra ti e, sete vezes, vier ter contigo, dizendo: Estou arrependido, perdoa-lhe.
5 Então, disseram os apóstolos ao Senhor: Aumenta-nos a fé.
6 Respondeu-lhes o Senhor: Se tiverdes fé como um grão de mostarda, direis a esta amoreira: Arranca-te e transplanta-te no mar; e ela vos obedecerá.
7 Qual de vós, tendo um servo ocupado na lavoura ou em guardar o gado, lhe dirá quando ele voltar do campo: Vem já e põe-te à mesa?
8 E que, antes, não lhe diga: Prepara-me a ceia, cinge-te e serve-me, enquanto eu como e bebo; depois, comerás tu e beberás?
9 Porventura, terá de agradecer ao servo porque este fez o que lhe havia ordenado?
10 Assim também vós, depois de haverdes feito quanto vos foi ordenado, dizei: Somos servos inúteis, porque fizemos apenas o que devíamos fazer.
11 De caminho para Jerusalém, passava Jesus pelo meio de Samaria e da Galileia.
12 Ao entrar numa aldeia, saíram-lhe ao encontro dez leprosos,
13 que ficaram de longe e lhe gritaram, dizendo: Jesus, Mestre, compadece-te de nós!
14 Ao vê-los, disse-lhes Jesus: Ide e mostrai-vos aos sacerdotes. Aconteceu que, indo eles, foram purificados.
15 Um dos dez, vendo que fora curado, voltou, dando glória a Deus em alta voz,
16 e prostrou-se com o rosto em terra aos pés de Jesus, agradecendo-lhe; e este era samaritano.
17 Então, Jesus lhe perguntou: Não eram dez os que foram curados? Onde estão os nove?
18 Não houve, porventura, quem voltasse para dar glória a Deus, senão este estrangeiro?
19 E disse-lhe: Levanta-te e vai; a tua fé te salvou.
20 Interrogado pelos fariseus sobre quando viria o reino de Deus, Jesus lhes respondeu: Não vem o reino de Deus com visível aparência.
21 Nem dirão: Ei-lo aqui! Ou: Lá está! Porque o reino de Deus está dentro de vós.
22 A seguir, dirigiu-se aos discípulos: Virá o tempo em que desejareis ver um dos dias do Filho do Homem e não o vereis.
23 E vos dirão: Ei-lo aqui! Ou: Lá está! Não vades nem os sigais;
24 porque assim como o relâmpago, fuzilando, brilha de uma à outra extremidade do céu, assim será, no seu dia, o Filho do Homem.
25 Mas importa que primeiro ele padeça muitas coisas e seja rejeitado por esta geração.
26 Assim como foi nos dias de Noé, será também nos dias do Filho do Homem:
27 comiam, bebiam, casavam e davam-se em casamento, até ao dia em que Noé entrou na arca, e veio o dilúvio e destruiu a todos.
28 O mesmo aconteceu nos dias de Ló: comiam, bebiam, compravam, vendiam, plantavam e edificavam;
29 mas, no dia em que Ló saiu de Sodoma, choveu do céu fogo e enxofre e destruiu a todos.
30 Assim será no dia em que o Filho do Homem se manifestar.
31 Naquele dia, quem estiver no eirado e tiver os seus bens em casa não desça para tirá-los; e de igual modo quem estiver no campo não volte para trás.
32 Lembrai-vos da mulher de Ló.
33 Quem quiser preservar a sua vida perdê-la-á; e quem a perder de fato a salvará.
34 Digo-vos que, naquela noite, dois estarão numa cama; um será tomado, e deixado o outro;
35 duas mulheres estarão juntas moendo; uma será tomada, e deixada a outra.
36 [Dois estarão no campo; um será tomado, e o outro, deixado.]
37 Então, lhe perguntaram: Onde será isso, Senhor? Respondeu-lhes: Onde estiver o corpo, aí se ajuntarão também os abutres.*
1 Disse-lhes Jesus uma parábola sobre o dever de orar sempre e nunca esmorecer:
2 Havia em certa cidade um juiz que não temia a Deus, nem respeitava homem algum.
3 Havia também, naquela mesma cidade, uma viúva que vinha ter com ele, dizendo: Julga a minha causa contra o meu adversário.
4 Ele, por algum tempo, não a quis atender; mas, depois, disse consigo: Bem que eu não temo a Deus, nem respeito a homem algum;
5 todavia, como esta viúva me importuna, julgarei a sua causa, para não suceder que, por fim, venha a molestar-me.
6 Então, disse o Senhor: Considerai no que diz este juiz iníquo.
7 Não fará Deus justiça aos seus escolhidos, que a ele clamam dia e noite, embora pareça demorado em defendê-los?
8 Digo-vos que, depressa, lhes fará justiça. Contudo, quando vier o Filho do Homem, achará, porventura, fé na terra?
9 Propôs também esta parábola a alguns que confiavam em si mesmos, por se considerarem justos, e desprezavam os outros:
10 Dois homens subiram ao templo com o propósito de orar: um, fariseu, e o outro, publicano.
11 O fariseu, posto em pé, orava de si para si mesmo, desta forma: Ó Deus, graças te dou porque não sou como os demais homens, roubadores, injustos e adúlteros, nem ainda como este publicano;
12 jejuo duas vezes por semana e dou o dízimo de tudo quanto ganho.
13 O publicano, estando em pé, longe, não ousava nem ainda levantar os olhos ao céu, mas batia no peito, dizendo: Ó Deus, sê propício a mim, pecador!
14 Digo-vos que este desceu justificado para sua casa, e não aquele; porque todo o que se exalta será humilhado; mas o que se humilha será exaltado.
15 Traziam-lhe também as crianças, para que as tocasse; e os discípulos, vendo, os repreendiam.
16 Jesus, porém, chamando-as para junto de si, ordenou: Deixai vir a mim os pequeninos e não os embaraceis, porque dos tais é o reino de Deus.
17 Em verdade vos digo: Quem não receber o reino de Deus como uma criança de maneira alguma entrará nele.
18 Certo homem de posição perguntou-lhe: Bom Mestre, que farei para herdar a vida eterna?
19 Respondeu-lhe Jesus: Por que me chamas bom? Ninguém é bom, senão um, que é Deus.
20 Sabes os mandamentos: Não adulterarás , não matarás , não furtarás , não dirás falso testemunho , honra a teu pai e a tua mãe.
21 Replicou ele: Tudo isso tenho observado desde a minha juventude.
22 Ouvindo-o Jesus, disse-lhe: Uma coisa ainda te falta: vende tudo o que tens, dá-o aos pobres e terás um tesouro nos céus; depois, vem e segue-me.
23 Mas, ouvindo ele estas palavras, ficou muito triste, porque era riquíssimo.
24 E Jesus, vendo-o assim triste, disse: Quão dificilmente entrarão no reino de Deus os que têm riquezas!
25 Porque é mais fácil passar um camelo pelo fundo de uma agulha do que entrar um rico no reino de Deus.
26 E os que ouviram disseram: Sendo assim, quem pode ser salvo?
27 Mas ele respondeu: Os impossíveis dos homens são possíveis para Deus.
28 E disse Pedro: Eis que nós deixamos nossa casa e te seguimos.
29 Respondeu-lhes Jesus: Em verdade vos digo que ninguém há que tenha deixado casa, ou mulher, ou irmãos, ou pais, ou filhos, por causa do reino de Deus,
30 que não receba, no presente, muitas vezes mais e, no mundo por vir, a vida eterna.
31 Tomando consigo os doze, disse-lhes Jesus: Eis que subimos para Jerusalém, e vai cumprir-se ali tudo quanto está escrito por intermédio dos profetas, no tocante ao Filho do Homem;
32 pois será ele entregue aos gentios, escarnecido, ultrajado e cuspido;
33 e, depois de o açoitarem, tirar-lhe-ão a vida; mas, ao terceiro dia, ressuscitará.
34 Eles, porém, nada compreenderam acerca destas coisas; e o sentido destas palavras era-lhes encoberto, de sorte que não percebiam o que ele dizia.
35 Aconteceu que, ao aproximar-se ele de Jericó, estava um cego assentado à beira do caminho, pedindo esmolas.
36 E, ouvindo o tropel da multidão que passava, perguntou o que era aquilo.
37 Anunciaram-lhe que passava Jesus, o Nazareno.
38 Então, ele clamou: Jesus, Filho de Davi, tem compaixão de mim!
39 E os que iam na frente o repreendiam para que se calasse; ele, porém, cada vez gritava mais: Filho de Davi, tem misericórdia de mim!
40 Então, parou Jesus e mandou que lho trouxessem. E, tendo ele chegado, perguntou-lhe:
41 Que queres que eu te faça? Respondeu ele: Senhor, que eu torne a ver.
42 Então, Jesus lhe disse: Recupera a tua vista; a tua fé te salvou.
43 Imediatamente, tornou a ver e seguia-o glorificando a Deus. Também todo o povo, vendo isto, dava louvores a Deus.*
1 Entrando em Jericó, atravessava Jesus a cidade.
2 Eis que um homem, chamado Zaqueu, maioral dos publicanos e rico,
3 procurava ver quem era Jesus, mas não podia, por causa da multidão, por ser ele de pequena estatura.
4 Então, correndo adiante, subiu a um sicômoro a fim de vê-lo, porque por ali havia de passar.
5 Quando Jesus chegou àquele lugar, olhando para cima, disse-lhe: Zaqueu, desce depressa, pois me convém ficar hoje em tua casa.
6 Ele desceu a toda a pressa e o recebeu com alegria.
7 Todos os que viram isto murmuravam, dizendo que ele se hospedara com homem pecador.
8 Entrementes, Zaqueu se levantou e disse ao Senhor: Senhor, resolvo dar aos pobres a metade dos meus bens; e, se nalguma coisa tenho defraudado alguém, restituo quatro vezes mais.
9 Então, Jesus lhe disse: Hoje, houve salvação nesta casa, pois que também este é filho de Abraão.
10 Porque o Filho do Homem veio buscar e salvar o perdido.
11 Ouvindo eles estas coisas, Jesus propôs uma parábola, visto estar perto de Jerusalém e lhes parecer que o reino de Deus havia de manifestar-se imediatamente.
12 Então, disse: Certo homem nobre partiu para uma terra distante, com o fim de tomar posse de um reino e voltar.
13 Chamou dez servos seus, confiou-lhes dez minas e disse-lhes: Negociai até que eu volte.
14 Mas os seus concidadãos o odiavam e enviaram após ele uma embaixada, dizendo: Não queremos que este reine sobre nós.
15 Quando ele voltou, depois de haver tomado posse do reino, mandou chamar os servos a quem dera o dinheiro, a fim de saber que negócio cada um teria conseguido.
16 Compareceu o primeiro e disse: Senhor, a tua mina rendeu dez.
17 Respondeu-lhe o senhor: Muito bem, servo bom; porque foste fiel no pouco, terás autoridade sobre dez cidades.
18 Veio o segundo, dizendo: Senhor, a tua mina rendeu cinco.
19 A este disse: Terás autoridade sobre cinco cidades.
20 Veio, então, outro, dizendo: Eis aqui, senhor, a tua mina, que eu guardei embrulhada num lenço.
21 Pois tive medo de ti, que és homem rigoroso; tiras o que não puseste e ceifas o que não semeaste.
22 Respondeu-lhe: Servo mau, por tua própria boca te condenarei. Sabias que eu sou homem rigoroso, que tiro o que não pus e ceifo o que não semeei;
23 por que não puseste o meu dinheiro no banco? E, então, na minha vinda, o receberia com juros.
24 E disse aos que o assistiam: Tirai-lhe a mina e dai-a ao que tem as dez.
25 Eles ponderaram: Senhor, ele já tem dez.
26 Pois eu vos declaro: a todo o que tem dar-se-lhe-á; mas ao que não tem, o que tem lhe será tirado.
27 Quanto, porém, a esses meus inimigos, que não quiseram que eu reinasse sobre eles, trazei-os aqui e executai-os na minha presença.
28 E, dito isto, prosseguia Jesus subindo para Jerusalém.
29 Ora, aconteceu que, ao aproximar-se de Betfagé e de Betânia, junto ao monte das Oliveiras, enviou dois de seus discípulos,
30 dizendo-lhes: Ide à aldeia fronteira e ali, ao entrardes, achareis preso um jumentinho que jamais homem algum montou; soltai-o e trazei-o.
31 Se alguém vos perguntar: Por que o soltais? Respondereis assim: Porque o Senhor precisa dele.
32 E, indo os que foram mandados, acharam segundo lhes dissera Jesus.
33 Quando eles estavam soltando o jumentinho, seus donos lhes disseram: Por que o soltais?
34 Responderam: Porque o Senhor precisa dele.
35 Então, o trouxeram e, pondo as suas vestes sobre ele, ajudaram Jesus a montar.
36 Indo ele, estendiam no caminho as suas vestes.
37 E, quando se aproximava da descida do monte das Oliveiras, toda a multidão dos discípulos passou, jubilosa, a louvar a Deus em alta voz, por todos os milagres que tinham visto,
38 dizendo: Bendito é o Rei que vem em nome do Senhor! Paz no céu e glória nas maiores alturas!
39 Ora, alguns dos fariseus lhe disseram em meio à multidão: Mestre, repreende os teus discípulos!
40 Mas ele lhes respondeu: Asseguro-vos que, se eles se calarem, as próprias pedras clamarão.
41 Quando ia chegando, vendo a cidade, chorou
42 e dizia: Ah! Se conheceras por ti mesma, ainda hoje, o que é devido à paz! Mas isto está agora oculto aos teus olhos.
43 Pois sobre ti virão dias em que os teus inimigos te cercarão de trincheiras e, por todos os lados, te apertarão o cerco;
44 e te arrasarão e aos teus filhos dentro de ti; não deixarão em ti pedra sobre pedra, porque não reconheceste a oportunidade da tua visitação.
45 Depois, entrando no templo, expulsou os que ali vendiam,
46 dizendo-lhes: Está escrito: A minha casa será casa de oração. Mas vós a transformastes em covil de salteadores.
47 Diariamente, Jesus ensinava no templo; mas os principais sacerdotes, os escribas e os maiorais do povo procuravam eliminá-lo;
48 contudo, não atinavam em como fazê-lo, porque todo o povo, ao ouvi-lo, ficava dominado por ele.*
1 Aconteceu que, num daqueles dias, estando Jesus a ensinar o povo no templo e a evangelizar, sobrevieram os principais sacerdotes e os escribas, juntamente com os anciãos,
2 e o arguiram nestes termos: Dize-nos: com que autoridade fazes estas coisas? Ou quem te deu esta autoridade?
3 Respondeu-lhes: Também eu vos farei uma pergunta; dizei-me:
4 o batismo de João era dos céus ou dos homens?
5 Então, eles arrazoavam entre si: Se dissermos: do céu, ele dirá: Por que não acreditastes nele?
6 Mas, se dissermos: dos homens, o povo todo nos apedrejará; porque está convicto de ser João um profeta.
7 Por fim, responderam que não sabiam.
8 Então, Jesus lhes replicou: Pois nem eu vos digo com que autoridade faço estas coisas.
9 A seguir, passou Jesus a proferir ao povo esta parábola: Certo homem plantou uma vinha, arrendou-a a lavradores e ausentou-se do país por prazo considerável.
10 No devido tempo, mandou um servo aos lavradores para que lhe dessem do fruto da vinha; os lavradores, porém, depois de o espancarem, o despacharam vazio.
11 Em vista disso, enviou-lhes outro servo; mas eles também a este espancaram e, depois de o ultrajarem, o despacharam vazio.
12 Mandou ainda um terceiro; também a este, depois de o ferirem, expulsaram.
13 Então, disse o dono da vinha: Que farei? Enviarei o meu filho amado; talvez o respeitem.
14 Vendo-o, porém, os lavradores, arrazoavam entre si, dizendo: Este é o herdeiro; matemo-lo, para que a herança venha a ser nossa.
15 E, lançando-o fora da vinha, o mataram. Que lhes fará, pois, o dono da vinha?
16 Virá, exterminará aqueles lavradores e passará a vinha a outros. Ao ouvirem isto, disseram: Tal não aconteça!
17 Mas Jesus, fitando-os, disse: Que quer dizer, pois, o que está escrito: A pedra que os construtores rejeitaram, esta veio a ser a principal pedra, angular?
18 Todo o que cair sobre esta pedra ficará em pedaços; e aquele sobre quem ela cair ficará reduzido a pó.
19 Naquela mesma hora, os escribas e os principais sacerdotes procuravam lançar-lhe as mãos, pois perceberam que, em referência a eles, dissera esta parábola; mas temiam o povo.
20 Observando-o, subornaram emissários que se fingiam de justos para verem se o apanhavam em alguma palavra, a fim de entregá-lo à jurisdição e à autoridade do governador.
21 Então, o consultaram, dizendo: Mestre, sabemos que falas e ensinas retamente e não te deixas levar de respeitos humanos, porém ensinas o caminho de Deus segundo a verdade;
22 é lícito pagar tributo a César ou não?
23 Mas Jesus, percebendo-lhes o ardil, respondeu:
24 Mostrai-me um denário. De quem é a efígie e a inscrição? Prontamente disseram: De César. Então, lhes recomendou Jesus:
25 Dai, pois, a César o que é de César e a Deus o que é de Deus.
26 Não puderam apanhá-lo em palavra alguma diante do povo; e, admirados da sua resposta, calaram-se.
27 Chegando alguns dos saduceus, homens que dizem não haver ressurreição,
28 perguntaram-lhe: Mestre, Moisés nos deixou escrito que, se morrer o irmão de alguém, sendo aquele casado e não deixando filhos, seu irmão deve casar com a viúva e suscitar descendência ao falecido.
29 Ora, havia sete irmãos: o primeiro casou e morreu sem filhos;
30 o segundo e o terceiro também desposaram a viúva;
31 igualmente os sete não tiveram filhos e morreram.
32 Por fim, morreu também a mulher.
33 Esta mulher, pois, no dia da ressurreição, de qual deles será esposa? Porque os sete a desposaram.
34 Então, lhes acrescentou Jesus: Os filhos deste mundo casam-se e dão-se em casamento;
35 mas os que são havidos por dignos de alcançar a era vindoura e a ressurreição dentre os mortos não casam, nem se dão em casamento.
36 Pois não podem mais morrer, porque são iguais aos anjos e são filhos de Deus, sendo filhos da ressurreição.
37 E que os mortos hão de ressuscitar, Moisés o indicou no trecho referente à sarça, quando chama ao Senhor o Deus de Abraão, o Deus de Isaque e o Deus de Jacó.
38 Ora, Deus não é Deus de mortos, e sim de vivos; porque para ele todos vivem.
39 Então, disseram alguns dos escribas: Mestre, respondeste bem!
40 Dali por diante, não ousaram mais interrogá-lo.
41 Mas Jesus lhes perguntou: Como podem dizer que o Cristo é filho de Davi?
42 Visto como o próprio Davi afirma no livro dos Salmos: Disse o Senhor ao meu Senhor: Assenta-te à minha direita,
43 até que eu ponha os teus inimigos por estrado dos teus pés.
44 Assim, pois, Davi lhe chama Senhor, e como pode ser ele seu filho?
45 Ouvindo-o todo o povo, recomendou Jesus a seus discípulos:
46 Guardai-vos dos escribas, que gostam de andar com vestes talares e muito apreciam as saudações nas praças, as primeiras cadeiras nas sinagogas e os primeiros lugares nos banquetes;
47 os quais devoram as casas das viúvas e, para o justificar, fazem longas orações; estes sofrerão juízo muito mais severo.*
1 Estando Jesus a observar, viu os ricos lançarem suas ofertas no gazofilácio.
2 Viu também certa viúva pobre lançar ali duas pequenas moedas;
3 e disse: Verdadeiramente, vos digo que esta viúva pobre deu mais do que todos.
4 Porque todos estes deram como oferta daquilo que lhes sobrava; esta, porém, da sua pobreza deu tudo o que possuía, todo o seu sustento.
5 Falavam alguns a respeito do templo, como estava ornado de belas pedras e de dádivas;
6 então, disse Jesus: Vedes estas coisas? Dias virão em que não ficará pedra sobre pedra que não seja derribada.
7 Perguntaram-lhe: Mestre, quando sucederá isto? E que sinal haverá de quando estas coisas estiverem para se cumprir?
8 Respondeu ele: Vede que não sejais enganados; porque muitos virão em meu nome, dizendo: Sou eu! E também: Chegou a hora! Não os sigais.
9 Quando ouvirdes falar de guerras e revoluções, não vos assusteis; pois é necessário que primeiro aconteçam estas coisas, mas o fim não será logo.
10 Então, lhes disse: Levantar-se-á nação contra nação, e reino, contra reino;
11 haverá grandes terremotos, epidemias e fome em vários lugares, coisas espantosas e também grandes sinais do céu.
12 Antes, porém, de todas estas coisas, lançarão mão de vós e vos perseguirão, entregando-vos às sinagogas e aos cárceres, levando-vos à presença de reis e governadores, por causa do meu nome;
13 e isto vos acontecerá para que deis testemunho.
14 Assentai, pois, em vosso coração de não vos preocupardes com o que haveis de responder;
15 porque eu vos darei boca e sabedoria a que não poderão resistir, nem contradizer todos quantos se vos opuserem.
16 E sereis entregues até por vossos pais, irmãos, parentes e amigos; e matarão alguns dentre vós.
17 De todos sereis odiados por causa do meu nome.
18 Contudo, não se perderá um só fio de cabelo da vossa cabeça.
19 É na vossa perseverança que ganhareis a vossa alma.
20 Quando, porém, virdes Jerusalém sitiada de exércitos, sabei que está próxima a sua devastação.
21 Então, os que estiverem na Judeia, fujam para os montes; os que se encontrarem dentro da cidade, retirem-se; e os que estiverem nos campos, não entrem nela.
22 Porque estes dias são de vingança, para se cumprir tudo o que está escrito.
23 Ai das que estiverem grávidas e das que amamentarem naqueles dias! Porque haverá grande aflição na terra e ira contra este povo.
24 Cairão a fio de espada e serão levados cativos para todas as nações; e, até que os tempos dos gentios se completem, Jerusalém será pisada por eles.
25 Haverá sinais no sol, na lua e nas estrelas; sobre a terra, angústia entre as nações em perplexidade por causa do bramido do mar e das ondas;
26 haverá homens que desmaiarão de terror e pela expectativa das coisas que sobrevirão ao mundo; pois os poderes dos céus serão abalados.
27 Então, se verá o Filho do Homem vindo numa nuvem, com poder e grande glória.
28 Ora, ao começarem estas coisas a suceder, exultai e erguei a vossa cabeça; porque a vossa redenção se aproxima.
29 Ainda lhes propôs uma parábola, dizendo: Vede a figueira e todas as árvores.
30 Quando começam a brotar, vendo-o, sabeis, por vós mesmos, que o verão está próximo.
31 Assim também, quando virdes acontecerem estas coisas, sabei que está próximo o reino de Deus.
32 Em verdade vos digo que não passará esta geração, sem que tudo isto aconteça.
33 Passará o céu e a terra, porém as minhas palavras não passarão.
34 Acautelai-vos por vós mesmos, para que nunca vos suceda que o vosso coração fique sobrecarregado com as consequências da orgia, da embriaguez e das preocupações deste mundo, e para que aquele dia não venha sobre vós repentinamente, como um laço.
35 Pois há de sobrevir a todos os que vivem sobre a face de toda a terra.
36 Vigiai, pois, a todo tempo, orando, para que possais escapar de todas estas coisas que têm de suceder e estar em pé na presença do Filho do Homem.
37 Jesus ensinava todos os dias no templo, mas à noite, saindo, ia pousar no monte chamado das Oliveiras.
38 E todo o povo madrugava para ir ter com ele no templo, a fim de ouvi-lo.*
1 Estava próxima a Festa dos Pães Asmos, chamada Páscoa.
2 Preocupavam-se os principais sacerdotes e os escribas em como tirar a vida a Jesus; porque temiam o povo.
3 Ora, Satanás entrou em Judas, chamado Iscariotes, que era um dos doze.
4 Este foi entender-se com os principais sacerdotes e os capitães sobre como lhes entregaria a Jesus;
5 então, eles se alegraram e combinaram em lhe dar dinheiro.
6 Judas concordou e buscava uma boa ocasião de lho entregar sem tumulto.
7 Chegou o dia da Festa dos Pães Asmos, em que importava comemorar a Páscoa.
8 Jesus, pois, enviou Pedro e João, dizendo: Ide preparar-nos a Páscoa para que a comamos.
9 Eles lhe perguntaram: Onde queres que a preparemos?
10 Então, lhes explicou Jesus: Ao entrardes na cidade, encontrareis um homem com um cântaro de água; segui-o até à casa em que ele entrar
11 e dizei ao dono da casa: O Mestre manda perguntar-te: Onde é o aposento no qual hei de comer a Páscoa com os meus discípulos?
12 Ele vos mostrará um espaçoso cenáculo mobilado; ali fazei os preparativos.
13 E, indo, tudo encontraram como Jesus lhes dissera e prepararam a Páscoa.
14 Chegada a hora, pôs-se Jesus à mesa, e com ele os apóstolos.
15 E disse-lhes: Tenho desejado ansiosamente comer convosco esta Páscoa, antes do meu sofrimento.
16 Pois vos digo que nunca mais a comerei, até que ela se cumpra no reino de Deus.
17 E, tomando um cálice, havendo dado graças, disse: Recebei e reparti entre vós;
18 pois vos digo que, de agora em diante, não mais beberei do fruto da videira, até que venha o reino de Deus.
19 E, tomando um pão, tendo dado graças, o partiu e lhes deu, dizendo: Isto é o meu corpo oferecido por vós; fazei isto em memória de mim.
20 Semelhantemente, depois de cear, tomou o cálice, dizendo: Este é o cálice da nova aliança no meu sangue derramado em favor de vós.
21 Todavia, a mão do traidor está comigo à mesa.
22 Porque o Filho do Homem, na verdade, vai segundo o que está determinado, mas ai daquele por intermédio de quem ele está sendo traído!
23 Então, começaram a indagar entre si quem seria, dentre eles, o que estava para fazer isto.
24 Suscitaram também entre si uma discussão sobre qual deles parecia ser o maior.
25 Mas Jesus lhes disse: Os reis dos povos dominam sobre eles, e os que exercem autoridade são chamados benfeitores.
26 Mas vós não sois assim; pelo contrário, o maior entre vós seja como o menor; e aquele que dirige seja como o que serve.
27 Pois qual é maior: quem está à mesa ou quem serve? Porventura, não é quem está à mesa? Pois, no meio de vós, eu sou como quem serve.
28 Vós sois os que tendes permanecido comigo nas minhas tentações.
29 Assim como meu Pai me confiou um reino, eu vo-lo confio,
30 para que comais e bebais à minha mesa no meu reino; e vos assentareis em tronos para julgar as doze tribos de Israel.
31 Simão, Simão, eis que Satanás vos reclamou para vos peneirar como trigo!
32 Eu, porém, roguei por ti, para que a tua fé não desfaleça; tu, pois, quando te converteres, fortalece os teus irmãos.
33 Ele, porém, respondeu: Senhor, estou pronto a ir contigo, tanto para a prisão como para a morte.
34 Mas Jesus lhe disse: Afirmo-te, Pedro, que, hoje, três vezes negarás que me conheces, antes que o galo cante.
35 A seguir, Jesus lhes perguntou: Quando vos mandei sem bolsa, sem alforje e sem sandálias, faltou-vos, porventura, alguma coisa? Nada, disseram eles.
36 Então, lhes disse: Agora, porém, quem tem bolsa, tome-a, como também o alforje; e o que não tem espada, venda a sua capa e compre uma.
37 Pois vos digo que importa que se cumpra em mim o que está escrito: Ele foi contado com os malfeitores. Porque o que a mim se refere está sendo cumprido.
38 Então, lhe disseram: Senhor, eis aqui duas espadas! Respondeu-lhes: Basta!
39 E, saindo, foi, como de costume, para o monte das Oliveiras; e os discípulos o acompanharam.
40 Chegando ao lugar escolhido, Jesus lhes disse: Orai, para que não entreis em tentação.
41 Ele, por sua vez, se afastou, cerca de um tiro de pedra, e, de joelhos, orava,
42 dizendo: Pai, se queres, passa de mim este cálice; contudo, não se faça a minha vontade, e sim a tua.
43 [Então, lhe apareceu um anjo do céu que o confortava.
44 E, estando em agonia, orava mais intensamente. E aconteceu que o seu suor se tornou como gotas de sangue caindo sobre a terra.]
45 Levantando-se da oração, foi ter com os discípulos, e os achou dormindo de tristeza,
46 e disse-lhes: Por que estais dormindo? Levantai-vos e orai, para que não entreis em tentação.
47 Falava ele ainda, quando chegou uma multidão; e um dos doze, o chamado Judas, que vinha à frente deles, aproximou-se de Jesus para o beijar.
48 Jesus, porém, lhe disse: Judas, com um beijo trais o Filho do Homem?
49 Os que estavam ao redor dele, vendo o que ia suceder, perguntaram: Senhor, feriremos à espada?
50 Um deles feriu o servo do sumo sacerdote e cortou-lhe a orelha direita.
51 Mas Jesus acudiu, dizendo: Deixai, basta. E, tocando-lhe a orelha, o curou.
52 Então, dirigindo-se Jesus aos principais sacerdotes, capitães do templo e anciãos que vieram prendê-lo, disse: Saístes com espadas e porretes como para deter um salteador?
53 Diariamente, estando eu convosco no templo, não pusestes as mãos sobre mim. Esta, porém, é a vossa hora e o poder das trevas.
54 Então, prendendo-o, o levaram e o introduziram na casa do sumo sacerdote. Pedro seguia de longe.
55 E, quando acenderam fogo no meio do pátio e juntos se assentaram, Pedro tomou lugar entre eles.
56 Entrementes, uma criada, vendo-o assentado perto do fogo, fitando-o, disse: Este também estava com ele.
57 Mas Pedro negava, dizendo: Mulher, não o conheço.
58 Pouco depois, vendo-o outro, disse: Também tu és dos tais. Pedro, porém, protestava: Homem, não sou.
59 E, tendo passado cerca de uma hora, outro afirmava, dizendo: Também este, verdadeiramente, estava com ele, porque também é galileu.
60 Mas Pedro insistia: Homem, não compreendo o que dizes. E logo, estando ele ainda a falar, cantou o galo.
61 Então, voltando-se o Senhor, fixou os olhos em Pedro, e Pedro se lembrou da palavra do Senhor, como lhe dissera: Hoje, três vezes me negarás, antes de cantar o galo.
62 Então, Pedro, saindo dali, chorou amargamente.
63 Os que detinham Jesus zombavam dele, davam-lhe pancadas e,
64 vendando-lhe os olhos, diziam: Profetiza-nos: quem é que te bateu?
65 E muitas outras coisas diziam contra ele, blasfemando.
66 Logo que amanheceu, reuniu-se a assembleia dos anciãos do povo, tanto os principais sacerdotes como os escribas, e o conduziram ao Sinédrio, onde lhe disseram:
67 Se tu és o Cristo, dize-nos. Então, Jesus lhes respondeu: Se vo-lo disser, não o acreditareis;
68 também, se vos perguntar, de nenhum modo me respondereis.
69 Desde agora, estará sentado o Filho do Homem à direita do Todo-Poderoso Deus.
70 Então, disseram todos: Logo, tu és o Filho de Deus? E ele lhes respondeu: Vós dizeis que eu sou.
71 Clamaram, pois: Que necessidade mais temos de testemunho? Porque nós mesmos o ouvimos da sua própria boca.*
1 Levantando-se toda a assembleia, levaram Jesus a Pilatos.
2 E ali passaram a acusá-lo, dizendo: Encontramos este homem pervertendo a nossa nação, vedando pagar tributo a César e afirmando ser ele o Cristo, o Rei.
3 Então, lhe perguntou Pilatos: És tu o rei dos judeus? Respondeu Jesus: Tu o dizes.
4 Disse Pilatos aos principais sacerdotes e às multidões: Não vejo neste homem crime algum.
5 Insistiam, porém, cada vez mais, dizendo: Ele alvoroça o povo, ensinando por toda a Judeia, desde a Galileia, onde começou, até aqui.
6 Tendo Pilatos ouvido isto, perguntou se aquele homem era galileu.
7 Ao saber que era da jurisdição de Herodes, estando este, naqueles dias, em Jerusalém, lho remeteu.
8 Herodes, vendo a Jesus, sobremaneira se alegrou, pois havia muito queria vê-lo, por ter ouvido falar a seu respeito; esperava também vê-lo fazer algum sinal.
9 E de muitos modos o interrogava; Jesus, porém, nada lhe respondia.
10 Os principais sacerdotes e os escribas ali presentes o acusavam com grande veemência.
11 Mas Herodes, juntamente com os da sua guarda, tratou-o com desprezo, e, escarnecendo dele, fê-lo vestir-se de um manto aparatoso, e o devolveu a Pilatos.
12 Naquele mesmo dia, Herodes e Pilatos se reconciliaram, pois, antes, viviam inimizados um com o outro.
13 Então, reunindo Pilatos os principais sacerdotes, as autoridades e o povo,
14 disse-lhes: Apresentastes-me este homem como agitador do povo; mas, tendo-o interrogado na vossa presença, nada verifiquei contra ele dos crimes de que o acusais.
15 Nem tampouco Herodes, pois no-lo tornou a enviar. É, pois, claro que nada contra ele se verificou digno de morte.
16 Portanto, após castigá-lo, soltá-lo-ei.
17 [E era-lhe forçoso soltar-lhes um detento por ocasião da festa.]
18 Toda a multidão, porém, gritava: Fora com este! Solta-nos Barrabás!
19 Barrabás estava no cárcere por causa de uma sedição na cidade e também por homicídio.
20 Desejando Pilatos soltar a Jesus, insistiu ainda.
21 Eles, porém, mais gritavam: Crucifica-o! Crucifica-o!
22 Então, pela terceira vez, lhes perguntou: Que mal fez este? De fato, nada achei contra ele para condená-lo à morte; portanto, depois de o castigar, soltá-lo-ei.
23 Mas eles instavam com grandes gritos, pedindo que fosse crucificado. E o seu clamor prevaleceu.
24 Então, Pilatos decidiu atender-lhes o pedido.
25 Soltou aquele que estava encarcerado por causa da sedição e do homicídio, a quem eles pediam; e, quanto a Jesus, entregou-o à vontade deles.
26 E, como o conduzissem, constrangendo um cireneu, chamado Simão, que vinha do campo, puseram-lhe a cruz sobre os ombros, para que a levasse após Jesus.
27 Seguia-o numerosa multidão de povo, e também mulheres que batiam no peito e o lamentavam.
28 Porém Jesus, voltando-se para elas, disse: Filhas de Jerusalém, não choreis por mim; chorai, antes, por vós mesmas e por vossos filhos!
29 Porque dias virão em que se dirá: Bem-aventuradas as estéreis, que não geraram, nem amamentaram.
30 Nesses dias, dirão aos montes: Caí sobre nós! E aos outeiros: Cobri-nos!
31 Porque, se em lenho verde fazem isto, que será no lenho seco?
32 E também eram levados outros dois, que eram malfeitores, para serem executados com ele.
33 Quando chegaram ao lugar chamado Calvário, ali o crucificaram, bem como aos malfeitores, um à direita, outro à esquerda.
34 Contudo, Jesus dizia: Pai, perdoa-lhes, porque não sabem o que fazem. Então, repartindo as vestes dele, lançaram sortes.
35 O povo estava ali e a tudo observava. Também as autoridades zombavam e diziam: Salvou os outros; a si mesmo se salve, se é, de fato, o Cristo de Deus, o escolhido.
36 Igualmente os soldados o escarneciam e, aproximando-se, trouxeram-lhe vinagre, dizendo:
37 Se tu és o rei dos judeus, salva-te a ti mesmo.
38 Também sobre ele estava esta epígrafe [em letras gregas, romanas e hebraicas]: Este é o Rei dos Judeus.
39 Um dos malfeitores crucificados blasfemava contra ele, dizendo: Não és tu o Cristo? Salva-te a ti mesmo e a nós também.
40 Respondendo-lhe, porém, o outro, repreendeu-o, dizendo: Nem ao menos temes a Deus, estando sob igual sentença?
41 Nós, na verdade, com justiça, porque recebemos o castigo que os nossos atos merecem; mas este nenhum mal fez.
42 E acrescentou: Jesus, lembra-te de mim quando vieres no teu reino.
43 Jesus lhe respondeu: Em verdade te digo que hoje estarás comigo no paraíso.
44 Já era quase a hora sexta, e, escurecendo-se o sol, houve trevas sobre toda a terra até à hora nona.
45 E rasgou-se pelo meio o véu do santuário.
46 Então, Jesus clamou em alta voz: Pai, nas tuas mãos entrego o meu espírito! E, dito isto, expirou.
47 Vendo o centurião o que tinha acontecido, deu glória a Deus, dizendo: Verdadeiramente, este homem era justo.
48 E todas as multidões reunidas para este espetáculo, vendo o que havia acontecido, retiraram-se a lamentar, batendo nos peitos.
49 Entretanto, todos os conhecidos de Jesus e as mulheres que o tinham seguido desde a Galileia permaneceram a contemplar de longe estas coisas.
50 E eis que certo homem, chamado José, membro do Sinédrio, homem bom e justo
51 (que não tinha concordado com o desígnio e ação dos outros), natural de Arimateia, cidade dos judeus, e que esperava o reino de Deus,
52 tendo procurado a Pilatos, pediu-lhe o corpo de Jesus,
53 e, tirando-o do madeiro, envolveu-o num lençol de linho, e o depositou num túmulo aberto em rocha, onde ainda ninguém havia sido sepultado.
54 Era o dia da preparação, e começava o sábado.
55 As mulheres que tinham vindo da Galileia com Jesus, seguindo, viram o túmulo e como o corpo fora ali depositado.
56 Então, se retiraram para preparar aromas e bálsamos. E, no sábado, descansaram, segundo o mandamento.*
1 Mas, no primeiro dia da semana, alta madrugada, foram elas ao túmulo, levando os aromas que haviam preparado.
2 E encontraram a pedra removida do sepulcro;
3 mas, ao entrarem, não acharam o corpo do Senhor Jesus.
4 Aconteceu que, perplexas a esse respeito, apareceram-lhes dois varões com vestes resplandecentes.
5 Estando elas possuídas de temor, baixando os olhos para o chão, eles lhes falaram: Por que buscais entre os mortos ao que vive?
6 Ele não está aqui, mas ressuscitou. Lembrai-vos de como vos preveniu, estando ainda na Galileia,
7 quando disse: Importa que o Filho do Homem seja entregue nas mãos de pecadores, e seja crucificado, e ressuscite no terceiro dia.
8 Então, se lembraram das suas palavras.
9 E, voltando do túmulo, anunciaram todas estas coisas aos onze e a todos os mais que com eles estavam.
10 Eram Maria Madalena, Joana e Maria, mãe de Tiago; também as demais que estavam com elas confirmaram estas coisas aos apóstolos.
11 Tais palavras lhes pareciam um como delírio, e não acreditaram nelas.
12 Pedro, porém, levantando-se, correu ao sepulcro. E, abaixando-se, nada mais viu, senão os lençóis de linho; e retirou-se para casa, maravilhado do que havia acontecido.
13 Naquele mesmo dia, dois deles estavam de caminho para uma aldeia chamada Emaús, distante de Jerusalém sessenta estádios.
14 E iam conversando a respeito de todas as coisas sucedidas.
15 Aconteceu que, enquanto conversavam e discutiam, o próprio Jesus se aproximou e ia com eles.
16 Os seus olhos, porém, estavam como que impedidos de o reconhecer.
17 Então, lhes perguntou Jesus: Que é isso que vos preocupa e de que ides tratando à medida que caminhais? E eles pararam entristecidos.
18 Um, porém, chamado Cleopas, respondeu, dizendo: És o único, porventura, que, tendo estado em Jerusalém, ignoras as ocorrências destes últimos dias?
19 Ele lhes perguntou: Quais? E explicaram: O que aconteceu a Jesus, o Nazareno, que era varão profeta, poderoso em obras e palavras, diante de Deus e de todo o povo,
20 e como os principais sacerdotes e as nossas autoridades o entregaram para ser condenado à morte e o crucificaram.
21 Ora, nós esperávamos que fosse ele quem havia de redimir a Israel; mas, depois de tudo isto, é já este o terceiro dia desde que tais coisas sucederam.
22 É verdade também que algumas mulheres, das que conosco estavam, nos surpreenderam, tendo ido de madrugada ao túmulo;
23 e, não achando o corpo de Jesus, voltaram dizendo terem tido uma visão de anjos, os quais afirmam que ele vive.
24 De fato, alguns dos nossos foram ao sepulcro e verificaram a exatidão do que disseram as mulheres; mas não o viram.
25 Então, lhes disse Jesus: Ó néscios e tardos de coração para crer tudo o que os profetas disseram!
26 Porventura, não convinha que o Cristo padecesse e entrasse na sua glória?
27 E, começando por Moisés, discorrendo por todos os Profetas, expunha-lhes o que a seu respeito constava em todas as Escrituras.
28 Quando se aproximavam da aldeia para onde iam, fez ele menção de passar adiante.
29 Mas eles o constrangeram, dizendo: Fica conosco, porque é tarde, e o dia já declina. E entrou para ficar com eles.
30 E aconteceu que, quando estavam à mesa, tomando ele o pão, abençoou-o e, tendo-o partido, lhes deu;
31 então, se lhes abriram os olhos, e o reconheceram; mas ele desapareceu da presença deles.
32 E disseram um ao outro: Porventura, não nos ardia o coração, quando ele, pelo caminho, nos falava, quando nos expunha as Escrituras?
33 E, na mesma hora, levantando-se, voltaram para Jerusalém, onde acharam reunidos os onze e outros com eles,
34 os quais diziam: O Senhor ressuscitou e já apareceu a Simão!
35 Então, os dois contaram o que lhes acontecera no caminho e como fora por eles reconhecido no partir do pão.
36 Falavam ainda estas coisas quando Jesus apareceu no meio deles e lhes disse: Paz seja convosco!
37 Eles, porém, surpresos e atemorizados, acreditavam estarem vendo um espírito.
38 Mas ele lhes disse: Por que estais perturbados? E por que sobem dúvidas ao vosso coração?
39 Vede as minhas mãos e os meus pés, que sou eu mesmo; apalpai-me e verificai, porque um espírito não tem carne nem ossos, como vedes que eu tenho.
40 Dizendo isto, mostrou-lhes as mãos e os pés.
41 E, por não acreditarem eles ainda, por causa da alegria, e estando admirados, Jesus lhes disse: Tendes aqui alguma coisa que comer?
42 Então, lhe apresentaram um pedaço de peixe assado [e um favo de mel].
43 E ele comeu na presença deles.
44 A seguir, Jesus lhes disse: São estas as palavras que eu vos falei, estando ainda convosco: importava se cumprisse tudo o que de mim está escrito na Lei de Moisés, nos Profetas e nos Salmos.
45 Então, lhes abriu o entendimento para compreenderem as Escrituras;
46 e lhes disse: Assim está escrito que o Cristo havia de padecer e ressuscitar dentre os mortos no terceiro dia
47 e que em seu nome se pregasse arrependimento para remissão de pecados a todas as nações, começando de Jerusalém.
48 Vós sois testemunhas destas coisas.
49 Eis que envio sobre vós a promessa de meu Pai; permanecei, pois, na cidade, até que do alto sejais revestidos de poder.
50 Então, os levou para Betânia e, erguendo as mãos, os abençoou.
51 Aconteceu que, enquanto os abençoava, ia-se retirando deles, sendo elevado para o céu.
52 Então, eles, adorando-o, voltaram para Jerusalém, tomados de grande júbilo;
53 e estavam sempre no templo, louvando a Deus.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Lucas','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)