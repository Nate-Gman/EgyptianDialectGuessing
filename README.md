# Egyptian Dialect Guess — picture-first story decipherer

> **This program produces guesses.** It is not a verified decipherment,
> not a proven translator, and not a sign-to-letter/sign-to-number system.
> Every definition, AUTO story, motif, cluster proverb, English rendering,
> historical semantic candidate, local-corroboration score, and book-level
> translation is a labeled hypothesis.
>
> Internal consistency means the program followed its own rules. It does
> **not** prove that any proposed English wording was the historical meaning.

## 1. Purpose

The program treats Egyptian-looking marks as a **picture language**:

1. identify the literal picture when possible;
2. store several possible uses for that picture;
3. place pictures in a top-to-bottom column;
4. choose one contextual use per occurrence;
5. explain how neighboring pictures changed that choice;
6. keep the result explicitly marked as a hypothesis.

A bird picture may therefore be stored as a literal bird, a traveller, an
actor, a result, or another candidate. The story engine chooses between those
possibilities according to the column around it. The same mark can receive a
different selected use at each occurrence.

## 2. Honest status

Current internally checked state:

- **10,042** catalogue marks, including picture signs, layout controls, PUA
  signary entries, unencoded series, and related scripts.
- **5,085** pictured Egyptian signs receive proposal candidates.
- **5,085/5,085** pictured signs have multi-use language metadata.
- **26,228** guessed uses are reported by the coverage metric.
- **0 duplicate candidate-definition texts**.
- **0/5,085** pictured signs are externally verified.
- **11/5,085** pictured signs are locally corroborated by internal agreement.

These are not different names for accuracy:

| Metric | Meaning | Proof level |
| --- | --- | --- |
| proposal coverage | signs with at least one guess | no proof |
| multi-use coverage | signs with noun/verb/adjective-like candidates | no proof |
| format-ready | candidate has mode, function, and register metadata | internal only |
| local corroboration | several internal checks agree | internal only |
| coherent book | saved columns render without gaps and with a readable spine | internal only |
| external verification | same use manually attested in two distinct transcribed columns | recorded judgment, still not outside validation |

A 100% internal score never means “100% deciphered.”

## 3. Startup pipeline

**Runtime requirements:** Python 3.10+ and the included local fonts/data.
The console/reporting path uses only the standard library. `pygame` is
required for the scribe window. Rebuilding or verifying glyph tiles requires
`pymupdf`, `pillow`, `numpy`, and `fontTools`; the checked-in `glyphs/` PNGs
allow normal use without rebuilding them.

`main()` builds the working model in this order:

1. `build_catalogue()` creates every recorded mark and its shelf ID,
   Unicode codepoint where available, block/genre, xref links, and literal
   depiction label.
2. `seed_rosetta()` adds the sixteen-sign Rosetta base column, its shape
   links, and explicitly labeled seed guesses.
3. `apply_picture_guesses()` adds the layered proposal set:
   - hand-written picture guesses;
   - catalogue depiction/category scaffolds;
   - PHRP semantic candidates marked `historical-candidate`;
   - generated multi-use noun/verb/adjective variables;
   - language-format metadata;
   - local-correlation annotations.
4. `Dialect.load()` overlays `egyptian_dialect.json`, restoring personal
   definitions, saved columns, learned correlations, clusters, attestations,
   explicit clears, and individually removed guesses.
5. The command-line flag selects a report, or the interactive window opens;
   if the window cannot open in a terminal session, the console starts.

Personal definitions stay primary where possible. Cleared signs remain
cleared, and removed built-in guesses do not return after save/load.

## 4. Sign data model

Each `Sign` represents one catalogue item:

- `sid`: stable shelf ID such as `N01`, `K001`, `V001C`, `X-13460`,
  `P-1234`, or `H-001`.
- `char`: Unicode character when one exists.
- `cp`: integer codepoint when available.
- `kind`: `sign`, `rosetta`, `mark`, or `ink`.
- `block`: the catalogue block/genre, used by the GENRE dropdown.
- `depicts`: literal pictured object or category label — the image, not the
  assumed meaning.
