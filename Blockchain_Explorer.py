import streamlit as st # type: ignore
import pandas as pd
import requests as rq
import random
from datetime import datetime as dt,timedelta
import streamlit.components.v1 as components

# Sidebar setup
sidebar = st.sidebar

# title = sidebar.radio(label="Latest Blocks from:", options=["Bitcoin: BTC", "Ethereum: ETH", "Binance Smart Chain: BNB", "Cardano: ADA", "Ripple: XRP"])
title = sidebar.radio(label="Latest Blocks from:", options=["Bitcoin: BTC", "Ethereum: ETH", "Binance Smart Chain: BNB", "Ripple: XRP"])

if title == "Bitcoin: BTC":

    st.image("images/bitcoin-btc-logo-full.svg", width=250)
    st.subheader("Bitcoin RPC API")
    st.write("""Using Getblock's Blockchain Node Provider for access to BTC network and data.""")
    st.write("""**Note:** Data returned from API calls are chain-specific.""")

    X_API_TOKEN = st.secrets["GETBLOCK_BTC_TOKEN"]
    headers = {
        "X-API-TOKEN": X_API_TOKEN,
    }
    
    btc_status_endpoint = "https://go.getblock.io/"+X_API_TOKEN

    def get_latest_block():

        btc_status_params = {
            
            "jsonrpc": "2.0",
            "id": "bitcoin",
            "method": "getblockchaininfo",
            "id": "getblock.io"
        }

        btc_chaindata = rq.post(url=btc_status_endpoint, json=btc_status_params, headers=headers).json()
        blockhash = btc_chaindata['result']['bestblockhash']

        return blockhash


    latest_blockhash = get_latest_block()

    btc_hash = latest_blockhash
    lastn = []

    index = []
    time = []
    blockhash = []
    blocksize = []
    nTx = []
    btc_txs = []

    for i in range(0, 10):
        last_block_params = {
            "jsonrpc": "2.0",
            "id": "bitcoin",
            "method": "getblock",
            "params": [btc_hash]
        }
        new_block = {}
        btc_blockdata = rq.post(url=btc_status_endpoint, json=last_block_params, headers=headers).json()
        new_block['index'] = btc_blockdata['result']['height']
        new_block['timestamp'] = btc_blockdata['result']['time']
        new_block['blockhash'] = btc_blockdata['result']['hash']
        new_block['blocksize'] = btc_blockdata['result']['size']
        new_block['nTx'] = btc_blockdata['result']['nTx']
        index.append(new_block['index'])
        time.append(dt.fromtimestamp(new_block['timestamp']).strftime('%Y.%m.%d %H:%M:%S'))
        blockhash.append(new_block['blockhash'])
        blocksize.append(new_block['blocksize'])
        nTx.append(new_block['nTx'])
        btc_txs.append(btc_blockdata['result']['tx'][:20])

        lastn.append(new_block)
        btc_hash = btc_blockdata['result']['previousblockhash']

    st.write("\nLatest Blocks\n")
    df = pd.DataFrame(columns=['index', 'timestamp (utc)', 'blockhash', 'blocksize', 'no.transactions'])

    df['index'] = index
    df['timestamp (utc)'] = time
    df['blockhash'] = blockhash
    df['blocksize'] = blocksize
    df['no.transactions'] = nTx

    # df = df.style.hide_index()
    st.dataframe(df)

    blocktime = []
    confirmations = []
    size = []
    txid = []
    value = []
    hash = []

    for i in range(0, 20):
        btc_txs_params = {
            "jsonrpc": "2.0",
            "method": "getrawtransaction",
            "params": {
                "txid": btc_txs[0][i],
                "verbose": True
            },
            "id": "getblock.io"
        }

        btc_txs_data = rq.post(url=btc_status_endpoint, json=btc_txs_params, headers=headers).json()
        # btc_txs_summary.append(btc_txs_data['result'])
        blocktime.append(dt.fromtimestamp(btc_txs_data['result']['blocktime']).strftime('%Y.%m.%d %H:%M:%S'))
        confirmations.append(btc_txs_data['result']['confirmations'])
        size.append(btc_txs_data['result']['size'])
        txid.append(btc_txs_data['result']['txid'])
        value.append(btc_txs_data['result']['vout'][0]['value'])
        hash.append(btc_txs_data['result']['hash'])

    st.write("\nLatest Transactions\n")
    dftx = pd.DataFrame(columns=['blocktime', 'confirmations', 'size', 'txid', 'value (BTC)', 'hash'])

    dftx['blocktime'] = blocktime
    dftx['confirmations'] = confirmations
    dftx['size'] = size
    dftx['txid'] = txid
    dftx['value (BTC)'] = value
    dftx['hash'] = hash

    # dftx = dftx.style.hide_index()

    st.dataframe(dftx)

