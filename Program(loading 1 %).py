ASOP=[]
AB=[]
V=[]
OG=[]
ONO=[]
OPP=[]
PZVS=[]
PA=[]
YBP=[]
CIKZ=[]

TASOP=[]
TAB=[]
TV=[]
TOG=[]
TONO=[]
TPZVS=[]
TPA=[]
TYBP=[]
TCIKZ=[]

if learningvar == 'В помещение АУЦ "Пулково"':
    if dimention=='Аварийно-спасательное обеспечение полетов':
        ASOP.append(puple)
    elif dimention=='Авиационная безопасность':
        AB.append(puple)
    elif dimention=='Водители':
        V.append(puple)
    elif dimention=='Опасные грузы':
        OG.append(puple)
    elif dimention=='Организация наземного обслуживания':
        ONO.append(puple)
    elif dimention=='Организация пассажирских перевозок':
        OPP.append(puple)
    elif dimention=='Противообледенительная защита воздушных судов':
        PZVS.append(puple)
    elif dimention=='Преподаватель АУЦ':
        PA.append(puple)
    elif dimention=='Управление безопасностью полетов':
        YBP.append(puple)
    elif dimention=='Центровка и контроль загрузки':
        CIKZ.append(puple)
####
if S.find(discipline,'Аварийно-спасательное обеспечение полетов')!=-1:
    ASOP.append(puple)
if S.find(discipline,'Авиационная безопасность')!=-1:
    AB.append(puple)
if S.find(discipline,'Водители')!=-1:
    V.append(puple)
if S.find(discipline,'Опасные грузы')!=-1:
    OG.append(puple)
if S.find(discipline,'Организация наземного обслуживания')!=-1:
    ONO.append(puple)
if S.find(discipline,'Организация пассажирских перевозок')!=-1:
    OPP.append(puple)
if S.find(discipline,'Противообледенительная защита воздушных судов')!=-1:
    PZVS.append(puple)
if S.find(discipline,'Преподаватель АУЦ')!=-1:
    PA.append(puple)
if S.find(discipline,'Управление безопасностью полетов')!=-1:
    YBP.append(puple)
if S.find(discipline,'Центровка и контроль загрузки')!=-1:
    CIKZ.append(puple)
