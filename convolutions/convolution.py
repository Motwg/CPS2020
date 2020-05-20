

def convolution(vector_y1, vector_y2, K=1):
    vector_y = []
    cut_vector_y2 = vector_y2  # [:len(vector_y2) // K]
    for n in range((len(vector_y1) + len(cut_vector_y2) - 1)):  # // K):
        vector_y.append(0)
        for k in range(len(vector_y1)):
            if 0 <= n - k < len(cut_vector_y2):
                vector_y[n] += vector_y1[k] * cut_vector_y2[n - k]
    return vector_y
