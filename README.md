# HandshakeSignedMessages

## Explanation

    Key Generation:
        The generate_keys function generates a pair of RSA keys (public and private).

    Message Signing:
        The sign_message function uses the sender's private key to sign the message. It uses PSS padding and SHA-256 hashing for the digital signature.

    Message Verification:
        The verify_message function uses the sender's public key to verify the signature against the message. It also uses PSS padding and SHA-256 hashing.

    Message Exchange:
        Alice signs a message and Bob verifies it.
        Bob signs a message and Alice verifies it.

This code ensures secure, authenticated, and untampered message exchange using RSA with the cryptography library.

## Theory

A secure and simple algorithm to exchange signed messages in a "handshake" challenge can be implemented using public-key cryptography. Here’s a basic outline of how this can be done using RSA (Rivest-Shamir-Adleman) as the cryptographic algorithm:
Steps for a Secure Handshake Using RSA

    Key Generation:
        Both parties (Alice and Bob) generate their own RSA key pairs (public and private keys).
        Each party securely shares their public key with the other.

    Message Signing and Exchange:

        Alice wants to send a message MM to Bob:
            Alice creates a hash of the message MM. The hash function should be a secure one, like SHA-256.
            Alice encrypts the hash with her private key to create a digital signature SASA​.
            Alice sends the message MM along with the digital signature SASA​ to Bob.

        Bob wants to send a message NN to Alice:
            Bob creates a hash of the message NN.
            Bob encrypts the hash with his private key to create a digital signature SBSB​.
            Bob sends the message NN along with the digital signature SBSB​ to Alice.

    Message Verification:

        When Bob receives the message MM and the signature SASA​ from Alice:
            Bob decrypts SASA​ using Alice's public key to get the hash HAHA​.
            Bob hashes the received message MM to get HMHM​.
            Bob compares HAHA​ and HMHM​. If they match, the message is verified to be from Alice and untampered.

        When Alice receives the message NN and the signature SBSB​ from Bob:
            Alice decrypts SBSB​ using Bob's public key to get the hash HBHB​.
            Alice hashes the received message NN to get HNHN​.
            Alice compares HBHB​ and HNHN​. If they match, the message is verified to be from Bob and untampered.

## Message Requirements

In the context of the "handshake" challenge involving the exchange of signed messages, 
the content of these messages must meet certain requirements to ensure secure and verifiable communication. 
These requirements include:

    Non-Predictability:
        The content should not be easily predictable or guessable. This helps to prevent replay attacks, 
        where an attacker could intercept a message and send it again to impersonate the sender.

    Uniqueness:
        Each message should include a unique identifier, such as a timestamp, nonce (number used once), 
        or sequence number, to distinguish it from other messages. This helps to ensure that each message 
        is unique and cannot be reused by an attacker.

    Relevance and Completeness:
        The message should contain all the necessary information required for the handshake process. 
        This might include the sender's identity, the purpose of the message, and any other relevant data.

    Integrity:
        The message content must remain unchanged from the time it is signed until the recipient verifies it. 
        Any alteration should be detectable through the verification process.

    Format:
        The message should be formatted in a way both parties have agreed upon, 
        ensuring it can be properly interpreted and verified.

    Confidentiality (Optional):
        If the content is sensitive, it should be encrypted to ensure that only the intended recipient can read it. 
        This is optional depending on the specific requirements of the handshake challenge.
        
