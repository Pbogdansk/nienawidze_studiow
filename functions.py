def N0(ksi, eta):
    return 0.25 * (1 - ksi) * (1 - eta)


def N1(ksi, eta):
    return 0.25 * (1 + ksi) * (1 - eta)


def N2(ksi, eta):
    return 0.25 * (1 + ksi) * (1 + eta)


def N3(ksi, eta):
    return 0.25 * (1 - ksi) * (1 + eta)