'''
this module contains all the messages
according to contacts in sub cmds sect in cmds file
'''

from .cmds import MEL, GOOD_SUP, BAD_SUP, NYOKA, MAL_FRIEND # instances from module
VIEWER_NAME = 'You'

MEL = MEL[0].capitalize()
GOOD_SUP = GOOD_SUP[0].capitalize()
NYOKA = NYOKA[0].capitalize()
BAD_SUP = BAD_SUP[0] # name not made lowercase for this reason
MAL_FRIEND = MAL_FRIEND[0]


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

{VIEWER_NAME}: Hi Mel I'm on leave today. Omw to u.

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

{VIEWER_NAME}: Sure.

WEDNESDAY

{BAD_SUP}: There's been some random changing of the execution database. Who do you think it is?

{VIEWER_NAME}: I'm on break...

{BAD_SUP}: I don't care. I need answers now.

{VIEWER_NAME}: I really cannot answer you right now. Ask the team to create a file named "`db changes`" for the documenting of any major changes. I can take a look at this issue once I'm back from my leave.

{BAD_SUP}: Fine!"""


MSGS_W_NYOKA = f"""FRIDAY

{NYOKA}: I named you Maveth for a Reason after your mother named your elder sister, a female firstborn, by herself.
{NYOKA}: I'm warning you... Don't ever text or vizit me again."""


MSGS_W_MAL_FRIEND = f'''WEDNESDAY

{MAL_FRIEND}: Hey Mav, I have sth to tell u...

THURSDAY

{VIEWER_NAME}: Hi Mal. sorry, I was hanging out with my sister.
{VIEWER_NAME}: what is it?

{MAL_FRIEND}: My pet ferret passed, your dad's car was involved...

{VIEWER_NAME}: .
{VIEWER_NAME}: I have no words... could we hop on a call for this?

{MAL_FRIEND}: Sure and neither do i'''


ARTICLE_A = """Almost all people with warmer toned streaks disappear. That phenomenon is as old as time. Yet, recently, no unnatural deaths have occurred concerning such people! For liberals such as myself, this is awesome news.

However, many traditionalists find this situation to be unfortunate. 

True story: I saw an old lady bawling her eyes out yesternight at the train station, and when I approached her and asked if she was okay, she responded with "A warm dude just stole my purse! If he had passed before, this wouldn't've happend." At the same time, I could clearly see her purse right beside her, because she was literally clutching it with more strength than I could ever possibly expend myself.

The crowd's been pressuring the government to give us answers — though none have been publicised thus far. I, for one, will be rooting for this all to stay this way for as long as possible."""


ARTICLE_B = """People with similarly coloured streaks have been staying together in groups. For cooler tones, this is due to a sense of superiority, and for warmer tones, this is so they can stick around for each other.

However, reports have been going around saying people with similar faces but dissimilar streaks have been going around pretending to be part of these groups. For whatever reason, if the group they're going in consists of warmer tones, then it becomes a guarantee for at least a few group members to disappear the very next day.

Some sources have even been claiming these are government spies looking for victims to execute, and that there is some sort of "TDA" responsible for this. However, while these theories have been circulating for decades, they have never gotten any solid evidence to support them.

It seems these sorts of people will never stop with their conspiracy theories. Regardless of who is responsible for any executions, these freaks certainly deserve whatever comes to them."""


SECRET_SITE_INFO = """If you're reading this, it's because you're a new employee and another person at the government decided to give you access to the below information regarding our secret mission. Do not give anyone else access to this passcode unless you or they are trusted. 

Welcome, we hope you have a good stay during your employment here.

You must already know very well that those with warmer tone streaks on the back of their hands are inferior to those with cooler tone streaks. The specific government segment that is in charge of the executions of such people is named 'The Agency For Democide' or the 'AFD'.

Employees of the democide agency can have multiple roles; they can be in charge of editing the database of targets, locating targets, or hunting down targets. They may also be responsible for any related technology or infrastructure.

To disguise as a person with a streak of a specifc colour, we have invented a yet to be released to the public technology that changes the colour of said streaks for the aforementioned goal. Unfortunately, we have lost an amulet from our warehouse, which can be detrimental to the secrecy of our mission. If you find it, do return it to us for you will be rewarded handsomely.

The room these employees work in is under the number 239, next to the laboratory for the creation of sedating drugs."""