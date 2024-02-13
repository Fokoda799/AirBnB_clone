#!/usr/bin/python3
"""Console Model contains the entry point
of the command interpreter"""
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json
import shlex

classes = ["BaseModel", "User", "State", "City", "Review", "Place", "Amenity"]


def create_instance(class_name):
    """Function to create instances"""
    classes_mapping = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Place": Place(),
        "Review": Review(),
    }

    if class_name in classes_mapping:
        inst = classes_mapping[class_name]
        inst.save()
        print(inst.id)


class HBNBCommand(Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_EOF(self, arg):
        """Quit command"""
        return True

    def do_create(self, arg):
        """Creates a new instance"""
        cls_name = classes
        if not arg:
            print("** class name missing **")
        elif arg not in cls_name:
            print("** class doesn't exist **")
        else:
            create_instance(arg)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()
        objs = storage.all()
        cls_name = classes
        if not args:
            print("** class name missing **")
        elif args[0] not in cls_name:
            print("** class doesn't exist **")
            print(args)
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f'{args[0]}.{args[1]}'
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        objs = storage.all()
        cls_name = classes
        if not args:
            print("** class name missing **")
        elif args[0] not in cls_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f'{args[0]}.{args[1]}'
            if key in objs:
                del objs[key]
                dicts = {}
                for k in objs.keys():
                    dicts[k] = objs[k].to_dict()
                with open("file.json", 'w') as f:
                    json.dump(dicts, f, indent=2)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        cls_name = classes
        if not arg:
            objs = storage.all()
            for key in objs.keys():
                print(objs[key])
        elif arg in cls_name:
            objs = storage.all()
            instances = [str(obj) for obj in objs.values() if type(obj).__name__ == arg]
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance"""
        args = shlex.split(arg)
        objs = storage.all()
        cls_name = classes
        if len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            try:
                value = float(args[3])
            except ValueError:
                try:
                    value = int(args[3])
                except ValueError:
                    value = args[3]

            key = f'{args[0]}.{args[1]}'
            if key in objs:
                setattr(objs[key], args[2], value)
                objs[key].save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
