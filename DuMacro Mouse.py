# DuMacro Recorder - MOUSE
from pynput import mouse
from pynput import keyboard
import time

x=input('File name:')
macro = r''+x+'.py'
f=open(macro,'w')
f.write('from pynput.mouse import Button, Controller\n')
f.write('\nimport time\n')
f.write('\nmouse = Controller()\n')
f.close()
press_release_time = []
release_press_time = []
VREME = []
VREME_CLICK = []
def on_move(x, y):
    if len(VREME) == 1:
        zap_1 = '\ntime.sleep('+str(time.time()-VREME[0])+')\n'
        fww=open(macro,'a')
        fww.write(zap_1) # WRITE
        fww.close()
        VREME.clear()
    txt='\ntime.sleep(1/60)\nmouse.position={0}\n'.format((x, y))
    fw=open(macro,'a')
    fw.write(txt) # WRITE
    fw.close()
def on_click(x, y, button, pressed):
    position='\nmouse.position={0}\n'.format((x, y))
    if pressed:
        if len(VREME) == 1:
            zap_1 = '\ntime.sleep('+str(time.time()-VREME[0])+')\n'
            fww=open(macro,'a')
            fww.write(zap_1) # WRITE
            fww.close()
            VREME.clear()
        release_press_time.append(time.time())
        if len(release_press_time) == 2:
            num = release_press_time[1]-release_press_time[0]
            txt_num = '\ntime.sleep('+str(num)+')\n'
            fw=open(macro,'a')
            fw.write(txt_num) # WRITE
            fw.close()
            del release_press_time[0]
        f_w=open(macro,'a')
        f_w.write(position) # WRITE
        f_w.close() 
        if button == mouse.Button.left:
            str_press = '\nmouse.press(Button.right)\n'
            fw=open(macro,'a')
            fw.write(str_press) # WRITE
            fw.close()
        if button == mouse.Button.right:
            str_press = '\nmouse.press(Button.left)\n'
            fw=open(macro,'a')
            fw.write(str_press) # WRITE
            fw.close()
        press_release_time.append(time.time())
        return True
    if not pressed:
        f_w=open(macro,'a')
        f_w.write(position) # WRITE
        f_w.close() 
        str_release = '\ntime.sleep('+str(time.time() - press_release_time[0])+')\n'
        f__w=open(macro,'a')
        f__w.write(str_release) # WRITE
        f__w.close()
        
        if button == mouse.Button.right:
            fw=open(macro,'a')
            fw.write('\nmouse.release(Button.right)\n') # WRITE
            fw.close()
        if button == mouse.Button.left:
            fw=open(macro,'a')
            fw.write('\nmouse.release(Button.left)\n') # WRITE
            fw.close()
        
        press_release_time.clear()
        return False
def on_release(key):
    if key == keyboard.Key.esc:
        exit()
        return False
def dc97():
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
        listener.join()
VREME.append(time.time())
while True:
    dc97()
