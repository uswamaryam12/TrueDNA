import random
import os
import csv
import pathlib
import pandas as pd



#Eyes
eye_colour = 'Black'
eye_type = 'Round'
eye_is_working_r = 1
eye_disability_r = 0
eye_is_working_l = 1
eye_disability_l = 0


if eye_disability_r == 0:
    eye_disability_type_r = None
else:
    eye_disability_type_r = random.randint(1,5)

if eye_disability_l == 0:
    eye_disability_type_l = None
else:
    eye_disability_type_l = random.randint(1,5)


eye_n_sight_r = 6
eye_f_sight_r = 4
eye_n_sight_l = 6
eye_f_sight_l = 6

eye_dark_circle = 1.4


#Hair
hair_colour = 'Black'
hair_size = 'long'
hair_type = 'straight'
hair_thickness = 8
hair_disability = 0


#Face
skin_tone = 'white'
face_type = 'oval'
face_cheeks = 1
face_disability = 0

#Nose
nose_type = 'mid'
nose_disability = 0

#Body
body_type = 'athlete'
body_disability = 0

#Ears
ear_size = 'mid'
ear_type = 'free'
ear_working_l = 1
ear_working_r = 1
ear_disability_l = 0
ear_disability_r = 0

#Tongue
tongue_size = 'mid'
tongue_disability = 0

#Hands
hand_size = 'mid'
hand_working_l = 1
hand_working_r = 1
hand_disability_l = 0
hand_disability_r = 0

#Feet
feet_size = 'mid'
feet_working_l = 1
feet_working_r = 1
feet_disability_l = 0
feet_disability_r = 0

#Misc
#Types of Personalties
analyist_person = {'INTJ':'Architect','INTP':'Logician','ENTJ':'Commander','ENTP':'Debater'}
diplomatic_person = {'INFJ':'Advocate','INFP': 'Mediator','ENFJ':'Protagonist','ENFP':'Campainer'}
sentinel_person = {'ISTJ':'Logistician','ISFJ':'Defender','ESTJ':'Executive','ESFJ': 'Consul'}
explorer_person = {'ISTP':'Virtuoso', 'ISFP':'Adventurer','ESTP':'Entrepreneur','ESFP': 'Entertainer'}


iq_god_gifted = random.randint(181, 220) #0.001%
iq_genius = random.randint(161, 180) #0.5%
iq_intelligent = random.randint(131, 160) #5.5%
iq_above_avg = random.randint(115, 130) #10%
iq_avg = random.randint(85, 114) #75%
iq_below_avg = random.randint(70, 84) #6%
iq_mild_mental = random.randint(55, 69) #2%
iq_moderate_mental = random.randint(40, 54) #0.6%
iq_severe_mental = random.randint(25, 39) #0.2%
iq_profound_mental = random.randint(1, 24) #0.001%

iq_list = [iq_god_gifted,iq_genius,iq_intelligent,iq_above_avg, iq_avg, iq_below_avg, iq_mild_mental, iq_moderate_mental, iq_severe_mental, iq_profound_mental]
iq = random.choices(iq_list , weights=(0.001,0.5,5.5,10,75,6,2,0.6,0.2,0.001))

IQ = iq[0]
IQ = {'Name': 'IQ','IQ' : IQ}

personalities_list = ['INTJ','ENTJ','INTP','ENTP','ENFJ','INFJ','INFP','ENFP','ISTJ','ISFJ','ESTJ','ESFJ','ISTP','ISFP','ESTP','ESFP']
personality_type = random.choices(personalities_list, weights=(2.1,1.8,3.3,3.2,2.5,1.5,4.4,8.1,11.6,13.8,8.7,12,5.4,8.8,4.3,8.5))

personality = personality_type[0]
personality = {'Name': 'Personality','Personality': personality}

height = 180
height = {'Name': 'Height','Height': height}
beauty_level = 9
beauty_level = {'Name': 'Beauty','Beauty' : beauty_level}
mieosis = random.randint(0,1)
mieosis = {'Name': 'Mieosis','Mieosis': mieosis}
mitosis = 0
mitosis = {'Name': 'Mitosis','Mitosis': mitosis}

