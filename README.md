# Text-Encryption-Utility
Text Encryption Utility using Python and Fernet(AES)
🎯 Objective:
To build a secure Python-based utility that allows users to encrypt and decrypt messages using symmetric encryption, ensuring confidentiality of sensitive data during storage or transmission.

🔧 Tools & Technologies Used:
Python 3.13

cryptography library (Fernet)

Basic Python I/O and error handling

ast module for safe evaluation of encrypted strings

os module for key file management

🛠️ Key Features Implemented:
Feature	Description
🔐 Key Generation & Storage	Generates an AES-based Fernet key and saves it to key.key file to ensure consistent encryption/decryption across sessions.
📝 Encryption Option	Accepts plaintext input and returns encrypted ciphertext using the Fernet scheme.
🔓 Decryption Option	Accepts ciphertext input and returns the original message (plaintext).
🚫 Common Error Handling	Prevents app crash due to invalid menu input or empty strings.
🔁 Continuous Loop	The utility runs in a loop allowing multiple operations without restarting the script.

🧪 How It Works:
On first run, a key is generated and saved.

User is prompted to choose:

1 for encryption

2 for decryption

Message is entered, and either:

Encrypted and printed

Decrypted using the existing key and displayed

💡 Security Notes:
Fernet encryption is based on AES-128 in CBC mode + HMAC-SHA256

This ensures confidentiality and integrity

key.key must be stored securely — compromise of the key compromises all data
