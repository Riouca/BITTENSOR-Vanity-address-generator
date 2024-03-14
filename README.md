
# Bittensor Vanity Address Generator

First off install the dependencies
```
sudo apt update
sudo apt install python3
pip install substrate-interface==1.7.5
sudo apt update nano
```

Then let's get into the project and open generator.py

```
git clone https://github.com/Riouca/BITTENSOR-Vanity-address-generator
cd BITTENSOR-Vanity-address-generator
nano generator.py
```

Now modify this line in generator.py and add your own desired prefixes in lowercase (add as many as you wish)

```python
def is_valid_address(address):
    valid_prefixes = ["5coffee","5dude","5etc"]
```
_Note : keep in mind that bittensor addresses __always__ start with 5C/5D/5E/5F/5G/5H_  

_Note 2 : difficulty increases exponentially for each character added (we suggest no more than 7 char prefixes)_

_Note 3 : if you want a case sensitive search, remove ```lower()``` in `if address.lower().startswith(prefix):`_

Let this bad boy run for a while and you'll see the results (address + mnemonic) in 
result.txt, remember that the time taken will depend on your CPU specs
```
cat result.txt
```

Optional : if you're willing to find a really difficult one (7+ char prefixes), you can use pm2 to let it run a longer period of time
```
apt install npm
npm install pm2 -g
pm2 start generator.py --interpreter python3 --name generator
pm2 logs generator
```
