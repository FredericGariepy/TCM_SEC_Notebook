import requests
from bs4 import BeautifulSoup
import re

def get_obfuscated_test():
    website='https://3e108f08d6a86cde.247ctf.com/'
    r = requests.get(url=website)

    if r.status_code ==200:
        soup = BeautifulSoup(r.content,'html.parser')

        script_tag =  soup.find('script')
        script_content =  script_tag.text[89:-23] #content between junk
        with open('obfuscatedScript.txt', 'w') as f:
            f.write(script_content)
