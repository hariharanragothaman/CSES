#!/usr/bin/env python3
"""
Clean all C++ files in the CSES repo to use a uniform, minimal template.
- Placeholder files → clean template with TODO
- Solved files → strip boilerplate, keep solution code
"""

import os
import re
import sys

CLEAN_PLACEHOLDER = '''\
#include <bits/stdc++.h>
using namespace std;

void solve() {
    // TODO: not solved
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
'''

BOILERPLATE_LINE_PATTERNS = [
    re.compile(r'^\s*#pragma GCC'),
    re.compile(r'^\s*#include\b'),
    re.compile(r'^\s*using namespace std'),
    re.compile(r'^\s*#define ONLINE_JUDGE'),
    re.compile(r'^\s*#define ENABLEFASTIO'),
    re.compile(r'^\s*#define stars\b'),
    re.compile(r'^\s*#define debug\b'),
    re.compile(r'^\s*#define f first'),
    re.compile(r'^\s*#define mp make_pair'),
    re.compile(r'^\s*#define pb push_back'),
    re.compile(r'^\s*#define eb emplace_back'),
    re.compile(r'^\s*#define lb lower_bound'),
    re.compile(r'^\s*#define ub upper_bound'),
    re.compile(r'^\s*#define rep\('),
    re.compile(r'^\s*#define trav\('),
    re.compile(r'^\s*#define sz\('),
    re.compile(r'^\s*#define double\b'),
    re.compile(r'^\s*typedef\b'),
    re.compile(r'^\s*using (i64|u64|i32|u32|ld)\b'),
    re.compile(r'^\s*using (vi|vl|vvi|vvl|pii|pll|vpii|vpll|iset|imap)\b'),
    re.compile(r'^\s*//-+\s*$'),
    re.compile(r'^\s*// For Hash'),
    re.compile(r'^\s*// For all useful constants'),
    re.compile(r'^\s*// Data-Structures'),
    re.compile(r'^\s*// Some basic typedef'),
    re.compile(r'^\s*// #defines for'),
    re.compile(r'^\s*// begin deepsigh'),
    re.compile(r'^\s*// end deepsigh'),
    re.compile(r'^\s*// BEGIN NO SAD'),
    re.compile(r'^\s*// END NO SAD'),
    re.compile(r'^\s*// Binary Search comforts'),
    re.compile(r'^\s*//\s*Includes Priority Queue'),
    re.compile(r'^\s*/\*\s*BEGIN HEADER FILES'),
    re.compile(r'^\s*/\*\s*END HEADER FILES'),
    re.compile(r'^\s*//#define\s+(min|max)\('),
    re.compile(r'^\s*//static const int ENABLEFASTIO'),
]

TYPE_EXPAND = {
    'vi': 'vector<int>',
    'vl': 'vector<long long>',
    'vvi': 'vector<vector<int>>',
    'vvl': 'vector<vector<long long>>',
    'll': 'long long',
    'pii': 'pair<int,int>',
    'pll': 'pair<long long,long long>',
    'vpii': 'vector<pair<int,int>>',
    'vpll': 'vector<pair<long long,long long>>',
    'iset': 'set<int>',
    'imap': 'map<int,int>',
}

MACRO_EXPAND = {
    'pb': 'push_back',
    'eb': 'emplace_back',
    'mp': 'make_pair',
}


def is_placeholder(content):
    return '// TODO: not solved' in content


def remove_header_comments(lines):
    """Remove leading comment blocks: /** ... */, /* ... */, // Created by..."""
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1

    if i >= len(lines):
        return lines

    start = i

    if lines[i].strip().startswith('/**') or lines[i].strip().startswith('/*'):
        while i < len(lines):
            if '*/' in lines[i]:
                i += 1
                break
            i += 1
        while i < len(lines) and lines[i].strip() == '':
            i += 1
        if i < len(lines) and (lines[i].strip().startswith('/*') or lines[i].strip().startswith('//')):
            if lines[i].strip().startswith('/*'):
                while i < len(lines):
                    if '*/' in lines[i]:
                        i += 1
                        break
                    i += 1
            else:
                while i < len(lines) and lines[i].strip().startswith('//'):
                    i += 1
        return lines[i:]

    if lines[i].strip().startswith('//'):
        while i < len(lines) and (lines[i].strip().startswith('//') or lines[i].strip() == ''):
            if lines[i].strip().startswith('//') and not lines[i].strip().startswith('// Created') and not lines[i].strip().startswith('//\n'):
                if i > start + 2:
                    break
            i += 1
        return lines[i:]

    return lines


