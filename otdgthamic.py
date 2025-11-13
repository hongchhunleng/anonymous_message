def anonymous_message():
    while True:
        # sur ke jong encode or decode hz ah .strip ng delete space derm bey srul check
        operation = input("Type encode to encrypt, type encode to decode: ").strip().lower()
        
        # check tha ke input trov ot ber ke sorse trov doch del yg jong ban hz continues tt
        if operation not in ["encode", "decode"]:
            print("Invalid operation. Please type 'encode' or 'decode'.")
            continue
        
        # dak massage del jong process
        message = input("Type your message: ")
        
        # jom noun shift del jong ban
        try:
            shift = int(input("Type the shift number: "))
        # ah except ValueError ng doch knea check dae yg check tha ke input lek kut or ey pseng
        # yy tv ber ke input krav pi lek kut oy ke input m'dg tt tus ke input lek del mean juj kor khos dae
        except ValueError:
            print("Invalid shift number. Please enter an integer.")
            continue
        
        # Process
        result = "" # ah nis dak vea t'ne jol tuk dak ah pel vea encode or decode hz vea jol tv ng
        for char in message:
            if char.isalpha(): # .isalpha ng chceck tur ahsor pkot tha man symbol ng lek berk ber check hz khernh tur ng chea symbol or lek vea bos oy else hz bos oy tv result mg  
                # kom nort tur ahsor muy muy tha chea ah sor thom or toch prus code khos knea
                # hz ord() ng chae build-in function muy somrap convert pi tur ah sor tv chea
                # lek unicode tam keyboard example A=65, a=97
                # tea jur krom nis yg oy defual vea jg vea check tur ah sor ber sen chea ah sor thom 
                # vea oy ascii_offset ng = A thom = 65 
                # tea ber ah sor toch
                # vea oy ascii_offset ng = a thom = 97 
                ascii_offset = ord('A') if char.isupper() else ord('a')
                
                # Apply the shift based on the operation
                if operation == "encode":
                    # chr() ng kor build-in function hz muk ngea vea convert pi unicode tv ah sor venh
                    # ord (char) ng yg yk tur ah sor message muy muy mk convert tv lek
                    # Rouj dork ng lek del yg oy ban mk pi ascii_offset
                    # hz + ng shift ke input 
                    # hz jek yk som norl ng 26
                    # % ng vea jek yk som norl example 25 % 26 jek ot kert jg lek ng = 25 del
                    # tea ber 26 % 26 = som norl sol 0
                    # tea ber 27 % 26 = nom norl sol 1 jg hah 
                    # hz + ng ascii_off venh 
                    # example 
                    # "H" jmuy shift 3:
                    # H thom = 72 hz vea chea ah sor thom jg ascii yg = 65 hz shift yg = 3 
                    # yg ban -> (72-65+3)%26+65 = (10)%26+65 = 10+65 = 75 -> K
                    # jg "H" -> "K"
                    shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:  # decode
                    shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                
                # jung kroy yg tur ah sor del process hz ng bos oy result nv ler 
                result += shifted_char
            else:
                # klaeng nis del tha check chea symbol or lek ng huh yg vea ot process te vea mk nis eng vea bos oy result direct mg
                result += char
        
        # result
        print(f"Here is {operation} result: {result}")
        
        # sur tha jong continue or not 
        continue_program = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_program != "yes":
            break

# Run the program
if __name__ == "__main__":
    anonymous_message()