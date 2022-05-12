import random

floor_count = random.choice(range(5, 21))

class Passenger:
    
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.desired_floor = self._get_desired_floor()

    def _get_desired_floor(self):
        """
        Method to generate a random floor 
        different from the one the passenger is on.
        """
        floor = random.randint(1, floor_count)
        if floor != self.current_floor:
            return floor
        else:
            return self._get_desired_floor()


class Floor:
    
    def __init__(self, number, passengers = []):
        self.number = number
        self.passengers = passengers


class Elevator:

    delivered_passengers_count = 0
    
    def __init__(self, floors = {}):
        self.current_floor = 1
        self.capacity = 5
        self.floors = floors
        self.passengers = []
        self.up_down = True
        self._create_floors()

    def _create_floors(self):
        """
        Creation of floors, 
        each floor has a certain 
        number of passengers.
        """
        for i in range(1, floor_count + 1):
            floor_obj = Floor(i, [Passenger(i) for j in range(random.choice(range(0, 11)))])
            self.floors[floor_obj.number] = floor_obj.passengers

    def _take_passengers(self):
        """
        A method that picks up passengers 
        from the current floor.
        """
        passengers = self.floors[self.current_floor]
        if len(passengers):
            print(f'НА {self.current_floor} ЭТАЖЕ ЕСТЬ ПАССАЖИРЫ, КОЛИЧЕСТВО {len(passengers)} ЧЕЛОВЕК')
            for i in passengers:
                if self.capacity > 0:
                    if self.up_down and i.desired_floor >= self.current_floor:
                        self.passengers.append(i)
                        self.capacity -= 1
                        self.delivered_passengers_count += 1
                    elif not self.up_down and i.desired_floor <= self.current_floor:
                        self.passengers.append(i)
                        self.capacity -= 1
                        self.delivered_passengers_count += 1
                else: break
            print(f'В ЛИФТЕ СЕЙЧАС {len(self.passengers)} ЧЕЛОВЕК')
            passengers = list(filter(lambda x: x not in self.passengers, passengers))
            self.floors[self.current_floor] = passengers
            print(f'НА {self.current_floor} ЭТАЖЕ ОСТАЛОСЬ {len(self.floors[self.current_floor])} ПАССАЖИРОВ')
        else:
            print(f'НА {self.current_floor} ЭТАЖЕ НЕТ ПАССАЖИРОВ')

    def _check_floor(self):
        """
        A method that checks 
        if there are passengers who need 
        to get off on this floor.
        """
        current_passengers_count = len(self.passengers)
        if len(self.passengers) != 0:
            self.passengers = list(filter(lambda x: x.desired_floor != self.current_floor, self.passengers))
        print(f'НА ЭТАЖЕ {self.current_floor} ВЫШЛО {current_passengers_count - len(self.passengers)} ПАССАЖИРОВ')
        self.capacity = 5 - len(self.passengers)
        print(f'В ЛИФТЕ ОСТАЛОСЬ {len(self.passengers)} ПАССАЖИРОВ')
        return self.capacity
        
    def up_floor(self):
        """
        Method, calls methods for disembarking passengers 
        and picking up new passengers, 
        then raises the elevator to the next floor.
        """
        print('^****^****^')
        print(f'СЕЙЧАС ЛИФТ НА {self.current_floor} ЭТАЖЕ')
        self._check_floor()
        self._take_passengers()
        self.current_floor += 1

    def down_floor(self):
        """
        Method, calls methods for disembarking passengers 
        and picking up new passengers, 
        then raises the elevator to the prev floor.
        """
        print('v****v****v')
        print(f'СЕЙЧАС ЛИФТ НА {self.current_floor} ЭТАЖЕ')
        self._check_floor()
        self._take_passengers()
        self.current_floor -= 1

    def start(self):
        """
        Method that starts the elevator, 
        the elevator will run until all passengers 
        have been delivered to the desired floors.
        """
        total_passengers = len([i for v in self.floors.values() for i in v]) 
        print('ЛИФТ ЗАПУЩЕН')
        while total_passengers + len(self.passengers) != self.delivered_passengers_count:
            if self.up_down:
                self.up_floor()
            else: 
                self.down_floor()
            
            if self.current_floor == floor_count:
                self.up_down = False
            elif self.current_floor  == 1:
                self.up_down = True
        print(f'ВСЕ ПАССАЖИРЫ ДОСТАВЛЕНЫ')        

elevator_object = Elevator()
elevator_object.start()
