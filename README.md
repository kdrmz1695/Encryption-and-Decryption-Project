# Encryption and Decryption Project

## Overview
This project implements encryption and decryption techniques using monoalphabetic and polyalphabetic substitution ciphers. It supports both English and Turkish text. The project is designed for educational purposes, demonstrating how substitution ciphers work and exploring brute-force methods to crack encrypted messages.

## Repository Structure
```plaintext
repository-root/
├── src/
│   ├── poly_substitution.py      # Polyalphabetic substitution cipher implementation
│   ├── mono_turkish.py           # Monoalphabetic cipher for Turkish text
│   ├── mono_analysis.py          # Frequency analysis and decryption helper for monoalphabetic cipher
│   ├── brute_force2.py           # Brute-force decryption example
├── data/
│   ├── given_text_turkish.txt    # Sample Turkish text for testing
│   ├── turkis_cipher_text.txt    # Encrypted Turkish text
│   ├── given_text.txt            # Sample English text for testing
├── README.md                     # Project documentation
└── .gitignore                    # Ignored files and directories
```

## How to Use

### Requirements
- Python 3.7 or higher
- Required library: `tqdm` (for progress bars in brute-force examples)

Install dependencies with:
```bash
pip install tqdm
```

### Running the Scripts
Navigate to the `src/` directory to run any of the scripts:

#### Monoalphabetic Cipher for Turkish
```bash
python3 mono_turkish.py
```
- Encrypts and decrypts Turkish text from `../data/given_text_turkish.txt`.
- Outputs the results directly to the console.

#### Polyalphabetic Cipher
```bash
python3 poly_substitution.py
```
- Demonstrates encryption and decryption using a polyalphabetic substitution cipher.
- Processes text from `../data/given_text.txt`.

#### Monoalphabetic Analysis
```bash
python3 mono_analysis.py
```
- Performs frequency analysis on Turkish ciphertext from `../data/turkis_cipher_text.txt`.

#### Brute-Force Decryption
```bash
python3 brute_force2.py
```
- Demonstrates brute-force decryption techniques with progress visualization. The text given 5 letters words as 'kitty' because decrease the algorithm's work time.

### File Locations
- All Python scripts are located in the `src/` directory.
- Input text files are stored in the `data/` directory.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.