#DNA Functions
def dnaEye(colour, type, is_working_l, is_working_r, disability_l, disability_r, n_sight_l, n_sight_r, f_sight_l, f_sight_r, dark_circle, disability_type_l, disability_type_r):
    dna_eye_l = {'Name': 'Left Eye', 'Tone': colour, 'Type': type, 'Working': is_working_l, 'N_Sight': n_sight_l,'F_Sight': f_sight_l, 'DarkCircle': dark_circle, 'Disability': disability_l, 'Disability_Type': disability_type_l}
    dna_eye_r = {'Name' : 'Right Eye','Tone': colour, 'Type': type,'Working': is_working_r,'N_Sight': n_sight_r,'F_Sight': f_sight_r,'DarkCircle': dark_circle,'Disability': disability_r,'Disability_Type': disability_type_r}
    dna_eye = [dna_eye_l, dna_eye_r]
    return dna_eye

def dnaEyeL(colour, type, is_working_l, n_sight_l,f_sight_l, dark_circle, disability_l, disability_type_l):
    dna_eye_l = {'Name': 'Left Eye', 'Tone': colour, 'Type': type, 'Working': is_working_l, 'N_Sight': n_sight_l,'F_Sight': f_sight_l, 'DarkCircle': dark_circle, 'Disability': disability_l,'Disability_Type': disability_type_l}
    return dna_eye_l

def dnaEyeR(colour, type, is_working_r, n_sight_r,f_sight_r, dark_circle, disability_r, disability_type_r):
    dna_eye_r = {'Name' : 'Right Eye','Tone': colour, 'Type': type,'Working': is_working_r,'N_Sight': n_sight_r,'F_Sight': f_sight_r,'DarkCircle': dark_circle,'Disability': disability_r,'Disability_Type': disability_type_r}
    return dna_eye_r

def dnaHair(colour, size, type, thickness, disability):
    dna_hair = {'Name': 'Hair','Tone': colour,'Size': size,'Type': type,'Thickness': thickness, 'Disability': disability}
    return dna_hair

def dnaFace(skin_tone, type, cheeks, disability):
    dna_face = {'Name': 'Face', 'Tone': skin_tone,'Type': type, 'Cheeks' : cheeks, 'Disability': disability}
    return dna_face

def dnaNose(type, disability):
    dna_nose = {'Name': 'Nose', 'Type': type, 'Disability': disability}
    return dna_nose

def dnaBody(type,skin_tone, disability):
    dna_body = {'Name': 'Body', 'Type': type,'Tone': skin_tone, 'Disability': disability}
    return dna_body

def dnaEar(size, type, is_working_l, is_working_r, disability_l, disability_r):
    dna_ear_l = {'Name': 'Left Ear', 'Type': type, 'Size' : size, 'Working': is_working_l, 'Disability' : disability_l}
    dna_ear_r = {'Name': 'Right Ear', 'Type': type, 'Size' : size, 'Working': is_working_r, 'Disability' : disability_r}
    dna_ear = [dna_ear_l, dna_ear_r]
    return dna_ear

def dnaEarL(type,size, is_working_l, disability_l):
    dna_ear_l = {'Name': 'Left Ear', 'Type': type, 'Size': size, 'Working': is_working_l, 'Disability': disability_l}
    return dna_ear_l

def dnaEarR(type,size, is_working_r, disability_r):
    dna_ear_r = {'Name': 'Right Ear', 'Type': type, 'Size' : size, 'Working': is_working_r, 'Disability' : disability_r}
    return dna_ear_r

def dnaTongue(size, disability):
    dna_tongue = {'Name': 'Tongue', 'Size': size, 'Disability': disability}
    return dna_tongue

def dnaHand(size, is_working_l, is_working_r, disability_l, disability_r):
    dna_hand_l = {'Name': 'Left Hand', 'Size': size,'Working': is_working_l, 'Disability': disability_l}
    dna_hand_r = {'Name': 'Right Hand', 'Size': size,'Working': is_working_r, 'Disability': disability_r}
    dna_hand = [dna_hand_l, dna_hand_r]
    return dna_hand

def dnaHandL(size, is_working_l, disability_l):
    dna_hand_l = {'Name': 'Left Hand', 'Size': size, 'Working': is_working_l, 'Disability': disability_l}
    return dna_hand_l

def dnaHandR(size, is_working_r, disability_r):
    dna_hand_r = {'Name': 'Right Hand', 'Size': size,'Working': is_working_r, 'Disability': disability_r}
    return dna_hand_r

