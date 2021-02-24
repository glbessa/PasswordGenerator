import string
import sys
import secrets
import argparse

def set_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--lenght', type=int, default=8)
    ap.add_argument('-ex', '--exceptions', type=str, help='Exceptions :P', nargs='*', default=[])
    ap.add_argument('--no-special', action='store_false', help='No special caracteres in the key')
    ap.add_argument('--no-lower', action='store_false')
    ap.add_argument('--no-upper', action='store_false')
    ap.add_argument('--no-number', action='store_false')
    ap.add_argument('--no-char', action='store_false')
    return vars(ap.parse_args())

def upperletters():
    return string.ascii_uppercase

def lowerletters():
    return string.ascii_lowercase

def digits():
    return string.digits

def specialsymbols():
    symbols = string.punctuation
    
    invalidsymbols = ["'", '"'] #',', '.', ':', ';', '`', '~']
    
    for i in invalidsymbols:
        symbols = symbols.replace(i, '')
    return symbols

def integrator(numbers=True, char=True, upper=True, lower=True, special=True, exceptions=''):
    validkeys = ''
    if numbers:
        validkeys += validkeys+digits()
    if char == False:
        upper = False
        lower = False
    if upper:
        validkeys += upperletters()
    if lower:
        validkeys += lowerletters()
    if special:
        validkeys += specialsymbols()
    for i in exceptions:
        validkeys = validkeys.replace(i, '')

    return validkeys

def generate(keys, lenght):
    return ''.join(secrets.choice(keys) for i in range(lenght))

if __name__ == '__main__':
    '''
    options = {'--no-digits':return digits=False, '--no-upper':return upper=False, '--no-lower': return lower=False, '--no-special':return special=False, '--exceptions':return sys.argv.split()[sys.argv.split().index('--exceptions')+1]}
    keys = ''
    for i in options[0:4]:
        if i in sys.argv:
            keys.join(integrator(digits, upper, lower, special))
   '''
    '''
    n, u, l, s = True, True, True, True
    e = ''    

    if '--no-digits' in sys.argv:
        n = False
    if '--no-upper' in sys.argv:
        u = False
    if '--no-lower' in sys.argv:
        l = False
    if '--no-special' in sys.argv:
        s = False
    #if '--exceptions' in sys.argv:
    #    e = sys.argv[(sys.argv.index('--exceptions')+1)]
    '''

    args = set_arguments()

    print(generate(integrator(args['no_number'], args['no_char'], args['no_upper'], args['no_lower'], args['no_special'], args['exceptions']), args['lenght']))