if title == "Ethereum: ETH":

    st.image("images/ethereum-eth-logo-full-horizontal.svg", width=250)
    st.subheader("Ethereum RPC API")
    st.write("""Using Getblock's Blockchain Node Provider for access to Ethereum network and data.""")
    st.write("""**Note:** Data returned from API calls are chain-specific.""")

    GETBLOCK_ETH_TOKEN = st.secrets["GETBLOCK_ETH_TOKEN"]
    GETBLOCK_ETH_URL = "https://go.getblock.io/"+GETBLOCK_ETH_TOKEN
    

    eth_headers = {
        "X-API-KEY": GETBLOCK_ETH_TOKEN
    }

    blocknumber = []
    timestamp = []
    blockhash = []
    gasLimit = []
    gasUsed = []

    latest_blocks = []
    block_num = "latest"
    eth_params = {
        "id": "blockNumber",
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [block_num, False]
    }
    eth_blockdata = rq.post(url=GETBLOCK_ETH_URL, json=eth_params, headers=eth_headers).json()
    curr_block_hash = eth_blockdata['result']['hash']
    curr_block_number = eth_blockdata['result']['number']
    curr_txs_hash = []

    for i in range(0, 10):
        hash_eth_params = {
            "id": "blockHash",
            "jsonrpc": "2.0",
            "method": "eth_getBlockByHash",
            "params": [curr_block_hash, False]
        }
        hash_eth_blockdata = rq.post(url=GETBLOCK_ETH_URL, json=hash_eth_params, headers=eth_headers).json()
        new_block = {'blocknumber': hash_eth_blockdata['result']['number'],
                        'timestamp': hash_eth_blockdata['result']['timestamp'],
                        'blockhash': hash_eth_blockdata['result']['hash'],
                        'gasLimit': hash_eth_blockdata['result']['gasLimit'],
                        'gasUsed': hash_eth_blockdata['result']['gasUsed']}

        latest_blocks.append(new_block)
        if i == 0:
            curr_txs_hash.append(hash_eth_blockdata['result']['transactions'][:20])
        curr_block_hash = hash_eth_blockdata['result']['parentHash']

    dec_blocks = []
    for dc in latest_blocks:
        dc['blocknumber'] = int(dc['blocknumber'], 16)
        dc['timestamp'] = int(dc['timestamp'], 16)
        dc['gasLimit'] = int(dc['gasLimit'], 16)
        dc['gasUsed'] = int(dc['gasUsed'], 16)
        blocknumber.append(dc['blocknumber'])
        timestamp.append(dt.fromtimestamp(dc['timestamp']).strftime('%Y.%m.%d %H:%M:%S'))
        blockhash.append(dc['blockhash'])
        gasLimit.append(dc['gasLimit'])
        gasUsed.append(dc['gasUsed'])

        dec_blocks.append(dc)

    df = pd.DataFrame(columns=['blocknumber', 'timestamp (utc)', 'blockhash', 'gasLimit', 'gasUsed'])
    df['blocknumber'] = blocknumber
    df['timestamp (utc)'] = timestamp
    df['blockhash'] = blockhash
    df['gasLimit'] = gasLimit
    df['gasUsed'] = gasUsed

    st.write("\nLatest Blocks\n")
    st.dataframe(df)

    transx_blockid = []
    trans_idx = []
    gas = []
    gas_price = []
    from_acct = []
    to_acct = []
    value = []
    type = []

    for i in range(0, 20):
        hash_eth_params = {
            "id": "txsHash",
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByHash",
            "params": [curr_txs_hash[0][i]]
        }
        hash_eth_txdata = rq.post(url=GETBLOCK_ETH_URL, json=hash_eth_params, headers=eth_headers).json()
        transx_blockid.append(int(hash_eth_txdata['result']['blockNumber'], 16))
        trans_idx.append(int(hash_eth_txdata['result']['transactionIndex'], 16))
        gas.append(int(hash_eth_txdata['result']['gas'], 16))
        gas_price.append(int(hash_eth_txdata['result']['gasPrice'], 16))
        from_acct.append(hash_eth_txdata['result']['from'])
        to_acct.append(hash_eth_txdata['result']['to'])
        value.append(int(hash_eth_txdata['result']['value'], 16))
        type.append(int(hash_eth_txdata['result']['type'], 16))

    txdf = pd.DataFrame(
        columns=['transx_blockid', 'trans_idx', 'gas', 'gas_price', 'from_acct', 'to_acct', 'value (WEI)', 'type'])
    txdf['transx_blockid'] = transx_blockid
    txdf['trans_idx'] = trans_idx
    txdf['gas'] = gas
    txdf['gas_price'] = gas_price
    txdf['from_acct'] = from_acct
    txdf['to_acct'] = to_acct
    txdf['value'] = value
    txdf['type'] = type

    st.write("\nLatest Transactions\n")
    st.dataframe(txdf)

