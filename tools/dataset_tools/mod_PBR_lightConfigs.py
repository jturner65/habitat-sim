#!/usr/bin/env python3

# Modify pbr-based dataset lighting to account for new PBR-specific intensity modification

import math
from os.path import join

import config_utils as ut

SRC_DIR = "/home/john/Facebook/habitat-sim/data/scene_datasets/replicaCAD_1-5/configs/lighting"

OUT_DIR = "/home/john/Facebook/habitat-sim/data/versioned_data/replica_cad_dataset_1.6/configs/lighting"


FILE_RE = "frl_apartment_([0-9]|stage).lighting_config.json"


def process_light(light_dict):
    light_dict["intensity"] /= math.pi


def process_lightConfig(json_src_file):
    all_lights_dict = json_src_file["lights"]
    for _, light_dict in all_lights_dict.items():
        process_light(light_dict)


# Read in all the lighting configs in SRC_DIR, the scale all lighting by intensity
# Subsequently, scale lighting by new hardcoded constant intensity (PI) and then normalize lights to find new light value + intensity
def main():
    # get all source path/dir/filenames
    file_listing_raw = ut.get_files_matching_regex(SRC_DIR, FILE_RE)

    for p, _, f in file_listing_raw:
        src_filename = join(p, f)
        dest_filename = join(OUT_DIR, f)
        print(
            f"src filename : {src_filename}\n\twill be modded and saved to\ndest_filename : {dest_filename}\n"
        )
        json_src_file = ut.load_json_into_dict(src_filename)
        process_lightConfig(json_src_file)
        ut.save_json_to_file(json_src_file, dest_filename)


if __name__ == "__main__":
    main()
