"""โปรแกรมบวกเลขอย่างง่าย - PyJen005"""
import sys


def add(a, b):
    """คืนค่าผลบวกของ a และ b"""
    return a + b


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) == 2:
        a, b = float(argv[0]), float(argv[1])
    else:
        a, b = 10, 20
    result = add(a, b)
    print(f"{a} + {b} = {result}")
    return result


if __name__ == "__main__":
    main()
