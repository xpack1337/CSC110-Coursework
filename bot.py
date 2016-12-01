token = 'REALTOEKEN'
url = 'https://api.telegram.org/bot{}'.format(token)
import urllib.parse
import urllib.request
def getMe():
    return url + '{}'.format('/getMe')
def getUpdates():
    return url + '{}'.format('/getUpdates')
def sendMessage (chat_id, text):
    url1 = url + '/sendMessage'
    values = {'chat_id':chat_id,'text':text}
    request = urllib.parse.urlencode(values)
    request = request.encode('utf-8')
    resp = urllib.request.Request(url1,request)
    return urllib.request.urlopen(resp)
def sendVideo (chat_id,video):
    url1 = url + '/sendVideo'
    values = {'chat_id':chat_id,'video':video}
    request = urllib.parse.urlencode(values)
    request = request.encode('utf-8')
    resp = urllib.request.Request(url1,request)
    return urllib.request.urlopen(resp)
def sendPhoto 
