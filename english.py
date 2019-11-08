import re, pronouncing
from gtts import gTTS
import os

poems = '''Poe.txt
Where the Sidewalk Ends.txt
Path Less Taken.txt'''.split("\n")

#print(poems)

def rhyme(rand):
    poem = "\n"
    print()
    f = open("dict/Poems/%s"%(poems[rand.pop()%len(poems)]),"r")
    poe = f.readlines()
    f.close()

    for i in range(len(poe)):
        poe[i] = re.sub('\n', 'X',poe[i])
        poe[i] = re.sub('[^A-Za-z0-9]+', ' ',poe[i])
        poe[i] = re.sub('X', '\n',poe[i])

    poe = ''.join(poe)
    poe = poe.lower()
    poe = re.sub('  ', '',poe)
    poe = poe.split("\n")
    for i in range(len(poe)):
        out = list()
        if i > 0:
            for word in poe[i].split():
                rhymes = pronouncing.rhymes(word)
                if len(rhymes) > 0:
                    out.append(rhymes[rand.pop() % len(rhymes)])
                else:
                    out.append(word)

            print(' '.join(out))
            poem += ' '.join(out)
        else:
            poem += poe[i]
            print(poe[i])

    tts = gTTS(text=poem, lang='en')
    tts.save("poem.mp3")
    os.system("poem.mp3")




