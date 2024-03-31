import streamlit as st
from time import time,strftime


#cd C:\Users\quewa\Documents\Pokémon\9
import streamlit as st #streamlit run Pok.py

st.set_option('deprecation.showPyplotGlobalUse', False)


# Charger le contenu du fichier CSS
with open('css.css') as f:
    css = f.read()

# Ajouter le contenu du fichier CSS à l'application Streamlit
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.title("Analyse des tiers")




gen = st.number_input("Sélectionnez votre gen", min_value=1, max_value=9, step=1, value=9 )


# Mettez à jour la session state avec la nouvelle valeur de gen
st.session_state.gen = gen

# Widget de sélection du mode
tier = st.selectbox("Choisissez le tier", ["ou", "uu","lc","ru","doublesou","ubers","1v1"]) # index=0

st.session_state.tier = tier


#traduction
@st.cache
def sttrad():
    print("cc trad")
    return("""0001	Bulbasaur	Bulbasaur	Bulbizarre
0002	Ivysaur	Ivysaur	Herbizarre
0003	Venusaur	Venusaur	Florizarre
0004	Charmander	Charmander	Salamèche
0005	Charmeleon	Charmeleon	Reptincel
0006	Charizard	Charizard	Dracaufeu
0007	Squirtle	Squirtle	Carapuce
0008	Wartortle	Wartortle	Carabaffe
0009	Blastoise	Blastoise	Tortank
0010	Caterpie	Caterpie	Chenipan
0011	Metapod	Metapod	Chrysacier
0012	Butterfree	Butterfree	Papilusion
0013	Weedle	Weedle	Aspicot
0014	Kakuna	Kakuna	Coconfort
0015	Beedrill	Beedrill	Dardargnan
0016	Pidgey	Pidgey	Roucool
0017	Pidgeotto	Pidgeotto	Roucoups
0018	Pidgeot	Pidgeot	Roucarnage
0019	Rattata	Rattata	Rattata
0020	Raticate	Raticate	Rattatac
0021	Spearow	Spearow	Piafabec
0022	Fearow	Fearow	Rapasdepic
0023	Ekans	Ekans	Abo
0024	Arbok	Arbok	Arbok
0025	Pikachu	Pikachu	Pikachu
0026	Raichu	Raichu	Raichu
0027	Sandshrew	Sandshrew	Sabelette
0028	Sandslash	Sandslash	Sablaireau
0029	Nidoran♀	Nidoran♀	Nidoran♀
0030	Nidorina	Nidorina	Nidorina
0031	Nidoqueen	Nidoqueen	Nidoqueen
0032	Nidoran♂	Nidoran♂	Nidoran♂
0033	Nidorino	Nidorino	Nidorino
0034	Nidoking	Nidoking	Nidoking
0035	Clefairy	Clefairy	Mélofée
0036	Clefable	Clefable	Mélodelfe
0037	Vulpix	Vulpix	Goupix
0038	Ninetales	Ninetales	Feunard
0039	Jigglypuff	Jigglypuff	Rondoudou
0040	Wigglytuff	Wigglytuff	Grodoudou
0041	Zubat	Zubat	Nosferapti
0042	Golbat	Golbat	Nosferalto
0043	Oddish	Oddish	Mystherbe
0044	Gloom	Gloom	Ortide
0045	Vileplume	Vileplume	Rafflesia
0046	Paras	Paras	Paras
0047	Parasect	Parasect	Parasect
0048	Venonat	Venonat	Mimitoss
0049	Venomoth	Venomoth	Aéromite
0050	Diglett	Diglett	Taupiqueur
0051	Dugtrio	Dugtrio	Triopikeur
0052	Meowth	Meowth	Miaouss
0053	Persian	Persian	Persian
0054	Psyduck	Psyduck	Psykokwak
0055	Golduck	Golduck	Akwakwak
0056	Mankey	Mankey	Férosinge
0057	Primeape	Primeape	Colossinge
0058	Growlithe	Growlithe	Caninos
0059	Arcanine	Arcanine	Arcanin
0060	Poliwag	Poliwag	Ptitard
0061	Poliwhirl	Poliwhirl	Têtarte
0062	Poliwrath	Poliwrath	Tartard
0063	Abra	Abra	Abra
0064	Kadabra	Kadabra	Kadabra
0065	Alakazam	Alakazam	Alakazam
0066	Machop	Machop	Machoc
0067	Machoke	Machoke	Machopeur
0068	Machamp	Machamp	Mackogneur
0069	Bellsprout	Bellsprout	Chétiflor
0070	Weepinbell	Weepinbell	Boustiflor
0071	Victreebel	Victreebel	Empiflor
0072	Tentacool	Tentacool	Tentacool
0073	Tentacruel	Tentacruel	Tentacruel
0074	Geodude	Geodude	Racaillou
0075	Graveler	Graveler	Gravalanch
0076	Golem	Golem	Grolem
0077	Ponyta	Ponyta	Ponyta
0078	Rapidash	Rapidash	Galopa
0079	Slowpoke	Slowpoke	Ramoloss
0080	Slowbro	Slowbro	Flagadoss
0081	Magnemite	Magnemite	Magnéti
0082	Magneton	Magneton	Magnéton
0083	Farfetch'd	Farfetch'd	Canarticho
0084	Doduo	Doduo	Doduo
0085	Dodrio	Dodrio	Dodrio
0086	Seel	Seel	Otaria
0087	Dewgong	Dewgong	Lamantine
0088	Grimer	Grimer	Tadmorv
0089	Muk	Muk	Grotadmorv
0090	Shellder	Shellder	Kokiyas
0091	Cloyster	Cloyster	Crustabri
0092	Gastly	Gastly	Fantominus
0093	Haunter	Haunter	Spectrum
0094	Gengar	Gengar	Ectoplasma
0095	Onix	Onix	Onix
0096	Drowzee	Drowzee	Soporifik
0097	Hypno	Hypno	Hypnomade
0098	Krabby	Krabby	Krabby
0099	Kingler	Kingler	Krabboss
0100	Voltorb	Voltorb	Voltorbe
0101	Electrode	Electrode	Électrode
0102	Exeggcute	Exeggcute	Noeunoeuf
0103	Exeggutor	Exeggutor	Noadkoko
0104	Cubone	Cubone	Osselait
0105	Marowak	Marowak	Ossatueur
0106	Hitmonlee	Hitmonlee	Kicklee
0107	Hitmonchan	Hitmonchan	Tygnon
0108	Lickitung	Lickitung	Excelangue
0109	Koffing	Koffing	Smogo
0110	Weezing	Weezing	Smogogo
0111	Rhyhorn	Rhyhorn	Rhinocorne
0112	Rhydon	Rhydon	Rhinoféros
0113	Chansey	Chansey	Leveinard
0114	Tangela	Tangela	Saquedeneu
0115	Kangaskhan	Kangaskhan	Kangourex
0116	Horsea	Horsea	Hypotrempe
0117	Seadra	Seadra	Hypocéan
0118	Goldeen	Goldeen	Poissirène
0119	Seaking	Seaking	Poissoroy
0120	Staryu	Staryu	Stari
0121	Starmie	Starmie	Staross
0122	Mr. Mime	Mr. Mime	M. Mime
0123	Scyther	Scyther	Insécateur
0124	Jynx	Jynx	Lippoutou
0125	Electabuzz	Electabuzz	Élektek
0126	Magmar	Magmar	Magmar
0127	Pinsir	Pinsir	Scarabrute
0128	Tauros	Tauros	Tauros
0129	Magikarp	Magikarp	Magicarpe
0130	Gyarados	Gyarados	Léviator
0131	Lapras	Lapras	Lokhlass
0132	Ditto	Ditto	Métamorph
0133	Eevee	Eevee	Évoli
0134	Vaporeon	Vaporeon	Aquali
0135	Jolteon	Jolteon	Voltali
0136	Flareon	Flareon	Pyroli
0137	Porygon	Porygon	Porygon
0138	Omanyte	Omanyte	Amonita
0139	Omastar	Omastar	Amonistar
0140	Kabuto	Kabuto	Kabuto
0141	Kabutops	Kabutops	Kabutops
0142	Aerodactyl	Aerodactyl	Ptéra
0143	Snorlax	Snorlax	Ronflex
0144	Articuno	Articuno	Artikodin
0145	Zapdos	Zapdos	Électhor
0146	Moltres	Moltres	Sulfura
0147	Dratini	Dratini	Minidraco
0148	Dragonair	Dragonair	Draco
0149	Dragonite	Dragonite	Dracolosse
0150	Mewtwo	Mewtwo	Mewtwo
0151	Mew	Mew	Mew
0152	Chikorita	Chikorita	Germignon
0153	Bayleef	Bayleef	Macronium
0154	Meganium	Meganium	Méganium
0155	Cyndaquil	Cyndaquil	Héricendre
0156	Quilava	Quilava	Feurisson
0157	Typhlosion	Typhlosion	Typhlosion
0158	Totodile	Totodile	Kaiminus
0159	Croconaw	Croconaw	Crocrodil
0160	Feraligatr	Feraligatr	Aligatueur
0161	Sentret	Sentret	Fouinette
0162	Furret	Furret	Fouinar
0163	Hoothoot	Hoothoot	Hoothoot
0164	Noctowl	Noctowl	Noarfang
0165	Ledyba	Ledyba	Coxy
0166	Ledian	Ledian	Coxyclaque
0167	Spinarak	Spinarak	Mimigal
0168	Ariados	Ariados	Migalos
0169	Crobat	Crobat	Nostenfer
0170	Chinchou	Chinchou	Loupio
0171	Lanturn	Lanturn	Lanturn
0172	Pichu	Pichu	Pichu
0173	Cleffa	Cleffa	Mélo
0174	Igglybuff	Igglybuff	Toudoudou
0175	Togepi	Togepi	Togepi
0176	Togetic	Togetic	Togetic
0177	Natu	Natu	Natu
0178	Xatu	Xatu	Xatu
0179	Mareep	Mareep	Wattouat
0180	Flaaffy	Flaaffy	Lainergie
0181	Ampharos	Ampharos	Pharamp
0182	Bellossom	Bellossom	Joliflor
0183	Marill	Marill	Marill
0184	Azumarill	Azumarill	Azumarill
0185	Sudowoodo	Sudowoodo	Simularbre
0186	Politoed	Politoed	Tarpaud
0187	Hoppip	Hoppip	Granivol
0188	Skiploom	Skiploom	Floravol
0189	Jumpluff	Jumpluff	Cotovol
0190	Aipom	Aipom	Capumain
0191	Sunkern	Sunkern	Tournegrin
0192	Sunflora	Sunflora	Héliatronc
0193	Yanma	Yanma	Yanma
0194	Wooper	Wooper	Axoloto
0195	Quagsire	Quagsire	Maraiste
0196	Espeon	Espeon	Mentali
0197	Umbreon	Umbreon	Noctali
0198	Murkrow	Murkrow	Cornèbre
0199	Slowking	Slowking	Roigada
0200	Misdreavus	Misdreavus	Feuforêve
0201	Unown	Unown	Zarbi
0202	Wobbuffet	Wobbuffet	Qulbutoké
0203	Girafarig	Girafarig	Girafarig
0204	Pineco	Pineco	Pomdepik
0205	Forretress	Forretress	Foretress
0206	Dunsparce	Dunsparce	Insolourdo
0207	Gligar	Gligar	Scorplane
0208	Steelix	Steelix	Steelix
0209	Snubbull	Snubbull	Snubbull
0210	Granbull	Granbull	Granbull
0211	Qwilfish	Qwilfish	Qwilfish
0212	Scizor	Scizor	Cizayox
0213	Shuckle	Shuckle	Caratroc
0214	Heracross	Heracross	Scarhino
0215	Sneasel	Sneasel	Farfuret
0216	Teddiursa	Teddiursa	Teddiursa
0217	Ursaring	Ursaring	Ursaring
0218	Slugma	Slugma	Limagma
0219	Magcargo	Magcargo	Volcaropod
0220	Swinub	Swinub	Marcacrin
0221	Piloswine	Piloswine	Cochignon
0222	Corsola	Corsola	Corayon
0223	Remoraid	Remoraid	Rémoraid
0224	Octillery	Octillery	Octillery
0225	Delibird	Delibird	Cadoizo
0226	Mantine	Mantine	Démanta
0227	Skarmory	Skarmory	Airmure
0228	Houndour	Houndour	Malosse
0229	Houndoom	Houndoom	Démolosse
0230	Kingdra	Kingdra	Hyporoi
0231	Phanpy	Phanpy	Phanpy
0232	Donphan	Donphan	Donphan
0233	Porygon2	Porygon2	Porygon2
0234	Stantler	Stantler	Cerfrousse
0235	Smeargle	Smeargle	Queulorior
0236	Tyrogue	Tyrogue	Debugant
0237	Hitmontop	Hitmontop	Kapoera
0238	Smoochum	Smoochum	Lippouti
0239	Elekid	Elekid	Élekid
0240	Magby	Magby	Magby
0241	Miltank	Miltank	Écrémeuh
0242	Blissey	Blissey	Leuphorie
0243	Raikou	Raikou	Raikou
0244	Entei	Entei	Entei
0245	Suicune	Suicune	Suicune
0246	Larvitar	Larvitar	Embrylex
0247	Pupitar	Pupitar	Ymphect
0248	Tyranitar	Tyranitar	Tyranocif
0249	Lugia	Lugia	Lugia
0250	Ho-Oh	Ho-Oh	Ho-Oh
0251	Celebi	Celebi	Celebi
0252	Treecko	Treecko	Arcko
0253	Grovyle	Grovyle	Massko
0254	Sceptile	Sceptile	Jungko
0255	Torchic	Torchic	Poussifeu
0256	Combusken	Combusken	Galifeu
0257	Blaziken	Blaziken	Braségali
0258	Mudkip	Mudkip	Gobou
0259	Marshtomp	Marshtomp	Flobio
0260	Swampert	Swampert	Laggron
0261	Poochyena	Poochyena	Medhyèna
0262	Mightyena	Mightyena	Grahyèna
0263	Zigzagoon	Zigzagoon	Zigzaton
0264	Linoone	Linoone	Linéon
0265	Wurmple	Wurmple	Chenipotte
0266	Silcoon	Silcoon	Armulys
0267	Beautifly	Beautifly	Charmillon
0268	Cascoon	Cascoon	Blindalys
0269	Dustox	Dustox	Papinox
0270	Lotad	Lotad	Nénupiot
0271	Lombre	Lombre	Lombre
0272	Ludicolo	Ludicolo	Ludicolo
0273	Seedot	Seedot	Grainipiot
0274	Nuzleaf	Nuzleaf	Pifeuil
0275	Shiftry	Shiftry	Tengalice
0276	Taillow	Taillow	Nirondelle
0277	Swellow	Swellow	Hélédelle
0278	Wingull	Wingull	Goélise
0279	Pelipper	Pelipper	Bekipan
0280	Ralts	Ralts	Tarsal
0281	Kirlia	Kirlia	Kirlia
0282	Gardevoir	Gardevoir	Gardevoir
0283	Surskit	Surskit	Arakdo
0284	Masquerain	Masquerain	Maskadra
0285	Shroomish	Shroomish	Balignon
0286	Breloom	Breloom	Chapignon
0287	Slakoth	Slakoth	Parecool
0288	Vigoroth	Vigoroth	Vigoroth
0289	Slaking	Slaking	Monaflèmit
0290	Nincada	Nincada	Ningale
0291	Ninjask	Ninjask	Ninjask
0292	Shedinja	Shedinja	Munja
0293	Whismur	Whismur	Chuchmur
0294	Loudred	Loudred	Ramboum
0295	Exploud	Exploud	Brouhabam
0296	Makuhita	Makuhita	Makuhita
0297	Hariyama	Hariyama	Hariyama
0298	Azurill	Azurill	Azurill
0299	Nosepass	Nosepass	Tarinor
0300	Skitty	Skitty	Skitty
0301	Delcatty	Delcatty	Delcatty
0302	Sableye	Sableye	Ténéfix
0303	Mawile	Mawile	Mysdibule
0304	Aron	Aron	Galekid
0305	Lairon	Lairon	Galegon
0306	Aggron	Aggron	Galeking
0307	Meditite	Meditite	Méditikka
0308	Medicham	Medicham	Charmina
0309	Electrike	Electrike	Dynavolt
0310	Manectric	Manectric	Élecsprint
0311	Plusle	Plusle	Posipi
0312	Minun	Minun	Négapi
0313	Volbeat	Volbeat	Muciole
0314	Illumise	Illumise	Lumivole
0315	Roselia	Roselia	Rosélia
0316	Gulpin	Gulpin	Gloupti
0317	Swalot	Swalot	Avaltout
0318	Carvanha	Carvanha	Carvanha
0319	Sharpedo	Sharpedo	Sharpedo
0320	Wailmer	Wailmer	Wailmer
0321	Wailord	Wailord	Wailord
0322	Numel	Numel	Chamallot
0323	Camerupt	Camerupt	Camérupt
0324	Torkoal	Torkoal	Chartor
0325	Spoink	Spoink	Spoink
0326	Grumpig	Grumpig	Groret
0327	Spinda	Spinda	Spinda
0328	Trapinch	Trapinch	Kraknoix
0329	Vibrava	Vibrava	Vibraninf
0330	Flygon	Flygon	Libégon
0331	Cacnea	Cacnea	Cacnea
0332	Cacturne	Cacturne	Cacturne
0333	Swablu	Swablu	Tylton
0334	Altaria	Altaria	Altaria
0335	Zangoose	Zangoose	Mangriff
0336	Seviper	Seviper	Séviper
0337	Lunatone	Lunatone	Séléroc
0338	Solrock	Solrock	Solaroc
0339	Barboach	Barboach	Barloche
0340	Whiscash	Whiscash	Barbicha
0341	Corphish	Corphish	Écrapince
0342	Crawdaunt	Crawdaunt	Colhomard
0343	Baltoy	Baltoy	Balbuto
0344	Claydol	Claydol	Kaorine
0345	Lileep	Lileep	Lilia
0346	Cradily	Cradily	Vacilys
0347	Anorith	Anorith	Anorith
0348	Armaldo	Armaldo	Armaldo
0349	Feebas	Feebas	Barpau
0350	Milotic	Milotic	Milobellus
0351	Castform	Castform	Morphéo
0352	Kecleon	Kecleon	Kecleon
0353	Shuppet	Shuppet	Polichombr
0354	Banette	Banette	Branette
0355	Duskull	Duskull	Skelénox
0356	Dusclops	Dusclops	Téraclope
0357	Tropius	Tropius	Tropius
0358	Chimecho	Chimecho	Éoko
0359	Absol	Absol	Absol
0360	Wynaut	Wynaut	Okéoké
0361	Snorunt	Snorunt	Stalgamin
0362	Glalie	Glalie	Oniglali
0363	Spheal	Spheal	Obalie
0364	Sealeo	Sealeo	Phogleur
0365	Walrein	Walrein	Kaimorse
0366	Clamperl	Clamperl	Coquiperl
0367	Huntail	Huntail	Serpang
0368	Gorebyss	Gorebyss	Rosabyss
0369	Relicanth	Relicanth	Relicanth
0370	Luvdisc	Luvdisc	Lovdisc
0371	Bagon	Bagon	Draby
0372	Shelgon	Shelgon	Drackhaus
0373	Salamence	Salamence	Drattak
0374	Beldum	Beldum	Terhal
0375	Metang	Metang	Métang
0376	Metagross	Metagross	Métalosse
0377	Regirock	Regirock	Regirock
0378	Regice	Regice	Regice
0379	Registeel	Registeel	Registeel
0380	Latias	Latias	Latias
0381	Latios	Latios	Latios
0382	Kyogre	Kyogre	Kyogre
0383	Groudon	Groudon	Groudon
0384	Rayquaza	Rayquaza	Rayquaza
0385	Jirachi	Jirachi	Jirachi
0386	Deoxys	Deoxys	Deoxys
0387	Turtwig	Turtwig	Tortipouss
0388	Grotle	Grotle	Boskara
0389	Torterra	Torterra	Torterra
0390	Chimchar	Chimchar	Ouisticram
0391	Monferno	Monferno	Chimpenfeu
0392	Infernape	Infernape	Simiabraz
0393	Piplup	Piplup	Tiplouf
0394	Prinplup	Prinplup	Prinplouf
0395	Empoleon	Empoleon	Pingoléon
0396	Starly	Starly	Étourmi
0397	Staravia	Staravia	Étourvol
0398	Staraptor	Staraptor	Étouraptor
0399	Bidoof	Bidoof	Keunotor
0400	Bibarel	Bibarel	Castorno
0401	Kricketot	Kricketot	Crikzik
0402	Kricketune	Kricketune	Mélokrik
0403	Shinx	Shinx	Lixy
0404	Luxio	Luxio	Luxio
0405	Luxray	Luxray	Luxray
0406	Budew	Budew	Rozbouton
0407	Roserade	Roserade	Roserade
0408	Cranidos	Cranidos	Kranidos
0409	Rampardos	Rampardos	Charkos
0410	Shieldon	Shieldon	Dinoclier
0411	Bastiodon	Bastiodon	Bastiodon
0412	Burmy	Burmy	Cheniti
0413	Wormadam	Wormadam	Cheniselle
0414	Mothim	Mothim	Papilord
0415	Combee	Combee	Apitrini
0416	Vespiquen	Vespiquen	Apireine
0417	Pachirisu	Pachirisu	Pachirisu
0418	Buizel	Buizel	Mustébouée
0419	Floatzel	Floatzel	Mustéflott
0420	Cherubi	Cherubi	Ceribou
0421	Cherrim	Cherrim	Ceriflor
0422	Shellos	Shellos	Sancoki
0423	Gastrodon	Gastrodon	Tritosor
0424	Ambipom	Ambipom	Capidextre
0425	Drifloon	Drifloon	Baudrive
0426	Drifblim	Drifblim	Grodrive
0427	Buneary	Buneary	Laporeille
0428	Lopunny	Lopunny	Lockpin
0429	Mismagius	Mismagius	Magirêve
0430	Honchkrow	Honchkrow	Corboss
0431	Glameow	Glameow	Chaglam
0432	Purugly	Purugly	Chaffreux
0433	Chingling	Chingling	Korillon
0434	Stunky	Stunky	Moufouette
0435	Skuntank	Skuntank	Moufflair
0436	Bronzor	Bronzor	Archéomire
0437	Bronzong	Bronzong	Archéodong
0438	Bonsly	Bonsly	Manzaï
0439	Mime Jr.	Mime Jr.	Mime Jr.
0440	Happiny	Happiny	Ptiravi
0441	Chatot	Chatot	Pijako
0442	Spiritomb	Spiritomb	Spiritomb
0443	Gible	Gible	Griknot
0444	Gabite	Gabite	Carmache
0445	Garchomp	Garchomp	Carchacrok
0446	Munchlax	Munchlax	Goinfrex
0447	Riolu	Riolu	Riolu
0448	Lucario	Lucario	Lucario
0449	Hippopotas	Hippopotas	Hippopotas
0450	Hippowdon	Hippowdon	Hippodocus
0451	Skorupi	Skorupi	Rapion
0452	Drapion	Drapion	Drascore
0453	Croagunk	Croagunk	Cradopaud
0454	Toxicroak	Toxicroak	Coatox
0455	Carnivine	Carnivine	Vortente
0456	Finneon	Finneon	Écayon
0457	Lumineon	Lumineon	Luminéon
0458	Mantyke	Mantyke	Babimanta
0459	Snover	Snover	Blizzi
0460	Abomasnow	Abomasnow	Blizzaroi
0461	Weavile	Weavile	Dimoret
0462	Magnezone	Magnezone	Magnézone
0463	Lickilicky	Lickilicky	Coudlangue
0464	Rhyperior	Rhyperior	Rhinastoc
0465	Tangrowth	Tangrowth	Bouldeneu
0466	Electivire	Electivire	Élekable
0467	Magmortar	Magmortar	Maganon
0468	Togekiss	Togekiss	Togekiss
0469	Yanmega	Yanmega	Yanméga
0470	Leafeon	Leafeon	Phyllali
0471	Glaceon	Glaceon	Givrali
0472	Gliscor	Gliscor	Scorvol
0473	Mamoswine	Mamoswine	Mammochon
0474	Porygon-Z	Porygon-Z	Porygon-Z
0475	Gallade	Gallade	Gallame
0476	Probopass	Probopass	Tarinorme
0477	Dusknoir	Dusknoir	Noctunoir
0478	Froslass	Froslass	Momartik
0479	Rotom	Rotom	Motisma
0480	Uxie	Uxie	Créhelf
0481	Mesprit	Mesprit	Créfollet
0482	Azelf	Azelf	Créfadet
0483	Dialga	Dialga	Dialga
0484	Palkia	Palkia	Palkia
0485	Heatran	Heatran	Heatran
0486	Regigigas	Regigigas	Regigigas
0487	Giratina	Giratina	Giratina
0488	Cresselia	Cresselia	Cresselia
0489	Phione	Phione	Phione
0490	Manaphy	Manaphy	Manaphy
0491	Darkrai	Darkrai	Darkrai
0492	Shaymin	Shaymin	Shaymin
0493	Arceus	Arceus	Arceus
0494	Victini	Victini	Victini
0495	Snivy	Snivy	Vipélierre
0496	Servine	Servine	Lianaja
0497	Serperior	Serperior	Majaspic
0498	Tepig	Tepig	Gruikui
0499	Pignite	Pignite	Grotichon
0500	Emboar	Emboar	Roitiflam
0501	Oshawott	Oshawott	Moustillon
0502	Dewott	Dewott	Mateloutre
0503	Samurott	Samurott	Clamiral
0504	Patrat	Patrat	Ratentif
0505	Watchog	Watchog	Miradar
0506	Lillipup	Lillipup	Ponchiot
0507	Herdier	Herdier	Ponchien
0508	Stoutland	Stoutland	Mastouffe
0509	Purrloin	Purrloin	Chacripan
0510	Liepard	Liepard	Léopardus
0511	Pansage	Pansage	Feuillajou
0512	Simisage	Simisage	Feuiloutan
0513	Pansear	Pansear	Flamajou
0514	Simisear	Simisear	Flamoutan
0515	Panpour	Panpour	Flotajou
0516	Simipour	Simipour	Flotoutan
0517	Munna	Munna	Munna
0518	Musharna	Musharna	Mushana
0519	Pidove	Pidove	Poichigeon
0520	Tranquill	Tranquill	Colombeau
0521	Unfezant	Unfezant	Déflaisan
0522	Blitzle	Blitzle	Zébribon
0523	Zebstrika	Zebstrika	Zéblitz
0524	Roggenrola	Roggenrola	Nodulithe
0525	Boldore	Boldore	Géolithe
0526	Gigalith	Gigalith	Gigalithe
0527	Woobat	Woobat	Chovsourir
0528	Swoobat	Swoobat	Rhinolove
0529	Drilbur	Drilbur	Rototaupe
0530	Excadrill	Excadrill	Minotaupe
0531	Audino	Audino	Nanméouïe
0532	Timburr	Timburr	Charpenti
0533	Gurdurr	Gurdurr	Ouvrifier
0534	Conkeldurr	Conkeldurr	Bétochef
0535	Tympole	Tympole	Tritonde
0536	Palpitoad	Palpitoad	Batracné
0537	Seismitoad	Seismitoad	Crapustule
0538	Throh	Throh	Judokrak
0539	Sawk	Sawk	Karaclée
0540	Sewaddle	Sewaddle	Larveyette
0541	Swadloon	Swadloon	Couverdure
0542	Leavanny	Leavanny	Manternel
0543	Venipede	Venipede	Venipatte
0544	Whirlipede	Whirlipede	Scobolide
0545	Scolipede	Scolipede	Brutapode
0546	Cottonee	Cottonee	Doudouvet
0547	Whimsicott	Whimsicott	Farfaduvet
0548	Petilil	Petilil	Chlorobule
0549	Lilligant	Lilligant	Fragilady
0550	Basculin	Basculin	Bargantua
0551	Sandile	Sandile	Mascaïman
0552	Krokorok	Krokorok	Escroco
0553	Krookodile	Krookodile	Crocorible
0554	Darumaka	Darumaka	Darumarond
0555	Darmanitan	Darmanitan	Darumacho
0556	Maractus	Maractus	Maracachi
0557	Dwebble	Dwebble	Crabicoque
0558	Crustle	Crustle	Crabaraque
0559	Scraggy	Scraggy	Baggiguane
0560	Scrafty	Scrafty	Baggaïd
0561	Sigilyph	Sigilyph	Cryptéro
0562	Yamask	Yamask	Tutafeh
0563	Cofagrigus	Cofagrigus	Tutankafer
0564	Tirtouga	Tirtouga	Carapagos
0565	Carracosta	Carracosta	Mégapagos
0566	Archen	Archen	Arkéapti
0567	Archeops	Archeops	Aéroptéryx
0568	Trubbish	Trubbish	Miamiasme
0569	Garbodor	Garbodor	Miasmax
0570	Zorua	Zorua	Zorua
0571	Zoroark	Zoroark	Zoroark
0572	Minccino	Minccino	Chinchidou
0573	Cinccino	Cinccino	Pashmilla
0574	Gothita	Gothita	Scrutella
0575	Gothorita	Gothorita	Mesmérella
0576	Gothitelle	Gothitelle	Sidérella
0577	Solosis	Solosis	Nucléos
0578	Duosion	Duosion	Méios
0579	Reuniclus	Reuniclus	Symbios
0580	Ducklett	Ducklett	Couaneton
0581	Swanna	Swanna	Lakmécygne
0582	Vanillite	Vanillite	Sorbébé
0583	Vanillish	Vanillish	Sorboul
0584	Vanilluxe	Vanilluxe	Sorbouboul
0585	Deerling	Deerling	Vivaldaim
0586	Sawsbuck	Sawsbuck	Haydaim
0587	Emolga	Emolga	Emolga
0588	Karrablast	Karrablast	Carabing
0589	Escavalier	Escavalier	Lançargot
0590	Foongus	Foongus	Trompignon
0591	Amoonguss	Amoonguss	Gaulet
0592	Frillish	Frillish	Viskuse
0593	Jellicent	Jellicent	Moyade
0594	Alomomola	Alomomola	Mamanbo
0595	Joltik	Joltik	Statitik
0596	Galvantula	Galvantula	Mygavolt
0597	Ferroseed	Ferroseed	Grindur
0598	Ferrothorn	Ferrothorn	Noacier
0599	Klink	Klink	Tic
0600	Klang	Klang	Clic
0601	Klinklang	Klinklang	Cliticlic
0602	Tynamo	Tynamo	Anchwatt
0603	Eelektrik	Eelektrik	Lampéroie
0604	Eelektross	Eelektross	Ohmassacre
0605	Elgyem	Elgyem	Lewsor
0606	Beheeyem	Beheeyem	Neitram
0607	Litwick	Litwick	Funécire
0608	Lampent	Lampent	Mélancolux
0609	Chandelure	Chandelure	Lugulabre
0610	Axew	Axew	Coupenotte
0611	Fraxure	Fraxure	Incisache
0612	Haxorus	Haxorus	Tranchodon
0613	Cubchoo	Cubchoo	Polarhume
0614	Beartic	Beartic	Polagriffe
0615	Cryogonal	Cryogonal	Hexagel
0616	Shelmet	Shelmet	Escargaume
0617	Accelgor	Accelgor	Limaspeed
0618	Stunfisk	Stunfisk	Limonde
0619	Mienfoo	Mienfoo	Kungfouine
0620	Mienshao	Mienshao	Shaofouine
0621	Druddigon	Druddigon	Drakkarmin
0622	Golett	Golett	Gringolem
0623	Golurk	Golurk	Golemastoc
0624	Pawniard	Pawniard	Scalpion
0625	Bisharp	Bisharp	Scalproie
0626	Bouffalant	Bouffalant	Frison
0627	Rufflet	Rufflet	Furaiglon
0628	Braviary	Braviary	Gueriaigle
0629	Vullaby	Vullaby	Vostourno
0630	Mandibuzz	Mandibuzz	Vaututrice
0631	Heatmor	Heatmor	Aflamanoir
0632	Durant	Durant	Fermite
0633	Deino	Deino	Solochi
0634	Zweilous	Zweilous	Diamat
0635	Hydreigon	Hydreigon	Trioxhydre
0636	Larvesta	Larvesta	Pyronille
0637	Volcarona	Volcarona	Pyrax
0638	Cobalion	Cobalion	Cobaltium
0639	Terrakion	Terrakion	Terrakium
0640	Virizion	Virizion	Viridium
0641	Tornadus	Tornadus	Boréas
0642	Thundurus	Thundurus	Fulguris
0643	Reshiram	Reshiram	Reshiram
0644	Zekrom	Zekrom	Zekrom
0645	Landorus	Landorus	Démétéros
0646	Kyurem	Kyurem	Kyurem
0647	Keldeo	Keldeo	Keldeo
0648	Meloetta	Meloetta	Meloetta
0649	Genesect	Genesect	Genesect
0650	Chespin	Chespin	Marisson
0651	Quilladin	Quilladin	Boguérisse
0652	Chesnaught	Chesnaught	Blindépique
0653	Fennekin	Fennekin	Feunnec
0654	Braixen	Braixen	Roussil
0655	Delphox	Delphox	Goupelin
0656	Froakie	Froakie	Grenousse
0657	Frogadier	Frogadier	Croâporal
0658	Greninja	Greninja	Amphinobi
0659	Bunnelby	Bunnelby	Sapereau
0660	Diggersby	Diggersby	Excavarenne
0661	Fletchling	Fletchling	Passerouge
0662	Fletchinder	Fletchinder	Braisillon
0663	Talonflame	Talonflame	Flambusard
0664	Scatterbug	Scatterbug	Lépidonille
0665	Spewpa	Spewpa	Pérégrain
0666	Vivillon	Vivillon	Prismillon
0667	Litleo	Litleo	Hélionceau
0668	Pyroar	Pyroar	Némélios
0669	Flabébé	Flabébé	Flabébé
0670	Floette	Floette	Floette
0671	Florges	Florges	Florges
0672	Skiddo	Skiddo	Cabriolaine
0673	Gogoat	Gogoat	Chevroum
0674	Pancham	Pancham	Pandespiègle
0675	Pangoro	Pangoro	Pandarbare
0676	Furfrou	Furfrou	Couafarel
0677	Espurr	Espurr	Psystigri
0678	Meowstic	Meowstic	Mistigrix
0679	Honedge	Honedge	Monorpale
0680	Doublade	Doublade	Dimoclès
0681	Aegislash	Aegislash	Exagide
0682	Spritzee	Spritzee	Fluvetin
0683	Aromatisse	Aromatisse	Cocotine
0684	Swirlix	Swirlix	Sucroquin
0685	Slurpuff	Slurpuff	Cupcanaille
0686	Inkay	Inkay	Sepiatop
0687	Malamar	Malamar	Sepiatroce
0688	Binacle	Binacle	Opermine
0689	Barbaracle	Barbaracle	Golgopathe
0690	Skrelp	Skrelp	Venalgue
0691	Dragalge	Dragalge	Kravarech
0692	Clauncher	Clauncher	Flingouste
0693	Clawitzer	Clawitzer	Gamblast
0694	Helioptile	Helioptile	Galvaran
0695	Heliolisk	Heliolisk	Iguolta
0696	Tyrunt	Tyrunt	Ptyranidur
0697	Tyrantrum	Tyrantrum	Rexillius
0698	Amaura	Amaura	Amagara
0699	Aurorus	Aurorus	Dragmara
0700	Sylveon	Sylveon	Nymphali
0701	Hawlucha	Hawlucha	Brutalibré
0702	Dedenne	Dedenne	Dedenne
0703	Carbink	Carbink	Strassie
0704	Goomy	Goomy	Mucuscule
0705	Sliggoo	Sliggoo	Colimucus
0706	Goodra	Goodra	Muplodocus
0707	Klefki	Klefki	Trousselin
0708	Phantump	Phantump	Brocélôme
0709	Trevenant	Trevenant	Desséliande
0710	Pumpkaboo	Pumpkaboo	Pitrouille
0711	Gourgeist	Gourgeist	Banshitrouye
0712	Bergmite	Bergmite	Grelaçon
0713	Avalugg	Avalugg	Séracrawl
0714	Noibat	Noibat	Sonistrelle
0715	Noivern	Noivern	Bruyverne
0716	Xerneas	Xerneas	Xerneas
0717	Yveltal	Yveltal	Yveltal
0718	Zygarde	Zygarde	Zygarde
0719	Diancie	Diancie	Diancie
0720	Hoopa	Hoopa	Hoopa
0721	Volcanion	Volcanion	Volcanion
0722	Rowlet	Rowlet	Brindibou
0723	Dartrix	Dartrix	Efflèche
0724	Decidueye	Decidueye	Archéduc
0725	Litten	Litten	Flamiaou
0726	Torracat	Torracat	Matoufeu
0727	Incineroar	Incineroar	Félinferno
0728	Popplio	Popplio	Otaquin
0729	Brionne	Brionne	Otarlette
0730	Primarina	Primarina	Oratoria
0731	Pikipek	Pikipek	Picassaut
0732	Trumbeak	Trumbeak	Piclairon
0733	Toucannon	Toucannon	Bazoucan
0734	Yungoos	Yungoos	Manglouton
0735	Gumshoos	Gumshoos	Argouste
0736	Grubbin	Grubbin	Larvibule
0737	Charjabug	Charjabug	Chrysapile
0738	Vikavolt	Vikavolt	Lucanon
0739	Crabrawler	Crabrawler	Crabagarre
0740	Crabominable	Crabominable	Crabominable
0741	Oricorio	Oricorio	Plumeline
0742	Cutiefly	Cutiefly	Bombydou
0743	Ribombee	Ribombee	Rubombelle
0744	Rockruff	Rockruff	Rocabot
0745	Lycanroc	Lycanroc	Lougaroc
0746	Wishiwashi	Wishiwashi	Froussardine
0747	Mareanie	Mareanie	Vorastérie
0748	Toxapex	Toxapex	Prédastérie
0749	Mudbray	Mudbray	Tiboudet
0750	Mudsdale	Mudsdale	Bourrinos
0751	Dewpider	Dewpider	Araqua
0752	Araquanid	Araquanid	Tarenbulle
0753	Fomantis	Fomantis	Mimantis
0754	Lurantis	Lurantis	Floramantis
0755	Morelull	Morelull	Spododo
0756	Shiinotic	Shiinotic	Lampignon
0757	Salandit	Salandit	Tritox
0758	Salazzle	Salazzle	Malamandre
0759	Stufful	Stufful	Nounourson
0760	Bewear	Bewear	Chelours
0761	Bounsweet	Bounsweet	Croquine
0762	Steenee	Steenee	Candine
0763	Tsareena	Tsareena	Sucreine
0764	Comfey	Comfey	Guérilande
0765	Oranguru	Oranguru	Gouroutan
0766	Passimian	Passimian	Quartermac
0767	Wimpod	Wimpod	Sovkipou
0768	Golisopod	Golisopod	Sarmuraï
0769	Sandygast	Sandygast	Bacabouh
0770	Palossand	Palossand	Trépassable
0771	Pyukumuku	Pyukumuku	Concombaffe
0772	Type: Null	Type: Null	Type:0
0773	Silvally	Silvally	Silvallié
0774	Minior	Minior	Météno
0775	Komala	Komala	Dodoala
0776	Turtonator	Turtonator	Boumata
0777	Togedemaru	Togedemaru	Togedemaru
0778	Mimikyu	Mimikyu	Mimiqui
0779	Bruxish	Bruxish	Denticrisse
0780	Drampa	Drampa	Draïeul
0781	Dhelmise	Dhelmise	Sinistrail
0782	Jangmo-o	Jangmo-o	Bébécaille
0783	Hakamo-o	Hakamo-o	Écaïd
0784	Kommo-o	Kommo-o	Ékaïser
0785	Tapu Koko	Tapu Koko	Tokorico
0786	Tapu Lele	Tapu Lele	Tokopiyon
0787	Tapu Bulu	Tapu Bulu	Tokotoro
0788	Tapu Fini	Tapu Fini	Tokopisco
0789	Cosmog	Cosmog	Cosmog
0790	Cosmoem	Cosmoem	Cosmovum
0791	Solgaleo	Solgaleo	Solgaleo
0792	Lunala	Lunala	Lunala
0793	Nihilego	Nihilego	Zéroïd
0794	Buzzwole	Buzzwole	Mouscoto
0795	Pheromosa	Pheromosa	Cancrelove
0796	Xurkitree	Xurkitree	Câblifère
0797	Celesteela	Celesteela	Bamboiselle
0798	Kartana	Kartana	Katagami
0799	Guzzlord	Guzzlord	Engloutyran
0800	Necrozma	Necrozma	Necrozma
0801	Magearna	Magearna	Magearna
0802	Marshadow	Marshadow	Marshadow
0803	Poipole	Poipole	Vémini
0804	Naganadel	Naganadel	Mandrillon
0805	Stakataka	Stakataka	Ama-Ama
0806	Blacephalon	Blacephalon	Pierroteknik
0807	Zeraora	Zeraora	Zeraora
0808	Meltan	Meltan	Meltan
0809	Melmetal	Melmetal	Melmetal
0810	Grookey	Grookey	Ouistempo
0811	Thwackey	Thwackey	Badabouin
0812	Rillaboom	Rillaboom	Gorythmic
0813	Scorbunny	Scorbunny	Flambino
0814	Raboot	Raboot	Lapyro
0815	Cinderace	Cinderace	Pyrobut
0816	Sobble	Sobble	Larméléon
0817	Drizzile	Drizzile	Arrozard
0818	Inteleon	Inteleon	Lézargus
0819	Skwovet	Skwovet	Rongourmand
0820	Greedent	Greedent	Rongrigou
0821	Rookidee	Rookidee	Minisange
0822	Corvisquire	Corvisquire	Bleuseille
0823	Corviknight	Corviknight	Corvaillus
0824	Blipbug	Blipbug	Larvadar
0825	Dottler	Dottler	Coléodôme
0826	Orbeetle	Orbeetle	Astronelle
0827	Nickit	Nickit	Goupilou
0828	Thievul	Thievul	Roublenard
0829	Gossifleur	Gossifleur	Tournicoton
0830	Eldegoss	Eldegoss	Blancoton
0831	Wooloo	Wooloo	Moumouton
0832	Dubwool	Dubwool	Moumouflon
0833	Chewtle	Chewtle	Khélocrok
0834	Drednaw	Drednaw	Torgamord
0835	Yamper	Yamper	Voltoutou
0836	Boltund	Boltund	Fulgudog
0837	Rolycoly	Rolycoly	Charbi
0838	Carkol	Carkol	Wagomine
0839	Coalossal	Coalossal	Monthracite
0840	Applin	Applin	Verpom
0841	Flapple	Flapple	Pomdrapi
0842	Appletun	Appletun	Dratatin
0843	Silicobra	Silicobra	Dunaja
0844	Sandaconda	Sandaconda	Dunaconda
0845	Cramorant	Cramorant	Nigosier
0846	Arrokuda	Arrokuda	Embrochet
0847	Barraskewda	Barraskewda	Hastacuda
0848	Toxel	Toxel	Toxizap
0849	Toxtricity	Toxtricity	Salarsen
0850	Sizzlipede	Sizzlipede	Grillepattes
0851	Centiskorch	Centiskorch	Scolocendre
0852	Clobbopus	Clobbopus	Poulpaf
0853	Grapploct	Grapploct	Krakos
0854	Sinistea	Sinistea	Théffroi
0855	Polteageist	Polteageist	Polthégeist
0856	Hatenna	Hatenna	Bibichut
0857	Hattrem	Hattrem	Chapotus
0858	Hatterene	Hatterene	Sorcilence
0859	Impidimp	Impidimp	Grimalin
0860	Morgrem	Morgrem	Fourbelin
0861	Grimmsnarl	Grimmsnarl	Angoliath
0862	Obstagoon	Obstagoon	Ixon
0863	Perrserker	Perrserker	Berserkatt
0864	Cursola	Cursola	Corayôme
0865	Sirfetch'd	Sirfetch'd	Palarticho
0866	Mr. Rime	Mr. Rime	M. Glaquette
0867	Runerigus	Runerigus	Tutétékri
0868	Milcery	Milcery	Crèmy
0869	Alcremie	Alcremie	Charmilly
0870	Falinks	Falinks	Hexadron
0871	Pincurchin	Pincurchin	Wattapik
0872	Snom	Snom	Frissonille
0873	Frosmoth	Frosmoth	Beldeneige
0874	Stonjourner	Stonjourner	Dolman
0875	Eiscue	Eiscue	Bekaglaçon
0876	Indeedee	Indeedee	Wimessir
0877	Morpeko	Morpeko	Morpeko
0878	Cufant	Cufant	Charibari
0879	Copperajah	Copperajah	Pachyradjah
0880	Dracozolt	Dracozolt	Galvagon
0881	Arctozolt	Arctozolt	Galvagla
0882	Dracovish	Dracovish	Hydragon
0883	Arctovish	Arctovish	Hydragla
0884	Duraludon	Duraludon	Duralugon
0885	Dreepy	Dreepy	Fantyrm
0886	Drakloak	Drakloak	Dispareptil
0887	Dragapult	Dragapult	Lanssorien
0888	Zacian	Zacian	Zacian
0889	Zamazenta	Zamazenta	Zamazenta
0890	Eternatus	Eternatus	Éthernatos
0891	Kubfu	Kubfu	Wushours
0892	Urshifu	Urshifu	Shifours
0893	Zarude	Zarude	Zarude
0894	Regieleki	Regieleki	Regieleki
0895	Regidrago	Regidrago	Regidrago
0896	Glastrier	Glastrier	Blizzeval
0897	Spectrier	Spectrier	Spectreval
0898	Calyrex	Calyrex	Sylveroy
0899	Wyrdeer	Wyrdeer	Cerbyllin
0900	Kleavor	Kleavor	Hachécateur
0901	Ursaluna	Ursaluna	Ursaking
0902	Basculegion	Basculegion	Paragruel
0903	Sneasler	Sneasler	Farfurex
0904	Overqwil	Overqwil	Qwilpik
0905	Enamorus	Enamorus	Amovénus
0906	Sprigatito	Sprigatito	Poussacha
0907	Floragato	Floragato	Matourgeon
0908	Meowscarada	Meowscarada	Miascarade
0909	Fuecoco	Fuecoco	Chochodile
0910	Crocalor	Crocalor	Crocogril
0911	Skeledirge	Skeledirge	Flâmigator
0912	Quaxly	Quaxly	Coiffeton
0913	Quaxwell	Quaxwell	Canarbello
0914	Quaquaval	Quaquaval	Palmaval
0915	Lechonk	Lechonk	Gourmelet
0916	Oinkologne	Oinkologne	Fragroin
0917	Tarountula	Tarountula	Tissenboule
0918	Spidops	Spidops	Filentrappe
0919	Nymble	Nymble	Lilliterelle
0920	Lokix	Lokix	Gambex
0921	Pawmi	Pawmi	Pohm
0922	Pawmo	Pawmo	Pohmotte
0923	Pawmot	Pawmot	Pohmarmotte
0924	Tandemaus	Tandemaus	Compagnol
0925	Maushold	Maushold	Famignol
0926	Fidough	Fidough	Pâtachiot
0927	Dachsbun	Dachsbun	Briochien
0928	Smoliv	Smoliv	Olivini
0929	Dolliv	Dolliv	Olivado
0930	Arboliva	Arboliva	Arboliva
0931	Squawkabilly	Squawkabilly	Tapatoès
0932	Nacli	Nacli	Selutin
0933	Naclstack	Naclstack	Amassel
0934	Garganacl	Garganacl	Gigansel
0935	Charcadet	Charcadet	Charbambin
0936	Armarouge	Armarouge	Carmadura
0937	Ceruledge	Ceruledge	Malvalame
0938	Tadbulb	Tadbulb	Têtampoule
0939	Bellibolt	Bellibolt	Ampibidou
0940	Wattrel	Wattrel	Zapétrel
0941	Kilowattrel	Kilowattrel	Fulgulairo
0942	Maschiff	Maschiff	Grondogue
0943	Mabosstiff	Mabosstiff	Dogrino
0944	Shroodle	Shroodle	Gribouraigne
0945	Grafaiai	Grafaiai	Tag-Tag
0946	Bramblin	Bramblin	Virovent
0947	Brambleghast	Brambleghast	Virevorreur
0948	Toedscool	Toedscool	Terracool
0949	Toedscruel	Toedscruel	Terracruel
0950	Klawf	Klawf	Craparoi
0951	Capsakid	Capsakid	Pimito
0952	Scovillain	Scovillain	Scovilain
0953	Rellor	Rellor	Léboulérou
0954	Rabsca	Rabsca	Bérasca
0955	Flittle	Flittle	Flotillon
0956	Espathra	Espathra	Cléopsytra
0957	Tinkatink	Tinkatink	Forgerette
0958	Tinkatuff	Tinkatuff	Forgella
0959	Tinkaton	Tinkaton	Forgelina
0960	Wiglett	Wiglett	Taupikeau
0961	Wugtrio	Wugtrio	Triopikeau
0962	Bombirdier	Bombirdier	Lestombaile
0963	Finizen	Finizen	Dofin
0964	Palafin	Palafin	Superdofin
0965	Varoom	Varoom	Vrombi
0966	Revavroom	Revavroom	Vrombotor
0967	Cyclizar	Cyclizar	Motorizard
0968	Orthworm	Orthworm	Ferdeter
0969	Glimmet	Glimmet	Germéclat
0970	Glimmora	Glimmora	Floréclat
0971	Greavard	Greavard	Toutombe
0972	Houndstone	Houndstone	Tomberro
0973	Flamigo	Flamigo	Flamenroule
0974	Cetoddle	Cetoddle	Piétacé
0975	Cetitan	Cetitan	Balbalèze
0976	Veluza	Veluza	Délestin
0977	Dondozo	Dondozo	Oyacata
0978	Tatsugiri	Tatsugiri	Nigirigon
0979	Annihilape	Annihilape	Courrousinge
0980	Clodsire	Clodsire	Terraiste
0981	Farigiraf	Farigiraf	Farigiraf
0982	Dudunsparce	Dudunsparce	Deusolourdo
0983	Kingambit	Kingambit	Scalpereur
0984	Great Tusk	Great Tusk	Fort-Ivoire
0985	Scream Tail	Scream Tail	Hurle-Queue
0986	Brute Bonnet	Brute Bonnet	Fongus-Furie
0987	Flutter Mane	Flutter Mane	Flotte-Mèche
0988	Slither Wing	Slither Wing	Rampe-Ailes
0989	Sandy Shocks	Sandy Shocks	Pelage-Sablé
0990	Iron Treads	Iron Treads	Roue-de-Fer
0991	Iron Bundle	Iron Bundle	Hotte-de-Fer
0992	Iron Hands	Iron Hands	Paume-de-Fer
0993	Iron Jugulis	Iron Jugulis	Têtes-de-Fer
0994	Iron Moth	Iron Moth	Mite-de-Fer
0995	Iron Thorns	Iron Thorns	Épine-de-Fer
0996	Frigibax	Frigibax	Frigodo
0997	Arctibax	Arctibax	Cryodo
0998	Baxcalibur	Baxcalibur	Glaivodo
0999	Gimmighoul	Gimmighoul	Mordudor
1000	Gholdengo	Gholdengo	Gromago
1001	Wo-Chien	Wo-Chien	Chongjian
1002	Chien-Pao	Chien-Pao	Baojian
1003	Ting-Lu	Ting-Lu	Dinglu
1004	Chi-Yu	Chi-Yu	Yuyu
1005	Roaring Moon	Roaring Moon	Rugit-Lune
1006	Iron Valiant	Iron Valiant	Garde-de-Fer
1007	Koraidon	Koraidon	Koraidon
1008	Miraidon	Miraidon	Miraidon
1009	Rotom-Wash	Rotom-Wash	Motisma-Lavage
1010	Moltres-Galar	Moltres-Galar	Sulfura-Galar
1011	Slowbro-Galar	Slowbro-Galar	Flagadoss-Galar
1012	Walking Wake	Walking Wake	Serpente-Eau
1013	Landorus-Therian	Landorus-Therian	Démétéros-Totem
1014	Ogerpon	Ogerpon	Ogerpon
1015	Enamorus-Therian	Enamorus-Therian	Amovénus-Totem
1016	Fezandipiti	Fezandipiti	Favianos
1017	Decidueye-Hisui	Decidueye-Hisui	Archéduc-Hisui
1018	Ogerpon-Wellspring	Ogerpon-Wellspring	Ogerpon-du Puits
1019	Typhlosion-Hisui	Typhlosion-Hisui	Typhlosion-Hisui
1020	Rotom-Mow	Rotom-Mow	Motisma-Tonte
1021	Sinistcha	Sinistcha	Théffroyable
1022	Sandslash-Alola	Sandslash-Alola	Sablaireau-Alola
1023	Electrode-Hisui	Electrode-Hisui	Électrode-Hisui
1024	Braviary-Hisui	Braviary-Hisui	Gueriaigle-Hisui
1025	Lycanroc-Midnight	Lycanroc-Midnight	Lougaroc-Nocturne
1026	Oricorio-Pom-Pom	Oricorio-Pom-Pom	Plumeline-Pom-Pom
1027	Lycanroc-Dusk	Lycanroc-Dusk	Lougaroc-Crépuscule
1028	Arcanine-Hisui	Arcanine-Hisui	Arcanin-Hisui
1029	Persian-Alola	Persian-Alola	Persian-Alola
1030	Tauros-Paldea-Aqua	Tauros-Paldea-Aqua	Tauros-Paldea-Eau
1031	Oinkologne-F	Oinkologne-F	Fragroin-F
1032	Hoopa-Unbound	Hoopa-Unbound	Hoopa-Déchaîné
1033	Ursaluna-Bloodmoon	Ursaluna-Bloodmoon	Ursaking-Lune
1034	Basculegion-F	Basculegion-F	Paragruel-F
1035	Zoroark-Hisui	Zoroark-Hisui	Zoroark-Hisui
1036	Qwilfish-Hisui	Qwilfish-Hisui	Qwilfish-Hisui
1037	Goodra-Hisui	Goodra-Hisui	Muplodocus-Hisui
1038	Golem-Alola	Golem-Alola	Grolem-Alola
1039	Tauros-Paldea-Blaze	Tauros-Paldea-Blaze	Tauros-Paldea-Feu
1040	Rotom-Frost	Rotom-Frost	Motisma-Froid
1041	Lilligant-Hisui	Lilligant-Hisui	Fragilady-Hisui
1042	Rotom-Fan	Rotom-Fan	Motisma-Hélice
1043	Dugtrio-Alola	Dugtrio-Alola	Triopikeur-Alola
1044	Raichu-Alola	Raichu-Alola	Raichu-Alola
1045	Dipplin	Dipplin	Pomdramour
1046	Weezing-Galar	Weezing-Galar	Smogogo-Galar
1047	Zapdos-Galar	Zapdos-Galar	Électhor-Galar
1048	Oricorio-Sensu	Oricorio-Sensu	Plumeline-Buyō
1049	Tornadus-Therian	Tornadus-Therian	Boréas-Totem
1050	Muk-Alola	Muk-Alola	Grotadmorv-Alola
1051	Ninetales-Alola	Ninetales-Alola	Feunard-Alola
1052	Tauros-Paldea-Combat	Tauros-Paldea-Combat	Tauros-Paldea-Combat
1053	Slowking-Galar	Slowking-Galar	Roigada-Galar
1054	Ogerpon-Cornerstone	Ogerpon-Cornerstone	Ogerpon-de la Pierre
1055	Samurott-Hisui	Samurott-Hisui	Clamiral-Hisui
1056	Iron Leaves	Iron Leaves	Vert-de-Fer
1057	Articuno-Galar	Articuno-Galar	Artikodin-Galar
1058	Munkidori	Munkidori	Fortusimia
1059	Okidogi	Okidogi	Félicanis
1060	Rotom-Heat	Rotom-Heat	Motisma-Chaleur
1061	Avalugg-Hisui	Avalugg-Hisui	Séracrawl-Hisui
1062	Thundurus-Therian	Thundurus-Therian	Fulguris-Totem
1063	Indeedee-F	Indeedee-F	Wimessir-F
1064	Archaludon	Archaludon	Pondralugon
1065	Terapagos	Terapagos	Terapagos
1066	Deoxys-Speed	Deoxys-Speed	Deoxys-Vitesse
1067	Raging Bolt	Raging Bolt	Ire-Foudre
1068	Iron Crown	Iron Crown	Chef-de-Fer
1069	Exeggutor-Alola	Exeggutor-Alola	Noadkoko-Alola
1070	Gouging Fire	Gouging Fire	Feu-Perçant
1071	Deoxys-Defense	Deoxys-Defense	Deoxys-Défense
1072	Iron Boulder	Iron Boulder	Roc-de-Fer
1073	Hydrapple	Hydrapple	Pomdorochi
1074	Mr. Mime-Galar	Mr. Mime-Galar	M. Mime-Galar""")
trad=sttrad()

# Stats  nv
data="""
Uber
Uber
Alakazam-MégaPsychicCalquePV
55Atq
50Déf
65SpA
175SpD
105Vit
150BST
600
Uber
CourrousingeFightingGhostEsprit Vital
AttentionAcharnéPV
110Atq
115Déf
80SpA
50SpD
90Vit
90BST
535
Uber
ArceusNormalMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-InsecteBugMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-TénèbresDarkMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-DragonDragonMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-ÉlectrikElectricMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-FéeFairyMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-CombatFightingMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-FeuFireMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-VolFlyingMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-SpectreGhostMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-PlanteGrassMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-SolGroundMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-GlaceIceMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-PoisonPoisonMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-PsyPsychicMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-RocheRockMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-AcierSteelMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
Arceus-EauWaterMulti-TypePV
120Atq
120Déf
120SpA
120SpD
120Vit
120BST
720
Uber
GlaivodoDragonIceThermodynamiqueCorps GelPV
115Atq
145Déf
92SpA
75SpD
86Vit
87BST
600
Uber
Tortank-MégaWaterMéga BlasterPV
79Atq
103Déf
120SpA
135SpD
115Vit
78BST
630
Uber
Braségali-MégaFireFightingTurboPV
80Atq
160Déf
80SpA
130SpD
80Vit
100BST
630
Uber
Sylveroy-FroidPsychicIceOsmose Équine (Blizzeval)PV
100Atq
165Déf
150SpA
85SpD
130Vit
50BST
680
Uber
BaojianDarkIceÉpée du FléauPV
80Atq
120Déf
80SpA
90SpD
65Vit
135BST
570
Uber
YuyuDarkFirePerles du FléauPV
55Atq
80Déf
80SpA
135SpD
120Vit
100BST
570
Uber
Darumacho-GalarIceEntêtementMode TransePV
105Atq
140Déf
55SpA
30SpD
55Vit
95BST
480
Uber
DeoxysPsychicPressionPV
50Atq
150Déf
50SpA
150SpD
50Vit
150BST
600
Uber
Deoxys-AttaquePsychicPressionPV
50Atq
180Déf
20SpA
180SpD
20Vit
150BST
600
Uber
Deoxys-VitessePsychicPressionPV
50Atq
95Déf
90SpA
95SpD
90Vit
180BST
600
Uber
DialgaSteelDragonPressionTélépathePV
100Atq
120Déf
120SpA
150SpD
100Vit
90BST
680
Uber
Dialga-OrigineSteelDragonPressionTélépathePV
100Atq
100Déf
120SpA
150SpD
120Vit
90BST
680
Uber
HydragonWaterDragonAbsorb Eau
PrognatheBaigne SablePV
90Atq
90Déf
100SpA
70SpD
80Vit
75BST
505
Uber
LanssorienDragonGhostCorps Sain
InfiltrationCorps MauditPV
88Atq
120Déf
75SpA
100SpD
75Vit
142BST
600
Uber
CléopsytraPsychicOpportuniste
FouilleTurboPV
95Atq
60Déf
60SpA
101SpD
60Vit
105BST
481
Uber
ÉthernatosPoisonDragonPressionPV
140Atq
85Déf
95SpA
145SpD
95Vit
130BST
690
Uber
Flotte-MècheGhostFairyPaléosynthèsePV
55Atq
55Déf
55SpA
135SpD
135Vit
135BST
570
Uber
GenesectBugSteelTéléchargePV
71Atq
120Déf
95SpA
120SpD
95Vit
99BST
600
Uber
Genesect-PyroBugSteelTéléchargePV
71Atq
120Déf
95SpA
120SpD
95Vit
99BST
600
Uber
Genesect-CryoBugSteelTéléchargePV
71Atq
120Déf
95SpA
120SpD
95Vit
99BST
600
Uber
Genesect-AquaBugSteelTéléchargePV
71Atq
120Déf
95SpA
120SpD
95Vit
99BST
600
Uber
Genesect-ChocBugSteelTéléchargePV
71Atq
120Déf
95SpA
120SpD
95Vit
99BST
600
Uber
GromagoSteelGhostCorps en OrPV
87Atq
60Déf
95SpA
133SpD
91Vit
84BST
550
Uber
GiratinaGhostDragonPressionTélépathePV
150Atq
100Déf
120SpA
100SpD
120Vit
90BST
680
Uber
Giratina-OrigineGhostDragonLévitationPV
150Atq
120Déf
100SpA
120SpD
100Vit
90BST
680
Uber
GroudonGroundSécheressePV
100Atq
150Déf
140SpA
100SpD
90Vit
90BST
670
Uber
Groudon-PrimoGroundFireTerre FinalePV
100Atq
180Déf
160SpA
150SpD
90Vit
90BST
770
Uber
Ho-OhFireFlyingPressionRégé-ForcePV
106Atq
130Déf
90SpA
110SpD
154Vit
90BST
680
Uber
Hotte-de-FerIceWaterCharge QuantiquePV
56Atq
80Déf
114SpA
124SpD
60Vit
136BST
570
Uber
Kangourex-MégaNormalAmour FilialPV
105Atq
125Déf
100SpA
60SpD
100Vit
100BST
590
Uber
ScalpereurDarkSteelAcharné
Général SuprêmePressionPV
100Atq
135Déf
120SpA
60SpD
85Vit
50BST
550
Uber
KyogreWaterCrachinPV
100Atq
100Déf
90SpA
150SpD
140Vit
90BST
670
Uber
Kyogre-PrimoWaterMer PrimairePV
100Atq
150Déf
90SpA
180SpD
160Vit
90BST
770
Uber
Kyurem-NoirDragonIceTéra-VoltagePV
125Atq
170Déf
100SpA
120SpD
90Vit
95BST
700
Uber
Kyurem-BlancDragonIceTurboBrasierPV
125Atq
120Déf
90SpA
170SpD
100Vit
95BST
700
Uber
DémétérosGroundFlyingForce SableSans LimitePV
89Atq
125Déf
90SpA
115SpD
80Vit
101BST
600
Uber
Lucario-MégaFightingSteelAdaptabilitéPV
70Atq
145Déf
88SpA
140SpD
70Vit
112BST
625
Uber
LugiaPsychicFlyingPressionMultiécaillePV
106Atq
90Déf
130SpA
90SpD
154Vit
110BST
680
Uber
LunalaPsychicGhostSpectro-BouclierPV
137Atq
113Déf
89SpA
137SpD
107Vit
97BST
680
Uber
MagearnaSteelFairyAnimacoeurPV
80Atq
95Déf
115SpA
130SpD
115Vit
65BST
600
Uber
Magearna-PasséSteelFairyAnimacoeurPV
80Atq
95Déf
115SpA
130SpD
115Vit
65BST
600
Uber
MarshadowFightingGhostTechnicienPV
90Atq
125Déf
80SpA
90SpD
90Vit
125BST
600
Uber
MelmetalSteelPoing de FerPV
135Atq
143Déf
143SpA
80SpD
65Vit
34BST
600
Uber
Métalosse-MégaSteelPsychicGriffe DurePV
80Atq
145Déf
150SpA
105SpD
110Vit
110BST
700
Uber
MewtwoPsychicPressionTensionPV
106Atq
110Déf
90SpA
154SpD
90Vit
130BST
680
Uber
Mewtwo-Méga-XPsychicFightingImpassiblePV
106Atq
190Déf
100SpA
154SpD
100Vit
130BST
780
Uber
Mewtwo-Méga-YPsychicInsomniaPV
106Atq
150Déf
70SpA
194SpD
120Vit
140BST
780
Uber
MandrillonPoisonDragonBoost ChimèrePV
73Atq
73Déf
73SpA
127SpD
73Vit
121BST
540
Uber
Necrozma-AurorePsychicGhostPrisme-ArmurePV
97Atq
113Déf
109SpA
157SpD
127Vit
77BST
680
Uber
Necrozma-CouchantPsychicSteelPrisme-ArmurePV
97Atq
157Déf
127SpA
113SpD
109Vit
77BST
680
Uber
Necrozma-UltraPsychicDragonCérébro-ForcePV
97Atq
167Déf
97SpA
167SpD
97Vit
129BST
754
Uber
Ogerpon-du FourneauGrassFireBrise MoulePV
80Atq
120Déf
84SpA
60SpD
96Vit
110BST
550
Uber
SuperdofinWaterSupermutationPV
100Atq
70Déf
72SpA
53SpD
62Vit
100BST
457
Uber
Superdofin-SuperWaterSupermutationPV
100Atq
160Déf
97SpA
106SpD
87Vit
100BST
650
Uber
PalkiaWaterDragonPressionTélépathePV
90Atq
120Déf
100SpA
150SpD
120Vit
100BST
680
Uber
Palkia-OrigineWaterDragonPressionTélépathePV
90Atq
100Déf
100SpA
150SpD
120Vit
120BST
680
Uber
CancreloveBugFightingBoost ChimèrePV
71Atq
137Déf
37SpA
137SpD
37Vit
151BST
570
Uber
RayquazaDragonFlyingAir LockPV
105Atq
150Déf
90SpA
150SpD
90Vit
95BST
680
Uber
RegielekiElectricTransistorPV
80Atq
100Déf
50SpA
100SpD
50Vit
200BST
580
Uber
ReshiramDragonFireTurboBrasierPV
100Atq
120Déf
100SpA
150SpD
120Vit
90BST
680
Uber
Rugit-LuneDragonDarkPaléosynthèsePV
105Atq
139Déf
71SpA
55SpD
101Vit
119BST
590
Uber
Drattak-MégaDragonFlyingPeau CélestePV
95Atq
145Déf
130SpA
120SpD
90Vit
120BST
700
Uber
Shaymin-CélesteGrassFlyingSérénitéPV
100Atq
103Déf
75SpA
120SpD
75Vit
127BST
600
Uber
FarfurexFightingPoisonPression
DélestageToxitouchePV
80Atq
130Déf
60SpA
40SpD
80Vit
120BST
510
Uber
SolgaleoPsychicSteelMétallo-GardePV
137Atq
137Déf
107SpA
113SpD
89Vit
97BST
680
Uber
SpectrevalGhostSombre RuadePV
100Atq
65Déf
60SpA
145SpD
80Vit
130BST
580
Uber
TerapagosNormalTéramorphosePV
90Atq
65Déf
85SpA
65SpD
85Vit
60BST
450
Uber
Terapagos-StellaireNormalTéraformation 0PV
160Atq
105Déf
110SpA
130SpD
110Vit
85BST
700
Uber
Terapagos-TéracristalNormalTéra CarapacePV
95Atq
95Déf
110SpA
105SpD
110Vit
85BST
600
Uber
Ursaking-Lune VermeilleGroundNormalOeil RévélateurPV
113Atq
70Déf
120SpA
135SpD
65Vit
52BST
555
Uber
ShifoursFightingDarkPoing InvisiblePV
100Atq
130Déf
100SpA
63SpD
60Vit
97BST
550
Uber
Serpente-EauWaterDragonPaléosynthèsePV
99Atq
83Déf
91SpA
125SpD
83Vit
109BST
590
Uber
XerneasFairyAura FéériquePV
126Atq
131Déf
95SpA
131SpD
98Vit
99BST
680
Uber
YveltalDarkFlyingAura TénébreusePV
126Atq
131Déf
95SpA
131SpD
98Vit
99BST
680
Uber
ZacianFairyLame IndomptablePV
92Atq
120Déf
115SpA
80SpD
115Vit
138BST
660
Uber
Zacian-ÉpéeFairySteelLame IndomptablePV
92Atq
150Déf
115SpA
80SpD
115Vit
148BST
700
Uber
Zamazenta-BouclierFightingSteelÉgide InflexiblePV
92Atq
120Déf
140SpA
80SpD
140Vit
128BST
700
Uber
ZekromDragonElectricTéra-VoltagePV
100Atq
150Déf
120SpA
120SpD
100Vit
90BST
680
Uber
ZygardeDragonGroundAura Inversée(Rassemblement)PV
108Atq
100Déf
121SpA
81SpD
95Vit
95BST
600
Uber
Zygarde-ParfaitDragonGroundRassemblementPV
216Atq
100Déf
121SpA
91SpD
95Vit
85BST
708
OU
OU
MamanboWaterCoeur Soin
HydratationRégé-ForcePV
165Atq
75Déf
80SpA
40SpD
45Vit
65BST
470
OU
PondralugonSteelDragonEndurance
FermetéNerfs d'AcierPV
90Atq
105Déf
130SpA
125SpD
65Vit
85BST
600
OU
Branette-MégaGhostFarceurPV
64Atq
165Déf
75SpA
93SpD
83Vit
75BST
555
OU
Dracaufeu-Méga-YFireFlyingSécheressePV
78Atq
104Déf
78SpA
159SpD
115Vit
100BST
634
OU
TerraistePoisonGroundPoint Poison
Absorb EauInconscientPV
130Atq
75Déf
60SpA
45SpD
100Vit
20BST
430
OU
CorvaillusFlyingSteelPression
TensionArmure MiroirPV
98Atq
87Déf
105SpA
53SpD
85Vit
67BST
495
OU
DarkraiDarkMauvais RêvePV
70Atq
90Déf
90SpA
135SpD
90Vit
125BST
600
OU
Diancie-MégaRockFairyMiroir MagikPV
50Atq
160Déf
110SpA
160SpD
110Vit
110BST
700
OU
DracolosseDragonFlyingAttentionMultiécaillePV
91Atq
134Déf
95SpA
100SpD
100Vit
80BST
600
OU
NoacierGrassSteelÉpine de FerAnticipationPV
74Atq
94Déf
131SpA
54SpD
116Vit
20BST
489
OU
CarchacrokDragonGroundVoile SablePeau DurePV
108Atq
130Déf
95SpA
80SpD
85Vit
102BST
600
OU
GiganselRockSel Purificateur
FermetéCorps SainPV
100Atq
100Déf
130SpA
45SpD
90Vit
35BST
500
OU
FloréclatRockPoisonDépôt ToxiqueCorrosionPV
83Atq
55Déf
90SpA
130SpD
81Vit
86BST
525
OU
ScorvolGroundFlyingHyper Cutter
Voile SableSoin PoisonPV
75Atq
95Déf
125SpA
45SpD
75Vit
95BST
510
OU
Feu-PerçantFireDragonPaléosynthèsePV
105Atq
115Déf
121SpA
65SpD
93Vit
91BST
590
OU
Fort-IvoireGroundFightingPaléosynthèsePV
115Atq
131Déf
131SpA
53SpD
53Vit
87BST
570
OU
AmphinobiWaterDarkTorrentProtéen
(Synergie)PV
72Atq
95Déf
67SpA
103SpD
71Vit
122BST
530
OU
Amphinobi-SynergieWaterDarkSynergiePV
72Atq
95Déf
67SpA
103SpD
71Vit
122BST
530
OU
SorcilencePsychicFairyCoeur Soin
AnticipationMiroir MagikPV
57Atq
90Déf
95SpA
136SpD
103Vit
29BST
510
OU
HeatranFireSteelTorcheCorps ArdentPV
91Atq
90Déf
106SpA
130SpD
106Vit
77BST
600
OU
Hoopa-DéchaînéPsychicDarkMagicienPV
80Atq
160Déf
60SpA
170SpD
130Vit
80BST
680
OU
Roc-de-FerRockPsychicCharge QuantiquePV
90Atq
120Déf
80SpA
68SpD
108Vit
124BST
590
OU
Chef-de-FerSteelPsychicCharge QuantiquePV
90Atq
72Déf
100SpA
122SpD
108Vit
98BST
590
OU
Roue-de-FerGroundSteelCharge QuantiquePV
90Atq
112Déf
120SpA
72SpD
70Vit
106BST
570
OU
Garde-de-FerFairyFightingCharge QuantiquePV
74Atq
130Déf
90SpA
120SpD
60Vit
116BST
590
OU
Démétéros-TotemGroundFlyingIntimidationPV
89Atq
145Déf
90SpA
105SpD
80Vit
91BST
600
OU
Lockpin-MégaNormalFightingQuerelleurPV
65Atq
136Déf
94SpA
54SpD
96Vit
135BST
580
OU
SulfuraFireFlyingPressionCorps ArdentPV
90Atq
100Déf
90SpA
125SpD
85Vit
90BST
580
OU
Ogerpon-du PuitsGrassWaterAbsorb EauPV
80Atq
120Déf
84SpA
60SpD
96Vit
110BST
550
OU
PêchaminusPoisonGhostEmprise ToxiquePV
88Atq
88Déf
160SpA
88SpD
88Vit
88BST
600
OU
BekipanWaterFlyingRegard Vif
CrachinCuvettePV
60Atq
50Déf
100SpA
95SpD
70Vit
65BST
440
OU
Ire-FoudreElectricDragonPaléosynthèsePV
125Atq
73Déf
91SpA
137SpD
89Vit
75BST
590
OU
GorythmicGrassEngraisCréa-HerbePV
100Atq
125Déf
90SpA
60SpD
70Vit
85BST
530
OU
Clamiral-HisuiWaterDarkTorrentIncisifPV
90Atq
108Déf
80SpA
100SpD
65Vit
85BST
528
OU
Cizayox-MégaBugSteelTechnicienPV
70Atq
150Déf
140SpA
65SpD
100Vit
75BST
600
OU
MajaspicGrassEngraisContestationPV
75Atq
75Déf
95SpA
75SpD
95Vit
113BST
528
OU
Roigada-GalarPoisonPsychicBreuvage Suspect
Tempo PersoRégé-ForcePV
95Atq
65Déf
80SpA
110SpD
110Vit
30BST
490
OU
Laggron-MégaWaterGroundGlissadePV
100Atq
150Déf
110SpA
95SpD
110Vit
70BST
635
OU
TokoricoElectricFairyCréa-ÉlecTélépathePV
70Atq
115Déf
85SpA
95SpD
75Vit
130BST
570
OU
TokopiyonPsychicFairyCréa-PsyTélépathePV
70Atq
85Déf
75SpA
130SpD
115Vit
95BST
570
OU
ChartorFireÉcran Fumée
SécheresseCoque ArmurePV
70Atq
85Déf
140SpA
85SpD
70Vit
20BST
470
OU
UrsakingGroundNormalCran
Pare-BallesTensionPV
130Atq
140Déf
105SpA
45SpD
80Vit
50BST
550
OU
Shifours-Mille PoingsFightingWaterPoing InvisiblePV
100Atq
130Déf
100SpA
63SpD
60Vit
97BST
550
OU
PyraxBugFireCorps ArdentEssaimPV
85Atq
60Déf
65SpA
135SpD
105Vit
100BST
550
OU
ZamazentaFightingÉgide InflexiblePV
92Atq
120Déf
115SpA
80SpD
115Vit
138BST
660
OU
ÉlecthorElectricFlyingPressionStatikPV
90Atq
90Déf
85SpA
125SpD
90Vit
100BST
580
OU par technicalité
(OU)
Carchacrok-MégaDragonGroundForce SablePV
108Atq
170Déf
115SpA
120SpD
95Vit
92BST
700
UUBL
UUBL
BraségaliFireFightingBrasierTurboPV
80Atq
120Déf
70SpA
110SpD
70Vit
80BST
530
UUBL
Dracaufeu-Méga-XFireDragonGriffe DurePV
78Atq
130Déf
111SpA
130SpD
85Vit
100BST
634
UUBL
OyacataWaterInconscient
BenêtIgnifu-VoilePV
150Atq
100Déf
115SpA
65SpD
65Vit
35BST
530
UUBL
LéviatorWaterFlyingIntimidationImpudencePV
95Atq
125Déf
79SpA
60SpD
100Vit
81BST
540
UUBL
Léviator-MégaWaterDarkBrise MoulePV
95Atq
155Déf
109SpA
70SpD
130Vit
81BST
640
UUBL
KatagamiGrassSteelBoost ChimèrePV
59Atq
181Déf
131SpA
59SpD
31Vit
109BST
570
UUBL
ÉkaïserDragonFightingPare-Balles
Anti-BruitEnvelocapePV
75Atq
110Déf
125SpA
100SpD
105Vit
85BST
600
UUBL
KyuremDragonIcePressionPV
125Atq
130Déf
90SpA
130SpD
90Vit
95BST
660
UUBL
ManaphyWaterHydratationPV
100Atq
100Déf
100SpA
100SpD
100Vit
100BST
600
UUBL
Mysdibule-MégaSteelFairyColoforcePV
50Atq
105Déf
125SpA
55SpD
95Vit
50BST
480
UUBL
Charmina-MégaFightingPsychicForce PurePV
60Atq
100Déf
85SpA
80SpD
85Vit
100BST
510
UUBL
MiascaradeGrassDarkEngraisProtéenPV
76Atq
110Déf
70SpA
81SpD
70Vit
123BST
530
UUBL
Ogerpon-de la PierreGrassRockFermetéPV
80Atq
120Déf
84SpA
60SpD
96Vit
110BST
550
UUBL
Scarabrute-MégaBugFlyingPeau CélestePV
65Atq
155Déf
120SpA
65SpD
90Vit
105BST
600
UUBL
Boréas-TotemFlyingRégé-ForcePV
79Atq
100Déf
80SpA
110SpD
90Vit
121BST
580
UUBL
DimoretDarkIcePressionPickpocketPV
70Atq
120Déf
65SpA
45SpD
85Vit
125BST
510
UUBL
CâblifèreElectricBoost ChimèrePV
83Atq
89Déf
71SpA
173SpD
71Vit
83BST
570
UU
UU
ExagideSteelGhostDéclic TactiquePV
60Atq
50Déf
140SpA
50SpD
140Vit
60BST
500
UU
Altaria-MégaDragonFairyPeau FéériquePV
75Atq
110Déf
110SpA
110SpD
105Vit
80BST
590
UU
GauletGrassPoisonPose SporeRégé-ForcePV
114Atq
85Déf
70SpA
85SpD
80Vit
30BST
464
UU
ScalproieDarkSteelAcharné
AttentionPressionPV
65Atq
125Déf
100SpA
60SpD
70Vit
70BST
490
UU
BamboiselleSteelFlyingBoost ChimèrePV
97Atq
101Déf
103SpA
107SpD
101Vit
61BST
570
UU
MalvalameFireGhostTorcheArmurouilléePV
75Atq
125Déf
80SpA
60SpD
100Vit
85BST
525
UU
LeveinardNormalMédic Nature
SérénitéCoeur SoinPV
250Atq
5Déf
5SpA
35SpD
105Vit
50BST
450
UU
PyrobutFireBrasierLibéroPV
80Atq
116Déf
75SpA
65SpD
75Vit
119BST
530
UU
MélodelfeFairyJoli Sourire
Garde MagikInconscientPV
95Atq
70Déf
73SpA
95SpD
90Vit
60BST
483
UU
GalvagonElectricDragonAbsorb Volt
AgitationBaigne SablePV
90Atq
100Déf
90SpA
80SpD
70Vit
75BST
505
UU
AmovénusFairyFlyingJoli SourireContestationPV
74Atq
115Déf
70SpA
135SpD
80Vit
106BST
580
UU
MinotaupeGroundSteelBaigne Sable
Force SableBrise MoulePV
110Atq
135Déf
60SpA
50SpD
65Vit
88BST
508
UU
Gardevoir-MégaPsychicFairyPeau FéériquePV
68Atq
85Déf
65SpA
165SpD
135Vit
100BST
618
UU
TritosorWaterGroundGlue
LavaboForce SablePV
111Atq
83Déf
68SpA
92SpD
82Vit
39BST
475
UU
SarmuraïBugWaterRepli TactiquePV
75Atq
125Déf
140SpA
60SpD
90Vit
40BST
530
UU
Muplodocus-HisuiSteelDragonHerbivore
Coque ArmurePoisseuxPV
80Atq
100Déf
100SpA
110SpD
150Vit
60BST
600
UU
TranchodonDragonRivalité
Brise MouleTensionPV
76Atq
147Déf
90SpA
60SpD
70Vit
97BST
540
UU
PomdorochiGrassDragonNectar Mielleux
Régé-ForceGluePV
106Atq
80Déf
110SpA
120SpD
80Vit
44BST
540
UU
Paume-de-FerFightingElectricCharge QuantiquePV
154Atq
140Déf
108SpA
50SpD
68Vit
50BST
570
UU
Mite-de-FerFirePoisonCharge QuantiquePV
80Atq
70Déf
60SpA
140SpD
110Vit
110BST
570
UU
KeldeoWaterFightingCoeur NoblePV
91Atq
72Déf
90SpA
129SpD
90Vit
108BST
580
UU
Keldeo-DécidéWaterFightingCoeur NoblePV
91Atq
72Déf
90SpA
129SpD
90Vit
108BST
580
UU
HachécateurBugRockEssaim
Sans LimiteIncisifPV
70Atq
135Déf
95SpA
45SpD
70Vit
85BST
500
UU
LatiosDragonPsychicLévitationPV
80Atq
90Déf
80SpA
130SpD
110Vit
110BST
600
UU
Latios-MégaDragonPsychicLévitationPV
80Atq
130Déf
100SpA
160SpD
120Vit
110BST
700
UU
Motisma-LavageElectricWaterLévitationPV
50Atq
65Déf
107SpA
105SpD
107Vit
86BST
520
UU
Ténéfix-MégaDarkGhostMiroir MagikPV
50Atq
85Déf
125SpA
85SpD
115Vit
20BST
480
UU
ThéffroyableGrassGhostAux Petits SoinsIgnifugéPV
71Atq
60Déf
106SpA
121SpD
80Vit
70BST
508
UU
Théffroyable-ExceptionnelleGrassGhostAux Petits SoinsIgnifugéPV
71Atq
60Déf
106SpA
121SpD
80Vit
70BST
508
UU
AirmureSteelFlyingRegard Vif
FermetéArmurouilléePV
65Atq
80Déf
140SpA
40SpD
70Vit
70BST
465
UU
FlâmigatorFireGhostBrasierInconscientPV
104Atq
75Déf
100SpA
110SpD
75Vit
66BST
530
UU
FlagadossWaterPsychicBenêt
Tempo PersoRégé-ForcePV
95Atq
75Déf
110SpA
100SpD
80Vit
30BST
490
UU
TokopiscoWaterFairyCréa-BrumeTélépathePV
70Atq
75Déf
115SpA
95SpD
130Vit
85BST
570
UU
Fulguris-TotemElectricFlyingAbsorb VoltPV
79Atq
105Déf
70SpA
145SpD
80Vit
101BST
580
UU
DingluDarkGroundUrne du FléauPV
155Atq
110Déf
125SpA
55SpD
80Vit
45BST
570
UU
PrédastériePoisonWaterCruauté
ÉchauffementRégé-ForcePV
50Atq
63Déf
152SpA
53SpD
142Vit
35BST
495
UU
TyranocifRockDarkSable VolantTensionPV
100Atq
134Déf
110SpA
95SpD
100Vit
61BST
600
UU
Tyranocif-MégaRockDarkSable VolantPV
100Atq
164Déf
150SpA
95SpD
120Vit
71BST
700
UU
Florizarre-MégaGrassPoisonIsograissePV
80Atq
100Déf
123SpA
122SpD
120Vit
80BST
625
UU
VictiniPsychicFireVictorieuxPV
100Atq
100Déf
100SpA
100SpD
100Vit
100BST
600
UU
Électhor-GalarFightingFlyingAcharnéPV
90Atq
125Déf
90SpA
85SpD
90Vit
100BST
580
RUBL
RUBL
Ptéra-MégaRockFlyingGriffe DurePV
80Atq
135Déf
85SpA
70SpD
95Vit
150BST
615
RUBL
AlakazamPsychicSynchro
AttentionGarde MagikPV
55Atq
50Déf
45SpA
135SpD
95Vit
120BST
500
RUBL
PierroteknikFireGhostBoost ChimèrePV
53Atq
127Déf
53SpA
151SpD
79Vit
107BST
570
RUBL
MouscotoBugFightingBoost ChimèrePV
107Atq
139Déf
139SpA
53SpD
53Vit
79BST
570
RUBL
Deoxys-DéfensePsychicPressionPV
50Atq
70Déf
160SpA
70SpD
160Vit
90BST
600
RUBL
Gallame-MégaPsychicFightingAttentionPV
68Atq
165Déf
95SpA
65SpD
115Vit
110BST
618
RUBL
EctoplasmaGhostPoisonCorps MauditPV
60Atq
65Déf
60SpA
130SpD
75Vit
110BST
500
RUBL
BrutalibréFightingFlyingÉchauffement
DélestageBrise MoulePV
78Atq
92Déf
75SpA
74SpD
63Vit
118BST
500
RUBL
Scarhino-MégaBugFightingMulti-CoupsPV
80Atq
185Déf
115SpA
40SpD
105Vit
75BST
600
RUBL
Vert-de-FerGrassPsychicCharge QuantiquePV
90Atq
130Déf
88SpA
70SpD
108Vit
104BST
590
RUBL
JirachiSteelPsychicSérénitéPV
100Atq
100Déf
100SpA
100SpD
100Vit
100BST
600
RUBL
Latias-MégaDragonPsychicLévitationPV
80Atq
100Déf
120SpA
140SpD
150Vit
110BST
700
RUBL
Fragilady-HisuiGrassFightingChlorophylle
AgitationFeuille GardePV
70Atq
105Déf
75SpA
50SpD
75Vit
105BST
480
RUBL
MammochonIceGroundBenêt
Rideau NeigeIsograissePV
110Atq
130Déf
80SpA
70SpD
60Vit
80BST
530
RUBL
MewPsychicSynchroPV
100Atq
100Déf
100SpA
100SpD
100Vit
100BST
600
RUBL
Sulfura-GalarDarkFlyingDracolèrePV
90Atq
85Déf
90SpA
100SpD
125Vit
90BST
580
RUBL
Porygon-ZNormalAdaptabilité
TéléchargeAnalystePV
85Atq
80Déf
70SpA
135SpD
75Vit
90BST
535
RUBL
DrattakDragonFlyingIntimidationImpudencePV
95Atq
135Déf
80SpA
110SpD
80Vit
100BST
600
RUBL
TerrakiumRockFightingCoeur NoblePV
91Atq
129Déf
90SpA
72SpD
90Vit
108BST
580
RUBL
Zoroark-HisuiNormalGhostIllusionPV
55Atq
100Déf
60SpA
125SpD
60Vit
110BST
510
RU
RU
BlizzaroiGrassIceAlerte NeigeAnti-BruitPV
90Atq
92Déf
75SpA
92SpD
85Vit
60BST
494
RU
Blizzaroi-MégaGrassIceAlerte NeigePV
90Atq
132Déf
105SpA
132SpD
105Vit
30BST
594
RU
AbsolDarkPression
ChanceuxCoeur NoblePV
65Atq
130Déf
60SpA
75SpD
60Vit
75BST
465
RU
Absol-MégaDarkMiroir MagikPV
65Atq
150Déf
60SpA
115SpD
60Vit
115BST
565
RU
LimaspeedBugHydratation
GlueDélestagePV
80Atq
70Déf
40SpA
100SpD
60Vit
145BST
495
RU
PtéraRockFlyingTête de Roc
PressionTensionPV
80Atq
105Déf
65SpA
60SpD
75Vit
130BST
515
RU
GalekingSteelRockFermeté
Tête de RocHeavy MetalPV
70Atq
110Déf
180SpA
60SpD
60Vit
50BST
530
RU
Galeking-MégaSteelFiltrePV
70Atq
140Déf
230SpA
60SpD
80Vit
50BST
630
RU
CharmillyFairyGluco-VoileAroma-VoilePV
65Atq
60Déf
75SpA
110SpD
121Vit
64BST
495
RU
AltariaDragonFlyingMédic NatureCiel GrisPV
75Atq
70Déf
90SpA
70SpD
105Vit
80BST
490
RU
CapidextreNormalTechnicien
RamassageMulti-CoupsPV
75Atq
100Déf
66SpA
60SpD
66Vit
115BST
482
RU
PharampElectricStatikPlusPV
90Atq
75Déf
85SpA
115SpD
90Vit
55BST
510
RU
Pharamp-MégaElectricDragonBrise MoulePV
90Atq
95Déf
105SpA
165SpD
110Vit
45BST
610
RU
DratatinGrassDragonMûrissement
GloutonnerieIsograissePV
110Atq
85Déf
80SpA
100SpD
80Vit
30BST
485
RU
TarenbulleWaterBugAquabulleAbsorb EauPV
68Atq
70Déf
92SpA
50SpD
132Vit
42BST
454
RU
ArbokPoisonIntimidation
MueTensionPV
60Atq
95Déf
69SpA
65SpD
79Vit
80BST
448
RU
ArbolivaGrassNormalSemencierRécoltePV
78Atq
69Déf
90SpA
125SpD
109Vit
39BST
510
RU
ArcaninFireIntimidation
TorcheCoeur NoblePV
90Atq
110Déf
80SpA
100SpD
80Vit
95BST
555
RU
Arcanin-HisuiFireRockIntimidation
TorcheTête de RocPV
95Atq
115Déf
80SpA
95SpD
80Vit
90BST
555
RU
AéroptéryxRockFlyingDéfaitistePV
75Atq
140Déf
65SpA
112SpD
65Vit
110BST
567
RU
HydraglaWaterIceAbsorb Eau
Corps GelChasse-NeigePV
90Atq
90Déf
100SpA
80SpD
90Vit
55BST
505
RU
GalvaglaElectricIceAbsorb Volt
StatikChasse-NeigePV
90Atq
100Déf
90SpA
90SpD
80Vit
55BST
505
RU
MigalosBugPoisonEssaim
InsomniaSniperPV
70Atq
90Déf
70SpA
60SpD
70Vit
40BST
400
RU
ArmaldoRockBugArmurbastonGlissadePV
75Atq
125Déf
100SpA
70SpD
80Vit
45BST
495
RU
CarmaduraFirePsychicTorcheArmurouilléePV
85Atq
60Déf
100SpA
125SpD
80Vit
75BST
525
RU
CocotineFairyCoeur SoinAroma-VoilePV
101Atq
72Déf
72SpA
99SpD
89Vit
29BST
462
RU
ArtikodinIceFlyingPressionRideau NeigePV
90Atq
85Déf
100SpA
95SpD
125Vit
85BST
580
RU
Artikodin-GalarPsychicFlyingBattantPV
90Atq
85Déf
85SpA
125SpD
100Vit
95BST
580
RU
NanméouïeNormalCoeur Soin
Régé-ForceMaladressePV
103Atq
60Déf
86SpA
60SpD
86Vit
50BST
445
RU
Nanméouïe-MégaNormalFairyCoeur SoinPV
103Atq
60Déf
126SpA
80SpD
126Vit
50BST
545
RU
DragmaraRockIcePeau GeléeAlerte NeigePV
123Atq
77Déf
72SpA
99SpD
92Vit
58BST
521
RU
SéracrawlIceTempo Perso
Corps GelFermetéPV
95Atq
117Déf
184SpA
44SpD
46Vit
28BST
514
RU
Séracrawl-HisuiIceRockPrognathe
Corps GelFermetéPV
95Atq
127Déf
184SpA
34SpD
36Vit
38BST
514
RU
CréfadetPsychicLévitationPV
75Atq
125Déf
70SpA
125SpD
70Vit
115BST
580
RU
AzumarillWaterFairyIsograisse
ColoforceHerbivorePV
100Atq
50Déf
80SpA
60SpD
80Vit
50BST
420
RU
BranetteGhostInsomnia
FouilleCorps MauditPV
64Atq
115Déf
65SpA
83SpD
63Vit
65BST
455
RU
GolgopatheRockWaterGriffe Dure
SniperPickpocketPV
72Atq
105Déf
115SpA
54SpD
86Vit
68BST
500
RU
HastacudaWaterGlissadePropulseurPV
61Atq
123Déf
60SpA
60SpD
50Vit
136BST
490
RU
ParagruelWaterGhostGlissade
AdaptabilitéBrise MoulePV
120Atq
112Déf
65SpA
80SpD
75Vit
78BST
530
RU
Paragruel-FWaterGhostGlissade
AdaptabilitéBrise MoulePV
120Atq
92Déf
65SpA
100SpD
75Vit
78BST
530
RU
BargantuaWaterTéméraire
AdaptabilitéBrise MoulePV
70Atq
92Déf
65SpA
80SpD
55Vit
98BST
460
RU
Bargantua-BleuWaterTête de Roc
AdaptabilitéBrise MoulePV
70Atq
92Déf
65SpA
80SpD
55Vit
98BST
460
RU
Bargantua-BlancWaterPhobique
AdaptabilitéBrise MoulePV
70Atq
92Déf
65SpA
80SpD
55Vit
98BST
460
RU
BastiodonRockSteelFermetéAnti-BruitPV
60Atq
52Déf
168SpA
47SpD
138Vit
30BST
495
RU
PolagriffeIceRideau Neige
Chasse-NeigeGlissadePV
95Atq
130Déf
80SpA
70SpD
80Vit
50BST
505
RU
CharmillonBugFlyingEssaimRivalitéPV
60Atq
70Déf
50SpA
100SpD
50Vit
65BST
395
RU
DardargnanBugPoisonEssaimSniperPV
65Atq
90Déf
40SpA
45SpD
80Vit
75BST
395
RU
Dardargnan-MégaBugPoisonAdaptabilitéPV
65Atq
150Déf
40SpA
15SpD
80Vit
145BST
495
RU
NeitramPsychicTélépathe
SynchroAnalystePV
75Atq
75Déf
75SpA
125SpD
95Vit
40BST
485
RU
AmpibidouElectricGrecharge
StatikMoiteurPV
109Atq
64Déf
91SpA
103SpD
83Vit
45BST
495
RU
JoliflorGrassChlorophylleCoeur SoinPV
75Atq
80Déf
95SpA
90SpD
100Vit
50BST
490
RU
CheloursNormalFightingBoule de Poils
MaladresseTensionPV
120Atq
125Déf
80SpA
55SpD
60Vit
60BST
500
RU
CastornoNormalWaterSimple
InconscientLunatiquePV
79Atq
85Déf
60SpA
55SpD
60Vit
71BST
410
RU
TortankWaterTorrentCuvettePV
79Atq
83Déf
100SpA
85SpD
105Vit
78BST
530
RU
LeuphorieNormalMédic Nature
SérénitéCoeur SoinPV
255Atq
10Déf
10SpA
75SpD
135Vit
55BST
540
RU
FulgudogElectricPrognatheBattantPV
69Atq
90Déf
60SpA
90SpD
60Vit
121BST
490
RU
LestombaileFlyingDarkCoeur de Coq
Regard VifPorte-RochePV
70Atq
103Déf
85SpA
60SpD
85Vit
82BST
485
RU
FrisonNormalTéméraire
HerbivoreAnti-BruitPV
95Atq
110Déf
95SpA
40SpD
95Vit
55BST
490
RU
VirevorreurGrassGhostAéroportéInfiltrationPV
55Atq
115Déf
70SpA
80SpD
70Vit
90BST
480
RU
GueriaigleNormalFlyingRegard Vif
Sans LimiteAcharnéPV
100Atq
123Déf
75SpA
57SpD
75Vit
80BST
510
RU
Gueriaigle-HisuiPsychicFlyingRegard Vif
Sans LimiteLentiteintéePV
110Atq
83Déf
70SpA
112SpD
70Vit
65BST
510
RU
ChapignonGrassFightingPose Spore
Soin PoisonTechnicienPV
60Atq
130Déf
80SpA
60SpD
60Vit
70BST
460
RU
ArchéodongSteelPsychicLévitation
IgnifugéHeavy MetalPV
67Atq
89Déf
116SpA
79SpD
116Vit
33BST
500
RU
Fongus-FurieGrassDarkPaléosynthèsePV
111Atq
127Déf
99SpA
79SpD
99Vit
55BST
570
RU
DenticrisseWaterPsychicCorps Coloré
PrognathePeau MiraclePV
68Atq
105Déf
70SpA
70SpD
70Vit
92BST
475
RU
PapilusionBugFlyingOeil ComposéLentiteintéePV
60Atq
45Déf
50SpA
90SpD
80Vit
70BST
395
RU
CacturneGrassDarkVoile SableAbsorb EauPV
70Atq
115Déf
60SpA
115SpD
60Vit
55BST
475
RU
SylveroyPsychicGrassTensionPV
100Atq
80Déf
80SpA
80SpD
80Vit
80BST
500
RU
CaméruptFireGroundArmumagma
Solide RocColériquePV
70Atq
100Déf
70SpA
105SpD
75Vit
40BST
460
RU
Camérupt-MégaFireGroundSans LimitePV
70Atq
120Déf
100SpA
145SpD
105Vit
20BST
560
RU
StrassieRockFairyCorps SainFermetéPV
50Atq
50Déf
150SpA
50SpD
150Vit
50BST
500
RU
VortenteGrassLévitationPV
74Atq
100Déf
72SpA
90SpD
72Vit
46BST
454
RU
MégapagosWaterRockSolide Roc
FermetéGlissadePV
74Atq
108Déf
133SpA
83SpD
65Vit
32BST
495
RU
MorphéoNormalMétéoPV
70Atq
70Déf
70SpA
70SpD
70Vit
70BST
420
RU
CelebiPsychicGrassMédic NaturePV
100Atq
100Déf
100SpA
100SpD
100Vit
100BST
600
RU
ScolocendreFireBugTorche
Écran FuméeCorps ArdentPV
100Atq
115Déf
65SpA
90SpD
90Vit
65BST
525
RU
BalbalèzeIceIsograisse
Chasse-NeigeSans LimitePV
170Atq
113Déf
65SpA
45SpD
55Vit
73BST
521
RU
LugulabreGhostFireTorche
Corps ArdentInfiltrationPV
60Atq
55Déf
90SpA
145SpD
90Vit
80BST
520
RU
DracaufeuFireFlyingBrasierForce SoleilPV
78Atq
84Déf
78SpA
109SpD
85Vit
100BST
534
RU
PijakoNormalFlyingRegard Vif
Pieds ConfusCoeur de CoqPV
76Atq
65Déf
45SpA
92SpD
42Vit
91BST
411
RU
CeriflorGrassDon FloralPV
70Atq
60Déf
70SpA
87SpD
78Vit
85BST
450
RU
BlindépiqueGrassFightingEngraisPare-BallesPV
88Atq
107Déf
122SpA
74SpD
75Vit
64BST
530
RU
ÉokoPsychicLévitationPV
75Atq
50Déf
80SpA
95SpD
90Vit
65BST
455
RU
PashmillaNormalJoli Sourire
TechnicienMulti-CoupsPV
75Atq
95Déf
60SpA
65SpD
60Vit
115BST
470
RU
GamblastWaterMéga BlasterPV
71Atq
73Déf
88SpA
120SpD
89Vit
59BST
500
RU
KaorineGroundPsychicLévitationPV
60Atq
70Déf
105SpA
70SpD
120Vit
75BST
500
RU
CrustabriWaterIceCoque Armure
Multi-CoupsEnvelocapePV
50Atq
95Déf
180SpA
85SpD
45Vit
70BST
525
RU
MonthraciteRockFireTurbine
Corps ArdentTorchePV
110Atq
80Déf
120SpA
80SpD
90Vit
30BST
510
RU
CobaltiumSteelFightingCoeur NoblePV
91Atq
90Déf
129SpA
90SpD
72Vit
108BST
580
RU
TutankaferGhostMomiePV
58Atq
50Déf
145SpA
95SpD
105Vit
30BST
483
RU
GuérilandeFairyFlora-Voile
PrioguérisonMédic NaturePV
51Atq
52Déf
90SpA
82SpD
110Vit
100BST
485
RU
BétochefFightingCran
Sans LimitePoing de FerPV
105Atq
140Déf
95SpA
55SpD
65Vit
45BST
505
RU
PachyradjahSteelSans LimiteHeavy MetalPV
122Atq
130Déf
69SpA
80SpD
69Vit
30BST
500
RU
CorayonWaterRockAgitation
Médic NatureRégé-ForcePV
65Atq
55Déf
95SpA
65SpD
95Vit
35BST
410
RU
CrabominableFightingIceHyper Cutter
Poing de FerColériquePV
97Atq
132Déf
77SpA
62SpD
67Vit
43BST
478
RU
VacilysRockGrassVentouseLavaboPV
86Atq
81Déf
97SpA
81SpD
107Vit
43BST
495
RU
NigosierFlyingWaterDégobagePV
70Atq
85Déf
55SpA
85SpD
95Vit
85BST
475
RU
ColhomardWaterDarkHyper Cutter
Coque ArmureAdaptabilitéPV
63Atq
120Déf
85SpA
90SpD
55Vit
55BST
468
RU
CresseliaPsychicLévitationPV
120Atq
70Déf
110SpA
75SpD
120Vit
85BST
580
RU
NostenferPoisonFlyingAttentionInfiltrationPV
85Atq
90Déf
80SpA
70SpD
80Vit
130BST
535
RU
CrabaraqueBugRockFermeté
Coque ArmureArmurouilléePV
70Atq
105Déf
125SpA
65SpD
75Vit
45BST
485
RU
HexagelIceLévitationPV
80Atq
50Déf
50SpA
95SpD
135Vit
105BST
515
RU
CorayômeGhostArmurouilléeCorps CondamnéPV
60Atq
95Déf
50SpA
145SpD
130Vit
30BST
510
RU
MotorizardDragonNormalMueRégé-ForcePV
70Atq
95Déf
65SpA
85SpD
65Vit
121BST
501
RU
BriochienFairyBien CuitAroma-VoilePV
57Atq
80Déf
115SpA
50SpD
80Vit
95BST
477
RU
DarumachoFireSans LimiteMode TransePV
105Atq
140Déf
55SpA
30SpD
55Vit
95BST
480
RU
ArchéducGrassGhostEngraisLongue PortéePV
78Atq
107Déf
75SpA
100SpD
100Vit
70BST
530
RU
Archéduc-HisuiGrassFightingEngraisQuerelleurPV
88Atq
112Déf
80SpA
95SpD
95Vit
60BST
530
RU
DedenneElectricFairyBajoues
RamassagePlusPV
67Atq
58Déf
57SpA
81SpD
67Vit
101BST
431
RU
DelcattyNormalJoli Sourire
NormalisePeau MiraclePV
70Atq
65Déf
65SpA
55SpD
55Vit
90BST
400
RU
CadoizoIceFlyingEsprit Vital
AgitationInsomniaPV
45Atq
55Déf
45SpA
65SpD
45Vit
75BST
330
RU
GoupelinFirePsychicBrasierMagicienPV
75Atq
69Déf
72SpA
114SpD
100Vit
104BST
534
RU
LamantineWaterIceIsograisse
HydratationCorps GelPV
90Atq
70Déf
80SpA
70SpD
95Vit
70BST
475
RU
SinistrailGhostGrassExpert AcierPV
70Atq
131Déf
100SpA
86SpD
90Vit
40BST
517
RU
DiancieRockFairyCorps SainPV
50Atq
100Déf
150SpA
100SpD
150Vit
50BST
600
RU
ExcavarenneNormalGroundRamassage
BajouesColoforcePV
85Atq
56Déf
77SpA
50SpD
77Vit
78BST
423
RU
PomdramourGrassDragonNectar Mielleux
GloutonnerieGluePV
80Atq
80Déf
110SpA
95SpD
80Vit
40BST
485
RU
MétamorphNormalÉchauffementImposteurPV
48Atq
48Déf
48SpA
48SpD
48Vit
48BST
288
RU
DodrioNormalFlyingFuite
MatinalPieds ConfusPV
60Atq
110Déf
70SpA
60SpD
60Vit
110BST
470
RU
DonphanGroundFermetéVoile SablePV
90Atq
120Déf
120SpA
60SpD
60Vit
50BST
500
RU
KravarechPoisonDragonPoint Poison
ToxitoucheAdaptabilitéPV
65Atq
75Déf
90SpA
97SpD
123Vit
44BST
494
RU
DraïeulNormalDragonDracolère
HerbivoreCiel GrisPV
78Atq
60Déf
85SpA
135SpD
91Vit
36BST
485
RU
DrascorePoisonDarkArmurbaston
SniperRegard VifPV
70Atq
90Déf
110SpA
60SpD
75Vit
95BST
500
RU
TorgamordWaterRockPrognathe
Coque ArmureGlissadePV
90Atq
115Déf
90SpA
48SpD
68Vit
74BST
485
RU
GrodriveGhostFlyingBoom Final
DélestageRage BrûlurePV
150Atq
80Déf
44SpA
90SpD
54Vit
80BST
498
RU
DrakkarminDragonPeau Dure
Sans LimiteBrise MoulePV
77Atq
120Déf
90SpA
60SpD
90Vit
48BST
485
RU
MoumouflonNormalBoule de Poils
ImpassiblePare-BallesPV
72Atq
80Déf
100SpA
60SpD
90Vit
88BST
490
RU
DeusolourdoNormalSérénité
FuitePhobiquePV
125Atq
100Déf
80SpA
85SpD
75Vit
55BST
520
RU
Deusolourdo-TripleNormalSérénité
FuitePhobiquePV
125Atq
100Déf
80SpA
85SpD
75Vit
55BST
520
RU
TriopikeurGroundVoile Sable
Piège SableForce SablePV
35Atq
100Déf
50SpA
50SpD
70Vit
120BST
425
RU
Triopikeur-AlolaGroundSteelVoile Sable
Mèche RebelleForce SablePV
35Atq
100Déf
60SpA
50SpD
70Vit
110BST
425
RU
DuralugonSteelDragonLight Metal
Heavy MetalNerfs d'AcierPV
70Atq
95Déf
115SpA
120SpD
50Vit
85BST
535
RU
FermiteBugSteelEssaim
AgitationAbsentéismePV
58Atq
109Déf
112SpA
48SpD
48Vit
109BST
484
RU
NoctunoirGhostPressionFouillePV
45Atq
100Déf
135SpA
65SpD
135Vit
45BST
525
RU
PapinoxBugPoisonÉcran PoudreOeil ComposéPV
60Atq
50Déf
70SpA
50SpD
90Vit
65BST
385
RU
OhmassacreElectricLévitationPV
85Atq
115Déf
80SpA
105SpD
80Vit
50BST
515
RU
BekaglaçonIceTête de GelPV
75Atq
80Déf
110SpA
65SpD
90Vit
50BST
470
RU
BlancotonGrassEffilochage
Régé-ForcePose SporePV
60Atq
50Déf
90SpA
80SpD
120Vit
60BST
460
RU
ÉlekableElectricMotoriséEsprit VitalPV
75Atq
123Déf
67SpA
95SpD
85Vit
95BST
540
RU
ÉlectrodeElectricAnti-Bruit
StatikBoom FinalPV
60Atq
50Déf
70SpA
80SpD
80Vit
150BST
490
RU
Électrode-HisuiElectricGrassAnti-Bruit
StatikBoom FinalPV
60Atq
50Déf
70SpA
80SpD
80Vit
150BST
490
RU
RoitiflamFireFightingBrasierTémérairePV
110Atq
123Déf
65SpA
100SpD
65Vit
65BST
528
RU
EmolgaElectricFlyingStatikMotoriséPV
55Atq
75Déf
60SpA
75SpD
60Vit
103BST
428
RU
PingoléonWaterSteelTorrentBattantPV
84Atq
86Déf
88SpA
111SpD
101Vit
60BST
530
RU
Amovénus-TotemFairyFlyingEnvelocapePV
74Atq
115Déf
110SpA
135SpD
100Vit
46BST
580
RU
EnteiFirePressionAttentionPV
115Atq
115Déf
85SpA
90SpD
75Vit
100BST
580
RU
LançargotBugSteelEssaim
Coque ArmureEnvelocapePV
70Atq
135Déf
105SpA
60SpD
105Vit
20BST
495
RU
MentaliPsychicSynchroMiroir MagikPV
65Atq
65Déf
60SpA
130SpD
95Vit
110BST
525
RU
NoadkokoGrassPsychicChlorophylleRécoltePV
95Atq
95Déf
85SpA
125SpD
75Vit
55BST
530
RU
Noadkoko-AlolaGrassDragonFouilleRécoltePV
95Atq
105Déf
85SpA
125SpD
75Vit
45BST
530
RU
BrouhabamNormalAnti-BruitQuerelleurPV
104Atq
91Déf
63SpA
91SpD
73Vit
68BST
490
RU
HexadronFightingArmurbastonAcharnéPV
65Atq
100Déf
100SpA
70SpD
60Vit
75BST
470
RU
CanartichoNormalFlyingRegard Vif
AttentionAcharnéPV
52Atq
90Déf
55SpA
58SpD
62Vit
60BST
377
RU
FarigirafNormalPsychicRuminant
Armure CaudaleHerbivorePV
120Atq
90Déf
70SpA
110SpD
70Vit
60BST
520
RU
RapasdepicNormalFlyingRegard VifSniperPV
65Atq
90Déf
65SpA
61SpD
61Vit
100BST
442
RU
AligatueurWaterTorrentSans LimitePV
85Atq
105Déf
100SpA
79SpD
83Vit
78BST
530
RU
FavianosPoisonFairyChaîne ToxiqueTechnicienPV
88Atq
91Déf
82SpA
70SpD
125Vit
99BST
555
RU
FlamenrouleFlyingFightingQuerelleur
Pieds ConfusCollabPV
82Atq
115Déf
74SpA
75SpD
64Vit
90BST
500
RU
PomdrapiGrassDragonMûrissement
GloutonnerieAgitationPV
70Atq
110Déf
80SpA
95SpD
60Vit
70BST
485
RU
PyroliFireTorcheCranPV
65Atq
130Déf
60SpA
95SpD
110Vit
65BST
525
RU
MustéflottWaterGlissadeIgnifu-VoilePV
85Atq
105Déf
55SpA
85SpD
50Vit
115BST
495
RU
FlorgesFairyFlora-VoileSymbiosePV
78Atq
65Déf
68SpA
112SpD
154Vit
75BST
552
RU
LibégonGroundDragonLévitationPV
80Atq
100Déf
80SpA
80SpD
80Vit
100BST
520
RU
ForetressBugSteelFermetéEnvelocapePV
75Atq
90Déf
140SpA
60SpD
60Vit
40BST
465
RU
MomartikIceGhostRideau NeigeCorps MauditPV
70Atq
80Déf
70SpA
80SpD
70Vit
110BST
480
RU
BeldeneigeIceBugÉcran PoudreÉcailles GlacéesPV
70Atq
65Déf
60SpA
125SpD
90Vit
65BST
475
RU
CouafarelNormalToison ÉpaissePV
75Atq
80Déf
60SpA
65SpD
90Vit
102BST
472
RU
FouinarNormalFuite
Regard VifFouillePV
85Atq
76Déf
64SpA
45SpD
55Vit
90BST
415
RU
GallamePsychicFightingImpassible
IncisifCoeur NoblePV
68Atq
125Déf
65SpA
65SpD
115Vit
80BST
518
RU
MygavoltBugElectricOeil Composé
TensionEssaimPV
70Atq
77Déf
60SpA
97SpD
60Vit
108BST
472
RU
MiasmaxPoisonPuanteur
ArmurouilléeBoom FinalPV
80Atq
95Déf
82SpA
60SpD
82Vit
75BST
474
RU
GardevoirPsychicFairySynchro
CalqueTélépathePV
68Atq
65Déf
65SpA
125SpD
115Vit
80BST
518
RU
GigalitheRockFermeté
Sable VolantForce SablePV
85Atq
135Déf
130SpA
60SpD
80Vit
25BST
515
RU
GivraliIceRideau NeigeCorps GelPV
65Atq
60Déf
110SpA
130SpD
95Vit
65BST
525
RU
OniglaliIceAttention
Corps GelLunatiquePV
80Atq
80Déf
80SpA
80SpD
80Vit
80BST
480
RU
Oniglali-MégaIcePeau GeléePV
80Atq
120Déf
80SpA
120SpD
80Vit
100BST
580
RU
BlizzevalIceBlanche RuadePV
100Atq
145Déf
130SpA
65SpD
110Vit
30BST
580
RU
ChevroumGrassHerbivoreToison HerbuePV
123Atq
100Déf
62SpA
97SpD
81Vit
68BST
531
RU
AkwakwakWaterMoiteur
Ciel GrisGlissadePV
80Atq
82Déf
78SpA
95SpD
80Vit
85BST
500
RU
GrolemRockGroundTête de Roc
FermetéVoile SablePV
80Atq
120Déf
130SpA
55SpD
65Vit
45BST
495
RU
Grolem-AlolaRockElectricMagnépiège
FermetéPeau ÉlectriquePV
80Atq
120Déf
130SpA
55SpD
65Vit
45BST
495
RU
GolemastocGroundGhostPoing de Fer
MaladresseAnnule GardePV
89Atq
124Déf
80SpA
55SpD
80Vit
55BST
483
RU
MuplodocusDragonHerbivore
HydratationPoisseuxPV
90Atq
100Déf
70SpA
110SpD
150Vit
80BST
600
RU
RosabyssWaterGlissadeHydratationPV
55Atq
84Déf
105SpA
114SpD
75Vit
52BST
485
RU
SidérellaPsychicFouille
BattantMarque OmbrePV
70Atq
55Déf
95SpA
95SpD
110Vit
65BST
490
RU
BanshitrouyeGhostGrassRamassage
FouilleInsomniaPV
65Atq
90Déf
122SpA
58SpD
75Vit
84BST
494
RU
Banshitrouye-MaxiGhostGrassRamassage
FouilleInsomniaPV
75Atq
95Déf
122SpA
58SpD
75Vit
69BST
494
RU
Banshitrouye-MiniGhostGrassRamassage
FouilleInsomniaPV
55Atq
85Déf
122SpA
58SpD
75Vit
99BST
494
RU
Banshitrouye-UltraGhostGrassRamassage
FouilleInsomniaPV
85Atq
100Déf
122SpA
58SpD
75Vit
54BST
494
RU
Tag-TagPoisonNormalDélestage
ToxitoucheFarceurPV
63Atq
95Déf
65SpA
80SpD
72Vit
110BST
485
RU
GranbullFairyIntimidation
Pied VélocePhobiquePV
90Atq
120Déf
75SpA
60SpD
60Vit
45BST
450
RU
KrakosFightingÉchauffementTechnicienPV
80Atq
118Déf
90SpA
70SpD
80Vit
42BST
480
RU
RongrigouNormalBajouesGloutonneriePV
120Atq
95Déf
95SpA
55SpD
75Vit
20BST
460
RU
AngoliathDarkFairyFarceur
FouillePickpocketPV
95Atq
120Déf
65SpA
95SpD
75Vit
60BST
510
RU
GroretPsychicIsograisse
Tempo PersoGloutonneriePV
80Atq
45Déf
65SpA
90SpD
110Vit
80BST
470
RU
ArgousteNormalFilature
PrognatheAdaptabilitéPV
88Atq
110Déf
60SpA
55SpD
60Vit
45BST
418
RU
EngloutyranDarkDragonBoost ChimèrePV
223Atq
101Déf
53SpA
97SpD
53Vit
43BST
570
RU
HariyamaFightingIsograisse
CranSans LimitePV
144Atq
120Déf
60SpA
40SpD
60Vit
50BST
474
RU
AflamanoirFireGloutonnerie
TorcheÉcran FuméePV
85Atq
97Déf
66SpA
105SpD
66Vit
65BST
484
RU
IguoltaElectricNormalPeau Sèche
Voile SableForce SoleilPV
62Atq
55Déf
52SpA
109SpD
94Vit
109BST
481
RU
ScarhinoBugFightingEssaim
CranImpudencePV
80Atq
125Déf
75SpA
40SpD
95Vit
85BST
500
RU
HippodocusGroundSable VolantForce SablePV
108Atq
112Déf
118SpA
68SpD
72Vit
47BST
525
RU
TygnonFightingRegard Vif
Poing de FerAttentionPV
50Atq
105Déf
79SpA
35SpD
110Vit
76BST
455
RU
KickleeFightingÉchauffement
TéméraireDélestagePV
50Atq
120Déf
53SpA
35SpD
110Vit
87BST
455
RU
KapoeraFightingIntimidation
TechnicienImpassiblePV
50Atq
95Déf
95SpA
35SpD
110Vit
70BST
455
RU
CorbossDarkFlyingInsomnia
ChanceuxImpudencePV
100Atq
125Déf
52SpA
105SpD
52Vit
71BST
505
RU
HoopaPsychicGhostMagicienPV
80Atq
110Déf
60SpA
150SpD
130Vit
70BST
600
RU
DémolosseDarkFireMatinal
TorcheTensionPV
75Atq
90Déf
50SpA
110SpD
80Vit
95BST
500
RU
Démolosse-MégaDarkFireForce SoleilPV
75Atq
90Déf
90SpA
140SpD
90Vit
115BST
600
RU
TomberroGhostBaigne SableBoule de PoilsPV
72Atq
101Déf
100SpA
50SpD
97Vit
68BST
488
RU
SerpangWaterGlissadeIgnifu-VoilePV
55Atq
104Déf
105SpA
94SpD
75Vit
52BST
485
RU
TrioxhydreDarkDragonLévitationPV
92Atq
105Déf
90SpA
125SpD
90Vit
98BST
600
RU
HypnomadePsychicInsomnia
PrédictionAttentionPV
85Atq
73Déf
70SpA
73SpD
115Vit
67BST
483
RU
LumivoleBugBenêt
LentiteintéeFarceurPV
65Atq
47Déf
75SpA
73SpD
85Vit
85BST
430
RU
FélinfernoFireDarkBrasierIntimidationPV
95Atq
115Déf
90SpA
80SpD
90Vit
60BST
530
RU
WimessirPsychicNormalAttention
SynchroCréa-PsyPV
60Atq
65Déf
55SpA
105SpD
95Vit
95BST
475
RU
Wimessir-FPsychicNormalTempo Perso
SynchroCréa-PsyPV
70Atq
55Déf
65SpA
95SpD
105Vit
85BST
475
RU
SimiabrazFireFightingBrasierPoing de FerPV
76Atq
104Déf
71SpA
104SpD
71Vit
108BST
534
RU
LézargusWaterTorrentSniperPV
70Atq
85Déf
65SpA
125SpD
65Vit
120BST
530
RU
Têtes-de-FerDarkFlyingCharge QuantiquePV
94Atq
80Déf
86SpA
122SpD
80Vit
108BST
570
RU
Épine-de-FerRockElectricCharge QuantiquePV
100Atq
134Déf
110SpA
70SpD
84Vit
72BST
570
RU
MoyadeWaterGhostAbsorb Eau
Corps MauditMoiteurPV
100Atq
60Déf
70SpA
85SpD
105Vit
60BST
480
RU
VoltaliElectricAbsorb VoltPied VélocePV
65Atq
65Déf
60SpA
110SpD
95Vit
130BST
525
RU
CotovolGrassFlyingChlorophylle
Feuille GardeInfiltrationPV
75Atq
55Déf
70SpA
55SpD
95Vit
110BST
460
RU
LippoutouIcePsychicBenêt
PrédictionPeau SèchePV
65Atq
50Déf
35SpA
115SpD
95Vit
95BST
455
RU
KabutopsRockWaterGlissade
ArmurbastonArmurouilléePV
60Atq
115Déf
105SpA
65SpD
70Vit
80BST
495
RU
KangourexNormalMatinal
QuerelleurAttentionPV
105Atq
95Déf
80SpA
40SpD
80Vit
90BST
490
RU
KecleonNormalHomochromieProtéenPV
60Atq
90Déf
70SpA
60SpD
120Vit
40BST
440
RU
FulgulairoElectricFlyingTurbine Éolienne
Absorb VoltBattantPV
70Atq
70Déf
60SpA
105SpD
60Vit
125BST
490
RU
HyporoiWaterDragonGlissade
SniperMoiteurPV
75Atq
95Déf
95SpA
95SpD
95Vit
85BST
540
RU
KrabbossWaterHyper Cutter
Coque ArmureSans LimitePV
55Atq
130Déf
115SpA
50SpD
50Vit
75BST
475
RU
CraparoiRockCourroupace
Coque ArmureRégé-ForcePV
70Atq
100Déf
115SpA
35SpD
55Vit
75BST
450
RU
TrousselinSteelFairyFarceurMagicienPV
57Atq
80Déf
91SpA
80SpD
87Vit
75BST
470
RU
CliticlicSteelPlus
MinusCorps SainPV
60Atq
100Déf
115SpA
70SpD
85Vit
90BST
520
RU
DodoalaNormalHypersommeilPV
65Atq
115Déf
65SpA
75SpD
95Vit
65BST
480
RU
MélokrikBugEssaimTechnicienPV
77Atq
85Déf
51SpA
55SpD
51Vit
65BST
384
RU
CrocoribleGroundDarkIntimidation
ImpudenceColériquePV
95Atq
117Déf
80SpA
65SpD
70Vit
92BST
519
RU
LanturnWaterElectricAbsorb Volt
LumiattiranceAbsorb EauPV
125Atq
58Déf
58SpA
76SpD
76Vit
67BST
460
RU
LokhlassWaterIceAbsorb Eau
Coque ArmureHydratationPV
130Atq
85Déf
80SpA
85SpD
95Vit
60BST
535
RU
LatiasDragonPsychicLévitationPV
80Atq
80Déf
90SpA
110SpD
130Vit
110BST
600
RU
PhyllaliGrassFeuille GardeChlorophyllePV
65Atq
110Déf
130SpA
60SpD
65Vit
95BST
525
RU
ManternelBugGrassEssaim
ChlorophylleEnvelocapePV
75Atq
103Déf
80SpA
70SpD
80Vit
92BST
500
RU
CoxyclaqueBugFlyingEssaim
MatinalPoing de FerPV
55Atq
35Déf
50SpA
55SpD
110Vit
85BST
390
RU
CoudlangueNormalTempo Perso
BenêtCiel GrisPV
110Atq
85Déf
95SpA
80SpD
95Vit
50BST
515
RU
LéopardusDarkÉchauffement
DélestageFarceurPV
64Atq
88Déf
50SpA
88SpD
50Vit
106BST
446
RU
FragiladyGrassChlorophylle
Tempo PersoFeuille GardePV
70Atq
60Déf
75SpA
110SpD
75Vit
90BST
480
RU
LinéonNormalRamassage
GloutonneriePied VélocePV
78Atq
70Déf
61SpA
50SpD
61Vit
100BST
420
RU
GambexBugDarkEssaimLentiteintéePV
71Atq
102Déf
78SpA
52SpD
55Vit
92BST
450
RU
LockpinNormalJoli Sourire
MaladresseÉchauffementPV
65Atq
76Déf
84SpA
54SpD
96Vit
105BST
480
RU
LucarioFightingSteelImpassible
AttentionCoeur NoblePV
70Atq
110Déf
70SpA
115SpD
70Vit
90BST
525
RU
LudicoloWaterGrassGlissade
CuvetteTempo PersoPV
80Atq
70Déf
70SpA
90SpD
100Vit
70BST
480
RU
LuminéonWaterGlissade
LavaboIgnifu-VoilePV
69Atq
69Déf
76SpA
69SpD
86Vit
91BST
460
RU
SélérocRockPsychicLévitationPV
90Atq
55Déf
65SpA
95SpD
85Vit
70BST
460
RU
FloramantisGrassFeuille GardeContestationPV
70Atq
105Déf
90SpA
80SpD
90Vit
45BST
480
RU
LovdiscWaterGlissadeHydratationPV
43Atq
30Déf
55SpA
40SpD
65Vit
97BST
330
RU
LuxrayElectricRivalité
IntimidationCranPV
80Atq
120Déf
79SpA
95SpD
79Vit
70BST
523
RU
LougarocRockRegard Vif
Baigne SableImpassiblePV
75Atq
115Déf
65SpA
55SpD
65Vit
112BST
487
RU
Lougaroc-CrépusculeRockGriffe DurePV
75Atq
117Déf
65SpA
55SpD
65Vit
110BST
487
RU
Lougaroc-NocturneRockRegard Vif
Esprit VitalAnnule GardePV
85Atq
115Déf
75SpA
55SpD
75Vit
82BST
487
RU
DogrinoDarkIntimidation
Chien de GardeFilaturePV
80Atq
120Déf
90SpA
60SpD
70Vit
85BST
505
RU
MackogneurFightingCran
Annule GardeImpassiblePV
90Atq
130Déf
80SpA
65SpD
85Vit
55BST
505
RU
VolcaropodFireRockArmumagma
Corps ArdentArmurouilléePV
60Atq
50Déf
120SpA
90SpD
80Vit
30BST
430
RU
MaganonFireCorps ArdentEsprit VitalPV
75Atq
95Déf
67SpA
125SpD
95Vit
83BST
540
RU
MagnézoneElectricSteelMagnépiège
FermetéAnalystePV
70Atq
70Déf
115SpA
130SpD
90Vit
60BST
535
RU
SepiatroceDarkPsychicContestation
VentouseInfiltrationPV
86Atq
92Déf
88SpA
68SpD
75Vit
73BST
482
RU
VaututriceDarkFlyingCoeur de Coq
EnvelocapeArmurouilléePV
110Atq
65Déf
105SpA
55SpD
95Vit
80BST
510
RU
ÉlecsprintElectricStatik
ParatonnerreMinusPV
70Atq
75Déf
60SpA
105SpD
60Vit
105BST
475
RU
Élecsprint-MégaElectricIntimidationPV
70Atq
75Déf
80SpA
135SpD
80Vit
135BST
575
RU
DémantaWaterFlyingGlissade
Absorb EauIgnifu-VoilePV
85Atq
40Déf
70SpA
80SpD
140Vit
70BST
485
RU
MaracachiGrassAbsorb Eau
ChlorophylleLavaboPV
75Atq
86Déf
67SpA
106SpD
67Vit
60BST
461
RU
OssatueurGroundTête de Roc
ParatonnerreArmurbastonPV
60Atq
80Déf
110SpA
50SpD
80Vit
45BST
425
RU
Ossatueur-AlolaFireGhostCorps Maudit
ParatonnerreTête de RocPV
60Atq
80Déf
110SpA
50SpD
80Vit
45BST
425
RU
MaskadraBugFlyingIntimidationTensionPV
70Atq
60Déf
62SpA
100SpD
82Vit
80BST
454
RU
FamignolNormalGarde Amie
BajouesTechnicienPV
74Atq
75Déf
70SpA
65SpD
75Vit
111BST
470
RU
Famignol-QuatreNormalGarde Amie
BajouesTechnicienPV
74Atq
75Déf
70SpA
65SpD
75Vit
111BST
470
RU
MysdibuleSteelFairyHyper Cutter
IntimidationSans LimitePV
50Atq
85Déf
85SpA
55SpD
55Vit
50BST
380
RU
CharminaFightingPsychicForce PureTélépathePV
60Atq
60Déf
75SpA
60SpD
75Vit
80BST
410
RU
MéganiumGrassEngraisFeuille GardePV
80Atq
82Déf
100SpA
83SpD
100Vit
80BST
525
RU
MeloettaNormalPsychicSérénitéPV
100Atq
77Déf
77SpA
128SpD
128Vit
90BST
600
RU
MeltanSteelMagnépiègePV
46Atq
65Déf
65SpA
55SpD
35Vit
34BST
300
RU
MistigrixPsychicRegard Vif
InfiltrationFarceurPV
74Atq
48Déf
76SpA
83SpD
81Vit
104BST
466
RU
Mistigrix-FPsychicRegard Vif
InfiltrationBattantPV
74Atq
48Déf
76SpA
83SpD
81Vit
104BST
466
RU
CréfolletPsychicLévitationPV
80Atq
105Déf
105SpA
105SpD
105Vit
80BST
580
RU
MétalosseSteelPsychicCorps SainLight MetalPV
80Atq
135Déf
130SpA
95SpD
90Vit
70BST
600
RU
ShaofouineFightingAttention
Régé-ForceTémérairePV
65Atq
125Déf
60SpA
95SpD
60Vit
105BST
510
RU
GrahyènaDarkIntimidation
Pied VéloceImpudencePV
70Atq
90Déf
70SpA
60SpD
60Vit
70BST
420
RU
MilobellusWaterÉcaille Spéciale
BattantJoli SourirePV
95Atq
60Déf
79SpA
100SpD
125Vit
81BST
540
RU
ÉcrémeuhNormalIsograisse
QuerelleurHerbivorePV
95Atq
80Déf
105SpA
40SpD
70Vit
100BST
490
RU
MimiquiGhostFairyFantômasquePV
55Atq
90Déf
80SpA
50SpD
105Vit
96BST
476
RU
MéténoRockFlyingBouclier-CarcanPV
60Atq
100Déf
60SpA
100SpD
60Vit
120BST
500
RU
NégapiElectricMinusAbsorb VoltPV
60Atq
40Déf
50SpA
75SpD
85Vit
95BST
405
RU
MagirêveGhostLévitationPV
60Atq
60Déf
60SpA
105SpD
105Vit
105BST
495
RU
MorpekoElectricDarkDéclic FringalePV
58Atq
95Déf
58SpA
70SpD
58Vit
97BST
436
RU
PapilordBugFlyingEssaimLentiteintéePV
70Atq
94Déf
50SpA
94SpD
50Vit
66BST
424
RU
M. MimePsychicFairyAnti-Bruit
FiltreTechnicienPV
40Atq
45Déf
65SpA
100SpD
120Vit
90BST
460
RU
M. GlaquetteIcePsychicPieds Confus
Brise-BarrièreCorps GelPV
80Atq
85Déf
75SpA
110SpD
100Vit
70BST
520
RU
BourrinosGroundTempo Perso
EnduranceAttentionPV
100Atq
125Déf
100SpA
55SpD
85Vit
35BST
500
RU
GrotadmorvPoisonPuanteur
GlueToxitouchePV
105Atq
105Déf
75SpA
65SpD
100Vit
50BST
500
RU
Grotadmorv-AlolaPoisonDarkToxitouche
GloutonnerieOsmosePV
105Atq
105Déf
75SpA
65SpD
100Vit
50BST
500
RU
FortusimiaPoisonPsychicChaîne ToxiqueFouillePV
88Atq
75Déf
66SpA
130SpD
90Vit
106BST
555
RU
MushanaPsychicPrédiction
SynchroTélépathePV
116Atq
55Déf
85SpA
107SpD
95Vit
29BST
487
RU
NecrozmaPsychicPrisme-ArmurePV
97Atq
107Déf
101SpA
127SpD
89Vit
79BST
600
RU
NidokingPoisonGroundPoint Poison
RivalitéSans LimitePV
81Atq
102Déf
77SpA
85SpD
75Vit
85BST
505
RU
NidoqueenPoisonGroundPoint Poison
RivalitéSans LimitePV
90Atq
92Déf
87SpA
75SpD
85Vit
76BST
505
RU
ZéroïdRockPoisonBoost ChimèrePV
109Atq
53Déf
47SpA
127SpD
131Vit
103BST
570
RU
FeunardFireTorcheSécheressePV
73Atq
76Déf
75SpA
81SpD
100Vit
100BST
505
RU
Feunard-AlolaIceFairyRideau NeigeAlerte NeigePV
73Atq
67Déf
75SpA
81SpD
100Vit
109BST
505
RU
NinjaskBugFlyingTurboInfiltrationPV
61Atq
90Déf
45SpA
50SpD
50Vit
160BST
456
RU
NoarfangNormalFlyingInsomnia
Regard VifLentiteintéePV
100Atq
50Déf
50SpA
86SpD
96Vit
70BST
452
RU
BruyverneFlyingDragonFouille
InfiltrationTélépathePV
85Atq
70Déf
80SpA
97SpD
80Vit
123BST
535
RU
IxonDarkNormalTéméraire
CranAcharnéPV
93Atq
90Déf
101SpA
60SpD
81Vit
95BST
520
RU
OctilleryWaterVentouse
SniperLunatiquePV
75Atq
105Déf
75SpA
105SpD
75Vit
45BST
480
RU
OgerponGrassAcharnéPV
80Atq
120Déf
84SpA
60SpD
96Vit
110BST
550
RU
FragroinNormalOdeur Tenace
GloutonnerieIsograissePV
110Atq
100Déf
75SpA
59SpD
80Vit
65BST
489
RU
Fragroin-FNormalAroma-Voile
GloutonnerieIsograissePV
115Atq
90Déf
70SpA
59SpD
90Vit
65BST
489
RU
FélicanisPoisonFightingChaîne ToxiqueChien de GardePV
88Atq
128Déf
115SpA
58SpD
86Vit
80BST
555
RU
AmonistarRockWaterGlissade
Coque ArmureArmurouilléePV
70Atq
60Déf
125SpA
115SpD
70Vit
55BST
495
RU
GouroutanNormalPsychicAttention
TélépatheSymbiosePV
90Atq
60Déf
80SpA
90SpD
110Vit
60BST
490
RU
AstronelleBugPsychicEssaim
FouilleTélépathePV
60Atq
45Déf
110SpA
80SpD
120Vit
90BST
505
RU
PlumelineFireFlyingDanseusePV
75Atq
70Déf
70SpA
98SpD
70Vit
93BST
476
RU
Plumeline-HulaPsychicFlyingDanseusePV
75Atq
70Déf
70SpA
98SpD
70Vit
93BST
476
RU
Plumeline-Pom-PomElectricFlyingDanseusePV
75Atq
70Déf
70SpA
98SpD
70Vit
93BST
476
RU
Plumeline-BuyōGhostFlyingDanseusePV
75Atq
70Déf
70SpA
98SpD
70Vit
93BST
476
RU
FerdeterSteelAbsorbe-TerreVoile SablePV
70Atq
85Déf
145SpA
60SpD
55Vit
65BST
480
RU
QwilpikDarkPoisonPoint Poison
GlissadeIntimidationPV
85Atq
115Déf
95SpA
65SpD
65Vit
85BST
510
RU
PachirisuElectricFuite
RamassageAbsorb VoltPV
60Atq
45Déf
70SpA
45SpD
90Vit
95BST
405
RU
TrépassableGhostGroundSable HumideVoile SablePV
85Atq
75Déf
110SpA
100SpD
75Vit
35BST
480
RU
PandarbareFightingDarkPoing de Fer
Brise MouleQuerelleurPV
95Atq
124Déf
78SpA
69SpD
71Vit
58BST
495
RU
ParasectBugGrassPose Spore
Peau SècheMoiteurPV
60Atq
95Déf
80SpA
60SpD
80Vit
30BST
405
RU
QuartermacFightingReceveurAcharnéPV
100Atq
120Déf
90SpA
40SpD
60Vit
80BST
490
RU
PohmarmotteElectricFightingAbsorb Volt
Médic NaturePoing de FerPV
70Atq
115Déf
70SpA
70SpD
60Vit
105BST
490
RU
BerserkattSteelArmurbaston
Griffe DureBoost AcierPV
70Atq
110Déf
100SpA
50SpD
60Vit
50BST
440
RU
PersianNormalÉchauffement
TechnicienTensionPV
65Atq
70Déf
60SpA
65SpD
65Vit
115BST
440
RU
Persian-AlolaDarkToison Épaisse
TechnicienPhobiquePV
65Atq
60Déf
60SpA
75SpD
65Vit
115BST
440
RU
PhioneWaterHydratationPV
80Atq
80Déf
80SpA
80SpD
80Vit
80BST
480
RU
RoucarnageNormalFlyingRegard Vif
Pieds ConfusCoeur de CoqPV
83Atq
80Déf
75SpA
70SpD
70Vit
101BST
479
RU
Roucarnage-MégaNormalFlyingAnnule GardePV
83Atq
80Déf
80SpA
135SpD
80Vit
121BST
579
RU
PikachuElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-AlolaElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-HoennElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-KalosElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-OriginalElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-PartenaireElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-SinnohElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-UnysElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
Pikachu-MondeElectricStatikParatonnerrePV
35Atq
55Déf
40SpA
50SpD
50Vit
90BST
320
RU
WattapikElectricParatonnerreCréa-ÉlecPV
48Atq
101Déf
95SpA
91SpD
85Vit
15BST
435
RU
ScarabruteBugHyper Cutter
Brise MouleImpudencePV
65Atq
125Déf
100SpA
55SpD
70Vit
85BST
500
RU
PosipiElectricPlusParatonnerrePV
60Atq
50Déf
40SpA
85SpD
75Vit
95BST
405
RU
TarpaudWaterAbsorb Eau
MoiteurCrachinPV
90Atq
75Déf
75SpA
90SpD
100Vit
70BST
500
RU
TartardWaterFightingAbsorb Eau
MoiteurGlissadePV
90Atq
95Déf
95SpA
70SpD
90Vit
70BST
510
RU
PolthégeistGhostArmurouilléeCorps MauditPV
60Atq
65Déf
65SpA
134SpD
114Vit
70BST
508
RU
Polthégeist-AntiqueGhostArmurouilléeCorps MauditPV
60Atq
65Déf
65SpA
134SpD
114Vit
70BST
508
RU
OratoriaWaterFairyTorrentHydrata-SonPV
80Atq
74Déf
74SpA
126SpD
116Vit
60BST
530
RU
TarinormeRockSteelFermeté
MagnépiègeForce SablePV
60Atq
55Déf
145SpA
75SpD
150Vit
40BST
525
RU
ChaffreuxNormalIsograisse
Tempo PersoAcharnéPV
71Atq
82Déf
64SpA
64SpD
59Vit
112BST
452
RU
NéméliosFireNormalRivalité
TensionImpudencePV
86Atq
68Déf
72SpA
109SpD
66Vit
106BST
507
RU
ConcombaffeWaterExpuls'OrganesInconscientPV
55Atq
60Déf
130SpA
30SpD
130Vit
5BST
410
RU
MaraisteWaterGroundMoiteur
Absorb EauInconscientPV
95Atq
85Déf
85SpA
65SpD
65Vit
35BST
430
RU
PalmavalWaterFightingTorrentImpudencePV
85Atq
120Déf
80SpA
85SpD
75Vit
85BST
530
RU
QwilfishWaterPoisonPoint Poison
GlissadeIntimidationPV
65Atq
95Déf
85SpA
55SpD
55Vit
85BST
440
RU
BérascaBugPsychicSynchroTélépathePV
75Atq
50Déf
85SpA
115SpD
100Vit
45BST
470
RU
RaichuElectricStatikParatonnerrePV
60Atq
90Déf
55SpA
90SpD
80Vit
110BST
485
RU
Raichu-AlolaElectricPsychicSurf CaudalPV
60Atq
85Déf
50SpA
95SpD
85Vit
110BST
485
RU
RaikouElectricPressionAttentionPV
90Atq
85Déf
75SpA
115SpD
100Vit
115BST
580
RU
CharkosRockBrise MouleSans LimitePV
97Atq
165Déf
60SpA
65SpD
50Vit
58BST
495
RU
GalopaFireFuite
TorcheCorps ArdentPV
65Atq
100Déf
70SpA
80SpD
80Vit
105BST
500
RU
Galopa-GalarPsychicFairyFuite
Voile PastelAnticipationPV
65Atq
100Déf
70SpA
80SpD
80Vit
105BST
500
RU
RattatacNormalFuite
CranAgitationPV
55Atq
81Déf
60SpA
50SpD
70Vit
97BST
413
RU
Rattatac-AlolaDarkNormalGloutonnerie
AgitationIsograissePV
75Atq
71Déf
70SpA
40SpD
80Vit
77BST
413
RU
RegiceIceCorps SainCorps GelPV
80Atq
50Déf
100SpA
100SpD
200Vit
50BST
580
RU
RegidragoDragonDent de DragonPV
200Atq
100Déf
50SpA
100SpD
50Vit
80BST
580
RU
RegigigasNormalDébut CalmePV
110Atq
160Déf
110SpA
80SpD
110Vit
100BST
670
RU
RegirockRockCorps SainFermetéPV
80Atq
100Déf
200SpA
50SpD
100Vit
50BST
580
RU
RegisteelSteelCorps SainLight MetalPV
80Atq
75Déf
150SpA
75SpD
150Vit
50BST
580
RU
RelicanthWaterRockGlissade
Tête de RocFermetéPV
100Atq
90Déf
130SpA
45SpD
65Vit
55BST
485
RU
SymbiosPsychicEnvelocape
Garde MagikRégé-ForcePV
110Atq
65Déf
75SpA
125SpD
85Vit
30BST
490
RU
VrombotorSteelPoisonEnvelocapeFiltrePV
80Atq
119Déf
90SpA
54SpD
67Vit
90BST
500
RU
RhinastocGroundRockParatonnerre
Solide RocTémérairePV
115Atq
140Déf
130SpA
55SpD
55Vit
40BST
535
RU
RubombelleBugFairyCherche Miel
Écran PoudreGluco-VoilePV
60Atq
55Déf
60SpA
95SpD
70Vit
124BST
464
RU
RoseradeGrassPoisonMédic Nature
Point PoisonTechnicienPV
60Atq
70Déf
65SpA
125SpD
105Vit
90BST
515
RU
MotismaElectricGhostLévitationPV
50Atq
50Déf
77SpA
95SpD
77Vit
91BST
440
RU
Motisma-HéliceElectricFlyingLévitationPV
50Atq
65Déf
107SpA
105SpD
107Vit
86BST
520
RU
Motisma-FroidElectricIceLévitationPV
50Atq
65Déf
107SpA
105SpD
107Vit
86BST
520
RU
Motisma-ChaleurElectricFireLévitationPV
50Atq
65Déf
107SpA
105SpD
107Vit
86BST
520
RU
Motisma-TonteElectricGrassLévitationPV
50Atq
65Déf
107SpA
105SpD
107Vit
86BST
520
RU
TutétékriGroundGhostÂme VagabondePV
58Atq
95Déf
145SpA
50SpD
105Vit
30BST
483
RU
TénéfixDarkGhostRegard Vif
FreinFarceurPV
50Atq
75Déf
75SpA
65SpD
65Vit
50BST
380
RU
MalamandrePoisonFireCorrosionBenêtPV
68Atq
64Déf
60SpA
111SpD
60Vit
117BST
480
RU
ClamiralWaterTorrentCoque ArmurePV
95Atq
100Déf
85SpA
108SpD
70Vit
70BST
528
RU
DunacondaGroundExpul'Sable
MueVoile SablePV
72Atq
107Déf
125SpA
65SpD
70Vit
71BST
510
RU
SablaireauGroundVoile SableBaigne SablePV
75Atq
100Déf
110SpA
45SpD
55Vit
65BST
450
RU
Sablaireau-AlolaIceSteelRideau NeigeChasse-NeigePV
75Atq
100Déf
120SpA
25SpD
65Vit
65BST
450
RU
Pelage-SabléElectricGroundPaléosynthèsePV
85Atq
81Déf
97SpA
121SpD
85Vit
101BST
570
RU
KaracléeFightingFermeté
AttentionBrise MoulePV
75Atq
125Déf
75SpA
30SpD
75Vit
85BST
465
RU
HaydaimNormalGrassChlorophylle
HerbivoreSérénitéPV
80Atq
100Déf
70SpA
60SpD
70Vit
95BST
475
RU
JungkoGrassEngraisDélestagePV
70Atq
85Déf
65SpA
105SpD
85Vit
120BST
530
RU
Jungko-MégaGrassDragonParatonnerrePV
70Atq
110Déf
75SpA
145SpD
85Vit
145BST
630
RU
CizayoxBugSteelEssaim
TechnicienLight MetalPV
70Atq
130Déf
100SpA
55SpD
80Vit
65BST
500
RU
BrutapodeBugPoisonPoint Poison
EssaimTurboPV
60Atq
100Déf
89SpA
55SpD
69Vit
112BST
485
RU
ScovilainGrassFireChlorophylle
InsomniaLunatiquePV
65Atq
108Déf
65SpA
108SpD
65Vit
75BST
486
RU
BaggaïdDarkFightingMue
ImpudenceIntimidationPV
65Atq
90Déf
115SpA
45SpD
115Vit
58BST
488
RU
Hurle-QueueFairyPsychicPaléosynthèsePV
115Atq
65Déf
99SpA
65SpD
115Vit
111BST
570
RU
PoissoroyWaterGlissade
Ignifu-VoileParatonnerrePV
80Atq
92Déf
65SpA
65SpD
80Vit
68BST
450
RU
CrapustuleWaterGroundGlissade
ToxitoucheAbsorb EauPV
105Atq
95Déf
75SpA
85SpD
75Vit
74BST
509
RU
SéviperPoisonMueInfiltrationPV
73Atq
100Déf
60SpA
100SpD
60Vit
65BST
458
RU
SharpedoWaterDarkPeau DureTurboPV
70Atq
120Déf
40SpA
95SpD
40Vit
95BST
460
RU
Sharpedo-MégaWaterDarkPrognathePV
70Atq
140Déf
70SpA
110SpD
65Vit
105BST
560
RU
ShayminGrassMédic NaturePV
100Atq
100Déf
100SpA
100SpD
100Vit
100BST
600
RU
TengaliceGrassDarkChlorophylle
AéroportéPickpocketPV
90Atq
100Déf
60SpA
90SpD
60Vit
80BST
480
RU
LampignonGrassFairyLumiattirance
Pose SporeCuvettePV
60Atq
45Déf
80SpA
90SpD
100Vit
30BST
405
RU
CaratrocBugRockFermeté
GloutonnerieContestationPV
20Atq
10Déf
230SpA
10SpD
230Vit
5BST
505
RU
CryptéroPsychicFlyingPeau Miracle
Garde MagikLentiteintéePV
72Atq
58Déf
80SpA
103SpD
80Vit
97BST
490
RU
SilvalliéNormalSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-InsecteBugSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-TénèbresDarkSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-DragonDragonSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-ÉlectrikElectricSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-FéeFairySystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-CombatFightingSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-FeuFireSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-VolFlyingSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-SpectreGhostSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-PlanteGrassSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-SolGroundSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-GlaceIceSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-PoisonPoisonSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-PsyPsychicSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-RocheRockSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-AcierSteelSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
Silvallié-EauWaterSystème AlphaPV
95Atq
95Déf
95SpA
95SpD
95Vit
95BST
570
RU
FlotoutanWaterGloutonnerieTorrentPV
75Atq
98Déf
63SpA
98SpD
63Vit
101BST
498
RU
FeuiloutanGrassGloutonnerieEngraisPV
75Atq
98Déf
63SpA
98SpD
63Vit
101BST
498
RU
FlamoutanFireGloutonnerieBrasierPV
75Atq
98Déf
63SpA
98SpD
63Vit
101BST
498
RU
PalartichoFightingImpassibleQuerelleurPV
62Atq
135Déf
95SpA
68SpD
82Vit
65BST
507
RU
MoufflairPoisonDarkPuanteur
Boom FinalRegard VifPV
103Atq
93Déf
67SpA
71SpD
61Vit
84BST
479
RU
MonaflèmitNormalAbsentéismePV
150Atq
160Déf
100SpA
95SpD
65Vit
100BST
670
RU
Rampe-AilesBugFightingPaléosynthèsePV
85Atq
135Déf
79SpA
85SpD
105Vit
81BST
570
RU
Flagadoss-GalarPoisonPsychicTir Vif
Tempo PersoRégé-ForcePV
95Atq
100Déf
95SpA
100SpD
70Vit
30BST
490
RU
Flagadoss-MégaWaterPsychicCoque ArmurePV
95Atq
75Déf
180SpA
130SpD
80Vit
30BST
590
RU
RoigadaWaterPsychicBenêt
Tempo PersoRégé-ForcePV
95Atq
75Déf
80SpA
100SpD
110Vit
30BST
490
RU
CupcanailleFairyGluco-VoileDélestagePV
82Atq
80Déf
86SpA
85SpD
75Vit
72BST
480
RU
QueuloriorNormalTempo Perso
TechnicienLunatiquePV
55Atq
20Déf
35SpA
20SpD
45Vit
75BST
250
RU
RonflexNormalVaccin
IsograisseGloutonneriePV
160Atq
110Déf
65SpA
65SpD
110Vit
30BST
540
RU
SolarocRockPsychicLévitationPV
90Atq
95Déf
85SpA
55SpD
65Vit
70BST
460
RU
FilentrappeBugInsomniaFilaturePV
60Atq
79Déf
92SpA
52SpD
86Vit
35BST
404
RU
SpindaNormalTempo Perso
Pieds ConfusContestationPV
60Atq
60Déf
60SpA
60SpD
60Vit
60BST
360
RU
SpiritombGhostDarkPressionInfiltrationPV
50Atq
92Déf
108SpA
92SpD
108Vit
35BST
485
RU
TapatoèsNormalFlyingIntimidation
AgitationCranPV
82Atq
96Déf
51SpA
45SpD
51Vit
92BST
417
RU
Tapatoès-BleuNormalFlyingIntimidation
AgitationCranPV
82Atq
96Déf
51SpA
45SpD
51Vit
92BST
417
RU
Tapatoès-BlancNormalFlyingIntimidation
AgitationSans LimitePV
82Atq
96Déf
51SpA
45SpD
51Vit
92BST
417
RU
Tapatoès-JauneNormalFlyingIntimidation
AgitationSans LimitePV
82Atq
96Déf
51SpA
45SpD
51Vit
92BST
417
RU
Ama-AmaRockSteelBoost ChimèrePV
61Atq
131Déf
211SpA
53SpD
101Vit
13BST
570
RU
ÉtouraptorNormalFlyingIntimidationTémérairePV
85Atq
120Déf
70SpA
50SpD
60Vit
100BST
485
RU
StarossWaterPsychicLumiattirance
Médic NatureAnalystePV
60Atq
75Déf
85SpA
100SpD
85Vit
115BST
520
RU
SteelixSteelGroundTête de Roc
FermetéSans LimitePV
75Atq
85Déf
200SpA
55SpD
65Vit
30BST
510
RU
Steelix-MégaSteelGroundForce SablePV
75Atq
125Déf
230SpA
55SpD
95Vit
30BST
610
RU
DolmanRockCercle d'ÉnergiePV
100Atq
125Déf
135SpA
20SpD
20Vit
70BST
470
RU
MastouffeNormalIntimidation
Baigne SableQuerelleurPV
85Atq
110Déf
90SpA
45SpD
90Vit
80BST
500
RU
LimondeGroundElectricStatik
ÉchauffementVoile SablePV
109Atq
66Déf
84SpA
81SpD
99Vit
32BST
471
RU
Limonde-GalarGroundSteelMimétismePV
109Atq
81Déf
99SpA
66SpD
84Vit
32BST
471
RU
SimularbreRockFermeté
Tête de RocPhobiquePV
70Atq
100Déf
115SpA
30SpD
65Vit
30BST
410
RU
SuicuneWaterPressionAttentionPV
100Atq
75Déf
115SpA
90SpD
115Vit
85BST
580
RU
HéliatroncGrassChlorophylle
Force SoleilMatinalPV
75Atq
75Déf
55SpA
105SpD
85Vit
30BST
425
RU
AvaltoutPoisonSuintement
GlueGloutonneriePV
100Atq
73Déf
83SpA
73SpD
83Vit
55BST
467
RU
LaggronWaterGroundTorrentMoiteurPV
100Atq
110Déf
90SpA
85SpD
90Vit
60BST
535
RU
LakmécygneWaterFlyingRegard Vif
Coeur de CoqHydratationPV
75Atq
87Déf
63SpA
87SpD
63Vit
98BST
473
RU
HélédelleNormalFlyingCranQuerelleurPV
60Atq
85Déf
60SpA
75SpD
50Vit
125BST
455
RU
RhinolovePsychicFlyingInconscient
MaladresseSimplePV
67Atq
57Déf
55SpA
77SpD
55Vit
114BST
425
RU
NymphaliFairyJoli SourirePeau FéériquePV
95Atq
65Déf
65SpA
110SpD
130Vit
60BST
525
RU
FlambusardFireFlyingCorps ArdentAiles BourrasquePV
78Atq
81Déf
71SpA
74SpD
69Vit
126BST
499
RU
BouldeneuGrassChlorophylle
Feuille GardeRégé-ForcePV
100Atq
100Déf
125SpA
110SpD
50Vit
50BST
535
RU
TokotoroGrassFairyCréa-HerbeTélépathePV
70Atq
130Déf
115SpA
85SpD
95Vit
75BST
570
RU
NigirigonDragonWaterCommandantLavaboPV
68Atq
50Déf
60SpA
120SpD
95Vit
82BST
475
RU
TaurosNormalIntimidation
ColériqueSans LimitePV
75Atq
100Déf
95SpA
40SpD
70Vit
110BST
490
RU
Tauros-Paldea-EauFightingWaterIntimidation
ColériqueRuminantPV
75Atq
110Déf
105SpA
30SpD
70Vit
100BST
490
RU
Tauros-Paldea-FeuFightingFireIntimidation
ColériqueRuminantPV
75Atq
110Déf
105SpA
30SpD
70Vit
100BST
490
RU
Tauros-Paldea-CombatFightingIntimidation
ColériqueRuminantPV
75Atq
110Déf
105SpA
30SpD
70Vit
100BST
490
RU
TentacruelWaterPoisonCorps Sain
SuintementCuvettePV
80Atq
70Déf
65SpA
80SpD
120Vit
100BST
515
RU
RoublenardDarkFuite
DélestageFilaturePV
70Atq
58Déf
58SpA
87SpD
92Vit
90BST
455
RU
JudokrakFightingCran
AttentionBrise MoulePV
120Atq
100Déf
85SpA
30SpD
85Vit
45BST
465
RU
FulgurisElectricFlyingFarceurAcharnéPV
79Atq
115Déf
70SpA
125SpD
80Vit
111BST
580
RU
ForgelinaFairySteelBrise Moule
Tempo PersoPickpocketPV
85Atq
75Déf
77SpA
70SpD
105Vit
94BST
506
RU
TerracruelGroundGrassForce FongiquePV
80Atq
70Déf
65SpA
80SpD
120Vit
100BST
515
RU
TogedemaruElectricSteelÉpine de Fer
ParatonnerreFermetéPV
65Atq
98Déf
63SpA
40SpD
73Vit
96BST
435
RU
TogekissFairyFlyingAgitation
SérénitéChanceuxPV
85Atq
50Déf
95SpA
120SpD
115Vit
80BST
545
RU
BoréasFlyingFarceurAcharnéPV
79Atq
115Déf
70SpA
125SpD
80Vit
111BST
580
RU
TorterraGrassGroundEngraisCoque ArmurePV
95Atq
109Déf
105SpA
75SpD
85Vit
56BST
525
RU
BazoucanNormalFlyingRegard Vif
Multi-CoupsSans LimitePV
80Atq
120Déf
75SpA
75SpD
75Vit
60BST
485
RU
CoatoxPoisonFightingAnticipation
Peau SècheToxitouchePV
83Atq
106Déf
65SpA
86SpD
65Vit
85BST
490
RU
SalarsenElectricPoisonPunk Rock
PlusTechnicienPV
75Atq
98Déf
70SpA
114SpD
70Vit
75BST
502
RU
Salarsen-GraveElectricPoisonPunk Rock
MinusTechnicienPV
75Atq
98Déf
70SpA
114SpD
70Vit
75BST
502
RU
DesséliandeGhostGrassMédic Nature
FouilleRécoltePV
85Atq
110Déf
76SpA
65SpD
82Vit
56BST
474
RU
TropiusGrassFlyingChlorophylle
Force SoleilRécoltePV
99Atq
68Déf
83SpA
72SpD
87Vit
51BST
460
RU
SucreineGrassFeuille Garde
Prestance RoyaleGluco-VoilePV
72Atq
120Déf
98SpA
50SpD
98Vit
72BST
510
RU
BoumataFireDragonCoque ArmurePV
60Atq
78Déf
135SpA
91SpD
85Vit
36BST
485
RU
TyphlosionFireBrasierTorchePV
78Atq
84Déf
78SpA
109SpD
85Vit
100BST
534
RU
Typhlosion-HisuiFireGhostBrasierFouillePV
73Atq
84Déf
78SpA
119SpD
85Vit
95BST
534
RU
RexilliusRockDragonPrognatheTête de RocPV
82Atq
121Déf
119SpA
69SpD
59Vit
71BST
521
RU
NoctaliDarkSynchroAttentionPV
95Atq
65Déf
110SpA
60SpD
130Vit
65BST
525
RU
DéflaisanNormalFlyingCoeur de Coq
ChanceuxRivalitéPV
80Atq
115Déf
80SpA
65SpD
55Vit
93BST
488
RU
ZarbiPsychicLévitationPV
48Atq
72Déf
48SpA
72SpD
48Vit
48BST
336
RU
CréhelfPsychicLévitationPV
75Atq
75Déf
130SpA
75SpD
130Vit
95BST
580
RU
SorbouboulIceCorps Gel
Alerte NeigeArmurouilléePV
71Atq
95Déf
85SpA
110SpD
95Vit
79BST
535
RU
AqualiWaterAbsorb EauHydratationPV
130Atq
65Déf
60SpA
110SpD
95Vit
65BST
525
RU
DélestinWaterPsychicBrise MouleIncisifPV
90Atq
102Déf
73SpA
78SpD
65Vit
70BST
478
RU
AéromiteBugPoisonÉcran Poudre
LentiteintéePeau MiraclePV
70Atq
65Déf
60SpA
90SpD
75Vit
90BST
450
RU
FlorizarreGrassPoisonEngraisChlorophyllePV
80Atq
82Déf
83SpA
100SpD
100Vit
80BST
525
RU
ApireineBugFlyingPressionTensionPV
70Atq
80Déf
102SpA
80SpD
102Vit
40BST
474
RU
EmpiflorGrassPoisonChlorophylleGloutonneriePV
80Atq
105Déf
65SpA
100SpD
70Vit
70BST
490
RU
LucanonBugElectricLévitationPV
77Atq
70Déf
90SpA
145SpD
75Vit
43BST
500
RU
RafflesiaGrassPoisonChlorophyllePose SporePV
75Atq
80Déf
85SpA
110SpD
90Vit
50BST
490
RU
ViridiumGrassFightingCoeur NoblePV
91Atq
90Déf
72SpA
90SpD
129Vit
108BST
580
RU
PrismillonBugFlyingÉcran Poudre
Oeil ComposéGarde AmiePV
80Atq
52Déf
50SpA
90SpD
50Vit
89BST
411
RU
Prismillon-FantaisieBugFlyingÉcran Poudre
Oeil ComposéGarde AmiePV
80Atq
52Déf
50SpA
90SpD
50Vit
89BST
411
RU
Prismillon-PokéballBugFlyingÉcran Poudre
Oeil ComposéGarde AmiePV
80Atq
52Déf
50SpA
90SpD
50Vit
89BST
411
RU
MucioleBugLumiattirance
EssaimFarceurPV
65Atq
73Déf
75SpA
47SpD
85Vit
85BST
430
RU
VolcanionFireWaterAbsorb EauPV
80Atq
110Déf
120SpA
130SpD
90Vit
70BST
600
RU
WailordWaterIgnifu-Voile
BenêtPressionPV
170Atq
90Déf
45SpA
90SpD
45Vit
60BST
500
RU
KaimorseIceWaterIsograisse
Corps GelBenêtPV
110Atq
80Déf
90SpA
95SpD
90Vit
65BST
530
RU
MiradarNormalLumiattirance
Regard VifAnalystePV
60Atq
85Déf
69SpA
60SpD
69Vit
77BST
420
RU
SmogogoPoisonLévitation
Gaz InhibiteurPuanteurPV
65Atq
90Déf
120SpA
85SpD
70Vit
60BST
490
RU
Smogogo-GalarPoisonFairyLévitation
Gaz InhibiteurCréa-BrumePV
65Atq
90Déf
120SpA
85SpD
70Vit
60BST
490
RU
FarfaduvetGrassFairyFarceur
InfiltrationChlorophyllePV
60Atq
67Déf
85SpA
77SpD
75Vit
116BST
480
RU
BarbichaWaterGroundBenêt
AnticipationHydratationPV
110Atq
78Déf
73SpA
76SpD
71Vit
60BST
468
RU
GrodoudouNormalFairyJoli Sourire
BattantFouillePV
140Atq
70Déf
45SpA
85SpD
50Vit
45BST
435
RU
FroussardineWaterBancPV
45Atq
20Déf
20SpA
25SpD
25Vit
40BST
175
RU
QulbutokéPsychicMarque OmbreTélépathePV
190Atq
33Déf
58SpA
33SpD
58Vit
33BST
405
RU
ChongjianDarkGrassBois du FléauPV
85Atq
85Déf
100SpA
95SpD
135Vit
70BST
570
RU
CheniselleBugGrassAnticipationEnvelocapePV
60Atq
59Déf
85SpA
79SpD
105Vit
36BST
424
RU
Cheniselle-SableBugGroundAnticipationEnvelocapePV
60Atq
79Déf
105SpA
59SpD
85Vit
36BST
424
RU
Cheniselle-DéchetBugSteelAnticipationEnvelocapePV
60Atq
69Déf
95SpA
69SpD
95Vit
36BST
424
RU
TriopikeauWaterPoisseux
PhobiqueVoile SablePV
35Atq
100Déf
50SpA
50SpD
70Vit
120BST
425
RU
CerbyllinNormalPsychicIntimidation
FouilleHerbivorePV
103Atq
105Déf
72SpA
105SpD
75Vit
65BST
525
RU
XatuPsychicFlyingSynchro
MatinalMiroir MagikPV
65Atq
75Déf
70SpA
95SpD
70Vit
95BST
470
RU
YanmégaBugFlyingTurbo
LentiteintéeFouillePV
86Atq
76Déf
86SpA
116SpD
56Vit
95BST
515
RU
MangriffNormalVaccinRage PoisonPV
73Atq
115Déf
60SpA
60SpD
60Vit
90BST
458
RU
ZarudeDarkGrassFeuille GardePV
105Atq
120Déf
105SpA
70SpD
95Vit
105BST
600
RU
Zarude-PapaDarkGrassFeuille GardePV
105Atq
120Déf
105SpA
70SpD
95Vit
105BST
600
RU
ZéblitzElectricParatonnerre
MotoriséHerbivorePV
75Atq
100Déf
63SpA
80SpD
63Vit
116BST
497
RU
ZeraoraElectricAbsorb VoltPV
88Atq
112Déf
75SpA
102SpD
80Vit
143BST
600
RU
ZoroarkDarkIllusionPV
60Atq
105Déf
60SpA
120SpD
60Vit
105BST
510
RU
Zygarde-10%DragonGroundAura Inversée(Rassemblement)PV
54Atq
100Déf
71SpA
61SpD
85Vit
115BST
486
NFEs non présents dans un tier supérieur
NFE
CapumainNormalFuite
RamassageMulti-CoupsPV
55Atq
70Déf
55SpA
40SpD
55Vit
85BST
360
NFE
CryodoDragonIceThermodynamiqueCorps GelPV
90Atq
95Déf
66SpA
45SpD
65Vit
62BST
423
NFE
MacroniumGrassEngraisFeuille GardePV
60Atq
62Déf
80SpA
63SpD
80Vit
60BST
405
NFE
GéolitheRockFermeté
ArmurouilléeForce SablePV
70Atq
105Déf
105SpA
50SpD
40Vit
20BST
390
NFE
RoussilFireBrasierMagicienPV
59Atq
59Déf
58SpA
90SpD
70Vit
73BST
409
NFE
OtarletteWaterTorrentHydrata-SonPV
60Atq
69Déf
69SpA
91SpD
81Vit
50BST
420
NFE
WagomineRockFireTurbine
Corps ArdentTorchePV
80Atq
60Déf
90SpA
60SpD
70Vit
50BST
410
NFE
BlindalysBugMuePV
50Atq
35Déf
55SpA
25SpD
25Vit
15BST
205
NFE
ChrysapileBugElectricBatteriePV
57Atq
82Déf
95SpA
55SpD
75Vit
36BST
400
NFE
ReptincelFireBrasierForce SoleilPV
58Atq
64Déf
58SpA
80SpD
65Vit
80BST
405
NFE
MéloféeFairyJoli Sourire
Garde MagikGarde AmiePV
70Atq
45Déf
48SpA
60SpD
65Vit
35BST
323
NFE
GalifeuFireFightingBrasierTurboPV
60Atq
85Déf
60SpA
85SpD
60Vit
55BST
405
NFE
BleuseilleFlyingRegard Vif
TensionCoeur de CoqPV
68Atq
67Déf
55SpA
43SpD
55Vit
77BST
365
NFE
CosmovumPsychicFermetéPV
43Atq
29Déf
131SpA
29SpD
131Vit
37BST
400
NFE
CrocogrilFireBrasierInconscientPV
81Atq
55Déf
78SpA
90SpD
58Vit
49BST
411
NFE
CrocrodilWaterTorrentSans LimitePV
65Atq
80Déf
80SpA
59SpD
63Vit
58BST
405
NFE
BombydouBugFairyCherche Miel
Écran PoudreGluco-VoilePV
40Atq
45Déf
40SpA
55SpD
40Vit
84BST
304
NFE
EfflècheGrassFlyingEngraisLongue PortéePV
78Atq
75Déf
75SpA
70SpD
70Vit
52BST
420
NFE
MateloutreWaterTorrentCoque ArmurePV
75Atq
75Déf
60SpA
83SpD
60Vit
60BST
413
NFE
TaupiqueurGroundVoile Sable
Piège SableForce SablePV
10Atq
55Déf
25SpA
35SpD
45Vit
95BST
265
NFE
OlivadoGrassNormalMatinalRécoltePV
52Atq
53Déf
60SpA
78SpD
78Vit
33BST
354
NFE
ColéodômeBugPsychicEssaim
Oeil ComposéTélépathePV
50Atq
35Déf
80SpA
50SpD
90Vit
30BST
335
NFE
DimoclèsSteelGhostAnnule GardePV
59Atq
110Déf
150SpA
45SpD
49Vit
35BST
448
NFE
DracoDragonMueÉcaille SpécialePV
61Atq
84Déf
65SpA
70SpD
70Vit
70BST
420
NFE
DispareptilDragonGhostCorps Sain
InfiltrationCorps MauditPV
68Atq
80Déf
50SpA
60SpD
50Vit
102BST
410
NFE
ArrozardWaterTorrentSniperPV
65Atq
60Déf
55SpA
95SpD
55Vit
90BST
420
NFE
InsolourdoNormalSérénité
FuitePhobiquePV
100Atq
70Déf
70SpA
65SpD
65Vit
45BST
415
NFE
MéiosPsychicEnvelocape
Garde MagikRégé-ForcePV
65Atq
40Déf
50SpA
125SpD
60Vit
30BST
370
NFE
TéraclopeGhostPressionFouillePV
40Atq
70Déf
130SpA
60SpD
130Vit
25BST
455
NFE
LampéroieElectricLévitationPV
65Atq
85Déf
70SpA
75SpD
70Vit
40BST
405
NFE
ÉlektekElectricStatikEsprit VitalPV
65Atq
83Déf
57SpA
95SpD
85Vit
105BST
490
NFE
LainergieElectricStatikPlusPV
70Atq
55Déf
55SpA
80SpD
60Vit
45BST
365
NFE
BraisillonFireFlyingCorps ArdentAiles BourrasquePV
62Atq
73Déf
55SpA
56SpD
52Vit
84BST
382
NFE
FlotillonPsychicAnticipation
FouilleTurboPV
30Atq
35Déf
30SpA
55SpD
30Vit
75BST
255
NFE
FloetteFairyFlora-VoileSymbiosePV
54Atq
45Déf
47SpA
75SpD
98Vit
52BST
371
NFE
MatourgeonGrassEngraisProtéenPV
61Atq
80Déf
63SpA
60SpD
63Vit
83BST
410
NFE
IncisacheDragonRivalité
Brise MouleTensionPV
66Atq
117Déf
70SpA
40SpD
50Vit
67BST
410
NFE
CroâporalWaterTorrentProtéenPV
54Atq
63Déf
52SpA
83SpD
56Vit
97BST
405
NFE
CarmacheDragonGroundVoile SablePeau DurePV
68Atq
90Déf
65SpA
50SpD
55Vit
82BST
410
NFE
GirafarigNormalPsychicAttention
MatinalHerbivorePV
70Atq
80Déf
65SpA
90SpD
65Vit
85BST
455
NFE
ScorplaneGroundFlyingHyper Cutter
Voile SableVaccinPV
65Atq
75Déf
105SpA
35SpD
65Vit
85BST
430
NFE
OrtideGrassPoisonChlorophyllePuanteurPV
60Atq
65Déf
70SpA
85SpD
75Vit
40BST
395
NFE
NosferaltoPoisonFlyingAttentionInfiltrationPV
75Atq
80Déf
70SpA
65SpD
75Vit
90BST
455
NFE
MesmérellaPsychicFouille
BattantMarque OmbrePV
60Atq
45Déf
70SpA
75SpD
85Vit
55BST
390
NFE
GravalanchRockGroundTête de Roc
FermetéVoile SablePV
55Atq
95Déf
115SpA
45SpD
45Vit
35BST
390
NFE
Gravalanch-AlolaRockElectricMagnépiège
FermetéPeau ÉlectriquePV
55Atq
95Déf
115SpA
45SpD
45Vit
35BST
390
NFE
BoskaraGrassEngraisCoque ArmurePV
75Atq
89Déf
85SpA
55SpD
65Vit
36BST
405
NFE
MasskoGrassEngraisDélestagePV
50Atq
65Déf
45SpA
85SpD
65Vit
95BST
405
NFE
OuvrifierFightingCran
Sans LimitePoing de FerPV
85Atq
105Déf
85SpA
40SpD
50Vit
40BST
405
NFE
ÉcaïdDragonFightingPare-Balles
Anti-BruitEnvelocapePV
55Atq
75Déf
90SpA
65SpD
70Vit
65BST
420
NFE
ChapotusPsychicCoeur Soin
AnticipationMiroir MagikPV
57Atq
40Déf
65SpA
86SpD
73Vit
49BST
370
NFE
SpectrumGhostPoisonLévitationPV
45Atq
50Déf
45SpA
115SpD
55Vit
95BST
405
NFE
PonchienNormalIntimidation
Baigne SableQuerelleurPV
65Atq
80Déf
65SpA
35SpD
65Vit
60BST
370
NFE
HerbizarreGrassPoisonEngraisChlorophyllePV
60Atq
62Déf
63SpA
80SpD
80Vit
60BST
405
NFE
RondoudouNormalFairyJoli Sourire
BattantGarde AmiePV
115Atq
45Déf
20SpA
45SpD
25Vit
20BST
270
NFE
KadabraPsychicSynchro
AttentionGarde MagikPV
40Atq
35Déf
30SpA
120SpD
70Vit
105BST
400
NFE
CoconfortBugPoisonMuePV
45Atq
25Déf
50SpA
25SpD
25Vit
35BST
205
NFE
KirliaPsychicFairySynchro
CalqueTélépathePV
38Atq
35Déf
35SpA
65SpD
55Vit
50BST
278
NFE
ClicSteelPlus
MinusCorps SainPV
60Atq
80Déf
95SpA
70SpD
85Vit
50BST
440
NFE
EscrocoGroundDarkIntimidation
ImpudenceColériquePV
60Atq
82Déf
45SpA
45SpD
45Vit
74BST
351
NFE
WushoursFightingAttentionPV
60Atq
90Déf
60SpA
53SpD
50Vit
72BST
385
NFE
GalegonSteelRockFermeté
Tête de RocHeavy MetalPV
60Atq
90Déf
140SpA
50SpD
50Vit
40BST
430
NFE
MélancoluxGhostFireTorche
Corps ArdentInfiltrationPV
60Atq
40Déf
60SpA
95SpD
60Vit
55BST
370
NFE
Linéon-GalarDarkNormalRamassage
GloutonneriePied VélocePV
78Atq
70Déf
61SpA
50SpD
61Vit
100BST
420
NFE
LombreWaterGrassGlissade
CuvetteTempo PersoPV
60Atq
50Déf
50SpA
60SpD
70Vit
50BST
340
NFE
RamboumNormalAnti-BruitQuerelleurPV
84Atq
71Déf
43SpA
71SpD
43Vit
48BST
360
NFE
LuxioElectricRivalité
IntimidationCranPV
60Atq
85Déf
49SpA
60SpD
49Vit
60BST
363
NFE
MachopeurFightingCran
Annule GardeImpassiblePV
80Atq
100Déf
70SpA
50SpD
60Vit
45BST
405
NFE
MagmarFireCorps ArdentEsprit VitalPV
65Atq
95Déf
57SpA
100SpD
85Vit
93BST
495
NFE
MagnétonElectricSteelMagnépiège
FermetéAnalystePV
50Atq
60Déf
95SpA
120SpD
70Vit
70BST
465
NFE
MarillWaterFairyIsograisse
ColoforceHerbivorePV
70Atq
20Déf
50SpA
20SpD
50Vit
40BST
250
NFE
FlobioWaterGroundTorrentMoiteurPV
70Atq
85Déf
70SpA
60SpD
70Vit
50BST
405
NFE
MéditikkaFightingPsychicForce PureTélépathePV
30Atq
40Déf
55SpA
40SpD
55Vit
60BST
280
NFE
MétangSteelPsychicCorps SainLight MetalPV
60Atq
75Déf
100SpA
55SpD
80Vit
50BST
420
NFE
ChrysacierBugMuePV
50Atq
20Déf
55SpA
25SpD
25Vit
30BST
205
NFE
FeuforêveGhostLévitationPV
60Atq
60Déf
60SpA
85SpD
85Vit
85BST
435
NFE
ChimpenfeuFireFightingBrasierPoing de FerPV
64Atq
78Déf
52SpA
78SpD
52Vit
81BST
405
NFE
FourbelinDarkFairyFarceur
FouillePickpocketPV
65Atq
60Déf
45SpA
75SpD
55Vit
70BST
370
NFE
M. Mime-GalarIcePsychicEsprit Vital
Brise-BarrièreCorps GelPV
50Atq
65Déf
65SpA
90SpD
90Vit
100BST
460
NFE
CornèbreDarkFlyingInsomnia
ChanceuxFarceurPV
60Atq
85Déf
42SpA
85SpD
42Vit
91BST
405
NFE
AmasselRockSel Purificateur
FermetéCorps SainPV
60Atq
60Déf
100SpA
35SpD
65Vit
35BST
355
NFE
NidorinaPoisonPoint Poison
RivalitéAgitationPV
70Atq
62Déf
67SpA
55SpD
55Vit
56BST
365
NFE
NidorinoPoisonPoint Poison
RivalitéAgitationPV
61Atq
72Déf
57SpA
55SpD
55Vit
65BST
365
NFE
PifeuilGrassDarkChlorophylle
MatinalPickpocketPV
70Atq
70Déf
40SpA
60SpD
40Vit
60BST
340
NFE
BatracnéWaterGroundGlissade
HydratationAbsorb EauPV
75Atq
65Déf
55SpA
65SpD
55Vit
69BST
384
NFE
PohmotteElectricFightingAbsorb Volt
Médic NaturePoing de FerPV
60Atq
75Déf
40SpA
50SpD
40Vit
85BST
350
NFE
RoucoupsNormalFlyingRegard Vif
Pieds ConfusCoeur de CoqPV
63Atq
60Déf
55SpA
50SpD
50Vit
71BST
349
NFE
GrotichonFireFightingBrasierIsograissePV
90Atq
93Déf
55SpA
70SpD
55Vit
55BST
418
NFE
CochignonIceGroundBenêt
Rideau NeigeIsograissePV
100Atq
100Déf
80SpA
60SpD
60Vit
50BST
450
NFE
VéminiPoisonBoost ChimèrePV
67Atq
73Déf
67SpA
73SpD
67Vit
73BST
420
NFE
TêtarteWaterAbsorb Eau
MoiteurGlissadePV
65Atq
65Déf
65SpA
50SpD
50Vit
90BST
385
NFE
PorygonNormalCalque
TéléchargeAnalystePV
65Atq
60Déf
70SpA
85SpD
75Vit
40BST
395
NFE
Porygon2NormalCalque
TéléchargeAnalystePV
85Atq
80Déf
90SpA
105SpD
95Vit
60BST
515
NFE
ColossingeFightingEsprit Vital
ColériqueAcharnéPV
65Atq
105Déf
60SpA
60SpD
70Vit
95BST
455
NFE
PrinploufWaterTorrentBattantPV
64Atq
66Déf
68SpA
81SpD
76Vit
50BST
405
NFE
YmphectRockGroundMuePV
70Atq
84Déf
70SpA
65SpD
70Vit
51BST
410
NFE
CanarbelloWaterTorrentImpudencePV
70Atq
85Déf
65SpA
65SpD
60Vit
65BST
410
NFE
FeurissonFireBrasierTorchePV
58Atq
64Déf
58SpA
80SpD
65Vit
80BST
405
NFE
BoguérisseGrassEngraisPare-BallesPV
61Atq
78Déf
95SpA
56SpD
58Vit
57BST
405
NFE
Qwilfish-HisuiDarkPoisonPoint Poison
GlissadeIntimidationPV
65Atq
95Déf
85SpA
55SpD
55Vit
85BST
440
NFE
LapyroFireBrasierLibéroPV
65Atq
86Déf
60SpA
55SpD
60Vit
94BST
420
NFE
RhinoférosGroundRockParatonnerre
Tête de RocTémérairePV
105Atq
130Déf
120SpA
45SpD
45Vit
40BST
485
NFE
RoséliaGrassPoisonMédic Nature
Point PoisonFeuille GardePV
50Atq
60Déf
45SpA
100SpD
80Vit
65BST
400
NFE
FuraiglonNormalFlyingRegard Vif
Sans LimiteAgitationPV
70Atq
83Déf
50SpA
37SpD
50Vit
60BST
350
NFE
BaggiguaneDarkFightingMue
ImpudenceIntimidationPV
50Atq
75Déf
70SpA
35SpD
70Vit
48BST
348
NFE
InsécateurBugFlyingEssaim
TechnicienImpassiblePV
70Atq
110Déf
80SpA
55SpD
80Vit
105BST
500
NFE
HypocéanWaterPoint Poison
SniperMoiteurPV
55Atq
65Déf
95SpA
95SpD
45Vit
85BST
440
NFE
PhogleurIceWaterIsograisse
Corps GelBenêtPV
90Atq
60Déf
70SpA
75SpD
70Vit
45BST
410
NFE
LianajaGrassEngraisContestationPV
60Atq
60Déf
75SpA
60SpD
75Vit
83BST
413
NFE
DrackhausDragonTête de RocEnvelocapePV
65Atq
95Déf
100SpA
60SpD
50Vit
50BST
420
NFE
ArmulysBugMuePV
50Atq
35Déf
55SpA
25SpD
25Vit
15BST
205
NFE
FloravolGrassFlyingChlorophylle
Feuille GardeInfiltrationPV
55Atq
45Déf
50SpA
45SpD
65Vit
80BST
340
NFE
ColimucusDragonHerbivore
HydratationPoisseuxPV
68Atq
75Déf
53SpA
83SpD
113Vit
60BST
452
NFE
Colimucus-HisuiSteelDragonHerbivore
Coque ArmurePoisseuxPV
58Atq
75Déf
83SpA
83SpD
113Vit
40BST
452
NFE
FarfuretDarkIceAttention
Regard VifPickpocketPV
55Atq
95Déf
55SpA
35SpD
75Vit
115BST
430
NFE
Farfuret-HisuiFightingPoisonAttention
Regard VifPickpocketPV
55Atq
95Déf
55SpA
35SpD
75Vit
115BST
430
NFE
PérégrainBugMueGarde AmiePV
45Atq
22Déf
60SpA
27SpD
30Vit
29BST
213
NFE
CerfrousseNormalIntimidation
FouilleHerbivorePV
73Atq
95Déf
62SpA
85SpD
65Vit
85BST
465
NFE
ÉtourvolNormalFlyingIntimidationTémérairePV
55Atq
75Déf
50SpA
40SpD
40Vit
80BST
340
NFE
CandineGrassFeuille Garde
BenêtGluco-VoilePV
52Atq
40Déf
48SpA
40SpD
48Vit
62BST
290
NFE
CouverdureBugGrassFeuille Garde
ChlorophylleEnvelocapePV
55Atq
63Déf
90SpA
50SpD
80Vit
42BST
380
NFE
BadabouinGrassEngraisCréa-HerbePV
70Atq
85Déf
70SpA
55SpD
60Vit
80BST
420
NFE
ForgellaFairySteelBrise Moule
Tempo PersoPickpocketPV
65Atq
55Déf
55SpA
45SpD
82Vit
78BST
380
NFE
TogeticFairyFlyingAgitation
SérénitéChanceuxPV
55Atq
40Déf
85SpA
80SpD
105Vit
40BST
405
NFE
MatoufeuFireBrasierIntimidationPV
65Atq
85Déf
50SpA
80SpD
50Vit
90BST
420
NFE
ColombeauNormalFlyingCoeur de Coq
ChanceuxRivalitéPV
62Atq
77Déf
62SpA
50SpD
42Vit
65BST
358
NFE
PiclaironNormalFlyingRegard Vif
Multi-CoupsRamassagePV
55Atq
85Déf
50SpA
40SpD
50Vit
75BST
355
NFE
Type:0NormalArmurbastonPV
95Atq
95Déf
95SpA
95SpD
95Vit
59BST
534
NFE
UrsaringNormalCran
Pied VéloceTensionPV
90Atq
130Déf
75SpA
75SpD
75Vit
55BST
500
NFE
SorboulIceCorps Gel
Rideau NeigeArmurouilléePV
51Atq
65Déf
65SpA
80SpD
75Vit
59BST
395
NFE
VibraninfGroundDragonLévitationPV
50Atq
70Déf
50SpA
50SpD
50Vit
70BST
340
NFE
VigorothNormalEsprit VitalPV
80Atq
80Déf
80SpA
55SpD
55Vit
90BST
440
NFE
Goupix-AlolaIceRideau NeigeAlerte NeigePV
38Atq
41Déf
40SpA
50SpD
65Vit
65BST
299
NFE
CarabaffeWaterTorrentCuvettePV
59Atq
63Déf
80SpA
65SpD
80Vit
58BST
405
NFE
BoustiflorGrassPoisonChlorophylleGloutonneriePV
65Atq
90Déf
50SpA
85SpD
45Vit
55BST
390
NFE
ScobolideBugPoisonPoint Poison
EssaimTurboPV
40Atq
55Déf
99SpA
40SpD
79Vit
47BST
360
NFE
YanmaBugFlyingTurbo
Oeil ComposéFouillePV
65Atq
65Déf
45SpA
75SpD
45Vit
95BST
390
NFE
DiamatDarkDragonAgitationPV
72Atq
85Déf
70SpA
65SpD
70Vit
58BST
420
LC
LC
AbraPsychicSynchro
AttentionGarde MagikPV
25Atq
20Déf
15SpA
105SpD
55Vit
90BST
310
LC
AmagaraRockIcePeau GeléeAlerte NeigePV
77Atq
59Déf
50SpA
67SpD
63Vit
46BST
362
LC
AnorithRockBugArmurbastonGlissadePV
45Atq
95Déf
50SpA
40SpD
50Vit
75BST
355
LC
VerpomGrassDragonMûrissement
GloutonneriePare-BallesPV
40Atq
40Déf
80SpA
40SpD
40Vit
20BST
260
LC
ArkéaptiRockFlyingDéfaitistePV
55Atq
112Déf
45SpA
74SpD
45Vit
70BST
401
LC
GalekidSteelRockFermeté
Tête de RocHeavy MetalPV
50Atq
70Déf
100SpA
40SpD
40Vit
30BST
330
LC
EmbrochetWaterGlissadePropulseurPV
41Atq
63Déf
40SpA
40SpD
30Vit
66BST
280
LC
CoupenotteDragonRivalité
Brise MouleTensionPV
46Atq
87Déf
60SpA
30SpD
40Vit
57BST
320
LC
AzurillNormalFairyIsograisse
ColoforceHerbivorePV
50Atq
20Déf
40SpA
20SpD
40Vit
20BST
190
LC
DrabyDragonTête de RocSans LimitePV
45Atq
75Déf
60SpA
40SpD
30Vit
50BST
300
LC
BalbutoGroundPsychicLévitationPV
40Atq
40Déf
55SpA
40SpD
70Vit
55BST
300
LC
BarlocheWaterGroundBenêt
AnticipationHydratationPV
50Atq
48Déf
43SpA
46SpD
41Vit
60BST
288
LC
TerhalSteelPsychicCorps SainLight MetalPV
40Atq
55Déf
80SpA
35SpD
60Vit
30BST
300
LC
ChétiflorGrassPoisonChlorophylleGloutonneriePV
50Atq
75Déf
35SpA
70SpD
30Vit
40BST
300
LC
GrelaçonIceTempo Perso
Corps GelFermetéPV
55Atq
69Déf
85SpA
32SpD
35Vit
28BST
304
LC
KeunotorNormalSimple
InconscientLunatiquePV
59Atq
45Déf
40SpA
35SpD
40Vit
31BST
250
LC
OpermineRockWaterGriffe Dure
SniperPickpocketPV
42Atq
52Déf
67SpA
39SpD
56Vit
50BST
306
LC
LarvadarBugEssaim
Oeil ComposéTélépathePV
25Atq
20Déf
20SpA
25SpD
45Vit
45BST
180
LC
ZébribonElectricParatonnerre
MotoriséHerbivorePV
45Atq
60Déf
32SpA
50SpD
32Vit
76BST
295
LC
ManzaïRockFermeté
Tête de RocPhobiquePV
50Atq
80Déf
95SpA
10SpD
45Vit
10BST
290
LC
CroquineGrassFeuille Garde
BenêtGluco-VoilePV
42Atq
30Déf
38SpA
30SpD
38Vit
32BST
210
LC
ViroventGrassGhostAéroportéInfiltrationPV
40Atq
65Déf
30SpA
45SpD
35Vit
60BST
275
LC
ArchéomireSteelPsychicLévitation
IgnifugéHeavy MetalPV
57Atq
24Déf
86SpA
24SpD
86Vit
23BST
300
LC
RozboutonGrassPoisonMédic Nature
Point PoisonFeuille GardePV
40Atq
30Déf
35SpA
50SpD
70Vit
55BST
280
LC
MustébouéeWaterGlissadeIgnifu-VoilePV
55Atq
65Déf
35SpA
60SpD
30Vit
85BST
330
LC
BulbizarreGrassPoisonEngraisChlorophyllePV
45Atq
49Déf
49SpA
65SpD
65Vit
45BST
318
LC
LaporeilleNormalFuite
MaladresseÉchauffementPV
55Atq
66Déf
44SpA
44SpD
56Vit
85BST
350
LC
SapereauNormalRamassage
BajouesColoforcePV
38Atq
36Déf
38SpA
32SpD
36Vit
57BST
237
LC
ChenitiBugMueEnvelocapePV
40Atq
29Déf
45SpA
29SpD
45Vit
36BST
224
LC
CacneaGrassVoile SableAbsorb EauPV
50Atq
85Déf
40SpA
85SpD
40Vit
35BST
335
LC
PimitoGrassChlorophylle
InsomniaMaladressePV
50Atq
62Déf
40SpA
62SpD
40Vit
50BST
304
LC
CarvanhaWaterDarkPeau DureTurboPV
45Atq
90Déf
20SpA
65SpD
20Vit
65BST
305
LC
ChenipanBugÉcran PoudreFuitePV
45Atq
30Déf
35SpA
20SpD
20Vit
45BST
195
LC
PiétacéIceIsograisse
Rideau NeigeSans LimitePV
108Atq
68Déf
45SpA
30SpD
40Vit
43BST
334
LC
CharbambinFireTorcheCorps ArdentPV
40Atq
50Déf
40SpA
50SpD
40Vit
35BST
255
LC
SalamècheFireBrasierForce SoleilPV
39Atq
52Déf
43SpA
60SpD
50Vit
65BST
309
LC
CeribouGrassChlorophyllePV
45Atq
35Déf
45SpA
62SpD
53Vit
35BST
275
LC
MarissonGrassEngraisPare-BallesPV
56Atq
61Déf
65SpA
48SpD
45Vit
38BST
313
LC
KhélocrokWaterPrognathe
Coque ArmureGlissadePV
50Atq
64Déf
50SpA
38SpD
38Vit
44BST
284
LC
GermignonGrassEngraisFeuille GardePV
45Atq
49Déf
65SpA
49SpD
65Vit
45BST
318
LC
OuisticramFireBrasierPoing de FerPV
44Atq
58Déf
44SpA
58SpD
44Vit
61BST
309
LC
LoupioWaterElectricAbsorb Volt
LumiattiranceAbsorb EauPV
75Atq
38Déf
38SpA
56SpD
56Vit
67BST
330
LC
KorillonPsychicLévitationPV
45Atq
30Déf
50SpA
65SpD
50Vit
45BST
285
LC
CoquiperlWaterCoque ArmurePhobiquePV
35Atq
64Déf
85SpA
74SpD
55Vit
32BST
345
LC
FlingousteWaterMéga BlasterPV
50Atq
53Déf
62SpA
58SpD
63Vit
44BST
330
LC
MéloFairyJoli Sourire
Garde MagikGarde AmiePV
50Atq
25Déf
28SpA
45SpD
55Vit
15BST
218
LC
PoulpafFightingÉchauffementTechnicienPV
50Atq
68Déf
60SpA
50SpD
50Vit
32BST
310
LC
ApitriniBugFlyingCherche MielAgitationPV
30Atq
30Déf
42SpA
30SpD
42Vit
70BST
244
LC
ÉcrapinceWaterHyper Cutter
Coque ArmureAdaptabilitéPV
43Atq
80Déf
65SpA
50SpD
35Vit
35BST
308
LC
Corayon-GalarGhostArmurouilléeCorps MauditPV
60Atq
55Déf
100SpA
65SpD
100Vit
30BST
410
LC
CosmogPsychicInconscientPV
43Atq
29Déf
31SpA
29SpD
31Vit
37BST
200
LC
DoudouvetGrassFairyFarceur
InfiltrationChlorophyllePV
40Atq
27Déf
60SpA
37SpD
50Vit
66BST
280
LC
CrabagarreFightingHyper Cutter
Poing de FerColériquePV
47Atq
82Déf
57SpA
42SpD
47Vit
63BST
338
LC
KranidosRockBrise MouleSans LimitePV
67Atq
125Déf
40SpA
30SpD
30Vit
58BST
350
LC
CradopaudPoisonFightingAnticipation
Peau SècheToxitouchePV
48Atq
61Déf
40SpA
61SpD
40Vit
50BST
300
LC
PolarhumeIceRideau Neige
Chasse-NeigePhobiquePV
55Atq
70Déf
40SpA
60SpD
40Vit
40BST
305
LC
OsselaitGroundTête de Roc
ParatonnerreArmurbastonPV
50Atq
50Déf
95SpA
40SpD
50Vit
35BST
320
LC
CharibariSteelSans LimiteHeavy MetalPV
72Atq
80Déf
49SpA
40SpD
49Vit
40BST
330
LC
HéricendreFireBrasierTorchePV
39Atq
52Déf
43SpA
60SpD
50Vit
65BST
309
LC
DarumarondFireAgitationAttentionPV
70Atq
90Déf
45SpA
15SpD
45Vit
50BST
315
LC
Darumarond-GalarIceAgitationAttentionPV
70Atq
90Déf
45SpA
15SpD
45Vit
50BST
315
LC
VivaldaimNormalGrassChlorophylle
HerbivoreSérénitéPV
60Atq
60Déf
50SpA
40SpD
50Vit
75BST
335
LC
SolochiDarkDragonAgitationPV
52Atq
65Déf
50SpA
45SpD
50Vit
38BST
300
LC
AraquaWaterBugAquabulleAbsorb EauPV
38Atq
40Déf
52SpA
40SpD
72Vit
27BST
269
LC
Taupiqueur-AlolaGroundSteelVoile Sable
Mèche RebelleForce SablePV
10Atq
55Déf
30SpA
35SpD
45Vit
90BST
265
LC
DoduoNormalFlyingFuite
MatinalPieds ConfusPV
35Atq
85Déf
45SpA
35SpD
35Vit
75BST
310
LC
MinidracoDragonMueÉcaille SpécialePV
41Atq
64Déf
45SpA
50SpD
50Vit
50BST
300
LC
FantyrmDragonGhostCorps Sain
InfiltrationCorps MauditPV
28Atq
60Déf
30SpA
40SpD
30Vit
82BST
270
LC
BaudriveGhostFlyingBoom Final
DélestageRage BrûlurePV
90Atq
50Déf
34SpA
60SpD
44Vit
70BST
348
LC
RototaupeGroundBaigne Sable
Force SableBrise MoulePV
60Atq
85Déf
40SpA
30SpD
45Vit
68BST
328
LC
SoporifikPsychicInsomnia
PrédictionAttentionPV
60Atq
48Déf
45SpA
43SpD
90Vit
42BST
328
LC
CouanetonWaterFlyingRegard Vif
Coeur de CoqHydratationPV
62Atq
44Déf
50SpA
44SpD
50Vit
55BST
305
LC
SkelénoxGhostLévitationFouillePV
20Atq
40Déf
90SpA
30SpD
90Vit
25BST
295
LC
CrabicoqueBugRockFermeté
Coque ArmureArmurouilléePV
50Atq
65Déf
85SpA
35SpD
35Vit
55BST
325
LC
ÉvoliNormalFuite
AdaptabilitéAnticipationPV
55Atq
55Déf
50SpA
45SpD
65Vit
55BST
325
LC
AboPoisonIntimidation
MueTensionPV
35Atq
60Déf
44SpA
40SpD
54Vit
55BST
288
LC
DynavoltElectricStatik
ParatonnerreMinusPV
40Atq
45Déf
40SpA
65SpD
40Vit
65BST
295
LC
ÉlekidElectricStatikEsprit VitalPV
45Atq
63Déf
37SpA
65SpD
55Vit
95BST
360
LC
LewsorPsychicTélépathe
SynchroAnalystePV
55Atq
55Déf
55SpA
85SpD
55Vit
30BST
335
LC
PsystigriPsychicRegard Vif
InfiltrationTempo PersoPV
62Atq
48Déf
54SpA
63SpD
60Vit
68BST
355
LC
NoeunoeufGrassPsychicChlorophylleRécoltePV
60Atq
40Déf
80SpA
60SpD
45Vit
40BST
325
LC
Canarticho-GalarFightingImpassibleQuerelleurPV
52Atq
95Déf
55SpA
58SpD
62Vit
55BST
377
LC
BarpauWaterGlissade
BenêtAdaptabilitéPV
20Atq
15Déf
20SpA
10SpD
55Vit
80BST
200
LC
FeunnecFireBrasierMagicienPV
40Atq
45Déf
40SpA
62SpD
60Vit
60BST
307
LC
GrindurGrassSteelÉpine de FerPV
44Atq
50Déf
91SpA
24SpD
86Vit
10BST
305
LC
PâtachiotFairyTempo PersoMaladressePV
37Atq
55Déf
70SpA
30SpD
55Vit
65BST
312
LC
DofinWaterIgnifu-VoilePV
70Atq
45Déf
40SpA
45SpD
40Vit
75BST
315
LC
ÉcayonWaterGlissade
LavaboIgnifu-VoilePV
49Atq
49Déf
56SpA
49SpD
61Vit
66BST
330
LC
FlabébéFairyFlora-VoileSymbiosePV
44Atq
38Déf
39SpA
61SpD
79Vit
42BST
303
LC
PasserougeNormalFlyingCoeur de CoqAiles BourrasquePV
45Atq
50Déf
43SpA
40SpD
38Vit
62BST
278
LC
MimantisGrassFeuille GardeContestationPV
40Atq
55Déf
35SpA
50SpD
35Vit
35BST
250
LC
TrompignonGrassPoisonPose SporeRégé-ForcePV
69Atq
55Déf
45SpA
55SpD
55Vit
15BST
294
LC
FrigodoDragonIceThermodynamiqueCorps GelPV
65Atq
75Déf
45SpA
35SpD
45Vit
55BST
320
LC
ViskuseWaterGhostAbsorb Eau
Corps MauditMoiteurPV
55Atq
40Déf
50SpA
65SpD
85Vit
40BST
335
LC
GrenousseWaterTorrentProtéenPV
41Atq
56Déf
40SpA
62SpD
44Vit
71BST
314
LC
ChochodileFireBrasierInconscientPV
67Atq
45Déf
59SpA
63SpD
40Vit
36BST
310
LC
FantominusGhostPoisonLévitationPV
30Atq
35Déf
30SpA
100SpD
35Vit
80BST
310
LC
RacaillouRockGroundTête de Roc
FermetéVoile SablePV
40Atq
80Déf
100SpA
30SpD
30Vit
20BST
300
LC
Racaillou-AlolaRockElectricMagnépiège
FermetéPeau ÉlectriquePV
40Atq
80Déf
100SpA
30SpD
30Vit
20BST
300
LC
GriknotDragonGroundVoile SablePeau DurePV
58Atq
70Déf
45SpA
40SpD
45Vit
42BST
300
LC
MordudorGhostPhobiquePV
45Atq
30Déf
70SpA
75SpD
70Vit
10BST
300
LC
Mordudor-MarcheGhostFuitePV
45Atq
30Déf
25SpA
75SpD
45Vit
80BST
300
LC
ChaglamNormalÉchauffement
Tempo PersoRegard VifPV
49Atq
55Déf
42SpA
42SpD
37Vit
85BST
310
LC
GerméclatRockPoisonDépôt ToxiqueCorrosionPV
48Atq
35Déf
42SpA
105SpD
60Vit
60BST
350
LC
PoissirèneWaterGlissade
Ignifu-VoileParatonnerrePV
45Atq
67Déf
60SpA
35SpD
50Vit
63BST
320
LC
GringolemGroundGhostPoing de Fer
MaladresseAnnule GardePV
59Atq
74Déf
50SpA
35SpD
50Vit
35BST
303
LC
MucusculeDragonHerbivore
HydratationPoisseuxPV
45Atq
50Déf
35SpA
55SpD
75Vit
40BST
300
LC
TournicotonGrassEffilochage
Régé-ForcePose SporePV
40Atq
40Déf
60SpA
40SpD
60Vit
10BST
250
LC
ScrutellaPsychicFouille
BattantMarque OmbrePV
45Atq
30Déf
50SpA
55SpD
65Vit
45BST
290
LC
ToutombeGhostRamassageBoule de PoilsPV
50Atq
61Déf
60SpA
30SpD
55Vit
34BST
290
LC
TadmorvPoisonPuanteur
GlueToxitouchePV
80Atq
80Déf
50SpA
40SpD
50Vit
25BST
325
LC
Tadmorv-AlolaPoisonDarkToxitouche
GloutonnerieOsmosePV
80Atq
80Déf
50SpA
40SpD
50Vit
25BST
325
LC
OuistempoGrassEngraisCréa-HerbePV
50Atq
65Déf
50SpA
40SpD
40Vit
65BST
310
LC
CaninosFireIntimidation
TorcheCoeur NoblePV
55Atq
70Déf
45SpA
70SpD
50Vit
60BST
350
LC
Caninos-HisuiFireRockIntimidation
TorcheTête de RocPV
60Atq
75Déf
45SpA
65SpD
50Vit
55BST
350
LC
LarvibuleBugEssaimPV
47Atq
62Déf
45SpA
55SpD
45Vit
46BST
300
LC
GlouptiPoisonSuintement
GlueGloutonneriePV
70Atq
43Déf
53SpA
43SpD
53Vit
40BST
302
LC
PtiraviNormalMédic Nature
SérénitéGarde AmiePV
100Atq
5Déf
5SpA
15SpD
65Vit
30BST
220
LC
BibichutPsychicCoeur Soin
AnticipationMiroir MagikPV
42Atq
30Déf
45SpA
56SpD
53Vit
39BST
265
LC
GalvaranElectricNormalPeau Sèche
Voile SableForce SoleilPV
44Atq
38Déf
33SpA
61SpD
43Vit
70BST
289
LC
HippopotasGroundSable VolantForce SablePV
68Atq
72Déf
78SpA
38SpD
42Vit
32BST
330
LC
MonorpaleSteelGhostAnnule GardePV
45Atq
80Déf
100SpA
35SpD
37Vit
28BST
325
LC
HoothootNormalFlyingInsomnia
Regard VifLentiteintéePV
60Atq
30Déf
30SpA
36SpD
56Vit
50BST
262
LC
GranivolGrassFlyingChlorophylle
Feuille GardeInfiltrationPV
35Atq
35Déf
40SpA
35SpD
55Vit
50BST
250
LC
HypotrempeWaterGlissade
SniperMoiteurPV
30Atq
40Déf
70SpA
70SpD
25Vit
60BST
295
LC
MalosseDarkFireMatinal
TorcheTensionPV
45Atq
60Déf
30SpA
80SpD
50Vit
65BST
330
LC
ToudoudouNormalFairyJoli Sourire
BattantGarde AmiePV
90Atq
30Déf
15SpA
40SpD
20Vit
15BST
210
LC
GrimalinDarkFairyFarceur
FouillePickpocketPV
45Atq
45Déf
30SpA
55SpD
40Vit
50BST
265
LC
SepiatopDarkPsychicContestation
VentouseInfiltrationPV
53Atq
54Déf
53SpA
37SpD
46Vit
45BST
288
LC
BébécailleDragonPare-Balles
Anti-BruitEnvelocapePV
45Atq
55Déf
65SpA
45SpD
45Vit
45BST
300
LC
StatitikBugElectricOeil Composé
TensionEssaimPV
50Atq
47Déf
50SpA
57SpD
50Vit
65BST
319
LC
KabutoRockWaterGlissade
ArmurbastonArmurouilléePV
30Atq
80Déf
90SpA
55SpD
45Vit
55BST
355
LC
CarabingBugEssaim
MueAnnule GardePV
50Atq
75Déf
45SpA
40SpD
45Vit
60BST
315
LC
TicSteelPlus
MinusCorps SainPV
40Atq
55Déf
70SpA
45SpD
60Vit
30BST
300
LC
SmogoPoisonLévitation
Gaz InhibiteurPuanteurPV
40Atq
65Déf
95SpA
60SpD
45Vit
35BST
340
LC
KrabbyWaterHyper Cutter
Coque ArmureSans LimitePV
30Atq
105Déf
90SpA
25SpD
25Vit
50BST
325
LC
CrikzikBugMueFuitePV
37Atq
25Déf
41SpA
25SpD
41Vit
25BST
194
LC
PyronilleBugFireCorps ArdentEssaimPV
55Atq
85Déf
55SpA
50SpD
55Vit
60BST
360
LC
EmbrylexRockGroundCranVoile SablePV
50Atq
64Déf
50SpA
45SpD
50Vit
41BST
300
LC
GourmeletNormalAroma-Voile
GloutonnerieIsograissePV
54Atq
45Déf
40SpA
35SpD
45Vit
35BST
254
LC
CoxyBugFlyingEssaim
MatinalPhobiquePV
40Atq
20Déf
30SpA
40SpD
80Vit
55BST
265
LC
ExcelangueNormalTempo Perso
BenêtCiel GrisPV
90Atq
55Déf
75SpA
60SpD
75Vit
30BST
385
LC
LiliaRockGrassVentouseLavaboPV
66Atq
41Déf
77SpA
61SpD
87Vit
23BST
355
LC
PonchiotNormalEsprit Vital
RamassageFuitePV
45Atq
60Déf
45SpA
25SpD
45Vit
55BST
275
LC
HélionceauFireNormalRivalité
TensionImpudencePV
62Atq
50Déf
58SpA
73SpD
54Vit
72BST
369
LC
FlamiaouFireBrasierIntimidationPV
45Atq
65Déf
40SpA
60SpD
40Vit
70BST
320
LC
FunécireGhostFireTorche
Corps ArdentInfiltrationPV
50Atq
30Déf
55SpA
65SpD
55Vit
20BST
275
LC
NénupiotWaterGrassGlissade
CuvetteTempo PersoPV
40Atq
30Déf
30SpA
40SpD
50Vit
30BST
220
LC
MachocFightingCran
Annule GardeImpassiblePV
70Atq
80Déf
50SpA
35SpD
35Vit
35BST
305
LC
MagbyFireCorps ArdentEsprit VitalPV
45Atq
75Déf
37SpA
70SpD
55Vit
83BST
365
LC
MagicarpeWaterGlissadePhobiquePV
20Atq
10Déf
55SpA
15SpD
20Vit
80BST
200
LC
MagnétiElectricSteelMagnépiège
FermetéAnalystePV
25Atq
35Déf
70SpA
95SpD
55Vit
45BST
325
LC
MakuhitaFightingIsograisse
CranSans LimitePV
72Atq
60Déf
30SpA
20SpD
30Vit
25BST
237
LC
FérosingeFightingEsprit Vital
ColériqueAcharnéPV
40Atq
80Déf
35SpA
35SpD
45Vit
70BST
305
LC
BabimantaWaterFlyingGlissade
Absorb EauIgnifu-VoilePV
45Atq
20Déf
50SpA
60SpD
120Vit
50BST
345
LC
VorastériePoisonWaterCruauté
ÉchauffementRégé-ForcePV
50Atq
53Déf
62SpA
43SpD
52Vit
45BST
305
LC
WattouatElectricStatikPlusPV
55Atq
40Déf
40SpA
65SpD
45Vit
35BST
280
LC
GrondogueDarkIntimidation
FuiteFilaturePV
60Atq
78Déf
60SpA
40SpD
51Vit
51BST
340
LC
MiaoussNormalRamassage
TechnicienTensionPV
40Atq
45Déf
35SpA
40SpD
40Vit
90BST
290
LC
Miaouss-AlolaDarkRamassage
TechnicienPhobiquePV
40Atq
35Déf
35SpA
50SpD
40Vit
90BST
290
LC
Miaouss-GalarSteelRamassage
Griffe DureTensionPV
50Atq
65Déf
55SpA
40SpD
40Vit
40BST
290
LC
KungfouineFightingAttention
Régé-ForceTémérairePV
45Atq
85Déf
50SpA
55SpD
50Vit
65BST
350
LC
CrèmyFairyGluco-VoileAroma-VoilePV
45Atq
40Déf
40SpA
50SpD
61Vit
34BST
270
LC
Mime Jr.PsychicFairyAnti-Bruit
FiltreTechnicienPV
20Atq
25Déf
45SpA
70SpD
90Vit
60BST
310
LC
ChinchidouNormalJoli Sourire
TechnicienMulti-CoupsPV
55Atq
50Déf
40SpA
40SpD
40Vit
75BST
300
LC
SpododoGrassFairyLumiattirance
Pose SporeCuvettePV
40Atq
35Déf
55SpA
65SpD
75Vit
15BST
285
LC
TiboudetGroundTempo Perso
EnduranceAttentionPV
70Atq
100Déf
70SpA
45SpD
55Vit
45BST
385
LC
GobouWaterTorrentMoiteurPV
50Atq
70Déf
50SpA
50SpD
50Vit
40BST
310
LC
GoinfrexNormalRamassage
IsograisseGloutonneriePV
135Atq
85Déf
40SpA
40SpD
85Vit
5BST
390
LC
MunnaPsychicPrédiction
SynchroTélépathePV
76Atq
25Déf
45SpA
67SpD
55Vit
24BST
292
LC
SelutinRockSel Purificateur
FermetéCorps SainPV
55Atq
55Déf
75SpA
35SpD
35Vit
25BST
280
LC
NatuPsychicFlyingSynchro
MatinalMiroir MagikPV
40Atq
50Déf
45SpA
70SpD
45Vit
70BST
320
LC
GoupilouDarkFuite
DélestageFilaturePV
40Atq
28Déf
28SpA
47SpD
52Vit
50BST
245
LC
Nidoran-FPoisonPoint Poison
RivalitéAgitationPV
55Atq
47Déf
52SpA
40SpD
40Vit
41BST
275
LC
Nidoran-MPoisonPoint Poison
RivalitéAgitationPV
46Atq
57Déf
40SpA
40SpD
40Vit
50BST
273
LC
NingaleBugGroundOeil ComposéFuitePV
31Atq
45Déf
90SpA
30SpD
30Vit
40BST
266
LC
SonistrelleFlyingDragonFouille
InfiltrationTélépathePV
40Atq
30Déf
35SpA
45SpD
40Vit
55BST
245
LC
TarinorRockFermeté
MagnépiègeForce SablePV
30Atq
45Déf
135SpA
45SpD
90Vit
30BST
375
LC
ChamallotFireGroundBenêt
SimpleTempo PersoPV
60Atq
60Déf
40SpA
65SpD
45Vit
35BST
305
LC
LilliterelleBugEssaimLentiteintéePV
33Atq
46Déf
40SpA
21SpD
25Vit
45BST
210
LC
MystherbeGrassPoisonChlorophylleFuitePV
45Atq
50Déf
55SpA
75SpD
65Vit
30BST
320
LC
AmonitaRockWaterGlissade
Coque ArmureArmurouilléePV
35Atq
40Déf
100SpA
90SpD
55Vit
35BST
355
LC
OnixRockGroundTête de Roc
FermetéArmurouilléePV
35Atq
45Déf
160SpA
30SpD
45Vit
70BST
385
LC
MoustillonWaterTorrentCoque ArmurePV
55Atq
55Déf
45SpA
63SpD
45Vit
45BST
308
LC
PandespiègleFightingPoing de Fer
Brise MouleQuerelleurPV
67Atq
82Déf
62SpA
46SpD
48Vit
43BST
348
LC
FlotajouWaterGloutonnerieTorrentPV
50Atq
53Déf
48SpA
53SpD
48Vit
64BST
316
LC
FeuillajouGrassGloutonnerieEngraisPV
50Atq
53Déf
48SpA
53SpD
48Vit
64BST
316
LC
FlamajouFireGloutonnerieBrasierPV
50Atq
53Déf
48SpA
53SpD
48Vit
64BST
316
LC
ParasBugGrassPose Spore
Peau SècheMoiteurPV
35Atq
70Déf
55SpA
45SpD
55Vit
25BST
285
LC
RatentifNormalFuite
Regard VifAnalystePV
45Atq
55Déf
39SpA
35SpD
39Vit
42BST
255
LC
PohmElectricStatik
Médic NaturePoing de FerPV
45Atq
50Déf
20SpA
40SpD
25Vit
60BST
240
LC
ScalpionDarkSteelAcharné
AttentionPressionPV
45Atq
85Déf
70SpA
40SpD
40Vit
60BST
340
LC
ChlorobuleGrassChlorophylle
Tempo PersoFeuille GardePV
45Atq
35Déf
50SpA
70SpD
50Vit
30BST
280
LC
PhanpyGroundRamassageVoile SablePV
90Atq
60Déf
60SpA
40SpD
40Vit
40BST
330
LC
BrocélômeGhostGrassMédic Nature
FouilleRécoltePV
43Atq
70Déf
48SpA
50SpD
60Vit
38BST
309
LC
PichuElectricStatikParatonnerrePV
20Atq
40Déf
15SpA
35SpD
35Vit
60BST
205
LC
RoucoolNormalFlyingRegard Vif
Pieds ConfusCoeur de CoqPV
40Atq
45Déf
40SpA
35SpD
35Vit
56BST
251
LC
PoichigeonNormalFlyingCoeur de Coq
ChanceuxRivalitéPV
50Atq
55Déf
50SpA
36SpD
30Vit
43BST
264
LC
PicassautNormalFlyingRegard Vif
Multi-CoupsRamassagePV
35Atq
75Déf
30SpA
30SpD
30Vit
65BST
265
LC
PomdepikBugFermetéEnvelocapePV
50Atq
65Déf
90SpA
35SpD
35Vit
15BST
290
LC
TiploufWaterTorrentBattantPV
53Atq
51Déf
53SpA
61SpD
56Vit
40BST
314
LC
PtitardWaterAbsorb Eau
MoiteurGlissadePV
40Atq
50Déf
40SpA
40SpD
40Vit
90BST
300
LC
PoltchageistGrassGhostAux Petits SoinsIgnifugéPV
40Atq
45Déf
45SpA
74SpD
54Vit
50BST
308
LC
PonytaFireFuite
TorcheCorps ArdentPV
50Atq
85Déf
55SpA
65SpD
65Vit
90BST
410
LC
Ponyta-GalarPsychicFuite
Voile PastelAnticipationPV
50Atq
85Déf
55SpA
65SpD
65Vit
90BST
410
LC
MedhyènaDarkFuite
Pied VélocePhobiquePV
35Atq
55Déf
35SpA
30SpD
30Vit
35BST
220
LC
OtaquinWaterTorrentHydrata-SonPV
50Atq
54Déf
54SpA
66SpD
56Vit
40BST
320
LC
PsykokwakWaterMoiteur
Ciel GrisGlissadePV
50Atq
52Déf
48SpA
65SpD
50Vit
55BST
320
LC
PitrouilleGhostGrassRamassage
FouilleInsomniaPV
49Atq
66Déf
70SpA
44SpD
55Vit
51BST
335
LC
Pitrouille-MaxiGhostGrassRamassage
FouilleInsomniaPV
54Atq
66Déf
70SpA
44SpD
55Vit
46BST
335
LC
Pitrouille-MiniGhostGrassRamassage
FouilleInsomniaPV
44Atq
66Déf
70SpA
44SpD
55Vit
56BST
335
LC
Pitrouille-UltraGhostGrassRamassage
FouilleInsomniaPV
59Atq
66Déf
70SpA
44SpD
55Vit
41BST
335
LC
ChacripanDarkÉchauffement
DélestageFarceurPV
41Atq
50Déf
37SpA
50SpD
37Vit
66BST
281
LC
CoiffetonWaterTorrentImpudencePV
55Atq
65Déf
45SpA
50SpD
45Vit
50BST
310
LC
TarsalPsychicFairySynchro
CalqueTélépathePV
28Atq
25Déf
25SpA
45SpD
35Vit
40BST
198
LC
RattataNormalFuite
CranAgitationPV
30Atq
56Déf
35SpA
25SpD
35Vit
72BST
253
LC
Rattata-AlolaDarkNormalGloutonnerie
AgitationIsograissePV
30Atq
56Déf
35SpA
25SpD
35Vit
72BST
253
LC
LéboulérouBugOeil ComposéMuePV
41Atq
50Déf
60SpA
31SpD
58Vit
30BST
270
LC
RémoraidWaterAgitation
SniperLunatiquePV
35Atq
65Déf
35SpA
65SpD
35Vit
65BST
300
LC
RhinocorneGroundRockParatonnerre
Tête de RocTémérairePV
80Atq
85Déf
95SpA
30SpD
30Vit
25BST
345
LC
RioluFightingImpassible
AttentionFarceurPV
40Atq
70Déf
40SpA
35SpD
40Vit
60BST
285
LC
RocabotRockRegard Vif
Esprit VitalImpassible
(Tempo Perso)PV
45Atq
65Déf
40SpA
30SpD
40Vit
60BST
280
LC
NodulitheRockFermeté
ArmurouilléeForce SablePV
55Atq
75Déf
85SpA
25SpD
25Vit
15BST
280
LC
CharbiRockTurbine
IgnifugéTorchePV
30Atq
40Déf
50SpA
40SpD
50Vit
30BST
240
LC
MinisangeFlyingRegard Vif
TensionCoeur de CoqPV
38Atq
47Déf
35SpA
33SpD
35Vit
57BST
245
LC
BrindibouGrassFlyingEngraisLongue PortéePV
68Atq
55Déf
55SpA
50SpD
50Vit
42BST
320
LC
TritoxPoisonFireCorrosionBenêtPV
48Atq
44Déf
40SpA
71SpD
40Vit
77BST
320
LC
MascaïmanGroundDarkIntimidation
ImpudenceColériquePV
50Atq
72Déf
35SpA
35SpD
35Vit
65BST
292
LC
SabeletteGroundVoile SableBaigne SablePV
50Atq
75Déf
85SpA
20SpD
30Vit
40BST
300
LC
Sabelette-AlolaIceSteelRideau NeigeChasse-NeigePV
50Atq
75Déf
90SpA
10SpD
35Vit
40BST
300
LC
BacabouhGhostGroundSable HumideVoile SablePV
55Atq
55Déf
80SpA
70SpD
45Vit
15BST
320
LC
LépidonilleBugÉcran Poudre
Oeil ComposéGarde AmiePV
38Atq
35Déf
40SpA
27SpD
25Vit
35BST
200
LC
FlambinoFireBrasierLibéroPV
50Atq
71Déf
40SpA
40SpD
40Vit
69BST
310
LC
GrainipiotGrassChlorophylle
MatinalPickpocketPV
40Atq
40Déf
50SpA
30SpD
30Vit
30BST
220
LC
OtariaWaterIsograisse
HydratationCorps GelPV
65Atq
45Déf
55SpA
45SpD
70Vit
45BST
325
LC
FouinetteNormalFuite
Regard VifFouillePV
35Atq
46Déf
34SpA
35SpD
45Vit
20BST
215
LC
LarveyetteBugGrassEssaim
ChlorophylleEnvelocapePV
45Atq
53Déf
70SpA
40SpD
60Vit
42BST
310
LC
KokiyasWaterCoque Armure
Multi-CoupsEnvelocapePV
30Atq
65Déf
100SpA
45SpD
25Vit
40BST
305
LC
SancokiWaterGlue
LavaboForce SablePV
76Atq
48Déf
48SpA
57SpD
62Vit
34BST
325
LC
EscargaumeBugHydratation
Coque ArmureEnvelocapePV
50Atq
40Déf
85SpA
40SpD
65Vit
25BST
305
LC
DinoclierRockSteelFermetéAnti-BruitPV
30Atq
42Déf
118SpA
42SpD
88Vit
30BST
350
LC
LixyElectricRivalité
IntimidationCranPV
45Atq
65Déf
34SpA
40SpD
34Vit
45BST
263
LC
GribouraignePoisonNormalDélestage
PickpocketFarceurPV
40Atq
65Déf
35SpA
40SpD
35Vit
75BST
290
LC
BalignonGrassPose Spore
Soin PoisonPied VélocePV
60Atq
40Déf
60SpA
40SpD
60Vit
35BST
295
LC
PolichombrGhostInsomnia
FouilleCorps MauditPV
44Atq
75Déf
35SpA
63SpD
33Vit
45BST
295
LC
DunajaGroundExpul'Sable
MueVoile SablePV
52Atq
57Déf
75SpA
35SpD
50Vit
46BST
315
LC
ThéffroiGhostArmurouilléeCorps MauditPV
40Atq
45Déf
45SpA
74SpD
54Vit
50BST
308
LC
GrillepattesFireBugTorche
Écran FuméeCorps ArdentPV
50Atq
65Déf
45SpA
50SpD
50Vit
45BST
305
LC
CabriolaineGrassHerbivoreToison HerbuePV
66Atq
65Déf
48SpA
62SpD
57Vit
52BST
350
LC
SkittyNormalJoli Sourire
NormalisePeau MiraclePV
50Atq
45Déf
45SpA
35SpD
35Vit
50BST
260
LC
RapionPoisonBugArmurbaston
SniperRegard VifPV
40Atq
50Déf
90SpA
30SpD
55Vit
65BST
330
LC
VenalguePoisonWaterPoint Poison
ToxitoucheAdaptabilitéPV
50Atq
60Déf
60SpA
60SpD
60Vit
30BST
320
LC
RongourmandNormalBajouesGloutonneriePV
70Atq
55Déf
55SpA
35SpD
35Vit
25BST
275
LC
ParecoolNormalAbsentéismePV
60Atq
60Déf
60SpA
35SpD
35Vit
30BST
280
LC
RamolossWaterPsychicBenêt
Tempo PersoRégé-ForcePV
90Atq
65Déf
65SpA
40SpD
40Vit
15BST
315
LC
Ramoloss-GalarPsychicGloutonnerie
Tempo PersoRégé-ForcePV
90Atq
65Déf
65SpA
40SpD
40Vit
15BST
315
LC
LimagmaFireArmumagma
Corps ArdentArmurouilléePV
40Atq
40Déf
40SpA
70SpD
40Vit
20BST
250
LC
OliviniGrassNormalMatinalRécoltePV
41Atq
35Déf
45SpA
58SpD
51Vit
30BST
260
LC
LippoutiIcePsychicBenêt
PrédictionHydratationPV
45Atq
30Déf
15SpA
85SpD
65Vit
65BST
305
LC
VipélierreGrassEngraisContestationPV
45Atq
45Déf
55SpA
45SpD
55Vit
63BST
308
LC
FrissonilleIceBugÉcran PoudreÉcailles GlacéesPV
30Atq
25Déf
35SpA
45SpD
30Vit
20BST
185
LC
StalgaminIceAttention
Corps GelLunatiquePV
50Atq
50Déf
50SpA
50SpD
50Vit
50BST
300
LC
BlizziGrassIceAlerte NeigeAnti-BruitPV
60Atq
62Déf
50SpA
62SpD
60Vit
40BST
334
LC
SnubbullFairyIntimidation
FuitePhobiquePV
60Atq
80Déf
50SpA
40SpD
40Vit
30BST
300
LC
LarméléonWaterTorrentSniperPV
50Atq
40Déf
40SpA
70SpD
40Vit
70BST
310
LC
NucléosPsychicEnvelocape
Garde MagikRégé-ForcePV
45Atq
30Déf
40SpA
105SpD
50Vit
20BST
290
LC
PiafabecNormalFlyingRegard VifSniperPV
40Atq
60Déf
30SpA
31SpD
31Vit
70BST
262
LC
ObalieIceWaterIsograisse
Corps GelBenêtPV
70Atq
40Déf
50SpA
55SpD
50Vit
25BST
290
LC
MimigalBugPoisonEssaim
InsomniaSniperPV
40Atq
60Déf
40SpA
40SpD
40Vit
30BST
250
LC
SpoinkPsychicIsograisse
Tempo PersoGloutonneriePV
60Atq
25Déf
35SpA
70SpD
80Vit
60BST
330
LC
PoussachaGrassEngraisProtéenPV
40Atq
61Déf
54SpA
45SpD
45Vit
65BST
310
LC
FluvetinFairyCoeur SoinAroma-VoilePV
78Atq
52Déf
60SpA
63SpD
65Vit
23BST
341
LC
CarapuceWaterTorrentCuvettePV
44Atq
48Déf
65SpA
50SpD
64Vit
43BST
314
LC
ÉtourmiNormalFlyingRegard VifTémérairePV
40Atq
55Déf
30SpA
30SpD
30Vit
60BST
245
LC
StariWaterLumiattirance
Médic NatureAnalystePV
30Atq
45Déf
55SpA
70SpD
55Vit
85BST
340
LC
NounoursonNormalFightingBoule de Poils
MaladresseJoli SourirePV
70Atq
75Déf
50SpA
45SpD
50Vit
50BST
340
LC
MoufouettePoisonDarkPuanteur
Boom FinalRegard VifPV
63Atq
63Déf
47SpA
41SpD
41Vit
74BST
329
LC
TournegrinGrassChlorophylle
Force SoleilMatinalPV
30Atq
30Déf
30SpA
30SpD
30Vit
30BST
180
LC
ArakdoBugWaterGlissadeCuvettePV
40Atq
30Déf
32SpA
50SpD
52Vit
65BST
269
LC
TyltonNormalFlyingMédic NatureCiel GrisPV
45Atq
40Déf
60SpA
40SpD
75Vit
50BST
310
LC
MarcacrinIceGroundBenêt
Rideau NeigeIsograissePV
50Atq
50Déf
40SpA
30SpD
30Vit
50BST
250
LC
SucroquinFairyGluco-VoileDélestagePV
62Atq
48Déf
66SpA
59SpD
57Vit
49BST
341
LC
TêtampouleElectricTempo Perso
StatikMoiteurPV
61Atq
31Déf
41SpA
59SpD
35Vit
45BST
272
LC
NirondelleNormalFlyingCranQuerelleurPV
40Atq
55Déf
30SpA
30SpD
30Vit
85BST
270
LC
CompagnolNormalFuite
RamassageTempo PersoPV
50Atq
50Déf
45SpA
40SpD
45Vit
75BST
305
LC
SaquedeneuGrassChlorophylle
Feuille GardeRégé-ForcePV
65Atq
55Déf
115SpA
100SpD
40Vit
60BST
435
LC
TissenbouleBugInsomniaFilaturePV
35Atq
41Déf
45SpA
29SpD
40Vit
20BST
210
LC
TeddiursaNormalRamassage
Pied VéloceCherche MielPV
60Atq
80Déf
50SpA
50SpD
50Vit
40BST
330
LC
TentacoolWaterPoisonCorps Sain
SuintementCuvettePV
40Atq
40Déf
35SpA
50SpD
100Vit
70BST
335
LC
GruikuiFireBrasierIsograissePV
65Atq
63Déf
45SpA
45SpD
45Vit
45BST
308
LC
CharpentiFightingCran
Sans LimitePoing de FerPV
75Atq
80Déf
55SpA
25SpD
35Vit
35BST
305
LC
ForgeretteFairySteelBrise Moule
Tempo PersoPickpocketPV
50Atq
45Déf
45SpA
35SpD
64Vit
58BST
297
LC
CarapagosWaterRockSolide Roc
FermetéGlissadePV
54Atq
78Déf
103SpA
53SpD
45Vit
22BST
355
LC
TerracoolGroundGrassForce FongiquePV
40Atq
40Déf
35SpA
50SpD
100Vit
70BST
335
LC
TogepiFairyAgitation
SérénitéChanceuxPV
35Atq
20Déf
65SpA
40SpD
65Vit
20BST
245
LC
PoussifeuFireBrasierTurboPV
45Atq
60Déf
40SpA
70SpD
50Vit
45BST
310
LC
KaiminusWaterTorrentSans LimitePV
50Atq
65Déf
64SpA
44SpD
48Vit
43BST
314
LC
ToxizapElectricPoisonPhobique
StatikMaladressePV
40Atq
38Déf
35SpA
54SpD
35Vit
40BST
242
LC
KraknoixGroundHyper Cutter
Piège SableSans LimitePV
45Atq
100Déf
45SpA
45SpD
45Vit
10BST
290
LC
ArckoGrassEngraisDélestagePV
40Atq
45Déf
35SpA
65SpD
55Vit
70BST
310
LC
MiamiasmePoisonPuanteur
GlueBoom FinalPV
50Atq
50Déf
62SpA
40SpD
62Vit
65BST
329
LC
TortipoussGrassEngraisCoque ArmurePV
55Atq
68Déf
64SpA
45SpD
55Vit
31BST
318
LC
TritondeWaterGlissade
HydratationAbsorb EauPV
50Atq
50Déf
40SpA
50SpD
40Vit
64BST
294
LC
AnchwattElectricLévitationPV
35Atq
55Déf
40SpA
45SpD
40Vit
60BST
275
LC
DebugantFightingCran
ImpassibleEsprit VitalPV
35Atq
35Déf
35SpA
35SpD
35Vit
35BST
210
LC
PtyranidurRockDragonPrognatheFermetéPV
58Atq
89Déf
77SpA
45SpD
45Vit
48BST
362
LC
SorbébéIceCorps Gel
Rideau NeigeArmurouilléePV
36Atq
50Déf
50SpA
65SpD
60Vit
44BST
305
LC
VrombiSteelPoisonEnvelocapeDébut CalmePV
45Atq
70Déf
63SpA
30SpD
45Vit
47BST
300
LC
VenipatteBugPoisonPoint Poison
EssaimTurboPV
30Atq
45Déf
59SpA
30SpD
39Vit
57BST
260
LC
MimitossBugPoisonOeil Composé
LentiteintéeFuitePV
60Atq
55Déf
50SpA
40SpD
55Vit
45BST
305
LC
VoltorbeElectricAnti-Bruit
StatikBoom FinalPV
40Atq
30Déf
50SpA
55SpD
55Vit
100BST
330
LC
Voltorbe-HisuiElectricGrassAnti-Bruit
StatikBoom FinalPV
40Atq
30Déf
50SpA
55SpD
55Vit
100BST
330
LC
VostournoDarkFlyingCoeur de Coq
EnvelocapeArmurouilléePV
70Atq
55Déf
75SpA
45SpD
65Vit
60BST
370
LC
GoupixFireTorcheSécheressePV
38Atq
41Déf
40SpA
50SpD
65Vit
65BST
299
LC
WailmerWaterIgnifu-Voile
BenêtPressionPV
130Atq
70Déf
35SpA
70SpD
35Vit
60BST
400
LC
ZapétrelElectricFlyingTurbine Éolienne
Absorb VoltBattantPV
40Atq
40Déf
35SpA
55SpD
40Vit
70BST
280
LC
AspicotBugPoisonÉcran PoudreFuitePV
40Atq
35Déf
30SpA
20SpD
20Vit
50BST
195
LC
ChuchmurNormalAnti-BruitPhobiquePV
64Atq
51Déf
23SpA
51SpD
23Vit
28BST
240
LC
TaupikeauWaterPoisseux
PhobiqueVoile SablePV
10Atq
55Déf
25SpA
35SpD
25Vit
95BST
245
LC
SovkipouBugWaterEscampettePV
25Atq
35Déf
40SpA
20SpD
30Vit
80BST
230
LC
GoéliseWaterFlyingRegard Vif
HydratationCuvettePV
40Atq
30Déf
30SpA
55SpD
30Vit
85BST
270
LC
ChovsourirPsychicFlyingInconscient
MaladresseSimplePV
65Atq
45Déf
43SpA
55SpD
43Vit
72BST
323
LC
MoumoutonNormalBoule de Poils
FuitePare-BallesPV
42Atq
40Déf
55SpA
40SpD
45Vit
48BST
270
LC
AxolotoWaterGroundMoiteur
Absorb EauInconscientPV
55Atq
45Déf
45SpA
25SpD
25Vit
15BST
210
LC
Axoloto-PaldeaPoisonGroundPoint Poison
Absorb EauInconscientPV
55Atq
45Déf
45SpA
25SpD
25Vit
15BST
210
LC
ChenipotteBugÉcran PoudreFuitePV
45Atq
45Déf
35SpA
20SpD
30Vit
20BST
195
LC
OkéokéPsychicMarque OmbreTélépathePV
95Atq
23Déf
48SpA
23SpD
48Vit
23BST
260
LC
TutafehGhostMomiePV
38Atq
30Déf
85SpA
55SpD
65Vit
30BST
303
LC
Tutafeh-GalarGroundGhostÂme VagabondePV
38Atq
55Déf
85SpA
30SpD
65Vit
30BST
303
LC
VoltoutouElectricRamasse BallPhobiquePV
59Atq
45Déf
50SpA
40SpD
50Vit
26BST
270
LC
MangloutonNormalFilature
PrognatheAdaptabilitéPV
48Atq
70Déf
30SpA
30SpD
30Vit
45BST
253
LC
ZigzatonNormalRamassage
GloutonneriePied VélocePV
38Atq
30Déf
41SpA
30SpD
41Vit
60BST
240
LC
Zigzaton-GalarDarkNormalRamassage
GloutonneriePied VélocePV
38Atq
30Déf
41SpA
30SpD
41Vit
60BST
240
LC
ZoruaDarkIllusionPV
40Atq
65Déf
40SpA
80SpD
40Vit
65BST
330
LC
Zorua-HisuiNormalGhostIllusionPV
35Atq
60Déf
40SpA
85SpD
40Vit
70BST
330
LC
NosferaptiPoisonFlyingAttentionInfiltrationPV
40Atq
45Déf
35SpA
30SpD
40Vit
55BST
245
"""


moves="""FlamethrowerFireSpecialPower
90Accuracy
100%PP
2410% chance to burn the target.
Seismic TossFightingPhysicalPower
—Accuracy
100%PP
32Does damage equal to the user's level.
Sleep TalkNormalStatusAccuracy
—PP
16User must be asleep. Uses another known move.
SporeGrassStatusAccuracy
100%PP
24Causes the target to fall asleep.
AccelerockRockPhysicalPower
40Accuracy
100%PP
32Usually goes first.
Acid ArmorPoisonStatusAccuracy
—PP
32Raises the user's Defense by 2.
AcrobaticsFlyingPhysicalPower
55Accuracy
100%PP
24Power doubles if the user has no held item.
AeroblastFlyingSpecialPower
100Accuracy
95%PP
8High critical hit ratio.
AgilityPsychicStatusAccuracy
—PP
48Raises the user's Speed by 2.
Air SlashFlyingSpecialPower
75Accuracy
95%PP
2430% chance to make the target flinch.
Alluring VoiceFairySpecialPower
80Accuracy
100%PP
16100% confuse target that had a stat rise this turn.
Anchor ShotSteelPhysicalPower
80Accuracy
100%PP
32Prevents the target from switching out.
Apple AcidGrassSpecialPower
80Accuracy
100%PP
16100% chance to lower the target's Sp. Def by 1.
Aqua CutterWaterPhysicalPower
70Accuracy
100%PP
32High critical hit ratio.
Aqua StepWaterPhysicalPower
80Accuracy
100%PP
16100% chance to raise the user's Speed by 1.
Aqua TailWaterPhysicalPower
90Accuracy
90%PP
16No additional effect.
Armor CannonFireSpecialPower
120Accuracy
100%PP
8Lowers the user's Defense and Sp. Def by 1.
AromatherapyGrassStatusAccuracy
—PP
8Cures the user's party of all status conditions.
Astral BarrageGhostSpecialPower
120Accuracy
100%PP
8No additional effect. Hits adjacent foes.
Attack OrderBugPhysicalPower
90Accuracy
100%PP
24High critical hit ratio.
Aura SphereFightingSpecialPower
80Accuracy
—PP
32This move does not check accuracy.
Aurora VeilIceStatusAccuracy
—PP
32For 5 turns, damage to allies halved. Snow only.
AutotomizeSteelStatusAccuracy
—PP
24Raises the user's Speed by 2; user loses 100 kg.
AvalancheIcePhysicalPower
60Accuracy
100%PP
16Power doubles if user is damaged by the target.
Baneful BunkerPoisonStatusAccuracy
—PP
16Protects from moves. Contact: poison.
Barb BarragePoisonPhysicalPower
60Accuracy
100%PP
1650% psn. 2x power if target already poisoned.
Baton PassNormalStatusAccuracy
—PP
64User switches, passing stat changes and more.
Beak BlastFlyingPhysicalPower
100Accuracy
100%PP
24Burns on contact with the user before it moves.
Behemoth BashSteelPhysicalPower
100Accuracy
100%PP
8No additional effect.
Behemoth BladeSteelPhysicalPower
100Accuracy
100%PP
8No additional effect.
Belly DrumNormalStatusAccuracy
—PP
16User loses 50% max HP. Maximizes Attack.
Bitter BladeFirePhysicalPower
90Accuracy
100%PP
16User recovers 50% of the damage dealt.
Bitter MaliceGhostSpecialPower
75Accuracy
100%PP
16100% chance to lower the target's Attack by 1.
Blaze KickFirePhysicalPower
85Accuracy
90%PP
16High critical hit ratio. 10% chance to burn.
Bleakwind StormFlyingSpecialPower
100Accuracy
80%PP
1630% to lower foe(s) Speed by 1. Rain: can't miss.
BlizzardIceSpecialPower
110Accuracy
70%PP
810% chance to freeze foe(s). Can't miss in Snow.
Blood MoonNormalSpecialPower
140Accuracy
100%PP
8Cannot be selected the turn after it's used.
Blue FlareFireSpecialPower
130Accuracy
85%PP
820% chance to burn the target.
Body PressFightingPhysicalPower
80Accuracy
100%PP
16Uses user's Def stat as Atk in damage calculation.
Body SlamNormalPhysicalPower
85Accuracy
100%PP
2430% chance to paralyze the target.
Bolt BeakElectricPhysicalPower
85Accuracy
100%PP
16Power doubles if user moves before the target.
Bolt StrikeElectricPhysicalPower
130Accuracy
85%PP
820% chance to paralyze the target.
BonemerangGroundPhysicalPower
50Accuracy
90%PP
16Hits 2 times in one turn.
BoomburstNormalSpecialPower
140Accuracy
100%PP
16No additional effect. Hits adjacent Pokemon.
Brave BirdFlyingPhysicalPower
120Accuracy
100%PP
24Has 33% recoil.
Brick BreakFightingPhysicalPower
75Accuracy
100%PP
24Destroys screens, unless the target is immune.
Bug BuzzBugSpecialPower
90Accuracy
100%PP
1610% chance to lower the target's Sp. Def by 1.
Bulk UpFightingStatusAccuracy
—PP
32Raises the user's Attack and Defense by 1.
Bullet PunchSteelPhysicalPower
40Accuracy
100%PP
48Usually goes first.
Calm MindPsychicStatusAccuracy
—PP
32Raises the user's Sp. Atk and Sp. Def by 1.
Ceaseless EdgeDarkPhysicalPower
65Accuracy
90%PP
24Sets a layer of Spikes on the opposing side.
Chilly ReceptionIceStatusAccuracy
—PP
16Starts Snow. User switches out.
ChloroblastGrassSpecialPower
150Accuracy
95%PP
8User loses 50% max HP.
Circle ThrowFightingPhysicalPower
60Accuracy
90%PP
16Forces the target to switch to a random ally.
Clanging ScalesDragonSpecialPower
110Accuracy
100%PP
8Lowers the user's Defense by 1.
Clangorous SoulDragonStatusAccuracy
100%PP
8User loses 33% of its max HP. +1 to all stats.
Clear SmogPoisonSpecialPower
50Accuracy
—PP
24Resets all of the target's stat stages to 0.
Close CombatFightingPhysicalPower
120Accuracy
100%PP
8Lowers the user's Defense and Sp. Def by 1.
CoilPoisonStatusAccuracy
—PP
32Raises user's Attack, Defense, accuracy by 1.
Collision CourseFightingPhysicalPower
100Accuracy
100%PP
8Deals 1.3333x damage with supereffective hits.
Core EnforcerDragonSpecialPower
100Accuracy
100%PP
16Nullifies the foe(s) Ability if the foe(s) move first.
Cotton GuardGrassStatusAccuracy
—PP
16Raises the user's Defense by 3.
Court ChangeNormalStatusAccuracy
100%PP
16Swaps user's field effects with the opposing side.
CrabhammerWaterPhysicalPower
100Accuracy
90%PP
16High critical hit ratio.
Cross ChopFightingPhysicalPower
100Accuracy
80%PP
8High critical hit ratio.
CrunchDarkPhysicalPower
80Accuracy
100%PP
2420% chance to lower the target's Defense by 1.
CurseGhostStatusAccuracy
—PP
16Curses if Ghost, else -1 Spe, +1 Atk, +1 Def.
Darkest LariatDarkPhysicalPower
85Accuracy
100%PP
16Ignores the target's stat stage changes.
Dark PulseDarkSpecialPower
80Accuracy
100%PP
2420% chance to make the target flinch.
Dazzling GleamFairySpecialPower
80Accuracy
100%PP
16No additional effect. Hits adjacent foes.
DefogFlyingStatusAccuracy
—PP
24-1 evasion; clears terrain and hazards on both sides.
Destiny BondGhostStatusAccuracy
—PP
8If an opponent knocks out the user, it also faints.
DetectFightingStatusAccuracy
—PP
8Prevents moves from affecting the user this turn.
Diamond StormRockPhysicalPower
100Accuracy
95%PP
850% chance to raise user's Defense by 2.
Dire ClawPoisonPhysicalPower
80Accuracy
100%PP
2450% chance to sleep, poison, or paralyze target.
DisableNormalStatusAccuracy
100%PP
32For 4 turns, disables the target's last move used.
DischargeElectricSpecialPower
80Accuracy
100%PP
2430% chance to paralyze adjacent Pokemon.
Doom DesireSteelSpecialPower
140Accuracy
100%PP
8Hits two turns after being used.
Double-EdgeNormalPhysicalPower
120Accuracy
100%PP
24Has 33% recoil.
Double Iron BashSteelPhysicalPower
60Accuracy
100%PP
8Hits twice. 30% chance to make the target flinch.
Double ShockElectricPhysicalPower
120Accuracy
100%PP
8User's Electric type: typeless; must be Electric.
Draco MeteorDragonSpecialPower
130Accuracy
90%PP
8Lowers the user's Sp. Atk by 2.
Dragon AscentFlyingPhysicalPower
120Accuracy
100%PP
8Lowers the user's Defense and Sp. Def by 1.
Dragon ClawDragonPhysicalPower
80Accuracy
100%PP
24No additional effect.
Dragon DanceDragonStatusAccuracy
—PP
32Raises the user's Attack and Speed by 1.
Dragon DartsDragonPhysicalPower
50Accuracy
100%PP
16Hits twice. Doubles: Tries to hit each foe once.
Dragon EnergyDragonSpecialPower
150Accuracy
100%PP
8Less power as user's HP decreases. Hits foe(s).
Dragon HammerDragonPhysicalPower
90Accuracy
100%PP
24No additional effect.
Dragon PulseDragonSpecialPower
85Accuracy
100%PP
16No additional effect.
Dragon TailDragonPhysicalPower
60Accuracy
90%PP
16Forces the target to switch to a random ally.
Draining KissFairySpecialPower
50Accuracy
100%PP
16User recovers 75% of the damage dealt.
Drain PunchFightingPhysicalPower
75Accuracy
100%PP
16User recovers 50% of the damage dealt.
Drill PeckFlyingPhysicalPower
80Accuracy
100%PP
32No additional effect.
Drill RunGroundPhysicalPower
80Accuracy
95%PP
16High critical hit ratio.
Drum BeatingGrassPhysicalPower
80Accuracy
100%PP
16100% chance to lower the target's Speed by 1.
Dynamax CannonDragonSpecialPower
100Accuracy
100%PP
8No additional effect.
Earth PowerGroundSpecialPower
90Accuracy
100%PP
1610% chance to lower the target's Sp. Def by 1.
EarthquakeGroundPhysicalPower
100Accuracy
100%PP
16Hits adjacent Pokemon. Double damage on Dig.
Eerie SpellPsychicSpecialPower
80Accuracy
100%PP
8Removes 3 PP from the target's last move.
Electro DriftElectricSpecialPower
100Accuracy
100%PP
8Deals 1.3333x damage with supereffective hits.
EncoreNormalStatusAccuracy
100%PP
8Target repeats its last move for its next 3 turns.
EndeavorNormalPhysicalPower
—Accuracy
100%PP
8Lowers the target's HP to the user's HP.
Energy BallGrassSpecialPower
90Accuracy
100%PP
1610% chance to lower the target's Sp. Def by 1.
EruptionFireSpecialPower
150Accuracy
100%PP
8Less power as user's HP decreases. Hits foe(s).
Esper WingPsychicSpecialPower
80Accuracy
100%PP
16100% chance to raise user Speed by 1. High crit.
Expanding ForcePsychicSpecialPower
80Accuracy
100%PP
16User on Psychic Terrain: 1.5x power, hits foes.
ExplosionNormalPhysicalPower
250Accuracy
100%PP
8Hits adjacent Pokemon. The user faints.
ExtrasensoryPsychicSpecialPower
80Accuracy
100%PP
3210% chance to make the target flinch.
Extreme SpeedNormalPhysicalPower
80Accuracy
100%PP
8Nearly always goes first.
FacadeNormalPhysicalPower
70Accuracy
100%PP
32Power doubles if user is burn/poison/paralyzed.
Fake OutNormalPhysicalPower
40Accuracy
100%PP
16Hits first. First turn out only. 100% flinch chance.
False SurrenderDarkPhysicalPower
80Accuracy
—PP
16This move does not check accuracy.
Fickle BeamDragonSpecialPower
80Accuracy
100%PP
8Has a 30% chance this move's power is doubled.
Fiery DanceFireSpecialPower
80Accuracy
100%PP
1650% chance to raise the user's Sp. Atk by 1.
Fiery WrathDarkSpecialPower
90Accuracy
100%PP
1620% chance to make the foe(s) flinch.
Fillet AwayNormalStatusAccuracy
—PP
16+2 Attack, Sp. Atk, Speed for 1/2 user's max HP.
Fire BlastFireSpecialPower
110Accuracy
85%PP
810% chance to burn the target.
Fire FangFirePhysicalPower
65Accuracy
95%PP
2410% chance to burn. 10% chance to flinch.
Fire LashFirePhysicalPower
80Accuracy
100%PP
24100% chance to lower the target's Defense by 1.
Fire PunchFirePhysicalPower
75Accuracy
100%PP
2410% chance to burn the target.
First ImpressionBugPhysicalPower
90Accuracy
100%PP
16Hits first. First turn out only.
Fishious RendWaterPhysicalPower
85Accuracy
100%PP
16Power doubles if user moves before the target.
Flame ChargeFirePhysicalPower
50Accuracy
100%PP
32100% chance to raise the user's Speed by 1.
FlamethrowerFireSpecialPower
90Accuracy
100%PP
2410% chance to burn the target.
Flare BlitzFirePhysicalPower
120Accuracy
100%PP
24Has 33% recoil. 10% chance to burn. Thaws user.
Flash CannonSteelSpecialPower
80Accuracy
100%PP
1610% chance to lower the target's Sp. Def by 1.
Fleur CannonFairySpecialPower
130Accuracy
90%PP
8Lowers the user's Sp. Atk by 2.
Flip TurnWaterPhysicalPower
60Accuracy
100%PP
32User switches out after damaging the target.
Flower TrickGrassPhysicalPower
70Accuracy
—PP
16Always results in a critical hit; no accuracy check.
Focus BlastFightingSpecialPower
120Accuracy
70%PP
810% chance to lower the target's Sp. Def by 1.
Focus PunchFightingPhysicalPower
150Accuracy
100%PP
32Fails if the user takes damage before it hits.
Foul PlayDarkPhysicalPower
95Accuracy
100%PP
24Uses target's Attack stat in damage calculation.
Freeze-DryIceSpecialPower
70Accuracy
100%PP
3210% chance to freeze. Super effective on Water.
Freezing GlarePsychicSpecialPower
90Accuracy
100%PP
1610% chance to freeze the target.
FrustrationNormalPhysicalPower
—Accuracy
100%PP
32Max 102 power at minimum Happiness.
Fusion BoltElectricPhysicalPower
100Accuracy
100%PP
8Power doubles if used after Fusion Flare this turn.
Fusion FlareFireSpecialPower
100Accuracy
100%PP
8Power doubles if used after Fusion Bolt this turn.
Future SightPsychicSpecialPower
120Accuracy
100%PP
16Hits two turns after being used.
Gear GrindSteelPhysicalPower
50Accuracy
85%PP
24Hits 2 times in one turn.
GeomancyFairyStatusAccuracy
—PP
16Charges, then raises SpA, SpD, Spe by 2 turn 2.
Giga DrainGrassSpecialPower
75Accuracy
100%PP
16User recovers 50% of the damage dealt.
Gigaton HammerSteelPhysicalPower
160Accuracy
100%PP
8Cannot be selected the turn after it's used.
Glacial LanceIcePhysicalPower
120Accuracy
100%PP
8No additional effect. Hits adjacent foes.
Glaive RushDragonPhysicalPower
120Accuracy
100%PP
8User takes sure-hit 2x damage until its next turn.
GlareNormalStatusAccuracy
100%PP
48Paralyzes the target.
Grass KnotGrassSpecialPower
—Accuracy
100%PP
32More power the heavier the target.
Grav AppleGrassPhysicalPower
80Accuracy
100%PP
16Target: 100% -1 Def. During Gravity: 1.5x power.
Gunk ShotPoisonPhysicalPower
120Accuracy
80%PP
830% chance to poison the target.
Hammer ArmFightingPhysicalPower
100Accuracy
90%PP
16Lowers the user's Speed by 1.
HazeIceStatusAccuracy
—PP
48Eliminates all stat changes.
Head ChargeNormalPhysicalPower
120Accuracy
100%PP
24Has 1/4 recoil.
Headlong RushGroundPhysicalPower
120Accuracy
100%PP
8Lowers the user's Defense and Sp. Def by 1.
Head SmashRockPhysicalPower
150Accuracy
80%PP
8Has 1/2 recoil.
Heal BellNormalStatusAccuracy
—PP
8Cures the user's party of all status conditions.
Healing WishPsychicStatusAccuracy
—PP
16User faints. Next hurt Pokemon is fully healed.
Heal OrderBugStatusAccuracy
—PP
16Heals the user by 50% of its max HP.
Heart SwapPsychicStatusAccuracy
—PP
16Swaps all stat changes with target.
Heat WaveFireSpecialPower
95Accuracy
90%PP
1610% chance to burn the foe(s).
High HorsepowerGroundPhysicalPower
95Accuracy
95%PP
16No additional effect.
High Jump KickFightingPhysicalPower
130Accuracy
90%PP
16User is hurt by 50% of its max HP if it misses.
Hone ClawsDarkStatusAccuracy
—PP
24Raises the user's Attack and accuracy by 1.
Horn LeechGrassPhysicalPower
75Accuracy
100%PP
16User recovers 50% of the damage dealt.
HurricaneFlyingSpecialPower
110Accuracy
70%PP
1630% chance to confuse target. Can't miss in rain.
Hydro PumpWaterSpecialPower
110Accuracy
80%PP
8No additional effect.
Hydro SteamWaterSpecialPower
80Accuracy
100%PP
24During Sunny Day: 1.5x damage instead of half.
Hyper DrillNormalPhysicalPower
100Accuracy
100%PP
8Bypasses protection without breaking it.
Hyper VoiceNormalSpecialPower
90Accuracy
100%PP
16No additional effect. Hits adjacent foes.
Ice BeamIceSpecialPower
90Accuracy
100%PP
1610% chance to freeze the target.
Ice FangIcePhysicalPower
65Accuracy
95%PP
2410% chance to freeze. 10% chance to flinch.
Ice HammerIcePhysicalPower
100Accuracy
90%PP
16Lowers the user's Speed by 1.
Ice ShardIcePhysicalPower
40Accuracy
100%PP
48Usually goes first.
Ice SpinnerIcePhysicalPower
80Accuracy
100%PP
24Ends the effects of terrain.
Icicle SpearIcePhysicalPower
25Accuracy
100%PP
48Hits 2-5 times in one turn.
Infernal ParadeGhostSpecialPower
60Accuracy
100%PP
2430% burn. 2x power if target is already statused.
InfestationBugSpecialPower
20Accuracy
100%PP
32Traps and damages the target for 4-5 turns.
Iron HeadSteelPhysicalPower
80Accuracy
100%PP
2430% chance to make the target flinch.
Ivy CudgelGrassPhysicalPower
100Accuracy
100%PP
16High critical hit ratio. Type depends on user's form.
JudgmentNormalSpecialPower
100Accuracy
100%PP
16Type varies based on the held Plate.
King's ShieldSteelStatusAccuracy
—PP
16Protects from damaging attacks. Contact: -1 Atk.
Knock OffDarkPhysicalPower
65Accuracy
100%PP
321.5x damage if foe holds an item. Removes item.
Kowtow CleaveDarkPhysicalPower
85Accuracy
—PP
16This move does not check accuracy.
Lash OutDarkPhysicalPower
75Accuracy
100%PP
82x power if the user had a stat lowered this turn.
Last ResortNormalPhysicalPower
140Accuracy
100%PP
8Fails unless each known move has been used.
Last RespectsGhostPhysicalPower
50Accuracy
100%PP
16+50 power for each time a party member fainted.
Lava PlumeFireSpecialPower
80Accuracy
100%PP
2430% chance to burn adjacent Pokemon.
Leaf BladeGrassPhysicalPower
90Accuracy
100%PP
24High critical hit ratio.
Leaf StormGrassSpecialPower
130Accuracy
90%PP
8Lowers the user's Sp. Atk by 2.
Leech LifeBugPhysicalPower
80Accuracy
100%PP
16User recovers 50% of the damage dealt.
Leech SeedGrassStatusAccuracy
90%PP
161/8 of target's HP is restored to user every turn.
Light of RuinFairySpecialPower
140Accuracy
90%PP
8Has 1/2 recoil.
Light ScreenPsychicStatusAccuracy
—PP
48For 5 turns, special damage to allies is halved.
LiquidationWaterPhysicalPower
85Accuracy
100%PP
1620% chance to lower the target's Defense by 1.
Lovely KissNormalStatusAccuracy
75%PP
16Causes the target to fall asleep.
Low KickFightingPhysicalPower
—Accuracy
100%PP
32More power the heavier the target.
Lumina CrashPsychicSpecialPower
80Accuracy
100%PP
16100% chance to lower the target's Sp. Def by 2.
Lunar DancePsychicStatusAccuracy
—PP
16User faints. Next hurt Pkmn is cured, max HP/PP.
LungeBugPhysicalPower
80Accuracy
100%PP
24100% chance to lower the target's Attack by 1.
Luster PurgePsychicSpecialPower
95Accuracy
100%PP
850% chance to lower the target's Sp. Def by 1.
Mach PunchFightingPhysicalPower
40Accuracy
100%PP
48Usually goes first.
Magic CoatPsychicStatusAccuracy
—PP
24Bounces back certain non-damaging moves.
Magma StormFireSpecialPower
100Accuracy
75%PP
8Traps and damages the target for 4-5 turns.
Make It RainSteelSpecialPower
120Accuracy
100%PP
8Lowers the user's Sp. Atk by 1. Hits foe(s).
Malignant ChainPoisonSpecialPower
100Accuracy
100%PP
850% chance to badly poison the target.
Matcha GotchaGrassSpecialPower
80Accuracy
90%PP
2420% burn. Recovers 50% dmg dealt. Thaws foe(s).
MegahornBugPhysicalPower
120Accuracy
85%PP
16No additional effect.
MementoDarkStatusAccuracy
100%PP
16Lowers target's Attack, Sp. Atk by 2. User faints.
Meteor MashSteelPhysicalPower
90Accuracy
90%PP
1620% chance to raise the user's Attack by 1.
Mighty CleaveRockPhysicalPower
95Accuracy
100%PP
8Bypasses protection without breaking it.
Milk DrinkNormalStatusAccuracy
—PP
8Heals the user by 50% of its max HP.
Mind BlownFireSpecialPower
150Accuracy
100%PP
8User loses 50% max HP. Hits adjacent Pokemon.
Mist BallPsychicSpecialPower
95Accuracy
100%PP
850% chance to lower the target's Sp. Atk by 1.
MoonblastFairySpecialPower
95Accuracy
100%PP
2430% chance to lower the target's Sp. Atk by 1.
Moongeist BeamGhostSpecialPower
100Accuracy
100%PP
8Ignores the Abilities of other Pokemon.
MoonlightFairyStatusAccuracy
—PP
8Heals the user by a weather-dependent amount.
Morning SunNormalStatusAccuracy
—PP
8Heals the user by a weather-dependent amount.
Mortal SpinPoisonPhysicalPower
30Accuracy
100%PP
24Poisons foes, frees user from hazards/bind/leech.
Mountain GaleIcePhysicalPower
100Accuracy
85%PP
1630% chance to make the target flinch.
Multi-AttackNormalPhysicalPower
120Accuracy
100%PP
16Type varies based on the held Memory.
Mystical PowerPsychicSpecialPower
70Accuracy
90%PP
16100% chance to raise the user's Sp. Atk by 1.
Nasty PlotDarkStatusAccuracy
—PP
32Raises the user's Sp. Atk by 2.
Nature's MadnessFairySpecialPower
—Accuracy
90%PP
16Does damage equal to 1/2 target's current HP.
Night ShadeGhostSpecialPower
—Accuracy
100%PP
24Does damage equal to the user's level.
No RetreatFightingStatusAccuracy
—PP
8Raises all stats by 1 (not acc/eva). Traps user.
NuzzleElectricPhysicalPower
20Accuracy
100%PP
32100% chance to paralyze the target.
Oblivion WingFlyingSpecialPower
80Accuracy
100%PP
16User recovers 75% of the damage dealt.
ObstructDarkStatusAccuracy
100%PP
16Protects from damaging attacks. Contact: -2 Def.
Order UpDragonPhysicalPower
80Accuracy
100%PP
16Curly|Droopy|Stretchy eaten: +1 Atk|Def|Spe.
Origin PulseWaterSpecialPower
110Accuracy
85%PP
16No additional effect. Hits adjacent foes.
OverdriveElectricSpecialPower
80Accuracy
100%PP
16No additional effect. Hits foe(s).
OverheatFireSpecialPower
130Accuracy
90%PP
8Lowers the user's Sp. Atk by 2.
Pain SplitNormalStatusAccuracy
—PP
32Shares HP of user and target equally.
Parting ShotDarkStatusAccuracy
100%PP
32Lowers target's Atk, Sp. Atk by 1. User switches.
Perish SongNormalStatusAccuracy
—PP
8All active Pokemon will faint in 3 turns.
Petal BlizzardGrassPhysicalPower
90Accuracy
100%PP
24No additional effect. Hits adjacent Pokemon.
Petal DanceGrassSpecialPower
120Accuracy
100%PP
16Lasts 2-3 turns. Confuses the user afterwards.
Photon GeyserPsychicSpecialPower
100Accuracy
100%PP
8Physical if user's Atk > Sp. Atk. Ignores Abilities.
Plasma FistsElectricPhysicalPower
100Accuracy
100%PP
24Normal moves become Electric type this turn.
Play RoughFairyPhysicalPower
90Accuracy
90%PP
1610% chance to lower the target's Attack by 1.
Poison JabPoisonPhysicalPower
80Accuracy
100%PP
3230% chance to poison the target.
PoltergeistGhostPhysicalPower
110Accuracy
90%PP
8Fails if the target has no held item.
Population BombNormalPhysicalPower
20Accuracy
90%PP
16Hits 10 times. Each hit can miss.
Power GemRockSpecialPower
80Accuracy
100%PP
32No additional effect.
Power-Up PunchFightingPhysicalPower
40Accuracy
100%PP
32100% chance to raise the user's Attack by 1.
Power WhipGrassPhysicalPower
120Accuracy
85%PP
16No additional effect.
Precipice BladesGroundPhysicalPower
120Accuracy
85%PP
16No additional effect. Hits adjacent foes.
ProtectNormalStatusAccuracy
—PP
16Prevents moves from affecting the user this turn.
PsybladePsychicPhysicalPower
80Accuracy
100%PP
24During Electric Terrain: 1.5x power.
PsychicPsychicSpecialPower
90Accuracy
100%PP
1610% chance to lower the target's Sp. Def by 1.
Psychic FangsPsychicPhysicalPower
85Accuracy
100%PP
16Destroys screens, unless the target is immune.
Psychic NoisePsychicSpecialPower
75Accuracy
100%PP
16For 2 turns, the target is prevented from healing.
Psycho BoostPsychicSpecialPower
140Accuracy
90%PP
8Lowers the user's Sp. Atk by 2.
Psycho CutPsychicPhysicalPower
70Accuracy
100%PP
32High critical hit ratio.
Psyshield BashPsychicPhysicalPower
70Accuracy
90%PP
16100% chance to raise the user's Defense by 1.
PsyshockPsychicSpecialPower
80Accuracy
100%PP
16Damages target based on Defense, not Sp. Def.
PsystrikePsychicSpecialPower
100Accuracy
100%PP
16Damages target based on Defense, not Sp. Def.
PursuitDarkPhysicalPower
40Accuracy
100%PP
32If a foe is switching out, hits it at 2x power.
Pyro BallFirePhysicalPower
120Accuracy
90%PP
810% chance to burn the target. Thaws user.
Quick AttackNormalPhysicalPower
40Accuracy
100%PP
48Usually goes first.
Quiver DanceBugStatusAccuracy
—PP
32Raises the user's Sp. Atk, Sp. Def, Speed by 1.
Rage FistGhostPhysicalPower
50Accuracy
100%PP
16+50 power for each time user was hit. Max 6 hits.
Raging BullNormalPhysicalPower
90Accuracy
100%PP
16Destroys screens. Type depends on user's form.
Raging FuryFirePhysicalPower
120Accuracy
100%PP
16Lasts 2-3 turns. Confuses the user afterwards.
Rapid SpinNormalPhysicalPower
50Accuracy
100%PP
64Free user from hazards/bind/Leech Seed; +1 Spe.
Razor ShellWaterPhysicalPower
75Accuracy
95%PP
1650% chance to lower the target's Defense by 1.
RecoverNormalStatusAccuracy
—PP
8Heals the user by 50% of its max HP.
ReflectPsychicStatusAccuracy
—PP
32For 5 turns, physical damage to allies is halved.
Reflect TypeNormalStatusAccuracy
—PP
24User becomes the same type as the target.
RestPsychicStatusAccuracy
—PP
8User sleeps 2 turns and restores HP and status.
ReturnNormalPhysicalPower
—Accuracy
100%PP
32Max 102 power at maximum Happiness.
Revelation DanceNormalSpecialPower
90Accuracy
100%PP
24Type varies based on the user's primary type.
RoarNormalStatusAccuracy
—PP
32Forces the target to switch to a random ally.
Rock BlastRockPhysicalPower
25Accuracy
90%PP
16Hits 2-5 times in one turn.
Rock PolishRockStatusAccuracy
—PP
32Raises the user's Speed by 2.
Rock SlideRockPhysicalPower
75Accuracy
90%PP
1630% chance to make the foe(s) flinch.
RoostFlyingStatusAccuracy
—PP
8Heals 50% HP. Flying-type removed 'til turn ends.
RuinationDarkSpecialPower
—Accuracy
90%PP
16Does damage equal to 1/2 target's current HP.
Sacred FireFirePhysicalPower
100Accuracy
95%PP
850% chance to burn the target. Thaws user.
Sacred SwordFightingPhysicalPower
90Accuracy
100%PP
24Ignores the target's stat stage changes.
Salt CureRockPhysicalPower
40Accuracy
100%PP
24Deals 1/8 max HP each turn; 1/4 on Steel, Water.
Sandsear StormGroundSpecialPower
100Accuracy
80%PP
1620% chance to burn foe(s). Can't miss in rain.
ScaldWaterSpecialPower
80Accuracy
100%PP
2430% chance to burn the target. Thaws target.
Scorching SandsGroundSpecialPower
70Accuracy
100%PP
1630% chance to burn the target. Thaws target.
Searing ShotFireSpecialPower
100Accuracy
100%PP
830% chance to burn adjacent Pokemon.
Secret SwordFightingSpecialPower
85Accuracy
100%PP
16Damages target based on Defense, not Sp. Def.
Seed BombGrassPhysicalPower
80Accuracy
100%PP
24No additional effect.
Seed FlareGrassSpecialPower
120Accuracy
85%PP
840% chance to lower the target's Sp. Def by 2.
Seismic TossFightingPhysicalPower
—Accuracy
100%PP
32Does damage equal to the user's level.
Shadow BallGhostSpecialPower
80Accuracy
100%PP
2420% chance to lower the target's Sp. Def by 1.
Shadow BoneGhostPhysicalPower
85Accuracy
100%PP
1620% chance to lower the target's Defense by 1.
Shadow ClawGhostPhysicalPower
70Accuracy
100%PP
24High critical hit ratio.
Shadow SneakGhostPhysicalPower
40Accuracy
100%PP
48Usually goes first.
Shed TailNormalStatusAccuracy
—PP
16User takes 1/2 its max HP to pass a substitute.
Shell Side ArmPoisonSpecialPower
90Accuracy
100%PP
1620% psn. Physical+contact if it would be stronger.
Shell SmashNormalStatusAccuracy
—PP
24Lowers Def, SpD by 1; raises Atk, SpA, Spe by 2.
Shift GearSteelStatusAccuracy
—PP
16Raises the user's Speed by 2 and Attack by 1.
Shore UpGroundStatusAccuracy
—PP
8User restores 1/2 its max HP; 2/3 in Sandstorm.
Signal BeamBugSpecialPower
75Accuracy
100%PP
2410% chance to confuse the target.
Silk TrapBugStatusAccuracy
—PP
16Protects from damaging attacks. Contact: -1 Spe.
Slack OffNormalStatusAccuracy
—PP
8Heals the user by 50% of its max HP.
Sleep PowderGrassStatusAccuracy
75%PP
24Causes the target to fall asleep.
Sleep TalkNormalStatusAccuracy
—PP
16User must be asleep. Uses another known move.
Sludge BombPoisonSpecialPower
90Accuracy
100%PP
1630% chance to poison the target.
Sludge WavePoisonSpecialPower
95Accuracy
100%PP
1610% chance to poison adjacent Pokemon.
Snipe ShotWaterSpecialPower
80Accuracy
100%PP
24High critical hit ratio. Cannot be redirected.
Soft-BoiledNormalStatusAccuracy
—PP
8Heals the user by 50% of its max HP.
Spacial RendDragonSpecialPower
100Accuracy
95%PP
8High critical hit ratio.
Sparkling AriaWaterSpecialPower
90Accuracy
100%PP
16The target is cured of its burn.
Spectral ThiefGhostPhysicalPower
90Accuracy
100%PP
16Steals target's boosts before dealing damage.
SpikesGroundStatusAccuracy
—PP
32Hurts grounded foes on switch-in. Max 3 layers.
Spiky ShieldGrassStatusAccuracy
—PP
16Protects from moves. Contact: loses 1/8 max HP.
Spin OutSteelPhysicalPower
100Accuracy
100%PP
8Lowers the user's Speed by 2.
Spirit BreakFairyPhysicalPower
75Accuracy
100%PP
24100% chance to lower the target's Sp. Atk by 1.
Spirit ShackleGhostPhysicalPower
80Accuracy
100%PP
16Prevents the target from switching out.
SporeGrassStatusAccuracy
100%PP
24Causes the target to fall asleep.
Springtide StormFairySpecialPower
100Accuracy
80%PP
830% chance to lower the foe(s) Attack by 1.
Stealth RockRockStatusAccuracy
—PP
32Hurts foes on switch-in. Factors Rock weakness.
Steam EruptionWaterSpecialPower
110Accuracy
95%PP
830% chance to burn the target. Thaws target.
Steel BeamSteelSpecialPower
140Accuracy
95%PP
8User loses 50% max HP.
Steel RollerSteelPhysicalPower
130Accuracy
100%PP
8Fails if there is no terrain active. Ends the terrain.
Sticky WebBugStatusAccuracy
—PP
32Lowers Speed of grounded foes by 1 on switch-in.
Stone AxeRockPhysicalPower
65Accuracy
90%PP
24Sets Stealth Rock on the target's side.
Stone EdgeRockPhysicalPower
100Accuracy
80%PP
8High critical hit ratio.
Stored PowerPsychicSpecialPower
20Accuracy
100%PP
16+ 20 power for each of the user's stat boosts.
Storm ThrowFightingPhysicalPower
60Accuracy
100%PP
16Always results in a critical hit.
Strange SteamFairySpecialPower
90Accuracy
95%PP
1620% chance to confuse the target.
Strength SapGrassStatusAccuracy
100%PP
16User heals HP=target's Atk stat. Lowers Atk by 1.
SubstituteNormalStatusAccuracy
—PP
16User takes 1/4 its max HP to put in a substitute.
Sucker PunchDarkPhysicalPower
70Accuracy
100%PP
8Usually goes first. Fails if target is not attacking.
Sunsteel StrikeSteelPhysicalPower
100Accuracy
100%PP
8Ignores the Abilities of other Pokemon.
Supercell SlamElectricPhysicalPower
100Accuracy
95%PP
24User is hurt by 50% of its max HP if it misses.
Super FangNormalPhysicalPower
—Accuracy
90%PP
16Does damage equal to 1/2 target's current HP.
SuperpowerFightingPhysicalPower
120Accuracy
100%PP
8Lowers the user's Attack and Defense by 1.
SurfWaterSpecialPower
90Accuracy
100%PP
24Hits adjacent Pokemon. Double damage on Dive.
Surging StrikesWaterPhysicalPower
25Accuracy
100%PP
8Always results in a critical hit. Hits 3 times.
SwitcherooDarkStatusAccuracy
100%PP
16User switches its held item with the target's.
Swords DanceNormalStatusAccuracy
—PP
32Raises the user's Attack by 2.
SynthesisGrassStatusAccuracy
—PP
8Heals the user by a weather-dependent amount.
Tail GlowBugStatusAccuracy
—PP
32Raises the user's Sp. Atk by 3.
Tail SlapNormalPhysicalPower
25Accuracy
85%PP
16Hits 2-5 times in one turn.
TailwindFlyingStatusAccuracy
—PP
24For 4 turns, allies' Speed is doubled.
TauntDarkStatusAccuracy
100%PP
32Target can't use status moves its next 3 turns.
TeleportPsychicStatusAccuracy
—PP
32User switches out.
Temper FlareFirePhysicalPower
75Accuracy
100%PP
16Power doubles if the user's last move failed.
Tera BlastNormalSpecialPower
80Accuracy
100%PP
16If Terastallized: Phys. if Atk > SpA, type = Tera.
Thousand ArrowsGroundPhysicalPower
90Accuracy
100%PP
16Grounds adjacent foes. First hit neutral on Flying.
Thousand WavesGroundPhysicalPower
90Accuracy
100%PP
16Hits adjacent foes. Prevents them from switching.
Throat ChopDarkPhysicalPower
80Accuracy
100%PP
24For 2 turns, the target cannot use sound moves.
ThunderElectricSpecialPower
110Accuracy
70%PP
1630% chance to paralyze. Can't miss in rain.
ThunderboltElectricSpecialPower
90Accuracy
100%PP
2410% chance to paralyze the target.
Thunder CageElectricSpecialPower
80Accuracy
90%PP
24Traps and damages the target for 4-5 turns.
Thunderous KickFightingPhysicalPower
90Accuracy
100%PP
16100% chance to lower the target's Defense by 1.
Thunder PunchElectricPhysicalPower
75Accuracy
100%PP
2410% chance to paralyze the target.
Thunder WaveElectricStatusAccuracy
90%PP
32Paralyzes the target.
Tidy UpNormalStatusAccuracy
—PP
16User +1 Atk, Spe. Clears all substitutes/hazards.
Torch SongFireSpecialPower
80Accuracy
100%PP
16100% chance to raise the user's Sp. Atk by 1.
ToxicPoisonStatusAccuracy
90%PP
16Badly poisons the target. Poison types can't miss.
Toxic SpikesPoisonStatusAccuracy
—PP
32Poisons grounded foes on switch-in. Max 2 layers.
TrailblazeGrassPhysicalPower
50Accuracy
100%PP
32100% chance to raise the user's Speed by 1.
TransformNormalStatusAccuracy
—PP
16Copies target's stats, moves, types, and Ability.
Tri AttackNormalSpecialPower
80Accuracy
100%PP
1620% chance to paralyze or burn or freeze target.
TrickPsychicStatusAccuracy
100%PP
16User switches its held item with the target's.
Trick RoomPsychicStatusAccuracy
—PP
8Goes last. For 5 turns, turn order is reversed.
Triple ArrowsFightingPhysicalPower
90Accuracy
100%PP
16High crit. Target: 50% -1 Defense, 30% flinch.
Triple AxelIcePhysicalPower
20Accuracy
90%PP
16Hits 3 times. Each hit can miss, but power rises.
Triple DiveWaterPhysicalPower
30Accuracy
95%PP
16Hits 3 times.
Twin BeamPsychicSpecialPower
40Accuracy
100%PP
16Hits 2 times in one turn.
U-turnBugPhysicalPower
70Accuracy
100%PP
32User switches out after damaging the target.
Victory DanceFightingStatusAccuracy
—PP
16Raises the user's Attack, Defense, Speed by 1.
Volt SwitchElectricSpecialPower
70Accuracy
100%PP
32User switches out after damaging the target.
Volt TackleElectricPhysicalPower
120Accuracy
100%PP
24Has 33% recoil. 10% chance to paralyze target.
WaterfallWaterPhysicalPower
80Accuracy
100%PP
2420% chance to make the target flinch.
Water ShurikenWaterSpecialPower
15Accuracy
100%PP
32Usually goes first. Hits 2-5 times in one turn.
Water SpoutWaterSpecialPower
150Accuracy
100%PP
8Less power as user's HP decreases. Hits foe(s).
Wave CrashWaterPhysicalPower
120Accuracy
100%PP
16Has 33% recoil.
Weather BallNormalSpecialPower
50Accuracy
100%PP
16Power doubles and type varies in each weather.
WhirlwindNormalStatusAccuracy
—PP
32Forces the target to switch to a random ally.
Wicked BlowDarkPhysicalPower
75Accuracy
100%PP
8Always results in a critical hit.
Wildbolt StormElectricSpecialPower
100Accuracy
80%PP
1620% chance to paralyze foe(s). Rain: can't miss.
Wild ChargeElectricPhysicalPower
90Accuracy
100%PP
24Has 1/4 recoil.
Will-O-WispFireStatusAccuracy
85%PP
24Burns the target.
WishNormalStatusAccuracy
—PP
16Next turn, 50% of the user's max HP is restored.
Wood HammerGrassPhysicalPower
120Accuracy
100%PP
24Has 33% recoil.
X-ScissorBugPhysicalPower
80Accuracy
100%PP
24No additional effect.
YawnNormalStatusAccuracy
—PP
16Puts the target to sleep after 1 turn.
Zen HeadbuttPsychicPhysicalPower
80Accuracy
90%PP
2420% chance to make the target flinch.
Zing ZapElectricPhysicalPower
80Accuracy
100%PP
1630% chance to make the target flinch.
CaptivateNormalStatusAccuracy
100%PP
32Lowers the foe(s) Sp. Atk by 2 if opposite gender.
False SwipeNormalPhysicalPower
40Accuracy
100%PP
64Always leaves the target with at least 1 HP.
Fury SwipesNormalPhysicalPower
18Accuracy
80%PP
24Hits 2-5 times in one turn.
Mean LookNormalStatusAccuracy
—PP
8Prevents the target from switching out.
Odor SleuthNormalStatusAccuracy
—PP
64Fighting, Normal hit Ghost. Evasiveness ignored.
SketchNormalStatusAccuracy
—PP
1Permanently copies the last move target used.
AbsorbGrassSpecialPower
20Accuracy
100%PP
40User recovers 50% of the damage dealt.
AcidPoisonSpecialPower
40Accuracy
100%PP
4810% chance to lower the foe(s) Sp. Def by 1.
Acid SprayPoisonSpecialPower
40Accuracy
100%PP
32100% chance to lower the target's Sp. Def by 2.
AcupressureNormalStatusAccuracy
—PP
48Raises a random stat of the user or an ally by 2.
Aerial AceFlyingPhysicalPower
60Accuracy
—PP
32This move does not check accuracy.
After YouNormalStatusAccuracy
—PP
24The target makes its move right after the user.
Air CutterFlyingSpecialPower
60Accuracy
95%PP
40High critical hit ratio. Hits adjacent foes.
Ally SwitchPsychicStatusAccuracy
—PP
24User and ally swap positions; using again can fail.
AmnesiaPsychicStatusAccuracy
—PP
32Raises the user's Sp. Def by 2.
Ancient PowerRockSpecialPower
60Accuracy
100%PP
810% chance to raise all stats by 1 (not acc/eva).
Aqua JetWaterPhysicalPower
40Accuracy
100%PP
32Usually goes first.
Aqua RingWaterStatusAccuracy
—PP
32User recovers 1/16 max HP per turn.
Arm ThrustFightingPhysicalPower
15Accuracy
100%PP
32Hits 2-5 times in one turn.
Aromatic MistFairyStatusAccuracy
—PP
32Raises an ally's Sp. Def by 1.
AssistNormalStatusAccuracy
—PP
32Uses a random move known by a team member.
AssuranceDarkPhysicalPower
60Accuracy
100%PP
16Power doubles if target was damaged this turn.
AstonishGhostPhysicalPower
30Accuracy
100%PP
2430% chance to make the target flinch.
AttractNormalStatusAccuracy
100%PP
24A target of the opposite gender gets infatuated.
Aura WheelElectricPhysicalPower
110Accuracy
100%PP
16Morpeko: Electric; Hangry: Dark; 100% +1 Spe.
Aurora BeamIceSpecialPower
65Accuracy
100%PP
3210% chance to lower the target's Attack by 1.
Axe KickFightingPhysicalPower
120Accuracy
90%PP
1630% confusion. User loses 50% max HP if miss.
Baby-Doll EyesFairyStatusAccuracy
100%PP
48Lowers the target's Attack by 1.
BarrageNormalPhysicalPower
15Accuracy
85%PP
32Hits 2-5 times in one turn.
BarrierPsychicStatusAccuracy
—PP
32Raises the user's Defense by 2.
Beat UpDarkPhysicalPower
—Accuracy
100%PP
16All healthy allies aid in damaging the target.
BelchPoisonSpecialPower
120Accuracy
90%PP
16Cannot be selected until the user eats a Berry.
BestowNormalStatusAccuracy
—PP
24User passes its held item to the target.
BideNormalPhysicalPower
—Accuracy
—PP
16Waits 2 turns; deals double the damage taken.
BindNormalPhysicalPower
15Accuracy
85%PP
32Traps and damages the target for 4-5 turns.
BiteDarkPhysicalPower
60Accuracy
100%PP
4030% chance to make the target flinch.
Blast BurnFireSpecialPower
150Accuracy
90%PP
8User cannot move next turn.
BlockNormalStatusAccuracy
—PP
8Prevents the target from switching out.
Bone ClubGroundPhysicalPower
65Accuracy
85%PP
3210% chance to make the target flinch.
Bone RushGroundPhysicalPower
25Accuracy
90%PP
16Hits 2-5 times in one turn.
BounceFlyingPhysicalPower
85Accuracy
85%PP
8Bounces turn 1. Hits turn 2. 30% paralyze.
Branch PokeGrassPhysicalPower
40Accuracy
100%PP
64No additional effect.
Breaking SwipeDragonPhysicalPower
60Accuracy
100%PP
24100% chance to lower the foe(s) Attack by 1.
BrineWaterSpecialPower
65Accuracy
100%PP
16Power doubles if the target's HP is 50% or less.
Brutal SwingDarkPhysicalPower
60Accuracy
100%PP
32No additional effect. Hits adjacent Pokemon.
BubbleWaterSpecialPower
40Accuracy
100%PP
4810% chance to lower the foe(s) Speed by 1.
Bubble BeamWaterSpecialPower
65Accuracy
100%PP
3210% chance to lower the target's Speed by 1.
Bug BiteBugPhysicalPower
60Accuracy
100%PP
32User steals and eats the target's Berry.
BulldozeGroundPhysicalPower
60Accuracy
100%PP
32100% chance lower adjacent Pkmn Speed by 1.
Bullet SeedGrassPhysicalPower
25Accuracy
100%PP
48Hits 2-5 times in one turn.
Burning BulwarkFireStatusAccuracy
—PP
16Protects from damaging attacks. Contact: burn.
Burning JealousyFireSpecialPower
70Accuracy
100%PP
8100% burns a target that had a stat rise this turn.
CamouflageNormalStatusAccuracy
—PP
32Changes user's type by terrain (default Normal).
CaptivateNormalStatusAccuracy
100%PP
32Lowers the foe(s) Sp. Atk by 2 if opposite gender.
CelebrateNormalStatusAccuracy
—PP
64No competitive use.
ChargeElectricStatusAccuracy
—PP
32+1 SpD, user's next Electric move 2x power.
Charge BeamElectricSpecialPower
50Accuracy
90%PP
1670% chance to raise the user's Sp. Atk by 1.
CharmFairyStatusAccuracy
100%PP
32Lowers the target's Attack by 2.
Chilling WaterWaterSpecialPower
50Accuracy
100%PP
32100% chance to lower the target's Attack by 1.
Chip AwayNormalPhysicalPower
70Accuracy
100%PP
32Ignores the target's stat stage changes.
ClampWaterPhysicalPower
35Accuracy
85%PP
24Traps and damages the target for 4-5 turns.
CoachingFightingStatusAccuracy
—PP
16Raises an ally's Attack and Defense by 1.
Comet PunchNormalPhysicalPower
18Accuracy
85%PP
24Hits 2-5 times in one turn.
ComeuppanceDarkPhysicalPower
—Accuracy
100%PP
16If hit by an attack, returns 1.5x damage.
ConfideNormalStatusAccuracy
—PP
32Lowers the target's Sp. Atk by 1.
Confuse RayGhostStatusAccuracy
100%PP
16Confuses the target.
ConfusionPsychicSpecialPower
50Accuracy
100%PP
4010% chance to confuse the target.
ConstrictNormalPhysicalPower
10Accuracy
100%PP
5610% chance to lower the target's Speed by 1.
ConversionNormalStatusAccuracy
—PP
48Changes user's type to match its first move.
Conversion 2NormalStatusAccuracy
—PP
48Changes user's type to resist target's last move.
CopycatNormalStatusAccuracy
—PP
32Uses the last move used in the battle.
Cosmic PowerPsychicStatusAccuracy
—PP
32Raises the user's Defense and Sp. Def by 1.
Cotton SporeGrassStatusAccuracy
100%PP
64Lowers the target's Speed by 2.
CounterFightingPhysicalPower
—Accuracy
100%PP
32If hit by physical attack, returns double damage.
CovetNormalPhysicalPower
60Accuracy
100%PP
40If the user has no item, it steals the target's.
Crafty ShieldFairyStatusAccuracy
—PP
16Protects allies from Status moves this turn.
Cross PoisonPoisonPhysicalPower
70Accuracy
100%PP
32High critical hit ratio. 10% chance to poison.
Crush ClawNormalPhysicalPower
75Accuracy
95%PP
1650% chance to lower the target's Defense by 1.
Crush GripNormalPhysicalPower
—Accuracy
100%PP
8More power the more HP the target has left.
DecorateFairyStatusAccuracy
—PP
24Raises the target's Attack and Sp. Atk by 2.
Defend OrderBugStatusAccuracy
—PP
16Raises the user's Defense and Sp. Def by 1.
Defense CurlNormalStatusAccuracy
—PP
64Raises the user's Defense by 1.
DigGroundPhysicalPower
80Accuracy
100%PP
16Digs underground turn 1, strikes turn 2.
Disarming VoiceFairySpecialPower
40Accuracy
—PP
24This move does not check accuracy. Hits foes.
DiveWaterPhysicalPower
80Accuracy
100%PP
16Dives underwater turn 1, strikes turn 2.
Dizzy PunchNormalPhysicalPower
70Accuracy
100%PP
1620% chance to confuse the target.
DoodleNormalStatusAccuracy
100%PP
16User and ally's Abilities become target's Ability.
Double HitNormalPhysicalPower
35Accuracy
90%PP
16Hits 2 times in one turn.
Double KickFightingPhysicalPower
30Accuracy
100%PP
48Hits 2 times in one turn.
Double SlapNormalPhysicalPower
15Accuracy
85%PP
16Hits 2-5 times in one turn.
Double TeamNormalStatusAccuracy
—PP
24Raises the user's evasiveness by 1.
Dragon BreathDragonSpecialPower
60Accuracy
100%PP
3230% chance to paralyze the target.
Dragon CheerDragonStatusAccuracy
—PP
24Ally: Crit ratio +1, or +2 if ally is Dragon type.
Dragon RageDragonSpecialPower
—Accuracy
100%PP
16Deals 40 HP of damage to the target.
Dragon RushDragonPhysicalPower
100Accuracy
75%PP
1620% chance to make the target flinch.
Dream EaterPsychicSpecialPower
100Accuracy
100%PP
24User gains 1/2 HP inflicted. Sleeping target only.
Dual ChopDragonPhysicalPower
40Accuracy
90%PP
24Hits 2 times in one turn.
Dual WingbeatFlyingPhysicalPower
40Accuracy
90%PP
16Hits 2 times in one turn.
Dynamic PunchFightingPhysicalPower
100Accuracy
50%PP
8100% chance to confuse the target.
Echoed VoiceNormalSpecialPower
40Accuracy
100%PP
24Power increases when used on consecutive turns.
Eerie ImpulseElectricStatusAccuracy
100%PP
24Lowers the target's Sp. Atk by 2.
Egg BombNormalPhysicalPower
100Accuracy
75%PP
16No additional effect.
Electric TerrainElectricStatusAccuracy
—PP
165 turns. Grounded: +Electric power, can't sleep.
ElectrifyElectricStatusAccuracy
—PP
32Changes the target's move to Electric this turn.
Electro BallElectricSpecialPower
—Accuracy
100%PP
16More power the faster the user is than the target.
Electro ShotElectricSpecialPower
130Accuracy
100%PP
16Raises Sp. Atk by 1, hits turn 2. Rain: no charge.
ElectrowebElectricSpecialPower
55Accuracy
95%PP
24100% chance to lower the foe(s) Speed by 1.
EmbargoDarkStatusAccuracy
100%PP
24For 5 turns, the target's item has no effect.
EmberFireSpecialPower
40Accuracy
100%PP
4010% chance to burn the target.
EndureNormalStatusAccuracy
—PP
16User survives attacks this turn with at least 1 HP.
EntrainmentNormalStatusAccuracy
100%PP
24The target's Ability changes to match the user's.
EternabeamDragonSpecialPower
160Accuracy
90%PP
8User cannot move next turn.
Fairy LockFairyStatusAccuracy
—PP
16Prevents all Pokemon from switching next turn.
Fairy WindFairySpecialPower
40Accuracy
100%PP
48No additional effect.
Fake TearsDarkStatusAccuracy
100%PP
32Lowers the target's Sp. Def by 2.
False SwipeNormalPhysicalPower
40Accuracy
100%PP
64Always leaves the target with at least 1 HP.
Feather DanceFlyingStatusAccuracy
100%PP
24Lowers the target's Attack by 2.
FeintNormalPhysicalPower
30Accuracy
100%PP
16Nullifies Detect, Protect, and Quick/Wide Guard.
Feint AttackDarkPhysicalPower
60Accuracy
—PP
32This move does not check accuracy.
Fell StingerBugPhysicalPower
50Accuracy
100%PP
40Raises user's Attack by 3 if this KOes the target.
Final GambitFightingSpecialPower
—Accuracy
100%PP
8Does damage equal to the user's HP. User faints.
Fire PledgeFireSpecialPower
80Accuracy
100%PP
16Use with Grass or Water Pledge for added effect.
Fire SpinFireSpecialPower
35Accuracy
85%PP
24Traps and damages the target for 4-5 turns.
FissureGroundPhysicalPower
—Accuracy
30%PP
8OHKOs the target. Fails if user is a lower level.
FlailNormalPhysicalPower
—Accuracy
100%PP
24More power the less HP the user has left.
Flame BurstFireSpecialPower
70Accuracy
100%PP
24Damages Pokemon next to the target as well.
Flame WheelFirePhysicalPower
60Accuracy
100%PP
4010% chance to burn the target. Thaws user.
FlashNormalStatusAccuracy
100%PP
32Lowers the target's accuracy by 1.
FlatterDarkStatusAccuracy
100%PP
24Raises the target's Sp. Atk by 1 and confuses it.
FlingDarkPhysicalPower
—Accuracy
100%PP
16Flings the user's item at the target. Power varies.
Floral HealingFairyStatusAccuracy
—PP
16Heals the target by 50% of its max HP.
Flower ShieldFairyStatusAccuracy
—PP
16Raises Defense by 1 of all active Grass types.
FlyFlyingPhysicalPower
90Accuracy
95%PP
24Flies up on first turn, then strikes the next turn.
Flying PressFightingPhysicalPower
100Accuracy
95%PP
16Combines Flying in its type effectiveness.
Focus EnergyNormalStatusAccuracy
—PP
48Raises the user's critical hit ratio by 2.
Follow MeNormalStatusAccuracy
—PP
32The foes' moves target the user on the turn used.
Force PalmFightingPhysicalPower
60Accuracy
100%PP
1630% chance to paralyze the target.
ForesightNormalStatusAccuracy
—PP
64Fighting, Normal hit Ghost. Evasiveness ignored.
Forest's CurseGrassStatusAccuracy
100%PP
32Adds Grass to the target's type(s).
Freeze ShockIcePhysicalPower
140Accuracy
90%PP
8Charges turn 1. Hits turn 2. 30% paralyze.
Frenzy PlantGrassSpecialPower
150Accuracy
90%PP
8User cannot move next turn.
Frost BreathIceSpecialPower
60Accuracy
90%PP
16Always results in a critical hit.
Fury AttackNormalPhysicalPower
15Accuracy
85%PP
32Hits 2-5 times in one turn.
Fury CutterBugPhysicalPower
40Accuracy
95%PP
32Power doubles with each hit, up to 160.
Fury SwipesNormalPhysicalPower
18Accuracy
80%PP
24Hits 2-5 times in one turn.
Gastro AcidPoisonStatusAccuracy
100%PP
16Nullifies the target's Ability.
Gear UpSteelStatusAccuracy
—PP
32Raises Atk, Sp. Atk of allies with Plus/Minus by 1.
Giga ImpactNormalPhysicalPower
150Accuracy
90%PP
8User cannot move next turn.
GlaciateIceSpecialPower
65Accuracy
95%PP
16100% chance to lower the foe(s) Speed by 1.
Grass PledgeGrassSpecialPower
80Accuracy
100%PP
16Use with Fire or Water Pledge for added effect.
Grass WhistleGrassStatusAccuracy
55%PP
24Causes the target to fall asleep.
Grassy GlideGrassPhysicalPower
55Accuracy
100%PP
32User on Grassy Terrain: +1 priority.
Grassy TerrainGrassStatusAccuracy
—PP
165 turns. Grounded: +Grass power, +1/16 max HP.
GravityPsychicStatusAccuracy
—PP
85 turns: no Ground immunities, 1.67x accuracy.
GrowlNormalStatusAccuracy
100%PP
64Lowers the foe(s) Attack by 1.
GrowthNormalStatusAccuracy
—PP
32Raises user's Attack and Sp. Atk by 1; 2 in Sun.
GrudgeGhostStatusAccuracy
—PP
8If the user faints, the attack used loses all its PP.
Guard SplitPsychicStatusAccuracy
—PP
16Averages Defense and Sp. Def stats with target.
Guard SwapPsychicStatusAccuracy
—PP
16Swaps Defense and Sp. Def changes with target.
GuillotineNormalPhysicalPower
—Accuracy
30%PP
8OHKOs the target. Fails if user is a lower level.
GustFlyingSpecialPower
40Accuracy
100%PP
56Power doubles during Bounce, Fly, and Sky Drop.
Gyro BallSteelPhysicalPower
—Accuracy
100%PP
8More power the slower the user than the target.
HailIceStatusAccuracy
—PP
16For 5 turns, hail crashes down.
Happy HourNormalStatusAccuracy
—PP
48No competitive use.
HardenNormalStatusAccuracy
—PP
48Raises the user's Defense by 1.
Hard PressSteelPhysicalPower
—Accuracy
100%PP
16More power the more HP the target has left.
HeadbuttNormalPhysicalPower
70Accuracy
100%PP
2430% chance to make the target flinch.
Heal BlockPsychicStatusAccuracy
100%PP
24For 5 turns, the foe(s) is prevented from healing.
Heal PulsePsychicStatusAccuracy
—PP
16Heals the target by 50% of its max HP.
Heart StampPsychicPhysicalPower
60Accuracy
100%PP
4030% chance to make the target flinch.
Heat CrashFirePhysicalPower
—Accuracy
100%PP
16More power the heavier the user than the target.
Heavy SlamSteelPhysicalPower
—Accuracy
100%PP
16More power the heavier the user than the target.
Helping HandNormalStatusAccuracy
—PP
32One adjacent ally's move power is 1.5x this turn.
HexGhostSpecialPower
65Accuracy
100%PP
16Power doubles if the target has a status ailment.
Hidden PowerNormalSpecialPower
60Accuracy
100%PP
24Varies in type based on the user's IVs.
Hidden Power BugBugSpecialPower
60Accuracy
100%PP
24
Hidden Power DarkDarkSpecialPower
60Accuracy
100%PP
24
Hidden Power DragonDragonSpecialPower
60Accuracy
100%PP
24
Hidden Power ElectricElectricSpecialPower
60Accuracy
100%PP
24
Hidden Power FightingFightingSpecialPower
60Accuracy
100%PP
24
Hidden Power FireFireSpecialPower
60Accuracy
100%PP
24
Hidden Power FlyingFlyingSpecialPower
60Accuracy
100%PP
24
Hidden Power GhostGhostSpecialPower
60Accuracy
100%PP
24
Hidden Power GrassGrassSpecialPower
60Accuracy
100%PP
24
Hidden Power GroundGroundSpecialPower
60Accuracy
100%PP
24
Hidden Power IceIceSpecialPower
60Accuracy
100%PP
24
Hidden Power PoisonPoisonSpecialPower
60Accuracy
100%PP
24
Hidden Power PsychicPsychicSpecialPower
60Accuracy
100%PP
24
Hidden Power RockRockSpecialPower
60Accuracy
100%PP
24
Hidden Power SteelSteelSpecialPower
60Accuracy
100%PP
24
Hidden Power WaterWaterSpecialPower
60Accuracy
100%PP
24
Horn AttackNormalPhysicalPower
65Accuracy
100%PP
40No additional effect.
Horn DrillNormalPhysicalPower
—Accuracy
30%PP
8OHKOs the target. Fails if user is a lower level.
HowlNormalStatusAccuracy
—PP
64Raises the user's and ally's Attack by 1.
Hydro CannonWaterSpecialPower
150Accuracy
90%PP
8User cannot move next turn.
Hyper BeamNormalSpecialPower
150Accuracy
90%PP
8User cannot move next turn.
Hyper FangNormalPhysicalPower
80Accuracy
90%PP
2410% chance to make the target flinch.
Hyperspace HolePsychicSpecialPower
80Accuracy
—PP
8Breaks the target's protection for this turn.
HypnosisPsychicStatusAccuracy
60%PP
32Causes the target to fall asleep.
Ice BallIcePhysicalPower
30Accuracy
90%PP
32Power doubles with each hit. Repeats for 5 turns.
Ice BurnIceSpecialPower
140Accuracy
90%PP
8Charges turn 1. Hits turn 2. 30% burn.
Ice PunchIcePhysicalPower
75Accuracy
100%PP
2410% chance to freeze the target.
Icicle CrashIcePhysicalPower
85Accuracy
90%PP
1630% chance to make the target flinch.
Icy WindIceSpecialPower
55Accuracy
95%PP
24100% chance to lower the foe(s) Speed by 1.
ImprisonPsychicStatusAccuracy
—PP
16No foe can use any move known by the user.
IncinerateFireSpecialPower
60Accuracy
100%PP
24Destroys the foe(s) Berry/Gem.
InfernoFireSpecialPower
100Accuracy
50%PP
8100% chance to burn the target.
IngrainGrassStatusAccuracy
—PP
32Traps/grounds user; heals 1/16 max HP per turn.
InstructPsychicStatusAccuracy
—PP
24The target immediately uses its last used move.
Ion DelugeElectricStatusAccuracy
—PP
40Normal moves become Electric type this turn.
Iron DefenseSteelStatusAccuracy
—PP
24Raises the user's Defense by 2.
Iron TailSteelPhysicalPower
100Accuracy
75%PP
2430% chance to lower the target's Defense by 1.
Jaw LockDarkPhysicalPower
80Accuracy
100%PP
16Prevents both user and target from switching out.
Jet PunchWaterPhysicalPower
60Accuracy
100%PP
24Usually goes first.
Jump KickFightingPhysicalPower
100Accuracy
95%PP
16User is hurt by 50% of its max HP if it misses.
Jungle HealingGrassStatusAccuracy
—PP
16User and allies: healed 1/4 max HP, status cured.
Karate ChopFightingPhysicalPower
50Accuracy
100%PP
40High critical hit ratio.
KinesisPsychicStatusAccuracy
80%PP
24Lowers the target's accuracy by 1.
Land's WrathGroundPhysicalPower
90Accuracy
100%PP
16No additional effect. Hits adjacent foes.
Laser FocusNormalStatusAccuracy
—PP
48Until the end of the next turn, user's moves crit.
LeafageGrassPhysicalPower
40Accuracy
100%PP
64No additional effect.
Leaf TornadoGrassSpecialPower
65Accuracy
90%PP
1650% chance to lower the target's accuracy by 1.
LeerNormalStatusAccuracy
100%PP
48Lowers the foe(s) Defense by 1.
LickGhostPhysicalPower
30Accuracy
100%PP
4830% chance to paralyze the target.
Life DewWaterStatusAccuracy
—PP
16Heals the user and its allies by 1/4 their max HP.
Lock-OnNormalStatusAccuracy
—PP
8User's next move will not miss the target.
Low SweepFightingPhysicalPower
65Accuracy
100%PP
32100% chance to lower the target's Speed by 1.
Lucky ChantNormalStatusAccuracy
—PP
48For 5 turns, shields user's party from critical hits.
Lunar BlessingPsychicStatusAccuracy
—PP
8User and allies: healed 1/4 max HP, status cured.
Magical LeafGrassSpecialPower
60Accuracy
—PP
32This move does not check accuracy.
Magic PowderPsychicStatusAccuracy
100%PP
32Changes the target's type to Psychic.
Magic RoomPsychicStatusAccuracy
—PP
16For 5 turns, all held items have no effect.
Magnet BombSteelPhysicalPower
60Accuracy
—PP
32This move does not check accuracy.
Magnetic FluxElectricStatusAccuracy
—PP
32Raises Def, Sp. Def of allies with Plus/Minus by 1.
Magnet RiseElectricStatusAccuracy
—PP
16For 5 turns, the user has immunity to Ground.
MagnitudeGroundPhysicalPower
—Accuracy
100%PP
48Hits adjacent Pokemon. Power varies; 2x on Dig.
Mat BlockFightingStatusAccuracy
—PP
16Protects allies from damaging attacks. Turn 1 only.
Mean LookNormalStatusAccuracy
—PP
8Prevents the target from switching out.
MeditatePsychicStatusAccuracy
—PP
64Raises the user's Attack by 1.
Me FirstNormalStatusAccuracy
—PP
32Copies a foe at 1.5x power. User must be faster.
Mega DrainGrassSpecialPower
40Accuracy
100%PP
24User recovers 50% of the damage dealt.
Mega KickNormalPhysicalPower
120Accuracy
75%PP
8No additional effect.
Mega PunchNormalPhysicalPower
80Accuracy
85%PP
32No additional effect.
Metal BurstSteelPhysicalPower
—Accuracy
100%PP
16If hit by an attack, returns 1.5x damage.
Metal ClawSteelPhysicalPower
50Accuracy
95%PP
5610% chance to raise the user's Attack by 1.
Metal SoundSteelStatusAccuracy
85%PP
64Lowers the target's Sp. Def by 2.
Meteor AssaultFightingPhysicalPower
150Accuracy
100%PP
8User cannot move next turn.
Meteor BeamRockSpecialPower
120Accuracy
90%PP
16Raises user's Sp. Atk by 1 on turn 1. Hits turn 2.
MetronomeNormalStatusAccuracy
—PP
16Picks a random move.
MimicNormalStatusAccuracy
—PP
16The last move the target used replaces this one.
Mind ReaderNormalStatusAccuracy
—PP
8User's next move will not miss the target.
MinimizeNormalStatusAccuracy
—PP
16Raises the user's evasiveness by 2.
Miracle EyePsychicStatusAccuracy
—PP
64Psychic hits Dark. Evasiveness ignored.
Mirror CoatPsychicSpecialPower
—Accuracy
100%PP
32If hit by special attack, returns double damage.
Mirror MoveFlyingStatusAccuracy
—PP
32User uses the target's last used move against it.
Mirror ShotSteelSpecialPower
65Accuracy
85%PP
1630% chance to lower the target's accuracy by 1.
MistIceStatusAccuracy
—PP
48For 5 turns, protects user's party from stat drops.
Misty ExplosionFairySpecialPower
100Accuracy
100%PP
8User faints. User on Misty Terrain: 1.5x power.
Misty TerrainFairyStatusAccuracy
—PP
165 turns. Can't status,-Dragon power vs grounded.
Mud BombGroundSpecialPower
65Accuracy
85%PP
1630% chance to lower the target's accuracy by 1.
Muddy WaterWaterSpecialPower
90Accuracy
85%PP
1630% chance to lower the foe(s) accuracy by 1.
Mud ShotGroundSpecialPower
55Accuracy
95%PP
24100% chance to lower the target's Speed by 1.
Mud-SlapGroundSpecialPower
20Accuracy
100%PP
16100% chance to lower the target's accuracy by 1.
Mud SportGroundStatusAccuracy
—PP
24For 5 turns, Electric-type attacks have 1/3 power.
Mystical FireFireSpecialPower
75Accuracy
100%PP
16100% chance to lower the target's Sp. Atk by 1.
Natural GiftNormalPhysicalPower
—Accuracy
100%PP
24Power and type depends on the user's Berry.
Nature PowerNormalStatusAccuracy
—PP
32Attack depends on terrain (default Tri Attack).
Needle ArmGrassPhysicalPower
60Accuracy
100%PP
2430% chance to make the target flinch.
Night DazeDarkSpecialPower
85Accuracy
95%PP
1640% chance to lower the target's accuracy by 1.
NightmareGhostStatusAccuracy
100%PP
24A sleeping target is hurt by 1/4 max HP per turn.
Night SlashDarkPhysicalPower
70Accuracy
100%PP
24High critical hit ratio.
Noble RoarNormalStatusAccuracy
100%PP
48Lowers the target's Attack and Sp. Atk by 1.
OctazookaWaterSpecialPower
65Accuracy
85%PP
1650% chance to lower the target's accuracy by 1.
OctolockFightingStatusAccuracy
100%PP
24Traps target, lowers Def and SpD by 1 each turn.
Odor SleuthNormalStatusAccuracy
—PP
64Fighting, Normal hit Ghost. Evasiveness ignored.
Ominous WindGhostSpecialPower
60Accuracy
100%PP
810% chance to raise all stats by 1 (not acc/eva).
OutrageDragonPhysicalPower
120Accuracy
100%PP
16Lasts 2-3 turns. Confuses the user afterwards.
Parabolic ChargeElectricSpecialPower
65Accuracy
100%PP
32User recovers 50% of the damage dealt.
PaybackDarkPhysicalPower
50Accuracy
100%PP
16Power doubles if the user moves after the target.
Pay DayNormalPhysicalPower
40Accuracy
100%PP
32Scatters coins.
PeckFlyingPhysicalPower
35Accuracy
100%PP
56No additional effect.
Phantom ForceGhostPhysicalPower
90Accuracy
100%PP
16Disappears turn 1. Hits turn 2. Breaks protection.
Pin MissileBugPhysicalPower
25Accuracy
95%PP
32Hits 2-5 times in one turn.
Play NiceNormalStatusAccuracy
—PP
32Lowers the target's Attack by 1.
PluckFlyingPhysicalPower
60Accuracy
100%PP
32User steals and eats the target's Berry.
Poison FangPoisonPhysicalPower
50Accuracy
100%PP
2450% chance to badly poison the target.
Poison GasPoisonStatusAccuracy
90%PP
64Poisons the foe(s).
Poison PowderPoisonStatusAccuracy
75%PP
56Poisons the target.
Poison StingPoisonPhysicalPower
15Accuracy
100%PP
5630% chance to poison the target.
Poison TailPoisonPhysicalPower
50Accuracy
100%PP
40High critical hit ratio. 10% chance to poison.
Pollen PuffBugSpecialPower
90Accuracy
100%PP
24If the target is an ally, heals 50% of its max HP.
PounceBugPhysicalPower
50Accuracy
100%PP
32100% chance to lower the target's Speed by 1.
PoundNormalPhysicalPower
40Accuracy
100%PP
56No additional effect.
PowderBugStatusAccuracy
100%PP
32If using a Fire move, target loses 1/4 max HP.
Powder SnowIceSpecialPower
40Accuracy
100%PP
4010% chance to freeze the foe(s).
Power SplitPsychicStatusAccuracy
—PP
16Averages Attack and Sp. Atk stats with target.
Power SwapPsychicStatusAccuracy
—PP
16Swaps Attack and Sp. Atk stat stages with target.
Power TrickPsychicStatusAccuracy
—PP
16Switches user's Attack and Defense stats.
Power TripDarkPhysicalPower
20Accuracy
100%PP
16+ 20 power for each of the user's stat boosts.
PresentNormalPhysicalPower
—Accuracy
90%PP
2440, 80, 120 power, or heals target 1/4 max HP.
Prismatic LaserPsychicSpecialPower
160Accuracy
100%PP
16User cannot move next turn.
PsybeamPsychicSpecialPower
65Accuracy
100%PP
3210% chance to confuse the target.
Psychic TerrainPsychicStatusAccuracy
—PP
165 turns. Grounded: +Psychic power, priority-safe.
Psycho ShiftPsychicStatusAccuracy
100%PP
16Transfers the user's status ailment to the target.
Psych UpNormalStatusAccuracy
—PP
16Copies the target's current stat stages.
PsywavePsychicSpecialPower
—Accuracy
100%PP
24Random damage equal to 0.5x-1.5x user's level.
PunishmentDarkPhysicalPower
—Accuracy
100%PP
860 power +20 for each of the target's stat boosts.
PurifyPoisonStatusAccuracy
—PP
32Cures target's status; heals user 1/2 max HP if so.
QuashDarkStatusAccuracy
100%PP
24Forces the target to move last this turn.
Quick GuardFightingStatusAccuracy
—PP
24Protects allies from priority attacks this turn.
RageNormalPhysicalPower
20Accuracy
100%PP
32Raises the user's Attack by 1 if hit during use.
Rage PowderBugStatusAccuracy
—PP
32The foes' moves target the user on the turn used.
Rain DanceWaterStatusAccuracy
—PP
8For 5 turns, heavy rain powers Water moves.
Razor LeafGrassPhysicalPower
55Accuracy
95%PP
40High critical hit ratio. Hits adjacent foes.
Razor WindNormalSpecialPower
80Accuracy
100%PP
16Charges, then hits foe(s) turn 2. High crit ratio.
RecycleNormalStatusAccuracy
—PP
16Restores the item the user last used.
RefreshNormalStatusAccuracy
—PP
32User cures its burn, poison, or paralysis.
Relic SongNormalSpecialPower
75Accuracy
100%PP
1610% chance to sleep foe(s). Meloetta transforms.
RetaliateNormalPhysicalPower
70Accuracy
100%PP
8Power doubles if an ally fainted last turn.
RevengeFightingPhysicalPower
60Accuracy
100%PP
16Power doubles if user is damaged by the target.
ReversalFightingPhysicalPower
—Accuracy
100%PP
24More power the less HP the user has left.
Rising VoltageElectricSpecialPower
70Accuracy
100%PP
322x power if target is grounded in Electric Terrain.
Roar of TimeDragonSpecialPower
150Accuracy
90%PP
8User cannot move next turn.
Rock ClimbNormalPhysicalPower
90Accuracy
85%PP
3220% chance to confuse the target.
Rock SmashFightingPhysicalPower
40Accuracy
100%PP
2450% chance to lower the target's Defense by 1.
Rock ThrowRockPhysicalPower
50Accuracy
90%PP
24No additional effect.
Rock TombRockPhysicalPower
60Accuracy
95%PP
24100% chance to lower the target's Speed by 1.
Rock WreckerRockPhysicalPower
150Accuracy
90%PP
8User cannot move next turn.
Role PlayPsychicStatusAccuracy
—PP
16User replaces its Ability with the target's.
Rolling KickFightingPhysicalPower
60Accuracy
85%PP
2430% chance to make the target flinch.
RolloutRockPhysicalPower
30Accuracy
90%PP
32Power doubles with each hit. Repeats for 5 turns.
RototillerGroundStatusAccuracy
—PP
16Raises Atk/Sp. Atk of grounded Grass types by 1.
RoundNormalSpecialPower
60Accuracy
100%PP
24Power doubles if others used Round this turn.
SafeguardNormalStatusAccuracy
—PP
40For 5 turns, protects user's party from status.
Sand AttackGroundStatusAccuracy
100%PP
24Lowers the target's accuracy by 1.
SandstormRockStatusAccuracy
—PP
16For 5 turns, a sandstorm rages. Rock: 1.5x SpD.
Sand TombGroundPhysicalPower
35Accuracy
85%PP
24Traps and damages the target for 4-5 turns.
Scale ShotDragonPhysicalPower
25Accuracy
90%PP
32Hits 2-5 times. User: -1 Def, +1 Spe after last hit.
Scary FaceNormalStatusAccuracy
100%PP
16Lowers the target's Speed by 2.
ScratchNormalPhysicalPower
40Accuracy
100%PP
56No additional effect.
ScreechNormalStatusAccuracy
85%PP
64Lowers the target's Defense by 2.
Secret PowerNormalPhysicalPower
70Accuracy
100%PP
32Effect varies with terrain. (30% paralysis chance)
Self-DestructNormalPhysicalPower
200Accuracy
100%PP
8Hits adjacent Pokemon. The user faints.
Shadow ForceGhostPhysicalPower
120Accuracy
100%PP
8Disappears turn 1. Hits turn 2. Breaks protection.
Shadow PunchGhostPhysicalPower
60Accuracy
—PP
32This move does not check accuracy.
SharpenNormalStatusAccuracy
—PP
48Raises the user's Attack by 1.
Sheer ColdIceSpecialPower
—Accuracy
30%PP
8OHKOs non-Ice targets. Fails if user's lower level.
Shell TrapFireSpecialPower
150Accuracy
100%PP
8User must take physical damage before moving.
ShelterSteelStatusAccuracy
—PP
16Raises the user's Defense by 2.
Shock WaveElectricSpecialPower
60Accuracy
—PP
32This move does not check accuracy.
Silver WindBugSpecialPower
60Accuracy
100%PP
810% chance to raise all stats by 1 (not acc/eva).
Simple BeamNormalStatusAccuracy
100%PP
24The target's Ability becomes Simple.
SingNormalStatusAccuracy
55%PP
24Causes the target to fall asleep.
Skill SwapPsychicStatusAccuracy
—PP
16The user and the target trade Abilities.
Skitter SmackBugPhysicalPower
70Accuracy
90%PP
16100% chance to lower target's Sp. Atk by 1.
Skull BashNormalPhysicalPower
130Accuracy
100%PP
16Raises user's Defense by 1 on turn 1. Hits turn 2.
Sky AttackFlyingPhysicalPower
140Accuracy
90%PP
8Charges, then hits turn 2. 30% flinch. High crit.
Sky DropFlyingPhysicalPower
60Accuracy
100%PP
16User and foe fly up turn 1. Damages on turn 2.
Sky UppercutFightingPhysicalPower
85Accuracy
90%PP
24Can hit Pokemon using Bounce, Fly, or Sky Drop.
SlamNormalPhysicalPower
80Accuracy
75%PP
32No additional effect.
SlashNormalPhysicalPower
70Accuracy
100%PP
32High critical hit ratio.
SludgePoisonSpecialPower
65Accuracy
100%PP
3230% chance to poison the target.
Smack DownRockPhysicalPower
50Accuracy
100%PP
24Removes the target's Ground immunity.
Smart StrikeSteelPhysicalPower
70Accuracy
—PP
16This move does not check accuracy.
Smelling SaltsNormalPhysicalPower
70Accuracy
100%PP
16Power doubles if target is paralyzed, and cures it.
SmogPoisonSpecialPower
30Accuracy
70%PP
3240% chance to poison the target.
SmokescreenNormalStatusAccuracy
100%PP
32Lowers the target's accuracy by 1.
Snap TrapGrassPhysicalPower
35Accuracy
100%PP
24Traps and damages the target for 4-5 turns.
SnarlDarkSpecialPower
55Accuracy
95%PP
24100% chance to lower the foe(s) Sp. Atk by 1.
SnatchDarkStatusAccuracy
—PP
16User steals certain support moves to use itself.
SnoreNormalSpecialPower
50Accuracy
100%PP
24User must be asleep. 30% chance to flinch target.
SnowscapeIceStatusAccuracy
—PP
16For 5 turns, snow falls. Ice: 1.5x Def.
SoakWaterStatusAccuracy
100%PP
32Changes the target's type to Water.
Solar BeamGrassSpecialPower
120Accuracy
100%PP
16Charges turn 1. Hits turn 2. No charge in sunlight.
Solar BladeGrassPhysicalPower
125Accuracy
100%PP
16Charges turn 1. Hits turn 2. No charge in sunlight.
Sonic BoomNormalSpecialPower
—Accuracy
90%PP
32Always does 20 HP of damage.
SparkElectricPhysicalPower
65Accuracy
100%PP
3230% chance to paralyze the target.
Speed SwapPsychicStatusAccuracy
—PP
16Swaps Speed stat with target.
Spicy ExtractGrassStatusAccuracy
—PP
24Raises target's Atk by 2 and lowers its Def by 2.
Spider WebBugStatusAccuracy
—PP
16Prevents the target from switching out.
Spike CannonNormalPhysicalPower
20Accuracy
100%PP
24Hits 2-5 times in one turn.
SpiteGhostStatusAccuracy
100%PP
16Lowers the PP of the target's last move by 4.
Spit UpNormalSpecialPower
—Accuracy
100%PP
16More power with more uses of Stockpile.
SplashNormalStatusAccuracy
—PP
64No competitive use.
SpotlightNormalStatusAccuracy
—PP
24Target's foes' moves are redirected to it this turn.
SteamrollerBugPhysicalPower
65Accuracy
100%PP
3230% chance to make the target flinch.
Steel WingSteelPhysicalPower
70Accuracy
90%PP
4010% chance to raise the user's Defense by 1.
StockpileNormalStatusAccuracy
—PP
32Raises user's Defense, Sp. Def by 1. Max 3 uses.
StompNormalPhysicalPower
65Accuracy
100%PP
3230% chance to make the target flinch.
Stomping TantrumGroundPhysicalPower
75Accuracy
100%PP
16Power doubles if the user's last move failed.
StrengthNormalPhysicalPower
80Accuracy
100%PP
24No additional effect.
String ShotBugStatusAccuracy
95%PP
64Lowers the foe(s) Speed by 2.
Struggle BugBugSpecialPower
50Accuracy
100%PP
32100% chance to lower the foe(s) Sp. Atk by 1.
Stuff CheeksNormalStatusAccuracy
—PP
16Must hold Berry to use. User eats Berry, Def +2.
Stun SporeGrassStatusAccuracy
75%PP
48Paralyzes the target.
SubmissionFightingPhysicalPower
80Accuracy
80%PP
32Has 1/4 recoil.
Sunny DayFireStatusAccuracy
—PP
8For 5 turns, intense sunlight powers Fire moves.
SupersonicNormalStatusAccuracy
55%PP
32Causes the target to become confused.
SwaggerNormalStatusAccuracy
85%PP
24Raises the target's Attack by 2 and confuses it.
SwallowNormalStatusAccuracy
—PP
16Heals the user based on uses of Stockpile.
Sweet KissFairyStatusAccuracy
75%PP
16Causes the target to become confused.
Sweet ScentNormalStatusAccuracy
100%PP
32Lowers the foe(s) evasiveness by 2.
SwiftNormalSpecialPower
60Accuracy
—PP
32This move does not check accuracy. Hits foes.
SynchronoisePsychicSpecialPower
120Accuracy
100%PP
16Hits adjacent Pokemon sharing the user's type.
Syrup BombGrassSpecialPower
60Accuracy
85%PP
16Target's Speed is lowered by 1 stage for 3 turns.
Tachyon CutterSteelSpecialPower
50Accuracy
—PP
16Hits twice. This move does not check accuracy.
TackleNormalPhysicalPower
40Accuracy
100%PP
56No additional effect.
Tail WhipNormalStatusAccuracy
100%PP
48Lowers the foe(s) Defense by 1.
Take DownNormalPhysicalPower
90Accuracy
85%PP
32Has 1/4 recoil.
Take HeartPsychicStatusAccuracy
—PP
24Cures user's status, raises Sp. Atk, Sp. Def by 1.
Tar ShotRockStatusAccuracy
100%PP
24Target gets -1 Spe and becomes weaker to Fire.
Tearful LookNormalStatusAccuracy
—PP
32Lowers the target's Attack and Sp. Atk by 1.
TeatimeNormalStatusAccuracy
—PP
16All active Pokemon consume held Berries.
Techno BlastNormalSpecialPower
120Accuracy
100%PP
8Type varies based on the held Drive.
Teeter DanceNormalStatusAccuracy
100%PP
32Confuses adjacent Pokemon.
TelekinesisPsychicStatusAccuracy
—PP
24For 3 turns, target floats but moves can't miss it.
Terrain PulseNormalSpecialPower
50Accuracy
100%PP
16User on terrain: power doubles, type varies.
ThiefDarkPhysicalPower
60Accuracy
100%PP
40If the user has no item, it steals the target's.
ThrashNormalPhysicalPower
120Accuracy
100%PP
16Lasts 2-3 turns. Confuses the user afterwards.
ThunderclapElectricSpecialPower
70Accuracy
100%PP
8Usually goes first. Fails if target is not attacking.
Thunder FangElectricPhysicalPower
65Accuracy
95%PP
2410% chance to paralyze. 10% chance to flinch.
Thunder ShockElectricSpecialPower
40Accuracy
100%PP
4810% chance to paralyze the target.
TickleNormalStatusAccuracy
100%PP
32Lowers the target's Attack and Defense by 1.
Topsy-TurvyDarkStatusAccuracy
—PP
32Inverts the target's stat stages.
TormentDarkStatusAccuracy
100%PP
24Target can't select the same move twice in a row.
Toxic ThreadPoisonStatusAccuracy
100%PP
32Lowers the target's Speed by 1 and poisons it.
Trick-or-TreatGhostStatusAccuracy
100%PP
32Adds Ghost to the target's type(s).
Triple KickFightingPhysicalPower
10Accuracy
90%PP
16Hits 3 times. Each hit can miss, but power rises.
Trop KickGrassPhysicalPower
70Accuracy
100%PP
24100% chance to lower the target's Attack by 1.
Trump CardNormalSpecialPower
—Accuracy
—PP
5More power the fewer PP this move has left.
TwineedleBugPhysicalPower
25Accuracy
100%PP
32Hits 2 times. Each hit has 20% chance to poison.
TwisterDragonSpecialPower
40Accuracy
100%PP
3220% chance to make the foe(s) flinch.
Upper HandFightingPhysicalPower
65Accuracy
100%PP
24100% flinch. Fails unless target using priority.
UproarNormalSpecialPower
90Accuracy
100%PP
16Lasts 3 turns. Active Pokemon cannot fall asleep.
Vacuum WaveFightingSpecialPower
40Accuracy
100%PP
48Usually goes first.
Venom DrenchPoisonStatusAccuracy
100%PP
32Lowers Atk/Sp. Atk/Speed of poisoned foes by 1.
VenoshockPoisonSpecialPower
65Accuracy
100%PP
16Power doubles if the target is poisoned.
Vine WhipGrassPhysicalPower
45Accuracy
100%PP
40No additional effect.
Vise GripNormalPhysicalPower
55Accuracy
100%PP
48No additional effect.
Vital ThrowFightingPhysicalPower
70Accuracy
—PP
16This move does not check accuracy. Goes last.
Wake-Up SlapFightingPhysicalPower
70Accuracy
100%PP
16Power doubles if target is asleep, and wakes it.
Water GunWaterSpecialPower
40Accuracy
100%PP
40No additional effect.
Water PledgeWaterSpecialPower
80Accuracy
100%PP
16Use with Grass or Fire Pledge for added effect.
Water PulseWaterSpecialPower
60Accuracy
100%PP
3220% chance to confuse the target.
Water SportWaterStatusAccuracy
—PP
24For 5 turns, Fire-type attacks have 1/3 power.
WhirlpoolWaterSpecialPower
35Accuracy
85%PP
24Traps and damages the target for 4-5 turns.
Wide GuardRockStatusAccuracy
—PP
16Protects allies from multi-target moves this turn.
Wing AttackFlyingPhysicalPower
60Accuracy
100%PP
56No additional effect.
WithdrawWaterStatusAccuracy
—PP
64Raises the user's Defense by 1.
Wonder RoomPsychicStatusAccuracy
—PP
16For 5 turns, all Defense and Sp. Def stats switch.
Work UpNormalStatusAccuracy
—PP
48Raises the user's Attack and Sp. Atk by 1.
Worry SeedGrassStatusAccuracy
100%PP
16The target's Ability becomes Insomnia.
WrapNormalPhysicalPower
15Accuracy
90%PP
32Traps and damages the target for 4-5 turns.
Wring OutNormalSpecialPower
—Accuracy
100%PP
8More power the more HP the target has left.
Zap CannonElectricSpecialPower
120Accuracy
50%PP
8100% chance to paralyze the target.
"""




import os #cd C:\Users\quewa\Documents\Pokémon\9
import pickle#streamlit run Pok.py
from datetime import datetime, timedelta,date

from json import*#cd C:\Users\quewa\Documents\Pokémon\9
from urllib.request import*#streamlit run Pok.py
#from datetime import datetime, timedelta,date

aujourdhui = datetime.now()
annee, mois = aujourdhui.year, aujourdhui.month
# Obtenir l'année et le mois précédent
if mois == 1:
    annee = annee - 1
    mois = 12
else:
    annee = annee
    mois = mois - 1


# Nom du fichier de sauvegarde
nom_fichier = "sav.pickle"

def sauvegarder(score_name):
    #print("save : ",gen,tier)
    # Charger les scores existants (ou créer un dictionnaire vide)
    #print("sav :",score_name+str(gen)+tier)
    try:
        with open(nom_fichier, "rb") as f:
            scores = pickle.load(f)
    except FileNotFoundError:
        scores = {}

    # Vérifier si la date du score est le même mois que le mois actuel
    if "date" in scores.get(score_name+str(gen)+tier, {}):
        saved_date = datetime.strptime(scores[score_name+str(gen)+tier]["date"], "%Y-%m")
        #print(saved_date)
        #print(mois,annee)
        if saved_date.month == mois and saved_date.year == annee:
            #print("cc1")
            #print(f"Ancienne valeur du score {score_name}: {scores[score_name]['score']} (Date: {scores[score_name]['date']})")
            return(scores[score_name+str(gen)+tier]['score'])
        else:
            # Mettre à jour le dictionnaire avec le nouveau score et la date
            #exec("sc="+score_name+"()")
            #print("cc2")
            scores[score_name+str(gen)+tier] = {"score": eval(score_name+"()"), "date": str(annee)+"-"+str(mois) }
            # Enregistrer le dictionnaire dans le fichier
            with open(nom_fichier, "wb") as f:
                pickle.dump(scores, f)
            return(scores[score_name+str(gen)+tier]['score'])
    else:
        # créer le score et la date
        #exec("sc="+score_name+"() \nprint(sc)")
        #print(sc)
        #print("cc3")
        scores[score_name+str(gen)+tier] = {"score": eval(score_name+"()") , "date": str(annee)+"-"+str(mois)}
        # Enregistrer le dictionnaire dans le fichier
        with open(nom_fichier, "wb") as f:
            pickle.dump(scores, f)
        return(scores[score_name+str(gen)+tier]['score'])  












try:
    gen=st.session_state.gen
    tier=st.session_state.tier
except:
    gen=9
    tier="ou"

#print("try : ",gen,tier)


#start_time = time()


def smogo():
    # Affichez un spinner pendant le chargement des données
    #with st.spinner("Chargement des données en cours..."):
    #print('https://www.smogon.com/stats/'+date(annee, mois, 1).strftime("%Y-%m")+'/chaos/gen'+str(gen)+tier+'-0.json')
    try:
        with urlopen('https://www.smogon.com/stats/'+date(annee, mois, 1).strftime("%Y-%m")+'/chaos/gen'+str(gen)+tier+'-0.json') as json_file:
            smog = load(json_file)
        #print("f:",smog)    
        return(smog)
    except:
        return()
    
smog=sauvegarder("smogo") 
print("smog : ",gen,tier)
#print("s:",smog)
#print("s:",list(smog['data'].keys())[0:10])

#end_time = time()
#print("Temps smog : " , end_time - start_time)

#start_time = time()

liste_trad = trad.split("\n")
pokemon_trad = {}

for element in liste_trad: #parcours de la liste
    num,pokemon, pokemon_en, pokemon_fr = element.split("\t")
    pokemon_trad[pokemon_en] = pokemon_fr

pokemon_fr = pokemon_trad.get("Caterpie")
#print("Caterpie est traduit par", pokemon_fr)
# Conversion str to liste
liste = "Glimmora / Orthworm / Grimmsnarl / Azumarill / Gholdengo / Dragapult"
liste = liste.split('/')
liste_clean = []
for element in liste:
    liste_clean.append(element.strip())
#print(liste_clean)
liste_trad=[pokemon_trad.get(i) for i in liste_clean]
#print(liste_trad)


#end_time = time()
#print("Temps 2 : " , end_time - start_time)





#table des types
def types(): #@st.cache
    "retourne le tableau de la table des types en fr"
    types=[["","acier","combat","dragon","eau","electrik","fee","feu","glace","insecte","normal","plante","poison","psy","roche","sol","spectre","tenebre","vol"],
          ["acier",0.5,2,0.5,1,1,0.5,2,0.5,0.5,0.5,0.5,0,0.5,0.5,2,1,1,0.5],
          ["combat",1,1,1,1,1,2,1,1,0.5,1,1,1,2,0.5,1,1,0.5,2],
          ["dragon",1,1,2,0.5,0.5,2,0.5,2,1,1,0.5,1,1,1,1,1,1,1],
          ["eau",0.5,1,1,0.5,2,1,0.5,0.5,1,1,2,1,1,1,1,1,1,1],
          ["electrik",0.5,1,1,1,0.5,1,1,1,1,1,1,1,1,1,2,1,1,0.5],
          ["fee",2,0.5,0,1,1,1,1,1,0.5,1,1,2,1,1,1,1,0.5,1],
          ["feu",0.5,1,1,2,1,0.5,0.5,0.5,0.5,1,0.5,1,1,2,2,1,1,1],
          ["glace",2,2,1,1,1,1,2,0.5,1,1,1,1,1,2,1,1,1,1],
          ["insecte",1,0.5,1,1,1,1,2,1,1,1,0.5,1,1,2,0.5,1,1,2],
          ["normal",1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
          ["plante",1,1,1,0.5,0.5,1,2,2,2,1,0.5,2,1,1,0.5,1,1,2],
          ["poison",1,0.5,1,1,1,0.5,1,1,0.5,1,0.5,0.5,2,1,2,1,1,1],
          ["psy",1,0.5,1,1,1,1,1,1,2,1,1,1,0.5,1,1,2,2,1],
          ["roche",2,2,1,2,1,1,0.5,1,1,0.5,2,0.5,1,1,2,1,1,0.5],
          ["sol",1,1,1,2,0,1,1,2,1,1,2,0.5,1,0.5,1,1,1,1],
          ["spectre",1,0,1,1,1,1,1,1,0.5,0,1,0.5,1,1,1,2,2,1],
          ["tenebre",1,2,1,1,1,2,1,1,2,1,1,1,0,1,1,0.5,0.5,1],
          ["vol",1,0.5,1,1,2,1,1,2,0.5,1,0.5,1,1,2,0,1,1,1]]
    return(types)


def types2():
    "retourne le tableau de la table des types en anglais"
    types=[["","Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"],
          ["Steel",0.5,2,0.5,1,1,0.5,2,0.5,0.5,0.5,0.5,0,0.5,0.5,2,1,1,0.5],
          ["Fighting",1,1,1,1,1,2,1,1,0.5,1,1,1,2,0.5,1,1,0.5,2],
          ["Dragon",1,1,2,0.5,0.5,2,0.5,2,1,1,0.5,1,1,1,1,1,1,1],
          ["Water",0.5,1,1,0.5,2,1,0.5,0.5,1,1,2,1,1,1,1,1,1,1],
          ["Electric",0.5,1,1,1,0.5,1,1,1,1,1,1,1,1,1,2,1,1,0.5],
          ["Fairy",2,0.5,0,1,1,1,1,1,0.5,1,1,2,1,1,1,1,0.5,1],
          ["Fire",0.5,1,1,2,1,0.5,0.5,0.5,0.5,1,0.5,1,1,2,2,1,1,1],
          ["Ice",2,2,1,1,1,1,2,0.5,1,1,1,1,1,2,1,1,1,1],
          ["Bug",1,0.5,1,1,1,1,2,1,1,1,0.5,1,1,2,0.5,1,1,2],
          ["Normal",1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
          ["Grass",1,1,1,0.5,0.5,1,2,2,2,1,0.5,2,1,1,0.5,1,1,2],
          ["Poison",1,0.5,1,1,1,0.5,1,1,0.5,1,0.5,0.5,2,1,2,1,1,1],
          ["Psychic",1,0.5,1,1,1,1,1,1,2,1,1,1,0.5,1,1,2,2,1],
          ["Rock",2,2,1,2,1,1,0.5,1,1,0.5,2,0.5,1,1,2,1,1,0.5],
          ["Ground",1,1,1,2,0,1,1,2,1,1,2,0.5,1,0.5,1,1,1,1],
          ["Ghost",1,0,1,1,1,1,1,1,0.5,0,1,0.5,1,1,1,2,2,1],
          ["Dark",1,2,1,1,1,2,1,1,2,1,1,1,0,1,1,0.5,0.5,1],
          ["Flying",1,0.5,1,1,2,1,1,2,0.5,1,0.5,1,1,2,0,1,1,1]]
    return(types)


def tradEN(pok):
    "traduit en anglais "
    liste_trad = trad.split("\n")
    pokemon_trad = {}
    for element in liste_trad: #parcours de la liste
        num,pokemon, pokemon_en, pokemon_fr = element.split("\t")
        pokemon_trad[pokemon_en] = pokemon_fr
    return( [key for key, value in pokemon_trad.items() if value == pok][0])


def tradFR(pok):
    "traduit en Français"
    return(pokemon_trad.get(pok))


def pokemon(nom):
    """Mettre le nom en Français, renvoie le type et les stats"""
    pok=nom
    l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
    type1=""
    j=0
    while type1=="":
        j+=1
        datpok=data.split(pok)[j]
        for i in l_types:
            if datpok.startswith(i):
                type1=i
                break
    type2=""
    for i in l_types:
        if datpok[len(type1):].startswith(i):
            type2=i
            break
    PV=datpok[data.split(pok)[j].find("PV")+3:data.split(pok)[j].find("Atq")]
    Atq=datpok[data.split(pok)[j].find("Atq")+4:data.split(pok)[j].find("Déf")]
    Def=datpok[data.split(pok)[j].find("Déf")+4:data.split(pok)[j].find("SpA")]
    SpA=datpok[data.split(pok)[j].find("SpA")+4:data.split(pok)[j].find("SpD")]
    SpD=datpok[data.split(pok)[j].find("SpD")+4:data.split(pok)[j].find("Vit")]
    Vit=datpok[data.split(pok)[j].find("Vit")+4:data.split(pok)[j].find("BST")]


    #traduction
    liste_trad = trad.split("\n")
    pokemon_trad = {}
    for element in liste_trad: #parcours de la liste
        num,pokemon, pokemon_en, pokemon_fr = element.split("\t")
        pokemon_trad[pokemon_en] = pokemon_fr
    traduction  = [key for key, value in pokemon_trad.items() if value == pok][0]

    #EV les plus courant
    max_value = max(smog['data'][traduction]['Spreads'].values())
    max_key = [key for key, value in smog['data'][traduction]['Spreads'].items() if value == max_value]
    ev = [int(x) for x in  max_key[0].split(':')[1].split('/')]

    StatPok=[2*int(PV)+ev[0]/4+141,2*int(Atq)+ev[1]/4+36,2*int(Def)+ev[2]/4+36,2*int(SpA)+ev[3]/4+36,2*int(SpD)+ev[4]/4+36,2*int(Vit)+ev[5]/4+36]
    StatPok=[int(i) for i in StatPok]

    return(type1,type2,StatPok)

def degats(type1,att,att1,pok):
    adv1=pokemon(pok)
    types=types2()
    numligne=1
    while adv1[0] !=types[0][numligne]: #landorus
        numligne+=1
    numcol=1
    while type1!=types[0][numcol]:#bulbi
        numcol+=1
    s=types[numligne][numcol]
    if adv1[1] !="":
        numligne=1
        while adv1[1]!=types[0][numligne]:
            numligne+=1
        s*=types[numligne][numcol]
    return((42*att*att1/adv1[2][2]/50+2)*s*0.9/adv1[2][0]*100)
    
    
def degatsSpa(type1,att,att1,pok):
    adv1=pokemon(pok)
    types=types2()
    numligne=1
    while adv1[0] !=types[0][numligne]: #landorus
        numligne+=1
    numcol=1
    while type1!=types[0][numcol]:#bulbi
        numcol+=1
    s=types[numligne][numcol]
    if adv1[1] !="":
        numligne=1
        while adv1[1]!=types[0][numligne]:
            numligne+=1
        s*=types[numligne][numcol]
    return((42*att*att1/adv1[2][4]/50+2)*s*0.9/adv1[2][0]*100)    
    
    
def degats2(type1,att,att1,liste):
    liste = liste.split('/')
    liste_clean = []
    for element in liste:
        liste_clean.append(element.strip())
    liste_trad=[pokemon_trad.get(i) for i in liste_clean]
    deg=[]
    for i in range(len(liste)):
        deg+=[degats(type1,att,att1,liste_trad[i])]
    return(deg)    
    

def degats2Spa(type1,att,att1,liste):
    liste = liste.split('/')
    liste_clean = []
    for element in liste:
        liste_clean.append(element.strip())
    liste_trad=[pokemon_trad.get(i) for i in liste_clean]
    deg=[]
    for i in range(len(liste)):
        deg+=[degatsSpa(type1,att,att1,liste_trad[i])]
    return(deg)


def degats3(type1,att,att1,type2,att2,type3,att3,liste):
    max_liste=[max(x) for x in zip(degats2(type1,att,att1,liste), degats2(type2,att,att2,liste), degats2(type3,att,att3,liste))]
    return(max_liste)


def degats3Spa(type1,att,att1,type2,att2,type3,att3,liste):
    max_liste=[max(x) for x in zip(degats2Spa(type1,att,att1,liste), degats2Spa(type2,att,att2,liste), degats2Spa(type3,att,att3,liste))]
    return(max_liste)

def destruction(type1,att,att1,type2,att2,type3,att3,liste):
    "Compte le nombre de pokemon que je peux battre"
    return(len([x for x in degats3(type1,att,att1,type2,att2,type3,att3,liste) if x > 100]))
def destructionSpa(type1,att,att1,type2,att2,type3,att3,liste):
    "Compte le nombre de pokemon que je peux battre"
    return(len([x for x in degats3Spa(type1,att,att1,type2,att2,type3,att3,liste) if x > 100]))


#meilleurs types offensifs
def score():
    "Score des types"
    print("score")
    score=[]
    poke=smog['data'].keys()#i landorus
    l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
    for i in l_types:
        sc=0
        for j in poke:
            try:
                #print(j)
                pok=tradFR(j)
                #print(pok)
                datpok=data.split(pok)[1]
                #print(datpok)
                for ii in l_types:
                    if datpok.startswith(ii):
                        type1=ii
                        break
                type2=""
                for ii in l_types:
                    if datpok[len(type1):].startswith(ii):
                        type2=ii
                        break
                numligne=1
                while type1!=types2()[0][numligne]:
                    numligne+=1
                numligne2=1
                if type2!="":
                    while type2!=types2()[0][numligne2]:
                        numligne2+=1
                numcol=1
                while i!=types2()[0][numcol]:
                    numcol+=1
                s=types2()[numligne][numcol]*smog['data'][j]['usage']
                if type2!="":
                    s*=types2()[numligne2][numcol]
                sc+=s
            except:
                if i==l_types[0]:
                    print(j)
                    print(pok)
                    print(datpok)
        score+=[sc]

    l_types, score = zip(*sorted(zip(l_types, score), key=lambda x: x[1], reverse=True))
    return(l_types,score)
    
    
#meilleurs doubles types offensifs
def score2():
    "Score des doubles types"
    l_double=[]
    score=[]
    poke=smog['data'].keys()#i landorus
    l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
    c=0
    for i in l_types:
        c+=1
        for i2 in l_types[c:]:
            l_double+=[(i,i2)]

            sc=0
            for j in poke:
                pok=tradFR(j)
                datpok=data.split(pok)[1]
                for ii in l_types:
                    if datpok.startswith(ii):
                        type1=ii
                        break
                type2=""
                for ii in l_types:
                    if datpok[len(type1):].startswith(ii):
                        type2=ii
                        break
                numligne=1
                while type1!=types2()[0][numligne]:
                    numligne+=1
                numligne2=1
                if type2!="":
                    while type2!=types2()[0][numligne2]:
                        numligne2+=1
                numcol=1
                while i!=types2()[0][numcol]:
                    numcol+=1
                s=types2()[numligne][numcol]*smog['data'][j]['usage']
                if type2!="":
                    s*=types2()[numligne2][numcol]

                numcol=1 #deuxième type offensif
                while i2!=types2()[0][numcol]:
                    numcol+=1
                s2=types2()[numligne][numcol]*smog['data'][j]['usage']
                if type2!="":
                    s2*=types2()[numligne2][numcol]

                sc+=max(s,s2)
            score+=[sc]

    l_double, score = zip(*sorted(zip(l_double, score), key=lambda x: x[1], reverse=True))
    return(l_double,score)    
    

#meilleurs triple types offensifs
def score3():
    "Score des triple types"
    l_triple=[]
    score=[]
    poke=smog['data'].keys()#i landorus
    l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
    c=0
    for i in l_types:
        c+=1
        cc=c
        for i2 in l_types[c:]:
            cc+=1
            for i3 in l_types[cc:]:
                l_triple+=[(i,i2,i3)]

                sc=0
                for j in poke:
                    pok=tradFR(j)
                    datpok=data.split(pok)[1]
                    for ii in l_types:
                        if datpok.startswith(ii):
                            type1=ii
                            break
                    type2=""
                    for ii in l_types:
                        if datpok[len(type1):].startswith(ii):
                            type2=ii
                            break
                    numligne=1
                    while type1!=types2()[0][numligne]:
                        numligne+=1
                    numligne2=1
                    if type2!="":
                        while type2!=types2()[0][numligne2]:
                            numligne2+=1
                    numcol=1
                    while i!=types2()[0][numcol]:
                        numcol+=1
                    s=types2()[numligne][numcol]*smog['data'][j]['usage']
                    if type2!="":
                        s*=types2()[numligne2][numcol]

                    numcol=1 #deuxième type offensif
                    while i2!=types2()[0][numcol]:
                        numcol+=1
                    s2=types2()[numligne][numcol]*smog['data'][j]['usage']
                    if type2!="":
                        s2*=types2()[numligne2][numcol]

                    numcol=1 #troisième type offensif
                    while i3!=types2()[0][numcol]:
                        numcol+=1
                    s3=types2()[numligne][numcol]*smog['data'][j]['usage']
                    if type2!="":
                        s3*=types2()[numligne2][numcol]

                    sc+=max(s,s2,s3)
                score+=[sc]

    l_triple, score = zip(*sorted(zip(l_triple, score), key=lambda x: x[1], reverse=True))
    return(l_triple,score)

l_types=l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"] 
def score4():
    "meilleurs pokemon offensif grâce à leurs types"
    poke=smog['data'].keys()
    sc=[]
    datscore=score()
    datscore2=score2()
    for j in poke:
        pok=tradFR(j)
        datpok=data.split(pok)[1]
        for ii in l_types:
            if datpok.startswith(ii):
                type1=ii
                break
        type2=""
        for ii in l_types:
            if datpok[len(type1):].startswith(ii):
                type2=ii
                break
        if type2=="":
            index = datscore[0].index(type1)
            sc+=[datscore[1][index]]
        else:
            try:
                index=datscore2[0].index((type1,type2))
            except:
                try:
                    index=datscore2[0].index((type2,type1))
                except:
                    print("Traduction raté : ",j)

            sc+=[datscore2[1][index]]

    # Combinez les deux listes en une liste de tuples
    poke_sc_tuples = list(zip(list(poke), sc))
    # Triez la liste de tuples en utilisant le score (deuxième élément du tuple)
    poke_sc_tuples.sort(key=lambda x: x[1],reverse=True)
    # Créez un nouveau dictionnaire trié à partir de la liste de tuples
    poke_tri = dict(poke_sc_tuples)
    # Affichez le dictionnaire trié
    return(poke_tri)



def scoreSweeper(att,type1,att1,type2,att2,type3,att3):
    "score de mon sweeper"
    poke=smog['data'].keys() #Liste des pok
    sc=0
    for j in poke:
        try:
            if destruction(type1,att,att1,type2,att2,type3,att3,j)==1:
                sc+=smog['data'][j]['usage'] # usage
        except:
            a=1
             #print("Type non trouvé pour: ",j)
    return(sc)
def scoreSweeperSpa(att,type1,att1,type2,att2,type3,att3):
    "score de mon sweeper Spa"
    poke=smog['data'].keys() #Liste des pok
    sc=0
    for j in poke:
        try:
            if destructionSpa(type1,att,att1,type2,att2,type3,att3,j)==1:
                sc+=smog['data'][j]['usage'] # usage
        except:
            a=1
             #print("Type non trouvé pour: ",j)
    return(sc)






#cd C:\Users\quewa\Documents\Pokémon\9
#import streamlit as st #streamlit run Pok.py

#st.set_option('deprecation.showPyplotGlobalUse', False)


# Charger le contenu du fichier CSS
#with open('css.css') as f:
#    css = f.read()

# Ajouter le contenu du fichier CSS à l'application Streamlit
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


#st.title("Analyse des tiers")




#gen = st.number_input("Sélectionnez votre gen", min_value=1, max_value=9, step=1, value=9 )


# Mettez à jour la session state avec la nouvelle valeur de gen
#st.session_state.gen = gen

# Widget de sélection du mode
#tier = st.selectbox("Choisissez le tier", ["ou", "uu","lc","ru","doublesou","ubers","1v1"]) # index=0

#st.session_state.tier = tier



# Liste des titres d'onglets
titres_onglets = ["Score des types", "Scores de mon Sweeper","Scores pour sweep des Pokémon","ACP"]

# Création des onglets
onglet_selectionne = st.selectbox("Mode",titres_onglets)


# Ajouter du contenu à chaque onglet
if onglet_selectionne=="Score des types":

    
    # Ajouter un titre
    st.title(f"Pokémon {tier} {gen}G")
    
    
    
    
    # Ajouter du texte
    #st.write(f"Analyse de l'OU {gen}G")
    
    
    
    
    #if col1.button('Pourcentage de femmes par grande discipline'):
    #    plot_graph1()
    
    
    # Titre de niveau 2 (h2)
    st.markdown("<h2>Score offensif des types</h2>", unsafe_allow_html=True)
    
    st.write("Exemple : ")
    
    st.write("Landorus a 40% d'utilisation et Heatran 10% d'utilisation. Donc une attaque Ice a un score de 0.4x4+0.1/4+... et une attaque Ground a un score de 0.4x0+0.1x4+... ")
    
    
    
    
    
    
    col1, col2,col3,col4 = st.columns(4)
    
    #meilleurs types offensifs score   "Score des types"   type score
    # Créer un bouton "Score"
    if col1.button('Score des types'):
        #1==1
        # Appeler la fonction score
        #print(sauvegarder("score"))
        liste1, liste2 = sauvegarder("score")
        # Afficher les deux listes
        #st.write(' '.join(liste1))
        #st.write( '   '.join([f'{x:.2f}' for x in liste2]))
        # Créer un tableau pour afficher les deux listes
        tableau = { 'Type : ': liste1, 'Score : ': liste2    }
        # Afficher le tableau
        st.table(tableau)
    
    if col2.button('Score des doubles types'):
        #1==1
        liste1, liste2 = sauvegarder("score2")
        liste1 = [f'{x} {y}' for x, y in liste1]
        tableau = { 'Double type : ': liste1, 'Score : ': liste2    }
        st.table(tableau)
    
    
    
    if col3.button('Score des triples types'):
        #1==1
        liste1, liste2 = sauvegarder("score3")
        liste1 = [f'{x} {y} {z}' for x, y, z in liste1]
        tableau = { 'Triple type : ': liste1, 'Score : ': liste2    }
        st.table(tableau)
    
    
    
    if col4.button('Pokémon avec le meilleur double stab'):
        #1==1
        liste1 = sauvegarder("score4")
        liste1 = [f'{x} ' for x in liste1]
        tableau = { 'Pokémon : ': liste1[:100]   }
        st.table(tableau)
    
    
    
    
    from streamlit.components.v1 import html
    
    # Définissez votre code JavaScript
    #mon_script_js = """alert("Bonjour, monde !");"""
    
    
    # Lire le contenu du fichier script.js et stocker dans une variable
    with open("script.js", "r") as js_file:
        mon_script_js = js_file.read()
    #print(mon_script_js)
    
    
    # Enveloppez le code JavaScript dans des balises <script>
    mon_html = f"<script>{mon_script_js}</script>"
    
    # Affichez le composant HTML
    html(mon_html)
    
    
    
 



def puis(move):
    "Mettre le nom anglais du move, retourne sa puissance"
    # Séparer les mouvements en une liste de chaînes de caractères moves_list = moves.split('.\n')
    # Parcourir la liste de mouvements
    # Séparer chaque mouvement en une liste de chaînes de caractères  move_info = move.split('\n')
    # Extraire le nom du mouvementname = move_info[0].split(' ')[0]
    l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
    m=moves
    endroit=m.find(move) #moves[endroit+len(move):endroit+len(move)+10]
    if endroit==-1:
        m=moves.lower().replace(' ', '').replace('-', '')
        endroit=m.find(move)
    ty=""   
    for ii in l_types:
        if m[endroit+len(move):endroit+len(move)+10].startswith((ii,ii.lower())):
            ty=ii
            break
    cat=""
    if m[endroit+len(move)+len(ty):endroit+len(move)+len(ty)+1] in "Pp" :
        cat="Physique"
    elif m[endroit+len(move)+len(ty):endroit+len(move)+len(ty)+2]=="Sp" or m[endroit+len(move)+len(ty):endroit+len(move)+len(ty)+2]=="sp" :
        cat="Special"
    else:
        cat="Statut"
    power=0
    if cat!="Statut":
        power=int(m[endroit+len(move)+len(ty):endroit+len(move)+len(ty)+40].split("\n")[1].lower().split("accuracy")[0])
    return(cat,ty,power)

def extraire_nombre(chaine):
    nombre = ''.join(filter(str.isdigit, chaine))
    return int(nombre)


def contre(att,type1,att1,type2,att2,type3,att3,pc=0.1):
    "Voir les pokémon qui me contre"
    poke=smog['data'].keys() #Liste des pok
    sc=0
    l=[]
    for j in poke:
        try:
            if destruction(type1,att,att1,type2,att2,type3,att3,j)==1:
                sc+=smog['data'][j]['usage'] # usage
            elif smog['data'][j]['usage']>pc:
                l+=[j+" "+str(smog['data'][j]['usage'])[2:4]]
        except:
            a=1
                #print("Type non trouvé pour: ",j)
    l = sorted(l, key=extraire_nombre, reverse=True)   
    return(l)

def contreSpa(att,type1,att1,type2,att2,type3,att3,pc=0.1):
    "Voir les pokémon qui me contre"
    poke=smog['data'].keys() #Liste des pok
    sc=0
    l=[]
    for j in poke:
        try:
            if destructionSpa(type1,att,att1,type2,att2,type3,att3,j)==1:
                sc+=smog['data'][j]['usage'] # usage
            elif smog['data'][j]['usage']>pc:
                l+=[j+" "+str(smog['data'][j]['usage'])[2:4]]
        except:
            a=1
                #print("Type non trouvé pour: ",j)
    l = sorted(l, key=extraire_nombre, reverse=True)
    return(l)


if onglet_selectionne=="Scores de mon Sweeper":

    st.title(f"Score et contres du combo contre {tier} {gen}G")
    # Créer des champs de saisie pour att, att1, att2 et att3
    
    st.write("""Exemple :  \n 
Je joue Braségali. \n 
Il a une attaque de 339.  \n 
Une fois que j'ai placé ma danse lames, mon attaque est de att=678.  \n 
Je joue mon set avec close combat et flareblitz.  \n 
Donc att1=120 att2=120 att3=0   type1=Fighting type2=Fire  \n 
Le score du Pokémon est 4.3  \n 
Cela veut dire qu'après une danse lames, Braségali peut One Shot en moyenne 4.3 Pokémon sur 6 de l'adversaire.  \n 
Un contre à Braségali est Great Tusk qui est joué dans 25% des teams, il survit à une attaque de Braségali.""")
    
    att = st.number_input("Valeur pour att",value=0)
    att1 = st.number_input("Valeur pour att1",value=0)
    att2 = st.number_input("Valeur pour att2",value=0)
    att3 = st.number_input("Valeur pour att3",value=0)
    
    # Liste des types disponibles
    l_types = ["Steel", "Fighting", "Dragon", "Water", "Electric", "Fairy", "Fire", "Ice", "Bug", "Normal", "Grass", "Poison", "Psychic", "Rock", "Ground", "Ghost", "Dark", "Flying"]
    
    # Sélection des types
    type1 = st.selectbox("Sélectionnez le type 1", l_types)
    type2 = st.selectbox("Sélectionnez le type 2", l_types)
    type3 = st.selectbox("Sélectionnez le type 3", l_types)
    
    # Bouton pour activer la fonction scoreSweeper
    if st.button("Calculer le score physique"):
        # Appeler la fonction scoreSweeper avec les valeurs entrées
        resultat1=scoreSweeper(att, type1, att1, type2, att2, type3, att3)
        st.session_state.resultat1=resultat1
    try:
        resultat1=st.session_state.resultat1
        st.write(f"Le score calculé est : **{resultat1}**",unsafe_allow_html =True)
    except:
        st.write(f"Le score calculé est :")


    if st.button("Calculer le score spécial"):
        resultat2=scoreSweeperSpa(att, type1, att1, type2, att2, type3, att3)
        st.session_state.resultat2=resultat2
    try:
        resultat2=st.session_state.resultat2
        st.write(f"Le score calculé est : **{resultat2}**", unsafe_allow_html=True)
    except:
        st.write(f"Le score calculé est :")


    if st.button("Contres de mon attaque physique"):
        contre1=contre(att,type1,att1,type2,att2,type3,att3,pc=0.01)
        st.session_state.contre1=contre1
    try:
        contre1=st.session_state.contre1
        # Diviser chaque élément de la liste en deux parties : nom et pourcentage
        name=[item.rsplit(maxsplit=1)[0] for item in contre1]
        noms = [tradFR(item) for item in name]
        pourcentages = [int(item.rsplit(maxsplit=1)[1]) for item in contre1]
        dfcontre1={"Name": name,"Nom":noms, "Pourcentage": pourcentages}
        st.write(f"Les contres de mon attaque physiques : ", unsafe_allow_html=True)#**{dfcontre1}**
        st.table(dfcontre1)
    except:
        st.write(f"Les contres de mon attaque physiques :")
    



    if st.button("Contres de mon attaque spécial"):
        contre2=contreSpa(att,type1,att1,type2,att2,type3,att3,pc=0.01)
        st.session_state.contre2=contre2
    try:
        contre2=st.session_state.contre2
        name=[item.rsplit(maxsplit=1)[0] for item in contre2]
        noms = [tradFR(item) for item in name]
        pourcentages = [int(item.rsplit(maxsplit=1)[1]) for item in contre2]
        dfcontre1={"Name": name,"Nom":noms, "Pourcentage": pourcentages}
        st.write(f"Les contres de mon attaque physiques : ", unsafe_allow_html=True)#**{dfcontre1}**
        st.table(dfcontre1)
    except:
        st.write(f"Les contres de mon attaque spécial :")



if onglet_selectionne=="Scores pour sweep des Pokémon":
    #Meilleurs Pokémon pour sweep
    import re #findall
    from time import time,sleep
    
    
    st.write("""Le set le plus joué de Braségali est : \n
EV: ['Adamant:0/252/0/0/4/252'] \n
Statistiques du Pokémon: [301, 339, 176, 256, 177, 259] \n 
Moves : ['closecombat', 'swordsdance', 'flareblitz', 'protect']  \n 
Le score du Pokémon est 4.3  \n
Cela veut dire qu'après une danse lames, Braségali peut One Shot en moyenne 4.3 Pokémon sur 6 de l'adversaire.""") 
    
    #smog['data'].keys() #Liste des pok
    #smog['data'][j]['usage'] # usage
    
    def sweep():
        
        #print("sweep : ",tier)
        
        time5=time()
        time1=time()
        l=[]
        m=moves.lower().replace(' ', '').replace('-', '')
        poke=smog['data'].keys() #Liste des pok
        print(poke)
        time1=time()-time1
        
        for po in list(poke):#[0:10]
            try:
                time2=time()
                pok=tradFR(po)
                #print(pok)
                #pok="Lanssorien"
                #print(pok)
                datpok=data.split(pok)[1]
                l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
                for i in l_types:
                    if datpok.startswith(i):
                        type1=i
                        break
                type2=""
                for i in l_types:
                    if datpok[len(type1):].startswith(i):
                        type2=i
                        break
                #print('Types du Pokémon:',type1,type2)
                PV=datpok[data.split(pok)[1].find("PV")+3:data.split(pok)[1].find("Atq")]
                Atq=datpok[data.split(pok)[1].find("Atq")+4:data.split(pok)[1].find("Déf")]
                Def=datpok[data.split(pok)[1].find("Déf")+4:data.split(pok)[1].find("SpA")]
                SpA=datpok[data.split(pok)[1].find("SpA")+4:data.split(pok)[1].find("SpD")]
                SpD=datpok[data.split(pok)[1].find("SpD")+4:data.split(pok)[1].find("Vit")]
                Vit=datpok[data.split(pok)[1].find("Vit")+4:data.split(pok)[1].find("BST")]
                #print('Statistiques du Pokémon:',PV,Atq,Def,SpA,SpD,Vit)
        
                #traduction
                #liste_trad = trad.split("\n")
                #pokemon_trad = {}
                #for element in liste_trad: #parcours de la liste
                #    num,pokemon, pokemon_en, pokemon_fr = element.split("\t")
                #    pokemon_trad[pokemon_en] = pokemon_fr
                traduction  = po #[key for key, value in pokemon_trad.items() if value == pok][0]
        
                #EV les plus courant
                max_value = max(smog['data'][traduction]['Spreads'].values())
                max_key = [key for key, value in smog['data'][traduction]['Spreads'].items() if value == max_value]
                #print('EV:', max_key)
                ev = [int(x) for x in  max_key[0].split(':')[1].split('/')]
        
                StatPok=[2*int(PV)+ev[0]/4+141,2*int(Atq)+ev[1]/4+36,2*int(Def)+ev[2]/4+36,2*int(SpA)+ev[3]/4+36,2*int(SpD)+ev[4]/4+36,2*int(Vit)+ev[5]/4+36]
                StatPok=[int(i) for i in StatPok]
                #print('Statistiques du Pokémon:',StatPok)
        
        
                #Les 4 attaques du pokemon
        
                # Trier les attaques par nombre d'utilisations décroissant
                attaques_triees = sorted(smog['data'][traduction]['Moves'].items(), key=lambda x: x[1], reverse=True)
                #print([i for i,j in attaques_triees[0:4]]) #[attaque for attaque, _ in donnees]
        
                #print(puis('dragondarts'))
        
                
                #l_types=["Steel","Fighting","Dragon","Water","Electric","Fairy","Fire","Ice","Bug","Normal","Grass","Poison","Psychic","Rock","Ground","Ghost","Dark","Flying"]
                for atta,sco in attaques_triees[0:4]:
                    #m=moves
                    #endroit=m.find(atta) #moves[endroit+len(move):endroit+len(move)+10]  Raises the user's Speed by 2;
                    #if endroit==-1:
                    #print(atta)
                    #print(m[0:100])
                    endroit=m.find(atta)
                    #print(m[endroit:endroit+100])
                    #print(endroit)
                    #print(atta, m[endroit:endroit+len(move)+24+100].split("\n")[2])
                    if "raisestheuser's" in m[endroit:endroit+24+100].split("\n")[2]:#raisestheuser's  Raises the user's
                        #print(atta,m[endroit:endroit+len(move)+24+100].split("\n")[2],"attack" in m[endroit:endroit+len(move)+24+100].split("\n")[2])
                        #print(atta," : ",m[endroit:endroit+len(move)+24+1000].split("\n")[2])#+24+len(move)
                        #sp.atk attack
                        if "attack" in m[endroit:endroit+24+100].split("\n")[2]:
                            #print(atta)
                            nombre = re.findall(r"\d+\.\d+|\d+", m[endroit:endroit+24+100].split("\n")[2])
                            #print(atta,nombre)
                            #print(atta,m[endroit:endroit+len(move)+24+100].split("\n")[2],nombre[1])
                            StatPok[1]=StatPok[1]*float(nombre[1])                 
                        if "sp.atk" in m[endroit:endroit+24+100].split("\n")[2]:
                            nombre = re.findall(r"\d+\.\d+|\d+", m[endroit+2:endroit+24+100].split("\n")[2])
                            StatPok[3]=StatPok[3]*float(nombre[1])  
                            
                att=max(StatPok[1],StatPok[3])
                #print(att)
                pui=[puis(i)[2] for i,j in attaques_triees[0:3]]
                ty=[puis(i)[1] for i,j in attaques_triees[0:3]]
        
                time2=time()-time2
                time3=time()
                for i in range(3):
                    if ty[i] in [type1,type2]:
                        pui[i]=1.5*pui[i]
                        
                if att>(60*2+31+63)*1.5:
                    if StatPok[1]>StatPok[3]:
                        time4=time()
                        sc=scoreSweeper(att,ty[0],pui[0],ty[1],pui[1],ty[2],pui[2])
                        if sc>1:
                            l+=[(pok,sc)]
                        time4=time()-time4    
                    else:
                        sc=scoreSweeperSpa(att,ty[0],pui[0],ty[1],pui[1],ty[2],pui[2])
                        if sc>1:
                            l+=[(pok,sc)]
            except:
                a=1
            
            time3=time()-time3
            
        
        #print("Temps : ",(time()-time5)/60)    
        l= sorted(l, key=lambda x: x[1], reverse=True)    
        return(l)
    sweep1=sauvegarder("sweep")    
    #st.write(sweep1) #dfcontre1={"Name": name,"Nom":noms, "Pourcentage": pourcentages}
    
    noms = [item[0] for item in sweep1]
    rescore = [item[1] for item in sweep1]
    sweep1={"Nom":noms, "Score": rescore}
    st.table(sweep1)



print(list(smog['data'].keys())[0:10])


if onglet_selectionne=="ACP":
    
    print("ACP " ,gen, tier )
 
    
    
    poke=smog['data'].keys()
    noms=list(poke)#liste des pok
    
    print(list(poke)[0:10])
    
    type1=[]
    type2=[]
    PV=[]
    Atq=[]
    Def=[]
    SpA=[]
    SpD=[]
    Vit=[]
    usa=[]
    sup=[]
    for i in noms[:]:
        try:
            pok=pokemon(tradFR(i))
            type1+=[pok[0]]
            type2+=[pok[1]]
            PV+=[pok[2][0]]
            Atq+=[pok[2][1]]
            Def+=[pok[2][2]]
            SpA+=[pok[2][3]]
            SpD+=[pok[2][4]]
            Vit+=[pok[2][5]]
            usa+=[smog['data'][i]['usage']]
        except:
            sup+=[i]
            
    # Supprimez les noms de la liste
    for ss in sup:
        noms.remove(ss)   
    
    
    
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    
    # Sélectionnez les variables quantitatives   "noms":noms,
    variables_quantitatives =  pd.DataFrame({ "PV": PV, "Atq": Atq, "Def": Def, "SpA": SpA, "SpD": SpD, "Vit": Vit, "usa": usa})
    
    
    
    
    # Standardisez les variables quantitatives
    variables_standardisees = (variables_quantitatives - variables_quantitatives.mean()) / variables_quantitatives.std()
    
    # Calculez la matrice de covariance
    matrice_covariance = variables_standardisees.cov()
    
    # Calculez les valeurs propres et vecteurs propres
    valeurs_propres, vecteurs_propres = np.linalg.eig(matrice_covariance)
    
    # Triez les vecteurs propres par ordre décroissant des valeurs propres
    indices_tries = np.argsort(valeurs_propres)[::-1]
    valeurs_propres_triees = valeurs_propres[indices_tries]
    vecteurs_propres_tries = vecteurs_propres[:, indices_tries]
    
    # Calculez les composantes principales
    composantes_principales = np.dot(variables_standardisees, vecteurs_propres_tries)
    
    # Créez un DataFrame avec les composantes principales
    acp_df = pd.DataFrame(data=composantes_principales, columns=[f"CP{i+1}" for i in range(len(variables_quantitatives.columns))])
    
    # Ajoutez la variable "noms" au DataFrame
    acp_df["noms"] = noms
    acp_df["type1"] = type1
    
    # Calculer le ratio de variance expliquée
    ratio_variance_expliquee = valeurs_propres_triees / np.sum(valeurs_propres_triees)
    
    # Affichez le ratio de variance expliquée
    for i, ratio in enumerate(ratio_variance_expliquee):
        st.write(f"CP{i+1} : {ratio:.2f}")
    
    # Cercle des corrélations
    plt.figure(figsize=(8, 8))
    for i, nom_variable in enumerate(variables_quantitatives.columns):
        plt.arrow(0, 0, vecteurs_propres_tries[i, 0], vecteurs_propres_tries[i, 1], head_width=0.05, head_length=0.025, fc='blue', ec='blue')
        plt.text(vecteurs_propres_tries[i, 0] * 1.25, vecteurs_propres_tries[i, 1] * 1.25, nom_variable, color='blue')
    
    circle = plt.Circle((0, 0), 1, color='blue', fill=False)
    plt.gca().add_patch(circle)        
        
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel("Composante Principale 1")
    plt.ylabel("Composante Principale 2")
    plt.title("Cercle des corrélations")
    plt.grid(True)
    #plt.show() 
    # Afficher le graphique dans Streamlit
    st.pyplot(plt)


    #Graphique des individues


    
    # Calculer le ratio de variance expliquée
    ratio_variance_expliquee = valeurs_propres_triees / np.sum(valeurs_propres_triees)
    
    # Créer un graphique des individus
    plt.figure(figsize=(8, 6))
    plt.scatter(composantes_principales[:, 0], composantes_principales[:, 1], c='blue', marker='o')
    
    # Ajouter les noms des individus
    for i, nom in enumerate(acp_df["noms"]):
        plt.annotate(tradFR(nom), (composantes_principales[i, 0], composantes_principales[i, 1]))
    
    # Afficher les axes
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
    
    # Ajouter les labels des axes
    plt.xlabel("CP1")
    plt.ylabel("CP2")
    
    # Titre du graphique
    plt.title("Graphique des individus (ACP)")


    st.pyplot(plt)


