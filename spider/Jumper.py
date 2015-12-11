import requests
import requests.cookies as cook

class Jumper:
    head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

    def __init__(self,url,proxies):
        self.url = url
        self.session = requests.session()
        self.cookies = None
        self.proxies = proxies

    def setcookiejar_from_dict(self,dict):
        self.cookies = cook.cookiejar_from_dict(dict)

    def post(self,url=None,data=None,redirect=False):
        if url is None:
            url=self.url

        head = self.head
        head['cache-control'] = 'max-age=0'
        head['content-type'] = 'application/x-www-form-urlencoded'
        content = None
        try:
            req = self.session.request(method='post', url=url, cookies=None, data=data, headers=head, allow_redirects=redirect)

        except requests.ConnectionError(),error:
            print error
        else:
            content=req.content
        return content

    def show(self, req):
        print req.status_code
        print 'hisotry:'
        print req.history
        print 'head:'
        print req.headers
        print 'redirect: ' + str(req.is_redirect)
        print 'links: ' + str(req.links)
        print 'cookies:'
        print req.cookies
        self._save('page.html', req.content)
        self._save('headers.txt', req.headers)
        self._save('cookie.txt', req.cookies)

    def jump(self,args):
        content=None
        try:
            req = self.session.request(method='get', url=self.url,cookies=self.cookies, params=args, headers=self.head,proxies=self.proxies)
        except requests.exceptions.ConnectionError,err:
            print err

        else:
            content = req.content
        return content

    def raw(self,url):
        raw = None
        try:
            req = self.session.request(method='get', url=url,cookies=self.cookies, headers=self.head,proxies=self.proxies,stream=True)
        except requests.exceptions.ConnectionError,err:
            print err

        else:
            raw= req.raw
        return raw

    def close(self):
        self.session.close()
