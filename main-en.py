def main():
    from platform import system
    from json import loads
    import os
    try:
        from random_user_agent.params import SoftwareName,OperatingSystem
        from random_user_agent.user_agent import UserAgent
    except:
        os.system("pip install random_user_agent")
        from random_user_agent.params import SoftwareName,OperatingSystem
        from random_user_agent.user_agent import UserAgent
        global p
    p=None
    if system()=="Windows":p="\\"
    elif system()=="Linux":p="//"
    while True:
        print(
"""

██╗░░░██╗░█████╗░██╗░░██╗
██║░░░██║██╔══██╗╚██╗██╔╝
██║░░░██║███████║░╚███╔╝░
██║░░░██║██╔══██║░██╔██╗░
╚██████╔╝██║░░██║██╔╝╚██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
Also known as UserAgentX...

Random user agent generator written in Python, 
using the Python random-user-agent package
and created by GoldenVadim.

  1. Start generating
  2. Show generated user agents
""")
        e=input(" Select a number >> ")
        if not e in ["1","2"]:pass
        elif e=="2":
            if not os.path.exists("generated"):
                os.mkdir("generated")
                open(f"generated{p}raw.txt","x").close()
            os.startfile("generated")
        elif e=="1":
            if not os.path.exists("generated"):
                os.mkdir("generated")
                open(f"generated{p}raw.txt","x").close()
            count=0
            custom=input("Generate user agents with custom software names and operating systems? [y/N] >> ")
            if not custom in ["y","n","Y","N"]:pass
            elif custom in ["n","N"]:
                software_names=[SoftwareName.CHROME.value,SoftwareName.OPERA.value,SoftwareName.EDGE.value,SoftwareName.CHROMIUM.value,SoftwareName.FIREFOX.value,SoftwareName.BLACKBERRY.value,SoftwareName.ALIENBLUE.value,SoftwareName.BLUE_CHROME.value]
                operating_systems=[OperatingSystem.WINDOWS.value,OperatingSystem.WINDOWS_MOBILE.value,OperatingSystem.WINDOWS_PHONE.value,OperatingSystem.LINUX.value,OperatingSystem.ANDROID.value,OperatingSystem.CHROMEOS.value,OperatingSystem.IOS.value,OperatingSystem.MACOS.value,OperatingSystem.BLACKBERRY.value,OperatingSystem.UNIX.value,OperatingSystem.WEBOS.value]
                limit=int(input("Please, write a limit of user agents >> "))
                ua=UserAgent(limit,software_names=software_names,operating_systems=operating_systems)
                with open(f"generated{p}raw.txt","wt") as generated:
                    for user_agent in ua.get_user_agents():
                        count+=1
                        print(f"Writing {ua.get_random_user_agent()} ({0}) to generated user agents...")
                        generated.write(f"{ua.get_random_user_agent()}\n")
                    generated.close()
                    print(f"Successfully generated {count} user agents.")
                    if system()=="Windows":os.system("pause")
if __name__=="__main__":main()