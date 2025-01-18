import requests
from bs4 import BeautifulSoup

url = 'https://www.rsaconference.com/usa/expo-and-sponsors#sort=%40name%20ascending&numberOfResults=100&f:product=[Device%20Security,Endpoint%20Security,Security%20Operations%20and%20Incident%20Response,Threat%20Intelligence]'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

company_links = soup.findAll('a', class_ = 'CoveoResultLink')

company_names = [link.text for link in company_links]
print(company_names)