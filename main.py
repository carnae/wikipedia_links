import random
from mediawiki import MediaWiki
wikipedia = MediaWiki(user_agent='WikiRandomBot')
Arr = []
End = ''
while End != ("yes"):
    search = input("enter title")
    results = int(input("number of results"))
    Arr = wikipedia.search(search, results)
    print(Arr)
    decision = input("next?")
    if decision == ("s"):
        continue
    elif decision == ("a"):
        article = int(input("enter number")) - 1
        chars = int(input("words?"))
        p = wikipedia.page(Arr[article])
        print(p.summarize(chars))
        view = input("next?")
        if view == "l":
            Arr = p.links
            print(Arr)
        elif view == ("m"):
            print(p.summarize())







