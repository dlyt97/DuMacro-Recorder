#DuMacro RECORDER - KEYBOARD
from pynput import keyboard
import time
x=input('File name:')
macro = r''+x+'.py'
fw=open(macro,'w')
fw.write('from pynput.keyboard import Key, Controller\n\n')
fw.write('import time\n\n')
fw.write('keyboard = Controller()\n\n')
fw.close()
duTime_v2 = [] # PRESS <-> RELEASE
duTime_v2_release = [] # RELEASE <-> PRESS 
endd = [] # RELEASE <-> PRESS (TIME)
VREME_KEY = []
def on_press(key):
    try:
        if len(VREME_KEY) == 1:
            str_vreme = 'time.sleep('+str(time.time() - VREME_KEY[0])+')\n'
            zapis=open(macro,'a')
            zapis.write(str_vreme)
            zapis.close()
            VREME_KEY.clear()
        jedan  = time.time()
        duTime_v2_release.append(jedan)
        try:
            if len(duTime_v2_release) == 2:
                string = str(duTime_v2_release[1]-duTime_v2_release[0])
                str_time = '\ntime.sleep('+string+')\n'
                f=open(macro,'a')
                f.write(str_time)
                f.close()
                del duTime_v2_release[0]
        except Exception:
            print('NEMA')
        txt_1 = "\nkeyboard.press('{0}')\n".format(key.char)
        press_1 = txt_1
        f=open(macro,'a')
        f.write(press_1)
        f.close()
        start = time.time()
        duTime_v2.append(start)   
    except AttributeError:
        txt_2 = "\nkeyboard.press({0})\n".format(key)
        press_2 = txt_2
        f=open(macro,'a')
        f.write(press_2)
        f.close()
        start = time.time()
        duTime_v2.append(start)
def on_release(key):
    try:
        end = time.time()
        duTime_v2.append(start)
        str_end = duTime_v2[1] - duTime_v2[0]
        time_sleep = '\ntime.sleep('+str(str_end)+')\n'
        f=open(macro,'a')
        f.write(time_sleep)
        f.close()
        duTime_v2.clear()
    except Exception:
        f=open(macro,'a')
        f.write('\ntime.sleep(0.03)\n')
        f.close()
    txt_3 = "\nkeyboard.release({0})\n".format(key)
    f=open(macro,'a')
    f.write(txt_3)
    f.close()
    if key == keyboard.Key.esc:
        exit()
        return False
def dc97():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
VREME_KEY.append(time.time())
dc97()