- `defs`: ordered candidate meanings; `defs[0]` is the primary candidate.
- `xref`: shelf IDs of visually similar shapes. Xrefs are comparison clues,
  not meaning transfers.
- `note`: user/research note.

Each candidate definition is a dictionary:

| Field | Purpose |
| --- | --- |
| `text` | human-readable proposed use |
| `src` | where the hypothesis came from |
| `conf` | `guess`, `assumed`, or a user endorsement label |
| `mode` | `literal`, `metaphorical`, `action`, `contextual`, `evolved`, or `historical` |
| `func` | story role such as `actor`, `action`, `place`, `yield`, `rest` |
| `reg` | register such as `noun`, `verb`, `adj`, or `adj+verb` |
| `also` | optional second simultaneous sense |
| `flex` | note explaining context-dependent flexibility |
| `scope` | `specific`, `catalogue-coverage`, `multi-use-format`, or `historical-candidate` |
| `concrete` | optional locked-reading flag |
| `local` | internal corroboration score/checks, never external evidence |

The same literal object and its language use are deliberately separate:
`depicts` says what the mark draws; `defs` say what the mark may be doing in
a particular story.

## 5. Candidate generation layers

### Specific picture guesses

A small curated layer gives explicit testable hypotheses for photographed
and useful catalogue signs, such as fish+water, bird travel, a resting
person, a weeping eye, and walking legs.

### Catalogue-coverage guesses

A pictured sign with no personal/specific reading receives generated
candidates based on its depiction and category. Example:

```text
a rope variant catalogued as V001C: the pictured thing is present
a rope variant catalogued as V001C: may mark food, goods, or work nearby
```

The catalogue form is included so different rope signs do not share identical
definition text.

### Historical semantic candidates

`historical_uses.json` plus curated entries supply conventional ideogram or
determinative glosses. They are marked `historical-candidate`, retain the
catalogue form, and never replace personal readings. Phonetic values,
alphabetic mappings, and numeric values are excluded.

### Multi-use variables

Every pictured sign can behave as a language variable rather than only a
noun. Candidates include action, qualifier/classifier, and
result/consequence uses. This allows a picture to flex with its neighbors
instead of receiving one permanent translation.

### Language-format tagging

`apply_language_format()` ensures candidates carry mode, function, and
register fields. These tags let the scorer compare candidates as story
roles; they are not claims about real Egyptian grammar.

## 6. How the AUTO story chooses meanings

`_positions()` converts a column into ordered sign positions. `[` and `]`
mark a condensed group: enclosed members receive the same group ID and may
also be read by a known whole-proverb cluster.

`_select()` then chooses one candidate per occurrence. Selection is a
sequence problem, not an independent dictionary lookup:

1. Single-candidate signs anchor first.
2. Ambiguous candidates are scored by shared imagery tokens, role metadata,
   position, learned correlations, and already chosen neighbors.
3. Neighbor influence decays with distance.
4. Signs inside the same bracketed group have doubled context weight.
5. Verb-like positions pull actor/object/place/yield candidates toward
   themselves; count marks bind to the action they quantify.
6. Opening positions favor opener-like roles; closing positions favor
   result/recovery/sustain/rest-like roles.
7. The first greedy pass is followed by whole-column refinement sweeps.
8. A grammar-balance pass prevents a column from collapsing into nouns when
   a candidate can supply the needed action role.
9. An English-form pass tries alternatives that better fill subject,
   action, complement, and closure slots.

A candidate gets whole-column token support only when another sign's
candidate vocabulary supports that token; it cannot score itself as its own
context. Learned correlation weights are used only where the involved uses
have distinct-column corroboration, so `teach` cannot masquerade as outside
evidence.

The result is still only the engine's best hypothesis for this column.

## 7. Clusters and multi-symbol changes

Two related mechanisms model “a group means more than its parts”:

- `MOTIF_RULES` match adjacent ordered pairs such as fish+water or
  bird+eye and return competing picture-proverb readings.
- `clusters` are unordered sign sets that can be read as one whole proverb
  when wrapped in `[ ... ]`.

