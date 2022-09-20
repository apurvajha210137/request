import requests 
cookies = {     '0ctf_csrf_cookie': '3998553cf82532bf79c9d23492e176b6',     'ctf_session': 'd90a6af1c5d13c2a7a7976463429ea29539daaad', } 
headers = {     'sec-gpc': '1',     'upgrade-insecure-requests': '1',     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36', } 
data = {     '0ctf_csrf_token': '3998553cf82532bf79c9d23492e176b6',     'email': 'admin@admin.com',     'password': 'dsdsf', } 
response = requests.post('https://ctf.0ops.sjtu.cn/login', 
cookies=cookies, headers=headers, data=data) print(response.text)