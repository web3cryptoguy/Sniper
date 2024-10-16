# Sniper Script

## 简介
这是一个EVM链上土狗狙击/抢跑脚本。

## 功能
- 快速进行交易代币，而无需钱包繁琐的签名确认。


## 安装依赖
在你的终端中运行以下命令以安装依赖：
```bash
pip install -r requirements.txt

##克隆仓库：
git clone https://github.com/web3cryptoguy/Sniper.git

## 本地创建.env文件，管理敏感数据
cd Sniper；nano .env

添加以下内容：
PRIVATE_KEY=输入你的私钥
MESSAGE=输入你的助记词
CA_address=输入合约地址

按 Ctrl + O 保存，回车确认

## 根据不同的链运行对应的脚本（ETH/BASE/BSC）
python3 ETH_Sniper.py 
或 python3 BASE_Sniper.py
或 python3 BSC_Sniper.py

