def pullpin(poem):
    secret_codes = []

    for poems in poem:
        secret_code = ''
        

        lines = poems.split("\n")

        for index, line in enumerate(lines):
            words = line.split()

            if len(words) > index:
                secret_code += str(len(words[index]))
            else:
                secret_code += '0'


        secret_codes.append(secret_code)
    return secret_codes








poem = """bayag malaki inutil
big ddd vagine or
orton sige"""

vaga = 'nigga\nhey\nbetlog mo to tho'

print(pullpin([poem, vaga]))
