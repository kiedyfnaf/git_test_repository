import random
l = ['Ace in the Hole', 'Adrenaline', 'Aftercare', 'Alert', 'Any Means Necessary', 'Appraisal', 'Autodidact', 'Background Player', 'Balanced Landing', 'Better than New', 'Bite the Bullet', 'Blast Mine', 'Blood Pact', 'Blood Rush', 'Boil Over', 'Bond', 'Boon: Circle of Healing', 'Boon: Dark Theory', 'Boon: Exponential', 'Boon: Shadow Step', 'Borrowed Time', 'Botany Knowledge', 'Breakdown', 'Breakout', 'Buckle Up', 'Built to Last', 'Calm Spirit', 'Chemical Trap', 'Clairvoyance', 'Corrective Action', 'Counterforce', 'Cut Loose', 'Dance With Me', 'Dark Sense', 'Dead Hard', 'Deception', 'Decisive Strike', 'Deliverance', 'Desperate Measures', 'Detective Hunch', 'Distortion', 'Diversion', 'Dramaturgy', 'Déjà Vu', 'Empathic Connection', 'Empathy', 'Fast Track', 'Flashbang', 'Flip-Flop', 'Fogwise', 'For the People', 'Friendly Competition', 'Guardian', 'Head On', 'Hope', 'Hyperfocus', 'Inner Focus', 'Inner Healing', 'Iron Will', 'Kindred', 'Kinship', 'Leader', 'Left Behind', 'Light-Footed', 'Lightweight', 'Lithe', 'Low Profile', 'Lucky Break', 'Lucky Star', 'Made for This', 'Mettle of Man', 'No Mither', 'No One Left Behind', 'Object of Obsession', 'Off the Record', 'Open-Handed', 'Overcome', 'Overzealous', 'Parental Guidance', 'Pharmacy', 'Plot Twist', 'Plunderer Instinct', 'Poised', 'Potential Energy', 'Power Struggle', 'Premonition', 'Prove Thyself', 'Quick & Quiet', 'Quick Gambit', 'Reactive Healing', 'Reassurance', 'Red Herring', 'Renewal', 'Repressed Alliance', 'Residual Manifest', 'Resilience', 'Resurgence', 'Rookie Spirit', 'Saboteur', 'Scavenger', 'Scene Partner', 'Self-Aware', 'Self-Care', 'Self-Preservation', 'Situational Awareness', 'Slippery Meat', 'Small Game', 'Smash Hit', 'Sole Survivor', 'Solidarity', 'Soul Guard', 'Spine Chill', 'Sprint Burst', 'Stake Out', 'Streetwise', 'Teamwork: Collective Stealth', 'Teamwork: Power of Two', 'Technician', 'Tenacity', 'This Is Not Happening', 'Troubleshooter', 'Unbreakable', 'Up the Ante', 'Urban Evasion', 'Vigil', 'Visionary', 'Wake Up!', 'We will Make It', 'We are Gonna Live Forever', 'Windows of Opportunity', 'Wiretap', 'X', 'X', 'X', 'X', 'X', 'X']
k = ['A Nurse Calling', 'Agitation', 'Alien Instinct', 'Awakened Awareness', 'Bamboozle', 'Barbecue & Chilli', 'Beast of Prey', 'Bitter Murmur', 'Blood Echo', 'Blood Warden', 'Bloodhound', 'Brutal Strength', 'Call of Brine', 'Claustrophobia', 'Corrupt Intervention', 'Coulrophobia', 'Coup de Grâce', 'Dark Devotion', 'Darkness Revealed', 'Dead Man Switch', 'Deadlock', 'Deathbound', 'Deerstalker', 'Discordance', 'Dissolution', 'Distressing', 'Dragon Grip', 'Dying Light', 'Enduring', 'Eruption', 'Fearmonger', 'Fire Up', 'Forced Hesitation', 'Forced Penance', 'Franklin Demise', 'Furtive Chase', 'Game Afoot', 'Gearhead', 'Genetic Limits', 'Grim Embrace', 'Hex: Blood Favour', 'Hex: Crowd Control', 'Hex: Devour Hope', 'Hex: Face the Darkness', 'Hex: Haunted Ground', 'Hex: Huntress Lullaby', 'Hex: No One Escapes Death', 'Hex: Pentimento', 'Hex: Plaything', 'Hex: Retribution', 'Hex: Ruin', 'Hex: The Third Seal', 'Hex: Thrill of the Hunt', 'Hex: Undying', 'Hoarder', 'Hubris', 'Hysteria', 'Im All Ears', 'Infectious Fright', 'Insidious', 'Iron Grasp', 'Iron Maiden', 'Jolt', 'Knock Out', 'Lethal Pursuer', 'Leverage', 'Lightborn', 'Machine Learning', 'Mad Grit', 'Make Your Choice', 'Merciless Storm', 'Monitor & Abuse', 'Nemesis', 'No Way Out', 'Nowhere to Hide', 'Oppression', 'Overcharge', 'Overwhelming Presence', 'Play with Your Food', 'Pop Goes the Weasel', 'Predator', 'Rancor', 'Rapid Brutality', 'Remember Me', 'Save the Best for Last', 'Scourge Hook: Floods of Rage', 'Scourge Hook: Gift of Pain', 'Scourge Hook: Hangmans Trick', 'Scourge Hook: Monstrous Shrine', 'Scourge Hook: Pain Resonance', 'Septic Touch', 'Shadowborn', 'Shattered Hope', 'Sloppy Butcher', 'Spies from the Shadows', 'Spirit Fury', 'Starstruck', 'Stridor', 'Superior Anatomy', 'Surveillance', 'THWACK!', 'Terminus', 'Territorial Imperative', 'Thanatophobia', 'Thrilling Tremors', 'Tinkerer', 'Trail of Torment', 'Ultimate Weapon', 'Unnerving Presence', 'Unrelenting', 'Whispers', 'Zanshin Tactics', 'X', 'X', 'X', 'X', 'X', 'X']
m = random.choice(('Flashlight', 'Key', 'Map', 'Med-Kit', 'Toolbox'))
t = random.choice(('The MacMillan Estate', 'Autohaven Wreckers', 'Coldwind Farm', 'Crotus Prenn Asylum', 'Haddonfield', 'Backwater Swamp', 'Lérys Memorial Institute', 'Red Forest', 'Springwood', 'Gideon Meat Plant', 'Yamaoka Estate', 'Ormond', 'Hawkins National Laboratory', 'Grave of Glenvale', 'Silent Hill', 'Raccoon City', 'Forsaken Boneyard', 'Withered Isle', 'The Decimated Borgo', 'Dvarka Deepwood', 'Recurring Structures'))
p = random.choice(('Ace Visconti', 'Ada Wong', 'Adam Francis','Ashley J. Williams', 'Leon Scott Kennedy', 'Meg Thomas', 'Mikaela Reid', 'Nancy Wheeler', 'Nea Karlsson', 'Nicolas Cage', 'Quentin Smith', 'Rebecca Chambers', 'Renato Lyra', 'Steve Harrington', 'Thalita Lyra', 'Vittorio Toscano', 'William Bill Overbeck', 'Yoichi Asakawa', 'Yui Kimura', 'Yun-Jin Lee', 'Zarina Kassir', 'Élodie Rakoto', 'Cheryl Mason', 'Claudette Morel', 'David King', 'Detective David Tapp', 'Dwight Fairfield', 'Ellen Ripley', 'Felix Richter', 'Feng Min', 'Gabriel Soma', 'Haddie Kaur', 'Jake Park', 'Jane Romero', 'Jeffrey Jeff Johansen', 'Jill Valentine', 'Jonah Vasquez', 'Kate Denson', 'Laurie Strode'))
Flashlight = ['Wide Lens', 'Power Bulb', 'Leather Grip', 'Battery', 'TIR Optic', 'Rubber Grip', 'Low Amp Filament', 'Heavy Duty Battery', 'Focus Lens', 'Long Life Batter', 'Intense Halogen', 'High-End Sapphire Lens', 'Odd Bulb', 'X']
Key = ['Prayer Rope', 'Scratched Pearl', 'Prayer Beads', 'Eroded Token', 'Gold Token', 'Weaved Ring', 'Milky Glass', 'Blood Amber', 'Unique Wedding Ring', 'X', 'X']
Map = ['Map Addendum', 'Yellow Wire', 'Unusual Stamp', 'Retardant Jelly', 'Red Twine', 'Glass Bead', 'Odd Stamp', '	Black Silk Cord', 'Crystal Bead', 'X', 'X']
Med_Kit = ['Rubber Glov', 'Butterfly Tape', 'Bandages', 'Sponge', 'Self Adherent Wrap', 'Needle & Thread', 'Medical Scissors', 'Surgical Suture', 'Gauze Roll', 'Styptic Agent', 'Abdominal Dressing', 'Gel Dressings', 'Anti-Haemorrhagic Syringe', 'X', 'X']
Toolbox = ['Scraps', 'Instructions', 'Clean Rag', 'Wire Spool', 'Spring Clamp', 'Socket Swivels', 'Protective Gloves', 'Cutting Wire', 'Hacksaw', 'Grip Wrench', 'Brand New Part', 'X', 'X']
v = random.choice(('Trapper', 'Wraith', 'Nurse', 'Shape', 'Hag', 'Doctor', 'Huntress', 'Cannibal', 'Nightmare', 'Pig', 'Clown', 'Spirit', 'Legion', 'Plague', 'Ghost Face', 'Demogorgon', 'Oni', 'Deathslinger', 'Executioner', 'Blight', 'Twins', 'Trickster', 'Nemesis', 'Cenobite', 'Artist', 'Onryō', ' Dredge', 'Mastermind', 'Knight', 'Skull Merchant', 'Singularity', 'Xenomorph'))
Trapper = ['Trapper Gloves', 'Padded Jaws', 'Makeshift Wrap', 'Bear Oil', 'Wax Brick', 'Serrated Jaws', 'Lengthened Jaws', 'Coffee Grounds', '4-Coil Spring Kit', 'Trapper Bag', 'Tar Bottle', 'Secondary Coil', 'Rusted Jaws', 'Fastening Tools', 'Trapper Sack', 'Tension Spring', 'Oily Coil', 'Honing Stone', 'Iridescent Stone', 'Bloody Coil', 'X', 'X']
Wraith = ['The Serpent', 'The Hound', 'The Ghost', 'The Beast', 'Bone Clapper', 'Blink', 'Windstorm', 'Swift Hunt', 'Blind Warrior', 'Windstorm', 'Swift Hunt', 'Shadow Dance', 'Blink', 'Blind Warrior', 'Windstorm', 'Swift Hunt', 'Shadow Dance', 'All Seeing', 'Coxcombed Clapper', 'All Seeing', 'X', 'X']
Nurse = ['Wooden Horse', 'White Nit Comb', 'Plaid Flannel', 'Metal Spoon', 'Pocket Watch', 'Dull Bracelet', 'Dark Cincture', 'Catatonic Boys Treasure', 'Bad Man Keepsake', 'Spasmodic Breath', 'Heavy Panting', 'Fragile Wheeze', 'Ataxic Respiration', 'Anxious Gasp', 'Kavanaghs Last Breath', 'Jenners Last Breath', 'Campbells Last Breath', 'Bad Man Last Breath', 'Torn Bookmark', 'Matchbox', 'X', 'X']
Shape = ['Tacky Earrings', 'Memorial Flower', 'Boyfriends Memo', 'Blond Hair', 'Reflective Fragment', 'Jewellery', 'Hair Brush', 'Glass Fragment', 'Dead Rabbit', 'Mirror Shard', 'Judiths Journal', 'Jewellery Box', 'J. Myers Memorial', 'Hair Bow', 'Vanity Mirror', 'Tombstone Piece', 'Scratched Mirror', 'Lock of Hair', 'Judiths Tombstone', 'Fragrant Tuft of Hair', 'X', 'X']
Hag = ['Rope Necklet', 'Powdered Eggshell', 'Dead Fly Mud', 'Bog Water', 'Pussy Willow Catkins', 'Half Eggshell', 'Dragonfly Wings', 'Cypress Necklet', 'Bloodied Water', 'Willow Wreath', 'Swamp Orchid Necklet', 'Dried Cicada', 'Cracked Turtle Egg', 'Bloodied Mud', 'Scarred Hand', 'Rusty Shackles', 'Grandmas Heart', 'Disfigured Ear', 'Waterlogged Shoe', 'Mint Rag', 'X', 'X']
Doctor = ['Mouldy Electrode', 'Maple Knight', 'Order - class I', 'Calm - Class I', 'Polished Electrode', 'Restraint - class II', 'Order - Class II', 'Discipline - Class II', 'Calm - Class II', 'Scrapped Tape', 'Interview Tape', 'High Stimulus Electrode', 'Restraint - Class III', 'Discipline - Class III', 'Restraint - Carters Notes', 'Order - Carters Notes', 'Discipline - Carters Notes', 'Calm - Carters Notes', 'Iridescent Queen', 'Iridescent King', 'X']
Huntress = ['Yellowed Cloth', 'Coarse Stone', 'Bandaged Haft', 'Amanita Toxin', 'Weighted Head', 'Shiny Pin', 'Oak Haft', 'Manna Grass Braid', 'Leather Loop', 'Venomous Concoction', 'Rusty Head', 'Rose Root', 'Flower Babushka', 'Deerskin Gloves', 'Wooden Fox', 'Infantry Belt', 'Glowing Concoction', 'Begrimed Head', 'Soldiers Puttee', 'Iridescent Head', 'X', 'X']
Clown = ['VHS Porn', 'Robin Feather', 'Party Bottle', 'Fingerless Parade Gloves', 'Thick Cork Stopper', 'Sticky Soda Bottle', 'Starling Feather', 'Solvent Jug', 'Kerosene Can', 'Sulphuric Acid Vial', 'Spirit of Hartshorn', 'Smelly Inner Soles', 'Flask of Bleach', 'Bottle of Chloroform', 'Garish Make-Up Kit', 'Ether 15 Vol%', 'Cigar Box', 'Cheap Gin Bottle', 'Tattoos Middle Finger', 'Redheads Pinkie Finger', 'X', 'X']
Artist = ['Vibrant Obituary', 'Thick Tar', 'Oil Paints', 'Choclo Corn', 'Velvet Fabric', 'Untitled Agony', 'Still Life Crow', 'Festering Carrion', 'Automatic Drawing', 'Thorny Nest', 'Silver Bell', 'O Grief, O Lover', 'Darkest Ink', 'Charcoal Stick', 'Severed Tongue', 'Severed Hands', 'Matias Baby Shoes', 'Ink Egg', 'Iridescent Feather', 'Garden of Rot', 'X', 'X']
Blight = ['Placebo Tablet', 'Foxglove', 'Compound Seven', 'Chipped Monocle', 'Shredded Notes', 'Pustula Dust', 'Plague Bile', 'Canker Thorn', 'Blighted Rat', 'Umbra Salts', 'Rose Tonic', 'Compound Twenty-One', 'Blighted Crow', 'Adrenaline Vial', 'Vigos Journal', 'Summoning Stone', 'Soul Chemical', 'Alchemists Ring', 'Iridescent Blight Tag', 'Compound Thirty-Three', 'X', 'X']
Twins = ['Toy Sword', 'Tiny Fingernail', 'Soured Milk', 'Cat Figurine', 'Madeleines Glove', 'Ceremonial Candelabrum', 'Cats Eye', 'Bloody Black Hood', 'Baby Teeth', 'Weighty Rattle', 'Stale Biscuit', 'Sewer Sludge', 'Rusted Needle', 'Madeleines Scarf', 'Victors Soldier', 'Spinning Top', 'Forest Stew', 'Drop of Perfume', 'Silencing Cloth', 'Iridescent Pendant', 'X']
Cannibal = ['Vegetable Oil', 'Spark Plug', 'Speed Limiter', 'Chainsaw File', 'Long Guide Bar', 'Primer Bulb', 'Knife Scratches', 'Homemade Muffler', 'Chilli', 'The Grease', 'The Beasts Marks', 'Shop Lubricant', 'Grisly Chains', 'Begrimed Chains', 'Rusted Chains', 'Light Chassis', 'Depth Gauge Rake', 'Award-winning Chilli', 'Iridescent Flesh', 'Carburettor Tuning Guide', 'X', 'X']
Hillbilly = ['Steel Toe Boots', 'Junkyard Air Filter', 'Heavy Clutch', 'Speed Limiter', 'Dads Boots', 'Punctured Muffler', 'Off-Brand Motor Oil', 'Death Engravings', 'Big Buckle', 'Mothers Helpers', 'Low Kickback Chains', 'Leafy Mash', 'Doom Engravings', 'Black Grease', 'Tuned Carburettor', 'Spiked Boots', 'Pighouse Gloves', 'LoPro Chains', 'Apex Muffler', 'Iridescent Brick','X', 'X']
Onryō = ['Videotape Copy', 'Old Newspaper', 'Mothers Mirror', 'Cabin Sign', 'Yoichis Fishing Net', 'Well Stone', 'Sea-Soaked Cloth', 'Reikos Watch', 'Clump of Hair', 'Well Water', 'Ring Drawing', 'Rickety Pinwheel', 'Mothers Comb', 'Bloody Fingernails', 'VCR', 'Telephone', 'Tape Editing Deck', 'Distorted Photo', 'Remote Control', 'Iridescent Videotape', 'X', 'X']
Nightmare = ['Wool Shirt', 'Sheep Block', 'Kids Drawing', 'Garden Rake', 'Prototype Claws', 'Outdoor Rope', 'Nancys Sketch', 'Green Dress', 'Cat Block', 'Unicorn Block', 'Paint Thinner', 'Nancys Masterpiece', 'Jump Rope', 'Blue Dress', 'Pill Bottle', 'Swing Chains', 'Class Photo', 'Z Block', 'Red Paint Brush', 'Black Box', 'X', 'X']
Skull_Merchant = ['Ultrasonic Trap Speaker', 'High-Power Floodlight', 'High-Current Upgrade', 'Adi Valente Issue 1', 'Stereo Remote Mic', 'Shotgun Speakers', 'Supercharge', 'Low-Power Mode', 'Adaptive Lighting', 'Vital Targeting Processor', 'Powdered Glass', 'Loose Screw', 'Infrared Upgrade', 'Brown Noise Generator', 'Randomised Strobes', 'Geographical Readout', 'Prototype Rotor', 'Advanced Movement Prediction', 'Expired Batteries', 'Iridescent Unpublished Manuscript', 'X', 'X']
Legion = ['Smiley Face Pin', 'Scratched Ruler', 'Mischief List', 'Friendship Bracelet', 'Never-Sleep Pills', 'Mural Sketch', 'Julies Mix Tape', 'Etched Ruler', 'Defaced Smiley Pin', 'The Legion Pin', 'Susies Mix Tape', 'Stolen Sketch Book', 'Stylish Sunglasses', 'Joeys Mix Tape', 'Stab Wounds Study', 'Franks Mix Tape', 'Filthy Blade', 'BFFs', 'Iridescent Button', 'Fuming Mix Tape', 'X', 'X']
Knight = ['Tattered Tabard', 'Pillaged Mead', 'Map of the Realm', 'Gritty Lump', 'Treated Blade', 'Dried Horsemeat', 'Cold Steel Manacles', 'Call To Arms', 'Battle Axe Head', 'Town Watchs Torch', 'Ironworkers Tongs', 'Grim Iron Mask', 'Chain Mail Fragment', 'Broken Hilt', 'Lightweight Greaves', 'Healing Poultice', 'Flint and Steel', 'Blacksmiths Hammer', 'Iridescent Company Banner', 'Knights Contract', 'X', 'X'] 
Xenomorph = ['Ripleys Watch', 'Ovomorph', 'Drinking Bird', 'Cereal Rations', 'Light Wand', 'Lamberts Star Map', 'Crew Headset', 'Bretts Cap', 'Ashs Innards', 'Parkers Headband', 'Multipurpose Hatchet', 'Moulted Skin', 'Kanes Helmet', 'Emergency Helmet', 'Semiotic Keyboard', 'Self-Destruct Bolt','Harpoon Gun', 'Cat Carrier', 'Improvised Cattle Prod', 'Acidic Blood', 'X', 'X']
Pig = ['Shattered Syringe', 'Johns Medical File', 'Interlocking Razor', 'Combat Straps', 'Workshop Grease', 'Utility Blades', 'Razor Wires', 'Last Will', 'Face Mask', 'Slow-Release Toxin', 'Rusty Attachments', 'Jigsaws Annotated Plan', 'Bag of Gears', 'Tampered Timer', 'Jigsaws Sketch', 'Crate of Gears', 'Amandas Secret','Amandas Letter' ,'Video Tape', 'X', 'X']
Ghost_Face = ['Philly', 'Walleyes Matchbook', 'Headline Cut-Outs', 'Cheap Cologne', 'Telephoto Lens', 'Cinch Straps', 'Olsens Journal', 'Olsens Address Book', 'Marked Map', 'Olsens Wallet', 'Leather Knife Sheath', 'Lasting Perfume', 'Knife Belt Clip', 'Chewed Pen', 'Victims Detailed Routine', 'Night Vision Monocular', 'Drop-Leg Knife Sheath', 'Drivers License', 'Ghost Face Caught on Tape', 'Outdoor Security Camera', 'X', 'X']
Demogorgon = ['Rotten Pumpkin', 'Black Heart', 'Rat Liver', 'Rat Tail', 'Sticky Lining', 'Viscous Webbing', 'Rotten Green Tripe', 'Mews Guts', 'Barbs Glasses', 'Elevens Soda', 'Thorny Vines', 'Brass Case Lighter', 'Violet Waxcap', 'Deer Lung', 'Lifeguard Whistle', 'Vermilion Webcap', 'Upside Down Resin', 'Unknown Egg', 'Leprose Lichen', 'Red Moss', 'X', 'X']
Singularity = ['Nutritional Slurry', 'Kids Ball Glove', 'Heavy Water', 'Broken Security Key', 'Ultrasonic Sensor', 'Diagnostic Tool (Repair)', 'Cryo Gel', 'Cremated Remains', 'Android Arm', 'Spent Oxygen Tank', 'Nanomachine Gel', 'Live Wires', 'Hyperawareness Spray', 'Hologram Generator', 'Soma Family Photo', 'Foreign Plant Fibres', 'Diagnostic Tool (Construction', 'Crew Manifest', 'Iridescent Crystal Shard', 'Denied Requisition Form', 'X', 'X']
Deathslinger = ['Spit Polish Rag', 'Snake Oil', 'Rickety Chain', 'Modified Ammo Belt', 'Rusted Spike', 'Poison Oak Leaves', 'Marshals Badge', 'Jaw Smasher', 'Chewing Tobacco', 'Wardens Keys', 'Wanted Poster', 'Tin Oil Can', 'Honey Locust Thorn', 'Bayshores Gold Tooth', 'Prison Chain', 'Gold Creek Whiskey', 'Bayshores Cigar', 'Barbed Wire', 'Iridescent Coin', 'Hellshire Iron', 'X', 'X']
Dredge = ['Wooden Plank', 'Mortar and Pestle', 'Followers Cowl', 'Caffeine Tablets', 'Malthinkers Skull', 'Haddies Calendar', 'Fallen Shingle', 'Burnt Letters', 'Air Freshener', 'Worry Stone', 'War Helmet', 'Ottomarian Writing', 'Destroyed Pillow', 'Broken Doll', 'Tilling Blade', 'Lavalier Microphone', 'Field Recorder', 'Boat Key', 'Boat Key', 'Iridescent Wooden Plank', 'X', 'X']
Executioner = ['Lead Ring', 'Dead Butterfly', 'Copper Ring', 'Black Strap', 'Wax Doll', 'Spearhead', 'Leopard-Print Fabric', 'Forgotten Videotape', 'Cinderella Music Box', 'Valtiel Sect Photograph', 'Tablet of the Oppressor', 'Misty Day, Remains of Judgement', 'Mannequin Foot', 'Burning Man Painting', 'Scarlet Egg', 'Rust-Coloured Egg', 'Lost Memories Book', 'Crimson Ceremony Book', 'Obsidian Goblet', 'Iridescent Seal of Metatron', 'X', 'X']
Trickster = ['Trick Pouch', 'Memento Blades', 'Killing Part Chords', 'Inferno Wires', 'Tequila Moonrock', 'On Target Single', 'Lucky Blade', 'Ji-Woons Autograph', 'Caged Heart Shoes', 'Melodious Murder', 'Waiting For You Watch', 'Ripper Brace', 'Fizz-Spin Soda', 'Bloody Boa', 'Trick Blades', 'Edge of Revival Album', 'Diamond Cufflinks', 'Cut Thru U Single', 'Iridescent Photocard', 'Death Throes Compilation', 'X', 'X']
Cenobite = ['Leather Strip', 'Lively Crickets', 'Burning Candle', 'Bent Nail', 'Wriggling Maggots', 'Spoiled Meal', 'Skewered Rat', 'Liquified Gore', 'Flickering Television', 'Torture Pillar', 'Slice of Frank', 'Larrys Remains', 'Larrys Blood', 'Franks Heart', '	Original Pain', 'Impaling Wire', 'Greasy Black Len', 'Chatterers Tooth', 'Iridescent Lament Configuration', 'Engineers Fang', 'X', 'X']
Nemesis = ['Visitor Wristband', 'S.T.A.R.S. Field Combat Manual', 'Damaged Syringe', 'Brians Intestine', 'Zombie Heart', 'Mikhails Eye', 'Marvins Blood', 'Admin Wristband', 'Adrenaline Injector', 'Tyrant Gore', 'T-Virus Sample', 'Serotonin Injector', 'Plant 43 Vines', 'Licker Tongue', '	NE-a Parasite', 'Jills Sandwich', 'Depleted Ink Ribbon', 'Broken Recovery Coin', 'Shattered S.T.A.R.S. Badge', 'Iridescent Umbrella Badge', 'X', 'X']
Plague = ['Prayer Tablet Fragment', 'Olibanum Incense', 'Limestone Seal', 'Healing Salve', 'Prophylactic Amulet', 'Potent Tincture', 'Haematite Seal', 'Emetic Potion', 'Blessed Apple', 'Rubbing Oil', 'Infected Emetic', 'Incensed Ointment', 'Exorcism Amulet', 'Ashen Apple', 'Worship Tablet', 'Vile Emetic', 'Vile Emetic', 'Devotees Amulet', 'Iridescent Seal', 'Black Incense', 'X', 'X']
Mastermind = ['Jewel Beetle', 'Unicorn Medallion', 'R.P.D. Shoulder Walkie', 'Uroboros Tendril', 'Uroboros Tendril', 'Leather Gloves', 'Lion Medallion', '	Chalice (Gold)', 'Bullhorn', 'Portable Safe', 'Red Herb', 'Maiden Medallion', 'Video Conference Device', 'Egg (Gold)', 'Dark Sunglasses', 'Green Herb', 'Helicopter Stick', 'Uroboros Virus', 'Lab Photo', 'Iridescent Uroboros Vial', 'X', 'X']
Spirit = ['Zōri', '	Shiawase Amulet', 'Origami Crane', 'Gifted Bamboo Comb', 'White Hair Ribbon', '	Rins Broken Watch', 'Muddy Sports Day Cap', 'Kaiun Talisman', 'Juniper Bonsai', 'Rusty Flute', 'Senko Hanabi', 'Katana Tsuba', 'Uchiwa', 'Mothers Glasses', 'Yakuyoke Amulet', 'Wakizashi Saya', 'Furin', 'Dried Cherry Blossom', 'Mother-Daughter Ring', 'Kintsugi Teacup', 'X', 'X']
Oni = ['Rotting Rope', 'Paper Lantern', 'Cracked Sakazuki', 'Blackened Toenail', 'Polished Maedate', 'Ink Lion', 'Chipped Saihai', 'Childs Wooden Sword', 'Bloody Sash', 'Yamaoka Sashimono', 'Wooden Oni Mask', 'Shattered Wakizashi', 'Scalped Topknot', 'Kanai-Anzen Talisman', 'Tear Soaked Tenugui', 'Splintered Hull', 'Lion Fang', 'Akitos Crutch', 'Renjiros Bloody Glove', 'Iridescent Family Crest', 'X', 'X']
a = input("Ask kil or sur:   ")
if a == 'kil':
    print(f'Killer: [{v}]')
    print(f'Perks: {random.sample(k, 4)}')
    killer_addons = {
        'Trapper': Trapper,
        'Wraith': Wraith,
        'Nurse': Nurse,
        'Shape': Shape,
        'Hag': Hag,
        'Doctor': Doctor,
        'Huntress': Huntress,
        'Nightmare': Nightmare,
        'Pig': Pig,
        'Clown': Clown,
        'Spirit': Spirit,
        'Legion': Legion,
        'Plague': Plague,
        'Ghost Face': Ghost_Face,
        'Demogorgon': Demogorgon,
        'Oni': Oni,
        'Deathslinger': Deathslinger,
        'Cannibal': Cannibal,
        'Executioner': Executioner,
        'Hillbilly': Hillbilly,
        'Blight': Blight,
        'Twins': Twins,
        'Trickster': Trickster,
        'Nemesis': Nemesis,
        'Cenobite': Cenobite,
        'Artist': Artist,
        'Onryō': Onryō,
        'Dredge': Dredge,
        'Mastermind': Mastermind,
        'Knight': Knight,
        'Skull Merchant': Skull_Merchant,
        'Singularity': Singularity,
        'Xenomorph': Xenomorph,
    }
    addons = killer_addons.get(v)
    if addons:
        print(f'Add-ons: {random.sample(addons, 2)}')
    else:
        print('You for real?')
elif a == 'sur':
    print(f'Survivor: [{p}]')
    print(f'Perks:{random.sample(l, 4)}')
    print(f'Item: [{m}]')
    if m == 'Flashlight':
        print(f'Add-ons :{random.sample(Flashlight, 2)}')
    elif m == 'Map':
         print(f'Add-ons :{random.sample(Map, 2)}')
    elif m == 'Med_Kit':
         print(f'Add-ons :{random.sample(Med_Kit, 2)}')
    elif m == 'Key':
         print(f'Add-ons :{random.sample(Key, 2)}')
    elif m == 'Toolbox':
         print(f'Add-ons :{random.sample(Toolbox, 2)}')
elif a == 'map':
    print(f'Map: [{t}]')
else:
    print('Are you stupid?')












