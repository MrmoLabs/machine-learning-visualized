# 机器学习可视化（Machine Learning Visualized）

![website](gifs/home.gif)

网址：[https://ml-visualized.com/](https://ml-visualized.com/)

机器学习可视化是一本 [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)，收录了一批 Jupyter Notebook，从第一性原理出发实现并数学推导机器学习算法。

书中还包含用 Marimo 构建的交互式 Notebook，可以直观地看到权重如何影响损失函数。

每个 Notebook 的输出都是该机器学习算法训练过程的可视化，最终收敛到最优权重。

每个机器学习算法都有独立的 GitHub 仓库。因此，本仓库只是用来配置和构建这本 Jupyter Book 的代码。简单来说，Jupyter Book 可以用 Markdown 文件和 Jupyter Notebook 构建出一个网站。请注意，本仓库中并不包含任何 Jupyter Notebook——有一个 SH 脚本会从其他 GitHub 仓库下载相关的 Jupyter Notebook。下载完成后即可构建 Jupyter Book。网站会在每次提交或拉取请求后，通过 `.github/workflows/ci.yml` 中的 GitHub Action 自动更新。若想在本地构建网站，请参考下方的「使用方法」章节。

## Jupyter Notebook

- [神经网络（Neural Networks）仓库](https://github.com/gavinkhung/neural-network)
- [自编码器（Autoencoder）仓库](https://github.com/gavinkhung/autoencoder)
- [逻辑回归（Logistic Regression）仓库](https://github.com/gavinkhung/logistic-regression)
- [感知机（Perceptron）仓库](https://github.com/gavinkhung/perceptron)
- [主成分分析（PCA）仓库](https://github.com/gavinkhung/pca)
- [K-均值聚类（K-Means）仓库](https://github.com/gavinkhung/k-means-clustering/)
- [梯度下降（Gradient Descent）仓库](https://github.com/gavinkhung/gradient-descent)

## Jupyter Book 信息

书籍的目录（Table of Contents）和结构由 `_toc.yml` 指定。

配置由 `_config.yml` 指定。

更多信息请查看 [Jupyter Book 官方文档](https://jupyterbook.org/en/stable/intro.html)。

## 使用方法

### 第 1 步：下载 Jupyter Notebook

```sh
chmod +x ./download_notebooks.sh
./download_notebooks.sh
```

### 第 2 步：构建 Jupyter Book

#### 方式 1：jupyter-book 命令行工具

```sh
pip install -U jupyter-book
jupyter-book build .
```

#### 方式 2：Docker Compose

```sh
docker compose run --rm jupyter-book
docker compose down --remove-orphans --volumes --rmi local
```

#### 方式 3：Docker

```sh
docker build -f Dockerfile.book -t jupyter-book .
docker run --rm -v "$(pwd)":/usr/src/app jupyter-book

docker stop jupyter-book
docker rm jupyter-book
docker rmi jupyter-book
```

### 第 3 步：打开 Jupyter Book

浏览 `_build/html/index.html` 即可。

## 构建 EPUB（新增）

```sh
brew install --cask mactex
nbmerge $(ls chapter1/*.ipynb chapter2/*.ipynb chapter3/*.ipynb chapter4/*.ipynb | sort) -o book/combined.ipynb
jupyter nbconvert --to latex book/combined.ipynb

docker build -f Dockerfile.pandoc -t my-pandoc .
docker run --rm -v $(pwd):/data my-pandoc pandoc book/combined.tex -o book/combined.epub --mathml --embed-resources --standalone
```

## 效果展示

### Marimo 交互式 Notebook

![Marimo](gifs/marimo.gif)

### 数学推导讲解

![latex](gifs/latex.gif)
