import json, re, os, sys, shutil, time, argparse

global_build_order_t = [ # terran
    (1, "command_center"),
    (2, "barracks"),
    (2, "supply_depot"),
    (255, "engineering_bay"),
    (4, "barracks"),
    (4, "missile_turret"),
    (255, "academy"),
    (4, "factory"),
    (4, "machine_shop"),
    (2, "command_center"),
    (255, "armory"),
    (1, "comsat_station"),
    (4, "starport"),
    (8, "factory"),
    (4, "control_tower"),
    (4, "supply_depot"),
    (255, "command_center"),
    (255, "barracks"),
    (255, "science_facility"),
    (255, "covert_ops"),
    (255, "physics_lab"),
    (255, "factory"),
    (255, "starport"),
    (255, "machine_shop"),
    (255, "control_tower"),
    (255, "missile_turret"),
    (255, "bunker"),
    (255, "supply_depot"),
    (255, "nuclear_silo"),
    (255, "comsat_station"),
]

global_build_order_p = [ # protoss
    (1, "nexus"),
    (4, "pylon"),
    (2, "gateway"),
    (1, "forge"),
    (6, "pylon"),
    (2, "cybernetics_core"),
    (4, "photon_cannon"),
    (2, "shield_battery"),
    (10, "pylon"),
    (4, "gateway"),
    (1, "citadel_of_adun"),
    (12, "pylon"),
    (2, "stargate"),
    (2, "robotics_facility"),
    (255, "forge"),
    (255, "cybernetics_core"),
    (255, "citadel_of_adun"),
    (12, "photon_cannon"),
    (16, "pylon"),
    (8, "gateway"),
    (4, "stargate"),
    (255, "templar_archives"),
    (255, "nexus"),
    (255, "shield_battery"),
    (255, "fleet_beacon"),
    (4, "robotics_facility"),
    (255, "observatory"),
    (255, "robotics_support_bay"),
    (255, "gateway"),
    (255, "arbiter_tribunal"),
    (8, "stargate"),
    (8, "robotics_facility"),
    (255, "pylon"),
    (255, "stargate"),
    (255, "robotics_facility"),
    (255, "photon_cannon"),
]

global_build_order_z = [ # zerg
    (4, "hatchery"),
    (1, "spawning_pool"),
    (1, "evolution_chamber"),
    (2, "creep_colony"),
    (1, "hydralisk_den"),
    (4, "lair"),
    (8, "hatchery"),
    (255, "spawning_pool"),
    (255, "evolution_chamber"),
    (255, "hydralisk_den"),
    (8, "creep_colony"),
    (4, "sunken_colony"),
    (4, "spore_colony"),
    (1, "spire"),
    (1, "queen_nest"),
    (4, "hive"),
    (8, "lair"),
    (12, "hatchery"),
    (255, "spire"),
    (255, "queen_nest"),
    (255, "ultralisk_cavern"),
    (255, "greater_spire"),
    (255, "defiler_mound"),
    (16, "hatchery"),
    (12, "lair"),
    (8, "hive"),
    (16, "creep_colony"),
    (8, "sunken_colony"),
    (8, "spore_colony"),
    (255, "hatchery"),
    (255, "lair"),
    (255, "hive"),
    (255, "creep_colony"),
    (255, "sunken_colony"),
    (255, "spore_colony"),
]

global_build_orders = {
    "t" : global_build_order_t,
    "p" : global_build_order_p,
    "z" : global_build_order_z,
}

def generate_build_order(building_counts, global_build_order):
    built_counts = {
        "command_center": 1,
        "nexus": 1,
        "hatchery": 1,
    }
    shortcut_buildings = [
        "comsat_station",
        "nuclear_silo",
        "machine_shop",
        "control_tower",
        "covert_ops",
        "physics_lab",
    ]
    is_first_pylon = True
    output_builds = []
    for count, bldg in global_build_order:
        if bldg not in built_counts:
            built_counts[bldg] = 0
        if bldg not in building_counts:
            continue
        if building_counts[bldg] > count:
            if bldg in shortcut_buildings:
                output_builds.append((count, bldg))
            else:
                for k in range(built_counts[bldg] + 1, count + 1):
                    # if k == count and bldg == "pylon" and is_first_pylon:
                    #     output_builds.append((k, "pylon[wait]"))
                    #     is_first_pylon = False
                    # else:
                    output_builds.append((k, bldg))
            built_counts[bldg] = count
        elif building_counts[bldg] > 0:
            if bldg in shortcut_buildings:
                output_builds.append((building_counts[bldg], bldg))
            else:
                for k in range(built_counts[bldg] + 1, building_counts[bldg] + 1):
                    # if k == building_counts[bldg] and bldg == "pylon" and is_first_pylon:
                    #     output_builds.append((k, "pylon[wait]"))
                    #     is_first_pylon = False
                    # else:
                    output_builds.append((k, bldg))
            built_counts[bldg] = building_counts[bldg]
            building_counts[bldg] = 0
    
    # double check
    for bldg in building_counts:
        if building_counts[bldg] > 0:
            print("MISSING:", building_counts[bldg], bldg)
            output_builds.append((building_counts[bldg], bldg))
    return output_builds

