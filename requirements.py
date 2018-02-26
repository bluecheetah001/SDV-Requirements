from collections import namedtuple, defaultdict
from math import ceil
Rule = namedtuple('Rule', 'name, required, source, ship, consume, produce')
Stack = namedtuple('Stack', 'item, count')
nicenames = {
    '16':'WildHorseradish','18':'Daffodil','20':'Leek','22':'Dandelion','24':'Parsnip','30':'Lumber','60':'Emerald','62':'Aquamarine','64':'Ruby','66':'Amethyst','68':'Topaz','70':'Jade','72':'Diamond','74':'PrismaticShard','78':'CaveCarrot','80':'Quartz','82':'FireQuartz','84':'FrozenTear','86':'EarthCrystal','88':'Coconut','90':'CactusFruit','92':'Sap','93':'Torch','94':'SpiritTorch','96':'DwarfScrollI','97':'DwarfScrollII','98':'DwarfScrollIII','99':'DwarfScrollIV','100':'ChippedAmphora','101':'Arrowhead','102':'LostBook','103':'AncientDoll','104':'ElvishJewelry','105':'ChewingStick','106':'OrnamentalFan','107':'DinosaurEgg','108':'RareDisc','109':'AncientSword','110':'RustySpoon','111':'RustySpur','112':'RustyCog','113':'ChickenStatue','114':'AncientSeed','115':'PrehistoricTool','116':'DriedStarfish','117':'Anchor','118':'GlassShards','119':'BoneFlute','120':'PrehistoricHandaxe','121':'DwarvishHelm','122':'DwarfGadget','123':'AncientDrum','124':'GoldenMask','125':'GoldenRelic','126':'StrangeDoll','127':'StrangeDoll','128':'Pufferfish','129':'Anchovy','130':'Tuna','131':'Sardine','132':'Bream','136':'LargemouthBass','137':'SmallmouthBass','138':'RainbowTrout','139':'Salmon','140':'Walleye','141':'Perch','142':'Carp','143':'Catfish','144':'Pike','145':'Sunfish','146':'RedMullet','147':'Herring','148':'Eel','149':'Octopus','150':'RedSnapper','151':'Squid','152':'Seaweed','153':'GreenAlgae','154':'SeaCucumber','155':'SuperCucumber','156':'Ghostfish','157':'WhiteAlgae','158':'Stonefish','159':'Crimsonfish','160':'Angler','161':'IcePip','162':'LavaEel','163':'Legend','164':'Sandfish','165':'ScorpionCarp','166':'TreasureChest','167':'JojaCola','168':'Trash','169':'Driftwood','170':'BrokenGlasses','171':'BrokenCD','172':'SoggyNewspaper','174':'LargeWhiteEgg','176':'WhiteEgg','178':'Hay','180':'BrownEgg','182':'LargeBrownEgg','184':'Milk','186':'LargeMilk','188':'GreenBean','190':'Cauliflower','192':'Potato','194':'FriedEgg','195':'Omelet','196':'Salad','197':'CheeseCauliflower','198':'BakedFish','199':'ParsnipSoup','200':'VegetableMedley','201':'CompleteBreakfast','202':'FriedCalamari','203':'StrangeBun','204':'LuckyLunch','205':'FriedMushroom','206':'Pizza','207':'BeanHotpot','208':'GlazedYams','209':'CarpSurprise','210':'Hashbrowns','211':'Pancakes','212':'SalmonDinner','213':'FishTaco','214':'CrispyBass','215':'PepperPoppers','216':'Bread','218':'TomKhaSoup','219':'TroutSoup','220':'ChocolateCake','221':'PinkCake','222':'RhubarbPie','223':'Cookie','224':'Spaghetti','225':'FriedEel','226':'SpicyEel','227':'Sashimi','228':'MakiRoll','229':'Tortilla','230':'RedPlate','231':'EggplantParmesan','232':'RicePudding','233':'IceCream','234':'BlueberryTart','235':'Autumn\'sBounty','236':'PumpkinSoup','237':'SuperMeal','238':'CranberrySauce','239':'Stuffing','240':'Farmer\'sLunch','241':'SurvivalBurger','242':'DishO\'TheSea','243':'Miner\'sTreat','244':'RootsPlatter','245':'Sugar','246':'WheatFlour','247':'Oil','248':'Garlic','250':'Kale','252':'Rhubarb','254':'Melon','256':'Tomato','257':'Morel','258':'Blueberry','259':'FiddleheadFern','260':'HotPepper','262':'Wheat','264':'Radish','266':'RedCabbage','268':'Starfruit','270':'Corn','272':'Eggplant','274':'Artichoke','276':'Pumpkin','278':'BokChoy','280':'Yam','281':'Chanterelle','282':'Cranberries','283':'Holly','284':'Beet','286':'CherryBomb','287':'Bomb','288':'MegaBomb','296':'Salmonberry','297':'GrassStarter','298':'HardwoodFence','299':'AmaranthSeeds','300':'Amaranth','301':'GrapeStarter','302':'HopsStarter','303':'PaleAle','304':'Hops','305':'VoidEgg','306':'Mayonnaise','307':'DuckMayonnaise','308':'VoidMayonnaise','309':'Acorn','310':'MapleSeed','311':'PineCone','322':'WoodFence','323':'StoneFence','324':'IronFence','325':'Gate','326':'DwarvishTranslationGuide','328':'WoodFloor','329':'StoneFloor','330':'Clay','331':'WeatheredFloor','333':'CrystalFloor','334':'CopperBar','335':'IronBar','336':'GoldBar','337':'IridiumBar','338':'RefinedQuartz','340':'Honey','341':'TeaSet','342':'Pickles','344':'Jelly','346':'Beer','347':'RareSeed','348':'Wine','349':'EnergyTonic','350':'Juice','351':'MuscleRemedy','368':'BasicFertilizer','369':'QualityFertilizer','370':'BasicRetainingSoil','371':'QualityRetainingSoil','372':'Clam','373':'GoldenPumpkin','376':'Poppy','378':'CopperOre','380':'IronOre','382':'Coal','384':'GoldOre','386':'IridiumOre','388':'Wood','390':'Stone','392':'NautilusShell','393':'Coral','394':'RainbowShell','395':'Coffee','396':'SpiceBerry','397':'SeaUrchin','398':'Grape','399':'SpringOnion','400':'Strawberry','401':'StrawFloor','402':'SweetPea','403':'FieldSnack','404':'CommonMushroom','405':'WoodPath','406':'WildPlum','407':'GravelPath','408':'Hazelnut','409':'CrystalPath','410':'Blackberry','411':'CobblestonePath','412':'WinterRoot','413':'BlueSlimeEgg','414':'CrystalFruit','415':'SteppingStonePath','416':'SnowYam','417':'SweetGemBerry','418':'Crocus','419':'Vinegar','420':'RedMushroom','421':'Sunflower','422':'PurpleMushroom','423':'Rice','424':'Cheese','425':'FairySeeds','426':'GoatCheese','427':'TulipBulb','428':'Cloth','429':'JazzSeeds','430':'Truffle','431':'SunflowerSeeds','432':'TruffleOil','433':'CoffeeBean','434':'Stardrop','436':'GoatMilk','437':'RedSlimeEgg','438':'L.GoatMilk','439':'PurpleSlimeEgg','440':'Wool','441':'ExplosiveAmmo','442':'DuckEgg','444':'DuckFeather','446':'Rabbit\'sFoot','449':'StoneBase','453':'PoppySeeds','454':'AncientFruit','455':'SpangleSeeds','456':'AlgaeSoup','457':'PaleBroth','458':'Bouquet','459':'Mead','460':'Mermaid\'sPendant','461':'DecorativePot','463':'DrumBlock','464':'FluteBlock','465':'Speed-Gro','466':'DeluxeSpeed-Gro','472':'ParsnipSeeds','473':'BeanStarter','474':'CauliflowerSeeds','475':'PotatoSeeds','476':'GarlicSeeds','477':'KaleSeeds','478':'RhubarbSeeds','479':'MelonSeeds','480':'TomatoSeeds','481':'BlueberrySeeds','482':'PepperSeeds','483':'WheatSeeds','484':'RadishSeeds','485':'RedCabbageSeeds','486':'StarfruitSeeds','487':'CornSeeds','488':'EggplantSeeds','489':'ArtichokeSeeds','490':'PumpkinSeeds','491':'BokChoySeeds','492':'YamSeeds','493':'CranberrySeeds','494':'BeetSeeds','495':'SpringSeeds','496':'SummerSeeds','497':'FallSeeds','498':'WinterSeeds','499':'AncientSeeds','516':'SmallGlowRing','517':'GlowRing','518':'SmallMagnetRing','519':'MagnetRing','520':'SlimeCharmerRing','521':'WarriorRing','522':'VampireRing','523':'SavageRing','524':'RingofYoba','525':'SturdyRing','526':'Burglar\'sRing','527':'IridiumBand','528':'JukeboxRing','529':'AmethystRing','530':'TopazRing','531':'AquamarineRing','532':'JadeRing','533':'EmeraldRing','534':'RubyRing','535':'Geode','536':'FrozenGeode','537':'MagmaGeode','538':'Alamite','539':'Bixite','540':'Baryte','541':'Aerinite','542':'Calcite','543':'Dolomite','544':'Esperite','545':'Fluorapatite','546':'Geminite','547':'Helvite','548':'Jamborite','549':'Jagoite','550':'Kyanite','551':'Lunarite','552':'Malachite','553':'Neptunite','554':'LemonStone','555':'Nekoite','556':'Orpiment','557':'PetrifiedSlime','558':'ThunderEgg','559':'Pyrite','560':'OceanStone','561':'GhostCrystal','562':'Tigerseye','563':'Jasper','564':'Opal','565':'FireOpal','566':'Celestine','567':'Marble','568':'Sandstone','569':'Granite','570':'Basalt','571':'Limestone','572':'Soapstone','573':'Hematite','574':'Mudstone','575':'Obsidian','576':'Slate','577':'FairyStone','578':'StarShards','579':'PrehistoricScapula','580':'PrehistoricTibia','581':'PrehistoricSkull','582':'SkeletalHand','583':'PrehistoricRib','584':'PrehistoricVertebra','585':'SkeletalTail','586':'NautilusFossil','587':'AmphibianFossil','588':'PalmFossil','589':'Trilobite','590':'ArtifactSpot','591':'Tulip','593':'SummerSpangle','595':'FairyRose','597':'BlueJazz','599':'Sprinkler','604':'PlumPudding','605':'ArtichokeDip','606':'StirFry','607':'RoastedHazelnuts','608':'PumpkinPie','609':'RadishSalad','610':'FruitSalad','611':'BlackberryCobbler','612':'CranberryCandy','613':'Apple','618':'Bruschetta','621':'QualitySprinkler','628':'CherrySapling','629':'ApricotSapling','630':'OrangeSapling','631':'PeachSapling','632':'PomegranateSapling','633':'AppleSapling','634':'Apricot','635':'Orange','636':'Peach','637':'Pomegranate','638':'Cherry','645':'IridiumSprinkler','648':'Coleslaw','649':'FiddleheadRisotto','651':'PoppyseedMuffin','680':'GreenSlimeEgg','681':'RainTotem','682':'MutantCarp','684':'BugMeat','685':'Bait','686':'Spinner','687':'DressedSpinner','688':'WarpTotem:Farm','689':'WarpTotem:Mountains','690':'WarpTotem:Beach','691':'BarbedHook','692':'LeadBobber','693':'TreasureHunter','694':'TrapBobber','695':'CorkBobber','698':'Sturgeon','699':'TigerTrout','700':'Bullhead','701':'Tilapia','702':'Chub','703':'Magnet','704':'Dorado','705':'Albacore','706':'Shad','707':'Lingcod','708':'Halibut','709':'Hardwood','710':'CrabPot','715':'Lobster','716':'Crayfish','717':'Crab','718':'Cockle','719':'Mussel','720':'Shrimp','721':'Snail','722':'Periwinkle','723':'Oyster','724':'MapleSyrup','725':'OakResin','726':'PineTar','727':'Chowder','728':'FishStew','729':'Escargot','730':'LobsterBisque','731':'MapleBar','732':'CrabCakes','734':'Woodskip','745':'StrawberrySeeds','746':'Jack-O-Lantern','747':'RottenPlant','748':'RottenPlant','749':'OmniGeode','766':'Slime','767':'BatWing','768':'SolarEssence','769':'VoidEssence','770':'MixedSeeds','771':'Fiber','772':'OilofGarlic','773':'LifeElixir','774':'WildBait','775':'Glacierfish','787':'BatteryPack','788':'LostAxe','789':'LuckyPurpleShorts','790':'BerryBasket','795':'VoidSalmon','796':'Slimejack',       
    'big8':'Scarecrow','big9':'LightningRod','big10':'BeeHouse','big12':'Keg','big13':'Furnace','big15':'PreservesJar','big17':'Loom','big16':'CheesePress','big19':'OilMaker','big20':'RecyclingMachine','big21':'Crystalarium','big24':'MayonnaiseMachine','big25':'SeedMaker','big71':'Staircase','big83':'WickedStatue','big105':'Tapper','big108':'Tubo\'Flowers','big114':'CharcoalKiln','big130':'Chest','big143':'WoodenBrazier','big144':'StoneBrazier','big145':'GoldBrazier','big146':'Campfire','big147':'StumpBrazier','big148':'CarvedBrazier','big149':'SkullBrazier','big150':'BarrelBrazier','big151':'MarbleBrazier','big152':'WoodLamp-post','big153':'IronLamp-post','big154':'WormBin','big156':'SlimeIncubator','big158':'SlimeEgg-Press','big163':'Cask',                                    
}
class ItemState:
    def __init__(self, id):
        if id in nicenames:
            self.name = nicenames[id]
            if id.startswith('big'):
                self.big = True
                self.id = int(id[3:])
            else:
                self.big = False
                self.id = int(id)
        else:
            self.name = None
            self.big = False
            self.id = id
        self._sources = []
        self.input = 0
        self.shipped = 0
        self.consumed = 0 
        self.extra = 0 # may be negative to indicate that more needs to be acquired
    @property
    def source(self):
        if len(self._sources) == 0:
            return None
        if len(self._sources) == 1:
            return self._sources[0]
        raise ValueError('Item '+self.name+' has multiple sources: '+str(self._sources))
    @source.setter
    def source(self, source):
        self._sources.append(source)
    def ship(self, count):
        self.extra -= max(0, count - self.shipped)
        self.shipped = max(count, self.shipped)
    def consume(self, count):
        self.extra -= count
        self.consumed += count
    def external(self, count):
        self.input += count
        self.extra += count
    def produce(self, count):
        self.extra += count
    def isobject(self):
        return self.name is not None and not self.big
    def isbig(self):
        return self.big
    def isother(self):
        return self.name is None
    def __str__(self):
        return "(input={}, ship={}, consume={}, extra={})".format(self.input, self.shipped, self.consumed, self.extra)
    def __repr__(self):
        return "(input={}, ship={}, consume={}, extra={})".format(self.input, self.shipped, self.consumed, self.extra)
