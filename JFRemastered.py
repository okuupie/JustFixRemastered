import os
import shutil
import subprocess
import random
import time
import buttonpad

rnum = random.randint(1, 9999)
temp = os.getenv('APPDATA')
temp2 = os.getenv('USERPROFILE')
temp3 = os.path.join(temp2, "Desktop")
pt1 = "C:\\Sk3dGuardNew"
pt2 = os.path.join(temp, "Sk3dGuard")
drfold = os.path.join(temp3, "JF-Remastered")
dr1 = "https://aka.ms/vc14/vc_redist.x64.exe"
dr2 = "https://go.microsoft.com/fwlink/?linkid=2124701"
dr3 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/7.0.410/dotnet-sdk-7.0.410-win-x64.exe"
dr4 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.418/dotnet-sdk-8.0.418-win-x64.exe"
dr5 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/9.0.311/dotnet-sdk-9.0.311-win-x64.exe"
dr6 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.103/dotnet-sdk-10.0.103-win-x64.exe" 

def sl(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
        )
        return result.stdout
    except:
        return ""

bp = buttonpad.ButtonPad(
    """исправить котлаван""",
    title="JustFixer remastered // @nachlene220",
    status_bar=f"нажми на кнопку - меню может залагать, просто жди // User #{rnum}"
)

def mk(widget, x, y):
    bp.status_bar=f"создал папку на рабочем столе - JF-Remastered // User #{rnum}"
    os.makedirs(drfold, exist_ok=True)

def fixc(widget, x, y):
    if os.path.exists(pt1):
        shutil.rmtree(pt1)
    if os.path.exists(pt2):
        shutil.rmtree(pt2)
    bp.status_bar=f"удалил файлы котлавана... // User #{rnum}"

def drins(widget, x, y):
    bp.status_bar=f"начал установку драйверов... ожидайте / ВЫКЛЮЧИТЕ ВПН ЕСЛИ НЕ ГРУЗИТ // User #{rnum}"
    sl(f'curl -L -k -o "{drfold}\\Drive1.exe" "{dr1}"')
    sl(f'curl -L -k -o "{drfold}\\Drive2.exe" "{dr2}"')
    sl(f'curl -L -k -o "{drfold}\\Drive3.exe" "{dr3}"')
    sl(f'curl -L -k -o "{drfold}\\Drive4.exe" "{dr4}"')
    sl(f'curl -L -k -o "{drfold}\\Drive5.exe" "{dr5}"')
    sl(f'curl -L -k -o "{drfold}\\Drive6.exe" "{dr6}"')

def rn(widget, x, y):
    bp.status_bar=f"открываю драйвера... // User #{rnum}"
    sl(f"start \"\" \"{drfold}\\Drive1.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive2.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive3.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive4.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive5.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive6.exe\"")

def runsc(widget, x, y):
    mk(widget, x, y)
    time.sleep(3)
    fixc(widget, x, y)
    time.sleep(1)
    drins(widget, x, y)
    rn(widget, x, y)
    input('любая клавиша для выхода')
    exit(0)

bp[0, 0].on_click = runsc

bp.run()