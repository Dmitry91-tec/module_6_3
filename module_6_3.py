class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        print('Создан объект Horse')
        pass

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        print('Создан объект Eagle')

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def __init__(self):
        print('Создан объект Pegasus')

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        self.tuple_ = (self.x_distance, self.y_distance)
        return self.tuple_

    def voice(self):
        self.sound = Eagle.sound
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
