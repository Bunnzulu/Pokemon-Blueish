import pygame,random
from math import sqrt, floor
pygame.init()
Pokes_img = {"Charmander":("Pokemon_imgs\Charmander_Back.png","Pokemon_imgs\Charmander_Front.png"),"Bulbasaur":("Pokemon_imgs\Bulbasaur_Back.png","Pokemon_imgs\Bulbasaur_Front.png"),"Squirtle":("Pokemon_imgs\Squirtle_Back.png","Pokemon_imgs\Squirtle_Front.png"),"Pidgey":("Pokemon_imgs\Pidgey_Back.png","Pokemon_imgs\Pidgey_Front.png"),"Rattata":("Pokemon_imgs\Rattata_Back.png","Pokemon_imgs\Rattata_Front.png"),"Spearow":("Pokemon_imgs\Spearow_Back.png","Pokemon_imgs\Spearow_Front.png"),"NidoranF":(r"Pokemon_imgs\NidoranF_Back.png",r"Pokemon_imgs\NidoranF_Front.png"),"NidoranM":(r"Pokemon_imgs\NidoranM_Back.png",r"Pokemon_imgs\NidoranM_Front.png"),"Caterpie":("Pokemon_imgs\Caterpie_Back.png","Pokemon_imgs\Caterpie_Front.png"),"Metapod":("Pokemon_imgs\Metapod_Back.png","Pokemon_imgs\Metapod_Front.png"),"Butterfree":("Pokemon_imgs\Butterfree_Back.png","Pokemon_imgs\Butterfree_Front.png"),"Weedle":("Pokemon_imgs\Weedle_Back.png","Pokemon_imgs\Weedle_Front.png"),"Kakuna":("Pokemon_imgs\Kakuna_Back.png","Pokemon_imgs\Kakuna_Front.png"),"Beedrill":("Pokemon_imgs\Beedrill_Back.png","Pokemon_imgs\Beedrill_Front.png"),"Pikachu":("Pokemon_imgs\Pikachu_Back.png","Pokemon_imgs\Pikachu_Front.png"),
"Diglett": ("Pokemon_imgs\Diglett_Back.png","Pokemon_imgs\Diglett_Front.png"),"Sandshrew":("Pokemon_imgs\Sandshrew_Back.png","Pokemon_imgs\Sandshrew_Front.png"),"Geodude":("Pokemon_imgs\Geodude_Back.png","Pokemon_imgs\Geodude_Front.png"),"Onix":("Pokemon_imgs\Onix_Back.png","Pokemon_imgs\Onix_Front.png"),"Ekans":(r"Pokemon_imgs\Ekans_Back.png",r"Pokemon_imgs\Ekans_Front.png"),"Jigglypuff":("Pokemon_imgs\Jigglypuff_Back.png","Pokemon_imgs\Jigglypuff_Front.png"),"Zubat":("Pokemon_imgs\Zubat_Back.png","Pokemon_imgs\Zubat_Front.png"),"Paras":("Pokemon_imgs\Paras_Back.png","Pokemon_imgs\Paras_Front.png"),"Clefairy":("Pokemon_imgs\Clefairy_Back.png","Pokemon_imgs\Clefairy_Front.png"),"Magnemite":("Pokemon_imgs\Magnemite_Back.png","Pokemon_imgs\Magnemite_Front.png"),"Voltorb":("Pokemon_imgs\Voltorb_Back.png","Pokemon_imgs\Voltorb_Front.png"),"Oddish":("Pokemon_imgs\Oddish_Back.png","Pokemon_imgs\Oddish_Front.png"),"Bellsprout":("Pokemon_imgs\Bellsprout_Back.png","Pokemon_imgs\Bellsprout_Front.png"),"Ivysaur":("Pokemon_imgs\Ivysaur_Back.png","Pokemon_imgs\Ivysaur_Front.png"),"Wartortle":("Pokemon_imgs\Wartortle_Back.png","Pokemon_imgs\Wartortle_Front.png"),"Charmeleon":("Pokemon_imgs\Charmeleon_Back.png","Pokemon_imgs\Charmeleon_Front.png"),
"Nidorino":(r"Pokemon_imgs\Nidorino_Back.png",r"Pokemon_imgs\Nidorino_Front.png"),"Nidorina":(r"Pokemon_imgs\Nidorina_Back.png",r"Pokemon_imgs\Nidorina_Front.png"),"Koffing":("Pokemon_imgs\Koffing_Back.png","Pokemon_imgs\Koffing_Front.png"),"Raticate":("Pokemon_imgs\Raticate_Back.png","Pokemon_imgs\Raticate_Front.png"),"Grimer":("Pokemon_imgs\Grimer_Back.png","Pokemon_imgs\Grimer_Front.png"),"Pidgeotto":("Pokemon_imgs\Pidgeotto_Back.png","Pokemon_imgs\Pidgeotto_Front.png"),"Abra":("Pokemon_imgs\Abra_Back.png","Pokemon_imgs\Abra_Front.png"),"Horsea":("Pokemon_imgs\Horsea_Back.png","Pokemon_imgs\Horsea_Front.png"),"Goldeen":("Pokemon_imgs\Goldeen_Back.png","Pokemon_imgs\Goldeen_Front.png"),"Shellder":("Pokemon_imgs\Shellder_Back.png","Pokemon_imgs\Shellder_Front.png"),"Staryu":("Pokemon_imgs\Staryu_Back.png","Pokemon_imgs\Staryu_Front.png"),"Starmie":("Pokemon_imgs\Starmie_Back.png","Pokemon_imgs\Starmie_Front.png"),"Mankey":("Pokemon_imgs\Mankey_Back.png","Pokemon_imgs\Mankey_Front.png"),"Machop":("Pokemon_imgs\Machop_Back.png","Pokemon_imgs\Machop_Front.png"),"Machop":("Pokemon_imgs\Machop_Back.png","Pokemon_imgs\Machop_Front.png"),"Slowpoke":("Pokemon_imgs\Slowpoke_Back.png","Pokemon_imgs\Slowpoke_Front.png"),"Drowzee":("Pokemon_imgs\Drowzee_Back.png","Pokemon_imgs\Drowzee_Front.png"),
"Meowth":("Pokemon_imgs\Meowth_Back.png","Pokemon_imgs\Meowth_Front.png"),"Magikarp":("Pokemon_imgs\Magikarp_Back.png","Pokemon_imgs\Magikarp_Front.png"),"Farfetch'd":("Pokemon_imgs\Farfetch'd_Back.png","Pokemon_imgs\Farfetch'd_Front.png"),"Growlithe":("Pokemon_imgs\Growlithe_Back.png","Pokemon_imgs\Growlithe_Front.png"),"Tentacool":("Pokemon_imgs\Tentacool_Back.png","Pokemon_imgs\Tentacool_Front.png"),"Ponyta":("Pokemon_imgs\Ponyta_Back.png","Pokemon_imgs\Ponyta_Front.png"),"Kadabra":("Pokemon_imgs\Kadabra_Back.png","Pokemon_imgs\Kadabra_Front.png"),"Raichu":("Pokemon_imgs\Raichu_Back.png","Pokemon_imgs\Raichu_Front.png"),"Dugtrio":("Pokemon_imgs\Dugtrio_Back.png","Pokemon_imgs\Dugtrio_Front.png"),"Poliwag":("Pokemon_imgs\Poliwag_Back.png","Pokemon_imgs\Poliwag_Front.png"),"Vulpix":("Pokemon_imgs\Vulpix_Back.png","Pokemon_imgs\Vulpix_Front.png"),"Magneton":("Pokemon_imgs\Magneton_Back.png","Pokemon_imgs\Magneton_Front.png"),"Venonat":("Pokemon_imgs\Venonat_Back.png","Pokemon_imgs\Venonat_Front.png"),"Mr. Mime":("Pokemon_imgs\Mr.Mime_Back.png","Pokemon_imgs\Mr.Mime_Front.png"),"Poliwhirl":("Pokemon_imgs\Poliwhirl_Back.png","Pokemon_imgs\Poliwhirl_Front.png"),"Jynx":("Pokemon_imgs\Jynx_Back.png","Pokemon_imgs\Jynx_Front.png"),"Cubone":("Pokemon_imgs\Cubone_Back.png","Pokemon_imgs\Cubone_Front.png"),
"Graveler":("Pokemon_imgs\Graveler_Back.png","Pokemon_imgs\Graveler_Front.png"),"Fearow":("Pokemon_imgs\Fearow_Back.png","Pokemon_imgs\Fearow_Front.png"),"Arbok":("Pokemon_imgs\Arbok_Back.png","Pokemon_imgs\Arbok_Front.png"),"Sandslash":("Pokemon_imgs\Sandslash_Back.png","Pokemon_imgs\Sandslash_Front.png"),"Golbat":("Pokemon_imgs\Golbat_Back.png","Pokemon_imgs\Golbat_Front.png"),"Weepinbell":("Pokemon_imgs\Weepinbell_Back.png","Pokemon_imgs\Weepinbell_Front.png"),"Gloom":("Pokemon_imgs\Gloom_Back.png","Pokemon_imgs\Gloom_Front.png"),"Parasect":("Pokemon_imgs\Parasect_Back.png","Pokemon_imgs\Parasect_Front.png"),"Hypno":("Pokemon_imgs\Hypno_Back.png","Pokemon_imgs\Hypno_Front.png"),"Muk":("Pokemon_imgs\Muk_Back.png","Pokemon_imgs\Muk_Front.png"),"Pinsir":("Pokemon_imgs\Pinsir_Back.png","Pokemon_imgs\Pinsir_Front.png"),"Dratini":("Pokemon_imgs\Dratini_Back.png","Pokemon_imgs\Dratini_Front.png"),"Porygon":("Pokemon_imgs\Porygon_Back.png","Pokemon_imgs\Porygon_Front.png"),"Eevee":(r"Pokemon_imgs\Eevee_Back.png",r"Pokemon_imgs\Eevee_Front.png"),"Vaporeon":("Pokemon_imgs\Vaporeon_Back.png","Pokemon_imgs\Vaporeon_Front.png"),"Jolteon":("Pokemon_imgs\Jolteon_Back.png","Pokemon_imgs\Jolteon_Front.png"),"Flareon":("Pokemon_imgs\Flareon_Back.png","Pokemon_imgs\Flareon_Front.png"),"Gyarados":("Pokemon_imgs\Gyarados_Back.png","Pokemon_imgs\Gyarados_Front.png"),
"Vileplume":("Pokemon_imgs\Vileplume_Back.png","Pokemon_imgs\Vileplume_Front.png"),"Exeggcute":(r"Pokemon_imgs\Exeggcute_Back.png",r"Pokemon_imgs\Exeggcute_Front.png"),"Tangela":("Pokemon_imgs\Tangela_Back.png","Pokemon_imgs\Tangela_Front.png"),"Victreebel":("Pokemon_imgs\Victreebel_Back.png","Pokemon_imgs\Victreebel_Front.png"),"Nidoking":(r"Pokemon_imgs\Nidoking_Back.png",r"Pokemon_imgs\Nidoking_Front.png"),"Nidoqueen":(r"Pokemon_imgs\Nidoqueen_Back.png",r"Pokemon_imgs\Nidoqueen_Front.png"),"Clefable":("Pokemon_imgs\Clefable_Back.png","Pokemon_imgs\Clefable_Front.png"),"Wigglytuff":("Pokemon_imgs\Wigglytuff_Back.png","Pokemon_imgs\Wigglytuff_Front.png"),"Ninetales":(r"Pokemon_imgs\Ninetales_Back.png",r"Pokemon_imgs\Ninetales_Front.png"),"Arcanine":(r"Pokemon_imgs\Arcanine_Back.png",r"Pokemon_imgs\Arcanine_Front.png"),"Poliwrath":(r"Pokemon_imgs\Poliwrath_Back.png",r"Pokemon_imgs\Poliwrath_Front.png"),"Cloyster":(r"Pokemon_imgs\Cloyster_Back.png",r"Pokemon_imgs\Cloyster_Front.png"),"Exeggutor":(r"Pokemon_imgs\Exeggutor_Back.png",r"Pokemon_imgs\Exeggutor_Front.png"),"Kangaskhan":("Pokemon_imgs\Kangaskhan_Back.png","Pokemon_imgs\Kangaskhan_Front.png"),"Rhyhorn":("Pokemon_imgs\Rhyhorn_Back.png","Pokemon_imgs\Rhyhorn_Front.png"),"Gastly":("Pokemon_imgs\Gastly_Back.png","Pokemon_imgs\Gastly_Front.png"),"Haunter":("Pokemon_imgs\Haunter_Back.png","Pokemon_imgs\Haunter_Front.png"),
"Dodrio":("Pokemon_imgs\Dodrio_Back.png","Pokemon_imgs\Dodrio_Front.png"),"Weezing":("Pokemon_imgs\Weezing_Back.png","Pokemon_imgs\Weezing_Front.png"),"Doduo":("Pokemon_imgs\Doduo_Back.png","Pokemon_imgs\Doduo_Front.png"),"Marowak":("Pokemon_imgs\Marowak_Back.png","Pokemon_imgs\Marowak_Front.png"),"Machoke":("Pokemon_imgs\Machoke_Back.png","Pokemon_imgs\Machoke_Front.png"),"Primeape":("Pokemon_imgs\Primeape_Back.png","Pokemon_imgs\Primeape_Front.png"),"Snorlax":("Pokemon_imgs\Snorlax_Back.png","Pokemon_imgs\Snorlax_Front.png"),"Lickitung":("Pokemon_imgs\Lickitung_Back.png","Pokemon_imgs\Lickitung_Front.png"),"Chansey":("Pokemon_imgs\Chansey_Back.png","Pokemon_imgs\Chansey_Front.png"),"Hitmonlee":("Pokemon_imgs\Hitmonlee_Back.png","Pokemon_imgs\Hitmonlee_Front.png"),"Tauros":("Pokemon_imgs\Tauros_Back.png","Pokemon_imgs\Tauros_Front.png"),"Venomoth":("Pokemon_imgs\Venomoth_Back.png","Pokemon_imgs\Venomoth_Front.png"),"Venusaur":("Pokemon_imgs\Venusaur_Back.png","Pokemon_imgs\Venusaur_Front.png"),"Blastoise":("Pokemon_imgs\Blastoise_Back.png","Pokemon_imgs\Blastoise_Front.png"),"Charizard":("Pokemon_imgs\Charizard_Back.png","Pokemon_imgs\Charizard_Front.png"),"Golem":("Pokemon_imgs\Golem_Back.png","Pokemon_imgs\Golem_Front.png"),"Pidgeot":("Pokemon_imgs\Pidgeot_Back.png","Pokemon_imgs\Pidgeot_Front.png"),"Electrode":("Pokemon_imgs\Electrode_Back.png","Pokemon_imgs\Electrode_Front.png"),
"Seadra":("Pokemon_imgs\Seadra_Back.png","Pokemon_imgs\Seadra_Front.png"),"Seaking":("Pokemon_imgs\Seaking_Back.png","Pokemon_imgs\Seaking_Front.png"),"Alakazam":("Pokemon_imgs\Alakazam_Back.png","Pokemon_imgs\Alakazam_Front.png"),"Tentacruel":("Pokemon_imgs\Tentacruel_Back.png","Pokemon_imgs\Tentacruel_Front.png"),"Persian":("Pokemon_imgs\Persian_Back.png","Pokemon_imgs\Persian_Front.png"),"Machamp":("Pokemon_imgs\Machamp_Back.png","Pokemon_imgs\Machamp_Front.png"),"Dragonair":("Pokemon_imgs\Dragonair_Back.png","Pokemon_imgs\Dragonair_Front.png"),"Gengar":("Pokemon_imgs\Gengar_Back.png","Pokemon_imgs\Gengar_Front.png"),"Hitmonchan":("Pokemon_imgs\Hitmonchan_Back.png","Pokemon_imgs\Hitmonchan_Front.png"),"Lapras":("Pokemon_imgs\Lapras_Back.png","Pokemon_imgs\Lapras_Front.png"),"Ditto":("Pokemon_imgs\Ditto_Back.png","Pokemon_imgs\Ditto_Front.png"),"Krabby":("Pokemon_imgs\Krabby_Back.png","Pokemon_imgs\Krabby_Front.png"),"Kingler":("Pokemon_imgs\Kingler_Back.png","Pokemon_imgs\Kingler_Front.png"),"Slowbro":("Pokemon_imgs\Slowbro_Back.png","Pokemon_imgs\Slowbro_Front.png"),"Psyduck":("Pokemon_imgs\Psyduck_Back.png","Pokemon_imgs\Psyduck_Front.png"),"Golduck":("Pokemon_imgs\Golduck_Back.png","Pokemon_imgs\Golduck_Front.png"),"Seel":("Pokemon_imgs\Seel_Back.png","Pokemon_imgs\Seel_Front.png"),"Dewgong":("Pokemon_imgs\Dewgong_Back.png","Pokemon_imgs\Dewgong_Front.png"),
"Omanyte":("Pokemon_imgs\Omanyte_Back.png","Pokemon_imgs\Omanyte_Front.png"),"Kabuto":("Pokemon_imgs\Kabuto_Back.png","Pokemon_imgs\Kabuto_Front.png"),"Aerodactyl":("Pokemon_imgs\Aerodactyl_Back.png","Pokemon_imgs\Aerodactyl_Front.png"),"Rapidash":("Pokemon_imgs\Rapidash_Back.png","Pokemon_imgs\Rapidash_Front.png"),"Magmar":("Pokemon_imgs\Magmar_Back.png","Pokemon_imgs\Magmar_Front.png"),"Electabuzz":("Pokemon_imgs\Electabuzz_Back.png","Pokemon_imgs\Electabuzz_Front.png"),"Rhydon":("Pokemon_imgs\Rhydon_Back.png","Pokemon_imgs\Rhydon_Front.png"),"Omastar":("Pokemon_imgs\Omastar_Back.png","Pokemon_imgs\Omastar_Front.png"),"Kabutops":("Pokemon_imgs\Kabutops_Back.png","Pokemon_imgs\Kabutops_Front.png"),"Dragonite":("Pokemon_imgs\Dragonite_Back.png","Pokemon_imgs\Dragonite_Front.png"),"Moltres":("Pokemon_imgs\Moltres_Back.png","Pokemon_imgs\Moltres_Front.png"),"Zapdos":("Pokemon_imgs\Zapdos_Back.png","Pokemon_imgs\Zapdos_Front.png"),"Articuno":("Pokemon_imgs\Articuno_Back.png","Pokemon_imgs\Articuno_Front.png"),"Scyther":("Pokemon_imgs\Scyther_Back.png","Pokemon_imgs\Scyther_Front.png"),"Mewtwo":("Pokemon_imgs\Mewtwo_Back.png","Pokemon_imgs\Mewtwo_Front.png"),"Mew":("Pokemon_imgs\Mew_Back.png","Pokemon_imgs\Mew_Front.png")}
Pokemon_BaseStats = {"Bulbasaur":(45,49,49,45,65),"Ivysaur":(60,62,63,60,80),"Charmander":(39,52,43,65,50),"Charmeleon":(58,64,58,80,65),"Squirtle":(44,48,65,43,50),"Wartortle":(59,63,80,58,65),"Pidgey":(40,45,40,56,35),"Rattata":(30,56,35,72,25),"Spearow":(40,60,30,70,31),"NidoranF":(55,47,52,41,40),"NidoranM":(45,57,40,50,40),"Caterpie":(45,30,35,45,20),"Metapod":(50,20,55,30,25),"Butterfree":(60,45,50,70,80),"Weedle":(40,35,30,50,20),"Kakuna":(45,25,50,35,25),"Beedrill":(65,80,40,75,45),"Pikachu":(35,55,30,90,50),"Diglett":(10,55,25,95,45),"Sandshrew":(50,75,85,40,30),"Geodude":(40,80,100,20,30),"Onix":(35,45,160,70,30),"Ekans":(35,60,44,55,40),"Jigglypuff":(115,45,20,20,25),"Zubat":(40,45,35,55,40),"Paras":(35,70,55,25,55),"Clefairy":(70,45,48,35,60),"Magnemite":(25,35,70,45,95),"Voltorb":(40,30,50,100,55),"Oddish":(45,50,55,30,75),"Bellsprout":(50,75,35,40,70),"Nidorino":(61,72,57,65,55),"Nidorina":(70,62,67,56,55),"Koffing":(40,65,95,35,60),"Raticate":(55,81,60,97,50),"Grimer":(80,80,50,25,40),"Pidgeotto":(63,60,55,71,50),"Abra":(25,20,15,90,105),"Horsea":(30,40,70,60,70),"Goldeen":(45,67,60,63,50),"Shellder":(30,65,100,40,45),"Staryu":(30,45,55,85,70),"Starmie":(60,75,85,115,100),"Mankey":(40,80,35,70,35),"Machop":(70,80,50,35,35),"Slowpoke":(90,65,65,15,40),"Drowzee":(60,48,45,42,90),
                     "Meowth":(40,45,35,90,40),"Magikarp":(20,10,55,80,20),"Farfetch'd":(52,65,55,60,58),"Growlithe":(55,70,45,60,50),"Tentacool":(40,40,35,70,100),"Ponyta":(50,85,55,90,65),"Kadabra":(40,35,30,105,120),"Raichu":(60,90,55,100,90),"Dugtrio":(35,80,50,120,70),"Poliwag":(40,50,40,90,40),"Vulpix":(38,41,40,65,65),"Magneton":(50,60,95,70,120),"Venonat":(60,55,50,45,40),"Mr. Mime":(40,45,65,90,100),"Poliwhirl":(65,65,65,90,50),"Jynx":(65,50,35,95,95),"Cubone":(50,50,95,35,40),"Graveler":(55,95,115,35,45),"Fearow":(65,90,65,100,61),"Arbok":(60,85,69,80,65),"Sandslash":(75,100,110,65,55),"Golbat":(75,80,70,90,75),"Weepinbell":(65,90,50,55,85),"Gloom":(60,65,70,40,85),"Parasect":(60,95,80,30,80),"Hypno":(85,73,70,67,115),"Muk":(105,105,75,50,65),"Pinsir":(65,125,100,85,55),"Dratini":(41,64,45,50,50),"Porygon":(65,60,70,40,75),"Eevee":(55,55,50,55,65),"Vaporeon":(130,65,60,65,110),"Jolteon":(65,65,60,130,110),"Flareon":(65,130,60,65,110),"Gyarados":(95,125,79,81,100),"Vileplume":(75,80,85,50,100),"Exeggcute":(60,40,80,40,60),"Tangela":(65,55,115,60,100),"Victreebel":(80,105,65,70,100),"Nidoking":(81,92,77,85,75),"Nidoqueen":(90,82,87,76,75),"Clefable":(95,70,73,60,85),"Wigglytuff":(140,70,45,45,50),"Ninetales":(73,76,75,100,100),"Arcanine":(90,110,80,95,80),"Poliwrath":(90,85,95,70,70),
                     "Cloyster":(50,95,180,70,85),"Exeggutor":(95,95,85,55,125),"Kangaskhan":(105,95,80,90,40),"Rhyhorn":(80,85,95,25,30),"Gastly":(30,35,30,80,100),"Haunter":(45,50,45,95,115),"Dodrio":(60,110,70,100,60),"Weezing":(65,90,120,60,85),"Doduo":(35,85,45,75,35),"Marowak":(60,80,110,45,50),"Machoke":(80,100,70,45,50),"Primeape":(65,105,60,95,60),"Snorlax":(160,110,65,30,65),"Lickitung":(90,55,75,30,60),"Chansey":(250,5,5,50,105),"Hitmonlee":(50,120,53,87,35),"Tauros":(75,100,95,110,70),"Venomoth":(70,65,60,90,90),"Venusaur":(80,82,83,80,100),"Blastoise":(79,83,100,78,85),"Charizard":(78,84,78,100,85),"Golem":(80,110,130,45,55),"Pidgeot":(83,80,75,91,70),"Electrode":(60,50,70,140,80),"Seadra":(55,65,95,85,95),"Seaking":(80,92,65,68,80),"Alakazam":(55,50,45,120,135),"Tentacruel":(80,70,65,100,120),"Persian":(65,70,60,115,65),"Machamp":(90,130,80,55,65),"Dragonair":(61,84,65,70,70),"Gengar":(60,65,60,110,130),"Hitmonchan":(50,105,79,76,35),"Lapras":(130,85,80,60,95),"Ditto":(48,48,48,48,48),"Krabby":(30,105,90,50,25),"Kingler":(55,130,115,75,50),"Slowbro":(95,75,110,30,80),"Psyduck":(50,52,48,55,50),"Golduck":(80,82,78,85,80),"Seel":(65,45,55,45,70),"Dewgong":(90,70,80,70,95),"Omanyte":(35,40,100,35,90),"Kabuto":(30,80,90,55,45),"Aerodactyl":(80,105,65,130,60),"Rapidash":(65,100,70,105,80),
                     "Magmar":(65,95,57,93,85),"Electabuzz":(65,83,57,105,85),"Rhydon":(105,130,120,40,45),"Omastar":(70,60,125,55,115),"Kabutops":(60,115,105,80,70),"Dragonite":(91,134,95,80,100),"Moltres":(90,100,90,90,125),"Zapdos":(90,90,85,100,125),"Articuno":(90,85,100,85,125),"Scyther":(70,110,80,105,55),"Mewtwo":(106,110,90,130,154),"Mew":(100,100,100,100,100)}
Pokemon_Types = {"Bulbasaur":["Grass","Poison"],"Ivysaur":["Grass","Poison"],"Charmander":["Fire",""],"Charmeleon":["Fire",""],"Squirtle":["Water",""],"Wartortle":["Water",""],"Pidgey":["Normal","Flying"],"Rattata":["Normal",""],"Spearow":["Normal","Flying"],"NidoranF":["Poison",""],"NidoranM":["Poison",""],"Caterpie":["Bug",""],"Metapod":["Bug",""],"Butterfree":["Bug","Flying"],"Weedle":["Bug","Poison"],"Kakuna":["Bug","Poison"],"Beedrill":["Bug","Poison"],"Pikachu":["Electric",""],"Diglett":["Ground",''],"Sandshrew":["Ground",''],"Geodude":["Rock","Ground"],"Onix":["Rock","Ground"],"Ekans":["Poison",""],"Jigglypuff":["Normal",""],"Zubat":["Poison","Flying"],"Paras":["Bug","Grass"],"Clefairy":["Noraml",''],"Magnemite":["Electric",""],"Voltorb":["Electric",""],"Oddish":["Grass","Poison"],"Bellsprout":["Grass","Poison"],"Nidorino":["Poison",""],"Nidorina":["Poison",""],"Koffing":["Poison",""],"Raticate":["Normal",""],"Grimer":["Poison",""],"Pidgeotto":["Normal","Flying"],"Abra":["Psychic",""],"Horsea":["Water",""],"Goldeen":["Water",""],"Shellder":["Water",""],"Staryu":["Water",""],"Starmie":["Water","Psychic"],"Mankey":["Fighting",""],"Machop":["Fighting",""],"Slowpoke":["Water","Psychic"],"Drowzee":["Psychic",""],"Meowth":["Normal",""],"Magikarp":["Water",""],"Farfetch'd":["Normal","Flying"],
                 "Growlithe":["Fire",""],"Tentacool":["Water","Poison"],"Ponyta":["Fire",""],"Kadabra":["Psychic",""],"Raichu":["Electric",""],"Dugtrio":["Ground",""],"Poliwag":["Water",""],"Vulpix":["Fire",""],"Magneton":["Electric",""],"Venonat":["Bug","Poison"],"Mr. Mime":["Psychic",""],"Poliwhirl":["Water",""],"Jynx":["Ice","Psychic"],"Cubone":["Ground",""],"Graveler":["Rock","Ground"],"Fearow":["Normal","Flying"],"Arbok":["Poison",""],"Sandslash":["Ground",""],"Golbat":["Poison","Flying"],"Weepinbell":["Grass","Poison"],"Gloom":["Grass","Poison"],"Parasect":["Bug","Grass"],"Hypno":["Psychic",""],"Muk":["Poison",""],"Pinsir":["Bug",""],"Dratini":["Dragon",""],"Porygon":["Normal",""],"Eevee":["Normal",""],"Vaporeon":["Water",""],"Jolteon":["Electric",""],"Flareon":["Fire",""],"Gyarados":["Water","Flying"],"Vileplume":["Grass","Poison"],"Exeggcute":["Grass","Psychic"],"Tangela":["Grass",""],"Victreebel":["Grass","Poison"],"Nidoking":["Poison","Ground"],"Nidoqueen":["Poison","Ground"],"Clefable":["Normal",""],"Wigglytuff":["Normal",""],"Ninetales":["Fire",""],"Arcanine":["Fire",""],"Poliwrath":["Water","Fighting"],"Cloyster":["Water","Ice"],"Exeggutor":["Grass","Psychic"],"Kangaskhan":["Normal",""],"Rhyhorn":["Ground","Rock"],"Gastly":["Ghost","Poison"],"Haunter":["Ghost",""],"Dodrio":["Normal","Flying"],
                 "Doduo":["Normal","Flying"],"Weezing":["Poison",""],"Marowak":["Ground",""],"Machoke":["Fighting",""],"Primeape":["Fighting",""],"Snorlax":["Normal",""],"Lickitung":["Normal",""],"Chansey":["Normal",""],"Hitmonlee":["Fighting",""],"Tauros":["Normal",""],"Venomoth":["Bug","Poison"],"Venusaur":["Grass","Poison"],"Blastoise":["Water",""],"Charizard":["Fire","Flying"],"Golem":["Rock","Ground"],"Pidgeot":["Normal","Flying"],"Electrode":["Electric",""],"Seadra":["Water",""],"Seaking":["Water",""],"Alakazam":["Psychic",""],"Tentacruel":["Water","Poison"],"Persian":["Normal",""],"Machamp":["Fighting",""],"Dragonair":["Dragon",""],"Gengar":["Ghost","Poison"],"Hitmonchan":["Fighting",""],"Lapras":["Water","Ice"],"Ditto":["Normal",""],"Krabby":["Water",""],"Kingler":["Water",""],"Slowbro":["Water","Psychic"],"Psyduck":["Water",""],"Golduck":["Water",""],"Seel":["Water",""],"Dewgong":["Water","Ice"],"Omanyte":["Rock","Water"],"Kabuto":["Rock","Water"],"Aerodactyl":["Rock","Flying"],"Rapidash":["Fire",""],"Magmar":["Fire",""],"Electabuzz":["Electric",""],"Rhydon":["Ground","Rock"],"Omastar":["Water","Rock"],"Kabutops":["Water","Rock"],"Dragonite":["Dragon","Flying"],"Moltres":["Fire","Flying"],"Zapdos":["Electric","Flying"],"Articuno":["Ice","Flying"],"Scyther":["Bug","Flying"],"Mewtwo":["Psychic",""],"Mew":["Psychic",""]}
