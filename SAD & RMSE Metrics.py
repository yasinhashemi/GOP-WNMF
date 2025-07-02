# SAD & RMSE Metrics
def SAD(real_endmembers, est_endmembers):
    sad = 0
    for i in range(real_endmembers.shape[1]):
        sad += np.arccos((real_endmembers[:, i].T @ est_endmembers[:, i]) / (norm(real_endmembers[:, i]) * norm(est_endmembers[:, i])))
    return sad / (real_endmembers.shape[1])


def RMSE(real_abundances, est_abundances):
    return np.sqrt(norm(real_abundances - est_abundances, 'f') ** 2 / (real_abundances.shape[0] * real_abundances.shape[1]))
    # return np.sqrt(np.mean(np.square(real_abundances - est_abundances)))