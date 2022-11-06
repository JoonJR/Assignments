class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons)

    def print_info(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        print("There are", len(self.persons), "in the room"
              "and their combined height is", total_height, 'cm')
        for person in self.persons:
            print(person.name, 'is', person.height)

    def tallest(self):
        tallest_person = None
        height_of_tallest = 0
        for person in self.persons:
            if tallest_person is None or person.height > height_of_tallest:
                tallest_person = person
                height_of_tallest = person.height

        return tallest_person

    def remove_tallest(self):
        tallest_person = self.tallest()

        if tallest_person:
            self.persons.remove(tallest_person)

        return tallest_person


room = Room()

print("Is the room empty?", room.is_empty())
print("The tallest is", room.tallest())

room.add(Person('Joona', 184))
room.add(Person('Jouni', 170))
room.add(Person('Jaakko', 165))
room.add(Person('Jenna', 176))
room.add(Person('Jarkko', 174))

print()

print("Is the room empty?", room.is_empty())
print("The tallest is", room.tallest())
room.print_info()

print()

removed = room.remove_tallest()
print('removed from the room', removed.name)
room.print_info()