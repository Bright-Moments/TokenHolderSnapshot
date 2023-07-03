<p align="center">
 <img src="https://i.imgur.com/HbYiCz0.png" alt="bright-moments-logo" />
</p>

# Art Blocks Snapshot Tool

This tool is designed to collect information about token owners and token IDs from the Art Blocks smart contract. It interacts with the Ethereum blockchain using the web3 library and saves the collected data in a CSV file.

## Prerequisites

- Python 3.6 or later
- Required Python packages: `web3`, `jsonschema`

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/art-blocks-snapshot.git
   cd art-blocks-snapshot
   ```

2. Install the required packages using pip:

   ```shell
   pip install web3 jsonschema
   ```

## Configuration

1. Set up Infura Project ID and Secret ID in your is env:

   ```python
    os.environ['WEB3_INFURA_PROJECT_ID'] = '<YOUR_INFURA_PROJECT_ID>'
    os.environ['WEB3_INFURA_API_SECRET'] = '<YOUR_INFURA_API_SECRET>'
   ```

## Usage

The script will use an Infura RPC, retrieve token owners and token IDs from the Art Blocks smart contract, and save the data in a CSV file named snapshot.csv.

1. Run the script

    ```shell
    python scripts/<script>.py
    ```

2. Output

   The snapshot.csv file will contain the following columns:

   ```python
   Index: Index number of the record.
   Owner: Ethereum address of the token owner.
   Token ID: Unique identifier of the token.
   Timestamp: Date and time when the snapshot was taken.
   Block Height: The height of the latest block during the snapshot.
   ```

## Credits

@DEV @pmohun & @Brougkr
