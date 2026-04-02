# This is the PL/I built-in function library.
# These functions are named with ALL CAPS for compatibility with PL/I.

# Import useful modules
from decimal import Decimal
import string
import math
import cmath
from datetime import datetime

def ABS(x): return abs(x)

def ACOS(x):
    if isinstance(x, complex):
        return cmath.acos(x)
    else:
        return math.acos(x)

def ADD(x, y): return x + y

def ADDR(x): pass

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

class _Collator:
    pass

_CollationString = _Collator()

def COLLATE(x):
	return _CollationString

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

def EMPTY(x): raise NotImplementedError('Restricted')

def EVERY(x):
    for e in x:
      if not e: return False  
    return True

def EXP(x):
    if isinstance(x, complex):
        return cmath.exp(x, 2)
    else:
        return math.exp(x, 2)

def EXPONENT(x): pass

def FILEOPEN(x): pass

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

def HBOUND(x): pass

def HIGH(x): pass

def IDENTICAL(x): pass

def INDEX(x): pass

def ISOCHAR(x): pass

def LBOUND(x): pass

def LENGTH(x): pass

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

def LOW(x): pass

def LTRIM(x): return lstrip(x)

def MAX(x, y): return max(x, y)

def MAXLENGTH(x): return len(x)

def MIN(x, y): return min(x, y)

def MOD(x): pass

def MULTIPLY(x): return x * y

def NULL(x):
    return None

def OFFSET(x): pass

def ONCODE(x): raise NotImplementedError('Conditions')

def ONFILE(x): raise NotImplementedError('Conditions')

def ONKEY(x): raise NotImplementedError('Conditions')

def ONSOURCE(x): raise NotImplementedError('Conditions')

def PAGENO(x): raise NotImplementedError('Printing')

def POINTER(x): pass

def PROD(x, y): pass

def REFERENCE(x): pass

def REVERSE(x): return x.reversed()

def ROUND(x):
    if isinstance(x, Decimal):
        return x.quantize(Decimal(1), rounding=ROUND_HALF_EVEN)
    else:
        return round(x)

def RTRIM(x): return rstrip(x)

def SEARCH(x): pass

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

def SUBSTR(x): pass

def SUBTRACT(x, y): return x - y

def SUM(x): pass

def TALLY(x): pass

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

def TRANSLATE(x): pass

def TRIM(x): return strip(x)

def TRUNC(x):
    if isinstance(x, Decimal):
        return x.quantize(Decimal(1), rounding=ROUND_DOWN)
    else:
        return trunc(x)

def UNSPEC(x): pass

def VALID(x): pass

def VERIFY(x): pass