def dnaFeet(size, is_working_l, is_working_r, disability_l, disability_r):
    dna_feet_l = {'Name': 'Left Feet', 'Size': size,'Working': is_working_l, 'Disability': disability_l}
    dna_feet_r = {'Name': 'Right Feet', 'Size': size,'Working': is_working_r, 'Disability': disability_r}
    dna_feet = [dna_feet_l, dna_feet_r]
    return dna_feet

def dnaFeetL(size, is_working_l, disability_l):
    dna_feet_l = {'Name': 'Left Feet', 'Size': size,'Working': is_working_l, 'Disability': disability_l}
    return dna_feet_l

def dnaFeetR(size, is_working_r, disability_r):
    dna_feet_r = {'Name': 'Right Feet', 'Size': size,'Working': is_working_r, 'Disability': disability_r}
    return dna_feet_r


def Sperm(dnaFace, dnaHair, dnaEye,dnaEar,dnaNose, dnaTongue, dnaBody, dnaHand, dnaFeet, dnaBeauty, dnaHeight, dnaIQ, dnaPersonality, mieosis):
    chromosome = [dnaFace, dnaHair, dnaEye[0],dnaEye[1],dnaEar[0],dnaEar[1],dnaNose,dnaTongue,dnaBody,dnaHand[0],dnaHand[1],dnaFeet[0],dnaFeet[1], dnaBeauty, dnaHeight, dnaIQ, dnaPersonality,mieosis]
    return chromosome

def Egg(dnaFace, dnaHair, dnaEye,dnaEar,dnaNose, dnaTongue, dnaBody, dnaHand, dnaFeet, dnaBeauty, dnaHeight, dnaIQ, dnaPersonality, mitosis):
    chromosome = [dnaFace, dnaHair, dnaEye[0],dnaEye[1],dnaEar[0],dnaEar[1],dnaNose,dnaTongue,dnaBody,dnaHand[0],dnaHand[1],dnaFeet[0],dnaFeet[1], dnaBeauty, dnaHeight, dnaIQ, dnaPersonality,mitosis]
    return chromosome

'''
dna_face = dnaFace(skin_tone,face_type, face_cheeks, face_disability)
dna_hair = dnaHair(hair_colour, hair_size, hair_type, hair_thickness, hair_disability)
dna_eye = dnaEye(eye_colour, eye_type, eye_is_working_l, eye_is_working_r, eye_disability_l, eye_disability_r, eye_n_sight_l, eye_n_sight_r, eye_f_sight_l,eye_f_sight_r,eye_dark_circle, eye_disability_type_l, eye_disability_type_r)
dna_ear = dnaEar(ear_size, ear_type, ear_working_l, ear_working_r, ear_disability_l, ear_disability_r)
dna_nose = dnaNose(nose_type, nose_disability)
dna_tongue = dnaTongue(tongue_size, tongue_disability)
dna_body = dnaBody(body_type,skin_tone, body_disability)
dna_hand = dnaHand(hand_size, hand_working_l, hand_working_r, hand_disability_l, hand_disability_r)
dna_feet = dnaFeet(feet_size, feet_working_l,feet_working_r,feet_disability_l, feet_disability_r)

#print(dna_face, dna_hair, dna_eye, dna_ear, dna_nose, dna_tongue, dna_body, dna_hand, dna_feet)
male_chrom = Sperm(dna_face, dna_hair, dna_eye, dna_ear, dna_nose, dna_tongue, dna_body, dna_hand, dna_feet, beauty_level, height, IQ, personality , mieosis)
female_chrom = Egg(dna_face, dna_hair, dna_eye, dna_ear, dna_nose, dna_tongue, dna_body, dna_hand, dna_feet, beauty_level, height, IQ, personality , mitosis)


chromosome_head_female = ['Name', 'Working', 'Size','Disability', 'Disability_Type', 'Tone', 'Type', 'N_Sight','F_Sight','DarkCircle', 'Cheeks', 'Thickness' , 'Beauty', 'Height', 'IQ', 'Personality', 'Mitosis']
chromosome_head_male = ['Name', 'Working', 'Size','Disability', 'Disability_Type', 'Tone', 'Type', 'N_Sight','F_Sight','DarkCircle', 'Cheeks', 'Thickness' , 'Beauty', 'Height', 'IQ', 'Personality', 'Mieosis']


with open('chromosome_male.csv', 'a+') as f:
    writer = csv.DictWriter(f, fieldnames=chromosome_head_male)
    writer.writeheader()
    writer.writerows(male_chrom)

with open('chromosome_female.csv', 'a+') as f:
    writer = csv.DictWriter(f, fieldnames=chromosome_head_female)
    writer.writeheader()
    writer.writerows(female_chrom)


read_male_data = pd.read_csv('chromosome_male.csv')
print(read_male_data.to_string()+ '\n\n')
read_female_data = pd.read_csv('chromosome_female.csv')
print(read_female_data.to_string())
'''

