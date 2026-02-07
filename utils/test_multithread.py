import numpy as np
import time
from tqdm.auto import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def test(a, b, c):
    for _ in tqdm(range(b), desc=f'{a} waiting'):
        time.sleep(c)

if __nmae__=='__main__':
    a_lst = range(32)
    c_lst = np.random.randint(5, size=32)
    
    with ThreadPoolExecutor() as executor:
        _ = [executor.submit(test, a, 5, c) for a, c in zip(a_lst, c_lst)]