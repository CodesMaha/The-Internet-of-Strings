''' '
this module contains all terminal commands made for this program.
it has two parts, commands and sub commands.
'''

        # sub cmds
                # sites
SEE_POP = ('www.pin-it.com', "A site that contains others sites pinned by experts. This is especially useful for those new here.")
BLUEBERRY = ('www.blueberries.gov', "A site about blueberries, and potentially even something more malicious.")
NEWS = ('www.informatioed.com', "A site which presents news.")
NUM_GUESSING = ('www.numberguessinggame.fun', "A site in which the viewer guesses a random number.")

                # not sites
BOOKMARKS = ('bookmarks', "Bookmarked sites.")
USERNAME = ('username', "Name set by the user. Default value for it is 'User'.")
HELP = ('help', "A control which will return a list of all codes.")
ALL_SAVED_FILES = ('saved files', "Newly saved files.")
ALL = ('all', "An argument passed to indicate a given command should affect all relevant information.")

                # contacts
MEL = ('melissa', "A saved contact and the only other live member in Maveth's immediate family.")
BAD_SUP = ('AFD supervisor', "A saved contact and Maveth's supervisor while he was undercover as an employee at the AFD.") # name should be made lowercase when used
GOOD_SUP = ('real supervisor', "A saved contact and Maveth's actual supervisor at the organization he actually works at.") # sup meaning supervisor
NYOKA = ('father', "A saved contact and Maveth Nyokason's father, Nyoka.")

        # cmds
# cmd name in code: list[str, str, list | None] 
# = ['user_input to activate cmd, checked before execution', "description of cmd for DEFINE", [what sub cmds the cmd accepts] | None if exceptions as handled in execution]
VISIT_SITE = ['visit', "A command used to visit any one site. Specify a site after inserting this command and the system will try to load the site.", [SEE_POP]]
VIEW_CONTROLS = ['view', "A command to view a setting.", [BOOKMARKS, USERNAME, HELP, ALL_SAVED_FILES]]
DEFINE = ['define', "A command used to define any given code.", None] # will accept anything as second arg
OPEN = ['open', "A command that will open a specified file on the computer.", None] # will accept the name of any known file
DOCUMENT = ['document', "A command that can save new information on the system in the form of a textual document.", None] # will accept anything other than all and default files
DELETE = ['delete', "A command that permanently deletes newly saved files.", [None, ALL]] # will accept filenames from saved files
MSG = ['message', "A command used to view the previous messages sent to a particular contact before a specific date.", [ALL, MEL, GOOD_SUP, BAD_SUP, NYOKA]] # takes all contacts as args, and all
EXIT = ['exit', "A command used to exit the application within the application.", None] # takes no sub cmd args, handled before execution