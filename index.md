# 机器学习可视化（Machine Learning Visualized）

一本收录 Jupyter Notebook 的书籍，从第一性原理出发实现并数学推导机器学习算法。每个 Notebook 的输出都是该算法训练过程的可视化，最终收敛到最优权重。祝学习愉快！—— [Gavin H](https://www.linkedin.com/in/gavinkhung/)

```{only} html
[![](https://img.shields.io/github/stars/gavinkhung/machine-learning-visualized?style=social)](https://github.com/gavinkhung/machine-learning-visualized)
[![](https://img.shields.io/github/forks/gavinkhung/machine-learning-visualized?style=social)](https://github.com/gavinkhung/machine-learning-visualized)
```

## 第 4 章 神经网络（Neural Networks）

在线性模型的基础上，我们会堆叠多个层，并应用除 Sigmoid 之外的新激活函数（Activation Function），使神经网络能够学习非线性的复杂函数。在神经网络上寻找最优权重和偏置的优化过程称为反向传播（Backpropagation）。

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: /chapter4/neural_network_weights
:class-header: bg-light

**神经网络损失曲面（Loss Landscape）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/neural-network/refs/heads/main/neural_network_weights_loss_landscape.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter4/neural_network_weights
:class-header: bg-light

**神经网络变换（Transformations）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/neural-network/main/neural_network_weights.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter4/neural_network
:class-header: bg-light

**神经网络函数逼近（Function Approximation）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/neural-network/main/neural_network.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter4/neural_network
:class-header: bg-light

**神经网络反向传播（Backpropagation）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/neural-network/refs/heads/main/neural_network_loss_landscape.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter4/autoencoder
:class-header: bg-light

**自编码器重建结果（Reconstructions）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/autoencoder/refs/heads/main/autoencoder.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter4/autoencoder
:class-header: bg-light

**自编码器潜在空间（Latent Space）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/autoencoder/refs/heads/main/autoencoder_latent_space.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

::::

## 第 3 章 线性模型与激活函数（Linear Models and Activation Function）

感知机（Perceptron）等线性模型通过对输入特征做线性组合来预测结果。线性组合中的参数由梯度下降（Gradient Descent）等优化算法从数据中学习得到。这相当于一个没有激活函数的单层神经网络。逻辑回归（Logistic Regression）在感知机的基础上引入了名为 Sigmoid 的激活函数以及二元交叉熵（Binary Cross Entropy）损失函数，从而扩展了感知机的思想。

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: /chapter3/logistic_regression
:class-header: bg-light

**逻辑回归（Logistic Regression）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/logistic-regression/main/logistic_regression.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter3/perceptron
:class-header: bg-light

**感知机（Perceptron）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/perceptron/main/perceptron.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

::::

## 第 2 章 聚类与降维（Clustering and Reduction）

机器学习模型的参数是从训练数据中学到的，因此对数据本身做分析十分重要。主成分分析（Principal Component Analysis）是一种压缩数据、找出能解释大部分方差（Variance）的特征的方法，让你可以把训练重点放在这些输入上。K-均值聚类（K-Means）是一种无监督聚类算法，可以帮助你发现彼此相关的数据点分组，这在数据预处理和识别离群点（Outlier）时非常有用。

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: /chapter2/k_means
:class-header: bg-light

**K-均值聚类（K-Means Clustering）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/k-means-clustering/main/k_means.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter2/pca
:class-header: bg-light

**主成分分析（Principal Component Analysis）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/pca/main/pca.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

::::

## 第 1 章 优化（Optimization）

优化是寻找能使函数取值最小的输入参数的过程。把这个思想推广到机器学习，优化算法就需要找到能让损失函数（Loss Function）的误预测最小的权重和偏置。梯度下降就是这样一种优化算法。收敛（Convergence）与稳定性对参数的学习至关重要。

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: /chapter1/linear_regression
:class-header: bg-light

**梯度下降（Gradient Descent）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/gradient-descent/refs/heads/main/gradient_descent.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

:::{grid-item-card}
:link: /chapter1/optimizers
:class-header: bg-light

**优化器（Optimizers）**
^^^

```{image} https://raw.githubusercontent.com/gavinkhung/optimizers/refs/heads/main/optimizers_pytorch.gif
:width: 100%
```

+++
Jupyter Notebook {fas}`arrow-right`
:::

::::

<!-- ## Table of Contents

```{tableofcontents}
``` -->

## 贡献指南（Contributing）

```{only} html
[![License: MIT](https://img.shields.io/badge/License-MIT-white.svg)](https://opensource.org/licenses/MIT)
```

我希望能建立一个社区，让全世界的人都能为这个开源资源/书籍添砖加瓦。简单来说，它就是一本收集了「实现机器学习算法的 Jupyter Notebook」的合集。

如果你有想加入本书的 Jupyter Notebook，欢迎向 [GitHub 仓库](https://github.com/gavinkhung/machine-learning-visualized) 提交拉取请求（Pull Request）。这里有一份[展示了全部必要代码改动的参考提交](https://github.com/gavinkhung/machine-learning-visualized/commit/98900877d3d1a42c972b3e618ad46968f02513cb)。

注意：你需要把你的 Notebook 上传到你自己的 GitHub 仓库。只要按照参考提交操作，拉取请求被合并后，本 Jupyter Book 的构建过程就会自动下载你的 `.ipynb` 文件并更新 GitHub Pages。

## 关于本书

> 我是一名充满好奇心的学习者，对高性能计算系统很感兴趣，尤其是支撑机器学习工作负载的系统。我计划申请计算机科学研究生项目（硕士学位），并以在职方式攻读，而不中断我的工作。如果你对计算机科学研究生申请有建议或认识相关的人，欢迎联系我（ghung AT umd DOT edu）。

这些 Python Jupyter Notebook 是我根据在[马里兰大学帕克分校（University of Maryland, College Park）](https://www.cs.umd.edu/)上课时的课堂笔记编写而成的。

如果你想自己运行这些 Jupyter Notebook，点击任意页面右上角的下载图标并选择 `.ipynb` 选项，然后在本地或 Google Colab 等云端环境中打开并运行这些代码块。

对于进阶用户，我还写了一些 Terraform 脚本，可以快速创建 AWS SageMaker Notebook，见[这里](https://github.com/gavinkhung/gpu-inference)。

### 值得一提的 UMD 课程

- [CMSC422 机器学习导论（Introduction to Machine Learning）](https://www.cs.umd.edu/class/fall2023/cmsc422/)
- [CMSC320 数据科学导论（Introduction to Data Science）](https://www.cs.umd.edu/class/spring2024/cmsc320-0201/)
- [UMD QML](https://qmlfire.github.io/)

### 机器学习课堂笔记

第 1 章：

- [梯度下降笔记](https://github.com/gavinkhung/gradient-descent/blob/main/gradient-descent.pdf)

第 2 章：

- [主成分分析笔记](https://github.com/gavinkhung/pca/blob/main/pca.pdf)

第 3 章：

- [感知机笔记](https://github.com/gavinkhung/perceptron/blob/main/perceptron.pdf)
- [朴素贝叶斯与最大似然估计笔记](https://github.com/gavinkhung/logistic-regression/blob/main/maximum-likelihood.pdf)
- [逻辑回归笔记](https://github.com/gavinkhung/logistic-regression/blob/main/logistic-regression.pdf)
- [Softmax 回归](https://github.com/gavinkhung/logistic-regression/blob/main/softmax.pdf)

第 4 章：

- [神经网络前向传播笔记](https://github.com/gavinkhung/neural-network/blob/main/forward-propagation.pdf)
- [神经网络反向传播笔记](https://github.com/gavinkhung/neural-network/blob/main/back-propagation.pdf)

<!-- ## Analytics

<iframe
  width="100%"
  height="500px"
  src="https://datastudio.google.com/embed/reporting/a767567e-8bac-4613-9c17-599a164a6638/page/kIV1C"
  frameborder="0"
  style="border: 0"
  allowfullscreen
  sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
></iframe> -->
