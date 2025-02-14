# lib/dog.py

approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        self._name = None  
        self._breed = None
        if self._validate_name(name):
            self.name = name
            self.breed = breed  

    def _validate_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            return True
        else:
            print("Name must be string between 1 and 25 characters.")
            return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._validate_name(value):
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
