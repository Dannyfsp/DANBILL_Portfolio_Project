#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from Backend.models import Product, User, Category
classes = {"Product" : Product, "User" : User, "Category": Category}

class APP(cmd.Cmd):
    """how to create the objects interactively """
    prompt = " (myAPP) "

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """creates an instance of a class"""
        classlist = arg.split()
        if len(classlist) == 0:
            print("***Class missing***")
            return
        elif classlist[0] not in classes:
            print("***Classs does not exist***")
        instance = classes[classlist[0]]()
        if len(classlist) > 1:
            Dic = {}
            for item in classlist[1:]:
                if "=" not in item:
                    return None
                L = item.split("=")
                k, v = L[0], L[1]
                Dic[k] = v
            for key in Dic:
                setattr(instance, key, Dic[key])
        instance.save()
        print(f"{instance.id} : {instance.name}")

    def do_show(self, arg):
        """We print a instace of a string based on the Id and class"""
        from Backend import Storage
        args = arg.split()
        if len(args) == 0:
            print("** Class Name is Missing **")
            return False
        if args[0] in classes:
            if len(arg) > 1:
                key = args[0] + "." + args[1]
                if key in Storage.all():
                    print(Storage.all()[key])
                else:
                    print("** No instace found**")
            else:
                print("***Id is missing***")
        else :
            print("*** class doesnt")
        
    def do_get(self, arg):
        """we get the class by the id using the get method"""
        from Backend import Storage
        args = arg.split()
        if len(args) == 0:
            print("*** Class Name is Missing ***")
            return False
        if args[0] in classes:
            if len(arg) > 1:
                user = Storage.get(classes[args[0]], args[1])
                print(user.to_dict())
            else :
                print("*** user id is missing ***")
        else:
            print("*** class doesn't exist ***")

if __name__ == '__main__':
        APP().cmdloop()
