#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: conllu_aligned_comparator.py
Description: CoNLL-U syntactic comparator that loads a sentence alignment
             table from an external CSV or JSON file, then compares DEPREL
             relations between Latin and English CoNLL-U files and suggests
             corrections for the Latin file.
Author: DH Student
Date: 2026-04-18
Version: 2.0

Workflow:
    1. Load alignment table from alignment_table.csv OR alignment_table.json
    2. Read Latin and English CoNLL-U files
    3. For each aligned pair: compare DEPREL sets
    4. Print a report of differences + export deprel_diff_report.csv
    5. Apply corrections via CORRECTIONS dict
    6. Save corrected Latin CoNLL-U file

Usage:
    python conllu_aligned_comparator.py

    Files expected in the same directory:
        alignment_table.csv   OR   alignment_table.json
        confessio_latin.conllu
        confessio_english.conllu
"""

# ── Imports ───────────────────────────────────────────────────────────────────
import ast
import csv
import json
from pathlib import Path
from dataclasses import dataclass, field

# ── Base directory: folder where THIS script lives ───────────────────────────
# This means all files are looked up relative to the script,
# not relative to wherever you run the terminal from.
BASE_DIR = Path(__file__).parent


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION — only edit the filenames, not the full paths
# ══════════════════════════════════════════════════════════════════════════════

LATIN_FILE      = BASE_DIR / "5.Confessio_Latin.conllu"
ENGLISH_FILE    = BASE_DIR / "4.Confessio_Eng.conllu"
OUTPUT_FILE     = BASE_DIR / "6.Confessio_Latin_corrected.conllu"
REPORT_CSV      = BASE_DIR / "7.deprel_diff_report.csv"

# Alignment table: script tries CSV first, then JSON.
# Update the filenames below to match your actual file names.
ALIGNMENT_CSV   = BASE_DIR / "1.alignment_table_final.csv"
ALIGNMENT_JSON  = BASE_DIR / "2.alignment_table.json"


# ══════════════════════════════════════════════════════════════════════════════
# CORRECTIONS TABLE
# Fill this after reviewing the diff report.
#
# Format:
#   pair_id (int): [
#       {"sent_index": int,    # 0-based Latin sentence index
#        "token_id":   str,    # token ID as string, e.g. "5"
#        "new_deprel": str,    # new DEPREL value (optional)
#        "new_head":   str},   # new HEAD value   (optional)
#   ]
#
# Example (uncomment and adapt):
# CORRECTIONS = {
#     1: [
#         {"sent_index": 0, "token_id": "2",
#          "new_deprel": "appos", "new_head": "3"},
#     ],
# }
# ══════════════════════════════════════════════════════════════════════════════

CORRECTIONS: dict[int, list[dict]] = {
    # Fill after reviewing the report
}


# ══════════════════════════════════════════════════════════════════════════════
# ALIGNMENT TABLE LOADER
# ══════════════════════════════════════════════════════════════════════════════

def load_alignment_csv(path: str) -> list[tuple]:
    """
    Load alignment table from a CSV file.

    Supports two column naming conventions automatically:

    Convention A (original):
        pair_id, align_type, latin_indices, english_indices, ...

    Convention B (your actual file):
        pair_id, align_type, latin_sent_id, latin_index,
        english_sent_ids, english_indices, ...

    latin_index / english_indices are stored as integers or Python list
    literals e.g. "[0]" or "[1, 2]" — parsed with ast.literal_eval.

    Returns list of tuples: (pair_id, align_type, latin_indices, english_indices)
    """

    def parse_index_field(value: str) -> list[int]:
        """
        Parse an index field that may be:
          - a plain integer:  "0"      → [0]
          - a list literal:   "[0]"    → [0]
          - a multi-list:     "[1, 2]" → [1, 2]
        """
        value = value.strip()
        if value.startswith("["):
            return ast.literal_eval(value)
        return [int(value)]

    table = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []

        # Detect which convention the file uses
        use_convention_b = "latin_index" in headers and "latin_sent_id" in headers

        for row in reader:
            pair_id    = int(row["pair_id"])
            align_type = row["align_type"].strip()

            if use_convention_b:
                # Convention B: latin_index + english_indices columns
                lat_indices = parse_index_field(row["latin_index"])
                eng_indices = parse_index_field(row["english_indices"])
            else:
                # Convention A: latin_indices + english_indices columns
                lat_indices = parse_index_field(row["latin_indices"])
                eng_indices = parse_index_field(row["english_indices"])

            table.append((pair_id, align_type, lat_indices, eng_indices))
    return table


def load_alignment_json(path: str) -> list[tuple]:
    """
    Load alignment table from a JSON file.

    Expected structure: list of objects with keys:
        pair_id, align_type, latin_indices, english_indices

    Returns list of tuples: (pair_id, align_type, latin_indices, english_indices)
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    table = []
    for entry in data:
        table.append((
            int(entry["pair_id"]),
            entry["align_type"],
            entry["latin_indices"],
            entry["english_indices"],
        ))
    return table


