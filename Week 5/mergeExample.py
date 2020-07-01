#%%
import pandas as pd
import re

# %%
bitcoinFile = "./bitcoin_cash_price.csv"
dashFile = "./dash_price.csv"

bitcoinDF = pd.read_csv(bitcoinFile)
dashDF = pd.read_csv(dashFile)


# %%
bitcoinDF["Market Cap"].apply(type)

# %%
pd.to_numeric(bitcoinDF["Market Cap"][0])

# %%
onlyNumbers = re.findall("[0-9]+",bitcoinDF["Market Cap"][0])

# %%
tmp = ''
for number in onlyNumbers:
    tmp = tmp + number
print(tmp)
print(type(tmp))

# %%
int(tmp)

# %%
int("".join(onlyNumbers))

# %%
def stringToInt(someString: str) -> int:
    matchingCharacters = re.findall("[0-9]+",someString)
    out = None
    for character in matchingCharacters:
        out = out + character
    if len(out) < 1:
        return None
    else:
        return int(out)

# %%
type(stringToInt(''))

# %%
bitcoinDF["Market Cap"].apply(stringToInt)
marketCapS = bitcoinDF["Market Cap"].apply(stringToInt)

# %%
marketCapS =  marketCapS.dropna()
marketCapS.apply(int)

# %%
bitcoinDF = bitcoinDF.drop(columns=['Market Cap'])

# %%
dashDF = dashDF.drop(columns=['Market Cap'])

# %%
bitcoinDashDF = pd.merge(dashDF, bitcoinDF, how='inner', on='Date', suffixes=('_dash','_bitcoin'))

# %%
def percentChange(old: float , new: float) -> float:
    return ((new - old) / old) * 100

percentChange(3,4)

# %%
percentChange(2,4)

# %%
percentChange(5,10)

# %%
for i in range(0, len(bitcoinDashDF["Close_dash"]) - 1):
    previous = i - 1
    if previous == -1:
        previous = 0

    dashPercentChange =  percentChange(bitcoinDashDF["Close_dash"][previous], bitcoinDashDF["Close_dash"][previous])