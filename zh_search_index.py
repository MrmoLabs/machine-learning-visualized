# -*- coding: utf-8 -*-
"""Sphinx 扩展：补齐中文搜索的「整句/整词」索引。

背景：Sphinx 的中文索引用 jieba 切词（`jieba.cut_for_search`），只把切出来的
词写进 searchindex.js；而搜索页面的查询端不切词，`梯度下降` 会被当成一个整体
去查——若 jieba 把它切成 `梯度` + `下降`，就永远命中不了，结果恒为 0。

补法：在 `split()` 里额外写入文本中**连续的中文串**（按标点/空白切出的最大片段）。
这样：
- 查询是完整中文词（如 `神经网络`）→ 走精确匹配，照常命中；
- 查询是跨词的中文短语（如 `梯度下降`）→ 走 searchtools.js 的部分匹配
  （`term.match(word)`，即索引词条包含查询串），命中所在句子。

只影响索引内容，不改代码、不改公式、不影响英文搜索。
"""
from __future__ import annotations

import re

from sphinx.search import languages
from sphinx.search.zh import SearchChinese

#: 连续的汉字串（不含标点、数字、拉丁字母）
CJK_RUN = re.compile(r"[\u4e00-\u9fff]+")


class SearchChineseWithPhrases(SearchChinese):
    """在 jieba 切词之外，把整段连续中文也登记为索引词条。"""

    def split(self, input: str) -> list[str]:
        tokens = list(super().split(input))
        tokens.extend(m.group() for m in CJK_RUN.finditer(input))
        return tokens


def setup(app):
    # 'zh' / 'zh_CN' / 'zh-CN' 都会回退到 'zh'
    languages["zh"] = SearchChineseWithPhrases
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
