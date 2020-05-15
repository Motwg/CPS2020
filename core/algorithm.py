import json
import os
from copy import deepcopy

import numpy as np

from core.functions import function_switcher


class Algorithm:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __copy__(self):
        return deepcopy(self)

    def perform_algorithm(self):
        vector_y = []
        vector_x = []

        for t in np.arange(self.kwargs['t1'], self.kwargs['d'] + self.kwargs['t1'], self.kwargs['f']):
            vector_x.append(t)
            vector_y.append(function_switcher(self.kwargs['function'])(t, **self.kwargs))
        return vector_x, vector_y

    def save_algorithm(self, filename, path='files'):
        print(os.getcwd())
        json_kwargs = json.dumps(self.kwargs, indent=4)
        os.makedirs(os.getcwd() + '/' + path, exist_ok=True)
        f = open(path + '/' + filename, 'w+')
        f.write(json_kwargs)
        f.close()

    def load_algorithm(self, filename, path='files'):
        try:
            with open(path + '/' + filename, 'r') as f:
                self.kwargs = json.load(f)
            return self
        except Exception:
            raise Exception('Cannot open {0}/{1}.json, file may not exists'.format(path, filename))