def load_alignment_table() -> list[tuple]:
    """
    Auto-detect and load the alignment table.
    Tries CSV first (ALIGNMENT_CSV), then JSON (ALIGNMENT_JSON).
    Raises FileNotFoundError if neither exists.
    """
    if Path(ALIGNMENT_CSV).exists():
        print(f"Loading alignment table from CSV: {ALIGNMENT_CSV}")
        return load_alignment_csv(ALIGNMENT_CSV)

    if Path(ALIGNMENT_JSON).exists():
        print(f"Loading alignment table from JSON: {ALIGNMENT_JSON}")
        return load_alignment_json(ALIGNMENT_JSON)

    raise FileNotFoundError(
        f"No alignment table found. Expected '{ALIGNMENT_CSV}' or '{ALIGNMENT_JSON}' "
        f"in the current directory."
    )


# ══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Token:
    """One token/word in CoNLL-U format."""
    id:     str
    form:   str
    lemma:  str
    upos:   str
    xpos:   str
    feats:  str
    head:   str
    deprel: str
    deps:   str
    misc:   str

    def to_conllu_line(self) -> str:
        """Serialize back to a CoNLL-U tab-separated line."""
        return "\t".join([
            self.id, self.form, self.lemma, self.upos, self.xpos,
            self.feats, self.head, self.deprel, self.deps, self.misc,
        ])


@dataclass
class Sentence:
    """One sentence: list of tokens + original comment lines."""
    tokens:   list[Token] = field(default_factory=list)
    comments: list[str]   = field(default_factory=list)

    def deprel_set(self) -> set[str]:
        """Return set of unique DEPREL values (skip multiword/empty nodes)."""
        return {t.deprel for t in self.tokens
                if "-" not in t.id and "." not in t.id}

    def preview(self, n: int = 60) -> str:
        """First N characters of the sentence text."""
        text = " ".join(t.form for t in self.tokens)
        return text[:n] + ("…" if len(text) > n else "")


# ══════════════════════════════════════════════════════════════════════════════
# CONLL-U I/O
# ══════════════════════════════════════════════════════════════════════════════

