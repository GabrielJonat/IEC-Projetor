import re


def parse_verses(text,book,chapter):
    chapter = int(chapter)
    newText = ''
    char = 0
    while char < len(text):
        if text[char] == '*':
            chapter += 1
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
22 Então, ordenou Faraó a todo o seu povo, dizendo: A todos os filhos que nascerem aos hebreus lançareis no Nilo, mas a todas as filhas deixareis viver.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Êxodo','50')
print(parsed_verses)