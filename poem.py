import google
import contemplating
import college
import troy_weather
from japan import haiku
from english import rhyme
from oh import my

from time import sleep as taking_refuge_inside_my_mind
from time import sleep

my = my()

#Start reading poem from bottom up, following code flow

def bonus_poem():
    concept = "patience is a virtue"
    for idea in concept:
        print(idea, end='')
        sleep(3600)


def writePoem(whatKind, my_wandering_thoughts):
    if(whatKind == 'h'):
        haiku(my_wandering_thoughts)
    elif(whatKind == 'r'):
        rhyme(my_wandering_thoughts)


def ask_someone():
    type = "unsure"
    while type not in ["h", "r"]:
        type = input("Should I write a Haiku or a Rhyme? (Enter H or R) ")
        type = type[0]
        type = type.lower()
    return type

def sure_of_what_kind_of_poem_to_write(my_wandering_thoughts,
whatKind="not sure",sure=False):
    if(not sure):
        recommended_kind = ask_someone()
        writePoem(recommended_kind, my_wandering_thoughts)
    else:
        writePoem(whatKind, my_wandering_thoughts)

def wake_up_inspired_by(my_wandering_thoughts):
    try:
        to_write_poem()
    except:
        I_am = not sure_of_what_kind_of_poem_to_write(my_wandering_thoughts,
        "torn between Haiku and Rhyming")


def bang_head_on_desk():
    my.thoughts = "I'm too tired to do this..."
    print(my.thoughts)
    pass #out from exaustion

def write_poem_to_relax():
    print("Let's write a poem to relax..")
    try:
        to_write_poem()
    except:
        my.mind = "Uninspired, bad at poetry"
        print(my.mentalState())
        inspiration = google.images()
        taking_refuge_inside_my_mind(contemplating.image())
        my.mind = "Tired of staring at Images, still uninspired, now tired"
        print(my.mentalState())
        bang_head_on_desk()
        taking_refuge_inside_my_mind(contemplating.theMeaningOfLife())
        my.wandering_thoughts = college.insanity_jumbles(inspiration);
        print("wakes up inspired by jumbled thoughts")
        wake_up_inspired_by(my.wandering_thoughts)

if(college.is_stressful() and troy_weather.is_gloomy()):
    write_poem_to_relax()