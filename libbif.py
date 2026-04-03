# This is the PL/I Subset G built-in function library.
# These functions are named with ALL CAPS for compatibility with PL/I.

# Import useful modules
from decimal import Decimal
import string
import math
import cmath
from datetime import datetime

class _Collator:
    pass

_collation_string = _Collator()

# Return True if characters are consecutive
def _consecutive(x):
    for i in range(1, len(x)):
        if ord(x[i -1]) + 1 != ord(x[i]): return False
    return True

def ABS(x): return abs(x)

def ACOS(x):
    if isinstance(x, complex):
        return cmath.acos(x)
    else:
        return math.acos(x)

def ADD(x, y): return x + y

def ADDR(x): raise NotImplementedError('Allocation')

def ASIN(x):
    if isinstance(x, complex):
        return cmath.asin(x)
    else:
        return math.asin(x)

def ATAN(x):
    if isinstance(x, complex):
        return cmath.atan(x)
    else:
        return math.atan(x)

def ATAND(x): return ATAN(x) * 180.0 / math.pi

def ATANH(x):
    if isinstance(x, complex):
        return cmath.atanh(x)
    else:
        return math.atanh(x)

def BINARY(x, precision=None, scale=None): raise NotImplementedError('Conversion')

def BIT(x): raise NotImplementedError('Conversion')

def BOOL(x): raise NotImplementedError('Conversion')

def CEIL(x):
    if isinstance(x, Decimal):
        return x.quantize(Decimal(1), rounding=ROUND_CEILING)
    else:
        return ceil(x)

def CHARACTER(x, y): raise NotImplementedError('Conversion')

def COLLATE(x):
	return __collation_string

def COPY(x, n): return x * n

def COS(x):
    if isinstance(x, complex):
        return cmath.cos(x)
    else:
        return math.cos(x)

def COSH(x):
    if isinstance(x, complex):
        return cmath.cosh(x)
    else:
        return math.cosh(x)

def COSD(x): return COS(x) * 180.0 / math.pi

def CURRENTSIZE(s): return len(s)

def DATE(x): return DATETIME()[2:8]

def DATETIME(x):
    dt = datetime.now()
    return dt[0:4] \
      + dt[5:7] \
      + dt[8:10] \
      + dt[11:13] \
      + dt[14:16] \
      + dt[17:19] \
      + dt[21:]

def DECIMAL(x): raise NotImplementedError('Conversion')

def DIMENSION(a, d = None):
    if (d == None): d = 1
    if (d != 1):
        raise NotImplementedError('Multidimensional')
    return len(d)

def DIVIDE(x, y): return x / y

def EDIT(x): raise NotImplementedError()

def EMPTY(x): raise NotImplementedError('Allocation')

def EVERY(x):
    for e in x:
      if not e: return False
    return True

def EXP(x):
    if isinstance(x, complex):
        return cmath.exp(x, 2)
    else:
        return math.exp(x, 2)

def EXPONENT(x): raise NotImplementedError()

def FILEOPEN(x): return not x.closed

def FIXED(x):
    if isinstance(x, int):
        return x
    else:
        return Decimal(x)

def FLOAT(x): return float(x)

def FLOOR(x):
    if isinstance(x, Decimal):
        return x.quantize(Decimal(1), rounding=ROUND_FLOOR)
    else:
        return floor(x)

def HBOUND(a, d = None):
    if (d == None): d = 1
    if (d != 1):
        raise NotImplementedError('Multidimensional')
    return len(d)

def HIGH(x, n): return chr(0x1FFFFF) * n

def IDENTICAL(x, y): return x == y

def INDEX(haystack, needle, n=1):
    n -= 1
    if needle is _collation_string and haystack is _collation_string:
        return 1 if n == 0 else 0
    elif needle is _collation_string:
        return 0
    elif haystack is _collation_string:
        if not _consecutive(needle):
            return 0
        else:
            return ord(needle[0]) + 1

    else:
        return haystack.find(needle) + 1

def ISOCHAR(hi, mid1=None, mid2=None, lo=None):
    if mid1 is None:
        return chr(hi)
    elif mid2 is None:
        return chr(hi * 16 + mid1)
    else:
        return chr(256 * 256 * 256 * hi
                  + 256 * 256 * mid1
                  + 256 * mid2
                  + lo)

