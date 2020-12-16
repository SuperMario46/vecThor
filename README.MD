# Vectors

vextors is a Python library for dealing with basic operation between vectors on R^N

## Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install vextors.

```bash
pip install vextors
```

## Usage

```python
from vextors import Vector


v1 = Vector([1,2,3]) # defines a three-dim vector

v2 = Vector([4,5,6])

v1.lenght # returns the lenght of the vector

v1.dot(v2) # returns the scalar multiplication of the two vectors

v1.cross(v2) # returns the cross product of the two vectors ( v1 x v2 )

v1.distance(v2) #returns the distance between the two vectors

```
## License
MIT License


