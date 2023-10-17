from statistics import mean as mn

class List_comparison:
    def __init__(self):
        self.list1, self.list2 = [], []
    
    def print_lists(self):
        print(*self.list1, sep=' ')
        print(*self.list2, sep=' ')

    def set_lists(self,list1,list2):
        self.list1, self.list2 = list1, list2
    
    def comparison_averages(self):
        self.avg1, self.avg2 = mn(self.list1), mn(self.list2)
        if self.avg1 > self.avg2:
            print(f"Первый список имеет большее среднее значение({round(self.avg1,2)} > {round(self.avg2,2)})")
        elif self.avg1 < self.avg2:
            print(f"Второй список имеет большее среднее значение({round(self.avg1,2)} < {round(self.avg2,2)})")
        else: print(f"Средние значения равны {round(self.avg1,2)}")