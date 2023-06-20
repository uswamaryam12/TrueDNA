class Urinary:
    def __init__(self):
        self.structure = self.Urinary_Structure()
        self.functions = self.Urinary_Functions()

    class Urinary_Structure:
        def __init__(self):
            self.system = None

            self.kidney = None
            self.ureters = None
            self.urinary_bladder = None
            self.urethra = None

    class Urinary_Functions:
        def __init__(self):
            self.system = None

            self.glomerular_filtration = None
            self.tubular_reabsorption = None
            self.tubular_secretion = None

            self.nephron_function = None
            self.renal_blood_flow = None
            self.fluid_balance = None

            self.ureter_peristalsis = None
            self.bladder_contraction = None
            self.urination = None

            self.sodium_balance = None
            self.potassium_balance = None
            self.calcium_balance = None
            self.phosphate_balance = None

            self.renal_tubular_acidosis = None
            self.metabolic_alkalosis = None
            self.respiratory_acidosis = None

            self.mucus_secretion = None
            self.urine_flow = None
            self.antimicrobial_peptides = None


        def filtration(self, glomerular_filtration, tubular_reabsorption, tubular_secretion):
            self.glomerular_filtration = glomerular_filtration
            self.tubular_reabsorption = tubular_reabsorption
            self.tubular_secretion = tubular_secretion

        def urine_formation(self, nephron_function, renal_blood_flow, fluid_balance):
            self.nephron_function = nephron_function
            self.renal_blood_flow = renal_blood_flow
            self.fluid_balance = fluid_balance

        def urinary_transport(self, ureter_peristalsis, bladder_contraction, urination):
            self.ureter_peristalsis = ureter_peristalsis
            self.bladder_contraction = bladder_contraction
            self.urination = urination

        def electrolyte_balance(self, sodium_balance, potassium_balance, calcium_balance, phosphate_balance):
            self.sodium_balance = sodium_balance
            self.potassium_balance = potassium_balance
            self.calcium_balance = calcium_balance
            self.phosphate_balance = phosphate_balance

        def acid_base_balance(self, renal_tubular_acidosis, metabolic_alkalosis, respiratory_acidosis):
            self.renal_tubular_acidosis = renal_tubular_acidosis
            self.metabolic_alkalosis = metabolic_alkalosis
            self.respiratory_acidosis = respiratory_acidosis

        def urinary_tract_defence(self, mucus_secretion, urine_flow, antimicrobial_peptides):
            self.mucus_secretion = mucus_secretion
            self.urine_flow = urine_flow
            self.antimicrobial_peptides = antimicrobial_peptides