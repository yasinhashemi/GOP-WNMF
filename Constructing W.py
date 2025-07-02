# Constructing W
def weight(X, U, S, mu1, mu2):
    residual = X - U @ S
    band_weight = np.reciprocal(norm(residual, axis= 1, keepdims= True))
    pixel_weight = np.reciprocal(norm(residual, axis= 0, keepdims= True))
    return mu1 * band_weight * mu2 * pixel_weight