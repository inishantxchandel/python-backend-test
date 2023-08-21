import requests
from bs4 import BeautifulSoup
import re

def extract_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        social_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'facebook' in href or 'linkedin' in href:
                social_links.append(href)
        
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, response.text)
        
        phone_pattern = r'\+\d{1,4}\s\d{1,4}\s\d{1,4}\s\d{1,4}'
        contacts = re.findall(phone_pattern, response.text)
        
        print("Social links:")
        for link in social_links:
            print(link)
        
        print("\nEmail:")
        for email in emails:
            print(email)
        
        print("\nContact:")
        for contact in contacts:
            print(contact)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

url = "https://ful.io/"

extract_details(url)
