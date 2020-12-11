import faker
import random
from time import process_time
from pprint import pprint


class Searcher:
    def __init__(self, cnt):
        self.array =[]
        self.fill(cnt)
        self.chance = []
        self.sorted_arr = []
        self.seg_cnt = 6

    def fill(self, cnt):
        fake = faker.Faker()
        for i in range(cnt):
            d = {'key': 100000 + i,
                 'name': fake.name()}
            self.array.append(d)

    def print(self):
        pprint(self.array)

    def brute(self, key):
        for item in self.array:
            if item['key'] == key:
                return item
        return None

    def binary(self, key):
        s = 0
        e = len(self.array) - 1
        mid = (s + e) // 2
        if self.array[s]['key'] > key:
            return None
        elif self.array[e]['key'] < key:
            return None

        if self.array[s]['key'] == key:
            return self.array[s]
        elif self.array[e]['key'] == key:
            return self.array[e]

        tmp = self.array[mid]['key']
        while key != tmp:
            if key < tmp:
                e = mid
            else:
                s = mid
            mid = (s + e) // 2
            tmp = self.array[mid]['key']
        return self.array[mid]

    def prepare_seg(self):
        p = 100 / ((1 + self.seg_cnt) * self.seg_cnt // 2) / 100

        for i in range(self.seg_cnt):
            self.chance.append((self.seg_cnt - i) * p)
        for i in range(1, self.seg_cnt):
            self.chance[i] += self.chance[i - 1]

    def segment(self, key):
        if len(self.chance) == 0:
            self.prepare_seg()
        for item in self.array:
            if item['key'] == key:
                return item
        return None


if __name__ == '__main__':
    repeat = 100000
    cnt = 100000

    s = Searcher(cnt)
    s.prepare_seg()

    t1 = process_time()
    print('init was done')
    for i in range(repeat):
        a = s.brute(i + 100000)
    t2 = process_time()

    print((t2 - t1) / repeat)
    for i in range(repeat):
        a = s.binary(i + 100000)
    t3 = process_time()

    print((t3 - t2) / repeat)
    for i in range(repeat):
        dice = random.random()
        if dice < s.chance[0]:
            key = random.randint(100000, 100000 + cnt // 6)
        elif dice < s.chance[1]:
            key = random.randint(100000 + cnt // 6, 100000 + 2 * cnt // 6)
        elif dice < s.chance[2]:
            key = random.randint(100000 + 2 * cnt // 6, 100000 + 3 * cnt // 6)
        elif dice < s.chance[3]:
            key = random.randint(100000 + 3 * cnt // 6, 100000 + 4 * cnt // 6)
        elif dice < s.chance[4]:
            key = random.randint(100000 + 4 * cnt // 6, 100000 + 5 * cnt // 6)
        else:
            key = random.randint(100000 + 5 * cnt // 6, 100000 + 6 * cnt // 6)
        a = s.segment(key)
    t4 = process_time()
    print((t4 - t3) / repeat)
