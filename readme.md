# snippets
コードをvscodeのsnippet設定ファイルに記入できる形式に変換するライブラリ

## インストール方法

```bash
pip install git+https://github.com/schnell3526/vscode_snippet_converter
```

## 使い方

以下のようにソースコード、prefix、descriptionを指定する。

```python
import snippets

converter = snippets.Converter()

src = \
r"""
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("hello world!")
}
"""

prefix = "hello world"
description = "print greeting message to console"
print(converter.convert(src, prefix, description))

# {
#     "hello world": {
#         "prefix": "hello world",
#         "body": [
#             "#include <stdio.h>",
#             "#include <stdlib.h>",
#             "",
#             "int main(int argc, char *argv[]) {",
#             "    printf(\"hello world!\")",
#             "}"
#         ],
#         "description": "print greeting message to console"
#     }
# }
```

現状一番外側に余計なカッコが出てしまいます。どのような出力が一番便利なのか検討を重ねて変更するかもしれないです。