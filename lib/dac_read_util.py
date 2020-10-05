import numpy as np
import glob

from lib.dac_read import dac_read


def read_field(dir_name):
    n_time = len(glob.glob(f'{dir_name}/*_ro_rank=0000.dac'))
    field = []
    for i in range(1, n_time + 1):
        data, x, y = dac_read(
            f'{dir_name}/{str(i).zfill(4)}_*_rank=*.dac', dimension=2)
        field.append(data)
    field = np.array(field)
    return field, x, y
