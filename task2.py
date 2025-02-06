import cv2
import numpy as np

def encrypt_image(image_path, key):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        return None
        
    # Generate a random key matrix of the same size as the image
    np.random.seed(key)
    key_matrix = np.random.randint(0, 256, img.shape, dtype=np.uint8)
    
    # Encrypt the image using XOR operation
    encrypted = cv2.bitwise_xor(img, key_matrix)
    return encrypted

def decrypt_image(encrypted_image, key):
    # Decryption is the same as encryption due to XOR properties
    np.random.seed(key)
    key_matrix = np.random.randint(0, 256, encrypted_image.shape, dtype=np.uint8)
    decrypted = cv2.bitwise_xor(encrypted_image, key_matrix)
    return decrypted

def main():
    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
            
        if choice == '1':
            # Encryption
            image_path = input("Enter image path: ")
            key = int(input("Enter a numeric key (remember this!): "))
            
            encrypted = encrypt_image(image_path, key)
            if encrypted is None:
                print("Error: Could not read image!")
                continue
                
            cv2.imwrite('encrypted_image.png', encrypted)
            print("Image encrypted and saved as 'encrypted_image.png'")
            
        elif choice == '2':
            # Decryption
            encrypted_path = input("Enter encrypted image path: ")
            key = int(input("Enter the same numeric key used for encryption: "))
            
            encrypted = cv2.imread(encrypted_path)
            if encrypted is None:
                print("Error: Could not read encrypted image!")
                continue
                
            decrypted = decrypt_image(encrypted, key)
            cv2.imwrite('decrypted_image.png', decrypted)
            print("Image decrypted and saved as 'decrypted_image.png'")
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()