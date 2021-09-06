# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Clarkesworld
# 
# Source: https://clarkesworldmagazine.com/
# 
# Description: Sci-fi/fantasy magazine
# 
# **Topics:**
# 
# * Scraping
# %% [markdown]
# ## Scrape the Clarkesworld homepage `4 points`
# 
# I want a CSV file that includes a row for each story, including the columns:
# 
# * Title
# * Byline
# * URL to story
# * Category (fiction/non-fiction/cover art)
# * Issue number (e.g. 180)
# * Publication date (e.g. September 2021)

# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd


# %%
url = 'https://clarkesworldmagazine.com/'
response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')


# %%
sep = ' – '
issue_date = doc.find(class_='issue').text
issue = issue_date.split(sep)[0]
date = issue_date.split(sep)[1]

print(issue,sep, date)


# %%
rows = []

for section in doc.select('.index-table .index-table'):
    category = section.find(class_='section').text
    for article in section.findAll('div', {'class':['index-col1', 'index-col2']}):
        row = {}
        row['category'] = category
        row['issue'] = issue
        row['date'] = date
        row['title'] = article.find(class_='story').text
        row['byline'] = article.find(class_='byline').text
        row['link'] = article.find('a')['href']
        # print(row)
        rows.append(row)


# %%
df = pd.DataFrame(rows)
df


# %%
filename = 'clarkesworld/stories.csv'

df.to_csv(filename, index=False)

# %% [markdown]
# ## Auto-updating scraper `3 points`
# 
# Using GitHub Actions, implement a scraper that will keep track of everything posted to the Clarkesworld homepage. For example, when issue 181 comes out it should *add to the CSV* instead of just replacing it.
# 
# > Tip: `drop_duplicates` might save you a lot of effort at one point or another.

# %%
pd.read_csv(filename).append(df).drop_duplicates().to_csv(filename, index=False)


