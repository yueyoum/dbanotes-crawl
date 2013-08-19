## 使用方法

```bash
$: python crawl.py -h
Usage: crawl.py [options]

Options:
  -h, --help   show this help message and exit
  --lxml       Using lxml library to parse html. Default using Re library
  -o FILENAME  Output file. Default is "result.txt"
```

用参数`-h` 运行程序会输出可选参数：

*   `--lxml`: 如果没有添加此参数，那么默认使用Python的标准正则库re来提取所需信息。

    如果使用了此参数，那么将使用lxml库来解析网页内容。

    使用lxml有两个好处：
    *   利用xpath来提取所需内容，比re简单。（在这个简单的例子中没体现出来）
    *   运行效率更高

    **注意**, 如果要`pip install lxml`， 那么需要计算中先安装`libxml2`和`libxslt`的头文件。
    ubuntu系统可以这样安装： `apt-get install libxml2-dev libxslt-dev`

*   `-o <FILE>` 此参数指定提取出内容的输出文件。不指定。默认就为当前文件夹下result.txt文件

## 如何运行

1.  `python crawl.py`
2.  `python crawl.py -o /tmp/output`
3.  `python crawl.py --lxml`