class ItemStateDict(dict):
    def __missing__(self, id):
        item = ItemState(id)
        self[id] = item
        return item
def rule(str):
    split = str.split(':',1)
    name = split[0].strip()
    split = split[1].split(',')
    args = {
        'name':name,
        'required':False,
        'source':True,
        'ship':{},
        'consume':{},
        'produce':{}
    }
    for arg in split:
        argsplit = arg.strip().split(' ')
        argname = argsplit[0]
        if argname == 'required':
            args[argname] = True
        if argname == 'no_source':
            args['source'] = False
        if argname in ('ship', 'consume', 'produce'):
            args[argname] = stacks(argsplit[1:])
    return Rule(**args)
def stacks(split):
    stacks = map(stack, split)
    return {s.item: s.count for s in stacks}
def stack(str):
    split = str.split('*')
    item = split[0]
    count = int(split[1]) if len(split)>1 else 1
    return Stack(item, count)
def rules(str):
    list = []
    for str in str.split('\n'):
        str = str.split('#',1)[0].strip()
        if len(str) == 0:
            continue
        list.append(rule(str))
    return list
def count(rules):
    items = ItemStateDict()
    taken = defaultdict(int)        # number of times each rule is taken
    
    def take(rule, c):
        taken[rule.name] += c
        for id, count in rule.ship.items():
            items[id].ship(count*c)
        for id, count in rule.consume.items():
            items[id].consume(count*c)
        for id, count in rule.produce.items():
            items[id].produce(count*c)
        
    
    for r in rules:
        if r.source:
            for id in r.produce.keys():
                items[id].source = r
        if r.required:
            take(r,1)
    
    didSomething = True
    while didSomething:
        didSomething = False
        for id, item in list(items.items()): # copy to be able to safely add items
            if item.extra < 0:
                didSomething = True
                rule = item.source
                if rule is None:
                    item.external(-item.extra)
                else:
                    count = int(ceil(-item.extra/rule.produce[id]))
                    take(rule, count)
                
                

    print('Objects:')
    printitems([item for item in items.values() if item.isobject()])
    print()
    print('Big Craftables:')
    printitems([item for item in items.values() if item.isbig()])
    print()
    print('Other:')
    printother([item for item in items.values() if item.isother()])
    print()
    printmap('rules taken:', taken)
