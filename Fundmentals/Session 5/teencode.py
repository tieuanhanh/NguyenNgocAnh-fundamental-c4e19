teen_code = {
    "hc" : "học",
    "ng" : "người",
    "pt" : "phát triển",
    "eny" : "em người yêu",
    "any" : "anh người yêu",
    "ns" : "nói", 
    "ngta" : "người ta",
    "lm" : "làm",
    "r" : "rồi",
    "stt" : "status"
}

loop = True
while loop:
    for key in teen_code.keys():
        print (key, end ="\t")
    print()

    code = input ("Your code? ")

    if code in teen_code :
        print ("*" * 20)
        print ("Code: ", code)
        print ("Translation: ", teen_code[code])
        print ("*" * 20)
    else:
        print ("Not found.")
        contribute = input ("Contribute?(Y/N?) ").upper()
        if contribute == "Y":
            trans = input ("Your translation:")
            teen_code[code] = trans
            print ("Updated")
        else:
            print ("Not updated")
            loop = False

