sk = ['Start', 'Holod', 'Golod', 'Radosti', 'Sciastie', 'Exit',
                 'Rabota', 'Otdih']
napravlenia = ['Iug', 'Sever', 'Zapad', 'Vostok']

gotovnosti = input('Potverdite shto vi gotovi igrati:')
while gotovnosti != 'Da' :
    gotovnosti = input('Potverdite shto vi gotovi igrati:')
komnata = sk[0]
print(napravlenia)
print('Vi nahoditesi v komnatе Start -> Tut ocheni klassno i uiutno.')
while komnata != sk[5] :


    if komnata == sk[0] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia :
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug':
            komnata = sk[3]
            print('Vi nahoditesi v komnate Radosti -> Tut mi ocheni horsho sebea chiuvstvuem.')
        elif napr == 'Sever' :
            komnata = sk[1]
            print('Vi nahoditesi v komnate Holoda -> Tut nabliudaiutsea kraine nizkie temeperatu'
                      'ri vozduha.')
        elif napr == 'Vostok' :
            komnata = sk[2]
            print('Vi nahoditesi v komnate Goloda -> Tut postoianna net edi v dostatochnom koli'
                      'chestve.')
        elif napr == 'Zapad' :
            komnata = sk[4]
            print('Vi nahoditesi v komnate Sciastia -> Tut vse naslazhdaiutsea zhizniu.')
        else :
            print('Takogo napravlenia ne sushestvuet!')


    if komnata == sk[4] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia:
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug':
            komnata = sk[3]
            print('Vi nahoditesi v komnate Radosti -> Tut mi ocheni horsho sebea chiuvstvuem.')
        elif napr == 'Sever' :
            komnata = sk[1]
            print('Vi nahoditesi v komnate Holoda -> Tut nabliudaiutsea kraine nizkie temeperatu'
                      'ri vozduha.')
        elif napr == 'Vostok' :
            komnata = sk[0]
            print('Vi nahoditesi v komnatе Start -> Tut ocheni klassno i uiutno.')
        elif napr == 'Zapad' :
            komnata = sk[5]
            print('Vi nahoditesi v komnate Exit -> Tut mi gotovimsea k pobede.')
        else :
            print('Takogo napravlenia ne sushestvuet!')


    if komnata == sk[5] :
        print('Vi proshli igru - pozdrovleaem!')


    if komnata == sk[1] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia:
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug':
            komnata = sk[0]
            print('Vi nahoditesi v komnatе Start -> Tut ocheni klassno i uiutno.')
        elif napr == 'Vostok' :
            komnata = sk[2]
            print('Vi nahoditesi v komnate Goloda -> Tut postoianna net edi v dostatochnom koli'
                      'chestve.')
        elif napr == 'Sever' :
            komnata = sk[6]
            print('Vi nahoditesi v komnate Raboti -> Tut vse kraine utomlonie i ne hoteat nich'
                      'ego delati.')
        elif napr == 'Zapad':
            komnata = sk[4]
            print('Vi nahoditesi v komnate Sciastia -> Tut vse naslazhdaiutsea zhizniu.')
        else:
            print('Takogo napravlenia ne sushestvuet!')


    if komnata == sk[3] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia:
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug':
            komnata = sk[7]
            print('Vi nahoditesi v komnatе Otdiha -> Tut vse radaostnie i ne o cheom ne'
                  'pekutsea.')
        elif napr == 'Vostok' :
            komnata = sk[2]
            print('Vi nahoditesi v komnate Goloda -> Tut postoianna net edi v dostatochnom koli'
                  'chestve.')
        elif napr == 'Sever' :
            komnata = sk[0]
            print('Vi nahoditesi v komnatе Start -> Tut ocheni klassno i uiutno.')
        elif napr == 'Zapad':
            komnata = sk[4]
            print('Vi nahoditesi v komnate Sciastia -> Tut vse naslazhdaiutsea zhizniu.')
        else:
            print('Takogo napravlenia ne sushestvuet!')


    if komnata == sk[2] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia:
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug' :
            komnata = sk[3]
            print('Vi nahoditesi v komnate Radosti -> Tut mi ocheni horsho sebea chiuvstvuem.')
        elif napr == 'Zapad' :
            komnata = sk[0]
            print('Vi nahoditesi v komnatе Start -> Tut ocheni klassno i uiutno.')
        elif napr == 'Sever' :
            komnata = sk[1]
            print('Vi nahoditesi v komnate Holoda -> Tut nabliudaiutsea kraine nizkie temeperatu'
                  'ri vozduha.')
        elif napr == 'Vostok' :
            komnata = sk[7]
            print('Vi nahoditesi v komnatе Otdiha -> Tut vse radaostnie i ne o cheom ne'
                  'pekutsea.')
        else :
            print('Takogo napravlenia ne sushestvuet!')




    if komnata == sk[7] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia:
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug' :
            komnata = sk[3]
            print('Vi nahoditesi v komnate Radosti -> Tut mi ocheni horsho sebea chiuvstvuem.')
        elif napr == 'Zapad' :
            komnata = sk[2]
            print('Vi nahoditesi v komnate Goloda -> Tut postoianna net edi v dostatochnom koli'
                  'chestve.')
        elif napr == 'Sever' :
            komnata = sk[6]
            print('Vi nahoditesi v komnate Raboti -> Tut vse kraine utomlonie i ne hoteat nich'
                  'ego delati.')
        elif napr == 'Vostok' :
            komnata = sk[7]
            print('V etom napravlenii net ni odnoi komnati!')
        else :
            print('Takogo napravlenia ne sushestvuet!')


    if komnata == sk[6] :
        napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        while napr not in napravlenia:
            napr = input('Vvedite nazvanie napravlenia v kotorom hotite dvigatsea:')
        if napr == 'Iug' :
            komnata = sk[7]
            print('Vi nahoditesi v komnatе Otdiha -> Tut vse radaostnie i ne o cheom ne'
                  'pekutsea.')
        elif napr == 'Zapad' :
            komnata = sk[1]
            print('Vi nahoditesi v komnate Holoda -> Tut nabliudaiutsea kraine nizkie temeperatu'
                  'ri vozduha.')
        elif napr == 'Sever' or napr == 'Vostok' :
            komnata = sk[6]
            print('Takogo napravlenia ne sushestvuet!')