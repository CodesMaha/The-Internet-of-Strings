'''
this module contains all the messages
according to contacts in sub cmds sect in cmds file
'''

from .cmds import MEL, GOOD_SUP, BAD_SUP # instances from module
VIEWER_NAME = 'You'

MEL = MEL[0].capitalize()
GOOD_SUP = GOOD_SUP[0].capitalize()
BAD_SUP = BAD_SUP[0] # name not made lowercase for this reason


MSGS_W_MEL = f"""WEDNESDAY

{MEL}: hahaha what. that literally makes no sense

{VIEWER_NAME}: No, it does not! kay bye I have to go our to get groceries.

{MEL}: ok goodbye. stay safe.

TUESDAY

{MEL}: DUDE DUDE DUDE I just found sth CRAAAAAAZYY

{VIEWER_NAME}: I'm sorry but can it wait? i am really busy atm

{MEL}: Uh yea thats ok. will you come over to mine's today

{VIEWER_NAME}: Sorry no...
{VIEWER_NAME}: I have to work thru the night today

{MEL}: I'm worried about your health.
{MEL}: U HAVE to take a few days off soon.

{VIEWER_NAME}: It's okay, I'm okay!

{MEL}: It's not! come on, i'll treat you to a good dinner

{VIEWER_NAME}: I'll think on it but for now I have to leave urgently okay, love you

{MEL}: fine, love ya

WEDNESDAY

{VIEWER_NAME}: Hi I'm on leave today. Omw to u.

{MEL}: YAY! I've got to show you this thing.
{MEL}: It's a sorta necklace that changes streak col!

{VIEWER_NAME}: What?!

{MEL}: IKR??! COME QUIKC!

SUNDAY

{VIEWER_NAME}: hey thanks for the food! I appreciate it.

{MEL}: Of course!!"""


MSGS_W_GOOD_SUP = f"""TUESDAY

{GOOD_SUP}: Hello Mav. I heard they lost an amulet. Did they tell you about it?

{VIEWER_NAME}: Yes, Sir.

{GOOD_SUP}: Oh, no need to call me that. We should find it before they do. We can study the technology and replicate it easily then. Sound good?

{VIEWER_NAME}: Yes, Ma'am.

{GOOD_SUP}: You know, I couldn't believe it when I was told you weren't the culture hire!

THURSDAY

{GOOD_SUP}: Hi, any updates on that amulet?

{VIEWER_NAME}: Aren't you on leave, too? And, yes, my sister found it.

{GOOD_SUP}: That's awesome! And yes, but I was curious, and I heard my substitute's internet wasn't running well.
{GOOD_SUP}: You just have to tell the team now! Good luck!

{VIEWER_NAME}: Thanks, I appreciate it."""


MSGS_W_BAD_SUP = f"""TUESDAY

{BAD_SUP}: Maveth, we lost a figure of tech. Did you see it?

{VIEWER_NAME}: No, I didn't.

{BAD_SUP}: Ask for an announcement then. We must find it soon.

{VIEWER_NAME}: Sure."""