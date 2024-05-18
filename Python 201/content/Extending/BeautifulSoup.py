import requests
from bs4 import BeautifulSoup

# URL of the weather page
url = "https://weather.com/en-TT/weather/tenday/l/Busan+South+Korea?canonicalCityId=860c52518619a09bb91b8517c5eec85e632b004d0bd1ffcaca926a709b12cea7"

# request to fetch the HTML content
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# parse the HTML with bs4
soup = BeautifulSoup(response.content, 'html.parser')

# find the first weather section
first_daypart_details = soup.find('div', class_='DaypartDetails--Content--2Yg3_ DaypartDetails--contentGrid--2_szQ')

# extract details from first section
date = first_daypart_details.find('span', class_='DailyContent--daypartDate--3VGlz').get_text()
temperature = first_daypart_details.find('span', class_='DailyContent--temp--1s3a7').get_text()
condition = first_daypart_details.find('div', class_='DailyContent--Condition--1zRBJ').find('svg').get('aria-label')
narrative = first_daypart_details.find('p', class_='DailyContent--narrative--3Ti6_').get_text()

# print details
print(f"Date: {date}")
print(f"Temperature: {temperature}")
print(f"Condition: {condition}")
print(f"Narrative: {narrative}")
