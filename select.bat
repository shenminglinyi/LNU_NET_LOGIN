@echo off
chcp 65001 > nul  REM �����ַ�����ΪUTF-8
cls

:menu
color 0A
echo ================================
color 0A
echo У԰����¼��ע���˵�
color 0B
echo ================================
color 0B
echo 1. ��¼У԰��
color 0C
echo 2. ע��У԰��
color 0E
echo 3. ��ѯ���
color 0D
echo 4. ����ѡ��
color 0C
echo 5. ����
color 0A
echo 6. �˳�
color 0A
echo ================================
set /p choice=��ѡ����� (1/2/3/4/5/6):

if "%choice%"=="" goto menu

if %choice%==1 (
    python bind.py
    goto menu
) else if %choice%==2 (
    python unbind.py
    goto menu
) else if %choice%==3 (
    cls
    goto chamenu
) else if %choice%==4 (
    cls
    goto setconfig
) else if %choice%==5 (
    cls
    goto guan
) else if %choice%==6 (
    exit
)else (
    echo ��Ч��ѡ��������ѡ��
    goto menu
)

:chamenu
color 0A
echo ================================
echo ��ѯ���
echo ================================

echo 1. ��������
color 0C
echo 2. ��������
color 0E
echo 3. ������ҳ��
color 0A
set /p choice=��ѡ����� (1/2/3):

if %choice%=="" (
    goto chamenu
) else if %choice%==1 (
    python -c "import GetRes;GetRes.yi()"
    goto chamenu
) else if %choice%==2 (
    python -c "import GetRes;GetRes.ke()"
    goto chamenu
) else if %choice%==3 (
    cls
    goto menu
) else (
    echo ��Ч��ѡ��������ѡ��
    goto chamenu
)

:setconfig
color 0A
echo ================================
echo ����ѡ��
echo ================================

python config.py
rem ���µ�Cookieֵд���ļ�����������������Թ�����ʹ��

pause
goto menu

:guan
color 0A
echo ================================
echo ����
echo ================================
echo http://gatesrv.lnu.edu.cn/
echo ���ߣ�21��xxx
pause
goto menu
