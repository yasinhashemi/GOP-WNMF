# K-NN Graph Construction
def KNN_graph(data, k, sigma):
    pixel_num = data.shape[1]
    transposed_data = data.T
    metric = faiss.METRIC_L2
    index = faiss.IndexFlatL2(transposed_data.shape[1])
    index.add(transposed_data)
    
    distances, indices = index.search(transposed_data, k + 1)
    distances, indices = np.exp((-1 / sigma) * distances[:, 1:]), indices[:, 1:]
    rows = np.tile(np.arange(pixel_num)[:, np.newaxis], k)
    W1 = (coo_array((0.5 *distances.ravel(), (rows.ravel(), indices.ravel())), shape= (pixel_num, pixel_num)) +
        coo_array((0.5 * distances.ravel(), (rows.ravel(), indices.ravel())), shape= (pixel_num, pixel_num)).T)

    return scipy.sparse.diags(W1.sum(axis= 1)), W1