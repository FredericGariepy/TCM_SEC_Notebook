Make HTTP requests with the requests module.
`pip install requests` and `import requests` to get started.

#### Store the response Object.
`resp_obj = requests.get('http://https://httpbin.org/get')`
#### Methods
| explannation | method | example |
| - | - | - |
| show headers as dictionary | `.headers` | r.headers |
| access header | `.headers['key']` | r.headers['Server'] |
| status code |  `.status_code` | r.status_code |
| send to receive time (Time Delta) | `.elapsed` | r.elapsed |
| cookie jar from server in response |  `.cookies` | r.cookies |
| response in _bytes_ | `.response` | r.response |
| response in _UNICODE_ | `.text` | r.text |
| request with params as dict |`.get('url',params={'key':'val}` | requests.get('http://https://httpbin.org/get', params={'id':1} ) |
| request with headers as dict|`.get('url',headers={'key':'val}`| requests.get('http://https://httpbin.org/get', headers={'Accept':'application/json', 'evil':'intentions'}) |
| delete | `.delete('url')` | 'r.delete(http://https://httpbin.org/delete') |
| post | '.post('url')` | r.post(http://https://httpbin.org/post', data={'data':123, 'data2':456}) |

#### Sending multi-part encoded files
`wget` image
```
# bash
wget url/resource/endpoint -0 filename
```
post image with python requests
```
# python
files = {'file': open('img.png': 'rb')} # rb = read bytes
r = requests.post('url', file = files)
```
#### basic authorization
`r.get('url', auth=('username','password'))`
__output__
```
print(r.text)
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ=",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-65f79fce-4c62345e1f54a818575ed409"
  },
  "origin": "185.216.231.60",
  "url": "http://httpbin.org/get"
}
```


