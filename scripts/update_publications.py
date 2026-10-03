#!/usr/bin/env python3

import requests
import yaml
import bibtexparser
from pathlib import Path

OUTPUT = Path("downloads/mfis-pubs.bib")
AUTHORS_DIR = Path("downloads/authors")

# Tipos que queremos conservar
KEEP_TYPES = {
    "article",
    "inproceedings",
    "proceedings",
    "book",
    "incollection"
}

def load_bib_file(path):
    print(f"Reading {path.name}")

    with open(path, encoding="utf8") as f:
        return bibtexparser.loads(f.read())

def main():

    entries = {}

    for bib_file in AUTHORS_DIR.glob("*.bib"):
        print(str(bib_file))

        bib = load_bib_file(bib_file)

        print(f"Found {len(bib.entries)} entries")

        for entry in bib.entries:

            if entry["ENTRYTYPE"] not in KEEP_TYPES:
                continue

            entries[entry["ID"]] = entry

    print(f"Collected {len(entries)} unique publications.")

    # Orden descendente por año
    ordered = sorted(
        entries.values(),
        key=lambda e: int(e.get("year", 0)),
        reverse=True
    )

    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = ordered

    with open(OUTPUT, "w", encoding="utf8") as f:
        writer = bibtexparser.bwriter.BibTexWriter()
        writer.indent = "    "
        writer.order_entries_by = None
        f.write(writer.write(db))

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
