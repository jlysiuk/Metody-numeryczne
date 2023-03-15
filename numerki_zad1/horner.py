def horner_result(tab, x: float) -> float:
    """
    Funkcja licząca wartość wielomianu dla podanego x, przy użyciu schematu Hornera
    W(x) = tab[0] + tab[1]*x + tab[2]*x*x + ...
    :param tab: tablica współczynników
    :param x: wartość x
    :return:
    """

    i = len(tab) - 1
    result = tab[i]
    while i > 0:
        i = i - 1
        result = result * x + tab[i]
    return result
