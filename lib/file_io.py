def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as text_deck:
        text_deck.write(f'{file_content}')

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as text_deck:
        text_deck.write(f'{append_content}')

def read_file(file_name):
    text_deck = open(f"{file_name}.txt", encoding="utf-8")
    return (text_deck.read())