# duplines

duplines cli eliminates duplicate lines in a file and keeps the sorting order

```bash
+-------+
|       |
|  foo  |
|  bar  |              +-------+
|  bar  |              |       |
|  foo  |              |  foo  |
|  bar  +------------->+  bar  |
|  baz  |              |  baz  |
|  foo  |              |       |
|  bar  |              +-------+
|       |
+-------+
```

# Installation

Simply run:

    $ pip install .


# Usage

To use it:

    $ duplines --help