def printitems(items):
    items.sort(key=lambda item:item.id)
    header = '  id |         name         | input | ship | consume | extra | '
    sep =    '-----+----------------------+-------+------+---------+-------+-'
    row = ' {:>3} | {:<20} | {:>5} | {:>4} | {:>7} | {:>5} | '
    rows = [row.format(item.id, item.name, item.input, item.shipped, item.consumed, item.extra) for item in items]
    print(header, sep, *rows, sep='\n')
def printother(items):
    items.sort(key=lambda item:item.id)
    header = '    name    |  input | ship | consume | extra | '
    sep =    '------------+--------+------+---------+-------+-'
    row = ' {:<10} | {:>6} | {:>4} | {:>7} | {:>5} | '
    rows = [row.format(item.id, item.input, item.shipped, item.consumed, item.extra) for item in items]
    print(header, sep, *rows, sep='\n')
def printmap(header, map):
    print(header)
    items = list(map.items())
    items.sort()
    for item, count in items:
        if count != 0:
            print('    {}: {}'.format(item, count))

count(rules('''
# achievements
ship_all: required, ship 16 18 20 22 24 78 88 90 92 174 176 180 182 184 186 188 190 192 248 250 252 254 256 257 258 259 260 262 264 266 268 270 272 274 276 278 280 281 282 283 284 296 300 303 304 305 306 307 308 330 334 335 336 337 338 340 342 344 346 348 350 372 376 378 380 382 384 386 388 390 392 393 394 396 397 398 399 400 402 404 406 408 410 412 414 416 417 418 420 421 422 424 426 428 430 432 433 436 438 440 442 444 446 454 459 591 593 595 597 613 634 635 636 637 638 684 709 724 725 726 766 767 768 769 771 787
ship_many: required, ship 24*15 188*15 190*15 192*15 248*15 250*15 252*15 254*15 256*15 258*15 260*15 262*15 264*15 266*15 268*15 270*15 272*15 274*15 276*15 278*15 280*15 282*15 284*15 300*15 304*15 398*15 400*15 433*15 

# not producing 499, as we still have to craft one anyway
museum: required, consume 60 62 64 66 68 70 72 74 80 82 84 86 96 97 98 99 100 101 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589

# bundles
# TODO add other bundles
bundle_bb_chef: required, no_source, consume 724 259 430 376 228 194, produce 221*3
bundle_bb_dye: required, no_source, consume 420 397 421 444 62 266, produce big25
bundle_bb_field: required, no_source, consume 422 392 702 84, produce big20
bundle_bb_fodder: required, no_source, consume 262*10 178*10 613*3, produce Heater # TODO better item id
bundle_bb_enchanter: required, no_source, consume 725 348 446 637, produce 336*5

# buildings
build_barn1: required, consume gold*6000 388*350 390*150
# build_barn2: required, consume gold*12000 388*450 390*200
# build_barn3: required, consume gold*2500 388*550 390*300
build_coop1: required, consume gold*4000 388*300 390*100
# build_coop2: required, consume gold*10000 388*400 390*150
# build_coop3: required, consume gold*20000 388*500 390*200
# build_mill: required, consume gold*2500 388*150 390*50 428*4
# build_shed: required, consume gold*15000 388*300
# build_silo: required, consume gold*100 390*100 330*10 334*5
# build_slime: required, consume gold*10000 390*500 337 388*10
# build_stable: required, consume gold*10000 709*100 335*5
# build_well: required, consume gold*1000 390*75
build_house2: required, consume gold*10000 388*450
build_house3: required, consume gold*50000 709*150
build_house4: required, consume gold*100000

# recipes
robin_recepies: required, consume gold*17250
dwarf_recepies: required, consume gold*500
krobus_recepies: required, consume gold*500
festival_recepies: required, consume gold*4000


# cooking
cook_194: required, produce 194, consume any_egg*1
cook_195: required, produce 195, consume any_egg*1 any_milk*1
cook_196: required, produce 196, consume 20*1 22*1 419*1
cook_197: required, produce 197, consume 190*1 424*1
cook_198: required, produce 198, consume 145*1 132*1 246*1
cook_199: required, produce 199, consume 24*1 any_milk*1 419*1
cook_200: required, produce 200, consume 256*1 284*1
cook_201: required, produce 201, consume 194*1 any_milk*1 210*1 211*1
cook_202: required, produce 202, consume 151*1 246*1 247*1
cook_203: required, produce 203, consume 246*1 722*1 308*1
cook_204: required, produce 204, consume 154*1 229*1 597*1
cook_205: required, produce 205, consume 404*1 257*1 247*1
cook_206: required, produce 206, consume 246*1 256*1 424*1
cook_207: required, produce 207, consume 188*2
cook_208: required, produce 208, consume 280*1 245*1
cook_209: required, produce 209, consume 142*4
cook_210: required, produce 210, consume 192*1 247*1
cook_211: required, produce 211, consume 246*1 any_egg*1
cook_212: required, produce 212, consume 139*1 300*1 250*1
cook_213: required, produce 213, consume 130*1 229*1 266*1 306*1
cook_214: required, produce 214, consume 136*1 246*1 247*1
cook_215: required, produce 215, consume 260*1 424*1
cook_216: required, produce 216, consume 246*1
cook_218: required, produce 218, consume 88*1 720*1 404*1
cook_219: required, produce 219, consume 138*1 153*1
cook_220: required, produce 220, consume 246*1 245*1 any_egg*1
cook_221: required, produce 221, consume 254*1 246*1 245*1 any_egg*1
cook_222: required, produce 222, consume 252*1 246*1 245*1
cook_223: required, produce 223, consume 246*1 245*1 any_egg*1
cook_224: required, produce 224, consume 246*1 256*1
cook_225: required, produce 225, consume 148*1 247*1
cook_226: required, produce 226, consume 148*1 260*1
cook_227: required, produce 227, consume any_fish*1
cook_228: required, produce 228, consume any_fish*1 152*1 423*1
cook_229: required, produce 229, consume 270*1
cook_230: required, produce 230, consume 266*1 264*1
cook_231: required, produce 231, consume 272*1 256*1
cook_232: required, produce 232, consume any_milk*1 245*1 423*1
cook_233: required, produce 233, consume any_milk*1 245*1
cook_234: required, produce 234, consume 258*1 246*1 245*1 any_egg*1
cook_235: required, produce 235, consume 280*1 276*1
cook_236: required, produce 236, consume 276*1 any_milk*1
cook_237: required, produce 237, consume 278*1 282*1 274*1
cook_238: required, produce 238, consume 282*1 245*1
cook_239: required, produce 239, consume 216*1 282*1 408*1
cook_240: required, produce 240, consume 195*1 24*1
cook_241: required, produce 241, consume 216*1 78*1 272*1
cook_242: required, produce 242, consume 131*2 210*1
cook_243: required, produce 243, consume 78*2 245*1 any_milk*1
cook_244: required, produce 244, consume 78*1 412*1
cook_456: required, produce 456, consume 153*4
cook_457: required, produce 457, consume 157*2
cook_604: required, produce 604, consume 406*2 246*1 245*1
cook_605: required, produce 605, consume 274*1 184*1
cook_606: required, produce 606, consume 78*1 404*1 250*1 247*1
cook_607: required, produce 607, consume 408*3
cook_608: required, produce 608, consume 276*1 246*1 184*1 245*1
cook_609: required, produce 609, consume 247*1 419*1 264*1
cook_610: required, produce 610, consume 258*1 254*1 634*1
cook_611: required, produce 611, consume 410*2 245*1 246*1
cook_612: required, produce 612, consume 282*1 613*1 245*1
cook_618: required, produce 618, consume 216*1 247*1 256*1
cook_648: required, produce 648, consume 266*1 419*1 306*1
cook_649: required, produce 649, consume 247*1 259*1 248*1
cook_651: required, produce 651, consume 376*1 246*1 245*1
cook_727: required, produce 727, consume 372*1 184*1
cook_730: required, produce 730, consume 715*1 184*1
cook_729: required, produce 729, consume 721*1 248*1
cook_728: required, produce 728, consume 716*1 719*1 722*1 256*1
cook_731: required, produce 731, consume 724*1 245*1 246*1
cook_732: required, produce 732, consume 717*1 246*1 any_egg*1 247*1

# crafting
craft_322: required, produce 322, consume 388*2
craft_323: required, produce 323, consume 390*2
craft_324: required, produce 324*10, consume 335*1
craft_298: required, produce 298, consume 709*1
craft_325: required, produce 325, consume 388*10
craft_big130: required, produce big130, consume 388*50
craft_93: required, produce 93, consume 388*1 92*2
craft_big8: required, produce big8, consume 388*50 382*1 771*20
craft_big10: required, produce big10, consume 388*40 382*8 335*1 724*1
craft_big12: required, produce big12, consume 388*30 334*1 335*1 725*1
craft_big163: required, produce big163, consume 388*20 709*1
craft_big13: required, produce big13, consume 378*20 390*25
craft_big16: required, produce big16, consume 388*45 390*45 709*10 334*1
craft_big24: required, produce big24, consume 388*15 390*15 86*1 334*1
craft_big25: required, produce big25, consume 388*25 382*10 336*1
craft_big17: required, produce big17, consume 388*60 771*30 726*1
craft_big19: required, produce big19, consume 766*50 709*20 336*1
craft_big20: required, produce big20, consume 388*25 390*25 335*1
craft_big154: required, produce big154, consume 709*25 336*1 335*1 771*50
craft_big15: required, produce big15, consume 388*50 390*40 382*8
craft_big114: required, produce big114, consume 388*20 336*1
craft_big105: required, produce big105, consume 388*40 334*2
craft_big9: required, produce big9, consume 335*1 338*1 767*5
craft_big156: required, produce big156, consume 337*2 766*100
craft_big158: required, produce big158, consume 382*25 82*1 787*1
craft_big21: required, produce big21, consume 390*99 336*5 337*2 787*1
craft_599: required, produce 599, consume 334*1 335*1
craft_621: required, produce 621, consume 335*1 336*1 338*1
craft_645: required, produce 645, consume 336*1 337*1 787*1
craft_big71: required, produce big71, consume 390*99
craft_464: required, produce 464, consume 388*10 378*2 771*20
craft_463: required, produce 463, consume 390*10 378*2 771*20
craft_368: required, produce 368, consume 92*2
craft_369: required, produce 369, consume 92*2 any_fish*1
craft_370: required, produce 370, consume 390*2
craft_371: required, produce 371*2, consume 390*3 330*1
craft_465: required, produce 465*5, consume 726*1 372*1
craft_466: required, produce 466*5, consume 725*1 393*1
craft_286: required, produce 286, consume 378*4 382*1
craft_287: required, produce 287, consume 380*4 382*1
craft_288: required, produce 288, consume 384*4 768*1 769*1
craft_441: required, produce 441*5, consume 335*1 382*2
craft_335: required, no_source, produce 335, consume 334*3
craft_336: required, no_source, produce 336, consume 335*2
craft_499: required, produce 499, consume 114*1
craft_495: required, produce 495*10, consume 16*1 18*1 20*1 22*1
craft_496: required, produce 496*10, consume 396*1 398*1 402*1
craft_497: required, produce 497*10, consume 404*1 406*1 408*1 410*1
craft_498: required, produce 498*10, consume 412*1 414*1 416*1 418*1
craft_688: required, produce 688, consume 709*1 340*1 771*20
craft_689: required, produce 689, consume 709*1 335*1 390*25
craft_690: required, produce 690, consume 709*1 393*2 771*10
craft_681: required, produce 681, consume 709*1 432*1 726*5
craft_403: required, produce 403, consume 309*1 310*1 311*1
craft_746: required, produce 746, consume 276*1 93*1
craft_328: required, produce 328, consume 388*1
craft_401: required, produce 401, consume 388*1 771*1
craft_331: required, produce 331, consume 388*1
craft_333: required, produce 333*5, consume 338*1
craft_329: required, produce 329, consume 390*1
craft_405: required, produce 405, consume 388*1
craft_407: required, produce 407, consume 390*1
craft_411: required, produce 411, consume 390*1
craft_415: required, produce 415, consume 390*1
craft_409: required, produce 409*5, consume 338*1
craft_774: required, produce 774*5, consume 771*10 684*5 766*5
craft_685: required, produce 685*5, consume 684*1
craft_686: required, produce 686, consume 335*2
craft_703: required, produce 703*3, consume 335*1
craft_694: required, produce 694, consume 334*1 92*10
craft_695: required, produce 695, consume 388*10 709*5 766*10
craft_687: required, produce 687, consume 335*2 428*1
craft_693: required, produce 693, consume 336*2
craft_691: required, produce 691, consume 334*1 335*1 336*1
craft_772: required, produce 772*1, consume 248*10 247*1
craft_773: required, produce 773*1, consume 420*1 422*1 257*1 281*1
craft_710: required, produce 710, consume 388*40 335*3
craft_527: required, produce 527, consume 337*5 768*50 769*50
craft_524: required, produce 524, consume 336*5 335*5 72*1
craft_525: required, produce 525, consume 334*10 338*5 86*10
craft_521: required, produce 521, consume 335*10 382*25 84*10
craft_big108: required, produce big108, consume 388*15 427*1 429*1 453*1 455*1
craft_big143: required, produce big143, consume 388*10 382*1 771*5
craft_big83: required, produce big83, consume 382*5 390*25
craft_big144: required, produce big144, consume 390*10 382*1 771*5
craft_big145: required, produce big145, consume 336*1 382*1 771*5
craft_big146: required, produce big146, consume 390*10 388*10 771*10
craft_big147: required, produce big147, consume 709*5 382*1
craft_big148: required, produce big148, consume 709*10 382*1
craft_big149: required, produce big149, consume 709*10 768*1 382*1
craft_big150: required, produce big150, consume 388*50 768*1 382*1
craft_big151: required, produce big151, consume 567*1 62*1 390*100
craft_big152: required, produce big152, consume 388*50 787*1
craft_big153: required, produce big153, consume 335*1 787*1

# farming
farm_24: produce 24 farmxp*8
farm_188: produce 188 farmxp*9
farm_190: produce 190 farmxp*23
farm_192: produce 192 farmxp*14 #actually id*1.2
farm_248: produce 248 farmxp*12
farm_250: produce 250 farmxp*0
farm_252: produce 252 farmxp*26
farm_254: produce 254 farmxp*27
farm_256: produce 256 farmxp*12 #actually id*1.05
farm_258: produce 258*3 farmxp*10 #actually id*3.02
farm_260: produce 260 farmxp*9
farm_262: produce 262 farmxp*0
farm_264: produce 264 farmxp*15
farm_266: produce 266 farmxp*28
farm_268: produce 268 farmxp*43
farm_270: produce 270 farmxp*10
farm_272: produce 272 farmxp*12
farm_274: produce 274 farmxp*22
farm_276: produce 276 farmxp*31
farm_278: produce 278 farmxp*14
farm_280: produce 280 farmxp*22
farm_282: produce 282*2 farmxp*14 #actually id*2.1
farm_284: produce 284 farmxp*16
farm_300: produce 300 farmxp*0
farm_304: produce 304 farmxp*6
farm_376: produce 376 farmxp*20
farm_398: produce 398 farmxp*14
farm_400: produce 400 farmxp*18 #actually id*1.02
farm_417: produce 417 farmxp*64
farm_421: produce 421 431*2 farmxp*14
# farm_433: produce 433*4 farmxp*4 #are seeds so no need to plant
farm_454: produce 454 farmxp*38
farm_591: produce 591 farmxp*7
farm_593: produce 593 farmxp*15
farm_595: produce 595 farmxp*29
farm_597: produce 597 farmxp*10

# tools, comment out any that are not useful
mayo_306: consume any_egg, produce 306
# mayo_307: consume 422, produce 307
# mayo_308: consume 305, produce 308
jar_342: consume any_vege, produce 342
jar_344: consume any_fruit, produce 344
cheese_424: consume any_milk, produce 424
# cheese_426: consume goat_milk, produce 426
# loom_428: consume 440, produce 428
keg_346: consume 262, produce 346
keg_303: consume 304, produce 303
keg_348: consume any_fruit, produce 348
keg_350: consume any_vege, produce 350
keg_459: consume 340, produce 459
keg_395: consume 433*5, produce 395
# oil_247: consume 431, produce 247 # sunflower seeds chosen since they are an already available by-product
# oil_432: consume 430, produce 432
# kiln_382: consume 388, produce 382
furnace_334: consume 378*5 382, produce 334
furnace_335: consume 380*5 382, produce 335
furnace_336: consume 384*5 382, produce 336
furnace_337: consume 386*5 382, produce 337
furnace_338: consume 80 382, produce 338
'''))
