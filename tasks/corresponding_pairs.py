from typing import TypeVar

__all__ = ("corresponding_pairs",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def corresponding_pairs(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    dek = []
    if (len(arr1)==0 or len(arr2)==0):
        return dek
    mn = min(len(arr1),len(arr2))
    for i in range(mn):
        dek.append((arr1[i],arr2[i]))
    return dek

