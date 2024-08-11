class Selfie:
    def __init__(self):
        self._current_state = -1
        self._states = {}

    def n_states(self):
        return len(self._states)

    def save_state(self):
        self._current_state += 1
        self._states[self._current_state] = {
            k: v for k, v in self.__dict__.items() if k not in ['_states', '_current_state']
        }
        pass

    def recover_state(self, state_num):
        if state_num not in self._states:
            return self

        state = self._states[state_num]
        selfie = Selfie()
        selfie.__dict__ = {k: v for k, v in state.items()}
        selfie._states = {1: state}
        selfie._current_state = 1
        return selfie


# TEST_4:
def sum_a_b(a, b):
    return a + b


def sub_a_b(a, b):
    return a - b


def mul_a_d(a, b):
    return a * b


def truediv_a_b(a, b):
    return a / b


obj = Selfie()
obj.sum_a_b = sum_a_b
print(obj.sum_a_b(1, 2))
obj.save_state()

obj.sub_a_b = sub_a_b
print(obj.sub_a_b(1, 2))
obj.save_state()

obj.mul_a_d = mul_a_d
print(obj.mul_a_d(1, 2))
obj.save_state()

obj.truediv_a_b = truediv_a_b
print(obj.truediv_a_b(1, 2))
obj.save_state()

print(obj.n_states())
obj = obj.recover_state(1)

print(obj.n_states())


# TEST_4:
# 3
# -1
# 2
# 0.5
# 4
# 1
