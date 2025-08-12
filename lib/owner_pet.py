class Owner:
    def __init__(self, name):
        # Ensure name is a string
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

    def pets(self):
        # Return all Pet instances that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Ensure the argument is a Pet instance
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        # Return the pets sorted by their name
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Ensure name is a string
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.pet_type = pet_type

        # Validate owner if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")
        self.owner = owner

        # Store the instance in Pet.all
        Pet.all.append(self)
