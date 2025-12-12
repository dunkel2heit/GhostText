
### \# GhostText 👻

> Encrypt and decrypt messages directly in your terminal using secure symmetric encryption (Fernet) derived from a custom password. GhostText ensures that your messages remain ephemeral, accessible only with the correct key/password.

### Table of Contents

  * [✨ Features](https://www.google.com/search?q=%23-features)
  * [🔑 Security and Concept](https://www.google.com/search?q=%23-security-and-concept)
  * [⚙️ Installation](https://www.google.com/search?q=%23%25EF%25B8%258F-installation)
  * [🚀 How to Use](https://www.google.com/search?q=%23-how-to-use)
  * [⚠️ Important Note](https://www.google.com/search?q=%23%25EF%25B8%258F-important-note)

-----

### ✨ Features

  * **Symmetric Encryption:** Uses the industry-standard Fernet (based on AES 128-bit) for robust encryption.
  * **Password Derivation:** Securely transforms a simple, custom password into a cryptographically strong 32-byte Fernet key using **PBKDF2HMAC** (Key Derivation Function).
  * **Key Options:** Choose between generating a new, fully random key or using a custom, memorable password.
  * **Simple Interface:** A clean, terminal-based interface for easy read and write operations.

### 🔑 Security and Concept

The core security of this project lies in the combination of Fernet and PBKDF2HMAC:

  * **Fernet:** Guarantees that the encrypted message cannot be read or tampered with without the correct key.
  * **PBKDF2HMAC:** Takes your human-readable password (e.g., "hello") and stretches it into the necessary 32-byte cryptographic key. This makes it much harder for attackers to crack the key, even if they guess your password.

-----

### ⚙️ Installation

To run GhostText, you only need Python and the `cryptography` library.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/dunkel2heit/GhostText
    cd GhostText
    ```

2.  **Install the required library:**

    ```bash
    pip install cryptography
    ```

3.  **Run the script:**

    ```bash
    python main.py
    ```

-----

### 🚀 How to Use

When you run `python main.py`, you will first be prompted to choose a key method.

#### 1\. First Run: Setting Up Your Key

You have two options for key setup:

| Option | Command | Description |
| :--- | :--- | :--- |
| **N** | **New random key** | Generates a 32-byte, highly secure, fully random key. You must save this key string manually to reuse it. |
| **C** | **Custom key** | Prompts you for a password (e.g., "mysecret"). This password is used to **derive** the secure 32-byte Fernet key. |

#### 2\. Encrypting a Message (Write)

1.  Select **`W`** when prompted for an action.
2.  Enter your message.
3.  The script will output the ciphertext (a long Base64 string). **Copy and save this string.**

#### 3\. Decrypting a Message (Read)

1.  Select **`R`** when prompted for an action.
2.  Paste the **full ciphertext string** (the output from the 'W' operation) when prompted.
3.  The script will use the currently loaded key (random key or password-derived key) to reveal the original message.

-----

### ⚠️ Important Note

  * **Key/Password is EVERYTHING:** If you choose the 'C' (Custom Key) method, you **MUST** use the exact same password and the exact same `SALT` value (currently hardcoded in the script) every time you run the script to decrypt a message.
  * **Security:** This script is for educational and simple personal use. For large-scale or mission-critical applications, always consult professional cryptographic guidelines.
  * **Salt:** The hardcoded `SALT` is essential for key derivation. If you modify the script, do not change the `SALT` value unless you intend to break compatibility with all previously encrypted messages.

-----

### Contributing

Feel free to open issues or submit pull requests to improve the script, add features, or enhance security best practices\!
