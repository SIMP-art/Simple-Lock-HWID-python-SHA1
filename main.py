import sys, subprocess, time, requests, hashlib

rhwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
hwid = rhwid.encode("utf-8")

enchwid = hashlib.sha1(hwid).hexdigest()

r = requests.get("pastebin link here")
def Main_Program():
    if enchwid in r.text:
        print("Correct hwid. Hello!") 
        time.sleep(.1)
    else:
        print("HWID Not In Database!")
        time.sleep(.1)
        print(f"Your HWID: {rhwid}") 
        time.sleep(3)
        sys.exit()
Main_Program()
