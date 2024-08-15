import random, os, time, requests, datetime

def menu():
  print("""
  """)
  print("""██████╗ ███████╗██████╗ ██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔════╝██╔══██╗██║██║   ██║████╗ ████║
██████╔╝█████╗  ██║  ██║██║██║   ██║██╔████╔██║
██╔══██╗██╔══╝  ██║  ██║██║██║   ██║██║╚██╔╝██║
██████╔╝███████╗██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
╚═════╝ ╚══════╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
  
  [>] Nitro Generator + Checker
  [>] Exit
  """)

  choice = int(input("[>] Choice: "))
  valid = 0
  valid_codes = []
  invalid = 0

  if choice == 10101010:
    amt = int(input("[>] How Many Nitro Codes Would You Like To Generate?: "))
    codeLen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890"
    k = open("utilities/other/NG/vaildnitrocodes.txt", "w")
    for i in range(amt):
      print("[$] https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)))
      k.write("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + "\n")
    k.close()
    print("[+] Codes saved to Vaildnitrocodes.txt")
  elif choice == 487814:
    with open("CodesToCheck.txt") as f:
      for line in f:
        s = requests.Session()
        nitro = line.strip("\n")
        start = datetime.datetime.now()


        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"


        r = s.get(url)

        if r.status_code == 200:
          print(f"[#] Valid | {nitro}".format(line.strip("\n")))
          valid_codes.append(nitro)
          valid += 1

          
          k = open("utilities/other/NG/2/Valids.txt", 'w')
          k.write(valid_codes)
        else:
          print(f"[!] Invalid | {nitro}".format(line.strip("\n")))
          invalid += 1
      print("\n")
      print(f"""
      Valids = {valid}
      Invalids = {invalid}
      Valid Codes: {', '.join(valid_codes)}
      """)
  elif choice == 1:
    amt = int(input("[>] How Many Nitro Codes Would You Like To Generate and Check?: "))
    codeLen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890"
    g = open("utilities/other/NG/1/AllCodes.txt", "w")
    u = open("utilities/other/NG/2/Valids.txt", "w")
    n = open("utilities/other/NG/3/Invalids.txt", "w")
    for i in range(amt):
      g.write("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + "\n")
    g.close()

    with open("utilities/other/NG/1/AllCodes.txt") as f:
      for line in f:
        invalid_codes = []
        valid_codes = []
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        s = requests.Session()

        r = s.get(url)

        if r.status_code == 200:
          print(f"[$] Valid | {nitro}".format(line.strip("\n")))

          valid_codes.append(nitro)
          break
        else:
          print(f"[x] Invalid | {nitro}".format(line.strip("\n")))

          invalid_codes.append(nitro)



  elif choice == 2:
    os.system('cls')
    print("[!] Quitting...") 
    time.sleep(3)
    exit(0)   
menu()