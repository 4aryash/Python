import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

for url in ['https://www.1point3acres.com/bbs/tag-399-1.html']:
  try:
      hdr = {'User-Agent': 'Mozilla/5.0'}
      
      response = requests.get(url)
      # If the response was successful, no Exception will be raised
      response.raise_for_status()
      response.encoding = 'utf-8' # Optional: requests infers this internally
      soup = BeautifulSoup(response.text,features="html.parser")
      for div in soup.findAll('div', attrs={'class':'bm_c'}):
        print(div.find('a')['href'])
        print(div.select('b'))











  except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')  # Python 3.6
    
  except Exception as err:
      print(f'Other error occurred: {err}')  # Python 3.6