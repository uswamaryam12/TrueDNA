import random
import os
import tkinter


most_important = []
least_important = []
internal_organs = []

#Most Important Internal Organs
brain = []
heart = []
most_important = [brain, heart]

#Least Important Internal Organs
lungs = []
liver = []
stomach = []
kidney = []
pancrease = []
intestine = []
male_reproductive_organ = []
female_reproductive_organ = []

least_important = [lungs, liver, stomach, kidney, pancrease, intestine, male_reproductive_organ, female_reproductive_organ]
internal_organs = [most_important, least_important]

#External Organs
external_organs = []
external_face = []
external_body = []
external_feet = []

#External Face Organs
face = []
eye = []
nose = []
lips = []
cheeks = []
eyebrows = []
eye_lashes = []
facial_hairs = []
teeth = []
ears = []
skin = []
tongue = []

external_face = [face, eye, nose, lips, cheeks, eyebrows, eye_lashes, facial_hairs, teeth, ears, skin, tongue]


#External Body Organs
chest = []
neck = []
back = []
belly = []
breast = []
umbilical = []
abdominal = []
body = []
mons = []
groin = []
shoulder = []
hands = []
arms = []
fingers_hand = []
axilla = []
elbow = []
fore_arm = []
wrist = []
vulva = []
penis = []
scrotum = []

external_body = [chest, neck, back, belly, breast,umbilical, abdominal, body, mons, groin, shoulder, hands, arms, fingers_hand, axilla, elbow, fore_arm, wrist, vulva, penis, scrotum]


#External Feet Organs
hip = []
thigh = []
knee = []
leg = []
ankle = []
foot = []
buttock = []
calf = []
heel = []
fingers_feet = []

external_feet = [hip, thigh, knee, leg, ankle, foot, buttock, calf, heel, fingers_feet]
external_organs = [external_face, external_body, external_feet]

#Others
special_features = []
bones = []
blood = []
sperm = []
egg = []
Aging = []
Health = []

class Brain:
    def __init__(self):
        # intelligence
        self.iq = None
        self.mentality_level = None

        # traits
        self.personality_traits = None
        self.behavioural_traits = None
        self.reproductive_traits = None

        # health
        self.brain_health = None
        self.mental_health = None

        # disease
        self.cancer = None
        self.tumor = None
        self.neurological_disorder = None

        # functions
        self.cell_signalling = None
        self.sleep_regulation = None
        self.cognitive_ability = None
        self.pain_perception = None
        self.neural_transmitter_regulator = None

        # adaptations
        self.environmental_adaptation = None

        # recover
        self.recover_timing = None
        self.healing_power = None

        # timingChart
        self.developmental_timing = None
        self.memory_formation = None

        # misc
        self.strength = None
        self.stress_rate = None
        self.age_factor = None
        self.disability = None
        self.neurons_speed = None
        self.shape = None
        self.size = None


class Heart:
    def __init__(self):
        # emotions
        self.emotion = None
        self.emotions_level = None

        # functions
        self.heart_rate = None
        self.heart_muscle = None
        self.pain_perception = None
        self.blood_pressure_regulation = None
        self.blood_speed = None

        # traits
        self.personality_traits = None
        self.behavioural_traits = None
        self.reproductive_traits = None
        self.feeling_traits = None

        # health
        self.heart_health = None
        self.emotion_health = None
        self.cardiovascular_health = None

        # disease
        self.cancer = None
        self.failure = None
        self.cardiovascular_disorder = None

        # adaptations
        self.environmental_adaptation = None

        # timeChart
        self.developmental_timing = None
        self.emotions_formation = None

        # recover
        self.recover_timing = None
        self.healing_power = None

        # misc
        self.age_factor = None
        self.strength = None
        self.shape = None
        self.size = None
        self.disability = None


