# AES-RSA-Encrypted-Hybrid-Steganography
The objective of this project is to overcome the limitations of traditional steganography software by developing an advanced and efficient steganography system. This system aims to address the vulnerabilities and weaknesses of traditional steganography software and provide improved security for data communication. The proposed two-layered approach combines the Least Significant Bit algorithm and Hybrid AES-RSA encryption techniques. The secret message is first encrypted using an AES symmetric key and then embedded in the LSB of cover media. This approach ensures that the information is well-hidden within digital content, while encryption provides an additional layer of protection to prevent unauthorized access.

**Algorithm for Hybrid AES-RSA Encryption:**

Input: Plain text, AES Symmetric key, RSA Public key

Output: Encrypted symmetric key, Cipher text

Begin Function hybridEncrypt(data, symmetricKey, rsaPublicKey):

encryptedData = aesEncrypt(data, symmetricKey)

//Encrypt the original data using AES encryption encryptedSymmetricKey = rsaEncrypt(symmetricKey, rsaPublicKey)

//Encrypt the symmetric key using RSA public key 

Return (encryptedSymmetricKey, encryptedData)

// Return the encrypted symmetric key and the encrypted data

End Function

**Algorithm for Hybrid AES-RSA Decryption**

Input: Encrypted AES Symmetric Key, RSA Private Key, Cipher text

Output: Plain text

Begin Function hybridDecrypt(encryptedSymmetricKey, rsaPrivateKey, encryptedData):

decryptedSymmetricKey = rsaDecrypt(encryptedSymmetricKey, rsaPrivateKey) 

// Decrypt the encrypted symmetric key using RSA private key

decryptedData = aesDecrypt(encryptedData, decryptedSymmetricKey) 

//Decrypt the cipher text using decrypted symmetric key

Return decryptedData

// Return the decrypted data as the final result.

End Function 
