alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def coded(teks,lompat,direct):
    kosong=''
    if direct =='encode':
        for i in teks:
            if i in alphabet:
                p=alphabet.index(i)
                en=p+lompat
                if en>len(alphabet)-1: #atau bisa juga list alphabet di dobelin
                    en=lompat-1
                    kosong+=alphabet[en]
                else:             
                    kosong+=alphabet[en]
            else:
                kosong+=i
        print(f"The encoded text is {kosong}")
    elif direct=='decode':
        for i in teks:
            if i in alphabet:
                p=alphabet.index(i)
                en=p-lompat
                if en>len(alphabet)-2: #atau bisa juga list alphabet di dobelin
                    en=lompat+1
                    kosong+=alphabet[en]
                else:             
                    kosong+=alphabet[en]
            else:
                kosong+=i
        print(f"The decoded text is {kosong}")
    else:
        print('please only input "encode" or "decode" only')
        

    