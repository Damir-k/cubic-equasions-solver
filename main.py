import math

angle_digits = 4 # точность после запятой для углов
number_digits = 4 # точность после запятой для чисел

def arg(z: complex):
    if z.real == 0:
        if z.imag == 0:
            raise ValueError("arg(0) is undefined")
        if z.imag > 0:
            return 90.0
        return -90.0
    elif z.real > 0:
        return math.degrees(math.atan(z.imag / z.real))
    elif z.real < 0:
        if z.imag > 0:
            return 180.0 - math.degrees(math.atan(-z.imag/z.real))
        elif z.imag < 0:
            return -180.0 + math.degrees(math.atan(-z.imag/z.real))
        else:
            return 180.0
    return 0.0

def text(z: complex | float):
    if type(z) == complex:
        z = complex(round(z.real, number_digits), round(z.imag, number_digits))
        return z.real if not z.imag else z
    if type(z) == float:
        return round(z, number_digits)
    return z

def trig(z: complex, raw_sqrt=False, raw_trig=False):
    argz = arg(z)
    c = math.cos(math.radians(argz))
    s = math.sin(math.radians(argz))
    if raw_sqrt:
        root = f"sqrt({text(abs(z.real))}^2 + {text(abs(z.imag))}^2)"
    else:
        root = f"{text(abs(z))}"
    if raw_trig:
        unit = f"(cos({round(argz, angle_digits)}) + sin({round(argz, angle_digits)})i)"
    else:
        unit = f"({text(c)}{'+' if s > 0 else ''}{text(s)}i)"
    return "*".join([root, unit])

