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
1 Havia um homem na terra de Uz, cujo nome era Jó; homem íntegro e reto, temente a Deus e que se desviava do mal.
2 Nasceram-lhe sete filhos e três filhas.
3 Possuía sete mil ovelhas, três mil camelos, quinhentas juntas de bois e quinhentas jumentas; era também mui numeroso o pessoal ao seu serviço, de maneira que este homem era o maior de todos os do Oriente.
4 Seus filhos iam às casas uns dos outros e faziam banquetes, cada um por sua vez, e mandavam convidar as suas três irmãs a comerem e beberem com eles.
5 Decorrido o turno de dias de seus banquetes, chamava Jó a seus filhos e os santificava; levantava-se de madrugada e oferecia holocaustos segundo o número de todos eles, pois dizia: Talvez tenham pecado os meus filhos e blasfemado contra Deus em seu coração. Assim o fazia Jó continuamente.
6 Num dia em que os filhos de Deus vieram apresentar-se perante o Senhor, veio também Satanás entre eles.
7 Então, perguntou o Senhor a Satanás: Donde vens? Satanás respondeu ao Senhor e disse: De rodear a terra e passear por ela.
8 Perguntou ainda o Senhor a Satanás: Observaste o meu servo Jó? Porque ninguém há na terra semelhante a ele, homem íntegro e reto, temente a Deus e que se desvia do mal.
9 Então, respondeu Satanás ao Senhor: Porventura, Jó debalde teme a Deus?
10 Acaso, não o cercaste com sebe, a ele, a sua casa e a tudo quanto tem? A obra de suas mãos abençoaste, e os seus bens se multiplicaram na terra.
11 Estende, porém, a mão, e toca-lhe em tudo quanto tem, e verás se não blasfema contra ti na tua face.
12 Disse o Senhor a Satanás: Eis que tudo quanto ele tem está em teu poder; somente contra ele não estendas a mão. E Satanás saiu da presença do Senhor.
13 Sucedeu um dia, em que seus filhos e suas filhas comiam e bebiam vinho na casa do irmão primogênito,
14 que veio um mensageiro a Jó e lhe disse: Os bois lavravam, e as jumentas pasciam junto a eles;
15 de repente, deram sobre eles os sabeus, e os levaram, e mataram aos servos a fio de espada; só eu escapei, para trazer-te a nova.
16 Falava este ainda quando veio outro e disse: Fogo de Deus caiu do céu, e queimou as ovelhas e os servos, e os consumiu; só eu escapei, para trazer-te a nova.
17 Falava este ainda quando veio outro e disse: Dividiram-se os caldeus em três bandos, deram sobre os camelos, os levaram e mataram aos servos a fio de espada; só eu escapei, para trazer-te a nova.
18 Também este falava ainda quando veio outro e disse: Estando teus filhos e tuas filhas comendo e bebendo vinho, em casa do irmão primogênito,
19 eis que se levantou grande vento do lado do deserto e deu nos quatro cantos da casa, a qual caiu sobre eles, e morreram; só eu escapei, para trazer-te a nova.
20 Então, Jó se levantou, rasgou o seu manto, rapou a cabeça e lançou-se em terra e adorou;
21 e disse: Nu saí do ventre de minha mãe e nu voltarei; o Senhor o deu e o Senhor o tomou; bendito seja o nome do Senhor!
22 Em tudo isto Jó não pecou, nem atribuiu a Deus falta alguma.*
1 Num dia em que os filhos de Deus vieram apresentar-se perante o Senhor, veio também Satanás entre eles apresentar-se perante o Senhor.
2 Então, o Senhor disse a Satanás: Donde vens? Respondeu Satanás ao Senhor e disse: De rodear a terra e passear por ela.
3 Perguntou o Senhor a Satanás: Observaste o meu servo Jó? Porque ninguém há na terra semelhante a ele, homem íntegro e reto, temente a Deus e que se desvia do mal. Ele conserva a sua integridade, embora me incitasses contra ele, para o consumir sem causa.
4 Então, Satanás respondeu ao Senhor: Pele por pele, e tudo quanto o homem tem dará pela sua vida.
5 Estende, porém, a mão, toca-lhe nos ossos e na carne e verás se não blasfema contra ti na tua face.
6 Disse o Senhor a Satanás: Eis que ele está em teu poder; mas poupa-lhe a vida.
7 Então, saiu Satanás da presença do Senhor e feriu a Jó de tumores malignos, desde a planta do pé até ao alto da cabeça.
8 Jó, sentado em cinza, tomou um caco para com ele raspar-se.
9 Então, sua mulher lhe disse: Ainda conservas a tua integridade? Amaldiçoa a Deus e morre.
10 Mas ele lhe respondeu: Falas como qualquer doida; temos recebido o bem de Deus e não receberíamos também o mal? Em tudo isto não pecou Jó com os seus lábios.
11 Ouvindo, pois, três amigos de Jó todo este mal que lhe sobreviera, chegaram, cada um do seu lugar: Elifaz, o temanita, Bildade, o suíta, e Zofar, o naamatita; e combinaram ir juntamente condoer-se dele e consolá-lo.
12 Levantando eles de longe os olhos e não o reconhecendo, ergueram a voz e choraram; e cada um, rasgando o seu manto, lançava pó ao ar sobre a cabeça.
13 Sentaram-se com ele na terra, sete dias e sete noites; e nenhum lhe dizia palavra alguma, pois viam que a dor era muito grande.*
1 Depois disto, passou Jó a falar e amaldiçoou o seu dia natalício.
2 Disse Jó:
3 Pereça o dia em que nasci e a noite em que se disse: Foi concebido um homem!
4 Converta-se aquele dia em trevas; e Deus, lá de cima, não tenha cuidado dele, nem resplandeça sobre ele a luz.
5 Reclamem-no as trevas e a sombra de morte; habitem sobre ele nuvens; espante-o tudo o que pode enegrecer o dia.
6 Aquela noite, que dela se apoderem densas trevas; não se regozije ela entre os dias do ano, não entre na conta dos meses.
7 Seja estéril aquela noite, e dela sejam banidos os sons de júbilo.
8 Amaldiçoem-na aqueles que sabem amaldiçoar o dia e sabem excitar o monstro marinho.
9 Escureçam-se as estrelas do crepúsculo matutino dessa noite; que ela espere a luz, e a luz não venha; que não veja as pálpebras dos olhos da alva,
10 pois não fechou as portas do ventre de minha mãe, nem escondeu dos meus olhos o sofrimento.
11 Por que não morri eu na madre? Por que não expirei ao sair dela?
12 Por que houve regaço que me acolhesse? E por que peitos, para que eu mamasse?
13 Porque já agora repousaria tranquilo; dormiria, e, então, haveria para mim descanso,
14 com os reis e conselheiros da terra que para si edificaram mausoléus;
15 ou com os príncipes que tinham ouro e encheram de prata as suas casas;
16 ou, como aborto oculto, eu não existiria, como crianças que nunca viram a luz.
17 Ali, os maus cessam de perturbar, e, ali, repousam os cansados.
18 Ali, os presos juntamente repousam e não ouvem a voz do feitor.
19 Ali, está tanto o pequeno como o grande e o servo livre de seu senhor.
20 Por que se concede luz ao miserável e vida aos amargurados de ânimo,
21 que esperam a morte, e ela não vem? Eles cavam em procura dela mais do que tesouros ocultos.
22 Eles se regozijariam por um túmulo e exultariam se achassem a sepultura.
23 Por que se concede luz ao homem, cujo caminho é oculto, e a quem Deus cercou de todos os lados?
24 Por que em vez do meu pão me vêm gemidos, e os meus lamentos se derramam como água?
25 Aquilo que temo me sobrevém, e o que receio me acontece.
26 Não tenho descanso, nem sossego, nem repouso, e já me vem grande perturbação.*
1 Então, respondeu Elifaz, o temanita, e disse:
2 Se intentar alguém falar-te, enfadar-te-ás? Quem, todavia, poderá conter as palavras?
3 Eis que tens ensinado a muitos e tens fortalecido mãos fracas.
4 As tuas palavras têm sustentado aos que tropeçavam, e os joelhos vacilantes tens fortificado.
5 Mas agora, em chegando a tua vez, tu te enfadas; sendo tu atingido, te perturbas.
6 Porventura, não é o teu temor de Deus aquilo em que confias, e a tua esperança, a retidão dos teus caminhos?
7 Lembra-te: acaso, já pereceu algum inocente? E onde foram os retos destruídos?
8 Segundo eu tenho visto, os que lavram a iniquidade e semeiam o mal, isso mesmo eles segam.
9 Com o hálito de Deus perecem; e com o assopro da sua ira se consomem.
10 Cessa o bramido do leão e a voz do leão feroz, e os dentes dos leõezinhos se quebram.
11 Perece o leão, porque não há presa, e os filhos da leoa andam dispersos.
12 Uma palavra se me disse em segredo; e os meus ouvidos perceberam um sussurro dela.
13 Entre pensamentos de visões noturnas, quando profundo sono cai sobre os homens,
14 sobrevieram-me o espanto e o tremor, e todos os meus ossos estremeceram.
15 Então, um espírito passou por diante de mim; fez-me arrepiar os cabelos do meu corpo;
16 parou ele, mas não lhe discerni a aparência; um vulto estava diante dos meus olhos; houve silêncio, e ouvi uma voz:
17 Seria, porventura, o mortal justo diante de Deus? Seria, acaso, o homem puro diante do seu Criador?
18 Eis que Deus não confia nos seus servos e aos seus anjos atribui imperfeições;
19 quanto mais àqueles que habitam em casas de barro, cujo fundamento está no pó, e são esmagados como a traça!
20 Nascem de manhã e à tarde são destruídos; perecem para sempre, sem que disso se faça caso.
21 Se se lhes corta o fio da vida, morrem e não atingem a sabedoria.*
1 Chama agora! Haverá alguém que te atenda? E para qual dos santos anjos te virarás?
2 Porque a ira do louco o destrói, e o zelo do tolo o mata.
3 Bem vi eu o louco lançar raízes; mas logo declarei maldita a sua habitação.
4 Seus filhos estão longe do socorro, são espezinhados às portas, e não há quem os livre.
5 A sua messe, o faminto a devora e até do meio dos espinhos a arrebata; e o intrigante abocanha os seus bens.
6 Porque a aflição não vem do pó, e não é da terra que brota o enfado.
7 Mas o homem nasce para o enfado, como as faíscas das brasas voam para cima.
8 Quanto a mim, eu buscaria a Deus e a ele entregaria a minha causa;
9 ele faz coisas grandes e inescrutáveis e maravilhas que não se podem contar;
10 faz chover sobre a terra e envia águas sobre os campos,
11 para pôr os abatidos num lugar alto e para que os enlutados se alegrem da maior ventura.
12 Ele frustra as maquinações dos astutos, para que as suas mãos não possam realizar seus projetos.
13 Ele apanha os sábios na sua própria astúcia; e o conselho dos que tramam se precipita.
14 Eles de dia encontram as trevas; ao meio-dia andam como de noite, às apalpadelas.
15 Porém Deus salva da espada que lhes sai da boca, salva o necessitado da mão do poderoso.
16 Assim, há esperança para o pobre, e a iniquidade tapa a sua própria boca.
17 Bem-aventurado é o homem a quem Deus disciplina; não desprezes, pois, a disciplina do Todo-Poderoso.
18 Porque ele faz a ferida e ele mesmo a ata; ele fere, e as suas mãos curam.
19 De seis angústias te livrará, e na sétima o mal te não tocará.
20 Na fome te livrará da morte; na guerra, do poder da espada.
21 Do açoite da língua estarás abrigado e, quando vier a assolação, não a temerás.
22 Da assolação e da fome te rirás e das feras da terra não terás medo.
23 Porque até com as pedras do campo terás a tua aliança, e os animais da terra viverão em paz contigo.
24 Saberás que a paz é a tua tenda, percorrerás as tuas possessões, e nada te faltará.
25 Saberás também que se multiplicará a tua descendência, e a tua posteridade, como a erva da terra.
26 Em robusta velhice entrarás para a sepultura, como se recolhe o feixe de trigo a seu tempo.
27 Eis que isto já o havemos inquirido, e assim é; ouve-o e medita nisso para teu bem.*
1 Então, Jó respondeu:
2 Oh! Se a minha queixa, de fato, se pesasse, e contra ela, numa balança, se pusesse a minha miséria,
3 esta, na verdade, pesaria mais que a areia dos mares; por isso é que as minhas palavras foram precipitadas.
4 Porque as flechas do Todo-Poderoso estão em mim cravadas, e o meu espírito sorve o veneno delas; os terrores de Deus se arregimentam contra mim.
5 Zurrará o jumento montês junto à relva? Ou mugirá o boi junto à sua forragem?
6 Comer-se-á sem sal o que é insípido? Ou haverá sabor na clara do ovo?
7 Aquilo que a minha alma recusava tocar, isso é agora a minha comida repugnante.
8 Quem dera que se cumprisse o meu pedido, e que Deus me concedesse o que anelo!
9 Que fosse do agrado de Deus esmagar-me, que soltasse a sua mão e acabasse comigo!
10 Isto ainda seria a minha consolação, e saltaria de contente na minha dor, que ele não poupa; porque não tenho negado as palavras do Santo.
11 Por que esperar, se já não tenho forças? Por que prolongar a vida, se o meu fim é certo?
12 Acaso, a minha força é a força da pedra? Ou é de bronze a minha carne?
13 Não! Jamais haverá socorro para mim; foram afastados de mim os meus recursos.
14 Ao aflito deve o amigo mostrar compaixão, a menos que tenha abandonado o temor do Todo-Poderoso.
15 Meus irmãos aleivosamente me trataram; são como um ribeiro, como a torrente que transborda no vale,
16 turvada com o gelo e com a neve que nela se esconde,
17 torrente que no tempo do calor seca, emudece e desaparece do seu lugar.
18 Desviam-se as caravanas dos seus caminhos, sobem para lugares desolados e perecem.
19 As caravanas de Temá procuram essa torrente, os viajantes de Sabá por ela suspiram.
20 Ficam envergonhados por terem confiado; em chegando ali, confundem-se.
21 Assim também vós outros sois nada para mim; vedes os meus males e vos espantais.
22 Acaso, disse eu: dai-me um presente? Ou: oferecei-me um suborno da vossa fazenda?
23 Ou: livrai-me do poder do opressor? Ou: redimi-me das mãos dos tiranos?
24 Ensinai-me, e eu me calarei; dai-me a entender em que tenho errado.
25 Oh! Como são persuasivas as palavras retas! Mas que é o que repreende a vossa repreensão?
26 Acaso, pensais em reprovar as minhas palavras, ditas por um desesperado ao vento?
27 Até sobre o órfão lançaríeis sorte e especularíeis com o vosso amigo?
28 Agora, pois, se sois servidos, olhai para mim e vede que não minto na vossa cara.
29 Tornai a julgar, vos peço, e não haja iniquidade; tornai a julgar, e a justiça da minha causa triunfará.
30 Há iniquidade na minha língua? Não pode o meu paladar discernir coisas perniciosas?*
1 Não é penosa a vida do homem sobre a terra? Não são os seus dias como os de um jornaleiro?
2 Como o escravo que suspira pela sombra e como o jornaleiro que espera pela sua paga,
3 assim me deram por herança meses de desengano e noites de aflição me proporcionaram.
4 Ao deitar-me, digo: quando me levantarei? Mas comprida é a noite, e farto-me de me revolver na cama, até à alva.
5 A minha carne está vestida de vermes e de crostas terrosas; a minha pele se encrosta e de novo supura.
6 Os meus dias são mais velozes do que a lançadeira do tecelão e se findam sem esperança.
7 Lembra-te de que a minha vida é um sopro; os meus olhos não tornarão a ver o bem.
8 Os olhos dos que agora me veem não me verão mais; os teus olhos me procurarão, mas já não serei.
9 Tal como a nuvem se desfaz e passa, aquele que desce à sepultura jamais tornará a subir.
10 Nunca mais tornará à sua casa, nem o lugar onde habita o conhecerá jamais.
11 Por isso, não reprimirei a boca, falarei na angústia do meu espírito, queixar-me-ei na amargura da minha alma.
12 Acaso, sou eu o mar ou algum monstro marinho, para que me ponhas guarda?
13 Dizendo eu: consolar-me-á o meu leito, a minha cama aliviará a minha queixa,
14 então, me espantas com sonhos e com visões me assombras;
15 pelo que a minha alma escolheria, antes, ser estrangulada; antes, a morte do que esta tortura.
16 Estou farto da minha vida; não quero viver para sempre. Deixa-me, pois, porque os meus dias são um sopro.
17 Que é o homem, para que tanto o estimes, e ponhas nele o teu cuidado,
18 e cada manhã o visites, e cada momento o ponhas à prova?
19 Até quando não apartarás de mim a tua vista? Até quando não me darás tempo de engolir a minha saliva?
20 Se pequei, que mal te fiz a ti, ó Espreitador dos homens? Por que fizeste de mim um alvo para ti, para que a mim mesmo me seja pesado?
21 Por que não perdoas a minha transgressão e não tiras a minha iniquidade? Pois agora me deitarei no pó; e, se me buscas, já não serei.*
1 Então, respondeu Bildade, o suíta:
2 Até quando falarás tais coisas? E até quando as palavras da tua boca serão qual vento impetuoso?
3 Perverteria Deus o direito ou perverteria o Todo-Poderoso a justiça?
4 Se teus filhos pecaram contra ele, também ele os lançou no poder da sua transgressão.
5 Mas, se tu buscares a Deus e ao Todo-Poderoso pedires misericórdia,
6 se fores puro e reto, ele, sem demora, despertará em teu favor e restaurará a justiça da tua morada.
7 O teu primeiro estado, na verdade, terá sido pequeno, mas o teu último crescerá sobremaneira.
8 Pois, eu te peço, pergunta agora a gerações passadas e atenta para a experiência de seus pais;
9 porque nós somos de ontem e nada sabemos; porquanto nossos dias sobre a terra são como a sombra.
10 Porventura, não te ensinarão os pais, não haverão de falar-te e do próprio entendimento não proferirão estas palavras:
11 Pode o papiro crescer sem lodo? Ou viça o junco sem água?
12 Estando ainda na sua verdura e ainda não colhidos, todavia, antes de qualquer outra erva se secam.
13 São assim as veredas de todos quantos se esquecem de Deus; e a esperança do ímpio perecerá.
14 A sua firmeza será frustrada, e a sua confiança é teia de aranha.
15 Encostar-se-á à sua casa, e ela não se manterá, agarrar-se-á a ela, e ela não ficará em pé.
16 Ele é viçoso perante o sol, e os seus renovos irrompem no seu jardim;
17 as suas raízes se entrelaçam num montão de pedras e penetram até às muralhas.
18 Mas, se Deus o arranca do seu lugar, então, este o negará, dizendo: Nunca te vi.
19 Eis em que deu a sua vida! E do pó brotarão outros.
20 Eis que Deus não rejeita ao íntegro, nem toma pela mão os malfeitores.
21 Ele te encherá a boca de riso e os teus lábios, de júbilo.
22 Teus aborrecedores se vestirão de ignomínia, e a tenda dos perversos não subsistirá.*
1 Então, Jó respondeu e disse:
2 Na verdade, sei que assim é; porque, como pode o homem ser justo para com Deus?
3 Se quiser contender com ele, nem a uma de mil coisas lhe poderá responder.
4 Ele é sábio de coração e grande em poder; quem porfiou com ele e teve paz?
5 Ele é quem remove os montes, sem que saibam que ele na sua ira os transtorna;
6 quem move a terra para fora do seu lugar, cujas colunas estremecem;
7 quem fala ao sol, e este não sai, e sela as estrelas;
8 quem sozinho estende os céus e anda sobre os altos do mar;
9 quem fez a Ursa, o Órion, o Sete-estrelo e as recâmaras do Sul;
10 quem faz grandes coisas, que se não podem esquadrinhar, e maravilhas tais, que se não podem contar.
11 Eis que ele passa por mim, e não o vejo; segue perante mim, e não o percebo.
12 Eis que arrebata a presa! Quem o pode impedir? Quem lhe dirá: Que fazes?
13 Deus não revogará a sua própria ira; debaixo dele se encurvam os auxiliadores do Egito.
14 Como, então, lhe poderei eu responder ou escolher as minhas palavras, para argumentar com ele?
15 A ele, ainda que eu fosse justo, não lhe responderia; antes, ao meu Juiz pediria misericórdia.
16 Ainda que o chamasse, e ele me respondesse, nem por isso creria eu que desse ouvidos à minha voz.
17 Porque me esmaga com uma tempestade e multiplica as minhas chagas sem causa.
18 Não me permite respirar; antes, me farta de amarguras.
19 Se se trata da força do poderoso, ele dirá: Eis-me aqui; se, de justiça: Quem me citará?
20 Ainda que eu seja justo, a minha boca me condenará; embora seja eu íntegro, ele me terá por culpado.
21 Eu sou íntegro, não levo em conta a minha alma, não faço caso da minha vida.
22 Para mim tudo é o mesmo; por isso, digo: tanto destrói ele o íntegro como o perverso.
23 Se qualquer flagelo mata subitamente, então, se rirá do desespero do inocente.
24 A terra está entregue nas mãos dos perversos; e Deus ainda cobre o rosto dos juízes dela; se não é ele o causador disso, quem é, logo?
25 Os meus dias foram mais velozes do que um corredor; fugiram e não viram a felicidade.
26 Passaram como barcos de junco; como a águia que se lança sobre a presa.
27 Se eu disser: eu me esquecerei da minha queixa, deixarei o meu ar triste e ficarei contente;
28 ainda assim todas as minhas dores me apavoram, porque bem sei que me não terás por inocente.
29 Serei condenado; por que, pois, trabalho eu em vão?
30 Ainda que me lave com água de neve e purifique as mãos com cáustico,
31 mesmo assim me submergirás no lodo, e as minhas próprias vestes me abominarão.
32 Porque ele não é homem, como eu, a quem eu responda, vindo juntamente a juízo.
33 Não há entre nós árbitro que ponha a mão sobre nós ambos.
34 Tire ele a sua vara de cima de mim, e não me amedronte o seu terror;
35 então, falarei sem o temer; do contrário, não estaria em mim.*
1 A minha alma tem tédio à minha vida; darei livre curso à minha queixa, falarei com amargura da minha alma.
2 Direi a Deus: Não me condenes; faze-me saber por que contendes comigo.
3 Parece-te bem que me oprimas, que rejeites a obra das tuas mãos e favoreças o conselho dos perversos?
4 Tens tu olhos de carne? Acaso, vês tu como vê o homem?
5 São os teus dias como os dias do mortal? Ou são os teus anos como os anos de um homem,
6 para te informares da minha iniquidade e averiguares o meu pecado?
7 Bem sabes tu que eu não sou culpado; todavia, ninguém há que me livre da tua mão.
8 As tuas mãos me plasmaram e me aperfeiçoaram, porém, agora, queres devorar-me.
9 Lembra-te de que me formaste como em barro; e queres, agora, reduzir-me a pó?
10 Porventura, não me derramaste como leite e não me coalhaste como queijo?
11 De pele e carne me vestiste e de ossos e tendões me entreteceste.
12 Vida me concedeste na tua benevolência, e o teu cuidado a mim me guardou.
13 Estas coisas, as ocultaste no teu coração; mas bem sei o que resolveste contigo mesmo.
14 Se eu pecar, tu me observas; e da minha iniquidade não me perdoarás.
15 Se for perverso, ai de mim! E, se for justo, não ouso levantar a cabeça, pois estou cheio de ignomínia e olho para a minha miséria.
16 Porque, se a levanto, tu me caças como a um leão feroz e de novo revelas poder maravilhoso contra mim.
17 Tu renovas contra mim as tuas testemunhas e multiplicas contra mim a tua ira; males e lutas se sucedem contra mim.
18 Por que, pois, me tiraste da madre? Ah! Se eu morresse antes que olhos nenhuns me vissem!
19 Teria eu sido como se nunca existira e já do ventre teria sido levado à sepultura.
20 Não são poucos os meus dias? Cessa, pois, e deixa-me, para que por um pouco eu tome alento,
21 antes que eu vá para o lugar de que não voltarei, para a terra das trevas e da sombra da morte;
22 terra de negridão, de profunda escuridade, terra da sombra da morte e do caos, onde a própria luz é tenebrosa.*
1 Então, respondeu Zofar, o naamatita:
2 Porventura, não se dará resposta a esse palavrório? Acaso, tem razão o tagarela?
3 Será o caso de as tuas parolas fazerem calar os homens? E zombarás tu sem que ninguém te envergonhe?
4 Pois dizes: A minha doutrina é pura, e sou limpo aos teus olhos.
5 Oh! Falasse Deus, e abrisse os seus lábios contra ti,
6 e te revelasse os segredos da sabedoria, da verdadeira sabedoria, que é multiforme! Sabe, portanto, que Deus permite seja esquecida parte da tua iniquidade.
7 Porventura, desvendarás os arcanos de Deus ou penetrarás até à perfeição do Todo-Poderoso?
8 Como as alturas dos céus é a sua sabedoria; que poderás fazer? Mais profunda é ela do que o abismo; que poderás saber?
9 A sua medida é mais longa do que a terra e mais larga do que o mar.
10 Se ele passa, prende a alguém e chama a juízo, quem o poderá impedir?
11 Porque ele conhece os homens vãos e, sem esforço, vê a iniquidade.
12 Mas o homem estúpido se tornará sábio, quando a cria de um asno montês nascer homem.
13 Se dispuseres o coração e estenderes as mãos para Deus;
14 se lançares para longe a iniquidade da tua mão e não permitires habitar na tua tenda a injustiça,
15 então, levantarás o rosto sem mácula, estarás seguro e não temerás.
16 Pois te esquecerás dos teus sofrimentos e deles só terás lembrança como de águas que passaram.
17 A tua vida será mais clara que o meio-dia; ainda que lhe haja trevas, serão como a manhã.
18 Sentir-te-ás seguro, porque haverá esperança; olharás em derredor e dormirás tranquilo.
19 Deitar-te-ás, e ninguém te espantará; e muitos procurarão obter o teu favor.
20 Mas os olhos dos perversos desfalecerão, o seu refúgio perecerá; sua esperança será o render do espírito.*
1 Então, Jó respondeu:
2 Na verdade, vós sois o povo, e convosco morrerá a sabedoria.
3 Também eu tenho entendimento como vós; eu não vos sou inferior; quem não sabe coisas como essas?
4 Eu sou irrisão para os meus amigos; eu, que invocava a Deus, e ele me respondia; o justo e o reto servem de irrisão.
5 No pensamento de quem está seguro, há desprezo para o infortúnio, um empurrão para aquele cujos pés já vacilam.
6 As tendas dos tiranos gozam paz, e os que provocam a Deus estão seguros; têm o punho por seu deus.
7 Mas pergunta agora às alimárias, e cada uma delas to ensinará; e às aves dos céus, e elas to farão saber.
8 Ou fala com a terra, e ela te instruirá; até os peixes do mar to contarão.
9 Qual entre todos estes não sabe que a mão do Senhor fez isto?
10 Na sua mão está a alma de todo ser vivente e o espírito de todo o gênero humano.
11 Porventura, o ouvido não submete à prova as palavras, como o paladar prova as comidas?
12 Está a sabedoria com os idosos, e, na longevidade, o entendimento?
13 Não! Com Deus está a sabedoria e a força; ele tem conselho e entendimento.
14 O que ele deitar abaixo não se reedificará; lança na prisão, e ninguém a pode abrir.
15 Se retém as águas, elas secam; se as larga, devastam a terra.
16 Com ele está a força e a sabedoria; seu é o que erra e o que faz errar.
17 Aos conselheiros, leva-os despojados do seu cargo e aos juízes faz desvairar.
18 Dissolve a autoridade dos reis, e uma corda lhes cinge os lombos.
19 Aos sacerdotes, leva-os despojados do seu cargo e aos poderosos transtorna.
20 Aos eloquentes ele tira a palavra e tira o entendimento aos anciãos.
21 Lança desprezo sobre os príncipes e afrouxa o cinto dos fortes.
22 Das trevas manifesta coisas profundas e traz à luz a densa escuridade.
23 Multiplica as nações e as faz perecer; dispersa-as e de novo as congrega.
24 Tira o entendimento aos príncipes do povo da terra e os faz vaguear pelos desertos sem caminho.
25 Nas trevas andam às apalpadelas, sem terem luz, e os faz cambalear como ébrios.*
1 Eis que tudo isso viram os meus olhos, e os meus ouvidos o ouviram e entenderam.
2 Como vós o sabeis, também eu o sei; não vos sou inferior.
3 Mas falarei ao Todo-Poderoso e quero defender-me perante Deus.
4 Vós, porém, besuntais a verdade com mentiras e vós todos sois médicos que não valem nada.
5 Tomara vos calásseis de todo, que isso seria a vossa sabedoria!
6 Ouvi agora a minha defesa e atentai para os argumentos dos meus lábios.
7 Porventura, falareis perversidade em favor de Deus e a seu favor falareis mentiras?
8 Sereis parciais por ele? Contendereis a favor de Deus?
9 Ser-vos-ia bom, se ele vos esquadrinhasse? Ou zombareis dele, como se zomba de um homem qualquer?
10 Acerbamente vos repreenderá, se em oculto fordes parciais.
11 Porventura, não vos amedrontará a sua dignidade, e não cairá sobre vós o seu terror?
12 As vossas máximas são como provérbios de cinza, os vossos baluartes, baluartes de barro.
13 Calai-vos perante mim, e falarei eu, e venha sobre mim o que vier.
14 Tomarei a minha carne nos meus dentes e porei a vida na minha mão.
15 Eis que me matará, já não tenho esperança; contudo, defenderei o meu procedimento.
16 Também isto será a minha salvação, o fato de o ímpio não vir perante ele.
17 Atentai para as minhas razões e dai ouvidos à minha exposição.
18 Tenho já bem-encaminhada minha causa e estou certo de que serei justificado.
19 Quem há que possa contender comigo? Neste caso, eu me calaria e renderia o espírito.
20 Concede-me somente duas coisas; então, me não esconderei do teu rosto:
21 alivia a tua mão de sobre mim, e não me espante o teu terror.
22 Interpela-me, e te responderei ou deixa-me falar e tu me responderás.
23 Quantas culpas e pecados tenho eu? Notifica-me a minha transgressão e o meu pecado.
24 Por que escondes o rosto e me tens por teu inimigo?
25 Queres aterrorizar uma folha arrebatada pelo vento? E perseguirás a palha seca?
26 Pois decretas contra mim coisas amargas e me atribuis as culpas da minha mocidade.
27 Também pões os meus pés no tronco, observas todos os meus caminhos e traças limites à planta dos meus pés,
28 apesar de eu ser como uma coisa podre que se consome e como a roupa que é comida da traça.*
1 O homem, nascido de mulher, vive breve tempo, cheio de inquietação.
2 Nasce como a flor e murcha; foge como a sombra e não permanece;
3 e sobre tal homem abres os olhos e o fazes entrar em juízo contigo?
4 Quem da imundícia poderá tirar coisa pura? Ninguém!
5 Visto que os seus dias estão contados, contigo está o número dos seus meses; tu ao homem puseste limites além dos quais não passará.
6 Desvia dele os olhares, para que tenha repouso, até que, como o jornaleiro, tenha prazer no seu dia.
7 Porque há esperança para a árvore, pois, mesmo cortada, ainda se renovará, e não cessarão os seus rebentos.
8 Se envelhecer na terra a sua raiz, e no chão morrer o seu tronco,
9 ao cheiro das águas brotará e dará ramos como a planta nova.
10 O homem, porém, morre e fica prostrado; expira o homem e onde está?
11 Como as águas do lago se evaporam, e o rio se esgota e seca,
12 assim o homem se deita e não se levanta; enquanto existirem os céus, não acordará, nem será despertado do seu sono.
13 Que me encobrisses na sepultura e me ocultasses até que a tua ira se fosse, e me pusesses um prazo e depois te lembrasses de mim!
14 Morrendo o homem, porventura tornará a viver? Todos os dias da minha luta esperaria, até que eu fosse substituído.
15 Chamar-me-ias, e eu te responderia; terias saudades da obra de tuas mãos;
16 e até contarias os meus passos e não levarias em conta os meus pecados.
17 A minha transgressão estaria selada num saco, e terias encoberto as minhas iniquidades.
18 Como o monte que se esboroa e se desfaz, e a rocha que se remove do seu lugar,
19 como as águas gastam as pedras, e as cheias arrebatam o pó da terra, assim destróis a esperança do homem.
20 Tu prevaleces para sempre contra ele, e ele passa, mudas-lhe o semblante e o despedes para o além.
21 Os seus filhos recebem honras, e ele o não sabe; são humilhados, e ele o não percebe.
22 Ele sente as dores apenas de seu próprio corpo, e só a seu respeito sofre a sua alma.*
1 Então, respondeu Elifaz, o temanita:
2 Porventura, dará o sábio em resposta ciência de vento? E encher-se-á a si mesmo de vento oriental,
3 arguindo com palavras que de nada servem e com razões de que nada aproveita?
4 Tornas vão o temor de Deus e diminuis a devoção a ele devida.
5 Pois a tua iniquidade ensina à tua boca, e tu escolheste a língua dos astutos.
6 A tua própria boca te condena, e não eu; os teus lábios testificam contra ti.
7 És tu, porventura, o primeiro homem que nasceu? Ou foste formado antes dos outeiros?
8 Ou ouviste o secreto conselho de Deus e a ti só limitaste a sabedoria?
9 Que sabes tu, que nós não saibamos? Que entendes, que não haja em nós?
10 Também há entre nós encanecidos e idosos, muito mais idosos do que teu pai.
11 Porventura, fazes pouco caso das consolações de Deus e das suaves palavras que te dirigimos nós?
12 Por que te arrebata o teu coração? Por que flamejam os teus olhos,
13 para voltares contra Deus o teu furor e deixares sair tais palavras da tua boca?
14 Que é o homem, para que seja puro? E o que nasce de mulher, para ser justo?
15 Eis que Deus não confia nem nos seus santos; nem os céus são puros aos seus olhos,
16 quanto menos o homem, que é abominável e corrupto, que bebe a iniquidade como a água!
17 Escuta-me, mostrar-to-ei; e o que tenho visto te contarei,
18 o que os sábios anunciaram, que o ouviram de seus pais e não o ocultaram
19 (aos quais somente se dera a terra, e nenhum estranho passou por entre eles):
20 Todos os dias o perverso é atormentado, no curto número de anos que se reservam para o opressor.
21 O sonido dos horrores está nos seus ouvidos; na prosperidade lhe sobrevém o assolador.
22 Não crê que tornará das trevas, e sim que o espera a espada.
23 Por pão anda vagueando, dizendo: Onde está? Bem sabe que o dia das trevas lhe está preparado, à mão.
24 Assombram-no a angústia e a tribulação; prevalecem contra ele, como o rei preparado para a peleja,
25 porque estendeu a mão contra Deus e desafiou o Todo-Poderoso;
26 arremete contra ele obstinadamente, atrás da grossura dos seus escudos,
27 porquanto cobriu o rosto com a sua gordura e criou enxúndia nas ilhargas;
28 habitou em cidades assoladas, em casas em que ninguém devia morar, que estavam destinadas a se fazerem montões de ruínas.
29 Por isso, não se enriquecerá, nem subsistirá a sua fazenda, nem se estenderão seus bens pela terra.
30 Não escapará das trevas; a chama do fogo secará os seus renovos, e ao assopro da boca de Deus será arrebatado.
31 Não confie, pois, na vaidade, enganando-se a si mesmo, porque a vaidade será a sua recompensa.
32 Esta se lhe consumará antes dos seus dias, e o seu ramo não reverdecerá.
33 Sacudirá as suas uvas verdes, como a vide, e deixará cair a sua flor, como a oliveira;
34 pois a companhia dos ímpios será estéril, e o fogo consumirá as tendas de suborno.
35 Concebem a malícia e dão à luz a iniquidade, pois o seu coração só prepara enganos.*
1 Então, respondeu Jó:
2 Tenho ouvido muitas coisas como estas; todos vós sois consoladores molestos.
3 Porventura, não terão fim essas palavras de vento? Ou que é que te instiga para responderes assim?
4 Eu também poderia falar como vós falais; se a vossa alma estivesse em lugar da minha, eu poderia dirigir-vos um montão de palavras e menear contra vós outros a minha cabeça;
5 poderia fortalecer-vos com as minhas palavras, e a compaixão dos meus lábios abrandaria a vossa dor.
6 Se eu falar, a minha dor não cessa; se me calar, qual é o meu alívio?
7 Na verdade, as minhas forças estão exaustas; tu, ó Deus, destruíste a minha família toda.
8 Testemunha disto é que já me tornaste encarquilhado, a minha magreza já se levanta contra mim e me acusa cara a cara.
9 Na sua ira me despedaçou e tem animosidade contra mim; contra mim rangeu os dentes e, como meu adversário, aguça os olhos.
10 Homens abrem contra mim a boca, com desprezo me esbofeteiam, e contra mim todos se ajuntam.
11 Deus me entrega ao ímpio e nas mãos dos perversos me faz cair.
12 Em paz eu vivia, porém ele me quebrantou; pegou-me pelo pescoço e me despedaçou; pôs-me por seu alvo.
13 Cercam-me as suas flechas, atravessa-me os rins, e não me poupa, e o meu fel derrama na terra.
14 Fere-me com ferimento sobre ferimento, arremete contra mim como um guerreiro.
15 Cosi sobre a minha pele o cilício e revolvi o meu orgulho no pó.
16 O meu rosto está todo afogueado de chorar, e sobre as minhas pálpebras está a sombra da morte,
17 embora não haja violência nas minhas mãos, e seja pura a minha oração.
18 Ó terra, não cubras o meu sangue, e não haja lugar em que se oculte o meu clamor!
19 Já agora sabei que a minha testemunha está no céu, e, nas alturas, quem advoga a minha causa.
20 Os meus amigos zombam de mim, mas os meus olhos se desfazem em lágrimas diante de Deus,
21 para que ele mantenha o direito do homem contra o próprio Deus e o do filho do homem contra o seu próximo.
22 Porque dentro de poucos anos eu seguirei o caminho de onde não tornarei.*
1 O meu espírito se vai consumindo, os meus dias se vão apagando, e só tenho perante mim a sepultura.
2 Estou, de fato, cercado de zombadores, e os meus olhos são obrigados a lhes contemplar a provocação.
3 Dá-me, pois, um penhor; sê o meu fiador para contigo mesmo; quem mais haverá que se possa comprometer comigo?
4 Porque ao seu coração encobriste o entendimento, pelo que não os exaltarás.
5 Se alguém oferece os seus amigos como presa, os olhos de seus filhos desfalecerão.
6 Mas a mim me pôs por provérbio dos povos; tornei-me como aquele em cujo rosto se cospe.
7 Pelo que já se escureceram de mágoa os meus olhos, e já todos os meus membros são como a sombra;
8 os retos pasmam disto, e o inocente se levanta contra o ímpio.
9 Contudo, o justo segue o seu caminho, e o puro de mãos cresce mais e mais em força.
10 Mas tornai-vos, todos vós, e vinde cá; porque sábio nenhum acharei entre vós.
11 Os meus dias passaram, e se malograram os meus propósitos, as aspirações do meu coração.
12 Convertem-me a noite em dia, e a luz, dizem, está perto das trevas.
13 Mas, se eu aguardo já a sepultura por minha casa; se nas trevas estendo a minha cama;
14 se ao sepulcro eu clamo: tu és meu pai; e aos vermes: vós sois minha mãe e minha irmã,
15 onde está, pois, a minha esperança? Sim, a minha esperança, quem a poderá ver?
16 Ela descerá até às portas da morte, quando juntamente no pó teremos descanso.*
1 Então, respondeu Bildade, o suíta:
2 Até quando andarás à caça de palavras? Considera bem, e, então, falaremos.
3 Por que somos reputados por animais, e aos teus olhos passamos por curtos de inteligência?
4 Oh! Tu, que te despedaças na tua ira, será a terra abandonada por tua causa? Remover-se-ão as rochas do seu lugar?
5 Na verdade, a luz do perverso se apagará, e para seu fogo não resplandecerá a faísca;
6 a luz se escurecerá nas suas tendas, e a sua lâmpada sobre ele se apagará;
7 os seus passos fortes se estreitarão, e a sua própria trama o derribará.
8 Porque por seus próprios pés é lançado na rede e andará na boca de forje.
9 A armadilha o apanhará pelo calcanhar, e o laço o prenderá.
10 A corda está-lhe escondida na terra, e a armadilha, na vereda.
11 Os assombros o espantarão de todos os lados e o perseguirão a cada passo.
12 A calamidade virá faminta sobre ele, e a miséria estará alerta ao seu lado,
13 a qual lhe devorará os membros do corpo; serão devorados pelo primogênito da morte.
14 O perverso será arrancado da sua tenda, onde está confiado, e será levado ao rei dos terrores.
15 Nenhum dos seus morará na sua tenda, espalhar-se-á enxofre sobre a sua habitação.
16 Por baixo secarão as suas raízes, e murcharão por cima os seus ramos.
17 A sua memória desaparecerá da terra, e pelas praças não terá nome.
18 Da luz o lançarão nas trevas e o afugentarão do mundo.
19 Não terá filho nem posteridade entre o seu povo, nem sobrevivente algum ficará nas suas moradas.
20 Do seu dia se espantarão os do Ocidente, e os do Oriente serão tomados de horror.
21 Tais são, na verdade, as moradas do perverso, e este é o paradeiro do que não conhece a Deus.*
1 Então, respondeu Jó:
2 Até quando afligireis a minha alma e me quebrantareis com palavras?
3 Já dez vezes me vituperastes e não vos envergonhais de injuriar-me.
4 Embora haja eu, na verdade, errado, comigo ficará o meu erro.
5 Se quereis engrandecer-vos contra mim e me arguis pelo meu opróbrio,
6 sabei agora que Deus é que me oprimiu e com a sua rede me cercou.
7 Eis que clamo: violência! Mas não sou ouvido; grito: socorro! Porém não há justiça.
8 O meu caminho ele fechou, e não posso passar; e nas minhas veredas pôs trevas.
9 Da minha honra me despojou e tirou-me da cabeça a coroa.
10 Arruinou-me de todos os lados, e eu me vou; e arrancou-me a esperança, como a uma árvore.
11 Inflamou contra mim a sua ira e me tem na conta de seu adversário.
12 Juntas vieram as suas tropas, prepararam contra mim o seu caminho e se acamparam ao redor da minha tenda.
13 Pôs longe de mim a meus irmãos, e os que me conhecem, como estranhos, se apartaram de mim.
14 Os meus parentes me desampararam, e os meus conhecidos se esqueceram de mim.
15 Os que se abrigam na minha casa e as minhas servas me têm por estranho, e vim a ser estrangeiro aos seus olhos.
16 Chamo o meu criado, e ele não me responde; tenho de suplicar-lhe, eu mesmo.
17 O meu hálito é intolerável à minha mulher, e pelo mau cheiro sou repugnante aos filhos de minha mãe.
18 Até as crianças me desprezam, e, querendo eu levantar-me, zombam de mim.
19 Todos os meus amigos íntimos me abominam, e até os que eu amava se tornaram contra mim.
20 Os meus ossos se apegam à minha pele e à minha carne, e salvei-me só com a pele dos meus dentes.
21 Compadecei-vos de mim, amigos meus, compadecei-vos de mim, porque a mão de Deus me atingiu.
22 Por que me perseguis como Deus me persegue e não cessais de devorar a minha carne?
23 Quem me dera fossem agora escritas as minhas palavras! Quem me dera fossem gravadas em livro!
24 Que, com pena de ferro e com chumbo, para sempre fossem esculpidas na rocha!
25 Porque eu sei que o meu Redentor vive e por fim se levantará sobre a terra.
26 Depois, revestido este meu corpo da minha pele, em minha carne verei a Deus.
27 Vê-lo-ei por mim mesmo, os meus olhos o verão, e não outros; de saudade me desfalece o coração dentro de mim.
28 Se disserdes: Como o perseguiremos? E: A causa deste mal se acha nele,
29 temei, pois, a espada, porque tais acusações merecem o seu furor, para saberdes que há um juízo.*
1 Então, respondeu Zofar, o naamatita:
2 Visto que os meus pensamentos me impõem resposta, eu me apresso.
3 Eu ouvi a repreensão, que me envergonha, mas o meu espírito me obriga a responder segundo o meu entendimento.
4 Porventura, não sabes tu que desde todos os tempos, desde que o homem foi posto sobre a terra,
5 o júbilo dos perversos é breve, e a alegria dos ímpios, momentânea?
6 Ainda que a sua presunção remonte aos céus, e a sua cabeça atinja as nuvens,
7 como o seu próprio esterco, apodrecerá para sempre; e os que o conheceram dirão: Onde está?
8 Voará como um sonho e não será achado, será afugentado como uma visão da noite.
9 Os olhos que o viram jamais o verão, e o seu lugar não o verá outra vez.
10 Os seus filhos procurarão aplacar aos pobres, e as suas mãos lhes restaurarão os seus bens.
11 Ainda que os seus ossos estejam cheios do vigor da sua juventude, esse vigor se deitará com ele no pó.
12 Ainda que o mal lhe seja doce na boca, e ele o esconda debaixo da língua,
13 e o saboreie, e o não deixe; antes, o retenha no seu paladar,
14 contudo, a sua comida se transformará nas suas entranhas; fel de áspides será no seu interior.
15 Engoliu riquezas, mas vomitá-las-á; do seu ventre Deus as lançará.
16 Veneno de áspides sorveu; língua de víbora o matará.
17 Não se deliciará com a vista dos ribeiros e dos rios transbordantes de mel e de leite.
18 Devolverá o fruto do seu trabalho e não o engolirá; do lucro de sua barganha não tirará prazer nenhum.
19 Oprimiu e desamparou os pobres, roubou casas que não edificou.
20 Por não haver limites à sua cobiça, não chegará a salvar as coisas por ele desejadas.
21 Nada escapou à sua cobiça insaciável, pelo que a sua prosperidade não durará.
22 Na plenitude da sua abastança, ver-se-á angustiado; toda a força da miséria virá sobre ele.
23 Para encher a sua barriga, Deus mandará sobre ele o furor da sua ira, que, por alimento, mandará chover sobre ele.
24 Se fugir das armas de ferro, o arco de bronze o traspassará.
25 Ele arranca das suas costas a flecha, e esta vem resplandecente do seu fel; e haverá assombro sobre ele.
26 Todas as calamidades serão reservadas contra os seus tesouros; fogo não assoprado o consumirá, fogo que se apascentará do que ficar na sua tenda.
27 Os céus lhe manifestarão a sua iniquidade; e a terra se levantará contra ele.
28 As riquezas de sua casa serão transportadas; como água serão derramadas no dia da ira de Deus.
29 Tal é, da parte de Deus, a sorte do homem perverso, tal a herança decretada por Deus.*
1 Respondeu, porém, Jó:
2 Ouvi atentamente as minhas razões, e já isso me será a vossa consolação.
3 Tolerai-me, e eu falarei; e, havendo eu falado, podereis zombar.
4 Acaso, é do homem que eu me queixo? Não tenho motivo de me impacientar?
5 Olhai para mim e pasmai; e ponde a mão sobre a boca;
6 porque só de pensar nisso me perturbo, e um calafrio se apodera de toda a minha carne.
7 Como é, pois, que vivem os perversos, envelhecem e ainda se tornam mais poderosos?
8 Seus filhos se estabelecem na sua presença; e os seus descendentes, ante seus olhos.
9 As suas casas têm paz, sem temor, e a vara de Deus não os fustiga.
10 O seu touro gera e não falha, suas novilhas têm a cria e não abortam.
11 Deixam correr suas crianças, como a um rebanho, e seus filhos saltam de alegria;
12 cantam com tamboril e harpa e alegram-se ao som da flauta.
13 Passam eles os seus dias em prosperidade e em paz descem à sepultura.
14 E são estes os que disseram a Deus: Retira-te de nós! Não desejamos conhecer os teus caminhos.
15 Que é o Todo-Poderoso, para que nós o sirvamos? E que nos aproveitará que lhe façamos orações?
16 Vede, porém, que não provém deles a sua prosperidade; longe de mim o conselho dos perversos!
17 Quantas vezes sucede que se apaga a lâmpada dos perversos? Quantas vezes lhes sobrevém a destruição? Quantas vezes Deus na sua ira lhes reparte dores?
18 Quantas vezes são como a palha diante do vento e como a pragana arrebatada pelo remoinho?
19 Deus, dizeis vós, guarda a iniquidade do perverso para seus filhos. Mas é a ele que deveria Deus dar o pago, para que o sinta.
20 Seus próprios olhos devem ver a sua ruína, e ele, beber do furor do Todo-Poderoso.
21 Porque depois de morto, cortado já o número dos seus meses, que interessa a ele a sua casa?
22 Acaso, alguém ensinará ciência a Deus, a ele que julga os que estão nos céus?
23 Um morre em pleno vigor, despreocupado e tranquilo,
24 com seus baldes cheios de leite e fresca a medula dos seus ossos.
25 Outro, ao contrário, morre na amargura do seu coração, não havendo provado do bem.
26 Juntamente jazem no pó, onde os vermes os cobrem.
27 Vede que conheço os vossos pensamentos e os injustos desígnios com que me tratais.
28 Porque direis: Onde está a casa do príncipe, e onde, a tenda em que morava o perverso?
29 Porventura, não tendes interrogado os que viajam? E não considerastes as suas declarações,
30 que o mau é poupado no dia da calamidade, é socorrido no dia do furor?
31 Quem lhe lançará em rosto o seu proceder? Quem lhe dará o pago do que faz?
32 Finalmente, é levado à sepultura, e sobre o seu túmulo se faz vigilância.
33 Os torrões do vale lhe são leves, todos os homens o seguem, assim como não têm número os que foram adiante dele.
34 Como, pois, me consolais em vão? Das vossas respostas só resta falsidade.*
1 Então, respondeu Elifaz, o temanita:
2 Porventura, será o homem de algum proveito a Deus? Antes, o sábio é só útil a si mesmo.
3 Ou tem o Todo-Poderoso interesse em que sejas justo ou algum lucro em que faças perfeitos os teus caminhos?
4 Ou te repreende pelo teu temor de Deus ou entra contra ti em juízo?
5 Porventura, não é grande a tua malícia, e sem termo, as tuas iniquidades?
6 Porque sem causa tomaste penhores a teu irmão e aos seminus despojaste das suas roupas.
7 Não deste água a beber ao cansado e ao faminto retiveste o pão.
8 Ao braço forte pertencia a terra, e só os homens favorecidos habitavam nela.
9 As viúvas despediste de mãos vazias, e os braços dos órfãos foram quebrados.
10 Por isso, estás cercado de laços, e repentino pavor te conturba
11 ou trevas, em que nada vês; e águas transbordantes te cobrem.
12 Porventura, não está Deus nas alturas do céu? Olha para as estrelas mais altas. Que altura!
13 E dizes: Que sabe Deus? Acaso, poderá ele julgar através de densa escuridão?
14 Grossas nuvens o encobrem, de modo que não pode ver; ele passeia pela abóbada do céu.
15 Queres seguir a rota antiga, que os homens iníquos pisaram?
16 Estes foram arrebatados antes do tempo; o seu fundamento, uma torrente o arrasta.
17 Diziam a Deus: Retira-te de nós. E: Que pode fazer-nos o Todo-Poderoso?
18 Contudo, ele enchera de bens as suas casas. Longe de mim o conselho dos perversos!
19 Os justos o veem e se alegram, e o inocente escarnece deles,
20 dizendo: Na verdade, os nossos adversários foram destruídos, e o fogo consumiu o resto deles.
21 Reconcilia-te, pois, com ele e tem paz, e assim te sobrevirá o bem.
22 Aceita, peço-te, a instrução que profere e põe as suas palavras no teu coração.
23 Se te converteres ao Todo-Poderoso, serás restabelecido; se afastares a injustiça da tua tenda
24 e deitares ao pó o teu ouro e o ouro de Ofir entre pedras dos ribeiros,
25 então, o Todo-Poderoso será o teu ouro e a tua prata escolhida.
26 Deleitar-te-ás, pois, no Todo-Poderoso e levantarás o rosto para Deus.
27 Orarás a ele, e ele te ouvirá; e pagarás os teus votos.
28 Se projetas alguma coisa, ela te sairá bem, e a luz brilhará em teus caminhos.
29 Se estes descem, então, dirás: Para cima! E Deus salvará o humilde
30 e livrará até ao que não é inocente; sim, será libertado, graças à pureza de tuas mãos.*
1 Respondeu, porém, Jó:
2 Ainda hoje a minha queixa é de um revoltado, apesar de a minha mão reprimir o meu gemido.
3 Ah! Se eu soubesse onde o poderia achar! Então, me chegaria ao seu tribunal.
4 Exporia ante ele a minha causa, encheria a minha boca de argumentos.
5 Saberia as palavras que ele me respondesse e entenderia o que me dissesse.
6 Acaso, segundo a grandeza de seu poder, contenderia comigo? Não; antes, me atenderia.
7 Ali, o homem reto pleitearia com ele, e eu me livraria para sempre do meu juiz.
8 Eis que, se me adianto, ali não está; se torno para trás, não o percebo.
9 Se opera à esquerda, não o vejo; esconde-se à direita, e não o diviso.
10 Mas ele sabe o meu caminho; se ele me provasse, sairia eu como o ouro.
11 Os meus pés seguiram as suas pisadas; guardei o seu caminho e não me desviei dele.
12 Do mandamento de seus lábios nunca me apartei, escondi no meu íntimo as palavras da sua boca.
13 Mas, se ele resolveu alguma coisa, quem o pode dissuadir? O que ele deseja, isso fará.
14 Pois ele cumprirá o que está ordenado a meu respeito e muitas coisas como estas ainda tem consigo.
15 Por isso, me perturbo perante ele; e, quando o considero, temo-o.
16 Deus é quem me fez desmaiar o coração, e o Todo-Poderoso, quem me perturbou,
17 porque não estou desfalecido por causa das trevas, nem porque a escuridão cobre o meu rosto.*
1 Por que o Todo-Poderoso não designa tempos de julgamento? E por que os que o conhecem não veem tais dias?
2 Há os que removem os limites, roubam os rebanhos e os apascentam.
3 Levam do órfão o jumento, da viúva, tomam-lhe o boi.
4 Desviam do caminho aos necessitados, e os pobres da terra todos têm de esconder-se.
5 Como asnos monteses no deserto, saem estes para o seu mister, à procura de presa no campo aberto, como pão para eles e seus filhos.
6 No campo segam o pasto do perverso e lhe rabiscam a vinha.
7 Passam a noite nus por falta de roupa e não têm cobertas contra o frio.
8 Pelas chuvas das montanhas são molhados e, não tendo refúgio, abraçam-se com as rochas.
9 Orfãozinhos são arrancados ao peito, e dos pobres se toma penhor;
10 de modo que estes andam nus, sem roupa, e, famintos, arrastam os molhos.
11 Entre os muros desses perversos espremem o azeite, pisam-lhes o lagar; contudo, padecem sede.
12 Desde as cidades gemem os homens, e a alma dos feridos clama; e, contudo, Deus não tem isso por anormal.
13 Os perversos são inimigos da luz, não conhecem os seus caminhos, nem permanecem nas suas veredas.
14 De madrugada se levanta o homicida, mata ao pobre e ao necessitado, e de noite se torna ladrão.
15 Aguardam o crepúsculo os olhos do adúltero; este diz consigo: Ninguém me reconhecerá; e cobre o rosto.
16 Nas trevas minam as casas, de dia se conservam encerrados, nada querem com a luz.
17 Pois a manhã para todos eles é como sombra de morte; mas os terrores da noite lhes são familiares.
18 Vós dizeis: Os perversos são levados rapidamente na superfície das águas; maldita é a porção dos tais na terra; já não andam pelo caminho das vinhas.
19 A secura e o calor desfazem as águas da neve; assim faz a sepultura aos que pecaram.
20 A mãe se esquecerá deles, os vermes os comerão gostosamente; nunca mais haverá lembrança deles; como árvore será quebrado o injusto,
21 aquele que devora a estéril que não tem filhos e não faz o bem à viúva.
22 Não! Pelo contrário, Deus por sua força prolonga os dias dos valentes; veem-se eles de pé quando desesperavam da vida.
23 Ele lhes dá descanso, e nisso se estribam; os olhos de Deus estão nos caminhos deles.
24 São exaltados por breve tempo; depois, passam, colhidos como todos os mais; são cortados como as pontas das espigas.
25 Se não é assim, quem me desmentirá e anulará as minhas razões?*
1 Então, respondeu Bildade, o suíta:
2 A Deus pertence o domínio e o poder; ele faz reinar a paz nas alturas celestes.
3 Acaso, têm número os seus exércitos? E sobre quem não se levanta a sua luz?
4 Como, pois, seria justo o homem perante Deus, e como seria puro aquele que nasce de mulher?
5 Eis que até a lua não tem brilho, e as estrelas não são puras aos olhos dele.
6 Quanto menos o homem, que é gusano, e o filho do homem, que é verme!*
1 Jó, porém, respondeu:
2 Como sabes ajudar ao que não tem força e prestar socorro ao braço que não tem vigor!
3 Como sabes aconselhar ao que não tem sabedoria e revelar plenitude de verdadeiro conhecimento!
4 Com a ajuda de quem proferes tais palavras? E de quem é o espírito que fala em ti?
5 A alma dos mortos treme debaixo das águas com seus habitantes.
6 O além está desnudo perante ele, e não há coberta para o abismo.
7 Ele estende o norte sobre o vazio e faz pairar a terra sobre o nada.
8 Prende as águas em densas nuvens, e as nuvens não se rasgam debaixo delas.
9 Encobre a face do seu trono e sobre ele estende a sua nuvem.
10 Traçou um círculo à superfície das águas, até aos confins da luz e das trevas.
11 As colunas do céu tremem e se espantam da sua ameaça.
12 Com a sua força fende o mar e com o seu entendimento abate o adversário.
13 Pelo seu sopro aclara os céus, a sua mão fere o dragão veloz.
14 Eis que isto são apenas as orlas dos seus caminhos! Que leve sussurro temos ouvido dele! Mas o trovão do seu poder, quem o entenderá?*
1 Prosseguindo Jó em seu discurso, disse:
2 Tão certo como vive Deus, que me tirou o direito, e o Todo-Poderoso, que amargurou a minha alma,
3 enquanto em mim estiver a minha vida, e o sopro de Deus nos meus narizes,
4 nunca os meus lábios falarão injustiça, nem a minha língua pronunciará engano.
5 Longe de mim que eu vos dê razão! Até que eu expire, nunca afastarei de mim a minha integridade.
6 À minha justiça me apegarei e não a largarei; não me reprova a minha consciência por qualquer dia da minha vida.
7 Seja como o perverso o meu inimigo, e o que se levantar contra mim, como o injusto.
8 Porque qual será a esperança do ímpio, quando lhe for cortada a vida, quando Deus lhe arrancar a alma?
9 Acaso, ouvirá Deus o seu clamor, em lhe sobrevindo a tribulação?
10 Deleitar-se-á o perverso no Todo-Poderoso e invocará a Deus em todo o tempo?
11 Ensinar-vos-ei o que encerra a mão de Deus e não vos ocultarei o que está com o Todo-Poderoso.
12 Eis que todos vós já vistes isso; por que, pois, alimentais vãs noções?
13 Eis qual será da parte de Deus a porção do perverso e a herança que os opressores receberão do Todo-Poderoso:
14 Se os seus filhos se multiplicarem, será para a espada, e a sua prole não se fartará de pão.
15 Os que ficarem dela, a peste os enterrará, e as suas viúvas não chorarão.
16 Se o perverso amontoar prata como pó e acumular vestes como barro,
17 ele os acumulará, mas o justo é que os vestirá, e o inocente repartirá a prata.
18 Ele edifica a sua casa como a da traça e como a choça que o vigia constrói.
19 Rico se deita com a sua riqueza, abre os seus olhos e já não a vê.
20 Pavores se apoderam dele como inundação, de noite a tempestade o arrebata.
21 O vento oriental o leva, e ele se vai; varre-o com ímpeto do seu lugar.
22 Deus lança isto sobre ele e não o poupa, a ele que procura fugir precipitadamente da sua mão;
23 à sua queda lhe batem palmas, à saída o apupam com assobios.*
1 Na verdade, a prata tem suas minas, e o ouro, que se refina, o seu lugar.
2 O ferro tira-se da terra, e da pedra se funde o cobre.
3 Os homens põem termo à escuridão e até aos últimos confins procuram as pedras ocultas nas trevas e na densa escuridade.
4 Abrem entrada para minas longe da habitação dos homens, esquecidos dos transeuntes; e, assim, longe deles, dependurados, oscilam de um lado para outro.
5 Da terra procede o pão, mas embaixo é revolvida como por fogo.
6 Nas suas pedras se encontra safira, e há pó que contém ouro.
7 Essa vereda, a ave de rapina a ignora, e jamais a viram os olhos do falcão.
8 Nunca a pisaram feras majestosas, nem o leãozinho passou por ela.
9 Estende o homem a mão contra o rochedo e revolve os montes desde as suas raízes.
10 Abre canais nas pedras, e os seus olhos veem tudo o que há de mais precioso.
11 Tapa os veios de água, e nem uma gota sai deles, e traz à luz o que estava escondido.
12 Mas onde se achará a sabedoria? E onde está o lugar do entendimento?
13 O homem não conhece o valor dela, nem se acha ela na terra dos viventes.
14 O abismo diz: Ela não está em mim; e o mar diz: Não está comigo.
15 Não se dá por ela ouro fino, nem se pesa prata em câmbio dela.
16 O seu valor não se pode avaliar pelo ouro de Ofir, nem pelo precioso ônix, nem pela safira.
17 O ouro não se iguala a ela, nem o cristal; ela não se trocará por joia de ouro fino;
18 ela faz esquecer o coral e o cristal; a aquisição da sabedoria é melhor que a das pérolas.
19 Não se lhe igualará o topázio da Etiópia, nem se pode avaliar por ouro puro.
20 Donde, pois, vem a sabedoria, e onde está o lugar do entendimento?
21 Está encoberta aos olhos de todo vivente e oculta às aves do céu.
22 O abismo e a morte dizem: Ouvimos com os nossos ouvidos a sua fama.
23 Deus lhe entende o caminho, e ele é quem sabe o seu lugar.
24 Porque ele perscruta até as extremidades da terra, vê tudo o que há debaixo dos céus.
25 Quando regulou o peso do vento e fixou a medida das águas;
26 quando determinou leis para a chuva e caminho para o relâmpago dos trovões,
27 então, viu ele a sabedoria e a manifestou; estabeleceu-a e também a esquadrinhou.
28 E disse ao homem: Eis que o temor do Senhor é a sabedoria, e o apartar-se do mal é o entendimento.*
1 Prosseguiu Jó no seu discurso e disse:
2 Ah! Quem me dera ser como fui nos meses passados, como nos dias em que Deus me guardava!
3 Quando fazia resplandecer a sua lâmpada sobre a minha cabeça, quando eu, guiado por sua luz, caminhava pelas trevas;
4 como fui nos dias do meu vigor, quando a amizade de Deus estava sobre a minha tenda;
5 quando o Todo-Poderoso ainda estava comigo, e os meus filhos, em redor de mim;
6 quando eu lavava os pés em leite, e da rocha me corriam ribeiros de azeite.
7 Quando eu saía para a porta da cidade, e na praça me era dado sentar-me,
8 os moços me viam e se retiravam; os idosos se levantavam e se punham em pé;
9 os príncipes reprimiam as suas palavras e punham a mão sobre a boca;
10 a voz dos nobres emudecia, e a sua língua se apegava ao paladar.
11 Ouvindo-me algum ouvido, esse me chamava feliz; vendo-me algum olho, dava testemunho de mim;
12 porque eu livrava os pobres que clamavam e também o órfão que não tinha quem o socorresse.
13 A bênção do que estava a perecer vinha sobre mim, e eu fazia rejubilar-se o coração da viúva.
14 Eu me cobria de justiça, e esta me servia de veste; como manto e turbante era a minha equidade.
15 Eu me fazia de olhos para o cego e de pés para o coxo.
16 Dos necessitados era pai e até as causas dos desconhecidos eu examinava.
17 Eu quebrava os queixos do iníquo e dos seus dentes lhe fazia eu cair a vítima.
18 Eu dizia: no meu ninho expirarei, multiplicarei os meus dias como a areia.
19 A minha raiz se estenderá até às águas, e o orvalho ficará durante a noite sobre os meus ramos;
20 a minha honra se renovará em mim, e o meu arco se reforçará na minha mão.
21 Os que me ouviam esperavam o meu conselho e guardavam silêncio para ouvi-lo.
22 Havendo eu falado, não replicavam; as minhas palavras caíam sobre eles como orvalho.
23 Esperavam-me como à chuva, abriam a boca como à chuva de primavera.
24 Sorria-me para eles quando não tinham confiança; e a luz do meu rosto não desprezavam.
25 Eu lhes escolhia o caminho, assentava-me como chefe e habitava como rei entre as suas tropas, como quem consola os que pranteiam.*
1 Mas agora se riem de mim os de menos idade do que eu, e cujos pais eu teria desdenhado de pôr ao lado dos cães do meu rebanho.
2 De que também me serviria a força das suas mãos, homens cujo vigor já pereceu?
3 De míngua e fome se debilitaram; roem os lugares secos, desde muito em ruínas e desolados.
4 Apanham malvas e folhas dos arbustos e se sustentam de raízes de zimbro.
5 Do meio dos homens são expulsos; grita-se contra eles, como se grita atrás de um ladrão;
6 habitam nos desfiladeiros sombrios, nas cavernas da terra e das rochas.
7 Bramam entre os arbustos e se ajuntam debaixo dos espinheiros.
8 São filhos de doidos, raça infame, e da terra são escorraçados.
9 Mas agora sou a sua canção de motejo e lhes sirvo de provérbio.
10 Abominam-me, fogem para longe de mim e não se abstêm de me cuspir no rosto.
11 Porque Deus afrouxou a corda do meu arco e me oprimiu; pelo que sacudiram de si o freio perante o meu rosto.
12 À direita se levanta uma súcia, e me empurra, e contra mim prepara o seu caminho de destruição.
13 Arruínam a minha vereda, promovem a minha calamidade; gente para quem já não há socorro.
14 Vêm contra mim como por uma grande brecha e se revolvem avante entre as ruínas.
15 Sobrevieram-me pavores, como pelo vento é varrida a minha honra; como nuvem passou a minha felicidade.
16 Agora, dentro de mim se me derrama a alma; os dias da aflição se apoderaram de mim.
17 A noite me verruma os ossos e os desloca, e não descansa o mal que me rói.
18 Pela grande violência do meu mal está desfigurada a minha veste, mal que me cinge como a gola da minha túnica.
19 Deus, tu me lançaste na lama, e me tornei semelhante ao pó e à cinza.
20 Clamo a ti, e não me respondes; estou em pé, mas apenas olhas para mim.
21 Tu foste cruel comigo; com a força da tua mão tu me combates.
22 Levantas-me sobre o vento e me fazes cavalgá-lo; dissolves-me no estrondo da tempestade.
23 Pois eu sei que me levarás à morte e à casa destinada a todo vivente.
24 De um montão de ruínas não estenderá o homem a mão e na sua desventura não levantará um grito por socorro?
25 Acaso, não chorei sobre aquele que atravessava dias difíceis ou não se angustiou a minha alma pelo necessitado?
26 Aguardava eu o bem, e eis que me veio o mal; esperava a luz, veio-me a escuridão.
27 O meu íntimo se agita sem cessar; e dias de aflição me sobrevêm.
28 Ando de luto, sem a luz do sol; levanto-me na congregação e clamo por socorro.
29 Sou irmão dos chacais e companheiro de avestruzes.
30 Enegrecida se me cai a pele, e os meus ossos queimam em febre.
31 Por isso, a minha harpa se me tornou em prantos de luto, e a minha flauta, em voz dos que choram.*
1 Fiz aliança com meus olhos; como, pois, os fixaria eu numa donzela?
2 Que porção, pois, teria eu do Deus lá de cima e que herança, do Todo-Poderoso desde as alturas?
3 Acaso, não é a perdição para o iníquo, e o infortúnio, para os que praticam a maldade?
4 Ou não vê Deus os meus caminhos e não conta todos os meus passos?
5 Se andei com falsidade, e se o meu pé se apressou para o engano
6 (pese-me Deus em balanças fiéis e conhecerá a minha integridade);
7 se os meus passos se desviaram do caminho, e se o meu coração segue os meus olhos, e se às minhas mãos se apegou qualquer mancha,
8 então, semeie eu, e outro coma, e sejam arrancados os renovos do meu campo.
9 Se o meu coração se deixou seduzir por causa de mulher, se andei à espreita à porta do meu próximo,
10 então, moa minha mulher para outro, e outros se encurvem sobre ela.
11 Pois seria isso um crime hediondo, delito à punição de juízes;
12 pois seria fogo que consome até à destruição e desarraigaria toda a minha renda.
13 Se desprezei o direito do meu servo ou da minha serva, quando eles contendiam comigo,
14 então, que faria eu quando Deus se levantasse? E, inquirindo ele a causa, que lhe responderia eu?
15 Aquele que me formou no ventre materno não os fez também a eles? Ou não é o mesmo que nos formou na madre?
16 Se retive o que os pobres desejavam ou fiz desfalecer os olhos da viúva;
17 ou, se sozinho comi o meu bocado, e o órfão dele não participou
18 (Porque desde a minha mocidade cresceu comigo como se eu lhe fora o pai, e desde o ventre da minha mãe fui o guia da viúva.);
19 se a alguém vi perecer por falta de roupa e ao necessitado, por não ter coberta;
20 se os seus lombos não me abençoaram, se ele não se aquentava com a lã dos meus cordeiros;
21 se eu levantei a mão contra o órfão, por me ver apoiado pelos juízes da porta,
22 então, caia a omoplata do meu ombro, e seja arrancado o meu braço da articulação.
23 Porque o castigo de Deus seria para mim um assombro, e eu não poderia enfrentar a sua majestade.
24 Se no ouro pus a minha esperança ou disse ao ouro fino: em ti confio;
25 se me alegrei por serem grandes os meus bens e por ter a minha mão alcançado muito;
26 se olhei para o sol, quando resplandecia, ou para a lua, que caminhava esplendente,
27 e o meu coração se deixou enganar em oculto, e beijos lhes atirei com a mão,
28 também isto seria delito à punição de juízes; pois assim negaria eu ao Deus lá de cima.
29 Se me alegrei da desgraça do que me tem ódio e se exultei quando o mal o atingiu
30 (Também não deixei pecar a minha boca, pedindo com imprecações a sua morte.);
31 se a gente da minha tenda não disse: Ah! Quem haverá aí que não se saciou de carne provida por ele
32 (O estrangeiro não pernoitava na rua; as minhas portas abria ao viandante.)!
33 Se, como Adão, encobri as minhas transgressões, ocultando o meu delito no meu seio;
34 porque eu temia a grande multidão, e o desprezo das famílias me apavorava, de sorte que me calei e não saí da porta.
35 Tomara eu tivesse quem me ouvisse! Eis aqui a minha defesa assinada! Que o Todo-Poderoso me responda! Que o meu adversário escreva a sua acusação!
36 Por certo que a levaria sobre o meu ombro, atá-la-ia sobre mim como coroa;
37 mostrar-lhe-ia o número dos meus passos; como príncipe me chegaria a ele.
38 Se a minha terra clamar contra mim, e se os seus sulcos juntamente chorarem;
39 se comi os seus frutos sem tê-la pago devidamente e causei a morte aos seus donos,
40 por trigo me produza cardos, e por cevada, joio. Fim das palavras de Jó.*
1 Cessaram aqueles três homens de responder a Jó no tocante ao se ter ele por justo aos seus próprios olhos.
2 Então, se acendeu a ira de Eliú, filho de Baraquel, o buzita, da família de Rão; acendeu-se a sua ira contra Jó, porque este pretendia ser mais justo do que Deus.
3 Também a sua ira se acendeu contra os três amigos, porque, mesmo não achando eles o que responder, condenavam a Jó.
4 Eliú, porém, esperara para falar a Jó, pois eram de mais idade do que ele.
5 Vendo Eliú que já não havia resposta na boca daqueles três homens, a sua ira se acendeu.
6 Disse Eliú, filho de Baraquel, o buzita: Eu sou de menos idade, e vós sois idosos; arreceei-me e temi de vos declarar a minha opinião.
7 Dizia eu: Falem os dias, e a multidão dos anos ensine a sabedoria.
8 Na verdade, há um espírito no homem, e o sopro do Todo-Poderoso o faz sábio.
9 Os de mais idade não é que são os sábios, nem os velhos, os que entendem o que é reto.
10 Pelo que digo: dai-me ouvidos, e também eu declararei a minha opinião.
11 Eis que aguardei as vossas palavras e dei ouvidos às vossas considerações, enquanto, quem sabe, buscáveis o que dizer.
12 Atentando, pois, para vós outros, eis que nenhum de vós houve que refutasse a Jó, nem que respondesse às suas razões.
13 Não vos desculpeis, pois, dizendo: Achamos sabedoria nele; Deus pode vencê-lo, e não o homem.
14 Ora, ele não me dirigiu palavra alguma, nem eu lhe retorquirei com as vossas palavras.
15 Jó, os três estão pasmados, já não respondem, faltam-lhes as palavras.
16 Acaso, devo esperar, pois não falam, estão parados e nada mais respondem?
17 Também eu concorrerei com a minha resposta; declararei a minha opinião.
18 Porque tenho muito que falar, e o meu espírito me constrange.
19 Eis que dentro de mim sou como o vinho, sem respiradouro, como odres novos, prestes a arrebentar-se.
20 Permiti, pois, que eu fale para desafogar-me; abrirei os lábios e responderei.
21 Não farei acepção de pessoas, nem usarei de lisonjas com o homem.
22 Porque não sei lisonjear; em caso contrário, em breve me levaria o meu Criador.*
1 Ouve, pois, Jó, as minhas razões e dá ouvidos a todas as minhas palavras.
2 Passo agora a falar, em minha boca fala a língua.
3 As minhas razões provam a sinceridade do meu coração, e os meus lábios proferem o puro saber.
4 O Espírito de Deus me fez, e o sopro do Todo-Poderoso me dá vida.
5 Se podes, contesta-me, dispõe bem as tuas razões perante mim e apresenta-te.
6 Eis que diante de Deus sou como tu és; também eu sou formado do barro.
7 Por isso, não te inspiro terror, nem será pesada sobre ti a minha mão.
8 Na verdade, falaste perante mim, e eu ouvi o som das tuas palavras:
9 Estou limpo, sem transgressão; puro sou e não tenho iniquidade.
10 Eis que Deus procura pretextos contra mim e me considera como seu inimigo.
11 Põe no tronco os meus pés e observa todas as minhas veredas.
12 Nisto não tens razão, eu te respondo; porque Deus é maior do que o homem.
13 Por que contendes com ele, afirmando que não te dá contas de nenhum dos seus atos?
14 Pelo contrário, Deus fala de um modo, sim, de dois modos, mas o homem não atenta para isso.
15 Em sonho ou em visão de noite, quando cai sono profundo sobre os homens, quando adormecem na cama,
16 então, lhes abre os ouvidos e lhes sela a sua instrução,
17 para apartar o homem do seu desígnio e livrá-lo da soberba;
18 para guardar a sua alma da cova e a sua vida de passar pela espada.
19 Também no seu leito é castigado com dores, com incessante contenda nos seus ossos;
20 de modo que a sua vida abomina o pão, e a sua alma, a comida apetecível.
21 A sua carne, que se via, agora desaparece, e os seus ossos, que não se viam, agora se descobrem.
22 A sua alma se vai chegando à cova, e a sua vida, aos portadores da morte.
23 Se com ele houver um anjo intercessor, um dos milhares, para declarar ao homem o que lhe convém,
24 então, Deus terá misericórdia dele e dirá ao anjo: Redime-o, para que não desça à cova; achei resgate.
25 Sua carne se robustecerá com o vigor da sua infância, e ele tornará aos dias da sua juventude.
26 Deveras orará a Deus, que lhe será propício; ele, com júbilo, verá a face de Deus, e este lhe restituirá a sua justiça.
27 Cantará diante dos homens e dirá: Pequei, perverti o direito e não fui punido segundo merecia.
28 Deus redimiu a minha alma de ir para a cova; e a minha vida verá a luz.
29 Eis que tudo isto é obra de Deus, duas e três vezes para com o homem,
30 para reconduzir da cova a sua alma e o alumiar com a luz dos viventes.
31 Escuta, pois, ó Jó, ouve-me; cala-te, e eu falarei.
32 Se tens alguma coisa que dizer, responde-me; fala, porque desejo justificar-te.
33 Se não, escuta-me; cala-te, e ensinar-te-ei a sabedoria.*
1 Disse mais Eliú:
2 Ouvi, ó sábios, as minhas razões; vós, instruídos, inclinai os ouvidos para mim.
3 Porque o ouvido prova as palavras, como o paladar, a comida.
4 O que é direito escolhamos para nós; conheçamos entre nós o que é bom.
5 Porque Jó disse: Sou justo, e Deus tirou o meu direito.
6 Apesar do meu direito, sou tido por mentiroso; a minha ferida é incurável, sem que haja pecado em mim.
7 Que homem há como Jó, que bebe a zombaria como água?
8 E anda em companhia dos que praticam a iniquidade e caminha com homens perversos?
9 Pois disse: De nada aproveita ao homem o comprazer-se em Deus.
10 Pelo que vós, homens sensatos, escutai-me: longe de Deus o praticar ele a perversidade, e do Todo-Poderoso o cometer injustiça.
11 Pois retribui ao homem segundo as suas obras e faz que a cada um toque segundo o seu caminho.
12 Na verdade, Deus não procede maliciosamente; nem o Todo-Poderoso perverte o juízo.
13 Quem lhe entregou o governo da terra? Quem lhe confiou o universo?
14 Se Deus pensasse apenas em si mesmo e para si recolhesse o seu espírito e o seu sopro,
15 toda a carne juntamente expiraria, e o homem voltaria para o pó.
16 Se, pois, há em ti entendimento, ouve isto; inclina os ouvidos ao som das minhas palavras.
17 Acaso, governaria o que aborrecesse o direito? E quererás tu condenar aquele que é justo e poderoso?
18 Dir-se-á a um rei: Oh! Vil? Ou aos príncipes: Oh! Perversos?
19 Quanto menos àquele que não faz acepção das pessoas de príncipes, nem estima ao rico mais do que ao pobre; porque todos são obra de suas mãos.
20 De repente, morrem; à meia-noite, os povos são perturbados e passam, e os poderosos são tomados por força invisível.
21 Os olhos de Deus estão sobre os caminhos do homem e veem todos os seus passos.
22 Não há trevas nem sombra assaz profunda, onde se escondam os que praticam a iniquidade.
23 Pois Deus não precisa observar por muito tempo o homem antes de o fazer ir a juízo perante ele.
24 Quebranta os fortes, sem os inquirir, e põe outros em seu lugar.
25 Ele conhece, pois, as suas obras; de noite, os transtorna, e ficam moídos.
26 Ele os fere como a perversos, à vista de todos;
27 porque dele se desviaram, e não quiseram compreender nenhum de seus caminhos,
28 e, assim, fizeram que o clamor do pobre subisse até Deus, e este ouviu o lamento dos aflitos.
29 Se ele aquietar-se, quem o condenará? Se encobrir o rosto, quem o poderá contemplar, seja um povo, seja um homem?
30 Para que o ímpio não reine, e não haja quem iluda o povo.
31 Se alguém diz a Deus: Sofri, não pecarei mais;
32 o que não vejo, ensina-mo tu; se cometi injustiça, jamais a tornarei a praticar,
33 acaso, deve ele recompensar-te segundo tu queres ou não queres? Acaso, deve ele dizer-te: Escolhe tu, e não eu; declara o que sabes, fala?
34 Os homens sensatos dir-me-ão, dir-me-á o sábio que me ouve:
35 Jó falou sem conhecimento, e nas suas palavras não há sabedoria.
36 Tomara fosse Jó provado até ao fim, porque ele respondeu como homem de iniquidade.
37 Pois ao seu pecado acrescenta rebelião, entre nós, com desprezo, bate ele palmas e multiplica as suas palavras contra Deus.*
1 Disse mais Eliú:
2 Achas que é justo dizeres: Maior é a minha justiça do que a de Deus?
3 Porque dizes: De que me serviria ela? Que proveito tiraria dela mais do que do meu pecado?
4 Dar-te-ei resposta, a ti e aos teus amigos contigo.
5 Atenta para os céus e vê; contempla as altas nuvens acima de ti.
6 Se pecas, que mal lhe causas tu? Se as tuas transgressões se multiplicam, que lhe fazes?
7 Se és justo, que lhe dás ou que recebe ele da tua mão?
8 A tua impiedade só pode fazer o mal ao homem como tu mesmo; e a tua justiça, dar proveito ao filho do homem.
9 Por causa das muitas opressões, os homens clamam, clamam por socorro contra o braço dos poderosos.
10 Mas ninguém diz: Onde está Deus, que me fez, que inspira canções de louvor durante a noite,
11 que nos ensina mais do que aos animais da terra e nos faz mais sábios do que as aves dos céus?
12 Clamam, porém ele não responde, por causa da arrogância dos maus.
13 Só gritos vazios Deus não ouvirá, nem atentará para eles o Todo-Poderoso.
14 Jó, ainda que dizes que não o vês, a tua causa está diante dele; por isso, espera nele.
15 Mas agora, porque Deus na sua ira não está punindo, nem fazendo muito caso das transgressões,
16 abres a tua boca, com palavras vãs, amontoando frases de ignorante.*
1 Prosseguiu Eliú e disse:
2 Mais um pouco de paciência, e te mostrarei que ainda tenho argumentos a favor de Deus.
3 De longe trarei o meu conhecimento e ao meu Criador atribuirei a justiça.
4 Porque, na verdade, as minhas palavras não são falsas; contigo está quem é senhor do assunto.
5 Eis que Deus é mui grande; contudo a ninguém despreza; é grande na força da sua compreensão.
6 Não poupa a vida ao perverso, mas faz justiça aos aflitos.
7 Dos justos não tira os olhos; antes, com os reis, no trono os assenta para sempre, e são exaltados.
8 Se estão presos em grilhões e amarrados com cordas de aflição,
9 ele lhes faz ver as suas obras, as suas transgressões, e que se houveram com soberba.
10 Abre-lhes também os ouvidos para a instrução e manda-lhes que se convertam da iniquidade.
11 Se o ouvirem e o servirem, acabarão seus dias em felicidade e os seus anos em delícias.
12 Porém, se não o ouvirem, serão traspassados pela lança e morrerão na sua cegueira.
13 Os ímpios de coração amontoam para si a ira; e, agrilhoados por Deus, não clamam por socorro.
14 Perdem a vida na sua mocidade e morrem entre os prostitutos cultuais.
15 Ao aflito livra por meio da sua aflição e pela opressão lhe abre os ouvidos.
16 Assim também procura tirar-te das fauces da angústia para um lugar espaçoso, em que não há aperto, e as iguarias da tua mesa seriam cheias de gordura;
17 mas tu te enches do juízo do perverso, e, por isso, o juízo e a justiça te alcançarão.
18 Guarda-te, pois, de que a ira não te induza a escarnecer, nem te desvie a grande quantia do resgate.
19 Estimaria ele as tuas lamúrias e todos os teus grandes esforços, para que te vejas livre da tua angústia?
20 Não suspires pela noite, em que povos serão tomados do seu lugar.
21 Guarda-te, não te inclines para a iniquidade; pois isso preferes à tua miséria.
22 Eis que Deus se mostra grande em seu poder! Quem é mestre como ele?
23 Quem lhe prescreveu o seu caminho ou quem lhe pode dizer: Praticaste a injustiça?
24 Lembra-te de lhe magnificares as obras que os homens celebram.
25 Todos os homens as contemplam; de longe as admira o homem.
26 Eis que Deus é grande, e não o podemos compreender; o número dos seus anos não se pode calcular.
27 Porque atrai para si as gotas de água que de seu vapor destilam em chuva,
28 a qual as nuvens derramam e gotejam sobre o homem abundantemente.
29 Acaso, pode alguém entender o estender-se das nuvens e os trovões do seu pavilhão?
30 Eis que estende sobre elas o seu relâmpago e encobre as profundezas do mar.
31 Pois por estas coisas julga os povos e lhes dá mantimento em abundância.
32 Enche as mãos de relâmpagos e os dardeja contra o adversário.
33 O fragor da tempestade dá notícias a respeito dele, dele que é zeloso na sua ira contra a injustiça.*
1 Sobre isto treme também o meu coração e salta do seu lugar.
2 Dai ouvidos ao trovão de Deus, estrondo que sai da sua boca;
3 ele o solta por debaixo de todos os céus, e o seu relâmpago, até aos confins da terra.
4 Depois deste, ruge a sua voz, troveja com o estrondo da sua majestade, e já ele não retém o relâmpago quando lhe ouvem a voz.
5 Com a sua voz troveja Deus maravilhosamente; faz grandes coisas, que nós não compreendemos.
6 Porque ele diz à neve: Cai sobre a terra; e à chuva e ao aguaceiro: Sede fortes.
7 Assim, torna ele inativas as mãos de todos os homens, para que reconheçam as obras dele.
8 E as alimárias entram nos seus esconderijos e ficam nas suas cavernas.
9 De suas recâmaras sai o pé de vento, e, dos ventos do norte, o frio.
10 Pelo sopro de Deus se dá a geada, e as largas águas se congelam.
11 Também de umidade carrega as densas nuvens, nuvens que espargem os relâmpagos.
12 Então, elas, segundo o rumo que ele dá, se espalham para uma e outra direção, para fazerem tudo o que lhes ordena sobre a redondeza da terra.
13 E tudo isso faz ele vir para disciplina, se convém à terra, ou para exercer a sua misericórdia.
14 Inclina, Jó, os ouvidos a isto, para e considera as maravilhas de Deus.
15 Porventura, sabes tu como Deus as opera e como faz resplandecer o relâmpago da sua nuvem?
16 Tens tu notícia do equilíbrio das nuvens e das maravilhas daquele que é perfeito em conhecimento?
17 Que faz aquecer as tuas vestes, quando há calma sobre a terra por causa do vento sul?
18 Ou estendeste com ele o firmamento, que é sólido como espelho fundido?
19 Ensina-nos o que lhe diremos; porque nós, envoltos em trevas, nada lhe podemos expor.
20 Contar-lhe-ia alguém o que tenho dito? Seria isso desejar o homem ser devorado.
21 Eis que o homem não pode olhar para o sol, que brilha no céu, uma vez passado o vento que o deixa limpo.
22 Do norte vem o áureo esplendor, pois Deus está cercado de tremenda majestade.
23 Ao Todo-Poderoso, não o podemos alcançar; ele é grande em poder, porém não perverte o juízo e a plenitude da justiça.
24 Por isso, os homens o temem; ele não olha para os que se julgam sábios.*
1 Depois disto, o Senhor, do meio de um redemoinho, respondeu a Jó:
2 Quem é este que escurece os meus desígnios com palavras sem conhecimento?
3 Cinge, pois, os lombos como homem, pois eu te perguntarei, e tu me farás saber.
4 Onde estavas tu, quando eu lançava os fundamentos da terra? Dize-mo, se tens entendimento.
5 Quem lhe pôs as medidas, se é que o sabes? Ou quem estendeu sobre ela o cordel?
6 Sobre que estão fundadas as suas bases ou quem lhe assentou a pedra angular,
7 quando as estrelas da alva, juntas, alegremente cantavam, e rejubilavam todos os filhos de Deus?
8 Ou quem encerrou o mar com portas, quando irrompeu da madre;
9 quando eu lhe pus as nuvens por vestidura e a escuridão por fraldas?
10 Quando eu lhe tracei limites, e lhe pus ferrolhos e portas,
11 e disse: até aqui virás e não mais adiante, e aqui se quebrará o orgulho das tuas ondas?
12 Acaso, desde que começaram os teus dias, deste ordem à madrugada ou fizeste a alva saber o seu lugar,
13 para que se apegasse às orlas da terra, e desta fossem os perversos sacudidos?
14 A terra se modela como o barro debaixo do selo, e tudo se apresenta como vestidos;
15 dos perversos se desvia a sua luz, e o braço levantado para ferir se quebranta.
16 Acaso, entraste nos mananciais do mar ou percorreste o mais profundo do abismo?
17 Porventura, te foram reveladas as portas da morte ou viste essas portas da região tenebrosa?
18 Tens ideia nítida da largura da terra? Dize-mo, se o sabes.
19 Onde está o caminho para a morada da luz? E, quanto às trevas, onde é o seu lugar,
20 para que as conduzas aos seus limites e discirnas as veredas para a sua casa?
21 Tu o sabes, porque nesse tempo eras nascido e porque é grande o número dos teus dias!
22 Acaso, entraste nos depósitos da neve e viste os tesouros da saraiva,
23 que eu retenho até ao tempo da angústia, até ao dia da peleja e da guerra?
24 Onde está o caminho para onde se difunde a luz e se espalha o vento oriental sobre a terra?
25 Quem abriu regos para o aguaceiro ou caminho para os relâmpagos dos trovões;
26 para que se faça chover sobre a terra, onde não há ninguém, e no ermo, em que não há gente;
27 para dessedentar a terra deserta e assolada e para fazer crescer os renovos da erva?
28 Acaso, a chuva tem pai? Ou quem gera as gotas do orvalho?
29 De que ventre procede o gelo? E quem dá à luz a geada do céu?
30 As águas ficam duras como a pedra, e a superfície das profundezas se torna compacta.
31 Ou poderás tu atar as cadeias do Sete-estrelo ou soltar os laços do Órion?
32 Ou fazer aparecer os signos do Zodíaco ou guiar a Ursa com seus filhos?
33 Sabes tu as ordenanças dos céus, podes estabelecer a sua influência sobre a terra?
34 Podes levantar a tua voz até às nuvens, para que a abundância das águas te cubra?
35 Ou ordenarás aos relâmpagos que saiam e te digam: Eis-nos aqui?
36 Quem pôs sabedoria nas camadas de nuvens? Ou quem deu entendimento ao meteoro?
37 Quem pode numerar com sabedoria as nuvens? Ou os odres dos céus, quem os pode despejar,
38 para que o pó se transforme em massa sólida, e os torrões se apeguem uns aos outros?
39 Caçarás, porventura, a presa para a leoa? Ou saciarás a fome dos leõezinhos,
40 quando se agacham nos covis e estão à espreita nas covas?
41 Quem prepara aos corvos o seu alimento, quando os seus pintainhos gritam a Deus e andam vagueando, por não terem que comer?*
1 Sabes tu o tempo em que as cabras monteses têm os filhos ou cuidaste das corças quando dão suas crias?
2 Podes contar os meses que cumprem? Ou sabes o tempo do seu parto?
3 Elas encurvam-se, para terem seus filhos, e lançam de si as suas dores.
4 Seus filhos se tornam robustos, crescem no campo aberto, saem e nunca mais tornam para elas.
5 Quem despediu livre o jumento selvagem, e quem soltou as prisões ao asno veloz,
6 ao qual dei o ermo por casa e a terra salgada por moradas?
7 Ri-se do tumulto da cidade, não ouve os muitos gritos do arrieiro.
8 Os montes são o lugar do seu pasto, e anda à procura de tudo o que está verde.
9 Acaso, quer o boi selvagem servir-te? Ou passará ele a noite junto da tua manjedoura?
10 Porventura, podes prendê-lo ao sulco com cordas? Ou gradará ele os vales após ti?
11 Confiarás nele, por ser grande a sua força, ou deixarás a seu cuidado o teu trabalho?
12 Fiarás dele que te traga para a casa o que semeaste e o recolha na tua eira?
13 O avestruz bate alegre as asas; acaso, porém, tem asas e penas de bondade?
14 Ele deixa os seus ovos na terra, e os aquenta no pó,
15 e se esquece de que algum pé os pode esmagar ou de que podem pisá-los os animais do campo.
16 Trata com dureza os seus filhos, como se não fossem seus; embora seja em vão o seu trabalho, ele está tranquilo,
17 porque Deus lhe negou sabedoria e não lhe deu entendimento;
18 mas, quando de um salto se levanta para correr, ri-se do cavalo e do cavaleiro.
19 Ou dás tu força ao cavalo ou revestirás o seu pescoço de crinas?
20 Acaso, o fazes pular como ao gafanhoto? Terrível é o fogoso respirar das suas ventas.
21 Escarva no vale, folga na sua força e sai ao encontro dos armados.
22 Ri-se do temor e não se espanta; e não torna atrás por causa da espada.
23 Sobre ele chocalha a aljava, flameja a lança e o dardo.
24 De fúria e ira devora o caminho e não se contém ao som da trombeta.
25 Em cada sonido da trombeta, ele diz: Avante! Cheira de longe a batalha, o trovão dos príncipes e o alarido.
26 Ou é pela tua inteligência que voa o falcão, estendendo as asas para o Sul?
27 Ou é pelo teu mandado que se remonta a águia e faz alto o seu ninho?
28 Habita no penhasco onde faz a sua morada, sobre o cimo do penhasco, em lugar seguro.
29 Dali, descobre a presa; seus olhos a avistam de longe.
30 Seus filhos chupam sangue; onde há mortos, ela aí está.*
1 Disse mais o Senhor a Jó:
2 Acaso, quem usa de censuras contenderá com o Todo-Poderoso? Quem assim argui a Deus que responda.
3 Então, Jó respondeu ao Senhor e disse:
4 Sou indigno; que te responderia eu? Ponho a mão na minha boca.
5 Uma vez falei e não replicarei, aliás, duas vezes, porém não prosseguirei.
6 Então, o Senhor, do meio de um redemoinho, respondeu a Jó:
7 Cinge agora os lombos como homem; eu te perguntarei, e tu me responderás.
8 Acaso, anularás tu, de fato, o meu juízo? Ou me condenarás, para te justificares?
9 Ou tens braço como Deus ou podes trovejar com a voz como ele o faz?
10 Orna-te, pois, de excelência e grandeza, veste-te de majestade e de glória.
11 Derrama as torrentes da tua ira e atenta para todo soberbo e abate-o.
12 Olha para todo soberbo e humilha-o, calca aos pés os perversos no seu lugar.
13 Cobre-os juntamente no pó, encerra-lhes o rosto no sepulcro.
14 Então, também eu confessarei a teu respeito que a tua mão direita te dá vitória.
15 Contempla agora o hipopótamo, que eu criei contigo, que come a erva como o boi.
16 Sua força está nos seus lombos, e o seu poder, nos músculos do seu ventre.
17 Endurece a sua cauda como cedro; os tendões das suas coxas estão entretecidos.
18 Os seus ossos são como tubos de bronze, o seu arcabouço, como barras de ferro.
19 Ele é obra-prima dos feitos de Deus; quem o fez o proveu de espada.
20 Em verdade, os montes lhe produzem pasto, onde todos os animais do campo folgam.
21 Deita-se debaixo dos lotos, no esconderijo dos canaviais e da lama.
22 Os lotos o cobrem com sua sombra; os salgueiros do ribeiro o cercam.
23 Se um rio transborda, ele não se apressa; fica tranquilo ainda que o Jordão se levante até à sua boca.
24 Acaso, pode alguém apanhá-lo quando ele está olhando? Ou lhe meter um laço pelo nariz?*
1 Podes tu, com anzol, apanhar o crocodilo ou lhe travar a língua com uma corda?
2 Podes meter-lhe no nariz uma vara de junco? Ou furar-lhe as bochechas com um gancho?
3 Acaso, te fará muitas súplicas? Ou te falará palavras brandas?
4 Fará ele acordo contigo? Ou tomá-lo-ás por servo para sempre?
5 Brincarás com ele, como se fora um passarinho? Ou tê-lo-ás preso à correia para as tuas meninas?
6 Acaso, os teus sócios negociam com ele? Ou o repartirão entre os mercadores?
7 Encher-lhe-ás a pele de arpões? Ou a cabeça, de farpas?
8 Põe a mão sobre ele, lembra-te da peleja e nunca mais o intentarás.
9 Eis que a gente se engana em sua esperança; acaso, não será o homem derribado só em vê-lo?
10 Ninguém há tão ousado, que se atreva a despertá-lo. Quem é, pois, aquele que pode erguer-se diante de mim?
11 Quem primeiro me deu a mim, para que eu haja de retribuir-lhe? Pois o que está debaixo de todos os céus é meu.
12 Não me calarei a respeito dos seus membros, nem da sua grande força, nem da graça da sua compostura.
13 Quem lhe abrirá as vestes do seu dorso? Ou lhe penetrará a couraça dobrada?
14 Quem abriria as portas do seu rosto? Pois em roda dos seus dentes está o terror.
15 As fileiras de suas escamas são o seu orgulho, cada uma bem-encostada como por um selo que as ajusta.
16 A tal ponto uma se chega à outra, que entre elas não entra nem o ar.
17 Umas às outras se ligam, aderem entre si e não se podem separar.
18 Cada um dos seus espirros faz resplandecer luz, e os seus olhos são como as pestanas da alva.
19 Da sua boca saem tochas; faíscas de fogo saltam dela.
20 Das suas narinas procede fumaça, como de uma panela fervente ou de juncos que ardem.
21 O seu hálito faz incender os carvões; e da sua boca sai chama.
22 No seu pescoço reside a força; e diante dele salta o desespero.
23 Suas partes carnudas são bem-pegadas entre si; todas fundidas nele e imóveis.
24 O seu coração é firme como uma pedra, firme como a mó de baixo.
25 Levantando-se ele, tremem os valentes; quando irrompe, ficam como que fora de si.
26 Se o golpe de espada o alcança, de nada vale, nem de lança, de dardo ou de flecha.
27 Para ele, o ferro é palha, e o cobre, pau podre.
28 A seta o não faz fugir; as pedras das fundas se lhe tornam em restolho.
29 Os porretes atirados são para ele como palha, e ri-se do brandir da lança.
30 Debaixo do ventre, há escamas pontiagudas; arrasta-se sobre a lama, como um instrumento de debulhar.
31 As profundezas faz ferver, como uma panela; torna o mar como caldeira de unguento.
32 Após si, deixa um sulco luminoso; o abismo parece ter-se encanecido.
33 Na terra, não tem ele igual, pois foi feito para nunca ter medo.
34 Ele olha com desprezo tudo o que é alto; é rei sobre todos os animais orgulhosos.*
1 Então, respondeu Jó ao Senhor:
2 Bem sei que tudo podes, e nenhum dos teus planos pode ser frustrado.
3 Quem é aquele, como disseste, que sem conhecimento encobre o conselho? Na verdade, falei do que não entendia; coisas maravilhosas demais para mim, coisas que eu não conhecia.
4 Escuta-me, pois, havias dito, e eu falarei; eu te perguntarei, e tu me ensinarás.
5 Eu te conhecia só de ouvir, mas agora os meus olhos te veem.
6 Por isso, me abomino e me arrependo no pó e na cinza.
7 Tendo o Senhor falado estas palavras a Jó, o Senhor disse também a Elifaz, o temanita: A minha ira se acendeu contra ti e contra os teus dois amigos; porque não dissestes de mim o que era reto, como o meu servo Jó.
8 Tomai, pois, sete novilhos e sete carneiros, e ide ao meu servo Jó, e oferecei holocaustos por vós. O meu servo Jó orará por vós; porque dele aceitarei a intercessão, para que eu não vos trate segundo a vossa loucura; porque vós não dissestes de mim o que era reto, como o meu servo Jó.
9 Então, foram Elifaz, o temanita, e Bildade, o suíta, e Zofar, o naamatita, e fizeram como o Senhor lhes ordenara; e o Senhor aceitou a oração de Jó.
Deus restaura a prosperidade de Jó
10 Mudou o Senhor a sorte de Jó, quando este orava pelos seus amigos; e o Senhor deu-lhe o dobro de tudo o que antes possuíra.
11 Então, vieram a ele todos os seus irmãos, e todas as suas irmãs, e todos quantos dantes o conheceram, e comeram com ele em sua casa, e se condoeram dele, e o consolaram de todo o mal que o Senhor lhe havia enviado; cada um lhe deu dinheiro e um anel de ouro.
12 Assim, abençoou o Senhor o último estado de Jó mais do que o primeiro; porque veio a ter catorze mil ovelhas, seis mil camelos, mil juntas de bois e mil jumentas.
13 Também teve outros sete filhos e três filhas.
14 Chamou o nome da primeira Jemima, o da outra, Quezia, e o da terceira, Quéren-Hapuque.
15 Em toda aquela terra não se acharam mulheres tão formosas como as filhas de Jó; e seu pai lhes deu herança entre seus irmãos.
16 Depois disto, viveu Jó cento e quarenta anos; e viu a seus filhos e aos filhos de seus filhos, até à quarta geração.
17 Então, morreu Jó, velho e farto de dias.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Jó','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)