import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

url = 'http://www.renren.com/SysHome.do'
response = urllib2.urlopen(url)
source = response.read()
soup = BeautifulSoup(source,'lxml')
#获取登录地址
log_url = soup('form',{'method':'post'})[0]['action']
#通过 Fiddler或Google Chrome开发者工具获取表单数据
form_data = {
            'email':'youremail','icode':'','origURL':'http://www.renren.com/home',
            'domain':'renren.com','key_id':1,'captcha_type':'web_login','password':
            'YourEncodePassword',
            'rkey':'cd0070708c41ed126d94d91b7bf2066c','f':'http%3A%2F%2Fwww.renren.com%2F821461363'
    }

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

try:
        r = urllib2.urlopen(log_url,urllib.urlencode(form_data))
        print r.read()
except urllib2.URLError,e:
        if hasattr(e,'reason'):
                print 'reason:{0}'.format(e.reason)
        if hasattr(e,'code'):
                print 'code:{0}'.format(e.code)







