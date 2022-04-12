#    This file contains the configuration for computing the detailed top stats in arcdps logs as parsed by Elite Insights.
#    Copyright (C) 2021 Freya Fleckenstein
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

stats_to_compute = ['deaths', 'dmg', 'dmg_taken', 'rips', 'cleanses', 'superspeed', 'dist', 'stability', 'protection', 'aegis', 'might', 'fury', 'resistance', 'resolution', 'quickness', 'swiftness', 'alacrity', 'vigor', 'regeneration']

# How many players will be listed who achieved top stats most often for each stat?
num_players_listed = {'dmg': 1000, 'rips': 1000, 'cleanses': 1000, 'dist': 1000, 'stability': 1000, 'protection': 1000, 'aegis': 1000, 'might': 1000, 'fury': 1000, 'dmg_taken': 1000, 'deaths': 1000, 'superspeed': 1000, 'resistance': 1000, 'resolution': 1000, 'quickness': 1000, 'swiftness': 1000, 'alacrity': 1000, 'vigor': 1000, 'regeneration': 1000}
# How many players are considered to be "top" in each fight for each stat?
num_players_considered_top = {'dmg': 5, 'rips': 5, 'cleanses': 5, 'dist': 5, 'stability': 5, 'protection': 5, 'aegis': 5, 'might': 5, 'fury': 5, 'dmg_taken': 5, 'deaths': 1, 'superspeed': 5, 'resistance': 5, 'resolution': 5, 'quickness': 5, 'swiftness': 5, 'alacrity': 5, 'vigor': 5, 'regeneration': 5}


# For what portion of all fights does a player need to be there to be considered for "consistency percentage" awards?
attendance_percentage_for_percentage = 50
# For what portion of all fights does a player need to be there to be considered for "late but great" awards?
attendance_percentage_for_late = 50
# For what portion of all fights does a player need to be there to be considered for "jack of all trades" awards? 
attendance_percentage_for_buildswap = 30
# For what portion of all fights does a player need to be there to be considered for "top average" awards? 
attendance_percentage_for_average = 33

# What portion of the top total player stat does someone need to reach to be considered for total awards?
percentage_of_top_for_consistent = 25
# What portion of the total stat of the top consistent player does someone need to reach to be considered for consistency awards?
percentage_of_top_for_total = 25
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for percentage awards?
percentage_of_top_for_percentage = 25
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for late but great awards?
percentage_of_top_for_late = 100
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for jack of all trades awards?
percentage_of_top_for_buildswap = 100

# minimum number of allied players to consider a fight in the stats
min_allied_players = 10
# minimum duration of a fight to be considered in the stats
min_fight_duration = 30
# minimum number of enemies to consider a fight in the stats
min_enemy_players = 10

# names as which each specialization will show up in the stats
profession_abbreviations = {}
profession_abbreviations["Guardian"] = "Guardian"
profession_abbreviations["Dragonhunter"] = "Dragonhunter"
profession_abbreviations["Firebrand"] = "Firebrand"
profession_abbreviations["Willbender"] = "Willbender"

profession_abbreviations["Revenant"] = "Revenant"
profession_abbreviations["Herald"] = "Herald"
profession_abbreviations["Renegade"] = "Renegade"
profession_abbreviations["Vindicator"] = "Vindicator"    

profession_abbreviations["Warrior"] = "Warrior"
profession_abbreviations["Berserker"] = "Berserker"
profession_abbreviations["Spellbreaker"] = "Spellbreaker"
profession_abbreviations["Bladesworn"] = "Bladesworn"

profession_abbreviations["Engineer"] = "Engineer"
profession_abbreviations["Scrapper"] = "Scrapper"
profession_abbreviations["Holosmith"] = "Holosmith"
profession_abbreviations["Mechanist"] = "Mechanist"    

profession_abbreviations["Ranger"] = "Ranger"
profession_abbreviations["Druid"] = "Druid"
profession_abbreviations["Soulbeast"] = "Soulbeast"
profession_abbreviations["Untamed"] = "Untamed"    

profession_abbreviations["Thief"] = "Thief"
profession_abbreviations["Daredevil"] = "Daredevil"
profession_abbreviations["Deadeye"] = "Deadeye"
profession_abbreviations["Specter"] = "Specter"

profession_abbreviations["Elementalist"] = "Elementalist"
profession_abbreviations["Tempest"] = "Tempest"
profession_abbreviations["Weaver"] = "Weaver"
profession_abbreviations["Catalyst"] = "Catalyst"

profession_abbreviations["Mesmer"] = "Mesmer"
profession_abbreviations["Chronomancer"] = "Chronomancer"
profession_abbreviations["Mirage"] = "Mirage"
profession_abbreviations["Virtuoso"] = "Virtuoso"
    
profession_abbreviations["Necromancer"] = "Necromancer"
profession_abbreviations["Reaper"] = "Reaper"
profession_abbreviations["Scourge"] = "Scourge"
profession_abbreviations["Harbinger"] = "Harbinger"

# name each stat will be written as
stat_names = {}
stat_names["dmg"] = "Damage"
stat_names["dmg_taken"] = "Damage Taken"
stat_names["rips"] = "Boon Strips"
stat_names["stability"] = "Stability"
stat_names["protection"] = "Protection"
stat_names["aegis"] = "Aegis"
stat_names["might"] = "Might"
stat_names["fury"] = "Fury"
stat_names["cleanses"] = "Condition Cleanses"
stat_names["heal"] = "Healing"
stat_names["barrier"] = "Barrier"
stat_names["dist"] = "Distance to Tag"
stat_names["deaths"] = "Deaths"
stat_names["superspeed"] = "Superspeed"
stat_names["regeneration"] = "Regeneration"
stat_names["resistance"] = "Resistance"
stat_names["resolution"] = "Resolution"
stat_names["quickness"] = "Quickness"
stat_names["swiftness"] = "Swiftness"
stat_names["alacrity"] = "Alacrity"
stat_names["vigor"] = "Vigor"