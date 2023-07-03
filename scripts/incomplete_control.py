# -*- coding: utf-8 -*-
#@DEV @pmohun & @Brougkr
## Run on first setup only
# !pip install web3
# !pip install --force-reinstall jsonschema==3.2.0

import os
import json
import csv
import time

current_time = time.time()
current_time_formatted = time.ctime(current_time)
os.environ['WEB3_INFURA_PROJECT_ID'] = '' #infura project id
os.environ['WEB3_INFURA_API_SECRET']= '' #infura secret id

from web3.auto.infura import w3 # Use Infura as our mainnet data provider
from ens import ENS

print(w3.isConnected()) # check connection
ns = ENS.fromWeb3(w3) # set provider as Infura
blockheight = w3.eth.get_block('latest')

"""Art Blocks"""
# ENS Registry smart contract application binary interface (ABI) 
# https://etherscan.io/address/0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e#code

# Open the JSON ABI
with open('abi.json', 'r') as file:
    # Load the JSON data
    abi = json.load(file)

address = '0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270' # ArtBlocks smart contract address
address_checksum = w3.toChecksumAddress(address)
ab_contract = w3.eth.contract(address=address_checksum, abi=abi)

"""CryptoCitizens & Fidenzas"""
## CryptoCitizen Token IDs

tokenids = []
# Only include eligible CryptoVenetian token IDs
for i in range(95000000,95000691, 1):
  tokenids.append(i)

# Only include minted CryptoNewYorkers
for i in range(189000000, 189000436, 1):
  tokenids.append(i)

# Minted Fidenzas
tokenids = []
for i in range(78000000,78000999,1):
  tokenids.append(i)

print(tokenids)

owners = []
tokenIDs = []

for id in tokenids:
  owner = ab_contract.functions.ownerOf(id).call()
  tokenid = id
  owners.append(owner)
  tokenIDs.append(tokenid)

print(owners)
print(tokenIDs)

owners_output = []
i = 0
for owner in owners:
  array = []
  array.append(i+1)
  array.append(owner)
  array.append(tokenIDs[i])
  owners_output.append(array)
  i += 1

blockheightAndTimeRow = []
blockheightAndTimeRow.append(current_time_formatted)
blockheightAndTimeRow.append(blockheight)


with open('snapshot.csv', 'wt') as f:
  writer = csv.writer(f)
  writer.writerows(owners_output)
  writer.writerow(blockheightAndTimeRow)
