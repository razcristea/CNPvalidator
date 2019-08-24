from wtforms.validators import ValidationError

def validate_CNP(form,field):
    if field.data.isdigit():
        if len(field.data) != 13:
            raise ValidationError('CNP-ul trebuie sa aiba 13 caractere!')
        if field.data.startswith('0'):
            raise ValidationError('CNP-ul nu poate sa inceapa cu cifra 0.')
        cnp_check = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
        k = 0
        for i in range(0, len(cnp_check)):
            k += int(field.data[i]) * int(cnp_check[i])
        if k % 11 == int(field.data[12]):
            return True
        elif k % 11 == 10 and int(field.data[12]) == 1:
            return True
        else:
            raise ValidationError('CNP-ul introdus {} nu este valid.'.format(field.data))
    else:
        raise ValidationError('CNP-ul trebuie sa contina doar cifre!')




# s este un dictionar care contine sexul, cetatenia si secolul nasterii, in functie de prima cifra a CNP-ului
status = {
    1: ('masculin', 'roman', 19), 2: ('feminin', 'roman', 19), 3: ('masculin', 'roman', 18),
    4: ('feminin', 'roman', 18), 5: ('masculin', 'roman', 20), 6: ('feminin', 'roman', 20),
    7: ('masculin', 'rezident', ''), 8: ('feminin', 'rezident', ''), 9: ('', 'strain', '')
}
# l este un dictionar care contine lunile anului
luna = {
    '01': 'ianuarie', '02': 'februarie', '03': 'martie', '04': 'aprilie', '05': 'mai', '06': 'iunie',
    '07': 'iulie', '08': 'august', '09': "septembrie", '10': 'octombrie', '11': 'noiembrie', '12': 'decembrie'
}
# j este un dictionar care contine judetele si codul loc corespondent
judet = {
    '01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita-Nasaud',
    '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras-Severin', '12': 'Cluj',
    '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj',
    '19': 'Harghita', '20': 'Hunedoara', '21': 'Ialomita', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures',
    '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu-Mare', '31': 'Salaj',
    '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea', '37': 'Vaslui',
    '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti Sector 1', '42': 'Bucuresti Sector 2',
    '43': 'Bucuresti Sector 3', '44': 'Bucuresti Sector 4', '45': 'Bucuresti Sector 5', '46': 'Bucuresti Sector 6',
    '51': 'Calarasi', '52': 'Giurgiu'
}
