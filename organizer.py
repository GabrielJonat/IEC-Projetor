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
1 São estes os nomes dos filhos de Israel que entraram com Jacó no Egito; cada um entrou com sua família:
2 Rúben, Simeão, Levi e Judá,
3 Issacar, Zebulom e Benjamim,
4 Dã, Naftali, Gade e Aser.
5 Todas as pessoas, pois, que descenderam de Jacó foram setenta; José, porém, estava no Egito.
6 Faleceu José, e todos os seus irmãos, e toda aquela geração.
7 Mas os filhos de Israel foram fecundos, e aumentaram muito, e se multiplicaram, e grandemente se fortaleceram, de maneira que a terra se encheu deles.
8 Entrementes, se levantou novo rei sobre o Egito, que não conhecera a José.
9 Ele disse ao seu povo: Eis que o povo dos filhos de Israel é mais numeroso e mais forte do que nós.
10 Eia, usemos de astúcia para com ele, para que não se multiplique, e seja o caso que, vindo guerra, ele se ajunte com os nossos inimigos, peleje contra nós e saia da terra.
11 E os egípcios puseram sobre eles feitores de obras, para os afligirem com suas cargas. E os israelitas edificaram a Faraó as cidades-celeiros, Pitom e Ramessés.
12 Mas, quanto mais os afligiam, tanto mais se multiplicavam e tanto mais se espalhavam; de maneira que se inquietavam por causa dos filhos de Israel;
13 então, os egípcios, com tirania, faziam servir os filhos de Israel
14 e lhes fizeram amargar a vida com dura servidão, em barro, e em tijolos, e com todo o trabalho no campo; com todo o serviço em que na tirania os serviam.
As parteiras desobedecem a Faraó
15 O rei do Egito ordenou às parteiras hebreias, das quais uma se chamava Sifrá, e outra, Puá,
16 dizendo: Quando servirdes de parteira às hebreias, examinai: se for filho, matai-o; mas, se for filha, que viva.
17 As parteiras, porém, temeram a Deus e não fizeram como lhes ordenara o rei do Egito; antes, deixaram viver os meninos.
18 Então, o rei do Egito chamou as parteiras e lhes disse: Por que fizestes isso e deixastes viver os meninos?
19 Responderam as parteiras a Faraó: É que as mulheres hebreias não são como as egípcias; são vigorosas e, antes que lhes chegue a parteira, já deram à luz os seus filhos.
20 E Deus fez bem às parteiras; e o povo aumentou e se tornou muito forte.
21 E, porque as parteiras temeram a Deus, ele lhes constituiu família.
22 Então, ordenou Faraó a todo o seu povo, dizendo: A todos os filhos que nascerem aos hebreus lançareis no Nilo, mas a todas as filhas deixareis viver.*
1 Foi-se um homem da casa de Levi e casou com uma descendente de Levi.
2 E a mulher concebeu e deu à luz um filho; e, vendo que era formoso, escondeu-o por três meses.
3 Não podendo, porém, escondê-lo por mais tempo, tomou um cesto de junco, calafetou-o com betume e piche e, pondo nele o menino, largou-o no carriçal à beira do rio.
4 A irmã do menino ficou de longe, para observar o que lhe haveria de suceder.
5 Desceu a filha de Faraó para se banhar no rio, e as suas donzelas passeavam pela beira do rio; vendo ela o cesto no carriçal, enviou a sua criada e o tomou.
6 Abrindo-o, viu a criança; e eis que o menino chorava. Teve compaixão dele e disse: Este é menino dos hebreus.
7 Então, disse sua irmã à filha de Faraó: Queres que eu vá chamar uma das hebreias que sirva de ama e te crie a criança?
8 Respondeu-lhe a filha de Faraó: Vai. Saiu, pois, a moça e chamou a mãe do menino.
9 Então, lhe disse a filha de Faraó: Leva este menino e cria-mo; pagar-te-ei o teu salário. A mulher tomou o menino e o criou.
10 Sendo o menino já grande, ela o trouxe à filha de Faraó, da qual passou ele a ser filho. Esta lhe chamou Moisés e disse: Porque das águas o tirei.
11 Naqueles dias, sendo Moisés já homem, saiu a seus irmãos e viu os seus labores penosos; e viu que certo egípcio espancava um hebreu, um do seu povo.
12 Olhou de um e de outro lado, e, vendo que não havia ali ninguém, matou o egípcio, e o escondeu na areia.
13 Saiu no dia seguinte, e eis que dois hebreus estavam brigando; e disse ao culpado: Por que espancas o teu próximo?
14 O qual respondeu: Quem te pôs por príncipe e juiz sobre nós? Pensas matar-me, como mataste o egípcio? Temeu, pois, Moisés e disse: Com certeza o descobriram.
15 Informado desse caso, procurou Faraó matar a Moisés; porém Moisés fugiu da presença de Faraó e se deteve na terra de Midiã; e assentou-se junto a um poço.
16 O sacerdote de Midiã tinha sete filhas, as quais vieram a tirar água e encheram os bebedouros para dar de beber ao rebanho de seu pai.
17 Então, vieram os pastores e as enxotaram dali; Moisés, porém, se levantou, e as defendeu, e deu de beber ao rebanho.
18 Tendo elas voltado a Reuel, seu pai, este lhes perguntou: Por que viestes, hoje, mais cedo?
19 Responderam elas: Um egípcio nos livrou das mãos dos pastores, e ainda nos tirou água, e deu de beber ao rebanho.
20 E onde está ele?, disse às filhas; por que deixastes lá o homem? Chamai-o para que coma pão.
21 Moisés consentiu em morar com aquele homem; e ele deu a Moisés sua filha Zípora,
22 a qual deu à luz um filho, a quem ele chamou Gérson, porque disse: Sou peregrino em terra estranha.
23 Decorridos muitos dias, morreu o rei do Egito; os filhos de Israel gemiam sob a servidão e por causa dela clamaram, e o seu clamor subiu a Deus.
24 Ouvindo Deus o seu gemido, lembrou-se da sua aliança com Abraão, com Isaque e com Jacó.
25 E viu Deus os filhos de Israel e atentou para a sua condição.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Êxodo','1')
print(parsed_verses)