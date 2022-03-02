#try raise except
import sys
def read_C():
    try:
        C=float(sys.argv[1])
    except IndexError:
        raise IndexError('Please append value after file name!')
    except ValueError:
        raise ValueError(sys.argv[1],'is invalid!')
    if C< -275.15:
        raise ValueError(sys.argv[1],' is less than minimum')
    return C

try:
    C = read_C()
except (IndexError,ValueError) as e:
    print(e)
F = 9.0*C/5 + 32
print(C,'C is :',F,'F')