Pokemon_EXPGroups = {"Bulbasaur":"Medium Slow","Ivysaur":"Medium Slow","Charmander":"Medium Slow","Charmeleon":"Medium Slow","Squirtle":"Medium Slow","Wartortle":"Medium Slow","Pidgey":"Medium Slow","Rattata":"Medium Fast","Spearow":"Medium Fast","NidoranF":"Medium Slow","NidoranM":"Medium Slow","Caterpie":"Medium Fast","Metapod":"Medium Fast","Butterfree":"Medium Fast","Weedle":"Medium Fast","Kakuna":"Medium Fast","Beedrill":"Medium Fast","Pikachu":"Medium Fast","Diglett":"Medium Fast","Sandshrew":"Medium Fast","Geodude":"Medium Slow","Onix":"Medium Fast","Ekans":"Medium Fast","Jigglypuff":"Fast","Zubat":"Medium Fast","Paras":"Medium Fast","Clefairy":"Fast","Magnemite":"Medium Fast","Voltorb":"Medium Fast","Oddish":"Medium Slow","Bellsprout":"Medium Slow","Nidorino":"Medium Slow","Nidorina":"Medium Slow","Koffing":"Medium Fast","Raticate":"Medium Fast","Grimer":"Medium Fast","Pidgeotto":"Medium Slow","Abra":"Medium Slow","Horsea":"Medium Fast","Goldeen":"Medium Fast","Shellder":"Slow","Staryu":"Slow","Starmie":"Slow","Mankey":"Medium Fast","Machop":"Medium Slow","Slowpoke":"Medium Fast","Drowzee":"Medium Fast","Meowth":"Medium Fast","Magikarp":"Slow","Farfetch'd":"Medium Fast","Growlithe":"Slow","Tentacool":"Slow","Ponyta":"Medium Fast","Kadabra":"Medium Slow","Raichu":"Medium Fast","Dugtrio":"Medium Fast","Poliwag":"Medium Slow","Vulpix":"Medium Fast","Magneton":"Medium Fast","Venonat":"Medium Fast","Mr. Mime":"Medium Fast","Poliwhirl":"Medium Slow","Jynx":"Medium Fast",
                     "Cubone":"Medium Fast","Graveler":"Medium Slow","Fearow":"Medium Fast","Arbok":"Medium Fast","Sandslash":"Medium Fast","Golbat":"Medium Fast","Weepinbell":"Medium Slow","Gloom":"Medium Slow","Parasect":"Medium Fast","Hypno":"Medium Fast","Muk":"Medium Fast","Pinsir":"Slow","Dratini":"Slow","Porygon":"Medium Fast","Eevee":"Medium Fast","Vaporeon":"Medium Fast","Jolteon":"Medium Fast","Flareon":"Medium Fast","Gyarados":"Slow","Vileplume":"Medium Slow","Exeggcute":"Slow","Tangela":"Medium Fast","Victreebel":"Medium Slow","Nidoqueen":"Medium Slow","Nidoking":"Medium Slow","Clefable":"Fast","Wigglytuff":"Fast","Ninetales":"Medium Fast","Arcanine":"Slow","Poliwrath":"Medium Slow","Cloyster":"Slow","Exeggutor":"Slow","Kangaskhan":"Medium Fast","Rhyhorn":"Slow","Gastly":"Medium Slow","Haunter":"Medium Slow","Doduo":"Medium Fast","Dodrio":"Medium Fast","Marowak":"Medium Fast","Machoke":"Medium Slow","Primeape":"Medium Fast","Snorlax":"Slow","Lickitung":"Medium Fast","Chansey":"Fast","Weezing":"Medium Fast","Hitmonlee":"Medium Fast","Tauros":"Slow","Venomoth":"Medium Fast","Venusaur":"Medium Slow","Blastoise":"Medium Slow","Charizard":"Medium Slow","Golem":"Medium Slow","Pidgeot":"Medium Slow","Electrode":"Medium Fast","Seadra":"Medium Fast","Seaking":"Medium Fast","Alakazam":"Medium Slow","Tentacruel":"Slow","Persian":"Medium Fast","Machamp":"Medium Slow","Dragonair":"Slow","Gengar":"Medium Slow","Hitmonchan":"Medium Fast","Lapras":"Slow","Ditto":"Medium Fast",
                     "Krabby":"Medium Fast","Kingler":"Medium Fast","Slowbro":"Medium Fast","Psyduck":"Medium Fast","Golduck":"Medium Fast","Seel":"Medium Fast","Dewgong":"Medium Fast","Omanyte":"Medium Fast","Kabuto":"Medium Fast","Aerodactyl":"Slow","Rapidash":"Medium Fast","Magmar":"Medium Fast","Electabuzz":"Medium Fast","Rhydon":"Slow","Omastar":"Medium Fast","Kabutops":"Medium Fast","Dragonite":"Slow","Moltres":"Slow","Zapdos":"Slow","Articuno":"Slow","Scyther":"Medium Fast","Mewtwo":"Slow","Mew":"Medium Slow"}
Pokemon_Move_PP = {"Tackle":35,"Tail Whip":30,"Growl":40,"Scratch":35,"Gust":35,"Quick Attack":30,"Sand Attack":15,"-":"--","Leech Seed":10,"Bubble":30,"Ember":25,"Peck":35,"Leer":30,"String Shot":40,"Harden":30,"Confusion":25,"Poison Sting":35,"ThunderShock":30,"Thunder Wave":20,"Horn Attack":25,"Fury Attack":20,"Defense Curl":40,"Screech":40,"Bide":10,"Wrap":20,"Pound":35,"Sing":15,"Disable":20,"Leech Life":15,"Supersonic":20,"Poison Powder":35,"Stun Spore":30,"Absorb":20,"Vine Whip":10,"Growth":40,"Water Gun":25,"Hyper Fang":15,"Focus Energy":30,"Rock Throw":15,"Bind":20,"Bite":25,"Smog":20,"Mega Punch":20,"Whirlwind":20,"Teleport":20,"Withdraw":40,"BubbleBeam":20,"Karate Chop":25,"Seismic Toss":20,"Hypnosis":20,"Dig":10,"Sleep Powder":15,"Splash":40,"Roar":20,"Acid":30,"Low Kick":20,"Body Slam":15,"Rest":5,"Cut":30,"SonicBoom":20,"Thunderbolt":15,"Flash":20,"Slash":20,"Selfdestruct":5,"Pay Day":20,"Barrier":20,"Lovely Kiss":10,"DoubleSlap":10,"Bone Club":20,"Headbutt":15,"Rage":20,"Twineedle":20,"Dream Eater":15,"Mirror Move":20,"Confuse Ray":10,"Swift":20,"Minimize":20,"Clamp":10,"Fury Swipes":15,"Swords Dance":30,"Light Screen":30,"Lick":30,"Poison Gas":40,"ViceGrip":30,"Sharpen":30,"Conversion":30,"Psybeam":20,"Agility":30,"Dragon Rage":10,"Hyper Beam":5,"Substitute":10,"Double Team":15,"Reflect":20,"Razor Wind":10,"Horn Drill":5,"Egg Bomb":10,"Mega Kick":5,"Take Down":20,"Submission":20,"Counter":20,"Ice Beam":10,"Rock Slide":10,"Tri Attack":10,"Barrage":20,"Constrict":35,"Thrash":10,"Razor Leaf":25,"Petal Dance":20,"Mega Drain":10,"Double Edge":15,"Comet Punch":15,"Night Shade":15,"Hydro Pump":5,"Amnesia":20,"Stomp":20,"Fly":15,"Sludge":20,"Drill Peck":20,"Surf":15,"Skull Bash":15,"Earthquake":10,"Wing Attack":35,"SmokeScreen":20,"Meditate":40,"Double Kick":30,"Rolling Kick":15,"Psychic":10,"Pin Missile":20,"Slam":20,"Recover":20,"Glare":30,"Toxic":10,"Metronome":10,"Spore":15,"Aurora Beam":20,"Guillotine":5,"Fire Punch":15,"Strength":15,"Mist":30,"Transform":10,"PsyWave":15,"Mimic":10,"Softboiled":10,"SolarBeam":10,"Blizzard":5,"Flamethrower":15,"Fire Blast":5,"Fire Spin":15,"Fissure":5,"Super Fang":10,"Thunder":10,"Haze":30,"Explosion":5,"Acid Armor":40,
                   "Spike Cannon":15,"Dizzy Punch":10,"Bonemerang":10,"Jump Kick":10,"Hi Jump Kick":10,"Waterfall":15,"Ice Punch":15,"Thunder Punch":15,"Crabhammer":10,"Sky Attack":5}
Pokemon_Move_Type = {"Tackle":"Normal","Tail Whip":"Normal","Growl":"Normal","Scratch":"Normal","Gust":"Normal","Sand Attack":"Normal","-":"--","Leech Seed":"Grass","Bubble":"Water","Ember":"Fire","Peck":"Flying","Leer":"Normal","String Shot":"Bug","Harden":"Normal","Confusion":"Psychic","Poison Sting":"Poison","ThunderShock":"Electric","Thunder Wave":"Electric","Quick Attack":"Normal","Horn Attack":"Normal","Fury Attack":"Normal","Defense Curl":"Normal","Screech":"Normal","Bide":"Normal","Wrap":"Normal","Pound":"Normal","Sing":"Normal","Disable":"Normal","Leech Life":"Bug","Supersonic":"Normal","Poison Powder":"Poison","Stun Spore":"Grass","Absorb":"Grass","Vine Whip":"Grass","Growth":"Normal","Water Gun":"Water","Hyper Fang":"Normal","Focus Energy":"Normal","Rock Throw":"Rock","Bind":"Normal","Bite":"Normal","Smog":"Poison","Mega Punch":"Normal","Whirlwind":"Normal","Teleport":"Psychic","Withdraw":"Water","BubbleBeam":"Water","Karate Chop":"Normal","Seismic Toss":"Fighting","Hypnosis":"Psychic","Dig":"Ground","Sleep Powder":"Grass","Splash":"Normal","Roar":"Normal","Acid":"Poison","Low Kick":"Fighting","Body Slam":"Normal","Rest":"Psychic","Cut":"Normal","SonicBoom":"Normal","Thunderbolt":"Electric","Flash":"Normal","Slash":"Normal","Selfdestruct":"Normal","Pay Day":"Normal","Barrier":"Psychic","Lovely Kiss":"Normal","DoubleSlap":"Normal","Bone Club":"Ground","Headbutt":"Normal","Rage":"Normal","Twineedle":"Bug","Dream Eater":"Psychic","Mirror Move":"Normal","Confuse Ray":"Ghost","Swift":"Normal","Minimize":"Normal","Clamp":"Water","Fury Swipes":"Normal","Swords Dance":"Normal","Light Screen":"Psychic","Lick":"Ghost","Poison Gas":"Poison","ViceGrip":"Normal","Sharpen":"Normal","Conversion":"Normal","Psybeam":"Psychic","Agility":"Psychic","Dragon Rage":"Dragon","Hyper Beam":"Normal","Substitute":"Normal","Double Team":"Normal","Reflect":"Psychic","Razor Wind":"Normal","Horn Drill":"Normal","Egg Bomb":"Normal","Mega Kick":"Normal","Take Down":"Normal","Submission":"Fighting","Counter":"Fighting",
                     "Ice Beam":"Ice","Rock Slide":"Rock","Tri Attack":"Normal","Barrage":"Normal","Constrict":"Normal","Thrash":"Normal","Razor Leaf":"Grass","Petal Dance":"Grass","Mega Drain":"Grass","Double Edge":"Normal","Comet Punch":"Normal","Night Shade":"Ghost","Hydro Pump":"Water","Amnesia":"Psychic","Stomp":"Normal","Fly":"Flying","Sludge":"Poison","Drill Peck":"Flying","Surf":"Water","Skull Bash":"Normal","Earthquake":"Ground","Wing Attack":"Flying","SmokeScreen":"Normal","Meditate":"Psychic","Double Kick":"Fighting","Rolling Kick":"Fighting","Psychic":"Psychic","Pin Missile":"Bug","Slam":"Normal","Recover":"Normal","Glare":"Normal","Toxic":"Poison","Metronome":"Normal","Spore":"Grass","Aurora Beam":"Ice","Guillotine":"Normal","Fire Punch":"Fire","Strength":"Normal","Mist":"Ice","Transform":"Normal","PsyWave":"Psychic","Mimic":"Normal","Softboiled":"Normal","SolarBeam":"Grass","Blizzard":"Ice","Flamethrower":"Fire","Fire Blast":"Fire","Fire Spin":"Fire","Fissure":"Ground","Super Fang":"Normal","Thunder":"Eletric","Haze":"Ice","Explosion":"Normal","Acid Armor":"Poison","Spike Cannon":"Normal","Dizzy Punch":"Normal","Bonemerang":"Ground","Jump Kick":"Fighting","Hi Jump Kick":"Fighting","Waterfall":"Water","Ice Punch":"Ice","Thunder Punch":"Electric","Crabhammer":"Water","Sky Attack":"Flying"}
Pokemon_Max_Move_PP = {"Tackle":56,"Tail Whip":48,"Growl":64,"Scratch":56,"Gust":56,"Sand Attack":24,"Leech Seed":16,"Bubble":48,"Ember":40,"Peck":56,"Leer":48,"String Shot":64,"Harden":48,"Confusion":40,"Poison Sting":56,"ThunderShock":48,"Thunder Wave":32,"Quick Attack":48,"Horn Attack":40,"Fury Attack":32,"Defense Curl":64,"Screech":64,"Bide":16,"Wrap":32,"Pound":56,"Sing":24,"Disable":32,"Leech Life":21,"Supersonic":32,"Poison Powder":56,"Stun Spore":48,"Absorb":40,"Vine Whip":30,"Growth":52,"Water Gun":40,"Hyper Fang":24,"Focus Energy":48,"Rock Throw":24,"Bind":32,"Bite":40,"Smog":32,"Mega Punch":32,"Whirlwind":32,"Teleport":32,"Withdraw":64,"BubbleBeam":32,"Karate Chop":40,"Seismic Toss":32,"Hypnosis":32,"Dig":16,"Sleep Powder":24,"Splash":64,"Roar":32,"Acid":48,"Low Kick":32,"Body Slam":24,"Rest":8,"Cut":48,"SonicBoom":32,"Thunderbolt":24,"Flash":32,"Slash":32,"Selfdestruct":8,"Pay Day":32,"Barrier":32,"Lovely Kiss":16,"DoubleSlap":16,"Bone Club":32,"Headbutt":24,"Rage":32,"Twineedle":32,"Dream Eater":24,"Mirror Move":32,"Confuse Ray":16,"Swift":32,"Minimize":32,"Clamp":16,"Fury Swipes":24,"Swords Dance":48,"Light Screen":48,"Lick":48,"Poison Gas":64,"ViceGrip":48,"Sharpen":48,"Conversion":48,"Psybeam":32,"Agility":48,"Dragon Rage":16,"Hyper Beam":8,"Substitute":16,"Double Team":24,"Reflect":32,"Razor Wind":16,"Horn Drill":8,"Egg Bomb":16,"Mega Kick":8,"Take Down":32,"Submission":32,"Counter":32,"Ice Beam":16,"Rock Slide":16,"Tri Attack":16,"Barrage":32,"Constrict":56,"Thrash":16,"Razor Leaf":40,"Petal Dance":32,"Mega Drain":16,"Double Edge":24,"Comet Punch":24,"Night Shade":24,"Hydro Pump":8,"Amnesia":32,"Stomp":32,"Fly":24,"Sludge":32,"Drill Peck":32,"Surf":24,"Skull Bash":24,"Earthquake":16,"Wing Attack":56,"SmokeScreen":32,"Meditate":64,"Double Kick":48,"Rolling Kick":24,"Psychic":16,"Pin Missile":32,"Slam":32,"Recover":32,"Glare":48,"Toxic":16,"Metronome":16,"Spore":24,"Aurora Beam":32,"Guillotine":8,"Fire Punch":24,"Strength":24,"Mist":48,"Transform":16,"PsyWave":24,"Mimic":16,"Softboiled":16,"SolarBeam":16,"Blizzard":8,"Flamethrower":24,"Fire Blast":8,"Fire Spin":24,"Fissure":8,"Super Fang":16,"Thunder":16,"Haze":48,"Explosion":8,"Acid Armor":64,
                       "Spike Cannon":24,"Dizzy Punch":16,"Bonemerang":16,"Jump Kick":16,"Hi Jump Kick":16,"Waterfall":24,"Ice Punch":24,"Thunder Punch":24,"Crabhammer":16,"Sky Attack":8}
