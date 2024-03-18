<img src="https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png" alt="Requests" width="100">

Make HTTP requests with the [requests module](https://requests.readthedocs.io/en/latest)
 
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
| post | `.post('url')` | r.post(http://https://httpbin.org/post', data={'data':123, 'data2':456}) |
| response as JSON | `.json()` | After request r is made, r.json() |

#### Sending multi-part encoded files
`wget` image
```bash
wget url/resource/endpoint -0 filename
```
post image with python requests
```python
files = {'file': open('img.png': 'rb')} # rb = read bytes
r = requests.post('url', file = files)
```
### basic authorization
`r.get('url', auth=('username','password'))`

__output:__
```bash
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
#### Auth decode 
 `"Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ="`
##### bash
`echo -ne dXNlcm5hbWU6cGFzc3dvcmQ= | base64 -d`

__output:__

`username:password`

#### Invalid SSL certificate
_Request will make its own due-dilligence in regards to SSL_

`requests.get(https://expired.badssl.com')`

__>>>__ ... __[SSL: CERTIFICATE_VERIFY_FAILED]__
##### bypass expired exception `verify=False`
`requests.get(https://expired.badssl.com',verify=False)`

__>>>__ ... __[InsecureRequestWarning: Unverified...]__

_Opens up request to get MIM'd_

#### 301 Redirects, `allow_redirects=False`
Request will perform redirections for all verbs, except HEAD.
```python
rd = requests.get('http://github.com',allow_redirects=False)
rd.headers
>>> {'Content-Length': '0', 'Location': 'https://github.com/'}
r.status_code
>>> 301
```

#### request with timeout `timeout=0.01`
`r = requests.get(https://github.com',timeout=0.01)`

__Output:__
```bash
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.VerifiedHTTPSConnection object at 0x7f95268e2d30>, 'Connection to github.com timed out. (connect timeout=0.01)'))
```
#### Statefull request, perssist data, session.
##### With cookies (cummbersome)
`c = requests.get('https://httpbin.org/cookies', cookies={'a': 'b'})`
##### With Sessions
```python
s =  requests.Session()
s.cookies.update({'a':'b'})
s.get('https://httpbin.org/cookies')
```
#### download and save to disk
```python
x  = requests.get('url/path/to/resource')
with open(file.type, 'wb') as f: # wb =  write bytes
    f.write(x.content)
``` 