A cluster can have multiple whole readings. `_cluster_pick()` chooses the
one whose vocabulary best agrees with both the grouped signs and the rest of
the column. Inserting or removing a symbol can therefore change:

- an individual sign's selected definition;
- a neighboring sign's role;
- a pair motif;
- the cluster's whole-proverb choice;
- the rendered English-form sentence;
- every occurrence-specific `NOTE:`.

## 8. AUTO story output anatomy

`read_column()` prints a decorated column, role spine, and story. For each
defined sign it shows:

- literal depiction/name;
- selected candidate text;
- confidence and mode;
- story function and register;
- alternatives;
- flexibility and double-sense notes;
- an occurrence-specific `NOTE:`.

The `NOTE:` records:

- the picture to the left and right;
- the role this occurrence took;
- why the neighbors pulled it toward that role;
- which alternative was displaced;
- whether the same mark occurs elsewhere in a different role;
- an adjacent-pair motif when one exists;
- whether it is at the opening or closing edge.

A single-use sign may be rendered “as itself” when the column does not call
for the stored use. An unknown/missing sign is shown honestly rather than
being silently translated.

## 9. Reading laws used by the model

- Read top-to-bottom within a column.
- Read columns left-to-right as separate records.
- An out-of-place picture may be a picture-proverb.
- A circled/condensed group may represent one whole paragraphic concept.
- Unread marks stay unknown; no borrowed decipherment key is assumed.
- Neighboring marks affect each other; the pictures before and after a mark
  help determine its selected use.

## 10. Interactive scribe window

Run without arguments, or use:

```powershell
python Egyptian.py --window
```

The window has three resizable panes:

- **ALL MARKS:** catalogue browser and drag source;
- **COLUMN:** scratch column being composed;
- **THE STORY:** live AUTO reading of the scratch column.

### Palette

- `ALL` shows 500 marks per page and currently has 21 pages.
- `<` / `>`, PageUp, and PageDown move between pages.
- `GENRE` opens a dropdown listing catalogue blocks and mark counts.
- Mouse wheel scrolls within the current page only.
- Tile size and column count rescale when the marks pane is resized.

### Search

- `SEARCH` indexes shelf IDs and candidate-definition vocabulary once.
- Definition and alternate-use terms rank above literal depiction/notes.
- Prefix, substring, and same-initial fuzzy matching are supported.
- Suggestion chips display the candidate definition that caused the match.
- Enter inserts the selected suggestion; exact shelf IDs also work.

### Column editing

- Drag a palette tile into the column to insert at a position.
- Drag an existing column tile to reorder it.
- Right-click a column tile to remove it.
- `[` opens a condensed group and `]` closes it.
- Backspace erases typed input first, then removes the last mark.
- Delete removes the last mark.
- Escape clears search input.
- `R` manually refreshes the story.
- `Ctrl+K` keeps the scratch column and reinforces the selected readings.
- `Ctrl+S` saves `egyptian_dialect.json`.

Every structural edit calls the story refresh; the AUTO reading is not a
static string.

## 11. Console workflow

Run:

```powershell
python Egyptian.py --console
```

Common workflow:

```text
compose                    build a scratch column
N01                        add a sign while composing
[ N08 N09 ]                mark a condensed group
read                       render the AUTO story
keep my-column             save and endorse the current column
page                       read saved columns left-to-right
show V001C                 inspect all candidate uses
define V001C <meaning>     add a personal candidate
prefer V001C 2             make candidate #2 primary
mode V001C 1 literal       tag the candidate mode
func V001C 1 yield         tag its story function
reg V001C 1 noun           tag its register
flex V001C 1 <note>        record context flexibility
double V001C 1 <sense>     attach a second sense
undefine V001C [n]         remove all or one candidate
cluster N08 N09 <meaning>  define a whole-proverb group
transcribe image review-id  machine-match image cells for review
review [review-id]         inspect candidate matches
pick review-id cell n|sid  choose a shelf mark for a cell
approve review-id name [n] save reviewed cells as a column
reject review-id           reject a transcription review
teach my-column            reinforce selected pairs in the matrix
attest source col sid n    record a manually reviewed use
audit [sid]                inspect evidence/coverage
save                       persist the dialect
```

