print('''Enter the choice for text analysis \n 
        Enter 1 for removing puncuation
        Enter 2 for converting text into uppercase
        Enter 3 to remove new line
        Enter 4 to remove extra space
        Enter 5 to remove no
''')
try:
    user_choice = int(input("\nEnter the choice no : "))
except:
    pass

if user_choice == 1:
        with open("file.txt") as file: 
            djtext = file.read()    
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}


if(user_choice == 2):
    with open("file.txt") as file: 
        djtext = file.read()
    analyzed = ""
    for char in djtext:
        analyzed = analyzed + char.upper()

    params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
    djtext = analyzed

if(user_choice == 3):
    with open("file.txt") as file: 
        djtext = file.read()
    analyzed = ""
    for index, char in enumerate(djtext):
        # It is for if a extraspace is in the last of the string
        if char == djtext[-1]:
                if not(djtext[index] == " "):
                    analyzed = analyzed + char

        elif not(djtext[index] == " " and djtext[index+1]==" "):                        
            analyzed = analyzed + char

    params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    djtext = analyzed

if (user_choice == 4):
    with open("file.txt") as file: 
        djtext = file.read()
    analyzed = ""
    for char in djtext:
        if char != "\n" and char!="\r":
            analyzed = analyzed + char

    params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}


if (user_choice == 5):
    with open("file.txt") as file: 
        djtext = file.read()
    analyzed = ""
    numbers = '0123456789'

    for char in djtext:
        if char not in numbers:
            analyzed = analyzed + char
    
    params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    djtext = analyzed