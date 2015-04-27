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
    if units == 'ft':
        return number / .3048

    return number / 3.28084

def lbs_kg(number=1, units='lbs'):
    '''converts between lbs and kg'''
    if units == 'lbs':
        return number / .453592

    return number / 2.20462

if __name__ == '__main__':
    print( '10 feet to meters' )
    print( ft_m(10, 'ft') )
    print( '10 lbs to kg' )
    print( lbs_kg(10, 'lbs') )
    
