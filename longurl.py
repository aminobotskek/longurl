import requests
class Client():
	def __init__(self):
		self.api="https://longurl.in/api"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def get_short_url(self,url):
		data={"longURL":url}
		return requests.post(f"{self.api}/create-url",json=data,headers=self.headers).json()
	def get_url_info(self,url):
		data={"shortURL":url}
		return requests.post(f"{self.api}/expand-url",json=data,headers=self.headers).json()