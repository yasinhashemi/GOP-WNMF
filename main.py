def OPNMF(X, U, V, S, endmembers_num, real_endmembers, real_abundances, alpha, beta, gamma, landa, theta, k, sigma, mu1, mu2, nu, p= 0.2, delta=15, Max_iter= 1500, error_tol= 1e-7):
    cnt = 0
    D, W = KNN_graph(X, k, sigma)
    former_residual = RMSE(X, U @ S)
    S[S <= 0] = 1e-5
    
    T = weight(X, U, S, mu1, mu2)
    A = sparsity(X, U, nu)


    for iter in range(Max_iter):
        # Update U
        numU = (T * T * X) @ S.T + alpha * V
        denU = (T * T * (U @ S)) @ S.T + alpha * V @ V.T @ U
        reU = numU / np.maximum(denU, 1e-10)
        U = U * reU
        U[U <= 1e-4] = 1e-4

        # Update V
        numV = theta * X @ S.T + alpha * U
        denV = theta * X @ X.T @ V + alpha * U @ U.T @ V
        reV = numV / np.maximum(denV, 1e-10)
        V = V * reV
        V[V <= 1e-4] = 1e-4

        # Update S
        Xbar = np.concatenate([X, delta * np.ones((1, X.shape[1]))])
        Ubar = np.concatenate([U, delta * np.ones((1, U.shape[1]))])
        Vbar = np.concatenate([V, delta * np.ones((1, V.shape[1]))])
        Tbar = np.concatenate([T, p * np.ones((1, T.shape[1]))])  # p = 0.2

        numS = Ubar.T @ (Tbar * Tbar * Xbar) + theta * Vbar.T @ Xbar + beta * S @ W + gamma * S @ D
        denS = Ubar.T @ (Tbar * Tbar * (Ubar @ S)) + theta * S + beta * S @ D + gamma * S @ D @ S.T @ S @ D + landa * A
        reS = numS / np.maximum(denS, 1e-10)
        S = S * reS
        S[S <= 1e-4] = 1e-4

        # Update T
        T =weight(X, U, S, mu1, mu2)

        # Update A
        A = sparsity(X, U, nu)

        latter_residual = RMSE(X, U @ S)

        err = np.abs(former_residual - latter_residual)
        former_residual = latter_residual

        if err < error_tol:
            cnt += 1
            if cnt == 10:
                break
    
    M, S = Permutation(real_endmembers, real_abundances, U, S)
    sad = SAD(real_endmembers, M)
    rmse = RMSE(real_abundances, S)

    return sad, rmse, cnt, M, S