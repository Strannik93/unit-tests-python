from statistics import mean as mn

class ListComparison():
    def __init__(self):
        self.avg1, self.avg2 = 0, 0

    def comparison_averages(self, list1: list, list2: list):
        self.avg1, self.avg2 = mn(list1), mn(list2)
        if self.avg1 > self.avg2:
            return "Первый список имеет большее среднее значение"
        elif self.avg1 < self.avg2:
            return "Второй список имеет большее среднее значение"
        else: return "Средние значения равны"