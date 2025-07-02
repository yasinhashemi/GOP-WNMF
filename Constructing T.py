# Constructing T
def sparsity(data, endmembers, nu):
    pixel_num = data.shape[1]
    endmembers_num = endmembers.shape[1]
    A = np.zeros((endmembers_num, pixel_num))

    for i in range(endmembers_num):
        A[i, :] = np.exp(norm(data - endmembers[:, [i]], axis= 0) / nu)

    return A