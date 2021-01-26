"""A collection of tools that can be used in the Jupyter notebooks."""


import sympy as sy


def hankel1(angular_momentum: sy.Symbol, x: sy.Symbol) -> sy.Expr:
    x_squared = x ** 2
    return sy.Piecewise(
        (
            1,
            sy.Eq(angular_momentum, 0),
        ),
        (
            1 + x_squared,
            sy.Eq(angular_momentum, 1),
        ),
        (
            9 + x_squared * (3 + x_squared),
            sy.Eq(angular_momentum, 2),
        ),
        (
            225 + x_squared * (45 + x_squared * (6 + x_squared)),
            sy.Eq(angular_momentum, 3),
        ),
        (
            1575 + x_squared * (135 + x_squared * (10 + x_squared)),
            sy.Eq(angular_momentum, 4),
        ),
    )


def blatt_weisskopf(
    q: sy.Symbol, q_r: sy.Symbol, angular_momentum: sy.Symbol
) -> sy.Expr:
    return sy.sqrt(
        hankel1(angular_momentum, q) / hankel1(angular_momentum, q_r)
    )
