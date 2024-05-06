@echo off
chcp 65001 > nul  REM 设置字符编码为UTF-8
cls

:menu
color 0A
echo ================================
color 0A
echo 校园网登录和注销菜单
color 0B
echo ================================
color 0B
echo 1. 登录校园网
color 0C
echo 2. 注销校园网
color 0E
echo 3. 查询余额
color 0D
echo 4. 配置选项
color 0C
echo 5. 关于
color 0A
echo 6. 退出
color 0A
echo ================================
set /p choice=请选择操作 (1/2/3/4/5/6):

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
    echo 无效的选择，请重新选择。
    goto menu
)

:chamenu
color 0A
echo ================================
echo 查询余额
echo ================================

echo 1. 已用流量
color 0C
echo 2. 可用流量
color 0E
echo 3. 返回主页面
color 0A
set /p choice=请选择操作 (1/2/3):

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
    echo 无效的选择，请重新选择。
    goto chamenu
)

:setconfig
color 0A
echo ================================
echo 配置选项
echo ================================

python config.py
rem 将新的Cookie值写入文件或进行其他操作，以供后续使用

pause
goto menu

:guan
color 0A
echo ================================
echo 关于
echo ================================
echo http://gatesrv.lnu.edu.cn/
echo 作者：21级xxx
pause
goto menu
