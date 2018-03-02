import eyeD3
tag = eyeD3.Tag()

userInput = raw_input("Enter directory")

tag.link(userInput)
print tag.getArtist()
print tag.getAlbum()
print tag.getTitle()
