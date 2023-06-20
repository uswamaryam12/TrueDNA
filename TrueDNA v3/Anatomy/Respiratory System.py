class Respiration:
    def __init__(self):
        self.structure = self.Respiratory_Structure()
        self.functions = self.Respiratory_Functions()


    class Respiratory_Structure:
        def __init__(self):
            self.system = None

            self.external_nares = None
            self.nasal_septum = None
            self.nasal_conchae = None
            self.nasal_mucosa = None
            self.olfactory_epithelium = None


            self.nasopharynx = None
            self.oropharynx = None
            self.laryngopharnx = None

            self.epiglottis = None
            self.vocal_cord = None

            self.trachea = None

            self.main_bronchi = None
            self.bronchioles = None
            self.alveolar_ducts = None
            self.alveoli = None

            self.lobes = None
            self.pleura = None
            self.bronchopulmonary_segments = None

            self.diaphragm = None

        def nasal_cavity(self, external_nares, nasal_septum, nasal_conchae, nasal_mucosa, olfactory_epithelium):
            self.external_nares = external_nares
            self.nasal_septum = nasal_septum
            self.nasal_conchae = nasal_conchae
            self.nasal_mucosa = nasal_mucosa
            self.olfactory_epithelium = olfactory_epithelium


        def pharynx(self, nasopharynx, oropharynx, laryngopharnx):
            self.nasopharynx = nasopharynx
            self.oropharynx = oropharynx
            self.laryngopharnx = laryngopharnx

        def larynx(self, epiglottis, vocal_cord):
            self.epiglottis = epiglottis
            self.vocal_cord = vocal_cord


        def bronchial_tree(self, main_bronchi, bronchioles, alveolar_ducts, alveoli):
            self.main_bronchi = main_bronchi
            self.bronchioles = bronchioles
            self.alveolar_ducts = alveolar_ducts
            self.alveoli = alveoli

        def lungs(self, lobes, pleura, bronchopulmonary_segments):
            self.lobes = lobes
            self.pleura = pleura
            self.bronchopulmonary_segments = bronchopulmonary_segments


    class Respiratory_Functions:
        def __init__(self):
            self.functions = None

            self.diaphragmatic_contraction = None
            self.intercostal_muscle_action = None

            self.pulmonary_ventilation = None
            self.alveolar_capillary_diffusion = None

            self.hemoglobin_function = None

            self.bicarbonate_ion_formation = None
            self.red_blood_cell_carbonic_anhydrase = None

            self.brainstem_respiratory_centers = None
            self.chemoreceptor_sensitivity = None

            self.mucociliary_escalator = None
            self.cough_mechanism = None

            self.elastic_fibers = None
            self.surfactant_production = None

            self.mucosal_immunity = None
            self.alveolar_macrophages = None
            self.ciliary_escalator = None
            self.mucus_production = None

            self.cough_reflex = None
            self.sneezing_reflex = None


        def breathing(self, diaphragmatic_contraction, intercostal_muscle_action):
            self.diaphragmatic_contraction = diaphragmatic_contraction
            self.intercostal_muscle_action = intercostal_muscle_action

        def gas_exchange(self, pulmonary_ventilation, alveolar_capillary_diffusion):
            self.pulmonary_ventilation = pulmonary_ventilation
            self.alveolar_capillary_diffusion = alveolar_capillary_diffusion

        def oxygen_transportation(self, hemoglobin_function):
            self.hemoglobin_function = hemoglobin_function

        def carbon_dioxide_transportation(self, bicarbonate_ion_formation, red_blood_cell_carbonic_anhydrase):
            self.bicarbonate_ion_formation = bicarbonate_ion_formation
            self.red_blood_cell_carbonic_anhydrase = red_blood_cell_carbonic_anhydrase


        def respiratory_control(self, brainstem_respiratory_centers, chemoreceptor_sensitivity):
            self.brainstem_respiratory_centers = brainstem_respiratory_centers
            self.chemoreceptor_sensitivity = chemoreceptor_sensitivity

        def airway_clearance(self, mucociliary_escalator, cough_mechanism):
            self.mucociliary_escalator = mucociliary_escalator
            self.cough_mechanism = cough_mechanism

        def lung_compliance(self, elastic_fibers, surfactant_production):
            self.elastic_fibers = elastic_fibers
            self.surfactant_production = surfactant_production

        def pulmonary_defence(self, mucosal_immunity, alveolar_macrophages, ciliary_escalator, mucus_production):
            self.mucosal_immunity = mucosal_immunity
            self.alveolar_macrophages = alveolar_macrophages
            self.ciliary_escalator = ciliary_escalator
            self.mucus_production = mucus_production

        def respiratory_reflexes(self, cough_reflex, sneezing_reflex):
            self.cough_reflex = cough_reflex
            self.sneezing_reflex = sneezing_reflex