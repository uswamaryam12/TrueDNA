def Heart(emotions, functions, traits, health, disease, adaptations, timeChart, recover, misc):

    #emotions
    emotion = None
    emotions_level = None

    #functions
    heart_rate = None
    heart_muscle = None
    pain_perception = None
    blood_pressure_regulation = None
    blood_speed = None

    #traits
    personality_traits = None
    behavioural_traits = None
    reproductive_traits = None
    feeling_traits = None

    #health
    heart_health = None
    emotion_health = None
    cardiovascular_health = None

    #disease
    cancer = None
    failure = None
    cardiovascular_disorder = None

    #adaptations
    environmental_adaptation = None

    #timeChart
    developmental_timing = None
    emotions_formation = None

    #recover
    recover_timing = None
    healing_power = None

    #misc
    age_factor = None
    strength = None
    shape = None
    size = None
    disability = None

    emotions = [age_factor, strength, emotion, emotions_level]
    functions = [age_factor, strength, heart_rate, heart_muscle, pain_perception,blood_speed, blood_pressure_regulation]
    traits = [personality_traits, behavioural_traits, reproductive_traits, feeling_traits]
    health = [age_factor, strength, heart_health, emotion_health, cardiovascular_health]
    disease = [age_factor, strength, cancer, failure, cardiovascular_disorder]
    adaptations = [age_factor, strength, environmental_adaptation]
    timeChart = [developmental_timing, emotions_formation]
    recover = [age_factor, strength, recover_timing, healing_power]
    misc = [age_factor, strength, shape, size, disability]