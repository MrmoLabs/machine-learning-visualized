# -*- coding: utf-8 -*-
"""本地预览服务器：按 GitHub Pages 的规则，把无扩展名的路径自动映射到 .html。

GitHub Pages 会把 `/chapter4/neural_network_weights` 解析成
`chapter4/neural_network_weights.html`，而 Python 自带的 http.server 不会，
直接访问会 404。用这个脚本即可在本地 1:1 还原线上行为，站内搜索也可用。

用法：
    python serve_local.py            # 默认 http://localhost:8000 ，目录 _build/html
    python serve_local.py --port 8080 --dir _build/html
"""
import argparse
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class CleanUrlsHandler(SimpleHTTPRequestHandler):
    """把 /foo 解析成 /foo.html（与 GitHub Pages 行为一致）。"""

    def translate_path(self, path):
        fs_path = super().translate_path(path)
        if not os.path.splitext(fs_path)[1] and os.path.isfile(fs_path + ".html"):
            return fs_path + ".html"
        return fs_path

    def log_message(self, fmt, *args):  # 只打印 404，减少噪音
        if args and str(args[1]).startswith(("404", "500")):
            super().log_message(fmt, *args)


def main():
    ap = argparse.ArgumentParser(description="预览 Jupyter Book 构建结果")
    ap.add_argument("--dir", default=os.path.join("_build", "html"), help="要托管的目录")
    ap.add_argument("--port", type=int, default=8000, help="端口号，默认 8000")
    ap.add_argument("--host", default="127.0.0.1", help="默认只监听本机")
    args = ap.parse_args()

    root = os.path.abspath(args.dir)
    if not os.path.isdir(root):
        raise SystemExit("目录不存在：%s（请先运行 jupyter-book build .）" % root)

    handler = partial(CleanUrlsHandler, directory=root)
    with ThreadingHTTPServer((args.host, args.port), handler) as httpd:
        print("预览地址: http://localhost:%d/   （Ctrl+C 停止）" % args.port)
        print("托管目录: %s" % root)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n已停止")


if __name__ == "__main__":
    main()
