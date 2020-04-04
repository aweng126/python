import tldextract

if __name__ == '__main__':
    url = 'www.kingwen.cn'
    res = tldextract.extract(url)
    print(res.subdomain, res.domain, res.suffix) # www kingwen cn
    print(res.registered_domain) # kingwen.cn
    url1 = 'localhost:8080/hello'
    res = tldextract.extract(url1)
    print(res.subdomain, res.domain, res.suffix) # ''  localhost  ''
