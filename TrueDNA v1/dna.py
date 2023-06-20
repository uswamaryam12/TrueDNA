import random
from pandas import *

#Types of Personalties
analyist_person = {'INTJ':'Architect','INTP':'Logician','ENTJ':'Commander','ENTP':'Debater'}
diplomatic_person = {'INFJ':'Advocate','INFP': 'Mediator','ENFJ':'Protagonist','ENFP':'Campainer'}
sentinel_person = {'ISTJ':'Logistician','ISFJ':'Defender','ESTJ':'Executive','ESFJ': 'Consul'}
explorer_person = {'ISTP':'Virtuoso', 'ISFP':'Adventurer','ESTP':'Entrepreneur','ESFP': 'Entertainer'}



personalities = {'INTJ','ENTJ','INTP','ENTP','ENFJ','INFJ','INFP','ENFP','ISTJ','ISFJ','ESTJ','ESFJ','ISTP','ISFP','ESTP','ESFP'}

personality = random.choice(list(personalities))
#print(personality)
#print()
names_male_list = "Male.csv"
names_female_list = "Female.csv"

data = read_csv(names_female_list)
data = data['Name'].tolist()
data1 = read_csv(names_male_list)
data1 = data1['Name'].tolist()

directory_c180 = 'folder' #folder for most intelligent one's
directory_intelligent = 'folder' #folder for intelligent one's
directory_mid = 'folder' #folder for mid one's
directory_low = 'folder' #folder for low one's
directory_mental = 'folder' #folder for mentally disable one's

#Level of IQ
iq_god_gifted = random.randint(181, 220) #0.1%
iq_genius = random.randint(161, 180) #2%
iq_intelligent = random.randint(131, 160) #4%
iq_above_avg = random.randint(115, 130) #10%
iq_avg = random.randint(85, 114) #75%
iq_below_avg = random.randint(70, 84) #6%
iq_mild_mental = random.randint(55, 69) #2%
iq_moderate_mental = random.randint(40, 54) #0.6%
iq_severe_mental = random.randint(25, 39) #0.2%
iq_profound_mental = random.randint(1, 24) #0.1%

iq_list = [iq_god_gifted,iq_genius,iq_intelligent,iq_above_avg, iq_avg, iq_below_avg, iq_mild_mental, iq_moderate_mental, iq_severe_mental, iq_profound_mental]
iq = random.choices(iq_list , weights=(0.001,0.5,5.5,10,75,6,2,0.6,0.2,0.001))

male = random.choice(list(data1)) + "_" + random.choice(list(data1)) + "_M"
female = random.choice(list(data)) + "_" + random.choice(list(data1)) + "_F"
name_list = {male,female}
name = random.choice(list(name_list))+".py"


def dna():
    iq_list = [iq_god_gifted, iq_genius, iq_intelligent, iq_above_avg, iq_avg, iq_below_avg, iq_mild_mental,
               iq_moderate_mental, iq_severe_mental, iq_profound_mental]
    iq = random.choices(iq_list, weights=(0.001, 0.599, 5.5, 10, 75, 7.099, 1.3, 0.3, 0.2, 0.001))
    personality = random.choice(list(personalities))

    return iq[0], personality


def baby(iq, personality):
    male = random.choice(list(data1)) + "_" + random.choice(list(data1)) + "_M"
    female = random.choice(list(data)) + "_" + random.choice(list(data1)) + "_F"
    name_list = {male, female}
    name = random.choice(list(name_list)) + ".py"

    if iq < 70:
        directory = directory_mental + name
        with open(directory, 'a+') as f:
            f.write("IQ = " + str(iq) + "\nPersonality = '" + personality + "'")

    elif iq >= 70 and iq < 85:
        directory = directory_low + name
        with open(directory, 'a+') as f:
            f.write("IQ = " + str(iq) + "\nPersonality = '" + personality + "'")

    elif iq >= 85 and iq <= 130:
        directory = directory_mid + name
        with open(directory, 'a+') as f:
            f.write("IQ = " + str(iq) + "\nPersonality = '" + personality + "'")

    elif iq > 180:
        directory = directory_c180 + name
        with open(directory, 'a+') as f:
            f.write("IQ = " + str(iq) + "\nPersonality = '" + personality + "'")
    else:
        directory = directory_intelligent + name
        with open(directory, 'a+') as f:
            f.write("IQ = " + str(iq) + "\nPersonality = '" + personality + "'")

    print("Baby is born!")

def pregnant(baby, iq):
    fun = dna()
    baby_iq = baby
    Iq = iq
    iq_avg = int(fun[0]+baby_iq+Iq)/3

    return int(iq_avg), fun[1]

def mating(iq):
    Iq = iq
    val = dna()[0]

    return Iq, val


def mating_ready(age, mating_interest):
    if age > 18 and mating_interest >= 70:
        a = 1
    else:
        a = 0
    return a