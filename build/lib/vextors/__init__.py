import math


class Vector:
    """It shall create an instance of an n-dimensional vector.

    Parameters
    ----------

    coordinates : list
        Set of numerical coordinates that defines the position and lenght.
    """

    _lenght = 0

    def __init__(self, coordinates):
        self.coordinates = coordinates

    @property
    def coordinates(self):
        """It shall return the set of coordinates of the vector.
        
        Returns
        -------

        coordinates : list
            Set of numerical coordinates.
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, values):
        """It shall initialize the vector with the passed coordinates
        or change the coordinates to a new set.
        It shall also calculate/update the lenght accordingly.

        Parameters
        ----------

        values : list
            Set of (new) numerical coordinates of the vector.
        """
        self._coordinates = values
        tempSum = 0
        for x in self.coordinates:
            tempSum = tempSum + x ** 2
        self._lenght = math.sqrt(tempSum)

    @property
    def lenght(self):
        """It shall return the lenght of the vector.

        Returns
        -------

        self._lenght : float
            Lenght of the Vector.
        """
        return self._lenght

    def distance(self, v2):
        """It shall return the distance to another vector.
        If the vectors are not of the same dimension, it shall then raise a ValueError.

        Parameters
        ----------
        
        v2 : Vector
            The vector to which the distance shall be calculated.

        Raises
        ------

        ValueError
            Arrays not of the same dimension.
        
        Returns
        -------

        result : float
            The distance between the two vectors.

        """
        if len(self.coordinates) == len(v2.coordinates):
            result = 0
            summe = 0
            for i in range(0, len(v2.coordinates)):
                summe = summe + (self.coordinates[i] - v2.coordinates[i]) ** 2
            result = math.sqrt(summe)
            return result
        else:
            raise ValueError("Arrays not of the same dimension!")

    def dot(self, v2):
        """It shall return the dot product with another vector.
        If the vectors are not of the same dimension, it shall then raise a ValueError.

        Parameters
        ----------

        v2 : Vector
            The vector to be (dot) multiplicated with.
        
        Raises
        ------

        ValueError
            Arrays not of the same dimension.

        Returns
        -------
        v3 : Vector
            The resulting vector of the dot product.
        """
        if len(self.coordinates) == len(v2.coordinates):
            summe = 0
            for i in range(0, len(v2.coordinates)):
                summe = summe + (self.coordinates[i] * v2.coordinates[i])
            return summe
        else:
            raise ValueError("Arrays are not of the same dimension")

    def cross(self, v2):
        """It shall return the cross product with another vector. 
        If the vectors are not of the same dimension, it shall then raise a ValueError.
        If the vectors are not defined in R^3, it shall then raise a ValueError.

        Parameters
        ----------
            
        v2 : Vector
            The vector to be (cross) multiplicated with.

        Raises
        ------

        ValueError
            Arrays not of the same dimension.
        
        ValueError
            Arrays not defined in R^3.

        
        Returns
        -------
        
        v3 : Vector
            The resulting vector of the cross product.
        
        """
        if len(self.coordinates) == len(v2.coordinates):
            if len(v2.coordinates) == 3:
                v3 = list((0, 0, 0))
                v3[0] = (
                    self.coordinates[1] * v2.coordinates[2]
                    - self.coordinates[2] * v2.coordinates[1]
                )
                v3[1] = (
                    self.coordinates[2] * v2.coordinates[0]
                    - self.coordinates[0] * v2.coordinates[2]
                )
                v3[2] = (
                    self.coordinates[0] * v2.coordinates[1]
                    - self.coordinates[1] * v2.coordinates[0]
                )
                return Vector(v3)
            else:
                raise ValueError("Cross Product implemented for R^3")
        else:
            raise ValueError("Arrays are not of the same dimension")
