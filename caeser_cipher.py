alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
exit = False

#encode
def encode(text, shift):
    new_code = ""
    for letters in text:
        #find the position of the letter in the alphabet list
        position = alphabet.index(letters)
        #add the newly encoded letter to the new_code string
        new_code += alphabet[position + shift]
    print(new_code)

#decode
def decode(text, shift):
    new_code = ""
    for letters in text:
        position = alphabet.index(letters)
        new_code += alphabet[position - shift]
    print(new_code)

while exit == False:
    action = input("Type 'encode' to encrypt or 'decode' to decrypt or 'exit' to exit: ")

    if action == "exit":
        break

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if action == "encode":
        encode(text, shift)
    elif action == "decode":
        decode(text, shift)
    else:
        print("Something didn't work")
