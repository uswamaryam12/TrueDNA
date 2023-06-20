class Integumentary:
    def __init__(self):
        self.structure = self.Integumentary_Structure()
        self.functions = self.Integumentary_Functions()

    class Integumentary_Structure:
        def __init__(self):
            self.system = None

            self.dermis = None
            self.epidermis = None
            self.hypodermis = None

            self.hair_shaft = None
            self.hair_follicle = None

            self.nail_plate = None
            self.nail_bed = None
            self.nail_matrix = None

            self.eccrine_sweat_glands = None
            self.epocrine_sweat_glands = None

            self.sebaceous_glands = None

        def skin(self, dermis, epidermis, hypodermis):
            self.dermis = dermis
            self.epidermis = epidermis
            self.hypodermis = hypodermis


        def hairs(self, hair_shaft, hair_follicle):
            self.hair_shaft = hair_shaft
            self.hair_follicle = hair_follicle


        def nails(self, nail_plate, nail_bed, nail_matrix):
            self.nail_plate = nail_plate
            self.nail_bed = nail_bed
            self.nail_matrix = nail_matrix

        def sweat_glands(self, eccrine_sweat_glands, epocrine_sweat_glands):
            self.eccrine_sweat_glands = eccrine_sweat_glands
            self.epocrine_sweat_glands = epocrine_sweat_glands


    class Integumentary_Functions:
        def __init__(self):
            self.system = None

            self.epidermal_differentiation = None
            self.hair_follicle_development = None

            self.epidermal_barrier_formation = None
            self.stratum_corneum_maintenance = None

            self.melanogenesis = None
            self.pigment_transport = None
            self.pigment_distribution = None

            self.sweat_production = None
            self.sweat_secretion = None
            self.thermoregulation = None

            self.sebum_production = None
            self.sebum_secretion = None
            self.skin_moisture_regulation = None

            self.inflammatory_response = None
            self.granulation_tissue_formation = None
            self.epithelialization = None

            self.hair_follicle_cycling = None
            self.keratin_formation = None
            self.keratin_differentiation = None

            self.nail_matrix_function = None
            self.nail_plate_formation = None

            self.eczema = None
            self.acne = None
            self.psoriasis = None

        def skin_development(self, epidermal_differentiation, hair_follicle_development):
            self.epidermal_differentiation = epidermal_differentiation
            self.hair_follicle_development = hair_follicle_development

        def skin_barrier(self, epidermal_barrier_formation, stratum_corneum_maintenance):
            self.epidermal_barrier_formation = epidermal_barrier_formation
            self.stratum_corneum_maintenance = stratum_corneum_maintenance

        def pigmentation(self, melanogenesis, pigment_transport, pigment_distribution):
            self.melanogenesis = melanogenesis
            self.pigment_transport = pigment_transport
            self.pigment_distribution = pigment_distribution

        def sweat_glands(self, sweat_production, sweat_secretion, thermoregulation):
            self.sweat_production = sweat_production
            self.sweat_secretion = sweat_secretion
            self.thermoregulation = thermoregulation

        def sebaceous_glands(self, sebum_production, sebum_secretion, skin_moisture_regulation):
            self.sebum_production = sebum_production
            self.sebum_secretion = sebum_secretion
            self.skin_moisture_regulation = skin_moisture_regulation

        def wound_healing(self, inflammatory_response, granulation_tissue_formation, epithelialization):
            self.inflammatory_response = inflammatory_response
            self.granulation_tissue_formation = granulation_tissue_formation
            self.epithelialization = epithelialization

        def hair_growth(self, hair_follicle_cycling, keratin_formation, keratin_differentiation):
            self.hair_follicle_cycling = hair_follicle_cycling
            self.keratin_formation = keratin_formation
            self.keratin_differentiation = keratin_differentiation

        def nail_growth(self, nail_matrix_function, nail_plate_formation):
            self.nail_matrix_function = nail_matrix_function
            self.nail_plate_formation = nail_plate_formation

        def skin_disorders(self, eczema, acne, psoriasis):
            self.eczema = eczema
            self.acne = acne
            self.psoriasis = psoriasis