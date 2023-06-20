class Reproduction:
    def __init__(self):
        self.functions = self.Reproductive_functions()
        self.structure = self.Reproductive_Structure()

    class Reproductive_Structure:
        def __init__(self):
            self.system = None

            self.testes = None
            self.epididymis = None
            self.vas_deferens = None
            self.seminal_vasicles = None
            self.prostate_glands = None
            self.bulbourethral_glands = None
            self.penis = None
            self.scrotum = None

            self.ovaries = None
            self.fallopian_tubes = None
            self.uterus = None
            self.cervix = None
            self.vagina = None
            self.vulva = None

        def male_reproductive_organ(self, testes, epididymis, vas_deferens, seminal_vasicles, prostate_glands, bulbourethral_glands, penis, scrotum):
            self.testes = testes
            self.epididymis = epididymis
            self.vas_deferens = vas_deferens
            self.seminal_vasicles = seminal_vasicles
            self.prostate_glands = prostate_glands
            self.bulbourethral_glands = bulbourethral_glands
            self.penis = penis
            self.scrotum = scrotum

        def female_reproductive_organ(self, ovaries, fallopian_tubes, uterus, cervix, vagina, vulva):
            self.ovaries = ovaries
            self.fallopian_tubes = fallopian_tubes
            self.uterus = uterus
            self.cervix = cervix
            self.vagina = vagina
            self.vulva = vulva


    class Reproductive_functions:
        def __init__(self):
            self.system = None

            self.spermatogenesis = None
            self.oogenesis = None

            self.testosterone_production = None
            self.estrogen_production = None
            self.progesterone_production = None
            self.follicle_stimulating_hormone_production = None
            self.luteinizing_hormone_production = None

            self.sperm_oocyte_interaction = None

            self.blastocyte_formation = None
            self.gastrulation = None
            self.organogenesis = None

            self.implantation = None
            self.placenta_development = None
            self.embryonic_development = None
            self.fetal_development = None

            self.uterine_contraction = None
            self.cervical_dilation = None
            self.fetus_expulsion = None

            self.follicular_phase = None
            self.ovulation = None
            self.luteal_phase = None
            self.menstruation = None

            self.hormonal_change = None
            self.ovarian_function_decline = None

            self.sperm_production = None
            self.egg_production = None
            self.sperm_maturation = None

        def gametogenesis(self, spermatogenesis, oogenesis):
            self.spermatogenesis = spermatogenesis
            self.oogenesis = oogenesis

        def hormone_production(self, testosterone_production, estrogen_production, progesterone_production, follicle_stimulating_hormone_production, luteinizing_hormone_production):
            self.testosterone_production = testosterone_production
            self.estrogen_production = estrogen_production
            self.progesterone_production = progesterone_production
            self.follicle_stimulating_hormone_production = follicle_stimulating_hormone_production
            self.luteinizing_hormone_production = luteinizing_hormone_production

        def fertilization(self, sperm_oocyte_interaction):
            self.sperm_oocyte_interaction = sperm_oocyte_interaction


        def embryonic_development(self, blastocyte_formation, gastrulation, organogenesis):
            self.blastocyte_formation = blastocyte_formation
            self.gastrulation = gastrulation
            self.organogenesis = organogenesis

        def pregrency(self, implantation, placenta_development, embryonic_development, fetal_development):
            self.implantation = implantation
            self.placenta_development = placenta_development
            self.embryonic_development = embryonic_development
            self.fetal_development = fetal_development

        def labor_delivery(self, uterine_contraction, cervical_dilation, fetus_expulsion):
            self.uterine_contraction = uterine_contraction
            self.cervical_dilation = cervical_dilation
            self.fetus_expulsion = fetus_expulsion

        def menstruation_cycle(self, follicular_phase, ovulation, luteal_phase, menstruation):
            self.follicular_phase = follicular_phase
            self.ovulation = ovulation
            self.luteal_phase = luteal_phase
            self.menstruation = menstruation

        def menopause(self, hormonal_change, ovarian_function_decline):
            self.hormonal_change = hormonal_change
            self.ovarian_function_decline = ovarian_function_decline

        def gametes_production(self, sperm_production, sperm_maturation, egg_production):
            self.sperm_production = sperm_production
            self.egg_production = egg_production
            self.sperm_maturation = sperm_maturation