`teach` and `keep` influence heuristic pair selection only. `attest` is the
operation that records an independent human review for progress metrics.

## 12. Command-line reports

```powershell
python Egyptian.py                    # interactive scribe window when possible
python Egyptian.py --window           # force the pygame writer
python Egyptian.py --console          # text console
python Egyptian.py --selftest --no-color
python Egyptian.py --stats --no-color
python Egyptian.py --knowledge --no-color
python Egyptian.py --guesses --no-color
python Egyptian.py --rosetta --no-color
python Egyptian.py --motifs [column] --no-color
python Egyptian.py --sources --no-color
python Egyptian.py --history [word] --no-color
python Egyptian.py --local [word] --no-color
python Egyptian.py --format --no-color
python Egyptian.py --book --no-color
python Egyptian.py --catalog [all|unknown|defined|marks|signs|rosetta|text]
python Egyptian.py --audit [sign-id] --no-color
python Egyptian.py --story <glyph-file> [translation-output.txt]
python Egyptian.py --translate <english.txt> <glyphs.txt> [retention-report.txt]
python Egyptian.py --transcribe <image> <review-id> [review.json] [--cells cells.txt]
python Egyptian.py --review [review-id]
python Egyptian.py --pick <review-id> <cell#> <candidate#|sid>
python Egyptian.py --approve <review-id> <column-name> [column#]
python Egyptian.py --reject <review-id>
python Egyptian.py --chart
python Egyptian.py --build-tiles [--verify]
python Egyptian.py --export
python Egyptian.py --laws
```

- `stats`: proposal and external-check coverage.
- `knowledge`: staged progress from proposal coverage to local corroboration
  and external checks.
- `guesses`: seeded and catalogue-level proposed stories.
- `motifs`: adjacent-pair picture hypotheses.
- `history`: external conventional semantic candidates, not proof.
- `local`: internally corroborated candidates, not proof.
- `format`: language-role/register coverage of the hypothesis set.
- `book`: coherence over distinct saved columns.
- `catalog`: browse every recorded mark, including undefined signs.
- `audit`: candidate senses and independent-column witness counts.
- `chart`: regenerate `egyptian_catalog.html`.
- `export`: write `egyptian_dialect.txt`.
- `selftest`: run the regression suite.

`--transcribe` is supervised image transcription, not OCR evidence. It finds
candidate cell regions, extracts photo ink, and ranks each crop against
`glyphs/*.png` using normalized shape masks, Dice overlap, chamfer distance,
and aspect/density descriptors. The optional `review.json` records bounding
boxes, ranked alternatives, status, and a warning that matches are proposals.

A `cells.txt` file can supply exact `x0,y0,x1,y1` regions when automatic page
segmentation is too coarse:

```text
6,16,89,77
6,80,89,114
6,119,89,177
```

Each cell starts as `candidate`. Use `--review` to inspect ranked marks,
`--pick` to choose one per cell, and `--approve` to create a saved column.
`--reject` marks a bad scan unusable. Approval only preserves the reviewed
shelf IDs; it creates no attestation and changes no verification count. A
separate `attest <source> <column> <sid> <reading#>` remains required for a
human-checked use, and verification still needs two distinct columns.

## 13. Glyph-book input and output

`--story` reads a text file containing actual glyph characters, shelf IDs,
or bracket markers:

```text
𓆟 𓈖 [ 𓅱 𓊻 ] 𓁹 | 𓄿 𓊵

next page starts after a blank line
```

Rules:

- blank lines separate pages;
- `|`, `¦`, or `‖` separates columns on a page;
- tokens may be spaced or contiguous glyph runs;
- `[` and `]` mark a condensed group;
- columns read top-to-bottom; page columns read left-to-right;
- unknown tokens are reported instead of invented.

The report includes page/column coherence, role spine, proposed story,
literal depiction, chosen use, source, sequence effect, evidence count,
alternatives, and motif explanations. Passing the optional output path writes
the report to disk.

## 14. English bridge mode

`--translate <english.txt> <glyphs.txt> [report]` is an experimental
proposal writer:

