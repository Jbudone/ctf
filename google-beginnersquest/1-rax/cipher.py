
with open('flag') as reader:
    encrypted = reader.readline().replace('\n', '').lower()
    for caesarOffset in range(25):
        caesarDec = ''.join(chr(((ord(charEnc) - ord('a') + caesarOffset) % 26) + ord('a')) if (charEnc >= 'a' and charEnc <= 'z') else charEnc for charEnc in encrypted)
        if caesarDec.find("flag") != -1:
            print(caesarDec)
