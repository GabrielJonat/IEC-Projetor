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
1 Houve um homem de Ramataim-Zofim, da região montanhosa de Efraim, cujo nome era Elcana, filho de Jeroão, filho de Eliú, filho de Toú, filho de Zufe, efraimita.
2 Tinha ele duas mulheres: uma se chamava Ana, e a outra, Penina; Penina tinha filhos; Ana, porém, não os tinha.
3 Este homem subia da sua cidade de ano em ano a adorar e a sacrificar ao Senhor dos Exércitos, em Siló. Estavam ali os dois filhos de Eli, Hofni e Fineias, como sacerdotes do Senhor.
4 No dia em que Elcana oferecia o seu sacrifício, dava ele porções deste a Penina, sua mulher, e a todos os seus filhos e filhas.
5 A Ana, porém, dava porção dupla, porque ele a amava, ainda mesmo que o Senhor a houvesse deixado estéril.
6 (A sua rival a provocava excessivamente para a irritar, porquanto o Senhor lhe havia cerrado a madre.)
7 E assim o fazia ele de ano em ano; e, todas as vezes que Ana subia à Casa do Senhor, a outra a irritava; pelo que chorava e não comia.
8 Então, Elcana, seu marido, lhe disse: Ana, por que choras? E por que não comes? E por que estás de coração triste? Não te sou eu melhor do que dez filhos?
9 Após terem comido e bebido em Siló, estando Eli, o sacerdote, assentado numa cadeira, junto a um pilar do templo do Senhor,
10 levantou-se Ana, e, com amargura de alma, orou ao Senhor, e chorou abundantemente.
11 E fez um voto, dizendo: Senhor dos Exércitos, se benignamente atentares para a aflição da tua serva, e de mim te lembrares, e da tua serva te não esqueceres, e lhe deres um filho varão, ao Senhor o darei por todos os dias da sua vida, e sobre a sua cabeça não passará navalha.
12 Demorando-se ela no orar perante o Senhor, passou Eli a observar-lhe o movimento dos lábios,
13 porquanto Ana só no coração falava; seus lábios se moviam, porém não se lhe ouvia voz nenhuma; por isso, Eli a teve por embriagada
14 e lhe disse: Até quando estarás tu embriagada? Aparta de ti esse vinho!
15 Porém Ana respondeu: Não, senhor meu! Eu sou mulher atribulada de espírito; não bebi nem vinho nem bebida forte; porém venho derramando a minha alma perante o Senhor.
16 Não tenhas, pois, a tua serva por filha de Belial; porque pelo excesso da minha ansiedade e da minha aflição é que tenho falado até agora.
17 Então, lhe respondeu Eli: Vai-te em paz, e o Deus de Israel te conceda a petição que lhe fizeste.
18 E disse ela: Ache a tua serva mercê diante de ti. Assim, a mulher se foi seu caminho e comeu, e o seu semblante já não era triste.
19 Levantaram-se de madrugada, e adoraram perante o Senhor, e voltaram, e chegaram a sua casa, a Ramá. Elcana coabitou com Ana, sua mulher, e, lembrando-se dela o Senhor,
20 ela concebeu e, passado o devido tempo, teve um filho, a que chamou Samuel, pois dizia: Do Senhor o pedi.
21 Subiu Elcana, seu marido, com toda a sua casa, a oferecer ao Senhor o sacrifício anual e a cumprir o seu voto.
22 Ana, porém, não subiu e disse a seu marido: Quando for o menino desmamado, levá-lo-ei para ser apresentado perante o Senhor e para lá ficar para sempre.
23 Respondeu-lhe Elcana, seu marido: Faze o que melhor te agrade; fica até que o desmames; tão somente confirme o Senhor a sua palavra. Assim, ficou a mulher e criou o filho ao peito, até que o desmamou.
24 Havendo-o desmamado, levou-o consigo, com um novilho de três anos, um efa de farinha e um odre de vinho, e o apresentou à Casa do Senhor, a Siló. Era o menino ainda muito criança.
25 Imolaram o novilho e trouxeram o menino a Eli.
26 E disse ela: Ah! Meu senhor, tão certo como vives, eu sou aquela mulher que aqui esteve contigo, orando ao Senhor.
27 Por este menino orava eu; e o Senhor me concedeu a petição que eu lhe fizera.
28 Pelo que também o trago como devolvido ao Senhor, por todos os dias que viver; pois do Senhor o pedi. E eles adoraram ali o Senhor.*
1 Então, orou Ana e disse: O meu coração se regozija no Senhor, a minha força está exaltada no Senhor; a minha boca se ri dos meus inimigos, porquanto me alegro na tua salvação.
2 Não há santo como o Senhor; porque não há outro além de ti; e Rocha não há, nenhuma, como o nosso Deus.
3 Não multipliqueis palavras de orgulho, nem saiam coisas arrogantes da vossa boca; porque o Senhor é o Deus da sabedoria e pesa todos os feitos na balança.
4 O arco dos fortes é quebrado, porém os débeis, cingidos de força.
5 Os que antes eram fartos hoje se alugam por pão, mas os que andavam famintos não sofrem mais fome; até a estéril tem sete filhos, e a que tinha muitos filhos perde o vigor.
6 O Senhor é o que tira a vida e a dá; faz descer à sepultura e faz subir.
7 O Senhor empobrece e enriquece; abaixa e também exalta.
8 Levanta o pobre do pó e, desde o monturo, exalta o necessitado, para o fazer assentar entre os príncipes, para o fazer herdar o trono de glória; porque do Senhor são as colunas da terra, e assentou sobre elas o mundo.
9 Ele guarda os pés dos seus santos, porém os perversos emudecem nas trevas da morte; porque o homem não prevalece pela força.
10 Os que contendem com o Senhor são quebrantados; dos céus troveja contra eles. O Senhor julga as extremidades da terra, dá força ao seu rei e exalta o poder do seu ungido.
11 Então, Elcana foi-se a Ramá, a sua casa; porém o menino ficou servindo ao Senhor, perante o sacerdote Eli.
12 Eram, porém, os filhos de Eli filhos de Belial e não se importavam com o Senhor;
13 pois o costume daqueles sacerdotes com o povo era que, oferecendo alguém sacrifício, vinha o moço do sacerdote, estando-se cozendo a carne, com um garfo de três dentes na mão;
14 e metia-o na caldeira, ou na panela, ou no tacho, ou na marmita, e tudo quanto o garfo tirava o sacerdote tomava para si; assim se fazia a todo o Israel que ia ali, a Siló.
15 Também, antes de se queimar a gordura, vinha o moço do sacerdote e dizia ao homem que sacrificava: Dá essa carne para assar ao sacerdote; porque não aceitará de ti carne cozida, senão crua.
16 Se o ofertante lhe respondia: Queime-se primeiro a gordura, e, depois, tomarás quanto quiseres, então, ele lhe dizia: Não, porém hás de ma dar agora; se não, tomá-la-ei à força.
17 Era, pois, mui grande o pecado destes moços perante o Senhor, porquanto eles desprezavam a oferta do Senhor.
18 Samuel ministrava perante o Senhor, sendo ainda menino, vestido de uma estola sacerdotal de linho.
19 Sua mãe lhe fazia uma túnica pequena e, de ano em ano, lha trazia quando, com seu marido, subia a oferecer o sacrifício anual.
20 Eli abençoava a Elcana e a sua mulher e dizia: O Senhor te dê filhos desta mulher, em lugar do filho que devolveu ao Senhor. E voltavam para a sua casa.
21 Abençoou, pois, o Senhor a Ana, e ela concebeu e teve três filhos e duas filhas; e o jovem Samuel crescia diante do Senhor.
22 Era, porém, Eli já muito velho e ouvia tudo quanto seus filhos faziam a todo o Israel e de como se deitavam com as mulheres que serviam à porta da tenda da congregação.
23 E disse-lhes: Por que fazeis tais coisas? Pois de todo este povo ouço constantemente falar do vosso mau procedimento.
24 Não, filhos meus, porque não é boa fama esta que ouço; estais fazendo transgredir o povo do Senhor.
25 Pecando o homem contra o próximo, Deus lhe será o árbitro; pecando, porém, contra o Senhor, quem intercederá por ele? Entretanto, não ouviram a voz de seu pai, porque o Senhor os queria matar.
26 Mas o jovem Samuel crescia em estatura e no favor do Senhor e dos homens.
27 Veio um homem de Deus a Eli e lhe disse: Assim diz o Senhor: Não me manifestei, na verdade, à casa de teu pai, estando os israelitas ainda no Egito, na casa de Faraó?
28 Eu o escolhi dentre todas as tribos de Israel para ser o meu sacerdote, para subir ao meu altar, para queimar o incenso e para trazer a estola sacerdotal perante mim; e dei à casa de teu pai todas as ofertas queimadas dos filhos de Israel.
29 Por que pisais aos pés os meus sacrifícios e as minhas ofertas de manjares, que ordenei se me fizessem na minha morada? E, tu, por que honras a teus filhos mais do que a mim, para tu e eles vos engordardes das melhores de todas as ofertas do meu povo de Israel?
30 Portanto, diz o Senhor, Deus de Israel: Na verdade, dissera eu que a tua casa e a casa de teu pai andariam diante de mim perpetuamente; porém, agora, diz o Senhor: Longe de mim tal coisa, porque aos que me honram, honrarei, porém os que me desprezam serão desmerecidos.
31 Eis que vêm dias em que cortarei o teu braço e o braço da casa de teu pai, para que não haja mais velho nenhum em tua casa.
32 E verás o aperto da morada de Deus, a um tempo com o bem que fará a Israel; e jamais haverá velho em tua casa.
33 O homem, porém, da tua linhagem a quem eu não afastar do meu altar será para te consumir os olhos e para te entristecer a alma; e todos os descendentes da tua casa morrerão na flor da idade.
34 Ser-te-á por sinal o que sobrevirá a teus dois filhos, a Hofni e Fineias: ambos morrerão no mesmo dia.
35 Então, suscitarei para mim um sacerdote fiel, que procederá segundo o que tenho no coração e na mente; edificar-lhe-ei uma casa estável, e andará ele diante do meu ungido para sempre.
36 Será que todo aquele que restar da tua casa virá a inclinar-se diante dele, para obter uma moeda de prata e um bocado de pão, e dirá: Rogo-te que me admitas a algum dos cargos sacerdotais, para ter um pedaço de pão, que coma.*
1 O jovem Samuel servia ao Senhor, perante Eli. Naqueles dias, a palavra do Senhor era mui rara; as visões não eram frequentes.
2 Certo dia, estando deitado no lugar costumado o sacerdote Eli, cujos olhos já começavam a escurecer-se, a ponto de não poder ver,
3 e tendo-se deitado também Samuel, no templo do Senhor, em que estava a arca, antes que a lâmpada de Deus se apagasse,
4 o Senhor chamou o menino: Samuel, Samuel! Este respondeu: Eis-me aqui!
5 Correu a Eli e disse: Eis-me aqui, pois tu me chamaste. Mas ele disse: Não te chamei; torna a deitar-te. Ele se foi e se deitou.
6 Tornou o Senhor a chamar: Samuel! Este se levantou, foi a Eli e disse: Eis-me aqui, pois tu me chamaste. Mas ele disse: Não te chamei, meu filho, torna a deitar-te.
7 Porém Samuel ainda não conhecia o Senhor, e ainda não lhe tinha sido manifestada a palavra do Senhor.
8 O Senhor, pois, tornou a chamar a Samuel, terceira vez, e ele se levantou, e foi a Eli, e disse: Eis-me aqui, pois tu me chamaste. Então, entendeu Eli que era o Senhor quem chamava o jovem.
9 Por isso, Eli disse a Samuel: Vai deitar-te; se alguém te chamar, dirás: Fala, Senhor, porque o teu servo ouve. E foi Samuel para o seu lugar e se deitou.
10 Então, veio o Senhor, e ali esteve, e chamou como das outras vezes: Samuel, Samuel! Este respondeu: Fala, porque o teu servo ouve.
11 Disse o Senhor a Samuel: Eis que vou fazer uma coisa em Israel, a qual todo o que a ouvir lhe tinirão ambos os ouvidos.
12 Naquele dia, suscitarei contra Eli tudo quanto tenho falado com respeito à sua casa; começarei e o cumprirei.
13 Porque já lhe disse que julgarei a sua casa para sempre, pela iniquidade que ele bem conhecia, porque seus filhos se fizeram execráveis, e ele os não repreendeu.
14 Portanto, jurei à casa de Eli que nunca lhe será expiada a iniquidade, nem com sacrifício, nem com oferta de manjares.
15 Ficou Samuel deitado até pela manhã e, então, abriu as portas da Casa do Senhor; porém temia relatar a visão a Eli.
16 Chamou Eli a Samuel e disse: Samuel, meu filho! Ele respondeu: Eis-me aqui!
17 Então, ele disse: Que é que o Senhor te falou? Peço-te que mo não encubras; assim Deus te faça o que bem lhe aprouver se me encobrires alguma coisa de tudo o que te falou.
18 Então, Samuel lhe referiu tudo e nada lhe encobriu. E disse Eli: É o Senhor; faça o que bem lhe aprouver.
19 Crescia Samuel, e o Senhor era com ele, e nenhuma de todas as suas palavras deixou cair em terra.
20 Todo o Israel, desde Dã até Berseba, conheceu que Samuel estava confirmado como profeta do Senhor.
21 Continuou o Senhor a aparecer em Siló, enquanto por sua palavra o Senhor se manifestava ali a Samuel.*
1 Veio a palavra de Samuel a todo o Israel. Israel saiu à peleja contra os filisteus e se acampou junto a Ebenézer; e os filisteus se acamparam junto a Afeca.
2 Dispuseram-se os filisteus em ordem de batalha, para sair de encontro a Israel; e, travada a peleja, Israel foi derrotado pelos filisteus; e estes mataram, no campo aberto, cerca de quatro mil homens.
3 Voltando o povo ao arraial, disseram os anciãos de Israel: Por que nos feriu o Senhor, hoje, diante dos filisteus? Tragamos de Siló a arca da Aliança do Senhor, para que venha no meio de nós e nos livre das mãos de nossos inimigos.
4 Mandou, pois, o povo trazer de Siló a arca do Senhor dos Exércitos, entronizado entre os querubins; os dois filhos de Eli, Hofni e Fineias, estavam ali com a arca da Aliança de Deus.
5 Sucedeu que, vindo a arca da Aliança do Senhor ao arraial, rompeu todo o Israel em grandes brados, e ressoou a terra.
6 Ouvindo os filisteus a voz do júbilo, disseram: Que voz de grande júbilo é esta no arraial dos hebreus? Então, souberam que a arca do Senhor era vinda ao arraial.
7 E se atemorizaram os filisteus e disseram: Os deuses vieram ao arraial. E diziam mais: Ai de nós! Que tal jamais sucedeu antes.
8 Ai de nós! Quem nos livrará das mãos destes grandiosos deuses? São os deuses que feriram aos egípcios com toda sorte de pragas no deserto.
9 Sede fortes, ó filisteus! Portai-vos varonilmente, para que não venhais a ser escravos dos hebreus, como eles serviram a vós outros! Portai-vos varonilmente e pelejai!
10 Então, pelejaram os filisteus; Israel foi derrotado, e cada um fugiu para a sua tenda; foi grande a derrota, pois foram mortos de Israel trinta mil homens de pé.
11 Foi tomada a arca de Deus, e mortos os dois filhos de Eli, Hofni e Fineias.
12 Então, correu um homem de Benjamim, saído das fileiras, e, no mesmo dia, chegou a Siló; trazia rasgadas as vestes e terra sobre a cabeça.
13 Quando chegou, Eli estava assentado numa cadeira, ao pé do caminho, olhando como quem espera, porque o seu coração estava tremendo pela arca de Deus. Depois de entrar o homem na cidade e dar as novas, toda a cidade prorrompeu em gritos.
14 Eli, ouvindo os gritos, perguntou: Que alvoroço é esse? Então, se apressou o homem e, vindo, deu as notícias a Eli.
15 Era Eli da idade de noventa e oito anos; os seus olhos tinham cegado, e já não podia ver.
16 Disse o homem a Eli: Eu sou o que saí das fileiras e delas fugi hoje mesmo. Perguntou-lhe Eli: Que sucedeu, meu filho?
17 Então, respondeu o que trazia as novas e disse: Israel fugiu de diante dos filisteus, houve grande morticínio entre o povo, e também os teus dois filhos, Hofni e Fineias, foram mortos, e a arca de Deus foi tomada.
18 Ao fazer ele menção da arca de Deus, caiu Eli da cadeira para trás, junto ao portão, e quebrou-se-lhe o pescoço, e morreu, porque era já homem velho e pesado; e havia ele julgado a Israel quarenta anos.
19 Estando sua nora, a mulher de Fineias, grávida, e próximo o parto, ouvindo estas novas, de que a arca de Deus fora tomada e de que seu sogro e seu marido morreram, encurvou-se e deu à luz; porquanto as dores lhe sobrevieram.
20 Ao expirar, disseram as mulheres que a assistiam: Não temas, pois tiveste um filho. Ela, porém, não respondeu, nem fez caso disso.
21 Mas chamou ao menino Icabô, dizendo: Foi-se a glória de Israel. Isto ela disse, porque a arca de Deus fora tomada e por causa de seu sogro e de seu marido.
22 E falou mais: Foi-se a glória de Israel, pois foi tomada a arca de Deus.*
1 Os filisteus tomaram a arca de Deus e a levaram de Ebenézer a Asdode.
2 Tomaram os filisteus a arca de Deus e a meteram na casa de Dagom, junto a este.
3 Levantando-se, porém, de madrugada os de Asdode, no dia seguinte, eis que estava caído Dagom com o rosto em terra, diante da arca do Senhor; tomaram-no e tornaram a pô-lo no seu lugar.
4 Levantando-se de madrugada no dia seguinte, pela manhã, eis que Dagom jazia caído de bruços diante da arca do Senhor; a cabeça de Dagom e as duas mãos estavam cortadas sobre o limiar; dele ficara apenas o tronco.
5 Por isso, os sacerdotes de Dagom e todos os que entram no seu templo não lhe pisam o limiar em Asdode, até ao dia de hoje.
6 Porém a mão do Senhor castigou duramente os de Asdode, e os assolou, e os feriu de tumores, tanto em Asdode como no seu território.
7 Vendo os homens de Asdode que assim era, disseram: Não fique conosco a arca do Deus de Israel; pois a sua mão é dura sobre nós e sobre Dagom, nosso deus.
8 Pelo que enviaram mensageiros, e congregaram a si todos os príncipes dos filisteus, e disseram: Que faremos da arca do Deus de Israel? Responderam: Seja levada a arca do Deus de Israel até Gate e, depois, de cidade em cidade. E a levaram até Gate.
9 Depois de a terem levado, a mão do Senhor foi contra aquela cidade, com mui grande terror; pois feriu os homens daquela cidade, desde o pequeno até ao grande; e lhes nasceram tumores.
10 Então, enviaram a arca de Deus a Ecrom. Sucedeu, porém, que, em lá chegando, os ecronitas exclamaram, dizendo: Transportaram até nós a arca do Deus de Israel, para nos matarem, a nós e ao nosso povo.
11 Então, enviaram mensageiros, e congregaram a todos os príncipes dos filisteus, e disseram: Devolvei a arca do Deus de Israel, e torne para o seu lugar, para que não mate nem a nós nem ao nosso povo. Porque havia terror de morte em toda a cidade, e a mão de Deus castigara duramente ali.
12 Os homens que não morriam eram atingidos com os tumores; e o clamor da cidade subiu até ao céu.*
1 Sete meses esteve a arca do Senhor na terra dos filisteus.
2 Estes chamaram os sacerdotes e os adivinhadores e lhes disseram: Que faremos da arca do Senhor? Fazei-nos saber como a devolveremos para o seu lugar.
3 Responderam eles: Quando enviardes a arca do Deus de Israel, não a envieis vazia, porém enviá-la-eis a seu Deus com uma oferta pela culpa; então, sereis curados e sabereis por que a sua mão se não tira de vós.
4 Então, disseram: Qual será a oferta pela culpa que lhe havemos de apresentar? Responderam: Segundo o número dos príncipes dos filisteus, cinco tumores de ouro e cinco ratos de ouro, porquanto a praga é uma e a mesma sobre todos vós e sobre todos os vossos príncipes.
5 Fazei umas imitações dos vossos tumores e dos vossos ratos, que andam destruindo a terra, e dai glória ao Deus de Israel; porventura, aliviará a sua mão de cima de vós, e do vosso deus, e da vossa terra.
6 Por que, pois, endureceríeis o coração, como os egípcios e Faraó endureceram o coração? Porventura, depois de os haverem tratado tão mal, não os deixaram ir, e eles não se foram?
7 Agora, pois, fazei um carro novo, tomai duas vacas com crias, sobre as quais não se pôs ainda jugo, e atai-as ao carro; seus bezerros, levá-los-eis para casa.
8 Então, tomai a arca do Senhor, e ponde-a sobre o carro, e metei num cofre, ao seu lado, as figuras de ouro que lhe haveis de entregar como oferta pela culpa; e deixai-a ir.
9 Reparai: se subir pelo caminho rumo do seu território a Bete-Semes, foi ele que nos fez este grande mal; e, se não, saberemos que não foi a sua mão que nos feriu; foi casual o que nos sucedeu.
10 Assim fizeram aqueles homens, e tomaram duas vacas com crias, e as ataram ao carro, e os seus bezerros encerraram em casa.
11 Puseram a arca do Senhor sobre o carro, como também o cofre com os ratos de ouro e com as imitações dos tumores.
12 As vacas se encaminharam diretamente para Bete-Semes e, andando e berrando, seguiam sempre por esse mesmo caminho, sem se desviarem nem para a direita nem para a esquerda; os príncipes dos filisteus foram atrás delas, até ao território de Bete-Semes.
13 Andavam os de Bete-Semes fazendo a sega do trigo no vale e, levantando os olhos, viram a arca; e, vendo-a, se alegraram.
14 O carro veio ao campo de Josué, o bete-semita, e parou ali, onde havia uma grande pedra; fenderam a madeira do carro e ofereceram as vacas ao Senhor, em holocausto.
15 Os levitas desceram a arca do Senhor, como também o cofre que estava junto a ela, em que estavam as obras de ouro, e os puseram sobre a grande pedra. No mesmo dia, os homens de Bete-Semes ofereceram holocaustos e imolaram sacrifícios ao Senhor.
16 Viram aquilo os cinco príncipes dos filisteus e voltaram para Ecrom no mesmo dia.
17 São estes, pois, os tumores de ouro que enviaram os filisteus ao Senhor como oferta pela culpa: por Asdode, um; por Gaza, outro; por Asquelom, outro; por Gate, outro; por Ecrom, outro;
18 como também os ratos de ouro, segundo o número de todas as cidades dos filisteus, pertencentes aos cinco príncipes, desde as cidades fortes até às aldeias campestres. A grande pedra, sobre a qual puseram a arca do Senhor, está até ao dia de hoje no campo de Josué, o bete-semita.
19 Feriu o Senhor os homens de Bete-Semes, porque olharam para dentro da arca do Senhor, sim, feriu deles setenta homens; então, o povo chorou, porquanto o Senhor fizera tão grande morticínio entre eles.
20 Então, disseram os homens de Bete-Semes: Quem poderia estar perante o Senhor, este Deus santo? E para quem subirá desde nós?
21 Enviaram, pois, mensageiros aos habitantes de Quiriate-Jearim, dizendo: Os filisteus devolveram a arca do Senhor; descei, pois, e fazei-a subir para vós outros.*
1 Então, vieram os homens de Quiriate-Jearim e levaram a arca do Senhor à casa de Abinadabe, no outeiro; e consagraram Eleazar, seu filho, para que guardasse a arca do Senhor.
2 Sucedeu que, desde aquele dia, a arca ficou em Quiriate-Jearim, e tantos dias se passaram, que chegaram a vinte anos; e toda a casa de Israel dirigia lamentações ao Senhor.
3 Falou Samuel a toda a casa de Israel, dizendo: Se é de todo o vosso coração que voltais ao Senhor, tirai dentre vós os deuses estranhos e os astarotes, e preparai o coração ao Senhor, e servi a ele só, e ele vos livrará das mãos dos filisteus.
4 Então, os filhos de Israel tiraram dentre si os baalins e os astarotes e serviram só ao Senhor.
5 Disse mais Samuel: Congregai todo o Israel em Mispa, e orarei por vós ao Senhor.
6 Congregaram-se em Mispa, tiraram água e a derramaram perante o Senhor; jejuaram aquele dia e ali disseram: Pecamos contra o Senhor. E Samuel julgou os filhos de Israel em Mispa.
7 Quando, pois, os filisteus ouviram que os filhos de Israel estavam congregados em Mispa, subiram os príncipes dos filisteus contra Israel; o que ouvindo os filhos de Israel, tiveram medo dos filisteus.
8 Então, disseram os filhos de Israel a Samuel: Não cesses de clamar ao Senhor, nosso Deus, por nós, para que nos livre da mão dos filisteus.
9 Tomou, pois, Samuel um cordeiro que ainda mamava e o sacrificou em holocausto ao Senhor; clamou Samuel ao Senhor por Israel, e o Senhor lhe respondeu.
10 Enquanto Samuel oferecia o holocausto, os filisteus chegaram à peleja contra Israel; mas trovejou o Senhor aquele dia com grande estampido sobre os filisteus e os aterrou de tal modo, que foram derrotados diante dos filhos de Israel.
11 Saindo de Mispa os homens de Israel, perseguiram os filisteus e os derrotaram até abaixo de Bete-Car.
12 Tomou, então, Samuel uma pedra, e a pôs entre Mispa e Sem, e lhe chamou Ebenézer, e disse: Até aqui nos ajudou o Senhor.
13 Assim, os filisteus foram abatidos e nunca mais vieram ao território de Israel, porquanto foi a mão do Senhor contra eles todos os dias de Samuel.
14 As cidades que os filisteus haviam tomado a Israel foram-lhe restituídas, desde Ecrom até Gate; e até os territórios delas arrebatou Israel das mãos dos filisteus. E houve paz entre Israel e os amorreus.
15 E julgou Samuel todos os dias de sua vida a Israel.
16 De ano em ano, fazia uma volta, passando por Betel, Gilgal e Mispa; e julgava a Israel em todos esses lugares.
17 Porém voltava a Ramá, porque sua casa estava ali, onde julgava a Israel e onde edificou um altar ao Senhor.*
1 Tendo Samuel envelhecido, constituiu seus filhos por juízes sobre Israel.
2 O primogênito chamava-se Joel, e o segundo, Abias; e foram juízes em Berseba.
3 Porém seus filhos não andaram pelos caminhos dele; antes, se inclinaram à avareza, e aceitaram subornos, e perverteram o direito.
4 Então, os anciãos todos de Israel se congregaram, e vieram a Samuel, a Ramá,
5 e lhe disseram: Vê, já estás velho, e teus filhos não andam pelos teus caminhos; constitui-nos, pois, agora, um rei sobre nós, para que nos governe, como o têm todas as nações.
6 Porém esta palavra não agradou a Samuel, quando disseram: Dá-nos um rei, para que nos governe. Então, Samuel orou ao Senhor.
7 Disse o Senhor a Samuel: Atende à voz do povo em tudo quanto te diz, pois não te rejeitou a ti, mas a mim, para eu não reinar sobre ele.
8 Segundo todas as obras que fez desde o dia em que o tirei do Egito até hoje, pois a mim me deixou, e a outros deuses serviu, assim também o faz a ti.
9 Agora, pois, atende à sua voz, porém adverte-o solenemente e explica-lhe qual será o direito do rei que houver de reinar sobre ele.
10 Referiu Samuel todas as palavras do Senhor ao povo, que lhe pedia um rei,
11 e disse: Este será o direito do rei que houver de reinar sobre vós: ele tomará os vossos filhos e os empregará no serviço dos seus carros e como seus cavaleiros, para que corram adiante deles;
12 e os porá uns por capitães de mil e capitães de cinquenta; outros para lavrarem os seus campos e ceifarem as suas messes; e outros para fabricarem suas armas de guerra e o aparelhamento de seus carros.
13 Tomará as vossas filhas para perfumistas, cozinheiras e padeiras.
14 Tomará o melhor das vossas lavouras, e das vossas vinhas, e dos vossos olivais e o dará aos seus servidores.
15 As vossas sementeiras e as vossas vinhas dizimará, para dar aos seus oficiais e aos seus servidores.
16 Também tomará os vossos servos, e as vossas servas, e os vossos melhores jovens, e os vossos jumentos e os empregará no seu trabalho.
17 Dizimará o vosso rebanho, e vós lhe sereis por servos.
18 Então, naquele dia, clamareis por causa do vosso rei que houverdes escolhido; mas o Senhor não vos ouvirá naquele dia.
19 Porém o povo não atendeu à voz de Samuel e disse: Não! Mas teremos um rei sobre nós.
20 Para que sejamos também como todas as nações; o nosso rei poderá governar-nos, sair adiante de nós e fazer as nossas guerras.
21 Ouvindo, pois, Samuel todas as palavras do povo, as repetiu perante o Senhor.
22 Então, o Senhor disse a Samuel: Atende à sua voz e estabelece-lhe um rei. Samuel disse aos filhos de Israel: Volte cada um para sua cidade.*
1 Havia um homem de Benjamim, cujo nome era Quis, filho de Abiel, filho de Zeror, filho de Becorate, filho de Afias, benjamita, homem de bens.
2 Tinha ele um filho cujo nome era Saul, moço e tão belo, que entre os filhos de Israel não havia outro mais belo do que ele; desde os ombros para cima, sobressaía a todo o povo.
3 Extraviaram-se as jumentas de Quis, pai de Saul. Disse Quis a Saul, seu filho: Toma agora contigo um dos moços, dispõe-te e vai procurar as jumentas.
4 Então, atravessando a região montanhosa de Efraim e a terra de Salisa, não as acharam; depois, passaram à terra de Saalim; porém elas não estavam ali; passaram ainda à terra de Benjamim; todavia, não as acharam.
5 Vindo eles, então, à terra de Zufe, Saul disse para o seu moço, com quem ele ia: Vem, e voltemos; não suceda que meu pai deixe de preocupar-se com as jumentas e se aflija por causa de nós.
6 Porém ele lhe disse: Nesta cidade há um homem de Deus, e é muito estimado; tudo quanto ele diz sucede; vamo-nos, agora, lá; mostrar-nos-á, porventura, o caminho que devemos seguir.
7 Então, Saul disse ao seu moço: Eis, porém, se lá formos, que levaremos, então, àquele homem? Porque o pão de nossos alforjes se acabou, e presente não temos que levar ao homem de Deus. Que temos?
8 O moço tornou a responder a Saul e disse: Eis que tenho ainda em mãos um quarto de siclo de prata, o qual darei ao homem de Deus, para que nos mostre o caminho.
9 (Antigamente, em Israel, indo alguém consultar a Deus, dizia: Vinde, vamos ter com o vidente; porque ao profeta de hoje, antigamente, se chamava vidente.)
10 Então, disse Saul ao moço: Dizes bem; anda, pois, vamos. E foram-se à cidade onde estava o homem de Deus.
11 Subindo eles pela encosta da cidade, encontraram umas moças que saíam a tirar água e lhes perguntaram: Está aqui o vidente?
12 Elas responderam: Está. Eis aí o tens diante de ti; apressa-te, pois, porque, hoje, veio à cidade; porquanto o povo oferece, hoje, sacrifício no alto.
13 Entrando vós na cidade, logo o achareis, antes que suba ao alto para comer; porque o povo não comerá enquanto ele não chegar, porque ele tem de abençoar o sacrifício, e só depois comem os convidados; subi, pois, agora, que, hoje, o achareis.
14 Subiram, pois, à cidade; ao entrarem, eis que Samuel lhes saiu ao encontro, para subir ao alto.
15 Ora, o Senhor, um dia antes de Saul chegar, o revelara a Samuel, dizendo:
16 Amanhã a estas horas, te enviarei um homem da terra de Benjamim, o qual ungirás por príncipe sobre o meu povo de Israel, e ele livrará o meu povo das mãos dos filisteus; porque atentei para o meu povo, pois o seu clamor chegou a mim.
17 Quando Samuel viu a Saul, o Senhor lhe disse: Eis o homem de quem eu já te falara. Este dominará sobre o meu povo.
18 Saul se chegou a Samuel no meio da porta e disse: Mostra-me, peço-te, onde é aqui a casa do vidente.
19 Samuel respondeu a Saul e disse: Eu sou o vidente; sobe adiante de mim ao alto; hoje, comereis comigo. Pela manhã, te despedirei e tudo quanto está no teu coração to declararei.
20 Quanto às jumentas que há três dias se te perderam, não se preocupe o teu coração com elas, porque já se encontraram. E para quem está reservado tudo o que é precioso em Israel? Não é para ti e para toda a casa de teu pai?
21 Então, respondeu Saul e disse: Porventura, não sou benjamita, da menor das tribos de Israel? E a minha família, a menor de todas as famílias da tribo de Benjamim? Por que, pois, me falas com tais palavras?
22 Samuel, tomando a Saul e ao seu moço, levou-os à sala de jantar e lhes deu o lugar de honra entre os convidados, que eram cerca de trinta pessoas.
23 Então, disse Samuel ao cozinheiro: Traze a porção que te dei, de que te disse: Põe-na à parte contigo.
24 Tomou, pois, o cozinheiro a coxa com o que havia nela e a pôs diante de Saul. Disse Samuel: Eis que isto é o que foi reservado; toma-o e come, pois se guardou para ti para esta ocasião, ao dizer eu: Convidei o povo. Assim, comeu Saul com Samuel naquele dia.
25 Tendo descido do alto para a cidade, falou Samuel com Saul sobre o eirado.
26 Levantaram-se de madrugada; e, quase ao subir da alva, chamou Samuel a Saul ao eirado, dizendo: Levanta-te; eu irei contigo para te encaminhar. Levantou-se Saul, e saíram ambos, ele e Samuel.
27 Desciam eles para a extremidade da cidade, quando Samuel disse a Saul: Dize ao moço que passe adiante de nós, e tu, tendo ele passado, espera, que te farei saber a palavra de Deus.*
1 Tomou Samuel um vaso de azeite, e lho derramou sobre a cabeça, e o beijou, e disse: Não te ungiu, porventura, o Senhor por príncipe sobre a sua herança, o povo de Israel?
2 Quando te apartares, hoje, de mim, acharás dois homens junto ao sepulcro de Raquel, no território de Benjamim, em Zelza, os quais te dirão: Acharam-se as jumentas que foste procurar, e eis que teu pai já não pensa no caso delas e se aflige por causa de vós, dizendo: Que farei eu por meu filho?
3 Quando dali passares adiante e chegares ao carvalho de Tabor, ali te encontrarão três homens, que vão subindo a Deus a Betel: um levando três cabritos; outro, três bolos de pão, e o outro, um odre de vinho.
4 Eles te saudarão e te darão dois pães, que receberás da sua mão.
5 Então, seguirás a Gibeá-Eloim, onde está a guarnição dos filisteus; e há de ser que, entrando na cidade, encontrarás um grupo de profetas que descem do alto, precedidos de saltérios, e tambores, e flautas, e harpas, e eles estarão profetizando.
6 O Espírito do Senhor se apossará de ti, e profetizarás com eles e tu serás mudado em outro homem.
7 Quando estes sinais te sucederem, faze o que a ocasião te pedir, porque Deus é contigo.
8 Tu, porém, descerás adiante de mim a Gilgal, e eis que eu descerei a ti, para sacrificar holocausto e para apresentar ofertas pacíficas; sete dias esperarás, até que eu venha ter contigo e te declare o que hás de fazer.
9 Sucedeu, pois, que, virando-se ele para despedir-se de Samuel, Deus lhe mudou o coração; e todos esses sinais se deram naquele mesmo dia.
10 Chegando eles a Gibeá, eis que um grupo de profetas lhes saiu ao encontro; o Espírito de Deus se apossou de Saul, e ele profetizou no meio deles.
11 Todos os que, dantes, o conheciam, vendo que ele profetizava com os profetas, diziam uns aos outros: Que é isso que sucedeu ao filho de Quis? Está também Saul entre os profetas?
12 Então, um homem respondeu: Pois quem é o pai deles? Pelo que se tornou em provérbio: Está também Saul entre os profetas?
13 E, tendo profetizado, seguiu para o alto.
14 Perguntou o tio de Saul, a ele e ao seu moço: Aonde fostes? Respondeu ele: A buscar as jumentas e, vendo que não apareciam, fomos a Samuel.
15 Então, disse o tio de Saul: Conta-me, peço-te, que é o que vos disse Samuel?
16 Respondeu Saul a seu tio: Informou-nos de que as jumentas foram encontradas. Porém, com respeito ao reino, de que Samuel falara, não lho declarou.
17 Convocou Samuel o povo ao Senhor, em Mispa,
18 e disse aos filhos de Israel: Assim diz o Senhor, Deus de Israel: Fiz subir a Israel do Egito e livrei-vos das mãos dos egípcios e das mãos de todos os reinos que vos oprimiam.
19 Mas vós rejeitastes, hoje, a vosso Deus, que vos livrou de todos os vossos males e trabalhos, e lhe dissestes: Não! Mas constitui um rei sobre nós. Agora, pois, ponde-vos perante o Senhor, pelas vossas tribos e pelos vossos grupos de milhares.
20 Tendo Samuel feito chegar todas as tribos, foi indicada por sorte a de Benjamim.
21 Tendo feito chegar a tribo de Benjamim pelas suas famílias, foi indicada a família de Matri; e dela foi indicado Saul, filho de Quis. Mas, quando o procuraram, não podia ser encontrado.
22 Então, tornaram a perguntar ao Senhor se aquele homem viera ali. Respondeu o Senhor: Está aí escondido entre a bagagem.
23 Correram e o tomaram dali. Estando ele no meio do povo, era o mais alto e sobressaía de todo o povo do ombro para cima.
24 Então, disse Samuel a todo o povo: Vedes a quem o Senhor escolheu? Pois em todo o povo não há nenhum semelhante a ele. Então, todo o povo rompeu em gritos, exclamando: Viva o rei!
25 Declarou Samuel ao povo o direito do reino, escreveu-o num livro e o pôs perante o Senhor. Então, despediu Samuel todo o povo, cada um para sua casa.
26 Também Saul se foi para sua casa, a Gibeá; e foi com ele uma tropa de homens cujo coração Deus tocara.
27 Mas os filhos de Belial disseram: Como poderá este homem salvar-nos? E o desprezaram e não lhe trouxeram presentes. Porém Saul se fez de surdo.*
1 Então, subiu Naás, amonita, e sitiou a Jabes-Gileade; e disseram todos os homens de Jabes a Naás: Faze aliança conosco, e te serviremos.
2 Porém Naás, amonita, lhes respondeu: Farei aliança convosco sob a condição de vos serem vazados os olhos direitos, trazendo assim eu vergonha sobre todo o Israel.
3 Então, os anciãos de Jabes lhe disseram: Concede-nos sete dias, para que enviemos mensageiros por todos os limites de Israel e, não havendo ninguém que nos livre, então, nos entregaremos a ti.
4 Chegando os mensageiros a Gibeá de Saul, relataram este caso ao povo. Então, todo o povo chorou em voz alta.
5 Eis que Saul voltava do campo, atrás dos bois, e perguntou: Que tem o povo, que chora? Então, lhe referiram as palavras dos homens de Jabes.
6 E o Espírito de Deus se apossou de Saul, quando ouviu estas palavras, e acendeu-se sobremodo a sua ira.
7 Tomou uma junta de bois, cortou-os em pedaços e os enviou a todos os territórios de Israel por intermédio de mensageiros que dissessem: Assim se fará aos bois de todo aquele que não seguir a Saul e a Samuel. Então, caiu o temor do Senhor sobre o povo, e saíram como um só homem.
8 Contou-os em Bezeque; dos filhos de Israel, havia trezentos mil; dos homens de Judá, trinta mil.
9 Então, disseram aos mensageiros que tinham vindo: Assim direis aos homens de Jabes-Gileade: Amanhã, quando aquentar o sol, sereis socorridos. Vindo, pois, os mensageiros, e, anunciando-o aos homens de Jabes, estes se alegraram
10 e disseram aos amonitas: Amanhã, nos entregaremos a vós outros; então, nos fareis segundo o que melhor vos parecer.
11 Sucedeu que, ao outro dia, Saul dividiu o povo em três companhias, que, pela vigília da manhã, vieram para o meio do arraial e feriram a Amom, até que se fez sentir o calor do dia. Os sobreviventes se espalharam, e não ficaram dois deles juntos.
12 Então, disse o povo a Samuel: Quem são aqueles que diziam: Reinará Saul sobre nós? Trazei-os para aqui, para que os matemos.
13 Porém Saul disse: Hoje, ninguém será morto, porque, no dia de hoje, o Senhor salvou a Israel.
14 Disse Samuel ao povo: Vinde, vamos a Gilgal e renovemos ali o reino.
15 E todo o povo partiu para Gilgal, onde proclamaram Saul seu rei, perante o Senhor, a cuja presença trouxeram ofertas pacíficas; e Saul muito se alegrou ali com todos os homens de Israel.*
1 Então, disse Samuel a todo o Israel: Eis que ouvi a vossa voz em tudo quanto me dissestes e constituí sobre vós um rei.
2 Agora, pois, eis que tendes o rei à vossa frente. Já envelheci e estou cheio de cãs, e meus filhos estão convosco; o meu procedimento esteve diante de vós desde a minha mocidade até ao dia de hoje.
3 Eis-me aqui, testemunhai contra mim perante o Senhor e perante o seu ungido: de quem tomei o boi? De quem tomei o jumento? A quem defraudei? A quem oprimi? E das mãos de quem aceitei suborno para encobrir com ele os meus olhos? E vo-lo restituirei.
4 Então, responderam: Em nada nos defraudaste, nem nos oprimiste, nem tomaste coisa alguma das mãos de ninguém.
5 E ele lhes disse: O Senhor é testemunha contra vós outros, e o seu ungido é, hoje, testemunha de que nada tendes achado nas minhas mãos. E o povo confirmou: Deus é testemunha.
6 Então, disse Samuel ao povo: Testemunha é o Senhor, que escolheu a Moisés e a Arão e tirou vossos pais da terra do Egito.
7 Agora, pois, ponde-vos aqui, e pleitearei convosco perante o Senhor, relativamente a todos os seus atos de justiça que fez a vós outros e a vossos pais.
8 Havendo entrado Jacó no Egito, clamaram vossos pais ao Senhor, e o Senhor enviou a Moisés e a Arão, que os tiraram do Egito e os fizeram habitar neste lugar.
9 Porém esqueceram-se do Senhor, seu Deus; então, os entregou nas mãos de Sísera, comandante do exército de Hazor, e nas mãos dos filisteus, e nas mãos do rei de Moabe, que pelejaram contra eles.
10 E clamaram ao Senhor e disseram: Pecamos, pois deixamos o Senhor e servimos aos baalins e astarotes; agora, pois, livra-nos das mãos de nossos inimigos, e te serviremos.
11 O Senhor enviou a Jerubaal, e a Baraque, e a Jefté, e a Samuel; e vos livrou das mãos de vossos inimigos em redor, e habitastes em segurança.
12 Vendo vós que Naás, rei dos filhos de Amom, vinha contra vós outros, me dissestes: Não! Mas reinará sobre nós um rei; ao passo que o Senhor, vosso Deus, era o vosso rei.
13 Agora, pois, eis aí o rei que elegestes e que pedistes; e eis que o Senhor vos deu um rei.
14 Se temerdes ao Senhor, e o servirdes, e lhe atenderdes à voz, e não lhe fordes rebeldes ao mandado, e seguirdes o Senhor, vosso Deus, tanto vós como o vosso rei que governa sobre vós, bem será.
15 Se, porém, não derdes ouvidos à voz do Senhor, mas, antes, fordes rebeldes ao seu mandado, a mão do Senhor será contra vós outros, como o foi contra vossos pais.
16 Ponde-vos também, agora, aqui e vede esta grande coisa que o Senhor fará diante dos vossos olhos.
17 Não é, agora, o tempo da sega do trigo? Clamarei, pois, ao Senhor, e dará trovões e chuva; e sabereis e vereis que é grande a vossa maldade, que tendes praticado perante o Senhor, pedindo para vós outros um rei.
18 Então, invocou Samuel ao Senhor, e o Senhor deu trovões e chuva naquele dia; pelo que todo o povo temeu em grande maneira ao Senhor e a Samuel.
19 Todo o povo disse a Samuel: Roga pelos teus servos ao Senhor, teu Deus, para que não venhamos a morrer; porque a todos os nossos pecados acrescentamos o mal de pedir para nós um rei.
20 Então, disse Samuel ao povo: Não temais; tendes cometido todo este mal; no entanto, não vos desvieis de seguir o Senhor, mas servi ao Senhor de todo o vosso coração.
21 Não vos desvieis; pois seguiríeis coisas vãs, que nada aproveitam e tampouco vos podem livrar, porque vaidade são.
22 Pois o Senhor, por causa do seu grande nome, não desamparará o seu povo, porque aprouve ao Senhor fazer-vos o seu povo.
23 Quanto a mim, longe de mim que eu peque contra o Senhor, deixando de orar por vós; antes, vos ensinarei o caminho bom e direito.
24 Tão somente, pois, temei ao Senhor e servi-o fielmente de todo o vosso coração; pois vede quão grandiosas coisas vos fez.
25 Se, porém, perseverardes em fazer o mal, perecereis, tanto vós como o vosso rei.*
1 Um ano reinara Saul em Israel. No segundo ano de seu reinado sobre o povo,
2 escolheu para si três mil homens de Israel; estavam com Saul dois mil em Micmás e na região montanhosa de Betel, e mil estavam com Jônatas em Gibeá de Benjamim; e despediu o resto do povo, cada um para sua casa.
3 Jônatas derrotou a guarnição dos filisteus que estava em Gibeá, o que os filisteus ouviram; pelo que Saul fez tocar a trombeta por toda a terra, dizendo: Ouçam isso os hebreus.
4 Todo o Israel ouviu dizer: Saul derrotou a guarnição dos filisteus, e também Israel se fez odioso aos filisteus. Então, o povo foi convocado para junto de Saul, em Gilgal.
5 Reuniram-se os filisteus para pelejar contra Israel: trinta mil carros, e seis mil cavaleiros, e povo em multidão como a areia que está à beira-mar; e subiram e se acamparam em Micmás, ao oriente de Bete-Áven.
6 Vendo, pois, os homens de Israel que estavam em apuros (porque o povo estava apertado), esconderam-se pelas cavernas, e pelos buracos, e pelos penhascos, e pelos túmulos, e pelas cisternas.
7 Também alguns dos hebreus passaram o Jordão para a terra de Gade e Gileade; e o povo que permaneceu com Saul, estando este ainda em Gilgal, se encheu de temor.
8 Esperou Saul sete dias, segundo o prazo determinado por Samuel; não vindo, porém, Samuel a Gilgal, o povo se foi espalhando dali.
9 Então, disse Saul: Trazei-me aqui o holocausto e ofertas pacíficas. E ofereceu o holocausto.
10 Mal acabara ele de oferecer o holocausto, eis que chega Samuel; Saul lhe saiu ao encontro, para o saudar.
11 Samuel perguntou: Que fizeste? Respondeu Saul: Vendo que o povo se ia espalhando daqui, e que tu não vinhas nos dias aprazados, e que os filisteus já se tinham ajuntado em Micmás,
12 eu disse comigo: Agora, descerão os filisteus contra mim a Gilgal, e ainda não obtive a benevolência do Senhor; e, forçado pelas circunstâncias, ofereci holocaustos.
13 Então, disse Samuel a Saul: Procedeste nesciamente em não guardar o mandamento que o Senhor, teu Deus, te ordenou; pois teria, agora, o Senhor confirmado o teu reino sobre Israel para sempre.
14 Já agora não subsistirá o teu reino. O Senhor buscou para si um homem que lhe agrada e já lhe ordenou que seja príncipe sobre o seu povo, porquanto não guardaste o que o Senhor te ordenou.
15 Então, se levantou Samuel e subiu de Gilgal a Gibeá de Benjamim. Logo, Saul contou o povo que se achava com ele, cerca de seiscentos homens.
16 Saul, e Jônatas, seu filho, e o povo que se achava com eles ficaram em Geba de Benjamim; porém os filisteus se acamparam em Micmás.
17 Os saqueadores saíram do campo dos filisteus em três tropas; uma delas tomou o caminho de Ofra à terra de Sual;
18 outra tomou o caminho de Bete-Horom; e a terceira, o caminho a cavaleiro do vale de Zeboim, na direção do deserto.
19 Ora, em toda a terra de Israel nem um ferreiro se achava, porque os filisteus tinham dito: Para que os hebreus não façam espada, nem lança.
20 Pelo que todo o Israel tinha de descer aos filisteus para amolar a relha do seu arado, e a sua enxada, e o seu machado, e a sua foice.
21 Os filisteus cobravam dos israelitas dois terços de um siclo para amolar os fios das relhas e das enxadas e um terço de um siclo para amolar machados e aguilhadas.
22 Sucedeu que, no dia da peleja, não se achou nem espada, nem lança na mão de nenhum do povo que estava com Saul e com Jônatas; porém se acharam com Saul e com Jônatas, seu filho.
23 Saiu a guarnição dos filisteus ao desfiladeiro de Micmás.*
1 Sucedeu que, um dia, disse Jônatas, filho de Saul, ao seu jovem escudeiro: Vem, passemos à guarnição dos filisteus, que está do outro lado. Porém não o fez saber a seu pai.
2 Saul se encontrava na extremidade de Gibeá, debaixo da romeira em Migrom; e o povo que estava com ele eram cerca de seiscentos homens.
3 Aías, filho de Aitube, irmão de Icabô, filho de Fineias, filho de Eli, sacerdote do Senhor em Siló, trazia a estola sacerdotal. O povo não sabia que Jônatas tinha ido.
4 Entre os desfiladeiros pelos quais Jônatas procurava passar à guarnição dos filisteus, deste lado havia uma penha íngreme, e do outro, outra; uma se chamava Bozez; a outra, Sené.
5 Uma delas se erguia ao norte, defronte de Micmás; a outra, ao sul, defronte de Geba.
6 Disse, pois, Jônatas ao seu escudeiro: Vem, passemos à guarnição destes incircuncisos; porventura, o Senhor nos ajudará nisto, porque para o Senhor nenhum impedimento há de livrar com muitos ou com poucos.
7 Então, o seu escudeiro lhe disse: Faze tudo segundo inclinar o teu coração; eis-me aqui contigo, a tua disposição será a minha.
8 Disse, pois, Jônatas: Eis que passaremos àqueles homens e nos daremos a conhecer a eles.
9 Se nos disserem assim: Parai até que cheguemos a vós outros; então, ficaremos onde estamos e não subiremos a eles.
10 Porém se disserem: Subi a nós; então, subiremos, pois o Senhor no-los entregou nas mãos. Isto nos servirá de sinal.
11 Dando-se, pois, ambos a conhecer à guarnição dos filisteus, disseram estes: Eis que já os hebreus estão saindo dos buracos em que se tinham escondido.
12 Os homens da guarnição responderam a Jônatas e ao seu escudeiro e disseram: Subi a nós, e nós vos daremos uma lição. Disse Jônatas ao escudeiro: Sobe atrás de mim, porque o Senhor os entregou nas mãos de Israel.
13 Então, trepou Jônatas de gatinhas, e o seu escudeiro, atrás; e os filisteus caíram diante de Jônatas, e o seu escudeiro os matava atrás dele.
14 Sucedeu esta primeira derrota, em que Jônatas e o seu escudeiro mataram perto de vinte homens, em cerca de meia jeira de terra.
15 Houve grande espanto no arraial, no campo e em todo o povo; também a mesma guarnição e os saqueadores tremeram, e até a terra se estremeceu; e tudo passou a ser um terror de Deus.
16 Olharam as sentinelas de Saul, em Gibeá de Benjamim, e eis que a multidão se dissolvia, correndo uns para cá, outros para lá.
17 Então, disse Saul ao povo que estava com ele: Ora, contai e vede quem é que saiu dentre nós. Contaram, e eis que nem Jônatas nem o seu escudeiro estavam ali.
18 Saul disse a Aías: Traze aqui a arca de Deus (porque, naquele dia, ela estava com os filhos de Israel).
19 Enquanto Saul falava ao sacerdote, o alvoroço que havia no arraial dos filisteus crescia mais e mais, pelo que disse Saul ao sacerdote: Desiste de trazer a arca.
20 Então, Saul e todo o povo que estava com ele se ajuntaram e vieram à peleja; e a espada de um era contra o outro, e houve mui grande tumulto.
21 Também com os filisteus dantes havia hebreus, que subiram com eles ao arraial; e também estes se ajuntaram com os israelitas que estavam com Saul e Jônatas.
22 Ouvindo, pois, todos os homens de Israel que se esconderam pela região montanhosa de Efraim que os filisteus fugiram, eles também os perseguiram de perto na peleja.
23 Assim, livrou o Senhor a Israel naquele dia; e a batalha passou além de Bete-Áven.
24 Estavam os homens de Israel angustiados naquele dia, porquanto Saul conjurara o povo, dizendo: Maldito o homem que comer pão antes de anoitecer, para que me vingue de meus inimigos. Pelo que todo o povo se absteve de provar pão.
25 Todo o povo chegou a um bosque onde havia mel no chão.
26 Chegando o povo ao bosque, eis que corria mel; porém ninguém chegou a mão à boca, porque o povo temia a conjuração.
27 Jônatas, porém, não tinha ouvido quando seu pai conjurara o povo, e estendeu a ponta da vara que tinha na mão, e a molhou no favo de mel; e, levando a mão à boca, tornaram a brilhar os seus olhos.
28 Então, respondeu um do povo: Teu pai conjurou solenemente o povo e disse: Maldito o homem que, hoje, comer pão; estava exausto o povo.
29 Então, disse Jônatas: Meu pai turbou a terra; ora, vede como brilham os meus olhos por ter eu provado um pouco deste mel.
30 Quanto mais se o povo, hoje, tivesse comido livremente do que encontrou do despojo de seus inimigos; porém desta vez não foi tão grande a derrota dos filisteus.
31 Feriram, porém, aquele dia aos filisteus, desde Micmás até Aijalom. O povo se achava exausto em extremo;
32 e, lançando-se ao despojo, tomaram ovelhas, bois e bezerros, e os mataram no chão, e os comeram com sangue.
33 Disto informaram a Saul, dizendo: Eis que o povo peca contra o Senhor, comendo com sangue. Disse ele: Procedestes aleivosamente; rolai para aqui, hoje, uma grande pedra.
34 Disse mais Saul: Espalhai-vos entre o povo e dizei-lhe: Cada um me traga o seu boi, a sua ovelha, e matai-os aqui, e comei, e não pequeis contra o Senhor, comendo com sangue. Então, todo o povo trouxe de noite, cada um o seu boi de que já lançara mão, e os mataram ali.
35 Edificou Saul um altar ao Senhor; este foi o primeiro altar que lhe edificou.
36 Disse mais Saul: Desçamos esta noite no encalço dos filisteus, e despojemo-los, até o raiar do dia, e não deixemos de resto um homem sequer deles. E disseram: Faze tudo o que bem te parecer.
37 Disse, porém, o sacerdote: Cheguemo-nos aqui a Deus. Então, consultou Saul a Deus, dizendo: Descerei no encalço dos filisteus? Entregá-los-ás nas mãos de Israel? Porém aquele dia Deus não lhe respondeu.
38 Então, disse Saul: Chegai-vos para aqui, todos os chefes do povo, e informai-vos, e vede qual o pecado que, hoje, se cometeu.
39 Porque tão certo como vive o Senhor, que salva a Israel, ainda que com meu filho Jônatas esteja a culpa, seja morto. Porém nenhum de todo o povo lhe respondeu.
40 Disse mais a todo o Israel: Vós estareis de um lado, e eu e meu filho Jônatas, do outro. Então, disse o povo a Saul: Faze o que bem te parecer.
41 Falou, pois, Saul ao Senhor, Deus de Israel: Mostra a verdade. Então, Jônatas e Saul foram indicados por sorte, e o povo saiu livre.
42 Disse Saul: Lançai a sorte entre mim e Jônatas, meu filho. E foi indicado Jônatas.
43 Disse, então, Saul a Jônatas: Declara-me o que fizeste. E Jônatas lhe disse: Tão somente provei um pouco de mel com a ponta da vara que tinha na mão. Eis-me aqui; estou pronto para morrer.
44 Então, disse Saul: Deus me faça o que bem lhe aprouver; é certo que morrerás, Jônatas.
45 Porém o povo disse a Saul: Morrerá Jônatas, que efetuou tamanha salvação em Israel? Tal não suceda. Tão certo como vive o Senhor, não lhe há de cair no chão um só cabelo da cabeça! Pois foi com Deus que fez isso, hoje. Assim, o povo salvou a Jônatas, para que não morresse.
46 E Saul deixou de perseguir os filisteus; e estes se foram para a sua terra.
47 Tendo Saul assumido o reinado de Israel, pelejou contra todos os seus inimigos em redor: contra Moabe, os filhos de Amom e Edom; contra os reis de Zobá e os filisteus; e, para onde quer que se voltava, era vitorioso.
48 Houve-se varonilmente, e feriu os amalequitas, e libertou a Israel das mãos dos que o saqueavam.
49 Os filhos de Saul eram Jônatas, Isvi e Malquisua; os nomes de suas duas filhas eram: o da mais velha, Merabe; o da mais nova, Mical.
50 A mulher de Saul chamava-se Ainoã, filha de Aimaás. O nome do general do seu exército, Abner, filho de Ner, tio de Saul.
51 Quis era pai de Saul; e Ner, pai de Abner, era filho de Abiel.
52 Por todos os dias de Saul, houve forte guerra contra os filisteus; pelo que Saul, a todos os homens fortes e valentes que via, os agregava a si.*
1 Disse Samuel a Saul: Enviou-me o Senhor a ungir-te rei sobre o seu povo, sobre Israel; atenta, pois, agora, às palavras do Senhor.
2 Assim diz o Senhor dos Exércitos: Castigarei Amaleque pelo que fez a Israel: ter-se oposto a Israel no caminho, quando este subia do Egito.
3 Vai, pois, agora, e fere a Amaleque, e destrói totalmente a tudo o que tiver, e nada lhe poupes; porém matarás homem e mulher, meninos e crianças de peito, bois e ovelhas, camelos e jumentos.
4 Saul convocou o povo e os contou em Telaim: duzentos mil homens de pé e dez mil homens de Judá.
5 Chegando, pois, Saul à cidade de Amaleque, pôs emboscadas no vale.
6 E disse aos queneus: Ide-vos, retirai-vos e saí do meio dos amalequitas, para que eu vos não destrua juntamente com eles, porque usastes de misericórdia para com todos os filhos de Israel, quando subiram do Egito. Assim, os queneus se retiraram do meio dos amalequitas.
7 Então, feriu Saul os amalequitas, desde Havilá até chegar a Sur, que está defronte do Egito.
8 Tomou vivo a Agague, rei dos amalequitas; porém a todo o povo destruiu a fio de espada.
9 E Saul e o povo pouparam Agague, e o melhor das ovelhas e dos bois, e os animais gordos, e os cordeiros, e o melhor que havia e não os quiseram destruir totalmente; porém toda coisa vil e desprezível destruíram.
10 Então, veio a palavra do Senhor a Samuel, dizendo:
11 Arrependo-me de haver constituído Saul rei, porquanto deixou de me seguir e não executou as minhas palavras. Então, Samuel se contristou e toda a noite clamou ao Senhor.
12 Madrugou Samuel para encontrar a Saul pela manhã; e anunciou-se àquele: Já chegou Saul ao Carmelo, e eis que levantou para si um monumento; e, dando volta, passou e desceu a Gilgal.
13 Veio, pois, Samuel a Saul, e este lhe disse: Bendito sejas tu do Senhor; executei as palavras do Senhor.
14 Então, disse Samuel: Que balido, pois, de ovelhas é este nos meus ouvidos e o mugido de bois que ouço?
15 Respondeu Saul: De Amaleque os trouxeram; porque o povo poupou o melhor das ovelhas e dos bois, para os sacrificar ao Senhor, teu Deus; o resto, porém, destruímos totalmente.
16 Então, disse Samuel a Saul: Espera, e te declararei o que o Senhor me disse esta noite. Respondeu-lhe Saul: Fala.
17 Prosseguiu Samuel: Porventura, sendo tu pequeno aos teus olhos, não foste por cabeça das tribos de Israel, e não te ungiu o Senhor rei sobre ele?
18 Enviou-te o Senhor a este caminho e disse: Vai, e destrói totalmente estes pecadores, os amalequitas, e peleja contra eles, até exterminá-los.
19 Por que, pois, não atentaste à voz do Senhor, mas te lançaste ao despojo e fizeste o que era mau aos olhos do Senhor?
20 Então, disse Saul a Samuel: Pelo contrário, dei ouvidos à voz do Senhor e segui o caminho pelo qual o Senhor me enviou; e trouxe a Agague, rei de Amaleque, e os amalequitas, os destruí totalmente;
21 mas o povo tomou do despojo ovelhas e bois, o melhor do designado à destruição para oferecer ao Senhor, teu Deus, em Gilgal.
22 Porém Samuel disse: Tem, porventura, o Senhor tanto prazer em holocaustos e sacrifícios quanto em que se obedeça à sua palavra? Eis que o obedecer é melhor do que o sacrificar, e o atender, melhor do que a gordura de carneiros.
23 Porque a rebelião é como o pecado de feitiçaria, e a obstinação é como a idolatria e culto a ídolos do lar. Visto que rejeitaste a palavra do Senhor, ele também te rejeitou a ti, para que não sejas rei.
24 Então, disse Saul a Samuel: Pequei, pois transgredi o mandamento do Senhor e as tuas palavras; porque temi o povo e dei ouvidos à sua voz.
25 Agora, pois, te rogo, perdoa-me o meu pecado e volta comigo, para que adore o Senhor.
26 Porém Samuel disse a Saul: Não tornarei contigo; visto que rejeitaste a palavra do Senhor, já ele te rejeitou a ti, para que não sejas rei sobre Israel.
27 Virando-se Samuel para se ir, Saul o segurou pela orla do manto, e este se rasgou.
28 Então, Samuel lhe disse: O Senhor rasgou, hoje, de ti o reino de Israel e o deu ao teu próximo, que é melhor do que tu.
29 Também a Glória de Israel não mente, nem se arrepende, porquanto não é homem, para que se arrependa.
30 Então, disse Saul: Pequei; honra-me, porém, agora, diante dos anciãos do meu povo e diante de Israel; e volta comigo, para que adore o Senhor, teu Deus.
31 Então, Samuel seguiu a Saul, e este adorou o Senhor.
32 Disse Samuel: Traze-me aqui Agague, rei dos amalequitas. Agague veio a ele, confiante; e disse: Certamente, já se foi a amargura da morte.
33 Disse, porém, Samuel: Assim como a tua espada desfilhou mulheres, assim desfilhada ficará tua mãe entre as mulheres. E Samuel despedaçou a Agague perante o Senhor, em Gilgal.
34 Então, Samuel se foi a Ramá; e Saul subiu à sua casa, a Gibeá de Saul.
35 Nunca mais viu Samuel a Saul até ao dia da sua morte; porém tinha pena de Saul. O Senhor se arrependeu de haver constituído Saul rei sobre Israel.*
1 Disse o Senhor a Samuel: Até quando terás pena de Saul, havendo-o eu rejeitado, para que não reine sobre Israel? Enche um chifre de azeite e vem; enviar-te-ei a Jessé, o belemita; porque, dentre os seus filhos, me provi de um rei.
2 Disse Samuel: Como irei eu? Pois Saul o saberá e me matará. Então, disse o Senhor: Toma contigo um novilho e dize: Vim para sacrificar ao Senhor.
3 Convidarás Jessé para o sacrifício; eu te mostrarei o que hás de fazer, e ungir-me-ás a quem eu te designar.
4 Fez, pois, Samuel o que dissera o Senhor e veio a Belém. Saíram-lhe ao encontro os anciãos da cidade, tremendo, e perguntaram: É de paz a tua vinda?
5 Respondeu ele: É de paz; vim sacrificar ao Senhor. Santificai-vos e vinde comigo ao sacrifício. Santificou ele a Jessé e os seus filhos e os convidou para o sacrifício.
6 Sucedeu que, entrando eles, viu a Eliabe e disse consigo: Certamente, está perante o Senhor o seu ungido.
7 Porém o Senhor disse a Samuel: Não atentes para a sua aparência, nem para a sua altura, porque o rejeitei; porque o Senhor não vê como vê o homem. O homem vê o exterior, porém o Senhor, o coração.
8 Então, chamou Jessé a Abinadabe e o fez passar diante de Samuel, o qual disse: Nem a este escolheu o Senhor.
9 Então, Jessé fez passar a Samá, porém Samuel disse: Tampouco a este escolheu o Senhor.
10 Assim, fez passar Jessé os seus sete filhos diante de Samuel; porém Samuel disse a Jessé: O Senhor não escolheu estes.
11 Perguntou Samuel a Jessé: Acabaram-se os teus filhos? Ele respondeu: Ainda falta o mais moço, que está apascentando as ovelhas. Disse, pois, Samuel a Jessé: Manda chamá-lo, pois não nos assentaremos à mesa sem que ele venha.
12 Então, mandou chamá-lo e fê-lo entrar. Era ele ruivo, de belos olhos e boa aparência. Disse o Senhor: Levanta-te e unge-o, pois este é ele.
13 Tomou Samuel o chifre do azeite e o ungiu no meio de seus irmãos; e, daquele dia em diante, o Espírito do Senhor se apossou de Davi. Então, Samuel se levantou e foi para Ramá.
14 Tendo-se retirado de Saul o Espírito do Senhor, da parte deste um espírito maligno o atormentava.
15 Então, os servos de Saul lhe disseram: Eis que, agora, um espírito maligno, enviado de Deus, te atormenta.
16 Manda, pois, senhor nosso, que teus servos, que estão em tua presença, busquem um homem que saiba tocar harpa; e será que, quando o espírito maligno, da parte do Senhor, vier sobre ti, então, ele a dedilhará, e te acharás melhor.
17 Disse Saul aos seus servos: Buscai-me, pois, um homem que saiba tocar bem e trazei-mo.
18 Então, respondeu um dos moços e disse: Conheço um filho de Jessé, o belemita, que sabe tocar e é forte e valente, homem de guerra, sisudo em palavras e de boa aparência; e o Senhor é com ele.
19 Saul enviou mensageiros a Jessé, dizendo: Envia-me Davi, teu filho, o que está com as ovelhas.
20 Tomou, pois, Jessé um jumento, e o carregou de pão, um odre de vinho e um cabrito, e enviou-os a Saul por intermédio de Davi, seu filho.
21 Assim, Davi foi a Saul e esteve perante ele; este o amou muito e o fez seu escudeiro.
22 Saul mandou dizer a Jessé: Deixa estar Davi perante mim, pois me caiu em graça.
23 E sucedia que, quando o espírito maligno, da parte de Deus, vinha sobre Saul, Davi tomava a harpa e a dedilhava; então, Saul sentia alívio e se achava melhor, e o espírito maligno se retirava dele.*
1 Ajuntaram os filisteus as suas tropas para a guerra, e congregaram-se em Socó, que está em Judá, e acamparam-se entre Socó e Azeca, em Efes-Damim.
2 Porém Saul e os homens de Israel se ajuntaram, e acamparam no vale de Elá, e ali ordenaram a batalha contra os filisteus.
3 Estavam estes num monte do lado dalém, e os israelitas, no outro monte do lado daquém; e, entre eles, o vale.
4 Então, saiu do arraial dos filisteus um homem guerreiro, cujo nome era Golias, de Gate, da altura de seis côvados e um palmo.
5 Trazia na cabeça um capacete de bronze e vestia uma couraça de escamas cujo peso era de cinco mil siclos de bronze.
6 Trazia caneleiras de bronze nas pernas e um dardo de bronze entre os ombros.
7 A haste da sua lança era como o eixo do tecelão, e a ponta da sua lança, de seiscentos siclos de ferro; e diante dele ia o escudeiro.
8 Parou, clamou às tropas de Israel e disse-lhes: Para que saís, formando-vos em linha de batalha? Não sou eu filisteu, e vós, servos de Saul? Escolhei dentre vós um homem que desça contra mim.
9 Se ele puder pelejar comigo e me ferir, seremos vossos servos; porém, se eu o vencer e o ferir, então, sereis nossos servos e nos servireis.
10 Disse mais o filisteu: Hoje, afronto as tropas de Israel. Dai-me um homem, para que ambos pelejemos.
11 Ouvindo Saul e todo o Israel estas palavras do filisteu, espantaram-se e temeram muito.
12 Davi era filho daquele efrateu de Belém de Judá cujo nome era Jessé, que tinha oito filhos; nos dias de Saul, era já velho e adiantado em anos entre os homens.
13 Apresentaram-se os três filhos mais velhos de Jessé a Saul e o seguiram à guerra; chamavam-se: Eliabe, o primogênito, o segundo, Abinadabe, e o terceiro, Samá.
14 Davi era o mais moço; só os três maiores seguiram Saul.
15 Davi, porém, ia a Saul e voltava, para apascentar as ovelhas de seu pai, em Belém.
16 Chegava-se, pois, o filisteu pela manhã e à tarde; e apresentou-se por quarenta dias.
17 Disse Jessé a Davi, seu filho: Leva, peço-te, para teus irmãos um efa deste trigo tostado e estes dez pães e corre a levá-los ao acampamento, a teus irmãos.
18 Porém estes dez queijos, leva-os ao comandante de mil; e visitarás teus irmãos, a ver se vão bem; e trarás uma prova de como passam.
19 Saul, e eles, e todos os homens de Israel estão no vale de Elá, pelejando com os filisteus.
20 Davi, pois, no dia seguinte, se levantou de madrugada, deixou as ovelhas com um guarda, carregou-se e partiu, como Jessé lhe ordenara; e chegou ao acampamento quando já as tropas saíam para formar-se em ordem de batalha e, a gritos, chamavam à peleja.
21 Os israelitas e filisteus se puseram em ordem, fileira contra fileira.
22 Davi, deixando o que trouxera aos cuidados do guarda da bagagem, correu à batalha; e, chegando, perguntou a seus irmãos se estavam bem.
23 Estando Davi ainda a falar com eles, eis que vinha subindo do exército dos filisteus o duelista, cujo nome era Golias, o filisteu de Gate; e falou as mesmas coisas que antes falara, e Davi o ouviu.
24 Todos os israelitas, vendo aquele homem, fugiam de diante dele, e temiam grandemente,
25 e diziam uns aos outros: Vistes aquele homem que subiu? Pois subiu para afrontar a Israel. A quem o matar, o rei o cumulará de grandes riquezas, e lhe dará por mulher a filha, e à casa de seu pai isentará de impostos em Israel.
26 Então, falou Davi aos homens que estavam consigo, dizendo: Que farão àquele homem que ferir a este filisteu e tirar a afronta de sobre Israel? Quem é, pois, esse incircunciso filisteu, para afrontar os exércitos do Deus vivo?
27 E o povo lhe repetiu as mesmas palavras, dizendo: Assim farão ao homem que o ferir.
28 Ouvindo-o Eliabe, seu irmão mais velho, falar àqueles homens, acendeu-se-lhe a ira contra Davi, e disse: Por que desceste aqui? E a quem deixaste aquelas poucas ovelhas no deserto? Bem conheço a tua presunção e a tua maldade; desceste apenas para ver a peleja.
29 Respondeu Davi: Que fiz eu agora? Fiz somente uma pergunta.
30 Desviou-se dele para outro e falou a mesma coisa; e o povo lhe tornou a responder como dantes.
31 Ouvidas as palavras que Davi falara, anunciaram-nas a Saul, que mandou chamá-lo.
32 Davi disse a Saul: Não desfaleça o coração de ninguém por causa dele; teu servo irá e pelejará contra o filisteu.
33 Porém Saul disse a Davi: Contra o filisteu não poderás ir para pelejar com ele; pois tu és ainda moço, e ele, guerreiro desde a sua mocidade.
34 Respondeu Davi a Saul: Teu servo apascentava as ovelhas de seu pai; quando veio um leão ou um urso e tomou um cordeiro do rebanho,
35 eu saí após ele, e o feri, e livrei o cordeiro da sua boca; levantando-se ele contra mim, agarrei-o pela barba, e o feri, e o matei.
36 O teu servo matou tanto o leão como o urso; este incircunciso filisteu será como um deles, porquanto afrontou os exércitos do Deus vivo.
37 Disse mais Davi: O Senhor me livrou das garras do leão e das do urso; ele me livrará das mãos deste filisteu. Então, disse Saul a Davi: Vai-te, e o Senhor seja contigo.
38 Saul vestiu a Davi da sua armadura, e lhe pôs sobre a cabeça um capacete de bronze, e o vestiu de uma couraça.
39 Davi cingiu a espada sobre a armadura e experimentou andar, pois jamais a havia usado; então, disse Davi a Saul: Não posso andar com isto, pois nunca o usei. E Davi tirou aquilo de sobre si.
40 Tomou o seu cajado na mão, e escolheu para si cinco pedras lisas do ribeiro, e as pôs no alforje de pastor, que trazia, a saber, no surrão; e, lançando mão da sua funda, foi-se chegando ao filisteu.
41 O filisteu também se vinha chegando a Davi; e o seu escudeiro ia adiante dele.
42 Olhando o filisteu e vendo a Davi, o desprezou, porquanto era moço ruivo e de boa aparência.
43 Disse o filisteu a Davi: Sou eu algum cão, para vires a mim com paus? E, pelos seus deuses, amaldiçoou o filisteu a Davi.
44 Disse mais o filisteu a Davi: Vem a mim, e darei a tua carne às aves do céu e às bestas-feras do campo.
45 Davi, porém, disse ao filisteu: Tu vens contra mim com espada, e com lança, e com escudo; eu, porém, vou contra ti em nome do Senhor dos Exércitos, o Deus dos exércitos de Israel, a quem tens afrontado.
46 Hoje mesmo, o Senhor te entregará nas minhas mãos; ferir-te-ei, tirar-te-ei a cabeça e os cadáveres do arraial dos filisteus darei, hoje mesmo, às aves dos céus e às bestas-feras da terra; e toda a terra saberá que há Deus em Israel.
47 Saberá toda esta multidão que o Senhor salva, não com espada, nem com lança; porque do Senhor é a guerra, e ele vos entregará nas nossas mãos.
48 Sucedeu que, dispondo-se o filisteu a encontrar-se com Davi, este se apressou e, deixando as suas fileiras, correu de encontro ao filisteu.
49 Davi meteu a mão no alforje, e tomou dali uma pedra, e com a funda lha atirou, e feriu o filisteu na testa; a pedra encravou-se-lhe na testa, e ele caiu com o rosto em terra.
50 Assim, prevaleceu Davi contra o filisteu, com uma funda e com uma pedra, e o feriu, e o matou; porém não havia espada na mão de Davi.
51 Pelo que correu Davi, e, lançando-se sobre o filisteu, tomou-lhe a espada, e desembainhou-a, e o matou, cortando-lhe com ela a cabeça. Vendo os filisteus que era morto o seu herói, fugiram.
52 Então, os homens de Israel e Judá se levantaram, e jubilaram, e perseguiram os filisteus, até Gate e até às portas de Ecrom. E caíram filisteus feridos pelo caminho, de Saaraim até Gate e até Ecrom.
53 Então, voltaram os filhos de Israel de perseguirem os filisteus e lhes despojaram os acampamentos.
54 Tomou Davi a cabeça do filisteu e a trouxe a Jerusalém; porém as armas dele pô-las Davi na sua tenda.
55 Quando Saul viu sair Davi a encontrar-se com o filisteu, disse a Abner, o comandante do exército: De quem é filho este jovem, Abner? Respondeu Abner: Tão certo como tu vives, ó rei, não o sei.
56 Disse o rei: Pergunta, pois, de quem é filho este jovem.
57 Voltando Davi de haver ferido o filisteu, Abner o tomou e o levou à presença de Saul, trazendo ele na mão a cabeça do filisteu.
58 Então, Saul lhe perguntou: De quem és filho, jovem? Respondeu Davi: Filho de teu servo Jessé, belemita.*
1 Sucedeu que, acabando Davi de falar com Saul, a alma de Jônatas se ligou com a de Davi; e Jônatas o amou como à sua própria alma.
2 Saul, naquele dia, o tomou e não lhe permitiu que tornasse para casa de seu pai.
3 Jônatas e Davi fizeram aliança; porque Jônatas o amava como à sua própria alma.
4 Despojou-se Jônatas da capa que vestia e a deu a Davi, como também a armadura, inclusive a espada, o arco e o cinto.
5 Saía Davi aonde quer que Saul o enviava e se conduzia com prudência; de modo que Saul o pôs sobre tropas do seu exército, e era ele benquisto de todo o povo e até dos próprios servos de Saul.
6 Sucedeu, porém, que, vindo Saul e seu exército, e voltando também Davi de ferir os filisteus, as mulheres de todas as cidades de Israel saíram ao encontro do rei Saul, cantando e dançando, com tambores, com júbilo e com instrumentos de música.
7 As mulheres se alegravam e, cantando alternadamente, diziam: Saul feriu os seus milhares, porém Davi, os seus dez milhares.
8 Então, Saul se indignou muito, pois estas palavras lhe desagradaram em extremo; e disse: Dez milhares deram elas a Davi, e a mim somente milhares; na verdade, que lhe falta, senão o reino?
9 Daquele dia em diante, Saul não via a Davi com bons olhos.
10 No dia seguinte, um espírito maligno, da parte de Deus, se apossou de Saul, que teve uma crise de raiva em casa; e Davi, como nos outros dias, dedilhava a harpa; Saul, porém, trazia na mão uma lança,
11 que arrojou, dizendo: Encravarei a Davi na parede. Porém Davi se desviou dele por duas vezes.
12 Saul temia a Davi, porque o Senhor era com este e se tinha retirado de Saul.
13 Pelo que Saul o afastou de si e o pôs por chefe de mil; ele fazia saídas e entradas militares diante do povo.
14 Davi lograva bom êxito em todos os seus empreendimentos, pois o Senhor era com ele.
15 Então, vendo Saul que Davi lograva bom êxito, tinha medo dele.
16 Porém todo o Israel e Judá amavam Davi, porquanto fazia saídas e entradas militares diante deles.
17 Disse Saul a Davi: Eis aqui Merabe, minha filha mais velha, que te darei por mulher; sê-me somente filho valente e guerreia as guerras do Senhor; porque Saul dizia consigo: Não seja contra ele a minha mão, e sim a dos filisteus.
18 Respondeu Davi a Saul: Quem sou eu, e qual é a minha vida e a família de meu pai em Israel, para vir a ser eu genro do rei?
19 Sucedeu, porém, que, ao tempo em que Merabe, filha de Saul, devia ser dada a Davi, foi dada por mulher a Adriel, meolatita.
20 Mas Mical, a outra filha de Saul, amava a Davi. Contaram-no a Saul, e isso lhe agradou.
21 Disse Saul: Eu lha darei, para que ela lhe sirva de laço e para que a mão dos filisteus venha a ser contra ele. Pelo que Saul disse a Davi: Com esta segunda serás, hoje, meu genro.
22 Ordenou Saul aos seus servos: Falai confidencialmente a Davi, dizendo: Eis que o rei tem afeição por ti, e todos os seus servos te amam; consente, pois, em ser genro do rei.
23 Os servos de Saul falaram estas palavras a Davi, o qual respondeu: Parece-vos coisa de somenos ser genro do rei, sendo eu homem pobre e de humilde condição?
24 Os servos de Saul lhe referiram isto, dizendo: Tais foram as palavras que falou Davi.
25 Então, disse Saul: Assim direis a Davi: O rei não deseja dote algum, mas cem prepúcios de filisteus, para tomar vingança dos inimigos do rei. Porquanto Saul tentava fazer cair a Davi pelas mãos dos filisteus.
26 Tendo os servos de Saul referido estas palavras a Davi, agradou-se este de que viesse a ser genro do rei. Antes de vencido o prazo,
27 dispôs-se Davi e partiu com os seus homens, e feriram dentre os filisteus duzentos homens; trouxe os seus prepúcios e os entregou todos ao rei, para que lhe fosse genro. Então, Saul lhe deu por mulher a sua filha Mical.
28 Viu Saul e reconheceu que o Senhor era com Davi; e Mical, filha de Saul, o amava.
29 Então, Saul temeu ainda mais a Davi e continuamente foi seu inimigo.
30 Cada vez que os príncipes dos filisteus saíam à batalha, Davi lograva mais êxito do que todos os servos de Saul; portanto, o seu nome se tornou muito estimado.*
1 Falou Saul a Jônatas, seu filho, e a todos os servos sobre matar Davi. Jônatas, filho de Saul, mui afeiçoado a Davi,
2 o fez saber a este, dizendo: Meu pai, Saul, procura matar-te; acautela-te, pois, pela manhã, fica num lugar oculto e esconde-te.
3 Eu sairei e estarei ao lado de meu pai no campo onde estás; falarei a teu respeito a meu pai, e verei o que houver, e te farei saber.
4 Então, Jônatas falou bem de Davi a Saul, seu pai, e lhe disse: Não peque o rei contra seu servo Davi, porque ele não pecou contra ti, e os seus feitos para contigo têm sido mui importantes.
5 Arriscando ele a vida, feriu os filisteus e efetuou o Senhor grande livramento a todo o Israel; tu mesmo o viste e te alegraste; por que, pois, pecarias contra sangue inocente, matando Davi sem causa?
6 Saul atendeu à voz de Jônatas e jurou: Tão certo como vive o Senhor, ele não morrerá.
7 Jônatas chamou a Davi, contou-lhe todas estas palavras e o levou a Saul; e esteve Davi perante este como dantes.
8 Tornou a haver guerra, e, quando Davi pelejou contra os filisteus e os feriu com grande derrota, e fugiram diante dele,
9 o espírito maligno, da parte do Senhor, tornou sobre Saul; estava este assentado em sua casa e tinha na mão a sua lança, enquanto Davi dedilhava o seu instrumento músico.
10 Procurou Saul encravar a Davi na parede, porém ele se desviou do seu golpe, indo a lança ferir a parede; então, fugiu Davi e escapou.
11 Porém Saul, naquela mesma noite, mandou mensageiros à casa de Davi, que o vigiassem, para ele o matar pela manhã; disto soube Davi por Mical, sua mulher, que lhe disse: Se não salvares a tua vida esta noite, amanhã serás morto.
12 Então, Mical desceu Davi por uma janela; e ele se foi, fugiu e escapou.
13 Mical tomou um ídolo do lar, e o deitou na cama, e pôs-lhe à cabeça um tecido de pelos de cabra, e o cobriu com um manto.
14 Tendo Saul enviado mensageiros que trouxessem Davi, ela disse: Está doente.
15 Então, Saul mandou mensageiros que vissem Davi, ordenando-lhes: Trazei-mo mesmo na cama, para que o mate.
16 Vindo, pois, os mensageiros, eis que estava na cama o ídolo do lar, e o tecido de pelos de cabra, ao redor de sua cabeça.
17 Então, disse Saul a Mical: Por que assim me enganaste e deixaste ir e escapar o meu inimigo? Respondeu-lhe Mical: Porque ele me disse: Deixa-me ir; se não, eu te mato.
18 Assim, Davi fugiu, e escapou, e veio a Samuel, a Ramá, e lhe contou tudo quanto Saul lhe fizera; e se retiraram, ele e Samuel, e ficaram na casa dos profetas.
19 Foi dito a Saul: Eis que Davi está na casa dos profetas, em Ramá.
20 Então, enviou Saul mensageiros para trazerem Davi, os quais viram um grupo de profetas profetizando, onde estava Samuel, que lhes presidia; e o Espírito de Deus veio sobre os mensageiros de Saul, e também eles profetizaram.
21 Avisado disto, Saul enviou outros mensageiros, e também estes profetizaram; então, enviou Saul ainda uns terceiros, os quais também profetizaram.
22 Então, foi também ele mesmo a Ramá e, chegando ao poço grande que estava em Seco, perguntou: Onde estão Samuel e Davi? Responderam-lhe: Eis que estão na casa dos profetas, em Ramá.
23 Então, foi para a casa dos profetas, em Ramá; e o mesmo Espírito de Deus veio sobre ele, que, caminhando, profetizava até chegar à casa dos profetas, em Ramá.
24 Também ele despiu a sua túnica, e profetizou diante de Samuel, e, sem ela, esteve deitado em terra todo aquele dia e toda aquela noite; pelo que se diz: Está também Saul entre os profetas?*
1 Então, fugiu Davi da casa dos profetas, em Ramá, e veio, e disse a Jônatas: Que fiz eu? Qual é a minha culpa? E qual é o meu pecado diante de teu pai, que procura tirar-me a vida?
2 Ele lhe respondeu: Tal não suceda; não serás morto. Meu pai não faz coisa nenhuma, nem grande nem pequena, sem primeiro me dizer; por que, pois, meu pai me ocultaria isso? Não há nada disso.
3 Então, Davi respondeu enfaticamente: Mui bem sabe teu pai que da tua parte achei mercê; pelo que disse consigo: Não saiba isto Jônatas, para que não se entristeça. Tão certo como vive o Senhor, e tu vives, Jônatas, apenas há um passo entre mim e a morte.
4 Disse Jônatas a Davi: O que tu desejares eu te farei.
5 Disse Davi a Jônatas: Amanhã é a Festa da Lua Nova, em que sem falta deveria assentar-me com o rei para comer; mas deixa-me ir, e esconder-me-ei no campo, até à terceira tarde.
6 Se teu pai notar a minha ausência, dirás: Davi me pediu muito que o deixasse ir a toda pressa a Belém, sua cidade; porquanto se faz lá o sacrifício anual para toda a família.
7 Se disser assim: Está bem! Então, teu servo terá paz. Porém, se muito se indignar, sabe que já o mal está, de fato, determinado por ele.
8 Usa, pois, de misericórdia para com o teu servo, porque lhe fizeste entrar contigo em aliança no Senhor; se, porém, há em mim culpa, mata-me tu mesmo; por que me levarias a teu pai?
9 Então, disse Jônatas: Longe de ti tal coisa; porém, se dalguma sorte soubesse que já este mal estava, de fato, determinado por meu pai, para que viesse sobre ti, não to declararia eu?
10 Perguntou Davi a Jônatas: Quem tal me fará saber, se, por acaso, teu pai te responder asperamente?
11 Então, disse Jônatas a Davi: Vem, e saiamos ao campo. E saíram.
12 E disse Jônatas a Davi: O Senhor, Deus de Israel, seja testemunha. Amanhã ou depois de amanhã, a estas horas sondarei meu pai; se algo houver favorável a Davi, eu to mandarei dizer.
13 Mas, se meu pai quiser fazer-te mal, faça com Jônatas o Senhor o que a este aprouver, se não to fizer saber eu e não te deixar ir embora, para que sigas em paz. E seja o Senhor contigo, como tem sido com meu pai.
14 Se eu, então, ainda viver, porventura, não usarás para comigo da bondade do Senhor, para que não morra?
15 Nem tampouco cortarás jamais da minha casa a tua bondade; nem ainda quando o Senhor desarraigar da terra todos os inimigos de Davi.
16 Assim, fez Jônatas aliança com a casa de Davi, dizendo: Vingue o Senhor os inimigos de Davi.
17 Jônatas fez jurar a Davi de novo, pelo amor que este lhe tinha, porque Jônatas o amava com todo o amor da sua alma.
18 Disse-lhe Jônatas: Amanhã é a Festa da Lua Nova; perguntar-se-á por ti, porque o teu lugar estará vazio.
19 Ao terceiro dia, descerás apressadamente e irás para o lugar em que te escondeste no dia do ajuste; e fica junto à pedra de Ezel.
20 Atirarei três flechas para aquele lado, como quem atira ao alvo.
21 Eis que mandarei o moço e lhe direi: Vai, procura as flechas; se eu disser ao moço: Olha que as flechas estão para cá de ti, traze-as; então, vem, Davi, porque, tão certo como vive o Senhor, terás paz, e nada há que temer.
22 Porém, se disser ao moço: Olha que as flechas estão para lá de ti. Vai-te embora, porque o Senhor te manda ir.
23 Quanto àquilo de que eu e tu falamos, eis que o Senhor está entre mim e ti, para sempre.
24 Escondeu-se, pois, Davi no campo; e, sendo a Festa da Lua Nova, pôs-se o rei à mesa para comer.
25 Assentou-se o rei na sua cadeira, segundo o costume, no lugar junto à parede; Jônatas, defronte dele, e Abner, ao lado de Saul; mas o lugar de Davi estava desocupado.
26 Porém, naquele dia, não disse Saul nada, pois pensava: Aconteceu-lhe alguma coisa, pela qual não está limpo; talvez esteja contaminado.
27 Sucedeu também ao outro dia, o segundo da Festa da Lua Nova, que o lugar de Davi continuava desocupado; disse, pois, Saul a Jônatas, seu filho: Por que não veio a comer o filho de Jessé, nem ontem nem hoje?
28 Respondeu Jônatas a Saul: Davi me pediu, encarecidamente, que o deixasse ir a Belém.
29 Ele me disse: Peço-te que me deixes ir, porque a nossa família tem um sacrifício na cidade, e um de meus irmãos insiste comigo para que eu vá. Se, pois, agora, achei mercê aos teus olhos, peço-te que me deixes partir, para que veja meus irmãos. Por isso, não veio à mesa do rei.
Saul irado contra Jônatas
30 Então, se acendeu a ira de Saul contra Jônatas, e disse-lhe: Filho de mulher perversa e rebelde; não sei eu que elegeste o filho de Jessé, para vergonha tua e para vergonha do recato de tua mãe?
31 Pois, enquanto o filho de Jessé viver sobre a terra, nem tu estarás seguro, nem seguro o teu reino; pelo que manda buscá-lo, agora, porque deve morrer.
32 Então, respondeu Jônatas a Saul, seu pai, e lhe disse: Por que há de ele morrer? Que fez ele?
33 Então, Saul atirou-lhe com a lança para o ferir; com isso entendeu Jônatas que, de fato, seu pai já determinara matar a Davi.
34 Pelo que Jônatas, todo encolerizado, se levantou da mesa e, neste segundo dia da Festa da Lua Nova, não comeu pão, pois ficara muito sentido por causa de Davi, a quem seu pai havia ultrajado.
35 Na manhã seguinte, saiu Jônatas ao campo, no tempo ajustado com Davi, e levou consigo um rapaz.
36 Então, disse ao seu rapaz: Corre a buscar as flechas que eu atirar. Este correu, e ele atirou uma flecha, que fez passar além do rapaz.
37 Chegando o rapaz ao lugar da flecha que Jônatas havia atirado, gritou Jônatas atrás dele e disse: Não está a flecha mais para lá de ti?
38 Tornou Jônatas a gritar: Apressa-te, não te demores. O rapaz de Jônatas apanhou as flechas e voltou ao seu senhor.
39 O rapaz não entendeu coisa alguma; só Jônatas e Davi sabiam deste ajuste.
40 Então, Jônatas deu as suas armas ao rapaz que o acompanhava e disse-lhe: Anda, leva-as à cidade.
41 Indo-se o rapaz, levantou-se Davi do lado do sul e prostrou-se rosto em terra três vezes; e beijaram-se um ao outro e choraram juntos; Davi, porém, muito mais.
42 Disse Jônatas a Davi: Vai-te em paz, porquanto juramos ambos em nome do Senhor, dizendo: O Senhor seja para sempre entre mim e ti e entre a minha descendência e a tua.
43 Então, se levantou Davi e se foi; e Jônatas entrou na cidade.*
1 Então, veio Davi a Nobe, ao sacerdote Aimeleque; Aimeleque, tremendo, saiu ao encontro de Davi e disse-lhe: Por que vens só, e ninguém, contigo?
2 Respondeu Davi ao sacerdote Aimeleque: O rei deu-me uma ordem e me disse: Ninguém saiba por que te envio e de que te incumbo; quanto aos meus homens, combinei que me encontrassem em tal e tal lugar.
3 Agora, que tens à mão? Dá-me cinco pães ou o que se achar.
4 Respondendo o sacerdote a Davi, disse-lhe: Não tenho pão comum à mão; há, porém, pão sagrado, se ao menos os teus homens se abstiveram das mulheres.
5 Respondeu Davi ao sacerdote e lhe disse: Sim, como sempre, quando saio à campanha, foram-nos vedadas as mulheres, e os corpos dos homens não estão imundos. Se tal se dá em viagem comum, quanto mais serão puros hoje!
6 Deu-lhe, pois, o sacerdote o pão sagrado, porquanto não havia ali outro, senão os pães da proposição, que se tiraram de diante do Senhor, quando trocados, no devido dia, por pão quente.
7 Achava-se ali, naquele dia, um dos servos de Saul, detido perante o Senhor, cujo nome era Doegue, edomita, o maioral dos pastores de Saul.
8 Disse Davi a Aimeleque: Não tens aqui à mão lança ou espada alguma? Porque não trouxe comigo nem a minha espada nem as minhas armas, porque a ordem do rei era urgente.
9 Respondeu o sacerdote: A espada de Golias, o filisteu, a quem mataste no vale de Elá, está aqui, envolta num pano detrás da estola sacerdotal; se a queres levar, leva-a, porque não há outra aqui, senão essa. Disse Davi: Não há outra semelhante; dá-ma.
10 Levantou-se Davi, naquele dia, e fugiu de diante de Saul, e foi a Aquis, rei de Gate.
11 Porém os servos de Aquis lhe disseram: Este não é Davi, o rei da sua terra? Não é a este que se cantava nas danças, dizendo: Saul feriu os seus milhares, porém Davi, os seus dez milhares?
12 Davi guardou estas palavras, considerando-as consigo mesmo, e teve muito medo de Aquis, rei de Gate.
13 Pelo que se contrafez diante deles, em cujas mãos se fingia doido, esgravatava nos postigos das portas e deixava correr saliva pela barba.
14 Então, disse Aquis aos seus servos: Bem vedes que este homem está louco; por que mo trouxestes a mim?
15 Faltam-me a mim doidos, para que trouxésseis este para fazer doidices diante de mim? Há de entrar este na minha casa?*
1 Davi retirou-se dali e se refugiou na caverna de Adulão; quando ouviram isso seus irmãos e toda a casa de seu pai, desceram ali para ter com ele.
2 Ajuntaram-se a ele todos os homens que se achavam em aperto, e todo homem endividado, e todos os amargurados de espírito, e ele se fez chefe deles; e eram com ele uns quatrocentos homens.
3 Dali passou Davi a Mispa de Moabe e disse ao seu rei: Deixa estar meu pai e minha mãe convosco, até que eu saiba o que Deus há de fazer de mim.
4 Trouxe-os perante o rei de Moabe, e com este moraram por todo o tempo que Davi esteve neste lugar seguro.
5 Porém o profeta Gade disse a Davi: Não fiques neste lugar seguro; vai e entra na terra de Judá. Então, Davi saiu e foi para o bosque de Herete.
6 Ouviu Saul que Davi e os homens que o acompanhavam foram descobertos. Achando-se Saul em Gibeá, debaixo de um arvoredo, numa colina, tendo na mão a sua lança, e todos os seus servos com ele,
7 disse a todos estes: Ouvi, peço-vos, filhos de Benjamim, dar-vos-á também o filho de Jessé, a todos vós, terras e vinhas e vos fará a todos chefes de milhares e chefes de centenas,
8 para que todos tenhais conspirado contra mim? E ninguém houve que me desse aviso de que meu filho fez aliança com o filho de Jessé; e nenhum dentre vós há que se doa por mim e me participe que meu filho contra mim instigou a meu servo, para me armar ciladas, como se vê neste dia.
9 Então, respondeu Doegue, o edomita, que também estava com os servos de Saul, e disse: Vi o filho de Jessé chegar a Nobe, a Aimeleque, filho de Aitube,
10 e como Aimeleque, a pedido dele, consultou o Senhor, e lhe fez provisões, e lhe deu a espada de Golias, o filisteu.
11 Então, o rei mandou chamar Aimeleque, sacerdote, filho de Aitube, e toda a casa de seu pai, a saber, os sacerdotes que estavam em Nobe; todos eles vieram ao rei.
12 Disse Saul: Ouve, peço-te, filho de Aitube! Este respondeu: Eis-me aqui, meu senhor!
13 Então, lhe disse Saul: Por que conspirastes contra mim, tu e o filho de Jessé? Pois lhe deste pão e espada e consultaste a favor dele a Deus, para que se levantasse contra mim e me armasse ciladas, como hoje se vê.
14 Respondeu Aimeleque ao rei e disse: E quem, entre todos os teus servos, há tão fiel como Davi, o genro do rei, chefe da tua guarda pessoal e honrado na tua casa?
15 Acaso, é de hoje que consulto a Deus em seu favor? Não! Jamais impute o rei coisa nenhuma a seu servo, nem a toda a casa de meu pai, pois o teu servo de nada soube de tudo isso, nem muito nem pouco.
16 Respondeu o rei: Aimeleque, morrerás, tu e toda a casa de teu pai.
17 Disse o rei aos da guarda, que estavam com ele: Volvei e matai os sacerdotes do Senhor, porque também estão de mãos dadas com Davi e porque souberam que fugiu e não mo fizeram saber. Porém os servos do rei não quiseram estender as mãos contra os sacerdotes do Senhor.
18 Então, disse o rei a Doegue: Volve-te e arremete contra os sacerdotes. Então, se virou Doegue, o edomita, e arremeteu contra os sacerdotes, e matou, naquele dia, oitenta e cinco homens que vestiam estola sacerdotal de linho.
19 Também a Nobe, cidade destes sacerdotes, passou a fio de espada: homens, e mulheres, e meninos, e crianças de peito, e bois, e jumentos, e ovelhas.
20 Porém dos filhos de Aimeleque, filho de Aitube, um só, cujo nome era Abiatar, salvou-se e fugiu para Davi;
21 e lhe anunciou que Saul tinha matado os sacerdotes do Senhor.
22 Então, Davi disse a Abiatar: Bem sabia eu, naquele dia, que, estando ali Doegue, o edomita, não deixaria de o dizer a Saul. Fui a causa da morte de todas as pessoas da casa de teu pai.
23 Fica comigo, não temas, porque quem procura a minha morte procura também a tua; estarás a salvo comigo.*
1 Foi dito a Davi: Eis que os filisteus pelejam contra Queila e saqueiam as eiras.
2 Consultou Davi ao Senhor, dizendo: Irei eu e ferirei estes filisteus? Respondeu o Senhor a Davi: Vai, e ferirás os filisteus, e livrarás Queila.
3 Porém os homens de Davi lhe disseram: Temos medo aqui em Judá, quanto mais indo a Queila contra as tropas dos filisteus.
4 Então, Davi tornou a consultar o Senhor, e o Senhor lhe respondeu e disse: Dispõe-te, desce a Queila, porque te dou os filisteus nas tuas mãos.
5 Partiu Davi com seus homens a Queila, e pelejou contra os filisteus, e levou todo o gado, e fez grande morticínio entre eles; assim, Davi salvou os moradores de Queila.
6 Sucedeu que, quando Abiatar, filho de Aimeleque, fugiu para Davi, a Queila, desceu com a estola sacerdotal na mão.
7 Foi anunciado a Saul que Davi tinha ido a Queila. Disse Saul: Deus o entregou nas minhas mãos; está encerrado, pois entrou numa cidade de portas e ferrolhos.
8 Então, Saul mandou chamar todo o povo à peleja, para que descessem a Queila e cercassem Davi e os seus homens.
9 Sabedor, porém, Davi de que Saul maquinava o mal contra ele, disse a Abiatar, sacerdote: Traze aqui a estola sacerdotal.
10 Orou Davi: Ó Senhor, Deus de Israel, teu servo ouviu que Saul, de fato, procura vir a Queila, para destruir a cidade por causa de mim.
11 Entregar-me-ão os homens de Queila nas mãos dele? Descerá Saul, como o teu servo ouviu? Ah! Senhor, Deus de Israel, faze-o saber ao teu servo. E disse o Senhor: Descerá.
12 Perguntou-lhe Davi: Entregar-me-ão os homens de Queila, a mim e aos meus servos, nas mãos de Saul? Respondeu o Senhor: Entregarão.
13 Então, se dispôs Davi com os seus homens, uns seiscentos, saíram de Queila e se foram sem rumo certo. Sendo anunciado a Saul que Davi fugira de Queila, cessou de persegui-lo.
14 Permaneceu Davi no deserto, nos lugares seguros, e ficou na região montanhosa no deserto de Zife. Saul buscava-o todos os dias, porém Deus não o entregou nas suas mãos.
15 Vendo, pois, Davi que Saul saíra a tirar-lhe a vida, deteve-se no deserto de Zife, em Horesa.
16 Então, se levantou Jônatas, filho de Saul, e foi para Davi, a Horesa, e lhe fortaleceu a confiança em Deus,
17 e lhe disse: Não temas, porque a mão de Saul, meu pai, não te achará; porém tu reinarás sobre Israel, e eu serei contigo o segundo, o que também Saul, meu pai, bem sabe.
18 E ambos fizeram aliança perante o Senhor. Davi ficou em Horesa, e Jônatas voltou para sua casa.
19 Então, subiram os zifeus a Saul, a Gibeá, dizendo: Não se escondeu Davi entre nós, nos lugares seguros de Horesa, no outeiro de Haquila, que está ao sul de Jesimom?
20 Agora, pois, ó rei, desce conforme te impõe o coração; toca-nos a nós entregarmo-lo nas mãos do rei.
21 Disse Saul: Benditos sejais vós do Senhor, porque vos compadecestes de mim.
22 Ide, pois, informai-vos ainda melhor, sabei e notai o lugar que frequenta e quem o tenha visto ali; porque me foi dito que é astutíssimo.
23 Pelo que atentai bem e informai-vos acerca de todos os esconderijos em que ele se oculta; então, voltai a ter comigo com seguras informações, e irei convosco; se ele estiver na terra, buscá-lo-ei entre todos os milhares de Judá.
24 Então, se levantaram eles e se foram a Zife, adiante de Saul; Davi, porém, e os seus homens estavam no deserto de Maom, na planície, ao sul de Jesimom.
25 Saul e os seus homens se foram ao encalço dele, e isto foi dito a Davi; pelo que desceu para a penha que está no deserto de Maom. Ouvindo-o Saul, perseguiu a Davi no deserto de Maom.
26 Saul ia de um lado do monte, e Davi e os seus homens, do outro; apressou-se Davi em fugir para escapar de Saul; porém este e os seus homens cercaram Davi e os seus homens para os prender.
27 Então, veio um mensageiro a Saul, dizendo: Apressa-te e vem, porque os filisteus invadiram a terra.
28 Pelo que Saul desistiu de perseguir a Davi e se foi contra os filisteus. Por esta razão, aquele lugar se chamou Pedra de Escape.
29 Subiu Davi daquele lugar e ficou nos lugares seguros de En-Gedi.*
1 Tendo Saul voltado de perseguir os filisteus, foi-lhe dito: Eis que Davi está no deserto de En-Gedi.
2 Tomou, então, Saul três mil homens, escolhidos dentre todo o Israel, e foi ao encalço de Davi e dos seus homens, nas faldas das penhas das cabras monteses.
3 Chegou a uns currais de ovelhas no caminho, onde havia uma caverna; entrou nela Saul, a aliviar o ventre. Ora, Davi e os seus homens estavam assentados no mais interior da mesma.
4 Então, os homens de Davi lhe disseram: Hoje é o dia do qual o Senhor te disse: Eis que te entrego nas mãos o teu inimigo, e far-lhe-ás o que bem te parecer. Levantou-se Davi e, furtivamente, cortou a orla do manto de Saul.
5 Sucedeu, porém, que, depois, sentiu Davi bater-lhe o coração, por ter cortado a orla do manto de Saul;
6 e disse aos seus homens: O Senhor me guarde de que eu faça tal coisa ao meu senhor, isto é, que eu estenda a mão contra ele, pois é o ungido do Senhor.
7 Com estas palavras, Davi conteve os seus homens e não lhes permitiu que se levantassem contra Saul; retirando-se Saul da caverna, prosseguiu o seu caminho.
8 Depois, também Davi se levantou e, saindo da caverna, gritou a Saul, dizendo: Ó rei, meu senhor! Olhando Saul para trás, inclinou-se Davi e fez-lhe reverência, com o rosto em terra.
9 Disse Davi a Saul: Por que dás tu ouvidos às palavras dos homens que dizem: Davi procura fazer-te mal?
10 Os teus próprios olhos viram, hoje, que o Senhor te pôs em minhas mãos nesta caverna, e alguns disseram que eu te matasse; porém a minha mão te poupou; porque disse: Não estenderei a mão contra o meu senhor, pois é o ungido de Deus.
11 Olha, pois, meu pai, vê aqui a orla do teu manto na minha mão. No fato de haver eu cortado a orla do teu manto sem te matar, reconhece e vê que não há em mim nem mal nem rebeldia, e não pequei contra ti, ainda que andas à caça da minha vida para ma tirares.
12 Julgue o Senhor entre mim e ti e vingue-me o Senhor a teu respeito; porém a minha mão não será contra ti.
13 Dos perversos procede a perversidade, diz o provérbio dos antigos; porém a minha mão não está contra ti.
14 Após quem saiu o rei de Israel? A quem persegue? A um cão morto? A uma pulga?
15 Seja o Senhor o meu juiz, e julgue entre mim e ti, e veja, e pleiteie a minha causa, e me faça justiça, e me livre da tua mão.
16 Tendo Davi acabado de falar a Saul todas estas palavras, disse Saul: É isto a tua voz, meu filho Davi? E chorou Saul em voz alta.
17 Disse a Davi: Mais justo és do que eu; pois tu me recompensaste com bem, e eu te paguei com mal.
18 Mostraste, hoje, que me fizeste bem; pois o Senhor me havia posto em tuas mãos, e tu me não mataste.
19 Porque quem há que, encontrando o inimigo, o deixa ir por bom caminho? O Senhor, pois, te pague com bem, pelo que, hoje, me fizeste.
20 Agora, pois, tenho certeza de que serás rei e de que o reino de Israel há de ser firme na tua mão.
21 Portanto, jura-me pelo Senhor que não eliminarás a minha descendência, nem desfarás o meu nome da casa de meu pai.
22 Então, jurou Davi a Saul, e este se foi para sua casa; porém Davi e os seus homens subiram ao lugar seguro.*
1 Faleceu Samuel; todos os filhos de Israel se ajuntaram, e o prantearam, e o sepultaram na sua casa, em Ramá. Davi se levantou e desceu ao deserto de Parã.
2 Havia um homem, em Maom, que tinha as suas possessões no Carmelo; homem abastado, tinha três mil ovelhas e mil cabras e estava tosquiando as suas ovelhas no Carmelo.
3 Nabal era o nome deste homem, e Abigail, o de sua mulher; esta era sensata e formosa, porém o homem era duro e maligno em todo o seu trato. Era ele da casa de Calebe.
4 Ouvindo Davi, no deserto, que Nabal tosquiava as suas ovelhas,
5 enviou dez moços e lhes disse: Subi ao Carmelo, ide a Nabal, perguntai-lhe, em meu nome, como está.
6 Direis àquele próspero: Paz seja contigo, e tenha paz a tua casa, e tudo o que possuis tenha paz!
7 Tenho ouvido que tens tosquiadores. Os teus pastores estiveram conosco; nenhum agravo lhes fizemos, e de nenhuma coisa sentiram falta todos os dias que estiveram no Carmelo.
8 Pergunta aos teus moços, e eles to dirão; achem mercê, pois, os meus moços na tua presença, porque viemos em boa hora; dá, pois, a teus servos e a Davi, teu filho, qualquer coisa que tiveres à mão.
9 Chegando, pois, os moços de Davi e tendo falado a Nabal todas essas palavras em nome de Davi, aguardaram.
10 Respondeu Nabal aos moços de Davi e disse: Quem é Davi, e quem é o filho de Jessé? Muitos são, hoje em dia, os servos que fogem ao seu senhor.
11 Tomaria eu, pois, o meu pão, e a minha água, e a carne das minhas reses que degolei para os meus tosquiadores e o daria a homens que eu não sei donde vêm?
12 Então, os moços de Davi puseram-se a caminho, voltaram e, tendo chegado, lhe contaram tudo, segundo todas estas palavras.
13 Pelo que disse Davi aos seus homens: Cada um cinja a sua espada. E cada um cingiu a sua espada, e também Davi, a sua; subiram após Davi uns quatrocentos homens, e duzentos ficaram com a bagagem.
14 Nesse meio tempo, um dentre os moços de Nabal o anunciou a Abigail, mulher deste, dizendo: Davi enviou do deserto mensageiros a saudar a nosso senhor; porém este disparatou com eles.
15 Aqueles homens, porém, nos têm sido muito bons, e nunca fomos agravados por eles e de nenhuma coisa sentimos falta em todos os dias de nosso trato com eles, quando estávamos no campo.
16 De muro em redor nos serviram, tanto de dia como de noite, todos os dias que estivemos com eles apascentando as ovelhas.
17 Agora, pois, considera e vê o que hás de fazer, porque já o mal está, de fato, determinado contra o nosso senhor e contra toda a sua casa; e ele é filho de Belial, e não há quem lhe possa falar.
18 Então, Abigail tomou, a toda pressa, duzentos pães, dois odres de vinho, cinco ovelhas preparadas, cinco medidas de trigo tostado, cem cachos de passas e duzentas pastas de figos, e os pôs sobre jumentos,
19 e disse aos seus moços: Ide adiante de mim, pois vos seguirei de perto. Porém nada disse ela a seu marido Nabal.
20 Enquanto ela, cavalgando um jumento, descia, encoberta pelo monte, Davi e seus homens também desciam, e ela se encontrou com eles.
21 Ora, Davi dissera: Com efeito, de nada me serviu ter guardado tudo quanto este possui no deserto, e de nada sentiu falta de tudo quanto lhe pertence; ele me pagou mal por bem.
22 Faça Deus o que lhe aprouver aos inimigos de Davi, se eu deixar, ao amanhecer, um só do sexo masculino dentre os seus.
23 Vendo, pois, Abigail a Davi, apressou-se, desceu do jumento e prostrou-se sobre o rosto diante de Davi, inclinando-se até à terra.
24 Lançou-se-lhe aos pés e disse: Ah! Senhor meu, caia a culpa sobre mim; permite falar a tua serva contigo e ouve as palavras da tua serva.
25 Não se importe o meu senhor com este homem de Belial, a saber, com Nabal; porque o que significa o seu nome ele é. Nabal é o seu nome, e a loucura está com ele; eu, porém, tua serva, não vi os moços de meu senhor, que enviaste.
26 Agora, pois, meu senhor, tão certo como vive o Senhor e a tua alma, foste pelo Senhor impedido de derramar sangue e de vingar-te por tuas próprias mãos. Como Nabal, sejam os teus inimigos e os que procuram fazer mal ao meu senhor.
27 Este é o presente que trouxe a tua serva a meu senhor; seja ele dado aos moços que seguem ao meu senhor.
28 Perdoa a transgressão da tua serva; pois, de fato, o Senhor te fará casa firme, porque pelejas as batalhas do Senhor, e não se ache mal em ti por todos os teus dias.
29 Se algum homem se levantar para te perseguir e buscar a tua vida, então, a tua vida será atada no feixe dos que vivem com o Senhor, teu Deus; porém a vida de teus inimigos, este a arrojará como se a atirasse da cavidade de uma funda.
30 E há de ser que, usando o Senhor contigo segundo todo o bem que tem dito a teu respeito e te houver estabelecido príncipe sobre Israel,
31 então, meu senhor, não te será por tropeço, nem por pesar ao coração o sangue que, sem causa, vieres a derramar e o te haveres vingado com as tuas próprias mãos; quando o Senhor te houver feito o bem, lembrar-te-ás da tua serva.
32 Então, Davi disse a Abigail: Bendito o Senhor, Deus de Israel, que, hoje, te enviou ao meu encontro.
33 Bendita seja a tua prudência, e bendita sejas tu mesma, que hoje me tolheste de derramar sangue e de que por minha própria mão me vingasse.
34 Porque, tão certo como vive o Senhor, Deus de Israel, que me impediu de que te fizesse mal, se tu não te apressaras e me não vieras ao encontro, não teria ficado a Nabal, até ao amanhecer, nem um sequer do sexo masculino.
35 Então, Davi recebeu da mão de Abigail o que esta lhe havia trazido e lhe disse: Sobe em paz à tua casa; bem vês que ouvi a tua petição e a ela atendi.
36 Voltou Abigail a Nabal. Eis que ele fazia em casa um banquete, como banquete de rei; o seu coração estava alegre, e ele, já mui embriagado, pelo que não lhe referiu ela coisa alguma, nem pouco nem muito, até ao amanhecer.
37 Pela manhã, estando Nabal já livre do vinho, sua mulher lhe deu a entender aquelas coisas; e se amorteceu nele o coração, e ficou ele como pedra.
38 Passados uns dez dias, feriu o Senhor a Nabal, e este morreu.
39 Ouvindo Davi que Nabal morrera, disse: Bendito seja o Senhor, que pleiteou a causa da afronta que recebi de Nabal e me deteve de fazer o mal, fazendo o Senhor cair o mal de Nabal sobre a sua cabeça. Mandou Davi falar a Abigail que desejava tomá-la por mulher.
40 Tendo ido os servos de Davi a Abigail, no Carmelo, lhe disseram: Davi nos mandou a ti, para te levar por sua mulher.
41 Então, ela se levantou, e se inclinou com o rosto em terra, e disse: Eis que a tua serva é criada para lavar os pés aos criados de meu senhor.
42 Abigail se apressou e, dispondo-se, cavalgou um jumento com as cinco moças que a assistiam; e ela seguiu os mensageiros de Davi, que a recebeu por mulher.
43 Também tomou Davi a Ainoã de Jezreel, e ambas foram suas mulheres,
44 porque Saul tinha dado sua filha Mical, mulher de Davi, a Palti, filho de Laís, o qual era de Galim.*
1 Vieram os zifeus a Saul, a Gibeá, e disseram: Não se acha Davi escondido no outeiro de Haquila, defronte de Jesimom?
2 Então, Saul se levantou e desceu ao deserto de Zife, e com ele, três mil homens escolhidos de Israel, a buscar a Davi.
3 Acampou-se Saul no outeiro de Haquila, defronte de Jesimom, junto ao caminho; porém Davi ficou no deserto, e, sabendo que Saul vinha para ali à sua procura,
4 enviou espias, e soube que Saul tinha vindo.
5 Davi se levantou, e veio ao lugar onde Saul acampara, e viu o lugar onde se deitaram Saul e Abner, filho de Ner, comandante do seu exército. Saul estava deitado no acampamento, e o povo, ao redor dele.
6 Disse Davi a Aimeleque, o heteu, e a Abisai, filho de Zeruia, irmão de Joabe: Quem descerá comigo a Saul, ao arraial? Respondeu Abisai: Eu descerei contigo.
7 Vieram, pois, Davi e Abisai, de noite, ao povo, e eis que Saul estava deitado, dormindo no acampamento, e a sua lança, fincada na terra à sua cabeceira; Abner e o povo estavam deitados ao redor dele.
8 Então, disse Abisai a Davi: Deus te entregou, hoje, nas mãos o teu inimigo; deixa-me, pois, agora, encravá-lo com a lança, ao chão, de um só golpe; não será preciso segundo.
9 Davi, porém, respondeu a Abisai: Não o mates, pois quem haverá que estenda a mão contra o ungido do Senhor e fique inocente?
10 Acrescentou Davi: Tão certo como vive o Senhor, este o ferirá, ou o seu dia chegará em que morra, ou em que, descendo à batalha, seja morto.
11 O Senhor me guarde de que eu estenda a mão contra o seu ungido; agora, porém, toma a lança que está à sua cabeceira e a bilha da água, e vamo-nos.
12 Tomou, pois, Davi a lança e a bilha da água da cabeceira de Saul, e foram-se; ninguém o viu, nem o soube, nem se despertou, pois todos dormiam, porquanto, da parte do Senhor, lhes havia caído profundo sono.
13 Tendo Davi passado ao outro lado, pôs-se no cimo do monte ao longe, de maneira que entre eles havia grande distância.
14 Bradou ao povo e a Abner, filho de Ner, dizendo: Não respondes, Abner? Então, Abner acudiu e disse: Quem és tu, que bradas ao rei?
15 Então, disse Davi a Abner: Porventura, não és homem? E quem há em Israel como tu? Por que, pois, não guardaste o rei, teu senhor? Porque veio um do povo para destruir o rei, teu senhor.
16 Não é bom isso que fizeste; tão certo como vive o Senhor, deveis morrer, vós que não guardastes a vosso senhor, o ungido do Senhor; vede, agora, onde está a lança do rei e a bilha da água, que tinha à sua cabeceira.
17 Então, reconheceu Saul a voz de Davi e disse: Não é a tua voz, meu filho Davi? Respondeu Davi: Sim, a minha, ó rei, meu senhor.
18 Disse mais: Por que persegue o meu senhor assim seu servo? Pois que fiz eu? E que maldade se acha nas minhas mãos?
19 Ouve, pois, agora, te rogo, ó rei, meu senhor, as palavras de teu servo: se é o Senhor que te incita contra mim, aceite ele a oferta de manjares; porém, se são os filhos dos homens, malditos sejam perante o Senhor; pois eles me expulsaram hoje, para que eu não tenha parte na herança do Senhor, como que dizendo: Vai, serve a outros deuses.
20 Agora, pois, não se derrame o meu sangue longe desta terra do Senhor; pois saiu o rei de Israel em busca de uma pulga, como quem persegue uma perdiz nos montes.
21 Então, disse Saul: Pequei; volta, meu filho Davi, pois não tornarei a fazer-te mal; porque foi, hoje, preciosa a minha vida aos teus olhos. Eis que tenho procedido como louco e errado excessivamente.
22 Davi, então, respondeu e disse: Eis aqui a lança, ó rei; venha aqui um dos moços e leve-a.
23 Pague, porém, o Senhor a cada um a sua justiça e a sua lealdade; pois o Senhor te havia entregado, hoje, nas minhas mãos, porém eu não quis estendê-las contra o ungido do Senhor.
24 Assim como foi a tua vida, hoje, de muita estima aos meus olhos, assim também seja a minha aos olhos do Senhor, e ele me livre de toda tribulação.
25 Então, Saul disse a Davi: Bendito sejas tu, meu filho Davi; pois grandes coisas farás e, de fato, prevalecerás. Então, Davi continuou o seu caminho, e Saul voltou para o seu lugar.*
1 Disse, porém, Davi consigo mesmo: Pode ser que algum dia venha eu a perecer nas mãos de Saul; nada há, pois, melhor para mim do que fugir para a terra dos filisteus; para que Saul perca de todo as esperanças e deixe de perseguir-me por todos os limites de Israel; assim, me livrarei da sua mão.
2 Dispôs-se Davi e, com os seiscentos homens que com ele estavam, passou a Aquis, filho de Maoque, rei de Gate.
3 Habitou Davi com Aquis em Gate, ele e os seus homens, cada um com a sua família; Davi, com ambas as suas mulheres, Ainoã, a jezreelita, e Abigail, a viúva de Nabal, o carmelita.
4 Avisado Saul de que Davi tinha fugido para Gate, desistiu de o perseguir.
5 Disse Davi a Aquis: Se achei mercê na tua presença, dá-me lugar numa das cidades da terra, para que ali habite; por que há de habitar o teu servo contigo na cidade real?
6 Então, lhe deu Aquis, naquele dia, a cidade de Ziclague. Pelo que Ziclague pertence aos reis de Judá, até ao dia de hoje.
7 E todo o tempo que Davi permaneceu na terra dos filisteus foi um ano e quatro meses.
8 Subia Davi com os seus homens, e davam contra os gesuritas, os gersitas e os amalequitas; porque eram estes os moradores da terra desde Telã, na direção de Sur, até à terra do Egito.
9 Davi feria aquela terra, e não deixava com vida nem homem nem mulher, e tomava as ovelhas, e os bois, e os jumentos, e os camelos, e as vestes; voltava e vinha a Aquis.
10 E perguntando Aquis: Contra quem deste hoje? Davi respondia: Contra o Sul de Judá, e o Sul dos jerameelitas, e o Sul dos queneus.
11 Davi não deixava com vida nem homem nem mulher, para os trazer a Gate, pois dizia: Para que não nos denunciem, dizendo: Assim Davi o fazia. Este era o seu proceder por todos os dias que habitou na terra dos filisteus.
12 Aquis confiava em Davi, dizendo: Fez-se ele, por certo, aborrecível para com o seu povo em Israel; pelo que me será por servo para sempre.*
1 Sucedeu, naqueles dias, que, juntando os filisteus os seus exércitos para a peleja, para fazer guerra contra Israel, disse Aquis a Davi: Fica sabendo que comigo sairás à peleja, tu e os teus homens.
2 Então, disse Davi a Aquis: Assim saberás quanto pode o teu servo fazer. Disse Aquis a Davi: Por isso, te farei minha guarda pessoal para sempre.
3 Já Samuel era morto, e todo o Israel o tinha chorado e o tinha sepultado em Ramá, que era a sua cidade; Saul havia desterrado os médiuns e os adivinhos.
4 Ajuntaram-se os filisteus e vieram acampar-se em Suném; ajuntou Saul a todo o Israel, e se acamparam em Gilboa.
5 Vendo Saul o acampamento dos filisteus, foi tomado de medo, e muito se estremeceu o seu coração.
6 Consultou Saul ao Senhor, porém o Senhor não lhe respondeu, nem por sonhos, nem por Urim, nem por profetas.
7 Então, disse Saul aos seus servos: Apontai-me uma mulher que seja médium, para que me encontre com ela e a consulte. Disseram-lhe os seus servos: Há uma mulher em En-Dor que é médium.
8 Saul disfarçou-se, vestiu outras roupas e se foi, e com ele, dois homens, e, de noite, chegaram à mulher; e lhe disse: Peço-te que me adivinhes pela necromancia e me faças subir aquele que eu te disser.
9 Respondeu-lhe a mulher: Bem sabes o que fez Saul, como eliminou da terra os médiuns e adivinhos; por que, pois, me armas cilada à minha vida, para me matares?
10 Então, Saul lhe jurou pelo Senhor, dizendo: Tão certo como vive o Senhor, nenhum castigo te sobrevirá por isso.
11 Então, lhe disse a mulher: Quem te farei subir? Respondeu ele: Faze-me subir Samuel.
12 Vendo a mulher a Samuel, gritou em alta voz; e a mulher disse a Saul: Por que me enganaste? Pois tu mesmo és Saul.
13 Respondeu-lhe o rei: Não temas; que vês? Então, a mulher respondeu a Saul: Vejo um deus que sobe da terra.
14 Perguntou ele: Como é a sua figura? Respondeu ela: Vem subindo um ancião e está envolto numa capa. Entendendo Saul que era Samuel, inclinou-se com o rosto em terra e se prostrou.
15 Samuel disse a Saul: Por que me inquietaste, fazendo-me subir? Então, disse Saul: Mui angustiado estou, porque os filisteus guerreiam contra mim, e Deus se desviou de mim e já não me responde, nem pelo ministério dos profetas, nem por sonhos; por isso, te chamei para que me reveles o que devo fazer.
16 Então, disse Samuel: Por que, pois, a mim me perguntas, visto que o Senhor te desamparou e se fez teu inimigo?
17 Porque o Senhor fez para contigo como, por meu intermédio, ele te dissera; tirou o reino da tua mão e o deu ao teu companheiro Davi.
18 Como tu não deste ouvidos à voz do Senhor e não executaste o que ele, no furor da sua ira, ordenou contra Amaleque, por isso, o Senhor te fez, hoje, isto.
19 O Senhor entregará também a Israel contigo nas mãos dos filisteus, e, amanhã, tu e teus filhos estareis comigo; e o acampamento de Israel o Senhor entregará nas mãos dos filisteus.
20 De súbito, caiu Saul estendido por terra e foi tomado de grande medo por causa das palavras de Samuel; e faltavam-lhe as forças, porque não comera pão todo aquele dia e toda aquela noite.
21 Aproximou-se de Saul a mulher e, vendo-o assaz perturbado, disse-lhe: Eis que a tua serva deu ouvidos à tua voz, e, arriscando a minha vida, atendi às palavras que me falaste.
22 Agora, pois, ouve também tu as palavras da tua serva e permite que eu ponha um bocado de pão diante de ti; come, para que tenhas forças e te ponhas a caminho.
23 Porém ele o recusou e disse: Não comerei. Mas os seus servos e a mulher o constrangeram; e atendeu. Levantou-se do chão e se assentou no leito.
24 Tinha a mulher em casa um bezerro cevado; apressou-se e matou-o, e, tomando farinha, a amassou, e a cozeu em bolos asmos.
25 E os trouxe diante de Saul e de seus servos, e comeram. Depois, se levantaram e se foram naquela mesma noite.*
1 Ajuntaram os filisteus todos os seus exércitos em Afeca, e acamparam-se os israelitas junto à fonte que está em Jezreel.
2 Os príncipes dos filisteus se foram para lá com centenas e com milhares; e Davi e seus homens iam com Aquis, na retaguarda.
3 Disseram, então, os príncipes dos filisteus: Estes hebreus, que fazem aqui? Respondeu Aquis aos príncipes dos filisteus: Não é este Davi, o servo de Saul, rei de Israel, que esteve comigo há muitos dias ou anos? E coisa nenhuma achei contra ele desde o dia em que, tendo desertado, passou para mim, até ao dia de hoje.
4 Porém os príncipes dos filisteus muito se indignaram contra ele; e lhe disseram: Faze voltar este homem, para que torne ao lugar que lhe designaste e não desça conosco à batalha, para que não se faça nosso adversário no combate; pois de que outro modo se reconciliaria como o seu senhor? Não seria, porventura, com as cabeças destes homens?
5 Não é este aquele Davi, de quem uns aos outros respondiam nas danças, dizendo: Saul feriu os seus milhares, porém Davi, os seus dez milhares?
6 Então, Aquis chamou a Davi e lhe disse: Tão certo como vive o Senhor, tu és reto, e me parece bem que tomes parte comigo nesta campanha; porque nenhum mal tenho achado em ti, desde o dia em que passaste para mim até ao dia de hoje; porém aos príncipes não agradas.
7 Volta, pois, agora, e volta em paz, para que não desagrades aos príncipes dos filisteus.
8 Então, Davi disse a Aquis: Porém que fiz eu? Ou que achaste no teu servo, desde o dia em que entrei para o teu serviço até hoje, para que não vá pelejar contra os inimigos do rei, meu senhor?
9 Respondeu, porém, Aquis e disse a Davi: Bem o sei; e que, na verdade, aos meus olhos és bom como um anjo de Deus; porém os príncipes dos filisteus disseram: Não suba este conosco à batalha.
10 Levanta-te, pois, amanhã de madrugada com os teus servos, que vieram contigo; e, levantando-vos, logo que haja luz, parti.
11 Então, Davi de madrugada se levantou, ele e os seus homens, para partirem e voltarem à terra dos filisteus. Os filisteus, porém, subiram a Jezreel.*
1 Sucedeu, pois, que, chegando Davi e os seus homens, ao terceiro dia, a Ziclague, já os amalequitas tinham dado com ímpeto contra o Sul e Ziclague e a esta, ferido e queimado;
2 tinham levado cativas as mulheres que lá se achavam, porém a ninguém mataram, nem pequenos nem grandes; tão somente os levaram consigo e foram seu caminho.
3 Davi e os seus homens vieram à cidade, e ei-la queimada, e suas mulheres, seus filhos e suas filhas eram levados cativos.
4 Então, Davi e o povo que se achava com ele ergueram a voz e choraram, até não terem mais forças para chorar.
5 Também as duas mulheres de Davi foram levadas cativas: Ainoã, a jezreelita, e Abigail, a viúva de Nabal, o carmelita.
6 Davi muito se angustiou, pois o povo falava de apedrejá-lo, porque todos estavam em amargura, cada um por causa de seus filhos e de suas filhas; porém Davi se reanimou no Senhor, seu Deus.
7 Disse Davi a Abiatar, o sacerdote, filho de Aimeleque: Traze-me aqui a estola sacerdotal. E Abiatar a trouxe a Davi.
8 Então, consultou Davi ao Senhor, dizendo: Perseguirei eu o bando? Alcançá-lo-ei? Respondeu-lhe o Senhor: Persegue-o, porque, de fato, o alcançarás e tudo libertarás.
9 Partiu, pois, Davi, ele e os seiscentos homens que com ele se achavam, e chegaram ao ribeiro de Besor, onde os retardatários ficaram.
10 Davi, porém, e quatrocentos homens continuaram a perseguição, pois que duzentos ficaram atrás, por não poderem, de cansados que estavam, passar o ribeiro de Besor.
11 Acharam no campo um homem egípcio e o trouxeram a Davi; deram-lhe pão, e comeu, e deram-lhe a beber água.
12 Deram-lhe também um pedaço de pasta de figos secos e dois cachos de passas, e comeu; recobrou, então, o alento, pois havia três dias e três noites que não comia pão, nem bebia água.
13 Então, lhe perguntou Davi: De quem és tu e de onde vens? Respondeu o moço egípcio: Sou servo de um amalequita, e meu senhor me deixou aqui, porque adoeci há três dias.
14 Nós demos com ímpeto contra o lado sul dos queretitas, contra o território de Judá e contra o lado sul de Calebe e pusemos fogo em Ziclague.
15 Disse-lhe Davi: Poderias, descendo, guiar-me a esse bando? Respondeu-lhe: Jura-me, por Deus, que me não matarás, nem me entregarás nas mãos de meu senhor, e descerei e te guiarei a esse bando.
16 E, descendo, o guiou. Eis que estavam espalhados sobre toda a região, comendo, bebendo e fazendo festa por todo aquele grande despojo que tomaram da terra dos filisteus e da terra de Judá.
17 Feriu-os Davi, desde o crepúsculo vespertino até à tarde do dia seguinte, e nenhum deles escapou, senão só quatrocentos moços que, montados em camelos, fugiram.
18 Assim, Davi salvou tudo quanto haviam tomado os amalequitas; também salvou as suas duas mulheres.
19 Não lhes faltou coisa alguma, nem pequena nem grande, nem os filhos, nem as filhas, nem o despojo, nada do que lhes haviam tomado: tudo Davi tornou a trazer.
20 Também tomou Davi todas as ovelhas e o gado, e o levaram diante de Davi e diziam: Este é o despojo de Davi.
21 Chegando Davi aos duzentos homens que, de cansados que estavam, não o puderam seguir e ficaram no ribeiro de Besor, estes saíram ao encontro de Davi e do povo que com ele vinha; Davi, aproximando-se destes, os saudou cordialmente.
22 Então, todos os maus e filhos de Belial, dentre os homens que tinham ido com Davi, responderam e disseram: Visto que não foram conosco, não lhes daremos do despojo que salvamos; cada um, porém, leve sua mulher e seus filhos e se vá embora.
23 Porém Davi disse: Não fareis assim, irmãos meus, com o que nos deu o Senhor, que nos guardou e entregou às nossas mãos o bando que contra nós vinha.
24 Quem vos daria ouvidos nisso? Porque qual é a parte dos que desceram à peleja, tal será a parte dos que ficaram com a bagagem; receberão partes iguais.
25 E assim, desde aquele dia em diante, foi isso estabelecido por estatuto e direito em Israel, até ao dia de hoje.
26 Chegando Davi a Ziclague, enviou do despojo aos anciãos de Judá, seus amigos, dizendo: Eis para vós outros um presente do despojo dos inimigos do Senhor:
27 aos de Betel, aos de Ramote do Neguebe, aos de Jatir,
28 aos de Aroer, aos de Sifmote, aos de Estemoa,
29 aos de Racal, aos que estavam nas cidades dos jerameelitas e nas cidades dos queneus,
30 aos de Horma, aos de Borasã, aos de Atace,
31 aos de Hebrom e a todos os lugares em que andara Davi, ele e os seus homens.*
1 Entretanto, os filisteus pelejaram contra Israel, e, tendo os homens de Israel fugido de diante dos filisteus, caíram feridos no monte Gilboa.
2 Os filisteus apertaram com Saul e seus filhos e mataram Jônatas, Abinadabe e Malquisua, filhos de Saul.
3 Agravou-se a peleja contra Saul; os flecheiros o avistaram, e ele muito os temeu.
4 Então, disse Saul ao seu escudeiro: Arranca a tua espada e atravessa-me com ela, para que, porventura, não venham estes incircuncisos, e me traspassem, e escarneçam de mim. Porém o seu escudeiro não o quis, porque temia muito; então, Saul tomou da espada e se lançou sobre ela.
5 Vendo, pois, o seu escudeiro que Saul já era morto, também ele se lançou sobre a sua espada e morreu com ele.
6 Morreu, pois, Saul, e seus três filhos, e o seu escudeiro, e também todos os seus homens foram mortos naquele dia com ele.
7 Vendo os homens de Israel que estavam deste lado do vale e daquém do Jordão que os homens de Israel fugiram e que Saul e seus filhos estavam mortos, desampararam as cidades e fugiram; e vieram os filisteus e habitaram nelas.
8 Sucedeu, pois, que, vindo os filisteus ao outro dia a despojar os mortos, acharam Saul e seus três filhos caídos no monte Gilboa.
9 Cortaram a cabeça a Saul e o despojaram das suas armas; enviaram mensageiros pela terra dos filisteus, em redor, a levar as boas-novas à casa dos seus ídolos e entre o povo.
10 Puseram as armas de Saul no templo de Astarote e o seu corpo afixaram no muro de Bete-Seã.
11 Então, ouvindo isto os moradores de Jabes-Gileade, o que os filisteus fizeram a Saul,
12 todos os homens valentes se levantaram, e caminharam toda a noite, e tiraram o corpo de Saul e os corpos de seus filhos do muro de Bete-Seã, e, vindo a Jabes, os queimaram.
13 Tomaram-lhes os ossos, e os sepultaram debaixo de um arvoredo, em Jabes, e jejuaram sete dias.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'1 Samuel','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)