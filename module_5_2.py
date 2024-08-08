class House:
    def __init__(self, name, numb):
        self.name = name
        self.numbers_of_floors = numb


    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)


    def __len__(self):
        return self.numbers_of_floors


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.numbers_of_floors}"


house1 = House("ЖК Эльбрус", 30)
house2 = House("ЖК Воробьёвы горы", 8)
print(house1)
print(house2)
print(len(house1))
print(len(house2))