#Chromosome Details
#skin_tone = random.choice(skin_tone_m, skin_tone_f)
def dnaBabyFace(skin_tone, type_m, cheeks_m, disability_m, type_f, cheeks_f, disability_f):
    face_type = random.choice(type_m,type_f)
    disability = random.choice(disability_m, disability_f)
    cheeks = random.choice(cheeks_m, cheeks_f)
    dnaBabyFace = {'Name': 'Face', 'Tone': skin_tone,'Type': face_type, 'Cheeks' : cheeks, 'Disability': disability}
    return dnaBabyFace

def dnaBabyEye(colour_m, colour_f, type_m, type_f, is_working_l_m,is_working_l_f, is_working_r_m,is_working_r_f,
               disability_l_m, disability_r_m,disability_l_f, disability_r_f, n_sight_l_m, n_sight_r_m,
               n_sight_l_f, n_sight_r_f, f_sight_l_m, f_sight_r_m,f_sight_l_f, f_sight_r_f, dark_circle_m,dark_circle_f,
               disability_type_l_m, disability_type_r_m,disability_type_l_f, disability_type_r_f):
    colour = random.choice(colour_m, colour_f)
    type = random.choice(type_m, type_f)
    is_working_l = random.choice(is_working_l_m,is_working_l_f)
    is_working_r = random.choice(is_working_r_m, is_working_r_f)
    n_sight_l = random.choice(n_sight_l_m, n_sight_l_f)
    n_sight_r = random.choice(n_sight_r_m, n_sight_r_f)
    f_sight_l = random.choice(f_sight_l_m, f_sight_l_f)
    f_sight_r = random.choice(f_sight_r_m, f_sight_r_f)
    dark_circle = random.choice(dark_circle_m, dark_circle_f)
    disability_l = random.choice(disability_l_m, disability_l_f)
    disability_r = random.choice(disability_r_m, disability_r_f)
    disability_type_l = random.choice(disability_type_l_m, disability_type_l_f)
    disability_type_r = random.choice(disability_type_r_m, disability_type_r_f)
    dna_eye_l = {'Name': 'Left Eye', 'Tone': colour, 'Type': type, 'Working': is_working_l, 'N_Sight': n_sight_l,'F_Sight': f_sight_l, 'DarkCircle': dark_circle, 'Disability': disability_l, 'Disability_Type': disability_type_l}
    dna_eye_r = {'Name' : 'Right Eye','Tone': colour, 'Type': type,'Working': is_working_r,'N_Sight': n_sight_r,'F_Sight': f_sight_r,'DarkCircle': dark_circle,'Disability': disability_r,'Disability_Type': disability_type_r}
    dna_eye = [dna_eye_l, dna_eye_r]
    return dna_eye

def dnaBabyEar(size_m,size_f, type_m, type_f, is_working_l_m, is_working_r_m, disability_l_m, disability_r_m, is_working_l_f, is_working_r_f, disability_l_f, disability_r_f):
    size = random.choice(size_m, size_f)
    type = random.choice(type_m, type_f)
    is_working_l = random.choice(is_working_l_m, is_working_l_f)
    is_working_r = random.choice(is_working_r_m, is_working_r_f)
    disability_l = random.choice(disability_l_m, disability_l_f)
    disability_r = random.choice(disability_r_m, disability_r_f)
    dna_ear_l = {'Name': 'Left Ear', 'Type': type, 'Size': size, 'Working': is_working_l, 'Disability': disability_l}
    dna_ear_r = {'Name': 'Right Ear', 'Type': type, 'Size': size, 'Working': is_working_r, 'Disability': disability_r}
    dna_ear = [dna_ear_l, dna_ear_r]
    return dna_ear