Pokemon_EXP = {"Bulbasaur":64,"Charmander":65,"Squirtle":66,"Pidgey":55,"Rattata":57,"Spearow":58,"NidoranF":59,"NidoranM":60,"Caterpie":53,"Metapod":72,"Butterfree":160,"Weedle":52,"Kakuna":71,"Beedrill":159,"Pikachu":82,"Diglett":81,"Sandshrew":93,"Geodude":86,"Onix":108,"Ekans":62,"Jigglypuff":76,"Zubat":54,"Paras":70,"Clefairy":68,"Magnemite":89,"Voltorb":103,"Oddish":78,"Bellsprout":84,"Ivysaur":141,"Wartortle":143,"Charmeleon":142,"Nidorino":118,"Nidorina":117,"Koffing":114,"Raticate":116,"Grimer":90,"Pidgeotto":113,"Abra":73,"Horsea":83,"Goldeen":111,"Shellder":97,"Staryu":106,"Starmie":207,"Mankey":74,"Machop":88,"Slowpoke":99,"Drowzee":102,"Meowth":69,"Magikarp":20,"Farfetch'd":94,"Growlithe":91,"Tentacool":105,"Ponyta":152,"Kadabra":145,"Raichu":122,"Dugtrio":153,"Poliwag":77,"Vulpix":63,"Magneton":161,"Venonat":75,"Mr. Mime":136,"Poliwhirl":131,"Jynx":137,"Cubone":87,"Graveler":134,"Fearow":162,"Arbok":147,"Sandslash":163,"Golbat":171,"Weepinbell":151,"Gloom":132,"Parasect":128,"Hypno":165,"Muk":157,"Pinsir":200,"Dratini":67,"Porygon":130,"Eevee":92,"Vaporeon":196,"Jolteon":197,"Flareon":198,"Gyarados":214,"Vileplume":184,"Exeggcute":98,"Tangela":166,"Victreebel":191,"Nidoking":195,"Nidoqueen":194,"Clefable":129,"Wigglytuff":109,"Ninetales":178,"Arcanine":213,"Poliwrath":185,"Cloyster":203,"Exeggutor":212,"Kangaskhan":175,"Rhyhorn":135,"Gastly":96,"Haunter":126,"Dodrio":158,"Doduo":96,"Marowak":124,"Machoke":146,"Primeape":149,"Snorlax":154,"Lickitung":127,"Chansey":255,"Weezing":173,"Hitmonlee":139,"Tauros":211,"Venomoth":138,"Venusaur":208,"Blastoise":210,"Charizard":209,"Golem":177,"Pidgeot":172,"Electrode":150,"Seadra":155,"Seaking":170,"Alakazam":186,"Tentacruel":205,"Persian":148,"Machamp":198,"Dragonair":144,"Gengar":190,"Hitmonchan":140,"Lapras":219,"Ditto":61,"Krabby":115,"Kingler":206,"Slowbro":164,"Psyduck":80,"Golduck":174,"Seel":100,"Dewgong":176,"Omanyte":120,"Kabuto":119,"Aerodactyl":202,"Rapidash":192,"Magmar":167,"Electabuzz":156,"Rhydon":204,"Omastar":199,"Kabutops":201,"Dragonite":218,"Moltres":217,"Zapdos":216,"Articuno":215,"Scyther":187,"Mewtwo":220,"Mew":64}
Pokemon_Learnsets = {"Bulbasaur":[(1,"Tackle"),(1,"Growl"),(7,"Leech Seed"),(13,"Vine Whip"),(20,"Poison Powder"),(27,"Razor Leaf"),(34,"Growth"),(41,"Sleep Powder"),(48,"SolarBeam")],"Ivysaur":[(22,"Poison Powder"),(30,"Razor Leaf"),(38,"Growth"),(46,"Sleep Powder"),(54,"SolarBeam")],"Squirtle":[(1,"Tackle"),(1,"Tail Whip"),(8,"Bubble"),(15,"Water Gun"),(22,"Bite"),(28,"Withdraw"),(35,"Skull Bash"),(42,"Hydro Pump")],"Wartortle":[(24,"Bite"),(31,"Withdraw"),(39,"Skull Bash"),(47,"Hydro Pump")],"Charmander":[(1,"Scratch"),(1,"Growl"),(9,"Ember"),(15,"Leer"),(22,"Rage"),(30,"Slash"),(38,"Flamethrower"),(46,"Fire Spin")],"Charmeleon":[(24,"Rage"),(33,"Slash"),(42,"Flamethrower"),(56,"Fire Spin")],"Pidgey":[(1,"Gust"),(5,"Sand Attack"),(12,"Quick Attack"),(19,"Whirlwind"),(28,"Wing Attack"),(36,"Agility"),(44,"Mirror Move")],"Rattata":[(1,"Tackle"),(1,"Tail Whip"),(7,"Quick Attack"),(14,"Hyper Fang"),(23,"Focus Energy"),(34,"Super Fang")],"Spearow":[(1,"Peck"),(1,"Growl"),(9,"Leer"),(15,"Fury Attack"),(22,"Mirror Move"),(29,"Drill Peck"),(36,"Agility")],"NidoranF":[(1,"Tackle"),(1,"Growl"),(8,"Scratch"),(14,"Poison Sting"),(21,"Tail Whip"),(29,"Bite"),(36,"Fury Swipes"),(43,"Double Kick")],"NidoranM":[(1,"Tackle"),(1,"Leer"),(8,"Horn Attack"),(14,"Poison Sting"),(21,"Focus Energy"),(29,"Fury Attack"),(36,"Horn Drill"),(43,"Double Kick")],"Caterpie":[(1,"Tackle"),(1,"String Shot")],"Metapod":[(1,"Harden"),(7,"Harden")],"Butterfree":[(10,"Confusion"),(15,"Poison Powder"),(16,"Stun Spore"),(17,"Sleep Powder"),(21,"Supersonic"),(26,"Whirlwind"),(32,"Psybeam")],"Weedle":[(1,"Poison Sting"),(1,"String Shot")],"Kakuna":[(1,"Harden"),(7,"Harden")],"Beedrill":[(12,"Fury Attack"),(16,"Focus Energy"),(20,"Twineedle"),(25,"Rage"),(30,"Pin Missile"),(35,"Agility")],"Pikachu":[(1,"ThunderShock"),(1,"Growl"),(9,"Thunder Wave"),(16,"Quick Attack"),(26,"Swift"),(33,"Agility"),(43,"Thunder")],"Diglett":[(1,"Scratch"),(15,"Growl"),(19,"Dig"),(24,"Sand Attack"),(31,"Slash"),(40,"Earthquake")],"Sandshrew":[(1,"Scratch"),(10,"Sand Attack"),(17,"Slash"),(24,"Poison Sting"),(31,"Swift"),(38,"Fury Swipes")],"Geodude":[(1,"Tackle"),(11,"Defense Curl"),(16,"Rock Throw"),(21,"Selfdestruct"),(26,"Harden"),(31,"Earthquake"),(36,"Explosion")],"Onix":[(1,"Tackle"),(1,"Screech"),(15,"Bind"),(19,"Rock Throw"),(25,"Rage"),(33,"Slam"),(43,"Harden")],"Ekans":[(1,"Wrap"),(1,"Leer"),(10,"Poison Sting"),(17,"Bite"),(24,"Glare"),(31,"Screech"),(38,"Acid")],"Jigglypuff":[(1,"Sing"),(9,"Pound"),(14,"Disable"),(19,"Defense Curl"),(24,"DoubleSlap"),(29,"Rest"),(34,"Body Slam")],"Zubat":[(1,"Leech Life"),(10,"Supersonic"),(15,"Bite"),(21,"Confuse Ray"),(28,"Wing Attack"),(36,"Haze")],"Paras":[(1,"Scratch"),(13,"Stun Spore"),(20,"Leech Life"),(27,"Spore"),(34,"Slash"),(41,"Growth")],"Clefairy":[(1,"Pound"),(1,"Growl"),(13,"Sing"),(18,"DoubleSlap"),(24,"Minimize"),(31,"Metronome"),(48,"Light Screen")],"Magnemite":[(1,"Tackle"),(21,"SonicBoom"),(25,"ThunderShock"),(35,"Thunder Wave"),(41,"Swift"),(47,"Screech")],"Voltorb":[(1,"Tackle"),(1,"Screech"),(17,"SonicBoom"),(22,"Selfdestruct"),(29,"Light Screen"),(36,"Swift"),(43,"Explosion")],
"Oddish":[(1,"Absorb"),(15,"Poison Powder"),(17,"Stun Spore"),(19,"Sleep Powder"),(24,"Acid"),(33,"Petal Dance"),(46,"SolarBeam")],"Bellsprout":[(1,"Vine Whip"),(1,"Growth"),(13,"Wrap"),(15,"Poison Powder"),(18,"Sleep Powder"),(21,"Stun Spore"),(26,"Acid"),(33,"Razor Leaf"),(42,"Slam")],"Nidorino":[(23,"Focus Energy"),(32,"Fury Attack")],"Nidorina":[(23,"Tail Whip"),(32,"Bite")],"Koffing":[(1,"Tackle"),(1,"Smog"),(32,"Sludge"),(37,"SmokeScreen"),(40,"Selfdestruct"),(45,"Haze"),(48,"Explosion")],"Raticate":[(1,"Tackle"),(1,"Tail Whip"),(1,"Quick Attack"),(14,"Hyper Fang"),(27,"Focus Energy"),(41,"Super Fang")],"Grimer":[(1,"Pound"),(1,"Disable"),(30,"Poison Gas"),(33,"Minimize"),(37,"Sludge"),(42,"Harden"),(48,"Screech"),(55,"Acid Armor")],"Pidgeotto":[(21,"Whirlwind"),(31,"Wing Attack"),(40,"Agility"),(49,"Mirror Move")],"Abra":[(1,"Teleport")],"Horsea":[(1,"Bubble"),(19,"SmokeScreen"),(24,"Leer"),(30,"Water Gun"),(37,"Agility"),(45,"Hydro Pump")],"Goldeen":[(1,"Peck"),(1,"Tail Whip"),(19,"Supersonic"),(24,"Horn Attack"),(30,"Fury Attack"),(37,"Waterfall"),(45,"Horn Drill"),(54,"Agility")],"Shellder":[(1,"Tackle"),(1,"Withdraw"),(18,"Supersonic"),(23,"Clamp"),(30,"Aurora Beam"),(39,"Leer"),(50,"Ice Beam")],"Staryu":[(1,"Tackle"),(17,"Water Gun"),(22,"Harden"),(27,"Recover"),(32,"Swift"),(37,"Minimize"),(42,"Light Screen"),(47,"Hydro Pump")],"Starmie":[(1,"Tackle"),(1,"Water Gun"),(1,"Harden")],"Mankey":[(1,"Scratch"),(1,"Leer"),(15,"Karate Chop"),(21,"Fury Swipes"),(27,"Focus Energy"),(33,"Seismic Toss"),(39,"Thrash")],"Machop":[(1,"Karate Chop"),(20,"Low Kick"),(25,"Leer"),(32,"Focus Energy"),(39,"Seismic Toss"),(46,"Submisson")],"Slowpoke":[(1,"Confusion"),(18,"Disable"),(22,"Headbutt"),(27,"Growl"),(33,"Water Gun"),(40,"Amnesia"),(48,"Psychic")],"Drowzee":[(1,"Pound"),(1,"Hypnosis"),(12,"Disable"),(17,"Confusion"),(24,"Headbutt"),(29,"Poison Gas"),(32,"Psychic"),(37,"Meditate")],"Meowth":[(1,"Scratch"),(1,"Growl"),(12,"Bite"),(17,"Pay Day"),(24,"Screech"),(33,"Fury Swipes"),(44,"Slash")],"Magikarp":[(1,"Splash"),(15,"Tackle")],"Farfetch'd":[(1,"Peck"),(1,"Sand Attack"),(7,"Leer"),(15,"Fury Attack"),(23,"Swords Dance"),(31,"Agility"),(39,"Slash")],"Growlithe":[(1,"Bite"),(1,"Roar"),(18,"Ember"),(23,"Leer"),(30,"Take Down"),(39,"Agility"),(50,"Flamethrower")],"Tentacool":[(1,"Acid"),(7,"Supersonic"),(13,"Wrap"),(18,"Poison Sting"),(22,"Water Gun"),(27,"Constrict"),(33,"Barrier"),(40,"Screech"),(48,"Hydro Pump")],
"Ponyta":[(1,"Ember"),(30,"Tail Whip"),(32,"Stomp"),(35,"Growl"),(39,"Fire Spin"),(43,"Take Down"),(48,"Agility")],"Kadabra":[(16,"Confusion"),(20,"Disable"),(27,"Psybeam"),(31,"Recover"),(38,"Psychic"),(42,"Reflect")],"Raichu":[(1,"ThunderShock"),(1,"Growl"),(1,"Thunder Wave")],"Dugtrio":[(1,"Scratch"),(15,"Growl"),(19,"Dig"),(24,"Sand Attack"),(35,"Slash"),(47,"Earthquake")],"Poliwag":[(1,"Bubble"),(16,"Hypnosis"),(19,"Water Gun"),(25,"DoubleSlap"),(31,"Body Slam"),(38,"Amnesia"),(45,"Hydro Pump")],"Vulpix":[(1,"Ember"),(1,"Tail Whip"),(16,"Quick Attack"),(21,"Roar"),(28,"Confuse Ray"),(35,"Flamethrower"),(42,"Fire Spin")],"Magneton":[(21,"SonicBoom"),(25,"ThunderShock"),(29,"Supersonic"),(38,"Thunder Wave"),(46,"Swift"),(54,"Screech")],"Venonat":[(1,"Tackle"),(1,"Disable"),(24,"Poison Powder"),(27,"Leech Life"),(30,"Stun Spore"),(35,"Psybeam"),(38,"Sleep Powder"),(43,"Psychic")],"Mr. Mime":[(1,"Confusion"),(1,"Barrier"),(23,"Light Screen"),(31,"DoubleSlap"),(39,"Meditate"),(47,"Substitute")],"Poliwhirl":[(1,"Bubble"),(16,"Hypnosis"),(19,"Water Gun"),(26,"DoubleSlap"),(33,"Body Slam"),(41,"Amnesia"),(49,"Hydro Pump")],"Jynx":[(1,"Pound"),(1,"Lovely Kiss"),(18,"Lick"),(23,"DoubleSlap"),(31,"Ice Punch"),(39,"Body Slam"),(47,"Thrash"),(58,"Blizzard")],"Cubone":[(1,"Growl"),(1,"Bone Club"),(25,"Leer"),(31,"Focus Energy"),(38,"Thrash"),(43,"Bonemerang"),(46,"Rage")],"Graveler":[(1,"Tackle"),(11,"Defense Curl"),(16,"Rock Throw"),(21,"Selfdestruct"),(29,"Harden"),(36,"Earthquake"),(43,"Explosion")],"Fearow":[(25,"Mirror Move"),(34,"Drill Peck"),(43,"Agility")],"Arbok":[(27,"Glare"),(36,"Screech"),(47,"Acid")],"Sandslash":[(27,"Poison Sting"),(36,"Swift"),(47,"Fury Swipes")],"Golbat":[(32,"Wing Attack"),(43,"Haze")],"Weepinbell":[(23,"Stun Spore"),(29,"Acid"),(38,"Razor Leaf"),(49,"Slam")],"Gloom":[(28,"Acid"),(38,"Petal Dance"),(52,"SolarBeam")],"Parasect":[(1,"Scratch"),(1,"Stun Spore"),(1,"Leech Life"),(30,"Spore"),(39,"Slash"),(48,"Growth")],"Hypno":[(33,"Poison Gas"),(37,"Psychic"),(43,"Meditate")],"Muk":[(30,"Poison Gas"),(33,"Minimize"),(37,"Sludge"),(45,"Harden"),(53,"Screech"),(60,"Acid Armor")],"Pinsir":[(1,"ViceGrip"),(25,"Seismic Toss"),(30,"Guillotine"),(36,"Focus Energy"),(43,"Harden"),(49,"Slash"),(54,"Swords Dance")],"Dratini":[(1,"Wrap"),(1,"Leer"),(10,"Thunder Wave"),(20,"Agility"),(30,"Slam"),(40,"Dragon Rage"),(50,"Hyper Beam")],
"Porygon":[(1,"Tackle"),(1,"Sharpen"),(1,"Conversion"),(23,"Psybeam"),(28,"Recover"),(35,"Agility"),(42,"Tri Attack")],"Eevee":[(1,"Tackle"),(1,"Sand Attack"),(27,"Quick Attack"),(31,"Tail Whip"),(37,"Bite"),(45,"Take Down")],"Vaporeon":[(1,"Tackle"),(1,"Quick Attack"),(1,"Water Gun"),(1,"Sand Attack"),(27,"Quick Attack"),(31,"Water Gun"),(37,"Tail Whip"),(40,"Bite"),(42,"Acid Armor"),(44,"Haze"),(48,"Mist"),(54,"Hydro Pump")],"Jolteon":[(1,"Tackle"),(1,"Sand Attack"),(27,"Quick Attack"),(31,"ThunderShock"),(37,"Tail Whip"),(40,"Thunder Wave"),(42,"Double Kick"),(44,"Agility"),(48,"Pin Missile"),(54,"Thunder")],"Flareon":[(1,"Tackle"),(1,"Sand Attack"),(27,"Quick Attack"),(31,"Ember"),(37,"Tail Whip"),(40,"Bite"),(42,"Leer"),(48,"Rage"),(54,"Flamethrower")],"Gyarados":[(20,"Bite"),(25,"Dragon Rage"),(32,"Leer"),(41,"Hydro Pump"),(52,"Hyper Beam")],"Vileplume":[(50,"Petal Dance")],"Exeggcute":[(1,"Barrage"),(1,"Hypnosis"),(25,"Reflect"),(28,"Leech Seed"),(32,"Stun Spore"),(37,"Poison Powder"),(42,"SolarBeam"),(48,"Sleep Powder")],"Tangela":[(1,"Constrict"),(1,"Bind"),(29,"Absorb"),(32,"Poison Powder"),(36,"Stun Spore"),(39,"Sleep Powder"),(45,"Slam"),(49,"Growth")],"Victreebel":[(30,"Razor Leaf")],"Nidoking":[(23,"Thrash")],"Nidoqueen":[(23,"Body Slam")],"Clefable":[(50,"Metronome")],"Wigglytuff":[(30,"DoubleSlap")],"Ninetales":[(1,"Roar")],"Arcanine":[(1,"Take Down")],"Poliwrath":[(19,"Water Gun")],"Cloyster":[(50,"Spike Cannon")],"Exeggutor":[(28,"Stomp")],"Kangaskhan":[(1,"Comet Punch"),(1,"Rage"),(26,"Bite"),(31,"Tail Whip"),(36,"Mega Punch"),(41,"Leer"),(46,"Dizzy Punch")],"Rhyhorn":[(1,"Horn Attack"),(30,"Stomp"),(35,"Tail Whip"),(40,"Fury Attack"),(45,"Horn Drill"),(50,"Leer"),(55,"Take Down")],"Gastly":[(1,"Lick"),(1,"Confuse Ray"),(1,"Night Shade"),(27,"Hypnosis"),(35,"Dream Eater")],"Haunter":[(1,"Lick"),(1,"Confuse Ray"),(1,"Night Shade"),(29,"Hypnosis"),(38,"Dream Eater")],"Dodrio":[(39,"Rage"),(45,"Tri Attack"),(51,"Agility")],"Doduo":[(1,"Peck"),(20,"Growl"),(24,"Fury Attack"),(30,"Drill Peck"),(36,"Rage"),(40,"Tri Attack"),(44,"Agility")],"Marowak":[(33,"Focus Energy"),(41,"Thrash"),(48,"Bonemerang"),(55,"Rage")],"Machoke":[(36,"Focus Energy"),(44,"Seismic Toss"),(52,"Submission")],"Primeape":[(37,"Seismic Toss"),(46,"Thrash")],
"Snorlax":[(1,"Headbutt"),(1,"Amnesia"),(1,"Rest"),(35,"Body Slam"),(41,"Harden"),(48,"Double Edge"),(56,"Hyper Beam")],"Lickitung":[(1,"Wrap"),(1,"Supersonic"),(7,"Stomp"),(15,"Disable"),(23,"Defense Curl"),(31,"Slam"),(39,"Screech")],"Chansey":[(1,"Pound"),(1,"DoubleSlap"),(24,"Sing"),(30,"Growl"),(38,"Minimize"),(44,"Defense Curl"),(48,"Light Screen"),(54,"Double Edge")],"Weezing":[(1,"Tackle"),(1,"Smog"),(32,"Sludge"),(39,"SmokeScreen"),(43,"Selfdestruct"),(49,"Haze"),(53,"Explosion")],"Hitmonlee":[(1,"Double Kick"),(1,"Meditate"),(33,"Rolling Kick"),(38,"Jump Kick"),(43,"Focus Energy"),(48,"Hi Jump Kick"),(53,"Mega Kick")],"Tauros":[(1,"Tackle"),(21,"Stomp"),(28,"Tail Whip"),(35,"Leer"),(44,"Rage"),(51,"Take Down")],"Venomoth":[(1,"Tackle"),(1,"Disable"),(24,"Poison Powder"),(27,"Leech Life"),(30,"Stun Spore"),(38,"Psybeam"),(43,"Sleep Powder"),(50,"Psychic")],"Venusaur":[(43,"Growth"),(55,"Sleep Powder"),(65,"SolarBeam")],"Blastoise":[(42,"Skull Bash"),(52,"Hydro Pump")],"Charizard":[(36,"Slash"),(46,"Flamethrower"),(55,"Fire Spin")],"Golem":[(36,"Earthquake"),(43,"Explosion")],"Pidgeot":[(44,"Agility"),(54,"Mirror Move")],"Electrode":[(40,"Swift"),(50,"Explosion")],"Seadra":[(41,"Agility"),(52,"Hydro Pump")],"Seaking":[(39,"Waterfall"),(48,"Horn Drill"),(54,"Agility")],"Alakazam":[(38,"Psychic"),(42,"Reflect")],"Tentacruel":[(35,"Barrier"),(43,"Screech"),(50,"Hydro Pump")],"Persian":[(37,"Fury Swipes"),(51,"Slash")],"Machamp":[(36,"Focus Energy"),(44,"Seismic Toss"),(52,"Submission")],"Dragonair":[(35,"Slam"),(45,"Dragon Rage"),(55,"Hyper Beam")],"Gengar":[(38,"Dream Eater")],"Hitmonchan":[(1,"Comet Punch"),(1,"Agility"),(33,"Fire Punch"),(38,"Ice Punch"),(43,"Thunder Punch"),(48,"Mega Punch"),(53,"Counter")],"Lapras":[(1,"Water Gun"),(1,"Growl"),(16,"Sing"),(20,"Mist"),(25,"Body Slam"),(31,"Confuse Ray"),(38,"Ice Beam"),(46,"Hydro Pump")],"Ditto":[(1,"Transform")],"Krabby":[(1,"Bubble"),(1,"Leer"),(20,"ViceGrip"),(25,"Guillotine"),(30,"Stomp"),(35,"Crabhammer"),(40,"Harden")],"Kingler":[(34,"Stomp"),(42,"Crabhammer"),(49,"Harden")],"Slowbro":[(37,"Withdraw"),(44,"Amnesia"),(55,"Psychic")],"Psyduck":[(1,"Scratch"),(28,"Tail Whip"),(31,"Disable"),(36,"Confusion"),(43,"Fury Swipes"),(52,"Hydro Pump")],
"Golduck":[(39,"Confusion"),(48,"Fury Swipes"),(59,"Hydro Pump")],"Seel":[(1,"Headbutt"),(30,"Growl"),(35,"Aurora Beam"),(40,"Rest"),(45,"Take Down"),(50,"Ice Beam")],"Dewgong":[(35,"Aurora Beam"),(44,"Rest"),(50,"Take Down"),(56,"Ice Beam")],"Omanyte":[(1,"Water Gun"),(1,"Withdraw"),(34,"Horn Attack"),(39,"Leer"),(46,"Spike Cannon"),(53,"Hydro Pump")],"Kabuto":[(1,"Scratch"),(1,"Harden"),(34,"Absorb"),(39,"Slash"),(44,"Leer"),(49,"Hydro Pump")],"Aerodactyl":[(1,"Wing Attack"),(1,"Agility"),(33,"Supersonic"),(38,"Bite"),(45,"Take Down"),(54,"Hyper Beam")],"Rapidash":[(47,"Take Down"),(55,"Agility")],"Magmar":[(1,"Ember"),(36,"Leer"),(39,"Confuse Ray"),(43,"Fire Punch"),(48,"SmokeScreen"),(52,"Smog"),(55,"Flamethrower")],"Electabuzz":[(1,"Quick Attack"),(1,"Leer"),(34,"ThunderShock"),(37,"Screech"),(42,"Thunder Punch"),(49,"Light Screen"),(54,"Thunder")],"Rhydon":[(48,"Horn Drill"),(55,"Leer"),(64,"Take Down")],"Omastar":[(44,"Spike Cannon"),(49,"Hydro Pump")],"Kabutops":[(46,"Leer"),(53,"Hydro Pump")],"Dragonite":[(60,"Hyper Beam")],"Moltres":[(51,"Leer"),(55,"Agility"),(60,"Sky Attack")],"Zapdos":[(51,"Thunder"),(55,"Agility"),(60,"Light Screen")],"Articuno":[(51,"Blizzard"),(55,"Agility"),(60,"Mist")],"Scyther":[(1,"Quick Attack"),(17,"Leer"),(20,"Focus Energy"),(24,"Double Team"),(29,"Slash"),(35,"Swords Dance"),(42,"Agility")],"Mewtwo":[(1,"Confusion"),(1,"Disable"),(1,"Swift"),(1,"Psychic"),(63,"Barrier"),(66,"Psychic"),(70,"Recover"),(75,"Mist"),(81,"Amnesia")],"Mew":[(1,"Pound"),(10,"Transform"),(20,"Mega Punch"),(30,"Metronome"),(40,"Psychic")]}
Pokemon_CatchRates = {"Bulbasaur":45,"Charmander":45,"Squirtle":45,"Wartortle":45,"Pidgey":255,"Rattata":255,"Spearow":255,"NidoranF":235,"NidoranM":235,"Caterpie":255,"Metapod":120,"Butterfree":45,"Weedle":255,"Kakuna":120,"Beedrill":45,"Pikachu":190,"Diglett":255,"Sandshrew":255,"Geodude":255,"Onix":45,"Ekans":255,"Jigglypuff":170,"Zubat":255,"Paras":190,"Clefairy":150,"Magnemite":190,"Voltorb":190,"Oddish":255,"Bellsprout":255,"Ivysaur":45,"Charmeleon":45,"Nidorino":120,"Nidorina":120,"Koffing":190,"Raticate":127,"Grimer":190,"Pidgeotto":120,"Abra":200,"Horsea":225,"Goldeen":225,"Shellder":190,"Staryu":225,"Starmie":60,"Mankey":190,"Machop":180,"Slowpoke":190,"Drowzee":190,"Meowth":255,"Magikarp":255,"Farfetch'd":45,"Growlithe":190,"Tentacool":190,"Ponyta":190,"Kadabra":100,"Raichu":75,"Dugtrio":50,"Poliwag":255,"Vulpix":190,"Magneton":60,"Venonat":190,"Mr. Mime":45,"Poliwhirl":120,"Jynx":45,"Cubone":190,"Graveler":120,"Fearow":90,"Arbok":90,"Sandslash":90,"Golbat":90,"Weepinbell":120,"Gloom":120,"Parasect":75,"Hypno":75,"Muk":75,"Pinsir":45,"Dratini":45,"Porygon":45,"Eevee":45,"Vaporeon":45,"Jolteon":45,"Flareon":45,"Gyarados":45,"Vileplume":45,"Exeggcute":90,"Tangela":45,"Victreebel":45,"Nidoking":45,"Nidoqueen":45,"Clefable":25,"Wigglytuff":50,"Ninetales":75,"Arcanine":75,"Poliwrath":45,"Cloyster":60,"Exeggutor":45,"Kangaskhan":45,"Rhyhorn":120,"Gastly":190,"Haunter":90,"Dodrio":45,"Doduo":190,"Marowak":75,"Machoke":90,"Primeape":75,"Snorlax":25,"Lickitung":45,"Chansey":30,"Weezing":60,"Hitmonlee":45,"Tauros":45,"Venomoth":75,"Venusaur":45,"Blastoise":45,"Charizard":45,"Golem":45,"Pidgeot":45,"Electrode":60,"Seadra":75,"Seaking":60,"Alakazam":50,"Tentacruel":60,"Persian":90,"Machamp":45,"Dragonair":45,"Gengar":45,"Hitmonchan":45,"Lapras":45,"Ditto":35,"Krabby":225,"Kingler":60,"Slowbro":75,"Psyduck":190,"Golduck":75,"Seel":190,"Dewgong":75,"Omanyte":45,"Kabuto":45,"Aerodactyl":45,"Rapidash":60,"Magmar":45,"Electabuzz":45,"Rhydon":60,"Omastar":45,"Kabutops":45,"Dragonite":45,"Moltres":3,"Zapdos":3,"Articuno":3,"Scyther":45,"Mewtwo":3,"Mew":45}
Pokemon_Evolutions = {"Bulbasaur":[16,"Ivysaur"],"Ivysaur":[36,"Venusaur"],"Charmander":[16,"Charmeleon"],"Charmeleon":[36,"Charizard"],"Squirtle":[16,"Wartortle"],"Wartortle":[36,"Blastoise"],"Pidgey":[18,"Pidgeotto"],"Rattata":[20,"Raticate"],"Spearow":[20,"Fearow"],"NidoranF":[16,"Nidorina"],"NidoranM":[16,"Nidorino"],"Caterpie":[7,"Metapod"],"Metapod":[10,"Butterfree"],"Butterfree":[101,""],"Weedle":[7,"Kakuna"],"Kakuna":[10,"Beedrill"],"Beedrill":[101,""],"Pikachu":[101,""],"Diglett":[26,"Dugtrio"],"Sandshrew":[22,"Sandslash"],"Geodude":[25,"Graveler"],"Onix":[101,""],"Ekans":[22,"Arbok"],"Jigglypuff":[101,"Wigglytuff"],"Zubat":[22,"Golbat"],"Paras":[24,"Parasect"],"Clefairy":[101,"Clefable"],"Magnemite":[30,"Magneton"],"Voltorb":[30,"Electrode"],"Oddish":[21,"Gloom"],"Bellsprout":[21,"Weepinbell"],"Nidorino":[101,"Nidoking"],"Nidorina":[101,"Nidoqueen"],"Koffing":[35,"Weezing"],"Raticate":[101,""],"Grimer":[38,"Muk"],"Pidgeotto":[36,"Pidgeot"],"Abra":[16,"Kadabra"],"Horsea":[32,"Seadra"],"Goldeen":[33,"Seaking"],"Shellder":[101,"Cloyster"],"Staryu":[101,"Starmie"],"Starmie":[101,""],"Mankey":[28,"Primeape"],"Machop":[28,"Machoke"],"Slowpoke":[37,"Slowbro"],"Drowzee":[26,"Hypno"],"Meowth":[28,"Persian"],"Magikarp":[20,"Gyarados"],"Farfetch'd":[101,""],"Growlithe":[101,"Arcanine"],"Tentacool":[30,"Tentacruel"],'Ponyta':[40,"Rapidash"],"Kadabra":[101,"Alakazam"],"Raichu":[101,""],"Dugtrio":[101,""],"Poliwag":[25,"Poliwhirl"],"Vulpix":[101,"Ninetales"],"Magneton":[101,""],"Venonat":[31,"Venomoth"],"Mr. Mime":[101,""],"Poliwhirl":[101,"Poliwrath"],"Jynx":[101,""],"Cubone":[28,"Marowak"],"Graveler":[36,"Golem"],"Fearow":[101,""],"Arbok":[101,""],"Sandslash":[101,""],"Golbat":[101,""],"Weepinbell":[101,"Victreebel"],"Gloom":[101,"Vileplume"],"Parasect":[101,""],"Hypno":[101,""],"Muk":[101,""],"Pinsir":[101,""],"Dratini":[30,"Dragonair"],"Porygon":[101,""],"Eevee":[101,""],"Vaporeon":[101,""],"Jolteon":[101,""],"Flareon":[101,""],"Gyarados":[101,""],"Vileplume":[101,""],
                      "Exeggcute":[101,"Exeggutor"],"Tangela":[101,""],"Victreebel":[101,""],"Nidoking":[101,""],"Nidoqueen":[101,""],"Clefable":[101,""],"Wigglytuff":[101,""],"Ninetales":[101,""],"Arcanine":[101,""],"Poliwrath":[101,""],"Cloyster":[101,""],"Exeggutor":[101,""],"Kangaskhan":[101,""],"Rhyhorn":[42,"Rhydon"],"Gastly":[25,"Haunter"],"Haunter":[36,"Gengar"],"Doduo":[31,"Dodrio"],"Dodrio":[101,""],"Marowak":[101,""],"Machoke":[36,"Machamp"],"Primeape":[101,""],"Snorlax":[101,""],"Lickitung":[101,""],"Chansey":[101,""],"Weezing":[101,""],"Hitmonlee":[101,""],"Tauros":[101,""],"Venomoth":[101,""],"Venusaur":[101,""],"Blastoise":[101,""],"Charizard":[101,""],"Golem":[101,""],"Pidgeot":[101,""],"Electrode":[101,""],"Seadra":[101,""],"Seaking":[101,""],"Alakazam":[101,""],"Tentacruel":[101,""],"Persian":[101,""],"Machamp":[101,""],"Dragonair":[55,"Dragonite"],"Gengar":[101,""],"Hitmonchan":[101,""],"Lapras":[101,""],"Ditto":[101,""],"Krabby":[28,"Kingler"],"Kingler":[101,""],"Slowbro":[101,""],"Psyduck":[33,"Golduck"],"Golduck":[101,""],"Seel":[34,"Dewgong"],"Dewgong":[101,""],"Omanyte":[40,"Omastar"],"Kabuto":[40,"Kabutops"],"Aerodactyl":[101,""],"Rapidash":[101,""],"Magmar":[101,""],"Electabuzz":[101,""],"Rhydon":[101,""],"Omastar":[101,""],"Kabutops":[101,""],"Dragonite":[101,""],"Moltres":[101,""],"Zapdos":[101,""],"Articuno":[101,""],"Scyther":[101,""],"Mewtwo":[101,""],"Mew":[101,""]}

def Two_D_ListCheck(List:list,item:str) -> bool:
    Check = False
    for i in range(len(List)):
        if item in List[i]:
            Check = True
            break
    return Check

class EvolutionStones:
    def __init__(self,Name,Pokemon):
        self.Name = Name
        self.Pokemon = Pokemon

PokeStones = [EvolutionStones("Moon Stone",["Nidorina","Nidorino","Clefairy","Jigglypuff"]),EvolutionStones("Fire Stone",["Vulpix","Growlithe","Eevee"]),EvolutionStones("Thunder Stone",["Pikachu","Eevee"]),EvolutionStones("Water Stone",["Poliwhirl","Eevee","Shellder","Staryu"]),EvolutionStones("Leaf Stone",["Gloom","Weepinbell","Exeggcute"])]
def Get_Stone(Name:str):
    for i in PokeStones:
        if i.Name == Name: return i