class Lungs:
    def __init__(self):
        # functions
        self.lungs_capacity = None
        self.gas_exchange_efficiency = None
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.lungs_health = None
        self.respiratory_health = None

        # disease
        self.lungs_cancer = None
        self.lungs_disorder = None
        self.lungs_disease = None
        self.genetic_disease = None
        self.respiratory_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.lungs_size = None
        self.lungs_shape = None
        self.strength = None
        self.age_factor = None


class Liver:
    def __init__(self):
        # functions
        self.metabolism = None
        self.detoxification_capacity = None
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.liver_health = None
        self.metabolism_helth = None

        # disease
        self.liver_cancer = None
        self.liver_disease = None
        self.liver_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.liver_shape = None
        self.liver_size = None
        self.age_factor = None
        self.strength = None


class Kidney:
    def __init__(self):
        # functions
        self.urine_production = None
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.kidney_health = None
        self.urine_health = None

        # disease
        self.kidney_cancer = None
        self.kidney_disease = None
        self.kidney_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.kidney_size = None
        self.kidney_shape = None
        self.strength = None
        self.age_factor = None


class Intestine:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.nutrient_absorption = None
        self.intestinal_mobility = None
        self.gut_microbiome_composition = None

        # health
        self.intestine_health = None

        # disease
        self.cancer = None
        self.intestine_disease = None
        self.disorder = None
        self.gastro_intestine_disorder = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Stomach:
    def __init__(self):
        # functions
        self.gastric_acid_production = None
        self.nutrient_absorption = None
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.stomach_health = None
        self.digestive_health = None

        # disease
        self.stomach_cancer = None
        self.stomach_disease = None
        self.stomach_disorder = None
        self.gastric_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.stomach_shape = None
        self.stomach_size = None
        self.age_factor = None
        self.strength = None


class Pancreases:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.insulin_production = None
        self.glucose_regulation = None
        self.digestive_enzyme_production = None

        # health
        self.pancreases_health = None
        self.insulin_health = None
        self.enzyme_health = None

        # disease
        self.cancer = None
        self.disorder = None
        self.genetic_disease = None
        self.diabetes = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Male_Reproductive_Organ:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.sex_hormone_production = None
        self.fertility = None
        self.changes_hormone_level = None

        # health
        self.organ_health = None
        self.sex_hormone_health = None

        # disease
        self.cancer = None
        self.organ_disease = None
        self.organ_disorder = None
        self.hormonal_disorder = None
        self.reproductive_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # traits
        self.reproductive_traits = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.sperm_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Female_Reproductive_Organ:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.sex_hormone_regulation = None
        self.fertility = None
        self.changes_hormone_level = None

        # health
        self.organ_health = None
        self.sex_hormone_health = None

        # disease
        self.cancer = None
        self.organ_disease = None
        self.organ_disorder = None
        self.reproductive_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # traits
        self.reproductive_traits = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.egg_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Cheeks:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.facial_fat = None
        self.facial_fat_distribution = None
        self.cheeks_structure = None

        # health
        self.cheeks_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.cheeks_disease = None
        self.cheeks_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.texture_change = None
        self.hardness_change = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.thickness = None
        self.hardness = None


class Ear:
    def __init__(self):
        # hearing
        self.frequency = None
        self.hearing_level = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.hearing_regulation = None

        # health
        self.ear_health = None
        self.hearing_health = None
        self.skin_health = None

        # disease
        self.cancer = None
        self.ear_disease = None
        self.ear_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.hearing_loss = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.hearing_ability = None
        self.ear_lobe_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.ear_lob_size = None


class Eye:
    def __init__(self):
        # vision
        self.blue = None
        self.red = None
        self.green = None
        self.far_vision = None
        self.near_vision = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.sensitivity_to_light = None

        # health
        self.eye_health = None
        self.iris_health = None
        self.lens_health = None
        self.retina_health = None
        self.skin_health = None

        # disease
        self.cancer = None
        self.eye_disease = None
        self.eye_disorder = None
        self.genetic_disease = None
        self.eye_redness = None
        self.eye_vision = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None
        self.iris_adaptation = None
        self.lens_adaptation = None
        self.retina_adaptation = None

        # timeChart
        self.developmental_timing = None
        self.iris_development = None
        self.lens_development = None
        self.retina_development = None
        self.eye_lid_upper = None
        self.eye_lid_lower = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.iris_color = None
        self.lens_size = None
        self.iris_size = None
        self.retina_size = None


