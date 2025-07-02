# Required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.sparse
from numpy.linalg import norm
from scipy.optimize import nnls
from scipy.signal import convolve2d
from scipy.io import loadmat
from scipy.io import savemat
from scipy.stats import entropy
from scipy.sparse import coo_array
from scipy.sparse import dia_array
from sklearn.manifold import TSNE
from matplotlib.ticker import FuncFormatter
from sklearn.neighbors import kneighbors_graph
import matplotlib.ticker as mtick
import faiss
plt.style.use('seaborn-v0_8-bright')
plt.rcParams['figure.dpi'] = 100