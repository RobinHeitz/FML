# birthday problem:
from math import factorial as fac
from math import comb



def at_least_2_people_with_same_birthday():
    """Calculates the Probability n persons in a room with at least 2 of them having the same birthday."""
    
    def calc_p(n=2):
        return 1 - comb(365, n) * fac(n) / (365 ** n)
    
    
    for n in range(2, 365):
        r = calc_p(n)
        print(f"Probability for n = {n:3}: {r:5}")
        if r > 0.5:
            break


def sick_given_pos_test(base_rate = 0.001, break_p = 0.99):
    """Calculates the probability to be sick after a positive test. Result depends heavily on base rate."""


    def calc_prob(num_tests):
        return 0.99**num_tests * base_rate / (0.99 ** num_tests * base_rate + 0.05**num_tests*(1-base_rate))
    
    for n in range(1, 50):
        p = calc_prob(n)
        print(f"With {n:2} tests, the probability of actually beeing sick given a positive test is: {p:4}")
        if p >= break_p:
            break





if __name__ == "__main__":
    # at_least_2_people_with_same_birthday()
    sick_given_pos_test(base_rate=0.001)
