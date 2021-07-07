# Overview
This python script extracts the company balance sheet report from WSJ Markets.

# Requirements
- Python 3
- PIP for the above Python 3

# Installation
1. Unzip the package `wsj.zip`
2. Setup the Python virtual environment in the above unzipped directory
   ```
    # python3 -v mvenv /path/to/wsj
    # cd /path/to/wsj
    # source bin/activate
   ```
3. Install the required Python modules
    ```
   # pip install -r requirements.txt
   ```
# Execution
1. Open the file `wsj.py` and modify the company settings according to the information from [WSJ](https://www.wsj.com/market-data/quotes/company-list/)
    > Hint: Look at the URL of the company page
    ```
    co_info = {
	    "country": "SG",
	    "exchange": "XSES",
	    "code": "C6L"
    }
    ```
2. Execute the following command:
    ```
   # python wsj.py
    ```

