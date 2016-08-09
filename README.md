# The Code Golf Museum

### crawler.py
A web parser/link collector.

Takes arguments of the start URL, and depth of collection, with an optional argument for a URL prefix to restrict search by.

Examples:
```bash
crawler.py https://python.org/ 3
crawler.py https://python.org/ 3 https://python.org/
```

### regparser.py
A windows registry parser which prints windows startup programs (only tested on win7)
