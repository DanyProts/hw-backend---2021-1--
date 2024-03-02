from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    newdict={}
    for i in d:
        newdict[d[i]]=i
    return newdict


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    newdict2={}
    for i in d:
        newdict2[d[i]]=[]
    for i in d:
        newdict2[d[i]].append(i)
    return newdict2