def LBOUND(a, d = None):
    if (d == None): d = 1
    if (d != 1):
        raise NotImplementedError('Multidimensional')
    return 0

def LENGTH(x): return len(x)

def LINENO(x): raise NotImplementedError('Printing')

def LOG10(x):
    if isinstance(x, complex):
        return cmath.log(x, 10)
    else:
        return math.log(x, 10)

def LOG2(x):
    if isinstance(x, complex):
        return cmath.log(x, 2)
    else:
        return math.log(x, 2)

def LOG(x):
    if isinstance(x, complex):
        return cmath.log(x)
    else:
        return math.log(x)

def LOW(x, n): return chr(0x000000) * n

def MAX(x, y): return max(x, y)

def MAXLENGTH(x): return len(x)

def MIN(x, y): return min(x, y)

def MOD(x): return x % y

def MULTIPLY(x): return x * y

def NULL(x):
    return None

def OFFSET(x): raise NotImplementedError('Allocation')

def ONCODE(x): raise NotImplementedError('Conditions')

def ONFILE(x): raise NotImplementedError('Conditions')

def ONKEY(x): raise NotImplementedError('Conditions')

def ONSOURCE(x): raise NotImplementedError('Conditions')

def PAGENO(x): raise NotImplementedError('Printing')

def POINTER(x): raise NotImplementedError('Allocation')

def PROD(x, y):
    result = 1
    for elem in x:
        result *= elem
    return result

def REVERSE(x): return x.reversed()

def ROUND(x):
    if isinstance(x, Decimal):
        return x.quantize(Decimal(1), rounding=ROUND_HALF_EVEN)
    else:
        return round(x)

def SEARCH(haystack, needle, n=1):
    n -= 1
    result = -1
    for ch in needle:
        found = INDEX(haystack, needle, n)
        if found >= 0 and found < result: result = found
    return result

def SIGN(x):
    sgn = -1 if x < 0 else (1 if x > 0 else 0)
    if isinstance(x, Decimal):
        return Decimal(sgn)
    else:
        return sgn

def SIN(x):
    if isinstance(x, complex):
        return cmath.sin(x)
    else:
        return math.sin(x)

def SIND(x): return SIN(x) * 180.0 / math.pi

def SINH(x):
    if isinstance(x, complex):
        return cmath.sinh(x)
    else:
        return math.sinh(x)

def SOME(x):
    for e in x:
      if e: return True
    return False

def SQRT(x):
    if isinstance(x, Decimal):
        return x.sqrt()
    elif isinstance(x, complex):
        return cmath.sqrt(x)
    else:
        return math.sqrt(x)

def STRING(x): return str(x)

def SUBSTR(x, start, length=None):
    if not instanceof(x, str): raise NotImplementedError('Bit strings')
    start -= 1
    if length is None:
        return x[start:start+length-1]
    else:
        return x[start:]

def SUBTRACT(x, y): return x - y

def SUM(x):
    result = 0
    for elem in x:
        result += elem
    return result

def TALLY(haystack, needle):
    result = 0
    start = 1
    while True:
        n = INDEX(haystack, needle, n)
        if n == 0: return result

def TAN(x):
    if isinstance(x, complex):
        return cmath.tan(x)
    else:
        return math.tan(x)

def TAND(x): return TAN(x) * 180.0 / math.pi

def TANH(x):
    if isinstance(x, complex):
        return cmath.tanh(x)
    else:
        return math.tanh(x)

def TIME(x): return DATETIME()[8:]

def TRANSLATE(x, frm, to):
    table = str.maketable(frm, to)
    return x.translate(table)

def TRIM(x):
    if x is _collation_string:
        return _collation_string
    else:
        return strip(x)

def TRUNC(x):
    if isinstance(x, Decimal):
        return x.quantize(Decimal(1), rounding=ROUND_DOWN)
    else:
        return trunc(x)

def UNSPEC(x): raise NotImplementedError()

def VALID(x): raise NotImplementedError()

def VERIFY(x): raise NotImplementedError('Allocation')

# Extension functions

def LTRIM(x):
    if x is _collation_string:
        return _collation_string
    else:
        return lstrip(x)

def RTRIM(x):
    if x is _collation_string:
        return _collation_string
    else:
        return rstrip(x)

def RANK(x): return 1

def INF(): math.inf

def NAN(): math.nan

def ISINF(): math.isinf

def ISNAN(): math.isnan

