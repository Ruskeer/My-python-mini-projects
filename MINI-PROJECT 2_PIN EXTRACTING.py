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








poem = """hotstop beautiful in the
dence beujrj and baluga
cute mo boss lol"""

vaga = 'bestie/greatie/insudkjenc'

print(pullpin([poem, vaga]))
