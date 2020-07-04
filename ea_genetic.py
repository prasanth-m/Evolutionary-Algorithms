#import requests
import random
import time


class EightQueens:

    def __init__(self, size):
        self.num_queens=size
        self.perfect_fit=(self.num_queens*(self.num_queens-1))/2  
        self.solve_8queens()    

    def gen_data_set(self):
        return [ random.randint(1, self.num_queens) for _ in range(self.num_queens) ]

    def fit_count(self, data_set):
        hc = sum([data_set.count(queen)-1 for queen in data_set])/2
        dc = 0

        n = len(data_set)
        ld = [0] * 2*n
        rd = [0] * 2*n
    
        for i in range(n):
            ld[i + data_set[i] - 1] += 1
            rd[len(data_set) - i + data_set[i] - 2] += 1

        dc = 0
        for i in range(2*n-1):
            counter = 0
            if ld[i] > 1:
                counter += ld[i]-1
            if rd[i] > 1:
                counter += rd[i]-1
            dc += counter / (n-abs(i-n+1))
    
        return int(self.perfect_fit - (hc + dc))

    def new_comb(self, data_set, fit_count):
        return self.fit_count(data_set) / self.perfect_fit

    def frame_new_set(self, data_set, comb):
        changeData = zip(data_set, comb)
        total = sum(w for c, w in changeData)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(data_set, comb):
            if upto + w >= r:
                return c
            upto += w
        
    def cross_over(self, x, y): 
        n = len(x)
        c = random.randint(0, n - 1)
        return x[0:c] + y[c:n]

    def rand_change(self, x):  
        n = len(x)
        c = random.randint(0, n - 1)
        m = random.randint(1, n)
        x[c] = m
        return x

    def print_set(self, data):
        data[:] = [number - 1 for number in data]
        print("Queens = {}".format(str(data)))
        timestr = time.strftime("%Y%m%d-%H%M%S")
        file_ptr = open("8queens-output-"+timestr+".txt", "w")
        file_ptr.write(str(data))
        file_ptr.close()
        
    def gen_new_set(self, data_set, fit_count):
        change = 0.04
        new_set = []
        comb = [self.new_comb(n, fit_count) for n in data_set]
        for i in range(len(data_set)):
            x = self.frame_new_set(data_set, comb)
            y = self.frame_new_set(data_set, comb) 
            res = self.cross_over(x, y) 
            if random.random() < change:
                res = self.rand_change(res)
        
            new_set.append(res)
            if self.fit_count(res) == self.perfect_fit:
                self.print_set(res)
                break
        return new_set

       
    def solve_8queens(self):
        data_set = [self.gen_data_set() for _ in range(100)]
        count = 1
        while not self.perfect_fit in [self.fit_count(set) for set in data_set]:
            data_set = self.gen_new_set(data_set, self.fit_count)
            count += 1

def main():
    EightQueens(8)

if __name__ == "__main__":
    main()