class Eye_Lashes:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None

        # health
        self.eye_lashes_health = None

        # disease
        self.cancer = None
        self.hormone_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.density = None
        self.thinning = None
        self.curl = None


class Eyebrows:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None

        # health
        self.eyebrows_health = None

        # disease
        self.cancer = None
        self.hormone_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.density = None
        self.thinning = None


class Facial_Hairs:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None
        self.facial_hair_growth = None
        self.growth_pattern = None

        # health
        self.facial_health = None

        # disease
        self.cancer = None
        self.hormone_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.density = None
        self.thinning = None
        self.moustache_thickness = None
        self.beard_thickness = None


class Lip:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.moisture_retention = None
        self.lip_texture = None

        # health
        self.lip_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.lip_disease = None
        self.lip_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.texture_change = None
        self.hardness_change = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.thickness = None
        self.hardness = None


class Nose:
    def __init__(self):
        # smell
        self.smell_ability = None
        self.smell_sensitivity = None
        self.smell_sense = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.nasal_passage_structure = None
        self.hormone_regulation = None

        # health
        self.ear_health = None
        self.smelling_health = None
        self.skin_health = None

        # disease
        self.cancer = None
        self.nose_disease = None
        self.nose_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.smell_loss = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Skin:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.texture = None
        self.pigmentation = None
        self.fat_growth = None
        self.fat_distribution = None

        # health
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.skin_disease = None
        self.skin_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.tone_change = None

        # misc
        self.size = None
        self.shape = None
        self.age_factor = None
        self.strength = None
        self.tone = None
        self.thickness = None
        self.hardness = None
        self.density = None


class Teeth:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.teeth_enamel_strength = None
        self.teeth_alignment = None

        # health
        self.teeth_health = None
        self.teeth_enamel_health = None

        # disease
        self.cancer = None
        self.disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Wrist:
    def __init__(self):
        # structure
        self.wrist_structure = None
        self.range_of_motion = None
        self.flexibility = None
        self.stability = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None
        self.joint_functions = None

        # health
        self.wrist_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.wrist_disease = None
        self.wrist_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.wrist_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Vulva:
    def __init__(self):
        # function
        self.growth_rate = None
        self.pain_perception = None
        self.vaginal_ph = None

        # health
        self.vulva_health = None
        self.vaginal_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.vulva_disease = None
        self.vulva_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # traits
        self.vulva_traits = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.vulva_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Penis:
    def __init__(self):
        # function
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.penis_health = None
        self.reproductive_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.penis_disease = None
        self.penis_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # traits
        self.penile_traits = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.penis_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Scrotum:
    def __init__(self):
        # function
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.scrotum_health = None
        self.testicular_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.scrotum_disease = None
        self.scrotum_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # traits
        self.scrotum_traits = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.scrotum_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Umbilical:
    def __init__(self):
        # structure
        self.cord_structure = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None

        # health
        self.umbilical_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.umbilical_disease = None
        self.umbilical_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # traits
        self.cord_traits = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.umbilical_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Abdominal:
    def __init__(self):
        # structure
        self.muscle_structure = None
        self.organ_placement = None
        self.fat_distribution = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None
        self.fat_production = None

        # health
        self.abdominal_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.abdominal_disease = None
        self.abdominal_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.abdominal_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Arm:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscular_strength = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.arm_circumference = None
        self.hormone_regulation = None

        # health

        self.arm_health = None
        self.muscle_health = None
        self.bone_health = None
        self.mass_strength = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.fungus = None
        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Axilla:
    def __init__(self):
        # structure
        self.armpit_traits = None
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strength = None
        self.sweat_gland = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.axilla_circumference = None
        self.hormone_regulation = None
        self.sweatgland_density = None

        # health

        self.axilla_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.fungus = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Back:
    def __init__(self):
        # structure
        self.spine_structure = None
        self.back_muscle = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None

        # health
        self.back_health = None
        self.spine_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.back_disease = None
        self.back_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.spinal_degeneration = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.back_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Belly:
    def __init__(self):
        # structure
        self.abdominal_structure = None
        self.fat_storage_tendency = None
        self.muscle_fat = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None
        self.core_strength = None

        # health
        self.ear_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.chest_disease = None
        self.chest_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Breast:
    def __init__(self):
        # structure
        self.nipple_structure = None
        self.breast_muscle = None
        self.breast_density = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.breast_tissue = None
        self.hormone_regulation = None

        # health
        self.breast_health = None
        self.nipple_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.breast_disease = None
        self.breast_disorder = None
        self.nipple_disease = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.nipple_development = None
        self.breast_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.nipple_size = None


