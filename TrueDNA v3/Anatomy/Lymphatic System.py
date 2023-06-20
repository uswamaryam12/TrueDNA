class Lymphatic:
    def __init__(self):
        self.structure = self.Lymphatic_Structure()
        self.functions = self.Lymphatic_Functions()


    class Lymphatic_Structure:
        def __init__(self):
            self.system = None

            self.lymphatic_vessels = None
            self.lymph_nodes = None
            self.tonsils = None
            self.spleen = None
            self.thymus = None
            self.bone_marrow = None


    class Lymphatic_Functions:
        def __init__(self):
            self.system = None

            self.b_cell_development = None
            self.t_cell_development = None
            self.natural_killer_cell_development = None

            self.cortex = None
            self.medulla = None
            self.sinuses = None

            self.lymph_flow = None
            self.lymphatic_drainage = None

            self.antigen_recognition = None
            self.antibody_production = None
            self.cell_mediated_immunity = None
            self.inflammation = None

            self.lymph_node_filtration = None
            self.spleen_filtration = None

            self.chemotaxis = None
            self.homing = None

            self.interstitial_fluid_drainage = None
            self.fat_absorption = None

            self.thymus = None
            self.tonsils = None
            self.spleen = None

        def lymphocyte_production(self, b_cell_development, t_cell_development, natural_killer_cell_development):
            self.b_cell_development = b_cell_development
            self.t_cell_development = t_cell_development
            self.natural_killer_cell_development = natural_killer_cell_development

        def lymph_node(self, cortex, medulla, sinuses):
            self.cortex = cortex
            self.medulla = medulla
            self.sinuses = sinuses

        def lymphatic_vessels(self, lymph_flow, lymphatic_drainage):
            self.lymph_flow = lymph_flow
            self.lymphatic_drainage = lymphatic_drainage

        def immune_response(self, antigen_recognition, antibody_production, cell_mediated_immunity, inflammation):
            self.antigen_recognition = antigen_recognition
            self.antibody_production = antibody_production
            self.cell_mediated_immunity = cell_mediated_immunity
            self.inflammation = inflammation

        def lymphatic_filtration(self, lymph_node_filtration, spleen_filtration):
            self.lymph_node_filtration = lymph_node_filtration
            self.spleen_filtration = spleen_filtration

        def immune_cell_migration(self, chemotaxis, homing):
            self.chemotaxis = chemotaxis
            self.homing = homing

        def lymphatic_transport(self, interstitial_fluid_drainage, fat_absorption):
            self.interstitial_fluid_drainage = interstitial_fluid_drainage
            self.fat_absorption = fat_absorption


        def lymphoid_organs(self, thymus, tonsils, spleen):
            self.thymus = thymus
            self.tonsils = tonsils
            self.spleen = spleen