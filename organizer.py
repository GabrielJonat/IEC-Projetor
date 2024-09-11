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
1 Provérbios de Salomão, filho de Davi, o rei de Israel.
2 Para aprender a sabedoria e o ensino; para entender as palavras de inteligência;
3 para obter o ensino do bom proceder, a justiça, o juízo e a equidade;
4 para dar aos simples prudência e aos jovens, conhecimento e bom siso.
5 Ouça o sábio e cresça em prudência; e o instruído adquira habilidade
6 para entender provérbios e parábolas, as palavras e enigmas dos sábios.
7 O temor do Senhor é o princípio do saber, mas os loucos desprezam a sabedoria e o ensino.
8 Filho meu, ouve o ensino de teu pai e não deixes a instrução de tua mãe.
9 Porque serão diadema de graça para a tua cabeça e colares, para o teu pescoço.
10 Filho meu, se os pecadores querem seduzir-te, não o consintas.
11 Se disserem: Vem conosco, embosquemo-nos para derramar sangue, espreitemos, ainda que sem motivo, os inocentes;
12 traguemo-los vivos, como o abismo, e inteiros, como os que descem à cova;
13 acharemos toda sorte de bens preciosos; encheremos de despojos a nossa casa;
14 lança a tua sorte entre nós; teremos todos uma só bolsa.
15 Filho meu, não te ponhas a caminho com eles; guarda das suas veredas os pés;
16 porque os seus pés correm para o mal e se apressam a derramar sangue.
17 Pois debalde se estende a rede à vista de qualquer ave.
18 Estes se emboscam contra o seu próprio sangue e a sua própria vida espreitam.
19 Tal é a sorte de todo ganancioso; e este espírito de ganância tira a vida de quem o possui.
20 Grita na rua a Sabedoria, nas praças, levanta a voz;
21 do alto dos muros clama, à entrada das portas e nas cidades profere as suas palavras:
22 Até quando, ó néscios, amareis a necedade? E vós, escarnecedores, desejareis o escárnio? E vós, loucos, aborrecereis o conhecimento?
23 Atentai para a minha repreensão; eis que derramarei copiosamente para vós outros o meu espírito e vos farei saber as minhas palavras.
24 Mas, porque clamei, e vós recusastes; porque estendi a mão, e não houve quem atendesse;
25 antes, rejeitastes todo o meu conselho e não quisestes a minha repreensão;
26 também eu me rirei na vossa desventura, e, em vindo o vosso terror, eu zombarei,
27 em vindo o vosso terror como a tempestade, em vindo a vossa perdição como o redemoinho, quando vos chegar o aperto e a angústia.
28 Então, me invocarão, mas eu não responderei; procurar-me-ão, porém não me hão de achar.
29 Porquanto aborreceram o conhecimento e não preferiram o temor do Senhor;
30 não quiseram o meu conselho e desprezaram toda a minha repreensão.
31 Portanto, comerão do fruto do seu procedimento e dos seus próprios conselhos se fartarão.
32 Os néscios são mortos por seu desvio, e aos loucos a sua impressão de bem-estar os leva à perdição.
33 Mas o que me der ouvidos habitará seguro, tranquilo e sem temor do mal.*
1 Filho meu, se aceitares as minhas palavras e esconderes contigo os meus mandamentos,
2 para fazeres atento à sabedoria o teu ouvido e para inclinares o coração ao entendimento,
3 e, se clamares por inteligência, e por entendimento alçares a voz,
4 se buscares a sabedoria como a prata e como a tesouros escondidos a procurares,
5 então, entenderás o temor do Senhor e acharás o conhecimento de Deus.
6 Porque o Senhor dá a sabedoria, e da sua boca vem a inteligência e o entendimento.
7 Ele reserva a verdadeira sabedoria para os retos; é escudo para os que caminham na sinceridade,
8 guarda as veredas do juízo e conserva o caminho dos seus santos.
9 Então, entenderás justiça, juízo e equidade, todas as boas veredas.
10 Porquanto a sabedoria entrará no teu coração, e o conhecimento será agradável à tua alma.
11 O bom siso te guardará, e a inteligência te conservará;
12 para te livrar do caminho do mal e do homem que diz coisas perversas;
13 dos que deixam as veredas da retidão, para andarem pelos caminhos das trevas;
14 que se alegram de fazer o mal, folgam com as perversidades dos maus,
15 seguem veredas tortuosas e se desviam nos seus caminhos;
16 para te livrar da mulher adúltera, da estrangeira, que lisonjeia com palavras,
17 a qual deixa o amigo da sua mocidade e se esquece da aliança do seu Deus;
18 porque a sua casa se inclina para a morte, e as suas veredas, para o reino das sombras da morte;
19 todos os que se dirigem a essa mulher não voltarão e não atinarão com as veredas da vida.
20 Assim, andarás pelo caminho dos homens de bem e guardarás as veredas dos justos.
21 Porque os retos habitarão a terra, e os íntegros permanecerão nela.
22 Mas os perversos serão eliminados da terra, e os aleivosos serão dela desarraigados.*
1 Filho meu, não te esqueças dos meus ensinos, e o teu coração guarde os meus mandamentos;
2 porque eles aumentarão os teus dias e te acrescentarão anos de vida e paz.
3 Não te desamparem a benignidade e a fidelidade; ata-as ao pescoço; escreve-as na tábua do teu coração
4 e acharás graça e boa compreensão diante de Deus e dos homens.
5 Confia no Senhor de todo o teu coração e não te estribes no teu próprio entendimento.
6 Reconhece-o em todos os teus caminhos, e ele endireitará as tuas veredas.
7 Não sejas sábio aos teus próprios olhos; teme ao Senhor e aparta-te do mal;
8 será isto saúde para o teu corpo e refrigério, para os teus ossos.
9 Honra ao Senhor com os teus bens e com as primícias de toda a tua renda;
10 e se encherão fartamente os teus celeiros, e transbordarão de vinho os teus lagares.
11 Filho meu, não rejeites a disciplina do Senhor, nem te enfades da sua repreensão.
12 Porque o Senhor repreende a quem ama, assim como o pai, ao filho a quem quer bem.
13 Feliz o homem que acha sabedoria, e o homem que adquire conhecimento;
14 porque melhor é o lucro que ela dá do que o da prata, e melhor a sua renda do que o ouro mais fino.
15 Mais preciosa é do que pérolas, e tudo o que podes desejar não é comparável a ela.
16 O alongar-se da vida está na sua mão direita, na sua esquerda, riquezas e honra.
17 Os seus caminhos são caminhos deliciosos, e todas as suas veredas, paz.
18 É árvore de vida para os que a alcançam, e felizes são todos os que a retêm.
19 O Senhor com sabedoria fundou a terra, com inteligência estabeleceu os céus.
20 Pelo seu conhecimento os abismos se rompem, e as nuvens destilam orvalho.
21 Filho meu, não se apartem estas coisas dos teus olhos; guarda a verdadeira sabedoria e o bom siso;
22 porque serão vida para a tua alma e adorno ao teu pescoço.
23 Então, andarás seguro no teu caminho, e não tropeçará o teu pé.
24 Quando te deitares, não temerás; deitar-te-ás, e o teu sono será suave.
25 Não temas o pavor repentino, nem a arremetida dos perversos, quando vier.
26 Porque o Senhor será a tua segurança e guardará os teus pés de serem presos.
27 Não te furtes a fazer o bem a quem de direito, estando na tua mão o poder de fazê-lo.
28 Não digas ao teu próximo: Vai e volta amanhã; então, to darei, se o tens agora contigo.
29 Não maquines o mal contra o teu próximo, pois habita junto de ti confiadamente.
30 Jamais pleiteies com alguém sem razão, se te não houver feito mal.
31 Não tenhas inveja do homem violento, nem sigas nenhum de seus caminhos;
32 porque o Senhor abomina o perverso, mas aos retos trata com intimidade.
33 A maldição do Senhor habita na casa do perverso, porém a morada dos justos ele abençoa.
34 Certamente, ele escarnece dos escarnecedores, mas dá graça aos humildes.
35 Os sábios herdarão honra, mas os loucos tomam sobre si a ignomínia.*
1 Ouvi, filhos, a instrução do pai e estai atentos para conhecerdes o entendimento;
2 porque vos dou boa doutrina; não deixeis o meu ensino.
3 Quando eu era filho em companhia de meu pai, tenro e único diante de minha mãe,
4 então, ele me ensinava e me dizia: Retenha o teu coração as minhas palavras; guarda os meus mandamentos e vive;
5 adquire a sabedoria, adquire o entendimento e não te esqueças das palavras da minha boca, nem delas te apartes.
6 Não desampares a sabedoria, e ela te guardará; ama-a, e ela te protegerá.
7 O princípio da sabedoria é: Adquire a sabedoria; sim, com tudo o que possuis, adquire o entendimento.
8 Estima-a, e ela te exaltará; se a abraçares, ela te honrará;
9 dará à tua cabeça um diadema de graça e uma coroa de glória te entregará.
10 Ouve, filho meu, e aceita as minhas palavras, e se te multiplicarão os anos de vida.
11 No caminho da sabedoria, te ensinei e pelas veredas da retidão te fiz andar.
12 Em andando por elas, não se embaraçarão os teus passos; se correres, não tropeçarás.
13 Retém a instrução e não a largues; guarda-a, porque ela é a tua vida.
14 Não entres na vereda dos perversos, nem sigas pelo caminho dos maus.
15 Evita-o; não passes por ele; desvia-te dele e passa de largo;
16 pois não dormem, se não fizerem mal, e foge deles o sono, se não fizerem tropeçar alguém;
17 porque comem o pão da impiedade e bebem o vinho das violências.
18 Mas a vereda dos justos é como a luz da aurora, que vai brilhando mais e mais até ser dia perfeito.
19 O caminho dos perversos é como a escuridão; nem sabem eles em que tropeçam.
20 Filho meu, atenta para as minhas palavras; aos meus ensinamentos inclina os ouvidos.
21 Não os deixes apartar-se dos teus olhos; guarda-os no mais íntimo do teu coração.
22 Porque são vida para quem os acha e saúde, para o seu corpo.
23 Sobre tudo o que se deve guardar, guarda o coração, porque dele procedem as fontes da vida.
24 Desvia de ti a falsidade da boca e afasta de ti a perversidade dos lábios.
25 Os teus olhos olhem direito, e as tuas pálpebras, diretamente diante de ti.
26 Pondera a vereda de teus pés, e todos os teus caminhos sejam retos.
27 Não declines nem para a direita nem para a esquerda; retira o teu pé do mal.*
1 Filho meu, atende a minha sabedoria; à minha inteligência inclina os ouvidos
2 para que conserves a discrição, e os teus lábios guardem o conhecimento;
3 porque os lábios da mulher adúltera destilam favos de mel, e as suas palavras são mais suaves do que o azeite;
4 mas o fim dela é amargoso como o absinto, agudo, como a espada de dois gumes.
5 Os seus pés descem à morte; os seus passos conduzem-na ao inferno.
6 Ela não pondera a vereda da vida; anda errante nos seus caminhos e não o sabe.
7 Agora, pois, filho, dá-me ouvidos e não te desvies das palavras da minha boca.
8 Afasta o teu caminho da mulher adúltera e não te aproximes da porta da sua casa;
9 para que não dês a outrem a tua honra, nem os teus anos, a cruéis;
10 para que dos teus bens não se fartem os estranhos, e o fruto do teu trabalho não entre em casa alheia;
11 e gemas no fim de tua vida, quando se consumirem a tua carne e o teu corpo,
12 e digas: Como aborreci o ensino! E desprezou o meu coração a disciplina!
13 E não escutei a voz dos que me ensinavam, nem a meus mestres inclinei os ouvidos!
14 Quase que me achei em todo mal que sucedeu no meio da assembleia e da congregação.
15 Bebe a água da tua própria cisterna e das correntes do teu poço.
16 Derramar-se-iam por fora as tuas fontes, e, pelas praças, os ribeiros de águas?
17 Sejam para ti somente e não para os estranhos contigo.
18 Seja bendito o teu manancial, e alegra-te com a mulher da tua mocidade,
19 corça de amores e gazela graciosa. Saciem-te os seus seios em todo o tempo; e embriaga-te sempre com as suas carícias.
20 Por que, filho meu, andarias cego pela estranha e abraçarias o peito de outra?
21 Porque os caminhos do homem estão perante os olhos do Senhor, e ele considera todas as suas veredas.
22 Quanto ao perverso, as suas iniquidades o prenderão, e com as cordas do seu pecado será detido.
23 Ele morrerá pela falta de disciplina, e, pela sua muita loucura, perdido, cambaleia.*
1 Filho meu, se ficaste por fiador do teu companheiro e se te empenhaste ao estranho,
2 estás enredado com o que dizem os teus lábios, estás preso com as palavras da tua boca.
3 Agora, pois, faze isto, filho meu, e livra-te, pois caíste nas mãos do teu companheiro: vai, prostra-te e importuna o teu companheiro;
4 não dês sono aos teus olhos, nem repouso às tuas pálpebras;
5 livra-te, como a gazela, da mão do caçador e, como a ave, da mão do passarinheiro.
6 Vai ter com a formiga, ó preguiçoso, considera os seus caminhos e sê sábio.
7 Não tendo ela chefe, nem oficial, nem comandante,
8 no estio, prepara o seu pão, na sega, ajunta o seu mantimento.
9 Ó preguiçoso, até quando ficarás deitado? Quando te levantarás do teu sono?
10 Um pouco para dormir, um pouco para tosquenejar, um pouco para encruzar os braços em repouso,
11 assim sobrevirá a tua pobreza como um ladrão, e a tua necessidade, como um homem armado.
12 O homem de Belial, o homem vil, é o que anda com a perversidade na boca,
13 acena com os olhos, arranha com os pés e faz sinais com os dedos.
14 No seu coração há perversidade; todo o tempo maquina o mal; anda semeando contendas.
15 Pelo que a sua destruição virá repentinamente; subitamente, será quebrantado, sem que haja cura.
16 Seis coisas o Senhor aborrece, e a sétima a sua alma abomina:
17 olhos altivos, língua mentirosa, mãos que derramam sangue inocente,
18 coração que trama projetos iníquos, pés que se apressam a correr para o mal,
19 testemunha falsa que profere mentiras e o que semeia contendas entre irmãos.
Advertência contra a mulher adúltera
20 Filho meu, guarda o mandamento de teu pai e não deixes a instrução de tua mãe;
21 ata-os perpetuamente ao teu coração, pendura-os ao pescoço.
22 Quando caminhares, isso te guiará; quando te deitares, te guardará; quando acordares, falará contigo.
23 Porque o mandamento é lâmpada, e a instrução, luz; e as repreensões da disciplina são o caminho da vida;
24 para te guardarem da vil mulher e das lisonjas da mulher alheia.
25 Não cobices no teu coração a sua formosura, nem te deixes prender com as suas olhadelas.
26 Por uma prostituta o máximo que se paga é um pedaço de pão, mas a adúltera anda à caça de vida preciosa.
27 Tomará alguém fogo no seio, sem que as suas vestes se incendeiem?
28 Ou andará alguém sobre brasas, sem que se queimem os seus pés?
29 Assim será com o que se chegar à mulher do seu próximo; não ficará sem castigo todo aquele que a tocar.
30 Não é certo que se despreza o ladrão, quando furta para saciar-se, tendo fome?
31 Pois este, quando encontrado, pagará sete vezes tanto; entregará todos os bens de sua casa.
32 O que adultera com uma mulher está fora de si; só mesmo quem quer arruinar-se é que pratica tal coisa.
33 Achará açoites e infâmia, e o seu opróbrio nunca se apagará.
34 Porque o ciúme excita o furor do marido; e não terá compaixão no dia da vingança.
35 Não se contentará com o resgate, nem aceitará presentes, ainda que sejam muitos.*
1 Filho meu, guarda as minhas palavras e conserva dentro de ti os meus mandamentos.
2 Guarda os meus mandamentos e vive; e a minha lei, como a menina dos teus olhos.
3 Ata-os aos dedos, escreve-os na tábua do teu coração.
4 Dize à Sabedoria: Tu és minha irmã; e ao Entendimento chama teu parente;
5 para te guardarem da mulher alheia, da estranha que lisonjeia com palavras.
6 Porque da janela da minha casa, por minhas grades, olhando eu,
7 vi entre os simples, descobri entre os jovens um que era carecente de juízo,
8 que ia e vinha pela rua junto à esquina da mulher estranha e seguia o caminho da sua casa,
9 à tarde do dia, no crepúsculo, na escuridão da noite, nas trevas.
10 Eis que a mulher lhe sai ao encontro, com vestes de prostituta e astuta de coração.
11 É apaixonada e inquieta, cujos pés não param em casa;
12 ora está nas ruas, ora, nas praças, espreitando por todos os cantos.
13 Aproximou-se dele, e o beijou, e de cara impudente lhe diz:
14 Sacrifícios pacíficos tinha eu de oferecer; paguei hoje os meus votos.
15 Por isso, saí ao teu encontro, a buscar-te, e te achei.
16 Já cobri de colchas a minha cama, de linho fino do Egito, de várias cores;
17 já perfumei o meu leito com mirra, aloés e cinamomo.
18 Vem, embriaguemo-nos com as delícias do amor, até pela manhã; gozemos amores.
19 Porque o meu marido não está em casa, saiu de viagem para longe.
20 Levou consigo um saquitel de dinheiro; só por volta da lua cheia ele tornará para casa.
21 Seduziu-o com as suas muitas palavras, com as lisonjas dos seus lábios o arrastou.
22 E ele num instante a segue, como o boi que vai ao matadouro; como o cervo que corre para a rede,
23 até que a flecha lhe atravesse o coração; como a ave que se apressa para o laço, sem saber que isto lhe custará a vida.
24 Agora, pois, filho, dá-me ouvidos e sê atento às palavras da minha boca;
25 não se desvie o teu coração para os caminhos dela, e não andes perdido nas suas veredas;
26 porque a muitos feriu e derribou; e são muitos os que por ela foram mortos.
27 A sua casa é caminho para a sepultura e desce para as câmaras da morte.*
1 Não clama, porventura, a Sabedoria, e o Entendimento não faz ouvir a sua voz?
2 No cimo das alturas, junto ao caminho, nas encruzilhadas das veredas ela se coloca;
3 junto às portas, à entrada da cidade, à entrada das portas está gritando:
4 A vós outros, ó homens, clamo; e a minha voz se dirige aos filhos dos homens.
5 Entendei, ó simples, a prudência; e vós, néscios, entendei a sabedoria.
6 Ouvi, pois falarei coisas excelentes; os meus lábios proferirão coisas retas.
7 Porque a minha boca proclamará a verdade; os meus lábios abominam a impiedade.
8 São justas todas as palavras da minha boca; não há nelas nenhuma coisa torta, nem perversa.
9 Todas são retas para quem as entende e justas, para os que acham o conhecimento.
10 Aceitai o meu ensino, e não a prata, e o conhecimento, antes do que o ouro escolhido.
11 Porque melhor é a sabedoria do que joias, e de tudo o que se deseja nada se pode comparar com ela.
12 Eu, a Sabedoria, habito com a prudência e disponho de conhecimentos e de conselhos.
13 O temor do Senhor consiste em aborrecer o mal; a soberba, a arrogância, o mau caminho e a boca perversa, eu os aborreço.
14 Meu é o conselho e a verdadeira sabedoria, eu sou o Entendimento, minha é a fortaleza.
15 Por meu intermédio, reinam os reis, e os príncipes decretam justiça.
16 Por meu intermédio, governam os príncipes, os nobres e todos os juízes da terra.
17 Eu amo os que me amam; os que me procuram me acham.
18 Riquezas e honra estão comigo, bens duráveis e justiça.
19 Melhor é o meu fruto do que o ouro, do que o ouro refinado; e o meu rendimento, melhor do que a prata escolhida.
20 Ando pelo caminho da justiça, no meio das veredas do juízo,
21 para dotar de bens os que me amam e lhes encher os tesouros.
22 O Senhor me possuía no início de sua obra, antes de suas obras mais antigas.
23 Desde a eternidade fui estabelecida, desde o princípio, antes do começo da terra.
24 Antes de haver abismos, eu nasci, e antes ainda de haver fontes carregadas de águas.
25 Antes que os montes fossem firmados, antes de haver outeiros, eu nasci.
26 Ainda ele não tinha feito a terra, nem as amplidões, nem sequer o princípio do pó do mundo.
27 Quando ele preparava os céus, aí estava eu; quando traçava o horizonte sobre a face do abismo;
28 quando firmava as nuvens de cima; quando estabelecia as fontes do abismo;
29 quando fixava ao mar o seu limite, para que as águas não traspassassem os seus limites; quando compunha os fundamentos da terra;
30 então, eu estava com ele e era seu arquiteto, dia após dia, eu era as suas delícias, folgando perante ele em todo o tempo;
31 regozijando-me no seu mundo habitável e achando as minhas delícias com os filhos dos homens.
32 Agora, pois, filhos, ouvi-me, porque felizes serão os que guardarem os meus caminhos.
33 Ouvi o ensino, sede sábios e não o rejeiteis.
34 Feliz o homem que me dá ouvidos, velando dia a dia às minhas portas, esperando às ombreiras da minha entrada.
35 Porque o que me acha acha a vida e alcança favor do Senhor.
36 Mas o que peca contra mim violenta a própria alma. Todos os que me aborrecem amam a morte.*
1 A Sabedoria edificou a sua casa, lavrou as suas sete colunas.
2 Carneou os seus animais, misturou o seu vinho e arrumou a sua mesa.
3 Já deu ordens às suas criadas e, assim, convida desde as alturas da cidade:
4 Quem é simples, volte-se para aqui. Aos faltos de senso diz:
5 Vinde, comei do meu pão e bebei do vinho que misturei.
6 Deixai os insensatos e vivei; andai pelo caminho do entendimento.
7 O que repreende o escarnecedor traz afronta sobre si; e o que censura o perverso a si mesmo se injuria.
8 Não repreendas o escarnecedor, para que te não aborreça; repreende o sábio, e ele te amará.
9 Dá instrução ao sábio, e ele se fará mais sábio ainda; ensina ao justo, e ele crescerá em prudência.
10 O temor do Senhor é o princípio da sabedoria, e o conhecimento do Santo é prudência.
11 Porque por mim se multiplicam os teus dias, e anos de vida se te acrescentarão.
12 Se és sábio, para ti mesmo o és; se és escarnecedor, tu só o suportarás.
13 A loucura é mulher apaixonada, é ignorante e não sabe coisa alguma.
14 Assenta-se à porta de sua casa, nas alturas da cidade, toma uma cadeira,
15 para dizer aos que passam e seguem direito o seu caminho:
16 Quem é simples, volte-se para aqui. E aos faltos de senso diz:
17 As águas roubadas são doces, e o pão comido às ocultas é agradável.
18 Eles, porém, não sabem que ali estão os mortos, que os seus convidados estão nas profundezas do inferno.*
1 Provérbios de Salomão. O filho sábio alegra a seu pai, mas o filho insensato é a tristeza de sua mãe.
2 Os tesouros da impiedade de nada aproveitam, mas a justiça livra da morte.
3 O Senhor não deixa ter fome o justo, mas rechaça a avidez dos perversos.
4 O que trabalha com mão remissa empobrece, mas a mão dos diligentes vem a enriquecer-se.
5 O que ajunta no verão é filho sábio, mas o que dorme na sega é filho que envergonha.
6 Sobre a cabeça do justo há bênçãos, mas na boca dos perversos mora a violência.
7 A memória do justo é abençoada, mas o nome dos perversos cai em podridão.
8 O sábio de coração aceita os mandamentos, mas o insensato de lábios vem a arruinar-se.
9 Quem anda em integridade anda seguro, mas o que perverte os seus caminhos será conhecido.
10 O que acena com os olhos traz desgosto, e o insensato de lábios vem a arruinar-se.
11 A boca do justo é manancial de vida, mas na boca dos perversos mora a violência.
12 O ódio excita contendas, mas o amor cobre todas as transgressões.
13 Nos lábios do prudente, se acha sabedoria, mas a vara é para as costas do falto de senso.
14 Os sábios entesouram o conhecimento, mas a boca do néscio é uma ruína iminente.
15 Os bens do rico são a sua cidade forte; a pobreza dos pobres é a sua ruína.
16 A obra do justo conduz à vida, e o rendimento do perverso, ao pecado.
17 O caminho para a vida é de quem guarda o ensino, mas o que abandona a repreensão anda errado.
18 O que retém o ódio é de lábios falsos, e o que difama é insensato.
19 No muito falar não falta transgressão, mas o que modera os lábios é prudente.
20 Prata escolhida é a língua do justo, mas o coração dos perversos vale mui pouco.
21 Os lábios do justo apascentam a muitos, mas, por falta de senso, morrem os tolos.
22 A bênção do Senhor enriquece, e, com ela, ele não traz desgosto.
23 Para o insensato, praticar a maldade é divertimento; para o homem inteligente, o ser sábio.
24 Aquilo que teme o perverso, isso lhe sobrevém, mas o anelo dos justos Deus o cumpre.
25 Como passa a tempestade, assim desaparece o perverso, mas o justo tem perpétuo fundamento.
26 Como vinagre para os dentes e fumaça para os olhos, assim é o preguiçoso para aqueles que o mandam.
27 O temor do Senhor prolonga os dias da vida, mas os anos dos perversos serão abreviados.
28 A esperança dos justos é alegria, mas a expectação dos perversos perecerá.
29 O caminho do Senhor é fortaleza para os íntegros, mas ruína aos que praticam a iniquidade.
30 O justo jamais será abalado, mas os perversos não habitarão a terra.
31 A boca do justo produz sabedoria, mas a língua da perversidade será desarraigada.
32 Os lábios do justo sabem o que agrada, mas a boca dos perversos, somente o mal.*
1 Balança enganosa é abominação para o Senhor, mas o peso justo é o seu prazer.
2 Em vindo a soberba, sobrevém a desonra, mas com os humildes está a sabedoria.
3 A integridade dos retos os guia; mas, aos pérfidos, a sua mesma falsidade os destrói.
4 As riquezas de nada aproveitam no dia da ira, mas a justiça livra da morte.
5 A justiça do íntegro endireita o seu caminho, mas pela sua impiedade cai o perverso.
6 A justiça dos retos os livrará, mas na sua maldade os pérfidos serão apanhados.
7 Morrendo o homem perverso, morre a sua esperança, e a expectação da iniquidade se desvanece.
8 O justo é libertado da angústia, e o perverso a recebe em seu lugar.
9 O ímpio, com a boca, destrói o próximo, mas os justos são libertados pelo conhecimento.
10 No bem-estar dos justos exulta a cidade, e, perecendo os perversos, há júbilo.
11 Pela bênção que os retos suscitam, a cidade se exalta, mas pela boca dos perversos é derribada.
12 O que despreza o próximo é falto de senso, mas o homem prudente, este se cala.
13 O mexeriqueiro descobre o segredo, mas o fiel de espírito o encobre.
14 Não havendo sábia direção, cai o povo, mas na multidão de conselheiros há segurança.
15 Quem fica por fiador de outrem sofrerá males, mas o que foge de o ser estará seguro.
16 A mulher graciosa alcança honra, como os poderosos adquirem riqueza.
17 O homem bondoso faz bem a si mesmo, mas o cruel a si mesmo se fere.
18 O perverso recebe um salário ilusório, mas o que semeia justiça terá recompensa verdadeira.
19 Tão certo como a justiça conduz para a vida, assim o que segue o mal, para a sua morte o faz.
20 Abomináveis para o Senhor são os perversos de coração, mas os que andam em integridade são o seu prazer.
21 O mau, é evidente, não ficará sem castigo, mas a geração dos justos é livre.
22 Como joia de ouro em focinho de porco, assim é a mulher formosa que não tem discrição.
23 O desejo dos justos tende somente para o bem, mas a expectação dos perversos redunda em ira.
24 A quem dá liberalmente, ainda se lhe acrescenta mais e mais; ao que retém mais do que é justo, ser-lhe-á em pura perda.
25 A alma generosa prosperará, e quem dá a beber será dessedentado.
26 Ao que retém o trigo, o povo o amaldiçoa, mas bênção haverá sobre a cabeça do seu vendedor.
27 Quem procura o bem alcança favor, mas ao que corre atrás do mal, este lhe sobrevirá.
28 Quem confia nas suas riquezas cairá, mas os justos reverdecerão como a folhagem.
29 O que perturba a sua casa herda o vento, e o insensato é servo do sábio de coração.
30 O fruto do justo é árvore de vida, e o que ganha almas é sábio.
31 Se o justo é punido na terra, quanto mais o perverso e o pecador!*
1 Quem ama a disciplina ama o conhecimento, mas o que aborrece a repreensão é estúpido.
2 O homem de bem alcança o favor do Senhor, mas ao homem de perversos desígnios, ele o condena.
3 O homem não se estabelece pela perversidade, mas a raiz dos justos não será removida.
4 A mulher virtuosa é a coroa do seu marido, mas a que procede vergonhosamente é como podridão nos seus ossos.
5 Os pensamentos do justo são retos, mas os conselhos do perverso, engano.
6 As palavras dos perversos são emboscadas para derramar sangue, mas a boca dos retos livra homens.
7 Os perversos serão derribados e já não são, mas a casa dos justos permanecerá.
8 Segundo o seu entendimento, será louvado o homem, mas o perverso de coração será desprezado.
9 Melhor é o que se estima em pouco e faz o seu trabalho do que o vanglorioso que tem falta de pão.
10 O justo atenta para a vida dos seus animais, mas o coração dos perversos é cruel.
11 O que lavra a sua terra será farto de pão, mas o que corre atrás de coisas vãs é falto de senso.
12 O perverso quer viver do que caçam os maus, mas a raiz dos justos produz o seu fruto.
13 Pela transgressão dos lábios o mau se enlaça, mas o justo sairá da angústia.
14 Cada um se farta de bem pelo fruto da sua boca, e o que as mãos do homem fizerem ser-lhe-á retribuído.
15 O caminho do insensato aos seus próprios olhos parece reto, mas o sábio dá ouvidos aos conselhos.
16 A ira do insensato num instante se conhece, mas o prudente oculta a afronta.
17 O que diz a verdade manifesta a justiça, mas a testemunha falsa, a fraude.
18 Alguém há cuja tagarelice é como pontas de espada, mas a língua dos sábios é medicina.
19 O lábio veraz permanece para sempre, mas a língua mentirosa, apenas um momento.
20 Há fraude no coração dos que maquinam mal, mas alegria têm os que aconselham a paz.
21 Nenhum agravo sobrevirá ao justo, mas os perversos, o mal os apanhará em cheio.
22 Os lábios mentirosos são abomináveis ao Senhor, mas os que agem fielmente são o seu prazer.
23 O homem prudente oculta o conhecimento, mas o coração dos insensatos proclama a estultícia.
24 A mão diligente dominará, mas a remissa será sujeita a trabalhos forçados.
25 A ansiedade no coração do homem o abate, mas a boa palavra o alegra.
26 O justo serve de guia para o seu companheiro, mas o caminho dos perversos os faz errar.
27 O preguiçoso não assará a sua caça, mas o bem precioso do homem é ser ele diligente.
28 Na vereda da justiça, está a vida, e no caminho da sua carreira não há morte.*
1 O filho sábio ouve a instrução do pai, mas o escarnecedor não atende à repreensão.
2 Do fruto da boca o homem comerá o bem, mas o desejo dos pérfidos é a violência.
3 O que guarda a boca conserva a sua alma, mas o que muito abre os lábios a si mesmo se arruína.
4 O preguiçoso deseja e nada tem, mas a alma dos diligentes se farta.
5 O justo aborrece a palavra de mentira, mas o perverso faz vergonha e se desonra.
6 A justiça guarda ao que anda em integridade, mas a malícia subverte ao pecador.
7 Uns se dizem ricos sem terem nada; outros se dizem pobres, sendo mui ricos.
8 Com as suas riquezas se resgata o homem, mas ao pobre não ocorre ameaça.
9 A luz dos justos brilha intensamente, mas a lâmpada dos perversos se apagará.
10 Da soberba só resulta a contenda, mas com os que se aconselham se acha a sabedoria.
11 Os bens que facilmente se ganham, esses diminuem, mas o que ajunta à força do trabalho terá aumento.
12 A esperança que se adia faz adoecer o coração, mas o desejo cumprido é árvore de vida.
13 O que despreza a palavra a ela se apenhora, mas o que teme o mandamento será galardoado.
14 O ensino do sábio é fonte de vida, para que se evitem os laços da morte.
15 A boa inteligência consegue favor, mas o caminho dos pérfidos é intransitável.
16 Todo prudente procede com conhecimento, mas o insensato espraia a sua loucura.
17 O mau mensageiro se precipita no mal, mas o embaixador fiel é medicina.
18 Pobreza e afronta sobrevêm ao que rejeita a instrução, mas o que guarda a repreensão será honrado.
19 O desejo que se cumpre agrada a alma, mas apartar-se do mal é abominável para os insensatos.
20 Quem anda com os sábios será sábio, mas o companheiro dos insensatos se tornará mau.
21 A desventura persegue os pecadores, mas os justos serão galardoados com o bem.
22 O homem de bem deixa herança aos filhos de seus filhos, mas a riqueza do pecador é depositada para o justo.
23 A terra virgem dos pobres dá mantimento em abundância, mas a falta de justiça o dissipa.
24 O que retém a vara aborrece a seu filho, mas o que o ama, cedo, o disciplina.
25 O justo tem o bastante para satisfazer o seu apetite, mas o estômago dos perversos passa fome.*
1 A mulher sábia edifica a sua casa, mas a insensata, com as próprias mãos, a derriba.
2 O que anda na retidão teme ao Senhor, mas o que anda em caminhos tortuosos, esse o despreza.
3 Está na boca do insensato a vara para a sua própria soberba, mas os lábios do prudente o preservarão.
4 Não havendo bois, o celeiro fica limpo, mas pela força do boi há abundância de colheitas.
5 A testemunha verdadeira não mente, mas a falsa se desboca em mentiras.
6 O escarnecedor procura a sabedoria e não a encontra, mas para o prudente o conhecimento é fácil.
7 Foge da presença do homem insensato, porque nele não divisarás lábios de conhecimento.
8 A sabedoria do prudente é entender o seu próprio caminho, mas a estultícia dos insensatos é enganadora.
9 Os loucos zombam do pecado, mas entre os retos há boa vontade.
10 O coração conhece a sua própria amargura, e da sua alegria não participará o estranho.
11 A casa dos perversos será destruída, mas a tenda dos retos florescerá.
12 Há caminho que ao homem parece direito, mas ao cabo dá em caminhos de morte.
13 Até no riso tem dor o coração, e o fim da alegria é tristeza.
14 O infiel de coração dos seus próprios caminhos se farta, como do seu próprio proceder, o homem de bem.
15 O simples dá crédito a toda palavra, mas o prudente atenta para os seus passos.
16 O sábio é cauteloso e desvia-se do mal, mas o insensato encoleriza-se e dá-se por seguro.
17 O que presto se ira faz loucuras, e o homem de maus desígnios é odiado.
18 Os simples herdam a estultícia, mas os prudentes se coroam de conhecimento.
19 Os maus inclinam-se perante a face dos bons, e os perversos, junto às portas do justo.
20 O pobre é odiado até do vizinho, mas o rico tem muitos amigos.
21 O que despreza ao seu vizinho peca, mas o que se compadece dos pobres é feliz.
22 Acaso, não erram os que maquinam o mal? Mas amor e fidelidade haverá para os que planejam o bem.
23 Em todo trabalho há proveito; meras palavras, porém, levam à penúria.
24 Aos sábios a riqueza é coroa, mas a estultícia dos insensatos não passa de estultícia.
25 A testemunha verdadeira livra almas, mas o que se desboca em mentiras é enganador.
26 No temor do Senhor, tem o homem forte amparo, e isso é refúgio para os seus filhos.
27 O temor do Senhor é fonte de vida para evitar os laços da morte.
28 Na multidão do povo, está a glória do rei, mas, na falta de povo, a ruína do príncipe.
29 O longânimo é grande em entendimento, mas o de ânimo precipitado exalta a loucura.
30 O ânimo sereno é a vida do corpo, mas a inveja é a podridão dos ossos.
31 O que oprime ao pobre insulta aquele que o criou, mas a este honra o que se compadece do necessitado.
32 Pela sua malícia é derribado o perverso, mas o justo, ainda morrendo, tem esperança.
33 No coração do prudente, repousa a sabedoria, mas o que há no interior dos insensatos vem a lume.
34 A justiça exalta as nações, mas o pecado é o opróbrio dos povos.
35 O servo prudente goza do favor do rei, mas o que procede indignamente é objeto do seu furor.*
1 A resposta branda desvia o furor, mas a palavra dura suscita a ira.
2 A língua dos sábios adorna o conhecimento, mas a boca dos insensatos derrama a estultícia.
3 Os olhos do Senhor estão em todo lugar, contemplando os maus e os bons.
4 A língua serena é árvore de vida, mas a perversa quebranta o espírito.
5 O insensato despreza a instrução de seu pai, mas o que atende à repreensão consegue a prudência.
6 Na casa do justo há grande tesouro, mas na renda dos perversos há perturbação.
7 A língua dos sábios derrama o conhecimento, mas o coração dos insensatos não procede assim.
8 O sacrifício dos perversos é abominável ao Senhor, mas a oração dos retos é o seu contentamento.
9 O caminho do perverso é abominação ao Senhor, mas este ama o que segue a justiça.
10 Disciplina rigorosa há para o que deixa a vereda, e o que odeia a repreensão morrerá.
11 O além e o abismo estão descobertos perante o Senhor; quanto mais o coração dos filhos dos homens!
12 O escarnecedor não ama àquele que o repreende, nem se chegará para os sábios.
13 O coração alegre aformoseia o rosto, mas com a tristeza do coração o espírito se abate.
14 O coração sábio procura o conhecimento, mas a boca dos insensatos se apascenta de estultícia.
15 Todos os dias do aflito são maus, mas a alegria do coração é banquete contínuo.
16 Melhor é o pouco, havendo o temor do Senhor, do que grande tesouro onde há inquietação.
17 Melhor é um prato de hortaliças onde há amor do que o boi cevado e, com ele, o ódio.
18 O homem iracundo suscita contendas, mas o longânimo apazigua a luta.
19 O caminho do preguiçoso é como que cercado de espinhos, mas a vereda dos retos é plana.
20 O filho sábio alegra a seu pai, mas o homem insensato despreza a sua mãe.
21 A estultícia é alegria para o que carece de entendimento, mas o homem sábio anda retamente.
22 Onde não há conselho fracassam os projetos, mas com os muitos conselheiros há bom êxito.
23 O homem se alegra em dar resposta adequada, e a palavra, a seu tempo, quão boa é!
24 Para o sábio há o caminho da vida que o leva para cima, a fim de evitar o inferno, embaixo.
25 O Senhor deita por terra a casa dos soberbos; contudo, mantém a herança da viúva.
26 Abomináveis são para o Senhor os desígnios do mau, mas as palavras bondosas lhe são aprazíveis.
27 O que é ávido por lucro desonesto transtorna a sua casa, mas o que odeia o suborno, esse viverá.
28 O coração do justo medita o que há de responder, mas a boca dos perversos transborda maldades.
29 O Senhor está longe dos perversos, mas atende à oração dos justos.
30 O olhar de amigo alegra ao coração; as boas-novas fortalecem até os ossos.
31 Os ouvidos que atendem à repreensão salutar no meio dos sábios têm a sua morada.
32 O que rejeita a disciplina menospreza a sua alma, porém o que atende à repreensão adquire entendimento.
33 O temor do Senhor é a instrução da sabedoria, e a humildade precede a honra.*
1 Melhor é um bocado seco e tranquilidade do que a casa farta de carnes e contendas.
2 O escravo prudente dominará sobre o filho que causa vergonha e, entre os irmãos, terá parte na herança.
3 O crisol prova a prata, e o forno, o ouro; mas aos corações prova o Senhor.
4 O malfazejo atenta para o lábio iníquo; o mentiroso inclina os ouvidos para a língua maligna.
5 O que escarnece do pobre insulta ao que o criou; o que se alegra da calamidade não ficará impune.
6 Coroa dos velhos são os filhos dos filhos; e a glória dos filhos são os pais.
7 Ao insensato não convém a palavra excelente; quanto menos ao príncipe, o lábio mentiroso!
8 Pedra mágica é o suborno aos olhos de quem o dá, e para onde quer que se volte terá seu proveito.
9 O que encobre a transgressão adquire amor, mas o que traz o assunto à baila separa os maiores amigos.
10 Mais fundo entra a repreensão no prudente do que cem açoites no insensato.
11 O rebelde não busca senão o mal; por isso, mensageiro cruel se enviará contra ele.
12 Melhor é encontrar-se uma ursa roubada dos filhos do que o insensato na sua estultícia.
13 Quanto àquele que paga o bem com o mal, não se apartará o mal da sua casa.
14 Como o abrir-se da represa, assim é o começo da contenda; desiste, pois, antes que haja rixas.
15 O que justifica o perverso e o que condena o justo abomináveis são para o Senhor, tanto um como o outro.
16 De que serviria o dinheiro na mão do insensato para comprar a sabedoria, visto que não tem entendimento?
17 Em todo tempo ama o amigo, e na angústia se faz o irmão.
18 O homem falto de entendimento compromete-se, ficando por fiador do seu próximo.
19 O que ama a contenda ama o pecado; o que faz alta a sua porta facilita a própria queda.
20 O perverso de coração jamais achará o bem; e o que tem a língua dobre vem a cair no mal.
21 O filho estulto é tristeza para o pai, e o pai do insensato não se alegra.
22 O coração alegre é bom remédio, mas o espírito abatido faz secar os ossos.
23 O perverso aceita suborno secretamente, para perverter as veredas da justiça.
24 A sabedoria é o alvo do inteligente, mas os olhos do insensato vagam pelas extremidades da terra.
25 O filho insensato é tristeza para o pai e amargura para quem o deu à luz.
26 Não é bom punir ao justo; é contra todo direito ferir ao príncipe.
27 Quem retém as palavras possui o conhecimento, e o sereno de espírito é homem de inteligência.
28 Até o estulto, quando se cala, é tido por sábio, e o que cerra os lábios, por sábio.*
1 O solitário busca o seu próprio interesse e insurge-se contra a verdadeira sabedoria.
2 O insensato não tem prazer no entendimento, senão em externar o seu interior.
3 Vindo a perversidade, vem também o desprezo; e, com a ignomínia, a vergonha.
4 Águas profundas são as palavras da boca do homem, e a fonte da sabedoria, ribeiros transbordantes.
5 Não é bom ser parcial com o perverso, para torcer o direito contra os justos.
6 Os lábios do insensato entram na contenda, e por açoites brada a sua boca.
7 A boca do insensato é a sua própria destruição, e os seus lábios, um laço para a sua alma.
8 As palavras do maldizente são doces bocados que descem para o mais interior do ventre.
9 Quem é negligente na sua obra já é irmão do desperdiçador.
10 Torre forte é o nome do Senhor, à qual o justo se acolhe e está seguro.
11 Os bens do rico lhe são cidade forte e, segundo imagina, uma alta muralha.
12 Antes da ruína, gaba-se o coração do homem, e diante da honra vai a humildade.
13 Responder antes de ouvir é estultícia e vergonha.
14 O espírito firme sustém o homem na sua doença, mas o espírito abatido, quem o pode suportar?
15 O coração do sábio adquire o conhecimento, e o ouvido dos sábios procura o saber.
16 O presente que o homem faz alarga-lhe o caminho e leva-o perante os grandes.
17 O que começa o pleito parece justo, até que vem o outro e o examina.
18 Pelo lançar da sorte, cessam os pleitos, e se decide a causa entre os poderosos.
19 O irmão ofendido resiste mais que uma fortaleza; suas contendas são ferrolhos de um castelo.
20 Do fruto da boca o coração se farta, do que produzem os lábios se satisfaz.
21 A morte e a vida estão no poder da língua; o que bem a utiliza come do seu fruto.
22 O que acha uma esposa acha o bem e alcançou a benevolência do Senhor.
23 O pobre fala com súplicas, porém o rico responde com durezas.
24 O homem que tem muitos amigos sai perdendo; mas há amigo mais chegado do que um irmão.*
1 Melhor é o pobre que anda na sua integridade do que o perverso de lábios e tolo.
2 Não é bom proceder sem refletir, e peca quem é precipitado.
3 A estultícia do homem perverte o seu caminho, mas é contra o Senhor que o seu coração se ira.
4 As riquezas multiplicam os amigos; mas, ao pobre, o seu próprio amigo o deixa.
5 A falsa testemunha não fica impune, e o que profere mentiras não escapa.
6 Ao generoso, muitos o adulam, e todos são amigos do que dá presentes.
7 Se os irmãos do pobre o aborrecem, quanto mais se afastarão dele os seus amigos! Corre após eles com súplicas, mas não os alcança.
8 O que adquire entendimento ama a sua alma; o que conserva a inteligência acha o bem.
9 A falsa testemunha não fica impune, e o que profere mentiras perece.
10 Ao insensato não convém a vida regalada, quanto menos ao escravo dominar os príncipes!
11 A discrição do homem o torna longânimo, e sua glória é perdoar as injúrias.
12 Como o bramido do leão, assim é a indignação do rei; mas seu favor é como o orvalho sobre a erva.
13 O filho insensato é a desgraça do pai, e um gotejar contínuo, as contenções da esposa.
14 A casa e os bens vêm como herança dos pais; mas do Senhor, a esposa prudente.
15 A preguiça faz cair em profundo sono, e o ocioso vem a padecer fome.
16 O que guarda o mandamento guarda a sua alma; mas o que despreza os seus caminhos, esse morre.
17 Quem se compadece do pobre ao Senhor empresta, e este lhe paga o seu benefício.
18 Castiga a teu filho, enquanto há esperança, mas não te excedas a ponto de matá-lo.
19 Homem de grande ira tem de sofrer o dano; porque, se tu o livrares, virás ainda a fazê-lo de novo.
20 Ouve o conselho e recebe a instrução, para que sejas sábio nos teus dias por vir.
21 Muitos propósitos há no coração do homem, mas o desígnio do Senhor permanecerá.
22 O que torna agradável o homem é a sua misericórdia; o pobre é preferível ao mentiroso.
23 O temor do Senhor conduz à vida; aquele que o tem ficará satisfeito, e mal nenhum o visitará.
24 O preguiçoso mete a mão no prato e não quer ter o trabalho de a levar à boca.
25 Quando ferires ao escarnecedor, o simples aprenderá a prudência; repreende ao sábio, e crescerá em conhecimento.
26 O que maltrata a seu pai ou manda embora a sua mãe filho é que envergonha e desonra.
27 Filho meu, se deixas de ouvir a instrução, desviar-te-ás das palavras do conhecimento.
28 A testemunha de Belial escarnece da justiça, e a boca dos perversos devora a iniquidade.
29 Preparados estão os juízos para os escarnecedores e os açoites, para as costas dos insensatos.*
1 O vinho é escarnecedor, e a bebida forte, alvoroçadora; todo aquele que por eles é vencido não é sábio.
2 Como o bramido do leão, é o terror do rei; o que lhe provoca a ira peca contra a sua própria vida.
3 Honroso é para o homem o desviar-se de contendas, mas todo insensato se mete em rixas.
4 O preguiçoso não lavra por causa do inverno, pelo que, na sega, procura e nada encontra.
5 Como águas profundas, são os propósitos do coração do homem, mas o homem de inteligência sabe descobri-los.
6 Muitos proclamam a sua própria benignidade; mas o homem fidedigno, quem o achará?
7 O justo anda na sua integridade; felizes lhe são os filhos depois dele.
8 Assentando-se o rei no trono do juízo, com os seus olhos dissipa todo mal.
9 Quem pode dizer: Purifiquei o meu coração, limpo estou do meu pecado?
10 Dois pesos e duas medidas, uns e outras são abomináveis ao Senhor.
11 Até a criança se dá a conhecer pelas suas ações, se o que faz é puro e reto.
12 O ouvido que ouve e o olho que vê, o Senhor os fez, tanto um como o outro.
13 Não ames o sono, para que não empobreças; abre os olhos e te fartarás do teu próprio pão.
14 Nada vale, nada vale, diz o comprador, mas, indo-se, então, se gaba.
15 Há ouro e abundância de pérolas, mas os lábios instruídos são joia preciosa.
16 Tome-se a roupa àquele que fica fiador por outrem; e, por penhor, àquele que se obriga por estrangeiros.
17 Suave é ao homem o pão ganho por fraude, mas, depois, a sua boca se encherá de pedrinhas de areia.
18 Os planos mediante os conselhos têm bom êxito; faze a guerra com prudência.
19 O mexeriqueiro revela o segredo; portanto, não te metas com quem muito abre os lábios.
20 A quem amaldiçoa a seu pai ou a sua mãe, apagar-se-lhe-á a lâmpada nas mais densas trevas.
21 A posse antecipada de uma herança no fim não será abençoada.
22 Não digas: Vingar-me-ei do mal; espera pelo Senhor, e ele te livrará.
23 Dois pesos são coisa abominável ao Senhor, e balança enganosa não é boa.
24 Os passos do homem são dirigidos pelo Senhor; como, pois, poderá o homem entender o seu caminho?
25 Laço é para o homem o dizer precipitadamente: É santo! E só refletir depois de fazer o voto.
26 O rei sábio joeira os perversos e faz passar sobre eles a roda.
27 O espírito do homem é a lâmpada do Senhor, a qual esquadrinha todo o mais íntimo do corpo.
28 Amor e fidelidade preservam o rei, e com benignidade sustém ele o seu trono.
29 O ornato dos jovens é a sua força, e a beleza dos velhos, as suas cãs.
30 Os vergões das feridas purificam do mal, e os açoites, o mais íntimo do corpo.*
1 Como ribeiros de águas assim é o coração do rei na mão do Senhor; este, segundo o seu querer, o inclina.
2 Todo caminho do homem é reto aos seus próprios olhos, mas o Senhor sonda os corações.
3 Exercitar justiça e juízo é mais aceitável ao Senhor do que sacrifício.
4 Olhar altivo e coração orgulhoso, a lâmpada dos perversos, são pecado.
5 Os planos do diligente tendem à abundância, mas a pressa excessiva, à pobreza.
6 Trabalhar por adquirir tesouro com língua falsa é vaidade e laço mortal.
7 A violência dos perversos os arrebata, porque recusam praticar a justiça.
8 Tortuoso é o caminho do homem carregado de culpa, mas reto, o proceder do honesto.
9 Melhor é morar no canto do eirado do que junto com a mulher rixosa na mesma casa.
10 A alma do perverso deseja o mal; nem o seu vizinho recebe dele compaixão.
11 Quando o escarnecedor é castigado, o simples se torna sábio; e, quando o sábio é instruído, recebe o conhecimento.
12 O Justo considera a casa dos perversos e os arrasta para o mal.
13 O que tapa o ouvido ao clamor do pobre também clamará e não será ouvido.
14 O presente que se dá em segredo abate a ira, e a dádiva em sigilo, uma forte indignação.
15 Praticar a justiça é alegria para o justo, mas espanto, para os que praticam a iniquidade.
16 O homem que se desvia do caminho do entendimento na congregação dos mortos repousará.
17 Quem ama os prazeres empobrecerá, quem ama o vinho e o azeite jamais enriquecerá.
18 O perverso serve de resgate para o justo; e, para os retos, o pérfido.
19 Melhor é morar numa terra deserta do que com a mulher rixosa e iracunda.
20 Tesouro desejável e azeite há na casa do sábio, mas o homem insensato os desperdiça.
21 O que segue a justiça e a bondade achará a vida, a justiça e a honra.
22 O sábio escala a cidade dos valentes e derriba a fortaleza em que ela confia.
23 O que guarda a boca e a língua guarda a sua alma das angústias.
24 Quanto ao soberbo e presumido, zombador é seu nome; procede com indignação e arrogância.
25 O preguiçoso morre desejando, porque as suas mãos recusam trabalhar.
26 O cobiçoso cobiça todo o dia, mas o justo dá e nada retém.
27 O sacrifício dos perversos já é abominação; quanto mais oferecendo-o com intenção maligna!
28 A testemunha falsa perecerá, mas a auricular falará sem ser contestada.
29 O homem perverso mostra dureza no rosto, mas o reto considera o seu caminho.
30 Não há sabedoria, nem inteligência, nem mesmo conselho contra o Senhor.
31 O cavalo prepara-se para o dia da batalha, mas a vitória vem do Senhor.*
1 Mais vale o bom nome do que as muitas riquezas; e o ser estimado é melhor do que a prata e o ouro.
2 O rico e o pobre se encontram; a um e a outro faz o Senhor.
3 O prudente vê o mal e esconde-se; mas os simples passam adiante e sofrem a pena.
4 O galardão da humildade e o temor do Senhor são riquezas, e honra, e vida.
5 Espinhos e laços há no caminho do perverso; o que guarda a sua alma retira-se para longe deles.
6 Ensina a criança no caminho em que deve andar, e, ainda quando for velho, não se desviará dele.
7 O rico domina sobre o pobre, e o que toma emprestado é servo do que empresta.
8 O que semeia a injustiça segará males; e a vara da sua indignação falhará.
9 O generoso será abençoado, porque dá do seu pão ao pobre.
10 Lança fora o escarnecedor, e com ele se irá a contenda; cessarão as demandas e a ignomínia.
11 O que ama a pureza do coração e é grácil no falar terá por amigo o rei.
12 Os olhos do Senhor conservam aquele que tem conhecimento, mas as palavras do iníquo ele transtornará.
13 Diz o preguiçoso: Um leão está lá fora; serei morto no meio das ruas.
14 Cova profunda é a boca da mulher estranha; aquele contra quem o Senhor se irar cairá nela.
15 A estultícia está ligada ao coração da criança, mas a vara da disciplina a afastará dela.
16 O que oprime ao pobre para enriquecer a si ou o que dá ao rico certamente empobrecerá.*
17 Inclina o ouvido, e ouve as palavras dos sábios, e aplica o coração ao meu conhecimento.
18 Porque é coisa agradável os guardares no teu coração e os aplicares todos aos teus lábios.
19 Para que a tua confiança esteja no Senhor, quero dar-te hoje a instrução, a ti mesmo.
20 Porventura, não te escrevi excelentes coisas acerca de conselhos e conhecimentos,
21 para mostrar-te a certeza das palavras da verdade, a fim de que possas responder claramente aos que te enviarem?
22 Não roubes ao pobre, porque é pobre, nem oprimas em juízo ao aflito,
23 porque o Senhor defenderá a causa deles e tirará a vida aos que os despojam.
24 Não te associes com o iracundo, nem andes com o homem colérico,
25 para que não aprendas as suas veredas e, assim, enlaces a tua alma.
26 Não estejas entre os que se comprometem e ficam por fiadores de dívidas,
27 pois, se não tens com que pagar, por que arriscas perder a cama de debaixo de ti?
28 Não removas os marcos antigos que puseram teus pais.
29 Vês a um homem perito na sua obra? Perante reis será posto; não entre a plebe.*
1 Quando te assentares a comer com um governador, atenta bem para aquele que está diante de ti;
2 mete uma faca à tua garganta, se és homem glutão.
3 Não cobices os seus delicados manjares, porque são comidas enganadoras.
4 Não te fatigues para seres rico; não apliques nisso a tua inteligência.
5 Porventura, fitarás os olhos naquilo que não é nada? Pois, certamente, a riqueza fará para si asas, como a águia que voa pelos céus.
6 Não comas o pão do invejoso, nem cobices os seus delicados manjares.
7 Porque, como imagina em sua alma, assim ele é; ele te diz: Come e bebe; mas o seu coração não está contigo.
8 Vomitarás o bocado que comeste e perderás as tuas suaves palavras.
9 Não fales aos ouvidos do insensato, porque desprezará a sabedoria das tuas palavras.
10 Não removas os marcos antigos, nem entres nos campos dos órfãos,
11 porque o seu Vingador é forte e lhes pleiteará a causa contra ti.
12 Aplica o coração ao ensino e os ouvidos às palavras do conhecimento.
13 Não retires da criança a disciplina, pois, se a fustigares com a vara, não morrerá.
14 Tu a fustigarás com a vara e livrarás a sua alma do inferno.
15 Filho meu, se o teu coração for sábio, alegrar-se-á também o meu;
16 exultará o meu íntimo, quando os teus lábios falarem coisas retas.
17 Não tenha o teu coração inveja dos pecadores; antes, no temor do Senhor perseverarás todo dia.
18 Porque deveras haverá bom futuro; não será frustrada a tua esperança.
19 Ouve, filho meu, e sê sábio; guia retamente no caminho o teu coração.
20 Não estejas entre os bebedores de vinho nem entre os comilões de carne.
21 Porque o beberrão e o comilão caem em pobreza; e a sonolência vestirá de trapos o homem.
22 Ouve a teu pai, que te gerou, e não desprezes a tua mãe, quando vier a envelhecer.
23 Compra a verdade e não a vendas; compra a sabedoria, a instrução e o entendimento.
24 Grandemente se regozijará o pai do justo, e quem gerar a um sábio nele se alegrará.
25 Alegrem-se teu pai e tua mãe, e regozije-se a que te deu à luz.
26 Dá-me, filho meu, o teu coração, e os teus olhos se agradem dos meus caminhos.
27 Pois cova profunda é a prostituta, poço estreito, a alheia.
28 Ela, como salteador, se põe a espreitar e multiplica entre os homens os infiéis.
29 Para quem são os ais? Para quem, os pesares? Para quem, as rixas? Para quem, as queixas? Para quem, as feridas sem causa? E para quem, os olhos vermelhos?
30 Para os que se demoram em beber vinho, para os que andam buscando bebida misturada.
31 Não olhes para o vinho, quando se mostra vermelho, quando resplandece no copo e se escoa suavemente.
32 Pois ao cabo morderá como a cobra e picará como o basilisco.
33 Os teus olhos verão coisas esquisitas, e o teu coração falará perversidades.
34 Serás como o que se deita no meio do mar e como o que se deita no alto do mastro
35 e dirás: Espancaram-me, e não me doeu; bateram-me, e não o senti; quando despertarei? Então, tornarei a beber.*
1 Não tenhas inveja dos homens malignos, nem queiras estar com eles,
2 porque o seu coração maquina violência, e os seus lábios falam para o mal.
3 Com a sabedoria edifica-se a casa, e com a inteligência ela se firma;
4 pelo conhecimento se encherão as câmaras de toda sorte de bens, preciosos e deleitáveis.
5 Mais poder tem o sábio do que o forte, e o homem de conhecimento, mais do que o robusto.
6 Com medidas de prudência farás a guerra; na multidão de conselheiros está a vitória.
7 A sabedoria é alta demais para o insensato; no juízo, a sua boca não terá palavra.
8 Ao que cuida em fazer o mal, mestre de intrigas lhe chamarão.
9 Os desígnios do insensato são pecado, e o escarnecedor é abominável aos homens.
10 Se te mostras fraco no dia da angústia, a tua força é pequena.
11 Livra os que estão sendo levados para a morte e salva os que cambaleiam indo para serem mortos.
12 Se disseres: Não o soubemos, não o perceberá aquele que pesa os corações? Não o saberá aquele que atenta para a tua alma? E não pagará ele ao homem segundo as suas obras?
13 Filho meu, saboreia o mel, porque é saudável, e o favo, porque é doce ao teu paladar.
14 Então, sabe que assim é a sabedoria para a tua alma; se a achares, haverá bom futuro, e não será frustrada a tua esperança.
15 Não te ponhas de emboscada, ó perverso, contra a habitação do justo, nem assoles o lugar do seu repouso,
16 porque sete vezes cairá o justo e se levantará; mas os perversos são derribados pela calamidade.
17 Quando cair o teu inimigo, não te alegres, e não se regozije o teu coração quando ele tropeçar;
18 para que o Senhor não veja isso, e lhe desagrade, e desvie dele a sua ira.
19 Não te aflijas por causa dos malfeitores, nem tenhas inveja dos perversos,
20 porque o maligno não terá bom futuro, e a lâmpada dos perversos se apagará.
21 Teme ao Senhor, filho meu, e ao rei e não te associes com os revoltosos.
22 Porque de repente levantará a sua perdição, e a ruína que virá daqueles dois, quem a conhecerá?
23 São também estes provérbios dos sábios. Parcialidade no julgar não é bom.
24 O que disser ao perverso: Tu és justo; pelo povo será maldito e detestado pelas nações.
25 Mas os que o repreenderem se acharão bem, e sobre eles virão grandes bênçãos.
26 Como beijo nos lábios, é a resposta com palavras retas.
27 Cuida dos teus negócios lá fora, apronta a lavoura no campo e, depois, edifica a tua casa.
28 Não sejas testemunha sem causa contra o teu próximo, nem o enganes com os teus lábios.
29 Não digas: Como ele me fez a mim, assim lhe farei a ele; pagarei a cada um segundo a sua obra.
30 Passei pelo campo do preguiçoso e junto à vinha do homem falto de entendimento;
31 eis que tudo estava cheio de espinhos, a sua superfície, coberta de urtigas, e o seu muro de pedra, em ruínas.
32 Tendo-o visto, considerei; vi e recebi a instrução.
33 Um pouco para dormir, um pouco para tosquenejar, um pouco para encruzar os braços em repouso,
34 assim sobrevirá a tua pobreza como um ladrão, e a tua necessidade, como um homem armado.*
1 São também estes provérbios de Salomão, os quais transcreveram os homens de Ezequias, rei de Judá.
2 A glória de Deus é encobrir as coisas, mas a glória dos reis é esquadrinhá-las.
3 Como a altura dos céus e a profundeza da terra, assim o coração dos reis é insondável.
4 Tira da prata a escória, e sairá vaso para o ourives;
5 tira o perverso da presença do rei, e o seu trono se firmará na justiça.
6 Não te glories na presença do rei, nem te ponhas no meio dos grandes;
7 porque melhor é que te digam: Sobe para aqui!, do que seres humilhado diante do príncipe. A respeito do que os teus olhos viram,
8 não te apresses a litigar, pois, ao fim, que farás, quando o teu próximo te puser em apuros?
9 Pleiteia a tua causa diretamente com o teu próximo e não descubras o segredo de outrem;
10 para que não te vitupere aquele que te ouvir, e não se te apegue a tua infâmia.
11 Como maçãs de ouro em salvas de prata, assim é a palavra dita a seu tempo.
12 Como pendentes e joias de ouro puro, assim é o sábio repreensor para o ouvido atento.
13 Como o frescor de neve no tempo da ceifa, assim é o mensageiro fiel para com os que o enviam, porque refrigera a alma dos seus senhores.
14 Como nuvens e ventos que não trazem chuva, assim é o homem que se gaba de dádivas que não fez.
15 A longanimidade persuade o príncipe, e a língua branda esmaga ossos.
16 Achaste mel? Come apenas o que te basta, para que não te fartes dele e venhas a vomitá-lo.
17 Não sejas frequente na casa do teu próximo, para que não se enfade de ti e te aborreça.
18 Maça, espada e flecha aguda é o homem que levanta falso testemunho contra o seu próximo.
19 Como dente quebrado e pé sem firmeza, assim é a confiança no desleal, no tempo da angústia.
20 Como quem se despe num dia de frio e como vinagre sobre feridas, assim é o que entoa canções junto ao coração aflito.
21 Se o que te aborrece tiver fome, dá-lhe pão para comer; se tiver sede, dá-lhe água para beber,
22 porque assim amontoarás brasas vivas sobre a sua cabeça, e o Senhor te retribuirá.
23 O vento norte traz chuva, e a língua fingida, o rosto irado.
24 Melhor é morar no canto do eirado do que junto com a mulher rixosa na mesma casa.
25 Como água fria para o sedento, tais são as boas-novas vindas de um país remoto.
26 Como fonte que foi turvada e manancial corrupto, assim é o justo que cede ao perverso.
27 Comer muito mel não é bom; assim, procurar a própria honra não é honra.
28 Como cidade derribada, que não tem muros, assim é o homem que não tem domínio próprio.*
1 Como a neve no verão e como a chuva na ceifa, assim, a honra não convém ao insensato.
2 Como o pássaro que foge, como a andorinha no seu voo, assim, a maldição sem causa não se cumpre.
3 O açoite é para o cavalo, o freio, para o jumento, e a vara, para as costas dos insensatos.
4 Não respondas ao insensato segundo a sua estultícia, para que não te faças semelhante a ele.
5 Ao insensato responde segundo a sua estultícia, para que não seja ele sábio aos seus próprios olhos.
6 Os pés corta e o dano sofre quem manda mensagens por intermédio do insensato.
7 As pernas do coxo pendem bambas; assim é o provérbio na boca dos insensatos.
8 Como o que atira pedra preciosa num montão de ruínas, assim é o que dá honra ao insensato.
9 Como galho de espinhos na mão do bêbado, assim é o provérbio na boca dos insensatos.
10 Como um flecheiro que a todos fere, assim é o que assalaria os insensatos e os transgressores.
11 Como o cão que torna ao seu vômito, assim é o insensato que reitera a sua estultícia.
12 Tens visto a um homem que é sábio a seus próprios olhos? Maior esperança há no insensato do que nele.
13 Diz o preguiçoso: Um leão está no caminho; um leão está nas ruas.
14 Como a porta se revolve nos seus gonzos, assim, o preguiçoso, no seu leito.
15 O preguiçoso mete a mão no prato e não quer ter o trabalho de a levar à boca.
16 Mais sábio é o preguiçoso a seus próprios olhos do que sete homens que sabem responder bem.
17 Quem se mete em questão alheia é como aquele que toma pelas orelhas um cão que passa.
18 Como o louco que lança fogo, flechas e morte,
19 assim é o homem que engana a seu próximo e diz: Fiz isso por brincadeira.
20 Sem lenha, o fogo se apaga; e, não havendo maldizente, cessa a contenda.
21 Como o carvão é para a brasa, e a lenha, para o fogo, assim é o homem contencioso para acender rixas.
22 As palavras do maldizente são comida fina, que desce para o mais interior do ventre.
23 Como vaso de barro coberto de escórias de prata, assim são os lábios amorosos e o coração maligno.
24 Aquele que aborrece dissimula com os lábios, mas no íntimo encobre o engano;
25 quando te falar suavemente, não te fies nele, porque sete abominações há no seu coração.
26 Ainda que o seu ódio se encobre com engano, a sua malícia se descobrirá publicamente.
27 Quem abre uma cova nela cairá; e a pedra rolará sobre quem a revolve.
28 A língua falsa aborrece a quem feriu, e a boca lisonjeira é causa de ruína.*
1 Não te glories do dia de amanhã, porque não sabes o que trará à luz.
2 Seja outro o que te louve, e não a tua boca; o estrangeiro, e não os teus lábios.
3 Pesada é a pedra, e a areia é uma carga; mas a ira do insensato é mais pesada do que uma e outra.
4 Cruel é o furor, e impetuosa, a ira, mas quem pode resistir à inveja?
5 Melhor é a repreensão franca do que o amor encoberto.
6 Leais são as feridas feitas pelo que ama, porém os beijos de quem odeia são enganosos.
7 A alma farta pisa o favo de mel, mas à alma faminta todo amargo é doce.
8 Qual ave que vagueia longe do seu ninho, tal é o homem que anda vagueando longe do seu lar.
9 Como o óleo e o perfume alegram o coração, assim, o amigo encontra doçura no conselho cordial.
10 Não abandones o teu amigo, nem o amigo de teu pai, nem entres na casa de teu irmão no dia da tua adversidade. Mais vale o vizinho perto do que o irmão longe.
11 Sê sábio, filho meu, e alegra o meu coração, para que eu saiba responder àqueles que me afrontam.
12 O prudente vê o mal e esconde-se; mas os simples passam adiante e sofrem a pena.
13 Tome-se a roupa àquele que fica fiador por outrem; e, por penhor, àquele que se obriga por mulher estranha.
14 O que bendiz ao seu vizinho em alta voz, logo de manhã, por maldição lhe atribuem o que faz.
15 O gotejar contínuo no dia de grande chuva e a mulher rixosa são semelhantes;
16 contê-la seria conter o vento, seria pegar o óleo na mão.
17 Como o ferro com o ferro se afia, assim, o homem, ao seu amigo.
18 O que trata da figueira comerá do seu fruto; e o que cuida do seu senhor será honrado.
19 Como na água o rosto corresponde ao rosto, assim, o coração do homem, ao homem.
20 O inferno e o abismo nunca se fartam, e os olhos do homem nunca se satisfazem.
21 Como o crisol prova a prata, e o forno, o ouro, assim, o homem é provado pelos louvores que recebe.
22 Ainda que pises o insensato com mão de gral entre grãos pilados de cevada, não se vai dele a sua estultícia.
23 Procura conhecer o estado das tuas ovelhas e cuida dos teus rebanhos,
24 porque as riquezas não duram para sempre, nem a coroa, de geração em geração.
25 Quando, removido o feno, aparecerem os renovos e se recolherem as ervas dos montes,
26 então, os cordeiros te darão as vestes, os bodes, o preço do campo,
27 e as cabras, leite em abundância para teu alimento, para alimento da tua casa e para sustento das tuas servas.*
1 Fogem os perversos, sem que ninguém os persiga; mas o justo é intrépido como o leão.
2 Por causa da transgressão da terra, mudam-se frequentemente os príncipes, mas por um, sábio e prudente, se faz estável a sua ordem.
3 O homem pobre que oprime os pobres é como chuva que a tudo arrasta e não deixa trigo.
4 Os que desamparam a lei louvam o perverso, mas os que guardam a lei se indignam contra ele.
5 Os homens maus não entendem o que é justo, mas os que buscam o Senhor entendem tudo.
6 Melhor é o pobre que anda na sua integridade do que o perverso, nos seus caminhos, ainda que seja rico.
7 O que guarda a lei é filho prudente, mas o companheiro de libertinos envergonha a seu pai.
8 O que aumenta os seus bens com juros e ganância ajunta-os para o que se compadece do pobre.
9 O que desvia os ouvidos de ouvir a lei, até a sua oração será abominável.
10 O que desvia os retos para o mau caminho, ele mesmo cairá na cova que fez, mas os íntegros herdarão o bem.
11 O homem rico é sábio aos seus próprios olhos; mas o pobre que é sábio sabe sondá-lo.
12 Quando triunfam os justos, há grande festividade; quando, porém, sobem os perversos, os homens se escondem.
13 O que encobre as suas transgressões jamais prosperará; mas o que as confessa e deixa alcançará misericórdia.
14 Feliz o homem constante no temor de Deus; mas o que endurece o coração cairá no mal.
15 Como leão que ruge e urso que ataca, assim é o perverso que domina sobre um povo pobre.
16 O príncipe falto de inteligência multiplica as opressões, mas o que aborrece a avareza viverá muitos anos.
17 O homem carregado do sangue de outrem fugirá até à cova; ninguém o detenha.
18 O que anda em integridade será salvo, mas o perverso em seus caminhos cairá logo.
19 O que lavra a sua terra virá a fartar-se de pão, mas o que se ajunta a vadios se fartará de pobreza.
20 O homem fiel será cumulado de bênçãos, mas o que se apressa a enriquecer não passará sem castigo.
21 Parcialidade não é bom, porque até por um bocado de pão o homem prevaricará.
22 Aquele que tem olhos invejosos corre atrás das riquezas, mas não sabe que há de vir sobre ele a penúria.
23 O que repreende ao homem achará, depois, mais favor do que aquele que lisonjeia com a língua.
24 O que rouba a seu pai ou a sua mãe e diz: Não é pecado, companheiro é do destruidor.
25 O cobiçoso levanta contendas, mas o que confia no Senhor prosperará.
26 O que confia no seu próprio coração é insensato, mas o que anda em sabedoria será salvo.
27 O que dá ao pobre não terá falta, mas o que dele esconde os olhos será cumulado de maldições.
28 Quando sobem os perversos, os homens se escondem, mas, quando eles perecem, os justos se multiplicam.*
1 O homem que muitas vezes repreendido endurece a cerviz será quebrantado de repente sem que haja cura.
2 Quando se multiplicam os justos, o povo se alegra, quando, porém, domina o perverso, o povo suspira.
3 O homem que ama a sabedoria alegra a seu pai, mas o companheiro de prostitutas desperdiça os bens.
4 O rei justo sustém a terra, mas o amigo de impostos a transtorna.
5 O homem que lisonjeia a seu próximo arma-lhe uma rede aos passos.
6 Na transgressão do homem mau, há laço, mas o justo canta e se regozija.
7 Informa-se o justo da causa dos pobres, mas o perverso de nada disso quer saber.
8 Os homens escarnecedores alvoroçam a cidade, mas os sábios desviam a ira.
9 Se o homem sábio discute com o insensato, quer este se encolerize, quer se ria, não haverá fim.
10 Os sanguinários aborrecem o íntegro, ao passo que, quanto aos retos, procuram tirar-lhes a vida.
11 O insensato expande toda a sua ira, mas o sábio afinal lha reprime.
12 Se o governador dá atenção a palavras mentirosas, virão a ser perversos todos os seus servos.
13 O pobre e o seu opressor se encontram, mas é o Senhor quem dá luz aos olhos de ambos.
14 O rei que julga os pobres com equidade firmará o seu trono para sempre.
15 A vara e a disciplina dão sabedoria, mas a criança entregue a si mesma vem a envergonhar a sua mãe.
16 Quando os perversos se multiplicam, multiplicam-se as transgressões, mas os justos verão a ruína deles.
17 Corrige o teu filho, e te dará descanso, dará delícias à tua alma.
18 Não havendo profecia, o povo se corrompe; mas o que guarda a lei, esse é feliz.
19 O servo não se emendará com palavras, porque, ainda que entenda, não obedecerá.
20 Tens visto um homem precipitado nas suas palavras? Maior esperança há para o insensato do que para ele.
21 Se alguém amimar o escravo desde a infância, por fim ele quererá ser filho.
22 O iracundo levanta contendas, e o furioso multiplica as transgressões.
23 A soberba do homem o abaterá, mas o humilde de espírito obterá honra.
24 O que tem parte com o ladrão aborrece a própria alma; ouve as maldições e nada denuncia.
25 Quem teme ao homem arma ciladas, mas o que confia no Senhor está seguro.
26 Muitos buscam o favor daquele que governa, mas para o homem a justiça vem do Senhor.
27 Para o justo, o iníquo é abominação, e o reto no seu caminho é abominação ao perverso.*
1 Palavras de Agur, filho de Jaque, de Massá. Disse o homem: Fatiguei-me, ó Deus; fatiguei-me, ó Deus, e estou exausto
2 porque sou demasiadamente estúpido para ser homem; não tenho inteligência de homem,
3 não aprendi a sabedoria, nem tenho o conhecimento do Santo.
4 Quem subiu ao céu e desceu? Quem encerrou os ventos nos seus punhos? Quem amarrou as águas na sua roupa? Quem estabeleceu todas as extremidades da terra? Qual é o seu nome, e qual é o nome de seu filho, se é que o sabes?
5 Toda palavra de Deus é pura; ele é escudo para os que nele confiam.
6 Nada acrescentes às suas palavras, para que não te repreenda, e sejas achado mentiroso.
7 Duas coisas te peço; não mas negues, antes que eu morra:
8 afasta de mim a falsidade e a mentira; não me dês nem a pobreza nem a riqueza; dá-me o pão que me for necessário;
9 para não suceder que, estando eu farto, te negue e diga: Quem é o Senhor? Ou que, empobrecido, venha a furtar e profane o nome de Deus.
10 Não calunies o servo diante de seu senhor, para que aquele te não amaldiçoe e fiques culpado.
11 Há daqueles que amaldiçoam a seu pai e que não bendizem a sua mãe.
12 Há daqueles que são puros aos próprios olhos e que jamais foram lavados da sua imundícia.
13 Há daqueles — quão altivos são os seus olhos e levantadas as suas pálpebras!
14 Há daqueles cujos dentes são espadas, e cujos queixais são facas, para consumirem na terra os aflitos e os necessitados entre os homens.
15 A sanguessuga tem duas filhas, a saber: Dá, Dá. Há três coisas que nunca se fartam, sim, quatro que não dizem: Basta!
16 Elas são a sepultura, a madre estéril, a terra, que se não farta de água, e o fogo, que nunca diz: Basta!
17 Os olhos de quem zomba do pai ou de quem despreza a obediência à sua mãe, corvos no ribeiro os arrancarão e pelos pintãos da águia serão comidos.
18 Há três coisas que são maravilhosas demais para mim, sim, há quatro que não entendo:
19 o caminho da águia no céu, o caminho da cobra na penha, o caminho do navio no meio do mar e o caminho do homem com uma donzela.
20 Tal é o caminho da mulher adúltera: come, e limpa a boca, e diz: Não cometi maldade.
21 Sob três coisas estremece a terra, sim, sob quatro não pode subsistir:
22 sob o servo quando se torna rei; sob o insensato quando anda farto de pão;
23 sob a mulher desdenhada quando se casa; sob a serva quando se torna herdeira da sua senhora.
24 Há quatro coisas mui pequenas na terra que, porém, são mais sábias que os sábios:
25 as formigas, povo sem força; todavia, no verão preparam a sua comida;
26 os arganazes, povo não poderoso; contudo, fazem a sua casa nas rochas;
27 os gafanhotos não têm rei; contudo, marcham todos em bandos;
28 o geco, que se apanha com as mãos; contudo, está nos palácios dos reis.
29 Há três que têm passo elegante, sim, quatro que andam airosamente:
30 O leão, o mais forte entre os animais, que por ninguém torna atrás;
31 o galo, que anda ereto, o bode e o rei, a quem não se pode resistir.
32 Se procedeste insensatamente em te exaltares ou se maquinaste o mal, põe a mão na boca.
33 Porque o bater do leite produz manteiga, e o torcer do nariz produz sangue, e o açular a ira produz contendas.*
1 Palavras do rei Lemuel, de Massá, as quais lhe ensinou sua mãe.
2 Que te direi, filho meu? Ó filho do meu ventre? Que te direi, ó filho dos meus votos?
3 Não dês às mulheres a tua força, nem os teus caminhos, às que destroem os reis.
4 Não é próprio dos reis, ó Lemuel, não é próprio dos reis beber vinho, nem dos príncipes desejar bebida forte.
5 Para que não bebam, e se esqueçam da lei, e pervertam o direito de todos os aflitos.
6 Dai bebida forte aos que perecem e vinho, aos amargurados de espírito;
7 para que bebam, e se esqueçam da sua pobreza, e de suas fadigas não se lembrem mais.
8 Abre a boca a favor do mudo, pelo direito de todos os que se acham desamparados.
9 Abre a boca, julga retamente e faze justiça aos pobres e aos necessitados.
O louvor da mulher virtuosa
10 Mulher virtuosa, quem a achará? O seu valor muito excede o de finas joias.
11 O coração do seu marido confia nela, e não haverá falta de ganho.
12 Ela lhe faz bem e não mal, todos os dias da sua vida.
13 Busca lã e linho e de bom grado trabalha com as mãos.
14 É como o navio mercante: de longe traz o seu pão.
15 É ainda noite, e já se levanta, e dá mantimento à sua casa e a tarefa às suas servas.
16 Examina uma propriedade e adquire-a; planta uma vinha com as rendas do seu trabalho.
17 Cinge os lombos de força e fortalece os braços.
18 Ela percebe que o seu ganho é bom; a sua lâmpada não se apaga de noite.
19 Estende as mãos ao fuso, mãos que pegam na roca.
20 Abre a mão ao aflito; e ainda a estende ao necessitado.
21 No tocante à sua casa, não teme a neve, pois todos andam vestidos de lã escarlate.
22 Faz para si cobertas, veste-se de linho fino e de púrpura.
23 Seu marido é estimado entre os juízes, quando se assenta com os anciãos da terra.
24 Ela faz roupas de linho fino, e vende-as, e dá cintas aos mercadores.
25 A força e a dignidade são os seus vestidos, e, quanto ao dia de amanhã, não tem preocupações.
26 Fala com sabedoria, e a instrução da bondade está na sua língua.
27 Atende ao bom andamento da sua casa e não come o pão da preguiça.
28 Levantam-se seus filhos e lhe chamam ditosa; seu marido a louva, dizendo:
29 Muitas mulheres procedem virtuosamente, mas tu a todas sobrepujas.
30 Enganosa é a graça, e vã, a formosura, mas a mulher que teme ao Senhor, essa será louvada.
31 Dai-lhe do fruto das suas mãos, e de público a louvarão as suas obras.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Provérbios','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)