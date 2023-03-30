#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from model import Product, User, Category
classes = {"Products" : Product, "User" : User, "Category": Category}

class APP(cmd.Cmd):
    """how to create the objects interactively """
    prompt = "<myAPP>"

    def do_quit(self, command):
        """exit the APP console"""
        exit()
    def emptylie(self):
        """overrides the cmd emptyline method """
        pass
    def do_create(self, arg):
        """creates an instance of a class"""
        classlist = arg.split()
        if len(arg) == 0:
            print("***Class missing***")
            return
        elif classlist[0] not in classes:
            print("***Classs does not exist***")
        instance = classlist[0]()
        if len(classlist) > 1:
            Dic = {}
            for item in classlist[1:]:
                if "=" not in item:
                    return None
                L = item.split("=")
                k, v = L[0], L[1]
                Dic[k] = v
            for key in Dic:
                setattr(instance, key, D[key])
        instance.save()
        print(f"{instance.id} : {instance.name}")

if __name__ == '__main__':
        MyCmd().cmdloop()
