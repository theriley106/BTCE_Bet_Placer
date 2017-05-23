import requests
from bs4 import BeautifulSoup
OrderType = {'BetUp': '0', "BetDown": '1'}
proxies = {}


s = requests.Session()
email = raw_input("Input Email: ")
password = raw_input('Input Password: ')
data = {'email': email,
'password': password}

url = "https://btc-e.com/ajax/login"
r = s.post(url, data=data, proxies=proxies)
soup = BeautifulSoup(r.text)
a = str(soup).split('\n')
for i in range(100):
	print(a[i])

r = s.post('https://btc-e.com/bets', data=data, proxies=proxies)
print(r.text)
soup = BeautifulSoup(s.get('https://btc-e.com/bets').text)
#a = str(soup).split('\n')
#print(len(a))
#for i in range(100):
#	print(a[i])
#hidden_tags = soup.find_all("input", type="hidden")
#csrf = soup.find(id="csrf-token")
#for csrf in hidden_tags:
	#print(csrf)


csrftoken = s.cookies['csrf']
url = 'https://btc-e.com/ajax/betting'
data = {'act':'bet',
'currency':'2',
'type':'0',
'amount':'0',
'csrfToken': csrftoken}
r = s.post(url, data=data, proxies=proxies)
print(r.text)
