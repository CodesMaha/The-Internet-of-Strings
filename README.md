# The Internet of Strings
Project in progress, so is the `README.md` file. Would not recommend building an application with current code.

## Building the application anyway
**Note**: This is a rough guide, primarily geared towards Windows. The process may not be exactly like this.
- Click on `Code` and then `Download ZIP` on GitHub.
- Extract the folder in File Explorer.
- Move the folder inside the folder of the same name outside back into downloads.
- Open command prompt, or terminal for Darwin — MacOs — and Linux.
- Enter in the following commands in order:
    + `pip install pyinstaller`, could be `pip3` instead for Linux and Darwin.
    + `cd C:\Downloads\The-Internet-of-Strings-main` for Windows, or `cd ~/Downloads/The-Internet-of-Strings-main` for Linux and Darwin. This is an example directory, do modify the directory in case this isn't it.
    + Try opening command prompt in administrator mode if the below command doesn't work.
    + `pyinstaller main.py --onefile`
- Move the `main.exe` file into the directory of your local `README.md` file, 
- and optionally delete both the `dist` and `build` folders.
- This project has no dependencies that are not already covered by the `builtins` library. You may need to install or update some packages for that on Darwin or Linux, though.
- `pip uninstall pyinstaller` — to free up space in case you don't want to do this again for a while.

---

**Start of development**: December 19, 2024, 11 A.M. UTC.  
**Creation of public repository**: January 15, 2025, 10 P.M. UTC.