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
1 São estas as palavras que Moisés falou a todo o Israel, dalém do Jordão, no deserto, na Arabá, defronte do mar de Sufe, entre Parã, Tofel, Labã, Hazerote e Di-Zaabe.
2 Jornada de onze dias há desde Horebe, pelo caminho da montanha de Seir, até Cades-Barneia.
3 Sucedeu que, no ano quadragésimo, no primeiro dia do undécimo mês, falou Moisés aos filhos de Israel, segundo tudo o que o Senhor lhe mandara a respeito deles,
4 depois que feriu a Seom, rei dos amorreus, que habitava em Hesbom, e a Ogue, rei de Basã, que habitava em Astarote, em Edrei.
5 Além do Jordão, na terra de Moabe, encarregou-se Moisés de explicar esta lei, dizendo:
6 O Senhor, nosso Deus, nos falou em Horebe, dizendo: Tempo bastante haveis estado neste monte.
7 Voltai-vos e parti; ide à região montanhosa dos amorreus, e a todos os seus vizinhos, na Arabá, e à região montanhosa, e à baixada, e ao Neguebe, e à costa marítima, terra dos cananeus, e ao Líbano, até ao grande rio Eufrates.
8 Eis aqui a terra que eu pus diante de vós; entrai e possuí a terra que o Senhor, com juramento, deu a vossos pais, Abraão, Isaque e Jacó, a eles e à sua descendência depois deles.
9 Nesse mesmo tempo, eu vos disse: eu sozinho não poderei levar-vos.
10 O Senhor, vosso Deus, vos tem multiplicado; e eis que, já hoje, sois multidão como as estrelas dos céus.
11 O Senhor, Deus de vossos pais, vos faça mil vezes mais numerosos do que sois e vos abençoe, como vos prometeu.
12 Como suportaria eu sozinho o vosso peso, a vossa carga e a vossa contenda?
13 Tomai-vos homens sábios, inteligentes e experimentados, segundo as vossas tribos, para que os ponha por vossos cabeças.
14 Então, me respondestes e dissestes: É bom cumprir a palavra que tens falado.
15 Tomei, pois, os cabeças de vossas tribos, homens sábios e experimentados, e os fiz cabeças sobre vós, chefes de milhares, chefes de cem, chefes de cinquenta, chefes de dez e oficiais, segundo as vossas tribos.
16 Nesse mesmo tempo, ordenei a vossos juízes, dizendo: ouvi a causa entre vossos irmãos e julgai justamente entre o homem e seu irmão ou o estrangeiro que está com ele.
17 Não sereis parciais no juízo, ouvireis tanto o pequeno como o grande; não temereis a face de ninguém, porque o juízo é de Deus; porém a causa que vos for demasiadamente difícil fareis vir a mim, e eu a ouvirei.
18 Assim, naquele tempo, vos ordenei todas as coisas que havíeis de fazer.
19 Então, partimos de Horebe e caminhamos por todo aquele grande e terrível deserto que vistes, pelo caminho da região montanhosa dos amorreus, como o Senhor, nosso Deus, nos ordenara; e chegamos a Cades-Barneia.
20 Então, eu vos disse: tendes chegado à região montanhosa dos amorreus, que o Senhor, nosso Deus, nos dá.
21 Eis que o Senhor, teu Deus, te colocou esta terra diante de ti. Sobe, possui-a, como te falou o Senhor, Deus de teus pais: Não temas e não te assustes.
22 Então, todos vós vos chegastes a mim e dissestes: Mandemos homens adiante de nós, para que nos espiem a terra e nos digam por que caminho devemos subir e a que cidades devemos ir.
23 Isto me pareceu bem; de maneira que tomei, dentre vós, doze homens, de cada tribo um homem.
24 E foram-se, e subiram à região montanhosa, e, espiando a terra, vieram até o vale de Escol,
25 e tomaram do fruto da terra nas mãos, e no-lo trouxeram, e nos informaram, dizendo: É terra boa que nos dá o Senhor, nosso Deus.
26 Porém vós não quisestes subir, mas fostes rebeldes à ordem do Senhor, vosso Deus.
27 Murmurastes nas vossas tendas e dissestes: Tem o Senhor contra nós ódio; por isso, nos tirou da terra do Egito para nos entregar nas mãos dos amorreus e destruir-nos.
28 Para onde subiremos? Nossos irmãos fizeram com que se derretesse o nosso coração, dizendo: Maior e mais alto do que nós é este povo; as cidades são grandes e fortificadas até aos céus. Também vimos ali os filhos dos anaquins.
29 Então, eu vos disse: não vos espanteis, nem os temais.
30 O Senhor, vosso Deus, que vai adiante de vós, ele pelejará por vós, segundo tudo o que fez conosco, diante de vossos olhos, no Egito,
31 como também no deserto, onde vistes que o Senhor, vosso Deus, nele vos levou, como um homem leva a seu filho, por todo o caminho pelo qual andastes, até chegardes a este lugar.
32 Mas nem por isso crestes no Senhor, vosso Deus,
33 que foi adiante de vós por todo o caminho, para vos procurar o lugar onde deveríeis acampar; de noite, no fogo, para vos mostrar o caminho por onde havíeis de andar, e, de dia, na nuvem.
34 Tendo, pois, ouvido o Senhor as vossas palavras, indignou-se e jurou, dizendo:
35 Certamente, nenhum dos homens desta maligna geração verá a boa terra que jurei dar a vossos pais,
36 salvo Calebe, filho de Jefoné; ele a verá, e a terra que pisou darei a ele e a seus filhos, porquanto perseverou em seguir ao Senhor.
37 Também contra mim se indignou o Senhor por causa de vós, dizendo: Também tu lá não entrarás.
38 Josué, filho de Num, que está diante de ti, ele ali entrará; anima-o, porque ele fará que Israel a receba por herança.
39 E vossos meninos, de quem dissestes: Por presa serão; e vossos filhos, que, hoje, nem sabem distinguir entre bem e mal, esses ali entrarão, e a eles darei a terra, e eles a possuirão.
40 Porém vós virai-vos e parti para o deserto, pelo caminho do mar Vermelho.
41 Então, respondestes e me dissestes: Pecamos contra o Senhor; nós subiremos e pelejaremos, segundo tudo o que nos ordenou o Senhor, nosso Deus. Vós vos armastes, cada um dos seus instrumentos de guerra, e vos mostrastes temerários em subindo à região montanhosa.
42 Disse-me o Senhor: Dize-lhes: Não subais, nem pelejeis, pois não estou no meio de vós, para que não sejais derrotados diante dos vossos inimigos.
43 Assim vos falei, e não escutastes; antes, fostes rebeldes às ordens do Senhor e, presunçosos, subistes às montanhas.
44 Os amorreus que habitavam naquela região montanhosa vos saíram ao encontro; e vos perseguiram como fazem as abelhas e vos derrotaram desde Seir até Horma.
45 Tornastes-vos, pois, e chorastes perante o Senhor, porém o Senhor não vos ouviu, não inclinou os ouvidos a vós outros.
46 Assim, permanecestes muitos dias em Cades.*
1 Depois, viramo-nos, e seguimos para o deserto, caminho do mar Vermelho como o Senhor me dissera, e muitos dias rodeamos a montanha de Seir.
2 Então, o Senhor me falou, dizendo:
3 Tendes já rodeado bastante esta montanha; virai-vos para o norte.
4 Ordena ao povo, dizendo: Passareis pelos limites de vossos irmãos, os filhos de Esaú, que habitam em Seir; e eles terão medo de vós; portanto, guardai-vos bem.
5 Não vos entremetais com eles, porque vos não darei da sua terra nem ainda a pisada da planta de um pé; pois a Esaú dei por possessão a montanha de Seir.
6 Comprareis deles, por dinheiro, comida que comais; também água que bebais comprareis por dinheiro.
7 Pois o Senhor, teu Deus, te abençoou em toda a obra das tuas mãos; ele sabe que andas por este grande deserto; estes quarenta anos o Senhor, teu Deus, esteve contigo; coisa nenhuma te faltou.
8 Passamos, pois, flanqueando assim nossos irmãos, os filhos de Esaú, que habitavam em Seir, como o caminho da Arabá, de Elate e de Eziom-Geber, viramo-nos e seguimos o caminho do deserto de Moabe.
9 Então, o Senhor me disse: Não molestes Moabe e não contendas com eles em peleja, porque te não darei possessão da sua terra; pois dei Ar em possessão aos filhos de Ló.
10 (Os emins, dantes, habitavam nela, povo grande, numeroso e alto como os anaquins;
11 também eles foram considerados refains, como os anaquins; e os moabitas lhes chamavam emins.
12 Os horeus também habitavam, outrora, em Seir; porém os filhos de Esaú os desapossaram, e os destruíram de diante de si, e habitaram no lugar deles, assim como Israel fez à terra da sua possessão, que o Senhor lhes tinha dado.)
13 Levantai-vos, agora, e passai o ribeiro de Zerede; assim, passamos o ribeiro de Zerede.
14 O tempo que caminhamos, desde Cades-Barneia até passarmos o ribeiro de Zerede, foram trinta e oito anos, até que toda aquela geração dos homens de guerra se consumiu do meio do arraial, como o Senhor lhes jurara.
15 Também foi contra eles a mão do Senhor, para os destruir do meio do arraial, até os haver consumido.
16 Sucedeu que, consumidos já todos os homens de guerra pela morte, do meio do povo,
17 o Senhor me falou, dizendo:
18 Hoje, passarás por Ar, pelos limites de Moabe,
19 e chegarás até defronte dos filhos de Amom; não os molestes e com eles não contendas, porque da terra dos filhos de Amom te não darei possessão, porquanto aos filhos de Ló a tenho dado por possessão.
20 (Também esta é considerada terra dos refains; dantes, habitavam nela refains, e os amonitas lhes chamavam zanzumins,
21 povo grande, numeroso e alto como os anaquins; o Senhor os destruiu diante dos amonitas; e estes, tendo-os desapossado, habitaram no lugar deles;
22 assim como fez com os filhos de Esaú que habitavam em Seir, de diante dos quais destruiu os horeus. Os filhos de Esaú, tendo-os desapossado, habitaram no lugar deles até este dia;
23 também os caftorins que saíram de Caftor destruíram os aveus, que habitavam em vilas até Gaza, e habitaram no lugar deles.)
24 Levantai-vos, parti e passai o ribeiro de Arnom; eis aqui na tua mão tenho dado a Seom, amorreu, rei de Hesbom, e a sua terra; passa a possuí-la e contende com eles em peleja.
25 Hoje, começarei a meter o terror e o medo de ti aos povos que estão debaixo de todo o céu; os que ouvirem a tua fama tremerão diante de ti e se angustiarão.
26 Então, mandei mensageiros desde o deserto de Quedemote a Seom, rei de Hesbom, com palavras de paz, dizendo:
27 deixa-me passar pela tua terra; somente pela estrada irei; não me desviarei para a direita nem para a esquerda.
28 A comida que eu coma vender-me-ás por dinheiro e dar-me-ás também por dinheiro a água que beba; tão somente deixa-me passar a pé,
29 como fizeram comigo os filhos de Esaú, que habitam em Seir, e os moabitas, que habitam em Ar; até que eu passe o Jordão, à terra que o Senhor, nosso Deus, nos dá.
30 Mas Seom, rei de Hesbom, não nos quis deixar passar por sua terra, porquanto o Senhor, teu Deus, endurecera o seu espírito e fizera obstinado o seu coração, para to dar nas mãos, como hoje se vê.
31 Disse-me, pois, o Senhor: Eis aqui, tenho começado a dar-te Seom e a sua terra; passa a desapossá-lo, para lhe ocupares o país.
32 Então, Seom saiu-nos ao encontro, ele e todo o seu povo, à peleja em Jasa.
33 E o Senhor, nosso Deus, no-lo entregou, e o derrotamos, a ele, e a seus filhos, e a todo o seu povo.
34 Naquele tempo, tomamos todas as suas cidades e a cada uma destruímos com os seus homens, mulheres e crianças; não deixamos sobrevivente algum.
35 Somente tomamos, por presa, o gado para nós e o despojo das cidades que tínhamos tomado.
36 Desde Aroer, que está à borda do vale de Arnom, e a cidade que nele está, até Gileade, nenhuma cidade houve alta demais para nós; tudo isto o Senhor, nosso Deus, nos entregou.
37 Somente à terra dos filhos de Amom não chegaste; nem a toda a borda do ribeiro de Jaboque, nem às cidades da região montanhosa, nem a lugar algum que nos proibira o Senhor, nosso Deus.*
1 Depois, nos viramos e subimos o caminho de Basã; e Ogue, rei de Basã, nos saiu ao encontro, ele e todo o seu povo, à peleja em Edrei.
2 Então, o Senhor me disse: Não temas, porque a ele, e todo o seu povo, e sua terra dei na tua mão; e far-lhe-ás como fizeste a Seom, rei dos amorreus, que habitava em Hesbom.
3 Deu-nos o Senhor, nosso Deus, em nossas mãos também a Ogue, rei de Basã, e a todo o seu povo; e ferimo-lo, até que lhe não ficou nenhum sobrevivente.
4 Nesse tempo, tomamos todas as suas cidades; nenhuma cidade houve que lhe não tomássemos: sessenta cidades, toda a região de Argobe, o reino de Ogue, em Basã.
5 Todas estas cidades eram fortificadas com altos muros, portas e ferrolhos; tomamos também outras muitas cidades, que eram sem muros.
6 Destruímo-las totalmente, como fizemos a Seom, rei de Hesbom, fazendo perecer, por completo, cada uma das cidades com os seus homens, suas mulheres e crianças.
7 Porém todo o gado e o despojo das cidades tomamos para nós, por presa.
8 Assim, nesse tempo, tomamos a terra da mão daqueles dois reis dos amorreus que estavam dalém do Jordão: desde o rio de Arnom até ao monte Hermom
9 (Os sidônios a Hermom chamam Siriom; porém os amorreus lhe chamam Senir.),
10 tomamos todas as cidades do planalto, e todo o Gileade, e todo o Basã, até Salca e Edrei, cidades do reino de Ogue, em Basã
11 (Porque só Ogue, rei de Basã, restou dos refains; eis que o seu leito, leito de ferro, não está, porventura, em Rabá dos filhos de Amom, sendo de nove côvados o seu comprimento, e de quatro, a sua largura, pelo côvado comum?).
12 Tomamos, pois, esta terra em possessão nesse tempo; desde Aroer, que está junto ao vale de Arnom, e a metade da região montanhosa de Gileade, com as suas cidades, dei aos rubenitas e gaditas.
13 O resto de Gileade, como também todo o Basã, o reino de Ogue, dei à meia tribo de Manassés; toda aquela região de Argobe, todo o Basã, se chamava a terra dos refains.
14 Jair, filho de Manassés, tomou toda a região de Argobe até ao limite dos gesuritas e maacatitas, isto é, Basã, e às aldeias chamou pelo seu nome: Havote-Jair, até o dia de hoje.
15 A Maquir dei Gileade.
16 Mas aos rubenitas e gaditas dei desde Gileade até ao vale de Arnom, cujo meio serve de limite; e até ao ribeiro de Jaboque, o limite dos filhos de Amom,
17 como também a Arabá e o Jordão por limite, desde Quinerete até ao mar da Arabá, o mar Salgado, pelas faldas de Pisga, para o oriente.
18 Nesse mesmo tempo, vos ordenei, dizendo: o Senhor, vosso Deus, vos deu esta terra, para a possuirdes; passai, pois, armados, todos os homens valentes, adiante de vossos irmãos, os filhos de Israel.
19 Tão somente vossas mulheres, e vossas crianças, e vosso gado (porque sei que tendes muito gado) ficarão nas vossas cidades que já vos tenho dado,
20 até que o Senhor dê descanso a vossos irmãos como a vós outros, para que eles também ocupem a terra que o Senhor, vosso Deus, lhes dá dalém do Jordão; então, voltareis cada qual à sua possessão que vos dei.
21 Também, nesse tempo, dei ordem a Josué, dizendo: os teus olhos veem tudo o que o Senhor, vosso Deus, tem feito a estes dois reis; assim fará o Senhor a todos os reinos a que tu passarás.
22 Não os temais, porque o Senhor, vosso Deus, é o que peleja por vós.
23 Também eu, nesse tempo, implorei graça ao Senhor, dizendo:
24 Ó Senhor Deus! Passaste a mostrar ao teu servo a tua grandeza e a tua poderosa mão; porque que deus há, nos céus ou na terra, que possa fazer segundo as tuas obras, segundo os teus poderosos feitos?
25 Rogo-te que me deixes passar, para que eu veja esta boa terra que está dalém do Jordão, esta boa região montanhosa e o Líbano.
26 Porém o Senhor indignou-se muito contra mim, por vossa causa, e não me ouviu; antes, me disse: Basta! Não me fales mais nisto.
27 Sobe ao cimo de Pisga, levanta os olhos para o ocidente, e para o norte, e para o sul, e para o oriente e contempla com os próprios olhos, porque não passarás este Jordão.
28 Dá ordens a Josué, e anima-o, e fortalece-o; porque ele passará adiante deste povo e o fará possuir a terra que tu apenas verás.
29 Assim, ficamos no vale defronte de Bete-Peor.*
1 Agora, pois, ó Israel, ouve os estatutos e os juízos que eu vos ensino, para os cumprirdes, para que vivais, e entreis, e possuais a terra que o Senhor, Deus de vossos pais, vos dá.
2 Nada acrescentareis à palavra que vos mando, nem diminuireis dela, para que guardeis os mandamentos do Senhor, vosso Deus, que eu vos mando.
3 Os vossos olhos viram o que o Senhor fez por causa de Baal-Peor; pois a todo homem que seguiu a Baal-Peor o Senhor, vosso Deus, consumiu do vosso meio.
4 Porém vós que permanecestes fiéis ao Senhor, vosso Deus, todos, hoje, estais vivos.
5 Eis que vos tenho ensinado estatutos e juízos, como me mandou o Senhor, meu Deus, para que assim façais no meio da terra que passais a possuir.
6 Guardai-os, pois, e cumpri-os, porque isto será a vossa sabedoria e o vosso entendimento perante os olhos dos povos que, ouvindo todos estes estatutos, dirão: Certamente, este grande povo é gente sábia e inteligente.
7 Pois que grande nação há que tenha deuses tão chegados a si como o Senhor, nosso Deus, todas as vezes que o invocamos?
8 E que grande nação há que tenha estatutos e juízos tão justos como toda esta lei que eu hoje vos proponho?
9 Tão somente guarda-te a ti mesmo e guarda bem a tua alma, que te não esqueças daquelas coisas que os teus olhos têm visto, e se não apartem do teu coração todos os dias da tua vida, e as farás saber a teus filhos e aos filhos de teus filhos.
10 Não te esqueças do dia em que estiveste perante o Senhor, teu Deus, em Horebe, quando o Senhor me disse: Reúne este povo, e os farei ouvir as minhas palavras, a fim de que aprenda a temer-me todos os dias que na terra viver e as ensinará a seus filhos.
11 Então, chegastes e vos pusestes ao pé do monte; e o monte ardia em fogo até ao meio dos céus, e havia trevas, e nuvens, e escuridão.
12 Então, o Senhor vos falou do meio do fogo; a voz das palavras ouvistes; porém, além da voz, não vistes aparência nenhuma.
13 Então, vos anunciou ele a sua aliança, que vos prescreveu, os dez mandamentos, e os escreveu em duas tábuas de pedra.
14 Também o Senhor me ordenou, ao mesmo tempo, que vos ensinasse estatutos e juízos, para que os cumprísseis na terra a qual passais a possuir.
15 Guardai, pois, cuidadosamente, a vossa alma, pois aparência nenhuma vistes no dia em que o Senhor, vosso Deus, vos falou em Horebe, no meio do fogo;
16 para que não vos corrompais e vos façais alguma imagem esculpida na forma de ídolo, semelhança de homem ou de mulher,
17 semelhança de algum animal que há na terra, semelhança de algum volátil que voa pelos céus,
18 semelhança de algum animal que rasteja sobre a terra, semelhança de algum peixe que há nas águas debaixo da terra.
19 Guarda-te não levantes os olhos para os céus e, vendo o sol, a lua e as estrelas, a saber, todo o exército dos céus, sejas seduzido a inclinar-te perante eles e dês culto àqueles, coisas que o Senhor, teu Deus, repartiu a todos os povos debaixo de todos os céus.
20 Mas o Senhor vos tomou e vos tirou da fornalha de ferro do Egito, para que lhe sejais povo de herança, como hoje se vê.
21 Também o Senhor se indignou contra mim, por vossa causa, e jurou que eu não passaria o Jordão e não entraria na boa terra que o Senhor, teu Deus, te dá por herança.
22 Porque eu morrerei neste lugar, não passarei o Jordão; porém vós o passareis e possuireis aquela boa terra.
23 Guardai-vos não vos esqueçais da aliança do Senhor, vosso Deus, feita convosco, e vos façais alguma imagem esculpida, semelhança de alguma coisa que o Senhor, vosso Deus, vos proibiu.
24 Porque o Senhor, teu Deus, é fogo que consome, é Deus zeloso.
25 Quando, pois, gerardes filhos e filhos de filhos, e vos envelhecerdes na terra, e vos corromperdes, e fizerdes alguma imagem esculpida, semelhança de alguma coisa, e fizerdes mal aos olhos do Senhor, teu Deus, para o provocar à ira,
26 hoje, tomo por testemunhas contra vós outros o céu e a terra, que, com efeito, perecereis, imediatamente, da terra a qual, passado o Jordão, ides possuir; não prolongareis os vossos dias nela; antes, sereis de todo destruídos.
27 O Senhor vos espalhará entre os povos, e restareis poucos em número entre as gentes aonde o Senhor vos conduzirá.
28 Lá, servireis a deuses que são obra de mãos de homens, madeira e pedra, que não veem, nem ouvem, nem comem, nem cheiram.
29 De lá, buscarás ao Senhor, teu Deus, e o acharás, quando o buscares de todo o teu coração e de toda a tua alma.
30 Quando estiveres em angústia, e todas estas coisas te sobrevierem nos últimos dias, e te voltares para o Senhor, teu Deus, e lhe atenderes a voz,
31 então, o Senhor, teu Deus, não te desamparará, porquanto é Deus misericordioso, nem te destruirá, nem se esquecerá da aliança que jurou a teus pais.
32 Agora, pois, pergunta aos tempos passados, que te precederam, desde o dia em que Deus criou o homem sobre a terra, desde uma extremidade do céu até à outra, se sucedeu jamais coisa tamanha como esta ou se se ouviu coisa como esta;
33 ou se algum povo ouviu falar a voz de algum deus do meio do fogo, como tu a ouviste, ficando vivo;
34 ou se um deus intentou ir tomar para si um povo do meio de outro povo, com provas, e com sinais, e com milagres, e com peleja, e com mão poderosa, e com braço estendido, e com grandes espantos, segundo tudo quanto o Senhor, vosso Deus, vos fez no Egito, aos vossos olhos.
35 A ti te foi mostrado para que soubesses que o Senhor é Deus; nenhum outro há, senão ele.
36 Dos céus te fez ouvir a sua voz, para te ensinar, e sobre a terra te mostrou o seu grande fogo, e do meio do fogo ouviste as suas palavras.
37 Porquanto amou teus pais, e escolheu a sua descendência depois deles, e te tirou do Egito, ele mesmo presente e com a sua grande força,
38 para lançar de diante de ti nações maiores e mais poderosas do que tu, para te introduzir na sua terra e ta dar por herança, como hoje se vê.
39 Por isso, hoje, saberás e refletirás no teu coração que só o Senhor é Deus em cima no céu e embaixo na terra; nenhum outro há.
40 Guarda, pois, os seus estatutos e os seus mandamentos que te ordeno hoje, para que te vá bem a ti e a teus filhos depois de ti e para que prolongues os dias na terra que o Senhor, teu Deus, te dá para todo o sempre.
41 Então, Moisés separou três cidades dalém do Jordão, do lado do nascimento do sol,
42 para que se acolhesse ali o homicida que matasse, involuntariamente, o seu próximo, a quem, dantes, não tivesse ódio algum, e se acolhesse a uma destas cidades e vivesse:
43 Bezer, no deserto, no planalto, para os rubenitas; Ramote, em Gileade, para os gaditas; e Golã, em Basã, para os manassitas.
44 Esta é a lei que Moisés propôs aos filhos de Israel.
45 São estes os testemunhos, e os estatutos, e os juízos que Moisés falou aos filhos de Israel, quando saíram do Egito,
46 além do Jordão, no vale defronte de Bete-Peor, na terra de Seom, rei dos amorreus, que habitava em Hesbom, a quem Moisés e os filhos de Israel feriram ao saírem do Egito,
47 e tomaram a sua terra em possessão, como também a terra de Ogue, rei de Basã, dois reis dos amorreus, que estavam além do Jordão, do lado do nascimento do sol;
48 desde Aroer, que está à borda do vale de Arnom, até ao monte Siom, que é Hermom,
49 e toda a Arabá, além do Jordão, do lado oriental, até ao mar da Arabá, pelas faldas de Pisga.*
1 Chamou Moisés a todo o Israel e disse-lhe: Ouvi, ó Israel, os estatutos e juízos que hoje vos falo aos ouvidos, para que os aprendais e cuideis em os cumprirdes.
2 O Senhor, nosso Deus, fez aliança conosco em Horebe.
3 Não foi com nossos pais que fez o Senhor esta aliança, e sim conosco, todos os que, hoje, aqui estamos vivos.
4 Face a face falou o Senhor conosco, no monte, do meio do fogo
5 (Nesse tempo, eu estava em pé entre o Senhor e vós, para vos notificar a palavra do Senhor, porque temestes o fogo e não subistes ao monte.), dizendo:
6 Eu sou o Senhor, teu Deus, que te tirei do Egito, da casa da servidão.
7 Não terás outros deuses diante de mim.
8 Não farás para ti imagem de escultura, nem semelhança alguma do que há em cima no céu, nem embaixo na terra, nem nas águas debaixo da terra;
9 não as adorarás, nem lhes darás culto; porque eu, o Senhor, teu Deus, sou Deus zeloso, que visito a iniquidade dos pais nos filhos até a terceira e quarta geração daqueles que me aborrecem,
10 e faço misericórdia até mil gerações daqueles que me amam e guardam os meus mandamentos.
11 Não tomarás o nome do Senhor, teu Deus, em vão, porque o Senhor não terá por inocente o que tomar o seu nome em vão.
12 Guarda o dia de sábado, para o santificar, como te ordenou o Senhor, teu Deus.
13 Seis dias trabalharás e farás toda a tua obra.
14 Mas o sétimo dia é o sábado do Senhor, teu Deus; não farás nenhum trabalho, nem tu, nem o teu filho, nem a tua filha, nem o teu servo, nem a tua serva, nem o teu boi, nem o teu jumento, nem animal algum teu, nem o estrangeiro das tuas portas para dentro, para que o teu servo e a tua serva descansem como tu;
15 porque te lembrarás que foste servo na terra do Egito e que o Senhor, teu Deus, te tirou dali com mão poderosa e braço estendido; pelo que o Senhor, teu Deus, te ordenou que guardasses o dia de sábado.
16 Honra a teu pai e a tua mãe, como o Senhor, teu Deus, te ordenou, para que se prolonguem os teus dias e para que te vá bem na terra que o Senhor, teu Deus, te dá.
17 Não matarás.
18 Não adulterarás.
19 Não furtarás.
20 Não dirás falso testemunho contra o teu próximo.
21 Não cobiçarás a mulher do teu próximo. Não desejarás a casa do teu próximo, nem o seu campo, nem o seu servo, nem a sua serva, nem o seu boi, nem o seu jumento, nem coisa alguma do teu próximo.
22 Estas palavras falou o Senhor a toda a vossa congregação no monte, do meio do fogo, da nuvem e da escuridade, com grande voz, e nada acrescentou. Tendo-as escrito em duas tábuas de pedra, deu-mas a mim.
23 Sucedeu que, ouvindo a voz do meio das trevas, enquanto ardia o monte em fogo, vos achegastes a mim, todos os cabeças das vossas tribos e vossos anciãos,
24 e dissestes: Eis aqui o Senhor, nosso Deus, nos fez ver a sua glória e a sua grandeza, e ouvimos a sua voz do meio do fogo; hoje, vimos que Deus fala com o homem, e este permanece vivo.
25 Agora, pois, por que morreríamos? Pois este grande fogo nos consumiria; se ainda mais ouvíssemos a voz do Senhor, nosso Deus, morreríamos.
26 Porque quem há, de toda carne, que tenha ouvido a voz do Deus vivo falar do meio do fogo, como nós ouvimos, e permanecido vivo?
27 Chega-te, e ouve tudo o que disser o Senhor, nosso Deus; e tu nos dirás tudo o que te disser o Senhor, nosso Deus, e o ouviremos, e o cumpriremos.
28 Ouvindo, pois, o Senhor as vossas palavras, quando me faláveis a mim, o Senhor me disse: Eu ouvi as palavras deste povo, as quais te disseram; em tudo falaram eles bem.
29 Quem dera que eles tivessem tal coração, que me temessem e guardassem em todo o tempo todos os meus mandamentos, para que bem lhes fosse a eles e a seus filhos, para sempre!
30 Vai, dize-lhes: Tornai-vos às vossas tendas.
31 Tu, porém, fica-te aqui comigo, e eu te direi todos os mandamentos, e estatutos, e juízos que tu lhes hás de ensinar que cumpram na terra que eu lhes darei para possuí-la.
32 Cuidareis em fazerdes como vos mandou o Senhor, vosso Deus; não vos desviareis, nem para a direita, nem para a esquerda.
33 Andareis em todo o caminho que vos manda o Senhor, vosso Deus, para que vivais, bem vos suceda, e prolongueis os dias na terra que haveis de possuir.*
1 Estes, pois, são os mandamentos, os estatutos e os juízos que mandou o Senhor, teu Deus, se te ensinassem, para que os cumprisses na terra a que passas para a possuir;
2 para que temas ao Senhor, teu Deus, e guardes todos os seus estatutos e mandamentos que eu te ordeno, tu, e teu filho, e o filho de teu filho, todos os dias da tua vida; e que teus dias sejam prolongados.
3 Ouve, pois, ó Israel, e atenta em os cumprires, para que bem te suceda, e muito te multipliques na terra que mana leite e mel, como te disse o Senhor, Deus de teus pais.
4 Ouve, Israel, o Senhor, nosso Deus, é o único Senhor.
5 Amarás, pois, o Senhor, teu Deus, de todo o teu coração, de toda a tua alma e de toda a tua força.
6 Estas palavras que, hoje, te ordeno estarão no teu coração;
7 tu as inculcarás a teus filhos, e delas falarás assentado em tua casa, e andando pelo caminho, e ao deitar-te, e ao levantar-te.
8 Também as atarás como sinal na tua mão, e te serão por frontal entre os olhos.
9 E as escreverás nos umbrais de tua casa e nas tuas portas.
10 Havendo-te, pois, o Senhor, teu Deus, introduzido na terra que, sob juramento, prometeu a teus pais, Abraão, Isaque e Jacó, te daria, grandes e boas cidades, que tu não edificaste;
11 e casas cheias de tudo o que é bom, casas que não encheste; e poços abertos, que não abriste; vinhais e olivais, que não plantaste; e, quando comeres e te fartares,
12 guarda-te, para que não esqueças o Senhor, que te tirou da terra do Egito, da casa da servidão.
13 O Senhor, teu Deus, temerás, a ele servirás, e, pelo seu nome, jurarás.
14 Não seguirás outros deuses, nenhum dos deuses dos povos que houver à roda de ti,
15 porque o Senhor, teu Deus, é Deus zeloso no meio de ti, para que a ira do Senhor, teu Deus, se não acenda contra ti e te destrua de sobre a face da terra.
16 Não tentarás o Senhor, teu Deus, como o tentaste em Massá.
17 Diligentemente, guardarás os mandamentos do Senhor, teu Deus, e os seus testemunhos, e os seus estatutos que te ordenou.
18 Farás o que é reto e bom aos olhos do Senhor, para que bem te suceda, e entres, e possuas a boa terra a qual o Senhor, sob juramento, prometeu dar a teus pais,
19 lançando todos os teus inimigos de diante de ti, como o Senhor tem dito.
20 Quando teu filho, no futuro, te perguntar, dizendo: Que significam os testemunhos, e estatutos, e juízos que o Senhor, nosso Deus, vos ordenou?
21 Então, dirás a teu filho: Éramos servos de Faraó, no Egito; porém o Senhor de lá nos tirou com poderosa mão.
22 Aos nossos olhos fez o Senhor sinais e maravilhas, grandes e terríveis, contra o Egito e contra Faraó e toda a sua casa;
23 e dali nos tirou, para nos levar e nos dar a terra que sob juramento prometeu a nossos pais.
24 O Senhor nos ordenou cumpríssemos todos estes estatutos e temêssemos o Senhor, nosso Deus, para o nosso perpétuo bem, para nos guardar em vida, como tem feito até hoje.
25 Será por nós justiça, quando tivermos cuidado de cumprir todos estes mandamentos perante o Senhor, nosso Deus, como nos tem ordenado.*
1 Quando o Senhor, teu Deus, te introduzir na terra a qual passas a possuir, e tiver lançado muitas nações de diante de ti, os heteus, e os girgaseus, e os amorreus, e os cananeus, e os ferezeus, e os heveus, e os jebuseus, sete nações mais numerosas e mais poderosas do que tu;
2 e o Senhor, teu Deus, as tiver dado diante de ti, para as ferir, totalmente as destruirás; não farás com elas aliança, nem terás piedade delas;
3 nem contrairás matrimônio com os filhos dessas nações; não darás tuas filhas a seus filhos, nem tomarás suas filhas para teus filhos;
4 pois elas fariam desviar teus filhos de mim, para que servissem a outros deuses; e a ira do Senhor se acenderia contra vós outros e depressa vos destruiria.
5 Porém assim lhes fareis: derribareis os seus altares, quebrareis as suas colunas, cortareis os seus postes-ídolos e queimareis as suas imagens de escultura.
6 Porque tu és povo santo ao Senhor, teu Deus; o Senhor, teu Deus, te escolheu, para que lhe fosses o seu povo próprio, de todos os povos que há sobre a terra.
7 Não vos teve o Senhor afeição, nem vos escolheu porque fôsseis mais numerosos do que qualquer povo, pois éreis o menor de todos os povos,
8 mas porque o Senhor vos amava e, para guardar o juramento que fizera a vossos pais, o Senhor vos tirou com mão poderosa e vos resgatou da casa da servidão, do poder de Faraó, rei do Egito.
9 Saberás, pois, que o Senhor, teu Deus, é Deus, o Deus fiel, que guarda a aliança e a misericórdia até mil gerações aos que o amam e cumprem os seus mandamentos;
10 e dá o pago diretamente aos que o odeiam, fazendo-os perecer; não será demorado para com o que o odeia; prontamente, lho retribuirá.
11 Guarda, pois, os mandamentos, e os estatutos, e os juízos que hoje te mando cumprir.
12 Será, pois, que, se, ouvindo estes juízos, os guardares e cumprires, o Senhor, teu Deus, te guardará a aliança e a misericórdia prometida sob juramento a teus pais;
13 ele te amará, e te abençoará, e te fará multiplicar; também abençoará os teus filhos, e o fruto da tua terra, e o teu cereal, e o teu vinho, e o teu azeite, e as crias das tuas vacas e das tuas ovelhas, na terra que, sob juramento a teus pais, prometeu dar-te.
14 Bendito serás mais do que todos os povos; não haverá entre ti nem homem, nem mulher estéril, nem entre os teus animais.
15 O Senhor afastará de ti toda enfermidade; sobre ti não porá nenhuma das doenças malignas dos egípcios, que bem sabes; antes, as porá sobre todos os que te odeiam.
16 Consumirás todos os povos que te der o Senhor, teu Deus; os teus olhos não terão piedade deles, nem servirás a seus deuses, pois isso te seria por ciladas.
17 Se disseres no teu coração: Estas nações são mais numerosas do que eu; como poderei desapossá-las?
18 Delas não tenhas temor; lembrar-te-ás do que o Senhor, teu Deus, fez a Faraó e a todo o Egito;
19 das grandes provas que viram os teus olhos, e dos sinais, e maravilhas, e mão poderosa, e braço estendido, com que o Senhor, teu Deus, te tirou; assim fará o Senhor, teu Deus, com todos os povos, aos quais temes.
20 Além disso, o Senhor, teu Deus, mandará entre eles vespões, até que pereçam os que ficarem e se esconderem de diante de ti.
21 Não te espantes diante deles, porque o Senhor, teu Deus, está no meio de ti, Deus grande e temível.
22 O Senhor, teu Deus, lançará fora estas nações, pouco a pouco, de diante de ti; não poderás destruí-las todas de pronto, para que as feras do campo se não multipliquem contra ti.
23 Mas o Senhor, teu Deus, tas entregará e lhes infligirá grande confusão, até que sejam destruídas.
24 Entregar-te-á também nas mãos os seus reis, para que apagues o nome deles de debaixo dos céus; nenhum homem poderá resistir-te, até que os destruas.
25 As imagens de escultura de seus deuses queimarás; a prata e o ouro que estão sobre elas não cobiçarás, nem os tomarás para ti, para que te não enlaces neles; pois são abominação ao Senhor, teu Deus.
26 Não meterás, pois, coisa abominável em tua casa, para que não sejas amaldiçoado, semelhante a ela; de todo, a detestarás e, de todo, a abominarás, pois é amaldiçoada.*
1 Cuidareis de cumprir todos os mandamentos que hoje vos ordeno, para que vivais, e vos multipliqueis, e entreis, e possuais a terra que o Senhor prometeu sob juramento a vossos pais.
2 Recordar-te-ás de todo o caminho pelo qual o Senhor, teu Deus, te guiou no deserto estes quarenta anos, para te humilhar, para te provar, para saber o que estava no teu coração, se guardarias ou não os seus mandamentos.
3 Ele te humilhou, e te deixou ter fome, e te sustentou com o maná, que tu não conhecias, nem teus pais o conheciam, para te dar a entender que não só de pão viverá o homem, mas de tudo o que procede da boca do Senhor viverá o homem.
4 Nunca envelheceu a tua veste sobre ti, nem se inchou o teu pé nestes quarenta anos.
5 Sabe, pois, no teu coração, que, como um homem disciplina a seu filho, assim te disciplina o Senhor, teu Deus.
6 Guarda os mandamentos do Senhor, teu Deus, para andares nos seus caminhos e o temeres;
7 porque o Senhor, teu Deus, te faz entrar numa boa terra, terra de ribeiros de águas, de fontes, de mananciais profundos, que saem dos vales e das montanhas;
8 terra de trigo e cevada, de vides, figueiras e romeiras; terra de oliveiras, de azeite e mel;
9 terra em que comerás o pão sem escassez, e nada te faltará nela; terra cujas pedras são ferro e de cujos montes cavarás o cobre.
10 Comerás, e te fartarás, e louvarás o Senhor, teu Deus, pela boa terra que te deu.
11 Guarda-te não te esqueças do Senhor, teu Deus, não cumprindo os seus mandamentos, os seus juízos e os seus estatutos, que hoje te ordeno;
12 para não suceder que, depois de teres comido e estiveres farto, depois de haveres edificado boas casas e morado nelas;
13 depois de se multiplicarem os teus gados e os teus rebanhos, e se aumentar a tua prata e o teu ouro, e ser abundante tudo quanto tens,
14 se eleve o teu coração, e te esqueças do Senhor, teu Deus, que te tirou da terra do Egito, da casa da servidão,
15 que te conduziu por aquele grande e terrível deserto de serpentes abrasadoras, de escorpiões e de secura, em que não havia água; e te fez sair água da pederneira;
16 que no deserto te sustentou com maná, que teus pais não conheciam; para te humilhar, e para te provar, e, afinal, te fazer bem.
17 Não digas, pois, no teu coração: A minha força e o poder do meu braço me adquiriram estas riquezas.
18 Antes, te lembrarás do Senhor, teu Deus, porque é ele o que te dá força para adquirires riquezas; para confirmar a sua aliança, que, sob juramento, prometeu a teus pais, como hoje se vê.
19 Se te esqueceres do Senhor, teu Deus, e andares após outros deuses, e os servires, e os adorares, protesto, hoje, contra vós outros que perecereis.
20 Como as nações que o Senhor destruiu de diante de vós, assim perecereis; porquanto não quisestes obedecer à voz do Senhor, vosso Deus.*
1 Ouve, ó Israel, tu passas, hoje, o Jordão para entrares a possuir nações maiores e mais fortes do que tu; cidades grandes e amuralhadas até aos céus;
2 povo grande e alto, filhos dos anaquins, que tu conheces e de que já ouvistes: Quem poderá resistir aos filhos de Enaque?
3 Sabe, pois, hoje, que o Senhor, teu Deus, é que passa adiante de ti; é fogo que consome, e os destruirá, e os subjugará diante de ti; assim, os desapossarás e, depressa, os farás perecer, como te prometeu o Senhor.
4 Quando, pois, o Senhor, teu Deus, os tiver lançado de diante de ti, não digas no teu coração: Por causa da minha justiça é que o Senhor me trouxe a esta terra para a possuir, porque, pela maldade destas gerações, é que o Senhor as lança de diante de ti.
5 Não é por causa da tua justiça, nem pela retitude do teu coração que entras a possuir a sua terra, mas pela maldade destas nações o Senhor, teu Deus, as lança de diante de ti; e para confirmar a palavra que o Senhor, teu Deus, jurou a teus pais, Abraão, Isaque e Jacó.
6 Sabe, pois, que não é por causa da tua justiça que o Senhor, teu Deus, te dá esta boa terra para possuí-la, pois tu és povo de dura cerviz.
7 Lembrai-vos e não vos esqueçais de que muito provocastes à ira o Senhor, vosso Deus, no deserto; desde o dia em que saístes do Egito até que chegastes a este lugar, rebeldes fostes contra o Senhor;
8 pois, em Horebe, tanto provocastes à ira o Senhor, que a ira do Senhor se acendeu contra vós para vos destruir.
9 Subindo eu ao monte a receber as tábuas de pedra, as tábuas da aliança que o Senhor fizera convosco, fiquei no monte quarenta dias e quarenta noites; não comi pão, nem bebi água.
10 Deu-me o Senhor as duas tábuas de pedra, escritas com o dedo de Deus; e, nelas, estavam todas as palavras segundo o Senhor havia falado convosco no monte, do meio do fogo, estando reunido todo o povo.
11 Ao fim dos quarenta dias e quarenta noites, o Senhor me deu as duas tábuas de pedra, as tábuas da aliança.
12 E o Senhor me disse: Levanta-te, desce depressa daqui, porque o teu povo, que tiraste do Egito, já se corrompeu; cedo se desviou do caminho que lhe ordenei; imagem fundida para si fez.
13 Falou-me ainda o Senhor, dizendo: Atentei para este povo, e eis que ele é povo de dura cerviz.
14 Deixa-me que o destrua e apague o seu nome de debaixo dos céus; e te faça a ti nação mais forte e mais numerosa do que esta.
15 Então, me virei e desci do monte; e o monte ardia em fogo; as duas tábuas da aliança estavam em ambas as minhas mãos.
16 Olhei, e eis que havíeis pecado contra o Senhor, vosso Deus; tínheis feito para vós outros um bezerro fundido; cedo vos desviastes do caminho que o Senhor vos ordenara.
17 Então, peguei as duas tábuas, e as arrojei das minhas mãos, e as quebrei ante os vossos olhos.
18 Prostrado estive perante o Senhor, como dantes, quarenta dias e quarenta noites; não comi pão e não bebi água, por causa de todo o vosso pecado que havíeis cometido, fazendo mal aos olhos do Senhor, para o provocar à ira.
19 Pois temia por causa da ira e do furor com que o Senhor tanto estava irado contra vós outros para vos destruir; porém ainda esta vez o Senhor me ouviu.
20 O Senhor se irou muito contra Arão para o destruir; mas também orei por Arão ao mesmo tempo.
21 Porém tomei o vosso pecado, o bezerro que tínheis feito, e o queimei, e o esmaguei, moendo-o bem, até que se desfez em pó; e o seu pó lancei no ribeiro que descia do monte.
22 Também em Taberá, em Massá e em Quibrote-Hataavá provocastes muito a ira do Senhor.
23 Quando também o Senhor vos enviou de Cades-Barneia, dizendo: Subi e possuí a terra que vos dei, rebeldes fostes ao mandado do Senhor, vosso Deus, e não o crestes, e não obedecestes à sua voz.
24 Rebeldes fostes contra o Senhor, desde o dia em que vos conheci.
25 Prostrei-me, pois, perante o Senhor e, quarenta dias e quarenta noites, estive prostrado; porquanto o Senhor dissera que vos queria destruir.
26 Orei ao Senhor, dizendo: Ó Senhor Deus! Não destruas o teu povo e a tua herança, que resgataste com a tua grandeza, que tiraste do Egito com poderosa mão.
27 Lembra-te dos teus servos Abraão, Isaque e Jacó; não atentes para a dureza deste povo, nem para a sua maldade, nem para o seu pecado,
28 para que o povo da terra donde nos tiraste não diga: Não tendo podido o Senhor introduzi-los na terra de que lhes tinha falado e porque os aborrecia, os tirou para matá-los no deserto.
29 Todavia, são eles o teu povo e a tua herança, que tiraste com a tua grande força e com o braço estendido.*
1 Naquele tempo, me disse o Senhor: Lavra duas tábuas de pedra, como as primeiras, e sobe a mim ao monte, e faze uma arca de madeira.
2 Escreverei nas duas tábuas as palavras que estavam nas primeiras que quebraste, e as porás na arca.
3 Assim, fiz uma arca de madeira de acácia, lavrei duas tábuas de pedra, como as primeiras, e subi ao monte com as duas tábuas na mão.
4 Então, escreveu o Senhor nas tábuas, segundo a primeira escritura, os dez mandamentos que ele vos falara no dia da congregação, no monte, no meio do fogo; e o Senhor mas deu a mim.
5 Virei-me, e desci do monte, e pus as tábuas na arca que eu fizera; e ali estão, como o Senhor me ordenou.
6 Partiram os filhos de Israel de Beerote-Benê-Jaacã para Mosera. Ali faleceu Arão e ali foi sepultado. Eleazar, seu filho, oficiou como sacerdote em seu lugar.
7 Dali partiram para Gudgoda e de Gudgoda para Jotbatá, terra de ribeiros de águas.
8 Por esse mesmo tempo, o Senhor separou a tribo de Levi para levar a arca da Aliança do Senhor, para estar diante do Senhor, para o servir e para abençoar em seu nome até ao dia de hoje.
9 Pelo que Levi não tem parte nem herança com seus irmãos; o Senhor é a sua herança, como o Senhor, teu Deus, lhe tem prometido.
10 Permaneci no monte, como da primeira vez, quarenta dias e quarenta noites; o Senhor me ouviu ainda por esta vez; não quis o Senhor destruir-te.
11 Porém o Senhor me disse: Levanta-te, põe-te a caminho diante do povo, para que entre e possua a terra que, sob juramento, prometi dar a seus pais.
12 Agora, pois, ó Israel, que é que o Senhor requer de ti? Não é que temas o Senhor, teu Deus, e andes em todos os seus caminhos, e o ames, e sirvas ao Senhor, teu Deus, de todo o teu coração e de toda a tua alma,
13 para guardares os mandamentos do Senhor e os seus estatutos que hoje te ordeno, para o teu bem?
14 Eis que os céus e os céus dos céus são do Senhor, teu Deus, a terra e tudo o que nela há.
15 Tão somente o Senhor se afeiçoou a teus pais para os amar; a vós outros, descendentes deles, escolheu de todos os povos, como hoje se vê.
16 Circuncidai, pois, o vosso coração e não mais endureçais a vossa cerviz.
17 Pois o Senhor, vosso Deus, é o Deus dos deuses e o Senhor dos senhores, o Deus grande, poderoso e temível, que não faz acepção de pessoas, nem aceita suborno;
18 que faz justiça ao órfão e à viúva e ama o estrangeiro, dando-lhe pão e vestes.
19 Amai, pois, o estrangeiro, porque fostes estrangeiros na terra do Egito.
20 Ao Senhor, teu Deus, temerás; a ele servirás, a ele te chegarás e, pelo seu nome, jurarás.
21 Ele é o teu louvor e o teu Deus, que te fez estas grandes e temíveis coisas que os teus olhos têm visto.
22 Com setenta almas, teus pais desceram ao Egito; e, agora, o Senhor, teu Deus, te pôs como as estrelas dos céus em multidão.*
1 Amarás, pois, o Senhor, teu Deus, e todos os dias guardarás os seus preceitos, os seus estatutos, os seus juízos e os seus mandamentos.
2 Considerai hoje (não falo com os vossos filhos que não conheceram, nem viram a disciplina do Senhor, vosso Deus), considerai a grandeza do Senhor, a sua poderosa mão e o seu braço estendido;
3 e também os seus sinais, as suas obras, que fez no meio do Egito a Faraó, rei do Egito, e a toda a sua terra;
4 e o que fez ao exército do Egito, aos seus cavalos e aos seus carros, fazendo passar sobre eles as águas do mar Vermelho, quando vos perseguiam, e como o Senhor os destruiu até ao dia de hoje;
5 e o que fez no deserto, até que chegastes a este lugar;
6 e ainda o que fez a Datã e a Abirão, filhos de Eliabe, filho de Rúben; como a terra abriu a boca e os tragou e bem assim a sua família, suas tendas e tudo o que os seguia, no meio de todo o Israel;
7 porquanto os vossos olhos são os que viram todas as grandes obras que fez o Senhor.
8 Guardai, pois, todos os mandamentos que hoje vos ordeno, para que sejais fortes, e entreis, e possuais a terra para onde vos dirigis;
9 para que prolongueis os dias na terra que o Senhor, sob juramento, prometeu dar a vossos pais e à sua descendência, terra que mana leite e mel.
10 Porque a terra que passais a possuir não é como a terra do Egito, donde saístes, em que semeáveis a vossa semente e, com o pé, a regáveis como a uma horta;
11 mas a terra que passais a possuir é terra de montes e de vales; da chuva dos céus beberá as águas;
12 terra de que cuida o Senhor, vosso Deus; os olhos do Senhor, vosso Deus, estão sobre ela continuamente, desde o princípio até ao fim do ano.
13 Se diligentemente obedecerdes a meus mandamentos que hoje vos ordeno, de amar o Senhor, vosso Deus, e de o servir de todo o vosso coração e de toda a vossa alma,
14 darei as chuvas da vossa terra a seu tempo, as primeiras e as últimas, para que recolhais o vosso cereal, e o vosso vinho, e o vosso azeite.
15 Darei erva no vosso campo aos vossos gados, e comereis e vos fartareis.
16 Guardai-vos não suceda que o vosso coração se engane, e vos desvieis, e sirvais a outros deuses, e vos prostreis perante eles;
17 que a ira do Senhor se acenda contra vós outros, e feche ele os céus, e não haja chuva, e a terra não dê a sua messe, e cedo sejais eliminados da boa terra que o Senhor vos dá.
18 Ponde, pois, estas minhas palavras no vosso coração e na vossa alma; atai-as por sinal na vossa mão, para que estejam por frontal entre os olhos.
19 Ensinai-as a vossos filhos, falando delas assentados em vossa casa, e andando pelo caminho, e deitando-vos, e levantando-vos.
20 Escrevei-as nos umbrais de vossa casa e nas vossas portas,
21 para que se multipliquem os vossos dias e os dias de vossos filhos na terra que o Senhor, sob juramento, prometeu dar a vossos pais, e sejam tão numerosos como os dias do céu acima da terra.
22 Porque, se diligentemente guardardes todos estes mandamentos que vos ordeno para os guardardes, amando o Senhor, vosso Deus, andando em todos os seus caminhos, e a ele vos achegardes,
23 o Senhor desapossará todas estas nações, e possuireis nações maiores e mais poderosas do que vós.
24 Todo lugar que pisar a planta do vosso pé, desde o deserto, desde o Líbano, desde o rio, o rio Eufrates, até ao mar ocidental, será vosso.
25 Ninguém vos poderá resistir; o Senhor, vosso Deus, porá sobre toda terra que pisardes o vosso terror e o vosso temor, como já vos tem dito.
26 Eis que, hoje, eu ponho diante de vós a bênção e a maldição:
27 a bênção, quando cumprirdes os mandamentos do Senhor, vosso Deus, que hoje vos ordeno;
28 a maldição, se não cumprirdes os mandamentos do Senhor, vosso Deus, mas vos desviardes do caminho que hoje vos ordeno, para seguirdes outros deuses que não conhecestes.
29 Quando, porém, o Senhor, teu Deus, te introduzir na terra a que vais para possuí-la, então, pronunciarás a bênção sobre o monte Gerizim e a maldição sobre o monte Ebal.
30 Porventura, não estão eles além do Jordão, na direção do pôr do sol, na terra dos cananeus, que habitam na Arabá, defronte de Gilgal, junto aos carvalhais de Moré?
31 Pois ides passar o Jordão para entrardes e possuirdes a terra que vos dá o Senhor, vosso Deus; possuí-la-eis e nela habitareis.
32 Tende, pois, cuidado em cumprir todos os estatutos e os juízos que eu, hoje, vos prescrevo.*
1 São estes os estatutos e os juízos que cuidareis de cumprir na terra que vos deu o Senhor, Deus de vossos pais, para a possuirdes todos os dias que viverdes sobre a terra.
2 Destruireis por completo todos os lugares onde as nações que ides desapossar serviram aos seus deuses, sobre as altas montanhas, sobre os outeiros e debaixo de toda árvore frondosa;
3 deitareis abaixo os seus altares, e despedaçareis as suas colunas, e os seus postes-ídolos queimareis, e despedaçareis as imagens esculpidas dos seus deuses, e apagareis o seu nome daquele lugar.
4 Não fareis assim para com o Senhor, vosso Deus,
5 mas buscareis o lugar que o Senhor, vosso Deus, escolher de todas as vossas tribos, para ali pôr o seu nome e sua habitação; e para lá ireis.
6 A esse lugar fareis chegar os vossos holocaustos, e os vossos sacrifícios, e os vossos dízimos, e a oferta das vossas mãos, e as ofertas votivas, e as ofertas voluntárias, e os primogênitos das vossas vacas e das vossas ovelhas.
7 Lá, comereis perante o Senhor, vosso Deus, e vos alegrareis em tudo o que fizerdes, vós e as vossas casas, no que vos tiver abençoado o Senhor, vosso Deus.
8 Não procedereis em nada segundo estamos fazendo aqui, cada qual tudo o que bem parece aos seus olhos,
9 porque, até agora, não entrastes no descanso e na herança que vos dá o Senhor, vosso Deus.
10 Mas passareis o Jordão e habitareis na terra que vos fará herdar o Senhor, vosso Deus; e vos dará descanso de todos os vossos inimigos em redor, e morareis seguros.
11 Então, haverá um lugar que escolherá o Senhor, vosso Deus, para ali fazer habitar o seu nome; a esse lugar fareis chegar tudo o que vos ordeno: os vossos holocaustos, e os vossos sacrifícios, e os vossos dízimos, e a oferta das vossas mãos, e toda escolha dos vossos votos feitos ao Senhor,
12 e vos alegrareis perante o Senhor, vosso Deus, vós, os vossos filhos, as vossas filhas, os vossos servos, as vossas servas e o levita que mora dentro das vossas cidades e que não tem porção nem herança convosco.
13 Guarda-te, não ofereças os teus holocaustos em todo lugar que vires;
14 mas, no lugar que o Senhor escolher numa das tuas tribos, ali oferecerás os teus holocaustos e ali farás tudo o que te ordeno.
15 Porém, consoante todo desejo da tua alma, poderás matar e comer carne nas tuas cidades, segundo a bênção do Senhor, teu Deus; o imundo e o limpo dela comerão, assim como se come da carne do corço e do veado.
16 Tão somente o sangue não comerás; sobre a terra o derramarás como água.
17 Nas tuas cidades, não poderás comer o dízimo do teu cereal, nem do teu vinho, nem do teu azeite, nem os primogênitos das tuas vacas, nem das tuas ovelhas, nem nenhuma das tuas ofertas votivas, que houveres prometido, nem as tuas ofertas voluntárias, nem as ofertas das tuas mãos;
18 mas o comerás perante o Senhor, teu Deus, no lugar que o Senhor, teu Deus, escolher, tu, e teu filho, e tua filha, e teu servo, e tua serva, e o levita que mora na tua cidade; e perante o Senhor, teu Deus, te alegrarás em tudo o que fizeres.
19 Guarda-te, não desampares o levita todos os teus dias na terra.
20 Quando o Senhor, teu Deus, alargar o teu território, como te prometeu, e, por desejares comer carne, disseres: Comerei carne, então, segundo o teu desejo, comerás carne.
21 Se estiver longe de ti o lugar que o Senhor, teu Deus, escolher para nele pôr o seu nome, então, matarás das tuas vacas e tuas ovelhas, que o Senhor te houver dado, como te ordenei; e comerás dentro da tua cidade, segundo todo o teu desejo.
22 Porém, como se come da carne do corço e do veado, assim comerás destas carnes; destas comerá tanto o homem imundo como o limpo.
23 Somente empenha-te em não comeres o sangue, pois o sangue é a vida; pelo que não comerás a vida com a carne.
24 Não o comerás; na terra o derramarás como água.
25 Não o comerás, para que bem te suceda a ti e a teus filhos, depois de ti, quando fizeres o que é reto aos olhos do Senhor.
26 Porém tomarás o que houveres consagrado daquilo que te pertence e as tuas ofertas votivas e virás ao lugar que o Senhor escolher.
27 E oferecerás os teus holocaustos, a carne e o sangue sobre o altar do Senhor, teu Deus; e o sangue dos teus sacrifícios se derramará sobre o altar do Senhor, teu Deus; porém a carne comerás.
28 Guarda e cumpre todas estas palavras que te ordeno, para que bem te suceda a ti e a teus filhos, depois de ti, para sempre, quando fizeres o que é bom e reto aos olhos do Senhor, teu Deus.
29 Quando o Senhor, teu Deus, eliminar de diante de ti as nações, para as quais vais para possuí-las, e as desapossares e habitares na sua terra,
30 guarda-te, não te enlaces com imitá-las, após terem sido destruídas diante de ti; e que não indagues acerca dos seus deuses, dizendo: Assim como serviram estas nações aos seus deuses, do mesmo modo também farei eu.
31 Não farás assim ao Senhor, teu Deus, porque tudo o que é abominável ao Senhor e que ele odeia fizeram eles a seus deuses, pois até seus filhos e suas filhas queimaram aos seus deuses.
32 Tudo o que eu te ordeno observarás; nada lhe acrescentarás, nem diminuirás.*
1 Quando profeta ou sonhador se levantar no meio de ti e te anunciar um sinal ou prodígio,
2 e suceder o tal sinal ou prodígio de que te houver falado, e disser: Vamos após outros deuses, que não conheceste, e sirvamo-los,
3 não ouvirás as palavras desse profeta ou sonhador; porquanto o Senhor, vosso Deus, vos prova, para saber se amais o Senhor, vosso Deus, de todo o vosso coração e de toda a vossa alma.
4 Andareis após o Senhor, vosso Deus, e a ele temereis; guardareis os seus mandamentos, ouvireis a sua voz, a ele servireis e a ele vos achegareis.
5 Esse profeta ou sonhador será morto, pois pregou rebeldia contra o Senhor, vosso Deus, que vos tirou da terra do Egito e vos resgatou da casa da servidão, para vos apartar do caminho que vos ordenou o Senhor, vosso Deus, para andardes nele. Assim, eliminarás o mal do meio de ti.
6 Se teu irmão, filho de tua mãe, ou teu filho, ou tua filha, ou a mulher do teu amor, ou teu amigo que amas como à tua alma te incitar em segredo, dizendo: Vamos e sirvamos a outros deuses, que não conheceste, nem tu, nem teus pais,
7 dentre os deuses dos povos que estão em redor de ti, perto ou longe de ti, desde uma até à outra extremidade da terra,
8 não concordarás com ele, nem o ouvirás; não olharás com piedade, não o pouparás, nem o esconderás,
9 mas, certamente, o matarás. A tua mão será a primeira contra ele, para o matar, e depois a mão de todo o povo.
10 Apedrejá-lo-ás até que morra, pois te procurou apartar do Senhor, teu Deus, que te tirou da terra do Egito, da casa da servidão.
11 E todo o Israel ouvirá e temerá, e não se tornará a praticar maldade como esta no meio de ti.
12 Quando em alguma das tuas cidades que o Senhor, teu Deus, te dá, para ali habitares, ouvires dizer
13 que homens malignos saíram do meio de ti e incitaram os moradores da sua cidade, dizendo: Vamos e sirvamos a outros deuses, que não conheceste,
14 então, inquirirás, investigarás e, com diligência, perguntarás; e eis que, se for verdade e certo que tal abominação se cometeu no meio de ti,
15 então, certamente, ferirás a fio de espada os moradores daquela cidade, destruindo-a completamente e tudo o que nela houver, até os animais.
16 Ajuntarás todo o seu despojo no meio da sua praça e a cidade e todo o seu despojo queimarás por oferta total ao Senhor, teu Deus, e será montão perpétuo de ruínas; nunca mais se edificará.
17 Também nada do que for condenado deverá ficar em tua mão, para que o Senhor se aparte do ardor da sua ira, e te faça misericórdia, e tenha piedade de ti, e te multiplique, como jurou a teus pais,
18 se ouvires a voz do Senhor, teu Deus, e guardares todos os seus mandamentos que hoje te ordeno, para fazeres o que é reto aos olhos do Senhor, teu Deus.*
1 Filhos sois do Senhor, vosso Deus; não vos dareis golpes, nem sobre a testa fareis calva por causa de algum morto.
2 Porque sois povo santo ao Senhor, vosso Deus, e o Senhor vos escolheu de todos os povos que há sobre a face da terra, para lhe serdes seu povo próprio.
3 Não comereis coisa alguma abominável.
4 São estes os animais que comereis: o boi, a ovelha, a cabra,
5 o veado, a gazela, a corça, a cabra montês, o antílope, a ovelha montês e o gamo.
6 Todo animal que tem unhas fendidas, e o casco se divide em dois, e rumina, entre os animais, isso comereis.
7 Porém estes não comereis, dos que somente ruminam ou que têm a unha fendida: o camelo, a lebre e o arganaz, porque ruminam, mas não têm a unha fendida; imundos vos serão.
8 Nem o porco, porque tem unha fendida, mas não rumina; imundo vos será. Destes não comereis a carne e não tocareis no seu cadáver.
9 Isto comereis de tudo o que há nas águas: tudo o que tem barbatanas e escamas.
10 Mas tudo o que não tiver barbatanas nem escamas não o comereis; imundo vos será.
11 Toda ave limpa comereis.
12 Estas, porém, são as que não comereis: a águia, o quebrantosso, a águia marinha,
13 o açor, o falcão e o milhano, segundo a sua espécie;
14 e todo corvo, segundo a sua espécie;
15 o avestruz, a coruja, a gaivota e o gavião, segundo a sua espécie;
16 o mocho, a íbis, a gralha,
17 o pelicano, o abutre, o corvo marinho,
18 a cegonha, e a garça, segundo a sua espécie, e a poupa, e o morcego.
19 Também todo inseto que voa vos será imundo; não se comerá.
20 Toda ave limpa comereis.
21 Não comereis nenhum animal que morreu por si. Podereis dá-lo ao estrangeiro que está dentro da tua cidade, para que o coma, ou vendê-lo ao estranho, porquanto sois povo santo ao Senhor, vosso Deus. Não cozerás o cabrito no leite da sua própria mãe.
22 Certamente, darás os dízimos de todo o fruto das tuas sementes, que ano após ano se recolher do campo.
23 E, perante o Senhor, teu Deus, no lugar que escolher para ali fazer habitar o seu nome, comerás os dízimos do teu cereal, do teu vinho, do teu azeite e os primogênitos das tuas vacas e das tuas ovelhas; para que aprendas a temer o Senhor, teu Deus, todos os dias.
24 Quando o caminho te for comprido demais, que os não possas levar, por estar longe de ti o lugar que o Senhor, teu Deus, escolher para ali pôr o seu nome, quando o Senhor, teu Deus, te tiver abençoado,
25 então, vende-os, e leva o dinheiro na tua mão, e vai ao lugar que o Senhor, teu Deus, escolher.
26 Esse dinheiro, dá-lo-ás por tudo o que deseja a tua alma, por vacas, ou ovelhas, ou vinho, ou bebida forte, ou qualquer coisa que te pedir a tua alma; come-o ali perante o Senhor, teu Deus, e te alegrarás, tu e a tua casa;
27 porém não desampararás o levita que está dentro da tua cidade, pois não tem parte nem herança contigo.
28 Ao fim de cada três anos, tirarás todos os dízimos do fruto do terceiro ano e os recolherás na tua cidade.
29 Então, virão o levita (pois não tem parte nem herança contigo), o estrangeiro, o órfão e a viúva que estão dentro da tua cidade, e comerão, e se fartarão, para que o Senhor, teu Deus, te abençoe em todas as obras que as tuas mãos fizerem.*
1 Ao fim de cada sete anos, farás remissão.
2 Este, pois, é o modo da remissão: todo credor que emprestou ao seu próximo alguma coisa remitirá o que havia emprestado; não o exigirá do seu próximo ou do seu irmão, pois a remissão do Senhor é proclamada.
3 Do estranho podes exigi-lo, mas o que tiveres em poder de teu irmão, quitá-lo-ás;
4 para que entre ti não haja pobre; pois o Senhor, teu Deus, te abençoará abundantemente na terra que te dá por herança, para a possuíres,
5 se apenas ouvires, atentamente, a voz do Senhor, teu Deus, para cuidares em cumprir todos estes mandamentos que hoje te ordeno.
6 Pois o Senhor, teu Deus, te abençoará, como te tem dito; assim, emprestarás a muitas nações, mas não tomarás empréstimos; e dominarás muitas nações, porém elas não te dominarão.
7 Quando entre ti houver algum pobre de teus irmãos, em alguma das tuas cidades, na tua terra que o Senhor, teu Deus, te dá, não endurecerás o teu coração, nem fecharás as mãos a teu irmão pobre;
8 antes, lhe abrirás de todo a mão e lhe emprestarás o que lhe falta, quanto baste para a sua necessidade.
9 Guarda-te não haja pensamento vil no teu coração, nem digas: Está próximo o sétimo ano, o ano da remissão, de sorte que os teus olhos sejam malignos para com teu irmão pobre, e não lhe dês nada, e ele clame contra ti ao Senhor, e haja em ti pecado.
10 Livremente, lhe darás, e não seja maligno o teu coração, quando lho deres; pois, por isso, te abençoará o Senhor, teu Deus, em toda a tua obra e em tudo o que empreenderes.
11 Pois nunca deixará de haver pobres na terra; por isso, eu te ordeno: livremente, abrirás a mão para o teu irmão, para o necessitado, para o pobre na tua terra.
12 Quando um de teus irmãos, hebreu ou hebreia, te for vendido, seis anos servir-te-á, mas, no sétimo, o despedirás forro.
13 E, quando de ti o despedires forro, não o deixarás ir vazio.
14 Liberalmente, lhe fornecerás do teu rebanho, da tua eira e do teu lagar; daquilo com que o Senhor, teu Deus, te houver abençoado, lhe darás.
15 Lembrar-te-ás de que foste servo na terra do Egito e de que o Senhor, teu Deus, te remiu; pelo que, hoje, isso te ordeno.
16 Se, porém, ele te disser: Não sairei de ti; porquanto te ama, a ti e a tua casa, por estar bem contigo,
17 então, tomarás uma sovela e lhe furarás a orelha, na porta, e será para sempre teu servo; e também assim farás à tua serva.
18 Não pareça aos teus olhos duro o despedi-lo forro; pois seis anos te serviu por metade do salário do jornaleiro; assim, o Senhor, teu Deus, te abençoará em tudo o que fizeres.
19 Todo primogênito que nascer do teu gado ou de tuas ovelhas, o macho consagrarás ao Senhor, teu Deus; com o primogênito do teu gado não trabalharás, nem tosquiarás o primogênito das tuas ovelhas.
20 Comê-lo-ás perante o Senhor, tu e a tua casa, de ano em ano, no lugar que o Senhor escolher.
21 Porém, havendo nele algum defeito, se for coxo, ou cego, ou tiver outro defeito grave, não o sacrificarás ao Senhor, teu Deus.
22 Na tua cidade, o comerás; o imundo e o limpo o comerão juntamente, como a carne do corço ou do veado.
23 Somente o seu sangue não comerás; sobre a terra o derramarás como água.*
1 Guarda o mês de abibe e celebra a Páscoa do Senhor, teu Deus; porque, no mês de abibe, o Senhor, teu Deus, te tirou do Egito, de noite.
2 Então, sacrificarás como oferta de Páscoa ao Senhor, teu Deus, do rebanho e do gado, no lugar que o Senhor escolher para ali fazer habitar o seu nome.
3 Nela, não comerás levedado; sete dias, nela, comerás pães asmos, pão de aflição (porquanto, apressadamente, saíste da terra do Egito), para que te lembres, todos os dias da tua vida, do dia em que saíste da terra do Egito.
4 Fermento não se achará contigo por sete dias, em todo o teu território; também da carne que sacrificares à tarde, no primeiro dia, nada ficará até pela manhã.
5 Não poderás sacrificar a Páscoa em nenhuma das tuas cidades que te dá o Senhor, teu Deus,
6 senão no lugar que o Senhor, teu Deus, escolher para fazer habitar o seu nome, ali sacrificarás a Páscoa à tarde, ao pôr do sol, ao tempo em que saíste do Egito.
7 Então, a cozerás e comerás no lugar que o Senhor, teu Deus, escolher; sairás pela manhã e voltarás às tuas tendas.
8 Seis dias comerás pães asmos, e, no sétimo dia, é solenidade ao Senhor, teu Deus; nenhuma obra farás.
9 Sete semanas contarás; quando a foice começar na seara, entrarás a contar as sete semanas.
10 E celebrarás a Festa das Semanas ao Senhor, teu Deus, com ofertas voluntárias da tua mão, segundo o Senhor, teu Deus, te houver abençoado.
11 Alegrar-te-ás perante o Senhor, teu Deus, tu, e o teu filho, e a tua filha, e o teu servo, e a tua serva, e o levita que está dentro da tua cidade, e o estrangeiro, e o órfão, e a viúva que estão no meio de ti, no lugar que o Senhor, teu Deus, escolher para ali fazer habitar o seu nome.
12 Lembrar-te-ás de que foste servo no Egito, e guardarás estes estatutos, e os cumprirás.
13 A Festa dos Tabernáculos, celebrá-la-ás por sete dias, quando houveres recolhido da tua eira e do teu lagar.
14 Alegrar-te-ás, na tua festa, tu, e o teu filho, e a tua filha, e o teu servo, e a tua serva, e o levita, e o estrangeiro, e o órfão, e a viúva que estão dentro das tuas cidades.
15 Sete dias celebrarás a festa ao Senhor, teu Deus, no lugar que o Senhor escolher, porque o Senhor, teu Deus, há de abençoar-te em toda a tua colheita e em toda obra das tuas mãos, pelo que de todo te alegrarás.
16 Três vezes no ano, todo varão entre ti aparecerá perante o Senhor, teu Deus, no lugar que escolher, na Festa dos Pães Asmos, e na Festa das Semanas, e na Festa dos Tabernáculos; porém não aparecerá de mãos vazias perante o Senhor;
17 cada um oferecerá na proporção em que possa dar, segundo a bênção que o Senhor, seu Deus, lhe houver concedido.
18 Juízes e oficiais constituirás em todas as tuas cidades que o Senhor, teu Deus, te der entre as tuas tribos, para que julguem o povo com reto juízo.
19 Não torcerás a justiça, não farás acepção de pessoas, nem tomarás suborno; porquanto o suborno cega os olhos dos sábios e subverte a causa dos justos.
20 A justiça seguirás, somente a justiça, para que vivas e possuas em herança a terra que te dá o Senhor, teu Deus.
21 Não estabelecerás poste-ídolo, plantando qualquer árvore junto ao altar do Senhor, teu Deus, que fizeres para ti.
22 Nem levantarás coluna, a qual o Senhor, teu Deus, odeia.*
1 Não sacrificarás ao Senhor, teu Deus, novilho ou ovelha em que haja imperfeição ou algum defeito grave; pois é abominação ao Senhor, teu Deus.
2 Quando no meio de ti, em alguma das tuas cidades que te dá o Senhor, teu Deus, se achar algum homem ou mulher que proceda mal aos olhos do Senhor, teu Deus, transgredindo a sua aliança,
3 que vá, e sirva a outros deuses, e os adore, ou ao sol, ou à lua, ou a todo o exército do céu, o que eu não ordenei;
4 e te seja denunciado, e o ouvires; então, indagarás bem; e eis que, sendo verdade e certo que se fez tal abominação em Israel,
5 então, levarás o homem ou a mulher que fez este malefício às tuas portas e os apedrejarás, até que morram.
6 Por depoimento de duas ou três testemunhas, será morto o que houver de morrer; por depoimento de uma só testemunha, não morrerá.
7 A mão das testemunhas será a primeira contra ele, para matá-lo; e, depois, a mão de todo o povo; assim, eliminarás o mal do meio de ti.
8 Quando alguma coisa te for difícil demais em juízo, entre caso e caso de homicídio, e de demanda e demanda, e de violência e violência, e outras questões de litígio, então, te levantarás e subirás ao lugar que o Senhor, teu Deus, escolher.
9 Virás aos levitas sacerdotes e ao juiz que houver naqueles dias; inquirirás, e te anunciarão a sentença do juízo.
10 E farás segundo o mandado da palavra que te anunciarem do lugar que o Senhor escolher; e terás cuidado de fazer consoante tudo o que te ensinarem.
11 Segundo o mandado da lei que te ensinarem e de acordo com o juízo que te disserem, farás; da sentença que te anunciarem não te desviarás, nem para a direita nem para a esquerda.
12 O homem, pois, que se houver soberbamente, não dando ouvidos ao sacerdote, que está ali para servir ao Senhor, teu Deus, nem ao juiz, esse morrerá; e eliminarás o mal de Israel,
13 para que todo o povo o ouça, tema e jamais se ensoberbeça.
14 Quando entrares na terra que te dá o Senhor, teu Deus, e a possuíres, e nela habitares, e disseres: Estabelecerei sobre mim um rei, como todas as nações que se acham em redor de mim,
15 estabelecerás, com efeito, sobre ti como rei aquele que o Senhor, teu Deus, escolher; homem estranho, que não seja dentre os teus irmãos, não estabelecerás sobre ti, e sim um dentre eles.
16 Porém este não multiplicará para si cavalos, nem fará voltar o povo ao Egito, para multiplicar cavalos; pois o Senhor vos disse: Nunca mais voltareis por este caminho.
17 Tampouco para si multiplicará mulheres, para que o seu coração se não desvie; nem multiplicará muito para si prata ou ouro.
18 Também, quando se assentar no trono do seu reino, escreverá para si um traslado desta lei num livro, do que está diante dos levitas sacerdotes.
19 E o terá consigo e nele lerá todos os dias da sua vida, para que aprenda a temer o Senhor, seu Deus, a fim de guardar todas as palavras desta lei e estes estatutos, para os cumprir.
20 Isto fará para que o seu coração não se eleve sobre os seus irmãos e não se aparte do mandamento, nem para a direita nem para a esquerda; de sorte que prolongue os dias no seu reino, ele e seus filhos no meio de Israel.*
1 Os sacerdotes levitas e toda a tribo de Levi não terão parte nem herança em Israel; das ofertas queimadas ao Senhor e daquilo que lhes é devido comerão.
2 Pelo que não terão herança no meio de seus irmãos; o Senhor é a sua herança, como lhes tem dito.
3 Será este, pois, o direito devido aos sacerdotes, da parte do povo, dos que oferecerem sacrifício, seja gado ou rebanho: que darão ao sacerdote a espádua, e as queixadas, e o bucho.
4 Dar-lhe-ás as primícias do teu cereal, do teu vinho e do teu azeite e as primícias da tosquia das tuas ovelhas.
5 Porque o Senhor, teu Deus, o escolheu de entre todas as tuas tribos para ministrar em o nome do Senhor, ele e seus filhos, todos os dias.
6 Quando vier um levita de alguma das tuas cidades de todo o Israel, onde ele habita, e vier com todo o desejo da sua alma ao lugar que o Senhor escolheu,
7 e ministrar em o nome do Senhor, seu Deus, como também todos os seus irmãos, os levitas, que assistem ali perante o Senhor,
8 porção igual à deles terá para comer, além das vendas do seu patrimônio.
9 Quando entrares na terra que o Senhor, teu Deus, te der, não aprenderás a fazer conforme as abominações daqueles povos.
10 Não se achará entre ti quem faça passar pelo fogo o seu filho ou a sua filha, nem adivinhador, nem prognosticador, nem agoureiro, nem feiticeiro;
11 nem encantador, nem necromante, nem mágico, nem quem consulte os mortos;
12 pois todo aquele que faz tal coisa é abominação ao Senhor; e por estas abominações o Senhor, teu Deus, os lança de diante de ti.
13 Perfeito serás para com o Senhor, teu Deus.
14 Porque estas nações que hás de possuir ouvem os prognosticadores e os adivinhadores; porém a ti o Senhor, teu Deus, não permitiu tal coisa.
15 O Senhor, teu Deus, te suscitará um profeta do meio de ti, de teus irmãos, semelhante a mim; a ele ouvirás,
16 segundo tudo o que pediste ao Senhor, teu Deus, em Horebe, quando reunido o povo: Não ouvirei mais a voz do Senhor, meu Deus, nem mais verei este grande fogo, para que não morra.
17 Então, o Senhor me disse: Falaram bem aquilo que disseram.
18 Suscitar-lhes-ei um profeta do meio de seus irmãos, semelhante a ti, em cuja boca porei as minhas palavras, e ele lhes falará tudo o que eu lhe ordenar.
19 De todo aquele que não ouvir as minhas palavras, que ele falar em meu nome, disso lhe pedirei contas.
20 Porém o profeta que presumir de falar alguma palavra em meu nome, que eu lhe não mandei falar, ou o que falar em nome de outros deuses, esse profeta será morto.
21 Se disseres no teu coração: Como conhecerei a palavra que o Senhor não falou?
22 Sabe que, quando esse profeta falar em nome do Senhor, e a palavra dele se não cumprir, nem suceder, como profetizou, esta é palavra que o Senhor não disse; com soberba, a falou o tal profeta; não tenhas temor dele.*
1 Quando o Senhor, teu Deus, eliminar as nações cuja terra te dará o Senhor, teu Deus, e as desapossares e morares nas suas cidades e nas suas casas,
2 três cidades separarás no meio da tua terra que te dará o Senhor, teu Deus, para a possuíres.
3 Preparar-te-ás o caminho e os limites da tua terra que te fará possuir o Senhor, teu Deus, dividirás em três; e isto será para que nelas se acolha todo homicida.
4 Este é o caso tocante ao homicida que nelas se acolher, para que viva: aquele que, sem o querer, ferir o seu próximo, a quem não aborrecia dantes.
5 Assim, aquele que entrar com o seu próximo no bosque, para cortar lenha, e, manejando com impulso o machado para cortar a árvore, o ferro saltar do cabo e atingir o seu próximo, e este morrer, o tal se acolherá em uma destas cidades e viverá;
6 para que o vingador do sangue não persiga o homicida, quando se lhe enfurecer o coração, e o alcance, por ser comprido o caminho, e lhe tire a vida, porque não é culpado de morte, pois não o aborrecia dantes.
7 Portanto, te ordeno: três cidades separarás.
8 Se o Senhor, teu Deus, dilatar os teus limites, como jurou a teus pais, e te der toda a terra que lhes prometeu,
9 desde que guardes todos estes mandamentos que hoje te ordeno, para cumpri-los, amando o Senhor, teu Deus, e andando nos seus caminhos todos os dias, então, acrescentarás outras três cidades além destas três,
10 para que o sangue inocente se não derrame no meio da tua terra que o Senhor, teu Deus, te dá por herança, pois haveria sangue sobre ti.
11 Mas, havendo alguém que aborrece a seu próximo, e lhe arma ciladas, e se levanta contra ele, e o fere de golpe mortal, e se acolhe em uma dessas cidades,
12 os anciãos da sua cidade enviarão a tirá-lo dali e a entregá-lo na mão do vingador do sangue, para que morra.
13 Não o olharás com piedade; antes, exterminarás de Israel a culpa do sangue inocente, para que te vá bem.
14 Não mudes os marcos do teu próximo, que os antigos fixaram na tua herança, na terra que o Senhor, teu Deus, te dá para a possuíres.
15 Uma só testemunha não se levantará contra alguém por qualquer iniquidade ou por qualquer pecado, seja qual for que cometer; pelo depoimento de duas ou três testemunhas, se estabelecerá o fato.
16 Quando se levantar testemunha falsa contra alguém, para o acusar de algum transvio,
17 então, os dois homens que tiverem a demanda se apresentarão perante o Senhor, diante dos sacerdotes e dos juízes que houver naqueles dias.
18 Os juízes indagarão bem; se a testemunha for falsa e tiver testemunhado falsamente contra seu irmão,
19 far-lhe-eis como cuidou fazer a seu irmão; e, assim, exterminarás o mal do meio de ti;
20 para que os que ficarem o ouçam, e temam, e nunca mais tornem a fazer semelhante mal no meio de ti.
21 Não o olharás com piedade: vida por vida, olho por olho, dente por dente, mão por mão, pé por pé.*
1 Quando saíres à peleja contra os teus inimigos e vires cavalos, e carros, e povo maior em número do que tu, não os temerás; pois o Senhor, teu Deus, que te fez sair da terra do Egito, está contigo.
2 Quando vos achegardes à peleja, o sacerdote se adiantará, e falará ao povo,
3 e dir-lhe-á: Ouvi, ó Israel, hoje, vos achegais à peleja contra os vossos inimigos; que não desfaleça o vosso coração; não tenhais medo, não tremais, nem vos aterrorizeis diante deles,
4 pois o Senhor, vosso Deus, é quem vai convosco a pelejar por vós contra os vossos inimigos, para vos salvar.
5 Os oficiais falarão ao povo, dizendo: Qual o homem que edificou casa nova e ainda não a consagrou? Vá, torne-se para casa, para que não morra na peleja, e outrem a consagre.
6 Qual o homem que plantou uma vinha e ainda não a desfrutou? Vá, torne-se para casa, para que não morra na peleja, e outrem a desfrute.
7 Qual o homem que está desposado com alguma mulher e ainda não a recebeu? Vá, torne-se para casa, para que não morra na peleja, e outro homem a receba.
8 E continuarão os oficiais a falar ao povo, dizendo: Qual o homem medroso e de coração tímido? Vá, torne-se para casa, para que o coração de seus irmãos se não derreta como o seu coração.
9 Quando os oficiais tiverem falado ao povo, designarão os capitães dos exércitos para a dianteira do povo.
10 Quando te aproximares de alguma cidade para pelejar contra ela, oferecer-lhe-ás a paz.
11 Se a sua resposta é de paz, e te abrir as portas, todo o povo que nela se achar será sujeito a trabalhos forçados e te servirá.
12 Porém, se ela não fizer paz contigo, mas te fizer guerra, então, a sitiarás.
13 E o Senhor, teu Deus, a dará na tua mão; e todos os do sexo masculino que houver nela passarás a fio de espada;
14 mas as mulheres, e as crianças, e os animais, e tudo o que houver na cidade, todo o seu despojo, tomarás para ti; e desfrutarás o despojo dos inimigos que o Senhor, teu Deus, te deu.
15 Assim farás a todas as cidades que estiverem mui longe de ti, que não forem das cidades destes povos.
16 Porém, das cidades destas nações que o Senhor, teu Deus, te dá em herança, não deixarás com vida tudo o que tem fôlego.
17 Antes, como te ordenou o Senhor, teu Deus, destruí-las-ás totalmente: os heteus, os amorreus, os cananeus, os ferezeus, os heveus e os jebuseus,
18 para que não vos ensinem a fazer segundo todas as suas abominações, que fizeram a seus deuses, pois pecaríeis contra o Senhor, vosso Deus.
19 Quando sitiares uma cidade por muito tempo, pelejando contra ela para a tomar, não destruirás o seu arvoredo, metendo nele o machado, porque dele comerás; pelo que não o cortarás, pois será a árvore do campo algum homem, para que fosse sitiada por ti?
20 Mas as árvores cujos frutos souberes não se comem, destruí-las-ás, cortando-as; e, contra a cidade que guerrear contra ti, edificarás baluartes, até que seja derribada.*
1 Quando na terra que te der o Senhor, teu Deus, para possuí-la se achar alguém morto, caído no campo, sem que se saiba quem o matou,
2 sairão os teus anciãos e os teus juízes e medirão a distância até às cidades que estiverem em redor do morto.
3 Os anciãos da cidade mais próxima do morto tomarão uma novilha da manada, que não tenha trabalhado, nem puxado com o jugo,
4 e a trarão a um vale de águas correntes, que não foi lavrado, nem semeado; e ali, naquele vale, desnucarão a novilha.
5 Chegar-se-ão os sacerdotes, filhos de Levi, porque o Senhor, teu Deus, os escolheu para o servirem, para abençoarem em nome do Senhor e, por sua palavra, decidirem toda demanda e todo caso de violência.
6 Todos os anciãos desta cidade, mais próximos do morto, lavarão as mãos sobre a novilha desnucada no vale
7 e dirão: As nossas mãos não derramaram este sangue, e os nossos olhos o não viram derramar-se.
8 Sê propício ao teu povo de Israel, que tu, ó Senhor, resgataste, e não ponhas a culpa do sangue inocente no meio do teu povo de Israel. E a culpa daquele sangue lhe será perdoada.
9 Assim, eliminarás a culpa do sangue inocente do meio de ti, pois farás o que é reto aos olhos do Senhor.
10 Quando saíres à peleja contra os teus inimigos, e o Senhor, teu Deus, os entregar nas tuas mãos, e tu deles levares cativos,
11 e vires entre eles uma mulher formosa, e te afeiçoares a ela, e a quiseres tomar por mulher,
12 então, a levarás para casa, e ela rapará a cabeça, e cortará as unhas,
13 e despirá o vestido do seu cativeiro, e ficará na tua casa, e chorará a seu pai e a sua mãe durante um mês. Depois disto, a tomarás; tu serás seu marido, e ela, tua mulher.
14 E, se não te agradares dela, deixá-la-ás ir à sua própria vontade; porém, de nenhuma sorte, a venderás por dinheiro, nem a tratarás mal, pois a tens humilhado.
15 Se um homem tiver duas mulheres, uma a quem ama e outra a quem aborrece, e uma e outra lhe derem filhos, e o primogênito for da aborrecida,
16 no dia em que fizer herdar a seus filhos aquilo que possuir, não poderá dar a primogenitura ao filho da amada, preferindo-o ao filho da aborrecida, que é o primogênito.
17 Mas ao filho da aborrecida reconhecerá por primogênito, dando-lhe dobrada porção de tudo quanto possuir, porquanto aquele é o primogênito do seu vigor; o direito da primogenitura é dele.
18 Se alguém tiver um filho contumaz e rebelde, que não obedece à voz de seu pai e à de sua mãe e, ainda castigado, não lhes dá ouvidos,
19 seu pai e sua mãe o pegarão, e o levarão aos anciãos da cidade, à sua porta,
20 e lhes dirão: Este nosso filho é rebelde e contumaz, não dá ouvidos à nossa voz, é dissoluto e beberrão.
21 Então, todos os homens da sua cidade o apedrejarão até que morra; assim, eliminarás o mal do meio de ti; todo o Israel ouvirá e temerá.
22 Se alguém houver pecado, passível da pena de morte, e tiver sido morto, e o pendurares num madeiro,
23 o seu cadáver não permanecerá no madeiro durante a noite, mas, certamente, o enterrarás no mesmo dia; porquanto o que for pendurado no madeiro é maldito de Deus; assim, não contaminarás a terra que o Senhor, teu Deus, te dá em herança.*
1 Vendo extraviado o boi ou a ovelha de teu irmão, não te furtarás a eles; restituí-los-ás, sem falta, a teu irmão.
2 Se teu irmão não for teu vizinho ou tu o não conheceres, recolhê-los-ás na tua casa, para que fiquem contigo até que teu irmão os busque, e tu lhos restituas.
3 Assim também farás com o seu jumento e assim farás com as suas vestes; o mesmo farás com toda coisa que se perder de teu irmão, e tu achares; não te poderás furtar a ela.
4 O jumento que é de teu irmão ou o seu boi não verás caído no caminho e a eles te furtarás; sem falta o ajudarás a levantá-lo.
5 A mulher não usará roupa de homem, nem o homem, veste peculiar à mulher; porque qualquer que faz tais coisas é abominável ao Senhor, teu Deus.
6 Se de caminho encontrares algum ninho de ave, nalguma árvore ou no chão, com passarinhos, ou ovos, e a mãe sobre os passarinhos ou sobre os ovos, não tomarás a mãe com os filhotes;
7 deixarás ir, livremente, a mãe e os filhotes tomarás para ti, para que te vá bem, e prolongues os teus dias.
8 Quando edificares uma casa nova, far-lhe-ás, no terraço, um parapeito, para que nela não ponhas culpa de sangue, se alguém de algum modo cair dela.
9 Não semearás a tua vinha com duas espécies de semente, para que não degenere o fruto da semente que semeaste e a messe da vinha.
10 Não lavrarás com junta de boi e jumento.
11 Não te vestirás de estofos de lã e linho juntamente.
12 Farás borlas nos quatro cantos do manto com que te cobrires.
13 Se um homem casar com uma mulher, e, depois de coabitar com ela, a aborrecer,
14 e lhe atribuir atos vergonhosos, e contra ela divulgar má fama, dizendo: Casei com esta mulher e me cheguei a ela, porém não a achei virgem,
15 então, o pai da moça e sua mãe tomarão as provas da virgindade da moça e as levarão aos anciãos da cidade, à porta.
16 O pai da moça dirá aos anciãos: Dei minha filha por mulher a este homem; porém ele a aborreceu;
17 e eis que lhe atribuiu atos vergonhosos, dizendo: Não achei virgem a tua filha; todavia, eis aqui as provas da virgindade de minha filha. E estenderão a roupa dela diante dos anciãos da cidade,
18 os quais tomarão o homem, e o açoitarão,
19 e o condenarão a cem siclos de prata, e o darão ao pai da moça, porquanto divulgou má fama sobre uma virgem de Israel. Ela ficará sendo sua mulher, e ele não poderá mandá-la embora durante a sua vida.
20 Porém, se isto for verdade, que se não achou na moça a virgindade,
21 então, a levarão à porta da casa de seu pai, e os homens de sua cidade a apedrejarão até que morra, pois fez loucura em Israel, prostituindo-se na casa de seu pai; assim, eliminarás o mal do meio de ti.
22 Se um homem for achado deitado com uma mulher que tem marido, então, ambos morrerão, o homem que se deitou com a mulher e a mulher; assim, eliminarás o mal de Israel.
23 Se houver moça virgem, desposada, e um homem a achar na cidade e se deitar com ela,
24 então, trareis ambos à porta daquela cidade e os apedrejareis até que morram; a moça, porque não gritou na cidade, e o homem, porque humilhou a mulher do seu próximo; assim, eliminarás o mal do meio de ti.
25 Porém, se algum homem no campo achar moça desposada, e a forçar, e se deitar com ela, então, morrerá só o homem que se deitou com ela;
26 à moça não farás nada; ela não tem culpa de morte, porque, como o homem que se levanta contra o seu próximo e lhe tira a vida, assim também é este caso.
27 Pois a achou no campo; a moça desposada gritou, e não houve quem a livrasse.
28 Se um homem achar moça virgem, que não está desposada, e a pegar, e se deitar com ela, e forem apanhados,
29 então, o homem que se deitou com ela dará ao pai da moça cinquenta siclos de prata; e, uma vez que a humilhou, lhe será por mulher; não poderá mandá-la embora durante a sua vida.
30 Nenhum homem tomará sua madrasta e não profanará o leito de seu pai.
1 Aquele a quem forem trilhados os testículos ou cortado o membro viril não entrará na assembleia do Senhor.
2 Nenhum bastardo entrará na assembleia do Senhor; nem ainda a sua décima geração entrará nela.
3 Nenhum amonita ou moabita entrará na assembleia do Senhor; nem ainda a sua décima geração entrará na assembleia do Senhor, eternamente.
4 Porquanto não foram ao vosso encontro com pão e água, no caminho, quando saíeis do Egito; e porque alugaram contra ti Balaão, filho de Beor, de Petor, da Mesopotâmia, para te amaldiçoar.
5 Porém o Senhor, teu Deus, não quis ouvir a Balaão; antes, trocou em bênção a maldição, porquanto o Senhor, teu Deus, te amava.
6 Não lhes procurarás nem paz nem bem em todos os teus dias, para sempre.
7 Não aborrecerás o edomita, pois é teu irmão; nem aborrecerás o egípcio, pois estrangeiro foste na sua terra.
8 Os filhos que lhes nascerem na terceira geração, cada um deles entrará na assembleia do Senhor.
9 Quando sair o exército contra os teus inimigos, então, te guardarás de toda coisa má.
10 Se houver entre vós alguém que, por motivo de polução noturna, não esteja limpo, sairá do acampamento; não permanecerá nele.
11 Porém, em declinando a tarde, lavar-se-á em água; e, posto o sol, entrará para o meio do acampamento.
12 Também haverá um lugar fora do acampamento, para onde irás.
13 Dentre as tuas armas terás um porrete; e, quando te abaixares fora, cavarás com ele e, volvendo-te, cobrirás o que defecaste.
14 Porquanto o Senhor, teu Deus, anda no meio do teu acampamento para te livrar e para entregar-te os teus inimigos; portanto, o teu acampamento será santo, para que ele não veja em ti coisa indecente e se aparte de ti.
15 Não entregarás ao seu senhor o escravo que, tendo fugido dele, se acolher a ti.
16 Contigo ficará, no meio de ti, no lugar que escolher, em alguma de tuas cidades onde lhe agradar; não o oprimirás.
17 Das filhas de Israel não haverá quem se prostitua no serviço do templo, nem dos filhos de Israel haverá quem o faça.
18 Não trarás salário de prostituição nem preço de sodomita à Casa do Senhor, teu Deus, por qualquer voto; porque uma e outra coisa são igualmente abomináveis ao Senhor, teu Deus.
19 A teu irmão não emprestarás com juros, seja dinheiro, seja comida ou qualquer coisa que é costume se emprestar com juros.
20 Ao estrangeiro emprestarás com juros, porém a teu irmão não emprestarás com juros, para que o Senhor, teu Deus, te abençoe em todos os teus empreendimentos na terra a qual passas a possuir.
21 Quando fizeres algum voto ao Senhor, teu Deus, não tardarás em cumpri-lo; porque o Senhor, teu Deus, certamente, o requererá de ti, e em ti haverá pecado.
22 Porém, abstendo-te de fazer o voto, não haverá pecado em ti.
23 O que proferiram os teus lábios, isso guardarás e o farás, porque votaste livremente ao Senhor, teu Deus, o que falaste com a tua boca.
24 Quando entrares na vinha do teu próximo, comerás uvas segundo o teu desejo, até te fartares, porém não as levarás no cesto.
25 Quando entrares na seara do teu próximo, com as mãos arrancarás as espigas; porém na seara não meterás a foice.*
1 Se um homem tomar uma mulher e se casar com ela, e se ela não for agradável aos seus olhos, por ter ele achado coisa indecente nela, e se ele lhe lavrar um termo de divórcio, e lho der na mão, e a despedir de casa;
2 e se ela, saindo da sua casa, for e se casar com outro homem;
3 e se este a aborrecer, e lhe lavrar termo de divórcio, e lho der na mão, e a despedir da sua casa ou se este último homem, que a tomou para si por mulher, vier a morrer,
4 então, seu primeiro marido, que a despediu, não poderá tornar a desposá-la para que seja sua mulher, depois que foi contaminada, pois é abominação perante o Senhor; assim, não farás pecar a terra que o Senhor, teu Deus, te dá por herança.
5 Homem recém-casado não sairá à guerra, nem se lhe imporá qualquer encargo; por um ano ficará livre em casa e promoverá felicidade à mulher que tomou.
6 Não se tomarão em penhor as duas mós, nem apenas a de cima, pois se penhoraria, assim, a vida.
7 Se se achar alguém que, tendo roubado um dentre os seus irmãos, dos filhos de Israel, o trata como escravo ou o vende, esse ladrão morrerá. Assim, eliminarás o mal do meio de ti.
8 Guarda-te da praga da lepra e tem diligente cuidado de fazer segundo tudo o que te ensinarem os sacerdotes levitas; como lhes tenho ordenado, terás cuidado de o fazer.
9 Lembra-te do que o Senhor, teu Deus, fez a Miriã no caminho, quando saíste do Egito.
10 Se emprestares alguma coisa ao teu próximo, não entrarás em sua casa para lhe tirar o penhor.
11 Ficarás do lado de fora, e o homem, a quem emprestaste, aí te trará o penhor.
12 Porém, se for homem pobre, não usarás de noite o seu penhor;
13 em se pondo o sol, restituir-lhe-ás, sem falta, o penhor para que durma no seu manto e te abençoe; isto te será justiça diante do Senhor, teu Deus.
14 Não oprimirás o jornaleiro pobre e necessitado, seja ele teu irmão ou estrangeiro que está na tua terra e na tua cidade.
15 No seu dia, lhe darás o seu salário, antes do pôr do sol, porquanto é pobre, e disso depende a sua vida; para que não clame contra ti ao Senhor, e haja em ti pecado.
16 Os pais não serão mortos em lugar dos filhos, nem os filhos, em lugar dos pais; cada qual será morto pelo seu pecado.
17 Não perverterás o direito do estrangeiro e do órfão; nem tomarás em penhor a roupa da viúva.
18 Lembrar-te-ás de que foste escravo no Egito e de que o Senhor te livrou dali; pelo que te ordeno que faças isso.
19 Quando, no teu campo, segares a messe e, nele, esqueceres um feixe de espigas, não voltarás a tomá-lo; para o estrangeiro, para o órfão e para a viúva será; para que o Senhor, teu Deus, te abençoe em toda obra das tuas mãos.
20 Quando sacudires a tua oliveira, não voltarás a colher o fruto dos ramos; para o estrangeiro, para o órfão e para a viúva será.
21 Quando vindimares a tua vinha, não tornarás a rebuscá-la; para o estrangeiro, para o órfão e para a viúva será o restante.
22 Lembrar-te-ás de que foste escravo na terra do Egito; pelo que te ordeno que faças isso.*
1 Em havendo contenda entre alguns, e vierem a juízo, os juízes os julgarão, justificando ao justo e condenando ao culpado.
2 Se o culpado merecer açoites, o juiz o fará deitar-se e o fará açoitar, na sua presença, com o número de açoites segundo a sua culpa.
3 Quarenta açoites lhe fará dar, não mais; para que, porventura, se lhe fizer dar mais do que estes, teu irmão não fique aviltado aos teus olhos.
4 Não atarás a boca ao boi quando debulha.
5 Se irmãos morarem juntos, e um deles morrer sem filhos, então, a mulher do que morreu não se casará com outro estranho, fora da família; seu cunhado a tomará, e a receberá por mulher, e exercerá para com ela a obrigação de cunhado.
6 O primogênito que ela lhe der será sucessor do nome do seu irmão falecido, para que o nome deste não se apague em Israel.
7 Porém, se o homem não quiser tomar sua cunhada, subirá esta à porta, aos anciãos, e dirá: Meu cunhado recusa suscitar a seu irmão nome em Israel; não quer exercer para comigo a obrigação de cunhado.
8 Então, os anciãos da sua cidade devem chamá-lo e falar-lhe; e, se ele persistir e disser: Não quero tomá-la,
9 então, sua cunhada se chegará a ele na presença dos anciãos, e lhe descalçará a sandália do pé, e lhe cuspirá no rosto, e protestará, e dirá: Assim se fará ao homem que não quer edificar a casa de seu irmão;
10 e o nome de sua casa se chamará em Israel: A casa do descalçado.
11 Quando brigarem dois homens, um contra o outro, e a mulher de um chegar para livrar o marido da mão do que o fere, e ela estender a mão, e o pegar pelas suas vergonhas,
12 cortar-lhe-ás a mão; não a olharás com piedade.
13 Na tua bolsa, não terás pesos diversos, um grande e um pequeno.
14 Na tua casa, não terás duas sortes de efa, um grande e um pequeno.
15 Terás peso integral e justo, efa integral e justo; para que se prolonguem os teus dias na terra que te dá o Senhor, teu Deus.
16 Porque é abominação ao Senhor, teu Deus, todo aquele que pratica tal injustiça.
17 Lembra-te do que te fez Amaleque no caminho, quando saías do Egito;
18 como te veio ao encontro no caminho e te atacou na retaguarda todos os desfalecidos que iam após ti, quando estavas abatido e afadigado; e não temeu a Deus.
19 Quando, pois, o Senhor, teu Deus, te houver dado sossego de todos os teus inimigos em redor, na terra que o Senhor, teu Deus, te dá por herança, para a possuíres, apagarás a memória de Amaleque de debaixo do céu; não te esqueças.*
1 Ao entrares na terra que o Senhor, teu Deus, te dá por herança, ao possuí-la e nela habitares,
2 tomarás das primícias de todos os frutos do solo que recolheres da terra que te dá o Senhor, teu Deus, e as porás num cesto, e irás ao lugar que o Senhor, teu Deus, escolher para ali fazer habitar o seu nome.
3 Virás ao que, naqueles dias, for sacerdote e lhe dirás: Hoje, declaro ao Senhor, teu Deus, que entrei na terra que o Senhor, sob juramento, prometeu dar a nossos pais.
4 O sacerdote tomará o cesto da tua mão e o porá diante do altar do Senhor, teu Deus.
5 Então, testificarás perante o Senhor, teu Deus, e dirás: Arameu prestes a perecer foi meu pai, e desceu para o Egito, e ali viveu como estrangeiro com pouca gente; e ali veio a ser nação grande, forte e numerosa.
6 Mas os egípcios nos maltrataram, e afligiram, e nos impuseram dura servidão.
7 Clamamos ao Senhor, Deus de nossos pais; e o Senhor ouviu a nossa voz e atentou para a nossa angústia, para o nosso trabalho e para a nossa opressão;
8 e o Senhor nos tirou do Egito com poderosa mão, e com braço estendido, e com grande espanto, e com sinais, e com milagres;
9 e nos trouxe a este lugar e nos deu esta terra, terra que mana leite e mel.
10 Eis que, agora, trago as primícias dos frutos da terra que tu, ó Senhor, me deste. Então, as porás perante o Senhor, teu Deus, e te prostrarás perante ele.
11 Alegrar-te-ás por todo o bem que o Senhor, teu Deus, te tem dado a ti e a tua casa, tu, e o levita, e o estrangeiro que está no meio de ti.
12 Quando acabares de separar todos os dízimos da tua messe no ano terceiro, que é o dos dízimos, então, os darás ao levita, ao estrangeiro, ao órfão e à viúva, para que comam dentro das tuas cidades e se fartem.
13 Dirás perante o Senhor, teu Deus: Tirei de minha casa o que é consagrado e dei também ao levita, e ao estrangeiro, e ao órfão, e à viúva, segundo todos os teus mandamentos que me tens ordenado; nada transgredi dos teus mandamentos, nem deles me esqueci.
14 Dos dízimos não comi no meu luto e deles nada tirei estando imundo, nem deles dei para a casa de algum morto; obedeci à voz do Senhor, meu Deus; segundo tudo o que me ordenaste, tenho feito.
15 Olha desde a tua santa habitação, desde o céu, e abençoa o teu povo, a Israel, e a terra que nos deste, como juraste a nossos pais, terra que mana leite e mel.
16 Hoje, o Senhor, teu Deus, te manda cumprir estes estatutos e juízos; guarda-os, pois, e cumpre-os de todo o teu coração e de toda a tua alma.
17 Hoje, fizeste o Senhor declarar que te será por Deus, e que andarás nos seus caminhos, e guardarás os seus estatutos, e os seus mandamentos, e os seus juízos, e darás ouvidos à sua voz.
18 E o Senhor, hoje, te fez dizer que lhe serás por povo seu próprio, como te disse, e que guardarás todos os seus mandamentos.
19 Para, assim, te exaltar em louvor, renome e glória sobre todas as nações que fez e para que sejas povo santo ao Senhor, teu Deus, como tem dito.*
1 Moisés e os anciãos de Israel deram ordem ao povo, dizendo: Guarda todos estes mandamentos que, hoje, te ordeno.
2 No dia em que passares o Jordão à terra que te der o Senhor, teu Deus, levantar-te-ás pedras grandes e as caiarás.
3 Havendo-o passado, escreverás, nelas, todas as palavras desta lei, para entrares na terra que te dá o Senhor, teu Deus, terra que mana leite e mel, como te prometeu o Senhor, Deus de teus pais.
4 Quando houveres passado o Jordão, levantarás estas pedras, que hoje te ordeno, no monte Ebal, e as caiarás.
5 Ali, edificarás um altar ao Senhor, teu Deus, altar de pedras, sobre as quais não manejarás instrumento de ferro.
6 De pedras toscas edificarás o altar do Senhor, teu Deus; e sobre ele lhe oferecerás holocaustos.
7 Também sacrificarás ofertas pacíficas; ali, comerás e te alegrarás perante o Senhor, teu Deus.
8 Nestas pedras, escreverás, mui distintamente, as palavras todas desta lei.
9 Falou mais Moisés, juntamente com os sacerdotes levitas, a todo o Israel, dizendo: Guarda silêncio e ouve, ó Israel! Hoje, vieste a ser povo do Senhor, teu Deus.
10 Portanto, obedecerás à voz do Senhor, teu Deus, e lhe cumprirás os mandamentos e os estatutos que hoje te ordeno.
11 Moisés deu ordem, naquele dia, ao povo, dizendo:
12 Quando houveres passado o Jordão, estarão sobre o monte Gerizim, para abençoarem o povo, estes: Simeão, Levi, Judá, Issacar, José e Benjamim.
13 E estes, para amaldiçoar, estarão sobre o monte Ebal: Rúben, Gade, Aser, Zebulom, Dã e Naftali.
14 Os levitas testificarão a todo o povo de Israel em alta voz e dirão:
15 Maldito o homem que fizer imagem de escultura ou de fundição, abominável ao Senhor, obra de artífice, e a puser em lugar oculto. E todo o povo responderá: Amém!
16 Maldito aquele que desprezar a seu pai ou a sua mãe. E todo o povo dirá: Amém!
17 Maldito aquele que mudar os marcos do seu próximo. E todo o povo dirá: Amém!
18 Maldito aquele que fizer o cego errar o caminho. E todo o povo dirá: Amém!
19 Maldito aquele que perverter o direito do estrangeiro, do órfão e da viúva. E todo o povo dirá: Amém!
20 Maldito aquele que se deitar com a madrasta, porquanto profanaria o leito de seu pai. E todo o povo dirá: Amém!
21 Maldito aquele que se ajuntar com animal. E todo o povo dirá: Amém!
22 Maldito aquele que se deitar com sua irmã, filha de seu pai ou filha de sua mãe. E todo o povo dirá: Amém!
23 Maldito aquele que se deitar com sua sogra. E todo o povo dirá: Amém!
24 Maldito aquele que ferir o seu próximo em oculto. E todo o povo dirá: Amém!
25 Maldito aquele que aceitar suborno para matar pessoa inocente. E todo o povo dirá: Amém!
26 Maldito aquele que não confirmar as palavras desta lei, não as cumprindo. E todo o povo dirá: Amém!*
1 Se atentamente ouvires a voz do Senhor, teu Deus, tendo cuidado de guardar todos os seus mandamentos que hoje te ordeno, o Senhor, teu Deus, te exaltará sobre todas as nações da terra.
2 Se ouvires a voz do Senhor, teu Deus, virão sobre ti e te alcançarão todas estas bênçãos:
3 Bendito serás tu na cidade e bendito serás no campo.
4 Bendito o fruto do teu ventre, e o fruto da tua terra, e o fruto dos teus animais, e as crias das tuas vacas e das tuas ovelhas.
5 Bendito o teu cesto e a tua amassadeira.
6 Bendito serás ao entrares e bendito, ao saíres.
7 O Senhor fará que sejam derrotados na tua presença os inimigos que se levantarem contra ti; por um caminho, sairão contra ti, mas, por sete caminhos, fugirão da tua presença.
8 O Senhor determinará que a bênção esteja nos teus celeiros e em tudo o que colocares a mão; e te abençoará na terra que te dá o Senhor, teu Deus.
9 O Senhor te constituirá para si em povo santo, como te tem jurado, quando guardares os mandamentos do Senhor, teu Deus, e andares nos seus caminhos.
10 E todos os povos da terra verão que és chamado pelo nome do Senhor e terão medo de ti.
11 O Senhor te dará abundância de bens no fruto do teu ventre, no fruto dos teus animais e no fruto do teu solo, na terra que o Senhor, sob juramento a teus pais, prometeu dar-te.
12 O Senhor te abrirá o seu bom tesouro, o céu, para dar chuva à tua terra no seu tempo e para abençoar toda obra das tuas mãos; emprestarás a muitas gentes, porém tu não tomarás emprestado.
13 O Senhor te porá por cabeça e não por cauda; e só estarás em cima e não debaixo, se obedeceres aos mandamentos do Senhor, teu Deus, que hoje te ordeno, para os guardar e cumprir.
14 Não te desviarás de todas as palavras que hoje te ordeno, nem para a direita nem para a esquerda, seguindo outros deuses, para os servires.
15 Será, porém, que, se não deres ouvidos à voz do Senhor, teu Deus, não cuidando em cumprir todos os seus mandamentos e os seus estatutos que, hoje, te ordeno, então, virão todas estas maldições sobre ti e te alcançarão:
16 Maldito serás tu na cidade e maldito serás no campo.
17 Maldito o teu cesto e a tua amassadeira.
18 Maldito o fruto do teu ventre, e o fruto da tua terra, e as crias das tuas vacas e das tuas ovelhas.
19 Maldito serás ao entrares e maldito, ao saíres.
20 O Senhor mandará sobre ti a maldição, a confusão e a ameaça em tudo quanto empreenderes, até que sejas destruído e repentinamente pereças, por causa da maldade das tuas obras, com que me abandonaste.
21 O Senhor fará que a pestilência te pegue a ti, até que te consuma a terra a que passas para possuí-la.
22 O Senhor te ferirá com a tísica, e a febre, e a inflamação, e com o calor ardente, e a secura, e com o crestamento, e a ferrugem; e isto te perseguirá até que pereças.
23 Os teus céus sobre a tua cabeça serão de bronze; e a terra debaixo de ti será de ferro.
24 Por chuva da tua terra, o Senhor te dará pó e cinza; dos céus, descerá sobre ti, até que sejas destruído.
25 O Senhor te fará cair diante dos teus inimigos; por um caminho, sairás contra eles, e, por sete caminhos, fugirás diante deles, e serás motivo de horror para todos os reinos da terra.
26 O teu cadáver servirá de pasto a todas as aves dos céus e aos animais da terra; e ninguém haverá que os espante.
27 O Senhor te ferirá com as úlceras do Egito, com tumores, com sarna e com prurido de que não possas curar-te.
28 O Senhor te ferirá com loucura, com cegueira e com perturbação do espírito.
29 Apalparás ao meio-dia, como o cego apalpa nas trevas, e não prosperarás nos teus caminhos; porém somente serás oprimido e roubado todos os teus dias; e ninguém haverá que te salve.
30 Desposar-te-ás com uma mulher, porém outro homem dormirá com ela; edificarás casa, porém não morarás nela; plantarás vinha, porém não a desfrutarás.
31 O teu boi será morto aos teus olhos, porém dele não comerás; o teu jumento será roubado diante de ti e não voltará a ti; as tuas ovelhas serão dadas aos teus inimigos; e ninguém haverá que te salve.
32 Teus filhos e tuas filhas serão dados a outro povo; os teus olhos o verão e desfalecerão de saudades todo o dia; porém a tua mão nada poderá fazer.
33 O fruto da tua terra e todo o teu trabalho, comê-los-á um povo que nunca conheceste; e tu serás oprimido e quebrantado todos os dias;
34 e te enlouquecerás pelo que vires com os teus olhos.
35 O Senhor te ferirá com úlceras malignas nos joelhos e nas pernas, das quais não te possas curar, desde a planta do pé até ao alto da cabeça.
36 O Senhor te levará e o teu rei que tiveres constituído sobre ti a uma gente que não conheceste, nem tu, nem teus pais; e ali servirás a outros deuses, feitos de madeira e de pedra.
37 Virás a ser pasmo, provérbio e motejo entre todos os povos a que o Senhor te levará.
38 Lançarás muita semente ao campo; porém colherás pouco, porque o gafanhoto a consumirá.
39 Plantarás e cultivarás muitas vinhas, porém do seu vinho não beberás, nem colherás as uvas, porque o verme as devorará.
40 Em todos os teus limites terás oliveiras; porém não te ungirás com azeite, porque as tuas azeitonas cairão.
41 Gerarás filhos e filhas, porém não ficarão contigo, porque serão levados ao cativeiro.
42 Todo o teu arvoredo e o fruto da tua terra o gafanhoto os consumirá.
43 O estrangeiro que está no meio de ti se elevará mais e mais, e tu mais e mais descerás.
44 Ele te emprestará a ti, porém tu não lhe emprestarás a ele; ele será por cabeça, e tu serás por cauda.
45 Todas estas maldições virão sobre ti, e te perseguirão, e te alcançarão, até que sejas destruído, porquanto não ouviste a voz do Senhor, teu Deus, para guardares os mandamentos e os estatutos que te ordenou.
46 Serão, no teu meio, por sinal e por maravilha, como também entre a tua descendência, para sempre.
47 Porquanto não serviste ao Senhor, teu Deus, com alegria e bondade de coração, não obstante a abundância de tudo.
48 Assim, com fome, com sede, com nudez e com falta de tudo, servirás aos inimigos que o Senhor enviará contra ti; sobre o teu pescoço porá um jugo de ferro, até que te haja destruído.
49 O Senhor levantará contra ti uma nação de longe, da extremidade da terra virá, como o voo impetuoso da águia, nação cuja língua não entenderás;
50 nação feroz de rosto, que não respeitará ao velho, nem se apiedará do moço.
51 Ela comerá o fruto dos teus animais e o fruto da tua terra, até que sejas destruído; e não te deixará cereal, mosto, nem azeite, nem as crias das tuas vacas e das tuas ovelhas, até que te haja consumido.
52 Sitiar-te-á em todas as tuas cidades, até que venham a cair, em toda a tua terra, os altos e fortes muros em que confiavas; e te sitiará em todas as tuas cidades, em toda a terra que o Senhor, teu Deus, te deu.
53 Comerás o fruto do teu ventre, a carne de teus filhos e de tuas filhas, que te der o Senhor, teu Deus, na angústia e no aperto com que os teus inimigos te apertarão.
54 O mais mimoso dos homens e o mais delicado do teu meio será mesquinho para com seu irmão, e para com a mulher do seu amor, e para com os demais de seus filhos que ainda lhe restarem;
55 de sorte que não dará a nenhum deles da carne de seus filhos, que ele comer; porquanto nada lhe ficou de resto na angústia e no aperto com que o teu inimigo te apertará em todas as tuas cidades.
56 A mais mimosa das mulheres e a mais delicada do teu meio, que de mimo e delicadeza não tentaria pôr a planta do pé sobre a terra, será mesquinha para com o marido de seu amor, e para com seu filho, e para com sua filha;
57 mesquinha da placenta que lhe saiu dentre os pés e dos filhos que tiver, porque os comerá às escondidas pela falta de tudo, na angústia e no aperto com que o teu inimigo te apertará nas tuas cidades.
58 Se não tiveres cuidado de guardar todas as palavras desta lei, escritas neste livro, para temeres este nome glorioso e terrível, o Senhor, teu Deus,
59 então, o Senhor fará terríveis as tuas pragas e as pragas de tua descendência, grandes e duradouras pragas, e enfermidades graves e duradouras;
60 fará voltar contra ti todas as moléstias do Egito, que temeste; e se apegarão a ti.
61 Também o Senhor fará vir sobre ti toda enfermidade e toda praga que não estão escritas no livro desta Lei, até que sejas destruído.
62 Ficareis poucos em número, vós que éreis como as estrelas dos céus em multidão, porque não destes ouvidos à voz do Senhor, vosso Deus.
63 Assim como o Senhor se alegrava em vós outros, em fazer-vos bem e multiplicar-vos, da mesma sorte o Senhor se alegrará em vos fazer perecer e vos destruir; sereis desarraigados da terra à qual passais para possuí-la.
64 O Senhor vos espalhará entre todos os povos, de uma até à outra extremidade da terra. Servirás ali a outros deuses que não conheceste, nem tu, nem teus pais; servirás à madeira e à pedra.
65 Nem ainda entre estas nações descansarás, nem a planta de teu pé terá repouso, porquanto o Senhor ali te dará coração tremente, olhos mortiços e desmaio de alma.
66 A tua vida estará suspensa como por um fio diante de ti; terás pavor de noite e de dia e não crerás na tua vida.
67 Pela manhã dirás: Ah! Quem me dera ver a noite! E, à noitinha, dirás: Ah! Quem me dera ver a manhã! Isso pelo pavor que sentirás no coração e pelo espetáculo que terás diante dos olhos.
68 O Senhor te fará voltar ao Egito em navios, pelo caminho de que te disse: Nunca jamais o verás; sereis ali oferecidos para venda como escravos e escravas aos vossos inimigos, mas não haverá quem vos compre.*
1 São estas as palavras da aliança que o Senhor ordenou a Moisés fizesse com os filhos de Israel na terra de Moabe, além da aliança que fizera com eles em Horebe.
2 Chamou Moisés a todo o Israel e disse-lhe: Tendes visto tudo quanto o Senhor fez na terra do Egito, perante vós, a Faraó, e a todos os seus servos, e a toda a sua terra;
3 as grandes provas que os vossos olhos viram, os sinais e grandes maravilhas;
4 porém o Senhor não vos deu coração para entender, nem olhos para ver, nem ouvidos para ouvir, até ao dia de hoje.
5 Quarenta anos vos conduzi pelo deserto; não envelheceram sobre vós as vossas vestes, nem se gastou no vosso pé a sandália.
6 Pão não comestes e não bebestes vinho nem bebida forte, para que soubésseis que eu sou o Senhor, vosso Deus.
7 Quando viestes a este lugar, Seom, rei de Hesbom, e Ogue, rei de Basã, nos saíram ao encontro, à peleja, e nós os ferimos;
8 tomamos-lhes a terra e a demos por herança aos rubenitas, e aos gaditas, e à meia tribo dos manassitas.
9 Guardai, pois, as palavras desta aliança e cumpri-as, para que prospereis em tudo quanto fizerdes.
10 Vós estais, hoje, todos perante o Senhor, vosso Deus: os cabeças de vossas tribos, vossos anciãos e os vossos oficiais, todos os homens de Israel,
11 os vossos meninos, as vossas mulheres e o estrangeiro que está no meio do vosso arraial, desde o vosso rachador de lenha até ao vosso tirador de água,
12 para que entres na aliança do Senhor, teu Deus, e no juramento que, hoje, o Senhor, teu Deus, faz contigo;
13 para que, hoje, te estabeleça por seu povo, e ele te seja por Deus, como te tem prometido, como jurou a teus pais, Abraão, Isaque e Jacó.
14 Não é somente convosco que faço esta aliança e este juramento,
15 porém com aquele que, hoje, aqui, está conosco perante o Senhor, nosso Deus, e também com aquele que não está aqui, hoje, conosco.
16 Porque vós sabeis como habitamos na terra do Egito e como passamos pelo meio das nações pelas quais viestes a passar;
17 vistes as suas abominações e os seus ídolos, feitos de madeira e de pedra, bem como vistes a prata e o ouro que havia entre elas;
18 para que, entre vós, não haja homem, nem mulher, nem família, nem tribo cujo coração, hoje, se desvie do Senhor, nosso Deus, e vá servir aos deuses destas nações; para que não haja entre vós raiz que produza erva venenosa e amarga,
19 ninguém que, ouvindo as palavras desta maldição, se abençoe no seu íntimo, dizendo: Terei paz, ainda que ande na perversidade do meu coração, para acrescentar à sede a bebedice.
20 O Senhor não lhe quererá perdoar; antes, fumegará a ira do Senhor e o seu zelo sobre tal homem, e toda maldição escrita neste livro jazerá sobre ele; e o Senhor lhe apagará o nome de debaixo do céu.
21 O Senhor o separará de todas as tribos de Israel para calamidade, segundo todas as maldições da aliança escrita neste Livro da Lei.
22 Então, dirá a geração vindoura, os vossos filhos, que se levantarem depois de vós, e o estrangeiro que virá de terras longínquas, vendo as pragas desta terra e as suas doenças, com que o Senhor a terá afligido,
23 e toda a sua terra abrasada com enxofre e sal, de sorte que não será semeada, e nada produzirá, nem crescerá nela erva alguma, assim como foi a destruição de Sodoma e de Gomorra, de Admá e de Zeboim, que o Senhor destruiu na sua ira e no seu furor,
24 isto é, todas as nações dirão: Por que fez o Senhor assim com esta terra? Qual foi a causa do furor de tamanha ira?
25 Então, se dirá: Porque desprezaram a aliança que o Senhor, Deus de seus pais, fez com eles, quando os tirou do Egito;
26 e se foram, e serviram a outros deuses, e os adoraram; deuses que não conheceram e que ele não lhes havia designado.
27 Pelo que a ira do Senhor se acendeu contra esta terra, trazendo sobre ela toda a maldição que está escrita neste livro.
28 O Senhor os arrancou, com ira, de sua terra, mas também com indignação e grande furor, e os lançou para outra terra, como hoje se vê.
29 As coisas encobertas pertencem ao Senhor, nosso Deus, porém as reveladas nos pertencem, a nós e a nossos filhos, para sempre, para que cumpramos todas as palavras desta lei.*
1 Quando, pois, todas estas coisas vierem sobre ti, a bênção e a maldição que pus diante de ti, se te recordares delas entre todas as nações para onde te lançar o Senhor, teu Deus;
2 e tornares ao Senhor, teu Deus, tu e teus filhos, de todo o teu coração e de toda a tua alma, e deres ouvidos à sua voz, segundo tudo o que hoje te ordeno,
3 então, o Senhor, teu Deus, mudará a tua sorte, e se compadecerá de ti, e te ajuntará, de novo, de todos os povos entre os quais te havia espalhado o Senhor, teu Deus.
4 Ainda que os teus desterrados estejam para a extremidade dos céus, desde aí te ajuntará o Senhor, teu Deus, e te tomará de lá.
5 O Senhor, teu Deus, te introduzirá na terra que teus pais possuíram, e a possuirás; e te fará bem e te multiplicará mais do que a teus pais.
6 O Senhor, teu Deus, circuncidará o teu coração e o coração de tua descendência, para amares o Senhor, teu Deus, de todo o coração e de toda a tua alma, para que vivas.
7 O Senhor, teu Deus, porá todas estas maldições sobre os teus inimigos e sobre os teus aborrecedores, que te perseguiram.
8 De novo, pois, darás ouvidos à voz do Senhor; cumprirás todos os seus mandamentos que hoje te ordeno.
9 O Senhor, teu Deus, te dará abundância em toda obra das tuas mãos, no fruto do teu ventre, no fruto dos teus animais e no fruto da tua terra e te beneficiará; porquanto o Senhor tornará a exultar em ti, para te fazer bem, como exultou em teus pais;
10 se deres ouvidos à voz do Senhor, teu Deus, guardando os seus mandamentos e os seus estatutos, escritos neste Livro da Lei, se te converteres ao Senhor, teu Deus, de todo o teu coração e de toda a tua alma.
11 Porque este mandamento que, hoje, te ordeno não é demasiado difícil, nem está longe de ti.
12 Não está nos céus, para dizeres: Quem subirá por nós aos céus, que no-lo traga e no-lo faça ouvir, para que o cumpramos?
13 Nem está além do mar, para dizeres: Quem passará por nós além do mar que no-lo traga e no-lo faça ouvir, para que o cumpramos?
14 Pois esta palavra está mui perto de ti, na tua boca e no teu coração, para a cumprires.
15 Vê que proponho, hoje, a vida e o bem, a morte e o mal;
16 se guardares o mandamento que hoje te ordeno, que ames o Senhor, teu Deus, andes nos seus caminhos, e guardes os seus mandamentos, e os seus estatutos, e os seus juízos, então, viverás e te multiplicarás, e o Senhor, teu Deus, te abençoará na terra à qual passas para possuí-la.
17 Porém, se o teu coração se desviar, e não quiseres dar ouvidos, e fores seduzido, e te inclinares a outros deuses, e os servires,
18 então, hoje, te declaro que, certamente, perecerás; não permanecerás longo tempo na terra à qual vais, passando o Jordão, para a possuíres.
19 Os céus e a terra tomo, hoje, por testemunhas contra ti, que te propus a vida e a morte, a bênção e a maldição; escolhe, pois, a vida, para que vivas, tu e a tua descendência,
20 amando o Senhor, teu Deus, dando ouvidos à sua voz e apegando-te a ele; pois disto depende a tua vida e a tua longevidade; para que habites na terra que o Senhor, sob juramento, prometeu dar a teus pais, Abraão, Isaque e Jacó.*
1 Passou Moisés a falar estas palavras a todo o Israel
2 e disse-lhes: Sou, hoje, da idade de cento e vinte anos. Já não posso sair e entrar, e o Senhor me disse: Não passarás o Jordão.
3 O Senhor, teu Deus, passará adiante de ti; ele destruirá estas nações de diante de ti, e tu as possuirás; Josué passará adiante de ti, como o Senhor tem dito.
4 O Senhor lhes fará como fez a Seom e a Ogue, reis dos amorreus, os quais destruiu, bem como a sua terra.
5 Quando, pois, o Senhor vos entregar estes povos diante de vós, então, com eles fareis segundo todo o mandamento que vos tenho ordenado.
6 Sede fortes e corajosos, não temais, nem vos atemorizeis diante deles, porque o Senhor, vosso Deus, é quem vai convosco; não vos deixará, nem vos desamparará.
7 Chamou Moisés a Josué e lhe disse na presença de todo o Israel: Sê forte e corajoso; porque, com este povo, entrarás na terra que o Senhor, sob juramento, prometeu dar a teus pais; e tu os farás herdá-la.
8 O Senhor é quem vai adiante de ti; ele será contigo, não te deixará, nem te desamparará; não temas, nem te atemorizes.
9 Esta lei, escreveu-a Moisés e a deu aos sacerdotes, filhos de Levi, que levavam a arca da Aliança do Senhor, e a todos os anciãos de Israel.
10 Ordenou-lhes Moisés, dizendo: Ao fim de cada sete anos, precisamente no ano da remissão, na Festa dos Tabernáculos,
11 quando todo o Israel vier a comparecer perante o Senhor, teu Deus, no lugar que este escolher, lerás esta lei diante de todo o Israel.
12 Ajuntai o povo, os homens, as mulheres, os meninos e o estrangeiro que está dentro da vossa cidade, para que ouçam, e aprendam, e temam o Senhor, vosso Deus, e cuidem de cumprir todas as palavras desta lei;
13 para que seus filhos que não a souberem ouçam e aprendam a temer o Senhor, vosso Deus, todos os dias que viverdes sobre a terra à qual ides, passando o Jordão, para a possuir.
14 Disse o Senhor a Moisés: Eis que os teus dias são chegados, para que morras; chama Josué, e apresentai-vos na tenda da congregação, para que eu lhe dê ordens. Assim, foram Moisés e Josué e se apresentaram na tenda da congregação.
15 Então, o Senhor apareceu, ali, na coluna de nuvem, a qual se deteve sobre a porta da tenda.
16 Disse o Senhor a Moisés: Eis que estás para dormir com teus pais; e este povo se levantará, e se prostituirá, indo após deuses estranhos na terra para cujo meio vai, e me deixará, e anulará a aliança que fiz com ele.
17 Nesse dia, a minha ira se acenderá contra ele; desampará-lo-ei e dele esconderei o rosto, para que seja devorado; e tantos males e angústias o alcançarão, que dirá naquele dia: Não nos alcançaram estes males por não estar o nosso Deus no meio de nós?
18 Esconderei, pois, certamente, o rosto naquele dia, por todo o mal que tiverem feito, por se haverem tornado a outros deuses.
19 Escrevei para vós outros este cântico e ensinai-o aos filhos de Israel; ponde-o na sua boca, para que este cântico me seja por testemunha contra os filhos de Israel.
20 Quando eu tiver introduzido o meu povo na terra que mana leite e mel, a qual, sob juramento, prometi a seus pais, e, tendo ele comido, e se fartado, e engordado, e houver tornado a outros deuses, e os houver servido, e me irritado, e anulado a minha aliança;
21 e, quando o tiverem alcançado muitos males e angústias, então, este cântico responderá contra ele por testemunha, pois a sua descendência, sempre, o trará na boca; porquanto conheço os desígnios que, hoje, estão formulando, antes que o introduza na terra que, sob juramento, prometi.
22 Assim, Moisés, naquele mesmo dia, escreveu este cântico e o ensinou aos filhos de Israel.
23 Ordenou o Senhor a Josué, filho de Num, e disse: Sê forte e corajoso, porque tu introduzirás os filhos de Israel na terra que, sob juramento, lhes prometi; e eu serei contigo.
24 Tendo Moisés acabado de escrever, integralmente, as palavras desta lei num livro,
25 deu ordem aos levitas que levavam a arca da Aliança do Senhor, dizendo:
26 Tomai este Livro da Lei e ponde-o ao lado da arca da Aliança do Senhor, vosso Deus, para que ali esteja por testemunha contra ti.
27 Porque conheço a tua rebeldia e a tua dura cerviz. Pois, se, vivendo eu, ainda hoje, convosco, sois rebeldes contra o Senhor, quanto mais depois da minha morte?
28 Ajuntai perante mim todos os anciãos das vossas tribos e vossos oficiais, para que eu fale aos seus ouvidos estas palavras e contra eles, por testemunhas, tomarei os céus e a terra.
29 Porque sei que, depois da minha morte, por certo, procedereis corruptamente e vos desviareis do caminho que vos tenho ordenado; então, este mal vos alcançará nos últimos dias, porque fareis mal perante o Senhor, provocando-o à ira com as obras das vossas mãos.
30 Então, Moisés pronunciou, integralmente, as palavras deste cântico aos ouvidos de toda a congregação de Israel:*
1 Inclinai os ouvidos, ó céus, e falarei; e ouça a terra as palavras da minha boca.
2 Goteje a minha doutrina como a chuva, destile a minha palavra como o orvalho, como chuvisco sobre a relva e como gotas de água sobre a erva.
3 Porque proclamarei o nome do Senhor. Engrandecei o nosso Deus.
4 Eis a Rocha! Suas obras são perfeitas, porque todos os seus caminhos são juízo; Deus é fidelidade, e não há nele injustiça; é justo e reto.
5 Procederam corruptamente contra ele, já não são seus filhos, e sim suas manchas; é geração perversa e deformada.
6 É assim que recompensas ao Senhor, povo louco e ignorante? Não é ele teu pai, que te adquiriu, te fez e te estabeleceu?
7 Lembra-te dos dias da antiguidade, atenta para os anos de gerações e gerações; pergunta a teu pai, e ele te informará, aos teus anciãos, e eles to dirão.
8 Quando o Altíssimo distribuía as heranças às nações, quando separava os filhos dos homens uns dos outros, fixou os limites dos povos, segundo o número dos filhos de Israel.
9 Porque a porção do Senhor é o seu povo; Jacó é a parte da sua herança.
10 Achou-o numa terra deserta e num ermo solitário povoado de uivos; rodeou-o e cuidou dele, guardou-o como a menina dos olhos.
11 Como a águia desperta a sua ninhada e voeja sobre os seus filhotes, estende as asas e, tomando-os, os leva sobre elas,
12 assim, só o Senhor o guiou, e não havia com ele deus estranho.
13 Ele o fez cavalgar sobre os altos da terra, comer as messes do campo, chupar mel da rocha e azeite da dura pederneira,
14 coalhada de vacas e leite de ovelhas, com a gordura dos cordeiros, dos carneiros que pastam em Basã e dos bodes, com o mais escolhido trigo; e bebeste o sangue das uvas, o mosto.
15 Mas, engordando-se o meu amado, deu coices; engordou-se, engrossou-se, ficou nédio e abandonou a Deus, que o fez, desprezou a Rocha da sua salvação.
16 Com deuses estranhos o provocaram a zelos, com abominações o irritaram.
17 Sacrifícios ofereceram aos demônios, não a Deus; a deuses que não conheceram, novos deuses que vieram há pouco, dos quais não se estremeceram seus pais.
18 Olvidaste a Rocha que te gerou; e te esqueceste do Deus que te deu o ser.
19 Viu isto o Senhor e os desprezou, por causa da provocação de seus filhos e suas filhas;
20 e disse: Esconderei deles o rosto, verei qual será o seu fim; porque são raça de perversidade, filhos em quem não há lealdade.
21 A zelos me provocaram com aquilo que não é Deus; com seus ídolos me provocaram à ira; portanto, eu os provocarei a zelos com aquele que não é povo; com louca nação os despertarei à ira.
22 Porque um fogo se acendeu no meu furor e arderá até ao mais profundo do inferno, consumirá a terra e suas messes e abrasará os fundamentos dos montes.
23 Amontoarei males sobre eles; as minhas setas esgotarei contra eles.
24 Consumidos serão pela fome, devorados pela febre e peste violenta; e contra eles enviarei dentes de feras e ardente peçonha de serpentes do pó.
25 Fora devastará a espada, em casa, o pavor, tanto ao jovem como à virgem, tanto à criança de peito como ao homem encanecido.
26 Eu teria dito: Por todos os cantos os espalharei e farei cessar a sua memória dentre os homens,
27 se eu não tivesse receado a provocação do inimigo, para que os seus adversários não se iludam, para que não digam: A nossa mão tem prevalecido, e não foi o Senhor quem fez tudo isto.
28 Porque o meu povo é gente falta de conselhos, e neles não há entendimento.
29 Tomara fossem eles sábios! Então, entenderiam isto e atentariam para o seu fim.
30 Como poderia um só perseguir mil, e dois fazerem fugir dez mil, se a sua Rocha lhos não vendera, e o Senhor lhos não entregara?
31 Porque a rocha deles não é como a nossa Rocha; e os próprios inimigos o atestam.
32 Porque a sua vinha é da vinha de Sodoma e dos campos de Gomorra; as suas uvas são uvas de veneno, seus cachos, amargos;
33 o seu vinho é ardente veneno de répteis e peçonha terrível de víboras.
34 Não está isto guardado comigo, selado nos meus tesouros?
35 A mim me pertence a vingança, a retribuição, a seu tempo, quando resvalar o seu pé; porque o dia da sua calamidade está próximo, e o seu destino se apressa em chegar.
36 Porque o Senhor fará justiça ao seu povo e se compadecerá dos seus servos, quando vir que o seu poder se foi, e já não há nem escravo nem livre.
37 Então, dirá: Onde estão os seus deuses? E a rocha em quem confiavam?
38 Deuses que comiam a gordura de seus sacrifícios e bebiam o vinho de suas libações? Levantem-se eles e vos ajudem, para que haja esconderijo para vós outros!
39 Vede, agora, que Eu Sou, Eu somente, e mais nenhum deus além de mim; eu mato e eu faço viver; eu firo e eu saro; e não há quem possa livrar alguém da minha mão.
40 Levanto a mão aos céus e afirmo por minha vida eterna:
41 se eu afiar a minha espada reluzente, e a minha mão exercitar o juízo, tomarei vingança contra os meus adversários e retribuirei aos que me odeiam.
42 Embriagarei as minhas setas de sangue (a minha espada comerá carne), do sangue dos mortos e dos prisioneiros, das cabeças cabeludas do inimigo.
43 Louvai, ó nações, o seu povo, porque o Senhor vingará o sangue dos seus servos, tomará vingança dos seus adversários e fará expiação pela terra do seu povo.
44 Veio Moisés e falou todas as palavras deste cântico aos ouvidos do povo, ele e Josué, filho de Num.
45 Tendo Moisés falado todas estas palavras a todo o Israel,
46 disse-lhes: Aplicai o coração a todas as palavras que, hoje, testifico entre vós, para que ordeneis a vossos filhos que cuidem de cumprir todas as palavras desta lei.
47 Porque esta palavra não é para vós outros coisa vã; antes, é a vossa vida; e, por esta mesma palavra, prolongareis os dias na terra à qual, passando o Jordão, ides para a possuir.
48 Naquele mesmo dia, falou o Senhor a Moisés, dizendo:
49 Sobe a este monte de Abarim, ao monte Nebo, que está na terra de Moabe, defronte de Jericó, e vê a terra de Canaã, que aos filhos de Israel dou em possessão.
50 E morrerás no monte, ao qual terás subido, e te recolherás ao teu povo, como Arão, teu irmão, morreu no monte Hor e se recolheu ao seu povo,
51 porquanto prevaricastes contra mim no meio dos filhos de Israel, nas águas de Meribá de Cades, no deserto de Zim, pois me não santificastes no meio dos filhos de Israel.
52 Pelo que verás a terra defronte de ti, porém não entrarás nela, na terra que dou aos filhos de Israel.*
1 Esta é a bênção que Moisés, homem de Deus, deu aos filhos de Israel, antes da sua morte.
2 Disse, pois: O Senhor veio do Sinai e lhes alvoreceu de Seir, resplandeceu desde o monte Parã; e veio das miríades de santos; à sua direita, havia para eles o fogo da lei.
3 Na verdade, amas os povos; todos os teus santos estão na tua mão; eles se colocam a teus pés e aprendem das tuas palavras.
4 Moisés nos prescreveu a lei por herança da congregação de Jacó.
5 E o Senhor se tornou rei ao seu povo amado, quando se congregaram os cabeças do povo com as tribos de Israel.
6 Viva Rúben e não morra; e não sejam poucos os seus homens!
7 Isto é o que disse de Judá: Ouve, ó Senhor, a voz de Judá e introduze-o no seu povo; com as tuas mãos, peleja por ele e sê tu ajuda contra os seus inimigos.
8 De Levi disse: Dá, ó Deus, o teu Tumim e o teu Urim para o homem, teu fidedigno, que tu provaste em Massá, com quem contendeste nas águas de Meribá;
9 aquele que disse a seu pai e a sua mãe: Nunca os vi; e não conheceu a seus irmãos e não estimou a seus filhos, pois guardou a tua palavra e observou a tua aliança.
10 Ensinou os teus juízos a Jacó e a tua lei, a Israel; ofereceu incenso às tuas narinas e holocausto, sobre o teu altar.
11 Abençoa o seu poder, ó Senhor, e aceita a obra das suas mãos, fere os lombos dos que se levantam contra ele e o aborrecem, para que nunca mais se levantem.
12 De Benjamim disse: O amado do Senhor habitará seguro com ele; todo o dia o Senhor o protegerá, e ele descansará nos seus braços.
13 De José disse: Bendita do Senhor seja a sua terra, com o que é mais excelente dos céus, do orvalho e das profundezas,
14 com o que é mais excelente daquilo que o sol amadurece e daquilo que os meses produzem,
15 com o que é mais excelente dos montes antigos e mais excelente dos outeiros eternos,
16 com o que é mais excelente da terra e da sua plenitude e da benevolência daquele que apareceu na sarça; que tudo isto venha sobre a cabeça de José, sobre a cabeça do príncipe entre seus irmãos.
17 Ele tem a imponência do primogênito do seu touro, e as suas pontas são como as de um boi selvagem; com elas rechaçará todos os povos até às extremidades da terra. Tais, pois, as miríades de Efraim, e tais, os milhares de Manassés.
18 De Zebulom disse: Alegra-te, Zebulom, nas tuas saídas marítimas, e tu, Issacar, nas tuas tendas.
19 Os dois chamarão os povos ao monte; ali apresentarão ofertas legítimas, porque chuparão a abundância dos mares e os tesouros escondidos da areia.
20 De Gade disse: Bendito aquele que faz dilatar Gade, o qual habita como a leoa e despedaça o braço e o alto da cabeça.
21 E se proveu da melhor parte, porquanto ali estava escondida a porção do chefe; ele marchou adiante do povo, executou a justiça do Senhor e os seus juízos para com Israel.
22 De Dã disse: Dã é leãozinho; saltará de Basã.
23 De Naftali disse: Naftali goza de favores e, cheio da bênção do Senhor, possuirá o lago e o Sul.
24 De Aser disse: Bendito seja Aser entre os filhos de Jacó, agrade a seus irmãos e banhe em azeite o pé.
25 Sejam de ferro e de bronze os teus ferrolhos, e, como os teus dias, durará a tua paz.
26 Não há outro, ó amado, semelhante a Deus, que cavalga sobre os céus para a tua ajuda e com a sua alteza sobre as nuvens.
27 O Deus eterno é a tua habitação e, por baixo de ti, estende os braços eternos; ele expulsou o inimigo de diante de ti e disse: Destrói-o.
28 Israel, pois, habitará seguro, a fonte de Jacó habitará a sós numa terra de cereal e de vinho; e os seus céus destilarão orvalho.
29 Feliz és tu, ó Israel! Quem é como tu? Povo salvo pelo Senhor, escudo que te socorre, espada que te dá alteza. Assim, os teus inimigos te serão sujeitos, e tu pisarás os seus altos.*
1 Então, subiu Moisés das campinas de Moabe ao monte Nebo, ao cimo de Pisga, que está defronte de Jericó; e o Senhor lhe mostrou toda a terra de Gileade até Dã;
2 e todo o Naftali, e a terra de Efraim, e Manassés; e toda a terra de Judá até ao mar ocidental;
3 e o Neguebe e a campina do vale de Jericó, a cidade das Palmeiras, até Zoar.
4 Disse-lhe o Senhor: Esta é a terra que, sob juramento, prometi a Abraão, a Isaque e a Jacó, dizendo: à tua descendência a darei; eu te faço vê-la com os próprios olhos; porém não irás para lá.
5 Assim, morreu ali Moisés, servo do Senhor, na terra de Moabe, segundo a palavra do Senhor.
6 Este o sepultou num vale, na terra de Moabe, defronte de Bete-Peor; e ninguém sabe, até hoje, o lugar da sua sepultura.
7 Tinha Moisés a idade de cento e vinte anos quando morreu; não se lhe escureceram os olhos, nem se lhe abateu o vigor.
8 Os filhos de Israel prantearam Moisés por trinta dias, nas campinas de Moabe; então, se cumpriram os dias do pranto no luto por Moisés.
9 Josué, filho de Num, estava cheio do espírito de sabedoria, porquanto Moisés impôs sobre ele as mãos; assim, os filhos de Israel lhe deram ouvidos e fizeram como o Senhor ordenara a Moisés.
10 Nunca mais se levantou em Israel profeta algum como Moisés, com quem o Senhor houvesse tratado face a face,
11 no tocante a todos os sinais e maravilhas que, por mando do Senhor, fez na terra do Egito, a Faraó, a todos os seus oficiais e a toda a sua terra;
12 e no tocante a todas as obras de sua poderosa mão e aos grandes e terríveis feitos que operou Moisés à vista de todo o Israel.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Deuteronômio','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)