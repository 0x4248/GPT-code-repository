# RSA Encryption - 1115

**Language**: `Cpp`

**Lines of code**: `94`

## Description

This program implements the RSA encryption algorithm to encrypt and decrypt messages. The program generates public and private keys, encrypts a message using the public key, and decrypts the message using the private key.

## Code

``` Cpp
#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef unsigned long long ull;

ull gcd(ull a, ull b) {
    if (b == 0) {
        return a;
    }
    else {
        return gcd(b, a % b);
    }
}

ull modPow(ull base, ull exp, ull mod) {
    ull result = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        exp = exp / 2;
        base = (base * base) % mod;
    }
    return result;
}

ull generatePrime(ull min, ull max) {
    ull p;
    do {
        p = rand() % (max - min + 1) + min;
    } while (p % 2 == 0 || p % 3 == 0 || p % 5 == 0 || p % 7 == 0);
    return p;
}

void generateKeys(ull& e, ull& d, ull& n) {
    ull p, q, phi;
    do {
        p = generatePrime(1000, 9999);
        q = generatePrime(1000, 9999);
        n = p * q;
        phi = (p - 1) * (q - 1);
    } while (gcd(phi, e) != 1);

    d = modPow(e, phi - 1, phi);
}

ull encrypt(ull m, ull e, ull n) {
    return modPow(m, e, n);
}

ull decrypt(ull c, ull d, ull n) {
    return modPow(c, d, n);
}

int main() {
    srand(time(NULL));
    ull e = 65537, d, n;
    generateKeys(e, d, n);

    string message;
    cout << "Enter a message to encrypt: ";
    getline(cin, message);

    cout << "Public key: (" << e << ", " << n << ")" << endl;
    cout << "Private key: (" << d << ", " << n << ")" << endl;

    cout << "Encrypting message..." << endl;
    for (int i = 0; i < message.length(); i++) {
        cout << encrypt((ull)message[i], e, n) << " ";
    }
    cout << endl;

    cout << "Decrypting message..." << endl;
    string decryptedMessage;
    string numberStr;
    for (int i = 0; i < message.length(); i++) {
        if (message[i] == ' ') {
            ull number = stoull(numberStr);
            decryptedMessage += (char)decrypt(number, d, n);
            numberStr = "";
        }
        else {
            numberStr += message[i];
        }
    }
    ull number = stoull(numberStr);
    decryptedMessage += (char)decrypt(number, d, n);
    cout << decryptedMessage << endl;

    return 0;
}

```

## Prompt

```
Make me a program in any language but python that is more than 20 lines of code long and includes complex math.
```