from random import randint


k = randint(0, 10)
n = randint(5, 20)


class Person:
    id_ = 0

    def __init__(self, floor_start, floor_end) -> None:
        self.id_ += 1
        self.floor_start = floor_start
        self.floor_end = floor_end
        self.top_bot = bool  # True = top, False = bot
        self.floor = 1

        if self.floor_start > self.floor_end:
            self.top_bot = True
        elif self.floor_start < self.floor_end:
            self.top_bot = False
        elif self.floor_start == self.floor_end:
            print(f"Person {self.id_} cannot start and end on the same floor")


class Elevator:

    people = list()
    position = 1
    max_count_people = 5

    def set_passanger(self, passanger: Person):
        self.people.append(passanger)

    def get_passanger(self):
        return self.people

    def delete_passanger(self, passanger: Person):
        if passanger in self.get_passanger():
            self.get_passanger().pop(self.get_passanger().index(passanger))

    def __init__(self, number) -> None:
        self.number = number
        self.create_floors()

    def create_floors(self):
        self.dict_floors = {
            k: list() for k in range(1, self.number + 1)
        }  # k - это этаж v - это информация

    def down_button(self, passanger: Person):
        print(
            f"Лифт поехал верх на {passanger.floor_end} этаж для пассажира с id:{passanger.id_}"
        )
        self.position = passanger.floor_end

    def top_button(self, passanger: Person):
        print(
            f"Лифт поехал вниз на {passanger.floor_end} этаж для пассажира с id:{passanger.id_}"
        )
        self.position = passanger.floor_end

    def check_elevator(self, passanger: Person) -> None:
        # print(passanger, 'PASSANGERфывьтфытвтфьытвфвьытфьвтфы')
        self.dict_floors[passanger.floor_start].append(passanger)
        if self.position in self.dict_floors:
            return self.position

    @classmethod
    def get_max_people(cls):
        return cls.max_count_people

    def enter_elevator(self, passanger: Person):
        try:
            if len(self.get_passanger()) > Elevator.get_max_people():
                raise Exception("Количество вместительности превышает")
        except Exception:
            return False
        else:
            self.set_passanger(passanger=passanger)
            self.call_elevator(passanger=passanger)
            return True

    def call_elevator(self, passanger: Person):
        print(f"Лифт вызвали на {passanger.floor_start} этаж")
        if passanger.top_bot:
            self.top_button(passanger=passanger)
            self.delete_passanger(passanger=passanger)
        else:
            self.down_button(passanger=passanger)
            self.delete_passanger(passanger=passanger)

    def start(self):
        for k, v in self.dict_floors.items():
            # print(self.dict_floors, 'asdasdasdasdasd')
            if not v:
                print(f"Пассажиров нет на {k} этаже")

            else:
                print(v)
                print(f"Пассажиров есть на {k} этаже")
                print(len(v))
                for pas in v:
                    if self.enter_elevator(passanger=pas):
                        v.pop(v.index(pas))
                        self.dict_floors[k] = v
                        continue
                    else:
                        # print('asdasdasdasdasdasdasdas')
                        for pas in self.get_passanger():
                            self.call_elevator(pas)


passager_list = list()

elevator = Elevator(n)
print(elevator.number)

for i in range(0, k):
    passanger = Person(floor_start=randint(5, n), floor_end=randint(5, n))
    elevator.check_elevator(passanger=passanger)

elevator.start()
print(elevator.dict_floors)