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
1 Princípio do evangelho de Jesus Cristo, Filho de Deus.
2 Conforme está escrito na profecia de Isaías: Eis aí envio diante da tua face o meu mensageiro, o qual preparará o teu caminho;
3 voz do que clama no deserto: Preparai o caminho do Senhor, endireitai as suas veredas;
4 apareceu João Batista no deserto, pregando batismo de arrependimento para remissão de pecados.
5 Saíam a ter com ele toda a província da Judeia e todos os habitantes de Jerusalém; e, confessando os seus pecados, eram batizados por ele no rio Jordão.
6 As vestes de João eram feitas de pelos de camelo; ele trazia um cinto de couro e se alimentava de gafanhotos e mel silvestre.
7 E pregava, dizendo: Após mim vem aquele que é mais poderoso do que eu, do qual não sou digno de, curvando-me, desatar-lhe as correias das sandálias.
8 Eu vos tenho batizado com água; ele, porém, vos batizará com o Espírito Santo.
9 Naqueles dias, veio Jesus de Nazaré da Galileia e por João foi batizado no rio Jordão.
10 Logo ao sair da água, viu os céus rasgarem-se e o Espírito descendo como pomba sobre ele.
11 Então, foi ouvida uma voz dos céus: Tu és o meu Filho amado, em ti me comprazo.
12 E logo o Espírito o impeliu para o deserto,
13 onde permaneceu quarenta dias, sendo tentado por Satanás; estava com as feras, mas os anjos o serviam.
14 Depois de João ter sido preso, foi Jesus para a Galileia, pregando o evangelho de Deus,
15 dizendo: O tempo está cumprido, e o reino de Deus está próximo; arrependei-vos e crede no evangelho.
16 Caminhando junto ao mar da Galileia, viu os irmãos Simão e André, que lançavam a rede ao mar, porque eram pescadores.
17 Disse-lhes Jesus: Vinde após mim, e eu vos farei pescadores de homens.
18 Então, eles deixaram imediatamente as redes e o seguiram.
19 Pouco mais adiante, viu Tiago, filho de Zebedeu, e João, seu irmão, que estavam no barco consertando as redes.
20 E logo os chamou. Deixando eles no barco a seu pai Zebedeu com os empregados, seguiram após Jesus.
21 Depois, entraram em Cafarnaum, e, logo no sábado, foi ele ensinar na sinagoga.
22 Maravilhavam-se da sua doutrina, porque os ensinava como quem tem autoridade e não como os escribas.
23 Não tardou que aparecesse na sinagoga um homem possesso de espírito imundo, o qual bradou:
24 Que temos nós contigo, Jesus Nazareno? Vieste para perder-nos? Bem sei quem és: o Santo de Deus!
25 Mas Jesus o repreendeu, dizendo: Cala-te e sai desse homem.
26 Então, o espírito imundo, agitando-o violentamente e bradando em alta voz, saiu dele.
27 Todos se admiraram, a ponto de perguntarem entre si: Que vem a ser isto? Uma nova doutrina! Com autoridade ele ordena aos espíritos imundos, e eles lhe obedecem!
28 Então, correu célere a fama de Jesus em todas as direções, por toda a circunvizinhança da Galileia.
29 E, saindo eles da sinagoga, foram, com Tiago e João, diretamente para a casa de Simão e André.
30 A sogra de Simão achava-se acamada, com febre; e logo lhe falaram a respeito dela.
31 Então, aproximando-se, tomou-a pela mão; e a febre a deixou, passando ela a servi-los.
32 À tarde, ao cair do sol, trouxeram a Jesus todos os enfermos e endemoninhados.
33 Toda a cidade estava reunida à porta.
34 E ele curou muitos doentes de toda sorte de enfermidades; também expeliu muitos demônios, não lhes permitindo que falassem, porque sabiam quem ele era.
35 Tendo-se levantado alta madrugada, saiu, foi para um lugar deserto e ali orava.
36 Procuravam-no diligentemente Simão e os que com ele estavam.
37 Tendo-o encontrado, lhe disseram: Todos te buscam.
38 Jesus, porém, lhes disse: Vamos a outros lugares, às povoações vizinhas, a fim de que eu pregue também ali, pois para isso é que eu vim.
39 Então, foi por toda a Galileia, pregando nas sinagogas deles e expelindo os demônios.
40 Aproximou-se dele um leproso rogando-lhe, de joelhos: Se quiseres, podes purificar-me.
41 Jesus, profundamente compadecido, estendeu a mão, tocou-o e disse-lhe: Quero, fica limpo!
42 No mesmo instante, lhe desapareceu a lepra, e ficou limpo.
43 Fazendo-lhe, então, veemente advertência, logo o despediu
44 e lhe disse: Olha, não digas nada a ninguém; mas vai, mostra-te ao sacerdote e oferece pela tua purificação o que Moisés determinou, para servir de testemunho ao povo.
45 Mas, tendo ele saído, entrou a propalar muitas coisas e a divulgar a notícia, a ponto de não mais poder Jesus entrar publicamente em qualquer cidade, mas permanecia fora, em lugares ermos; e de toda parte vinham ter com ele.*
1 Dias depois, entrou Jesus de novo em Cafarnaum, e logo correu que ele estava em casa.
2 Muitos afluíram para ali, tantos que nem mesmo junto à porta eles achavam lugar; e anunciava-lhes a palavra.
3 Alguns foram ter com ele, conduzindo um paralítico, levado por quatro homens.
4 E, não podendo aproximar-se dele, por causa da multidão, descobriram o eirado no ponto correspondente ao em que ele estava e, fazendo uma abertura, baixaram o leito em que jazia o doente.
5 Vendo-lhes a fé, Jesus disse ao paralítico: Filho, os teus pecados estão perdoados.
6 Mas alguns dos escribas estavam assentados ali e arrazoavam em seu coração:
7 Por que fala ele deste modo? Isto é blasfêmia! Quem pode perdoar pecados, senão um, que é Deus?
8 E Jesus, percebendo logo por seu espírito que eles assim arrazoavam, disse-lhes: Por que arrazoais sobre estas coisas em vosso coração?
9 Qual é mais fácil? Dizer ao paralítico: Estão perdoados os teus pecados, ou dizer: Levanta-te, toma o teu leito e anda?
10 Ora, para que saibais que o Filho do Homem tem sobre a terra autoridade para perdoar pecados — disse ao paralítico:
11 Eu te mando: Levanta-te, toma o teu leito e vai para tua casa.
12 Então, ele se levantou e, no mesmo instante, tomando o leito, retirou-se à vista de todos, a ponto de se admirarem todos e darem glória a Deus, dizendo: Jamais vimos coisa assim!
13 De novo, saiu Jesus para junto do mar, e toda a multidão vinha ao seu encontro, e ele os ensinava.
14 Quando ia passando, viu a Levi, filho de Alfeu, sentado na coletoria e disse-lhe: Segue-me! Ele se levantou e o seguiu.
15 Achando-se Jesus à mesa na casa de Levi, estavam juntamente com ele e com seus discípulos muitos publicanos e pecadores; porque estes eram em grande número e também o seguiam.
16 Os escribas dos fariseus, vendo-o comer em companhia dos pecadores e publicanos, perguntavam aos discípulos dele: Por que come [e bebe] ele com os publicanos e pecadores?
17 Tendo Jesus ouvido isto, respondeu-lhes: Os sãos não precisam de médico, e sim os doentes; não vim chamar justos, e sim pecadores.
18 Ora, os discípulos de João e os fariseus estavam jejuando. Vieram alguns e lhe perguntaram: Por que motivo jejuam os discípulos de João e os dos fariseus, mas os teus discípulos não jejuam?
19 Respondeu-lhes Jesus: Podem, porventura, jejuar os convidados para o casamento, enquanto o noivo está com eles? Durante o tempo em que estiver presente o noivo, não podem jejuar.
20 Dias virão, contudo, em que lhes será tirado o noivo; e, nesse tempo, jejuarão.
21 Ninguém costura remendo de pano novo em veste velha; porque o remendo novo tira parte da veste velha, e fica maior a rotura.
22 Ninguém põe vinho novo em odres velhos; do contrário, o vinho romperá os odres; e tanto se perde o vinho como os odres. Mas põe-se vinho novo em odres novos.
23 Ora, aconteceu atravessar Jesus, em dia de sábado, as searas, e os discípulos, ao passarem, colhiam espigas.
24 Advertiram-no os fariseus: Vê! Por que fazem o que não é lícito aos sábados?
25 Mas ele lhes respondeu: Nunca lestes o que fez Davi, quando se viu em necessidade e teve fome, ele e os seus companheiros?
26 Como entrou na Casa de Deus, no tempo do sumo sacerdote Abiatar, e comeu os pães da proposição, os quais não é lícito comer, senão aos sacerdotes, e deu também aos que estavam com ele?
27 E acrescentou: O sábado foi estabelecido por causa do homem, e não o homem por causa do sábado;
28 de sorte que o Filho do Homem é senhor também do sábado.*
1 De novo, entrou Jesus na sinagoga e estava ali um homem que tinha ressequida uma das mãos.
2 E estavam observando a Jesus para ver se o curaria em dia de sábado, a fim de o acusarem.
3 E disse Jesus ao homem da mão ressequida: Vem para o meio!
4 Então, lhes perguntou: É lícito nos sábados fazer o bem ou fazer o mal? Salvar a vida ou tirá-la? Mas eles ficaram em silêncio.
5 Olhando-os ao redor, indignado e condoído com a dureza do seu coração, disse ao homem: Estende a mão. Estendeu-a, e a mão lhe foi restaurada.
6 Retirando-se os fariseus, conspiravam logo com os herodianos, contra ele, em como lhe tirariam a vida.
7 Retirou-se Jesus com os seus discípulos para os lados do mar. Seguia-o da Galileia uma grande multidão. Também da Judeia,
8 de Jerusalém, da Idumeia, dalém do Jordão e dos arredores de Tiro e de Sidom uma grande multidão, sabendo quantas coisas Jesus fazia, veio ter com ele.
9 Então, recomendou a seus discípulos que sempre lhe tivessem pronto um barquinho, por causa da multidão, a fim de não o comprimirem.
10 Pois curava a muitos, de modo que todos os que padeciam de qualquer enfermidade se arrojavam a ele para o tocar.
11 Também os espíritos imundos, quando o viam, prostravam-se diante dele e exclamavam: Tu és o Filho de Deus!
12 Mas Jesus lhes advertia severamente que o não expusessem à publicidade.
13 Depois, subiu ao monte e chamou os que ele mesmo quis, e vieram para junto dele.
14 Então, designou doze para estarem com ele e para os enviar a pregar
15 e a exercer a autoridade de expelir demônios.
16 Eis os doze que designou: Simão, a quem acrescentou o nome de Pedro;
17 Tiago, filho de Zebedeu, e João, seu irmão, aos quais deu o nome de Boanerges, que quer dizer: filhos do trovão;
18 André, Filipe, Bartolomeu, Mateus, Tomé, Tiago, filho de Alfeu, Tadeu, Simão, o Zelote,
19 e Judas Iscariotes, que foi quem o traiu.
20 Então, ele foi para casa. Não obstante, a multidão afluiu de novo, de tal modo que nem podiam comer.
21 E, quando os parentes de Jesus ouviram isto, saíram para o prender; porque diziam: Está fora de si.
22 Os escribas, que haviam descido de Jerusalém, diziam: Ele está possesso de Belzebu. E: É pelo maioral dos demônios que expele os demônios.
23 Então, convocando-os Jesus, lhes disse, por meio de parábolas: Como pode Satanás expelir a Satanás?
24 Se um reino estiver dividido contra si mesmo, tal reino não pode subsistir;
25 se uma casa estiver dividida contra si mesma, tal casa não poderá subsistir.
26 Se, pois, Satanás se levantou contra si mesmo e está dividido, não pode subsistir, mas perece.
27 Ninguém pode entrar na casa do valente para roubar-lhe os bens, sem primeiro amarrá-lo; e só então lhe saqueará a casa.
28 Em verdade vos digo que tudo será perdoado aos filhos dos homens: os pecados e as blasfêmias que proferirem.
29 Mas aquele que blasfemar contra o Espírito Santo não tem perdão para sempre, visto que é réu de pecado eterno.
30 Isto, porque diziam: Está possesso de um espírito imundo.
31 Nisto, chegaram sua mãe e seus irmãos e, tendo ficado do lado de fora, mandaram chamá-lo.
32 Muita gente estava assentada ao redor dele e lhe disseram: Olha, tua mãe, teus irmãos e irmãs estão lá fora à tua procura.
33 Então, ele lhes respondeu, dizendo: Quem é minha mãe e meus irmãos?
34 E, correndo o olhar pelos que estavam assentados ao redor, disse: Eis minha mãe e meus irmãos.
35 Portanto, qualquer que fizer a vontade de Deus, esse é meu irmão, irmã e mãe.*
1 Voltou Jesus a ensinar à beira-mar. E reuniu-se numerosa multidão a ele, de modo que entrou num barco, onde se assentou, afastando-se da praia. E todo o povo estava à beira-mar, na praia.
2 Assim, lhes ensinava muitas coisas por parábolas, no decorrer do seu doutrinamento.
3 Ouvi: Eis que saiu o semeador a semear.
4 E, ao semear, uma parte caiu à beira do caminho, e vieram as aves e a comeram.
5 Outra caiu em solo rochoso, onde a terra era pouca, e logo nasceu, visto não ser profunda a terra.
6 Saindo, porém, o sol, a queimou; e, porque não tinha raiz, secou-se.
7 Outra parte caiu entre os espinhos; e os espinhos cresceram e a sufocaram, e não deu fruto.
8 Outra, enfim, caiu em boa terra e deu fruto, que vingou e cresceu, produzindo a trinta, a sessenta e a cem por um.
9 E acrescentou: Quem tem ouvidos para ouvir, ouça.
10 Quando Jesus ficou só, os que estavam junto dele com os doze o interrogaram a respeito das parábolas.
11 Ele lhes respondeu: A vós outros vos é dado conhecer o mistério do reino de Deus; mas, aos de fora, tudo se ensina por meio de parábolas,
12 para que, vendo, vejam e não percebam; e, ouvindo, ouçam e não entendam; para que não venham a converter-se, e haja perdão para eles.
13 Então, lhes perguntou: Não entendeis esta parábola e como compreendereis todas as parábolas?
14 O semeador semeia a palavra.
15 São estes os da beira do caminho, onde a palavra é semeada; e, enquanto a ouvem, logo vem Satanás e tira a palavra semeada neles.
16 Semelhantemente, são estes os semeados em solo rochoso, os quais, ouvindo a palavra, logo a recebem com alegria.
17 Mas eles não têm raiz em si mesmos, sendo, antes, de pouca duração; em lhes chegando a angústia ou a perseguição por causa da palavra, logo se escandalizam.
18 Os outros, os semeados entre os espinhos, são os que ouvem a palavra,
19 mas os cuidados do mundo, a fascinação da riqueza e as demais ambições, concorrendo, sufocam a palavra, ficando ela infrutífera.
20 Os que foram semeados em boa terra são aqueles que ouvem a palavra e a recebem, frutificando a trinta, a sessenta e a cem por um.
21 Também lhes disse: Vem, porventura, a candeia para ser posta debaixo do alqueire ou da cama? Não vem, antes, para ser colocada no velador?
22 Pois nada está oculto, senão para ser manifesto; e nada se faz escondido, senão para ser revelado.
23 Se alguém tem ouvidos para ouvir, ouça.
24 Então, lhes disse: Atentai no que ouvis. Com a medida com que tiverdes medido vos medirão também, e ainda se vos acrescentará.
25 Pois ao que tem se lhe dará; e, ao que não tem, até o que tem lhe será tirado.
26 Disse ainda: O reino de Deus é assim como se um homem lançasse a semente à terra;
27 depois, dormisse e se levantasse, de noite e de dia, e a semente germinasse e crescesse, não sabendo ele como.
28 A terra por si mesma frutifica: primeiro a erva, depois, a espiga, e, por fim, o grão cheio na espiga.
29 E, quando o fruto já está maduro, logo se lhe mete a foice, porque é chegada a ceifa.
30 Disse mais: A que assemelharemos o reino de Deus? Ou com que parábola o apresentaremos?
31 É como um grão de mostarda, que, quando semeado, é a menor de todas as sementes sobre a terra;
32 mas, uma vez semeada, cresce e se torna maior do que todas as hortaliças e deita grandes ramos, a ponto de as aves do céu poderem aninhar-se à sua sombra.
33 E com muitas parábolas semelhantes lhes expunha a palavra, conforme o permitia a capacidade dos ouvintes.
34 E sem parábolas não lhes falava; tudo, porém, explicava em particular aos seus próprios discípulos.
35 Naquele dia, sendo já tarde, disse-lhes Jesus: Passemos para a outra margem.
36 E eles, despedindo a multidão, o levaram assim como estava, no barco; e outros barcos o seguiam.
37 Ora, levantou-se grande temporal de vento, e as ondas se arremessavam contra o barco, de modo que o mesmo já estava a encher-se de água.
38 E Jesus estava na popa, dormindo sobre o travesseiro; eles o despertaram e lhe disseram: Mestre, não te importa que pereçamos?
39 E ele, despertando, repreendeu o vento e disse ao mar: Acalma-te, emudece! O vento se aquietou, e fez-se grande bonança.
40 Então, lhes disse: Por que sois assim tímidos?! Como é que não tendes fé?
41 E eles, possuídos de grande temor, diziam uns aos outros: Quem é este que até o vento e o mar lhe obedecem?*
1 Entrementes, chegaram à outra margem do mar, à terra dos gerasenos.
2 Ao desembarcar, logo veio dos sepulcros, ao seu encontro, um homem possesso de espírito imundo,
3 o qual vivia nos sepulcros, e nem mesmo com cadeias alguém podia prendê-lo;
4 porque, tendo sido muitas vezes preso com grilhões e cadeias, as cadeias foram quebradas por ele, e os grilhões, despedaçados. E ninguém podia subjugá-lo.
5 Andava sempre, de noite e de dia, clamando por entre os sepulcros e pelos montes, ferindo-se com pedras.
6 Quando, de longe, viu Jesus, correu e o adorou,
7 exclamando com alta voz: Que tenho eu contigo, Jesus, Filho do Deus Altíssimo? Conjuro-te por Deus que não me atormentes!
8 Porque Jesus lhe dissera: Espírito imundo, sai desse homem!
9 E perguntou-lhe: Qual é o teu nome? Respondeu ele: Legião é o meu nome, porque somos muitos.
10 E rogou-lhe encarecidamente que os não mandasse para fora do país.
11 Ora, pastava ali pelo monte uma grande manada de porcos.
12 E os espíritos imundos rogaram a Jesus, dizendo: Manda-nos para os porcos, para que entremos neles.
13 Jesus o permitiu. Então, saindo os espíritos imundos, entraram nos porcos; e a manada, que era cerca de dois mil, precipitou-se despenhadeiro abaixo, para dentro do mar, onde se afogaram.
14 Os porqueiros fugiram e o anunciaram na cidade e pelos campos. Então, saiu o povo para ver o que sucedera.
15 Indo ter com Jesus, viram o endemoninhado, o que tivera a legião, assentado, vestido, em perfeito juízo; e temeram.
16 Os que haviam presenciado os fatos contaram-lhes o que acontecera ao endemoninhado e acerca dos porcos.
17 E entraram a rogar-lhe que se retirasse da terra deles.
18 Ao entrar Jesus no barco, suplicava-lhe o que fora endemoninhado que o deixasse estar com ele.
19 Jesus, porém, não lho permitiu, mas ordenou-lhe: Vai para tua casa, para os teus. Anuncia-lhes tudo o que o Senhor te fez e como teve compaixão de ti.
20 Então, ele foi e começou a proclamar em Decápolis tudo o que Jesus lhe fizera; e todos se admiravam.
21 Tendo Jesus voltado no barco, para o outro lado, afluiu para ele grande multidão; e ele estava junto do mar.
22 Eis que se chegou a ele um dos principais da sinagoga, chamado Jairo, e, vendo-o, prostrou-se a seus pés
23 e insistentemente lhe suplicou: Minha filhinha está à morte; vem, impõe as mãos sobre ela, para que seja salva, e viverá.
24 Jesus foi com ele. Grande multidão o seguia, comprimindo-o.
25 Aconteceu que certa mulher, que, havia doze anos, vinha sofrendo de uma hemorragia
26 e muito padecera à mão de vários médicos, tendo despendido tudo quanto possuía, sem, contudo, nada aproveitar, antes, pelo contrário, indo a pior,
27 tendo ouvido a fama de Jesus, vindo por trás dele, por entre a multidão, tocou-lhe a veste.
28 Porque, dizia: Se eu apenas lhe tocar as vestes, ficarei curada.
29 E logo se lhe estancou a hemorragia, e sentiu no corpo estar curada do seu flagelo.
30 Jesus, reconhecendo imediatamente que dele saíra poder, virando-se no meio da multidão, perguntou: Quem me tocou nas vestes?
31 Responderam-lhe seus discípulos: Vês que a multidão te aperta e dizes: Quem me tocou?
32 Ele, porém, olhava ao redor para ver quem fizera isto.
33 Então, a mulher, atemorizada e tremendo, cônscia do que nela se operara, veio, prostrou-se diante dele e declarou-lhe toda a verdade.
34 E ele lhe disse: Filha, a tua fé te salvou; vai-te em paz e fica livre do teu mal.
35 Falava ele ainda, quando chegaram alguns da casa do chefe da sinagoga, a quem disseram: Tua filha já morreu; por que ainda incomodas o Mestre?
36 Mas Jesus, sem acudir a tais palavras, disse ao chefe da sinagoga: Não temas, crê somente.
37 Contudo, não permitiu que alguém o acompanhasse, senão Pedro e os irmãos Tiago e João.
38 Chegando à casa do chefe da sinagoga, viu Jesus o alvoroço, os que choravam e os que pranteavam muito.
39 Ao entrar, lhes disse: Por que estais em alvoroço e chorais? A criança não está morta, mas dorme.
40 E riam-se dele. Tendo ele, porém, mandado sair a todos, tomou o pai e a mãe da criança e os que vieram com ele e entrou onde ela estava.
41 Tomando-a pela mão, disse: Talitá cumi!, que quer dizer: Menina, eu te mando, levanta-te!
42 Imediatamente, a menina se levantou e pôs-se a andar; pois tinha doze anos. Então, ficaram todos sobremaneira admirados.
43 Mas Jesus ordenou-lhes expressamente que ninguém o soubesse; e mandou que dessem de comer à menina.*
1 Tendo Jesus partido dali, foi para a sua terra, e os seus discípulos o acompanharam.
2 Chegando o sábado, passou a ensinar na sinagoga; e muitos, ouvindo-o, se maravilhavam, dizendo: Donde vêm a este estas coisas? Que sabedoria é esta que lhe foi dada? E como se fazem tais maravilhas por suas mãos?
3 Não é este o carpinteiro, filho de Maria, irmão de Tiago, José, Judas e Simão? E não vivem aqui entre nós suas irmãs? E escandalizavam-se nele.
4 Jesus, porém, lhes disse: Não há profeta sem honra, senão na sua terra, entre os seus parentes e na sua casa.
5 Não pôde fazer ali nenhum milagre, senão curar uns poucos enfermos, impondo-lhes as mãos.
6 Admirou-se da incredulidade deles. Contudo, percorria as aldeias circunvizinhas, a ensinar.
7 Chamou Jesus os doze e passou a enviá-los de dois a dois, dando-lhes autoridade sobre os espíritos imundos.
8 Ordenou-lhes que nada levassem para o caminho, exceto um bordão; nem pão, nem alforje, nem dinheiro;
9 que fossem calçados de sandálias e não usassem duas túnicas.
10 E recomendou-lhes: Quando entrardes nalguma casa, permanecei aí até vos retirardes do lugar.
11 Se nalgum lugar não vos receberem nem vos ouvirem, ao sairdes dali, sacudi o pó dos pés, em testemunho contra eles.
12 Então, saindo eles, pregavam ao povo que se arrependesse;
13 expeliam muitos demônios e curavam numerosos enfermos, ungindo-os com óleo.
14 Chegou isto aos ouvidos do rei Herodes, porque o nome de Jesus já se tornara notório; e alguns diziam: João Batista ressuscitou dentre os mortos, e, por isso, nele operam forças miraculosas.
15 Outros diziam: É Elias; ainda outros: É profeta como um dos profetas.
16 Herodes, porém, ouvindo isto, disse: É João, a quem eu mandei decapitar, que ressurgiu.
17 Porque o mesmo Herodes, por causa de Herodias, mulher de seu irmão Filipe (porquanto Herodes se casara com ela), mandara prender a João e atá-lo no cárcere.
18 Pois João lhe dizia: Não te é lícito possuir a mulher de teu irmão.
19 E Herodias o odiava, querendo matá-lo, e não podia.
20 Porque Herodes temia a João, sabendo que era homem justo e santo, e o tinha em segurança. E, quando o ouvia, ficava perplexo, escutando-o de boa mente.
21 E, chegando um dia favorável, em que Herodes no seu aniversário natalício dera um banquete aos seus dignitários, aos oficiais militares e aos principais da Galileia,
22 entrou a filha de Herodias e, dançando, agradou a Herodes e aos seus convivas. Então, disse o rei à jovem: Pede-me o que quiseres, e eu to darei.
23 E jurou-lhe: Se pedires mesmo que seja a metade do meu reino, eu ta darei.
24 Saindo ela, perguntou à sua mãe: Que pedirei? Esta respondeu: A cabeça de João Batista.
25 No mesmo instante, voltando apressadamente para junto do rei, disse: Quero que, sem demora, me dês num prato a cabeça de João Batista.
26 Entristeceu-se profundamente o rei; mas, por causa do juramento e dos que estavam com ele à mesa, não lha quis negar.
27 E, enviando logo o executor, mandou que lhe trouxessem a cabeça de João. Ele foi, e o decapitou no cárcere,
28 e, trazendo a cabeça num prato, a entregou à jovem, e esta, por sua vez, a sua mãe.
29 Os discípulos de João, logo que souberam disto, vieram, levaram-lhe o corpo e o depositaram no túmulo.
30 Voltaram os apóstolos à presença de Jesus e lhe relataram tudo quanto haviam feito e ensinado.
31 E ele lhes disse: Vinde repousar um pouco, à parte, num lugar deserto; porque eles não tinham tempo nem para comer, visto serem numerosos os que iam e vinham.
32 Então, foram sós no barco para um lugar solitário.
33 Muitos, porém, os viram partir e, reconhecendo-os, correram para lá, a pé, de todas as cidades, e chegaram antes deles.
34 Ao desembarcar, viu Jesus uma grande multidão e compadeceu-se deles, porque eram como ovelhas que não têm pastor. E passou a ensinar-lhes muitas coisas.
35 Em declinando a tarde, vieram os discípulos a Jesus e lhe disseram: É deserto este lugar, e já avançada a hora;
36 despede-os para que, passando pelos campos ao redor e pelas aldeias, comprem para si o que comer.
37 Porém ele lhes respondeu: Dai-lhes vós mesmos de comer. Disseram-lhe: Iremos comprar duzentos denários de pão para lhes dar de comer?
38 E ele lhes disse: Quantos pães tendes? Ide ver! E, sabendo-o eles, responderam: Cinco pães e dois peixes.
39 Então, Jesus lhes ordenou que todos se assentassem, em grupos, sobre a relva verde.
40 E o fizeram, repartindo-se em grupos de cem em cem e de cinquenta em cinquenta.
41 Tomando ele os cinco pães e os dois peixes, erguendo os olhos ao céu, os abençoou; e, partindo os pães, deu-os aos discípulos para que os distribuíssem; e por todos repartiu também os dois peixes.
42 Todos comeram e se fartaram;
43 e ainda recolheram doze cestos cheios de pedaços de pão e de peixe.
44 Os que comeram dos pães eram cinco mil homens.
45 Logo a seguir, compeliu Jesus os seus discípulos a embarcar e passar adiante para o outro lado, a Betsaida, enquanto ele despedia a multidão.
46 E, tendo-os despedido, subiu ao monte para orar.
47 Ao cair da tarde, estava o barco no meio do mar, e ele, sozinho em terra.
48 E, vendo-os em dificuldade a remar, porque o vento lhes era contrário, por volta da quarta vigília da noite, veio ter com eles, andando por sobre o mar; e queria tomar-lhes a dianteira.
49 Eles, porém, vendo-o andar sobre o mar, pensaram tratar-se de um fantasma e gritaram.
50 Pois todos ficaram aterrados à vista dele. Mas logo lhes falou e disse: Tende bom ânimo! Sou eu. Não temais!
51 E subiu para o barco para estar com eles, e o vento cessou. Ficaram entre si atônitos,
52 porque não haviam compreendido o milagre dos pães; antes, o seu coração estava endurecido.
53 Estando já no outro lado, chegaram a terra, em Genesaré, onde aportaram.
54 Saindo eles do barco, logo o povo reconheceu Jesus;
55 e, percorrendo toda aquela região, traziam em leitos os enfermos, para onde ouviam que ele estava.
56 Onde quer que ele entrasse nas aldeias, cidades ou campos, punham os enfermos nas praças, rogando-lhe que os deixasse tocar ao menos na orla da sua veste; e quantos a tocavam saíam curados.*
1 Ora, reuniram-se a Jesus os fariseus e alguns escribas, vindos de Jerusalém.
2 E, vendo que alguns dos discípulos dele comiam pão com as mãos impuras, isto é, por lavar
3 (pois os fariseus e todos os judeus, observando a tradição dos anciãos, não comem sem lavar cuidadosamente as mãos;
4 quando voltam da praça, não comem sem se aspergirem; e há muitas outras coisas que receberam para observar, como a lavagem de copos, jarros e vasos de metal [e camas]),
5 interpelaram-no os fariseus e os escribas: Por que não andam os teus discípulos de conformidade com a tradição dos anciãos, mas comem com as mãos por lavar?
6 Respondeu-lhes: Bem profetizou Isaías a respeito de vós, hipócritas, como está escrito: Este povo honra-me com os lábios, mas o seu coração está longe de mim.
7 E em vão me adoram, ensinando doutrinas que são preceitos de homens.
8 Negligenciando o mandamento de Deus, guardais a tradição dos homens.
9 E disse-lhes ainda: Jeitosamente rejeitais o preceito de Deus para guardardes a vossa própria tradição.
10 Pois Moisés disse: Honra a teu pai e a tua mãe; e: Quem maldisser a seu pai ou a sua mãe seja punido de morte.
11 Vós, porém, dizeis: Se um homem disser a seu pai ou a sua mãe: Aquilo que poderias aproveitar de mim é Corbã, isto é, oferta para o Senhor,
12 então, o dispensais de fazer qualquer coisa em favor de seu pai ou de sua mãe,
13 invalidando a palavra de Deus pela vossa própria tradição, que vós mesmos transmitistes; e fazeis muitas outras coisas semelhantes.
14 Convocando ele, de novo, a multidão, disse-lhes: Ouvi-me, todos, e entendei.
15 Nada há fora do homem que, entrando nele, o possa contaminar; mas o que sai do homem é o que o contamina.
16 [Se alguém tem ouvidos para ouvir, ouça.]
17 Quando entrou em casa, deixando a multidão, os seus discípulos o interrogaram acerca da parábola.
18 Então, lhes disse: Assim vós também não entendeis? Não compreendeis que tudo o que de fora entra no homem não o pode contaminar,
19 porque não lhe entra no coração, mas no ventre, e sai para lugar escuso? E, assim, considerou ele puros todos os alimentos.
20 E dizia: O que sai do homem, isso é o que o contamina.
21 Porque de dentro, do coração dos homens, é que procedem os maus desígnios, a prostituição, os furtos, os homicídios, os adultérios,
22 a avareza, as malícias, o dolo, a lascívia, a inveja, a blasfêmia, a soberba, a loucura.
23 Ora, todos estes males vêm de dentro e contaminam o homem.
24 Levantando-se, partiu dali para as terras de Tiro [e Sidom]. Tendo entrado numa casa, queria que ninguém o soubesse; no entanto, não pôde ocultar-se,
25 porque uma mulher, cuja filhinha estava possessa de espírito imundo, tendo ouvido a respeito dele, veio e prostrou-se-lhe aos pés.
26 Esta mulher era grega, de origem siro-fenícia, e rogava-lhe que expelisse de sua filha o demônio.
27 Mas Jesus lhe disse: Deixa primeiro que se fartem os filhos, porque não é bom tomar o pão dos filhos e lançá-lo aos cachorrinhos.
28 Ela, porém, lhe respondeu: Sim, Senhor; mas os cachorrinhos, debaixo da mesa, comem das migalhas das crianças.
29 Então, lhe disse: Por causa desta palavra, podes ir; o demônio já saiu de tua filha.
30 Voltando ela para casa, achou a menina sobre a cama, pois o demônio a deixara.
31 De novo, se retirou das terras de Tiro e foi por Sidom até ao mar da Galileia, através do território de Decápolis.
32 Então, lhe trouxeram um surdo e gago e lhe suplicaram que impusesse as mãos sobre ele.
33 Jesus, tirando-o da multidão, à parte, pôs-lhe os dedos nos ouvidos e lhe tocou a língua com saliva;
34 depois, erguendo os olhos ao céu, suspirou e disse: Efatá!, que quer dizer: Abre-te!
35 Abriram-se-lhe os ouvidos, e logo se lhe soltou o empecilho da língua, e falava desembaraçadamente.
36 Mas lhes ordenou que a ninguém o dissessem; contudo, quanto mais recomendava, tanto mais eles o divulgavam.
37 Maravilhavam-se sobremaneira, dizendo: Tudo ele tem feito esplendidamente bem; não somente faz ouvir os surdos, como falar os mudos.*
1 Naqueles dias, quando outra vez se reuniu grande multidão, e não tendo eles o que comer, chamou Jesus os discípulos e lhes disse:
2 Tenho compaixão desta gente, porque há três dias que permanecem comigo e não têm o que comer.
3 Se eu os despedir para suas casas, em jejum, desfalecerão pelo caminho; e alguns deles vieram de longe.
4 Mas os seus discípulos lhe responderam: Donde poderá alguém fartá-los de pão neste deserto?
5 E Jesus lhes perguntou: Quantos pães tendes? Responderam eles: Sete.
6 Ordenou ao povo que se assentasse no chão. E, tomando os sete pães, partiu-os, após ter dado graças, e os deu a seus discípulos, para que estes os distribuíssem, repartindo entre o povo.
7 Tinham também alguns peixinhos; e, abençoando-os, mandou que estes igualmente fossem distribuídos.
8 Comeram e se fartaram; e dos pedaços restantes recolheram sete cestos.
9 Eram cerca de quatro mil homens. Então, Jesus os despediu.
10 Logo a seguir, tendo embarcado juntamente com seus discípulos, partiu para as regiões de Dalmanuta.
11 E, saindo os fariseus, puseram-se a discutir com ele; e, tentando-o, pediram-lhe um sinal do céu.
12 Jesus, porém, arrancou do íntimo do seu espírito um gemido e disse: Por que pede esta geração um sinal? Em verdade vos digo que a esta geração não se lhe dará sinal algum.
13 E, deixando-os, tornou a embarcar e foi para o outro lado.
14 Ora, aconteceu que eles se esqueceram de levar pães e, no barco, não tinham consigo senão um só.
15 Preveniu-os Jesus, dizendo: Vede, guardai-vos do fermento dos fariseus e do fermento de Herodes.
16 E eles discorriam entre si: É que não temos pão.
17 Jesus, percebendo-o, lhes perguntou: Por que discorreis sobre o não terdes pão? Ainda não considerastes, nem compreendestes? Tendes o coração endurecido?
18 Tendo olhos, não vedes? E, tendo ouvidos, não ouvis? Não vos lembrais
19 de quando parti os cinco pães para os cinco mil, quantos cestos cheios de pedaços recolhestes? Responderam eles: Doze!
20 E de quando parti os sete pães para os quatro mil, quantos cestos cheios de pedaços recolhestes? Responderam: Sete!
21 Ao que lhes disse Jesus: Não compreendeis ainda?
22 Então, chegaram a Betsaida; e lhe trouxeram um cego, rogando-lhe que o tocasse.
23 Jesus, tomando o cego pela mão, levou-o para fora da aldeia e, aplicando-lhe saliva aos olhos e impondo-lhe as mãos, perguntou-lhe: Vês alguma coisa?
24 Este, recobrando a vista, respondeu: Vejo os homens, porque como árvores os vejo, andando.
25 Então, novamente lhe pôs as mãos nos olhos, e ele, passando a ver claramente, ficou restabelecido; e tudo distinguia de modo perfeito.
26 E mandou-o Jesus embora para casa, recomendando-lhe: Não entres na aldeia.
27 Então, Jesus e os seus discípulos partiram para as aldeias de Cesareia de Filipe; e, no caminho, perguntou-lhes: Quem dizem os homens que sou eu?
28 E responderam: João Batista; outros: Elias; mas outros: Algum dos profetas.
29 Então, lhes perguntou: Mas vós, quem dizeis que eu sou? Respondendo, Pedro lhe disse: Tu és o Cristo.
30 Advertiu-os Jesus de que a ninguém dissessem tal coisa a seu respeito.
31 Então, começou ele a ensinar-lhes que era necessário que o Filho do Homem sofresse muitas coisas, fosse rejeitado pelos anciãos, pelos principais sacerdotes e pelos escribas, fosse morto e que, depois de três dias, ressuscitasse.
32 E isto ele expunha claramente. Mas Pedro, chamando-o à parte, começou a reprová-lo.
33 Jesus, porém, voltou-se e, fitando os seus discípulos, repreendeu a Pedro e disse: Arreda, Satanás! Porque não cogitas das coisas de Deus, e sim das dos homens.
34 Então, convocando a multidão e juntamente os seus discípulos, disse-lhes: Se alguém quer vir após mim, a si mesmo se negue, tome a sua cruz e siga-me.
35 Quem quiser, pois, salvar a sua vida perdê-la-á; e quem perder a vida por causa de mim e do evangelho salvá-la-á.
36 Que aproveita ao homem ganhar o mundo inteiro e perder a sua alma?
37 Que daria um homem em troca de sua alma?
38 Porque qualquer que, nesta geração adúltera e pecadora, se envergonhar de mim e das minhas palavras, também o Filho do Homem se envergonhará dele, quando vier na glória de seu Pai com os santos anjos.*
1 Dizia-lhes ainda: Em verdade vos afirmo que, dos que aqui se encontram, alguns há que, de maneira nenhuma, passarão pela morte até que vejam ter chegado com poder o reino de Deus.
2 Seis dias depois, tomou Jesus consigo a Pedro, Tiago e João e levou-os sós, à parte, a um alto monte. Foi transfigurado diante deles;
3 as suas vestes tornaram-se resplandecentes e sobremodo brancas, como nenhum lavandeiro na terra as poderia alvejar.
4 Apareceu-lhes Elias com Moisés, e estavam falando com Jesus.
5 Então, Pedro, tomando a palavra, disse: Mestre, bom é estarmos aqui e que façamos três tendas: uma será tua, outra, para Moisés, e outra, para Elias.
6 Pois não sabia o que dizer, por estarem eles aterrados.
7 A seguir, veio uma nuvem que os envolveu; e dela uma voz dizia: Este é o meu Filho amado; a ele ouvi.
8 E, de relance, olhando ao redor, a ninguém mais viram com eles, senão Jesus.
9 Ao descerem do monte, ordenou-lhes Jesus que não divulgassem as coisas que tinham visto, até o dia em que o Filho do Homem ressuscitasse dentre os mortos.
10 Eles guardaram a recomendação, perguntando uns aos outros que seria o ressuscitar dentre os mortos.
11 E interrogaram-no, dizendo: Por que dizem os escribas ser necessário que Elias venha primeiro?
12 Então, ele lhes disse: Elias, vindo primeiro, restaurará todas as coisas; como, pois, está escrito sobre o Filho do Homem que sofrerá muito e será aviltado?
13 Eu, porém, vos digo que Elias já veio, e fizeram com ele tudo o que quiseram, como a seu respeito está escrito.
14 Quando eles se aproximaram dos discípulos, viram numerosa multidão ao redor e que os escribas discutiam com eles.
15 E logo toda a multidão, ao ver Jesus, tomada de surpresa, correu para ele e o saudava.
16 Então, ele interpelou os escribas: Que é que discutíeis com eles?
17 E um, dentre a multidão, respondeu: Mestre, trouxe-te o meu filho, possesso de um espírito mudo;
18 e este, onde quer que o apanha, lança-o por terra, e ele espuma, rilha os dentes e vai definhando. Roguei a teus discípulos que o expelissem, e eles não puderam.
19 Então, Jesus lhes disse: Ó geração incrédula, até quando estarei convosco? Até quando vos sofrerei? Trazei-mo.
20 E trouxeram-lho; quando ele viu a Jesus, o espírito imediatamente o agitou com violência, e, caindo ele por terra, revolvia-se espumando.
21 Perguntou Jesus ao pai do menino: Há quanto tempo isto lhe sucede? Desde a infância, respondeu;
22 e muitas vezes o tem lançado no fogo e na água, para o matar; mas, se tu podes alguma coisa, tem compaixão de nós e ajuda-nos.
23 Ao que lhe respondeu Jesus: Se podes! Tudo é possível ao que crê.
24 E imediatamente o pai do menino exclamou [com lágrimas]: Eu creio! Ajuda-me na minha falta de fé!
25 Vendo Jesus que a multidão concorria, repreendeu o espírito imundo, dizendo-lhe: Espírito mudo e surdo, eu te ordeno: Sai deste jovem e nunca mais tornes a ele.
26 E ele, clamando e agitando-o muito, saiu, deixando-o como se estivesse morto, a ponto de muitos dizerem: Morreu.
27 Mas Jesus, tomando-o pela mão, o ergueu, e ele se levantou.
28 Quando entrou em casa, os seus discípulos lhe perguntaram em particular: Por que não pudemos nós expulsá-lo?
29 Respondeu-lhes: Esta casta não pode sair senão por meio de oração [e jejum].
30 E, tendo partido dali, passavam pela Galileia, e não queria que ninguém o soubesse;
31 porque ensinava os seus discípulos e lhes dizia: O Filho do Homem será entregue nas mãos dos homens, e o matarão; mas, três dias depois da sua morte, ressuscitará.
32 Eles, contudo, não compreendiam isto e temiam interrogá-lo.
33 Tendo eles partido para Cafarnaum, estando ele em casa, interrogou os discípulos: De que é que discorríeis pelo caminho?
34 Mas eles guardaram silêncio; porque, pelo caminho, haviam discutido entre si sobre quem era o maior.
35 E ele, assentando-se, chamou os doze e lhes disse: Se alguém quer ser o primeiro, será o último e servo de todos.
36 Trazendo uma criança, colocou-a no meio deles e, tomando-a nos braços, disse-lhes:
37 Qualquer que receber uma criança, tal como esta, em meu nome, a mim me recebe; e qualquer que a mim me receber, não recebe a mim, mas ao que me enviou.
38 Disse-lhe João: Mestre, vimos um homem que, em teu nome, expelia demônios, o qual não nos segue; e nós lho proibimos, porque não seguia conosco.
39 Mas Jesus respondeu: Não lho proibais; porque ninguém há que faça milagre em meu nome e, logo a seguir, possa falar mal de mim.
40 Pois quem não é contra nós é por nós.
41 Porquanto, aquele que vos der de beber um copo de água, em meu nome, porque sois de Cristo, em verdade vos digo que de modo algum perderá o seu galardão.
42 E quem fizer tropeçar a um destes pequeninos crentes, melhor lhe fora que se lhe pendurasse ao pescoço uma grande pedra de moinho, e fosse lançado no mar.
43 E, se tua mão te faz tropeçar, corta-a; pois é melhor entrares maneta na vida do que, tendo as duas mãos, ires para o inferno, para o fogo inextinguível
44 [onde não lhes morre o verme, nem o fogo se apaga].
45 E, se teu pé te faz tropeçar, corta-o; é melhor entrares na vida aleijado do que, tendo os dois pés, seres lançado no inferno
46 [onde não lhes morre o verme, nem o fogo se apaga].
47 E, se um dos teus olhos te faz tropeçar, arranca-o; é melhor entrares no reino de Deus com um só dos teus olhos do que, tendo os dois seres lançado no inferno,
48 onde não lhes morre o verme, nem o fogo se apaga.
49 Porque cada um será salgado com fogo.
50 Bom é o sal; mas, se o sal vier a tornar-se insípido, como lhe restaurar o sabor? Tende sal em vós mesmos e paz uns com os outros.*
1 Levantando-se Jesus, foi dali para o território da Judeia, além do Jordão. E outra vez as multidões se reuniram junto a ele, e, de novo, ele as ensinava, segundo o seu costume.
2 E, aproximando-se alguns fariseus, o experimentaram, perguntando-lhe: É lícito ao marido repudiar sua mulher?
3 Ele lhes respondeu: Que vos ordenou Moisés?
4 Tornaram eles: Moisés permitiu lavrar carta de divórcio e repudiar.
5 Mas Jesus lhes disse: Por causa da dureza do vosso coração, ele vos deixou escrito esse mandamento;
6 porém, desde o princípio da criação, Deus os fez homem e mulher.
7 Por isso, deixará o homem a seu pai e mãe [e unir-se-á a sua mulher],
8 e, com sua mulher, serão os dois uma só carne. De modo que já não são dois, mas uma só carne.
9 Portanto, o que Deus ajuntou não separe o homem.
10 Em casa, voltaram os discípulos a interrogá-lo sobre este assunto.
11 E ele lhes disse: Quem repudiar sua mulher e casar com outra comete adultério contra aquela.
12 E, se ela repudiar seu marido e casar com outro, comete adultério.
13 Então, lhe trouxeram algumas crianças para que as tocasse, mas os discípulos os repreendiam.
14 Jesus, porém, vendo isto, indignou-se e disse-lhes: Deixai vir a mim os pequeninos, não os embaraceis, porque dos tais é o reino de Deus.
15 Em verdade vos digo: Quem não receber o reino de Deus como uma criança de maneira nenhuma entrará nele.
16 Então, tomando-as nos braços e impondo-lhes as mãos, as abençoava.
17 E, pondo-se Jesus a caminho, correu um homem ao seu encontro e, ajoelhando-se, perguntou-lhe: Bom Mestre, que farei para herdar a vida eterna?
18 Respondeu-lhe Jesus: Por que me chamas bom? Ninguém é bom senão um, que é Deus.
19 Sabes os mandamentos: Não matarás, não adulterarás, não furtarás, não dirás falso testemunho, não defraudarás ninguém, honra a teu pai e tua mãe.
20 Então, ele respondeu: Mestre, tudo isso tenho observado desde a minha juventude.
21 E Jesus, fitando-o, o amou e disse: Só uma coisa te falta: Vai, vende tudo o que tens, dá-o aos pobres e terás um tesouro no céu; então, vem e segue-me.
22 Ele, porém, contrariado com esta palavra, retirou-se triste, porque era dono de muitas propriedades.
23 Então, Jesus, olhando ao redor, disse aos seus discípulos: Quão dificilmente entrarão no reino de Deus os que têm riquezas!
24 Os discípulos estranharam estas palavras; mas Jesus insistiu em dizer-lhes: Filhos, quão difícil é [para os que confiam nas riquezas] entrar no reino de Deus!
25 É mais fácil passar um camelo pelo fundo de uma agulha do que entrar um rico no reino de Deus.
26 Eles ficaram sobremodo maravilhados, dizendo entre si: Então, quem pode ser salvo?
27 Jesus, porém, fitando neles o olhar, disse: Para os homens é impossível; contudo, não para Deus, porque para Deus tudo é possível.
28 Então, Pedro começou a dizer-lhe: Eis que nós tudo deixamos e te seguimos.
29 Tornou Jesus: Em verdade vos digo que ninguém há que tenha deixado casa, ou irmãos, ou irmãs, ou mãe, ou pai, ou filhos, ou campos por amor de mim e por amor do evangelho,
30 que não receba, já no presente, o cêntuplo de casas, irmãos, irmãs, mães, filhos e campos, com perseguições; e, no mundo por vir, a vida eterna.
31 Porém muitos primeiros serão últimos; e os últimos, primeiros.
32 Estavam de caminho, subindo para Jerusalém, e Jesus ia adiante dos seus discípulos. Estes se admiravam e o seguiam tomados de apreensões. E Jesus, tornando a levar à parte os doze, passou a revelar-lhes as coisas que lhe deviam sobrevir, dizendo:
33 Eis que subimos para Jerusalém, e o Filho do Homem será entregue aos principais sacerdotes e aos escribas; condená-lo-ão à morte e o entregarão aos gentios;
34 hão de escarnecê-lo, cuspir nele, açoitá-lo e matá-lo; mas, depois de três dias, ressuscitará.
35 Então, se aproximaram dele Tiago e João, filhos de Zebedeu, dizendo-lhe: Mestre, queremos que nos concedas o que te vamos pedir.
36 E ele lhes perguntou: Que quereis que vos faça?
37 Responderam-lhe: Permite-nos que, na tua glória, nos assentemos um à tua direita e o outro à tua esquerda.
38 Mas Jesus lhes disse: Não sabeis o que pedis. Podeis vós beber o cálice que eu bebo ou receber o batismo com que eu sou batizado?
39 Disseram-lhe: Podemos. Tornou-lhes Jesus: Bebereis o cálice que eu bebo e recebereis o batismo com que eu sou batizado;
40 quanto, porém, ao assentar-se à minha direita ou à minha esquerda, não me compete concedê-lo; porque é para aqueles a quem está preparado.
41 Ouvindo isto, indignaram-se os dez contra Tiago e João.
42 Mas Jesus, chamando-os para junto de si, disse-lhes: Sabeis que os que são considerados governadores dos povos têm-nos sob seu domínio, e sobre eles os seus maiorais exercem autoridade.
43 Mas entre vós não é assim; pelo contrário, quem quiser tornar-se grande entre vós, será esse o que vos sirva;
44 e quem quiser ser o primeiro entre vós será servo de todos.
45 Pois o próprio Filho do Homem não veio para ser servido, mas para servir e dar a sua vida em resgate por muitos.
46 E foram para Jericó. Quando ele saía de Jericó, juntamente com os discípulos e numerosa multidão, Bartimeu, cego mendigo, filho de Timeu, estava assentado à beira do caminho
47 e, ouvindo que era Jesus, o Nazareno, pôs-se a clamar: Jesus, Filho de Davi, tem compaixão de mim!
48 E muitos o repreendiam, para que se calasse; mas ele cada vez gritava mais: Filho de Davi, tem misericórdia de mim!
49 Parou Jesus e disse: Chamai-o. Chamaram, então, o cego, dizendo-lhe: Tem bom ânimo; levanta-te, ele te chama.
50 Lançando de si a capa, levantou-se de um salto e foi ter com Jesus.
51 Perguntou-lhe Jesus: Que queres que eu te faça? Respondeu o cego: Mestre, que eu torne a ver.
52 Então, Jesus lhe disse: Vai, a tua fé te salvou. E imediatamente tornou a ver e seguia a Jesus estrada fora.*
1 Quando se aproximavam de Jerusalém, de Betfagé e Betânia, junto ao monte das Oliveiras, enviou Jesus dois dos seus discípulos
2 e disse-lhes: Ide à aldeia que aí está diante de vós e, logo ao entrar, achareis preso um jumentinho, o qual ainda ninguém montou; desprendei-o e trazei-o.
3 Se alguém vos perguntar: Por que fazeis isso? Respondei: O Senhor precisa dele e logo o mandará de volta para aqui.
4 Então, foram e acharam o jumentinho preso, junto ao portão, do lado de fora, na rua, e o desprenderam.
5 Alguns dos que ali estavam reclamaram: Que fazeis, soltando o jumentinho?
6 Eles, porém, responderam conforme as instruções de Jesus; então, os deixaram ir.
7 Levaram o jumentinho, sobre o qual puseram as suas vestes, e Jesus o montou.
8 E muitos estendiam as suas vestes no caminho, e outros, ramos que haviam cortado dos campos.
9 Tanto os que iam adiante dele como os que vinham depois clamavam: Hosana! Bendito o que vem em nome do Senhor!
10 Bendito o reino que vem, o reino de Davi, nosso pai! Hosana, nas maiores alturas!
11 E, quando entrou em Jerusalém, no templo, tendo observado tudo, como fosse já tarde, saiu para Betânia com os doze.
12 No dia seguinte, quando saíram de Betânia, teve fome.
13 E, vendo de longe uma figueira com folhas, foi ver se nela, porventura, acharia alguma coisa. Aproximando-se dela, nada achou, senão folhas; porque não era tempo de figos.
14 Então, lhe disse Jesus: Nunca jamais coma alguém fruto de ti! E seus discípulos ouviram isto.
15 E foram para Jerusalém. Entrando ele no templo, passou a expulsar os que ali vendiam e compravam; derribou as mesas dos cambistas e as cadeiras dos que vendiam pombas.
16 Não permitia que alguém conduzisse qualquer utensílio pelo templo;
17 também os ensinava e dizia: Não está escrito: A minha casa será chamada casa de oração para todas as nações? Vós, porém, a tendes transformado em covil de salteadores.
18 E os principais sacerdotes e escribas ouviam estas coisas e procuravam um modo de lhe tirar a vida; pois o temiam, porque toda a multidão se maravilhava de sua doutrina.
19 Em vindo a tarde, saíram da cidade.
20 E, passando eles pela manhã, viram que a figueira secara desde a raiz.
21 Então, Pedro, lembrando-se, falou: Mestre, eis que a figueira que amaldiçoaste secou.
22 Ao que Jesus lhes disse: Tende fé em Deus;
23 porque em verdade vos afirmo que, se alguém disser a este monte: Ergue-te e lança-te no mar, e não duvidar no seu coração, mas crer que se fará o que diz, assim será com ele.
24 Por isso, vos digo que tudo quanto em oração pedirdes, crede que recebestes, e será assim convosco.
25 E, quando estiverdes orando, se tendes alguma coisa contra alguém, perdoai, para que vosso Pai celestial vos perdoe as vossas ofensas.
26 [Mas, se não perdoardes, também vosso Pai celestial não vos perdoará as vossas ofensas.]
27 Então, regressaram para Jerusalém. E, andando ele pelo templo, vieram ao seu encontro os principais sacerdotes, os escribas e os anciãos
28 e lhe perguntaram: Com que autoridade fazes estas coisas? Ou quem te deu tal autoridade para as fazeres?
29 Jesus lhes respondeu: Eu vos farei uma pergunta; respondei-me, e eu vos direi com que autoridade faço estas coisas.
30 O batismo de João era do céu ou dos homens? Respondei!
31 E eles discorriam entre si: Se dissermos: Do céu, dirá: Então, por que não acreditastes nele?
32 Se, porém, dissermos: dos homens, é de temer o povo. Porque todos consideravam a João como profeta.
33 Então, responderam a Jesus: Não sabemos. E Jesus, por sua vez, lhes disse: Nem eu tampouco vos digo com que autoridade faço estas coisas.*
1 Depois, entrou Jesus a falar-lhes por parábola: Um homem plantou uma vinha, cercou-a de uma sebe, construiu um lagar, edificou uma torre, arrendou-a a uns lavradores e ausentou-se do país.
2 No tempo da colheita, enviou um servo aos lavradores para que recebesse deles dos frutos da vinha;
3 eles, porém, o agarraram, espancaram e o despacharam vazio.
4 De novo, lhes enviou outro servo, e eles o esbordoaram na cabeça e o insultaram.
5 Ainda outro lhes mandou, e a este mataram. Muitos outros lhes enviou, dos quais espancaram uns e mataram outros.
6 Restava-lhe ainda um, seu filho amado; a este lhes enviou, por fim, dizendo: Respeitarão a meu filho.
7 Mas os tais lavradores disseram entre si: Este é o herdeiro; ora, vamos, matemo-lo, e a herança será nossa.
8 E, agarrando-o, mataram-no e o atiraram para fora da vinha.
9 Que fará, pois, o dono da vinha? Virá, exterminará aqueles lavradores e passará a vinha a outros.
10 Ainda não lestes esta Escritura: A pedra que os construtores rejeitaram, essa veio a ser a principal pedra, angular;
11 isto procede do Senhor, e é maravilhoso aos nossos olhos?
12 E procuravam prendê-lo, mas temiam o povo; porque compreenderam que contra eles proferira esta parábola. Então, desistindo, retiraram-se.
13 E enviaram-lhe alguns dos fariseus e dos herodianos, para que o apanhassem em alguma palavra.
14 Chegando, disseram-lhe: Mestre, sabemos que és verdadeiro e não te importas com quem quer que seja, porque não olhas a aparência dos homens; antes, segundo a verdade, ensinas o caminho de Deus; é lícito pagar tributo a César ou não? Devemos ou não devemos pagar?
15 Mas Jesus, percebendo-lhes a hipocrisia, respondeu: Por que me experimentais? Trazei-me um denário para que eu o veja.
16 E eles lho trouxeram. Perguntou-lhes: De quem é esta efígie e inscrição? Responderam: De César.
17 Disse-lhes, então, Jesus: Dai a César o que é de César e a Deus o que é de Deus. E muito se admiraram dele.
18 Então, os saduceus, que dizem não haver ressurreição, aproximaram-se dele e lhe perguntaram, dizendo:
19 Mestre, Moisés nos deixou escrito que, se morrer o irmão de alguém e deixar mulher sem filhos, seu irmão a tome como esposa e suscite descendência a seu irmão.
20 Ora, havia sete irmãos; o primeiro casou e morreu sem deixar descendência;
21 o segundo desposou a viúva e morreu, também sem deixar descendência; e o terceiro, da mesma forma.
22 E, assim, os sete não deixaram descendência. Por fim, depois de todos, morreu também a mulher.
23 Na ressurreição, quando eles ressuscitarem, de qual deles será ela a esposa? Porque os sete a desposaram.
24 Respondeu-lhes Jesus: Não provém o vosso erro de não conhecerdes as Escrituras, nem o poder de Deus?
25 Pois, quando ressuscitarem de entre os mortos, nem casarão, nem se darão em casamento; porém, são como os anjos nos céus.
26 Quanto à ressurreição dos mortos, não tendes lido no Livro de Moisés, no trecho referente à sarça, como Deus lhe falou: Eu sou o Deus de Abraão, o Deus de Isaque e o Deus de Jacó?
27 Ora, ele não é Deus de mortos, e sim de vivos. Laborais em grande erro.
28 Chegando um dos escribas, tendo ouvido a discussão entre eles, vendo como Jesus lhes houvera respondido bem, perguntou-lhe: Qual é o principal de todos os mandamentos?
29 Respondeu Jesus: O principal é: Ouve, ó Israel, o Senhor, nosso Deus, é o único Senhor!
30 Amarás, pois, o Senhor, teu Deus, de todo o teu coração, de toda a tua alma, de todo o teu entendimento e de toda a tua força.
31 O segundo é: Amarás o teu próximo como a ti mesmo. Não há outro mandamento maior do que estes.
32 Disse-lhe o escriba: Muito bem, Mestre, e com verdade disseste que ele é o único, e não há outro senão ele,
33 e que amar a Deus de todo o coração e de todo o entendimento e de toda a força, e amar ao próximo como a si mesmo excede a todos os holocaustos e sacrifícios.
34 Vendo Jesus que ele havia respondido sabiamente, declarou-lhe: Não estás longe do reino de Deus. E já ninguém mais ousava interrogá-lo.
35 Jesus, ensinando no templo, perguntou: Como dizem os escribas que o Cristo é filho de Davi?
36 O próprio Davi falou, pelo Espírito Santo: Disse o Senhor ao meu Senhor: Assenta-te à minha direita, até que eu ponha os teus inimigos debaixo dos teus pés.
37 O mesmo Davi chama-lhe Senhor; como, pois, é ele seu filho? E a grande multidão o ouvia com prazer.
38 E, ao ensinar, dizia ele: Guardai-vos dos escribas, que gostam de andar com vestes talares e das saudações nas praças;
39 e das primeiras cadeiras nas sinagogas e dos primeiros lugares nos banquetes;
40 os quais devoram as casas das viúvas e, para o justificar, fazem longas orações; estes sofrerão juízo muito mais severo.
41 Assentado diante do gazofilácio, observava Jesus como o povo lançava ali o dinheiro. Ora, muitos ricos depositavam grandes quantias.
42 Vindo, porém, uma viúva pobre, depositou duas pequenas moedas correspondentes a um quadrante.
43 E, chamando os seus discípulos, disse-lhes: Em verdade vos digo que esta viúva pobre depositou no gazofilácio mais do que o fizeram todos os ofertantes.
44 Porque todos eles ofertaram do que lhes sobrava; ela, porém, da sua pobreza deu tudo quanto possuía, todo o seu sustento.*
1 Ao sair Jesus do templo, disse-lhe um de seus discípulos: Mestre! Que pedras, que construções!
2 Mas Jesus lhe disse: Vês estas grandes construções? Não ficará pedra sobre pedra, que não seja derribada.
3 No monte das Oliveiras, defronte do templo, achava-se Jesus assentado, quando Pedro, Tiago, João e André lhe perguntaram em particular:
4 Dize-nos quando sucederão estas coisas, e que sinal haverá quando todas elas estiverem para cumprir-se.
5 Então, Jesus passou a dizer-lhes: Vede que ninguém vos engane.
6 Muitos virão em meu nome, dizendo: Sou eu; e enganarão a muitos.
7 Quando, porém, ouvirdes falar de guerras e rumores de guerras, não vos assusteis; é necessário assim acontecer, mas ainda não é o fim.
8 Porque se levantará nação contra nação, e reino, contra reino. Haverá terremotos em vários lugares e também fomes. Estas coisas são o princípio das dores.
9 Estai vós de sobreaviso, porque vos entregarão aos tribunais e às sinagogas; sereis açoitados, e vos farão comparecer à presença de governadores e reis, por minha causa, para lhes servir de testemunho.
10 Mas é necessário que primeiro o evangelho seja pregado a todas as nações.
11 Quando, pois, vos levarem e vos entregarem, não vos preocupeis com o que haveis de dizer, mas o que vos for concedido naquela hora, isso falai; porque não sois vós os que falais, mas o Espírito Santo.
12 Um irmão entregará à morte outro irmão, e o pai, ao filho; filhos haverá que se levantarão contra os progenitores e os matarão.
13 Sereis odiados de todos por causa do meu nome; aquele, porém, que perseverar até ao fim, esse será salvo.
14 Quando, pois, virdes o abominável da desolação situado onde não deve estar (quem lê entenda), então, os que estiverem na Judeia fujam para os montes;
15 quem estiver em cima, no eirado, não desça nem entre para tirar da sua casa alguma coisa;
16 e o que estiver no campo não volte atrás para buscar a sua capa.
17 Ai das que estiverem grávidas e das que amamentarem naqueles dias!
18 Orai para que isso não suceda no inverno.
19 Porque aqueles dias serão de tamanha tribulação como nunca houve desde o princípio do mundo, que Deus criou, até agora e nunca jamais haverá.
20 Não tivesse o Senhor abreviado aqueles dias, e ninguém se salvaria; mas, por causa dos eleitos que ele escolheu, abreviou tais dias.
21 Então, se alguém vos disser: Eis aqui o Cristo! Ou: Ei-lo ali! Não acrediteis;
22 pois surgirão falsos cristos e falsos profetas, operando sinais e prodígios, para enganar, se possível, os próprios eleitos.
23 Estai vós de sobreaviso; tudo vos tenho predito.
24 Mas, naqueles dias, após a referida tribulação, o sol escurecerá, a lua não dará a sua claridade,
25 as estrelas cairão do firmamento, e os poderes dos céus serão abalados.
26 Então, verão o Filho do Homem vir nas nuvens, com grande poder e glória.
27 E ele enviará os anjos e reunirá os seus escolhidos dos quatro ventos, da extremidade da terra até à extremidade do céu.
28 Aprendei, pois, a parábola da figueira: quando já os seus ramos se renovam, e as folhas brotam, sabeis que está próximo o verão.
29 Assim, também vós: quando virdes acontecer estas coisas, sabei que está próximo, às portas.
30 Em verdade vos digo que não passará esta geração sem que tudo isto aconteça.
31 Passará o céu e a terra, porém as minhas palavras não passarão.
32 Mas a respeito daquele dia ou da hora ninguém sabe; nem os anjos no céu, nem o Filho, senão o Pai.
33 Estai de sobreaviso, vigiai [e orai]; porque não sabeis quando será o tempo.
34 É como um homem que, ausentando-se do país, deixa a sua casa, dá autoridade aos seus servos, a cada um a sua obrigação, e ao porteiro ordena que vigie.
35 Vigiai, pois, porque não sabeis quando virá o dono da casa: se à tarde, se à meia-noite, se ao cantar do galo, se pela manhã;
36 para que, vindo ele inesperadamente, não vos ache dormindo.
37 O que, porém, vos digo, digo a todos: vigiai!*
1 Dali a dois dias, era a Páscoa e a Festa dos Pães Asmos; e os principais sacerdotes e os escribas procuravam como o prenderiam, à traição, e o matariam.
2 Pois diziam: Não durante a festa, para que não haja tumulto entre o povo.
3 Estando ele em Betânia, reclinado à mesa, em casa de Simão, o leproso, veio uma mulher trazendo um vaso de alabastro com preciosíssimo perfume de nardo puro; e, quebrando o alabastro, derramou o bálsamo sobre a cabeça de Jesus.
4 Indignaram-se alguns entre si e diziam: Para que este desperdício de bálsamo?
5 Porque este perfume poderia ser vendido por mais de trezentos denários e dar-se aos pobres. E murmuravam contra ela.
6 Mas Jesus disse: Deixai-a; por que a molestais? Ela praticou boa ação para comigo.
7 Porque os pobres, sempre os tendes convosco e, quando quiserdes, podeis fazer-lhes bem, mas a mim nem sempre me tendes.
8 Ela fez o que pôde: antecipou-se a ungir-me para a sepultura.
9 Em verdade vos digo: onde for pregado em todo o mundo o evangelho, será também contado o que ela fez, para memória sua.
10 E Judas Iscariotes, um dos doze, foi ter com os principais sacerdotes, para lhes entregar Jesus.
11 Eles, ouvindo-o, alegraram-se e lhe prometeram dinheiro; nesse meio tempo, buscava ele uma boa ocasião para o entregar.
12 E, no primeiro dia da Festa dos Pães Asmos, quando se fazia o sacrifício do cordeiro pascal, disseram-lhe seus discípulos: Onde queres que vamos fazer os preparativos para comeres a Páscoa?
13 Então, enviou dois dos seus discípulos, dizendo-lhes: Ide à cidade, e vos sairá ao encontro um homem trazendo um cântaro de água;
14 segui-o e dizei ao dono da casa onde ele entrar que o Mestre pergunta: Onde é o meu aposento no qual hei de comer a Páscoa com os meus discípulos?
15 E ele vos mostrará um espaçoso cenáculo mobilado e pronto; ali fazei os preparativos.
16 Saíram, pois, os discípulos, foram à cidade e, achando tudo como Jesus lhes tinha dito, prepararam a Páscoa.
17 Ao cair da tarde, foi com os doze.
18 Quando estavam à mesa e comiam, disse Jesus: Em verdade vos digo que um dentre vós, o que come comigo, me trairá.
19 E eles começaram a entristecer-se e a dizer-lhe, um após outro: Porventura, sou eu?
20 Respondeu-lhes: É um dos doze, o que mete comigo a mão no prato.
21 Pois o Filho do Homem vai, como está escrito a seu respeito; mas ai daquele por intermédio de quem o Filho do Homem está sendo traído! Melhor lhe fora não haver nascido!
22 E, enquanto comiam, tomou Jesus um pão e, abençoando-o, o partiu e lhes deu, dizendo: Tomai, isto é o meu corpo.
23 A seguir, tomou Jesus um cálice e, tendo dado graças, o deu aos seus discípulos; e todos beberam dele.
24 Então, lhes disse: Isto é o meu sangue, o sangue da [nova] aliança, derramado em favor de muitos.
25 Em verdade vos digo que jamais beberei do fruto da videira, até àquele dia em que o hei de beber, novo, no reino de Deus.
26 Tendo cantado um hino, saíram para o monte das Oliveiras.
27 Então, lhes disse Jesus: Todos vós vos escandalizareis, porque está escrito: Ferirei o pastor, e as ovelhas ficarão dispersas.
28 Mas, depois da minha ressurreição, irei adiante de vós para a Galileia.
29 Disse-lhe Pedro: Ainda que todos se escandalizem, eu, jamais!
30 Respondeu-lhe Jesus: Em verdade te digo que hoje, nesta noite, antes que duas vezes cante o galo, tu me negarás três vezes.
31 Mas ele insistia com mais veemência: Ainda que me seja necessário morrer contigo, de nenhum modo te negarei. Assim disseram todos.
32 Então, foram a um lugar chamado Getsêmani; ali chegados, disse Jesus a seus discípulos: Assentai-vos aqui, enquanto eu vou orar.
33 E, levando consigo a Pedro, Tiago e João, começou a sentir-se tomado de pavor e de angústia.
34 E lhes disse: A minha alma está profundamente triste até à morte; ficai aqui e vigiai.
35 E, adiantando-se um pouco, prostrou-se em terra; e orava para que, se possível, lhe fosse poupada aquela hora.
36 E dizia: Aba, Pai, tudo te é possível; passa de mim este cálice; contudo, não seja o que eu quero, e sim o que tu queres.
37 Voltando, achou-os dormindo; e disse a Pedro: Simão, tu dormes? Não pudeste vigiar nem uma hora?
38 Vigiai e orai, para que não entreis em tentação; o espírito, na verdade, está pronto, mas a carne é fraca.
39 Retirando-se de novo, orou repetindo as mesmas palavras.
40 Voltando, achou-os outra vez dormindo, porque os seus olhos estavam pesados; e não sabiam o que lhe responder.
41 E veio pela terceira vez e disse-lhes: Ainda dormis e repousais! Basta! Chegou a hora; o Filho do Homem está sendo entregue nas mãos dos pecadores.
42 Levantai-vos, vamos! Eis que o traidor se aproxima.
43 E logo, falava ele ainda, quando chegou Judas, um dos doze, e com ele, vinda da parte dos principais sacerdotes, escribas e anciãos, uma turba com espadas e porretes.
44 Ora, o traidor tinha-lhes dado esta senha: Aquele a quem eu beijar, é esse; prendei-o e levai-o com segurança.
45 E, logo que chegou, aproximando-se, disse-lhe: Mestre! E o beijou.
46 Então, lhe deitaram as mãos e o prenderam.
47 Nisto, um dos circunstantes, sacando da espada, feriu o servo do sumo sacerdote e cortou-lhe a orelha.
48 Disse-lhes Jesus: Saístes com espadas e porretes para prender-me, como a um salteador?
49 Todos os dias eu estava convosco no templo, ensinando, e não me prendestes; contudo, é para que se cumpram as Escrituras.
50 Então, deixando-o, todos fugiram.
51 Seguia-o um jovem, coberto unicamente com um lençol, e lançaram-lhe a mão.
52 Mas ele, largando o lençol, fugiu desnudo.
53 E levaram Jesus ao sumo sacerdote, e reuniram-se todos os principais sacerdotes, os anciãos e os escribas.
54 Pedro seguira-o de longe até ao interior do pátio do sumo sacerdote e estava assentado entre os serventuários, aquentando-se ao fogo.
55 E os principais sacerdotes e todo o Sinédrio procuravam algum testemunho contra Jesus para o condenar à morte e não achavam.
56 Pois muitos testemunhavam falsamente contra Jesus, mas os depoimentos não eram coerentes.
57 E, levantando-se alguns, testificavam falsamente, dizendo:
58 Nós o ouvimos declarar: Eu destruirei este santuário edificado por mãos humanas e, em três dias, construirei outro, não por mãos humanas.
59 Nem assim o testemunho deles era coerente.
60 Levantando-se o sumo sacerdote, no meio, perguntou a Jesus: Nada respondes ao que estes depõem contra ti?
61 Ele, porém, guardou silêncio e nada respondeu. Tornou a interrogá-lo o sumo sacerdote e lhe disse: És tu o Cristo, o Filho do Deus Bendito?
62 Jesus respondeu: Eu sou, e vereis o Filho do Homem assentado à direita do Todo-Poderoso e vindo com as nuvens do céu.
63 Então, o sumo sacerdote rasgou as suas vestes e disse: Que mais necessidade temos de testemunhas?
64 Ouvistes a blasfêmia; que vos parece? E todos o julgaram réu de morte.
65 Puseram-se alguns a cuspir nele, a cobrir-lhe o rosto, a dar-lhe murros e a dizer-lhe: Profetiza! E os guardas o tomaram a bofetadas.
66 Estando Pedro embaixo no pátio, veio uma das criadas do sumo sacerdote
67 e, vendo a Pedro, que se aquentava, fixou-o e disse: Tu também estavas com Jesus, o Nazareno.
68 Mas ele o negou, dizendo: Não o conheço, nem compreendo o que dizes. E saiu para o alpendre. [E o galo cantou.]
69 E a criada, vendo-o, tornou a dizer aos circunstantes: Este é um deles.
70 Mas ele outra vez o negou. E, pouco depois, os que ali estavam disseram a Pedro: Verdadeiramente, és um deles, porque também tu és galileu.
71 Ele, porém, começou a praguejar e a jurar: Não conheço esse homem de quem falais!
72 E logo cantou o galo pela segunda vez. Então, Pedro se lembrou da palavra que Jesus lhe dissera: Antes que duas vezes cante o galo, tu me negarás três vezes. E, caindo em si, desatou a chorar.*
1 Logo pela manhã, entraram em conselho os principais sacerdotes com os anciãos, os escribas e todo o Sinédrio; e, amarrando a Jesus, levaram-no e o entregaram a Pilatos.
2 Pilatos o interrogou: És tu o rei dos judeus? Respondeu Jesus: Tu o dizes.
3 Então, os principais sacerdotes o acusavam de muitas coisas.
4 Tornou Pilatos a interrogá-lo: Nada respondes? Vê quantas acusações te fazem!
5 Jesus, porém, não respondeu palavra, a ponto de Pilatos muito se admirar.
6 Ora, por ocasião da festa, era costume soltar ao povo um dos presos, qualquer que eles pedissem.
7 Havia um, chamado Barrabás, preso com amotinadores, os quais em um tumulto haviam cometido homicídio.
8 Vindo a multidão, começou a pedir que lhes fizesse como de costume.
9 E Pilatos lhes respondeu, dizendo: Quereis que eu vos solte o rei dos judeus?
10 Pois ele bem percebia que por inveja os principais sacerdotes lho haviam entregado.
11 Mas estes incitaram a multidão no sentido de que lhes soltasse, de preferência, Barrabás.
12 Mas Pilatos lhes perguntou: Que farei, então, deste a quem chamais o rei dos judeus?
13 Eles, porém, clamavam: Crucifica-o!
14 Mas Pilatos lhes disse: Que mal fez ele? E eles gritavam cada vez mais: Crucifica-o!
15 Então, Pilatos, querendo contentar a multidão, soltou-lhes Barrabás; e, após mandar açoitar a Jesus, entregou-o para ser crucificado.
16 Então, os soldados o levaram para dentro do palácio, que é o pretório, e reuniram todo o destacamento.
17 Vestiram-no de púrpura e, tecendo uma coroa de espinhos, lha puseram na cabeça.
18 E o saudavam, dizendo: Salve, rei dos judeus!
19 Davam-lhe na cabeça com um caniço, cuspiam nele e, pondo-se de joelhos, o adoravam.
20 Depois de o terem escarnecido, despiram-lhe a púrpura e o vestiram com as suas próprias vestes. Então, conduziram Jesus para fora, com o fim de o crucificarem.
21 E obrigaram a Simão Cireneu, que passava, vindo do campo, pai de Alexandre e de Rufo, a carregar-lhe a cruz.
22 E levaram Jesus para o Gólgota, que quer dizer Lugar da Caveira.
23 Deram-lhe a beber vinho com mirra; ele, porém, não tomou.
24 Então, o crucificaram e repartiram entre si as vestes dele, lançando-lhes sorte, para ver o que levaria cada um.
25 Era a hora terceira quando o crucificaram.
26 E, por cima, estava, em epígrafe, a sua acusação: O Rei dos Judeus.
27 Com ele crucificaram dois ladrões, um à sua direita, e outro à sua esquerda.
28 [E cumpriu-se a Escritura que diz: Com malfeitores foi contado. ]
29 Os que iam passando, blasfemavam dele, meneando a cabeça e dizendo: Ah! Tu que destróis o santuário e, em três dias, o reedificas!
30 Salva-te a ti mesmo, descendo da cruz!
31 De igual modo, os principais sacerdotes com os escribas, escarnecendo, entre si diziam: Salvou os outros, a si mesmo não pode salvar-se;
32 desça agora da cruz o Cristo, o rei de Israel, para que vejamos e creiamos. Também os que com ele foram crucificados o insultavam.
33 Chegada a hora sexta, houve trevas sobre toda a terra até a hora nona.
34 À hora nona, clamou Jesus em alta voz: Eloí, Eloí, lamá sabactâni? Que quer dizer: Deus meu, Deus meu, por que me desamparaste?
35 Alguns dos que ali estavam, ouvindo isto, diziam: Vede, chama por Elias!
36 E um deles correu a embeber uma esponja em vinagre e, pondo-a na ponta de um caniço, deu-lhe de beber, dizendo: Deixai, vejamos se Elias vem tirá-lo!
37 Mas Jesus, dando um grande brado, expirou.
38 E o véu do santuário rasgou-se em duas partes, de alto a baixo.
39 O centurião que estava em frente dele, vendo que assim expirara, disse: Verdadeiramente, este homem era o Filho de Deus.
40 Estavam também ali algumas mulheres, observando de longe; entre elas, Maria Madalena, Maria, mãe de Tiago, o menor, e de José, e Salomé;
41 as quais, quando Jesus estava na Galileia, o acompanhavam e serviam; e, além destas, muitas outras que haviam subido com ele para Jerusalém.
42 Ao cair da tarde, por ser o dia da preparação, isto é, a véspera do sábado,
43 vindo José de Arimateia, ilustre membro do Sinédrio, que também esperava o reino de Deus, dirigiu-se resolutamente a Pilatos e pediu o corpo de Jesus.
44 Mas Pilatos admirou-se de que ele já tivesse morrido. E, tendo chamado o centurião, perguntou-lhe se havia muito que morrera.
45 Após certificar-se, pela informação do comandante, cedeu o corpo a José.
46 Este, baixando o corpo da cruz, envolveu-o em um lençol que comprara e o depositou em um túmulo que tinha sido aberto numa rocha; e rolou uma pedra para a entrada do túmulo.
47 Ora, Maria Madalena e Maria, mãe de José, observaram onde ele foi posto.*
1 Passado o sábado, Maria Madalena, Maria, mãe de Tiago, e Salomé, compraram aromas para irem embalsamá-lo.
2 E, muito cedo, no primeiro dia da semana, ao despontar do sol, foram ao túmulo.
3 Diziam umas às outras: Quem nos removerá a pedra da entrada do túmulo?
4 E, olhando, viram que a pedra já estava removida; pois era muito grande.
5 Entrando no túmulo, viram um jovem assentado ao lado direito, vestido de branco, e ficaram surpreendidas e atemorizadas.
6 Ele, porém, lhes disse: Não vos atemorizeis; buscais a Jesus, o Nazareno, que foi crucificado; ele ressuscitou, não está mais aqui; vede o lugar onde o tinham posto.
7 Mas ide, dizei a seus discípulos e a Pedro que ele vai adiante de vós para a Galileia; lá o vereis, como ele vos disse.
8 E, saindo elas, fugiram do sepulcro, porque estavam possuídas de temor e de assombro; e, de medo, nada disseram a ninguém.
9 Havendo ele ressuscitado de manhã cedo no primeiro dia da semana, apareceu primeiro a Maria Madalena, da qual expelira sete demônios.
10 E, partindo ela, foi anunciá-lo àqueles que, tendo sido companheiros de Jesus, se achavam tristes e choravam.
11 Estes, ouvindo que ele vivia e que fora visto por ela, não acreditaram.
12 Depois disto, manifestou-se em outra forma a dois deles que estavam de caminho para o campo.
13 E, indo, eles o anunciaram aos demais, mas também a estes dois eles não deram crédito.
14 Finalmente, apareceu Jesus aos onze, quando estavam à mesa, e censurou-lhes a incredulidade e dureza de coração, porque não deram crédito aos que o tinham visto já ressuscitado.
15 E disse-lhes: Ide por todo o mundo e pregai o evangelho a toda criatura.
16 Quem crer e for batizado será salvo; quem, porém, não crer será condenado.
17 Estes sinais hão de acompanhar aqueles que creem: em meu nome, expelirão demônios; falarão novas línguas;
18 pegarão em serpentes; e, se alguma coisa mortífera beberem, não lhes fará mal; se impuserem as mãos sobre enfermos, eles ficarão curados.
19 De fato, o Senhor Jesus, depois de lhes ter falado, foi recebido no céu e assentou-se à destra de Deus.
20 E eles, tendo partido, pregaram em toda parte, cooperando com eles o Senhor e confirmando a palavra por meio de sinais, que se seguiam.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Marcos','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)