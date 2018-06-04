dics = {
    "hc" : "hoc",
    "ng" : "nguoi",
    "ns" : "noi",
    "any" : "anh nguoi yeu",
    "eny" : "em nguoi yeu"
}
while True:
    for k in dics:
        print(k, end="\t")  #\t = tab
    print()
    print("* " * 20)
    code = input("Code: ")

    if code in dics:
        print("Translation: ",dics[code])
    else:
        ques = input("Not found, do you want to contribute this word? (Y/N): ").upper()
        if ques == "Y":
            ans = input("Enter your translation: ")
            dics[code] = ans
            print(code," = ",ans)
        else:
            break

