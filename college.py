from PIL import Image

def is_stressful():
    return True

def insanity_jumbles(inspiration):
    rand = []
    i = 0
    j = 0
    fails = 0
    while True:
        try:
            rand.append(abs(hash(inspiration[i,j])))
            i += 1
            fails = 0
        except:
            fails += 1
            i = 0
            j += 1
            if fails > 2:
                rand = list(dict.fromkeys(rand))
                return rand