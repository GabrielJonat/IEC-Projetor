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
1 Nos dias em que julgavam os juízes, houve fome na terra; e um homem de Belém de Judá saiu a habitar na terra de Moabe, com sua mulher e seus dois filhos.
2 Este homem se chamava Elimeleque, e sua mulher, Noemi; os filhos se chamavam Malom e Quiliom, efrateus, de Belém de Judá; vieram à terra de Moabe e ficaram ali.
3 Morreu Elimeleque, marido de Noemi; e ficou ela com seus dois filhos,
4 os quais casaram com mulheres moabitas; era o nome de uma Orfa, e o nome da outra, Rute; e ficaram ali quase dez anos.
5 Morreram também ambos, Malom e Quiliom, ficando, assim, a mulher desamparada de seus dois filhos e de seu marido.
6 Então, se dispôs ela com as suas noras e voltou da terra de Moabe, porquanto, nesta, ouviu que o Senhor se lembrara do seu povo, dando-lhe pão.
7 Saiu, pois, ela com suas duas noras do lugar onde estivera; e, indo elas caminhando, de volta para a terra de Judá,
8 disse-lhes Noemi: Ide, voltai cada uma à casa de sua mãe; e o Senhor use convosco de benevolência, como vós usastes com os que morreram e comigo.
9 O Senhor vos dê que sejais felizes, cada uma em casa de seu marido. E beijou-as. Elas, porém, choraram em alta voz
10 e lhe disseram: Não! Iremos contigo ao teu povo.
11 Porém Noemi disse: Voltai, minhas filhas! Por que iríeis comigo? Tenho eu ainda no ventre filhos, para que vos sejam por maridos?
12 Tornai, filhas minhas! Ide-vos embora, porque sou velha demais para ter marido. Ainda quando eu dissesse: tenho esperança ou ainda que esta noite tivesse marido e houvesse filhos,
13 esperá-los-íeis até que viessem a ser grandes? Abster-vos-íeis de tomardes marido? Não, filhas minhas! Porque, por vossa causa, a mim me amarga o ter o Senhor descarregado contra mim a sua mão.
14 Então, de novo, choraram em voz alta; Orfa, com um beijo, se despediu de sua sogra, porém Rute se apegou a ela.
15 Disse Noemi: Eis que tua cunhada voltou ao seu povo e aos seus deuses; também tu, volta após a tua cunhada.
16 Disse, porém, Rute: Não me instes para que te deixe e me obrigue a não seguir-te; porque, aonde quer que fores, irei eu e, onde quer que pousares, ali pousarei eu; o teu povo é o meu povo, o teu Deus é o meu Deus.
17 Onde quer que morreres, morrerei eu e aí serei sepultada; faça-me o Senhor o que bem lhe aprouver, se outra coisa que não seja a morte me separar de ti.
18 Vendo, pois, Noemi que de todo estava resolvida a acompanhá-la, deixou de insistir com ela.
19 Então, ambas se foram, até que chegaram a Belém; sucedeu que, ao chegarem ali, toda a cidade se comoveu por causa delas, e as mulheres diziam: Não é esta Noemi?
20 Porém ela lhes dizia: Não me chameis Noemi; chamai-me Mara, porque grande amargura me tem dado o Todo-Poderoso.
21 Ditosa eu parti, porém o Senhor me fez voltar pobre; por que, pois, me chamareis Noemi, visto que o Senhor se manifestou contra mim e o Todo-Poderoso me tem afligido?
22 Assim, voltou Noemi da terra de Moabe, com Rute, sua nora, a moabita; e chegaram a Belém no princípio da sega da cevada.*
1 Tinha Noemi um parente de seu marido, senhor de muitos bens, da família de Elimeleque, o qual se chamava Boaz.
2 Rute, a moabita, disse a Noemi: Deixa-me ir ao campo, e apanharei espigas atrás daquele que mo favorecer. Ela lhe disse: Vai, minha filha!
3 Ela se foi, chegou ao campo e apanhava após os segadores; por casualidade entrou na parte que pertencia a Boaz, o qual era da família de Elimeleque.
4 Eis que Boaz veio de Belém e disse aos segadores: O Senhor seja convosco! Responderam-lhe eles: O Senhor te abençoe!
5 Depois, perguntou Boaz ao servo encarregado dos segadores: De quem é esta moça?
6 Respondeu-lhe o servo: Esta é a moça moabita que veio com Noemi da terra de Moabe.
7 Disse-me ela: Deixa-me rebuscar espigas e ajuntá-las entre as gavelas após os segadores. Assim, ela veio; desde pela manhã até agora está aqui, menos um pouco que esteve na choça.
8 Então, disse Boaz a Rute: Ouve, filha minha, não vás colher em outro campo, nem tampouco passes daqui; porém aqui ficarás com as minhas servas.
9 Estarás atenta ao campo que segarem e irás após elas. Não dei ordem aos servos, que te não toquem? Quando tiveres sede, vai às vasilhas e bebe do que os servos tiraram.
10 Então, ela, inclinando-se, rosto em terra, lhe disse: Como é que me favoreces e fazes caso de mim, sendo eu estrangeira?
11 Respondeu Boaz e lhe disse: Bem me contaram tudo quanto fizeste a tua sogra, depois da morte de teu marido, e como deixaste a teu pai, e a tua mãe, e a terra onde nasceste e vieste para um povo que dantes não conhecias.
12 O Senhor retribua o teu feito, e seja cumprida a tua recompensa do Senhor, Deus de Israel, sob cujas asas vieste buscar refúgio.
13 Disse ela: Tu me favoreces muito, senhor meu, pois me consolaste e falaste ao coração de tua serva, não sendo eu nem ainda como uma das tuas servas.
14 À hora de comer, Boaz lhe disse: Achega-te para aqui, e come do pão, e molha no vinho o teu bocado. Ela se assentou ao lado dos segadores, e ele lhe deu grãos tostados de cereais; ela comeu e se fartou, e ainda lhe sobejou.
15 Levantando-se ela para rebuscar, Boaz deu ordem aos seus servos, dizendo: Até entre as gavelas deixai-a colher e não a censureis.
16 Tirai também dos molhos algumas espigas, e deixai-as, para que as apanhe, e não a repreendais.
17 Esteve ela apanhando naquele campo até à tarde; debulhou o que apanhara, e foi quase um efa de cevada.
18 Tomou-o e veio à cidade; e viu sua sogra o que havia apanhado; também o que lhe sobejara depois de fartar-se tirou e deu a sua sogra.
19 Então, lhe disse a sogra: Onde colheste hoje? Onde trabalhaste? Bendito seja aquele que te acolheu favoravelmente! E Rute contou a sua sogra onde havia trabalhado e disse: O nome do senhor, em cujo campo trabalhei, é Boaz.
20 Então, Noemi disse a sua nora: Bendito seja ele do Senhor, que ainda não tem deixado a sua benevolência nem para com os vivos nem para com os mortos. Disse-lhe mais Noemi: Esse homem é nosso parente chegado e um dentre os nossos resgatadores.
21 Continuou Rute, a moabita: Também ainda me disse: Com os meus servos ficarás, até que acabem toda a sega que tenho.
22 Disse Noemi a sua nora, Rute: Bom será, filha minha, que saias com as servas dele, para que, noutro campo, não te molestem.
23 Assim, passou ela à companhia das servas de Boaz, para colher, até que a sega da cevada e do trigo se acabou; e ficou com a sua sogra.*
1 Disse-lhe Noemi, sua sogra: Minha filha, não hei de eu buscar-te um lar, para que sejas feliz?
2 Ora, pois, não é Boaz, na companhia de cujas servas estiveste, um dos nossos parentes? Eis que esta noite alimpará a cevada na eira.
3 Banha-te, e unge-te, e põe os teus melhores vestidos, e desce à eira; porém não te dês a conhecer ao homem, até que tenha acabado de comer e beber.
4 Quando ele repousar, notarás o lugar em que se deita; então, chegarás, e lhe descobrirás os pés, e te deitarás; ele te dirá o que deves fazer.
5 Respondeu-lhe Rute: Tudo quanto me disseres farei.
6 Então, foi para a eira e fez conforme tudo quanto sua sogra lhe havia ordenado.
7 Havendo, pois, Boaz comido e bebido e estando já de coração um tanto alegre, veio deitar-se ao pé de um monte de cereais; então, chegou ela de mansinho, e lhe descobriu os pés, e se deitou.
8 Sucedeu que, pela meia-noite, assustando-se o homem, sentou-se; e eis que uma mulher estava deitada a seus pés.
9 Disse ele: Quem és tu? Ela respondeu: Sou Rute, tua serva; estende a tua capa sobre a tua serva, porque tu és resgatador.
10 Disse ele: Bendita sejas tu do Senhor, minha filha; melhor fizeste a tua última benevolência que a primeira, pois não foste após jovens, quer pobres, quer ricos.
11 Agora, pois, minha filha, não tenhas receio; tudo quanto disseste eu te farei, pois toda a cidade do meu povo sabe que és mulher virtuosa.
12 Ora, é muito verdade que eu sou resgatador; mas ainda outro resgatador há mais chegado do que eu.
13 Fica-te aqui esta noite, e será que, pela manhã, se ele te quiser resgatar, bem está, que te resgate; porém, se não lhe apraz resgatar-te, eu o farei, tão certo como vive o Senhor; deita-te aqui até à manhã.
14 Ficou-se, pois, deitada a seus pés até pela manhã e levantou-se antes que pudessem conhecer um ao outro; porque ele disse: Não se saiba que veio mulher à eira.
15 Disse mais: Dá-me o manto que tens sobre ti e segura-o. Ela o segurou, ele o encheu com seis medidas de cevada e lho pôs às costas; então, entrou ela na cidade.
16 Em chegando à casa de sua sogra, esta lhe disse: Como se te passaram as coisas, filha minha? Ela lhe contou tudo quanto aquele homem lhe fizera.
17 E disse ainda: Estas seis medidas de cevada, ele mas deu e me disse: Não voltes para a tua sogra sem nada.
18 Então, lhe disse Noemi: Espera, minha filha, até que saibas em que darão as coisas, porque aquele homem não descansará, enquanto não se resolver este caso ainda hoje.*
1 Boaz subiu à porta da cidade e assentou-se ali. Eis que o resgatador de que Boaz havia falado ia passando; então, lhe disse: Ó fulano, chega-te para aqui e assenta-te; ele se virou e se assentou.
2 Então, Boaz tomou dez homens dos anciãos da cidade e disse: Assentai-vos aqui. E assentaram-se.
3 Disse ao resgatador: Aquela parte da terra que foi de Elimeleque, nosso irmão, Noemi, que tornou da terra dos moabitas, a tem para venda.
4 Resolvi, pois, informar-te disso e dizer-te: compra-a na presença destes que estão sentados aqui e na de meu povo; se queres resgatá-la, resgata-a; se não, declara-mo para que eu o saiba, pois outro não há senão tu que a resgate, e eu, depois de ti. Respondeu ele: Eu a resgatarei.
5 Disse, porém, Boaz: No dia em que tomares a terra da mão de Noemi, também a tomarás da mão de Rute, a moabita, já viúva, para suscitar o nome do esposo falecido, sobre a herança dele.
6 Então, disse o resgatador: Para mim não a poderei resgatar, para que não prejudique a minha; redime tu o que me cumpria resgatar, porque eu não poderei fazê-lo.
7 Este era, outrora, o costume em Israel, quanto a resgates e permutas: o que queria confirmar qualquer negócio tirava o calçado e o dava ao seu parceiro; assim se confirmava negócio em Israel.
8 Disse, pois, o resgatador a Boaz: Compra-a tu. E tirou o calçado.
9 Então, Boaz disse aos anciãos e a todo o povo: Sois, hoje, testemunhas de que comprei da mão de Noemi tudo o que pertencia a Elimeleque, a Quiliom e a Malom;
10 e também tomo por mulher Rute, a moabita, que foi esposa de Malom, para suscitar o nome deste sobre a sua herança, para que este nome não seja exterminado dentre seus irmãos e da porta da sua cidade; disto sois, hoje, testemunhas.
11 Todo o povo que estava na porta e os anciãos disseram: Somos testemunhas; o Senhor faça a esta mulher, que entra na tua casa, como a Raquel e como a Lia, que ambas edificaram a casa de Israel; e tu, Boaz, há-te valorosamente em Efrata e faze-te nome afamado em Belém.
12 Seja a tua casa como a casa de Perez, que Tamar teve de Judá, pela prole que o Senhor te der desta jovem.
13 Assim, tomou Boaz a Rute, e ela passou a ser sua mulher; coabitou com ela, e o Senhor lhe concedeu que concebesse, e teve um filho.
14 Então, as mulheres disseram a Noemi: Seja o Senhor bendito, que não deixou, hoje, de te dar um neto que será teu resgatador, e seja afamado em Israel o nome deste.
15 Ele será restaurador da tua vida e consolador da tua velhice, pois tua nora, que te ama, o deu à luz, e ela te é melhor do que sete filhos.
16 Noemi tomou o menino, e o pôs no regaço, e entrou a cuidar dele.
17 As vizinhas lhe deram nome, dizendo: A Noemi nasceu um filho. E lhe chamaram Obede. Este é o pai de Jessé, pai de Davi.
18 São estas, pois, as gerações de Perez: Perez gerou a Esrom,
19 Esrom gerou a Rão, Rão gerou a Aminadabe,
20 Aminadabe gerou a Naassom, Naassom gerou a Salmom,
21 Salmom gerou a Boaz, Boaz gerou a Obede,
22 Obede gerou a Jessé, e Jessé gerou a Davi.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Rute','1')
#print(parsed_verses)
with open('textzin', 'w', encoding='utf-8') as f:
    f.write(parsed_verses)