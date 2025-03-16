




import re


memes = 'ola marilene a noite tem tainha vinho e muito sexo'


texto_v = re.compile(r'vinho')
texto_s = re.compile(r'sexo')

print(texto_v.search(memes))
print(texto_v.sub('VINHO',memes))

memes = texto_v.sub('VINHO',memes)
print()

print(texto_s.search(memes))
print(texto_s.sub(r'SEXO',memes))


if r'sexo' in memes:
    print('foi')












