Set WshShell = CreateObject("WScript.Shell")
exePath = "C:\Users\havy1\OneDrive\Desktop\Project\WuysMacro\dist\BladeBall_Console_20260121_0229.exe"
WshShell.Run Chr(34) & exePath & Chr(34), 2 ' 2 = Minimized
Set WshShell = Nothing
