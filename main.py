from transliterate import to_cyrillic, to_latin, transliterate
import regax
check = bool(regax.search(r'\p{IsCyrillic}', 'salom'))

def cril_or_latin(text):
    check = bool(regax.search(r'\p{IsCyrillic}', 'salom'))
    if check == True:
        result = to_latin(text)
    else:
        result = to_cyrillic(text)
    return result
savol = input("So'z kiriting")
print(cril_or_latin(savol))
