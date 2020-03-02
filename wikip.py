import wikipedia
wikipedia.set_lang("hi")
wikipe=input("question here => ")
answer=(wikipedia.summary(wikipe))
print(answer)
