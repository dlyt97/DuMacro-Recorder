from pynput import mouse
import time
_NAME_ = r'DuMOUSE.py'
def write(text,mode='a'):
    f=open(_NAME_,mode);f.write(text);f.close()
string='''from pynput.mouse import Button, Controller
import time
mouse = Controller()\n\n'''
write(string,mode='w')

press_release = []
release_press = []
_TIME_ = []

def on_move(x, y):
    if len(_TIME_) == 1:
        write('\ntime.sleep('+str(time.time()-_TIME_[0])+')\n')
        _TIME_.clear()
    write('\ntime.sleep(1/60)\nmouse.position={0}\n'.format((x, y)))
    
def on_click(x, y, button, pressed):
    position='\nmouse.position={0}\n'.format((x, y))
    
    if pressed:
        if len(_TIME_) == 1:
            write('\ntime.sleep('+str(time.time()-_TIME_[0])+')\n')
            _TIME_.clear()
        release_press.append(time.time())
        if len(release_press) == 2:
            write('\ntime.sleep('+str(release_press[1]-release_press[0])+')\n')
            del release_press[0]
        write(position)
        if button == mouse.Button.left:
            write('\nmouse.press(Button.right)\n')
        if button == mouse.Button.right:
            write('\nmouse.press(Button.left)\n')
        press_release.append(time.time())
        return True
    
    if not pressed:
        write(position)
        write('\ntime.sleep('+str(time.time() - press_release[0])+')\n')
        if button == mouse.Button.left:
            write('\nmouse.release(Button.right)\n')
        if button == mouse.Button.right:
            write('\nmouse.release(Button.left)\n')
        press_release.clear()
        return False
    
def on_scroll(x, y, dx, dy):
    txt=str('\nmouse.scroll{0}{1}\ntime.sleep(1/60)\n'.format('' if dy < 0 else '',(x, y)))
    write(txt)
    
def on_release(key):
    if key == keyboard.Key.esc:
        exit()
        return False
    
def _mouse_():
    with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
        listener.join()
        
def du_mouse():
    _TIME_.append(time.time())
    while True:
        _mouse_()
du_mouse()
