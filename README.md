# 机器学习可视化（Machine Learning Visualized）

![website](gifs/home.gif)

网址：[https://ml-visualized.com/](https://ml-visualized.com/)

机器学习可视化是一本 [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)，收录了一批 Jupyter Notebook，从第一性原理出发实现并数学推导机器学习算法。

书中还包含用 Marimo 构建的交互式 Notebook，可以直观地看到权重如何影响损失函数。

每个 Notebook 的输出都是该机器学习算法训练过程的可视化，最终收敛到最优权重。

每个机器学习算法都有独立的 GitHub 仓库。因此，本仓库只是用来配置和构建这本 Jupyter Book 的代码。简单来说，Jupyter Book 可以用 Markdown 文件和 Jupyter Notebook 构建出一个网站。汉化后的 Jupyter Notebook 已随本仓库一起纳入版本管理；`download_notebooks.sh` 仅用于在文件缺失时从上游仓库补齐，默认会跳过已存在的文件。网站会在每次提交或拉取请求后，通过 `.github/workflows/ci.yml` 中的 GitHub Action 自动更新。若想在本地构建网站，请参考下方的「使用方法」章节。

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

> 汉化后的 notebook 已随仓库提供，本脚本默认**跳过所有已存在的文件**，
> 只在文件缺失时才从上游下载；如需强制同步上游英文原版：
> `FORCE_DOWNLOAD=1 ./download_notebooks.sh`。

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

### 第 3 步：本地预览（必须用 HTTP 服务，不能直接双击）

构建完成后，**不要直接双击 `_build/html/index.html`**（即 `file://` 方式打开）。
那样只能看静态内容，站内搜索、首页卡片链接和 3 个 Marimo 交互页全部不可用。
请在仓库根目录启动本地服务器：

```sh
python serve_local.py              # 默认 http://localhost:8000 ，托管 _build/html
python serve_local.py --port 8080  # 换端口
```

然后访问 <http://localhost:8000/>。

| 功能 | 直接打开 `index.html`（`file://`） | `python serve_local.py` |
| --- | --- | --- |
| 正文、图片/GIF、公式、左侧目录、章节间链接、下载 `.ipynb` | ✅ 可用 | ✅ |
| 首页 6 张卡片链接 | ❌ `/chapter4/...` 被解析成 `file:///盘符/chapter4/...`，文件不存在 | ✅ |
| 站内搜索（顶栏搜索框、search.html） | ❌ 浏览器禁止 `file://` 页面 `fetch` 本地 `searchindex.js` | ✅ 中文词与短语均可搜索 |
| 3 个 Marimo 交互页（线性回归、感知机、逻辑回归） | ❌ 永远打不开，见下方说明 | ✅ |

**为什么交互页在 `file://` 下必然空白**：Marimo 服务端返回的
`Content-Security-Policy: frame-ancestors *` 中，按 CSP 规范 `*` 只匹配
`http`/`https`/`ws`/`wss` 这类网络协议，**不包含 `file:`**，
因此嵌入请求会被直接拦截，控制台报 `net::ERR_BLOCKED_BY_RESPONSE`。
这与你的网络、构建配置都无关，必须有一个 `http://` 源才能加载。

> `serve_local.py` 会按 GitHub Pages 的规则把无扩展名路径补全为 `.html`
> （`python -m http.server` 不会，直接访问会 404），因此本地预览与线上行为一致。
> 从 Release 下载的离线网页包同理：解压后也需要执行本脚本才能用搜索与交互。

## 构建 EPUB（新增）

依赖：`pip install nbmerge`，并安装 [pandoc](https://pandoc.org/installing.html)。

```sh
nbmerge $(ls chapter1/*.ipynb chapter2/*.ipynb chapter3/*.ipynb chapter4/*.ipynb | sort) -o combined.ipynb
pandoc combined.ipynb -f ipynb -o release/machine-learning-visualized-zh.epub \
  --toc --embed-resources \
  --lua-filter epub-unpack-cells.lua \
  --resource-path "chapter1:chapter2:chapter3:chapter4:." \
  --metadata-file epub-metadata.yaml
```

> `epub-unpack-cells.lua` 用于去掉 pandoc 给每个 cell 包的 Div，
> 否则 EPUB 无法按章节分文件，整本书会挤成一个 `ch001.xhtml`。

也可以直接推标签自动发布（`.github/workflows/release.yml` 会执行上面的流程，
并额外打包一份离线网页，一起挂到 GitHub Release 页面）：

```sh
git tag v1.0.0
git push origin v1.0.0
```

> 注意：Release 附件只能**下载后查看**，GitHub 不会在 Releases 页面渲染网页；
> 要在线浏览请在 `Settings -> Pages` 把 Source 设为 `GitHub Actions`。

## 效果展示

### Marimo 交互式 Notebook

![Marimo](gifs/marimo.gif)

### 数学推导讲解

![latex](gifs/latex.gif)
