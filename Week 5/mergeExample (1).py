#%%
import pandas as pd
import re
import numpy as np

#%%
bitcoinFile ="./bitcoin_cash_price.csv"
dashFile = "./dash_price.csv"

bitcoin_df = pd.read_csv(bitcoinFile)
dash_df = pd.read_csv(dashFile)

onlyNumbers = re.findall("[0-9]+",bitcoin_df["Market Cap"][0])

# %%
tmp =""
for number in onlyNumbers:
    tmp = tmp + number
print(tmp)
print(type(tmp))

# %%
int(tmp)

# %%
# stringToInt("123")

#%%
def stringToInt(someString: str) -> (int, None):
    matchingCharacters = re.findall("[0-9]+",someString)
    out = ""
    for character in matchingCharacters:
        out = out + character
    if len(out) < 1:
        return None
    else:
        return int(out)

# %%
bitcoin_df['Market Cap'].apply(stringToInt)
marketCaps = bitcoin_df['Market Cap'].apply(stringToInt)
marketCaps = marketCaps.dropna()
marketCaps.apply(int)

#%%
bitcoin_df = bitcoin_df.drop(columns = ["Market Cap"])

dash_df = dash_df.drop(columns = ['Market Cap'])

bitcoin_dash_df = pd.merge(dash_df,bitcoin_df, how = 'inner', on = "Date", suffixes = ("_dash","_bitcoin"))

# %%
def percentChange(old: float, new: float) -> float:
    return((new-old)/old)*100

def GreaterPercentChange(dash: float, bitcoin: float) -> str:
    result = np.where(dash > bitcoin,'Dash','Bitcoin')
    return(str(result))

# %%
bitcoin_dash_df["Percent Change Dash"] = percentChange(bitcoin_dash_df["Open_dash"],bitcoin_dash_df["Close_dash"])
bitcoin_dash_df["Percent Change Bitcoin"] = percentChange(bitcoin_dash_df["Open_bitcoin"],bitcoin_dash_df["Close_bitcoin"])
bitcoin_dash_df["Biggest Percent Change"] = np.where(bitcoin_dash_df["Percent Change Dash"] > bitcoin_dash_df["Percent Change Bitcoin"], "Dash", "Bitcoin")
# %%
