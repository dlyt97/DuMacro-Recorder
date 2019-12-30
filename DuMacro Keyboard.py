#DuMacro RECORDER - KEYBOARD
from pynput import keyboard
import time

press_release=[]
release_press=[]
VREME_KEY=[]

macro=r'DuKEY.py'

def zapis(text,mode='a'):
    f=open(macro,mode);f.write(text);f.close()
zap='''from pynput.keyboard import Key, Controller
import time
keyboard = Controller()\n\n'''
zapis(zap,'w')

def on_press(key):
    try:
        if len(VREME_KEY) == 1:
            try:
                zapis('time.sleep('+str(time.time() - VREME_KEY[0])+')\n')#WRITE
            except:
                print('NECE DA SE ZAPISE VREME ZA PRESS KEY !!!')
            VREME_KEY.clear()
        release_press.append(time.time())
        try:
            if len(release_press) == 2:
                try:
                    zapis('\ntime.sleep('+str(release_press[1]-release_press[0])+')\n')#WRITE
                except:
                    print('NECE DA SE ZAPISE VREME ZA PRESS KEY & RELEASE KEY !!!')
                del release_press[0]
        except Exception:
            print('NEMA')
        zapis(str("\nkeyboard.press('{0}')\n".format(key.char)))#WRITE
        press_release.append(time.time())
    except AttributeError:
        try:
            zapis("\nkeyboard.press({0})\n".format(key))#WRITE
        except:
            print('NECE DA SE ZAPISE !!!')
        press_release.append(time.time())
        
def on_release(key):
    try:
        press_release.append(time.time());zapis(str('\ntime.sleep('+str(press_release[1] - press_release[0])+')\n'));press_release.clear()
    except Exception:
        try:
            zapis(str('\ntime.sleep(0.03)\n'))
        except:
            print('NECE DA SE ZAPISE 0.03 VREME !!!')
    try:
        zapis(str("\nkeyboard.release({0})\n".format(key)))
    except:
        print('NECE DA SE ZAPISE RELEASE KEY !!!')
    if key == keyboard.Key.esc:
        exit()
        return False
    
def _keyboard_():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    
def du_key():
    VREME_KEY.append(time.time())
    _keyboard_()
    
du_key()
