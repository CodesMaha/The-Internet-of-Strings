''' 
this contains all the interfaces for the sites. 
it will be able to run inputted cmds.
they will correspond to sub cmds in the cmds file

this is the heart of the project, 
it is the implementation of all features
'''

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logging.debug("\n\nHi, I am a message from the `logging` module in the `execution.py` file. \nDon't forget to let my module and I leave once this project is finished!\n")

from . import cmds as c # in case a command name is changed, this file will stay error-free
from . import other_saved_data as d # contains username, password a & b, progress
# from string import ascii_lowercase
# from random import randint

def run_cmd(
    cmd: list[str], 
    _all_cmd_info: list[list[str, str, list | None], tuple[str, str]], 
    _all_file_info: list[str, bool, str], 
    _all_saved_file_info: list[list[str, bool, str]]
    ) -> tuple[bool, str]:

    ''' run any cmd given by the player '''
    
    package_name = 'external' # script run in working directory outside package, 
    # so package_name from the perspective of ..
    
    cmd: list[str, str] = [cmd[0], " ".join(cmd[1:])] 
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

        if d.progress == 0: # # copy paste from default_values
            with open(f'{package_name}/default_values.py', 'r') as f:
                content = f.read()
            with open(f'{package_name}/other_saved_data.py', 'w') as f:
                f.write(content)
            return # do not rewrite file

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
- {c.VISIT_SITE[0]} {c.NEWS[0]}
- {c.VIEW_CONTROLS[0]} {c.HELP[0]}
- {c.OPEN[0]} filename
- {c.MSG[0]} {c.ALL[0]}
- {c.VISIT_SITE[0]} {c.NUM_GUESSING[0]}
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
                from .writings import SECRET_SITE_INFO
                print(SECRET_SITE_INFO)

        
        if cmd[1] == c.NEWS[0]:
            print(
f"""Welcome! \nWe have the world's largest database of articles.

Here is the most popular one of the year so far:

1. All Executions Just STOPPED

Other popular articles:

2. Are People CHANGING STREAKS?
3. ...

Is there a particular article you'd like to read?
Enter in its index down below!"""
            )

            while True:
                user_input = input("\nIndex: ")

                try:
                    user_input = int(user_input)
                    break
                except ValueError: # easier to ask for forgiveness than permission
                    print('\nNon-numeric input detected...')
                    continue

            print('\nYour chosen article:') # TODO: write both articles
            
            if user_input == 1:
                from .writings import ARTICLE_A
                print(
f"""All Executions Just STOPPED\n\n{ARTICLE_A}"""
                )

            elif user_input == 2:
                from .writings import ARTICLE_B
                print(
f"""Are People CHANGING STREAKS?\n\n{ARTICLE_B}"""
                )

            else:
                print("...")

        
        if cmd[1] == c.NUM_GUESSING[0]:
            from random import randint
            random_num = randint(1, 10)

            user_input = input("\nA random integer from one to ten was chosen. \nGuess the number: ")
            if user_input.strip() == str(random_num):
                print(f"\nCorrect, the number was {random_num}.")
            else:
                print(f"\nIncorrect, the number was {random_num}.")


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
            for index, item in enumerate(_all_cmd_info[0], 1):
                print(f"{index}. '{item[0]}';")


        if cmd[1] == c.ALL_SAVED_FILES[0]:

            if len(_all_saved_file_info) < 1:
                print('You have no files saved.')
                return val_return(False)

            print('\nAll saved files:')
            for index, item in enumerate(_all_saved_file_info, 1):
                print(f'{index}. "{item[0]};"')


    if cmd[0] == c.DEFINE[0]:
        # connect both lists in list so that
        # both cmds and sub cmds can be checked at once
        chosen_list = _all_cmd_info[0]
        chosen_list.extend(_all_cmd_info[1])

        for item in chosen_list:
            if cmd[1] == item[0]:
                print(f"\nDefinition of '{cmd[1]}':\n{item[1]}")
                return val_return() # default param True
        
        print('Could not find inputted command.')
        return val_return(False)


    if cmd[0] == c.OPEN[0]:

        # cmd has two words, sub cmd can have over two words
        cmd: list[str, str] = [cmd[0], " ".join(cmd[1].split(" "))] # [-1] already made wholly string

        for i in range(2): # done twice, once for files and other for _all_saved_file_info
            chosen_list = _all_file_info if i < 1 else _all_saved_file_info

            for item in chosen_list: # if saved_files list is empty, loop will not run
                if cmd[1] != item[0]:
                    continue
                    
                if item[1] == False:
                    user_input = input('This file is untrusted by the system.\nWould you still like to open it? (y/n): ')
                    return val_return(False) if user_input.strip().lower() == 'y' else item[1] == True
                    # when bool becomes true, the if statement gets passed before the return is carried out
                
                print(f"\nContent of '{item[0]}':\n{item[2]}") # display content and name

                if i < 1: # would not like to overwrite preexisting story file
                    return val_return() 
                
                user_input = input('\nWould you like to overwrite this file? (y/n): ')
                if user_input.strip().lower() != 'y': # if overwriting newly saved file
                    return val_return()
                user_input = input('\nNew content:\n')
                item[2] = user_input

                save_files(_all_saved_file_info)
                print('\nFile overwritten; new content saved in system.')
                return val_return()
            
        print('Could not find file from inputted filename.')


    if cmd[0] == c.DOCUMENT[0]:

        _all_file_names = [filename[0] for filename in _all_file_info] 
        # player saved files and files should not have identical names;
        # whichever one is checked for first will open instead of the actual one the player intended.

        if len(_all_saved_file_info) > 0:
            _all_saved_file_names = [filename[0] for filename in _all_saved_file_names]
            # same except there is a chance there are no files in saved_files

        if cmd[1] == c.ALL[0]:
            print(f"\nCannot name file 'all' as that is a sub-command for deleting all recently saved files.\nWill instead name it '_{cmd[1]}'.")
            cmd[1] = f'_{cmd[1]}'

        elif cmd[1] in _all_file_names: # check for identical names with preexisting default system files
            print(f"\nCannot name file '{cmd[1]}' as that is the name of an older file in the system.\nWill instead name it '_{cmd[1]}'.")
            cmd[1] = f'_{cmd[1]}'
        
        user_input = input('\nFile content:\n')

        _all_saved_file_info.append([cmd[1], True, user_input])
        save_files(_all_saved_file_info)
        print('File saved in system.')


    if cmd[0] == c.DELETE[0]:

        if cmd[1].strip().lower() == c.ALL[0]:

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
    

    if cmd[0] == c.MSG[0]:

        if cmd[1] == c.ALL[0]:
            print('\nYour saved contacts: ')
            for index, name in enumerate(c.MSG[2][1:], 1):
                print(f'{index}. "{name[0].lower()}";') # all arg should always come first
            return val_return()

        if cmd[1] == c.MEL[0]:
            from .writings import MSGS_W_MEL as CHOSEN_MSGS

        elif cmd[1] == c.BAD_SUP[0].lower(): # AFD is uppercase in cmds module
            from .writings import MSGS_W_BAD_SUP as CHOSEN_MSGS

        elif cmd[1] == c.GOOD_SUP[0]:
            from .writings import MSGS_W_GOOD_SUP as CHOSEN_MSGS

        elif cmd[1] == c.NYOKA[0]:
            from .writings import MSGS_W_NYOKA as CHOSEN_MSGS

        else:
            print(f'Could not find {cmd[1]} in contacts.')
            return val_return(False)
        
        print("\n" + CHOSEN_MSGS)
    

    if d.progress < 1:
        d.progress = 1 # first progress is opening the game and running a cmd, 
        # but running a cmd successfully which is why this is at the end

    return val_return()