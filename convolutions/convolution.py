

# funkcja oznaczona w opisie jako 3 do splotu
# todo nie wiem czy parametr K powinien tu byc? mowa jest o jakims obcieciu f
def convolution(vector_y1, vector_y2, K=1):
    vector_y = []
    for n in range((len(vector_y1) + len(vector_y2) - 1) // K):
        vector_y.append(0)
        for k in range(len(vector_y1)):
            if 0 <= n - k < len(vector_y2):
                vector_y[n] += vector_y1[k] * vector_y2[n - k]
    return vector_y
