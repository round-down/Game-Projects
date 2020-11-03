import pygame
pygame.mixer.init()
t=pygame.mixer.Sound('c.ogg')
t.play(loops=-1)

rff=None

while True:
    me=input('[GV/SV/SVB/RP/S/P/UP/SETT/E]:')
    
    if me=='e':
        t.stop()
        break
    elif me=='rp':
        pygame.mixer.Sound.play(t)
    elif me=='gv':
        rff=pygame.mixer.Sound.get_volume(t)
        print(rff)
        continue
    elif me=='s':
        pygame.mixer.Sound.stop()
        continue
    elif me=='p':
        pygame.mixer.Sound.pause()
        continue
    elif me=='up':
        pygame.mixer.Sound.unpause()
        continue
    elif me=='sv':
        if rff==None:
            print('[NEVER GOT MUSIC VOLUME YET]')
            continue
        else:
            svi=input('Input Sound Volume: ')
            t.set_volume(float(svi))
            print('Set Volume to {}'.format(svi))
            continue
    elif me=='svb':
        pygame.mixer.Sound.set_volume(rff)
        print('Set Volume back to {}'.format(rff))
        continue
