#!/usr/bin/env python3
"""Generate C++ placeholder files for unsolved CSES problems."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SECTIONS = {
    "01_introductory_problems": [
        "Weird Algorithm",
        "Missing Number",
        "Repetitions",
        "Increasing Array",
        "Permutations",
        "Number Spiral",
        "Two Knights",
        "Two Sets",
        "Bit Strings",
        "Trailing Zeros",
        "Coin Piles",
        "Palindrome Reorder",
        "Gray Code",
        "Tower of Hanoi",
        "Creating Strings",
        "Apple Division",
        "Chessboard and Queens",
        "Raab Game I",
        "Mex Grid Construction",
        "Knight Moves Grid",
        "Grid Coloring I",
        "Digit Queries",
        "String Reorder",
        "Grid Path Description",
    ],
    "02_sorting_and_searching": [
        "Distinct Numbers",
        "Apartments",
        "Ferris Wheel",
        "Concert Tickets",
        "Restaurant Customers",
        "Movie Festival",
        "Sum of Two Values",
        "Maximum Subarray Sum",
        "Stick Lengths",
        "Missing Coin Sum",
        "Collecting Numbers",
        "Collecting Numbers II",
        "Playlist",
        "Towers",
        "Traffic Lights",
        "Distinct Values Subarrays",
        "Distinct Values Subsequences",
        "Josephus Problem I",
        "Josephus Problem II",
        "Nested Ranges Check",
        "Nested Ranges Count",
        "Room Allocation",
        "Factory Machines",
        "Tasks and Deadlines",
        "Reading Books",
        "Sum of Three Values",
        "Sum of Four Values",
        "Nearest Smaller Values",
        "Subarray Sums I",
        "Subarray Sums II",
        "Subarray Divisibility",
        "Distinct Values Subarrays II",
        "Array Division",
        "Movie Festival II",
        "Maximum Subarray Sum II",
    ],
    "03_dynamic_programming": [
        "Dice Combinations",
        "Minimizing Coins",
        "Coin Combinations I",
        "Coin Combinations II",
        "Removing Digits",
        "Grid Paths I",
        "Book Shop",
        "Array Description",
        "Counting Towers",
        "Edit Distance",
        "Longest Common Subsequence",
        "Rectangle Cutting",
        "Minimal Grid Path",
        "Money Sums",
        "Removal Game",
        "Two Sets II",
        "Mountain Range",
        "Increasing Subsequence",
        "Projects",
        "Elevator Rides",
        "Counting Tilings",
        "Counting Numbers",
        "Increasing Subsequence II",
    ],
    "04_graph_algorithms": [
        "Counting Rooms",
        "Labyrinth",
        "Building Roads",
        "Message Route",
        "Building Teams",
        "Round Trip",
        "Monsters",
        "Shortest Routes I",
        "Shortest Routes II",
        "High Score",
        "Flight Discount",
        "Cycle Finding",
        "Flight Routes",
        "Round Trip II",
        "Course Schedule",
        "Longest Flight Route",
        "Game Routes",
        "Investigation",
        "Planets Queries I",
        "Planets Queries II",
        "Planets Cycles",
        "Road Reparation",
        "Road Construction",
        "Flight Routes Check",
        "Planets and Kingdoms",
        "Giant Pizza",
        "Coin Collector",
        "Mail Delivery",
        "De Bruijn Sequence",
        "Teleporters Path",
        "Hamiltonian Flights",
        "Knight's Tour",
        "Download Speed",
        "Police Chase",
        "School Dance",
        "Distinct Routes",
    ],
    "05_range_queries": [
        "Static Range Sum Queries",
        "Static Range Minimum Queries",
        "Dynamic Range Sum Queries",
        "Dynamic Range Minimum Queries",
        "Range Xor Queries",
        "Range Update Queries",
        "Forest Queries",
        "Hotel Queries",
        "List Removals",
        "Salary Queries",
        "Prefix Sum Queries",
        "Pizzeria Queries",
        "Visible Buildings Queries",
        "Range Interval Queries",
        "Subarray Sum Queries",
        "Subarray Sum Queries II",
        "Distinct Values Queries",
        "Distinct Values Queries II",
        "Increasing Array Queries",
        "Movie Festival Queries",
        "Forest Queries II",
        "Range Updates and Sums",
        "Polynomial Queries",
        "Range Queries and Copies",
        "Missing Coin Sum Queries",
    ],
    "06_tree_algorithms": [
        "Subordinates",
        "Tree Matching",
        "Tree Diameter",
        "Tree Distances I",
        "Tree Distances II",
        "Company Queries I",
        "Company Queries II",
        "Distance Queries",
        "Counting Paths",
        "Subtree Queries",
        "Path Queries",
        "Path Queries II",
        "Distinct Colors",
        "Finding a Centroid",
        "Fixed-Length Paths I",
        "Fixed-Length Paths II",
    ],
    "07_math": [
        "Josephus Queries",
        "Exponentiation",
        "Exponentiation II",
        "Counting Divisors",
        "Common Divisors",
        "Sum of Divisors",
        "Divisor Analysis",
        "Prime Multiples",
        "Counting Coprime Pairs",
        "Next Prime",
        "Binomial Coefficients",
        "Creating Strings II",
        "Distributing Apples",
        "Christmas Party",
        "Permutation Order",
        "Permutation Rounds",
        "Bracket Sequences I",
        "Bracket Sequences II",
        "Counting Necklaces",
        "Counting Grids",
        "Fibonacci Numbers",
        "Throwing Dice",
        "Graph Paths I",
        "Graph Paths II",
        "System of Linear Equations",
        "Sum of Four Squares",
        "Triangle Number Sums",
        "Dice Probability",
        "Moving Robots",
        "Candy Lottery",
        "Inversion Probability",
        "Stick Game",
        "Nim Game I",
        "Nim Game II",
        "Stair Game",
        "Grundy's Game",
        "Another Game",
    ],
    "08_string_algorithms": [
        "Word Combinations",
        "String Matching",
        "Finding Borders",
        "Finding Periods",
        "Minimal Rotation",
        "Longest Palindrome",
        "All Palindromes",
        "Required Substring",
        "Palindrome Queries",
        "Finding Patterns",
        "Counting Patterns",
        "Pattern Positions",
        "Distinct Substrings",
        "Distinct Subsequences",
        "Repeating Substring",
        "String Functions",
        "Inverse Suffix Array",
        "String Transform",
        "Substring Order I",
        "Substring Order II",
        "Substring Distribution",
    ],
    "09_geometry": [
        "Point Location Test",
        "Line Segment Intersection",
        "Polygon Area",
        "Point in Polygon",
        "Polygon Lattice Points",
        "Minimum Euclidean Distance",
        "Convex Hull",
        "Maximum Manhattan Distances",
        "All Manhattan Distances",
        "Intersection Points",
        "Line Segments Trace I",
        "Line Segments Trace II",
        "Lines and Queries I",
        "Lines and Queries II",
        "Area of Rectangles",
        "Robot Path",
    ],
    "10_advanced_techniques": [
        "Meet in the Middle",
        "Hamming Distance",
        "Corner Subgrid Check",
        "Corner Subgrid Count",
        "Reachable Nodes",
        "Reachability Queries",
        "Cut and Paste",
        "Substring Reversals",
        "Reversals and Sums",
        "Necessary Roads",
        "Necessary Cities",
        "Eulerian Subgraphs",
        "Monster Game I",
        "Monster Game II",
        "Subarray Squares",
        "Houses and Schools",
        "Knuth Division",
        "Apples and Bananas",
        "One Bit Positions",
        "Signal Processing",
        "New Roads Queries",
        "Dynamic Connectivity",
        "Parcel Delivery",
        "Task Assignment",
        "Distinct Routes II",
    ],
    "11_sliding_window_problems": [
        "Sliding Window Sum",
        "Sliding Window Minimum",
        "Sliding Window Xor",
        "Sliding Window Or",
        "Sliding Window Distinct Values",
        "Sliding Window Mode",
        "Sliding Window Mex",
        "Sliding Window Median",
        "Sliding Window Cost",
        "Sliding Window Inversions",
        "Sliding Window Advertisement",
    ],
    "12_interactive_problems": [
        "Hidden Integer",
        "Hidden Permutation",
        "K-th Highest Score",
        "Permuted Binary Strings",
        "Colored Chairs",
        "Inversion Sorting",
    ],
    "13_bitwise_operations": [
        "Counting Bits",
        "Maximum Xor Subarray",
        "Maximum Xor Subset",
        "Number of Subset Xors",
        "K Subset Xors",
        "All Subarray Xors",
        "Xor Pyramid Peak",
        "Xor Pyramid Diagonal",
        "Xor Pyramid Row",
        "SOS Bit Problem",
        "And Subset Count",
    ],
    "14_construction_problems": [
        "Inverse Inversions",
        "Monotone Subsequences",
        "Third Permutation",
        "Permutation Prime Sums",
        "Chess Tournament",
        "Distinct Sums Grid",
        "Filling Trominos",
        "Grid Path Construction",
    ],
    "15_advanced_graph_problems": [
        "Nearest Shops",
        "Prüfer Code",
        "Tree Traversals",
        "Course Schedule II",
        "Acyclic Graph Edges",
        "Strongly Connected Edges",
        "Even Outdegree Edges",
        "Graph Girth",
        "Fixed Length Walk Queries",
        "Transfer Speeds Sum",
        "MST Edge Check",
        "MST Edge Set Check",
        "MST Edge Cost",
        "Network Breakdown",
        "Tree Coin Collecting I",
        "Tree Coin Collecting II",
        "Tree Isomorphism I",
        "Tree Isomorphism II",
        "Flight Route Requests",
        "Critical Cities",
        "Visiting Cities",
        "Graph Coloring",
        "Bus Companies",
        "Split into Two Paths",
        "Network Renovation",
        "Forbidden Cities",
        "Creating Offices",
        "New Flight Routes",
    ],
    "16_counting_problems": [
        "Filled Subgrid Count I",
        "Filled Subgrid Count II",
        "All Letter Subgrid Count I",
        "All Letter Subgrid Count II",
        "Border Subgrid Count I",
        "Border Subgrid Count II",
        "Raab Game II",
        "Empty String",
        "Permutation Inversions",
        "Counting Bishops",
        "Counting Sequences",
        "Grid Paths II",
        "Counting Permutations",
        "Grid Completion",
        "Counting Reorders",
        "Tournament Graph Distribution",
        "Collecting Numbers Distribution",
        "Functional Graph Distribution",
    ],
    "17_additional_problems_i": [
        "Shortest Subsequence",
        "Distinct Values Sum",
        "Distinct Values Splits",
        "Swap Game",
        "Beautiful Permutation II",
        "Multiplication Table",
        "Bubble Sort Rounds I",
        "Bubble Sort Rounds II",
        "Nearest Campsites I",
        "Nearest Campsites II",
        "Advertisement",
        "Special Substrings",
        "Counting LCM Arrays",
        "Square Subsets",
        "Subarray Sum Constraints",
        "Water Containers Moves",
        "Water Containers Queries",
        "Stack Weights",
        "Maximum Average Subarrays",
        "Subsets with Fixed Average",
        "Two Array Average",
        "Pyramid Array",
        "Permutation Subsequence",
        "Bit Inversions",
        "Writing Numbers",
        "Letter Pair Move Game",
        "Maximum Building I",
        "Sorting Methods",
        "Cyclic Array",
        "List of Sums",
    ],
    "18_additional_problems_ii": [
        "Bouncing Ball Steps",
        "Bouncing Ball Cycle",
        "Knight Moves Queries",
        "K Subset Sums I",
        "K Subset Sums II",
        "Increasing Array II",
        "Food Division",
        "Swap Round Sorting",
        "Binary Subsequences",
        "School Excursion",
        "Coin Grid",
        "Grid Coloring II",
        "Programmers and Artists",
        "Removing Digits II",
        "Coin Arrangement",
        "Replace with Difference",
        "Grid Puzzle I",
        "Grid Puzzle II",
        "Bit Substrings",
        "Reversal Sorting",
        "Book Shop II",
        "GCD Subsets",
        "Minimum Cost Pairs",
        "Same Sum Subsets",
        "Mex Grid Queries",
        "Maximum Building II",
        "Stick Divisions",
        "Stick Difference",
        "Coding Company",
        "Two Stacks Sorting",
    ],
}

# problem index (1-based) -> existing filename stems (without .cpp) that satisfy it
EXISTING_ALIASES: dict[str, dict[int, list[str]]] = {
    "01_introductory_problems": {
        1: ["01_weird_algorithm"],
        2: ["02_missing_number"],
        3: ["03_repititions"],
        4: ["04_increasing_array"],
        5: ["05_permutations"],
        6: ["06_number_spiral"],
        7: ["07_two_knights"],
        11: ["11_coin_piles"],
        16: ["16_apple_division"],
        18: ["1480B", "18_raab_game_i"],
    },
    "02_sorting_and_searching": {
        1: ["distinctNumbers", "01_distinct_numbers"],
        3: ["ferris_wheel", "ferris_wheel2", "03_ferris_wheel"],
        4: ["concert_tickets", "04_concert_tickets"],
        5: ["restaurant_customers", "05_restaurant_customers"],
        6: ["movie_festival", "06_movie_festival"],
        9: ["stick_lengths", "09_stick_lengths"],
        11: ["collecting_numbers", "11_collecting_numbers"],
        13: ["13_playlist"],
        15: ["traffic_lights", "traffic_lights2", "15_traffic_lights"],
        18: ["josephus1", "18_josephus_problem_i"],
        23: ["factory_machines", "23_factory_machines"],
        24: ["tasks_and_deadlines", "24_tasks_and_deadlines"],
        31: ["subarray_divisibility", "31_subarray_divisibility"],
        33: ["031_array_division", "33_array_division"],
    },
    "03_dynamic_programming": {
        1: ["dice_combinations", "01_dice_combinations"],
        18: ["increasing_sequence", "18_increasing_subsequence"],
    },
    "04_graph_algorithms": {
        1: ["01_counting_rooms_iterative", "01_counting_rooms_recursion", "01_counting_rooms"],
        2: ["02_labyrinth_bfs_efficient", "02_labyrinth_bfs_tle", "02_labyrinth"],
        3: ["03_building_roads"],
        4: ["04_message_route"],
        5: ["05_building_teams"],
        6: ["round_trip", "06_round_trip"],
        15: ["15_course_schedule"],
        23: ["23_road_construction"],
    },
    "05_range_queries": {
        1: ["01_static_range_sum_queries"],
        2: ["02_static_range_minimum_queries"],
        3: ["03_dynamic_range_sum_queries"],
        4: ["04_dynamic_range_minimum_queries"],
        5: ["05_range_xor_queries"],
    },
    "06_tree_algorithms": {
        1: ["subordinates", "01_subordinates"],
        3: ["01_tree_diameter", "diameter_of_tree", "03_tree_diameter"],
        6: ["company_queries", "company_queries2", "company_queries_without_function_calls", "06_company_queries_i"],
    },
    "07_math": {
        4: ["counting_divisors", "04_counting_divisors"],
        5: ["common_divisors", "common_divisors2", "05_common_divisors"],
    },
    "08_string_algorithms": {
        1: ["01_word_combinations"],
        13: ["12_distinct_substrings", "13_distinct_substrings"],
    },
    "09_geometry": {
        1: ["01_point_location_test"],
    },
    "10_advanced_techniques": {
        2: ["02_hamming_distance"],
    },
    "11_sliding_window_problems": {
        8: ["sliding_median_by_sorting", "sliding_median_multi_sets", "08_sliding_window_median"],
    },
    "17_additional_problems_i": {
        1: ["shortest_subsequence", "01_shortest_subsequence"],
    },
}


def slugify(name: str) -> str:
    s = name.lower()
    s = s.replace("'", "")
    s = s.replace("ü", "u")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def canonical_name(index: int, problem: str) -> str:
    return f"{index:02d}_{slugify(problem)}.cpp"


def list_existing_stems(cpp_dir: Path) -> set[str]:
    if not cpp_dir.exists():
        return set()
    return {p.stem for p in cpp_dir.glob("*.cpp")}


def is_covered(section: str, index: int, problem: str, existing: set[str]) -> bool:
    canonical = f"{index:02d}_{slugify(problem)}"
    if canonical in existing:
        return True
    aliases = EXISTING_ALIASES.get(section, {}).get(index, [])
    if any(alias in existing for alias in aliases):
        return True
    # fuzzy: any existing file contains slug tokens
    slug = slugify(problem)
    for stem in existing:
        if stem == slug or stem.endswith(f"_{slug}") or stem.startswith(f"{index:02d}_"):
            if slug in stem or stem.replace("_", "") == slug.replace("_", ""):
                return True
    return False


TEMPLATE = '''/**
 * File              : {filename}
 * Problem           : {problem}
 * Section           : {section_title}
 * Status            : UNSOLVED (placeholder)
 */

#include "bits/stdc++.h"
#include <numeric>
using namespace std;

#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("data.in");
ofstream  o_data("data.out");
#define cin  i_data
#define cout o_data
#else
#endif

#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int long long
#define stars cout << "********************************" << endl;
#define debug(a)  cout << a << endl;
#define MOD 1000000007
#define all(x) x.begin(), x.end()

template<typename T>
void print(std::vector<T> const &v)
{{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}}

void solve()
{{
    // TODO: not solved
}}

int32_t main()
{{
    ENABLEFASTIO();
    int T;
    T = 1;
    //cin >> T;
    while(T--)
        solve();
}}
'''


def section_title(folder: str) -> str:
    return folder.split("_", 1)[1].replace("_", " ").title()


def main() -> None:
    created = 0
    skipped = 0

    for folder, problems in SECTIONS.items():
        cpp_dir = ROOT / folder / "cpp"
        cpp_dir.mkdir(parents=True, exist_ok=True)
        existing = list_existing_stems(cpp_dir)

        for idx, problem in enumerate(problems, start=1):
            filename = canonical_name(idx, problem)
            path = cpp_dir / filename

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

    print(f"Created {created} placeholder files")
    print(f"Skipped {skipped} existing/solved problems")


if __name__ == "__main__":
    main()
