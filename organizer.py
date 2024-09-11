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
1 Livro da genealogia de Jesus Cristo, filho de Davi, filho de Abraão.
2 Abraão gerou a Isaque; Isaque, a Jacó; Jacó, a Judá e a seus irmãos;
3 Judá gerou de Tamar a Perez e a Zera; Perez gerou a Esrom; Esrom, a Arão;
4 Arão gerou a Aminadabe; Aminadabe, a Naassom; Naassom, a Salmom;
5 Salmom gerou de Raabe a Boaz; este, de Rute, gerou a Obede; e Obede, a Jessé;
6 Jessé gerou ao rei Davi; e o rei Davi, a Salomão, da que fora mulher de Urias;
7 Salomão gerou a Roboão; Roboão, a Abias; Abias, a Asa;
8 Asa gerou a Josafá; Josafá, a Jorão; Jorão, a Uzias;
9 Uzias gerou a Jotão; Jotão, a Acaz; Acaz, a Ezequias;
10 Ezequias gerou a Manassés; Manassés, a Amom; Amom, a Josias;
11 Josias gerou a Jeconias e a seus irmãos, no tempo do exílio na Babilônia.
12 Depois do exílio na Babilônia, Jeconias gerou a Salatiel; e Salatiel, a Zorobabel;
13 Zorobabel gerou a Abiúde; Abiúde, a Eliaquim; Eliaquim, a Azor;
14 Azor gerou a Sadoque; Sadoque, a Aquim; Aquim, a Eliúde;
15 Eliúde gerou a Eleazar; Eleazar, a Matã; Matã, a Jacó.
16 E Jacó gerou a José, marido de Maria, da qual nasceu Jesus, que se chama o Cristo.
17 De sorte que todas as gerações, desde Abraão até Davi, são catorze; desde Davi até ao exílio na Babilônia, catorze; e desde o exílio na Babilônia até Cristo, catorze.
18 Ora, o nascimento de Jesus Cristo foi assim: estando Maria, sua mãe, desposada com José, sem que tivessem antes coabitado, achou-se grávida pelo Espírito Santo.
19 Mas José, seu esposo, sendo justo e não a querendo infamar, resolveu deixá-la secretamente.
20 Enquanto ponderava nestas coisas, eis que lhe apareceu, em sonho, um anjo do Senhor, dizendo: José, filho de Davi, não temas receber Maria, tua mulher, porque o que nela foi gerado é do Espírito Santo.
21 Ela dará à luz um filho e lhe porás o nome de Jesus, porque ele salvará o seu povo dos pecados deles.
22 Ora, tudo isto aconteceu para que se cumprisse o que fora dito pelo Senhor por intermédio do profeta:
23 Eis que a virgem conceberá e dará à luz um filho, e ele será chamado pelo nome de Emanuel (que quer dizer: Deus conosco).
24 Despertado José do sono, fez como lhe ordenara o anjo do Senhor e recebeu sua mulher.
25 Contudo, não a conheceu, enquanto ela não deu à luz um filho, a quem pôs o nome de Jesus.*
1 Tendo Jesus nascido em Belém da Judeia, em dias do rei Herodes, eis que vieram uns magos do Oriente a Jerusalém.
2 E perguntavam: Onde está o recém-nascido Rei dos judeus? Porque vimos a sua estrela no Oriente e viemos para adorá-lo.
3 Tendo ouvido isso, alarmou-se o rei Herodes, e, com ele, toda a Jerusalém;
4 então, convocando todos os principais sacerdotes e escribas do povo, indagava deles onde o Cristo deveria nascer.
5 Em Belém da Judeia, responderam eles, porque assim está escrito por intermédio do profeta:
6 E tu, Belém, terra de Judá, não és de modo algum a menor entre as principais de Judá; porque de ti sairá o Guia que há de apascentar a meu povo, Israel.
7 Com isto, Herodes, tendo chamado secretamente os magos, inquiriu deles com precisão quanto ao tempo em que a estrela aparecera.
8 E, enviando-os a Belém, disse-lhes: Ide informar-vos cuidadosamente a respeito do menino; e, quando o tiverdes encontrado, avisai-me, para eu também ir adorá-lo.
9 Depois de ouvirem o rei, partiram; e eis que a estrela que viram no Oriente os precedia, até que, chegando, parou sobre onde estava o menino.
10 E, vendo eles a estrela, alegraram-se com grande e intenso júbilo.
11 Entrando na casa, viram o menino com Maria, sua mãe. Prostrando-se, o adoraram; e, abrindo os seus tesouros, entregaram-lhe suas ofertas: ouro, incenso e mirra.
12 Sendo por divina advertência prevenidos em sonho para não voltarem à presença de Herodes, regressaram por outro caminho a sua terra.
13 Tendo eles partido, eis que apareceu um anjo do Senhor a José, em sonho, e disse: Dispõe-te, toma o menino e sua mãe, foge para o Egito e permanece lá até que eu te avise; porque Herodes há de procurar o menino para o matar.
14 Dispondo-se ele, tomou de noite o menino e sua mãe e partiu para o Egito;
15 e lá ficou até à morte de Herodes, para que se cumprisse o que fora dito pelo Senhor, por intermédio do profeta: Do Egito chamei o meu Filho.
16 Vendo-se iludido pelos magos, enfureceu-se Herodes grandemente e mandou matar todos os meninos de Belém e de todos os seus arredores, de dois anos para baixo, conforme o tempo do qual com precisão se informara dos magos.
17 Então, se cumpriu o que fora dito por intermédio do profeta Jeremias:
18 Ouviu-se um clamor em Ramá, pranto, [choro] e grande lamento; era Raquel chorando por seus filhos e inconsolável porque não mais existem.
19 Tendo Herodes morrido, eis que um anjo do Senhor apareceu em sonho a José, no Egito, e disse-lhe:
20 Dispõe-te, toma o menino e sua mãe e vai para a terra de Israel; porque já morreram os que atentavam contra a vida do menino.
21 Dispôs-se ele, tomou o menino e sua mãe e regressou para a terra de Israel.
22 Tendo, porém, ouvido que Arquelau reinava na Judeia em lugar de seu pai Herodes, temeu ir para lá; e, por divina advertência prevenido em sonho, retirou-se para as regiões da Galileia.
23 E foi habitar numa cidade chamada Nazaré, para que se cumprisse o que fora dito por intermédio dos profetas: Ele será chamado Nazareno.*
1 Naqueles dias, apareceu João Batista pregando no deserto da Judeia e dizia:
2 Arrependei-vos, porque está próximo o reino dos céus.
3 Porque este é o referido por intermédio do profeta Isaías: Voz do que clama no deserto: Preparai o caminho do Senhor, endireitai as suas veredas.
4 Usava João vestes de pelos de camelo e um cinto de couro; a sua alimentação eram gafanhotos e mel silvestre.
5 Então, saíam a ter com ele Jerusalém, toda a Judeia e toda a circunvizinhança do Jordão;
6 e eram por ele batizados no rio Jordão, confessando os seus pecados.
7 Vendo ele, porém, que muitos fariseus e saduceus vinham ao batismo, disse-lhes: Raça de víboras, quem vos induziu a fugir da ira vindoura?
8 Produzi, pois, frutos dignos de arrependimento;
9 e não comeceis a dizer entre vós mesmos: Temos por pai a Abraão; porque eu vos afirmo que destas pedras Deus pode suscitar filhos a Abraão.
10 Já está posto o machado à raiz das árvores; toda árvore, pois, que não produz bom fruto é cortada e lançada ao fogo.
11 Eu vos batizo com água, para arrependimento; mas aquele que vem depois de mim é mais poderoso do que eu, cujas sandálias não sou digno de levar. Ele vos batizará com o Espírito Santo e com fogo.
12 A sua pá, ele a tem na mão e limpará completamente a sua eira; recolherá o seu trigo no celeiro, mas queimará a palha em fogo inextinguível.
13 Por esse tempo, dirigiu-se Jesus da Galileia para o Jordão, a fim de que João o batizasse.
14 Ele, porém, o dissuadia, dizendo: Eu é que preciso ser batizado por ti, e tu vens a mim?
15 Mas Jesus lhe respondeu: Deixa por enquanto, porque, assim, nos convém cumprir toda a justiça. Então, ele o admitiu.
16 Batizado Jesus, saiu logo da água, e eis que se lhe abriram os céus, e viu o Espírito de Deus descendo como pomba, vindo sobre ele.
17 E eis uma voz dos céus, que dizia: Este é o meu Filho amado, em quem me comprazo.*
1 A seguir, foi Jesus levado pelo Espírito ao deserto, para ser tentado pelo diabo.
2 E, depois de jejuar quarenta dias e quarenta noites, teve fome.
3 Então, o tentador, aproximando-se, lhe disse: Se és Filho de Deus, manda que estas pedras se transformem em pães.
4 Jesus, porém, respondeu: Está escrito: Não só de pão viverá o homem, mas de toda palavra que procede da boca de Deus.
5 Então, o diabo o levou à Cidade Santa, colocou-o sobre o pináculo do templo
6 e lhe disse: Se és Filho de Deus, atira-te abaixo, porque está escrito: Aos seus anjos ordenará a teu respeito que te guardem; e: Eles te susterão nas suas mãos, para não tropeçares nalguma pedra.
7 Respondeu-lhe Jesus: Também está escrito: Não tentarás o Senhor, teu Deus.
8 Levou-o ainda o diabo a um monte muito alto, mostrou-lhe todos os reinos do mundo e a glória deles
9 e lhe disse: Tudo isto te darei se, prostrado, me adorares.
10 Então, Jesus lhe ordenou: Retira-te, Satanás, porque está escrito: Ao Senhor, teu Deus, adorarás, e só a ele darás culto.
11 Com isto, o deixou o diabo, e eis que vieram anjos e o serviram.
12 Ouvindo, porém, Jesus que João fora preso, retirou-se para a Galileia;
13 e, deixando Nazaré, foi morar em Cafarnaum, situada à beira-mar, nos confins de Zebulom e Naftali;
14 para que se cumprisse o que fora dito por intermédio do profeta Isaías:
15 Terra de Zebulom, terra de Naftali, caminho do mar, além do Jordão, Galileia dos gentios!
16 O povo que jazia em trevas viu grande luz, e aos que viviam na região e sombra da morte resplandeceu-lhes a luz.
17 Daí por diante, passou Jesus a pregar e a dizer: Arrependei-vos, porque está próximo o reino dos céus.
18 Caminhando junto ao mar da Galileia, viu dois irmãos, Simão, chamado Pedro, e André, que lançavam as redes ao mar, porque eram pescadores.
19 E disse-lhes: Vinde após mim, e eu vos farei pescadores de homens.
20 Então, eles deixaram imediatamente as redes e o seguiram.
21 Passando adiante, viu outros dois irmãos, Tiago, filho de Zebedeu, e João, seu irmão, que estavam no barco em companhia de seu pai, consertando as redes; e chamou-os.
22 Então, eles, no mesmo instante, deixando o barco e seu pai, o seguiram.
Jesus prega por toda a Galileia e cura muitos enfermos
23 Percorria Jesus toda a Galileia, ensinando nas sinagogas, pregando o evangelho do reino e curando toda sorte de doenças e enfermidades entre o povo.
24 E a sua fama correu por toda a Síria; trouxeram-lhe, então, todos os doentes, acometidos de várias enfermidades e tormentos: endemoninhados, lunáticos e paralíticos. E ele os curou.
25 E da Galileia, Decápolis, Jerusalém, Judeia e dalém do Jordão numerosas multidões o seguiam.*
1 Vendo Jesus as multidões, subiu ao monte, e, como se assentasse, aproximaram-se os seus discípulos;
2 e ele passou a ensiná-los, dizendo:
3 Bem-aventurados os humildes de espírito, porque deles é o reino dos céus.
4 Bem-aventurados os que choram, porque serão consolados.
5 Bem-aventurados os mansos, porque herdarão a terra.
6 Bem-aventurados os que têm fome e sede de justiça, porque serão fartos.
7 Bem-aventurados os misericordiosos, porque alcançarão misericórdia.
8 Bem-aventurados os limpos de coração, porque verão a Deus.
9 Bem-aventurados os pacificadores, porque serão chamados filhos de Deus.
10 Bem-aventurados os perseguidos por causa da justiça, porque deles é o reino dos céus.
11 Bem-aventurados sois quando, por minha causa, vos injuriarem, e vos perseguirem, e, mentindo, disserem todo mal contra vós.
12 Regozijai-vos e exultai, porque é grande o vosso galardão nos céus; pois assim perseguiram aos profetas que viveram antes de vós.
13 Vós sois o sal da terra; ora, se o sal vier a ser insípido, como lhe restaurar o sabor? Para nada mais presta senão para, lançado fora, ser pisado pelos homens.
14 Vós sois a luz do mundo. Não se pode esconder a cidade edificada sobre um monte;
15 nem se acende uma candeia para colocá-la debaixo do alqueire, mas no velador, e alumia a todos os que se encontram na casa.
16 Assim brilhe também a vossa luz diante dos homens, para que vejam as vossas boas obras e glorifiquem a vosso Pai que está nos céus.
17 Não penseis que vim revogar a Lei ou os Profetas; não vim para revogar, vim para cumprir.
18 Porque em verdade vos digo: até que o céu e a terra passem, nem um i ou um til jamais passará da Lei, até que tudo se cumpra.
19 Aquele, pois, que violar um destes mandamentos, posto que dos menores, e assim ensinar aos homens, será considerado mínimo no reino dos céus; aquele, porém, que os observar e ensinar, esse será considerado grande no reino dos céus.
20 Porque vos digo que, se a vossa justiça não exceder em muito a dos escribas e fariseus, jamais entrareis no reino dos céus.
21 Ouvistes que foi dito aos antigos: Não matarás; e: Quem matar estará sujeito a julgamento.
22 Eu, porém, vos digo que todo aquele que [sem motivo] se irar contra seu irmão estará sujeito a julgamento; e quem proferir um insulto a seu irmão estará sujeito a julgamento do tribunal; e quem lhe chamar: Tolo, estará sujeito ao inferno de fogo.
23 Se, pois, ao trazeres ao altar a tua oferta, ali te lembrares de que teu irmão tem alguma coisa contra ti,
24 deixa perante o altar a tua oferta, vai primeiro reconciliar-te com teu irmão; e, então, voltando, faze a tua oferta.
25 Entra em acordo sem demora com o teu adversário, enquanto estás com ele a caminho, para que o adversário não te entregue ao juiz, o juiz, ao oficial de justiça, e sejas recolhido à prisão.
26 Em verdade te digo que não sairás dali, enquanto não pagares o último centavo.
27 Ouvistes que foi dito: Não adulterarás.
28 Eu, porém, vos digo: qualquer que olhar para uma mulher com intenção impura, no coração, já adulterou com ela.
29 Se o teu olho direito te faz tropeçar, arranca-o e lança-o de ti; pois te convém que se perca um dos teus membros, e não seja todo o teu corpo lançado no inferno.
30 E, se a tua mão direita te faz tropeçar, corta-a e lança-a de ti; pois te convém que se perca um dos teus membros, e não vá todo o teu corpo para o inferno.
31 Também foi dito: Aquele que repudiar sua mulher, dê-lhe carta de divórcio.
32 Eu, porém, vos digo: qualquer que repudiar sua mulher, exceto em caso de relações sexuais ilícitas, a expõe a tornar-se adúltera; e aquele que casar com a repudiada comete adultério.
33 Também ouvistes que foi dito aos antigos: Não jurarás falso, mas cumprirás rigorosamente para com o Senhor os teus juramentos.
34 Eu, porém, vos digo: de modo algum jureis; nem pelo céu, por ser o trono de Deus;
35 nem pela terra, por ser estrado de seus pés; nem por Jerusalém, por ser cidade do grande Rei;
36 nem jures pela tua cabeça, porque não podes tornar um cabelo branco ou preto.
37 Seja, porém, a tua palavra: Sim, sim; não, não. O que disto passar vem do maligno.
38 Ouvistes que foi dito: Olho por olho, dente por dente.
39 Eu, porém, vos digo: não resistais ao perverso; mas, a qualquer que te ferir na face direita, volta-lhe também a outra;
40 e, ao que quer demandar contigo e tirar-te a túnica, deixa-lhe também a capa.
41 Se alguém te obrigar a andar uma milha, vai com ele duas.
42 Dá a quem te pede e não voltes as costas ao que deseja que lhe emprestes.
43 Ouvistes que foi dito: Amarás o teu próximo e odiarás o teu inimigo.
44 Eu, porém, vos digo: amai os vossos inimigos e orai pelos que vos perseguem;
45 para que vos torneis filhos do vosso Pai celeste, porque ele faz nascer o seu sol sobre maus e bons e vir chuvas sobre justos e injustos.
46 Porque, se amardes os que vos amam, que recompensa tendes? Não fazem os publicanos também o mesmo?
47 E, se saudardes somente os vossos irmãos, que fazeis de mais? Não fazem os gentios também o mesmo?
48 Portanto, sede vós perfeitos como perfeito é o vosso Pai celeste.*
1 Guardai-vos de exercer a vossa justiça diante dos homens, com o fim de serdes vistos por eles; doutra sorte, não tereis galardão junto de vosso Pai celeste.
2 Quando, pois, deres esmola, não toques trombeta diante de ti, como fazem os hipócritas, nas sinagogas e nas ruas, para serem glorificados pelos homens. Em verdade vos digo que eles já receberam a recompensa.
3 Tu, porém, ao dares a esmola, ignore a tua mão esquerda o que faz a tua mão direita;
4 para que a tua esmola fique em secreto; e teu Pai, que vê em secreto, te recompensará.
5 E, quando orardes, não sereis como os hipócritas; porque gostam de orar em pé nas sinagogas e nos cantos das praças, para serem vistos dos homens. Em verdade vos digo que eles já receberam a recompensa.
6 Tu, porém, quando orares, entra no teu quarto e, fechada a porta, orarás a teu Pai, que está em secreto; e teu Pai, que vê em secreto, te recompensará.
7 E, orando, não useis de vãs repetições, como os gentios; porque presumem que pelo seu muito falar serão ouvidos.
8 Não vos assemelheis, pois, a eles; porque Deus, o vosso Pai, sabe o de que tendes necessidade, antes que lho peçais.
9 Portanto, vós orareis assim: Pai nosso, que estás nos céus, santificado seja o teu nome;
10 venha o teu reino; faça-se a tua vontade, assim na terra como no céu;
11 o pão nosso de cada dia dá-nos hoje;
12 e perdoa-nos as nossas dívidas, assim como nós temos perdoado aos nossos devedores;
13 e não nos deixes cair em tentação; mas livra-nos do mal [pois teu é o reino, o poder e a glória para sempre. Amém]!
14 Porque, se perdoardes aos homens as suas ofensas, também vosso Pai celeste vos perdoará;
15 se, porém, não perdoardes aos homens [as suas ofensas], tampouco vosso Pai vos perdoará as vossas ofensas.
16 Quando jejuardes, não vos mostreis contristados como os hipócritas; porque desfiguram o rosto com o fim de parecer aos homens que jejuam. Em verdade vos digo que eles já receberam a recompensa.
17 Tu, porém, quando jejuares, unge a cabeça e lava o rosto,
18 com o fim de não parecer aos homens que jejuas, e sim ao teu Pai, em secreto; e teu Pai, que vê em secreto, te recompensará.
19 Não acumuleis para vós outros tesouros sobre a terra, onde a traça e a ferrugem corroem e onde ladrões escavam e roubam;
20 mas ajuntai para vós outros tesouros no céu, onde traça nem ferrugem corrói, e onde ladrões não escavam, nem roubam;
21 porque, onde está o teu tesouro, aí estará também o teu coração.
22 São os olhos a lâmpada do corpo. Se os teus olhos forem bons, todo o teu corpo será luminoso;
23 se, porém, os teus olhos forem maus, todo o teu corpo estará em trevas. Portanto, caso a luz que em ti há sejam trevas, que grandes trevas serão!
24 Ninguém pode servir a dois senhores; porque ou há de aborrecer-se de um e amar ao outro, ou se devotará a um e desprezará ao outro. Não podeis servir a Deus e às riquezas.
25 Por isso, vos digo: não andeis ansiosos pela vossa vida, quanto ao que haveis de comer ou beber; nem pelo vosso corpo, quanto ao que haveis de vestir. Não é a vida mais do que o alimento, e o corpo, mais do que as vestes?
26 Observai as aves do céu: não semeiam, não colhem, nem ajuntam em celeiros; contudo, vosso Pai celeste as sustenta. Porventura, não valeis vós muito mais do que as aves?
27 Qual de vós, por ansioso que esteja, pode acrescentar um côvado ao curso da sua vida?
28 E por que andais ansiosos quanto ao vestuário? Considerai como crescem os lírios do campo: eles não trabalham, nem fiam.
29 Eu, contudo, vos afirmo que nem Salomão, em toda a sua glória, se vestiu como qualquer deles.
30 Ora, se Deus veste assim a erva do campo, que hoje existe e amanhã é lançada no forno, quanto mais a vós outros, homens de pequena fé?
31 Portanto, não vos inquieteis, dizendo: Que comeremos? Que beberemos? Ou: Com que nos vestiremos?
32 Porque os gentios é que procuram todas estas coisas; pois vosso Pai celeste sabe que necessitais de todas elas;
33 buscai, pois, em primeiro lugar, o seu reino e a sua justiça, e todas estas coisas vos serão acrescentadas.
34 Portanto, não vos inquieteis com o dia de amanhã, pois o amanhã trará os seus cuidados; basta ao dia o seu próprio mal.*
1 Não julgueis, para que não sejais julgados.
2 Pois, com o critério com que julgardes, sereis julgados; e, com a medida com que tiverdes medido, vos medirão também.
3 Por que vês tu o argueiro no olho de teu irmão, porém não reparas na trave que está no teu próprio?
4 Ou como dirás a teu irmão: Deixa-me tirar o argueiro do teu olho, quando tens a trave no teu?
5 Hipócrita! Tira primeiro a trave do teu olho e, então, verás claramente para tirar o argueiro do olho de teu irmão.
6 Não deis aos cães o que é santo, nem lanceis ante os porcos as vossas pérolas, para que não as pisem com os pés e, voltando-se, vos dilacerem.
7 Pedi, e dar-se-vos-á; buscai e achareis; batei, e abrir-se-vos-á.
8 Pois todo o que pede recebe; o que busca encontra; e, a quem bate, abrir-se-lhe-á.
9 Ou qual dentre vós é o homem que, se porventura o filho lhe pedir pão, lhe dará pedra?
10 Ou, se lhe pedir um peixe, lhe dará uma cobra?
11 Ora, se vós, que sois maus, sabeis dar boas dádivas aos vossos filhos, quanto mais vosso Pai, que está nos céus, dará boas coisas aos que lhe pedirem?
12 Tudo quanto, pois, quereis que os homens vos façam, assim fazei-o vós também a eles; porque esta é a Lei e os Profetas.
13 Entrai pela porta estreita (larga é a porta, e espaçoso, o caminho que conduz para a perdição, e são muitos os que entram por ela),
14 porque estreita é a porta, e apertado, o caminho que conduz para a vida, e são poucos os que acertam com ela.
15 Acautelai-vos dos falsos profetas, que se vos apresentam disfarçados em ovelhas, mas por dentro são lobos roubadores.
16 Pelos seus frutos os conhecereis. Colhem-se, porventura, uvas dos espinheiros ou figos dos abrolhos?
17 Assim, toda árvore boa produz bons frutos, porém a árvore má produz frutos maus.
18 Não pode a árvore boa produzir frutos maus, nem a árvore má produzir frutos bons.
19 Toda árvore que não produz bom fruto é cortada e lançada ao fogo.
20 Assim, pois, pelos seus frutos os conhecereis.
21 Nem todo o que me diz: Senhor, Senhor! entrará no reino dos céus, mas aquele que faz a vontade de meu Pai, que está nos céus.
22 Muitos, naquele dia, hão de dizer-me: Senhor, Senhor! Porventura, não temos nós profetizado em teu nome, e em teu nome não expelimos demônios, e em teu nome não fizemos muitos milagres?
23 Então, lhes direi explicitamente: nunca vos conheci. Apartai-vos de mim, os que praticais a iniquidade.
24 Todo aquele, pois, que ouve estas minhas palavras e as pratica será comparado a um homem prudente que edificou a sua casa sobre a rocha;
25 e caiu a chuva, transbordaram os rios, sopraram os ventos e deram com ímpeto contra aquela casa, que não caiu, porque fora edificada sobre a rocha.
26 E todo aquele que ouve estas minhas palavras e não as pratica será comparado a um homem insensato que edificou a sua casa sobre a areia;
27 e caiu a chuva, transbordaram os rios, sopraram os ventos e deram com ímpeto contra aquela casa, e ela desabou, sendo grande a sua ruína.
28 Quando Jesus acabou de proferir estas palavras, estavam as multidões maravilhadas da sua doutrina;
29 porque ele as ensinava como quem tem autoridade e não como os escribas.*
1 Ora, descendo ele do monte, grandes multidões o seguiram.
2 E eis que um leproso, tendo-se aproximado, adorou-o, dizendo: Senhor, se quiseres, podes purificar-me.
3 E Jesus, estendendo a mão, tocou-lhe, dizendo: Quero, fica limpo! E imediatamente ele ficou limpo da sua lepra.
4 Disse-lhe, então, Jesus: Olha, não o digas a ninguém, mas vai mostrar-te ao sacerdote e fazer a oferta que Moisés ordenou, para servir de testemunho ao povo.
5 Tendo Jesus entrado em Cafarnaum, apresentou-se-lhe um centurião, implorando:
6 Senhor, o meu criado jaz em casa, de cama, paralítico, sofrendo horrivelmente.
7 Jesus lhe disse: Eu irei curá-lo.
8 Mas o centurião respondeu: Senhor, não sou digno de que entres em minha casa; mas apenas manda com uma palavra, e o meu rapaz será curado.
9 Pois também eu sou homem sujeito à autoridade, tenho soldados às minhas ordens e digo a este: vai, e ele vai; e a outro: vem, e ele vem; e ao meu servo: faze isto, e ele o faz.
10 Ouvindo isto, admirou-se Jesus e disse aos que o seguiam: Em verdade vos afirmo que nem mesmo em Israel achei fé como esta.
11 Digo-vos que muitos virão do Oriente e do Ocidente e tomarão lugares à mesa com Abraão, Isaque e Jacó no reino dos céus.
12 Ao passo que os filhos do reino serão lançados para fora, nas trevas; ali haverá choro e ranger de dentes.
13 Então, disse Jesus ao centurião: Vai-te, e seja feito conforme a tua fé. E, naquela mesma hora, o servo foi curado.
14 Tendo Jesus chegado à casa de Pedro, viu a sogra deste acamada e ardendo em febre.
15 Mas Jesus tomou-a pela mão, e a febre a deixou. Ela se levantou e passou a servi-lo.
16 Chegada a tarde, trouxeram-lhe muitos endemoninhados; e ele meramente com a palavra expeliu os espíritos e curou todos os que estavam doentes;
17 para que se cumprisse o que fora dito por intermédio do profeta Isaías: Ele mesmo tomou as nossas enfermidades e carregou com as nossas doenças.
18 Vendo Jesus muita gente ao seu redor, ordenou que passassem para a outra margem.
19 Então, aproximando-se dele um escriba, disse-lhe: Mestre, seguir-te-ei para onde quer que fores.
20 Mas Jesus lhe respondeu: As raposas têm seus covis, e as aves do céu, ninhos; mas o Filho do Homem não tem onde reclinar a cabeça.
21 E outro dos discípulos lhe disse: Senhor, permite-me ir primeiro sepultar meu pai.
22 Replicou-lhe, porém, Jesus: Segue-me, e deixa aos mortos o sepultar os seus próprios mortos.
23 Então, entrando ele no barco, seus discípulos o seguiram.
24 E eis que sobreveio no mar uma grande tempestade, de sorte que o barco era varrido pelas ondas. Entretanto, Jesus dormia.
25 Mas os discípulos vieram acordá-lo, clamando: Senhor, salva-nos! Perecemos!
26 Perguntou-lhes, então, Jesus: Por que sois tímidos, homens de pequena fé? E, levantando-se, repreendeu os ventos e o mar; e fez-se grande bonança.
27 E maravilharam-se os homens, dizendo: Quem é este que até os ventos e o mar lhe obedecem?
28 Tendo ele chegado à outra margem, à terra dos gadarenos, vieram-lhe ao encontro dois endemoninhados, saindo dentre os sepulcros, e a tal ponto furiosos, que ninguém podia passar por aquele caminho.
29 E eis que gritaram: Que temos nós contigo, ó Filho de Deus! Vieste aqui atormentar-nos antes do tempo?
30 Ora, andava pastando, não longe deles, uma grande manada de porcos.
31 Então, os demônios lhe rogavam: Se nos expeles, manda-nos para a manada de porcos.
32 Pois ide, ordenou-lhes Jesus. E eles, saindo, passaram para os porcos; e eis que toda a manada se precipitou, despenhadeiro abaixo, para dentro do mar, e nas águas pereceram.
33 Fugiram os porqueiros e, chegando à cidade, contaram todas estas coisas e o que acontecera aos endemoninhados.
34 Então, a cidade toda saiu para encontrar-se com Jesus; e, vendo-o, lhe rogaram que se retirasse da terra deles.*
1 Entrando Jesus num barco, passou para o outro lado e foi para a sua própria cidade.
2 E eis que lhe trouxeram um paralítico deitado num leito. Vendo-lhes a fé, Jesus disse ao paralítico: Tem bom ânimo, filho; estão perdoados os teus pecados.
3 Mas alguns escribas diziam consigo: Este blasfema.
4 Jesus, porém, conhecendo-lhes os pensamentos, disse: Por que cogitais o mal no vosso coração?
5 Pois qual é mais fácil? Dizer: Estão perdoados os teus pecados, ou dizer: Levanta-te e anda?
6 Ora, para que saibais que o Filho do Homem tem sobre a terra autoridade para perdoar pecados — disse, então, ao paralítico: Levanta-te, toma o teu leito e vai para tua casa.
7 E, levantando-se, partiu para sua casa.
8 Vendo isto, as multidões, possuídas de temor, glorificaram a Deus, que dera tal autoridade aos homens.
9 Partindo Jesus dali, viu um homem chamado Mateus sentado na coletoria e disse-lhe: Segue-me! Ele se levantou e o seguiu.
10 E sucedeu que, estando ele em casa, à mesa, muitos publicanos e pecadores vieram e tomaram lugares com Jesus e seus discípulos.
11 Ora, vendo isto, os fariseus perguntavam aos discípulos: Por que come o vosso Mestre com os publicanos e pecadores?
12 Mas Jesus, ouvindo, disse: Os sãos não precisam de médico, e sim os doentes.
13 Ide, porém, e aprendei o que significa: Misericórdia quero e não holocaustos; pois não vim chamar justos, e sim pecadores [ao arrependimento].
14 Vieram, depois, os discípulos de João e lhe perguntaram: Por que jejuamos nós, e os fariseus [muitas vezes], e teus discípulos não jejuam?
15 Respondeu-lhes Jesus: Podem, acaso, estar tristes os convidados para o casamento, enquanto o noivo está com eles? Dias virão, contudo, em que lhes será tirado o noivo, e nesses dias hão de jejuar.
16 Ninguém põe remendo de pano novo em veste velha; porque o remendo tira parte da veste, e fica maior a rotura.
17 Nem se põe vinho novo em odres velhos; do contrário, rompem-se os odres, derrama-se o vinho, e os odres se perdem. Mas põe-se vinho novo em odres novos, e ambos se conservam.
18 Enquanto estas coisas lhes dizia, eis que um chefe, aproximando-se, o adorou e disse: Minha filha faleceu agora mesmo; mas vem, impõe a mão sobre ela, e viverá.
19 E Jesus, levantando-se, o seguia, e também os seus discípulos.
20 E eis que uma mulher, que durante doze anos vinha padecendo de uma hemorragia, veio por trás dele e lhe tocou na orla da veste;
21 porque dizia consigo mesma: Se eu apenas lhe tocar a veste, ficarei curada.
22 E Jesus, voltando-se e vendo-a, disse: Tem bom ânimo, filha, a tua fé te salvou. E, desde aquele instante, a mulher ficou sã.
23 Tendo Jesus chegado à casa do chefe e vendo os tocadores de flauta e o povo em alvoroço, disse:
24 Retirai-vos, porque não está morta a menina, mas dorme. E riam-se dele.
25 Mas, afastado o povo, entrou Jesus, tomou a menina pela mão, e ela se levantou.
26 E a fama deste acontecimento correu por toda aquela terra.
27 Partindo Jesus dali, seguiram-no dois cegos, clamando: Tem compaixão de nós, Filho de Davi!
28 Tendo ele entrado em casa, aproximaram-se os cegos, e Jesus lhes perguntou: Credes que eu posso fazer isso? Responderam-lhe: Sim, Senhor!
29 Então, lhes tocou os olhos, dizendo: Faça-se-vos conforme a vossa fé.
30 E abriram-se-lhes os olhos. Jesus, porém, os advertiu severamente, dizendo: Acautelai-vos de que ninguém o saiba.
31 Saindo eles, porém, divulgaram-lhe a fama por toda aquela terra.
32 Ao retirarem-se eles, foi-lhe trazido um mudo endemoninhado.
33 E, expelido o demônio, falou o mudo; e as multidões se admiravam, dizendo: Jamais se viu tal coisa em Israel!
34 Mas os fariseus murmuravam: Pelo maioral dos demônios é que expele os demônios.
35 E percorria Jesus todas as cidades e povoados, ensinando nas sinagogas, pregando o evangelho do reino e curando toda sorte de doenças e enfermidades.
36 Vendo ele as multidões, compadeceu-se delas, porque estavam aflitas e exaustas como ovelhas que não têm pastor.
37 E, então, se dirigiu a seus discípulos: A seara, na verdade, é grande, mas os trabalhadores são poucos.
38 Rogai, pois, ao Senhor da seara que mande trabalhadores para a sua seara.*
1 Tendo chamado os seus doze discípulos, deu-lhes Jesus autoridade sobre espíritos imundos para os expelir e para curar toda sorte de doenças e enfermidades.
2 Ora, os nomes dos doze apóstolos são estes: primeiro, Simão, por sobrenome Pedro, e André, seu irmão; Tiago, filho de Zebedeu, e João, seu irmão;
3 Filipe e Bartolomeu; Tomé e Mateus, o publicano; Tiago, filho de Alfeu, e Tadeu;
4 Simão, o Zelote, e Judas Iscariotes, que foi quem o traiu.
5 A estes doze enviou Jesus, dando-lhes as seguintes instruções: Não tomeis rumo aos gentios, nem entreis em cidade de samaritanos;
6 mas, de preferência, procurai as ovelhas perdidas da casa de Israel;
7 e, à medida que seguirdes, pregai que está próximo o reino dos céus.
8 Curai enfermos, ressuscitai mortos, purificai leprosos, expeli demônios; de graça recebestes, de graça dai.
9 Não vos provereis de ouro, nem de prata, nem de cobre nos vossos cintos;
10 nem de alforje para o caminho, nem de duas túnicas, nem de sandálias, nem de bordão; porque digno é o trabalhador do seu alimento.
11 E, em qualquer cidade ou povoado em que entrardes, indagai quem neles é digno; e aí ficai até vos retirardes.
12 Ao entrardes na casa, saudai-a;
13 se, com efeito, a casa for digna, venha sobre ela a vossa paz; se, porém, não o for, torne para vós outros a vossa paz.
14 Se alguém não vos receber, nem ouvir as vossas palavras, ao sairdes daquela casa ou daquela cidade, sacudi o pó dos vossos pés.
15 Em verdade vos digo que menos rigor haverá para Sodoma e Gomorra, no Dia do Juízo, do que para aquela cidade.
16 Eis que eu vos envio como ovelhas para o meio de lobos; sede, portanto, prudentes como as serpentes e símplices como as pombas.
17 E acautelai-vos dos homens; porque vos entregarão aos tribunais e vos açoitarão nas suas sinagogas;
18 por minha causa sereis levados à presença de governadores e de reis, para lhes servir de testemunho, a eles e aos gentios.
19 E, quando vos entregarem, não cuideis em como ou o que haveis de falar, porque, naquela hora, vos será concedido o que haveis de dizer,
20 visto que não sois vós os que falais, mas o Espírito de vosso Pai é quem fala em vós.
21 Um irmão entregará à morte outro irmão, e o pai, ao filho; filhos haverá que se levantarão contra os progenitores e os matarão.
22 Sereis odiados de todos por causa do meu nome; aquele, porém, que perseverar até ao fim, esse será salvo.
23 Quando, porém, vos perseguirem numa cidade, fugi para outra; porque em verdade vos digo que não acabareis de percorrer as cidades de Israel, até que venha o Filho do Homem.
24 O discípulo não está acima do seu mestre, nem o servo, acima do seu senhor.
25 Basta ao discípulo ser como o seu mestre, e ao servo, como o seu senhor. Se chamaram Belzebu ao dono da casa, quanto mais aos seus domésticos?
26 Portanto, não os temais; pois nada há encoberto, que não venha a ser revelado; nem oculto, que não venha a ser conhecido.
27 O que vos digo às escuras, dizei-o a plena luz; e o que se vos diz ao ouvido, proclamai-o dos eirados.
28 Não temais os que matam o corpo e não podem matar a alma; temei, antes, aquele que pode fazer perecer no inferno tanto a alma como o corpo.
29 Não se vendem dois pardais por um asse? E nenhum deles cairá em terra sem o consentimento de vosso Pai.
30 E, quanto a vós outros, até os cabelos todos da cabeça estão contados.
31 Não temais, pois! Bem mais valeis vós do que muitos pardais.
32 Portanto, todo aquele que me confessar diante dos homens, também eu o confessarei diante de meu Pai, que está nos céus;
33 mas aquele que me negar diante dos homens, também eu o negarei diante de meu Pai, que está nos céus.
34 Não penseis que vim trazer paz à terra; não vim trazer paz, mas espada.
35 Pois vim causar divisão entre o homem e seu pai; entre a filha e sua mãe e entre a nora e sua sogra.
36 Assim, os inimigos do homem serão os da sua própria casa.
37 Quem ama seu pai ou sua mãe mais do que a mim não é digno de mim; quem ama seu filho ou sua filha mais do que a mim não é digno de mim;
38 e quem não toma a sua cruz e vem após mim não é digno de mim.
39 Quem acha a sua vida perdê-la-á; quem, todavia, perde a vida por minha causa achá-la-á.
40 Quem vos recebe a mim me recebe; e quem me recebe recebe aquele que me enviou.
41 Quem recebe um profeta, no caráter de profeta, receberá o galardão de profeta; quem recebe um justo, no caráter de justo, receberá o galardão de justo.
42 E quem der a beber, ainda que seja um copo de água fria, a um destes pequeninos, por ser este meu discípulo, em verdade vos digo que de modo algum perderá o seu galardão.*
1 Ora, tendo acabado Jesus de dar estas instruções a seus doze discípulos, partiu dali a ensinar e a pregar nas cidades deles.
2 Quando João ouviu, no cárcere, falar das obras de Cristo, mandou por seus discípulos perguntar-lhe:
3 És tu aquele que estava para vir ou havemos de esperar outro?
4 E Jesus, respondendo, disse-lhes: Ide e anunciai a João o que estais ouvindo e vendo:
5 os cegos veem, os coxos andam, os leprosos são purificados, os surdos ouvem, os mortos são ressuscitados, e aos pobres está sendo pregado o evangelho.
6 E bem-aventurado é aquele que não achar em mim motivo de tropeço.
7 Então, em partindo eles, passou Jesus a dizer ao povo a respeito de João: Que saístes a ver no deserto? Um caniço agitado pelo vento?
8 Sim, que saístes a ver? Um homem vestido de roupas finas? Ora, os que vestem roupas finas assistem nos palácios reais.
9 Mas para que saístes? Para ver um profeta? Sim, eu vos digo, e muito mais que profeta.
10 Este é de quem está escrito: Eis aí eu envio diante da tua face o meu mensageiro, o qual preparará o teu caminho diante de ti.
11 Em verdade vos digo: entre os nascidos de mulher, ninguém apareceu maior do que João Batista; mas o menor no reino dos céus é maior do que ele.
12 Desde os dias de João Batista até agora, o reino dos céus é tomado por esforço, e os que se esforçam se apoderam dele.
13 Porque todos os Profetas e a Lei profetizaram até João.
14 E, se o quereis reconhecer, ele mesmo é Elias, que estava para vir.
15 Quem tem ouvidos [para ouvir], ouça.
16 Mas a quem hei de comparar esta geração? É semelhante a meninos que, sentados nas praças, gritam aos companheiros:
17 Nós vos tocamos flauta, e não dançastes; entoamos lamentações, e não pranteastes.
18 Pois veio João, que não comia nem bebia, e dizem: Tem demônio!
19 Veio o Filho do Homem, que come e bebe, e dizem: Eis aí um glutão e bebedor de vinho, amigo de publicanos e pecadores! Mas a sabedoria é justificada por suas obras.
20 Passou, então, Jesus a increpar as cidades nas quais ele operara numerosos milagres, pelo fato de não se terem arrependido:
21 Ai de ti, Corazim! Ai de ti, Betsaida! Porque, se em Tiro e em Sidom se tivessem operado os milagres que em vós se fizeram, há muito que elas se teriam arrependido com pano de saco e cinza.
22 E, contudo, vos digo: no Dia do Juízo, haverá menos rigor para Tiro e Sidom do que para vós outras.
23 Tu, Cafarnaum, elevar-te-ás, porventura, até ao céu? Descerás até ao inferno; porque, se em Sodoma se tivessem operado os milagres que em ti se fizeram, teria ela permanecido até ao dia de hoje.
24 Digo-vos, porém, que menos rigor haverá, no Dia do Juízo, para com a terra de Sodoma do que para contigo.
25 Por aquele tempo, exclamou Jesus: Graças te dou, ó Pai, Senhor do céu e da terra, porque ocultaste estas coisas aos sábios e instruídos e as revelaste aos pequeninos.
26 Sim, ó Pai, porque assim foi do teu agrado.
27 Tudo me foi entregue por meu Pai. Ninguém conhece o Filho, senão o Pai; e ninguém conhece o Pai, senão o Filho e aquele a quem o Filho o quiser revelar.
28 Vinde a mim, todos os que estais cansados e sobrecarregados, e eu vos aliviarei.
29 Tomai sobre vós o meu jugo e aprendei de mim, porque sou manso e humilde de coração; e achareis descanso para a vossa alma.
30 Porque o meu jugo é suave, e o meu fardo é leve.*
1 Por aquele tempo, em dia de sábado, passou Jesus pelas searas. Ora, estando os seus discípulos com fome, entraram a colher espigas e a comer.
2 Os fariseus, porém, vendo isso, disseram-lhe: Eis que os teus discípulos fazem o que não é lícito fazer em dia de sábado.
3 Mas Jesus lhes disse: Não lestes o que fez Davi quando ele e seus companheiros tiveram fome?
4 Como entrou na Casa de Deus, e comeram os pães da proposição, os quais não lhes era lícito comer, nem a ele nem aos que com ele estavam, mas exclusivamente aos sacerdotes?
5 Ou não lestes na Lei que, aos sábados, os sacerdotes no templo violam o sábado e ficam sem culpa? Pois eu vos digo:
6 aqui está quem é maior que o templo.
7 Mas, se vós soubésseis o que significa: Misericórdia quero e não holocaustos, não teríeis condenado inocentes.
8 Porque o Filho do Homem é senhor do sábado.
9 Tendo Jesus partido dali, entrou na sinagoga deles.
10 Achava-se ali um homem que tinha uma das mãos ressequida; e eles, então, com o intuito de acusá-lo, perguntaram a Jesus: É lícito curar no sábado?
11 Ao que lhes respondeu: Qual dentre vós será o homem que, tendo uma ovelha, e, num sábado, esta cair numa cova, não fará todo o esforço, tirando-a dali?
12 Ora, quanto mais vale um homem que uma ovelha? Logo, é lícito, nos sábados, fazer o bem.
13 Então, disse ao homem: Estende a mão. Estendeu-a, e ela ficou sã como a outra.
14 Retirando-se, porém, os fariseus, conspiravam contra ele, sobre como lhe tirariam a vida.
15 Mas Jesus, sabendo disto, afastou-se dali. Muitos o seguiram, e a todos ele curou,
16 advertindo-lhes, porém, que o não expusessem à publicidade,
17 para se cumprir o que foi dito por intermédio do profeta Isaías:
18 Eis aqui o meu servo, que escolhi, o meu amado, em quem a minha alma se compraz. Farei repousar sobre ele o meu Espírito, e ele anunciará juízo aos gentios.
19 Não contenderá, nem gritará, nem alguém ouvirá nas praças a sua voz.
20 Não esmagará a cana quebrada, nem apagará a torcida que fumega, até que faça vencedor o juízo.
21 E, no seu nome, esperarão os gentios.
22 Então, lhe trouxeram um endemoninhado, cego e mudo; e ele o curou, passando o mudo a falar e a ver.
23 E toda a multidão se admirava e dizia: É este, porventura, o Filho de Davi?
24 Mas os fariseus, ouvindo isto, murmuravam: Este não expele demônios senão pelo poder de Belzebu, maioral dos demônios.
25 Jesus, porém, conhecendo-lhes os pensamentos, disse: Todo reino dividido contra si mesmo ficará deserto, e toda cidade ou casa dividida contra si mesma não subsistirá.
26 Se Satanás expele a Satanás, dividido está contra si mesmo; como, pois, subsistirá o seu reino?
27 E, se eu expulso demônios por Belzebu, por quem os expulsam vossos filhos? Por isso, eles mesmos serão os vossos juízes.
28 Se, porém, eu expulso demônios pelo Espírito de Deus, certamente é chegado o reino de Deus sobre vós.
29 Ou como pode alguém entrar na casa do valente e roubar-lhe os bens sem primeiro amarrá-lo? E, então, lhe saqueará a casa.
30 Quem não é por mim é contra mim; e quem comigo não ajunta espalha.
31 Por isso, vos declaro: todo pecado e blasfêmia serão perdoados aos homens; mas a blasfêmia contra o Espírito não será perdoada.
32 Se alguém proferir alguma palavra contra o Filho do Homem, ser-lhe-á isso perdoado; mas, se alguém falar contra o Espírito Santo, não lhe será isso perdoado, nem neste mundo nem no porvir.
33 Ou fazei a árvore boa e o seu fruto bom ou a árvore má e o seu fruto mau; porque pelo fruto se conhece a árvore.
34 Raça de víboras, como podeis falar coisas boas, sendo maus? Porque a boca fala do que está cheio o coração.
35 O homem bom tira do tesouro bom coisas boas; mas o homem mau do mau tesouro tira coisas más.
36 Digo-vos que de toda palavra frívola que proferirem os homens, dela darão conta no Dia do Juízo;
37 porque, pelas tuas palavras, serás justificado e, pelas tuas palavras, serás condenado.
38 Então, alguns escribas e fariseus replicaram: Mestre, queremos ver de tua parte algum sinal.
39 Ele, porém, respondeu: Uma geração má e adúltera pede um sinal; mas nenhum sinal lhe será dado, senão o do profeta Jonas.
40 Porque assim como esteve Jonas três dias e três noites no ventre do grande peixe, assim o Filho do Homem estará três dias e três noites no coração da terra.
41 Ninivitas se levantarão, no Juízo, com esta geração e a condenarão; porque se arrependeram com a pregação de Jonas. E eis aqui está quem é maior do que Jonas.
42 A rainha do Sul se levantará, no Juízo, com esta geração e a condenará; porque veio dos confins da terra para ouvir a sabedoria de Salomão. E eis aqui está quem é maior do que Salomão.
43 Quando o espírito imundo sai do homem, anda por lugares áridos procurando repouso, porém não encontra.
44 Por isso, diz: Voltarei para minha casa donde saí. E, tendo voltado, a encontra vazia, varrida e ornamentada.
45 Então, vai e leva consigo outros sete espíritos, piores do que ele, e, entrando, habitam ali; e o último estado daquele homem torna-se pior do que o primeiro. Assim também acontecerá a esta geração perversa.
46 Falava ainda Jesus ao povo, e eis que sua mãe e seus irmãos estavam do lado de fora, procurando falar-lhe.
47 E alguém lhe disse: Tua mãe e teus irmãos estão lá fora e querem falar-te.
48 Porém ele respondeu ao que lhe trouxera o aviso: Quem é minha mãe e quem são meus irmãos?
49 E, estendendo a mão para os discípulos, disse: Eis minha mãe e meus irmãos.
50 Porque qualquer que fizer a vontade de meu Pai celeste, esse é meu irmão, irmã e mãe.*
1 Naquele mesmo dia, saindo Jesus de casa, assentou-se à beira-mar;
2 e grandes multidões se reuniram perto dele, de modo que entrou num barco e se assentou; e toda a multidão estava em pé na praia.
3 E de muitas coisas lhes falou por parábolas e dizia: Eis que o semeador saiu a semear.
4 E, ao semear, uma parte caiu à beira do caminho, e, vindo as aves, a comeram.
5 Outra parte caiu em solo rochoso, onde a terra era pouca, e logo nasceu, visto não ser profunda a terra.
6 Saindo, porém, o sol, a queimou; e, porque não tinha raiz, secou-se.
7 Outra caiu entre os espinhos, e os espinhos cresceram e a sufocaram.
8 Outra, enfim, caiu em boa terra e deu fruto: a cem, a sessenta e a trinta por um.
9 Quem tem ouvidos [para ouvir], ouça.
10 Então, se aproximaram os discípulos e lhe perguntaram: Por que lhes falas por parábolas?
11 Ao que respondeu: Porque a vós outros é dado conhecer os mistérios do reino dos céus, mas àqueles não lhes é isso concedido.
12 Pois ao que tem se lhe dará, e terá em abundância; mas, ao que não tem, até o que tem lhe será tirado.
13 Por isso, lhes falo por parábolas; porque, vendo, não veem; e, ouvindo, não ouvem, nem entendem.
14 De sorte que neles se cumpre a profecia de Isaías: Ouvireis com os ouvidos e de nenhum modo entendereis; vereis com os olhos e de nenhum modo percebereis.
15 Porque o coração deste povo está endurecido, de mau grado ouviram com os ouvidos e fecharam os olhos; para não suceder que vejam com os olhos, ouçam com os ouvidos, entendam com o coração, se convertam e sejam por mim curados.
16 Bem-aventurados, porém, os vossos olhos, porque veem; e os vossos ouvidos, porque ouvem.
17 Pois em verdade vos digo que muitos profetas e justos desejaram ver o que vedes e não viram; e ouvir o que ouvis e não ouviram.
18 Atendei vós, pois, à parábola do semeador.
19 A todos os que ouvem a palavra do reino e não a compreendem, vem o maligno e arrebata o que lhes foi semeado no coração. Este é o que foi semeado à beira do caminho.
20 O que foi semeado em solo rochoso, esse é o que ouve a palavra e a recebe logo, com alegria;
21 mas não tem raiz em si mesmo, sendo, antes, de pouca duração; em lhe chegando a angústia ou a perseguição por causa da palavra, logo se escandaliza.
22 O que foi semeado entre os espinhos é o que ouve a palavra, porém os cuidados do mundo e a fascinação das riquezas sufocam a palavra, e fica infrutífera.
23 Mas o que foi semeado em boa terra é o que ouve a palavra e a compreende; este frutifica e produz a cem, a sessenta e a trinta por um.
24 Outra parábola lhes propôs, dizendo: O reino dos céus é semelhante a um homem que semeou boa semente no seu campo;
25 mas, enquanto os homens dormiam, veio o inimigo dele, semeou o joio no meio do trigo e retirou-se.
26 E, quando a erva cresceu e produziu fruto, apareceu também o joio.
27 Então, vindo os servos do dono da casa, lhe disseram: Senhor, não semeaste boa semente no teu campo? Donde vem, pois, o joio?
28 Ele, porém, lhes respondeu: Um inimigo fez isso. Mas os servos lhe perguntaram: Queres que vamos e arranquemos o joio?
29 Não! Replicou ele, para que, ao separar o joio, não arranqueis também com ele o trigo.
30 Deixai-os crescer juntos até à colheita, e, no tempo da colheita, direi aos ceifeiros: ajuntai primeiro o joio, atai-o em feixes para ser queimado; mas o trigo, recolhei-o no meu celeiro.
31 Outra parábola lhes propôs, dizendo: O reino dos céus é semelhante a um grão de mostarda, que um homem tomou e plantou no seu campo;
32 o qual é, na verdade, a menor de todas as sementes, e, crescida, é maior do que as hortaliças, e se faz árvore, de modo que as aves do céu vêm aninhar-se nos seus ramos.
33 Disse-lhes outra parábola: O reino dos céus é semelhante ao fermento que uma mulher tomou e escondeu em três medidas de farinha, até ficar tudo levedado.
34 Todas estas coisas disse Jesus às multidões por parábolas e sem parábolas nada lhes dizia;
35 para que se cumprisse o que foi dito por intermédio do profeta: Abrirei em parábolas a minha boca; publicarei coisas ocultas desde a criação [do mundo].
36 Então, despedindo as multidões, foi Jesus para casa. E, chegando-se a ele os seus discípulos, disseram: Explica-nos a parábola do joio do campo.
37 E ele respondeu: O que semeia a boa semente é o Filho do Homem;
38 o campo é o mundo; a boa semente são os filhos do reino; o joio são os filhos do maligno;
39 o inimigo que o semeou é o diabo; a ceifa é a consumação do século, e os ceifeiros são os anjos.
40 Pois, assim como o joio é colhido e lançado ao fogo, assim será na consumação do século.
41 Mandará o Filho do Homem os seus anjos, que ajuntarão do seu reino todos os escândalos e os que praticam a iniquidade
42 e os lançarão na fornalha acesa; ali haverá choro e ranger de dentes.
43 Então, os justos resplandecerão como o sol, no reino de seu Pai. Quem tem ouvidos [para ouvir], ouça.
44 O reino dos céus é semelhante a um tesouro oculto no campo, o qual certo homem, tendo-o achado, escondeu. E, transbordante de alegria, vai, vende tudo o que tem e compra aquele campo.
45 O reino dos céus é também semelhante a um que negocia e procura boas pérolas;
46 e, tendo achado uma pérola de grande valor, vende tudo o que possui e a compra.
47 O reino dos céus é ainda semelhante a uma rede que, lançada ao mar, recolhe peixes de toda espécie.
48 E, quando já está cheia, os pescadores arrastam-na para a praia e, assentados, escolhem os bons para os cestos e os ruins deitam fora.
49 Assim será na consumação do século: sairão os anjos, e separarão os maus dentre os justos,
50 e os lançarão na fornalha acesa; ali haverá choro e ranger de dentes.
51 Entendestes todas estas coisas? Responderam-lhe: Sim!
52 Então, lhes disse: Por isso, todo escriba versado no reino dos céus é semelhante a um pai de família que tira do seu depósito coisas novas e coisas velhas.
53 Tendo Jesus proferido estas parábolas, retirou-se dali.
54 E, chegando à sua terra, ensinava-os na sinagoga, de tal sorte que se maravilhavam e diziam: Donde lhe vêm esta sabedoria e estes poderes miraculosos?
55 Não é este o filho do carpinteiro? Não se chama sua mãe Maria, e seus irmãos, Tiago, José, Simão e Judas?
56 Não vivem entre nós todas as suas irmãs? Donde lhe vem, pois, tudo isto?
57 E escandalizavam-se nele. Jesus, porém, lhes disse: Não há profeta sem honra, senão na sua terra e na sua casa.
58 E não fez ali muitos milagres, por causa da incredulidade deles.*
1 Por aquele tempo, ouviu o tetrarca Herodes a fama de Jesus
2 e disse aos que o serviam: Este é João Batista; ele ressuscitou dos mortos, e, por isso, nele operam forças miraculosas.
3 Porque Herodes, havendo prendido e atado a João, o metera no cárcere, por causa de Herodias, mulher de Filipe, seu irmão;
4 pois João lhe dizia: Não te é lícito possuí-la.
5 E, querendo matá-lo, temia o povo, porque o tinham como profeta.
6 Ora, tendo chegado o dia natalício de Herodes, dançou a filha de Herodias diante de todos e agradou a Herodes.
7 Pelo que prometeu, com juramento, dar-lhe o que pedisse.
8 Então, ela, instigada por sua mãe, disse: Dá-me, aqui, num prato, a cabeça de João Batista.
9 Entristeceu-se o rei, mas, por causa do juramento e dos que estavam com ele à mesa, determinou que lha dessem;
10 e deu ordens e decapitou a João no cárcere.
11 Foi trazida a cabeça num prato e dada à jovem, que a levou a sua mãe.
12 Então, vieram os seus discípulos, levaram o corpo e o sepultaram; depois, foram e o anunciaram a Jesus.
13 Jesus, ouvindo isto, retirou-se dali num barco, para um lugar deserto, à parte; sabendo-o as multidões, vieram das cidades seguindo-o por terra.
14 Desembarcando, viu Jesus uma grande multidão, compadeceu-se dela e curou os seus enfermos.
15 Ao cair da tarde, vieram os discípulos a Jesus e lhe disseram: O lugar é deserto, e vai adiantada a hora; despede, pois, as multidões para que, indo pelas aldeias, comprem para si o que comer.
16 Jesus, porém, lhes disse: Não precisam retirar-se; dai-lhes, vós mesmos, de comer.
17 Mas eles responderam: Não temos aqui senão cinco pães e dois peixes.
18 Então, ele disse: Trazei-mos.
19 E, tendo mandado que a multidão se assentasse sobre a relva, tomando os cinco pães e os dois peixes, erguendo os olhos ao céu, os abençoou. Depois, tendo partido os pães, deu-os aos discípulos, e estes, às multidões.
20 Todos comeram e se fartaram; e dos pedaços que sobejaram recolheram ainda doze cestos cheios.
21 E os que comeram foram cerca de cinco mil homens, além de mulheres e crianças.
22 Logo a seguir, compeliu Jesus os discípulos a embarcar e passar adiante dele para o outro lado, enquanto ele despedia as multidões.
23 E, despedidas as multidões, subiu ao monte, a fim de orar sozinho. Em caindo a tarde, lá estava ele, só.
24 Entretanto, o barco já estava longe, a muitos estádios da terra, açoitado pelas ondas; porque o vento era contrário.
25 Na quarta vigília da noite, foi Jesus ter com eles, andando por sobre o mar.
26 E os discípulos, ao verem-no andando sobre as águas, ficaram aterrados e exclamaram: É um fantasma! E, tomados de medo, gritaram.
27 Mas Jesus imediatamente lhes disse: Tende bom ânimo! Sou eu. Não temais!
28 Respondendo-lhe Pedro, disse: Se és tu, Senhor, manda-me ir ter contigo, por sobre as águas.
29 E ele disse: Vem! E Pedro, descendo do barco, andou por sobre as águas e foi ter com Jesus.
30 Reparando, porém, na força do vento, teve medo; e, começando a submergir, gritou: Salva-me, Senhor!
31 E, prontamente, Jesus, estendendo a mão, tomou-o e lhe disse: Homem de pequena fé, por que duvidaste?
32 Subindo ambos para o barco, cessou o vento.
33 E os que estavam no barco o adoraram, dizendo: Verdadeiramente és Filho de Deus!
34 Então, estando já no outro lado, chegaram a terra, em Genesaré.
35 Reconhecendo-o os homens daquela terra, mandaram avisar a toda a circunvizinhança e trouxeram-lhe todos os enfermos;
36 e lhe rogavam que ao menos pudessem tocar na orla da sua veste. E todos os que tocaram ficaram sãos.*
1 Então, vieram de Jerusalém a Jesus alguns fariseus e escribas e perguntaram:
2 Por que transgridem os teus discípulos a tradição dos anciãos? Pois não lavam as mãos, quando comem.
3 Ele, porém, lhes respondeu: Por que transgredis vós também o mandamento de Deus, por causa da vossa tradição?
4 Porque Deus ordenou: Honra a teu pai e a tua mãe; e: Quem maldisser a seu pai ou a sua mãe seja punido de morte.
5 Mas vós dizeis: Se alguém disser a seu pai ou a sua mãe: É oferta ao Senhor aquilo que poderias aproveitar de mim;
6 esse jamais honrará a seu pai ou a sua mãe. E, assim, invalidastes a palavra de Deus, por causa da vossa tradição.
7 Hipócritas! Bem profetizou Isaías a vosso respeito, dizendo:
8 Este povo honra-me com os lábios, mas o seu coração está longe de mim.
9 E em vão me adoram, ensinando doutrinas que são preceitos de homens.
10 E, tendo convocado a multidão, lhes disse: Ouvi e entendei:
11 não é o que entra pela boca o que contamina o homem, mas o que sai da boca, isto, sim, contamina o homem.
12 Então, aproximando-se dele os discípulos, disseram: Sabes que os fariseus, ouvindo a tua palavra, se escandalizaram?
13 Ele, porém, respondeu: Toda planta que meu Pai celestial não plantou será arrancada.
14 Deixai-os; são cegos, guias de cegos. Ora, se um cego guiar outro cego, cairão ambos no barranco.
15 Então, lhe disse Pedro: Explica-nos a parábola.
16 Jesus, porém, disse: Também vós não entendeis ainda?
17 Não compreendeis que tudo o que entra pela boca desce para o ventre e, depois, é lançado em lugar escuso?
18 Mas o que sai da boca vem do coração, e é isso que contamina o homem.
19 Porque do coração procedem maus desígnios, homicídios, adultérios, prostituição, furtos, falsos testemunhos, blasfêmias.
20 São estas as coisas que contaminam o homem; mas o comer sem lavar as mãos não o contamina.
21 Partindo Jesus dali, retirou-se para os lados de Tiro e Sidom.
22 E eis que uma mulher cananeia, que viera daquelas regiões, clamava: Senhor, Filho de Davi, tem compaixão de mim! Minha filha está horrivelmente endemoninhada.
23 Ele, porém, não lhe respondeu palavra. E os seus discípulos, aproximando-se, rogaram-lhe: Despede-a, pois vem clamando atrás de nós.
24 Mas Jesus respondeu: Não fui enviado senão às ovelhas perdidas da casa de Israel.
25 Ela, porém, veio e o adorou, dizendo: Senhor, socorre-me!
26 Então, ele, respondendo, disse: Não é bom tomar o pão dos filhos e lançá-lo aos cachorrinhos.
27 Ela, contudo, replicou: Sim, Senhor, porém os cachorrinhos comem das migalhas que caem da mesa dos seus donos.
28 Então, lhe disse Jesus: Ó mulher, grande é a tua fé! Faça-se contigo como queres. E, desde aquele momento, sua filha ficou sã.
29 Partindo Jesus dali, foi para junto do mar da Galileia; e, subindo ao monte, assentou-se ali.
30 E vieram a ele muitas multidões trazendo consigo coxos, aleijados, cegos, mudos e outros muitos e os largaram junto aos pés de Jesus; e ele os curou.
31 De modo que o povo se maravilhou ao ver que os mudos falavam, os aleijados recobravam saúde, os coxos andavam e os cegos viam. Então, glorificavam ao Deus de Israel.
32 E, chamando Jesus os seus discípulos, disse: Tenho compaixão desta gente, porque há três dias que permanece comigo e não tem o que comer; e não quero despedi-la em jejum, para que não desfaleça pelo caminho.
33 Mas os discípulos lhe disseram: Onde haverá neste deserto tantos pães para fartar tão grande multidão?
34 Perguntou-lhes Jesus: Quantos pães tendes? Responderam: Sete e alguns peixinhos.
35 Então, tendo mandado o povo assentar-se no chão,
36 tomou os sete pães e os peixes, e, dando graças, partiu, e deu aos discípulos, e estes, ao povo.
37 Todos comeram e se fartaram; e, do que sobejou, recolheram sete cestos cheios.
38 Ora, os que comeram eram quatro mil homens, além de mulheres e crianças.
39 E, tendo despedido as multidões, entrou Jesus no barco e foi para o território de Magadã.*
1 Aproximando-se os fariseus e os saduceus, tentando-o, pediram-lhe que lhes mostrasse um sinal vindo do céu.
2 Ele, porém, lhes respondeu: Chegada a tarde, dizeis: Haverá bom tempo, porque o céu está avermelhado;
3 e, pela manhã: Hoje, haverá tempestade, porque o céu está de um vermelho sombrio. Sabeis, na verdade, discernir o aspecto do céu e não podeis discernir os sinais dos tempos?
4 Uma geração má e adúltera pede um sinal; e nenhum sinal lhe será dado, senão o de Jonas. E, deixando-os, retirou-se.
5 Ora, tendo os discípulos passado para o outro lado, esqueceram-se de levar pão.
6 E Jesus lhes disse: Vede e acautelai-vos do fermento dos fariseus e dos saduceus.
7 Eles, porém, discorriam entre si, dizendo: É porque não trouxemos pão.
8 Percebendo-o Jesus, disse: Por que discorreis entre vós, homens de pequena fé, sobre o não terdes pão?
9 Não compreendeis ainda, nem vos lembrais dos cinco pães para cinco mil homens e de quantos cestos tomastes?
10 Nem dos sete pães para os quatro mil e de quantos cestos tomastes?
11 Como não compreendeis que não vos falei a respeito de pães? E sim: acautelai-vos do fermento dos fariseus e dos saduceus.
12 Então, entenderam que não lhes dissera que se acautelassem do fermento de pães, mas da doutrina dos fariseus e dos saduceus.
13 Indo Jesus para os lados de Cesareia de Filipe, perguntou a seus discípulos: Quem diz o povo ser o Filho do Homem?
14 E eles responderam: Uns dizem: João Batista; outros: Elias; e outros: Jeremias ou algum dos profetas.
15 Mas vós, continuou ele, quem dizeis que eu sou?
16 Respondendo Simão Pedro, disse: Tu és o Cristo, o Filho do Deus vivo.
17 Então, Jesus lhe afirmou: Bem-aventurado és, Simão Barjonas, porque não foi carne e sangue que to revelaram, mas meu Pai, que está nos céus.
18 Também eu te digo que tu és Pedro, e sobre esta pedra edificarei a minha igreja, e as portas do inferno não prevalecerão contra ela.
19 Dar-te-ei as chaves do reino dos céus; o que ligares na terra terá sido ligado nos céus; e o que desligares na terra terá sido desligado nos céus.
20 Então, advertiu os discípulos de que a ninguém dissessem ser ele o Cristo.
21 Desde esse tempo, começou Jesus Cristo a mostrar a seus discípulos que lhe era necessário seguir para Jerusalém e sofrer muitas coisas dos anciãos, dos principais sacerdotes e dos escribas, ser morto e ressuscitado no terceiro dia.
22 E Pedro, chamando-o à parte, começou a reprová-lo, dizendo: Tem compaixão de ti, Senhor; isso de modo algum te acontecerá.
23 Mas Jesus, voltando-se, disse a Pedro: Arreda, Satanás! Tu és para mim pedra de tropeço, porque não cogitas das coisas de Deus, e sim das dos homens.
24 Então, disse Jesus a seus discípulos: Se alguém quer vir após mim, a si mesmo se negue, tome a sua cruz e siga-me.
25 Porquanto, quem quiser salvar a sua vida perdê-la-á; e quem perder a vida por minha causa achá-la-á.
26 Pois que aproveitará o homem se ganhar o mundo inteiro e perder a sua alma? Ou que dará o homem em troca da sua alma?
27 Porque o Filho do Homem há de vir na glória de seu Pai, com os seus anjos, e, então, retribuirá a cada um conforme as suas obras.
28 Em verdade vos digo que alguns há, dos que aqui se encontram, que de maneira nenhuma passarão pela morte até que vejam vir o Filho do Homem no seu reino.*
1 Seis dias depois, tomou Jesus consigo a Pedro e aos irmãos Tiago e João e os levou, em particular, a um alto monte.
2 E foi transfigurado diante deles; o seu rosto resplandecia como o sol, e as suas vestes tornaram-se brancas como a luz.
3 E eis que lhes apareceram Moisés e Elias, falando com ele.
4 Então, disse Pedro a Jesus: Senhor, bom é estarmos aqui; se queres, farei aqui três tendas; uma será tua, outra para Moisés, outra para Elias.
5 Falava ele ainda, quando uma nuvem luminosa os envolveu; e eis, vindo da nuvem, uma voz que dizia: Este é o meu Filho amado, em quem me comprazo; a ele ouvi.
6 Ouvindo-a os discípulos, caíram de bruços, tomados de grande medo.
7 Aproximando-se deles, tocou-lhes Jesus, dizendo: Erguei-vos e não temais!
8 Então, eles, levantando os olhos, a ninguém viram, senão Jesus.
9 E, descendo eles do monte, ordenou-lhes Jesus: A ninguém conteis a visão, até que o Filho do Homem ressuscite dentre os mortos.
10 Mas os discípulos o interrogaram: Por que dizem, pois, os escribas ser necessário que Elias venha primeiro?
11 Então, Jesus respondeu: De fato, Elias virá e restaurará todas as coisas.
12 Eu, porém, vos declaro que Elias já veio, e não o reconheceram; antes, fizeram com ele tudo quanto quiseram. Assim também o Filho do Homem há de padecer nas mãos deles.
13 Então, os discípulos entenderam que lhes falara a respeito de João Batista.
14 E, quando chegaram para junto da multidão, aproximou-se dele um homem, que se ajoelhou e disse:
15 Senhor, compadece-te de meu filho, porque é lunático e sofre muito; pois muitas vezes cai no fogo e outras muitas, na água.
16 Apresentei-o a teus discípulos, mas eles não puderam curá-lo.
17 Jesus exclamou: Ó geração incrédula e perversa! Até quando estarei convosco? Até quando vos sofrerei? Trazei-me aqui o menino.
18 E Jesus repreendeu o demônio, e este saiu do menino; e, desde aquela hora, ficou o menino curado.
19 Então, os discípulos, aproximando-se de Jesus, perguntaram em particular: Por que motivo não pudemos nós expulsá-lo?
20 E ele lhes respondeu: Por causa da pequenez da vossa fé. Pois em verdade vos digo que, se tiverdes fé como um grão de mostarda, direis a este monte: Passa daqui para acolá, e ele passará. Nada vos será impossível.
21 [Mas esta casta não se expele senão por meio de oração e jejum.]
22 Reunidos eles na Galileia, disse-lhes Jesus: O Filho do Homem está para ser entregue nas mãos dos homens;
23 e estes o matarão; mas, ao terceiro dia, ressuscitará. Então, os discípulos se entristeceram grandemente.
24 Tendo eles chegado a Cafarnaum, dirigiram-se a Pedro os que cobravam o imposto das duas dracmas e perguntaram: Não paga o vosso Mestre as duas dracmas?
25 Sim, respondeu ele. Ao entrar Pedro em casa, Jesus se lhe antecipou, dizendo: Simão, que te parece? De quem cobram os reis da terra impostos ou tributo: dos seus filhos ou dos estranhos?
26 Respondendo Pedro: Dos estranhos, Jesus lhe disse: Logo, estão isentos os filhos.
27 Mas, para que não os escandalizemos, vai ao mar, lança o anzol, e o primeiro peixe que fisgar, tira-o; e, abrindo-lhe a boca, acharás um estáter. Toma-o e entrega-lhes por mim e por ti.*
1 Naquela hora, aproximaram-se de Jesus os discípulos, perguntando: Quem é, porventura, o maior no reino dos céus?
2 E Jesus, chamando uma criança, colocou-a no meio deles.
3 E disse: Em verdade vos digo que, se não vos converterdes e não vos tornardes como crianças, de modo algum entrareis no reino dos céus.
4 Portanto, aquele que se humilhar como esta criança, esse é o maior no reino dos céus.
5 E quem receber uma criança, tal como esta, em meu nome, a mim me recebe.
6 Qualquer, porém, que fizer tropeçar a um destes pequeninos que creem em mim, melhor lhe fora que se lhe pendurasse ao pescoço uma grande pedra de moinho, e fosse afogado na profundeza do mar.
7 Ai do mundo, por causa dos escândalos; porque é inevitável que venham escândalos, mas ai do homem pelo qual vem o escândalo!
8 Portanto, se a tua mão ou o teu pé te faz tropeçar, corta-o e lança-o fora de ti; melhor é entrares na vida manco ou aleijado do que, tendo duas mãos ou dois pés, seres lançado no fogo eterno.
9 Se um dos teus olhos te faz tropeçar, arranca-o e lança-o fora de ti; melhor é entrares na vida com um só dos teus olhos do que, tendo dois, seres lançado no inferno de fogo.
10 Vede, não desprezeis a qualquer destes pequeninos; porque eu vos afirmo que os seus anjos nos céus veem incessantemente a face de meu Pai celeste.
11 [Porque o Filho do Homem veio salvar o que estava perdido.]
12 Que vos parece? Se um homem tiver cem ovelhas, e uma delas se extraviar, não deixará ele nos montes as noventa e nove, indo procurar a que se extraviou?
13 E, se porventura a encontra, em verdade vos digo que maior prazer sentirá por causa desta do que pelas noventa e nove que não se extraviaram.
14 Assim, pois, não é da vontade de vosso Pai celeste que pereça um só destes pequeninos.
15 Se teu irmão pecar [contra ti], vai argui-lo entre ti e ele só. Se ele te ouvir, ganhaste a teu irmão.
16 Se, porém, não te ouvir, toma ainda contigo uma ou duas pessoas, para que, pelo depoimento de duas ou três testemunhas, toda palavra se estabeleça.
17 E, se ele não os atender, dize-o à igreja; e, se recusar ouvir também a igreja, considera-o como gentio e publicano.
18 Em verdade vos digo que tudo o que ligardes na terra terá sido ligado nos céus, e tudo o que desligardes na terra terá sido desligado nos céus.
19 Em verdade também vos digo que, se dois dentre vós, sobre a terra, concordarem a respeito de qualquer coisa que, porventura, pedirem, ser-lhes-á concedida por meu Pai, que está nos céus.
20 Porque, onde estiverem dois ou três reunidos em meu nome, ali estou no meio deles.
21 Então, Pedro, aproximando-se, lhe perguntou: Senhor, até quantas vezes meu irmão pecará contra mim, que eu lhe perdoe? Até sete vezes?
22 Respondeu-lhe Jesus: Não te digo que até sete vezes, mas até setenta vezes sete.
23 Por isso, o reino dos céus é semelhante a um rei que resolveu ajustar contas com os seus servos.
24 E, passando a fazê-lo, trouxeram-lhe um que lhe devia dez mil talentos.
25 Não tendo ele, porém, com que pagar, ordenou o senhor que fosse vendido ele, a mulher, os filhos e tudo quanto possuía e que a dívida fosse paga.
26 Então, o servo, prostrando-se reverente, rogou: Sê paciente comigo, e tudo te pagarei.
27 E o senhor daquele servo, compadecendo-se, mandou-o embora e perdoou-lhe a dívida.
28 Saindo, porém, aquele servo, encontrou um dos seus conservos que lhe devia cem denários; e, agarrando-o, o sufocava, dizendo: Paga-me o que me deves.
29 Então, o seu conservo, caindo-lhe aos pés, lhe implorava: Sê paciente comigo, e te pagarei.
30 Ele, entretanto, não quis; antes, indo-se, o lançou na prisão, até que saldasse a dívida.
31 Vendo os seus companheiros o que se havia passado, entristeceram-se muito e foram relatar ao seu senhor tudo que acontecera.
32 Então, o seu senhor, chamando-o, lhe disse: Servo malvado, perdoei-te aquela dívida toda porque me suplicaste;
33 não devias tu, igualmente, compadecer-te do teu conservo, como também eu me compadeci de ti?
34 E, indignando-se, o seu senhor o entregou aos verdugos, até que lhe pagasse toda a dívida.
35 Assim também meu Pai celeste vos fará, se do íntimo não perdoardes cada um a seu irmão.*
1 E aconteceu que, concluindo Jesus estas palavras, deixou a Galileia e foi para o território da Judeia, além do Jordão.
2 Seguiram-no muitas multidões, e curou-as ali.
3 Vieram a ele alguns fariseus e o experimentavam, perguntando: É lícito ao marido repudiar a sua mulher por qualquer motivo?
4 Então, respondeu ele: Não tendes lido que o Criador, desde o princípio, os fez homem e mulher
5 e que disse: Por esta causa deixará o homem pai e mãe e se unirá a sua mulher, tornando-se os dois uma só carne?
6 De modo que já não são mais dois, porém uma só carne. Portanto, o que Deus ajuntou não o separe o homem.
7 Replicaram-lhe: Por que mandou, então, Moisés dar carta de divórcio e repudiar?
8 Respondeu-lhes Jesus: Por causa da dureza do vosso coração é que Moisés vos permitiu repudiar vossa mulher; entretanto, não foi assim desde o princípio.
9 Eu, porém, vos digo: quem repudiar sua mulher, não sendo por causa de relações sexuais ilícitas, e casar com outra comete adultério [e o que casar com a repudiada comete adultério].
10 Disseram-lhe os discípulos: Se essa é a condição do homem relativamente à sua mulher, não convém casar.
11 Jesus, porém, lhes respondeu: Nem todos são aptos para receber este conceito, mas apenas aqueles a quem é dado.
12 Porque há eunucos de nascença; há outros a quem os homens fizeram tais; e há outros que a si mesmos se fizeram eunucos, por causa do reino dos céus. Quem é apto para o admitir admita.
13 Trouxeram-lhe, então, algumas crianças, para que lhes impusesse as mãos e orasse; mas os discípulos os repreendiam.
14 Jesus, porém, disse: Deixai os pequeninos, não os embaraceis de vir a mim, porque dos tais é o reino dos céus.
15 E, tendo-lhes imposto as mãos, retirou-se dali.
16 E eis que alguém, aproximando-se, lhe perguntou: Mestre, que farei eu de bom, para alcançar a vida eterna?
17 Respondeu-lhe Jesus: Por que me perguntas acerca do que é bom? Bom só existe um. Se queres, porém, entrar na vida, guarda os mandamentos.
18 E ele lhe perguntou: Quais? Respondeu Jesus: Não matarás, não adulterarás, não furtarás, não dirás falso testemunho;
19 honra a teu pai e a tua mãe e amarás o teu próximo como a ti mesmo.
20 Replicou-lhe o jovem: Tudo isso tenho observado; que me falta ainda?
21 Disse-lhe Jesus: Se queres ser perfeito, vai, vende os teus bens, dá aos pobres e terás um tesouro no céu; depois, vem e segue-me.
22 Tendo, porém, o jovem ouvido esta palavra, retirou-se triste, por ser dono de muitas propriedades.
23 Então, disse Jesus a seus discípulos: Em verdade vos digo que um rico dificilmente entrará no reino dos céus.
24 E ainda vos digo que é mais fácil passar um camelo pelo fundo de uma agulha do que entrar um rico no reino de Deus.
25 Ouvindo isto, os discípulos ficaram grandemente maravilhados e disseram: Sendo assim, quem pode ser salvo?
26 Jesus, fitando neles o olhar, disse-lhes: Isto é impossível aos homens, mas para Deus tudo é possível.
27 Então, lhe falou Pedro: Eis que nós tudo deixamos e te seguimos; que será, pois, de nós?
28 Jesus lhes respondeu: Em verdade vos digo que vós, os que me seguistes, quando, na regeneração, o Filho do Homem se assentar no trono da sua glória, também vos assentareis em doze tronos para julgar as doze tribos de Israel.
29 E todo aquele que tiver deixado casas, ou irmãos, ou irmãs, ou pai, ou mãe [ou mulher], ou filhos, ou campos, por causa do meu nome, receberá muitas vezes mais e herdará a vida eterna.
30 Porém muitos primeiros serão últimos; e os últimos, primeiros.*
1 Porque o reino dos céus é semelhante a um dono de casa que saiu de madrugada para assalariar trabalhadores para a sua vinha.
2 E, tendo ajustado com os trabalhadores a um denário por dia, mandou-os para a vinha.
3 Saindo pela terceira hora, viu, na praça, outros que estavam desocupados
4 e disse-lhes: Ide vós também para a vinha, e vos darei o que for justo. Eles foram.
5 Tendo saído outra vez, perto da hora sexta e da nona, procedeu da mesma forma,
6 e, saindo por volta da hora undécima, encontrou outros que estavam desocupados e perguntou-lhes: Por que estivestes aqui desocupados o dia todo?
7 Responderam-lhe: Porque ninguém nos contratou. Então, lhes disse ele: Ide também vós para a vinha.
8 Ao cair da tarde, disse o senhor da vinha ao seu administrador: Chama os trabalhadores e paga-lhes o salário, começando pelos últimos, indo até aos primeiros.
9 Vindo os da hora undécima, recebeu cada um deles um denário.
10 Ao chegarem os primeiros, pensaram que receberiam mais; porém também estes receberam um denário cada um.
11 Mas, tendo-o recebido, murmuravam contra o dono da casa,
12 dizendo: Estes últimos trabalharam apenas uma hora; contudo, os igualaste a nós, que suportamos a fadiga e o calor do dia.
13 Mas o proprietário, respondendo, disse a um deles: Amigo, não te faço injustiça; não combinaste comigo um denário?
14 Toma o que é teu e vai-te; pois quero dar a este último tanto quanto a ti.
15 Porventura, não me é lícito fazer o que quero do que é meu? Ou são maus os teus olhos porque eu sou bom?
16 Assim, os últimos serão primeiros, e os primeiros serão últimos [porque muitos são chamados, mas poucos escolhidos].
17 Estando Jesus para subir a Jerusalém, chamou à parte os doze e, em caminho, lhes disse:
18 Eis que subimos para Jerusalém, e o Filho do Homem será entregue aos principais sacerdotes e aos escribas. Eles o condenarão à morte.
19 E o entregarão aos gentios para ser escarnecido, açoitado e crucificado; mas, ao terceiro dia, ressurgirá.
20 Então, se chegou a ele a mulher de Zebedeu, com seus filhos, e, adorando-o, pediu-lhe um favor.
21 Perguntou-lhe ele: Que queres? Ela respondeu: Manda que, no teu reino, estes meus dois filhos se assentem, um à tua direita, e o outro à tua esquerda.
22 Mas Jesus respondeu: Não sabeis o que pedis. Podeis vós beber o cálice que eu estou para beber? Responderam-lhe: Podemos.
23 Então, lhes disse: Bebereis o meu cálice; mas o assentar-se à minha direita e à minha esquerda não me compete concedê-lo; é, porém, para aqueles a quem está preparado por meu Pai.
24 Ora, ouvindo isto os dez, indignaram-se contra os dois irmãos.
25 Então, Jesus, chamando-os, disse: Sabeis que os governadores dos povos os dominam e que os maiorais exercem autoridade sobre eles.
26 Não é assim entre vós; pelo contrário, quem quiser tornar-se grande entre vós, será esse o que vos sirva;
27 e quem quiser ser o primeiro entre vós será vosso servo;
28 tal como o Filho do Homem, que não veio para ser servido, mas para servir e dar a sua vida em resgate por muitos.
29 Saindo eles de Jericó, uma grande multidão o acompanhava.
30 E eis que dois cegos, assentados à beira do caminho, tendo ouvido que Jesus passava, clamaram: Senhor, Filho de Davi, tem compaixão de nós!
31 Mas a multidão os repreendia para que se calassem; eles, porém, gritavam cada vez mais: Senhor, Filho de Davi, tem misericórdia de nós!
32 Então, parando Jesus, chamou-os e perguntou: Que quereis que eu vos faça?
33 Responderam: Senhor, que se nos abram os olhos.
34 Condoído, Jesus tocou-lhes os olhos, e imediatamente recuperaram a vista e o foram seguindo.*
1 Quando se aproximaram de Jerusalém e chegaram a Betfagé, ao monte das Oliveiras, enviou Jesus dois discípulos, dizendo-lhes:
2 Ide à aldeia que aí está diante de vós e logo achareis presa uma jumenta e, com ela, um jumentinho. Desprendei-a e trazei-mos.
3 E, se alguém vos disser alguma coisa, respondei-lhe que o Senhor precisa deles. E logo os enviará.
4 Ora, isto aconteceu para se cumprir o que foi dito por intermédio do profeta:
5 Dizei à filha de Sião: Eis aí te vem o teu Rei, humilde, montado em jumento, num jumentinho, cria de animal de carga.
6 Indo os discípulos e tendo feito como Jesus lhes ordenara,
7 trouxeram a jumenta e o jumentinho. Então, puseram em cima deles as suas vestes, e sobre elas Jesus montou.
8 E a maior parte da multidão estendeu as suas vestes pelo caminho, e outros cortavam ramos de árvores, espalhando-os pela estrada.
9 E as multidões, tanto as que o precediam como as que o seguiam, clamavam: Hosana ao Filho de Davi! Bendito o que vem em nome do Senhor! Hosana nas maiores alturas!
10 E, entrando ele em Jerusalém, toda a cidade se alvoroçou, e perguntavam: Quem é este?
11 E as multidões clamavam: Este é o profeta Jesus, de Nazaré da Galileia!
12 Tendo Jesus entrado no templo, expulsou todos os que ali vendiam e compravam; também derribou as mesas dos cambistas e as cadeiras dos que vendiam pombas.
13 E disse-lhes: Está escrito: A minha casa será chamada casa de oração; vós, porém, a transformais em covil de salteadores.
14 Vieram a ele, no templo, cegos e coxos, e ele os curou.
15 Mas, vendo os principais sacerdotes e os escribas as maravilhas que Jesus fazia e os meninos clamando: Hosana ao Filho de Davi!, indignaram-se e perguntaram-lhe:
16 Ouves o que estes estão dizendo? Respondeu-lhes Jesus: Sim; nunca lestes: Da boca de pequeninos e crianças de peito tiraste perfeito louvor?
17 E, deixando-os, saiu da cidade para Betânia, onde pernoitou.
18 Cedo de manhã, ao voltar para a cidade, teve fome;
19 e, vendo uma figueira à beira do caminho, aproximou-se dela; e, não tendo achado senão folhas, disse-lhe: Nunca mais nasça fruto de ti! E a figueira secou imediatamente.
20 Vendo isto os discípulos, admiraram-se e exclamaram: Como secou depressa a figueira!
21 Jesus, porém, lhes respondeu: Em verdade vos digo que, se tiverdes fé e não duvidardes, não somente fareis o que foi feito à figueira, mas até mesmo, se a este monte disserdes: Ergue-te e lança-te no mar, tal sucederá;
22 e tudo quanto pedirdes em oração, crendo, recebereis.
23 Tendo Jesus chegado ao templo, estando já ensinando, acercaram-se dele os principais sacerdotes e os anciãos do povo, perguntando: Com que autoridade fazes estas coisas? E quem te deu essa autoridade?
24 E Jesus lhes respondeu: Eu também vos farei uma pergunta; se me responderdes, também eu vos direi com que autoridade faço estas coisas.
25 Donde era o batismo de João, do céu ou dos homens? E discorriam entre si: Se dissermos: do céu, ele nos dirá: Então, por que não acreditastes nele?
26 E, se dissermos: dos homens, é para temer o povo, porque todos consideram João como profeta.
27 Então, responderam a Jesus: Não sabemos. E ele, por sua vez: Nem eu vos digo com que autoridade faço estas coisas.
28 E que vos parece? Um homem tinha dois filhos. Chegando-se ao primeiro, disse: Filho, vai hoje trabalhar na vinha.
29 Ele respondeu: Sim, senhor; porém não foi.
30 Dirigindo-se ao segundo, disse-lhe a mesma coisa. Mas este respondeu: Não quero; depois, arrependido, foi.
31 Qual dos dois fez a vontade do pai? Disseram: O segundo. Declarou-lhes Jesus: Em verdade vos digo que publicanos e meretrizes vos precedem no reino de Deus.
32 Porque João veio a vós outros no caminho da justiça, e não acreditastes nele; ao passo que publicanos e meretrizes creram. Vós, porém, mesmo vendo isto, não vos arrependestes, afinal, para acreditardes nele.
33 Atentai noutra parábola. Havia um homem, dono de casa, que plantou uma vinha. Cercou-a de uma sebe, construiu nela um lagar, edificou-lhe uma torre e arrendou-a a uns lavradores. Depois, se ausentou do país.
34 Ao tempo da colheita, enviou os seus servos aos lavradores, para receber os frutos que lhe tocavam.
35 E os lavradores, agarrando os servos, espancaram a um, mataram a outro e a outro apedrejaram.
36 Enviou ainda outros servos em maior número; e trataram-nos da mesma sorte.
37 E, por último, enviou-lhes o seu próprio filho, dizendo: A meu filho respeitarão.
38 Mas os lavradores, vendo o filho, disseram entre si: Este é o herdeiro; ora, vamos, matemo-lo e apoderemo-nos da sua herança.
39 E, agarrando-o, lançaram-no fora da vinha e o mataram.
40 Quando, pois, vier o senhor da vinha, que fará àqueles lavradores?
41 Responderam-lhe: Fará perecer horrivelmente a estes malvados e arrendará a vinha a outros lavradores que lhe remetam os frutos nos seus devidos tempos.
42 Perguntou-lhes Jesus: Nunca lestes nas Escrituras: A pedra que os construtores rejeitaram, essa veio a ser a principal pedra, angular; isto procede do Senhor e é maravilhoso aos nossos olhos?
43 Portanto, vos digo que o reino de Deus vos será tirado e será entregue a um povo que lhe produza os respectivos frutos.
44 Todo o que cair sobre esta pedra ficará em pedaços; e aquele sobre quem ela cair ficará reduzido a pó.
45 Os principais sacerdotes e os fariseus, ouvindo estas parábolas, entenderam que era a respeito deles que Jesus falava;
46 e, conquanto buscassem prendê-lo, temeram as multidões, porque estas o consideravam como profeta.*
1 De novo, entrou Jesus a falar por parábolas, dizendo-lhes:
2 O reino dos céus é semelhante a um rei que celebrou as bodas de seu filho.
3 Então, enviou os seus servos a chamar os convidados para as bodas; mas estes não quiseram vir.
4 Enviou ainda outros servos, com esta ordem: Dizei aos convidados: Eis que já preparei o meu banquete; os meus bois e cevados já foram abatidos, e tudo está pronto; vinde para as bodas.
5 Eles, porém, não se importaram e se foram, um para o seu campo, outro para o seu negócio;
6 e os outros, agarrando os servos, os maltrataram e mataram.
7 O rei ficou irado e, enviando as suas tropas, exterminou aqueles assassinos e lhes incendiou a cidade.
8 Então, disse aos seus servos: Está pronta a festa, mas os convidados não eram dignos.
9 Ide, pois, para as encruzilhadas dos caminhos e convidai para as bodas a quantos encontrardes.
10 E, saindo aqueles servos pelas estradas, reuniram todos os que encontraram, maus e bons; e a sala do banquete ficou repleta de convidados.
11 Entrando, porém, o rei para ver os que estavam à mesa, notou ali um homem que não trazia veste nupcial
12 e perguntou-lhe: Amigo, como entraste aqui sem veste nupcial? E ele emudeceu.
13 Então, ordenou o rei aos serventes: Amarrai-o de pés e mãos e lançai-o para fora, nas trevas; ali haverá choro e ranger de dentes.
14 Porque muitos são chamados, mas poucos, escolhidos.
15 Então, retirando-se os fariseus, consultaram entre si como o surpreenderiam em alguma palavra.
16 E enviaram-lhe discípulos, juntamente com os herodianos, para dizer-lhe: Mestre, sabemos que és verdadeiro e que ensinas o caminho de Deus, de acordo com a verdade, sem te importares com quem quer que seja, porque não olhas a aparência dos homens.
17 Dize-nos, pois: que te parece? É lícito pagar tributo a César ou não?
18 Jesus, porém, conhecendo-lhes a malícia, respondeu: Por que me experimentais, hipócritas?
19 Mostrai-me a moeda do tributo. Trouxeram-lhe um denário.
20 E ele lhes perguntou: De quem é esta efígie e inscrição?
21 Responderam: De César. Então, lhes disse: Dai, pois, a César o que é de César e a Deus o que é de Deus.
22 Ouvindo isto, se admiraram e, deixando-o, foram-se.
23 Naquele dia, aproximaram-se dele alguns saduceus, que dizem não haver ressurreição, e lhe perguntaram:
24 Mestre, Moisés disse: Se alguém morrer, não tendo filhos, seu irmão casará com a viúva e suscitará descendência ao falecido.
25 Ora, havia entre nós sete irmãos. O primeiro, tendo casado, morreu e, não tendo descendência, deixou sua mulher a seu irmão;
26 o mesmo sucedeu com o segundo, com o terceiro, até ao sétimo;
27 depois de todos eles, morreu também a mulher.
28 Portanto, na ressurreição, de qual dos sete será ela esposa? Porque todos a desposaram.
29 Respondeu-lhes Jesus: Errais, não conhecendo as Escrituras nem o poder de Deus.
30 Porque, na ressurreição, nem casam, nem se dão em casamento; são, porém, como os anjos no céu.
31 E, quanto à ressurreição dos mortos, não tendes lido o que Deus vos declarou:
32 Eu sou o Deus de Abraão, o Deus de Isaque e o Deus de Jacó? Ele não é Deus de mortos, e sim de vivos.
33 Ouvindo isto, as multidões se maravilhavam da sua doutrina.
34 Entretanto, os fariseus, sabendo que ele fizera calar os saduceus, reuniram-se em conselho.
35 E um deles, intérprete da Lei, experimentando-o, lhe perguntou:
36 Mestre, qual é o grande mandamento na Lei?
37 Respondeu-lhe Jesus: Amarás o Senhor, teu Deus, de todo o teu coração, de toda a tua alma e de todo o teu entendimento.
38 Este é o grande e primeiro mandamento.
39 O segundo, semelhante a este, é: Amarás o teu próximo como a ti mesmo.
40 Destes dois mandamentos dependem toda a Lei e os Profetas.
41 Reunidos os fariseus, interrogou-os Jesus:
42 Que pensais vós do Cristo? De quem é filho? Responderam-lhe eles: De Davi.
43 Replicou-lhes Jesus: Como, pois, Davi, pelo Espírito, chama-lhe Senhor, dizendo:
44 Disse o Senhor ao meu Senhor: Assenta-te à minha direita, até que eu ponha os teus inimigos debaixo dos teus pés?
45 Se Davi, pois, lhe chama Senhor, como é ele seu filho?
46 E ninguém lhe podia responder palavra, nem ousou alguém, a partir daquele dia, fazer-lhe perguntas.*
1 Então, falou Jesus às multidões e aos seus discípulos:
2 Na cadeira de Moisés, se assentaram os escribas e os fariseus.
3 Fazei e guardai, pois, tudo quanto eles vos disserem, porém não os imiteis nas suas obras; porque dizem e não fazem.
4 Atam fardos pesados [e difíceis de carregar] e os põem sobre os ombros dos homens; entretanto, eles mesmos nem com o dedo querem movê-los.
5 Praticam, porém, todas as suas obras com o fim de serem vistos dos homens; pois alargam os seus filactérios e alongam as suas franjas.
6 Amam o primeiro lugar nos banquetes e as primeiras cadeiras nas sinagogas,
7 as saudações nas praças e o serem chamados mestres pelos homens.
8 Vós, porém, não sereis chamados mestres, porque um só é vosso Mestre, e vós todos sois irmãos.
9 A ninguém sobre a terra chameis vosso pai; porque só um é vosso Pai, aquele que está nos céus.
10 Nem sereis chamados guias, porque um só é vosso Guia, o Cristo.
11 Mas o maior dentre vós será vosso servo.
12 Quem a si mesmo se exaltar será humilhado; e quem a si mesmo se humilhar será exaltado.
13 Ai de vós, escribas e fariseus, hipócritas, porque fechais o reino dos céus diante dos homens; pois vós não entrais, nem deixais entrar os que estão entrando!
14 [Ai de vós, escribas e fariseus, hipócritas, porque devorais as casas das viúvas e, para o justificar, fazeis longas orações; por isso, sofrereis juízo muito mais severo!]
15 Ai de vós, escribas e fariseus, hipócritas, porque rodeais o mar e a terra para fazer um prosélito; e, uma vez feito, o tornais filho do inferno duas vezes mais do que vós!
16 Ai de vós, guias cegos, que dizeis: Quem jurar pelo santuário, isso é nada; mas, se alguém jurar pelo ouro do santuário, fica obrigado pelo que jurou!
17 Insensatos e cegos! Pois qual é maior: o ouro ou o santuário que santifica o ouro?
18 E dizeis: Quem jurar pelo altar, isso é nada; quem, porém, jurar pela oferta que está sobre o altar fica obrigado pelo que jurou.
19 Cegos! Pois qual é maior: a oferta ou o altar que santifica a oferta?
20 Portanto, quem jurar pelo altar jura por ele e por tudo o que sobre ele está.
21 Quem jurar pelo santuário jura por ele e por aquele que nele habita;
22 e quem jurar pelo céu jura pelo trono de Deus e por aquele que no trono está sentado.
23 Ai de vós, escribas e fariseus, hipócritas, porque dais o dízimo da hortelã, do endro e do cominho e tendes negligenciado os preceitos mais importantes da Lei: a justiça, a misericórdia e a fé; devíeis, porém, fazer estas coisas, sem omitir aquelas!
24 Guias cegos, que coais o mosquito e engolis o camelo!
25 Ai de vós, escribas e fariseus, hipócritas, porque limpais o exterior do copo e do prato, mas estes, por dentro, estão cheios de rapina e intemperança!
26 Fariseu cego, limpa primeiro o interior do copo, para que também o seu exterior fique limpo!
27 Ai de vós, escribas e fariseus, hipócritas, porque sois semelhantes aos sepulcros caiados, que, por fora, se mostram belos, mas interiormente estão cheios de ossos de mortos e de toda imundícia!
28 Assim também vós exteriormente pareceis justos aos homens, mas, por dentro, estais cheios de hipocrisia e de iniquidade.
29 Ai de vós, escribas e fariseus, hipócritas, porque edificais os sepulcros dos profetas, adornais os túmulos dos justos
30 e dizeis: Se tivéssemos vivido nos dias de nossos pais, não teríamos sido seus cúmplices no sangue dos profetas!
31 Assim, contra vós mesmos, testificais que sois filhos dos que mataram os profetas.
32 Enchei vós, pois, a medida de vossos pais.
33 Serpentes, raça de víboras! Como escapareis da condenação do inferno?
34 Por isso, eis que eu vos envio profetas, sábios e escribas. A uns matareis e crucificareis; a outros açoitareis nas vossas sinagogas e perseguireis de cidade em cidade;
35 para que sobre vós recaia todo o sangue justo derramado sobre a terra, desde o sangue do justo Abel até ao sangue de Zacarias, filho de Baraquias, a quem matastes entre o santuário e o altar.
36 Em verdade vos digo que todas estas coisas hão de vir sobre a presente geração.
37 Jerusalém, Jerusalém, que matas os profetas e apedrejas os que te foram enviados! Quantas vezes quis eu reunir os teus filhos, como a galinha ajunta os seus pintinhos debaixo das asas, e vós não o quisestes!
38 Eis que a vossa casa vos ficará deserta.
39 Declaro-vos, pois, que, desde agora, já não me vereis, até que venhais a dizer: Bendito o que vem em nome do Senhor!*
1 Tendo Jesus saído do templo, ia-se retirando, quando se aproximaram dele os seus discípulos para lhe mostrar as construções do templo.
2 Ele, porém, lhes disse: Não vedes tudo isto? Em verdade vos digo que não ficará aqui pedra sobre pedra que não seja derribada.
3 No monte das Oliveiras, achava-se Jesus assentado, quando se aproximaram dele os discípulos, em particular, e lhe pediram: Dize-nos quando sucederão estas coisas e que sinal haverá da tua vinda e da consumação do século.
4 E ele lhes respondeu: Vede que ninguém vos engane.
5 Porque virão muitos em meu nome, dizendo: Eu sou o Cristo, e enganarão a muitos.
6 E, certamente, ouvireis falar de guerras e rumores de guerras; vede, não vos assusteis, porque é necessário assim acontecer, mas ainda não é o fim.
7 Porquanto se levantará nação contra nação, reino contra reino, e haverá fomes e terremotos em vários lugares;
8 porém tudo isto é o princípio das dores.
9 Então, sereis atribulados, e vos matarão. Sereis odiados de todas as nações, por causa do meu nome.
10 Nesse tempo, muitos hão de se escandalizar, trair e odiar uns aos outros;
11 levantar-se-ão muitos falsos profetas e enganarão a muitos.
12 E, por se multiplicar a iniquidade, o amor se esfriará de quase todos.
13 Aquele, porém, que perseverar até o fim, esse será salvo.
14 E será pregado este evangelho do reino por todo o mundo, para testemunho a todas as nações. Então, virá o fim.
15 Quando, pois, virdes o abominável da desolação de que falou o profeta Daniel, no lugar santo (quem lê entenda),
16 então, os que estiverem na Judeia fujam para os montes;
17 quem estiver sobre o eirado não desça a tirar de casa alguma coisa;
18 e quem estiver no campo não volte atrás para buscar a sua capa.
19 Ai das que estiverem grávidas e das que amamentarem naqueles dias!
20 Orai para que a vossa fuga não se dê no inverno, nem no sábado;
21 porque nesse tempo haverá grande tribulação, como desde o princípio do mundo até agora não tem havido e nem haverá jamais.
22 Não tivessem aqueles dias sido abreviados, ninguém seria salvo; mas, por causa dos escolhidos, tais dias serão abreviados.
23 Então, se alguém vos disser: Eis aqui o Cristo! Ou: Ei-lo ali! Não acrediteis;
24 porque surgirão falsos cristos e falsos profetas operando grandes sinais e prodígios para enganar, se possível, os próprios eleitos.
25 Vede que vo-lo tenho predito.
26 Portanto, se vos disserem: Eis que ele está no deserto!, não saiais. Ou: Ei-lo no interior da casa!, não acrediteis.
27 Porque, assim como o relâmpago sai do oriente e se mostra até no ocidente, assim há de ser a vinda do Filho do Homem.
28 Onde estiver o cadáver, aí se ajuntarão os abutres.
29 Logo em seguida à tribulação daqueles dias, o sol escurecerá, a lua não dará a sua claridade, as estrelas cairão do firmamento, e os poderes dos céus serão abalados.
30 Então, aparecerá no céu o sinal do Filho do Homem; todos os povos da terra se lamentarão e verão o Filho do Homem vindo sobre as nuvens do céu, com poder e muita glória.
31 E ele enviará os seus anjos, com grande clangor de trombeta, os quais reunirão os seus escolhidos, dos quatro ventos, de uma a outra extremidade dos céus.
32 Aprendei, pois, a parábola da figueira: quando já os seus ramos se renovam e as folhas brotam, sabeis que está próximo o verão.
33 Assim também vós: quando virdes todas estas coisas, sabei que está próximo, às portas.
34 Em verdade vos digo que não passará esta geração sem que tudo isto aconteça.
35 Passará o céu e a terra, porém as minhas palavras não passarão.
36 Mas a respeito daquele dia e hora ninguém sabe, nem os anjos dos céus, nem o Filho, senão o Pai.
37 Pois assim como foi nos dias de Noé, também será a vinda do Filho do Homem.
38 Porquanto, assim como nos dias anteriores ao dilúvio comiam e bebiam, casavam e davam-se em casamento, até ao dia em que Noé entrou na arca,
39 e não o perceberam, senão quando veio o dilúvio e os levou a todos, assim será também a vinda do Filho do Homem.
40 Então, dois estarão no campo, um será tomado, e deixado o outro;
41 duas estarão trabalhando num moinho, uma será tomada, e deixada a outra.
42 Portanto, vigiai, porque não sabeis em que dia vem o vosso Senhor.
43 Mas considerai isto: se o pai de família soubesse a que hora viria o ladrão, vigiaria e não deixaria que fosse arrombada a sua casa.
44 Por isso, ficai também vós apercebidos; porque, à hora em que não cuidais, o Filho do Homem virá.
45 Quem é, pois, o servo fiel e prudente, a quem o senhor confiou os seus conservos para dar-lhes o sustento a seu tempo?
46 Bem-aventurado aquele servo a quem seu senhor, quando vier, achar fazendo assim.
47 Em verdade vos digo que lhe confiará todos os seus bens.
48 Mas, se aquele servo, sendo mau, disser consigo mesmo: Meu senhor demora-se,
49 e passar a espancar os seus companheiros e a comer e beber com ébrios,
50 virá o senhor daquele servo em dia em que não o espera e em hora que não sabe
51 e castigá-lo-á, lançando-lhe a sorte com os hipócritas; ali haverá choro e ranger de dentes.*
1 Então, o reino dos céus será semelhante a dez virgens que, tomando as suas lâmpadas, saíram a encontrar-se com o noivo.
2 Cinco dentre elas eram néscias, e cinco, prudentes.
3 As néscias, ao tomarem as suas lâmpadas, não levaram azeite consigo;
4 no entanto, as prudentes, além das lâmpadas, levaram azeite nas vasilhas.
5 E, tardando o noivo, foram todas tomadas de sono e adormeceram.
6 Mas, à meia-noite, ouviu-se um grito: Eis o noivo! Saí ao seu encontro!
7 Então, se levantaram todas aquelas virgens e prepararam as suas lâmpadas.
8 E as néscias disseram às prudentes: Dai-nos do vosso azeite, porque as nossas lâmpadas estão-se apagando.
9 Mas as prudentes responderam: Não, para que não nos falte a nós e a vós outras! Ide, antes, aos que o vendem e comprai-o.
10 E, saindo elas para comprar, chegou o noivo, e as que estavam apercebidas entraram com ele para as bodas; e fechou-se a porta.
11 Mais tarde, chegaram as virgens néscias, clamando: Senhor, senhor, abre-nos a porta!
12 Mas ele respondeu: Em verdade vos digo que não vos conheço.
13 Vigiai, pois, porque não sabeis o dia nem a hora.
14 Pois será como um homem que, ausentando-se do país, chamou os seus servos e lhes confiou os seus bens.
15 A um deu cinco talentos, a outro, dois e a outro, um, a cada um segundo a sua própria capacidade; e, então, partiu.
16 O que recebera cinco talentos saiu imediatamente a negociar com eles e ganhou outros cinco.
17 Do mesmo modo, o que recebera dois ganhou outros dois.
18 Mas o que recebera um, saindo, abriu uma cova e escondeu o dinheiro do seu senhor.
19 Depois de muito tempo, voltou o senhor daqueles servos e ajustou contas com eles.
20 Então, aproximando-se o que recebera cinco talentos, entregou outros cinco, dizendo: Senhor, confiaste-me cinco talentos; eis aqui outros cinco talentos que ganhei.
21 Disse-lhe o senhor: Muito bem, servo bom e fiel; foste fiel no pouco, sobre o muito te colocarei; entra no gozo do teu senhor.
22 E, aproximando-se também o que recebera dois talentos, disse: Senhor, dois talentos me confiaste; aqui tens outros dois que ganhei.
23 Disse-lhe o senhor: Muito bem, servo bom e fiel; foste fiel no pouco, sobre o muito te colocarei; entra no gozo do teu senhor.
24 Chegando, por fim, o que recebera um talento, disse: Senhor, sabendo que és homem severo, que ceifas onde não semeaste e ajuntas onde não espalhaste,
25 receoso, escondi na terra o teu talento; aqui tens o que é teu.
26 Respondeu-lhe, porém, o senhor: Servo mau e negligente, sabias que ceifo onde não semeei e ajunto onde não espalhei?
27 Cumpria, portanto, que entregasses o meu dinheiro aos banqueiros, e eu, ao voltar, receberia com juros o que é meu.
28 Tirai-lhe, pois, o talento e dai-o ao que tem dez.
29 Porque a todo o que tem se lhe dará, e terá em abundância; mas ao que não tem, até o que tem lhe será tirado.
30 E o servo inútil, lançai-o para fora, nas trevas. Ali haverá choro e ranger de dentes.
31 Quando vier o Filho do Homem na sua majestade e todos os anjos com ele, então, se assentará no trono da sua glória;
32 e todas as nações serão reunidas em sua presença, e ele separará uns dos outros, como o pastor separa dos cabritos as ovelhas;
33 e porá as ovelhas à sua direita, mas os cabritos, à esquerda;
34 então, dirá o Rei aos que estiverem à sua direita: Vinde, benditos de meu Pai! Entrai na posse do reino que vos está preparado desde a fundação do mundo.
35 Porque tive fome, e me destes de comer; tive sede, e me destes de beber; era forasteiro, e me hospedastes;
36 estava nu, e me vestistes; enfermo, e me visitastes; preso, e fostes ver-me.
37 Então, perguntarão os justos: Senhor, quando foi que te vimos com fome e te demos de comer? Ou com sede e te demos de beber?
38 E quando te vimos forasteiro e te hospedamos? Ou nu e te vestimos?
39 E quando te vimos enfermo ou preso e te fomos visitar?
40 O Rei, respondendo, lhes dirá: Em verdade vos afirmo que, sempre que o fizestes a um destes meus pequeninos irmãos, a mim o fizestes.
41 Então, o Rei dirá também aos que estiverem à sua esquerda: Apartai-vos de mim, malditos, para o fogo eterno, preparado para o diabo e seus anjos.
42 Porque tive fome, e não me destes de comer; tive sede, e não me destes de beber;
43 sendo forasteiro, não me hospedastes; estando nu, não me vestistes; achando-me enfermo e preso, não fostes ver-me.
44 E eles lhe perguntarão: Senhor, quando foi que te vimos com fome, com sede, forasteiro, nu, enfermo ou preso e não te assistimos?
45 Então, lhes responderá: Em verdade vos digo que, sempre que o deixastes de fazer a um destes mais pequeninos, a mim o deixastes de fazer.
46 E irão estes para o castigo eterno, porém os justos, para a vida eterna.*
1 Tendo Jesus acabado todos estes ensinamentos, disse a seus discípulos:
2 Sabeis que, daqui a dois dias, celebrar-se-á a Páscoa; e o Filho do Homem será entregue para ser crucificado.
3 Então, os principais sacerdotes e os anciãos do povo se reuniram no palácio do sumo sacerdote, chamado Caifás;
4 e deliberaram prender Jesus, à traição, e matá-lo.
5 Mas diziam: Não durante a festa, para que não haja tumulto entre o povo.
6 Ora, estando Jesus em Betânia, em casa de Simão, o leproso,
7 aproximou-se dele uma mulher, trazendo um vaso de alabastro cheio de precioso bálsamo, que lhe derramou sobre a cabeça, estando ele à mesa.
8 Vendo isto, indignaram-se os discípulos e disseram: Para que este desperdício?
9 Pois este perfume podia ser vendido por muito dinheiro e dar-se aos pobres.
10 Mas Jesus, sabendo disto, disse-lhes: Por que molestais esta mulher? Ela praticou boa ação para comigo.
11 Porque os pobres, sempre os tendes convosco, mas a mim nem sempre me tendes;
12 pois, derramando este perfume sobre o meu corpo, ela o fez para o meu sepultamento.
13 Em verdade vos digo: Onde for pregado em todo o mundo este evangelho, será também contado o que ela fez, para memória sua.
14 Então, um dos doze, chamado Judas Iscariotes, indo ter com os principais sacerdotes, propôs:
15 Que me quereis dar, e eu vo-lo entregarei? E pagaram-lhe trinta moedas de prata.
16 E, desse momento em diante, buscava ele uma boa ocasião para o entregar.
17 No primeiro dia da Festa dos Pães Asmos, vieram os discípulos a Jesus e lhe perguntaram: Onde queres que te façamos os preparativos para comeres a Páscoa?
18 E ele lhes respondeu: Ide à cidade ter com certo homem e dizei-lhe: O Mestre manda dizer: O meu tempo está próximo; em tua casa celebrarei a Páscoa com os meus discípulos.
19 E eles fizeram como Jesus lhes ordenara e prepararam a Páscoa.
20 Chegada a tarde, pôs-se ele à mesa com os doze discípulos.
21 E, enquanto comiam, declarou Jesus: Em verdade vos digo que um dentre vós me trairá.
22 E eles, muitíssimo contristados, começaram um por um a perguntar-lhe: Porventura, sou eu, Senhor?
23 E ele respondeu: O que mete comigo a mão no prato, esse me trairá.
24 O Filho do Homem vai, como está escrito a seu respeito, mas ai daquele por intermédio de quem o Filho do Homem está sendo traído! Melhor lhe fora não haver nascido!
25 Então, Judas, que o traía, perguntou: Acaso, sou eu, Mestre? Respondeu-lhe Jesus: Tu o disseste.
26 Enquanto comiam, tomou Jesus um pão, e, abençoando-o, o partiu, e o deu aos discípulos, dizendo: Tomai, comei; isto é o meu corpo.
27 A seguir, tomou um cálice e, tendo dado graças, o deu aos discípulos, dizendo: Bebei dele todos;
28 porque isto é o meu sangue, o sangue da [nova] aliança, derramado em favor de muitos, para remissão de pecados.
29 E digo-vos que, desta hora em diante, não beberei deste fruto da videira, até aquele dia em que o hei de beber, novo, convosco no reino de meu Pai.
30 E, tendo cantado um hino, saíram para o monte das Oliveiras.
31 Então, Jesus lhes disse: Esta noite, todos vós vos escandalizareis comigo; porque está escrito: Ferirei o pastor, e as ovelhas do rebanho ficarão dispersas.
32 Mas, depois da minha ressurreição, irei adiante de vós para a Galileia.
33 Disse-lhe Pedro: Ainda que venhas a ser um tropeço para todos, nunca o serás para mim.
34 Replicou-lhe Jesus: Em verdade te digo que, nesta mesma noite, antes que o galo cante, tu me negarás três vezes.
35 Disse-lhe Pedro: Ainda que me seja necessário morrer contigo, de nenhum modo te negarei. E todos os discípulos disseram o mesmo.
36 Em seguida, foi Jesus com eles a um lugar chamado Getsêmani e disse a seus discípulos: Assentai-vos aqui, enquanto eu vou ali orar;
37 e, levando consigo a Pedro e aos dois filhos de Zebedeu, começou a entristecer-se e a angustiar-se.
38 Então, lhes disse: A minha alma está profundamente triste até à morte; ficai aqui e vigiai comigo.
39 Adiantando-se um pouco, prostrou-se sobre o seu rosto, orando e dizendo: Meu Pai, se possível, passe de mim este cálice! Todavia, não seja como eu quero, e sim como tu queres.
40 E, voltando para os discípulos, achou-os dormindo; e disse a Pedro: Então, nem uma hora pudestes vós vigiar comigo?
41 Vigiai e orai, para que não entreis em tentação; o espírito, na verdade, está pronto, mas a carne é fraca.
42 Tornando a retirar-se, orou de novo, dizendo: Meu Pai, se não é possível passar de mim este cálice sem que eu o beba, faça-se a tua vontade.
43 E, voltando, achou-os outra vez dormindo; porque os seus olhos estavam pesados.
44 Deixando-os novamente, foi orar pela terceira vez, repetindo as mesmas palavras.
45 Então, voltou para os discípulos e lhes disse: Ainda dormis e repousais! Eis que é chegada a hora, e o Filho do Homem está sendo entregue nas mãos de pecadores.
46 Levantai-vos, vamos! Eis que o traidor se aproxima.
47 Falava ele ainda, e eis que chegou Judas, um dos doze, e, com ele, grande turba com espadas e porretes, vinda da parte dos principais sacerdotes e dos anciãos do povo.
48 Ora, o traidor lhes tinha dado este sinal: Aquele a quem eu beijar, é esse; prendei-o.
49 E logo, aproximando-se de Jesus, lhe disse: Salve, Mestre! E o beijou.
50 Jesus, porém, lhe disse: Amigo, para que vieste? Nisto, aproximando-se eles, deitaram as mãos em Jesus e o prenderam.
51 E eis que um dos que estavam com Jesus, estendendo a mão, sacou da espada e, golpeando o servo do sumo sacerdote, cortou-lhe a orelha.
52 Então, Jesus lhe disse: Embainha a tua espada; pois todos os que lançam mão da espada à espada perecerão.
53 Acaso, pensas que não posso rogar a meu Pai, e ele me mandaria neste momento mais de doze legiões de anjos?
54 Como, pois, se cumpririam as Escrituras, segundo as quais assim deve suceder?
55 Naquele momento, disse Jesus às multidões: Saístes com espadas e porretes para prender-me, como a um salteador? Todos os dias, no templo, eu me assentava [convosco] ensinando, e não me prendestes.
56 Tudo isto, porém, aconteceu para que se cumprissem as Escrituras dos profetas. Então, os discípulos todos, deixando-o, fugiram.
57 E os que prenderam Jesus o levaram à casa de Caifás, o sumo sacerdote, onde se haviam reunido os escribas e os anciãos.
58 Mas Pedro o seguia de longe até ao pátio do sumo sacerdote e, tendo entrado, assentou-se entre os serventuários, para ver o fim.
59 Ora, os principais sacerdotes e todo o Sinédrio procuravam algum testemunho falso contra Jesus, a fim de o condenarem à morte.
60 E não acharam, apesar de se terem apresentado muitas testemunhas falsas. Mas, afinal, compareceram duas, afirmando:
61 Este disse: Posso destruir o santuário de Deus e reedificá-lo em três dias.
62 E, levantando-se o sumo sacerdote, perguntou a Jesus: Nada respondes ao que estes depõem contra ti?
63 Jesus, porém, guardou silêncio. E o sumo sacerdote lhe disse: Eu te conjuro pelo Deus vivo que nos digas se tu és o Cristo, o Filho de Deus.
64 Respondeu-lhe Jesus: Tu o disseste; entretanto, eu vos declaro que, desde agora, vereis o Filho do Homem assentado à direita do Todo-Poderoso e vindo sobre as nuvens do céu.
65 Então, o sumo sacerdote rasgou as suas vestes, dizendo: Blasfemou! Que necessidade mais temos de testemunhas? Eis que ouvistes agora a blasfêmia!
66 Que vos parece? Responderam eles: É réu de morte.
67 Então, uns cuspiram-lhe no rosto e lhe davam murros, e outros o esbofeteavam, dizendo:
68 Profetiza-nos, ó Cristo, quem é que te bateu!
69 Ora, estava Pedro assentado fora no pátio; e, aproximando-se uma criada, lhe disse: Também tu estavas com Jesus, o galileu.
70 Ele, porém, o negou diante de todos, dizendo: Não sei o que dizes.
71 E, saindo para o alpendre, foi ele visto por outra criada, a qual disse aos que ali estavam: Este também estava com Jesus, o Nazareno.
72 E ele negou outra vez, com juramento: Não conheço tal homem.
73 Logo depois, aproximando-se os que ali estavam, disseram a Pedro: Verdadeiramente, és também um deles, porque o teu modo de falar o denuncia.
74 Então, começou ele a praguejar e a jurar: Não conheço esse homem! E imediatamente cantou o galo.
75 Então, Pedro se lembrou da palavra que Jesus lhe dissera: Antes que o galo cante, tu me negarás três vezes. E, saindo dali, chorou amargamente.*
1 Ao romper o dia, todos os principais sacerdotes e os anciãos do povo entraram em conselho contra Jesus, para o matarem;
2 e, amarrando-o, levaram-no e o entregaram ao governador Pilatos.
3 Então, Judas, o que o traiu, vendo que Jesus fora condenado, tocado de remorso, devolveu as trinta moedas de prata aos principais sacerdotes e aos anciãos, dizendo:
4 Pequei, traindo sangue inocente. Eles, porém, responderam: Que nos importa? Isso é contigo.
5 Então, Judas, atirando para o santuário as moedas de prata, retirou-se e foi enforcar-se.
6 E os principais sacerdotes, tomando as moedas, disseram: Não é lícito deitá-las no cofre das ofertas, porque é preço de sangue.
7 E, tendo deliberado, compraram com elas o campo do oleiro, para cemitério de forasteiros.
8 Por isso, aquele campo tem sido chamado, até ao dia de hoje, Campo de Sangue.
9 Então, se cumpriu o que foi dito por intermédio do profeta Jeremias: Tomaram as trinta moedas de prata, preço em que foi estimado aquele a quem alguns dos filhos de Israel avaliaram;
10 e as deram pelo campo do oleiro, assim como me ordenou o Senhor.
11 Jesus estava em pé ante o governador; e este o interrogou, dizendo: És tu o rei dos judeus? Respondeu-lhe Jesus: Tu o dizes.
12 E, sendo acusado pelos principais sacerdotes e pelos anciãos, nada respondeu.
13 Então, lhe perguntou Pilatos: Não ouves quantas acusações te fazem?
14 Jesus não respondeu nem uma palavra, vindo com isto a admirar-se grandemente o governador.
15 Ora, por ocasião da festa, costumava o governador soltar ao povo um dos presos, conforme eles quisessem.
16 Naquela ocasião, tinham eles um preso muito conhecido, chamado Barrabás.
17 Estando, pois, o povo reunido, perguntou-lhes Pilatos: A quem quereis que eu vos solte, a Barrabás ou a Jesus, chamado Cristo?
18 Porque sabia que, por inveja, o tinham entregado.
19 E, estando ele no tribunal, sua mulher mandou dizer-lhe: Não te envolvas com esse justo; porque hoje, em sonho, muito sofri por seu respeito.
20 Mas os principais sacerdotes e os anciãos persuadiram o povo a que pedisse Barrabás e fizesse morrer Jesus.
21 De novo, perguntou-lhes o governador: Qual dos dois quereis que eu vos solte? Responderam eles: Barrabás!
22 Replicou-lhes Pilatos: Que farei, então, de Jesus, chamado Cristo? Seja crucificado! Responderam todos.
23 Que mal fez ele? Perguntou Pilatos. Porém cada vez clamavam mais: Seja crucificado!
24 Vendo Pilatos que nada conseguia, antes, pelo contrário, aumentava o tumulto, mandando vir água, lavou as mãos perante o povo, dizendo: Estou inocente do sangue deste [justo]; fique o caso convosco!
25 E o povo todo respondeu: Caia sobre nós o seu sangue e sobre nossos filhos!
26 Então, Pilatos lhes soltou Barrabás; e, após haver açoitado a Jesus, entregou-o para ser crucificado.
27 Logo a seguir, os soldados do governador, levando Jesus para o pretório, reuniram em torno dele toda a coorte.
28 Despojando-o das vestes, cobriram-no com um manto escarlate;
29 tecendo uma coroa de espinhos, puseram-lha na cabeça e, na mão direita, um caniço; e, ajoelhando-se diante dele, o escarneciam, dizendo: Salve, rei dos judeus!
30 E, cuspindo nele, tomaram o caniço e davam-lhe com ele na cabeça.
31 Depois de o terem escarnecido, despiram-lhe o manto e o vestiram com as suas próprias vestes. Em seguida, o levaram para ser crucificado.
32 Ao saírem, encontraram um cireneu, chamado Simão, a quem obrigaram a carregar-lhe a cruz.
33 E, chegando a um lugar chamado Gólgota, que significa Lugar da Caveira,
34 deram-lhe a beber vinho com fel; mas ele, provando-o, não o quis beber.
35 Depois de o crucificarem, repartiram entre si as suas vestes, tirando a sorte.
36 E, assentados ali, o guardavam.
37 Por cima da sua cabeça puseram escrita a sua acusação: Este é Jesus, o Rei dos Judeus.
38 E foram crucificados com ele dois ladrões, um à sua direita, e outro à sua esquerda.
39 Os que iam passando blasfemavam dele, meneando a cabeça e dizendo:
40 Ó tu que destróis o santuário e em três dias o reedificas! Salva-te a ti mesmo, se és Filho de Deus, e desce da cruz!
41 De igual modo, os principais sacerdotes, com os escribas e anciãos, escarnecendo, diziam:
42 Salvou os outros, a si mesmo não pode salvar-se. É rei de Israel! Desça da cruz, e creremos nele.
43 Confiou em Deus; pois venha livrá-lo agora, se, de fato, lhe quer bem; porque disse: Sou Filho de Deus.
44 E os mesmos impropérios lhe diziam também os ladrões que haviam sido crucificados com ele.
45 Desde a hora sexta até à hora nona, houve trevas sobre toda a terra.
46 Por volta da hora nona, clamou Jesus em alta voz, dizendo: Eli, Eli, lamá sabactâni? O que quer dizer: Deus meu, Deus meu, por que me desamparaste?
47 E alguns dos que ali estavam, ouvindo isto, diziam: Ele chama por Elias.
48 E, logo, um deles correu a buscar uma esponja e, tendo-a embebido de vinagre e colocado na ponta de um caniço, deu-lhe a beber.
49 Os outros, porém, diziam: Deixa, vejamos se Elias vem salvá-lo.
50 E Jesus, clamando outra vez com grande voz, entregou o espírito.
51 Eis que o véu do santuário se rasgou em duas partes de alto a baixo; tremeu a terra, fenderam-se as rochas;
52 abriram-se os sepulcros, e muitos corpos de santos, que dormiam, ressuscitaram;
53 e, saindo dos sepulcros depois da ressurreição de Jesus, entraram na cidade santa e apareceram a muitos.
54 O centurião e os que com ele guardavam a Jesus, vendo o terremoto e tudo o que se passava, ficaram possuídos de grande temor e disseram: Verdadeiramente este era Filho de Deus.
55 Estavam ali muitas mulheres, observando de longe; eram as que vinham seguindo a Jesus desde a Galileia, para o servirem;
56 entre elas estavam Maria Madalena, Maria, mãe de Tiago e de José, e a mulher de Zebedeu.
57 Caindo a tarde, veio um homem rico de Arimateia, chamado José, que era também discípulo de Jesus.
58 Este foi ter com Pilatos e lhe pediu o corpo de Jesus. Então, Pilatos mandou que lho fosse entregue.
59 E José, tomando o corpo, envolveu-o num pano limpo de linho
60 e o depositou no seu túmulo novo, que fizera abrir na rocha; e, rolando uma grande pedra para a entrada do sepulcro, se retirou.
61 Achavam-se ali, sentadas em frente da sepultura, Maria Madalena e a outra Maria.
62 No dia seguinte, que é o dia depois da preparação, reuniram-se os principais sacerdotes e os fariseus e, dirigindo-se a Pilatos,
63 disseram-lhe: Senhor, lembramo-nos de que aquele embusteiro, enquanto vivia, disse: Depois de três dias ressuscitarei.
64 Ordena, pois, que o sepulcro seja guardado com segurança até ao terceiro dia, para não suceder que, vindo os discípulos, o roubem e depois digam ao povo: Ressuscitou dos mortos; e será o último embuste pior que o primeiro.
65 Disse-lhes Pilatos: Aí tendes uma escolta; ide e guardai o sepulcro como bem vos parecer.
66 Indo eles, montaram guarda ao sepulcro, selando a pedra e deixando ali a escolta.*
1 No findar do sábado, ao entrar o primeiro dia da semana, Maria Madalena e a outra Maria foram ver o sepulcro.
2 E eis que houve um grande terremoto; porque um anjo do Senhor desceu do céu, chegou-se, removeu a pedra e assentou-se sobre ela.
3 O seu aspecto era como um relâmpago, e a sua veste, alva como a neve.
4 E os guardas tremeram espavoridos e ficaram como se estivessem mortos.
5 Mas o anjo, dirigindo-se às mulheres, disse: Não temais; porque sei que buscais Jesus, que foi crucificado.
6 Ele não está aqui; ressuscitou, como tinha dito. Vinde ver onde ele jazia.
7 Ide, pois, depressa e dizei aos seus discípulos que ele ressuscitou dos mortos e vai adiante de vós para a Galileia; ali o vereis. É como vos digo!
8 E, retirando-se elas apressadamente do sepulcro, tomadas de medo e grande alegria, correram a anunciá-lo aos discípulos.
9 E eis que Jesus veio ao encontro delas e disse: Salve! E elas, aproximando-se, abraçaram-lhe os pés e o adoraram.
10 Então, Jesus lhes disse: Não temais! Ide avisar a meus irmãos que se dirijam à Galileia e lá me verão.
11 E, indo elas, eis que alguns da guarda foram à cidade e contaram aos principais sacerdotes tudo o que sucedera.
12 Reunindo-se eles em conselho com os anciãos, deram grande soma de dinheiro aos soldados,
13 recomendando-lhes que dissessem: Vieram de noite os discípulos dele e o roubaram enquanto dormíamos.
14 Caso isto chegue ao conhecimento do governador, nós o persuadiremos e vos poremos em segurança.
15 Eles, recebendo o dinheiro, fizeram como estavam instruídos. Esta versão divulgou-se entre os judeus até ao dia de hoje.
16 Seguiram os onze discípulos para a Galileia, para o monte que Jesus lhes designara.
17 E, quando o viram, o adoraram; mas alguns duvidaram.
18 Jesus, aproximando-se, falou-lhes, dizendo: Toda a autoridade me foi dada no céu e na terra.
19 Ide, portanto, fazei discípulos de todas as nações, batizando-os em nome do Pai, e do Filho, e do Espírito Santo;
20 ensinando-os a guardar todas as coisas que vos tenho ordenado. E eis que estou convosco todos os dias até à consumação do século.    
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Mateus','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)