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
17 Enviarei sobre vós a fome e bestas-feras que te desfilharão; a peste e o sangue passarão por ti, e trarei a espada sobre ti. Eu, o Senhor, falei.*
1 Veio a mim a palavra do Senhor, dizendo:
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
9 Olhei, e eis quatro rodas junto aos querubins, uma roda junto a cada querubim; o aspecto das rodas era brilhante como pedra de berilo.
10 Quanto ao seu aspecto, tinham as quatro a mesma aparência; eram como se estivesse uma roda dentro da outra.
11 Andando elas, podiam ir em quatro direções e não se viravam quando iam; para onde ia a primeira, seguiam as outras e não se viravam quando iam.
12 Todo o corpo dos querubins, suas costas, as mãos, as asas e também as rodas que os quatro tinham estavam cheias de olhos ao redor.
13 Quanto às rodas, foram elas chamadas girantes, ouvindo-o eu.
14 Cada um dos seres viventes tinha quatro rostos: o rosto do primeiro era rosto de querubim, o do segundo, rosto de homem, o do terceiro, rosto de leão, e o do quarto, rosto de águia.
15 Os querubins se elevaram. São estes os mesmos seres viventes que vi junto ao rio Quebar.
16 Andando os querubins, andavam as rodas juntamente com eles; e, levantando os querubins as suas asas, para se elevarem de sobre a terra, as rodas não se separavam deles.
17 Parando eles, paravam elas; e, elevando-se eles, elevavam-se elas, porque o espírito dos seres viventes estava nelas.
18 Então, saiu a glória do Senhor da entrada da casa e parou sobre os querubins.
19 Os querubins levantaram as suas asas e se elevaram da terra à minha vista, quando saíram acompanhados pelas rodas; pararam à entrada da porta oriental da Casa do Senhor, e a glória do Deus de Israel estava no alto, sobre eles.
20 São estes os seres viventes que vi debaixo do Deus de Israel, junto ao rio Quebar, e fiquei sabendo que eram querubins.
21 Cada um tinha quatro rostos e quatro asas e a semelhança de mãos de homem debaixo das asas.
22 A aparência dos seus rostos era como a dos rostos que eu vira junto ao rio Quebar; tinham o mesmo aspecto, eram os mesmos seres. Cada qual andava para a sua frente.*
1 Então, o Espírito me levantou e me levou à porta oriental da Casa do Senhor, a qual olha para o oriente. À entrada da porta, estavam vinte e cinco homens; no meio deles, vi a Jazanias, filho de Azur, e a Pelatias, filho de Benaías, príncipes do povo.
2 E disse-me: Filho do homem, são estes os homens que maquinam vilezas e aconselham perversamente nesta cidade,
3 os quais dizem: Não está próximo o tempo de construir casas; esta cidade é a panela, e nós, a carne.
4 Portanto, profetiza contra eles, profetiza, ó filho do homem.
5 Caiu, pois, sobre mim o Espírito do Senhor e disse-me: Fala: Assim diz o Senhor: Assim tendes dito, ó casa de Israel; porque, quanto às coisas que vos surgem à mente, eu as conheço.
6 Multiplicastes os vossos mortos nesta cidade e deles enchestes as suas ruas.
7 Portanto, assim diz o Senhor Deus: Os que vós matastes e largastes no meio dela são a carne, e ela, a panela; a vós outros, porém, vos tirarei do meio dela.
8 Temestes a espada, mas a espada trarei sobre vós, diz o Senhor Deus.
9 Tirar-vos-ei do meio dela, e vos entregarei nas mãos de estrangeiros, e executarei juízos entre vós.
10 Caireis à espada; nos confins de Israel, vos julgarei, e sabereis que eu sou o Senhor.
11 Esta cidade não vos servirá de panela, nem vós servireis de carne no seu meio; nos confins de Israel, vos julgarei,
12 e sabereis que eu sou o Senhor. Pois não andastes nos meus estatutos, nem executastes os meus juízos; antes, fizestes segundo os juízos das nações que estão em redor de vós.
13 Ao tempo em que eu profetizava, morreu Pelatias, filho de Benaías. Então, caí com o rosto em terra, clamei em alta voz e disse: ah! Senhor Deus! Darás fim ao resto de Israel?
14 Veio a mim a palavra do Senhor, dizendo:
15 Filho do homem, teus irmãos, os teus próprios irmãos, os homens do teu parentesco e toda a casa de Israel, todos eles são aqueles a quem os habitantes de Jerusalém disseram: Apartai-vos para longe do Senhor; esta terra se nos deu em possessão.
16 Portanto, dize: Assim diz o Senhor Deus: Ainda que os lancei para longe entre as nações e ainda que os espalhei pelas terras, todavia, lhes servirei de santuário, por um pouco de tempo, nas terras para onde foram.
17 Dize ainda: Assim diz o Senhor Deus: Hei de ajuntá-los do meio dos povos, e os recolherei das terras para onde foram lançados, e lhes darei a terra de Israel.
18 Voltarão para ali e tirarão dela todos os seus ídolos detestáveis e todas as suas abominações.
19 Dar-lhes-ei um só coração, espírito novo porei dentro deles; tirarei da sua carne o coração de pedra e lhes darei coração de carne;
20 para que andem nos meus estatutos, e guardem os meus juízos, e os executem; eles serão o meu povo, e eu serei o seu Deus.
21 Mas, quanto àqueles cujo coração se compraz em seus ídolos detestáveis e abominações, eu farei recair sobre sua cabeça as suas obras, diz o Senhor Deus.
22 Então, os querubins elevaram as suas asas, e as rodas os acompanhavam; e a glória do Deus de Israel estava no alto, sobre eles.
23 A glória do Senhor subiu do meio da cidade e se pôs sobre o monte que está ao oriente da cidade.
24 Depois, o Espírito de Deus me levantou e me levou na sua visão à Caldeia, para os do cativeiro; e de mim se foi a visão que eu tivera.
25 Então, falei aos do cativeiro todas as coisas que o Senhor me havia mostrado.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, tu habitas no meio da casa rebelde, que tem olhos para ver e não vê, tem ouvidos para ouvir e não ouve, porque é casa rebelde.
3 Tu, pois, ó filho do homem, prepara a bagagem de exílio e de dia sai, à vista deles, para o exílio; e, do lugar onde estás, parte para outro lugar, à vista deles. Bem pode ser que o entendam, ainda que eles são casa rebelde.
4 À vista deles, pois, traze para a rua, de dia, a tua bagagem de exílio; depois, à tarde, sairás, à vista deles, como quem vai para o exílio.
5 Abre um buraco na parede, à vista deles, e sai por ali.
6 À vista deles, aos ombros a levarás; às escuras, a transportarás; cobre o rosto para que não vejas a terra; porque por sinal te pus à casa de Israel.
7 Como se me ordenou, assim eu fiz: de dia, levei para fora a minha bagagem de exílio; então, à tarde, com as mãos abri para mim um buraco na parede; às escuras, eu saí e, aos ombros, transportei a bagagem, à vista deles.
8 Pela manhã, veio a mim a palavra do Senhor, dizendo:
9 Filho do homem, não te perguntou a casa de Israel, aquela casa rebelde: Que fazes tu?
10 Dize-lhes: Assim diz o Senhor Deus: Esta sentença refere-se ao príncipe em Jerusalém e a toda a casa de Israel, que está no meio dela.
11 Dize: Eu sou o vosso sinal. Como eu fiz, assim se lhes fará a eles; irão para o exílio, para o cativeiro.
12 O príncipe que está no meio deles levará aos ombros a bagagem e, às escuras, sairá; abrirá um buraco na parede para sair por ele; cobrirá o rosto para que seus olhos não vejam a terra.
13 Também estenderei a minha rede sobre ele, e será apanhado nas minhas malhas; levá-lo-ei a Babilônia, à terra dos caldeus, mas não a verá, ainda que venha a morrer ali.
14 A todos os ventos espalharei todos os que, para o ajudarem, estão ao redor dele, e todas as suas tropas; desembainharei a espada após eles.
15 Saberão que eu sou o Senhor, quando eu os dispersar entre as nações e os espalhar pelas terras.
16 Deles deixarei ficar alguns poucos, escapos da espada, da fome e da peste, para que publiquem todas as suas coisas abomináveis entre as nações para onde forem; e saberão que eu sou o Senhor.
17 Então, veio a mim a palavra do Senhor, dizendo:
18 Filho do homem, o teu pão comerás com tremor e a tua água beberás com estremecimento e ansiedade;
19 e dirás ao povo da terra: Assim diz o Senhor Deus acerca dos habitantes de Jerusalém, na terra de Israel: O seu pão comerão com ansiedade e a sua água beberão com espanto, pois que a sua terra será despojada de tudo quanto contém, por causa da violência de todos os que nela habitam.
20 As cidades habitadas cairão em ruínas, e a terra se tornará em desolação; e sabereis que eu sou o Senhor.
21 Veio a mim a palavra do Senhor, dizendo:
22 Filho do homem, que provérbio é esse que vós tendes na terra de Israel: Prolongue-se o tempo, e não se cumpra a profecia?
23 Portanto, dize-lhes: Assim diz o Senhor Deus: Farei cessar esse provérbio, e já não se servirão dele em Israel; mas dize-lhes: Os dias estão próximos e o cumprimento de toda profecia.
24 Porque já não haverá visão falsa nenhuma, nem adivinhação lisonjeira, no meio da casa de Israel.
25 Porque eu, o Senhor, falarei, e a palavra que eu falar se cumprirá e não será retardada; porque, em vossos dias, ó casa rebelde, falarei a palavra e a cumprirei, diz o Senhor Deus.
26 Veio-me ainda a palavra do Senhor, dizendo:
27 Filho do homem, eis que os da casa de Israel dizem: A visão que tem este é para muitos dias, e ele profetiza de tempos que estão mui longe.
28 Portanto, dize-lhes: Assim diz o Senhor Deus: Não será retardada nenhuma das minhas palavras; e a palavra que falei se cumprirá, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, profetiza contra os profetas de Israel que, profetizando, exprimem, como dizes, o que lhes vem do coração. Ouvi a palavra do Senhor.
3 Assim diz o Senhor Deus: Ai dos profetas loucos, que seguem o seu próprio espírito sem nada ter visto!
4 Os teus profetas, ó Israel, são como raposas entre as ruínas.
5 Não subistes às brechas, nem fizestes muros para a casa de Israel, para que ela permaneça firme na peleja no Dia do Senhor.
6 Tiveram visões falsas e adivinhação mentirosa os que dizem: O Senhor disse; quando o Senhor os não enviou; e esperam o cumprimento da palavra.
7 Não tivestes visões falsas e não falastes adivinhação mentirosa, quando dissestes: O Senhor diz, sendo que eu tal não falei?
8 Portanto, assim diz o Senhor Deus: Como falais falsidade e tendes visões mentirosas, por isso, eu sou contra vós outros, diz o Senhor Deus.
9 Minha mão será contra os profetas que têm visões falsas e que adivinham mentiras; não estarão no conselho do meu povo, não serão inscritos nos registros da casa de Israel, nem entrarão na terra de Israel. Sabereis que eu sou o Senhor Deus.
10 Visto que andam enganando, sim, enganando o meu povo, dizendo: Paz, quando não há paz, e quando se edifica uma parede, e os profetas a caiam,
11 dize aos que a caiam que ela ruirá. Haverá chuva de inundar. Vós, ó pedras de saraivada, caireis, e tu, vento tempestuoso, irromperás.
12 Ora, eis que, caindo a parede, não vos dirão: Onde está a cal com que a caiastes?
13 Portanto, assim diz o Senhor Deus: Tempestuoso vento farei irromper no meu furor, e chuva de inundar haverá na minha ira, e pedras de saraivada, na minha indignação, para a consumir.
14 Derribarei a parede que caiastes, darei com ela por terra, e o seu fundamento se descobrirá; quando cair, perecereis no meio dela e sabereis que eu sou o Senhor.
15 Assim, cumprirei o meu furor contra a parede e contra os que a caiaram e vos direi: a parede já não existe, nem aqueles que a caiaram,
16 os profetas de Israel que profetizaram a respeito de Jerusalém e para ela têm visões de paz, quando não há paz, diz o Senhor Deus.
17 Tu, ó filho do homem, põe-te contra as filhas do teu povo que profetizam de seu coração, profetiza contra elas
18 e dize: Assim diz o Senhor Deus: Ai das que cosem invólucros feiticeiros para todas as articulações das mãos e fazem véus para cabeças de todo tamanho, para caçarem almas! Querereis matar as almas do meu povo e preservar outras para vós mesmas?
19 Vós me profanastes entre o meu povo, por punhados de cevada e por pedaços de pão, para matardes as almas que não haviam de morrer e para preservardes com vida as almas que não haviam de viver, mentindo, assim, ao meu povo, que escuta mentiras.
20 Portanto, assim diz o Senhor Deus: Eis aí vou eu contra vossos invólucros feiticeiros, com que vós caçais as almas como aves, e as arrancarei de vossas mãos; soltarei livres como aves as almas que prendestes.
21 Também rasgarei os vossos véus e livrarei o meu povo das vossas mãos, e nunca mais estará ao vosso alcance para ser caçado; e sabereis que eu sou o Senhor.
22 Visto que com falsidade entristecestes o coração do justo, não o havendo eu entristecido, e fortalecestes as mãos do perverso para que não se desviasse do seu mau caminho e vivesse,
23 por isso, já não tereis visões falsas, nem jamais fareis adivinhações; livrarei o meu povo das vossas mãos, e sabereis que eu sou o Senhor.*
1 Então, vieram ter comigo alguns dos anciãos de Israel e se assentaram diante de mim.
2 Veio a mim a palavra do Senhor, dizendo:
3 Filho do homem, estes homens levantaram os seus ídolos dentro do seu coração, tropeço para a iniquidade que sempre têm eles diante de si; acaso, permitirei que eles me interroguem?
4 Portanto, fala com eles e dize-lhes: Assim diz o Senhor Deus: Qualquer homem da casa de Israel que levantar os seus ídolos dentro do seu coração, e tem tal tropeço para a sua iniquidade, e vier ao profeta, eu, o Senhor, vindo ele, lhe responderei segundo a multidão dos seus ídolos;
5 para que eu possa apanhar a casa de Israel no seu próprio coração, porquanto todos se apartaram de mim para seguirem os seus ídolos.
6 Portanto, dize à casa de Israel: Assim diz o Senhor Deus: Convertei-vos, e apartai-vos dos vossos ídolos, e dai as costas a todas as vossas abominações,
7 porque qualquer homem da casa de Israel ou dos estrangeiros que moram em Israel que se alienar de mim, e levantar os seus ídolos dentro do seu coração, e tiver tal tropeço para a iniquidade, e vier ao profeta, para me consultar por meio dele, a esse, eu, o Senhor, responderei por mim mesmo.
8 Voltarei o rosto contra o tal homem, e o farei sinal e provérbio, e eliminá-lo-ei do meio do meu povo; e sabereis que eu sou o Senhor.
9 Se o profeta for enganado e falar alguma coisa, fui eu, o Senhor, que enganei esse profeta; estenderei a mão contra ele e o eliminarei do meio do meu povo de Israel.
10 Ambos levarão sobre si a sua iniquidade; a iniquidade daquele que consulta será como a do profeta;
11 para que a casa de Israel não se desvie mais de mim, nem mais se contamine com todas as suas transgressões. Então, diz o Senhor Deus: Eles serão o meu povo, e eu serei o seu Deus.
12 Veio ainda a mim a palavra do Senhor, dizendo:
13 Filho do homem, quando uma terra pecar contra mim, cometendo graves transgressões, estenderei a mão contra ela, e tornarei instável o sustento do pão, e enviarei contra ela fome, e eliminarei dela homens e animais;
14 ainda que estivessem no meio dela estes três homens, Noé, Daniel e Jó, eles, pela sua justiça, salvariam apenas a sua própria vida, diz o Senhor Deus.
15 Se eu fizer passar pela terra bestas-feras, e elas a assolarem, que fique assolada, e ninguém possa passar por ela por causa das feras;
16 tão certo como eu vivo, diz o Senhor Deus, ainda que esses três homens estivessem no meio dela, não salvariam nem a seus filhos nem a suas filhas; só eles seriam salvos, e a terra seria assolada.
17 Ou se eu fizer vir a espada sobre essa terra e disser: Espada, passa pela terra; e eu eliminar dela homens e animais,
18 tão certo como eu vivo, diz o Senhor Deus, ainda que esses três homens estivessem no meio dela, não salvariam nem a seus filhos nem a suas filhas; só eles seriam salvos.
19 Ou se eu enviar a peste sobre essa terra e derramar o meu furor sobre ela com sangue, para eliminar dela homens e animais,
20 tão certo como eu vivo, diz o Senhor Deus, ainda que Noé, Daniel e Jó estivessem no meio dela, não salvariam nem a seu filho nem a sua filha; pela sua justiça salvariam apenas a sua própria vida.
21 Porque assim diz o Senhor Deus: Quanto mais, se eu enviar os meus quatro maus juízos, a espada, a fome, as bestas-feras e a peste, contra Jerusalém, para eliminar dela homens e animais?
22 Mas eis que alguns restarão nela, que levarão fora tanto filhos como filhas; eis que eles virão a vós outros, e vereis o seu caminho e os seus feitos; e ficareis consolados do mal que eu fiz vir sobre Jerusalém, sim, de tudo o que fiz vir sobre ela.
23 Eles vos consolarão quando virdes o seu caminho e os seus feitos; e sabereis que não foi sem motivo tudo quanto fiz nela, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, por que mais é o sarmento de videira que qualquer outro, o sarmento que está entre as árvores do bosque?
3 Toma-se dele madeira para fazer alguma obra? Ou toma-se dele alguma estaca, para que se lhe pendure algum objeto?
4 Eis que é lançado no fogo, para ser consumido; se ambas as suas extremidades consome o fogo, e o meio dele fica também queimado, serviria, acaso, para alguma obra?
5 Ora, se, estando inteiro, não servia para obra alguma, quanto menos sendo consumido pelo fogo ou sendo queimado, se faria dele qualquer obra?
6 Portanto, assim diz o Senhor Deus: Como o sarmento da videira entre as árvores do bosque, que dei ao fogo para que seja consumido, assim entregarei os habitantes de Jerusalém.
7 Voltarei o rosto contra eles; ainda que saiam do fogo, o fogo os consumirá; e sabereis que eu sou o Senhor, quando tiver voltado o rosto contra eles.
8 Tornarei a terra em desolação, porquanto cometeram graves transgressões, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, faze conhecer a Jerusalém as suas abominações;
3 e dize: Assim diz o Senhor Deus a Jerusalém: A tua origem e o teu nascimento procedem da terra dos cananeus; teu pai era amorreu, e tua mãe, heteia.
4 Quanto ao teu nascimento, no dia em que nasceste, não te foi cortado o umbigo, nem foste lavada com água para te limpar, nem esfregada com sal, nem envolta em faixas.
5 Não se apiedou de ti olho algum, para te fazer alguma destas coisas, compadecido de ti; antes, foste lançada em pleno campo, no dia em que nasceste, porque tiveram nojo de ti.
6 Passando eu por junto de ti, vi-te a revolver-te no teu sangue e te disse: Ainda que estás no teu sangue, vive; sim, ainda que estás no teu sangue, vive.
7 Eu te fiz multiplicar como o renovo do campo; cresceste, e te engrandeceste, e chegaste a grande formosura; formaram-se os teus seios, e te cresceram cabelos; no entanto, estavas nua e descoberta.
8 Passando eu por junto de ti, vi-te, e eis que o teu tempo era tempo de amores; estendi sobre ti as abas do meu manto e cobri a tua nudez; dei-te juramento e entrei em aliança contigo, diz o Senhor Deus; e passaste a ser minha.
9 Então, te lavei com água, e te enxuguei do teu sangue, e te ungi com óleo.
10 Também te vesti de roupas bordadas, e te calcei com couro da melhor qualidade, e te cingi de linho fino, e te cobri de seda.
11 Também te adornei com enfeites e te pus braceletes nas mãos e colar à roda do teu pescoço.
12 Coloquei-te um pendente no nariz, arrecadas nas orelhas e linda coroa na cabeça.
13 Assim, foste ornada de ouro e prata; o teu vestido era de linho fino, de seda e de bordados; nutriste-te de flor de farinha, de mel e azeite; eras formosa em extremo e chegaste a ser rainha.
14 Correu a tua fama entre as nações, por causa da tua formosura, pois era perfeita, por causa da minha glória que eu pusera em ti, diz o Senhor Deus.
15 Mas confiaste na tua formosura e te entregaste à lascívia, graças à tua fama; e te ofereceste a todo o que passava, para seres dele.
16 Tomaste dos teus vestidos e fizeste lugares altos adornados de diversas cores, nos quais te prostituíste; tais coisas nunca se deram e jamais se darão.
17 Tomaste as tuas joias de enfeite, que eu te dei do meu ouro e da minha prata, fizeste estátuas de homens e te prostituíste com elas.
18 Tomaste os teus vestidos bordados e as cobriste; o meu óleo e o meu perfume puseste diante delas.
19 O meu pão, que te dei, a flor da farinha, o óleo e o mel, com que eu te sustentava, também puseste diante delas em aroma suave; e assim se fez, diz o Senhor Deus.
20 Demais, tomaste a teus filhos e tuas filhas, que me geraste, os sacrificaste a elas, para serem consumidos. Acaso, é pequena a tua prostituição?
21 Mataste a meus filhos e os entregaste a elas como oferta pelo fogo.
22 Em todas as tuas abominações e nas tuas prostituições, não te lembraste dos dias da tua mocidade, quando estavas nua e descoberta, a revolver-te no teu sangue.
23 Depois de toda a tua maldade (Ai, ai de ti! — diz o Senhor Deus),
24 edificaste prostíbulo de culto e fizeste elevados altares por todas as praças.
25 A cada canto do caminho, edificaste o teu altar, e profanaste a tua formosura, e abriste as pernas a todo que passava, e multiplicaste as tuas prostituições.
26 Também te prostituíste com os filhos do Egito, teus vizinhos de grandes membros, e multiplicaste a tua prostituição, para me provocares à ira.
27 Por isso, estendi a mão contra ti e diminuí a tua porção; e te entreguei à vontade das que te aborrecem, as filhas dos filisteus, as quais se envergonhavam do teu caminho depravado.
28 Também te prostituíste com os filhos da Assíria, porquanto eras insaciável; e, prostituindo-te com eles, nem ainda assim te fartaste;
29 antes, multiplicaste as tuas prostituições na terra de Canaã até a Caldeia e ainda com isso não te fartaste.
30 Quão fraco é o teu coração, diz o Senhor Deus, fazendo tu todas estas coisas, só próprias de meretriz descarada.
31 Edificando tu o teu prostíbulo de culto à entrada de cada rua e os teus elevados altares em cada praça, não foste sequer como a meretriz, pois desprezaste a paga;
32 foste como a mulher adúltera, que, em lugar de seu marido, recebe os estranhos.
33 A todas as meretrizes se dá a paga, mas tu dás presentes a todos os teus amantes; e o fazes para que venham a ti de todas as partes adulterar contigo.
34 Contigo, nas tuas prostituições, sucede o contrário do que se dá com outras mulheres, pois não te procuram para prostituição, porque, dando tu a paga e a ti não sendo dada, fazes o contrário.
35 Portanto, ó meretriz, ouve a palavra do Senhor.
36 Assim diz o Senhor Deus: Por se ter exagerado a tua lascívia e se ter descoberto a tua nudez nas tuas prostituições com os teus amantes; e por causa também das abominações de todos os teus ídolos e do sangue de teus filhos a estes sacrificados,
37 eis que ajuntarei todos os teus amantes, com os quais te deleitaste, como também todos os que amaste, com todos os que aborreceste; ajuntá-los-ei de todas as partes contra ti e descobrirei as tuas vergonhas diante deles, para que todos as vejam.
38 Julgar-te-ei como são julgadas as adúlteras e as sanguinárias; e te farei vítima de furor e de ciúme.
39 Entregar-te-ei nas suas mãos, e derribarão o teu prostíbulo de culto e os teus elevados altares; despir-te-ão de teus vestidos, tomarão as tuas finas joias e te deixarão nua e descoberta.
40 Farão subir contra ti uma multidão, apedrejar-te-ão e te traspassarão com suas espadas.
41 Queimarão as tuas casas e executarão juízos contra ti, à vista de muitas mulheres; farei cessar o teu meretrício, e já não darás paga.
42 Desse modo, satisfarei em ti o meu furor, os meus ciúmes se apartarão de ti, aquietar-me-ei e jamais me indignarei.
43 Visto que não te lembraste dos dias da tua mocidade e me provocaste à ira com tudo isto, eis que também eu farei recair sobre a tua cabeça o castigo do teu procedimento, diz o Senhor Deus; e a todas as tuas abominações não acrescentarás esta depravação.
44 Eis que todo o que usa de provérbios usará contra ti este, dizendo: Tal mãe, tal filha.
45 Tu és filha de tua mãe, que teve nojo de seu marido e de seus filhos; e tu és irmã de tuas irmãs, que tiveram nojo de seus maridos e de seus filhos; vossa mãe foi heteia, e vosso pai, amorreu.
46 E tua irmã, a maior, é Samaria, que habita à tua esquerda com suas filhas; e a tua irmã, a menor, que habita à tua mão direita, é Sodoma e suas filhas.
47 Todavia, não só andaste nos seus caminhos, nem só fizeste segundo as suas abominações; mas, como se isto fora mui pouco, ainda te corrompeste mais do que elas, em todos os teus caminhos.
48 Tão certo como eu vivo, diz o Senhor Deus, não fez Sodoma, tua irmã, ela e suas filhas, como tu fizeste, e também tuas filhas.
49 Eis que esta foi a iniquidade de Sodoma, tua irmã: soberba, fartura de pão e próspera tranquilidade teve ela e suas filhas; mas nunca amparou o pobre e o necessitado.
50 Foram arrogantes e fizeram abominações diante de mim; pelo que, em vendo isto, as removi dali.
51 Também Samaria não cometeu metade de teus pecados; pois tu multiplicaste as tuas abominações mais do que elas e assim justificaste a tuas irmãs com todas as abominações que fizeste.
52 Tu, pois, levas a tua ignomínia, tu que advogaste a causa de tuas irmãs; pelos pecados que cometeste, mais abomináveis do que elas, mais justas são elas do que tu; envergonha-te logo também e leva a tua ignomínia, pois justificaste a tuas irmãs.
53 Restaurarei a sorte delas, a de Sodoma e de suas filhas, a de Samaria e de suas filhas e a tua própria sorte entre elas,
54 para que leves a tua ignomínia e sejas envergonhada por tudo o que fizeste, servindo-lhes de consolação.
55 Quando tuas irmãs, Sodoma e suas filhas, tornarem ao seu primeiro estado, e Samaria e suas filhas tornarem ao seu, também tu e tuas filhas tornareis ao vosso primeiro estado.
56 Não usaste como provérbio o nome Sodoma, tua irmã, nos dias da tua soberba,
57 antes que se descobrisse a tua maldade? Agora, te tornaste, como ela, objeto de opróbrio das filhas da Síria e de todos os que estão ao redor dela, as filhas dos filisteus que te desprezam.
58 As tuas depravações e as tuas abominações tu levarás, diz o Senhor.
59 Porque assim diz o Senhor Deus: Eu te farei a ti como fizeste, pois desprezaste o juramento, invalidando a aliança.
60 Mas eu me lembrarei da aliança que fiz contigo nos dias da tua mocidade e estabelecerei contigo uma aliança eterna.
61 Então, te lembrarás dos teus caminhos e te envergonharás quando receberes as tuas irmãs, tanto as mais velhas como as mais novas, e tas darei por filhas, mas não pela tua aliança.
62 Estabelecerei a minha aliança contigo, e saberás que eu sou o Senhor,
63 para que te lembres e te envergonhes, e nunca mais fale a tua boca soberbamente, por causa do teu opróbrio, quando eu te houver perdoado tudo quanto fizeste, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, propõe um enigma e usa de uma parábola para com a casa de Israel;
3 e dize: Assim diz o Senhor Deus: Uma grande águia, de grandes asas, de comprida plumagem, farta de penas de várias cores, veio ao Líbano e levou a ponta de um cedro.
4 Arrancou a ponta mais alta dos seus ramos e a levou para uma terra de negociantes; na cidade de mercadores, a deixou.
5 Tomou muda da terra e a plantou num campo fértil; tomou-a e pôs junto às muitas águas, como salgueiro.
6 Ela cresceu e se tornou videira mui larga, de pouca altura, virando para a águia os seus ramos, porque as suas raízes estavam debaixo dela; assim, se tornou em videira, e produzia ramos, e lançava renovos.
7 Houve outra grande águia, de grandes asas e de muitas penas; e eis que a videira lançou para ela as suas raízes e estendeu para ela os seus ramos, desde a cova do seu plantio, para que a regasse.
8 Em boa terra, à borda de muitas águas, estava ela plantada, para produzir ramos, e dar frutos, e ser excelente videira.
9 Dize: Assim diz o Senhor Deus: Acaso, prosperará ela? Não lhe arrancará a águia as raízes e não cortará o seu fruto, para que se sequem todas as folhas de seus renovos? Não será necessário nem poderoso braço nem muita gente para a arrancar por suas raízes.
10 Mas, ainda plantada, prosperará? Acaso, tocando-lhe o vento oriental, de todo não se secará? Desde a cova do seu plantio se secará.
11 Então, veio a mim a palavra do Senhor, dizendo:
12 Dize agora à casa rebelde: Não sabeis o que significam estas coisas? Dize: Eis que veio o rei da Babilônia a Jerusalém, e tomou o seu rei e os seus príncipes, e os levou consigo para a Babilônia;
13 tomou um da estirpe real e fez aliança com ele; também tomou dele juramento, levou os poderosos da terra,
14 para que o reino ficasse humilhado e não se levantasse, mas, guardando a sua aliança, pudesse subsistir.
15 Mas ele se rebelou contra o rei da Babilônia, enviando os seus mensageiros ao Egito, para que se lhe mandassem cavalos e muita gente. Prosperará, escapará aquele que faz tais coisas? Violará a aliança e escapará?
16 Tão certo como eu vivo, diz o Senhor Deus, no lugar em que habita o rei que o fez reinar, cujo juramento desprezou e cuja aliança violou, sim, junto dele, no meio da Babilônia será morto.
17 Faraó, nem com grande exército, nem com numerosa companhia, o ajudará na guerra, levantando tranqueiras e edificando baluartes, para destruir muitas vidas.
18 Pois desprezou o juramento, violando a aliança feita com aperto de mão, e praticou todas estas coisas; por isso, não escapará.
19 Portanto, assim diz o Senhor Deus: Tão certo como eu vivo, o meu juramento que desprezou e a minha aliança que violou, isto farei recair sobre a sua cabeça.
20 Estenderei sobre ele a minha rede, e ficará preso no meu laço; levá-lo-ei à Babilônia e ali entrarei em juízo com ele por causa da rebeldia que praticou contra mim.
21 Todos os seus fugitivos, com todas as suas tropas, cairão à espada, e os que restarem serão espalhados a todos os ventos; e sabereis que eu, o Senhor, o disse.
22 Assim diz o Senhor Deus: Também eu tomarei a ponta de um cedro e a plantarei; do principal dos seus ramos cortarei o renovo mais tenro e o plantarei sobre um monte alto e sublime.
23 No monte alto de Israel, o plantarei, e produzirá ramos, dará frutos e se fará cedro excelente. Debaixo dele, habitarão animais de toda sorte, e à sombra dos seus ramos se aninharão aves de toda espécie.
24 Saberão todas as árvores do campo que eu, o Senhor, abati a árvore alta, elevei a baixa, sequei a árvore verde e fiz reverdecer a seca; eu, o Senhor, o disse e o fiz.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Que tendes vós, vós que, acerca da terra de Israel, proferis este provérbio, dizendo: Os pais comeram uvas verdes, e os dentes dos filhos é que se embotaram?
3 Tão certo como eu vivo, diz o Senhor Deus, jamais direis este provérbio em Israel.
4 Eis que todas as almas são minhas; como a alma do pai, também a alma do filho é minha; a alma que pecar, essa morrerá.
5 Sendo, pois, o homem justo e fazendo juízo e justiça,
6 não comendo carne sacrificada nos altos, nem levantando os olhos para os ídolos da casa de Israel, nem contaminando a mulher do seu próximo, nem se chegando à mulher na sua menstruação;
7 não oprimindo a ninguém, tornando ao devedor a coisa penhorada, não roubando, dando o seu pão ao faminto e cobrindo ao nu com vestes;
8 não dando o seu dinheiro à usura, não recebendo juros, desviando a sua mão da injustiça e fazendo verdadeiro juízo entre homem e homem;
9 andando nos meus estatutos, guardando os meus juízos e procedendo retamente, o tal justo, certamente, viverá, diz o Senhor Deus.
10 Se ele gerar um filho ladrão, derramador de sangue, que fizer a seu irmão qualquer destas coisas
11 e não cumprir todos aqueles deveres, mas, antes, comer carne sacrificada nos altos, contaminar a mulher de seu próximo,
12 oprimir ao pobre e necessitado, praticar roubos, não tornar o penhor, levantar os olhos para os ídolos, cometer abominação,
13 emprestar com usura e receber juros, porventura, viverá? Não viverá. Todas estas abominações ele fez e será morto; o seu sangue será sobre ele.
14 Eis que, se ele gerar um filho que veja todos os pecados que seu pai fez, e, vendo-os, não cometer coisas semelhantes,
15 não comer carne sacrificada nos altos, não levantar os olhos para os ídolos da casa de Israel e não contaminar a mulher de seu próximo;
16 não oprimir a ninguém, não retiver o penhor, não roubar, der o seu pão ao faminto, cobrir ao nu com vestes;
17 desviar do pobre a mão, não receber usura e juros, fizer os meus juízos e andar nos meus estatutos, o tal não morrerá pela iniquidade de seu pai; certamente, viverá.
18 Quanto a seu pai, porque praticou extorsão, roubou os bens do próximo e fez o que não era bom no meio de seu povo, eis que ele morrerá por causa de sua iniquidade.
19 Mas dizeis: Por que não leva o filho a iniquidade do pai? Porque o filho fez o que era reto e justo, e guardou todos os meus estatutos, e os praticou, por isso, certamente, viverá.
20 A alma que pecar, essa morrerá; o filho não levará a iniquidade do pai, nem o pai, a iniquidade do filho; a justiça do justo ficará sobre ele, e a perversidade do perverso cairá sobre este.
21 Mas, se o perverso se converter de todos os pecados que cometeu, e guardar todos os meus estatutos, e fizer o que é reto e justo, certamente, viverá; não será morto.
22 De todas as transgressões que cometeu não haverá lembrança contra ele; pela justiça que praticou, viverá.
23 Acaso, tenho eu prazer na morte do perverso? — diz o Senhor Deus; não desejo eu, antes, que ele se converta dos seus caminhos e viva?
24 Mas, desviando-se o justo da sua justiça e cometendo iniquidade, fazendo segundo todas as abominações que faz o perverso, acaso, viverá? De todos os atos de justiça que tiver praticado não se fará memória; na sua transgressão com que transgrediu e no seu pecado que cometeu, neles morrerá.
25 No entanto, dizeis: O caminho do Senhor não é direito. Ouvi, agora, ó casa de Israel: Não é o meu caminho direito? Não são os vossos caminhos tortuosos?
26 Desviando-se o justo da sua justiça e cometendo iniquidade, morrerá por causa dela; na iniquidade que cometeu, morrerá.
27 Mas, convertendo-se o perverso da perversidade que cometeu e praticando o que é reto e justo, conservará ele a sua alma em vida.
28 Pois se considera e se converte de todas as transgressões que cometeu, certamente, viverá; não será morto.
29 No entanto, diz a casa de Israel: O caminho do Senhor não é direito. Não são os meus caminhos direitos, ó casa de Israel? E não são os vossos caminhos tortuosos?
30 Portanto, eu vos julgarei, a cada um segundo os seus caminhos, ó casa de Israel, diz o Senhor Deus. Convertei-vos e desviai-vos de todas as vossas transgressões; e a iniquidade não vos servirá de tropeço.
31 Lançai de vós todas as vossas transgressões com que transgredistes e criai em vós coração novo e espírito novo; pois, por que morreríeis, ó casa de Israel?
32 Porque não tenho prazer na morte de ninguém, diz o Senhor Deus. Portanto, convertei-vos e vivei.*
1 E tu levanta uma lamentação sobre os príncipes de Israel
2 e dize: Quem é tua mãe? Uma leoa entre leões, a qual, deitada entre os leõezinhos, criou os seus filhotes.
3 Criou um dos seus filhotinhos, o qual veio a ser leãozinho, e aprendeu a apanhar a presa, e devorou homens.
4 As nações ouviram falar dele, e foi ele apanhado na cova que elas fizeram e levado com ganchos para a terra do Egito.
5 Vendo a leoa frustrada e perdida a sua esperança, tomou outro dos seus filhotes e o fez leãozinho.
6 Este, andando entre os leões, veio a ser um leãozinho, e aprendeu a apanhar a presa, e devorou homens.
7 Aprendeu a fazer viúvas e a tornar desertas as cidades deles; ficaram estupefatos a terra e seus habitantes, ao ouvirem o seu rugido.
8 Então, se ajuntaram contra ele as gentes das províncias em roda, estenderam sobre ele a rede, e foi apanhado na cova que elas fizeram.
9 Com gancho, meteram-no em jaula, e o levaram ao rei da Babilônia, e fizeram-no entrar nos lugares fortes, para que se não ouvisse mais a sua voz nos montes de Israel.
10 Tua mãe, de sua natureza, era qual videira plantada junto às águas; plantada à borda, ela frutificou e se encheu de ramos, por causa das muitas águas.
11 Tinha galhos fortes para cetros de dominadores; elevou-se a sua estatura entre os espessos ramos, e foi vista na sua altura com a multidão deles.
12 Mas foi arrancada com furor e lançada por terra, e o vento oriental secou-lhe o fruto; quebraram-se e secaram os seus fortes galhos, e o fogo os consumiu.
13 Agora, está plantada no deserto, numa terra seca e sedenta.
14 Dos galhos dos seus ramos saiu fogo que consumiu o seu fruto, de maneira que já não há nela galho forte que sirva de cetro para dominar. Esta é uma lamentação e ficará servindo de lamentação.*
1 No quinto mês do sétimo ano, aos dez dias do mês, vieram alguns dos anciãos de Israel para consultar ao Senhor; e assentaram-se diante de mim.
2 Então, veio a mim a palavra do Senhor, dizendo:
3 Filho do homem, fala aos anciãos de Israel e dize-lhes: Assim diz o Senhor Deus: Acaso, viestes consultar-me? Tão certo como eu vivo, diz o Senhor Deus, vós não me consultareis.
4 Julgá-los-ias tu, ó filho do homem, julgá-los-ias? Faze-lhes saber as abominações de seus pais
5 e dize-lhes: Assim diz o Senhor Deus: No dia em que escolhi a Israel, levantando a mão, jurei à descendência da casa de Jacó e me dei a conhecer a eles na terra do Egito; levantei-lhes a mão e jurei: Eu sou o Senhor, vosso Deus.
6 Naquele dia, levantei-lhes a mão e jurei tirá-los da terra do Egito para uma terra que lhes tinha previsto, a qual mana leite e mel, coroa de todas as terras.
7 Então, lhes disse: Cada um lance de si as abominações de que se agradam os seus olhos, e não vos contamineis com os ídolos do Egito; eu sou o Senhor, vosso Deus.
8 Mas rebelaram-se contra mim e não me quiseram ouvir; ninguém lançava de si as abominações de que se agradavam os seus olhos, nem abandonava os ídolos do Egito. Então, eu disse que derramaria sobre eles o meu furor, para cumprir a minha ira contra eles, no meio da terra do Egito.
9 O que fiz, porém, foi por amor do meu nome, para que não fosse profanado diante das nações no meio das quais eles estavam, diante das quais eu me dei a conhecer a eles, para os tirar da terra do Egito.
10 Tirei-os da terra do Egito e os levei para o deserto.
11 Dei-lhes os meus estatutos e lhes fiz conhecer os meus juízos, os quais, cumprindo-os o homem, viverá por eles.
12 Também lhes dei os meus sábados, para servirem de sinal entre mim e eles, para que soubessem que eu sou o Senhor que os santifica.
13 Mas a casa de Israel se rebelou contra mim no deserto, não andando nos meus estatutos e rejeitando os meus juízos, os quais, cumprindo-os o homem, viverá por eles; e profanaram grandemente os meus sábados. Então, eu disse que derramaria sobre eles o meu furor no deserto, para os consumir.
14 O que fiz, porém, foi por amor do meu nome, para que não fosse profanado diante das nações perante as quais os fiz sair.
15 Demais, levantei-lhes no deserto a mão e jurei não deixá-los entrar na terra que lhes tinha dado, a qual mana leite e mel, coroa de todas as terras.
16 Porque rejeitaram os meus juízos, e não andaram nos meus estatutos, e profanaram os meus sábados, pois o seu coração andava após os seus ídolos.
17 Não obstante, os meus olhos lhes perdoaram, e eu não os destruí, nem os consumi de todo no deserto.
18 Mas disse eu a seus filhos no deserto: Não andeis nos estatutos de vossos pais, nem guardeis os seus juízos, nem vos contamineis com os seus ídolos.
19 Eu sou o Senhor, vosso Deus; andai nos meus estatutos, e guardai os meus juízos, e praticai-os;
20 santificai os meus sábados, pois servirão de sinal entre mim e vós, para que saibais que eu sou o Senhor, vosso Deus.
21 Mas também os filhos se rebelaram contra mim e não andaram nos meus estatutos, nem guardaram os meus juízos, os quais, cumprindo-os o homem, viverá por eles; antes, profanaram os meus sábados. Então, eu disse que derramaria sobre eles o meu furor, para cumprir contra eles a minha ira no deserto.
22 Mas detive a mão e o fiz por amor do meu nome, para que não fosse profanado diante das nações perante as quais os fiz sair.
23 Também levantei-lhes no deserto a mão e jurei espalhá-los entre as nações e derramá-los pelas terras;
24 porque não executaram os meus juízos, rejeitaram os meus estatutos, profanaram os meus sábados, e os seus olhos se iam após os ídolos de seus pais;
25 pelo que também lhes dei estatutos que não eram bons e juízos pelos quais não haviam de viver;
26 e permiti que eles se contaminassem com seus dons sacrificiais, como quando queimavam tudo o que abre a madre, para horrorizá-los, a fim de que soubessem que eu sou o Senhor.
27 Portanto, fala à casa de Israel, ó filho do homem, e dize-lhes: Assim diz o Senhor Deus: Ainda nisto me blasfemaram vossos pais e transgrediram contra mim.
28 Porque, havendo-os eu introduzido na terra sobre a qual eu, levantando a mão, jurara dar-lha, onde quer que viam um outeiro alto e uma árvore frondosa, aí ofereciam os seus sacrifícios, apresentavam suas ofertas provocantes, punham os seus suaves aromas e derramavam as suas libações.
29 Eu lhes disse: Que alto é este, aonde vós ides? O seu nome tem sido Lugar Alto, até ao dia de hoje.
30 Portanto, dize à casa de Israel: Assim diz o Senhor Deus: Vós vos contaminais a vós mesmos, à maneira de vossos pais, e vos prostituís com as suas abominações?
31 Ao oferecerdes os vossos dons sacrificiais, como quando queimais os vossos filhos, vós vos contaminais com todos os vossos ídolos, até ao dia de hoje. Porventura, me consultaríeis, ó casa de Israel? Tão certo como eu vivo, diz o Senhor Deus, vós não me consultareis.
32 O que vos ocorre à mente de maneira nenhuma sucederá; isto que dizeis: Seremos como as nações, como as outras gerações da terra, servindo às árvores e às pedras.
33 Tão certo como eu vivo, diz o Senhor Deus, com mão poderosa, com braço estendido e derramado furor, hei de reinar sobre vós;
34 tirar-vos-ei dentre os povos e vos congregarei das terras nas quais andais espalhados, com mão forte, com braço estendido e derramado furor.
35 Levar-vos-ei ao deserto dos povos e ali entrarei em juízo convosco, face a face.
36 Como entrei em juízo com vossos pais, no deserto da terra do Egito, assim entrarei em juízo convosco, diz o Senhor Deus.
37 Far-vos-ei passar debaixo do meu cajado e vos sujeitarei à disciplina da aliança;
38 separarei dentre vós os rebeldes e os que transgrediram contra mim; da terra das suas moradas eu os farei sair, mas não entrarão na terra de Israel; e sabereis que eu sou o Senhor.
39 Quanto a vós outros, vós, ó casa de Israel, assim diz o Senhor Deus: Ide; cada um sirva aos seus ídolos, agora e mais tarde, pois que a mim não me quereis ouvir; mas não profaneis mais o meu santo nome com as vossas dádivas e com os vossos ídolos.
40 Porque no meu santo monte, no monte alto de Israel, diz o Senhor Deus, ali toda a casa de Israel me servirá, toda, naquela terra; ali me agradarei deles, ali requererei as vossas ofertas e as primícias das vossas dádivas, com todas as vossas coisas santas.
41 Agradar-me-ei de vós como de aroma suave, quando eu vos tirar dentre os povos e vos congregar das terras em que andais espalhados; e serei santificado em vós perante as nações.
42 Sabereis que eu sou o Senhor, quando eu vos der entrada na terra de Israel, na terra que, levantando a mão, jurei dar a vossos pais.
43 Ali, vos lembrareis dos vossos caminhos e de todos os vossos feitos com que vos contaminastes e tereis nojo de vós mesmos, por todas as vossas iniquidades que tendes cometido.
44 Sabereis que eu sou o Senhor, quando eu proceder para convosco por amor do meu nome, não segundo os vossos maus caminhos, nem segundo os vossos feitos corruptos, ó casa de Israel, diz o Senhor Deus.
45 Veio a mim a palavra do Senhor, dizendo:
46 Filho do homem, volve o rosto para o Sul e derrama as tuas palavras contra ele; profetiza contra o bosque do campo do Sul
47 e dize ao bosque do Sul: Ouve a palavra do Senhor: Assim diz o Senhor Deus: Eis que acenderei em ti um fogo que consumirá em ti toda árvore verde e toda árvore seca; não se apagará a chama flamejante; antes, com ela se queimarão todos os rostos, desde o Sul até ao Norte.
48 E todos os homens verão que eu, o Senhor, o acendi; não se apagará.
49 Então, disse eu: ah! Senhor Deus! Eles dizem de mim: Não é ele proferidor de parábolas?*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, volve o rosto contra Jerusalém, derrama as tuas palavras contra os santuários e profetiza contra a terra de Israel.
3 Dize à terra de Israel: Assim diz o Senhor: Eis que sou contra ti, e tirarei a minha espada da bainha, e eliminarei do meio de ti tanto o justo como o perverso.
4 Porque hei de eliminar do meio de ti o justo e o perverso, a minha espada sairá da bainha contra todo vivente, desde o Sul até ao Norte.
5 Saberão todos os homens que eu, o Senhor, tirei da bainha a minha espada; jamais voltará a ela.
6 Tu, porém, ó filho do homem, suspira; à vista deles, suspira de coração quebrantado e com amargura.
7 Quando te perguntarem: Por que suspiras tu? Então, dirás: Por causa das novas. Quando elas vêm, todo coração desmaia, todas as mãos se afrouxam, todo espírito se angustia, e todos os joelhos se desfazem em água; eis que elas vêm e se cumprirão, diz o Senhor Deus.
8 Veio a mim a palavra do Senhor, dizendo:
9 Filho do homem, profetiza e dize: Assim diz o Senhor: A espada, a espada está afiada e polida;
10 afiada para matança, polida para reluzir como relâmpago. Israel diz: Alegremo-nos! O cetro do meu filho despreza qualquer outra madeira.
11 Mas Deus responde: Deu-se a espada a polir, para ser manejada; ela está afiada e polida, para ser posta na mão do matador.
12 Grita e geme, ó filho do homem, porque ela será contra o meu povo, contra todos os príncipes de Israel. Estes, juntamente com o meu povo, estão entregues à espada; dá, pois, pancadas na tua coxa.
13 Pois haverá uma prova; e que haverá, se o próprio cetro que desprezou a todos não vier a subsistir? — diz o Senhor Deus.
14 Tu, pois, ó filho do homem, profetiza e bate com as palmas uma na outra; duplique a espada o seu golpe, triplique-o a espada da matança, da grande matança, que os rodeia;
15 para que desmaie o seu coração, e se multiplique o seu tropeçar junto a todas as portas. Faço reluzir a espada. Ah! Ela foi feita para ser raio e está afiada para matar.
16 Ó espada, vira-te, com toda a força, para a direita, vira-te para a esquerda, para onde quer que o teu rosto se dirigir.
17 Também eu baterei as minhas palmas uma na outra e desafogarei o meu furor; eu, o Senhor, é que falei.
18 Veio a mim a palavra do Senhor, dizendo:
19 Tu, pois, ó filho do homem, propõe dois caminhos por onde venha a espada do rei da Babilônia; ambos procederão da mesma terra; põe neles marcos indicadores, põe-nos na entrada do caminho para a cidade.
20 Indica o caminho para que a espada chegue à Rabá dos filhos de Amom, a Judá e a Jerusalém, a fortificada.
21 Porque o rei da Babilônia para na encruzilhada, na entrada dos dois caminhos, para consultar os oráculos: sacode as flechas, interroga os ídolos do lar, examina o fígado.
22 Caiu-lhe o oráculo para a direita, sobre Jerusalém, para dispor os aríetes, para abrir a boca com ordens de matar, para lançar gritos de guerra, para colocar os aríetes contra as portas, para levantar terraplenos, para edificar baluartes.
23 Aos judeus, lhes parecerá isto oráculo enganador, pois têm em seu favor juramentos solenes; mas Deus se lembrará da iniquidade deles, para que sejam apreendidos.
24 Portanto, assim diz o Senhor Deus: Visto que me fazeis lembrar da vossa iniquidade, descobrindo-se as vossas transgressões, aparecendo os vossos pecados em todos os vossos atos, e visto que me viestes à memória, sereis apreendidos por causa disso.
25 E tu, ó profano e perverso, príncipe de Israel, cujo dia virá no tempo do seu castigo final;
26 assim diz o Senhor Deus: Tira o diadema e remove a coroa; o que é já não será o mesmo; será exaltado o humilde e abatido o soberbo.
27 Ruína! Ruína! A ruínas a reduzirei, e ela já não será, até que venha aquele a quem ela pertence de direito; a ele a darei.
28 E tu, ó filho do homem, profetiza e dize: Assim diz o Senhor Deus acerca dos filhos de Amom e acerca dos seus insultos; dize, pois: A espada, a espada está desembainhada, polida para a matança, para consumir, para reluzir como relâmpago;
29 para ser posta no pescoço dos profanos, dos perversos, cujo dia virá no tempo do castigo final, ao passo que te pregam visões falsas e te adivinham mentiras.
30 Torna a tua espada à sua bainha. No lugar em que foste formado, na terra do teu nascimento, te julgarei.
31 Derramarei sobre ti a minha indignação, assoprarei contra ti o fogo do meu furor e te entregarei nas mãos de homens brutais, mestres de destruição.
32 Servirás de pasto ao fogo, o teu sangue será derramado no meio da terra, já não serás lembrado; pois eu, o Senhor, é que falei.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Tu, pois, ó filho do homem, acaso, julgarás, julgarás a cidade sanguinária? Faze-lhe conhecer, pois, todas as suas abominações
3 e dize: Assim diz o Senhor Deus: Ai da cidade que derrama sangue no meio de si, para que venha o seu tempo, e que faz ídolos contra si mesma, para se contaminar!
4 Pelo teu sangue, por ti mesma derramado, tu te fizeste culpada e pelos teus ídolos, por ti mesma fabricados, tu te contaminaste e fizeste chegar o dia do teu julgamento e o término de teus anos; por isso, eu te fiz objeto de opróbrio das nações e de escárnio de todas as terras.
5 As que estão perto de ti e as que estão longe escarnecerão de ti, ó infamada, cheia de inquietação.
6 Eis que os príncipes de Israel, cada um segundo o seu poder, nada mais intentam, senão derramar sangue.
7 No meio de ti, desprezam o pai e a mãe, praticam extorsões contra o estrangeiro e são injustos para com o órfão e a viúva.
8 Desprezaste as minhas coisas santas e profanaste os meus sábados.
9 Homens caluniadores se acham no meio de ti, para derramarem sangue; no meio de ti, comem carne sacrificada nos montes e cometem perversidade.
10 No teu meio, descobrem a vergonha de seu pai e abusam da mulher no prazo da sua menstruação.
11 Um comete abominação com a mulher do seu próximo, outro contamina torpemente a sua nora, e outro humilha no meio de ti a sua irmã, filha de seu pai.
12 No meio de ti, aceitam subornos para se derramar sangue; usura e lucros tomaste, extorquindo-o; exploraste o teu próximo com extorsão; mas de mim te esqueceste, diz o Senhor Deus.
13 Eis que bato as minhas palmas com furor contra a exploração que praticaste e por causa da tua culpa de sangue, que há no meio de ti. Estará firme o teu coração?
14 Estarão fortes as tuas mãos, nos dias em que eu vier a tratar contigo? Eu, o Senhor, o disse e o farei.
15 Espalhar-te-ei entre as nações, e te dispersarei em outras terras, e porei termo à tua imundícia.
16 Serás profanada em ti mesma, à vista das nações, e saberás que eu sou o Senhor.
17 Veio a mim a palavra do Senhor, dizendo:
18 Filho do homem, a casa de Israel se tornou para mim em escória; todos eles são cobre, estanho, ferro e chumbo no meio do forno; em escória de prata se tornaram.
19 Portanto, assim diz o Senhor Deus: Pois que todos vós vos tornastes em escória, eis que vos ajuntarei no meio de Jerusalém.
20 Como se ajuntam a prata, e o cobre, e o ferro, e o chumbo, e o estanho no meio do forno, para assoprar o fogo sobre eles, a fim de se fundirem, assim vos ajuntarei na minha ira e no meu furor, e ali vos deixarei, e fundirei.
21 Congregar-vos-ei e assoprarei sobre vós o fogo do meu furor; e sereis fundidos no meio de Jerusalém.
22 Como se funde a prata no meio do forno, assim sereis fundidos no meio dela; e sabereis que eu, o Senhor, derramei o meu furor sobre vós.
23 Veio a mim a palavra do Senhor, dizendo:
24 Filho do homem, dize-lhe: Tu és terra que não está purificada e que não tem chuva no dia da indignação.
25 Conspiração dos seus profetas há no meio dela; como um leão que ruge, que arrebata a presa, assim eles devoram as almas; tesouros e coisas preciosas tomam, multiplicam as suas viúvas no meio dela.
26 Os seus sacerdotes transgridem a minha lei e profanam as minhas coisas santas; entre o santo e o profano, não fazem diferença, nem discernem o imundo do limpo e dos meus sábados escondem os olhos; e, assim, sou profanado no meio deles.
27 Os seus príncipes no meio dela são como lobos que arrebatam a presa para derramarem o sangue, para destruírem as almas e ganharem lucro desonesto.
28 Os seus profetas lhes encobrem isto com cal por visões falsas, predizendo mentiras e dizendo: Assim diz o Senhor Deus, sem que o Senhor tenha falado.
29 Contra o povo da terra praticam extorsão, andam roubando, fazem violência ao aflito e ao necessitado e ao estrangeiro oprimem sem razão.
30 Busquei entre eles um homem que tapasse o muro e se colocasse na brecha perante mim, a favor desta terra, para que eu não a destruísse; mas a ninguém achei.
31 Por isso, eu derramei sobre eles a minha indignação, com o fogo do meu furor os consumi; fiz cair-lhes sobre a cabeça o castigo do seu procedimento, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, houve duas mulheres, filhas de uma só mãe.
3 Estas se prostituíram no Egito; prostituíram-se na sua mocidade; ali foram apertados os seus peitos e apalpados os seios da sua virgindade.
4 Os seus nomes eram: Oolá, a mais velha, e Oolibá, sua irmã; e foram minhas e tiveram filhos e filhas; e, quanto ao seu nome, Samaria é Oolá, e Jerusalém é Oolibá.
5 Prostituiu-se Oolá, quando era minha; inflamou-se pelos seus amantes, pelos assírios, seus vizinhos,
6 que se vestiam de azul, governadores e sátrapas, todos jovens de cobiçar, cavaleiros montados a cavalo.
7 Assim, cometeu ela as suas devassidões com eles, que eram todos a fina flor dos filhos da Assíria, e com todos aqueles pelos quais se inflamava; com todos os seus ídolos se contaminou.
8 As suas impudicícias, que trouxe do Egito, não as deixou; porque com ela se deitaram na sua mocidade, e eles apalparam os seios da sua virgindade e derramaram sobre ela a sua impudicícia.
9 Por isso, a entreguei nas mãos dos seus amantes, nas mãos dos filhos da Assíria, pelos quais se inflamara.
10 Estes descobriram as vergonhas dela, levaram seus filhos e suas filhas; porém a ela mataram à espada; e ela se tornou falada entre as mulheres, e sobre ela executaram juízos.
11 Vendo isto sua irmã Oolibá, corrompeu a sua paixão mais do que ela, e as suas devassidões foram maiores do que as de sua irmã.
12 Inflamou-se pelos filhos da Assíria, governadores e sátrapas, seus vizinhos, vestidos com primor, cavaleiros montados a cavalo, todos jovens de cobiçar.
13 Vi que se tinha contaminado; o caminho de ambas era o mesmo.
14 Aumentou as suas impudicícias, porque viu homens pintados na parede, imagens dos caldeus, pintados de vermelho:
15 de lombos cingidos e turbantes pendentes da cabeça, todos com aparência de oficiais, semelhantes aos filhos da Babilônia, na Caldeia, em terra do seu nascimento.
16 Vendo-os, inflamou-se por eles e lhes mandou mensageiros à Caldeia.
17 Então, vieram ter com ela os filhos da Babilônia, para o leito dos amores, e a contaminaram com as suas impudicícias; ela, após contaminar-se com eles, enojada, os deixou.
18 Assim, tendo ela posto a descoberto as suas devassidões e sua nudez, a minha alma se alienou dela, como já se dera com respeito à sua irmã.
19 Ela, todavia, multiplicou as suas impudicícias, lembrando-se dos dias da sua mocidade, em que se prostituíra na terra do Egito.
20 Inflamou-se pelos seus amantes, cujos membros eram como o de jumento e cujo fluxo é como o fluxo de cavalos.
21 Assim, trouxeste à memória a luxúria da tua mocidade, quando os do Egito apalpavam os teus seios, os peitos da tua mocidade.
22 Por isso, ó Oolibá, assim diz o Senhor Deus: Eis que eu suscitarei contra ti os teus amantes, os quais, enojada, tu os deixaras, e os trarei contra ti de todos os lados:
23 os filhos da Babilônia e todos os caldeus de Pecode, de Soa, de Coa e todos os filhos da Assíria com eles, jovens de cobiçar, governadores e sátrapas, príncipes e homens de renome, todos montados a cavalo.
24 Virão contra ti do Norte, com carros e carretas e com multidão de povos; pôr-se-ão contra ti em redor, com paveses, e escudos, e capacetes; e porei diante deles o juízo, e julgar-te-ão segundo os seus direitos.
25 Porei contra ti o meu zelo, e eles te tratarão com furor; cortar-te-ão o nariz e as orelhas, e o que restar cairá à espada; levarão teus filhos e tuas filhas, e quem ainda te restar será consumido pelo fogo.
26 Despojar-te-ão dos teus vestidos e tomarão as tuas joias de adorno.
27 Assim, farei cessar em ti a tua luxúria e a tua prostituição, provenientes da terra do Egito; não levantarás os olhos para eles e já não te lembrarás do Egito.
28 Porque assim diz o Senhor Deus: Eis que eu te entregarei nas mãos daqueles a quem aborreces, nas mãos daqueles que, enojada, tu deixaste.
29 Eles te tratarão com ódio, e levarão todo o fruto do teu trabalho, e te deixarão nua e despida; descobrir-se-á a vergonha da tua prostituição, a tua luxúria e as tuas devassidões.
30 Estas coisas se te farão, porque te prostituíste com os gentios e te contaminaste com os seus ídolos.
31 Andaste no caminho de tua irmã; por isso, entregarei o seu copo na tua mão.
32 Assim diz o Senhor Deus: Beberás o copo de tua irmã, fundo e largo; servirás de riso e escárnio; pois nele cabe muito.
33 Encher-te-ás de embriaguez e de dor; o copo de tua irmã Samaria é copo de espanto e de desolação.
34 Tu o beberás, e esgotá-lo-ás, e lhe roerás os cacos, e te rasgarás os peitos, pois eu o falei, diz o Senhor Deus.
35 Portanto, assim diz o Senhor Deus: Como te esqueceste de mim e me viraste as costas, também carregarás com a tua luxúria e as tuas devassidões.
36 Disse-me ainda o Senhor: Filho do homem, julgarás tu a Oolá e a Oolibá? Declara-lhes, pois, as suas abominações.
37 Porque adulteraram, e nas suas mãos há culpa de sangue; com seus ídolos adulteraram, e até os seus filhos, que me geraram, ofereceram a eles para serem consumidos pelo fogo.
38 Ainda isto me fizeram: no mesmo dia contaminaram o meu santuário e profanaram os meus sábados.
39 Pois, havendo sacrificado seus filhos aos ídolos, vieram, no mesmo dia, ao meu santuário para o profanarem; e assim o fizeram no meio da minha casa.
40 E mais ainda: mandaram vir uns homens de longe; fora-lhes enviado um mensageiro, e eis que vieram; por amor deles, te banhaste, coloriste os olhos e te ornaste de enfeites;
41 e te assentaste num suntuoso leito, diante do qual se achava mesa preparada, sobre que puseste o meu incenso e o meu óleo.
42 Com ela se ouvia a voz de muita gente que folgava; com homens de classe baixa foram trazidos do deserto uns bêbados, que puseram braceletes nas mãos delas e, na cabeça, coroas formosas.
43 Então, disse eu da envelhecida em adultérios: continuará ela em suas prostituições?
44 E passaram a estar com ela, como quem frequenta a uma prostituta; assim, passaram a frequentar a Oolá e a Oolibá, mulheres depravadas,
45 de maneira que homens justos as julgarão como se julgam as adúlteras e as sanguinárias; porque são adúlteras, e, nas suas mãos, há culpa de sangue.
46 Pois assim diz o Senhor Deus: Farei subir contra elas grande multidão e as entregarei ao tumulto e ao saque.
47 A multidão as apedrejará e as golpeará com as suas espadas; a seus filhos e suas filhas matarão e as suas casas queimarão.
48 Assim, farei cessar a luxúria da terra, para que se escarmentem todas as mulheres e não façam segundo a luxúria delas.
49 O castigo da vossa luxúria recairá sobre vós, e levareis os pecados dos vossos ídolos; e sabereis que eu sou o Senhor Deus.*
1 Veio a mim a palavra do Senhor, em o nono ano, no décimo mês, aos dez dias do mês, dizendo:
2 Filho do homem, escreve o nome deste dia, deste mesmo dia; porque o rei da Babilônia se atira contra Jerusalém neste dia.
3 Propõe uma parábola à casa rebelde e dize-lhe: Assim diz o Senhor Deus: Põe ao lume a panela, põe-na, deita-lhe água dentro,
4 ajunta nela pedaços de carne, todos os bons pedaços, as coxas e as espáduas; enche-a de ossos escolhidos.
5 Pega do melhor do rebanho e empilha lenha debaixo dela; faze-a ferver bem, e cozam-se dentro dela os ossos.
6 Portanto, assim diz o Senhor Deus: Ai da cidade sanguinária, da panela cheia de ferrugem, ferrugem que não foi tirada dela! Tira de dentro a carne, pedaço por pedaço, sem escolha.
7 Porque a culpa de sangue está no meio dela; derramou-o sobre penha descalvada e não sobre a terra, para o cobrir com o pó;
8 para fazer subir a indignação, para tomar vingança, eu pus o seu sangue numa penha descalvada, para que não fosse coberto.
9 Portanto, assim diz o Senhor Deus: Ai da cidade sanguinária! Também eu farei pilha grande.
10 Amontoa muita lenha, acende o fogo, cozinha a carne, engrossa o caldo, e ardam os ossos.
11 Então, porás a panela vazia sobre as brasas, para que ela aqueça, o seu cobre se torne candente, funda-se a sua imundícia dentro dela, e se consuma a sua ferrugem.
12 Trabalho inútil! Não sai dela a sua muita ferrugem, nem pelo fogo.
13 Na tua imundícia está a luxúria; porque eu quis purificar-te, e não te purificaste, não serás nunca purificada da tua imundícia, até que eu tenha satisfeito o meu furor contra ti.
14 Eu, o Senhor, o disse: será assim, e eu o farei; não tornarei atrás, não pouparei, nem me arrependerei; segundo os teus caminhos e segundo os teus feitos, serás julgada, diz o Senhor Deus.
15 Veio a mim a palavra do Senhor, dizendo:
16 Filho do homem, eis que, às súbitas, tirarei a delícia dos teus olhos, mas não lamentarás, nem chorarás, nem te correrão as lágrimas.
17 Geme em silêncio, não faças lamentação pelos mortos, prende o teu turbante, mete as tuas sandálias nos pés, não cubras os bigodes e não comas o pão que te mandam.
18 Falei ao povo pela manhã, e, à tarde, morreu minha mulher; na manhã seguinte, fiz segundo me havia sido mandado.
19 Então, me disse o povo: Não nos farás saber o que significam estas coisas que estás fazendo?
20 Eu lhes disse: Veio a mim a palavra do Senhor, dizendo:
21 Dize à casa de Israel: Assim diz o Senhor Deus: Eis que eu profanarei o meu santuário, objeto do vosso mais alto orgulho, delícia dos vossos olhos e anelo de vossa alma; vossos filhos e vossas filhas, que deixastes, cairão à espada.
22 Fareis como eu fiz: não cobrireis os bigodes, nem comereis o pão que vos mandam.
23 Trareis à cabeça os vossos turbantes e as vossas sandálias, nos pés; não lamentareis, nem chorareis, mas definhar-vos-eis nas vossas iniquidades e gemereis uns com os outros.
24 Assim vos servirá Ezequiel de sinal; segundo tudo o que ele fez, assim fareis. Quando isso acontecer, sabereis que eu sou o Senhor Deus.
25 Filho do homem, não sucederá que, no dia em que eu lhes tirar o objeto do seu orgulho, o seu júbilo, a sua glória, a delícia dos seus olhos e o anelo de sua alma e a seus filhos e suas filhas,
26 nesse dia, virá ter contigo algum que escapar, para te dar a notícia pessoalmente?
27 Nesse dia, abrir-se-á a tua boca para com aquele que escapar; falarás e já não ficarás mudo. Assim, lhes servirás de sinal, e saberão que eu sou o Senhor.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, volve o rosto contra os filhos de Amom e profetiza contra eles.
3 Dize aos filhos de Amom: Ouvi a palavra do Senhor Deus: Assim diz o Senhor Deus: Visto que tu disseste: Bem feito!, acerca do meu santuário, quando foi profanado; acerca da terra de Israel, quando foi assolada; e da casa de Judá, quando foi para o exílio,
4 eis que te entregarei ao poder dos filhos do Oriente, e estabelecerão em ti os seus acampamentos e porão em ti as suas moradas; eles comerão os teus frutos e beberão o teu leite.
5 Farei de Rabá uma estrebaria de camelos e dos filhos de Amom, um curral de ovelhas; e sabereis que eu sou o Senhor.
6 Porque assim diz o Senhor Deus: Visto como bateste as palmas, e pateaste, e, com toda a malícia de tua alma, te alegraste da terra de Israel,
7 eis que estendi a mão contra ti e te darei por despojo às nações; eliminar-te-ei dentre os povos e te farei perecer dentre as terras. Acabarei de todo contigo, e saberás que eu sou o Senhor.
8 Assim diz o Senhor Deus: Visto como dizem Moabe e Seir: Eis que a casa de Judá é como todas as nações,
9 eis que eu abrirei o flanco de Moabe desde as cidades, desde as suas cidades fronteiras, a glória da terra, Bete-Jesimote, Baal-Meom e Quiriataim;
10 dá-las-ei aos povos do Oriente em possessão, como também os filhos de Amom, para que destes não haja memória entre as nações.
11 Também executarei juízos contra Moabe, e os moabitas saberão que eu sou o Senhor.
12 Assim diz o Senhor Deus: Visto que Edom se houve vingativamente para com a casa de Judá e se fez culpadíssimo, quando se vingou dela,
13 assim diz o Senhor Deus: Também estenderei a mão contra Edom e eliminarei dele homens e animais; torná-lo-ei deserto, e desde Temã até Dedã cairão à espada.
14 Exercerei a minha vingança contra Edom, por intermédio do meu povo de Israel; este fará em Edom segundo a minha ira e segundo o meu furor; e os edomitas conhecerão a minha vingança, diz o Senhor Deus.
15 Assim diz o Senhor Deus: Visto que os filisteus se houveram vingativamente e com desprezo de alma executaram vingança, para destruírem com perpétua inimizade,
16 assim diz o Senhor Deus: Eis que eu estendo a mão contra os filisteus, e eliminarei os queretitas, e farei perecer o resto da costa do mar.
17 Tomarei deles grandes vinganças, com furiosas repreensões; e saberão que eu sou o Senhor, quando eu tiver exercido a minha vingança contra eles.*
1 No undécimo ano, no primeiro dia do mês, veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, visto que Tiro disse no tocante a Jerusalém: Bem feito! Está quebrada a porta dos povos; abriu-se para mim; eu me tornarei rico, agora que ela está assolada,
3 assim diz o Senhor Deus: Eis que eu estou contra ti, ó Tiro, e farei subir contra ti muitas nações, como faz o mar subir as suas ondas.
4 Elas destruirão os muros de Tiro e deitarão abaixo as suas torres; e eu varrerei o seu pó, e farei dela penha descalvada.
5 No meio do mar, virá a ser um enxugadouro de redes, porque eu o anunciei, diz o Senhor Deus; e ela servirá de despojo para as nações.
6 Suas filhas que estão no continente serão mortas à espada; e saberão que eu sou o Senhor.
7 Porque assim diz o Senhor Deus: Eis que eu trarei contra Tiro a Nabucodonosor, rei da Babilônia, desde o Norte, o rei dos reis, com cavalos, carros e cavaleiros e com a multidão de muitos povos.
8 As tuas filhas que estão no continente, ele as matará à espada; levantará baluarte contra ti; contra ti levantará terrapleno e um telhado de paveses.
9 Disporá os seus aríetes contra os teus muros e, com os seus ferros, deitará abaixo as tuas torres.
10 Pela multidão de seus cavalos, te cobrirá de pó; os teus muros tremerão com o estrondo dos cavaleiros, das carretas e dos carros, quando ele entrar pelas tuas portas, como pelas entradas de uma cidade em que se fez brecha.
11 Com as unhas dos seus cavalos, socará todas as tuas ruas; ao teu povo matará à espada, e as tuas fortes colunas cairão por terra.
12 Roubarão as tuas riquezas, saquearão as tuas mercadorias, derribarão os teus muros e arrasarão as tuas casas preciosas; as tuas pedras, as tuas madeiras e o teu pó lançarão no meio das águas.
13 Farei cessar o arruído das tuas cantigas, e já não se ouvirá o som das tuas harpas.
14 Farei de ti uma penha descalvada; virás a ser um enxugadouro de redes, jamais serás edificada, porque eu, o Senhor, o falei, diz o Senhor Deus.
15 Assim diz o Senhor Deus a Tiro: Não tremerão as terras do mar com o estrondo da tua queda, quando gemerem os traspassados, quando se fizer espantosa matança no meio de ti?
16 Todos os príncipes do mar descerão dos seus tronos, tirarão de si os seus mantos e despirão as suas vestes bordadas; de tremores se vestirão, assentar-se-ão na terra e estremecerão a cada momento; e, por tua causa, pasmarão.
17 Levantarão lamentações sobre ti e te dirão: Como pereceste, ó bem-povoada e afamada cidade, que foste forte no mar, tu e os teus moradores, que atemorizastes a todos os teus visitantes!
18 Agora, estremecerão as ilhas no dia da tua queda; as ilhas, que estão no mar, turbar-se-ão com tua saída.
19 Porque assim diz o Senhor Deus: Quando eu te fizer cidade assolada, como as cidades que não se habitam, quando eu fizer vir sobre ti as ondas do mar e as muitas águas te cobrirem,
20 então, te farei descer com os que descem à cova, ao povo antigo, e te farei habitar nas mais baixas partes da terra, em lugares desertos antigos, com os que descem à cova, para que não sejas habitada; e criarei coisas gloriosas na terra dos viventes.
21 Farei de ti um grande espanto, e já não serás; quando te buscarem, jamais serás achada, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Tu, pois, ó filho do homem, levanta lamentação sobre Tiro;
3 dize a Tiro, que habita nas entradas do mar e negocia com os povos em muitas terras do mar: Assim diz o Senhor Deus: Ó Tiro, tu dizes: Eu sou perfeita em formosura.
4 No coração dos mares, estão os teus limites; os que te edificaram aperfeiçoaram a tua formosura.
5 Fabricaram todos os teus conveses de ciprestes de Senir; trouxeram cedros do Líbano, para te fazerem mastros.
6 Fizeram os teus remos de carvalhos de Basã; os teus bancos, fizeram-nos de marfim engastado em pinho das ilhas dos quiteus.
7 De linho fino bordado do Egito era a tua vela, para servir de estandarte; azul e púrpura das ilhas de Elisá eram o teu toldo.
8 Os moradores de Sidom e de Arvade foram os teus remeiros; os teus sábios, ó Tiro, que se achavam em ti, esses foram os teus pilotos.
9 Os anciãos de Gebal e os seus sábios foram em ti os teus calafates; todos os navios do mar e os marinheiros se acharam em ti, para trocar as tuas mercadorias.
10 Os persas, os lídios e os de Pute se acharam em teu exército e eram teus homens de guerra; escudos e capacetes penduraram em ti; manifestaram a tua glória.
11 Os filhos de Arvade e o teu exército estavam sobre os teus muros em redor, e os gamaditas, nas torres; penduravam os seus escudos nos teus muros em redor; aperfeiçoavam a tua formosura.
12 Társis negociava contigo, por causa da abundância de toda sorte de riquezas; trocavam por tuas mercadorias prata, ferro, estanho e chumbo.
13 Javã, Tubal e Meseque eram os teus mercadores; em troca das tuas mercadorias, davam escravos e objetos de bronze.
14 Os da casa de Togarma, em troca das tuas mercadorias, davam cavalos, ginetes e mulos.
15 Os filhos de Dedã eram os teus mercadores; muitas terras do mar eram o mercado das tuas manufaturas; em troca, traziam dentes de marfim e madeira de ébano.
16 A Síria negociava contigo por causa da multidão das tuas manufaturas; por tuas mercadorias, eles davam esmeralda, púrpura, obras bordadas, linho fino, coral e pedras preciosas.
17 Judá e a terra de Israel eram os teus mercadores; pelas tuas mercadorias, trocavam o trigo de Minite, confeitos, mel, azeite e bálsamo.
18 Damasco negociava contigo, por causa da multidão das tuas manufaturas, por causa da abundância de toda sorte de riquezas, dando em troca vinho de Helbom e lã de Saar.
19 Também Dã e Javã, de Uzal, pelas tuas mercadorias, davam em troca ferro trabalhado, cássia e cálamo, que assim entravam no teu comércio.
20 Dedã negociava contigo com baixeiros para cavalgaduras.
21 A Arábia e todos os príncipes de Quedar eram mercadores ao teu serviço; negociavam contigo com cordeiros, carneiros e bodes; nisto, negociavam contigo.
22 Os mercadores de Sabá e Raamá eram os teus mercadores; pelas tuas mercadorias, davam em troca os mais finos aromas, pedras preciosas e ouro.
23 Harã, Cane e Éden, mercadores de Sabá, Assíria e Quilmade negociavam contigo.
24 Estes eram teus mercadores em toda sorte de mercadorias, em pano de púrpura e bordados, tapetes de várias cores e cordas trançadas e fortes.
25 Os navios de Társis eram as tuas caravanas para as tuas mercadorias; e te enriqueceste e ficaste mui famosa no coração dos mares.
26 Os teus remeiros te conduziram sobre grandes águas; o vento oriental te quebrou no coração dos mares.
27 As tuas riquezas, as tuas mercadorias, os teus bens, os teus marinheiros, os teus pilotos, os calafates, os que faziam os teus negócios e todos os teus soldados que estão em ti, juntamente com toda a multidão do povo que está no meio de ti, se afundarão no coração dos mares no dia da tua ruína.
28 Ao estrondo da gritaria dos teus pilotos, tremerão as praias.
29 Todos os que pegam no remo, os marinheiros, e todos os pilotos do mar descerão de seus navios e pararão em terra;
30 farão ouvir a sua voz sobre ti e gritarão amargamente; lançarão pó sobre a cabeça e na cinza se revolverão;
31 far-se-ão calvos por tua causa, cingir-se-ão de pano de saco e chorarão sobre ti, com amargura de alma, com amargura e lamentação.
32 Levantarão lamentações sobre ti no seu pranto, lamentarão sobre ti, dizendo: Quem foi como Tiro, como a que está reduzida ao silêncio no meio do mar?
33 Quando as tuas mercadorias eram exportadas pelos mares, fartaste a muitos povos; com a multidão da tua riqueza e do teu negócio, enriqueceste os reis da terra.
34 No tempo em que foste quebrada nos mares, nas profundezas das águas se afundaram os teus negócios e toda a tua multidão, no meio de ti.
35 Todos os moradores das terras dos mares se espantam por tua causa; os seus reis tremem sobremaneira e estão de rosto perturbado.
36 Os mercadores dentre os povos assobiam contra ti; vens a ser objeto de espanto e jamais subsistirás.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, dize ao príncipe de Tiro: Assim diz o Senhor Deus: Visto que se eleva o teu coração, e dizes: Eu sou Deus, sobre a cadeira de Deus me assento no coração dos mares, e não passas de homem e não és Deus, ainda que estimas o teu coração como se fora o coração de Deus —
3 sim, és mais sábio que Daniel, não há segredo algum que se possa esconder de ti;
4 pela tua sabedoria e pelo teu entendimento, alcançaste o teu poder e adquiriste ouro e prata nos teus tesouros;
5 pela extensão da tua sabedoria no teu comércio, aumentaste as tuas riquezas; e, por causa delas, se eleva o teu coração —,
6 assim diz o Senhor Deus: Visto que estimas o teu coração como se fora o coração de Deus,
7 eis que eu trarei sobre ti os mais terríveis estrangeiros dentre as nações, os quais desembainharão a espada contra a formosura da tua sabedoria e mancharão o teu resplendor.
8 Eles te farão descer à cova, e morrerás da morte dos traspassados no coração dos mares.
9 Dirás ainda diante daquele que te matar: Eu sou Deus? Pois não passas de homem e não és Deus, no poder do que te traspassa.
10 Da morte de incircuncisos morrerás, por intermédio de estrangeiros, porque eu o falei, diz o Senhor Deus.
11 Veio a mim a palavra do Senhor, dizendo:
12 Filho do homem, levanta uma lamentação contra o rei de Tiro e dize-lhe: Assim diz o Senhor Deus: Tu és o sinete da perfeição, cheio de sabedoria e formosura.
13 Estavas no Éden, jardim de Deus; de todas as pedras preciosas te cobrias: o sárdio, o topázio, o diamante, o berilo, o ônix, o jaspe, a safira, o carbúnculo e a esmeralda; de ouro se te fizeram os engastes e os ornamentos; no dia em que foste criado, foram eles preparados.
14 Tu eras querubim da guarda ungido, e te estabeleci; permanecias no monte santo de Deus, no brilho das pedras andavas.
15 Perfeito eras nos teus caminhos, desde o dia em que foste criado até que se achou iniquidade em ti.
16 Na multiplicação do teu comércio, se encheu o teu interior de violência, e pecaste; pelo que te lançarei, profanado, fora do monte de Deus e te farei perecer, ó querubim da guarda, em meio ao brilho das pedras.
17 Elevou-se o teu coração por causa da tua formosura, corrompeste a tua sabedoria por causa do teu resplendor; lancei-te por terra, diante dos reis te pus, para que te contemplem.
18 Pela multidão das tuas iniquidades, pela injustiça do teu comércio, profanaste os teus santuários; eu, pois, fiz sair do meio de ti um fogo, que te consumiu, e te reduzi a cinzas sobre a terra, aos olhos de todos os que te contemplam.
19 Todos os que te conhecem entre os povos estão espantados de ti; vens a ser objeto de espanto e jamais subsistirás.
20 Veio a mim a palavra do Senhor, dizendo:
21 Filho do homem, volve o rosto contra Sidom, profetiza contra ela
22 e dize: Assim diz o Senhor Deus: Eis-me contra ti, ó Sidom, e serei glorificado no meio de ti; saberão que eu sou o Senhor, quando nela executar juízos e nela me santificar.
23 Pois enviarei contra ela a peste e o sangue nas suas ruas, e os traspassados cairão no meio dela, pela espada contra ela, por todos os lados; e saberão que eu sou o Senhor.
24 Para a casa de Israel já não haverá espinho que a pique, nem abrolho que cause dor, entre todos os vizinhos que a tratam com desprezo; e saberão que eu sou o Senhor Deus.
25 Assim diz o Senhor Deus: Quando eu congregar a casa de Israel dentre os povos entre os quais estão espalhados e eu me santificar entre eles, perante as nações, então, habitarão na terra que dei a meu servo, a Jacó.
26 Habitarão nela seguros, edificarão casas e plantarão vinhas; sim, habitarão seguros, quando eu executar juízos contra todos os que os tratam com desprezo ao redor deles; e saberão que eu sou o Senhor, seu Deus.*
1 No décimo ano, no décimo mês, aos doze dias do mês, veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, volve o rosto contra Faraó, rei do Egito, e profetiza contra ele e contra todo o Egito.
3 Fala e dize: Assim diz o Senhor Deus: Eis-me contra ti, ó Faraó, rei do Egito, crocodilo enorme, que te deitas no meio dos seus rios e que dizes: O meu rio é meu, e eu o fiz para mim mesmo.
4 Mas eu porei anzóis em teus queixos e farei que os peixes dos teus rios se apeguem às tuas escamas; tirar-te-ei do meio dos teus rios, juntamente com todos os peixes dos teus rios que se apeguem às tuas escamas.
5 Lançar-te-ei para o deserto, a ti e a todo peixe dos teus rios; sobre o campo aberto cairás; não serás recolhido, nem sepultado; aos animais da terra e às aves do céu te dei por pasto.
6 E saberão todos os moradores do Egito que eu sou o Senhor, pois se tornaram um bordão de cana para a casa de Israel.
7 Tomando-te eles pela mão, tu te rachaste e lhes rasgaste o ombro; e, encostando-se eles a ti, tu te quebraste, fazendo tremer os lombos deles.
8 Por isso, assim diz o Senhor Deus: Eis que trarei sobre ti a espada e eliminarei de ti homem e animal.
9 A terra do Egito se tornará em desolação e deserto; e saberão que eu sou o Senhor.
10 Visto que disseste: O rio é meu, e eu o fiz, eis que eu estou contra ti e contra os teus rios; tornarei a terra do Egito deserta, em completa desolação, desde Migdol até Sevene, até às fronteiras da Etiópia.
11 Não passará por ela pé de homem, nem pé de animal passará por ela, nem será habitada quarenta anos,
12 porquanto tornarei a terra do Egito em desolação, no meio de terras desoladas; as suas cidades no meio das cidades desertas se tornarão em desolação por quarenta anos; espalharei os egípcios entre as nações e os derramarei pelas terras.
13 Mas assim diz o Senhor Deus: Ao cabo de quarenta anos, ajuntarei os egípcios dentre os povos para o meio dos quais foram espalhados.
14 Restaurarei a sorte dos egípcios e os farei voltar à terra de Patros, à terra de sua origem; e serão ali um reino humilde.
15 Tornar-se-á o mais humilde dos reinos e nunca mais se exaltará sobre as nações; porque os diminuirei, para que não dominem sobre as nações.
16 Já não terá a confiança da casa de Israel, confiança essa que me traria à memória a iniquidade de Israel quando se voltava a ele à procura de socorro; antes, saberão que eu sou o Senhor Deus.
17 No vigésimo sétimo ano, no mês primeiro, no primeiro dia do mês, veio a mim a palavra do Senhor, dizendo:
18 Filho do homem, Nabucodonosor, rei da Babilônia, fez que o seu exército me prestasse grande serviço contra Tiro; toda cabeça se tornou calva, e de todo ombro saiu a pele, e não houve paga de Tiro para ele, nem para o seu exército, pelo serviço que prestou contra ela.
19 Portanto, assim diz o Senhor Deus: Eis que eu darei a Nabucodonosor, rei da Babilônia, a terra do Egito; ele levará a sua multidão, e tomará o seu despojo, e roubará a sua presa, e isto será a paga para o seu exército.
20 Por paga do seu trabalho, com que serviu contra ela, lhe dei a terra do Egito, visto que trabalharam por mim, diz o Senhor Deus.
21 Naquele dia, farei brotar o poder na casa de Israel e te darei que fales livremente no meio deles; e saberão que eu sou o Senhor.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, profetiza e dize: Assim diz o Senhor Deus: Gemei: Ah! Aquele dia!
3 Porque está perto o dia, sim, está perto o Dia do Senhor, dia nublado; será o tempo dos gentios.
4 A espada virá contra o Egito, e haverá grande dor na Etiópia, quando caírem os traspassados no Egito; o seu povo será levado para o cativeiro, e serão destruídos os seus fundamentos.
5 A Etiópia, Pute e Lude e toda a Arábia, os de Cube e os outros aliados do Egito cairão juntamente com ele à espada.
6 Assim diz o Senhor: Também cairão os que sustêm o Egito, e será humilhado o orgulho do seu poder; desde Migdol até Sevene, cairão à espada, diz o Senhor Deus.
7 Serão desolados no meio das terras desertas; e as suas cidades estarão no meio das cidades devastadas.
8 Saberão que eu sou o Senhor, quando eu tiver posto fogo no Egito e se acharem destruídos todos os que lhe prestavam auxílio.
9 Naquele dia, sairão mensageiros de diante de mim em navios, para espantarem a Etiópia descuidada; e sobre ela haverá angústia, como no dia do Egito; pois eis que já vem.
10 Assim diz o Senhor Deus: Eu, pois, farei cessar a pompa do Egito, por intermédio de Nabucodonosor, rei da Babilônia.
11 Ele e o seu povo com ele, os mais terríveis das nações, serão levados para destruírem a terra; desembainharão a espada contra o Egito e encherão de traspassados a terra.
12 Secarei os rios e venderei a terra, entregando-a nas mãos dos maus; por meio de estrangeiros, farei desolada a terra e tudo o que nela houver; eu, o Senhor, é que falei.
13 Assim diz o Senhor Deus: Também destruirei os ídolos e darei cabo das imagens em Mênfis; já não haverá príncipe na terra do Egito, onde implantarei o terror.
14 Farei desolada a Patros, porei fogo em Zoã e executarei juízo em Nô.
15 Derramarei o meu furor sobre Sim, fortaleza do Egito, e exterminarei a multidão de Nô.
16 Atearei fogo no Egito; Sim terá grande angústia, Nô será destruída, e Mênfis terá adversários em pleno dia.
17 Os jovens de Áven e de Pi-Besete cairão à espada, e estas cidades cairão em cativeiro.
18 Em Tafnes, se escurecerá o dia, quando eu quebrar ali os jugos do Egito e nela cessar o orgulho do seu poder; uma nuvem a cobrirá, e suas filhas cairão em cativeiro.
19 Assim, executarei juízo no Egito, e saberão que eu sou o Senhor.
20 No undécimo ano, no mês primeiro, aos sete dias do mês, veio a mim a palavra do Senhor, dizendo:
21 Filho do homem, eu quebrei o braço de Faraó, rei do Egito, e eis que não foi atado, nem tratado com remédios, nem lhe porão ligaduras, para tornar-se forte e pegar da espada.
22 Portanto, assim diz o Senhor Deus: Eis que eu estou contra Faraó, rei do Egito; quebrar-lhe-ei os braços, tanto o forte como o que já está quebrado, e lhe farei cair da mão a espada.
23 Espalharei os egípcios entre as nações e os derramarei pelas terras.
24 Fortalecerei os braços do rei da Babilônia e lhe porei na mão a minha espada; mas quebrarei os braços de Faraó, que, diante dele, gemerá como geme o traspassado.
25 Levantarei os braços do rei da Babilônia, mas os braços de Faraó cairão; e saberão que eu sou o Senhor, quando eu puser a minha espada na mão do rei da Babilônia e ele a estender contra a terra do Egito.
26 Espalharei os egípcios entre as nações e os derramarei pelas terras; assim, saberão que eu sou o Senhor.*
1 No undécimo ano, no terceiro mês, no primeiro dia do mês, veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, dize a Faraó, rei do Egito, e à multidão do seu povo: A quem és semelhante na tua grandeza?
3 Eis que a Assíria era um cedro no Líbano, de lindos ramos, de sombrosa folhagem, de grande estatura, cujo topo estava entre os ramos espessos.
4 As águas o fizeram crescer, as fontes das profundezas da terra o exalçaram e fizeram correr as torrentes no lugar em que estava plantado, enviando ribeiros para todas as árvores do campo.
5 Por isso, se elevou a sua estatura sobre todas as árvores do campo, e se multiplicaram os seus ramos, e se alongaram as suas varas, por causa das muitas águas durante o seu crescimento.
6 Todas as aves do céu se aninhavam nos seus ramos, todos os animais do campo geravam debaixo da sua fronde, e todos os grandes povos se assentavam à sua sombra.
7 Assim, era ele formoso na sua grandeza e na extensão dos seus ramos, porque a sua raiz estava junto às muitas águas.
8 Os cedros no jardim de Deus não lhe eram rivais; os ciprestes não igualavam os seus ramos, e os plátanos não tinham renovos como os seus; nenhuma árvore no jardim de Deus se assemelhava a ele na sua formosura.
9 Formoso o fiz com a multidão dos seus ramos; todas as árvores do Éden, que estavam no jardim de Deus, tiveram inveja dele.
10 Portanto, assim diz o Senhor Deus: Como sobremaneira se elevou, e se levantou o seu topo no meio dos espessos ramos, e o seu coração se exalçou na sua altura,
11 eu o entregarei nas mãos da mais poderosa das nações, que lhe dará o tratamento segundo merece a sua perversidade; lançá-lo-ei fora.
12 Os mais terríveis estrangeiros das nações o cortaram e o deixaram; caíram os seus ramos sobre os montes e por todos os vales; os seus renovos foram quebrados por todas as correntes da terra; todos os povos da terra se retiraram da sua sombra e o deixaram.
13 Todas as aves do céu habitarão na sua ruína, e todos os animais do campo se acolherão sob os seus ramos,
14 para que todas as árvores junto às águas não se exaltem na sua estatura, nem levantem o seu topo no meio dos ramos espessos, nem as que bebem as águas venham a confiar em si, por causa da sua altura; porque todos os orgulhosos estão entregues à morte e se abismarão às profundezas da terra, no meio dos filhos dos homens, com os que descem à cova.
15 Assim diz o Senhor Deus: No dia em que ele passou para o além, fiz eu que houvesse luto; por sua causa, cobri a profundeza da terra, retive as suas correntes, e as suas muitas águas se detiveram; cobri o Líbano de preto, por causa dele, e todas as árvores do campo desfaleceram por causa dele.
16 Ao som da sua queda, fiz tremer as nações, quando o fiz passar para o além com os que descem à cova; todas as árvores do Éden, a fina flor e o melhor do Líbano, todas as que foram regadas pelas águas se consolavam nas profundezas da terra.
17 Também estas, com ele, passarão para o além, a juntar-se aos que foram traspassados à espada; sim, aos que foram seu braço e que estavam assentados à sombra no meio das nações.
18 A quem, pois, és semelhante em glória e em grandeza entre as árvores do Éden? Todavia, descerás com as árvores do Éden às profundezas da terra; no meio dos incircuncisos, jazerás com os que foram traspassados à espada; este é Faraó e toda a sua pompa, diz o Senhor Deus.*
1 No ano duodécimo, no duodécimo mês, no primeiro dia do mês, veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, levanta uma lamentação contra Faraó, rei do Egito, e dize-lhe: Foste comparado a um filho de leão entre as nações, mas não passas de um crocodilo nas águas; agitavas as águas, turvando-as com os pés, sujando os rios.
3 Assim diz o Senhor Deus: Estenderei sobre ti a minha rede no meio de muitos povos, que te puxarão para fora na minha rede.
4 Então, te deixarei em terra; no campo aberto, te lançarei e farei morar sobre ti todas as aves do céu; e se fartarão de ti os animais de toda a terra.
5 Porei as tuas carnes sobre os montes e encherei os vales da tua corpulência.
6 Com o teu sangue que se derrama, regarei a terra até aos montes, e dele se encherão as correntes.
7 Quando eu te extinguir, cobrirei os céus e farei enegrecer as suas estrelas; encobrirei o sol com uma nuvem, e a lua não resplandecerá a sua luz.
8 Por tua causa, vestirei de preto todos os brilhantes luminares do céu e trarei trevas sobre o teu país, diz o Senhor Deus.
9 Afligirei o coração de muitos povos, quando se levar às nações, às terras que não conheceste, a notícia da tua destruição.
10 Farei que muitos povos fiquem pasmados a teu respeito, e os seus reis tremam sobremaneira, quando eu brandir a minha espada ante o seu rosto; estremecerão a cada momento, cada um pela sua vida, no dia da tua queda.
11 Pois assim diz o Senhor Deus: A espada do rei da Babilônia virá contra ti.
12 Farei cair a tua multidão com as espadas dos valentes, que são todos os mais terríveis dos povos; eles destruirão a soberba do Egito, e toda a sua pompa será destruída.
13 Farei perecer todos os seus animais ao longo de muitas águas; pé de homem não as turbará, nem as turbarão unhas de animais.
14 Então, farei assentar as suas águas; e farei correr os seus rios como o azeite, diz o Senhor Deus.
15 Quando eu tornar a terra do Egito em desolação e a terra for destituída de tudo que a enchia, e quando eu ferir a todos os que nela habitam, então, saberão que eu sou o Senhor.
16 Esta é a lamentação que se fará, que farão as filhas das nações; sobre o Egito e toda sua pompa se lamentará, diz o Senhor Deus.
17 Também no ano duodécimo, aos quinze dias do primeiro mês, veio a mim a palavra do Senhor, dizendo:
18 Filho do homem, pranteia sobre a multidão do Egito, faze-a descer, a ela e as filhas das nações formosas, às profundezas da terra, juntamente com os que descem à cova.
19 A quem sobrepujas tu em beleza? Desce e deita-te com os incircuncisos.
20 No meio daqueles que foram traspassados à espada, eles cairão; à espada, ele está entregue; arrastai o Egito e a toda a sua multidão.
21 Os mais poderosos dos valentes, juntamente com os que o socorrem, lhe gritarão do além: Desceram e lá jazem eles, os incircuncisos, traspassados à espada.
22 Ali, está a Assíria com todo o seu povo; em redor dela, todos os seus sepulcros; todos eles foram traspassados e caíram à espada.
23 Os seus sepulcros foram postos nas extremidades da cova, e todo o seu povo se encontra ao redor do seu sepulcro; todos foram traspassados, e caíram à espada os que tinham causado espanto na terra dos viventes.
24 Ali, está Elão com todo o seu povo, em redor do seu sepulcro; todos eles foram traspassados e caíram à espada; eles, os incircuncisos, desceram às profundezas da terra, causaram terror na terra dos viventes e levaram a sua vergonha com os que desceram à cova.
25 No meio dos traspassados, lhe puseram um leito entre todo o seu povo; ao redor dele, estão os seus sepulcros; todos eles são incircuncisos, traspassados à espada, porque causaram terror na terra dos viventes e levaram a sua vergonha com os que desceram à cova; no meio dos traspassados, foram postos.
26 Ali, estão Meseque e Tubal com todo o seu povo; ao redor deles, estão os seus sepulcros; todos eles são incircuncisos e traspassados à espada, porquanto causaram terror na terra dos viventes.
27 E não se acharão com os valentes de outrora que, dentre os incircuncisos, caíram e desceram ao sepulcro com as suas próprias armas de guerra e com a espada debaixo da cabeça; a iniquidade deles está sobre os seus ossos, porque eram o terror dos heróis na terra dos viventes.
28 Também tu, Egito, serás quebrado no meio dos incircuncisos e jazerás com os que foram traspassados à espada.
29 Ali, está Edom, os seus reis e todos os seus príncipes, que, apesar do seu poder, foram postos com os que foram traspassados à espada; estes jazem com os incircuncisos e com os que desceram à cova.
30 Ali, estão os príncipes do Norte, todos eles, e todos os sidônios, que desceram com os traspassados, envergonhados com o terror causado pelo seu poder; e jazem incircuncisos com os que foram traspassados à espada e levam a sua vergonha com os que desceram à cova.
31 Faraó os verá e se consolará com toda a sua multidão; sim, o próprio Faraó e todo o seu exército, pelo que jazerá no meio dos traspassados à espada, diz o Senhor Deus.
32 Porque também eu pus o meu espanto na terra dos viventes; pelo que jazerá, no meio dos incircuncisos, com os traspassados à espada, Faraó e todo o seu povo, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, fala aos filhos de teu povo e dize-lhes: Quando eu fizer vir a espada sobre a terra, e o povo da terra tomar um homem dos seus limites, e o constituir por seu atalaia;
3 e, vendo ele que a espada vem sobre a terra, tocar a trombeta e avisar o povo;
4 se aquele que ouvir o som da trombeta não se der por avisado, e vier a espada e o abater, o seu sangue será sobre a sua cabeça.
5 Ele ouviu o som da trombeta e não se deu por avisado; o seu sangue será sobre ele; mas o que se dá por avisado salvará a sua vida.
6 Mas, se o atalaia vir que vem a espada e não tocar a trombeta, e não for avisado o povo; se a espada vier e abater uma vida dentre eles, este foi abatido na sua iniquidade, mas o seu sangue demandarei do atalaia.
7 A ti, pois, ó filho do homem, te constituí por atalaia sobre a casa de Israel; tu, pois, ouvirás a palavra da minha boca e lhe darás aviso da minha parte.
8 Se eu disser ao perverso: Ó perverso, certamente, morrerás; e tu não falares, para avisar o perverso do seu caminho, morrerá esse perverso na sua iniquidade, mas o seu sangue eu o demandarei de ti.
9 Mas, se falares ao perverso, para o avisar do seu caminho, para que dele se converta, e ele não se converter do seu caminho, morrerá ele na sua iniquidade, mas tu livraste a tua alma.
10 Tu, pois, filho do homem, dize à casa de Israel: Assim falais vós: Visto que as nossas prevaricações e os nossos pecados estão sobre nós, e nós desfalecemos neles, como, pois, viveremos?
11 Dize-lhes: Tão certo como eu vivo, diz o Senhor Deus, não tenho prazer na morte do perverso, mas em que o perverso se converta do seu caminho e viva. Convertei-vos, convertei-vos dos vossos maus caminhos; pois por que haveis de morrer, ó casa de Israel?
12 Tu, pois, filho do homem, dize aos filhos do teu povo: A justiça do justo não o livrará no dia da sua transgressão; quanto à perversidade do perverso, não cairá por ela, no dia em que se converter da sua perversidade; nem o justo pela justiça poderá viver no dia em que pecar.
13 Quando eu disser ao justo que, certamente, viverá, e ele, confiando na sua justiça, praticar iniquidade, não me virão à memória todas as suas justiças, mas na sua iniquidade, que pratica, ele morrerá.
14 Quando eu também disser ao perverso: Certamente, morrerás; se ele se converter do seu pecado, e fizer juízo e justiça,
15 e restituir esse perverso o penhor, e pagar o furtado, e andar nos estatutos da vida, e não praticar iniquidade, certamente, viverá; não morrerá.
16 De todos os seus pecados que cometeu não se fará memória contra ele; juízo e justiça fez; certamente, viverá.
17 Todavia, os filhos do teu povo dizem: Não é reto o caminho do Senhor; mas o próprio caminho deles é que não é reto.
18 Desviando-se o justo da sua justiça e praticando iniquidade, morrerá nela.
19 E, convertendo-se o perverso da sua perversidade e fazendo juízo e justiça, por isto mesmo viverá.
20 Todavia, vós dizeis: Não é reto o caminho do Senhor. Mas eu vos julgarei, cada um segundo os seus caminhos, ó casa de Israel.
21 No ano duodécimo do nosso exílio, aos cinco dias do décimo mês, veio a mim um que tinha escapado de Jerusalém, dizendo: Caiu a cidade.
22 Ora, a mão do Senhor estivera sobre mim pela tarde, antes que viesse o que tinha escapado; abrira-se-me a boca antes de, pela manhã, vir ter comigo o tal homem; e, uma vez aberta, já não fiquei em silêncio.
23 Então, veio a mim a palavra do Senhor, dizendo:
24 Filho do homem, os moradores destes lugares desertos da terra de Israel falam, dizendo: Abraão era um só; no entanto, possuiu esta terra; ora, sendo nós muitos, certamente, esta terra nos foi dada em possessão.
25 Dize-lhes, portanto: Assim diz o Senhor Deus: Comeis a carne com sangue, levantais os olhos para os vossos ídolos e derramais sangue; porventura, haveis de possuir a terra?
26 Vós vos estribais sobre a vossa espada, cometeis abominações, e contamina cada um a mulher do seu próximo; e possuireis a terra?
27 Assim lhes dirás: Assim diz o Senhor Deus: Tão certo como eu vivo, os que estiverem em lugares desertos cairão à espada, e o que estiver em campo aberto, o entregarei às feras, para que o devorem, e os que estiverem em fortalezas e em cavernas morrerão de peste.
28 Tornarei a terra em desolação e espanto, e será humilhado o orgulho do seu poder; os montes de Israel ficarão tão desolados, que ninguém passará por eles.
29 Então, saberão que eu sou o Senhor, quando eu tornar a terra em desolação e espanto, por todas as abominações que cometeram.
30 Quanto a ti, ó filho do homem, os filhos do teu povo falam de ti junto aos muros e nas portas das casas; fala um com o outro, cada um a seu irmão, dizendo: Vinde, peço-vos, e ouvi qual é a palavra que procede do Senhor.
31 Eles vêm a ti, como o povo costuma vir, e se assentam diante de ti como meu povo, e ouvem as tuas palavras, mas não as põem por obra; pois, com a boca, professam muito amor, mas o coração só ambiciona lucro.
32 Eis que tu és para eles como quem canta canções de amor, que tem voz suave e tange bem; porque ouvem as tuas palavras, mas não as põem por obra.
33 Mas, quando vier isto e aí vem, então, saberão que houve no meio deles um profeta.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, profetiza contra os pastores de Israel; profetiza e dize-lhes: Assim diz o Senhor Deus: Ai dos pastores de Israel que se apascentam a si mesmos! Não apascentarão os pastores as ovelhas?
3 Comeis a gordura, vestis-vos da lã e degolais o cevado; mas não apascentais as ovelhas.
4 A fraca não fortalecestes, a doente não curastes, a quebrada não ligastes, a desgarrada não tornastes a trazer e a perdida não buscastes; mas dominais sobre elas com rigor e dureza.
5 Assim, se espalharam, por não haver pastor, e se tornaram pasto para todas as feras do campo.
6 As minhas ovelhas andam desgarradas por todos os montes e por todo elevado outeiro; as minhas ovelhas andam espalhadas por toda a terra, sem haver quem as procure ou quem as busque.
7 Portanto, ó pastores, ouvi a palavra do Senhor:
8 Tão certo como eu vivo, diz o Senhor Deus, visto que as minhas ovelhas foram entregues à rapina e se tornaram pasto para todas as feras do campo, por não haver pastor, e que os meus pastores não procuram as minhas ovelhas, pois se apascentam a si mesmos e não apascentam as minhas ovelhas, —
9 portanto, ó pastores, ouvi a palavra do Senhor:
10 Assim diz o Senhor Deus: Eis que eu estou contra os pastores e deles demandarei as minhas ovelhas; porei termo no seu pastoreio, e não se apascentarão mais a si mesmos; livrarei as minhas ovelhas da sua boca, para que já não lhes sirvam de pasto.
11 Porque assim diz o Senhor Deus: Eis que eu mesmo procurarei as minhas ovelhas e as buscarei.
12 Como o pastor busca o seu rebanho, no dia em que encontra ovelhas dispersas, assim buscarei as minhas ovelhas; livrá-las-ei de todos os lugares para onde foram espalhadas no dia de nuvens e de escuridão.
13 Tirá-las-ei dos povos, e as congregarei dos diversos países, e as introduzirei na sua terra; apascentá-las-ei nos montes de Israel, junto às correntes e em todos os lugares habitados da terra.
14 Apascentá-las-ei de bons pastos, e nos altos montes de Israel será a sua pastagem; deitar-se-ão ali em boa pastagem e terão pastos bons nos montes de Israel.
15 Eu mesmo apascentarei as minhas ovelhas e as farei repousar, diz o Senhor Deus.
16 A perdida buscarei, a desgarrada tornarei a trazer, a quebrada ligarei e a enferma fortalecerei; mas a gorda e a forte destruirei; apascentá-las-ei com justiça.
17 Quanto a vós outras, ó ovelhas minhas, assim diz o Senhor Deus: Eis que julgarei entre ovelhas e ovelhas, entre carneiros e bodes.
18 Acaso, não vos basta a boa pastagem? Haveis de pisar aos pés o resto do vosso pasto? E não vos basta o terdes bebido as águas claras? Haveis de turvar o resto com os pés?
19 Quanto às minhas ovelhas, elas pastam o que haveis pisado com os pés e bebem o que haveis turvado com os pés.
20 Por isso, assim lhes diz o Senhor Deus: Eis que eu mesmo julgarei entre ovelhas gordas e ovelhas magras.
21 Visto que, com o lado e com o ombro, dais empurrões e, com os chifres, impelis as fracas até as espalhardes fora,
22 eu livrarei as minhas ovelhas, para que já não sirvam de rapina, e julgarei entre ovelhas e ovelhas.
23 Suscitarei para elas um só pastor, e ele as apascentará; o meu servo Davi é que as apascentará; ele lhes servirá de pastor.
24 Eu, o Senhor, lhes serei por Deus, e o meu servo Davi será príncipe no meio delas; eu, o Senhor, o disse.
25 Farei com elas aliança de paz e acabarei com as bestas-feras da terra; seguras habitarão no deserto e dormirão nos bosques.
26 Delas e dos lugares ao redor do meu outeiro, eu farei bênção; farei descer a chuva a seu tempo, serão chuvas de bênçãos.
27 As árvores do campo darão o seu fruto, e a terra dará a sua novidade, e estarão seguras na sua terra; e saberão que eu sou o Senhor, quando eu quebrar as varas do seu jugo e as livrar das mãos dos que as escravizavam.
28 Já não servirão de rapina aos gentios, e as feras da terra nunca mais as comerão; e habitarão seguramente, e ninguém haverá que as espante.
29 Levantar-lhes-ei plantação memorável, e nunca mais serão consumidas pela fome na terra, nem mais levarão sobre si o opróbrio dos gentios.
30 Saberão, porém, que eu, o Senhor, seu Deus, estou com elas e que elas são o meu povo, a casa de Israel, diz o Senhor Deus.
31 Vós, pois, ó ovelhas minhas, ovelhas do meu pasto; homens sois, mas eu sou o vosso Deus, diz o Senhor Deus.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, volve o rosto contra o monte Seir e profetiza contra ele.
3 Dize-lhe: Assim diz o Senhor Deus: Eis que eu estou contra ti, ó monte Seir, e estenderei a mão contra ti, e te farei desolação e espanto.
4 Farei desertas as tuas cidades, e tu serás desolado; e saberás que eu sou o Senhor.
5 Pois guardaste inimizade perpétua e abandonaste os filhos de Israel à violência da espada, no tempo da calamidade e do castigo final.
6 Por isso, diz o Senhor Deus, tão certo como eu vivo, eu te fiz sangrar, e sangue te perseguirá; visto que não aborreceste o sangue, o sangue te perseguirá.
7 Farei do monte Seir extrema desolação e eliminarei dele o que por ele passa e o que por ele volta.
8 Encherei os seus montes dos seus traspassados; nos teus outeiros, nos teus vales e em todas as tuas correntes, cairão os traspassados à espada.
9 Em perpétuas desolações, te porei, e as tuas cidades jamais serão habitadas; assim sabereis que eu sou o Senhor.
10 Visto que dizes: Os dois povos e as duas terras serão meus, e os possuirei, ainda que o Senhor se achava ali,
11 por isso, tão certo como eu vivo, diz o Senhor Deus, procederei segundo a tua ira e segundo a tua inveja, com que, no teu ódio, os trataste; e serei conhecido deles, quando te julgar.
12 Saberás que eu, o Senhor, ouvi todas as blasfêmias que proferiste contra os montes de Israel, dizendo: Já estão desolados, a nós nos são entregues por pasto.
13 Vós vos engrandecestes contra mim com a vossa boca e multiplicastes as vossas palavras contra mim; eu o ouvi.
14 Assim diz o Senhor Deus: Ao alegrar-se toda a terra, eu te reduzirei à desolação.
15 Como te alegraste com a sorte da casa de Israel, porque foi desolada, assim também farei a ti; desolado serás, ó monte Seir e todo o Edom, sim, todo; e saberão que eu sou o Senhor.*
1 Tu, ó filho do homem, profetiza aos montes de Israel e dize: Montes de Israel, ouvi a palavra do Senhor.
2 Assim diz o Senhor Deus: Visto que diz o inimigo contra vós outros: Bem feito!, e também: Os eternos lugares altos são nossa herança,
3 portanto, profetiza e dize: Assim diz o Senhor Deus: Visto que vos assolaram e procuraram abocar-vos de todos os lados, para que fôsseis possessão do resto das nações e andais em lábios paroleiros e na infâmia do povo,
4 portanto, ouvi, ó montes de Israel, a palavra do Senhor Deus: Assim diz o Senhor Deus aos montes e aos outeiros, às correntes e aos vales, aos lugares desertos e desolados e às cidades desamparadas, que se tornaram rapina e escárnio para o resto das nações circunvizinhas.
5 Portanto, assim diz o Senhor Deus: Certamente, no fogo do meu zelo, falei contra o resto das nações e contra todo o Edom. Eles se apropriaram da minha terra, com alegria de todo o coração e com menosprezo de alma, para despovoá-la e saqueá-la.
6 Portanto, profetiza sobre a terra de Israel e dize aos montes e aos outeiros, às correntes e aos vales: Assim diz o Senhor Deus: Eis que falei no meu zelo e no meu furor, porque levastes sobre vós o opróbrio das nações.
7 Portanto, assim diz o Senhor Deus: Levantando eu a mão, jurei que as nações que estão ao redor de vós levem o seu opróbrio sobre si mesmas.
8 Mas vós, ó montes de Israel, vós produzireis os vossos ramos e dareis o vosso fruto para o meu povo de Israel, o qual está prestes a vir.
9 Porque eis que eu estou convosco; voltar-me-ei para vós outros, e sereis lavrados e semeados.
10 Multiplicarei homens sobre vós, a toda a casa de Israel, sim, toda; as cidades serão habitadas, e os lugares devastados serão edificados.
11 Multiplicarei homens e animais sobre vós; eles se multiplicarão e serão fecundos; fá-los-ei habitar-vos como dantes e vos tratarei melhor do que outrora; e sabereis que eu sou o Senhor.
12 Farei andar sobre vós homens, o meu povo de Israel; eles vos possuirão, e sereis a sua herança e jamais os desfilhareis.
13 Assim diz o Senhor Deus: Visto que te dizem: Tu és terra que devora os homens e és terra que desfilha o seu povo,
14 por isso, tu não devorarás mais os homens, nem desfilharás mais o teu povo, diz o Senhor Deus.
15 Não te permitirei jamais que ouças a ignomínia dos gentios; não mais levarás sobre ti o opróbrio dos povos, nem mais farás tropeçar o teu povo, diz o Senhor Deus.
16 Veio a mim a palavra do Senhor, dizendo:
17 Filho do homem, quando os da casa de Israel habitavam na sua terra, eles a contaminaram com os seus caminhos e as suas ações; como a imundícia de uma mulher em sua menstruação, tal era o seu caminho perante mim.
18 Derramei, pois, o meu furor sobre eles, por causa do sangue que derramaram sobre a terra e por causa dos seus ídolos com que a contaminaram.
19 Espalhei-os entre as nações, e foram derramados pelas terras; segundo os seus caminhos e segundo os seus feitos, eu os julguei.
20 Em chegando às nações para onde foram, profanaram o meu santo nome, pois deles se dizia: São estes o povo do Senhor, porém tiveram de sair da terra dele.
21 Mas tive compaixão do meu santo nome, que a casa de Israel profanou entre as nações para onde foi.
22 Dize, portanto, à casa de Israel: Assim diz o Senhor Deus: Não é por amor de vós que eu faço isto, ó casa de Israel, mas pelo meu santo nome, que profanastes entre as nações para onde fostes.
23 Vindicarei a santidade do meu grande nome, que foi profanado entre as nações, o qual profanastes no meio delas; as nações saberão que eu sou o Senhor, diz o Senhor Deus, quando eu vindicar a minha santidade perante elas.
24 Tomar-vos-ei de entre as nações, e vos congregarei de todos os países, e vos trarei para a vossa terra.
25 Então, aspergirei água pura sobre vós, e ficareis purificados; de todas as vossas imundícias e de todos os vossos ídolos vos purificarei.
26 Dar-vos-ei coração novo e porei dentro de vós espírito novo; tirarei de vós o coração de pedra e vos darei coração de carne.
27 Porei dentro de vós o meu Espírito e farei que andeis nos meus estatutos, guardeis os meus juízos e os observeis.
28 Habitareis na terra que eu dei a vossos pais; vós sereis o meu povo, e eu serei o vosso Deus.
29 Livrar-vos-ei de todas as vossas imundícias; farei vir o trigo, e o multiplicarei, e não trarei fome sobre vós.
30 Multiplicarei o fruto das árvores e a novidade do campo, para que jamais recebais o opróbrio da fome entre as nações.
31 Então, vos lembrareis dos vossos maus caminhos e dos vossos feitos que não foram bons; tereis nojo de vós mesmos por causa das vossas iniquidades e das vossas abominações.
32 Não é por amor de vós, fique bem-entendido, que eu faço isto, diz o Senhor Deus. Envergonhai-vos e confundi-vos por causa dos vossos caminhos, ó casa de Israel.
33 Assim diz o Senhor Deus: No dia em que eu vos purificar de todas as vossas iniquidades, então, farei que sejam habitadas as cidades e sejam edificados os lugares desertos.
34 Lavrar-se-á a terra deserta, em vez de estar desolada aos olhos de todos os que passam.
35 Dir-se-á: Esta terra desolada ficou como o jardim do Éden; as cidades desertas, desoladas e em ruínas estão fortificadas e habitadas.
36 Então, as nações que tiverem restado ao redor de vós saberão que eu, o Senhor, reedifiquei as cidades destruídas e replantei o que estava abandonado. Eu, o Senhor, o disse e o farei.
37 Assim diz o Senhor Deus: Ainda nisto permitirei que seja eu solicitado pela casa de Israel: que lhe multiplique eu os homens como um rebanho.
38 Como um rebanho de santos, o rebanho de Jerusalém nas suas festas fixas, assim as cidades desertas se encherão de rebanhos de homens; e saberão que eu sou o Senhor.*
1 Veio sobre mim a mão do Senhor; ele me levou pelo Espírito do Senhor e me deixou no meio de um vale que estava cheio de ossos,
2 e me fez andar ao redor deles; eram mui numerosos na superfície do vale e estavam sequíssimos.
3 Então, me perguntou: Filho do homem, acaso, poderão reviver estes ossos? Respondi: Senhor Deus, tu o sabes.
4 Disse-me ele: Profetiza a estes ossos e dize-lhes: Ossos secos, ouvi a palavra do Senhor.
5 Assim diz o Senhor Deus a estes ossos: Eis que farei entrar o espírito em vós, e vivereis.
6 Porei tendões sobre vós, farei crescer carne sobre vós, sobre vós estenderei pele e porei em vós o espírito, e vivereis. E sabereis que eu sou o Senhor.
7 Então, profetizei segundo me fora ordenado; enquanto eu profetizava, houve um ruído, um barulho de ossos que batiam contra ossos e se ajuntavam, cada osso ao seu osso.
8 Olhei, e eis que havia tendões sobre eles, e cresceram as carnes, e se estendeu a pele sobre eles; mas não havia neles o espírito.
9 Então, ele me disse: Profetiza ao espírito, profetiza, ó filho do homem, e dize-lhe: Assim diz o Senhor Deus: Vem dos quatro ventos, ó espírito, e assopra sobre estes mortos, para que vivam.
10 Profetizei como ele me ordenara, e o espírito entrou neles, e viveram e se puseram em pé, um exército sobremodo numeroso.
11 Então, me disse: Filho do homem, estes ossos são toda a casa de Israel. Eis que dizem: Os nossos ossos se secaram, e pereceu a nossa esperança; estamos de todo exterminados.
12 Portanto, profetiza e dize-lhes: Assim diz o Senhor Deus: Eis que abrirei a vossa sepultura, e vos farei sair dela, ó povo meu, e vos trarei à terra de Israel.
13 Sabereis que eu sou o Senhor, quando eu abrir a vossa sepultura e vos fizer sair dela, ó povo meu.
14 Porei em vós o meu Espírito, e vivereis, e vos estabelecerei na vossa própria terra. Então, sabereis que eu, o Senhor, disse isto e o fiz, diz o Senhor.
15 Veio a mim a palavra do Senhor, dizendo:
16 Tu, pois, ó filho do homem, toma um pedaço de madeira e escreve nele: Para Judá e para os filhos de Israel, seus companheiros; depois, toma outro pedaço de madeira e escreve nele: Para José, pedaço de madeira de Efraim, e para toda a casa de Israel, seus companheiros.
17 Ajunta-os um ao outro, faze deles um só pedaço, para que se tornem apenas um na tua mão.
18 Quando te falarem os filhos do teu povo, dizendo: Não nos revelarás o que significam estas coisas?
19 Tu lhes dirás: Assim diz o Senhor Deus: Eis que tomarei o pedaço de madeira de José, que esteve na mão de Efraim, e das tribos de Israel, suas companheiras, e o ajuntarei ao pedaço de Judá, e farei deles um só pedaço, e se tornarão apenas um na minha mão.
20 Os pedaços de madeira em que houveres escrito estarão na tua mão, perante eles.
21 Dize-lhes, pois: Assim diz o Senhor Deus: Eis que eu tomarei os filhos de Israel de entre as nações para onde eles foram, e os congregarei de todas as partes, e os levarei para a sua própria terra.
22 Farei deles uma só nação na terra, nos montes de Israel, e um só rei será rei de todos eles. Nunca mais serão duas nações; nunca mais para o futuro se dividirão em dois reinos.
23 Nunca mais se contaminarão com os seus ídolos, nem com as suas abominações, nem com qualquer das suas transgressões; livrá-los-ei de todas as suas apostasias em que pecaram e os purificarei. Assim, eles serão o meu povo, e eu serei o seu Deus.
24 O meu servo Davi reinará sobre eles; todos eles terão um só pastor, andarão nos meus juízos, guardarão os meus estatutos e os observarão.
25 Habitarão na terra que dei a meu servo Jacó, na qual vossos pais habitaram; habitarão nela, eles e seus filhos e os filhos de seus filhos, para sempre; e Davi, meu servo, será seu príncipe eternamente.
26 Farei com eles aliança de paz; será aliança perpétua. Estabelecê-los-ei, e os multiplicarei, e porei o meu santuário no meio deles, para sempre.
27 O meu tabernáculo estará com eles; eu serei o seu Deus, e eles serão o meu povo.
28 As nações saberão que eu sou o Senhor que santifico a Israel, quando o meu santuário estiver para sempre no meio deles.*
1 Veio a mim a palavra do Senhor, dizendo:
2 Filho do homem, volve o rosto contra Gogue, da terra de Magogue, príncipe de Rôs, de Meseque e Tubal; profetiza contra ele
3 e dize: Assim diz o Senhor Deus: Eis que eu sou contra ti, ó Gogue, príncipe de Rôs, de Meseque e Tubal.
4 Far-te-ei que te volvas, porei anzóis no teu queixo e te levarei a ti e todo o teu exército, cavalos e cavaleiros, todos vestidos de armamento completo, grande multidão, com pavês e escudo, empunhando todos a espada;
5 persas e etíopes e Pute com eles, todos com escudo e capacete;
6 Gômer e todas as suas tropas; a casa de Togarma, do lado do Norte, e todas as suas tropas, muitos povos contigo.
7 Prepara-te, sim, dispõe-te, tu e toda a multidão do teu povo que se reuniu a ti, e serve-lhe de guarda.
8 Depois de muitos dias, serás visitado; no fim dos anos, virás à terra que se recuperou da espada, ao povo que se congregou dentre muitos povos sobre os montes de Israel, que sempre estavam desolados; este povo foi tirado de entre os povos, e todos eles habitarão seguramente.
9 Então, subirás, virás como tempestade, far-te-ás como nuvem que cobre a terra, tu, e todas as tuas tropas, e muitos povos contigo.
10 Assim diz o Senhor Deus: Naquele dia, terás imaginações no teu coração e conceberás mau desígnio;
11 e dirás: Subirei contra a terra das aldeias sem muros, virei contra os que estão em repouso, que vivem seguros, que habitam, todos, sem muros e não têm ferrolhos nem portas;
12 isso a fim de tomares o despojo, arrebatares a presa e levantares a mão contra as terras desertas que se acham habitadas e contra o povo que se congregou dentre as nações, o qual tem gado e bens e habita no meio da terra.
13 Sabá e Dedã, e os mercadores de Társis, e todos os seus governadores rapaces te dirão: Vens tu para tomar o despojo? Ajuntaste o teu bando para arrebatar a presa, para levar a prata e o ouro, para tomar o gado e as possessões, para saquear grandes despojos?
14 Portanto, ó filho do homem, profetiza e dize a Gogue: Assim diz o Senhor Deus: Acaso, naquele dia, quando o meu povo de Israel habitar seguro, não o saberás tu?
15 Virás, pois, do teu lugar, dos lados do Norte, tu e muitos povos contigo, montados todos a cavalo, grande multidão e poderoso exército;
16 e subirás contra o meu povo de Israel, como nuvem, para cobrir a terra. Nos últimos dias, hei de trazer-te contra a minha terra, para que as nações me conheçam a mim, quando eu tiver vindicado a minha santidade em ti, ó Gogue, perante elas.
17 Assim diz o Senhor Deus: Não és tu aquele de quem eu disse nos dias antigos, por intermédio dos meus servos, os profetas de Israel, os quais, então, profetizaram, durante anos, que te faria vir contra eles?
18 Naquele dia, quando vier Gogue contra a terra de Israel, diz o Senhor Deus, a minha indignação será mui grande.
19 Pois, no meu zelo, no brasume do meu furor, disse que, naquele dia, será fortemente sacudida a terra de Israel,
20 de tal sorte que os peixes do mar, e as aves do céu, e os animais do campo, e todos os répteis que se arrastam sobre a terra, e todos os homens que estão sobre a face da terra tremerão diante da minha presença; os montes serão deitados abaixo, os precipícios se desfarão, e todos os muros desabarão por terra.
21 Chamarei contra Gogue a espada em todos os meus montes, diz o Senhor Deus; a espada de cada um se voltará contra o seu próximo.
22 Contenderei com ele por meio da peste e do sangue; chuva inundante, grandes pedras de saraiva, fogo e enxofre farei cair sobre ele, sobre as suas tropas e sobre os muitos povos que estiverem com ele.
23 Assim, eu me engrandecerei, vindicarei a minha santidade e me darei a conhecer aos olhos de muitas nações; e saberão que eu sou o Senhor.*
1 Tu, pois, ó filho do homem, profetiza ainda contra Gogue e dize: Assim diz o Senhor Deus: Eis que eu sou contra ti, ó Gogue, príncipe de Rôs, de Meseque e Tubal.
2 Far-te-ei que te volvas e te conduzirei, far-te-ei subir dos lados do Norte e te trarei aos montes de Israel.
3 Tirarei o teu arco da tua mão esquerda e farei cair as tuas flechas da tua mão direita.
4 Nos montes de Israel, cairás, tu, e todas as tuas tropas, e os povos que estão contigo; a toda espécie de aves de rapina e aos animais do campo eu te darei, para que te devorem.
5 Cairás em campo aberto, porque eu falei, diz o Senhor Deus.
6 Meterei fogo em Magogue e nos que habitam seguros nas terras do mar; e saberão que eu sou o Senhor.
7 Farei conhecido o meu santo nome no meio do meu povo de Israel e nunca mais deixarei profanar o meu santo nome; e as nações saberão que eu sou o Senhor, o Santo em Israel.
8 Eis que vem e se cumprirá, diz o Senhor Deus; este é o dia de que tenho falado.
9 Os habitantes das cidades de Israel sairão e queimarão, de todo, as armas, os escudos, os paveses, os arcos, as flechas, os bastões de mão e as lanças; farão fogo com tudo isto por sete anos.
10 Não trarão lenha do campo, nem a cortarão dos bosques, mas com as armas acenderão fogo; saquearão aos que os saquearam e despojarão aos que os despojaram, diz o Senhor Deus.
11 Naquele dia, darei ali a Gogue um lugar de sepultura em Israel, o vale dos Viajantes, ao oriente do mar; espantar-se-ão os que por ele passarem. Nele, sepultarão a Gogue e a todas as suas forças e lhe chamarão o vale das Forças de Gogue.
12 Durante sete meses, estará a casa de Israel a sepultá-los, para limpar a terra.
13 Sim, todo o povo da terra os sepultará; ser-lhes-á memorável o dia em que eu for glorificado, diz o Senhor Deus.
14 Serão separados homens que, sem cessar, percorrerão a terra para sepultar os que entre os transeuntes tenham ficado nela, para a limpar; depois de sete meses, iniciarão a busca.
15 Ao percorrerem eles a terra, a qual atravessarão, em vendo algum deles o osso de algum homem, porá ao lado um sinal, até que os enterradores o sepultem no vale das Forças de Gogue.
16 Também o nome da cidade será o das Forças. Assim, limparão a terra.
17 Tu, pois, ó filho do homem, assim diz o Senhor Deus: Dize às aves de toda espécie e a todos os animais do campo: Ajuntai-vos e vinde, ajuntai-vos de toda parte para o meu sacrifício, que eu oferecerei por vós, sacrifício grande nos montes de Israel; e comereis carne e bebereis sangue.
18 Comereis a carne dos poderosos e bebereis o sangue dos príncipes da terra, dos carneiros, dos cordeiros, dos bodes e dos novilhos, todos engordados em Basã.
19 Do meu sacrifício, que oferecerei por vós, comereis a gordura até vos fartardes e bebereis o sangue até vos embriagardes.
20 À minha mesa, vós vos fartareis de cavalos e de cavaleiros, de valentes e de todos os homens de guerra, diz o Senhor Deus.
21 Manifestarei a minha glória entre as nações, e todas as nações verão o meu juízo, que eu tiver executado, e a minha mão, que sobre elas tiver descarregado.
22 Desse dia em diante, os da casa de Israel saberão que eu sou o Senhor, seu Deus.
23 Saberão as nações que os da casa de Israel, por causa da sua iniquidade, foram levados para o exílio, porque agiram perfidamente contra mim, e eu escondi deles o rosto, e os entreguei nas mãos de seus adversários, e todos eles caíram à espada.
24 Segundo a sua imundícia e as suas transgressões, assim me houve com eles e escondi deles o rosto.
25 Portanto, assim diz o Senhor Deus: Agora, tornarei a mudar a sorte de Jacó e me compadecerei de toda a casa de Israel; terei zelo pelo meu santo nome.
26 Esquecerão a sua vergonha e toda a perfídia com que se rebelaram contra mim, quando eles habitarem seguros na sua terra, sem haver quem os espante,
27 quando eu tornar a trazê-los de entre os povos, e os houver ajuntado das terras de seus inimigos, e tiver vindicado neles a minha santidade perante muitas nações.
28 Saberão que eu sou o Senhor, seu Deus, quando virem que eu os fiz ir para o cativeiro entre as nações, e os tornei a ajuntar para voltarem à sua terra, e que lá não deixarei a nenhum deles.
29 Já não esconderei deles o rosto, pois derramarei o meu Espírito sobre a casa de Israel, diz o Senhor Deus.*
1 No ano vigésimo quinto do nosso exílio, no princípio do ano, no décimo dia do mês, catorze anos após ter caído a cidade, nesse mesmo dia, veio sobre mim a mão do Senhor, e ele me levou para lá.
2 Em visões, Deus me levou à terra de Israel e me pôs sobre um monte muito alto; sobre este havia um como edifício de cidade, para o lado sul.
3 Ele me levou para lá, e eis um homem cuja aparência era como a do bronze; estava de pé na porta e tinha na mão um cordel de linho e uma cana de medir.
4 Disse-me o homem: Filho do homem, vê com os próprios olhos, ouve com os próprios ouvidos; e põe no coração tudo quanto eu te mostrar, porque para isso foste trazido para aqui; anuncia, pois, à casa de Israel tudo quanto estás vendo.
5 Vi um muro exterior que rodeava toda a casa e, na mão do homem, uma cana de medir, de seis côvados, cada um dos quais media um côvado e quatro dedos. Ele mediu a largura do edifício, uma cana; e a altura, uma cana.
6 Então, veio à porta que olhava para o oriente e subiu pelos seus degraus; mediu o limiar da porta: uma cana de largura, e o outro limiar: uma cana de largura.
7 Cada câmara tinha uma cana de comprido e uma cana de largura; o espaço entre uma e outra câmara era de cinco côvados; o limiar da porta, junto ao vestíbulo da porta interior, tinha uma cana.
8 Também mediu o vestíbulo da porta interior: uma cana.
9 Então, mediu o vestíbulo da porta, que tinha oito côvados; e os seus pilares: dois côvados; o vestíbulo olha do interior da casa para a porta.
10 A porta para o lado oriental possuía três câmaras de cada lado, cuja medida era a mesma para cada uma; também os pilares deste lado e do outro mediam o mesmo.
11 Mediu mais a largura da entrada da porta, que era de dez côvados; a profundidade da entrada: treze côvados.
12 O espaço em frente das câmaras era de um côvado, e de um côvado, o espaço do outro lado; cada câmara tinha seis côvados em quadrado.
13 Então, mediu a porta desde a extremidade do teto de uma câmara até à da outra: vinte e cinco côvados de largura; e uma porta defronte da outra.
14 Mediu a distância até aos pilares, sessenta côvados, e o átrio se estendia até aos pilares em redor da porta.
15 Desde a dianteira da porta da entrada até à dianteira do vestíbulo da porta interior, havia cinquenta côvados.
16 Havia também janelas com fasquias fixas superpostas para as câmaras e para os pilares, e da mesma sorte, para os vestíbulos; as janelas estavam à roda pela parte de dentro, e nos pilares havia palmeiras esculpidas.
17 Ele me levou ao átrio exterior; e eis que havia nele câmaras e um pavimento feito no átrio em redor; defronte deste pavimento havia trinta câmaras.
18 O pavimento ao lado das portas era a par do comprimento das portas; era o pavimento inferior.
19 Então, mediu a largura desde a dianteira da porta inferior até à dianteira do átrio interior, por fora: cem côvados do lado leste e do norte.
20 Quanto à porta que olhava para o norte, no átrio exterior, ele mediu o seu comprimento e a sua largura.
21 As suas câmaras, três de um lado e três do outro, e os seus pilares, e os seus vestíbulos eram da medida do primeiro vestíbulo; de cinquenta côvados era o seu comprimento, e a largura, de vinte e cinco côvados.
22 As suas janelas, e os seus vestíbulos, e as suas palmeiras eram da medida da porta que olhava para o oriente; subia-se para ela por sete degraus, e o seu vestíbulo estava diante dela.
23 Essa porta do átrio interior estava defronte tanto da porta do norte como da do oriente; e mediu, de porta a porta, cem côvados.
24 Então, ele me levou para o lado sul, e eis que havia ali uma porta que olhava para o sul; e mediu os seus pilares e os seus vestíbulos, que tinham as mesmas dimensões.
25 Havia também janelas em redor dos seus vestíbulos, como as outras janelas; cinquenta côvados, o comprimento do vestíbulo, e a largura, vinte e cinco côvados.
26 De sete degraus eram as suas subidas, e os seus vestíbulos estavam diante deles; e tinha palmeiras esculpidas, uma de um lado e outra do outro, nos seus pilares.
27 Também havia uma porta no átrio interior para o sul; e mediu, de porta a porta, para o sul, cem côvados.
28 Então, me levou ao átrio interior pela porta do sul; e mediu a porta do sul, que tinha as mesmas dimensões.
29 As suas câmaras, e os seus pilares, e os seus vestíbulos eram segundo estas medidas; e tinham também janelas ao redor dos seus vestíbulos; o comprimento do vestíbulo era de cinquenta côvados, e a largura, de vinte e cinco côvados.
30 Havia vestíbulos em redor; o comprimento era de vinte e cinco côvados, e a largura, de cinco côvados.
31 Os seus vestíbulos olhavam para o átrio exterior, e havia palmeiras nos seus pilares; e de oito degraus eram as suas subidas.
32 Depois, me levou ao átrio interior, para o oriente, e mediu a porta, que tinha as mesmas dimensões.
33 Também as suas câmaras, e os seus pilares, e os seus vestíbulos, segundo estas medidas; havia também janelas em redor dos seus vestíbulos; o comprimento do vestíbulo era de cinquenta côvados, e a largura, de vinte e cinco côvados.
34 Os seus vestíbulos olhavam para o átrio exterior; também havia palmeiras nos seus pilares, de um e de outro lado; e eram as suas subidas de oito degraus.
35 Então, me levou à porta do norte e a mediu; tinha as mesmas dimensões.
36 Também as suas câmaras, e os seus pilares, e os seus vestíbulos, e as suas janelas em redor; o comprimento do vestíbulo era de cinquenta côvados, e a largura, de vinte e cinco côvados.
37 Os seus pilares olhavam para o átrio exterior; também havia palmeiras nos seus pilares, de um e de outro lado; e eram as suas subidas de oito degraus.
38 A sua câmara e a sua entrada estavam junto aos pilares dos vestíbulos onde lavavam o holocausto.
39 No vestíbulo da porta havia duas mesas de um lado e duas do outro, para nelas se degolar o holocausto e a oferta pelo pecado e pela culpa.
40 Também do lado de fora da subida para a entrada da porta do norte havia duas mesas; e, no outro lado do vestíbulo da porta, havia duas mesas.
41 Quatro mesas de um lado, e quatro do outro lado; junto à porta, oito mesas, sobre as quais imolavam.
42 As quatro mesas para o holocausto eram de pedras lavradas; o comprimento era de um côvado e meio, a largura, de um côvado e meio, e a altura, de um côvado; sobre elas se punham os instrumentos com que imolavam o holocausto e os sacrifícios.
43 Os ganchos, de quatro dedos de comprimento, estavam fixados por dentro ao redor, e sobre as mesas estava a carne da oblação.
44 Fora da porta interior estavam duas câmaras dos cantores, no átrio de dentro; uma, do lado da porta do norte, e olhava para o sul; outra, do lado da porta do sul, e olhava para o norte.
45 Ele me disse: Esta câmara que olha para o sul é para os sacerdotes que têm a guarda do templo.
46 Mas a câmara que olha para o norte é para os sacerdotes que têm a guarda do altar; são estes os filhos de Zadoque, os quais, dentre os filhos de Levi, se chegam ao Senhor para o servirem.
47 Ele mediu o átrio: comprimento, cem côvados, largura, cem côvados, um quadrado; o altar estava diante do templo.
48 Então, me levou ao vestíbulo do templo e mediu cada pilar do vestíbulo, cinco côvados de um lado e cinco do outro; e a largura da porta, três côvados de um lado e três do outro.
49 O comprimento do vestíbulo era de vinte côvados, e a largura, de onze; e era por degraus que se subia. Havia colunas junto aos pilares, uma de um lado e outra do outro.*
1 Então, me levou ao templo e mediu os pilares, seis côvados de largura de um lado e seis de largura do outro, que era a largura do tabernáculo.
2 A largura da entrada: dez côvados; os lados da entrada: cinco côvados de um lado e cinco do outro; também mediu a profundidade da entrada: quarenta côvados, e a largura: vinte côvados.
3 Penetrou e mediu o pilar da entrada: dois côvados, a altura da entrada: seis côvados, e a largura da entrada: sete côvados.
4 Também mediu o seu comprimento: vinte côvados, e a largura: vinte côvados, diante do templo, e me disse: Este é o Santo dos Santos.
5 Então, mediu a parede do templo: seis côvados, e a largura de cada câmara lateral: quatro côvados, por todo o redor do templo.
6 As câmaras laterais estavam em três andares, câmara sobre câmara, trinta em cada andar; e havia reentrâncias na parede do templo ao redor, para as câmaras laterais, para que as vigas se apoiassem nelas e não fossem introduzidas na parede do templo.
7 As câmaras laterais aumentavam em largura de andar para andar, correspondendo às reentrâncias do templo de andar em andar ao redor; daí ter o templo mais largura em cima. Assim, se subia do andar inferior para o superior pelo intermediário.
8 E vi um pavimento elevado ao redor do templo; eram os fundamentos das câmaras laterais de uma cana inteira, isto é, de seis côvados de altura.
9 A grossura da parede das câmaras laterais de fora era de cinco côvados; e a área aberta entre as câmaras laterais, que estavam junto ao templo
10 e às células, tinha a largura de vinte côvados por todo o redor do templo.
11 As entradas das câmaras laterais estavam voltadas para a área aberta: uma entrada para o norte e outra para o sul; a largura da área aberta era de cinco côvados em redor.
12 O edifício que estava numa área separada, do lado ocidental, tinha a largura de setenta côvados; a parede do edifício era de cinco côvados de largura em redor, e o seu comprimento, de noventa côvados.
13 Assim, mediu o templo: cem côvados de comprimento, como também a área separada, o edifício e as suas paredes: cem côvados de comprimento.
14 A largura da frente oriental do templo e da área separada, de uma e de outra parte: cem côvados.
15 Também mediu o comprimento do edifício, que estava na área separada e por detrás do templo, e as suas galerias de uma e de outra parte: cem côvados. O templo propriamente dito, o Santíssimo e o vestíbulo do átrio eram apainelados.
16 As janelas, de fasquias fixas superpostas, estavam ao redor dos três lugares. Dentro, as paredes estavam cobertas de madeira em redor, e isto desde o chão até às janelas, que estavam cobertas.
17 No espaço em cima da porta, e até ao templo de dentro e de fora, e em toda a parede em redor, por dentro e por fora, havia obras de escultura,
18 querubins e palmeiras, de sorte que cada palmeira estava entre querubim e querubim, e cada querubim tinha dois rostos,
19 a saber, um rosto de homem olhava para a palmeira de um lado, e um rosto de leãozinho, para a palmeira do outro lado; assim se fez pela casa toda ao redor.
20 Desde o chão até acima da entrada estavam feitos os querubins e as palmeiras, como também pela parede do templo.
21 As ombreiras do templo eram quadradas, e, no tocante à entrada do Santo dos Santos, era esta da mesma aparência.
22 O altar de madeira era de três côvados de altura, e o seu comprimento, de dois côvados; os seus cantos, a sua base e as suas paredes eram de madeira; e o homem me disse: Esta é a mesa que está perante o Senhor.
23 O templo e o Santíssimo, ambos tinham duas portas.
24 Havia duas folhas para as portas, duas folhas dobráveis; duas para cada porta.
25 Nelas, isto é, nas portas do templo, foram feitos querubins e palmeiras, como estavam feitos nas paredes, e havia um baldaquino de madeira na frontaria do vestíbulo por fora.
26 E havia janelas de fasquias fixas superpostas e palmeiras, em ambos os lados do vestíbulo, como também nas câmaras laterais do templo e no baldaquino.*
1 Depois disto, me fez sair para o átrio exterior, para o norte; e me levou às celas que estavam para o norte, opostas ao edifício na área separada, edifício que olha para o norte,
2 do comprimento de cem côvados, com portas que davam para o norte; e a largura era de cinquenta côvados.
3 Em frente dos vinte côvados que pertenciam ao átrio interior, defronte do pavimento que pertencia ao átrio exterior, havia galeria contra galeria em três andares.
4 Diante das câmaras havia um passeio de dez côvados de largura, do lado de dentro, e cem de comprimento; e as suas entradas eram para o lado norte.
5 As câmaras superiores eram mais estreitas; porque as galerias tiravam mais espaço destas do que das de baixo e das do meio do edifício.
6 Porque elas eram de três andares e não tinham colunas como as colunas dos átrios; por isso, as superiores eram mais estreitas do que as de baixo e as do meio.
7 O muro que estava por fora, defronte das câmaras, no caminho do átrio exterior, diante das câmaras, tinha cinquenta côvados de comprimento.
8 Pois o comprimento das câmaras, que estavam no átrio exterior, era de cinquenta côvados; e eis que defronte do templo havia cem côvados.
9 Da parte de baixo destas câmaras, estava a entrada do lado do oriente, quando se entra nelas pelo átrio exterior.
10 Do muro do átrio para o oriente, diante do edifício na área separada, havia também celas
11 e um passeio; tinham a feição das celas que olhavam para o norte, e o mesmo comprimento, e a mesma largura, e ainda as mesmas saídas, e o mesmo arranjo; como eram as suas entradas,
12 assim eram as das celas que olhavam para o sul, no princípio do caminho, a saber, o caminho bem defronte do muro para o oriente, para quem por elas entra.
13 Então, o homem me disse: As câmaras do norte e as câmaras do sul, que estão diante da área separada, são câmaras santas, em que os sacerdotes, que se chegam ao Senhor, comerão e onde depositarão as coisas santíssimas, isto é, as ofertas de manjares e as pelo pecado e pela culpa; porque o lugar é santo.
14 Quando os sacerdotes entrarem, não sairão do santuário para o átrio exterior, mas porão ali as vestiduras com que ministraram, porque elas são santas; usarão outras vestiduras e assim se aproximarão do lugar destinado ao povo.
15 Acabando ele de medir o templo interior, ele me fez sair pela porta que olha para o oriente; e mediu em redor.
16 Mediu o lado oriental com a cana de medir: quinhentas canas ao redor.
17 Mediu o lado norte: quinhentas canas ao redor.
18 Mediu também o lado sul: quinhentas canas.
19 Voltou-se para o lado ocidental e mediu quinhentas canas.
20 Mediu pelos quatro lados; havia um muro em redor, de quinhentas canas de comprimento e quinhentas de largura, para fazer separação entre o santo e o profano.*
1 Então, o homem me levou à porta, à porta que olha para o oriente.
2 E eis que, do caminho do oriente, vinha a glória do Deus de Israel; a sua voz era como o ruído de muitas águas, e a terra resplandeceu por causa da sua glória.
3 O aspecto da visão que tive era como o da visão que eu tivera, quando vim destruir a cidade; e eram as visões como a que tive junto ao rio Quebar; e me prostrei, rosto em terra.
4 A glória do Senhor entrou no templo pela porta que olha para o oriente.
5 O Espírito me levantou e me levou ao átrio interior; e eis que a glória do Senhor enchia o templo.
6 Então, ouvi uma voz que me foi dirigida do interior do templo, e o homem se pôs de pé junto a mim, e o Senhor me disse:
7 Filho do homem, este é o lugar do meu trono, e o lugar das plantas dos meus pés, onde habitarei no meio dos filhos de Israel para sempre; os da casa de Israel não contaminarão mais o meu nome santo, nem eles nem os seus reis, com as suas prostituições e com o cadáver dos seus reis, nos seus monumentos,
8 pondo o seu limiar junto ao meu limiar e a sua ombreira, junto à minha ombreira, e havendo uma parede entre mim e eles. Contaminaram o meu santo nome com as suas abominações que faziam; por isso, eu os consumi na minha ira.
9 Agora, lancem eles para longe de mim a sua prostituição e o cadáver dos seus reis, e habitarei no meio deles para sempre.
10 Tu, pois, ó filho do homem, mostra à casa de Israel este templo, para que ela se envergonhe das suas iniquidades; e meça o modelo.
11 Envergonhando-se eles de tudo quanto praticaram, faze-lhes saber a planta desta casa e o seu arranjo, as suas saídas, as suas entradas e todas as suas formas; todos os seus estatutos, todos os seus dispositivos e todas as suas leis; escreve isto na sua presença para que observem todas as suas instituições e todos os seus estatutos e os cumpram.
12 Esta é a lei do templo; sobre o cimo do monte, todo o seu limite ao redor será santíssimo; eis que esta é a lei do templo.
13 São estas as medidas do altar, em côvados, sendo o côvado de côvado comum e quatro dedos; a base será de um côvado de altura e um côvado de largura, e a sua borda, em todo o seu contorno, de quatro dedos; esta é a base do altar.
14 Da base, na linha da terra, até à fiada do fundo, dois côvados, e de largura, um côvado; da fiada pequena até à fiada grande, quatro côvados, e a largura, um côvado.
15 A lareira, de quatro côvados de altura; da lareira para cima se projetarão quatro chifres.
16 A lareira terá doze côvados de comprimento e doze de largura, quadrada nos quatro lados.
17 A fiada terá catorze côvados de comprimento e catorze de largura, nos seus quatro lados; a borda ao redor dela, de meio côvado; e a base ao redor do altar se projetará um côvado; os seus degraus olharão para o oriente.
18 E o Senhor me disse: Filho do homem, assim diz o Senhor Deus: São estas as determinações do altar, no dia em que o farão, para oferecerem sobre ele holocausto e para sobre ele aspergirem sangue.
19 Aos sacerdotes levitas, que são da descendência de Zadoque, que se chegam a mim, diz o Senhor Deus, para me servirem, darás um novilho para oferta pelo pecado.
20 Tomarás do seu sangue e o porás sobre os quatro chifres do altar, e nos quatro cantos da fiada, e na borda ao redor; assim, farás a purificação e a expiação.
21 Então, tomarás o novilho da oferta pelo pecado, o qual será queimado no lugar da casa para isso designado, fora do santuário.
22 No segundo dia, oferecerás um bode sem defeito, oferta pelo pecado; e purificarão o altar, como o purificaram com o novilho.
23 Acabando tu de o purificar, oferecerás um novilho sem defeito e, do rebanho, um carneiro sem defeito.
24 Oferecê-los-ás perante o Senhor; os sacerdotes deitarão sal sobre eles e os oferecerão em holocausto ao Senhor.
25 Durante sete dias, prepararás cada dia um bode para oferta pelo pecado; também prepararão um novilho e, do rebanho, um carneiro sem defeito.
26 Por sete dias, expiarão o altar e o purificarão; e, assim, o consagrarão.
27 Tendo eles cumprido estes dias, será que, ao oitavo dia, dali em diante, prepararão os sacerdotes sobre o altar os vossos holocaustos e as vossas ofertas pacíficas; e eu vos serei propício, diz o Senhor Deus.*
1 Então, o homem me fez voltar para o caminho da porta exterior do santuário, que olha para o oriente, a qual estava fechada.
2 Disse-me o Senhor: Esta porta permanecerá fechada, não se abrirá; ninguém entrará por ela, porque o Senhor, Deus de Israel, entrou por ela; por isso, permanecerá fechada.
3 Quanto ao príncipe, ele se assentará ali por ser príncipe, para comer o pão diante do Senhor; pelo vestíbulo da porta entrará e por aí mesmo sairá.
4 Depois, o homem me levou pela porta do norte, diante da casa; olhei, e eis que a glória do Senhor enchia a Casa do Senhor; então, caí rosto em terra.
5 Disse-me o Senhor: Filho do homem, nota bem, e vê com os próprios olhos, e ouve com os próprios ouvidos tudo quanto eu te disser de todas as determinações a respeito da Casa do Senhor e de todas as leis dela; nota bem quem pode entrar no templo e quem deve ser excluído do santuário.
6 Dize aos rebeldes, à casa de Israel: Assim diz o Senhor Deus: Bastem-vos todas as vossas abominações, ó casa de Israel!
7 Porquanto introduzistes estrangeiros, incircuncisos de coração e incircuncisos de carne, para estarem no meu santuário, para o profanarem em minha casa, quando ofereceis o meu pão, a gordura e o sangue; violastes a minha aliança com todas as vossas abominações.
8 Não cumpristes as prescrições a respeito das minhas coisas sagradas; antes, constituístes em vosso lugar estrangeiros para executarem o serviço no meu santuário.
9 Assim diz o Senhor Deus: Nenhum estrangeiro que se encontra no meio dos filhos de Israel, incircunciso de coração ou incircunciso de carne, entrará no meu santuário.
10 Os levitas, porém, que se apartaram para longe de mim, quando Israel andava errado, que andavam transviados, desviados de mim, para irem atrás dos seus ídolos, bem levarão sobre si a sua iniquidade.
11 Contudo, eles servirão no meu santuário como guardas nas portas do templo e ministros dele; eles imolarão o holocausto e o sacrifício para o povo e estarão perante este para lhe servir.
12 Porque lhe ministraram diante dos seus ídolos e serviram à casa de Israel de tropeço de maldade; por isso, levantando a mão, jurei a respeito deles, diz o Senhor Deus, que eles levarão sobre si a sua iniquidade.
13 Não se chegarão a mim, para me servirem no sacerdócio, nem se chegarão a nenhuma de todas as minhas coisas sagradas, que são santíssimas, mas levarão sobre si a sua vergonha e as suas abominações que cometeram.
14 Contudo, eu os encarregarei da guarda do templo, e de todo o serviço, e de tudo o que se fizer nele.
15 Mas os sacerdotes levitas, os filhos de Zadoque, que cumpriram as prescrições do meu santuário, quando os filhos de Israel se extraviaram de mim, eles se chegarão a mim, para me servirem, e estarão diante de mim, para me oferecerem a gordura e o sangue, diz o Senhor Deus.
16 Eles entrarão no meu santuário, e se chegarão à minha mesa, para me servirem, e cumprirão as minhas prescrições.
17 E será que, quando entrarem pelas portas do átrio interior, usarão vestes de linho; não se porá lã sobre eles, quando servirem nas portas do átrio interior, dentro do templo.
18 Tiaras de linho lhes estarão sobre a cabeça, e calções de linho sobre as coxas; não se cingirão a ponto de lhes vir suor.
19 Saindo eles ao átrio exterior, ao povo, despirão as vestes com que ministraram, pô-las-ão nas santas câmaras e usarão outras vestes, para que, com as suas vestes, não santifiquem o povo.
20 Não raparão a cabeça, nem deixarão crescer o cabelo; antes, como convém, tosquiarão a cabeça.
21 Nenhum sacerdote beberá vinho quando entrar no átrio interior.
22 Não se casarão nem com viúva nem com repudiada, mas tomarão virgens da linhagem da casa de Israel ou viúva que o for de sacerdote.
23 A meu povo ensinarão a distinguir entre o santo e o profano e o farão discernir entre o imundo e o limpo.
24 Quando houver contenda, eles assistirão a ela para a julgarem; pelo meu direito julgarão; as minhas leis e os meus estatutos em todas as festas fixas guardarão e santificarão os meus sábados.
25 Não se aproximarão de nenhuma pessoa morta, porque se contaminariam; somente por pai, ou mãe, ou filho, ou filha, ou irmão, ou por irmã que não tiver marido, se poderão contaminar.
26 Depois de ser ele purificado, contar-se-lhe-ão sete dias.
27 No dia em que ele entrar no lugar santo, no átrio interior, para ministrar no lugar santo, apresentará a sua oferta pelo pecado, diz o Senhor Deus.
28 Os sacerdotes terão uma herança; eu sou a sua herança. Não lhes dareis possessão em Israel; eu sou a sua possessão.
29 A oferta de manjares, e a oferta pelo pecado, e a pela culpa eles comerão; e toda coisa consagrada em Israel será deles.
30 O melhor de todos os primeiros frutos de toda espécie e toda oferta serão dos sacerdotes; também as primeiras das vossas massas dareis ao sacerdote, para que faça repousar a bênção sobre a vossa casa.
31 Não comerão os sacerdotes coisa alguma que de si mesma haja morrido ou tenha sido dilacerada de aves e de animais.*
1 Quando, pois, repartirdes a terra por sortes em herança, fareis uma oferta ao Senhor, uma porção santa da terra; o comprimento desta porção será de vinte e cinco mil côvados, e a largura, de dez mil; ela será santa em toda a sua extensão ao redor.
2 Será o santuário de quinhentos côvados com mais quinhentos, em quadrado, e terá em redor uma área aberta de cinquenta côvados.
3 Desta porção santa medirás vinte e cinco mil côvados de comprimento e dez mil de largura; ali estará o santuário, o lugar santíssimo.
4 Este será o lugar santo da terra; ele será para os sacerdotes, ministros do santuário, que dele se aproximam para servir ao Senhor, e lhes servirá de lugar para casas; e, como lugar santo, pertencerá ao santuário.
5 Os levitas, ministros da casa, terão vinte e cinco mil côvados de comprimento e dez mil de largura, para possessão sua, para vinte câmaras.
6 Para a possessão da cidade, de largura dareis cinco mil côvados e vinte e cinco mil de comprimento defronte da porção santa, o que será para toda a casa de Israel.
7 O príncipe, porém, terá a sua parte deste e do outro lado da santa porção e da possessão da cidade, diante da santa porção e diante da possessão da cidade, ao lado ocidental e oriental; e o comprimento corresponderá a uma das porções, desde o limite ocidental até ao limite oriental.
8 Esta terra será a sua possessão em Israel; os meus príncipes nunca mais oprimirão o meu povo; antes, distribuirão a terra à casa de Israel, segundo as suas tribos.
9 Assim diz o Senhor Deus: Basta, ó príncipes de Israel; afastai a violência e a opressão e praticai juízo e justiça: tirai as vossas desapropriações do meu povo, diz o Senhor Deus.
10 Tereis balanças justas, efa justo e bato justo.
11 O efa e o bato serão da mesma capacidade, de maneira que o bato contenha a décima parte do ômer, e o efa, a décima parte do ômer; segundo o ômer, será a sua medida.
12 O siclo será de vinte geras. Vinte siclos, mais vinte e cinco siclos, mais quinze siclos serão iguais a uma mina para vós.
13 Esta será a oferta que haveis de fazer: de trigo, a sexta parte de um efa de cada ômer, e também de cevada, a sexta parte de um efa de cada ômer.
14 A porção determinada de azeite será a décima parte de um bato de cada coro; um coro, como o ômer, tem dez batos.
15 De cada rebanho de duzentas cabeças, um cordeiro tirado dos pastos ricos de Israel; tudo para oferta de manjares, e para holocausto, e para sacrifício pacífico; para que façam expiação pelo povo, diz o Senhor Deus.
16 Todo o povo da terra fará contribuição, para esta oferta, ao príncipe em Israel.
17 Estarão a cargo do príncipe os holocaustos, e as ofertas de manjares, e as libações, nas Festas da Lua Nova e nos sábados, em todas as festas fixas da casa de Israel; ele mesmo proverá a oferta pelo pecado, e a oferta de manjares, e o holocausto, e os sacrifícios pacíficos, para fazer expiação pela casa de Israel.
18 Assim diz o Senhor Deus: No primeiro mês, no primeiro dia do mês, tomarás um novilho sem defeito e purificarás o santuário.
19 O sacerdote tomará do sangue e porá dele nas ombreiras da casa, e nos quatro cantos da fiada do altar, e nas ombreiras da porta do átrio interior.
20 Assim também farás no sétimo dia do mês, por causa dos que pecam por ignorância e por causa dos símplices; assim, expiareis o templo.
21 No primeiro mês, no dia catorze do mês, tereis a Páscoa, festa de sete dias; pão asmo se comerá.
22 O príncipe, no mesmo dia, por si e por todo o povo da terra, proverá um novilho para oferta pelo pecado.
23 Nos sete dias da festa, preparará ele um holocausto ao Senhor, sete novilhos e sete carneiros sem defeito, cada dia durante os sete dias; e um bode cada dia como oferta pelo pecado.
24 Também preparará uma oferta de manjares: para cada novilho, um efa, e um efa para cada carneiro, e um him de azeite para cada efa.
25 No dia quinze do sétimo mês e durante os sete dias da festa, fará o mesmo: a mesma oferta pelo pecado, o mesmo holocausto, a mesma oferta e a mesma porção de azeite.*
1 Assim diz o Senhor Deus: A porta do átrio interior, que olha para o oriente, estará fechada durante os seis dias que são de trabalho; mas no sábado ela se abrirá e também no dia da Festa da Lua Nova.
2 O príncipe entrará de fora pelo vestíbulo da porta e permanecerá junto da ombreira da porta; os sacerdotes prepararão o holocausto dele e os seus sacrifícios pacíficos, e ele adorará no limiar da porta e sairá; mas a porta não se fechará até à tarde.
3 O povo da terra adorará na entrada da mesma porta, nos sábados e nas Festas da Lua Nova, diante do Senhor.
4 O holocausto que o príncipe oferecer ao Senhor serão, no dia de sábado, seis cordeiros sem defeito e um carneiro sem defeito.
5 A oferta de manjares será um efa para cada carneiro; para cada cordeiro, a oferta de manjares será o que puder dar; e de azeite, um him para cada efa.
6 Mas, no dia da Festa da Lua Nova, será um novilho sem defeito e seis cordeiros e um carneiro; eles serão sem defeito.
7 Preparará por oferta de manjares um efa para cada novilho e um efa para cada carneiro, mas, pelos cordeiros, segundo puder; e um him de azeite para cada efa.
8 Quando entrar o príncipe, entrará pelo vestíbulo da porta e sairá pelo mesmo caminho.
9 Mas, quando vier o povo da terra perante o Senhor, nas festas fixas, aquele que entrar pela porta do norte, para adorar, sairá pela porta do sul; e aquele que entrar pela porta do sul sairá pela porta do norte; não tornará pela porta por onde entrou, mas sairá pela porta oposta.
10 O príncipe entrará no meio deles, quando eles entrarem; em saindo eles, ele sairá.
11 Nas solenidades e nas festas fixas, a oferta de manjares será um efa para cada novilho e um para cada carneiro; mas, pelos cordeiros, o que puder dar; e de azeite, um him para cada efa.
12 Quando o príncipe preparar holocausto ou sacrifícios pacíficos como oferta voluntária ao Senhor, então, lhe abrirão a porta que olha para o oriente, e fará ele o seu holocausto e os seus sacrifícios pacíficos, como costuma fazer no dia de sábado; e sairá, e se fechará a porta depois de ele sair.
13 Prepararás um cordeiro de um ano, sem defeito, em holocausto ao Senhor, cada dia; manhã após manhã, o prepararás.
14 Juntamente com ele, prepararás, manhã após manhã, uma oferta de manjares para o Senhor, a sexta parte de um efa e, de azeite, a terça parte de um him, para misturar com a flor de farinha. Isto é estatuto perpétuo e contínuo.
15 Assim prepararão o cordeiro, e a oferta de manjares, e o azeite, manhã após manhã, em holocausto contínuo.
16 Assim diz o Senhor Deus: Quando o príncipe der um presente de sua herança a alguns de seus filhos, pertencerá a estes; será possessão deles por herança.
17 Mas, dando ele um presente da sua herança a algum dos seus servos, será deste até ao ano da liberdade; então, tornará para o príncipe, porque a seus filhos, somente a eles, pertencerá a herança.
18 O príncipe não tomará nada da herança do povo, não os esbulhará da sua possessão; da sua própria possessão deixará herança a seus filhos, para que o meu povo não seja retirado, cada um da sua possessão.
19 Depois disto, o homem me trouxe, pela entrada que estava ao lado da porta, às câmaras santas dos sacerdotes, as quais olhavam para o norte; e eis que ali havia um lugar nos fundos extremos que olham para o ocidente.
20 Ele me disse: Este é o lugar onde os sacerdotes cozerão a oferta pela culpa e a oferta pelo pecado e onde cozerão a oferta de manjares, para que não a tragam ao átrio exterior e assim santifiquem o povo.
21 Então, me levou para fora, para o átrio exterior, e me fez passar aos quatro cantos do átrio; e eis que em cada canto do átrio havia outro átrio.
22 Nos quatro cantos do átrio havia átrios pequenos, menores, de quarenta côvados de comprimento e trinta de largura; estes quatro cantos tinham a mesma dimensão.
23 Havia um muro ao redor dos átrios, ao redor dos quatro, e havia lugares para cozer ao pé dos muros ao redor.
24 E me disse: São estas as cozinhas, onde os ministros do templo cozerão o sacrifício do povo.*
1 Depois disto, o homem me fez voltar à entrada do templo, e eis que saíam águas de debaixo do limiar do templo, para o oriente; porque a face da casa dava para o oriente, e as águas vinham de baixo, do lado direito da casa, do lado sul do altar.
2 Ele me levou pela porta do norte e me fez dar uma volta por fora, até à porta exterior, que olha para o oriente; e eis que corriam as águas ao lado direito.
3 Saiu aquele homem para o oriente, tendo na mão um cordel de medir; mediu mil côvados e me fez passar pelas águas, águas que me davam pelos tornozelos.
4 Mediu mais mil e me fez passar pelas águas, águas que me davam pelos joelhos; mediu mais mil e me fez passar pelas águas, águas que me davam pelos lombos.
5 Mediu ainda outros mil, e era já um rio que eu não podia atravessar, porque as águas tinham crescido, águas que se deviam passar a nado, rio pelo qual não se podia passar.
6 E me disse: Viste isto, filho do homem? Então, me levou e me tornou a trazer à margem do rio.
7 Tendo eu voltado, eis que à margem do rio havia grande abundância de árvores, de um e de outro lado.
8 Então, me disse: Estas águas saem para a região oriental, e descem à campina, e entram no mar Morto, cujas águas ficarão saudáveis.
9 Toda criatura vivente que vive em enxames viverá por onde quer que passe este rio, e haverá muitíssimo peixe, e, aonde chegarem estas águas, tornarão saudáveis as do mar, e tudo viverá por onde quer que passe este rio.
10 Junto a ele se acharão pescadores; desde En-Gedi até En-Eglaim haverá lugar para se estenderem redes; o seu peixe, segundo as suas espécies, será como o peixe do mar Grande, em multidão excessiva.
11 Mas os seus charcos e os seus pântanos não serão feitos saudáveis; serão deixados para o sal.
12 Junto ao rio, às ribanceiras, de um e de outro lado, nascerá toda sorte de árvore que dá fruto para se comer; não fenecerá a sua folha, nem faltará o seu fruto; nos seus meses, produzirá novos frutos, porque as suas águas saem do santuário; o seu fruto servirá de alimento, e a sua folha, de remédio.
13 Assim diz o Senhor Deus: Este será o limite pelo qual repartireis a terra em herança, segundo as doze tribos de Israel. José terá duas partes.
14 Vós a repartireis em heranças iguais, tanto para um como para outro; pois jurei, levantando a mão, dá-la a vossos pais; assim, que esta mesma terra vos cairá a vós outros em herança.
15 Este será o limite da terra: do lado norte, desde o mar Grande, caminho de Hetlom, até à entrada de Zedade,
16 Hamate, Berota, Sibraim (que estão entre o limite de Damasco e o de Hamate), a cidade Hazer-Haticom (que está junto ao limite de Haurã).
17 Assim, o limite será desde o mar até Hazar-Enom, o limite de Damasco, e, na direção do norte, está o limite de Hamate; este será o lado do Norte.
18 O lado do oriente, entre Haurã, e Damasco, e Gileade, e a terra de Israel, será o Jordão; desde o limite do norte até ao mar do oriente, medireis; este será o lado do oriente.
19 O lado do sul será desde Tamar até às águas de Meribá-Cades, junto ao ribeiro do Egito até ao mar Grande; este será o lado do sul.
20 O lado do ocidente será o mar Grande, desde o limite do sul até à entrada de Hamate; este será o lado do ocidente.
21 Repartireis, pois, esta terra entre vós, segundo as tribos de Israel.
22 Será, porém, que a sorteareis para vossa herança e para a dos estrangeiros que moram no meio de vós, que gerarem filhos no meio de vós; e vos serão como naturais entre os filhos de Israel; convosco entrarão em herança, no meio das tribos de Israel.
23 E será que, na tribo em que morar o estrangeiro, ali lhe dareis a sua herança, diz o Senhor Deus.*
1 São estes os nomes das tribos: desde a parte extrema do norte, via Hetlom, até à entrada de Hamate, até Hazar-Enom, o limite norte de Damasco até junto de Hamate e desde o lado oriental até ao ocidente, Dã terá uma porção.
2 Limitando-se com Dã, desde o lado oriental até ao ocidental, Aser, uma porção.
3 Limitando-se com Aser, desde o lado oriental até ao ocidental, Naftali, uma porção.
4 Limitando-se com Naftali, desde o lado oriental até ao ocidental, Manassés, uma porção.
5 Limitando-se com Manassés, desde o lado oriental até ao ocidental, Efraim, uma porção.
6 Limitando-se com Efraim, desde o lado oriental até ao ocidental, Rúben, uma porção.
7 Limitando-se com Rúben, desde o lado oriental até ao ocidental, Judá, uma porção.
8 Limitando-se com Judá, desde o lado oriental até ao ocidental, será a região sagrada que haveis de separar, de vinte e cinco mil côvados de largura e de comprimento, o mesmo que o das porções, desde o lado oriental até ao ocidental; o santuário estará no meio dela.
9 A região que haveis de separar ao Senhor será do comprimento de vinte e cinco mil côvados e da largura de dez mil.
10 Esta região santa dos sacerdotes terá, ao norte, vinte e cinco mil côvados, ao ocidente, dez mil de largura, ao oriente, dez mil de largura e ao sul, vinte e cinco mil de comprimento; o santuário do Senhor estará no meio dela.
11 Será para os sacerdotes santificados, para os filhos de Zadoque, que cumpriram o seu dever e não andaram errados, quando os filhos de Israel se extraviaram, como fizeram os levitas.
12 Será região especial dentro da região sagrada, lugar santíssimo, fazendo limites com a porção dos levitas.
13 Os levitas, segundo o limite dos sacerdotes, terão vinte e cinco mil côvados de comprimento e dez mil de largura; todo o comprimento será vinte e cinco mil, e a largura, dez mil.
14 Não venderão nada disto, nem trocarão, nem transferirão a outrem o melhor da terra, porque é santo ao Senhor.
15 Mas os cinco mil côvados que ficaram da largura diante dos vinte e cinco mil serão para o uso civil da cidade, para habitação e para arredores; a cidade estará no meio.
16 Serão estas as suas medidas: o lado norte, de quatro mil e quinhentos côvados, o lado sul, de quatro mil e quinhentos, o lado oriental, de quatro mil e quinhentos, e o lado ocidental, de quatro mil e quinhentos.
17 Os arredores da cidade serão, ao norte, de duzentos e cinquenta côvados, ao sul, de duzentos e cinquenta côvados, ao oriente, de duzentos e cinquenta e, ao ocidente, de duzentos e cinquenta.
18 Quanto ao que ficou do resto do comprimento, paralelo à região sagrada, será de dez mil para o oriente e de dez mil para o ocidente e corresponderá à região sagrada; e o seu produto será para o sustento daqueles que trabalham na cidade.
19 Lavrá-lo-ão os trabalhadores da cidade, provindos de todas as tribos de Israel.
20 A região toda será de vinte e cinco mil côvados em quadrado, isto é, a região sagrada juntamente com a possessão da cidade.
21 O que restar será para o príncipe, deste e do outro lado da região sagrada e da possessão da cidade. Por isso, aquilo que se estende dos vinte e cinco mil côvados em direção do oriente e também dos vinte e cinco mil côvados em direção do ocidente, paralelamente com as porções, será do príncipe; a região sagrada e o santuário do templo estarão no meio.
22 Excetuando o que pertence aos levitas e a cidade que está no meio daquilo que pertence ao príncipe, entre o território de Judá e o de Benjamim, será isso para o príncipe.
23 Quanto ao resto das tribos, desde o lado oriental até ao ocidental, Benjamim terá uma porção.
24 Limitando-se com Benjamim, desde o lado oriental até ao ocidental, Simeão, uma porção.
25 Limitando-se com Simeão, desde o lado oriental até ao ocidental, Issacar, uma porção.
26 Limitando-se com Issacar, desde o lado oriental até ao ocidental, Zebulom, uma porção.
27 Limitando-se com Zebulom, desde o lado oriental até ao ocidental, Gade, uma porção.
28 Limitando-se com o território de Gade, ao sul, o limite será desde Tamar até às águas de Meribá-Cades, ao longo do ribeiro do Egito até ao mar Grande.
29 Esta é a terra que sorteareis em herança às tribos de Israel; e estas, as suas porções, diz o Senhor Deus.
30 São estas as saídas da cidade: do lado norte, que mede quatro mil e quinhentos côvados,
31 três portas: a porta de Rúben, a de Judá e a de Levi, tomando as portas da cidade os nomes das tribos de Israel;
32 do lado oriental, quatro mil e quinhentos côvados e três portas, a saber: a porta de José, a de Benjamim e a de Dã;
33 do lado sul, quatro mil e quinhentos côvados e três portas: a porta de Simeão, a de Issacar e a de Zebulom;
34 do lado ocidental, quatro mil e quinhentos côvados e as suas três portas: a porta de Gade, a de Aser e a de Naftali.
35 Dezoito mil côvados em redor; e o nome da cidade desde aquele dia será: O Senhor Está Ali.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Ezequiel','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)