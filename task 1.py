def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_base + shift) % 26
            result += chr(shifted + ascii_base)
        else:
            result += char
            
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("\nCaesar Cipher Encryption/Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
            
        message = input("Enter the message: ")
        
        while True:
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid number.")
        
        if choice == '1':
            result = encrypt(message, shift)
            print(f"\nEncrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"\nDecrypted message: {result}")

if __name__ == "__main__":
    main()