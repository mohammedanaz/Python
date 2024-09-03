def count_letter(st):
    dct = {}
    for x in st:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] =1
        
    for letter, count in dct.items():
        print(f'{letter} - {count}')

count_letter('Happy')