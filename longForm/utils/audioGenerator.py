import pyttsx3
import random

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


def soundifyAuthor(title, asker):
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 200)
    if len(voices) > 1:
        voice_index = random.randrange(0, len(voices))  # Choose a random voice index
    else:
        voice_index = 0  # Default to the first voice if only one is available

    engine.setProperty('voice', voices[voice_index].id)
    engine.save_to_file(title, asker+"/temp"+"0"+".mp3")
    engine.runAndWait()



def soundifyComment(comment, index, sectionid, asker):
    
    engine.setProperty('rate', 200)
    swears = ["fuck", "shit"]

    comment = comment.split()

    for word in comment:
        if word in swears:
            print("yikes")

    comment =' '.join(comment)
    
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 200)
    sectionid = str(sectionid)

    if len(sectionid) < 2:
        sectionid = "0" + sectionid

    engine.save_to_file(comment, asker+"/temp"+str(index)+"_"+str(sectionid)+".mp3")
    engine.runAndWait()


