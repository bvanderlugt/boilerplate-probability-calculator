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
            self.contents = []
            return ret
        result = []
        for _ in range(n):
            i = random.randint(0, len(self.contents)-1)
            ball = self.contents[i]
            result.append(ball)
            del self.contents[i]
        return result



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        h = copy.deepcopy(hat)
        balls = h.draw(num_balls_drawn)
        balls_actual = {}
        for ball in balls:
            balls_actual[ball] = balls_actual.get(ball, 0) + 1
        outcome = []
        for expected_ball in expected_balls:
            actual = balls_actual.get(expected_ball, 0)
            expected = expected_balls.get(expected_ball)
            if actual >= expected:
                outcome.append(True)
            else:
                outcome.append(False)
        if False not in outcome:
            m += 1
    return m/num_experiments
