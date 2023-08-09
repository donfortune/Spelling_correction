from textblob import TextBlob, Word

text = 'commmittte'
blob = TextBlob(text)
print(blob.correct())

