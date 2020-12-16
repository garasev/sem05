import random
from pprint import pprint
from time import sleep

import termcolor


class Unit:
    def __init__(self, ground):
        self.ground = ground
        self.water = 0

    def __str__(self):
        return '{}, {}'.format(self.ground, self.water)


class Map:
    def __init__(self, size):
        self.size = size
        self.map = []

    def generate(self):
        res = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Unit(random.randint(1, 2)))
            res.append(row)
        self.map = res

    def print(self):
        print('****************************************')
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j].water == 0:
                    color = 'yellow'
                else:
                    color = 'blue'
                termcolor.cprint('{:2.2}'.format(float(self.map[i][j].water + self.map[i][j].ground)), color, end='  ')
            print('')

    def add_peak(self):
        self.map[self.size // 2][self.size // 2].height = 3

    def add_water(self, i, j, litr):
        self.map[i][j].water += litr

    def find_peak(self):
        local_max = 0
        x = 0
        y = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j].water + self.map[i][j].ground > local_max:
                    x = i
                    y = j
                    local_max = self.map[i][j].water + self.map[i][j].ground
        return x, y

    def calc_avg_level(self, i, j):
        tmp = 0
        lvl = 0
        if i > 0:
            tmp += 1
            lvl += self.map[i - 1][j].water + self.map[i - 1][j].ground
        if j > 0:
            tmp += 1
            lvl += self.map[i][j - 1].water + self.map[i][j - 1].ground
        if i > 0 and j > 0:
            tmp += 1
            lvl += self.map[i - 1][j - 1].water + self.map[i - 1][j - 1].ground
        if i < self.size - 1:
            tmp += 1
            lvl += self.map[i + 1][j].water + self.map[i + 1][j].ground
        if j < self.size - 1:
            tmp += 1
            lvl += self.map[i][j + 1].water + self.map[i][j + 1].ground
        if i < self.size - 1 and j > 0:
            tmp += 1
            lvl += self.map[i + 1][j - 1].water + self.map[i + 1][j - 1].ground
        if j < self.size - 1 and i > 0:
            tmp += 1
            lvl += self.map[i - 1][j + 1].water + self.map[i - 1][j + 1].ground
        if j < self.size - 1 and i < self.size - 1:
            tmp += 1
            lvl += self.map[i + 1][j + 1].water + self.map[i + 1][j + 1].ground
        return float(lvl) / tmp

    def share_water(self, i, j, water):
        tmp = 0
        if i > 0:
            tmp += 1
        if j > 0:
            tmp += 1
        if i > 0 and j > 0:
            tmp += 1
        if i < self.size - 1:
            tmp += 1
        if j < self.size - 1:
            tmp += 1
        if i < self.size - 1 and j > 0:
            tmp += 1
        if j < self.size - 1 and i > 0:
            tmp += 1
        if j < self.size - 1 and i < self.size - 1:
            tmp += 1

        self.map[i][j].water -= water

        if i > 0:
            self.map[i - 1][j].water += water / tmp
        if j > 0:
            self.map[i][j - 1].water += water / tmp
        if i > 0 and j > 0:
            self.map[i - 1][j - 1].water += water / tmp
        if i < self.size - 1:
            self.map[i + 1][j].water += water / tmp
        if j < self.size - 1:
            self.map[i][j + 1].water += water / tmp
        if i < self.size - 1 and j > 0:
            self.map[i + 1][j - 1].water += water / tmp
        if j < self.size - 1 and i > 0:
            self.map[i - 1][j + 1].water += water / tmp
        if j < self.size - 1 and i < self.size - 1:
            self.map[i + 1][j + 1].water += water / tmp

    def test(self):
        pass

    def run(self):
        jopa = 0
        while True:
            i, j = self.find_peak()
            avg = self.calc_avg_level(i, j)
            self.share_water(i, j, float(self.map[i][j].water + self.map[i][j].ground - avg) / 3)
            jopa += 1
            #sleep(5)
            self.print()
            if jopa > 100000:
                break


if __name__ == '__main__':
    map = Map(5)
    map.generate()
    map.add_peak()
    map.print()
    map.add_water(2, 2, 10)
    map.run()
    print('*********************')
    map.print()

