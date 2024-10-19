from typing import TypeVar

__all__ = ("cartesian_product",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def cartesian_product(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    dek=[]
    if (len(arr1)==0 or len(arr2)==0):
        return dek
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            dek.append((arr1[i],arr2[j]))
    return dek

