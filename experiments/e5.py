import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)
