from pdfminer.high_level import extract_text

text = extract_text('6cbf859a-80e3-4057-8902-4a38ba13886a.pdf')
text = text.split(sep='\n')
text = [i for i in text if i]
for i in text:
    if ':' not in i:
        text.remove(i)
text = text[:-1]

keys = [i.split(sep=':')[0] for i in text]
values = [i.split(sep=':')[1] for i in text]

dictionary = dict(zip(keys, values))
print(dictionary)
