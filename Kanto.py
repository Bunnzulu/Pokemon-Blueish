import pygame,random
from pytmx.util_pygame import load_pygame
from Pokemon import Pokemon
pygame.init()

WildPokemonLocations = {"Route 1": ["Pidgey","Rattata"],"Route 2": ["Pidgey","Pidgey","Rattata","Rattata","Rattata","Caterpie"],"Route 22":["Rattata","Rattata","Rattata","Rattata","Rattata","Spearow","Spearow","NidoranF","NidoranF","NidoranF","NidoranM"],"ViridainForest":["Pikachu","Kakuna","Weedle","Metapod","Metapod","Caterpie","Caterpie","Caterpie"],"Route 3": ["Pidgey","Pidgey","Pidgey","Spearow","Spearow","Spearow","Jigglypuff"],"Mt.Moon(1)":["Zubat","Zubat","Zubat","Zubat","Zubat","Zubat","Zubat","Zubat","Geodude","Geodude","Geodude","Paras","Paras","Clefairy"],"Mt.Moon(2)":["Zubat","Zubat","Zubat","Zubat","Zubat","Zubat","Geodude","Geodude","Geodude","Paras","Paras","Clefairy"],"Mt.Moon(3)":["Zubat","Zubat","Zubat","Zubat","Zubat","Geodude","Geodude","Geodude","Paras","Paras","Clefairy"],"Route 4":["Rattata","Rattata","Rattata","Rattata","Spearow","Spearow","Spearow","Sandshrew","Sandshrew"],
                        "Route 24":["Bellsprout","Bellsprout","Bellsprout","Pidgey","Pidgey","Metapod","Abra"],"Route 25":["Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Pidgey","Pidgey","Pidgey","Metapod","Metapod","Metapod","Metapod","Caterpie","Caterpie","Caterpie","Caterpie","Abra","Abra","Abra","Kakuna","Kakuna","Weedle"],"Route 5":["Pidgey","Pidgey","Pidgey","Pidgey","Bellsprout","Bellsprout","Bellsprout","Meowth","Meowth"],"Route 6":["Pidgey","Pidgey","Pidgey","Pidgey","Bellsprout","Bellsprout","Bellsprout","Meowth","Meowth"],"Diglett Cave":["Diglett","Diglett","Diglett","Diglett","Diglett","Diglett","Diglett","Diglett","Diglett","Dugtrio"],"Route 11":["Sandshrew","Sandshrew","Sandshrew","Sandshrew","Spearow","Spearow","Spearow","Drowzee"],"Route 9":["Rattata","Rattata","Rattata","Rattata","Spearow","Spearow","Spearow","Sandshrew","Sandshrew"],"Route 10":["Voltorb","Voltorb","Voltorb","Voltorb","Spearow","Spearow","Spearow","Sandshrew","Sandshrew"],
                        "Rock TunnelF1":["Zubat","Zubat","Zubat","Zubat","Zubat","Geodude","Geodude","Geodude","Machop","Machop","Machop","Onix"],"Rock TunnelF2":["Zubat","Zubat","Zubat","Zubat","Zubat","Geodude","Geodude","Geodude","Machop","Machop","Machop","Onix"],"Route 8":["Pidgey","Pidgey","Pidgey","Meowth","Meowth","Vulpix","Sandshrew"],"Route 7":["Pidgey","Pidgey","Pidgey","Meowth","Meowth","Meowth","Bellsprout","Bellsprout","Bellsprout","Vulpix"],"PokemonTowerF3":["Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Haunter","Cubone"],"PokemonTowerF4":["Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Haunter","Cubone"],"PokemonTowerF5":["Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Haunter","Cubone"],"PokemonTowerF6":["Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Haunter","Cubone"],"PokemonTowerF7":["Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Gastly","Haunter","Cubone"],
                        "Route 16":["Rattata","Rattata","Rattata","Raticate","Spearow","Spearow","Spearow","Spearow","Doduo","Doduo"],"Route 17":["Raticate","Raticate","Raticate","Spearow","Spearow","Spearow","Spearow","Fearow","Doduo","Doduo"],"Route 12":["Weepinbell","Venonat","Venonat","Venonat","Venonat","Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout"],"Route 13":["Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Venonat","Venonat","Venonat","Venonat","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Weepinbell","Ditto"],"Route 14":["Pidgeotto","Pidgey","Pidgey","Pidgey","Venonat","Venonat","Venonat","Venonat","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Weepinbell","Ditto","Ditto","Ditto"],"Route 15":["Pidgeotto","Pidgey","Pidgey","Pidgey","Venonat","Venonat","Venonat","Venonat","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Bellsprout","Weepinbell","Ditto","Ditto","Ditto"],"Route 19":["Tentacool"],"Route 20":["Tentacool"],"Route 21 Land":["Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Pidgeotto","Pidgeotto","Pidgeotto","Rattata","Rattata","Rattata","Rattata","Rattata","Rattata","Rattata","Raticate","Raticate","Raticate","Tangela","Tangela"],
                        "Route 21 Sea":["Tentacool"],"PokemonMansionF1":["Vulpix","Vulpix","Ponyta","Ponyta","Ponyta","Ponyta","Ponyta","Ponyta","Ponyta","Ponyta","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Muk","Koffing","Weezing"],"PokemonMansionF2":["Vulpix","Vulpix","Vulpix","Vulpix","Vulpix","Ponyta","Ponyta","Ponyta","Ponyta","Ponyta","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Muk","Koffing","Weezing"],"PokemonMansionF3":["Vulpix","Vulpix","Vulpix","Ponyta","Ponyta","Ponyta","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Muk","Muk","Muk","Koffing","Weezing","Magmar","Magmar"],"PokemonMansionFB1":["Vulpix","Vulpix","Vulpix","Ponyta","Ponyta","Ponyta","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Grimer","Muk","Muk","Koffing","Weezing","Magmar"],"Power Plant":["Pikachu","Pikachu","Pikachu","Pikachu","Pikachu","Raichu","Magnemite","Magnemite","Magnemite","Magnemite","Magnemite","Magneton","Magneton","Voltorb","Voltorb","Voltorb","Voltorb","Voltorb","Voltorb","Voltorb"],"CCave F1":["Raichu","Sandslash","Sandslash","Golbat","Golbat","Golbat","Golbat","Parasect","Venomoth","Venomoth","Kadabra","Magneton","Magneton","Magneton","Dodrio","Dodrio","Hypno","Hypno","Hypno","Hypno","Ditto"],"CCave BF":["Raichu","Raichu","Sandslash","Parasect","Parasect","Electrode","Electrode","Electrode","Marowak","Marowak","Marowak","Rhydon","Rhydon","Rhydon","Rhydon","Rhydon","Chansey","Chansey","Ditto","Ditto"],
                        "CCave F2":["Wigglytuff","Venomoth","Venomoth","Venomoth","Kadabra","Kadabra","Kadabra","Dodrio","Dodrio","Dodrio","Dodrio","Dodrio","Electrode","Electrode","Marowak","Marowak","Rhydon","Rhydon","Chansey","Ditto"]}
WildPokemonLVS = {"Route 1 Pidgey":[2,5],"Route 1 Rattata":[2,4],"Route 2 Pidgey":[3,5],"Route 2 Rattata":[2,5],"Route 2 Caterpie":[3,5],"Route 22 Rattata":[2,4],"Route 22 Spearow":[3,5],"Route 22 NidoranF":[2,4],"Route 22 NidoranM":[3,4],"ViridainForest Pikachu":[3,5],"ViridainForest Caterpie":[3,5],"ViridainForest Metapod":[4,6],"ViridainForest Weedle":[3,3],"ViridainForest Kakuna":[4,4],"Route 3 Pidgey":[6,8],"Route 3 Spearow":[5,8],"Route 3 Jigglypuff":[3,7],"Mt.Moon(1) Zubat":[6,11],"Mt.Moon(1) Geodude":[8,10],"Mt.Moon(1) Paras":[8,8],"Mt.Moon(1) Clefairy":[8,8],"Mt.Moon(2) Zubat":[7,11],"Mt.Moon(2) Geodude":[7,9],"Mt.Moon(2) Paras":[10,10],"Mt.Moon(2) Clefairy":[9,9],"Mt.Moon(3) Zubat":[10,12],"Mt.Moon(3) Geodude":[9,10],"Mt.Moon(3) Paras":[10,12],"Mt.Moon(3) Clefairy":[10,12],"Route 4 Rattata":[8,12],"Route 4 Spearow":[8,12],"Route 4 Sandshrew":[6,12],"Route 24 Caterpie":[7,7],"Route 24 Metapod":[8,8],"Route 24 Pidgey":[12,13],"Route 24 Abra":[8,12],"Route 24 Bellsprout":[12,14],"Route 25 Bellsprout":[12,14],"Route 25 Abra":[10,12],"Route 25 Pidgey":[13,13],"Route 25 Caterpie":[8,8],"Route 25 Metapod":[9,9],"Route 25 Weedle":[8,8],"Route 25 Kakuna":[7,7],
                  "Route 5 Pidgey":[13,16],"Route 5 Meowth":[10,16],"Route 5 Bellsprout":[13,16],"Route 6 Pidgey":[13,16],"Route 6 Meowth":[10,16],"Route 6 Bellsprout":[13,16],"Diglett Cave Diglett":[15,22],"Diglett Cave Dugtrio":[29,31],"Route 11 Sandshrew":[12,15],"Route 11 Drowzee":[9,15],"Route 11 Spearow":[13,17],"Route 9 Rattata":[14,17],"Route 9 Spearow":[13,17],"Route 9 Sandshrew":[11,17],"Route 10 Sandshrew":[11,17],"Route 10 Spearow":[13,17],"Route 10 Voltorb":[14,17],"Rock TunnelF1 Zubat":[15,18],"Rock TunnelF1 Geodude":[16,17],"Rock TunnelF1 Machop":[15,17],"Rock TunnelF1 Onix":[13,15],"Rock TunnelF2 Zubat":[16,18],"Rock TunnelF2 Geodude":[16,18],"Rock TunnelF2 Machop":[15,17],"Rock TunnelF2 Onix":[13,17],"Route 8 Pidgey":[18,20],"Route 8 Vulpix":[15,18],"Route 8 Meowth":[18,20],"Route 8 Sandshrew":[17,19],"Route 7 Pidgey":[19,22],"Route 7 Vulpix":[18,20],"Route 7 Meowth":[17,20],"Route 7 Bellsprout":[19,22],"PokemonTowerF3 Gastly":[18,24],"PokemonTowerF3 Haunter":[25,25],"PokemonTowerF3 Cubone":[20,22],"PokemonTowerF4 Gastly":[18,24],"PokemonTowerF4 Haunter":[25,25],"PokemonTowerF4 Cubone":[20,22],"PokemonTowerF5 Gastly":[18,24],"PokemonTowerF5 Haunter":[25,25],"PokemonTowerF5 Cubone":[20,22],
                  "PokemonTowerF6 Gastly":[19,24],"PokemonTowerF6 Haunter":[26,28],"PokemonTowerF6 Cubone":[22,24],"PokemonTowerF7 Gastly":[20,24],"PokemonTowerF7 Haunter":[28,30],"PokemonTowerF7 Cubone":[22,24],"Route 16 Rattata":[18,22],"Route 16 Raticate":[23,25],"Route 16 Spearow":[20,22],"Route 16 Doduo":[18,22],"Route 17 Raticate":[25,29],"Route 17 Spearow":[20,22],"Route 17 Fearow":[25,27],"Route 17 Doduo":[24,28],"Route 12 Weepinbell":[28,30],"Route 12 Bellsprout":[22,26],"Route 12 Pidgey":[23,27],"Route 12 Venonat":[24,26],"Route 13 Weepinbell":[29,29],"Route 13 Bellsprout":[22,26],"Route 13 Pidgey":[25,27],"Route 13 Venonat":[24,26],"Route 13 Ditto":[25,25],"Route 14 Weepinbell":[30,30],"Route 14 Bellsprout":[22,26],"Route 14 Pidgey":[26,26],"Route 14 Venonat":[24,26],"Route 14 Ditto":[23,23],"Route 14 Pidgeotto":[28,30],"Route 15 Weepinbell":[30,30],"Route 15 Bellsprout":[22,26],"Route 15 Pidgey":[23,23],"Route 15 Venonat":[24,26],"Route 15 Ditto":[26,26],"Route 15 Pidgeotto":[28,30],"Route 19 Tentacool":[5,40],"Route 20 Tentacool":[5,40],"Route 21 Land Pidgey":[21,23],"Route 21 Land Pidgeotto":[30,32],"Route 21 Land Rattata":[21,23],"Route 21 Land Raticate":[30,30],"Route 21 Land Tangela":[28,32],
                  "Route 21 Sea Tentacool":[5,40],"PokemonMansionF1 Vulpix":[34,34],"PokemonMansionF1 Ponyta":[28,34],"PokemonMansionF1 Grimer":[30,32],"PokemonMansionF1 Muk":[37,37],"PokemonMansionF1 Koffing":[30,30],"PokemonMansionF1 Weezing":[39,39],"PokemonMansionF2 Vulpix":[32,32],"PokemonMansionF2 Ponyta":[28,32],"PokemonMansionF2 Grimer":[30,34],"PokemonMansionF2 Muk":[39,39],"PokemonMansionF2 Koffing":[30,30],"PokemonMansionF2 Weezing":[37,37],"PokemonMansionF3 Vulpix":[33,33],"PokemonMansionF3 Ponyta":[32,36],"PokemonMansionF3 Grimer":[31,35],"PokemonMansionF3 Muk":[38,40],"PokemonMansionF3 Koffing":[34,34],"PokemonMansionF3 Weezing":[42,42],"PokemonMansionF3 Magmar":[34,34],"PokemonMansionFB1 Vulpix":[35,35],"PokemonMansionFB1 Ponyta":[32,34],"PokemonMansionFB1 Grimer":[31,33],"PokemonMansionFB1 Muk":[40,40],"PokemonMansionFB1 Koffing":[35,35],"PokemonMansionFB1 Weezing":[42,42],"PokemonMansionFB1 Magmar":[38,38],"Power Plant Pikachu":[20,24],"Power Plant Raichu":[33,36],"Power Plant Magnemite":[21,23],"Power Plant Magneton":[32,35],"Power Plant Voltorb":[21,23],"CCave F1 Raichu":[53,53],"CCave F1 Sandslash":[52,52],"CCave F1 Golbat":[46,46],"CCave F1 Parasect":[52,52],"CCave F1 Venomoth":[49,49],
                  "CCave F1 Kadabra":[49,49],"CCave F1 Magneton":[46,46],"CCave F1 Dodrio":[49,49],"CCave F1 Hypno":[46,46],"CCave F1 Ditto":[53,53],"CCave BF Raichu":[64,64],"CCave BF Sandslash":[57,57],"CCave BF Parasect":[64,64],"CCave BF Electrode":[55,55],"CCave BF Marowak":[55,55],"CCave BF Rhydon":[55,55],"CCave BF Chansey":[64,64],"CCave BF Ditto":[63,67],"CCave F2 Wigglytuff":[54,54],"CCave F2 Venomoth":[51,51],"CCave F2 Kadabra":[51,51],"CCave F2 Dodrio":[51,51],"CCave F2 Electrode":[52,52],"CCave F2 Marowak":[52,52],"CCave F2 Rhydon":[52,52],"CCave F2 Chansey":[56,56],"CCave F2 Ditto":[55,60]}

SafariPokemonLocations = {"Main Area":["NidoranM","NidoranM","NidoranM","NidoranM","NidoranM","Nidorina","Nidorina","Nidorino","Parasect","Venonat","Venonat","Venonat","Exeggcute","Exeggcute","Exeggcute","Exeggcute","Rhyhorn","Rhyhorn","Rhyhorn","Chansey","Pinsir"],"Area 1":["NidoranM","NidoranM","NidoranM","NidoranM","NidoranM","Nidorina","Nidorina","NidoranF","Parasect","Paras","Paras","Paras","Doduo","Doduo","Doduo","Exeggcute","Exeggcute","Exeggcute","Exeggcute","Kangaskhan","Pinsir"],"Area 2":["NidoranM","NidoranM","NidoranM","NidoranM","NidoranM","Nidorina","Nidorina","Nidorino","Paras","Paras","Paras","Venomoth","Exeggcute","Exeggcute","Exeggcute","Exeggcute","Rhyhorn","Rhyhorn","Rhyhorn","Chansey","Tauros"],"Area 3":["NidoranF","NidoranF","NidoranF","NidoranF","NidoranF","Nidorina","Nidorina","NidoranM","Venonat","Venonat","Venonat","Venomoth","Doduo","Doduo","Doduo","Exeggcute","Exeggcute","Exeggcute","Exeggcute","Kangaskhan","Tauros"]}
SafariPokemonLVS = {"Main Area NidoranM":[22,22],"Main Area Nidorina":[31,31],"Main Area Nidorino":[31,31],"Main Area Parasect":[30,30],"Main Area Venonat":[22,22],"Main Area Exeggcute":[24,25],"Main Area Rhyhorn":[25,25],"Main Area Chansey":[23,23],"Main Area Pinsir":[23,23],"Area 1 NidoranM":[24,24],"Area 1 Nidorina":[33,33],"Area 1 NidoranF":[24,24],"Area 1 Paras":[22,22],"Area 1 Parasect":[25,25],"Area 1 Doduo":[26,26],"Area 1 Exeggcute":[23,25],"Area 1 Kangaskhan":[25,25],"Area 1 Pinsir":[28,28],"Area 2 NidoranM":[22,22],"Area 2 Nidorina":[30,30],"Area 2 Nidorino":[30,30],"Area 2 Paras":[23,23],"Area 2 Venomoth":[32,32],"Area 2 Exeggcute":[25,27],"Area 2 Rhyhorn":[26,26],"Area 2 Chansey":[26,26],"Area 2 Tauros":[28,28], "Area 3 NidoranF":[25,25],"Area 3 Nidorina":[33,33],"Area 3 NidoranM":[25,25],"Area 3 Venonat":[23,23],"Area 3 Venomoth":[31,31],"Area 3 Doduo":[26,26],"Area 3 Exeggcute":[24,26],"Area 3 Kangaskhan":[28,28],"Area 3 Tauros":[26,26]}

WildPokemonLocations.update(SafariPokemonLocations)
WildPokemonLVS.update(SafariPokemonLVS)

VictoryRoadPokemonLocations = {"Victory Road F1":["Zubat","Zubat","Zubat","Golbat","Machop","Machop","Machop","Machop","Machop","Machoke","Geodude","Geodude","Geodude","Graveler","Marowak","Onix","Onix","Onix","Onix","Onix","Onix"],"Victory Road F2":["Zubat","Zubat","Zubat","Golbat","Machop","Machop","Machop","Machop","Machop","Machoke","Geodude","Geodude","Geodude","Graveler","Marowak","Onix","Onix","Onix","Onix","Onix","Onix"],
                               "Victory Road F3":["Zubat","Zubat","Zubat","Golbat","Machop","Machop","Machop","Machop","Machop","Venomoth","Venomoth","Geodude","Geodude","Geodude","Graveler","Onix","Onix","Onix","Onix"]}
VictoryRoadPokemonLVS = {"Victory Road F1 Zubat":[22,22],"Victory Road F1 Golbat":[41,41],"Victory Road F1 Machop":[24,24],"Victory Road F1 Machoke":[42,42],"Victory Road F1 Geodude":[26,26],"Victory Road F1 Graveler":[41,41],"Victory Road F1 Onix":[36,42],"Victory Road F1 Marowak":[43,43],"Victory Road F2 Zubat":[26,26],"Victory Road F2 Golbat":[40,40],"Victory Road F2 Machop":[22,22],"Victory Road F2 Machoke":[41,41],"Victory Road F2 Geodude":[24,24],"Victory Road F2 Graveler":[43,43],"Victory Road F2 Onix":[36,42],"Victory Road F2 Marowak":[40,40],
"Victory Road F3 Zubat":[22,22],"Victory Road F3 Golbat":[41,41],"Victory Road F3 Machop":[24,24],"Victory Road F3 Machoke":[42,45],"Victory Road F3 Geodude":[26,26],"Victory Road F3 Graveler":[43,43],"Victory Road F3 Onix":[42,45],"Victory Road F3 Venomoth":[40,40]}

WildPokemonLocations.update(VictoryRoadPokemonLocations)
WildPokemonLVS.update(VictoryRoadPokemonLVS)

SeaFoamIslandPokemonLocations = {"SFIF1":["Zubat","Zubat","Golbat","Psyduck","Psyduck","Psyduck","Psyduck","Slowpoke","Slowbro","Seel","Seel","Seel","Seel","Krabby","Krabby","Krabby","Krabby","Staryu","Staryu","Staryu","Staryu"],"SFIFB1":["Psyduck","Psyduck","Psyduck","Seel","Seel","Seel","Dewgong","Shellder","Shellder","Shellder","Shellder","Krabby","Krabby","Krabby","Krabby","Krabby","Krabby","Kingler","Staryu","Staryu","Staryu"],"SFIFB2":["Golbat","Psyduck","Psyduck","Psyduck","Psyduck","Psyduck","Psyduck","Golduck","Seel","Seel","Seel","Seel","Seel","Seel","Seel","Shellder","Shellder","Krabby","Krabby","Krabby","Staryu"],"SFIFB3":["Psyduck","Psyduck","Psyduck","Psyduck","Psyduck","Psyduck","Psyduck","Seel","Seel","Seel","Seel","Seel","Seel","Dewgong","Krabby","Krabby","Krabby","Kingler","Staryu","Staryu","Staryu"],"SFIFB4":["Golbat","Psyduck","Psyduck","Psyduck","Golduck","Seel","Seel","Seel","Krabby","Krabby","Krabby","Krabby","Krabby","Krabby","Krabby","Staryu","Staryu","Staryu","Staryu","Staryu","Staryu"]}
SeaFoamIslandPokemonLVS = {"SFIF1 Zubat":[21,21],"SFIF1 Golbat":[29,29],"SFIF1 Psyduck":[30,30],"SFIF1 Slowpoke":[28,28],"SFIF1 Slowbro":[38,38],"SFIF1 Seel":[30,30],"SFIF1 Krabby":[28,30],"SFIF1 Staryu":[28,30],"SFIFB1 Psyduck":[28,30],"SFIFB1 Dewgong":[38,38],"SFIFB1 Seel":[28,30],"SFIFB1 Shellder":[30,30],"SFIFB1 Krabby":[30,32],"SFIFB1 Staryu":[32,32],"SFIFB1 Kingler":[37,37],"SFIFB2 Golbat":[30,30],"SFIFB2 Psyduck":[30,32],"SFIFB2 Golduck":[37,37],"SFIFB2 Seel":[30,32],"SFIFB2 Shellder":[30,30],"SFIFB2 Krabby":[28,30],"SFIFB2 Staryu":[28,28],
                           "SFIFB3 Psyduck":[31,33],"SFIFB3 Seel":[31,33],"SFIFB3 Dewgong":[37,37],"SFIFB3 Krabby":[29,31],"SFIFB3 Kingler":[39,39],"SFIFB3 Staryu":[29,31],"SFIFB4 Golbat":[32,32],"SFIFB4 Psyduck":[29,31],"SFIFB4 Golduck":[39,39],"SFIFB4 Seel":[29,31],"SFIFB4 Krabby":[31,33],"SFIFB4 Staryu":[31,33]}

WildPokemonLocations.update(SeaFoamIslandPokemonLocations)
WildPokemonLVS.update(SeaFoamIslandPokemonLVS)

TrainerImgs = {"Bug Catcher":"Trainer_imgs\Bug_Catcher.png","JR.TRAINER(Male)":"Trainer_imgs\Jr_Trainer_male.png","JR.TRAINER(FEMALE)":"Trainer_imgs\Jr_Trainer_female.png","Brock":"Trainer_imgs\Brock.png","Lass":"Trainer_imgs\Lass.png","Youngster":"Trainer_imgs\Youngster.png","Hiker":"Trainer_imgs\Hiker.png","Super Nerd":"Trainer_imgs\Super_Nerd.png","Rocket":"Trainer_imgs\Rocket.png","Swimmer":"Trainer_imgs\Swimmer.png","Misty":"Trainer_imgs\Misty.png","Gentleman":"Trainer_imgs\Gentleman.png","Sailor":"Trainer_imgs\Sailor.png","Fisherman":"Trainer_imgs\Fisherman.png","Rocker":"Trainer_imgs\Rocker.png","Lt.Surge":"Trainer_imgs\Lt.Surge.png","Engineer":"Trainer_imgs\Engineer.png","Gambler":"Trainer_imgs\Gambler.png","Pokemaniac":"Trainer_imgs\PokéManiac.png","CooltrainerF":"Trainer_imgs\CoolTrainerF.png","CooltrainerM":"Trainer_imgs\CoolTrainerM.png","Erika":"Trainer_imgs\Erika.png","Beauty":"Trainer_imgs\Beauty.png","Giovanni":"Trainer_imgs\Giovanni.png","Channeler":"Trainer_imgs\Channeler.png","Biker":"Trainer_imgs\Biker.png","Cue Ball":"Trainer_imgs\Cue_Ball.png","Bird Keeper":"Trainer_imgs\Bird Keeper.png","Tamer":"Trainer_imgs\Tamer.png","Juggler":"Trainer_imgs\Juggler.png","Koga":"Trainer_imgs\Koga.png","Scientist":"Trainer_imgs\Scientist.png","Blackbelt":"Trainer_imgs\Blackbelt.png","Psychic":"Trainer_imgs\Psychic.png","Sabrina":"Trainer_imgs\Sabrina.png",
               "Burglar":"Trainer_imgs\Burglar.png","Blaine":"Trainer_imgs\Blaine.png","Lorelei":"Trainer_imgs\Lorelei.png","Bruno":"Trainer_imgs\Bruno.png","Agatha":"Trainer_imgs\Agatha.png","Lance":"Trainer_imgs\Lance.png","Oak":"Trainer_imgs\Dr.Oak.png","Creator":"Trainer_imgs\Super_Nerd.png"}

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos:tuple,surf,groups,Name:str = "Tile"):
        super().__init__(groups)
        self.Name = Name
        self.group = groups
        self.image = surf
        self.rect = self.image.get_rect(topleft = (pos))

class SecretTrashcans:
    def __init__(self,x:int,y:int,w:int,h:int):
        self.Rect = pygame.Rect(x,y,w,h)
        self.SwitchOn = False
        self.HasSwitch = False

class WildPokemonTiles:
    def __init__(self,x:int,y:int,w:int,h:int,Location:str,Lowest_Chance:int,Highest_Chance:int,Tiletype="Grass"):
        self.Patch = pygame.Rect(x,y,w,h)
        self.Place = Location
        if Tiletype == "Grass":self.Pokemon = WildPokemonLocations[Location]
        self.Low_Chance = Lowest_Chance
        self.High_CHance = Highest_Chance
        self.WildPokemon = Pokemon
        self.MakeRandomWildPokemon()
    
    def MakeRandomWildPokemon(self):
        Name = random.choice(self.Pokemon)
        LvRange = WildPokemonLVS[f"{self.Place} {Name}"]  
        Level = random.randint(LvRange[0],LvRange[1])
        self.WildPokemon = Pokemon(Name,Level,["Tackle"],"Wild",Name)
        self.WildPokemon.Moves = self.WildPokemon.Last4Moves(self.WildPokemon.Level)

class Terrains:
    def __init__(self,x:int,y:int,w:int,h:int,land:str):
        self.Rect = pygame.Rect(x,y,w,h)
        self.Land = land

class HiddenItems:
    def __init__(self,x:int,y:int,w:int,h:int,Item:str):
        self.Rect = pygame.Rect(x,y,w,h)
        self.Item = Item
        self.Picked = False

class Readables:
    def __init__(self,x:int,y:int,w:int,h:int,Text:str,Name = "",Text2:str = "",Text3:str = ''):
        self.Rect = pygame.Rect(x,y,w,h)
        self.Text = Text
        self.Text2= Text2
        self.Text3 = Text3
        self.Name = Name

class Question:
    def __init__(self,x:int,y:int,w:int,h:int,Question:str):
        self.Rect = pygame.Rect(x,y,w,h)
        self.Answered = False
        self.Correct = False
        self.Q = Question

class Interactions:
    def __init__(self,x,y,w,h,Name):
        self.Rect = pygame.Rect(x,y,w,h)
        self.Name = Name

class MoverBlocks:
    def __init__(self,x,y,w,h,Direction):
        self.rect = pygame.Rect(x,y,w,h)
        self.Way = Direction

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.Display_Surf = pygame.display.get_surface()
        #Camera offfset
        self.offset = pygame.math.Vector2()
        self.half_w = self.Display_Surf.get_width()//2
        self.half_y = self.Display_Surf.get_height()//2

        self.internal_surf_size = (800,800)
        self.internal_surf = pygame.Surface(self.internal_surf_size,pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_y))
        self.internal_surf_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offest = pygame.math.Vector2()
        self.internal_offest.x = self.internal_surf_size[0]//2 - self.half_w
        self.internal_offest.y = self.internal_surf_size[1]//2 - self.half_y

    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_y

    # def Zoom(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_q]: self.Zoom_Scale -= 0.1
    #     elif keys[pygame.K_e]: self.Zoom_Scale += 0.1

    def custom_draw(self,Player,Draw):
        if Draw:
            self.center_target_camera(Player)

            self.internal_surf.fill("Black")
            
            for sprite in self.sprites():
                offset_pos = sprite.rect.topleft - self.offset + self.internal_offest
                self.internal_surf.blit(sprite.image,offset_pos)
            
            scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surf_size_vector * 2)
            scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_y))

            self.Display_Surf.blit(scaled_surf,scaled_rect)

class Pickups(pygame.sprite.Sprite):
    def __init__(self,pos:tuple,surf,groups,Item):
        super().__init__(groups)
        self.image = surf
        self.group = groups
        self.rect = self.image.get_rect(topleft = (pos))
        self.Item = Item
        self.Picked = False
        
class Transportion:
    def __init__(self,x,y,w,h,Desination):
        self.Rect = pygame.Rect(x,y,w,h)
        self.Desination = Desination

class NPC(pygame.sprite.Sprite):
    def __init__(self,sprite:pygame.Surface,Group:pygame.sprite.Group,Type:str,pos:tuple,Text1_a:str,Name:str,Text1_b:str = "",Text1_c:str = '',Item:str = '',ItemAmount:int = 0,IA1:str = '0',IA2:str = '0',IA3:str = '0',Store:str = "PokeBall-100,Heal-500"):
        super().__init__(Group)
        self.image = sprite
        self.Group = Group
        self.rect = self.image.get_rect(topleft = pos)
        self.org_pos = pos
        self.Type1 = Type
        self.Item = Item
        self.ItemAmount = ItemAmount
        self.type = self.Type1
        self.Text1_a = Text1_a
        self.Text1_b = Text1_b
        self.Text1_c = Text1_c
        self.Text = [self.Text1_a,self.Text1_b,self.Text1_c]
        self.IA1 = IA1
        self.IA2 = IA2
        self.IA3 = IA3
        self.Name = Name
        self.Store = Store.split(",")
        for i in range(len(self.Store)):
            self.Store[i] = self.Store[i].split("-")

class TraderNPC(pygame.sprite.Sprite):
    def __init__(self,sprite:pygame.Surface,Group:pygame.sprite.Group,Type:str,pos:tuple,Text1_a:str,Name:str,HisPokemon:Pokemon,YourPokemon:Pokemon,PokeNickName:str,Text1_b:str = "",Text1_c:str = '',IA1:str = '0',IA2:str = '0',IA3:str = '0'):
        super().__init__(Group)
        self.image = sprite
        self.rect = self.image.get_rect(topleft = pos)
        self.Type1 = Type
        self.type = self.Type1
        self.Text1_a = Text1_a
        self.Text1_b = Text1_b
        self.Text1_c = Text1_c
        self.Name = Name
        self.HisPokemon = HisPokemon
        self.YourPokemon = YourPokemon
        self.PokemonNickname = PokeNickName
        self.Traded = False
    
class TrainerNPC(pygame.sprite.Sprite):
    def __init__(self,Name:str,sprite:pygame.Surface,Group:pygame.sprite.Group,pos:tuple,Team:str,PBT:list[str],AftermathText:list[str],Money:int,WinnerText:list[str],Side:str,Bag:list,CompName:str):
        super().__init__(Group)
        self.image = sprite
        self.rect = self.image.get_rect(topleft = pos)
        self.org_pos = pos
        self.preBattleText = PBT
        self.group = Group
        self.WinnerText = WinnerText
        if len(self.WinnerText) < 3:
            for i in range(3 -len(self.WinnerText)):
                self.WinnerText.append("")
        self.AftermathText = AftermathText
        self.Name = Name
        self.CompName = CompName
        self.Money = Money
        self.Bag = Bag
        if self.Bag == None:self.Bag = []
        self.TextTeam = Team.split(",")
        self.TextTeam = [p.split("-") for p in self.TextTeam]
        for p in range(len(self.TextTeam)): self.TextTeam[p][2] = self.TextTeam[p][2].split("_")
        self.Team = []
        for pokemon in self.TextTeam:self.Team.append(Pokemon(pokemon[0],int(pokemon[1]),pokemon[2],pokemon[3],pokemon[4]))
        self.Text = PBT
        self.Vision = None
        try: 
            self.Trainer_img = pygame.image.load(TrainerImgs[self.CompName]).convert_alpha()
        except: 
            if "JR.TRAINER(Male)" in self.CompName:self.Trainer_img = pygame.image.load(TrainerImgs["JR.TRAINER(Male)"]).convert_alpha()
            elif "JR.TRAINER(FEMALE)" in self.CompName:self.Trainer_img = pygame.image.load(TrainerImgs["JR.TRAINER(FEMALE)"]).convert_alpha()
            elif "CooltrainerF" in self.CompName:self.Trainer_img = pygame.image.load(TrainerImgs["CooltrainerF"]).convert_alpha()
            else:self.Trainer_img = pygame.image.load(TrainerImgs[self.Name]).convert_alpha()
        self.Battled = False
        self.Side = Side
    
    def Back_to_Pos(self):
        if self.Battled:
            self.rect.topleft = self.org_pos

    def TextChange(self):
        if self.Battled:
            self.Text = self.AftermathText

class GymLeaderNPC(pygame.sprite.Sprite):
    def __init__(self,Name:str,sprite:pygame.Surface,Group:pygame.sprite.Group,pos:tuple,Team:str,BT:list[str],AftermathText:list[str],Money:int,WinnerText:list[str],Bag:list,ExtraWinnerText:list[str]):
        super().__init__(Group)
        self.image = sprite
        self.rect = self.image.get_rect(topleft = pos)
        self.BeginningText = BT
        self.WinnerText = WinnerText
        self.ExtraWinner = ExtraWinnerText
        self.AftermathText = AftermathText
        self.Name = Name
        self.Money = Money
        self.type = ""
        self.Bag = Bag
        self.Bag = Bag.split("-")
        self.TextTeam = Team.split(",")
        self.TextTeam = [p.split("-") for p in self.TextTeam]
        for p in range(len(self.TextTeam)): self.TextTeam[p][2] = self.TextTeam[p][2].split("_")
        self.Team = []
        for pokemon in self.TextTeam:self.Team.append(Pokemon(pokemon[0],int(pokemon[1]),pokemon[2],pokemon[3],pokemon[4]))
        self.Text = BT
        self.Trainer_img = pygame.image.load(TrainerImgs[self.Name]).convert_alpha()
        self.Battled = False


    def TextChange(self):
        if self.Battled:
            self.type = "AfterBattleDialogue"
            self.Text = self.AftermathText

class Rocks(pygame.sprite.Sprite):
    def __init__(self,pos:tuple,surf,groups,Borders:list[pygame.Rect],Cameras = ()):
        super().__init__(groups)
        self.group = groups
        self.image = surf
        self.Cameras = Cameras
        self.rect = self.image.get_rect(topleft = (pos))
        self.Borders = Borders
        self.Speed = [0,0]
        self.Org_pos = pos
        self.Moving = False
    
    def Set_Speed(self,x,y):
        self.Speed[0] = x
        self.Speed[1] = y
        self.Moving = True

    def Reset(self,Camera):
        if Camera not in self.Cameras: self.rect.topleft = self.Org_pos

    def Transport(self,Door,Pos,Camera):
        if self.rect.colliderect(Door):
            self.rect.center = Pos
            self.group.remove(self)
            self.group = Camera
            self.group.add(self)
            return True
        return False

    def Move(self):
        if self.Speed[0] > 0: 
            self.rect.x += 1
            self.Speed[0] -= 1 
            self.Horizontal_Collison()
        elif self.Speed[0] < 0: 
            self.rect.x -= 1
            self.Speed[0] += 1 
            self.Horizontal_Collison()
        elif self.Speed[1] > 0: 
            self.rect.y += self.Speed[1]
            self.Speed[1] -= 1
            self.Vertical_Collison()
        elif self.Speed[1] < 0: 
            self.rect.y += self.Speed[1]
            self.Speed[1] += 1
            self.Vertical_Collison()
        else:self.Moving = False

    def Horizontal_Collison(self):
        for rect in self.Borders:
            if rect.colliderect(self.rect):
                if self.Speed[0] < 0 and self.rect.right -1!= rect.left and self.rect.bottom - 1!=  rect.top and self.rect.top + 1!= rect.bottom:
                    self.rect.left = rect.right
                if self.Speed[0] > 0 and self.rect.left +1 != rect.right and self.rect.bottom - 1!=  rect.top and self.rect.top + 1!= rect.bottom:
                    self.rect.right = rect.left

    def Vertical_Collison(self):
        for rect in self.Borders:
            if rect.colliderect(self.rect):
                if self.Speed[1] < 0 and self.rect.bottom - 1!=  rect.top and self.rect.right -1!= rect.left and self.rect.left +1!= rect.right:
                    self.rect.top = rect.bottom
                if self.Speed[1] > 0 and self.rect.top + 1!= rect.bottom and self.rect.right -1!= rect.left and self.rect.left +1!= rect.right:
                    self.rect.bottom = rect.top
#crtl k+0
class TrainerVision:
    def __init__(self,x:int,y:int,w:int,h:int,Trainer:str):
        self.rect = pygame.Rect(x,y,w,h)
        self.Trainer = Trainer

class Kanto:
    def __init__(self):
        self.Kanto =  load_pygame('Map\Kanto.tmx')
        self.PlayerHouse = load_pygame('Map\Player_House.tmx')
        self.RivalHouse = load_pygame("Map\Rival_House.tmx")
        self.OakLab = load_pygame("Map\Oak_Lab.tmx")
        self.PokeMart = load_pygame("Map\PokeMart.tmx")
        self.PokeCenter = load_pygame("Map\PokeCenter.tmx")
        self.VH1 = load_pygame("Map\VH1.tmx")
        self.VH2 = load_pygame("Map\VH2.tmx")
        self.PokemonLeagueF1 = load_pygame("Map\Pokemon_LeagueF1.tmx")
        self.ViridainForest = load_pygame("Map\ViridainForest.tmx")
        self.PreForest = load_pygame("Map\Pre_Forest.tmx")
        self.AfterForest = load_pygame("Map\After_Forest.tmx")
        self.PH1 = load_pygame("Map\PH1.tmx")
        self.PH2 = load_pygame("Map\PH2.tmx")
        self.PewterGym = load_pygame("Map\Pewter_Gym.tmx")
        self.PewterMuseum = load_pygame("Map\Pewter_Museum.tmx")
        self.Mt_Moon = load_pygame("Map\Mt.Moon.tmx")
        self.CCH1 = load_pygame("Map\CC1House.tmx")
        self.CCH2 = load_pygame("Map\CCH2.tmx")
        self.Bike_Shop = load_pygame("Map\Bike_Shop.tmx")
        self.CCGym = load_pygame("Map\CCGym.tmx")
        self.Sea_Cottage = load_pygame("Map\Sea_Cottage.tmx")
        self.Robbed_House = load_pygame("Map\Robbed_House.tmx")
        self.DayCare = load_pygame("Map\DayCare.tmx")
        self.BetweenR5_SC = load_pygame("Map\R5ToSaffron.tmx")
        self.UndergroundEntrance = load_pygame(r"Map\Underground_Entrance.tmx")
        self.UndergroundNSTunnel = load_pygame(r"Map\Underground_NSTunnel.tmx")
        self.VCH1 = load_pygame("Map\VCH1.tmx")
        self.PokemonFanClub = load_pygame("Map\PokeFan_Club.tmx")
        self.SS_Anne = load_pygame("Map\SS.Anne.tmx")
        self.SS_AnneF0 = load_pygame("Map\SS.AnneBottom.tmx")
        self.SS_AnneF2 = load_pygame("Map\SS.AnneSecondFloor.tmx")
        self.SS_AnneF3 = load_pygame("Map\SS.AnneThirdFloor.tmx")
        self.VCGym = load_pygame("Map\VCGym.tmx")
        self.DiglettCave = load_pygame("Map\Diglett_Cave.tmx")
        self.R21H = load_pygame("Map\R21H.tmx")
        self.R22H = load_pygame("Map\R22H.tmx")
        self.R11H = load_pygame("Map\R11H.tmx")
        self.Rock_Tunnel = load_pygame("Map\Rock_Tunnel.tmx")
        self.LTVolunteerHouse = load_pygame("Map\LT_VolunteerHouse.tmx")
        self.LT1H = load_pygame("Map\LTH1.tmx")
        self.SaffronEWEntrance = load_pygame("Map\SaffronEWEntrance.tmx")
        self.Underground_EWEntrance = load_pygame(r"Map\Underground_EWEntrance.tmx")
        self.Underground_WETunnel = load_pygame(r"Map\Underground_WETunnel.tmx")
        self.Game_Corner = load_pygame("Map\Game_Corner.tmx")
        self.Prize_Booth = load_pygame("Map\Prize_Booth.tmx")
        self.CERestourant = load_pygame("Map\CERestourant.tmx")
        self.CE1H = load_pygame("Map\CE1H.tmx")
        self.CE2H = load_pygame("Map\CE2H.tmx")
        self.CEMansion = load_pygame("Map\Celadon_Mansion.tmx")
        self.CEStore = load_pygame("Map\CEStore.tmx")
        self.CEGym = load_pygame("Map\CEGym.tmx")
        self.Rocket_Hideout = load_pygame("Map\Rocket_Hideout.tmx")
        self.Pokemon_Tower = load_pygame("Map\Pokemon_Tower.tmx")
        self.R16GuardHouse = load_pygame("Map\R16GuardHouse.tmx")
        self.R16House2 = load_pygame("Map\R16H2.tmx")
        self.R18GuardHouse = load_pygame("Map\R18GuardHouse.tmx")
        self.FCH1 = load_pygame("Map\FCH1.tmx")
        self.FCH2 = load_pygame("Map\FCH2.tmx")
        self.FCH3 = load_pygame("Map\FCH3.tmx")
        self.FCWH = load_pygame("Map\FCWH.tmx")
        self.SZE = load_pygame("Map\Safari_Zone_Entrance.tmx")
        self.Safari_Zone = load_pygame("Map\Safari_Zone.tmx")
        self.SZMAH1 = load_pygame("Map\SZMAH1.tmx")
        self.SZA3SH = load_pygame("Map\SZA3SecretHouse.tmx")
        self.FCGym = load_pygame("Map\FGym.tmx")
        self.SFH1 = load_pygame("Map\SFH1.tmx")
        self.SFH2 = load_pygame("Map\SFH2.tmx")
        self.SFH3 = load_pygame("Map\SFH3.tmx")
        self.Fighting_Dojo = load_pygame("Map\FightingDojo.tmx")
        self.Silph_Co = load_pygame("Map\Silph_Co.tmx")
        self.SFGym = load_pygame("Map\SFGym.tmx")
        self.R12GH = load_pygame("Map\R12GH.tmx")
        self.R12H = load_pygame("Map\R12H.tmx")
        self.R15GH = load_pygame("Map\R15GH.tmx")
        self.Pokemon_Lab = load_pygame("Map\PokemonLab.tmx")
        self.Pokemon_Mansion = load_pygame("Map\Pokemon_Mansion.tmx")
        self.CGym = load_pygame("Map\CGym.tmx")
        self.VGym = load_pygame("Map\VGym.tmx")
        self.VRoad = load_pygame("Map\Victory_Road.tmx")
        self.IndigoPlateauEntrance = load_pygame("Map\IndigoLeagueEntrance.tmx")
        self.IndigoPlateau = load_pygame("Map\IndigoPlateau_Elite4.tmx")
        self.IndigoPlateauChampion = load_pygame("Map\IndigoPlateau_Champion.tmx")
        self.Fame_Hall = load_pygame("Map\Fame_Hall.tmx")
        self.Power_Plant = load_pygame("Map\Power_Plant.tmx")
        self.SeaFoam_Island = load_pygame("Map\SeaFoam_Island.tmx")
        self.Cerulean_Cave = load_pygame("Map\Cerulean_Cave.tmx")
        self.OverworldCamera = CameraGroup()
        self.PLayerHouse1Camera = CameraGroup()
        self.PLayerHouse0Camera = CameraGroup()
        self.RivalHouseCamera = CameraGroup()
        self.OakLabCamera = CameraGroup()
        self.PokeMartCamera = CameraGroup()
        self.PokeCenterCamera = CameraGroup()
        self.PokemonLeagueF1Camera = CameraGroup()
        self.VH1Camera = CameraGroup()
        self.VH2Camera = CameraGroup()
        self.ViridainForestCamera = CameraGroup()
        self.PreForestCamera = CameraGroup()
        self.AfterForestCamera = CameraGroup()
        self.PH1Camera = CameraGroup()
        self.PH2Camera = CameraGroup()
        self.PewterGymCamera = CameraGroup()
        self.PewterMuseumCamera = CameraGroup()
        self.PewterMuseumBasementCamera = CameraGroup()
        self.Mt_MoonFloor1Camera = CameraGroup()
        self.Mt_MoonFloor2Camera = CameraGroup()
        self.Mt_MoonFloor3Camera = CameraGroup()
        self.CCH1Camera = CameraGroup()
        self.CCH2Camera = CameraGroup()
        self.Bike_ShopCamera = CameraGroup()
        self.CCGymCamera = CameraGroup()
        self.Sea_CottageCamera = CameraGroup()
        self.Robbed_HouseCamera = CameraGroup()
        self.DayCareCamera = CameraGroup()
        self.BetweenR5_SCCamera = CameraGroup()
        self.BetweenR6_SCCamera = CameraGroup()
        self.UndergroundEntranceCamera = CameraGroup()
        self.UndergroundNSTunnelCamera = CameraGroup()
        self.UndergroundSEntranceCamera = CameraGroup()
        self.VCH1Camera = CameraGroup()
        self.VCH2Camera = CameraGroup()
        self.VCH3Camera = CameraGroup()
        self.PokemonFanClubCamera = CameraGroup()
        self.SS_AnneF1Camera = CameraGroup()
        self.SS_AnneF1RoomsCamera = CameraGroup()
        self.SS_AnneF1KitchenCamera = CameraGroup()
        self.SS_AnneF0Camera = CameraGroup()
        self.SS_AnneF0RoomsCamera = CameraGroup()
        self.SS_AnneF2Camera = CameraGroup()
        self.SS_AnneF2RoomsCamera = CameraGroup()
        self.SS_AnneF3HallWayCamera = CameraGroup()
        self.SS_AnneF3Camera = CameraGroup()
        self.SS_AnneF2CaptainCamera = CameraGroup()
        self.VCGymCamera = CameraGroup()
        self.DiglettCaveEntranceCamera = CameraGroup()
        self.DiglettCaveCamera = CameraGroup()
        self.DiglettCaveExitCamera = CameraGroup()
        self.R21HCamera = CameraGroup()
        self.R22HCamera = CameraGroup()
        self.R11HCamera = CameraGroup()
        self.R11F2HCamera = CameraGroup()
        self.Rock_TunnelF1LightCamera = CameraGroup()
        self.Rock_TunnelF1DarkCamera = CameraGroup()
        self.Rock_TunnelF2LightCamera = CameraGroup()
        self.Rock_TunnelF2DarkCamera = CameraGroup()
        self.LTVolunteerHouseCamera = CameraGroup()
        self.LT1HCamera = CameraGroup()
        self.LT2HCamera = CameraGroup()
        self.SaffronEEntranceCamera = CameraGroup()
        self.Underground_EEntranceCamera = CameraGroup()
        self.Underground_WEntranceCamera = CameraGroup()
        self.Underground_WETunnelCamera = CameraGroup()
        self.Game_CornerNormalCamera = CameraGroup()
        self.Game_CornerSecretCamera = CameraGroup()
        self.Prize_BoothCamera = CameraGroup()
        self.CERestourantCamera = CameraGroup()
        self.CE1HCamera = CameraGroup()
        self.CE2HCamera = CameraGroup()
        self.CEMansionF1Camera = CameraGroup()
        self.CEMansionF2Camera = CameraGroup()
        self.CEMansionF3Camera = CameraGroup()
        self.CEMansionF4Camera = CameraGroup()
        self.CEMansionF4HouseCamera = CameraGroup()
        self.CEStoreF1Camera = CameraGroup()
        self.CEStoreF2Camera = CameraGroup()
        self.CEStoreF3Camera = CameraGroup()
        self.CEStoreF4Camera = CameraGroup()
        self.CEStoreF5Camera = CameraGroup()
        self.CEStoreRooftopCamera = CameraGroup()
        self.CEStoreElevatorCamera = CameraGroup()
        self.CEGymCamera = CameraGroup()
        self.Rocket_HideoutF1Camera = CameraGroup()
        self.Rocket_HideoutF2Camera = CameraGroup()
        self.Rocket_HideoutF3Camera = CameraGroup()
        self.Rocket_HideoutF4Camera = CameraGroup()
        self.Rocket_HideoutElevatorCamera = CameraGroup()
        self.Pokemon_TowerF1Camera = CameraGroup()
        self.Pokemon_TowerF2Camera = CameraGroup()
        self.Pokemon_TowerF3Camera = CameraGroup()
        self.Pokemon_TowerF4Camera = CameraGroup()
        self.Pokemon_TowerF5Camera = CameraGroup()
        self.Pokemon_TowerF6Camera = CameraGroup()
        self.Pokemon_TowerF7Camera = CameraGroup()
        self.R16GuardHouseCamera = CameraGroup()
        self.R16GuardHouseF2Camera = CameraGroup()
        self.R16House2Camera = CameraGroup()
        self.R18GuardHouseCamera = CameraGroup()
        self.R18GuardHouseF2Camera = CameraGroup()
        self.FCH1Camera = CameraGroup()
        self.FCH2Camera = CameraGroup()
        self.FCH3Camera = CameraGroup()
        self.FCWHCamera = CameraGroup()
        self.SZECamera = CameraGroup()
        self.Safari_ZoneMZCamera = CameraGroup()
        self.SZMAH1Camera = CameraGroup()
        self.Safari_ZoneA1Camera = CameraGroup()
        self.SZA1RestHouseCamera = CameraGroup()
        self.Safari_ZoneA2Camera = CameraGroup()
        self.SZA2RestHouseCamera = CameraGroup()
        self.Safari_ZoneA3Camera = CameraGroup()
        self.SZA3RestHouseCamera = CameraGroup()
        self.SZA3SHCamera = CameraGroup()
        self.FCGymCamera = CameraGroup()
        self.SFH1Camera = CameraGroup()
        self.SFH2Camera = CameraGroup()
        self.SFH3F1Camera = CameraGroup()
        self.SFH3F2Camera = CameraGroup()
        self.Fighting_DojoCamera = CameraGroup()
        self.Silph_CoF1Camera = CameraGroup()
        self.Silph_CoF2Camera = CameraGroup()
        self.Silph_CoF3Camera = CameraGroup()
        self.Silph_CoF4Camera = CameraGroup()
        self.Silph_CoF5Camera = CameraGroup()
        self.Silph_CoF6Camera = CameraGroup()
        self.Silph_CoF7Camera = CameraGroup()
        self.Silph_CoF8Camera = CameraGroup()
        self.Silph_CoF9Camera = CameraGroup()
        self.Silph_CoF10Camera = CameraGroup()
        self.Silph_CoF11Camera = CameraGroup()
        self.Silph_CoElevatorCamera = CameraGroup()
        self.SFGymCamera = CameraGroup()
        self.R12GHCamera = CameraGroup()
        self.R12GHF2Camera = CameraGroup()
        self.R12HCamera = CameraGroup()
        self.R15GHCamera = CameraGroup()
        self.R15GHF2Camera = CameraGroup()
        self.Pokemon_LabHallCamera = CameraGroup()
        self.Pokemon_LabMRCamera = CameraGroup()
        self.Pokemon_LabRDCamera = CameraGroup()
        self.Pokemon_LabTRCamera = CameraGroup()
        self.Pokemon_MansionF1Camera = CameraGroup()
        self.Pokemon_MansionF2Camera = CameraGroup()
        self.Pokemon_MansionF3Camera = CameraGroup()
        self.Pokemon_MansionFB1Camera = CameraGroup()
        self.CGymCamera = CameraGroup()
        self.VGymCamera = CameraGroup()
        self.VRoadF1Camera = CameraGroup()
        self.VRoadF2Camera = CameraGroup()
        self.VRoadF3Camera = CameraGroup()
        self.IndigoPlateauEntranceCamera = CameraGroup()
        self.IndigoPlateauE1Camera = CameraGroup()
        self.IndigoPlateauE2Camera = CameraGroup()
        self.IndigoPlateauE3Camera = CameraGroup()
        self.IndigoPlateauE4Camera = CameraGroup()
        self.IndigoPlateauChampionCamera = CameraGroup()
        self.Fame_HallCamera = CameraGroup()
        self.Power_PlantCamera = CameraGroup()
        self.SeaFoam_IslandF1Camera = CameraGroup()
        self.SeaFoam_IslandFB1Camera = CameraGroup()
        self.SeaFoam_IslandFB2Camera = CameraGroup()
        self.SeaFoam_IslandFB3Camera = CameraGroup()
        self.SeaFoam_IslandFB4Camera = CameraGroup()
        self.Cerulean_CaveF1Camera = CameraGroup()
        self.Cerulean_CaveBFCamera = CameraGroup()
        self.Cerulean_CaveF2Camera = CameraGroup()
        self.SSPlayerHouseSpawnpoint = (642,710)
        self.SS_AnneF1RoomsBarriers = []
        self.Silph_CoF1Barriers = []
        self.SS_AnneF2CaptainBarriers = []
        self.SAF1_KitDoor = Transportion
        self.R16House2Barriers = []
        self.LSFIF1_OSpawn = ()
        self.O_LSFIF1Door = Transportion
        self.SilCoF5_SilCoF4Spawn = ()
        self.SilCoF4_SilCoF5Door = Transportion
        self.BattlerOak = TrainerNPC
        self.OakBattle = pygame.Rect
        self.SilCoF2_SilCoF1Spawn = ()
        self.RSFIF1_OSpawn = ()
        self.O_RSFIF1Door = Transportion
        self.SeaFoam_IslandFB1Barriers = []
        self.O_R12HDoor = Transportion
        self.O_CCaveDoor = Transportion
        self.VRoadF22Wall = []
        self.Silph_CoF4Barriers = []
        self.RDGiv = NPC
        self.SFH3F2Barriers = []
        self.CCave_OSpawn = ()
        self.PokeMansionF3Barriers = []
        self.VRoadF21Wall = []
        self.Silph_CoF4InvisableBarrier = []
        self.PP_OSpawn = ()
        self.O_PPDoor = Transportion
        self.ILE_Nurse = NPC
        self.ILEClerk = NPC
        self.ILENurse_desk = pygame.Rect
        self.VRoadF2Boulders = []
        self.ILE_E4Door = Transportion
        self.IndigoLeagueEntranceNPCS = []
        self.VRoadF22Button = Tile
        self.ILE_ODoor = Transportion
        self.MartDesk = pygame.Rect
        self.VRoadF21Button = Tile
        self.ILEPC = pygame.Rect
        self.R12HBarriers = []
        self.O_ILESpawn = ()
        self.Pokemon_LabRDBarriers = []
        self.CCaveA1_A2Spawn = ()
        self.CCaveD1_D2Spawn = ()
        self.Cerulean_CaveF2Wilds = []
        self.CCaveC2_C1Door = Transportion
        self.Cerulean_CaveF2Barriers = []
        self.Cerulean_CaveF2Pickups = []
        self.CCaveB1_B2Spawn = ()
        self.CCaveD2_D1Door = Transportion
        self.CCaveA2_A1Door = Transportion
        self.VRoadF2Pickups = []
        self.RDScientist = NPC
        self.CCaveF1_F2Spawn  = ()
        self.CCaveC1_C2Spawn = ()
        self.CCaveB2_B1Door = Transportion
        self.PostgameNPCS = []
        self.CCaveF2_F1Door = Transportion
        self.VRoadF2HiddenItems = []
        self.CCaveE1_E2Spawn = ()
        self.VRoadF2Barriers = []
        self.CCaveE2_E1Door = Transportion
        self.PokeLabHall_PokeLabTRSpawn = ()
        self.PokeLabTR_PokeLabHallDoor = Transportion
        self.R12GHF2Girl = NPC
        self.O_R12HSpawn = ()
        self.PokeLabTR_PokeLabHallSpawn = ()
        self.PokeLabRD_PokeLabHallDoor = Transportion
        self.PokeLabHall_PokeLabRDSpawn = ()
        self.Pokemon_LabHallReadables = []
        self.CCaveMan = NPC
        self.BPLRivalBattleLine = pygame.Rect
        self.BPLRivalSpot = ()
        self.R12HFisher = NPC
        self.PokeLabRD_PokeLabHallSpawn = ()
        self.PokeLabMR_PokeLabHallSpawn = ()
        self.PokeLabHall_PokeLabMRDoor = Transportion
        self.Pokemon_LabHallBarriers = []
        self.MHMan = NPC
        self.PokeLabHall_PokeLabTRDoor = Transportion
        self.VRoadF3Barriers = []
        self.R12H_ODoor = Transportion
        self.PokeLabHall_PokeLabRDDoor = Transportion
        self.Silph_CoF4Readables = []
        self.VRoadF3Pickups = []
        self.VRoadF3Wall = []
        self.IPE1Wall = []
        self.VRoadF1Trainereyes = []
        self.Lorelei = GymLeaderNPC
        self.O_RSFIF1Spawn = ()
        self.SZA3RHBarriers = []
        self.RSFIF1_ODoor = Transportion
        self.SeaFoam_IslandF1Boulders = []
        self.SeaFoam_IslandFB2Barriers = []
        self.R12GuardHouseF2Barriers = []
        self.LSFIK2_K1Spawn = ()
        self.LSFID2_D1Door = Transportion
        self.LSFID1_D2Spawn = ()
        self.LSFIF1_ODoor = Transportion
        self.LSFIL1_L2Spawn = ()
        self.LSFIL2_L1Door = Transportion
        self.LSFIK1_K2Spawn =()
        self.LSFIE1_E2Spawn =()
        self.LSFIE2_E1Door = Transportion
        self.VRoadF1Trainers = []
        self.LSFIK2_K1Door = Transportion
        self.LSFIK1_K2Door = Transportion
        self.LSFIC1_C2Spawn = ()
        self.LSFIC2_C1Door = Transportion
        self.LSFIC2_C1Spawn = ()
        self.LSFIE1_E2Door = Transportion
        self.SeaFoam_IslandFB1Boulders = []
        self.LSFIC1_C2Door = Transportion
        self.LSFIE2_E1Spawn = ()
        self.LSFIA1_A2Spawn = ()
        self.LSFID2_D1Spawn =()
        self.LSFIB1_B2Spawn = ()
        self.LSFID1_D2Door = Transportion
        self.LSFIB2_B1Door = Transportion
        self.LSFIA2_A1Door = Transportion
        self.LSFIA1_A2Door = Transportion
        self.LSFIL2_L1Spawn = ()
        self.LSFIL1_L2Door = Transportion
        self.LSFIA2_A1Spawn = ()
        self.IndigoPlateauE3Barriers = []
        self.O_LSFIF1Spawn = ()
        self.SeaFoam_IslandF1Barriers = []
        self.LSFIB2_B1Spawn = ()
        self.Cerulean_CaveBFBarriers = []
        self.CCaveG2_G1Door = Transportion
        self.VRoadF3Boulders = []
        self.CCaveG1_G2Spawn = ()
        self.LSFIB1_B2Door = Transportion
        self.Cerulean_CaveBFHiddenItems = []
        self.Cerulean_CaveBFFishingPoint = []
        self.Cerulean_CaveBFWilds = []
        self.Agatha = GymLeaderNPC
        self.Cerulean_CaveBFPickups = []
        self.SeaFoam_IslandFB3Barriers = []
        self.IPE3Wall = []
        self.IndigoPlateauE3_E4Door = Transportion
        self.SeaFoam_IslandFB4Barriers = []
        self.SZA3RHNPCS = []
        self.GhostSpawn = ()
        self.SA3GrassBlocks = []
        self.R15Aide = NPC
        self.O_CE1HDoor = Transportion
        self.R23_PLF1Door = Transportion
        self.SilCoF1_SilCoF2Door = Transportion
        self.IndigoLeagueEntranceBarriers = []
        self.PokeMansionD_DSpawn = ()
        self.IndigoPlateauE4_CDoor = Transportion
        self.Lance = GymLeaderNPC
        self.PokeMansionG1_G2Door = Transportion
        self.Pokemon_MansionF1Pickups = []
        self.IndigoPlateauE4Barriers = []
        self.FinalBattleLine = pygame.Rect
        self.IPCOak = NPC
        self.O_PokeMansionF1Spawn = ()
        self.IndigoPlateauChampionBarriers = []
        self.IPE4Wall = []
        self.PokeMansionG2_G1Spawn = ()
        self.IndigoPlateauE4_CSpawn = ()
        self.DragonSpawn = ()
        self.PokeMansionF1_ODoor = Transportion
        self.VRoadF1Button = Tile
        self.PokeMansionA2_A1Spawn = ()
        self.PokeMansionA1_A2Door = Transportion
        self.SilCoF3_SilCoF4Spawn = ()
        self.PokeMansionF1Barriers = []
        self.R15GH_F2Spawn = ()
        self.VRoadF1Boulders = []
        self.VRoadF1Wall = []
        self.SilCoF4_SilCoF3Door = Transportion
        self.O_SilCoF1Spawn = ()
        self.O_VictoryRoadF2Spawn = ()
        self.F2_R15GHDoor = Transportion
        self.O_ILEDoor = Transportion
        self.R15GuardHouseF2Readables = []
        self.ILE_OSpawn = ()
        self.CIPokeCenterSpawn = ()
        self.O_PokeMansionF1Door = Transportion
        self.R16H1F2_R16H1Door = Transportion
        self.O_CIPokeMartDoor = Transportion
        self.PokeMansionF1_OSpawn = ()
        self.VictoryRoadA2_A1Spawn = ()
        self.VictoryRoadA1_A2Door = Transportion
        self.PokeMansionB2_B1Door = Transportion
        self.PokeMansionF3Switch = pygame.Rect
        self.VRoadF1Barriers = []
        self.PokeMansionF1_F2Spawn = []
        self.PokeMansionC1_C2Spawn = ()
        self.PokeMansionF3Readables = []
        self.Pokemon_MansionF3WallsA = []
        self.PokeMansionF2_F1Door = Transportion
        self.PokeMansionFB1Barriers = []
        self.Pokemon_MansionF3Pickups = []
        self.Bruno = GymLeaderNPC
        self.Pokemon_MansionF3WallsB = []
        self.IndigoPlateauE2_E3Door = Transportion
        self.IPE2Wall = []
        self.RockSpawn = ()
        self.IndigoPlateauE2Barriers = []
        self.PokeMansionF3HiddenItems = []
        self.CIPokeMartSpawn = ()
        self.PokeMansionD_DDoor = Transportion
        self.O_R16H2Door = Transportion
        self.PokeMansionE_EDoor = Transportion
        self.PokeMansionC2_C1Door = Transportion
        self.R15GuardHouseF2Barriers = []
        self.O_CIPokeCenterDoor = Transportion
        self.PokeMansionB1_B2Spawn = ()
        self.R12GuardHouseBarriers = []
        self.SZA3_MZDoor = Transportion
        self.SZMZ_A3Spawn = ()
        self.SZA3_MZSpawn = ()
        self.SZMZ_A3Door = Transportion
        self.O_SMZSpawn = ()
        self.SA1GrassBlocks = []
        self.Pokemon_MansionF1Blocks = []
        self.Pokemon_MansionF3Blocks = []
        self.Pokemon_MansionFB1Blocks = []
        self.Pokemon_MansionF2Blocks = []
        self.R16H2_OSpawn = ()
        self.R16H1_R16H1F2Spawn = ()
        self.O_SFH3F1Door = Transportion
        self.CGymQuestion1 = Question
        self.SFH3F1_OSpawn = ()
        self.O_CGymSpawn = ()
        self.CGym_ODoor = Transportion
        self.SAF1_KSpawn = ()
        self.O_VictoryRoadF1Spawn = ()
        self.VRoadF1Pickups = []
        self.VictoryRoadF1_ODoor = Transportion
        self.CGymBarriers = []
        self.O_R18GHSpawn = ()
        self.CEMF3_CEMF4Spawn = ()
        self.O_VictoryRoadF1Door = Transportion
        self.VictoryRoadF1_OSpawn = ()
        self.TRMan = TraderNPC
        self.PokeMansionF2_F1Spawn = ()
        self.SilCoF10Woman = NPC
        self.PokeMansionA1_A2Spawn = ()
        self.CGym_OSpawn = ()
        self.PokemonTowerF4Tiles = []
        self.CGymReadables = []
        self.O_CGymDoor = Transportion
        self.PokeMansionE_ESpawn = ()
        self.Blaine = GymLeaderNPC
        self.PokeMansionF1_F2Door = Transportion
        self.PokeMansionF2_F1Spawn = ()
        self.PokeMansionB2_B1Spawn = ()
        self.Pokemon_MansionF2Pickups = []
        self.PokeMansionA2_A1Door = Transportion
        self.CGymWall2 = []
        self.CGymWall1 = []
        self.CGymWall3 = []
        self.O_VictoryRoadF2Door = Transportion
        self.VictoryRoadF2_OSpawn = ()
        self.VictoryRoadF2_ODoor = Transportion
        self.VictoryRoadE2_E1Spawn = ()
        self.PCM_O2Spawn = ()
        self.PCM1_O2Door = Transportion
        self.PCM1GScientist = NPC
        self.CGymWall4 = []
        self.O2_PCM1Spawn = ()
        self.CGymWall5 = []
        self.CGymWall6 = []
        self.PCMuseum2Door = Transportion
        self.Pokemon_MansionF2WallsB = []
        self.CGymTrainers = []
        self.PokeMansionF2Readables = []
        self.PokeMansionC2_C1Spawn = ()
        self.PokeMansionC1_C2Door = Transportion
        self.PokeMansionF2Switch = pygame.Rect
        self.CCaveG2_G1Spawn = ()
        self.R15_GHDoor = Transportion
        self.CCaveG1_G2Door = Transportion
        self.Pokemon_MansionF2WallsA = []
        self.Pokemon_LabTRBarriers = []
        self.CCaveE2_E1Spawn = ()
        self.CCaveE1_E2Door = Transportion
        self.Mewtwo = Tile
        self.PokeMansionB1_B2Door = Transportion
        self.CCaveD1_D2Door = Transportion
        self.O_CCaveSpawn =()
        self.CCaveF2_F1Spawn = ()
        self.PokeMansionF2Barriers = []
        self.CCaveF1_F2Door = Transportion
        self.CCaveD2_D1Spawn = ()
        self.CCaveC1_C2Door = Transportion
        self.CCaveB2_B1Spawn = ()
        self.O_PokeLabHallSpawn = ()
        self.PokeLabHall_ODoor = Transportion
        self.CCaveB1_B2Door = Transportion
        self.CCaveA2_A1Spawn= ()
        self.CCaveC2_C1Spawn = ()
        self.CCaveA1_A2Door = Transportion
        self.Cerulean_CaveF1FishingPoint = []
        self.Cerulean_CaveF1Pickups =[]
        self.CCave_ODoor = Transportion
        self.Cerulean_CaveF1HiddenItems =[]
        self.Cerulean_CaveF1Barriers = []
        self.GH_R15Spawn = ()
        self.Cerulean_CaveF1Wilds =[]
        self.GH_FCSpawn = ()
        self.O_R18GHDoor = Transportion
        self.Pokemon_MansionFB1WallsA= []
        self.Pokemon_MansionFB1WallsB = []
        self.FC_GHDoor = Transportion
        self.R18GuardHouseBarriers = []
        self.PokeMansionFB1BSwitch = pygame.Rect
        self.R18GH_OSpawn = ()
        self.PokeMansionFB1Readables = []
        self.Pokemon_MansionFB1Pickups = []
        self.E4LanceBattleLine = pygame.Rect
        self.PokeMansionFB1ASwitch = pygame.Rect
        self.PokemonTowerF5Tiles = []
        self.PokeMansionFB1HiddenItems = []
        self.R18GH_ODoor = Transportion
        self.Pokemon_LabMRBarriers = []
        self.PokemonTowerF6Tiles = []
        self.PokeMansionG1_G2Spawn = ()
        self.PokeMansionG2_G1Door = Transportion
        self.PokeLabHall_PokeLabMRSpawn = ()
        self.Silph_CoF2Barriers = []
        self.PokeLabMR_PokeLabHallDoor = Transportion
        self.SilCoF1_SilCoF2Spawn = ()
        self.Silph_CoF2Readables = []
        self.SilCoF3_SilCoF2Spawn =()
        self.SilCoF2_SilCoF3Door = Transportion
        self.SilCoF2_SilCoF1Door = Transportion
        self.O_SFH2Spawn = ()
        self.SFH2_ODoor = Transportion
        self.SFH2Barriers = []
        self.Silph_CoF2InvisableBarrier = []
        self.O_FCWHSpawn = ()
        self.F2_R15GHSpawn = ()
        self.R15GHDesk = pygame.Rect
        self.R15GH_F2Door = Transportion
        self.R15_GHSpawn = ()
        self.GH_R15Door = Transportion
        self.R15GuardHouseBarriers = []
        self.PokeLabHall_OSpawn = ()
        self.FC_GHSpawn = ()
        self.O_PokeLabHallDoor = Transportion
        self.GH_FCDoor = Transportion
        self.SFH2Readables = []
        self.SilCoF2Woman = NPC
        self.SFH2NPCS = []
        self.SilCoF1_ODoor = Transportion
        self.CEMF4_CEMF3Door = Transportion
        self.FCWH_OSpawn = ()
        self.O_FCWHDoor = Transportion
        self.BCEMF3_BCEMF4Spawn = ()
        self.FCWHBoulders = []
        self.SilphCoGioLine = pygame.Rect
        self.R12GuardHouse_ODoor = Transportion
        self.O_R12GuardHouseSpawn = ()
        self.FCWHBarriers = []
        self.R12GuardHouse_F2Spawn = ()
        self.R12GuardHouse_F2Door = Transportion
        self.O2_R12GuardHouseSpawn = ()
        self.F2_R12GuardHouseSpawn = ()
        self.R12GHDesk = pygame.Rect
        self.F2_R12GuardHouseDoor = Transportion
        self.R12GuardHouse_O2Door = Transportion
        self.SilCoGiovanni = TrainerNPC
        self.R12GHGuard = NPC
        self.O2_R12GuardHouseDoor = Transportion
        self.R12H_OSpawn = ()
        self.R12GuardHouse_OSpawn = ()
        self.O_R12GuardHouseDoor = Transportion
        self.SilCoGiovanni = TrainerNPC
        self.R12GuardHouse_O2Spawn = ()
        self.O2_InterR5Door = Transportion
        self.Pokemon_TowerF3Pickups = []
        self.FCWHNPCS = []
        self.SMZReadables = []
        self.F3Desk = pygame.Rect
        self.InterR5_O2Spawn = ()
        self.O2_InterR6Door = Transportion
        self.InterR6_O2Spawn = ()
        self.FCWH_ODoor = Transportion
        self.CEStoreF4Barriers = []
        self.PokeTowerF4_PokeTowerF3Spawn = ()
        self.SA1Readables = []
        self.SMZBarriers = []
        self.SMZ_ODoor = Transportion
        self.SilCoF2_SilCoF3Spawn = ()
        self.SilCoF3_SilCoF2Door = Transportion
        self.LaprasMan = NPC
        self.Pokemon_MansionF1WallsA = []
        self.Pokemon_MansionF1WallsB = []
        self.PokeMansionF1Switch = pygame.Rect
        self.PokeTowerF4Barriers = []
        self.PokeMansionExitDoor = Transportion
        self.PokeMansionF1HiddenItems = []
        self.Silph_CoF3InvisableBarrier = []
        self.O_SFH2Door = Transportion
        self.SFH2_OSpawn = ()
        self.Silph_CoF3Readables = []
        self.PokeTowerF3_PokeTowerF4Door = Transportion
        self.Silph_CoF3Barriers = []
        self.SilCoF4_SilCoF3Spawn = ()
        self.SilCoF3_SilCoF4Door = Transportion
        self.PokeTowerF2_PokeTowerF3Spawn = ()
        self.CEStoreF3Readables = []
        self.SA1FishingPoint = []
        self.PokeTowerF3_PokeTowerF2Door = Transportion
        self.O2_R18GHSpawn = ()
        self.R18GHF2_R18GHSpawn = ()
        self.R18GuardHouseF2Readables = []
        self.SMZFishingPoint = []
        self.R18GH_O2Door = Transportion
        self.SZA1_MZSpawn = ()
        self.R18GH_R18GHF2Door = Transportion
        self.SZMZ_A1Door = Transportion
        self.Silph_CoF7Barriers = []
        self.R18GuardHouseF2NPCS = []
        self.O_FPokeCenterDoor = Transportion
        self.FPokeMart_OSpawn = ()
        self.SZA2_MZSpawn = ()
        self.SZMZ_A2Door = Transportion
        self.R18GuardHouseF2Barriers = []
        self.H1_SZA2Spawn = ()
        self.SZA2_H1Door = Transportion
        self.O_FPokeMartDoor = Transportion
        self.O_SilCoF1Door = Transportion
        self.SilCoF1_OSpawn = ()
        self.SZMZ_A2Spawn = ()
        self.RH_SZA3Spawn = ()
        self.SZA3_RHDoor = Transportion
        self.SZA3_A2Spawn2 = ()
        self.SilCoF10_SilCoF9Spawn = ()
        self.SilCoF9_SilCoF10Door = Transportion
        self.SZA2_A3Door2 = Transportion
        self.SA3Barriers = []
        self.SZA2_A3Spawn2 = ()
        self.SZA3_A2Door2 = Transportion
        self.SA3Readables = []
        self.SZA2_MZDoor = Transportion
        self.SilCoF9_SilCoF8Spawn = ()
        self.SilCoF8_SilCoF9Door = Transportion
        self.FPokeCenter_OSpawn = ()
        self.SFH3CopyCat = NPC
        self.SilCoF8_SilCoF9Spawn = ()
        self.SilCoF9_SilCoF8Door = Transportion
        self.SZA2RHNPCS = []
        self.SZA2_A3Spawn = ()
        self.SZA3_A2Door = Transportion
        self.SFH3F2Readables = []
        self.Silph_CoF8Barriers = []
        self.Silph_CoF9Readables = []
        self.Silph_CoF9InvisableBarrier = []
        self.O_SFtoR8Door = Transportion
        self.Silph_CoF9Barriers = []
        self.O_SFtoR7Door = Transportion
        self.CESOldMan = NPC
        self.SZA3_A2Spawn = ()
        self.SZA2_A3Door = Transportion
        self.SFtoR8_OSpawn = ()
        self.Silph_CoF8Readables = []
        self.SFtoR7_OSpawn = ()
        self.Silph_CoF8Trainers = []
        self.Silph_CoF8Trainereyes = []
        self.Silph_CoF8InvisableBarrier = []
        self.R18GH_R18GHF2Spawn = ()
        self.SilCoF7_SilCoF8Spawn = ()
        self.IndigoPlateauE1_E2Door = Transportion
        self.SilCoF8_SilCoF7Door = Transportion
        self.SZA2RHBarriers =[]
        self.R18GHF2_R18GHDoor = Transportion
        self.SilCoP2_SilCoP1Spawn = ()
        self.CounterMan = NPC
        self.IceSpawn = ()
        self.IndigoPlateauE1Barriers = []
        self.SilCoP1_SilCoP2Door = Transportion
        self.SilCoE_SilCoF8Spawn = ()
        self.SilCoF8_SilCoEDoor = Transportion
        self.O2_R18GHDoor = Transportion
        self.Silph_CoF7NPCS = []
        self.SilCoO1_SilCoO2Spawn = ()
        self.SilCoO2_SilCoO1Door = Transportion
        self.R18GH_O2Spawn = ()
        self.O_PokeTowerF1Door = Transportion
        self.O_SFGymDoor = Transportion
        self.SFGym_OSpawn = ()
        self.O_SFGymSpawn = ()
        self.SilCoF6_SilCoF7Spawn = ()
        self.SilCoF7_SilCoF6Door = Transportion
        self.Sabrina = GymLeaderNPC
        self.SFGymBarriers = []
        self.SFGymReadables = []
        self.PokeTowerF1_OSpawn = ()
        self.SFGym_ODoor = Transportion
        self.SFGymNPCS = []
        self.SFGymTrainereyes = []
        self.SFGymTrainers = []
        self.CEStoreF3NPCS = []
        self.Safari_ZoneA1Pickups = []
        self.Safari_ZoneA3Pickups = []
        self.Safari_ZoneA2Pickups = []
        self.CEStoreF3_CEStoreF4Door = Transportion
        self.CEStoreF4_CEStoreF3Spawn = ()
        self.CEStoreF3_CEStoreF2Door = Transportion
        self.Safari_ZoneMZPickups = []
        self.CEStoreF3_ElevatorDoor = Transportion
        self.SA2Barriers = []
        self.Silph_CoF7Readables = []
        self.Silph_CoF7InvisableBarrier = []
        self.CEStoreF2_CEStoreF3Spawn = ()
        self.SilCoF8_SilCoF7Spawn = ()
        self.SilCoF7_SilCoF8Door = Transportion
        self.SA2FishingPoint = []
        self.SA2GrassBlocks = []
        self.SA2Readables = []
        self.Elevator_CEStoreF3Spawn = ()
        self.BCEMF4_BCEMF3Door = Transportion
        self.RocketBaseF1_GCSpawn = ()
        self.GCLever = pygame.Rect
        self.GC_RocketBaseF1Door = Transportion
        self.CEMF4Barriers = []
        self.SA1Barriers = []
        self.RocketBaseF2Barriers = []
        self.Silph_CoF10InvisableBarrier = []
        self.CE1H_OSpawn = ()
        self.Silph_CoF10Barriers = []
        self.SilCoF11_SilCoF10Spawn = ()
        self.SilCoF10_SilCoF11Door = Transportion
        self.SilCoF9_SilCoF10Spawn = ()
        self.SilCoF10_SilCoF9Door = Transportion
        self.Silph_CoF10Readables = []
        self.RocketBaseF1_GCDoor = Transportion
        self.O_CE1HSpawn = ()
        self.RocketBaseF1Barriers = []
        self.GC_RocketBaseF1Spawn = ()
        self.PokeTowerF5_PokeTowerF4Spawn = ()
        self.PokeTowerF4_PokeTowerF5Door = Transportion
        self.PokeTowerF5Barriers = []
        self.Game_CornerReadables = []
        self.CEMF3Barriers = []
        self.PokeTowerF3_PokeTowerF4Spawn = ()
        self.PokeTowerF4_PokeTowerF3Door = Transportion
        self.CEMF4_CEMF3Spawn = ()
        self.PokeTowerF6_PokeTowerF5Spawn = ()
        self.PokeTowerF5_PokeTowerF6Door = Transportion
        self.Pokemon_TowerF4Pickups = []
        self.CEMF3_CEMF4Door = Transportion
        self.BCEMF4_BCEMF3Spawn = ()
        self.R16House2NPCS = []
        self.BCEMF3_BCEMF4Door = Transportion
        self.MovingRocketBaseF3Blocks = []
        self.Silph_CoF11Barriers = []
        self.Silph_CoF11Readables = []
        self.Silph_CoF11InvisableBarrier = []
        self.RocketBaseF1Doors = Readables
        self.SilCoF10_SilCoF11Spawn = ()
        self.SilCoF11_SilCoF10Door = Transportion
        self.O_R16H2Spawn = ()
        self.R16H2_ODoor = Transportion
        self.RocketBaseF1Readables = []
        self.RocketBaseF2Doors = Readables
        self.Bike_OnlyZone = pygame.Rect
        self.PokeTowerF4_PokeTowerF5Spawn = ()
        self.PokeTowerF5_PokeTowerF4Door = Transportion
        self.RocketBaseElevatorBarriers = []
        self.RocketBaseF4_RocketBaseF3Spawn = ()
        self.RocketBaseF3_RocketBaseF4Door = Transportion
        self.RocketBaseF3_RocketBaseF4Spawn = ()
        self.RocketBaseF4Barriers = []
        self.PokeTowerF7Trainereyes = []
        self.R16GuardHouseF2Readables =[]
        self.PokeTowerF7Trainers = []
        self.Pokemon_TowerF5Pickups = []
        self.RocketBaseF2Readables = []
        self.R16GuardHouseF2NPCS = []
        self.SHGuy = NPC
        self.SH_SZA3Spawn= ()
        self.SZA3_SHDoor = Transportion
        self.SZA3_SHSpawn = ()
        self.SH_SZA3Door = Transportion
        self.SZA3SHBarriers = []
        self.Pokemon_TowerF1NPCS = []
        self.PokeTowerF7_PokeTowerF6Spawn = ()
        self.PokemonTowerF7Tiles = []
        self.O_FCGymSpawn = ()
        self.FCGym_ODoor = Transportion
        self.FCGymBarriers = []
        self.FCGymReadables = []
        self.FCGymTrainereyes = []
        self.FCGymNPCS = []
        self.FCGymTrainers = []
        self.Koga = GymLeaderNPC
        self.PokeTowerF3Trainers = []
        self.PokeTowerF3Trainereyes = []
        self.R16GuardHouseF2Barriers = []
        self.Pokemon_TowerF2NPCS = []
        self.Silph_CoElevatorBarriers = []
        self.SilCo_SilCoESpawn = ()
        self.SilCoElevatorMenu = pygame.Rect
        self.PokeTowerF6_PokeTowerF7Door = Transportion
        self.Pokemon_TowerF6Pickups = []
        self.PokeTowerF6_PokeTowerF5Door = Transportion
        self.PokeTowerF5_PokeTowerF6Spawn = ()
        self.RocketBaseF1Trainers = []
        self.PokeTowerF6Barriers = []
        self.RocketBaseF2Trainers = []
        self.PokeTowerF7Barriers= []
        self.PokeTowerF6_PokeTowerF7Spawn = ()
        self.PokeTowerF7_PokeTowerF6Door = Transportion
        self.PokeTowerF2Barriers = []
        self.PokeTowerF1_PokeTowerF2Spawn = ()
        self.O_FCGymDoor = Transportion
        self.FCGym_OSpawn = ()
        self.RocketBaseF3Trainers = []
        self.RocketBaseF4Trainers = []
        self.Bike_OnlyZone2 = pygame.Rect
        self.RocketBaseF1Trainereyes = []
        self.PokeTowerF2_PokeTowerF1Door = Transportion
        self.RocketBaseF2Trainereyes = []
        self.RocketBaseF3Trainereyes = []
        self.RocketBaseF4Trainereyes = []
        self.CEMF2_CEMF3Spawn = ()
        self.O_FCH1Spawn = ()
        self.FCH1_ODoor = Transportion
        self.FCH1Barriers = []
        self.PokemonTowerF3Tiles = []
        self.RocketBaseF3_RocketBaseF2Spawn = ()
        self.RocketBaseF2_RocketBaseF3Door = Transportion
        self.CEMF3_CEMF2Door = Transportion
        self.RocketBaseF4_RocketBaseF3Door = Transportion
        self.RocketBaseF2_RocketBaseF3Spawn = ()
        self.RocketBaseF3Barriers = []
        self.F2LeftDesk = pygame.Rect
        self.H1_SZA1Spawn = ()
        self.SZA1RHNPCS = []
        self.SZA1_H1Door = Transportion
        self.RocketBaseF3_RocketBaseF2Door = Transportion
        self.SZA1RHBarriers = []
        self.CEStoreF2_CEStoreF3Door = Transportion
        self.O_SZESpawn = ()
        self.SZEBarriers = []
        self.SZENPCS = []
        self.SZE_ODoor = Transportion
        self.Rocket_HideoutF3Pickups = []
        self.Rocket_HideoutF3HiddenItems = []
        self.Rocket_HideoutF4Pickups = []
        self.Rocket_HideoutF4HiddenItems = []
        self.CEStoreF3_CEStoreF2Spawn = ()
        self.CEStoreF2_ElevatorDoor = Transportion
        self.Silph_CoF5Barriers = []
        self.SilCoF5_SilCoF6Spawn = ()
        self.SilCoF6_SilCoF5Door = Transportion
        self.SilCoF4_SilCoF5Spawn = ()
        self.SilCoF5_SilCoF4Door = Transportion
        self.SilCoF7_SilCoF6Spawn = ()
        self.SilCoF6_SilCoF7Door = Transportion
        self.Silph_CoF6Barriers = []
        self.SilCoF6_SilCoF5Spawn = ()
        self.SilCoF5_SilCoF6Door = Transportion
        self.F2RightDesk = pygame.Rect
        self.Silph_CoF6Readables = []
        self.Silph_CoF6InvisableBarrier = []
        self.RocketBaseF2_2RocketBaseF1Door = Transportion
        self.Silph_CoF5InvisableBarrier = []
        self.Silph_CoF5Readables = []
        self.RocketBaseF1_2RocketBaseF2Spawn = ()
        self.Silph_CoF2Trainereyes = []
        self.Elevator_CEStoreF2Spawn = ()
        self.Silph_CoF2Trainers = []
        self.RocketBaseF2_2RocketBaseF1Spawn = ()
        self.CEStoreF2NPCS = []
        self.SilCoE_SilCoF1Spawn = ()
        self.RBaseElevator_Menu = pygame.Rect
        self.SilCoE_SilCoF2Spawn = ()
        self.SilCoF2_SilCoEDoor = Transportion
        self.CEStoreF3Barriers = []
        self.SilCoF1_SilCoEDoor = Transportion
        self.RocketBaseF1_2RocketBaseF2Door = Transportion
        self.CEStoreF2Readables = []
        self.BCEMF2_BCEMF3Spawn = ()
        self.Elevator_CEStoreF1Spawn = ()
        self.CEStoreF2_CEStoreF1Door = Transportion
        self.CEStoreF1_CEStoreF2Spawn = ()
        self.BCEMF3_BCEMF2Door = Transportion
        self.SZA2_A1Spawn = ()
        self.SZA1_A2Spawn = ()
        self.SZA2_A1Door = Transportion
        self.CEStoreF2_CEStoreF1Spawn = ()
        self.CEStoreF1_CEStoreF2Door = Transportion
        self.SZA1_A2Door = Transportion
        self.CESleepingSnorlax = []
        self.LTVHMr_Fuji = NPC
        self.O_CEStoreF1RightDoor = Transportion
        self.PokeTowerBattleLine = pygame.Rect
        self.CE1HNPCS = []
        self.CEStoreF1NPCS = []
        self.PokeTowerRival = NPC
        self.CEStoreRooftopBarriers = []
        self.CEStoreF2Barriers = []
        self.Elevator_RocketBaseF4Spawn = ()
        self.RocketBaseF4_ElevatorDoor = Transportion
        self.CEStoreF1_ElevatorDoor = Transportion
        self.RocketBaseF1_ElevatorDoor = Transportion
        self.F5RightDesk = pygame.Rect
        self.RocketBaseF2_ElevatorDoor = Transportion
        self.SZMAH1Barriers = []
        self.SZMAH1NPCS = []
        self.H1_SZMASpawn = ()
        self.SZMA_H1Spawn = ()
        self.Elevator_RocketBaseF2Spawn = ()
        self.H1_SZMADoor = Transportion
        self.Elevator_RocketBaseF1Spawn = ()
        self.SZMA_H1Door = Transportion
        self.F5LeftDesk = pygame.Rect
        self.CEStoreF1Barriers = []
        self.RocketBase_ElevatorSpawn = ()
        self.CEStoreF5NPCS = []
        self.CEStoreF1Readables = []
        self.CEStoreF5_ElevatorDoor = Transportion
        self.CEStoreF5Readables = []
        self.Elevator_CEStoreF5Spawn = ()
        self.F1Desk = pygame.Rect
        self.CEStoreF5_CEStoreF4Door = Transportion
        self.CEStoreF4_CEStoreF5Spawn = ()
        self.CEStoreF5_CEStoreRoofDoor = Transportion
        self.CEStoreRoof_CEStoreF5Spawn = ()
        self.O_CEStoreF1RightSpawn = ()
        self.CEStoreF1Right_ODoor = Transportion
        self.CEStoreF4Readables = []
        self.F4Desk = pygame.Rect
        self.CEStoreF4_CEStoreF3Door = Transportion
        self.CEStoreF3_CEStoreF4Spawn = ()
        self.CEStoreF4NPCS = []
        self.Elevator_Menu = pygame.Rect
        self.CEStoreF4_CEStoreF5Door = Transportion
        self.CEStoreF5_CEStoreF4Spawn = ()
        self.RooftopVendingMachines = []
        self.CEStoreF4_ElevatorDoor = Transportion
        self.CEStoreRooftopNPCS = []
        self.Elevator_CEStoreF4Spawn = ()
        self.CEStoreRooftopReadables = []
        self.O_CEStoreF1LeftSpawn = ()
        self.CEStoreRoof_CEStoreF5Door = Transportion
        self.MovingRocketBaseF2Blocks = []
        self.CEStoreF5_CEStoreRoofSpawn = ()
        self.CEStoreF1Left_ODoor = Transportion
        self.O_CEStoreF1LeftDoor = Transportion
        self.CEStoreF1Left_OSpawn = ()
        self.CeladonGymTrainers = []
        self.CEMF2_CEMF1Spawn = ()
        self.BCEMF1_ODoor = Transportion
        self.O_BCEMF1Spawn = ()
        self.CE1H_ODoor = Transportion
        self.CEMF4HouseBarriers = []
        self.SMZGrassBlocks = []
        self.BCEMF2_BCEMF1Spawn = ()
        self.BCEMF4H_BCEMF4Spawn = ()
        self.BCEMF4_BCEMF4HSpawn = ()
        self.Erika = GymLeaderNPC
        self.BCEMF4H_BCEMF4Door = Transportion
        self.CEMF4HNPCS = []
        self.CeladonGymTrainereyes = []
        self.F4Eevee = Tile
        self.BCEMF4_BCEMF4HDoor = Transportion
        self.BCEMF1_BCEMF2Door = Transportion
        self.CEMF2Barriers = []
        self.O_BCEMF1Door = Transportion
        self.BCEMF1_OSpawn = ()
        self.O_CEMF1Spawn = ()
        self.CEMF1_ODoor = Transportion
        self.CEMF2_CEMF1Spawn = ()
        self.CEMF1_CEMF2Door = Transportion
        self.CEMF1Barriers = []
        self.CEMF1NPCS = []
        self.O_CE2HSpawn  = ()
        self.CE2HBarriers = []
        self.CE2H_ODoor = Transportion
        self.CE2HNPCS = []
        self.CE1HBarriers = []
        self.DiglettCaveBarriers = []
        self.DCE_DCDoor = Transportion
        self.DCE_DCSpawn = ()
        self.DC_DCESpawn = ()
        self.DC_DCEDoor = Transportion
        self.Kit_SAF1Door = Transportion
        self.SSShip = Tile
        self.SS_AnneF1KitchenBarriers = []
        self.SS_AnneF0RoomsBarriers = []
        self.SS_AnneF2RoomsBarriers = []
        self.VFHiddenItems = []
        self.DC_2DCEDoor = Transportion
        self.RTF1_ExitSpawn = ()
        self.Exit_RTF1Door = Transportion
        self.InterExit_ODoor = Transportion
        self.O_CE2HDoor = Transportion
        self.UnderGWETunnel_UnderGWEDoor = Transportion
        self.UnderGWE_UnderGWETunnelSpawn = ()
        self.InterR6_OSpawn = ()
        self.FCH3_ODoor = Transportion
        self.FCH3_O2Door = Transportion
        self.MtM3HiddenItems = []
        self.O2_FCH3Spawn = ()
        self.O_FCH3Spawn = ()
        self.FCH3Barriers = []
        self.FCH3NPCS = []
        self.O_InterExitSpawn = ()
        self.R22NPCS = []
        self.R22HAide = NPC
        self.OverworldHiddenItems = []
        self.KitchenHiddenItems = []
        self.PO_R22HSpawn = ()
        self.CE2H_OSpawn = ()
        self.R22H_PODoor = Transportion
        self.R22H_VODoor = Transportion
        self.R11H_R12Door = Transportion
        self.PO_R22HDoor = Transportion
        self.R11H_R12Spawn = ()
        self.R22H_POSpawn = ()
        self.R111HNPCS = []
        self.WETunnel_UnderGESpawn = ()
        self.R12_R11HSpawn = ()
        self.Rock_TunnelF2Barriers = []
        self.Underground_EEntranceNPCS = []
        self.UnderWEGE_ODoor = Transportion
        self.UnderGE_WETunnelDoor = Transportion
        self.Rock_TunnelF2Trainers = []
        self.O_UnderWEGESpawn = ()
        self.Underground_EEntranceBarriers = []
        self.O_GCSpawn = ()
        self.GC_ODoor = Transportion
        self.Game_CornerBarriers = []
        self.R11HDesk = pygame.Rect
        self.Game_CornerTradeDesk = pygame.Rect
        self.Game_CornerNPCS = []
        self.Game_CornerWorkerDesk = pygame.Rect
        self.Game_CornerTrader = NPC
        self.O_PrizeBoothDoor = Transportion
        self.PrizeBooth_OSpawn = ()
        self.R11HBarriers = []
        self.Game_CornerReadables = []
        self.R11H_VCODoor = Transportion
        self.SaffronEEntranceBarriers = []
        self.R22HBarriers = []
        self.Prize_BoothBarriers = []
        self.O_CERestourantSpawn = ()
        self.CERestourant_ODoor = Transportion
        self.MaidDesk = pygame.Rect
        self.ChefDesk = pygame.Rect
        self.O_PrizeBoothSpawn = ()
        self.CERestourantNPCS = []
        self.CERestourantBarriers = []
        self.PrizeBooth_ODoor = Transportion
        self.CE2HDesk = pygame.Rect
        self.Prize_BoothNPCS = []
        self.Booth1 = pygame.Rect
        self.Booth2 = pygame.Rect
        self.Booth3 = pygame.Rect
        self.O_CERestourantDoor = Transportion
        self.CERestourant_OSpawn = ()
        self.VO_R22HDoor = Transportion
        self.R22H_VOSpawn = ()
        self.VO_R22HSpawn = ()
        self.R11HF2Readables = []
        self.O_InterR6Door = Transportion
        self.SAF0RoomsHiddenItems = []
        self.O_R8toSFDoor = Transportion
        self.UnderGE_UnderGWETunnelSpawn = ()
        self.UnderGWETunnel_UnderGEDoor = Transportion
        self.R8toSF_OSpawn = ()
        self.DCExit_DCSpawn = ()
        self.SS_AnneF1KitchenNPCS = []
        self.Underground_WETunnelBarriers = []
        self.R10_PCDoor = Transportion
        self.PC_R10Spawn = ()
        self.R11H_R11HF2Door = Transportion
        self.R11H_R11HF2Spawn = ()
        self.R11HF2_R11HDoor = Transportion
        self.R11HAide = NPC
        self.R112NPCS = []
        self.DiglettCaveExitNPCS = []
        self.EWGuardBoundry = pygame.Rect
        self.O_DCExitDoor = Transportion
        self.SaffronEEntrance_ODoor = Transportion
        self.O_SaffronEEntranceSpawn = ()
        self.DCExit_OSpawn = ()
        self.UGEWEntrance_OSpawn = ()
        self.Kit_SAF1Spawn = ()
        self.R11HF2Barriers = []
        self.O_UGEWEntranceDoor = Transportion
        self.VCSleepingSnorlax = []
        self.PlayerDHouseSpawnpoint = ()
        self.O_CeruleanGymSpawn = ()
        self.R11HF2_R11HSpawn = ()
        self.BetweenR5_SCBarriers = []
        self.R21HBarriers = []
        self.R21H_OSpawn = ()
        self.O_R21HDoor= Transportion
        self.R11H_VCOSpawn = ()
        self.PlayerRoomReadables = []
        self.O_R21HSpawn = ()
        self.R21NPCS = []
        self.LT1HBarriers = []
        self.O_LTHSpawn = ()
        self.LTH_ODoor = Transportion
        self.LT1HNPCS = []
        self.LTH1_OSpawn = ()
        self.O_LTH1Door = Transportion
        self.GymGiovanni = GymLeaderNPC
        self.LTH2_OSpawn = ()
        self.VGymD1MoverSpawn = ()
        self.VGymD1Mover = Transportion
        self.VGymD2MoverSpawn = ()
        self.VGymD2Mover = Transportion
        self.VGymD3MoverSpawn = ()
        self.VGymD3Mover = Transportion
        self.O_LTH2Door = Transportion
        self.R21H_ODoor = Transportion
        self.O_VCH3Door = Transportion
        self.VCH3_OSpawn = ()
        self.VCH3NPCS = []
        self.PlayerRoomInteracts = []
        self.VCH3Readables = []
        self.InterEnterance_ODoor = Transportion
        self.R1_SAF0Door = Transportion
        self.SAF2_HWSpawn = ()
        self.RTF1_ASpawn = ()
        self.A_RTF1Door = Transportion
        self.RTF1_BSpawn = ()
        self.B_RTF1Door = Transportion
        self.RTF1_CSpawn = ()
        self.C_RTF1Door = Transportion
        self.RTF1_DSpawn = ()
        self.D_RTF1Door = Transportion
        self.SAF2_SAF1Door = Transportion
        self.OverworldFishingPoint = []
        self.SSCaptain = NPC
        self.SS_AnneF3HallWayBarriers = []
        self.SS_AnneF3Trainereyes = []
        self.SAF2_CCDoor = Transportion
        self.SAF3_HWDoor = Transportion
        self.SAF2_CCSpawn = ()
        self.CC_SAF2Door = Transportion
        self.VGymR1MoverSpawn = ()
        self.VGymR1Mover = Transportion
        self.VGymR2MoverSpawn = ()
        self.VGymR2Mover = Transportion
        self.VGymR3MoverSpawn = ()
        self.VGymR3Mover = Transportion
        self.SaffronEWEntranceNPCS = []
        self.SS_AnneF3NPCs = []
        self.ThirdGymTrashcans = []
        self.CC_SAF2Spawn = ()
        self.R2_SAF2Spawn = ()
        self.SS_AnneF2RoomsPickups = []
        self.SAF2_R2Door = Transportion
        self.SAF2_R2Spawn = ()
        self.VermilionGymTrainereyes = []
        self.LT2HBarriers = []
        self.SS_AnneF2NPCS = []
        self.VermilionGymCNPCS = []
        self.VermilionGymTrainers = []
        self.CGymQuestion2 = Question
        self.CGymQuestion5 = Question
        self.CGymQuestion4 = Question
        self.SS_AnneF2RoomsTrainereyes = []
        self.CGymQuestion3 = Question
        self.CGymQuestion6 = Question
        self.VGymL1MoverSpawn = ()
        self.SS_AnneF2RoomsTrainers = []
        self.VCO_R11HSpawn = () 
        self.VGymU1MoverSpawn = ()
        self.VGymU1Mover = Transportion
        self.VGymU2MoverSpawn = ()
        self.VGymU2Mover = Transportion
        self.VGymU3MoverSpawn = ()
        self.VGymU3Mover = Transportion
        self.VGymL2MoverSpawn = ()
        self.VGymL2Mover = Transportion
        self.VGymL3MoverSpawn = ()
        self.VGymL3Mover = Transportion
        self.VCO_R11HDoor = Transportion
        self.R12_R11HDoor = Transportion
        self.VGymL1Mover = Transportion
        self.SS_AnneF2RoomsNPCs = []
        self.R2_SAF2Door = Transportion
        self.O_VCDoor = Transportion
        self.VC_OSpawn = ()
        self.O_VCSpawn = ()
        self.VC_ODoor = Transportion
        self.VermilionGymReadables = []
        self.VermilionGymBarriers = []
        self.SS_AnneF3Trainers = []
        self.HW_SAF3Spawn = ()
        self.SAF2_R6Spawn = ()
        self.R5_SAF2Door = Transportion
        self.PLF1_R23Spawn = ()
        self.DiglettCaveEntranceNPCS = []
        self.R23BadgeCheck1 = pygame.Rect
        self.R23BadgeCheck2 = pygame.Rect
        self.R23BadgeCheck3 = pygame.Rect
        self.R23BadgeCheck4 = pygame.Rect
        self.R23BadgeCheck5 = pygame.Rect
        self.R23BadgeCheck6 = pygame.Rect
        self.R23BadgeCheck7 = pygame.Rect
        self.R6_SAF2Door = Transportion
        self.PLF1_R23Door = Transportion
        self.R23_PLF1Spawn = ()
        self.O_FCH3Door = Transportion
        self.DCE_R11Door = Transportion
        self.FCH3_OSpawn = ()
        self.DiglettCaveEntranceBarriers = []
        self.R11_DCEDoor = Transportion
        self.O2_FCH3Door = Transportion
        self.DCE_R11Spawn = ()
        self.FCH3_O2Spawn = ()
        self.R11_DCESpawn = ()
        self.SAF2_R6Door = Transportion
        self.R6_SAF2Spawn = ()
        self.SAF2_R3Door = Transportion
        self.SAF2_R5Spawn = ()
        self.SAF2_R5Door = Transportion
        self.R5_SAF2Spawn = ()
        self.R4_SAF2Door = Transportion
        self.R4_SAF2Spawn = ()
        self.SAF2_R4Spawn = ()
        self.SAF2_R4Door = Transportion
        self.R3_SAF2Spawn = ()
        self.SAF2_R3Spawn = ()
        self.R3_SAF2Door = Transportion
        self.SS_AnneF3Barriers = []
        self.SAF2_R1Door = Transportion
        self.R1_SAF2Door = Transportion
        self.R1_SAF2Spawn = ()
        self.SAF2_R1Spawn = ()
        self.HW_SAF2Door = Transportion
        self.VCDoors = Readables
        self.SSBattleSpot = ()
        self.R1_SAF0Spawn = ()
        self.SSBattleLine = pygame.Rect
        self.R1_SAF1Door = Transportion
        self.SAF1_R1Spawn = ()
        self.O_InterR5Door = Transportion
        self.SAF2_SAF1Spawn = ()
        self.SAF1_SAF2Door = Transportion
        self.SAF2_SAF1Door = Transportion
        self.SS_AnneF2Barriers = []
        self.SAF1_SAF2Spawn = ()
        self.SAF2_HWDoor = Transportion
        self.O_InterEnteranceSpawn = ()
        self.HW_SAF2Spawn = ()
        self.PFC_OSpawn = ()
        self.O_PFCDoor = Transportion
        self.VRoadF2Blocks = []
        self.VRoadF1Blocks = []
        self.PokemonFanClubNPCS = []
        self.Moltres = Tile
        self.VRoadF3Blocks = []
        self.SAF1_SAF0Spawn = ()
        self.VCH3Barriers = []
        self.SAF0_SAF1Spawn = ()
        self.PFCChairman = NPC
        self.SAF1_SAF0Door = Transportion
        self.SS_AnneF0Barriers = []
        self.PokemonFanClubBarriers = []
        self.O_PFCSpawn = ()
        self.PFC_ODoor = Transportion
        self.InterEnterance_OSpawn = ()
        self.O_BillSpawn = ()
        self.UndergroundEntranceNPCS = []
        self.UndergroundNSTunnelBarriers = []
        self.SS_AnneF1RoomsNPCs = []
        self.BetweenR5_SCNPCS = []
        self.Bill_ODoor = Transportion
        self.UnderGNSTunnel_UnderGSEDoor = Transportion
        self.VCH1Barriers = []
        self.SS_AnneF1RoomsTrainereyes = []
        self.VCH1_ODoor = Transportion
        self.VCH1NPCS = []
        self.O_R16H1Spawn4 = ()
        self.R16H1_ODoor4 = Transportion
        self.O_R16H1Spawn = ()
        self.O_R16H1Door4 = Transportion
        self.R16H1_OSpawn4 = ()
        self.R16H1_ODoor = Transportion
        self.BikeLine = pygame.Rect
        self.R16H1_R16H1F2Door = Transportion
        self.R16H1_OSpawn2 = ()
        self.R16H1F2_R16H1Spawn = ()
        self.R16GuardHouseNPCS = []
        self.O_R16H1Door2 = Transportion
        self.O_R16H1Spawn2 = ()
        self.R16H1_ODoor2 = Transportion
        self.VCH1_OSpawn = ()
        self.O_R16H1Door3 = Transportion
        self.R16H1_OSpawn = ()
        self.O_R16H1Door = Transportion
        self.R16H1_OSpawn3 = ()
        self.O_R16H1Door3 = Transportion
        self.R16H1_ODoor3 = Transportion
        self.O_R16H1Spawn3 = ()
        self.R6_UnderGSEDoor = Transportion
        self.M3_DSpawn = ()
        self.SS_AnneF1Barriers = []
        self.Sea_CottageBarriers = []
        self.R16GuardHouseBarriers = []
        self.UndergroundSEntranceNPCS = []
        self.O_VCH1Door = Transportion
        self.PokemonFanClubReadables = []
        self.O_SS_AnneF1Spawn = ()
        self.SS_AnneF1_ODoor = Transportion
        self.UnderGSE_R6Spawn = ()
        self.PokeMartBarriers = []
        self.VCH2NPCS = []
        self.SS_Anne_OSpawn = ()
        self.O_SS_AnneDoor = Transportion
        self.VCPokeCenter_OSpawn = ()
        self.SS_AnneF1RoomsPickups = []
        self.VCPokeMart_OSpawn = ()
        self.O_VCPokeMartDoor = Transportion
        self.O_VCH1Spawn = ()
        self.O_VCPokeCenterDoor = Transportion
        self.UndergroundSEntranceBarriers = []
        self.SFH3F2_SFH3F1Spawn = ()
        self.SFH3F1NPCS = []
        self.Misty = GymLeaderNPC
        self.SFH3F1_SFH3F2Door = Transportion
        self.Mt_MoonF3Barriers = []
        self.SFH3F1_SFH3F2Spawn = ()
        self.SFH3F2_SFH3F1Door = Transportion
        self.SFH3F1_ODoor = Transportion
        self.O_SFH3F1Spawn = ()
        self.O_VCH2Door = Transportion
        self.SFH3F1Barriers = []
        self.VCH2_OSpawn = ()
        self.VCH2Barriers = []
        self.SS_AnneF1NPCS = []
        self.SAF1_R1Door = Transportion
        self.R1_SAF1Spawn = ()
        self.PlayerHouse1_0Transport = Transportion
        self.OverworldBarriers = []
        self.UnderGSE_UnderGNSTunnelSpawn = ()
        self.UnderGE_R5Door = Transportion
        self.R5_UnderGESpawn = ()
        self.CeruleanGymBarriers = []
        self.UnderGE_R5Spawn = ()
        self.R5_UnderGEDoor = Transportion
        self.CeruleanGymReadables = []
        self.OverworldReadables = []
        self.O2_RHSpawn = ()
        self.O2_RHDoor = Transportion
        self.UnderGE_UnderGNSTunnelSpawn = ()
        self.UndergroundEntranceBarriers = []
        self.Robbed_HouseNPCS = []
        self.PlayerRoomBarriers = []
        self.RH_O2Spawn = ()
        self.RH_O2Door = Transportion
        self.RivalHouseBarriers = []
        self.O_RHSpawn = ()
        self.RH_ODoor = Transportion
        self.O_RHDoor = Transportion
        self.Robbed_HouseBarriers = []
        self.O_DayCareSpawn = ()
        self.DayCare_ODoor = Transportion
        self.DayCareBarriers = []
        self.OakLabBarriers = []
        self.CeruleanGym_ODoor = Transportion
        self.Bike_ShopDesk = pygame.Rect
        self.PlayerHouse0Barriers = []
        self.Mt_MoonF1Barriers = []
        self.E_M3Spawn = ()
        self.M3_ESpawn = ()
        self.PlayerHouse0Readables = []
        self.BikeShopNPCS = []
        self.PewterGymBarriers = []
        self.BikeShop_ODoor = Transportion
        self.Bill_OSpawn = ()
        self.Daycare_OSpawn = ()
        self.O_BillDoor = Transportion
        self.BikeShopBarriers = []
        self.O_BikeShopSpawn = ()
        self.O_DaycareDoor = Transportion
        self.M3_ETunnel = Transportion
        self.O_CCGymDoor = Transportion
        self.M3_FSpawn = ()
        self.NugEnd = pygame.Rect
        self.F_M3Tunnel = Transportion
        self.E_M3Tunnel = Transportion
        self.PewterGymNPCS = []
        self.F_M3Spawn =()
        self.O_CCH2Door = Transportion
        self.NBRocket = TrainerNPC
        self.M3_DTunnel = Transportion
        self.Mom = NPC
        self.M3_FTunnel = Transportion
        self.Rival_sis = NPC
        self.R1SampleMart  = NPC
        self.R1InfoGuy = NPC
        self.O_PCM1Spawn = ()
        self.PPokeMartDoor = Transportion
        self.O_CCH2Spawn = ()
        self.PCM1_ODoor = Transportion
        self.BikeShopSpawn = ()
        self.PCM1Barriers = []
        self.CCH2_ODoor = Transportion
        self.PCM1NPCS = []
        self.R3NPCS = []
        self.O_BikeShopDoor = Transportion
        self.CCH2NPCS = []
        self.CCH2Barriers = []
        self.CCH2_OSpawn = ()
        self.PCM1_PCM2Spawn = ()
        self.PewterMuseumBasementReadables = []
        self.PCM2Barriers = []
        self.DaycareWorker = NPC
        self.Brock = GymLeaderNPC
        self.PCM2Barriers = []
        self.MtMoonF3Pickups = []
        self.CCGym_OSpawn = ()
        self.MtMoonF1Pickups = []
        self.MtMoonFossilsTiles = []
        self.PCM1_PCM2Stairs = Transportion
        self.PlayerHouse0_1Transport= Transportion
        self.PlayerHouse0_OTransport= Transportion
        self.PlayerHouseO_0Transport = (0,0)
        self.Overworld_RivalHouseTransport = Transportion
        self.RivalHouse_OverworldTransport = Transportion
        self.Overworld_OakLabTransport = Transportion
        self.OakLab_OverWorldTransport = Transportion
        self.OverworldGrassBlocks = []
        self.PLayerHouseOSpawn = ()
        self.CeruleanGymTrainers = []
        self.CeruleanGymTrainereyes = []
        self.R3_ATunnel = Transportion
        self.CCRivalBattleLine = pygame.Rect
        self.CCRivalBattleSpot = ()
        self.MtMoonF3Trainers = []
        self.PewterGym_ODoor = Transportion
        self.O_PewterGymDoor = Transportion
        self.Mt_MoonF3Rocks = []
        self.PewterGym_OSpawn = ()
        self.SCNPCS = []
        self.RivalHouseSpawn = ()
        self.RH_OSpwnpoint = ()
        self.PewterMuseumReadables = []
        self.Rival = NPC
        self.PickinPokeLine = pygame.Rect
        self.Oak_Overworldspawn = ()
        self.OaklabReadables = []
        self.Mt_MoonF1Rocks = []
        self.OakLabSpawn = ()
        self.D_M3Tunnel = Transportion
        self.Starters = []
        self.PCMBuyLine = pygame.Rect
        self.O_PewterGymSpawn = ()
        self.OakLabAides = []
        self.ViridainForestNPCs = []
        self.CCH1Barriers = []
        self.ViridainForestTrainers = []
        self.InCCH1_ODoor = Transportion
        self.Oak_Cutscene_Line = pygame.Rect
        self.Cutscene1Oak = NPC
        self.Oak = NPC
        self.PokeMartClerk = NPC
        self.InCCH1_BYSpawn = ()
        self.BY_CCH1Spawn = ()
        self.BY_CCH1Door = Transportion
        self.O_CCH1Door = Transportion
        self.OakStoppoint = ()
        self.O_InCCH1Spawn = ()
        self.CCH1NPCS = []
        self.RPokepickspawn1 = ()
        self.InCCH1_BYDoor = Transportion
        self.OverworldTrainers = []
        self.OverworldTrainereyes = []
        self.InCCH1_OSpawn = ()
        self.RPokepickspawn2 = ()
        self.RPokepickspawn3 = ()
        self.Rival_RivalBattlePoint = ()
        self.Player_RivalBattlePoint = ()
        self.PokemonMartSpawn = ()
        self.O_LPokeMartDoor = Transportion
        self.LPokeMart_OSpawn = ()
        self.Pokemon_MansionF1Trainers = []
        self.PokeCenterBarriers = []
        self.Pokemon_MansionFB1Trainers = []
        self.O_LPokeCenterDoor = Transportion
        self.Pokemon_MansionF3Trainers = []
        self.LPokeCenter_OSpawn = ()
        self.VH1Barriers = []
        self.Pokemon_MansionFB1Trainereyes = []
        self.Pokemon_MansionF3Trainereyes = []
        self.Pokemon_MansionF2Trainers = []
        self.Pokemon_MansionF2Trainereyes = []
        self.MtMoonFossils = []
        self.CliffBlocks = []
        self.PokeMart_ODoor = Transportion
        self.Pokemon_MansionF1Trainereyes = []
        self.O_VPokeCenterDoor = Transportion
        self.R3_CTunnel = Transportion
        self.PokeCenter_ODoor = Transportion
        self.O_VPokeMartDoor = Transportion
        self.R3_CSpawn = ()
        self.C_R3Tunnel = Transportion
        self.C_R3Spawn = ()
        self.VPokeMart_OSpawnpoint = ()
        self.B_R3Spawn = ()
        self.CutscenePokeMart = ()
        self.B_R3Tunnel = Transportion
        self.R3_BSpawn = ()
        self.VH1Spawn = ()
        self.R3_BTunnel = Transportion
        self.A_R3Tunnel = Transportion
        self.PPokeCenterDoor = Transportion
        self.Mt_MoonF2Rocks = []
        self.VH1_VCOSpawn = ()
        self.Rock_TunnelF1WildBlocks = []
        self.A_R3Spawn = ()
        self.G_M3Spawn = ()
        self.FakePower_PlantPickups = []
        self.PP_O2Door = Transportion
        self.O_RTF1Spawn = ()
        self.M3_GSpawn = ()
        self.PowerPlantWilds = []
        self.RTF1_ADoor = Transportion
        self.Fighting_DojoTrainers = []
        self.Zapdos = Tile
        self.Fighting_DojoBarriers = []
        self.Fighting_DojoTrainereyes = []
        self.Power_PlantPickups = []
        self.Fighting_DojoReadables = []
        self.FD_ODoor = Transportion
        self.O_FDSpawn = ()
        self.A_RTF1Spawn = ()
        self.Power_PlantHiddenItems = []
        self.C_RTF1Spawn = ()
        self.Rock_TunnelF1Trainers = []
        self.Exit_RTF1Spawn = ()
        self.D_RTF1Spawn = ()
        self.RTF1_DDoor = Transportion
        self.RTF1_ExitDoor = Transportion
        self.RTF1_BDoor = Transportion
        self.RTF1_CDoor = Transportion
        self.B_RTF1Spawn = ()
        self.G_M3Tunnel = Transportion
        self.RTF1_ODoor = Transportion
        self.M3_GTunnel = Transportion
        self.PokemonCenter_VCOSpawn = ()
        self.PokeballLine = pygame.Rect
        self.VGrandpaStoppoint = ()
        self.VH1Door = Transportion
        self.Rock_TunnelF1Barriers = []
        self.VH1_ODoor = Transportion
        self.VH2Barriers = []
        self.ViridainForestBarriers = []
        self.VH2_ODoor = Transportion
        self.O_RTF1Door = Transportion
        self.VGrandpa = NPC
        self.RTF1_OSpawn = ()
        self.Name_Rater = NPC
        self.AVGrandpa = NPC
        self.D_M3Spawn = ()
        self.VH2Spawn = ()
        self.R3_PokeCenterDoor = Transportion
        self.PokeTowerF1_ODoor = Transportion
        self.O_PokeTowerF1Spawn = ()
        self.PokeTowerF1Barriers = []
        self.PC_R3Spawn = ()
        self.Nurse_Joy = NPC
        self.PokeTowerF1_PokeTowerF2Door = Transportion
        self.VH2_VCOSpawn = ()
        self.VH2Door = Transportion
        self.PokeTowerF2_PokeTowerF1Spawn = ()
        self.PokemonTowerF1Desk = pygame.Rect
        self.PokemonCenterSpawn = ()
        self.ViridainCityNPCS = []
        self.SAF0_R1Door = Transportion
        self.PokeTowerF3Barriers = []
        self.PokeballSpawn = ()
        self.Cuttables = []
        self.SAF0_R1Spawn =()
        self.SAF0_R2Door = Transportion
        self.SS_AnneF0RoomsPickups = []
        self.SAF0_R3Door = Transportion
        self.SS_AnneF0RoomsTrainereyes = []
        self.SS_AnneF0RoomsTrainers = []
        self.SS_AnneF0RoomsNPCs = []
        self.R5_SAF0Spawn = ()
        self.R4_SAF0Spawn = ()
        self.R5_SAF0Door = Transportion
        self.SAF0_R5Spawn = ()
        self.R3_SAF0Spawn = ()
        self.SAF0_R5Door = Transportion
        self.SAF0_R4Spawn = ()
        self.R4_SAF0Door = Transportion
        self.R3_SAF0Door = Transportion
        self.PokeTowerF3_PokeTowerF2Spawn = ()
        self.PokeTowerF2_PokeTowerF3Door = Transportion 
        self.SAF0_R4Door = Transportion
        self.SAF0_R3Spawn =()
        self.SAF0_R2Spawn = ()
        self.R2_SAF0Spawn = ()
        self.R2_SAF0Door = Transportion
        self.Nurse_Joy_desk = pygame.Rect
        self.PokeCenterPC = pygame.Rect
        self.VF_AFDoor = Transportion
        self.PC_PH1Door = Transportion
        self.VH1NPCS = []
        self.PH1Barriers = []
        self.O_GCDoor = Transportion
        self.R3_MtMoonDoor = Transportion
        self.O_SaffronWExitSpawn = ()
        self.GC_OSpawn = ()
        self.CEPokeCenter_OSpawn = ()
        self.O_CEPokeCenterDoor = Transportion
        self.SaffronWExit_ODoor = Transportion
        self.PH2Barriers = []
        self.R7toSF_OSpawn = ()
        self.O_R7toSFDoor = Transportion
        self.SFNPCS = []
        self.O_PH1Spawn = ()
        self.SS_AnneF1RoomsTrainers = []
        self.O_SPokeMartDoor = Transportion
        self.SPokeMart_OSpawn = ()
        self.SPokeCenter_OSpawn = ()
        self.O_SPokeCenterDoor = Transportion
        self.O_PH2Spawn = ()
        self.PH1_OSpawn = ()
        self.SAF1_R3Door = Transportion
        self.O_VGymDoor = Transportion
        self.VGymAnnouncer = NPC
        self.VGym_ODoor = Transportion
        self.VGymTrainers = []
        self.VGymBarriers = []
        self.VGymTrainereyes = []
        self.VGym_OSpawn = ()
        self.O_VGymSpawn = ()
        self.SAF1_R3Spawn = ()
        self.VGymReadables = []
        self.SAF1_R4Spawn = ()
        self.R5_SAF1Door = Transportion
        self.SAF1_R5Door = Transportion
        self.SAF1_R6Door = Transportion
        self.SAF1_R6Spawn = ()
        self.R6_SAF1Spawn = ()
        self.R6_SAF1Door = Transportion
        self.SAF1_R5Spawn = ()
        self.R4_SAF1Door = Transportion
        self.R5_SAF1Spawn = ()
        self.R4_SAF1Spawn = ()
        self.R3_SAF1Door = Transportion
        self.R3_SAF1Spawn = ()
        self.CEGym_OSpawn = ()
        self.O_CEGymDoor = Transportion
        self.SAF1_R4Door = Transportion
        self.MtMoonF1Trainers = []
        self.CeladonGymBarriers = []
        self.PP_ODoor = Transportion
        self.O_PPSpawn = ()
        self.CeladonGymReadables = []
        self.O_CEGymSpawn = ()
        self.RBH_OSpawn = ()
        self.PowerPlantBarriers = []
        self.SAF1_R2Door = Transportion
        self.CEGym_ODoor = Transportion
        self.R2_SAF1Spawn = ()
        self.SAF1_R2Spawn = ()
        self.R2_SAF1Door = Transportion
        self.O_LTVHDoor = Transportion
        self.O_LTVHSpawn = ()
        self.LTVH_ODoor = Transportion
        self.LTVolunteerHouseReadables = []
        self.SZA1_MZDoor = Transportion
        self.LTVolunteerHouseNPCS = []
        self.LTVolunteerHouseBarriers = []
        self.LTVH_OSpawn = ()
        self.HelpBillSpawn = ()
        self.CEMF1_CEMF2Spawn = ()
        self.CEMF3_CEMF2Spawn = ()
        self.SZMZ_A1Spawn = ()
        self.CEMF2_CEMF3Door = Transportion
        self.BCEMF3_BCEMF2Spawn = ()
        self.BCEMF2_BCEMF3Door = Transportion
        self.CEMF2_CEMF1Door = Transportion
        self.BCEMF2_BCEMF1Door = Transportion
        self.BCEMF1_BCEMF2Spawn = ()
        self.MtMoon_R4Spawn =()
        self.R4_MtMoonSpawn = ()
        self.MtMoon_R4Tunnel = Transportion
        self.R4_MtMoonDoor = Transportion
        self.PH1NPCS = []
        self.PH2NPCS = []
        self.NPCFossilChoice = False
        self.FossilChosen = False
        self.GuardBoundry = pygame.Rect
        self.NPCHelix = NPC
        self.NPCDome = NPC
        self.Mt_MoonF2Barriers = []
        self.PCM2NPCS = []
        self.UnderGNSTunnel_UnderGEDoor = Transportion
        self.PH1_ODoor = Transportion
        self.MtMoonTrainerseyes = []
        self.PH2_ODoor = Transportion
        self.FCWHPickups = []
        self.SZA3HiddenItems = []
        self.O_CEMansionDoor = Transportion
        self.CEMansion_OSpawn = ()
        self.PewterGymTrainers = []
        self.O_FCH2Spawn = ()
        self.FCH2_ODoor = Transportion
        self.FCH2Barriers = []
        self.VH2NPCS = []
        self.FCH2_OSpawn = ()
        self.VH1Readables = []
        self.FD_OSpawn = ()
        self.O_FCH2Door = Transportion
        self.O_FDDoor = Transportion
        self.O_SFH1Spawn = ()
        self.SFH1_ODoor = Transportion
        self.MrPsychic = NPC
        self.UnderGE_UnderGRDoor = Transportion
        self.Terrains = []
        self.FCH2NPCS = []
        self.BrockBattleLine = pygame.Rect
        self.SFH1Barriers = []
        self.PokeMartDesk = pygame.Rect
        self.O_SFH1Door = Transportion
        self.SFH1_OSpawn = ()
        self.R22RivalSpot = ()
        self.OptionalRivalBattleLine = pygame.Rect
        self.SilCoG1_SilCoG2Door = Transportion
        self.SilCoF5Man = NPC
        self.Silph_CoF6Trainereyes = []
        self.Silph_CoF6Trainers = []
        self.SilCoF3Pickups = []
        self.SilCoF5Pickups = []
        self.SilCoE1_SilCoE2Spawn = ()
        self.SilCoF6Pickups = []
        self.VictoryRoadB2_B1Door = Transportion
        self.VictoryRoadB1_B2Spawn = ()
        self.VictoryRoadB1_B2Door = Transportion
        self.VictoryRoadB2_B1Spawn = ()
        self.SilCoF4Pickups = []
        self.SilCoE2_SilCoE1Door = Transportion
        self.SilCoH1_SilCoH2Spawn = ()
        self.SilCoH2_SilCoH1Door = Transportion
        self.VictoryRoadF3_F2Spawn = ()
        self.SilCoG2_SilCoG1Spawn = ()
        self.SilCoF1_SilCoF2Door2 = Transportion
        self.SilCoF2_SilCoF1Spawn2 = ()
        self.VictoryRoadF3_F2Door = Transportion
        self.VictoryRoadC2_C1Door = Transportion
        self.VictoryRoadC1_C2Spawn = ()
        self.VictoryRoadC1_C2Door = Transportion
        self.VictoryRoadC2_C1Spawn = ()
        self.VictoryRoadD1_D2Door = Transportion
        self.VictoryRoadD2_D1Spawn = ()
        self.VictoryRoadD2_D1Door = Transportion
        self.VictoryRoadD1_D2Spawn = ()
        self.VictoryRoadE2_E1Door = Transportion
        self.VictoryRoadE1_E2Spawn = ()
        self.VictoryRoadE1_E2Door = Transportion
        self.VictoryRoadE2_E1Spawn = ()
        self.O_FCH1Door = Transportion
        self.FCH1_OSpawn = ()
        self.FCH1NPCS = []
        self.O_PokeLeagueDoor = Transportion
        self.R3_Aspawn = ()
        self.UnderGR_UnderGESpawn = ()
        self.VGymBarrierPlace = ()
        self.SS_AnneF3HallWayNPCS = []
        self.VGymBarrier = pygame.Rect
        self.Underground_WEntranceBarriers = []
        self.Mt_MoonF1Readables = []
        self.Underground_WEntranceNPCS = []
        self.O_AFDoor = Transportion
        self.PokemonLeagueF1Barriers = []
        self.UGWEHiddenItems = []
        self.UGNSHiddenItems = []
        self.FCWHBoulders = []
        self.Fighting_DojoLeader = TrainerNPC
        self.Silph_CoF7Trainereyes = []
        self.SilCoF1_SilCoF2Spawn2 = ()
        self.SilCoF2_SilCoF1Door2 = Transportion
        self.Silph_CoF7Trainers = []
        self.PL_OSpawn = ()
        self.SilCoJ1_SilCoJ2Spawn = ()
        self.SilCoE_SilCoF7Spawn = ()
        self.SilCoF7Pickups = []
        self.SilCoF7_SilCoEDoor = Transportion
        self.SilCoI1_SilCoI2Spawn = ()
        self.PPokeMart_OSpawn = ()
        self.SilCoJ2_SilCoJ1Door = Transportion
        self.Silph_CoF6NPCS = []
        self.SilCoF6_SilCoEDoor = Transportion
        self.SilCoE_SilCoF6Spawn = ()
        self.SilCoI2_SilCoI1Door = Transportion
        self.CliffBlocks2 = []
        self.PokemonLeagueF1Spawn = ()
        self.Silph_CoF4Trainers = []
        self.Silph_CoF4Trainereyes = []
        self.UGWEEntrance_OSpawn = ()
        self.SilCoD2_SilCoD1Door = Transportion
        self.SilCoE1_SilCoE2Door = Transportion
        self.SilCoE2_SilCoE1Spawn = ()
        self.SilCoN1_SilCoN2Spawn = ()
        self.SilCoN2_SilCoN1Door = Transportion
        self.O_UGWEEntranceDoor = Transportion
        self.SilCoO2_SilCoO1Spawn = ()
        self.SilCoO1_SilCoO2Door = Transportion
        self.SilCoH2_SilCoH1Spawn = ()
        self.SilCoQ2_SilCoQ1Spawn = ()
        self.SilCoH1_SilCoH2Door = Transportion
        self.SilCoN2_SilCoN1Spawn = ()
        self.SilCoN1_SilCoN2Door = Transportion
        self.Pokemon_TowerF5NPCS = []
        self.DojoFightLine = pygame.Rect
        self.PewterGymReadables = []
        self.PokeTowerF6Trainers = []
        self.PokeTowerSafeZone = pygame.Rect
        self.Fighting_DojoPokemon = []
        self.PokeTowerF6Trainereyes = []
        self.PCGymBarriers = []
        self.Silph_CoF3Trainers = []
        self.Silph_CoF3Trainereyes = []
        self.PC_CCSpawn = ()
        self.SilCoD2_SilCoD1Spawn = ()
        self.SilCoI2_SilCoI1Spawn = ()
        self.SilCoA2_SilCoA1Spawn = ()
        self.SilCoD1_SilCoD2Door = Transportion
        self.CCNPCS = []
        self.SilCoI1_SilCoI2Door = Transportion
        self.SilCoB2_SilCoB1Spawn = ()
        self.SilCoB1_SilCoB2Door = Transportion
        self.Rock_TunnelF2Trainereyes = []
        self.SilCoA1_SilCoA2Door = Transportion
        self.PCM_OSpawn = ()
        self.SilCoK2_SilCoK1Spawn = ()
        self.Silph_CoF5Trainereyes = []
        self.SilCoK1_SilCoK2Door = Transportion
        self.CC_PMDoor = Transportion
        self.Silph_CoF5Trainers = []
        self.SilCoF4Man = NPC
        self.PokeTowerGhostLine = pygame.Rect
        self.SilCoF9Woman = NPC
        self.Silph_CoF10Trainers = []
        self.Silph_CoF10Trainereyes = []
        self.SilCoF9HiddenItems = []
        self.MRWoman = TraderNPC
        self.MRMan = NPC
        self.CeladonGymCuttables = []
        self.SilCoQ1_SilCoQ2Spawn = ()
        self.SilCoQ2_SilCoQ1Door = Transportion
        self.PM_CCSpawn = ()
        self.SilCoF5_SilCoEDoor = Transportion
        self.SilCoG1_SilCoG2Spawn = ()
        self.SilCoG2_SilCoG1Door = Transportion
        self.SilCoE_SilCoF5Spawn = ()
        self.SilCoM2_SilCoM1Spawn = ()
        self.SilCoM1_SilCoM2Door = Transportion
        self.GCRocket = TrainerNPC
        self.MROld_Man = TraderNPC
        self.SilCoJ2_SilCoJ1Spawn = ()
        self.Creator = TrainerNPC
        self.SilCoJ1_SilCoJ2Door = Transportion
        self.MROld_Man = TraderNPC
        self.PokeLeague_ODoor = Transportion
        self.SilCoL2_SilCoL1Spawn = ()
        self.SilCoL1_SilCoL2Door = Transportion
        self.SilCoE_SilCoF9Spawn = ()
        self.SilCoF9_SilCoEDoor = Transportion
        self.ViridianForestTrainereyes = []
        self.Silph_CoF9Trainers = []
        self.SilCoE_SilCoF10Spawn = ()
        self.SilCoF10_SilCoEDoor = Transportion
        self.Silph_CoF9Trainereyes = []
        self.PVF_VFSpawn = ()
        self.CC_PCDoor = Transportion
        self.SilCoA1_SilCoA2Spawn = ()
        self.SilCoL1_SilCoL2Spawn = ()
        self.SilCoE_SilCoF11Spawn = ()
        self.SilCoF11_SilCoEDoor = Transportion
        self.SilCoF10Pickups = []
        self.SilCoK1_SilCoK2Spawn = ()
        self.Silph_CoF11Trainers = []
        self.Silph_CoF11Trainereyes = []
        self.SilCoK2_SilCoK1Door = Transportion
        self.SilCoL2_SilCoL1Door = Transportion
        self.SilCoM1_SilCoM2Spawn = ()
        self.SilCoM2_SilCoM1Door = Transportion
        self.SilCoA2_SilCoA1Door = Transportion
        self.SilCoC2_SilCoC1Spawn = ()
        self.SilCoC1_SilCoC2Door = Transportion
        self.SilCoC1_SilCoC2Spawn = ()
        self.SilCoC2_SilCoC1Door = Transportion
        self.SilCoF8Man = NPC
        self.SilCoB1_SilCoB2Spawn = ()
        self.SilCoB2_SilCoB1Door = ()
        self.SilCoE_SilCoF4Spawn = ()
        self.SilCoF4_SilCoEDoor = Transportion
        self.SZE_OSpawn = ()
        self.SZEDesk = pygame.Rect
        self.O_SZEDoor = Transportion
        self.PLGuard1 = NPC
        self.ViridainForestReadables = []
        self.Traders = []
        self.R2_PVFTransport = Transportion
        self.PreViridainForestBarriers = []
        self.PokeTowerF4Trainers = []
        self.PokeTowerF4Trainereyes = []
        self.PokeTowerF5Trainers = []
        self.PokeTowerF5Trainereyes = []
        self.AF_ODoor = Transportion
        self.AF_VFDoor = Transportion
        self.SilCoPresident = NPC
        self.VF_AFSpawn = ()
        self.O_AFSpawn = ()
        self.Silph_CoF11NPCS = []
        self.RocketBaseF1_RocketBaseF2Spawn = ()
        self.SilCoF5HiddenItems = []
        self.RBaseGiovanni = TrainerNPC
        self.Mr_Fuji = NPC
        self.RocketBaseF2_RocketBaseF1Door = Transportion
        self.Rocket_HideoutF2Pickups = []
        self.CeruleanGymNPCS = []
        self.SilCoP1_SilCoP2Spawn = ()
        self.SilCoP2_SilCoP1Door = Transportion
        self.CEStoreElevatorBarriers = []
        self.SilCoE_SilCoF3Spawn =()
        self.SilphCoRivalSpot = ()
        self.SilCoF3_SilCoEDoor = Transportion
        self.SilCoD1_SilCoD2Spawn = ()
        self.SilphCoRivalBattleLine = pygame.Rect
        self.AfterForestNPC = []
        self.Rocket_HideoutF1HiddenItems = []
        self.VGuy = NPC
        self.AfterForestBarriers = []
        self.Rocket_HideoutF1Pickups = []
        self.RocketBaseF2_RocketBaseF1Spawn = ()
        self.RocketBaseF1_RocketBaseF2Door = Transportion
        self.AF_VFSpawn = ()
        self.SilCoF3Man = NPC
        self.SFA2_A1Door = Transportion
        self.SFE2_E1Spawn = ()
        self.SFE1_E2Door = Transportion
        self.SFF2_F1Spawn = ()
        self.SFF1_F2Door = Transportion
        self.SFF1_F2Spawn = ()
        self.SFM2_M1Door = Transportion
        self.SFN2_N1Spawn = ()
        self.SFIWave3Spawn = ()
        self.SFN1_N2Door = Transportion
        self.SeaFoam_IslandFB2HiddenItems = []
        self.LSFII2_I1Spawn = ()
        self.SeaFoam_IslandFB3Boulders = []
        self.SFIFB3_BF4Hole = Transportion
        self.LSFII2_I1Door = Transportion
        self.LSFII1_I2Spawn = ()
        self.SeaFoam_IslandFB4Boulders = []
        self.LSFIJ1_J2Spawn = ()
        self.SeaFoam_IslandFB2Boulders = []
        self.LSFIG1_G2Spawn = ()
        self.SeaFoam_IslandFB4Readables =[]
        self.SFIFB2_BF32Hole = Transportion
        self.SFIFB3_BF42Hole = Transportion
        self.Articuno = Tile
        self.SFIFB3_BF4Spawn = ()
        self.SFIFB2_BF3Hole = Transportion
        self.SFIBF4Risingpoint = pygame.Rect
        self.SFIFB3_BF42Spawn = ()
        self.LSFII1_I2Door = Transportion
        self.SFIWave2Spawn = ()
        self.SFIF1_BF12Hole = Transportion
        self.SeaFoam_IslandFB3FishingPoint = []
        self.SeaFoam_IslandFB4FishingPoint = []
        self.SFIFB2_BF33Spawn = ()
        self.SFIF1_BF1Hole = Transportion
        self.SFIFB2_BF3Spawn = ()
        self.SFIFB2_BF32Spawn = ()
        self.SFIWaveSpawn = ()
        self.LSFIG2_G1Spawn =()
        self.SFIF1_BF12Spawn = ()
        self.SeaFoam_IslandFB4Wilds =[]
        self.SeaFoam_IslandF1Wilds = []
        self.SeaFoam_IslandFB3Wilds = []
        self.SeaFoam_IslandFB4HiddenItems = []
        self.SeaFoam_IslandFB3HiddenItems = []
        self.SeaFoam_IslandFB2Wilds = []
        self.SeaFoam_IslandFB1Wilds = []
        self.SFIF1_BF1Spawn = ()
        self.SFIFB1_BF22Spawn =()
        self.LSFIJ2_J1Door = Transportion
        self.SFIFB1_BF2Spawn =()
        self.LSFIG2_G1Door = Transportion
        self.LSFIG1_G2Door = Transportion
        self.SFO2_O1Spawn = ()
        self.LSFIF2_F1Door = Transportion
        self.LSFIF1_F2Spawn =()
        self.LSFIJ1_J2Door = Transportion
        self.LSFIH1_H2Door = Transportion
        self.LSFIJ2_J1Spawn = ()
        self.SFIFB1_BF2Hole = Transportion
        self.SFIFB1_BF22Hole = Transportion
        self.LSFIH2_H1Spawn = ()
        self.SFM2_M1Spawn = ()
        self.LSFIH1_H2Spawn =()
        self.LSFIH2_H1Door = Transportion
        self.LSFIF2_F1Spawn = ()
        self.LSFIF1_F2Door = Transportion
        self.SFO2_O1Door = Transportion
        self.SFH2_H1Spawn = ()
        self.SFM1_M2Door = Transportion
        self.SFO1_O2Spawn = ()
        self.SFM1_M2Spawn = ()
        self.SFO1_O2Door = Transportion
        self.SFH1_H2Door = Transportion
        self.SFH1_H2Spawn = ()
        self.SFL2_L1Door = Transportion
        self.SFL1_L2Spawn = ()
        self.SFH2_H1Door = Transportion
        self.SFN1_N2Spawn = ()
        self.SFN2_N1Door = Transportion
        self.SFI2_I1Spawn = ()
        self.SFI1_I2Door = Transportion
        self.SFJ2_J1Spawn = ()
        self.SFJ1_J2Door = Transportion
        self.SFJ1_J2Spawn = ()
        self.SFJ2_J1Door = Transportion
        self.SFK2_K1Spawn = ()
        self.SFK1_K2Door = Transportion
        self.SFK1_K2Spawn = ()
        self.SFK2_K1Door = Transportion
        self.R1NPCS = []
        self.SFL2_L1Spawn = ()
        self.SFL1_L2Door = Transportion
        self.SFI1_I2Spawn = ()
        self.SFI2_I1Door = Transportion
        self.SFF2_F1Door = Transportion
        self.SFG2_G1Spawn = ()
        self.SFG1_G2Door = Transportion
        self.VRoadF3Trainers = []
        self.SFG1_G2Spawn = ()
        self.SFG2_G1Door = Transportion
        self.SFE1_E2Spawn = ()
        self.VRoadF3Trainereyes = []
        self.SFE2_E1Door = Transportion
        self.SFA1_A2Spawn = ()
        self.VRoadF2Trainers =[]
        self.SFA2_A1Door = Transportion
        self.SFB2_B1Spawn = ()
        self.VRoadF2Trainereyes = []
        self.SFB1_B2Door = Transportion
        self.SFB1_B2Spawn = ()
        self.StartersSprites = []
        self.SFD2_D1Spawn = ()
        self.SFD1_D2Door = Transportion
        self.SFD1_D2Spawn = ()
        self.FameHallSpawn = ()
        self.SFD2_D1Door = Transportion
        self.SFC2_C1Spawn = ()
        self.SFC1_C2Door = Transportion
        self.SFC1_C2Spawn = ()
        self.SFC2_C1Door = Transportion
        self.SFB2_B1Door = Transportion
        self.PVF_R2Spawn = ()
        self.HW_SAF3Door = Transportion
        self.SFA2_A1Spawn = ()
        self.ElevatorSpawn = ()
        self.Rock_TunnelF1Trainereyes = []
        self.SFA1_A2Door = Transportion
        self.CEStoreF5Barriers = []
        self.SAF3_HWSpawn = ()
        self.Rock_TunnelF2WildBlocks = []
        self.PewterGymTrainereyes = []
        self.AF_OSpawn = ()
        self.OverworldPickups = []
        self.DiglettCaveRocks = []
        self.R16House2Girl = NPC
        self.R2_PVFSpawn = ()
        self.VF_PVFSpawn =()
        self.CoinMan = NPC
        self.R3_MtMoonSpawn = ()
        self.OverworldNPCS = []
        self.R3_MtMoonDoor = Transportion
        self.Surge = GymLeaderNPC
        self.PPC_OSpawn = ()
        self.SSTicketCheck = pygame.Rect
        self.PVF_R2Door = Transportion
        self.MtMoon_R3Spawn = ()
        self.MtMoon_R3Door = Transportion
        self.ViridainForestPickups = []
        self.VF_R2Door = Transportion
        self.PreForestNPC = []
        self.ViridainForestGrass = []
        self.PVF_VFDoor = Transportion
        self.BadgeCheck1 = pygame.Rect
        self.Load_Kanto_region()
        self.Load_PlayerHouse()
        self.Load_RivalHouse()
        self.Load_OakLab()
        self.Load_PokeMart()
        self.Load_PokeCenter()
        self.Load_VH1()
        self.Load_VH2()
        self.Load_PokemonLeagueF1()
        self.Load_PreForest()
        self.Load_AfterForest()
        self.Load_ViridainForest()
        self.Load_R21H()
        self.Load_R22H()
        self.Load_PH1()
        self.Load_PH2()
        self.Load_PewterGym()
        self.Load_PewterMuseum()
        self.Load_MtMoon()
        self.Load_CCH1()
        self.Load_CCH2()
        self.Load_Bike_Shop()
        self.Load_CeruleanGym()
        self.Load_Sea_Cottage()
        self.Load_RobbedHouse()
        self.Load_DayCare()
        self.Load_BetweenR5_SC()
        self.Load_UnderGround_Entrance()
        self.Load_UnderGroundNSTunnel()
        self.Load_VCH1()
        self.Load_PokemonFan_Club()
        self.Load_SS_Anne()
        self.Load_SS_AnneF0()
        self.Load_SS_AnneF2()
        self.Load_SS_AnneF3()
        self.Load_VermilionGym()
        self.Load_DiglettCave()
        self.Load_R11H()
        self.Load_Rock_Tunnel()
        self.Load_LTVolunteerHouse()
        self.Load_LT1H()
        self.Load_SaffronEWEntrance()
        self.Load_UnderGroundWE_Entrance()
        self.Load_UnderGroundWETunnel()
        self.Load_Game_Corner()
        self.Load_Prize_Booth()
        self.Load_CERestourant()
        self.Load_CE1H()
        self.Load_CE2H()
        self.Load_CEMansion()
        self.Load_CEStore()
        self.Load_CeladonGym()
        self.Load_GCRocketBase()
        self.Load_PokemonTower()
        self.Load_R16GuardHouse()
        self.Load_R16House2()
        self.Load_R18GuardHouse()
        self.Load_FC1H()
        self.Load_FC2H()
        self.Load_FC3H()
        self.Load_FCWH()
        self.Load_SZE()
        self.Load_SafariZone()
        self.Load_SZMAH1()
        self.Load_SZA3SH()
        self.Load_FuschiaGym()
        self.Load_Fighting_Dojo()
        self.Load_SFH1()
        self.Load_SilphCo()
        self.Load_SFH2()
        self.Load_SFH3()
        self.Load_SaffronGym()
        self.Load_R12GuardHouse()
        self.Load_R12H()
        self.Load_R15GuardHouse()
        self.Load_PokemonLab()
        self.Load_PokemonMansion()
        self.Load_CinnabarGym()
        self.Load_ViridianGym()
        self.Load_Victory_Road()
        self.Load_IndigoPlateauEntrance()
        self.Load_IndigoPlateau()
        self.Load_IndigoPlateauChampion()
        self.Load_Hall_of_Fame()
        self.Load_Power_Plant()
        self.Load_SeaFoam_Islands()
        self.Load_Cerulean_Cave()
        self.VRoadF3Trainers = self.TrainerEyes(self.VRoadF3Trainereyes,self.VRoadF3Trainers)
        self.VRoadF2Trainers = self.TrainerEyes(self.VRoadF2Trainereyes,self.VRoadF2Trainers)
        self.VRoadF1Trainers = self.TrainerEyes(self.VRoadF1Trainereyes,self.VRoadF1Trainers)
        self.VGymTrainers = self.TrainerEyes(self.VGymTrainereyes,self.VGymTrainers)
        self.Pokemon_MansionFB1Trainers = self.TrainerEyes(self.Pokemon_MansionFB1Trainereyes,self.Pokemon_MansionFB1Trainers)
        self.Pokemon_MansionF3Trainers = self.TrainerEyes(self.Pokemon_MansionF3Trainereyes,self.Pokemon_MansionF3Trainers)
        self.Pokemon_MansionF2Trainers = self.TrainerEyes(self.Pokemon_MansionF2Trainereyes,self.Pokemon_MansionF2Trainers)
        self.Pokemon_MansionF1Trainers = self.TrainerEyes(self.Pokemon_MansionF1Trainereyes,self.Pokemon_MansionF1Trainers)
        self.SFGymTrainers = self.TrainerEyes(self.SFGymTrainereyes,self.SFGymTrainers)
        self.Silph_CoF11Trainers = self.TrainerEyes(self.Silph_CoF11Trainereyes,self.Silph_CoF11Trainers)
        self.Silph_CoF10Trainers = self.TrainerEyes(self.Silph_CoF10Trainereyes,self.Silph_CoF10Trainers)
        self.Silph_CoF9Trainers = self.TrainerEyes(self.Silph_CoF9Trainereyes,self.Silph_CoF9Trainers)
        self.Silph_CoF8Trainers = self.TrainerEyes(self.Silph_CoF8Trainereyes,self.Silph_CoF8Trainers)
        self.Silph_CoF7Trainers = self.TrainerEyes(self.Silph_CoF7Trainereyes,self.Silph_CoF7Trainers)
        self.Silph_CoF6Trainers = self.TrainerEyes(self.Silph_CoF6Trainereyes,self.Silph_CoF6Trainers)
        self.Silph_CoF5Trainers = self.TrainerEyes(self.Silph_CoF5Trainereyes,self.Silph_CoF5Trainers)
        self.Silph_CoF4Trainers = self.TrainerEyes(self.Silph_CoF4Trainereyes,self.Silph_CoF4Trainers)
        self.Silph_CoF3Trainers = self.TrainerEyes(self.Silph_CoF3Trainereyes,self.Silph_CoF3Trainers)
        self.Silph_CoF2Trainers = self.TrainerEyes(self.Silph_CoF2Trainereyes,self.Silph_CoF2Trainers)
        self.Fighting_DojoTrainers = self.TrainerEyes(self.Fighting_DojoTrainereyes,self.Fighting_DojoTrainers)
        self.FCGymTrainers = self.TrainerEyes(self.FCGymTrainereyes,self.FCGymTrainers)
        self.PokeTowerF7Trainers = self.TrainerEyes(self.PokeTowerF7Trainereyes,self.PokeTowerF7Trainers)
        self.PokeTowerF6Trainers = self.TrainerEyes(self.PokeTowerF6Trainereyes,self.PokeTowerF6Trainers)
        self.PokeTowerF5Trainers = self.TrainerEyes(self.PokeTowerF5Trainereyes,self.PokeTowerF5Trainers)
        self.PokeTowerF4Trainers = self.TrainerEyes(self.PokeTowerF4Trainereyes,self.PokeTowerF4Trainers)
        self.PokeTowerF3Trainers = self.TrainerEyes(self.PokeTowerF3Trainereyes,self.PokeTowerF3Trainers)
        self.RocketBaseF4Trainers = self.TrainerEyes(self.RocketBaseF4Trainereyes,self.RocketBaseF4Trainers)
        self.RocketBaseF3Trainers = self.TrainerEyes(self.RocketBaseF3Trainereyes,self.RocketBaseF3Trainers)
        self.RocketBaseF2Trainers = self.TrainerEyes(self.RocketBaseF2Trainereyes,self.RocketBaseF2Trainers)
        self.RocketBaseF1Trainers = self.TrainerEyes(self.RocketBaseF1Trainereyes,self.RocketBaseF1Trainers)
        self.CeladonGymTrainers = self.TrainerEyes(self.CeladonGymTrainereyes,self.CeladonGymTrainers)
        self.Rock_TunnelF1Trainers = self.TrainerEyes(self.Rock_TunnelF1Trainereyes,self.Rock_TunnelF1Trainers)
        self.Rock_TunnelF2Trainers = self.TrainerEyes(self.Rock_TunnelF2Trainereyes,self.Rock_TunnelF2Trainers)
        self.VermilionGymTrainers = self.TrainerEyes(self.VermilionGymTrainereyes,self.VermilionGymTrainers)
        self.SS_AnneF2RoomsTrainers = self.TrainerEyes(self.SS_AnneF2RoomsTrainereyes,self.SS_AnneF2RoomsTrainers)
        self.SS_AnneF3Trainers = self.TrainerEyes(self.SS_AnneF3Trainereyes,self.SS_AnneF3Trainers)
        self.SS_AnneF0RoomsTrainers = self.TrainerEyes(self.SS_AnneF0RoomsTrainereyes,self.SS_AnneF0RoomsTrainers)
        self.SS_AnneF1RoomsTrainers = self.TrainerEyes(self.SS_AnneF1RoomsTrainereyes,self.SS_AnneF1RoomsTrainers)
        self.CeruleanGymTrainers = self.TrainerEyes(self.CeruleanGymTrainereyes,self.CeruleanGymTrainers)
        self.ViridainForestTrainers = self.TrainerEyes(self.ViridianForestTrainereyes,self.ViridainForestTrainers)
        self.MtMoonF1Trainers = self.TrainerEyes(self.MtMoonTrainerseyes,self.MtMoonF1Trainers)
        self.MtMoonF3Trainers = self.TrainerEyes(self.MtMoonTrainerseyes,self.MtMoonF3Trainers)
        self.PewterGymTrainers = self.TrainerEyes(self.PewterGymTrainereyes,self.PewterGymTrainers)
        self.OverworldTrainers = self.TrainerEyes(self.OverworldTrainereyes,self.OverworldTrainers)
    
    def TrainerEyes(self,Vision:list[TrainerVision],Trainers:list[TrainerNPC]):
        New = []
        for Trainer in Trainers:
            if Trainer.Vision == None:
                for eyes in Vision:
                    if eyes.Trainer == Trainer.CompName:
                        Trainer.Vision = eyes.rect
                        New.append(Trainer)
        return New

    def Load_Kanto_region(self):
        for layer in self.Kanto.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.OverworldCamera))

        for obj in self.Kanto.objects:
            if obj.name in ("Dr.Oak Lab_toprect","Player_House_rect","RivalHouse_rect","Bushes","Fence","Border","VirdinPokerect","VirdinPokeMartrect","VirdinHouse1rect","VirdinHouse2rect"):
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.OverworldBarriers.append(Rect)
            elif obj.name == "PlayerHouseOSpawn":
                self.PLayerHouseOSpawn = (obj.x,obj.y)
            elif obj.name == "Dr.OakSpawnpoint":
                self.Oak_Overworldspawn = (obj.x,obj.y)
            elif obj.name == "PLayerDoorO_0":
                self.PlayerHouseO_0Transport =Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RH_OSpawn":
                self.RH_OSpwnpoint = (obj.x,obj.y)
            elif obj.name == "RivalHouse_Door":
                self.Overworld_RivalHouseTransport = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Prof.Oak Door":
                self.Overworld_OakLabTransport = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Oak_Line": self.Oak_Cutscene_Line = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Oak": 
                self.Cutscene1Oak = NPC(obj.image,(self.OverworldCamera),"Talk",(obj.x,obj.y),'',"Oak")
                self.OverworldCamera.remove(self.Cutscene1Oak)
            elif obj.name == "AF_O": self.AF_OSpawn = (obj.x,obj.y)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.OverworldHiddenItems.append(H)
            elif obj.name == "O_AFDoor":self.O_AFDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Mart Employee":
                self.R1SampleMart = NPC(obj.image,(self.OverworldCamera),"Giver",(obj.x,obj.y),obj.Dialouge,"Mart Boy",obj.Dialouge2,obj.Dialouge3,obj.Item,1,"We also carry POKE BALLS for catching POKEMON!",'','')
                self.OverworldBarriers.append(self.R1SampleMart.rect)
                self.R1NPCS.append(self.R1SampleMart)
            elif obj.name == "InfoGuy1":
                self.R1InfoGuy = NPC(obj.image,(self.OverworldCamera),"Dialogue",(obj.x,obj.y),obj.Dialouge,"Random Guy",obj.Dialouge2,obj.Dialouge3)
                self.OverworldBarriers.append(self.R1InfoGuy.rect)
                self.R1NPCS.append(self.R1InfoGuy)
            elif obj.name in ("RedHouseSign","RivalHouseSign","TownSign","Dr.Oak Sign","Credits#2","Next","Sign"):
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,Text2=obj.Text2,Text3=obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.OverworldCamera))
                self.OverworldReadables.append(Read)
                self.OverworldBarriers.append(Read.Rect)
            elif obj.name == "PokeLeagueDoor": self.O_PokeLeagueDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeLeagueSpawn": self.PL_OSpawn = (obj.x,obj.y)
            elif obj.name == "Grass_Patch":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.OverworldGrassBlocks.append(WildTile)
            elif obj.name == "Cliff":
                Cliff = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CliffBlocks.append(Cliff)
            elif obj.name == "Cliff2":
                Cliff = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CliffBlocks2.append(Cliff)
            elif obj.name == "LandMark": 
                T = Terrains(obj.x,obj.y,obj.width,obj.height,obj.Land)
                self.Terrains.append(T)
            elif obj.name == "TT":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.OverworldCamera))
                self.OverworldReadables.append(Read)
                self.OverworldBarriers.append(Read.Rect)
            elif obj.name == "Snorlax":
                S = Tile((obj.x,obj.y),obj.image,(self.OverworldCamera))
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.OverworldReadables.append(Read)
                self.OverworldBarriers.append(Read.Rect)
                self.VCSleepingSnorlax = [S,Read]
            elif obj.name == "V.GrandpaPoint": self.VGrandpaStoppoint = (obj.x,obj.y)
            elif obj.name == "VPokeMartDoor": self.O_VPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name in ("VRandom Guy","VGrandpa GrandDaughter","VCatipillar Guy","VOld Man"):
                npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[1::],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.ViridainCityNPCS.append(npc)
                self.OverworldBarriers.append(npc.rect)
            elif obj.name == "VGrandpa":
                self.VGrandpa = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Grandpa",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.ViridainCityNPCS.append(self.VGrandpa)
                self.OverworldBarriers.append(self.VGrandpa.rect)
            elif obj.name == "VGuy":
                self.VGuy = NPC(obj.image,(self.OverworldCamera),"Giver",(obj.x,obj.y),obj.Dialouge,"Guy",obj.Dialouge2,obj.Dialouge3,obj.Item,1,"TM42 contains DREAM EATER... ...Snore...",'','')
                self.OverworldBarriers.append(self.VGuy.rect)
                self.ViridainCityNPCS.append(self.VGuy)
            elif obj.name == "AGrandpa":self.AVGrandpa = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Grandpa",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            elif obj.name == "VPokeMartSpawn": self.VPokeMart_OSpawnpoint = (obj.x,obj.y)
            elif obj.name == "VPokeCenterSpawn": self.PokemonCenter_VCOSpawn = (obj.x,obj.y)
            elif obj.name == "VH1Spawn": self.VH1_VCOSpawn = (obj.x,obj.y)
            elif obj.name == "VPokeCenterDoor":self.O_VPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VH1Door": self.VH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VH2Spawn": self.VH2_VCOSpawn = (obj.x,obj.y)
            elif obj.name == "VH2Door": self.VH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "OldManStop": self.PokeballLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "OldManSpawn": self.PokeballSpawn = (obj.x,obj.y)
            elif obj.name == "R22RivalBattle": self.OptionalRivalBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "R22RivalSpot": self.R22RivalSpot = (obj.x,obj.y)
            elif obj.name == "VGymBarrierPlace": self.VGymBarrierPlace = (obj.x,obj.y)
            elif obj.name == "VGymBarrier":self.VGymBarrier = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Small Tree":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                tree = Tile((obj.x,obj.y),obj.image,(self.OverworldCamera))
                self.Cuttables.append([Rect,tree])
                self.OverworldBarriers.append(Rect)
            elif obj.name == "VFEntrance":self.R2_PVFTransport = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VF_OSpawn": self.PVF_R2Spawn = (obj.x,obj.y)
            elif obj.name in ("PMan", "PGirl"):
                npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[1::],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.OverworldNPCS.append(npc)
                self.OverworldBarriers.append(npc.rect)
            elif obj.name == "PHouse1Door": self.PC_PH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PH1_OSpawn": self.PH1_OSpawn = (obj.x,obj.y)
            elif obj.name == "PPokeCenterDoor":self.PPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "DCExit_OSpawn": self.DCExit_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_DCExitDoor":self.O_DCExitDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PPC_OSpawn": self.PPC_OSpawn = (obj.x,obj.y)
            elif obj.name == "PH2Door": self.PC_PH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PH2_OSpawn": self.PH2_OSpawn = (obj.x,obj.y)
            elif obj.name == "PPokeMart":self.PPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PPokeMart_OSpawn":self.PPokeMart_OSpawn = (obj.x,obj.y)
            elif obj.name == "PCGym_OSpawn":self.PewterGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "BrockBattleLine":self.BrockBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "PCGymDoor":self.O_PewterGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PCMuseumDoor": self.O_PCMDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PCM_OSpawn": self.PCM_OSpawn = (obj.x,obj.y)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.OverworldTrainereyes.append(eyes)
            elif obj.name in ("R3Girl","R3Man"):
                npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R3NPCS.append(npc)
                self.OverworldBarriers.append(npc.rect)
            elif obj.name == "PC_R3Spawn":
                self.PC_R3Spawn = (obj.x,obj.y)
            elif obj.name == "R3_PokeCenterDoor":
                self.R3_PokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R3_Mt.MoonDoor":self.R3_MtMoonDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Mt.Moon_R3Spawn":self.MtMoon_R3Spawn = (obj.x,obj.y)
            elif obj.name == "Mt.Moon_R4Spawn":self.MtMoon_R4Spawn = (obj.x,obj.y)
            elif obj.name == "R4_Mt.MoonDoor":self.R4_MtMoonDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PC_CCSpawn":self.PC_CCSpawn = (obj.x,obj.y)
            elif obj.name == "PM_CCSpawn":self.PM_CCSpawn = (obj.x,obj.y)
            elif obj.name == "CC_PMDoor":self.CC_PMDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CC_PCDoor":self.CC_PCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCH1Door":self.O_CCH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "InCCH1_OSpawn":self.InCCH1_OSpawn = (obj.x,obj.y)
            elif obj.name == "InCCH1_BYSpawn":self.InCCH1_BYSpawn = (obj.x,obj.y)
            elif obj.name == "BY1Door":self.BY_CCH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_CCH2Door":self.O_CCH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCH2_OSpawn":self.CCH2_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_BikeShopDoor":self.O_BikeShopDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BikeShopSpawn":self.BikeShopSpawn = (obj.x,obj.y)
            elif obj.name == "CCRivalBattleLine":self.CCRivalBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "CCRivalBattleSpot": self.CCRivalBattleSpot = (obj.x,obj.y)
            elif obj.name == "O_CCGymDoor":self.O_CCGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCGym_OSpawn":self.CCGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_BillDoor":self.O_BillDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Bill_OSpawn":self.Bill_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_RHDoor":self.O_RHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RBH_OSpawn":self.RBH_OSpawn = (obj.x,obj.y)
            elif obj.name == "O2_RHDoor":self.O2_RHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RH_O2Spawn":self.RH_O2Spawn = (obj.x,obj.y)
            elif obj.name == "Daycare_OSpawn":self.Daycare_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_DaycareDoor":self.O_DaycareDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "InterR5_OSpawn":self.InterEnterance_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_InterR5Door":self.O_InterR5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "UnderGE_R5Spawn":self.UnderGE_R5Spawn = (obj.x,obj.y)
            elif obj.name == "R5_UnderGEDoor":self.R5_UnderGEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "UnderGSE_R6Spawn":self.UnderGSE_R6Spawn = (obj.x,obj.y)
            elif obj.name == "R6_UnderGSEDoor":self.R6_UnderGSEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_VCH1Door":self.O_VCH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VCH1_OSpawn":self.VCH1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_VCH2Door":self.O_VCH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VCH2_OSpawn":self.VCH2_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_PFCDoor":self.O_PFCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PFC_OSpawn":self.PFC_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_VCH3Door":self.O_VCH3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VCH3_OSpawn":self.VCH3_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_R21HDoor":self.O_R21HDoor= Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R21H_OSpawn":self.R21H_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_VCPokeCenterDoor":self.O_VCPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VCPokeCenter_OSpawn":self.VCPokeCenter_OSpawn = (obj.x,obj.y)
            elif obj.name == "SS.TicketCheck":self.SSTicketCheck = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "O_VCPokeMartDoor":self.O_VCPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VCPokeMart_OSpawn":self.VCPokeMart_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SS.AnneDoor":self.O_SS_AnneDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SS.Anne_OSpawn":self.SS_Anne_OSpawn = (obj.x,obj.y)
            elif obj.name == "VC_OSpawn":self.VC_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_VCDoor":self.O_VCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ship":self.SSShip = Tile((obj.x,obj.y),obj.image,(self.OverworldCamera),"Ship")
            elif obj.name == "DCE_R11Spawn":self.DCE_R11Spawn = (obj.x,obj.y)
            elif obj.name == "R11_DCEDoor":self.R11_DCEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R22H_VOSpawn":self.R22H_VOSpawn = (obj.x,obj.y)
            elif obj.name == "VO_R22HDoor":self.VO_R22HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R22H_POSpawn":self.R22H_POSpawn = (obj.x,obj.y)
            elif obj.name == "PO_R22HDoor":self.PO_R22HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R11H_VCOSpawn":self.R11H_VCOSpawn = (obj.x,obj.y)
            elif obj.name == "VCO_R11HDoor":self.VCO_R11HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R11H_R12Spawn":self.R11H_R12Spawn = (obj.x,obj.y)
            elif obj.name == "R12_R11HDoor":self.R12_R11HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "InterR6_OSpawn":self.InterR6_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_InterR6Door":self.O_InterR6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R10_PCDoor":self.R10_PCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PC_R10Spawn":self.PC_R10Spawn = (obj.x,obj.y)
            elif obj.name == "O_RTF1Door":self.O_RTF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RTF1_OSpawn":self.RTF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "Exit_RTF1Door":self.Exit_RTF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RTF1_ExitSpawn":self.RTF1_ExitSpawn = (obj.x,obj.y)
            elif obj.name == "O_LPokeCenterDoor":self.O_LPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LPokeCenter_OSpawn":self.LPokeCenter_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_LPokeMartDoor":self.O_LPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LPokeMart_OSpawn":self.LPokeMart_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_LTVHDoor":self.O_LTVHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LTVH_OSpawn":self.LTVH_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_LTH1Door":self.O_LTH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LTH1_OSpawn":self.LTH1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_LTH2Door":self.O_LTH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LTH2_OSpawn":self.LTH2_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_R8toSFDoor":self.O_R8toSFDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R8toSF_OSpawn":self.R8toSF_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_UGEWEntranceDoor":self.O_UGEWEntranceDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "UGEWEntrance_OSpawn":self.UGEWEntrance_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_UGWEEntranceDoor":self.O_UGWEEntranceDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "UGWEEntrance_OSpawn":self.UGWEEntrance_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_R7toSFDoor":self.O_R7toSFDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R7toSF_OSpawn":self.R7toSF_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CEPokeCenterDoor":self.O_CEPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEPokeCenter_OSpawn":self.CEPokeCenter_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_GCDoor":self.O_GCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "GC_OSpawn":self.GC_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_PrizeBoothDoor":self.O_PrizeBoothDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PrizeBooth_OSpawn":self.PrizeBooth_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CERestourantDoor":self.O_CERestourantDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CERestourant_OSpawn":self.CERestourant_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CE1HDoor":self.O_CE1HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CE1H_OSpawn":self.CE1H_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CE2HDoor":self.O_CE2HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CE2H_OSpawn":self.CE2H_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CEMansionDoor":self.O_CEMansionDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEMansion_OSpawn":self.CEMansion_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_BCEMF1Door":self.O_BCEMF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF1_OSpawn":self.BCEMF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CEStoreF1RightDoor":self.O_CEStoreF1RightDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF1Right_OSpawn":self.CEStoreF1Right_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CEStoreF1LeftDoor":self.O_CEStoreF1LeftDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF1Left_OSpawn":self.CEStoreF1Left_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CEGymDoor":self.O_CEGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEGym_OSpawn":self.CEGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_PokeTowerF1Door":self.O_PokeTowerF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeTowerF1_OSpawn":self.PokeTowerF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "3O_R16H1Door":self.O_R16H1Door3 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "3R16H1_OSpawn":self.R16H1_OSpawn3 = (obj.x,obj.y)
            elif obj.name == "O_R16H1Door":self.O_R16H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R16H1_OSpawn":self.R16H1_OSpawn = (obj.x,obj.y)
            elif obj.name == "2O_R16H1Door":self.O_R16H1Door2 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "2R16H1_OSpawn":self.R16H1_OSpawn2 = (obj.x,obj.y)
            elif obj.name == "4O_R16H1Door":self.O_R16H1Door4 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "4R16H1_OSpawn":self.R16H1_OSpawn4 = (obj.x,obj.y)
            elif obj.name == "O_R16H2Door":self.O_R16H2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R16H2_OSpawn":self.R16H2_OSpawn = (obj.x,obj.y)
            elif obj.name == "Bike Only":self.Bike_OnlyZone = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "O_R18GHDoor":self.O_R18GHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R18GH_OSpawn":self.R18GH_OSpawn = (obj.x,obj.y)
            elif obj.name == "O2_R18GHDoor":self.O2_R18GHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R18GH_O2Spawn":self.R18GH_O2Spawn = (obj.x,obj.y)
            elif obj.name == "Bike Only2":self.Bike_OnlyZone2 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "O_FPokeCenterDoor":self.O_FPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FPokeCenter_OSpawn":self.FPokeCenter_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_FPokeMartDoor":self.O_FPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FPokeMart_OSpawn":self.FPokeMart_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_FCH1Door":self.O_FCH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FCH1_OSpawn":self.FCH1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_FCH2Door":self.O_FCH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FCH2_OSpawn":self.FCH2_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_FCH3Door":self.O_FCH3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FCH3_OSpawn":self.FCH3_OSpawn = (obj.x,obj.y)
            elif obj.name == "O2_FCH3Door":self.O2_FCH3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FCH3_O2Spawn":self.FCH3_O2Spawn = (obj.x,obj.y)
            elif obj.name == "O_FCWHDoor":self.O_FCWHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FCWH_OSpawn":self.FCWH_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SZEDoor":self.O_SZEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZE_OSpawn":self.SZE_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_FCGymDoor":self.O_FCGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FCGym_OSpawn":self.FCGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SPokeCenterDoor":self.O_SPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SPokeCenter_OSpawn":self.SPokeCenter_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SPokeMartDoor":self.O_SPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SPokeMart_OSpawn":self.SPokeMart_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SFH1Door":self.O_SFH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFH1_OSpawn":self.SFH1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_FDDoor":self.O_FDDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FD_OSpawn":self.FD_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SilCoF1Door":self.O_SilCoF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF1_OSpawn":self.SilCoF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SFtoR7Door":self.O_SFtoR7Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFtoR7_OSpawn":self.SFtoR7_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SFtoR8Door":self.O_SFtoR8Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFtoR8_OSpawn":self.SFtoR8_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SFH2Door":self.O_SFH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFH2_OSpawn":self.SFH2_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_SFH3F1Door":self.O_SFH3F1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFH3F1_OSpawn":self.SFH3F1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O2_InterR5Door":self.O2_InterR5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "InterR5_O2Spawn":self.InterR5_O2Spawn = (obj.x,obj.y)
            elif obj.name == "O2_InterR6Door":self.O2_InterR6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "InterR6_O2Spawn":self.InterR6_O2Spawn = (obj.x,obj.y)
            elif obj.name == "O_SFGymDoor":self.O_SFGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFGym_OSpawn":self.SFGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_R12GuardHouseDoor":self.O_R12GuardHouseDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R12GuardHouse_OSpawn":self.R12GuardHouse_OSpawn = (obj.x,obj.y)
            elif obj.name == "O2_R12GuardHouseDoor":self.O2_R12GuardHouseDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R12GuardHouse_O2Spawn":self.R12GuardHouse_O2Spawn = (obj.x,obj.y)
            elif obj.name == "O_R12HDoor":self.O_R12HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R12H_OSpawn":self.R12H_OSpawn = (obj.x,obj.y)
            elif obj.name == "R15_GHDoor":self.R15_GHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "GH_R15Spawn":self.GH_R15Spawn = (obj.x,obj.y)
            elif obj.name == "FC_GHDoor":self.FC_GHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "GH_FCSpawn":self.GH_FCSpawn = (obj.x,obj.y)
            elif obj.name == "O_CIPokeCenterDoor":self.O_CIPokeCenterDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CIPokeCenterSpawn":self.CIPokeCenterSpawn = (obj.x,obj.y)
            elif obj.name == "O_CIPokeMartDoor":self.O_CIPokeMartDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CIPokeMartSpawn":self.CIPokeMartSpawn = (obj.x,obj.y)
            elif obj.name == "O_PokeLabHallDoor":self.O_PokeLabHallDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeLabHall_OSpawn":self.PokeLabHall_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_PokeMansionF1Door":self.O_PokeMansionF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionF1_OSpawn":self.PokeMansionF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CGymDoor":self.O_CGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CGym_OSpawn":self.CGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_VGymDoor":self.O_VGymDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VGym_OSpawn":self.VGym_OSpawn = (obj.x,obj.y)
            elif obj.name == "PCMuseum2Door": self.PCMuseum2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PCM_O2Spawn": self.PCM_O2Spawn = (obj.x,obj.y)
            elif obj.name == "BPLRivalBattle": self.BPLRivalBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BPLRivalSpot": self.BPLRivalSpot = (obj.x,obj.y)
            elif obj.name == "R23_PLF1Door": self.R23_PLF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PLF1_R23Spawn": self.PLF1_R23Spawn = (obj.x,obj.y)
            elif obj.name == "BadgeCheck1": self.R23BadgeCheck1 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BadgeCheck2": self.R23BadgeCheck2 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BadgeCheck3": self.R23BadgeCheck3 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BadgeCheck4": self.R23BadgeCheck4 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BadgeCheck5": self.R23BadgeCheck5 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BadgeCheck6": self.R23BadgeCheck6 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BadgeCheck7": self.R23BadgeCheck7 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "O_VictoryRoadF1Door": self.O_VictoryRoadF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadF1_OSpawn": self.VictoryRoadF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_VictoryRoadF2Door": self.O_VictoryRoadF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadF2_OSpawn": self.VictoryRoadF2_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_ILEDoor": self.O_ILEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "ILE_OSpawn": self.ILE_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_PPDoor": self.O_PPDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PP_OSpawn": self.PP_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_LSFIF1Door": self.O_LSFIF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIF1_OSpawn": self.LSFIF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_RSFIF1Door": self.O_RSFIF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RSFIF1_OSpawn": self.RSFIF1_OSpawn = (obj.x,obj.y)
            elif obj.name == "O_CCaveDoor": self.O_CCaveDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCave_OSpawn": self.CCave_OSpawn = (obj.x,obj.y)
            elif obj.name == "OakBattle": self.OakBattle = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "BattleOak":
                self.BattlerOak = TrainerNPC("Oak",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.OverworldCamera.remove(self.BattlerOak)
            elif obj.name == "CESnorlax":
                S = Tile((obj.x,obj.y),obj.image,(self.OverworldCamera))
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.OverworldReadables.append(Read)
                self.OverworldBarriers.append(Read.Rect)
                self.CESleepingSnorlax = [S,Read]
            elif obj.name == "Seapoint":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.OverworldFishingPoint.append(Rect)
                self.OverworldBarriers.append(Rect)
            elif obj.name == "NB1Rocket":
                self.NBRocket = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.OverworldBarriers.append(self.NBRocket.rect)
            elif obj.name == "R24JR.TRAINER(Male)":
                trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.OverworldTrainers.append(trainer)
                self.OverworldBarriers.append(trainer.rect)
            elif obj.name == "NugEnd":
                self.NugEnd = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.OverworldCamera,obj.Item)
                self.OverworldPickups.append(ball)
            elif obj.name != None:
                if "R3" in obj.name:
                    trainer = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)
                elif "R11" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)
                elif obj.name == "R41Lass":
                    trainer = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)
                elif "CC1" in obj.name or "CC2" in obj.name:
                    if obj.name != "CC1Rocket":
                        npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[3:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                        self.CCNPCS.append(npc)
                        self.OverworldBarriers.append(npc.rect)
                elif obj.name == "CCaveMan":
                    self.CCaveMan = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Man",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.OverworldBarriers.append(self.CCaveMan.rect)
                elif "VC" in obj.name:
                    npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[3:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.OverworldNPCS.append(npc)
                    self.OverworldBarriers.append(npc.rect)
                elif "PG" in obj.name:
                    npc = TraderNPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                    self.PostgameNPCS.append(npc)
                    self.OverworldCamera.remove(npc)
                elif "LT" in obj.name:
                    npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[3:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.OverworldNPCS.append(npc)
                    self.OverworldBarriers.append(npc.rect)
                elif "FC" in obj.name:
                    npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.OverworldNPCS.append(npc)
                    self.OverworldBarriers.append(npc.rect)
                elif "CE" in obj.name:
                    if obj.name == "CESOld Man":
                        self.CESOldMan = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[3:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="TM41 reaches SOFTBOILED! Only one POKEMON can use it! That POKEMON",IA2="is CHANSEY!")
                        self.OverworldNPCS.append(self.CESOldMan)
                        self.OverworldBarriers.append(self.CESOldMan.rect)
                    npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.OverworldNPCS.append(npc)
                    self.OverworldBarriers.append(npc.rect)
                elif "NB" in obj.name:
                    if obj.name != "NB1JR.TRAINER(Male)":
                        trainer = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                elif "R25" in obj.name:
                    if obj.name != "R251JR.TRAINER(Male)":
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                elif "R6" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                elif "R9" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                elif "R10" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                elif "R8" in obj.name:
                    trainer = TrainerNPC(obj.name[3:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)
                elif "R16" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)
                elif "R17" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)
                elif "R18" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect)            
                elif "SF" in obj.name:
                    npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    if "Rocket" not in obj.name:self.OverworldCamera.remove(npc)
                    else:self.OverworldBarriers.append(npc.rect)
                    self.SFNPCS.append(npc)
                elif "R12" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)               
                elif "R13" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)   
                elif "R14" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect) 
                elif "R15" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)
                    else:
                        trainer = TrainerNPC("JR.TRAINER",obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                        self.OverworldTrainers.append(trainer)
                        self.OverworldBarriers.append(trainer.rect)     
                elif "R19" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect) 
                elif "R20" in obj.name:
                    if "JR.TRAINER" not in obj.name:
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    else:
                        trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect) 
                elif "R21" in obj.name:
                    trainer = TrainerNPC(obj.name[4:],obj.image,self.OverworldCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.OverworldTrainers.append(trainer)
                    self.OverworldBarriers.append(trainer.rect) 
                elif "R23" in obj.name:
                    npc = NPC(obj.image,self.OverworldCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[4:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.OverworldNPCS.append(npc)
                    self.OverworldBarriers.append(npc.rect)
            else:
                if obj.image: Tile((obj.x,obj.y),obj.image,(self.OverworldCamera))

    def Load_PlayerHouse(self):
        for layer in self.PlayerHouse.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "PlayerRoom":
                        Tile((x*32,y*32),surf,(self.PLayerHouse1Camera))
                    else: Tile((x*32,y*32),surf,(self.PLayerHouse0Camera))
        
        for obj in self.PlayerHouse.objects:
            if obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PlayerRoomBarriers.append(Rect)
            if obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PlayerHouse0Barriers.append(Rect)
            if obj.name in ("PS4_rect","TrashCan"):
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text)
                self.PlayerRoomBarriers.append(Read.Rect)
                self.PlayerRoomReadables.append(Read)
            elif obj.name in ("Computer_rect"):
                I = Interactions(obj.x,obj.y,obj.width,obj.height,obj.name)
                self.PlayerRoomInteracts.append(I)
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PlayerRoomBarriers.append(Rect)
            elif obj.name in ("Downstairs"):
                self.PlayerHouse1_0Transport = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)              
            elif obj.name in ("UpStairs"):
                self.PlayerHouse0_1Transport= Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name in ("Overworld_Door"):
                self.PlayerHouse0_OTransport= Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name in ("TV","Books"):
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text)
                self.PlayerHouse0Readables.append(Read)
                self.PlayerHouse0Barriers.append(Read.Rect)
            elif obj.name == "SSSpawn": self.SSPlayerHouseSpawnpoint = (obj.x,obj.y)
            elif obj.name == "Startpoint1":self.PlayerDHouseSpawnpoint = (obj.x,obj.y)
            elif obj.name == "HouseSpawnPoint":self.PlayerHouseO_0Spawnpoint = (obj.x,obj.y)
            elif obj.name == "Mom": 
                self.Mom = NPC(obj.image,(self.PLayerHouse0Camera),"Dialogue",(obj.x,obj.y),obj.Dialouge,"Mom",obj.Dialouge2)
                self.PlayerHouse0Barriers.append(self.Mom.rect)

    def Load_RivalHouse(self):
        for layer in self.RivalHouse.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.RivalHouseCamera))
        
        for obj in self.RivalHouse.objects:
            if obj.name == "RivalHouse0_O": self.RivalHouseSpawn = (obj.x,obj.y)
            elif obj.name == "RivalHouseDoor": self.RivalHouse_OverworldTransport = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Rival_sis": 
                self.Rival_sis = NPC(obj.image,(self.RivalHouseCamera),"Dialogue",(obj.x,obj.y),obj.Dialouge,obj.name,Item="Map",ItemAmount=1,IA1="POKEMON are living things! If they get tired, give them a rest!",IA2='')
                self.RivalHouseBarriers.append(self.Rival_sis.rect)
            else:
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RivalHouseBarriers.append(Rect)

    def Load_OakLab(self):
        for layer in self.OakLab.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.OakLabCamera))
        
        for obj in self.OakLab.objects:
            if obj.name == "Oak_LabDoor": self.OakLab_OverWorldTransport = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Spawnpoint": self.OakLabSpawn = (obj.x,obj.y)
            elif obj.name == "Rivalpoint": self.Rival_RivalBattlePoint = (obj.x,obj.y)
            elif obj.name == "Point": self.Player_RivalBattlePoint = (obj.x,obj.y)
            elif obj.name == "Rival": 
                self.Rival = NPC(obj.image,(self.OakLabCamera),"Dialogue",(obj.x,obj.y),obj.Dialouge,obj.name)
                self.OakLabBarriers.append(self.Rival.rect)
            elif obj.name == "Oak": 
                self.Oak = NPC(obj.image,(self.OakLabCamera),"Dialogue",(obj.x,obj.y),"",obj.name)
                self.OakLabCamera.remove(self.Oak)
            elif obj.name == "Stoppoint": self.OakStoppoint = (obj.x,obj.y)
            elif obj.name == "Pokeball":
                ball = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.Poke)
                self.Starters.append(ball)
                self.StartersSprites.append(Tile((obj.x,obj.y),obj.image,(self.OakLabCamera),obj.Poke))
            elif obj.name == "Stop":
                self.PickinPokeLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "B": self.RPokepickspawn1 = (obj.x,obj.y)
            elif obj.name == "S": self.RPokepickspawn2 = (obj.x,obj.y)
            elif obj.name == "C": self.RPokepickspawn3 = (obj.x,obj.y)
            elif obj.name == "Books":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.OakLabBarriers.append(Rect)
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name)
                self.OaklabReadables.append(Read)
            elif obj.name == "Aide":
                npc = NPC(obj.image,(self.OakLabCamera),"Dialogue",(obj.x,obj.y),obj.Text,"Aide")
                self.OakLabAides.append(npc)
            else:
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.OakLabBarriers.append(Rect)

    def Load_PokeMart(self):
        for layer in self.PokeMart.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PokeMartCamera))

        for obj in self.PokeMart.objects:
            if obj.name == "PlayerPoint": self.PokemonMartSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PokeMart_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeMartBarriers.append(Rect)
            elif obj.name == "Store Clerk": self.PokeMartClerk = NPC(obj.image,self.PokeMartCamera,"Dialogue",(obj.x,obj.y),obj.Dialouge,obj.name)
            elif obj.name == "CutscenePoint":self.CutscenePokeMart = (obj.x,obj.y)
            elif obj.name == "Desk": 
                self.PokeMartDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeMartBarriers.append(self.PokeMartDesk)

    def Load_PokeCenter(self):
        for layer in self.PokeCenter.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PokeCenterCamera))

        for obj in self.PokeCenter.objects:
            if obj.name == "PlayerPoint": self.PokemonCenterSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PokeCenter_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Nurse": self.Nurse_Joy = NPC(obj.image,self.PokeCenterCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Nurse",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            elif obj.name == "Desk": self.Nurse_Joy_desk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeCenterBarriers.append(Rect)
            elif obj.name == "PC": 
                self.PokeCenterPC = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeCenterBarriers.append(self.PokeCenterPC)

    def Load_VH1(self):
        for layer in self.VH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.VH1Camera))

        for obj in self.VH1.objects:
            if obj.name == "PlayerPoint": self.VH1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.VH1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VH1Barriers.append(Rect)
            elif obj.name == "Read":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text)
                self.VH1Readables.append(Read)
                self.VH1Barriers.append(Read.Rect)
            else:
                npc = NPC(obj.image,self.VH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.VH1NPCS.append(npc)
                self.VH1Barriers.append(npc.rect)
    
    def Load_VH2(self):
        for layer in self.VH2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.VH2Camera))

        for obj in self.VH2.objects:
            if obj.name == "PlayerPoint": self.VH2Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.VH2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VH2Barriers.append(Rect)
            else:
                npc = NPC(obj.image,self.VH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.VH2NPCS.append(npc)
                self.VH2Barriers.append(npc.rect)
    
    def Load_PokemonLeagueF1(self):
        for layer in self.PokemonLeagueF1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PokemonLeagueF1Camera))

        for obj in self.PokemonLeagueF1.objects:
            if obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokemonLeagueF1Barriers.append(Rect)
            elif obj.name == "PlayerPoint": self.PokemonLeagueF1Spawn = (obj.x,obj.y)
            elif obj.name == "Guard1":
                self.PLGuard1 = NPC(obj.image,self.PokemonLeagueF1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Guard")
                self.PokemonLeagueF1Barriers.append(self.PLGuard1.rect)
            elif obj.name == "Door": self.PokeLeague_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R23_PLF1Spawn": self.R23_PLF1Spawn = (obj.x,obj.y)
            elif obj.name == "PLF1_R23Door": self.PLF1_R23Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Check": self.BadgeCheck1 = pygame.Rect((obj.x,obj.y),(obj.width,obj.height))

    def Load_PreForest(self):
        for layer in self.PreForest.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PreForestCamera))
        
        for obj in self.PreForest.objects:
            if obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PreViridainForestBarriers.append(Rect)
            elif obj.name == "R2": self.PVF_R2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VF": self.PVF_VFDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Playerpoint": self.R2_PVFSpawn = (obj.x,obj.y)
            elif obj.name == "Playerpoint2":
                self.VF_PVFSpawn = (obj.x,obj.y)
                
            else:
                npc = NPC(obj.image,self.PreForestCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PreForestNPC.append(npc)
                self.PreViridainForestBarriers.append(npc.rect)

    def Load_AfterForest(self):
        for layer in self.AfterForest.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.AfterForestCamera))
        
        for obj in self.AfterForest.objects:
            if obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.AfterForestBarriers.append(Rect)
            elif obj.name == "Overworld": self.AF_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VF": self.AF_VFDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Playerpoint": 
                self.VF_AFSpawn = (obj.x,obj.y)
            elif obj.name == "Playerpoint2":self.O_AFSpawn = (obj.x,obj.y)               
            else:
                npc = NPC(obj.image,self.AfterForestCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.AfterForestNPC.append(npc)
                self.AfterForestBarriers.append(npc.rect)

    def Load_ViridainForest(self):
        for layer in self.ViridainForest.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.ViridainForestCamera))
        
        for obj in self.ViridainForest.objects:
            if obj.name in ("Trees","Stump"):
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.ViridainForestBarriers.append(Rect)
            elif obj.name == "Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,Text2=obj.Text2,Text3=obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.ViridainForestCamera))
                self.ViridainForestBarriers.append(Read.Rect)
                self.ViridainForestReadables.append(Read)
            elif obj.name == "PlayerPoint": self.PVF_VFSpawn = (obj.x,obj.y)
            elif obj.name =="Playerpoint2": self.AF_VFSpawn = (obj.x,obj.y)
            elif obj.name == "OverWorld": self.VF_R2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Pewter City": self.VF_AFDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.VFHiddenItems.append(H)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.ViridainForestCamera,obj.Item)
                self.ViridainForestPickups.append(ball)
            elif obj.name == "Grass_Patch":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.ViridainForestGrass.append(WildTile)
            elif obj.name == "Boy":
                npc = NPC(obj.image,self.ViridainForestCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Boy",obj.Dialouge2,obj.Dialouge3)
                self.ViridainForestNPCs.append(npc)
                self.ViridainForestBarriers.append(npc.rect)
            elif "Bug" in obj.name:
                trainer = TrainerNPC(obj.name[1:],obj.image,self.ViridainForestCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.ViridainForestTrainers.append(trainer)
                self.ViridainForestBarriers.append(trainer.rect)
            elif obj.name == "Vision":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.ViridianForestTrainereyes.append(eyes)

    def Load_PH1(self):
        for layer in self.PH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PH1Camera))
        
        for obj in self.PH1.objects:
            if obj.name == "PlayerPoint": 
                self.O_PH1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PH1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PH1Barriers.append(Rect)
            else:
                npc = NPC(obj.image,self.PH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PH1NPCS.append(npc)
                self.PH1Barriers.append(npc.rect)
    
    def Load_PH2(self):
        for layer in self.PH2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PH2Camera))
        
        for obj in self.PH2.objects:
            if obj.name == "PlayerPoint": 
                self.O_PH2Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PH2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PH2Barriers.append(Rect)
            else:
                npc = NPC(obj.image,self.PH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PH2NPCS.append(npc)
                self.PH2Barriers.append(npc.rect)
    
    def Load_PewterGym(self):
        for layer in self.PewterGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PewterGymCamera))
        
        for obj in self.PewterGym.objects:
            if obj.name == "PlayerPoint": 
                self.O_PewterGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PewterGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PewterGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.PewterGymReadables.append(Read)
                self.PewterGymBarriers.append(Read.Rect)
            elif obj.name == "JR.TRAINER(Male)":
                trainer = TrainerNPC("JR.TRAINER",obj.image,self.PewterGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,"JR.TRAINER(Male)")
                self.PewterGymTrainers.append(trainer)
                self.PewterGymBarriers.append(trainer.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.PewterGymTrainereyes.append(eyes)
            elif obj.name == "Brock":     
                self.Brock = GymLeaderNPC("Brock",obj.image,self.PewterGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.PewterGymBarriers.append(self.Brock.rect)
            else:
                npc = NPC(obj.image,self.PewterGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PewterGymNPCS.append(npc)
                self.PewterGymBarriers.append(npc.rect)

    def Load_PewterMuseum(self):
        for layer in self.PewterMuseum.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "1stFloor":Tile((x*32,y*32),surf,(self.PewterMuseumCamera))
                    else: Tile((x*32,y*32),surf,(self.PewterMuseumBasementCamera))
        
        for obj in self.PewterMuseum.objects:
            if obj.name == "PlayerPoint": 
                self.O_PCM1Spawn = (obj.x,obj.y)
            elif obj.name == "PlayerPoint2": 
                self.O2_PCM1Spawn = (obj.x,obj.y)
            elif obj.name == "PlayerPoint3": 
                self.PCM1_PCM2Spawn = (obj.x,obj.y)
            elif obj.name == "Stairs":
                self.PCM1_PCM2Stairs = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Up":
                self.PCM2_PCM1Stairs = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Door": self.PCM1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Door2": self.PCM1_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BuyLine":
                self.PCMBuyLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PCM1Barriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PCM2Barriers.append(Rect)
            elif obj.name == "Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.PewterMuseumReadables.append(Read)
                self.PCM1Barriers.append(Read.Rect)
            elif obj.name == "Sign2":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.PewterMuseumBasementReadables.append(Read)
                self.PCM2Barriers.append(Read.Rect)
            elif obj.name == "GScientist":
                self.PCM1GScientist = NPC(obj.image,self.PewterMuseumCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Scientist",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Ssh! Get the OLD AMBER checked!",IA2="",IA3="")
                self.PCM1Barriers.append(self.PCM1GScientist.rect)
                self.PCM1NPCS.append(self.PCM1GScientist)
            elif obj.name in ("Scientist", "Old Man"):
                npc = NPC(obj.image,self.PewterMuseumCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PCM1NPCS.append(npc)
                self.PCM1Barriers.append(npc.rect)
            elif obj.name in ("Scientist2", "Old Man2","Boy2","Dad2","Girl2"):
                npc = NPC(obj.image,self.PewterMuseumBasementCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[:-1],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PCM2NPCS.append(npc)
                self.PCM2Barriers.append(npc.rect)
    
    def Load_MtMoon(self):
        for layer in self.Mt_Moon.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "First Floor":Tile((x*32,y*32),surf,(self.Mt_MoonFloor1Camera))
                    elif layer.name == "Second Floor": Tile((x*32,y*32),surf,(self.Mt_MoonFloor2Camera))
                    else:Tile((x*32,y*32),surf,(self.Mt_MoonFloor3Camera))
        
        for obj in self.Mt_Moon.objects:
            if obj.name == "Rocks": 
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Mt_MoonF1Barriers.append(Rect)
            elif obj.name == "Rocks2": 
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Mt_MoonF2Barriers.append(Rect)
            elif obj.name == "Rocks3": 
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Mt_MoonF3Barriers.append(Rect)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.MtM3HiddenItems.append(H)
            elif obj.name == "R3_Mt.MoonSpawn":
                self.R3_MtMoonSpawn = (obj.x,obj.y)
            elif obj.name == "Mt.Moon_R3Door":
                self.MtMoon_R3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wild Rocks":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Mt_MoonF1Rocks.append(Rock)
            elif obj.name == "Wild Rocks2":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Mt_MoonF2Rocks.append(Rock)
            elif obj.name == "Wild Rocks3":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Mt_MoonF3Rocks.append(Rock)
            elif "Mt.MoonF1" in obj.name:
                trainer = TrainerNPC(obj.name[10:],obj.image,self.Mt_MoonFloor1Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.MtMoonF1Trainers.append(trainer)
                self.Mt_MoonF1Barriers.append(trainer.rect)
            elif "Mt.MoonF3" in obj.name:
                trainer = TrainerNPC(obj.name[10:],obj.image,self.Mt_MoonFloor3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.MtMoonF3Trainers.append(trainer)
                self.Mt_MoonF3Barriers.append(trainer.rect)
            elif obj.name == "Fossil":
                F = Tile((obj.x,obj.y),obj.image,(self.Mt_MoonFloor3Camera),obj.Fossil)
                self.MtMoonFossilsTiles.append(F)
                fossil = Readables(obj.x,obj.y,obj.width,obj.height,f"Do you want the {obj.Fossil}",obj.Fossil)
                self.MtMoonFossils.append(fossil)
                self.Mt_MoonF3Barriers.append(fossil.Rect)
            elif obj.name == "HF":self.NPCHelix = NPC(obj.image,self.Mt_MoonFloor3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            elif obj.name == "DF":self.NPCDome = NPC(obj.image,self.Mt_MoonFloor3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.Mt_MoonFloor1Camera,obj.Item)
                self.MtMoonF1Pickups.append(ball)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Mt_MoonFloor3Camera,obj.Item)
                self.MtMoonF3Pickups.append(ball)
            elif obj.name == "Vision":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.MtMoonTrainerseyes.append(eyes)
            elif obj.name == "Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,Text2=obj.Text2,Text3=obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.Mt_MoonFloor1Camera))
                self.Mt_MoonF1Barriers.append(Read.Rect)
                self.Mt_MoonF1Readables.append(Read)
            elif obj.name == "R3_ASpawn":
                self.R3_Aspawn = (obj.x,obj.y)
            elif obj.name == "R3_ATunnel":
                self.R3_ATunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "A_R3Spawn":
                self.A_R3Spawn = (obj.x,obj.y)
            elif obj.name == "A_R3Tunnel":
                self.A_R3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "B_R3Tunnel":
                self.B_R3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R3_BSpawn":
                self.R3_BSpawn = (obj.x,obj.y)
            elif obj.name == "R3_BTunnel":
                self.R3_BTunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "B_R3Spawn":
                self.B_R3Spawn = (obj.x,obj.y)
            elif obj.name == "R3_CTunnel":
                self.R3_CTunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "C_R3Spawn":
                self.C_R3Spawn = (obj.x,obj.y)
            elif obj.name == "R3_CSpawn":
                self.R3_CSpawn = (obj.x,obj.y)
            elif obj.name == "C_R3Tunnel":
                self.C_R3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D_M3Tunnel":
                self.D_M3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "M3_DSpawn":
                self.M3_DSpawn = (obj.x,obj.y)
            elif obj.name == "D_M3Spawn":
                self.D_M3Spawn = (obj.x,obj.y)
            elif obj.name == "M3_DTunnel":
                self.M3_DTunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "F_M3Spawn":
                self.F_M3Spawn = (obj.x,obj.y)
            elif obj.name == "M3_FTunnel":
                self.M3_FTunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "M3_FSpawn":
                self.M3_FSpawn = (obj.x,obj.y)
            elif obj.name == "F_M3Tunnel":
                self.F_M3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "M3_ESpawn":
                self.M3_ESpawn = (obj.x,obj.y)
            elif obj.name == "E_M3Tunnel":
                self.E_M3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "E_M3Spawn":
                self.E_M3Spawn = (obj.x,obj.y)
            elif obj.name == "M3_ETunnel":
                self.M3_ETunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "G_M3Spawn":
                self.G_M3Spawn = (obj.x,obj.y)
            elif obj.name == "M3_GTunnel":
                self.M3_GTunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "G_M3Tunnel":
                self.G_M3Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "M3_GSpawn":self.M3_GSpawn = (obj.x,obj.y)
            elif obj.name == "Mt.Moon_R4Tunnel":
                self.MtMoon_R4Tunnel = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R4_Mt.MoonSpawn":self.R4_MtMoonSpawn = (obj.x,obj.y)

    def Load_CCH1(self):
        for layer in self.CCH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CCH1Camera))

        for obj in self.CCH1.objects:
            if obj.name == "Spawn1": self.O_InCCH1Spawn = (obj.x,obj.y)
            elif obj.name == "Spawn2":self.BY_CCH1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.InCCH1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Door2": self.InCCH1_BYDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CCH1Barriers.append(Rect)
            else:
                npc = NPC(obj.image,self.CCH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CCH1NPCS.append(npc)
                self.CCH1Barriers.append(npc.rect)
    
    def Load_CCH2(self):
        for layer in self.CCH2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CCH2Camera))

        for obj in self.CCH2.objects:
            if obj.name == "Spawn": self.O_CCH2Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CCH2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CCH2Barriers.append(Rect)
            elif obj.name == "Old Man":
                npc = TraderNPC(obj.image,self.CCH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.CCH2NPCS.append(npc)
                self.Traders.append(npc)
                self.CCH2Barriers.append(npc.rect)
            else:
                npc = NPC(obj.image,self.CCH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CCH2NPCS.append(npc)
                self.CCH2Barriers.append(npc.rect)
    
    def Load_Bike_Shop(self):
        for layer in self.Bike_Shop.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Bike_ShopCamera))

        for obj in self.Bike_Shop.objects:
            if obj.name == "Spawn": self.O_BikeShopSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.BikeShop_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.BikeShopBarriers.append(Rect)
            elif obj.name == "Desk":
                self.Bike_ShopDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.BikeShopBarriers.append(self.Bike_ShopDesk)
            else:
                npc = NPC(obj.image,self.Bike_ShopCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.BikeShopNPCS.append(npc)
                self.BikeShopBarriers.append(npc.rect)

    def Load_CeruleanGym(self):
        for layer in self.CCGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CCGymCamera))
        
        for obj in self.CCGym.objects:
            if obj.name == "Spawn": 
                self.O_CeruleanGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CeruleanGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CeruleanGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.CeruleanGymReadables.append(Read)
                self.CeruleanGymBarriers.append(Read.Rect)
            elif obj.name == "JR.TRAINER(FEMALE)":
                trainer = TrainerNPC("JR.TRAINER",obj.image,self.CCGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,"JR.TRAINER(FEMALE)")
                self.CeruleanGymTrainers.append(trainer)
                self.CeruleanGymBarriers.append(trainer.rect)
            elif obj.name == "Swimmer":
                trainer = TrainerNPC("Swimmer",obj.image,self.CCGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,"Swimmer")
                self.CeruleanGymTrainers.append(trainer)
                self.CeruleanGymBarriers.append(trainer.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.CeruleanGymTrainereyes.append(eyes)
            elif obj.name == "Misty":     
                self.Misty = GymLeaderNPC("Misty",obj.image,self.CCGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.CeruleanGymBarriers.append(self.Misty.rect)
            else:
                if obj.name == "Announcer":
                    npc = NPC(obj.image,self.CCGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.CeruleanGymNPCS.append(npc)
                    self.CeruleanGymBarriers.append(npc.rect)

    def Load_Sea_Cottage(self):
        for layer in self.Sea_Cottage.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Sea_CottageCamera))

        for obj in self.Sea_Cottage.objects:
            if obj.name == "Spawn": self.O_BillSpawn = (obj.x,obj.y)
            elif obj.name == "Spawn2": self.HelpBillSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.Bill_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Sea_CottageBarriers.append(Rect)
            else:
                npc = NPC(obj.image,self.Sea_CottageCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                if obj.name == "Bill":self.Sea_CottageCamera.remove(npc)
                else:self.Sea_CottageBarriers.append(npc.rect)
                self.SCNPCS.append(npc)

    def Load_RobbedHouse(self):
        for layer in self.Robbed_House.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Robbed_HouseCamera))

        for obj in self.Robbed_House.objects:
            if obj.name == "Spawn": self.O_RHSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.RH_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Robbed_HouseBarriers.append(Rect)
            elif obj.name == "Door2":self.RH_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Spawn2": self.O2_RHSpawn = (obj.x,obj.y)
            else:
                npc = NPC(obj.image,self.Robbed_HouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Robbed_HouseNPCS.append(npc)
                self.Robbed_HouseBarriers.append(npc.rect)
    
    def Load_DayCare(self):
        for layer in self.DayCare.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.DayCareCamera))

        for obj in self.DayCare.objects:
            if obj.name == "Spawn": self.O_DayCareSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.DayCare_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.DayCareBarriers.append(Rect)
            else:
                self.DaycareWorker = NPC(obj.image,self.DayCareCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.DayCareBarriers.append(self.DaycareWorker.rect)

    def Load_BetweenR5_SC(self):
        for layer in self.BetweenR5_SC.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.BetweenR5_SCCamera,self.BetweenR6_SCCamera))

        for obj in self.BetweenR5_SC.objects:
            if obj.name == "O_InterR5Spawn": self.O_InterEnteranceSpawn = (obj.x,obj.y)
            elif obj.name == "InterR5_ODoor": self.InterEnterance_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_InterExitSpawn": self.O_InterExitSpawn = (obj.x,obj.y)
            elif obj.name == "Exit": self.InterExit_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.BetweenR5_SCBarriers.append(Rect)
            elif obj.name == "Boundry":
                self.GuardBoundry = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Guard":
                npc = NPC(obj.image,(self.BetweenR5_SCCamera,self.BetweenR6_SCCamera),obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.BetweenR5_SCNPCS.append(npc)
                self.BetweenR5_SCBarriers.append(npc.rect)
            else:
                pass
  
    def Load_UnderGround_Entrance(self):
        for layer in self.UndergroundEntrance.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.UndergroundEntranceCamera,self.UndergroundSEntranceCamera))

        for obj in self.UndergroundEntrance.objects:
            if obj.name == "Spawn1": self.R5_UnderGESpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.UnderGE_R5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            if obj.name == "Spawn2": self.UnderGR_UnderGESpawn = (obj.x,obj.y)
            elif obj.name == "Door2": self.UnderGE_UnderGRDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.UndergroundEntranceBarriers.append(Rect)
                self.UndergroundSEntranceBarriers.append(Rect)
            elif obj.name == "Girl":
                npc = TraderNPC(obj.image,self.UndergroundEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.UndergroundEntranceNPCS.append(npc)
                self.Traders.append(npc)
                self.UndergroundEntranceBarriers.append(npc.rect)
            elif obj.name == "Woman":
                npc = NPC(obj.image,self.UndergroundSEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.UndergroundSEntranceNPCS.append(npc)
                self.UndergroundSEntranceBarriers.append(npc.rect)
    
    def Load_UnderGroundNSTunnel(self):
        for layer in self.UndergroundNSTunnel.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.UndergroundNSTunnelCamera))

        for obj in self.UndergroundNSTunnel.objects:
            if obj.name == "Spawn": self.UnderGE_UnderGNSTunnelSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.UnderGNSTunnel_UnderGEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Spawn2": self.UnderGSE_UnderGNSTunnelSpawn = (obj.x,obj.y)
            elif obj.name == "SDoor": self.UnderGNSTunnel_UnderGSEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.UGNSHiddenItems.append(H)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.UndergroundNSTunnelBarriers.append(Rect)

    def Load_VCH1(self):
        for layer in self.VCH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.VCH1Camera,self.VCH2Camera,self.VCH3Camera))

        for obj in self.VCH1.objects:
            if obj.name == "Spawn": self.O_VCH1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.VCH1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VCH1Barriers.append(Rect)
                self.VCH2Barriers.append(Rect)
                self.VCH3Barriers.append(Rect)
            elif obj.name == "Girl":
                npc = TraderNPC(obj.image,self.VCH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.VCH2NPCS.append(npc)
                self.Traders.append(npc)
                self.VCH2Barriers.append(npc.rect)
            elif obj.name in ("Pidgey","Boy"):
                npc = NPC(obj.image,self.VCH3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.VCH3NPCS.append(npc)
                self.VCH3Barriers.append(npc.rect)
            elif obj.name == "Note":
                Tile((obj.x,obj.y),obj.image,(self.VCH3Camera))
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,Text2=obj.Text2,Text3=obj.Text3)
                self.VCH3Readables.append(Read)
            else:
                npc = NPC(obj.image,self.VCH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Hello there, young one! How are the fish biting?",IA2="",IA3="")
                self.VCH1NPCS.append(npc)
                self.VCH1Barriers.append(npc.rect)
    
    def Load_PokemonFan_Club(self):
        for layer in self.PokemonFanClub.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.PokemonFanClubCamera))

        for obj in self.PokemonFanClub.objects:
            if obj.name == "Spawn": self.O_PFCSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PFC_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Poster":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,Text2=obj.Text2,Text3=obj.Text3)
                self.PokemonFanClubReadables.append(Read)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokemonFanClubBarriers.append(Rect)
            elif obj.name == "Chairman":
                self.PFCChairman = NPC(obj.image,self.PokemonFanClubCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PokemonFanClubBarriers.append(npc.rect)
            else:
                npc = NPC(obj.image,self.PokemonFanClubCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PokemonFanClubNPCS.append(npc)
                self.PokemonFanClubBarriers.append(npc.rect)
    
    def Load_SS_Anne(self):
        for layer in self.SS_Anne.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.SS_AnneF1Camera))
                    elif layer.name == "Floor1Rooms":Tile((x*32,y*32),surf,(self.SS_AnneF1RoomsCamera))
                    else:Tile((x*32,y*32),surf,(self.SS_AnneF1KitchenCamera))

        for obj in self.SS_Anne.objects:
            if obj.name == "Spawn": self.O_SS_AnneF1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.SS_AnneF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF1Barriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF1RoomsBarriers.append(Rect)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF1KitchenBarriers.append(Rect)
            elif obj.name == "SAF1_R1Door":self.SAF1_R1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R1Spawn": self.SAF1_R1Spawn = (obj.x,obj.y)
            elif obj.name == "R1_SAF1Spawn": self.R1_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.KitchenHiddenItems.append(H)
            elif obj.name == "R1_SAF1Door":self.R1_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R2Door":self.SAF1_R2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R2Spawn": self.SAF1_R2Spawn = (obj.x,obj.y)
            elif obj.name == "R2_SAF1Spawn": self.R2_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "R2_SAF1Door":self.R2_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R3Door":self.SAF1_R3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R3Spawn": self.SAF1_R3Spawn = (obj.x,obj.y)
            elif obj.name == "R3_SAF1Spawn": self.R3_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "R3_SAF1Door":self.R3_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R4Door":self.SAF1_R4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R4Spawn": self.SAF1_R4Spawn = (obj.x,obj.y)
            elif obj.name == "R4_SAF1Spawn": self.R4_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "R4_SAF1Door":self.R4_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R5Door":self.SAF1_R5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R5Spawn": self.SAF1_R5Spawn = (obj.x,obj.y)
            elif obj.name == "R5_SAF1Spawn": self.R5_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "R5_SAF1Door":self.R5_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R6Door":self.SAF1_R6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_R6Spawn": self.SAF1_R6Spawn = (obj.x,obj.y)
            elif obj.name == "R6_SAF1Spawn": self.R6_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "R6_SAF1Door":self.R6_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Kit_SAF1Spawn": self.Kit_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "SAF1_KitDoor":self.SAF1_KitDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF1_KSpawn": self.SAF1_KSpawn = (obj.x,obj.y)
            elif obj.name == "Kit_SAF1Door":self.Kit_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF0_SAF1Spawn": self.SAF0_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "SAF1_SAF0Door":self.SAF1_SAF0Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_SAF1Spawn": self.SAF2_SAF1Spawn = (obj.x,obj.y)
            elif obj.name == "SAF1_SAF2Door":self.SAF1_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.SS_AnneF1RoomsCamera,obj.Item)
                self.SS_AnneF1RoomsPickups.append(ball)
            elif obj.name in ("Man","Waiter"):
                npc = NPC(obj.image,self.SS_AnneF1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SS_AnneF1NPCS.append(npc)
                self.SS_AnneF1Barriers.append(npc.rect)
            elif obj.name == "Chef" or obj.name == "Worker":
                npc = NPC(obj.image,self.SS_AnneF1KitchenCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SS_AnneF1KitchenNPCS.append(npc)
                self.SS_AnneF1KitchenBarriers.append(npc.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.SS_AnneF1RoomsTrainereyes.append(eyes)
            elif "SAF1" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.SS_AnneF1RoomsCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.SS_AnneF1RoomsTrainers.append(trainer)
                self.SS_AnneF1RoomsBarriers.append(trainer.rect)
            elif "F1" in obj.name:
                npc = NPC(obj.image,self.SS_AnneF1RoomsCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],obj.Dialouge2,obj.Dialouge3)
                self.SS_AnneF1RoomsNPCs.append(npc)
                self.SS_AnneF1RoomsBarriers.append(npc.rect)
    
    def Load_SS_AnneF0(self):
        for layer in self.SS_AnneF0.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor0":Tile((x*32,y*32),surf,(self.SS_AnneF0Camera))
                    elif layer.name == "Floor0Rooms":Tile((x*32,y*32),surf,(self.SS_AnneF0RoomsCamera))

        for obj in self.SS_AnneF0.objects:
            if obj.name == "SAF1_SAF0Spawn": self.SAF1_SAF0Spawn = (obj.x,obj.y)
            elif obj.name == "SAF0_SAF1Door": self.SAF0_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF0Barriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF0RoomsBarriers.append(Rect)
            elif obj.name == "SAF0_R1Door":self.SAF0_R1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF0_R1Spawn": self.SAF0_R1Spawn = (obj.x,obj.y)
            elif obj.name == "R1_SAF0Door":self.R1_SAF0Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R1_SAF0Spawn": self.R1_SAF0Spawn = (obj.x,obj.y)
            elif obj.name == "SAF0_R2Door":self.SAF0_R2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SAF0RoomsHiddenItems.append(H)
            elif obj.name == "SAF0_R2Spawn": self.SAF0_R2Spawn = (obj.x,obj.y)
            elif obj.name == "R2_SAF0Door":self.R2_SAF0Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R2_SAF0Spawn": self.R2_SAF0Spawn = (obj.x,obj.y)
            elif obj.name == "SAF0_R3Door":self.SAF0_R3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF0_R3Spawn": self.SAF0_R3Spawn = (obj.x,obj.y)
            elif obj.name == "R3_SAF0Door":self.R3_SAF0Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R3_SAF0Spawn": self.R3_SAF0Spawn = (obj.x,obj.y)
            elif obj.name == "SAF0_R4Door":self.SAF0_R4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF0_R4Spawn": self.SAF0_R4Spawn = (obj.x,obj.y)
            elif obj.name == "R4_SAF0Door":self.R4_SAF0Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R4_SAF0Spawn": self.R4_SAF0Spawn = (obj.x,obj.y)
            elif obj.name == "SAF0_R5Door":self.SAF0_R5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF0_R5Spawn": self.SAF0_R5Spawn = (obj.x,obj.y)
            elif obj.name == "R5_SAF0Door":self.R5_SAF0Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R5_SAF0Spawn": self.R5_SAF0Spawn = (obj.x,obj.y)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.SS_AnneF0RoomsTrainereyes.append(eyes)
            elif "SAF0" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.SS_AnneF0RoomsCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.SS_AnneF0RoomsTrainers.append(trainer)
                self.SS_AnneF0RoomsBarriers.append(trainer.rect)
            elif "F0" in obj.name:
                npc = NPC(obj.image,self.SS_AnneF0RoomsCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],obj.Dialouge2,obj.Dialouge3)
                self.SS_AnneF0RoomsNPCs.append(npc)
                self.SS_AnneF0RoomsBarriers.append(npc.rect)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.SS_AnneF0RoomsCamera,obj.Item)
                self.SS_AnneF0RoomsPickups.append(ball)
    
    def Load_SS_AnneF2(self):
        for layer in self.SS_AnneF2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor2":Tile((x*32,y*32),surf,(self.SS_AnneF2Camera))
                    elif layer.name == "Floor2Rooms":Tile((x*32,y*32),surf,(self.SS_AnneF2RoomsCamera))
                    else:Tile((x*32,y*32),surf,(self.SS_AnneF2CaptainCamera))

        for obj in self.SS_AnneF2.objects:
            if obj.name == "SAF1_SAF2Spawn": self.SAF1_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_SAF1Door": self.SAF2_SAF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF2Barriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF2RoomsBarriers.append(Rect)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF2CaptainBarriers.append(Rect)
            elif obj.name == "HW_SAF2Spawn": self.HW_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_HWDoor": self.SAF2_HWDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R1_SAF2Spawn": self.R1_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_R1Door": self.SAF2_R1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_R1Spawn": self.SAF2_R1Spawn = (obj.x,obj.y)
            elif obj.name == "R1_SAF2Door": self.R1_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R2_SAF2Spawn": self.R2_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_R2Door": self.SAF2_R2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_R2Spawn": self.SAF2_R2Spawn = (obj.x,obj.y)
            elif obj.name == "R2_SAF2Door": self.R2_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R3_SAF2Spawn": self.R3_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_R3Door": self.SAF2_R3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_R3Spawn": self.SAF2_R3Spawn = (obj.x,obj.y)
            elif obj.name == "R3_SAF2Door": self.R3_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R4_SAF2Spawn": self.R4_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_R4Door": self.SAF2_R4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_R4Spawn": self.SAF2_R4Spawn = (obj.x,obj.y)
            elif obj.name == "R4_SAF2Door": self.R4_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R5_SAF2Spawn": self.R5_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_R5Door": self.SAF2_R5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_R5Spawn": self.SAF2_R5Spawn = (obj.x,obj.y)
            elif obj.name == "R5_SAF2Door": self.R5_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R6_SAF2Spawn": self.R6_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_R6Door": self.SAF2_R6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SAF2_R6Spawn": self.SAF2_R6Spawn = (obj.x,obj.y)
            elif obj.name == "R6_SAF2Door": self.R6_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CC_SAF2Spawn": self.CC_SAF2Spawn = (obj.x,obj.y)
            elif obj.name == "SAF2_CCDoor": self.SAF2_CCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Spawn": self.SAF2_CCSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CC_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.SS_AnneF2RoomsCamera,obj.Item)
                self.SS_AnneF2RoomsPickups.append(ball)
            elif obj.name == "Captain":
                self.SSCaptain = NPC(obj.image,self.SS_AnneF2CaptainCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SS_AnneF2CaptainBarriers.append(self.SSCaptain.rect)
            elif obj.name == "Man":
                npc = NPC(obj.image,self.SS_AnneF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SS_AnneF2NPCS.append(npc)
                self.SS_AnneF2Barriers.append(npc.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.SS_AnneF2RoomsTrainereyes.append(eyes)
            elif "SAF2" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.SS_AnneF2RoomsCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.SS_AnneF2RoomsTrainers.append(trainer)
                self.SS_AnneF2RoomsBarriers.append(trainer.rect)
            elif "F2" in obj.name:
                npc = NPC(obj.image,self.SS_AnneF2RoomsCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],obj.Dialouge2,obj.Dialouge3)
                self.SS_AnneF2RoomsNPCs.append(npc)
                self.SS_AnneF2RoomsBarriers.append(npc.rect)
            elif obj.name == "Battle":
                self.SSBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Spot":
                self.SSBattleSpot = (obj.x,obj.y)
   
    def Load_SS_AnneF3(self):
        for layer in self.SS_AnneF3.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Hallway":Tile((x*32,y*32),surf,(self.SS_AnneF3HallWayCamera))
                    else:Tile((x*32,y*32),surf,(self.SS_AnneF3Camera))

        for obj in self.SS_AnneF3.objects:
            if obj.name == "SAF2_HWSpawn": self.SAF2_HWSpawn = (obj.x,obj.y)
            elif obj.name == "HW_SAF2Door": self.HW_SAF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Worker":
                npc = NPC(obj.image,self.SS_AnneF3HallWayCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SS_AnneF3HallWayNPCS.append(npc)
                self.SS_AnneF3HallWayBarriers.append(npc.rect)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF3HallWayBarriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SS_AnneF3Barriers.append(Rect)
            elif obj.name == "SAF3_HWSpawn": self.SAF3_HWSpawn = (obj.x,obj.y)
            elif obj.name == "HW_SAF3Door": self.HW_SAF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "HW_SAF3Spawn": self.HW_SAF3Spawn = (obj.x,obj.y)
            elif obj.name == "SAF3_HWDoor": self.SAF3_HWDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.SS_AnneF3Trainereyes.append(eyes)
            elif "SAF3" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.SS_AnneF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.SS_AnneF3Trainers.append(trainer)
                self.SS_AnneF3Barriers.append(trainer.rect)
            elif "F3" in obj.name:
                npc = NPC(obj.image,self.SS_AnneF3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],obj.Dialouge2,obj.Dialouge3)
                self.SS_AnneF3NPCs.append(npc)
                self.SS_AnneF3Barriers.append(npc.rect)

    def Load_VermilionGym(self):
        for layer in self.VCGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.VCGymCamera))
        
        for obj in self.VCGym.objects:
            if obj.name == "Spawn": 
                self.O_VCSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.VC_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Doors": 
                self.VCDoors = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text)
                self.VermilionGymBarriers.append(self.VCDoors.Rect)
                self.VermilionGymReadables.append(self.VCDoors)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VermilionGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.VermilionGymReadables.append(Read)
                self.VermilionGymBarriers.append(Read.Rect)
            elif obj.name == "Trashcan":
                Tile((obj.x,obj.y),obj.image,(self.VCGymCamera))
                can = SecretTrashcans(obj.x,obj.y,obj.width,obj.height)
                self.VermilionGymBarriers.append(can.Rect)
                self.ThirdGymTrashcans.append(can)
            elif "VC" in obj.name:
                trainer = TrainerNPC(obj.name[2:],obj.image,self.VCGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.VermilionGymTrainers.append(trainer)
                self.VermilionGymBarriers.append(trainer.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.VermilionGymTrainereyes.append(eyes)
            elif obj.name == "Lt.Surge":     
                self.Surge = GymLeaderNPC("Lt.Surge",obj.image,self.VCGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3,obj.Dialouge4],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.VermilionGymBarriers.append(self.Surge.rect)
            else:
                if obj.name == "Dude":
                    npc = NPC(obj.image,self.VCGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                    self.VermilionGymCNPCS.append(npc)
                    self.VermilionGymBarriers.append(npc.rect)

    def Load_DiglettCave(self):
        for layer in self.DiglettCave.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "R11Entrance":Tile((x*32,y*32),surf,(self.DiglettCaveEntranceCamera,self.DiglettCaveExitCamera))
                    else:Tile((x*32,y*32),surf,(self.DiglettCaveCamera))

        for obj in self.DiglettCave.objects:
            if obj.name == "R11_DCESpawn": self.R11_DCESpawn = (obj.x,obj.y)
            elif obj.name == "DCE_R11Door": self.DCE_R11Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "DC_DCESpawn": self.DC_DCESpawn = (obj.x,obj.y)
            elif obj.name == "DCE_DCDoor": self.DCE_DCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "DCE_DCSpawn": self.DCE_DCSpawn = (obj.x,obj.y)
            elif obj.name == "DC_DCEDoor": self.DC_DCEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "2DCE_DCSpawn": self.DCExit_DCSpawn = (obj.x,obj.y)
            elif obj.name == "DC_2DCEDoor": self.DC_2DCEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.DiglettCaveEntranceBarriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.DiglettCaveBarriers.append(Rect)
            elif obj.name == "Rocks":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.DiglettCaveRocks.append(Rock)
            elif obj.name == "Man":
                npc = NPC(obj.image,self.DiglettCaveEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.DiglettCaveEntranceNPCS.append(npc)
                self.DiglettCaveEntranceBarriers.append(npc.rect)
            elif obj.name == "Guy":
                npc = NPC(obj.image,self.DiglettCaveExitCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.DiglettCaveExitNPCS.append(npc)
                self.DiglettCaveEntranceBarriers.append(npc.rect)
    
    def Load_R21H(self):
        for layer in self.R21H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.R21HCamera))

        for obj in self.R21H.objects:
            if obj.name == "Spawn": self.O_R21HSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.R21H_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R21HBarriers.append(Rect)
            elif obj.name == "Boy":
                npc = TraderNPC(obj.image,self.R21HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.R21NPCS.append(npc)
                self.Traders.append(npc)
                self.R21HBarriers.append(npc.rect)
            else:
                npc = NPC(obj.image,self.R21HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R21NPCS.append(npc)
                self.R21HBarriers.append(npc.rect)
    
    def Load_R22H(self):
        for layer in self.R22H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.R22HCamera))

        for obj in self.R22H.objects:
            if obj.name == "Spawn": self.VO_R22HSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.R22H_VODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Spawn2": self.PO_R22HSpawn = (obj.x,obj.y)
            elif obj.name == "Door2": self.R22H_PODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R22HBarriers.append(Rect)
            elif obj.name == "Aide":
                self.R22HAide = NPC(obj.image,self.R22HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R22HBarriers.append(self.R22HAide.rect)
            else:
                npc = NPC(obj.image,self.R22HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R22NPCS.append(npc)
                self.R22HBarriers.append(npc.rect)
    
    def Load_R11H(self):
        for layer in self.R11H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.R11HCamera))
                    else:Tile((x*32,y*32),surf,(self.R11F2HCamera))

        for obj in self.R11H.objects:
            if obj.name == "VCO_R11HSpawn": self.VCO_R11HSpawn = (obj.x,obj.y)
            elif obj.name == "R11H_VCODoor": self.R11H_VCODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R11H_R12Door": self.R11H_R12Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R12_R11HSpawn": self.R12_R11HSpawn = (obj.x,obj.y)
            elif obj.name == "R11H_R11HF2Door": self.R11H_R11HF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R11HF2_R11HSpawn": self.R11HF2_R11HSpawn = (obj.x,obj.y)
            elif obj.name == "R11HF2_R11HDoor": self.R11HF2_R11HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R11H_R11HF2Spawn": self.R11H_R11HF2Spawn = (obj.x,obj.y)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R11HBarriers.append(Rect)
            elif obj.name == "Scope":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.R11HF2Readables.append(Read)
                self.R11HF2Barriers.append(Read.Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R11HF2Barriers.append(Rect)
            elif obj.name == "Desk": 
                self.R11HDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R11HBarriers.append(self.R11HDesk)
            elif obj.name == "Boy":
                npc = TraderNPC(obj.image,self.R11F2HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.R112NPCS.append(npc)
                self.Traders.append(npc)
                self.R11HF2Barriers.append(npc.rect)
            elif obj.name == "Aide":
                self.R11HAide = NPC(obj.image,self.R11F2HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R11HF2Barriers.append(self.R11HAide.rect)
            elif obj.name == "Guard":
                npc = NPC(obj.image,self.R11HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R111HNPCS.append(npc)
                self.R11HBarriers.append(npc.rect)
    
    def Load_Rock_Tunnel(self):
        for layer in self.Rock_Tunnel.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1(Light)":Tile((x*32,y*32),surf,(self.Rock_TunnelF1LightCamera))
                    elif layer.name == "Floor1(Dark)":Tile((x*32,y*32),surf,(self.Rock_TunnelF1DarkCamera))
                    elif layer.name == "Floor 2(Light)":Tile((x*32,y*32),surf,(self.Rock_TunnelF2LightCamera))
                    elif layer.name == "Floor 2(Dark)":Tile((x*32,y*32),surf,(self.Rock_TunnelF2DarkCamera))

        for obj in self.Rock_Tunnel.objects:
            if obj.name == "O_RTF1Spawn": self.O_RTF1Spawn = (obj.x,obj.y)
            elif obj.name == "RTF1_ODoor":self.RTF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "A_RTF1Spawn": self.A_RTF1Spawn = (obj.x,obj.y)
            elif obj.name == "RTF1_ADoor":self.RTF1_ADoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "B_RTF1Spawn": self.B_RTF1Spawn = (obj.x,obj.y)
            elif obj.name == "RTF1_BDoor":self.RTF1_BDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "C_RTF1Spawn": self.C_RTF1Spawn = (obj.x,obj.y)
            elif obj.name == "RTF1_CDoor":self.RTF1_CDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D_RTF1Spawn": self.D_RTF1Spawn = (obj.x,obj.y)
            elif obj.name == "RTF1_DDoor":self.RTF1_DDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Exit_RTF1Spawn": self.Exit_RTF1Spawn = (obj.x,obj.y)
            elif obj.name == "RTF1_ExitDoor":self.RTF1_ExitDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RTF1_ASpawn": self.RTF1_ASpawn = (obj.x,obj.y)
            elif obj.name == "A_RTF1Door":self.A_RTF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RTF1_BSpawn": self.RTF1_BSpawn = (obj.x,obj.y)
            elif obj.name == "B_RTF1Door":self.B_RTF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RTF1_CSpawn": self.RTF1_CSpawn = (obj.x,obj.y)
            elif obj.name == "C_RTF1Door":self.C_RTF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RTF1_DSpawn": self.RTF1_DSpawn = (obj.x,obj.y)
            elif obj.name == "D_RTF1Door":self.D_RTF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Rocks":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Rock_TunnelF1WildBlocks.append(WildTile)
            elif obj.name == "Rocks2":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Rock_TunnelF2WildBlocks.append(WildTile)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Rock_TunnelF1Barriers.append(Rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Rock_TunnelF2Barriers.append(Rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Rock_TunnelF1Trainereyes.append(eyes)
            elif obj.name == "Eyes2":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Rock_TunnelF2Trainereyes.append(eyes)
            elif "RTF1" in obj.name:
                if "JR.TRAINER" not in obj.name:
                    trainer = TrainerNPC(obj.name[5:],obj.image,self.Rock_TunnelF1LightCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.Rock_TunnelF1Trainers.append(trainer)
                    self.Rock_TunnelF1Barriers.append(trainer.rect)
                else:
                    trainer = TrainerNPC("JR.TRAINER",obj.image,self.Rock_TunnelF1LightCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.Rock_TunnelF1Trainers.append(trainer)
                    self.Rock_TunnelF1Barriers.append(trainer.rect)         
            elif "RTF2" in obj.name:
                if "JR.TRAINER" not in obj.name:
                    trainer = TrainerNPC(obj.name[5:],obj.image,self.Rock_TunnelF2LightCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.Rock_TunnelF2Trainers.append(trainer)
                    self.Rock_TunnelF2Barriers.append(trainer.rect)
                else:
                    trainer = TrainerNPC("JR.TRAINER",obj.image,self.Rock_TunnelF2LightCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.Rock_TunnelF2Trainers.append(trainer)
                    self.Rock_TunnelF2Barriers.append(trainer.rect)
            
    def Load_LTVolunteerHouse(self):
        for layer in self.LTVolunteerHouse.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.LTVolunteerHouseCamera))

        for obj in self.LTVolunteerHouse.objects:
            if obj.name == "O_LTVHSpawn": self.O_LTVHSpawn = (obj.x,obj.y)
            elif obj.name == "LTVH_ODoor": self.LTVH_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.LTVolunteerHouseBarriers.append(Rect)
            elif obj.name == "Booklet":
                Tile((obj.x,obj.y),obj.image,(self.LTVolunteerHouseCamera))
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,Text2=obj.Text2,Text3=obj.Text3)
                self.LTVolunteerHouseReadables.append(Read)
            elif obj.name == "Mr.Fuji":
                self.LTVHMr_Fuji = NPC(obj.image,self.LTVolunteerHouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Has my FLUTE helped you?",IA2="",IA3="")
            else:
                npc = NPC(obj.image,self.LTVolunteerHouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.LTVolunteerHouseNPCS.append(npc)
                self.LTVolunteerHouseBarriers.append(npc.rect)
    
    def Load_LT1H(self):
        for layer in self.LT1H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.LT1HCamera,self.LT2HCamera))

        for obj in self.LT1H.objects:
            if obj.name == "Spawn": self.O_LTHSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.LTH_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.LT1HBarriers.append(Rect)
                self.LT2HBarriers.append(Rect)
            elif obj.name == "Name Rater":
                self.Name_Rater = NPC(obj.image,self.LT2HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.LT2HBarriers.append(self.Name_Rater.rect)
            else:
                npc = NPC(obj.image,self.LT1HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.LT1HNPCS.append(npc)
                self.LT1HBarriers.append(npc.rect)
    
    def Load_SaffronEWEntrance(self):
        for layer in self.SaffronEWEntrance.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SaffronEEntranceCamera))

        for obj in self.SaffronEWEntrance.objects:
            if obj.name == "O_EntranceSpawn": self.O_SaffronEEntranceSpawn = (obj.x,obj.y)
            elif obj.name == "Entrance": self.SaffronEEntrance_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_ExitSpawn": self.O_SaffronWExitSpawn = (obj.x,obj.y)
            elif obj.name == "Exit": self.SaffronWExit_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SaffronEEntranceBarriers.append(Rect)
            elif obj.name == "Boundry":
                self.EWGuardBoundry = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Guard":
                npc = NPC(obj.image,(self.SaffronEEntranceCamera),obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SaffronEWEntranceNPCS.append(npc)
                self.SaffronEEntranceBarriers.append(npc.rect)
            else:
                pass
  
    def Load_UnderGroundWE_Entrance(self):
        for layer in self.Underground_EWEntrance.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Underground_EEntranceCamera,self.Underground_WEntranceCamera))

        for obj in self.Underground_EWEntrance.objects:
            if obj.name == "Spawn1": self.O_UnderWEGESpawn = (obj.x,obj.y)
            elif obj.name == "Outside": self.UnderWEGE_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Spawn2": self.WETunnel_UnderGESpawn = (obj.x,obj.y)
            elif obj.name == "Tunnel": self.UnderGE_WETunnelDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Underground_EEntranceBarriers.append(Rect)
                self.Underground_WEntranceBarriers.append(Rect)
            elif obj.name == "Woman":
                npc = NPC(obj.image,self.Underground_EEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Underground_EEntranceNPCS.append(npc)
                self.Underground_EEntranceBarriers.append(npc.rect)
            elif obj.name == "Man":
                npc = NPC(obj.image,self.Underground_WEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Underground_WEntranceNPCS.append(npc)
                self.Underground_WEntranceBarriers.append(npc.rect)
    
    def Load_UnderGroundWETunnel(self):
        for layer in self.Underground_WETunnel.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Underground_WETunnelCamera))

        for obj in self.Underground_WETunnel.objects:
            if obj.name == "ESpawn": self.UnderGE_UnderGWETunnelSpawn = (obj.x,obj.y)
            elif obj.name == "EastEntrance": self.UnderGWETunnel_UnderGEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "WSpawn": self.UnderGWE_UnderGWETunnelSpawn = (obj.x,obj.y)
            elif obj.name == "WestEntrance": self.UnderGWETunnel_UnderGWEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.UGWEHiddenItems.append(H)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Underground_WETunnelBarriers.append(Rect)

    def Load_Game_Corner(self):
        for layer in self.Game_Corner.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Normal":Tile((x*32,y*32),surf,(self.Game_CornerNormalCamera))
                    else:Tile((x*32,y*32),surf,(self.Game_CornerSecretCamera))

        for obj in self.Game_Corner.objects:
            if obj.name == "O_GCSpawn": self.O_GCSpawn = (obj.x,obj.y)
            elif obj.name == "GC_ODoor": self.GC_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Game_CornerBarriers.append(Rect)
            elif obj.name == "Machine":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.Game_CornerReadables.append(Read)
                self.Game_CornerBarriers.append(Read.Rect)
            elif obj.name == "Employee":
                self.Game_CornerTrader = NPC(obj.image,(self.Game_CornerNormalCamera,self.Game_CornerSecretCamera),obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Game_CornerBarriers.append(self.Game_CornerTrader.rect)
            elif obj.name == "Desk":
                self.Game_CornerTradeDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Game_CornerBarriers.append(self.Game_CornerTradeDesk)
            elif obj.name == "Rocket":
                self.GCRocket = TrainerNPC("Rocket",obj.image,(self.Game_CornerNormalCamera),(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,"Rocket")
                self.Game_CornerBarriers.append(self.GCRocket.rect)
            elif obj.name == "Lever":
                self.GCLever = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,"Sign",obj.Text2,obj.Text3)
                self.Game_CornerBarriers.append(self.GCLever.Rect)
            elif obj.name == "RocketBaseF1_GCSpawn": self.RocketBaseF1_GCSpawn = (obj.x,obj.y)
            elif obj.name == "GC_RocketBaseF1Door": self.GC_RocketBaseF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Desk2":
                self.Game_CornerWorkerDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Game_CornerBarriers.append(self.Game_CornerWorkerDesk)
            else:
                npc = NPC(obj.image,(self.Game_CornerNormalCamera,self.Game_CornerSecretCamera),obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Game_CornerNPCS.append(npc)
                self.Game_CornerBarriers.append(npc.rect)
    
    def Load_Prize_Booth(self):
        for layer in self.Prize_Booth.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Prize_BoothCamera))

        for obj in self.Prize_Booth.objects:
            if obj.name == "Spawn": self.O_PrizeBoothSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.PrizeBooth_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Prize_BoothBarriers.append(Rect)
            elif obj.name == "Booth1":
                self.Booth1 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Prize_BoothBarriers.append(self.Booth1)
            elif obj.name == "Booth2":
                self.Booth2 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Prize_BoothBarriers.append(self.Booth2)
            elif obj.name == "Booth3":
                self.Booth3 = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Prize_BoothBarriers.append(self.Booth3)
            else:
                npc = NPC(obj.image,self.Prize_BoothCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Prize_BoothNPCS.append(npc)
                self.Prize_BoothBarriers.append(npc.rect)
    
    def Load_CERestourant(self):
        for layer in self.CERestourant.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CERestourantCamera))

        for obj in self.CERestourant.objects:
            if obj.name == "Spawn": self.O_CERestourantSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CERestourant_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CERestourantBarriers.append(Rect)
            elif obj.name == "MaidDesk":
                self.MaidDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CERestourantBarriers.append(self.MaidDesk)
            elif obj.name == "ChefDesk":
                self.ChefDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CERestourantBarriers.append(self.ChefDesk)
            elif obj.name == "DMan":
                self.CoinMan = NPC(obj.image,self.CERestourantCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Man",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="I always thought I was going to win it back...",IA2="",IA3="")
                self.CERestourantNPCS.append(self.CoinMan)
                self.CERestourantBarriers.append(self.CoinMan.rect)
            else:
                npc = NPC(obj.image,self.CERestourantCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CERestourantNPCS.append(npc)
                self.CERestourantBarriers.append(npc.rect)
    
    def Load_CE1H(self):
        for layer in self.CE1H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CE1HCamera))

        for obj in self.CE1H.objects:
            if obj.name == "Spawn": self.O_CE1HSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CE1H_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CE1HBarriers.append(Rect)
            else:
                npc = NPC(obj.image,self.CE1HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CE1HNPCS.append(npc)
                self.CE1HBarriers.append(npc.rect)
    
    def Load_CE2H(self):
        for layer in self.CE2H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CE2HCamera))

        for obj in self.CE2H.objects:
            if obj.name == "Spawn": self.O_CE2HSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CE2H_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Rect":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CE2HBarriers.append(Rect)
            elif obj.name == "Desk":
                self.CE2HDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CE2HBarriers.append(self.CE2HDesk)
            else:
                npc = NPC(obj.image,self.CE2HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CE2HNPCS.append(npc)
                self.CE2HBarriers.append(npc.rect)
    
    def Load_CEMansion(self):
        for layer in self.CEMansion.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.CEMansionF1Camera))
                    elif layer.name == "Floor2":Tile((x*32,y*32),surf,(self.CEMansionF2Camera))
                    elif layer.name == "Floor3":Tile((x*32,y*32),surf,(self.CEMansionF3Camera))
                    elif layer.name == "Floor4":Tile((x*32,y*32),surf,(self.CEMansionF4Camera))
                    elif layer.name == "Floor4House":Tile((x*32,y*32),surf,(self.CEMansionF4HouseCamera))

        for obj in self.CEMansion.objects:
            if obj.name == "O_CEMF1Spawn": self.O_CEMF1Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF1_ODoor": self.CEMF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEMF1Barriers.append(Rect)
            elif obj.name == "CEMF2_CEMF1Spawn": self.CEMF2_CEMF1Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF1_CEMF2Door": self.CEMF1_CEMF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_BCEMF1Spawn": self.O_BCEMF1Spawn = (obj.x,obj.y)
            elif obj.name == "BCEMF1_ODoor": self.BCEMF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF1_BCEMF2Door": self.BCEMF1_BCEMF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 2
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEMF2Barriers.append(Rect)
            elif obj.name == "CEMF1_CEMF2Spawn": self.CEMF1_CEMF2Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF2_CEMF1Door": self.CEMF2_CEMF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF1_BCEMF2Spawn": self.BCEMF1_BCEMF2Spawn = (obj.x,obj.y)
            elif obj.name == "BCEMF2_BCEMF1Door": self.BCEMF2_BCEMF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEMF3_CEMF2Spawn": self.CEMF3_CEMF2Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF2_CEMF3Door": self.CEMF2_CEMF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF2_BCEMF3Door": self.BCEMF2_BCEMF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif "F1" in obj.name:
                npc = NPC(obj.image,self.CEMansionF1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEMF1NPCS.append(npc)
                self.CEMF1Barriers.append(npc.rect)
            #Floor 3
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEMF3Barriers.append(Rect)
            elif obj.name == "CEMF2_CEMF3Spawn": self.CEMF2_CEMF3Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF3_CEMF2Door": self.CEMF3_CEMF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF3_BCEMF2Door": self.BCEMF3_BCEMF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEMF4_CEMF3Spawn": self.CEMF4_CEMF3Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF3_CEMF4Door": self.CEMF3_CEMF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF4_BCEMF3Spawn": self.BCEMF4_BCEMF3Spawn = (obj.x,obj.y)
            elif obj.name == "BCEMF3_BCEMF4Door": self.BCEMF3_BCEMF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Creator":
                self.Creator = TrainerNPC(obj.name,obj.image,self.CEMansionF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.CEMF3Barriers.append(self.Creator.rect)
            #Floor 4
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEMF4Barriers.append(Rect)
            elif obj.name == "CEMF3_CEMF4Spawn": self.CEMF3_CEMF4Spawn = (obj.x,obj.y)
            elif obj.name == "CEMF4_CEMF3Door": self.CEMF4_CEMF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF3_BCEMF4Spawn": self.BCEMF3_BCEMF4Spawn = (obj.x,obj.y)
            elif obj.name == "BCEMF4_BCEMF3Door": self.BCEMF4_BCEMF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BCEMF4H_BCEMF4Spawn": self.BCEMF4H_BCEMF4Spawn = (obj.x,obj.y)
            elif obj.name == "BCEMF4_BCEMF4HDoor": self.BCEMF4_BCEMF4HDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor4House
            elif obj.name == "Border5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEMF4HouseBarriers.append(Rect)
            elif obj.name == "BCEMF4_BCEMF4HSpawn": self.BCEMF4_BCEMF4HSpawn = (obj.x,obj.y)
            elif obj.name == "BCEMF4H_BCEMF4Door": self.BCEMF4H_BCEMF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Man":
                npc = NPC(obj.image,self.CEMansionF4HouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEMF4HNPCS.append(npc)
                self.CEMF4HouseBarriers.append(npc.rect)
            elif obj.name == "Ball":self.F4Eevee = Tile((obj.x,obj.y),obj.image,(self.CEMansionF4HouseCamera))

    def Load_CEStore(self):
        for layer in self.CEStore.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.CEStoreF1Camera))
                    elif layer.name == "Floor2":Tile((x*32,y*32),surf,(self.CEStoreF2Camera))
                    elif layer.name == "Floor3":Tile((x*32,y*32),surf,(self.CEStoreF3Camera))
                    elif layer.name == "Floor4":Tile((x*32,y*32),surf,(self.CEStoreF4Camera))
                    elif layer.name == "Floor5":Tile((x*32,y*32),surf,(self.CEStoreF5Camera))
                    elif layer.name == "Elevator":Tile((x*32,y*32),surf,(self.CEStoreElevatorCamera))
                    elif layer.name == "Rooftop":Tile((x*32,y*32),surf,(self.CEStoreRooftopCamera))

        for obj in self.CEStore.objects:
            if obj.name == "O_CEStoreF1RightSpawn": self.O_CEStoreF1RightSpawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF1Right_ODoor": self.CEStoreF1Right_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_CEStoreF1LeftSpawn": self.O_CEStoreF1LeftSpawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF1Left_ODoor": self.CEStoreF1Left_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF2_CEStoreF1Spawn": self.CEStoreF2_CEStoreF1Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF1_CEStoreF2Door": self.CEStoreF1_CEStoreF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF1_ElevatorDoor":self.CEStoreF1_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Elevator_CEStoreF1Spawn": self.Elevator_CEStoreF1Spawn = (obj.x,obj.y)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF1Barriers.append(Rect)
            elif obj.name == "F1Desk":
                self.F1Desk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF1Barriers.append(self.F1Desk)
            elif obj.name == "F1Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name[2:],obj.Text2,obj.Text3)
                self.CEStoreF1Readables.append(Read)
                self.CEStoreF1Barriers.append(Read.Rect)
            elif obj.name == "F1Woman":
                npc = NPC(obj.image,self.CEStoreF1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEStoreF1NPCS.append(npc)
                self.CEStoreF1Barriers.append(npc.rect)
            #Floor 2
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF2Barriers.append(Rect)
            elif obj.name == "CEStoreF2_CEStoreF1Door": self.CEStoreF2_CEStoreF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF1_CEStoreF2Spawn": self.CEStoreF1_CEStoreF2Spawn = (obj.x,obj.y)
            elif obj.name == "F2RightDesk":
                self.F2RightDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF2Barriers.append(self.F2RightDesk)
            elif obj.name == "F2LeftDesk":
                self.F2LeftDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF2Barriers.append(self.F2LeftDesk)
            elif obj.name == "CEStoreF2_ElevatorDoor":self.CEStoreF2_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Elevator_CEStoreF2Spawn": self.Elevator_CEStoreF2Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF2_CEStoreF3Door": self.CEStoreF2_CEStoreF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF3_CEStoreF2Spawn": self.CEStoreF3_CEStoreF2Spawn = (obj.x,obj.y)
            elif obj.name == "F2Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name[2:],obj.Text2,obj.Text3)
                self.CEStoreF2Readables.append(Read)
                self.CEStoreF2Barriers.append(Read.Rect)
            #Floor 3
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF3Barriers.append(Rect)
            elif obj.name == "CEStoreF3_CEStoreF2Door": self.CEStoreF3_CEStoreF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF2_CEStoreF3Spawn": self.CEStoreF2_CEStoreF3Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF3_ElevatorDoor":self.CEStoreF3_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Elevator_CEStoreF3Spawn": self.Elevator_CEStoreF3Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF3_CEStoreF4Door": self.CEStoreF3_CEStoreF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF4_CEStoreF3Spawn": self.CEStoreF4_CEStoreF3Spawn = (obj.x,obj.y)
            elif obj.name == "F3Worker":
                self.CounterMan = NPC(obj.image,self.CEStoreF3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Man",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="TM18 is COUNTER! Not like the one I'm leaning on, mind you!",IA2="",IA3="")
                self.CEStoreF3NPCS.append(self.CounterMan)
                self.CEStoreF3Barriers.append(self.CounterMan.rect)
            elif obj.name == "F3Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name[2:],obj.Text2,obj.Text3)
                self.CEStoreF3Readables.append(Read)
                self.CEStoreF3Barriers.append(Read.Rect)
            elif obj.name == "F3Desk":
                self.F3Desk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF3Barriers.append(self.F3Desk)
            #Floor 4
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF4Barriers.append(Rect)
            elif obj.name == "CEStoreF4_CEStoreF3Door": self.CEStoreF4_CEStoreF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF3_CEStoreF4Spawn": self.CEStoreF3_CEStoreF4Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF4_CEStoreF5Door": self.CEStoreF4_CEStoreF5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF5_CEStoreF4Spawn": self.CEStoreF5_CEStoreF4Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF4_ElevatorDoor":self.CEStoreF4_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Elevator_CEStoreF4Spawn": self.Elevator_CEStoreF4Spawn = (obj.x,obj.y)
            elif obj.name == "F4Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name[2:],obj.Text2,obj.Text3)
                self.CEStoreF4Readables.append(Read)
                self.CEStoreF4Barriers.append(Read.Rect)
            elif obj.name == "F4Desk":
                self.F4Desk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF4Barriers.append(self.F4Desk)
            #Floor5
            elif obj.name == "Border5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF5Barriers.append(Rect)
            elif obj.name == "CEStoreF5_CEStoreF4Door": self.CEStoreF5_CEStoreF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF4_CEStoreF5Spawn": self.CEStoreF4_CEStoreF5Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF5_CEStoreRoofDoor": self.CEStoreF5_CEStoreRoofDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreRoof_CEStoreF5Spawn": self.CEStoreRoof_CEStoreF5Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreF5_ElevatorDoor":self.CEStoreF5_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Elevator_CEStoreF5Spawn": self.Elevator_CEStoreF5Spawn = (obj.x,obj.y)
            elif obj.name == "CEStoreRoof_CEStoreF5Door": self.CEStoreRoof_CEStoreF5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CEStoreF5_CEStoreRoofSpawn": self.CEStoreF5_CEStoreRoofSpawn = (obj.x,obj.y)
            elif obj.name == "F5Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name[2:],obj.Text2,obj.Text3)
                self.CEStoreF5Readables.append(Read)
                self.CEStoreF5Barriers.append(Read.Rect)
            elif obj.name == "F5RightDesk":
                self.F5RightDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF5Barriers.append(self.F5RightDesk)
            elif obj.name == "F5LeftDesk":
                self.F5LeftDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreF5Barriers.append(self.F5LeftDesk)
            elif "F2" in obj.name:
                npc = NPC(obj.image,self.CEStoreF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEStoreF2NPCS.append(npc)
                self.CEStoreF2Barriers.append(npc.rect)
            elif "F3" in obj.name:
                npc = NPC(obj.image,self.CEStoreF3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEStoreF3NPCS.append(npc)
                self.CEStoreF3Barriers.append(npc.rect)
            elif "F4" in obj.name:
                npc = NPC(obj.image,self.CEStoreF4Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEStoreF4NPCS.append(npc)
                self.CEStoreF4Barriers.append(npc.rect)
            elif "F5" in obj.name:
                npc = NPC(obj.image,self.CEStoreF5Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEStoreF5NPCS.append(npc)
                self.CEStoreF5Barriers.append(npc.rect)
            elif obj.name == "BorderE":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreElevatorBarriers.append(Rect)
            elif obj.name == "ElevatorSpawn":self.ElevatorSpawn = (obj.x,obj.y)
            elif obj.name == "Elevator_Menu":
                self.Elevator_Menu = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreElevatorBarriers.append(self.Elevator_Menu)
            elif obj.name == "BorderR":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CEStoreRooftopBarriers.append(Rect)
            elif obj.name == "RSign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name[2:],obj.Text2,obj.Text3)
                self.CEStoreRooftopReadables.append(Read)
                self.CEStoreRooftopBarriers.append(Read.Rect)
            elif obj.name == "Vending Machine":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RooftopVendingMachines.append(Rect)
                self.CEStoreRooftopBarriers.append(Rect)
            elif "RT" in obj.name:
                npc = NPC(obj.image,self.CEStoreRooftopCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CEStoreRooftopNPCS.append(npc)
                self.CEStoreRooftopBarriers.append(npc.rect)

    def Load_CeladonGym(self):
        for layer in self.CEGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CEGymCamera))
        
        for obj in self.CEGym.objects:
            if obj.name == "Spawn": 
                self.O_CEGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CEGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CeladonGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.CeladonGymReadables.append(Read)
                self.CeladonGymBarriers.append(Read.Rect)
            elif obj.name == "JR.TRAINER(FEMALE)":
                trainer = TrainerNPC("JR.TRAINER",obj.image,self.CEGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,"JR.TRAINER(FEMALE)")
                self.CeladonGymTrainers.append(trainer)
                self.CeladonGymBarriers.append(trainer.rect)
            elif obj.name == "CooltrainerF":
                trainer = TrainerNPC("Cooltrainer",obj.image,self.CEGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,"CooltrainerF")
                self.CeladonGymTrainers.append(trainer)
                self.CeladonGymBarriers.append(trainer.rect)
            elif obj.name == "Tree":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                tree = Tile((obj.x,obj.y),obj.image,(self.CEGymCamera))
                self.CeladonGymCuttables.append([Rect,tree])
                self.CeladonGymBarriers.append(Rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.CeladonGymTrainereyes.append(eyes)
            elif obj.name == "Erika":     
                self.Erika = GymLeaderNPC("Erika",obj.image,self.CEGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3,obj.Dialouge4],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.CeladonGymBarriers.append(self.Erika.rect)
            else:
                if "CE" in obj.name:
                    trainer = TrainerNPC(obj.name[3:],obj.image,self.CEGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                    self.CeladonGymTrainers.append(trainer)
                    self.CeladonGymBarriers.append(trainer.rect)

    def Load_GCRocketBase(self):
        for layer in self.Rocket_Hideout.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.Rocket_HideoutF1Camera))
                    elif layer.name == "Floor2":Tile((x*32,y*32),surf,(self.Rocket_HideoutF2Camera))
                    elif layer.name == "Floor3":Tile((x*32,y*32),surf,(self.Rocket_HideoutF3Camera))
                    elif layer.name == "Floor4":Tile((x*32,y*32),surf,(self.Rocket_HideoutF4Camera))
                    else:Tile((x*32,y*32),surf,(self.Rocket_HideoutElevatorCamera))

        for obj in self.Rocket_Hideout.objects:
            if obj.name == "GC_RocketBaseF1Spawn": self.GC_RocketBaseF1Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF1_GCDoor": self.RocketBaseF1_GCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RocketBaseF2_RocketBaseF1Spawn": self.RocketBaseF2_RocketBaseF1Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF1_RocketBaseF2Door": self.RocketBaseF1_RocketBaseF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.Rocket_HideoutF1Camera,obj.Item)
                self.Rocket_HideoutF1Pickups.append(ball)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.Rocket_HideoutF1HiddenItems.append(H)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RocketBaseF1Barriers.append(Rect)
            elif obj.name == "RocketBaseF2_2RocketBaseF1Spawn": self.RocketBaseF2_2RocketBaseF1Spawn = (obj.x,obj.y)
            elif obj.name == "2RocketBaseF1_2RocketBaseF2Door": self.RocketBaseF1_2RocketBaseF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall": 
                self.RocketBaseF1Doors = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text)
                self.RocketBaseF1Barriers.append(self.RocketBaseF1Doors.Rect)
                self.RocketBaseF1Readables.append(self.RocketBaseF1Doors)
            elif obj.name == "Elevator_RocketBaseF1Spawn": self.Elevator_RocketBaseF1Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF1_ElevatorDoor": self.RocketBaseF1_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #FLoor2
            elif obj.name == "RocketBaseF1_RocketBaseF2Spawn": self.RocketBaseF1_RocketBaseF2Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF2_RocketBaseF1Door": self.RocketBaseF2_RocketBaseF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "RocketBaseF3_RocketBaseF2Spawn": self.RocketBaseF3_RocketBaseF2Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF2_RocketBaseF3Door": self.RocketBaseF2_RocketBaseF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball2":
                ball = Pickups((obj.x,obj.y),obj.image,self.Rocket_HideoutF2Camera,obj.Item)
                self.Rocket_HideoutF2Pickups.append(ball)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RocketBaseF2Barriers.append(Rect)
            elif obj.name == "Move":
                B = MoverBlocks(obj.x,obj.y,obj.width,obj.height,obj.Way)
                self.MovingRocketBaseF2Blocks.append(B)
            elif obj.name == "2RocketBaseF1_2RocketBaseF2Spawn": self.RocketBaseF1_2RocketBaseF2Spawn = (obj.x,obj.y)
            elif obj.name == "2RocketBaseF2_2RocketBaseF1Door": self.RocketBaseF2_2RocketBaseF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall2": 
                self.RocketBaseF2Doors = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text)
                self.RocketBaseF2Barriers.append(self.RocketBaseF2Doors.Rect)
                self.RocketBaseF2Readables.append(self.RocketBaseF2Doors)
            elif obj.name == "Elevator_RocketBaseF2Spawn": self.Elevator_RocketBaseF2Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF2_ElevatorDoor": self.RocketBaseF2_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 3
            elif obj.name == "RocketBaseF2_RocketBaseF3Spawn": self.RocketBaseF2_RocketBaseF3Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF3_RocketBaseF2Door": self.RocketBaseF3_RocketBaseF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RocketBaseF3Barriers.append(Rect)
            elif obj.name == "Move2":
                B = MoverBlocks(obj.x,obj.y,obj.width,obj.height,obj.Way)
                self.MovingRocketBaseF3Blocks.append(B)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Rocket_HideoutF3Camera,obj.Item)
                self.Rocket_HideoutF3Pickups.append(ball)
            elif obj.name == "Hidden3":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.Rocket_HideoutF3HiddenItems.append(H)
            elif obj.name == "RocketBaseF4_RocketBaseF3Spawn": self.RocketBaseF4_RocketBaseF3Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF3_RocketBaseF4Door": self.RocketBaseF3_RocketBaseF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor4
            elif obj.name == "RocketBaseF3_RocketBaseF4Spawn": self.RocketBaseF3_RocketBaseF4Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF4_RocketBaseF3Door": self.RocketBaseF4_RocketBaseF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RocketBaseF4Barriers.append(Rect)
            elif obj.name == "Ball4":
                ball = Pickups((obj.x,obj.y),obj.image,self.Rocket_HideoutF4Camera,obj.Item)
                self.Rocket_HideoutF4Pickups.append(ball)
            elif obj.name == "Scopes":
                ball = Pickups((obj.x,obj.y),obj.image,self.Rocket_HideoutF4Camera,obj.Item)
                self.Rocket_HideoutF4Camera.remove(ball)
                self.Rocket_HideoutF4Pickups.append(ball)
            elif obj.name == "Hidden4":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.Rocket_HideoutF4HiddenItems.append(H)
            elif obj.name == "Elevator_RocketBaseF4Spawn": self.Elevator_RocketBaseF4Spawn = (obj.x,obj.y)
            elif obj.name == "RocketBaseF4_ElevatorDoor": self.RocketBaseF4_ElevatorDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #ELevator
            elif obj.name == "BorderE":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RocketBaseElevatorBarriers.append(Rect)
            elif obj.name == "RocketBase_ElevatorSpawn": self.RocketBase_ElevatorSpawn = (obj.x,obj.y)
            elif obj.name == "Elevator_Menu":
                self.RBaseElevator_Menu = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.RocketBaseElevatorBarriers.append(self.RBaseElevator_Menu)
            elif "F1" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Rocket_HideoutF1Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.RocketBaseF1Trainers.append(trainer)
                self.RocketBaseF1Barriers.append(trainer.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.RocketBaseF1Trainereyes.append(eyes)
            elif "F2" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Rocket_HideoutF2Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.RocketBaseF2Trainers.append(trainer)
                self.RocketBaseF2Barriers.append(trainer.rect)
            elif obj.name == "Eyes2":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.RocketBaseF2Trainereyes.append(eyes)
            elif "F3" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Rocket_HideoutF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.RocketBaseF3Trainers.append(trainer)
                self.RocketBaseF3Barriers.append(trainer.rect)
            elif obj.name == "Eyes3":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.RocketBaseF3Trainereyes.append(eyes)
            elif "F4" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Rocket_HideoutF4Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.RocketBaseF4Trainers.append(trainer)
                self.RocketBaseF4Barriers.append(trainer.rect)
            elif obj.name == "Eyes4":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.RocketBaseF4Trainereyes.append(eyes)
            elif obj.name == "Giovanni":
                self.RBaseGiovanni = TrainerNPC("Giovanni",obj.image,self.Rocket_HideoutF4Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.RocketBaseF4Barriers.append(self.RBaseGiovanni.rect)

    def Load_PokemonTower(self):
        for layer in self.Pokemon_Tower.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.Pokemon_TowerF1Camera))
                    elif layer.name == "Floor2":Tile((x*32,y*32),surf,(self.Pokemon_TowerF2Camera))
                    elif layer.name == "Floor3":Tile((x*32,y*32),surf,(self.Pokemon_TowerF3Camera))
                    elif layer.name == "Floor4":Tile((x*32,y*32),surf,(self.Pokemon_TowerF4Camera))
                    elif layer.name == "Floor5":Tile((x*32,y*32),surf,(self.Pokemon_TowerF5Camera))
                    elif layer.name == "Floor6":Tile((x*32,y*32),surf,(self.Pokemon_TowerF6Camera))
                    else:Tile((x*32,y*32),surf,(self.Pokemon_TowerF7Camera))

        for obj in self.Pokemon_Tower.objects:
            if obj.name == "O_PokeTowerF1Spawn": self.O_PokeTowerF1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF1_ODoor": self.PokeTowerF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF1Barriers.append(Rect)
            elif obj.name == "PokeTowerF2_PokeTowerF1Spawn": self.PokeTowerF2_PokeTowerF1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF1_PokeTowerF2Door": self.PokeTowerF1_PokeTowerF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Desk":
                self.PokemonTowerF1Desk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF1Barriers.append(self.PokemonTowerF1Desk)
            #FLoor2
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF2Barriers.append(Rect)
            elif obj.name == "PokeTowerF1_PokeTowerF2Spawn": self.PokeTowerF1_PokeTowerF2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF2_PokeTowerF1Door": self.PokeTowerF2_PokeTowerF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BattleLine":
                self.PokeTowerBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Rival": 
                self.PokeTowerRival = NPC(obj.image,(self.Pokemon_TowerF2Camera),"Dialogue",(obj.x,obj.y),"None",obj.name)
                self.PokeTowerF2Barriers.append(self.PokeTowerRival.rect)
            elif obj.name == "PokeTowerF3_PokeTowerF2Spawn": self.PokeTowerF3_PokeTowerF2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF2_PokeTowerF3Door": self.PokeTowerF2_PokeTowerF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor3
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF3Barriers.append(Rect)
            elif obj.name == "PokeTowerF2_PokeTowerF3Spawn": self.PokeTowerF2_PokeTowerF3Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF3_PokeTowerF2Door": self.PokeTowerF3_PokeTowerF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeTowerF4_PokeTowerF3Spawn": self.PokeTowerF4_PokeTowerF3Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF3_PokeTowerF4Door": self.PokeTowerF3_PokeTowerF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_TowerF3Camera,obj.Item)
                self.Pokemon_TowerF3Pickups.append(ball)
            #Floor4
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF4Barriers.append(Rect)
            elif obj.name == "PokeTowerF3_PokeTowerF4Spawn": self.PokeTowerF3_PokeTowerF4Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF4_PokeTowerF3Door": self.PokeTowerF4_PokeTowerF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeTowerF5_PokeTowerF4Spawn": self.PokeTowerF5_PokeTowerF4Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF4_PokeTowerF5Door": self.PokeTowerF4_PokeTowerF5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball4":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_TowerF4Camera,obj.Item)
                self.Pokemon_TowerF4Pickups.append(ball)
            #Floor5
            elif obj.name == "Border5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF5Barriers.append(Rect)
            elif obj.name == "PokeTowerF4_PokeTowerF5Spawn": self.PokeTowerF4_PokeTowerF5Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF5_PokeTowerF4Door": self.PokeTowerF5_PokeTowerF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeTowerF6_PokeTowerF5Spawn": self.PokeTowerF6_PokeTowerF5Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF5_PokeTowerF6Door": self.PokeTowerF5_PokeTowerF6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball5":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_TowerF5Camera,obj.Item)
                self.Pokemon_TowerF5Pickups.append(ball)
            #Floor6
            elif obj.name == "Border6":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF6Barriers.append(Rect)
            elif obj.name == "PokeTowerF5_PokeTowerF6Spawn":self.PokeTowerF5_PokeTowerF6Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF6_PokeTowerF5Door": self.PokeTowerF6_PokeTowerF5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeTowerF7_PokeTowerF6Spawn":self.PokeTowerF7_PokeTowerF6Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF6_PokeTowerF7Door": self.PokeTowerF6_PokeTowerF7Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball6":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_TowerF6Camera,obj.Item)
                self.Pokemon_TowerF6Pickups.append(ball)
            #Floor7
            elif obj.name == "Border7":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeTowerF7Barriers.append(Rect)
            elif obj.name == "PokeTowerF6_PokeTowerF7Spawn":self.PokeTowerF6_PokeTowerF7Spawn = (obj.x,obj.y)
            elif obj.name == "PokeTowerF7_PokeTowerF6Door": self.PokeTowerF7_PokeTowerF6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Mr.Fuji":
                self.Mr_Fuji = NPC(obj.image,self.Pokemon_TowerF7Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.PokeTowerF7Barriers.append(self.Mr_Fuji.rect)
            elif "F1" in obj.name:
                npc = NPC(obj.image,self.Pokemon_TowerF1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_TowerF1NPCS.append(npc)
                self.PokeTowerF1Barriers.append(npc.rect)
            elif "F2" in obj.name:
                npc = NPC(obj.image,self.Pokemon_TowerF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_TowerF2NPCS.append(npc)
                self.PokeTowerF2Barriers.append(npc.rect)
            elif "F3" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_TowerF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.PokeTowerF3Trainers.append(trainer)
                self.PokeTowerF3Barriers.append(trainer.rect)
            elif obj.name == "Eyes3":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.PokeTowerF3Trainereyes.append(eyes)
            elif "F4" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_TowerF4Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.PokeTowerF4Trainers.append(trainer)
                self.PokeTowerF4Barriers.append(trainer.rect)
            elif obj.name == "Eyes4":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.PokeTowerF4Trainereyes.append(eyes)
            elif "F5" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_TowerF5Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.PokeTowerF5Trainers.append(trainer)
                self.PokeTowerF5Barriers.append(trainer.rect)
            elif obj.name == "Eyes5":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.PokeTowerF5Trainereyes.append(eyes)
            elif obj.name == "Healer":
                npc = NPC(obj.image,self.Pokemon_TowerF5Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_TowerF5NPCS.append(npc)
                self.PokeTowerF5Barriers.append(npc.rect)
            elif obj.name == "Safe Zone":self.PokeTowerSafeZone = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif "F6" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_TowerF6Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.PokeTowerF6Trainers.append(trainer)
                self.PokeTowerF6Barriers.append(trainer.rect)
            elif obj.name == "Eyes6":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.PokeTowerF6Trainereyes.append(eyes)
            elif "F7" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_TowerF7Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.PokeTowerF7Trainers.append(trainer)
                self.PokeTowerF7Barriers.append(trainer.rect)
            elif obj.name == "Eyes7":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.PokeTowerF7Trainereyes.append(eyes)
            elif obj.name == "GhostLine":self.PokeTowerGhostLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Wild3":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.PokemonTowerF3Tiles.append(WildTile)
            elif obj.name == "Wild4":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.PokemonTowerF4Tiles.append(WildTile)
            elif obj.name == "Wild5":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.PokemonTowerF5Tiles.append(WildTile)
            elif obj.name == "Wild6":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.PokemonTowerF6Tiles.append(WildTile)
            elif obj.name == "Wild7":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.PokemonTowerF7Tiles.append(WildTile)

    def Load_R16GuardHouse(self):
        for layer in self.R16GuardHouse.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.R16GuardHouseCamera))
                    else:Tile((x*32,y*32),surf,(self.R16GuardHouseF2Camera))

        for obj in self.R16GuardHouse.objects:
            if obj.name == "3O_R16H1Spawn": self.O_R16H1Spawn3 = (obj.x,obj.y)
            elif obj.name == "3R16H1_ODoor": self.R16H1_ODoor3 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_R16H1Spawn": self.O_R16H1Spawn = (obj.x,obj.y)
            elif obj.name == "R16H1_ODoor": self.R16H1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "2O_R16H1Spawn": self.O_R16H1Spawn2 = (obj.x,obj.y)
            elif obj.name == "2R16H1_ODoor": self.R16H1_ODoor2 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "4O_R16H1Spawn": self.O_R16H1Spawn4 = (obj.x,obj.y)
            elif obj.name == "4R16H1_ODoor": self.R16H1_ODoor4 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "BikeLine":self.BikeLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif "F1" in obj.name:
                npc = NPC(obj.image,(self.R16GuardHouseCamera),obj.Type,(obj.x,obj.y),obj.Dialouge[2:],obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R16GuardHouseNPCS.append(npc)
                self.R16GuardHouseBarriers.append(npc.rect)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R16GuardHouseBarriers.append(Rect)
            elif obj.name == "R16H1F2_R16H1Spawn": self.R16H1F2_R16H1Spawn = (obj.x,obj.y)
            elif obj.name == "R16H1_R16H1F2Door": self.R16H1_R16H1F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor2
            elif obj.name == "R16H1_R16H1F2Spawn": self.R16H1_R16H1F2Spawn = (obj.x,obj.y)
            elif obj.name == "R16H1F2_R16H1Door": self.R16H1F2_R16H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R16GuardHouseF2Barriers.append(Rect)
            elif obj.name == "Scope":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.R16GuardHouseF2Readables.append(Read)
                self.R16GuardHouseF2Barriers.append(Read.Rect)
            elif "F2" in obj.name:
                npc = NPC(obj.image,(self.R16GuardHouseF2Camera),obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R16GuardHouseF2NPCS.append(npc)
                self.R16GuardHouseF2Barriers.append(npc.rect)

    def Load_R16House2(self):
        for layer in self.R16House2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.R16House2Camera))

        for obj in self.R16House2.objects:
            if obj.name == "O_R16H2Spawn": self.O_R16H2Spawn = (obj.x,obj.y)
            elif obj.name == "R16H2_ODoor": self.R16H2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R16House2Barriers.append(Rect)
            elif obj.name == "Fearow":
                npc = NPC(obj.image,self.R16House2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R16House2NPCS.append(npc)
                self.R16House2Barriers.append(npc.rect)
            else:
                self.R16House2Girl = NPC(obj.image,self.R16House2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Hm02 is FLY. It will take you back to any town. Put it to good use!",IA2="",IA3="")
                self.R16House2NPCS.append(self.R16House2Girl)
                self.R16House2Barriers.append(self.R16House2Girl.rect)
    
    def Load_R18GuardHouse(self):
        for layer in self.R18GuardHouse.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor1":Tile((x*32,y*32),surf,(self.R18GuardHouseCamera))
                    else:Tile((x*32,y*32),surf,(self.R18GuardHouseF2Camera))

        for obj in self.R18GuardHouse.objects:
            if obj.name == "O_R18GHSpawn": self.O_R18GHSpawn = (obj.x,obj.y)
            elif obj.name == "R18GH_ODoor": self.R18GH_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O2_R18GHSpawn": self.O2_R18GHSpawn = (obj.x,obj.y)
            elif obj.name == "R18GH_O2Door": self.R18GH_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R18GHF2_R18GHSpawn": self.R18GHF2_R18GHSpawn = (obj.x,obj.y)
            elif obj.name == "R18GH_R18GHF2Door": self.R18GH_R18GHF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R18GuardHouseBarriers.append(Rect)
            elif obj.name == "R18GH_R18GHF2Spawn": self.R18GH_R18GHF2Spawn = (obj.x,obj.y)
            elif obj.name == "R18GHF2_R18GHDoor": self.R18GHF2_R18GHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor2
            elif obj.name == "R16H1_R16H1F2Spawn": self.R16H1_R16H1F2Spawn = (obj.x,obj.y)
            elif obj.name == "R16H1F2_R16H1Door": self.R16H1F2_R16H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R18GuardHouseF2Barriers.append(Rect)
            elif obj.name == "Scope":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.R18GuardHouseF2Readables.append(Read)
                self.R18GuardHouseF2Barriers.append(Read.Rect)
            elif obj.name == "Boy":
                npc = TraderNPC(obj.image,self.R18GuardHouseF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.R18GuardHouseF2NPCS.append(npc)
                self.Traders.append(npc)
                self.R18GuardHouseF2Barriers.append(npc.rect)

    def Load_FC1H(self):
        for layer in self.FCH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.FCH1Camera))

        for obj in self.FCH1.objects:
            if obj.name == "Spawn": self.O_FCH1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.FCH1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.FCH1Barriers.append(Rect)
            else:
                npc = NPC(obj.image,self.FCH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.FCH1NPCS.append(npc)
                self.FCH1Barriers.append(npc.rect)

    def Load_FC2H(self):
        for layer in self.FCH2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.FCH2Camera))

        for obj in self.FCH2.objects:
            if obj.name == "Spawn": self.O_FCH2Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.FCH2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.FCH2Barriers.append(Rect)
            else:
                npc = NPC(obj.image,self.FCH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.FCH2NPCS.append(npc)
                self.FCH2Barriers.append(npc.rect)     

    def Load_FC3H(self):
        for layer in self.FCH3.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.FCH3Camera))

        for obj in self.FCH3.objects:
            if obj.name == "Spawn": self.O_FCH3Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.FCH3_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.FCH3Barriers.append(Rect)
            elif obj.name == "Spawn2": self.O2_FCH3Spawn = (obj.x,obj.y)
            elif obj.name == "Door2": self.FCH3_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            else:
                npc = NPC(obj.image,self.FCH3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Hello there, young one! How are the fish biting?",IA2="",IA3="")
                self.FCH3NPCS.append(npc)
                self.FCH3Barriers.append(npc.rect)   

    def Load_FCWH(self):
        for layer in self.FCWH.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.FCWHCamera))

        for obj in self.FCWH.objects:
            if obj.name == "Spawn": self.O_FCWHSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.FCWH_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.FCWHBarriers.append(Rect)
            elif obj.name == "Boulder":
                x = Rocks((obj.x,obj.y),obj.image,self.FCWHCamera,self.FCWHBarriers)
                self.FCWHBarriers.append(x.rect)
                self.FCWHBoulders.append(x)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.FCWHCamera,obj.Item)
                self.FCWHPickups.append(ball)
            else:
                npc = NPC(obj.image,self.FCWHCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.FCWHNPCS.append(npc)
                self.FCWHBarriers.append(npc.rect) 

    def Load_SZE(self):
        for layer in self.SZE.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SZECamera))

        for obj in self.SZE.objects:
            if obj.name == "Spawn": self.O_SZESpawn = (obj.x,obj.y)
            elif obj.name == "Overworld": self.SZE_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Desk":
                self.SZEDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SZEBarriers.append(self.SZEDesk)
            elif obj.name == "Pay":self.SZPayLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Worker2":Tile((obj.x,obj.y),obj.image,(self.SZECamera))
            elif obj.name == "Worker":
                npc = NPC(obj.image,self.SZECamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SZENPCS.append(npc)
                self.SZEBarriers.append(npc.rect) 
            else:
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SZEBarriers.append(Rect)

    def Load_SafariZone(self):
        for layer in self.Safari_Zone.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Main Zone":Tile((x*32,y*32),surf,(self.Safari_ZoneMZCamera))
                    elif layer.name == "Area 1":Tile((x*32,y*32),surf,(self.Safari_ZoneA1Camera))
                    elif layer.name == "Area 2":Tile((x*32,y*32),surf,(self.Safari_ZoneA2Camera))
                    else:Tile((x*32,y*32),surf,(self.Safari_ZoneA3Camera))

        for obj in self.Safari_Zone.objects:
            if obj.name == "O_SMZSpawn": self.O_SMZSpawn = (obj.x,obj.y)
            elif obj.name == "SMZ_ODoor": self.SMZ_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "H1_SZMASpawn": self.H1_SZMASpawn = (obj.x,obj.y)
            elif obj.name == "SZMA_H1Door": self.SZMA_H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA1_MZSpawn": self.SZA1_MZSpawn = (obj.x,obj.y)
            elif obj.name == "SZMZ_A1Door": self.SZMZ_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA2_MZSpawn": self.SZA2_MZSpawn = (obj.x,obj.y)
            elif obj.name == "SZMZ_A2Door": self.SZMZ_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA3_MZSpawn": self.SZA3_MZSpawn = (obj.x,obj.y)
            elif obj.name == "SZMZ_A3Door": self.SZMZ_A3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Seapoint":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SMZFishingPoint.append(Rect)
                self.SMZBarriers.append(Rect)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SMZBarriers.append(Rect)
            elif obj.name == "Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,self.Safari_ZoneMZCamera)
                self.SMZReadables.append(Read)
                self.SMZBarriers.append(Read.Rect)
            elif obj.name == "Grass":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SMZGrassBlocks.append(WildTile)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.Safari_ZoneMZCamera,obj.Item)
                self.Safari_ZoneMZPickups.append(ball)
            # Area 1
            elif obj.name == "SZA1_MZDoor":self.SZA1_MZDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZMZ_A1Spawn": self.SZMZ_A1Spawn = (obj.x,obj.y)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SA1Barriers.append(Rect)
            elif obj.name == "Grass2":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SA1GrassBlocks.append(WildTile)
            elif obj.name == "Sign2":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,self.Safari_ZoneA1Camera)
                self.SA1Readables.append(Read)
                self.SA1Barriers.append(Read.Rect)
            elif obj.name == "Seapoint2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SA1FishingPoint.append(Rect)
                self.SA1Barriers.append(Rect)
            elif obj.name == "H1_SZA1Spawn": self.H1_SZA1Spawn = (obj.x,obj.y)
            elif obj.name == "SZA1_H1Door": self.SZA1_H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA2_A1Spawn": self.SZA2_A1Spawn = (obj.x,obj.y)
            elif obj.name == "SZA1_A2Door": self.SZA1_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball2":
                ball = Pickups((obj.x,obj.y),obj.image,self.Safari_ZoneA1Camera,obj.Item)
                self.Safari_ZoneA1Pickups.append(ball)
            # Area 2
            elif obj.name == "SZA1_A2Spawn": self.SZA1_A2Spawn = (obj.x,obj.y)
            elif obj.name == "SZA2_A1Door": self.SZA2_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SA2Barriers.append(Rect)
            elif obj.name == "Sign3":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,self.Safari_ZoneA2Camera)
                self.SA2Readables.append(Read)
                self.SA2Barriers.append(Read.Rect)
            elif obj.name == "Seapoint3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SA2FishingPoint.append(Rect)
                self.SA2Barriers.append(Rect)
            elif obj.name == "Grass3":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SA2GrassBlocks.append(WildTile)
            elif obj.name == "H1_SZA2Spawn": self.H1_SZA2Spawn = (obj.x,obj.y)
            elif obj.name == "SZA2_H1Door": self.SZA2_H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZMZ_A2Spawn": self.SZMZ_A2Spawn = (obj.x,obj.y)
            elif obj.name == "SZA2_MZDoor": self.SZA2_MZDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA3_A2Spawn": self.SZA3_A2Spawn = (obj.x,obj.y)
            elif obj.name == "SZA2_A3Door": self.SZA2_A3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA3_A2Spawn2": self.SZA3_A2Spawn2 = (obj.x,obj.y)
            elif obj.name == "SZA2_A3Door2": self.SZA2_A3Door2 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Safari_ZoneA2Camera,obj.Item)
                self.Safari_ZoneA2Pickups.append(ball)
            #Area 3
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SA3Barriers.append(Rect)
            elif obj.name == "Sign4":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,self.Safari_ZoneA3Camera)
                self.SA3Readables.append(Read)
                self.SA3Barriers.append(Read.Rect)
            elif obj.name == "RH_SZA3Spawn": self.RH_SZA3Spawn = (obj.x,obj.y)
            elif obj.name == "SZA3_RHDoor": self.SZA3_RHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZMZ_A3Spawn": self.SZMZ_A3Spawn = (obj.x,obj.y)
            elif obj.name == "SZA3_MZDoor": self.SZA3_MZDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA2_A3Spawn": self.SZA2_A3Spawn = (obj.x,obj.y)
            elif obj.name == "SZA3_A2Door": self.SZA3_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SZA2_A3Spawn2": self.SZA2_A3Spawn2 = (obj.x,obj.y)
            elif obj.name == "SZA3_A2Door2": self.SZA3_A2Door2 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SH_SZA3Spawn": self.SH_SZA3Spawn = (obj.x,obj.y)
            elif obj.name == "Grass4":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SA3GrassBlocks.append(WildTile)
            elif obj.name == "SZA3_SHDoor": self.SZA3_SHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SZA3HiddenItems.append(H)
            elif obj.name == "Ball4":
                ball = Pickups((obj.x,obj.y),obj.image,self.Safari_ZoneA3Camera,obj.Item)
                self.Safari_ZoneA3Pickups.append(ball)
            
    def Load_SZMAH1(self):
        for layer in self.SZMAH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SZMAH1Camera,self.SZA1RestHouseCamera,self.SZA2RestHouseCamera,self.SZA3RestHouseCamera))

        for obj in self.SZMAH1.objects:
            if obj.name == "Spawn": 
                self.SZMA_H1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.H1_SZMADoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SZMAH1Barriers.append(Rect)
                self.SZA1RHBarriers.append(Rect)
                self.SZA2RHBarriers.append(Rect)
                self.SZA3RHBarriers.append(Rect)
            elif "A1" in obj.name:
                npc = NPC(obj.image,self.SZA1RestHouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SZA1RHNPCS.append(npc)
                self.SZA1RHBarriers.append(npc.rect) 
            elif "A2" in obj.name:
                npc = NPC(obj.image,self.SZA2RestHouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SZA2RHNPCS.append(npc)
                self.SZA2RHBarriers.append(npc.rect) 
            elif "A3" in obj.name:
                npc = NPC(obj.image,self.SZA3RestHouseCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SZA3RHNPCS.append(npc)
                self.SZA3RHBarriers.append(npc.rect) 
            else:
                npc = NPC(obj.image,self.SZMAH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SZMAH1NPCS.append(npc)
                self.SZMAH1Barriers.append(npc.rect) 

    def Load_SZA3SH(self):
        for layer in self.SZA3SH.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SZA3SHCamera))

        for obj in self.SZA3SH.objects:
            if obj.name == "Spawn": self.SZA3_SHSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.SH_SZA3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SZA3SHBarriers.append(Rect)
            else:
                self.SHGuy = NPC(obj.image,self.SZA3SHCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Man",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="HM03 is SURF! POKEMON will be able to ferry you across water!",IA2="And, this HM isn't disposable! You can use it over and over!",IA3="You're super lucky for winning this fabulous prize!")
                self.SZA3SHBarriers.append(self.SHGuy.rect) 

    def Load_FuschiaGym(self):
        for layer in self.FCGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.FCGymCamera))
        
        for obj in self.FCGym.objects:
            if obj.name == "Spawn": 
                self.O_FCGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.FCGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.FCGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.FCGymReadables.append(Read)
                self.FCGymBarriers.append(Read.Rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.FCGymTrainereyes.append(eyes)
            elif obj.name == "Koga":     
                self.Koga = GymLeaderNPC("Koga",obj.image,self.FCGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.FCGymBarriers.append(self.Koga.rect)
            elif obj.name == "Announcer":
                npc = NPC(obj.image,self.FCGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.FCGymNPCS.append(npc)
                self.FCGymBarriers.append(npc.rect)
            else:
                trainer = TrainerNPC(obj.name[2:],obj.image,self.FCGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.FCGymTrainers.append(trainer)
                self.FCGymBarriers.append(trainer.rect)

    def Load_SFH1(self):
        for layer in self.SFH1.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SFH1Camera))

        for obj in self.SFH1.objects:
            if obj.name == "Spawn": self.O_SFH1Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.SFH1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SFH1Barriers.append(Rect)
            else:
                self.MrPsychic = NPC(obj.image,self.SFH1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="TM29 is PSYCHIC! It can lower the target's SPECIAL abilities.",IA2="",IA3="")
                self.SFH1Barriers.append(self.MrPsychic.rect)
    
    def Load_Fighting_Dojo(self):
        for layer in self.Fighting_Dojo.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Fighting_DojoCamera))
        
        for obj in self.Fighting_Dojo.objects:
            if obj.name == "Spawn": 
                self.O_FDSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.FD_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Fighting_DojoBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.Fighting_DojoReadables.append(Read)
                self.Fighting_DojoBarriers.append(Read.Rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Fighting_DojoTrainereyes.append(eyes)
            elif obj.name == "Leader":     
                self.Fighting_DojoLeader = TrainerNPC("Blackbelt",obj.image,self.Fighting_DojoCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Fighting_DojoBarriers.append(self.Fighting_DojoLeader.rect)
                self.Fighting_DojoTrainers.append(self.Fighting_DojoLeader)
            elif obj.name == "Fight":
                self.DojoFightLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif "Hit" in obj.name:
                ball = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.Fighting_DojoReadables.append(ball)
                self.Fighting_DojoPokemon.append([ball,Tile((obj.x,obj.y),obj.image,(self.Fighting_DojoCamera))])
            else:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Fighting_DojoCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Fighting_DojoTrainers.append(trainer)
                self.Fighting_DojoBarriers.append(trainer.rect)

    def Load_SilphCo(self):
        for layer in self.Silph_Co.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.Silph_CoF1Camera))
                    elif layer.name == "Floor 2":Tile((x*32,y*32),surf,(self.Silph_CoF2Camera))
                    elif layer.name == "Floor 3":Tile((x*32,y*32),surf,(self.Silph_CoF3Camera))
                    elif layer.name == "Floor 4":Tile((x*32,y*32),surf,(self.Silph_CoF4Camera))
                    elif layer.name == "Floor 5":Tile((x*32,y*32),surf,(self.Silph_CoF5Camera))
                    elif layer.name == "Floor 6":Tile((x*32,y*32),surf,(self.Silph_CoF6Camera))
                    elif layer.name == "Floor 7":Tile((x*32,y*32),surf,(self.Silph_CoF7Camera))
                    elif layer.name == "Floor 8":Tile((x*32,y*32),surf,(self.Silph_CoF8Camera))
                    elif layer.name == "Floor 9":Tile((x*32,y*32),surf,(self.Silph_CoF9Camera))
                    elif layer.name == "Floor 10":Tile((x*32,y*32),surf,(self.Silph_CoF10Camera))
                    elif layer.name == "Floor 11":Tile((x*32,y*32),surf,(self.Silph_CoF11Camera))
                    else:Tile((x*32,y*32),surf,(self.Silph_CoElevatorCamera))

        for obj in self.Silph_Co.objects:
            if obj.name == "O_SilCoF1Spawn": self.O_SilCoF1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF1_ODoor": self.SilCoF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF1Barriers.append(Rect)
            elif obj.name == "SilCoF2_SilCoF1Spawn": self.SilCoF2_SilCoF1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF1_SilCoF2Door": self.SilCoF1_SilCoF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE_SilCoF1Spawn": self.SilCoE_SilCoF1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF1_SilCoEDoor": self.SilCoF1_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 2
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF2Barriers.append(Rect)
            elif obj.name == "SilCoF1_SilCoF2Spawn": self.SilCoF1_SilCoF2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF2_SilCoF1Door": self.SilCoF2_SilCoF1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "2Woman":
                self.SilCoF2Woman = NPC(obj.image,self.Silph_CoF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="TM36 is SELFDESTRUCT! It's powerful, but the POKEMON that uses it",IA2="faints! Be careful.",IA3="")
                self.Silph_CoF2Barriers.append(self.SilCoF2Woman.rect)
            elif obj.name == "SilCoF3_SilCoF2Spawn": self.SilCoF3_SilCoF2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF2_SilCoF3Door": self.SilCoF2_SilCoF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall2":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF2Barriers.append(Rect.Rect)
                self.Silph_CoF2Readables.append(Rect)
                self.Silph_CoF2InvisableBarrier.append(Rect)
            elif obj.name == "SilCoE_SilCoF2Spawn": self.SilCoE_SilCoF2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF2_SilCoEDoor": self.SilCoF2_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoA2_SilCoA1Spawn": self.SilCoA2_SilCoA1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoA1_SilCoA2Door": self.SilCoA1_SilCoA2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoB2_SilCoB1Spawn": self.SilCoB2_SilCoB1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoB1_SilCoB2Door": self.SilCoB1_SilCoB2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoD2_SilCoD1Spawn": self.SilCoD2_SilCoD1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoD1_SilCoD2Door": self.SilCoD1_SilCoD2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoI2_SilCoI1Spawn": self.SilCoI2_SilCoI1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoI1_SilCoI2Door": self.SilCoI1_SilCoI2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 3
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF3Barriers.append(Rect)
            elif obj.name == "SilCoF2_SilCoF3Spawn": self.SilCoF2_SilCoF3Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF3_SilCoF2Door": self.SilCoF3_SilCoF2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall3":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF3Barriers.append(Rect.Rect)
                self.Silph_CoF3Readables.append(Rect)
                self.Silph_CoF3InvisableBarrier.append(Rect)
            elif obj.name == "SilCoF4_SilCoF3Spawn": self.SilCoF4_SilCoF3Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF3_SilCoF4Door": self.SilCoF3_SilCoF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "3Man":
                self.SilCoF3Man = NPC(obj.image,self.Silph_CoF3Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF3Barriers.append(self.SilCoF3Man.rect)
            elif obj.name == "SilCoE_SilCoF3Spawn": self.SilCoE_SilCoF3Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF3_SilCoEDoor": self.SilCoF3_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoD1_SilCoD2Spawn": self.SilCoD1_SilCoD2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoD2_SilCoD1Door": self.SilCoD2_SilCoD1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE2_SilCoE1Spawn": self.SilCoE2_SilCoE1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoE1_SilCoE2Door": self.SilCoE1_SilCoE2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoN2_SilCoN1Spawn": self.SilCoN2_SilCoN1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoN1_SilCoN2Door": self.SilCoN1_SilCoN2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Silph_CoF3Camera,obj.Item)
                self.SilCoF3Pickups.append(ball)
            elif obj.name == "SilCoN1_SilCoN2Spawn": self.SilCoN1_SilCoN2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoN2_SilCoN1Door": self.SilCoN2_SilCoN1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoH2_SilCoH1Spawn": self.SilCoH2_SilCoH1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoH1_SilCoH2Door": self.SilCoH1_SilCoH2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoO2_SilCoO1Spawn": self.SilCoO2_SilCoO1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoO1_SilCoO2Door": self.SilCoO1_SilCoO2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoQ2_SilCoQ1Spawn": self.SilCoQ2_SilCoQ1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoQ1_SilCoQ2Door": self.SilCoQ1_SilCoQ2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 4
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF4Barriers.append(Rect)
            elif obj.name == "SilCoF3_SilCoF4Spawn": self.SilCoF3_SilCoF4Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF4_SilCoF3Door": self.SilCoF4_SilCoF3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF5_SilCoF4Spawn": self.SilCoF5_SilCoF4Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF4_SilCoF5Door": self.SilCoF4_SilCoF5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall4":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF4Barriers.append(Rect.Rect)
                self.Silph_CoF4Readables.append(Rect)
                self.Silph_CoF4InvisableBarrier.append(Rect)
            elif obj.name == "SilCoE_SilCoF4Spawn": self.SilCoE_SilCoF4Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF4_SilCoEDoor": self.SilCoF4_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoK2_SilCoK1Spawn": self.SilCoK2_SilCoK1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoK1_SilCoK2Door": self.SilCoK1_SilCoK2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball4":
                ball = Pickups((obj.x,obj.y),obj.image,self.Silph_CoF4Camera,obj.Item)
                self.SilCoF4Pickups.append(ball)
            elif obj.name == "SilCoL2_SilCoL1Spawn": self.SilCoL2_SilCoL1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoL1_SilCoL2Door": self.SilCoL1_SilCoL2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "4Man":
                self.SilCoF4Man = NPC(obj.image,self.Silph_CoF4Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF4Barriers.append(self.SilCoF4Man.rect)
            elif obj.name == "SilCoM2_SilCoM1Spawn": self.SilCoM2_SilCoM1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoM1_SilCoM2Door": self.SilCoM1_SilCoM2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoJ2_SilCoJ1Spawn": self.SilCoJ2_SilCoJ1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoJ1_SilCoJ2Door": self.SilCoJ1_SilCoJ2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 5
            elif obj.name == "Border5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF5Barriers.append(Rect)
            elif obj.name == "SilCoF4_SilCoF5Spawn": self.SilCoF4_SilCoF5Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF5_SilCoF4Door": self.SilCoF5_SilCoF4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF6_SilCoF5Spawn": self.SilCoF6_SilCoF5Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF5_SilCoF6Door": self.SilCoF5_SilCoF6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall5":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF5Barriers.append(Rect.Rect)
                self.Silph_CoF5Readables.append(Rect)
                self.Silph_CoF5InvisableBarrier.append(Rect)
            elif obj.name == "SilCoE_SilCoF5Spawn": self.SilCoE_SilCoF5Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF5_SilCoEDoor": self.SilCoF5_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Board":
                ball = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.Silph_CoF5Readables.append(ball)
                Tile((obj.x,obj.y),obj.image,(self.Silph_CoF5Camera))
            elif obj.name == "SilCoE1_SilCoE2Spawn": self.SilCoE1_SilCoE2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoE2_SilCoE1Door": self.SilCoE2_SilCoE1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF2_SilCoF1Spawn2": self.SilCoF2_SilCoF1Spawn2 = (obj.x,obj.y)
            elif obj.name == "5Man":
                self.SilCoF5Man = NPC(obj.image,self.Silph_CoF5Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF5Barriers.append(self.SilCoF5Man.rect)
            elif obj.name == "SilCoF1_SilCoF2Door2": self.SilCoF1_SilCoF2Door2 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoG2_SilCoG1Spawn": self.SilCoG2_SilCoG1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoG1_SilCoG2Door": self.SilCoG1_SilCoG2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball5":
                ball = Pickups((obj.x,obj.y),obj.image,self.Silph_CoF5Camera,obj.Item)
                self.SilCoF5Pickups.append(ball)
            elif obj.name == "SilCoH1_SilCoH2Spawn": self.SilCoH1_SilCoH2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoH2_SilCoH1Door": self.SilCoH2_SilCoH1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden5":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SilCoF5HiddenItems.append(H)
            #Floor 6
            elif obj.name == "Border6":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF6Barriers.append(Rect)
            elif obj.name == "SilCoF5_SilCoF6Spawn": self.SilCoF5_SilCoF6Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF6_SilCoF5Door": self.SilCoF6_SilCoF5Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF7_SilCoF6Spawn": self.SilCoF7_SilCoF6Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF6_SilCoF7Door": self.SilCoF6_SilCoF7Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall6":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF6Barriers.append(Rect.Rect)
                self.Silph_CoF6Readables.append(Rect)
                self.Silph_CoF6InvisableBarrier.append(Rect)
            elif obj.name == "SilCoI1_SilCoI2Spawn": self.SilCoI1_SilCoI2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoI2_SilCoI1Door": self.SilCoI2_SilCoI1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoJ1_SilCoJ2Spawn": self.SilCoJ1_SilCoJ2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoJ2_SilCoJ1Door": self.SilCoJ2_SilCoJ1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball6":
                ball = Pickups((obj.x,obj.y),obj.image,self.Silph_CoF6Camera,obj.Item)
                self.SilCoF6Pickups.append(ball)
            elif obj.name == "SilCoE_SilCoF6Spawn": self.SilCoE_SilCoF6Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF6_SilCoEDoor": self.SilCoF6_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name[0] == "6":
                npc = NPC(obj.image,self.Silph_CoF6Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,IA1=obj.ChangeText)
                self.Silph_CoF6NPCS.append(npc)
                self.Silph_CoF6Barriers.append(npc.rect) 
            #Floor 7
            elif obj.name == "Border7":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF7Barriers.append(Rect)
            elif obj.name == "SilCoF6_SilCoF7Spawn": self.SilCoF6_SilCoF7Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF7_SilCoF6Door": self.SilCoF7_SilCoF6Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall7":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF7Barriers.append(Rect.Rect)
                self.Silph_CoF7Readables.append(Rect)
                self.Silph_CoF7InvisableBarrier.append(Rect)
            elif obj.name == "SilCoF8_SilCoF7Spawn": self.SilCoF8_SilCoF7Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF7_SilCoF8Door": self.SilCoF7_SilCoF8Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE_SilCoF7Spawn": self.SilCoE_SilCoF7Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF7_SilCoEDoor": self.SilCoF7_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball7":
                ball = Pickups((obj.x,obj.y),obj.image,self.Silph_CoF7Camera,obj.Item)
                self.SilCoF7Pickups.append(ball)
            elif obj.name == "SilCoF1_SilCoF2Spawn2": self.SilCoF1_SilCoF2Spawn2 = (obj.x,obj.y)
            elif obj.name == "SilCoF2_SilCoF1Door2": self.SilCoF2_SilCoF1Door2 = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoO1_SilCoO2Spawn": self.SilCoO1_SilCoO2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoO2_SilCoO1Door": self.SilCoO2_SilCoO1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name[0] == "7":
                npc = NPC(obj.image,self.Silph_CoF7Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,IA1=obj.ChangeText)
                self.Silph_CoF7NPCS.append(npc)
                self.Silph_CoF7Barriers.append(npc.rect)  
            elif obj.name == "SilCoP2_SilCoP1Spawn": self.SilCoP2_SilCoP1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoP1_SilCoP2Door": self.SilCoP1_SilCoP2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilphCoRivalBattleLine":self.SilphCoRivalBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "SilphCoRivalSpot": self.SilphCoRivalSpot = (obj.x,obj.y)
            elif obj.name == "LaprasMan":
                self.LaprasMan = NPC(obj.image,self.Silph_CoF7Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Man",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,IA1=obj.ChangeText)
                self.Silph_CoF7Barriers.append(self.LaprasMan.rect)
            #Floor 8
            elif obj.name == "Border8":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF8Barriers.append(Rect)
            elif obj.name == "SilCoF7_SilCoF8Spawn": self.SilCoF7_SilCoF8Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF8_SilCoF7Door": self.SilCoF8_SilCoF7Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall8":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF8Barriers.append(Rect.Rect)
                self.Silph_CoF8Readables.append(Rect)
                self.Silph_CoF8InvisableBarrier.append(Rect)
            elif obj.name == "SilCoF9_SilCoF8Spawn": self.SilCoF9_SilCoF8Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF8_SilCoF9Door": self.SilCoF8_SilCoF9Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE_SilCoF8Spawn": self.SilCoE_SilCoF8Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF8_SilCoEDoor": self.SilCoF8_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "8Man":
                self.SilCoF8Man = NPC(obj.image,self.Silph_CoF8Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF8Barriers.append(self.SilCoF8Man.rect)           
            elif obj.name == "SilCoA1_SilCoA2Spawn": self.SilCoA1_SilCoA2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoA2_SilCoA1Door": self.SilCoA2_SilCoA1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoB1_SilCoB2Spawn": self.SilCoB1_SilCoB2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoB2_SilCoB1Door": self.SilCoB2_SilCoB1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoC2_SilCoC1Spawn": self.SilCoC2_SilCoC1Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoC1_SilCoC2Door": self.SilCoC1_SilCoC2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoC1_SilCoC2Spawn": self.SilCoC1_SilCoC2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoC2_SilCoC1Door": self.SilCoC2_SilCoC1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Floor 9
            elif obj.name == "Border9":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF9Barriers.append(Rect)
            elif obj.name == "Wall9":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF9Barriers.append(Rect.Rect)
                self.Silph_CoF9Readables.append(Rect)
                self.Silph_CoF9InvisableBarrier.append(Rect)
            elif obj.name == "SilCoF8_SilCoF9Spawn": self.SilCoF8_SilCoF9Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF9_SilCoF8Door": self.SilCoF9_SilCoF8Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF10_SilCoF9Spawn": self.SilCoF10_SilCoF9Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF9_SilCoF10Door": self.SilCoF9_SilCoF10Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE_SilCoF9Spawn": self.SilCoE_SilCoF9Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF9_SilCoEDoor": self.SilCoF9_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoG1_SilCoG2Spawn": self.SilCoG1_SilCoG2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoG2_SilCoG1Door": self.SilCoG2_SilCoG1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoQ1_SilCoQ2Spawn": self.SilCoQ1_SilCoQ2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoQ2_SilCoQ1Door": self.SilCoQ2_SilCoQ1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "9Woman":
                self.SilCoF9Woman = NPC(obj.image,self.Silph_CoF9Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF9Barriers.append(self.SilCoF9Woman.rect)           
            elif obj.name == "Hidden9":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SilCoF9HiddenItems.append(H)
            #Floor 10
            elif obj.name == "Border10":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF10Barriers.append(Rect)
            elif obj.name == "Wall10":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF10Barriers.append(Rect.Rect)
                self.Silph_CoF10Readables.append(Rect)
                self.Silph_CoF10InvisableBarrier.append(Rect)
            elif obj.name == "SilCoF9_SilCoF10Spawn": self.SilCoF9_SilCoF10Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF10_SilCoF9Door": self.SilCoF10_SilCoF9Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoF11_SilCoF10Spawn": self.SilCoF11_SilCoF10Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF10_SilCoF11Door": self.SilCoF10_SilCoF11Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE_SilCoF10Spawn": self.SilCoE_SilCoF10Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF10_SilCoEDoor": self.SilCoF10_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoL1_SilCoL2Spawn": self.SilCoL1_SilCoL2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoL2_SilCoL1Door": self.SilCoL2_SilCoL1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoK1_SilCoK2Spawn": self.SilCoK1_SilCoK2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoK2_SilCoK1Door": self.SilCoK2_SilCoK1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoM1_SilCoM2Spawn": self.SilCoM1_SilCoM2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoM2_SilCoM1Door": self.SilCoM2_SilCoM1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Ball10":
                ball = Pickups((obj.x,obj.y),obj.image,self.Silph_CoF10Camera,obj.Item)
                self.SilCoF10Pickups.append(ball)
            elif obj.name == "10Woman":
                self.SilCoF10Woman = NPC(obj.image,self.Silph_CoF10Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF10Barriers.append(self.SilCoF10Woman.rect) 
            #Floor 11
            elif obj.name == "Border11":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoF11Barriers.append(Rect)
            elif obj.name == "Wall11":
                Rect = Readables(obj.x,obj.y,obj.width,obj.height,"An Invisable Wall!",obj.name,"","")
                self.Silph_CoF11Barriers.append(Rect.Rect)
                self.Silph_CoF11Readables.append(Rect)
                self.Silph_CoF11InvisableBarrier.append(Rect)
            elif obj.name == "SilCoF10_SilCoF11Spawn": self.SilCoF10_SilCoF11Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF11_SilCoF10Door": self.SilCoF11_SilCoF10Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoE_SilCoF11Spawn": self.SilCoE_SilCoF11Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoF11_SilCoEDoor": self.SilCoF11_SilCoEDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilCoP1_SilCoP2Spawn": self.SilCoP1_SilCoP2Spawn = (obj.x,obj.y)
            elif obj.name == "SilCoP2_SilCoP1Door": self.SilCoP2_SilCoP1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SilphCoGioLine":self.SilphCoGioLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Giovanni":
                self.SilCoGiovanni = TrainerNPC("Giovanni",obj.image,self.Silph_CoF11Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF11Barriers.append(self.SilCoGiovanni.rect)
            elif obj.name == "Secretary":
                self.SilCoSecretary = NPC(obj.image,self.Silph_CoF11Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Silph_CoF11Barriers.append(self.SilCoSecretary.rect)
                self.Silph_CoF11NPCS.append(self.SilCoSecretary)
            elif obj.name == "President":
                self.SilCoPresident = NPC(obj.image,self.Silph_CoF11Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="You can't buy that anywhere! It's our secret prototype MASTER BALL!",IA2="It will catch any POKEMON without fail! You should be quiet about",IA3="using it, though.")
                self.Silph_CoF11Barriers.append(self.SilCoPresident.rect)
                self.Silph_CoF11NPCS.append(self.SilCoPresident)
            #Elevator
            elif obj.name == "BorderE":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoElevatorBarriers.append(Rect)
            elif obj.name == "SilCo_SilCoESpawn": self.SilCo_SilCoESpawn = (obj.x,obj.y)
            elif obj.name == "Menu": 
                self.SilCoElevatorMenu = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Silph_CoElevatorBarriers.append(self.SilCoElevatorMenu)
            #Trainers
            elif "F2" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF2Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF2Trainers.append(trainer)
                self.Silph_CoF2Barriers.append(trainer.rect)
            elif obj.name == "Eyes2":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF2Trainereyes.append(eyes)
            elif "F3" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF3Trainers.append(trainer)
                self.Silph_CoF3Barriers.append(trainer.rect)
            elif obj.name == "Eyes3":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF3Trainereyes.append(eyes)
            elif "F4" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF4Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF4Trainers.append(trainer)
                self.Silph_CoF4Barriers.append(trainer.rect)
            elif obj.name == "Eyes4":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF4Trainereyes.append(eyes)
            elif "F5" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF5Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF5Trainers.append(trainer)
                self.Silph_CoF5Barriers.append(trainer.rect)
            elif obj.name == "Eyes5":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF5Trainereyes.append(eyes)
            elif "F6" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF6Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF6Trainers.append(trainer)
                self.Silph_CoF6Barriers.append(trainer.rect)
            elif obj.name == "Eyes6":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF6Trainereyes.append(eyes)
            elif "F7" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF7Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF7Trainers.append(trainer)
                self.Silph_CoF7Barriers.append(trainer.rect)
            elif obj.name == "Eyes7":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF7Trainereyes.append(eyes)
            elif "F8" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF8Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF8Trainers.append(trainer)
                self.Silph_CoF8Barriers.append(trainer.rect)
            elif obj.name == "Eyes8":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF8Trainereyes.append(eyes)
            elif "F9" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Silph_CoF9Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF9Trainers.append(trainer)
                self.Silph_CoF9Barriers.append(trainer.rect)
            elif obj.name == "Eyes9":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF9Trainereyes.append(eyes)
            elif "F10" in obj.name:
                trainer = TrainerNPC(obj.name[4:],obj.image,self.Silph_CoF10Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF10Trainers.append(trainer)
                self.Silph_CoF10Barriers.append(trainer.rect)
            elif obj.name == "Eyes10":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF10Trainereyes.append(eyes)
            elif "F11" in obj.name:
                trainer = TrainerNPC(obj.name[4:],obj.image,self.Silph_CoF11Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Silph_CoF11Trainers.append(trainer)
                self.Silph_CoF11Barriers.append(trainer.rect)
            elif obj.name == "Eyes11":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Silph_CoF11Trainereyes.append(eyes)

    def Load_SFH2(self):
        for layer in self.SFH2.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SFH2Camera))

        for obj in self.SFH2.objects:
            if obj.name == "Spawn": self.O_SFH2Spawn = (obj.x,obj.y)
            elif obj.name == "Door": self.SFH2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SFH2Barriers.append(Rect)
            elif obj.name == "Letter":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.SFH2Readables.append(Read)
                self.SFH2Barriers.append(Read.Rect)
            else:
                npc = NPC(obj.image,self.SFH2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SFH2NPCS.append(npc.rect)
                self.SFH2Barriers.append(npc.rect)
    
    def Load_SFH3(self):
        for layer in self.SFH3.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.SFH3F1Camera))
                    else:Tile((x*32,y*32),surf,(self.SFH3F2Camera))

        for obj in self.SFH3.objects:
            if obj.name == "O_SFH3F1Spawn": self.O_SFH3F1Spawn = (obj.x,obj.y)
            elif obj.name == "SFH3F1_ODoor": self.SFH3F1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SFH3F1Barriers.append(Rect)
            elif obj.name == "SFH3F2_SFH3F1Spawn": self.SFH3F2_SFH3F1Spawn = (obj.x,obj.y)
            elif obj.name == "SFH3F1_SFH3F2Door": self.SFH3F1_SFH3F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFH3F1_SFH3F2Spawn": self.SFH3F1_SFH3F2Spawn = (obj.x,obj.y)
            elif obj.name == "SFH3F2_SFH3F1Door": self.SFH3F2_SFH3F1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif "F1" in obj.name:
                npc = NPC(obj.image,self.SFH3F1Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SFH3F1NPCS.append(npc.rect)
                self.SFH3F1Barriers.append(npc.rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SFH3F2Barriers.append(Rect)
            elif obj.name == "Doll":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.SFH3F2Readables.append(Read)
                self.SFH3F2Barriers.append(Read.Rect)
            elif obj.name == "CopyCat":
                self.SFH3CopyCat = NPC(obj.image,self.SFH3F2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SFH3F2Barriers.append(self.SFH3CopyCat.rect)

    def Load_SaffronGym(self):
        for layer in self.SFGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.SFGymCamera))
        
        for obj in self.SFGym.objects:
            if obj.name == "Spawn": 
                self.O_SFGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.SFGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "A2_A1Spawn": self.SFA2_A1Spawn = (obj.x,obj.y)
            elif obj.name == "A1_A2Door": self.SFA1_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "A1_A2Spawn": self.SFA1_A2Spawn = (obj.x,obj.y)
            elif obj.name == "A2_A1Door": self.SFA2_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "B2_B1Spawn": self.SFB2_B1Spawn = (obj.x,obj.y)
            elif obj.name == "B1_B2Door": self.SFB1_B2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "B1_B2Spawn": self.SFB1_B2Spawn = (obj.x,obj.y)
            elif obj.name == "B2_B1Door": self.SFB2_B1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "C2_C1Spawn": self.SFC2_C1Spawn = (obj.x,obj.y)
            elif obj.name == "C1_C2Door": self.SFC1_C2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "C1_C2Spawn": self.SFC1_C2Spawn = (obj.x,obj.y)
            elif obj.name == "C2_C1Door": self.SFC2_C1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D2_D1Spawn": self.SFD2_D1Spawn = (obj.x,obj.y)
            elif obj.name == "D1_D2Door": self.SFD1_D2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D1_D2Spawn": self.SFD1_D2Spawn = (obj.x,obj.y)
            elif obj.name == "D2_D1Door": self.SFD2_D1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "E2_E1Spawn": self.SFE2_E1Spawn = (obj.x,obj.y)
            elif obj.name == "E1_E2Door": self.SFE1_E2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "E1_E2Spawn": self.SFE1_E2Spawn = (obj.x,obj.y)
            elif obj.name == "E2_E1Door": self.SFE2_E1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "F2_F1Spawn": self.SFF2_F1Spawn = (obj.x,obj.y)
            elif obj.name == "F1_F2Door": self.SFF1_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "F1_F2Spawn": self.SFF1_F2Spawn = (obj.x,obj.y)
            elif obj.name == "F2_F1Door": self.SFF2_F1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "G2_G1Spawn": self.SFG2_G1Spawn = (obj.x,obj.y)
            elif obj.name == "G1_G2Door": self.SFG1_G2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "G1_G2Spawn": self.SFG1_G2Spawn = (obj.x,obj.y)
            elif obj.name == "G2_G1Door": self.SFG2_G1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "H2_H1Spawn": self.SFH2_H1Spawn = (obj.x,obj.y)
            elif obj.name == "H1_H2Door": self.SFH1_H2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "H1_H2Spawn": self.SFH1_H2Spawn = (obj.x,obj.y)
            elif obj.name == "H2_H1Door": self.SFH2_H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "I2_I1Spawn": self.SFI2_I1Spawn = (obj.x,obj.y)
            elif obj.name == "I1_I2Door": self.SFI1_I2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "I1_I2Spawn": self.SFI1_I2Spawn = (obj.x,obj.y)
            elif obj.name == "I2_I1Door": self.SFI2_I1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "J2_J1Spawn": self.SFJ2_J1Spawn = (obj.x,obj.y)
            elif obj.name == "J1_J2Door": self.SFJ1_J2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "J1_J2Spawn": self.SFJ1_J2Spawn = (obj.x,obj.y)
            elif obj.name == "J2_J1Door": self.SFJ2_J1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "K2_K1Spawn": self.SFK2_K1Spawn = (obj.x,obj.y)
            elif obj.name == "K1_K2Door": self.SFK1_K2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "K1_K2Spawn": self.SFK1_K2Spawn = (obj.x,obj.y)
            elif obj.name == "K2_K1Door": self.SFK2_K1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "L2_L1Spawn": self.SFL2_L1Spawn = (obj.x,obj.y)
            elif obj.name == "L1_L2Door": self.SFL1_L2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "L1_L2Spawn": self.SFL1_L2Spawn = (obj.x,obj.y)
            elif obj.name == "L2_L1Door": self.SFL2_L1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "N2_N1Spawn": self.SFN2_N1Spawn = (obj.x,obj.y)
            elif obj.name == "N1_N2Door": self.SFN1_N2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "N1_N2Spawn": self.SFN1_N2Spawn = (obj.x,obj.y)
            elif obj.name == "N2_N1Door": self.SFN2_N1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "M2_M1Spawn": self.SFM2_M1Spawn = (obj.x,obj.y)
            elif obj.name == "M1_M2Door": self.SFM1_M2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "M1_M2Spawn": self.SFM1_M2Spawn = (obj.x,obj.y)
            elif obj.name == "M2_M1Door": self.SFM2_M1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O2_O1Spawn": self.SFO2_O1Spawn = (obj.x,obj.y)
            elif obj.name == "O1_O2Door": self.SFO1_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O1_O2Spawn": self.SFO1_O2Spawn = (obj.x,obj.y)
            elif obj.name == "O2_O1Door": self.SFO2_O1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SFGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.SFGymReadables.append(Read)
                self.SFGymBarriers.append(Read.Rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.SFGymTrainereyes.append(eyes)
            elif obj.name == "Sabrina":     
                self.Sabrina = GymLeaderNPC("Sabrina",obj.image,self.SFGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.SFGymBarriers.append(self.Sabrina.rect)
            elif obj.name == "Announcer":
                npc = NPC(obj.image,self.SFGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.SFGymNPCS.append(npc)
                self.SFGymBarriers.append(npc.rect)
            else:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.SFGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.SFGymTrainers.append(trainer)
                self.SFGymBarriers.append(trainer.rect)

    def Load_R12GuardHouse(self):
        for layer in self.R12GH.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.R12GHCamera))
                    else:Tile((x*32,y*32),surf,(self.R12GHF2Camera))

        for obj in self.R12GH.objects:
            if obj.name == "O_R12GuardHouseSpawn": self.O_R12GuardHouseSpawn = (obj.x,obj.y)
            elif obj.name == "R12GuardHouse_ODoor": self.R12GuardHouse_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O2_R12GuardHouseSpawn": self.O2_R12GuardHouseSpawn = (obj.x,obj.y)
            elif obj.name == "R12GuardHouse_O2Door": self.R12GuardHouse_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "F2_R12GuardHouseSpawn": self.F2_R12GuardHouseSpawn = (obj.x,obj.y)
            elif obj.name == "R12GuardHouse_F2Door": self.R12GuardHouse_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R12GuardHouseBarriers.append(Rect)
            elif obj.name == "Desk":
                self.R12GHDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R12GuardHouseBarriers.append(self.R12GHDesk)
            elif obj.name == "Guard":
                self.R12GHGuard = NPC(obj.image,self.R12GHCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            #Floor2
            elif obj.name == "R12GuardHouse_F2Spawn": self.R12GuardHouse_F2Spawn = (obj.x,obj.y)
            elif obj.name == "F2_R12GuardHouseDoor": self.F2_R12GuardHouseDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R12GuardHouseF2Barriers.append(Rect)
            elif obj.name == "Scope":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.R18GuardHouseF2Readables.append(Read)
                self.R18GuardHouseF2Barriers.append(Read.Rect)
            elif obj.name == "Girl":
                self.R12GHF2Girl = NPC(obj.image,self.R12GHF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="TM39 is a move called SWIFT. It's very accurate, so use it during",IA2="battles you can't afford to lose.",IA3="")
                self.R12GuardHouseF2Barriers.append(self.R12GHF2Girl.rect)

    def Load_R12H(self):
        for layer in self.R12H.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.R12HCamera))

        for obj in self.R12H.objects:
            if obj.name == "Spawn": self.O_R12HSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.R12H_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R12HBarriers.append(Rect)
            else:
                self.R12HFisher = NPC(obj.image,self.R12HCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Hello there, RED! Use the SUPER ROD in any water! You can catch",IA2="different kinds of POKEMON. Try fishing wherever you can!",IA3="")
                self.R12HBarriers.append(self.R12HFisher.rect)   

    def Load_R15GuardHouse(self):
        for layer in self.R15GH.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.R15GHCamera))
                    else:Tile((x*32,y*32),surf,(self.R15GHF2Camera))

        for obj in self.R15GH.objects:
            if obj.name == "R15_GHSpawn": self.R15_GHSpawn = (obj.x,obj.y)
            elif obj.name == "GH_R15Door": self.GH_R15Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "FC_GHSpawn": self.FC_GHSpawn = (obj.x,obj.y)
            elif obj.name == "GH_FCDoor": self.GH_FCDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "F2_R15GHSpawn": self.F2_R15GHSpawn = (obj.x,obj.y)
            elif obj.name == "R15GH_F2Door": self.R15GH_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R15GuardHouseBarriers.append(Rect)
            elif obj.name == "Desk":
                self.R15GHDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R15GuardHouseBarriers.append(self.R12GHDesk)
            elif obj.name == "Guard":
                self.R15GHGuard = NPC(obj.image,self.R15GHCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            #Floor2
            elif obj.name == "R15GH_F2Spawn": self.R15GH_F2Spawn = (obj.x,obj.y)
            elif obj.name == "F2_R15GHDoor": self.F2_R15GHDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.R15GuardHouseF2Barriers.append(Rect)
            elif obj.name == "Scope":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.R15GuardHouseF2Readables.append(Read)
                self.R15GuardHouseF2Barriers.append(Read.Rect)
            elif obj.name == "Aide":
                self.R15Aide = NPC(obj.image,self.R15GHF2Camera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.R15GuardHouseF2Barriers.append(self.R15Aide.rect)

    def Load_PokemonLab(self):
        for layer in self.Pokemon_Lab.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "HallWay":Tile((x*32,y*32),surf,(self.Pokemon_LabHallCamera))
                    elif layer.name == "Meeting Room":Tile((x*32,y*32),surf,(self.Pokemon_LabMRCamera))
                    elif layer.name == "R-and-D Room":Tile((x*32,y*32),surf,(self.Pokemon_LabRDCamera))
                    else:Tile((x*32,y*32),surf,(self.Pokemon_LabTRCamera))

        for obj in self.Pokemon_Lab.objects:
            if obj.name == "O_PokeLabHallSpawn": self.O_PokeLabHallSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabHall_ODoor": self.PokeLabHall_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Pokemon_LabHallBarriers.append(Rect)   
            elif obj.name == "MHMan":
                self.MHMan = NPC(obj.image,self.Pokemon_LabHallCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_LabHallBarriers.append(self.MHMan.rect)
            elif obj.name == "PokeLabMR_PokeLabHallSpawn": self.PokeLabMR_PokeLabHallSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabHall_PokeLabMRDoor": self.PokeLabHall_PokeLabMRDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeLabRD_PokeLabHallSpawn": self.PokeLabRD_PokeLabHallSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabHall_PokeLabRDDoor": self.PokeLabHall_PokeLabRDDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeLabTR_PokeLabHallSpawn": self.PokeLabTR_PokeLabHallSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabHall_PokeLabTRDoor": self.PokeLabHall_PokeLabTRDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Sign":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.Pokemon_LabHallReadables.append(Read)
                self.Pokemon_LabHallBarriers.append(Read.Rect)
            #Meeting Room
            elif obj.name == "PokeLabHall_PokeLabMRSpawn": self.PokeLabHall_PokeLabMRSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabMR_PokeLabHallDoor": self.PokeLabMR_PokeLabHallDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Pokemon_LabMRBarriers.append(Rect)   
            elif obj.name == "MROld Man":
                self.MROld_Man = TraderNPC(obj.image,self.Pokemon_LabMRCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.Pokemon_LabMRBarriers.append(self.MROld_Man.rect)
                self.Traders.append(self.MROld_Man)
            elif obj.name == "MRWoman":
                self.MRWoman = TraderNPC(obj.image,self.Pokemon_LabMRCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.Pokemon_LabMRBarriers.append(self.MRWoman.rect)
                self.Traders.append(self.MRWoman)
            elif obj.name == "MRMan":
                self.MRMan = NPC(obj.image,self.Pokemon_LabMRCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_LabMRBarriers.append(self.MRMan.rect)
            #R-D:
            elif obj.name == "PokeLabHall_PokeLabRDSpawn": self.PokeLabHall_PokeLabRDSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabRD_PokeLabHallDoor": self.PokeLabRD_PokeLabHallDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Pokemon_LabRDBarriers.append(Rect)  
            elif obj.name == "RDGiv":
                self.RDGiv = NPC(obj.image,self.Pokemon_LabRDCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Scientist",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,Item=obj.Item,ItemAmount=1,IA1="Tch-tch-tch! That's the sound of a METRONOME! It tweaks your",IA2="POKEMON's brain into using moves it doesn't know!",IA3="")
                self.Pokemon_LabRDBarriers.append(self.RDGiv.rect) 
            elif obj.name == "RDScientist":
                self.RDScientist = NPC(obj.image,self.Pokemon_LabRDCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_LabRDBarriers.append(self.RDScientist.rect)
            #TR:
            elif obj.name == "PokeLabHall_PokeLabTRSpawn": self.PokeLabHall_PokeLabTRSpawn = (obj.x,obj.y)
            elif obj.name == "PokeLabTR_PokeLabHallDoor": self.PokeLabTR_PokeLabHallDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Pokemon_LabTRBarriers.append(Rect)  
            elif obj.name == "TRMan":
                self.TRMan = TraderNPC(obj.image,self.Pokemon_LabTRCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3,HisPokemon=obj.HisPokemon,YourPokemon=obj.YourPokemon,PokeNickName=obj.Nickname)
                self.Traders.append(self.TRMan)
                self.Pokemon_LabTRBarriers.append(self.TRMan.rect)
            elif obj.name == "TRScientist":
                self.TRScientist = NPC(obj.image,self.Pokemon_LabTRCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name[2:],Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.Pokemon_LabTRBarriers.append(self.TRScientist.rect)

    def Load_PokemonMansion(self):
        for layer in self.Pokemon_Mansion.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.Pokemon_MansionF1Camera))
                    elif layer.name == "Floor 2":Tile((x*32,y*32),surf,(self.Pokemon_MansionF2Camera))
                    elif layer.name == "Floor 3":Tile((x*32,y*32),surf,(self.Pokemon_MansionF3Camera))
                    else:Tile((x*32,y*32),surf,(self.Pokemon_MansionFB1Camera))

        for obj in self.Pokemon_Mansion.objects:
            if obj.name == "O_PokeMansionF1Spawn": self.O_PokeMansionF1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionF1_ODoor": self.PokeMansionF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionA2_A1Spawn": self.PokeMansionA2_A1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionA1_A2Door": self.PokeMansionA1_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionG2_G1Spawn": self.PokeMansionG2_G1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionG1_G2Door": self.PokeMansionG1_G2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeMansionF1Barriers.append(Rect)
            elif obj.name == "PokeMansionD_DSpawn": self.PokeMansionD_DSpawn = (obj.x,obj.y)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_MansionF1Camera,obj.Item)
                self.Pokemon_MansionF1Pickups.append(ball)
            elif obj.name == "Exit": self.PokeMansionExitDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "WallA":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF1Camera))
                self.Pokemon_MansionF1WallsA.append([Rect,wall])
                self.PokeMansionF1Barriers.append(Rect)
            elif obj.name == "WallB":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF1Camera))
                self.Pokemon_MansionF1WallsB.append([Rect,wall])
                self.PokeMansionF1Barriers.append(Rect)
            elif obj.name == "Switch":self.PokeMansionF1Switch = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.PokeMansionF1HiddenItems.append(H)
            elif obj.name == "Tile":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Pokemon_MansionF1Blocks.append(WildTile)
            #Floor2
            elif obj.name == "PokeMansionA1_A2Spawn": self.PokeMansionA1_A2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionA2_A1Door": self.PokeMansionA2_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionB2_B1Spawn": self.PokeMansionB2_B1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionB1_B2Door": self.PokeMansionB1_B2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeMansionF2Barriers.append(Rect)
            elif obj.name == "Book2":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF2Camera))
                self.PokeMansionF2Readables.append(Read)
                self.PokeMansionF2Barriers.append(Read.Rect)
            elif obj.name == "Wall2A":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF2Camera))
                self.Pokemon_MansionF2WallsA.append([Rect,wall])
                self.PokeMansionF2Barriers.append(Rect)
            elif obj.name == "Wall2B":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF2Camera))
                self.Pokemon_MansionF2WallsB.append([Rect,wall])
                self.PokeMansionF2Barriers.append(Rect)
            elif obj.name == "Switch2":self.PokeMansionF2Switch = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "PokeMansionC2_C1Spawn": self.PokeMansionC2_C1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionC1_C2Door": self.PokeMansionC1_C2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionF2_F1Spawn": self.PokeMansionF2_F1Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionF1_F2Door": self.PokeMansionF1_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionE_ESpawn": self.PokeMansionE_ESpawn = (obj.x,obj.y)
            elif obj.name == "Ball2":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_MansionF2Camera,obj.Item)
                self.Pokemon_MansionF2Pickups.append(ball)
            elif obj.name == "Tile2":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Pokemon_MansionF2Blocks.append(WildTile)
            #Floor 3
            elif obj.name == "PokeMansionC1_C2Spawn": self.PokeMansionC1_C2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionC2_C1Door": self.PokeMansionC2_C1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionB1_B2Spawn": self.PokeMansionB1_B2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionB2_B1Door": self.PokeMansionB2_B1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeMansionF3Barriers.append(Rect)
            elif obj.name == "PokeMansionD_DDoor": self.PokeMansionD_DDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PokeMansionE_EDoor": self.PokeMansionE_EDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wall3A":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF3Camera))
                self.Pokemon_MansionF3WallsA.append([Rect,wall])
                self.PokeMansionF3Barriers.append(Rect)
            elif obj.name == "Wall3B":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF3Camera))
                self.Pokemon_MansionF3WallsB.append([Rect,wall])
                self.PokeMansionF3Barriers.append(Rect)
            elif obj.name == "Switch3":self.PokeMansionF3Switch = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Book3":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionF3Camera))
                self.PokeMansionF3Readables.append(Read)
                self.PokeMansionF3Barriers.append(Read.Rect)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_MansionF3Camera,obj.Item)
                self.Pokemon_MansionF3Pickups.append(ball)
            elif obj.name == "PokeMansionF1_F2Spawn": self.PokeMansionF1_F2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionF2_F1Door": self.PokeMansionF2_F1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden3":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.PokeMansionF3HiddenItems.append(H)
            elif obj.name == "Tile3":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Pokemon_MansionF3Blocks.append(WildTile)
            #Floor 4
            elif obj.name == "PokeMansionG1_G2Spawn": self.PokeMansionG1_G2Spawn = (obj.x,obj.y)
            elif obj.name == "PokeMansionG2_G1Door": self.PokeMansionG2_G1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PokeMansionFB1Barriers.append(Rect)
            elif obj.name == "Wall4A":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionFB1Camera))
                self.Pokemon_MansionFB1WallsA.append([Rect,wall])
                self.PokeMansionFB1Barriers.append(Rect)
            elif obj.name == "Wall4B":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionFB1Camera))
                self.Pokemon_MansionFB1WallsB.append([Rect,wall])
                self.PokeMansionFB1Barriers.append(Rect)
            elif obj.name == "Switch4A":self.PokeMansionFB1ASwitch = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Switch4B":self.PokeMansionFB1BSwitch = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Book4":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.Pokemon_MansionFB1Camera))
                self.PokeMansionFB1Readables.append(Read)
                self.PokeMansionFB1Barriers.append(Read.Rect)
            elif obj.name == "Ball4":
                ball = Pickups((obj.x,obj.y),obj.image,self.Pokemon_MansionFB1Camera,obj.Item)
                self.Pokemon_MansionFB1Pickups.append(ball)
            elif obj.name == "Hidden4":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.PokeMansionFB1HiddenItems.append(H)
            elif obj.name == "Tile4":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Pokemon_MansionFB1Blocks.append(WildTile)
            elif "F1" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_MansionF1Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Pokemon_MansionF1Trainers.append(trainer)
                self.PokeMansionF1Barriers.append(trainer.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Pokemon_MansionF1Trainereyes.append(eyes)
            elif "F2" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_MansionF2Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Pokemon_MansionF2Trainers.append(trainer)
                self.PokeMansionF2Barriers.append(trainer.rect)
            elif obj.name == "Eyes2":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Pokemon_MansionF2Trainereyes.append(eyes)
            elif "F3" in obj.name:
                trainer = TrainerNPC(obj.name[3:],obj.image,self.Pokemon_MansionF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Pokemon_MansionF3Trainers.append(trainer)
                self.PokeMansionF3Barriers.append(trainer.rect)
            elif obj.name == "Eyes3":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Pokemon_MansionF3Trainereyes.append(eyes)
            elif "FB1" in obj.name:
                trainer = TrainerNPC(obj.name[4:],obj.image,self.Pokemon_MansionFB1Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.Pokemon_MansionFB1Trainers.append(trainer)
                self.PokeMansionFB1Barriers.append(trainer.rect)
            elif obj.name == "Eyes4":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.Pokemon_MansionFB1Trainereyes.append(eyes)

    def Load_CinnabarGym(self):
        for layer in self.CGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.CGymCamera))
        
        for obj in self.CGym.objects:
            if obj.name == "Spawn": 
                self.O_CGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.CGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.CGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.CGymReadables.append(Read)
                self.CGymBarriers.append(Read.Rect)
            elif obj.name == "Blaine":     
                self.Blaine = GymLeaderNPC("Blaine",obj.image,self.CGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.CGymBarriers.append(self.Blaine.rect)
            elif obj.name == "Announcer":
                self.CGymAnnouncer = NPC(obj.image,self.CGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.CGymBarriers.append(self.CGymAnnouncer.rect)
            elif obj.name == "Wall1":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.CGymCamera))
                self.CGymWall1.append([Rect,wall])
                self.CGymBarriers.append(Rect)
            elif obj.name == "Wall2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.CGymCamera))
                self.CGymWall2.append([Rect,wall])
                self.CGymBarriers.append(Rect)
            elif obj.name == "Wall3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.CGymCamera))
                self.CGymWall3.append([Rect,wall])
                self.CGymBarriers.append(Rect)
            elif obj.name == "Wall4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.CGymCamera))
                self.CGymWall4.append([Rect,wall])
                self.CGymBarriers.append(Rect)
            elif obj.name == "Wall5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.CGymCamera))
                self.CGymWall5.append([Rect,wall])
                self.CGymBarriers.append(Rect)
            elif obj.name == "Wall6":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.CGymCamera))
                self.CGymWall6.append([Rect,wall])
                self.CGymBarriers.append(Rect)
            elif obj.name == "Q1":
                self.CGymQuestion1 = Question(obj.x,obj.y,obj.width,obj.height,obj.Question)
                self.CGymBarriers.append(self.CGymQuestion1.Rect)
            elif obj.name == "Q2":
                self.CGymQuestion2 = Question(obj.x,obj.y,obj.width,obj.height,obj.Question)
                self.CGymBarriers.append(self.CGymQuestion2.Rect)
            elif obj.name == "Q3":
                self.CGymQuestion3 = Question(obj.x,obj.y,obj.width,obj.height,obj.Question)
                self.CGymBarriers.append(self.CGymQuestion3.Rect)
            elif obj.name == "Q4":
                self.CGymQuestion4 = Question(obj.x,obj.y,obj.width,obj.height,obj.Question)
                self.CGymBarriers.append(self.CGymQuestion4.Rect)
            elif obj.name == "Q5":
                self.CGymQuestion5 = Question(obj.x,obj.y,obj.width,obj.height,obj.Question)
                self.CGymBarriers.append(self.CGymQuestion5.Rect)
            elif obj.name == "Q6":
                self.CGymQuestion6 = Question(obj.x,obj.y,obj.width,obj.height,obj.Question)
                self.CGymBarriers.append(self.CGymQuestion6.Rect)
            else:
                trainer = TrainerNPC(obj.name[2:],obj.image,self.CGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.CGymTrainers.append(trainer)
                self.CGymBarriers.append(trainer.rect)

    def Load_ViridianGym(self):
        for layer in self.VGym.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.VGymCamera))
        
        for obj in self.VGym.objects:
            if obj.name == "Spawn": 
                self.O_VGymSpawn = (obj.x,obj.y)
            elif obj.name == "Door": self.VGym_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "L1MoverSpawn": self.VGymL1MoverSpawn = (obj.x,obj.y)
            elif obj.name == "L1Mover": self.VGymL1Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "L2MoverSpawn": self.VGymL2MoverSpawn = (obj.x,obj.y)
            elif obj.name == "L2Mover": self.VGymL2Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "L3MoverSpawn": self.VGymL3MoverSpawn = (obj.x,obj.y)
            elif obj.name == "L3Mover": self.VGymL3Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "U1MoverSpawn": self.VGymU1MoverSpawn = (obj.x,obj.y)
            elif obj.name == "U1Mover": self.VGymU1Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "U2MoverSpawn": self.VGymU2MoverSpawn = (obj.x,obj.y)
            elif obj.name == "U2Mover": self.VGymU2Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "U3MoverSpawn": self.VGymU3MoverSpawn = (obj.x,obj.y)
            elif obj.name == "U3Mover": self.VGymU3Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R1MoverSpawn": self.VGymR1MoverSpawn = (obj.x,obj.y)
            elif obj.name == "R1Mover": self.VGymR1Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R2MoverSpawn": self.VGymR2MoverSpawn = (obj.x,obj.y)
            elif obj.name == "R2Mover": self.VGymR2Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "R3MoverSpawn": self.VGymR3MoverSpawn = (obj.x,obj.y)
            elif obj.name == "R3Mover": self.VGymR3Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D1MoverSpawn": self.VGymD1MoverSpawn = (obj.x,obj.y)
            elif obj.name == "D1Mover": self.VGymD1Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D2MoverSpawn": self.VGymD2MoverSpawn = (obj.x,obj.y)
            elif obj.name == "D2Mover": self.VGymD2Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "D3MoverSpawn": self.VGymD3MoverSpawn = (obj.x,obj.y)
            elif obj.name == "D3Mover": self.VGymD3Mover = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VGymBarriers.append(Rect)
            elif obj.name == "Totem":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,obj.Text2,obj.Text3)
                self.VGymReadables.append(Read)
                self.VGymBarriers.append(Read.Rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.VGymTrainereyes.append(eyes)
            elif obj.name == "Giovanni":     
                self.GymGiovanni = GymLeaderNPC("Giovanni",obj.image,self.VGymCamera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.VGymBarriers.append(self.GymGiovanni.rect)
            elif obj.name == "Announcer":
                self.VGymAnnouncer = NPC(obj.image,self.VGymCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.VGymBarriers.append(self.VGymAnnouncer.rect)
            else:
                trainer = TrainerNPC(obj.name[2:],obj.image,self.VGymCamera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.VGymTrainers.append(trainer)
                self.VGymBarriers.append(trainer.rect)

    def Load_Victory_Road(self):
        for layer in self.VRoad.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.VRoadF1Camera))
                    elif layer.name == "Floor 2":Tile((x*32,y*32),surf,(self.VRoadF2Camera))
                    else:Tile((x*32,y*32),surf,(self.VRoadF3Camera))

        for obj in self.VRoad.objects:
            if obj.name == "O_VictoryRoadF1Spawn": self.O_VictoryRoadF1Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadF1_ODoor": self.VictoryRoadF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Boulder":
                x = Rocks((obj.x,obj.y),obj.image,self.VRoadF1Camera,self.VRoadF1Barriers,Cameras=(self.VRoadF1Camera,self.VRoadF2Camera,self.VRoadF3Camera))
                self.VRoadF1Barriers.append(x.rect)
                self.VRoadF1Boulders.append(x)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VRoadF1Barriers.append(Rect)
            elif obj.name == "Ball1":
                ball = Pickups((obj.x,obj.y),obj.image,self.VRoadF1Camera,obj.Item)
                self.VRoadF1Pickups.append(ball)
            elif obj.name == "Button":
                self.VRoadF1Button = Tile((obj.x,obj.y),obj.image,(self.VRoadF1Camera))
            elif obj.name == "Wall":
                self.VRoadF1Wall = [pygame.Rect(obj.x,obj.y,obj.width,obj.height),Tile((obj.x,obj.y),obj.image,(self.VRoadF1Camera))]      
                self.VRoadF1Barriers.append(self.VRoadF1Wall[0])
            elif obj.name == "VictoryRoadA2_A1Spawn": self.VictoryRoadA2_A1Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadA1_A2Door": self.VictoryRoadA1_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Rocks":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.VRoadF1Blocks.append(WildTile)
            #
            elif obj.name == "Boulder2":
                x = Rocks((obj.x,obj.y),obj.image,self.VRoadF2Camera,self.VRoadF2Barriers,Cameras=(self.VRoadF1Camera,self.VRoadF2Camera,self.VRoadF3Camera))
                self.VRoadF2Barriers.append(x.rect)
                self.VRoadF2Boulders.append(x)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VRoadF2Barriers.append(Rect)
            elif obj.name == "Ball2":
                ball = Pickups((obj.x,obj.y),obj.image,self.VRoadF2Camera,obj.Item)
                self.VRoadF2Pickups.append(ball)
            elif obj.name == "Button21":
                self.VRoadF21Button = Tile((obj.x,obj.y),obj.image,(self.VRoadF2Camera))
            elif obj.name == "Button22":
                self.VRoadF22Button = Tile((obj.x,obj.y),obj.image,(self.VRoadF2Camera))
            elif obj.name == "Wall21":
                rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.VRoadF2Camera))
                self.VRoadF21Wall.append([rect,wall])   
                self.VRoadF2Barriers.append(rect)
            elif obj.name == "VictoryRoadA2_A1Door": self.VictoryRoadA2_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadA1_A2Spawn": self.VictoryRoadA1_A2Spawn = (obj.x,obj.y)
            elif obj.name == "Wall22":
                rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.VRoadF2Camera))
                self.VRoadF22Wall.append([rect,wall])   
                self.VRoadF2Barriers.append(rect)
            elif obj.name == "Hidden2":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.VRoadF2HiddenItems.append(H)
            elif obj.name == "VictoryRoadB2_B1Door": self.VictoryRoadB2_B1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadB1_B2Spawn": self.VictoryRoadB1_B2Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadB1_B2Door": self.VictoryRoadB1_B2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadB2_B1Spawn": self.VictoryRoadB2_B1Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadC2_C1Door": self.VictoryRoadC2_C1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadC1_C2Spawn": self.VictoryRoadC1_C2Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadC1_C2Door": self.VictoryRoadC1_C2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadC2_C1Spawn": self.VictoryRoadC2_C1Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadD1_D2Door": self.VictoryRoadD1_D2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadD2_D1Spawn": self.VictoryRoadD2_D1Spawn = (obj.x,obj.y)
            elif obj.name == "Moltres":
                self.Moltres = Tile((obj.x,obj.y),obj.image,(self.VRoadF2Camera))
                self.VRoadF2Barriers.append(self.Moltres.rect)
            elif obj.name == "VictoryRoadD2_D1Door": self.VictoryRoadD2_D1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadD1_D2Spawn": self.VictoryRoadD1_D2Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadE2_E1Door": self.VictoryRoadE2_E1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadE1_E2Spawn": self.VictoryRoadE1_E2Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadE1_E2Door": self.VictoryRoadE1_E2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadE2_E1Spawn": self.VictoryRoadE2_E1Spawn = (obj.x,obj.y)
            elif obj.name == "VictoryRoadF3_F2Door": self.VictoryRoadF3_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "VictoryRoadF3_F2Spawn": self.VictoryRoadF3_F2Spawn = (obj.x,obj.y)
            elif obj.name == "Rocks2":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.VRoadF2Blocks.append(WildTile)
            elif obj.name == "VictoryRoadF2_ODoor": self.VictoryRoadF2_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_VictoryRoadF2Spawn": self.O_VictoryRoadF2Spawn = (obj.x,obj.y)
            elif obj.name == "Boulder3":
                x = Rocks((obj.x,obj.y),obj.image,self.VRoadF3Camera,self.VRoadF3Barriers,Cameras=(self.VRoadF1Camera,self.VRoadF2Camera,self.VRoadF3Camera))
                self.VRoadF3Barriers.append(x.rect)
                self.VRoadF3Boulders.append(x)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.VRoadF3Barriers.append(Rect)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.VRoadF3Camera,obj.Item)
                self.VRoadF3Pickups.append(ball)
            elif obj.name == "Button3":
                self.VRoadF3Button = Tile((obj.x,obj.y),obj.image,(self.VRoadF3Camera))
            elif obj.name == "Wall3":
                self.VRoadF3Wall = [pygame.Rect(obj.x,obj.y,obj.width,obj.height),Tile((obj.x,obj.y),obj.image,(self.VRoadF3Camera))]      
                self.VRoadF3Barriers.append(self.VRoadF3Wall[0])
            elif obj.name == "Rocks3":
                WildTile = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.VRoadF3Blocks.append(WildTile)
            elif "VRF1" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.VRoadF1Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.VRoadF1Trainers.append(trainer)
                self.VRoadF1Barriers.append(trainer.rect)
            elif obj.name == "Eyes":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.VRoadF1Trainereyes.append(eyes)
            elif "VRF2" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.VRoadF2Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.VRoadF2Trainers.append(trainer)
                self.VRoadF2Barriers.append(trainer.rect)
            elif obj.name == "Eyes2":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.VRoadF2Trainereyes.append(eyes)
            elif "VRF3" in obj.name:
                trainer = TrainerNPC(obj.name[5:],obj.image,self.VRoadF3Camera,(obj.x,obj.y),obj.Team,obj.BattleStart.split("-"),obj.AfterBattle.split("-"),obj.Money,obj.BattleEnd.split("-"),obj.Side,obj.Bag,obj.name)
                self.VRoadF3Trainers.append(trainer)
                self.VRoadF3Barriers.append(trainer.rect)
            elif obj.name == "Eyes3":
                eyes = TrainerVision(obj.x,obj.y,obj.width,obj.height,obj.Trainer)
                self.VRoadF3Trainereyes.append(eyes)

    def Load_IndigoPlateauEntrance(self):
        for layer in self.IndigoPlateauEntrance.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.IndigoPlateauEntranceCamera))

        for obj in self.IndigoPlateauEntrance.objects:
            if obj.name == "O_ILESpawn": self.O_ILESpawn = (obj.x,obj.y)
            elif obj.name == "ILE_ODoor": self.ILE_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Nurse": self.ILE_Nurse = NPC(obj.image,self.IndigoPlateauEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,"Nurse",Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
            elif obj.name == "HealDesk": 
                self.ILENurse_desk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoLeagueEntranceBarriers.append(self.ILENurse_desk)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoLeagueEntranceBarriers.append(Rect)
            elif obj.name == "PC": 
                self.ILEPC = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoLeagueEntranceBarriers.append(self.ILEPC)
            elif obj.name == "Store Clerk": 
                self.ILEClerk = NPC(obj.image,self.IndigoPlateauEntranceCamera,"Merchant",(obj.x,obj.y),obj.Dialouge,obj.name)
                self.ILEClerk.Store = [["Ultra Ball",1200],["Great Ball",600],["Escape Rope",550],["Full Restore",3000],["Max Potion",2500],["Revive",1500],["Full Heal",600],["Max Repel",700]]
            elif obj.name == "MartDesk": 
                self.MartDesk = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoLeagueEntranceBarriers.append(self.MartDesk)
            elif obj.name == "ILE_E4Door": self.ILE_E4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            else: 
                npc = NPC(obj.image,self.IndigoPlateauEntranceCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.IndigoLeagueEntranceNPCS.append(npc)
                self.IndigoLeagueEntranceBarriers.append(npc.rect)
            
    def Load_IndigoPlateau(self):
        for layer in self.IndigoPlateau.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Lorelei's room":Tile((x*32,y*32),surf,(self.IndigoPlateauE1Camera))
                    elif layer.name == "Bruno's Room":Tile((x*32,y*32),surf,(self.IndigoPlateauE2Camera))
                    elif layer.name == "Agatha's Room":Tile((x*32,y*32),surf,(self.IndigoPlateauE3Camera))
                    else:Tile((x*32,y*32),surf,(self.IndigoPlateauE4Camera))
        
        for obj in self.IndigoPlateau.objects:
            if obj.name == "IceSpawn": 
                self.IceSpawn = (obj.x,obj.y)
            elif obj.name == "IndigoPlateauE1_E2Door": self.IndigoPlateauE1_E2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoPlateauE1Barriers.append(Rect)
            elif obj.name == "Lorelei":     
                self.Lorelei = GymLeaderNPC("Lorelei",obj.image,self.IndigoPlateauE1Camera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3,obj.Dialouge4],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.IndigoPlateauE1Barriers.append(self.Lorelei.rect)
            elif obj.name == "Wall":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.IndigoPlateauE1Camera))
                self.IPE1Wall.append([Rect,wall])
                self.IndigoPlateauE1Barriers.append(Rect)
            elif obj.name == "RockSpawn": 
                self.RockSpawn = (obj.x,obj.y)
            elif obj.name == "IndigoPlateauE2_E3Door": self.IndigoPlateauE2_E3Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoPlateauE2Barriers.append(Rect)
            elif obj.name == "Bruno":     
                self.Bruno = GymLeaderNPC("Bruno",obj.image,self.IndigoPlateauE2Camera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3,obj.Dialouge4],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.IndigoPlateauE2Barriers.append(self.Bruno.rect)
            elif obj.name == "Wall2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.IndigoPlateauE2Camera))
                self.IPE2Wall.append([Rect,wall])
                self.IndigoPlateauE2Barriers.append(Rect)
            elif obj.name == "GhostSpawn": 
                self.GhostSpawn = (obj.x,obj.y)
            elif obj.name == "IndigoPlateauE3_E4Door": self.IndigoPlateauE3_E4Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoPlateauE3Barriers.append(Rect)
            elif obj.name == "Agatha":     
                self.Agatha = GymLeaderNPC("Agatha",obj.image,self.IndigoPlateauE3Camera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3,obj.Dialouge4],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.IndigoPlateauE3Barriers.append(self.Agatha.rect)
            elif obj.name == "Wall3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.IndigoPlateauE3Camera))
                self.IPE3Wall.append([Rect,wall])
                self.IndigoPlateauE3Barriers.append(Rect)
            elif obj.name == "DragonSpawn": 
                self.DragonSpawn = (obj.x,obj.y)
            elif obj.name == "IndigoPlateauE4_CDoor": self.IndigoPlateauE4_CDoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoPlateauE4Barriers.append(Rect)
            elif obj.name == "Lance":     
                self.Lance = GymLeaderNPC("Lance",obj.image,self.IndigoPlateauE4Camera,(obj.x,obj.y),obj.Team,[obj.Dialouge,obj.Dialouge2,obj.Dialouge3,obj.Dialouge4],[obj.AfterBattle,obj.AfterBattle2,obj.AfterBattle3],obj.Money,[obj.WonBattle1,obj.WonBattle2,obj.WonBattle3],obj.Bag,[obj.WonBattle4,obj.WonBattle5,obj.WonBattle6])
                self.IndigoPlateauE4Barriers.append(self.Lance.rect)
            elif obj.name == "Wall4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                wall = Tile((obj.x,obj.y),obj.image,(self.IndigoPlateauE4Camera))
                self.IPE4Wall.append([Rect,wall])
                self.IndigoPlateauE4Barriers.append(Rect)
            elif obj.name == "BattleLine":self.E4LanceBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)

    def Load_IndigoPlateauChampion(self):
        for layer in self.IndigoPlateauChampion.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.IndigoPlateauChampionCamera))

        for obj in self.IndigoPlateauChampion.objects:
            if obj.name == "CSpawn": self.IndigoPlateauE4_CSpawn = (obj.x,obj.y)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.IndigoPlateauChampionBarriers.append(Rect)
            elif obj.name == "FinalBattleLine":self.FinalBattleLine = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
            elif obj.name == "Oak":
                self.IPCOak = NPC(obj.image,self.IndigoPlateauChampionCamera,obj.Type,(obj.x,obj.y),obj.Dialouge,obj.name,Text1_b=obj.Dialouge2,Text1_c=obj.Dialouge3)
                self.IndigoPlateauChampionCamera.remove(self.IPCOak)

    def Load_Hall_of_Fame(self):
        for layer in self.Fame_Hall.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Fame_HallCamera))

        for obj in self.Fame_Hall.objects:
            if obj.name == "Spawn": self.FameHallSpawn = (obj.x,obj.y)
            else:
                Tile((obj.x,obj.y),obj.image,(self.Fame_HallCamera))
        
    def Load_Power_Plant(self):
        for layer in self.Power_Plant.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    Tile((x*32,y*32),surf,(self.Power_PlantCamera))

        for obj in self.Power_Plant.objects:
            if obj.name == "O_PPSpawn": self.O_PPSpawn = (obj.x,obj.y)
            elif obj.name == "PP_ODoor": self.PP_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "PP_O2Door": self.PP_O2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.PowerPlantBarriers.append(Rect)
            elif obj.name == "WIld_Tile":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.PowerPlantWilds.append(Rock)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.Power_PlantCamera,obj.Item)
                self.Power_PlantPickups.append(ball)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.Power_PlantHiddenItems.append(H)
            elif obj.name == "Zapdos":
                self.Zapdos = Tile((obj.x,obj.y),obj.image,(self.Power_PlantCamera))
                self.PowerPlantBarriers.append(self.Zapdos.rect)
            elif obj.name == "Fake":
                ball = Pickups((obj.x,obj.y),obj.image,self.Power_PlantCamera,obj.Item)
                self.FakePower_PlantPickups.append(ball)
    
    def Load_SeaFoam_Islands(self):
        for layer in self.SeaFoam_Island.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.SeaFoam_IslandF1Camera))
                    elif layer.name == "Basement Floor 1":Tile((x*32,y*32),surf,(self.SeaFoam_IslandFB1Camera))
                    elif layer.name == "Basement Floor 2":Tile((x*32,y*32),surf,(self.SeaFoam_IslandFB2Camera))
                    elif layer.name == "Basement Floor 3":Tile((x*32,y*32),surf,(self.SeaFoam_IslandFB3Camera))
                    else:Tile((x*32,y*32),surf,(self.SeaFoam_IslandFB4Camera))

        for obj in self.SeaFoam_Island.objects:
            if obj.name == "O_LSFIF1Spawn": self.O_LSFIF1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIF1_ODoor": self.LSFIF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "O_RSFIF1Spawn": self.O_RSFIF1Spawn = (obj.x,obj.y)
            elif obj.name == "RSFIF1_ODoor": self.RSFIF1_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandF1Barriers.append(Rect)
            elif obj.name == "Boulder":
                x = Rocks((obj.x,obj.y),obj.image,self.SeaFoam_IslandF1Camera,self.SeaFoam_IslandF1Barriers)
                self.SeaFoam_IslandF1Barriers.append(x.rect)
                self.SeaFoam_IslandF1Boulders.append(x)
            elif obj.name == "LSFIA2_A1Spawn": self.LSFIA2_A1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIA1_A2Door": self.LSFIA1_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIB2_B1Spawn": self.LSFIB2_B1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIB1_B2Door": self.LSFIB1_B2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIL2_L1Spawn": self.LSFIL2_L1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIL1_L2Door": self.LSFIL1_L2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFIF1_BF1Hole": self.SFIF1_BF1Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFIF1_BF12Hole": self.SFIF1_BF12Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wild Rocks":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SeaFoam_IslandF1Wilds.append(Rock)
            #Floor 2
            elif obj.name == "LSFIL1_L2Spawn": self.LSFIL1_L2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIL2_L1Door": self.LSFIL2_L1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIA1_A2Spawn": self.LSFIA1_A2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIA2_A1Door": self.LSFIA2_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIB1_B2Spawn": self.LSFIB1_B2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIB2_B1Door": self.LSFIB2_B1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB1Barriers.append(Rect)
            elif obj.name == "LSFIC2_C1Spawn": self.LSFIC2_C1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIC1_C2Door": self.LSFIC1_C2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFID2_D1Spawn": self.LSFID2_D1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFID1_D2Door": self.LSFID1_D2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIE2_E1Spawn": self.LSFIE2_E1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIE1_E2Door": self.LSFIE1_E2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIK2_K1Spawn": self.LSFIK2_K1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIK1_K2Door": self.LSFIK1_K2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFIF1_BF12Spawn": self.SFIF1_BF12Spawn = (obj.x,obj.y)
            elif obj.name == "SFIF1_BF1Spawn": self.SFIF1_BF1Spawn = (obj.x,obj.y)
            elif obj.name == "SFIFB1_BF2Hole": self.SFIFB1_BF2Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFIFB1_BF22Hole": self.SFIFB1_BF22Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wild Rocks2":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SeaFoam_IslandFB1Wilds.append(Rock)
            #Floor 3
            elif obj.name == "LSFIC1_C2Spawn": self.LSFIC1_C2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIC2_C1Door": self.LSFIC2_C1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFID1_D2Spawn": self.LSFID1_D2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFID2_D1Door": self.LSFID2_D1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIE1_E2Spawn": self.LSFIE1_E2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIE2_E1Door": self.LSFIE2_E1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIK1_K2Spawn": self.LSFIK1_K2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIK2_K1Door": self.LSFIK2_K1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB2Barriers.append(Rect)
            elif obj.name == "LSFIF2_F1Spawn": self.LSFIF2_F1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIF1_F2Door": self.LSFIF1_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIH2_H1Spawn": self.LSFIH2_H1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIH1_H2Door": self.LSFIH1_H2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFII2_I1Spawn": self.LSFII2_I1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFII1_I2Door": self.LSFII1_I2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Hidden3":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SeaFoam_IslandFB2HiddenItems.append(H)
            elif obj.name == "SFIFB1_BF22Spawn": self.SFIFB1_BF22Spawn = (obj.x,obj.y)
            elif obj.name == "SFIFB1_BF2Spawn": self.SFIFB1_BF2Spawn = (obj.x,obj.y)
            elif obj.name == "SFIFB2_BF32Hole": self.SFIFB2_BF32Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFIFB2_BF3Hole": self.SFIFB2_BF3Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wild Rocks3":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SeaFoam_IslandFB2Wilds.append(Rock)
            #Floor 4
            elif obj.name == "LSFII1_I2Spawn": self.LSFII1_I2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFII2_I1Door": self.LSFII2_I1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIH1_H2Spawn": self.LSFIH1_H2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIH2_H1Door": self.LSFIH2_H1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIF1_F2Spawn": self.LSFIF1_F2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIF2_F1Door": self.LSFIF2_F1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB3Barriers.append(Rect)
            elif obj.name == "LSFIJ2_J1Spawn": self.LSFIJ2_J1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIJ1_J2Door": self.LSFIJ1_J2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIG2_G1Spawn": self.LSFIG2_G1Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIG1_G2Door": self.LSFIG1_G2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Boulder4":
                x = Rocks((obj.x,obj.y),obj.image,self.SeaFoam_IslandFB3Camera,self.SeaFoam_IslandFB3Barriers)
                self.SeaFoam_IslandFB3Barriers.append(x.rect)
                self.SeaFoam_IslandFB3Boulders.append(x)
            elif obj.name == "SFIFB2_BF32Spawn": self.SFIFB2_BF32Spawn = (obj.x,obj.y)
            elif obj.name == "SFIFB2_BF3Spawn": self.SFIFB2_BF3Spawn = (obj.x,obj.y)
            elif obj.name == "SFIFB2_BF33Spawn": self.SFIFB2_BF33Spawn = (obj.x,obj.y)
            elif obj.name == "Hidden4":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SeaFoam_IslandFB3HiddenItems.append(H)
            elif obj.name == "SFIFB3_BF42Hole": self.SFIFB3_BF42Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "SFIFB3_BF4Hole": self.SFIFB3_BF4Hole = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Wild Rocks4":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SeaFoam_IslandFB3Wilds.append(Rock)
            elif obj.name == "Seapoint4":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB3FishingPoint.append(Rect)
                self.SeaFoam_IslandFB3Barriers.append(Rect)
            #Floor 5
            elif obj.name == "SFIFB3_BF4Spawn": self.SFIFB3_BF4Spawn = (obj.x,obj.y)
            elif obj.name == "SFIFB3_BF42Spawn": self.SFIFB3_BF42Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIG1_G2Spawn": self.LSFIG1_G2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIG2_G1Door": self.LSFIG2_G1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "LSFIJ1_J2Spawn": self.LSFIJ1_J2Spawn = (obj.x,obj.y)
            elif obj.name == "LSFIJ2_J1Door": self.LSFIJ2_J1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB4Barriers.append(Rect)
            elif obj.name == "Hidden5":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.SeaFoam_IslandFB4HiddenItems.append(H)         
            elif obj.name == "SFIWaveSpawn": self.SFIWaveSpawn = (obj.x,obj.y)
            elif obj.name == "SFIWave2Spawn": self.SFIWave2Spawn = (obj.x,obj.y)
            elif obj.name == "SFIWave3Spawn": self.SFIWave3Spawn = (obj.x,obj.y)
            elif obj.name == "Seapoint5":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB4FishingPoint.append(Rect)
                self.SeaFoam_IslandFB4Barriers.append(Rect)
            elif obj.name == "Seapoint2":
                self.SFIBF4Risingpoint = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.SeaFoam_IslandFB4Barriers.append(self.SFIBF4Risingpoint)
            elif obj.name == "Wild Rocks5":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.SeaFoam_IslandFB4Wilds.append(Rock)
            elif obj.name == "Articuno":
                self.Articuno = Tile((obj.x,obj.y),obj.image,(self.SeaFoam_IslandFB4Camera))
                self.SeaFoam_IslandFB4Barriers.append(self.Articuno.rect)
            elif obj.name == "Sign5":
                Read = Readables(obj.x,obj.y,obj.width,obj.height,obj.Text,obj.name,Text2=obj.Text2,Text3=obj.Text3)
                Tile((obj.x,obj.y),obj.image,(self.SeaFoam_IslandFB4Camera))
                self.SeaFoam_IslandFB4Readables.append(Read)
                self.SeaFoam_IslandFB4Barriers.append(Read.Rect)

    def Load_Cerulean_Cave(self):
        for layer in self.Cerulean_Cave.layers:
            if hasattr(layer,"data"):
                for x,y,surf in layer.tiles():
                    if layer.name == "Floor 1":Tile((x*32,y*32),surf,(self.Cerulean_CaveF1Camera))
                    elif layer.name == "Basement Floor 1":Tile((x*32,y*32),surf,(self.Cerulean_CaveBFCamera))
                    else:Tile((x*32,y*32),surf,(self.Cerulean_CaveF2Camera))

        for obj in self.Cerulean_Cave.objects:
            if obj.name == "O_CCaveSpawn": self.O_CCaveSpawn = (obj.x,obj.y)
            elif obj.name == "CCave_ODoor": self.CCave_ODoor = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "Border":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Cerulean_CaveF1Barriers.append(Rect)
            elif obj.name == "Wild Rocks":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Cerulean_CaveF1Wilds.append(Rock)
            elif obj.name == "Ball":
                ball = Pickups((obj.x,obj.y),obj.image,self.Cerulean_CaveF1Camera,obj.Item)
                self.Cerulean_CaveF1Pickups.append(ball)
            elif obj.name == "Hidden":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.Cerulean_CaveF1HiddenItems.append(H)
            elif obj.name == "Seapoint":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Cerulean_CaveF1FishingPoint.append(Rect)
                self.Cerulean_CaveF1Barriers.append(Rect)
            elif obj.name == "CCaveA2_A1Spawn": self.CCaveA2_A1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveA1_A2Door": self.CCaveA1_A2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveB2_B1Spawn": self.CCaveB2_B1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveB1_B2Door": self.CCaveB1_B2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveC2_C1Spawn": self.CCaveC2_C1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveC1_C2Door": self.CCaveC1_C2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveD2_D1Spawn": self.CCaveD2_D1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveD1_D2Door": self.CCaveD1_D2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveE2_E1Spawn": self.CCaveE2_E1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveE1_E2Door": self.CCaveE1_E2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveF2_F1Spawn": self.CCaveF2_F1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveF1_F2Door": self.CCaveF1_F2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveG2_G1Spawn": self.CCaveG2_G1Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveG1_G2Door": self.CCaveG1_G2Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            #Basement Floor
            elif obj.name == "Mewtwo":
                self.Mewtwo = Tile((obj.x,obj.y),obj.image,(self.Cerulean_CaveBFCamera))
                self.Cerulean_CaveBFBarriers.append(self.Mewtwo.rect)
            elif obj.name == "Border2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Cerulean_CaveBFBarriers.append(Rect)
            elif obj.name == "Wild Rocks2":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Cerulean_CaveBFWilds.append(Rock)
            elif obj.name == "Ball2":
                ball = Pickups((obj.x,obj.y),obj.image,self.Cerulean_CaveBFCamera,obj.Item)
                self.Cerulean_CaveBFPickups.append(ball)
            elif obj.name == "Hidden2":
                H = HiddenItems(obj.x,obj.y,obj.width,obj.height,obj.Item)
                self.Cerulean_CaveBFHiddenItems.append(H)
            elif obj.name == "Seapoint2":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Cerulean_CaveBFFishingPoint.append(Rect)
                self.Cerulean_CaveBFBarriers.append(Rect)
            elif obj.name == "CCaveG1_G2Spawn": self.CCaveG1_G2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveG2_G1Door": self.CCaveG2_G1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
        #Floor 2
            elif obj.name == "Border3":
                Rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                self.Cerulean_CaveF2Barriers.append(Rect)
            elif obj.name == "Wild Rocks3":
                Rock = WildPokemonTiles(obj.x,obj.y,obj.width,obj.height,obj.GrassType,obj.LowChance,obj.HighChance)
                self.Cerulean_CaveF2Wilds.append(Rock)
            elif obj.name == "Ball3":
                ball = Pickups((obj.x,obj.y),obj.image,self.Cerulean_CaveF2Camera,obj.Item)
                self.Cerulean_CaveF2Pickups.append(ball)
            elif obj.name == "CCaveA1_A2Spawn": self.CCaveA1_A2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveA2_A1Door": self.CCaveA2_A1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveB1_B2Spawn": self.CCaveB1_B2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveB2_B1Door": self.CCaveB2_B1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveC1_C2Spawn": self.CCaveC1_C2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveC2_C1Door": self.CCaveC2_C1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveD1_D2Spawn": self.CCaveD1_D2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveD2_D1Door": self.CCaveD2_D1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveE1_E2Spawn": self.CCaveE1_E2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveE2_E1Door": self.CCaveE2_E1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)
            elif obj.name == "CCaveF1_F2Spawn": self.CCaveF1_F2Spawn = (obj.x,obj.y)
            elif obj.name == "CCaveF2_F1Door": self.CCaveF2_F1Door = Transportion(obj.x,obj.y,obj.width,obj.height,obj.Destination)