def get_building_counts(source_file):
    output = {}
    rem_file = []
    pneed_called = 0
    with open(source_file, encoding = "utf8") as asc3fp:
        for line in asc3fp:
            line_clean = line.strip()
            if line_clean.startswith("player_need"):
                _, count_str, unit = re.split(r"\W+", line_clean)
                count = int(count_str)
                if unit in output:
                    output[unit] = max(count, unit)
                else:
                    output[unit] = count
                if not pneed_called:
                    rem_file.append("<ADD_MULTIRUN_HERE>\n")
                    pneed_called = 1
                continue
            rem_file.append(line)
            
    if not pneed_called:
        return None, None, None
    
    # fix zerg morph
    if "hive" in output:
        if "hatchery" not in output or output["hatchery"] < output["hive"]:
            output["hatchery"] = output["hive"]
        if "lair" not in output or output["lair"] < output["hive"]:
            output["lair"] = output["hive"]
    elif "lair" in output:
        if "hatchery" not in output or output["hatchery"] < output["lair"]:
            output["hatchery"] = output["lair"]
    if "greater_spire" in output:
        if "spire" not in output or output["spire"] < output["greater_spire"]:
            output["spire"] = output["greater_spire"]
            
    creep_needed = 0
    if "sunken_colony" in output:
        creep_needed += output["sunken_colony"]
    if "spore_colony" in output:
        creep_needed += output["spore_colony"]
    if "creep_colony" not in output or output["creep_colony"] < creep_needed:
        output["creep_colony"] = creep_needed
        
    rem_text = "".join(rem_file)
    if "command_center" in rem_text or "scv" in rem_text:
        race = "t"
    elif "nexus" in rem_text or "probe" in rem_text:
        race = "p"
    elif "hatchery" in rem_text or "drone" in rem_text:
        race = "z"
    else:
        raise NotImplementedError("cannot find race", source_file)
    return output, rem_text, race

def generate_asc3_with_build_order(rem_file, build_order, multirun_wait = 1000):
    # replace ADD_MULTIRUN_HERE token
    rem_file = re.sub(r"<ADD_MULTIRUN_HERE>", "multirun make_buildings\nwait {}".format(multirun_wait), rem_file)
    if not rem_file.endswith("\n"):
        rem_file += "\n"
    rem_file += "\n"
    
    rem_file += ":make_buildings\n"
    for num, unit in build_order:
        if unit.endswith("[wait]"):
            rem_file += "build {} {} 80\n".format(num, unit[:-6])
            rem_file += "wait_buildstart {} {}\n".format(num, unit[:-6])
            rem_file += "wait 600\n"
        else:
            rem_file += "build {} {} 80\n".format(num, unit)
            rem_file += "wait_buildstart {} {}\n".format(num, unit)
    rem_file += "wait 100\n"
    rem_file += "stop\n"
    return rem_file

def convert_asc3_file(in_file, out_file, multirun_wait):
    build_counts, rem_file, race = get_building_counts(in_file)
    if build_counts is None:
        print("Not a valid script (player_need not found):", os.path.basename(in_file))
        return
    build_order = generate_build_order(build_counts, global_build_orders[race])
    result_asc3 = generate_asc3_with_build_order(rem_file, build_order, multirun_wait = multirun_wait[race])
    
    with open(out_file, "w", encoding = "utf8") as fp:
        fp.write(result_asc3)
    print("Converted:", os.path.basename(in_file))

def convert_asc3_dir(in_dir, out_dir, multirun_wait = 1000):
    os.makedirs(out_dir, exist_ok=True)

    for file_name in os.listdir(in_dir):
        if file_name.endswith(".asc3"):
            file_path = os.path.join(in_dir, file_name)
            dest_path = os.path.join(out_dir, file_name)
            convert_asc3_file(file_path, dest_path, multirun_wait = multirun_wait)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "convert player_need in asc3 to build orders")
    parser.add_argument("--waitz", type=int, default = 2000, help = "wait time for zerg buildings")
    parser.add_argument("--waitt", type=int, default = 2000, help = "wait time for terran buildings")
    parser.add_argument("--waitp", type=int, default = 3000, help = "wait time for protoss buildings")
    parser.add_argument("in_dir", type=str, help = "input asc3 dir")
    parser.add_argument("out_dir", type=str, help = "output asc3 dir")
    args = parser.parse_args()

    convert_asc3_dir(args.in_dir, args.out_dir, multirun_wait = {
        "z": args.waitz,
        "t": args.waitt,
        "p": args.waitp
    })