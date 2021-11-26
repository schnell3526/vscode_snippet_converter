import unittest
import snippets

class TestConverter(unittest.TestCase):
    """
    test class of snippets.Converter
    """

    def test_convert(self):
        input = \
"""
#include <iostream>
#include <vector>

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long d = extGCD(b, a%b, y, x);
    y -= a/b * x;
    return d;
}

int main() {

}
"""
        prefix = "kyopro"
        description = "template for kyopro"

        expected = \
"""
{
    "kyopro": {
        "prefix": "kyopro",
        "body": [
            "#include <iostream>",
            "#include <vector>",
            "",
            "long long extGCD(long long a, long long b, long long &x, long long &y) {",
            "    if (b == 0) {",
            "        x = 1;",
            "        y = 0;",
            "        return a;",
            "    }",
            "    long long d = extGCD(b, a%b, y, x);",
            "    y -= a/b * x;",
            "    return d;",
            "}",
            "",
            "int main() {",
            "",
            "}"
        ],
        "description": "template for kyopro"
    }
}
"""     
        expected = expected.strip()
        result = snippets.Converter().convert(input, prefix, description)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