def read_conllu(filepath: str) -> list[Sentence]:
    """
    Read a CoNLL-U file and return a list of Sentence objects.
    Preserves comment lines per sentence.
    Skips multiword token lines (ID contains '-') and empty nodes ('.').
    """
    sentences: list[Sentence] = []
    current = Sentence()

    with open(filepath, encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")

            if line.startswith("#"):
                current.comments.append(line)
                continue

            if line == "":
                if current.tokens:
                    sentences.append(current)
                    current = Sentence()
                continue

            parts = line.split("\t")
            if len(parts) != 10:
                continue

            token_id = parts[0]
            if "-" in token_id or "." in token_id:
                continue

            current.tokens.append(Token(*parts))

    if current.tokens:
        sentences.append(current)

    return sentences


def write_conllu(sentences: list[Sentence], output_path: str) -> None:
    """Write a list of Sentence objects back to CoNLL-U format."""
    with open(output_path, "w", encoding="utf-8") as f:
        for sent in sentences:
            for comment in sent.comments:
                f.write(comment + "\n")
            for tok in sent.tokens:
                f.write(tok.to_conllu_line() + "\n")
            f.write("\n")
    print(f"\n✅ Saved corrected file: {output_path}")


# ══════════════════════════════════════════════════════════════════════════════
# DEPREL COMPARISON
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class DiffEntry:
    """Difference between one aligned Latin–English sentence pair."""
    pair_id:       int
    align_type:    str
    lat_preview:   str
    eng_preview:   str
    only_in_latin: list[str]
    only_in_eng:   list[str]
    shared:        list[str]


def compare_pair(
    pair_id:     int,
    align_type:  str,
    lat_sents:   list[Sentence],
    eng_sents:   list[Sentence],
    lat_indices: list[int],
    eng_indices: list[int],
) -> DiffEntry:
    """
    Compare DEPREL sets for one aligned pair.
    Merges sentences when alignment is 1-2, 2-1, or 1-3.
    """
    lat_ok = [i for i in lat_indices if i < len(lat_sents)]
    eng_ok = [i for i in eng_indices if i < len(eng_sents)]

    if not lat_ok or not eng_ok:
        return DiffEntry(
            pair_id=pair_id, align_type=align_type,
            lat_preview="[index out of range]",
            eng_preview="[index out of range]",
            only_in_latin=[], only_in_eng=[], shared=[],
        )

    lat_deprels: set[str] = set()
    for i in lat_ok:
        lat_deprels |= lat_sents[i].deprel_set()

    eng_deprels: set[str] = set()
    for j in eng_ok:
        eng_deprels |= eng_sents[j].deprel_set()

    lat_preview = " / ".join(lat_sents[i].preview(50) for i in lat_ok)
    eng_preview = " / ".join(eng_sents[j].preview(50) for j in eng_ok)

    return DiffEntry(
        pair_id=pair_id,
        align_type=align_type,
        lat_preview=lat_preview,
        eng_preview=eng_preview,
        only_in_latin=sorted(lat_deprels - eng_deprels),
        only_in_eng=sorted(eng_deprels - lat_deprels),
        shared=sorted(lat_deprels & eng_deprels),
    )


def run_comparison(
    alignment_table: list[tuple],
    lat_sents:       list[Sentence],
    eng_sents:       list[Sentence],
) -> list[DiffEntry]:
    """Run comparison for all pairs in the alignment table."""
    return [
        compare_pair(pid, atype, lat_sents, eng_sents, lat_idx, eng_idx)
        for (pid, atype, lat_idx, eng_idx) in alignment_table
    ]


# ══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ══════════════════════════════════════════════════════════════════════════════

def print_report(results: list[DiffEntry]) -> None:
    """Print a human-readable diff report to the terminal."""
    print("\n" + "═" * 100)
    print("  DEPREL DIFFERENCE REPORT")
    print("═" * 100)

    problems = [r for r in results if r.only_in_latin or r.only_in_eng]
    clean    = [r for r in results if not r.only_in_latin and not r.only_in_eng]

    print(f"\n  ✅ Pairs with matching DEPREL sets : {len(clean)}")
    print(f"  ⚠️  Pairs with differences          : {len(problems)}\n")

    for r in problems:
        print(f"  Pair #{r.pair_id:>2}  [{r.align_type}]")
        print(f"  Latin  : {r.lat_preview}")
        print(f"  English: {r.eng_preview}")
        if r.only_in_latin:
            print(f"  ❌ Only in Latin  : {r.only_in_latin}")
        if r.only_in_eng:
            print(f"  ❌ Only in English: {r.only_in_eng}")
        print(f"  ✅ Shared         : {r.shared}")
        print("  " + "-" * 96)


def export_report_csv(results: list[DiffEntry], output_path: str) -> None:
    """Export diff report to CSV for review in Excel or Obsidian."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "pair_id", "align_type",
            "latin_preview", "english_preview",
            "only_in_latin", "only_in_english",
            "shared", "has_diff",
        ])
        for r in results:
            writer.writerow([
                r.pair_id, r.align_type,
                r.lat_preview, r.eng_preview,
                "; ".join(r.only_in_latin),
                "; ".join(r.only_in_eng),
                "; ".join(r.shared),
                "YES" if (r.only_in_latin or r.only_in_eng) else "no",
            ])
    print(f"✅ CSV report saved: {output_path}")


# ══════════════════════════════════════════════════════════════════════════════
# CORRECTIONS
# ══════════════════════════════════════════════════════════════════════════════

def apply_corrections(
    lat_sents:   list[Sentence],
    corrections: dict[int, list[dict]],
) -> int:
    """
    Apply corrections from the CORRECTIONS dict to Latin sentences in place.
    Returns number of corrections applied.
    """
    count = 0

    for pair_id, fixes in corrections.items():
        for fix in fixes:
            si  = fix.get("sent_index")
            tid = fix.get("token_id")

            if si is None or tid is None:
                print(f"  ⚠️  Pair {pair_id}: missing sent_index or token_id — skipped")
                continue
            if si >= len(lat_sents):
                print(f"  ⚠️  Pair {pair_id}: sent_index {si} out of range — skipped")
                continue

            for tok in lat_sents[si].tokens:
                if tok.id == tid:
                    if "new_deprel" in fix:
                        old, tok.deprel = tok.deprel, fix["new_deprel"]
                        print(f"  ✏️  Pair {pair_id} | sent {si} | '{tok.form}' "
                              f"DEPREL: {old} → {tok.deprel}")
                        count += 1
                    if "new_head" in fix:
                        old, tok.head = tok.head, fix["new_head"]
                        print(f"  ✏️  Pair {pair_id} | sent {si} | '{tok.form}' "
                              f"HEAD: {old} → {tok.head}")
                        count += 1
                    break
            else:
                print(f"  ⚠️  Pair {pair_id}: token_id '{tid}' not found in sent {si}")

    return count


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:

    # ── 1. Check CoNLL-U files exist ──────────────────────────────────────────
    for path in [LATIN_FILE, ENGLISH_FILE]:
        if not Path(path).exists():
            print(f"❌ File not found: {path}")
            print("   Update LATIN_FILE / ENGLISH_FILE at the top of the script.")
            return

    # ── 2. Load alignment table (CSV or JSON, auto-detected) ──────────────────
    try:
        alignment_table = load_alignment_table()
        print(f"  → {len(alignment_table)} sentence pairs loaded")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    # ── 3. Load CoNLL-U files ─────────────────────────────────────────────────
    print(f"\nLoading: {LATIN_FILE}")
    lat_sents = read_conllu(LATIN_FILE)
    print(f"  → {len(lat_sents)} Latin sentences")

    print(f"Loading: {ENGLISH_FILE}")
    eng_sents = read_conllu(ENGLISH_FILE)
    print(f"  → {len(eng_sents)} English sentences")

    # ── 4. Run DEPREL comparison ──────────────────────────────────────────────
    print("\nRunning DEPREL comparison...")
    results = run_comparison(alignment_table, lat_sents, eng_sents)

    # ── 5. Print + export report ──────────────────────────────────────────────
    print_report(results)
    export_report_csv(results, REPORT_CSV)

    # ── 6. Apply corrections ──────────────────────────────────────────────────
    if CORRECTIONS:
        print("\nApplying corrections...")
        n = apply_corrections(lat_sents, CORRECTIONS)
        print(f"  → {n} correction(s) applied")
    else:
        print("\nℹ️  No corrections defined yet.")
        print("   Review the report, then fill the CORRECTIONS dict at the top of this script.")

    # ── 7. Save corrected Latin CoNLL-U ──────────────────────────────────────
    write_conllu(lat_sents, OUTPUT_FILE)
    print("\nDone ✅")


if __name__ == "__main__":
    main()
