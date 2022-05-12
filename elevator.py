import random

# floor_count = random.choice(range(5, 21))
floor_count = 5

class Elevator:

    counter = 0
    
    def __init__(self, floors = {}):
        self.current_floor = 1
        self.max_floor = 0
        self.min_floor = 0
        self.capacity = 5
        self.floors = floors
        self.passengers = []
            

    def _take_passengers(self):
        passengers = self.floors[self.current_floor]
        if len(passengers):
            print(f'НА {self.current_floor} ЭТАЖЕ ЕСТЬ ПАССАЖИРЫ, КОЛИЧЕСТВО {len(passengers)} ЧЕЛОВЕК')
            for i in passengers:
                if self.capacity > 0:
                    self.passengers.append(i)
                    self.capacity -= 1
                    self.counter += 1
                else: break
            print(f'В ЛИФТЕ СЕЙЧАС {len(self.passengers)} ЧЕЛОВЕК')
            passengers = list(filter(lambda x: x not in self.passengers, passengers))
            self.floors[self.current_floor] = passengers
            print(f'НА {self.current_floor} ЭТАЖЕ ОСТАЛОСЬ {len(self.floors[self.current_floor])} ПАССАЖИРОВ')
            return
        else:
            print(f'НА {self.current_floor} ЭТАЖЕ НЕТ ПАССАЖИРОВ')

        # if len(self.passengers):
        #     self.max_floor = max([i.desired_floor for i in self.passengers])
        #     self.min_floor = min([i.desired_floor for i in self.passengers])

    def _check_floor(self):
        current_passengers_count = len(self.passengers)
        if len(self.passengers) != 0:
            self.passengers = list(filter(lambda x: x.desired_floor != self.current_floor, self.passengers))
        print(f'НА ЭТАЖЕ {self.current_floor} ВЫШЛО {current_passengers_count - len(self.passengers)} ПАССАЖИРОВ')
        self.capacity = 5 - len(self.passengers)
        return self.capacity
        
    def _up_floor(self):
        print('^****^****^')
        print(f'СЕЙЧАС ЛИФТ НА {self.current_floor} ЭТАЖЕ')
        self._check_floor()
        self._take_passengers()
        self.current_floor += 1
        return

    def _down_floor(self):
        print('v****v****v')
        print(f'СЕЙЧАС ЛИФТ НА {self.current_floor} ЭТАЖЕ')
        self._check_floor()
        self._take_passengers()
        self.current_floor -= 1
        return 

    def start(self):
        total_passengers = len([i for v in self.floors.values() for i in v])
        print(total_passengers)
        print('ЛИФТ ЗАПУЩЕН')
        up_down = True
        while total_passengers != self.counter:
            print(self.counter)
            # print(passengers_total_count)
            if up_down:
                self._up_floor()
            else: 
                self._down_floor()
            
            if self.current_floor == floor_count:
                up_down = False
            elif self.current_floor  == 1:
                up_down = True
        print(f'ВСЕ ПАССАЖИРЫ ДОСТАВЛЕНЫ')

            

class Floor:
    
    def __init__(self, number, passengers = []):
        self.number = number
        self.passengers = passengers

class Passenger:
    
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.desired_floor = self._get_desired_floor()
        # print(f'CREATED! {self.current_floor} {self.desired_floor}')

    def _get_desired_floor(self):
        floor = random.randint(1, floor_count)
        if floor != self.current_floor:
            return floor
        else:
            return self._get_desired_floor()

elevator_object = Elevator()

for i in range(1, floor_count + 1):
    floor_obj = Floor(i, [Passenger(i) for j in range(random.choice(range(0, 11)))])
    # print(floor_obj.number, [i.desired_floor for i in floor_obj.passengers])
    elevator_object.floors[floor_obj.number] = floor_obj.passengers

data = {k: [i.desired_floor for i in v] for k, v in elevator_object.floors.items()}
with open('data.txt', 'a+') as f:
    f.write(str(data) + "\n")
elevator_object.start()



# pass_obj = Passenger(1)
# print(pass_obj.current_floor, pass_obj.desired_floor)