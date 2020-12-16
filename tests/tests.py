import pytest
import math
from vector import Vector


class TestVector:
    def test_cross_Product(self):
        """
        Checks if the cross product of two arbitrary vectors
        returns the right answer, otherweise raise AssertError
        """
        v1 = Vector([3, 4, 5])
        v2 = Vector([8, 2, 6])
        result = Vector([14, 22, -26])
        assert v1.cross(v2).coordinates == result.coordinates, "Cross Product fails"

    def test_dot(self):
        """
        Checks if the dot product of two arbitrary vectors
        returns the right answer, otherweise raise AssertError
        """
        v1 = Vector([1, 2, 3])
        v2 = Vector([3, 4, 5])
        result = 26
        assert v1.dot(v2) == result, "Dot Product fails"

    def test_distance(self):
        """
        Checks if distance between two arbitrary vectors
        returns the right answer, otherweise raise AssertError
        """
        v1 = Vector([4, 5, 6])
        v2 = Vector([7, 7, 10])
        result = math.sqrt(29)
        assert v1.distance(v2) == result, "Distance Attribute Fails"

    def test_lenght(self):
        """
        Checks if the lenght of an arbitrary vector
        is correctly implemented, otherweise raise AssertError
        """
        v1 = Vector([1, 2, 3])
        result = math.sqrt(14)
        assert v1.lenght == result, "Lenght Attribute fails"

    def test_dot_different_size(self):
        """
        Checks if the dot product of two arrays of different size
        returns a ValueError
        """
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2])
        try:
            assert (
                v1.dot(v2) == ValueError
            ), "Dot Product between two vectors of different size should return a ValueError"
        except ValueError:
            return True

    def test_distance_different_size(self):
        """
        Checks if the distance between two arrays of different size
        returns a ValueError
        """
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2])
        try:
            assert (
                v1.distance(v2) == ValueError
            ), "Distance betweeen two vectors of different size should return a ValueError"
        except ValueError:
            return True

    def test_cross_different_size(self):
        """
        Checks if the cross product of two arrays of different size
        returns a ValueError
        """
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2])
        try:
            assert (
                v1.cross(v2) == ValueError
            ), "Cross product of two vectors of different size should return a ValueError"
        except ValueError:
            return True

    def test_cross_R3(self):
        """
        Checks if the arrays are defined on R^3 for the cross product, otherweise should get ValueError
        """
        v1 = Vector([1, 2, 3, 4])
        v2 = Vector([1, 2, 3, 4])
        try:
            assert (
                v1.cross(v2) == ValueError
            ), "Cross Product of two vectors not defined on R^3 should return a ValueError"
        except ValueError:
            return True