# if title == "Cardano: ADA":

#     st.image("images/cardanosizedlogo.svg", width=250)
#     st.subheader("Cardano Rosetta API.")
#     st.write("""Using Getblock's Blockchain Node Provider for access to the Cardano network and data.""")
#     st.write("""**Note:** Data returned from API calls are chain-specific.""")

#     GETBLOCK_ADA_TOKEN = st.secrets["GETBLOCK_CRD_TOKEN"]
#     ada_status_endpoint = "https://go.getblock.io/"+GETBLOCK_ADA_TOKEN
    
#     headers = {
#         "X-API-KEY": GETBLOCK_ADA_TOKEN,
#         "Content-Type": "application/json"
#     }

#     status_params = {
#         "network_identifier": {
#             "blockchain": "cardano",
#             "network": "mainnet"},
#         "metadata": {}
#     }

#     ada_status = rq.post(url=ada_status_endpoint, json=status_params, headers=headers).json()
#     st.write(ada_status)
#     curr_block_idx = ada_status['current_block_identifier']['index']
#     curr_block_hash = ada_status['current_block_identifier']['hash']
#     latest_blocks = []

#     epoch = []
#     index = []
#     timestamp = []
#     blockhash = []
#     blocksize = []

#     for i in range(0, 20):
#         ada_block_endpoint = "https://go.getblock.io/"+GETBLOCK_ADA_TOKEN
#         block_params = {
#             "network_identifier": {
#                 "blockchain": "cardano",
#                 "network": "mainnet"},
#             "metadata": {},
#             "block_identifier": {
#                 "index": curr_block_idx,
#                 "hash": curr_block_hash}
#         }

#         block_data = rq.post(url=ada_block_endpoint, json=block_params, headers=headers).json()
#         new_block = {'epoch': block_data['block']['metadata']['epochNo'],
#                         'index': block_data['block']['block_identifier']['index'],
#                         'timestamp': block_data['block']['timestamp'],
#                         'blockhash': block_data['block']['block_identifier']['hash'],
#                         'blocksize': block_data['block']['metadata']['size']}
#         epoch.append(new_block['epoch'])
#         index.append(new_block['index'])
#         timestamp.append(dt.fromtimestamp((new_block['timestamp'])/1000).strftime('%Y.%m.%d %H:%M:%S'))
#         blockhash.append(new_block['blockhash'])
#         blocksize.append(new_block['blocksize'])

#         latest_blocks.append(new_block)

#         curr_block_idx = block_data['block']['parent_block_identifier']['index']
#         curr_block_hash = block_data['block']['parent_block_identifier']['hash']

#     df = pd.DataFrame(columns=['epoch', 'index', 'timestamp (utc)', 'blockhash', 'blocksize'])
#     df['epoch'] = epoch
#     df['index'] = index
#     df['timestamp (utc)'] = timestamp
#     df['blockhash'] = blockhash
#     df['blocksize'] = blocksize

#     st.dataframe(df)
#     #st.json(latest_blocks)

