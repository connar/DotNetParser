# DotNetParser
This script is written in python and is used to quickly parse a .NET assembly to read its methods and instructions. It's just a quick way to parse and decompile raw bytecode to IL and read the instructions, instead of loading it to a decompiler like DnSpy, ILSpy etc.  
It was just an exercise I did for myself and thought it would be a good tool for anyone looking to parse .NET code this way. So enjoy:D


# Example
Running the tool provides this output, which we can compare with the gui output of DnSpy:  
![image](https://github.com/connar/DotNetParser/assets/87579399/44276ed6-74fe-4115-83b5-5f08f4675727)


Also, the script outputs the instructions of each non empty static method to the corresponding file for further analysis:  
```sh
└─$ cat Main_instructions.txt 
System.Void qCaVAPJGIk.OItkKtykOO::Main(System.String[]) INSTRUCTIONS

IL_0000: ldstr "kernel32.dll"
IL_0005: call System.IntPtr qCaVAPJGIk.OItkKtykOO::LoadLibrary(System.String)
IL_000A: stloc.0
IL_000B: ldloc.0
IL_000C: call System.Text.Encoding System.Text.Encoding::get_UTF8()
IL_0011: ldstr "7Nlzeiulaok36CkiA7cg1PZCx7oWzwew3998xAF7DZY="
IL_0016: call System.Byte[] System.Convert::FromBase64String(System.String)
IL_001B: ldstr "8AOx7b0fGddReqjf+6WzB7n6yOJGvgsGZXvpBa9764w="
IL_0020: call System.Byte[] System.Convert::FromBase64String(System.String)
IL_0025: ldstr "T1D5QuS4MCdJRbPrcYCB/Q=="
IL_002A: call System.Byte[] System.Convert::FromBase64String(System.String)
IL_002F: call System.Byte[] qCaVAPJGIk.OItkKtykOO::GtsGqcLyiX(System.Byte[],System.Byte[],System.Byte[])
IL_0034: callvirt System.String System.Text.Encoding::GetString(System.Byte[])
IL_0039: call System.IntPtr qCaVAPJGIk.OItkKtykOO::GetProcAddress(System.IntPtr,System.String)
IL_003E: stloc.1
IL_003F: ldloc.0
IL_0040: call System.Text.Encoding System.Text.Encoding::get_UTF8()
IL_0045: ldstr "6EcApKsMBv3vWB/3DjNzSZqGNNgYdHg9di7QBebhuwQ="
-- more --
```


# Dependencies
- pythonnet
- ironpython
- dnlib.dll (you can find it this in my Jlaive-Deobfuscator repo)
