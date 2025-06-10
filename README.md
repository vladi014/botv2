# Solana Meme Coin Bot

## Description
This repository contains an asynchronous bot that scans for newly created pools on Solana and evaluates each token for potential rug pull risks and growth potential. It is a minimal demo that relies on mocked data but illustrates how a real implementation could monitor the network in real time.

## Project Structure
```
solana_bot/      # Package with bot modules
├── onchain.py   # Helpers for fetching on-chain data
├── offchain.py  # Functions for sentiment and listings
├── scoring.py   # Risk and potential scoring logic
├── main.py      # Entrypoint that coordinates the analysis

 tests/          # Unit tests for scoring utilities
 README.md       # Project information
 requirements.txt
```

## Requirements
- Python 3.8+
- aiohttp

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
Run the bot demo:
```bash
python -m solana_bot.main
```

Execute the tests:
```bash
python -m unittest discover -s tests
```

## License
MIT
