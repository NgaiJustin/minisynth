import z3


def solve(phi):
    s = z3.Solver()
    s.add(phi)
    s.check()
    return s.model()


if __name__ == "__main__":
    x = z3.BitVec("x", 8)
    slow_expr = x * 1
    hole = z3.BitVec("hole", 8)
    fast_expr = x << hole
    formula = z3.ForAll([x], slow_expr == fast_expr)

    print(slow_expr == fast_expr)
    print(solve(formula))
