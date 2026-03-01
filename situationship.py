# 💌 Situationship Decoder
print('Welcome to my Situationship Decoder')
name = input('Hey whats your name?')
print(f'Hi {name}, I am here to help you decode your situationship!')
print('Please answer the following questions!')

#PICKING GENDER
gender = input('Are you a boy or a girl?').lower()
if gender == 'girl':
    print('Great! Let\'s get started!')
elif gender == 'boy':
    print('Great! Let\'s get started!')
else:
    print('I am sorry, I do not support other genders at this time.')

#SCOREBOARD
score = 0

#PICKING QUESTIONS FOR GIRLS
if gender == 'girl':
    print('Question one, does he initiate consistently? For example, does he text multiple times a week, start convos without reason, asks questions?')
    q1 = input('Type yes or no').lower()
    if q1 == 'yes':
        score += 1.5
    elif q1 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does he increase proximity? For example, does he sit closer, stand near you, lean in when you talk?')
    q2 = input('Type yes or no').lower()
    if q2 == 'yes':
        score += 1
    elif q2 == 'no':
        score -= 1  
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does he mirror you? For example, does he match your tone, copy your phrases, laughing when you laugh, similar body language?')
    q3 = input('Type yes or no').lower()
    if q3 == 'yes':
        score += 1
    elif q3 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does he remember small details? For example, does he bring up something you mentioned last week, notices changes in you?')
    q4 = input('Type yes or no').lower()
    if q4 == 'yes':
        score += 1
    elif q4 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does he prioritize you when busy? For example, does he respond when busy, reschedules if he cancels, make time for you, not just find time?')
    q5 = input('Type yes or no').lower()
    if q5 == 'yes':
        score += 1.5
    elif q5 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does he integrate you into his life? For example, does he introduce you to friends, family, include you in plans?')
    q6 = input('Type yes or no').lower()
    if q6 == 'yes':
        score += 1.5
    elif q6 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does he plan ahead with you? For example, \"we should go next week\", mentions events months away, talks about things you\'ll do together?')
    q7 = input('Type yes or no').lower()
    if q7 == 'yes':
        score += 1.5
    elif q7 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does he show protective behavior? For example, does he walk on the street side, checks if you got home, steps in if someone disrespects you?')
    q8 = input('Type yes or no').lower()
    if q8 == 'yes':
        score += 1
    elif q8 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does he get slightly nervous? For example fidgeting, voice changes, playful teasing, slight awkwardness?')
    q9 = input('Type yes or no').lower()
    if q9 == 'yes':
        score += 1
    elif q9 == 'no':
        score -=1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does his behavior stay consistent over time? Biggest one, anyone can act intrested for a week. There has to be consistent behavior across multiple WEEEKS.')
    q10 = input('Type yes or no').lower()
    if q10 == 'yes':
        score += 2
    elif q10 == 'no':
        score -=2
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 2
    #SCOREBOARD:
    if score >= 9:
        print(f'{name}, pretty strong genuine interest! He is likely into you, but of course, there are no guarantees in life. Just be mindful of red flags and trust your gut.')
    elif score >= 4.5:
        print(f'{name}, there are some signs of interest, but it is not super strong. He may be into you, but it is also possible he just enjoys your company. I would say keep an eye out for red flags and trust your gut.')
    elif score >= 0.5:
        print(f'{name}, it\’s kind of unclear. There are mixed signals, and he might like you a little, but it could also just be convenience or attention. I would stay observant and not overinvest yet.')
    elif score >= -6:
         print(f'{name}, the investment looks low. He may enjoy talking to you, but the effort is not strong enough to show real intention. Protect your energy.')

    else:
        print(f'{name}, this looks more like convenience than genuine interest. The effort and consistency just are not there. You deserve someone who is sure about you.')

#PICKING QUESTIONS FOR GUYS
if gender == 'boy':
    print('Is she consistent with you over time? For example does she stay warm, not hot-and-cold? Does she keep responding with similar energy week after week?')
    q1 = input('Type yes or no').lower()
    if q1 == 'yes':
        score += 2
    elif q1 == 'no':
        score -= 2
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 2
    print('Does she initiate sometimes? For example, texts first occasionally, sends random things that remind her of you?')
    q2 = input('Type yes or no').lower()
    if q2 == 'yes':
        score += 1.5
    elif q2 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does she priotitize responding to you? For example, replies when busy, doesn\'t leave you on delievered for days?')
    q3 = input('Type yes or no').lower()
    if q3 == 'yes':
        score += 1.5
    elif q3 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does she ask personal questions about you? For example, your goals, your family, your opinions?')
    q4 = input('Type yes or no').lower()
    if q4 == 'yes':
        score += 1.5
    elif q4 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does she try to look good around you specifically? For example, fixes her hair, adjusts her outfit, puts in noticeable effort?')
    q5 = input('Type yes or no').lower()
    if q5 == 'yes':
        score += 1.5
    elif q5 == 'no':
        score -= 1.5
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1.5
    print('Does she laugh at yout jokes more than others?')
    q6 = input('Type yes or no').lower()
    if q6 == 'yes':
        score += 1
    elif q6 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does she remember small things about you? For example, does she bring up something you mentioned last week, notices changes in you?')
    q7 = input('Type yes or no').lower()
    if q7 == 'yes':
        score += 1
    elif q7 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does she get slightly shy or softer around you? For example, slight blush, quieter voice, playful teasing, slight awkwardness?')
    q8 = input('Type yes or no').lower()
    if q8 == 'yes':
        score += 1
    elif q8 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does she include you in her social world? For example, introduces you to friends, family, includes you in plans?')
    q9 = input('Type yes or no').lower()
    if q9 == 'yes':
        score += 1
    elif q9 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    print('Does she get a little jealous? For example, asks about other girls, seems bothered when you talk about other girls?')
    q10 = input('Type yes or no').lower()
    if q10 == 'yes':
        score += 1
    elif q10 == 'no':
        score -= 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        score -= 1
    #SCOREBOARD:
    if score >= 9:
        print(f'{name}, pretty strong genuine interest! She is likely into you, but of course, there are no guarantees in life. Just be mindful of red flags and trust your gut.')
    elif score >= 4.5:
        print(f'{name}, there are some signs of interest, but it is not super strong. She may be into you, but it is also possible she just enjoys your company. I would say keep an eye out for red flags and trust your gut.')
    elif score >= 0.5:
        print(f'{name}, it\’s kind of unclear. There are mixed signals, and she might like you a little, but it could also just be convenience or attention. I would stay observant and not overinvest yet.')
    elif score >= -6:
         print(f'{name}, the investment looks low. She may enjoy talking to you, but the effort is not strong enough to show real intention. Protect your energy.')

    else:
        print(f'{name}, this looks more like convenience than genuine interest. The effort and consistency just are not there. You deserve someone who is sure about you.')

    