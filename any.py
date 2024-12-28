import yt_dlp
import pyfiglet
from colorama import init, Fore, Style
import time
init()
text = "Ghost"
formatted_text = pyfiglet.figlet_format(text)
print (Fore.BLUE + formatted_text + Style.RESET_ALL)
words = [Fore.MAGENTA + "<Ghost> : "+ Style.RESET_ALL,"Hi","user","welcome","to",Fore.MAGENTA +"@Ghost"+ Style.RESET_ALL,Fore.RED +":)"+Style.RESET_ALL,Fore.MAGENTA +"\n\n<Ghost> : "+ Style.RESET_ALL,"Ghost", "is",Fore.RED +"simple","virus","and","tools"+ Style.RESET_ALL,"for","Beginner","programming","in","python"]
for word in words:
    print(word, end=' ', flush=True)
    time.sleep(0.09)  
print()  
def download_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  
        'format': 'best',                
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("[+] Downloading video...")
            ydl.download([url])
            print("[+] Download complete!")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    words = [Fore.MAGENTA + "<Ghost> : "+ Style.RESET_ALL,"Supported","platforms",":",Fore.RED +"YouTube","Instagram","TikTok","Facebook","etc."+ Style.RESET_ALL, ]
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(0.09)  
    print()  
    link = input(Fore.YELLOW +"<Ghost> : Enter the video link to download: "+ Style.RESET_ALL)
    download_video(link)