class Chest:
    def __init__(self):
        # structure
        self.ribcage_structure = None
        self.wall_flexibility = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.lungs_capacity = None
        self.hormone_regulation = None

        # health
        self.chest_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.chest_disease = None
        self.chest_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.chest_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Elbow:
    def __init__(self):
        # structure
        self.elbow_structure = None
        self.range_of_motion = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None
        self.joint_functions = None

        # health
        self.elbow_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.elbow_disease = None
        self.elbow_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.elbow_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class FingerHand:
    def __init__(self):
        # structure
        self.nail_structure = None
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strenght = None
        self.fingerprints = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.finger_circumference = None
        self.hormone_regulation = None
        self.fingerjoint_mobility = None

        # health

        self.finger_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.fungus = None
        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class ForeArm:
    def __init__(self):
        # structure
        self.muscle_strength = None
        self.tendon_strength = None
        self.muscle_mass = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None
        self.joint_functions = None

        # health
        self.fore_arm_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.fore_arm_disease = None
        self.fore_arm_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.fore_arm_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Hand:
    def __init__(self):
        # structure
        self.hand_structure = None
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strenght = None
        self.hand_grip = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.finger_dexterity = None
        self.hormone_regulation = None
        self.palsweat_production = None

        # health

        self.hand_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.fungus = None
        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Neck:
    def __init__(self):
        # structure
        self.cervical_spine_structure = None
        self.neck_flexibility = None
        self.neck_muscle_strength = None
        self.neck_mobility = None

        # function
        self.growth_rate = None
        self.pain_perception = None
        self.hormone_regulation = None

        # health
        self.neck_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.neck_disease = None
        self.neck_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.neck_muscle_development = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Shoulder:
    def __init__(self):
        # structure
        self.shoulder_structure = None
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strenght = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.shoulder_circumference = None
        self.hormone_regulation = None
        self.range_of_motion = None
        self.muscle_development = None

        # health

        self.shoulder_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Ankle:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None

        # functions
        self.growth_rate = None
        self.pain_perception = None

        # health
        self.ankle_health = None
        self.bones_health = None

        # disease
        self.disorder = None
        self.genetic_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Buttock:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strength = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.buttock_circumference = None
        self.hormone_regulation = None

        # health

        self.buttock_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Calf:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.calf_circumference = None
        self.hormone_regulation = None

        # health
        self.calf_health = None
        self.bones_health = None
        self.muscle_health = None

        # disease
        self.disorder = None
        self.genetic_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class FingerFeet:
    def __init__(self):
        # structure
        self.nail_structure = None
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strength = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.finger_circumference = None
        self.hormone_regulation = None

        # health

        self.finger_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.fungus = None
        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Foot:
    def __init__(self):
        # structure
        self.foot_structure = None
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strength = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.foot_circumference = None
        self.hormone_regulation = None

        # health

        self.foot_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None
        self.fungus = None
        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Heel:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.heel_circumference = None
        self.hormone_regulation = None

        # health
        self.heel_health = None
        self.bones_health = None
        self.muscle_health = None

        # disease
        self.disorder = None
        self.genetic_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Hip:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None
        self.muscle_strength = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.hip_circumference = None
        self.hormone_regulation = None

        # health

        self.hip_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Knee:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.ligament_strength = None
        self.bones_density = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.knee_structure = None
        self.knee_circumference = None
        self.hormone_regulation = None

        # health

        self.knee_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.knee_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None


