#!/usr/bin/env python
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request as ur

# Enter company information
# Refer to: https://www.wsj.com/market-data/quotes/company-list/

# Malayan Banking Bhd
#co_info = {
#        "country": "MY",
#        "exchange": "XKLS",
#        "code": "1155"
#        }

# Singapore Airlines Ltd.
co_info = {
        "country": "SG",
        "exchange": "XSES",
        "code": "C6L"
        }

# URL link 
url_wsj = '/'.join(str(x) for x in co_info.values())
url_wsj = 'https://www.wsj.com/market-data/quotes/' + url_wsj + '/financials/annual/balance-sheet'
#print(url_wsj)

req = ur.Request(
    url_wsj, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
read_data = ur.urlopen(req).read()
soup_page = BeautifulSoup(read_data,'lxml')

# Get the data table
data_header = []
data_body = []
for container in soup_page.find_all('table', class_='cr_dataTable'):
    # Get the table header
    # Skip it if we already have the header
    if len(data_header) == 0:
        thead = container.find("thead")
        for tr in thead.find_all("tr"):
            _data = []
            # exclude the mini bar chart in last column
            for th in tr.find_all("th")[:-1]:
                _data.append(th.text)
            # add label
            _data[0] = 'Year'
            if _data:
                data_header = _data
    
    # Get the table body in multiple containers
    tbody = container.find("tbody")
    for tr in tbody.find_all("tr"):
        # Skip hidden row
        #_class = tr.get("class")
        #if _class is not None and len(_class) and "hide" == _class[0]:
        #    continue

        # exclude the mini bar chart in last column
        td = tr.find_all('td')[:-1]
        for val in td:
            if val.text and val.text.strip():
                data_body.append(val.text)

# Convert data into pandas dataframe
data_header.extend(data_body)
data = list(zip(*[iter(data_header)]*6))
df = pd.DataFrame(data[0:])
df.replace('-', np.NaN, inplace=True)
with pd.option_context('display.max_rows', 200, 'display.max_columns', 10):
    print(df)
