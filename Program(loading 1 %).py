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

if learningvar == '� ��������� ��� "�������"':
    if dimention=='��������-������������ ����������� �������':
        ASOP.append(puple)
    elif dimention=='����������� ������������':
        AB.append(puple)
    elif dimention=='��������':
        V.append(puple)
    elif dimention=='������� �����':
        OG.append(puple)
    elif dimention=='����������� ��������� ������������':
        ONO.append(puple)
    elif dimention=='����������� ������������ ���������':
        OPP.append(puple)
    elif dimention=='���������������������� ������ ��������� �����':
        PZVS.append(puple)
    elif dimention=='������������� ���':
        PA.append(puple)
    elif dimention=='���������� ������������� �������':
        YBP.append(puple)
    elif dimention=='��������� � �������� ��������':
        CIKZ.append(puple)
####
if S.find(discipline,'��������-������������ ����������� �������')!=-1:
    ASOP.append(puple)
if S.find(discipline,'����������� ������������')!=-1:
    AB.append(puple)
if S.find(discipline,'��������')!=-1:
    V.append(puple)
if S.find(discipline,'������� �����')!=-1:
    OG.append(puple)
if S.find(discipline,'����������� ��������� ������������')!=-1:
    ONO.append(puple)
if S.find(discipline,'����������� ������������ ���������')!=-1:
    OPP.append(puple)
if S.find(discipline,'���������������������� ������ ��������� �����')!=-1:
    PZVS.append(puple)
if S.find(discipline,'������������� ���')!=-1:
    PA.append(puple)
if S.find(discipline,'���������� ������������� �������')!=-1:
    YBP.append(puple)
if S.find(discipline,'��������� � �������� ��������')!=-1:
    CIKZ.append(puple)
