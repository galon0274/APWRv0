class charger:
    instTypeA11 = 1800
    instTypeA22 = 2000
    instTypeB11 = 2200
    instTypeB22 = 2400

    def __init__(self):
        self.sid = 0
        self.vendorPartNum = ''
        self.name = ''
        self.type = ''
        self.group = ''
        self.picList = []
        self.description = ''
        self.mainFeatures = []
        self.electricalParams = []
        self.equipment = []
        self.envConditions = []
        self.connectivity = []
        self.instDetails = []
        self.safety = []
        self.cost = 0
        self.price2Cell = 0
        self.instPrice = 0


class FeatureItem:
    def __init__(self):
        self.fName = ''
        self.fDescription = ''