# -*- coding: utf-8 -*-
import urllib2
import urllib


def get_html(link, params=None, cp949=False, chunk_size=None, headers=[('User-Agent', 'Mozilla/1.0 beta')]):
    """
    :param link: 접속할 링크정보를 의미한다.
    :param cp949: CP949 유무를 의미한다.  기본값은  False 이다.
    :param chunk_size: 앞쪽 일부 내용만 필요한 경우를 대비한 사이즈 크기를 의미한다.
    :param params:  POST 형태의 파라미터를 의미한다.
    :param headers: [(key, value)]  헤더의 정보를 의미한다. 기본적으로  User-Agent 정보에 Mozilla 정보를 채워준다.
    :return:
    """
    req = urllib2.Request(link)
    for h in headers:
        k, v = h
        req.add_header(k, v)

    if params:
        params = urllib.urlencode(params)

    handle = urllib2.urlopen(req, data=params, timeout=5)

    if chunk_size:
        data = handle.read(chunk_size)
    else:
        data = handle.read()
    data = data.decode('cp949', 'ignore') if cp949 else data
    handle.close()
    return data




if __name__ == '__main__':
    print get_html('http://m.stock.naver.com/api/item/getPriceDayList.nhn?code=000250&pageSize=20&page=1')