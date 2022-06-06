import json

cachedTalents = {
	"captain": {
		"name": "captain",
		"count": 18,
		"trees": [
			{
				"name": "gunslinger",
				"talents": [
					{
						"name": "handsomestranger",
						"localizedName": "Once Upon a Time on Europa",
						"description": """Unlock recipe: Revolver Round.
Your crew's reputation gains are improved by 20%.
Whenever you gain Helm skill, also gain Weapons skill.
As long as your Helm skill is 100 or higher, they gain twice as much Weapons skill.""",
						"level": 1
					},
					{
						"name": "tumble",
						"localizedName": "Tumble",
						"description": """Whenever you ragdoll for at least 0.75 seconds, your attacks with pistols are 40% more powerful for the next 2.5 seconds.""",
						"level": 2
					},
					{
						"name": "quickdraw",
						"localizedName": "Quickdraw",
						"description": """If it has been longer than 8 seconds since you've attacked with a pistol, your next attack with a pistol is 40% more powerful.""",
						"level": 2
					},
					{
						"name": "sailorwithnoname",
						"localizedName": "Sailor with No Name",
						"description": """Unlock recipe: Cigar.
Gain a bonus of 20 to Medical.
Gain an additional 50% Chem addiction resistance.""",
						"level": 3
					},
					{
						"name": "drunkensailor",
						"localizedName": "Drunken Sailor",
						"description": """Gain 25% physical damage resistance and 50% stun resistance while drunk.
When you play a Harmonica, a random ally on your current submarine has a 4% chance to gain a random skill point every second.""",
						"level": 3
					},
					{
						"name": "bountyhunter",
						"localizedName": "Bounty Hunter",
						"description": """Unlock recipe: .
Whenever you or an allied crewmember kills a monster, your crew gains additional marks equal to 25% of the creature's maximum health.""",
						"level": 4
					}
				]
			},
			{
				"name": "skipper",
				"talents": [
					{
						"name": "travelingtradesman",
						"localizedName": "Traveling Tradesman",
						"description": """Your crew gains an additional 500 marks whenever you reach a new station.
Special sales offer 4 additional items.""",
						"level": 1
					},
					{
						"name": "evasivemaneuvers",
						"localizedName": "Evasive Maneuvers",
						"description": """Whenever your submarine takes damage from a monster, gain a bonus of 75 to the Helm skill for 5 seconds.
You are paid an additional 15% for monster and nest missions.""",
						"level": 1
					},
					{
						"name": "trustedcaptain",
						"localizedName": "Trusted Captain",
						"description": """Whenever you finish at least one mission, gain a Coalition Commendation.
When you apply a Coalition Commendation on another character, gain 275 experience.""",
						"level": 2
					},
					{
						"name": "trucker",
						"localizedName": "Trucker",
						"description": """Whenever you finish all your selected missions, gain an additional Coalition Commendation.
You are paid an additional 25% for cargo and escort missions.""",
						"level": 3
					},
					{
						"name": "downwiththeship",
						"localizedName": "Down with the Ship",
						"description": """If you are on your submarine and it becomes at least 50% flooded, you gain an additional 50% swimming speed and a bonus of 25 to Mechanical and Electrical skills for 60 seconds.""",
						"level": 3
					},
					{
						"name": "esteemedcaptain",
						"localizedName": "Esteemed Captain",
						"description": """Whenever you finish at least one mission, gain a Coalition Medal.
When you apply a Coalition Medal on another character, gain 750 experience.
You may select an additional mission.""",
						"level": 4
					}
				]
			},
			{
				"name": "shipmaster",
				"talents": [
					{
						"name": "commander",
						"localizedName": "Commander",
						"description": """Whenever you give an order to another character, apply Inspiration to that character, giving them 25% physical damage resistance and a bonus of 10 to all skills.
Giving an order to a new character removes the effect from the last character.""",
						"level": 1
					},
					{
						"name": "trustbuilding",
						"localizedName": "Trust Building",
						"description": """Whenever you finish a mission, your crew gains an additional 2.5% maximum health, and if all crewmembers survived, your crew gains an additional 5% maximum health instead, up to a maximum of 25%.
This bonus is lost on death.
The deaths of assistants do not count.""",
						"level": 2
					},
					{
						"name": "maintenanceroutine",
						"localizedName": "Maintenance Routine",
						"description": """In addition to other Inspiration bonuses, the ordered character also gains the following attributes:
+20% Repair Speed
+20% Hull Repair Speed
+35% Skill Gain Speed""",
						"level": 2
					},
					{
						"name": "camaraderie",
						"localizedName": "Camaraderie",
						"description": """Whenever you finish a mission without a crewmember dying, and your crew contains at least 5 different jobs, your crew gains an additional 20% money and experience.
The deaths of assistants do not count.""",
						"level": 3
					},
					{
						"name": "inspiretobattle",
						"localizedName": "Inspire to Battle",
						"description": """In addition to other Inspiration bonuses, the ordered character also gains the following attributes:
+30% Stun resistance
+30% Melee Attack Speed
+20% Ranged Fire Rate
+20% Turret Fire Rate""",
						"level": 3
					},
					{
						"name": "allhandsondeck",
						"localizedName": "All Hands on Deck",
						"description": """You may bestow an additional character with Inspiration effects.
You may select an additional mission.""",
						"level": 4
					}
				]
			}
		]
	},
	"securityofficer": {
		"name": "securityofficer",
		"count": 19,
		"trees": [
			{
				"name": "specialist",
				"talents": [
					{
						"name": "firstaidtraining",
						"localizedName": "First Aid Training",
						"description": """Gain a bonus of 15 to Medical.
Medical items are 35% more potent when applied to you.""",
						"level": 1
					},
					{
						"name": "physicalconditioning",
						"localizedName": "Physical Conditioning",
						"description": """Gain an additional 25% Melee Attack Speed.
Gain an additional 15% Movement Speed.
Gain an additional 40% Oxygen low resistance.""",
						"level": 1
					},
					{
						"name": "navydiver",
						"localizedName": "Navy Diver",
						"description": """Unlock recipe: Slipsuit.
Attacks you suffer are 25% less powerful while you are in water.""",
						"level": 2
					},
					{
						"name": "scavenger",
						"localizedName": "Scavenger",
						"description": """Whenever you open a container outside your submarine for the first time, you have a 20% chance of finding additional items.
Gain an additional 50% Buff Duration.""",
						"level": 2
					},
					{
						"name": "buccaneer",
						"localizedName": "Buccaneer",
						"description": """Aiming with a melee weapon before attacking adds up to 100% power to your next melee attack.
Gain an additional 25% Stun resistance.
Unlock recipe: Boarding Axe.""",
						"level": 3
					},
					{
						"name": "deepseaslayer",
						"localizedName": "Deep Sea Slayer",
						"description": """Gain an additional 25% attack power to harpoons.
If you are in the open sea, gain an additional 50% attack power to harpoons instead.
When you kill a monster while outside your submarine, it has a 40% chance of having an additional alien material.""",
						"level": 3
					},
					{
						"name": "dualspecops",
						"localizedName": "Dual Spec-Ops",
						"description": """When you ragdoll in water, propel yourself forward in your current direction.
Gain 2 free additional talent points.""",
						"level": 4
					}
				]
			},
			{
				"name": "warden",
				"talents": [
					{
						"name": "enforcer",
						"localizedName": "Enforcer",
						"description": """Unlock recipe: Shotgun Shell.
Gain an additional 25% Maximum Health.""",
						"level": 1
					},
					{
						"name": "beatcop",
						"localizedName": "Beat Cop",
						"description": """You can tackle other characters by ragdolling into them at high speeds.
Inflict 25% more stun.
Gain an additional 25% Repair Speed.""",
						"level": 2
					},
					{
						"name": "munitionsexpertise",
						"localizedName": "Munitions Expertise",
						"description": """Unlock recipe: Explosive Slug.
Gain 125% more Weapons skill from fabricating items.
Whenever you fabricate SMG ammo, shotgun ammo or stun gun ammo, you have a 50% chance to gain twice as much output.""",
						"level": 2
					},
					{
						"name": "stonewall",
						"localizedName": "Stonewall",
						"description": """Whenever you are attacked, gain an additional 30% physical damage resistance and 30% stun resistance for 4 seconds.""",
						"level": 3
					},
					{
						"name": "bythebook",
						"localizedName": "By the Book",
						"description": """Unlock recipe: Fulgurium Stun Gun Dart.
Whenever you finish at least one mission, your crew gains an additional 1250 marks and 200 experience for each captured, live enemy human on board your ship, up to a maximum of 2500 marks and 400 experience.""",
						"level": 3
					},
					{
						"name": "implacable",
						"localizedName": "Implacable",
						"description": """Unlock recipe: Autoshotgun.
Whenever you fall below 0 health, you will remain fully conscious and your attacks are 25% more powerful for 15 seconds.
This effect can only occur once per life each round.""",
						"level": 4
					}
				]
			},
			{
				"name": "soldier",
				"talents": [
					{
						"name": "bootcamp",
						"localizedName": "Bootcamp",
						"description": """Unlock recipe: SMG Magazine.
Whenever you finish a mission without a crewmember dying, you gain an additional 35% experience.
The deaths of assistants do not count.""",
						"level": 1
					},
					{
						"name": "warriorpoet",
						"localizedName": "Warrior Poet",
						"description": """You can write a book.
To do this, ragdoll yourself. After 15 seconds, you will gain the item Art of Submarine Warfare and 100 marks for each enemy you've killed since your last book (as royalties).
This effect cannot occur again until you finish another mission.""",
						"level": 2
					},
					{
						"name": "gunsmith",
						"localizedName": "Gunsmith",
						"description": """Unlock recipe: Bandolier.
Weapons you fabricate are of 1 higher quality.""",
						"level": 2
					},
					{
						"name": "commando",
						"localizedName": "Expert Commando",
						"description": """When firing a ranged weapon while crouched, you gain 70% reduction to spread and your attacks are 25% more powerful, but your firing rate is 30% slower.
Recover from bleeding much more quickly.""",
						"level": 3
					},
					{
						"name": "tandemfire",
						"localizedName": "Tandem Fire",
						"description": """As long as you are manning a turret alongside another allied crewmember, both of your attacks are 25% more powerful. Only the closest allied crewmember gains this effect.""",
						"level": 3
					},
					{
						"name": "warlord",
						"localizedName": "Warlord",
						"description": """Unlock recipe: .
Whenever you attack with any weapon, your attack has a 5% chance of becoming twice as powerful.""",
						"level": 4
					}
				]
			}
		]
	},
	"assistant": {
		"name": "assistant",
		"count": 19,
		"trees": [
			{
				"name": "jackofalltrades",
				"talents": [
					{
						"name": "multitasker",
						"localizedName": "Multitasker",
						"description": """Whenever you gain a skill point, if it’s not for the same skill as the last skill point gained, gain an additional skill point.
Gain an additional 20% Repair Speed.""",
						"level": 1
					},
					{
						"name": "apprenticeship",
						"localizedName": "Apprenticeship",
						"description": """Whenever another allied character gains a skill point, you have a 20% chance to also gain a skill point in that skill.
Gain an additional 15% Maximum Health.""",
						"level": 1
					},
					{
						"name": "standanddeliver",
						"localizedName": "Stand and Deliver",
						"description": """Whenever you finish at least one mission, gain 'The Sailor's Guide'.
Whenever you use 'The Sailor's Guide', the ally nearest to you gains 4 to all skills.""",
						"level": 2
					},
					{
						"name": "richinknowledge",
						"localizedName": "Rich in Knowledge",
						"description": """Whenever you gain a skill point, gain an additional 20 experience, while your allied crewmembers gain 10 experience.
This effect can only occur up to 15 times until you finish another mission.""",
						"level": 3
					},
					{
						"name": "aceofalltrades",
						"localizedName": "Ace of All Trades",
						"description": """Gain a bonus of 15 to all skills.
Gain 15 marks when you gain a skill point.""",
						"level": 3
					},
					{
						"name": "olympian",
						"localizedName": "Olympian",
						"description": """You can gain skills past their ordinary maximum.""",
						"level": 4
					}
				]
			},
			{
				"name": "grayshirt",
				"talents": [
					{
						"name": "playingcatchup",
						"localizedName": "Playing Catchup",
						"description": """If you are 2 or more levels behind your most highest-leveled crewmember, gain an additional 100% mission experience.""",
						"level": 1
					},
					{
						"name": "skedaddle",
						"localizedName": "Skedaddle",
						"description": """Move 10% faster. When you are attacked, this bonus is increased to 30% for 5 seconds.
Gain an additional 30% Stun resistance.""",
						"level": 1
					},
					{
						"name": "survivalpackage",
						"localizedName": "Survival Package",
						"description": """Enemies will ignore you if you have been ragdolled for longer than 4 seconds.
1x Morphine
1x Bandage
1x Blood Pack""",
						"level": 2
					},
					{
						"name": "crewlayabout",
						"localizedName": "Crew Layabout",
						"description": """Lose 40% Repair Speed.
Suffer a reduction of 15 to all skills.
Allies near you repair 25% faster and gain a bonus of 10 to all skills.""",
						"level": 2
					},
					{
						"name": "insurancepolicy",
						"localizedName": "Insurance Policy",
						"description": """Whenever you die from non-friendly sources during a mission, your crew is paid 700 marks for each mission you've completed since the last time you've died.""",
						"level": 3
					},
					{
						"name": "stillkicking",
						"localizedName": "Still Kicking",
						"description": """Whenever you fall below 0 health, rapidly heal normal damage types and remove stun over a short duration.
This effect can only occur once per life each round.""",
						"level": 3
					},
					{
						"name": "graduationceremony",
						"localizedName": "Graduation Ceremony",
						"description": """Upon creating a new character, retain all of your current experience for that new character.
Gain an additional 10% maximum health for each of your levels.""",
						"level": 4
					}
				]
			},
			{
				"name": "clown",
				"talents": [
					{
						"name": "enrollintoclowncollege",
						"localizedName": "Enroll into Clown College",
						"description": """As long as you are wearing a full clown outfit, you gain Clown Power.
Clown Power allows you to honk your horn to give nearby allies an additional 30% skill gain for a short while.
Clown Power gives you an additional 25% physical damage resistance.""",
						"level": 1
					},
					{
						"name": "waterprankster",
						"localizedName": "Water Prankster",
						"description": """Unlock recipe: Clown Diving Mask.
Clown Power gives you immunity to pressure and allows you to swim 50% faster.""",
						"level": 2
					},
					{
						"name": "inspiringtunes",
						"localizedName": "Inspiring Tunes",
						"description": """Clown Power allows you to honk your horn to repair nearby electrical and mechanical items, and nearby allies to gain a bonus of 15 to all skills for a short while.""",
						"level": 2
					},
					{
						"name": "psychoclown",
						"localizedName": "Psycho Clown",
						"description": """Clown Power allows you to attack faster with melee weapons based on how much Psychosis you have, up to 150%, but you cannot run while having Psychosis.""",
						"level": 3
					},
					{
						"name": "slapstickexpert",
						"localizedName": "Slapstick Expert",
						"description": """Clown Power allows you to have a small chance to trip randomly when you run.
While ragdolled, Clown Power allows you to reduce the power of incoming attacks by 50%, and characters that attack you have a 50% chance of becoming stunned for 4 seconds.""",
						"level": 3
					},
					{
						"name": "truepotential",
						"localizedName": "True Potential",
						"description": """Clown Power allows you to honk your horn to slowly heal nearby allies.
Clown Power allows you to hit characters with a Toy Hammer for a 0.75% chance to implode them.
Clown Power gives you an additional 25% physical damage resistance.""",
						"level": 4
					}
				]
			}
		]
	},
	"engineer": {
		"name": "engineer",
		"count": 19,
		"trees": [
			{
				"name": "weaponsengineer",
				"talents": [
					{
						"name": "militaryapplications",
						"localizedName": "Military Applications",
						"description": """Unlock recipe: .
Gain a bonus of 20 to Weapons.""",
						"level": 1
					},
					{
						"name": "strengthenedalloys",
						"localizedName": "Strengthened Alloys",
						"description": """Unlock recipe: .
Gain a bonus of 20 to Mechanical Engineering.""",
						"level": 2
					},
					{
						"name": "armsdealer",
						"localizedName": "Arms Dealer",
						"description": """Unlock recipe: Depleted Fuel SMG Magazine,
Depleted Fuel Revolver Round.
Whenever you finish at least one mission, gain the following items as an additional reward:
4x Magnesium
2x Steel Bar
2x Copper""",
						"level": 2
					},
					{
						"name": "expandedresearch",
						"localizedName": "Expanded Research",
						"description": """Whenever you or another allied crewmember deconstructs depleted fuel, they gain 200 experience.
This effect can only occur up to 3 times until you finish another mission.""",
						"level": 3
					},
					{
						"name": "castledoctrine",
						"localizedName": "Castle Doctrine",
						"description": """Unlock recipe: Dirty Bomb.
Your attacks are 35% more powerful against monsters inside your submarine.""",
						"level": 3
					},
					{
						"name": "nuclearoption",
						"localizedName": "Nuclear Option",
						"description": """Unlock recipe: Rapid Fissile Accelerator.
When you fabricate a fuel rod, gain triple output.
This effect cannot occur again until you finish another mission.
Gain an additional 100% Nausea resistance.""",
						"level": 4
					}
				]
			},
			{
				"name": "electrician",
				"talents": [
					{
						"name": "minorinmechanics",
						"localizedName": "Minor in Mechanics",
						"description": """Unlock recipe: Handheld Electrical Monitor.
Whenever you gain Electrical Engineering skill, also gain Mechanical Engineering skill.
As long as your Electrical Engineering skill is 100 or higher, they gain twice as much Mechanical Engineering skill.""",
						"level": 1
					},
					{
						"name": "justascratch",
						"localizedName": "Just a scratch",
						"description": """When you are below 50% health, normal damage types slowly heal by themselves.""",
						"level": 1
					},
					{
						"name": "melodicrespite",
						"localizedName": "Melodic Respite",
						"description": """When you play a guitar, you and allies near you gain the following attributes for up to 480 seconds:
+15% Attack Power
+15% Repair Speed
+15% Physical damage resistance""",
						"level": 2
					},
					{
						"name": "intheflow",
						"localizedName": "In the Flow",
						"description": """Whenever you fully repair a device, repair 70% faster for the next 7 seconds.""",
						"level": 2
					},
					{
						"name": "electrochemist",
						"localizedName": "Electrochemist",
						"description": """Batteries you fabricate are of 1 higher quality.
If you have not been attacked for 10 seconds, the next attack you suffer has 80% less power and your attacker is stunned for 4 seconds.""",
						"level": 3
					},
					{
						"name": "optimizedpowerflow",
						"localizedName": "Optimized Power-Flow",
						"description": """Gain an additional percentage to Turret Power Cost Reduction and Turret Charge Speed equal to 50% of your Electrical skill.
Whenever you fully repair an item, gain a bonus of 1 to Electrical.
This talent can only give up to 100 skill bonus.
This bonus is lost on death.""",
						"level": 3
					},
					{
						"name": "allseeingeye",
						"localizedName": "All-Seeing Eye",
						"description": """Unlock recipe: Thermal Goggles.
Gain all the talents in this talent tree.""",
						"level": 4
					}
				]
			},
			{
				"name": "physicist",
				"talents": [
					{
						"name": "remotemonitor",
						"localizedName": "Remote Monitor",
						"description": """Unlock recipe: Reactor PDA.
Fuel rods you fabricate are of 1 higher quality.
Gain a bonus of 15 to Electrical Engineering.""",
						"level": 1
					},
					{
						"name": "coauthor",
						"localizedName": "Co-Author",
						"description": """You can co-write a book with a Mechanic.
To do this, select their character and have them select yours. After 10 seconds, you will gain The Handy Seaman, and both of you gain 150 experience.
This effect cannot occur again until you finish another mission.""",
						"level": 2
					},
					{
						"name": "hazardousmaterials",
						"localizedName": "Hazardous Materials",
						"description": """Unlock recipe: Volatile Fulgurium Fuel Rod.
Whenever you loot a reactor in a wreck for the first time, you will find rare materials.""",
						"level": 2
					},
					{
						"name": "collegeathletics",
						"localizedName": "College Athletics",
						"description": """Unlock recipe: Cargo Scooter.
Gain an additional 35% Maximum Health.
Gain an additional 30% Swimming Speed.
Gain an additional 20% Walking Speed.""",
						"level": 3
					},
					{
						"name": "polymath",
						"localizedName": "Polymath",
						"description": """Gain a bonus of 20 to all skills, and you gain 65% more mission experience, but you have 25% less maximum health.""",
						"level": 3
					},
					{
						"name": "phdinnuclearphysics",
						"localizedName": "Ph.D in Nuclear Physics",
						"description": """Unlock recipe: PUCS.
Your attacks with crowbars are 140% more powerful.
As long as your electrical skill is 100 or higher, you can repair electrical devices 40% past their maximum condition.""",
						"level": 4
					}
				]
			}
		]
	},
	"mechanic": {
		"name": "mechanic",
		"count": 18,
		"trees": [
			{
				"name": "machinist",
				"talents": [
					{
						"name": "tinkerer",
						"localizedName": "Tinkerer",
						"description": """You can use a wrench to tinker with devices.

You can tinker with a pump, increasing its pumping rate by 400%.
You can tinker with an engine, increasing its torque by 150%.
You can tinker with a loader, increasing the connected turret's firing rate and damage by 20%, while lowering its power usage by 20%.

The device is only affected for as long as you keep tinkering with it.
You can tinker for 10 seconds. After you have tinkered with a device, you cannot tinker for 25 seconds.""",
						"level": 1
					},
					{
						"name": "quickfix",
						"localizedName": "Quickfix",
						"description": """Unlock recipe: Repair Pack.
Whenever you fully repair a device, gain 40 experience.
This effect can only occur up to 8 times until you finish another mission.""",
						"level": 2
					},
					{
						"name": "massproduction",
						"localizedName": "Mass Production",
						"description": """You can tinker with a fabricator or a deconstructor, increasing their operating rate by 250%.
You can tinker with fabricators and deconstructors indefinitely.
Gain 75% more skill from fabricating items.""",
						"level": 2
					},
					{
						"name": "hullsealer",
						"localizedName": "Hull Sealer",
						"description": """Unlock recipe: Fixfoam Grenade.
You can tinker for an additional 5 seconds.""",
						"level": 3
					},
					{
						"name": "overclocking",
						"localizedName": "Overclocking",
						"description": """Tinkering with items damages them, but the effects of tinkering are increased by 50%.
The cooldown period of tinkering is reduced to 12.5 seconds.""",
						"level": 3
					},
					{
						"name": "letitdrain",
						"localizedName": "Let It Drain",
						"description": """Unlock recipe: Portable Pump.
You can only install a maximum of 2 of this item on your submarine.
Non-turret devices you tinker with will always function as if they had power.""",
						"level": 4
					}
				]
			},
			{
				"name": "technician",
				"talents": [
					{
						"name": "safetyfirst",
						"localizedName": "Safety First",
						"description": """Unlock recipe: Safety Harness.
Whenever you gain Mechanical Engineering skill, also gain Electrical Engineering skill.
As long as your Mechanical Engineering skill is 100 or higher, they gain twice as much Electrical Engineering skill.""",
						"level": 1
					},
					{
						"name": "aggressiveengineering",
						"localizedName": "Aggressive Engineering",
						"description": """When you attack with a wrench, you have a 30% chance to attack with 200% additional power and inflict an additional stun.
You can repair mechanical devices 20% past their normal maximum condition.""",
						"level": 1
					},
					{
						"name": "hullfixer",
						"localizedName": "Hull Fixer",
						"description": """Unlock recipe: Handheld Status Monitor.
Welding tools and plasma cutters you fabricate are 1 higher quality.
Repair hulls 25% faster with welding tools.""",
						"level": 2
					},
					{
						"name": "crisismanagement",
						"localizedName": "Crisis Management",
						"description": """The more filled with water your submarine is, the faster you repair devices and swim, up to an additional 75% repair speed and 75% swimming speed.""",
						"level": 3
					},
					{
						"name": "pyromaniac",
						"localizedName": "Pyromaniac",
						"description": """When you inflict burning damage on an enemy, gain 40% physical damage resistance for 5 seconds.
Inflict 25% more burning damage.""",
						"level": 3
					},
					{
						"name": "artisansmith",
						"localizedName": "Artisan Smith",
						"description": """Unlock recipe: .
Tools you fabricate are of 1 higher quality.
Gain a bonus of 30 to Mechanical Engineering.""",
						"level": 4
					}
				]
			},
			{
				"name": "pioneer",
				"talents": [
					{
						"name": "scrounger",
						"localizedName": "Scrounger",
						"description": """Whenever you open a container in a wreck for the first time, you have a 40% chance of finding an additional scrap.
When you deconstruct scrap, gain 50 experience.
Force doors open 50% faster.""",
						"level": 1
					},
					{
						"name": "miner",
						"localizedName": "Miner",
						"description": """Whenever you deconstruct an ore, you have a 50% chance to gain double the output.
Deal 100% more damage to structures with cutters.
Detach ores 100% faster with cutters.""",
						"level": 2
					},
					{
						"name": "demolitionsexpert",
						"localizedName": "Demolitions Expert",
						"description": """Gain a bonus of 25 to Weapons.
Explosives you fabricate are of 1 higher quality.""",
						"level": 2
					},
					{
						"name": "cannedheat",
						"localizedName": "Canned Heat",
						"description": """Fuel and oxygen tanks you fabricate are of 1 higher quality.
Whenever you play an accordion, the ally nearest to you will gain 15 experience every second. When they do, you gain 10 experience.
This effect can only occur up to 20 times until you finish another mission.""",
						"level": 3
					},
					{
						"name": "elbowgrease",
						"localizedName": "Elbow Grease",
						"description": """Gain an additional percentage to Melee Power and Maximum Health equal to 40% of your Mechanical skill.
Whenever you deconstruct scrap, gain a bonus of 3 to Mechanical.
This talent can only give up to 100 skill bonus.
This bonus is lost on death.""",
						"level": 3
					},
					{
						"name": "scrapsavant",
						"localizedName": "Scrap Savant",
						"description": """You can refine 3 scrap to any alien material.
Gain 150 experience when you fabricate an alien material.
Whenever you open a container in a wreck for the first time, you have a 80% chance of finding an additional scrap.""",
						"level": 4
					}
				]
			}
		]
	},
	"medicaldoctor": {
		"name": "medicaldoctor",
		"count": 19,
		"trees": [
			{
				"name": "xenologist",
				"talents": [
					{
						"name": "researchersintuition",
						"localizedName": "Researcher's Intuition",
						"description": """Whenever you open an alien container for the first time, you have a 50% chance of finding additional items.
While you are holding a large alien artifact, gain an additional 50% Swimming Speed.""",
						"level": 1
					},
					{
						"name": "curiosity",
						"localizedName": "Curiosity",
						"description": """Whenever you deconstruct an alien artifact, you and another random allied crewmember gains 150 experience. Small alien artifacts, when deconstructed, give 50 experience instead.""",
						"level": 2
					},
					{
						"name": "doubleduty",
						"localizedName": "Double Duty",
						"description": """As long as you are outside your sub, take 25% less physical damage. As long as you are inside your submarine, gain a bonus of 20 to Medicine.""",
						"level": 2
					},
					{
						"name": "alienhoarder",
						"localizedName": "Alien Hoarder",
						"description": """Your attacks with alien pistols have 8% additional power for each alien artifact you are carrying, up to an additional 40% power.
Gain an additional 50% Psychosis resistance.""",
						"level": 3
					},
					{
						"name": "reverseengineer",
						"localizedName": "Reverse Engineer",
						"description": """Whenever you deconstruct an alien artifact, you have a 50% chance to gain double output from it and gain 8 to a random skill. Small alien artifacts, when deconstructed, give 4 skill instead.""",
						"level": 3
					},
					{
						"name": "atmosmachine",
						"localizedName": "Atmos Machine",
						"description": """When you deconstruct an alien artifact, there is a 20% chance it will instead transform into a random alien item.
Whenever you finish a mission, your crew gains 10% additional mission experience for each large alien artifact on board your ship, up to 20%.
Gain an additional 150% Deconstructor Speed.""",
						"level": 4
					}
				]
			},
			{
				"name": "medic",
				"talents": [
					{
						"name": "fieldmedic",
						"localizedName": "Field Medic",
						"description": """Whenever you complete a mission, if all crewmembers survived, gain 3 points in Medical skill.
The deaths of assistants do not count.
Gain an additional 20% Maximum Health.""",
						"level": 1
					},
					{
						"name": "mechanicscourse",
						"localizedName": "Mechanics Course",
						"description": """Unlock recipe: Auto-Injector Headset.
Gain a bonus of 20 to Mechanical Engineering.""",
						"level": 2
					},
					{
						"name": "firemanscarry",
						"localizedName": "Fireman's Carry",
						"description": """You can drag characters at full speed.
Gain an additional 50% Burn resistance.""",
						"level": 2
					},
					{
						"name": "bedsidemanner",
						"localizedName": "Bedside Manner",
						"description": """Whenever you apply medicine to a friendly character, they gain 20 physical damage resistance and an additional 25% skill gain, the total duration depending on your medical skill.""",
						"level": 3
					},
					{
						"name": "combatmedic",
						"localizedName": "Combat Medic",
						"description": """Unlock recipe: Combat Stimulant.
Gain an additional percentage to Movement Speed, Ranged Fire Rate and Melee Attack Speed equal to 30% of your medical skill.""",
						"level": 3
					},
					{
						"name": "dontdieonme",
						"localizedName": "Don't Die on Me!",
						"description": """Unlock recipe: Endocrine Booster.
The CPR you apply is much more powerful.""",
						"level": 4
					}
				]
			},
			{
				"name": "scientist",
				"talents": [
					{
						"name": "drsubmarine",
						"localizedName": "Dr. Submarine",
						"description": """Using medical items while crouched also applies 50% of the effects on you as well.
Gain an additional 35% Opiate addiction resistance.""",
						"level": 1
					},
					{
						"name": "genetherapist",
						"localizedName": "Gene Therapist",
						"description": """Refining genetic materials adds an additional 10% to their potency.
Medical items you apply are 25% more potent.""",
						"level": 1
					},
					{
						"name": "researchgrant",
						"localizedName": "Research Grant",
						"description": """Unlock recipe: Pressure Stabilizer.
Whenever you refine or combine genetic items, gain 300 marks.""",
						"level": 2
					},
					{
						"name": "researchanddevelopment",
						"localizedName": "Research and Development",
						"description": """Whenever you finish a mission without a crewmember dying, you gain an additional 45% experience and gain the item Europan Medicine.
The deaths of assistants do not count.""",
						"level": 2
					},
					{
						"name": "geneharvester",
						"localizedName": "Gene Harvester",
						"description": """When you or another crewmember kills a monster while outside your submarine, you have a 35% chance of finding a random genetic material on it.""",
						"level": 3
					},
					{
						"name": "geneticstability",
						"localizedName": "Genetic Stability",
						"description": """Combining different types of genetic materials is 50% less likely to taint the materials.
Gain a bonus of 15 to all skills.""",
						"level": 3
					},
					{
						"name": "advancedsplicing",
						"localizedName": "Advanced Splicing",
						"description": """Unlock recipe: Advanced Gene Splicer.
Whenever you or another allied crewmember combines or refines genetic materials, gain 125 experience and a bonus of 5 to medical.
This talent can only give up to 100 skill bonus.
This bonus is lost on death.""",
						"level": 4
					}
				]
			}
		]
	}
}


def get():
	return json.dumps(cachedTalents)
