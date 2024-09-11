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
 1 Aconteceu no trigésimo ano, no quinto dia do quarto mês, que, estando eu no meio dos exilados, junto ao rio Quebar, se abriram os céus, e eu tive visões de Deus.
2 No quinto dia do referido mês, no quinto ano de cativeiro do rei Joaquim,
3 veio expressamente a palavra do Senhor a Ezequiel, filho de Buzi, o sacerdote, na terra dos caldeus, junto ao rio Quebar, e ali esteve sobre ele a mão do Senhor.
4 Olhei, e eis que um vento tempestuoso vinha do Norte, e uma grande nuvem, com fogo a revolver-se, e resplendor ao redor dela, e no meio disto, uma coisa como metal brilhante, que saía do meio do fogo.
5 Do meio dessa nuvem saía a semelhança de quatro seres viventes, cuja aparência era esta: tinham a semelhança de homem.
6 Cada um tinha quatro rostos, como também quatro asas.
7 As suas pernas eram direitas, a planta de cujos pés era como a de um bezerro e luzia como o brilho de bronze polido.
8 Debaixo das asas tinham mãos de homem, aos quatro lados; assim todos os quatro tinham rostos e asas.
9 Estas se uniam uma à outra; não se viravam quando iam; cada qual andava para a sua frente.
10 A forma de seus rostos era como o de homem; à direita, os quatro tinham rosto de leão; à esquerda, rosto de boi; e também rosto de águia, todos os quatro.
11 Assim eram os seus rostos. Suas asas se abriam em cima; cada ser tinha duas asas, unidas cada uma à do outro; outras duas cobriam o corpo deles.
12 Cada qual andava para a sua frente; para onde o espírito havia de ir, iam; não se viravam quando iam.
13 O aspecto dos seres viventes era como carvão em brasa, à semelhança de tochas; o fogo corria resplendente por entre os seres, e dele saíam relâmpagos,
14 os seres viventes ziguezagueavam à semelhança de relâmpagos.
15 Vi os seres viventes; e eis que havia uma roda na terra, ao lado de cada um deles.
16 O aspecto das rodas e a sua estrutura eram brilhantes como o berilo; tinham as quatro a mesma aparência, cujo aspecto e estrutura eram como se estivera uma roda dentro da outra.
17 Andando elas, podiam ir em quatro direções; e não se viravam quando iam.
18 As suas cambotas eram altas, e metiam medo; e, nas quatro rodas, as mesmas eram cheias de olhos ao redor.
19 Andando os seres viventes, andavam as rodas ao lado deles; elevando-se eles, também elas se elevavam.
20 Para onde o espírito queria ir, iam, pois o espírito os impelia; e as rodas se elevavam juntamente com eles, porque nelas havia o espírito dos seres viventes.
21 Andando eles, andavam elas e, parando eles, paravam elas, e, elevando-se eles da terra, elevavam-se também as rodas juntamente com eles; porque o espírito dos seres viventes estava nas rodas.
22 Sobre a cabeça dos seres viventes havia algo semelhante ao firmamento, como cristal brilhante que metia medo, estendido por sobre a sua cabeça.
23 Por debaixo do firmamento, estavam estendidas as suas asas, a de um em direção à de outro; cada um tinha outras duas asas com que cobria o corpo de um e de outro lado.
24 Andando eles, ouvi o tatalar das suas asas, como o rugido de muitas águas, como a voz do Onipotente; ouvi o estrondo tumultuoso, como o tropel de um exército. Parando eles, abaixavam as asas.
25 Veio uma voz de cima do firmamento que estava sobre a sua cabeça. Parando eles, abaixavam as asas.
26 Por cima do firmamento que estava sobre a sua cabeça, havia algo semelhante a um trono, como uma safira; sobre esta espécie de trono, estava sentada uma figura semelhante a um homem.
27 Vi-a como metal brilhante, como fogo ao redor dela, desde os seus lombos e daí para cima; e desde os seus lombos e daí para baixo, vi-a como fogo e um resplendor ao redor dela.
28 Como o aspecto do arco que aparece na nuvem em dia de chuva, assim era o resplendor em redor. Esta era a aparência da glória do Senhor; vendo isto, caí com o rosto em terra e ouvi a voz de quem falava.*
1 Esta voz me disse: Filho do homem, põe-te em pé, e falarei contigo.
2 Então, entrou em mim o Espírito, quando falava comigo, e me pôs em pé, e ouvi o que me falava.
3 Ele me disse: Filho do homem, eu te envio aos filhos de Israel, às nações rebeldes que se insurgiram contra mim; eles e seus pais prevaricaram contra mim, até precisamente ao dia de hoje.
4 Os filhos são de duro semblante e obstinados de coração; eu te envio a eles, e lhes dirás: Assim diz o Senhor Deus.
5 Eles, quer ouçam quer deixem de ouvir, porque são casa rebelde, hão de saber que esteve no meio deles um profeta.
6 Tu, ó filho do homem, não os temas, nem temas as suas palavras, ainda que haja sarças e espinhos para contigo, e tu habites com escorpiões; não temas as suas palavras, nem te assustes com o rosto deles, porque são casa rebelde.
7 Mas tu lhes dirás as minhas palavras, quer ouçam quer deixem de ouvir, pois são rebeldes.
8 Tu, ó filho do homem, ouve o que eu te digo, não te insurjas como a casa rebelde; abre a boca e come o que eu te dou.
9 Então, vi, e eis que certa mão se estendia para mim, e nela se achava o rolo de um livro.
10 Estendeu-o diante de mim, e estava escrito por dentro e por fora; nele, estavam escritas lamentações, suspiros e ais.*
1 Ainda me disse: Filho do homem, come o que achares; come este rolo, vai e fala à casa de Israel.
2 Então, abri a boca, e ele me deu a comer o rolo.
3 E me disse: Filho do homem, dá de comer ao teu ventre e enche as tuas entranhas deste rolo que eu te dou. Eu o comi, e na boca me era doce como o mel.
4 Disse-me ainda: Filho do homem, vai, entra na casa de Israel e dize-lhe as minhas palavras.
5 Porque tu não és enviado a um povo de estranho falar nem de língua difícil, mas à casa de Israel;
6 nem a muitos povos de estranho falar e de língua difícil, cujas palavras não possas entender; se eu aos tais te enviasse, certamente, te dariam ouvidos.
7 Mas a casa de Israel não te dará ouvidos, porque não me quer dar ouvidos a mim; pois toda a casa de Israel é de fronte obstinada e dura de coração.
8 Eis que fiz duro o teu rosto contra o rosto deles e dura a tua fronte, contra a sua fronte.
9 Fiz a tua fronte como o diamante, mais dura do que a pederneira; não os temas, pois, nem te assustes com o seu rosto, porque são casa rebelde.
10 Ainda me disse mais: Filho do homem, mete no coração todas as minhas palavras que te hei de falar e ouve-as com os teus ouvidos.
11 Eia, pois, vai aos do cativeiro, aos filhos do teu povo, e, quer ouçam quer deixem de ouvir, fala com eles, e dize-lhes: Assim diz o Senhor Deus.
12 Levantou-me o Espírito, e ouvi por detrás de mim uma voz de grande estrondo, que, levantando-se do seu lugar, dizia: Bendita seja a glória do Senhor.
13 Ouvi o tatalar das asas dos seres viventes, que tocavam umas nas outras, e o barulho das rodas juntamente com eles e o sonido de um grande estrondo.
14 Então, o Espírito me levantou e me levou; eu fui amargurado na excitação do meu espírito; mas a mão do Senhor se fez muito forte sobre mim.
15 Então, fui a Tel-Abibe, aos do exílio, que habitavam junto ao rio Quebar, e passei a morar onde eles habitavam; e, por sete dias, assentei-me ali, atônito, no meio deles.
16 Findos os sete dias, veio a mim a palavra do Senhor, dizendo:
17 Filho do homem, eu te dei por atalaia sobre a casa de Israel; da minha boca ouvirás a palavra e os avisarás da minha parte.
18 Quando eu disser ao perverso: Certamente, morrerás, e tu não o avisares e nada disseres para o advertir do seu mau caminho, para lhe salvar a vida, esse perverso morrerá na sua iniquidade, mas o seu sangue da tua mão o requererei.
19 Mas, se avisares o perverso, e ele não se converter da sua maldade e do seu caminho perverso, ele morrerá na sua iniquidade, mas tu salvaste a tua alma.
20 Também quando o justo se desviar da sua justiça e fizer maldade, e eu puser diante dele um tropeço, ele morrerá; visto que não o avisaste, no seu pecado morrerá, e suas justiças que praticara não serão lembradas, mas o seu sangue da tua mão o requererei.
21 No entanto, se tu avisares o justo, para que não peque, e ele não pecar, certamente, viverá, porque foi avisado; e tu salvaste a tua alma.
22 A mão do Senhor veio sobre mim, e ele me disse: Levanta-te e sai para o vale, onde falarei contigo.
23 Levantei-me e saí para o vale, e eis que a glória do Senhor estava ali, como a glória que eu vira junto ao rio Quebar; e caí com o rosto em terra.
24 Então, entrou em mim o Espírito, e me pôs em pé, e falou comigo, e me disse: Vai e encerra-te dentro da tua casa.
25 Porque, ó filho do homem, eis que porão cordas sobre ti e te ligarão com elas; e não sairás ao meio deles.
26 Farei que a tua língua se pegue ao teu paladar, ficarás mudo e incapaz de os repreender; porque são casa rebelde.
27 Mas, quando eu falar contigo, darei que fale a tua boca, e lhes dirás: Assim diz o Senhor Deus: Quem ouvir ouça, e quem deixar de ouvir deixe; porque são casa rebelde.*
1 Tu, pois, ó filho do homem, toma um tijolo, põe-no diante de ti e grava nele a cidade de Jerusalém.
2 Põe cerco contra ela, edifica contra ela fortificações, levanta contra ela tranqueiras e põe contra ela arraiais e aríetes em redor.
3 Toma também uma assadeira de ferro e põe-na por muro de ferro entre ti e a cidade; dirige para ela o rosto, e assim será cercada, e a cercarás; isto servirá de sinal para a casa de Israel.
4 Deita-te também sobre o teu lado esquerdo e põe a iniquidade da casa de Israel sobre ele; conforme o número dos dias que te deitares sobre ele, levarás sobre ti a iniquidade dela.
5 Porque eu te dei os anos da sua iniquidade, segundo o número dos dias, trezentos e noventa dias; e levarás sobre ti a iniquidade da casa de Israel.
6 Quando tiveres cumprido estes dias, deitar-te-ás sobre o teu lado direito e levarás sobre ti a iniquidade da casa de Judá.
7 Quarenta dias te dei, cada dia por um ano. Voltarás, pois, o rosto para o cerco de Jerusalém, com o teu braço descoberto, e profetizarás contra ela.
8 Eis que te prenderei com cordas; assim não te voltarás de um lado para o outro, até que cumpras os dias do teu cerco.
9 Toma trigo e cevada, favas e lentilhas, aveia e centeio, mete-os numa vasilha e faze deles pão; segundo o número dos dias que te deitares sobre o teu lado, trezentos e noventa dias, comerás dele.
10 A tua comida será por peso, vinte siclos por dia; de tempo em tempo, a comerás.
11 Também beberás a água por medida, a sexta parte de um him; de tempo em tempo, a beberás.
12 O que comeres será como bolos de cevada; cozê-lo-ás sobre esterco de homem, à vista do povo.
13 Disse o Senhor: Assim comerão os filhos de Israel o seu pão imundo, entre as nações para onde os lançarei.
14 Então, disse eu: ah! Senhor Deus! Eis que a minha alma não foi contaminada, pois, desde a minha mocidade até agora, nunca comi animal morto de si mesmo nem dilacerado por feras, nem carne abominável entrou na minha boca.
15 Então, ele me disse: Dei-te esterco de vacas, em lugar de esterco humano; sobre ele prepararás o teu pão.
16 Disse-me ainda: Filho do homem, eis que eu tirarei o sustento de pão em Jerusalém; comerão o pão por peso e, com ansiedade, beberão a água por medida e com espanto;
17 porque lhes faltará o pão e a água, espantar-se-ão uns com os outros e se consumirão nas suas iniquidades.*
1 Tu, ó filho do homem, toma uma espada afiada; como navalha de barbeiro a tomarás e a farás passar pela tua cabeça e pela tua barba; tomarás uma balança de peso e repartirás os cabelos.
2 Uma terça parte queimarás, no meio da cidade, quando se cumprirem os dias do cerco; tomarás outra terça parte e a ferirás com uma espada ao redor da cidade; e a outra terça parte espalharás ao vento; desembainharei a espada atrás deles.
3 Desta terça parte tomarás uns poucos e os atarás nas abas da tua veste.
4 Destes ainda tomarás alguns, e os lançarás no meio do fogo, e os queimarás; dali sairá um fogo contra toda a casa de Israel.
5 Assim diz o Senhor Deus: Esta é Jerusalém; pu-la no meio das nações e terras que estão ao redor dela.
6 Ela, porém, se rebelou contra os meus juízos, praticando o mal mais do que as nações e transgredindo os meus estatutos mais do que as terras que estão ao redor dela; porque rejeitaram os meus juízos e não andaram nos meus estatutos.
7 Portanto, assim diz o Senhor Deus: Porque sois mais rebeldes do que as nações que estão ao vosso redor e não tendes andado nos meus estatutos, nem cumprido os meus juízos, nem procedido segundo os direitos das nações ao redor de vós,
8 por isso, assim diz o Senhor Deus: Eis que eu, eu mesmo, estou contra ti; e executarei juízos no meio de ti, à vista das nações.
9 Farei contigo o que nunca fiz e o que jamais farei, por causa de todas as tuas abominações.
10 Portanto, os pais devorarão a seus filhos no meio de ti, e os filhos devorarão a seus pais; executarei em ti juízos e tudo o que restar de ti espalharei a todos os ventos.
11 Portanto, tão certo como eu vivo, diz o Senhor Deus, pois que profanaste o meu santuário com todas as tuas coisas detestáveis e com todas as tuas abominações, eu retirarei, sem piedade, os olhos de ti e não te pouparei.
12 Uma terça parte de ti morrerá de peste e será consumida de fome no meio de ti; outra terça parte cairá à espada em redor de ti; e a outra terça parte espalharei a todos os ventos e desembainharei a espada atrás dela.
13 Assim, se cumprirá a minha ira, e satisfarei neles o meu furor e me consolarei; saberão que eu, o Senhor, falei no meu zelo, quando cumprir neles o meu furor.
14 Pôr-te-ei em desolação e por objeto de opróbrio entre as nações que estão ao redor de ti, à vista de todos os que passarem.
15 Assim, serás objeto de opróbrio e ludíbrio, de escarmento e espanto às nações que estão ao redor de ti, quando eu executar em ti juízos com ira e indignação, em furiosos castigos. Eu, o Senhor, falei.
16 Quando eu despedir as malignas flechas da fome contra eles, flechas destruidoras, que eu enviarei para vos destruir, então, aumentarei a fome sobre vós e vos tirarei o sustento de pão.
17 Enviarei sobre vós a fome e bestas-feras que te desfilharão; a peste e o sangue passarão por ti, e trarei a espada sobre ti. Eu, o Senhor, falei.*1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, vira o rosto para os montes de Israel e profetiza contra eles, dizendo:
3 Montes de Israel, ouvi a palavra do Senhor Deus: Assim diz o Senhor Deus aos montes, aos outeiros, aos ribeiros e aos vales: Eis que eu, eu mesmo, trarei a espada sobre vós e destruirei os vossos altos.
4 Ficarão desolados os vossos altares, e quebrados, os vossos altares de incenso; arrojarei os vossos mortos à espada, diante dos vossos ídolos.
5 Porei os cadáveres dos filhos de Israel diante dos seus ídolos e espalharei os vossos ossos ao redor dos vossos altares.
6 Em todos os vossos lugares habitáveis, as cidades serão destruídas, e os altos ficarão desolados, para que os vossos altares sejam destruídos e arruinados, e os vossos ídolos, quebrados e extintos, e os vossos altares do incenso sejam eliminados, e desfeitas as vossas obras.
7 Os mortos à espada cairão no meio de vós, para que saibais que eu sou o Senhor.
8 Mas deixarei um resto, porquanto alguns de vós escapareis da espada entre as nações, quando fordes espalhados pelas terras.
9 Então, se lembrarão de mim os que dentre vós escaparem entre as nações para onde foram levados em cativeiro; pois me quebrantei por causa do seu coração dissoluto, que se desviou de mim, e por causa dos seus olhos, que se prostituíram após os seus ídolos. Eles terão nojo de si mesmos, por causa dos males que fizeram em todas as suas abominações.
10 Saberão que eu sou o Senhor e não disse debalde que lhes faria este mal.
11 Assim diz o Senhor Deus: Bate as palmas, bate com o pé e dize: Ah! Por todas as terríveis abominações da casa de Israel! Pois cairão à espada, e de fome, e de peste.
12 O que estiver longe morrerá de peste; o que estiver perto cairá à espada; e o que ficar de resto e cercado morrerá de fome. Assim, neles cumprirei o meu furor.
13 Então, sabereis que eu sou o Senhor, quando os seus mortos à espada jazerem no meio dos seus ídolos, em redor dos seus altares, em todo outeiro alto, em todos os cimos dos montes e debaixo de toda árvore frondosa, debaixo de todo carvalho espesso, lugares onde ofereciam suave perfume a todos os seus ídolos.
14 Estenderei a mão sobre eles e farei a terra tornar-se desolada, desolada desde o deserto até Ribla, em todas as suas habitações; e saberão que eu sou o Senhor.*
1 Veio ainda a palavra do Senhor a mim, dizendo:
2 Ó tu, filho do homem, assim diz o Senhor Deus acerca da terra de Israel: Haverá fim! O fim vem sobre os quatro cantos da terra.
3 Agora, vem o fim sobre ti; enviarei sobre ti a minha ira, e te julgarei segundo os teus caminhos, e farei cair sobre ti todas as tuas abominações.
4 Os meus olhos não te pouparão, nem terei piedade, mas porei sobre ti os teus caminhos, e as tuas abominações estarão no meio de ti. Sabereis que eu sou o Senhor.
5 Assim diz o Senhor Deus: Mal após mal, eis que vêm.
6 Haverá fim, vem o fim, despertou-se contra ti;
7 vem a tua sentença, ó habitante da terra. Vem o tempo; é chegado o dia da turbação, e não da alegria, sobre os montes.
8 Agora, em breve, derramarei o meu furor sobre ti, cumprirei a minha ira contra ti, julgar-te-ei segundo os teus caminhos e porei sobre ti todas as tuas abominações.
9 Os meus olhos não te pouparão, nem terei piedade; segundo os teus caminhos, assim te castigarei, e as tuas abominações estarão no meio de ti. Sabereis que eu, o Senhor, é que firo.
10 Eis o dia, eis que vem; brotou a tua sentença, já floresceu a vara, reverdeceu a soberba.
11 Levantou-se a violência para servir de vara perversa; nada restará deles, nem da sua riqueza, nem dos seus rumores, nem da sua glória.
12 Vem o tempo, é chegado o dia; o que compra não se alegre, e o que vende não se entristeça; porque a ira ardente está sobre toda a multidão deles.
13 Porque o que vende não tornará a possuir aquilo que vendeu, por mais que viva; porque a profecia contra a multidão não voltará atrás; ninguém fortalece a sua vida com a sua própria iniquidade.
14 Tocaram a trombeta e prepararam tudo, mas não há quem vá à peleja, porque toda a minha ira ardente está sobre toda a multidão deles.
15 Fora está a espada; dentro, a peste e a fome; o que está no campo morre à espada, e o que está na cidade, a fome e a peste o consomem.
16 Se alguns deles, fugindo, escaparem, estarão pelos montes, como pombas dos vales, todos gemendo, cada um por causa da sua iniquidade.
17 Todas as mãos se tornarão débeis, e todos os joelhos, em água.
18 Cingir-se-ão de pano de saco, e o horror os cobrirá; em todo rosto haverá vergonha, e calva, em toda a cabeça.
19 A sua prata lançarão pelas ruas, e o seu ouro lhes será como sujeira; nem a sua prata, nem o seu ouro os poderá livrar no dia da indignação do Senhor; eles não saciarão a sua fome, nem lhes encherão o estômago, porque isto lhes foi o tropeço para cair em iniquidade.
20 De tais preciosas joias fizeram seu objeto de soberba e fabricaram suas abomináveis imagens e seus ídolos detestáveis;
21 portanto, eu fiz que isso lhes fosse por sujeira e o entregarei nas mãos dos estrangeiros, por presa, e aos perversos da terra, por despojo; eles o profanarão.
22 Desviarei deles o rosto, e profanarão o meu recesso; nele, entrarão profanadores e o saquearão.
23 Faze cadeia, porque a terra está cheia de crimes de sangue, e a cidade, cheia de violência.
24 Farei vir os piores de entre as nações, que possuirão as suas casas; farei cessar a arrogância dos valentes, e os seus lugares santos serão profanados.
25 Vem a destruição; eles buscarão paz, mas não há nenhuma.
26 Virá miséria sobre miséria, e se levantará rumor sobre rumor; buscarão visões de profetas; mas do sacerdote perecerá a lei, e dos anciãos, o conselho.
27 O rei se lamentará, e o príncipe se vestirá de horror, e as mãos do povo da terra tremerão de medo; segundo o seu caminho, lhes farei e, com os seus próprios juízos, os julgarei; e saberão que eu sou o Senhor.*
1 No sexto ano, no sexto mês, aos cinco dias do mês, estando eu sentado em minha casa, e os anciãos de Judá, assentados diante de mim, sucedeu que ali a mão do Senhor Deus caiu sobre mim.
2 Olhei, e eis uma figura como de fogo; desde os seus lombos e daí para baixo, era fogo e, dos seus lombos para cima, como o resplendor de metal brilhante.
3 Estendeu ela dali uma semelhança de mão e me tomou pelos cachos da cabeça; o Espírito me levantou entre a terra e o céu e me levou a Jerusalém em visões de Deus, até à entrada da porta do pátio de dentro, que olha para o norte, onde estava colocada a imagem dos ciúmes, que provoca o ciúme de Deus.
4 Eis que a glória do Deus de Israel estava ali, como a glória que eu vira no vale.
5 Ele me disse: Filho do homem, levanta agora os olhos para o norte. Levantei os olhos para lá, e eis que do lado norte, à porta do altar, estava esta imagem dos ciúmes, à entrada.
6 Disse-me ainda: Filho do homem, vês o que eles estão fazendo? As grandes abominações que a casa de Israel faz aqui, para que me afaste do meu santuário? Pois verás ainda maiores abominações.
7 Ele me levou à porta do átrio; olhei, e eis que havia um buraco na parede. Então, me disse: Filho do homem, cava naquela parede.
8 Cavei na parede, e eis que havia uma porta.
9 Disse-me: Entra e vê as terríveis abominações que eles fazem aqui.
10 Entrei e vi; eis toda forma de répteis e de animais abomináveis e de todos os ídolos da casa de Israel, pintados na parede em todo o redor.
11 Setenta homens dos anciãos da casa de Israel, com Jazanias, filho de Safã, que se achava no meio deles, estavam em pé diante das pinturas, tendo cada um na mão o seu incensário; e subia o aroma da nuvem de incenso.
12 Então, me disse: Viste, filho do homem, o que os anciãos da casa de Israel fazem nas trevas, cada um nas suas câmaras pintadas de imagens? Pois dizem: O Senhor não nos vê, o Senhor abandonou a terra.
13 Disse-me ainda: Tornarás a ver maiores abominações que eles estão fazendo.
14 Levou-me à entrada da porta da Casa do Senhor, que está no lado norte, e eis que estavam ali mulheres assentadas chorando a Tamuz.
15 Disse-me: Vês isto, filho do homem? Verás ainda abominações maiores do que estas.
16 Levou-me para o átrio de dentro da Casa do Senhor, e eis que estavam à entrada do templo do Senhor, entre o pórtico e o altar, cerca de vinte e cinco homens, de costas para o templo do Senhor e com o rosto para o oriente; adoravam o sol, virados para o oriente.
17 Então, me disse: Vês, filho do homem? Acaso, é coisa de pouca monta para a casa de Judá o fazerem eles as abominações que fazem aqui, para que ainda encham de violência a terra e tornem a irritar-me? Ei-los a chegar o ramo ao seu nariz.
18 Pelo que também eu os tratarei com furor; os meus olhos não pouparão, nem terei piedade. Ainda que me gritem aos ouvidos em alta voz, nem assim os ouvirei.*
1 Então, ouvi que gritava em alta voz, dizendo: Chegai-vos, vós executores da cidade, cada um com a sua arma destruidora na mão.
2 Eis que vinham seis homens a caminho da porta superior, que olha para o norte, cada um com a sua arma esmagadora na mão, e entre eles, certo homem vestido de linho, com um estojo de escrevedor à cintura; entraram e se puseram junto ao altar de bronze.
3 A glória do Deus de Israel se levantou do querubim sobre o qual estava, indo até à entrada da casa; e o Senhor clamou ao homem vestido de linho, que tinha o estojo de escrevedor à cintura,
4 e lhe disse: Passa pelo meio da cidade, pelo meio de Jerusalém, e marca com um sinal a testa dos homens que suspiram e gemem por causa de todas as abominações que se cometem no meio dela.
5 Aos outros disse, ouvindo eu: Passai pela cidade após ele; e, sem que os vossos olhos poupem e sem que vos compadeçais, matai;
6 matai a velhos, a moços e a virgens, a crianças e a mulheres, até exterminá-los; mas a todo homem que tiver o sinal não vos chegueis; começai pelo meu santuário.
7 Então, começaram pelos anciãos que estavam diante da casa. E ele lhes disse: Contaminai a casa, enchei de mortos os átrios e saí. Saíram e mataram na cidade.
8 Havendo-os eles matado, e ficando eu de resto, caí com o rosto em terra, clamei e disse: ah! Senhor Deus! Dar-se-á o caso que destruas todo o restante de Israel, derramando o teu furor sobre Jerusalém?
9 Então, me respondeu: A iniquidade da casa de Israel e de Judá é excessivamente grande, a terra se encheu de sangue, e a cidade, de injustiça; e eles ainda dizem: O Senhor abandonou a terra, o Senhor não nos vê.
10 Também quanto a mim, os meus olhos não pouparão, nem me compadecerei; porém sobre a cabeça deles farei recair as suas obras.
11 Eis que o homem que estava vestido de linho, a cuja cintura estava o estojo de escrevedor, relatou, dizendo: Fiz como me mandaste.*
1 Olhei, e eis que, no firmamento que estava por cima da cabeça dos querubins, apareceu sobre eles uma como pedra de safira semelhando a forma de um trono.
2 E falou ao homem vestido de linho, dizendo: Vai por entre as rodas, até debaixo dos querubins, e enche as mãos de brasas acesas dentre os querubins, e espalha-as sobre a cidade. Ele entrou à minha vista.
3 Os querubins estavam ao lado direito da casa, quando entrou o homem; e a nuvem encheu o átrio interior.
4 Então, se levantou a glória do Senhor de sobre o querubim, indo para a entrada da casa; a casa encheu-se da nuvem, e o átrio, da resplandecência da glória do Senhor.
5 O tatalar das asas dos querubins se ouviu até ao átrio exterior, como a voz do Deus Todo-Poderoso, quando fala.
6 Tendo o Senhor dado ordem ao homem vestido de linho, dizendo: Toma fogo dentre as rodas, dentre os querubins, ele entrou e se pôs junto às rodas.
7 Então, estendeu um querubim a mão de entre os querubins para o fogo que estava entre os querubins; tomou dele e o pôs nas mãos do homem que estava vestido de linho, o qual o tomou e saiu.
8 Tinham os querubins uma semelhança de mão de homem debaixo das suas asas.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Ezequiel','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)