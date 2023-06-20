class Digestion:
    def __inti__(self):
        self.structure = self.Digestive_Structure()
        self.functions = self.Digestive_Functions()

    class Digestive_Structure:
        def __init__(self):
            self.system = None

            self.teeth = None
            self.tongue = None
            self.salivary_glands = None

            self.pharynx = None
            self.esophagus = None
            self.stomach = None
            self.liver = None
            self.gallbladder = None
            self.pancreases = None

            self.cardiac_region = None
            self.fundas = None
            self.body = None
            self.pylorus = None

            self.dudenum = None
            self.jejunum = None
            self.ileum = None

            self.cecum = None
            self.ascending_colon = None
            self.descending_colon = None
            self.transverse_colon = None
            self.sigmoid_colon = None
            self.rectum = None
            self.anus = None

        def oral_cavity(self, teeth, tongue, salivary_glands):
            self.teeth = teeth
            self.tongue = tongue
            self.salivary_glands = salivary_glands

        def stomach(self, cardiac_region, fundas, body, pylorus):
            self.cardiac_region = cardiac_region
            self.fundas = fundas
            self.body = body
            self.pylorus = pylorus

        def small_intestine(self, dudenum, jejunum, ileum):
            self.dudenum = dudenum
            self.jejunum = jejunum
            self.ileum = ileum

        def large_intestine(self, cecum, ascending_colon, descending_colon, transverse_colon, sigmoid_colon, rectum, anus):
            self.cecum = cecum
            self.ascending_colon = ascending_colon
            self.descending_colon = descending_colon
            self.transverse_colon = transverse_colon
            self.sigmoid_colon = sigmoid_colon
            self.rectum = rectum
            self.anus = anus



    class Digestive_Functions:
        def __init__(self):
            self.system = None

            self.enzymatic_digestion = None
            self.mechanic_digestion = None

            self.nutrient_absorption = None
            self.water_absorption = None
            self.bacterial_fermentation = None

            self.gastric_acid_secretion = None
            self.enzyme_secretion = None
            self.bicarbonate_secretion = None

            self.peristalsis = None
            self.segmentation = None

            self.gastric_emptying = None
            self.gastric_acid_regulation = None

            self.detoxification = None
            self.bile_production = None

            self.bile_storage = None
            self.bile_release = None


        def digestion(self, enzymatic_digestion, mechanic_digestion):
            self.enzymatic_digestion = enzymatic_digestion
            self.mechanic_digestion = mechanic_digestion

        def intestinal_functions(self, nutrient_absorption, water_absorption, bacterial_fermentation):
            self.nutrient_absorption = nutrient_absorption
            self.water_absorption = water_absorption
            self.bacterial_fermentation = bacterial_fermentation

        def motility(self, peristalsis, segmentation):
            self.peristalsis = peristalsis
            self.segmentation = segmentation

        def gastric_functions(self, gastric_emptying, gastric_acid_regulation):
            self.gastric_emptying = gastric_emptying
            self.gastric_acid_regulation = gastric_acid_regulation

        def liver_functions(self, detoxification, bile_production):
            self.detoxification = detoxification
            self.bile_production = bile_production

        def pancreatic_functions(self, gastric_acid_secretion, enzyme_secretion, bicarbonate_secretion):
            self.gastric_acid_secretion = gastric_acid_secretion
            self.enzyme_secretion = enzyme_secretion
            self.bicarbonate_secretion = bicarbonate_secretion

        def gallbladder_functions(self, bile_storage, bile_release):
            self.bile_storage = bile_storage
            self.bile_release = bile_release
