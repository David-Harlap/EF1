from typing import List


class Agent:
    value: dict

    def __init__(self, value: dict):
        self.value = value

    def item_value(self, item_index: int) -> float:
        return self.value[item_index]


#
def is_ef1(agents: List[Agent], bundles: List[List[int]]) -> bool:
    # We need to check that there is no jealousy in any of the pairs of agents so we will go over them all
    for i in range(len(agents)):
        # my_sum to save the specific agent value
        my_sum = 0
        for j in bundles[i]:
            my_sum += agents[i].item_value(j)

        for j in range(len(bundles)):
            other_sum = 0  # to save each other agent value and compare with my_sum to check if someone jealous
            g = 0  # the biggest value that if we drop him and their are not jealous its good.
            if j == i:
                continue
            for k in bundles[j]:
                temp = agents[i].item_value(k)
                g = temp if temp > g else g
                other_sum += temp
            # if other sum - g i bigger than my_sum its mean that agents[i] jealous on agents[j] more than EF1.
            if other_sum - g > my_sum:
                return False
    # if we finish all the iteration and don't receive False its mean that we don't have jealous and the bundles is EF1.
    return True


if __name__ == '__main__':
    ag1 = Agent({1: 0.25, 2: 5.55, 3: 0.78, 4: 2.33})
    ag2 = Agent({1: 0.25, 2: 5.55, 3: 0.78, 4: 2.33})
    print(is_ef1([ag1, ag2], [[1, 3], [2, 4]]))
