# Egyptian Dialect Guess — Program Overview

> **Important:** this project is a **picture-first hypothesis engine**, not a
> verified decipherment system. Every generated definition, AUTO story,
> historical candidate, motif, cluster proverb, shape match, and English
> rendering is a labeled guess unless independently reviewed. Internal
> consistency is not historical proof.

## What the program does

The program treats Egyptian-looking marks as visual language variables:

1. Catalogue the literal shape and shelf ID of each mark.
2. Store several possible story uses for that mark.
3. Place marks into top-to-bottom columns.
4. Select one use per occurrence according to the surrounding pictures.
5. Render a story hypothesis, role spine, alternatives, and explanations.
6. Let a human correct, save, review, and independently attest hypotheses.

A picture does not have to keep one fixed meaning. A bird can remain a bird in
one column, function as travel in another, and join a larger proverb when it
stands beside strokes or other marks.

## Current state

| Area | Current result |
| --- | --- |
| Catalogue | 10,042 recorded marks |
| Pictured Egyptian signs | 5,085 |
| Proposal coverage | 5,085/5,085 pictured signs |
| Multi-use metadata | 5,085/5,085 pictured signs |
| Candidate definitions | about 26,228 generated/loaded uses |
| Duplicate candidate text | 0 |
| Local corroboration | internal agreement only |
| External verification | 0/5,085 pictured signs |
| Regression suite | all checks pass |

The internal model is complete enough for experimentation, but historical
accuracy is still unproven.

## Main components

### 1. Catalogue layer

`build_catalogue()` creates all recorded marks, including:

- standard Egyptian hieroglyphs;
- Extended-A signs;
- format-control marks;
- ancient private-use signary entries;
- Coptic and Meroitic related scripts;
- ink-only Hieratic, Demotic, Proto-Sinaitic, Proto-Egyptian, and Early
  Dynastic series;
- the 16-sign Rosetta seed column and species variants.

Each sign has:

- `sid`: shelf ID such as `N01`, `K001`, `V001C`, `X-13460`;
- `depicts`: literal pictured object/category;
- `defs`: ordered candidate meanings;
- `xref`: visually similar signs;
- `kind`, `cp`, `block`, and `note`.

`defs[0]` is the primary candidate. Xrefs help compare shapes but never
transfer meaning.

### 2. Candidate-definition layers

The model combines several clearly labeled sources:

- curated picture guesses;
- catalogue depiction/category scaffolds;
- multi-use noun/verb/adjective-style variables;
- PHRP ideogram/determinative semantic candidates;
- personal user definitions;
- cluster and motif hypotheses;
- local-corroboration annotations.

Historical candidates do **not** import phonetic, alphabetic, or numeric
values. Personal definitions remain primary after save/load.

### 3. AUTO story engine

`read_column()` flattens the scratch column and calls `_select()` to choose
one candidate for each occurrence.

Selection considers:

- neighboring literal depictions;
- shared candidate vocabulary;
- distance-weighted context;
- bracket-group membership;
- positional opener/closer priors;
- actor/action/object/place/yield/transition/rest roles;
- learned correlation-matrix weights;
- adjacent-pair motifs;
- cluster/whole-proverb readings;
- verb-site and role-filler constraints;
- English-form subject/action/complement/closure refinement.

Every insertion, deletion, reordering, repeat, or bracket change refreshes the
entire story. `NOTE:` lines explain why an occurrence selected its current
use and which alternatives were displaced.

### 4. Motifs and clusters

- `MOTIF_RULES` recognize ordered adjacent pairs such as fish+water,
  fish+basket, bird+eye, bird+strokes, and shore+water.
- `[ ... ]` creates a condensed group that may receive one whole-proverb
  meaning.
- `_cluster_pick()` chooses a cluster reading according to group members and
  surrounding-column vocabulary.

A group can therefore mean more than its separate marks, but the selected
proverb remains an explicitly labeled interpretation.

## Interactive scribe window

Start with:

```powershell
python Egyptian.py
# or
python Egyptian.py --window
```

The window contains three resizable panes:

- **ALL MARKS**: the 10,042-mark palette;
- **COLUMN**: the scratch column being composed;
- **THE STORY**: the live AUTO interpretation.

### ALL MARKS pane

- 6+ columns depending on pane width;
- 500 marks per page;
- `ALL` produces 21 pages;
- `PAGE` buttons and PageUp/PageDown navigate;
- `GENRE` opens a counted dropdown;
- indexed search ranks definition matches first;
- suggestion chips show the actual matching candidate;
- glyph tiles rescale when the pane is widened.

### Defining a mark from the palette

1. Right-click a mark in **ALL MARKS**.
2. Click `DEFINE <sid>...`.
3. Type the corrective meaning in the bottom bar.
4. Press `ENTER`.

The meaning becomes `defs[0]`, is indexed for search immediately, and is saved
to `egyptian_dialect.json`, so it remains primary after relaunch. `ESC`
cancels. A correction is a saved personal hypothesis, not external evidence.

### F1 help

The top-center `F1 INFO / DEFINE` button opens the same explanation. Pressing
`F1` toggles the informational panel.

### COLUMN pane

- Drag palette marks into the column.
- Drag existing marks to reorder them.
- Right-click removes a mark.
- `[` and `]` create condensed proverb groups.
- The column scrolls independently.

### THE STORY pane

- Updates after every structural change.
- Shows role strip, guesses, `NOTE:` explanations, motifs, and alternatives.
- The story is clipped above the bottom search bar.
- Mouse wheel scrolls older/newer story lines.
- A scrollbar appears when content overflows.

### Bottom search/write bar

- `SEARCH >` finds marks by shelf ID, definition, depiction, or note.
- Misspellings use indexed same-initial fuzzy matching.
- `ENTER` inserts the selected suggestion.
- While defining a mark it becomes `DEFINE <sid> >`.

