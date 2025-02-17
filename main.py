# import statements
from external import cmds, files, saved_files
from external.execution import run_cmd
from external.other_saved_data import username, progress
# from external.files import most_sentimental

from platform import system
curr_sys = system()
del system

from sys import exit

app_name = 'The Internet of Strings'

all_cmd_info: list[list[list], list[tuple]] = [[], []]
for attr in [attr for attr in dir(cmds) if ('__' not in attr) and (attr.isupper())]:
    attr = getattr(cmds, attr)
    if isinstance(attr, list): # check if cmd or sub cmd
        all_cmd_info[0].append(attr) # cmd
    if isinstance(attr, tuple):
        all_cmd_info[1].append(attr) # sub cmd
del attr

# retrieve names of cmds, which is first time of each,
# excluding sub cmds since they are not checked for
all_cmd_names: list[str] = [attr[0] for attr in all_cmd_info[0]]

# retrieve data from files module
all_file_info = [getattr(files, attr) for attr in dir(files) if ('__' not in attr)]
all_file_names = [attr[0] for attr in all_file_info]

# retrieve data from player saved files
all_saved_file_info = [getattr(saved_files, attr) for attr in dir(saved_files) if ('__' not in attr)]

# change the tab name of cmd prompt
match curr_sys:
    case 'Windows':
        from os import system
        system(f'title {app_name}')
        del system

    case 'Linux' | 'Darwin': # for cross platform compatibility
        from sys import stdout
        stdout.write(f"\033]0;{app_name}\007")
        stdout.flush()
        del stdout

    case _: # any other system does not get this privilege
        pass

# intro
print(f"Welcome, {username}! \nFeel free to input the command '{cmds.VISIT_SITE[0]} {cmds.SEE_POP[0]}' if you're just starting out.")
if progress == 0: # i knew this var would have a use heheheh
    from external.files import most_sentimental
    print(f"\nAdditionally, the previously unsaved changes of 2 characters in the file '{most_sentimental[0]}' were saved before exit.") # TODO: check grammatical
    del most_sentimental

def ask_user() -> list:
    if_invalid = lambda inputted: f'"{inputted}" is unrecognised code.' # to maintain consistency
    valid = False

    while valid is False:
        user_input: str = input('\n> ').strip().lower()

        if user_input == cmds.EXIT[0]:
            print('Exiting...')
            exit()

        if ' ' in user_input:
            user_input = user_input.split(' ')
        else:
            print(if_invalid(''.join(user_input)))
            continue
        
        if not (user_input[0] in all_cmd_names): 
            # cmds like define can accept both cmds and sub cmds,
            # so sub cmds are not checked for in this input sanitization
            print(if_invalid(' '.join(user_input)))
            continue

        valid = True

    return user_input # list

while True:
    error_free, username = run_cmd(ask_user(), all_cmd_info, all_file_info, all_saved_file_info)
    print(f'\nCode executed. {error_free = }')