# import statements
from external import cmds, files, saved_files
from external.execution import run_cmd
from external.other_saved_data import username

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

# retrieve names of cmds, which is first time of each
all_cmd_names: list[list[str], list[str]] = [[], []]
all_cmd_names[0] = [attr[0] for attr in all_cmd_info[0]] # cmd
all_cmd_names[1] = [attr[0] for attr in all_cmd_info[1]] # sub cmd

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

    case 'Linux' | 'Darwin':
        from sys import stdout
        stdout.write(f"\033]0;{app_name}\007")
        stdout.flush()
        del stdout

    case _:
        pass

# intro
print(f"Welcome, {username}! \nFeel free to input the command '{cmds.VISIT_SITE[0]} {cmds.SEE_POP[0]}' if you're just starting out.")

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
        
        if not (user_input[0] in all_cmd_names[0]): # cmds like define can accept both cmds and sub cmds
            print(if_invalid(' '.join(user_input)))
            continue

        valid = True

    return user_input # list

while True:
    error_free, username = run_cmd(ask_user(), all_cmd_info, all_cmd_names, all_file_info, all_saved_file_info)
    print(f'\nCode executed. {error_free = }')