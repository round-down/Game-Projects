from os import remove, rename
import game as test

def MainMenu():

    atcs=input('\nWould you like to clear the screen?\n\n[Y/Return]: ')
    if atcs in ['y','Y','yes','Yes']:
        for i in range(0,53):
            print()

    print('\n\n\n' + (78*'='))
    test.printa('\n\n\t\t\t   [IN DEVELOPMENT]\n\t\t\t   version: alpha 5.0\n\n\t\t\"SOME\" things won\'t work as expected...',0.5,0.01)
    while True:

        print('\n\n\n' + (78*'='))
        print('\n\n  L [Load Game]','  N [New Game]','  S [Settings]',
              '  Q [Quit Game]','  C [Credits]\n  H [Help]','   T [Test Game]')

        ui=input('\n[L/N/S/Q/C/H/T]: ')

        if ui in ['n','N','New Game','New','new','new game']:

            while True:
                atcs=input('\nWould you like to clear the screen?\n\n[Y/Return]: ')
                if atcs in ['y','Y','yes','Yes']:
                    for i in range(0,53):
                        print()
                    break
                else:
                    break
                
            New_Game()

                
            #ADD THE PLAY GAME FUNCTION HERE WHEN MADE#
            

            
        elif ui in ['l','L','Load Game','Load','load game','load']:
            print('loading game save...')
            
            Load_Game()
            

            #ADD THE PLAY GAME FUNCTION HERE WHEN MADE#


            
        
        elif ui in ['s','S','Settings','settings']:

            Settings()
        
        elif ui in ['e','E','quit','Quit','q','Q','quit game','Quit Game']:
            print('Exiting')
            break
        
        elif ui in ['c', 'C','credits','Credits']:
            print('\n\n\n' + (78*'='))
            test.printa('\n\nCo-Programmers \n\nAbbas Al-Akashi' \
                  '\n& C.M. Hurley\n\n\t\t\t\tAbbacus Inc.',0.5,0.01)
            continue

        elif ui in ['h','H','help','Help']:

            Help()

        elif ui in ['t','T','test','Test','test game','Test Game']:
            test.chields_tale()
  
        else:
            print('\n\n[ INVALID KEY ]')



def New_Game():

    while True:
        while True:
            print(78*'=')
            ugim=input('\nm[Male] or f[Female]? or leave blank\n[M/F]: ')
            if ugim in ['m','M','Male','male','f','F','female','Female']:
                break
            elif ugim in ['none','None','both','b','Both','']:
                print('\nNo discrimination here...')
                break
            else:
                print('\n[ INVALID INPUT ]')
                False

        while True:
            try:
                uaim=int(input('\nAnd your age?\nAge: '))
                if uaim >= 120:
                    print('\nTHAT OLD ?!\nNo way...')
                    False
                elif uaim ==69:
                    print('\nHeh, nice age...')
                    break
                elif uaim ==30:
                    print('\nThirty and Flirty...perhaps?? ;)')
                    break
                elif 19 < uaim < 30:
                    print('\nTwenties are nice')
                    break
                elif 10 <= uaim <= 19:
                    print('\nOoh so young')
                    break
                elif 6 < uaim < 10:
                    input('\nDid you get your parents permission first?\nEh...whatever: ')
                    break
                elif uaim in [1,2,3,4,5,6]:
                    input('I\'m not sure what this game is rated but I\'m pretty\nsure that you cannot play: ')
                    False
                elif uaim < 0:
                    print('\nPlease enter an appropriate age.')
            except ValueError:
                print('\n[ INVALID INPUT ]')
                continue
                    
            
        uni=input('\nEnter a username: ')
        print('\n\n' + (78*'='))
        edit=input('\nInfo:\n\tGender [{}]\n\tAge [{}]\n\tName [{}]\n\nIs your info right?' \
                    '[Y/N]: '.format(ugim,uaim,uni))
        print('\n' + (78*'='))
        if edit in ['y','Y','yes','Yes']:
            pin=input('\nName this file so you can load it in\nthe [Load Game] menu after you quit: ')
            
            f=open(str(pin) + '.txt', 'a')
            
            f.write(uni)
            f.write('\n' + str(uaim))
            f.write('\n' + str(ugim))

            f.close()
            break
        elif edit in ['n','N','no','No']:
            continue
        
    input('Let\'s go!\n[Return]: ')
    test.printa('\nClearing Screen and Loading Data...',0.5,0.01)
    for loading in range(53):
        print()
    print(78*'=')     
    test.printa('\nHello {}, and welcome to Practice Mode!' \
          '\n...Sorry, still in development.'.format(uni),0.5,0.01)



