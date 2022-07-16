import os

if os.name == 'nt':
    import msvcrt

class KBHit:
    
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''

        if os.name == 'nt':
            pass
        
        else:
    
            # Save settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)
    
            # New terminal settings
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
    
            # Normal-terminal reset at exit
            atexit.register(self.set_normal_term)
    
    #Resets terminal to normal
    def set_normal_term(self):
        if os.name == 'nt':
            pass
        
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    #Returns keyboard character after kbhit() is called. Don't use with get arrow.
    def getch(self):
        s = ''
        
        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')
        
        else:
            return sys.stdin.read(1)
                        
    #Returns arrow-key code after kbhit() has been called 0: up 1: right 2: down 3: left Not to be used with getch()
    def getarrow(self):
        
        if os.name == 'nt':
            msvcrt.getch()
            c = msvcrt.getch()
            vals = [72, 77, 80, 75]
            
        else:
            c = sys.stdin.read(3)[2]
            vals = [65, 67, 66, 68]
        
        return vals.index(ord(c.decode('utf-8')))
        
    #Returns true if keyboard is hit, otherwise false.
    def kbhit(self):
        if os.name == 'nt':
            return msvcrt.kbhit()
        
        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []
    
    
# Test    
if __name__ == "__main__":
    
    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break
            print(c)
             
    kb.set_normal_term()