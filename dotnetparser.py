from os.path import realpath, dirname, join
import sys

import clr
from System.Reflection import Assembly

current_directory = dirname(realpath(__file__))
dnlib_ = join(current_directory, "../dnlib-4.4.0/src/bin/Debug/net45/dnlib.dll")
clr.AddReference(dnlib_)
import dnlib


def find_methods(module):
	methods = []
	for t in module.Types:
		for m in t.Methods:
			print(f"Found method: {m.Name}")
			methods.append(m)

	print()
	return methods

def parse_dotnet(absolute_path_of_assembly):
    # Path to your .NET executable
    exe_path = absolute_path_of_assembly

    # Load the .NET executable using dnlib
    try:
        module = dnlib.DotNet.ModuleDefMD.Load(exe_path)
    except Exception as e:
        print(f"Error loading module: {e}")
        return

    # Find the Main method
    methods = find_methods(module)
    if len(methods) > 0:
    	for m in methods:
    		print(m.FullName)
    		if m.IsStatic and m.HasBody:
    			print(f"{m.Name} has a body and is static. Writting instructions to {m.Name}_instructions.txt\n")
    			with open(f"./{m.Name}_instructions.txt","w") as f:
    				f.write(f"{m.FullName} INSTRUCTIONS\n\n")
    				for instr in m.Body.Instructions:
    					f.write(str(instr)+"\n")
    			f.close()
    		else:
    			print(f"{m.Name} does not have a body. It's probably a winapi func.\n")



def main():

    if len(sys.argv) != 2:
        # If no filename is provided or if more than one argument is given
        print("Usage: python unjlaive.py [obfuscated.bat]")
        return

    # Example usage:
    filename = sys.argv[1]
    parse_dotnet(filename)


if __name__ == "__main__":
    main()
