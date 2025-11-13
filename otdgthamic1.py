def caesar_cipher():
    while True:
        operation = input("Type encode to encrypt, type decode to decrypt: ").strip().lower()
        
        if operation not in ["encode", "decode"]:
            print("Invalid operation. Please type 'encode' or 'decode'.")
            continue
        
        message = input("Type your message: ")
        
        try:
            shift = int(input("Type the shift number: "))
        except ValueError:
            print("Invalid shift number. Please enter an integer.")
            continue
        
        result = ""
        for char in message:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                
                if operation == "encode":
                    shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                
                result += shifted_char
            else:
                result += char
        
        print(f"Here is {operation} result: {result}")
        
        continue_program = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_program != "yes":
            break

if __name__ == "__main__":
    caesar_cipher()