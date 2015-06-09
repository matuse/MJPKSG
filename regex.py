import re

s = 'M'

" This is an example of a compact regular expression "

patternc = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

re.search(patternc, s)

" This is an example of a VERBOSE regular expression"

patternv = '''
^                   # beginning of string
M{0,3}              # thousands - 0 to 3 Ms
(CM|CD|D?C{0,3})	# hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                    #            or 500-800 (D, followed by 0 to 3 Cs)
(XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                    #        or 50-80 (L, followed by 0 to 3 Xs)
(IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                    #        or 5-8 (V, followed by 0 to 3 Is)
$                   # end of string
'''

re.search(patternv, s, re.VERBOSE)

''' Both of the above examples do the same thing, it's just that the VERBOSE
version contains inline documentation in order to explain each step of the
expression explicitly. '''

phonenum = '800-555-1212'

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

phonePattern.search(phonenum).groups()
