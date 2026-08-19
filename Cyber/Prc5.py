# Diffie-Hellman key exchange

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter alice's private key: "))
b = int(input("Enter bob's private key: "))

#public keys
A = pow(g, a, p)
B = pow(g, b, p)

# shared secret keys
KA = pow(B, a, p)
KB = pow(A, b, p)

print("\nAlice's public key: ",A)
print("Bob's public key:, B")

print("\nAlice's shared secret:", KA)
print("Bob's shared secret:", KA)

if KA == KB:
    print("\n Key Exchange Successful!")
else:
    print("\nKey Exchange Failed!")
    