def remove_ifdef_blocks(lines):
    """Remove #ifndef ONLINE_JUDGE...#endif and #ifdef LOCAL...#endif blocks."""
    result = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()

        if stripped.startswith('#ifndef ONLINE_JUDGE') or stripped.startswith('#ifdef LOCAL'):
            depth = 1
            i += 1
            while i < len(lines) and depth > 0:
                s = lines[i].strip()
                if s.startswith('#if'):
                    depth += 1
                elif s.startswith('#endif'):
                    depth -= 1
                elif s.startswith('#else') and depth == 1:
                    pass
                i += 1
            continue

        if stripped == '//#define LOCAL' or stripped == '#define LOCAL':
            i += 1
            continue

        result.append(lines[i])
        i += 1

    return result


def remove_block_comments(lines):
    """Remove specific block comments (advice blocks, FOCUS+DETERMINATION, etc.)."""
    result = []
    i = 0
    skip_patterns = [
        'Some General Advice',
        'FOCUS + DETERMINATION',
        'BEGIN HEADER FILES',
    ]
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith('/*'):
            block_start = i
            block_text = stripped
            j = i
            while j < len(lines) and '*/' not in lines[j][lines[j].find('/*')+2 if j == i else 0:]:
                block_text += lines[j]
                j += 1
            if j < len(lines):
                block_text += lines[j]
            if any(pat in block_text for pat in skip_patterns):
                i = j + 1
                continue
        result.append(lines[i])
        i += 1
    return result


def remove_print_template(lines):
    """Remove template<typename T> void print(...) function."""
    result = []
    i = 0
    while i < len(lines):
        if re.search(r'template\s*<', lines[i]) and i + 1 < len(lines) and 'void print' in lines[i + 1]:
            depth = 0
            found_open = False
            i += 1
            while i < len(lines):
                depth += lines[i].count('{') - lines[i].count('}')
                if '{' in lines[i]:
                    found_open = True
                i += 1
                if found_open and depth == 0:
                    break
            continue
        result.append(lines[i])
        i += 1
    return result


def remove_fast_io_function(lines):
    """Remove inline void fast_io() { ... } function definition."""
    result = []
    i = 0
    while i < len(lines):
        if re.match(r'^\s*inline\s+void\s+fast_io\s*\(\)', lines[i]):
            depth = 0
            found_open = False
            while i < len(lines):
                depth += lines[i].count('{') - lines[i].count('}')
                if '{' in lines[i]:
                    found_open = True
                i += 1
                if found_open and depth == 0:
                    break
            continue
        result.append(lines[i])
        i += 1
    return result


def remove_boilerplate_lines(lines):
    """Remove individual lines matching known boilerplate patterns."""
    result = []
    for line in lines:
        if any(pat.match(line) for pat in BOILERPLATE_LINE_PATTERNS):
            continue
        result.append(line)
    return result


def unwrap_solution_class(lines):
    """Convert class Solution { public: ... }; to free functions."""
    has_solution_class = any(re.match(r'^\s*class Solution\s*$', l) for l in lines)
    if not has_solution_class:
        return lines

    result = []
    i = 0
    in_class = False
    class_depth = 0

    while i < len(lines):
        stripped = lines[i].strip()

        if re.match(r'^class Solution\s*$', stripped) and not in_class:
            in_class = True
            i += 1
            while i < len(lines) and lines[i].strip() in ('{', 'public:', ''):
                if '{' in lines[i]:
                    class_depth += 1
                i += 1
            continue

        if in_class:
            if stripped == '};' and class_depth == 1:
                in_class = False
                class_depth = 0
                i += 1
                continue

            if '{' in lines[i]:
                class_depth += lines[i].count('{')
            if '}' in lines[i]:
                class_depth -= lines[i].count('}')

            dedented = lines[i]
            if dedented.startswith('    '):
                dedented = dedented[4:]
            elif dedented.startswith('\t'):
                dedented = dedented[1:]
            result.append(dedented)
        else:
            result.append(lines[i])
        i += 1

    return result


def try_consume_wrapper(lines, start):
    """Try to consume a T=1/while(T--)/solve() wrapper starting at `start`.
    Returns (end_index, True) on success, (start+1, False) on failure."""
    i = start + 1

    def skip_blank():
        nonlocal i
        while i < len(lines) and lines[i].strip() == '':
            i += 1

    skip_blank()

    if i < len(lines) and re.match(r'^\s*T\s*=\s*1\s*;', lines[i].strip()):
        i += 1
        skip_blank()

    if i < len(lines) and '//cin >> T' in lines[i]:
        i += 1
        skip_blank()

    if i < len(lines) and re.match(r'^\s*Solution\s+\w+\s*;', lines[i].strip()):
        i += 1
        skip_blank()

    if i >= len(lines) or not re.match(r'^\s*while\s*\(\s*T\s*--\s*\)', lines[i].strip()):
        return start + 1, False

    while_line = lines[i].strip()
    if 'solve()' in while_line:
        return i + 1, True

    i += 1
    if i >= len(lines):
        return start + 1, False

    if 'solve()' in lines[i].strip() and '{' not in lines[i]:
        return i + 1, True

    if lines[i].strip() == '{':
        depth = 1
        i += 1
        while i < len(lines) and depth > 0:
            depth += lines[i].count('{') - lines[i].count('}')
            i += 1
        return i, True

    return start + 1, False


