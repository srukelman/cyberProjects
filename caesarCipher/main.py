def main():
    while True:
        print("Encode(e) or Decode(d)?")
        selection = input()
        if selection.lower() == "encode" or selection.lower() == "e":
            encode()
        else:
            decode()
        print("\nContinue(Y/N)?")
        cont = input()
        if cont.lower() == "no" or cont.lower() == "n":
            break
        else:
            continue
            

def encode():
    encText =""
    print("\nText to Encode: ")
    plainText = input()
    print("\nShift: ")
    shift = int(input())
    for i in plainText:
            val = ord(i) + shift
            if(val < 97):
                val +=26
            if(val < 97):
                val = ord(i)
            encText += chr(val)
    print(encText)

def decode():
    decText = ""
    print("\nText to Decode: ")
    encText = input()
    print("\nKnown Shift (Y/N)? ")
    known = input()
    if known.lower() == "yes" or known.lower() == "y":
        print("\nShift Value: ")
        shift = int(input())
        for i in encText:
            val = ord(i) -shift
            if(val < 97):
                val +=26
            if(val < 97):
                val = ord(i)
            decText += chr(val)
    else:
        pass
    print(decText)
if __name__ == "__main__":
    main()