if title == "Binance Smart Chain: BNB":

    st.image("images/330px-Binance_logo.svg.png", width=250)
    st.subheader(f"Binance Smart Chain (BNB): Ethereum RPC API")
    st.write("""Using Getblock's Blockchain Node Provider for access to Binance Smart Chain network and data.""")
    st.write("""**Note:** Data returned from API calls are chain-specific.""")

    GETBLOCK_BSC_TOKEN = st.secrets["GETBLOCK_BSC_TOKEN"]
    GETBLOCK_BSC_URL = "https://go.getblock.io/"+GETBLOCK_BSC_TOKEN

    bsc_headers = {
        "X-API-KEY": GETBLOCK_BSC_TOKEN,
        "Content-Type": "application/json"
    }

    blocknumber = []
    timestamp = []
    size = []
    blockhash = []
    gasLimit = []
    gasUsed = []
    miner = []

    latest_blocks = []
    curr_block_num = "latest"

    num_bsc_params = {
        "id": "binance",
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [curr_block_num, True]
    }
    num_bsc_blockdata = rq.post(url=GETBLOCK_BSC_URL, json=num_bsc_params, headers=bsc_headers).json()

    curr_block_hash = num_bsc_blockdata['result']['hash']
    curr_txs_hash = []
    # print(curr_block_hash)

    for i in range(0, 10):
        hash_bsc_params = {
            "id": "binance",
            "jsonrpc": "2.0",
            "method": "eth_getBlockByHash",
            "params": [curr_block_hash, True]
        }

        hash_bsc_blockdata = rq.post(url=GETBLOCK_BSC_URL, json=hash_bsc_params, headers=bsc_headers).json()
        # print(hash_bsc_blockdata)
        new_block = {'blocknumber': hash_bsc_blockdata['result']['number'],
                        'timestamp': hash_bsc_blockdata['result']['timestamp'],
                        'size': hash_bsc_blockdata['result']['size'],
                        'blockhash': hash_bsc_blockdata['result']['hash'],
                        'gasLimit': hash_bsc_blockdata['result']['gasLimit'],
                        'gasUsed': hash_bsc_blockdata['result']['gasUsed'],
                        'miner': hash_bsc_blockdata['result']['miner']}

        latest_blocks.append(new_block)
        if i == 0:
            curr_txs_hash.append(hash_bsc_blockdata['result']['transactions'][:20])
        curr_block_hash = hash_bsc_blockdata['result']['parentHash']

    dec_blocks = []
    for dc in latest_blocks:
        dc['blocknumber'] = int(dc['blocknumber'], 16)
        dc['timestamp'] = int(dc['timestamp'], 16)
        dc['size'] = int(dc['size'], 16)
        dc['gasLimit'] = int(dc['gasLimit'], 16)
        dc['gasUsed'] = int(dc['gasUsed'], 16)
        blocknumber.append(dc['blocknumber'])
        timestamp.append(dt.fromtimestamp(dc['timestamp']).strftime('%Y.%m.%d %H:%M:%S'))
        size.append(dc['size'])
        blockhash.append(dc['blockhash'])
        gasLimit.append(dc['gasLimit'])
        gasUsed.append(dc['gasUsed'])
        miner.append(dc['miner'])

        dec_blocks.append(dc)

    df = pd.DataFrame(columns=['blocknumber', 'timestamp', 'size', 'blockhash', 'gasLimit', 'gasUsed', 'miner'])
    df['blocknumber'] = blocknumber
    df['timestamp'] = timestamp
    df['size'] = size
    df['blockhash'] = blockhash
    df['gasLimit'] = gasLimit
    df['gasUsed'] = gasUsed
    df['miner'] = miner

    st.dataframe(df)
    # st.json(dec_blocks)

    transx_blockid = []
    trans_idx = []
    gas = []
    gas_price = []
    from_acct = []
    to_acct = []
    value = []
    type = []

    for i in curr_txs_hash[0]:
        transx_blockid.append(int(i['blockNumber'], 16))
        trans_idx.append(int(i['transactionIndex'], 16))
        gas.append(int(i['gas'], 16))
        gas_price.append(int(i['gasPrice'], 16))
        from_acct.append(i['from'])
        to_acct.append(i['to'])
        value.append(int(i['value'], 16))
        type.append(int(i['type'], 16))

    txdf = pd.DataFrame(
        columns=['transx_blockid', 'trans_idx', 'gas', 'gas_price', 'from_acct', 'to_acct', 'value (WEI)', 'type'])
    txdf['transx_blockid'] = transx_blockid
    txdf['trans_idx'] = trans_idx
    txdf['gas'] = gas
    txdf['gas_price'] = gas_price
    txdf['from_acct'] = from_acct
    txdf['to_acct'] = to_acct
    txdf['value (WEI)'] = value
    txdf['type'] = type

    st.dataframe(txdf)