def fix_main(lines):
    """Clean up main() function: replace macros, simplify test case wrapper."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if 'ENABLEFASTIO()' in stripped and not stripped.startswith('#define'):
            indent = line[:len(line) - len(line.lstrip())]
            result.append(f'{indent}ios::sync_with_stdio(false);\n{indent}cin.tie(nullptr);\n')
            i += 1
            continue

        if stripped == 'fast_io();':
            indent = line[:len(line) - len(line.lstrip())]
            result.append(f'{indent}ios::sync_with_stdio(false);\n{indent}cin.tie(nullptr);\n')
            i += 1
            continue

        if 'cin.tie(NULL)' in line:
            line = line.replace('cin.tie(NULL)', 'cin.tie(nullptr)')

        if re.match(r'^\s*(int\s+T\s*=\s*1\s*;|int\s+T\s*;\s*)$', stripped):
            end, found = try_consume_wrapper(lines, i)
            if found:
                indent = line[:len(line) - len(line.lstrip())]
                result.append(f'{indent}solve();\n')
                i = end
                continue

        result.append(line)
        i += 1

    return result


def expand_type_aliases(lines, original_content):
    """Expand typedef/using aliases that appear in solution code."""
    code = '\n'.join(lines)
    for short, full in TYPE_EXPAND.items():
        pattern = re.compile(r'\b' + short + r'\b')
        if pattern.search(original_content):
            code = pattern.sub(full, code)
    for short, full in MACRO_EXPAND.items():
        pattern = re.compile(r'\b' + short + r'\b')
        if pattern.search(code):
            code = code.replace('.' + short + '(', '.' + full + '(')
    return code.split('\n')


def clean_whitespace(lines):
    """Collapse multiple consecutive blank lines into one."""
    result = []
    prev_blank = False
    for line in lines:
        is_blank = line.strip() == ''
        if is_blank and prev_blank:
            continue
        result.append(line)
        prev_blank = is_blank
    return result


def clean_solved_file(content):
    original = content
    lines = content.split('\n')

    has_int_ll = bool(re.search(r'^\s*#define\s+int\s+long\s+long', content, re.MULTILINE))
    has_endl_define = bool(re.search(r'^\s*#define\s+endl\s+"\\n"', content, re.MULTILINE))
    has_mod_define = re.search(r'^\s*#define\s+MOD\s+(\S+)', content, re.MULTILINE)
    has_all_macro = bool(re.search(r'^\s*#define\s+all\(', content, re.MULTILINE))

    lines = remove_header_comments(lines)
    lines = remove_block_comments(lines)
    lines = remove_ifdef_blocks(lines)
    lines = remove_print_template(lines)
    lines = remove_fast_io_function(lines)
    lines = remove_boilerplate_lines(lines)

    remaining = '\n'.join(lines)
    lines = [l for l in lines if not re.match(r'^\s*#define\s+(int\s+long\s+long|endl\s+"\\n"|MOD\s|all\()', l)]

    lines = unwrap_solution_class(lines)
    lines = expand_type_aliases(lines, original)
    lines = fix_main(lines)
    lines = clean_whitespace(lines)

    while lines and lines[0].strip() == '':
        lines.pop(0)
    while lines and lines[-1].strip() == '':
        lines.pop()

    header_lines = ['#include <bits/stdc++.h>', 'using namespace std;']

    remaining_code = '\n'.join(lines)
    all_used = 'all(' in remaining_code and has_all_macro
    mod_used = has_mod_define and 'MOD' in remaining_code

    if has_int_ll:
        header_lines.append('#define int long long')
    if has_endl_define:
        header_lines.append('#define endl "\\n"')
    if mod_used:
        header_lines.append(f'#define MOD {has_mod_define.group(1)}')
    if all_used:
        header_lines.append('#define all(x) x.begin(), x.end()')

    header_lines.append('')

    return '\n'.join(header_lines + lines) + '\n'


def process_file(filepath, dry_run=False):
    with open(filepath) as f:
        content = f.read()

    if is_placeholder(content):
        new_content = CLEAN_PLACEHOLDER
    else:
        new_content = clean_solved_file(content)

    if content != new_content:
        if dry_run:
            print(f"WOULD CHANGE: {filepath}")
        else:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Cleaned: {filepath}")
        return True
    return False


def main():
    dry_run = '--dry-run' in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    changed = 0
    total = 0

    for dirpath, dirnames, filenames in os.walk(root):
        if '.git' in dirpath:
            continue
        if 'scripts' in dirpath:
            continue
        for f in sorted(filenames):
            if f.endswith('.cpp'):
                total += 1
                filepath = os.path.join(dirpath, f)
                if process_file(filepath, dry_run):
                    changed += 1

    action = "Would change" if dry_run else "Changed"
    print(f"\n{action} {changed}/{total} files")


if __name__ == '__main__':
    main()