def explain():
    print("\nПервый шаг: Дискриминант")
    print(f"D = q^2 / 4 + p^3 / 27\n  = ({text(q)})^2 / 4 + ({text(p)}^3 / 27)\n  = {text(D)}")
    print("\nВторой шаг: a^3")
    if D.imag == 0:
        print(f"a^3 = -q / 2 + sqrt(D)")
        print(f"  = -{text(q)} / 2 + sqrt({text(D.real)})")
        print(f"  = {-text(q) / 2} + {text(D.real**0.5)}")
        print(f"  = {text(a_cubed)}")
    else:
        print(f"D = {text(D)}")
        if abs(D.real) < 0.000001 or abs(D.imag) < 0.000001:
            print(f"    // очеввидно, arg(D)={round(arg(D), angle_digits)}")
        elif D.real < 0 and D.imag < 0:
            print(f"    // arg(D) = -180 + arctg({text(abs(D.imag))} / {text(abs(D.real))})")
            print(f"    //        = -180 + {round(180 + arg(D), angle_digits)} = {round(arg(D), angle_digits)}")
        elif D.real < 0 and D.imag > 0:
            print(f"    // arg(D) = 180 - arctg({text(abs(D.imag))} / {text(abs(D.real))})")
            print(f"    //        = 180 - {round(180 - arg(D), angle_digits)} = {round(arg(D), angle_digits)}")
        else:
            print(f"    // arg(D) = arctg({text(D.imag)} / {text(D.real)})")
            print(f"    //        = {round(arg(D), angle_digits)}")
        print(f"  = {trig(D, raw_sqrt=True, raw_trig=True)}")
        print(f"  = {trig(D, raw_trig=True)}")
        print(f"\nsqrt(D) = sqrt({text(abs(D))})*(cos({round(arg(D), angle_digits)} / 2) + sin({round(arg(D), angle_digits)} / 2)i)")
        print(f"        = {trig(sqrtD, raw_trig=True)}")
        print(f"        = {trig(sqrtD)}")
        print(f"        = {text(sqrtD)}")
        print("\na^3 = -q / 2 + sqrt(D) =")
        print(f"    = -{text(q)} / 2 + ({text(sqrtD)}) =")
        print(f"    = {text(a_cubed)}")
    print("\nТретий шаг: a1")
    print(f"a^3 = {text(a_cubed)}")
    if abs(a_cubed.real) < 0.000001 or abs(a_cubed.imag) < 0.000001:
        print(f"      // очеввидно, arg(a^3)={round(arg(a_cubed), angle_digits)}")
    elif a_cubed.real < 0 and a_cubed.imag < 0:
        print(f"      // arg(a^3) = -180 + arctg({text(abs(a_cubed.imag))} / {text(abs(a_cubed.real))})")
        print(f"      //          = -180 + {round(arg(a_cubed) + 180, angle_digits)} = {round(arg(a_cubed), angle_digits)}")
    elif a_cubed.real < 0 and a_cubed.imag > 0:
        print(f"      // arg(a^3) = 180 - arctg({text(abs(a_cubed.imag))} / {text(abs(a_cubed.real))})")
        print(f"      //          = 180 - {round(180 - arg(a_cubed), angle_digits)} = {round(arg(a_cubed), angle_digits)}")
    else:
        print(f"      // arg(a^3) = arctg({text(a_cubed.imag)} / {text(a_cubed.real)})")
        print(f"      //          = {round(arg(a_cubed), angle_digits)}")
    print(f"    = {trig(a_cubed, raw_sqrt=True, raw_trig=True)}")
    print(f"    = {trig(a_cubed, raw_trig=True)}")
    print(f"\na1 = cbrt({text(abs(a_cubed))})*(cos({round(arg(a_cubed), angle_digits)} / 3) + sin({round(arg(a_cubed), angle_digits)} / 3)i)")
    print(f"   = {trig(a1, raw_trig=True)}")
    print(f"   = {trig(a1)}")
    print(f"   = {text(a1)}")
    print("\nЧетвертый шаг: b1")
    print("b1 = -p / (3 * a1)")
    print(f"   = -p * conj(a1) / (3 * |a1|)")
    print(f"     // |a1| = sqrt({text(abs(a1.real))}^2 + {text(abs(a1.imag))}^2)")
    print(f"     // |a1| = {text(abs(a1))}")
    print(f"   = {text(-p)} * ({text(a1.conjugate())}) / (3 * {text(abs(a1))})")
    print(f"   = {text(b1)}")
    print("\nПятый шаг: первый корень x1")
    print("x1 = a1 + b1")
    print(f"   = ({text(a1)}) + ({text(b1)})")
    print(f"   = {text(x1)}")
    print("\nШестой шаг: второй корень")
    print(f"a2 = cbrt({text(abs(a_cubed))})*(cos(120 + {round(arg(a_cubed), angle_digits)} / 3) + sin(120 + {round(arg(a_cubed), angle_digits)} / 3)i)")
    print(f"   = {trig(a2, raw_trig=True)}")
    print(f"   = {trig(a2)}")
    print(f"   = {text(a2)}")
    print("b2 = -p / (3 * a2)")
    print(f"   = {text(-p)} * ({text(a2.conjugate())}) / (3 * {text(abs(a2))})")
    print(f"   = {text(b2)}")
    print("\nx2 = a2 + b2")
    print(f"   = ({text(a2)}) + ({text(b2)})")
    print(f"   = {text(x2)}")
    print("\nСедьмой шаг: третий корень")
    if abs(x1.imag) < 0.000001 and abs(x2.imag) < 0.000001:
        print("x3 = -x1 - x2")
        print(f"   = -({text(x1)}) - ({text(x2)})")
        print(f"   = {text(x3)}")
    elif abs(x1.imag) < 0.000001:
        print("x3 = conj(x2)")
        print(f"   = {text(x3)}")
    else:
        print("x3 = conj(x1)")
        print(f"   = {text(x3)}")

if __name__ == "__main__":
    print("Решение кубического уравнения вида (z^3 + pz + q = 0)\n")
    p_parts = tuple(map(float, input("Введите вещественную и мнимую части p через пробел:\n").split()))
    p = complex(p_parts[0], p_parts[1])

    q_parts = tuple(map(float, input("Введите вещественную и мнимую части q через пробел:\n").split()))
    q = complex(q_parts[0], q_parts[1])

    D = q**2 / 4 + p**3 / 27
    sqrtD = D ** 0.5
    a_cubed = -q / 2 + sqrtD

    a1 = a_cubed ** (1/3)
    b1 = -p / (3 * a1)
    x1 = a1 + b1

    root_of_unity = -1/2 + 3**0.5 * 1j/2
    a2 = root_of_unity * a1
    b2 = -p / (3 * a2)
    x2 = a2 + b2

    x3 = -x1 - x2

    if input("Написать объяснение?[y/n]\n") != "n":
        explain()

    print(f"\nКорни многочлена x^3 + ({text(p)})x + ({text(q)}): ")
    print(f"x1 = {text(x1)}")
    print(f"x2 = {text(x2)}")
    print(f"x3 = {text(x3)}")