class PokemonMoves:
    def __init__(self):
        self.Type = ''
        self.Crit = False
        self.TypeDamage = 1
        self.HMMoves = ["Cut","Fly","Surf","Strength"]
        self.SpecialMoves = ["Water","Grass","Fire","Ice","Electric","Psychic","Dragon"]
        self.NormalDamagingList = ["Tackle","Scratch","Gust","Peck","Horn Attack","Pound","Vine Whip","Water Gun","Rock Throw","Mega Punch","Seismic Toss","Splash","Cut","SonicBoom","Pay Day","Rage","Swift","ViceGrip","Dragon Rage","Egg Bomb","Mega Kick","Rock Slide","Tri Attack","Night Shade","Hydro Pump","Drill Peck","Surf","Earthquake","Wing Attack","Slam","Strength","PsyWave","Guillotine","Horn Drill","Fissure","Super Fang","Dizzy Punch","Waterfall"]
        self.EnemyStatChangingList = ["Growl","Tail Whip","Sand Attack","Leer","String Shot","Screech","Flash","SmokeScreen"]
        self.SelfStatChangingList = ["Harden","Defense Curl","Growth","Withdraw","Barrier","Minimize","Swords Dance","Sharpen","Agility","Double Team","Amnesia","Meditate","Acid Armor"]
        self.StatusDamagingList = ["Ember","Confusion","Poison Sting","ThunderShock","Smog","Body Slam","Thunderbolt","Twineedle","Lick","Psybeam","Ice Beam","Sludge","Fire Punch","Blizzard","Flamethrower","Fire Blast","Thunder","Ice Punch","Thunder Punch"]
        self.StatusList = ["Thunder Wave","Sing","Supersonic","Poison Powder","Stun Spore","Hypnosis","Sleep Powder","Lovely Kiss","Confuse Ray","Poison Gas","Glare","Toxic","Spore"]
        self.EnemyStatDamagingList = ["Bubble","BubbleBeam","Acid","Constrict","Psychic","Aurora Beam"]
        self.FieldAffectingList = ["Leech Seed"]
        self.DrainingAttacksList = ["Leech Life","Absorb","Dream Eater","Mega Drain"]
        self.PriorityDamagingList = ["Quick Attack","Counter"]
        self.MultiturnMovesList = ["Bide","Dig","Hyper Beam","Razor Wind","Skull Bash","SolarBeam","Fly","Sky Attack"]
        self.MultihitList = ["Fury Attack","DoubleSlap","Fury Swipes","Barrage","Comet Punch","Double Kick","Spike Cannon","Bonemerang"]
        self.TrappingMoves = ["Wrap","Bind","Clamp","Fire Spin"]
        self.FlinchingMoves = ["Hyper Fang","Bite","Low Kick","Bone Club","Stomp","Headbutt","Rolling Kick"]
        self.WildBattleMoves = ["Whirlwind","Teleport","Roar"]
        self.HighCritMoves = ["Karate Chop","Slash","Razor Leaf","Crabhammer"]
        self.SelfFaintingMoves = ["Selfdestruct","Explosion"]
        self.RampageMoves = ["Thrash","Petal Dance"]
        self.RecoilMoves = ["Struggle","Take Down","Submission","Double Edge","Jump Kick","Hi Jump Kick"]
        self.HealingMoves = ["Recover","Softboiled"]
        self.UnAffectedFlyMoves = ["Recover","Softboiled","Teleport","Focus Energy","Light Screen","Reflect","Rest","Metronome","Mirror Move","Substitute","Transform","Mist","Haze"]
    
    def Physical_Damage_Calculation(self,Attacker,Defender,Power:int,MoveType:str,Move:str):
        STAB = 1
        TYPE1 = self.Type_Calculation(MoveType,Defender.Type[0])
        TYPE2 = self.Type_Calculation(MoveType,Defender.Type[1])
        if Defender.Type[1] == "":TYPE2 = 1
        if Move == "Counter":
            if TYPE1 == 0:TYPE1 = 1
        CRIT = 1
        RANDOM = round(random.randint(217,255)/255,2)
        if MoveType in Attacker.Type:
            STAB = 1.5
        self.Crit = self.Crit_Calculation(Attacker)
        if self.Crit:
            A = Attacker.Atk
            D = Defender.DEF
            CRIT = 2
        if not self.Crit: 
            A = Attacker.GetBattleAttack()
            D = Defender.DEF*Defender.DEFModifier
            CRIT = 1
            if Attacker.ReflectUp:A *= 2**Attacker.ReflectDamage
            if A > 1024: A = 1024
        if Attacker.Atk > 255 or Defender.DEF > 255:
            A = floor(A/4)
            D = floor(D/4)
        if Move in ("Selfdestruct","Explosion"):
            D = D//2
        Damage = ((((2 * Attacker.Level * CRIT)/5 + 2) * Power * (A/D))/50 + 2) * STAB * TYPE1 * TYPE2 * RANDOM
        return round(Damage),self.Crit,TYPE2*TYPE1

    def Special_Damage_Calculation(self,Attacker,Defender,Power:int,MoveType:str,Move:str):
        STAB = 1
        TYPE1 = self.Type_Calculation(MoveType,Defender.Type[0])
        TYPE2 = self.Type_Calculation(MoveType,Defender.Type[1])
        if Defender.Type[1] == "":TYPE2 = 1
        CRIT = 1
        RANDOM = round(random.randint(217,255)/255,2)
        if MoveType in Attacker.Type:
            STAB = 1.5
        self.Crit = self.Crit_Calculation(Attacker)
        if self.Crit:
            A = Attacker.SPECIAL
            D = Defender.SPECIAL
            CRIT = 2
        if not self.Crit: 
            A = Attacker.SPECIAL*Attacker.SPECIALModifier
            D = Defender.SPECIAL*Defender.SPECIALModifier
            CRIT = 1
            if Attacker.LightScreenUp:A *= 2**Attacker.LightScreenDamage
            if A > 1024: A = 1024
        if Attacker.SPECIAL > 255 or Defender.SPECIAL > 255:
            A = floor(A/4)
            D = floor(D/4)
        Damage = ((((2 * Attacker.Level * CRIT)/5 + 2) * Power * (A/D))/50 + 2) * STAB * TYPE1 * TYPE2 * RANDOM
        return round(Damage),self.Crit,TYPE2*TYPE1
 
    def Confusion_Damage_Calculation(self,Attacker):
        STAB = 1
        TYPE1 = 1
        TYPE2 = 1
        CRIT = 1
        RANDOM = round(random.randint(217,255)/255,2)
        A = Attacker.GetBattleAttack()
        D = Attacker.DEF*Attacker.DEFModifier
        if Attacker.Atk > 255:
            A = floor(A/4)
            D = floor(D/4)
        Damage = ((((2 * Attacker.Level * CRIT)/5 + 2) * 40 * (A/D))/50 + 2) * STAB * TYPE1 * TYPE2 * RANDOM
        return round(Damage)

    def Accuracy_Calculation(self,Attacker,Defender,MoveAccuracy:int):
        if Defender.Dig:return False
        A = MoveAccuracy/100
        T = (A*255) * Attacker.Accuracy * Defender.Evasion
        R = random.randint(0,255)
        if T == 255 and R == 255: return True
        return R < T

    def Type_Calculation(self,Movetype:str,Defendertype:str):
        if Movetype == "Grass":
            if Defendertype in ("Water","Rock","Ground"):
                return 2
            elif Defendertype in ("Fire","Grass","Poison","Flying","Bug","Dragon"):
                return 0.5
            else:
                return 1
        elif Movetype == "Fire":
            if Defendertype in ("Ice","Bug","Grass"):
                return 2
            elif Defendertype in ("Water","Rock","Fire","Dragon"):
                return 0.5
            else:
                return 1
        elif Movetype == "Water":
            if Defendertype in ("Fire","Rock","Ground"):
                return 2
            elif Defendertype in ("Water","Grass","Dragon"):
                return 0.5
            else:
                return 1
        elif Movetype == "Normal":
            if Defendertype == "Rock":
                return 0.5
            elif Defendertype == "Ghost":
                return 0
            else:
                return 1
        elif Movetype == "Electric":
            if Defendertype in ("Water","Flying"):
                return 2
            elif Defendertype in ("Electric","Grass","Dragon"):
                return 0.5
            elif Defendertype == "Ground":
                return 0
            else:
                return 1
        elif Movetype == "Ice":
            if Defendertype in ("Grass","Flying","Dragon","Ground"):
                return 2
            elif Defendertype in ("Ice","Water"):
                return 0.5
            else:
                return 1
        elif Movetype == "Fighting":
            if Defendertype in ("Normal","Rock","Ice"):
                return 2
            elif Defendertype in ("Flying","Bug","Poison","Psychic"):
                return 0.5
            elif Defendertype in ("Ghost"):
                return 0
            else:
                return 1
        elif Movetype == "Poison":
            if Defendertype in ("Bug","Grass"):
                return 2
            elif Defendertype in ("Poison","Ground","Dragon","Rock","Ghost"):
                return 0.5
            else:
                return 1
        elif Movetype == "Ground":
            if Defendertype in ("Electric","Fire","Rock","Poison"):
                return 2
            elif Defendertype in ("Bug","Grass"):
                return 0.5
            elif Defendertype in ("Flying"):
                return 0
            else:
                return 1
        elif Movetype == "Flying":
            if Defendertype in ("Bug","Grass","Fighting"):
                return 2
            elif Defendertype in ("Electric","Rock"):
                return 0.5
            else:
                return 1
        elif Movetype == "Psychic":
            if Defendertype in ("Poison","Fighting"):
                return 2
            elif Defendertype in ("Psychic"):
                return 0.5
            else:
                        return 1
        elif Movetype == "Bug":
            if Defendertype in ("Psychic","Grass","Poison"):
                return 2
            elif Defendertype in ("Flying","Fire","Fighting","Ghost"):
                return 0.5
            else:
                return 1
        elif Movetype == "Rock":
            if Defendertype in ("Fire","Flying","Bug","Ice"):
                return 2
            elif Defendertype in ("Ground","Fighting"):
                return 0.5
            else:
                return 1
        elif Movetype == "Ghost":
            if Defendertype in ("Ghost","Psychic"):
                return 2
            elif Defendertype in ("Normal"):
                return 0
            else:
                return 1
        elif Movetype == "Dragon":
            if Defendertype in ("Dragon"):
                return 2
            else:
                return 1
        else: return 1

    def Crit_Calculation(self,Attacker) -> bool:
        Threshold = round(Attacker.SPEED/2)
        if Attacker.Attack in self.HighCritMoves: Threshold = min(8 *round(Attacker.SPEED/2),255)
        if Attacker.FocusEnergy:Threshold *= 4
        if Threshold > 255: Threshold = 255
        Crit = random.randint(0,255)
        return Crit < Threshold or Threshold == 255

    def Tackle(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,95)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,35,"Normal","Tackle")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation
    
    def Slam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,85,"Normal","Slam")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation
    
    def Strength(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Normal","Strength")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation
    
    def Dizzy_Punch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,70,"Normal","Dizzy Punch")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation
    
    def Tri_Attack(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Normal","Tri Attack")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tri_Attack_Animation
    
    def Swift(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,60,"Normal","Swift")
        if Effect == 2: Text1 = "It was super Effective"
        if Effect == 1: Text1 = ''
        if Effect == 0:
            Text2 = ''
            Text1 = "It had no effect!"
        elif Effect < 1: Text1 = "It wasn't very effective"
        if Crit and Effect > 0: 
            Text2 = "It was a critical Hit!!"
        if not Crit or Effect == 0 : Text2 = ''
        return Damage,Text1,Text2,Attacker.Swift_Animation
    
    def Rage(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,20,"Normal","Rage")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation
    
    def Splash(self,Attacker,Defender):
        return 0,"No Effect","",Attacker.Tackle_Animation
    
    def Scratch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,40,"Normal","Scratch")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Scratch_Animation

    def Gust(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,40,"Normal","Gust")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Gust_Animation

    def Peck(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,35,"Flying","Gust")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Peck_Animation

    def Horn_Attack(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65,"Normal","Horn Attack")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Horn_Attack_Animation

    def Pound(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,40,"Normal","Pound")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation

    def Vine_Whip(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,35,"Grass","Vine Whip")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Vine_Whip_Animation

    def PsyWave(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,80)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,random.randint(1,int(1.5*Attacker.Level)),"Psychic","PsyWave")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.PsyWave_Animation

    def Cut(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,95)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Normal","Cut")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Scratch_Animation

    def SonicBoom(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage = 20
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Roar_Animation

    def Rock_Slide(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,75,"Rock","Rock Slide")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Rock_Slide_Animation

    def Earthquake(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,100,"Ground","Earthquake")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Earthquake_Animation

    def Dragon_Rage(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage = 40
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Dragon_Rage_Animation

    def Super_Fang(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage = Defender.HP//2
            if Damage < 1:Damage = 1
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Hyper_Fang_Animation

    def Seismic_Toss(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage = Attacker.Level
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation

    def Night_Shade(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage = Attacker.Level
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Night_Shade_Animation

    def Mega_Kick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,120,"Normal","Mega Kick")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation

    def Wing_Attack(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,35,"Flying","Wing Attack")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation

    def Horn_Drill(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,30)
        if Hit and Attacker.GetBattleSpeed() > Defender.GetBattleSpeed(): 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65535,"Normal","Horn Drill")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Horn_Attack_Animation

    def Guillotine(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,30)
        if Hit and Attacker.GetBattleSpeed() > Defender.GetBattleSpeed(): 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65535,"Normal","Guillotine")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation

    def Fissure(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,30)
        if Hit and Attacker.GetBattleSpeed() > Defender.GetBattleSpeed(): 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65535,"Ground","Fissure")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Rock_Slide_Animation

    def Quick_Attack(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,40,"Normal","Quick Attack")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,1,Attacker.Quick_Attack_Animation

    def Counter(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit and Attacker.CounterDamage > 0: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,Attacker.CounterDamage,"Fighting","Counter")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,-5,Attacker.Tackle_Animation

    def Water_Gun(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,40,"Water","Water Gun")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Water_Gun_Animation

    def Waterfall(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,80,"Water","Waterfall")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Waterfall_Animation

    def Hydro_Pump(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,80)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,110,"Water","Hydro Pump")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Hydro_Pump_Animation

    def Surf(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,95,"Water","Surf")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Surf_Animation

    def Rock_Throw(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,65)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Rock","Rock Throw")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Rock_Throw_Animation

    def Egg_Bomb(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,100,"Normal","Egg Bomb")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Egg_Bomb_Animation

    def Mega_Punch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Normal","Mega Punch")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Tackle_Animation

    def Pay_Day(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,40,"Normal","Pay Day")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Pay_Day_Animation

    def Struggle(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        Recoil = 0
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Normal","Struggle")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
                Text3 = ""
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            Text3 = f"{Attacker.NickName} took recoil damage"
            if not Crit or Effect == 0 : 
                Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        Recoil = Damage//2
        return Damage,Text1,Text2,Text3,Recoil,Attacker.Tackle_Animation
    
    def Take_Down(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        Recoil = 0
        if Hit: 
            Text3 = f"{Attacker.NickName} took recoil damage"
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,90,"Normal","Take Down")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
                Text3 = ""
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : 
                Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        Recoil = Damage//4
        return Damage,Text1,Text2,Text3,Recoil,Attacker.Tackle_Animation
    
    def Double_Edge(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        Recoil = 0
        if Hit: 
            Text3 = f"{Attacker.NickName} took recoil damage"
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,100,"Normal","Double Edge")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
                Text3 = ""
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : 
                Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        Recoil = Damage//4
        return Damage,Text1,Text2,Text3,Recoil,Attacker.Tackle_Animation
    
    def Submission(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,80)
        Recoil = 0
        if Hit: 
            Text3 = f"{Attacker.NickName} took recoil damage"
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Fighting","Submission")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
                Text3 = ""
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : 
                Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        Recoil = Damage//4
        return Damage,Text1,Text2,Text3,Recoil,Attacker.Tackle_Animation
    
    def Jump_Kick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,95)
        Recoil = 0
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,70,"Fighting","Jump Kick")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
                Text3 = ""
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : 
                Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = f"{Attacker.NickName} Crashed"
            Recoil = 1
        return Damage,Text1,Text2,Text3,Recoil,Attacker.Tackle_Animation
    
    def Hi_Jump_Kick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        Recoil = 0
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,85,"Fighting","Hi Jump Kick")
            if Effect == 2: Text1 = "It was super Effective"
            if Effect == 1: Text1 = ''
            if Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
                Text3 = ""
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: 
                Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : 
                Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = f"{Attacker.NickName} Crashed"
            Recoil = 1
        return Damage,Text1,Text2,Text3,Recoil,Attacker.Tackle_Animation
    
    def Headbutt(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,70,"Normal","Headbutt")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Tackle_Animation

    def ViceGrip(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,55,"Normal","ViceGrip")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Scratch_Animation

    def Drill_Peck(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Flying","Drill Peck")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Drill_Peck_Animation

    def Tail_Whip(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.DEFCounter > -6:
                Defender.DEFCounter -= 1
                Text1 = f"{Defender.NickName}'s Defense went Down"
            else:
                Text1 = f"{Defender.NickName}'s Defense is too low"
        else:
            Text1 = "It missed"
        return Defender.DEFCounter,Text1,'Defense',Attacker.Tail_Whip_Animation

    def Growl(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.AtkCounter > -6:
                Defender.AtkCounter -= 1
                Text1 = f"{Defender.NickName}'s Attack went Down"
            else:
                Text1 = f"{Defender.NickName}'s Attack is too low"
        else:
            Text1 = "It missed"
        return Defender.AtkCounter,Text1,'Attack',Attacker.Growl_Animation

    def Sand_Attack(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.ACCURACYCounter > -6:
                Defender.ACCURACYCounter -= 1
                Text1 = f"{Defender.NickName}'s Accuracy went Down"
            else:
                Text1 = f"{Defender.NickName}'s Accuracy is too low"
        else:
            Text1 = "It missed"
        return Defender.ACCURACYCounter,Text1,'Accuracy',Attacker.Sand_Attack_Animation

    def Leer(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.DEFCounter > -6:
                Defender.DEFCounter -= 1
                Text1 = f"{Defender.NickName}'s Defense went Down"
            else:
                Text1 = f"{Defender.NickName}'s Defense is too low"
        else:
            Text1 = "It missed"
        return Defender.DEFCounter,Text1,'Defense',Attacker.Leer_Animation

    def String_Shot(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,95)
        if Hit:
            if Defender.SPEEDCounter > -6:
                Defender.SPEEDCounter -= 1
                Text1 = f"{Defender.NickName}'s Speed went Down"
            else:
                Text1 = f"{Defender.NickName}'s Speed is too low"
        else:
            Text1 = "It missed"
        return Defender.SPEEDCounter,Text1,'Speed',Attacker.String_Shot_Animation

    def Screech(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit:
            if Defender.DEFCounter > -6:
                Defender.DEFCounter -= 2
                Text1 = f"{Defender.NickName}'s Defense sharply decreased"
            else:
                Text1 = f"{Defender.NickName}'s Defense is too low"
        else:
            Text1 = "It missed"
        return Defender.DEFCounter,Text1,'Defense',Attacker.Screech_Animation

    def Flash(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,70)
        if Hit:
            if Defender.ACCURACYCounter > -6:
                Defender.ACCURACYCounter -= 1
                Text1 = f"{Defender.NickName} was slightly blinded"
            else:
                Text1 = f"{Defender.NickName} is Blind"
        else:
            Text1 = "It missed"
        return Defender.ACCURACYCounter,Text1,'Accuracy',Attacker.Flash_Animation

    def SmokeScreen(self,Attacker,Defender):
        Text1 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.ACCURACYCounter > -6:
                Defender.ACCURACYCounter -= 1
                Text1 = f"{Defender.NickName}'s vision was clouded"
            else:
                Text1 = f"{Defender.NickName} is Blind"
        else:
            Text1 = "It missed"
        return Defender.ACCURACYCounter,Text1,'Accuracy',Attacker.SmokeScreen_Animation

    def Harden(self,Attacker):
        Text1 = ""
        if Attacker.DEFCounter < 6:
            Attacker.DEFCounter += 1
            Text1 = f"{Attacker.NickName}'s Defense went up"
        else: Text1 = f"{Attacker.NickName}'s Defense is too high"
        return Attacker.DEFCounter,Text1,'Defense',Attacker.Harden_Animation

    def Acid_Armor(self,Attacker):
        Text1 = ""
        if Attacker.DEFCounter < 6:
            Attacker.DEFCounter += 2
            Text1 = f"{Attacker.NickName}'s Defense sharply rose"
        else: Text1 = f"{Attacker.NickName}'s Defense is too high"
        return Attacker.DEFCounter,Text1,'Defense',Attacker.Acid_Armor_Animation

    def Barrier(self,Attacker):
        Text1 = ""
        if Attacker.DEFCounter < 6:
            Attacker.DEFCounter += 2
            Text1 = f"{Attacker.NickName}'s Defense sharply increased"
        else: Text1 = f"{Attacker.NickName}'s Defense is too high"
        return Attacker.DEFCounter,Text1,'Defense',Attacker.Teleport_Animation

    def Defense_Curl(self,Attacker):
        Text1 = ""
        if Attacker.DEFCounter < 6:
            Attacker.DEFCounter += 1
            Text1 = f"{Attacker.NickName}'s Defense went up"
        else: Text1 = f"{Attacker.NickName}'s Defense is too high"
        return Attacker.DEFCounter,Text1,'Defense',Attacker.Defense_Curl_Animation

    def Growth(self,Attacker):
        Text1 = ""
        if Attacker.SPECIALCounter < 6:
            Attacker.SPECIALCounter += 1
            Text1 = f"{Attacker.NickName}'s Special went up"
        else: Text1 = f"{Attacker.NickName}'s Special is too high"
        return Attacker.SPECIALCounter,Text1,'Special',Attacker.Growth_Animation

    def Withdraw(self,Attacker):
        Text1 = ""
        if Attacker.DEFCounter < 6:
            Attacker.DEFCounter += 1
            Text1 = f"{Attacker.NickName}'s Defense went up"
        else: Text1 = f"{Attacker.NickName}'s Defense is too high"
        return Attacker.DEFCounter,Text1,'Defense',Attacker.Withdraw_Animation

    def Minimize(self,Attacker):
        Text1 = ""
        if Attacker.EVASIONCounter < 6:
            Attacker.EVASIONCounter += 1
            Text1 = f"{Attacker.NickName} got smaller"
        else: Text1 = f"{Attacker.NickName} is too smaller"
        return Attacker.EVASIONCounter,Text1,'Evasion',Attacker.Defense_Curl_Animation

    def Double_Team(self,Attacker):
        Text1 = ""
        if Attacker.EVASIONCounter < 6:
            Attacker.EVASIONCounter += 1
            Text1 = f"{Attacker.NickName}'s evasion rose"
        else: Text1 = f"{Attacker.NickName}'s evasion is too high"
        return Attacker.EVASIONCounter,Text1,'Evasion',Attacker.Defense_Curl_Animation

    def Swords_Dance(self,Attacker):
        Text1 = ""
        if Attacker.AtkCounter < 6:
            Attacker.AtkCounter += 2
            Text1 = f"{Attacker.NickName}'s Attack sharply increased"
        else: Text1 = f"{Attacker.NickName}'s Attack is too high"
        return Attacker.AtkCounter,Text1,'Attack',Attacker.Swords_Dance_Animation

    def Sharpen(self,Attacker):
        Text1 = ""
        if Attacker.AtkCounter < 6:
            Attacker.AtkCounter += 1
            Text1 = f"{Attacker.NickName}'s Attack increased"
        else: Text1 = f"{Attacker.NickName}'s Attack is too high"
        return Attacker.AtkCounter,Text1,'Attack',Attacker.Harden_Animation

    def Meditate(self,Attacker):
        Text1 = ""
        if Attacker.AtkCounter < 6:
            Attacker.AtkCounter += 1
            Text1 = f"{Attacker.NickName}'s Attack increased"
        else: Text1 = f"{Attacker.NickName}'s Attack is too high"
        return Attacker.AtkCounter,Text1,'Attack',Attacker.Teleport_Animation

    def Agility(self,Attacker):
        Text1 = ""
        if Attacker.SPEEDCounter < 6:
            Attacker.SPEEDCounter += 2
            Text1 = f"{Attacker.NickName}'s Speed sharply increased"
        else: Text1 = f"{Attacker.NickName}'s Speed is too high"
        return Attacker.SPEEDCounter,Text1,"Speed",Attacker.Teleport_Animation

    def Amnesia(self,Attacker):
        Text1 = ""
        if Attacker.SPECIALCounter < 6:
            Attacker.SPECIALCounter += 2
            Text1 = f"{Attacker.NickName}'s Special sharply increased"
        else: Text1 = f"{Attacker.NickName}'s Special is too high"
        return Attacker.SPECIALCounter,Text1,"Special",Attacker.Teleport_Animation

    def Ember(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,40,"Fire","Ember")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1  and Defender.Status == "OK" and "Fire" not in Defender.Type: 
                effect = "BRN"
                Text3 = f"{Defender.NickName} was burned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Ember_Animation,effect

    def Flamethrower(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,95,"Fire","Flamethrower")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1  and Defender.Status == "OK" and "Fire" not in Defender.Type: 
                effect = "BRN"
                Text3 = f"{Defender.NickName} was burned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Flamethrower_Animation,effect

    def Fire_Blast(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,120,"Fire","Fire Blast")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) in (1,2,3)  and Defender.Status == "OK" and "Fire" not in Defender.Type: 
                effect = "BRN"
                Text3 = f"{Defender.NickName} was burned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Fire_Blast_Animation,effect

    def Fire_Punch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,75,"Fire","Fire Punch")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1  and Defender.Status == "OK" and "Fire" not in Defender.Type: 
                effect = "BRN"
                Text3 = f"{Defender.NickName} was burned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Fire_Punch_Animation,effect

    def Ice_Punch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,75,"Ice","Ice Punch")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1  and Defender.Status == "OK": 
                effect = "FRZ"
                Text3 = f"{Defender.NickName} was Frozen"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Ice_Punch_Animation,effect

    def Blizzard(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,110,"Ice","Blizzard")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1  and Defender.Status == "OK": 
                effect = "FRZ"
                Text3 = f"{Defender.NickName} was Frozen"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Blizzard_Animation,effect

    def Confusion(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,50,"Psychic","Confusion")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1 and Defender.Status2 == "": 
                effect = "Confused"
                Text3 = f"{Defender.NickName} got Confused"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Confusion_Animation,effect

    def Psybeam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,65,"Psychic","Psybeam")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1 and Defender.Status2 == "": 
                effect = "Confused"
                Text3 = f"{Defender.NickName} got Confused"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Psybeam_Animation,effect

    def Poison_Sting(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,5)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,15,"Poison","Poison Sting")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 2 and Defender.Status == "OK" and "Poison" not in Defender.Type: 
                effect = "PSN"
                Text3 = f"{Defender.NickName} was Poisoned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Poison_Sting_Animation,effect

    def Sludge(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65,"Poison","Sludge")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r in (1,2,3,4) and Defender.Status == "OK" and "Poison" not in Defender.Type: 
                effect = "PSN"
                Text3 = f"{Defender.NickName} was Poisoned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Sludge_Animation,effect

    def Twineedle(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,5)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Bug","Twineedle")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 2 and Defender.Status == "OK" and "Poison" not in Defender.Type: 
                effect = "PSN"
                Text3 = f"{Defender.NickName} was Poisoned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Twineedle_Animation,effect

    def ThunderShock(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,40,"Electric","ThunderShock")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and "Electric" not in Defender.Type: 
                effect = "PAR"
                Text3 = f"{Defender.NickName} was Paralyzed"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.ThunderShock_Animation,effect

    def Thunderbolt(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,90,"Electric","Thunderbolt")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and "Electric" not in Defender.Type: 
                effect = "PAR"
                Text3 = f"{Defender.NickName} was Paralyzed"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Thunderbolt_Animation,effect

    def Thunder_Punch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,75,"Electric","Thunder Punch")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and "Electric" not in Defender.Type: 
                effect = "PAR"
                Text3 = f"{Defender.NickName} was Paralyzed"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Thunder_Punch_Animation,effect

    def Thunder(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,70)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,110,"Electric","Thunder")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and "Electric" not in Defender.Type: 
                effect = "PAR"
                Text3 = f"{Defender.NickName} was Paralyzed"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Thunder_Animation,effect

    def Ice_Beam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,95,"Ice","Ice Beam")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and "Ice" not in Defender.Type: 
                effect = "FRZ"
                Text3 = f"{Defender.NickName} was Frozen"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Ice_Beam_Animation,effect

    def Lick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,20,"Ghost","Lick")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and  "Ghost" not in Defender.Type: 
                effect = "PAR"
                Text3 = f"{Defender.NickName} was Paralyzed"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Lick_Animation,effect

    def Smog(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,10)
        Hit = self.Accuracy_Calculation(Attacker,Defender,70)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,20,"Poison","Smog")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r in (1,2,3,4) and Defender.Status == "OK" and "Poison" not in Defender.Type: 
                effect = "PSN"
                Text3 = f"{Defender.NickName} was Poisoned"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Smog_Animation,effect

    def Body_Slam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        effect = "OK"
        r = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,85,"Normal","Body Slam")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if r == 1 and Defender.Status == "OK" and "Normal" not in Defender.Type and "Ghost" not in Defender.Type: 
                effect = "PAR"
                Text3 = f"{Defender.NickName} was Paralyzed"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Tackle_Animation,effect

    def Bubble(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        slowdown = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,20,"Water","Bubble")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if slowdown == 3: 
                if Defender.SPEEDCounter > -6: 
                    Defender.SPEEDCounter -= 1
                    Text3 = f"{Defender.NickName}'s Speed was lowered"
                else: Text3 =  f"{Defender.NickName}'s Speed was too low"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Bubble_Animation,Defender.SPEEDCounter,'Speed'

    def BubbleBeam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        slowdown = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,65,"Water","BubbleBeam")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if slowdown == 3: 
                if Defender.SPEEDCounter > -6: 
                    Defender.SPEEDCounter -= 1
                    Text3 = f"{Defender.NickName}'s Speed was lowered"
                else: Text3 =  f"{Defender.NickName}'s Speed was too low"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.BubbleBeam_Animation,Defender.SPEEDCounter,'Speed'

    def Aurora_Beam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Attackdown = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,65,"Ice","Aurora Beam")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Attackdown == 3: 
                if Defender.AtkCounter > -6: 
                    Defender.AtkCounter -= 1
                    Text3 = f"{Defender.NickName}'s Attack was lowered"
                else: Text3 =  f"{Defender.NickName}'s Attack was too low"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Aurora_Beam_Animation,Defender.AtkCounter,'Attack'

    def Psychic(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        slowdown = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,90,"Psychic","Psychic")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if slowdown == 3: 
                if Defender.SPECIALCounter > -6: 
                    Defender.SPECIALCounter -= 1
                    Text3 = f"{Defender.NickName}'s Special was lowered"
                else: Text3 =  f"{Defender.NickName}'s Special was too low"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Psychic_Animation,Defender.SPECIALCounter,'Special'

    def Acid(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        ddown = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,40,"Poison","Acid")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if ddown == 3: 
                if Defender.DEFCounter > -6: 
                    Defender.DEFCounter -= 1
                    Text3 = f"{Defender.NickName}'s Defense was lowered"
                else: Text3 =  f"{Defender.NickName}'s Defense was too low"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Acid_Animation,Defender.DEFCounter,'Defense'

    def Constrict(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        slowdown = random.randint(1,3)
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,10,"Normal","Constrict")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if slowdown == 3: 
                if Defender.SPEEDCounter > -6: 
                    Defender.SPEEDCounter -= 1
                    Text3 = f"{Defender.NickName}'s Speed was lowered"
                else: Text3 =  f"{Defender.NickName}'s Speed was too low"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Wrap_Animation,Defender.SPEEDCounter,'Speed'

    def Leech_Seed(self,Attacker,Defender):
        Text1 = ""
        Time = "Inf"
        Effect = 'Leech Seed'
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit:
            if Two_D_ListCheck(Defender.MyField,'Leech Seed'):
                Text1 = f"{Defender.Name} is already seeded"
            else: Text1 = f"{Defender.Name} was seeded"
            Time = "Inf"
            Effect = 'Leech Seed'
        else:
            Text1 = "It missed"
            Time = ""
            Effect = ''
        return Text1,Effect,Time,Attacker.Leech_Seed_Animation,False
    
    def Thunder_Wave(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit and "Ground" not in Defender.Type:
            if Defender.Status == "OK":Text1 = f"{Defender.NickName} already has a status effect"
            else:
                effect = "PAR"
                Text1 = f"{Defender.NickName} is Paralyzed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Thunder_Wave_Animation

    def Glare(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit:
            if Defender.Status == "OK":Text1 = f"{Defender.NickName} already has a status effect"
            else:
                effect = "PAR"
                Text1 = f"{Defender.NickName} is Paralyzed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Glare_Animation

    def Sing(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,55)
        if Hit and "Ghost" not in Defender.Type:
            if Defender.Status == "OK":
                Text1 = f"{Defender.NickName} fell asleep"
                effect = "SLP"
            else:
                Text1 = f"{Defender.NickName} already has an effect"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Sing_Animation

    def Supersonic(self,Attacker,Defender):
        Text1 = ""
        effect = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,55)
        if Hit and "Ghost" not in Defender.Type:
            if Defender.Status2 == "":
                Text1 = f"{Defender.NickName} became confused"
                effect = "Confused"
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Supersonic_Animation

    def Confuse_Ray(self,Attacker,Defender):
        Text1 = ""
        effect = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.Status2 == "":
                Text1 = f"{Defender.NickName} became confused"
                effect = "Confused"
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Confuse_Ray_Animation

    def Hypnosis(self,Attacker,Defender):
        Text1 = ""
        effect = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,60)
        if Hit:
            if Defender.Status == "OK":
                Text1 = f"{Defender.NickName} fell asleep"
                effect = "SLP"
            else:
                Text1 = f"{Defender.NickName} already has an effect"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Hypnosis_Animation

    def Poison_Powder(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit:
            if Defender.Status == "OK" and "Poison" not in Defender.Type:
                Text1 = f"{Defender.NickName} became poisoned"
                effect = "PSN"
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.PoisonPowder_Animation

    def Toxic(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit:
            if Defender.Status == "OK" and "Poison" not in Defender.Type:
                Text1 = f"{Defender.NickName} became badly poisoned"
                effect = "Bad PSN"
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.PoisonPowder_Animation

    def Poison_Gas(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,55)
        if Hit:
            if Defender.Status == "OK" and "Poison" not in Defender.Type:
                Text1 = f"{Defender.NickName} became poisoned"
                effect = "PSN"
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.PoisonPowder_Animation

    def Stun_Spore(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit:
            if Defender.Status == "OK" and "Ground"  not in Defender.Type:
                Text1 = f"{Defender.NickName} is Paralyzed"
                effect = "PAR"
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Stun_Spore_Animation

    def Sleep_Powder(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit:
            if Defender.Status == "OK":
                Text1 = f"{Defender.NickName} fell asleep"
                effect = "SLP"
            else:
                Text1 = f"{Defender.NickName} already has an effect"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.SleepPowder_Animation

    def Spore(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.Status == "OK":
                Text1 = f"{Defender.NickName} fell asleep"
                effect = "SLP"
            else:
                Text1 = f"{Defender.NickName} already has an effect"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.SleepPowder_Animation

    def Lovely_Kiss(self,Attacker,Defender):
        Text1 = ""
        effect = 'OK'
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit:
            if Defender.Status == "OK":
                Text1 = f"{Defender.NickName} fell asleep"
                effect = "SLP"
            else:
                Text1 = f"{Defender.NickName} already has an effect"
        else:
            Text1 = "It missed"
        return Text1,effect,Attacker.Lovely_Kiss_Animation

    def Fury_Attack(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,15,"Normal","Fury Attack")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Horn_Attack_Animation

    def Pin_Missile(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,14,"Bug","Pin Missile")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Pin_Missile_Animation

    def DoubleSlap(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,15,"Normal","DoubleSlap")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Tackle_Animation

    def Fury_Swipes(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,80)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,18,"Normal","Fury Swipes")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Scratch_Animation

    def Barrage(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,15,"Normal","Barrage")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Barrage_Animation

    def Comet_Punch(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,18,"Normal","Comet Punch")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Tackle_Animation

    def Spike_Cannon(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,20,"Normal","Spike Cannon")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = random.randint(2,5)
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Roar_Animation

    def Double_Kick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,30,"Fighting","Double Kick")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = 2
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Tackle_Animation

    def Bonemerang(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ''
        Hits = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Ground","Bonemerang")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            Hits = 2
            Text3 = f'{Attacker.NickName} hit {Hits} times'
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage*Hits,Text1,Text2,Text3,Attacker.Bonemerang_Animation

    def Bide(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'Bide':
            return 0,f"{Attacker.NickName} is storing energy",'',1,random.randint(2,3),Attacker.Bide_Animation,"Bide"
        elif Attacker.IdleTurns > 0 and Attacker.IdleMove == 'Bide':
            return 0,f"{Attacker.NickName} is storing energy",'',1,Attacker.IdleTurns - 1,Attacker.Bide_Animation,"Bide"
        elif Attacker.IdleTurns == 0 and Attacker.IdleMove == 'Bide':
            if Attacker.BideDamage > 0: 
                Attacker.BideDamage *= 2
                Text1 = f"{Attacker.NickName} unleashed the energy"
            else:
                Attacker.BideDamage = 0
                Text1 = "It Missed"
                Text2 = ''
            return Attacker.BideDamage,Text1,Text2,1,0,Attacker.Bide_Animation,""

    def Dig(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'Dig':
            return 0,f"{Attacker.NickName} is burrowing",'',0,1,Attacker.Dig_Animation,"Dig"
        elif Attacker.IdleTurns == 1 and Attacker.IdleMove == 'Dig':
            Hit = self.Accuracy_Calculation(Attacker,Defender,100)
            if Hit: 
                Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,100,"Ground","Dig")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,0,Attacker.Dig_Animation,""
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.Dig_Animation,""

    def Fly(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'Fly':
            return 0,f"{Attacker.NickName} is flying into the sky",'',0,1,Attacker.Fly_Animation,"Fly"
        elif Attacker.IdleTurns == 1 and Attacker.IdleMove == 'Fly':
            Hit = self.Accuracy_Calculation(Attacker,Defender,95)
            if Hit: 
                Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,70,"Flying","Fly")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,0,Attacker.Fly_Animation,""
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.Fly_Animation,""

    def Sky_Attack(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'Sky Attack':
            return 0,f"{Attacker.NickName} is glowing",'',0,1,Attacker.SkyAttackCharging_Animation,"Sky Attack"
        elif Attacker.IdleTurns == 1 and Attacker.IdleMove == 'Sky Attack':
            Hit = self.Accuracy_Calculation(Attacker,Defender,90)
            if Hit: 
                Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,140,"Flying","Fly")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,0,Attacker.Tackle_Animation,""
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.Tackle_Animation,""

    def Hyper_Beam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 1 and Attacker.IdleMove == 'Hyper Beam':
            return 0,f"{Attacker.NickName} is recharging",'',0,0,Attacker.Tackle_Animation,""
        elif Attacker.IdleTurns == 0 and Attacker.IdleMove == '':
            Hit = self.Accuracy_Calculation(Attacker,Defender,90)
            if Hit: 
                Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,150,"Normal","Hyper Beam")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,1,Attacker.Hyper_Beam_Animation,"Hyper Beam"
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.Hyper_Beam_Animation,""

    def SolarBeam(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'SolarBeam':
            return 0,f"{Attacker.NickName} gathered energy ",'',0,1,Attacker.SolarBeamCharging_Animation,"SolarBeam"
        elif Attacker.IdleTurns == 1 and Attacker.IdleMove == 'SolarBeam':
            Hit = self.Accuracy_Calculation(Attacker,Defender,100)
            if Hit: 
                Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,120,"Grass","SolarBeam")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,0,Attacker.SolarBeam_Animation,""
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.SolarBeam_Animation,""

    def Razor_Wind(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'Razor Wind':
            return 0,f"{Attacker.NickName} made a whirlwind ",'',0,1,Attacker.Gust_Animation,"Razor Wind"
        elif Attacker.IdleTurns == 1 and Attacker.IdleMove == 'Razor Wind':
            Hit = self.Accuracy_Calculation(Attacker,Defender,75)
            if Hit: 
                Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Normal","Razor Wind")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,0,Attacker.Gust_Animation,""
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.Gust_Animation,""

    def Skull_Bash(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Damage = 0
        if Attacker.IdleTurns == 0 and Attacker.IdleMove != 'Skull Bash':
            return 0,f"{Attacker.NickName} lowered their head ",'',0,1,Attacker.Harden_Animation,"Skull Bash"
        elif Attacker.IdleTurns == 1 and Attacker.IdleMove == 'Skull Bash':
            Hit = self.Accuracy_Calculation(Attacker,Defender,100)
            if Hit: 
                Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,100,"Normal","Skull Bash")
                if Effect == 2: Text1 = "It was super Effective"
                elif Effect == 1: Text1 = ''
                elif Effect == 0:
                    Text2 = ''
                    Text1 = "It had no effect!"
                elif Effect < 1: Text1 = "It wasn't very effective"
                if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
                if not Crit or Effect == 0 : Text2 = ''
                return Damage,Text1,Text2,1,0,Attacker.Tackle_Animation,""
            else:
                Damage = 0 
                Text1 = f"{Attacker.NickName} missed"
                Text2 = ''
            return Damage,Text1,Text2,1,0,Attacker.Tackle_Animation,""

    def Thrash(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        IdleTurns = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,90,"Normal","Thrash")
            Text3 = f"{Attacker.NickName} is going on a rampage "
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Attacker.IdleTurns == 0:IdleTurns = random.randint(4,5)
            if Attacker.IdleTurns > 0: IdleTurns = Attacker.IdleTurns - 1
        else:
            IdleTurns = 0
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage,Text1,Text2,Text3,IdleTurns,Attacker.Tackle_Animation,"Thrash"

    def Petal_Dance(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        IdleTurns = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,70,"Grass","Petal Dance")
            Text3 = f"{Attacker.NickName} is going on a rampage "
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Attacker.IdleTurns == 0:IdleTurns = random.randint(4,5)
            if Attacker.IdleTurns > 0: IdleTurns = Attacker.IdleTurns - 1
        else:
            IdleTurns = 0
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
            Text3 = ""
        return Damage,Text1,Text2,Text3,IdleTurns,Attacker.Petal_Dance_Animation,"Petal Dance"

    def Wrap(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        TrappedTurns = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,15,"Normal","Wrap")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Defender.TrappedTurns <= 0: 
                TrappedTurns = random.randint(3,6)
                Text1 = f'{Attacker.NickName} wraps around {Defender.NickName}'
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,0,TrappedTurns,Attacker.Wrap_Animation

    def Bind(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        TrappedTurns = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,15,"Normal","Bind")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Defender.TrappedTurns <= 0: 
                TrappedTurns = random.randint(3,6)
                Text1 = f'{Attacker.NickName} binds around {Defender.NickName}'
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,0,TrappedTurns,Attacker.Wrap_Animation

    def Clamp(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        TrappedTurns = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,35,"Water","Bind")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Defender.TrappedTurns <= 0: 
                TrappedTurns = random.randint(3,6)
                Text1 = f'{Attacker.NickName} binds around {Defender.NickName}'
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,0,TrappedTurns,Attacker.Clamp_Animation

    def Fire_Spin(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        TrappedTurns = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,75)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,15,"Fire","Fire Spin")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Defender.TrappedTurns <= 0: 
                TrappedTurns = random.randint(3,6)
                Text1 = f'{Attacker.NickName} binds around {Defender.NickName}'
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,0,TrappedTurns,Attacker.Fire_Spin_Animation

    def Leech_Life(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,20,"Bug","Leech Life")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Text2 != '': Text3 = f"{Defender.NickName} HP was Drained"
            if Text2 == "": Text2 = f"{Defender.NickName} HP was Drained"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Leech_Life_Animation

    def Absorb(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,20,"Grass","Absorb")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Text2 != '': Text3 = f"{Defender.NickName} HP was Drained"
            if Text2 == "": Text2 = f"{Defender.NickName} HP was Drained"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Absorb_Animation

    def Mega_Drain(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,40,"Grass","Mega Drain")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Text2 != '': Text3 = f"{Defender.NickName} HP was Drained"
            if Text2 == "": Text2 = f"{Defender.NickName} HP was Drained"
        else:
            Damage = 0
            Text1 = "It Missed"
        return Damage,Text1,Text2,Text3,Attacker.Mega_Drain_Animation

    def Dream_Eater(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Text3 = ""
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit and Defender.Status == "SLP":
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,100,"Psychic","Dream Eater")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if Text2 != '': Text3 = f"{Defender.NickName} dreams were eatened"
            if Text2 == "": Text2 = f"{Defender.NickName} dreams were eatened"
        elif not Hit:
            Damage = 0
            Text1 = "It Missed"
        else:
            Damage = 0
            Text1 = "It failed"
        return Damage,Text1,Text2,Text3,Attacker.Dream_Eater_Animation

    def Disable(self,Attacker,Defender):
        Text1 = ""
        Move = ''
        Timer = 0
        Hit = self.Accuracy_Calculation(Attacker,Defender,55)
        if Hit: 
            for i in range(4):
                if Defender.Moves[i] != "-" and Defender.Movespp[i] > 0:
                    Move = Defender.Moves[i]
            if Move == "" or Defender.DisabledMove != "":
                Text1 = "Move Failed"
                Move = ''
            else:
                Text1 = f"{Move} is Disabled"
                Timer = random.randint(2,8)
        else:
            Text1 = "It Missed"
        return Text1,Move,Timer,Attacker.Disable_Animation

    def Focus_Energy(self,Attacker):
        Text1 = f"{Attacker.NickName} is getting pumped up"
        return Text1,True,Attacker.Focus_Energy_Animation

    def Light_Screen(self,Attacker):
        if not Attacker.LightScreenUp:Text1 = f"{Attacker.NickName} put up a screen"
        else:Text1 = "Move Failed"
        return Text1,True,Attacker.Teleport_Animation

    def Reflect(self,Attacker):
        if not Attacker.ReflectUp:Text1 = f"{Attacker.NickName} put up a screen"
        else:Text1 = "Move Failed"
        return Text1,True,Attacker.Teleport_Animation

    def Hyper_Fang(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,80,"Normal","Hyper Fang")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) >= 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Hyper_Fang_Animation

    def Bite(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,60,"Normal","Bite")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,10) == 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Hyper_Fang_Animation

    def Low_Kick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,90)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Fighting","Low Kick")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,3) == 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Tackle_Animation

    def Rolling_Kick(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,60,"Fighting","Rolling Kick")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,3) == 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Tackle_Animation

    def Bone_Club(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65,"Ground","Bone Club")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,3) == 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Bone_Club_Animation

    def Stomp(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        F= False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,65,"Normal","Stomp")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
            if random.randint(1,3) == 1:
                F = True
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,F,Attacker.Tackle_Animation

    def Whirlwind(self,Attacker,Defender):
        Text1 = ""
        ran = False
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit:
            if Defender.Trainer == "Wild":
                Text1 = f"{Attacker.NickName} ran away"
                ran = True
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,ran,Attacker.Gust_Animation

    def Teleport(self,Attacker,Defender):
        Text1 = ""
        ran = False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.Trainer == "Wild" or Attacker.Trainer == "Wild":
                Text1 = f"{Attacker.NickName} ran away"
                ran = True
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,ran,Attacker.Teleport_Animation

    def Roar(self,Attacker,Defender):
        Text1 = ""
        ran = False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit:
            if Defender.Trainer == "Wild" or Attacker.Trainer == "Wild":
                Text1 = f"{Attacker.NickName} ran away"
                ran = True
            else:
                Text1 = "Move Failed"
        else:
            Text1 = "It missed"
        return Text1,ran,Attacker.Roar_Animation

    def Karate_Chop(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,50,"Normal","Karate Chop")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Scratch_Animation

    def Slash(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,70,"Normal","Slash")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Scratch_Animation

    def Razor_Leaf(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,95)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,55,"Grass","Razor Leaf")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Razor_Leaf_Animation

    def Crabhammer(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Hit = self.Accuracy_Calculation(Attacker,Defender,85)
        if Hit: 
            Damage,Crit,Effect = self.Special_Damage_Calculation(Attacker,Defender,90,"Water","Crabhammer")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        return Damage,Text1,Text2,Attacker.Crabhammer_Animation

    def Rest(self,Attacker):
        NewHP = Attacker.MAXHP
        Text1 = f"{Attacker.NickName} fell asleep"
        effect = "SLP"
        return Text1,effect,Attacker.MAXHP,Attacker.Teleport_Animation

    def Selfdestruct(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Faint = False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,130,"Normal","Selfdestruct")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        Faint = True
        return Damage,Text1,Text2,Faint,Attacker.Selfdestruct_Animation

    def Explosion(self,Attacker,Defender):
        Text1 = ""
        Text2 = ''
        Faint = False
        Hit = self.Accuracy_Calculation(Attacker,Defender,100)
        if Hit: 
            Damage,Crit,Effect = self.Physical_Damage_Calculation(Attacker,Defender,170,"Normal","Explosion")
            if Effect == 2: Text1 = "It was super Effective"
            elif Effect == 1: Text1 = ''
            elif Effect == 0:
                Text2 = ''
                Text1 = "It had no effect!"
            elif Effect < 1: Text1 = "It wasn't very effective"
            if Crit and Effect > 0: Text2 = "It was a critical Hit!!"
            if not Crit or Effect == 0 : Text2 = ''
        else:
            Damage = 0
            Text1 = "It Missed"
            Text2 = ''
        Faint = True
        return Damage,Text1,Text2,Faint,Attacker.Selfdestruct_Animation

    def Recover(self,Attacker):
        Text1 = ""
        Text2 = ''
        HP = 0
        if Attacker.HP < Attacker.MAXHP: 
            HP = Attacker.MAXHP//2
            Text1 = f"{Attacker.NickName} recovered"
        else:
            HP = 0
            Text1 = "Move failed"
        return HP,Text1,Attacker.Teleport_Animation

    def Softboiled(self,Attacker):
        Text1 = ""
        HP = 0
        if Attacker.HP < Attacker.MAXHP: 
            HP = Attacker.MAXHP//2
            Text1 = f"{Attacker.NickName} recovered"
        else:
            HP = 0
            Text1 = "Move failed"
        return HP,Text1,Attacker.Defense_Curl_Animation

    def Get_NormalDamagingAttack_by_Name(self,Attack:str,Attacker,Defender):
        if Attack =="Tackle":
            D,Text1,Text2,Battle_Animation = self.Tackle(Attacker,Defender)
        elif Attack == "Scratch":
            D,Text1,Text2,Battle_Animation = self.Scratch(Attacker,Defender)
        elif Attack == "Gust":
            D,Text1,Text2,Battle_Animation = self.Gust(Attacker,Defender)
        elif Attack == "Peck":
            D,Text1,Text2,Battle_Animation = self.Peck(Attacker,Defender)
        elif Attack == "Horn Attack":
            D,Text1,Text2,Battle_Animation = self.Horn_Attack(Attacker,Defender)
        elif Attack == "Pound":
            D,Text1,Text2,Battle_Animation = self.Pound(Attacker,Defender)
        elif Attack == "Vine Whip":
            D,Text1,Text2,Battle_Animation = self.Vine_Whip(Attacker,Defender)
        elif Attack == "Water Gun":
            D,Text1,Text2,Battle_Animation = self.Water_Gun(Attacker,Defender)
        elif Attack == "Rock Throw":
            D,Text1,Text2,Battle_Animation = self.Rock_Throw(Attacker,Defender)
        elif Attack == "Mega Punch":
            D,Text1,Text2,Battle_Animation = self.Mega_Punch(Attacker,Defender)
        elif Attack == "Karate Chop":
            D,Text1,Text2,Battle_Animation = self.Karate_Chop(Attacker,Defender)
        elif Attack == "Seismic Toss":
            D,Text1,Text2,Battle_Animation = self.Seismic_Toss(Attacker,Defender)
        elif Attack == "Splash":
            D,Text1,Text2,Battle_Animation = self.Splash(Attacker,Defender) 
        elif Attack == "Cut":
            D,Text1,Text2,Battle_Animation = self.Cut(Attacker,Defender) 
        elif Attack == "SonicBoom":D,Text1,Text2,Battle_Animation = self.SonicBoom(Attacker,Defender) 
        elif Attack == "Slash":D,Text1,Text2,Battle_Animation = self.Slash(Attacker,Defender) 
        elif Attack == "Pay Day":D,Text1,Text2,Battle_Animation = self.Pay_Day(Attacker,Defender)
        elif Attack == "Headbutt":D,Text1,Text2,Battle_Animation = self.Headbutt(Attacker,Defender)
        elif Attack == "Rage":D,Text1,Text2,Battle_Animation = self.Rage(Attacker,Defender)
        elif Attack == "Swift":D,Text1,Text2,Battle_Animation = self.Swift(Attacker,Defender)
        elif Attack == "ViceGrip":D,Text1,Text2,Battle_Animation = self.ViceGrip(Attacker,Defender)
        elif Attack == "Dragon Rage":D,Text1,Text2,Battle_Animation = self.Dragon_Rage(Attacker,Defender)
        elif Attack == "Horn Drill":D,Text1,Text2,Battle_Animation = self.Horn_Drill(Attacker,Defender)
        elif Attack == "Egg Bomb":D,Text1,Text2,Battle_Animation = self.Egg_Bomb(Attacker,Defender)
        elif Attack == "Mega Kick":D,Text1,Text2,Battle_Animation = self.Mega_Kick(Attacker,Defender)
        elif Attack == "Rock Slide":D,Text1,Text2,Battle_Animation = self.Rock_Slide(Attacker,Defender)
        elif Attack == "Tri Attack":D,Text1,Text2,Battle_Animation = self.Tri_Attack(Attacker,Defender)
        elif Attack == "Razor Leaf":D,Text1,Text2,Battle_Animation = self.Razor_Leaf(Attacker,Defender)
        elif Attack == "Night Shade":D,Text1,Text2,Battle_Animation = self.Night_Shade(Attacker,Defender)
        elif Attack == "Hydro Pump":D,Text1,Text2,Battle_Animation = self.Hydro_Pump(Attacker,Defender)
        elif Attack == "Drill Peck":D,Text1,Text2,Battle_Animation = self.Drill_Peck(Attacker,Defender)
        elif Attack == "Surf":D,Text1,Text2,Battle_Animation = self.Surf(Attacker,Defender)
        elif Attack == "Earthquake":D,Text1,Text2,Battle_Animation = self.Earthquake(Attacker,Defender)
        elif Attack == "Wing Attack":D,Text1,Text2,Battle_Animation = self.Wing_Attack(Attacker,Defender)
        elif Attack == "Slam":D,Text1,Text2,Battle_Animation = self.Slam(Attacker,Defender)
        elif Attack == "Guillotine":D,Text1,Text2,Battle_Animation = self.Guillotine(Attacker,Defender)
        elif Attack == "Strength":D,Text1,Text2,Battle_Animation = self.Strength(Attacker,Defender)
        elif Attack == "PsyWave":D,Text1,Text2,Battle_Animation = self.PsyWave(Attacker,Defender)
        elif Attack == "Fissure":D,Text1,Text2,Battle_Animation = self.Fissure(Attacker,Defender)
        elif Attack == "Super Fang":D,Text1,Text2,Battle_Animation = self.Super_Fang(Attacker,Defender)
        elif Attack == "Dizzy Punch":D,Text1,Text2,Battle_Animation = self.Dizzy_Punch(Attacker,Defender)
        elif Attack == "Waterfall":D,Text1,Text2,Battle_Animation = self.Waterfall(Attacker,Defender)
        elif Attack == "Crabhammer":D,Text1,Text2,Battle_Animation = self.Crabhammer(Attacker,Defender)
        return D,Text1,Text2,Battle_Animation

    def Get_RecoilAttack_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Struggle":D,Text1,Text2,Text3,R,Battle_Animation = self.Struggle(Attacker,Defender) 
        elif Attack == "Take Down":D,Text1,Text2,Text3,R,Battle_Animation = self.Take_Down(Attacker,Defender) 
        elif Attack == "Submission":D,Text1,Text2,Text3,R,Battle_Animation = self.Submission(Attacker,Defender)
        elif Attack == "Double Edge":D,Text1,Text2,Text3,R,Battle_Animation = self.Double_Edge(Attacker,Defender)
        elif Attack == "Jump Kick":D,Text1,Text2,Text3,R,Battle_Animation = self.Jump_Kick(Attacker,Defender)
        elif Attack == "Hi Jump Kick":D,Text1,Text2,Text3,R,Battle_Animation = self.Hi_Jump_Kick(Attacker,Defender)
        return D,Text1,Text2,Text3,R,Battle_Animation 

    def Get_EnemyStatChanging_Move_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Tail Whip":
            C,Text1,Text2 ,Battle_Animation = self.Tail_Whip(Attacker,Defender)
        elif Attack == "Growl":
            C,Text1,Text2,Battle_Animation = self.Growl(Attacker,Defender)
        elif Attack == "Sand Attack":
            C,Text1,Text2,Battle_Animation = self.Sand_Attack(Attacker,Defender)
        elif Attack == "Leer":
            C,Text1,Text2,Battle_Animation = self.Leer(Attacker,Defender)
        elif Attack == "String Shot":
            C,Text1,Text2,Battle_Animation = self.String_Shot(Attacker,Defender)
        elif Attack == "Screech":C,Text1,Text2,Battle_Animation = self.Screech(Attacker,Defender)
        elif Attack == "Flash":C,Text1,Text2,Battle_Animation = self.Flash(Attacker,Defender)
        elif Attack == "SmokeScreen":C,Text1,Text2,Battle_Animation = self.SmokeScreen(Attacker,Defender)
        if Defender.SubstituteOn:Text1 = "It had no effect on the substitute"
        if Defender.StatProtect:Text1 = ""
        return C,Text1,Text2,Battle_Animation 

    def Get_SelfStatChanging_Move_by_Name(self,Attack:str,Attacker):
        if Attack == "Harden":
            C,Text1,Text2,Battle_Animation = self.Harden(Attacker)
        elif Attack == "Defense Curl":
            C,Text1,Text2,Battle_Animation = self.Defense_Curl(Attacker)
        elif Attack == "Growth":
            C,Text1,Text2,Battle_Animation = self.Growth(Attacker)
        elif Attack == "Withdraw":C,Text1,Text2,Battle_Animation = self.Withdraw(Attacker)
        elif Attack == "Barrier":C,Text1,Text2,Battle_Animation = self.Barrier(Attacker)
        elif Attack == "Minimize":C,Text1,Text2,Battle_Animation = self.Minimize(Attacker)
        elif Attack == "Swords Dance":C,Text1,Text2,Battle_Animation = self.Swords_Dance(Attacker)
        elif Attack == "Sharpen":C,Text1,Text2,Battle_Animation = self.Sharpen(Attacker)
        elif Attack == "Agility":C,Text1,Text2,Battle_Animation = self.Agility(Attacker)
        elif Attack == "Double Team":C,Text1,Text2,Battle_Animation = self.Double_Team(Attacker)
        elif Attack == "Amnesia":C,Text1,Text2,Battle_Animation = self.Amnesia(Attacker)
        elif Attack == "Meditate":C,Text1,Text2,Battle_Animation = self.Meditate(Attacker)
        elif Attack == "Acid Armor":C,Text1,Text2,Battle_Animation = self.Acid_Armor(Attacker)
        return C,Text1,Text2,Battle_Animation
        
    def Get_EnemyStatDamagingMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Bubble":Damage,Text1,Text2,Text3,Battle_Animation,S,Stat = self.Bubble(Attacker,Defender)
        if Attack == "BubbleBeam":Damage,Text1,Text2,Text3,Battle_Animation,S,Stat = self.BubbleBeam(Attacker,Defender)
        if Attack == "Acid":Damage,Text1,Text2,Text3,Battle_Animation,S,Stat = self.Acid(Attacker,Defender)
        if Attack == "Constrict":Damage,Text1,Text2,Text3,Battle_Animation,S,Stat = self.Constrict(Attacker,Defender)
        if Attack == "Psychic":Damage,Text1,Text2,Text3,Battle_Animation,S,Stat = self.Psychic(Attacker,Defender)
        if Attack == "Aurora Beam":Damage,Text1,Text2,Text3,Battle_Animation,S,Stat = self.Aurora_Beam(Attacker,Defender)
        if Defender.SubstituteOn:Text3 = ""
        return Damage,Text1,Text2,Text3,Battle_Animation,S,Stat

    def Get_EnemyStatusDamagingMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Ember": Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Ember(Attacker,Defender)
        elif Attack == "Confusion":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Confusion(Attacker,Defender)
        elif Attack == "Poison Sting":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Poison_Sting(Attacker,Defender)
        elif Attack == "ThunderShock":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.ThunderShock(Attacker,Defender)
        elif Attack == "Smog":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Smog(Attacker,Defender)
        elif Attack == "Body Slam":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Body_Slam(Attacker,Defender)
        elif Attack == "Thunderbolt":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Thunderbolt(Attacker,Defender)
        elif Attack == "Twineedle":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Twineedle(Attacker,Defender)
        elif Attack == "Lick":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Lick(Attacker,Defender)
        elif Attack == "Psybeam":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Psybeam(Attacker,Defender)
        elif Attack == "Ice Beam":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Ice_Beam(Attacker,Defender)
        elif Attack == "Sludge":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Sludge(Attacker,Defender)
        elif Attack == "Fire Punch":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Fire_Punch(Attacker,Defender)
        elif Attack == "Blizzard":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Blizzard(Attacker,Defender)
        elif Attack == "Flamethrower":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Flamethrower(Attacker,Defender)
        elif Attack == "Fire Blast":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Fire_Blast(Attacker,Defender)
        elif Attack == "Thunder":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Thunder(Attacker,Defender)
        elif Attack == "Ice Punch":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Ice_Punch(Attacker,Defender)
        elif Attack == "Thunder Punch":Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus = self.Thunder_Punch(Attacker,Defender)
        if Defender.SubstituteOn:Text3 = ""
        return Damage,Text1,Text2,Text3,Battle_Animation,EnemyStatus

    def Get_EnemyStatusMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Thunder Wave": Text1,EnemyStatus,Battle_Animation = self.Thunder_Wave(Attacker,Defender)
        elif Attack == "Sing": Text1,EnemyStatus,Battle_Animation = self.Sing(Attacker,Defender)
        elif Attack == "Supersonic": Text1,EnemyStatus,Battle_Animation = self.Supersonic(Attacker,Defender)
        elif Attack == "Poison Powder": Text1,EnemyStatus,Battle_Animation = self.Poison_Powder(Attacker,Defender)
        elif Attack == "Stun Spore": Text1,EnemyStatus,Battle_Animation = self.Stun_Spore(Attacker,Defender)
        elif Attack == "Hypnosis": Text1,EnemyStatus,Battle_Animation = self.Hypnosis(Attacker,Defender)
        elif Attack == "Sleep Powder": Text1,EnemyStatus,Battle_Animation = self.Sleep_Powder(Attacker,Defender)
        elif Attack == "Lovely Kiss":Text1,EnemyStatus,Battle_Animation = self.Lovely_Kiss(Attacker,Defender)
        elif Attack == "Confuse Ray":Text1,EnemyStatus,Battle_Animation = self.Confuse_Ray(Attacker,Defender)
        elif Attack == "Poison Gas": Text1,EnemyStatus,Battle_Animation = self.Poison_Gas(Attacker,Defender)
        elif Attack == "Glare":Text1,EnemyStatus,Battle_Animation = self.Glare(Attacker,Defender)
        elif Attack == "Toxic":Text1,EnemyStatus,Battle_Animation = self.Toxic(Attacker,Defender)
        elif Attack == "Spore":Text1,EnemyStatus,Battle_Animation = self.Spore(Attacker,Defender)
        if Defender.SubstituteOn: Text1 = "It had no effect on the substitute"
        return Text1,EnemyStatus,Battle_Animation

    def Get_PriorityMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Quick Attack": Damage,Text1,Text2,P,Battle_Animation = self.Quick_Attack(Attacker,Defender)
        elif Attack == "Counter":Damage,Text1,Text2,P,Battle_Animation = self.Counter(Attacker,Defender)
        return Damage,Text1,Text2,P,Battle_Animation

    def Get_FieldAffectingMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Leech Seed":
            Text1,Effect,EffectTerm,Battle_Animation,FieldTarget = self.Leech_Seed(Attacker,Defender)
        return Text1,Effect,EffectTerm,Battle_Animation,FieldTarget

    def Get_MultiTurnMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Bide":
            Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Bide(Attacker,Defender)
        elif Attack == "Dig":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Dig(Attacker,Defender)
        elif Attack == "Hyper Beam":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Hyper_Beam(Attacker,Defender)
        elif Attack == "Razor Wind":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Razor_Wind(Attacker,Defender)
        elif Attack == "Fly":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Fly(Attacker,Defender)
        elif Attack == "Skull Bash":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Skull_Bash(Attacker,Defender)
        elif Attack == "SolarBeam":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.SolarBeam(Attacker,Defender)
        elif Attack == "Sky Attack":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move = self.Sky_Attack(Attacker,Defender)
        return Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation,Move

    def Get_RampageMoves_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Thrash":Damage,Text1,Text2,Text3,IdleTurns,BattleAnimation,Move = self.Thrash(Attacker,Defender)
        elif Attack == "Petal Dance":Damage,Text1,Text2,Text3,IdleTurns,BattleAnimation,Move = self.Petal_Dance(Attacker,Defender)
        return Damage,Text1,Text2,Text3,IdleTurns,BattleAnimation,Move

    def Get_MultiTrappingMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Wrap":
            Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation = self.Wrap(Attacker,Defender)
        if Attack == "Bind":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation = self.Bind(Attacker,Defender)
        if Attack == "Clamp":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation = self.Clamp(Attacker,Defender)
        if Attack == "Fire Spin":Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation = self.Fire_Spin(Attacker,Defender)
        if Defender.SubstituteOn:
            IdleTurns = 0
            Text1 = f'It had no effect because of the Substitute'
        return Damage,Text1,Text2,Priority,IdleTurns,BattleAnimation

    def Get_MultiHitMove_by_Name(self,Attack:str,Attacker,Defender):
        if Attack == "Fury Attack": Damage,Text1,Text2,Text3,BattleAnimation = self.Fury_Attack(Attacker,Defender)
        elif Attack == "DoubleSlap":Damage,Text1,Text2,Text3,BattleAnimation = self.DoubleSlap(Attacker,Defender)
        elif Attack == "Fury Swipes":Damage,Text1,Text2,Text3,BattleAnimation = self.Fury_Swipes(Attacker,Defender)
        elif Attack == "Barrage":Damage,Text1,Text2,Text3,BattleAnimation = self.Barrage(Attacker,Defender)
        elif Attack == "Comet Punch":Damage,Text1,Text2,Text3,BattleAnimation = self.Comet_Punch(Attacker,Defender)
        elif Attack == "Double Kick":Damage,Text1,Text2,Text3,BattleAnimation = self.Double_Kick(Attacker,Defender)
        elif Attack == "Pin Missile":Damage,Text1,Text2,Text3,BattleAnimation = self.Pin_Missile(Attacker,Defender)
        elif Attack == "Spike Cannon":Damage,Text1,Text2,Text3,BattleAnimation = self.Spike_Cannon(Attacker,Defender)
        elif Attack == "Bonemerang":Damage,Text1,Text2,Text3,BattleAnimation = self.Bonemerang(Attacker,Defender)
        return Damage,Text1,Text2,Text3,BattleAnimation

    def Get_DrainingMoves_by_Name(self,Attack,Attacker,Defender):
        if Attack == "Leech Life":Damage,Text1,Text2,Text3,Battle_Animation = self.Leech_Life(Attacker,Defender)
        elif Attack == "Absorb":Damage,Text1,Text2,Text3,Battle_Animation = self.Absorb(Attacker,Defender)
        elif Attack == "Dream Eater":Damage,Text1,Text2,Text3,Battle_Animation = self.Dream_Eater(Attacker,Defender)
        elif Attack == "Mega Drain":Damage,Text1,Text2,Text3,Battle_Animation = self.Mega_Drain(Attacker,Defender)
        return Damage,Text1,Text2,Text3,Battle_Animation

    def Get_Disable(self,Attacker,Defender):
        Text1,Move,Timer,BA = self.Disable(Attacker,Defender)
        return Text1,Move,Timer,BA

    def Get_Rest(self,Attacker,Defender):
        Text1,effect,NHP,BA = self.Rest(Attacker)
        return Text1,effect,NHP,BA

    def Get_FlinchingMoves(self,Attack,Attacker,Defender):
        if Attack == "Hyper Fang":Damage,Text1,Text2,Flinch,BA = self.Hyper_Fang(Attacker,Defender)
        if Attack == "Bite":Damage,Text1,Text2,Flinch,BA = self.Bite(Attacker,Defender)
        if Attack == "Low Kick":Damage,Text1,Text2,Flinch,BA = self.Low_Kick(Attacker,Defender)
        if Attack == "Bone Club":Damage,Text1,Text2,Flinch,BA = self.Bone_Club(Attacker,Defender)
        if Attack == "Stomp":Damage,Text1,Text2,Flinch,BA = self.Stomp(Attacker,Defender)
        if Attack == "Headbutt":Damage,Text1,Text2,Flinch,BA = self.Headbutt(Attacker,Defender)
        if Attack == "Rolling Kick":Damage,Text1,Text2,Flinch,BA = self.Rolling_Kick(Attacker,Defender)
        if Defender.SubstituteOn: Flinch = False
        return Damage,Text1,Text2,Flinch,BA

    def Get_SelfFaintingMoves(self,Attack,Attacker,Defender):
        if Attack == "Selfdestruct": Damage,Text1,Text2,Died,Battle_Animation = self.Selfdestruct(Attacker,Defender)
        elif Attack == "Explosion": Damage,Text1,Text2,Died,Battle_Animation = self.Explosion(Attacker,Defender)
        return Damage,Text1,Text2,Died,Battle_Animation

    def Get_WildMoves(self,Attack,Attacker,Defender):
        if Attack == "Whirlwind": Text1,ran,BA = self.Whirlwind(Attacker,Defender)
        elif Attack == "Teleport": Text1,ran,BA = self.Teleport(Attacker,Defender)
        elif Attack == "Roar": Text1,ran,BA = self.Roar(Attacker,Defender)
        return Text1,ran,BA

    def Get_HealingMoves(self,Attack,Attacker):
        if Attack == "Recover":GainHP,Text1,BA = self.Recover(Attacker)
        elif Attack == "Softboiled":GainHP,Text1,BA = self.Softboiled(Attacker)
        return GainHP,Text1,BA

class Pokemon():
    def __init__(self,Name:str,Level:int,Moves:list[str],Owner:str,NickName:str,Exp:int = 0):
        self.Trainer = Owner
        self.Running = False
        self.NickName = NickName
        self.Name = Name
        if Name == "Mr.Mime":Name = "Mr. Mime"
        self.Name = Name
        self.Faint = False
        self.LightScreenUp = False
        self.SubstituteOn = False
        self.SubstituteHP = 0
        self.LightScreenDamage = 0
        self.ReflectUp = False
        self.ToxicTurn = 0
        self.ReflectDamage = 0
        self.RecoilDamage = 0
        self.StatProtect = False
        self.LastmoveUsed = ""
        self.RageOn = False
        self.Status = "OK"
        self.Status2 = ""
        self.CounterDamage = 0
        self.ConfusionTimeLimit = 0
        self.FocusEnergy = False
        self.Back_Img = pygame.image.load(Pokes_img[self.Name][0]).convert_alpha()
        self.Front_Img = pygame.image.load(Pokes_img[self.Name][1]).convert_alpha()
        self.Back_Img = pygame.transform.rotozoom(self.Back_Img,360,2)
        self.EnemyBattlerect = self.Front_Img.get_rect(topleft = (570,50))
        self.PlayerBattlerect = self.Back_Img.get_rect(topleft = (70, 240))
        self.HallofFameBackrect = self.Back_Img.get_rect(topleft = (800, 350))
        self.HallofFameFrontrect = self.Front_Img.get_rect(topright = (0,100))
        self.BattleAnimation = None
        self.Type = Pokemon_Types[Name]
        self.Level = Level
        self.Level_up = False
        self.CatchRate = Pokemon_CatchRates[Name]
        self.NextStage = Pokemon_Evolutions[Name]
        self.Died = False
        self.In_Battle = False
        self.Particaption = False
        self.MoveType = ''
        self.EXPGroup = Pokemon_EXPGroups[Name]
        self.Moves = Moves
        if len(self.Moves) < 4:
            for i in range(4 - len(Moves)):
                self.Moves.append("-")
        self.Move1pp = Pokemon_Move_PP[Moves[0]]
        self.Move1Type = Pokemon_Move_Type[Moves[0]]
        self.MaxMove1pp = self.Move1pp
        self.Move2pp = Pokemon_Move_PP[Moves[1]]
        self.Move2Type = Pokemon_Move_Type[Moves[1]]
        self.MaxMove2pp = self.Move2pp
        self.Move3pp = Pokemon_Move_PP[Moves[2]]
        self.Move3Type = Pokemon_Move_Type[Moves[2]]
        self.MaxMove3pp = self.Move3pp
        self.Move4pp = Pokemon_Move_PP[Moves[3]]
        self.Move4Type = Pokemon_Move_Type[Moves[3]]
        self.MaxMove4pp = self.Move4pp
        self.Movespp = [self.Move1pp,self.Move2pp,self.Move3pp,self.Move4pp]
        self.BaseHp = Pokemon_BaseStats[self.Name][0]
        self.BaseAtk = Pokemon_BaseStats[self.Name][1]
        self.BaseDEF = Pokemon_BaseStats[self.Name][2]
        self.BaseSPECIAL = Pokemon_BaseStats[self.Name][4]
        self.BaseSPEED = Pokemon_BaseStats[self.Name][3]
        self.DVHP = 0
        self.DVAtk = random.randint(0,15)
        self.DVDEF = random.randint(0,15)
        self.DVSPECIAL = random.randint(0,15)
        self.DVSPEED = random.randint(0,15)
        self.EVHP = 0
        self.EVAtk = 0
        self.EVDEF = 0
        self.EVSPECIAL =0
        self.EVSPEED = 0
        if self.DVAtk % 2 == 1: self.DVHP += 8
        if self.DVDEF % 2 == 1:self.DVHP += 4
        if self.DVSPEED %2 == 1: self.DVHP += 2
        if self.DVSPECIAL %2 == 1: self.DVHP += 1
        self.LearnSet = Pokemon_Learnsets[self.Name]
        self.HP = Pokemon_BaseStats[self.Name][0]
        self.MAXHP = self.HP
        self.Atk:int = Pokemon_BaseStats[self.Name][1]
        self.AtkModifier = 1
        self.AtkCounter = 0
        self.DEF:int = Pokemon_BaseStats[self.Name][2]
        self.DEFModifier = 1
        self.DEFCounter = 0
        self.SPECIAL:int = Pokemon_BaseStats[self.Name][4]
        self.SPECIALModifier = 1
        self.Mimic = [False,0]
        self.SPECIALCounter = 0
        self.SPEED:int = Pokemon_BaseStats[self.Name][3]
        self.SPEEDModifier = 1
        self.SPEEDCounter = 0
        self.Evasion= 1
        self.EVASIONCounter = 0
        self.Accuracy = 1
        self.ACCURACYCounter = 0
        self.GainEXP = 0
        self.Fly = False
        self.Dig = False
        self.exp = Exp
        self.Stat_Update()
        self.HP = self.MAXHP 
        self.Heathbarlength = 100
        self.HealthbarColor = "Red"
        self.Health_Ratio = self.MAXHP/ self.Heathbarlength
        self.EXPGOAL = 0
        self.Attack = ''
        self.AttackDamage = 0
        self.AftermathText1 = ''
        self.AftermathText2 = ''
        self.AftermathText3 = ''
        self.AftermathStatus = ''
        self.AftermathStat = ''
        self.EnemyChangedStat = 0
        self.SelfChangedStat = 0
        self.Set_EXP_Goal()
        self.SleepTimer = 0
        self.PokemonMoves = PokemonMoves()
        self.Animation_Done1 = False
        self.Animation_Done2 = False 
        self.PAnimationCircle = ()
        self.PAnimationCircle2 = ()
        self.EAnimationCircle = (self.EnemyBattlerect.centerx - 50,self.EnemyBattlerect.centery)
        self.EAnimationCircle2 = (self.EnemyBattlerect.centerx - 50,self.EnemyBattlerect.centery + 50)
        self.TargetHP = 0
        self.ExtraTargetHP = 0
        self.HealedHP = 0
        self.BattleRole = "Player"
        self.Delay = 100
        self.OtherSpeedFactors =1
        self.OtherAttackFactors = 1
        self.LeechSeed = False
        self.FieldEffect = ''
        self.OPTrapTurns = 0
        self.TrappedTurns = -10
        self.NewMoveStatus = "None"
        self.FieldEffectTerm= 0
        self.NewMove = ""
        self.Flinch = False
        self.FieldTarget = False
        self.MovePriority = 0
        self.MoveTurn = ""
        self.IdleTurns = 0
        self.IdleMove = ''
        self.DisabledMove = ''
        self.DisabledTimer = 0
        self.ODisabledMove = ''
        self.ODisabledTimer = 0
        self.BideDamage = 0
        self.TransMove = []
        self.AllField = [['',0],['',0]]
        self.MyField = [['',0],['',0],['',0]]

    def Stat_Update(self):
        old = self.HP/self.MAXHP
        self.MAXHP = round((((self.BaseHp + self.DVHP) * 2 + round(sqrt(self.EVHP)/4)) * self.Level)/100) + self.Level + 10
        self.Atk = round((((self.BaseAtk + self.DVAtk) * 2 + round(sqrt(self.EVAtk)/4)) * self.Level)/100) + 5
        self.DEF = round((((self.BaseDEF + self.DVDEF) * 2 + round(sqrt(self.EVDEF)/4)) * self.Level)/100) + 5
        self.SPEED = round((((self.BaseSPEED + self.DVSPEED) * 2 + round(sqrt(self.EVSPEED)/4)) * self.Level)/100) + 5
        self.SPECIAL = round((((self.BaseSPECIAL + self.DVSPECIAL) * 2 + round(sqrt(self.EVSPECIAL)/4)) * self.Level)/100) + 5
        self.HP = self.MAXHP * old
        self.HP = round(self.HP)

    def Healthbar_Color(self):
        Healthpercent = self.HP / self.MAXHP
        if Healthpercent <= 1 and Healthpercent > 0.5:
            self.HealthbarColor = "Green"
        elif Healthpercent <= 0.5 and Healthpercent > 0.2:
            self.HealthbarColor = "Yellow"
        elif Healthpercent <= 0.2:
            self.HealthbarColor = "Red"

    def SetUpNewMove(self,ReplacedMove:int,Move:str):
        if ReplacedMove == 1:
            self.Moves[0] = Move
            self.Move1pp = Pokemon_Move_PP[self.Moves[0]]
            self.Move1Type = Pokemon_Move_Type[self.Moves[0]]
            self.MaxMove1pp = self.Move1pp
        elif ReplacedMove == 2:
            self.Moves[1] = Move
            self.Move2pp = Pokemon_Move_PP[self.Moves[1]]
            self.Move2Type = Pokemon_Move_Type[self.Moves[1]]
            self.MaxMove2pp = self.Move2pp
        elif ReplacedMove == 3:
            self.Moves[2] = Move
            self.Move3pp = Pokemon_Move_PP[self.Moves[2]]
            self.Move3Type = Pokemon_Move_Type[self.Moves[2]]
            self.MaxMove3pp = self.Move3pp
        else:
            self.Moves[3] = Move
            self.Move4pp = Pokemon_Move_PP[self.Moves[3]]
            self.Move4Type = Pokemon_Move_Type[self.Moves[3]]
            self.MaxMove4pp = self.Move4pp

    def Draw_Healthar(self,x:int,y:int):
        self.Healthbar_Color()
        pygame.draw.rect(pygame.display.get_surface(),self.HealthbarColor,(x,y,int(self.HP)/self.Health_Ratio,10),border_radius=12)

    def AddPPMove(self,Move:str,Amount:int):
        if Move == "1": 
            self.Move1pp += Amount
            if self.Move1pp > self.MaxMove1pp:self.Move1pp = self.MaxMove1pp
        elif Move == "2": 
            self.Move2pp += Amount
            if self.Move2pp > self.MaxMove2pp:self.Move2pp = self.MaxMove2pp
        elif Move == "3": 
            self.Move3pp += Amount
            if self.Move3pp > self.MaxMove3pp:self.Move3pp = self.MaxMove3pp
        elif Move == "4": 
            self.Move4pp += Amount
            if self.Move4pp > self.MaxMove4pp:self.Move4pp = self.MaxMove4pp

    def IncreaseMovePP(self,Move:str):
        if Move == "1": 
            self.MaxMove1pp += self.MaxMove1pp/5
            if self.Move1pp +5 == self.MaxMove1pp:self.Move1pp = self.MaxMove1pp
        elif Move == "2": 
            self.MaxMove2pp += self.MaxMove2pp/5
            if self.Move2pp +5 == self.MaxMove2pp:self.Move2pp = self.MaxMove2pp
        elif Move == "3": 
            self.MaxMove3pp += self.MaxMove3pp/5
            if self.Move3pp +5 == self.MaxMove3pp:self.Move3pp = self.MaxMove3pp
        elif Move == "4": 
            self.MaxMove4pp += self.MaxMove4pp/5
            if self.Move4pp +5 == self.MaxMove4pp:self.Move4pp = self.MaxMove4pp

    def MissedMove(self):
        self.AftermathText1 = f"{self.NickName} missed"
        self.AftermathText2 = ""
        self.AftermathText3 = ""
        self.EnemyChangedStat = 0
        self.AftermathStat = ""
        self.AftermathStatus = "OK"
        self.AttackDamage = 0
        self.Flinch = False
        self.ODisabledTimer = 0
        self.ODisabledMove = ''

    def Exp_Gain(self,Defeated_poke,Particapants:int,Trainer:str,Exp_All:bool = False):
        a = 1
        t = 1
        b = Pokemon_EXP[Defeated_poke.Name]
        L = Defeated_poke.Level
        s = Particapants
        if Exp_All:
            if self.Particaption:
                s = 2*Particapants
            else:
                s = 2*Particapants*1
        if Trainer != self.Trainer:
            t = 1.5
        if Defeated_poke.Trainer != "Wild": a = 1.5
        self.GainEXP = ((b * L)/7) * (1/s) * a * t
        self.EVGain(Defeated_poke.Name,Particapants)
        self.exp += self.GainEXP
        self.NewMoveStatus = "None"
        self.NewMove = ""
        while self.exp >= self.EXPGOAL:
            self.exp -= self.EXPGOAL
            self.exp = round(self.exp)
            self.Level += 1
            self.Level_up = True
            self.LV_UP()
        self.exp = round(self.exp)

    def LV_UP(self):
        self.LearnSetMove()
        self.Set_EXP_Goal()
        self.Stat_Update()

    def Last4Moves(self,Level):
        Move = []
        Moves = []
        for y,i in enumerate(self.LearnSet):
            if Level >= i[0] and len(Moves) < 4: Moves.append(y)
        Moves.reverse()
        for i in Moves: Move.append(self.LearnSet[i][1])
        if len(Move) < 4:
            for i in range(4 - len(Move)):
                Move.append("-")
        self.Move1pp = Pokemon_Move_PP[Move[0]]
        self.Move1Type = Pokemon_Move_Type[Move[0]]
        self.MaxMove1pp = self.Move1pp
        self.Move2pp = Pokemon_Move_PP[Move[1]]
        self.Move2Type = Pokemon_Move_Type[Move[1]]
        self.MaxMove2pp = self.Move2pp
        self.Move3pp = Pokemon_Move_PP[Move[2]]
        self.Move3Type = Pokemon_Move_Type[Move[2]]
        self.MaxMove3pp = self.Move3pp
        self.Move4pp = Pokemon_Move_PP[Move[3]]
        self.Move4Type = Pokemon_Move_Type[Move[3]]
        self.MaxMove4pp = self.Move4pp
        return Move

    def EVGain(self,Defeated_poke_Name:str,Particapants:int):
        self.EVHP += round(Pokemon_BaseStats[Defeated_poke_Name][0]/Particapants)
        if self.EVHP > 65_535:self.EVHP = 65_535
        self.EVAtk += round(Pokemon_BaseStats[Defeated_poke_Name][1]/Particapants)
        if self.EVAtk > 65_535:self.EVAtk = 65_535
        self.EVDEF += round(Pokemon_BaseStats[Defeated_poke_Name][2]/Particapants)
        if self.EVDEF > 65_535:self.EVDEF = 65_535
        self.EVSPEED += round(Pokemon_BaseStats[Defeated_poke_Name][3]/Particapants)
        if self.EVSPEED > 65_535:self.EVSPEED = 65_535
        self.EVSPECIAL += round(Pokemon_BaseStats[Defeated_poke_Name][4]/Particapants)
        if self.EVSPECIAL > 65_535:self.EVSPECIAL = 65_535

    def Move_Update(self):
        self.Move1pp = Pokemon_Move_PP[self.Moves[0]]
        self.Move1Type = Pokemon_Move_Type[self.Moves[0]]
        self.MaxMove1pp = self.Move1pp
        self.Move2pp = Pokemon_Move_PP[self.Moves[1]]
        self.Move2Type = Pokemon_Move_Type[self.Moves[1]]
        self.MaxMove2pp = self.Move2pp
        self.Move3pp = Pokemon_Move_PP[self.Moves[2]]
        self.Move3Type = Pokemon_Move_Type[self.Moves[2]]
        self.MaxMove3pp = self.Move3pp
        self.Move4pp = Pokemon_Move_PP[self.Moves[3]]
        self.Move4Type = Pokemon_Move_Type[self.Moves[3]]
        self.MaxMove4pp = self.Move4pp

    def Evoluation(self):
        self.Name = self.NextStage[1]
        self.Back_Img = pygame.image.load(Pokes_img[self.Name][0]).convert_alpha()
        self.Front_Img = pygame.image.load(Pokes_img[self.Name][1]).convert_alpha()
        self.Back_Img = pygame.transform.rotozoom(self.Back_Img,360,2)
        self.PlayerBattlerect = self.Back_Img.get_rect(topleft = (70, 290))
        self.Type = Pokemon_Types[self.Name]
        self.CatchRate = Pokemon_CatchRates[self.Name]
        self.NextStage = Pokemon_Evolutions[self.Name]
        self.EXPGroup = Pokemon_EXPGroups[self.Name]
        self.BaseHp = Pokemon_BaseStats[self.Name][0]
        self.BaseAtk = Pokemon_BaseStats[self.Name][1]
        self.BaseDEF = Pokemon_BaseStats[self.Name][2]
        self.BaseSPECIAL = Pokemon_BaseStats[self.Name][4]
        self.BaseSPEED = Pokemon_BaseStats[self.Name][3]
        self.LearnSet = Pokemon_Learnsets[self.Name]
        self.Stat_Update()
        self.LearnSetMove()

    def New_move(self,Move:str):
        self.NewMove = Move
        if Move not in self.Moves:
            if "-" in self.Moves:
                self.NewMoveStatus = "Learned"
                if self.Moves[1] == '-':
                    self.Moves[1] = Move
                    self.Move2pp = Pokemon_Move_PP[self.Moves[1]]
                    self.Move2Type = Pokemon_Move_Type[self.Moves[1]]
                    self.MaxMove2pp = self.Move2pp
                elif self.Moves[2] == '-':
                    self.Moves[2] = Move
                    self.Move3pp = Pokemon_Move_PP[self.Moves[2]]
                    self.Move3Type = Pokemon_Move_Type[self.Moves[2]]
                    self.MaxMove3pp = self.Move3pp
                elif self.Moves[3] == '-':
                    self.Moves[3] = Move
                    self.Move4pp = Pokemon_Move_PP[self.Moves[3]]
                    self.Move4Type = Pokemon_Move_Type[self.Moves[3]]
                    self.MaxMove4pp = self.Move4pp
            else: self.NewMoveStatus = "Choice"

    def LearnSetMove(self):
        Index = '0'
        for i,Move in enumerate(self.LearnSet):
            if Move[0] == self.Level: Index = i
        if Index != '0': self.New_move(self.LearnSet[Index][1])

    def GetBattleAttack(self) -> int:
        if self.Status == "BRN": return (self.Atk * self.AtkModifier)/2
        else: return (self.Atk * self.AtkModifier)
    
    def GetBattleSpeed(self) -> int:
        return (self.SPEED * self.SPEEDModifier) * self.OtherSpeedFactors
    
    def ADSSStat_update(self,StatCounter:int):
        if StatCounter == 0: return 1
        elif StatCounter == 1: return 1.5
        elif StatCounter == 2: return 2
        elif StatCounter == 3: return 2.5
        elif StatCounter == 4: return 3
        elif StatCounter == 5: return 3.5
        elif StatCounter == 6: return 4
        elif StatCounter == -1: return 0.67
        elif StatCounter == -2: return 0.5
        elif StatCounter == -3: return 0.4
        elif StatCounter == -4: return 0.33
        elif StatCounter == -5: return 0.29
        elif StatCounter == -6: return 0.25

    def EvasionStat_update(self):
        if self.EVASIONCounter == 0: self.Evasion = 1
        elif self.EVASIONCounter == 1: self.Evasion = 0.75
        elif self.EVASIONCounter == 2: self.Evasion = 0.60
        elif self.EVASIONCounter == 3: self.Evasion = 0.50
        elif self.EVASIONCounter == 4: self.Evasion = 0.43
        elif self.EVASIONCounter == 5: self.Evasion = 0.38
        elif self.EVASIONCounter == 6: self.Evasion = 0.33
        elif self.EVASIONCounter == -1: self.Evasion = 1.33
        elif self.EVASIONCounter == -2: self.Evasion = 1.67
        elif self.EVASIONCounter == -3: self.Evasion = 2
        elif self.EVASIONCounter == -4: self.Evasion = 2.33
        elif self.EVASIONCounter == -5: self.Evasion = 2.67
        elif self.EVASIONCounter == -6: self.Evasion = 3

    def Accuracy_update(self):
        if self.ACCURACYCounter == 0: self.Accuracy = 1
        elif self.ACCURACYCounter == -1: self.Accuracy = 0.75
        elif self.ACCURACYCounter == -2: self.Accuracy = 0.60
        elif self.ACCURACYCounter == -3: self.Accuracy = 0.50
        elif self.ACCURACYCounter == -4: self.Accuracy = 0.43
        elif self.ACCURACYCounter == -5: self.Accuracy = 0.38
        elif self.ACCURACYCounter == -6: self.Accuracy = 0.33
        elif self.ACCURACYCounter == 1: self.Accuracy = 1.33
        elif self.ACCURACYCounter == 2: self.Accuracy = 1.67
        elif self.ACCURACYCounter == 3: self.Accuracy = 2
        elif self.ACCURACYCounter == 4: self.Accuracy = 2.33
        elif self.ACCURACYCounter == 5: self.Accuracy = 2.67
        elif self.ACCURACYCounter == 6: self.Accuracy = 3

    def BattleStat_update(self):
        self.AtkModifier = self.ADSSStat_update(self.AtkCounter)
        self.DEFModifier = self.ADSSStat_update(self.DEFCounter)
        self.SPECIALModifier = self.ADSSStat_update(self.SPECIALCounter)
        self.SPEEDModifier = self.ADSSStat_update(self.SPEEDCounter)
        self.EvasionStat_update()
        self.Accuracy_update()
        if self.Status == "Paralyz": self.OtherSpeedFactors = 3/4

    def Set_EXP_Goal(self):
        n = self.Level + 1
        if self.EXPGroup == "Medium Slow":self.EXPGOAL = ((6/5 * (n**3)) - (15 * (n**2)) + (100 * n) - 140) - ((6/5 * (self.Level**3)) - (15 * (self.Level**2)) + (100 * self.Level) - 140)
        elif self.EXPGroup == "Medium Fast":self.EXPGOAL = (n**3) - (self.Level**3)
        elif self.EXPGroup == "Fast":self.EXPGOAL = (((4*n)**3)/5) - (((4*self.Level)**3)/5)
        elif self.EXPGroup == "Slow":self.EXPGOAL = (((5*n)**3)/4) - (((5*self.Level)**3)/4)
        self.EXPGOAL = round(self.EXPGOAL)

    def Get_Move(self,Attacker,Defender):
        if self.Attack in self.PokemonMoves.NormalDamagingList or self.Attack in self.PokemonMoves.HighCritMoves:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.BattleAnimation = self.PokemonMoves.Get_NormalDamagingAttack_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.EnemyStatChangingList:
            self.EnemyChangedStat,self.AftermathText1,self.AftermathStat,self.BattleAnimation  = self.PokemonMoves.Get_EnemyStatChanging_Move_by_Name(self.Attack,Attacker,Defender)
            self.AttackDamage = 0
        elif self.Attack in self.PokemonMoves.FieldAffectingList:
            self.AftermathText1,self.FieldEffect,self.FieldEffectTerm,self.BattleAnimation,self.FieldTarget = self.PokemonMoves.Get_FieldAffectingMove_by_Name(self.Attack,Attacker,Defender)
            self.AttackDamage = 0
        elif self.Attack in self.PokemonMoves.EnemyStatDamagingList:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.AftermathText3,self.BattleAnimation,self.EnemyChangedStat,self.AftermathStat = self.PokemonMoves.Get_EnemyStatDamagingMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.StatusDamagingList:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.AftermathText3,self.BattleAnimation,self.AftermathStatus = self.PokemonMoves.Get_EnemyStatusDamagingMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.SelfStatChangingList:
            self.SelfChangedStat,self.AftermathText1,self.AftermathStat,self.BattleAnimation = self.PokemonMoves.Get_SelfStatChanging_Move_by_Name(self.Attack,Attacker)
            self.AttackDamage = 0
        elif self.Attack in self.PokemonMoves.StatusList:
            self.AftermathText1,self.AftermathStatus,self.BattleAnimation = self.PokemonMoves.Get_EnemyStatusMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.PriorityDamagingList:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.MovePriority,self.BattleAnimation = self.PokemonMoves.Get_PriorityMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.MultihitList:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.AftermathText3,self.BattleAnimation = self.PokemonMoves.Get_MultiHitMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.MultiturnMovesList:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.MovePriority,self.IdleTurns,self.BattleAnimation,self.IdleMove = self.PokemonMoves.Get_MultiTurnMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.TrappingMoves:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.MovePriority,self.OPTrapTurns,self.BattleAnimation = self.PokemonMoves.Get_MultiTrappingMove_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.DrainingAttacksList:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.AftermathText3,self.BattleAnimation = self.PokemonMoves.Get_DrainingMoves_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.FlinchingMoves:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.Flinch,self.BattleAnimation = self.PokemonMoves.Get_FlinchingMoves(self.Attack,Attacker,Defender)
        elif self.Attack == "Disable":
            self.AftermathText1,self.ODisabledMove,self.ODisabledTimer,self.BattleAnimation = self.PokemonMoves.Get_Disable(Attacker,Defender)
        elif self.Attack == "Focus Energy":
            self.AftermathText1,self.FocusEnergy,self.BattleAnimation = self.PokemonMoves.Focus_Energy(Attacker)        
        elif self.Attack == "Light Screen":
            self.AftermathText1,self.LightScreenUp,self.BattleAnimation = self.PokemonMoves.Light_Screen(Attacker)
        elif self.Attack == "Reflect":
            self.AftermathText1,self.ReflectUp,self.BattleAnimation = self.PokemonMoves.Reflect(Attacker)
        elif self.Attack == "Rest":
            self.AftermathText1,self.AftermathStatus,self.ExtraTargetHP,self.BattleAnimation = self.PokemonMoves.Get_Rest(Attacker,Defender)
        elif self.Attack in self.PokemonMoves.WildBattleMoves:
            self.AftermathText1,self.Running,self.BattleAnimation = self.PokemonMoves.Get_WildMoves(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.SelfFaintingMoves:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.Faint,self.BattleAnimation = self.PokemonMoves.Get_SelfFaintingMoves(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.RecoilMoves:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.AftermathText3,self.RecoilDamage,self.BattleAnimation = self.PokemonMoves.Get_RecoilAttack_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack == "Mirror Move":
            if Defender.LastmoveUsed in ("","Trapped","Flinch"):
                self.AttackDamage,self.AftermathText1 = 0,"Move Failed"
                self.BattleAnimation = self.Teleport_Animation
            else:
                self.Attack = Defender.LastmoveUsed
                self.Get_Move(Attacker,Defender)
                self.Attack = "Mirror Move"
        elif self.Attack == "Metronome":
            self.Attack = random.choice(Pokemon_Move_Type.keys())
            self.Get_Move(Attacker,Defender)
            self.Attack = "Metronome"
        elif self.Attack == "Conversion":
            self.AftermathText1 = f"{self.NickName} copied {Defender.NickName} type"
            self.Type = Defender.Type 
            self.BattleAnimation = self.Teleport_Animation
        elif self.Attack == "Substitute":
            self.BattleAnimation = self.Substitute_Animation         
        elif self.Attack == "Mist":
            self.BattleAnimation = self.Mist_Animation
            self.StatProtect = True
            self.AftermathText1 = f"{self.NickName} put up a Mist"
        elif self.Attack == "Transform":
            if not(Defender.Dig and Defender.Fly and Defender.SubstituteOn):
                self.TransMove = self.Moves
                self.Moves = Defender.Moves
                self.Back_Img = Defender.Back_Img
                self.Front_Img = Defender.Front_Img
                self.Type = Defender.Type
                self.Atk = Defender.Atk
                self.DEF = Defender.DEF
                self.SPECIAL = Defender.SPECIAL
                self.SPEED = Defender.SPEED
                self.AtkCounter = Defender.AtkCounter
                self.DEFCounter = Defender.DEFCounter
                self.SPECIALCounter = Defender.SPECIALCounter
                self.SPEEDCounter = Defender.SPEEDCounter
                self.AftermathText1 = f"{self.NickName} transformed"
            else:
                self.AftermathText1 = "Move failed"
            self.BattleAnimation = self.Substitute_Animation
        elif self.Attack == "Mimic":
            if self.Moves[0] == "Mimic":
                self.Moves[0] = random.choice(Defender.Moves)
                self.Move1Type = Pokemon_Move_Type[self.Moves[0]]
                self.AftermathText1 = f"{self.NickName} copied {self.Moves[0]}"
                self.Mimic = [True,1]
            elif self.Moves[1] == "Mimic":
                self.Moves[1] = random.choice(Defender.Moves)
                self.Move2Type = Pokemon_Move_Type[self.Moves[1]]
                self.AftermathText1 = f"{self.NickName} copied {self.Moves[1]}"
                self.Mimic = [True,2]
            elif self.Moves[2] == "Mimic":
                self.Moves[2] = random.choice(Defender.Moves)
                self.Move3Type = Pokemon_Move_Type[self.Moves[2]]
                self.AftermathText1 = f"{self.NickName} copied {self.Moves[2]}"
                self.Mimic = [True,3]
            else:
                self.Moves[3] = random.choice(Defender.Moves)
                self.Move4Type = Pokemon_Move_Type[self.Moves[3]]
                self.Mimic = [True,4]
                self.AftermathText1 = f"{self.NickName} copied {self.Moves[3]}"
            self.BattleAnimation = self.Substitute_Animation
        elif self.Attack == "Haze":
            self.BattleAnimation = self.Mist_Animation
            self.AftermathText1 = f"{self.NickName} hazed the field"        
        elif self.Attack in self.PokemonMoves.RampageMoves:
            self.AttackDamage,self.AftermathText1,self.AftermathText2,self.AftermathText3,self.IdleTurns,self.BattleAnimation,self.IdleMove = self.PokemonMoves.Get_RampageMoves_by_Name(self.Attack,Attacker,Defender)
        elif self.Attack in self.PokemonMoves.HealingMoves:
            self.HealedHP,self.AftermathText1,self.BattleAnimation = self.PokemonMoves.Get_HealingMoves(self.Attack,Attacker)
        else:
            self.AttackDamage,self.AftermathText1,self.AftermathText2 = 0,f"{Defender.NickName}'s Attack continues",''

    def ConfusionEffect(self):
        return self.HP - self.PokemonMoves.Confusion_Damage_Calculation(self)       

    def End_Transformation(self):
        if self.TransMove != []:
            self.Stat_Update()
            self.Moves = self.TransMove
            self.Back_Img = pygame.image.load(Pokes_img[self.Name][0]).convert_alpha()
            self.Back_Img = pygame.transform.rotozoom(self.Back_Img,360,2)
            self.Front_Img = pygame.image.load(Pokes_img[self.Name][1]).convert_alpha()
            self.Type = Pokemon_Types[self.Name]

    def Get_Hazed(self):
        self.Remove_Battle_Counters()
        self.FocusEnergy = False
        self.StatProtect = False
        self.ReflectUp = False
        self.LightScreenUp = False
        self.ToxicTurn = 0
        self.ReflectDamage = 0
        self.ODisabledMove,self.ODisabledTimer = "",0
        self.Status2 = ""
        self.ConfusionTimeLimit = 0
        self.MyField = [['',0],['',0],['',0]]
        if self.Status not in ("PSN","BRN"): self.Status = "OK"
        self.LightScreenDamage = 0

    def PP_Control(self):
        if self.Attack == self.Moves[0]: self.Move1pp -= 1
        elif self.Attack == self.Moves[1]: self.Move2pp -= 1
        elif self.Attack == self.Moves[2]: self.Move3pp -= 1
        elif self.Attack == self.Moves[3]: self.Move4pp -= 1

    def Tackle_Animation(self):
        if self.BattleRole == "Player":
            if self.PlayerBattlerect.x > 30 and not self.Animation_Done1:
                self.PlayerBattlerect.x -= 0.01
                if self.PlayerBattlerect.x <= 30: self.Animation_Done1 = True
            elif self.PlayerBattlerect.x <= 30 or self.PlayerBattlerect.x < 70:
                self.PlayerBattlerect.x +=  1          
            if self.PlayerBattlerect.x >= 70:
                self.Animation_Done1 = False
                self.PlayerBattlerect.x = 70
                return True
        else:
            if self.EnemyBattlerect.x < 634 and not self.Animation_Done1:
                self.EnemyBattlerect.x += 1
                if self.EnemyBattlerect.x > 634: self.Animation_Done1 = True
            elif self.EnemyBattlerect.x >= 634 or self.EnemyBattlerect.x > 570:
                self.EnemyBattlerect.x -=  0.01          
                if self.EnemyBattlerect.x >= 570:
                    self.Animation_Done1 = False
                    self.EnemyBattlerect.x = 570
                    return True
        return False

    def Drill_Peck_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.polygon(pygame.display.get_surface(),"Gray",[(self.PlayerBattlerect.topright[0] + 20,self.PlayerBattlerect.y),(self.PlayerBattlerect.topright[0] + 20,self.PlayerBattlerect.centery),(self.PlayerBattlerect.topright[0] + 80,(self.PlayerBattlerect.centery + self.PlayerBattlerect.y)/2)])
            if self.PlayerBattlerect.x > 30 and not self.Animation_Done1:
                self.PlayerBattlerect.x -= 0.01
                if self.PlayerBattlerect.x <= 30: self.Animation_Done1 = True
            elif self.PlayerBattlerect.x <= 30 or self.PlayerBattlerect.x < 70:
                self.PlayerBattlerect.x +=  1          
            if self.PlayerBattlerect.x >= 70:
                self.Animation_Done1 = False
                self.PlayerBattlerect.x = 70
                return True
        else:
            pygame.draw.polygon(pygame.display.get_surface(),"Gray",[(self.EnemyBattlerect.topleft[0] - 20,self.EnemyBattlerect.y),(self.EnemyBattlerect.topleft[0] - 20,self.EnemyBattlerect.centery),(self.EnemyBattlerect.topleft[0] - 80,(self.EnemyBattlerect.centery + self.EnemyBattlerect.y)/2)])
            if self.EnemyBattlerect.x < 634 and not self.Animation_Done1:
                self.EnemyBattlerect.x += 1
                if self.EnemyBattlerect.x > 634: self.Animation_Done1 = True
            elif self.EnemyBattlerect.x >= 634 or self.EnemyBattlerect.x > 574:
                self.EnemyBattlerect.x -=  0.01          
                if self.EnemyBattlerect.x >= 574:
                    self.Animation_Done1 = False
                    self.EnemyBattlerect.x = 574
                    return True
        return False

    def Swift_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.centerx - 30,self.EnemyBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.centerx ,self.EnemyBattlerect.centery - 30),20,5)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.centerx + 30,self.PlayerBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.centerx ,self.PlayerBattlerect.centery - 30),20,5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Horn_Attack_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.polygon(pygame.display.get_surface(),"Gray",[(self.PlayerBattlerect.topright[0] + 20,self.PlayerBattlerect.y),(self.PlayerBattlerect.topright[0] + 20,self.PlayerBattlerect.centery),(self.PlayerBattlerect.topright[0] + 80,(self.PlayerBattlerect.centery + self.PlayerBattlerect.y)/2)])
        else:pygame.draw.polygon(pygame.display.get_surface(),"Gray",[(self.EnemyBattlerect.topleft[0] - 20,self.EnemyBattlerect.y),(self.EnemyBattlerect.topleft[0] - 20,self.EnemyBattlerect.centery),(self.EnemyBattlerect.topleft[0] - 80,(self.EnemyBattlerect.centery + self.EnemyBattlerect.y)/2)])
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Pay_Day_Animation(self):
        if self.BattleRole == "Player":
            for x in range(0,800,40):
                pygame.draw.circle(pygame.display.get_surface(),"Yellow",(x,self.EnemyBattlerect.bottomright[1]),10)
        else:
            for x in range(0,800,40):
                pygame.draw.circle(pygame.display.get_surface(),"Yellow",(x,self.PlayerBattlerect.bottomright[1]),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Dig_Animation(self):
        if self.BattleRole == "Player":
            if not self.Dig:
                if self.PlayerBattlerect.y < 800:self.PlayerBattlerect.y += 10
                else:return True
            else:
                if self.PlayerBattlerect.y > 240:self.PlayerBattlerect.y -= 40
                else:return True
        else:
            if not self.Dig:
                if self.EnemyBattlerect.y < 800:self.EnemyBattlerect.y += 20
                else:return True
            else:
                self.EnemyBattlerect = self.Front_Img.get_rect(topleft = (574,50))
                return True    
        return False

    def Fly_Animation(self):
        if self.BattleRole == "Player":
            if not self.Fly:
                if self.PlayerBattlerect.y > -50:self.PlayerBattlerect.y -= 10
                else:return True
            else:
                if self.PlayerBattlerect.y < 240:self.PlayerBattlerect.y += 40
                else:return True
        else:
            if not self.Fly:
                if self.EnemyBattlerect.y > -50:self.EnemyBattlerect.y -= 20
                else:return True
            else:
                self.EnemyBattlerect = self.Front_Img.get_rect(topleft = (574,50))
                return True    
        return False

    def Quick_Attack_Animation(self):
        if self.BattleRole == "Player":
            if self.PlayerBattlerect.x > 30 and not self.Animation_Done1:
                self.PlayerBattlerect.x -= 0.02
                if self.PlayerBattlerect.x <= 30: self.Animation_Done1 = True
            elif self.PlayerBattlerect.x <= 30 or self.PlayerBattlerect.x < 70:
                self.PlayerBattlerect.x +=  2          
            if self.PlayerBattlerect.x >= 70:
                self.Animation_Done1 = False
                self.PlayerBattlerect.x = 70
                return True
        else:
            if self.EnemyBattlerect.x < 634 and not self.Animation_Done1:
                self.EnemyBattlerect.x += 2
                if self.EnemyBattlerect.x > 634: self.Animation_Done1 = True
            elif self.EnemyBattlerect.x >= 634 or self.EnemyBattlerect.x > 574:
                self.EnemyBattlerect.x -=  0.02          
                if self.EnemyBattlerect.x >= 574:
                    self.Animation_Done1 = False
                    self.EnemyBattlerect.x = 574
                    return True
        return False

    def Vine_Whip_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"DarkGreen",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"DarkGreen",self.EnemyBattlerect.topright,self.EnemyBattlerect.bottomleft,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"DarkGreen",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"DarkGreen",self.PlayerBattlerect.topright,self.PlayerBattlerect.bottomleft,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Crabhammer_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Blue",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Blue",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Tail_Whip_Animation(self):
        if self.BattleRole == "Player":
            if self.PlayerBattlerect.x < 100 and not self.Animation_Done1 and not self.Animation_Done2:
                self.PlayerBattlerect.x += 1
                if self.PlayerBattlerect.x >= 100: self.Animation_Done1 = True
            elif (self.PlayerBattlerect.x <= 100 or self.PlayerBattlerect.x > 30) and not self.Animation_Done2:
                self.PlayerBattlerect.x -=  1          
                if self.PlayerBattlerect.x <= 30:
                    self.PlayerBattlerect.x = 30
                    self.Animation_Done2 = True
            elif self.PlayerBattlerect.x < 70:
                self.PlayerBattlerect.x +=  1          
                if self.PlayerBattlerect.x >= 70:
                    self.PlayerBattlerect.x = 70
                    self.Animation_Done2 = False
                    self.Animation_Done1 = False
                    return True
        else:
            if self.EnemyBattlerect.x < 604 and not self.Animation_Done1 and not self.Animation_Done2:
                self.EnemyBattlerect.x += 1
                if self.EnemyBattlerect.x >= 604: self.Animation_Done1 = True
            elif (self.EnemyBattlerect.x <= 604 or self.EnemyBattlerect.x > 534) and not self.Animation_Done2:
                self.EnemyBattlerect.x -=  1          
                if self.EnemyBattlerect.x <= 534:
                    self.EnemyBattlerect.x = 534
                    self.Animation_Done2 = True
            elif self.EnemyBattlerect.x < 574:
                self.EnemyBattlerect.x +=  1          
                if self.EnemyBattlerect.x >= 574:
                    self.EnemyBattlerect.x = 574
                    self.Animation_Done2 = False
                    self.Animation_Done1 = False
                    return True

    def Growl_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.topright,(self.PlayerBattlerect.topright[0] + 100,self.PlayerBattlerect.topright[1] - 50))
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.midright,(self.PlayerBattlerect.midright[0] + 100,self.PlayerBattlerect.centery))
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.bottomright,(self.PlayerBattlerect.bottomright[0] + 100,self.PlayerBattlerect.bottomleft[1] + 50))
        else:
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.topleft,(self.EnemyBattlerect.x - 100,self.EnemyBattlerect.y - 50))
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.midleft,(self.EnemyBattlerect.midleft[0] - 100,self.EnemyBattlerect.centery))
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.bottomleft,(self.EnemyBattlerect.bottomleft[0] - 100,self.EnemyBattlerect.bottomleft[1] + 50))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Leer_Animation(self):
        if self.BattleRole == "Player":
            if self.PlayerBattlerect.x < 100 and not self.Animation_Done1 and not self.Animation_Done2:
                self.PlayerBattlerect.x += 1
                if self.PlayerBattlerect.x >= 100: self.Animation_Done1 = True
            elif (self.PlayerBattlerect.x <= 100 or self.PlayerBattlerect.x > 30) and not self.Animation_Done2:
                self.PlayerBattlerect.x -=  1          
                if self.PlayerBattlerect.x <= 30:
                    self.PlayerBattlerect.x = 30
                    self.Animation_Done2 = True
            elif self.PlayerBattlerect.x < 70:
                self.PlayerBattlerect.x +=  1          
                if self.PlayerBattlerect.x >= 70:
                    self.PlayerBattlerect.x = 70
                    self.Animation_Done2 = False
                    self.Animation_Done1 = False
                    return True
        else:
            if self.EnemyBattlerect.x < 604 and not self.Animation_Done1 and not self.Animation_Done2:
                self.EnemyBattlerect.x += 1
                if self.EnemyBattlerect.x >= 604: self.Animation_Done1 = True
            elif (self.EnemyBattlerect.x <= 604 or self.EnemyBattlerect.x > 534) and not self.Animation_Done2:
                self.EnemyBattlerect.x -=  1          
                if self.EnemyBattlerect.x <= 534:
                    self.EnemyBattlerect.x = 534
                    self.Animation_Done2 = True
            elif self.EnemyBattlerect.x < 574:
                self.EnemyBattlerect.x +=  1          
                if self.EnemyBattlerect.x >= 574:
                    self.EnemyBattlerect.x = 574
                    self.Animation_Done2 = False
                    self.Animation_Done1 = False
                    return True

    def String_Shot_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.center),(self.EnemyBattlerect.center),4)
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.midleft),(self.EnemyBattlerect.midright),2)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.topleft),(self.EnemyBattlerect.topright),2)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.bottomleft),(self.EnemyBattlerect.bottomright),2)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.midleft),(self.PlayerBattlerect.midright),2)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.topleft),(self.PlayerBattlerect.topright),2)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.bottomleft),(self.PlayerBattlerect.bottomright),2)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Harden_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Silver",self.PlayerBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Silver",self.EnemyBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Acid_Armor_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Purple",self.PlayerBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Purple",self.EnemyBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def SolarBeamCharging_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Green",self.PlayerBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Green",self.EnemyBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def SkyAttackCharging_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Defense_Curl_Animation(self):
        if self.BattleRole == "Player": pygame.draw.circle(pygame.display.get_surface(),"Silver",self.PlayerBattlerect.center,self.PlayerBattlerect.size[0])
        else:pygame.draw.circle(pygame.display.get_surface(),"Silver",self.EnemyBattlerect.center,self.EnemyBattlerect.size[0])
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Withdraw_Animation(self):
        if self.BattleRole == "Player": pygame.draw.circle(pygame.display.get_surface(),"Aqua",self.PlayerBattlerect.center,self.PlayerBattlerect.size[0])
        else:pygame.draw.circle(pygame.display.get_surface(),"Aqua",self.EnemyBattlerect.center,self.EnemyBattlerect.size[0])
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Growth_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"DarkGreen",(self.PlayerBattlerect.centerx,self.PlayerBattlerect.y+100),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"DarkGreen",(self.PlayerBattlerect.midright[0]+100,self.PlayerBattlerect.midright[1]),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"DarkGreen",(self.PlayerBattlerect.midleft[0]-100,self.PlayerBattlerect.midleft[1]),10,6)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"DarkGreen",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y+100),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"DarkGreen",(self.EnemyBattlerect.midright[0]+100,self.EnemyBattlerect.midright[1]),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"DarkGreen",(self.EnemyBattlerect.midleft[0]-100,self.EnemyBattlerect.midleft[1]),10,6)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Scratch_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"White",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"White",self.EnemyBattlerect.topright,self.EnemyBattlerect.bottomleft,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"White",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"White",self.PlayerBattlerect.topright,self.PlayerBattlerect.bottomleft,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
            
    def Gust_Animation(self):
        for y in range(0,801,30):
            pygame.draw.line(pygame.display.get_surface(),"azure4",(0,y),(800,y),5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Aurora_Beam_Animation(self):
        for y in range(0,801,30):
            pygame.draw.line(pygame.display.get_surface(),random.choice(["Red","Orange","Yellow","Green","Blue","Purple","Pink"]),(0,y),(800,y),5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Petal_Dance_Animation(self):
        for y in range(0,801,30):
            pygame.draw.line(pygame.display.get_surface(),"Green",(0,y),(800,y),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Pin_Missile_Animation(self):
        for y in range(0,801,30):
            pygame.draw.line(pygame.display.get_surface(),"Yellow",(0,y),(800,y),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Peck_Animation(self):
        if self.BattleRole == "Player":
            if self.PlayerBattlerect.x > 30 and not self.Animation_Done1:
                self.PlayerBattlerect.x -= 0.01
                if self.PlayerBattlerect.x <= 30: self.Animation_Done1 = True
            elif self.PlayerBattlerect.x <= 30 or self.PlayerBattlerect.x < 70:
                self.PlayerBattlerect.x +=  1          
            if self.PlayerBattlerect.x >= 70:
                self.Animation_Done1 = False
                self.PlayerBattlerect.x = 70
                return True
        else:
            if self.EnemyBattlerect.x < 634 and not self.Animation_Done1:
                self.EnemyBattlerect.x += 1
                if self.EnemyBattlerect.x > 634: self.Animation_Done1 = True
            elif self.EnemyBattlerect.x >= 634 or self.EnemyBattlerect.x > 574:
                self.EnemyBattlerect.x -=  0.01          
                if self.EnemyBattlerect.x >= 574:
                    self.Animation_Done1 = False
                    self.EnemyBattlerect.x = 574
                    return True
        return False

    def Water_Gun_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y + 10),20)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx - 20,self.EnemyBattlerect.y + 10),20)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx + 20,self.EnemyBattlerect.y + 10),20)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx,self.PlayerBattlerect.y + 10),20)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx - 20,self.PlayerBattlerect.y + 10),20)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx + 20,self.PlayerBattlerect.y + 10),20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Sand_Attack_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"Brown",(0,0,800,250))
        else:pygame.draw.rect(pygame.display.get_surface(),"Brown",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Screech_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Blue",(400,200),30)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Blue",self.EnemyBattlerect.center,30,8)
        else:pygame.draw.circle(pygame.display.get_surface(),"Blue",self.PlayerBattlerect.center,30,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True

    def Leech_Seed_Animation(self):
        if self.BattleRole == "Player":
            for x in range(0,800,40):
                pygame.draw.circle(pygame.display.get_surface(),"Brown",(x,self.EnemyBattlerect.bottomright[1]),10)
        else:
            for x in range(0,800,40):
                pygame.draw.circle(pygame.display.get_surface(),"Brown",(x,self.PlayerBattlerect.bottomright[1]),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Bubble_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx - 30,self.EnemyBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx ,self.EnemyBattlerect.centery - 30),20,5)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx + 30,self.PlayerBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx ,self.PlayerBattlerect.centery - 30),20,5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Barrage_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk4",(self.EnemyBattlerect.centerx - 30,self.EnemyBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk4",(self.EnemyBattlerect.centerx ,self.EnemyBattlerect.centery - 30),20,5)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk4",(self.PlayerBattlerect.centerx + 30,self.PlayerBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk4",(self.PlayerBattlerect.centerx ,self.PlayerBattlerect.centery - 30),20,5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def BubbleBeam_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Aqua",(300,200),20,5)
        pygame.draw.circle(pygame.display.get_surface(),"Aqua",(400,200),20,5)
        pygame.draw.circle(pygame.display.get_surface(),"Aqua",(500,200),20,5)
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx - 30,self.EnemyBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.centerx ,self.EnemyBattlerect.centery - 30),20,5)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx + 30,self.PlayerBattlerect.centery),20,5)
            pygame.draw.circle(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.centerx ,self.PlayerBattlerect.centery - 30),20,5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Rock_Throw_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Brown",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y - 20),20)
            pygame.draw.circle(pygame.display.get_surface(),"Brown",(self.EnemyBattlerect.x ,self.EnemyBattlerect.y - 20),20)
            pygame.draw.circle(pygame.display.get_surface(),"Brown",(self.EnemyBattlerect.topright[0] ,self.EnemyBattlerect.y - 20),20)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Brown",(self.PlayerBattlerect.centerx ,self.PlayerBattlerect.y - 20),20)
            pygame.draw.circle(pygame.display.get_surface(),"Brown",(self.PlayerBattlerect.x ,self.PlayerBattlerect.y - 30),20)
            pygame.draw.circle(pygame.display.get_surface(),"Brown",(self.PlayerBattlerect.topright[0] ,self.PlayerBattlerect.y - 30),20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Egg_Bomb_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"burlywood3",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y - 20),20)
            pygame.draw.circle(pygame.display.get_surface(),"burlywood3",(self.EnemyBattlerect.x ,self.EnemyBattlerect.y - 20),20)
            pygame.draw.circle(pygame.display.get_surface(),"burlywood3",(self.EnemyBattlerect.topright[0] ,self.EnemyBattlerect.y - 20),20)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"burlywood3",(self.PlayerBattlerect.centerx ,self.PlayerBattlerect.y - 20),20)
            pygame.draw.circle(pygame.display.get_surface(),"burlywood3",(self.PlayerBattlerect.x ,self.PlayerBattlerect.y - 30),20)
            pygame.draw.circle(pygame.display.get_surface(),"burlywood3",(self.PlayerBattlerect.topright[0] ,self.PlayerBattlerect.y - 30),20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Ember_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.rect(pygame.display.get_surface(),"Red",((self.EnemyBattlerect.midleft),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"Red",((self.EnemyBattlerect.center),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"Red",((self.EnemyBattlerect.midright),(30,50)))
        else:
            pygame.draw.rect(pygame.display.get_surface(),"Red",((self.PlayerBattlerect.midleft),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"Red",((self.PlayerBattlerect.center),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"Red",((self.PlayerBattlerect.midright),(30,50)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Dragon_Rage_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.rect(pygame.display.get_surface(),"darkorchid1",((self.EnemyBattlerect.midleft),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"darkorchid1",((self.EnemyBattlerect.center),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"darkorchid1",((self.EnemyBattlerect.midright),(30,50)))
        else:
            pygame.draw.rect(pygame.display.get_surface(),"darkorchid1",((self.PlayerBattlerect.midleft),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"darkorchid1",((self.PlayerBattlerect.center),(30,50)))
            pygame.draw.rect(pygame.display.get_surface(),"darkorchid1",((self.PlayerBattlerect.midright),(30,50)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Confusion_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"Pink",self.EnemyBattlerect,10)
        else:pygame.draw.rect(pygame.display.get_surface(),"Pink",self.PlayerBattlerect,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Poison_Sting_Animation(self):
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Purple",self.EnemyBattlerect.center,10)
        else:pygame.draw.circle(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.center,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def ThunderShock_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.center,10)
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.center,(self.EnemyBattlerect.centerx,self.EnemyBattlerect.centery - 20))
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.center,(self.EnemyBattlerect.centerx,self.EnemyBattlerect.centery + 20))
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.center,(self.EnemyBattlerect.centerx - 20,self.EnemyBattlerect.centery))
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.center,(self.EnemyBattlerect.centerx + 20,self.EnemyBattlerect.centery))
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.center,10)
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.center,(self.PlayerBattlerect.centerx,self.PlayerBattlerect.centery - 20))
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.center,(self.PlayerBattlerect.centerx,self.PlayerBattlerect.centery + 20))
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.center,(self.PlayerBattlerect.centerx - 20,self.PlayerBattlerect.centery))
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.center,(self.PlayerBattlerect.centerx + 20,self.PlayerBattlerect.centery))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Thunderbolt_Animation(self):
        if self.BattleRole == "Player":pygame.draw.line(pygame.display.get_surface(),"Yellow",(self.EnemyBattlerect.centerx,0),(self.EnemyBattlerect.centerx,900),10)
        else:pygame.draw.line(pygame.display.get_surface(),"Yellow",(self.PlayerBattlerect.centerx,0),(self.PlayerBattlerect.centerx,900),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Thunder_Animation(self):
        if self.BattleRole == "Player":pygame.draw.line(pygame.display.get_surface(),"Yellow",(self.EnemyBattlerect.centerx,0),(self.EnemyBattlerect.centerx,900),30)
        else:pygame.draw.line(pygame.display.get_surface(),"Yellow",(self.PlayerBattlerect.centerx,0),(self.PlayerBattlerect.centerx,900),30)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Waterfall_Animation(self):
        if self.BattleRole == "Player":pygame.draw.line(pygame.display.get_surface(),"Blue",self.EnemyBattlerect.midtop,self.EnemyBattlerect.midbottom,10)
        else:pygame.draw.line(pygame.display.get_surface(),"Blue",self.PlayerBattlerect.midtop,self.PlayerBattlerect.midbottom,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Rock_Slide_Animation(self):
        if self.BattleRole == "Player":pygame.draw.line(pygame.display.get_surface(),"Brown",(self.EnemyBattlerect.centerx,0),(self.EnemyBattlerect.centerx,900),self.EnemyBattlerect.width + 100)
        else:pygame.draw.line(pygame.display.get_surface(),"Brown",(self.PlayerBattlerect.centerx,0),(self.PlayerBattlerect.centerx,900),self.PlayerBattlerect.width + 100)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Smog_Animation(self):
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Purple",self.EnemyBattlerect.center,30)
        else:pygame.draw.circle(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.center,30)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Thunder_Wave_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.topleft,self.EnemyBattlerect.topright)
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.midleft,self.EnemyBattlerect.midright)
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.bottomleft,self.EnemyBattlerect.bottomright)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.topleft,self.PlayerBattlerect.topright)
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.midleft,self.PlayerBattlerect.midright)
            pygame.draw.line(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.bottomleft,self.PlayerBattlerect.bottomright)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Sing_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Green",(400,200),30,8)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Green",self.EnemyBattlerect.center,30,8)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Green",self.PlayerBattlerect.center,30,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Roar_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Gray",(400,200),30,8)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Gray",self.EnemyBattlerect.center,30,8)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Gray",self.PlayerBattlerect.center,30,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Teleport_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Pink",self.PlayerBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Pink",self.EnemyBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Acid_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Purple",self.EnemyBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Purple",self.PlayerBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Sludge_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.center,self.EnemyBattlerect.center,7)
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Purple",self.EnemyBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"Purple",self.PlayerBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Lick_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"Pink",(self.EnemyBattlerect.x,0,(self.EnemyBattlerect.topright[0]-self.EnemyBattlerect.x),800))
        else:pygame.draw.rect(pygame.display.get_surface(),"Pink",(self.PlayerBattlerect.x,0,(self.PlayerBattlerect.topright[0]-self.PlayerBattlerect.x),800))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Supersonic_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Blue",(400,200),30,8)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Blue",self.EnemyBattlerect.center,30,8)
        else:pygame.draw.circle(pygame.display.get_surface(),"Blue",self.PlayerBattlerect.center,30,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def PsyWave_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Pink",(400,200),30,8)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Pink",self.EnemyBattlerect.center,30,8)
        else:pygame.draw.circle(pygame.display.get_surface(),"Pink",self.PlayerBattlerect.center,30,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Confuse_Ray_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Purple",(400,200),30,8)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Purple",self.EnemyBattlerect.center,30,8)
        else:pygame.draw.circle(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.center,30,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Razor_Leaf_Animation(self):
        pygame.draw.circle(pygame.display.get_surface(),"Darkgreen",(400,200),30)
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Darkgreen",self.EnemyBattlerect.center,30)
        else:pygame.draw.circle(pygame.display.get_surface(),"Darkgreen",self.PlayerBattlerect.center,30)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Swords_Dance_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.x,self.PlayerBattlerect.y - 10),(self.PlayerBattlerect.x,self.PlayerBattlerect.bottomleft[1]),10)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.centerx,self.PlayerBattlerect.y - 10),(self.PlayerBattlerect.centerx,self.PlayerBattlerect.bottomleft[1]),10)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.PlayerBattlerect.topright[0],self.PlayerBattlerect.y - 10),(self.PlayerBattlerect.topright[0],self.PlayerBattlerect.bottomleft[1]),10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.x,self.EnemyBattlerect.y ),(self.EnemyBattlerect.x,self.EnemyBattlerect.bottomleft[1]),10)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y),(self.EnemyBattlerect.centerx,self.EnemyBattlerect.bottomleft[1]),10)
            pygame.draw.line(pygame.display.get_surface(),"Gray",(self.EnemyBattlerect.topright[0],self.EnemyBattlerect.y),(self.EnemyBattlerect.topright[0],self.EnemyBattlerect.bottomleft[1]),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Bone_Club_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Brown",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Brown",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Twineedle_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Purple",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"Purple",self.EnemyBattlerect.topright,self.EnemyBattlerect.bottomleft,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.topright,self.PlayerBattlerect.bottomleft,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Bonemerang_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Brown",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"Brown",self.EnemyBattlerect.topright,self.EnemyBattlerect.bottomleft,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Brown",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"Brown",self.PlayerBattlerect.topright,self.PlayerBattlerect.bottomleft,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Hypnosis_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Pink",self.EnemyBattlerect.center,30,8)
            pygame.draw.circle(pygame.display.get_surface(),"Pink",self.EnemyBattlerect.center,50,8)
            pygame.draw.circle(pygame.display.get_surface(),"Pink",self.EnemyBattlerect.center,70,8)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Pink",self.PlayerBattlerect.center,30,8)
            pygame.draw.circle(pygame.display.get_surface(),"Pink",self.PlayerBattlerect.center,50,8)
            pygame.draw.circle(pygame.display.get_surface(),"Pink",self.PlayerBattlerect.center,70,8)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def PoisonPowder_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"Purple",(0,0,800,250))
        else:pygame.draw.rect(pygame.display.get_surface(),"Purple",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def SmokeScreen_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"Gray",(0,0,800,250))
        else:pygame.draw.rect(pygame.display.get_surface(),"Gray",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Stun_Spore_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"Yellow",(0,0,800,250))
        else:pygame.draw.rect(pygame.display.get_surface(),"Yellow",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def SleepPowder_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"Green",(0,0,800,250))
        else:pygame.draw.rect(pygame.display.get_surface(),"Green",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Psychic_Animation(self):
        if self.BattleRole == "Player":pygame.draw.rect(pygame.display.get_surface(),"deeppink1",(0,0,800,250))
        else:pygame.draw.rect(pygame.display.get_surface(),"deeppink1",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Lovely_Kiss_Animation(self):
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Pink",self.EnemyBattlerect.center,20)
        else:pygame.draw.circle(pygame.display.get_surface(),"Pink",self.PlayerBattlerect.center,20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Fire_Punch_Animation(self):
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Red",self.EnemyBattlerect.center,20)
        else:pygame.draw.circle(pygame.display.get_surface(),"Red",self.PlayerBattlerect.center,20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Ice_Punch_Animation(self):
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"aquamarine1",self.EnemyBattlerect.center,20)
        else:pygame.draw.circle(pygame.display.get_surface(),"aquamarine1",self.PlayerBattlerect.center,20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Thunder_Punch_Animation(self):
        if self.BattleRole == "Player":pygame.draw.circle(pygame.display.get_surface(),"Yellow",self.EnemyBattlerect.center,20)
        else:pygame.draw.circle(pygame.display.get_surface(),"Yellow",self.PlayerBattlerect.center,20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Fire_Blast_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Red",self.EnemyBattlerect.center,40)
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.midleft,self.EnemyBattlerect.midright)
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.midtop,self.EnemyBattlerect.midbottom)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Red",self.PlayerBattlerect.center,40)
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.midleft,self.PlayerBattlerect.midright)
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.midtop,self.PlayerBattlerect.midbottom)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Glare_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Red",(self.EnemyBattlerect.centerx - 10,self.EnemyBattlerect.centery),20)
            pygame.draw.circle(pygame.display.get_surface(),"Red",(self.EnemyBattlerect.centerx + 10,self.EnemyBattlerect.centery),20)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Pink",(self.PlayerBattlerect.centerx -10,self.PlayerBattlerect.centery),20)
            pygame.draw.circle(pygame.display.get_surface(),"Pink",(self.PlayerBattlerect.centerx +10,self.PlayerBattlerect.centery),20)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Surf_Animation(self):
        pygame.display.get_surface().fill("Aqua")
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Mist_Animation(self):
        pygame.display.get_surface().fill("Lightblue")
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Earthquake_Animation(self):
        pygame.display.get_surface().fill("Brown")
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Wrap_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.EnemyBattlerect.x - 10,self.EnemyBattlerect.y),(self.EnemyBattlerect.bottomleft[0] - 10,self.EnemyBattlerect.bottomleft[1]))
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.EnemyBattlerect.topright[0] + 10,self.EnemyBattlerect.topright[1]),(self.EnemyBattlerect.bottomright[0] + 10,self.EnemyBattlerect.bottomright[1]))
        else:
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.PlayerBattlerect.x - 10,self.PlayerBattlerect.y),(self.PlayerBattlerect.bottomleft[0] - 10,self.PlayerBattlerect.bottomleft[1]))
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.PlayerBattlerect.topright[0] + 10,self.PlayerBattlerect.topright[1]),(self.PlayerBattlerect.bottomright[0] + 10,self.PlayerBattlerect.bottomright[1]))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Clamp_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.x - 10,self.EnemyBattlerect.y),(self.EnemyBattlerect.bottomleft[0] - 10,self.EnemyBattlerect.bottomleft[1]))
            pygame.draw.line(pygame.display.get_surface(),"Aqua",(self.EnemyBattlerect.topright[0] + 10,self.EnemyBattlerect.topright[1]),(self.EnemyBattlerect.bottomright[0] + 10,self.EnemyBattlerect.bottomright[1]))
        else:
            pygame.draw.line(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.x - 10,self.PlayerBattlerect.y),(self.PlayerBattlerect.bottomleft[0] - 10,self.PlayerBattlerect.bottomleft[1]))
            pygame.draw.line(pygame.display.get_surface(),"Aqua",(self.PlayerBattlerect.topright[0] + 10,self.PlayerBattlerect.topright[1]),(self.PlayerBattlerect.bottomright[0] + 10,self.PlayerBattlerect.bottomright[1]))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Fire_Spin_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Red",(self.EnemyBattlerect.x - 10,self.EnemyBattlerect.y),(self.EnemyBattlerect.bottomleft[0] - 10,self.EnemyBattlerect.bottomleft[1]))
            pygame.draw.line(pygame.display.get_surface(),"Red",(self.EnemyBattlerect.topright[0] + 10,self.EnemyBattlerect.topright[1]),(self.EnemyBattlerect.bottomright[0] + 10,self.EnemyBattlerect.bottomright[1]))
        else:
            pygame.draw.line(pygame.display.get_surface(),"Red",(self.PlayerBattlerect.x - 10,self.PlayerBattlerect.y),(self.PlayerBattlerect.bottomleft[0] - 10,self.PlayerBattlerect.bottomleft[1]))
            pygame.draw.line(pygame.display.get_surface(),"Red",(self.PlayerBattlerect.topright[0] + 10,self.PlayerBattlerect.topright[1]),(self.PlayerBattlerect.bottomright[0] + 10,self.PlayerBattlerect.bottomright[1]))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Tri_Attack_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.polygon(pygame.display.get_surface(),"Aqua",[(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y),self.EnemyBattlerect.bottomright,self.EnemyBattlerect.bottomleft],5)
        else:
            pygame.draw.polygon(pygame.display.get_surface(),"Aqua",[(self.PlayerBattlerect.centerx,self.PlayerBattlerect.y),self.PlayerBattlerect.bottomright,self.PlayerBattlerect.bottomleft],5)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Bide_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk1",(self.PlayerBattlerect.centerx,self.PlayerBattlerect.y+100),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk1",(self.PlayerBattlerect.midright[0]+100,self.PlayerBattlerect.midright[1]),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk1",(self.PlayerBattlerect.midleft[0]-100,self.PlayerBattlerect.midleft[1]),10,6)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk1",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y+100),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk1",(self.EnemyBattlerect.midright[0]+100,self.EnemyBattlerect.midright[1]),10,6)
            pygame.draw.circle(pygame.display.get_surface(),"cornsilk1",(self.EnemyBattlerect.midleft[0]-100,self.EnemyBattlerect.midleft[1]),10,6)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Leech_Life_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"darkseagreen1",self.PlayerBattlerect.center,self.EnemyBattlerect.center,7)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Absorb_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Darkgreen",self.PlayerBattlerect.center,self.EnemyBattlerect.center,7)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Mega_Drain_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Darkgreen",self.PlayerBattlerect.topleft,self.EnemyBattlerect.topright,12)
        pygame.draw.line(pygame.display.get_surface(),"Darkgreen",self.PlayerBattlerect.center,self.EnemyBattlerect.center,12)
        pygame.draw.line(pygame.display.get_surface(),"Darkgreen",self.PlayerBattlerect.bottomleft,self.EnemyBattlerect.bottomright,12)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Psybeam_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Pink",self.PlayerBattlerect.center,self.EnemyBattlerect.center,7)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Ice_Beam_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"aquamarine1",self.PlayerBattlerect.center,self.EnemyBattlerect.center,7)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Hydro_Pump_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Blue",self.PlayerBattlerect.center,self.EnemyBattlerect.center,400)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def SolarBeam_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Green",self.PlayerBattlerect.center,self.EnemyBattlerect.center,400)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Flamethrower_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.center,self.EnemyBattlerect.center,400)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Dream_Eater_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"Purple",self.PlayerBattlerect.center,self.EnemyBattlerect.center,7)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Disable_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.topleft,self.EnemyBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"Red",self.EnemyBattlerect.topright,self.EnemyBattlerect.bottomleft,10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.topleft,self.PlayerBattlerect.bottomright,10)
            pygame.draw.line(pygame.display.get_surface(),"Red",self.PlayerBattlerect.topright,self.PlayerBattlerect.bottomleft,10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Night_Shade_Animation(self):
        pygame.display.get_surface().fill("Black")
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Blizzard_Animation(self):
        pygame.display.get_surface().fill("aquamarine1")
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Flash_Animation(self):
        Color = "White"
        if self.Delay > 0:
            pygame.display.get_surface().fill(Color)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Focus_Energy_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",(self.PlayerBattlerect.centerx,self.PlayerBattlerect.y+100),10)
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",(self.PlayerBattlerect.midright[0]+100,self.PlayerBattlerect.midright[1]),10)
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",(self.PlayerBattlerect.midleft[0]-100,self.PlayerBattlerect.midleft[1]),10)
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",(self.EnemyBattlerect.centerx,self.EnemyBattlerect.y+100),10)
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",(self.EnemyBattlerect.midright[0]+100,self.EnemyBattlerect.midright[1]),10)
            pygame.draw.circle(pygame.display.get_surface(),"Yellow",(self.EnemyBattlerect.midleft[0]-100,self.EnemyBattlerect.midleft[1]),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Hyper_Fang_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.EnemyBattlerect.x - 30,self.EnemyBattlerect.y -10),(self.EnemyBattlerect.topright[0] + 10,self.EnemyBattlerect.topright[1] -10),3)
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.EnemyBattlerect.bottomleft[0] - 30,self.EnemyBattlerect.bottomleft[1] +10),(self.EnemyBattlerect.bottomright[0] + 10,self.EnemyBattlerect.bottomright[1] +10),3)
            pygame.draw.line(pygame.display.get_surface(),"Black",(int(((self.EnemyBattlerect.x -30) + (self.EnemyBattlerect.topright[0] + 10))/2),self.EnemyBattlerect.y -10),(int(((self.EnemyBattlerect.x -30) + (self.EnemyBattlerect.topright[0] + 10))/2),int(((self.EnemyBattlerect.bottomright[1] +10) + (self.EnemyBattlerect.y -10))/2)),10)
        else:
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.PlayerBattlerect.x - 30,self.PlayerBattlerect.y -10),(self.PlayerBattlerect.topright[0] + 10,self.PlayerBattlerect.topright[1] -10),3)
            pygame.draw.line(pygame.display.get_surface(),"Black",(self.PlayerBattlerect.bottomleft[0] - 30,self.PlayerBattlerect.bottomleft[1] +10),(self.PlayerBattlerect.bottomright[0] + 10,self.PlayerBattlerect.bottomright[1] +10),3)
            pygame.draw.line(pygame.display.get_surface(),"Black",(int(((self.PlayerBattlerect.x -30) + (self.PlayerBattlerect.topright[0] + 10))/2),self.PlayerBattlerect.y -10),(int(((self.PlayerBattlerect.x -30) + (self.PlayerBattlerect.topright[0] + 10))/2),int(((self.PlayerBattlerect.bottomright[1] +10) + (self.PlayerBattlerect.y -10))/2)),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Hyper_Beam_Animation(self):
        pygame.draw.line(pygame.display.get_surface(),"cornsilk1",(self.PlayerBattlerect.center),(self.EnemyBattlerect.center),10)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Selfdestruct_Animation(self):
        if self.BattleRole == "Player":
            pygame.draw.circle(pygame.display.get_surface(),"Black",self.PlayerBattlerect.center,100)
            pygame.draw.rect(pygame.display.get_surface(),"Red",(0,0,800,250))
        else:
            pygame.draw.circle(pygame.display.get_surface(),"Black",self.EnemyBattlerect.center,100)
            pygame.draw.rect(pygame.display.get_surface(),"Red",(0,self.PlayerBattlerect.y -10,800,pygame.display.get_surface().get_width() - (self.PlayerBattlerect.y -10)))
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False

    def Substitute_Animation(self):
        if self.BattleRole == "Player": pygame.draw.rect(pygame.display.get_surface(),"cornsilk1",self.PlayerBattlerect)
        else:pygame.draw.rect(pygame.display.get_surface(),"cornsilk1",self.EnemyBattlerect)
        self.Delay -= 1
        if self.Delay <= 0: 
            self.Delay = 100
            return True
        return False
    
    def Heal(self,Amount:int,PP:bool = False,Status:bool = False):
        self.HP += Amount
        if self.HP > self.MAXHP:self.HP = self.MAXHP
        if PP:
            self.Move1pp = self.MaxMove1pp
            self.Move2pp = self.MaxMove2pp
            self.Move3pp = self.MaxMove3pp
            self.Move4pp = self.MaxMove4pp
        if Status: 
            self.Status = "OK"
            self.Status2 = ""
            self.ToxicTurn = 0

    def AddingtoBattleField(self,Effect:str,Term:int,All:bool):
        if All:
            for i in range(10):
                if self.AllField[i][0] == '':
                    self.AllField[i][0] = Effect
                    self.AllField[i][1] = Term
                    break
        else:
            for i in range(10):
                if self.MyField[i][0] == '':
                    self.MyField[i][0] = Effect
                    self.MyField[i][1] = Term
                    break

    def Attack_AfterMath(self,Status:str,Stat:str,Change_in_Stat:int,FieldEffect:str,FieldEffectterm:int,FieldTarget:bool):
        if not self.SubstituteOn:
            if Status == "Confused" and self.Status2 == "": 
                self.Status2 = Status
                self.ConfusionTimeLimit = random.randint(2,5)
            else: 
                if Status != "Confused":
                    if self.Status == "OK": 
                        self.Status = Status
                        if Status == "SLP":
                            self.SleepTimer = random.randint(2,8)
                        if Status == "Bad PSN":
                            self.ToxicTurn = 1
                            self.Status = "PSN"
        if FieldEffectterm != 0 and not Two_D_ListCheck(self.MyField,FieldEffect) and not Two_D_ListCheck(self.AllField,FieldEffect):
            self.AddingtoBattleField(FieldEffect,FieldEffectterm,FieldTarget)
        if not self.SubstituteOn and not self.StatProtect:
            if Stat != "":
                if Stat == "Attack":
                    self.AtkCounter = Change_in_Stat
                elif Stat == 'Defense':
                    self.DEFCounter = Change_in_Stat
                elif Stat == 'Accuracy':
                    self.ACCURACYCounter = Change_in_Stat
                elif Stat == 'Evasion':
                    self.EVASIONCounter = Change_in_Stat
                elif Stat == "Speed":
                    self.SPEEDCounter = Change_in_Stat  
                else:
                    self.SPECIALCounter = Change_in_Stat

    def Remove_Battle_Counters(self):
        self.AtkCounter = 0
        self.DEFCounter = 0
        self.SPECIALCounter = 0
        self.SPEEDCounter = 0
        self.ACCURACYCounter = 0
        self.EVASIONCounter = 0