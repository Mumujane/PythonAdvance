class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value >100:
            raise ValueError("score must between 0 ~ 100!")

        self._score = value


# 新实现方法
class NewStudent(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value



class ReadOnlyStudent(object):
    """
    # 定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    """

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


if __name__ == '__main__':
    s = Student()
    s.set_score(60)
    print(s.get_score())

    "*** 新方法***"

    # 把一个getter方法变成属性，只需要加上@property就可
    new_s = NewStudent()
    new_s.score = 61
    print(new_s.score)

    """
    @property广泛应用在类的定义中，可以让调用者写出简短的代码，
    同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
    
    """