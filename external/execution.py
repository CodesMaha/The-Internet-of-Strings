''' 
this contains all the interfaces for the sites. 
it will be able to run inputted cmds.
they will correspond to sub cmds in the cmds file

this is the heart of the project, 
it is the implementation of all features
'''

from . import cmds as c # in case a command name is changed, this file will stay error-free
from . import other_saved_data as d # contains username, password a & b, progress

def run_cmd(cmd: list, _all_cmd_info: list[list, list], _all_cmd_names, _all_file_info, _all_saved_file_info: list[list[str, bool, str]]) -> tuple[bool, str]:
    
    package_name = 'external' # script run in working directory outside package, 
    # so package_name from the perspective of ..
    
    cmd = [cmd[0], " ".join(cmd[1:])] 
    # some sub commands are over a word, but commands cannot be like that, unlike open


    def val_return(_error_free = True) -> tuple[bool, str]:
        return (_error_free, d.username)


    def save_files(_all_saved_file_info) -> None:
        with open(f'{package_name}/saved_files.py', 'w') as f:

            from string import ascii_lowercase
            ids = list(ascii_lowercase)
            del ascii_lowercase

            if len(_all_saved_file_info) > len(ids): # 26 as per the alphabet
                _all_saved_file_info = _all_saved_file_info[:(len(ids)+1)]
                print(f'Can only save {len(ids)} files. \nAny more created have been expelled from the system.')

            for index, item in enumerate(_all_saved_file_info):
                f.write(f'file_{ids[index]} = {item}\n')


    def save_to_data() -> None:

        if d.progress == 0:
            d.username = 'User'
            d.password_b = '********'

        with open(f'{package_name}/other_saved_data.py', 'w') as f:
            f.write(
                f"username: str = '{d.username}'\n"
                f"password_a: str = '4PurpleBlueberries'\n"
                f"password_b: str = '{d.password_b}'\n"
                f"real_password_b: str = '3ricaceae5'\n"
                f'progress: int = {d.progress}\n'
            )


    if cmd[0] == c.VISIT_SITE[0]:

        if cmd[1] == c.SEE_POP[0]:
            print(
f'''The top code searched this year is:
{c.VISIT_SITE[0]} {c.SEE_POP[0]}
We are pleased to present this news to you, 
and still believe most of our traffic comes from manufacturers allowing us to shine as the default first site a new user would usually attend.

See other popular codes:
- {c.VIEW_CONTROLS[0]} {c.USERNAME[0]}
- {c.VIEW_CONTROLS[0]} {c.HELP[0]}
- {c.OPEN[0]} filename
- ...'''
            )


        if cmd[1] == c.BLUEBERRY[0]:
            print(
'''Here, we believe blueberries are the best fruit in the world!
Join us on our mission of making blueberries dominate the food market.

To do so, enter in your prescribed password below. 
If you don't have one, email us and we may assess your eligibility.'''
            )

            user_input = input('\nPassword: ').strip()

            if user_input == d.password_a:
                print("\nWe really appreciate your willingness to join in. You'll be emailed about your eligibility soon.")
                if '*' in d.password_b:
                    d.password_b = d.real_password_b # revealed after first passcode
                    save_to_data()

            if user_input == d.password_b:
                print(
"""If you're reading this, it's because you're a new employee and another person at the government decided to give you access to the secret information regarding our secret mission. Do not give anyone else access to this passcode unless you or they are trusted. 

Welcome, we hope you have a good stay during your employment here."""
)
    

    if cmd[0] == c.VIEW_CONTROLS[0]:

        if cmd[1] == c.BOOKMARKS[0]:
            print(
f"""You have no bookmarks saved.

Instead, this note was found:
'I really dislike bookmarking things. 
If I really liked something that much, I would remember its code myself.'"""
            )

        if cmd[1] == c.USERNAME[0]:
            print(f"Your current username is '{d.username}'.")

            _user_input = input('\nWould you like to change it? (y/n): ')
            if _user_input.strip().lower() == 'y':
                d.username = input('What would you like to change it to? : ')

                save_to_data()

                print(f'\nUsername changed to {d.username}.')


        if cmd[1] == c.HELP[0]:

            print('\nAll available commands:')
            for index, item in enumerate(_all_cmd_names[0], 1):
                print(f"{index}. '{item}';")


        if cmd[1] == c.ALL_SAVED_FILES[0]:

            if len(_all_saved_file_info) < 1:
                print('You have no files saved.')
                return val_return(False)

            print('\nAll saved files:')
            for index, item in enumerate(_all_saved_file_info, 1):
                print(f'{index}. "{item[0]};"')


    if cmd[0] == c.DEFINE[0]:
        chosen_list = _all_cmd_info[0]
        chosen_list.extend(_all_cmd_info[1])

        for item in chosen_list:
            if cmd[1] == item[0]:
                print(f"\nDefinition of '{cmd[1]}':\n{item[1]}")
                return val_return() # default param True
        
        print('Could not find inputted command.')
        return val_return(False)


    if cmd[0] == c.OPEN[0]:

        # cmd has two words, sub cmd can have two words
        cmd: list[list[str], list[str, str]] = [[cmd[0]], cmd[1].split(" ", 1)] # [-1] already made wholly string
        cmd[0].extend(cmd[1])
        cmd: list[str, str] = cmd[0]

        for i in range(2):
            chosen_list = _all_file_info if i < 1 else _all_saved_file_info

            for item in chosen_list:
                if cmd[1] == item[0]:
                    
                    if item[1] == False:
                        user_input = input('This file is untrusted by the system.\nWould you still like to open it? (y/n): ')
                        return val_return(False) if user_input.strip().lower() == 'y' else item[1] == True
                    
                    print(f"\nContent of '{item[0]}':\n{item[2]}")

                    if i > 0:
                        user_input = input('\nWould you like to overwrite this file? (y/n): ')
                        if user_input.strip().lower() == 'y':
                            user_input = input('\nNew content:\n')
                            item[2] = user_input

                            save_files(_all_saved_file_info)
                            print('\nFile overwritten; new content saved in system.')
                    return val_return()
            
        print('Could not find file from inputted filename.')


    if cmd[0] == c.DOCUMENT[0]:
        cmd: list[str, str] = [cmd[0], " ".join(cmd[1:])]

        if cmd[1].strip().lower() == 'all':
            print(f"\nCannot name file 'all' as that is a sub-command for deleting all recently saved files.\nWill instead name it '_{cmd[1]}'.")
            cmd[1] = f'_{cmd[1]}'
        
        user_input = input('\nFile content:\n')

        _all_saved_file_info.append([cmd[1], True, user_input])
        save_files(_all_saved_file_info)


    if cmd[0] == c.DELETE[0]:

        if cmd[1].strip().lower() == 'all':

            if len(_all_saved_file_info) < 1:
                print('You have not saved any files.')
                return val_return(False)

            noun: str = f'all {len(_all_saved_file_info)} files' if len(_all_saved_file_info) > 1 else 'the file'
            user_input = input(f'\nThis action will permanently delete {noun} you saved.\nWould you like to proceed? (y/n): ')
        
            if user_input.strip().lower() != 'y':
                return val_return(False)
            
            with open(f'{package_name}/saved_files.py', 'w'):
                pass
            print(f'{noun.capitalize()} deleted.')
            save_files(_all_saved_file_info)
            return val_return()


        for item in _all_saved_file_info:
            if item[0] == cmd[1]:
                user_input = input(f'\nThis action will permanently delete the file "{item[0]}". \nWould you like to proceed? (y/n): ')
                
                if user_input.strip().lower() != 'y':
                    return val_return(False)
                
                _all_saved_file_info.remove(item)
                print(f'The file "{item[0]}" has been deleted.')
                save_files(_all_saved_file_info)
                return val_return()
        
        print('Could not find file from inputted filename.')
        return val_return(False)
    
    
    if d.progress < 1:
        d.progress = 1 # first progress is opening the game and running a cmd, 
        # but running a cmd successfully which is why this is at the end

    return val_return()