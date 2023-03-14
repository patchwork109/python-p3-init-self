#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        print(name)
        self.breed = breed
        print(breed)

fido = Dog("Fido", "Lab")
fido.name
fido.breed
