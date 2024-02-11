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
classes = ["BaeModel", "User", "State", "City", "Review", "Place", "Amenity"]


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
                for key in objs.keys():
                    dicts[key] = objs[key].to_dict()
                with open("file.json", 'w') as f:
                    json.dump(dicts, f, indent=2)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        cls_name = classes
        if not arg or arg in cls_name:
            objs = storage.all()
            list = []
            for key in objs.keys():
                list.append(str(objs[key].__str__()))
            print(list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance"""
        args = shlex.split(arg)
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
            if key not in objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                try:
                    arg_float = float(args[3])
                    objs[key].__dict__[args[2]] = arg_float
                    objs[key].save()
                except ValueError:
                    try:
                        arg_int = int(args[3])
                        objs[key].__dict__[args[2]] = arg_int
                        objs[key].save()
                    except ValueError:
                        objs[key].__dict__[args[2]] = args[3]
                        objs[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