## Console and command-line operation

Interactive console:

```powershell
python Egyptian.py --console
```

Common console commands:

```text
compose                    build a scratch column
keep <name>                save and endorse it
read                       render the AUTO story
show <sid>                 inspect candidates
define <sid> <meaning>     add a personal candidate
prefer <sid> <n>           promote a candidate to primary
mode/func/reg/flex         tag hypothesis metadata
cluster <sids> <meaning>   define a whole-proverb group
teach <name>               reinforce selected pairs heuristically
attest <src> <col> <id> <n> record a manually reviewed use
review / pick / approve    transcription-review workflow
save / load                persist or reload state
```

Important reports:

```powershell
python Egyptian.py --selftest --no-color
python Egyptian.py --stats --no-color
python Egyptian.py --knowledge --no-color
python Egyptian.py --guesses --no-color
python Egyptian.py --motifs [column] --no-color
python Egyptian.py --history [word] --no-color
python Egyptian.py --local [word] --no-color
python Egyptian.py --format --no-color
python Egyptian.py --book --no-color
python Egyptian.py --audit [sid] --no-color
python Egyptian.py --catalog [filter] --no-color
python Egyptian.py --story <glyph-file> [output.txt]
python Egyptian.py --translate <english.txt> <glyphs.txt> [report.txt]
python Egyptian.py --chart
python Egyptian.py --build-tiles --verify
python Egyptian.py --export
```

## Supervised image transcription

`--transcribe` is a shape-review assistant, not OCR evidence.

It extracts ink from an image, attempts column/cell segmentation, and ranks
each region against `glyphs/*.png` using normalized masks, Dice overlap,
chamfer distance, and aspect/density descriptors.

Basic workflow:

```powershell
python Egyptian.py --transcribe image.png scan1 review.json
python Egyptian.py --review scan1
python Egyptian.py --pick scan1 1 K001
python Egyptian.py --approve scan1 scan-column 1
python Egyptian.py --reject scan1
```

For difficult images, exact manual cells can be supplied:

```text
# cells.txt
6,16,89,77
6,80,89,114
6,119,89,177
```

Then:

```powershell
python Egyptian.py --transcribe image.png scan1 --cells cells.txt
```

Review states are:

- `candidate` — machine proposal only;
- `human-reviewed` — a person picked the shelf ID;
- `rejected` — the scan was discarded.

`approve` creates a saved column but does **not** create evidence. The
separate `attest` command is still required for a manually checked reading.

## Evidence and verification boundary

The program deliberately separates several layers:

| Layer | Meaning |
| --- | --- |
| Guess | generated or personal hypothesis |
| Historical candidate | conventional semantic possibility, still not proof |
| Local corroboration | internal model agreement |
| Learned correlation | heuristic pair support |
| Shape match | two marks look visually similar |
| Human-reviewed transcription | person chose a shelf ID |
| Attestation | manually recorded use in an independent column |
| Verified | same use attested in two distinct transcribed columns |

Machine matches, generated stories, coherent books, and repeated teaching do
not advance verification. Duplicate columns do not count twice.

## Persistence

`egyptian_dialect.json` stores:

- personal candidate definitions and primary order;
- depictions and notes;
- cleared signs;
- removed generated guesses;
- saved columns;
- learned matrix weights;
- cluster records;
- manual attestations;
- supervised transcription reviews;
- fingerprints of already-taught columns.

Loading overlays the personal state onto freshly generated built-in guesses.
Removed guesses stay removed, cleared signs stay cleared, and personal
readings remain primary where possible.

## Glyph tiles

The UI uses transparent 120×120 PNG tiles in `glyphs/`:

- Unicode-chart crops where available;
- local font rendering for chart gaps;
- the supplied Rosetta crop for seed marks;
- deterministic pictorial placeholders for unencoded series.

All 10,042 catalogue marks currently have non-empty, non-tofu tile files.
`--build-tiles --verify` can rebuild and audit them.

## Main files

| File/folder | Purpose |
| --- | --- |
| `Egyptian.py` | engine, reports, persistence, and UI |
| `README.md` | full operating guide |
| `overview.md` | this project-wide summary |
| `DECIPHER_PROGRESS.md` | progress and evidence log |
| `SOURCE_REVIEW.md` | source boundaries and excluded mappings |
| `egyptian_dialect.json` | persistent personal state |
| `historical_uses.json` | extracted semantic candidates |
| `object_names.json` | depiction labels |
| `pua_names.json` | private-use mappings |
| `glyphs/` | 10,042 glyph tiles |
| `ReferenceDialect/` | supplied reference images |
| `CorrectedTestImages/` | corrected visual test fragments |
| `DR_SEUSS_EXAMPLE_STORY.md` | glyph-book test input |

## Safe interpretation checklist

Before treating an output as meaningful:

1. Check whether it is marked `guess`, `assumed`, `historical`,
   `catalogue-coverage`, `multi-use-format`, or `locally-corroborated`.
2. Read `depicts` separately from the selected `use`.
3. Read the occurrence-specific `NOTE:`.
4. Inspect alternative candidates.
5. Remember that a coherent story is only internally consistent.
6. Do not treat a shape match as transcription evidence.
7. Require human review and independent attestations before calling a result
   verified.

## Verification command

The authoritative regression check is:

```powershell
python Egyptian.py --selftest --no-color
```

Current result:

```text
all checks passed -- the dialect engine is sound
```

## Current limitation

The program is now a strong hypothesis/research workspace, but it has not
produced a verified decipherment. The next meaningful progress requires more
independently transcribed columns, human-reviewed sign identifications, and
repeated attestation of the same uses in different contexts.