def Load_Game():
    
    while True:
        print(78*'=')
        pin=input('\nEnter the name of your game save: ')
        try:
            f=open(str(pin) + '.txt', 'r')
            und=f.readline()

            test.printa('\nWelcome back ' + str(und),0.5,0.01)
        
            f.close()
            break
        except:
            atr=input('\nFile ' + '[' + pin + ']' + '.txt not found\n\nReturn to main menu?\n[Y/N]: ')
            if atr in ['y','Y','yes','Yes']:
                break
            else:
                continue



def Settings():

    print('\n\n\n' + (78*'='))
    print('\n\t\t\t   [SETTINGS]')
    
    while True:
        print('\n' + (78*'='))
        print('\n\n  B [Back]','  D [Delete Save]','  R [Rename Save]')
        ui=input('\n[B/D/R]: ')
        
        if ui in ['d','D','del','Del','delete save','Delete Save']:
            
            while True:
                sn=input('\n-1[Back]\nName of the save file you want to DELETE: ')

                if sn=='-1':
                    break
                
                else:
                    agds=input('\nIs [ {} ] spelled correctly?\n[Y/N]: '.format(sn))
                    
                    if agds in ['y','Y','yes','Yes']:
                        ag=input('\nAre you sure you want to delete [ {} ]?\n[Y/N]: '.format(sn))
                        
                        if ag in ['y','Y','yes','Yes']:
                            remove(str(sn) + '.txt')
                            input('\n\nDeleted [ {} ]...\n\n[Back]: '.format(sn))
                            break
                        
                        else:
                            break
                        
                    else:
                        continue
                
                
        elif ui in ['r','R','rename','Rename','rename save','Rename Save']:

            while True:
                sn=input('\n-1 [Back]\nName of the save file you want to RENAME: ')

                if sn=='-1':
                    break
                
                else:
                    agds=input('\nIs [ {} ] spelled correctly?\n[Y/N]: '.format(sn))

                    try:
                        f=open(str(sn) + '.txt')
                        f.close()
                        
                    except FileNotFoundError:
                        print('\nFile [ {} ] not found.'.format(sn))
                        continue

                    if agds in ['y','Y','yes','Yes']:

                        while True:
                            
                            rnn=input('\nEnter the new name: ')
                            agrnn=input('\nIs [ {} ] spelled correctly?\n[Y/N]: '.format(rnn))
                            
                            if agrnn in ['y','Y','yes','Yes']:
                                ag=input('\nAre you sure you want to Rename [ {} ] to [ {} ]?\n[Y/N]: '.format(sn,rnn))
                                
                                if ag in ['y','Y','yes','Yes']:
                                    rename(str(sn) + '.txt',str(rnn) + '.txt')
                                    input('\n\nRenamed [ {} ] to [ {} ]...\n\n[Back]: '.format(sn,rnn))
                                    break
                                
                                else:
                                    if ag in ['n','N','no','No']:
                                        print('\nReturning to Rename option...')
                                        break
                                    else:
                                        print('\nInvalid key, taken as [N]\nReturning to Rename option...')
                                        break

                            else:
                                print('\n[ INVALID KEY ] taken as [N]')
                                continue
                            
                    else:
                        continue

        #elif [Add more settings here]

        elif ui in ['b','B','back','Back']:
            break

        else:
            print('\n\n[ INVALID KEY ]')
            continue
        


def Help():

    print('\n\n\n' + (78*'='))
    print('\n\t\t\t   [HELP]','\n\n\tAdd info here later')
    ip=input('\n[Return]: ')




    
MainMenu()
