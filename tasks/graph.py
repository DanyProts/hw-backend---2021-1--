from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__

class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root


    def dfs(self) -> list[Node]:
        complete = set()
        sp = []
        def dfs1(node : Node) -> None:
            if node in complete:
                return
            complete.add(node)
            sp.append(node)
            for next in node.outbound:
                dfs1(next)
        dfs1(self._root)
        return sp



    def bfs(self) -> list[Node]:
        complete = set()
        sp = []
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            if node in complete:
                continue
            complete.add(node)
            sp.append(node)
            for next in node.outbound:
                if next not in complete:
                    queue.append(next)
        return sp

