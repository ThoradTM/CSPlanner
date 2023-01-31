from methods.webscraper import fetch_data

username = input("What is your username?")
password = input("What is your password?")

text = fetch_data(username, password)

print(text)
