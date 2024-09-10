import re


def parse_verses(text,book,chapter):

    newText = ''
    char = 0
    while char < len(text):
        if text[char].isnumeric():
            if text[char + 1].isnumeric() and text[char + 2].isalpha():
                newText += '\n' + book + ' ' + chapter + ':' + text[char] + text[char + 1]+' '
                char += 1
            elif text[char + 1].isnumeric() and text[char + 2].isnumeric():
                newText += '\n' + book + ' ' + chapter + ':' + text[char] + text[char + 1]+text[char+2]+' '
                char += 2
            else:
                newText += '\n'+book+' '+chapter+':'+text[char]+' '
        else:
            newText += text[char]
        char += 1
    return newText


text = """
1Então, José se lançou sobre o rosto de seu pai, e chorou sobre ele, e o beijou. 2Ordenou José a seus servos, aos que eram médicos, que embalsamassem a seu pai; e os médicos embalsamaram a Israel, 3gastando nisso quarenta dias, pois assim se cumprem os dias do embalsamamento; e os egípcios o choraram setenta dias.4Passados os dias de o chorarem, falou José à casa de Faraó: Se agora achei mercê perante vós, rogo-vos que faleis aos ouvidos de Faraó, dizendo: 5Meu pai me fez jurar, declarando: Eis que eu morro; no meu sepulcro que abri para mim na terra de Canaã, ali me sepultarás. Agora, pois, desejo subir e sepultar meu pai, depois voltarei. 6Respondeu Faraó: Sobe e sepulta o teu pai como ele te fez jurar. 7José subiu para sepultar o seu pai; e subiram com ele todos os oficiais de Faraó, os principais da sua casa e todos os principais da terra do Egito, 8como também toda a casa de José, e seus irmãos, e a casa de seu pai; somente deixaram na terra de Gósen as crianças, e os rebanhos, e o gado. 9E subiram também com ele tanto carros como cavaleiros; e o cortejo foi grandíssimo. 10Chegando eles, pois, à eira de Atade, que está além do Jordão, fizeram ali grande e intensa lamentação; e José pranteou seu pai durante sete dias. 11Tendo visto os moradores da terra, os cananeus, o luto na eira de Atade, disseram: Grande pranto é este dos egípcios. E por isso se chamou aquele lugar de Abel-Mizraim, que está além do Jordão. 12Fizeram-lhe seus filhos como lhes havia ordenado: 13levaram-no para a terra de Canaã e o sepultaram na caverna do campo de Macpela, que Abraão comprara com o campo, por posse de sepultura, a Efrom, o heteu, fronteiro a Manre. 14Depois disso, voltou José para o Egito, ele, seus irmãos e todos os que com ele subiram a sepultar o seu pai.15Vendo os irmãos de José que seu pai já era morto, disseram: É o caso de José nos perseguir e nos retribuir certamente o mal todo que lhe fizemos. 16Portanto, mandaram dizer a José: Teu pai ordenou, antes da sua morte, dizendo: 17Assim direis a José: Perdoa, pois, a transgressão de teus irmãos e o seu pecado, porque te fizeram mal; agora, pois, te rogamos que perdoes a transgressão dos servos do Deus de teu pai. José chorou enquanto lhe falavam. 18Depois, vieram também seus irmãos, prostraram-se diante dele e disseram: Eis-nos aqui por teus servos. 19Respondeu-lhes José: Não temais; acaso, estou eu em lugar de Deus? 20Vós, na verdade, intentastes o mal contra mim; porém Deus o tornou em bem, para fazer, como vedes agora, que se conserve muita gente em vida. 21Não temais, pois; eu vos sustentarei a vós outros e a vossos filhos. Assim, os consolou e lhes falou ao coração.22José habitou no Egito, ele e a casa de seu pai; e viveu cento e dez anos. 23Viu José os filhos de Efraim até à terceira geração; também os filhos de Maquir, filho de Manassés, os quais José tomou sobre seus joelhos. 24Disse José a seus irmãos: Eu morro; porém Deus certamente vos visitará e vos fará subir desta terra para a terra que jurou dar a Abraão, a Isaque e a Jacó. 25José fez jurar os filhos de Israel, dizendo: Certamente Deus vos visitará, e fareis transportar os meus ossos daqui. 26Morreu José da idade de cento e dez anos; embalsamaram-no e o puseram num caixão no Egito.
"""
# Example input text

# Parse the verses
parsed_verses = parse_verses(text,'Gênesis','50')
print(parsed_verses)