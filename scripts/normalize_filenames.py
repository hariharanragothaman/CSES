#!/usr/bin/env python3
"""Rename solution files to canonical NN_problem_name.{cpp,py} format."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generate_cpp_placeholders import (  # noqa: E402
    EXISTING_ALIASES as CPP_ALIASES,
    SECTIONS,
    slugify,
)

PY_EXTRA_ALIASES: dict[str, dict[int, list[str]]] = {
    "01_introductory_problems": {
        10: ["10_trailing_zeroes"],
        12: ["11_palindrome_reorder"],
        15: ["14_creating_strings"],
    },
    "02_sorting_and_searching": {
        2: ["apartments_optimized", "apartments_tle_solution"],
        10: [
            "smallest_sum_cannot_create_with_array",
            "smallest_sum_cannot_create_with_array_optimized",
        ],
        16: ["subarray_distinct_values"],
        28: ["nearest_smallest_values_intro_to_monotonic_stack"],
        29: [
            "subarray_sums_1_using_prefix_sum",
            "subarray_sums_1_using_sliding_window",
        ],
        30: ["subarray_sums_2_using_prefix_sum"],
    },
    "04_graph_algorithms": {
        2: ["02_labyrinth_shortest_path_from_node_to_destination"],
        23: [
            "23_road_construction_dsu_fast_solution",
            "23_road_construction_dsu_problem_clean",
        ],
    },
    "05_range_queries": {
        1: ["01_static_range_sum_queries_segment_tree"],
        2: ["static_range_minimum_queries"],
    },
    "06_tree_algorithms": {
        3: ["tree_diameter_using_dfs", "tree_diameter_using_dfs_optimized"],
        4: ["tree_distances_1_dfs"],
    },
    "08_string_algorithms": {
        2: ["string_matching", "02_string_matching_through_hashing_rabin_karp"],
        6: ["06_longest_palindrome_substring_manachers"],
        10: ["09_finding_patterns"],
    },
    "10_advanced_techniques": {
        1: [
            "meet_in_the_middle_fastio_optimization",
            "meet_in_the_middle_good_solution_tle",
        ],
    },
}

NON_CSES_STEMS = {
    ("02_sorting_and_searching", "cpp"): ["beautiful_item_in_each_query", "977F"],
    ("02_sorting_and_searching", "py"): ["977F"],
}


def is_placeholder(path: Path) -> bool:
    text = path.read_text()
    return "UNSOLVED (placeholder)" in text


def is_solved(path: Path) -> bool:
    return not is_placeholder(path)


def aliases_for(section: str, lang: str) -> dict[int, list[str]]:
    base = CPP_ALIASES.get(section, {}).copy()
    if lang == "py":
        extra = PY_EXTRA_ALIASES.get(section, {})
        merged: dict[int, list[str]] = {k: list(v) for k, v in base.items()}
        for idx, names in extra.items():
            merged.setdefault(idx, [])
            for name in names:
                if name not in merged[idx]:
                    merged[idx].append(name)
        return merged
    return base


def file_matches_problem(
    stem: str, section: str, idx: int, problem: str, lang: str
) -> bool:
    canonical = f"{idx:02d}_{slugify(problem)}"
    if stem == canonical:
        return True
    if stem in aliases_for(section, lang).get(idx, []):
        return True
    slug = slugify(problem)
    if stem == slug:
        return True
    if stem.startswith(f"{idx:02d}_") and slug in stem:
        return True
    return False


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    subprocess.run(["git", "mv", str(src), str(dst)], cwd=ROOT, check=True)


def move_file(src: Path, dst: Path) -> None:
    if subprocess.run(["git", "mv", str(src), str(dst)], cwd=ROOT).returncode != 0:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            dst.unlink()
        src.rename(dst)


def normalize_lang(lang: str) -> tuple[int, int]:
    ext = "cpp" if lang == "cpp" else "py"
    renamed = 0
    removed = 0
    non_cses = 0

    for folder, problems in SECTIONS.items():
        lang_dir = ROOT / folder / lang
        if not lang_dir.exists():
            continue

        files = list(lang_dir.glob(f"*.{ext}"))
        stems = {p.stem: p for p in files}
        assigned: set[str] = set()

        for idx, problem in enumerate(problems, start=1):
            canonical = f"{idx:02d}_{slugify(problem)}"
            canonical_path = lang_dir / f"{canonical}.{ext}"

            matches = [
                stems[s]
                for s in stems
                if file_matches_problem(s, folder, idx, problem, lang)
            ]
            if not matches:
                continue

            for m in matches:
                assigned.add(m.stem)

            def sort_key(p: Path) -> tuple:
                solved = 0 if is_solved(p) else 1
                canonical_pref = 0 if p.stem == canonical else 1
                return (solved, canonical_pref, p.stem)

            matches.sort(key=sort_key)
            primary = matches[0]

            if canonical_path.exists() and canonical_path != primary:
                if is_placeholder(canonical_path):
                    canonical_path.unlink()
                    removed += 1
                elif is_solved(canonical_path) and is_solved(primary):
                    alt_dst = lang_dir / f"{canonical}_alt_{primary.stem}.{ext}"
                    if primary != canonical_path:
                        move_file(primary, alt_dst)
                        renamed += 1
                    continue

            if primary.stem != canonical:
                move_file(primary, canonical_path)
                renamed += 1
                primary = canonical_path

            alt_idx = 1
            for alt in matches[1:]:
                if alt == primary:
                    continue
                alt_name = f"{canonical}_alt_{alt.stem}.{ext}"
                alt_dst = lang_dir / alt_name
                if alt_dst.exists():
                    continue
                move_file(alt, alt_dst)
                renamed += 1
                alt_idx += 1

        for stem, path in list(stems.items()):
            if stem in assigned:
                continue
            non_list = NON_CSES_STEMS.get((folder, lang), [])
            if stem in non_list or stem.startswith("_non_cses_"):
                new_name = f"_non_cses_{stem}.{ext}" if not stem.startswith("_non_cses_") else f"{stem}.{ext}"
                dst = lang_dir / new_name
                if path.name != new_name:
                    move_file(path, dst)
                    non_cses += 1
                continue

            # try fuzzy: assign as alt to best matching problem by slug overlap
            best = None
            for idx, problem in enumerate(problems, start=1):
                slug = slugify(problem)
                if slug in stem or stem in slug:
                    best = (idx, problem)
                    break
            if best:
                idx, problem = best
                canonical = f"{idx:02d}_{slugify(problem)}"
                dst = lang_dir / f"{canonical}_alt_{stem}.{ext}"
                if not dst.exists():
                    move_file(path, dst)
                    renamed += 1
            else:
                dst = lang_dir / f"_unmapped_{stem}.{ext}"
                if not dst.exists():
                    move_file(path, dst)
                    non_cses += 1

    return renamed, removed, non_cses


def main() -> None:
    total_renamed = 0
    total_removed = 0
    total_non_cses = 0
    for lang in ("cpp", "py"):
        r, d, n = normalize_lang(lang)
        print(f"{lang}: renamed={r}, removed_placeholders={d}, non_cses={n}")
        total_renamed += r
        total_removed += d
        total_non_cses += n
    print(f"total renamed={total_renamed}")


if __name__ == "__main__":
    main()
