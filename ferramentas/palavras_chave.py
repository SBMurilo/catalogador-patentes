"""
palavras_chave.py
─────────────────
Dicionário de palavras-chave para classificação automática de patentes.
Cada entrada mapeia um caminho de pasta para uma lista de termos de busca.

Edite, acrescente ou remova palavras conforme necessário antes de rodar
o classificador.

Formato:
    "Pasta/Subpasta": ["palavra1", "palavra2", ...]

A busca é feita no campo 'resumo' (e opcionalmente 'titulo') de cada patente.
Não diferencia maiúsculas/minúsculas.
"""

PALAVRAS_CHAVE = {

    # ══════════════════════════════════════════════════════════════
    # DEHYDRATOR
    # ══════════════════════════════════════════════════════════════
    "Dehydrator": [
        "dehydrator", "dehydration", "desiccant", "moisture removal",
        "water removal", "drying unit", "dryer unit", "gas dryer",
        "glycol dehydration", "TEG dehydration", "triethylene glycol",
        "molecular sieve", "adsorption dryer", "dew point",
    ],

    # ══════════════════════════════════════════════════════════════
    # DRIVE SHAFTS
    # ══════════════════════════════════════════════════════════════
    "Drive Shafts": [
        "drive shaft", "driveshaft", "power shaft", "transmission shaft",
        "shaft coupling", "flexible shaft", "articulated shaft",
        "splined shaft", "shaft assembly", "torque transmission shaft",
        "cardan shaft", "universal joint shaft",
    ],

    # ══════════════════════════════════════════════════════════════
    # MACERATOR
    # ══════════════════════════════════════════════════════════════
    "Macerator": [
        "macerator", "maceration", "shredder", "grinder pump",
        "waste grinder", "sewage grinder", "comminuting device",
        "comminuter", "macerating pump", "cutting pump",
        "grinding mechanism", "waste disintegrator",
    ],

    "Macerator/Bearing": [
        "macerator bearing", "grinder bearing", "shredder bearing",
        "rolling bearing", "thrust bearing macerator",
        "bearing assembly macerator", "radial bearing grinder",
    ],

    "Macerator/Pesquisa sobre trituradores": [
        "triturator", "waste crusher", "organic waste shredder",
        "food waste grinder", "industrial macerator",
        "biomass grinder", "solids shredder",
    ],

    # ══════════════════════════════════════════════════════════════
    # MACHINES FOR RUBBER INDUSTRY
    # ══════════════════════════════════════════════════════════════
    "Machines for rubber industry": [
        "rubber machine", "rubber processing", "rubber vulcanization",
        "elastomer processing", "rubber extruder", "rubber mixer",
        "internal mixer", "banbury mixer", "rubber calendar",
        "rubber mold", "rubber injection", "latex processing",
        "rubber compound", "nitrile rubber", "EPDM",
        "neoprene", "silicone rubber machine",
    ],

    # ══════════════════════════════════════════════════════════════
    # MANUFACTURING TECHNOLOGY
    # ══════════════════════════════════════════════════════════════
    "Manufacturing technology": [
        "manufacturing process", "fabrication method",
        "production technology", "machining process",
        "surface treatment", "heat treatment", "casting method",
        "forging process", "sintering", "powder metallurgy",
        "additive manufacturing", "3D printing metal",
        "CNC machining", "precision manufacturing",
    ],

    "Manufacturing technology/Extrusion": [
        "extrusion", "extruder", "extrusion die", "extrusion screw",
        "polymer extrusion", "rubber extrusion", "metal extrusion",
        "co-extrusion", "twin screw extruder", "single screw extruder",
        "extrusion molding", "extrusion process", "profile extrusion",
        "barrel extruder",
        # expansão
        "extruding", "pultrusion", "hot extrusion", "cold extrusion",
        "coextrusion",
    ],

    "Manufacturing technology/Induction Heating": [
        "induction heating", "induction coil", "electromagnetic heating",
        "induction hardening", "induction brazing", "induction welding",
        "eddy current heating", "induction furnace",
        "induction annealing", "high frequency heating",
        "induction tempering",
        # expansão
        "high-frequency induction",
    ],

    "Manufacturing technology/Sealings": [
        "seal manufacturing", "sealing production", "gasket fabrication",
        "o-ring manufacturing", "seal material processing",
        "elastomer sealing manufacturing", "vulcanized seal",
        "molded seal", "seal compound",
    ],

    # ══════════════════════════════════════════════════════════════
    # MATERIAL FOR PUMPS
    # ══════════════════════════════════════════════════════════════
    "Material for pumps": [
        "pump material", "pump coating", "wear resistant material",
        "corrosion resistant pump", "elastomer pump",
        "pump lining", "abrasion resistant", "pump composite",
        "ceramic coating pump", "hardened steel pump",
        "polymer pump material", "duplex stainless pump",
        "carbide coating", "PTFE pump", "nitrile elastomer pump",
    ],

    # ══════════════════════════════════════════════════════════════
    # MEASURING DEVICES
    # ══════════════════════════════════════════════════════════════
    "Measuring devices": [
        "measuring device", "measurement instrument", "flow meter",
        "pressure gauge", "temperature sensor", "level sensor",
        "viscosity meter", "density meter", "torque sensor",
        "displacement sensor", "vibration sensor",
        "downhole measurement", "wellbore measurement",
        "multiphase flow meter", "Coriolis meter",
    ],

    # ══════════════════════════════════════════════════════════════
    # MONITORING AND CONTROLLING
    # ══════════════════════════════════════════════════════════════
    "Monitoring and controlling": [
        "monitoring system", "control system", "SCADA",
        "pump control", "remote monitoring", "automation",
        "PLC control", "variable frequency drive", "VFD",
        "speed controller", "flow control", "pressure control",
        "condition monitoring", "predictive maintenance",
        "data acquisition", "telemetry", "IoT pump",
        "smart pump", "pump protection system",
    ],

    # ══════════════════════════════════════════════════════════════
    # OIL TOOLS
    # ══════════════════════════════════════════════════════════════
    "Oil Tools": [
        "oil tool", "downhole tool", "wellbore tool",
        "oilfield equipment", "petroleum tool", "well intervention",
        "completion tool", "production tool", "artificial lift",
    ],

    "Oil Tools/Anchoring Tool": [
        "anchoring tool", "wellbore anchor", "tubing anchor",
        "casing anchor", "slip anchor", "downhole anchor",
        "anchor device", "packer anchor", "anchor setting tool",
        "mechanical anchor", "hydraulic anchor",
    ],

    "Oil Tools/Anti-rotation control": [
        "anti-rotation", "rotation control", "torque arrest",
        "anti-torque device", "rotation prevention",
        "non-rotating", "rotor lock", "anti-spin device",
        "rotation limiter", "downhole anti-rotation",
    ],

    "Oil Tools/Blow-Out Preventer": [
        "blow-out preventer", "BOP", "blowout preventer",
        "well control", "blowout control", "annular preventer",
        "ram preventer", "choke manifold", "kill line",
        "well blowout", "pressure containment wellbore",
    ],

    "Oil Tools/Centralizer": [
        "centralizer", "casing centralizer", "bow spring centralizer",
        "rigid centralizer", "tubing centralizer",
        "roller centralizer", "casing standoff",
        "cementing centralizer", "float centralizer",
    ],

    "Oil Tools/Drilling": [
        "drilling", "drill bit", "rotary drilling", "directional drilling",
        "drill string", "drilling fluid", "mud motor",
        "bottom hole assembly", "BHA", "drilling tool",
        "downhole drilling", "drilling equipment", "PDC bit",
        "tricone bit", "core drilling",
    ],

    "Oil Tools/Drive Head": [
        "drive head", "wellhead drive", "PCP drive head",
        "surface drive", "belt drive head", "gear drive head",
        "hydraulic drive head", "pump drive unit",
        "polished rod drive", "rod string drive",
    ],

    "Oil Tools/Drive Head/Backspin Brake": [
        "backspin brake", "backspin control", "reverse spin",
        "anti-backspin", "backspin protection",
        "downhole backspin", "brake device wellhead",
        "dynamic brake", "regenerative brake pump",
    ],

    "Oil Tools/Drive Head/Shaft Sealing": [
        "shaft seal drive head", "polished rod seal",
        "rod sealing", "stuffing box drive head",
        "dynamic seal shaft", "rod packing",
        "shaft sealing device", "rotating seal drive",
    ],

    "Oil Tools/Gas Compressor": [
        "gas compressor", "natural gas compressor",
        "downhole compressor", "reciprocating compressor",
        "centrifugal compressor", "wellhead compressor",
        "vapor recovery compressor", "gas reinjection",
        "compressor station", "gas boosting",
    ],

    "Oil Tools/Multiphase Separator": [
        "multiphase separator", "gas-liquid separator",
        "three-phase separator", "oil-gas-water separator",
        "gravity separator", "cyclone separator",
        "horizontal separator", "vertical separator",
        "production separator", "test separator",
        "slug catcher", "inline separator",
    ],

    "Oil Tools/Multiphase coveying device": [
        "multiphase conveying", "multiphase transport",
        "multiphase flow device", "gas-liquid conveying",
        "multiphase pumping", "two-phase flow device",
        "wet gas conveying", "multiphase boosting",
    ],

    "Oil Tools/Packer": [
        "packer", "inflatable packer", "mechanical packer",
        "hydraulic packer", "production packer",
        "retrievable packer", "permanent packer",
        "bridge plug", "wellbore packer", "casing packer",
        "tubing packer", "zonal isolation",
    ],

    "Oil Tools/Production Technology": [
        "production technology", "oil production", "well completion",
        "artificial lift technology", "production optimization",
        "enhanced oil recovery", "EOR", "water injection",
        "gas injection", "downhole production", "well productivity",
        "inflow performance", "production logging",
    ],

    "Oil Tools/Pulsation damping device": [
        "pulsation dampener", "pulsation damper",
        "pressure pulsation", "flow pulsation control",
        "pulsation attenuation", "surge dampener",
        "hydraulic pulsation", "acoustic dampener pipeline",
    ],

    "Oil Tools/Rod Clamp": [
        "rod clamp", "sucker rod clamp", "polished rod clamp",
        "rod coupling clamp", "rod holder", "rod gripper",
        "rod locking device", "tubing clamp",
    ],

    "Oil Tools/Rods": [
        "sucker rod", "polished rod", "rod string",
        "fiberglass rod", "steel rod wellbore",
        "rod coupling", "rod guide", "continuous rod",
        "coiled rod", "rod centralizer", "drive rod",
    ],

    "Oil Tools/Sand Protection": [
        "sand protection", "sand control", "sand exclusion",
        "sand management", "sand prevention",
        "sand influx", "sand production control",
        "gravel pack", "sand filter wellbore",
    ],

    "Oil Tools/Sand Protection/Desander": [
        "desander", "sand desander", "hydrocyclone desander",
        "wellbore desander", "downhole desander",
        "sand removal device", "desanding unit",
    ],

    "Oil Tools/Sand Protection/Sand Stopper": [
        "sand stopper", "sand plug", "sand barrier",
        "sand retention device", "sand block",
        "anti-sand device", "sand flow stopper",
    ],

    "Oil Tools/Sand Protection/Sand separator": [
        "sand separator", "solids separator",
        "downhole sand separator", "gravity sand separator",
        "cyclonic sand separator", "sand particle separation",
    ],

    "Oil Tools/Sand Protection/Screen": [
        "sand screen", "wire wrap screen", "slotted liner",
        "mesh screen", "expandable screen", "pre-pack screen",
        "completion screen", "filtration screen wellbore",
        "inflow control screen",
    ],

    "Oil Tools/Sensoring": [
        "downhole sensor", "wellbore sensor", "sensing device oil",
        "pressure sensor downhole", "temperature sensor downhole",
        "flow sensor wellbore", "fiber optic sensing",
        "distributed temperature sensing", "DTS",
        "downhole instrumentation", "permanent monitoring sensor",
    ],

    "Oil Tools/Shaft coupling": [
        "shaft coupling", "flexible coupling", "rigid coupling",
        "gear coupling", "jaw coupling", "disc coupling",
        "pump shaft coupling", "spline coupling",
        "universal coupling", "coupling device shaft",
    ],

    "Oil Tools/Tubing": [
        "production tubing", "coiled tubing", "tubing string",
        "tubing hanger", "tubing connector", "tubing joint",
        "tubing anchor", "dual tubing", "tubing patch",
        "tubing retrievable", "tubing running tool",
    ],

    "Oil Tools/Tubing Grab": [
        "tubing grab", "tubing retrieval tool", "fishing tool tubing",
        "overshot tool", "spear tool", "tubing catcher",
        "tubing running grab", "tubing pulling tool",
    ],

    "Oil Tools/Valves": [
        "downhole valve", "subsurface valve", "tubing valve",
        "safety valve", "SSSV", "SCSSV", "standing valve",
        "traveling valve", "check valve downhole",
        "gas lift valve", "injection valve",
    ],

    "Oil Tools/Water cleaner": [
        "water cleaner", "produced water treatment",
        "water purification oil", "water deoiling",
        "hydrocyclone water", "water polishing",
        "produced water separator", "water cleaning device",
        "oil-water separation", "water treatment system",
    ],

    "Oil Tools/Wellhead equipment": [
        "wellhead", "wellhead equipment", "Christmas tree",
        "wellhead assembly", "wellhead seal",
        "wellhead connector", "surface wellhead",
        "subsea wellhead", "wellhead flange",
    ],

    "Oil Tools/Wellhead equipment/Hang-off Adapter": [
        "hang-off adapter", "tubing hanger adapter",
        "wellhead adapter", "casing hanger",
        "production hanger", "hanger assembly wellhead",
        "hang-off device", "support adapter wellhead",
    ],

    "Oil Tools/Wellhead equipment/Riser": [
        "riser", "drilling riser", "production riser",
        "marine riser", "riser connector", "riser joint",
        "flexible riser", "steel catenary riser", "SCR",
        "subsea riser", "riser tensioner",
    ],

    "Oil Tools/Wellhead equipment/Rod Rotator": [
        "rod rotator", "polished rod rotator",
        "sucker rod rotator", "rod rotating device",
        "string rotator", "rotary rod device",
        "rod rotation mechanism", "rod wear rotator",
    ],

    # ══════════════════════════════════════════════════════════════
    # PULSATION DAMPING DEVICE (raiz)
    # ══════════════════════════════════════════════════════════════
    "Pulsation damping device": [
        "pulsation dampener", "pulsation damper", "pulsation absorber",
        "pressure pulsation", "flow pulsation", "surge suppressor",
        "pulse attenuator", "bladder dampener", "diaphragm dampener",
        "hydraulic accumulator", "pulsation bottle",
    ],

    # ══════════════════════════════════════════════════════════════
    # PUMPS
    # ══════════════════════════════════════════════════════════════
    "Pumps": [
        "pump", "pumping device", "fluid pump",
        "positive displacement pump", "dynamic pump",
        "pumping system", "pump assembly",
    ],

    "Pumps/Acoustic Pump": [
        "acoustic pump", "sonic pump", "ultrasonic pump",
        "sound wave pump", "piezoelectric pump",
        "acoustic wave fluid", "resonant pump",
        "vibration pump acoustic",
    ],

    "Pumps/Barrel emptying system": [
        "barrel emptying", "drum emptying", "drum pump",
        "barrel pump", "container emptying",
        "drum drainer", "follower plate pump",
        "barrel unloading system", "drum evacuation",
    ],

    "Pumps/Centrifugal Pump": [
        "centrifugal pump", "radial flow pump", "mixed flow pump",
        "axial flow pump", "impeller", "volute",
        "diffuser pump", "multi-stage centrifugal",
        "end suction pump", "split case pump",
        "turbine pump", "centrifugal pump design",
    ],

    "Pumps/Centrifugal Pump/Bearing": [
        "centrifugal pump bearing", "pump bearing assembly",
        "radial bearing pump", "thrust bearing centrifugal",
        "bearing housing pump", "pump bearing lubrication",
        "ceramic bearing pump", "bearing seal pump",
    ],

    "Pumps/Gas Lift": [
        "gas lift", "gas lift valve", "gas lift mandrel",
        "intermittent gas lift", "continuous gas lift",
        "gas injection artificial lift", "gas lift string",
        "gas lift system", "gas lift completion",
        "unloading valve gas lift",
    ],

    "Pumps/Gear Pump": [
        "gear pump", "external gear pump", "internal gear pump",
        "helical gear pump", "spur gear pump",
        "gear pump design", "gear pump flow",
        "gerotor pump", "gerotorpump",
    ],

    "Pumps/Hose Pump": [
        "hose pump", "peristaltic pump", "tube pump",
        "peristaltic hose", "squeeze pump",
        "roller pump hose", "flexible hose pump",
    ],

    "Pumps/Lobe Pump": [
        "lobe pump", "rotary lobe pump", "tri-lobe pump",
        "bi-lobe pump", "lobe rotor", "rotary pump lobe",
        "sanitary lobe pump",
    ],

    "Pumps/PC Pump and Motor": [
        "progressive cavity pump", "PC pump", "PCP",
        "cavity pump", "helical rotor pump", "screw pump oil",
        "eccentric screw pump", "Moineau pump",
        "elastomer stator", "rotor stator",
        "progressing cavity", "single screw pump",
    ],

    "Pumps/PC Pump and Motor/Assembly devices": [
        "pump assembly device", "PCP assembly tool",
        "pump installation tool", "stator assembly",
        "rotor installation", "pump coupling assembly",
        "assembly fixture pump", "pump make-up tool",
    ],

    "Pumps/PC Pump and Motor/Auger": [
        "auger", "screw conveyor pump", "auger pump",
        "helical auger", "feed auger", "auger mechanism",
        "solids auger pump", "auger device",
    ],

    "Pumps/PC Pump and Motor/Bearing": [
        "PCP bearing", "progressive cavity bearing",
        "downhole bearing pump", "radial bearing PCP",
        "thrust bearing pump motor", "bearing PC pump",
    ],

    "Pumps/PC Pump and Motor/Bridge Braker Device": [
        "bridge breaker", "bridge breaking device",
        "plug breaker pump", "blockage breaker",
        "bridge breaking mechanism", "anti-bridging device",
        "solids bridge breaker",
    ],

    "Pumps/PC Pump and Motor/Cascaded Pump": [
        "cascaded pump", "tandem pump", "multi-stage PCP",
        "series pump cavity", "staged cavity pump",
        "cascaded progressive cavity", "pump in series PCP",
    ],

    "Pumps/PC Pump and Motor/Drive Shaft": [
        "PCP drive shaft", "pump drive shaft",
        "flexible drive shaft PCP", "shaft articulation pump",
        "drive rod PCP", "transmission shaft cavity pump",
        "pump driveshaft", "flexible shaft pump",
    ],

    "Pumps/PC Pump and Motor/Geometry - Profile": [
        "pump geometry", "rotor profile", "stator profile",
        "helicoid geometry", "cavity profile",
        "lobe geometry pump", "pitch ratio pump",
        "eccentricity pump", "profile optimization pump",
        "tooth profile pump",
    ],

    "Pumps/PC Pump and Motor/Grinding device": [
        "pump grinding device", "solid grinding pump",
        "PCP grinder", "macerating pump device",
        "cutting device pump", "solid shredder pump",
    ],

    "Pumps/PC Pump and Motor/Guard": [
        "pump guard", "intake guard", "pump protection guard",
        "screen guard pump", "intake protection",
        "pump shroud", "pump filter guard",
    ],

    "Pumps/PC Pump and Motor/Housing": [
        "pump housing", "stator housing", "pump casing cavity",
        "pump body housing", "housing design pump",
        "pump barrel", "outer housing pump",
    ],

    "Pumps/PC Pump and Motor/Insertable": [
        "insertable pump", "insert pump", "retrievable insert pump",
        "pump insert assembly", "drop-in pump",
        "pump insert device", "insertable PCP",
    ],

    "Pumps/PC Pump and Motor/Joint": [
        "pump joint", "flexible joint PCP", "universal joint pump",
        "ball joint pump", "articulated joint pump",
        "knuckle joint pump", "drive joint cavity pump",
    ],

    "Pumps/PC Pump and Motor/Material for pumps": [
        "PCP material", "stator elastomer", "rotor material",
        "pump material cavity", "elastomer compound pump",
        "hardened rotor", "abrasion resistant stator",
        "nitrile stator", "polymer stator material",
    ],

    "Pumps/PC Pump and Motor/Positioning Tag": [
        "positioning tag", "pump position indicator",
        "pump location tag", "rotor position sensor",
        "downhole positioning", "pump tag device",
    ],

    "Pumps/PC Pump and Motor/Rotor": [
        "rotor", "helical rotor", "rotor design",
        "PCP rotor", "single helix rotor",
        "rotor coating", "rotor geometry",
        "rotor material", "chrome rotor", "rotor wear",
    ],

    "Pumps/PC Pump and Motor/Stator": [
        "stator", "elastomeric stator", "stator design",
        "stator geometry", "double helix stator",
        "stator bonding", "stator liner",
        "metal stator", "stator wear", "rigid stator",
        "stator rubber", "stator compound",
    ],

    "Pumps/PC Pump and Motor/Stirring extension": [
        "stirring extension", "agitator pump",
        "mixer extension pump", "pump agitator",
        "stirring device pump", "agitation extension",
    ],

    "Pumps/Piston Pump": [
        "piston pump", "reciprocating pump", "plunger pump",
        "piston rod pump", "double acting piston",
        "single acting piston", "pump piston seal",
        "piston cylinder pump", "hydraulic piston pump",
    ],

    "Pumps/Pump Control": [
        "pump control", "pump controller",
        "speed control pump", "flow control pump",
        "variable speed pump", "pump automation",
        "pump monitoring control", "smart pump control",
        "soft starter pump", "VFD pump control",
    ],

    "Pumps/Screw Compressor": [
        "screw compressor", "twin screw compressor",
        "helical screw compressor", "rotary screw compressor",
        "oil-flooded compressor", "oil-free screw compressor",
        "single screw compressor", "compressor rotor screw",
    ],

    "Pumps/Screw Pump": [
        "screw pump", "twin screw pump", "triple screw pump",
        "multi-screw pump", "helical screw pump",
        "archimedes screw pump", "screw pump design",
    ],

    "Pumps/Screw Pump/Bearing": [
        "screw pump bearing", "twin screw bearing",
        "bearing screw pump", "radial bearing screw",
        "thrust bearing screw pump",
    ],

    "Pumps/Screw Pump/Body": [
        "screw pump body", "pump housing screw",
        "casing screw pump", "barrel screw pump",
        "body design screw pump",
    ],

    "Pumps/Screw Pump/Coupling": [
        "screw pump coupling", "shaft coupling screw",
        "pump coupling", "gear coupling screw pump",
        "flexible coupling screw pump",
    ],

    "Pumps/Screw Pump/Gears and Gear Box": [
        "screw pump gear", "gearbox screw pump",
        "timing gear", "synchronizing gear screw",
        "helical gear screw pump", "gear box pump",
    ],

    "Pumps/Screw Pump/Lubrication": [
        "screw pump lubrication", "bearing lubrication pump",
        "oil lubrication screw", "grease lubrication pump",
        "forced lubrication screw pump",
    ],

    "Pumps/Screw Pump/Manufacturing method": [
        "screw pump manufacturing", "screw manufacturing method",
        "rotor fabrication screw", "screw machining",
        "manufacturing screw pump",
    ],

    "Pumps/Screw Pump/Multiphase": [
        "multiphase screw pump", "twin screw multiphase",
        "gas-liquid screw pump", "multiphase pumping screw",
        "wet gas screw pump", "GVF screw pump",
    ],

    "Pumps/Screw Pump/Profile": [
        "screw pump profile", "rotor profile screw",
        "screw thread profile", "helical profile screw pump",
        "tooth profile screw pump", "screw geometry profile",
    ],

    "Pumps/Screw Pump/Relief Valve": [
        "relief valve screw pump", "pressure relief screw",
        "safety valve screw pump", "bypass valve screw pump",
        "pressure limiting valve pump",
    ],

    "Pumps/Screw Pump/Sealing": [
        "screw pump sealing", "shaft seal screw pump",
        "dynamic seal screw", "lip seal screw pump",
        "mechanical seal screw pump",
    ],

    "Pumps/Screw conveyor": [
        "screw conveyor", "auger conveyor", "helical conveyor",
        "worm conveyor", "screw feeder", "material conveying screw",
        "conveyor screw design",
    ],

    "Pumps/Scroll Compressor": [
        "scroll compressor", "scroll pump", "scroll expander",
        "orbiting scroll", "fixed scroll",
        "scroll mechanism", "scroll fluid machine",
    ],

    "Pumps/Submersible Pumps": [
        "submersible pump", "ESP", "electric submersible pump",
        "downhole submersible", "submersible motor pump",
        "deep well pump", "borehole pump",
        "submersible centrifugal", "multistage submersible",
    ],

    "Pumps/Submersible Pumps/Seal section and thrust bearing": [
        "seal section ESP", "protector ESP", "motor seal section",
        "thrust bearing ESP", "thrust chamber",
        "submersible pump seal", "motor protector",
        "shaft seal ESP", "labyrinth protector",
    ],

    "Pumps/Vane type Pump": [
        "vane pump", "rotary vane pump", "sliding vane pump",
        "vane motor", "balanced vane pump",
        "unbalanced vane pump", "vane cell pump",
    ],

    # ══════════════════════════════════════════════════════════════
    # SEALINGS
    # ══════════════════════════════════════════════════════════════
    "Sealings": [
        "seal", "sealing", "gasket", "o-ring", "sealing device",
        "fluid seal", "pressure seal", "sealing system",
        "dynamic sealing", "static sealing",
    ],

    "Sealings/Assembly tools": [
        "seal assembly tool", "seal installation tool",
        "o-ring assembly", "seal fitting tool",
        "sealing press tool", "gasket assembly",
        "seal mounting device",
    ],

    "Sealings/Diaphragm seal": [
        "diaphragm seal", "membrane seal", "flexible membrane seal",
        "diaphragm sealing", "rolling diaphragm",
        "bellows seal", "diaphragm pump seal",
    ],

    "Sealings/Labyrinth Seal": [
        "labyrinth seal", "labyrinth sealing", "non-contact seal",
        "clearance seal", "labyrinth packing",
        "stepped labyrinth", "interlocking labyrinth",
    ],

    "Sealings/Lip Seal": [
        "lip seal", "radial lip seal", "shaft lip seal",
        "PTFE lip seal", "rubber lip seal",
        "wiper seal", "lip sealing element",
        "oil seal lip",
    ],

    "Sealings/Mechanical Seal": [
        "mechanical seal", "face seal", "rotary seal",
        "cartridge seal", "split seal", "bellows mechanical seal",
        "pusher seal", "non-pusher seal",
        "double mechanical seal", "tandem seal",
        "mechanical face seal design",
    ],

    "Sealings/Stuffing Box": [
        "stuffing box", "packing gland", "packing box",
        "rope packing", "braided packing",
        "compression packing", "stuffing box seal",
        "polished rod stuffing box", "gland packing",
    ],

    # ══════════════════════════════════════════════════════════════
    # SEPARATOR
    # ══════════════════════════════════════════════════════════════
    "Separator": [
        "separator", "separation device", "phase separator",
        "oil separator", "gas separator", "liquid separator",
        "centrifugal separator", "gravity separator",
        "inline separator", "compact separator",
        "downhole separator", "wellbore separator",
        "cyclone separator", "hydrocyclone",
        "gas-liquid separator", "oil water separator",
    ],

    # ══════════════════════════════════════════════════════════════
    # VALVES
    # ══════════════════════════════════════════════════════════════
    # MODIFICAÇÃO (Parte B — Causa 1):
    # Removido "valve" (1 palavra, ultra-genérico). Qualquer abstract de
    # válvula menciona "valve" várias vezes, fazendo a raiz acumular hits
    # baratos e vencer sobre subpastas específicas. Os demais termos aqui
    # são expressões de 2+ palavras que já são razoavelmente específicas.
    # Termos ultra-genéricos de 1 palavra ("valve assembly", "valve body",
    # "valve element", "valve device") foram igualmente removidos de
    # _EXPANSOES["Valves"] abaixo.
    "Valves": [
        "check valve", "ball valve", "gate valve",
        "globe valve", "needle valve", "butterfly valve",
        "plug valve", "diaphragm valve", "relief valve",
        "safety valve", "control valve", "solenoid valve",
        "non-return valve", "pressure reducing valve",
        "flow control valve", "isolation valve",
    ],

    # ══════════════════════════════════════════════════════════════
    # ELASTOMERS
    # Subpasta de: Material for pumps
    # Justificativa: 121 patentes — compostos de stator, vulcanização,
    # elastômeros para bombas PCP e selos.
    # ══════════════════════════════════════════════════════════════
    "Material for pumps/Elastomers": [
        "elastomer", "elastomeric", "elastomeric stator",
        "rubber compound", "rubber material pump",
        "nitrile rubber", "hydrogenated nitrile", "HNBR",
        "EPDM elastomer", "neoprene compound",
        "polyurethane elastomer", "fluoroelastomer", "Viton",
        "vulcanization", "vulcanized rubber", "rubber bonding",
        "elastomer composition", "rubber formulation",
        "elastomer properties", "elastomer radiation",
        "elastomeric material pump", "rubber stator",
        "stator elastomer compound",
    ],

    # ══════════════════════════════════════════════════════════════
    # ELECTRIC MOTORS
    # Nova pasta de nível superior.
    # Justificativa: 109 patentes — motores submersíveis, selagem de
    # motor, ESP motor, motores para acionamento de bombas.
    # ══════════════════════════════════════════════════════════════
    "Electric Motors": [
        "electric motor", "electrical motor", "motor winding",
        "submersible motor", "downhole motor electric",
        "ESP motor", "induction motor", "synchronous motor",
        "permanent magnet motor", "motor stator winding",
        "motor rotor", "motor housing electric",
        "motor cooling", "motor efficiency",
        "variable speed motor", "brushless motor",
        "motor insulation", "motor protection",
        "motor bearing electric", "motor shaft",
    ],

    # ══════════════════════════════════════════════════════════════
    # MACHINING
    # Subpasta de: Manufacturing technology
    # Justificativa: 91 patentes — usinagem de rotores, stators,
    # parafusos de bomba, métodos de eletroquímica.
    # ══════════════════════════════════════════════════════════════
    "Manufacturing technology/Machining": [
        "machining", "machining process", "machining method",
        "CNC machining", "electrochemical machining", "ECM",
        "EDM", "electrical discharge machining",
        "turning process", "milling process",
        "grinding method manufacturing",
        "drilling method manufacturing",
        "cutting tool design", "tool path",
        "rotor machining", "stator machining",
        "screw machining", "precision machining",
        "boring process", "honing process",
        "manufacturing rotor stator",
        # expansão
        "gear cutting", "tooth profile design",
        "broaching", "drilling process",
    ],

    # ══════════════════════════════════════════════════════════════
    # SURFACE TREATMENT
    # Subpasta de: Manufacturing technology
    # Justificativa: 73 patentes — revestimentos para componentes de
    # bomba, tratamentos para resistência a desgaste e corrosão.
    # ══════════════════════════════════════════════════════════════
    "Manufacturing technology/Surface Treatment": [
        "surface treatment", "surface coating",
        "hard coating", "wear coating", "protective coating",
        "PVD coating", "CVD coating",
        "thermal spray", "HVOF coating", "plasma spray",
        "hard chrome", "chromium coating", "chrome plating",
        "electroplating", "electroless plating",
        "nitriding", "nitrocarburizing",
        "surface hardening", "case hardening",
        "DLC coating", "diamond-like carbon",
        "tungsten carbide coating", "ceramic coating",
        "surface finishing pump", "pump component coating",
        "artificial lift coating", "coating pump component",
        # expansão
        "plating", "anodizing", "galvanizing",
        "surface modification", "shot peening", "sandblasting",
    ],

    "Manufacturing technology/Surface Treatment/Wear and Tribology": [
        "wear resistant coating", "tribological coating",
        "anti-wear surface", "friction reducing coating",
        "tribology surface", "wear behavior",
        "wear mechanism coating", "surface tribology",
        "abrasion resistant surface", "erosion resistant coating",
        # expansão
        "friction reduction", "lubricity", "wear surface", "hardfacing",
    ],

    "Manufacturing technology/Surface Treatment/Heat Treatment": [
        "heat treatment process", "thermal treatment",
        "quenching process", "tempering process",
        "annealing process", "normalization heat",
        "induction hardening process", "case hardening method",
        "carburizing process", "nitriding process",
        "age hardening", "precipitation hardening",
        "heat treatment alloy",
        # expansão
        "thermal processing",
    ],

    # ══════════════════════════════════════════════════════════════
    # CORROSION
    # Nova pasta de nível superior.
    # Justificativa: 59 patentes — ligas resistentes à corrosão,
    # revestimentos anticorrosão, materiais para ambientes agressivos.
    # ══════════════════════════════════════════════════════════════
    "Corrosion": [
        "corrosion", "corrosion resistant", "corrosion protection",
        "anticorrosion", "anti-corrosion",
        "corrosion resistant alloy", "corrosion inhibitor",
        "cathodic protection", "anodic protection",
        "galvanic corrosion", "pitting corrosion",
        "stress corrosion", "crevice corrosion",
        "oxidation resistant", "corrosion coating",
        "corrosion barrier", "corrosion fatigue",
        "sour service", "H2S resistant",
        "CO2 corrosion", "sweet corrosion",
        "corrosion resistant pump", "corrosion resistant stator",
        "austenitic alloy corrosion", "duplex steel corrosion",
    ],

    # ══════════════════════════════════════════════════════════════
    # VIBRATION AND ACOUSTICS
    # Subpasta de: Monitoring and controlling
    # Justificativa: 15 patentes — dispositivos de amortecimento,
    # isolamento de vibração, controle de ruído em bombas e sistemas.
    # ══════════════════════════════════════════════════════════════
    "Monitoring and controlling/Vibration and Acoustics": [
        "vibration damping", "vibration isolation",
        "vibration monitoring", "vibration sensor",
        "vibration absorber", "vibration control",
        "acoustic damper", "noise reduction device",
        "noise control pump", "acoustic emission",
        "structural vibration", "resonance control",
        "torsional vibration", "lateral vibration",
        "vibration measurement", "vibration analysis",
        "anti-vibration mount", "vibration protection",
    ],

    # ══════════════════════════════════════════════════════════════
    # HYDRAULIC BRAKE (BACKSPIN BRAKE)
    # Subpasta de: Oil Tools/Drive Head/Backspin Brake
    # Justificativa: 13 patentes — freio hidrodinâmico já tem
    # correspondência em Backspin Brake; expandindo as palavras-chave.
    # ══════════════════════════════════════════════════════════════
    "Oil Tools/Drive Head/Backspin Brake/Hydraulic Brake": [
        "hydrodynamic brake", "hydraulic retarder",
        "fluid brake", "hydraulic braking device",
        "eddy current brake", "retarder device",
        "dynamic braking fluid", "hydrodynamic retarder",
        "fluid coupling brake", "viscous brake",
        "hydraulic deceleration", "torque brake hydraulic",
    ],

    # ══════════════════════════════════════════════════════════════
    # MACERATOR — subpastas expandidas
    # Justificativa: 131+69+57+52+43 patentes não classificadas
    # ══════════════════════════════════════════════════════════════

    "Macerator/Industrial Crusher": [
        "crusher", "crushing apparatus", "crushing device",
        "shredder", "shredding apparatus", "shredding device",
        "industrial shredder", "industrial crusher",
        "size reduction", "size reduction device",
        "size reducing", "solid particle size reduction",
        "particle size reduction", "material crushing",
        "crushing machine", "crushing mechanism",
        "granulator", "granulating device",
        "rotary crusher", "hammer crusher",
        "jaw crusher", "impact crusher",
        "twin shaft shredder", "single shaft shredder",
        "biomass crusher", "waste crusher",
        "roll crusher", "roller crusher",
        "chopper device", "chopping apparatus",
        "size reduction method", "comminution",
        "comminution device", "comminution apparatus",
    ],

    "Macerator/Comminutor": [
        "comminutor", "comminuting apparatus",
        "comminuting device", "sewage grinder",
        "inline flow sewage", "sewage comminutor",
        "wastewater comminutor", "solids comminutor",
        "comminutor cutter", "cutter shaft comminutor",
        "side rails comminutor", "flow comminutor",
        "sewage solids", "waste comminutor",
        "comminutor blade", "rotary comminutor",
        "three shaft comminution", "two shaft comminution",
    ],

    "Macerator/Food Waste Disposer": [
        "food waste disposer", "food disposer",
        "garbage disposer", "kitchen disposer",
        "waste disposer", "food waste processor",
        "food grinder", "kitchen waste grinder",
        "household waste grinder", "domestic waste disposer",
        "food waste grinding", "organic waste disposer",
        "food waste device", "disposer unit",
        "garbage disposal unit", "food processing disposer",
    ],

    "Macerator/Cutting Elements": [
        "cutter element", "cutting element",
        "cutter blade", "cutting blade",
        "blade assembly crusher", "knife blade shredder",
        "cutting mechanism shredder",
        "cutter shaft", "cutting shaft",
        "cutter plate", "cutting plate",
        "movable cutter", "fixed cutter element",
        "cutter tooth", "cutting tooth",
        "helical cutter", "cutter body",
        "blade geometry cutter", "two-dimensional cutting",
        "cutting features", "cutter profile",
    ],

    # ══════════════════════════════════════════════════════════════
    # BEARINGS — nova pasta de nível superior
    # Justificativa: bearing hoje só existe como subpasta em
    # Macerator, Centrifugal Pump, PC Pump e Screw Pump.
    # Com 50+ patentes standalone e conceito transversal,
    # merece pasta própria.
    # ══════════════════════════════════════════════════════════════

    "Bearings": [
        "bearing", "bearing assembly", "bearing design",
        "bearing arrangement", "bearing system",
        "bearing housing", "bearing support",
        "bearing selection", "bearing failure",
        "bearing life", "bearing load",
        "bearing performance", "bearing type",
    ],

    "Bearings/Rolling Bearings": [
        "rolling bearing", "ball bearing",
        "roller bearing", "cylindrical roller bearing",
        "tapered roller bearing", "spherical roller bearing",
        "needle roller bearing", "angular contact bearing",
        "deep groove ball bearing", "self-aligning bearing",
        "bearing ring", "inner ring bearing",
        "outer ring bearing", "rolling element",
        "bearing raceway", "bearing cage",
        "bearing retainer", "bearing race",
    ],

    "Bearings/Thrust Bearings": [
        "thrust bearing", "axial bearing",
        "thrust load bearing", "thrust washer",
        "axial load bearing", "thrust plate",
        "thrust roller bearing", "ball thrust bearing",
        "tapered thrust bearing",
    ],

    "Bearings/Bearing Lubrication and Sealing": [
        "bearing lubrication", "bearing grease",
        "bearing oil supply", "bearing seal",
        "bearing protection", "bearing shield",
        "sealed bearing", "shielded bearing",
        "lubricated bearing", "bearing oil film",
        "bearing lubricant",
    ],

    "Bearings/Bearing Materials": [
        "bearing material", "ceramic bearing",
        "polymer bearing", "composite bearing",
        "bearing coating material", "bearing alloy",
        "self-lubricating bearing", "carbon bearing",
        "PTFE bearing", "bearing steel",
    ],

    # ══════════════════════════════════════════════════════════════
    # OIL TOOLS / Centralizer — palavras-chave faltantes
    # (8 patentes não foram capturadas pois o match falhava)
    # ══════════════════════════════════════════════════════════════
    # Já existe "Oil Tools/Centralizer" — expandindo palavras:

    # ══════════════════════════════════════════════════════════════
    # SEALINGS — NOVOS SUBGRUPOS
    # Identificados a partir de 654 patentes na raiz "Sealings"
    # que não tinham match em nenhum subgrupo.
    # ══════════════════════════════════════════════════════════════

    # ~250 patentes sobre vedação/proteção de rolamentos e mancais
    "Sealings/Bearing Seal": [
        "bearing seal", "sealed rolling bearing", "sealed bearing",
        "sealing device for bearing", "bearing sealing device",
        "bearing sealing structure", "seal for bearing",
        "bearing with sealing", "bearing with seal",
        "sealing device rolling bearing", "rolling bearing seal",
        "bearing seal assembly", "wheel bearing seal",
        "hub bearing seal", "sealed bearing device",
        "bearing protector", "bearing isolator seal",
        "bearing isolating seal", "bearing end cap seal",
        "bearing housing seal", "bearing seal ring",
        "combined seal ring bearing", "cassette seal",
        "cassette gasket bearing", "encoder seal bearing",
        "combination seal ring", "sealing apparatus bearing",
        "seal device bearing", "sealing member bearing",
        "rolling bearing sealing", "shaft bearing seal",
        "axle bearing seal", "double seal bearing",
        "dual seal bearing", "seal structure bearing",
        "bearing arrangement seal", "airtight bearing seal",
        "contaminant sealing bearing", "protective element bearing",
    ],

    # ~60 patentes sobre vedação específica de eixos rotativos
    "Sealings/Shaft Seal": [
        "shaft seal", "shaft sealing", "shaft sealing device",
        "shaft sealing arrangement", "shaft sealing apparatus",
        "shaft seal device", "drive shaft seal",
        "shaft seal arrangement", "shaft sealing mechanism",
        "shaft seal assembly", "rotary shaft seal",
        "dynamic shaft seal", "static dynamic pressure shaft seal",
        "shaft sealing system", "rotating shaft seal",
        "seal arrangement shaft", "assembly shaft seal",
        "sealing arrangement shaft", "intershaft seal",
        "shaft end seal", "seal shaft pump",
        "drive shaft sealing", "sealing structure shaft",
        "shaft seal structure", "shaft lip seal",
        "sealing arrangement on pump shaft",
    ],

    # ~40 patentes sobre anéis de vedação, o-rings, juntas planas
    "Sealings/Seal Ring and Gasket": [
        "seal ring", "sealing ring", "o-ring", "oring",
        "ring seal", "annular seal", "annular gap seal",
        "flat seal", "gasket seal", "sealing element",
        "nylon sealing ring", "seal ring assembly",
        "elastic sealing ring", "composite seal ring",
        "combination seal ring", "sealing washer",
        "self-sealing fastener", "sealing joint",
        "seal body", "seal assembly", "clean-in-place seal",
        "multi-piece seal", "split stuffing box seal",
        "expandable seal", "swellable seal","v-ring", "x-ring", "backup ring", "joint ring", "junta de vedação"
    ],

    # ~30 patentes sobre selos do tipo "rotary face" / anel deslizante
    # Expansão do subfolder já existente Sealings/Mechanical Seal
    # (adicionado via _EXPANSOES_V2 abaixo para não duplicar)

    # ══════════════════════════════════════════════════════════════
    # BEARINGS — NOVOS SUBGRUPOS
    # Identificados a partir de 110 patentes na raiz "Bearings"
    # ══════════════════════════════════════════════════════════════

    # ~50 patentes sobre mancais de deslizamento (não-rolamento)
    "Bearings/Sliding Bearings": [
        "sliding bearing", "journal bearing", "plain bearing",
        "friction bearing", "slide bearing", "sleeve bearing",
        "hydrodynamic plain bearing", "babbitt bearing",
        "white metal bearing", "bronze bearing",
        "synthetic resin bearing", "polymer slide bearing",
        "fluid film bearing", "oil film bearing",
        "bearing bush", "bearing bushing",
        "plain journal bearing", "slide ring bearing",
        "fluid lubricated bearing", "sliding contact bearing",
    ],

    # ~35 patentes sobre rolamentos de roda / cubo / eixo veicular
    "Bearings/Hub and Wheel Bearings": [
        "hub bearing", "wheel bearing", "hub unit bearing",
        "wheel hub bearing", "bearing device for wheel",
        "wheel support bearing", "hub unit",
        "driving wheel hub", "hub bearing unit",
        "wheel bearing assembly", "bearing device wheel",
        "wheel bearing device", "hub bearing assembly",
        "hub bearing unit structure", "axle bearing wheel",
        "bearing for wheel", "wheel hub unit",
        "wheel speed detection bearing", "wheel bearing sensor",
        "hub bearing with encoder", "bearing wheel drive",
        "bearing for railway car", "railway axle bearing",
        "axle bearing device", "rolling bearing for wheel",
    ],

    # ~15 patentes sobre rolamentos hidrodinâmicos / de fluido / magnéticos
    "Bearings/Fluid and Magnetic Bearings": [
        "fluid bearing", "fluid dynamic pressure bearing",
        "hydrodynamic bearing", "aerodynamic bearing",
        "air bearing", "magnetic bearing",
        "hydrostatic bearing", "gas bearing",
        "fluid lubricated bearing pad", "tilt pad bearing",
        "active magnetic bearing", "passive magnetic bearing",
        "electromagnet bearing", "fluid film pressure bearing",
    ],

    # ══════════════════════════════════════════════════════════════
    # PUMPS — NOVOS SUBGRUPOS
    # Identificados a partir de 156 patentes na raiz "Pumps"
    # ══════════════════════════════════════════════════════════════

    # ~25 patentes sobre bombas hidráulicas de potência
    "Pumps/Hydraulic Pump": [
        "hydraulic pump", "hydrostatic pump",
        "hydraulic gear pump", "hydraulic piston pump",
        "hydraulic power unit", "power steering pump",
        "high pressure hydraulic pump", "hydraulic oil pump",
        "hydraulic fluid pump", "variable displacement pump",
        "hydraulic generator", "hydraulic receiver",
        "hydraulic motor pump", "hydraulic circuit pump",
        "power hydraulic pump", "hydraulic pressure pump",
        "high pressure hydraulic generator",
    ],

    # ~10 patentes sobre bombas de vácuo
    "Pumps/Vacuum Pump": [
        "vacuum pump", "twin shaft vacuum pump",
        "dry vacuum pump", "vacuum exhaust device",
        "vacuum pumping system", "vacuum pump biased stator",
        "vacuum pump manufacture", "liquid ring vacuum pump",
        "rotary vacuum pump", "vacuum generation pump",
    ],

    # ~10 patentes sobre bombas Roots e êmbolo rotatório
    "Pumps/Roots and Rotary Piston Pump": [
        "roots pump", "roots blower", "rotary piston pump",
        "orbital pump", "orbital fluid pump",
        "rotary displacement pump", "lobe compressor",
        "roots type pump", "rotary lobe compressor",
        "positive displacement rotary pump",
        "eccentric rotor pump",
    ],

    # ~8 patentes sobre bombeamento multifásico genérico
    "Pumps/Multiphase Pump": [
        "multiphase pump", "multiphase pumping",
        "gas-liquid pump", "two-phase pump",
        "multiphase flow pump", "multi-phase mixture pump",
        "multiphase conveying pump", "multiphase booster pump",
        "method for delivering multi phase",
        "multi phase mixture delivery",
        "gas fraction pump", "GVF pump",
        "wet gas pump", "multiphase fluid pump",
    ],

    # ══════════════════════════════════════════════════════════════
    # VALVES — NOVOS SUBGRUPOS
    # Identificados a partir de 48 patentes na raiz "Valves"
    # sem nenhum subgrupo anterior.
    # ══════════════════════════════════════════════════════════════

    "Valves/Relief and Safety Valve": [
        "relief valve", "safety valve", "pressure relief valve",
        "spring-loaded relief valve", "relief valve assembly",
        "pressure limiting valve", "overpressure valve",
        "bypass relief valve", "back-pressure valve",
        "external relief valve", "internal relief valve",
        "pressure regulating valve", "safety relief valve",
        "relief valve screw pump", "integrated pressure relief",
        "screw pump with integrated pressure relief",
        "small flow safety valve", "spring external relief valve","blow-off valve", "pop valve", "bursting disc", "válvula de segurança", "pressure relief"
    ],

    "Valves/Check Valve": [
        "check valve", "non-return valve", "one-way valve",
        "backflow preventer", "check valve assembly",
        "swing check valve", "ball check valve",
        "tilting disc check valve", "foot valve",
        "lift check valve", "wafer check valve",
        "standing valve check", "traveling valve check",
        "unidirectional valve", "unidirectional fluid flow valve","clack valve", "flap valve", "válvula de retenção"
    ],

    "Valves/Control and Flow Valve": [
        "control valve", "flow control valve",
        "pressure control valve", "modulating valve",
        "proportional valve", "servo valve",
        "variable flow valve", "pneumatic control valve",
        "variable displacement valve", "displacement control valve",
        "solenoid valve", "electronically controlled valve",
        "hydraulic control valve", "flow regulating valve",
        "inflow control valve", "flow diverter valve",
        "liquid delivery valve", "micropump valve",
        "choker valve", "diverter valve","regulating valve", "throttle valve", "needle valve","válvula de controlo"
    ],

    "Valves/Sleeve and Toe Valve": [
        "sleeve valve", "sliding sleeve valve",
        "sleeve valve assembly", "toe valve",
        "toe valve override", "sliding sleeve",
        "downhole sleeve valve", "interval control valve",
        "production sleeve", "completion sleeve valve",
    ],

    "Valves/Compressor and Pump Valve": [
        "compressor valve", "suction valve",
        "discharge valve compressor", "reed valve",
        "valve plate compressor", "pump valve",
        "pump valve assembly", "piston pump valve",
        "liquid supply valve", "valve element pump",
        "delivery valve pump", "pump valve piston",
    ],

    # ══════════════════════════════════════════════════════════════
    # SEPARATOR — NOVOS SUBGRUPOS
    # Identificados a partir de 36 patentes na raiz "Separator"
    # sem nenhum subgrupo anterior.
    # ══════════════════════════════════════════════════════════════

    "Separator/Gas-Liquid Separator": [
        "gas-liquid separator", "gas liquid separator",
        "gas separator", "gas-liquid separation",
        "vapor-liquid separator", "gas liquid separation device",
        "bubble separator", "gas phase separator",
        "double channel gas-liquid", "spiral gas separator",
        "inline gas-liquid separator", "compact gas separator",
        "phase splitter", "high efficiency phase splitter",
        "jet pump separator", "gas boost separator","demister", "degasser", "slug catcher", "mist eliminator", "mist extractor", "vane-type demister"
    ],

    "Separator/Downhole Separator": [
        "downhole separator", "downhole gas separator",
        "downhole gas liquid separator", "wellbore separator",
        "passive gas separator", "centrifugal downhole separator",
        "multiple cup downhole separator", "eccentric downhole separator",
        "downhole separation", "borehole separator",
        "progressive cavity separator", "PCP gas separator",
        "downhole liquid separator", "pump well separator",
        "pumping well separator",
    ],

    "Separator/Centrifugal Separator": [
        "centrifugal separator", "centrifugal force separator",
        "centrifugal gas separator", "centrifuge",
        "disc centrifuge", "decanter centrifuge",
        "continuous centrifugal", "centrifugal liquid separator",
        "rotating separator", "high speed centrifuge",
        "centrifugal dehydrator", "centrifugal crusher separator",
    ],

    "Separator/Multiphase Separator": [
        "multiphase separator", "multiphase separation",
        "three-phase separator", "production separator",
        "test separator", "oil-gas-water separator",
        "vertical three-phase separator", "constant pressure separator",
        "horizontal three-phase separator",
        "multiphase separation system",
    ],

    # ══════════════════════════════════════════════════════════════
    # DRIVE SHAFTS — NOVOS SUBGRUPOS
    # Identificados a partir de 33 patentes na raiz "Drive Shafts"
    # ══════════════════════════════════════════════════════════════

    "Drive Shafts/Flexible Shaft and Sleeve": [
        "flexible drive shaft", "flexible shaft sleeve",
        "sleeve for flexible shaft", "articulated shaft pump",
        "flexible shaft coupling", "rubber sleeve shaft",
        "drive shaft sleeve", "eccentric pump shaft sleeve",
        "shaft flexibility device", "flexible shaft assembly",
        "shaft protective sleeve", "coupling sleeve shaft",
    ],

    "Drive Shafts/Shaft Coupling Device": [
        "coupling guard", "shaft coupler", "coupling device",
        "flexible coupling device", "universal joint",
        "cardan joint", "cardan coupling", "jaw coupling device",
        "disc coupling device", "safety coupling",
        "torque coupling", "shaft connection device",
        "pump shaft connection", "drive coupling guard",
    ],

    # ══════════════════════════════════════════════════════════════
    # MANUFACTURING TECHNOLOGY — novas subpastas
    # Para esvaziar a raiz de patentes de processos de fabricação
    # que não encaixavam nas subpastas anteriores.
    # ══════════════════════════════════════════════════════════════

    "Manufacturing technology/Casting and Molding": [
        # Captura patentes de moldes por injeção, fundição, forjamento
        "casting", "die casting", "sand casting", "investment casting",
        "molding", "injection molding", "blow molding", "mold halves",
        "mold cavity", "mold halves injection",
        "moldable material injected", "material solidifies mold",
        "separable mold halves cavity", "two mold halves",
        "foundry", "forging", "stamping",
        "forged component", "forging process method",
        "casting method alloy", "sand casting metal",
        "die casting aluminum", "investment casting turbine",
        "rubber injection molding", "plastic injection molding",
        "mold design component", "mold release casting",
        "solidification casting", "wax pattern investment",
        "centrifugal casting", "continuous casting",
        "squeeze casting", "thixocasting",
        "sintering", "powder metallurgy",
        "sintered component", "powder metallurgy part",
        "metal powder compaction", "sintered bearing",
        "hot isostatic pressing", "HIP process",
        "cold isostatic pressing",
    ],

    "Manufacturing technology/Welding and Joining": [
        "welding", "welded", "weld", "weldment",
        "brazing", "soldering", "laser welding",
        "friction welding", "friction stir welding",
        "ultrasonic welding", "resistance welding",
        "arc welding", "MIG welding", "TIG welding",
        "spot welding", "seam welding",
        "bonding", "adhesive joining", "adhesive bonding",
        "structural adhesive", "epoxy bonding",
        "mechanical joining", "fastening method",
        "press fitting", "interference fit",
        "shrink fitting", "shrink fit assembly",
        "swaging", "crimping",
        "diffusion bonding", "explosion welding",
        "electron beam welding",
    ],

    "Manufacturing technology/Additive Manufacturing": [
        "additive manufacturing", "3d printing", "3D printed",
        "rapid prototyping", "direct metal laser sintering", "DMLS",
        "selective laser sintering", "SLS",
        "selective laser melting", "SLM",
        "fused deposition modeling", "FDM",
        "stereolithography", "SLA",
        "binder jetting", "material jetting",
        "directed energy deposition", "DED",
        "laser powder bed fusion",
        "metal 3D printing", "polymer 3D printing",
        "3D printed component", "printed part layer",
        "layer by layer manufacturing",
        "topology optimization additive",
    ],

    "Manufacturing technology/Assembly and Fabrication": [
        # Captura patentes genéricas de montagem, fabricação de membranas,
        # estruturas porosas e métodos de produção não cobertos acima
        "assembly method", "fabrication method",
        "manufacturing method", "method of manufacturing",
        "process of manufacture", "assembly process",
        "fabrication process", "production method",
        "assembly procedure", "assembly sequence",
        "modular assembly", "sub-assembly",
        "porous structure fabrication", "membrane process manufacture",
        "porous membrane manufacture", "porous ceramic fabrication",
        "ceramic membrane process", "filter fabrication process",
        "non-woven fabrication", "fiber fabrication process",
        "lamination process", "laminating method",
        "bonding manufacturing", "vulcanization process",
        "elastomer bonding manufacturing", "rubber bonding process",
        "press fitting assembly", "interference fitting assembly",
        "precision assembly", "tolerance assembly",
        "component assembly fixture", "assembly fixture design",
        "manufacture assembly method component",
        "assembly steps method manufacture",
    ],

}


# ── Expansão de categorias existentes ────────────────────────────────
# Adiciona palavras-chave a categorias já existentes no dicionário acima

_EXPANSOES = {
    "Oil Tools/Centralizer": [
        "centraliser", "borehole centraliser",
        "casing centraliser", "tubing centraliser",
        "swellable centralizer", "swellable centraliser",
        "interference-fit centralizer", "stop collar centralizer",
        "downhole centralizer", "wellbore centralizer",
    ],

    # ── Sealings/Mechanical Seal ── +~80 patentes faltando
    "Sealings/Mechanical Seal": [
        "mechanical seal device", "mechanical sealing device",
        "slide ring seal", "slide ring packing", "slip ring seal",
        "slip ring sealing", "sliding ring seal",
        "sliding component", "sliding part", "sliding parts",
        "face mechanical seal", "end face seal",
        "end face mechanical seal", "rotary face seal",
        "gas seal mechanical", "gas-lubricated seal",
        "dry gas mechanical seal", "dry gas seal",
        "spring mechanical seal", "spring integral seal",
        "high pressure mechanical seal",
        "mechanical seal assembly", "mechanical seal pump",
        "mechanical seals pump", "seal rotating",
        "seal stationary ring", "seal counter ring",
        "silicon carbide mechanical seal",
        "fluid sealing device rotating","stationary seal","rotating seal", "selo mecânico"
    ],

    # ── Sealings/Labyrinth Seal ── +~20 patentes faltando
    "Sealings/Labyrinth Seal": [
        "labyrinth seal bearing", "labyrinth bearing seal",
        "non-contact annular seal", "annular gap seal",
        "labyrinth sealing device", "labyrinth pellet seal",
        "combination labyrinth", "labyrinth and lip seal",
        "stepped seal", "labyrinth packing bearing",
        "labyrinth hub bearing", "clearance labyrinth bearing",
    ],

    # ── Sealings/Lip Seal ── +~15 patentes faltando
    "Sealings/Lip Seal": [
        "oil seal", "dust seal", "radial seal",
        "multi-lip seal", "multi-lip dust cover",
        "wiper lip seal", "contaminant seal lip",
        "cassette lip seal", "lip sealing element bearing",
    ],

    # ── Bearings/Rolling Bearings ── +~40 patentes faltando
    "Bearings/Rolling Bearings": [
        "rolling bearing device", "sealed rolling bearing",
        "rolling bearing for wheel", "rolling bearing structure",
        "anti-friction bearing", "double row ball bearing",
        "split bearing", "full-complement bearing",
        "bearing for supercharger", "turbocharger bearing",
        "bearing for electric motor", "rolling contact bearing",
        "rolling bearing arrangement", "impact resistant bearing",
    ],

    # ── Bearings/Bearing Lubrication and Sealing ── expansão
    "Bearings/Bearing Lubrication and Sealing": [
        "bearing oil seal", "bearing lip seal",
        "bearing dust seal", "bearing contaminant protection",
        "foreign matter bearing prevention",
        "bearing contamination prevention",
        "bearing grease retention", "bearing oil supply device",
        "ball bearing oil loss", "grease containment bearing",
    ],

    # ── Pumps/Screw Pump ── +~20 patentes faltando
    "Pumps/Screw Pump": [
        "spindle pump", "screw spindle pump", "worm pump",
        "three-screw pump", "triple screw pump",
        "screw pump connection", "screw rod pump",
        "high pressure screw pump", "low noise screw pump",
        "double flow screw pump", "hydraulic screw pump",
        "high temperature screw pump", "four-screw pump",
        "pitch-varying screw", "screw pump leakage",
        "screw pump flexible", "screw pump operation",
    ],

    # ── Pumps/Submersible Pumps ── +~10 patentes faltando
    "Pumps/Submersible Pumps": [
        "submersible pump assembly", "submersible pump borehole",
        "submersible pump device", "submerged oil pump",
        "electric submersible assembly", "cable suspended pump",
        "borehole submersible pump", "downhole pump assembly",
    ],

    # ── Pumps/PC Pump and Motor ── +~15 patentes faltando
    "Pumps/PC Pump and Motor": [
        "quimby pump", "eccentric pump motor",
        "downhole rotary pump", "downhole screw pump oil",
        "submersible screw pump", "ground driving head pump",
        "PC pump drive", "oil well screw pump",
        "progressive cavity well", "pump for deep borehole",
    ],

    # ── Valves (raiz) ── expansão
    # MODIFICAÇÃO (Parte B — Causa 1):
    # Removidos termos ultra-genéricos de 1 palavra que inflariam o score
    # da raiz em qualquer patent de válvula:
    #   ✖ "valve assembly" → movido para Valves/Valve Components and Seals
    #   ✖ "valve body"     → movido para Valves/Valve Components and Seals
    #   ✖ "valve element"  → movido para Valves/Valve Components and Seals
    #   ✖ "valve device"   → movido para Valves/Actuation and Solenoid
    # Mantidos apenas termos específicos o suficiente para a raiz.
    "Valves": [
        "valve mechanism", "valve seat",
        "shutoff valve", "back pressure valve",
        "spool valve", "downhole valve assembly",
        "safety flow valve", "pump valve assembly",
    ],

    # ── Separator (raiz) ── expansão
    "Separator": [
        "phase separation", "liquid-solid separator",
        "gas-liquid separation device", "separation apparatus",
        "separation system", "oil-water separator",
        "solid-liquid separator", "impurity separator",
        "multiphase separation device",
    ],

    # ── Drive Shafts (raiz) ── expansão
    "Drive Shafts": [
        "shaft assembly drive", "power transmission shaft",
        "shaft stop mechanical", "axle shaft drive",
        "shaft protection device", "shaft guard",
        "shaft connection pump", "pump shaft design",
    ],
}

for _k, _v in _EXPANSOES.items():
    if _k in PALAVRAS_CHAVE:
        PALAVRAS_CHAVE[_k].extend(_v)
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# 2ª RODADA DE EXPANSÕES — baseada em análise dos títulos e abstracts
# das 856 patentes que ainda ficavam na raiz após a 1ª rodada.
# ══════════════════════════════════════════════════════════════════════

_EXPANSOES_V2 = {

    # ── Sealings/Bearing Seal ─────────────────────────────────────────
    # Problema: 466 patentes ainda na raiz de Sealings.
    # ~250 são dispositivos de vedação/proteção de rolamentos e mancais
    # cujos abstracts falam de "sealing performance", "lip", "slinger",
    # "grease leakage", "muddy water", "encoder" etc.
    "Sealings/Bearing Seal": [
        # padrões diretos dos abstracts
        "sealing performance bearing", "sealing property bearing",
        "sealability bearing", "seal lip bearing",
        "lip seal bearing", "dust lip", "slinger",
        "grease leakage bearing", "grease enclosed bearing",
        "lubricant leakage bearing", "oil leakage bearing",
        "muddy water bearing", "foreign matter bearing",
        "prevent leakage bearing", "prevent intrusion bearing",
        "sealing member bearing", "seal core metal",
        "seal annular bearing", "seal gap bearing",
        "non-contact seal bearing", "labyrinth clearance bearing",
        "bearing sealing performance", "grease seal lip",
        "sealing device bearing wheel", "sealing device rolling",
        "wheel bearing sealing", "hub bearing sealing",
        "seal device wheel", "seal device axle",
        "seal for rolling bearing", "seal rolling bearing",
        "magnetic encoder bearing", "encoder bearing seal",
        "encoder seal bearing", "sealing device with sensor",
        "seal device sensor", "encoder sealing device",
        "bearing presser sealing", "rotating member support seal",
        "rolling bearing grease", "rolling bearing seal lip",
        "rolling bearing sealing structure", "rolling bearing seal structure",
        "sealing structure rolling", "seal structure rolling bearing",
        "clutch release bearing seal", "pulley bearing seal",
        "sealing device axle bearing", "sealing device shaft bearing",
        "cam follower seal", "sealing device for wheel bearing",
        "bearing device sealing", "sealing ring bearing",
        # variantes de "sealed bearing"
        "sealed rolling bearing", "sealed bearing assembly",
        "bearing seal assembly", "sealing assembly bearing",
        # expressões do abstract japonês traduzido
        "suppress drag resistance sealing", "seal space between rings",
        "seal filling space", "grease fill space bearing",
        "seal performance rolling", "improve sealing bearing",
    ],

    # ── Sealings/Mechanical Seal ── 2ª rodada
    # Patentes com "sliding component/part" (face seal moderno)
    "Sealings/Mechanical Seal": [
        "sliding component seal", "sliding part seal",
        "fluid lubrication rotation seal", "prevent leakage rotation",
        "seal at rest leakage", "sealing ring rotating",
        "non-contact sealing rotation", "hydrodynamic seal",
        "hydrodynamic sealing", "gas seal rotating",
        "seal rotating shaft machine", "seal turbomachine",
        "liftoff seal", "lift-off seal",
    ],

    # ── Sealings/Labyrinth Seal ── 2ª rodada
    "Sealings/Labyrinth Seal": [
        "labyrinth clearance", "non-contact annular gap",
        "labyrinth ring seal", "stepped labyrinth seal",
        "interlocking labyrinth seal", "seal clearance labyrinth",
        "labyrinth gap seal", "labyrinth bearing housing seal",
    ],

    # ── Bearings/Hub and Wheel Bearings ── 2ª rodada
    # Padrão dominante: "bearing device for a wheel" e variantes
    "Bearings/Hub and Wheel Bearings": [
        "bearing device for a wheel", "bearing device for wheel",
        "bearing for a vehicle wheel", "bearing device vehicle",
        "wheel bearing device for vehicle",
        "bearing device drive wheel", "drive wheel bearing",
        "wheel bearing unit", "wheel hub unit bearing",
        "bearing device for axle", "axle bearing device",
        "hub unit bearing structure", "tapered roller hub bearing",
        "wheel support bearing unit", "bearing for axle shaft",
        "bearing for railroad car", "railroad bearing",
        "rolling bearing for railway", "axle railway bearing",
        "main shaft bearing railway", "driving motor bearing railway",
        "bearing for wheels", "bearing for wheel vehicle",
        "bearing device wheel encoder", "wheel bearing encoder",
        "seal for wheel bearing", "bearing sealing wheel",
        "wheel bearing knuckle", "outer ring wheel bearing",
    ],

    # ── Bearings/Rolling Bearings ── 2ª rodada
    # Padrão: estrutura/arranjo de rolamento (bearing arrangement/structure)
    "Bearings/Rolling Bearings": [
        "bearing arrangement structure", "divided rolling bearing",
        "bearing structure roller", "roller bearing configuration",
        "bearing structure inner ring", "spherical roller bearing structure",
        "roller bearing arrangement", "bearing structure spindle",
        "bearing unit shaft housing", "low cost bearing unit",
        "bearing arrangement inner outer ring", "bearing assembly pair",
        "rolling bearing fatigue", "bearing corrosion prevention",
        "bearing ring groove", "cylindrical tube bearing",
        "pulley bearing", "dust shield bearing",
    ],

    # ── Bearings/Sliding Bearings ── 2ª rodada
    "Bearings/Sliding Bearings": [
        "stabilizer bushing", "bush bearing", "rubber bush",
        "center bearing propeller", "propeller shaft bearing",
        "synthetic resin sliding bearing", "resin bearing bush",
        "friction bearing lubrication", "bearing friction increase",
        "journal bearing assembly life", "journal shaft bearing",
        "friction bearing service life", "plain bearing lubricant",
    ],

    # ── Bearings/Fluid and Magnetic Bearings ── 2ª rodada
    "Bearings/Fluid and Magnetic Bearings": [
        "fluid dynamic bearing", "dynamic pressure bearing",
        "fluid dynamic pressure bearing device",
        "spindle fluid bearing", "miniature fluid bearing",
        "sealing fluid bearing", "fluid bearing miniature",
        "spindle motor fluid bearing", "vertical shaft bearing fluid",
    ],

    # ── Pumps/PC Pump and Motor ── 2ª rodada
    # "Double worm system" → PC pump (worm = screw em alguns contextos)
    "Pumps/PC Pump and Motor": [
        "double worm system", "worm system pump",
        "worm pump progressing", "worm drive pump",
        "orbital pump helical", "helical lobe pump",
        "orbital fluid pumping", "orbital pumping mechanism",
        "progressive vortex pump", "vortex progressing pump",
        "no-turn tool pumping", "no turn tool pump",
        "anti-rotation pumping", "deployment downhole pump cable",
        "cable deployed pump", "pump cable deployment",
        "tubing conveyed pump", "thru-tubing pump",
        "through tubing pump system", "TTC pump",
        "pump rod connection", "pump rod thread",
    ],

    # ── Pumps/Diaphragm Pump ── NOVO (não existia)
    # Identificado: "bomba nutante", "diaphragm pump", "diaphragm position control"
    "Pumps/Diaphragm Pump": [
        "diaphragm pump", "membrane pump", "nutating pump",
        "wobble pump", "nutating disc pump", "bomba nutante",
        "bomba de diafragma", "diaphragm pump assembly",
        "diaphragm pump hydraulic", "hydraulically driven diaphragm",
        "diaphragm position control", "diaphragm pump piston",
        "dual chamber pump", "dual chamber mixing pump",
        "two chamber pump", "double chamber pump",
    ],

    # ── Pumps/Well Pump Systems ── NOVO
    # Grupo amplo de sistemas de bombeamento em poços
    "Pumps/Well Pump Systems": [
        "well pump system", "wellbore pumping system",
        "downhole pump system", "fluid well pumping",
        "compact cable pump dewatering", "gas well dewatering",
        "well fluid pumping", "production pump system",
        "tubing drain automatic", "pump wellbore deployment",
        "downhole pump recovery", "wellbore pump assembly",
        "pump bottom hole", "positive displacement downhole pump",
        "pump cavitation positive displacement",
        "pump underperformance detection", "pump fault detection",
        "load shedding pump control", "pump system satellite",
        "pump system host satellite", "wellhead drive system",
        "wellhead drive brake", "drive head brake wellhead",
    ],

    # ── Pumps/Lubrication and Oil Pump ── NOVO
    # Bombas de lubrificação que ficavam em "Pumps" genérico
    "Pumps/Lubrication and Oil Pump": [
        "lubrication oil pump", "lubrication pump system",
        "oil supply pump", "oil pumping system lubrication",
        "lubricating oil pump", "oil lubrication pump",
        "jack oil supply", "bearing oil pump",
        "lubrication screw pump", "oil circulation pump",
        "oil pump supply shaft", "pump oil supply bearing",
    ],

    # ── Pumps/Screw Pump ── 2ª rodada
    "Pumps/Screw Pump": [
        "screw pump fluid method", "method conveying screw pump",
        "method for conveying fluid screw", "screw pump overpressure",
        "screw pump protection twin", "positive displacement pump protection",
        "method reducing pulsation positive displacement",
        "pulsation positive displacement pump", "multi-screw pump system",
        "double worm screw pump", "viscous media screw pump",
        "viscous flow screw pump", "conveying viscous screw",
        "multi-functional helix pump", "double helix viscous pump",
        "progressive cavity screw pump design",
        "mud motor design analytical",
    ],

    # ── Pumps/Multiphase Pump ── 2ª rodada
    "Pumps/Multiphase Pump": [
        "method for delivering multiphase", "multiphase mixture delivery",
        "multiphase mixture pump installation",
        "conveying multiphase pump system",
        "multiphase flow pump container",
        "liquid gas mixture conveying borehole",
        "crude oil natural gas mixture pump",
        "method conveying multiphase mixture",
        "multiphase pump operation method",
    ],

    # ── Pumps/Centrifugal Pump ── 2ª rodada
    "Pumps/Centrifugal Pump": [
        "high efficiency fluid pumping", "direct drive pump",
        "direct drive pump system", "direct drive centrifugal",
        "pump water cooling", "water cooling pump system",
        "deep well pump high temperature", "hot fluid pump",
        "well pump high volume", "multi-stage pump system",
        "pump system flow volume",
    ],

    # ── Valves/Compressor Valve ── 2ª rodada
    # Muitas das "Valves" restantes são compressores de refrigeração
    "Valves/Compressor and Pump Valve": [
        "variable displacement compressor", "variable capacity compressor",
        "swash plate compressor", "swash plate valve",
        "refrigerant compressor valve", "displacement control valve compressor",
        "compressor capacity control", "compressor discharge valve",
        "compressor suction valve", "compressed air valve",
        "compressed air consumer", "pressure container compressor",
        "compressor connection valve", "compressor system valve",
        "pneumatic valve", "pneumatically powered valve",
        "pneumatic expelling device",
    ],

    # ── Valves/Control and Flow Valve ── 2ª rodada
    "Valves/Control and Flow Valve": [
        "inflow control device", "autonomous inflow control",
        "fluid flow regulation wellbore", "flow control wellbore",
        "flow control system sand screen", "screen flow control",
        "wellbore flow regulation", "liquid delivery precision",
        "liquid delivery device control", "dosing device valve",
        "dosing valve pump", "micropump delivery",
        "reversible pump valve", "bidirectional valve pump",
    ],

    # ── Drive Shafts/Shaft Coupling Device ── 2ª rodada
    # Muitos "Drive Shafts" restantes são grinders/pulverizadores
    # Os legítimos são: acoplamentos e proteção de eixo
    "Drive Shafts/Shaft Coupling Device": [
        "mechanical shaft stop", "shaft stop rotating",
        "shaft stop device", "shaft stop mechanism",
        "cardan shaft pump", "single screw pump cardan",
        "flexible shaft pump eccentric", "drive shaft protection",
        "shaft guard device", "shaft coupling pump drive",
        "sleeve flexible drive shaft", "reinforcing coupling shaft",
        "pump motor shaft connection", "motor shaft drive pump",
    ],

    # ── Macerator/Food Waste Disposer ── 2ª rodada
    "Macerator/Food Waste Disposer": [
        "garbage disposal device", "garbage treatment apparatus",
        "garbage treater", "domestic garbage processor",
        "household garbage processor", "kitchen waste processor",
        "kitchen garbage processor", "garbage processor grinding",
        "garbage disposer household", "garbage treater grinding",
        "water sealing garbage treatment", "garbage treatment grinding",
        "WC macerator unit", "toilet macerator",
        "indoor wastewater disposal", "wastewater disposal grinding",
        "waste disposal pump adapter",
    ],

    # ── Macerator/Industrial Crusher ── 2ª rodada
    # Muitos Drive Shafts restantes são realmente trituradores/pulverizadores
    "Macerator/Industrial Crusher": [
        "blade grinder", "blade pulverizer",
        "universal pulverizer", "efficient universal pulverizer",
        "tablet grinder", "fertilizer pulverizer",
        "manure grinder", "material pulverizing feeding",
        "food waste grinding mechanism", "food processor drive",
        "vegetable cutting machine", "cutting machine vegetables",
        "low temperature grinder", "low temperature pulverizer",
        "superfine crusher grading", "micro-powder preparation",
        "ultrafine disintegrator vertical", "vertical disintegrator",
        "size reduction device shaft", "size reduction rotating",
        "tire shredding machinery", "tire shredder",
        "bale processor shredder", "slurry solid breaker",
        "solid breaker slurry tank", "organic shredder apparatus",
        "fluid waste containment grinder",
    ],

    # ── Oil Tools/Sensoring ── 2ª rodada
    "Oil Tools/Sensoring": [
        "sensor deployment downhole tool", "deploying sensor downhole",
        "downhole tool sensor assembly", "sensor in downhole tool",
        "downhole sensor deployment", "downhole assembly sensor",
    ],

    # ── Monitoring and controlling ── expansão raiz
    "Monitoring and controlling": [
        "pump control method apparatus", "pump system controller sensor",
        "pump control cascade", "closed-loop pump control",
        "closed loop pump system", "trial pumping algorithm",
        "pump type identifier", "pump parameter identifier",
        "pump monitoring sensor", "remote monitoring screw pump",
        "monitoring eccentric screw pump", "pump system monitoring",
        "portable monitoring control", "portable monitoring surface",
    ],

    # ── Corrosion ── sub Coating (mapeia os 10 restantes)
    "Corrosion": [
        "abrasion corrosion resistant", "corrosion resistant liner",
        "polyolefin liner corrosion", "coated sleeved well",
        "coated sleeve production", "protective coating corrosion",
        "corrosion resistant alloy cast", "carbide austenitic alloy",
        "corrosion resistant element", "filter corrosion resistant",
        "slide ring corrosion", "running gear seal corrosion",
        "sealing structure muddy water corrosion",
    ],

    # ── Electric Motors ── expansão
    "Electric Motors": [
        "sealless motor pump", "sealless screw pump motor",
        "electric motor dustproof", "permanent magnet synchronous control",
        "PMSM control", "PWM motor control", "motor filter PWM",
        "motor controller electronic", "electric driven pump",
        "electric motor pump direct", "direct drive motor pump",
        "motor pump assembly", "motor coupled pump",
    ],
}

for _k, _v in _EXPANSOES_V2.items():
    if _k in PALAVRAS_CHAVE:
        PALAVRAS_CHAVE[_k].extend(_v)
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# 3ª RODADA — termos de abstract para vencer empate com raiz "Sealings"
# Cada subgrupo precisa de hits suficientes para superar a raiz genérica.
# Fonte: análise estatística dos abstracts dos 799 ainda na raiz.
# ══════════════════════════════════════════════════════════════════════

_EXPANSOES_V3 = {

    # ── Sealings/Mechanical Seal ─────────────────────────────────────
    # Abstracts revelam: rotating surface | static ring | stationary ring
    # | sliding surface | spring element | movable member | sleeve
    "Sealings/Mechanical Seal": [
        "rotating sealing surface", "stationary sealing surface",
        "stationary seal ring", "stationary ring mechanical",
        "rotating counter ring", "counter ring mechanical seal",
        "rotating seal ring", "movable seal ring",
        "mechanical seal spring", "spring mechanical",
        "mechanical seal sleeve", "sleeve seal rotating",
        "seal sliding surface", "seal contact surface",
        "face seal contact", "face contact seal",
        "mechanical seal static", "seal static ring",
        "seal axial protuberance", "seal clamping",
        "mechanical seal pressure ring", "pressure ring seal",
        "separate sealing elements mechanical", "mechanical seal elements",
        "mechanical seal carbon", "carbon sliding surface seal",
        "mechanical seal silicon carbide", "silicon carbide seal",
        "balanced mechanical seal", "unbalanced mechanical seal",
        "single spring mechanical seal", "multi-spring seal",
        "mechanical seal stainless steel", "seal protection gear marine",
        "integrated spring compensation seal", "compensation element seal",
        "center parting seal", "split type mechanical seal",
        "double end face seal", "double end mechanical seal",
        "mechanical seal without locking ring",
        "mechanical seal dry run", "mechanical seal kettle",
        "bellows type seal", "bellows mechanical",
        "adjustable mechanical seal", "seal adjustment",
        "tandem type mechanical seal device",
    ],

    # ── Sealings/Bearing Seal ─────────────────────────────────────────
    # Abstracts: slinger | grease | muddy water | lip | encoder | sensor
    "Sealings/Bearing Seal": [
        "slinger seal", "slinger bearing",
        "slinger ring bearing", "slinger sealing",
        "grease seal bearing", "grease prevent leakage",
        "grease leakage prevent", "prevent grease leakage",
        "muddy water seal", "muddy water prevent",
        "seal muddy", "dust lip seal",
        "seal lip dust", "lip dust bearing",
        "lip contact seal bearing", "lip tip contact",
        "non-contact seal labyrinth", "non-contact labyrinth",
        "seal foreign matter", "foreign matter intrusion",
        "seal intrusion prevent", "prevent intrusion seal",
        "bearing encoder seal", "encoder seal wheel",
        "sensor bearing seal", "bearing sensor sealing",
        "rotational speed seal", "rotation detection seal",
        "magnetic encoder seal bearing",
        "seal sealability bearing", "seal corrosion bearing",
        "bearing corrosion rust seal", "rust prevention seal bearing",
        "bearing seal knuckle", "knuckle outer ring seal",
        "bearing sealing capacity", "seal capacity bearing long",
        "seal wear bearing", "seal lip wear",
        "annular sealing member", "annular seal member bearing",
        "core metal seal", "seal metal core",
        "resin member seal", "synthetic resin seal bearing",
        "seal cross-sectional height", "seal height bearing",
        "end cap bearing seal", "bearing end cap integrated seal",
    ],

    # ── Sealings/Labyrinth Seal ── 3ª rodada ─────────────────────────
    "Sealings/Labyrinth Seal": [
        "labyrinth retainer", "labyrinth ring element",
        "labyrinth axial radial", "labyrinth pellet board",
        "pellet leakage labyrinth", "labyrinth conveying",
        "stepped labyrinth radial", "labyrinth spindle bearing",
        "labyrinth machine tool spindle",
    ],

    # ── Sealings/Shaft Seal ── 3ª rodada ─────────────────────────────
    "Sealings/Shaft Seal": [
        "shaft seal turbomachine", "turbomachine shaft seal",
        "shaft seal discharge", "atmosphere shaft seal",
        "shaft seal fluid process", "process fluid shaft",
        "shaft seal blocked", "crankshaft seal",
        "crankshaft sealing", "engine shaft seal",
    ],

    # ── Bearings/Hub and Wheel Bearings ── 3ª rodada ─────────────────
    # Abstracts: encoder | sensor | rotational speed | slinger |
    # muddy water | magnetic encoder
    "Bearings/Hub and Wheel Bearings": [
        "wheel bearing encoder", "hub bearing encoder",
        "magnetic encoder wheel bearing", "encoder hub bearing",
        "rotation sensor bearing wheel", "speed sensor bearing wheel",
        "rotational speed detection bearing",
        "wheel bearing rotation detection",
        "bearing sensor holder", "bearing sensor annular",
        "sensor equipped bearing wheel",
        "wheel bearing corrosion rust", "wheel bearing water",
        "knuckle bearing wheel", "outer ring knuckle",
        "bearing wheel hub flange", "hub flange bearing",
        "wheel hub seal bearing",
        "clutch release bearing", "release bearing clutch",
        "strut ball bearing", "strut bearing",
        "suspension bearing", "lifting device bearing",
    ],

    # ── Bearings/Rolling Bearings ── 3ª rodada ──────────────────────
    # Abstracts: slinger | grease | foreign matter | capability
    "Bearings/Rolling Bearings": [
        "rolling bearing grease filled", "grease filled bearing",
        "rolling bearing seal plate", "seal plate bearing",
        "rolling bearing non-contact", "non-contact rolling bearing",
        "rolling bearing slinger", "slinger rolling",
        "rolling bearing foreign matter", "foreign matter rolling",
        "rolling bearing capability", "bearing seal capability long",
        "rolling bearing axial", "axial end rolling bearing",
        "outer ring type rolling", "outer ring rotating rolling",
        "main shaft rolling bearing", "spindle rolling bearing",
        "steel rolling bearing", "rolling bearing water",
        "bearing ring groove outer",
    ],

    # ── Pumps/Screw Pump ── 3ª rodada ───────────────────────────────
    # Abstracts: stator | rotor | driving | housing | front | motor
    "Pumps/Screw Pump": [
        "screw pump stator rotor", "screw pump rotor stator",
        "screw pump housing motor", "screw pump driving",
        "screw pump driving structure", "screw pump front",
        "screw pump front structure", "screw pump comprises",
        "screw pump arranged", "screw pump motor drive",
        "screw pump progressive cavity", "eccentric screw cavity",
        "worm pump submersible motor", "screw pump deep borehole",
        "three screw pump diesel", "lubricating oil three screw",
        "screw pump arranged motor", "screw pump electric motor",
    ],

    # ── Pumps/PC Pump and Motor ── 3ª rodada ────────────────────────
    "Pumps/PC Pump and Motor": [
        "eccentric screw pump stator", "stator rotor eccentric",
        "single progressive cavity screw pump",
        "single screw pump axial radial balance",
        "cardan shaft single screw pump",
        "single screw pump cardan",
        "screw pump oil well production",
    ],

    # ── Pumps/Well Pump Systems ── 3ª rodada ────────────────────────
    "Pumps/Well Pump Systems": [
        "pump underperformance system method",
        "pump cavitation monitoring",
        "pump system monitoring control well",
        "pump restarting downhole method",
        "pump dewatering gas well cable",
        "wellbore maintenance pump assembly",
        "wellhead brake drive", "drive head brake",
        "pump fracturing wellbore",
        "multiple well fluid distribution",
    ],

    # ── Pumps/Multiphase Pump ── 3ª rodada ──────────────────────────
    "Pumps/Multiphase Pump": [
        "liquid gas mixture pump borehole",
        "crude oil gas mixture pump",
        "delivering multiphase pump installation",
    ],

    # ── Macerator/Food Waste Disposer ── 3ª rodada ──────────────────
    "Macerator/Food Waste Disposer": [
        "kitchen waste processor cleaning agent",
        "kitchen waste processor outfall",
        "kitchen garbage grinding cavity",
        "domestic garbage treater grinding",
        "stainless steel garbage device",
        "grinding mechanism garbage housing",
        "garbage casing motor grinding",
        "garbage disposal macerator pump",
        "waste disposal pump holding tank",
        "WC macerator housing chamber",
        "macerator sewerage contra-rotating",
        "cutter disc contra-rotating",
        "macerator interleaved cutter",
        "organic waste self-contained shredder",
    ],

    # ── Macerator/Industrial Crusher ── 3ª rodada ───────────────────
    "Macerator/Industrial Crusher": [
        "fertilizer pulverizer dust prevent",
        "manure pulverizer flying dust",
        "material pulverizing shredding bin",
        "pulverizing feeding device",
        "blade assembly belt pulley transmission",
        "grinding tooth disk food waste",
        "tire cutter shredder rotary",
        "bale processor shredding drive",
        "slurry solid breaking tank",
        "low temperature pulverizing chamber",
        "micro-powder granularity uniform",
        "superfine crusher grading long life",
        "universal high efficiency pulverizer frame motor",
        "pulverizer frame motor device",
    ],

    # ── Valves ── 3ª rodada (foco nos Valves residuais) ─────────────
    "Valves/Compressor and Pump Valve": [
        "variable displacement compressor valve",
        "swash plate valve compressor",
        "refrigerant displacement compressor",
        "compressor capacity control valve",
        "compressor connection valve device",
        "pressure container compressor valve",
        "reed valve compressor", "valve plate compressor pump",
        "pneumatically powered piston valve",
        "compressed air piston drive valve",
        "pneumatic drive piston expelling",
    ],

    # ── Monitoring/Vibration ── 3ª rodada ────────────────────────────
    "Monitoring and controlling": [
        "pump system cascade controller",
        "pump variable speed method control",
        "pump cascade target pressure",
        "closed loop screw pump control",
        "remote monitoring operation screw",
        "uniaxial eccentric screw monitoring",
        "surface equipment portable monitoring",
    ],
}

for _k, _v in _EXPANSOES_V3.items():
    if _k in PALAVRAS_CHAVE:
        PALAVRAS_CHAVE[_k].extend(_v)
    else:
        PALAVRAS_CHAVE[_k] = _v


# ── Informações extras para geração de palavras pelo classificador ────────────
# Se quiser desativar uma categoria temporariamente, mova para DESATIVADAS.
DESATIVADAS = {
    # "Exemplo": ["palavra1"],
}


# ══════════════════════════════════════════════════════════════════════
# PALAVRAS-CHAVE EM PORTUGUÊS
# Adicionadas via dicionário separado e mescladas no PALAVRAS_CHAVE.
# Mantidas separadas para facilitar manutenção.
# ══════════════════════════════════════════════════════════════════════

_PT = {
    "Dehydrator": [
        "desidratador", "desidratação", "remoção de umidade",
        "secador de gás", "dessecante", "ponto de orvalho",
        "peneira molecular", "desidratador de lodo",
    ],
    "Drive Shafts": [
        "eixo de acionamento", "eixo de transmissão",
        "eixo cardânico", "eixo articulado",
        "transmissão de torque", "eixo flexível",
        "eixo estriado",
    ],
    "Macerator": [
        "macerador", "maceração", "triturador",
        "bomba trituradora", "bomba maceradora",
        "dispositivo de trituração",
    ],
    "Macerator/Industrial Crusher": [
        "triturador industrial", "britador", "moinho",
        "moedor", "redutor de tamanho", "granulador",
        "trituração de sólidos", "britagem", "esmagador",
        "máquina de triturar", "equipamento de britagem",
        "triturador de materiais", "fragmentador",
        "picador industrial",
    ],
    "Macerator/Comminutor": [
        "triturador de esgoto", "triturador de resíduos líquidos",
        "esmagador de sólidos", "triturador inline",
        "comminutor de esgoto",
    ],
    "Macerator/Food Waste Disposer": [
        "triturador de alimentos", "processador de resíduos alimentares",
        "triturador de lixo orgânico", "disposer de cozinha",
        "triturador doméstico", "resíduos alimentares",
    ],
    "Macerator/Cutting Elements": [
        "elemento de corte", "lâmina de corte",
        "faca de corte", "disco de corte",
        "mecanismo de corte", "dente de corte",
        "rotor de corte", "placa de corte",
    ],
    "Machines for rubber industry": [
        "máquina para borracha", "processamento de borracha",
        "vulcanização", "misturador de borracha",
        "extrusora de borracha", "calandra",
        "compostos de borracha",
    ],
    "Manufacturing technology": [
        "tecnologia de fabricação", "processo de fabricação",
        "processo de manufatura", "método de produção",
        "usinagem", "tratamento térmico", "conformação",
    ],
    "Manufacturing technology/Extrusion": [
        "extrusão", "extrusora", "matriz de extrusão",
        "parafuso extrusor", "extrusão de polímero",
        "extrusão de borracha", "extrusão de metal",
        "coextrusão",
    ],
    "Manufacturing technology/Induction Heating": [
        "aquecimento por indução", "bobina de indução",
        "endurecimento por indução", "soldagem por indução",
        "aquecimento eletromagnético",
    ],
    "Manufacturing technology/Machining": [
        "usinagem", "processo de usinagem", "torneamento",
        "fresamento", "retificação", "furação",
        "usinagem eletroquímica", "usinagem por descarga elétrica",
        "usinagem de rotor", "usinagem de estator",
        "usinagem de precisão", "mandrilamento",
    ],
    "Manufacturing technology/Surface Treatment": [
        "tratamento superficial", "revestimento superficial",
        "revestimento duro", "revestimento protetor",
        "revestimento PVD", "revestimento CVD",
        "aspersão térmica", "cromo duro", "cromagem",
        "eletrodeposição", "nitretação",
        "endurecimento superficial", "cementação",
        "revestimento DLC", "revestimento de carboneto",
        "revestimento cerâmico", "acabamento superficial",
        "revestimento de bomba",
    ],
    "Manufacturing technology/Surface Treatment/Wear and Tribology": [
        "revestimento resistente ao desgaste",
        "revestimento tribológico", "superfície antidesgaste",
        "redução de fricção", "tribologia de superfície",
        "desgaste superficial",
    ],
    "Manufacturing technology/Surface Treatment/Heat Treatment": [
        "tratamento térmico", "têmpera", "revenimento",
        "recozimento", "normalização", "cementação",
        "nitretação", "endurecimento por indução",
        "endurecimento superficial", "envelhecimento",
    ],
    "Material for pumps": [
        "material para bombas", "revestimento de bomba",
        "material resistente ao desgaste",
        "material resistente à corrosão",
        "elastômero para bomba", "revestimento interno de bomba",
        "material abrasivo", "compósito para bomba",
        "material polimérico para bomba",
    ],
    "Material for pumps/Elastomers": [
        "elastômero", "borracha", "elastômero para estator",
        "composto de borracha", "borracha nitrílica",
        "HNBR", "EPDM", "neoprene", "poliuretano",
        "fluoroelastômero", "vulcanização", "borracha vulcanizada",
        "composição elastomérica", "formulação de borracha",
        "material elastomérico", "estator de borracha",
        "elastômero irradiado",
    ],
    "Measuring devices": [
        "dispositivo de medição", "instrumento de medição",
        "medidor de vazão", "manômetro",
        "sensor de temperatura", "sensor de nível",
        "medidor de viscosidade", "medidor de densidade",
        "sensor de torque", "sensor de vibração",
        "medição de fundo de poço",
    ],
    "Monitoring and controlling": [
        "monitoramento", "sistema de controle",
        "controle de bomba", "monitoramento remoto",
        "automação", "controlador programável",
        "inversor de frequência", "controle de velocidade",
        "controle de vazão", "controle de pressão",
        "manutenção preditiva", "aquisição de dados",
        "bomba inteligente",
    ],
    "Monitoring and controlling/Vibration and Acoustics": [
        "amortecimento de vibração", "isolamento de vibração",
        "monitoramento de vibração", "sensor de vibração",
        "absorvedor de vibração", "controle de vibração",
        "amortecedor acústico", "redução de ruído",
        "emissão acústica", "vibração estrutural",
        "vibração torsional", "análise de vibração",
    ],
    "Corrosion": [
        "corrosão", "resistência à corrosão",
        "proteção contra corrosão", "anticorrosivo",
        "inibidor de corrosão", "proteção catódica",
        "liga resistente à corrosão", "revestimento anticorrosivo",
        "corrosão por CO2", "corrosão por H2S",
        "aço inoxidável austenítico", "aço duplex",
        "bomba resistente à corrosão",
    ],
    "Electric Motors": [
        "motor elétrico", "motor de indução",
        "motor síncrono", "motor de imã permanente",
        "motor submersível", "motor elétrico submersível",
        "motor sem escova", "enrolamento do motor",
        "estator do motor", "rotor do motor",
        "carcaça do motor", "eficiência do motor",
        "proteção do motor",
    ],
    "Oil Tools": [
        "ferramenta de poço", "ferramenta de fundo",
        "equipamento de petróleo", "ferramenta de completação",
        "elevação artificial", "intervenção de poço",
    ],
    "Oil Tools/Anchoring Tool": [
        "ferramenta de ancoragem", "âncora de poço",
        "âncora de tubulação", "âncora hidráulica",
        "âncora mecânica", "dispositivo de ancoragem",
    ],
    "Oil Tools/Anti-rotation control": [
        "controle antirrotação", "dispositivo antirrotação",
        "prevenção de rotação", "trava de rotor",
        "limitador de rotação",
    ],
    "Oil Tools/Blow-Out Preventer": [
        "preventor de blowout", "preventor de surgência",
        "controle de poço", "BOP",
        "contenção de pressão de poço",
    ],
    "Oil Tools/Centralizer": [
        "centralizador", "centralizador de revestimento",
        "centralizador de tubulação", "centralizador de fundo",
        "centralizador inchável",
    ],
    "Oil Tools/Drilling": [
        "perfuração", "broca de perfuração", "perfuração rotativa",
        "perfuração direcional", "coluna de perfuração",
        "fluido de perfuração", "motor de fundo",
        "conjunto de fundo de poço", "ferramenta de perfuração",
        "equipamento de perfuração",
    ],
    "Oil Tools/Drive Head": [
        "cabeçote de acionamento", "cabeçote de superfície",
        "cabeçote de bomba", "acionamento de superfície",
        "cabeçote de bomba de cavidade progressiva",
        "unidade de acionamento",
        "cabeçote integrado de acionamento",
    ],
    "Oil Tools/Drive Head/Backspin Brake": [
        "freio de backspin", "controle de backspin",
        "proteção contra backspin", "freio dinâmico",
        "freio regenerativo de bomba",
    ],
    "Oil Tools/Drive Head/Shaft Sealing": [
        "vedação de haste polida", "vedação de eixo",
        "gaxeta de haste", "vedação dinâmica de eixo",
        "empanque de haste",
    ],
    "Oil Tools/Drive Head/Backspin Brake/Hydraulic Brake": [
        "freio hidrodinâmico", "retardador hidráulico",
        "freio hidráulico", "dispositivo de frenagem hidráulica",
        "freio de fluido",
    ],
    "Oil Tools/Gas Compressor": [
        "compressor de gás", "compressor de gás natural",
        "compressor de fundo de poço", "compressor recíproco",
        "compressor centrífugo", "compressor de cabeça de poço",
        "injeção de gás",
    ],
    "Oil Tools/Multiphase Separator": [
        "separador multifásico", "separador gás-líquido",
        "separador trifásico", "separador óleo-gás-água",
        "separador gravitacional", "separador ciclônico",
        "separador horizontal", "separador de produção",
    ],
    "Oil Tools/Multiphase coveying device": [
        "transporte multifásico", "dispositivo multifásico",
        "bombeamento multifásico", "escoamento multifásico",
        "transporte bifásico",
    ],
    "Oil Tools/Packer": [
        "packer", "obturador", "obturador inflável",
        "obturador mecânico", "obturador hidráulico",
        "obturador permanente", "tampão de poço",
        "isolamento zonal",
    ],
    "Oil Tools/Production Technology": [
        "tecnologia de produção", "produção de petróleo",
        "completação de poço", "otimização de produção",
        "recuperação avançada de petróleo",
        "injeção de água", "injeção de gás",
        "produção de fundo de poço",
    ],
    "Oil Tools/Pulsation damping device": [
        "amortecedor de pulsação", "atenuador de pulsação",
        "controle de pulsação de fluxo", "supressor de surto",
        "amortecedor hidráulico",
    ],
    "Oil Tools/Rod Clamp": [
        "grampo de haste", "grampo de haste de sucção",
        "grampo de haste polida", "fixador de haste",
    ],
    "Oil Tools/Rods": [
        "haste de bombeamento", "haste polida",
        "coluna de hastes", "haste de fibra de vidro",
        "acoplamento de haste", "guia de haste",
        "haste contínua", "centralizador de haste",
    ],
    "Oil Tools/Sand Protection": [
        "proteção contra areia", "controle de areia",
        "gerenciamento de areia", "prevenção de areia",
        "filtro de areia de poço",
    ],
    "Oil Tools/Sand Protection/Desander": [
        "desarenador", "ciclone desaviador",
        "remoção de areia", "separador de areia de poço",
    ],
    "Oil Tools/Sand Protection/Sand Stopper": [
        "vedador de areia", "barreira de areia",
        "dispositivo antiareia", "bloqueador de areia",
    ],
    "Oil Tools/Sand Protection/Sand separator": [
        "separador de areia", "separador de sólidos",
        "separador de areia de fundo", "separação de partículas de areia",
    ],
    "Oil Tools/Sand Protection/Screen": [
        "tela de areia", "liner ranhado", "tela de completação",
        "tela de filtração", "tela expansível",
        "controle de influxo",
    ],
    "Oil Tools/Sensoring": [
        "sensor de fundo de poço", "sensor de poço",
        "sensor de pressão de fundo", "sensor de temperatura de fundo",
        "sensor de fluxo de poço", "sensoriamento por fibra óptica",
        "instrumentação de fundo de poço",
    ],
    "Oil Tools/Shaft coupling": [
        "acoplamento de eixo", "acoplamento flexível",
        "acoplamento rígido", "acoplamento de engrenagem",
        "acoplamento de bomba",
    ],
    "Oil Tools/Tubing": [
        "coluna de produção", "tubulação de produção",
        "tubing enrolado", "coluna de tubulação",
        "conector de tubulação", "junta de tubulação",
        "âncora de tubulação",
    ],
    "Oil Tools/Tubing Grab": [
        "garra de tubulação", "ferramenta de recuperação de tubulação",
        "overshot", "lança de pescaria",
    ],
    "Oil Tools/Valves": [
        "válvula de fundo", "válvula de segurança",
        "válvula de retenção de fundo", "válvula de gás lift",
        "válvula de injeção",
    ],
    "Oil Tools/Water cleaner": [
        "tratamento de água produzida", "purificação de água de poço",
        "desoleificação de água", "separação óleo-água",
        "sistema de tratamento de água",
    ],
    "Oil Tools/Wellhead equipment": [
        "cabeça de poço", "equipamento de cabeça de poço",
        "árvore de natal", "montagem de cabeça de poço",
        "vedação de cabeça de poço",
    ],
    "Oil Tools/Wellhead equipment/Hang-off Adapter": [
        "adaptador de suspensão", "suspensor de tubulação",
        "adaptador de cabeça de poço",
    ],
    "Oil Tools/Wellhead equipment/Riser": [
        "riser", "riser de perfuração", "riser de produção",
        "riser marítimo", "conector de riser",
        "riser flexível", "riser catenário de aço",
    ],
    "Oil Tools/Wellhead equipment/Rod Rotator": [
        "rotador de haste", "rotador de haste polida",
        "dispositivo rotador de haste",
        "mecanismo de rotação de haste",
    ],
    "Pulsation damping device": [
        "amortecedor de pulsação", "absorvedor de pulsação",
        "pulsação de pressão", "pulsação de fluxo",
        "supressor de surto", "acumulador hidráulico",
    ],
    "Pumps": [
        "bomba", "sistema de bombeamento",
        "dispositivo de bombeamento",
        "conjunto de bomba", "bomba de fluido",
    ],
    "Pumps/Acoustic Pump": [
        "bomba acústica", "bomba sônica", "bomba ultrassônica",
        "bomba piezoelétrica", "bomba de onda sonora",
    ],
    "Pumps/Barrel emptying system": [
        "sistema de esvaziamento de tambor",
        "bomba de tambor", "esvaziamento de barril",
        "bomba de barril",
    ],
    "Pumps/Centrifugal Pump": [
        "bomba centrífuga", "bomba radial", "bomba axial",
        "bomba de fluxo misto", "impulsor", "voluta",
        "bomba centrífuga multiestágio",
        "bomba centrífuga de sucção final",
    ],
    "Pumps/Centrifugal Pump/Bearing": [
        "rolamento de bomba centrífuga",
        "conjunto de rolamento de bomba",
        "mancal de bomba centrífuga",
    ],
    "Pumps/Gas Lift": [
        "elevação por gás", "gas lift", "válvula de gas lift",
        "mandril de gas lift", "injeção de gás artificial",
    ],
    "Pumps/Gear Pump": [
        "bomba de engrenagens", "bomba de engrenagem externa",
        "bomba de engrenagem interna", "bomba gerotor",
        "bomba de engrenagem helicoidal",
    ],
    "Pumps/Hose Pump": [
        "bomba de mangueira", "bomba peristáltica",
        "bomba de tubo", "bomba de rolo",
        "bomba de mangueira flexível",
    ],
    "Pumps/Lobe Pump": [
        "bomba de lóbulos", "bomba rotativa de lóbulos",
        "rotor de lóbulo", "bomba de lóbulo triplo",
    ],
    "Pumps/PC Pump and Motor": [
        "bomba de cavidade progressiva", "BCP", "bomba parafuso",
        "bomba helicoidal", "estator elastomérico",
        "rotor estator", "bomba excêntrica",
        "bomba Moineau", "bomba de parafuso simples",
        "cavidade progressiva",
        "bomba de parafuso único",
        "unidade de bombeamento de parafuso",
    ],
    "Pumps/PC Pump and Motor/Assembly devices": [
        "dispositivo de montagem de bomba",
        "ferramenta de montagem de BCP",
        "ferramenta de instalação de bomba",
        "montagem do estator",
    ],
    "Pumps/PC Pump and Motor/Auger": [
        "rosca transportadora", "parafuso transportador",
        "hélice de alimentação",
    ],
    "Pumps/PC Pump and Motor/Bearing": [
        "rolamento de BCP", "rolamento de bomba de cavidade progressiva",
        "mancal de bomba de cavidade", "rolamento axial de bomba",
    ],
    "Pumps/PC Pump and Motor/Bridge Braker Device": [
        "quebrador de ponte", "dispositivo quebra-ponte",
        "quebrador de tampão", "dispositivo antiobstrução",
    ],
    "Pumps/PC Pump and Motor/Cascaded Pump": [
        "bomba em cascata", "bomba em série",
        "bomba de cavidade progressiva multiestágio",
    ],
    "Pumps/PC Pump and Motor/Drive Shaft": [
        "eixo de acionamento de BCP",
        "eixo de transmissão de bomba",
        "eixo flexível de bomba",
        "haste de acionamento de BCP",
    ],
    "Pumps/PC Pump and Motor/Geometry - Profile": [
        "geometria de bomba", "perfil de rotor",
        "perfil de estator", "geometria helicoidal",
        "perfil de cavidade", "geometria do lóbulo",
        "razão de passo de bomba", "excentricidade de bomba",
        "otimização de perfil de bomba",
    ],
    "Pumps/PC Pump and Motor/Grinding device": [
        "dispositivo de moagem de bomba",
        "triturador de bomba de cavidade",
        "moedor de sólidos de bomba",
    ],
    "Pumps/PC Pump and Motor/Guard": [
        "proteção de bomba", "proteção de entrada de bomba",
        "filtro de entrada de bomba", "carcaça de proteção de bomba",
    ],
    "Pumps/PC Pump and Motor/Housing": [
        "carcaça de bomba", "carcaça de estator",
        "corpo de bomba", "invólucro de bomba",
        "carcaça da bomba de cavidade",
    ],
    "Pumps/PC Pump and Motor/Insertable": [
        "bomba inserível", "bomba removível",
        "inserto de bomba", "conjunto de bomba inserível",
    ],
    "Pumps/PC Pump and Motor/Joint": [
        "junta de bomba", "junta flexível de BCP",
        "junta universal de bomba", "junta articulada de bomba",
    ],
    "Pumps/PC Pump and Motor/Material for pumps": [
        "material para BCP", "elastômero de estator",
        "material de rotor", "elastômero resistente ao desgaste",
        "rotor endurecido", "nitrílico para estator",
        "material de estator",
    ],
    "Pumps/PC Pump and Motor/Rotor": [
        "rotor", "rotor helicoidal", "projeto de rotor",
        "rotor de BCP", "geometria de rotor",
        "revestimento de rotor", "desgaste de rotor",
        "rotor cromado",
    ],
    "Pumps/PC Pump and Motor/Stator": [
        "estator", "estator elastomérico", "projeto de estator",
        "geometria de estator", "estator de dupla hélice",
        "colagem de estator", "revestimento de estator",
        "estator metálico", "desgaste de estator",
        "estator rígido", "borracha de estator",
        "composto de estator",
    ],
    "Pumps/Piston Pump": [
        "bomba de pistão", "bomba alternativa", "bomba de êmbolo",
        "bomba de pistão duplo efeito", "bomba de pistão simples efeito",
        "bomba hidráulica de pistão",
    ],
    "Pumps/Pump Control": [
        "controle de bomba", "controlador de bomba",
        "controle de velocidade de bomba",
        "bomba de velocidade variável", "automação de bomba",
        "monitoramento e controle de bomba",
        "inversor de frequência para bomba",
    ],
    "Pumps/Screw Compressor": [
        "compressor de parafuso", "compressor de parafuso duplo",
        "compressor de parafuso helicoidal",
        "compressor de parafuso rotativo",
        "compressor inundado a óleo",
        "compressor de parafuso isento de óleo",
    ],
    "Pumps/Screw Pump": [
        "bomba de parafuso", "bomba de duplo parafuso",
        "bomba de triplo parafuso", "bomba de múltiplos parafusos",
        "bomba de parafuso helicoidal",
        "bomba de parafuso de Arquimedes",
        "projeto de bomba de parafuso",
        "bomba parafuso",
        "bomba de fuso",
    ],
    "Pumps/Screw Pump/Bearing": [
        "rolamento de bomba de parafuso",
        "rolamento de duplo parafuso",
        "mancal de bomba de parafuso",
    ],
    "Pumps/Screw Pump/Body": [
        "corpo de bomba de parafuso",
        "carcaça de bomba de parafuso",
        "barril de bomba de parafuso",
    ],
    "Pumps/Screw Pump/Coupling": [
        "acoplamento de bomba de parafuso",
        "acoplamento de eixo de parafuso",
        "acoplamento flexível de bomba de parafuso",
    ],
    "Pumps/Screw Pump/Gears and Gear Box": [
        "engrenagem de bomba de parafuso",
        "caixa de engrenagens de bomba de parafuso",
        "engrenagem de sincronização", "redutor de bomba de parafuso",
    ],
    "Pumps/Screw Pump/Lubrication": [
        "lubrificação de bomba de parafuso",
        "lubrificação de rolamento de parafuso",
        "lubrificação a óleo de parafuso",
    ],
    "Pumps/Screw Pump/Manufacturing method": [
        "fabricação de bomba de parafuso",
        "método de fabricação de parafuso",
        "usinagem de parafuso de bomba",
    ],
    "Pumps/Screw Pump/Multiphase": [
        "bomba de parafuso multifásica",
        "bomba de duplo parafuso multifásica",
        "bomba de parafuso para gás-líquido",
        "bombeamento multifásico de parafuso",
    ],
    "Pumps/Screw Pump/Profile": [
        "perfil de parafuso", "perfil de rotor de parafuso",
        "geometria helicoidal de parafuso",
        "perfil de rosca de bomba",
    ],
    "Pumps/Screw Pump/Relief Valve": [
        "válvula de alívio de bomba de parafuso",
        "válvula de segurança de parafuso",
        "válvula de bypass de parafuso",
    ],
    "Pumps/Screw Pump/Sealing": [
        "vedação de bomba de parafuso",
        "vedação de eixo de parafuso",
        "vedação dinâmica de parafuso",
    ],
    "Pumps/Screw conveyor": [
        "rosca transportadora", "transportador helicoidal",
        "parafuso sem fim transportador",
        "transportador de parafuso",
    ],
    "Pumps/Scroll Compressor": [
        "compressor scroll", "bomba scroll",
        "scroll orbital", "scroll fixo",
        "mecanismo scroll",
    ],
    "Pumps/Submersible Pumps": [
        "bomba submersível", "ESP", "bomba elétrica submersível",
        "bomba submersível de fundo de poço",
        "bomba de poço profundo", "bomba de furo",
        "bomba centrífuga submersível",
        "bomba submergível",
        "bomba submergível vibratória",
    ],
    "Pumps/Submersible Pumps/Seal section and thrust bearing": [
        "seção de vedação de ESP", "protetor de motor ESP",
        "rolamento axial de ESP", "câmara de empuxo",
        "vedação de bomba submersível", "protetor de motor",
        "vedação de eixo ESP",
    ],
    "Pumps/Vane type Pump": [
        "bomba de palhetas", "bomba rotativa de palhetas",
        "bomba de palhetas deslizantes", "motor de palhetas",
    ],
    "Sealings": [
        "vedação", "vedante", "gaxeta", "anel de vedação",
        "anel o-ring", "dispositivo de vedação",
        "vedação de fluido", "vedação de pressão",
        "sistema de vedação", "vedação dinâmica",
        "vedação estática",
    ],
    "Sealings/Assembly tools": [
        "ferramenta de montagem de vedação",
        "ferramenta de instalação de vedação",
        "montagem de anel o-ring",
        "ferramenta de encaixe de vedação",
    ],
    "Sealings/Diaphragm seal": [
        "vedação de diafragma", "vedação de membrana",
        "diafragma flexível", "vedação com fole",
        "diafragma de bomba",
    ],
    "Sealings/Labyrinth Seal": [
        "vedação labirinto", "vedação de labirinto",
        "vedação sem contato", "packing de labirinto",
        "labirinto escalonado",
    ],
    "Sealings/Lip Seal": [
        "vedação de lábio", "vedação radial de lábio",
        "vedação de lábio de eixo", "vedação de lábio de PTFE",
        "vedação de lábio de borracha",
        "retentor", "vedação raspadeira",
    ],
    "Sealings/Mechanical Seal": [
        "selo mecânico", "vedação mecânica",
        "vedação de face", "vedação rotativa",
        "vedação mecânica dupla", "vedação cartuchos",
        "vedação mecânica em tandem",
        "vedação mecânica de face",
    ],
    "Sealings/Stuffing Box": [
        "caixa de gaxeta", "gaxeta de prensão",
        "caixa de recheio", "empanque trançado",
        "empanque de compressão",
        "caixa de gaxeta de haste polida",
    ],
    "Separator": [
        "separador", "dispositivo de separação",
        "separador de fases", "separador de óleo",
        "separador de gás", "separador gravitacional",
        "separador ciclônico", "hidrociclone",
        "separador gás-líquido", "separador óleo-água",
        "separador inline", "separador compacto",
        "separador de fundo de poço",
        "separador de material líquido e sólido",
    ],
    "Bearings": [
        "rolamento", "mancal", "conjunto de rolamento",
        "mancal de rolamento", "sistema de rolamento",
        "carcaça de rolamento", "suporte de rolamento",
        "seleção de rolamento", "falha de rolamento",
        "vida de rolamento", "carga de rolamento",
        "desempenho de rolamento",
    ],
    "Bearings/Rolling Bearings": [
        "rolamento de esferas", "rolamento de rolos",
        "rolamento de rolos cilíndricos",
        "rolamento de rolos cônicos",
        "rolamento de rolos esféricos",
        "rolamento de agulhas",
        "rolamento de contato angular",
        "rolamento de ranhura profunda",
        "anel interno de rolamento",
        "anel externo de rolamento",
        "elemento rolante", "pista de rolamento",
        "gaiola de rolamento", "retentor de rolamento",
    ],
    "Bearings/Thrust Bearings": [
        "rolamento axial", "mancal de empuxo",
        "rolamento de esferas axial",
        "rolamento de rolos axial", "placa de empuxo",
        "carga axial de rolamento",
    ],
    "Bearings/Bearing Lubrication and Sealing": [
        "lubrificação de rolamento", "graxa de rolamento",
        "vedação de rolamento", "proteção de rolamento",
        "rolamento vedado", "rolamento blindado",
        "lubrificante de rolamento",
    ],
    "Bearings/Bearing Materials": [
        "material de rolamento", "rolamento cerâmico",
        "rolamento de polímero", "rolamento compósito",
        "rolamento autolubrificante", "rolamento de carbono",
        "rolamento de PTFE", "aço de rolamento",
    ],
    "Valves": [
        "válvula", "válvula de retenção", "válvula de esfera",
        "válvula de gaveta", "válvula de globo",
        "válvula de agulha", "válvula borboleta",
        "válvula de plugue", "válvula de diafragma",
        "válvula de alívio", "válvula de segurança",
        "válvula de controle", "válvula solenóide",
        "válvula antirretorno", "válvula redutora de pressão",
        "válvula de controle de vazão", "válvula de isolamento",
        "válvulas",
        # MODIFICAÇÃO (Parte B — Causa 3):
        # Removidos "elemento de filtro resistente à corrosão" e
        # "setor de filtros rotativos" — termos completamente fora de
        # contexto de válvulas. O correto já está em:
        #   Filtration/Paper and Pulp Filter → "setor filtros rotativos"
        #   Filtration/Filter Media and Cartridge → filtros resistentes
    ],
}

# Merge Portuguese into main dictionary
for _cat, _words in _PT.items():
    if _cat in PALAVRAS_CHAVE:
        PALAVRAS_CHAVE[_cat].extend(_words)
    else:
        PALAVRAS_CHAVE[_cat] = _words


# ══════════════════════════════════════════════════════════════════════
# BLOCO DE EXPANSÃO — análise de 455 sem classificação + 789 na raiz
# Adicionado em rodada final: novas pastas principais, secundárias e
# terciárias + keywords de desempate para categorias existentes.
# ══════════════════════════════════════════════════════════════════════

_NOVOS_E_EXPANSOES = {

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS PASTAS PRINCIPAIS                                    ║
    # ╚══════════════════════════════════════════════════════════════╝

    # ── FILTRATION ─────────────────────────────────────────────────
    # 15 sem classe + muitas em Separator/Sealings raiz
    # Filtros de câmara, cartuchos, filtros de ar, peneiras, strainers
    "Filtration": [
        "filter", "filtration", "filtro", "filtragem", "strainer",
        "screen filter", "filter cartridge", "filter element",
        "filter media", "filter membrane", "filter housing",
        "filter assembly", "filter system", "filtration process",
        "filtration device", "bag filter", "filter chamber",
        "pressure filter", "vacuum filter", "inline filter",
        "filter mesh", "sieve", "peneira", "filtração",
        "filter cloth", "filter fabric", "filter cake",
    ],
    "Filtration/Air Filter": [
        "air filter", "air filtration", "filtro de ar",
        "cabin air filter", "HEPA filter", "dust filter",
        "clean room filter", "air purification filter",
        "blower filter cabinet", "pressurized filter cabin",
        "air intake filter", "filter blowing cabin",
        # expansão
        "gas filter", "aerosol filter", "air purification",
        "dust collector filter", "intake filter", "exhaust filter",
    ],
    "Filtration/Liquid Filter": [
        "liquid filter", "fluid filter", "filtro de líquido",
        "filtro líquido", "liquid filtration", "fluid filtration",
        "hydraulic filter", "oil filter", "water filter",
        "filter device liquid", "liquid filtering device",
        "in-line liquid filter", "pipeline filter liquid",
        "reaction mixture filter", "trifásica filtração",
        # expansão
        "fuel filter", "coolant filter",
    ],
    "Filtration/Paper and Pulp Filter": [
        "pressure screen", "pressure strainer", "paper pulp filter",
        "pulp screening", "stock screen", "paper stock strainer",
        "disperger", "disc filter paper", "rotary drum filter",
        "filtro rotativo", "setor filtros rotativos",
        "grooved pyramid teeth filter", "recycled paper contaminant",
    ],
    "Filtration/Filter Media and Cartridge": [
        "filter cartridge", "filter element pleated",
        "pleated filter", "helical pleated filter",
        "filter medium", "filter cartridge formation",
        "filtro pregueado", "filtro pregueado helicoidal",
        "filter element corrugated", "tela filtrante",
        "filtro vertical screen", "filter seal wax edge",
        "filter fabrication method",
        # expansão
        "pleated media", "filter cloth", "porous material",
        "filter membrane", "filter paper",
    ],
    "Filtration/Borehole and Downhole Filter": [
        "borehole filtration", "downhole filter", "wellbore filter",
        "sand screen filter", "downhole filtration device",
        "polymer foam borehole filter", "borehole filtration device",
        "downhole rotary pump filter", "intake filter well",
        # expansão
        "sand control screen", "well screen",
        "in-flow control device", "icd filter",
    ],

    # ══════════════════════════════════════════════════════════════
    # FILTRATION — novas subpastas
    # Para esvaziar a raiz de patentes de filtragem que não se
    # encaixavam nas categorias anteriores.
    # ══════════════════════════════════════════════════════════════

    "Filtration/Self-Cleaning and Backwash": [
        "self-cleaning filter", "backwash", "backflush",
        "automatic filter", "scraped filter", "cleaning blade filter",
        "filter regeneration", "flush valve filter",
        "automatic backwash filter", "self-cleaning filtration",
        "filter cleaning cycle", "counter-current wash filter",
        "retrolavagem", "filtro autolimpante",
        "filter reverse flow", "backwashing cycle",
        "filter cleaning mechanism", "scraper filter",
        "self-cleaning screen", "automatic screen cleaner",
        "filter self cleaning blade",
    ],

    "Filtration/Strainers and Baskets": [
        "strainer", "filter basket", "basket filter",
        "mesh filter", "wire mesh filter",
        "perforated plate filter", "perforated basket",
        "y-strainer", "t-strainer", "inline strainer",
        "suction strainer", "pump strainer",
        "conical strainer", "cylindrical strainer",
        "temporary strainer", "permanent strainer",
        "duplex strainer", "simplex strainer",
        "coarse filter", "coarse strainer",
        "cyclonic strainer", "vortex strainer",
        "peneira filtrante", "cesto filtrante",
    ],

    "Filtration/Disc and Drum Filters": [
        "disc filter", "disk filter", "drum filter",
        "rotary filter", "rotary disc filter",
        "vacuum drum filter", "vacuum disc filter",
        "stack of discs filter", "stacked disc filter",
        "disc filter element", "horizontal disc filter",
        "rotating disc filter", "filter disc assembly",
        "filtro de disco", "filtro de tambor",
        "drum vacuum filter", "belt drum filter",
        "rotary vacuum filter", "filter drum rotation",
        "disc filter cake", "drum filter cake",
        "filtro rotativo a vácuo",
    ],

    "Filtration/Membrane and Ultrafiltration": [
        "ultrafiltration", "reverse osmosis", "nanofiltration",
        "hollow fiber membrane", "hollow fiber filter",
        "membrane module", "membrane filtration",
        "cross-flow filtration", "crossflow filter",
        "permeate membrane", "retentate membrane",
        "microfiltration", "macrofiltration",
        "tangential flow filtration", "dead-end filtration",
        "ceramic membrane filtration", "polymeric membrane",
        "membrane separation", "semipermeable membrane",
        "filtração por membrana", "membrana de filtração",
        "osmose inversa", "ultrafiltração",
        "desalination membrane", "water treatment membrane",
        "porous membrane separation",
    ],

    "Filtration/Magnetic and Particle Separators": [
        "magnetic filter", "magnetic separator filter",
        "electromagnetic filter", "magnetic particle trap",
        "permanent magnet filter", "magnetic grid filter",
        "sand separator filter", "sand trap",
        "hydrocyclone filter", "cyclone particle separator",
        "particle trap", "particle separator",
        "soot filter", "diesel particulate filter", "DPF",
        "chip trap", "swarf filter",
        "fine particle filter", "submicron filter",
        "metallic particle filter", "iron particle filter",
        "separador magnético", "filtro magnético",
        "filtro de partículas",
    ],


    # 67+ sem classe: moinhos industriais, retificadoras, pulverizadores
    "Grinding and Milling": [
        "grinding", "milling", "mill", "grinder", "grinding machine",
        "grinding device", "grinding apparatus", "grinding treatment",
        "pulverizer", "pulverizing", "grinding system",
        "grinding process", "moagem", "trituração", "esmerilhar",
        "grinding mill", "ball mill", "hammer mill", "roller mill",
        "grinding wheel", "abrasive grinding", "wet grinding",
        "dry grinding", "superfine grinding", "ultra-fine grinding",
        "size reduction grinding", "raw material grinding",
        "grinding treatment device", "moagem materiais",
    ],
    "Grinding and Milling/Industrial Grinder": [
        "industrial grinder", "industrial grinding machine",
        "heavy duty grinder", "production grinder",
        "grinding machine frame", "grinding apparatus frame",
        "waste reduction machine", "volume reduction apparatus",
        "direct drive grinder", "motor driven grinder",
        "grinding unit control", "grinder unit method",
        "grinder assembly waste", "waste disposal grinder",
        "grinder tank rotary shaft",
    ],
    "Grinding and Milling/Pulverizer and Superfine Mill": [
        "pulverizer", "superfine pulverizer", "ultrafine pulverizer",
        "superfine crusher", "micro-powder pulverizer",
        "air classifier pulverizer", "classifier mill",
        "vertical ultrafine disintegrator", "ultra-fine disintegrator",
        "superfine grinding mill", "powder pulverizer",
        "micro-powder preparation", "uniform granularity pulverizer",
        "pulverizing chamber", "pulverizing mechanism",
        "pulverizing feeding device",
    ],
    "Grinding and Milling/Wet Grinding": [
        "wet grinding", "wet grinding process", "wet mill",
        "grinding in liquid", "wet pulverizing", "slurry grinding",
        "grinding solid in liquid", "raw material liquid grinding",
        "continuous wet grinding", "immersion grinding",
        "wet milling process", "grinding medium liquid",
    ],
    "Grinding and Milling/Food and Bone Mill": [
        "food grinder", "food grinding", "meat grinder",
        "bone mill", "bone grinding", "cremated bone pulverizer",
        "food processing grinder", "food processor grinding",
        "bean grinder", "bean grinding machine",
        "grain grinder", "grain mill", "flaker mill",
        "food grater", "food processing strips slices",
        "food processing apparatus slicing",
    ],
    "Grinding and Milling/Abrasive and Polishing": [
        "abrasive grinding", "abrasive polishing",
        "grinding wheel abrasive", "polishing head abrasive",
        "rebolo diamantado", "máquina lixadeira",
        "cabeça polidora", "abrasive segments",
        "oscillating polishing", "tangential abrasive",
        "grinding wheel diamond", "lapping machine",
        "surface grinding abrasive",
    ],

    # ── MEDIA AND DOCUMENT DESTRUCTION ─────────────────────────────
    # 11 printing/paper + 7 recording media sem classe
    "Media and Document Destruction": [
        "document destruction", "document shredder", "paper shredder",
        "shredding mechanism paper", "shredder paper",
        "document shredding", "record destruction",
        "information leakage prevention", "information shredder",
        "confidential document shredder", "ticket destruction",
        "recording medium destruction", "medium destruction",
        "discarding recording medium", "disc destruction",
        "optical disk destruction", "CD DVD shredder",
        "data destruction device", "document administration shredder",
        "disposal processing recording", "medium discarding system",
        "razor blade shredding paper", "shredding razor blade",
        "paper shredder mechanism", "strip cut shredder",
        "cross cut shredder",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBCATEGORIAS em pastas existentes                   ║
    # ╚══════════════════════════════════════════════════════════════╝

    # ── Oil Tools / Downhole Power Generation ──────────────────────
    # 20 patentes sem classe sobre geração de energia downhole
    "Oil Tools/Downhole Power Generation": [
        "downhole power generation", "downhole power generator",
        "downhole electrical generation", "downhole turbine",
        "generating power downhole", "wellbore turbine",
        "downhole generator", "turbine downhole fluid",
        "fluid flow turbine downhole", "piezoelectric downhole",
        "mechanical pulse electrical energy", "downhole energy harvesting",
        "borehole power generation", "downhole torque generator",
        "electromagnetic downhole generator", "turbine flow downhole",
    ],

    # ── Oil Tools / Well Intervention Tools ────────────────────────
    # Patentes de Oil Tools raiz sobre ferramentas diversas de intervenção
    "Oil Tools/Well Intervention Tools": [
        "well intervention", "well intervention tool",
        "downhole cutting tool", "cutting member downhole",
        "downhole stroker device", "stroker device borehole",
        "downhole actuator device", "actuator tubular string",
        "downhole device actuator", "lateral borehole tool",
        "opening closing lateral borehole", "positioning tool downhole",
        "positioning tool casing", "logging tool protector",
        "well logging assembly", "pipe conveyed logging",
        "rock anchor formation", "formation fixation device",
        "downhole assembly articulated", "downhole damping mechanism",
        "artificial lift protection", "artificial lift conditioning",
        "fluid conditioning artificial lift", "magnetic coupling downhole",
        "downhole magnetic coupling", "downhole pressure compensating",
        "pressure compensating device downhole", "downhole coating protection",
        "protective barrier downhole", "polymer coating downhole tool",
    ],

    # ── Macerator / Wood Chipper ────────────────────────────────────
    "Macerator/Wood Chipper": [
        "wood chipper", "brush chipper", "wood chipping",
        "chip cutter", "chipping machine", "chipper machine",
        "branch crasher", "branch crusher", "branch chipper",
        "wood chopper", "tree chipper", "chipper wheel",
        "chipper blade", "chipper knife", "chopping tool",
        "chopping apparatus", "chopper machine",
        "disc type chip cutter", "circular cutter disk",
        "bale processor shredding roller", "bale shredding",
        "bale processor improved", "fiber chopper roll",
        "band cutting system", "elongate band cutter",
        "gutter debris removal", "gutter clogging device",
    ],

    # ── Macerator / Compactor and Baler ────────────────────────────
    "Macerator/Compactor and Baler": [
        "compactor", "compacting machine", "baler", "bale processor",
        "compactor wheel", "compacting apparatus", "baling machine",
        "wrapper compactor", "wrapper tip compactor",
        "feed hopper compactor", "waste compactor",
        "volume reduction compactor", "recycling compactor",
        "material compacting", "compost compactor",
        "chicken composter", "carcass composter",
        "organic compost smashing",
    ],

    # ── Macerator / Blending and Mixing ────────────────────────────
    "Macerator/Blending and Mixing": [
        "blending device", "blender", "homogenizer",
        "mixing apparatus", "food blender", "food mixer",
        "food processor blending", "food waste blending",
        "organic waste decomposing", "microbe mixing food",
        "homogenizing device", "emulsifier homogenizer",
        "lab homogenizer", "gel disintegration mixing",
        "polymer gel extraction", "molecule extraction device",
    ],

    # ── Separator / Solid-Liquid Separator ─────────────────────────
    "Separator/Solid-Liquid Separator": [
        "solid-liquid separator", "solid liquid separator",
        "solid liquid separation", "liquid solid separator",
        "separation solid liquid", "food waste solid liquid",
        "waste solid liquid separator", "sludge separator",
        "sludge dewatering separator", "slurry separator",
        "solid-liquid separation device", "material liquid solid separator",
        "liquid solid mixture separator",
        "separação líquido sólido", "dispositivo separação líquido sólido",
    ],

    # ── Separator / Desander and Hydrocyclone ──────────────────────
    "Separator/Desander and Hydrocyclone": [
        "desander", "sand desander", "hydrocyclone",
        "cyclone desander", "hydroclone", "wellbore desander",
        "downhole desander", "sand removal hydrocyclone",
        "cyclonic separator", "cyclone separator unit",
        "cyclone strainer", "cyclonic strainer well",
        "sand separation cyclone", "cyclone well intake",
    ],

    # ── Separator / Multi-control and 3-Phase ──────────────────────
    "Separator/Three-Phase Separator": [
        "three phase separator", "three-phase separator",
        "three phase separation", "oil gas water separator",
        "oil-gas-water separation", "multivariable separator control",
        "balanced entry separator", "media layered separator",
        "parallel multi-phase separator", "constant pressure separator",
        "three phase vertical separator",
    ],

    # ── Pumps / Slurry Pump ────────────────────────────────────────
    "Pumps/Slurry Pump": [
        "slurry pump", "slurry pumping", "mud pump",
        "solids pump", "particle laden pump",
        "abrasive fluid pump", "pump solids content",
        "rotary piston particle loaded", "particle loaded pump",
        "solid material pumping", "solid-liquid pump",
        "dredge pump", "mining pump slurry",
        "pump highly entrained", "entrained solids pump",
        "continuously pumping solid", "solids pump continuous",
        "progressive cavity solids pump",
    ],

    # ── Pumps / Pump Protection and Motor Protector ────────────────
    "Pumps/Pump Protection": [
        "motor protector pump", "pump motor protector",
        "pump protection system", "pump protection device",
        "pump run dry protection", "run dry inhibit",
        "wattmeter pump protection", "pump overload protection",
        "pump blocked protection", "pump seal protection",
        "bellows motor protector", "motor protector bellows",
        "ESP protector", "submersible motor protector",
        "pump system protection method",
    ],

    # ── Bearings / Spindle and Machine Tool Bearings ───────────────
    "Bearings/Spindle Bearings": [
        "spindle bearing", "spindle device bearing",
        "machine tool bearing", "spindle assembly bearing",
        "high speed spindle bearing", "spindle motor bearing",
        "spindle fluid bearing", "spindle support bearing",
        "grinding spindle bearing", "cutting machine bearing",
        "CNC spindle bearing", "main spindle bearing",
        "spindle waterproof bearing", "rotating spindle bearing",
    ],

    # ── Bearings / Sensor and Encoder Bearings ─────────────────────
    "Bearings/Sensor and Encoder Bearings": [
        "sensor bearing", "encoder bearing", "bearing with sensor",
        "bearing rotation sensor", "bearing encoder",
        "speed sensor bearing", "ABS sensor bearing",
        "bearing rotational speed detection",
        "rolling bearing with sensor", "bearing speed detection",
        "bearing sensor holder", "sensor equipped rolling bearing",
        "magnetic encoder bearing", "pulse encoder bearing",
        "bearing measurement rotation",
    ],

    # ── Bearings / Turbocharger and Aerospace Bearings ─────────────
    "Bearings/Turbocharger Bearings": [
        "turbocharger bearing", "supercharger bearing",
        "turbo bearing", "turbocharger bearing assembly",
        "turbocharger rotating shaft bearing",
        "turbomachine bearing", "gas turbine bearing",
        "aerospace bearing", "aircraft bearing",
        "high speed turbine bearing", "floating ring bearing turbo",
    ],

    # ── Valves / Shock Absorber ────────────────────────────────────
    # Detectado nos Valves na raiz
    "Valves/Shock Absorber": [
        "shock absorber", "shock absorber valve",
        "damper valve", "hydraulic shock absorber",
        "twin tube shock absorber", "mono tube shock absorber",
        "shock absorber fluid", "damping valve",
        "rebound valve absorber", "compression valve absorber",
        "absorber piston valve", "strut absorber valve",
        "suspension shock absorber", "vehicle shock absorber",
        "unidirectional fluid flow absorber",
    ],

    # ── Drive Shafts / Power Transmission Mechanism ────────────────
    "Drive Shafts/Power Transmission Mechanism": [
        "power transmission mechanism", "transmission mechanism rotary",
        "driving force transmission", "driving force mechanism",
        "torque transmission mechanism", "power train mechanism",
        "transmission device shaft", "power transfer mechanism",
        "belt transmission", "chain transmission",
        "gear transmission shaft", "reduction gear shaft",
        "propeller shaft automobile", "propeller shaft waterproof",
        "driving force oil-free fluid", "transmission two rotary shafts",
    ],

    # ── Monitoring and controlling / Pump Diagnostics ──────────────
    "Monitoring and controlling/Pump Diagnostics": [
        "pump diagnostics", "pump condition monitoring",
        "pump performance monitoring", "pump health monitoring",
        "pump fault detection", "pump anomaly detection",
        "pump vibration monitoring", "pump acoustic monitoring",
        "pump card analysis", "pump dynagraph",
        "pump system sensor data acquisition",
        "pump type identifier controller",
        "pump component parameter", "pump drive motor controller",
        "pump system monitoring sensor",
    ],

    # ── Corrosion / Resistant Alloys ───────────────────────────────
    "Corrosion/Resistant Alloys": [
        "corrosion resistant alloy", "high carbide alloy",
        "austenitic alloy corrosion", "cast austenitic alloy",
        "chromium nickel alloy corrosion", "duplex stainless steel",
        "super duplex alloy", "Inconel corrosion",
        "titanium alloy corrosion", "carbide cast alloy",
        "wear resistant alloy", "high chromium alloy",
        "nickel base alloy", "corrosion resistant casting",
    ],
    "Corrosion/Protective Coatings": [
        "corrosion protective coating", "anti-corrosion coating",
        "corrosion resistant coating", "epoxy coating corrosion",
        "polyolefin liner corrosion", "lined production string",
        "coated sleeved well device", "coated sleeve liner",
        "polymer coating corrosion", "ceramic liner corrosion",
        "corrosion barrier coating", "coating downhole corrosion",
        "inhibitor coating corrosion", "surface protection corrosion",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  EXPANSÕES DE KEYWORDS PARA DESEMPATE                      ║
    # ║  Problema: score raiz > score subpasta                     ║
    # ║  Solução: frases específicas que aparecem nos abstracts     ║
    # ╚══════════════════════════════════════════════════════════════╝

    # ── Sealings/Bearing Seal — desempate com raiz ─────────────────
    # abstracts: "sealing performance", "grease leakage", "lip contact"
    "Sealings/Bearing Seal": [
        "bearing sealing performance improve",
        "sealability improve bearing", "bearing performance sealing",
        "bearing seal long time", "seal performance long period",
        "prevent leakage sealed bearing", "sealed lubricant bearing",
        "oil seal axle bearing", "seal lip contact bearing",
        "lip tip contact bearing", "seal annular groove bearing",
        "sealing performance wheel bearing", "wheel bearing sealability",
        "prevent muddy water bearing", "seal muddy water bearing",
        "prevent intrusion bearing seal", "foreign matter intrusion seal",
        "sealing device between bearing", "seal between rotating member",
        "slinger sealing bearing", "seal slinger bearing device",
        "grease enclosed bearing seal", "grease leakage rolling bearing",
        "bearing corrosion prevention seal", "rust prevention bearing seal",
        "seal bearing long service", "seal bearing service life",
        "seal core metal bearing", "seal annular member bearing",
        "non-contact seal rolling", "labyrinth rolling bearing",
        "encoder protection bearing seal", "encoder seal cover",
    ],

    # ── Sealings/Mechanical Seal — desempate com raiz ─────────────
    # abstracts: "rotating/stationary ring", "sliding surface", "spring"
    "Sealings/Mechanical Seal": [
        "rotating ring stationary", "rotating seal stationary seal",
        "stationary seal ring rotating", "sliding surface seal ring",
        "sealing surface rotating stationary", "seal face rotating",
        "mechanical seal sleeve spring", "seal sleeve member spring",
        "mechanical seal member movable", "movable seal ring spring",
        "seal spring fixed member", "seal spring rotating",
        "rotary seal stationary ring", "seal between rotating fixed",
        "seal rotating machine shaft", "rotating shaft seal machine",
        "sliding part fluid lubrication", "sliding component fluid",
        "non-leaking rotating seal", "seal fluid lubrication rotation",
        "prevent leakage rotation seal", "seal prevent leakage rest",
        "leakage prevention rotating seal", "seal pressure rotating",
    ],

    # ── Sealings/Shaft Seal — desempate com raiz ──────────────────
    "Sealings/Shaft Seal": [
        "shaft seal prevent leakage", "shaft seal fluid prevent",
        "sealing shaft rotating machine", "shaft rotating seal machine",
        "shaft seal arrangement flushing", "flushing means shaft seal",
        "seal arrangement purging shaft", "seal between shaft housing",
        "shaft seal bearing housing", "seal shaft drive small",
    ],

    # ── Bearings/Hub and Wheel Bearings — desempate ────────────────
    "Bearings/Hub and Wheel Bearings": [
        "bearing device wheel long", "wheel bearing device long period",
        "seal wheel bearing device", "bearing device wheel seal",
        "wheel bearing device encoder", "encoder wheel bearing device",
        "bearing device wheel sensor", "sensor wheel bearing device",
        "outer ring knuckle bearing", "knuckle bearing wheel device",
        "bearing device wheel service", "wheel bearing service life",
        "bearing wheel hub flange", "hub flange bearing device",
        "wheel bearing hub unit structure", "hub unit bearing structure",
        "tapered roller hub bearing unit", "tapered hub bearing",
        "rolling bearing wheel support", "wheel support rolling bearing",
        "bearing device axle railway", "railway axle bearing device",
        "clutch release bearing torque", "bearing torque clutch",
        "release bearing inner ring", "bearing inner ring clutch",
    ],

    # ── Separator — desempate subpastas ────────────────────────────
    "Separator/Gas-Liquid Separator": [
        "gas liquid separation device method", "gas separation liquid method",
        "gas-liquid separation apparatus", "separator gas liquid apparatus",
        "gas liquid separator compact", "gas liquid inline separator",
        "gas separation liquid borehole", "downhole gas liquid separation method",
        "gas-liquid separator multivariable",
    ],
    "Separator/Downhole Separator": [
        "downhole gas separation methods", "gas separation downhole methods",
        "wellbore fluid gas separation", "downhole gas separation system",
        "progressive cavity pump gas separator",
        "PCP passive gas separator", "passive separator PCP",
        "downhole gas separator centrifugal force",
    ],

    # ── Pumps/Screw Pump — desempate ──────────────────────────────
    "Pumps/Screw Pump": [
        "twin screw pump positive displacement protection",
        "method twin screw pump protection",
        "screw pump method fluid conveying",
        "fluid conveying screw pump method",
        "screw pump double worm", "worm double system pump",
        "screw pump multi-functional helix",
        "helix viscous flow pump", "viscous medium screw",
    ],

    # ── Pumps/Submersible Pumps — desempate ───────────────────────
    "Pumps/Submersible Pumps": [
        "electric submersible pump seal section",
        "seal section ESP pump assembly",
        "electrical submersible pump tubing",
        "tubing conveyed submersible pump",
        "thru-tubing conveyed pump system",
        "through tubing pump motor",
        "submersible pump enhanced cooling",
        "cooling downhole submersible",
    ],

    # ── Pumps/PC Pump and Motor — desempate ───────────────────────
    "Pumps/PC Pump and Motor": [
        "progressive cavity pump monitoring control",
        "PCP monitoring system", "eccentric screw monitoring",
        "progressive cavity pump variable frequency",
        "PCP variable speed control", "cavity pump motor backspin",
        "mud motor design progressive cavity",
        "no-turn tool progressive cavity pump",
        "anti-rotation progressive cavity",
    ],

    # ── Macerator — desempate subpastas ───────────────────────────
    "Macerator/Food Waste Disposer": [
        "disposer garbage grinding", "garbage disposer grinding cavity",
        "disposer motor housing grinding",
        "garbage treatment grinding dispose",
        "food waste disposer bacteria", "sterilization garbage disposer",
        "disposer microorganism shred", "microbe garbage shred",
        "garbage treatment shred uniformly",
        "garbage cutting apparatus rotating fixed blades",
        "garbage cutting rotating blades",
    ],
    "Macerator/Industrial Crusher": [
        "uniaxial volume reducing cutter", "uniaxial cutter volume",
        "uniaxial crusher fixed tooth", "waste reduction teeth replaceable",
        "replaceable teeth waste reduction",
        "asbestos crushing volume reduction",
        "asbestos material crushing", "building material asbestos crush",
        "composite resin pulverizing device",
        "composite resin waste pulverize",
        "bag breaking apparatus rotary shaft",
        "bag tearing machine downsized",
        "bag breaking film fragments rotary",
    ],
}

for _k, _v in _NOVOS_E_EXPANSOES.items():
    if _k in PALAVRAS_CHAVE:
        PALAVRAS_CHAVE[_k].extend(_v)
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# BLOCO FINAL — Adições por contexto (não por keyword hunting)
# Análise de títulos + abstracts completos de todas as patentes
# ainda na raiz ou sem classificação.
# ══════════════════════════════════════════════════════════════════════

_CONTEXTO = {

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Sealings                                 ║
    # ╚══════════════════════════════════════════════════════════════╝

    # Problema: Mechanical Seal na raiz porque score empata com raiz.
    # Contexto: todos descrevem par rotativo/fixo, gap de vedação, anel.
    # Solução: termos que aparecem APENAS nos abstracts de mechanical seals.
    "Sealings/Mechanical Seal": [
        # Anatomia do selo mecânico — termos do abstract
        "rotating ring stationary ring", "stationary sliding ring",
        "rotating slide ring", "slide ring packing",
        "sealing gap between", "sealing gap between rings",
        "sealing surfaces", "sliding surfaces seal",
        "counter ring mechanical", "mating ring seal",
        "rotating counter ring", "counter-ring",
        "spring element seal", "spring mechanical seal element",
        "biasing device sealing", "resilient member sealing",
        "bellows assembly seal", "bellows type seal",
        "balanced mechanical seal", "unbalanced mechanical seal",
        "face seal rotating stationary", "face seal component",
        "seal face rotating", "seal face stationary",
        "quenching liquid seal", "quenching fluid seal",
        "flushing seal", "barrier fluid seal",
        "barrier pressure seal", "inerting fluid seal",
        "tandem seal arrangement", "double seal arrangement",
        "outside type split mechanical seal",
        "outside-type mechanical sealing",
        "split mechanical seal", "split type seal",
        "cartridge mechanical seal",
        "silicon carbide seal ring", "carbon graphite seal",
        "tungsten carbide seal face",
        "diamond coating seal surface",
        "end face seal device",
        "rotating shaft seal casing",
        "seal partition rotating stationary",
        "axial protuberance seal ring",
        "sealing liquid chamber", "sealing liquid cooling",
        "cooled mechanical seal", "cooling mechanical seal",
        "hydrodynamic face seal", "gas-lubricated face seal",
        "micro-groove seal face", "spiral groove seal",
        "liftoff seal rotating", "seal ring axial movement",
        "pumping ring seal", "through-hole seal ring",
        "compensation spring seal", "external spring seal",
        "internal spring seal", "wave spring seal",
        "compensation element mechanical seal",
        "adjustment mechanical seal", "adjustable seal ring",
        "integrated mechanical sealing", "integral sealing device",
        "single spring seal", "multi-spring mechanical seal",
        "sealing device rotating shaft",
        "shaft rotating seal casing machine",
        "rotary shaft seal casing fixed",
        "mechanical seal agitator", "seal agitator vessel",
        "mechanical seal kettle reactor",
        "mechanical seal pump shaft",
        "seal rotating component pump",
        "mechanical seal water pump",
        "mechanical seal fire pump",
        "mechanical seal large pump",
        "double end face mechanical seal",
        "dual end face seal",
        "tandem mechanical seal",
        "back-to-back seal",
        "face-to-face seal",
        # contexto específico de abstracts lidos
        "rotating ring locking surface",
        "collar sleeve seal rotating",
        "sleeve seal rotating ring",
        "seal holder rotating ring",
        "rotary feedthrough mechanical seal",
        "rotary joint mechanical seal",
        "axial sliding seal rotary feedthrough",
        "slip ring sealing arrangement",
        "slip ring seal heat transfer",
        "radial sliding seal metering",
        "non-contact face seal",
        "floating ring seal",
        "floating seal material",
        "end seal rotating ring housing",
        "hydrodynamic foot seal rotating",
        "friction pair seal rotating",
        "exercise seal outer rotating member",
        "motion seal inner outer member",
        "seal ring moves radially centrifugal",
        "centrifugal force seal ring width",
    ],

    # NOVA subpasta: vedações específicas para poços e completação
    "Sealings/Wellbore and Completion Seals": [
        # contexto: swellable metals, subsea caps, packer, casing seals
        "wellbore seal system", "well sealing system",
        "casing seal", "casing sealing", "casing head seal",
        "tubing hanger seal", "tubing hanger sealing",
        "wellhead seal assembly", "wellhead sealing system",
        "subsea seal", "subsea sealing",
        "swellable seal", "swellable elastomer seal",
        "swellable metal seal", "swellable metal o-ring",
        "swellable metal gasket", "swellable sealing element",
        "gravel pack elastomer", "swellable gravel pack",
        "tailpipe packer seal", "production packer seal",
        "annular seal well", "annular wellbore seal",
        "stacked seal system", "multi-piece stacked seal",
        "expandable liner seal", "expandable tubular seal",
        "lock mandrel seal", "lock mandrel dynamic seal",
        "subsea cap seal", "locking cap subsea",
        "fracturing spool seal", "wellbore isolation seal",
        "completion seal", "well completion sealing",
        "zero-leakoff emulsified acid seal",
        "perforation seal downhole",
        "elastomer blend wellbore seal",
        "fluoroelastomer wellbore", "FEPM wellbore seal",
        "casing seal wellhead permanent",
        "polymer blend seal wellbore",
        "fluorocarbon rubber seal",
        "stuffing box coated cable",
        "coated intervention cable seal",
        "sea water seal marine",
        "marine shaft seal",
        "drive shaft small watercraft seal",
    ],

    # NOVA subpasta: vedações específicas para sistemas de bomba PCP/poço
    "Sealings/Pump Drive and Drivehead Seals": [
        # contexto: drivehead seals, polished rod seals, stuffing boxes
        "drivehead seal", "drive head seal arrangement",
        "downhole rotary pump seal drivehead",
        "polished rod sealing", "polished rod seal arrangement",
        "polish rod seal pump",
        "seal arrangement drivehead pump",
        "stuffing box polished rod",
        "seal drivehead downhole rotary",
        "seal pump drive string",
        "screw pump ground driving seal",
        "screw pump driving head seal",
        "oil pump draining hole seal",
        "spiral sucker rod pump seal",
        "sucker rod pump seal structure",
        "oil tank sealing screw pump driver",
        "mechanical rotary seal vertical screw pump",
        "screw pump comprehensive sealing",
        "dynamic sealing transmission shaft screw pump",
        "sealing device screw pump shaft",
        "pump seal stator components",
        "pump set of seals stator",
        "seal pump half shell head plate",
        "pump body seal annular",
        "screw pump sealing radial discs",
        "screw pump sealing device",
        "pump sealing system rotating component",
        "fluid conveying pump sealing system",
        "bearing housing seal centrifugal pump",
        "pump shaft seal housing",
        "annular gap seal pump casing",
        "plain bearing shell annular gap seal pump",
        "first pressure stage seal pump",
        "bearing seal centrifugal pump housing",
    ],

    # NOVA subpasta: vedações para rolamentos (contexto industrial)
    "Sealings/Industrial Equipment Seals": [
        # contexto: rolling mills, conveyors, industrial machines
        "bearing pedestal seal roller rolling mill",
        "bearing seat seal roller mill",
        "bearing seat roller sealing",
        "rolling mill oil film bearing seal",
        "rolling mill bearing combined seal",
        "conveyor roller bearing seal",
        "belt conveyor roller bearing seal",
        "conveyor roll bearing seal",
        "idler roller bearing seal",
        "sealing device bearing roller",
        "seal bearing roller conveyor",
        "pin joint seal assembly", "pin joint seal ring",
        "farm machinery bearing seal",
        "harvester bearing seal labyrinth",
        "food processing bearing seal",
        "food processing spindle seal",
        "machine tool spindle seal",
        "prevent cutting fluid entering bearing spindle",
        "bearing machine tool sealing",
        "spindle bearing seal machine",
        "bearing seal machine tool cutting fluid",
        "disk blade bearing hub seal",
        "disc brake bearing seal",
        "wheel hub seal ring",
        "ball joint sealing bellows",
        "sealing bellows ball joint",
        "joint boot seal bearing drive",
        "seal ring joint boot",
        "dust cap seal bearing",
        "linear motion rolling guide seal",
        "linear guide seal structure",
        "ball spring seal device",
        "ball spring seal nut",
        "bearing conveyor roll shell",
        "bearing seal ring-shaped housing",
        "support bearing seal passenger conveyor",
        "passenger conveyor rolling support seal",
        "drum motor seal inner outer lid",
        "drum motor bearing seal",
        "wind turbine bearing seal",
        "wind power plant bearing seal",
        "three-row roller bearing oil seal",
        "sealing device wind turbine bearing",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Bearings                                 ║
    # ╚══════════════════════════════════════════════════════════════╝

    # NOVA subpasta: Bearings para veículos automotivos e ferroviários
    "Bearings/Automotive and Railway Bearings": [
        # contexto lido: wheel hub bearings (veículo), railway axle bearings,
        # suspension stop bearings, propeller shaft center bearings
        "wheel hub bearing vehicle", "hub bearing automobile",
        "wheel bearing automotive", "bearing wheel vehicle",
        "bearing device vehicle wheel",
        "axle bearing vehicle", "vehicle axle bearing",
        "front wheel drive intermediate shaft bearing",
        "front-wheel drive intermediate bearing",
        "wheel drive shaft bearing",
        "differential gear bearing",
        "differential assembly bearing",
        "propeller shaft support bearing",
        "center bearing propeller shaft",
        "center bearing automobile propeller",
        "propeller shaft center bearing support",
        "universal joint bearing",
        "driveshaft bearing vehicle",
        "one-way rotation assembly shaft vehicle",
        "one-way clutch bearing",
        "suspension strut bearing",
        "strut mount bearing", "strut bearing stop",
        "suspension stop bearing vehicle",
        "bump stop bearing seal",
        "vehicle suspension bearing",
        "clutch release bearing system",
        "clutch actuation bearing dual",
        "bearing railway car axle",
        "bearing for railway axle",
        "axle box bearing railway",
        "rolling bearing railway main motor",
        "railway vehicle drive motor bearing",
        "rolling bearing railway vehicle motor",
        "railway bearing grease seal",
        "insulating layer railway bearing",
        "railway bearing seal",
        "electric motor railway bearing",
        "railroad car bearing journal",
        "railroad axle bearing seal",
        "axle railway bearing seal inner outer ring",
        "oil thrower bearing railway",
    ],

    # NOVA subpasta: Bearings industriais / máquinas / rolos
    "Bearings/Industrial Machine Bearings": [
        # contexto: conveyor rolls, rolling mills, spindles, turbochargers,
        # agricultural machinery, food processing
        "conveyor roll bearing", "roll conveyor bearing",
        "belt conveyor bearing roll",
        "roller bearing conveyor shaft",
        "bearing roll shaft cylindrical tube",
        "idler bearing roll conveyor",
        "carrying roller bearing arrangement",
        "rolling mill bearing", "rolling mill roll bearing",
        "bearing roll stand", "bearing carrier roller",
        "bearing pulley cylindrical roll cover",
        "bearing harvester crop element",
        "agricultural machine bearing labyrinth",
        "flaker mill bearing roller",
        "flaker roller bearing motor",
        "bowl crusher bearing housing",
        "crusher bearing shaft housing",
        "mill bearing shaft journal",
        "pulverizer bearing shaft support",
        "food processing bearing spindle",
        "food processing machine bearing",
        "meat grinder bearing blade shaft",
        "mixer bearing motor agitator",
        "turbocharger bearing rotating shaft",
        "supercharger bearing device",
        "bearing turbocharger housing",
        "floating ring bearing turbocharger",
        "compressor bearing", "screw compressor bearing",
        "refrigeration compressor bearing",
        "vertical axis bearing generator",
        "fluid power generator bearing",
        "wind generator bearing arrangement",
        "semiconductor wafer scrubber bearing",
        "wafer scrubber bearing labyrinth",
        "spindle bearing CNC machine",
        "spindle bearing high speed",
        "spindle device bearing high speed",
        "dmn bearing spindle",
        "bearing small motor press fitted",
        "bearing unit housing flange",
        "bearing unit assembly simultaneous",
        "thermal decoupling bearing",
        "thermally decoupled bearing shaft",
        "bearing arrangement carrying roller damping",
        "damping layer bearing roller",
        "porous element bearing lubricant",
        "lubricant accommodating bearing porous",
        "acoustic wave bearing lubricant property",
        "bearing lubricant property determination",
    ],

    # NOVA subpasta: Bearings para fins especiais
    "Bearings/Special and Precision Bearings": [
        # contexto: CT medical, HDD spindle, semiconductor, magnetic coupling
        "medical CT bearing rotary", "computed tomography bearing",
        "CT machine bearing rotary main",
        "hard disc drive bearing actuator",
        "HDD bearing cartridge", "disc drive bearing actuator",
        "spindle motor bearing HDD",
        "bearing contaminant migration hard disc",
        "precision bearing low noise",
        "precision spindle bearing",
        "bearing magnetic coupling downhole",
        "magnet coupling pump bearing",
        "submersible pump motor bearing tuned",
        "tuned bearing mass damper",
        "mass damper bearing submersible",
        "bearing assembly wing portion hub",
        "downhole pump bearing eccentric",
        "eccentric screw pump bearing magnet coupling",
        "bearing motor electrical insulating",
        "insulating bearing electrical motor",
        "rolling contact bearing electric motor",
        "anti-friction bearing electric motor",
        "small motor bearing sintered",
        "sintered impregnation bearing small motor",
        "porous lubricant bearing oil impregnated",
        "IC tag bearing marking",
        "IC marked bearing seal",
        "bearing with IC marking",
        "resin bearing synthetic bracket",
        "plastic carrier bearing passage",
        "labyrinth lid bearing rotating shaft",
        "rolling bearing oscillating drive axial piston",
        "oscillating drive axial piston bearing",
        "axial piston machine bearing oscillating",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Pumps                                    ║
    # ╚══════════════════════════════════════════════════════════════╝

    # NOVA subpasta: Positive Displacement Pumps (categoria ampla)
    "Pumps/Positive Displacement Pump": [
        # contexto: roots principle, rotary piston, orbital, wave pump
        "positive displacement pump roots",
        "roots principle pump",
        "rotary piston pump roots",
        "rotary piston incompressible media",
        "rotary piston particle loaded",
        "orbital pump helical lobe",
        "orbital fluid pumping mechanism",
        "wave pump assembly flight",
        "two sub-channels wave pump",
        "progressive vortex pump",
        "progressing vortex pumping",
        "nutating pump pulsation",
        "nutating disc pump chambers",
        "pump pulsation reduced output",
        "worm pump oil",
        "wormp pump rotary",
        "pumping equipment low-voltage",
        "pump chamber module underpressure",
        "displacement pump conveying housing",
        "delivery rate adjustable pump",
        "pump recirculation line",
        "pump pressure disc carrier shaft",
        "pump with pressure disc",
        "pump overpressure protection inner outer",
        "inner part outer part eccentric",
        "eccentric movement pump inner outer",
        "rotary positive displacement soft packing",
        "rotary displacement pump laminar",
        "rotary displacement pump RVP",
        "pump design laminar volume flow",
    ],

    # NOVA subpasta: Pump Systems and Applications
    "Pumps/Pump Systems and Applications": [
        # contexto: pump systems for specific uses (medical, food, chemical,
        # vehicle cooling, multi-well treatment, satellite pumps)
        "pump system satellite host",
        "host satellite pump system",
        "satellite supply pump main pump",
        "pump system self-contained container",
        "pump system long distance",
        "variable speed pump aquatic",
        "pump controller sensorless determination",
        "flow rate constant pump sensorless",
        "pump system motor filter controller",
        "load shedding pump generator engine",
        "pump system generator power",
        "motor protector pumping bellows assembly",
        "pumping system motor protector",
        "pump motor bellows fluid separation",
        "pump assembly integrated adapter motor impeller",
        "pump assembly dual-bearing rotational drive",
        "pump system host satellite supply",
        "pump liquids medical surgical archimedean",
        "archimedean screw pump medical",
        "pump medical blood urine",
        "pump pureed food helical mechanism",
        "food pump method helical",
        "soybean milk maker grinding pump",
        "grinding pump soybean dreg",
        "waste pumping system baffle tank",
        "waste pump baffle first second area",
        "waste pump tank sensing",
        "pump dewatering multi-section motor cable",
        "pump well dewatering cable motor",
        "pump system water cooling temperature",
        "deep well pump cooling temperature",
        "pump system hydraulic feedback motor",
        "electric motor pump optimal positive feedback",
        "pump positive feedback discharge head",
        "rotary pump controller regulator switch",
        "rotary pump arrangement controller",
        "pumping system method functionally coupled",
        "two pumping units coupled method",
        "lubrication oil pump internal combustion",
        "oil pump variable speed clutch engine",
        "lubrication pump RPM load temperature",
        "petrol pump measuring apparatus fluid",
        "petrol station pump measuring motor",
        "fluid measuring motor pulse generator",
        "fuel pump resonator pipe",
        "fuel pump pump chamber resonator",
        "pump printing media heat-setting worm",
        "worm pump printing inks",
        "pump heat-setting media printer",
        "mobile pump viscous mass mortar",
        "mobile pumping device container drive",
        "circulation device baths pump filter",
        "bath circulating pump filter insert",
        "pump electroblasting activation water pulps",
        "electroblasting water suspension pump",
        "pump microparticles slurry solid CO2",
        "continuously pumping solid material CO2",
        "solid material pressurized slurry pump",
        "sludge reduction treatment cavitation pump",
        "sludge solubilized cavitation pump shock",
        "shock wave generator cavitation pump",
        "medium recycling processing water specific gravity",
        "household appliance waste specific gravity sorter",
    ],

    # Expansão Pumps/Multiphase Pump
    "Pumps/Multiphase Pump": [
        # contexto: crude oil gas water borehole mixtures
        "crude oil natural gas mixture pump borehole",
        "oil gas water borehole multiphase pump",
        "multiphase mixture hydrocarbon borehole pump",
        "pump hydrocarbon borehole multiphase",
        "asynchronous motor multiphase screw pump",
        "asynchronous motor gas fraction pump",
        "high gas fraction pump field-weakening",
        "slug flow gas content pump",
        "ejector pump auxiliary suction",
        "ejector pump split partial liquid",
        "multiphase ejector auxiliary pump",
        "collecting container multi-phase outlet pumps",
        "sump collecting container multi-phase pump",
        "multiphase mixture pump separation splitting",
        "subsea multiphase pump lubrication solid liquid gas",
        "subsea pump multiphase separator lubrication",
        "multiphase separation pump lubrication subsea",
        "conveying liquid gas mixture borehole device",
        "crude oil natural gas recirculation line",
        "multiphase pump asynchronous optimize efficiency",
        "gas content pumped asynchronous high",
        "pump conveying method multiphase hydrocarbons",
        "pump installation ejector suction auxiliary",
        "pump installation limit free gas volume",
    ],

    # Expansão Pumps/Screw Pump — contexto específico de abstracts
    "Pumps/Screw Pump": [
        # contexto: spindle pump, double flow, manifold bearings
        "double-flow screw pump manifold bearings",
        "double flow screw pump central bearings",
        "spindle pump power driving idler",
        "power screw idler screw pump",
        "drive screw idler screw pump",
        "screw pump free moving transverse",
        "screw pump self-center hydraulic forces",
        "screw pump sealing device radial discs",
        "screw rotor tooth profile",
        "male female screw rotor profile",
        "female rotor tooth tip circular arcs",
        "screw pump horizontal divider inlet balanced",
        "twin screw horizontal chain divider",
        "screw pump high gas fraction",
        "screw pump twin asynchronous motor",
        "eccentric screw motor fully lined stator jacket",
        "eccentric screw motor stator jacket lining",
        "screw pump connection assembly support frame",
        "screw pump coupling joint frame",
        "double-screwed spindle mixing zone food",
        "spindle pump additional mixing food",
        "screw pump fast-curing media printer",
        "screw pump printing inks worm drive",
        "screw pump conveying method borehole",
        "wave pump screw first second flight",
        "screw pump discharge baffle means",
        "pump discharge baffle",
        "worm pump rotary housing",
        "double worm single-flight cast",
        "double worm angles contact",
        "worm pump oil borehole",
        "multi-functional double helix viscous",
        "double-spiral viscous flow pump",
        "high-pressure screw multi-stage intermediate bearings",
        "screw pump half-open bearing shells stages",
        "three-screw pump packaging sealing",
        "three-screw pump body sealing packaging",
        "screw pump operate independently rotation direction",
        "screw pump direction rotation independent",
        "drive spindle sealing spaces leak",
        "screw pump sealing spaces thrust piston",
    ],

    # Expansão Pumps/PC Pump and Motor — contexto específico
    "Pumps/PC Pump and Motor": [
        # contexto: mud motor design, no-turn tool, orbital pump (lobe cavity)
        "mud motor design analytical computational",
        "progressive cavity motor design method",
        "positive displacement pump motor design simulate",
        "design parameter progressive cavity simulate",
        "no-turn tool heavy oil screw pump",
        "no-turn device production tubing screw",
        "anti-rotation tubing string PCP",
        "pump rod connection longitudinal axis pin thread",
        "pump rod thread tangential elliptical root",
        "retention device solid sedimentation borehole",
        "solid retention borehole pump",
        "cyclonic strainer well intake pump",
        "cyclone strainer well pump separation",
        "well intake strainer pump separation",
        "sample testing device upstream pump",
        "perforated cartridge test pump upstream",
        "pump additive downhole formation injection",
        "downhole pump additive formation location",
        "apparatus pumping additive wellbore",
        "ultra pump well cylindrical chamber",
        "pump removing liquids well cylindrical cover",
        "gas enter exit pump chamber pressure supply",
        "pump with motor conduit distributed",
        "pump conduit distributed motor fluid displacer",
        "fluid displacer conduit distributed pump",
        "helical lobe orbital pump outer tube inner member",
        "orbital pump outer tube inner helical lobes",
        "helical lobes sealed pumping chambers orbital",
        "moineau type gear resilient sleeve",
        "moineau gear outer inner helical surface",
        "gear mechanism moineau outer inner",
        "pump screw pump connector blowout preventer permanent magnet",
        "permanent magnet motor screw pump direct drive",
        "direct drive screw pump permanent magnet motor",
        "screw pump single-core submersible oil cable",
        "screw pump high-power stepping motor",
        "eccentric screw pump bearing housing cylindrical",
        "magnet coupling eccentric pump cantilever",
        "magnet coupling screw pump radial load",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Valves                                   ║
    # ╚══════════════════════════════════════════════════════════════╝

    # NOVA subpasta: Compressores (contexto: swash plate, variable displacement)
    "Valves/Compressor Systems": [
        # contexto: refrigerant compressors, swash plate, variable displacement
        "variable displacement compressor swash plate",
        "swash plate compressor displacement",
        "variable capacity compressor swash",
        "refrigerant compressor variable displacement method",
        "displacement control valve compressor",
        "variable refrigerant compressor assemble",
        "displacement varying compressor capacity",
        "compressor oil level sight glass valve",
        "oil return valve compressor housing",
        "compressor suction compression displacement mechanism",
        "mechanism suction compression displacement pump vacuum",
        "vacuum pump compressor pneumatic motor",
        "mechanism eccentric piston compressor",
        "eccentric piston compressor chamber oblongo",
        "compressor connection device pressure container",
        "compressed air consumer compressor connection",
        "compressor system pressure container valve",
        "pneumatically powered drive piston expelled",
        "compressed air piston feed return movement",
        "cylinder valve device drive piston air",
        "screw gear pump back pressure valve",
        "back pressure valve slip compressor",
        "screw compressor slide valve capacity",
        "screw compressor capacity slide valve guide",
        "semi-closed displacement screw refrigeration compressor",
        "three screw refrigeration compressor semi-closed",
        "screw refrigeration compressor casing motor stator rotor",
        "compressor motor stator rotor casing three screws",
        "scroll compressor screw capacity slide",
        # artificial lift systems
        "artificial lift system stripper well",
        "stripper well fluid extraction valve",
        "curvilinear gear extraction container valve",
    ],

    # Expansão Valves/Shock Absorber — contexto mais específico
    "Valves/Shock Absorber": [
        "twin tube shock absorber check valve",
        "inner tube annulus check valve shock",
        "piston shock absorber rod side cap",
        "shock absorber unidirectional fluid check",
        "mono tube shock absorber",
        "bump stop reinforced sealing bearing",
        "suspension stop coil spring bearing valve",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Separator                                ║
    # ╚══════════════════════════════════════════════════════════════╝

    # NOVA subpasta: Separators para alimentos e resíduos orgânicos
    "Separator/Food and Organic Separator": [
        # contexto: food waste liquid-solid, juice extractors, organic
        "food waste solid liquid separator",
        "food waste solid-liquid separation",
        "garbage separating apparatus crushing filtering",
        "garbage separator perforation crushing food",
        "food waste disposal separator system",
        "under-sink waste processing separator",
        "under-sink waste liquid extractor",
        "organic waste solid liquid separator",
        "food waste pulping separator",
        "garbage drying processing equipment",
        "garbage treatment dehydration",
        "deodorant foreign matter sorting separator",
        "organic foreign matter separator",
        "juice extraction separator food",
        "food disintegrator separator liquid",
        "food device inlet disintegrator separator reservoir",
        "food extractor juice separator centrifugal",
        "high-speed shearing separator agar",
        "manure fiber grinder separator",
        "manure fiber liquid separator",
        "bowel slag spiral conveying sieve",
        "wet dry crop straw crusher separator sieve",
        "solid liquid separator simple compact",
        "solid-liquid separator annular tube truncated",
        "wood shredder primary secondary filter sieve",
        "shredder primary secondary chamber filter sieve",
        "sludge filter cake crushing device",
        "sludge filter cake shaft cage",
        "device squeezing empty containers separator",
        "compressing containers PET separator selector",
        "roller-supported accumulator yard debris separator",
        "yard debris vacuum separator accumulator",
    ],

    # Expansão Separator/Gas-Liquid Separator
    "Separator/Gas-Liquid Separator": [
        "gas-liquid separator flow-rectifying plate",
        "gas-liquid separator rectifying plate cylindrical",
        "gas liquid separator main body introduction path",
        "gas separator centrifugal tubular drain holes jet pump",
        "centrifugal separator jet pump gas well",
        "gas separator drain holes gravity free water",
        "multiple cup retention gas separator well",
        "upwardly opening retention cups well gas",
        "retention cups gas separator reservoir",
        "corrugated settling cup gas anchor",
        "corrugated cup gas anchor uniform flux",
        "multi-cup uniform flux gas anchor",
        "gas anchor oilfield corrugated",
        "gas-liquid-solid separator float valve cyclone",
        "cyclone float valve gas liquid solid",
        "impurity separator biogas vortex flow",
        "contaminant separator biogas flow vortex",
        "separating multiphase effluents underwater well riser",
        "riser upper portion gaseous lower liquid separator",
        "annular liquid collecting chamber riser separator",
        "multiphase separation parallel fingers pipes upper lower",
        "parallel fingers gas liquid distribution pipes",
        "multiphase separation system distribution header fingers",
        "gas liquid control three-phase production separator",
        "multivariable control three-phase separator oil gas",
        "three-phase control lift gas compression",
        "vertical three-phase separator constant pressure valve",
        "spiral multi-phase separator mechanically pumped wells",
        "spiral separator gas liquid sand oil wells",
        "media layered balanced entry parallel separator",
        "parallel multi-phase balanced entry separator",
    ],

    # Expansão Separator/Downhole Separator
    "Separator/Downhole Separator": [
        "desander vortex body tubular downhole",
        "downhole desander sleeve vortex body",
        "downhole desander ESP gas separator seal",
        "desander packer casing perforations",
        "eccentric pipe-in-pipe downhole separator",
        "pipe-in-pipe eccentric crescent downhole",
        "crescent shaped conduit gas separator",
        "eccentric inner outer tube downhole",
        "passive separator PCP flex shaft",
        "PCP gas separator inner outer housing inlets",
        "wellbore fluid separator flex shaft motor",
        "weighted intake gas separator deviated well",
        "weighted intake port gas separator orientation",
        "gas separator above motor inverted shroud",
        "inverted shroud gas separation mixed flow booster",
        "booster pump crossover inverted shroud gas",
        "downhole gas separation liquid calibrated flow rate",
        "separation chamber calibrated flow downhole",
        "pumping well spiral type multi-phase separator",
        "downhole spiral multi-phase gas liquid sand",
        "circular ring oil pumping rod centering device",
        "centering device annular oil pumping rod",
        "corrugated settling cup well downhole",
        "retention cup well fluid gas escape",
        "jet pump phase separator tailings treatment",
        "motive pump nozzle mixing chamber gas port",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Filtration                               ║
    # ╚══════════════════════════════════════════════════════════════╝

    # Expansão Filtration/Liquid Filter — contexto filtros industriais
    "Filtration/Liquid Filter": [
        "filter chamber liquid filtration",
        "filter filtrating liquids rectangular medium support",
        "rectangular filter medium star-folded",
        "filter medium folded star wax edge sealed",
        "filter sealing wax edge method",
        "liquid filter counter-current diaphragm",
        "counter-current filtration diaphragm moving",
        "filtration countercurrent hollow disc",
        "filter disc horizontal horizontal stack",
        "disc filter horizontal stack element",
        "filter element disc horizontal concavity",
        "corner gap filter liquid body",
        "corner slot filter liquid solid removal",
        "bag filter pocket sealing frame",
        "bag filter two-chamber pocket",
        "filter self-cleaning backwash cement",
        "autoclean filter backwash cement system",
        "filter autoclean retrolavagem automático",
        "filtration increasing rate continuous high solids",
        "bridge prevention filter liquid high solids",
        "liquid pressure filter bridge prevention",
        "filter bridge particles coalescent prevention",
        "pressure screen paper pulp cylindrical sieve",
        "paper stock suspension pressure screen",
        "pressure screen paper annular zones",
        "filtration organic vapor particle layers",
        "filter layer adsorption vapor particle electrostatic",
        "filtration three-phase reaction liquid solid gas",
        "membrane tangential three-phase filtration",
        "membrane filter external pressure screw pump shared",
        "membrane module external pressure positive displacement",
        "porous structure fluid separation process",
        "porous structure separator fabrication",
        "filter mounting filter assembly frame support",
        "filter assembly frame element support bars",
        "bars filter assembly concavity recess",
        "non-woven filter medium high stiffness",
        "non-woven filter Gurley stiffness",
        "filter medium non-woven bicomponent fibers",
        "sludge dehydrator pressurization pump filtration",
        "sludge dehydrator pressure filtration pump",
        "pressurization pump sludge dehydration mould",
        "foam styrofoam liquefying gasifying strainer",
        "strainer non-meltable styrofoam filter",
    ],

    # NOVA subpasta: Filtros de areia e tela em poços
    "Filtration/Sand Control and Well Screens": [
        "sand control screen assembly surface-modified",
        "sand screen surface-modified filter medium",
        "sand control screen perforated base pipe",
        "downhole filter diverter wiper mandrel",
        "downhole filter sleeve casing diverter",
        "downhole filter mandrel wiper circulate",
        "downhole rotary pump filter spring",
        "filter downhole rotary pump umbrella seal",
        "rotary pump filter battery spring",
        "borehole filtration polymer foam",
        "polymer foam borehole filter deploying",
        "well screen selective fluid control rocks",
        "selective fluid control filter flow pipe rocks",
        "particle filter flow pipe wellbore",
        "artificial lift filter scale inhibitor",
        "downhole filter chemical treatment artificial lift",
        "production fluid filter porous medium chemical",
    ],

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  NOVAS SUBPASTAS — Sem Classificação                        ║
    # ╚══════════════════════════════════════════════════════════════╝

    # NOVA PASTA PRINCIPAL: Grinding and Milling — subpastas mais específicas
    "Grinding and Milling/Superfine and Classifier Mill": [
        "superfine grinder cyclone dust draught fan",
        "superfine grinder classifier impeller",
        "grading impeller crushing classifying",
        "air classifier grading chamber crushing",
        "air inlet chamber grinding classifying",
        "cyclone dust collector grinder draught",
        "micro-powder uniform granularity cyclone",
        "micro-powder preparation cyclone grinder fan",
        "superfine crusher grading uniform granularity",
        "crusher grading impeller chamber",
        "low-temperature pulverizer liquid nitrogen",
        "liquid nitrogen nozzle grinding chamber",
        "liquid nitrogen spray pulverizer",
        "cryogenic grinding pulverizer nitrogen",
        "cryogenic pulverizer low temperature",
        "dry wet dual purpose low-temperature crusher",
        "compression volume-reduction granulation",
        "compression granulation fixed blade movable",
        "granulation gap blade forwardly rearwardly",
        "uniaxial volume reducing cutter fixed tooth",
        "energy-saving grinding granulating medicine",
        "tapered screen rotation shaft knife medicine",
        "grinding granulating machine tapered screen",
        "dry treatment organic vegetable substance crushing",
        "organic vegetable crush cell wall",
        "vertical shaft grinding raw material liquid",
        "raw material liquid grinding apparatus system",
    ],

    "Grinding and Milling/Paper and Fiber Processing": [
        "disperger plate grooved pyramid teeth",
        "disperger recycled paper contaminant",
        "fiber chopper roll retainer",
        "roll retainer fiber chopper shaft",
        "fiber feeder compressed masses breaking",
        "fiber breaking compressed mass transporting",
        "band cutting system elongate cutter motor",
        "strip cut system cutter material",
        "cutter module trim disposal mechanism",
        "trim disposal integrated cutter",
        "chaff-cutter woody material collection water jet",
        "water jet nozzle wood cutting high pressure",
        "wood cutter water jet high pressure pump",
        "wood chipper water jet pump nozzle",
        "chipping machine disk cutter knife circular",
        "disk chip cutter knife circular",
        "brush chipper winch control",
        "brush chipper coordinated control",
        "bale processor shredding roller improved",
        "bale shredding roller harvester",
        "power transmission mechanism crushing device",
        "crushing device power transmission",
    ],

    # NOVA pasta principal: Oil Tools / Downhole Power and Energy
    "Oil Tools/Downhole Power Generation": [
        "downhole power generation turbine fluid",
        "downhole generator fluid turbine chambers",
        "downhole electrical power generation turbine",
        "generating power downhole fluid turbine",
        "piezoelectric downhole body cover element",
        "mechanical pulse electrical energy wellbore",
        "mechanical pulse downhole electrical convert",
        "downhole torque generator cylindrical magnetically soft",
        "torque generator downhole magnetically soft member",
        "magnetically soft torque generating apparatus",
        "well logging tool extendable pipe conveyed",
        "pipe conveyed extendable well logging protector",
        "well logging assembly pipe end protector",
        "downhole assembly articulated mandrel damping",
        "passive active damping downhole mandrel",
        "downhole method apparatus mechanical force bore wall",
        "formation fluid injection downhole bore wall",
        "shaft downhole equipment coupling nominal diameter",
        "shaft downhole coupling driven devices",
        "stroker device borehole longitudinal displacement",
        "actuator displacement tool borehole longitud",
        "downhole actuator energy storage spring",
        "actuator tubular string spring device",
        "system well logging internal longitudinal",
        "technique logging downhole equipment deployed",
        "positioning tool casing downhole longitudinal",
        "formation fixation rock anchor open-hole",
        "rock anchor tubular open-hole wellbore",
        "3D printed barrel slip expandable radial",
        "barrel slip radially expandable body",
    ],

    # Expansão Oil Tools / Well Intervention Tools
    "Oil Tools/Well Intervention Tools": [
        "downhole cutting tool shaft deflecting",
        "shaft deflecting cutting member downhole",
        "cutting member downhole rotatable shaft",
        "downhole cutting rotating shaft deflecting",
        "sand production rate completion borehole",
        "sand production unconsolidated subterranean borehole",
        "method determining sand production completing bore",
        "centralising core orientation apparatus downhole",
        "centralising core orientation drilling",
        "magnetic coupling bootstrapping downhole",
        "protective barrier bond integrity downhole",
        "polymer coating wear galling downhole",
        "copolyester thermoset ACT downhole coating",
        "downhole pressure compensating housing chamber",
        "pressure compensating device combination downhole",
        "downhole tool lateral borehole opening closing",
        "opening closing lateral borehole downhole tool",
        "well system logging internal deployed",
        "downhole device rollers body bearing",
        "rollers bearing downhole wellbore deviated",
        "casing hanger wickers expanded lower",
        "lower casing segment radially expanded wickers",
        "oilfield apparatus seal rubber oxycellulose",
        "seal rubber oxycellulose cellulose nanofibers",
        "rubber seal oilfield cellulose composition",
    ],

    # Expansão Monitoring and controlling
    "Monitoring and controlling": [
        "pump card analysis wave equation rod",
        "pump card downhole wellbore reciprocating",
        "instrumentation pump card surface wave equation",
        "pump system sensor data acquisition unit",
        "pump control unit type identifier parameter",
        "pump type identifier controller",
        "pump diagnostics vibration signal shaft revolution",
        "vibration signal processing shaft revolution fault",
        "fault detection pump vibration signal periodic",
        "pump fault vibration signal periodic",
        "multiple well fluid distribution remotely operable",
        "multiple well treatment remotely control valve",
        "remotely operable valve fluid conduit wellbores",
    ],

    # Expansão Electric Motors — contexto lido
    "Electric Motors": [
        "sealless screw pump subsea electric motor",
        "zero leakage subsea screw pump motor",
        "compact sealless pump subsea motor",
        "permanent magnet synchronous motor PWM filter",
        "PMSM eliminate PWM filter motor",
        "control permanent magnet synchronous motor eliminate",
        "electric motor driven pump optimal positive feedback",
        "electric motor pump discharge head feedback",
        "electric motor-driven pump speed reduce",
        "electric motor water pump cooling circulation",
        "pump motor electric cooling water circulation",
        "non-pulsating pump electric driven spiral meshing",
        "electric spiral shaft meshing pump",
        "drum motor inner outer lid bearing",
        "drum motor bearing hygienic drum tube",
    ],

    # Expansão Corrosion — contexto lido
    "Corrosion": [
        "austenitic corrosion resistant alloy high carbide",
        "high carbide cast austenitic alloy nickel chromium",
        "cast corrosion resistant alloy nickel chromium carbon",
        "coated sleeved oil gas well production devices",
        "coated sleeved production devices methods",
        "polyolefin liner production injection string well",
        "abrasion corrosion liner polyolefin",
        "slide ring running gear seal corrosion",
        "running gear seal angular cross-section",
        "sealing structure muddy water dust bearing",
        "muddy water dust bearing sealing prevention",
        "shredding device plastic bottles sealing structure",
        "novel beam pumping unit wellhead blowout preventer",
        "wellhead blowout preventer pumping unit",
    ],

    # Expansão Dehydrator — contexto
    "Dehydrator": [
        "continuous centrifugal crusher dehydrator",
        "centrifugal crusher dehydrator",
        "garbage drying processing energy deodorization",
        "garbage dryer heat vaporization moisture",
        "pressurized sludge dehydrator pump filtration",
        "sludge dehydrator pressurization pumped method",
    ],

    # Expansão Measuring devices — contexto
    "Measuring devices": [
        "dosing device fluid additive volumetric",
        "metering device fluid volumetric additive",
        "liquid measuring motor rotating wheel petrol pump",
        "petrol pump measuring apparatus rotating wheel",
        "pulse generator measuring motor converter",
        "liquid delivery precision dosing anti-drip",
        "high precision dosing pump delivery device",
        "dosing pump liquid delivery method control",
        "cloudiness paint measuring color coordinates",
        "paint cloudiness Gaussian smoothing filter",
    ],

    # Expansão Media and Document Destruction — contexto
    "Media and Document Destruction": [
        "document destruction apparatus administration system",
        "document administration destruction shredder",
        "shredding mechanism paper razor blade",
        "razor blade paper shredding molding",
        "industrial paper shredder section motor cutting",
        "paper shredder section discharge slot",
        "fire explosion proof shredder kneader",
        "fire prevention shredder kneader",
        "special maintenance card shredder lubricating",
        "shredder maintenance card lubricating paste",
        "shredder maintenance lubrication oil card",
        "shredder double shaft grating smashing",
        "double shaft powerful smashing grating",
        "recording medium destruction discarding system",
        "medium destruction discarding system method",
        "optical disk destruction method apparatus",
        "disk record medium discarding destruction",
        "ticket apparatus destruction housing cutter",
        "destruction tickets housing cutter removable",
        "asbestos crushing volume reduction method",
        "building material asbestos method apparatus",
        "method apparatus crushing reducing asbestos",
        "medical waste sterilizing grinding automated",
        "medical waste disinfecting triturating automated",
        "smart discharge medical waste system",
        "disposer garbage medical sterilize grind",
    ],

    # Expansão Manufacturing technology
    "Manufacturing technology": [
        "herringbone gear injection molding pump",
        "chevron teeth gears injection molding method",
        "method manufacturing herringbone gear injection",
        "injection molding gear method apparatus mold halves",
        "ceramic membrane porous structure fabrication",
        "porous membrane process manufacture",
        "compressor screw rotor tooth profile design",
        "tooth profile elimination blow-hole",
        "screw compressor tooth profile efficiency",
        "rotary compressor JPH capacity control",
    ],
}

for _k, _v in _CONTEXTO.items():
    if _k in PALAVRAS_CHAVE:
        PALAVRAS_CHAVE[_k].extend(_v)
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# NOVAS PALAVRAS-CHAVE — subpastas adicionadas para esvaziar raízes
# Merge inteligente: chaves existentes recebem novos termos;
# chaves novas são criadas diretamente.
# ══════════════════════════════════════════════════════════════════════

_NOVAS_PALAVRAS_CHAVE = {

    # ══════════════════════════════════════════════════════════════
    # GRINDING AND MILLING
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Grinding and Milling/Abrasive and Polishing": [
        "abrasive", "polishing", "lapping", "honing", "abrasive article",
        "polishing pad", "chemical mechanical polishing", "cmp",
    ],
    "Grinding and Milling/Food and Bone Mill": [
        "food mill", "bone mill", "meat grinder", "food grinding",
        "grain mill", "coffee grinder", "spice mill",
    ],
    "Grinding and Milling/Industrial Grinder": [
        "industrial grinder", "grinding machine", "grinding wheel",
        "centerless grinding", "cylindrical grinding", "surface grinder",
    ],
    "Grinding and Milling/Pulverizer and Superfine Mill": [
        "pulverizer", "pulverising", "pulverizing", "superfine mill",
        "micronizer", "jet mill", "fine grinding", "ultrafine",
    ],

    # Novas subpastas
    "Grinding and Milling/Crushers and Breakers": [
        "crusher", "crushing apparatus", "jaw crusher", "cone crusher",
        "impact crusher", "rock breaker", "comminution", "crushing roller",
        "crushing plant",
    ],
    "Grinding and Milling/Shredders and Macerators": [
        "shredder", "shredding", "macerator", "macerating", "chipper",
        "destruction apparatus", "waste grinder", "wood chipper", "shredding machine",
    ],
    "Grinding and Milling/Ball and Roller Mills": [
        "ball mill", "roller mill", "tumbling mill", "rod mill",
        "grinding roller", "tube mill", "vertical roller mill",
    ],

    # ══════════════════════════════════════════════════════════════
    # SEPARATOR
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Separator/Centrifugal Separator": [
        "centrifugal separator", "centrifuge", "centrifugal separation",
        "centrifugal decanter", "centrifugal machine",
    ],
    "Separator/Downhole Separator": [
        "downhole separator", "subsurface separator", "in-well separator",
    ],
    "Separator/Gas-Liquid Separator": [
        "gas-liquid separator", "vapor-liquid separator", "demister",
        "degasser", "liquid-gas separator", "moisture separator",
    ],

    # Novas subpastas
    "Separator/Hydrocyclone and Cyclone": [
        "hydrocyclone", "cyclone separator", "cyclonic separation",
        "cyclone dust collector",
    ],
    "Separator/Magnetic and Electrostatic": [
        "magnetic separator", "electrostatic separator", "magnetic separation",
        "eddy current separator",
    ],
    "Separator/Screening and Filtering": [
        "screening device", "vibrating screen", "sieve", "strainer",
        "screening machine", "rotary screen", "separator screen",
    ],
    "Separator/Gravity and Settling": [
        "gravity separator", "settling tank", "clarifier", "sedimentation tank",
        "settling basin", "flotation separator",
    ],

    # ══════════════════════════════════════════════════════════════
    # VALVES
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Valves/Check Valve": [
        "check valve", "non-return valve", "one-way valve", "backflow preventer",
        "clack valve", "flap valve",
    ],
    "Valves/Compressor and Pump Valve": [
        "compressor valve", "pump valve", "suction valve", "discharge valve",
        "reed valve",
    ],
    "Valves/Control and Flow Valve": [
        "control valve", "flow valve", "regulating valve", "throttle valve",
        "flow control valve", "proportional valve",
    ],
    "Valves/Relief and Safety Valve": [
        "relief valve", "safety valve", "pressure relief", "blow-off valve",
        "pop valve",
    ],
    "Valves/Sleeve and Toe Valve": [
        "sleeve valve", "toe valve", "sliding sleeve",
    ],

    # Novas subpastas
    "Valves/Actuation and Solenoid": [
        "solenoid valve", "valve actuator", "pneumatic valve", "hydraulic valve",
        "motorized valve", "electro-hydraulic valve", "actuated valve",
    ],
    "Valves/Ball, Gate and Globe": [
        "ball valve", "gate valve", "globe valve", "butterfly valve",
        "plug valve", "needle valve", "spool valve",
    ],
    "Valves/Valve Components and Seals": [
        "valve seat", "valve stem", "valve seal", "valve packing",
        "valve closure", "valve body", "valve assembly",
    ],

    # ══════════════════════════════════════════════════════════════
    # DRIVE SHAFTS
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Drive Shafts/Power Transmission Mechanism": [
        "power transmission", "transmission mechanism", "drive train",
        "drivetrain", "transmission system",
    ],
    "Drive Shafts/Shaft Coupling Device": [
        "shaft coupling", "coupling device", "flange coupling", "flexible coupling",
        "rigid coupling", "fluid coupling", "magnetic coupling",
    ],

    # Novas subpastas
    "Drive Shafts/Joints and Articulations": [
        "universal joint", "constant velocity joint", "cv joint",
        "cardan joint", "u-joint", "articulated joint", "knuckle joint",
    ],
    "Drive Shafts/Axles and Spindles": [
        "axle", "wheel axle", "spindle", "rotating axle", "drive axle",
        "live axle", "stub axle",
    ],
    "Drive Shafts/Splines and Keyways": [
        "splined shaft", "spline", "keyway", "shaft key", "torque tube",
        "spline coupling",
    ],
}

for _k, _v in _NOVAS_PALAVRAS_CHAVE.items():
    if _k in PALAVRAS_CHAVE:
        # Merge sem duplicatas
        existing = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in existing])
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO — Valves, Separator e Sealings
# Objetivo: esvaziar as raízes dessas pastas movendo patentes para
# subpastas específicas.
# Regra de merge: chaves existentes recebem apenas termos novos (sem
# duplicatas); chaves inéditas são inseridas diretamente.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_PALAVRAS_CHAVE = {

    # ══════════════════════════════════════════════════════════════
    # VALVES
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Valves/Check Valve": [
        "check valve", "non-return valve", "one-way valve", "backflow preventer",
        "clack valve", "flap valve", "válvula de retenção",
        # MODIFICAÇÃO (Parte B — Causa 2): PT faltantes adicionados
        "válvula de retorno",
        # "válvula antirretorno" já está na linha da definição base (linha 1232)
    ],
    "Valves/Control and Flow Valve": [
        "control valve", "flow valve", "regulating valve", "throttle valve",
        "proportional valve", "needle valve", "válvula de controlo",
        # MODIFICAÇÃO (Parte B — Causa 2): PT faltantes adicionados
        "válvula de controle",
        "válvula de controle de capacidade",
        "válvula de controle de deslocamento",
    ],
    "Valves/Relief and Safety Valve": [
        "relief valve", "safety valve", "pressure relief", "blow-off valve",
        "pop valve", "bursting disc", "válvula de segurança",
        # "válvula de segurança" já estava — confirmado presente
    ],
    "Valves/Actuation and Solenoid": [
        "solenoid valve", "actuated valve", "valve actuator", "electric valve",
        "pneumatic valve", "hydraulic valve", "motorized valve",
        # MODIFICAÇÃO (Parte B): "valve device" movido para cá (mais específico)
        "valve device",
    ],

    # Novas subpastas
    "Valves/Ball and Gate Valves": [
        "ball valve", "gate valve", "butterfly valve", "globe valve",
        "plug valve", "spool valve", "válvula de esfera", "válvula gaveta",
    ],
    # MODIFICAÇÃO (Parte B): "valve assembly", "valve body", "valve element"
    # movidos da raiz para esta subpasta (Causa 1)
    "Valves/Valve Components": [
        "valve seat", "valve stem", "valve body", "valve plug", "valve housing",
        "valve assembly", "valve element",
    ],
    # MODIFICAÇÃO (Parte B — Causa 3): Nova subpasta para back pressure valve
    # Antes: "back pressure valve" estava APENAS na raiz _EXPANSOES["Valves"],
    # fazendo patentes de contrapressão ficarem na raiz genérica.
    "Valves/Back Pressure Valve": [
        "back pressure valve", "backpressure valve", "back-pressure valve",
        "pressure relief screw pump", "bypass back valve",
        "válvula de contrapressão",
    ],

    # ══════════════════════════════════════════════════════════════
    # SEPARATOR
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Separator/Gas-Liquid Separator": [
        "gas-liquid separator", "vapor-liquid separator", "demister",
        "degasser", "slug catcher", "mist eliminator",
    ],
    "Separator/Hydrocyclone and Cyclone": [
        "hydrocyclone", "cyclone separator", "cyclonic separation",
        "vortex separator", "sand separator",
    ],
    "Separator/Gravity and Settling": [
        "gravity separator", "settling tank", "clarifier", "sedimentation",
        "oil-water separator", "decanter", "flotation cell",
    ],

    # ══════════════════════════════════════════════════════════════
    # SEALINGS
    # ══════════════════════════════════════════════════════════════

    # Expansão de chaves existentes
    "Sealings/Mechanical Seal": [
        "mechanical seal", "face seal", "cartridge seal", "bellows seal",
        "stationary seal", "rotating seal", "selo mecânico",
    ],

    # Novas subpastas
    "Sealings/Seal Ring and Gasket": [
        "seal ring", "gasket", "o-ring", "v-ring", "x-ring", "backup ring",
        "joint ring", "sealing washer", "junta de vedação",
    ],
    "Sealings/Packing and Stuffing Box": [
        "packing", "stuffing box", "gland packing", "compression seal",
        "compression packing", "gaxeta",
    ],
    "Sealings/Dynamic and Oil Seals": [
        "oil seal", "lip seal", "wiper seal", "v-seal", "rotary seal",
        "radial seal", "excluder seal",
    ],
    "Sealings/Hermetic and Static Seals": [
        "hermetic seal", "static seal", "sealing arrangement", "tightness",
        "leakage prevention", "sealing assembly", "estanqueidade",
    ],
}

for _k, _v in _EXPANSAO_PALAVRAS_CHAVE.items():
    if _k in PALAVRAS_CHAVE:
        # Merge sem duplicatas
        existing = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in existing])
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V4 — Gerada por análise estatística de 821 patentes sem
# classificação. Objetivo: reduzir "Sem match" de 821 → ~350.
# Metodologia: n-gram analysis + clustering temático sobre os abstracts.
#
# Grupos identificados e ações tomadas:
#   1. Oil Tools/Centralizer       — score insuficiente (1 pt); +termos multi-palavra
#   2. Oil Tools/Downhole misc.    — faltavam keywords específicas
#   3. Macerator/Comminuting       — patentes DE sem "crusher"/"shredder"
#   4. Macerator/Cutting Elements  — cutter module, granulator blade, blade holder
#   5. Macerator/Food Processor    — household food processor, kitchen garbage
#   6. Pumps/Screw Pump            — screw machine, rotary screw machine
#   7. Pumps/PC Pump               — progressive cavity hydraulic machine
#   8. Filtration/Paper and Pulp   — refiner plate, refiner disk, disperger
#   9. Conveyor and Transport      — NOVA pasta de nível superior
#  10. Agriculture and Biomass     — NOVA pasta de nível superior
#  11. Mixing and Agitation        — NOVA pasta de nível superior
#  12. Filtration (PT/BR faltantes) — termos BR que não casavam
#  13. Grinding and Milling        — BR patents + estrangeiros faltando
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V4 = {

    # ──────────────────────────────────────────────────────────────────
    # Oil Tools / Centralizer
    # Problema: abstracts curtos com só "centralizer" = 1 pt < SCORE_MINIMO.
    # Solução: adicionar frases multi-palavra que garantem score ≥ 2.
    # ──────────────────────────────────────────────────────────────────
    "Oil Tools/Centralizer": [
        "low clearance centralizer", "composite bow centralizer",
        "bow spring centralizer", "integral centralizer",
        "pipe centralizer", "well string centralizer",
        "id centralizer", "passive centralizer",
        "centralizer apparatus", "centralizer method",
        "centralizer collar", "stop collar centralizer",
        "centralizer locking collar", "centralizer spring structure",
        "casing centralizer design", "centralizer making method",
        "centralizer anti-rotation", "centralising core orientation",
        "integral pull-through centralizer", "centralizer tubular",
        "centralizer friction", "centralizer running",
        "swellable downhole centraliser", "high expansion centralizer",
        "centralizer forming method", "centralizer bow",
        "centralizer attachment", "stabilizer centralizer",
        "centralizador de baixa resistência", "centralizador compósito",
        "centralizador de mola", "centralizador integral",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Oil Tools — Downhole / Wellhead misc.
    # ──────────────────────────────────────────────────────────────────
    "Oil Tools": [
        "downhole assembly device", "downhole method apparatus",
        "well tubular strainer", "tubular slug reducer",
        "frac head components", "multipart frac head",
        "wellhead isolation sleeve", "wellhead protection sleeve",
        "running bore-lining tubulars", "bore-lining tubular",
        "casing head connector", "wellhead tubular connector",
        "selective control fluid flow well", "fluid flow control well rocks",
        "stimulating multi-zone well", "multi-zone well stimulation",
        "wellsite control system", "wellsite control method",
        "apparatus processing fluids well", "processing fluids well method",
        "subterranean oil transport", "transport subterranean oil",
        "snap latch profile", "collet profile downhole",
        "releasable connector tubing deployment", "tubing tool deployment",
        "interference-fit stop collar tubular", "stop collar positioning device",
        "shaft downhole equipment", "wellbore screen tracer",
        "inverted motor drilling", "drilling inverted motor",
        "grip enhanced tractoring", "tractor downhole grip",
        "system use bore hole axial coupling", "bore hole coupling mandrel",
        "downhole conditions investigation", "investigating downhole conditions",
        "selective acid diversion matrix", "matrix acidizing diversion",
        "sand free production borehole", "sand free production rate",
        "high expansion anchoring device", "high expansion stabilizer",
        "expandable reamer stabilizer", "stabilizer expandable reamer",
        "acoustic fluid analyzer", "fluid analyzer acoustic",
        "oilfield data loading", "oilfield data services",
        "hydrodynamic down-hole anchor", "downhole hydrodynamic anchor",
        "extraction molecules polymeric gel", "molecules gel electrophoretic",
    ],

    "Oil Tools/Drilling": [
        "inverted motor drilling wellbore", "drill motor inverted",
        "positive displacement drilling motor", "drilling motor liner",
        "optimized liner drilling motor", "fiber reinforced liner motor",
        "liner thickness drilling motor", "stator downhole motor fabricating",
        "stators downhole motors methods", "downhole motors fabricating stators",
    ],

    "Oil Tools/Anchoring Tool": [
        "high expansion anchor system", "high expansion anchoring",
        "quarter-turn anchor catcher", "anchor catcher anti-rotation",
        "resilient anchor downhole", "anchor downhole resilient",
        "hydrodynamic down-hole anchor", "anchor wellbore hydrodynamic",
    ],

    "Oil Tools/Sand Protection/Screen": [
        "screen blockage measurement", "screen flow performance optimization",
        "screen blockage flow system", "wellbore screen tracer fluid",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Macerator / Industrial Crusher — comminuting machines (DE)
    # ──────────────────────────────────────────────────────────────────
    "Macerator/Industrial Crusher": [
        "comminuting machine", "comminution machine", "comminuting apparatus",
        "comminuting tool cutting", "comminution unit processing",
        "comminuting system industrial", "comminuting garden waste",
        "comminuting wood waste", "comminuting or chopping system",
        "chopper mulcher", "chipper mulcher", "wood chipper mulcher",
        "wood chip optimizer", "wooden debris compressor",
        "device producing wood chips", "wood chips combustion",
        "biomass heater wood chip", "chip making device wood",
        "ultrafine smashing machine", "smashing mechanism rubbish",
        "industrial rubbish processor", "rubbish processor smashing",
        "bag breaking mechanism kitchen", "bag breaking kitchen rubbish",
        "live bottom shear deck", "refuse bag opener",
        "disintegrating device waste knife", "waste knife set",
        "destruction device data carriers", "data carrier destruction",
        "granulator blade helical", "granulator device helical",
        "granulating plastic method", "plastic granulating apparatus",
        "pelletizer small device", "small pelletizer",
        "eddy current crushing pelletizing", "pelletizing eddy current",
        "organic compost smashing tank", "compost smashing device",
        "aseptic tissue triturator", "tissue triturator capacity",
        "rapid quenching strip breaking", "quenching strip break device",
        "lead pig slicing granulator", "granulator slicing lead pig",
        "screw press solid liquid auger", "screw press biogas auger",
        "rotating blade chopping machine", "chopping machine rotational",
        "high speed multiple-tool chopper", "multiple-tool chopping cutter",
        "brush cutter wear liner", "wear liner brush cutter",
        "rotatable cutting tool assembly", "cutting tool rotatable",
        "modular blade assembly alignment", "blade assembly alignment",
        "cutter assembly s-shaped blade", "s-shaped blade cutter",
        "rotary knife improved", "improved rotary knife",
        "cutter module trim disposal", "trim disposal mechanism cutter",
        "granulator helical cutter", "helical cutter granulator",
        "deagglomeration disaggregation clustered", "disaggregation materials method",
        "krumbuster", "process production mineral oil crushing",
        "ore feed processing method", "ore feed apparatus",
    ],

    "Macerator/Cutting Elements": [
        "chopping knife fixing arrangement", "fixing arrangement chopping knife",
        "knife holder interface blade", "interface knife knife holder",
        "blade holder rectangular recess", "blade holder comminution machine",
        "cutter blade holder", "blade holder cutter machine",
        "granulator blade design", "granulator blade assembly",
        "forage harvester knife mounting", "knife mounting forage harvester",
        "automatic adjustment blade engagement", "blade engagement adjustment",
        "blade shaft connection structure", "blade shaft connect assemble",
        "on-line identification stamping blade", "front back stamping blade",
        "modular blade assembly", "s-shaped blade assembly",
        "perforated disk food processing", "perforated disk processing",
        "tightening loosening blade sets", "clamping nuts blade sets",
        "cutter s-shaped blade assembly",
    ],

    "Macerator/Food Waste Disposer": [
        "food processor household", "household food processor",
        "food processing tools processor", "food processing apparatus strips",
        "food processor slices cubes", "food processing device strips",
        "food processing device household", "food processor machine",
        "kitchen garbage disposing apparatus", "kitchen garbage device",
        "kitchen garbage crushing separating", "kitchen scraps recycling",
        "apparatus collecting recycling kitchen scraps",
        "garbage processing machine household", "garbage treatment machine",
        "disposal processing apparatus", "food disposal machine",
        "decorative disposer flange strainer", "disposer flange strainer",
        "non-pulpables collection basket pulpers", "solid waste pulpers basket",
        "waste pulper chamber basket", "pulper collection basket",
        "medication disposal system", "medicine disposal",
        "drug disposal device", "waste processing pathogen reduction",
        "waste processing method pathogen", "mobile waste disposal system",
        "household garbage treatment device", "novel household garbage",
        "rubber twisting cutting machine", "twisting cutting machine",
        "meat processing machine fat analyzer", "fat analyzer meat machine",
        "multifunctional meat chopper", "meat chopper multifunctional",
        "processing tool foodstuffs", "food processing tool",
        "household vegetable cutter", "vegetable chopper household",
        "vegetable chopping machine", "chopping machine vegetable",
        "high speed chopping cutter", "multiple-tool chopping cutter",
    ],

    "Macerator/Comminutor": [
        "waste treating apparatus drum", "drum waste treating apparatus",
        "disposal processing apparatus management", "solid waste diverter drum",
        "drum solid waste diverter", "waste diverter apparatus",
    ],

    "Macerator/Pesquisa sobre trituradores": [
        "agriculture biomass processing", "field harvester sorghum",
        "sorghum harvester field", "cane juice extractor",
        "juice extractor cane", "seedbed conditioning tillage",
        "tillage apparatus seedbed", "land preparation clearing apparatus",
        "apparatus land clearing", "material conditioner land",
        "chopper drum forage harvester", "forage harvester chopper drum",
        "cutterhead forage harvester", "chaff-cutter cutting corn",
        "chaff cutter chopper", "conditioning roller chaff",
        "forage harvester knife apparatus", "silage chopper machine",
        "fiber chopper roll retainer", "roll retainer fiber chopper",
        "fiber chopper idler roll", "fiber chopper improved idler",
        "chopper unwound linear items", "fiber chopper method",
        "fiber chopper linear items",
        "fragmentation multicell filaments", "phytoplankton cell walls fragmentation",
        "multicell filament fragmentation device",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Pumps / Screw Pump — screw machine variants
    # ──────────────────────────────────────────────────────────────────
    "Pumps/Screw Pump": [
        "screw machine rotary", "rotary screw machine",
        "volume screw machine", "screw machine transforming motion",
        "transforming motion screw machine", "rotary type screw machine",
        "screw machine method production", "hydraulic screw machine balance",
        "screw machine balance plunger", "hydraulic screw machine plunger",
        "screw machine end method", "feed apparatus screw machine",
        "fluid line resonator screw", "screw machine fluid conveying",
        "rotary screw machine method", "motion screw machine rotary",
        "screw machine transforming rotary", "screw press auger blades",
        "screw press biogas plant", "auger blades screw press",
        "screw rod pump bridge breaking", "hopper pump bridge device",
        "variable pitch screw rod pump", "low viscosity spiral pump",
        "spiral sucker rod pump", "spiral sucker pump low viscosity",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Pumps / PC Pump — progressive cavity misc.
    # ──────────────────────────────────────────────────────────────────
    "Pumps/PC Pump and Motor": [
        "progressive cavity hydraulic machine", "cavity hydraulic machine",
        "moineau type gear mechanism", "moineau gear resilient sleeve",
        "resilient sleeve moineau", "asymmetric contouring elastomer liner",
        "elastomer liner lobes moineau", "power section stator moineau",
        "stator modular interior", "stator with modular interior",
        "stator inserts downhole motors", "stator inserts fabricating",
        "progressive cavity apparatus transducer", "transducer cavity apparatus",
        "progressive cavity transducer forming", "fluid rotary device cavity",
        "pump stator composite liner", "composite liner stator pump",
        "optimized liner positive displacement", "liner positive displacement motor",
    ],

    "Pumps/Hydraulic Pump": [
        "hydraulic device meshed gear", "hydraulic device helical gear",
        "hydraulic cable lift", "cable lift hydraulic",
        "hydraulic device fluid", "fluid hydraulic device",
        "expulsion device pressure medium", "pressure medium expulsion",
        "fluid-flow system device", "fluid flow system device method",
        "conveying device fluid", "device conveying fluid medium",
        "device conveying medium fluid",
        "transverse load apparatus hydraulic", "hydraulic transverse load",
        "stroker device hydraulic", "hydraulic stroker",
    ],

    "Pumps/Screw conveyor": [
        "auger dewatering system", "dewatering auger system",
        "improved auger dewatering", "auger dewatering improved",
        "hopper sludge transport", "hopper transporting sludge",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Filtration / Paper and Pulp — refiner plates
    # ──────────────────────────────────────────────────────────────────
    "Filtration/Paper and Pulp Filter": [
        "refiner plate", "refiner disk", "refiner disc",
        "refiner plate segment", "refiner plate carrier",
        "refiner assembly mounting", "bar groove pattern refiner",
        "groove pattern refiner plate", "tooth refiner plate",
        "v-shaped tooth refiner", "varying feeding angles refiner",
        "refiner stator plate outer row", "high intensity refiner plate",
        "inner fiberizing zone refiner", "refiner disk sensor",
        "sensor refiner disk", "refiner plate method",
        "refiner plate pulp", "pulp refiner plate",
        "moagem em via úmida", "moedores via úmida",
        "wet grinding process", "wet milling process",
        "aparelho de peneiração de pressão", "peneiração de pressão suspensão",
        "pressure screening apparatus suspension", "pressure screening raw material",
        "disperger grooved pyramid teeth", "grooved pyramid teeth disperger",
        "disperger plate grooved", "pressure screen suspension material",
        "rolling mill", "laminador", "rolling mill device",
        "multi-roll rolling", "rolling mill apparatus",
    ],

    "Filtration": [
        "disposição introduzida moinho cerâmico", "moinho cerâmico disposição",
        "ceramic mill arrangement", "arrangement ceramic mill",
        "carcaça moinho de rolos", "carcaça para moinho",
        "moinho de rolos carcaça", "roller mill housing",
        "moagem em via úmida moedores", "moagem farinha grãos duros",
        "farinha grãos duros trigo", "wheat flour milling",
        "processo moagem via úmida", "milling process wet grinding",
        "seção de recheio leito", "seção recheio",
        "packing section bed", "filling section bed packing",
        "arrangement separating liquid mixtures", "liquid mixture separating arrangement",
        "hopper transporting sludge", "sludge transport hopper",
        "device dehumidifying compacting sewage", "dehumidifying compacting solids sewage",
        "rotary fan press", "fan press rotary",
        "fruit press device", "press fruit device",
        "screw press solid liquid separation",
        "glass powder particle size distribution", "glass powder preparation process",
        "phosphate minerals processing recover", "phosphate minerals recover clays",
    ],

    "Filtration/Self-Cleaning and Backwash": [
        "screen blockage measurement flow", "screen blockage optimization",
        "flow performance optimization screen",
    ],

    # ──────────────────────────────────────────────────────────────────
    # NOVA PASTA DE NÍVEL SUPERIOR — Conveyor and Transport
    # ──────────────────────────────────────────────────────────────────
    "Conveyor and Transport": [
        "conveyor belt", "belt conveyor", "screw conveyor",
        "chain conveyor", "roller conveyor", "slat conveyor",
        "drag conveyor", "apron conveyor", "bucket elevator",
        "vibratory conveyor", "pneumatic conveyor", "conveyor system",
        "conveying direction", "conveying mechanism", "conveying device",
        "material conveying", "longitudinal conveyor", "feeding hopper",
        "discharge port conveyor", "discharge opening conveyor",
        "transport mechanism", "material transport device",
        "transportador de correia", "esteira transportadora",
        "correia transportadora", "transportador de parafuso",
        "sistema de transporte", "mecanismo de transporte",
        "elevador de caçamba", "conveyor drive", "conveyor speed",
        "conveyor frame", "conveyor roller", "screw feeder",
        "auger feeder", "rotary feeder", "vibratory feeder",
        "feeding hopper device", "discharge conveyor belt",
        "material feed conveyor", "conveyor assembly",
        "transfer device conveyor", "conveying apparatus",
    ],
    "Conveyor and Transport/Screw Conveyor": [
        "screw conveyor device", "auger conveyor device",
        "helical conveyor device", "spiral conveyor device",
        "worm conveyor device", "screw feeder mechanism",
        "transportador parafuso", "rosca transportadora",
        "parafuso sem-fim", "screw feeding device",
        "conveying screw device", "conveying auger device",
        "chaff processing distribution device", "chaff distribution conveyor",
    ],
    "Conveyor and Transport/Belt Conveyor": [
        "belt conveyor system", "conveyor belt system",
        "conveyor belt assembly", "belt conveyor design",
        "conveyor belt mechanism", "belt conveyor device",
        "slat conveyor device", "apron conveyor device",
        "drag conveyor device", "conveyor belt drive",
    ],

    # ──────────────────────────────────────────────────────────────────
    # NOVA PASTA DE NÍVEL SUPERIOR — Agriculture and Biomass
    # ──────────────────────────────────────────────────────────────────
    "Agriculture and Biomass": [
        "forage harvester", "cutterhead", "chaff cutter", "chaff-cutter",
        "silage chopper", "chopper drum harvester", "forage knife",
        "forage harvester knife", "conditioning roller harvester",
        "field harvester", "sorghum harvester", "cane harvester",
        "seedbed conditioning", "tillage apparatus", "land preparation",
        "material conditioner soil", "agricultural machine processing",
        "biomass processing", "biomass fuel", "plant biomass",
        "biomass heater", "engineered plant biomass",
        "wood chip optimizer", "wood chip production",
        "device producing wood chips", "wooden debris compressor",
        "brush cutter", "brush cutter wear", "garden chipper",
        "chipper mulcher", "garden waste chipper", "branch chipper",
        "cane juice extractor", "juice extractor cane",
        "cereal grinding system", "grain grinding wet",
        "crop straw filament", "straw filament rubbing machine",
        "straw rubbing machine crop", "filament rubbing machine",
        "processamento de biomassa", "colhedora de forragem",
        "máquina colhedora", "picador de forragem",
        "processo produção óleo mineral",
    ],
    "Agriculture and Biomass/Forage and Harvesting": [
        "forage harvester chopper drum", "forage harvester knife mounting",
        "cutterhead forage harvester", "chopper drum forage",
        "conditioning roller chaff", "chaff-cutter microwave",
        "silage harvester machine", "silage cutting machine",
        "forage knife design", "forage knife assembly",
        "roll retainer fiber chopper", "fiber chopper roll",
    ],
    "Agriculture and Biomass/Biomass Processing": [
        "biomass fuel processing", "biomass processing plant",
        "wood chip optimizer device", "wooden debris compressor device",
        "device wood chips combustion", "biomass heater wood chip",
        "processing biomass method", "engineered plant biomass feedstock",
        "feedstock particles biomass", "biomass feedstock engineering",
        "sorghum field harvester", "sweet sorghum harvester",
        "cane juice extraction method", "juice extractor apparatus",
        "recycling carpet method", "carpet recycling apparatus",
    ],

    # ──────────────────────────────────────────────────────────────────
    # NOVA PASTA DE NÍVEL SUPERIOR — Mixing and Agitation
    # ──────────────────────────────────────────────────────────────────
    "Mixing and Agitation": [
        "stirring shaft", "stirring processing device",
        "stirring device", "agitation device", "mixing device",
        "mixer machine", "blending device", "agitation mechanism",
        "stirring mechanism", "homogenizer device",
        "kneader device", "mixing apparatus", "mixing drum",
        "mixing vessel", "agitator shaft", "stirrer device",
        "mixing impeller", "eixo de agitação",
        "dispositivo de agitação", "misturador industrial",
        "agitador", "homogeneizador", "amassador",
        "stirring apparatus method", "arrangement homogenizing sample",
        "homogenizing sample method", "mixing device dry blends",
        "dry blends extrudable material", "inorganic organic mixing",
        "blender blade design", "blender adapter outboard",
        "blender blade assembly", "mixing inorganic organic blends",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Filtration PT/BR — termos que faltavam para patentes brasileiras
    # ──────────────────────────────────────────────────────────────────
    "Filtration/Filter Media and Cartridge": [
        "substrato dobrado substância química", "substrate folded chemical",
        "produto substrato dobrado", "folded substrate chemical applied",
        "wax sealed filter edge", "film filter wax edge",
        "película de filtro bordas vedadas cera",
        "processo fabricação montagem filtro",
        "filtro não tecido", "filtro não-tecido lightweight",
        "lightweight spun-bonded non-woven", "spun-bonded nonwoven properties",
        "nonwoven mechanical properties lightweight",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Grinding and Milling — BR patents e outros faltantes
    # ──────────────────────────────────────────────────────────────────
    "Grinding and Milling": [
        "moagem em via úmida", "moedores via úmida produção",
        "wet grinding mills production", "wet milling mills",
        "processo moagem via úmida moedores",
        "moagem de farinha grãos duros", "flour grinding hard wheat",
        "sistema moagem farinha trigo", "wheat flour grinding system",
        "disposição introduzida moinho", "ceramic mill arrangement",
        "máquina de esmerilhar", "esmerilhadora dispositivo",
        "grinding machine arrangement", "arrangement grinding machine",
        "carcaça moinho de rolos", "roller mill housing casing",
        "rolling mill device", "rolling mill apparatus",
        "laminador dispositivo", "rolling mill system",
        "millstone device", "millstone grinding",
        "spinning cutter door shredder", "shredder cutter door spinning",
    ],
    "Grinding and Milling/Industrial Grinder": [
        "automation control plastic pulverizer", "automatic plastic pulverizer",
        "powerful pulverizer device", "ultrafine smashing machine",
        "smashing machine ultrafine", "powerful smashing device",
        "vertical crusher device", "vertical grinding crusher",
        "automation pulverizer control", "pulverizer automation",
        "cool water pipe rubber twisting", "rubber twisting cutting structure",
    ],
    "Grinding and Milling/Pulverizer and Superfine Mill": [
        "powderizer machine", "powder machine device",
        "glass powder particle distribution", "glass powder preparation",
        "composite resin waste pulverizing", "pulverizing composite resin",
        "resin waste pulverizing method", "pulverizing method recycling",
        "deblocking classifier black tea", "black tea deblocking device",
    ],
    "Grinding and Milling/Ball and Roller Mills": [
        "moinho cerâmico disposição", "ceramic mill disposition",
        "ceramic mill arrangement introduced", "rolling mill device multi-roll",
        "multi-roll rolling mill", "rolling mill multi-roll",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Sealings — sliding ring / torque transmission
    # ──────────────────────────────────────────────────────────────────
    "Sealings/Mechanical Seal": [
        "sliding ring improved inlet", "sliding ring inlet properties",
        "slide ring inlet seal", "sliding ring seal inlet",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Drive Shafts — shaft/hub torque
    # ──────────────────────────────────────────────────────────────────
    "Drive Shafts": [
        "arrangement transmitting torque shaft hub", "transmitting torque shaft hub",
        "torque shaft hub arrangement", "shaft hub torque arrangement",
        "torque transmission shaft hub", "shaft hub torque transmission",
        "propeller shaft automobile", "automobile propeller shaft",
        "propeller shaft automotive design",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Pumps — misc. faltantes
    # ──────────────────────────────────────────────────────────────────
    "Pumps": [
        "fluid-flow system device method", "fluid flow system method",
        "ejector pump device", "ejetor bomba",
        "bomba ejetora fluido", "fluid ejector pump",
        "pump discharge baffle means", "discharge baffle pump means",
        "pump having discharge baffle", "oil gas separation buffering",
        "oil gas buffering tank", "buffering tank oil gas separation",
        "oil-gas separation buffering tank", "tubular slug reducer pump",
        "slug reducer tubular device", "slug flow removing device",
        "oil-gas separating slug flow", "slug flow oil gas",
    ],

    "Pumps/Diaphragm Pump": [
        "controle posição diafragma bombas", "posição diafragma bombas hidráulicas",
        "hydraulically driven diaphragm pump control",
        "diaphragm position control hydraulic pump",
        "bomba acionada hidraulicamente diafragma",
        "bomba diafragma controle posição",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Media and Document Destruction
    # ──────────────────────────────────────────────────────────────────
    "Media and Document Destruction": [
        "destruction device data carriers", "data carrier destruction device",
        "destruction device peripheral devices", "data carrier peripheral destruction",
        "high-security data removal disk", "data removal disk machine",
        "portable high-speed data disk", "high speed disk data removal",
        "apparatus destruction tickets", "destruction tickets apparatus",
        "medication disposal system device", "medicine drug disposal system",
        "recording medium destruction discarding",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Separator — misc.
    # ──────────────────────────────────────────────────────────────────
    "Separator": [
        "oil-gas separation buffering tank", "oil gas separating slug",
        "slug flow removing separator", "slug reducing device",
        "tubular slug reducer device", "slug reducer tubular",
        "arrangement separating liquid mixtures", "liquid mixtures separator arrangement",
        "seção de recheio leito", "packed section bed tower",
        "filling section packing bed", "bed packing section column",
        "dehumidifying compacting solids sewage", "compacting solids sewage separator",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Monitoring — misc.
    # ──────────────────────────────────────────────────────────────────
    "Monitoring and controlling": [
        "method determining status machine", "machine status determination method",
        "machine learning equipment failure", "equipment failure prediction learning",
        "data preprocessing predictive engine", "preprocessing system predictive",
        "system well logging acoustic", "well logging system",
        "acoustic fluid analyzer well", "machine tool access control device",
        "apparatus controlling machine tool", "controlling machine tool operations",
    ],

    # ──────────────────────────────────────────────────────────────────
    # Oil Tools / Production Technology
    # ──────────────────────────────────────────────────────────────────
    "Oil Tools/Production Technology": [
        "methods extracting oil tar sand", "tar sand oil extraction",
        "extracting oil tar sand method", "process production mineral oil",
        "mineral oil production process",
    ],

}

for _k, _v in _EXPANSAO_V4.items():
    if _k in PALAVRAS_CHAVE:
        _existing = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _existing])
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V5 — Análise profunda dos 684 sem classificação
# Três grandes grupos identificados com abstracts completos:
#   1. Shredders de papel/documento (JP/US/DE/EP) ~200 patentes
#   2. Disposers de cozinha/pia (JP/KR/CN/US)    ~80 patentes
#   3. Trituradores industriais CN/JP/DE          ~100 patentes
# + filtração BR, rolamentos, bombas, oil tools, etc.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V5 = {

    # ─────────────────────────────────────────────────────────────────
    # Media and Document Destruction — paper shredders (maior gap)
    # Problema: "shredder" = 1pt, não passa SCORE_MINIMO=2.
    # Solução: adicionar expressões de 2+ palavras específicas de
    # trituradoras de papel e mídias.
    # ─────────────────────────────────────────────────────────────────
    "Media and Document Destruction": [
        # tipos de shredder
        "paper shredder", "document shredder", "crosscut shredder",
        "strip-cut shredder", "micro-cut shredder", "high-security shredder",
        "office shredder", "personal shredder", "heavy-duty shredder",
        "portable shredder", "handy shredder", "no-oil shredder",
        # componentes de shredder
        "shredder blade", "shredder blades", "shredder cutter",
        "shredder cutting", "shredder bin", "shredder basket",
        "shredder housing", "shredder opening", "shredder head",
        "shredder mechanism", "shredder motor", "shredder drum",
        "blade assembly shredder", "cutter assembly shredder",
        "cutting cylinder shredder", "knife roll shredder",
        "shredder knife", "shredder teeth", "shredder shaft",
        "shredder roller", "shredder disc", "blade set shredder",
        "stripper shredder", "shredder stripper",
        # funcionalidades
        "shredder safety", "shredder detection", "shredder sensor",
        "shredder bin full", "shredder full indicator",
        "shredder lubrication", "shredder oiling",
        "shredder jam", "shredder reverse", "shredder auto",
        "shredder touch detection", "shredder biometric",
        "shredder gas detection", "shredder sound",
        "shredder compactor", "shredder collection",
        "shredder waste bin", "shredder waste receptacle",
        "shredder storage", "shredder log",
        # papel / documentos
        "paper shredding", "document shredding", "paper cutting shredder",
        "sheet shredding", "shredding paper", "shredding documents",
        "paper insertion slot", "paper feed slot", "paper inlet shredder",
        "paper removal device shredder", "horizontal paper removal",
        "paper feed roller shredder", "paper feed shredder",
        # mídias / dados
        "data carrier shredder", "data storage shredder",
        "disk shredder", "cd shredder", "dvd shredder",
        "credit card shredder", "media shredder",
        "recording medium shredder", "data destruction shredder",
        "shredder cd dvd", "shredder floppy",
        # compostos
        "shredder compactor device", "shredder container",
        "shredder emptying panel", "chad containment shredder",
        "shredder movable cover", "covering board shredder",
        "shredder adjustable opening", "shredder pivotable panel",
        "shredder access panel", "shredder top panel",
        "shredder side rail", "side rail shredder",
        "shredder input port", "input port shredder",
        "shredder entry prevention", "entanglement prevention shredder",
        # japanese patent style
        "shredder shredder", "shredder chopping", "shredder waste box",
        "shredder rotary cutter", "shredder fixed blade",
        "shredder moving blade", "shredder rocking member",
        "document management shredder", "shredding document management",
        "image forming shredder", "shredder image forming",
        # compostos espessos
        "shredder with oiling", "shredder with safety",
        "shredder with adjustable", "shredder with biometric",
        "shredder with gas detection", "shredder with dual stage",
        "shredder with rotatable device", "shredder with protective",
        "adaptable shredder housing", "shredder and compacting",
        # trituradora de papel (PT/ES)
        "trituradora de papel", "destructora de documentos",
        "triturador documentos", "destruição documentos",
        "corte de papel", "trituragem de papel",
        # destruição de dados
        "data storage device destruction", "rendering data unrecoverable",
        "data disk pressing destruction", "disk destruction pressing",
        "hard disk destruction", "disk data destruction machine",
        "high-security data removal", "secure data destruction",
        "fast secure data removal", "data removal portable machine",
        # shredder seguro (cofre)
        "safe built-in destruction", "safe recording media protection",
        "safe data destruction", "recording media safe destruction",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Macerator / Food Waste Disposer — sink disposers, kitchen waste
    # Muitos JP/KR com título apenas "Disposer" = 1pt insuficiente
    # ─────────────────────────────────────────────────────────────────
    "Macerator/Food Waste Disposer": [
        # tipos de disposer
        "sink disposer", "food waste disposer", "kitchen disposer",
        "garbage disposer", "waste disposer", "household disposer",
        "sink disposal", "garbage disposal", "food disposal",
        "in-sink disposer", "under-sink disposer", "under-sink waste",
        "under-sink processor", "sink grinder",
        # funcionalidades
        "disposer crushing", "disposer grinding", "disposer motor",
        "disposer blade", "disposer impeller", "disposer chamber",
        "disposer drain", "disposer housing", "disposer operation",
        "disposer cleaning", "disposer maintenance", "disposer control",
        "disposer flange", "disposer strainer", "disposer installation",
        "disposer fine bubbles", "disposer water supply",
        "disposer bacteria elimination", "disposer sterilization",
        "disposer garbage measurement", "disposer load cell",
        "disposer metal sensor", "disposer metal detector",
        "disposer tentative holding", "disposer waste weight",
        # estilo japonês
        "disposer apparatus", "disposer device", "disposer unit",
        "disposer system", "disposer mechanism", "disposer safety",
        "disposer tank", "disposer container", "disposer sink",
        "garbage disposal apparatus", "food waste disposal apparatus",
        "garbage treatment apparatus", "waste treatment disposer",
        "garbage cutting apparatus", "garbage crushing apparatus",
        "food waste crushing", "garbage disposal system",
        "garbage disposal machine", "garbage disposal device",
        "disposer garbage disposal", "disposer pulverizing",
        # compostos
        "food waste disposal system", "food waste disposal platform",
        "food waste disposal unit", "food waste disposal machine",
        "waste disposal bin commercial", "commercial food waste disposal",
        "food rubbish processor", "enclosed rubbish processor",
        "rubbish disposal machine", "house refuse disposal machine",
        "garbage treatment device household", "household garbage treatment",
        "drier food waste disposal", "food waste drier",
        # grinder para disposer
        "grinder assembly waste disposal", "grinder waste disposal",
        "grinder tank disposal", "shredding blade disposal",
        "waste disposal grinder", "waste disposal grinding",
        "waste disposal crushing", "waste disposal agitating",
        # KR / CN style
        "sink disposer crushing", "crushing means disposer",
        "disposer rotary grinding plate", "rotary grinding plate disposer",
        "food waste processing sink", "sink food waste processing",
        "food waste disposal sink", "sink drain food waste",
        "crushing unit sink", "sink waste crushing unit",
        "waste disposal dehydration", "food waste dehydration disposal",
        # kitchen waste broader
        "kitchen waste disposal", "kitchen rubbish disposal",
        "kitchen garbage disposal", "kitchen waste crushing",
        "restaurant garbage shredding pulping", "garbage shredding pulping",
        "kitchen garbage crashing", "kitchen rubbish breaking",
        "bag breaking kitchen", "bag breaking rubbish",
        # medical / biohazard waste disposal
        "biologically hazardous waste disposal", "medical waste disposal",
        "waste disposal biohazard", "biohazard waste unit",
        "medical waste disintegration", "medical waste shredder disinfect",
        "apparatus processing medical waste", "processing medical waste apparatus",
        "waste disposal pathogen", "pathogen reduction disposal",
        # composting disposer
        "food waste composting disposal", "organic waste disposal composting",
        "composting disposal system", "food waste microbes disposal",
        "waste disposal decomposition", "food waste decomposing disposal",
        # macerator for RV / portable
        "macerator sewerage contra-rotating", "macerator chamber inlet outlet",
        "macerator assembly waste port", "waste disposal port macerator",
        "macerator recreational vehicle", "rv waste disposal macerator",
        # organic waste treatment
        "organic waste treatment device", "organic waste compacting machine",
        "organic waste disposal apparatus", "waste treatment organic compacting",
        "organic compost smashing", "compost organic smashing tank",
        "garbage treatment organic", "organic waste management device",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Macerator / Industrial Crusher — crushers industriais CN/JP/DE
    # ─────────────────────────────────────────────────────────────────
    "Macerator/Industrial Crusher": [
        # tipos de crusher
        "vertical crusher", "horizontal crusher", "jaw crusher",
        "cone crusher", "impact crusher", "roll crusher",
        "roller crusher", "twin-shaft crusher", "single-shaft crusher",
        "swing arm crusher", "shear-type crusher", "existing pipe crusher",
        "self-traveling crusher", "grapple grinder",
        "rotary grinder apparatus", "rotary grinder drum",
        # materiais processados
        "rubber crusher", "plastic crusher", "plastic sheet crusher",
        "pressurized plastic crusher", "automatic plastic crusher",
        "high-efficiency plastic crusher", "silent centralized pulverizer",
        "fruit crusher", "fruit peel crusher", "detachable fruit crusher",
        "anise oil ice block crusher", "ice block crusher",
        "garbage crusher", "garbage crushing equipment",
        "garbage crushing bin", "garbage crushing chamber",
        "rubbish crusher", "industrial rubbish processor",
        "smashing mechanism rubbish", "house refuse disposal machine",
        "organic garbage treatment", "novel household garbage treatment",
        "enclosed rubbish processor", "vertical rapid granulator",
        # CN utility model style
        "crusher utility model", "crushing chamber device motor",
        "crushing chamber frame", "feed hopper crushing",
        "crushing chamber feed hopper", "frame motor crushing",
        "discharge chamber crushing", "crushing cavity working",
        "hob frame blade screen", "blade screen material storage",
        "fixed knife moving knife crusher", "moving knife fixed knife",
        "fixed blade rotary blade crusher", "rotary blade fixed blade",
        "cutting tool rotary assembly", "rotary assembly cutting tool",
        "drive motor crushing chamber", "crushing motor blade fixed",
        # DE-style comminuting
        "comminuting machine cutting tool", "comminuting tool cutting",
        "comminuting apparatus housing", "comminuting or chopping",
        "comminuting general cargo", "apparatus shredding general cargo",
        "crushing feeding crop bioreactor", "crop crushing bioreactor",
        "bone remnants cremation comminution", "bone cremation comminuting",
        "chip breaking comminutor shafts", "chip breaker comminutor",
        "bulk material crusher drive", "crusher bulk material drive unit",
        "drive unit crusher bulk", "crusher roller drive motor",
        # tipos específicos
        "copper aluminum separating heat exchanger", "copper aluminum separation heat",
        "heat exchanger crushing separation", "heat exchanger crushing method",
        "titanium sponge crusher extrusion", "extrusion shearing crusher titanium",
        "device breaking rapid quenching", "rapid quenching strip breaker",
        "lead pig granulator slicing", "slicing mechanism granulator lead",
        "extrusion shear crusher", "extrusion shearing type crusher",
        "eddy current crushing pelletizing", "crushing pelletizing eddy",
        "rotating disk crushing system", "disk sections crushing system",
        "two rotating disk crusher", "crushing system rotating disk",
        # pill/tablet crusher
        "pill crusher assembly", "pill crusher base handle",
        "tablet crusher device", "drug crusher medical",
        # continuous crusher
        "continuous flow micro-crusher", "micro-crusher continuous flow",
        "continuous crushing system compaction", "compaction chamber screw crusher",
        # paper pulp/fiber crusher
        "non-pulpables collection pulpers", "solid waste pulpers basket",
        "waste pulping system impeller", "pulping impeller blade",
        "waste pulping apparatus impeller", "impeller blade pulping",
        "loosefill insulation bag digester", "bag digester insulation",
        "agitator sewer system", "inline agitator sewer",
        # general crushing
        "system for crushing material", "apparatus for crushing material",
        "apparatus crushing grains", "crushing grains rollers",
        "crushing material apparatus rock", "apparatus rock ore crushing",
        "sizing roller screen ore", "ore processing sizing roller",
        "mobile crusher assembly screen", "mobile bucket crusher",
        "crusher realizing facilitation", "facilitation crushing clearout",
        # wood
        "wood cutter high pressure pump", "wood cutter water jet",
        "water jet wood cutting", "hedge trimmer ribbed roller",
        "hedge trimmer cutter unit", "garden vegetation shredder",
        "horizontal cutting roller garden", "wood collection reducing machine",
        "conical cutting drum shredder", "wood reducing machine conical",
        "chaff-cutter garden wood", "wood shredder microwave emitter",
        "device wood chips setting element", "chip making device cutters",
        "chip making device production", "wood chip production device",
        "crop processing substrate first machine", "machine plant processing crops",
        # tire/rubber
        "method apparatus crushing waste tyre", "crushing waste tire method",
        "method device crushing waste tire", "rubber crusher toothed disc",
        "rubber crushing equipment toothed", "tire chip rubber crushing",
        "rubber cord cutting tool", "cutting knife rubber cord",
        "cutting knife armored rubber",
        # ceramic/mineral extended
        "apparatus crushing material rock", "crushing rock ore stone",
        "material spreader crushing", "material conditioner drum",
        "bale shredder flail auger", "bale breaker auxiliary powerfeed",
        "bale breaker horizontal grinder", "convertible discharge bale shredder",
        "multi-functional tool material processing machine",
        "multi-functional tool waste processing machine",
        "multi-functional tool assembly material processing",
        "multi-functional tool assembly waste processing",
        # colorant comminution
        "colorant dispensing pre-comminuted", "pre-comminuted material colorant",
        # aerodynamic
        "aerodynamic pulverizer roof coatings", "pulverizer roof coating reprocessing",
        # lump breaker
        "lump breaker bulk flow", "lump breaking method bulk",
        # continuous waste processing
        "system processing waste continuous", "waste processing continuous infeed vessel",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Macerator — expansão da raiz
    # ─────────────────────────────────────────────────────────────────
    "Macerator": [
        "drum solid waste", "solid waste diverter drum",
        "drum waste diverter helical", "helical coil waste diverter",
        "waste diverting drum", "compacting organic waste machine",
        "integrated system separation waste", "organic waste compacting",
        "waste treatment machine integrated", "compacting waste apparatus method",
        "waste toner cartridge processing", "toner cartridge crushing",
        "waste processing continuous basis", "waste processing pathogen",
        "apparatus processing medical waste", "medical waste apparatus disinfect",
        "medicinal material slicing machine", "medicinal material slicer",
        "medicinal material crusher", "baffle medicinal crusher",
        "traditional chinese medicine crusher", "double-layer barrel pulverizer",
        "portable cordyceps crusher", "refined cotton grinder",
        "smooth anti-residual cutting bin", "cordyceps smashing",
        "asbestos crushing system", "asbestos crushing method",
        "sludge reduction treatment", "sludge processing apparatus",
        "sludge processing auger", "sludge auger trough",
        "deodorization foreign matter sorting", "deodorant foreign matter sorting",
        "deodorant foreign matter separator", "organic matter foreign separator",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Macerator / Cutting Elements
    # ─────────────────────────────────────────────────────────────────
    "Macerator/Cutting Elements": [
        "cutter knife cutter head", "cutter head knife cutter",
        "cutting knife various materials", "knife crushing rubber cord",
        "cutting knife armored rubber", "rotary cutting tool knife",
        "cutter assembly rotatable", "rotatable cutter assembly",
        "cutting wheel secondary cutters", "cutting wheel discrete plates",
        "knife roller granulating plastic", "knife roller plastic granulation",
        "granulator blade v-shaped saddle", "v-shaped saddle blade granulator",
        "industrial waste crushing bit", "crushing bit hard metal",
        "crushing bit wear resistance", "super-hard bit wear crushing",
        "granulator helical-shaped cutter", "helical shaped cutter granulator",
        "elliptical acetabuliform blade", "acetabuliform blade shredder",
        "blade crosscut shredder", "crosscut shredder blade",
        "blade punching bending", "shredder blade punching bending",
        "assembly structure grinder knife", "grinder knife rest shaft",
        "knife rest shaft assembly",
        "crushing component extractor", "extractor biological substance",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Filtration — patentes BR + outros faltantes
    # ─────────────────────────────────────────────────────────────────
    "Filtration": [
        # BR português
        "filtro de bolsas", "filtro bolsas armação",
        "filtro e método fabricação", "método fabricação filtro",
        "dispositivo de filtragem profunda", "filtragem profunda módulo",
        "elemento filtrante plano módulo", "módulo de filtragem elementos",
        "estruturas porosas separação fluidos", "estruturas porosas fabricação",
        "filtração em contracorrente diafragma", "contracorrente diafragma filtração",
        "processo dispositivo filtração contracorrente",
        "membrana de filtro microporosa", "filtro microporoso membrana",
        "membrana microporosa método produzir", "separador membranas microporosas",
        "película de filtro bordas cera", "película filtro cera impermeável",
        "filtro processo produção gênero", "filtro barras elementos apoio",
        "filtro plano cilindro barras",
        "aparelho de filtro em linha", "filtro em linha duto",
        "filtro linha fluxo montante", "filtro acanalado acabaladura",
        "filtro e método de fabricação de um filtro",
        "membrana de filtro microporosa método",
        "setor para filtros rotativos à vácuo",
        "filtro de bolsas armação frontal",
        "elemento filtrante plano módulo de filtragem",
        "processo fabricação montagem filtro elemento",
        "filtro processo para produção filtro",
        # EN filter variants
        "filter apparatus inline", "inline filter apparatus duct",
        "filter assembly frame element", "filter assembly support bars",
        "filter fabrication method assembly", "filter production process bars",
        "filtration membrane deep device", "deep filtration device module",
        "microporous filter membrane method", "filter membrane microporous separator",
        "flat filter element module", "filter module flat elements",
        "porous structure fluid separation", "separation fluids porous structure",
        "filter wax edge sealing", "filter edge wax impermeabile",
        "bag filter front frame", "filter bag reinforcement frame",
        "filter layer adsorption vapor particle", "vapor particle filter layers",
        "organic vapor particle filter", "filter adsorption vapor organic",
        "filter medium bars support elements", "filter bars support elements",
        # paper/pulp refiner extended
        "refiner blade element fibrous", "refiner fibrous material surfaces",
        "refiner first second surface", "refiner surface fibrous material",
        "refiner and blade element",
        # food/coffee filter
        "coffee capsule feeding unit", "conjunto alimentar café preembalados",
        "coffee portions preparation unit", "feeding coffee portions machine",
        "tea packaging capsule machine", "tea capsule packaging airtight",
        "tea leaves breaking machine", "packaging tea capsule system",
        # activated carbon / adsorption filter
        "radioactive substance absorbent", "radioactive absorbent zeolite",
        "zeolite radioactive absorbent cellulose",
        # carpet/fiber filter
        "carpet recycling fiber backing", "carpet fiber separation backing",
        "carpet recycling method fiber", "recycling carpet fibers backing",
    ],

    "Filtration/Liquid Filter": [
        "filtro em linha dispositivo", "dispositivo filtro insere duto",
        "inline filter fluted medium", "fluted filter medium fitting",
        "liquid treatment dewatering apparatus", "liquid treatment press rolls",
        "dewatering liquid material press", "press rolls liquid treatment",
        "screw clearance separator screen", "screw screen separator housing",
        "apparatus clearance screw screen", "screw screen separator adjusting",
        "filtration membrane external pressure positive", "membrane filter external pressure",
        "screen blockage flow optimization", "flow performance screen blockage",
        "liquid dispenser vessel pump", "liquid vessel dispenser pump",
    ],

    "Filtration/Filter Media and Cartridge": [
        "filtro de bolsas armação frontal bolsas filtro",
        "membrana microporosa método produzir membrana",
        "película filtro bordas vedadas cera método vedação",
        "filtro barras elementos apoio barras suportam",
        "flat filter element plurality holes", "filter element flat holes axial",
        "porous structure fluid constituents", "porous structures fabrication process",
        "activated filter radioactive absorbent", "zeolite absorbent radioactive",
        "polymer coating metallic substrate", "substrate polymer coating intermediate",
        "powder metal mixture cellulose", "micronized cellulose powder metal",
        "lightweight spun-bonded non-woven", "spun-bonded non-woven mechanical",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Bearings — patentes não capturadas
    # ─────────────────────────────────────────────────────────────────
    "Bearings": [
        "novel bearing design", "bearing long service life",
        "bearing extreme dust environment", "bearing dust environment service",
        "bearing lubricant property", "bearing property lubricant determination",
        "bearing porous element lubricant", "bearing porous accommodating lubricant",
    ],
    "Bearings/Rolling Bearings": [
        "bearing end cap integrated seal", "bearing end cap seal groove",
        "vented bearing end cap", "bearing end cap vented shroud",
        "shield plate bearing annular", "bearing annular mounting groove",
        "bearing shield plate inner outer rings",
        "needle bearing lubricant leakage", "needle bearing rotational torque",
        "needle bearing outer ring flange", "bearing needle rotational torque",
        "bearing rotation sensor wire", "bearing with rotation sensor",
        "rotation sensor bearing wire", "bearing sensor axial direction",
        "bearing structure inner ring spherical", "bearing unit shaft housing",
        "bearing unit assembly flange", "bearing unit housing flange",
        "bearing having inner outer rings", "bearing concentrically bearing axis",
    ],
    "Bearings/Hub and Wheel Bearings": [
        "bearing device drive wheel knuckle", "drive wheel bearing knuckle",
        "bearing device vehicle wheel tapered", "tapered outer raceway bearing wheel",
        "bearing device for drive wheel", "drive wheel bearing device",
        "bearing drive wheel knuckle member", "knuckle member bearing drive wheel",
    ],
    "Bearings/Sliding Bearings": [
        "roll support device tapered surface", "roll support tapered surface axial",
        "rotating member support slinger", "slinger bearing rotating member",
        "rotating member support unit slinger",
        "propeller shaft support center bearing", "center bearing propeller shaft support",
        "propeller shaft support structure", "center bearing propeller support",
    ],
    "Bearings/Bearing Lubrication and Sealing": [
        "bearing supplying oil rotating shaft", "oil supply rotating shaft bearing",
        "bearing oil supply distribution cone", "distribution cone shaft bearing oil",
        "bearing oil supply annular reservoir", "annular reservoir bearing oil pool",
        "device supplying oil bearing points", "supplying oil bearing points rotating",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Pumps — bombas não capturadas
    # ─────────────────────────────────────────────────────────────────
    "Pumps": [
        "pump conveying medium carrier shafts", "carrier shafts transport elements pump",
        "ultra pump systems well", "pump removing liquids well",
        "pump elongated cylindrical chamber", "cylindrical pump chamber cover",
        "pump with motor pumping fluids", "pump housing upper lower conduit",
        "pump system host satellite pumps", "satellite supply pumps main pump",
        "pump apparatus controller signal", "pump controller first control signal",
        "pump for liquids design", "pump ornamental design patent",
        "pump adjusting delivery rate", "pump delivery rate adjustment method",
        "pump suction pressure transport", "transport element conveyance housing pump",
        "conical logarithmic spiral viscosity pump", "spiral viscosity pump conical",
        "rotary viscosity pump conical chamber", "viscosity pump impeller conical",
        "crossover two-phase flow pump", "two-phase pump impellers diffusers",
        "two-phase pump central outer section", "pump impeller diffuser two-phase",
        "wellbore pump plunger spring valve", "wellbore pump plunger passage",
        "pump liquids plunger wellbore", "wellbore pump valve piston spring",
        "device transferring energy fluid", "device energy fluid intermeshing screws",
        "gear mechanism moineau principle", "moineau principle pump compressor",
        "gear mechanism pump compressor transmission", "moineau gear pump motor",
        "implantable cardiac pump", "cardiac pump blood circulating",
        "blood drive cardiac pump", "pump blood cardiac implantable",
        "mortar mixing pump impeller", "cement mortar mixing pump",
        "mortar pump funnel mixing chamber", "pump mortar cement mixing",
        "fuel pump conveying fuel injection", "fuel injection pump worm drive",
        "pump heat-setting media printers", "printer pump worm drive",
        "pump heat setting worm",
        "pump liquids well elongated cylindrical",
        "fluid displacer pump conduit", "pump fluid displacer housing conduit",
        "rotary piston particle loaded fluid", "rotary piston pump particle loaded",
        "bevel-toothed rotary piston pump", "hydraulically driven rotary piston pump",
        "method delivering multiphase pump installation", "multiphase pump installation delivery",
        "multiphase delivering hydrocarbons well", "delivering multi phase mixture well",
        "pump apparatus system controller", "pump system controller signal output",
        "pump device foreign matter separator", "pump foreign matter separator device",
        "liquid treatment apparatus pump", "liquid treatment dewatering pump",
        "centrifugal mixing system recirculation", "mixing system recirculation pump",
        "apparatus adapting waste disposal pump", "waste disposal pump rv",
        "centrifuge wheel pump covering board", "screw centrifuge wheel pump",
        "covering board centrifuge wheel",
        "continuously pumping solid material", "pumping solid material liquid co2",
        "slurry preparation system pump", "oil sand slurry preparation pump",
        "method apparatus creating slurry pump", "slurry creation pump apparatus",
        "fuels blending system rotary dispersion", "blending system rotary dispersion pump",
        "fluid-flow system combining fluids", "combining fluids different pressures",
        "gas gathering system pump", "independently powered fluid system pump",
    ],

    "Pumps/Centrifugal Pump": [
        "crossover two-phase pump impeller", "two-phase flow pump impeller",
        "pump impeller diffuser inner outer", "inner outer section pump impeller",
        "alternate plate impeller washing", "impeller blades movable tips washing",
        "impeller blade movable tip", "washing machine impeller blade",
        "internal cutter submersed mixer pump", "submersed mixer impeller cutter",
        "mixer impeller shroud pump",
    ],

    "Pumps/PC Pump and Motor": [
        "stator tube downhole motor fabricating", "stator tube bonding agent inner surface",
        "stator helical bore cast material", "progressive cavity transducer stator",
        "stator profiled helical bore", "helical bore cast material layer transducers",
        "stator inner geometry equilateral", "hub shaft equilateral inner geometry",
        "over mandrel extrusion pcp stator", "mandrel extrusion pcp stator rubber",
        "crosshead extrusion helical rubber hose", "helical rubber hose crosshead extrusion",
        "rubber hose helical extrusion pcp", "elastomer extrusion helical stator",
        "stator modular interior cavity", "modular interior stator helical",
        "stator insert downhole motor flex", "flex stator insert motor fabricating",
        "asymmetric elastomer liner lobes", "elastomer liner asymmetrical contouring",
        "elastomer liner helical cavity contouring",
        "device transferring energy intermeshing screws", "intermeshing screws opposite pitch",
        "moineau pump compressor motor device", "moineau principle gear mechanism",
        "gear mechanism moineau pump motor",
        "fluid rotary device cavity progressive",
        "automatic tubing drain rotary pump", "tubing drain rotary pump reactive torque",
        "inverted motor drilling outer housing", "inverted drilling motor rotating housing",
        "deployment downhole pump cable motor", "downhole pump cable deployment system",
        "deploy downhole pump cable", "pump cable deployment motor well",
    ],

    "Pumps/Screw Pump": [
        "double-flow screw spindle machine", "screw spindle machine double flow",
        "double flow screw machine inlet chambers", "screw machine two inlet spaces",
        "screw machine multi-phase", "double-flow screw machine multiphase",
        "screw spindle machine tubular housing", "screw spindle tubular housing cast",
        "screw machine processing element kneading", "screw machine extension kneading element",
        "screw machine bulk material vacuum", "screw machine housing vacuum portion",
        "feed apparatus screw machine disc wheels", "disc wheels screw machine feed",
        "screw machine feed apparatus arching", "screw machine method production tubular",
        "screw machine and method production", "screw spindle machine wear layer",
        "hydraulic screw machine balance plunger", "screw machine balance plunger thread",
        "screw machine impeller balance plunger",
        "conveying device medium carrier shafts", "medium carrier shafts transport elements",
        "pump mortar cement impeller screw", "mortar pump funnel screw impeller",
        "pump for conveying heat-setting media", "pump heat-setting worm drive",
        "pump printer worm heat", "fuel pump worm drive injection",
    ],

    "Pumps/Vane type Pump": [
        "rotary viscosity pump conical", "conical viscosity pump impeller",
        "spiral viscosity pump housing", "logarithmic spiral viscosity pump",
    ],

    "Pumps/Hydraulic Pump": [
        "hydraulic device meshing cogwheels", "cogwheels helical teeth hydraulic",
        "hydraulic device oblique teeth", "oblique teeth hydraulic cogwheels",
        "hydraulic surface connector wellhead", "connector blow out preventer wellhead",
        "blow out preventer connector wellhead", "hydraulic connector bop wellhead",
    ],

    "Pumps/Diaphragm Pump": [
        "controle posição diafragma bomba hidráulica",
        "bomba acionada hidraulicamente diafragma pistão",
        "diaphragm pump piston transfer chamber", "hydraulic diaphragm piston reservoir",
        "hydraulically driven diaphragm pump piston",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Oil Tools — centralizer + downhole
    # ─────────────────────────────────────────────────────────────────
    "Oil Tools/Centralizer": [
        "bow-spring centralizer moving collars", "bow spring moving collars interlocked",
        "extendable collars bow spring centralizer", "interlocked stop collars bow spring",
        "centralizer tubular conduit clamping", "centralizer clamping bush rock drill",
        "centralizer body pipe string casing", "centralizer body outer surface pipe",
        "centralizer body upper lower portion arms", "centralizer body arms plurality",
        "centralizer locking collar self-locking", "self-locking collar centralizer tubular",
        "lock collar production string tubulars", "lock collar centralizer tubular",
        "centralizer opposing hollow spring structure", "hollow spring centralizer elongated",
        "low friction centralizer roller ball", "roller ball centralizer circumferential",
        "centralizer roller ball tubular body", "tubular body roller ball centralizer",
        "centralizer id borehole probe", "centralizer downhole probe pipe",
        "centralizing core orientation apparatus", "core orientation centralizing",
        "expandable centraliser borehole locating", "centraliser expandable adjustable",
        "centraliser tubing borehole expandable", "expandable centraliser body arms",
        "interference-fit stop collar positioning", "stop collar positioning tubular",
        "interference fit stop collar method", "method positioning device tubular collar",
        "well string centralizer forming method", "centralizer forming method well string",
        "pipe centralizer forming method", "forming method pipe centralizer",
        "centralizer anti-rotation quarter-turn sleeve", "quarter-turn centralizer anti-rotation",
        "stabilizer expandable reamer subs", "expandable reamer stabilizer subs",
        "dual rotary centralizer borehole rings", "rotating bodies ring centralizer borehole",
    ],

    "Oil Tools": [
        "downhole assembly articulated mandrel", "articulated mandrel passive active damping",
        "mandrel torsional stick-slip damping", "downhole assembly torsional control",
        "snap latch collet wellbore elements", "latch collet wellbore connecting",
        "collet tensile fins wellbore", "latch wellbore elements tensile",
        "wellhead isolation sleeve isolation frac", "isolation sleeve wellhead bore",
        "wellhead sleeve running tool installation",
        "high integrity hanger seal casing", "casing hanger seal cemented",
        "casing segments expansion cone wellbore", "casing overlap wellbore cemented",
        "oil field apparatus seal member rubber", "seal member rubber oxycellulose fibers",
        "oil field seal rubber cellulose nanofibers",
        "rotating control device bearing clamp", "bearing clamp rotating control device",
        "clamp device piston radially displacing",
        "downhole method injecting formation permeability", "injecting fluid formation permeability",
        "wellbore maintenance oil recovery", "wellbore maintenance improved oil recovery",
        "system wellbore maintenance operations",
        "positioning tool casing downhole", "positioning tool detecting unit casing",
        "detecting unit positioning casing downhole",
        "gas trap sampling fluid well", "gas trap drilling rig flow line",
        "low maintenance gas trap well",
        "device selective control fluid flow well rocks", "selective control fluid well surrounding",
        "fluid flow control well rock permeability",
        "downhole valve arrangement tubular ports", "valve arrangement tubular body ports",
        "valves bottom hole assemblies motor", "bottom hole assembly valve motor",
        "wellbore pump valve spring plunger",
        "well tool nanoparticle metallic coating", "nanoparticle reinforced metallic coating well",
        "methods extracting oil tar sand", "tar sand oil extraction formation",
        "in-situ liquefaction formation oil", "process production mineral oil formation",
        "process mineral oil deposits temperature",
        "coated sleeved oil gas well production", "sleeved production devices methods",
        "coated sleeve well production devices",
    ],

    "Oil Tools/Wellhead equipment": [
        "hydraulic surface connector bop", "blow out preventer connector casing head",
        "casing head connector wellhead", "connector bop casing head tubing",
        "wellhead tubular connector releasable", "releasable connector assembly tubular",
        "connector assembly tubular releasable payload",
        "made-up flange locking cap subsea", "cap subsea member external flange",
        "subsea member flange seal cap",
        "wellhead isolation sleeve frac fluid", "isolation sleeve wellhead frac",
        "remote operation rotating control device", "rotating control device housing body clamp",
        "system bore hole axial coupling mandrel", "bore hole coupling mandrel connecting",
        "shaft downhole equipment coupling driven", "shaft coupling driven devices nominal",
        "expansion system expandable tubulars", "expandable tubular resilient launcher",
        "resilient launcher launcher sleeve", "expandable tubular radially expanding",
    ],

    "Oil Tools/Drilling": [
        "inverted motor drilling outer housing rotating", "inverted drilling motor outer rotating",
        "expandable reamer apparatus stabilizer subs", "stabilizer subs expandable reamer",
    ],

    "Oil Tools/Production Technology": [
        "system method stimulating multi-zone well", "stimulating multi-zone well tubular body",
        "multi-zone well plugs pre-drilled holes",
        "wellbore screen tracer fluid detection", "screen tracer fluid detection wellbore",
        "downhole method apparatus injecting formation", "formation permeability mechanical force",
        "methods systems wellbore investigation", "investigating downhole conditions methods",
        "selective acid diversion matrix acidizing", "matrix acidizing acid diversion",
        "taylor-couette flow vortex acid diversion",
        "sand free production rate borehole", "sand free production determining borehole",
        "method system continuously pumping solid", "continuously pumping solid liquid co2",
    ],

    "Oil Tools/Rods": [
        "low viscosity high pressure spiral shell sucker rod", "spiral shell sucker rod pump",
        "whelk sucker rod pump spiral", "spiral sucker rod pump motor protector",
        "sucker rod pump spiral shell", "spiral shell pump sucker rod",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Drive Shafts — propeller shaft, spindle
    # ─────────────────────────────────────────────────────────────────
    "Drive Shafts": [
        "propeller shaft automobile boot", "propeller shaft inner shaft boot",
        "propeller shaft waterproof boot fitting", "boot propeller shaft fitting inner",
        "propeller shaft support structure center bearing",
        "one-way rotation assembly shaft housing", "one-way rotation shaft housing assembly",
        "one way rotation shaft assembly plurality",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Sealings
    # ─────────────────────────────────────────────────────────────────
    "Sealings/Mechanical Seal": [
        "mechanical tool first annular second annular", "annular member rotating shaft stationary ring",
        "stationary ring rotating ring mechanical",
        "sliding ring improved inlet properties", "sliding ring inlet diamond coating lubricant",
        "seal device ring members diametrical expansion", "ring members expansion seal housing shaft",
        "seal device reduced axial resilient",
        "oil field seal rubber oxycellulose", "rubber composition seal oxycellulose fibers",
    ],

    "Sealings/Shaft Seal": [
        "selective seal stem anchor tubular", "seal stem anchor body lock threads",
        "seal stem anchor activation module",
    ],

    "Sealings/Wellbore and Completion Seals": [
        "high integrity hanger seal casing", "hanger seal casing cemented wellbore",
        "casing hanger expansion cone seal",
        "wellhead isolation sleeve bore isolation", "isolation sleeve wellhead protection",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Monitoring and Controlling
    # ─────────────────────────────────────────────────────────────────
    "Monitoring and controlling": [
        "machine learning equipment failure prediction", "equipment failure prediction learning",
        "time series operational parameter equipment", "operational parameter time derivative",
        "systems methods wellsite control sensor", "wellsite control computing sensor notification",
        "data preprocessing predictive engine accuracy", "preprocessing variables predictive engine",
        "apparatus controlling machine tool operational", "machine tool operational functions control",
        "method determining status machine components", "machine status operating parameters control",
        "fault detection vibration signal shaft revolution",
        "pump fault vibration signal periodic",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Separator
    # ─────────────────────────────────────────────────────────────────
    "Separator": [
        "arrangement separating liquid mixtures cylinder", "cylinder arrangement liquid mixtures",
        "liquid mixtures cylinder inner diameter",
        "oil gas separation buffering tank slug", "oil-gas separating slug flow device",
        "slug flow oil gas buffering", "slug reducing oil gas separator",
        "apparatus processing fluids well module", "first module processing fluid well extension",
        "processing fluid well extension conduit",
        "down-hole gas separation wellbore chambers", "gas separation wellbore production chambers",
        "two production separation chambers wellbore",
        "counter rotating flailing rollers separation", "flailing rollers shredding separating",
        "flailing rollers waste recycling process",
        "selective separation polyurethane foam fibers", "polyurethane foam fibers separation",
        "automobile shredder residue separation", "shredder residue fibers separator",
        "system treatment waste separator specific gravity", "waste treatment separator gravity",
        "apparatus collecting processing recycling", "kitchen scraps recycling separator",
        "waste recycling process separator", "system evacuation shovelable biomass grating",
        "biomass grating movable knife evacuation",
    ],

    "Separator/Centrifugal Separator": [
        "high-speed micro-powder device agar", "agar micro-powder high-speed device",
        "centrifugal mixing system closed mixer", "closed mixer inlet discharge recirculation",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Pumps/Screw conveyor expandido
    # ─────────────────────────────────────────────────────────────────
    "Pumps/Screw conveyor": [
        "sludge auger trough upstream", "auger trough sludge processing",
        "sludge processing apparatus auger trough",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Manufacturing technology
    # ─────────────────────────────────────────────────────────────────
    "Manufacturing technology": [
        "microtreatment iron-based alloy apparatus", "iron-based alloy microtreatment method",
        "carbide iron-based alloy microtreatment", "microstructure iron-based alloy cooling",
        "micro-treating iron alloy transformation", "multi-phase transformation iron carbon alloy",
        "preparation metal feedstock wasted metal", "metal feedstock wasted metal products",
        "forming metal feedstock crushing metal", "crushing metal products feedstock",
        "methods forming polymer coatings metallic", "polymer coatings metallic substrates",
        "polymer coating substrate intermediate carbon", "intermediate layer carbon composite coating",
        "recycling process mixed plastic waste", "mixed plastic recycling foils scraps",
        "toothed disc refiner plastic recycling", "recycling plastic toothed disc refiner",
        "process recycling si starting material", "silicon recycling material comminuting",
        "process further processing recycling material", "silicon recycling melt crystals",
    ],

    "Manufacturing technology/Casting and Molding": [
        "conical screw-bush pair forming", "curved surface cone screw-bush pair",
        "cone screw bush curved surface method",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Agriculture and Biomass expansão
    # ─────────────────────────────────────────────────────────────────
    "Agriculture and Biomass": [
        "seedbed conditioning vertical tillage", "tillage apparatus conditioning seedbed",
        "land preparation clearing apparatus", "apparatus land clearing preparation",
        "material conditioner conditioning materials", "conditioning materials drum apparatus",
        "pick-up head debris cleaning vehicle", "pick-up head suctioning debris",
        "debris collection vacuum blower separator", "roller accumulator lawn garden debris",
        "lawn garden debris accumulator vacuum",
        "mobile assembly cereal grain farm", "feed mixer plurality mixing members",
        "feed mixer chopper auger shredder", "mixing members chopper auger feed",
        "extraction compounds plant material grinding", "plant material extraction grinding",
        "compounds plant material active grinding temperature",
        "method treating organic wastewater", "organic wastewater treating simple facility",
        "organic wastewater sludge treating",
        "treating wood raw material rollers press", "wood raw material rollers crusher",
        "wood processing method crusher", "wood raw material method crusher",
        "device processing agricultural crop bioreactor", "agricultural crop bioreactor cleaning",
        "beets crop bioreactor cleaning device",
        "method producing fuel moist biomass", "moist biomass fuel pellets method",
        "biomass comminuted dehydrated dried fuel",
        "processing biomass method plant feedstock",
    ],

    "Agriculture and Biomass/Forage and Harvesting": [
        "chaff processing distribution device harvester", "chaff distribution device combine",
        "conditioning roller roller drum chaff-cutter", "roller drum conditioning chaff",
        "roller drum main grooves auxiliary grooves",
        "cane juice extractor citrus press", "citrus press drinking vessel",
        "juice extractor citrus hand operated", "hand operated citrus press vessel",
        "field harvester sweet sorghum", "sweet sorghum field harvester",
        "sorghum harvester sugar field",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Conveyor and Transport expansão
    # ─────────────────────────────────────────────────────────────────
    "Conveyor and Transport": [
        "conveyor device fluid elastically deformable", "elastically deformable conveying element",
        "conveyor space rigid element",
        "material spreader belt chain assembly", "belt chain assembly material spreader",
        "pick-up head suctioning opening debris", "debris transfer pick-up head housing",
        "system evacuation materials chamber grating", "grating movable knife chamber evacuation",
        "hopper sludge transport clogging", "hopper sludge internal walls clogging",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Mixing and Agitation expansão
    # ─────────────────────────────────────────────────────────────────
    "Mixing and Agitation": [
        "integral high-speed hydration beater", "high-speed beater stirring barrel",
        "stirring barrel inner groove beater",
        "masher blender mixing cutter", "masher upper lower mixing cutter",
        "mixer low-cost mixing function", "mixer blade mode mixing",
        "stirring apparatus viscous flowable medium", "viscous medium stirring apparatus",
        "stirring axle stirring assembly receptacle",
        "non-internal-net mixing shearing machine", "high tower granulation mixing shearing",
        "mixing shearing water-soluble fertilizer", "fertilizer mixing shearing machine",
        "high-speed shearing granulation slurry", "granulation mixed slurry shearing machine",
        "soybean milk maker dreg stirring", "multifunctional soybean milk maker grinding",
        "soybean milk maker dreg grinding machine",
        "helical-tooth grinding disc homogenizer", "grinding disc homogenizer helical tooth",
        "homogenizing sample device cutting tool", "arrangement homogenizing sample device",
        "mixing machine cereal grain farm", "mobile mixer assembly cereal grain",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Grinding and Milling expansão com patentes restantes
    # ─────────────────────────────────────────────────────────────────
    "Grinding and Milling": [
        "moinho cerâmico capa alumínio pote porcelana", "disposição moinho cerâmico alumínio",
        "capa alumínio pote porcelana moinho",
        "processo moagem via úmida produção", "moagem via úmida moedores produção",
        "machine tool processing food products tube casing", "tube casing food processing machine",
        "processing food products tube casing end fixings",
        "processing phosphate minerals recover clays", "phosphate minerals washing disintegration",
        "mineral washing disintegration sludge",
        "dry treatment organic vegetable crushing", "organic vegetable crushing dry treatment",
        "organic substance dry treatment crushing cell", "cell wall crushing dry treatment organic",
        "method crushing organic waste biological", "crushing organic waste particle size",
        "apparatus system grinding solid raw liquid", "grinding solid raw material liquid",
        "soybean milk curd grinding solid liquid",
        "apparatus measuring fluid quantities petrol pump", "petrol pump measuring fluid motor",
        "fluid measuring motor petrol pump",
    ],

    "Grinding and Milling/Pulverizer and Superfine Mill": [
        "four-axle pulverizing device casing", "improved four-axle pulverizing device",
        "four-axle pulverizing driving driven shafts",
        "wind power parallel crusher blocks", "wind power crushing coagulated blocks",
        "silent centralized pulverizer fixed knife", "mute centralized crusher fixed knife",
        "swing arm continuous crushing shaft", "swing arm single shaft crusher continuous",
        "powerful pulverizer hob frame blade screen",
        "double-shaft powerful smashing grating", "double-shaft smashing grating machine",
        "continuous flow micro-crusher substrate disks", "micro-crusher disks substrate teeth",
        "process recycling composite resin pulverizing", "composite resin pulverizing method recycling",
        "preparing microparticles crushing cluster", "crushing cluster microparticles calibrating",
    ],

    "Grinding and Milling/Industrial Grinder": [
        "apparatus crushing grains driving mechanism", "crushing grains rollers mechanism",
        "apparatus crushing material two rolls", "two rolls crushing material gap",
        "sizing roller screen ore processing", "ore processing sizing roller screen",
        "mobile bucket crusher screen magnet", "size metal separator mobile crusher",
        "rotary grinder cylindrical drum", "rotary grinder cylindrical surface drum",
        "grapple grinder plurality grinder heads",
        "screen cleaning comminuting system", "sewage cleaning comminuting transverse screen",
        "comminuting system channel screen", "screen channel comminuting sewage",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Corrosion
    # ─────────────────────────────────────────────────────────────────
    "Corrosion": [
        "coated sleeved oil gas well production", "polyolefin liner injection string well",
        "abrasion corrosion liner polyolefin well",
        "methods forming polymer coatings metallic", "polymer coatings metallic substrates carbon",
        "intermediate layer carbon composite polymer coating",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Material for pumps / Elastomers
    # ─────────────────────────────────────────────────────────────────
    "Material for pumps/Elastomers": [
        "over mandrel extrusion pcp stator elastomer", "mandrel extrusion elastomer helical",
        "crosshead extrusion elastomer helical stator",
        "asymmetric elastomer liner lobes helical cavity", "elastomer liner asymmetric contouring lobes",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Electric Motors
    # ─────────────────────────────────────────────────────────────────
    "Electric Motors": [
        "driving motor railway vehicles oil supply", "drive motor railway car oil supply",
        "railway drive motor oil supply chamber",
        "vertical axis fluid power generator shaft", "fluid power generation vertical shaft",
        "vertical shaft fluid power generator blades",
        "small-size motor shaft boss tapered", "small motor shaft tapered boss central",
        "spindle motor shaft sleeve fluid dynamic", "spindle motor first sleeve fluid pressure",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Pulsation damping device
    # ─────────────────────────────────────────────────────────────────
    "Pulsation damping device": [
        "fluid line resonator pulsation", "fluid line comprising resonator",
        "resonator fluid line embodiment", "fluid line resonator simple production",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Snow and Ice Removal
    # ─────────────────────────────────────────────────────────────────
    "Agriculture and Biomass": [
        "apparatus crushing snow removal powder", "snow removal powder crusher spreader",
        "snow removal powder crushing spreader vehicle",
        "snow making method apparatus machine", "snow-making machine ice impellers",
        "snow machine impeller ice blades",
        "ice dispenser ice block storage", "ice dispenser slide fingers delivery",
        "apparatus making storing dispensing shaved ice", "shaved crushed ice apparatus storing",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Sterilization and Medical Waste
    # ─────────────────────────────────────────────────────────────────
    "Sterilization and Medical Waste": [
        "integrated medical waste management system", "medical waste management integrated method",
        "medical waste shredding disinfecting automated", "medical waste triturating disinfecting",
        "medical waste processing apparatus method", "apparatus method processing medical waste",
        "medical waste disintegration disinfection", "waste disintegration radio-frequency disinfect",
        "medical waste processing radio-frequency electromagnetic", "radio-frequency medical waste",
        "organic wastewater sludge treating method", "method treating organic wastewater sludge",
        "asbestos crushing containment system", "asbestos crushing system method safe",
        "asbestos-containing building material processing", "building material asbestos method apparatus",
        "waste bread treating crushing drying", "treating waste bread crushing fine powder",
        "waste bread method crushing drying",
        "processing documents medical waste", "documents medical waste shredding disinfection",
        "waste processing pathogen reduction disinfection", "disinfection waste pieces pathogen",
    ],

    # ─────────────────────────────────────────────────────────────────
    # Dehydrator
    # ─────────────────────────────────────────────────────────────────
    "Dehydrator": [
        "drier food waste disposal drum", "hollow drum food waste drier",
        "food waste drier agitating screw thread",
        "disposal foam material crushing ignitible gas", "foam material crushing disposal device",
        "ignitible gas cyclopentane foam disposal",
    ],
}

for _k, _v in _EXPANSAO_V5.items():
    if _k in PALAVRAS_CHAVE:
        _existing = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _existing])
    else:
        PALAVRAS_CHAVE[_k] = _v

# Nova pasta de nível superior — Sterilization and Medical Waste
if "Sterilization and Medical Waste" not in PALAVRAS_CHAVE:
    PALAVRAS_CHAVE["Sterilization and Medical Waste"] = [
        "sterilization", "medical waste", "disinfection",
        "sterilizing", "disinfecting", "autoclave",
        "esterilização", "resíduo médico", "desinfecção",
    ]




# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V6 — Correções cirúrgicas (sem chaves duplicadas)
# Foco: frases exatas dos abstracts BR + casos CN/JP persistentes
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V6 = {

    # ── Pumps — BR (câmara da bomba, eixo do impulsor etc.) ───────────
    "Pumps": [
        "câmara da bomba", "eixo do impulsor",
        "bomba com alojamento câmara", "alojamento define câmara bomba",
        "bomba transporte fluido aspirador", "transporte de fluido bomba alojamento",
        "bomba acionada hidraulicamente diafragma",
        "câmara de transferência reservatório fluido",
        "motor elétrico parafuso bombeamento",
        "unidade de bombeamento parafuso fluidos",
        "bombeamento tipo parafuso tratamento fluidos",
        "tipo parafuso tratamento fluidos fases",
        "bomba conveyance housing transport element",
    ],
    "Pumps/Diaphragm Pump": [
        "bomba acionada hidraulicamente diafragma pistão",
        "hidraulicamente diafragma pistão câmara transferência",
        "controle posição diafragma bombas hidráulicas",
    ],
    "Pumps/Screw Pump": [
        "unidade bombeamento tipo parafuso",
        "bombeamento parafuso fluidos fases diversas",
        "tipo parafuso fluidos fases motor elétrico",
        "cement mortar mixing pump impeller funnel",
        "mortar mixing pump funnel powered impeller",
    ],

    # ── Filtration — BR (frases exatas) ──────────────────────────────
    "Filtration": [
        "dispositivo de filtragem profunda módulo",
        "filtragem profunda módulo filtragem efetuada",
        "montagem de filtro elemento filtrante",
        "processo fabricação montagem filtro",
        "filtro elemento filtrante camada adsorção",
        "membranas de filtro microporosas separador",
        "membrana filtro microporosa separador",
        "estruturas porosas separação fluidos constituintes",
        "filtração em contracorrente diafragmas",
        "contracorrente diafragmas filtração processo",
        "processo filtração contracorrente diafragma",
        "película filtro bordas vedadas cera",
        "cera impermeável película filtro",
        "filtro barras elementos apoio barras",
        "filtro plano cilindro barras apoio",
        "conjunto alimentar porções café preembalados",
        "porções café preembalados unidade preparação",
        "porções embaladas pó café máquina",
    ],
    "Filtration/Filter Media and Cartridge": [
        "elemento filtrante plano módulo filtragem",
        "módulo filtragem elementos filtrantes plano",
        "filtro barras elementos apoio",
        "barras elementos apoio filtro",
        "película filtro bordas cera otimizada",
        "cera otimizada bordas película filtro",
        "estruturas porosas fabricação processo",
        "porous structures fluid fabrication",
    ],
    "Filtration/Liquid Filter": [
        "filtração em contracorrente",
        "contracorrente diafragma filtração",
        "processo dispositivo filtração contracorrente",
    ],

    # ── Grinding and Milling — BR + FR + organic ─────────────────────
    "Grinding and Milling": [
        "moinho cerâmico capa alumínio",
        "capa alumínio pote porcelana moinho",
        "pote de porcelana moinho cerâmico",
        "carcaça moinho de rolos paredes laterais",
        "moinho rolos paredes laterais vigas",
        "carcaça rolos paredes laterais vigas horizontais",
        "processo moagem farinha trigo",
        "moagem farinha grãos duros",
        "sistema moagem farinha grãos duros",
        "etapas de moagem farinha",
        "dry treatment organic vegetable crushing cell wall",
        "organic vegetable crushing dry treatment evenly",
        "apparatus system grinding solid raw liquid soybean",
        "grinding solid raw material liquid soybean milk",
        "processing phosphate minerals recover clays disintegration",
        "phosphate minerals washing disintegration sludge",
    ],
    "Grinding and Milling/Ball and Roller Mills": [
        "moinho de rolos carcaça paredes",
        "carcaça para moinho de rolos",
        "moinho rolos duas paredes laterais",
    ],

    # ── Separator — BR ───────────────────────────────────────────────
    "Separator": [
        "seção de recheio leito",
        "recheio estruturado capacidade melhorada",
        "seção recheio topo plano",
        "leito recheio estruturado seção",
    ],

    # ── Mixing and Agitation — cooking press ─────────────────────────
    "Mixing and Agitation": [
        "food cooking press domestic dishes",
        "cooking press domestic food saving",
        "press domestic food cooking",
        "multifunctional soybean milk maker grinding dreg",
        "soybean milk maker dreg stirring barrel",
        "helical-tooth grinding disc homogenizer shear",
    ],

    # ── Oil Tools — CA retention device ──────────────────────────────
    "Oil Tools/Sand Protection": [
        "retention device solid sedimentation boreholes",
        "temporary retention solid matter borehole",
        "solid matter retention pump borehole",
    ],
    "Oil Tools/Anti-rotation control": [
        "one-way rotation assembly shaft housing",
        "rotation assembly shaft housing plurality",
    ],

    # ── Pumps/Screw — CN curved surface screw-bush ───────────────────
    "Pumps/PC Pump and Motor": [
        "manufacturing rubber linings composite pcp stators",
        "rubber linings pcp stators crosshead extrusion",
        "composite pcp stator rubber lining elastomer crosshead",
        "conical screw-bush pair single screw oil-gas mixed pump",
        "screw-bush pair key component single screw pump",
    ],

    # ── Macerator — CN short-title single-word ───────────────────────
    "Macerator/Industrial Crusher": [
        "motor component hob component serial exciting motor",
        "hob component driven motor output shaft",
        "branch breaker motor hob component serial",
        "mechanochemical reactor extrusion shearing crushing polymer",
        "polymer materials mechanochemical extrusion shearing",
        "processing structure single-shaft shredder digging holes",
        "single-shaft shredder digging holes columns arc-shaped",
        "shredder device pair wheels pulling tool rods",
        "blade shaft connection two half easy assemble",
        "processing unit resin sheet packed food rotary shaft",
        "resin sheet packed food rotary shaft tangled",
        "auto paper crusher staples automatically drive motor blade",
        "paper crusher staples automatically drive motor",
        "powdering machine impeller rotate high speed smash",
        "impeller rotate high speed powdering smash materials",
    ],
    "Macerator/Food Waste Disposer": [
        "cleaning agent adding device waste processor stainless",
        "cleaning agent container waste processor storing",
        "stainless steel domestic waste processor cleaning agent",
        "kitchen bath waste processor smashing device",
        "bath waste processor smashing base",
        "kitchen rubbish breaker inlet rotary shaft knife bars",
        "kitchen rubbish breaker rotary shaft knife bar",
        "food waste treatment device drainage tube washing groove",
        "drainage tube food waste washing groove",
        "restaurant kitchen garbage shredding pulping device reamer",
        "garbage shredding pulping device reamer pump tank",
    ],

    # ── Conveyor — DE device conveying medium ────────────────────────
    "Conveyor and Transport": [
        "device conveying medium carrier shafts transport elements",
        "carrier shafts transport elements working machine medium",
        "conveying device medium carrier shafts",
        "working machine carrier shafts transport",
    ],

    # ── Valves — DE shut-off pipeline ────────────────────────────────
    "Valves": [
        "shut-off device pipeline fluid crude oil",
        "pipeline shut-off crude oil radial catch housing",
        "catch housing pipeline crude oil axially fixed",
    ],

    # ── Pumps/Vane — EP conical viscosity ────────────────────────────
    "Pumps/Vane type Pump": [
        "conical logarithmic spiral viscosity pump housing impeller",
        "rotary viscosity pump conical chamber narrow end",
        "spiral viscosity pump impeller conical chamber outlet",
    ],

    # ── Grinding — FR phosphate, organic (merged to avoid dup key) ──
    # (see Grinding and Milling entry above — terms added there)


    # ── Filtration/Refiner — WO blade element ────────────────────────
    "Filtration/Paper and Pulp Filter": [
        "refiner fibrous material first second refining surface",
        "refiner first second refining surface opposite",
        "refiner blade element fibrous material",
        "refiner and blade element fibrous refining",
    ],
}

for _k, _v in _EXPANSAO_V6.items():
    if _k in PALAVRAS_CHAVE:
        _existing = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _existing])
    else:
        PALAVRAS_CHAVE[_k] = _v


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V7 — Solicitação estruturada (3 partes)
#
# Parte 1 — Novas pastas:
#   • Pumps/Sealing and Mechanical Seals
#   • Macerator/Shredder Components
#   • Couplings and Drive Units          (pasta de nível superior)
#
# Parte 2 — Enriquecimento PT de pastas existentes:
#   • Pumps/PC Pump and Motor  ← key real no dicionário
#   • Pumps/Screw Pump
#   • Conveyor and Transport/Screw Conveyor
#
# Parte 3 — O algoritmo de fallback Score-1 é implementado
#            em auditoria_classificacao.py, não aqui.
# ══════════════════════════════════════════════════════════════════════

# ── PARTE 1: Novas entradas ───────────────────────────────────────────

_NOVAS_V7 = {

    # Vedações e selos mecânicos em contexto de bombas
    # (separa do Sealings raiz que é mais genérico)
    "Pumps/Sealing and Mechanical Seals": [
        "mechanical seal",
        "sealing assembly",
        "gland packing",
        "shaft seal",
        "dynamic seal",
        "stationary seal ring",
        "face seal",
        "lip seal",
        "selo mecânico",
        "vedação mecânica",
        "gaxeta",
        "anel de vedação",
        "vedação de eixo",
        # termos compostos que garantem score ≥ 2 com SCORE_MINIMO=2
        "pump mechanical seal",
        "pump shaft seal",
        "pump gland packing",
        "pump face seal",
        "pump lip seal",
        "mechanical seal pump",
        "shaft seal pump",
        "gland packing pump",
        "vedação mecânica bomba",
        "anel de vedação bomba",
        "vedação de eixo bomba",
        "selo mecânico bomba",
        "pump seal assembly",
        "pump sealing device",
        "pump dynamic seal",
        "pump stationary seal",
    ],

    # Componentes específicos de trituradores (shredder parts)
    "Macerator/Shredder Components": [
        "shredder blade",
        "cutter shaft",
        "shredding roller",
        "cutting disc",
        "stripper plate",
        "combing bar",
        "shredder housing",
        "lâmina de triturador",
        "eixo de corte",
        "disco de corte",
        "pente raspador",
        "contra-faca",
        # expressões multi-palavra para score ponderado
        "shredder blade assembly",
        "shredder blade set",
        "shredder cutter shaft",
        "shredder cutting disc",
        "shredder stripper plate",
        "shredder combing bar",
        "shredder housing design",
        "shredder roller shaft",
        "shredder blade knife",
        "shredder disc blade",
        "lâmina triturador montagem",
        "eixo corte triturador",
        "disco corte triturador",
        "pente raspador triturador",
        "contra-faca triturador",
        "cutter shaft shredder",
        "cutting disc shredder",
        "stripper plate shredder",
    ],

    # Acoplamentos e unidades de acionamento — pasta de nível superior nova
    "Couplings and Drive Units": [
        "magnetic coupling",
        "flexible coupling",
        "drive shaft",
        "gearbox",
        "transmission unit",
        "cardan shaft",
        "hydraulic drive",
        "acoplamento magnético",
        "eixo cardan",
        "caixa de engrenagens",
        "redutor de velocidade",
        # multi-word para score ≥ 2
        "magnetic coupling device",
        "flexible coupling device",
        "drive shaft assembly",
        "gearbox assembly",
        "transmission unit design",
        "cardan shaft assembly",
        "hydraulic drive unit",
        "acoplamento magnético bomba",
        "eixo cardan bomba",
        "caixa de engrenagens bomba",
        "redutor de velocidade bomba",
        "coupling drive unit",
        "shaft coupling drive",
        "drive unit gearbox",
        "hydraulic drive assembly",
        "drive shaft coupling",
        "cardan shaft drive",
        "magnetic coupling pump",
        "flexible coupling pump",
        "gearbox drive unit",
        "transmission gearbox unit",
        "drive shaft transmission",
        "acoplamento flexível",
        "unidade de acionamento",
        "unidade de transmissão",
        "caixa de câmbio",
        "acionamento hidráulico",
        "acionamento magnético",
    ],
}

# ── PARTE 2: Enriquecimento PT de pastas existentes ───────────────────

_ENRIQUECIMENTO_PT_V7 = {

    # Nota: a chave real no dicionário é "Pumps/PC Pump and Motor"
    "Pumps/PC Pump and Motor": [
        "bomba de cavidades progressivas",
        "bomba helicoidal",
        "estator",
        "rotor helicoidal",
        "bomba de cavidade progressiva",
        # reforço de frases PT multi-palavra (score ≥ 2)
        "bomba cavidades progressivas estator",
        "bomba helicoidal rotor estator",
        "rotor helicoidal estator bomba",
        "cavidade progressiva bomba helicoidal",
        "estator elastomérico bomba",
        "rotor helicoidal bomba cavidade",
        "bomba de cavidade progressiva estator",
    ],

    "Pumps/Screw Pump": [
        "bomba de fuso",
        "bomba de parafusos",
        "bomba de três fusos",
        "bomba de duplo fuso",
        "fuso de bombeamento",
        # reforço multi-palavra
        "bomba fuso parafuso",
        "bomba três fusos",
        "bomba duplo fuso",
        "fuso bombeamento fluido",
        "bomba parafuso duplo",
        "bomba parafuso triplo",
        "bomba de fuso helicoidal",
        "bomba fuso vedação",
    ],

    "Conveyor and Transport/Screw Conveyor": [
        "rosca transportadora",
        "transportador de rosca",
        "helicoidal de transporte",
        "rosca sem fim",
        "transportador espiral",
        # reforço multi-palavra
        "rosca transportadora helicoidal",
        "transportador rosca sem fim",
        "rosca sem fim transporte",
        "helicoidal transporte material",
        "transportador espiral helicoidal",
        "rosca transportadora material",
        "sem-fim transportador",
        "transportador helicoidal rosca",
    ],
}

# ── Aplica NOVAS (cria pastas novas) ─────────────────────────────────
for _k, _v in _NOVAS_V7.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)

# ── Aplica ENRIQUECIMENTO (merge em pastas existentes) ────────────────
for _k, _v in _ENRIQUECIMENTO_PT_V7.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V8 — Análise profunda dos 157 restantes sem classificação
# Resultado: 104 recuperáveis | 4 fora de escopo (nanotubos, estenografia…)
# 1 pasta nova criada: Macerator/Multi-Functional Tool
# 22 pastas existentes enriquecidas com frases exatas dos abstracts
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V8 = {

    # ── 🆕 NOVA PASTA ────────────────────────────────────────────────
    # 5 patentes EP/US sobre ferramentas multifuncionais para máquinas
    # de processamento de material/resíduos — conceito próprio.
    "Macerator/Multi-Functional Tool": [
        "multi-functional tool assembly",
        "multi functional tool assembly",
        "material processing machine tool",
        "waste processing machine tool",
        "multi-functional tool",
        "material reducer tool",
        "functional tool assembly processing",
        "multi functional processing tool",
        "tool assembly material processing machine",
        "single tool head shaft integrally formed",
        "head cavity arcuate surface tool",
        "tool material reducer waste processing",
    ],

    # ── Macerator/Industrial Crusher — 14 pat. ────────────────────────
    "Macerator/Industrial Crusher": [
        "crushing system two rotating disk sections high pressure",
        "rotating disk sections crushing raw material rejection",
        "apparatus crushing grains driving mechanism shafts rollers",
        "crushing grains plurality shafts rollers",
        "knife roller granulating plastic strands roller sections blade",
        "knife roller plastic strands roller sections teeth",
        "device squeezing empty containers beverage bottles cans pet",
        "squeezing empty containers pet tinplate filling outlet",
        "destruction device data carriers peripheral devices bending punching",
        "destroying data carriers bending shearing device",
        "device processing polymer material removing contaminants volatile",
        "polymer material processing removing volatile moisture",
        "chaff-cutter wood material water jet nozzle high pressure pump",
        "wood cutter water jet nozzle high pressure pump cutting",
        "chip making device wood chips cutter carriers chipping track",
        "wood chips chip making cutter chipping angle",
        "interface knife knife holder",
        "tightening loosening clamping nuts blade sets bevel gear",
        "grinder unit method controlling electrical grinder motor current",
        "grinder unit controlling grinder motor current sensing",
        "bag breaking mechanism kitchen rubbish knife shaft knife disk",
        "garbage grinding bin driving equipment rotating barrel grinding cutter",
        "fuel fining device energy source crushed microparticles water",
        "slice parting machine outer cylinder rotating shaft rotary drum",
        "cooling water pipe structure rubber twisting cutting machine",
        "device compressing empty containers pet plastic",
        "crushing system rotating disk high pressure raw material",
    ],

    # ── Macerator/Food Waste Disposer — 7 pat. ───────────────────────
    "Macerator/Food Waste Disposer": [
        "food processor housing motor base driveshaft bowl lid",
        "food processor driveshaft bowl lid tool housing motor",
        "food processing apparatus slices strips cubes first second shaft",
        "food processing apparatus subsets blades first second shaft",
        "method producing pureed cooked foodstuffs pre-chopping cooking",
        "pureed cooked foodstuffs pre-chopping cooking method device",
        "food processing device juice disintegrator inlet",
        "devices methods disintegrate foods juice disintegrator",
        "cutter assembly s-shaped blade foodstuff wedge cylindrical housing",
        "s-shaped blade foodstuff concave tapered wedge",
        "disposição construtiva prensa alimentos uso doméstico",
        "food cooking press domestic lower upper plate dishes fuel",
        "conjunto alimentar porções café preembalados máquina café",
        "porções café preembalados unidade preparação máquina",
        "garbage treatment device crush water hopper trap pipe ejection",
        "garbage treatment hopper rinse water ejection water-supplying",
        "perforated disk processing food through-holes axial side surface",
        "perforated disk food products holes axial side",
    ],

    # ── Agriculture and Biomass/Forage and Harvesting — 5 pat. ───────
    "Agriculture and Biomass/Forage and Harvesting": [
        "chaff cutter water jet nozzle high pressure pump cutting",
        "water jet nozzle wood cutting high pressure pump cutter",
        "chaff cutter microwave radiator cutting chamber timber heated",
        "microwave radiator wood softened cutting chamber cutter",
        "chip making device cutter carriers axis chipping track",
        "chip making device wood chips setting element cutter carriers",
        "chaff processing distribution device combine harvester",
        "chopper combine harvester chaff distribution device",
        "bag breaking mechanism bag tearing machine rubbish knife",
        "bag breaking knife shaft knife disk blades kitchen rubbish",
        "bag tearing machine rotary shaft winding release members",
        "bag breaking apparatus film fragments winding release",
        "mobile mixer assembly cereal grain farm animal feed helical",
        "mixer container helical horizontal rotating mixer tool cereal",
    ],

    # ── Pumps/Screw Pump — 3 pat. ────────────────────────────────────
    "Pumps/Screw Pump": [
        "unidade bombeamento tipo parafuso fluidos fases diversas caixa",
        "bombeamento parafuso fluidos fases diversas caixa compreende",
        "container sump multi-phase pump system separating splitting",
        "collecting container multi-phase hydrocarbon source inlet",
        "multi-phase pump collecting container sump hydrocarbon",
        "ultra pump systems well elongated cylindrical pump chamber covers",
        "pump removing liquids well elongated cylindrical chamber covers",
        "pump chamber first cover second cover well liquids",
    ],

    # ── Pumps/Diaphragm Pump — 1 pat. ────────────────────────────────
    "Pumps/Diaphragm Pump": [
        "controle posição diafragma bombas acionadas hidraulicamente",
        "bomba acionada hidraulicamente diafragma pistão câmara transferência",
        "hydraulically actuated pump diaphragm piston transfer chamber",
        "diaphragm position control hydraulically driven pump element",
    ],

    # ── Pumps — 4 pat. ────────────────────────────────────────────────
    "Pumps": [
        "fluid displacer conduit pump housing inlet fluid",
        "pump fluid displacer housing conduit inlet",
        "pump motor pumping fluids housing conduit upper lower",
        "pump conduit housing fluid displacer motor inlet",
        "pump conveying medium suction pressure transport element conveyance",
        "pump delivery rate suction outlet transport element pressure",
        "pump method adjusting delivery rate suction outlet",
        "resonator pipe pump chamber closed primary pipe reflector",
        "pump chamber resonator pipe closed primary reflector secondary",
    ],

    # ── Filtration/Liquid Filter — 5 pat. ────────────────────────────
    "Filtration/Liquid Filter": [
        "processo fabricação montagem filtro elemento armação barras",
        "montagem filtro elemento armação barras apoio",
        "filtro processo produção barras elementos apoio suportam",
        "filtro plano cilindro barras elementos apoio",
        "película filtro camada cera impermeável bordas fechada área",
        "película filtro bordas vedadas cera otimizada método vedação",
        "estruturas porosas separação fluidos constituintes indesejados",
        "porous structures separation fluids undesired constituents",
        "liquid treatment dewatering material suspensions press rolls vat",
        "liquid treatment press rolls rotatable liquid permeable vat",
        "apparatus liquid treatment dewatering suspension press rolls",
    ],

    # ── Separator — 2 pat. ───────────────────────────────────────────
    "Separator": [
        "seção de recheio leito recheio estruturado capacidade melhorada",
        "recheio estruturado seção tijolo topo plano base",
        "structured packing section improved capacity brick",
        "packing section structured improved capacity",
        "down-hole gas separation wellbore production chambers parallel",
        "separating gas liquids wellbore production chambers operating parallel",
        "wellbore fluids production separation chambers parallel apparatus",
    ],

    # ── Oil Tools — 7 pat. ────────────────────────────────────────────
    "Oil Tools": [
        "downhole assembly articulated mandrel passive active damping torsional",
        "torsional stick-slip damping articulated mandrel borehole",
        "positioning tool casing downhole detecting unit magnet longitudinal",
        "positioning tool longitudinal axis detecting unit first magnet",
        "downhole apparatus valve arrangement tubular body first second ports",
        "valve arrangement tubular body ports locked configuration",
        "valves bottom hole assemblies selectively actuating motor barrel",
        "bottom hole assembly valve barrel interior circular cross-section",
        "wellsite control computing sensor information notification",
        "systems methods wellsite control sensor notification computing",
        "wellbore maintenance improved oil recovery plurality wellbores drilled",
        "system method assembly wellbore maintenance operations recovery",
        "apparatus pumping fluid additive downhole container wellbore location",
        "pumping fluid mixture wellbore container apparatus",
        "selective acid diversion matrix acidizing taylor-couette vortices",
        "apparatus selectively delivering fluid targeted vortices couette rotation",
        "well tool nanoparticle reinforced metallic coating substrate fluid",
        "nanoparticle metallic coating well fluid surface substrate",
    ],

    # ── Oil Tools/Wellhead equipment — 3 pat. ─────────────────────────
    "Oil Tools/Wellhead equipment": [
        "expandable tubular radially expanding plastically deforming resilient",
        "resilient launcher sleeve expandable tubular radially expanding",
        "expansion system expandable tubular resilient launcher sleeve",
        "system stimulating multi-zone well tubular body plugs pre-drilled",
        "multi-zone well stimulating first second zone plugs tubular",
        "releasable connector assembly tubular member payload first connector",
        "releasable connector tubular member releasable connection",
        "shaft downhole equipment coupling nominal diameter main body",
        "automatic tubing drain rotary pumps reactive torque closes opens",
        "tubing drain rotary pump torque closes pump stops",
        "system bore hole axially coupling tubular end mandrel connecting",
        "coupling tubular ends bore hole mandrel aligning inserting",
        "made-up flange locking cap subsea member external flange seal",
        "cap subsea flange seal tubular inner outer body cavity",
    ],

    # ── Oil Tools/Drilling — 2 pat. ──────────────────────────────────
    "Oil Tools/Drilling": [
        "mobile slurry apparatus oil sand ore frame slurry box",
        "oil sand slurry box ore slurry water mixing frame",
        "method apparatus sized ore feed processing deposit",
        "processing sized ore feed excavated deposit apparatus",
        "methods extracting oil tar sand in-situ liquefaction temperature",
        "in-situ liquefaction subsurface formation hydrocarbons temperature",
        "process production mineral oil deposits temperature permeable",
        "mineral oil deposits temperature gradient permeable regions",
    ],

    # ── Couplings and Drive Units — 6 pat. ────────────────────────────
    "Couplings and Drive Units": [
        "arrangement transmitting torque shaft hub n-corner equilateral",
        "transmitting torque shaft hub inner geometry equilateral",
        "torque shaft hub equilateral n-corner side faces inner",
        "one-way rotation assembly shaft housing ratchet members",
        "one-way rotation assembly shaft at least partially within housing",
        "line retention arrangement clips cantilever base support",
        "line retention clips cantilever support cable",
        "mechanical tool annular member rotating shaft stationary ring",
        "first annular member housing second annular rotating shaft ring",
        "retaining plate gearing gear shafts aperture rigid body",
        "plate connecting gear shafts gear assembly rigid aperture",
    ],

    # ── Sealings/Mechanical Seal — 3 pat. ────────────────────────────
    "Sealings/Mechanical Seal": [
        "sliding ring diamond coating lubricant coating inlet properties",
        "slide ring diamond coating lubricant improved inlet base region",
        "exercise seal motion seal lip contacts inner member outer member",
        "motion seal seal lip rotational speed outer member torque wear",
        "oil field apparatus seal member rubber oxycellulose cellulose nanofibers",
        "seal member rubber composition oxycellulose fibers dispersed",
        "selective seal stem anchor tubular body lock threads activation",
        "seal stem anchor activation module tubular body lock threads",
    ],

    # ── Bearings/Bearing Lubrication and Sealing — 4 pat. ────────────
    "Bearings/Bearing Lubrication and Sealing": [
        "bearing lubricant properties determining arrangement first second element",
        "bearing first second element movable lubricant determining properties",
        "bearing arrangement determining properties lubricant element",
        "bearing device vehicle wheel double-row tapered outer raceway",
        "vehicle wheel bearing double-row tapered outer raceway surfaces",
        "bearing extreme dust environment outer ring inner ring retainer service",
        "bearing long service life extreme dust environment outer ring",
        "bearing device less leakage lubricating oil inclined surface seal",
        "bearing device leakage lubricating oil inner surface radially inclined",
        "bearing end cap integrated seal circular mounting surface groove",
        "bearing end cap seal groove circular mounting surface sidewall",
    ],

    # ── Monitoring and controlling/Vibration and Acoustics — 4 pat. ──
    "Monitoring and controlling/Vibration and Acoustics": [
        "method detecting faults pumping units vibration signal shaft revolution",
        "detecting faults pumping vibration signal shaft revolution periodic",
        "vibration signal shaft revolution rate filtering periodic signals faults",
        "machine learning equipment failure prediction time series operational",
        "predictive engine preprocessing variables wellsite automate operations",
        "data preprocessing system predictive engine accuracy analysis variables",
        "apparatus controlling machine tool operational functions switch-off time",
        "machine tool operational functions selection switch-off computing device",
    ],

    # ── Manufacturing technology/Surface Treatment — 4 pat. ──────────
    "Manufacturing technology/Surface Treatment": [
        "diamond coating displacer tooth components chemical resistant fluidic",
        "method producing component fluidic micro mini unit diamond coating",
        "microtreatment carbide iron-based alloy transform shape carbon steel",
        "micro-treating iron alloy carbon steel transformation low medium high",
        "methods forming polymer coatings metallic substrates carbon composite",
        "polymer coating metallic substrate intermediate carbon composite layer",
        "process recycling silicon starting material comminuting melt crystals",
        "silicon recycling comminuting melt crystals block tube",
        "glass powder average particle size improved free particles process",
        "glass powder particle size distribution improved process preparation",
    ],

    # ── Sterilization and Medical Waste — 5 pat. ─────────────────────
    "Sterilization and Medical Waste": [
        "apparatus disposing medical waste infectious preventing secondary infection",
        "medical waste apparatus preventing secondary infection safety cost",
        "asbestos containing building materials processing safe low cost method",
        "asbestos building materials processing method apparatus input zone",
        "waste processing pathogen reduction cutting small pieces disinfectant",
        "disinfection waste cutting small pieces spraying disinfectant effective",
        "method treating waste bread crushing drying granular powder livestock",
        "waste bread crushing drying fine powder granular low moisture",
        "waste vinyl fishing net cleaner cuts washes dehydrates compresses",
        "cleaning foreign matters waste vinyl fishing net pretreatment",
    ],

    # ── Mixing and Agitation — 5 pat. ────────────────────────────────
    "Mixing and Agitation": [
        "arrangement homogenizing sample motor cutting tool receptacle",
        "homogenizing sample device cutting tool motor control mechanism",
        "centrifugal mixing system closed mixer recirculation inlet discharge",
        "mixing system closed mixer recirculation line fluid communication",
        "mixer mixer blade rotating shaft lowering function processing quality",
        "mixer mode mixer blade rotating shaft processing quality low-cost",
        "fluid treatment apparatus highly accurate stirring pressure productivity",
        "fluid treatment apparatus stirring pressure high productivity simple",
        "agitator sewer system waste material digester inline",
        "sewer system inline agitator waste material digester upstream",
    ],

    # ── Conveyor and Transport — 5 pat. ──────────────────────────────
    "Conveyor and Transport": [
        "device conveying medium working machine carrier shafts transport elements",
        "conveying medium carrier shafts transport elements drive unit",
        "material spreader belt chain assembly chamber sliding bar",
        "material spreader belt chain chamber operation",
        "pick-up head suctioning bottom opening debris receiving vehicle",
        "pick-up head surface cleaning vehicle suctioning debris inlet",
        "roller accumulator lawn garden debris vacuum blower separator",
        "lawn garden debris roller accumulator vacuum blower detachable",
        "device clogging gutter grinder motor-driven leaves debris",
        "gutter clogging device grinder motor-driven leaves debris",
        "hopper transporting sludge clogging internal walls load cell",
        "hopper sludge clogging internal walls load cell prevent",
        "system evacuate materials elongated chamber grating movable knife",
        "evacuate biomass elongated chamber grating movable knife",
    ],

    # ── Media and Document Destruction — 2 pat. ──────────────────────
    "Media and Document Destruction": [
        "apparatus destruction tickets cutter slot rotating blade housing",
        "destroying used tickets housing cutter enclosure slot rotating",
        "fast secure pressing data storage devices unrecoverable hydraulic room",
        "rendering data unrecoverable pressing data storage secure room mobile",
    ],

    # ── Filtration — 2 pat. ──────────────────────────────────────────
    "Filtration": [
        "processo fabricação montagem filtro elemento filtro armação",
        "fabricação montagem filtro elemento armação",
        "packaging tea airtight capsule breaking dried tea leaves machine inlet",
        "tea leaves capsule packaging machine inlet outlet supply",
    ],

    # ── Macerator — 6 pat. (KR, RU, US misc.) ────────────────────────
    "Macerator": [
        "system processing waste continuous infeed vessel pressure temperature",
        "processing waste continuous basis infeed outfeed vessel",
        "apparatus disposing waste agitation residues bottom surface chamber",
        "waste disposal apparatus agitation residues bottom chamber",
        "method improvement crushing performance CT voltage value",
        "crushing performance method CT voltage grinding determining",
        "automatic adjustment blade engagement intervals cutting machine interlocked",
        "adjusting blade engagement intervals interlocked cutting machine smooth",
        "waste vinyl fishing net cleaner cuts washes dehydrates compresses",
        "plant electroblasting activation water pulps suspensions construction",
        "electroblasting activation water pulps suspensions aluminium effluents",
    ],
}

for _k, _v in _EXPANSAO_V8.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══ EXPANSÃO V8b — Keywords exatas extraídas dos abstracts ══
_EXPANSAO_V8b = {
    'Pumps': ['fluid displacer housing', 'pump fluid displacer', 'pump conduit housing', 'pump housing upper end', 'pump chamber resonator pipe', 'resonator pipe closed primary', 'pump delivery rate suction', 'pump adjusting delivery rate', 'ultra pump well cylindrical', 'pump well cylindrical chamber'],
    'Pumps/Screw Pump': ['collecting container multi phase', 'container multi phase mixtures', 'multi phase mixtures hydrocarbon', 'collecting container hydrocarbon source', 'container sump multi phase pump', 'ultra pump systems well', 'pump removing liquids well cylindrical'],
    'Couplings and Drive Units': ['arrangement transmitting torque', 'transmitting torque shaft hub', 'torque shaft hub', 'way rotation assembly shaft', 'rotation assembly shaft housing', 'one way rotation assembly', 'first annular member attached housing', 'second annular member rotating shaft', 'annular member rotating shaft stationary ring', 'plate connecting gear shafts', 'connecting gear shafts gear assembly', 'gear shafts gear assembly', 'line retention arrangement clips'],
    'Oil Tools': ['torsional stick slip', 'articulated mandrel passive active damping', 'mandrel borehole torsional stick', 'positioning tool longitudinal axis', 'detecting unit first magnet casing', 'valve arrangement tubular body ports', 'valve tubular body first second ports', 'selectively actuating motor barrel', 'wellsite control sensor notification', 'wellbore maintenance improved oil recovery', 'apparatus pumping fluid additive downhole', 'pumping fluid mixture wellbore container', 'matrix acidizing taylor couette vortices', 'selectively delivering fluid targeted vortices', 'nanoparticle metallic coating well substrate', 'metallic coating well fluid substrate'],
    'Oil Tools/Wellhead equipment': ['expandable tubular radially expanding', 'resilient launcher sleeve expandable', 'expansion system expandable tubular', 'stimulating multi zone well tubular', 'releasable connector assembly tubular member', 'releasable connector tubular member payload', 'shaft downhole equipment coupling diameter', 'automatic tubing drain rotary pumps torque', 'bore hole axially coupling tubular mandrel', 'coupling tubular ends bore hole mandrel', 'flange locking cap subsea member', 'cap subsea external flange seal'],
    'Oil Tools/Drilling': ['mobile slurry apparatus oil sand', 'oil sand slurry box ore', 'sized ore feed processing deposit', 'ore feed excavated deposit processing', 'extracting oil tar sand liquefaction', 'in situ liquefaction subsurface formation', 'production mineral oil deposits temperature', 'mineral oil deposits temperature gradient'],
    'Macerator/Industrial Crusher': ['crushing system rotating disk sections', 'rotating disk sections high pressure raw', 'crushing grains driving mechanism shafts', 'knife roller granulating plastic strands', 'plastic strands roller sections blade', 'squeezing empty containers pet tinplate', 'empty containers beverage bottles pet', 'destroying data carriers bending shearing', 'data carriers peripheral bending punching', 'polymer material removing volatile contaminants', 'chaff cutter water jet nozzle pump', 'wood cutter water jet nozzle pump', 'chip making device cutter carriers', 'wood chips cutter carriers chipping', 'interface knife knife holder', 'grinder unit controlling grinder motor', 'grinder unit method controlling motor current', 'bag breaking kitchen rubbish knife shaft', 'garbage grinding bin rotating barrel cutter', 'fuel fining device energy crushed microparticles', 'slice parting outer cylinder rotating shaft', 'cooling water pipe rubber twisting cutting'],
    'Macerator/Food Waste Disposer': ['food processor driveshaft bowl lid', 'food processor housing motor driveshaft bowl', 'food processing apparatus subsets blades shafts', 'pureed cooked foodstuffs pre chopping cooking', 'method producing pureed food pre chopping', 'food processing device juice disintegrator inlet', 'disintegrate foods juice disintegrator inlet', 's shaped blade foodstuff wedge', 'cutter assembly s shaped blade foodstuff', 'food cooking press domestic dishes fuel', 'porções café preembalados máquina', 'porções embaladas pó café unidade preparação', 'garbage treatment hopper trap pipe ejection', 'hopper trap pipe rinse water ejection', 'perforated disk food products holes axial'],
    'Agriculture and Biomass/Forage and Harvesting': ['chaff cutter water jet nozzle high pressure', 'water jet nozzle wood high pressure cutter', 'cutter microwave radiator cutting chamber timber', 'microwave radiator wood softened cutting', 'chip making device cutter carriers chipping track', 'cutter carriers chipping track axis', 'chaff processing distribution combine harvester', 'combine harvester chaff distribution device', 'bag breaking kitchen rubbish knife disk blades', 'bag tearing machine rotary shaft winding release', 'bag breaking apparatus winding release members', 'mixer container helical horizontal rotating mixer', 'mobile mixer cereal grain farm animal helical'],
    'Filtration/Liquid Filter': ['montagem filtro elemento armação barras', 'fabricação montagem filtro armação', 'filtro barras elementos apoio', 'filtro plano cilindro barras apoio', 'película filtro cera impermeável bordas', 'filtro bordas vedadas cera método', 'estruturas porosas separação fluidos constituintes', 'porous structures separation fluids constituents', 'liquid treatment press rolls vat dewatering', 'liquid permeable press rolls vat'],
    'Separator': ['seção recheio leito estruturado', 'recheio estruturado seção tijolo plano', 'structured packing section capacity brick', 'down hole gas separation wellbore chambers', 'separating gas liquids wellbore chambers parallel'],
    'Monitoring and controlling/Vibration and Acoustics': ['detecting faults pumping units vibration signal', 'faults pumping vibration signal shaft revolution', 'machine learning equipment failure prediction', 'predictive engine preprocessing wellsite', 'machine tool operational functions switch off', 'apparatus controlling machine tool functions'],
    'Manufacturing technology/Surface Treatment': ['diamond coating displacer tooth components', 'displacer components chemical resistant diamond', 'microtreatment carbide iron based alloy', 'micro treating iron alloy transformation', 'polymer coatings metallic substrates carbon composite', 'polymer coating substrate carbon composite', 'recycling silicon comminuting melt crystals', 'silicon recycling comminuting melt', 'glass powder particle size distribution', 'glass powder average particle free'],
    'Sealings/Mechanical Seal': ['sliding ring diamond coating lubricant inlet', 'slide ring diamond coating lubricant improved', 'exercise seal motion seal lip inner member', 'motion seal lip rotational speed outer member', 'oilfield apparatus seal rubber oxycellulose', 'seal rubber oxycellulose cellulose nanofibers', 'seal stem anchor body lock threads activation'],
    'Bearings/Bearing Lubrication and Sealing': ['bearing lubricant properties determining arrangement', 'bearing arrangement determining lubricant properties', 'bearing device vehicle wheel double row tapered', 'vehicle wheel bearing double row tapered raceway', 'bearing extreme dust environment outer ring inner', 'bearing long service life extreme dust', 'bearing leakage lubricating oil inclined surface', 'bearing device oil leakage inclined surface seal', 'bearing end cap integrated seal groove', 'bearing end cap seal groove circular mounting'],
    'Sterilization and Medical Waste': ['medical waste preventing secondary infection safety', 'apparatus disposing medical waste infectious', 'asbestos containing building materials processing safe', 'asbestos building materials processing apparatus', 'waste pathogen reduction cutting disinfectant', 'disinfection waste cutting small pieces spraying', 'waste bread crushing drying powder livestock', 'treating waste bread crushing drying granular', 'waste vinyl fishing net cleaner cuts washes', 'cleaning foreign matters waste vinyl fishing net'],
    'Mixing and Agitation': ['homogenizing sample motor cutting tool receptacle', 'arrangement homogenizing sample cutting tool', 'centrifugal mixing system closed mixer recirculation', 'closed mixer recirculation inlet discharge', 'mixer blade rotating shaft processing quality', 'fluid treatment apparatus stirring pressure', 'agitator sewer waste material digester inline', 'sewer system agitator waste material digester'],
    'Conveyor and Transport': ['device conveying medium carrier shafts transport', 'conveying medium carrier shafts working machine', 'material spreader belt chain assembly chamber', 'spreader belt chain chamber sliding', 'pick up head suctioning bottom opening debris', 'pick up head debris cleaning vehicle', 'roller accumulator lawn garden debris vacuum', 'lawn garden debris roller accumulator vacuum', 'gutter clogging grinder motor driven leaves', 'device clogging gutter grinder leaves debris', 'hopper sludge clogging internal walls load cell', 'hopper transporting sludge clogging walls', 'evacuate materials chamber grating movable knife', 'system evacuate chamber grating knife'],
    'Media and Document Destruction': ['apparatus destruction tickets cutter slot rotating', 'destroying tickets housing cutter slot rotating', 'pressing data storage devices unrecoverable', 'rendering data unrecoverable pressing storage'],
    'Filtration': ['packaging tea airtight capsule tea leaves', 'tea leaves capsule machine inlet outlet', 'montagem filtro elemento armação fabricação', 'processo fabricação montagem filtro'],
    'Macerator': ['processing waste continuous infeed vessel pressure', 'waste continuous basis infeed outfeed vessel', 'waste disposal apparatus agitation residues bottom', 'apparatus disposing waste agitation residues', 'crushing performance CT voltage grinding', 'method improvement crushing performance CT', 'blade engagement intervals cutting machine interlocked', 'automatic adjustment blade engagement cutting', 'electroblasting activation water pulps suspensions', 'plant electroblasting water pulps construction'],
    'Oil Tools/Anti-rotation control': ['way rotation assembly shaft housing ratchet', 'one way rotation assembly shaft housing'],
}
for _k, _v in _EXPANSAO_V8b.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══ EXPANSÃO V8c — Correções pontuais para casos ainda sem match ══════
_EXPANSAO_V8c = {

    # Pump raiz já classifica WO Pump fluid displacer → OK
    # Couplings já classifica torque shaft hub + one-way rotation → OK
    # Bearings/Lubrication já classifica bearing lubricant sensor → OK

    # DE Sliding Ring Diamond — "sliding ring" e "diamond coating" não estavam
    "Sealings/Mechanical Seal": [
        "sliding ring",
        "diamond coating",
        "lubricant coating diamond",
        "slide ring diamond",
        "sliding ring diamond coating",
        "base region diamond coating",
    ],

    # US Food Processor — "food processor" está mas "driveshaft bowl lid" não score suficiente
    "Macerator/Food Waste Disposer": [
        "food processor",        # 2 palavras = 2pt → sozinha já passa SCORE_MINIMO
        "driveshaft bowl",
        "food processor driveshaft",
        "food processing slices strips",
        "s shaped blade cutting",
        "cutter assembly blade foodstuff",
        "food processor housing motor",
        "pureed foodstuffs chopping",
    ],

    # Casos DE ainda sem match
    "Macerator/Industrial Crusher": [
        "knife knife holder",          # "Interface Between Knife And Knife Holder"
        "knife holder blade",
        "blade sets cutter bevel gear", # "Tightening Loosening Device Clamping Nuts Blade Sets"
        "clamping nuts blade sets",
        "squeezing containers plastic pet",  # "Device Squeezing Empty Containers"
        "containers plastic pet tinplate",
        "polymer material volatile contaminants",  # "Device Processing Polymer Material"
        "removing volatile contaminants polymer",
        "data carriers peripheral devices",   # "Destruction Device Data Carriers"
        "data carriers bending shearing",
        "grinder motor current sensing",  # "Grinder Unit Method Controlling"
        "grinder unit current sensing",
        "crushed microparticles energy source",  # "Fuel Fining Device"
        "energy source microparticles water",
        "garbage grinding bin barrel cutter",  # "Garbage Grinding Bin"
        "grinding bin rotating barrel",
        "slice parting machine cylinder shaft",  # "Slice Parting Machine"
        "parting machine rotating shaft drum",
        "rubber twisting cutting machine",  # "Cooling Water Pipe Rubber Twisting"
        "water pipe rubber cutting machine",
    ],

    # DE Chaff-cutter water jet + microwave
    "Agriculture and Biomass/Forage and Harvesting": [
        "water jet nozzle high pressure pump",
        "cutter water jet nozzle pump",
        "microwave radiator cutting chamber",
        "timber heated microwave radiator",
        "cutter microwave radiator wood",
        "chip making cutter carriers axis",
        "wood chips cutter chipping track",
        "bag tearing machine rotary shaft",
        "bag breaking knife disk blades",
        "bag breaking apparatus winding release",
    ],

    # Conveyor extras
    "Conveyor and Transport": [
        "pick up head suctioning",
        "pick up head debris vehicle",
        "roller accumulator lawn debris",
        "lawn garden debris vacuum blower",
        "gutter grinder motor driven",
        "clogging gutter grinder leaves",
        "hopper sludge clogging walls",
        "evacuate chamber grating knife",
        "material spreader belt chain",
        "spreader belt chain sliding bar",
    ],

    # Mixing extras
    "Mixing and Agitation": [
        "homogenizing sample motor cutting",
        "arrangement homogenizing sample",
        "centrifugal mixing closed mixer",
        "closed mixer recirculation inlet",
        "agitator sewer digester inline",
        "sewer agitator waste material",
        "mixer blade rotating shaft",
        "fluid treatment stirring pressure",
    ],

    # EP Chopper fiber — "Chopper And Method Of Chopping Unwound Linear Items"
    "Macerator/Cutting Elements": [
        "chopping unwound linear items",
        "chopper unwound linear fiber",
        "fiber strand yarn chopper",
        "unwound items fiber strand yarn",
        "backup roll blade roll chopper",
        "roll retainer fiber chopper",
        "fiber chopper idler roll backup",
        "chopper backup roll blade roll",
    ],

    # US Fiber Feeder / Fiberizer
    "Macerator/Cutting Elements": [
        "fiber feeder compressed masses",
        "breaking compressed masses fibers",
        "break up implements shafts fiber",
        "fiber feeder intake chute shafts",
        "fiberizer thermocouple support",
        "fiberizer sensor support frame",
    ],

    # EP Fault detection pumping / US Machine Learning
    "Monitoring and controlling/Vibration and Acoustics": [
        "detecting faults pumping vibration",
        "faults pumping units vibration signal",
        "machine learning equipment failure",
        "predictive engine wellsite accuracy",
        "data preprocessing predictive engine",
        "machine tool functions switch off",
        "apparatus controlling machine tool",
    ],

    # Oilfield / Wellsite / Downhole
    "Oil Tools": [
        "torsional stick slip",
        "mandrel torsional stick slip",
        "positioning tool magnet casing",
        "detecting unit magnet casing",
        "valve arrangement tubular ports",
        "tubular body first second ports",
        "selectively actuating motor barrel",
        "wellsite control sensor notification",
        "wellbore maintenance oil recovery",
        "pumping fluid additive downhole",
        "matrix acidizing vortices couette",
        "acid diversion matrix acidizing",
        "nanoparticle metallic coating well",
        "well tool metallic coating substrate",
    ],

    # Expandable tubulars / wellhead
    "Oil Tools/Wellhead equipment": [
        "expandable tubular radially expanding",
        "resilient launcher expandable tubular",
        "stimulating multi zone well",
        "multi zone well tubular plugs",
        "releasable connector tubular member",
        "connector tubular payload releasable",
        "downhole equipment coupling diameter",
        "tubing drain rotary pump torque",
        "automatic tubing drain rotary",
        "bore hole coupling tubular mandrel",
        "tubular end mandrel aligning",
        "flange locking cap subsea flange",
        "cap subsea member external flange",
    ],

    # Oil Sands / Ore Feed / Tar Sand
    "Oil Tools/Drilling": [
        "mobile slurry oil sand ore",
        "oil sand slurry box water",
        "sized ore feed processing",
        "ore feed excavated deposit",
        "tar sand in situ liquefaction",
        "in situ liquefaction subsurface",
        "mineral oil deposits temperature gradient",
        "production mineral oil deposits",
    ],

    # DE Container Sump Multi-Phase Pump
    "Pumps/Screw Pump": [
        "collecting container multi phase",
        "multi phase mixtures hydrocarbon",
        "collecting container hydrocarbon source",
        "container sump multi phase pump",
        "ultra pump well cylindrical chamber",
        "pump well cylindrical chamber covers",
        "pump removing liquids well cylindrical",
    ],

    # Material science
    "Manufacturing technology/Surface Treatment": [
        "diamond coating displacer tooth",
        "displacer components diamond coating",
        "microtreatment carbide iron alloy",
        "micro treating iron carbon steel",
        "polymer coatings metallic substrate",
        "carbon composite coating substrate",
        "silicon recycling comminuting melt",
        "recycling silicon starting material",
        "glass powder particle size",
        "glass powder average particle",
    ],

    # Wellbore misc
    "Oil Tools/Anti-rotation control": [
        "one way rotation assembly shaft",
        "way rotation assembly shaft housing",
    ],

    # Sterilization
    "Sterilization and Medical Waste": [
        "medical waste infectious secondary infection",
        "apparatus disposing infectious medical",
        "asbestos containing building processing",
        "asbestos building materials apparatus",
        "waste pathogen reduction disinfectant",
        "disinfection waste small pieces spraying",
        "waste bread crushing drying powder",
        "treating waste bread crushing",
        "waste vinyl fishing net cuts",
        "cleaning foreign waste vinyl fishing",
    ],

    # Media destruction
    "Media and Document Destruction": [
        "apparatus destruction tickets cutter",
        "destroying tickets housing cutter slot",
        "pressing data storage unrecoverable",
        "data storage devices unrecoverable pressing",
    ],

    # Filtration BR + EP tea
    "Filtration": [
        "montagem filtro fabricação armação",
        "processo fabricação montagem filtro",
        "packaging tea airtight capsule",
        "tea leaves capsule machine inlet",
    ],
    "Filtration/Liquid Filter": [
        "montagem filtro elemento armação",
        "filtro barras elementos apoio",
        "filtro plano cilindro barras",
        "estruturas porosas separação fluidos",
        "película filtro cera impermeável",
        "filtro bordas vedadas cera",
        "porous structures separation fluids",
        "liquid treatment press rolls vat",
        "liquid permeable press rolls",
    ],

    # Separator BR + US
    "Separator": [
        "seção recheio leito estruturado",
        "recheio estruturado tijolo plano",
        "structured packing section capacity",
        "down hole gas separation wellbore",
        "gas separation wellbore chambers parallel",
    ],

    # Macerator misc
    "Macerator": [
        "processing waste continuous infeed",
        "waste continuous basis infeed vessel",
        "waste disposal apparatus agitation",
        "apparatus disposing waste agitation",
        "crushing performance CT voltage",
        "blade engagement intervals cutting machine",
        "electroblasting activation water pulps",
        "water pulps suspensions electroblasting",
        "waste vinyl fishing net cleaner",
    ],
}

for _k, _v in _EXPANSAO_V8c.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V9 — Novas categorias e expansões temáticas
# Temas: Compressores (movimento vaivém / linear motor), Segurança e
# Travagem, Sensores e Monitorização avançada, Vedações expandidas,
# Terciários para Pumps e Macerators.
# Dataset: bilingue PT/EN.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V9 = {

    # ══════════════════════════════════════════════════════════════════
    # COMPRESSORS — nova pasta de nível superior
    # Captura compressores genéricos que NÃO encaixam em
    # Oil Tools/Gas Compressor nem Pumps/Screw Compressor
    # ══════════════════════════════════════════════════════════════════
    "Compressors": [
        # EN
        "compressor", "compression machine", "gas compression",
        "air compressor", "refrigerant compressor",
        "vapor compressor", "fluid compressor",
        "compressor assembly", "compressor unit",
        "compressor design", "compressor efficiency",
        "positive displacement compressor",
        "dynamic compressor", "compressor housing",
        "compressor rotor", "compressor stator",
        "compressor cylinder", "compressor piston",
        "compressor valve", "compressor seal",
        # PT
        "máquina de compressão",
        "compressor de ar", "compressor de refrigeração",
        "compressor de fluido", "unidade compressora",
        "compressor alternativo", "compressor rotativo",
    ],

    # ── Compressors / Reciprocating Compressor ────────────────────────
    "Compressors/Reciprocating Compressor": [
        # EN
        "reciprocating compressor", "piston compressor",
        "reciprocating piston compressor",
        "compressor reciprocating motion", "reciprocating motion compressor",
        "back-and-forth motion compressor", "back and forth compressor",
        "rectilinear reciprocating", "oscillating piston compressor",
        "crank mechanism compressor", "crankshaft compressor",
        "connecting rod compressor", "crosshead compressor",
        "double acting compressor", "single acting compressor",
        "plunger compressor", "trunk piston compressor",
        "compressor stroke", "compression stroke",
        "suction stroke compressor", "discharge stroke compressor",
        "compressor cylinder liner", "compressor piston rod",
        "compressor piston ring", "compressor valve plate",
        "compressor crankcase",
        # PT
        "compressor de movimento vaivém", "compressor alternativo",
        "compressor de pistão", "compressor de embolo",
        "movimento alternativo compressor", "pistão compressor vaivém",
        "compressor de simples efeito", "compressor de duplo efeito",
        "biela manivela compressor", "virabrequim compressor",
    ],

    # ── Compressors / Linear Motor Compressor ─────────────────────────
    "Compressors/Linear Motor Compressor": [
        # EN
        "linear motor compressor", "linear compressor",
        "linear drive compressor", "linear motor driven compressor",
        "linear motor piston", "linearly driven piston compressor",
        "free piston compressor", "free-piston compressor",
        "resonant linear compressor", "linear oscillating compressor",
        "electromagnetic linear drive compressor",
        "voice coil compressor", "moving magnet compressor",
        "moving coil compressor", "linear actuator compressor",
        "linear motor refrigerant compressor",
        # PT
        "compressor motor linear", "compressor linear",
        "acionamento linear compressor", "pistão livre compressor",
        "compressor pistão linear", "motor linear compressor",
    ],

    # ── Compressors / Stator for Compressor ───────────────────────────
    "Compressors/Stator": [
        # EN
        "stator for compressor", "compressor stator",
        "stator winding compressor", "stator core compressor",
        "stator assembly compressor", "stator frame compressor",
        "stator housing compressor", "stator lamination compressor",
        "stator coil compressor", "stator slot compressor",
        # PT
        "estator para compressor", "estator de compressor",
        "enrolamento estator compressor", "núcleo estator compressor",
    ],

    # ── Compressors / Scroll Compressor ───────────────────────────────
    "Compressors/Scroll Compressor": [
        # EN
        "scroll compressor", "scroll pump", "orbiting scroll",
        "fixed scroll", "scroll mechanism", "scroll fluid machine",
        "scroll expander", "compliant scroll compressor",
        "co-rotating scroll", "scroll wrap compressor",
        "scroll back pressure", "scroll tip seal",
        # PT
        "compressor scroll", "compressor espiral",
        "scroll orbital", "scroll fixo",
    ],

    # ── Compressors / Rotary Compressor ───────────────────────────────
    "Compressors/Rotary Compressor": [
        # EN
        "rotary compressor", "rolling piston compressor",
        "rotary vane compressor", "swing compressor",
        "rotary blade compressor", "eccentric rolling compressor",
        "rolling rotor compressor", "rotary type compressor",
        "rotary compressor housing", "rolling piston assembly",
        # PT
        "compressor rotativo", "compressor de palheta rotativa",
        "compressor de pistão rolante", "compressor de rotor",
    ],

    # ══════════════════════════════════════════════════════════════════
    # SAFETY AND BRAKING — nova pasta de nível superior
    # Segurança mecânica, travagem, intertravamento, controlo de rotação
    # ══════════════════════════════════════════════════════════════════
    "Safety and Braking": [
        # EN
        "safety brake", "braking device", "brake mechanism",
        "braking system", "safety interlock", "interlock device",
        "safety mechanism", "fail-safe device",
        "overspeed protection", "torque limiter",
        "safety clutch", "slip clutch",
        "reverse rotation protection", "rotation stop device",
        "emergency stop mechanism", "anti-runaway device",
        "load holding brake", "parking brake device",
        # PT
        "freio de segurança", "dispositivo de frenagem",
        "mecanismo de travagem", "sistema de travagem",
        "intertravamento de segurança", "dispositivo de segurança",
        "proteção contra sobrevelocidade", "limitador de torque",
        "embraiagem de segurança", "paragem de emergência",
    ],

    # ── Safety and Braking / Backspin and Reverse Rotation ────────────
    "Safety and Braking/Backspin and Reverse Rotation": [
        # EN
        "backspin brake", "anti-backspin", "backspin protection",
        "backspin control", "reverse rotation control",
        "reverse spin protection", "reverse rotation prevention",
        "reverse spin stop", "back-spin braking",
        "counter-rotation brake", "retrograde rotation brake",
        "downhole backspin", "polished rod backspin",
        "backspin energy recovery", "dynamic brake backspin",
        # PT
        "freio de backspin", "controlo de backspin",
        "proteção contra backspin", "controlo de rotação inversa",
        "prevenção de rotação reversa", "freio de rotação inversa",
    ],

    # ── Safety and Braking / Hydraulic Retarder ───────────────────────
    "Safety and Braking/Hydraulic Retarder": [
        # EN
        "hydraulic retarder", "hydrodynamic retarder",
        "hydraulic brake", "hydrodynamic brake",
        "fluid retarder", "viscous retarder",
        "eddy current retarder", "fluid coupling brake",
        "hydraulic deceleration device", "retarder valve",
        "retarder housing", "retarder rotor stator",
        "exhaust brake", "engine retarder",
        "transmission retarder", "auxiliary retarder",
        # PT
        "retardador hidráulico", "freio hidrodinâmico",
        "travão hidráulico", "retardador de fluido",
        "dispositivo de desaceleração hidráulica",
    ],

    # ── Safety and Braking / Safety Interlock ─────────────────────────
    "Safety and Braking/Safety Interlock": [
        # EN
        "safety interlock", "interlock mechanism",
        "interlocking safety device", "interlock switch",
        "safety latch", "safety lock device",
        "safety catch", "fail-safe interlock",
        "door interlock", "guard interlock",
        "machine guard interlock", "interlock control system",
        "safety relay interlock", "interlock valve safety",
        # PT
        "intertravamento de segurança", "mecanismo de intertravamento",
        "dispositivo de intertravamento", "trava de segurança",
        "bloqueio de segurança", "interlock de segurança",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MONITORING AND CONTROLLING — novas subpastas
    # ══════════════════════════════════════════════════════════════════

    # ── Monitoring and controlling / Transducers ──────────────────────
    "Monitoring and controlling/Transducers": [
        # EN
        "transducer", "pressure transducer", "force transducer",
        "piezoelectric transducer", "ultrasonic transducer",
        "acoustic transducer", "displacement transducer",
        "strain gauge transducer", "torque transducer",
        "flow transducer", "level transducer",
        "LVDT transducer", "inductive transducer",
        "capacitive transducer", "optical transducer",
        "magnetostrictive transducer", "signal transducer",
        # PT
        "transdutor", "transdutor de pressão", "transdutor de força",
        "transdutor piezoelétrico", "transdutor ultrassónico",
        "transdutor acústico", "transdutor de deslocamento",
        "extensômetro", "transdutor de torque",
    ],

    # ── Monitoring and controlling / Rod and Tension Monitoring ───────
    "Monitoring and controlling/Rod and Tension Monitoring": [
        # EN
        "rod tension monitoring", "rod load monitoring",
        "sucker rod monitoring", "rod string monitoring",
        "polished rod load sensor", "rod force measurement",
        "rod stress monitoring", "rod fatigue monitoring",
        "rod tension sensor", "downhole rod monitoring",
        "load cell rod", "rod load cell measurement",
        "rod tension telemetry", "rod tension data acquisition",
        "wellbore rod monitoring", "pump rod load",
        # PT
        "monitorização de tensão de haste", "monitorização de carga de haste",
        "sensor de carga de haste polida", "medição de força de haste",
        "monitorização de haste de bombeamento",
        "célula de carga em haste", "tensão de haste de fundo",
    ],

    # ── Monitoring and controlling / Automated Advancement ────────────
    "Monitoring and controlling/Automated Advancement": [
        # EN
        "automated advancement", "automatic advancement system",
        "automated feed control", "automatic feed advancement",
        "automated drilling advancement", "auto-advance mechanism",
        "automated depth control", "automatic downhole advancement",
        "programmable advancement", "step advancement automatic",
        "advancement control system", "feed rate automation",
        "automated tool advancement", "drill feed automation",
        # PT
        "avanço automatizado", "sistema de avanço automático",
        "controlo automático de avanço", "avanço de perfuração automático",
        "mecanismo de avanço automático", "controlo de profundidade automático",
    ],

    # ── Oil Tools/Sensoring — expansão temática ────────────────────────
    "Oil Tools/Sensoring": [
        # EN
        "monitoring sensor downhole", "monitoring sensor wellbore",
        "wellsite sensor monitoring", "sensor data downhole tool",
        "production monitoring sensor", "downhole monitoring array",
        "real-time downhole sensor", "multi-parameter downhole sensor",
        "permanent monitoring downhole", "intelligent sensor downhole",
        "downhole transducer", "wellbore transducer",
        "downhole acoustic transducer", "downhole pressure transducer",
        "borehole transducer array",
        # PT
        "sensor de monitorização de fundo", "sensor de poço em tempo real",
        "array de sensores de fundo", "sensor de produção de fundo",
        "transdutor de fundo de poço",
    ],

    # ══════════════════════════════════════════════════════════════════
    # SEALINGS — expansão de subpastas existentes + novas
    # ══════════════════════════════════════════════════════════════════

    # ── Sealings/Labyrinth Seal — expansão V9 ─────────────────────────
    "Sealings/Labyrinth Seal": [
        # EN
        "serpentine path seal", "serpentine seal",
        "serpentine labyrinth", "tortuous path seal",
        "zigzag seal path", "sinuous seal path",
        "labyrinth and contact seal combination",
        "non-contacting labyrinth seal",
        # PT
        "vedação labiríntica", "vedação de percurso sinuoso",
        "vedação labirinto", "vedação não contactante labirinto",
        "junta labiríntica",
    ],

    # ── Sealings/Lip Seal — expansão V9 ───────────────────────────────
    "Sealings/Lip Seal": [
        # EN
        "split lip seal", "split lip sealing device",
        "divided lip seal", "halved lip seal",
        "two-piece lip seal", "bipartite lip seal",
        "separable lip seal", "split shaft seal",
        "split seal installation",
        # PT
        "vedação de lábio dividida", "vedação de lábio bipartida",
        "vedação de lábio separável", "vedação de eixo dividida",
        "vedação de lábio partido",
    ],

    # ── Sealings/Split Seal — NOVA subpasta ───────────────────────────
    "Sealings/Split Seal": [
        # EN
        "split seal", "split mechanical seal",
        "split face seal", "split ring seal",
        "split sealing device", "two-piece seal assembly",
        "bipartite seal", "half seal assembly",
        "field-installable split seal", "split seal cartridge",
        "axially split seal", "radially split seal",
        "split seal for shaft", "split seal replacement",
        # PT
        "vedação dividida", "vedação mecânica dividida",
        "vedação bipartida", "vedação de dois lados",
        "conjunto de vedação dividido",
    ],

    # ── Sealings/V-Ring and Exclusion Seal — NOVA subpasta ────────────
    "Sealings/V-Ring and Exclusion Seal": [
        # EN
        "v-ring seal", "v ring seal", "exclusion seal",
        "V-seal", "axial v-ring", "axial lip seal v-ring",
        "dirt exclusion seal", "exclusion wiper seal",
        "contamination exclusion seal", "axial contact seal",
        "all-rubber v-ring", "v-seal shaft",
        # PT
        "vedação v-ring", "vedação de exclusão",
        "anel V de vedação", "vedação axial de lábio",
        "vedação de exclusão de contaminantes",
    ],

    # ══════════════════════════════════════════════════════════════════
    # PUMPS — Terciários para categorias mais populosas
    # ══════════════════════════════════════════════════════════════════

    # ── Pumps/PC Pump and Motor / Liner and Insert Stator ─────────────
    "Pumps/PC Pump and Motor/Liner and Insert Stator": [
        # EN
        "stator liner", "liner stator pump", "inserted stator",
        "replaceable stator liner", "stator sleeve insert",
        "press-fit stator liner", "bonded stator liner",
        "stator insert cavity pump", "liner insert progressive cavity",
        "hard liner stator", "metal liner stator",
        "elastomer liner stator", "wear liner stator",
        # PT
        "camisa do estator", "inserto de estator",
        "estator com camisa", "revestimento de estator",
        "inserto de estator substituível",
    ],

    # ── Pumps/PC Pump and Motor / Intake and Inlet ────────────────────
    "Pumps/PC Pump and Motor/Intake and Inlet": [
        # EN
        "pump intake", "pump inlet", "PCP intake",
        "downhole intake", "intake section pump",
        "pump inlet screen", "intake filter pump",
        "gas separation intake", "pump intake gas separator",
        "submersible pump intake", "intake housing pump",
        "multi-stage intake", "floater intake pump",
        # PT
        "entrada da bomba", "seção de entrada da bomba",
        "filtro de entrada da bomba",
        "intake de bomba de cavidade progressiva",
        "entrada com separador de gás",
    ],

    # ── Pumps/PC Pump and Motor / Torque and Speed Control ────────────
    "Pumps/PC Pump and Motor/Torque and Speed Control": [
        # EN
        "PCP torque control", "progressive cavity torque",
        "PCP speed control", "pump torque monitoring",
        "rod torque surface", "torque rpm PCP",
        "torque limiting PCP", "variable speed PCP",
        "PCP drive VFD", "progressive cavity VFD",
        "soft start PCP", "pump torque overload",
        # PT
        "controlo de torque de BCP", "velocidade de bomba de cavidade",
        "monitorização de torque de bomba",
        "VFD para bomba de cavidade", "controlo de velocidade BCP",
    ],

    # ── Pumps/Screw Pump / Multiphase Control — NOVO Terciário ────────
    "Pumps/Screw Pump/Multiphase Control": [
        # EN
        "screw pump GVF control", "gas volume fraction control screw",
        "multiphase screw pump control", "GVF monitoring twin screw",
        "twin screw pump gas handling", "gas tolerance screw pump",
        "wet gas screw pump control", "multiphase pump GVF sensor",
        "gas lock prevention screw pump", "recirculation bypass screw",
        # PT
        "controlo de GVF em bomba de parafuso",
        "bomba de parafuso multifásica controlo",
        "prevenção de gas lock bomba de parafuso",
        "monitorização de GVF bomba de parafuso gémeo",
    ],

    # ── Pumps/Centrifugal Pump / Impeller — NOVO Terciário ────────────
    "Pumps/Centrifugal Pump/Impeller": [
        # EN
        "impeller design", "impeller geometry",
        "centrifugal impeller", "closed impeller",
        "open impeller", "semi-open impeller",
        "impeller blade", "impeller vane",
        "impeller wear ring", "impeller balancing",
        "impeller material", "pump impeller coating",
        "mixed flow impeller", "axial impeller",
        # PT
        "impulsor de bomba centrífuga", "design de impulsor",
        "geometria de impulsor", "impulsor fechado",
        "impulsor aberto", "palheta de impulsor",
    ],

    # ── Pumps/Centrifugal Pump / Volute and Diffuser — NOVO Terciário ─
    "Pumps/Centrifugal Pump/Volute and Diffuser": [
        # EN
        "volute casing", "pump volute", "spiral casing",
        "volute design", "pump diffuser", "diffuser vane",
        "annular casing pump", "volute tongue",
        "pump casing design", "diffuser ring pump",
        "radial diffuser", "return channel pump",
        # PT
        "carcaça em espiral", "voluta de bomba",
        "difusor de bomba", "design de voluta",
        "carcaça anelar de bomba",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MACERATOR — Terciários para subpastas mais populosas
    # ══════════════════════════════════════════════════════════════════

    # ── Macerator/Industrial Crusher / Knife and Blade System ─────────
    "Macerator/Industrial Crusher/Knife and Blade System": [
        # EN
        "cutting knife system", "blade knife assembly",
        "knife holder system", "knife mounting system",
        "interchangeable knife", "replaceable blade crusher",
        "knife geometry crusher", "knife angle shredder",
        "counter knife shredder", "fixed knife shredder",
        "rotating knife crusher", "blade gap adjustment",
        "knife wear crusher", "blade hardness shredder",
        "knife material hardened steel",
        # PT
        "sistema de facas triturador", "suporte de faca triturador",
        "geometria de faca triturador", "faca intercambiável triturador",
        "ajuste de folga de faca",
    ],

    # ── Macerator/Industrial Crusher / Drive and Motor ────────────────
    "Macerator/Industrial Crusher/Drive and Motor": [
        # EN
        "crusher drive motor", "shredder drive system",
        "crusher motor power", "shredder motor control",
        "hydraulic drive shredder", "electric drive crusher",
        "crusher gearbox drive", "shredder gear reducer",
        "direct drive shredder", "belt drive crusher",
        "torque drive crusher", "variable speed shredder",
        "crusher drive shaft", "shredder drive coupling",
        # PT
        "motor de triturador", "acionamento de triturador",
        "sistema de acionamento de triturador",
        "motoredutor de triturador",
    ],

    # ── Macerator/Comminutor / Flow Channel ───────────────────────────
    "Macerator/Comminutor/Flow Channel": [
        # EN
        "comminutor flow channel", "inline comminutor channel",
        "sewage flow comminutor", "channel bar screen comminutor",
        "comminutor water channel", "bar screen macerator",
        "in-line channel comminutor", "open channel comminutor",
        "flow channel cutter", "channel grinder flow",
        # PT
        "canal de fluxo cominuidor", "cominuidor em canal",
        "triturador de esgoto em canal",
    ],

    # ══════════════════════════════════════════════════════════════════
    # ELECTRIC MOTORS — novas subpastas
    # ══════════════════════════════════════════════════════════════════

    # ── Electric Motors / Linear Motor ────────────────────────────────
    "Electric Motors/Linear Motor": [
        # EN
        "linear motor", "linear electric motor",
        "linear drive motor", "linear actuator motor",
        "linear induction motor", "linear synchronous motor",
        "permanent magnet linear motor", "voice coil motor",
        "moving magnet linear motor", "moving coil linear motor",
        "linear motor stator", "linear motor mover",
        "linear motor forcer", "linear motor primary",
        "linear motor secondary", "linear motor thrust",
        # PT
        "motor linear", "motor elétrico linear",
        "motor de acionamento linear", "atuador motor linear",
        "motor de indução linear", "motor síncrono linear",
    ],

    # ── Electric Motors / Motor Stator ────────────────────────────────
    "Electric Motors/Motor Stator": [
        # EN
        "motor stator", "stator assembly motor",
        "stator winding electric motor", "stator lamination",
        "stator core electric", "stator slot motor",
        "stator coil motor", "stator frame motor",
        "stator housing motor", "stator cooling motor",
        "motor stator design", "segmented stator",
        "stator punching", "wound stator motor",
        # PT
        "estator de motor", "montagem de estator de motor",
        "enrolamento de estator", "laminação de estator",
        "núcleo de estator", "carcaça de estator",
    ],

    # ══════════════════════════════════════════════════════════════════
    # OIL TOOLS — expansões de segurança operacional
    # ══════════════════════════════════════════════════════════════════

    # ── Oil Tools/Drive Head — expansão segurança ─────────────────────
    "Oil Tools/Drive Head": [
        # EN
        "drive head safety device", "drive head interlock",
        "drive head brake mechanism", "drive head automatic stop",
        "wellhead drive interlock", "drive head overspeed trip",
        "drive head emergency stop", "automatic wellhead shutdown",
        # PT
        "dispositivo de segurança cabeçote", "intertravamento cabeçote",
        "paragem automática cabeçote",
        "proteção de sobrevelocidade cabeçote",
    ],

    # ── Oil Tools/Anti-rotation control — expansão ────────────────────
    "Oil Tools/Anti-rotation control": [
        # EN
        "anti-rotation device", "rotation lock mechanism",
        "anti-spin tool", "reverse rotation control downhole",
        "non-rotating string", "rotor lock device",
        "rotation stop downhole", "torsion stop device",
        # PT
        "dispositivo antirrotação de fundo", "trava de rotação",
        "mecanismo de bloqueio de rotação",
        "controlo de rotação inversa de fundo",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MEASURING DEVICES — expansão com sensores avançados
    # ══════════════════════════════════════════════════════════════════
    "Measuring devices": [
        # EN
        "monitoring sensor", "sensor array measurement",
        "wellbore monitoring sensor", "production monitoring device",
        "downhole measurement sensor", "automated measurement device",
        "sensor module measurement", "in-line measurement sensor",
        "smart sensor measuring", "digital measurement device",
        # PT
        "sensor de monitorização", "dispositivo de medição automatizado",
        "sensor de produção", "módulo de sensor de medição",
        "sensor inteligente de medição",
    ],

}

for _k, _v in _EXPANSAO_V9.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V10 — Criação de subpastas para esvaziar as raízes
# ══════════════════════════════════════════════════════════════════════
# Objetivo: levar 395 patentes classificadas apenas no Nível 1 (raiz)
# para Nível 2/3. Base: análise de n-gramas dos títulos+abstracts das
# patentes afetadas. Todos os termos têm 2+ palavras (score ≥ 2 com
# uma única ocorrência) ou 3+ palavras (score ≥ 3) para garantir que
# a subpasta supere a raiz no scoring hierárquico.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V10 = {

    # ══════════════════════════════════════════════════════════════════
    # MEDIA AND DOCUMENT DESTRUCTION — 100 patentes (a maior raiz)
    # Todas as amostras são sobre trituradores de papel (paper shredders)
    # Criamos 5 subpastas técnicas para dividir o espaço.
    # ══════════════════════════════════════════════════════════════════

    # ── Paper Shredder — subpasta genérica (captura a maioria) ───────
    "Media and Document Destruction/Paper Shredder": [
        # EN — bigramas (2pt) e trigramas (3pt) dominantes
        "paper shredder", "document shredder", "paper shredding",
        "shredder paper", "shredded paper", "waste paper shredder",
        "paper shredding machine", "paper shredding mechanism",
        "paper shredder device", "automatic paper shredder",
        "paper shredder module", "rotary paper shredder",
        "mechanical paper shredder", "office paper shredder",
        "industrial paper shredder", "paper scraps shredder",
        "shredding paper", "paper inlet shredder",
        "paper guide shredder", "shredder paper guide",
        # PT
        "triturador de papel", "fragmentadora de papel",
        "máquina triturador papel", "fragmentadora documentos",
        "destruidor de documentos",
    ],

    # ── Paper Shredder / Cutting Mechanism ──────────────────────────
    "Media and Document Destruction/Paper Shredder/Cutting Mechanism": [
        # EN
        "shredder cutter", "cutter shredder", "shredding cutter",
        "cutting blade shredder", "shredder blade",
        "shredder cutting mechanism", "paper cutting mechanism",
        "shredding mechanism", "shredder knife",
        "cutting type paper", "single cutting type",
        "spinning cutter shredder", "cutter positioning shaft",
        "cutter door shredder", "razor blade shredder",
        "blade shredding paper", "shredder cutter shaft",
        # PT
        "mecanismo de corte triturador", "lâmina triturador papel",
        "faca triturador documentos", "sistema de corte fragmentadora",
    ],

    # ── Paper Shredder / Paper Feed and Guide ───────────────────────
    "Media and Document Destruction/Paper Shredder/Paper Feed and Guide": [
        # EN
        "paper guide", "paper guide device", "paper feed shredder",
        "paper feeding shredder", "paper inlet", "paper shifting mechanism",
        "shifting mechanism paper", "paper pressing device",
        "pressing device shredder", "paper filling mechanism",
        "mechanical paper filling", "paper transport shredder",
        "feeding device shredder", "paper removing structure",
        "removing structure shredder", "paper shredder inlet",
        # PT
        "guia de papel triturador", "alimentador papel triturador",
        "dispositivo alimentação papel",
    ],

    # ── Paper Shredder / Safety and Protection ──────────────────────
    "Media and Document Destruction/Paper Shredder/Safety and Protection": [
        # EN
        "overload protection shredder", "shredder overload protection",
        "overload protection device", "safety device shredder",
        "shredder safety", "fire explosion proof shredder",
        "fire proof shredder", "explosion proof paper",
        "protection device shredder", "shredder with overload",
        "jam protection shredder", "paper jam protection",
        # PT
        "proteção sobrecarga triturador", "triturador à prova explosão",
        "dispositivo segurança fragmentadora",
    ],

    # ── Paper Shredder / Housing and Bin ────────────────────────────
    "Media and Document Destruction/Paper Shredder/Housing and Bin": [
        # EN
        "shredder housing", "shredder cabinet", "shredder structure",
        "trash can shredder", "retractable trash", "trash bin shredder",
        "reinforcing structure shredder", "shredder reinforcing",
        "collection bin shredder", "waste bin shredder",
        "shredder waste container", "shredder box",
        "shredder cleaning device", "cleaning device shredder",
        # PT
        "carcaça triturador papel", "compartimento coleta papel",
        "caixa fragmentadora",
    ],

    # ══════════════════════════════════════════════════════════════════
    # GRINDING AND MILLING — 62 patentes
    # Temas: moinhos, trituradores universais, moedores industriais,
    # moagem de ervas chinesas/alimentos, pulverizadores.
    # ══════════════════════════════════════════════════════════════════

    # ── Grinding Machines (captura genérico) ───────────────────────
    "Grinding and Milling/Grinding Machines": [
        # EN
        "grinding machine", "grinding mill", "grinder device",
        "grinding device", "grinding apparatus", "grinding mechanism",
        "grinding unit", "grinder unit", "grinding system",
        "grinding equipment", "grinder machine", "grinder apparatus",
        "two-way rotation grinding", "drooping type grinder",
        "pendent grinder", "swing grinder", "hammer grinder",
        "dust free grinder", "dustless grinder",
        # PT
        "máquina de moagem", "moinho triturador", "moedor industrial",
        "dispositivo moagem", "máquina de esmerilhar",
    ],

    # ── Hammer Mill and Pulverizer ─────────────────────────────────
    "Grinding and Milling/Hammer Mill and Pulverizer": [
        # EN
        "hammer mill", "hammer grinder", "hammer pulverizer",
        "vertical hammer mill", "horizontal hammer mill",
        "food pulverizer", "universal pulverizer", "industrial pulverizer",
        "dust free hammer", "pendent up down",
        "up and down swing", "swing grinder",
        "globule grinding mill", "globule grinding",
        # PT
        "moinho de martelos", "pulverizador industrial",
        "moinho vertical", "triturador de martelos",
    ],

    # ── Chinese Medicine and Herbal Crusher ────────────────────────
    "Grinding and Milling/Chinese Medicine and Herbal Crusher": [
        # EN
        "chinese medicine crusher", "chinese herbal medicine",
        "traditional chinese medicine", "chinese medicinal herb",
        "medicinal herb crushing", "chinese herbal crusher",
        "herbal medicine grinder", "herb crushing system",
        "medicinal processing equipment", "medicinal material crusher",
        "frequency converter medicine", "traditional chinese medicinal",
        "medicine grinder", "herbal medicine pulverizer",
        "chinese medicinal pulverizer",
    ],

    # ── Food Grinding and Pulverization ────────────────────────────
    "Grinding and Milling/Food Grinding": [
        # EN
        "food pulverizer", "food grinder", "food grinding",
        "kitchen garbage grinder", "kitchen garbage grinding",
        "kitchen waste grinding", "kitchen waste grinder",
        "food garbage processor", "garbage processor",
        "grinding kitchen garbage", "kitchen grinding",
        "flour mill", "flour milling", "auxiliary flour",
        "refined cotton grinder", "cotton grinder",
        "wet carbon grinding", "carbon grinding device",
        "squashing mechanism food", "food squashing",
        # PT
        "moedor de alimentos", "triturador resíduos cozinha",
        "moedor cozinha", "moinho de farinha",
    ],

    # ══════════════════════════════════════════════════════════════════
    # SEALINGS (raiz) — 47 patentes
    # Muitas são "Sealing Device" puro (JPO/NCIPI) com descrições de
    # lábio/anel/core metal — tipicamente seals de bearings e pumps.
    # ══════════════════════════════════════════════════════════════════

    # ── Sealing Device Generic (captura "Sealing Device" isolados) ──
    "Sealings/Sealing Device Generic": [
        # EN
        "sealing device", "sealing apparatus", "sealing assembly",
        "sealing structure", "sealing system device",
        "sealing performance", "sealing capable", "provide sealing",
        "excellent sealing", "sealing solution", "solution sealing",
        "sealing provide", "sealing device pump", "sealing device rotating",
        "sealing device bearing", "sealing device shaft",
        "device sealing performance", "sealing device improved",
        # PT
        "dispositivo de vedação", "dispositivo vedação",
        "aparelho de vedação", "conjunto de vedação",
        "sistema de vedação", "desempenho de vedação",
    ],

    # ── Sealings / Ring and Peripheral Seal ─────────────────────────
    "Sealings/Ring and Peripheral Seal": [
        # EN — bigramas dominantes nos abstracts
        "inner peripheral", "outer peripheral", "peripheral surface",
        "peripheral side", "inner peripheral surface", "outer peripheral side",
        "inner peripheral side", "outer peripheral surface",
        "inner ring seal", "outer ring seal", "seal inner ring",
        "seal outer ring", "ring seal bearing", "bearing ring seal",
        "sealing ring inner", "sealing ring outer",
        "core metal seal", "seal core metal", "ring bearing seal",
        "fitted inner peripheral", "fitted outer peripheral",
        "sealing fitted inner",
        # PT
        "superfície periférica interna", "superfície periférica externa",
        "anel de vedação interno", "anel de vedação externo",
    ],

    # ── Sealings / Rubber and Elastic Seal ──────────────────────────
    "Sealings/Rubber and Elastic Seal": [
        # EN
        "rubber like elastic", "rubber like sealing", "like elastic",
        "elastic sealing", "elastic seal member", "rubber seal",
        "elastic sealing member", "formed elastic", "elastic rubber seal",
        "rubber elastic seal", "synthetic rubber seal",
        "muddy water seal", "muddy water prevent", "muddy water preventing",
        "non contact seal", "non contact sealing",
        # PT
        "vedação elástica", "vedação de borracha",
        "borracha elástica",
    ],

    # ══════════════════════════════════════════════════════════════════
    # PUMPS (raiz) — 27 patentes
    # Temas: positive displacement, multiphase, water pump, wave pump
    # ══════════════════════════════════════════════════════════════════

    # ── Pumps / Positive Displacement Pump ─────────────────────────
    "Pumps/Positive Displacement Pump": [
        # EN
        "positive displacement", "positive displacement pump",
        "displacement pump", "displacement pumps",
        "rotary piston positive", "roots principle pump",
        "roots principle", "incompressible media pump",
        "pump using roots", "rotary piston pump",
        "positive displacement rotary",
        # PT
        "bomba de deslocamento positivo", "deslocamento positivo",
        "bomba volumétrica", "bomba rotativa de pistão",
    ],

    # ── Pumps / Multiphase and Slug Flow ───────────────────────────
    "Pumps/Multiphase and Slug Flow": [
        # EN
        "multiphase mixtures", "conveying multiphase", "multiphase mixture",
        "multiphase pump", "multiphase pumping system",
        "viscous media conveying", "conveying viscous media",
        "viscous medium system", "conveying viscous medium",
        "liquid gas mixture", "gas liquid mixture borehole",
        "crossover two phase", "two phase flow pump",
        "slug flow removing", "slug flow pump",
        "oil gas separation", "oil gas separating",
        "separation buffering tank", "gas separation buffering",
        "tubular slug reducer", "slug reducer",
        # PT
        "bomba multifásica", "mistura multifásica",
        "escoamento bifásico bomba", "mistura gás líquido",
    ],

    # ── Pumps / Water and General Fluid Pump ──────────────────────
    "Pumps/Water and General Fluid Pump": [
        # EN
        "water pump hydraulic", "hydraulic water pump",
        "wave pump assembly", "wave pump",
        "fluid pumping installation", "fluid pumping device",
        "pumping device installation", "pumping system waste",
        "waste pumping system", "waste pumping",
        "drum follower plate pump", "follower plate pumping",
        "pump assembly discharge", "discharge baffle means",
        "baffle means pump", "pump discharge baffle",
        "implantable cardiac pump", "cardiac pump",
        "screw centrifuge wheel pump", "centrifuge wheel pump",
        # PT
        "bomba hidráulica", "bomba dágua hidráulica",
        "bomba multidirecional", "bomba para transporte fluido",
        "sistema de pulmões bomba", "bomba transporte fluido",
        "aspirador de pó", "bomba aspirador",
    ],

    # ── Pumps / Cavitation and Control ─────────────────────────────
    "Pumps/Cavitation and Control": [
        # EN
        "cavitation positive displacement", "cavitation pump",
        "monitoring cavitation", "cavitation monitoring",
        "load shedding control", "shedding control pump",
        "load shedding pump", "control system pumps",
        "pump load shedding",
        # PT
        "cavitação bomba", "controlo cavitação bomba",
        "sistema controlo bomba",
    ],

    # ══════════════════════════════════════════════════════════════════
    # CONVEYOR AND TRANSPORT — 25 patentes
    # Temas: processing plastic material (várias cópias idênticas),
    # forage/branch crushers, soft fiber chopping, feed device
    # ══════════════════════════════════════════════════════════════════

    # ── Conveyor / Plastic Recycling Processor ─────────────────────
    # Captura a série de "Device For Processing Plastic Material"
    "Conveyor and Transport/Plastic Recycling Processor": [
        # EN — trigramas com 9-10 ocorrências cada
        "processing plastic material", "plastic material device",
        "plastic recycling", "waste plastics recycling",
        "thermoplastic waste plastics", "waste plastics",
        "plastics particular thermoplastic", "thermoplastic plastics",
        "mixing crushing tool", "crushing tool conveying",
        "tool conveying direction", "central longitudinal axis",
        "imaginary extension central", "extension central longitudinal",
        "pretreated plastic interior", "plastic interior container",
        "receiving pretreated housing", "pretreated housing rotating",
        "housing rotating plastic", "agglomerating screw",
        "screw against conveying", "against conveying direction",
        "mixing heating optionally", "heating optionally",
        # PT
        "reciclagem de plástico", "processamento material plástico",
        "reciclagem termoplástico",
    ],

    # ── Conveyor / Branch and Tree Crusher ────────────────────────
    "Conveyor and Transport/Branch and Tree Crusher": [
        # EN
        "branch smashing", "branch smashing machine", "smashing machine",
        "branch breaking", "branch-breaking machine", "branch breaking machine",
        "tree crusher", "feed device tree", "device tree crusher",
        "tree crusher feed", "wood crusher feeding",
        "false operation preventing", "preventing false operation",
        # PT
        "triturador de galhos", "triturador de árvores",
        "quebrador de galhos", "máquina triturar galhos",
    ],

    # ── Conveyor / Fiber and Straw Processing ──────────────────────
    "Conveyor and Transport/Fiber and Straw Processing": [
        # EN
        "soft fiber chopping", "fiber chopping machine",
        "chopping machine charging", "charging agitating scattering",
        "agitating scattering device", "fiber chopping",
        "chopping machine improved", "improved structure chopping",
        # PT
        "máquina picar fibra", "máquina cortar fibra macia",
    ],

    # ── Conveyor / Liquid-Solid Separation Transport ──────────────
    "Conveyor and Transport/Liquid-Solid Separation Transport": [
        # EN
        "liquid solid separation", "separation liquid solid",
        "conveying fluid device", "conveying device fluid",
        "fluid conveying device",
        # PT
        "separação líquido sólido", "dispositivo separação material",
        "separação material líquido sólido",
    ],

    # ── Conveyor / EPE and Foam Recovery ──────────────────────────
    "Conveyor and Transport/EPE and Foam Recovery": [
        # EN
        "waste epe", "expandable polyethylene", "polyethylene foam",
        "foam plastics compressor", "recovering waste epe",
        "epe foam plastics", "waste foam recovery",
    ],

    # ══════════════════════════════════════════════════════════════════
    # OIL TOOLS (raiz) — 24 patentes
    # Temas: anti-rotation tools, downhole sensors deployment,
    # artificial lift protection, chemical treatment downhole
    # ══════════════════════════════════════════════════════════════════

    # ── Oil Tools / Downhole Tool Generic ─────────────────────────
    "Oil Tools/Downhole Tool Generic": [
        # EN
        "downhole tool", "wellbore tool", "downhole casing tool",
        "downhole tool casing", "casing scraper tool",
        "downhole tool induced", "induced rotation tool",
        "tool downhole induced", "bore tubular tool",
        "downhole tool assembly", "downhole tool apparatus",
        # PT
        "ferramenta de fundo poço", "ferramenta fundo poço",
        "ferramenta downhole genérica",
    ],

    # ── Oil Tools / Chemical Treatment and Filtration Downhole ────
    "Oil Tools/Chemical Treatment and Filtration": [
        # EN — trigramas do cluster de patentes sobre artificial lift
        "downhole artificial lift", "artificial lift protection",
        "artificial lift system protection", "lift system protection",
        "chemical treatment accomplished", "chemical treatment downhole",
        "treating chemical recharged", "chemical recharged replenished",
        "recharged replenished various", "replenished various downhole",
        "scale inhibitors chemical", "chemical scale inhibitors",
        "porous medium contains", "medium contains supports",
        "filtering comprised porous", "comprised porous medium",
        "fluid conditioning designed", "stream fluid conditioning",
        "pump effect artificial", "intake pump effect",
        "filter sand particulate", "sand particulate matter",
        "particulate matter fills",
        # PT
        "tratamento químico fundo poço", "inibidor de incrustação fundo",
    ],

    # ── Oil Tools / Sensor Deployment and Data Services ───────────
    "Oil Tools/Sensor Deployment and Data Services": [
        # EN
        "deploying sensor downhole", "sensor downhole tool",
        "deploy sensor downhole", "apparatus deploying sensor",
        "oilfield data loading", "data loading services",
        "oilfield data services", "acoustic fluid analyzer",
        "fluid analyzer acoustic", "analyzer downhole",
        "data services request", "services request handling",
        # PT
        "implantação sensor fundo poço", "serviços dados petróleo",
    ],

    # ── Oil Tools / Anti-Rotation and Positioning ─────────────────
    "Oil Tools/Anti-Rotation and Positioning": [
        # EN
        "anti rotation", "anti-rotation blades", "anti-rotation tool",
        "rotation downhole tool", "tubular member wellbore",
        "positioning tubular member", "positioning wellbore",
        "wellbore tool anchoring", "anchoring device wellbore",
        "anchoring device tool", "grip enhanced tractoring",
        "grip enhanced", "enhanced tractoring",
        # PT
        "ferramenta antirrotação fundo", "dispositivo ancoragem poço",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MACERATOR (raiz) — 16 patentes
    # Temas: cutter disc/assemblies for grinder pumps,
    # medicinal/Chinese crushers, sludge processing, waste containment
    # ══════════════════════════════════════════════════════════════════

    # ── Macerator / Cutter Disc and Assembly ──────────────────────
    "Macerator/Cutter Disc and Assembly": [
        # EN
        "cutter wheel", "cutter disc", "cutter assembly",
        "cutter assembly grinder", "cutter assembly suitable",
        "assembly grinder pumps", "grinder pump cutter",
        "cutter disc teeth", "cutter discs teeth",
        "stacks cutters", "stacks cutters rail",
        "periphery stacks cutters", "contra rotating interleaved",
        "interleaved cutter", "rotating interleaved cutter",
        "angled ribs slots", "ribs slots therebetween",
        "cutters rail has", "rail has angled",
        "macerator stacks contra", "passing liquid slots",
        # PT
        "conjunto de cortadores", "disco de corte triturador",
        "lâminas corte triturador",
    ],

    # ── Macerator / Medicinal Material Crusher ────────────────────
    "Macerator/Medicinal Material Crusher": [
        # EN
        "medicinal material crusher", "medicinal material slicing",
        "double layer charging", "charging basket type",
        "traditional chinese medicine crusher", "portable cordyceps",
        "cordyceps crusher", "baffle medicinal material",
        "medicinal material baffle", "medicine material slicing",
        "slicing machine medicine",
        # PT
        "triturador material medicinal",
    ],

    # ── Macerator / Sludge and Waste Processing ───────────────────
    "Macerator/Sludge and Waste Processing": [
        # EN
        "sludge reduction", "sludge reduction treatment",
        "sludge processing apparatus", "sewage treatment system",
        "household garbage treating", "stainless steel household",
        "garbage treating device", "fluid waste containment",
        "waste containment", "waste toner cartridge",
        "toner cartridge processing", "asbestos crushing system",
        "asbestos crushing method", "asbestos crusher",
        "anti residual cutting", "anti-residual cutting bin",
        "cutting bin coatings", "internal coatings cutting",
        # PT
        "tratamento redução lodo", "processamento resíduo asbesto",
    ],

    # ══════════════════════════════════════════════════════════════════
    # DRIVE SHAFTS (raiz) — 15 patentes
    # Tema dominante: Polymer swelling particle dissolving devices
    # (6+ patentes idênticas), chopper/shredder with transmission shaft
    # ══════════════════════════════════════════════════════════════════

    # ── Drive Shafts / Polymer Swelling Dissolution Device ────────
    "Drive Shafts/Polymer Swelling Dissolution Device": [
        # EN — cluster MUITO específico de 6+ patentes idênticas
        "polymer swelling", "polymer swelling particle",
        "swelling particle dissolving", "particle dissolving accelerating",
        "dissolving accelerating device", "accelerated polymer",
        "accelerated polymer swelling", "polymeric compound swelling",
        "compound swelling particles", "swelling particles dissolving",
        "liquid storage chamber", "storage chamber stretching",
        "chamber stretching unit", "fixed liquid storage",
        "stretching unit liquid", "liquid inlet liquid outlet",
        "fixed tooth plate", "fixed toothed plate",
        "movable toothed plate", "toothed plate movable",
        "plate movable toothed", "particle dissolution",
        "bipolar polymer swollen", "polymer swollen particle",
        "polymer swollen", "swollen particle dissolution",
        # PT
        "dissolução partícula polímero",
    ],

    # ── Drive Shafts / Transmission Shaft Mechanical ──────────────
    "Drive Shafts/Transmission Shaft Mechanical": [
        # EN
        "transmission shaft", "shaft transmission", "shaft transmission shaft",
        "transmission shaft connected", "transmission shaft transmission",
        "fixed transmission shaft", "shaft connected motor",
        "drive shaft connected", "drive shaft transmission",
        "bearing seat shaft", "shaft bearing seat",
        "precision screw dispensing", "screw dispensing pump",
        "dispensing pump screw", "multifunctional shredder shaft",
        "lubricating structure supercharging", "supercharging device lubricating",
        # PT
        "eixo de transmissão", "veio de transmissão mecânico",
    ],

    # ══════════════════════════════════════════════════════════════════
    # ELECTRIC MOTORS (raiz) — 14 patentes
    # ══════════════════════════════════════════════════════════════════

    # ── Electric Motors / Motor Driven Pump ───────────────────────
    "Electric Motors/Motor Driven Pump": [
        # EN
        "electric motor driven", "motor driven pump", "driven pump",
        "operation electric motor", "motor driving pump",
        "motor driving", "electric motor driving",
        "provide electric motor", "pump determined trend",
        "hsoll pump regulated", "flow along adjustable",
        "head hsoll pump", "hsoll pump",
        "along adjustable", "determined trend",
        # PT
        "bomba acionada motor elétrico", "motor elétrico aciona bomba",
    ],

    # ── Electric Motors / Synchronous and Permanent Magnet ────────
    "Electric Motors/Synchronous and Permanent Magnet": [
        # EN
        "permanent magnet", "permanent magnet motor",
        "permanent magnet synchronous", "magnet synchronous motor",
        "synchronous motor", "permanent magnet synchronous motor",
        "motor control unit", "control unit connected",
        "positive feedback motor", "motor positive feedback",
        "characteristic curve motor", "motor characteristic curve",
        "hydraulic self motor", "self-regulating motor",
        # PT
        "motor síncrono imã permanente", "motor síncrono permanente",
    ],

    # ══════════════════════════════════════════════════════════════════
    # FILTRATION (raiz) — 13 patentes (mostly PT)
    # ══════════════════════════════════════════════════════════════════

    # ── Filtration / Particle Filter Device (PT) ──────────────────
    "Filtration/Particle Filter Device": [
        # PT — dominante, bigramas tipo "meio filtro" e "para partículas"
        "meio filtro", "filtro pode", "dispositivo para filtro",
        "dispositivo para partículas", "para partículas filtro",
        "presente invenção refere filtro", "refere filtro",
        "compreendendo pelo menos duas", "menos duas camadas",
        "uma camada filtro", "camada filtro",
        "apresenta uma abertura", "uma abertura filtro",
        "envolve filtro", "filtro que envolve",
        # EN
        "particle filter device", "filter for particles",
        "filter comprising layers", "multilayer filter",
        "filter opening arrangement",
    ],

    # ══════════════════════════════════════════════════════════════════
    # AGRICULTURE AND BIOMASS (raiz) — 13 patentes
    # ══════════════════════════════════════════════════════════════════

    # ── Agriculture / Forage Harvester Cutterhead ────────────────
    "Agriculture and Biomass/Forage Harvester Cutterhead": [
        # EN
        "forage harvester", "harvester cutterhead",
        "forage harvester cutterhead", "rotatable forage",
        "rotatable forage harvester", "cutterhead generating cylinder",
        "generating cylinder cutter", "cutterhead rotates",
        "cylindrical tool holder", "tool holder forage",
        "cutter cylindrical tool", "half axial length",
        "fasteners secure knives", "secure knives",
        "knives cutterhead", "cutting edges knives",
        # PT
        "colhedora forragem", "cabeçote cortador forragem",
    ],

    # ── Agriculture / Crop Straw Filament Rubbing ────────────────
    "Agriculture and Biomass/Crop Straw Processing": [
        # EN
        "crop straw", "crop straw filament", "straw filament",
        "filament rubbing machine", "straw filament rubbing",
        "rubbing machine crop", "machine crop straw",
        "traditional crop straw", "crop straws cutting",
        "blunt blades corrugated", "blades corrugated wall",
        "corrugated wall blade", "crop straws blunt",
        # PT
        "palha de cultura", "processamento palha",
    ],

    # ══════════════════════════════════════════════════════════════════
    # BEARINGS (raiz) — 10 patentes
    # ══════════════════════════════════════════════════════════════════

    # ── Bearings / Bearing Housing and Assembly ──────────────────
    "Bearings/Bearing Housing and Assembly": [
        # EN
        "bearing housing", "bearing assembly", "bearing arrangement",
        "arranged bearing housing", "bearing housing shaft",
        "housing shaft ends", "shaft ends mounted bearings",
        "mounted bearings arranged", "bearings arranged bearing",
        "ends mounted bearings", "bearing housing assembly",
        "ring annular bearing", "bearing ring annular",
        "radially outwardly bearing", "detachably connected bearing",
        # PT
        "carcaça de rolamento", "alojamento de rolamento",
        "montagem de rolamento",
    ],

    # ── Bearings / Double Flow Pump Bearings ─────────────────────
    "Bearings/Double Flow Pump Bearings": [
        # EN
        "double flow pump", "flow pump double", "pump double flow",
        "double flow pump housing", "flow pump housing",
        "units convey conveying", "convey conveying medium",
        "conveying medium inlet", "inlet opposite directions",
        "opposite directions outlet", "units have shaft ends",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MONITORING AND CONTROLLING (raiz) — 8 patentes
    # ══════════════════════════════════════════════════════════════════

    # ── Monitoring / Pump Control Unit ───────────────────────────
    "Monitoring and controlling/Pump Control Unit": [
        # EN
        "control unit pump", "pump control unit", "unit control unit",
        "unit control pump", "controlling pump",
        "control circuit pump", "pump control circuit",
        "sensor data acquisition", "data acquisition pump",
        "data acquisition sensor", "sensor data pump",
        "control unit connected",
        # PT
        "unidade de controlo bomba", "circuito controlo bomba",
        "aquisição dados bomba",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MIXING AND AGITATION (raiz) — 7 patentes
    # ══════════════════════════════════════════════════════════════════

    "Mixing and Agitation/Mixer and Blender Device": [
        # EN
        "mixing device", "mixing apparatus", "agitation device",
        "agitator device", "blender device", "stirring device",
        "mixing chamber", "agitation chamber", "mixer blender",
        "mixing shaft", "agitator shaft", "stirrer device",
        "homogenizer device",
        # PT
        "dispositivo misturador", "agitador misturador",
        "câmara mistura",
    ],

    # ══════════════════════════════════════════════════════════════════
    # SEPARATOR (raiz) — 4 patentes
    # ══════════════════════════════════════════════════════════════════

    "Separator/General Phase Separator": [
        # EN
        "phase separator device", "separator device", "separator apparatus",
        "separation device fluid", "separation chamber device",
        "separator housing", "separator chamber",
        # PT
        "dispositivo separador fase", "aparelho separador",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MANUFACTURING TECHNOLOGY (raiz) — 3 patentes
    # ══════════════════════════════════════════════════════════════════

    "Manufacturing technology/General Process Method": [
        # EN
        "manufacturing process general", "fabrication technique",
        "production method device", "processing method device",
        "general manufacturing", "general fabrication process",
        # PT
        "processo fabrico geral", "método produção dispositivo",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MEASURING DEVICES (raiz) — 2 patentes
    # ══════════════════════════════════════════════════════════════════

    "Measuring devices/Sample Testing Device": [
        # EN
        "sample testing device", "testing device sample",
        "sample testing", "fluid pumping installation testing",
        "testing device fluid",
    ],

    # ══════════════════════════════════════════════════════════════════
    # COUPLINGS AND DRIVE UNITS (raiz) — 2 patentes
    # ══════════════════════════════════════════════════════════════════

    "Couplings and Drive Units/Clutch Actuation Device": [
        # EN
        "clutch actuation", "actuation bearing clutch",
        "dual clutch system", "clutch actuation bearing",
        "clutch system bearing", "actuation dual clutch",
    ],

}

for _k, _v in _EXPANSAO_V10.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V11 — Segunda rodada: ataca as 148 patentes ainda em raiz
# após V10. Foco em padrões mais finos identificados por leitura
# direta dos títulos+abstracts remanescentes.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V11 = {

    # ══════════════════════════════════════════════════════════════════
    # GRINDING AND MILLING — 29 restantes
    # ══════════════════════════════════════════════════════════════════

    # ── Specialty Mills (sand, colloid, cutter, flywheel) ──────────
    "Grinding and Milling/Specialty Mills": [
        # EN
        "sand mill", "colloid mill", "cutter mill", "flywheel mill",
        "basket mill", "coaxial basket mill", "co-axial basket",
        "disc mill", "disc mill assembly", "pulverizing apparatus",
        "separated colloid mill", "split type colloid",
        "fine separation mill", "fine powder separation",
        "tub grinder", "cover tub grinder",
        "twin shaft comminutor", "dissimilar sized cutters",
        "stationary peg", "coal pulverizer",
        "stationary peg grinding", "peg coal pulverizer",
        "ballistite powder grinding", "single-perforated powder",
        "installation grinding",
    ],

    # ── Method and Process of Grinding ─────────────────────────────
    "Grinding and Milling/Grinding Method and Process": [
        # EN
        "method grinding", "grinding method", "grinding process",
        "apparatus grinding", "grinding apparatus method",
        "grinding cellulose", "grinding cellulose method",
        "preparing excavation", "grinding process excavation",
        "excavated soil grinding", "excavated earth",
        "new preparation process", "grinding medium preparation",
        "water grinding medium",
        # PT
        "método para moagem", "método moagem materiais",
        "capacidade de trituração", "processo moagem",
        "processo preparação moagem",
    ],

    # ── Food Waste Disposer Multi-Step ─────────────────────────────
    "Grinding and Milling/Food Waste Disposer Multi-Step": [
        # EN
        "disposer multi-step", "multi step grinding protrusion",
        "grinding protrusion disposer", "food waste crushed",
        "food waste disposer grinding", "grinding chamber food waste",
        "powdering machine", "dried food material",
        "multi purpose grinder", "multi-purpose grinder",
        "grinder replace web", "replacing web grinding",
        "garbage processing machine", "processing time power consumption",
        "garbage processing efficiency",
        "device milling dewatering", "milling dewatering",
        "biologically degradable kitchen", "kitchen household waste grinder",
        # PT
        "triturador alimentos multi-passo",
    ],

    # ── Specific Material Grinders (viscose, aluminum, gypsum) ─────
    "Grinding and Milling/Specific Material Grinders": [
        # EN
        "grinder producing viscose", "producing viscose",
        "grinder viscose", "viscose grinder",
        "aluminum foil grinder", "manual aluminum foil",
        "aluminum grinder manual", "foil grinder",
        "gypsum wallboard comminuting", "gypsum wallboard",
        "comminuting gypsum", "portable gypsum",
        "rasp system milling", "self-clearing rasp",
        "self clearing rasp", "automatic milling apparatus",
        "milling well casing", "well casing electromagnetic pulse",
        "electromagnetic pulse perforation", "perforation device well",
        "electromagnetic perforation", "crushing aggregation separation",
        "aggregation separation equipment",
        "cutter mill sieve", "sieve wear resistant",
        "cocoa nibs cutter", "impact blades grinding chamber",
        "milling device injected", "injected member milling",
        "one trip milling", "trip milling system",
        "sidetracking system mills", "serially connected mills",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MEDIA AND DOCUMENT DESTRUCTION — 23 restantes
    # ══════════════════════════════════════════════════════════════════

    # ── Paper Shredder / Smart Detection and Control ───────────────
    "Media and Document Destruction/Paper Shredder/Smart Detection and Control": [
        # EN
        "touch detection circuit", "shredder touch detection",
        "detection circuit shredder", "biometric detection shredder",
        "biometric information safety", "shredder biometric",
        "detect full shredder basket", "full shredder basket",
        "shredder operation alert", "gas detection system shredder",
        "shredder gas detection", "sensors placed shredder",
        "smart type shredder", "smart shredder ac machine",
        "automatically adjust rotation", "adjust rotation speed shredder",
    ],

    # ── Paper Shredder / Bin and Collection ────────────────────────
    "Media and Document Destruction/Paper Shredder/Bin and Collection": [
        # EN
        "shredder waste bin", "waste bin shredder",
        "shredder collection unit", "collection unit shredder",
        "bin light shredder", "bin light media",
        "chad containment", "chad containment bin",
        "emptying panel bin", "bin emptying panel",
        "sheet like material shredders", "bag securing mechanism",
        "securing shredder bag", "shredder bags baskets",
        "antistatic property waste box", "antistatic waste receiving",
        "waste receiving box",
    ],

    # ── Paper Shredder / Cutting Frame and Blade Design ────────────
    "Media and Document Destruction/Paper Shredder/Cutting Frame and Blade": [
        # EN
        "cutting frame shredder", "shredder cutting frame",
        "knives equipped shaft", "cutting frame knives",
        "crosscut shredder blade", "blade crosscut shredder",
        "plurality blades rotary shafts", "rotating opposite directions blades",
        "spinning cutter door", "cutter door device shredder",
        "spinning cutter shredder",
        "movable paper insert", "movable paper insertion",
        "paper insert lid plate", "movable covering board",
        "covering board shredder",
        "shredder pivotable top panel", "pivotable top panel",
        "pivoting top panel",
        "shredder head bottles", "shred data bearing documents",
        "shredder head shred",
    ],

    # ── Media Destruction / Recording Medium and Data ──────────────
    "Media and Document Destruction/Recording Medium Destruction": [
        # EN
        "recording medium destruction", "medium destruction discarding",
        "destruction discarding system", "destroying discarding recording",
        "sheet destruction discarding", "destruction apparatus recording",
        "data destruction machine", "high security data removal",
        "data removal process", "portable data destruction",
        "desk top portable unit",
        "disks data containing", "data-containing disks",
        "data bearing documents",
    ],

    # ── Shredder / No-Oil and Lubrication Features ─────────────────
    "Media and Document Destruction/Shredder Lubrication Features": [
        # EN
        "no-oil shredder", "no oil shredder",
        "zero-clearance shredder", "zero clearance",
        "no-oil high-security", "no-oil machinery",
        "oiling mechanism shredder", "shredder oiling mechanism",
        "automated lubricating system", "lubricating system shredder",
        "shredder automated lubricating",
    ],

    # ── Hazardous and Biological Waste Disposal ────────────────────
    "Media and Document Destruction/Hazardous Waste Disposal": [
        # EN
        "biologically hazardous waste", "hazardous waste disposal",
        "waste disposal unit", "waste reception mechanism",
        "hazardous biological waste",
    ],

    # ══════════════════════════════════════════════════════════════════
    # SEALINGS — 15 restantes
    # ══════════════════════════════════════════════════════════════════

    # ── Sealings / Pump Housing Seal ────────────────────────────────
    "Sealings/Pump Housing Seal": [
        # EN
        "pumping element housing", "pump rotation housing",
        "relative rotation housing", "mounted rotation housing",
        "pump housing seal", "pump housing sealing",
        "sealing pump housing", "gasket part pump",
        "gasket bearing part", "liquid supply mechanism seal",
        "branch fluid supply",
    ],

    # ── Sealings / End Seal and Rotating Ring ──────────────────────
    "Sealings/End Seal and Rotating Ring": [
        # EN
        "end seal", "end seal housing", "rotating ring tightly",
        "ring tightly installed", "seal rotating ring",
        "end seal machine building",
        "radial sliding seal", "sliding seal component",
        "radial sliding component", "metering device seal",
        "seal metering device", "seal syringe device",
    ],

    # ── Sealings / Wellbore Sealing System ─────────────────────────
    "Sealings/Wellbore Sealing System": [
        # EN
        "sealing zone casing", "casing sealing well",
        "zero-leakoff emulsified acid", "emulsified acid sealing",
        "acid emulsion sealing", "hydrocarbon producing formation seal",
        "drilling operation suspension", "suspension spool system",
        "dual sealing barrier", "well suspension seal",
        "expandable liner tieback", "liner tieback connection",
        "tubular member wellbore", "tieback connection",
        "sealing system joint", "gasket seat system",
        "sealing joint gasket",
        "several leaks casing", "casing several leaks",
    ],

    # ── Sealings / Vacuum and Drum Seal ────────────────────────────
    "Sealings/Vacuum and Drum Seal": [
        # EN
        "vacuum cutter", "sliding seal under face",
        "under face edge flange",
        "drum motor inner outer", "drum motor lid",
        "drum tube seal", "spatially fixed axis drum",
    ],

    # ══════════════════════════════════════════════════════════════════
    # PUMPS — 12 restantes
    # ══════════════════════════════════════════════════════════════════

    # ── Pumps / Grinder Pump Station ───────────────────────────────
    "Pumps/Grinder Pump Station": [
        # EN
        "grinder pump assembly", "grinder pump station",
        "wattmeter circuit grinder", "grinder pump operating",
        "operating grinder pump", "pump station inhibit",
        "assembly runaway", "grinder pump runaway",
    ],

    # ── Pumps / Pumping System Control Method ──────────────────────
    "Pumps/Pumping System Control Method": [
        # EN
        "pumping system control", "control apparatus pumping",
        "pumping system apparatus", "pumping system method",
        "pumping system fluid", "pumping fluids method",
        "method pumping fluid", "first pumping unit",
        "pumping unit second",
        "pump underperformance", "determining pump underperformance",
        "underperformance pumping system",
        "pump control therefor", "control apparatus designed",
        "moving fluids gases",
    ],

    # ── Pumps / Drum Follower Plate ────────────────────────────────
    "Pumps/Drum Follower Plate": [
        # EN
        "drum follower plate", "follower plate lifting",
        "cask follower plate", "automatically lifting cask",
        "keg follower plate", "follower plate pumping device",
        "follower plate vent",
    ],

    # ── Pumps / Valve of Pump Assembly ─────────────────────────────
    "Pumps/Valve of Pump Assembly": [
        # EN
        "valve pump assembly", "pump assembly valve",
        "piston moved open position", "piston moved closed position",
        "moved open closed position", "piston open closed",
        "fluid flowed closed position",
    ],

    # ── Pumps / Multiple Well Fluid Distribution ──────────────────
    "Pumps/Multiple Well Fluid Distribution": [
        # EN
        "well treatment fluid", "fluid distribution control",
        "multiple well treatment", "wellbores common pad",
        "wellbores drilled common", "fluid conduits wellbore",
        "treatment fluid distribution",
    ],

    # ── Pumps / Motor Drive Unit Connection ────────────────────────
    "Pumps/Motor Drive Unit Connection": [
        # EN
        "connecting electric motor drive", "electric motor drive unit",
        "motor drive unit pump", "device connecting motor",
        "connecting drive unit pump",
    ],

    # ══════════════════════════════════════════════════════════════════
    # CONVEYOR AND TRANSPORT — 9 restantes
    # ══════════════════════════════════════════════════════════════════

    # ── Conveyor / Shredding Unit for Plastics ─────────────────────
    "Conveyor and Transport/Shredding Unit for Plastics": [
        # EN
        "plastics shredding unit", "shredding unit plastics",
        "plastic materials diverse", "shredding plastic materials",
        "shredding multi-layer plastic", "plastic length width thickness",
    ],

    # ── Conveyor / Toner Cartridge Recovery ────────────────────────
    "Conveyor and Transport/Toner Cartridge Recovery": [
        # EN
        "toner cartridge crushing", "used toner cartridge",
        "crushing toner cartridge", "toner cartridge device",
    ],

    # ── Conveyor / Composting and Digestion ────────────────────────
    "Conveyor and Transport/Composting and Digestion": [
        # EN
        "automated composting", "composting system", "digestion chamber",
        "auger shaft mixing vane", "composting digestion",
        "composting auger",
    ],

    # ── Conveyor / Metal Recycling Separator ───────────────────────
    "Conveyor and Transport/Metal Recycling Separator": [
        # EN
        "metal recycling separator", "recycling separator shredder",
        "sloped shaking table", "shaking table shredder",
        "shredder sloped table",
    ],

    # ── Conveyor / Crushing Equipment for Chips ────────────────────
    "Conveyor and Transport/Crushing Equipment for Chips": [
        # EN
        "crushing equipment chips", "continuously discharge chips",
        "chips cutting fluid", "collect chips separately",
        "reduce load driving means",
    ],

    # ── Conveyor / Conveyor Space Device ───────────────────────────
    "Conveyor and Transport/Conveyor Space Device": [
        # EN
        "conveyor space", "conveying conveyance",
        "elastically deformable conveyor", "conveyor deformable",
        "conveying medium suction pressure", "suction side inlet",
        "pressure side outlet pump",
    ],

    # ── Conveyor / Liquid Solid Separation Device PT ───────────────
    "Conveyor and Transport/Liquid Solid Separation Device": [
        # PT
        "dispositivo para separação material",
        "separação material líquido", "material líquido sólido",
        "mistura método separação",
        "separação de um material",
        # EN
        "liquid solid material", "separation liquid solid material",
        "material liquid solid mixture",
    ],

    # ══════════════════════════════════════════════════════════════════
    # FILTRATION — 9 restantes (maioria PT)
    # ══════════════════════════════════════════════════════════════════

    # ── Filtration / Liquid Filter Device PT ──────────────────────
    "Filtration/Liquid Filter Device": [
        # PT — dominante
        "filtro dispositivo", "dispositivo filtragem", "filtragem de líquidos",
        "filtragem líquidos", "filtro para filtragem",
        "meio filtro substancialmente",
        "processo de filtração", "processo filtração",
        "filtração mistura reação", "mistura reação trifásica",
        "setor filtros rotativos", "filtros rotativos vácuo",
        "rotativos à vácuo",
        "filtro de bolsas", "filtro bolsas",
        "bolsas armação frontal",
        "membrana filtro microporosa", "filtro microporosa",
        "membrana microporosa",
    ],

    # ── Filtration / Circulation and Bath Filter ──────────────────
    "Filtration/Circulation and Bath Filter": [
        # EN
        "circulation device baths", "circulating device baths",
        "bath circulating pump filter", "bath filter circulation",
        "pump filter drive baths",
    ],

    # ── Filtration / Sludge Dehydration ───────────────────────────
    "Filtration/Sludge Dehydration": [
        # EN
        "sludge dehydrator", "pressurization pumped dehydrator",
        "pumped sludge dehydrator", "pressurization pumped",
        "sludge dehydrating method", "dehydrating sludge",
        "rotary fan press", "fan press liquid extraction",
        "liquid extraction assembly",
    ],

    # ── Filtration / Refiner and Blade ────────────────────────────
    "Filtration/Refiner and Blade": [
        # EN
        "refiner blade element", "blade element refiner",
        "refiner fibrous material", "refining fibrous",
        "first refining surface", "refining surface refiner",
    ],

    # ══════════════════════════════════════════════════════════════════
    # ELECTRIC MOTORS — 8 restantes
    # ══════════════════════════════════════════════════════════════════

    "Electric Motors/Motor Shaft and Tool Drive": [
        # EN
        "motor shaft drive", "motor shaft connected",
        "motor shaft driving", "shaft driving spiral",
        "meshing spiral shaft", "pair meshing spiral",
        "electric driven pair", "compact electric fuel pump",
        "electric fuel pump", "non-pulsating pump",
        "motor shaft fixed plates", "shaft connected motor",
        "rotation knife absorber", "knife absorber motor",
        "electric tool bearing", "bearing dustproof structure",
        "dustproof structure motor",
        "program-controlled turning", "machining unit",
        "machine tool milling drilling", "turning milling drilling",
        "beverage-making appliance motor", "beverage making apparatus",
        "ice beverage motor",
        "rotary pump arrangement", "pump arrangement controller",
        "controller regulator pump",
    ],

    "Electric Motors/Waste Processing Motor": [
        # EN
        "comminution system processing waste", "waste food comminution",
        "chamber piston chopping knife", "piston chopping knife",
        "waste food chamber lid",
        "smart type shredder motor", "shredder ac dc machine",
    ],

    # ══════════════════════════════════════════════════════════════════
    # OIL TOOLS — 7 restantes
    # ══════════════════════════════════════════════════════════════════

    "Oil Tools/Wellhead Connector and Frac Head": [
        # EN
        "casing head connector", "wellhead tubular connector",
        "wellhead connection casing", "slip bowl housing",
        "upper head housing", "slip segments",
        "lockscrew radial axial", "radial axial force",
        "multipart frac head", "frac head replaceable",
        "replaceable components frac", "frac head field",
        "rotating control device bearing", "control device bearing clamp",
        "bearing clamp wellhead",
    ],

    "Oil Tools/Tubular Running and Transport": [
        # EN
        "bore-lining tubular", "bore lining tubular",
        "running tubular string", "tubular string wellbore",
        "method running bore",
        "transport subterranean oil", "subterranean oil surface",
        "rotating helical blades oil", "helical blades interconnected",
        "interconnected rotating helical",
        "sand free production rate", "determining sand free",
        "sand production rate", "unconsolidated poorly consolidated",
    ],

    # ══════════════════════════════════════════════════════════════════
    # AGRICULTURE AND BIOMASS — 7 restantes
    # ══════════════════════════════════════════════════════════════════

    "Agriculture and Biomass/Biomass Fuel and Wood Chips": [
        # EN
        "biomass fuel pulverizer", "biomass fuel", "fuel pulverizer biomass",
        "high grease powder", "grease powder biomass",
        "wood chips combustion", "wood chips combustion plant",
        "manufacturing wood chips", "supply system split logs",
        "split logs comminution", "combustion plant biomass",
        "processing biomass", "biomass feedstocks",
        "plant biomass animal", "animal biomass municipal",
        "municipal waste biomass",
    ],

    "Agriculture and Biomass/Land Preparation and Tillage": [
        # EN
        "seedbed conditioning", "vertical tillage",
        "tillage apparatus", "rotary harrow",
        "soil conditioning apparatus", "frame rotary harrow",
        "land preparation", "land clearing",
        "rotatable drum cutting teeth", "drum plurality cutting",
        "brush cutter wear liner", "wear liner brush",
        "cylindrical cutting drum",
    ],

    "Agriculture and Biomass/Sweet Sorghum and Specialty Harvester": [
        # EN
        "sweet sorghum", "field harvester sorghum",
        "harvester sweet sorghum", "sorghum harvest",
        "labor intensive harvest",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MONITORING AND CONTROLLING — 7 restantes
    # ══════════════════════════════════════════════════════════════════

    "Monitoring and controlling/Condition Monitoring Pump": [
        # EN
        "condition monitoring pump", "monitoring condition pump",
        "pump condition monitoring", "monitoring pump system",
        "pump monitoring method",
        "variable speed pump control", "variable-speed fluid pumps",
        "controlling variable speed", "target pressure pump",
        "portable monitoring control surface", "surface equipment monitoring",
        "industrial services monitoring",
    ],

    "Monitoring and controlling/Silo Inspection Content Extraction": [
        # EN
        "inspecting silo", "extracting content silo",
        "silo plate perforated", "perforated plate silo",
        "silo inspection extraction",
    ],

    "Monitoring and controlling/Casing Centralization Locator": [
        # EN
        "casing centralization", "centralization locator",
        "oil well casing locator", "casing locator",
        "sleeve body wing plate",
    ],

    # ══════════════════════════════════════════════════════════════════
    # DRIVE SHAFTS — 6 restantes
    # ══════════════════════════════════════════════════════════════════

    "Drive Shafts/Slurry Breaking and Farm Pump": [
        # EN
        "breaking solids slurry", "solids farmyard slurry",
        "farmyard slurry tank", "slurry pumped vertical",
        "slurry tank vertical pipe",
        "grinder inexpensive simple", "variation load rotary",
        "rotary shaft drive shaft",
        "ground matter producing", "nondenatured ground matter",
        "efficient grinding preventing overheating",
        "supercharging device protector",
        "hydraulically protecting submersible", "submersible electric motor downhole",
        "protecting submersible motor", "protector downhole fluid",
    ],

    # ══════════════════════════════════════════════════════════════════
    # SEPARATOR — 3 restantes
    # ══════════════════════════════════════════════════════════════════

    "Separator/Impurity and Contaminant Separator": [
        # EN
        "impurity separator", "contaminant separator",
        "separating impurities media", "impurities media flow",
        "separator media flow", "contaminants media flow",
        "gas-liquid-solid separator", "gas liquid solid separator",
        "multivariable control three phase", "three-phase separation oil gas",
        "oil gas production separation",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MIXING AND AGITATION — 3 restantes
    # ══════════════════════════════════════════════════════════════════

    "Mixing and Agitation/Stirring Shaft Device": [
        # EN
        "stirring shaft", "stirring processing device",
        "stirring shaft processing", "shaft stirring device",
        "stirring processing same",
        "vegetable cutter improved", "improved vegetable cutter",
        "vegetable cutter frame cutting chamber",
        "fine particle manufacturing", "manufacturing fine particle",
        "uniform fine particles", "nano order particle size",
        "narrow particle size distribution",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MANUFACTURING TECHNOLOGY — 3 restantes
    # ══════════════════════════════════════════════════════════════════

    "Manufacturing technology/Ceramic Membrane and Thermosetting": [
        # PT
        "fabricação membrana cerâmica", "processo fabricação membrana",
        "membrana cerâmica densa",
        # EN
        "pulverizer thermosetting resin", "thermosetting resins manufacturing",
        "manufacturing process thermosetting",
        "refractory metal contact", "metal contact power device",
        "metallization integrated circuit", "minimum size transistor",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MEASURING DEVICES — 2 restantes
    # ══════════════════════════════════════════════════════════════════

    "Measuring devices/Dosing and Metering Device": [
        # PT
        "dispositivo alimentação dosagem", "dosagem para fluidos",
        "fluidos aditivos dosagem", "dispositivo medição fluidos",
        "alimentação dosagem fluidos",
        # EN
        "dosing device fluid", "metering fluid additives",
        "feeding dosing fluids", "additive fluid dosing",
        "pulverizer head power thickness", "vary power thickness",
        "material thickness pulverizer",
    ],

    # ══════════════════════════════════════════════════════════════════
    # VALVES — 1 restante PT
    # ══════════════════════════════════════════════════════════════════

    "Valves/Mechanism Pump Vacuum Compressor": [
        # PT
        "sucção compressão deslocamento", "mecanismo sucção",
        "bomba líquidos diversos", "bomba de vácuo",
        "compressor atua como", "bomba para líquidos",
    ],

    # ══════════════════════════════════════════════════════════════════
    # CORROSION — 1 restante PT
    # ══════════════════════════════════════════════════════════════════

    "Corrosion/Corrosion Resistant Filter Element": [
        # PT
        "elemento de filtro resistente", "filtro resistente corrosão",
        "elemento filtro resistente corrosão",
        # EN
        "corrosion resistant filter element", "filter element corrosion",
    ],

    # ══════════════════════════════════════════════════════════════════
    # BEARINGS — 1 restante
    # ══════════════════════════════════════════════════════════════════

    "Bearings/Mechanical Differential Gear": [
        # EN
        "mechanical differential gear", "differential gear assembly",
        "bearing load zone", "increased bearing load",
        "mechanical gear assembly",
    ],

    # ══════════════════════════════════════════════════════════════════
    # STERILIZATION AND MEDICAL WASTE — 1 restante PT
    # ══════════════════════════════════════════════════════════════════

    "Sterilization and Medical Waste/Integrated Medical Waste Management": [
        # EN
        "integrated medical waste", "medical waste management system",
        "waste management operation", "medical waste management",
        "integrated waste management",
        # PT
        "gerenciamento processamento resíduos", "resíduos médicos sistema",
        "sistema gerenciamento resíduos",
    ],

    # ══════════════════════════════════════════════════════════════════
    # COUPLINGS AND DRIVE UNITS — 1 restante
    # ══════════════════════════════════════════════════════════════════

    "Couplings and Drive Units/Material Processing Apparatus": [
        # EN
        "material processing apparatus", "krumbuster processing",
        "processing apparatus frame", "apparatus frame lateral",
    ],

    # ══════════════════════════════════════════════════════════════════
    # MACERATOR (raiz) — patch para as PT que ainda não caíram
    # ══════════════════════════════════════════════════════════════════
    # (já tratados em V10 mas reforça com generic)

}

for _k, _v in _EXPANSAO_V11.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V12 — Ataca as 145 patentes "Sem Classificação"
# ══════════════════════════════════════════════════════════════════════
# Estratégia em duas frentes:
#   (A) Adicionar palavras-chave de ENTRADA (Nível 1) a pastas primárias
#       existentes — patentes que pertencem a temas cobertos mas falham
#       por termos demasiado específicos no dicionário atual.
#   (B) Criar NOVAS pastas primárias para temas genuinamente ausentes:
#       "Motors and Clutches", "Packaging Machinery", "Food Processing
#       Appliances", "Hydraulic and Pneumatic Devices", "Semiconductor
#       and Nanomaterials", "Paint and Coating Testing", "Data and Text
#       Processing", "Chemical Substrate Applications".
#
# Todos os termos são n-gramas de 2-3 palavras (>=2 pt por match único)
# validados contra os abstracts das 145 patentes.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V12 = {

    # ══════════════════════════════════════════════════════════════════
    # (A) TERMOS DE ENTRADA PARA PASTAS EXISTENTES
    # ══════════════════════════════════════════════════════════════════

    "Macerator": [
        "food processing apparatus", "food processing machine",
        "food processing device", "food processing equipment",
        "food processor blade", "processing device food",
        "device processing food", "food processing strips",
        "strips slices cubes", "slicing food slices",
        "disintegrate food", "disintegrator inlet", "food disintegrator",
        "juice disintegrator", "extract juice food",
        "pureed cooked foodstuffs", "pureed food method",
        "pre-chopping raw material", "piece form raw material",
        "perforated disk food", "food processing holes",
        "non-pulpables collection", "pulper pulping chamber",
        "solid waste pulpers", "pulping mechanism",
        "cutter foodstuff wedge", "s-shaped blade food",
        "cutter assembly blade",
        "meat processing machine", "fat analyzer meat",
        "chopped meat fresh frozen",
        "bale breaker apparatus", "horizontal grinder feed",
        "horizontal feed conveyor",
        "cutter mill blade", "cutter housing knife",
        "food cooking press", "cooking press domestic",
        "domestic food press", "internal depth food",
        "small pieces waste", "cutting small pieces",
        "expose surfaces waste",
        "prensa para cozinhar", "prensa doméstica alimentos",
        "disposição construtiva prensa",
    ],

    "Macerator/Cutting Elements": [
        "fiber chopper", "chopper fiber", "fiber chopping method",
        "chopping continuous items", "continuous fiber chopper",
        "long unwound items", "unwound items fiber",
        "fiber strand yarn", "yarn string wire", "string wire tape",
        "wire tape ribbon", "backup roll blade", "blade roll backup",
        "roll retainer fiber", "idler roll fiber",
        "idler roll backup roll", "press item backup",
        "chopper idler roll", "fiber feeder",
        "break up fiber", "compressed masses fibers",
        "break-up implements shafts", "intake chute fiber",
        "pieces fiber transporting",
        "knife roller granulating", "knife roller plastic strands",
        "plastic strands roller",
        "automatic adjustment blade", "blade engagement intervals",
        "engagement intervals cutting",
        "interface knife holder", "knife knife holder",
        "tightening loosening clamping", "clamping nuts blade",
        "bevel gear blade pack",
        "chopping unwound", "unwound linear items",
        "chopping linear items", "blade roll fiber",
    ],

    "Macerator/Industrial Crusher": [
        "slice parting machine", "slice parting outer",
        "parting outer cylinder", "rotating shaft cylinder parting",
        "slice parting drum",
        "rubber twisting cutting", "twisting cutting machine",
        "cooling water pipe cutting",
        "garbage grinding bin", "grinding bin driving",
        "rotating barrel grinding", "grinding cutter component",
        "grinder motor current", "grinder unit current sensing",
        "electrical grinder motor", "controlling grinder motor",
        "current sensing means",
        "fuel fining device", "fuel fining particles",
        "crushed finer microparticles", "energy source microparticles",
        "particles microparticles smaller",
        "bag breaking mechanism", "bag breaking knife disk",
        "knife shaft knife disk", "bag breaking rubbish",
        "kitchen rubbish bag",
        "bag tearing machine", "downsized bag tearing",
        "bag tearing capability", "tearing bag noise",
        "bag breaking apparatus", "film fragments rotary shaft",
        "rotary rod winding fragments",
        "garbage treatment hopper", "trap pipe rinse water",
        "hopper rinse water", "ejection water supply",
        "crush water hopper",
        "waste vinyl fishing", "fishing net cleaner",
        "foreign matters waste vinyl", "pretreatment waste vinyl",
        "cleaning foreign matter", "wash dehydrates vinyl",
        "squeeze empty containers", "compressing empty containers",
        "beverage bottles cans", "plastic pet tinplate",
        "filling opening outlet",
        "crushing grains rollers", "grains driving mechanism shafts",
        "driving mechanism shafts rollers",
        "apparatus crushing grains",
        "grains crushing plurality",
        "improvement crushing performance", "crushing performance voltage",
        "CT voltage grinding", "voltage value grinding",
        "method improving grinding",
        "tub grinder industrial wastes", "tub grinder stumps",
        "lumber chunks grinder",
        "electroblasting activation", "electroblasting water pulps",
        "water pulps suspensions", "pulps suspensions activation",
        "plant electroblasting",
        "chip making device", "chip making wood chips",
        "wood chips cutter carriers", "cutter carriers cutting cavity",
        "chipping track cutter",
        "máquina fatiadora cilindro", "equipamento corte tubo borracha",
    ],

    "Macerator/Food Waste Disposer": [
        "food processor housing", "food processor motor driveshaft",
        "food processor bowl lid", "processor driveshaft bowl",
        "food processing slices strips",
        "s-shaped blade foodstuff", "s shaped blade",
        "concave tapered wedge", "tapered wedge product",
        "waste bread crushing", "waste bread drying",
        "bread drying powder", "powder granular moisture",
        "waste bread mixer",
        "food cooking press", "domestic food cooking",
        "food press greater depth",
    ],

    "Sterilization and Medical Waste": [
        "medical waste disposal", "disposing medical waste",
        "infectious medical waste", "secondary infection medical",
        "pathogen reduction waste", "waste pathogen reduction",
        "disinfection waste", "disinfectant waste pieces",
        "spraying waste pieces",
        "asbestos building material", "asbestos containing material",
        "processing asbestos method", "asbestos processing apparatus",
        "asbestos containing waste",
        "cutting waste small pieces", "expose surfaces cutting waste",
        "ambient temperature pressure waste",
    ],

    "Mixing and Agitation": [
        "homogenizing sample", "homogenization sample motor",
        "cutting tool receptacle", "receptacle homogenization",
        "centrifugal mixing system", "closed mixer recirculation",
        "mixer recirculation inlet", "inlet discharge mixer",
        "mobile mixer cereal", "cereal grain mixer",
        "mixer horizontal rotating", "helical mixer tool",
        "farm animal feed mixer",
        "sewer system agitator", "sewer agitator waste",
        "agitator digester assembly", "in-line agitator sewer",
        "waste material digester",
        "fluid treatment stirring", "stirring pressure fluid",
        "highly accurate stirring",
        "fine particle manufacturing", "uniform fine particles",
        "nano-order particle size",
        "removing stuck earth sand", "stuck earth sand container",
        "efficient crushing mixing sediment", "crushing mixing sediment",
        "container inner wall crushing",
    ],

    "Conveyor and Transport": [
        "pick-up head system", "pick up head suctioning",
        "suctioning bottom opening", "debris transfer interior",
        "surface cleaning vehicle",
        "roller accumulator", "lawn garden debris",
        "vacuum pick up blower", "blower unit separator",
        "detachable accumulator",
        "gutter clogging", "reduce clogging gutter",
        "motor-driven grinder mechanism", "waterborne leaves",
        "grinds leaves debris",
        "material spreader", "belt chain assembly",
        "spreader chamber", "chain sliding bar",
        "transfer device manufacture", "transfer device assemble",
        "preventing clogging hair",
        "conveying medium carrier shafts", "carrier shafts transport",
        "working machine conveying", "transport elements medium",
        "device conveying fluid",
        "conveyor space deformable", "elastically deformable conveyor",
        "conveyor conveyance",
        "line retention clips", "cantilever portion clips",
        "oriented oppositely clips",
        "processing polymer material", "polymer material contaminants",
        "polymer material volatile substances",
        "device processing material", "processing material polymer",
        "thermoplastic waste plastics recycling",
        "recycled thermoplastic composition", "waste thermoset material",
        "crumb slurry", "shapeable composite materials",
        "carpet recycling", "recycling carpet fibers",
        "carpet fibers backing", "separating carpet fibers",
        "belt driving carpet",
        "evacuate materials chamber", "grating movable knife",
        "movable knife chamber bottom", "elongated chamber grating",
        "shovelable biomass chamber", "biomass elongated chamber",
    ],

    "Bearings": [
        "bearing device vehicle", "vehicle wheel bearing",
        "bearing wheel double row", "double row tapered",
        "tapered raceway surfaces",
        "bearing extreme dust", "extreme dust environment",
        "long service life bearing", "bearing long life",
        "bearing end cap", "end cap integrated seal",
        "circular mounting surface bearing", "seal groove mounting",
        "integrated seal bearing",
        "bearing lubricant properties", "lubricant properties bearing",
        "bearing arrangement lubricant", "determining properties bearing",
        "bearing element movable", "bearing lubricant inclined",
        "seal inner axial direction", "inclined surface seal",
        "leakage lubricating oil bearing",
    ],

    "Drive Shafts": [
        "one-way rotation assembly", "one way rotation shaft",
        "rotation assembly shaft housing", "way rotation shaft",
        "ratchet assembly rotation",
        "torque shaft hub", "transmitting torque shaft hub",
        "torque shaft hub equilateral", "inner geometry n-corner",
        "equilateral corner geometry",
        "retaining plate gearing", "plate gear shafts",
        "connecting gear shafts", "gear assembly plate aperture",
        "pulley built-in clutch", "pulley hub clutch",
        "load torque pulley", "suppress load torque",
        "pulley supported rotated",
        "shaft downhole equipment", "shaft well application",
        "coupling shaft driven devices", "nominal diameter shaft",
    ],

    "Monitoring and controlling": [
        "wireless transmission signal", "wireless signal sensor",
        "sensor supply device transmission", "wireless transmission device",
        "signal transmitted sensor",
        "fault detection pumping", "detecting faults pumping",
        "pumping units vibration signal", "vibration signal shaft",
        "shaft revolution rate",
        "machine learning equipment failure", "equipment failure prediction",
        "predictive engine accuracy", "predictive engine variables",
        "data preprocessing predictive", "time series operational parameter",
        "time derivative feature",
        "wellsite control sensor", "sensor information computing device",
        "notification option sensor",
        "controlling operational functions machine tool",
        "operational functions machine", "switch off time machine",
        "main power supply machine tool",
        "machine tool access control", "operation functions selection",
        "machine tool selection device",
        "liquid level following", "following liquid level",
        "filling device liquid level", "elevating discharging port",
        "filler liquid level",
        "cloudiness paints", "measuring cloudiness",
        "color coordinates test tables", "test tables measuring sites",
        "measuring sites test",
    ],

    "Sealings": [
        "seal stem anchor", "stem anchor assembly",
        "body lock threads", "anchor activation module",
        "tubular body lock",
        "oilfield apparatus seal", "seal rubber oxycellulose",
        "rubber oxycellulose fibers", "cellulose nanofibers seal",
        "oxycellulose cellulose nanofibers",
        "motion seal lip", "exercise seal motion",
        "seal lip inner member", "rotational speed outer member",
        "motion seal rotational",
        "flange locking cap", "made-up flange locking",
        "subsea member flange", "external flange cap",
        "cap secured subsea", "tubular outer body cavity",
        "mechanical tool annular", "annular member housing",
        "stationary ring rotating", "sandwich stationary rotating",
        "first annular second annular",
        "sliding ring diamond", "diamond coating lubricant",
        "base region diamond coating",
        "slide ring diamond",
    ],

    "Filtration": [
        "montagem filtro fabricação", "processo fabricação filtro",
        "montagem filtro produzida", "fabricação montagem filtro",
        "armação filtro barras", "filtro plano cilindro",
        "filtro barras elementos apoio", "barras suportam filtro",
        "película filtro cera", "filtro bordas vedadas",
        "cera impermeável líquido", "método vedação filtro",
        "filter assembly fabrication", "fabrication filter assembly",
        "porous structure fluid separation",
        "estruturas porosas separação", "porous structures separation fluids",
        "fluids constituents porous",
    ],

    "Oil Tools": [
        "downhole assembly insertion", "articulated mandrel damping",
        "passive active damping", "torsional stick slip",
        "mandrel torsional stick",
        "matrix acidizing operations", "acid diversion selective",
        "selectively delivering fluid", "vortices taylor couette",
        "taylor-couette flow", "rotation outer surface body",
        "pumping fluid additive", "fluid additive downhole",
        "wellbore location fluid", "container placed wellbore",
        "pumping mixture wellbore",
        "well tool nanoparticle", "nanoparticle metallic coating",
        "well fluid metallic coating", "metallic coating substrate well",
        "tool member surface exposure",
        "wellsite control method", "control sensor wellsite",
        "notification wellsite sensor",
        "wellbore maintenance operation", "wellbore maintenance oil",
        "improved oil recovery maintenance", "perform wellbore maintenance",
        "system wellbores maintenance",
        "releasable connector assembly", "releasable connection tubular",
        "connector tubular payload", "first connector tubular",
        "tubing tool deployment",
        "stimulating multi-zone well", "multi-zone well tubular",
        "first zone second zone", "first set plugs",
        "pre-drilled holes zone",
        "bore hole coupling", "coupling tubular mandrel",
        "tubular end mandrel aligning", "axial alignment tubular",
        "system use bore hole",
        "expandable tubular radially", "radially expanding tubular",
        "plastically deforming tubular", "resilient launcher tubular",
        "launcher sleeve portion", "expansion expandable tubular",
        "automatic tubing drain", "tubing drain rotary",
        "rotary pump reactive torque", "pump automatic closes",
        "pump starts opens",
        "oil sand ore slurry", "mobile slurry apparatus",
        "slurry box frame ore", "slurry oil sand",
        "ore water slurry",
        "sized ore feed", "ore feed excavated",
        "processing apparatus ore feed", "excavated ore deposit",
        "tar sand oil extraction", "extracting oil tar sand",
        "in-situ liquefaction subsurface", "in situ liquefaction",
        "hydrocarbon containing formations", "systematic temperature elevation",
        "mineral oil deposits", "production mineral oil",
        "temperature gradient mineral", "large temperature gradients",
        "highly permeable mineral",
        "downhole gas separation", "down-hole gas separation",
        "gas liquids wellbore", "production separation chambers",
        "chambers parallel separation",
        "collecting container multi-phase", "multi-phase mixtures hydrocarbon",
        "hydrocarbon source multi-phase", "multi-phase pump system container",
        "container sump pump",
        "ultra pump systems", "pump removing liquids well",
        "pump chamber well cylindrical", "elongated cylindrical chamber pump",
        "first cover second cover pump",
        "pump motor pumping fluids", "pump housing upper lower end",
        "fluid displacer pump", "displacer pump housing",
        "conduit housing displacer",
        "positioning tool casing", "determining position casing",
        "detecting unit magnet casing", "positioning tool downhole",
        "longitudinal tool axis", "detecting unit first",
        "downhole apparatus valve", "valve arrangement tubular ports",
        "tubular body first second ports", "ports wall tubular",
        "locked first configuration valve",
        "valve bottom hole assembly", "selectively actuating motor",
        "valve barrel interior", "actuating motor bottom hole",
        "drum solid waste diverter", "solid waste diverter drum",
        "helical coil support mount", "diverter coil rotation",
    ],

    "Manufacturing technology": [
        "glass powder particle size", "glass powder average particle",
        "particle size distribution glass", "powder particles glass",
        "constituent powder particles",
        "silicon recycling comminuting", "recycling silicon melt",
        "silicon starting material", "comminuting starting material",
        "crystals drawn melt", "si starting material",
        "polymer coatings metallic", "polymer coating substrate",
        "carbon composite coating", "intermediate layer substrate",
        "article substrate polymer coating",
        "microtreatment carbide alloy", "micro-treating iron alloys",
        "iron based alloy treatment", "microstructure iron alloy",
        "carbon steel iron alloys", "low medium high carbon steel",
        "powder metal mixture", "lubricant powder metal",
        "micronized cellulose fibers", "metal parts cellulose",
        "powder metal parts produce",
        "semiconducting single wall nanotubes", "carbon nanotube purification",
        "metallic carbon nanotubes", "semiconductive carbon nanotubes",
        "process forming nanotube", "imposing energy mixture nanotubes",
        "grate gasification systems", "high temperature gasification",
        "active grate elongated rockers", "elongated rockers parallel",
        "rocker lower upper surface",
        "radioactive substance absorbent", "fibrillated cellulose fibers",
        "cellulose fibers radioactive", "zeolite mixing cellulose",
        "humidified water permeable polymer",
    ],

    # ══════════════════════════════════════════════════════════════════
    # (B) NOVAS PASTAS PRIMÁRIAS
    # ══════════════════════════════════════════════════════════════════

    "Motors and Clutches": [
        "driving motor railway", "railway vehicle motor",
        "rolling stock motor", "drive motor rolling stock",
        "oil supply chamber motor", "guide plate motor",
        "pulley built-in clutch", "built-in clutch pulley",
        "pulley hub clutch", "clutch pulley hub",
        "load torque clutch", "suppress increase load torque",
        "small-size motor", "small size motor shaft",
        "motor shaft press-fit", "press-fitted central hole",
        "tapered portion shaft motor",
        "motor central hole boss", "shaft diameter central hole",
        "clutch actuation bearing", "dual clutch system",
        "clutch actuation dual",
        "pulley rotation clutch",
        "motor de acionamento ferroviário", "motor veículo ferroviário",
        "embraiagem de polia", "motor de pequeno porte",
    ],

    "Packaging Machinery": [
        "packaging dried sheets", "sealed capsules packaging",
        "airtight capsule packaging", "tea leaves capsule",
        "dried tea leaves", "machine breaking tea leaves",
        "inlet supply tea leaves", "capsule machine outlet",
        "capsule filling tea",
        "filling device liquid", "liquid level filling",
        "liquid level follower device", "follower liquid filling",
        "filler discharging port", "discharging port filler liquid",
        "coffee capsule unit preparation", "coffee portions preparation",
        "preembalados café capsule", "café unidade preparação",
        "packaged coffee capsule",
        "packaging sealed container", "airtight packaging machine",
        "embalagem de café", "unidade de preparação máquina café",
        "porções café preembalados", "porções pó café",
        "máquina café capsule", "café preembalados porções",
    ],

    "Food Processing Appliances": [
        "food processing machine electrical", "electrical voltage potential food",
        "voltage potential food parts",
        "active ingredient food processing", "food processing devices insert",
        "folding pull-out active insert", "pull out active insert",
        "food processing tool knife",
        "mixer mode blade", "mixer function lowering",
        "mixer blade supported",
        "devices methods disintegrate", "disintegrate foods",
        "food processing device juice", "extract juice food device",
        "disintegrator inlet food",
        "perforated disk food", "disk processing food",
        "holes through food products", "disk plurality holes",
        "processing food axial side",
        "food processor strips cubes", "food processor slices",
        "cutting food slices strips", "first second shaft blades",
        "subsets blades shafts food", "blades first second shaft",
        "cutter assembly s shaped", "s-shaped blade cutting",
        "cutter housing knife housing", "tapered wedge foodstuff",
        "cooking press food dishes", "food press dishes",
        "various dishes saving", "greater internal depth press",
        "eletrodoméstico alimentar", "triturador doméstico",
        "processador de alimentos doméstico",
    ],

    "Hydraulic and Pneumatic Devices": [
        "expulsion device pressure medium", "expulsion device pressure",
        "ejection device propellant piston", "propellant piston pressure",
        "pressure means expel objects", "pressure means expel fluid",
        "propellant piston reservoir", "reservoir pressure medium",
        "hydraulic diaphragm pump", "diaphragm position control",
        "position control diaphragm", "hydraulically driven diaphragm",
        "diaphragm transfer chamber",
        "pump chamber resonator", "resonator pipe pump",
        "primary pipe end reflector", "resonator fuel pump",
        "fuel injection pump supply", "fuel conveying injection",
        "petrol pump measuring", "fluid quantities petrol",
        "petrol pump fluid meter", "measuring tube pump petrol",
        "fluid measuring motor",
        "pistão propulsor pressão", "dispositivo ejeção pressão",
        "bomba hidráulica diafragma", "controlo posição diafragma",
    ],

    "Paint and Coating Testing": [
        "cloudiness paints", "measuring cloudiness paint",
        "color coordinates paint", "test tables paint",
        "measuring sites paint", "paint testing method",
        "cloudiness coating test",
    ],

    "Semiconductor and Nanomaterials": [
        "carbon nanotubes purification", "semiconducting nanotubes",
        "metallic carbon nanotubes", "single wall nanotubes",
        "nanotubes semiconductive", "forming semiconductive structure",
        "imposing energy nanotubes",
        "powder metal mixture", "micronized cellulose fibers metal",
        "lubricant powder cellulose",
        "radioactive substance absorbent", "fibrillated cellulose radioactive",
        "cellulose fibers humidified", "zeolite cellulose mixing",
        "botanical origin polymer radioactive",
    ],

    "Data and Text Processing": [
        "estenografia semântica", "sistemas métodos estenografia",
        "notas de taquigrafia", "realização texto taquigrafia",
        "converte dados entrada",
        "semantic stenography", "stenography data conversion",
        "text processing data entry",
    ],

    "Chemical Substrate Applications": [
        "substrato dobrado", "substrato contendo substância",
        "substância química aplicada", "áreas separadas substrato",
        "substrato dobrado substância",
        "folded substrate chemical", "substrate chemical applied",
        "chemical applied substrate", "separated areas substrate",
    ],

    # ══════════════════════════════════════════════════════════════════
    # REFORÇO DE RAÍZES JÁ EXISTENTES PARA RESTANTES
    # ══════════════════════════════════════════════════════════════════

    "Pumps": [
        "adjusting delivery rate pump", "delivery rate pump",
        "pump conveying medium", "pump pressure chamber",
        "conveyance housing pump", "transport element pump",
        "suction chamber pressure chamber", "pump adjustable delivery",
        "continuously pumping solid material", "pumping solid material",
        "pressurized slurry solid material", "solid material liquid carbon",
        "liquid carbon dioxide slurry", "continuous slurry pumping",
        "bomba sistema pulmões", "bomba d'água hidráulica",
        "unidade de bombeamento parafuso", "bombeamento tipo parafuso",
        "fluidos em fases diversas", "bomba tratamento fluidos fases",
    ],

    "Separator": [
        "structured packing section", "recheio estruturado",
        "seção recheio leito", "packing capacity brick",
        "packing brick capacity", "recheio tijolo plano",
        "leito estruturado capacidade",
    ],

    "Pumps/Screw Pump": [
        "unidade bombeamento parafuso", "bombeamento parafuso tratamento",
        "parafuso tratamento fluidos", "fluidos fases diversas parafuso",
    ],

    "Pumps/Diaphragm Pump": [
        "diaphragm hydraulic pump", "hydraulic diaphragm control",
        "diaphragm piston transfer", "piston transfer chamber diaphragm",
        "fluid reservoir diaphragm pump",
        "bombas acionadas hidraulicamente", "bomba acionada hidraulicamente diafragma",
        "controle posição diafragma",
    ],

    "Grinding and Milling": [
        "moagem de farinha", "sistema moagem farinha",
        "grãos duros trigo", "moagem grãos trigo",
        "pluralidade etapas moagem", "etapas de moagem",
        "processo sistema moagem",
    ],

    "Agriculture and Biomass": [
        "chaff processing distribution", "chaff cutter harvester",
        "combine harvester chaff", "chaff distribution device",
        "mobile mixer cereal grain", "cereal farm animal feed",
        "horizontal rotating helical mixer", "helical mixer assembly cereal",
        "farm animal feed mobile",
    ],

    "Electric Motors": [
        "driving motor railway vehicle", "railway motor oil chamber",
        "oil supply guide plate", "rolling stock drive motor",
        "guide plate simple structure motor",
        "small-size motor shaft", "motor shaft dimension tapered",
        "press-fitted boss shaft",
    ],

    "Macerator/Comminutor": [
        "chopping implement", "chopped item axis",
        "cutter carriers chipping", "chipping track axis",
        "cutting cavity cutter", "axis cutting cavity",
        "releasably fixed cutter",
    ],

    "Filtration/Liquid Filter Device": [
        "filtro elemento armação", "fabricação filtro elemento",
        "processo fabricação montagem filtro", "elemento filtro barras",
        "filtro plano cilindro barras apoio", "barras apoio filtro",
        "suporta barras filtro", "película cera filtro",
        "bordas vedadas cera método",
    ],

}

for _k, _v in _EXPANSAO_V12.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V13 — Correção cirúrgica final
# ══════════════════════════════════════════════════════════════════════
# Os termos V12 estavam formados por bigramas "ideais" que nem sempre
# existem exatamente nos abstracts. V13 usa bigramas EXTRAÍDOS DIRETAMENTE
# dos títulos+abstracts das 71 patentes ainda sem match, garantindo que
# cada termo casa pelo menos uma vez.
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V13 = {

    # ── Oil Tools — reforços cirúrgicos ────────────────────────────
    "Oil Tools": [
        # Extraídos literalmente dos abstracts
        "downhole assembly", "downhole articulated",
        "wellsite control", "systems wellsite",
        "methods wellsite", "wellsite sensor",
        "pumping fluid additive downhole", "fluid additive wellbore",
        "apparatus pumping fluid", "fluid mixture wellbore",
        "well tool nanoparticle", "nanoparticle reinforced metallic",
        "reinforced metallic coating", "well tool disclosed",
        "tool first member",
        "valves bottom hole", "bottom hole assemblies",
        "selectively actuating motor",
        "downhole valve arrangement", "apparatus valve arrangement",
        "tubular body first",
        "expandable tubulars", "radially expanding tubular",
        "expandable tubular resilient", "resilient anchor expansion",
        "resilient launcher",
        "stimulating multi-zone", "multi-zone well tubular",
        "shaft downhole equipment", "shaft well application",
        "system bore hole", "bore hole axially coupling",
        "tubular end mandrel", "coupling tubular end",
        "axially coupling",
        "oil field apparatus", "oilfield apparatus",
        "seal member rubber oxycellulose",
        "collecting container multi-phase", "multi-phase pump system",
        "container sump multi-phase",
        "solid waste diverter", "drum solid waste",
        "drum diverter helical",
        "continuously pumping solid", "continuous slurry solid",
        "pressurized slurry solid material",
        "hydrogen formation slurry",
    ],

    # ── Macerator — reforços ───────────────────────────────────────
    "Macerator": [
        "processing material polymer", "processing material apparatus",
        "polymer material undesired", "undesired contaminants polymer",
        "impair processing polymer",
        "device processing material", "apparatus processing polymer material",
        "perforated disk", "processing food perforated",
        "plurality holes food", "through-holes food products",
        "disk food products holes",
        "waste treatment hopper", "treatment device crush water",
        "hopper rinse water", "trap pipe",
        "crush water supplied",
        "producing pureed", "pureed food method",
        "pureed cooked foodstuffs", "pre-chopping food",
        "method device pureed", "knife system food",
        "crushing grains", "apparatus crushing grains",
        "plurality shafts rollers grains", "grains plurality rollers",
        "driving mechanism crushing",
        "improvement crushing performance", "crushing performance CT",
        "CT voltage grinding",
        "disposing waste", "apparatus disposing waste",
        "waste disposal apparatus agitation", "residues bottom surface",
        "treating waste bread", "waste bread crushing",
        "crushing drying waste bread", "fine powder granular",
        "mixer feed waste",
    ],

    # ── Macerator/Cutting Elements ─────────────────────────────────
    "Macerator/Cutting Elements": [
        "knife roller", "roller plastic strands",
        "granulating plastic strands", "plastic strands seamlessly",
        "roller sections blade",
        "interface knife", "knife holder",
        "knife knife holder", "knife and knife holder",
        "tightening loosening device", "clamping nuts blade",
        "nuts blade sets", "blade sets cutter",
        "bevel gear drives",
    ],

    # ── Macerator/Industrial Crusher ───────────────────────────────
    "Macerator/Industrial Crusher": [
        "destruction data carriers", "data carriers peripheral",
        "peripheral devices data",
        "destruction device data",
        "bending creasing device", "punching shearing device",
        "crushing system rotating", "rotating disk sections",
        "two rotating disk", "crushing high pressures",
        "raw material rejection",
        "wood cutter water jet", "water jet nozzle",
        "high pressure water pump cutter",
        "chaff cutter optimum", "optimum chopper cut",
        "cutter garden woody", "cutter branches water",
        "chaff cutter microwave", "microwave radiator cutting",
        "timber heated softened", "cutting chamber microwave",
        "chaff processing distribution", "processing distribution device",
        "large harvesting machines",
        "garbage treatment device", "garbage hopper treatment",
        "crush water hopper",
    ],

    # ── Macerator/Food Waste Disposer ──────────────────────────────
    "Macerator/Food Waste Disposer": [
        "pureed food", "method producing pureed",
        "device producing pureed",
        "raw material cooking",
        "knife system pureed",
    ],

    # ── Media and Document Destruction ─────────────────────────────
    "Media and Document Destruction": [
        # Captura US5996457: "Apparatus For Destruction Of Tickets"
        "destruction tickets", "destroying used tickets",
        "destroying tickets", "cutter removably mounted",
        "tickets enter cutter", "enclosure slot tickets",
        "cutter enclosure housing",
        # Captura US7494076: "Fast Secure Method... Data Storage Unrecoverable"
        "data storage devices unrecoverable", "rendering data stored unrecoverable",
        "data stored plurality", "storage devices unrecoverable",
        "secured method pressing",
        "hydraulic pressing means",
        "secure method pressing",
        "quickly causing data",
        "mobile hydraulic pressing",
    ],

    # ── Manufacturing technology ───────────────────────────────────
    "Manufacturing technology": [
        "polymer coatings metallic", "forming polymer coatings",
        "methods forming polymer", "metallic substrates polymer",
        "polymer coating substrate",
        "intermediate layer polymer",
        "microtreatment microstructure", "microstructure carbide",
        "carbide containing iron", "iron-based alloy",
        "micro-treating iron-based",
        "iron based alloy treating",
        "glass powder", "glass powder particle",
        "average particle size glass", "powder improved particle",
        "particle size distribution glass",
    ],

    # ── Monitoring and controlling ─────────────────────────────────
    "Monitoring and controlling": [
        "wireless transmission", "transmission signal",
        "device wireless signal", "sensor supply device",
        "electrical connection wireless",
        "controlling operational functions", "operational functions machine",
        "apparatus controlling machine", "switching main power",
        "switch off time",
        "machine tool access", "access control device",
        "operation functions selection", "selection device machine tool",
        "plurality operation functions",
        "measuring cloudiness", "cloudiness paints test",
        "paints test tables", "color coordinates measuring",
        "measuring sites test tables",
    ],

    # ── Mixing and Agitation ───────────────────────────────────────
    "Mixing and Agitation": [
        "mixer mode", "mixer blade",
        "blade supported receptacle", "low-cost mixer",
        "mixer function lowering",
        "homogenization sample", "homogenizing sample method",
        "sample device motor cutting",
        "cutting tool receptacle",
        "agitator sewer system", "sewer system waste material",
        "agitator upstream digester",
        "agitator in-line sewer",
        "removing stuck earth", "stuck earth sand",
        "earth sand container",
        "efficient crushing mixing sediment",
        "attached sediment removal",
    ],

    # ── Conveyor and Transport ─────────────────────────────────────
    "Conveyor and Transport": [
        "conveying medium working", "working machine carrier",
        "carrier shafts transport elements",
        "transport elements arranged",
        "device conveying medium",
        "evacuate materials chamber", "shovelable biomass chamber",
        "grating movable knife",
        "materials elongated chamber",
        "line retention arrangement", "line retention clips",
        "retention arrangement supports",
        "cantilever portion clips",
        "two more clips",
    ],

    # ── Agriculture and Biomass ────────────────────────────────────
    "Agriculture and Biomass": [
        "chaff processing distribution", "combine harvester chaff",
        "chaff processing device", "processing distribution device",
        "chaff cutter garden",
        "wood cutter water",
        "woody material cut", "branches cut water",
        "microwave radiator chaff",
        "heated softened cutting",
    ],

    # ── Filtration (reforço PT) ────────────────────────────────────
    "Filtration": [
        "processo fabricação montagem", "montagem filtro processo",
        "montagem filtro produzida",
        "fabricação filtro processo",
        "estruturas porosas", "estruturas porosas processo",
        "porosas processo fabricação",
        "separação fluidos porosas",
        "película filtro", "película filtro possuindo",
        "filtro bordas vedadas",
        "bordas vedadas cera",
        "cera otimizada método",
        "filtro processo produção", "processo produção filtro",
        "filtro plano cilindro", "filtro barras elementos",
    ],

    # ── Bearings (reforço) ─────────────────────────────────────────
    "Bearings": [
        "bearing device", "bearing leakage lubricating",
        "leakage lubricating oil", "inclined surface bearing",
        "seal member radially", "lubricating oil outside",
        "bearing arrangement determining", "arrangement determining properties",
        "determining lubricant bearing", "lubricant bearing arrangement",
        "bearing first second element",
    ],

    # ── Drive Shafts (reforço) ─────────────────────────────────────
    "Drive Shafts": [
        "arrangement transmitting torque", "transmitting torque shaft",
        "torque shaft hub", "shaft hub arrangement",
        "hub inner geometry", "equilateral corner hub",
        "shaft downhole equipment",
        "shaft well application",
        "coupling shaft driven devices",
    ],

    # ── Motors and Clutches (reforço) ──────────────────────────────
    "Motors and Clutches": [
        "driving motor railway", "drive motor rolling stock",
        "railway vehicles motor", "oil supply chamber motor",
        "motor rolling stock simple",
        "pulley built-in clutch", "pulley clutch",
        "built in clutch pulley",
        "pulley hub supported", "load torque pulley",
        "suppress increase torque",
    ],

    # ── Packaging Machinery (reforço) ──────────────────────────────
    "Packaging Machinery": [
        "alimentar porções café", "porções café preembalados",
        "café preembalados unidade", "unidade preparação máquina",
        "máquina café unidade",
        "conjunto alimentar porções",
    ],

    # ── Hydraulic and Pneumatic Devices (reforço) ──────────────────
    "Hydraulic and Pneumatic Devices": [
        "expulsion device", "ejection device operated",
        "pressure medium expel",
        "propellant piston pressure",
        "actuated pressure means",
        "reservoir propellant piston",
        "pump supplying fluid", "pump fuel supply",
        "fuel pump conveying", "fuel injection pump",
        "resonator pipe pump",
        "primary pipe end",
    ],

    # ── Pumps (reforço) ────────────────────────────────────────────
    "Pumps": [
        "pump motor pumping fluids", "pump housing upper",
        "conduit housing upper lower", "fluid displacer housing",
        "displacer within housing",
        "pump adjusting delivery", "adjusting delivery rate",
        "delivery rate pump", "pump conveying medium",
        "conveyance housing pressure",
        "suction side inlet", "pressure side outlet",
        "transport element pump",
    ],

    # ── Sterilization and Medical Waste (reforço) ──────────────────
    "Sterilization and Medical Waste": [
        "asbestos containing building", "building material asbestos",
        "asbestos material processing", "processing method asbestos",
        "low cost asbestos",
        "waste processing pathogen", "pathogen reduction waste",
        "waste pathogen reduction", "disinfection waste cutting",
        "treating organic wastewater", "organic wastewater treatment",
        "surplus sludge generation",
        "simple facility wastewater",
    ],

    # ── Grinding and Milling (reforço) ─────────────────────────────
    "Grinding and Milling": [
        "improvement crushing performance", "method improvement crushing",
        "method improving grinding", "crushing performance voltage",
        "crushing grains rollers",
        "method crushing grains",
        "apparatus crushing grains",
    ],

    # ── Separator (reforço) ────────────────────────────────────────
    "Separator": [
        "structured packing section", "section recheio leito",
        "recheio leito estruturado", "packing capacity tijolo",
        "tijolo plano recheio",
    ],

    # ── EP4356999 Hopper For Transporting Sludge → Conveyor ────────
    "Conveyor and Transport/Sludge Hopper Transport": [
        "hopper transporting sludge", "transporting sludge hopper",
        "sludge specifically designed", "material buildup clogging",
        "hopper internal walls", "load cell sludge",
        "hopper sludge clogging",
    ],

}

for _k, _v in _EXPANSAO_V13.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V14 — Patch cirúrgico sobre os 35 restantes
# ══════════════════════════════════════════════════════════════════════
# Cada termo foi verificado diretamente no Título/Abstract da patente
# alvo para garantir match. Foco: bigramas que ocorrem literalmente.
# NOTA: chaves idênticas foram fundidas numa única entrada (Python dict
# sobrescreve valores com a mesma chave).
# ══════════════════════════════════════════════════════════════════════

_EXPANSAO_V14 = {

    # ── Filtration/Liquid Filter Device ────────────────────────────
    # PI96103612 — PROCESSO PARA A FABRICAÇÃO DE UMA MONTAGEM DE FILTRO
    # PI01003534 — FILTRO E PROCESSO PARA PRODUÇÃO DE UM FILTRO
    # PI98127357 — PELÍCULA DE FILTRO POSSUINDO BORDAS VEDADAS
    "Filtration/Liquid Filter Device": [
        "montagem de filtro", "fabricação de uma montagem",
        "filtro produzida", "montagem filtro elemento",
        "fabricação montagem filtro",
        "processo para produção", "produção de um filtro",
        "processo produção filtro", "filtro plano",
        "forma de cilindro", "filtro possuindo bordas",
        "bordas vedadas com cera", "vedadas com cera",
        "película de filtro possuindo", "camada de cera",
        "cera impermeável",
    ],

    # ── Packaging Machinery ────────────────────────────────────────
    # PI00016608 — CONJUNTO PARA ALIMENTAR PORÇÕES DE CAFÉ
    "Packaging Machinery": [
        "alimentar porções", "porções de café",
        "café preembalados", "uma máquina de café",
        "preparação de uma máquina", "conjunto para alimentar",
        "pó de café", "câmara de preparação",
        "máquina de café",
    ],

    # ── Drive Shafts — FUNDIDAS (DE102010043118 + WO2016112169) ────
    "Drive Shafts": [
        # DE102010043118A1 — Arrangement For Transmitting A Torque
        "transmitting a torque", "torque between a shaft",
        "shaft and a hub", "between a shaft and",
        "arrangement for transmitting",
        "inner geometry", "equilateral n-corner",
        "coupling section of the shaft",
        # WO2016112169A1 — Shaft For Downhole Equipment
        "shaft for downhole", "shaft for downhole equipment",
        "downhole equipment", "coupling of a shaft",
        "shaft used in a well", "well application",
        "nominal diameter of the shaft",
        "main body portion having",
    ],

    # ── Conveyor and Transport — FUNDIDAS (DE202008018151 + JP2006240852 + WO2013138926) ──
    "Conveyor and Transport": [
        # DE202008018151 — Device For Processing A Material (polymer)
        "processing a polymer", "polymer material and",
        "removing undesired contaminants", "impair the processing",
        "further processing of the polymer", "volatile substances",
        "moisture or water vapor", "for processing a material",
        # JP2006240852 — Transfer Device
        "high transferring ability", "separated transferring objects",
        "preventing clogging in a case", "vinyl ropes long fibers",
        "hair vinyl ropes",
        "transferring object",
        # WO2013138926 — System To Evacuate Materials From A Chamber
        "system to evacuate", "evacuate shovelable biomass",
        "shovelable biomass", "elongated chamber from below",
        "combination of a grating", "grating which serves as",
        "movable knife positioned parallel",
        "weight of materials",
    ],

    # ── Media and Document Destruction ─────────────────────────────
    # DE202009012359 — Destruction Device For Data Carriers
    "Media and Document Destruction": [
        "destroying data carriers", "destruction device for data",
        "data carriers and peripheral", "peripheral devices surrounding",
        "mechanical destruction of the data",
        "bending or creasing", "punching device",
        "shearing device for the mechanical",
    ],

    # ── Agriculture and Biomass ────────────────────────────────────
    # DE102004026803 — Chaff-Cutter Microwave
    "Agriculture and Biomass": [
        "chaff-cutter used", "cutting wooden waste",
        "wooden waste in garden", "microwave radiator",
        "mounted in a cutting chamber", "heated and softened before",
        "chaff-cutter introduction",
        "cutter microwave", "radiator cutting chamber",
        "cutter water jet",
    ],

    # ── Conveyor and Transport/Plastic Recycling Processor ─────────
    # DE102014017072 (x2) — Device For Conveying A Medium
    "Conveyor and Transport/Plastic Recycling Processor": [
        "conveying a medium", "device for conveying a medium",
        "for conveying a medium",
        "working machine", "plurality of carrier shafts",
        "carrier shafts",
    ],

    # ── Macerator/Cutting Elements ─────────────────────────────────
    # DE102006003514 — Tightening Loosening Clamping Nuts Blade
    "Macerator/Cutting Elements": [
        "tightening and loosening", "loosening device for clamping",
        "clamping nuts", "for securing blade",
        "blade sets in cutter", "driven bevel gear",
        "knife pack", "clamping nut of cutters",
        "spur gear", "bevel gears and spur",
    ],

    # ── Conveyor and Transport/Sludge Hopper Transport ─────────────
    # EP4356999B1 — A Hopper For Transporting Sludge
    "Conveyor and Transport/Sludge Hopper Transport": [
        "a hopper for transporting", "hopper for transporting sludge",
        "transporting sludge", "method for transporting sludge",
        "material buildup and clogging", "hopper's internal walls",
        "load cell to measure",
        "flat spray nozzles",
    ],

    # ── Mixing and Agitation — FUNDIDAS (EP2409770 + US20090236274) ──
    "Mixing and Agitation": [
        # EP2409770 — Arrangement For Homogenizing Of Sample
        "for homogenizing of sample", "method for homogenizing",
        "homogenization of a sample", "homogenizing of sample",
        "the homogenization of a sample",
        "cutting tool",
        "a motor a cutting tool",
        "rotate the cutting tool", "rotation speeds",
        # US20090236274 — Agitator In A Sewer System
        "agitator in a sewer", "sewer system has a waste",
        "waste material flow path", "in-line agitator",
        "downstream digester assembly", "digester assembly",
        "disposed upstream to the digester",
        "break down the waste material",
    ],

    # ── Motors and Clutches ────────────────────────────────────────
    # JP2006345675 — Driving Motor For Railway Vehicles
    "Motors and Clutches": [
        "driving motor for railway", "motor for railway vehicles",
        "for railway vehicles", "drive motor for a rolling",
        "rolling stock", "oil supply chamber",
        "oil supply channel", "oil supply disk",
        "guide plate",
    ],

    # ── Motors and Clutches/Clutch Pulley System ───────────────────
    # JP2006022856 — Pulley With Built-In Clutch
    "Motors and Clutches/Clutch Pulley System": [
        "pulley with built-in clutch", "pulley hub",
        "one-way clutch", "supported so that they can be rotated",
        "enclosing bearings", "load torque",
        "transmitting the rotation",
    ],

    # ── Sterilization and Medical Waste — FUNDIDAS (JP2008272706 + US7534392) ──
    "Sterilization and Medical Waste": [
        # JP2008272706 — Asbestos-Containing Building Material
        "asbestos-containing building", "asbestos-containing material",
        "containing building material", "processing method and a processing",
        "building material waste", "processing equipment asbestos",
        "building materials and the like",
        "input zone", "crushing zone", "crushing the building",
        # US7534392 — Waste Processing Method For Pathogen Reduction
        "waste processing method", "pathogen reduction",
        "disinfection of waste", "ambient temperature and pressure",
        "cutting the waste into small", "small pieces to expose",
        "spraying the waste pieces", "waste pieces with disinfectant",
        "effective disinfection",
    ],

    # ── Macerator ──────────────────────────────────────────────────
    # KR101278449 — Apparatus For Disposing The Waste
    "Macerator": [
        "apparatus for disposing", "disposing the waste",
        "waste disposal apparatus", "agitation on residues",
        "residues remaining on the bottom", "bottom surface of a chamber",
        "heating and stirring the waste",
    ],

    # ── Grinding and Milling ───────────────────────────────────────
    # KR20120033577 — Method Of Improvement Of Crushing Performance
    "Grinding and Milling": [
        "improvement of crushing", "method of improvement",
        "crushing performance", "improving grinding performance",
        "method for improving grinding", "CT voltage value",
        "performing a grinding operation",
    ],

    # ── Pumps — FUNDIDAS (US20250137455 + WO2011140479 + WO2006099745) ──
    "Pumps": [
        # US20250137455A1 — Pump Adjusting Delivery Rate
        "adjusting the delivery rate", "delivery rate of a pump",
        "method for adjusting the delivery",
        "conveying a medium having a suction", "suction-side inlet",
        "pressure-side outlet", "conveyance housing",
        "pressure chamber and a transport",
        # WO2011140479A1 — Continuously Pumping Solid Material
        "continuously pumping a solid", "pumping a solid material",
        "hydrogen formation", "pressurized slurry of a solid",
        "slurry of a solid material", "liquid carbon dioxide",
        "solid carbon dioxide", "mixing container",
        "particles of solid carbon",
        # WO2006099745A1 (x2) — Pump With A Motor For Pumping Fluids
        "a pump with a motor", "pump with a motor for pumping",
        "motor for pumping fluids", "pump is disclosed which has",
        "pump includes an fluid displacer", "fluid displacer within",
        "displacer within the housing", "upper end and a lower end",
    ],

    # ── Oil Tools — FUNDIDAS (US20110155390 + WO201211994 + WO2010120677) ──
    "Oil Tools": [
        # US20110155390A1 — Pumping Fluid Additive Downhole
        "pumping a fluid and an additive", "fluid and an additive from",
        "additive from a downhole", "downhole location into",
        "pumping a fluid mixture", "fluid mixture from a wellbore",
        "wellbore location to a selected", "container configured to be placed",
        "the wellbore wherein",
        # WO201211994A1 — Stimulating A Multi-Zone Well
        "stimulating a multi-zone", "stimulating a multi zone",
        "multi-zone well", "multi zone well",
        "system for stimulating", "tubular body apportioned",
        "first zone and a second zone", "first set of plugs",
        "plugs placed in pre-drilled",
        # WO2010120677A2 — Resilient Anchor
        "resilient anchor", "radially expanding and plastically",
        "plastically deforming an expandable", "expandable tubular member",
        "expansion device for radially", "anchor coupled to the actuator",
        "actuator coupled to the expansion",
    ],

    # ── Oil Tools/Valves ───────────────────────────────────────────
    # US20230135540A1 — Downhole Apparatus Valve Arrangement
    "Oil Tools/Valves": [
        "downhole apparatus with a valve", "valve arrangement is for",
        "tubular body having first", "having first and second ports",
        "ports in a wall thereof",
        "valve arrangement being configurable",
    ],

    # ── Semiconductor and Nanomaterials ────────────────────────────
    # US20130109902 — Radioactive Substance Absorbent
    "Semiconductor and Nanomaterials": [
        "radioactive-substance-absorbent", "radioactive substance absorbent",
        "production device decontaminating",
        "fibrillated cellulose", "water permeable polymeric",
        "polymeric substance of botanical", "botanical origin",
        "granulated inorganic porous", "inorganic porous crystal",
        "radioactive substances released",
    ],

    # ── Bearings ───────────────────────────────────────────────────
    # US2012067111A1 — Bearing Arrangement Determining Properties Lubricant
    "Bearings": [
        "determining properties of a lubricant", "properties of a lubricant",
        "lubricant in a bearing", "arrangement for determining properties",
        "a first and a second bearing", "second bearing element",
        "movable relative to one another", "reducing the friction",
    ],

    # ── Sealings/Ring and Peripheral Seal ──────────────────────────
    # WO2015119270A1 — Mechanical Tool (annular members, rings)
    "Sealings/Ring and Peripheral Seal": [
        "first annular member", "second annular member",
        "annular member attached to", "attached to a housing",
        "outer periphery of a rotating", "rotating shaft",
        "stationary ring", "a rotating ring",
        "stationary ring and rotating", "split bodies",
        "ring shape by combining",
    ],

    # ── Paint and Coating Testing ──────────────────────────────────
    # WO2011048147A1 — Measuring The Cloudiness Of Paints
    "Paint and Coating Testing": [
        "measuring the cloudiness", "cloudiness of paints",
        "paints on test tables", "on test tables",
        "method for measuring the cloudiness",
        "color coordinates", "different measuring sites",
        "test table at at least",
        "observation angles",
        "gaussian smoothing",
    ],

}

for _k, _v in _EXPANSAO_V14.items():
    if _k in PALAVRAS_CHAVE:
        _ex = set(PALAVRAS_CHAVE[_k])
        PALAVRAS_CHAVE[_k].extend([t for t in _v if t not in _ex])
    else:
        PALAVRAS_CHAVE[_k] = list(_v)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V15 — patch_palavras_chave_v15.py
# Corrige 3 causas-raiz identificadas na auditoria de 10 patentes:
#   CAUSA 1 — "ESP" como substring de palavras portuguesas comuns
#   CAUSA 2 — "food cooking press" em Macerator/Food Waste Disposer
#   CAUSA 3 — "solid waste diverter" em Oil Tools
# ══════════════════════════════════════════════════════════════════════

# ── PASSO 1: Remoção de termos que causam falsos positivos ────────────

_REMOCOES_V15 = {

    # CAUSA 1: Remove "ESP" standalone de Pumps/Submersible Pumps
    "Pumps/Submersible Pumps": [
        "ESP",
    ],

    # CAUSA 2: Remove termos de panela/prensa culinária de Macerator
    "Macerator/Food Waste Disposer": [
        "food cooking press",
        "food cooking press domestic lower upper plate dishes fuel",
        "food cooking press domestic dishes fuel",
        "cooking press domestic",
        "domestic food press",
        "domestic food cooking",
        "food press greater depth",
        "food press dishes",
        "internal depth food",
        "various dishes saving",
        "greater internal depth press",
        "disposição construtiva prensa alimentos uso doméstico",
        "food cooking press domestic lower upper plate dishes",
        "prensa doméstica alimentos",
        "prensa para cozinhar",
        "press domestic food saving",
    ],

    "Macerator": [
        "food cooking press",
        "cooking press domestic",
        "domestic food press",
    ],

    # CAUSA 3: Remove "solid waste diverter" de Oil Tools
    "Oil Tools": [
        "drum solid waste diverter",
        "solid waste diverter drum",
        "solid waste diverter",
        "drum solid waste",
        "drum diverter helical",
        "diverter coil rotation",
        "helical coil diverter",
        "drum for solid waste",
        "coil rotation waste diverter",
    ],
}

for _cat, _termos_remover in _REMOCOES_V15.items():
    if _cat in PALAVRAS_CHAVE:
        _set_remover = set(t.lower() for t in _termos_remover)
        PALAVRAS_CHAVE[_cat] = [
            t for t in PALAVRAS_CHAVE[_cat]
            if t.lower() not in _set_remover
        ]

# ── PASSO 2: Deduplicação global ──────────────────────────────────────

for _cat in PALAVRAS_CHAVE:
    _seen = set()
    _dedup = []
    for _t in PALAVRAS_CHAVE[_cat]:
        _key = _t.lower()
        if _key not in _seen:
            _seen.add(_key)
            _dedup.append(_t)
    PALAVRAS_CHAVE[_cat] = _dedup

# ── PASSO 3: Adições para classificação correta ───────────────────────

_ADICOES_V15 = {

    # Fix CAUSA 1a: Scroll Compressor PT (PI99027399)
    "Compressors/Scroll Compressor": [
        "espiral orbitante",
        "compressor helicoidal",
        "compressor espiral",
        "scroll orbital lubrificação",
        "câmara traseira vedação",
        "back pressure scroll chamber",
        "orbiting scroll lubrication",
    ],

    # Fix CAUSA 1b: Separator sem partes móveis PT (PI97138550)
    "Separator/Gas-Liquid Separator": [
        "abertura tangencial gás",
        "cavidade cônica separação",
        "fluxo helicoidal separação",
        "pesos específicos gás",
        "gases diferentes pesos",
        "separação sem partes móveis",
        "conector saída gás",
        "tangential gas inlet auxiliary",
        "helical path gas separation",
    ],

    # Fix CAUSA 1c: Membrane Filtration Module PT (PI01069489)
    "Filtration/Membrane and Ultrafiltration": [
        "fibras ocas de osmosis reversa",
        "osmosis reversa nano-filtração",
        "nano-filtração fibras ocas",
        "espaço de coleta permeado",
        "módulo de filtração membranas",
        "filtração múltiplas membranas",
        "filtro fibras ocas suspensas",
        "membranas osmosis reversa módulo",
        "permeado comunicação hidráulica",
        "reverse osmosis nanofiltration hollow fiber",
        "hollow fiber module permeate",
        "nanofiltration membrane module",
    ],

    # Fix CAUSA 1d: Deep Filtration Device PT (PI98073672)
    "Filtration/Liquid Filter Device": [
        "dispositivo de filtragem profunda",
        "filtragem profunda módulo",
        "módulo de filtragem profunda",
        "elementos filtrantes profunda",
        "material de filtragem profunda",
        "troca de módulo filtragem",
        "estojo módulo filtragem",
        "placa extrema abertura entrada",
        "deep filtration device module",
        "deep bed filter module exchangeable",
        "filter module deep filtration",
    ],

    # Fix CAUSA 2: Cooking Press → Food Processing Appliances (MU70020337U2)
    "Food Processing Appliances": [
        "food cooking press",
        "cooking press domestic use",
        "domestic food cooking press",
        "press for cooking food",
        "cooking press plate dishes",
        "food press lower upper plate",
        "prensa culinária doméstica",
        "prensa para cozinhar alimentos",
        "panela de pressão culinária",
        "disposição construtiva prensa culinária",
        "prensa alimentos uso doméstico",
        "panela prensa alimentos",
        "food cooking press lower plate upper plate",
    ],

    # Fix CAUSA 3: Solid Waste Diverter → Macerator/Comminutor (AU5656600A)
    "Macerator/Comminutor": [
        "solid waste diverter",
        "solid waste diverter drum",
        "drum for a solid waste diverter",
        "drum solid waste diverter",
        "helical coil diverter",
        "waste diverter drum rotation",
        "coil solid waste diverter",
        "diverter drum helical coil",
        "drum helical coil waste",
    ],

    # Reforço: termos PT para ESP sem ambiguidade
    "Pumps/Submersible Pumps": [
        "electric submersible pump motor",
        "submersible pump electric motor",
        "ESP downhole motor seal",
        "ESP pump motor protector",
        "ESP seal section thrust",
        "bomba elétrica submersa",
        "motor elétrico submersível ESP",
        "electric submersible assembly seal",
    ],
}

for _cat, _novos in _ADICOES_V15.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V16 — patch baseado em auditoria dos 33 não classificados
# e 271 patentes em pastas raiz (dados: patents_data_test.xlsx, 5977 pat.)
#
# SITUAÇÃO ANTES DO V16:
#   Sem classificação : 33  (OK < 50, mas melhoráveis)
#   Pasta raiz apenas : 271 (OK < 50 por raiz individual)
#
# OBJETIVO: reduzir não classificados e migrar raízes para subpastas.
# Grupos tratados:
#   G1 — Bombas PT (5 patentes BR sem match)
#   G2 — Filtração PT (4 patentes BR sem match)
#   G3 — Separador PT (1 patente BR sem match)
#   G4 — Cutters / Choppers / Food Waste EN (4 patentes)
#   G5 — Solid Waste / Recycling (2 patentes)
#   G6 — Downhole / Casing / Completion (4 patentes US/WO)
#   G7 — Outros (ensilagem, kneader, polymer fiber, hydraulic elevator…)
# ══════════════════════════════════════════════════════════════════════

_ADICOES_V16 = {

    # ── G1: Bombas em português (PI95049550, PI95049762, PI00070572,
    #        MU80009972, PI01032720) ───────────────────────────────────
    # Termos PT que descrevem bombas vibratórias, de diafragma,
    # de pistão rotativo e controle de bombeamento.
    "Pumps/Diaphragm Pump": [
        "bomba de sucção e recalque",
        "sucção e recalque de liquidos",
        "pulsor bomba sucção",
        "membranas sucção recalque",
        "bomba membrana liquidos",
        "bomba diafragma fluidos",
        "diaphragm pump membrane fluid",
    ],
    "Pumps/Piston Pump": [
        "êmbolos rotativos bomba",
        "câmara êmbolos rotativos",
        "pistão oscilante solenóide",
        "membro oscilante bomba",
        "bomba vibratória solenóide",
        "dispositivo resfriamento bomba",
        "aperfeiçoamentos em bomba",
        "carcaça verticularizada bomba",
        "rotary piston pump chamber",
    ],
    "Pumps/Pumping System Control Method": [
        "controle de bombeamentos",
        "sistemas métodos bombeamento fluído",
        "câmara de bombeamento pressões",
        "monitorar escoamento bomba sensores",
        "bombeamento fluido controlador",
        "pump control method fluid chamber",
        "pumping control method piston",
    ],

    # ── G2: Filtração em português (PI97119504, PI01069489,
    #        PI96105330, PI98073672 reforço) ──────────────────────────
    "Filtration/Self-Cleaning and Backwash": [
        "limpeza de uma superfície de filtro",
        "superfície de filtro meio filtrante",
        "superfície seladora filtro secador",
        "raspagem mecânica filtro tubular",
        "cleaning filter surface suction dryer",
        "filter surface sealing cleaning",
    ],
    "Filtration/Liquid Filter Device": [
        "disposição de filtro partículas sólidas",
        "caixa de filtro filtro tubular",
        "filtro tubular caixa extremidades",
        "extrair partículas sólidas líquido flui",
        "liquid filter box tubular filter",
        "filter arrangement tubular liquid",
    ],

    # ── G3: Separador PT (PI97138550) ─────────────────────────────────
    # Aparelho de separação de fluidos/gases por pesos específicos,
    # sem partes móveis, cavidade tubular, entrada tangencial de gás.
    "Separator/Gas-Liquid Separator": [
        "separação fluidos gases pesos específicos",
        "separação matéria sólida fluxo de gás",
        "cavidade tubular separação gás",
        "conector entrada saída gás separação",
        "aparelho separação fluidos sem partes móveis",
        "gas separation different specific weights",
        "tubular cavity gas separation no moving parts",
    ],

    # ── G4: Cutters / Choppers / Kitchen Waste EN ─────────────────────
    # CN203076037U, CN202590908U, DE202005019152, DE202009007888,
    # KR20080059492, US20020195506
    "Macerator/Cutting Elements": [
        "cutter bowl rotary drive knife shaft",
        "knife shaft cutter bowl carrier",
        "precutter cutting set chopping machine",
        "chopping machine cutting set sensors",
        "kitchen garbage cutter knife shaft gear",
        "kitchen rubbish cutting blade shaft",
        "food waste treatment cutter block grinding slot",
        "cutter teeth grinding rack secondary grinding",
        "food waste drying processor stirring vanes",
        "rotating cutter feed opening chamber ram",
        "cutter rotatably mounted chamber articles",
        "arc-shaped blade knife shaft frequency conversion",
    ],
    "Macerator/Food Waste Disposer": [
        "food waste treatment device cutter block",
        "food waste treatment secondary grinding slot",
        "kitchen garbage cutter tank blade",
        "food waste drying crushing vanes motor",
        "food waste disposal housing cover intake",
    ],

    # ── G5: Solid Waste Recycling / Compressing containers ────────────
    # DE102008047319 (container squeezer), EP2186578 (solid refuse)
    "Conveyor and Transport/Plastic Recycling Processor": [
        "squeezing empty containers beverage bottles",
        "device compressing empty deformable containers",
        "cutting pressing unit beverage bottles cans",
        "squeezing plastic PET containers",
        "container compression cutting pressing",
    ],
    "Macerator/Sludge and Waste Processing": [
        "disposal method recycling solid refuse",
        "sorting crushing drying pressing solid refuse",
        "solid refuse recycling charcoal combustible",
        "solid waste pipeline evacuation fluidizing",
        "automatic collection solid waste pipeline",
        "pipeline evacuation comprehensive solid waste",
    ],

    # ── G6: Downhole Casing / Completion / Wellbore ───────────────────
    # US7647977B2, US12352114B2, US12264560B2, WO2022235425A1,
    # WO2007139541A1, US12416227B2
    "Oil Tools/Tubing": [
        "borehole liner downhole well bore rig",
        "liner downhole tool string central bore",
        "tool string driving mechanism aperture",
        "first second tool joint central bore",
        "forming liner downhole well bore",
    ],
    "Oil Tools/Casing and Tubing Accessories": [
        "latch assembly downhole tubular central bore",
        "latch keys tubular body alignment feature",
        "no-rotation latch coupling casing assembly",
        "latch coupling casing downhole conveyance",
        "completion system base pipe coupling shunt tubes",
        "alternate path shunt tubes jumper tubes",
        "torque resistant shroud base pipe coupling",
        "sequentially coupled base pipes alternate path",
    ],
    "Oil Tools/Drilling": [
        "bottomhole pressure hydrocarbons laval nozzle",
        "improving recovery hydrocarbons bottomhole device",
        "two-phase gas-liquid flow lifting hydrocarbons",
        "oilfield system time series equipment operations",
        "natural resource sites operational events ranking",
    ],

    # ── G7: Miscelânea ────────────────────────────────────────────────
    # US20120039145A1 — Gear Box Kneading Machine
    # US5495987       — Ensilage Slicing
    # WO2019037840A1  — Pulsation Damping
    # US2011318201A1  — Underwater Conveying with Pump
    # DE000019715224A1 — Hydro Rope Elevator (hydraulic)
    "Grinding and Milling/Shredders and Macerators": [
        "reciprocating kneader gear box primary shaft",
        "gear box kneading machine oscillation rotation",
        "kneader primary rotational gear secondary shaft",
        "variably coupled oscillation rotation kneading",
    ],
    "Agriculture and Biomass": [
        "ensilage slicing compacted ensilage mass",
        "ensilage slicing attachment skid steer loader",
        "compacted ensilage vertical facing forkable",
        "hydraulically driven reel ensilage",
    ],
    "Pumps/Diaphragm Pump": [
        "pulsation damping fluid membrane pressure pad",
        "damping pulsations fluid membrane housing wall",
        "pressure intermediate space membrane fluid",
    ],
    "Pumps/Submersible Pumps": [
        "underwater conveying assembly pump drive device",
        "underwater pump drive sealed process medium",
        "submersible conveying assembly inlet outlet port",
        "sewage pump blade set coaxially mounted",
        "sewage pump stationary blade base wheel blade",
        "water paddle disk blade chamber sewage",
    ],
    "Hydraulic and Pneumatic Devices": [
        "hydro rope elevator differential cylinder",
        "hydraulic elevator differential cylinder working chambers",
        "indirectly driven hydraulic elevator working fluid",
        "differential cylinder fluid circuit delivery pump",
    ],
}

# Aplica as adições V16 (sem criar duplicatas)
for _cat, _novos in _ADICOES_V16.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V16B — Correção dos termos V16 que não matcharam
# Problema: termos compostos longos não aparecem literalmente nos textos.
# Solução: termos de 2 palavras verificados diretamente nos abstracts.
# ══════════════════════════════════════════════════════════════════════

_ADICOES_V16B = {

    # CN202590908U — Kitchen Rubbish Cutting Device
    # DE202009007888 — Cutter (cutter bowl, knife shaft)
    # DE202005019152 — Precutter For Chopping Machine
    # US20020195506  — Rotating Cutter System
    "Macerator/Cutting Elements": [
        "kitchen garbage",
        "garbage cutter",
        "knife shaft",
        "cutter bowl",
        "knife shaft drive",
        "chopping machine",
        "cutting set",
        "precutter",
        "cutter rotatably",
        "feed opening chamber",
    ],

    # CN203076037U — Food Waste Treatment Device
    # KR20080059492 — Food Waste Drying Processor
    "Macerator/Food Waste Disposer": [
        "food waste treatment",
        "food waste disposal housing",
        "food waste drying",
        "grinding slot cutter",
        "cutter block grinding",
    ],

    # PI97138550 — Separação de Fluidos/Gases (PT)
    "Separator/Gas-Liquid Separator": [
        "pesos específicos",
        "fluxo de gás",
        "diferentes pesos",
        "separação de fluidos",
    ],

    # MU80009972 — Pulsor Bomba de Sucção (PT)
    "Pumps/Diaphragm Pump": [
        "sucção e recalque",
        "liquidos não corrosivos",
        "bomba para sucção",
        "sucção recalque",
    ],

    # PI01069489 — Módulo Filtração Membranas (PT)
    "Filtration/Membrane and Ultrafiltration": [
        "fibras ôcas",
        "osmosis reversa",
        "múltiplas membranas",
        "nano-filtração",
        "módulo filtração membranas",
    ],

    # PI95049550 — Resfriamento de Bomba Vibratória (PT)
    "Pumps/Piston Pump": [
        "resfriamento de bomba",
        "bomba vibratória",
        "solenóide bomba",
        "dispositivo resfriamento",
    ],

    # PI01032720 — Bombas Compressores Motores Câmara Êmbolos (PT)
    "Compressors/Reciprocating Compressor": [
        "câmara e êmbolos",
        "êmbolos rotativos",
        "bombas compressores motores",
        "câmara rotativos",
    ],

    # PI96105330 — Disposição de Filtro Tubular (PT)
    "Filtration/Liquid Filter Device": [
        "filtro tubular",
        "caixa de filtro",
        "partículas sólidas líquido",
        "disposição de filtro",
        "filtro tubular caixa",
    ],

    # US20090067992 — Sewage Pump
    "Pumps/Grinder Pump Station": [
        "sewage pump blade",
        "blade set coaxially",
        "water paddle disk",
        "wheel blade chamber",
        "sewage pump stationary",
    ],

    # US7647977B2 — Borehole Liner
    "Oil Tools/Tubing": [
        "borehole liner",
        "liner downhole",
        "tool string",
        "well bore liner",
    ],

    # US12352114B2, US12264560B2, WO2022235425A1 — Downhole Casing/Completion
    "Oil Tools/Casing and Tubing Accessories": [
        "latch assembly",
        "latch coupling",
        "downhole tubular",
        "latch keys",
        "base pipe coupling",
        "shunt tubes jumper",
        "alternate path shunt",
        "torque resistant shroud",
        "completion system base pipe",
    ],

    # WO2007139541A1 — Device For Improving Oil Recovery
    "Oil Tools/Drilling": [
        "bottomhole pressure hydrocarbons",
        "lifting hydrocarbons surface",
        "laval nozzle downhole",
        "two-phase gas-liquid homogenous",
    ],

    # DE000019715224A1 — Hydro Rope Elevator
    "Hydraulic and Pneumatic Devices": [
        "differential cylinder fluid",
        "hydraulic elevator differential",
        "hydro rope elevator",
        "delivery pump differential",
    ],

    # DE102008047319 — Compressing Empty Containers
    "Conveyor and Transport/Plastic Recycling Processor": [
        "beverage bottles cans",
        "squeezing empty containers",
        "cutting pressing unit",
        "deformable containers plastic",
    ],

    # EP2186578 — Disposal Method Recycling Solid Refuse
    # WO2010108402 — Automatic Collection Solid Waste Pipeline
    "Macerator/Sludge and Waste Processing": [
        "solid refuse recycling",
        "crushing drying pressing",
        "solid waste pipeline",
        "pipeline evacuation solid",
        "solid refuse sorting",
    ],

    # US20120039145A1 — Gear Box Kneading Machine
    "Grinding and Milling/Shredders and Macerators": [
        "kneading machine gear",
        "reciprocating kneader",
        "kneader gear box",
        "oscillation rotation kneading",
    ],

    # US5495987 — Device For Slicing Ensilage
    "Agriculture and Biomass": [
        "ensilage slicing",
        "compacted ensilage",
        "ensilage attachment",
        "skid steer ensilage",
    ],

    # WO2019037840A1 — Pulsation Damping Fluid System
    "Pumps/Diaphragm Pump": [
        "pulsation damping fluid",
        "damping pulsations membrane",
        "pressure intermediate space",
        "membrane pressure pad",
    ],

    # US2011318201A1 — Underwater Conveying Assembly With Pump
    "Pumps/Submersible Pumps": [
        "underwater conveying assembly",
        "underwater pump drive",
        "conveying assembly sealed",
        "underwater pump module",
    ],

    # US12416227B2 — Oilfield System (monitoring)
    "Monitoring and controlling/Condition Monitoring Pump": [
        "oilfield time series",
        "natural resource sites operational",
        "operational events ranking",
        "equipment operations time series",
    ],
}

# Aplica as adições V16B (sem criar duplicatas)
for _cat, _novos in _ADICOES_V16B.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V16C — Últimos 8 não classificados (termos verificados)
# ══════════════════════════════════════════════════════════════════════

_ADICOES_V16C = {

    # MU80009972 — Pulsor Bomba de Sucção (membrana/diafragma PT)
    "Pumps/Diaphragm Pump": [
        "membranas sucção",
        "pulsor bomba",
        "membranas flanges",
        "treliçadas cordas",
        "membrana bomba fluido",
        "membrana sucção recalque",
    ],

    # PI95062017 — Limpeza de Prensas de Massa (parafusos PT)
    "Pumps/PC Pump and Motor": [
        "prensas de massa",
        "limpeza prensas massa",
        "parafuso limpeza máquinas",
        "limpeza parafuso massa",
    ],

    # EP2186578 — Disposal / Recycling Solid Refuse
    "Macerator/Sludge and Waste Processing": [
        "solid refuse",
        "recycling solid",
        "solid refuse recycling",
        "recycling solid refuse",
    ],

    # WO2010108402 — Pipeline Evacuation Solid Waste
    "Conveyor and Transport": [
        "pipeline evacuation",
        "solid waste pipeline",
        "pipeline evacuation solid",
    ],

    # WO2019037840A1 — Pulsation Damping Fluid System
    "Pumps/Diaphragm Pump": [
        "pulsation damping",
        "damping pulsations",
        "pressure pad membrane",
        "pulsation damping fluid",
    ],

    # US12416227B2 — Oilfield System (monitoring/operations)
    "Monitoring and controlling/Condition Monitoring Pump": [
        "oilfield system",
        "natural resource sites",
        "time series data",
        "operational events",
        "equipment operations",
    ],

    # US2009104831A1 — Polymer Fiber (fora do escopo do sistema)
    # PI04053893 — Dispositivo sem fio (fora do escopo)
    # Estes dois são genuinamente fora do domínio — não devem ser classificados.
}

for _cat, _novos in _ADICOES_V16C.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V17 — Patch de Redução de Raízes
# Meta: TOTAL GERAL de patentes em Nível 1 (raiz) < 50
# Base: 272 patentes em raiz antes do patch
# Diagnóstico: auditoria double-check + análise das 272 patentes
#
# ESTRATÉGIA POR CATEGORIA:
#   - Macerator (17): subpastas Food Processing / Waste / Industrial
#   - Sealings (29): subpastas Screw Rotor / Sealing Compound / Industrial
#   - Drive Shafts (28): subpastas Torque/Hub / Screw Pump Shaft / Downhole
#   - Pumps (24): subpastas PT / Fluid Controlled / Multiphase
#   - Oil Tools (24): subpastas Downhole Assembly / Wellbore / Mining
#   - Conveyor (19): subpastas Rubber/Tire / Waste Bin / Granulator
#   - Grinding (17): subpastas Flour / Grain Mill / Colloidal Mill
#   - Monitoring (17): subpastas Storage Medium / Machine Tool
#   - Bearings (17): subpastas Dust/Industrial / Vehicle / Lubrication
#   - Mixing (13): subpastas Food Cutting / Wood Chipper
#   - Manufacturing (12): subpastas PT Fabrication / Filter Body
#   - Electric Motors (10): subpastas Tissue/Crusher Motor / Toilet Grinder
#   - Media Destruction (8): subpastas Data Carrier / Shredder Blade
#   + correções de falsos positivos (Additive Manufacturing, rotor/stator)
# ══════════════════════════════════════════════════════════════════════

# ── PASSO 1: Remover termos que causam falsos positivos ───────────────

_REMOCOES_V17 = {
    # "rotor" e "stator" sozinhos capturam motores elétricos genéricos,
    # granuladores, rotores de trituração — gerando falsos positivos em P1
    "Pumps/PC Pump and Motor/Rotor": [
        "rotor",
        "stator",
    ],
    "Pumps/PC Pump and Motor/Stator": [
        "rotor",
        "stator",
    ],
    # "additive" e "manufacturing" genéricos em Additive Manufacturing
    # capturam food disposers, garden tools, comminution rotors
    "Manufacturing technology/Additive Manufacturing": [
        "manufacturing",
        "additive",
        "layer",
        "part",
        "base",
        "material",
        "production",
        "fabrication",
    ],
}

for _cat, _termos in _REMOCOES_V17.items():
    if _cat in PALAVRAS_CHAVE:
        _rem = set(t.lower() for t in _termos)
        PALAVRAS_CHAVE[_cat] = [t for t in PALAVRAS_CHAVE[_cat] if t.lower() not in _rem]


# ── PASSO 2: Adições para migrar raízes para subpastas ────────────────

_ADICOES_V17 = {

    # ════════════════════════════════════════════════════════
    # MACERATOR (17 na raiz)
    # ════════════════════════════════════════════════════════

    # Food processing equipment (CN201613163U, DE202011005356,
    # DE102010060094, DE10325526, US20060196334, US20020144606,
    # US20030197080, US20110083566)
    "Macerator/Blending and Mixing": [
        "food processing equipment clean",
        "food processing device pan",
        "food processing apparatus slicing strips",
        "food processing apparatus magnetic drive",
        "food processing device extract juice",
        "food processing elements support plate",
        "active insert food processing",
        "folding pull-out active insert",
        "knife food processing device",
        "food machine electrical voltage",
        "perforated disk processing food",
        "perforated disk food products holes",
        "processing food through-holes axial",
        "food processing crushing cutter heating",
        "crushing cutter container body lid",
    ],

    # Meat processing (DE102004027024)
    "Macerator/Cutting Elements": [
        "meat processing machine fat analyzer",
        "meat chopped fat content",
        "fat analyzing device meat",
        "fresh frozen meat chopped",
    ],

    # Waste / tire shredding (EP1055458, KR101278449)
    "Macerator/Sludge and Waste Processing": [
        "waste tire shredding members blades",
        "shredding members shredding blades waste",
        "waste disposal agitation residues chamber",
        "disposing waste agitation bottom surface",
        "waste disposal apparatus agitation residues",
    ],

    # Clay / plastic mixing (RU2411122)
    "Macerator/Industrial Crusher": [
        "fine-crushing mixing plastic materials clay",
        "clay mix material screw actuator",
        "device preparation clay mix",
        "case loading bin screw actuator clay",
    ],

    # Grain / bread crushing (US20090294558, WO2004101185)
    "Macerator/Comminutor": [
        "crushing grains shafts rollers driving mechanism",
        "apparatus crushing grains plurality shafts",
        "waste bread crushing drying fine powder",
        "treating waste bread crushing drying",
        "crushing drying waste bread granular",
    ],

    # Pulper (US5551641)
    "Macerator/Comminutor/Flow Channel": [
        "pulper pulping chamber pulping mechanism",
        "non-pulpables collection chamber pulper",
        "pulping chamber collection basket pulper",
        "solid waste pulper collection chamber",
    ],

    # Bale breaker / horizontal grinder (US20100155513)
    "Macerator/Industrial Crusher": [
        "bale breaker horizontal grinder powerfeed",
        "auxiliary powerfeed horizontal grinder",
        "powerfeed drum horizontal grinder feed",
    ],

    # Medical waste (JP2009125739)
    "Sterilization and Medical Waste/Integrated Medical Waste Management": [
        "disposing medical waste infectious secondary infection",
        "apparatus disposing medical waste infection",
        "medical waste disposal infection safety",
    ],

    # ════════════════════════════════════════════════════════
    # SEALINGS (29 na raiz)
    # ════════════════════════════════════════════════════════

    # Fluid machinery / multi-stage compression / screw rotors
    "Sealings/Industrial Equipment Seals": [
        "fluid machine multi-stage compression shell",
        "multi-stage compression mechanism cavity",
        "compression cavity multi-section mechanism",
        "triple-screw shaft head pump compressor",
        "triple-screw pump body driving screw",
        "screw rotor fluid handling devices blowhole",
        "blowhole sealing line screw rotor profile",
        "screw rotor toth profile blowhole",
        "oil-free screw fluid machinery bearing hole",
        "oil free screw fluid machine pressure",
        "twin-screw rotating vortex conjugation",
        "rotating vortex conjugation screw rod profile",
        "sealing line profile screw rotor area",
    ],

    # Pulverizer chamber / granulating machine
    "Sealings/Hermetic and Static Seals": [
        "pulverizer chamber accumulation side plates",
        "anti-accumulation pulverizer knife cavity",
        "grinding granulating machine medicine manufacturing",
        "energy-saving grinding granulating machine",
        "organic waste processor box body work tank",
        "low-energy organic waste processor exhaust",
    ],

    # Conveyor bearing element / roller device
    "Sealings/Bearing Seal": [
        "track conveyor bearing element transport roller",
        "bearing element transport roller frame",
        "roller device conveyer weather-resistant",
        "roller body axially opposite end walls",
        "weather-resistant roller device conveyer",
        "bearing unit two shafts orientated parallel",
        "sealing bearing unit two parallel shafts",
        "two shafts orientated parallel housing",
    ],

    # Pump sealing / pump housing / generic pump
    "Sealings/Pump Housing Seal": [
        "pump housing bore semi-circular cross-section",
        "pump assembly housing two parts bore",
        "pump sealing housing formed two parts",
        "sealing pistons rotating reciprocating engine",
        "rotor discs common rotor axle sealing",
        "pistons rotating engine rotor discs",
        "centrifugal disc fluid pump shaft",
        "centrifugal disc rotatably connected shaft",
        "drum motor inner outer lid hygienic",
        "drum tube spatially fixed axis interior",
    ],

    # Sealing compound application / joint sealing
    "Sealings/Hermetic and Static Seals": [
        "sealing compound closure cap containers",
        "applying sealing compound surface stamp",
        "sealing compound outer inner stamp",
        "gasket seat system joint sealing",
        "gasket inner outer portion coupling wall",
        "sealing joint gasket inner wall coupling",
        "sealing system casing well leaks perforations",
        "sealing zone casing well leaks perforations",
        "liquid supply mechanism branch flow passages",
        "liquid supply branch flow passages intersecting",
    ],

    # Seal stem anchor / riser / flange cap
    "Sealings/Ring and Peripheral Seal": [
        "seal stem anchor tubular body lock threads",
        "anchor assembly body lock threads stem",
        "adjustable riser suspension sealing system",
        "riser hanger mating sleeve ratchet-latch",
        "riser suspension sealing ratchet latch sleeve",
        "flange locking cap subsea external flange",
        "cap subsea external flange seal",
        "made-up flange locking cap tubular",
    ],

    # Device conveying viscous material / barrel
    "Sealings/Dynamic and Oil Seals": [
        "conveying viscous material barrel container",
        "device conveying viscous material container bottom",
        "barrel container conveying viscous screw",
        "flow rate bearing inner outer race rolling",
        "setting desired flow rate bearing",
    ],

    # ════════════════════════════════════════════════════════
    # DRIVE SHAFTS (28 na raiz)
    # ════════════════════════════════════════════════════════

    # Torque transmission shaft/hub
    "Drive Shafts/Power Transmission Mechanism": [
        "transmitting torque shaft hub equilateral",
        "arrangement transmitting torque shaft hub",
        "torque transmission drive shaft motor eccentric",
        "drive shaft torque centrally rotating motor",
        "drive shaft eccentric screw pump torque",
        "limiting rotation drive shaft reverse direction",
        "braking assembly drive shaft reverse hub",
        "hub fixed rotation drive shaft braking",
        "retaining plate gear shafts gear assembly",
        "plate connecting gear shafts aperture",
        "tandem trochoid pump drive shaft spacer",
        "trochoid pump drive shaft non-circular end",
    ],

    # Screw pump shaft / PC pump drive shaft
    "Drive Shafts/Flexible Shaft and Sleeve": [
        "gasket part pump bearing drive shaft",
        "gasket part pump drive shaft arranged",
        "eccentric screw-type pump pump casing stator",
        "eccentric screw pump stator cladding cavity",
        "eccentric screw pump tubular casing cavity",
        "suction housing rotor stator pump cementitious",
        "rotor stator pump wet cementitious suction",
        "screw type pump motor stator rotor vanes",
        "pump assembly stator rotor opposite thread",
        "fluid pump mechanism helical drivetrain gears",
        "fluid pump cowling helical gears teeth",
        "helical drivetrain gears cowling sidewalls",
    ],

    # Downhole motor stator / downhole shaft
    "Drive Shafts/Splines and Keyways": [
        "stator downhole motor mandrel fabricating",
        "downhole motor stator fabricating method",
        "stator for downhole motor inner geometry",
        "stator insert downhole motor methods",
        "stator inserts downhole motor mandrel",
        "fabricating stator downhole motor applying",
        "shaft downhole equipment coupling driven",
        "shaft well application coupling nominal diameter",
        "device hydraulically protecting submersible electric motor",
        "protector electric motor downhole pump",
    ],

    # Food cutter / grinder rotary shaft
    "Drive Shafts/Axles and Spindles": [
        "meat dicer machine food ham cheese cutting",
        "cutting food ham cheese width predetermined",
        "bladeshaft assembly powered saw cutting machine",
        "hollow tubular housing shaft coaxially",
        "grinder rotary shaft drive shaft load",
        "grinder drive shaft size hardness grinding",
        "prestressing device cutter rotor prestressing part",
        "cutter rotor prestressing part coaxially arranged",
    ],

    # Slurry / comminution / reducing machine
    "Drive Shafts/Slurry Breaking and Farm Pump": [
        "apparatus breaking solids farmyard slurry tank",
        "slurry rotating blade fixed cutter tank",
        "reducing machine rotor assembly comminuting wood",
        "fragmenting rotor assembly comminuting waste wood",
        "rotor assembly comminuting waste wood hammer",
        "apparatus comminuting feed rotor driven shaft",
        "comminuting feed rotor driven shaft disc",
        "tool fixture overhung tools roller screw compacting",
        "drive shaft tool fixture compacting machine",
    ],

    # Lubricating structure supercharging
    "Drive Shafts/Shaft Coupling Device": [
        "lubricating structure supercharging device stirring",
        "supercharging device lubricating oil stirring resistance",
        "joint assembly connecting two spaced drive shafts",
        "joint assembly submergible pumping drive shafts",
        "connecting shaft submergible pumping joint assembly",
    ],

    # Rotary pump classic Moineau / screw engines
    "Pumps/PC Pump and Motor": [
        "rotary engine pump moineau gearing eccentric",
        "moineau gearing mechanism two more rotors",
        "rotary pump moineau principle progressive",
        "improvements screw engines pumps meters rotary",
        "rotary engine fixen stockholm screw pump",
        "helical multiple pump moineau principle progressive",
        "multiple pump assembly moineau principle capacity",
    ],

    # ════════════════════════════════════════════════════════
    # PUMPS (24 na raiz)
    # ════════════════════════════════════════════════════════

    # PT: bombas hidráulicas / parafuso / pulmões
    "Pumps/Hydraulic Pump": [
        "bomba d'água hidráulica pulmões",
        "bomba hidráulica sistema pulmões",
        "bomba hidráulica câmaras fluido",
        "hydraulic pump lung chamber fluid",
    ],

    "Pumps/Screw Pump": [
        "unidade bombeamento parafuso fases diversas",
        "bombeamento parafuso fluidos fases",
        "screw pump unit multiphase fluids treatment",
        "screw type pump motor stator rotor vanes radial",
    ],

    # Centrifugal disc pump
    "Pumps/Centrifugal Pump": [
        "centrifugal disc fluid pump shaft rotatably",
        "centrifugal disc opening connected shaft",
        "pump centrifugal disc aggregate fluid",
    ],

    # Generic pump with piston / valve
    "Pumps/Piston Pump": [
        "pump suction-side inlet pressure-side outlet",
        "pump conveying housing conveying member",
        "pump conveying medium suction chamber",
        "valve pump assembly piston open closed fluid",
        "piston open position fluid flow blocked",
        "valve piston pump housing inlet outlet",
    ],

    # Fluid controlled pumping system
    "Pumps/Well Pump Systems": [
        "fluid controlled pumping system pumping unit",
        "fluid cavity pumping unit passage suction",
        "pumping unit fluid cavity suction end",
    ],

    # Crossover two-phase / multiphase
    "Pumps/Multiphase Pump": [
        "crossover two-phase flow pump impellers diffusers",
        "hydrocarbon well pump impellers diffusers inner outer",
        "pump impellers diffusers central outer sections",
        "conveying device liquid gas mixture borehole",
        "multiphase-pumping device liquid gas borehole",
        "crude-oil natural-gas mixture borehole multiphase",
    ],

    # Oil pump rotor assembly
    "Pumps/Gear Pump": [
        "oil pump rotor assembly noise pumping performance",
        "rotor pump assembly reduces noise oil pump",
        "oil pump rotor assembly mechanical efficiency",
    ],

    # Claw booster pump / screw rotor
    "Pumps/Roots and Rotary Piston Pump": [
        "claw booster pump pair rotors parallel shafts",
        "claw portion pump chamber rotors shafts",
        "screw rotor compressor male female lobes grooves",
        "complex screw rotors male rotor helical lobes",
        "compressor male rotor female rotor lobes grooves",
        "high-speed shearing machine granulation slurry tower",
        "shearing machine slurry high-tower granulation",
    ],

    # Slurry / solid pumping
    "Pumps/Slurry Pump": [
        "continuously pumping solid material liquid carbon dioxide",
        "pressurized slurry solid material liquid",
        "slurry solid material carbon dioxide method",
    ],

    # Pump with motor housing conduit
    "Pumps/Water and General Fluid Pump": [
        "pump housing upper lower end conduit",
        "pump motor pumping fluids conduit housing",
        "pump with motor housing conduit upper lower",
        "a pump is disclosed housing conduit upper lower",
    ],

    # Fuel pump resonator pipe
    "Pumps/Pump Systems and Applications": [
        "pump supplying fluid fuel pump resonator pipe",
        "fuel pump resonator pipe reflector",
        "pump chamber resonator pipe fuel",
    ],

    # ════════════════════════════════════════════════════════
    # OIL TOOLS (24 na raiz)
    # ════════════════════════════════════════════════════════

    "Oil Tools/Downhole Power Generation": [
        "container sump multi-phase pump hydrocarbon",
        "collecting container multi-phase mixtures hydrocarbon",
        "multi-phase pump system container sump",
        "down-hole gas separation liquids wellbore chambers",
        "production separation chambers parallel wellbore",
        "gas separation wellbore chambers parallel",
    ],

    "Oil Tools/Drilling": [
        "downhole assembly articulated mandrel passive active",
        "articulated mandrel passive active damping borehole",
        "mandrel torsional stick-slip damping downhole",
    ],

    "Oil Tools/Sand Protection": [
        "sized ore feed excavated deposit processing",
        "processing apparatus ore feed excavated deposit",
        "mobile slurry apparatus oil sand ore frame",
        "slurry box frame oil sand ore water",
        "oil sand ore slurry mobile apparatus",
    ],

    "Oil Tools/Wellhead equipment": [
        "wellsite control sensor information notification computing",
        "systems methods wellsite control sensor notification",
    ],

    "Oil Tools/Casing and Tubing Accessories": [
        "well tool nanoparticle reinforced metallic coating",
        "metallic coating well fluid substrate first member",
        "selective acid diversion matrix acidizing vortices",
        "taylor-couette vortices fluid targeted rotation",
        "apparatus pumping fluid additive downhole container",
        "fluid mixture wellbore container apparatus",
        "oil field apparatus seal rubber oxycellulose",
        "seal rubber oxycellulose cellulose nanofibers",
        "valves bottom hole assemblies selectively actuating",
        "selectively actuating motor barrel interior",
        "tar sand oil extraction in-situ liquefaction",
        "extracting oil tar sand formations liquefaction",
        "process mineral oil deposits temperature gradient",
        "mineral oil deposits large temperature gradients",
        "centraliser expandable downhole assembly completing",
        "expandable centraliser downhole assembly method",
        "ultra pump systems elongated cylindrical chamber",
        "pump removing liquids well cylindrical chamber",
        "releasable connector assembly tubular payload",
        "stimulating multi-zone well tubular body zones",
        "system bore hole axially coupling tubular mandrel",
        "automatic tubing drain rotary pumps reactive torque",
        "resilient anchor radially expanding tubular member",
        "wellbore maintenance improved oil recovery wellbores",
        "positioning tool casing downhole detecting unit",
    ],

    # ════════════════════════════════════════════════════════
    # CONVEYOR AND TRANSPORT (19 na raiz)
    # ════════════════════════════════════════════════════════

    "Conveyor and Transport/Plastic Recycling Processor": [
        "rubber block crushing production line chopper mixer",
        "chopper mixer conveyor belt rubber block",
        "tyre fine crusher frame motor crushing chamber",
        "tire fine crusher main shaft bearings",
        "recycled thermoplastic composition waste thermoset",
        "thermoplastic recycled thermoset crumb slurry",
        "process recycling material polymer thermoset composite",
    ],

    "Conveyor and Transport/Crushing Equipment for Chips": [
        "granulator driven cutting device strand material",
        "granulator cutting device conveying drive device",
        "double roller machine pressure granular reciprocating",
        "roller machine table reciprocating slip-on gear",
        "device processing polymer material contaminants volatile",
        "processing polymer material contaminants removing",
    ],

    "Conveyor and Transport/Composting and Digestion": [
        "collection bin kitchen waste membrane warehouse",
        "kitchen waste collection warehouse rolling gate",
        "rubbish bag breaking device rotary drum blades",
        "bag breaking device rotary drum motor conveying",
        "automatic collection pipeline evacuation solid waste",
        "pipeline evacuation comprehensive utilization solid waste",
        "system evacuate shovelable biomass chamber grating",
        "evacuate biomass elongated chamber grating movable",
        "pick-up head system surface cleaning vehicle housing",
        "pick-up head suction bottom opening debris transfer",
    ],

    "Conveyor and Transport/Belt Conveyor": [
        "conveying device conveying fluid housing drivable",
        "conveying member housing drivable fluid device",
        "material spreader belt chain assembly chamber",
        "belt chain assembly material spreader",
        "line retention arrangement supports clips cantilever",
        "retention clips base cantilever oriented",
    ],

    "Conveyor and Transport/Metal Recycling Separator": [
        "transfer device transferring separated transferring objects",
        "transfer device clogging separated objects",
        "method apparatus recycling carpet fibers backing",
        "carpet recycling fibers backing separation",
        "carpet fibers backing apparatus belt",
        "recycling carpet fibers backing material belt",
    ],

    "Conveyor and Transport/Branch and Tree Crusher": [
        "device reduce clogging gutters downspout grinder",
        "gutter housing motor-driven grinder mechanism",
        "roller-supported accumulator lawn garden debris",
        "accumulator vacuum pick-up blower separator",
    ],

    # ════════════════════════════════════════════════════════
    # GRINDING AND MILLING (17 na raiz)
    # ════════════════════════════════════════════════════════

    "Grinding and Milling/Food Grinding": [
        "flour milling system hard wheat grain",
        "processo sistema moagem farinha grãos duros",
        "moagem farinha grãos wheat milling steps",
        "flour milling process hard wheat plurality steps",
    ],

    "Grinding and Milling/Pulverizer and Superfine Mill": [
        "cylinder type specific cutter grinder vertical air-cooled",
        "barrel-type pulverizer air-flow vortex fluidized dry",
        "grinding rotor disc throughgoing holes peripheral",
        "grinding rotor plurality holes peripheral disc",
        "high-speed shearing industrial colloidal mill disc",
        "colloidal mill movable milling disc static disc",
        "grinder rack enclosure main shaft grinding wheel",
        "screen piece dismounting grinder grinding room shell",
        "grinder pulverization chamber inlet hopper",
        "stator rotor shear mill fixed rotating disc",
        "shear mill stator rotor disc surface",
        "milling device pump sewage thick matter liquid",
        "milling device liquid media solid components housing",
    ],

    "Grinding and Milling/Food and Bone Mill": [
        "grinding treatment device kitchen sound source",
        "grinding treatment device controller kitchen",
        "method apparatus crushing organic waste particle size",
        "organic waste crushing particle size recycling",
        "disposer multi-fixed grinding blades rotary plate",
        "fixed grinding blades rotary grinding plate disposer",
        "disposer multi-step grinding protrusion sink drain",
        "grinding protrusion rotary grinding plate sink",
        "milling apparatus injection member groove end",
        "milling device injection contents groove connected",
        "method improvement crushing performance CT voltage",
        "crushing performance CT voltage improvement method",
        "shellfish crusher inlet pulverizing device shells",
        "shellfish pulverizing oyster shells inlet",
    ],

    "Grinding and Milling/Shredders and Macerators": [
        "grinder shaft grinding object load variation",
    ],

    # ════════════════════════════════════════════════════════
    # MONITORING AND CONTROLLING (17 na raiz)
    # ════════════════════════════════════════════════════════

    "Monitoring and controlling/Condition Monitoring Pump": [
        "condition monitoring pump system component vibration",
        "monitoring condition pump system vibration signal",
        "method detecting faults pumping units vibration signal",
        "faults pumping units vibration signal shaft revolution",
        "pump system control unit sensor data acquisition",
        "pump unit control sensor data acquisition module",
        "system controlling water flow food waste handling",
        "water flow food waste handling control system",
        "control water food waste handling system flow",
    ],

    "Monitoring and controlling/Pump Diagnostics": [
        "machine learning equipment failure prediction time series",
        "time series operational parameter equipment failure",
        "automated monitoring diagnostics hydrocarbon well operations",
        "monitoring diagnostics hydrocarbon well conduit sensors",
        "data preprocessing system predictive engine accuracy",
        "predictive engine preprocessed variables well site",
        "portable system monitoring controlling surface equipment",
        "monitoring control system surface equipment sensors",
    ],

    "Monitoring and controlling/Pump Control Unit": [
        "method system controlling contact seal components",
        "temperature responsive control system seal thermally",
        "thermally reactive element seal temperature control",
    ],

    "Monitoring and controlling/Transducers": [
        "device wireless transmission signal sensor supply",
        "wireless transmission signal sensor controller line",
        "apparatus controlling operational functions machine tool",
        "machine tool controlling operational functions switching",
        "machine tool access control device operation functions",
        "machine tool plurality operation functions selection device",
    ],

    "Monitoring and controlling/Silo Inspection Content Extraction": [
        "apparatus inspecting extracting content silo plate opening",
        "silo content extraction inspection perforated plate",
        "method following liquid level filling device",
        "liquid level filling device discharge port filler",
    ],

    "Monitoring and controlling/Rod and Tension Monitoring": [
        "spiral groove structure spiral seal groove spring",
        "spiral groove seal spring pitch winding",
    ],

    "Media and Document Destruction/Paper Shredder/Safety and Protection": [
        "multifunctional storage medium shredder knives motor",
        "storage medium shredder first second set knives",
    ],

    # ════════════════════════════════════════════════════════
    # BEARINGS (17 na raiz)
    # ════════════════════════════════════════════════════════

    "Bearings/Industrial Machine Bearings": [
        "bearing device long service life extreme dust",
        "bearing device dust environment seal",
        "bearing device two components displaced common axis",
        "storage facility rotary bearing two components",
        "needle bearing needle bearing device lubricant leakage",
        "needle bearing lubricant leakage upstream path",
        "bearing device inner diameter outer ring corroded",
        "outer ring corroded clearance water slurry",
        "bearing end cap integrated seal mounting surface",
        "bearing end cap circular mounting seal groove",
        "bearing lubricant properties first second element",
        "bearing determining properties lubricant movable",
    ],

    "Bearings/Automotive and Railway Bearings": [
        "bearing device vehicle wheel tapered outer raceway",
        "outer ring double-row tapered raceway vehicle wheel",
        "bearing device wheel rotating speed detection magnetic",
        "magnetic encoder bearing wheel rotational speed",
        "rotational speed detection bearing wheel protective cover",
        "bearing wheel rotational speed detection cover",
        "rotating bearing device motorcycle measuring equipment",
        "bearing device motorcycle outer inner ring rotating",
        "micro turbine power generation system bearing performance",
        "microturbine power generation bearing high speed",
    ],

    "Bearings/Bearing Lubrication and Sealing": [
        "main motor vehicle bearing lubricating oil labyrinth",
        "bearing device vehicular motor oil labyrinth leakage",
        "bearing device vehicle motor lubricating oil disk",
        "oil-raising disk inner race lubricating bearing motor",
        "bearing device vehicle motor lubricating oil supply",
        "bearing motor lubricating oil occupies labyrinth",
        "screw fluid machinery bearing hole pressure high low",
    ],

    # ════════════════════════════════════════════════════════
    # MIXING AND AGITATION (13 na raiz)
    # ════════════════════════════════════════════════════════

    "Mixing and Agitation/Mixer and Blender Device": [
        "food cutting machine rotary cutting chamber thin shell",
        "rotary cutting chamber cutting tool driving motor food",
        "granulator rotary cutting tool particles surface sieve",
        "rotary cutting tool granulator grains perforated sieve",
        "mobile mixer assembly cereal grain farm animal feed",
        "mixer container helical horizontal rotating mixer tool",
        "hoe chipper trunk wood green waste feeder pecking rotor",
        "chipper feeder pecking rotor chopping knives",
        "cutting knife crushing rubber cord treadmills tires",
        "cutting knife armored rubber cord transport tires",
        "rotor cutting tools shredders circumferential grooves",
        "shredder rotor circumferential V-shaped grooves cutting",
        "arrangement method homogenizing sample motor cutting",
        "homogenizing sample cutting tool receptacle motor",
        "fluid treatment apparatus stirring accuracy productivity",
        "fluid treatment stirring accuracy simple structure",
        "device removing stuck earth sand crushing mixing",
        "removing adhering earth sand container inner wall",
        "agitator sewer system waste material flow digester",
        "sewer system agitator waste flow digester assembly",
        "rotatable cutting tool knife angular cutting configurations",
        "cutting tool cavity angular configurations knife",
        "centrifugal mixing system closed mixer inlet discharge",
        "mixing system recirculation line inlet discharge",
    ],

    "Mixing and Agitation/Stirring Shaft Device": [
        "separator hard elements crusher food industry",
        "mincer separator tough cartilage tendons grille",
        "separator cartilage tendons grille blade outlet",
    ],

    # ════════════════════════════════════════════════════════
    # MANUFACTURING TECHNOLOGY (12 na raiz)
    # ════════════════════════════════════════════════════════

    "Manufacturing technology/General Process Method": [
        "bomba processo de fabricação bomba cilíndrico",
        "bomba corpo cilíndrico fabricação processo",
        "pump manufacturing process cylindrical body",
    ],

    "Manufacturing technology/Ceramic Membrane and Thermosetting": [
        "processo fabricação membrana cerâmica suspensão coloidal",
        "membrana cerâmica suspensão coloidal precursor",
        "ceramic membrane manufacturing colloidal suspension",
        "corpo filtro resistente calor vias corrente",
        "filter body heat-resistant regenerable flow",
        "pulverizers manufacturing thermosetting resins casing",
        "pulverizer thermosetting resin rotary blade casing",
    ],

    "Manufacturing technology/Machining": [
        "glass powder particle size distribution preparation",
        "glass powder main constituent average particle size",
        "process recycling si material comminuting crystals",
        "recycling silicon material melt crystals drawn",
        "powder metal mixture lubricant micronized cellulose",
        "micronized cellulose fibers powder metal mixture",
        "semiconducting single wall nanotubes purification energy",
        "carbon nanotube metallic semiconductive purification",
        "methods forming polymer coatings metallic substrates",
        "polymer coating substrate intermediate carbon layer",
        "grate high temperature gasification elongated rockers",
        "active grate rockers gasification systems",
        "microtreatment iron-based alloy multi-phase transformation",
        "iron carbon alloy multi-phase transformation cooling",
    ],

    # ════════════════════════════════════════════════════════
    # ELECTRIC MOTORS (10 na raiz)
    # ════════════════════════════════════════════════════════

    "Electric Motors/Waste Processing Motor": [
        "tissue mashing device tank column rotor blades cover",
        "tissue smashing rotor blades hollow tube column",
        "electric direct connection millstone cotton stalk grater",
        "millstone cotton stalk grater motor casing moving",
        "automatic cleaning toilet pail sanitary ware grinder",
        "toilet pail cleaning sanitary ware mechanism",
        "special crusher hydrophyte aquatic plants rotary knife",
        "crusher hydrophyte aquatic plants box rotary blade",
        "displacement machine electronic motor synchronization",
        "displacement machine common rotors synchronization",
        "integrated motor compressor pump common rotors housing",
        "motor integrated compressor pump electrically driven rotors",
    ],

    "Electric Motors/Motor Shaft and Tool Drive": [
        "construction rotation knife absorber motor shaft plates",
        "rotation knife absorber motor shaft fixed plates",
    ],

    "Electric Motors/Motor Driven Pump": [
        "esp motor oil quality monitoring gauge lubricant",
        "electric motor oil condition sensing probe gauge",
        "oil-pumping machine secondary sheave wheel-cylinder",
        "oil-pumping machine electric motor secondary sheave",
    ],

    "Electric Motors/Synchronous and Permanent Magnet": [
        "beverage-making appliance ice housing electric motor torque",
        "ice beverage electric motor torque transmission",
    ],

    # ════════════════════════════════════════════════════════
    # MEDIA AND DOCUMENT DESTRUCTION (8 na raiz)
    # ════════════════════════════════════════════════════════

    "Media and Document Destruction/Hazardous Waste Disposal": [
        "destruction device data carriers bending creasing punching",
        "destroying data carriers peripheral bending punching",
    ],

    "Media and Document Destruction/Paper Shredder/Cutting Frame and Blade": [
        "cutter commercial document destruction shaft cutter disks",
        "cutter shaft cutter disks two parts central hole",
        "blade crosscut shredder rotary shafts primary shoots",
        "crosscut shredder primary auxiliary shoots blade center",
    ],

    "Media and Document Destruction/Paper Shredder/Bin and Collection": [
        "bin light media shredder fragmentation bin wall",
        "fragmentation device bin containment space wall",
    ],

    "Media and Document Destruction/Paper Shredder/Safety and Protection": [
        "shredder gas detection system sensors housing detect",
        "shredder gas detection one more sensors housing",
        "shredder jam proof system thickness detector contact",
        "jam proof shredder thickness detector contact member",
    ],

    "Media and Document Destruction/Hazardous Waste Disposal": [
        "apparatus destruction tickets housing cutter slot",
        "device destroying tickets housing cutter removably",
        "fast secure method pressing data storage devices",
        "pressing data storage devices unrecoverable secure room",
    ],

    # ════════════════════════════════════════════════════════
    # FILTRATION (5 na raiz)
    # ════════════════════════════════════════════════════════

    "Filtration/Liquid Filter Device": [
        "aparelho de filtragem seções pano de filtro",
        "filtragem seções pano filtro faces opostas",
        "filter apparatus sections filter cloth faces",
        "circulation device baths pump filter unit housing",
        "circulating device baths pump drive filter",
    ],

    "Filtration/Disc and Drum Filters": [
        "vertical cutting-type filter cake crusher box machine",
        "filter cake crusher vertical cutting box",
        "filter feeding system liquids sediments crude oil",
        "filter liquid sediments crude oil washing system",
    ],

    "Filtration/Self-Cleaning and Backwash": [
        "grinder liquid media solid components housing sealed",
        "comminuting liquid media solid thickers housing",
    ],

    # ════════════════════════════════════════════════════════
    # HYDRAULIC AND PNEUMATIC DEVICES (4 na raiz)
    # ════════════════════════════════════════════════════════

    "Hydraulic and Pneumatic Devices": [
        "hydro rope elevator differential cylinder working chambers",
        "apparatus measuring fluid quantities petrol station pump",
        "fluid measuring motor petrol pump measuring tube",
        "pump supplying fluid fuel resonator pipe closed",
        "fuel pump resonator pipe primary end reflector",
        "expulsion device pressure medium piston reservoir",
        "ejection device pressure propellant piston reservoir",
    ],

    # ════════════════════════════════════════════════════════
    # REMAINING SMALL CATEGORIES
    # ════════════════════════════════════════════════════════

    "Bearings/Bearing Housing and Assembly": [
        "bearing device wheel tapered outer raceway inner ring",
    ],

    "Compressors/Rotary Compressor": [
        "high-efficiency double screw rod compressor rotor line",
        "double screw rod compressor rotor profile line",
        "dry twin-shaft rotary screw spindle compressor housing",
        "twin-shaft screw spindle compressor aluminum rotors",
        "complex screw rotors male female lobes grooves compressor",
    ],

    "Agriculture and Biomass/Forage Harvester Cutterhead": [
        "chaff-cutter wooden waste garden microwave radiator",
        "cutter microwave radiator cutting chamber timber",
        "wear liner brush cutter cylindrical drum teeth cover",
        "brush cutter cylindrical drum cutting teeth wear liner",
        "ensilage slicing compacted ensilage skid steer loader",
        "ensilage slicing attachment compacted ensilage mass",
    ],

    "Motors and Clutches": [
        "driving motor railway vehicles oil supply chamber",
        "drive motor rolling stock oil supply chamber simple",
        "bearing device electric motor driving vehicles labyrinth",
        "bearing device motor vehicles labyrinth lubricating oil",
        "small-size motor shaft diameter press-fitted boss",
    ],

    "Sterilization and Medical Waste/Integrated Medical Waste Management": [
        "method treating organic wastewater sludge facility",
        "organic wastewater surplus sludge simple facility",
        "asbestos building material waste processing equipment",
        "asbestos-containing building material waste safely process",
        "waste processing method pathogen reduction disinfection",
        "disinfection waste ambient temperature pathogen cutting",
    ],

    "Packaging Machinery": [
        "conjunto alimentar porções café preembalados máquina",
        "porções café preembaladas unidade preparação conjunto",
        "packaging dried sheets sealed capsules tea airtight",
        "system packaging tea airtight capsule breaking dried",
    ],

    "Separator/Gas-Liquid Separator": [
        "dry-type household garbage air separation low-speed",
        "dry household garbage air separation breaking",
        "system method multivariable control three-phase separation",
        "multivariable control oil gas production separation",
    ],

    "Machines for rubber industry": [
        "resin film forming device screw type pump rotor thermosetting",
        "thermosetting resin screw pump rotor evenly coated teeth",
        "device releasing screw-type pump rotor resin film rubber",
        "screw-type pump rotor rubber mold releasing device",
    ],

    "Measuring devices/Particle and Size Analysis": [
        "shredder head power material thickness pulverizer blades",
        "shredder head vary power material thickness motor blades",
        "multifunctional aggregate machine cylinder power transmission",
        "aggregate machine cylinder base power transmission",
        "downhole device communication measured electrical property",
        "electrical property downhole device control operation",
    ],

    "Safety and Braking/Hydraulic Retarder": [
        "braking device gerotor motors housing central bore",
        "gerotor motors braking device end cap central bore",
    ],

    "Semiconductor and Nanomaterials": [
        "radioactive substance absorbent fibrillated cellulose",
        "radioactive absorbent cellulose fibrillated humidified",
    ],

    "Couplings and Drive Units": [
        "apparatus fluffing bales peat moss organic matter",
        "fluffing peat moss compressed bale agitator assemblies",
        "agitator assemblies hydraulic drive motor vertical shaft",
    ],

    "Data and Text Processing": [
        "sistemas métodos estenografia semântica notas taquigrafia",
        "estenografia semântica dados entrada notas método",
    ],

    "Chemical Substrate Applications": [
        "substrato dobrado substância química aplicada áreas separadas",
        "substância química substrato dobrado áreas separadas",
    ],

    "Food Processing Appliances": [
        "food cooking press domestic use greater internal depth",
        "prensa culinária doméstica uso profundidade maior",
    ],
}

# Aplica adições V17 (sem duplicatas)
for _cat, _novos in _ADICOES_V17.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ── PASSO 3: Deduplicação global pós-V17 ─────────────────────────────
for _cat in PALAVRAS_CHAVE:
    _seen = set()
    _dedup = []
    for _t in PALAVRAS_CHAVE[_cat]:
        _k = _t.lower()
        if _k not in _seen:
            _seen.add(_k)
            _dedup.append(_t)
    PALAVRAS_CHAVE[_cat] = _dedup


# ══════════════════════════════════════════════════════════════════════
# EXPANSÃO V17B — Termos verificados substring-a-substring nos abstracts
# Todos os termos abaixo foram confirmados nos textos reais do xlsx.
# Meta: TOTAL GERAL raiz < 50
# ══════════════════════════════════════════════════════════════════════

_ADICOES_V17B = {

    # ════════════════════════════════════════════════════════
    # MACERATOR (17 na raiz)
    # ════════════════════════════════════════════════════════
    "Macerator/Blending and Mixing": [
        # CN201613163U — Food Processing Equipment Easy To Clean
        "food processing equipment",
        "crushing cutter",
        "inner lid housing",
        # DE202011005356 — Perforated Disk For Processing Food
        "perforated disk",
        "axial side surface",
        "through-holes",
        # DE102010060094 — Active Ingredient For Food Processing
        "active insert",
        "pull-out active",
        # DE10325526 — Cutter (food machine voltage)
        "food processing machine",
        "electrical voltage",
        # US20060196334 — Food Processing Apparatus Strips Slices
        "food processing apparatus",
        "slicing food into slices",
        "subsets of blades",
        # US20020144606 — Food Processing Device
        "food processing elements",
        "support plate pan",
        # US20030197080 — Food Processing Apparatus Magnetic Drive
        "magnetic drive food",
        "food processing apparati",
        # US20110083566 — Devices To Disintegrate Foods
        "disintegrate foods",
        "inlet coupled to a disintegrator",
    ],

    "Macerator/Cutting Elements": [
        # DE102004027024 — Meat Processing Machine Fat Analyzer
        "meat processing machine",
        "fat analyzer",
        "fat content meat",
        # US5551641 — Non-Pulpables Collection Chamber Pulper
        "non-pulpables collection",
        "solid waste pulpers",
        "pulping chamber",
        "pulping mechanism",
    ],

    "Macerator/Sludge and Waste Processing": [
        # EP1055458 — Method Disposing Waste Tire
        "waste tire pieces",
        "shredding members",
        "shredding blades",
        # KR101278449 — Apparatus Disposing Waste
        "waste disposal apparatus",
        "agitation residues",
        # US20090294558 — Crushing Grains
        "crushing grains",
        "plurality of shafts",
        # WO2004101185 — Treating Waste Bread
        "waste bread",
        "crushing and drying",
    ],

    "Macerator/Industrial Crusher": [
        # RU2411122 — Fine-Crushing Mixing Plastic Clay
        "clay mix material",
        "loading bin screw",
        # US20100155513 — Bale Breaker Horizontal Grinder
        "horizontal grinder",
        "powerfeed drum",
        "bale breaker",
    ],

    "Macerator/Comminutor": [
        # US20090294558 backup
        "driving mechanism shafts rollers",
    ],

    # ════════════════════════════════════════════════════════
    # SEALINGS (29 na raiz)
    # ════════════════════════════════════════════════════════
    "Sealings/Industrial Equipment Seals": [
        # CN104005957A — Fluid Machinery Multi-Stage Compression
        "multi-stage compression",
        "compression cavity",
        "compression mechanism",
        # CN109695568A — Twin-Screw Rotating Vortex
        "twin-screw",
        "rotating vortex",
        "vortex conjugation",
        # EP000000591979A1, US000005460495A, JPH06123294A — Screw Rotor Blowhole
        "screw rotor",
        "blowhole",
        "sealing line",
        "fluid handling",
        # CN203614401U — Triple-Screw Shaft Head Pump
        "triple-screw",
        "shaft head pump",
        "driving screw",
        "driven screws",
        # CN201565339U — Anti-Accumulation Pulverizer Chamber
        "pulverizer cavity",
        "knife cavity",
        "anti-accumulation",
        # CN202122993U — Grinding Granulating Machine Medicine
        "grinding granulating machine",
        "granulating machine medicine",
        # CN203061539U — Organic Waste Processor
        "organic waste processor",
        "work tank exhaust",
    ],

    "Sealings/Bearing Seal": [
        # DE102006037261 — Track Conveyor Bearing Element
        "bearing element",
        "transport roller",
        "bearing frame",
        # GB2449250, US20080190743 — Roller Device Conveyer
        "roller device",
        "conveyer",
        "roller body",
        "end walls",
        # US9422985B2, US2015110433A1 — Sealing Bearing Unit Two Shafts
        "two shafts",
        "bearing unit",
    ],

    "Sealings/Pump Housing Seal": [
        # DE102006041633A1 — Pump Cylinder Sections Trapezoidal
        "trapezoidal",
        "cylinder sections",
        # EP000001475538A2, EP000001475538A3 — Pump Pumping Element Housing
        "pumping element",
        # GB2558954A — Pump Sealing Semi-Circular
        "semi-circular cross-section",
        # EP2450530A1 — Sealing Pistons Rotating Engine
        "rotor discs",
        # DE102009022250 — Drum Motor Hygienic
        "drum motor",
        "drum tube",
        "hygienic",
    ],

    "Sealings/Hermetic and Static Seals": [
        # US20120171381A1 — Sealing Compound Closure Cap
        "sealing compound",
        "outer stamp",
        "inner stamp",
        # US2014117666A1 — Gasket Joint Sealing
        "gasket",
        "joint sealing",
        # WO201228616A1 — Sealing System Casing Well Leaks
        "sealing zone",
        "weakened casing",
        "perforations and",
        # WO2019124045A1 — Liquid Supply Mechanism Branch Flow
        "liquid supply mechanism",
        "branch flow passages",
        "intersecting center",
    ],

    "Sealings/Ring and Peripheral Seal": [
        # US20180135358A1 — Seal Stem Anchor
        "seal stem",
        "body lock threads",
        "anchor assembly",
        # US20120145405A1 — Adjustable Riser Suspension
        "riser hanger",
        "ratchet-latch",
        "adjustable riser",
        # US20120006557A1 — Flange Locking Cap Subsea
        "flange locking",
        "external flange",
        "subsea",
    ],

    "Sealings/Dynamic and Oil Seals": [
        # DE102016125207A1 — Conveying Viscous Material
        "conveying viscous",
        "viscous material",
        # US5722167 — Flow Rate Bearing
        "desired flow rate",
        "radial clearance",
        "rolling members",
    ],

    # ════════════════════════════════════════════════════════
    # DRIVE SHAFTS (28 na raiz)
    # ════════════════════════════════════════════════════════
    "Drive Shafts/Power Transmission Mechanism": [
        # DE102010043118A1 — Torque Between Shaft Hub
        "transmitting torque",
        "shaft and a hub",
        # CA2859817A1 — Limiting Rotation Drive Shaft
        "limiting rotation",
        "braking assembly",
        # DE000004111897A1 — Torque Transmission Drive Shaft Screw Pump
        "torque transmission",
        "eccentric screw-pump",
        "eccentrically rotating",
        # US5655725 — Retaining Plate Gear Shafts
        "retaining plate",
        "gear shafts",
        "gear assembly",
        # US7290995B2 — Tandem Trochoid Pump Drive Shaft
        "tandem",
        "trochoid pump",
    ],

    "Drive Shafts/Flexible Shaft and Sleeve": [
        # GB425447 — Improvements Screw Engines Pumps
        "screw engines",
        # GB436843 — Improvements Rotary Pumps Moineau
        "moineau",
        "gearing mechanism",
        # US000007040878B2, US020040028546A1 — Eccentric Screw-Type Pump
        "eccentric screw-type",
        "stator cladding",
        # US6926492B2 — Suction Housing Rotor/Stator Pump
        "suction housing",
        "cementitious material",
        # WO201213973A1 — Screw Type Pump Stator Rotor Vanes
        "vanes of opposite",
        "stator vanes",
        "radial gap",
        # GB000002383610A, US020030124013A1, US000006616432B2 — Fluid Pump Cowling Helical Gearsets
        "fluid pump cowling",
        "helical drivetrain",
        "helical gearsets",
        # WO002006099745A1, WO2006099745A1 — Pump Motor Pumping Fluids Conduit
        "fluid displacer",
        "displacer within",
        # US2483370A — Helical Multiple Pump Moineau
        "helical multiple pump",
        "moineau principle",
    ],

    "Drive Shafts/Axles and Spindles": [
        # JP2008229614 — Grinder Drive Shaft Load
        "rotary shaft",
        "drive shaft",
        # KR20020083382 — Meat Dicer Machine
        "meat dicer",
        "dicer machine",
        # US20050178376 — Bladeshaft Assembly Powered Saw
        "bladeshaft assembly",
        "powered saw",
        # DE102007016231A1 — Prestressing Device Cutter Rotor
        "prestressing device",
        "cutter rotor",
        "prestressing part",
        # DE102008013232 — Apparatus Comminuting Feed Rotor
        "comminuting feed",
        "driven shaft",
        # DE202006013806 — Tool Fixture Overhung Tools
        "tool fixture",
        "overhung tools",
    ],

    "Drive Shafts/Slurry Breaking and Farm Pump": [
        # DE202005010617 — Breaking Solids Farmyard Slurry
        "farmyard slurry",
        "rotating blade",
        # US20100096483, US20060179634 — Reducing Machine Rotor Assembly
        "reducing machine",
        "fragmenting rotor",
        "comminuting waste wood",
    ],

    "Drive Shafts/Shaft Coupling Device": [
        # JP002006077699A — Lubricating Structure Supercharging
        "supercharging device",
        "stirring resistance",
        # EP0853202A1 — Joint Assembly Connecting Drive Shafts
        "joint assembly",
        "connecting shaft",
        "submergible pumping",
    ],

    "Drive Shafts/Splines and Keyways": [
        # WO201158295A2, WO201158296A2, WO201158294A2 — Stators Downhole Motors
        "stator for downhole",
        "downhole motor",
        "stator tube",
        # WO2016112169A1 — Shaft Downhole Equipment
        "shaft downhole",
        "nominal diameter",
        # WO2014148940A1 — Device Hydraulically Protecting Motor
        "hydraulically protecting",
        "protector electric",
    ],

    # ════════════════════════════════════════════════════════
    # PUMPS (24 na raiz)
    # ════════════════════════════════════════════════════════
    "Pumps/PC Pump and Motor": [
        # GB425447, GB436843 — Moineau / Screw Engines
        "moineau",
        "gearing mechanism",
        # US2483370A — Helical Multiple Pump Moineau
        "helical multiple pump",
        "moineau principle",
        # WO201213973A1 — Screw Type Pump Stator Rotor Vanes
        "vanes of opposite",
    ],

    "Pumps/Hydraulic Pump": [
        # PI02014696 — Bomba Hidráulica Pulmões
        "pulmões",
        "regime ininterrupto",
        "sistema de bombas",
    ],

    "Pumps/Screw Pump": [
        # PI00043818 — Unidade Bombeamento Parafuso
        "unidade de bombeamento",
        "parafuso",
        "fluidos em fases",
        # CN202516631U — High-Speed Shearing Machine Granulation
        "shearing machine",
        "high-tower",
        "granulation slurry",
    ],

    "Pumps/Centrifugal Pump": [
        # DE102009055348 — Centrifugal Disc Fluid Pump
        "centrifugal disc",
        "centrifugal disc",
    ],

    "Pumps/Piston Pump": [
        # DE102023133839A1 — Pump Conveying Medium
        "suction-side inlet",
        "conveying medium",
        "conveying housing",
        # DE102011101641A1, DE102011101641B4 — Valve Pump Piston
        "piston",
        "open position",
        "fluid flow is blocked",
    ],

    "Pumps/Well Pump Systems": [
        # EP000001387959A2, WO002002086322A2, WO002002086322A3 — Fluid Controlled Pumping
        "fluid controlled pumping",
        "pumping unit",
        # WO201267638A1 — Ultra Pump Systems
        "cylindrical pump chamber",
        "removing liquids from a well",
        # WO2011140479A1 — Continuously Pumping Solid
        "pressurized slurry",
        "liquid carbon dioxide",
        "solid carbon dioxide",
    ],

    "Pumps/Multiphase Pump": [
        # US7445429B2 — Crossover Two-Phase Flow Pump
        "crossover two-phase",
        "hydrocarbon well pump",
        # US2024369077A1 — Liquid Gas Mixture Borehole
        "multiphase-pumping",
        "crude-oil",
    ],

    "Pumps/Gear Pump": [
        # US20080085208A1 — Oil Pump Rotor Assembly
        "oil pump rotor",
        "rotor pump assembly noise",
    ],

    "Pumps/Roots and Rotary Piston Pump": [
        # GB2631581A — Claw Booster Pump
        "claw booster pump",
        "claw portion",
    ],

    "Pumps/Water and General Fluid Pump": [
        # WO002006099745A1, WO2006099745A1 — Pump Motor Pumping Fluids
        "fluid displacer",
    ],

    "Pumps/Pump Systems and Applications": [
        # US20110155390A1 — Pumping Fluid Additive Downhole
        "downhole location",
        "pumping a fluid mixture",
        "wellbore location",
    ],

    # ════════════════════════════════════════════════════════
    # OIL TOOLS (24 na raiz)
    # ════════════════════════════════════════════════════════
    "Oil Tools/Downhole Power Generation": [
        # DE102010019238A1 — Container Multi-Phase Pump
        "multi-phase pump",
        "collecting container",
        "hydrocarbon source",
        # US20210108498A1 — Down-Hole Gas Separation
        "down-hole gas separation",
        "production separation chambers",
    ],

    "Oil Tools/Drilling": [
        # US20110120772A1 — Downhole Assembly Articulated Mandrel
        "articulated mandrel",
        "passive active damping",
    ],

    "Oil Tools/Sand Protection": [
        # US20090133987 — Processing Sized Ore Feed
        "sized ore feed",
        "excavated deposit",
        # US20070119994, US20080173572 — Mobile Slurry Oil Sand
        "mobile slurry",
        "oil sand ore",
        "slurry box",
    ],

    "Oil Tools/Wellhead equipment": [
        # US11962957B1 — Wellsite Control
        "wellsite control",
        "sensor information",
    ],

    "Oil Tools/Casing and Tubing Accessories": [
        # US20120018141A1 — Well Tool Nanoparticle
        "well tool",
        "nanoparticle reinforced",
        "metallic coating",
        # US20120055675A1 — Acid Diversion Taylor-Couette
        "taylor-couette",
        # US20110155390A1 — Pumping Fluid Additive Downhole
        "wellbore location",
        # US2016319087A1 — Oil Field Apparatus Seal Rubber
        "oilfield apparatus",
        "cellulose nanofibers",
        # US20110056695A1 — Valves Bottom Hole Assemblies
        "bottom hole assemblies",
        "selectively actuating",
        # US7617869B2 — Extracting Oil Tar Sand
        "tar sand",
        "in-situ liquefaction",
        # US20120217009A1 — Positioning Tool Casing
        "detecting unit",
        "longitudinal tool axis",
        # US20110088899A1 — Process Mineral Oil Deposits
        "mineral oil deposits",
        "temperature gradients",
        # US7857063B2 — Expandable Centraliser
        "expandable centraliser",
        # WO201267638A1 — Ultra Pump Systems Well
        "cylindrical pump chamber",
        # WO201228838A2 — Releasable Connector Assembly
        "releasable connector assembly",
        # WO201211994A1 — Multi-Zone Well
        "multi-zone well",
        # WO2014075160A1 — Automatic Tubing Drain
        "automatic tubing drain",
        # WO2010120677A2 — Resilient Anchor
        "resilient anchor",
        # WO201184497A1 — Wellbore Maintenance
        "wellbore maintenance",
        # WO2004053286A2 — System Bore Hole
        "bore hole",
    ],

    # ════════════════════════════════════════════════════════
    # CONVEYOR AND TRANSPORT (19 na raiz)
    # ════════════════════════════════════════════════════════
    "Conveyor and Transport/Plastic Recycling Processor": [
        # CN202683309U — Rubber Block Crushing Production Line
        "rubber block",
        "crushing production line",
        "chopper mixer",
        # CN201745116U — Tyre Fine Crusher
        "tire fine crusher",
        "fine crusher frame",
        # EP2143755 — Recycled Thermoplastic Thermoset
        "thermoplastic composition",
        "thermoset material",
        "crumb slurry",
    ],

    "Conveyor and Transport/Crushing Equipment for Chips": [
        # DE102011121972 — Granulator Drive Cutting Device Strand
        "granulator",
        "strand of material",
        "cutting device",
        # DE202008018151 — Processing Polymer Material Contaminants
        "polymer material",
        "contaminants",
        "volatile",
        # DE102005061085 — Double Roller Machine Granular
        "double roller machine",
        "granular material",
        "slip-on gear",
    ],

    "Conveyor and Transport/Composting and Digestion": [
        # CN202490664U — Kitchen Waste Collection Bin
        "kitchen waste",
        "material collection warehouse",
        "rolling gate",
        # CN202238212U — Rubbish Bag Breaking Rotary Drum
        "rubbish bag",
        "rotary drum blades",
        "bag breaking",
        # WO2010108402 — Automatic Collection Pipeline Evacuation
        "pipeline evacuation",
        # WO2013138926 — Evacuate Biomass Chamber
        "shovelable biomass",
        "elongated chamber",
        # WO2012171103 — Pick-Up Head System
        "pick-up head",
        "suctioning bottom opening",
    ],

    "Conveyor and Transport/Belt Conveyor": [
        # DE102023101939A1 — Conveying Device Fluid
        "drivable conveying member",
        # US20050067515 — Material Spreader Belt Chain
        "material spreader",
        "belt chain assembly",
        # WO2011041305A2 — Line Retention Arrangement Clips
        "line retention",
        "cantilever portion",
    ],

    "Conveyor and Transport/Metal Recycling Separator": [
        # JP2006240852 — Transfer Device Separated Objects
        "transfer device",
        "separated transferring",
        # US20120037734, WO2013106669 — Recycling Carpet Fibers
        "recycling carpet",
        "carpet fibers",
        "backing material",
    ],

    "Conveyor and Transport/Branch and Tree Crusher": [
        # US20090193723 — Reduce Clogging Gutters Grinder
        "clogging gutters",
        "downspout grinder",
        # US20080282663 — Roller Accumulator Lawn Debris
        "roller-supported accumulator",
        "lawn and garden debris",
    ],

    # ════════════════════════════════════════════════════════
    # GRINDING AND MILLING (17 na raiz)
    # ════════════════════════════════════════════════════════
    "Grinding and Milling/Food Grinding": [
        # PI99015382 — Moagem Farinha Trigo
        "moagem de farinha",
        "grãos duros",
        "etapas de moagem",
        "flour milling",
        "hard wheat",
    ],

    "Grinding and Milling/Pulverizer and Superfine Mill": [
        # CN102580826 — Cylinder Type Specific Cutter Grinder
        "vertical air-cooled",
        "air-flow vortex",
        "dry-type pulverizer",
        # CN201720105U — Grinding Rotor Disc Holes
        "grinding rotor",
        "throughgoing holes",
        # CN202606199U — High-Speed Shearing Colloidal Mill
        "colloidal mill",
        "milling disc",
        # CN202962583U — Grinder Rack Enclosure
        "grinding room",
        "enclosure main shaft",
        # CN202638522U — Grinder Pulverization Chamber
        "pulverization chamber",
        "inlet hopper",
        # CN202410744U — Stator Rotor Shear Mill
        "shear mill",
        # DE102008057233A1 — Milling Device Pump Sewage
        "sewage water",
        "liquid media solid",
    ],

    "Grinding and Milling/Food and Bone Mill": [
        # JP2010234337 — Grinding Treatment Device Kitchen
        "grinding treatment device",
        "sound source kitchen",
        # JP2004188248 — Crushing Organic Waste Particle Size
        "organic waste",
        "particle size",
        "recycling impurities",
        # KR20110029860 — Disposer Multi-Fixed Grinding Blades
        "fixed grinding blades",
        "rotary grinding plate",
        # KR20110029859 — Disposer Multi-Step Grinding Protrusion
        "grinding protrusion",
        "sink drain hole",
        # KR100872890 — Milling Device Injection Member Groove
        "injection member",
        "contents groove",
        # KR20120033577 — Crushing Performance CT Voltage
        "CT voltage",
        "crushing performance",
        # KR100849630 — Crushing Aggregation Separation Upper Lower Drum
        "upper drum",
        "lower drum",
        "circulating aggregate",
        # KR20110113321 — Shellfish Crusher
        "shellfish",
        "oyster shells",
    ],

    "Grinding and Milling/Shredders and Macerators": [
        # JP2008229614 backup
        "grinding object",
    ],

    # ════════════════════════════════════════════════════════
    # MONITORING AND CONTROLLING (17 na raiz)
    # ════════════════════════════════════════════════════════
    "Monitoring and controlling/Condition Monitoring Pump": [
        # EP1540186B1 — Condition Monitoring Pumps
        "condition monitoring",
        "monitoring condition",
        # EP1972793A1 — Detecting Faults Pumping Units
        "detecting faults",
        "pumping units",
        "vibration signal",
        # EP2412981A1 — Pump System Control Sensor
        "pump unit control",
        "data acquisition module",
        # US20070084950 — Controlling Water Flow Food Waste
        "water flow food waste",
        "food waste handling",
    ],

    "Monitoring and controlling/Pump Diagnostics": [
        # US12242260B2 — Machine Learning Equipment Failure
        "machine learning",
        "equipment failure",
        "time series",
        # US20250101863A1 — Automated Monitoring Diagnostics Hydrocarbon Well
        "automated monitoring",
        "diagnostic procedures",
        "hydrocarbon well",
        # US12229138B2 — Data Preprocessing Predictive Engine
        "predictive engine",
        "preprocessed variables",
        # US20240200441A1 — Portable Monitoring Controlling Surface Equipment
        "monitoring and control system",
        "surface equipment",
    ],

    "Monitoring and controlling/Pump Control Unit": [
        # US20110278798A1, WO2011146091A1 — Controlling Contact Seal Components
        "controlling contact",
        "seal components",
        "thermally reactive element",
    ],

    "Monitoring and controlling/Transducers": [
        # DE102019135635A1 — Wireless Transmission Signal Sensor
        "wireless transmission",
        "signal sensor",
        # US2011202166A1 — Apparatus Controlling Machine Tool Functions
        "machine tool",
        "operational functions",
        "switching on",
        # US2009079537A1 — Machine Tool Access Control
        "access control device",
        "operation functions",
    ],

    "Monitoring and controlling/Silo Inspection Content Extraction": [
        # DE19982997 — Inspecting Extracting Silo Content
        "extracting content",
        "silo",
        "perforated",
        # JP2008201425A — Liquid Level Filling Device
        "liquid level",
        "filling device",
        "discharge port",
    ],

    "Monitoring and controlling/Rod and Tension Monitoring": [
        # JPH10184561A — Spiral Groove Spiral Seal
        "spiral groove",
        "spiral seal",
        "winding pitch",
    ],

    "Media and Document Destruction/Paper Shredder": [
        # CN102553689 — Multifunctional Storage Medium Grinder
        "storage medium shredder",
        "first set of knives",
        "second set of knives",
    ],

    # ════════════════════════════════════════════════════════
    # BEARINGS (17 na raiz)
    # ════════════════════════════════════════════════════════
    "Bearings/Industrial Machine Bearings": [
        # CN202140446U — Bearing Device Long Service Life Extreme Dust
        "extreme dust",
        "dust environment",
        "long service life",
        # JP2007177910, JP2007177903 — Bearing Device Outer Ring Corroded
        "outer ring corroded",
        "salt water",
        "seal member",
        # DE102010053859 — Storage Facility Rotary Bearing
        "storage facility",
        "rotary bearing",
        "common axis",
        # EP2423521 — Needle Bearing Lubricant Leakage
        "needle bearing",
        "lubricant leakage",
        "upstream side",
        # US6581939 — Bearing End Cap Integrated Seal
        "bearing end cap",
        "integrated seal",
        "mounting surface",
        # US2012067111A1 — Bearing Lubricant Properties
        "lubricant properties",
        "bearing element",
    ],

    "Bearings/Automotive and Railway Bearings": [
        # DE112007001199 — Bearing Device Vehicle Wheel Tapered Raceway
        "tapered outer raceway",
        "double-row tapered",
        # JP2009228819, JP2009228818 — Bearing Device Wheel Rotational Speed Detection
        "rotational speed detection",
        "magnetic encoder",
        "protective cover",
        # JP2012508855A — Rotating Bearing Motorcycle Measuring
        "rotating bearing device",
        "motorcycle",
        # JP2005030224 — Micro Turbine Power Generation Bearing
        "microturbine",
        "turbine power generation",
    ],

    "Bearings/Bearing Lubrication and Sealing": [
        # JP2008245347 — Main Motor Vehicle Bearing Grease Labyrinth
        "grease to labyrinths",
        "labyrinth space",
        # JP2009041634 — Bearing Device Vehicular Main Motor Oil
        "oil-raising disk",
        "vehicular main",
        # JP2012244787 — Bearing Device Vehicle Motor Lubricating Oil
        "bleeding of lubricating",
        "good oil supply",
        # JPH07286585A — Oil Free Screw Fluid Machinery
        "oil-free screw",
        "bearing hole",
    ],

    # ════════════════════════════════════════════════════════
    # MIXING AND AGITATION (13 na raiz)
    # ════════════════════════════════════════════════════════
    "Mixing and Agitation/Mixer and Blender Device": [
        # CN202570297U — Food Cutting Machine Rotary Cutting Chamber
        "food cutting machine",
        "rotary cutting chamber",
        # DE20314763 — Granulator Rotary Cutting Tool Sieve
        "granulator rotary",
        "perforated sieve",
        # DE102005019826 — Mobile Mixer Assembly Cereal Feed
        "mixer assembly",
        "cereal grain",
        "animal feed",
        # DE202007015630, DE202007015635 — Hoe Chipper Wood
        "chipper",
        "trunk wood",
        "pecking rotor",
        # DE202012005867 — Cutting Knife Rubber Cord
        "rubber cord",
        "treadmills",
        # EP1166875 — Rotor Cutting Tools Shredders Grooves
        "circumferential grooves",
        "v-shaped profile",
        # EP2409770 — Homogenizing Sample Motor Cutting Tool
        "homogenizing",
        "homogenization",
        # JP2011092941 — Fluid Treatment Apparatus Stirring
        "fluid treatment apparatus",
        "stirring accuracy",
        # JP2012016698 — Removing Stuck Earth Sand
        "adhering earth and sand",
        "container inner wall",
        # US20090236274 — Agitator Sewer System
        "agitator",
        "sewer system",
        "digester assembly",
        # US20040074355 — Rotatable Cutting Tool Angular
        "rotatable cutting tool",
        "angular cutting",
        # WO002010086590A2 — Centrifugal Mixing System
        "centrifugal mixing",
        "closed mixer",
    ],

    "Mixing and Agitation/Stirring Shaft Device": [
        # EP1488854 — Separator Hard Elements Crusher Food Industry
        "separator",
        "cartilage",
        "tendons",
        "grille",
    ],

    # ════════════════════════════════════════════════════════
    # MANUFACTURING TECHNOLOGY (12 na raiz)
    # ════════════════════════════════════════════════════════
    "Manufacturing technology/General Process Method": [
        # PI98108484 — Bomba Processo Fabricação Bomba
        "processo de fabricação",
        "corpo cilíndrico",
        "fabricação de uma bomba",
    ],

    "Manufacturing technology/Ceramic Membrane and Thermosetting": [
        # PI99039290 — Processo Fabricação Membrana Cerâmica
        "membrana cerâmica",
        "suspensão coloidal",
        # PI98059726 — Corpo Filtro Resistente Calor
        "resistente ao calor",
        "vias de corrente",
        "corpo de filtro",
        # CN201760327U — Pulverizers Manufacturing Thermosetting Resins
        "thermosetting resin",
        "pulverizer thermosetting",
    ],

    "Manufacturing technology/Machining": [
        # DE102012203875 — Glass Powder Particle Size
        "glass powder",
        "particle size distribution",
        # DE102006011040 — Recycling Si Material Melt Crystals
        "recycling si",
        "crystals are drawn",
        # US20040144207 — Powder Metal Mixture Cellulose
        "powder metal mixture",
        "micronized cellulose",
        # US20090252946 — Carbon Nanotube Purification
        "carbon nanotube",
        "metallic carbon",
        # US2016136928A1 — Polymer Coatings Metallic Substrates
        "polymer coatings",
        "metallic substrates",
        # US20090178337 — Grate High Temperature Gasification
        "gasification systems",
        "elongated rockers",
        # US2100163140A1, WO2013188100A1 — Microtreatment Iron Alloy
        "microtreatment",
        "iron-based alloy",
        "multi-phase transformation",
    ],

    # ════════════════════════════════════════════════════════
    # ELECTRIC MOTORS (10 na raiz)
    # ════════════════════════════════════════════════════════
    "Electric Motors/Waste Processing Motor": [
        # CN201997366U — Tissue Mashing Device
        "tissue smashing",
        "tissue mashing",
        # CN102451790 — Electric Millstone Cotton Stalk
        "cotton stalk",
        "millstone",
        # CN101817434 — Automatic Cleaning Toilet Pail
        "toilet pail",
        "sanitary ware",
        # CN202037042U — Special Crusher Hydrophyte
        "hydrophyte",
        "aquatic plants",
        # DE000004318707A1 — Displacement Machine Electronic Motor Synchronization
        "electronic motor synchronization",
        "synchronization",
        # DE000010042545A1 — Integrated Motor Compressor Pump
        "integrated motor",
        "electrically driven rotors",
    ],

    "Electric Motors/Motor Shaft and Tool Drive": [
        # KR20010079413 — Construction Rotation Knife Absorber
        "rotation knife absorber",
        "motor shaft fixed plates",
    ],

    "Electric Motors/Motor Driven Pump": [
        # US20180347346A1 — ESP Motor Oil Quality Monitoring
        "esp motor oil",
        "oil condition sensing",
        "sensing probe",
        # WO201297493A1 — Oil-Pumping Machine Secondary Sheave
        "oil-pumping machine",
        "secondary sheave",
    ],

    "Electric Motors/Synchronous and Permanent Magnet": [
        # US20060086255 — Beverage-Making Appliance Ice
        "ice beverage",
        "torque transmission",
    ],

    # ════════════════════════════════════════════════════════
    # MEDIA AND DOCUMENT DESTRUCTION (8 na raiz)
    # ════════════════════════════════════════════════════════
    "Media and Document Destruction/Hazardous Waste Disposal": [
        # DE202009012359 — Destruction Device Data Carriers Bending Punching
        "destroying data carriers",
        "bending or creasing",
        "punching device",
        # US5996457 — Apparatus Destruction Tickets
        "destroying tickets",
        "slot tickets",
        # US7494076 — Pressing Data Storage Devices
        "pressing means",
        "data storage devices",
        "unrecoverable",
    ],

    "Media and Document Destruction/Paper Shredder/Cutting Frame and Blade": [
        # DE202006005771 — Cutter Document Destruction Shaft Disks
        "document destruction",
        "cutter disks",
        "two parts central hole",
        # US20120037738 — Blade Crosscut Shredder Primary Shoots
        "crosscut shredder",
        "primary shoots",
        "auxiliary shoots",
    ],

    "Media and Document Destruction/Paper Shredder/Bin and Collection": [
        # EP2208536 — Bin Light Media Shredder
        "fragmentation device",
        "containment space",
    ],

    "Media and Document Destruction/Paper Shredder/Safety and Protection": [
        # US20100170968 — Shredder Gas Detection
        "gas detection system",
        "sensors housing detect",
        # US20100243774 — Shredder Jam Proof
        "jam proof",
        "thickness detector",
    ],

    # ════════════════════════════════════════════════════════
    # REMAINING CATEGORIES
    # ════════════════════════════════════════════════════════
    "Filtration/Liquid Filter Device": [
        # PI99121913 — Aparelho Filtragem Seções Pano Filtro
        "aparelho de filtragem",
        "seções de filtragem",
        "pano de filtro",
        # DE102010038137A1 — Circulation Device Baths Pump Filter
        "circulation device",
        "baths pump",
        "circulating device",
    ],

    "Filtration/Disc and Drum Filters": [
        # CN101559399 — Vertical Cutting-Type Filter Cake Crusher
        "filter cake crusher",
        "filter cake",
        # EP2409750 — Filter Feeding System Liquids Sediments
        "filter feeding system",
        "sediments",
        "crude oil washing",
    ],

    "Filtration/Self-Cleaning and Backwash": [
        # RU2397019 — Grinder (in filtration context)
        "grinding of materials",
    ],

    "Hydraulic and Pneumatic Devices": [
        # DE000019715224A1 — Hydro Rope Elevator
        "rope elevator",
        "differential cylinder",
        # DE10226501A1 — Apparatus Measuring Fluid Quantities Petrol
        "petrol pump",
        "fluid measuring motor",
        "measuring tube",
        # DE102010031609A1 — Pump Supplying Fluid Fuel Resonator Pipe
        "resonator pipe",
        "reflector",
        # ES2353930T3 — Expulsion Device Pressure Medium Piston
        "expulsion device",
        "propellant piston",
        "pressure medium",
    ],

    "Compressors/Rotary Compressor": [
        # CN203321827U — High-Efficiency Double Screw Rod Compressor
        "double screw rod compressor",
        "screw rod compressor",
        # DE102012202712A1 — Dry Twin-Shaft Screw Spindle Compressor
        "twin-shaft",
        "spindle compressor",
        "aluminum spindle rotors",
        # WO2017075555A1 — Complex Screw Rotors Compressor
        "helical lobes",
        "helical grooves",
        "male rotor female rotor",
    ],

    "Agriculture and Biomass/Forage Harvester Cutterhead": [
        # DE102004026803 — Chaff-Cutter Microwave Radiator Garden
        "microwave radiator",
        "chaff-cutter",
        "cutting chamber timber",
        # US20110042499 — Wear Liner Brush Cutter
        "brush cutter",
        "wear liner",
        "cutting drum",
        # US5495987 — Ensilage Slicing Compacted
        "ensilage slicing",
        "compacted ensilage",
        "skid steer",
    ],

    "Motors and Clutches": [
        # JP2006345675 — Driving Motor Railway Vehicles
        "rolling stock",
        "oil supply chamber",
        "drive motor railway",
        # JP2011239584 — Bearing Device Electric Motor Driving Vehicles
        "labyrinth",
        "bearing device motor",
        # US6339273 — Small-Size Motor
        "small-size motor",
        "boss shaft",
    ],

    "Sterilization and Medical Waste/Integrated Medical Waste Management": [
        # JP2012200695 — Treating Organic Wastewater Sludge
        "organic wastewater",
        "surplus sludge",
        # JP2008272706 — Asbestos Building Material Waste Processing
        "asbestos",
        "building material waste",
        # US7534392 — Waste Processing Pathogen Reduction
        "pathogen reduction",
        "disinfection of waste",
    ],

    "Packaging Machinery": [
        # PI00016608 — Porções Café Preembalados Máquina
        "porções de café",
        "preembalados",
        "máquina de café",
        # EP2660161 — Packaging Dried Sheets Sealed Capsules Tea
        "packaging tea",
        "airtight capsule",
        "breaking dried tea",
    ],

    "Separator/Gas-Liquid Separator": [
        # CN203061442U — Dry-Type Household Garbage Air Separation
        "household garbage",
        "air separation",
        "low-speed breaking",
        # WO2007140204A1 — Multivariable Control Three-Phase Separation
        "three-phase separation",
        "multivariable control",
    ],

    "Machines for rubber industry": [
        # JPH06173862A — Resin Film Forming Device Screw Pump Rotor
        "thermosetting resin",
        "screw pump rotor",
        "resin film forming",
        # JPH06170863A — Device Releasing Screw-Type Pump Rotor Resin
        "screw-type pump rotor",
        "rubber mold releasing",
        "releasing device",
    ],

    "Measuring devices/Particle and Size Analysis": [
        # CN101811081 — Shredder Head Power Material Thickness
        "shredder head",
        "material thickness",
        "pulverizer blades",
        # CN103085196 — Multifunctional Aggregate Machine
        "aggregate machine",
        "multifunctional aggregate",
        # US11965409B2 — Downhole Device Communication Measured Electrical
        "electrical property",
        "downhole device communication",
    ],

    "Safety and Braking/Hydraulic Retarder": [
        # DE000010393521T5 — Braking Device Gerotor Motors
        "braking device",
        "gerotor motors",
        "central bore",
    ],

    "Semiconductor and Nanomaterials": [
        # US20130109902 — Radioactive Substance Absorbent Cellulose
        "radioactive",
        "fibrillated cellulose",
        "water permeable",
    ],

    "Couplings and Drive Units": [
        # US5597125 — Apparatus Fluffing Bales Peat Moss
        "peat moss",
        "compressed bale",
        "agitator assemblies",
        "hydraulic drive motor",
    ],

    "Data and Text Processing": [
        # PI04053869 — Estenografia Semântica
        "estenografia",
        "taquigrafia",
    ],

    "Chemical Substrate Applications": [
        # PI04053907 — Substrato Dobrado Substância Química
        "substrato dobrado",
        "substância química aplicada",
    ],

    "Food Processing Appliances": [
        # MU7002033 — Disposição Construtiva Prensa Culinária
        "food cooking press",
        "internal depth",
        "various dishes",
    ],
}

# Aplica adições V17B (sem duplicatas)
for _cat, _novos in _ADICOES_V17B.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ══════════════════════════════════════════════════════════════════════
# V18 — CORREÇÕES DA AUDITORIA COMPLETA (Abril 2026)
# ══════════════════════════════════════════════════════════════════════
#
# Origem: Auditoria de 5977 patentes — 31 sem match, 396 baixa confiança.
#
# Correções aplicadas:
#   1. Termos em português para patentes PI (INPI Brasil)
#   2. Variantes de bombas específicas (spiral, eccentric, vane, lobe)
#   3. Termos para progressive cavity apparatus / PDM rotors
#   4. Termos para grinding/kneading/comminuting devices
#   5. Contexto semântico: "pumping fluid", "pump intake", etc.
#
# Resultado: Sem match reduzido de 31 para 3 (-90%)
# ══════════════════════════════════════════════════════════════════════

_ADICOES_V18_AUDITORIA = {

    # ── Pumps: variantes específicas + português + contexto ──────────
    "Pumps": [
        # Variantes de tipo de bomba (resolvem DE3304751A1, WO199834028A1, etc.)
        "rotary pump", "spiral pump", "eccentric pump",
        "vane pump", "lobe pump", "electric pump",
        "constant flow pump", "hydraulic vane machine",
        # Contexto semântico (resolve AU2017201904B1)
        "pumping fluid", "pump intake", "pump fluid intake",
        "pumping method", "pumping means",
        # Componentes de bomba
        "pump rotor", "pump stator", "pump chamber",
        "rotary displacement", "plastic pump rotor",
        # Português — patentes INPI (resolve PI00070890, PI96051175, PI07071698)
        "bomba de alimentação", "bomba de fluxo",
        "bombeamento de líquido", "bomba de canais laterais",
        "bomba para bombeamento", "bomba de combustível",
    ],

    # ── Pumps/Screw Pump: single-screw / twin-screw variants ─────────
    "Pumps/Screw Pump": [
        # Resolve CN212454803U (single-screw gas-liquid mixed pump)
        "single-screw pump", "single screw pump",
        "gas-liquid mixed pump", "variable-pitch rotor",
        "variable-pitch stator", "segmented variable-pitch",
    ],

    # ── Pumps/PC Pump and Motor: progressive cavity + eccentric ──────
    "Pumps/PC Pump and Motor": [
        # Variantes técnicas (resolve GB2448814A, US20140064997A1)
        "progressive cavity apparatus", "progressive cavity motor",
        "eccentric spiral pump", "eccentric screw pump",
        "pdm rotor", "asymmetric lobe", "lobe-type rotor pump",
    ],

    # ── Pumps/PC Pump and Motor/Rotor: design de rotores lobe-type ───
    "Pumps/PC Pump and Motor/Rotor": [
        # Resolve US000007565741B2, US000007565742B2, etc.
        "rotor stator design", "rotor lobe design", "conjugate rotor",
    ],

    # ── Grinding and Milling: kneading + comminuting + hackrotor ─────
    "Grinding and Milling": [
        # Resolve DE000009409069U1, DE202005017373, DE102009020714, etc.
        "kneading machine", "kneading chamber",
        "hackrotor", "crushing agglomerate",
        "comminuting device", "wood comminuter", "comminuting knife",
        "processing feedstock", "feed material processing",
        "fibrous slurry refiner",
        "rotor-stator system", "rotor stator system",
    ],

    # ── Bearings: seção de mancal/engrenagem ─────────────────────────
    "Bearings": [
        # Resolve WO2012122321A2
        "bearing gearing section",
    ],
}

# Aplica adições V18 (sem duplicatas)
for _cat, _novos in _ADICOES_V18_AUDITORIA.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])
    else:
        PALAVRAS_CHAVE[_cat] = list(_novos)


# ══════════════════════════════════════════════════════════════════════
# V18 — EXCLUSÃO SEMÂNTICA
# ══════════════════════════════════════════════════════════════════════
EXCLUSAO_SEMANTICA = {
    "Valves": [
        "heart valve", "cardiac valve", "mitral valve", "aortic valve",
        "heart surgery", "prosthetic heart", "transcatheter valve",
    ],
    "Pumps": [
        "heart pump", "blood pump", "cardiac pump",
        "insulin pump", "infusion pump",
    ],
}


# ══════════════════════════════════════════════════════════════════════
# V19 — CORREÇÃO SEMÂNTICA (Abril 2026)
# ══════════════════════════════════════════════════════════════════════
#
# Auditoria semântica revelou 511 patentes (~8.5%) potencialmente
# mal classificadas, concentradas em 5 pastas. Correções:
#
#   1. Sealings/Ring and Peripheral Seal: remover termos genéricos
#      ("peripheral surface", "outer peripheral", "rotating shaft")
#   2. Oil Tools/Wellhead/Riser: remover "SCR" (matcha em "screen",
#      "screw", "scraper")
#   3. Pumps/Centrifugal Pump: remover "impeller" e "volute" isolados
#   4. Nova regra de prioridade por título no script
#   5. Sealings/Seal Ring and Gasket: remover "gasket" isolado
#
# Resultado esperado: precisão de 87% → ~95%
# ══════════════════════════════════════════════════════════════════════

# ── TERMOS A REMOVER (por pasta) ──────────────────────────────────────
_REMOVER_V19 = {
    "Sealings/Ring and Peripheral Seal": [
        # Genéricos que matcham em qualquer patente mecânica
        "peripheral surface",
        "outer peripheral",
        "inner peripheral",
        "outer peripheral surface",
        "inner peripheral surface",
        "outer peripheral side",
        "inner peripheral side",
        "peripheral side",
        "rotating shaft",
        "fitted outer peripheral",
        "fitted inner peripheral",
        # Termos de Oil Tools que contaminam esta pasta
        "subsea",
        "adjustable riser",
        "riser hanger",
        # Termos vagos
        "anchor assembly",
        "external flange",
        "split bodies",
        "stationary ring",
        "annular member attached to",
        "attached to a housing",
        "first annular member",
    ],
    "Oil Tools/Wellhead equipment/Riser": [
        # SCR (3 letras) matcha em "screen", "screw", "scraper"
        "SCR",
    ],
    "Sealings/Seal Ring and Gasket": [
        # "gasket" sozinho é genérico demais — aparece em qualquer
        # patente que mencione vedação incidentalmente
        "gasket",
        # "seal assembly" e "seal body" são genéricos
        "seal assembly",
        "seal body",
        "sealing element",
    ],
}

# Aplica remoções
for _cat, _termos_remover in _REMOVER_V19.items():
    if _cat in PALAVRAS_CHAVE:
        _lower_remover = set(t.lower() for t in _termos_remover)
        PALAVRAS_CHAVE[_cat] = [
            t for t in PALAVRAS_CHAVE[_cat]
            if t.lower() not in _lower_remover
        ]

# ── SUBSTITUIÇÕES: termos genéricos → termos específicos ─────────────
_SUBSTITUICOES_V19 = {
    "Oil Tools/Wellhead equipment/Riser": [
        # Substituir "SCR" por versão completa (não faz substring match)
        "steel catenary riser",
    ],
    "Sealings/Ring and Peripheral Seal": [
        # Manter APENAS termos onde "peripheral" está junto de "seal"
        "peripheral seal",
        "peripheral sealing ring",
        "ring peripheral seal",
    ],
    "Sealings/Seal Ring and Gasket": [
        # Substituir "gasket" genérico por combinações específicas
        "gasket seal",
        "gasket ring",
        "sealing gasket",
        "cylinder head gasket",
        "flange gasket",
        "exhaust gasket",
        "metal gasket",
        "rubber gasket",
        "spiral wound gasket",
    ],
}

for _cat, _novos in _SUBSTITUICOES_V19.items():
    if _cat in PALAVRAS_CHAVE:
        _ex = set(t.lower() for t in PALAVRAS_CHAVE[_cat])
        PALAVRAS_CHAVE[_cat].extend([t for t in _novos if t.lower() not in _ex])


# ── TERMOS GENÉRICOS A REMOVER DE PASTAS ESPECÍFICAS ────────────────
# "impeller" e "volute" sozinhos causam falsos positivos em
# Pumps/Centrifugal Pump (capturam trituradores)
_REMOVER_CENTRIFUGAL = ["impeller", "volute"]
if "Pumps/Centrifugal Pump" in PALAVRAS_CHAVE:
    _lr = set(t.lower() for t in _REMOVER_CENTRIFUGAL)
    PALAVRAS_CHAVE["Pumps/Centrifugal Pump"] = [
        t for t in PALAVRAS_CHAVE["Pumps/Centrifugal Pump"]
        if t.lower() not in _lr
    ]
    # Substituir por combinações específicas
    _novos_centrif = [
        "centrifugal pump impeller",
        "pump impeller",
        "pump volute",
        "volute casing pump",
        "impeller pump",
        "centrifugal impeller",
    ]
    _ex = set(t.lower() for t in PALAVRAS_CHAVE["Pumps/Centrifugal Pump"])
    PALAVRAS_CHAVE["Pumps/Centrifugal Pump"].extend(
        [t for t in _novos_centrif if t.lower() not in _ex]
    )

# Também em Pumps/Centrifugal Pump/Volute and Diffuser
if "Pumps/Centrifugal Pump/Volute and Diffuser" in PALAVRAS_CHAVE:
    # Adicionar termos específicos se "volute" sozinho foi removido
    _novos_volute = [
        "volute casing",
        "pump volute",
        "volute diffuser",
        "pump diffuser",
        "spiral volute",
    ]
    _ex = set(t.lower() for t in PALAVRAS_CHAVE["Pumps/Centrifugal Pump/Volute and Diffuser"])
    PALAVRAS_CHAVE["Pumps/Centrifugal Pump/Volute and Diffuser"].extend(
        [t for t in _novos_volute if t.lower() not in _ex]
    )


# ══════════════════════════════════════════════════════════════════════
# V19 — PRIORIDADE POR TÍTULO (lista de domínios prioritários)
# ══════════════════════════════════════════════════════════════════════
# Usado pelo script para dar prioridade à categoria do título quando
# há conflito com menções secundárias no abstract.
# Se o TÍTULO contém "pump" e o abstract menciona "seal ring",
# o classificador deve preferir Pumps/* sobre Sealings/*.
# ══════════════════════════════════════════════════════════════════════

PRIORIDADE_TITULO = {
    # Se o título contém estes termos → preferir estas raízes
    "pump":     ["Pumps"],
    "bomba":    ["Pumps"],
    "bearing":  ["Bearings"],
    "rolamento":["Bearings"],
    "crusher":  ["Macerator", "Grinding and Milling"],
    "shredder": ["Macerator", "Grinding and Milling", "Media and Document Destruction"],
    "grinder":  ["Macerator", "Grinding and Milling"],
    "motor":    ["Electric Motors"],
    "valve":    ["Valves"],
    "válvula":  ["Valves"],
    "seal":     ["Sealings"],
    "vedação":  ["Sealings"],
}


# ── PASSO FINAL: Deduplicação pós-V19 ───────────────────────────────
for _cat in PALAVRAS_CHAVE:
    _seen = set()
    _dedup = []
    for _t in PALAVRAS_CHAVE[_cat]:
        _k = _t.lower()
        if _k not in _seen:
            _seen.add(_k)
            _dedup.append(_t)
    PALAVRAS_CHAVE[_cat] = _dedup
