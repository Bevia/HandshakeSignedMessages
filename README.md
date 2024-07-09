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
