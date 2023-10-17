import pytest

from List_comparison import ListComparison

class TestCompAvg:
    @pytest.mark.parametrize('x, y, rezult', [([2,4],[4,2],
                                               "Средние значения равны"),
                                              ([2,4],[1,4],
                                               "Первый список имеет большее среднее значение"),
                                              ([2,5],[6,8],
                                               "Второй список имеет большее среднее значение")])
    def test_comp_avg(self, x,y,rezult):
        lc = ListComparison()
        assert lc.comparison_averages(x,y) == rezult
