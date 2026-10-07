#!/usr/bin/env bash
set -euo pipefail

# 本仓库已将汉化后的 notebook 纳入版本管理，因此默认跳过下载，
# 构建时直接使用仓库中的中文版本（否则 CI 会用上游英文原版覆盖它们）。
# 如需强制同步上游最新版：FORCE_DOWNLOAD=1 ./download_notebooks.sh
download() {
  if [[ -z "${FORCE_DOWNLOAD:-}" && -f "$1" ]]; then
    echo "skip $1 (already in repo; set FORCE_DOWNLOAD=1 to refresh)"
    return 0
  fi
  # Fail on HTTP errors (--fail) and follow redirects (-L) so that a 404 does not
  # get silently written into a .ipynb file and break the build later.
  curl --fail --location --silent --show-error -o "$1" "$2"
}

# Chapter 1
download chapter1/linear_regression.ipynb https://raw.githubusercontent.com/gavinkhung/gradient-descent/refs/heads/main/linear_regression.ipynb
download chapter1/REGRESSION-gradientDescent-data.txt https://raw.githubusercontent.com/gavinkhung/gradient-descent/refs/heads/main/REGRESSION-gradientDescent-data.txt
download chapter1/optimizers.ipynb https://raw.githubusercontent.com/gavinkhung/optimizers/refs/heads/main/optimizers.ipynb

# Chapter 2
download chapter2/pca.ipynb https://raw.githubusercontent.com/gavinkhung/pca/refs/heads/main/pca.ipynb
download chapter2/k_means.ipynb https://raw.githubusercontent.com/gavinkhung/k-means-clustering/refs/heads/main/k_means.ipynb

# Chapter 3
download chapter3/logistic_regression.ipynb https://raw.githubusercontent.com/gavinkhung/logistic-regression/refs/heads/main/logistic-regression.ipynb
download chapter3/perceptron.ipynb https://raw.githubusercontent.com/gavinkhung/perceptron/refs/heads/main/perceptron.ipynb

# Chapter 4
download chapter4/neural_network.ipynb https://raw.githubusercontent.com/gavinkhung/neural-network/refs/heads/main/neural_network.ipynb
download chapter4/plot/nn.svg https://raw.githubusercontent.com/gavinkhung/neural-network/refs/heads/main/plot/nn.svg
download chapter4/plot/architecture/nn-1.png https://raw.githubusercontent.com/gavinkhung/neural-network/refs/heads/main/plot/architecture/nn-1.png

download chapter4/neural_network_weights.ipynb https://raw.githubusercontent.com/gavinkhung/neural-network/refs/heads/main/neural_network_weights.ipynb
download chapter4/autoencoder.ipynb https://raw.githubusercontent.com/gavinkhung/autoencoder/refs/heads/main/autoencoder.ipynb
