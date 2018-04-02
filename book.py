###
   Test books
###

import requests;
import urlparse
base_url = 'http://localhost:8000'
def test_books():
    """测试所有的books"""
    resource = '/api/books'
    url = urlparse.urljoin(base_url, resource)
    r = requests.get(url)
    try:
        books = r.json()
        for book in books:
            if not book.get('title', None):
                print 'test_books title is null', book.get('id', 0)
        print('ok')
    except:
        print  'test_books result not json'

def test_book():
    "测试一本数"
    pass
def create_book():
    '创建一本书'
    pass
def update_book():
    "更新一本书"
    pass
def delete_book():
    "删除一本书"
    pass


# format
# 字符串拼接