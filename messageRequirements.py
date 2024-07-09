from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import time
import json
import os


# Function to generate RSA keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return public_key, private_key


# Function to create a message
def create_message(content, sender_id):
    timestamp = time.time()
    nonce = os.urandom(16).hex()  # Generate a unique nonce
    message = {
        'content': content,
        'sender_id': sender_id,
        'timestamp': timestamp,
        'nonce': nonce
    }
    return json.dumps(message)


# Function to sign a message
def sign_message(message, private_key):
    message_bytes = message.encode()
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


# Function to verify a message
def verify_message(message, signature, public_key):
    message_bytes = message.encode()
    try:
        public_key.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False


# Generate RSA keys for Alice and Bob
alice_public_key, alice_private_key = generate_keys()
bob_public_key, bob_private_key = generate_keys()

# Alice creates and signs a message
M_content = "Hello Bob"
M = create_message(M_content, "Alice")
signature_A = sign_message(M, alice_private_key)

# Bob verifies Alice's message
if verify_message(M, signature_A, alice_public_key):
    print("Bob: Message from Alice is verified and untampered.")
else:
    print("Bob: Message from Alice could not be verified or was tampered.")

# Bob creates and signs a message
N_content = "Hello Alice"
N = create_message(N_content, "Bob")
signature_B = sign_message(N, bob_private_key)

# Alice verifies Bob's message
if verify_message(N, signature_B, bob_public_key):
    print("Alice: Message from Bob is verified and untampered.")
else:
    print("Alice: Message from Bob could not be verified or was tampered.")
