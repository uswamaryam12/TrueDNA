def Brain(intelligence, functions, health, disease, recover,traits, adaptations,timeChart, misc):

    #intelligence
    iq = None
    mentality_level = None

    #traits
    personality_traits = None
    behavioural_traits = None
    reproductive_traits = None

    #health
    brain_health = None
    mental_health = None

    #disease
    cancer = None
    tumor = None
    neurological_disorder = None

    #functions
    cell_signalling = None
    sleep_regulation = None
    cognitive_ability = None
    pain_perception = None
    neural_transmitter_regulator = None

    #adaptations
    environmental_adaptation = None

    #recover
    recover_timing = None
    healing_power = None

    #timingChart
    developmental_timing = None
    memory_formation = None

    #misc
    strength = None
    stress_rate = None
    age_factor = None
    disability = None
    shape = None
    size = None

    intelligence = [age_factor, strength, iq, mentality_level]
    functions = [age_factor, strength, cell_signalling, sleep_regulation,cognitive_ability, pain_perception, neural_transmitter_regulator]
    adaptations = [age_factor, strength, environmental_adaptation]
    health = [age_factor, strength, brain_health, mental_health, stress_rate]
    disease = [age_factor, strength, cancer, tumor, stress_rate, neurological_disorder]
    traits = [personality_traits, behavioural_traits, reproductive_traits]
    recover = [age_factor, strength, recover_timing, healing_power]
    timeChart = [developmental_timing, memory_formation]
    misc = [age_factor, strength, disability, stress_rate, shape, size]