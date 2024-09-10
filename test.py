import json

# Função para ler o texto e converter em dicionário
def parse_bible_text(file_path):
    bible_data = {"version": "ARA", "books": {}}
    current_book = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Exemplo de linha: Genesis 1:1 No princípio, criou Deus os céus e a terra.
            parts = line.split(' ', 2)
            if len(parts) < 3:
                continue  # Linha inválida, pular

            book_name = parts[0]
            chapter_verse = parts[1].split(':')
            if len(chapter_verse) != 2:
                continue  # Formato inválido, pular

            chapter = chapter_verse[0]
            verse = chapter_verse[1]
            text = parts[2].strip()

            # Inicializar o livro se não existir
            if book_name not in bible_data["books"]:
                bible_data["books"][book_name] = {}

            # Inicializar o capítulo se não existir
            if chapter not in bible_data["books"][book_name]:
                bible_data["books"][book_name][chapter] = {}

            # Adicionar o versículo
            bible_data["books"][book_name][chapter][verse] = text

    return bible_data

# Caminho para o arquivo de texto
file_path = 'bible_text.txt'

# Criar o dicionário e salvar como JSON
bible_data = parse_bible_text(file_path)

# Escrever o JSON em um arquivo
with open('bible_ara.json', 'w', encoding='utf-8') as f:
    json.dump(bible_data, f, ensure_ascii=False, indent=4)

print("Arquivo JSON criado com sucesso!")
