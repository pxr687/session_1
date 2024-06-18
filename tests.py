import numpy as np

rng = np.random.default_rng()
full = 1*52*1

def test_1():
    
    correct = []
    
    my_frac = (1*1*1*1/full*1*1*1)
    
    my_frac_2 = (1*1*1*51/full*1*1*1)
    
    n = 1*1*1*1*1*1*1*20*1
    
    for i in np.arange(10_000):

        twenty_random_guesses = rng.choice(['A', 'B'],
                                           p =[my_frac, my_frac_2], size=n)
        n_correct = np.sum(twenty_random_guesses == 'A')

        correct.append(n_correct)

    correct = np.array(correct)

    return np.mean(correct)

def test_2(guesses):

    results = np.zeros(10_000)

    for i in np.arange(10_000):

        simulated_guesses = rng.choice(['CORRECT', 'INCORRECT'], p =[1/5, 4/5], size = len(guesses))

        results[i] = np.sum(simulated_guesses == 'CORRECT')

    return np.mean(results)