# 0x0C. Python - Almost a circle

## Technologies
* C files are compiled using `gcc 9.3.0`
* C files are written according to the standard `C89 with GNU extensions`
* Shell scripts tested using `bash`
* Python interpreter `python3 version 3.8.5`
* Python code use `pycodestyle (version 2.8.*)`
* Tested on `Ubuntu 20.04 LTS`

## Tasks
The following files are python scripts, shell scripts and functions in C:

| Filename | Description |
| -------- | ----------- |
| `tests/` | Directory containing unit testing for all the project files. |
| `models/base.py, models/__init__.py` | `models` folder containing `__init__.py` empty file and `base.py` module defining the first class `Base`. |
| `models/rectangle.py` | Class `Rectangle` that inherits from `Base`. |
| `models/rectangle.py` | Update the class `Rectangle` by adding validation of all setter methods and instantiation (id excluded). |
| `models/rectangle.py` | Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the Rectangle instance. |
| `models/rectangle.py` | Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here. |
| `models/rectangle.py` | Update the class `Rectangle`  by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`. |
| `models/rectangle.py` | Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`. |
| `models/rectangle.py` | Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute. |
| `models/rectangle.py` | Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes. |
| `models/square.py` | Class `Square` that inherits from `Rectangle`. |
| `models/square.py` | Update the class `Square` by adding the public getter and setter `size`. |
| `models/square.py` | Update the class `Square` by adding the public method `def update(self, *args, **kwargs):` that assigns attributes. |
| `models/rectangle.py` | Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`. |
| `models/square.py` | Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`. |
| `models/base.py` | Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries` |
| `models/base.py` | Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file. |
| `models/base.py` | Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`. |
| `models/base.py` | Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set. |
| `models/base.py` | Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances. |

### Advanced
| Filename | Description |
| -------- | ----------- |
| `models/base.py` | Update the class `Base` by adding the class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in `CSV`. |
| `models/base.py` | Update the class `Base` by adding the static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangles` and `Squares` using `Turtle graphics module`. |