- content words map to a small bridge glossary or suggestion search;
- English grammar/context words are retained in the report, not drawn;
- every source token is listed as mapped, syntax, or unmapped;
- unmapped words remain explicit rather than being guessed as evidence.

Source-token retention can be 100%, but semantic equivalence is not
guaranteed. Non-English languages must first be translated to English by a
separate translator.

## 15. Persistence

`egyptian_dialect.json` version 4 stores:

- defined sign candidates and changed `depicts`/notes;
- explicitly cleared signs;
- individually removed generated guesses;
- saved columns;
- learned correlation matrix;
- cluster records;
- manual attestations;
- supervised image-transcription reviews (`candidate`, `human-reviewed`, or
  `rejected`);
- fingerprints of already-taught columns.

Loading merges the saved personal state with current built-in guesses.
Deleted generated guesses stay deleted through `removed_guesses`; fully
cleared signs stay cleared through `cleared`. Empty old-save entries do not
erase newly generated proposals.

## 16. Glyph tiles

The UI draws transparent 120×120 PNG tiles from `glyphs/`:

- authentic Unicode-chart crops where available;
- local font rendering for chart gaps;
- deterministic pictorial slot marks for unencoded series with no recorded
  digital shape.

`python Egyptian.py --build-tiles --verify` rebuilds and audits tile
presence, ink, tofu-box detection, mass duplication, and chart/font facing
variants. Pictorial placeholders are rendering aids only; they are not
claims about a lost sign's historical shape.

## 17. Correlation, learning, and evidence boundaries

The correlation matrix learns which selected candidate uses appear near one
another after `keep` or `teach`. It can nudge future selections, but it is
not independent evidence.

Manual `attest` entries are separated from heuristic learning. Progress
requires the same candidate text on the same sign to appear in two distinct
column contents. Duplicate columns and re-taught copies cannot inflate the
witness count or pair matrix. Image-transcription matches and approved
transcription columns are also excluded from evidence until `attest` records a
human-checked reading against an independently transcribed column.

Local corroboration combines depiction fit, candidate-layer agreement,
format metadata, role fit, selected-column use, motifs, and learned support.
It exists to rank hypotheses, not to certify them.

## 18. Main data files

- `Egyptian.py`: catalogue, engine, reports, persistence, and UI.
- `egyptian_dialect.json`: personal dialect state.
- `egyptian_dialect.txt`: exported human-readable record.
- `historical_uses.json`: extracted PHRP semantic candidates.
- `object_names.json`: catalogue depiction labels.
- `pua_names.json`: private-use signary slot mappings.
- `glyphs/*.png`: transparent tile images.
- `egyptian_catalog.html`: generated shaped catalogue/xref sheet.
- `DECIPHER_PROGRESS.md`: evidence and progress log.
- `SOURCE_REVIEW.md`: accepted visual-source boundaries.
- `DR_SEUSS_EXAMPLE_STORY.md`: glyph-book test input.
- `DR_SEUSS_EXAMPLE_TRANSLATION.txt`: generated proposal output.

## 19. Safe interpretation checklist

When reading output:

1. Check whether the text is marked `guess`, `assumed`, `historical`,
   `catalogue-coverage`, `multi-use-format`, or `locally-corroborated`.
2. Read the literal `depicts` separately from the selected `use`.
3. Inspect `NOTE:` to see why this occurrence chose that candidate.
4. Inspect alternatives before accepting the selected wording.
5. Treat motif and cluster output as competing picture stories.
6. Do not interpret book coherence or 100% proposal coverage as proof.
7. Use supervised transcription review, independent transcriptions, and manual
   attestations to advance a hypothesis toward recorded verification. A shape
   match only says two marks look similar.

## 20. Verification

Run:

```powershell
python Egyptian.py --selftest --no-color
```

A passing suite currently verifies catalogue size, proposal metadata,
sign-specific definitions, persistence, duplicate protection, context
insertion effects, cluster behavior, story notes, search, paging, genre
filtering, pane resizing, glyph tiles, and saved-column coherence.

It verifies that the software follows its stated model. It does not verify
the historical language itself.
