#!/usr/bin/python3
"""Module containing just one class definition for Models"""
import json
import csv


class Base:
    """Class Model definition
    Private class atributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Public class instance constructor
        Inicilizating atributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """
        obj_dict = []
        if list_objs:
            for obj in list_objs:
                obj_dict.append(obj.to_dictionary())

        with open(cls.__name__ + '.json', 'w') as myfile:
            myfile.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """
        if cls.__name__ == 'Rectangle':
            aux = cls(1, 1)
        elif cls.__name__ == 'Square':
            aux = cls(1)

        aux.update(**dictionary)
        return aux

    @classmethod
    def load_from_file(cls):
        """ Load file to instances """
        try:
            with open(cls.__name__ + '.json', 'r') as myfile:
                jsonstr = myfile.read()
                list_dict = Base.from_json_string(jsonstr)
                list_objs = []
                for obj_dict in list_dict:
                    list_objs.append(cls.create(**obj_dict))
                return list_objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to csv """
        file_name = cls.__name__ + '.csv'
        with open(file_name, 'w', encoding='utf-8') as myfile:
            if list_objs is None or len(list_objs) == 0:
                myfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    attrs = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    attrs = ['id', 'size', 'x', 'y']

                filecsv = csv.DictWriter(myfile, fieldnames=attrs)
                for obj in list_objs:
                    filecsv.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load from csv """
        file_name = cls.__name__ + '.csv'
        try:
            with open(file_name, 'r', encoding='utf-8') as myfile:
                if cls.__name__ == 'Rectangle':
                    attrs = ['id', 'width', 'height', 'x', 'y']
                else:
                    attrs = ['id', 'size', 'x', 'y']

                csvdict = csv.DictReader(myfile, fieldnames=attrs)
                list_dict = []
                for row in csvdict:
                    newdict = {}
                    for key, val in row.items():
                        newdict[key] = int(val)
                    listdict.append(newdict)

                saved = []
                for obj in listdict:
                    saved.append(cls.create(**obj))
                return saved
        except IOError:
            return []
