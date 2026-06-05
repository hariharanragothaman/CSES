#!/usr/bin/env python3
"""Generate Python placeholder files for unsolved CSES problems."""

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

_spec = importlib.util.spec_from_file_location(
    "generate_cpp_placeholders",
    ROOT / "scripts" / "generate_cpp_placeholders.py",
)
_cpp_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_cpp_mod)

SECTIONS = _cpp_mod.SECTIONS
slugify = _cpp_mod.slugify
section_title = _cpp_mod.section_title

# problem index (1-based) -> existing filename stems (without .py) that satisfy it
PY_EXISTING_ALIASES: dict[str, dict[int, list[str]]] = {
    "01_introductory_problems": {
        1: ["01_weird_algorithm"],
        2: ["02_missing_number"],
        3: ["03_repititions"],
        4: ["04_increasing_array"],
        5: ["05_permutations"],
        6: ["06_number_spiral"],
        8: ["08_two_sets"],
        9: ["09_bit_strings"],
        10: ["10_trailing_zeroes"],
        12: ["11_palindrome_reorder", "12_palindrome_reorder"],
        13: ["13_gray_codes"],
        15: ["14_creating_strings", "15_creating_strings"],
        22: ["18_digit_queries", "22_digit_queries"],
    },
    "02_sorting_and_searching": {
        1: ["distinct_numbers", "01_distinct_numbers"],
        2: ["apartments_optimized", "apartments_tle_solution", "02_apartments"],
        7: ["sum_of_two_values", "07_sum_of_two_values"],
        8: ["maximum_subarray_sum", "08_maximum_subarray_sum"],
        10: [
            "smallest_sum_cannot_create_with_array",
            "smallest_sum_cannot_create_with_array_optimized",
            "10_missing_coin_sum",
        ],
        11: ["collecting_numbers", "11_collecting_numbers"],
        14: ["towers", "14_towers"],
        15: ["traffic_lights", "15_traffic_lights"],
        16: ["subarray_distinct_values", "16_distinct_values_subarrays"],
        26: ["sum_of_three_values", "26_sum_of_three_values"],
        28: [
            "nearest_smallest_values_intro_to_monotonic_stack",
            "28_nearest_smaller_values",
        ],
        29: [
            "subarray_sums_1_using_prefix_sum",
            "subarray_sums_1_using_sliding_window",
            "29_subarray_sums_i",
        ],
        30: ["subarray_sums_2_using_prefix_sum", "30_subarray_sums_ii"],
        31: ["subarray_divisibility", "31_subarray_divisibility"],
        33: ["array_division", "33_array_division"],
    },
    "03_dynamic_programming": {
        18: ["increasing_sequence", "18_increasing_subsequence"],
    },
    "04_graph_algorithms": {
        1: ["01_counting_rooms"],
        2: [
            "02_labyrinth_optimized",
            "02_labyrinth_shortest_path_from_node_to_destination",
            "02_labyrinth",
        ],
        3: ["03_building_roads"],
        4: ["05_message_route", "04_message_route"],
        5: ["04_building_teams", "05_building_teams"],
        15: ["15_course_schedule"],
        23: [
            "23_road_construction_dsu_fast_solution",
            "23_road_construction_dsu_problem_clean",
            "23_road_construction",
        ],
    },
    "05_range_queries": {
        1: [
            "01_static_range_sum_queries",
            "01_static_range_sum_queries_segment_tree",
        ],
        2: ["static_range_minimum_queries", "02_static_range_minimum_queries"],
    },
    "06_tree_algorithms": {
        1: ["subordinates", "01_subordinates"],
        3: [
            "01_tree_diameter",
            "tree_diameter_using_dfs",
            "tree_diameter_using_dfs_optimized",
            "03_tree_diameter",
        ],
        4: ["tree_distances_1_dfs", "04_tree_distances_i"],
    },
    "08_string_algorithms": {
        2: [
            "02_string_matching_through_hashing_rabin_karp",
            "string_matching",
            "02_string_matching",
        ],
        3: ["03_finding_borders"],
        6: [
            "06_longest_palindrome_substring_manachers",
            "06_longest_palindrome",
        ],
        10: ["09_finding_patterns", "10_finding_patterns"],
    },
    "10_advanced_techniques": {
        1: [
            "meet_in_the_middle_fastio_optimization",
            "meet_in_the_middle_good_solution_tle",
            "01_meet_in_the_middle",
        ],
    },
    "13_bitwise_operations": {
        1: ["counting_bits", "01_counting_bits"],
    },
    "15_advanced_graph_problems": {
        21: ["visiting_cities", "21_visiting_cities"],
    },
}


def canonical_name(index: int, problem: str) -> str:
    return f"{index:02d}_{slugify(problem)}.py"


def list_existing_stems(py_dir: Path) -> set[str]:
    if not py_dir.exists():
        return set()
    return {p.stem for p in py_dir.glob("*.py")}


def is_covered(section: str, index: int, problem: str, existing: set[str]) -> bool:
    canonical = f"{index:02d}_{slugify(problem)}"
    if canonical in existing:
        return True
    aliases = PY_EXISTING_ALIASES.get(section, {}).get(index, [])
    if any(alias in existing for alias in aliases):
        return True
    slug = slugify(problem)
    for stem in existing:
        if stem in {slug, canonical}:
            return True
        if stem.endswith(f"_{slug}") or stem == slug.replace("_", ""):
            return True
        if stem.startswith(f"{index:02d}_") and slug in stem:
            return True
    return False


TEMPLATE = '''"""
File    : {filename}
Problem : {problem}
Section : {section_title}
Status  : UNSOLVED (placeholder)
"""

import os
import sys
import time


def solve():
    # TODO: not solved
    pass


def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()

    solve()
    debug("-")

    if os.path.exists("data.in"):
        print(f"Time Elapsed: {{time.time() - start_time}} seconds")
        sys.stdout.close()


# region debug

def input_as_array() -> list[int]:
    return list(map(int, input().split()))


def debug(char) -> None:
    if os.path.exists("data.in"):
        print(char * 25)


def debug2(value) -> None:
    if os.path.exists("data.in"):
        print(value)


# endregion


if __name__ == "__main__":
    main()
'''


def main() -> None:
    created = 0
    skipped = 0

    for folder, problems in SECTIONS.items():
        py_dir = ROOT / folder / "py"
        py_dir.mkdir(parents=True, exist_ok=True)
        existing = list_existing_stems(py_dir)

        for idx, problem in enumerate(problems, start=1):
            filename = canonical_name(idx, problem)
            path = py_dir / filename

            if is_covered(folder, idx, problem, existing):
                skipped += 1
                continue

            if path.exists():
                skipped += 1
                continue

            content = TEMPLATE.format(
                filename=filename,
                problem=problem,
                section_title=section_title(folder),
            )
            path.write_text(content)
            existing.add(path.stem)
            created += 1

    from ensure_test_io import ensure_test_io_files

    io_created = ensure_test_io_files(ROOT)

    print(f"Created {created} placeholder files")
    print(f"Skipped {skipped} existing/solved problems")
    print(f"Ensured test I/O files ({io_created} newly created)")


if __name__ == "__main__":
    main()
