import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        '''
        Takes a variable number of balls of different colors in the form:
        red=1, blue=3, cyan=2
        '''
        self.contents = []
        for key, val in kwargs.items():
            for x in range(val):
                self.contents.append(key)

    def draw(self, n):
        if n >= len(self.contents):
            ret = self.contents
            del self.contents
            return self.contents
        result = []
        for _ in range(n):
            i = random.randint(0, len(self.contents)-1)
            ball = self.contents[i]
            result.append(ball)
            del self.contents[i]
        return result



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
