__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    even = 0
    odd = 0
    if (len(numbers)==0):
        return 0
    for i in range (len(numbers)):
        if numbers[i] % 2 == 0:
            even+=numbers[i]
        else:
            odd+=numbers[i]
    if (odd == 0):
        return 0
    return even/odd

