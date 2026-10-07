-- pandoc 的 ipynb 读取器会把每个 cell 包进一个 Div（classes: cell, ...），
-- 导致所有标题都处于嵌套层级，EPUB 写出器按顶层标题拆分章节时看不到它们，
-- 最终整本书只有一个 ch001.xhtml。此过滤器去掉这层包裹，恢复顶层标题结构。
function Div(el)
  for _, c in ipairs(el.classes) do
    if c == 'cell' then
      return el.content
    end
  end
end
