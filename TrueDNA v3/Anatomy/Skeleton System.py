class Skeleton:
    def __init__(self):
        self.structure = self.Skeletal_Structure()
        self.functions = self.Skeletal_Functions()

    class Skeletal_Structure:
        def __init__(self):
            self.system = None

            #  Skull
            self.frontal_bone = None
            self.parietal_bone = None
            self.temporal_bone = None
            self.occipital_bone = None
            self.mandible = None

            # Spine
            self.cervical_vertebrae = None
            self.thoracic_vertebrae = None
            self.lumbar_vertebrae = None
            self.spine_sacrum = None
            self.spine_coccyx = None

            # Rib_Cage
            self.true_ribs = None
            self.false_ribs = None
            self.floating_ribs = None

            # Sternum
            self.manubrium = None
            self.body = None
            self.xiphoid_process = None

            # Upper_Limb
            self.clavicle = None
            self.scapula = None
            self.humerus = None
            self.radius = None
            self.ulna = None
            self.carpals = None
            self.metacarpals = None
            self.upper_phalangus = None

            # Lower_Limb
            self.femur = None
            self.patella = None
            self.tibia = None
            self.fibula = None
            self.tarsals = None
            self.metatarsals = None
            self.lower_phalangus = None

            # Pelvic_Girdle
            self.hip_bone = None
            self.pelvic_sacrum = None
            self.pelvic_coccyx = None


        def skull(self, frontal_bone, parietal_bone,temporal_bone, occipital_bone, mandible):

            self.frontal_bone = frontal_bone
            self.parietal_bone = parietal_bone
            self.temporal_bone = temporal_bone
            self.occipital_bone = occipital_bone
            self.mandible = mandible

        def spine(self,cervical_vertebrae, thoracic_vertebrae, lumbar_vertebrae, spine_sacrum, spine_coccyx):
            self.cervical_vertebrae = cervical_vertebrae
            self.thoracic_vertebrae = thoracic_vertebrae
            self.lumbar_vertebrae = lumbar_vertebrae
            self.sacrum = spine_sacrum
            self.coccyx = spine_coccyx

        def rib_cage(self, true_ribs, false_ribs, floating_ribs):
            self.true_ribs = true_ribs
            self.false_ribs = false_ribs
            self.floating_ribs = floating_ribs

        def sternum(self, manubrium, body, xiphoid_process):
            self.manubrium = manubrium
            self.body = body
            self.xiphoid_process = xiphoid_process


        def upper_limb(self, clavicle, scapula, humerus, radius, ulna, carpals, metacarpals, upper_phalangus):
            self.clavicle = clavicle
            self.scapula = scapula
            self.humerus = humerus
            self.radius = radius
            self.ulna = ulna
            self.carpals = carpals
            self.metacarpals = metacarpals
            self.upper_phalangus = upper_phalangus

        def lower_limb(self, femur, patella, tibia, fibula, tarsals, metatarsals, lower_phalangus):
            self.femur = femur
            self.patella = patella
            self.tibia = tibia
            self.fibula = fibula
            self.tarsals = tarsals
            self.metatarsals = metatarsals
            self.lower_phalangus = lower_phalangus

        def pelvic_girdle(self, hip_bone, pelvic_sacrum, pelvic_coccyx):
            self.hip_bone = hip_bone
            self.pelvic_sacrum = pelvic_sacrum
            self.pelvic_coccyx = pelvic_coccyx


    class Skeletal_Functions:
        def __init__(self):
            self.functions = None

            self.osteogenesis = None

            self.collagen_production = None
            self.mineralization = None

            self.osteoclast_activity = None
            self.osteoblast_activity = None

            self.synovial_fluid_production = None
            self.cartilage_maintenance = None
            self.ligament_strength = None
            self.tendon_elasticity = None

            self.endochondral_ossification = None
            self.intramembranous = None
            self.ossification = None

            self.fracture_healing = None
            self.cartilage_regeneration = None

            self.calcium_metabolism = None
            self.vitaminD_receptor = None
            self.hormonal_regulation = None

            self.collagen_crosslinking = None
            self.mineral_composition = None


        def bone_formation(self, osteogenesis):
            self.osteogenesis = osteogenesis

        def bone_structure(self, collagen_production, mineralization):
            self.collagen_production = collagen_production
            self.mineralization = mineralization

        def bone_remodeling(self,osteoclast_activity, osteoblast_activity):
            self.osteoclast_activity = osteoclast_activity
            self.osteoblast_activity = osteoblast_activity

        def joint_functions(self, synovial_fluid_production, cartilage_maintenance, ligament_strength, tendon_elasticity):
            self.synovial_fluid_production = synovial_fluid_production
            self.cartilage_maintenance = cartilage_maintenance
            self.ligament_strength = ligament_strength
            self.tendon_elasticity = tendon_elasticity

        def skeletal_growth(self, endochondral_ossification, intramembranous, ossification):
            self.endochondral_ossification = endochondral_ossification
            self.intramembranous = intramembranous
            self.ossification = ossification

        def bone_repair(self, fracture_healing, cartilage_regeneration):
            self.fracture_healing = fracture_healing
            self.cartilage_regeneration = cartilage_regeneration

        def bone_density(self, calcium_metabolism, vitaminD_receptor, hormonal_regulation):
            self.calcium_metabolism = calcium_metabolism
            self.vitaminD_receptor = vitaminD_receptor
            self.hormonal_regulation = hormonal_regulation

        def bone_strength(self, collagen_crosslinking, mineral_composition):
            self.collagen_crosslinking = collagen_crosslinking
            self.mineral_composition = mineral_composition
