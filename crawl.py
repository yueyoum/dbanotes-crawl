import sys
import re
import urllib2


class Crawl(object):
    def __init__(self, site="http://news.dbanotes.net/"):
        self.site_fd = urllib2.urlopen(site)

    def dumps(self, filename):
        data = self.process()
        if isinstance(data, unicode):
            data = data.encode('utf-8')

        with open(filename, 'w') as f:
            f.write(data)

    def process(self):
        # subclass should overwrite this method
        raise NotImplemented()



class LxmlCrawl(Crawl):
    def process(self):
        from lxml import etree

        parse = etree.HTMLParser()
        tree = etree.parse(self.site_fd, parse)

        titles = tree.xpath('//td[@class="title"]/a/text()')
        links = tree.xpath('//td[@class="title"]/a/@href')

        data = '\n'.join(['%s %s' % (title, link) for title, link in zip(titles, links) if title != 'More'])
        return data


class ReCrawl(Crawl):
    def process(self):
        html = self.site_fd.read()
        pattern = re.compile(r'\<td class="title"\>\<a.+?href="(.+?)".*?\>(.+?)\</a\>')
        result = pattern.findall(html)
        data = '\n'.join(['%s %s' % (title, link) for link, title in result if title != 'More'])
        return data


if __name__ == '__main__':
    from optparse import OptionParser
    parse = OptionParser()

    parse.add_option(
        '--lxml',
        action='store_true',
        dest='using_lxml',
        default=False,
        help='Using lxml library to parse html. Default using Re library'
    )

    parse.add_option(
        '-o',
        type='string',
        dest='filename',
        default='result.txt',
        help='Output file. Default is "result.txt"'
    )

    options, args = parse.parse_args(sys.argv)
    worker = LxmlCrawl() if options.using_lxml else ReCrawl()
    worker.dumps(options.filename)