def dnaBabyHair(colour_m, size_m, type_m, thickness_m, disability_m, colour_f, size_f, type_f, thickness_f, disability_f):
    colour = random.choice(colour_m, colour_f)
    size = random.choice(size_m, size_f)
    type = random.choice(type_m, type_f)
    thickness = random.choice(thickness_m, thickness_f)
    disability = random.choice(disability_m, disability_f)
    dna_hair = {'Name': 'Hair','Tone': colour,'Size': size,'Type': type,'Thickness': thickness, 'Disability': disability}
    return dna_hair

def dnaBabyNose(type_m, disability_m, type_f, disability_f):
    type = random.choice(type_m, type_f)
    disability = random.choice(disability_m, disability_f)
    dna_nose = {'Name': 'Nose', 'Type': type, 'Disability': disability}
    return dna_nose

def dnaBabyTongue(size_m, disability_m, size_f, disability_f):
    size = random.choice(size_m, size_f)
    disability = random.choice(disability_m, disability_f)
    dna_tongue = {'Name': 'Tongue', 'Size': size, 'Disability': disability}
    return dna_tongue

def dnaBabyBody(type_m,skin_tone_m, disability_m, type_f, skin_tone_f, disability_f):
    type = random.choice(type_m, type_f)
    disability = random.choice(disability_m, disability_f)
    skin_tone = random.choice(skin_tone_m, skin_tone_f)
    dna_body = {'Name': 'Body', 'Type': type,'Tone': skin_tone, 'Disability': disability}
    return dna_body

def dnababyHand(size_m, is_working_l_m, is_working_r_m, disability_l_m, disability_r_m, size_f, is_working_l_f, is_working_r_f, disability_l_f, disability_r_f):
    size = random.choice(size_m, size_f)
    is_working_l = random.choice(is_working_l_m, is_working_l_f)
    is_working_r = random.choice(is_working_r_m, is_working_r_f)
    disability_l = random.choice(disability_l_m, disability_l_f)
    disability_r = random.choice(disability_r_m, disability_r_f)
    dna_hand_l = {'Name': 'Left Hand', 'Size': size,'Working': is_working_l, 'Disability': disability_l}
    dna_hand_r = {'Name': 'Right Hand', 'Size': size,'Working': is_working_r, 'Disability': disability_r}
    dna_hand = [dna_hand_l, dna_hand_r]
    return dna_hand

def dnababyFeet(size_m, is_working_l_m, is_working_r_m, disability_l_m, disability_r_m, size_f, is_working_l_f, is_working_r_f, disability_l_f, disability_r_f):
    size = random.choice(size_m, size_f)
    is_working_l = random.choice(is_working_l_m, is_working_l_f)
    is_working_r = random.choice(is_working_r_m, is_working_r_f)
    disability_l = random.choice(disability_l_m, disability_l_f)
    disability_r = random.choice(disability_r_m, disability_r_f)
    dna_feet_l = {'Name': 'Left Feet', 'Size': size, 'Working': is_working_l, 'Disability': disability_l}
    dna_feet_r = {'Name': 'Right Feet', 'Size': size, 'Working': is_working_r, 'Disability': disability_r}
    dna_feet = [dna_feet_l, dna_feet_r]
    return dna_feet

def chromosome(dnaFace, dnaHair, dnaEye,dnaEar,dnaNose,dnaTongue,dnaBody,dnaHand,dnaFeet, dnaBeauty, dnaHeight, dnaIQ, dnaPersonality):
    chromosome = [dnaFace, dnaHair, dnaEye[0],dnaEye[1],dnaEar[0],dnaEar[1],dnaNose,dnaTongue,dnaBody,dnaHand[0],dnaHand[1],dnaFeet[0],dnaFeet[1], dnaBeauty, dnaHeight, dnaIQ, dnaPersonality]
    return chromosome

def chromosomeBaby(dnaFace, dnaHair, dnaEye,dnaEar,dnaNose,dnaTongue,dnaBody,dnaHand,dnaFeet, dnaBeauty, dnaHeight, dnaIQ, dnaPersonality):
    chromosome = [dnaFace, dnaHair, dnaEye[0],dnaEye[1],dnaEar[0],dnaEar[1],dnaNose,dnaTongue,dnaBody,dnaHand[0],dnaHand[1],dnaFeet[0],dnaFeet[1], dnaBeauty, dnaHeight, dnaIQ, dnaPersonality]
    return chromosome

name = os.path.basename(__file__)
name = name.replace(".py", "")
name = name.title()
print(name)