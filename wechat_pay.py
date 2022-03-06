import hashlib
import random
import time  # 引入time模块
import urllib.parse
import urllib.request
import urllib.request

try:
    import pycurl
    from cStringIO import StringIO
except ImportError:
    pycurl = None


def createNoncestr(length=32):
    """产生随机字符串，不长于32位"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    strs = []
    for x in range(length):
        strs.append(chars[random.randrange(0, len(chars))])
    return "".join(strs)


def formatBizQueryParaMap(paraMap, urlencode):
    """格式化参数，签名过程需要使用"""
    slist = sorted(paraMap)
    buff = []
    for k in slist:
        v = urllib.parse.quote(paraMap[k]) if urlencode else paraMap[k]
        buff.append("{0}={1}".format(k, v))

    return "&".join(buff)


def arrayToXml(arr):
    """array转xml"""
    xml = ["<xml>"]
    for k, v in arr.items():
        if v.isdigit():
            xml.append("<{0}>{1}</{0}>".format(k, v))
        else:
            xml.append("<{0}><![CDATA[{1}]]></{0}>".format(k, v))
    xml.append("</xml>")
    return "".join(xml)


ss = int(round(time.time() * 1000))  # 毫秒级时间戳
# 请求地址url
url = "https://api.mch.weixin.qq.com/pay/micropay"

# 发送给服务器的数据
# 构建发送数据
# =======【基本信息设置】=====================================
# 微信公众号身份的唯一标识。审核通过后，在微信发送的邮件中查看
APPID = "wx3******"
# 商户ID，身份标识
MCHID = "1364****"
# 商户支付密钥Key。审核通过后，在微信发送的邮件中查看
KEY = "******"
# =======【证书路径设置】=====================================
# 证书路径,注意应该填写绝对路径
SSLCERT_PATH = "/******/cacert/apiclient_cert.pem"
SSLKEY_PATH = "/******/cacert/apiclient_key.pem"
# =======【curl超时设置】===================================
CURL_TIMEOUT = 30
# =======【支付信息】=====================================
goodsbody = '***购物广场'  #商品信息
out_trade_no = "PY" + time.strftime("%Y%m%d%H%M%S", time.localtime())  # 商户单据号
total_fee = "1"  # 支付金额
spbill_create_ip = "192.168.1.1"
auth_code = "134685557443922177"  # 付款码
nonce_str = createNoncestr()

# =======【支付信息构造】=====================================
jsonData = {}
jsonData['appid'] = APPID
jsonData['mch_id'] = MCHID
jsonData['nonce_str'] = nonce_str
jsonData['body'] = goodsbody
jsonData['out_trade_no'] = out_trade_no
jsonData['total_fee'] = total_fee
jsonData['spbill_create_ip'] = '192.168.1.1'
jsonData['auth_code'] = auth_code

# 1.对参数按照key=value的格式，并按照参数名ASCII字典序排序生成字符串：
String = formatBizQueryParaMap(jsonData, False)
print('json转字符串：' + String)
# 2.连接密钥key：
String = String + '&key=' + KEY
print('连接密钥的字符串：' + String)  # 计算签名用的字符串
# jsonData['key'] = KEY   #后添加key是因为key不参与排序，因为不参与计算，不添加也可以
ParamStr = {}
ParamStr['appid'] = APPID
ParamStr['mch_id'] = MCHID
ParamStr['nonce_str'] = nonce_str
ParamStr['body'] = goodsbody
ParamStr['out_trade_no'] = out_trade_no
ParamStr['total_fee'] = total_fee
ParamStr['spbill_create_ip'] = spbill_create_ip
ParamStr['auth_code'] = auth_code
# 3.生成sign并转成大写：
# APIV2 md5签名 扫码付款暂时还没有V3版的api
ParamStr['sign'] = hashlib.md5(String.encode('utf-8')).hexdigest().upper()
# 4生成提交的xml
String = arrayToXml(ParamStr)
print(String)
# =======【支付提交】=====================================
# 5 POST发送的data必须为bytes或bytes类型的可迭代对象，不能是字符串
form_data = bytes(String, encoding='utf-8')
#
# 6 构造请求对象Request
req = urllib.request.Request(url, data=form_data)
#
# 7 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode()
# 8 支付结果
print(data)
en = int(round(time.time() * 1000))  # 毫秒级时间戳
print('过程耗时：', en - ss, '毫秒')
