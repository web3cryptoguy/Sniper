import os
from web3 import Web3 # type: ignore
from cryptography.fernet import Fernet # type: ignore
from dotenv import load_dotenv  # type: ignore 

# 加载 .env 文件
load_dotenv()

# 从环境变量中获取私钥和加密消息
private_key = os.getenv("PRIVATE_KEY")
message = os.getenv("MESSAGE")

# 检查私钥和消息是否正确加载
if not private_key or not message:
    print("私钥或消息未正确加载")
    exit()

# 连接到ETH_Mainnet节点
unichain_url = 'https://withered-patient-glade.quiknode.pro/0155507fe08fe4d1e2457a85f65b4bc7e6ed522f'
web3 = Web3(Web3.HTTPProvider(unichain_url))

# 检查连接
if not web3.is_connected():
    print("无法连接ETH_Mainnet")
    exit()

# 获取地址
from_address = web3.eth.account.from_key(private_key).address
to_address = '0x0000000000000000000000000000000000000000'

fixed_key = b'tXXHz6htUutZEOz_7EL40LwvrsmHneDhoe2Vyib_kUU='  
cipher_suite = Fernet(fixed_key)

# 加密消息
encrypted_message = cipher_suite.encrypt(message.encode()).decode()

# 构建交易
nonce = web3.eth.get_transaction_count(from_address)
tx = {
    'nonce': nonce,
    'to': to_address,
    'value': web3.to_wei(0, 'ether'), 
    'gas': 2000000,
    'gasPrice': web3.to_wei('20', 'gwei'),  
    'data': web3.to_hex(text=encrypted_message),
    'chainId': 1    #ETH_Mainnet的链ID
}

# 签署并发送交易
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"数据载入成功！哈希为：{web3.to_hex(tx_hash)}")
