class Nervous:
    def __init__(self):
        self.structure = self.Nervous_Structure()
        self.functions = self.Nervous_Functions()

    class Nervous_Structure:
        def __init__(self):
            self.system = None

            self.brain = None
            self.spinal_cord = None

            self.cranial_nerves = None
            self.spinal_nerves = None
            self.autonomic_nerves = None

            self.photoreceptors = None
            self.thermoreceptors = None
            self.mechanoreceptors = None
            self.chemoreceptors = None
            self.nociceptors = None

            self.motor_neurons = None
            self.sensory_neurons = None
            self.interneurons = None

            self.dopamine = None
            self.serotonin = None
            self.acetylcholine = None
            self.gaba = None
            self.glutomate = None

        def central_nervous_system(self, brain, spinal_cord):
            self.brain = brain
            self.spinal_cord = spinal_cord

        def peripheral_nervous_system(self, cranial_nerves, spinal_nerves, autonomic_nerves):
            self.cranial_nerves = cranial_nerves
            self.spinal_nerves = spinal_nerves
            self.autonomic_nerves = autonomic_nerves

        def sensory_receptors(self, photoreceptors, thermoreceptors, mechanoreceptors,chemoreceptors, nociceptors):
            self.photoreceptors = photoreceptors
            self.thermoreceptors = thermoreceptors
            self.mechanoreceptors = mechanoreceptors
            self.chemoreceptors = chemoreceptors
            self.nociceptors = nociceptors

        def neurons(self, motor_neurons, sensory_neurons, interneurons):
            self.motor_neurons = motor_neurons
            self.sensory_neurons = sensory_neurons
            self.interneurons = interneurons

        def neurotransmitters(self, dopamine, serotonin, acetylcholine, gaba, glutomate):
            self.dopamine = dopamine
            self.serotonin = serotonin
            self.acetylcholine = acetylcholine
            self.gaba = gaba
            self.glutomate = glutomate



    class Nervous_Functions:
        def __init__(self):
            self.system = None

            self.neurogenesis = None
            self.axon_guidance = None
            self.synaptogenesis = None

            self.dopamine = None
            self.serotonin = None
            self.acetylcholine = None
            self.gaba = None
            self.glutomate = None

            self.action_potential = None
            self.synaptic_vesicle_release = None
            self.neurotransmitter_binding = None

            self.neural_connectivity = None
            self.synaptic_plasticity = None
            self.neural_network_formation = None

            self.vision = None
            self.hearing = None
            self.touch = None
            self.taste = None
            self.smell = None

            self.voluntary_movements = None
            self.reflexes = None
            self.balance = None
            self.coordination = None

            self.memory = None
            self.attention = None
            self.learning = None
            self.language = None
            self.problem_solving = None

            self.alzheimer_disease = None
            self.parkinson_disease = None
            self.multiple_sclerosis = None
            self.epilepsy = None


        def neuron_development(self, neurogenesis, axon_guidance, synaptogenesis):
            self.neurogenesis = neurogenesis
            self.axon_guidance = axon_guidance
            self.synaptogenesis = synaptogenesis

        def neurotransmitters(self, dopamine, serotonin, acetylcholine, gaba, glutomate):
            self.dopamine = dopamine
            self.serotonin = serotonin
            self.acetylcholine = acetylcholine
            self.gaba = gaba
            self.glutomate = glutomate

        def synaptic_transmission(self, action_potential, synaptic_vesicle_release, neurotransmitter_binding):
            self.action_potential = action_potential
            self.synaptic_vesicle_release = synaptic_vesicle_release
            self.neurotransmitter_binding = neurotransmitter_binding

        def neural_circuit_formation(self, neural_connectivity, synaptic_plasticity, neural_network_formation):
            self.neural_connectivity = neural_connectivity
            self.synaptic_plasticity = synaptic_plasticity
            self.neural_network_formation = neural_network_formation

        def sensory_processing(self, vision, hearing, touch, taste,smell):
            self.vision = vision
            self.hearing = hearing
            self.touch = touch
            self.taste = taste
            self.smell = smell

        def motor_control(self, voluntary_movements, reflexes, balance, coordination):
            self.voluntary_movements = voluntary_movements
            self.reflexes = reflexes
            self.balance = balance
            self.coordination = coordination

        def cognitive_functions(self, memory, attention, learning, language, problem_solving):
            self.memory = memory
            self.attention = attention
            self.learning = learning
            self.language = language
            self.problem_solving = problem_solving

        def neurological_disorders(self, alzheimer_disease, parkinson_disease, multiple_sclerosis, epilepsy):
            self.alzheimer_disease = alzheimer_disease
            self.parkinson_disease = parkinson_disease
            self.multiple_sclerosis = multiple_sclerosis
            self.epilepsy = epilepsy
