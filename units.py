'''

Unit conversion by Matt James 2015-04-27

Available Functions:

ft_m(number, units)
    returns the number of meters in a given number of feet
    or visa versa depending on input unit

lbs_kg(number, units)
    returns the number of killograms in a given number of pounds
    or visa versa depending on input unit


example usage:

>>> import units
>>> ft_m(3, ft)
0.9144

>>> ft_m(1, m)
3.28084

>>> lbs_kg(2.5, lbs)
1.13398

>>> lbs_kg(1, kg)
2.20462

'''

def ft_m(number=1, units='ft'):
    '''converts between feet and meters'''
    if number < 0:
        return ValueError('number must be non-negative')

    if units == 'ft':
        return number * .3048

    if units == 'm':
        return number * 3.28084

    return ValueError('not valid units')

def lbs_kg(number=1, units='lbs'):
    '''converts between lbs and kg'''
    if number < 0:
        return ValueError('number must be non-negative')

    if units == 'lbs':
        return number * .453592

    if units == 'kg':
        return number * 2.20462

    return ValueError('not valid units')

if __name__ == '__main__':
    print( '10 feet to meters' )
    print( ft_m(10, 'ft') )
    print( '10 lbs to kg' )
    print( lbs_kg(10, 'lbs') )
    print( '10 meters to feet' )
    print( ft_m(10, 'm') )
    print( '10 kg to lbs' )
    print( lbs_kg(10, 'kg') )
    print( '10 ton to kg' )
    print( lbs_kg(10, 'ton') )
    print( '-10 ton to kg' )
    print( lbs_kg(-10, 'ton') )