if title == "Ripple: XRP":

    st.image("images/xrp-xrp-logo.png", width=70)
    st.subheader("XRP Ledger API")
    st.write("""Accessing XRP Ledger throuoh Ripple gateway nodes and APIs to the XRP chains, their proprietary network, protocols and each chain's data.""")
    st.write("""**Note:** Data returned from API calls are chain-specific.""")

    XRP_API_URL = "https://s1.ripple.com:51234/"
    xrp_headers = {
        "content-type": "application/json"
    }

    blocknumber = []
    timestamp = []
    block_hash = []
    total_coins = []
    transaction_hash = []

    latest_blocks = []
    latest_tx = []

    init_ledger_hash = "current"
    
    METHOD = "ledger_closed"

    for i in range(0, 1):
        xrp_params = {
            "method": METHOD,
            "params": [
                {
                    "ledger_index": init_ledger_hash
                }
            ]
        }
        xrp_data = rq.post(url=XRP_API_URL, json=xrp_params, headers=xrp_headers).json()
        curr_blockhash = xrp_data['result']['ledger_hash']
        curr_blockindex = xrp_data['result']['ledger_index']
        # st.write(xrp_data['result'])

    METHOD = "ledger_data"

    for i in range(0, 20):
        xrp_params = {
            "method": METHOD,
            "params": [
                {
                    "binary": False,
                    "ledger_hash": curr_blockhash,
                    "limit": 20
                }
            ]
        }
        xrp_data = rq.post(url=XRP_API_URL, json=xrp_params, headers=xrp_headers).json()
        # st.write(xrp_data['result'])

        blocknumber.append(xrp_data['result']['ledger']['ledger_index'])
        timestamp.append(xrp_data['result']['ledger']['close_time_human'])
        block_hash.append(xrp_data['result']['ledger']['ledger_hash'])
        total_coins.append(xrp_data['result']['ledger']['total_coins'])
        transaction_hash.append(xrp_data['result']['ledger']['transaction_hash'])

        curr_blockhash = xrp_data['result']['ledger']['parent_hash']


    st.write("Latest Ledgers (Blocks)")

    df = pd.DataFrame(columns=['blocknumber', 'timestamp', 'block_hash', 'total_coins', 'transaction_hash'])
    df['blocknumber'] = blocknumber
    df['timestamp'] = timestamp
    df['block_hash'] = block_hash
    df['total_coins'] = total_coins
    df['transaction_hash'] = transaction_hash

    st.dataframe(df)

    # st.write("Latest Transactions")
    
    # latest_tx = []
    # txledger_index = []
    # trans_type = []
    # account = []
    # fee = []
    # expiration = []
    # tx_hash = []

    # METHOD = "ledger_data"

    # xrp_tx_params = {
    #     "method": METHOD,
    #     "params": [
    #         {
    #             "start": 0,
    #             "binary": False,
    #             "limit": 1
    #         }
    #     ]
    # }
    # xrp_tx_data = rq.post(url=XRP_API_URL, json=xrp_tx_params, headers=xrp_headers).json()
    # st.write(xrp_tx_data['result'])

    # latest_tx.append(xrp_tx_data['result']['txs'])

    # for i in range(0, len(latest_tx[0])):
    #     txledger_index.append(latest_tx[0][i]['ledger_index'])
    #     trans_type.append(latest_tx[0][i]['TransactionType'])
    #     account.append(latest_tx[0][i]['Account'])
    #     fee.append(latest_tx[0][i]['Fee'])
    #     #     expiration.append(latest_tx[0][tx]['Expiration'])
    #     tx_hash.append(latest_tx[0][i]['hash'])

    # txdf = pd.DataFrame(columns=['txledger_index', 'trans_type', 'account', 'fee', 'tx_hash'])
    # txdf['txledger_index'] = txledger_index
    # txdf['trans_type'] = trans_type
    # txdf['account'] = account
    # txdf['fee'] = fee
    # # txdf['expiration'] = expiration
    # txdf['tx_hash'] = tx_hash

    # st.dataframe(txdf)