class Leg:
    def __init__(self):
        # structure
        self.bone_structure = None
        self.flexibility = None
        self.joint_stability = None
        self.bones_density = None
        self.muscle_strenght = None

        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.leg_circumference = None
        self.hormone_regulation = None

        # health
        self.leg_health = None
        self.muscle_health = None
        self.bone_health = None

        # diseases
        self.cancer = None
        self.muscle_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None

        # misc
        self.size = None
        self.shape = None
        self.strength = None
        self.age_factor = None
        self.hair = None


class Thigh:
    def __init__(self):
        # functions
        self.growth_rate = None
        self.pain_perception = None
        self.thigh_structure = None
        self.thigh_circumference = None
        self.hormone_regulation = None

        # health
        self.thigh_health = None
        self.skin_health = None
        self.muscle_health = None

        # disease
        self.cancer = None
        self.thigh_disease = None
        self.thigh_disorder = None
        self.genetic_disease = None
        self.susceptibility_disease = None
        self.allergies = None
        self.wound_density = None

        # recover
        self.resistance_genetic_disease = None
        self.wound_heal = None

        # adaptations
        self.environmental_adaptations = None

        # timeChart
        self.developmental_timing = None
        self.hormone_development = None

        # misc
        self.size = None
        self.shape = None
        self.age_factor = None
        self.strength = None
        self.hair = None


class DNA:
    def __init__(self):
        self.brain = Brain()  # Instantiate the Brain class within the DNA class
        self.heart = Heart()
        self.lungs = Lungs()
        self.liver = Liver()
        self.kidney = Kidney()
        self.intestine = Intestine()
        self.stomach = Stomach()
        self.pancreases = Pancreases()
        self.male_reproductive_organ = Male_Reproductive_Organ()
        self.female_reproductive_organ = Female_Reproductive_Organ()
        self.cheeks = Cheeks()
        self.ear = Ear()
        self.eye = Eye()
        self.eye_lashes = Eye_Lashes()
        self.eyebrows = Eyebrows()
        self.facial_hairs = Facial_Hairs()
        self.lip = Lip()
        self.nose = Nose()
        self.skin = Skin()
        self.teeth = Teeth()
        self.wrist = Wrist()
        self.vulva = Vulva()
        self.penis = Penis()
        self.scrotum = Scrotum()
        self.umbilical = Umbilical()
        self.abdominal = Abdominal()
        self.arm = Arm()
        self.axilla = Axilla()
        self.back = Back()
        self.belly = Belly()
        self.breast = Breast()
        self.chest = Chest()
        self.elbow = Elbow()
        self.finger_hand = FingerHand()
        self.fore_arm = ForeArm()
        self.hand = Hand()
        self.neck = Neck()
        self.shoulder = Shoulder()
        self.ankle = Ankle()
        self.buttock = Buttock()
        self.calf = Calf()
        self.finger_feet = FingerFeet()
        self.foot = Foot()

        self.heel = Heel()
        self.hip = Hip()
        self.knee = Knee()
        self.leg = Leg()
        self.thigh = Thigh()
    # ... Rest of the DNA class implementation



# Create an instance of the DNA class
Kumail = DNA()

Kumail.brain.iq = 113

print(Kumail.brain.iq)
