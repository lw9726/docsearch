import unittest

from website.crawl.cnki_spiders import *

ARTICLE_URL = "dbcode=CAPJ&dbname=CAPJDAY&filename=ZZDZ20210513000"
# AUTHOR_URL = "skey=王宁&code=33167488"
# AUTHOR_URL = "skey=傅广生&code=05967496"
AUTHOR_URL = "skey=王颖&code=07079336"
# AUTHOR_URL = "skey=杜会静&code=07074873"
SOURCE_URL = "DBCode=cjfq&BaseID=ZZDZ"
ORGANIZATION_URL = "DBCode=CDMD&BaseID=GBYDU"
article = Article(ARTICLE_URL)
author = Author(AUTHOR_URL)
source = Source(SOURCE_URL)
organization = Organization(ORGANIZATION_URL)
db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnkidemo', port=3306, charset='utf8')


class MyTestCase(unittest.TestCase):
    def test_keyList_crawl(self):
        """测试检索页"""
        flag = False
        key = "人工智能"
        try:
            k = KeyList()
            k.input_keyword(key)
            k.crawl_qikan()
            k.crawl_lunwen()
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取关键词列表错误")

    def test_article_crawl(self):
        """测试爬取单个文献"""
        item = article.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_article_store(self):
        """存储单个文献"""
        flag = False
        try:
            article.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取文献错误")

    def test_author_crawl(self):
        """测试爬取单个作者"""
        item = author.crawl()
        print(item)
        author.close()
        self.assertIsNotNone(item, '无')

    def test_author_store(self):
        """测试存储单个作者"""
        flag = False
        try:
            author.store(db)
            author.close()
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取作者错误")

    def test_source_crawl(self):
        """测试爬取单个文献来源"""
        item = source.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_source_store(self):
        """测试存储单个文献"""
        flag = False
        try:
            source.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取文献来源错误")

    def test_organization_crawl(self):
        """测试爬取单个组织"""
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_organization_store(self):
        """存储组织"""
        flag = False
        try:
            organization.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取组织错误")

    def test_getArticleUrls(self):
        """测试sql：未爬取的文献"""
        urls = getArticleUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlArticle(self):
        """测试：爬取并存储未爬取的文章"""
        try:
            urls = getArticleUrls(db)
            crawlArticle(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的文章异常")
        self.assertTrue(True)

    def test_getSource(self):
        """获取未被爬取的来源列表"""
        urls = getSourceUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlSource(self):
        """爬取未被爬取的来源"""
        try:
            urls = getSourceUrls(db)
            crawlSource(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的来源异常")
        self.assertTrue(True)

    def test_getAuthor(self):
        """获取未被爬取的作者列表"""
        urls = getAuthorsUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlAuthor(self):
        """爬取未被爬取的作者"""
        try:
            urls = getAuthorsUrls(db)
            print("url的个数为", len(urls))
            print(url for url in urls)
            crawlAuthor(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的作者异常")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
