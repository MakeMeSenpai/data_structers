#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# binary is "10" leading "0" have no value
# hexdigits is '0123456789abcdefABCDEF' leading "0x" have no value
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
# bases to the power of, for example binary has a base of 2, and every number has
#  a place holder, such as the 5 in 50. So if we have "10" then we would take 2^0 
#  and 2^1 = 2. if it's to the power of zero ignore. example of hexidecimal if we
#  have "0xB2", 16^1 * 11 + 2 = 13


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # incrimentor
    i = 0
    # decrimentor
    d = len(digits) - 1
    # defines our answer
    new_digits = 0

    # while i is greater then 0
    while 0 <= d:
        # checks our digit for strs
        if digits[d].isalpha():
            # turns any letters into our hexidecimal's base of 16
            number = string.ascii_lowercase.index(digits[d].lower()) + 10
        else:
            # turns our digit to int
            number = int(digits[d])

        # Then if digit doesn't equal '0'
        if digits[d] is not '0':
            # take the base (binary: 2) to the power of
            #  placeholder (i) multiplied by number
            opperator = base ** i * number
            # adds our products together
            new_digits += opperator

        # incriments i & decriments d
        i += 1
        d -= 1
    
    # gives us our answer
    return new_digits



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # defines an empty array
    new_number = []
    # while the number is higher then 0
    while 0 < number:
        # take the remainder
        remainder = number % base
        # if the remainder is greater then 9
        if remainder > 9:
            # translate it into ascii for hexidecimal
            letter = string.ascii_lowercase[remainder - 10]
            # put it in the first index of new_number
            new_number.insert(0, letter)
        # else put it in the first index of new_number
        else:
            new_number.insert(0, str(remainder))

        # divide the number by it's base
        number //= base

    # returns our answer as a str
    return ''.join(new_number)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
