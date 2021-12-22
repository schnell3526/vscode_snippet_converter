import snippets

from collections import OrderedDict
import json

class Converter:
    def test(self):
        print("hello converter")
    
    def convert(self, src:str, prefix:str, description:str) -> str:
        """
        ソースコードをvscodeスニペット形式に変換\n
        Example:
        "Print to console": {
            "prefix": "log",
            "body": [
                "console.log('$1');",
                "$2"
            ],
            "description": "Log output to console"
        }
        """
        
        lines = src.strip().split("\n")

        snippet = OrderedDict()
        snippet[prefix] = OrderedDict()
        snippet[prefix]["prefix"] = prefix
        snippet[prefix]["body"] = lines
        snippet[prefix]["description"] = description

        res = json.dumps(snippet, indent=4, ensure_ascii=False)
        return res
