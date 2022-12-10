import wikipediaapi
print('''
		Welcome to the Python Version of the world famous encyclopedia,
					Wikipedia.
	Here instead of going through the hassle of opening up the website and searching
	what you need to search on the internet, Python Wikipedia presents the content of
	Wikipedia on your own local machine. Just run it and type what you need to know, 
				And you're ready to go!
	\n
	''')
text=str(input("What would you like to know about today? : "))
text=text.replace(' ','')
wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

p_wiki = wiki_wiki.page(text)
print(p_wiki.text)

