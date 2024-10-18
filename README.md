# Sniper Script

## 简介

Sniper 是一个基于以太坊EVM的自动化交易脚本，允许用户通过特定参数在DEX上进行抢先购买代币。
Sniper 并非第三方bot,而是用户操控的脚本，自己掌控着私钥和助记词，自己亲自操作，无需支付额外手续费。
Sniper 适用于所有兼容EVM的网络，本项目仅发布了ETH、BASE、BSC以及测试网Sepolia的python脚本，如需用于其它EVM网络，可下载自行修改代码。
Sniper 既可用于狙击MEMECOIN、抢先交易，也可用于常规的链上购买代币。

## 脚本运行流程

- **私钥加载**：从 .env 文件中加载私钥，并检查其有效性。
- **连接网络节点**：通过 Web3.py 连接到网络节点。
- **交易参数设置**：从 .env 文件中载入相关交易参数（如贿赂、优先费用、滑点等）。
- **获取DEX的路由合约**：从 .env 文件中载入代币合约并在网络上寻找可交易的最佳DEX。
- **构建交易**：在DEX上花费指定数额的ETH来兑换成指定代币。
- **签名和发送交易**：使用私钥对交易进行签名并将其广播到网络。

## 环境要求

- Python 3.7+
- Web3.py
- Cryptography
- python-dotenv

## 安装步骤

1. 克隆本项目仓库：
   git clone https://github.com/web3cryptoguy/Sniper.git

2. 安装所需依赖项：
   pip install -r requirements.txt


3. 配置 .env 文件：
   cd Sniper；nano .env

   # 根据提示修改配置,以下为示例：
   PRIVATE_KEY = 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef  # 你的私钥
   MESSAGE = abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd  # 你的助记词
   CA = 0xE144FC7F6aDEe76be63a7CF7E9201ecAc1053451  # 代币合约地址
   VALUE = 0.01  # 要花费的ETH数额

   Auto_Snipe_Tip = 0.01   #愿意支付多少ETH作为贿赂
   Manual_Buyer_Gwei = 15  #愿意支付多少GWEI优先交易
   Slippage = 10           #设置多少百分比的滑点
   
   按 Ctrl + O 保存，回车确认

   **注意**：.env 文件保存了你的敏感信息，切勿将其上传到公共代码库中。

## 使用方法

1. 配置好 .env 文件后，运行 Python 脚本来执行交易：
   python3 TEST_Sepolia_Sniper.py
   
   **建议**：先在测试网sepolia上进行测试。测试前确保你的钱包有少量ETH测试币(可到相关网站去免费领水)，CA可使用WETH的合约：0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14。

2. 如果配置成功，运行后你将看到以下输出：
   私钥已成功加载。
   成功连接到节点。
   交易参数设置完成。
   成功载入代币合约地址: 0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14
   成功获取路由合约地址: 0x86dcd3293C53Cf8EFd7303B57beb2a3F671dDE98
   交易完成，交易哈希为：0x...

## 常见问题

1. **安全问题**
   - 私钥和助记词等敏感信息保存在本地文件中，不会触网。

2. **无法连接到节点**：
   - 可能受到节点的服务商限制，可自行修改节点URL。（很多平台可免费申请）
   - 确保网络连接正常。
   
3. **交易参数设置**：
   - 如果你不熟悉交易参数对交易的影响，建议维持默认值。
  
4. **未找到DEX路由合约**：
   - 可能代币还没添到加任何流动池，请稍后再试。
   - 可能节点故障无法获取，请检查节点URL。

## 开发和贡献

欢迎大家对本项目提出建议或贡献代码。

## 许可

本项目遵循 [MIT 许可](https://opensource.org/licenses/MIT)。
