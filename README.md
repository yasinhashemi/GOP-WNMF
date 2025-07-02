# Robust Oblique Projection and Weighted NMF for Hyperspectral Unmixing
## Abstract
Hyperspectral unmixing (HU) is a crucial method for interpreting remotely sensed hyperspectral images (HSIs), with the aim of splitting the image into pure spectral  components (endmembers) and their abundance fractions in every pixel of the scene. However, the effectiveness of this procedure is hindered by the presence of noise and anomalies. These kind of disruptions mainly arise from real-world factors such as atmospheric effects and endmember variability.
To address this challenge, a novel approach called Graph-Regularized Oblique Projection Weighted NMF (GOP-WNMF) is introduced, which is grounded in a more precise separation of signal and noise subspaces, aiming to enhance the accuracy and robustness of the analysis. GOP-WNMF achieves this by constructing an oblique projector that projects each pixel onto the signal subspace, i.e., the space formed by signatures of endmembers, and parallel to the noise subspace. This approach effectively suppresses noise while preserving crucial spectral information. Furthermore, our new oblique NMF framework includes a unique residual-based weighting approach to detect and remove anomalies in pixels and spectral bands simultaneously. In addition to this, another weighting matrix is proposed  by establishing a bipartite graph connecting endmembers and pixels to promote smoothness and sparsity in the resulting abundance maps. GOP-WNMF also enhances abundance map estimation accuracy by mitigating the negative effects of pixel outliers through the utilization of Laplacian eigenmaps technique to maintain the manifold structure of data. The effectiveness of GOP-WNMF is evaluated through comprehensive testing on synthetic and real HSIs, and its superiority is demonstrated over multiple state-of-the-art approaches.
## Requirements
Numpy \n
Scipy \n
Matplotlib \n
Sklearn \n
Faiss \n
