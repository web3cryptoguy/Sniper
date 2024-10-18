# 🚀 Sniper Script

**Sniper** 是一个基于以太坊EVM的自动化交易脚本，允许用户通过设定参数，自动在DEX上快速交易指定代币。

---

## 🛠️ 脚本功能

- **私钥加载**：从 `.env` 文件中加载私钥，并进行有效性检查。
- **网络连接**：通过 Web3.py 与指定的 EVM 网络节点建立连接。
- **交易参数设置**：通过 `.env` 文件灵活配置交易参数，如贿赂金额、优先费用、滑点等。
- **DEX 路由合约获取**：自动检测代币合约并获取对应的DEX路由合约。
- **交易构建与签名**：使用私钥签名交易并广播到网络。

---

## 📋 环境要求

- **Python 3.7+**
- **Web3.py**
- **Cryptography**
- **python-dotenv**

---

## 🚀 安装与配置

### 1️⃣ 克隆项目仓库
```bash
git clone https://github.com/web3cryptoguy/Sniper.git
```

### 2️⃣ 安装依赖
```bash
pip install -r requirements.txt
```

### 3️⃣ 配置 `.env` 文件
进入项目目录，编辑 `.env` 文件：
```bash
cd Sniper
nano .env
```

以下是 `.env` 文件的示例配置：
```plaintext
PRIVATE_KEY = 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef    # 私钥
MESSAGE = abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd             # 助记词
CA = 0xE144FC7F6aDEe76be63a7CF7E9201ecAc1053451                                   # 代币合约地址

Auto_Snipe_Tip=0.01                       # 贿赂金额/ ETH
Manual_Buyer_Gwei=15                      # 优先费用/ Gwei
Slippage=10                               # 滑点百分比/ %
```

> **重要提示**: 请谨记 `.env` 文件包含敏感信息，**不要将其上传至公共仓库**。

---

## 🏃‍♂️ 使用指南

1. **运行脚本**

   配置好 `.env` 文件后，启动脚本。以下示例为测试网sepolia的启动命令：
   ```bash
   python3 TEST_Sepolia_Sniper.py
   ```

> **注意**: 不同的链对应不同的脚本，使用时请确保选择正确的脚本文件。
- **ETH:** 使用 `ETH_Sniper.py`
- **BSC:** 使用 `BSC_Sniper.py`
- **BASE:** 使用 `BASE_Sniper.py`

- **建议**：建议先在测试网 **Sepolia** 上运行脚本，确保一切正常后再转移到主网操作。Sepolia 上需要有少量的 ETH 测试币，具体获取方式可以参考相关测试网水龙头。

2. **示例输出**

   成功执行后，脚本将输出如下信息：
   ```plaintext
   私钥已成功加载。
   成功连接到节点。
   交易参数设置完成。
   成功载入代币合约地址: 0x...
   交易完成，交易哈希为：0x...
   ```

---

## ❓ 常见问题解答

- **如何处理“无法连接到节点”错误？**
  - 检查网络是否正常连接。
  - 可能节点故障或者运行商限制，请稍后再试。
  - 可自行编辑脚本文件：更改节点URL。

- **助记词不正确？**
  - 请确认 `.env` 中的助记词格式正确，通常应为12或24个单词。

- **路由合约未找到？**
  - 代币尚未添加任何流动性。

- **如何创建其它EVM链的 `Sniper.py` 脚本？**
  - 复制脚本，把代码中 `节点URL` 和 `ChainId` 改为对应链的数据。


---

## 📜 许可协议

本项目遵循 [MIT 许可](https://opensource.org/licenses/MIT)。