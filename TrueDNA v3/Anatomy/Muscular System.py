class Muscular:
    def __init__(self):
        self.structure = self.Muscular_Structure()
        self.functions = self.Muscular_Functions()

    class Muscular_Structure:
        def __init__(self):
            self.system = None

            self.head_muscle = None
            self.neck_muscle = None
            self.upper_limb_muscle = None
            self.lower_limb_muscle = None
            self.trunk_muscle = None

            self.digestive_muscle = None
            self.respiratory_muscle = None
            self.blood_vessels_muscle = None
            self.reproductive_muscle = None

            self.cardiac_muscle = None

        def skeletal_muscle(self, head_muscle, neck_muscle, upper_limb_muscle, lower_limb_muscle, trunk_muscle):
            self.head_muscle = head_muscle
            self.neck_muscle = neck_muscle
            self.upper_limb_muscle = upper_limb_muscle
            self.lower_limb_muscle = lower_limb_muscle
            self.trunk_muscle = trunk_muscle

        def smooth_muscle(self, digestive_muscle, respiratory_muscle, blood_vessels_muscle, reproductive_muscle):
            self.digestive_muscle = digestive_muscle
            self.respiratory_muscle = respiratory_muscle
            self.blood_vessels_muscle = blood_vessels_muscle
            self.reproductive_muscle = reproductive_muscle

    class Muscular_Functions:
        def __init__(self):
            self.system = None

            self.myogenesis = None
            self.muscle_fiber_formation = None

            self.actin = None
            self.myosin = None
            self.troponin = None
            self.tropomyosin = None

            self.atp_synthesis = None
            self.glycolysis = None
            self.oxidative_phosphorylation = None

            self.type_1_fibers = None
            self.type_2_fibers = None

            self.satellite_cell = None
            self.myostatin = None
            self.insulin = None

            self.muscle_motor_recruitment = None
            self.muscle_synergies = None

            self.muscular_dystrophy = None
            self.myasthenia_gravis = None
            self.rhabdomyolysis = None


        def muscle_development(self, myogenesis, muscle_fiber_formation):
            self.myogenesis = myogenesis
            self.muscle_fiber_formation = muscle_fiber_formation

        def muscle_contraction(self, actin, myosin, troponin, tropomyosin):
            self.actin = actin
            self.myosin = myosin
            self.troponin = troponin
            self.tropomyosin = tropomyosin

        def energy_metabolism(self, atp_synthesis, glycolysis, oxidative_phosphorylation):
            self.atp_synthesis = atp_synthesis
            self.glycolysis = glycolysis
            self.oxidative_phosphorylation = oxidative_phosphorylation

        def muscle_fiber(self, type_1_fibers, type_2_fibers):
            self.type_1_fibers = type_1_fibers
            self.type_2_fibers = type_2_fibers

        def muscle_growth(self, satellite_cell, myostatin, insulin):
            self.satellite_cell = satellite_cell
            self.myostatin = myostatin
            self.insulin = insulin

        def muscle_coordination(self, muscle_motor_recruitment, muscle_synergies):
            self.muscle_motor_recruitment = muscle_motor_recruitment
            self.muscle_synergies = muscle_synergies

        def muscle_disorder(self, muscular_dystrophy, myasthenia_gravis, rhabdomyolysis):
            self.muscular_dystrophy = muscular_dystrophy
            self.myasthenia_gravis = myasthenia_gravis
            self.rhabdomyolysis = rhabdomyolysis