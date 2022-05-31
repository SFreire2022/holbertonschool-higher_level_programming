


|`0-lookup.py`|Function that returns the list of available attributes and methods of an object|
|`1-my_list.py`|Write a class MyList that inherits from list|
|`2-is_same_class.py`|Function that returns True if the object is exactly an instance of the specified class ; otherwise False|
|`3-is_kind_of_class.py`|Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False|
|`4-inherits_from.py`|Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False|
|`5-base_geometry.py`|Empty class BaseGeometry|
|`6-base_geometry.py`|Class BaseGeometry (based on 5-base_geometry.py) with a Public instance method: def area(self): that raises an Exception with the message area() is not implemented|
|`7-base_geometry.py`|Class BaseGeometry (based on 6-base_geometry.py). Public instance method: def integer_validator(self, name, value): that validates value:if value is not an integer: raise a TypeError exception, with the message <name> must be an integer. Otherwise: if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0|
|`8-rectangle.py`|Class Rectangle that inherits from BaseGeometry (7-base_geometry.py).Instantiation with width and height: def __init__(self, width, height):width and height must be private. No getter or setter width and height must be positive integers, validated by integer_validator|
|`9-rectangle.py`|Class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)Instantiation with width and height: def __init__(self, width, height):: width and height must be private. No getter or setter ; width and height must be positive integers validated by integer_validator the area() method must be implemented ; print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>|
|`10-square.py`|Class Square that inherits from Rectangle (9-rectangle.py): Instantiation with size: def __init__(self, size):: size must be private. No getter or setter | size must be a positive integer, validated by integer_validator | the area() method must be implemented|
|`11-square.py`|Class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).Instantiation with size: def __init__(self, size):: size must be private. No getter or setter | size must be a positive integer, validated by integer_validator | the area() method must be implemented | print() should print, and str() should return, the square description: [Square] <width>/<height>|
|100-my_int.py|Class MyInt that inherits from int.|
|101-add_attribute.py|Function that adds a new attribute to an object if it’s possible.|
