import uuid
import datetime

print(f"""
dP     dP dP     dP dP 888888ba            .88888.   88888888b 888888ba  
88     88 88     88 88 88    `8b          d8'   `88  88        88    `8b 
88     88 88     88 88 88     88          88         a88aaaa   88     88 
88     88 88     88 88 88     88 88888888 88   YP88  88        88     88 
Y8.   .8P Y8.   .8P 88 88    .8P          Y8.   .88  88        88     88 
`Y88888P' `Y88888P' dP 8888888P            `88888'   88888888P dP     dP

This very simple tool assists in generating UUIDs.
It is recommended to not go over a count of 10000.
Find this project on GitHub: https://github.com/Dborasik/UUID-Gen
""")

def requestUUIDCount():
    while(True):
        UUIDCount = input("[?] Input UUID Count >>> ")
        if UUIDCount.isnumeric():
            if int(UUIDCount) > 0:
                return int(UUIDCount)
                continue
            else:
                print("[!] Invalid UUID Count. Please try again.")
                continue
        else:
            print("[!] Invalid UUID Count. Please try again.")
            continue

def requestOutputType():
    while(True):
        outputType = input("[?] Output Type [Regular/Quiet] >>> ")
        match outputType.lower():
            case "regular":
                return "regular"
                break
            case "quiet":
                return "quiet"
                break
            case _:
                print("[!] Invalid Output Type. Please try again.")
                continue
        break

def requestExitDecision():
    while(True):
        exitDecision = input("[?] Exit Program [Y/N] >>> ")
        match exitDecision.lower():
            case "y":
                return True
                break
            case "n":
                return False
                break
            case _:
                print("[!] Invalid Exit Decision. Please try again.")
                continue
        break


def generate_uuid():
    return str(uuid.uuid4())

def generate_uuids_list(count):
    return [generate_uuid() for i in range(count)]

def write_to_file(generatedUUIDs, UUIDCount, outputType):
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
    fileName = f"UUIDs_{UUIDCount}_{currentDate}.txt"

    with open(fileName, "w") as f:
        currentDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if outputType == "regular":
            f.write("Created by UUIDGenerator.py\n")
            f.write(f"Generated on {currentDateTime}\n")
            f.write(f"Total Count: {UUIDCount}\n\n")
        for uuid in generatedUUIDs:
            f.write(f"{uuid}\n")

try :
    exitProgram = False
    while(exitProgram == False):
        UUIDCount = requestUUIDCount()
        outputType = requestOutputType()
        print("[*] Generating UUIDs...")
        generatedUUIDs = generate_uuids_list(UUIDCount)
        print("[*] Writing UUIDs to file...")
        write_to_file(generatedUUIDs, UUIDCount, outputType)
        print(f"[✓] Generation of file with {UUIDCount} UUIDs complete.")
        exitProgram = requestExitDecision()
    
    print("[*] Exiting program...")
    print("""
___ _  _ ____ _  _ _  _    _   _ ____ _  _ 
 |  |__| |__| |\ | |_/      \_/  |  | |  | 
 |  |  | |  | | \| | \_      |   |__| |__|
    """)

except Exception as e:
    print(f"""
 __ __  __  __  __  
|_ |__)|__)/  \|__) 
|__| \ | \ \__/| \\

{e}

A fatal error has occured and the program must exit.
If this issue continues, please open an issue on Github.
    """)
    exit()