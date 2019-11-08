import pronouncing
from gtts import gTTS
import os

words = {}
files = {
"dict/adjectives/1syllableadjectives.txt" : "adj1",
"dict/adjectives/28K adjectives.txt" : "adj",
"dict/adjectives/2syllableadjectives.txt" : "adj2",
"dict/adjectives/3syllableadjectives.txt" : "adj3",
"dict/adjectives/4syllableadjectives.txt" : "adj4",
"dict/adverbs/1syllableadverbs.txt" : "adv1",
"dict/adverbs/2syllableadverbs.txt" : "adv2",
"dict/adverbs/3syllableadverbs.txt" : "adv3",
"dict/adverbs/4syllableadverbs.txt" : "adv4",
"dict/adverbs/6K adverbs.txt" : "adv",
"dict/nouns/1syllablenouns.txt" : "n1",
"dict/nouns/2syllablenouns.txt" : "n2",
"dict/nouns/3syllablenouns.txt" : "n3",
"dict/nouns/4syllablenouns.txt" : "n4",
"dict/nouns/91K nouns.txt" : "n",
"dict/verbs/1syllableverbs.txt" : "v1",
"dict/verbs/2syllableverbs.txt" : "v2",
"dict/verbs/31K verbs.txt" : "v",
"dict/verbs/3syllableverbs.txt" : "v3",
"dict/verbs/4syllableverbs.txt" : "v4"
}

DEBUG = False

for file in files.keys():
    f = open(file,"r")
    words[files[file]] = (''.join(f.readlines())).split("\n")
    f.close()

types = ["adj","adv","n","v"]

for type in types:
    for i in range(1,5):
        t = type + str(i)
        for word in words[t]:
            try:
                pronunciation_list = pronouncing.phones_for_word(word)
                syl = pronouncing.syllable_count(pronunciation_list[0])
                if syl != i:
                    #print(syl, i, word)
                    words[t].remove(word)
            except:
                #print(word, "not in pronouc")
                words[t].remove(word)


def haiku(rand):
    for n in range(3):
        poem = "\n"
        #line 1
        syllables = 0
        r = rand.pop()%(3-syllables) +1
        syllables += r
        poem += words["n%s"%r][rand.pop() % len(words["n%s"%r])] + ' '
        if DEBUG: print(syllables, end=' ')
        r = rand.pop()%(4-syllables) +1
        syllables += r
        poem += words["v%s"%r][rand.pop() % len(words["v%s"%r])] + ' '
        if DEBUG: print(syllables, end=' ')
        r = 5-syllables
        syllables += r
        poem += words["adv%s"%r][rand.pop() % len(words["adv%s"%r])] + ' '
        #print(words["adv%s"%r][rand.pop() % len(words["adv%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        #print()
        poem += "\n"
        #line 2
        syllables = 0
        r = rand.pop()%(4-syllables) +1
        syllables += r
        poem += words["adj%s"%r][rand.pop() % len(words["adj%s"%r])] + ' '
        #print(words["adj%s"%r][rand.pop() % len(words["adj%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        r = rand.pop()%(5-syllables) +1
        syllables += r
        poem += words["n%s"%r][rand.pop() % len(words["n%s"%r])] + ' '
        #print(words["n%s"%r][rand.pop() % len(words["n%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        r = rand.pop()%(6-syllables) +1
        syllables += r
        poem += words["v%s"%r][rand.pop() % len(words["v%s"%r])] + ' '
        #print(words["v%s"%r][rand.pop() % len(words["v%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        r = 7-syllables
        syllables += r
        poem += words["adv%s"%r][rand.pop() % len(words["adv%s"%r])] + ' '
        #print(words["adv%s"%r][rand.pop() % len(words["adv%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        #print()
        poem += "\n"
        #line 3
        syllables = 0
        r = rand.pop()%(3-syllables) +1
        syllables += r
        poem += words["n%s"%r][rand.pop() % len(words["n%s"%r])] + ' '
        #print(words["n%s"%r][rand.pop() % len(words["n%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        r = rand.pop()%(4-syllables) +1
        syllables += r
        poem += words["v%s"%r][rand.pop() % len(words["v%s"%r])] + ' '
        #print(words["v%s"%r][rand.pop() % len(words["v%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        r = 5-syllables
        syllables += r
        poem += words["adv%s"%r][rand.pop() % len(words["adv%s"%r])] + ' '
        #print(words["adv%s"%r][rand.pop() % len(words["adv%s"%r])], end=' ')
        if DEBUG: print(syllables, end=' ')
        poem += "\n"
        poem += "\n"

        print(poem)
        tts = gTTS(text=poem, lang='en')
        tts.save("poem.mp3")
        os.system("poem.mp3")

