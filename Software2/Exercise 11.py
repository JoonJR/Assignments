#Exercise 1
print("******************Exercise1******************")
class Publication():
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Name of the book: {self.name}\nAuthor: {self.author}\nPage count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Name of the magazine: {self.name}\nChief editor: {self.chief_editor}")

pubs = []
pubs.append(Book("Compartment No. 6", "Rosa Liksom", 192))
pubs.append(Magazine("Aku Ankka", "Aki Hyyppä"))
for i in pubs:
    print("---------------------")
    i.print_information()

#Exercise2
print("******************Exercise2******************")


class Car:

    def __init__(self, reg, max_speed, curr_speed=0, distance_travelled=0):
        self.reg = reg
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.distance_travelled = distance_travelled

    def accelerate(self, change_of_speed):
        if self.max_speed >= self.curr_speed + change_of_speed >= 0:
            self.curr_speed = self.curr_speed + change_of_speed
        elif self.max_speed < self.curr_speed + change_of_speed:
            self.curr_speed = self.max_speed
        elif self.curr_speed + change_of_speed < 0:
            self.curr_speed = 0
        return self.curr_speed

    def drive(self, number_of_hours):
        self.distance_travelled += number_of_hours * self.curr_speed


class Electric(Car):

    def __init__(self, reg, max_speed, battery):
        super().__init__(reg, max_speed)
        self.battery = battery

    def print_distance_travelled(self):
        print("Travelled distance is " + str(self.distance_travelled))


class Gasoline(Car):

    def __init__(self, reg, max_speed, tank):
        super().__init__(reg, max_speed)
        self.tank = tank

    def print_distance_travelled(self):
        print("Travelled distance is " + str(self.distance_travelled))

electriccar = Electric("ABC-15", 100, 52.5)
gascar = Gasoline("ACD-123", 165, 32.3)
electriccar.accelerate(80.)
electriccar.drive(3.)
gascar.accelerate(120)
gascar.drive(3.)
electriccar.print_distance_travelled()
gascar.print_distance_travelled()