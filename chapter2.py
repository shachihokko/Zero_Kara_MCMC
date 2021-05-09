import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

K_list = [1, 2, 3, 4, 5, 100] #和を取る一様乱数の数
n_iter = 1000000 #乱数の発生個数
#step = 1/1000
#x = np.arange(-2, 2+step, step)

#def norm_dist(x:np.ndarray, mu:float, sigma:float) -> np.ndarray:
#  return np.exp(-np.square(x-mu)/(2*sigma))/(np.sqrt(2*np.pi)*sigma)

#a=np.random.rand(K, n_iter)-0.5
#plt.hist(np.sum(a, axis=0), bins=1000, normed=True)
#plt.plot(x, norm_dist(x, 0, 1))
#plt.show()


nrow_fig, ncol_fig = 3, 2 # グラフの横の数と縦の数を求める
fig = plt.figure(figsize=(8,8)) # グラフの描画処理
for i, K in enumerate(K_list):
    ax = plt.subplot2grid((nrow_fig, ncol_fig), (i//ncol_fig, i%ncol_fig))
    # K*n_iterの一様乱数[-0.5, 0.5)の発生
    sum_uniform = np.sum(np.random.rand(K, n_iter)-0.5, axis=0) #行方向に和を取る(n_iter個の一様乱数の和になっている)
    ax.hist(sum_uniform, bins=1000, normed=True) #ヒストグラムの描画
    ax.legend(f"K={K}") #サブプロットにタイトルを表示

plt.tight_layout() #サブプロット間の間隔調整
plt.show()