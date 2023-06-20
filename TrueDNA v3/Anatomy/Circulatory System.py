class Circulation:
    def __init__(self):
        self.structure = self.Circulatory_Structure()
        self.functions = self.Circulatory_Functions()


    class Circulatory_Structure:
        def __init__(self):
            self.system = None

            self.heart = None

            self.aorta = None
            self.pulmonary_arteries = None
            self.coronary_arteries = None

            self.superior_vena_cava = None
            self.inferior_vena_cava = None
            self.pulmonary_veins = None
            self.coronary_sinus = None

            self.capillaries = None

            self.red_blood_cells = None
            self.white_blood_cells = None
            self.platelets = None

        def arteries(self, aorta, pulmonary_arteries, coronary_arteries):
            self.aorta = aorta
            self.pulmonary_arteries = pulmonary_arteries
            self.coronary_arteries = coronary_arteries

        def veins(self, superior_vena_cava, inferior_vena_cava, pulmonary_veins, coronary_sinus):
            self.superior_vena_cava = superior_vena_cava
            self.inferior_vena_cava = inferior_vena_cava
            self.pulmonary_veins = pulmonary_veins
            self.coronary_sinus = coronary_sinus

        def blood(self, red_blood_cells, white_blood_cells, platelets):
            self.red_blood_cells = red_blood_cells
            self.white_blood_cells = white_blood_cells
            self.platelets = platelets

    class Circulatory_Functions:
        def __init__(self):
            self.system = None

            self.cardiac_muscle = None
            self.conduction_system = None

            self.arteries = None
            self.veins = None
            self.capillaries = None

            self.erythropoiesis = None
            self.leukopoiesis = None
            self.thrombopoiesis = None

            self.red_blood_cells = None
            self.white_blood_cells = None
            self.platelets = None

            self.plasma = None
            self.proteins = None
            self.electrolytes = None

            self.coagulation_factor = None
            self.fibrinogen = None
            self.platelet_aggregation = None

            self.renin_angiotensin_system = None
            self.baroreceptor_reflex = None

            self.oxygen_transport = None
            self.hemoglobin = None

            self.insulin = None
            self.glucagon = None

        def heart_functions(self, cardiac_muscle, conduction_system):
            self.cardiac_muscle = cardiac_muscle
            self.conduction_system = conduction_system

        def blood_vessels_structure(self, arteries, veins, capillaries):
            self.arteries = arteries
            self.veins = veins
            self.capillaries = capillaries

        def blood_cell_production(self, erythropoiesis, leukopoiesis, thrombopoiesis):
            self.erythropoiesis = erythropoiesis
            self.leukopoiesis = leukopoiesis
            self.thrombopoiesis = thrombopoiesis

        def blood_cell_types(self, red_blood_cells, white_blood_cells, platelets):
            self.red_blood_cells = red_blood_cells
            self.white_blood_cells = white_blood_cells
            self.platelets = platelets

        def blood_composition(self, plasma, proteins, electrolytes):
            self.plasma = plasma
            self.proteins = proteins
            self.electrolytes = electrolytes

        def blood_clotting(self, coagulation_factor, fibrinogen, platelet_aggregation):
            self.coagulation_factor = coagulation_factor
            self.fibrinogen = fibrinogen
            self.platelet_aggregation = platelet_aggregation

        def blood_pressure_regulation(self, renin_angiotensin_system, baroreceptor_reflex):
            self.renin_angiotensin_system = renin_angiotensin_system
            self.baroreceptor_reflex = baroreceptor_reflex

        def blood_oxygenation(self, oxygen_transport, hemoglobin):
            self.oxygen_transport = oxygen_transport
            self.hemoglobin = hemoglobin

        def blood_sugar_regulation(self, insulin, glucagon):
            self.insulin = insulin
            self.glucagon = glucagon
