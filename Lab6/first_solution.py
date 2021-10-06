import math
from typing import Callable, List


class DistanceFuncs:
    def calc_distance(
        self, point_a: List[float], point_b: List[float], dist_func: Callable, /
    ) -> float:
        """Calculates distance between two points using the passed dist_func"""
        return dist_func(point_a, point_b)

    @staticmethod
    def euclidean(point_a: List[float], point_b: List[float], /) -> float:
        """
        Calculates Euclidean Distance between two points Example:
        >>> DistanceFuncs.euclidean([1,1],[1,1])
        0.0
        """
        # print("returning something")
        return math.dist(point_a, point_b)

    @staticmethod
    def manhattan_distance(point_a: List[float], point_b: List[float], /):
        """Compute the manhattan_distance between two points"""
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

    @staticmethod
    def jaccard_distance(point_a: List[float], point_b: List[float], /):
        """Compute the jaccard_distance between two points"""
        Union_set = set([])
        intersection_set = set([])
        for a in point_a:
            for b in point_b:
                if a == b:
                    intersection_set.add(a)
        for a in point_a:
            Union_set.add(a)
        for b in point_b:
            Union_set.add(b)
        return 1 - (len(intersection_set) / len(Union_set))


def main():
    """Demonstrate the usage of DistanceFuncs"""
    Obj = DistanceFuncs()
    print(
        "manhattan_distance = ",
        Obj.calc_distance([2, 2], [1, 1], Obj.manhattan_distance),
    )
    print(
        "jaccard_distance = ", Obj.calc_distance([2, 2], [2, 1], Obj.jaccard_distance)
    )
    print("euclidean_distance = ", Obj.calc_distance([2, 2], [2, 1], Obj.euclidean))


if __name__ == "__main__":
    main()
