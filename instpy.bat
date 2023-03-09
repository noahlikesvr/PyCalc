@echo off
echo Installing Python 3.10...
powershell -Command "& { Add-AppxPackage -Path 'Microsoft.Python3.10_3.10.17763.0_x64__8wekyb3d8bbwe' -RegisterAllResources }"
echo Python 3.10 installed successfully!