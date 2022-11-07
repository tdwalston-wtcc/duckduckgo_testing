#
# Tyler Walston
# November 6, 2022
# DuckDuckGo API Testing
#

import pytest
import requests

# Define URLs for DuckDuckGo and for search query
ddg = "https://api.duckduckgo.com"
url = "https://duckduckgo.com/?q=presidents+of+the+united+states&format=json"

# Use GET request to obtain search results
response = requests.get(url)

# Parse data to JSON format
response_data = response.json()

# Create list of RelatedTopics
api_results = response_data['RelatedTopics']

# Add data to string for text searching
api_text = ""
for result in api_results:
    api_text += result['Text']

# List of US Presidents (excluding duplicate last names)
presidents_list = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Van Buren', 'Harrison', 'Tyler',
                   'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes',
                   'Garfield',
                   'Arthur', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover',
                   'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush',
                   'Clinton',
                   'Obama', 'Trump', 'Biden']


# Test for functioning of DuckDuckGo
def test_ddg_1():
    resp = requests.get(ddg)
    assert resp.status_code == 200


# Test for "DuckDuckGo" heading in GET request to API
def test_ddg_2():
    resp = requests.get(ddg + "/?q=DuckDuckGo&format=json")
    resp_data = resp.json()
    assert "DuckDuckGo" in resp_data["Heading"]


# Test for functioning of search query
def test_url():
    resp = requests.get(url)
    assert resp.status_code == 200


# Test that API data was properly parsed to JSON format
def test_data():
    assert type(response_data) == dict


# Test that each US President's last name appears in the search query
def test_presidents():
    for name in presidents_list:
        assert name in api_text
