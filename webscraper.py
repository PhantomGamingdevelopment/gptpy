import requests
from bs4 import BeautifulSoup
import pandas as pd

# Prompt the user for the URL and output file name
url = input('Enter the URL of the website to scrape: ')
output_file = input('Enter the name of the output CSV file (e.g., data.csv): ')

# Fetch and parse the webpage
response = requests.get(url)
response.raise_for_status()  # Check for request errors

soup = BeautifulSoup(response.text, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

if table is None:
    raise ValueError('No table found on the webpage.')

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    rows.append([cell.text.strip() for cell in cells])

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(rows, columns=headers)
df.to_csv(output_file, index=False)

print(f'Data has been scraped and saved to {output_file}')
