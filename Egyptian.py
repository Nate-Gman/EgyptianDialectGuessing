#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
 Egyptian.py -- THE FRESH DIALECT
 A complete interactive model of the Egyptian column-script, read YOUR way
================================================================================

This program throws away every book ever written about Egyptian. No Champollion,
no Gardiner, no "mdw ntr". The only data admitted into evidence is the MARKS
THEMSELVES -- every sign that has ever been recorded as Egyptian is catalogued
here, and every one of them enters the record stamped UNKNOWN. Meanings are
earned only one way: somebody reads the picture and says what it says.

The seed of the whole language is one column (ReferenceDialect/Rosetta.png):
a day's work record read as a picture-story. From it we take the grammar of
the whole system:

  LAW 1   Reading is TOP TO BOTTOM inside a column, columns run LEFT TO RIGHT.
  LAW 2   Each column is its own record -- a chapter, a day, a story. Columns
          do not bleed into each other.
  LAW 3   A picture that seems out of place is not out of place: it is a
          PROVERB. "A fish out of water" means exactly what it looks like.
          The image generalizes an understanding; the concept is assumed
          self-explanatory.
  LAW 4   Signs circled or condensed together inside a column are an
          EMPHATIC proverb-group -- a meme; more weight than a lone sign.
  LAW 5   Penmanship was childish. Scribble is expected. A sloppy drawing
          is still its own sign. Everything not yet read stays UNKNOWN --
          nobody else's decipherment is imported, ever.
  LAW 6   Adjacent marks RELATE to each other, regardless of what they
          are -- bird beside eye is 'going to see', and the mark that
          follows names the destination. Circled memes obey exactly the
          same rule: the marks beside a cluster complete it.

A column of these signs is read like a strip of emojis -- each picture a
generalized concept; place proverbs together and you get a story.

  POLYSEMY  A symbol may carry any number of candidate uses; ten is not
            a linguistic limit.
            Every mark in the registry stays UNKNOWN except the hard-coded
            Rosetta readings -- picture-story guesses, not established
            letter values, numerical values, or verified translations.
            The bird over strokes MAY depict the writer travelling.
            Even those may be corrected as more columns are read.
  DOUBLES   Like English, a reading may carry a deliberate DOUBLE MEANING --
            two senses true at once, not either/or (the crossing under the
            bird: to-and-fro that sold spare bait AND two trips for more).
            'double' attaches the second sense; the engine scores and
            prints both.
  EVOLVED   The dialect evolved: a mark's DEPICTION is its mask, not its
            meaning -- a drawn bird can mean 'travel' (you cannot draw
            'went to and fro', so a figure is drawn DOING it). Crude
            stick-figures mark ACTION. The same-looking image may mean
            something entirely different, so every sign records 'depicts'
            (what it draws, for shape cross-reference) apart from 'defs'
            (what it means), and each reading may carry a mode:
            evolved | action | literal. Like Chinese chengyu -- though it
            is not Chinese -- whole clusters carry paragraphic meaning
            assumed automatically understood.
  THE STRIP The format is MEME-COMIC: a column is a comic strip told in
            assumed meaning. Depictions are often deliberately NOT 100%
            accurate -- what matters is the FUNCTION the symbol performs
            (bird = 'travel', legs = 'transition'), and functional stand-ins
            sit side by side with accurate depictions (ripples = 'river').
            Each reading therefore carries a 'func' tag -- its role in the
            record -- and 'read' prints the strip's spine of roles.
  FLEX      Definitions are NOT 100% concrete: a reading is used
            adjectivally while also verbally, at the same time or not, and
            it flexes with the neighbouring TERMINOLOGY. 'Fish out of
            water' holds only because 'water' stands beside it -- a fish
            beside a basket would read 'fish basket', not the proverb. So
            each candidate reading notes its register
            ('reg': adj | verb | noun | adj+verb...) and an optional 'flex'
            note; 'concrete' flags the rare locked readings.
  IDENTITY  A mark is only its DEPICTION until it is placed: the bird is
            literally a bird; 'travel' is merely what it is being used FOR
            in that column. So nothing is defined ahead of use -- the card
            shows the object (depicts) and beneath it the recorded uses.
            Two different bird-species marks are different signs sharing
            depicts='bird'; their kind is shown through the art, and each
            keeps its own unknown usages until seen in a column.
  THE MATRIX A correlation engine sits between the marks and the story --
            upgraded to pattern recognition: lexical imagery overlap,
            distance decay, condensed-group bonds, the learned pair matrix,
            POSITION priors (openers lean early, closers lean late), and
            SLOT GRAMMAR (verb-site funcs pull actor/place/object marks
            toward them -- the marks beside a verb are its subject and
            object).
            when a sign is ambiguous it scores each candidate reading by
            how well its imagery correlates with the readings chosen around
            it (distance-weighted, doubled inside condensed proverb-groups)
            plus a learned matrix of which readings have been confirmed
            together before. The result is a corrected, intuitive English
            rendering of the record -- with play in the definitions, from
            single concepts to multi-sentence proverbial meanings.
  REFINE    After the greedy pass, every ambiguous reading re-scores
            against the FINISHED story -- a reading that lost early can
            win once the whole record is assembled (fixpoint sweeps).
  LEARN     'keep'/'teach' endorse a column: the matrix reinforces
            sign<->sign pairs, cluster<->member bonds, and the cluster's
            chosen proverb -- memes learn exactly like single marks.
            Nothing is learned without endorsement.

--------------------------------------------------------------------------------
THE REGISTRY (what the language contains -- the program's own count)
--------------------------------------------------------------------------------
Every mark that has ever been recorded as Egyptian writing lives here,
stamped UNKNOWN until a column uses it: main hieroglyphs (1,072), the
scribal format controls (48), the extended block (3,995), Coptic in all
its forms (174 incl. Epact numbers and the letters that hide inside the
Greek block), Meroitic hieroglyphic + cursive (128), plus ink-only marks
for the scripts no codepoint ever got -- hieratic, demotic,
proto-sinaitic -- and the 18 hand-drawn Rosetta marks. 5,515 marks, a
PNG tile for each (glyphs/), every tile labelled sid + object + script.

--------------------------------------------------------------------------------
NAMING (the only label that may sit under a symbol)
--------------------------------------------------------------------------------
A mark gets an English pictured-object label from local documentation
or inspection: [catalogue label] means an object-name proposal, not
a verified use (a falcon is not automatically "travel");
[family] names are the recorded category the sign was carved in;
everything else stays UNLABELED -- 'unnamed recorded mark U+xxxxx' --
because a guess written under a glyph becomes a lie the moment somebody
reads it. Depicts is the mask, defs are the uses: a bowl is a bowl until
the column makes it more.

--------------------------------------------------------------------------------
DIALECTS (the speech these marks carried)
--------------------------------------------------------------------------------
'dialects' lists every documented stage of the language these marks
belong to -- Old, Middle, Late Egyptian, Demotic, then the Coptic stage
where regional speech finally became visible in writing: Bohairic,
Sahidic, Fayyumic, Akhmimic, Lycopolitan, Oxyrhynchite, Bashmuric. The
dialect tag says WHICH community wrote the mark -- never what it means.

--------------------------------------------------------------------------------
FIT-GATE (why a lone mark stays its picture)
--------------------------------------------------------------------------------
A single-reading sign speaks its usage ONLY when the column calls for
it: shared imagery with a chosen neighbour, a learned link, in-meme
membership, or role-family adjacency. Otherwise it renders 'as itself'.
That is the whole philosophy in one rule: the picture is literal until
the story needs it to be more.

--------------------------------------------------------------------------------
RUN
--------------------------------------------------------------------------------
    python Egyptian.py                 # open the interactive scribe WINDOW
    python Egyptian.py --window        # same -- the column-writer UI
    python Egyptian.py --console       # the text scribe console instead
    python Egyptian.py --selftest      # verify catalog, rosetta record, reader, save/load
    python Egyptian.py --rosetta       # print the base column, sign by sign + the story
    python Egyptian.py --stats         # how much of the language is still UNKNOWN
    python Egyptian.py --guesses       # proposed picture-story reading + alternatives
    python Egyptian.py --motifs [name] # two-picture readings of a saved column
    python Egyptian.py --sources       # external visual clues used; no letter values
    python Egyptian.py --history [word]# historical semantic candidates (not proof)
    python Egyptian.py --local [word]  # internal correlation verification (not proof)
    python Egyptian.py --format        # proposed story-grammar coverage of pictured signs
    python Egyptian.py --knowledge     # staged progress toward verified language knowledge
    python Egyptian.py --book          # coherence audit over every saved column
    python Egyptian.py --story <file> [out] # read a glyph-only book file
    python Egyptian.py --translate <english.txt> <glyphs.txt> [report]
                                      # write a proposed picture-book from English
    python Egyptian.py --transcribe <image> <id> [review.json] [--cells cells.txt]
                                      # supervised image-match review; not evidence
    python Egyptian.py --review [id]   # inspect transcription candidates
    python Egyptian.py --pick <id> <cell> <n|sid> # choose a reviewed mark
    python Egyptian.py --approve <id> <column> [column#]
                                      # save reviewed marks as a column
    python Egyptian.py --reject <id>   # discard a transcription review
    python Egyptian.py --catalog       # dump the whole recorded-sign catalogue
    python Egyptian.py --chart         # write egyptian_catalog.html (shaped xref sheet)
    python Egyptian.py --build-tiles   # rebuild glyphs/*.png from the documents
    python Egyptian.py --laws          # print the six reading laws
    python Egyptian.py --export        # write your dialect + rosetta record to a text file

Dependencies: none. Standard library only.

--------------------------------------------------------------------------------
CONSOLE COMMANDS
--------------------------------------------------------------------------------
    laws ................... the six reading laws
    rosetta ................ the base record: every sign, then the story it tells
    read [name] ............ read a column top-to-bottom as a story
    page [names] ........... read columns left-to-right, each its own record
    compose ................ build a column, sign by sign ('[' ']' wraps a proverb-group)
    columns ................ list your saved columns
    show <id> .............. a sign's card: sketch, status, all candidate readings
    define <id> <meaning> .. add a candidate reading (no arbitrary cap)
    prefer <id> <n> ........ promote candidate reading #n to primary
    likely <id> <n> ........ flag candidate reading #n 'highly likely'
    double <id> <n> <sens> . give candidate #n a co-valid second sense
    undouble <id> <n> ...... remove the second sense
    depict <id> <image> .... record what a mark literally depicts (the mask)
    mode <id> <n> <m> ...... tag candidate #n: evolved|action|literal|-
    func <id> <n> <role> ... tag candidate #n's FUNCTION in the strip
    reg <id> <n> <regs> .... tag candidate #n's register: adj|verb|adj+verb
    flex <id> <n> <note> ... note how a reading flexes with terminology
    concrete <id> <n> ...... toggle a locked (unflexing) reading
    undefine <id> [n] ...... drop all readings, or just reading #n
    note <id> <text> ....... attach a working note to a sign
    teach [column] ......... endorse the current reading -> reinforce the matrix
    matrix [id] ............ strongest learned correlations (or for a sign)
    attest <source> <column> <id> <n> .. manually check a proposed use
    audit [id] ............. independent evidence and 0-100 coverage
    guesses ............... picture-story candidate reading (not a proof)
    motifs [column] ....... competing readings for adjacent glyph pairs
    sources ................ external visual clues reviewed; no letter values
    history [word] ......... historical semantic candidates; not proof
    local [word] ........... internal correlation verification; not proof
    format ................. proposed story-grammar coverage of pictured signs
    knowledge .............. staged progress toward verified language knowledge
    book ................... coherence audit over every saved column
    story <file> [out] ..... read a glyph-only book file, optionally export
    translate <english.txt> <glyphs.txt> [report] .. English bridge -> pictures
    transcribe <image> <id>  machine-match image cells for review (not evidence)
    review [id] ............ show transcription candidates
    pick <id> <cell> <n|sid> choose a reviewed shelf mark
    approve <id> <column> [column#] .. approve reviewed cells into a saved column
    reject <id> ............ discard a transcription candidate
    cluster <sids> <mean> .. a circled group's WHOLE-proverb reading (chengyu)
    uncluster <sids> ....... remove a cluster reading
    catalog [all|unknown|defined|<text>] ... browse the recorded sign catalogue
    window ................. open the scribe window (autocorrect writer)
    search <word> .......... find signs by meaning/note
    stats .................. proposed vs cross-checked coverage
    save / load ............ persist your dialect (egyptian_dialect.json)
    export ................. write the record + your dictionary to a text file
    help / quit

Sign IDs:
  'N01'..'N16' -- the sixteen signs of the Rosetta base column (our seed set)
  'A001'..'V011D' style marks -- shelf numbers for the recorded catalogue;
      they are ONLY shelf numbers. They carry no borrowed meaning.
  'X-13460' style marks -- recorded signs unnamed in this Python's Unicode
      tables (the extended block); still real, still UNKNOWN.
  Control marks (VERTICAL-JOINER, MODIFIER-DAMAGED, LOST-SIGN, ...) -- the
      scribal format controls: recorded marks, not pictures, kind='mark'.

The catalogue covers ALL THREE Unicode Egyptian blocks -- every symbol ever
recorded as Egyptian. Each N-sign carries 'xref' links to the recorded shelf
marks judged the same shape (e.g. N01 fish <-> K001), and 'chart' writes an
HTML sheet where every mark is drawn in its canonical shape for future
cross-referencing against photographs.
"""

import difflib
import html
import json
import os
import re
import sys
import shlex
import textwrap
import unicodedata
from collections import defaultdict

# ==============================================================================
# SECTION 0 -- TERMINAL
# ==============================================================================

def _enable_ansi():
    if os.name == "nt":
        try:
            os.system("")
            import ctypes
            k = ctypes.windll.kernel32
            k.SetConsoleMode(k.GetStdHandle(-11), 7)
        except Exception:
            pass

_enable_ansi()
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

NO_COLOR = ("--no-color" in sys.argv) or os.environ.get("NO_COLOR")

def _c(code):
    return "" if NO_COLOR else code

AMBER = _c("\033[38;5;214m")
STONE = _c("\033[38;5;245m")
GOLD  = _c("\033[38;5;220m")
CYAN  = _c("\033[36m")
RED   = _c("\033[31m")
GREEN = _c("\033[32m")
DIM   = _c("\033[2m")
BOLD  = _c("\033[1m")
RESET = _c("\033[0m")

W = 76

def bar(title="", ch="=", color=AMBER):
    if title:
        side = (W - len(title) - 2) // 2
        print(f"{color}{ch*side} {title} {ch*(W-len(title)-2-side)}{RESET}")
    else:
        print(f"{color}{ch*W}{RESET}")

def wrap(text, indent="", width=W):
    out = []
    for line in str(text).splitlines() or [""]:
        out += textwrap.wrap(line, width=width,
                             initial_indent=indent,
                             subsequent_indent=indent) or [indent]
    return "\n".join(out)

# ==============================================================================
# SECTION 1 -- THE CATALOGUE: every recorded Egyptian sign, all UNKNOWN
# ==============================================================================
# We scan the Unicode Egyptian ranges and register everything that exists.
# Names are used ONLY as shelf marks ("A001", "V011D", ...) -- a shelf number
# is not a decipherment. Where a recorded sign has no name in this Python's
# Unicode tables (the Extended-A range), it is still registered by codepoint.

# (block name, first cp, last cp, kind) -- every Unicode Egyptian block,
# which is the complete registry of signs ever recorded as Egyptian.
RECORDED_BLOCKS = [
    ("Egyptian Hieroglyphs",           0x13000, 0x1342F, "sign"),
    ("Hieroglyph Format Controls",     0x13430, 0x1345F, "mark"),
    ("Egyptian Hieroglyphs Extended-A",0x13460, 0x143FA, "sign"),
    ("Meroitic Hieroglyphs",           0x10980, 0x1099F, "sign"),
    ("Meroitic Cursive",               0x109A0, 0x109FF, "sign"),
    ("Coptic",                         0x2C80,  0x2CFF,  "sign"),
    ("Coptic Epact Numbers",           0x102E0, 0x102FF, "sign"),
    ("Coptic (in Greek block)",        0x03E2,  0x03EF,  "sign"),
]

# Historical stages + documented Coptic dialects -- the language varieties
# these scripts carried. Regional dialects became explicit once Egyptian
# moved to the Greek-derived Coptic alphabet (the first to record vowels).
DIALECTS_TEXT = """DIALECTS -- every documented stage of the Egyptian language
======================================================================
  Pre-Coptic stages (written with hieroglyphs / hieratic / demotic ink):
    PROTO-EGYPTIAN  the FIRST recordings: tomb U-j bone/ivory tags at
                    Abydos, ~3200 BC -- predates every sign list
    OLD EGYPTIAN    earliest stage; pyramid texts, ~2686-2181 BC
    MIDDLE EGYPTIAN classical literary language, ~2055-1650 BC
    LATE EGYPTIAN   New Kingdom vernacular, ~1550-600 BC
    DEMOTIC         late script + speech, ~650 BC - 452 AD
    COPTIC          the final stage, ~3rd cent. AD - present (church)
  Coptic dialects (Greek-derived alphabet, records vowels; these use
  the Coptic codepoints already registered in this program):
    BOHAIRIC        northern -- west Nile Delta; survives today as the
                    liturgical language of the Coptic Orthodox Church
    SAHIDIC         classical southern dialect of Upper Egypt; main
                    literary dialect of early Christian texts
    FAYYUMIC        Fayyum oasis; local 'r' sounds shift to 'l'
    AKHMIMIC        archaic south, Akhmim; Gnostic/Manichaean mss
    LYCOPOLITAN     a.k.a. Asyutic, Asyut; same Gnostic/Manichaean mss
    OXYRHYNCHITE    a.k.a. Mesokemic, Middle Egypt; Oxyrhynchus mss
    BASHMURIC       Delta-fringe dialect, poorly attested remnants
  Related languages written with Egyptian-derived scripts (their
  codepoints are also registered in this program):
    MEROITIC        language of the Kingdom of Kush, ~300 BC-400 AD;
                    two scripts -- hieroglyphic (monumental) and
                    cursive (everyday); still only partly read today
    OLD NUBIAN      medieval Nubian, ~8th-15th cent.; written with the
                    Coptic alphabet plus its own extra letters
  Every glyph in this program remains script-first: the dialect tag
  describes WHICH community wrote it, never what a mark means.
======================================================================
SCRIPT PROVENANCE -- where each registered family comes from
======================================================================
  Hieroglyphs U+13000-1342F   Gardiner set + standard additions
  Format controls U+13430-5F  scribal layout marks (joiners/damage)
  Extended-A U+13460-143FF    Unicode 15.0 (2022) sign-list proposal
  Ancient signary (PUA)       Hieroglyphica PIREI 2000 signary --
                              private-use slots Unicode never adopted
  Coptic U+2C80-2CFF (+Greek) Greek uncials + demotic-derived letters
  Epact numbers U+102E0-102FF Coptic-era calendar numerals
  Meroitic U+10980-109FF      Kushite hieroglyphic + cursive
  Hieratic (ink-only)         Moeller's Hieratische Palaeographie
  Demotic (ink-only)          the demotic signary, unencoded
  Proto-Sinaitic (ink-only)   Serabit el-Khadim corpus, ~1850 BC
======================================================================"""

# Standard Gardiner taxonomy -- the block's own historically accurate
# category names, used as object names when no fetched description exists.
CATEGORY_WORD = {
    "A": "man", "B": "woman", "C": "deity", "D": "body",
    "E": "mammal", "F": "mammal-part", "G": "bird", "H": "bird-part",
    "I": "reptile", "K": "fish", "L": "creature", "M": "plant",
    "N": "nature", "O": "building", "P": "boat", "Q": "furniture",
    "R": "ritual", "S": "regalia", "T": "weapon", "U": "tool",
    "V": "rope", "W": "vessel", "X": "bread", "Y": "writing",
    "Z": "stroke", "Aa": "unclassified",
}

_NAMES = None
_PUA = None

def object_name(sid):
    """One-word English object name for a sign -- fetched table first,
    then the Gardiner category word. Returns '' when unknown."""
    global _NAMES, _PUA
    if _NAMES is None:
        try:
            _NAMES = json.load(open(
                os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "object_names.json")))
        except Exception:
            _NAMES = {}
    if sid in _NAMES:
        return _NAMES[sid]
    if sid.startswith("P-"):        # signary PUA marks: documented code
        if _PUA is None:
            try:
                _PUA = json.load(open(
                    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "pua_names.json")))
            except Exception:
                _PUA = {}
        code = _PUA.get(sid[2:].lstrip("0") or "0") or _PUA.get(sid[2:])
        if code:
            return CATEGORY_WORD.get(code[0].upper(), "mark")
        return "signary mark"
    if sid.startswith("X-"):        # Extended-A: name via its mapped
        if _PUA is None:            # signary slot (provisional map --
            try:                    # the standard encoded)
                _PUA = json.load(open(
                    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "pua_names.json")))
            except Exception:
                _PUA = {}
        cp = int(sid[2:], 16)
        if cp < 0x13460:            # Coptic/Meroitic X- marks keep their
            return ""               # recorded Unicode name -- no map
        code = _PUA.get(f"{0xF3440 + (cp - 0x13460):X}")
        if code:
            return CATEGORY_WORD.get(code[0].upper(), "")
        return ""                   # no documented name exists -- stays
                                    # unlabeled (verified-only rule)
    pref = "".join(c for c in sid if c.isalpha())
    if not any(c.isdigit() for c in sid) or len(pref) > 2:
        return ""                   # controls/letters: keep their own
                                    # recorded Unicode name, no guessing
    pref = "".join(c for c in sid if c.isalpha())
    return CATEGORY_WORD.get("Aa" if pref.upper().startswith("AA")
                             else pref[0].upper(), "")

UNKNOWN = "UNKNOWN"
MAX_DEFS = 10          # display target, not a limit on observed uses
CONF_LIKELY = "highly likely"   # explicit user endorsement only
CONF_ASSUMED = "assumed"        # readings inferred only from context
CONF_GUESS = "guess"            # picture-first possibility, not an attestation

class Sign:
    """One mark. Meaning is UNKNOWN until YOU read it -- and then it is
    not one meaning but any number of candidate readings: in language the
    same symbol legitimately carries several meanings, and which one is
    right is decided by the column it stands in."""
    __slots__ = ("sid", "char", "kind", "sketch", "defs", "note",
                 "cp", "block", "xref", "depicts")

    def __init__(self, sid, char=None, kind="sign", sketch=None,
                 meaning=UNKNOWN, note="", source="",
                 cp=None, block="", xref=(), depicts=None):
        self.sid = sid            # shelf mark: 'A001', 'X-13460', 'N03'
        self.char = char          # unicode char, or None -> sketch only
        self.kind = kind          # 'sign' | 'mark' | 'rosetta'
        self.sketch = sketch      # ASCII picture (list of str), or None
        # candidate readings: [{"text": ..., "src": ...}, ...]  primary first
        self.defs = ([] if meaning in (UNKNOWN, None, "")
                     else [{"text": meaning, "src": source}])
        self.note = note
        self.cp = cp              # codepoint int, or None for drawn signs
        self.block = block        # which recorded block it sits in
        self.xref = list(xref)    # sids of other signs claimed same shape
        self.depicts = depicts    # the LITERAL image drawn (bird, coil...)
                                  # -- the mask, not the meaning

    @property
    def defined(self):
        return len(self.defs) > 0

    @property
    def meaning(self):
        """Primary candidate reading (defs[0]) or UNKNOWN."""
        return self.defs[0]["text"] if self.defs else UNKNOWN

    def display(self):
        """The mark itself: real char if we have one, else our sketch."""
        return self.char if self.char else "<drawn>"


# ==============================================================================
# SECTION 1b -- THE CORRELATION MATRIX
# ==============================================================================
# When a sign carries several readings, the reader must choose the one that
# makes the column tell the most obvious story. Two forces decide:
#   1. LEXICAL CORRELATION -- candidate readings that share imagery-words
#      with their neighbours' readings are more likely to belong together
#      (a "fish" near a "river" beats a "fortress" near a "river").
#   2. LEARNED CORRELATION -- every column you KEEP (endorse as correctly
#      read) reinforces the pair of chosen readings in a matrix, so the
#      engine gets better the more you read. Persisted with the dialect.

STOPWORDS = {
    "a", "an", "the", "of", "to", "and", "or", "in", "on", "at", "is", "it",
    "its", "for", "with", "from", "by", "that", "this", "be", "as", "was",
    "are", "were", "so", "than", "then", "into", "out", "his", "her", "he",
    "she", "they", "them", "their", "you", "your", "we", "our", "i",
}

def tokens(text):
    """Content words of a reading -- its imagery fingerprint."""
    return {w.strip(".,;:!?()[]\"'--").lower()
            for w in str(text).split()} - STOPWORDS - {""}


class Correlator:
    """The correlation matrix: W[a][b] = how often reading a of one sign
    was chosen alongside reading b of another in a column you endorsed."""
    def __init__(self):
        self.w = {}

    def get(self, a, b):
        return self.w.get(a, {}).get(b, 0)

    def reinforce(self, keys):
        keys = list(dict.fromkeys(keys))
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                self.w.setdefault(a, {}).setdefault(b, 0)
                self.w.setdefault(b, {}).setdefault(a, 0)
                self.w[a][b] += 1
                self.w[b][a] += 1

    def top(self, sid=None, n=15):
        seen, pairs = set(), []
        for a, m in self.w.items():
            for b, c in m.items():
                key = tuple(sorted((a, b)))
                if key in seen:
                    continue
                seen.add(key)
                if sid and not (a.startswith(sid + "#")
                                or b.startswith(sid + "#")):
                    continue
                pairs.append((c, a, b))
        pairs.sort(reverse=True)
        return pairs[:n]


def build_catalogue():
    """Every recorded Egyptian mark. No meanings shipped. None. Ever.

    Three blocks make up the whole registry: the main picture signs, the
    scribal format controls (joiners / damage marks / enclosures -- recorded
    marks, not pictures, catalogued as kind='mark'), and the extended block.
    Signs unnamed in this Python's Unicode table are still real recorded
    marks -- they get codepoint shelf marks 'X-XXXXX'."""
    cat = {}
    for block, lo, hi, kind in RECORDED_BLOCKS:
        for cp in range(lo, hi + 1):
            name = unicodedata.name(chr(cp), "")
            if name.startswith("EGYPTIAN HIEROGLYPH"):
                sid = name.replace("EGYPTIAN HIEROGLYPH ", "").replace(" ", "-")
            else:
                sid = f"X-{cp:05X}"   # recorded but unnamed in this table
            cat[sid] = Sign(sid, chr(cp), kind=kind, cp=cp, block=block,
                            depicts=object_name(sid) or
                                    (name or f"unnamed recorded mark "
                                             f"U+{cp:05X}"))
    # ink-only scripts: hieratic / demotic / proto-sinaitic were never
    # encoded in Unicode -- no codepoints exist. They are catalogued as
    # ink marks (kind='ink'): searchable, drawable as cells, honest that
    # no recorded digital shape exists.
    # counts follow the published palaeographies: Moeller's Hieratische
    # Palaeographie (~740 entries), the demotic signary (~500), the
    # proto-Sinaitic corpus (~40 attested signs)
    for i in range(1, 741):
        cat[f"H-{i:03d}"] = Sign(f"H-{i:03d}", kind="ink",
                                 block="Hieratic (unencoded)",
                                 depicts="hieratic sign")
    for i in range(1, 501):
        cat[f"D-{i:03d}"] = Sign(f"D-{i:03d}", kind="ink",
                                 block="Demotic (unencoded)",
                                 depicts="demotic sign")
    for i in range(1, 41):
        cat[f"PS-{i:02d}"] = Sign(f"PS-{i:02d}", kind="ink",
                                  block="Proto-Sinaitic (unencoded)",
                                  depicts="proto-sinaitic sign")
    # the FIRST Egyptian recordings: tomb U-j bone/ivory tags at Abydos
    # (~3200 BC, predating every sign list) + early-dynastic forms
    for i in range(1, 201):
        cat[f"UJ-{i:03d}"] = Sign(f"UJ-{i:03d}", kind="ink",
                                  block="Proto-Egyptian U-j (unencoded)",
                                  depicts="proto-egyptian tag mark")
    for i in range(1, 61):
        cat[f"ED-{i:03d}"] = Sign(f"ED-{i:03d}", kind="ink",
                                  block="Early Dynastic (unencoded)",
                                  depicts="early dynastic sign")
    # the ancient signary beyond the standard: the Hieroglyphica/Aegyptus
    # repertoire kept recorded signs in private-use slots that Unicode
    # never standardized -- quadrat groups and extra signs. Every slot
    # that carries a glyph is catalogued (pua_slots.txt = the measured
    # font map), rendered through the Aegyptus fallback.
    try:
        _pf = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "pua_slots.txt")
        for ln in open(_pf):
            cp = int(ln.strip(), 16)
            cat[f"P-{cp:05X}"] = Sign(f"P-{cp:05X}", chr(cp),
                                      cp=cp, block="Ancient signary (PUA)",
                                      depicts=object_name(f"P-{cp:05X}")
                                              or "signary mark")
    except Exception:
        pass
    return cat

# ==============================================================================
# SECTION 2 -- THE ROSETTA BASE RECORD  (the seed dictionary)
# ==============================================================================
# One column. A day's work. Read top to bottom as a picture-story.
# The marks in the photograph are rough -- 'child like depictions' -- so each
# sign here is anchored by OUR sketch; 'char' is only a nearest recorded shape
# guess, never a borrowed meaning.

def S(lines):
    return lines.strip("\n").splitlines()

SK_FISH = S(r"""
        ___
    o  /   \__
    <>< \_____/ >
""")

SK_RIPPLES = S(r"""
    ~ ~ ~ ~ ~
     ~ ~ ~ ~ ~
    ~ ~ ~ ~ ~
""")

SK_EYE = S(r"""
     .-----.
    /  ___  \
    \ ( o ) /
     '--^--'
""")

SK_FIGURE = S(r"""
       O
      /|\
      / \
   ___/ \____
   ~ shoreline ~
""")

SK_SNAIL = S(r"""
     .---.
    /  _  \
   |  (_)  \__
    \     ____)
     '----'
""")

SK_SLIT = S(r"""
   ____________
   ------------
""")

SK_FOUNDATION = S(r"""
   ________________
  |////////////////|
  |________________|
""")

SK_BIRD = S(r"""
       __
     _(  )>
    (___//
       ||
     __||__
""")

SK_TWO = S(r"""
     |    |
     |    |
     |    |
""")

SK_LEGS = S(r"""
      |\
      | \
      |  \
      \   \
       \__\
""")

SK_GRAIN = S(r"""
    \\ || //
     \\||//
      |||
    __|||__
""")

SK_BOX = S(r"""
     +-----+
     |     |
     +-----+
""")

SK_SHADE = S(r"""
       _____
      /     \
     /_______\
       |   |
       |   |
""")

SK_CACTUS = S(r"""
        _
       |_|
     | |
     | |_
     |_  |
       | |
      _|_|_
""")

SK_LYING = S(r"""
     ______________
    __o___________)
   ----------------
""")

# species variants: the SAME object name drawn differently -- the kind is
# shown through the art, and each variant keeps its own unknown uses
SK_BIRD2 = S(r"""
        ,
       (o)_
      // \>
     //  //
       _||_
""")

SK_BIRD3 = S(r"""
      ___
     /o  \__
    <     \>
     \___/
       ||
""")

# (sid, name, nearest-shape char, sketch, meaning or None->UNKNOWN, note, group,
#  xref) -- group: entries sharing a group letter form a CONDENSED PROVERB
# (law 4).  xref: recorded shelf marks judged the SAME SHAPE as our drawn
# sign -- the formal cross-reference between our reading and the catalogue.
ROSETTA_SPEC = [
    # -- section 1 : the setting ------------------------------------------
    ("N01", "fish",            "𓆛", SK_FISH,
     "A FISH OUT OF WATER -- something out of its place; the day's work begins",
     "First mark of the record. Read as a proverb, not a zoology report.",
     None, ["K001"]),
    ("N02", "ripples",         "𓈗", SK_RIPPLES,
     "the river -- the fishing waters; the workplace",
     "Stacked water lines. Where the work happens.", None, ["N035A"]),
    ("N03", "eye",             "𓁹", SK_EYE,
     "the bigger picture -- take in the whole scene",
     "A wide eye over the water: surveying the situation.", None, ["D006"]),
    ("N04", "figure-at-shore", None, SK_FIGURE,
     "a man standing at the shore -- oneself at the edge of the work",
     "The worker himself, planted at the waterline.", None, ["A021"]),
    # -- section 2 : the labor --------------------------------------------
    ("N05", "snail-coil",      None, SK_SNAIL, None,
     "A snail-like creature drawn partly standing with its eyes extended -- "
     "appears several times, its terminology varying across the page; "
     "assumed the bait itself once the later depictions are read (see "
     "N12: bait lifted to a scale).", None, ["F051C"]),
    ("N06", "slit",            None, SK_SLIT, None,
     "Horizontal slit; separation or opening are picture-first guesses.",
     None, ["Z016"]),
    ("N07", "foundation",      None, SK_FOUNDATION,
     "a foundation set under the work -- a break in the job",
     "A hatched platform laid beneath the labor: the pause.", None, ["N001"]),
    ("N08", "bird",            "𓅬", SK_BIRD,
     "a bird -- the SYMBOL OF TRAVEL: the writer is the bird, a trip taken",
     "Metaphorical, not literal: no bird flew anywhere -- the man IS the "
     "bird. Read with the crossing beneath it (N09), the pair says HE took "
     "two trips, a guess. The supplied crop depicts a plump waterfowl "
     "facing right -- the standing-goose kind, not an owl.", "B", ["G038"]),
    ("N09", "two-strokes",     None, SK_TWO,
     "to and fro -- TWO trips: one there and back again still carrying "
     "his bait; a bad day's fishing, no catch, so the bait itself was "
     "carried back to sell",
     "A crossing drawn beneath the bird -- a DOUBLE-MEANING proverb, like "
     "an English pun: it also reads as two trips taken for more bait. Both "
     "senses stand at once as possibilities, not facts.", "B", ["Z016B"]),
    ("N10", "lift",            "𓂻", SK_LEGS,
     "a full body lifts whatever mark stands right before it -- the "
     "lifted thing is ANY symbol: the sign just before this one is what "
     "he lifts",
     "An incomplete stick figure that reads as a full body performing a "
     "lift -- the mark directly before it is the load.", None, ["D054"]),
    # -- section 3 : the yield and the rest -------------------------------
    ("N11", "grain",           None, SK_GRAIN,
     "the yield he carried back -- his own bait, sold instead of fish: "
     "a bad day at work",
     "A bound sheaf: what he carries home is the bait, not the catch.",
     None, ["M034"]),
    ("N12", "small-box",       None, SK_BOX, None,
     "The small box -- assumed a scale: bait is lifted onto it, and in "
     "this dialect goods lifted to a scale reads SOLD, not bought.",
     None, ["N022"]),
    ("N13", "slip",            None, SK_SLIT, None,
     "Horizontal slip; a divider or small carried object are guesses.",
     None, ["Z016A"]),
    ("N14", "shade",           None, SK_SHADE,
     "took shade -- shelter from the sun after work",
     "An awning on poles: getting out of the sun.", None, ["V019"]),
    ("N15", "cactus-drink",    None, SK_CACTUS,
     "drank from a cactus -- refreshment",
     "A water-plant used as a cup.", None, ["M026"]),
    ("N16", "lying-down",      None, SK_LYING,
     "laid down for rest -- the day is done",
     "Flat on the ground. End of record.", None, ["A056"]),
]

ROSETTA_SECTIONS = {
    1: (1, 4,  "THE SETTING"),
    2: (5, 10, "THE LABOR"),
    3: (11, 16, "THE YIELD AND THE REST"),
}

ROSETTA_STORY = (
    "A fish out of water -- the record opens on something out of place, and "
    "the place is the river: a man stands at the shore -- too hot, or too "
    "crowded, it is a guess and unknown which -- taking in the whole scene. Then the labor: a coiled thing -- the "
    "gathered harvest itself, not bait (were it fishing-goods they would "
    "have drawn a fish with a basket) -- beside a slit still unread, a "
    "foundation laid under the work -- a break in the job -- and a bird "
    "with a crossing drawn beneath it, an emphatic proverb used "
    "metaphorically: no bird went anywhere. The writer is saying HE took "
    "the trips -- he IS the bird: TWO trips, one there and back again "
    "still carrying his bait -- a bad day's fishing, no catch, so the "
    "bait itself went to market. (Or, the double sense: the fishing was "
    "too good to need it.) The stick man picks up the yield he is "
    "selling. He returns to town to sell: a scale -- the bait lifted "
    "onto it "
    "to be weighed, which in this dialect reads SOLD, not bought -- and "
    "the coin paid under it pocketed into a pouch. The record closes the "
    "way a day closes: shade taken, a drink drawn from a cactus, and a "
    "man laid down to rest. A finished day's work."
)


# Assumed readings: marks we can only guess from LATER depictions -- the
# snail-thing reads as the bait once the scale is understood; goods lifted
# to a scale reads SOLD (you weigh what you give), never bought. A weaker
# confidence tier for inherited contextual proposals.
ASSUMED_SEED = {
    "N05": ("bait -- a coiled creature, the fishing bait itself "
            "(assumed from the scale that follows)"),
    "N12": ("a scale -- bait lifted onto it to be weighed: in this dialect "
            "goods lifted to a scale reads SOLD, not bought"),
}

# Further assumed candidates: alternate readings of the same marks, weaker
# still -- the snail may be the harvest itself (not bait: if it were fishing
# goods they would have drawn fish+basket), the slit a pocket for the coin,
# the legs the man picking up the yield he is selling.
ALT_SEED = {
    "N05": ("or else the gathered harvest itself -- a coiled yield, not "
            "bait: were it fishing-goods they would have drawn a fish with "
            "a basket"),
    "N10": "the stick man picks up the yield he is selling",
    "N13": ("a pocket or pouch -- the coin paid under the scale is "
            "pocketed: a finished day's work"),
}

# Double senses seeded into base defs: one mark, two true readings at once
# (like an English double meaning -- not either/or, but both at once).
DBL_SEED = {
    "N09": ("or equally: the fishing was too good to need it -- the bait "
            "ran short / two trips for more"),
    "N04": ("or the shore is TOO CROWDED -- it is either too hot or too "
            "crowded: a guess, unknown which"),
}


# Seed clusters: circled sign-groups that read as ONE whole proverb -- like
# Chinese chengyu, a cluster means a paragraph without being broken down.
# A cluster record: {"depicts": literal image, "defs": [up to MAX_DEFS
# candidate whole-proverb readings, each {text, src, conf?, mode?, also?}]}
# -- the evolved dialect means the same ring of marks can read several
# entirely different ways; context picks.  Key = "+".join(sids in column
# order); unordered lookup also works.
CLUSTER_SEED = {
    "N08+N09": {
        "depicts": "a bird perched over a two-stroke crossing",
        "defs": [{
            "text": ("THE TRAVELLER -- he went to and fro: the writer IS "
                     "the bird; trips made, whether to fetch more bait or "
                     "to sell the spare, the catch too good to need it"),
            "src": "Nathan -- Rosetta base column",
            "conf": CONF_GUESS,
            "mode": "evolved",
        }],
    },
    # bird beside an eye, NO distance-marks between them: short distance --
    # 'going to see'. The mark that FOLLOWS is the destination: person,
    # place, or thing. A standing terminology pattern of the dialect.
    "N03+N08": {
        "depicts": "a bird beside an eye -- no crossing, no distance",
        "defs": [{
            "text": ("GOING TO SEE -- a short trip to look at whatever "
                     "follows: person, place or thing. No distance-marks "
                     "means short distance"),
            "src": "Nathan -- dialect terminology",
            "conf": CONF_ASSUMED,
            "mode": "evolved",
            "func": "act-visit",
        }],
    },
}


def _norm_cluster(rec):
    """Normalize a cluster record to {'depicts':?, 'defs':[...]} -- accepts
    the old flat {'meaning': ...} shape from earlier dialect files."""
    if "defs" in rec:
        return rec
    rec["defs"] = ([{"text": rec.get("meaning", ""), "src": rec.get("src", ""),
                     "conf": rec.get("conf", CONF_GUESS)}]
                   if rec.get("meaning") else [])
    rec.pop("meaning", None)
    return rec

# Reading modes seeded on base defs: 'evolved' = the mark depicts one thing
# but means another (bird -> travel); 'action' = a crude stick-figure used
# because you cannot draw the act itself (you draw a figure DOING it).
MODE_SEED = {
    "N08": "evolved",
    "N04": "action",
    "N10": "action",
    "N16": "action",
}

# The FUNCTION each seed sign performs in the strip -- what the mark DOES,
# not what it depicts. Depictions in this dialect are often not 100%
# accurate on purpose: a functional stand-in (bird = travel) sits beside
# accurate marks (ripples = river), and the reader is expected to know.
FUNC_SEED = {
    "N01": "proverb-opener",   # something out of place -- sets the tone
    "N02": "place",            # the river -- where the strip happens
    "N03": "observe",          # taking in the whole scene
    "N04": "actor",            # the man himself
    "N07": "pause",            # the break in the job
    "N08": "act-travel",       # to and fro -- a function, not a bird
    "N09": "count",            # the tally of trips
    "N10": "transition",       # the story moves on
    "N11": "yield",            # the harvest -- result of the work
    "N14": "recover",          # shade after labor
    "N15": "sustain",          # the drink
    "N16": "rest",             # closure -- the strip ends
    "N05": "object",           # the bait itself (assumed)
    "N12": "exchange",         # the scale -- goods weighed out = SOLD
}

# Reading REGISTERS: a def is used adjectivally while also verbally, at the
# same time or not -- the register(s) it can serve.
REG_SEED = {
    "N01": "adj+verb",   # 'fish out of water' describes AND acts
    "N02": "noun",
    "N04": "noun",
    "N08": "verb",
    "N09": "verb",
    "N11": "noun",
    "N16": "verb",
}

# Terminology FLEX: readings are not 100% concrete -- they flex with the
# neighbouring terminology. The noted example: 'fish out of water' holds
# only because 'water' is beside it; a fish beside a basket reads
# 'fish basket', not the proverb.
FLEX_SEED = {
    "N01": ("flexes with the paired mark: fish beside a basket would read "
            "'fish basket', not 'fish out of water'"),
}

# Species variants: marks NOT in the rosetta column, seeded to show that
# the same object name can be drawn as different kinds -- N17/N18 are also
# 'bird' but their uses are their own and still UNKNOWN until placed.
VARIANT_SEED = [
    ("N17", "bird", SK_BIRD2, ["G026"],
     "A different bird-species mark -- same object name as N08, its own "
     "unknown uses. The kind is shown through the art."),
    ("N18", "bird", SK_BIRD3, ["G014"],
     "Another kind of bird mark -- depicts bird, unread."),
]

def seed_rosetta(cat):
    """Install the sixteen base signs into the catalogue as N-signs,
    each carrying codepoint + xref links to matching recorded shapes.
    Rosetta interpretations are explicitly labeled guesses; catalogue
    labels describe pictured objects only."""
    for sid, name, ch, sketch, meaning, note, grp, xref in ROSETTA_SPEC:
        s = Sign(sid, ch, kind="rosetta", sketch=sketch,
                 meaning=meaning or UNKNOWN,
                 note=note,
                 source="Nathan -- Rosetta base column" if meaning else "",
                 cp=ord(ch) if ch else None,
                 block="Rosetta base column",
                 xref=xref,
                 depicts=name)
        for dd in s.defs:
            dd["conf"] = CONF_GUESS
        if sid in ASSUMED_SEED and not s.defs:
            s.defs.append({"text": ASSUMED_SEED[sid],
                           "src": "Nathan -- Rosetta base column",
                           "conf": CONF_ASSUMED})
        if sid in ALT_SEED:
            s.defs.insert(0, {"text": ALT_SEED[sid],
                              "src": "Nathan -- Rosetta base column",
                              "conf": CONF_ASSUMED})   # the canonical read
        if sid in DBL_SEED and s.defs:
            s.defs[0]["also"] = DBL_SEED[sid]
        if sid in MODE_SEED and s.defs:
            s.defs[0]["mode"] = MODE_SEED[sid]
        if sid in FUNC_SEED and s.defs:
            s.defs[0]["func"] = FUNC_SEED[sid]
        if sid in REG_SEED and s.defs:
            s.defs[0]["reg"] = REG_SEED[sid]
        if sid in FLEX_SEED and s.defs:
            s.defs[0]["flex"] = FLEX_SEED[sid]
        cat[sid] = s
        # wire the back-link: the recorded sign points at our drawn sign
        for xsid in xref:
            if xsid in cat and sid not in cat[xsid].xref:
                cat[xsid].xref.append(sid)
        # the drawn mark borrows the recorded sign's authentic shape
        if not s.char and s.xref:
            for xsid in s.xref:
                if xsid in cat and cat[xsid].char:
                    s.char = cat[xsid].char
                    break
    # species variants: same object name, different art, no uses yet
    for vsid, vname, vsketch, vxref, vnote in VARIANT_SEED:
        cat[vsid] = Sign(vsid, None, kind="rosetta", sketch=vsketch,
                         note=vnote, block="Rosetta base column",
                         depicts=vname, xref=vxref)
        if vxref and vxref[0] in cat:
            cat[vsid].char = cat[vxref[0]].char
    return cat

# Picture-first candidates: (shelf mark, proposed use, literal/metaphorical
# mode, role). The object labels are shape descriptions, not word meanings.
# These are deliberately specific enough to be tested against future columns.
PICTURE_GUESSES = [
    ("N06", "a gap or interruption between pictured actions", "metaphorical", "pause"),
    ("N06", "a narrow opening or passage", "literal", "place"),
    ("N13", "a line separating one event from the next", "metaphorical", "pause"),
    ("N13", "a thin slip or small object carried after the exchange", "literal", "object"),
    ("N05", "a slow creature: the task or journey takes time", "metaphorical", "transition"),
    ("N08", "a bird present at the water, rather than a human journey", "literal", "actor"),
    ("N09", "two parallel strokes: a pictured pair, with no fixed numerical value", "literal", "object"),
    ("N12", "a small container holding goods, rather than a scale", "literal", "object"),
    ("N17", "a compact bird: a creature pictured at this place", "literal", "actor"),
    ("N18", "a slender bird variant: a creature pictured at this place", "literal", "actor"),
    ("A001", "a seated person: someone at rest or waiting", "literal", "actor"),
    ("A021", "a standing person: someone present at the scene", "literal", "actor"),
    ("A056", "a lying person: resting or sleeping", "literal", "rest"),
    ("D004", "an eye: someone looks at what follows", "metaphorical", "observe"),
    ("D004", "an eye drawn on a person or object", "literal", "object"),
    ("D009", "a weeping eye: grief or trouble", "metaphorical", "observe"),
    ("D046", "a hand: taking hold of or giving the next object", "metaphorical", "action"),
    ("D046", "a hand pictured beside another mark", "literal", "object"),
    ("D054", "legs: moving or changing location", "metaphorical", "transition"),
    ("G038", "a goose or water bird at this scene", "literal", "actor"),
    ("G038", "a bird journey: leaving or returning", "metaphorical", "act-travel"),
    ("K001", "a fish: a catch in water", "literal", "yield"),
    ("K001", "a fish separated from water: something out of place", "metaphorical", "proverb-opener"),
    ("N020", "a riverbank: the edge of the water", "literal", "place"),
    ("N020", "a boundary or point of crossing", "metaphorical", "place"),
    ("N027", "the sun at the horizon: time of day", "literal", "place"),
    ("N027", "a horizon: arrival, departure, or a new stage", "metaphorical", "transition"),
    ("N035", "water: river or flowing water at the scene", "literal", "place"),
    ("N035", "water: drinking, washing, or renewal", "metaphorical", "sustain"),
    ("O001", "a house: a dwelling or destination", "literal", "place"),
    ("O001", "a house: returning home or seeking shelter", "metaphorical", "recover"),
    ("P001", "a boat: crossing water", "literal", "act-travel"),
    ("P001", "a boat: a journey or transporting goods", "metaphorical", "act-travel"),
    ("T024", "a fishing net: gathering a catch", "literal", "yield"),
    ("T024", "a net: gathering or holding something together", "metaphorical", "action"),
    ("V030", "a basket: carrying or storing the adjacent thing", "literal", "object"),
    ("V030", "a basket: collected goods or harvest", "metaphorical", "yield"),
    ("W015", "a water jar: water carried for drinking", "literal", "sustain"),
    ("W015", "a filled jar: provision for the journey", "metaphorical", "sustain"),
    ("M001", "a tree: vegetation at this place", "literal", "place"),
    ("M001", "a tree: shade or shelter", "metaphorical", "recover"),
    ("M034", "a sheaf of grain: harvested food", "literal", "yield"),
    ("M034", "grain: the reward or result of work", "metaphorical", "yield"),
    ("A002", "a person speaking to someone nearby", "literal", "actor"),
    ("A002", "a person speaking: a message or instruction follows", "metaphorical", "action"),
    ("A017", "a child: a young person in the scene", "literal", "actor"),
    ("A017", "a child: something new or just beginning", "metaphorical", "proverb-opener"),
    ("A019", "an older person in the scene", "literal", "actor"),
    ("A019", "an older person: time has passed or experience is needed", "metaphorical", "observe"),
    ("D021", "a mouth: eating or speaking", "literal", "action"),
    ("D021", "a mouth: a statement or a need for food", "metaphorical", "action"),
    ("D055", "walking legs: someone moving on foot", "literal", "transition"),
    ("D055", "walking legs: the story continues elsewhere", "metaphorical", "transition"),
    ("G017", "an owl: a bird in this scene", "literal", "actor"),
    ("G017", "an owl: watchfulness or activity at night", "metaphorical", "observe"),
    ("G001", "a falcon: a bird overhead", "literal", "actor"),
    ("G001", "a falcon: a high view or flight across distance", "metaphorical", "act-travel"),
    ("K008", "a catfish: fish in the water or a catch", "literal", "yield"),
    ("K008", "a catfish: food or goods caught at the river", "metaphorical", "yield"),
    ("M002", "a plant growing at this place", "literal", "place"),
    ("M002", "a plant: growth, renewal, or a season passing", "metaphorical", "transition"),
    ("M033", "grain: a crop in the field", "literal", "object"),
    ("M033", "grain: food grown or expected from work", "metaphorical", "yield"),
    ("N005", "the sun: daytime or heat in the scene", "literal", "place"),
    ("N005", "the sun: a day's passing or the start of work", "metaphorical", "proverb-opener"),
    ("N006", "the sky: what is above the scene", "literal", "place"),
    ("N006", "the sky: the wider setting or outside world", "metaphorical", "place"),
    ("N007", "a sky with rain: wet weather", "literal", "place"),
    ("N007", "rain: water arriving or a change in conditions", "metaphorical", "transition"),
    ("N015", "a star: the night sky", "literal", "place"),
    ("N015", "a star: night travel or a distant point to follow", "metaphorical", "act-travel"),
    ("N036", "water: a flow or nearby water", "literal", "place"),
    ("N036", "water: washing or renewal", "metaphorical", "sustain"),
    ("O051", "a pile of grain: gathered harvest", "literal", "yield"),
    ("O051", "a pile of grain: abundance or stored provisions", "metaphorical", "yield"),
    ("P002", "a boat under sail: travel on water", "literal", "act-travel"),
    ("P002", "a sailing boat: cargo moving to another place", "metaphorical", "act-travel"),
    ("V031", "a basket: carrying the pictured goods", "literal", "object"),
    ("V031", "a basket: stored goods or a collected result", "metaphorical", "yield"),
    ("W001", "a vessel: holding food, water, or other contents", "literal", "object"),
    ("W001", "a vessel: provisions put aside for later", "metaphorical", "sustain"),
    ("X002", "bread: food eaten or carried", "literal", "sustain"),
    ("X002", "bread: a meal or the reward for work", "metaphorical", "yield"),
    ("Z012", "several small strokes: an amount or repetition", "literal", "count"),
    ("Z012", "several small strokes: many times or repeated effort", "metaphorical", "count"),
    ("Z001", "a single stroke: a mark whose role depends on nearby pictures", "literal", "object"),
    ("Z001", "a single stroke: a pause if it divides two scenes", "metaphorical", "pause"),
]

AUTO_GUESS_SCOPE = "catalogue-coverage"
MULTIUSE_GUESS_SCOPE = "multi-use-format"
HISTORICAL_GUESS_SCOPE = "historical-candidate"
AUTO_GUESS_SOURCE = "catalogue depiction/category correlation (shape-only guess)"
MULTIUSE_GUESS_SOURCE = "multi-use variable correlation (language-format guess)"
HISTORICAL_GUESS_SOURCE = ("PHRP Gardiner sign-list ideogram/determinative "
                           "semantic uses; phonetic values ignored")
AUTO_SCOPES = {AUTO_GUESS_SCOPE, MULTIUSE_GUESS_SCOPE,
               HISTORICAL_GUESS_SCOPE}

# Historical semantic candidates imported ONLY as alternative hypotheses.
# These are conventional ideogram/determinative glosses from PHRP. They are
# not loaded as phonetic values, not claims about the photographed dialect,
# and not independent attestations.
HISTORICAL_GUESSES = [
    ("A001", "historical: man/person; also first person 'I/me'", "actor"),
    ("A002", "historical: eat, drink, speak, think, or feel", "action"),
    ("A003", "historical: sit or be seated", "rest"),
    ("A004", "historical: supplicate or hide", "action"),
    ("A005", "historical: hide", "action"),
    ("A006", "historical: pure or clean", "recover"),
    ("A007", "historical: weary or weak", "recover"),
    ("A008", "historical: jubilation", "observe"),
    ("A009", "historical: load, carry, or work", "action"),
    ("A010", "historical: sail", "act-travel"),
    ("A011", "historical: friend", "actor"),
    ("A012", "historical: army or soldiers", "actor"),
    ("A013", "historical: enemy", "actor"),
    ("A014", "historical: die or enemy", "action"),
    ("A015", "historical: fall or overthrow", "action"),
    ("A016", "historical: bow down", "action"),
    ("A017", "historical: young", "actor"),
    ("A019", "historical: old or great", "observe"),
    ("A020", "historical: eldest", "actor"),
    ("A021", "historical: official or noble", "actor"),
    ("A022", "historical: statue", "object"),
    ("A023", "historical: sovereign", "actor"),
    ("A024", "historical: strike, force, or effort", "action"),
    ("A025", "historical: strike", "action"),
    ("A026", "historical: call or vocative appeal", "record"),
    ("A028", "historical: high, joy, or mourn", "observe"),
    ("A029", "historical: upside-down", "transition"),
    ("A030", "historical: praise, supplicate, or awe", "observe"),
    ("A031", "historical: turn away", "transition"),
    ("A032", "historical: dance or joy", "action"),
    ("A033", "historical: herdsman or wander", "actor"),
    ("A034", "historical: pound or build", "action"),
    ("A035", "historical: build", "action"),
    ("A036", "historical: brewer", "actor"),
    ("A038", "historical: Cusae town", "place"),
    ("A040", "historical: god; or first person of a god", "actor"),
    ("A041", "historical: king; or first person of a king", "actor"),
    ("A043", "historical: king of Upper Egypt or Osiris", "actor"),
    ("A045", "historical: king of Lower Egypt", "actor"),
    ("A047", "historical: herdsman, guard, or protect", "actor"),
    ("A048", "historical: relating to or belonging to", "object"),
    ("A049", "historical: foreigner", "actor"),
    ("A050", "historical: revered person or first person", "actor"),
    ("A053", "historical: mummy, form, or shape", "object"),
    ("A054", "historical: dead", "rest"),
    ("A055", "historical: lie down or death", "rest"),
    ("D054", "historical: come; movement or lack of movement", "transition"),
    ("D055", "historical: backwards or return", "transition"),
    ("G001", "historical: falcon or Horus", "actor"),
    ("G038", "historical: goose, Geb, or birds generally", "actor"),
    ("K001", "historical: Nile tilapia/perch", "yield"),
    ("M001", "historical: tree", "place"),
    ("M002", "historical: plant, flower, or be light", "place"),
    ("M026", "historical: Upper Egypt", "place"),
    ("M033", "historical: barley or corn", "yield"),
    ("M034", "historical: emmer grain", "yield"),
    ("N005", "historical: sun, day, or actions of the sun", "place"),
    ("N007", "historical: day-time", "place"),
    ("N011", "historical: moon", "place"),
    ("N013", "historical: half-moon festival", "record"),
    ("N014", "historical: star or constellation", "place"),
    ("N015", "historical: Duat or netherworld", "place"),
    ("N016", "historical: earth or land", "place"),
    ("N018", "historical: island, desert, foreign country, horizon, or loin-cloth", "place"),
    ("N019", "historical: Ra-Horakhty", "record"),
    ("N020", "historical: sand bank or shore", "place"),
    ("N021", "historical: land or bank", "place"),
    ("N022", "historical: land or field", "place"),
    ("N023", "historical: irrigated land or time", "place"),
    ("N024", "historical: district, estate, province, or garden", "place"),
    ("N025", "historical: hill-country, foreign land, desert, necropolis, or east", "place"),
    ("N026", "historical: mountain", "place"),
    ("N027", "historical: horizon", "place"),
    ("N028", "historical: hill of sunrise or appear in glory", "transition"),
    ("N030", "historical: mound", "place"),
    ("N031", "historical: road, travel, position, or distance", "transition"),
    ("N032", "historical: clay or filth", "object"),
    ("N033", "historical: sand, metal, mineral, medicaments, or incense", "object"),
    ("N034", "historical: copper or objects of copper/bronze", "object"),
    ("N035", "historical: water, liquid, or actions connected with water", "place"),
    ("N036", "historical: canal, river, lake, or sea", "place"),
    ("O001", "historical: house, building, seat, or horizon", "place"),
    ("O031", "historical: door or open", "place"),
    ("O032", "historical: door or gateway", "place"),
    ("O036", "historical: wall", "place"),
    ("O049", "historical: village or town", "place"),
    ("O051", "historical: granary", "place"),
    ("P001", "historical: boat, ship, sail, or travel by water", "act-travel"),
    ("P002", "historical: sail upstream", "act-travel"),
    ("P003", "historical: sacred bark, divine boat, or divine journey", "act-travel"),
    ("T007", "historical: axe, hew, or carpenter", "action"),
    ("T009", "historical: bow", "object"),
    ("T010", "historical: bow, foreign people, troop, or bowman", "actor"),
    ("T011", "historical: arrow", "object"),
    ("T012", "historical: string, bow-string, or restrain", "action"),
    ("T013", "historical: wakeful or vigilant", "observe"),
    ("T014", "historical: throw-stick, throw, club, or foreigner", "action"),
    ("T017", "historical: chariot", "act-travel"),
    ("T018", "historical: follow or accompany", "transition"),
    ("T019", "historical: bone or harpoon", "object"),
    ("T021", "historical: one", "count"),
    ("T022", "historical: two", "count"),
    ("T024", "historical: net or field", "object"),
    ("T026", "historical: trap or snare", "object"),
    ("T028", "historical: under", "place"),
    ("T030", "historical: knife, sharp, or cut", "action"),
    ("T033", "historical: butcher", "actor"),
    ("T034", "historical: knife", "object"),
    ("V001", "historical: rope, drag, tie, or surround", "action"),
    ("V005", "historical: plan, plot out, or found", "record"),
    ("V006", "historical: cord, tie up, or clothes", "object"),
    ("V015", "historical: seize", "action"),
    ("V016", "historical: hobble", "object"),
    ("V017", "historical: protection", "recover"),
    ("V019", "historical: stable, stall, mat, land, or sack-measure", "place"),
    ("V020", "historical: stables or ten", "count"),
    ("V026", "historical: spool or reel", "object"),
    ("V029", "historical: wipe or ward off", "action"),
    ("V030", "historical: basket", "object"),
    ("V032", "historical: harpooner, bundles, or tribute", "actor"),
    ("V033", "historical: linen or cloth", "object"),
    ("V036", "historical: receptacle given to a temple", "object"),
    ("V037", "historical: bandage or bind", "action"),
    ("V038", "historical: bandage or mummy-cloth", "object"),
    ("W014", "historical: water-pot", "sustain"),
    ("W015", "historical: be cool", "recover"),
    ("W016", "historical: libation", "sustain"),
    ("W019", "historical: milk-jug", "sustain"),
    ("W020", "historical: milk", "sustain"),
    ("W021", "historical: wine", "sustain"),
    ("W022", "historical: beer, pot, measure, or fluid notions", "sustain"),
    ("W023", "historical: pot, measure, or fluid notions", "sustain"),
    ("W025", "historical: bring or fetch", "transition"),
    ("X002", "historical: bread", "sustain"),
    ("Y001", "historical: papyrus-roll, writing, things written, or abstract notions", "record"),
    ("Y003", "historical: scribe outfit, writing, smooth, or red", "record"),
    ("Z001", "historical: one, unity, or ideogram marker", "count"),
    ("Z002", "historical: plurality", "count"),
    ("Z003", "historical: plurality", "count"),
    ("Z004", "historical: dual or replacement of dangerous signs", "count"),
    ("Z009", "historical: break, encounter, or answer", "action"),
]


PICTURE_BLOCKS = {"Egyptian Hieroglyphs",
                  "Egyptian Hieroglyphs Extended-A",
                  "Rosetta base column"}

ROLE_REGISTER = {
    "actor": "noun", "place": "noun", "object": "noun", "yield": "noun",
    "sustain": "noun", "recover": "noun", "record": "noun",
    "action": "verb", "observe": "verb", "transition": "verb",
    "rest": "verb", "count": "adj+verb", "pause": "adj+verb",
    "proverb-opener": "adj+verb", "act-travel": "verb",
    "exchange": "verb",
}

ROLE_CONTEXT = {
    "actor": "may mark a person, creature, or participant in the nearby action",
    "place": "may set the location or conditions around the nearby action",
    "object": "may mark a thing handled, carried, collected, or shown nearby",
    "action": "may stand for doing, handling, or preparing the nearby thing",
    "yield": "may mark food, goods, or the result of nearby work",
    "sustain": "may mark provisions, refreshment, or what keeps the actor going",
    "recover": "may mark shelter, shade, rest, or recovery",
    "observe": "may mark looking, attention, awareness, or inspection",
    "transition": "may mark movement or a change between pictured actions",
    "count": "may mark repetition or amount, without a fixed number",
    "record": "may mark a message, record, name, or documented thing",
    "rest": "may mark resting or the close of a pictured episode",
}

ROLE_ACTION = {
    "actor": "may act, arrive, or be changed by the next picture",
    "place": "may mark arrival at, departure from, or work in this place",
    "object": "may be taken, given, used, carried, or exchanged",
    "action": "may name the act performed on the neighbouring picture",
    "yield": "may be gathered, produced, eaten, or stored",
    "sustain": "may be consumed or used to continue the action",
    "recover": "may provide shelter, relief, or recovery",
    "observe": "may mark the thing seen, noticed, or sought",
    "transition": "may mark motion, departure, return, or change",
    "count": "may qualify how much or how often an action occurs",
    "record": "may name, record, or communicate nearby information",
    "rest": "may close the episode or mark recovery",
    "pause": "may divide one pictured action from the next",
    "proverb-opener": "may introduce the pictured saying or situation",
    "act-travel": "may mark a journey, crossing, or repeated trip",
    "exchange": "may mark goods changing hands or being weighed",
}

def _guess_role(s):
    """Infer a functional hypothesis from the pictured object's words."""
    dep = (s.depicts or "").lower().replace("-", " ").replace("_", " ")
    if not dep or dep.startswith(("egyptian hieroglyph", "unnamed recorded mark")):
        return "object"
    if any(w in dep for w in
           ("eye", "face", "head", "eyebrow", "pupil")):
        return "observe"
    if any(w in dep for w in ("leg", "foot", "feet", "walking")):
        return "transition"
    if any(w in dep for w in ("lying", "lying-down", "sleep", "resting")):
        return "rest"
    if any(w in dep for w in
           ("mouth", "lip", "hand", "finger", "fist", "arm", "nose", "ear",
            "hair", "body", "breast", "spine", "tooth", "tongue")):
        return "action"
    if any(w in dep for w in
           ("man", "woman", "person", "child", "god", "goddess", "deity",
            "king", "priest", "mummy", "figure", "ancestor")):
        return "actor"
    if any(w in dep for w in
           ("bird", "falcon", "owl", "goose", "duck", "ibis", "vulture",
            "mammal", "bull", "cow", "horse", "donkey", "lion", "cat",
            "dog", "pig", "goat", "sheep", "antelope", "monkey", "elephant",
            "reptile", "snake", "crocodile", "lizard", "frog", "creature",
            "scorpion", "beetle", "insect", "worm")):
        return "actor"
    if any(w in dep for w in ("fish", "catfish", "tilapia")):
        return "yield"
    if any(w in dep for w in
           ("grain", "bread", "food", "cake", "fruit", "harvest")):
        return "yield"
    if any(w in dep for w in ("jar", "pot", "cup", "vessel", "beer")):
        return "sustain"
    if any(w in dep for w in
           ("tree", "plant", "flower", "reed", "papyrus plant", "leaf")):
        return "place"
    if any(w in dep for w in
           ("water", "river", "land", "earth", "sky", "sun", "moon", "star",
            "rain", "wind", "night", "day", "field", "desert", "horizon")):
        return "place"
    if any(w in dep for w in
           ("house", "building", "room", "door", "gate", "wall", "court",
            "shrine", "temple", "town", "city")):
        return "place"
    if any(w in dep for w in ("boat", "ship", "sail", "oar", "rudder")):
        return "transition"
    if any(w in dep for w in ("shade", "bed", "chair", "seat", "pillow")):
        return "recover"
    if any(w in dep for w in
           ("net", "trap", "weapon", "bow", "arrow", "spear", "knife",
            "axe", "shield", "tool", "staff", "stick", "plough", "hoe")):
        return "action"
    if any(w in dep for w in ("rope", "cord", "basket", "bag", "sack")):
        return "yield"
    if any(w in dep for w in
           ("writing", "scribe", "papyrus", "document", "book", "seal")):
        return "record"
    if any(w in dep for w in ("stroke", "mark", "tick", "line")):
        return "count"
    return "object"

def _clean_depiction(s):
    dep = (s.depicts or "").replace("-", " ").replace("_", " ")
    dep = " ".join(dep.split())
    if not dep or dep.startswith(("EGYPTIAN HIEROGLYPH", "unnamed recorded mark")):
        return "unidentified pictured mark"
    return dep

def _dep_form(s, dep):
    """Sign-specific form label used to keep generated guesses distinct."""
    if dep == "unidentified pictured mark":
        return f"unidentified mark catalogued as {s.sid}"
    return f"{dep} variant catalogued as {s.sid}"

def _catalogue_guesses(s):
    dep = _clean_depiction(s)
    role = _guess_role(s)
    source = AUTO_GUESS_SOURCE + (
        f"; shape xref {','.join(s.xref[:4])} (visual link only)"
        if s.xref else "")
    if dep == "unidentified pictured mark":
        form = _dep_form(s, dep)
        return [{
            "text": f"{form}: read this mark through its neighbours",
            "src": source, "conf": CONF_GUESS,
            "mode": "contextual", "func": "object", "reg": "noun",
            "scope": AUTO_GUESS_SCOPE,
            "flex": "no catalogue object name; nearby pictures supply the clue",
        }, {
            "text": f"the {s.sid} form of a missing object or action",
            "src": source, "conf": CONF_GUESS,
            "mode": "metaphorical", "func": "object", "reg": "adj+verb",
            "scope": AUTO_GUESS_SCOPE,
            "flex": "coverage scaffold only -- not an identification",
        }]
    form = _dep_form(s, dep)
    article = "an" if form[:1] in "aeiou" else "a"
    return [{
        "text": f"{article} {form}: the pictured thing is present in the scene",
        "src": source, "conf": CONF_GUESS,
        "mode": "literal", "func": role, "reg": "noun",
        "scope": AUTO_GUESS_SCOPE,
        "flex": "names the pictured object; adjacent signs determine its use",
    }, {
        "text": f"{article} {form}: {ROLE_CONTEXT[role]}",
        "src": source, "conf": CONF_GUESS,
        "mode": "metaphorical", "func": role,
        "reg": ROLE_REGISTER.get(role, "adj+verb"),
        "scope": AUTO_GUESS_SCOPE,
        "flex": "correlation scaffold; do not treat as a fixed translation",
    }]

def apply_catalogue_guesses(d):
    """Give every otherwise-unread pictured sign two labeled candidates.

    This is coverage-by-hypothesis: it uses the sign's literal depiction,
    catalogue category and shape xrefs as *correlation prompts*, never as
    proof or borrowed phonetic values."""
    added = 0
    for s in d.signs.values():
        if (s.block not in PICTURE_BLOCKS or s.defined
                or s.sid in d._cleared):
            continue
        for guess in _catalogue_guesses(s):
            if guess["text"] in d._removed_guesses[s.sid]:
                continue
            s.defs.append(dict(guess))
            added += 1
    return added

def _multiuse_guesses(s):
    """Return action/qualifier variants for a pictured sign.

    These are the 'multi-use variables': the same picture may be a noun in
    one column, an action prompted by its neighbours in another, or a
    qualifier/classifier for the mark beside it."""
    dep = _clean_depiction(s)
    role = (s.defs[0].get("func") if s.defs else "") or _guess_role(s)
    source = MULTIUSE_GUESS_SOURCE + (
        f"; shape xref {','.join(s.xref[:4])} (visual link only)"
        if s.xref else "")
    if dep == "unidentified pictured mark":
        return [{
            "text": (f"the {s.sid} variable: its role is supplied by "
                     "the neighbouring marks"),
            "src": source, "conf": CONF_GUESS,
            "mode": "contextual", "func": "action", "reg": "verb",
            "scope": MULTIUSE_GUESS_SCOPE,
            "flex": "can act as noun, action, or qualifier until context narrows it",
        }, {
            "text": (f"the {s.sid} classifier link: it may qualify or "
                     "connect the picture before or after it"),
            "src": source, "conf": CONF_GUESS,
            "mode": "metaphorical", "func": "object", "reg": "adj",
            "scope": MULTIUSE_GUESS_SCOPE,
            "flex": "use only when the adjacent sequence needs a bridge",
        }, {
            "text": (f"the {s.sid} result or consequence named by the "
                     "preceding action"),
            "src": source, "conf": CONF_GUESS,
            "mode": "metaphorical", "func": "yield", "reg": "noun",
            "scope": MULTIUSE_GUESS_SCOPE,
            "flex": "fallback for a missing result/object in the story",
        }]
    form = _dep_form(s, dep)
    article = "an" if form[:1] in "aeiou" else "a"
    action = ROLE_ACTION.get(role, "may take the action implied by neighbours")
    return [{
        "text": f"{article} {form}: {action}",
        "src": source, "conf": CONF_GUESS,
        "mode": "action", "func": "action", "reg": "verb",
        "scope": MULTIUSE_GUESS_SCOPE,
        "flex": "same picture may switch from noun to verb in context",
    }, {
        "text": (f"{article} {form}: may qualify, classify, or belong to "
                 "the adjacent picture"),
        "src": source, "conf": CONF_GUESS,
        "mode": "metaphorical", "func": role, "reg": "adj",
        "scope": MULTIUSE_GUESS_SCOPE,
        "flex": "possible modifier/variable use; context decides",
    }, {
        "text": (f"{article} {form}: may name the result or consequence "
                 "of the preceding action"),
        "src": source, "conf": CONF_GUESS,
        "mode": "metaphorical", "func": "yield", "reg": "noun",
        "scope": MULTIUSE_GUESS_SCOPE,
        "flex": "a possible outcome/result use when the story needs one",
    }]

def apply_multiuse_guesses(d):
    """Add action and qualifier variables to every pictured sign."""
    added = 0
    for s in d.signs.values():
        if (s.block not in PICTURE_BLOCKS or not s.defs
                or s.sid in d._cleared):
            continue
        for guess in _multiuse_guesses(s):
            if (guess["text"] in d._removed_guesses[s.sid]
                    or any(dd["text"] == guess["text"] for dd in s.defs)):
                continue
            s.defs.append(dict(guess))
            added += 1
    return added

HISTORICAL_USES_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "historical_uses.json")
_HISTORICAL_ROWS = None


def _historical_role(gloss):
    """Infer a usable story role from an English historical gloss."""
    t = gloss.lower()
    def has(*words):
        return re.search(r"\b(?:" + "|".join(words) + r")\b", t) is not None
    if has("road", "travel", "sail", "sail.*water", "come", "go", "move",
           "depart", "return", "bring", "fetch", "walk", "journey"):
        return "transition"
    if has("see", "look", "know", "perceive", "watch", "vigilant",
           "hear", "smell"):
        return "observe"
    if has("strike", "break", "cut", "build", "work", "carry", "tie",
           "bind", "seize", "throw", "fight", "action", "do", "make",
           "smite", "hide", "eat", "drink", "speak", "think", "feel"):
        return "action"
    if has("give", "offer", "exchange", "buy", "sell", "receive",
           "tribute", "tax"):
        return "exchange"
    if has("one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine", "ten", "hundred", "thousand", "dual",
           "plural", "measure"):
        return "count"
    if has("sit", "lie", "sleep", "rest", "death", "dead"):
        return "rest"
    if has("bread", "beer", "wine", "milk", "water", "food", "offering",
           "liquid", "cup", "pot", "jar", "vessel"):
        return "sustain"
    if has("clean", "pure", "cool", "protect", "heal", "recover",
           "mourn", "weary", "weak"):
        return "recover"
    if has("write", "scribe", "record", "name", "call", "festival",
           "office", "rank", "written"):
        return "record"
    if has("house", "land", "earth", "field", "town", "village", "place",
           "shore", "bank", "desert", "country", "district", "sky",
           "heaven", "world", "horizon", "under", "seat"):
        return "place"
    if has("man", "woman", "child", "person", "king", "god", "goddess",
           "enemy", "friend", "official", "soldier", "bird", "animal",
           "fish", "butcher", "herdsman", "me"):
        return "actor"
    if has("grain", "corn", "harvest", "produce", "crop", "result"):
        return "yield"
    return "object"


def _historical_use_rows():
    """Curated rows plus optional extracted PHRP semantic rows."""
    global _HISTORICAL_ROWS
    if _HISTORICAL_ROWS is None:
        rows = list(HISTORICAL_GUESSES)
        try:
            with open(HISTORICAL_USES_FILE, encoding="utf-8") as f:
                extracted = json.load(f)
        except (OSError, json.JSONDecodeError):
            extracted = []
        for row in extracted:
            for use in row.get("uses", []):
                gloss = "; ".join(re.findall(r"'([^']+)'", use)) or use
                gloss = re.sub(r"^(?:I|D|I,\s*D|d)\s+", "", gloss).strip()
                if not gloss or gloss.lower().startswith(("p ", "phon")):
                    continue
                text = f"historical: {row['description']} -- {gloss}"
                rows.append((row["sid"], text, _historical_role(gloss)))
        _HISTORICAL_ROWS = rows
    return _HISTORICAL_ROWS


def apply_historical_guesses(d):
    """Append conventional semantic uses as labelled historical candidates.

    These are external reference hypotheses only. They never replace personal
    readings, never become observations, and do not count toward verified
    knowledge until manually attested in two distinct transcribed columns."""
    added = 0
    for sid, text, role in _historical_use_rows():
        s = d.signs.get(sid)
        if not s:
            continue
        text = f"{text} [{sid} form]"
        if (sid in d._cleared or text in d._removed_guesses[sid]
                or any(dd["text"] == text for dd in s.defs)):
            continue
        s.defs.append({
            "text": text, "src": HISTORICAL_GUESS_SOURCE,
            "conf": CONF_GUESS, "mode": "historical",
            "func": role, "scope": HISTORICAL_GUESS_SCOPE,
            "flex": ("external historical semantic candidate; not evidence "
                     "in the photographed dialect"),
        })
        added += 1
    return added


def apply_specific_picture_guesses(d):
    """Add labeled hypotheses; never overwrite a user's existing readings."""
    added = 0
    carved = {row[0] for row in ROSETTA_SPEC}
    for sid, text, mode, role in PICTURE_GUESSES:
        s = d.signs.get(sid)
        if (not s or sid in d._cleared
                or text in d._removed_guesses[sid]
                or any(dd["text"] == text for dd in s.defs)):
            continue
        source = ("ReferenceDialect/Rosetta.png (visual guess)"
                  if sid in carved else
                  "catalogue shape/variant (pictured-object analogy)")
        s.defs.append({"text": text, "src": source,
                       "conf": CONF_GUESS, "mode": mode, "func": role})
        added += 1
    return added

def _language_tag_def(s, dd):
    """Fill missing format fields on one candidate; returns fields added."""
    inferred = _guess_role(s)
    tagged = 0
    if not dd.get("mode"):
        dd["mode"] = "contextual"; tagged += 1
    if not dd.get("func"):
        dd["func"] = inferred; tagged += 1
    if not dd.get("reg"):
        dd["reg"] = ("noun" if dd.get("mode") == "literal"
                     else ROLE_REGISTER.get(dd["func"], "adj+verb"))
        tagged += 1
    return tagged

def apply_language_format(d):
    """Tag pictured-sign hypotheses with the slot grammar fields.

    This is metadata only: it never creates evidence. Personal readings get
    inferred defaults so they also participate in the story-role model."""
    return sum(_language_tag_def(s, dd)
               for s in d.signs.values() if s.block in PICTURE_BLOCKS
               for dd in s.defs)

def apply_picture_guesses(d, include_catalogue=True):
    added = apply_specific_picture_guesses(d)
    if include_catalogue:
        added += apply_catalogue_guesses(d)
        added += apply_historical_guesses(d)
        added += apply_multiuse_guesses(d)
    apply_language_format(d)
    local_verification(d)
    return added

# Compounds are proposed uses of neighbouring *pictures*, not new fixed
# definitions of either member. A motif fires only for explicitly listed
# shelf marks; a shape xref alone never transfers a meaning.
# (label, first signs, following signs, possible stories, grounding)
MOTIF_RULES = [
    ("fish+water", ("N01", "K001", "K008"), ("N02", "N035", "N035A", "N036"),
     ("a fish in or beside the river -- a catch",
      "a fish outside its proper place -- an out-of-place proverb"),
     "Rosetta first two pictures; water placement is ambiguous"),
    ("fish+basket", ("N01", "K001", "K008"), ("V030", "V031"),
     ("fish put into a basket -- gathering or carrying a catch",
      "fish prepared for transport or exchange"),
     "counterexample proposed in WhatIThink.md; no photographed instance assigned"),
    ("shore+water", ("N020",), ("N035", "N035A", "N036"),
     ("land beside water -- a shore or riverbank",
      "a boundary where someone may cross or work beside the river"),
     "local Gardiner sign-list depicts N20 as tongue of land and N35 as ripple; no reading imported"),
    ("bird+eye", ("N08", "G038", "G001"), ("N03", "D004", "D006"),
     ("a journey to see a person or place",
      "an actual bird looking at the next pictured object"),
     "bird/eye adjacency proposed in WhatIThink.md"),
    ("bird+strokes", ("N08", "G038"), ("N09", "Z016B"),
     ("a traveller making repeated trips",
      "a bird with two marks -- a count, not necessarily a journey"),
     "annotated Rosetta bird above strokes"),
    ("bird+horizon", ("N08", "G038", "G001"), ("N027",),
     ("setting out toward or looking over the horizon",
      "a bird actually pictured at sunrise or sunset"),
     "analogy to Reference1 column 8; exact sign identity not transcribed"),
    ("water+boat", ("N035", "N035A", "N036", "N02"), ("P001", "P002"),
     ("a boat crossing the water",
      "boats or cargo kept on the river"),
     "picture analogy; requires a transcribed occurrence"),
    ("boat+basket", ("P001", "P002"), ("V030", "V031"),
     ("goods carried by boat in a basket",
      "a boat and basket drawn together without a specified journey"),
     "boat and basket pictured-object labels; no photographed instance assigned"),
    ("net+fish", ("T024",), ("K001", "K008", "N01"),
     ("fish caught in a net",
      "a fish near a net, not necessarily caught"),
     "picture analogy; requires a transcribed occurrence"),
    ("eye+person", ("D004", "D006", "N03"), ("A021", "A002", "N04"),
     ("someone sees the person that follows",
      "the person's own eye or attention"),
     "eye/figure pattern proposed in TestResults.md"),
    ("coil+slit", ("N05",), ("N06", "Z016"),
     ("a coiled thing carried through an opening",
      "work on a coiled item, then a pause or divider"),
     "adjacent Rosetta pictures; opening vs divider unresolved"),
    ("slit+base", ("N06", "Z016"), ("N07", "N001"),
     ("a gap followed by a foundation or solid ground",
      "a pause between work on the coil and the next scene"),
     "adjacent Rosetta pictures; object identities tentative"),
    ("yield+box", ("N11", "M034"), ("N12",),
     ("a harvested yield put in a container",
      "goods weighed or exchanged -- scale is only a guess"),
     "adjacent Rosetta pictures; no purchase/sale proven"),
    ("box+slip", ("N12",), ("N13", "Z016A"),
     ("a container followed by a scene break",
      "a container followed by a receipt or token"),
     "adjacent Rosetta pictures; slip is ambiguous"),
    ("grain+basket", ("M034", "M033", "O051", "N11"),
     ("V030", "V031"),
     ("grain gathered in a basket",
      "stored harvest or provisions for a later journey"),
     "picture analogy; requires a transcribed occurrence"),
    ("shade+plant", ("N14", "M001"), ("N15", "W015"),
     ("shade followed by water or refreshment",
      "trees or plants simply marking the setting"),
     "Rosetta closing pictures; plant and drink are guesses"),
    ("drink+rest", ("N15", "W015"), ("N16", "A056"),
     ("after drinking, the person rests",
      "a jar beside a reclining person, without fixed event order"),
     "Rosetta closing pictures"),
]

# Short photo fragments transcribed at the *shape* level only. Unknown
# drawings deliberately remain descriptions rather than forced catalogue IDs.
PHOTO_FRAGMENTS = [
    ("ReferenceDialect/Reference2.png (center columns)",
     "bird-like outlines alternating with line marks and containers",
     "several visits or trips with goods",
     "actual birds and household or waterside objects"),
    ("CorrectedTestImages/p2_river_both_banks.png",
     "two parallel wavy banks in one mark",
     "one river seen with both banks", "not two separate rivers"),
    ("CorrectedTestImages/p3_flatline_sentence_end.png",
     "a flat stroke at a boundary",
     "end of a sentence or episode", "a platform or pictured object"),
    ("CorrectedTestImages/p6_col8_structure.png",
     "bird/ticks, divider, loop-like mark, uprights, eyes further below",
     "travel, pause, encounter, then looking",
     "actual birds and objects in successive scenes"),
    ("CorrectedTestImages/p7_spot_later_same_place.png",
     "dots beside a line; dots recur",
     "later at the same place", "repeat of an amount or time mark"),
    ("CorrectedTestImages/p7_spot_absent.png",
     "dots alongside a standing figure",
     "a location with someone absent",
     "a person standing by a count or place marker"),
    ("CorrectedTestImages/p10_snail_standing_eyes.png",
     "a coiled creature with raised eye stalks",
     "a creature moving or carrying a burden",
     "a pictured creature, not necessarily bait"),
]

# External galleries are used as checks on graphic variation only. IDs are
# catalogue shelf labels, never asserted letter or numerical values.
VISUAL_SOURCE_LINKS = {
    "G017": ("multiple separately painted owl forms",
             "https://www.digital-epigraphy.com/public/painted-hieroglyph?qby=source&qv=4"),
    "G038": ("photographed and painted white-fronted goose variants",
             "https://www.phrp.be/ListOccurrences.php?Gard=G38&SignKey=282"),
    "N020": ("a long tongue of land / shore shape in Thot Sign List",
             "https://thotsignlist.org/mysign?id=4205"),
    "N035": ("multiple painted water-ripple forms",
             "https://www.digital-epigraphy.com/public/painted-hieroglyph?qby=source&qv=4"),
    "V030": ("multiple painted basket forms",
             "https://www.digital-epigraphy.com/public/painted-hieroglyph?qby=source&qv=4"),
}

SOURCE_CLUES = [
    ("Unicode 18 code charts (local PDFs)",
     "reference drawings only; chart shapes are explicitly not prescriptive"),
    ("Gardiner's sign-list PDF / local wikitext",
     "pictured-object descriptions and warning that original signs vary by context"),
    ("Thot Sign List, N20",
     "describes the pictured sign as a long tongue of land -- useful shape clue"),
    ("PHRP G38 occurrences",
     "five photographed/painted goose occurrences show colour and drawing variation"),
    ("digitalEPIGRAPHY painted-hieroglyph gallery",
     "multiple physical renderings of owl G17, water N35, and basket V30"),
    ("British Museum EA24 record",
     "real Rosetta Stone is a three-script stela; this project's annotated "
     "column remains a separate crop, not a bilingual key"),
]

def motif_matches(entries):
    """Return reproducible hypotheses for adjacent, ordered sign pairs."""
    signs = [e for e in entries if e not in ("[", "]")]
    return [(i + 1, a, b, label, stories, grounding)
            for i, (a, b) in enumerate(zip(signs, signs[1:]))
            for label, first, second, stories, grounding in MOTIF_RULES
            if a in first and b in second]

def motif_counts(d):
    """Count motifs by distinct saved column contents, not re-teaching."""
    counts = defaultdict(set)
    for entries in d.columns.values():
        fingerprint = tuple(entries)
        for _, a, b, label, _, _ in motif_matches(entries):
            counts[(a, b, label)].add(fingerprint)
    return {key: len(columns) for key, columns in counts.items()}

VERB_ROLES = {"action", "observe", "transition", "exchange", "record",
              "rest", "pause", "count"}
NOUN_ROLES = {"actor", "object", "place", "yield", "sustain", "recover",
              "proverb-opener"}
CLOSE_ROLES = {"yield", "transition", "sustain", "recover", "rest",
               "exchange", "record", "place"}


def _profile_dd(item):
    """Accept either a definition dict or a (sid, sign, definition) tuple."""
    return item[2] if isinstance(item, tuple) else item


def _is_verb_dd(dd):
    return (dd.get("reg") in ("verb", "adj+verb")
            or dd.get("func", "").startswith("act-")
            or dd.get("func") in VERB_ROLES
            or dd.get("func") in ("yield", "sustain", "recover"))


def _is_noun_dd(dd):
    return (dd.get("reg") in ("noun", "adj")
            or dd.get("func") in NOUN_ROLES)


STRONG_VERB_ROLES = {"action", "observe", "transition", "exchange",
                     "record", "count", "rest", "pause"}


def _is_strong_verb_dd(dd):
    return (dd.get("func", "").startswith("act-")
            or dd.get("func") in STRONG_VERB_ROLES)


def english_sequence_profile(selected):
    """Score whether selected candidates can be rendered as English prose.

    A column may be either an English-like clause (subject, one dominant
    action, complement, closure) or a grammatical scene description (a
    noun frame ending on a closing noun). This is an internal readability
    gate only; it does not prove the historical language used English
    word order or semantics."""
    defs = [_profile_dd(x) for x in selected]
    empty = {"score": 0, "readable": False, "subject": False,
             "action": False, "complement": False, "closure": False,
             "order": False, "flow": False, "registers": False,
             "pattern": False, "specific": False, "mode": "none"}
    if not defs:
        return empty
    subject_i = next((i for i, dd in enumerate(defs) if _is_noun_dd(dd)), -1)
    strong = [i for i, dd in enumerate(defs)
              if i > subject_i and _is_strong_verb_dd(dd)]
    action_i = next((i for i in strong if i < len(defs) - 1),
                    strong[-1] if strong else -1)
    nouns = [i for i, dd in enumerate(defs)
             if i != subject_i and i != action_i and _is_noun_dd(dd)]
    scene = action_i < 0 and len(nouns) >= 2
    checks = {
        "subject": subject_i >= 0,
        "action": action_i >= 0,
        "complement": bool(nouns),
        "closure": (defs[-1].get("func") in CLOSE_ROLES
                    or defs[-1].get("reg") == "noun"),
        "order": action_i < 0 or subject_i >= 0 and action_i > subject_i,
        "flow": action_i < 0
                or len([i for i in strong if i != len(defs) - 1])
                <= max(1, len(defs) // 3),
        "registers": any(dd.get("reg") in ("noun", "adj") for dd in defs)
                     and any(_is_verb_dd(dd) for dd in defs),
        "pattern": action_i >= 0 or scene,
        "specific": sum(dd.get("scope") != MULTIUSE_GUESS_SCOPE
                        for dd in defs) >= max(1, len(defs) // 2),
    }
    score = sum(checks.values())
    readable = (score >= 7 and checks["subject"] and checks["complement"]
                and checks["closure"] and checks["order"]
                and checks["flow"] and checks["pattern"])
    return {"score": score, "readable": readable,
            "mode": "clause" if action_i >= 0 else "scene", **checks}


def _verb_phrase(dd):
    """Turn an action-role candidate into a readable English verb phrase."""
    text = dd["text"].lower()
    pairs = (("see", "sees"), ("look", "looks at"),
             ("watch", "watches"), ("observe", "observes"),
             ("travel", "travels toward"), ("sail", "sails toward"),
             ("move", "moves toward"), ("walk", "walks toward"),
             ("come", "comes to"), ("return", "returns to"),
             ("eat", "eats"), ("drink", "drinks"), ("speak", "speaks"),
             ("rest", "rests"), ("sleep", "sleeps"), ("lie", "lies"),
             ("sit", "sits"), ("carry", "carries"), ("gather", "gathers"),
             ("collect", "collects"), ("build", "builds"), ("hide", "hides"),
             ("give", "gives"), ("offer", "offers"), ("bring", "brings"),
             ("fetch", "fetches"), ("record", "records"), ("count", "counts"),
             ("strike", "strikes"), ("know", "knows"), ("hear", "hears"))
    for needle, phrase in pairs:
        if re.search(rf"\b{re.escape(needle)}", text):
            return phrase
    return {"observe": "looks at", "transition": "moves toward",
            "exchange": "exchanges", "record": "records",
            "count": "counts", "rest": "rests", "pause": "pauses",
            "act-travel": "travels toward", "act-visit": "visits",
            "yield": "receives", "sustain": "is sustained by",
            "recover": "recovers", "action": "acts upon"}.get(
                dd.get("func"), "relates to")


def _noun_phrase(s, dd):
    base = (s.depicts or "thing").replace("-", " ").replace("_", " ")
    if not base or base == "unnamed recorded mark":
        base = dd["text"].split(":", 1)[0].strip("a ") or "thing"
    return f"the {base}"


def _english_slots(selected):
    """Pick subject/action/complement/closure slots from selected readings."""
    picked = [_profile_dd(x) for x in selected]
    signs = [x[1] if isinstance(x, tuple) else None for x in selected]
    si = next((i for i, dd in enumerate(picked) if _is_noun_dd(dd)), -1)
    ai = next((i for i, dd in enumerate(picked)
               if i > si and _is_strong_verb_dd(dd)), -1)
    nouns = [i for i, dd in enumerate(picked)
             if i not in (si, ai) and _is_noun_dd(dd)]
    if not nouns:
        ci = -1
    else:
        ci = min(nouns, key=lambda i: (
            {"place": 0, "object": 1, "yield": 2, "sustain": 3,
             "recover": 4, "actor": 5}.get(picked[i].get("func"), 6),
            abs(i - ai) if ai >= 0 else i))
    return signs, picked, si, ai, ci


def english_rendering(selected):
    """Render selected picture uses as one compact English-form hypothesis."""
    signs, picked, si, ai, ci = _english_slots(selected)
    if si < 0:
        return " / ".join(dd["text"] for dd in picked)
    subject = _noun_phrase(signs[si], picked[si]) if signs[si] else "the scene"
    if ai < 0:
        nouns = [_noun_phrase(signs[i], picked[i])
                 for i, dd in enumerate(picked) if i != si and _is_noun_dd(dd)]
        return f"{subject} is pictured with {', '.join(nouns)}." if nouns else subject + "."
    verb = _verb_phrase(picked[ai])
    obj = (_noun_phrase(signs[ci], picked[ci])
           if ci >= 0 and signs[ci] else "the adjacent picture")
    last_func = picked[-1].get("func")
    ending = (" and rests" if last_func == "rest"
              else " and recovers" if last_func == "recover"
              else " and is sustained" if last_func == "sustain"
              else " and continues" if last_func == "transition"
              else "")
    return f"{subject} {verb} {obj}{ending}."



LOCAL_SUPPORTED = "internally-supported"
LOCAL_CORROBORATED = "locally-corroborated"


def _local_layer(dd):
    """Candidate layers that can agree without external attestations."""
    return {HISTORICAL_GUESS_SCOPE: "historical",
            AUTO_GUESS_SCOPE: "catalogue",
            MULTIUSE_GUESS_SCOPE: "multiuse"}.get(dd.get("scope"),
                                                  "specific")


def local_verification(d, annotate=True):
    """Score candidate uses against the internal correlation/language model.

    This is deliberately NOT historical verification: generated guesses,
    PHRP semantic candidates, motifs, and learned correlations can only
    corroborate each other inside the program. A candidate is locally
    corroborated when it has format metadata, support from two distinct
    layers, a shape or grammar fit, at least five total checks, and one
    actual-context signal (selection, motif, or learned matrix)."""
    apply_language_format(d)
    chosen = defaultdict(set)
    readable_picks = defaultdict(set)
    motifs = defaultdict(list)
    for entries in dict.fromkeys(tuple(x) for x in d.columns.values()):
        positions = _positions(d, entries)
        picks = _select(d, positions)
        selected = []
        for i, (sid, _g) in enumerate(positions):
            if picks.get(i) is not None:
                chosen[sid].add(picks[i])
                selected.append((sid, d.signs[sid], d.signs[sid].defs[picks[i]]))
        if english_sequence_profile(selected)["readable"]:
            for sid, _s, dd in selected:
                readable_picks[sid].add(d.signs[sid].defs.index(dd))
        for _pos, a, b, label, stories, grounding in motif_matches(entries):
            motifs[a].append((label, stories, grounding))
            motifs[b].append((label, stories, grounding))

    rows, signs, supported = [], set(), set()
    for s in d.signs.values():
        if s.block not in PICTURE_BLOCKS:
            continue
        for di, dd in enumerate(s.defs):
            text_tokens = tokens(dd["text"])
            depiction_tokens = tokens(s.depicts or "")
            layers = {_local_layer(other)
                      for other in s.defs if other is not dd
                      and ((tokens(other["text"]) & text_tokens)
                           or other.get("func") == dd.get("func"))}
            motif_context = " ".join(
                " ".join(stories) + " " + grounding
                for _label, stories, grounding in motifs.get(s.sid, ()))
            checks = {
                "shape": bool(depiction_tokens & text_tokens)
                         or dd.get("mode") == "literal",
                "layers": len(layers) >= 2,
                "format": all(dd.get(k) for k in ("mode", "func", "reg")),
                "grammar": (dd.get("func") == _guess_role(s)
                            or (dd.get("mode") == "literal"
                                and ROLE_REGISTER.get(dd.get("func"))
                                == dd.get("reg"))),
                "context": di in chosen.get(s.sid, ()),
                "motif": bool(motifs.get(s.sid))
                         and bool(text_tokens & tokens(motif_context)),
                "matrix": any(d.corr.get(f"{s.sid}#{di}", other)
                              for m in d.corr.w.values() for other in m),
                "english": di in readable_picks.get(s.sid, ()),
            }
            score = sum(checks.values())
            context_support = (checks["context"] or checks["motif"]
                               or checks["matrix"])
            verified = (score >= 5 and checks["layers"]
                        and checks["format"] and context_support
                        and (checks["shape"] or checks["grammar"]))
            status = (LOCAL_CORROBORATED if verified
                      else LOCAL_SUPPORTED if score >= 4
                      and checks["layers"] and checks["format"]
                      else "proposal")
            if annotate:
                dd["local"] = {"score": score, "status": status,
                               "checks": [k for k, v in checks.items() if v]}
            if status == LOCAL_SUPPORTED:
                supported.add(s.sid)
            if verified:
                signs.add(s.sid)
                rows.append({"sid": s.sid, "index": di + 1, "text": dd["text"],
                             "score": score, "checks": checks})
    rows.sort(key=lambda r: (-r["score"], r["sid"], r["index"]))
    return {"total": sum(s.block in PICTURE_BLOCKS for s in d.signs.values()),
            "verified_signs": len(signs), "supported_signs": len(supported),
            "verified": rows,
            "verified_ids": {r["sid"] for r in rows}}


def local_report(d, query=None):
    """Report local corroboration without pretending it is external proof."""
    info = local_verification(d)
    if query:
        q = query.lower()
        info["verified"] = [r for r in info["verified"]
                            if q in r["sid"].lower() or q in r["text"].lower()
                            or q in (d.signs[r["sid"]].depicts or "").lower()]
    total = info["total"]
    pct = (100.0 * info["verified_signs"] / total) if total else 0.0
    bar("LOCAL CORRELATION VERIFICATION (INTERNAL ONLY)")
    print(f"  locally corroborated signs : {info['verified_signs']:,}/{total:,} "
          f"({pct:.4f}%)")
    print(f"  locally supported signs    : {info['supported_signs']:,}/{total:,}")
    print(f"  corroborated candidates    : {len(info['verified']):,}")
    for row in info["verified"]:
        s = d.signs[row["sid"]]
        marks = ",".join(k for k, v in row["checks"].items() if v)
        print(wrap(f"  {row['sid']:<6} #{row['index']} score {row['score']}/8 "
                   f"[{marks}] {row['text']}", width=W))
    print("  These are findings whose candidate layers, depiction, language")
    print("  roles, selected context, motifs, matrix, and English-form")
    print("  readability agree.")
    print("  External verification still requires two distinct transcribed")
    print("  columns and remains separately reported.")
    bar()


def motifs_report(d, entries=None):
    entries = d.rosetta_column if entries is None else entries
    bar("COMPOUND PICTURE GUESSES (NOT VERIFIED)")
    hits = motif_matches(entries)
    counts = motif_counts(d)
    for pos, a, b, label, stories, grounding in hits:
        print(f"  {pos:>2}. {a} + {b} [{label}] "
              f"({counts.get((a, b, label), 0)} distinct saved columns)")
        print(wrap(f"      A: {stories[0]}", width=W))
        print(wrap(f"      B: {stories[1]}", width=W))
        print(wrap(f"      basis: {grounding}", width=W))
    if not hits:
        print("  No known adjacent picture motifs; individual marks may still have uses.")
    print("  These matches do not update the matrix or verified coverage.")
    print("  Photo-only shape fragments (no claimed shelf-mark matches):")
    for path, shapes, first, alternative in PHOTO_FRAGMENTS:
        print(wrap(f"    {path}: {shapes}. Guess: {first}; "
                   f"alternative: {alternative}.", width=W))
    bar()

def sources_report():
    """Summarize external materials used only for pictured-shape evidence."""
    bar("EXTERNAL VISUAL SOURCES (NO LETTER/NUMBER VALUES)")
    print("  These sources were checked for drawing style, pictured objects,")
    print("  variants, and surrounding-image context only.")
    for source, clue in SOURCE_CLUES:
        print(wrap(f"  - {source}: {clue}", width=W))
    print("  Sign-specific visual clues:")
    for sid, (description, url) in sorted(VISUAL_SOURCE_LINKS.items()):
        print(wrap(f"    {sid}: {description} -- {url}", width=W))
    print("  Phonetic, alphabetic, and numeric fields were ignored.")
    print("  No external source supplies an attestation for this dialect.")
    bar()


def history_report(d, query=None):
    """Show conventional semantic candidates kept separate from evidence."""
    rows = [(s, dd) for s in d.signs.values()
            for dd in s.defs if dd.get("scope") == HISTORICAL_GUESS_SCOPE]
    q = (query or "").lower()
    if q:
        rows = [(s, dd) for s, dd in rows
                if q in s.sid.lower() or q in (s.depicts or "").lower()
                or q in dd["text"].lower()]
    bar("HISTORICAL SEMANTIC CANDIDATES (NOT PHOTO EVIDENCE)")
    print(f"  {len(rows):,} PHRP ideogram/determinative candidates loaded.")
    print("  These supplement picture-first guesses; they do not attest this dialect.")
    for s, dd in rows:
        print(wrap(f"  {s.sid:<7} {s.char or '?':<2} {s.depicts or '-'}: "
                   f"{dd['text']}  [{dd.get('func','?')}/{dd.get('reg','?')}]",
                   width=W))
    bar()

# ==============================================================================
# SECTION 3 -- THE DIALECT STORE (your perspective, persisted)
# ==============================================================================

DIALECT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "egyptian_dialect.json")

class Dialect:
    def __init__(self):
        self.signs = seed_rosetta(build_catalogue())
        self._baseline = {sid: (s.note, s.depicts)
                          for sid, s in self.signs.items()}
        self._cleared = set()
        self._removed_guesses = defaultdict(set)
        self.corr = Correlator()          # the learned correlation matrix
        # rosetta column layout: list of sids; '[' ']' = proverb markers
        self.rosetta_column = self._rosetta_layout()
        self.columns = {"rosetta": self.rosetta_column}
        self.scratch = []   # the column being composed
        # circled clusters -> ONE holistic meaning each (chengyu-style)
        self.clusters = {k: dict(v) for k, v in CLUSTER_SEED.items()}
        self.attestations = []  # independent, manually reviewed uses
        self.taught = []        # column fingerprints already reinforced
        self.transcriptions = {}  # supervised image matches, not evidence

    def _rosetta_layout(self):
        out = []
        for sid, _n, _c, _s, _m, _nt, grp, _x in ROSETTA_SPEC:
            if grp == "B" and sid == "N08":
                out.append("[")
            out.append(sid)
            if grp == "B" and sid == "N09":
                out.append("]")
        return out

    # -- persistence -------------------------------------------------------
    def save(self, path=DIALECT_FILE):
        data = {
            "version": 4,
            "definitions": {
                sid: {"defs": s.defs, "note": s.note, "depicts": s.depicts}
                for sid, s in self.signs.items()
                if (s.defined or sid in self._cleared
                    or sid in self._removed_guesses
                    or (s.note, s.depicts) != self._baseline[sid])
            },
            "cleared": sorted(self._cleared),
            "removed_guesses": {sid: sorted(texts)
                                for sid, texts in self._removed_guesses.items()
                                if texts},
            "columns": self.columns,
            "matrix": self.corr.w,
            "clusters": self.clusters,
            "attestations": self.attestations,
            "taught": self.taught,
            "transcriptions": self.transcriptions,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return path

    def load(self, path=DIALECT_FILE):
        if not os.path.exists(path):
            return False
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        version = data.get("version", 1)
        self._cleared = set(data.get("cleared", []))
        self._removed_guesses = defaultdict(set, {
            sid: set(texts)
            for sid, texts in data.get("removed_guesses", {}).items()
        })
        for sid, d in data.get("definitions", {}).items():
            if sid not in self.signs:
                continue
            s = self.signs[sid]
            if "defs" in d and (d["defs"] or sid in self._cleared):
                built_in = [dict(dd) for dd in s.defs
                            if dd.get("conf") == CONF_GUESS]
                s.defs = [dict(dd) for dd in d["defs"]]
                if sid not in self._cleared:
                    for dd in built_in:
                        if (dd["text"] not in self._removed_guesses[sid]
                                and not any(x["text"] == dd["text"]
                                            for x in s.defs)):
                            s.defs.append(dd)
            elif "defs" in d and version < 4 and s.kind == "rosetta" \
                    and any(row[0] == sid and row[4] for row in ROSETTA_SPEC):
                # Old saves have no explicit-cleared flag. Only a seeded
                # Rosetta reading can safely be treated as intentionally removed.
                s.defs = []
            elif d.get("meaning", UNKNOWN) != UNKNOWN:   # v1 back-compat
                s.defs = [{"text": d["meaning"],
                           "src": d.get("source", "")}]
            for dd in s.defs:
                if (version < 4 and dd.get("conf") == CONF_LIKELY and
                        dd.get("src") == "Nathan -- Rosetta base column"):
                    dd["conf"] = CONF_GUESS
            s.note = d.get("note", "")
            if d.get("depicts"):
                s.depicts = d["depicts"]
        self.columns.update(data.get("columns", {}))
        self.corr.w = data.get("matrix", {})
        self.clusters.update(data.get("clusters", {}))
        for rec in self.clusters.values():
            for dd in _norm_cluster(rec)["defs"]:
                if (dd.get("conf") == CONF_LIKELY and
                        dd.get("src") == "Nathan -- Rosetta base column"):
                    dd["conf"] = CONF_GUESS
        self.attestations = data.get("attestations", [])
        self.taught = data.get("taught", [])
        self.transcriptions = data.get("transcriptions", {})
        for s in self.signs.values():
            if s.block in PICTURE_BLOCKS:
                for dd in s.defs:
                    _language_tag_def(s, dd)
        return True

    # -- operations --------------------------------------------------------
    def define(self, sid, meaning, source="Nathan -- personal reading"):
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}   (try 'catalog' to browse shelf marks)"
        if any(dd["text"] == meaning for dd in s.defs):
            return f"{sid} already carries that reading."
        dd = {"text": meaning, "src": source}
        s.defs.append(dd)
        if s.block in PICTURE_BLOCKS:
            _language_tag_def(s, dd)
        self._cleared.discard(sid)
        self._removed_guesses[sid].discard(meaning)
        return f"{sid} +reading#{len(s.defs)} := {meaning}"

    def undefine(self, sid, n=None):
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if n is None:
            s.defs = []
            self._cleared.add(sid)
            return f"{sid} -- all readings dropped; back to UNKNOWN."
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        gone = s.defs.pop(n - 1)
        if gone.get("conf") == CONF_GUESS:
            self._removed_guesses[sid].add(gone["text"])
        if not s.defs:
            self._cleared.add(sid)
        return f"{sid} -reading#{n} ({gone['text'][:40]})  [{len(s.defs)} left]"

    def prefer(self, sid, n):
        """Promote candidate reading #n to primary (defs[0])."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        s.defs.insert(0, s.defs.pop(n - 1))
        return f"{sid} primary := {s.defs[0]['text']}"

    def double(self, sid, n, sense):
        """Attach a co-valid SECOND SENSE to candidate #n -- a deliberate
        double meaning, like an English pun: both readings stand at once."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        s.defs[n - 1]["also"] = sense
        return f"{sid} #{n} now reads double: {sense}"

    def depict(self, sid, text):
        """Record what a mark literally DEPICTS (the drawn object) -- the
        mask, separate from its meanings. Evolved use means a confusing
        image can mean something entirely different."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        s.depicts = text
        return f"{sid} depicts: {text}"

    def mode(self, sid, n, mode):
        """Tag candidate #n with a reading mode: 'evolved' (image != meaning),
        'action' (stick-figure act), 'literal', or '-' to clear."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        if mode in ("-", "none"):
            s.defs[n - 1].pop("mode", None)
            return f"{sid} #{n} mode cleared."
        s.defs[n - 1]["mode"] = mode
        return f"{sid} #{n} mode := {mode}"

    def func(self, sid, n, role):
        """Tag candidate #n with its FUNCTION in the strip (actor, place,
        action, yield, rest...) -- what the symbol DOES, not what it draws."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        if role in ("-", "none"):
            s.defs[n - 1].pop("func", None)
            return f"{sid} #{n} function cleared."
        s.defs[n - 1]["func"] = role
        return f"{sid} #{n} function := {role}"

    def reg(self, sid, n, reg):
        """Tag candidate #n's register(s): adj, verb, noun, adj+verb... --
        a reading is used adjectivally while also verbally, at once or not."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        if reg in ("-", "none"):
            s.defs[n - 1].pop("reg", None)
            return f"{sid} #{n} register cleared."
        s.defs[n - 1]["reg"] = reg
        return f"{sid} #{n} register := {reg}"

    def flex(self, sid, n, note):
        """Note candidate #n's terminology FLEX: how the reading shifts with
        neighbouring marks ('fish out of water' holds only near 'water' --
        fish beside a basket reads 'fish basket')."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        if note in ("-", "none"):
            s.defs[n - 1].pop("flex", None)
            return f"{sid} #{n} flex note cleared."
        s.defs[n - 1]["flex"] = note
        return f"{sid} #{n} flex := {note}"

    def concrete(self, sid, n):
        """Toggle candidate #n's CONCRETE flag -- a locked reading. Every
        reading is flexible by default in this dialect; concrete marks the
        exceptions that do not bend with terminology."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        dd = s.defs[n - 1]
        if dd.get("concrete"):
            dd.pop("concrete")
            return f"{sid} #{n} back to flexible."
        dd["concrete"] = True
        return f"{sid} #{n} marked concrete (locked)."

    def undouble(self, sid, n):
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)) or "also" not in s.defs[n - 1]:
            return f"{sid} #{n} carries no second sense"
        s.defs[n - 1].pop("also")
        return f"{sid} #{n} back to a single sense."

    def likely(self, sid, n):
        """Flag candidate reading #n 'highly likely' -- you have seen this
        reading hold up where the story is clearly depicted."""
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        if not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        s.defs[n - 1]["conf"] = CONF_LIKELY
        return f"{sid} #{n} flagged {CONF_LIKELY}."

    def note(self, sid, text):
        s = self.signs.get(sid)
        if not s:
            return f"no such sign: {sid}"
        s.note = text
        return f"{sid} note set."

    # -- clusters: circled groups that mean ONE whole concept --------------
    def cluster_for(self, members):
        """Look up a condensed group's record; tries the column order first,
        then unordered (a circle may wrap its signs either way)."""
        rec = (self.clusters.get("+".join(members))
               or self.clusters.get("+".join(sorted(members))))
        return _norm_cluster(rec) if rec else None

    def define_cluster(self, members, meaning,
                       source="Nathan -- personal reading"):
        """Append a candidate whole-proverb reading to a cluster."""
        key = "+".join(members)
        rec = _norm_cluster(self.clusters.setdefault(key, {"defs": []}))
        if any(dd["text"] == meaning for dd in rec["defs"]):
            return f"cluster {key} already carries that reading."
        rec["defs"].append({"text": meaning, "src": source})
        return f"cluster {key} +reading#{len(rec['defs'])} := {meaning}"

    def drop_cluster(self, members):
        for k in ("+".join(members), "+".join(sorted(members))):
            if k in self.clusters:
                del self.clusters[k]
                return f"cluster {'+'.join(members)} removed"
        return "no such cluster"

    def learn_column(self, entries):
        """Endorse a column's reading: reinforce every pair of chosen
        readings in the correlation matrix. Repeated identical columns
        cannot manufacture independent support."""
        fingerprint = [e for e in entries if e in ("[", "]") or e in self.signs]
        if not fingerprint or fingerprint in self.taught:
            return 0
        positions = _positions(self, entries)
        chosen = _select(self, positions)
        keys = [f"{sid}#{di}" for i, (sid, _g) in enumerate(positions)
                for di in [chosen.get(i, -1)] if di >= 0]
        # clusters learn too: reinforce the circled meme's chosen proverb
        # against each of its members -- the marks beside a meme complete it
        groups, cur = [], None
        for e in entries:
            if e == "[":
                cur = []
            elif e == "]":
                if cur is not None:
                    groups.append(cur)
                cur = None
            elif cur is not None:
                cur.append(e)
        if cur is not None:
            groups.append(cur)
        for grp in groups:
            rec = self.cluster_for(grp)
            if rec:
                di = _cluster_pick(self, rec, grp, positions, chosen)
                keys.append(f"CL:{'+'.join(sorted(grp))}#{di}")
                for msid in grp:
                    for i, (sid, _g) in enumerate(positions):
                        if sid == msid and chosen.get(i, -1) >= 0:
                            keys.append(f"{sid}#{chosen[i]}")
        self.corr.reinforce(keys)
        self.taught.append(fingerprint)
        return len(keys)

    def attest(self, source, column, sid, n):
        """Record a human-checked use, never an engine prediction.
        Sources identify images/manuscripts; columns are independently
        transcribed records within them."""
        entries = self.columns.get(column)
        s = self.signs.get(sid)
        if not source.strip() or not entries or sid not in entries:
            return "attest requires a source and a saved column containing the sign"
        if not s or not (1 <= n <= len(s.defs)):
            return f"{sid} has no reading #{n}"
        text = s.defs[n - 1]["text"]
        key = (source.strip(), column, sid)
        self.attestations = [a for a in self.attestations
                             if (a["source"], a["column"], a["sid"]) != key]
        self.attestations.append({"source": source.strip(), "column": column,
                                  "sid": sid, "reading": text,
                                  "entries": list(entries)})
        return f"{sid} #{n} attested in {source.strip()} / {column} (provisional)"

    def evidence(self):
        """Per-sign audit. One witness = one distinct transcribed column;
        matching a shape/xref or repeating the same column is not a witness."""
        seen = defaultdict(lambda: defaultdict(set))
        for a in self.attestations:
            s = self.signs.get(a.get("sid"))
            col = self.columns.get(a.get("column"), [])
            if (s and a.get("entries") == col and a.get("sid") in col and
                    any(dd["text"] == a.get("reading") for dd in s.defs)):
                seen[s.sid][a["reading"]].add(tuple(col))
        return seen

    def observed_pairs(self):
        """Adjacent glyphs in distinct transcribed columns (not guessed
        English). Duplicate copies of a column count only once."""
        pairs = defaultdict(set)
        unique = set()
        for name, entries in self.columns.items():
            fingerprint = tuple(entries)
            if fingerprint in unique:
                continue
            unique.add(fingerprint)
            marks = [e for e in entries if e in self.signs]
            for a, b in zip(marks, marks[1:]):
                pairs[tuple(sorted((a, b)))].add(name)
        return pairs

    def progress(self):
        """Catalogue and picture-script coverage, not translation accuracy.
        Coptic/Meroitic letters and layout controls are not picture signs."""
        seen = self.evidence()
        eligible = [s for s in self.signs.values() if s.kind != "mark"]
        pictured = [s for s in eligible
                    if s.block in ("Egyptian Hieroglyphs",
                                   "Egyptian Hieroglyphs Extended-A",
                                   "Rosetta base column")]
        verified = {sid for sid, uses in seen.items()
                    if any(len(witnesses) >= 2 for witnesses in uses.values())}
        polysemous = {sid for sid, uses in seen.items() if len(uses) > 1}
        return {"total": len(eligible),
                "proposed": sum(s.defined for s in eligible),
                "attested": sum(s.sid in seen for s in eligible),
                "verified": sum(s.sid in verified for s in eligible),
                "pictured_total": len(pictured),
                "pictured_proposed": sum(s.defined for s in pictured),
                "pictured_auto": sum(any(dd.get("scope") in AUTO_SCOPES
                                         for dd in s.defs)
                                     for s in pictured),
                "pictured_multi": sum(len(s.defs) >= 4 and
                                        any(dd.get("scope") == MULTIUSE_GUESS_SCOPE
                                            for dd in s.defs)
                                        for s in pictured),
                "format_ready": sum(bool(s.defs) and all(
                    dd.get("mode") and dd.get("func") and dd.get("reg")
                    for dd in s.defs) for s in pictured),
                "pictured_verified": sum(s.sid in verified for s in pictured),
                "polysemous": len(polysemous)}

    def stats(self):
        total = len(self.signs)
        defined = sum(1 for s in self.signs.values() if s.defined)
        return total, defined, total - defined

# ==============================================================================
# SECTION 4 -- THE READER (top->down, columns left->right, proverb groups)
# ==============================================================================

def render_sign_lines(d, sid, width=20):
    """The mark as a little block of lines (sketch or char)."""
    s = d.signs.get(sid)
    if s is None:
        return [" <?> ", f" no sign '{sid}' "]
    if s.sketch:
        return [ln[:width] for ln in s.sketch]
    return ["", f"      {s.char}", ""]


def _positions(d, entries):
    """Flatten column entries -> [(sid, group_id_or_None)] top to bottom."""
    pos, gid, next_gid = [], None, 0
    for e in entries:
        if e == "[":
            next_gid += 1
            gid = next_gid
        elif e == "]":
            gid = None
        else:
            pos.append((e, gid))
    return pos


def _dtokens(dd):
    """Imagery tokens of a candidate reading -- including its second sense
    when the reading is a deliberate double meaning."""
    return tokens(dd["text"]) | tokens(dd.get("also", ""))


def _def_label(d, key):
    """'N08#0' -> that candidate reading's text, shortened."""
    sid, _, k = key.rpartition("#")
    s = d.signs.get(sid)
    if s is None or not k.isdigit() or int(k) >= len(s.defs):
        return key
    return s.defs[int(k)]["text"]


def _select(d, positions):
    """The correlation engine: for every sign with several candidate
    readings choose the one that makes the column tell the most obvious
    story -- the 'correction matrix' that turns imagery into English.

    score(candidate) = sum over already-chosen neighbours of
        distance-decay * ( 2*shared imagery-words
                         + 3*learned matrix weight )
        with same-proverb-group neighbours weighted double;
    plus a weak whole-column prior. Anchors (single-reading signs) lock
    first; the most confident ambiguity resolves next, then becomes an
    anchor itself. Returns {position: def_index}."""
    cand = []
    token_support = defaultdict(int)
    evidence = d.evidence()
    for sid, _g in positions:
        s = d.signs.get(sid)
        ds = s.defs if s else []
        cand.append(list(range(len(ds))))
        sign_tokens = set()
        for dd in ds:
            sign_tokens |= _dtokens(dd)
        for tok in sign_tokens:
            token_support[tok] += 1

    chosen = {i: c[0] for i, c in enumerate(cand) if len(c) == 1}
    remaining = [i for i, c in enumerate(cand) if len(c) > 1]

    def key(i, di):
        return f"{positions[i][0]}#{di}"

    def corroborated(i, di):
        sid = positions[i][0]
        text = d.signs[sid].defs[di]["text"]
        return len(evidence.get(sid, {}).get(text, ())) >= 2

    n = len(positions)
    # EXPERIMENTAL priors -- derived from unverified field observations
    # (C3/C4/C8 in TestResults2.md). They are weak nudges only, never
    # rules: observations may be wrong, so these weights stay sub-decisive.
    OPENERS = ("proverb-opener", "actor", "place", "observe")
    CLOSERS = ("yield", "recover", "sustain", "rest", "transition")
    VERB_SITES = ("observe", "transition", "count", "action")
    ROLE_FILLERS = ("actor", "object", "place", "yield")

    def _is_verb(f):
        return f.startswith("act-") or f in VERB_SITES

    def score(i, di):
        s_i = d.signs[positions[i][0]]
        dd_i = s_i.defs[di]
        t = _dtokens(dd_i)
        f = dd_i.get("func", "")
        sc = 0.25 * sum(token_support[tok] > 1 for tok in t)
        if f == _guess_role(s_i):
            sc += 1.0       # depiction/category role prior
        if dd_i.get("mode") == "literal":
            sc += 0.25      # literal picture before generated fallbacks
        # Prefer concrete/specific hypotheses over generic multi-use filler
        # when scores are otherwise close; this keeps translations readable.
        if "may qualify, classify, or belong" in dd_i["text"]:
            sc -= 0.9
        elif "may name the result or consequence" in dd_i["text"]:
            sc -= 0.7
        elif dd_i.get("scope") == MULTIUSE_GUESS_SCOPE:
            sc -= 0.35
        elif dd_i.get("scope") == HISTORICAL_GUESS_SCOPE:
            sc += 0.15
        elif not dd_i.get("scope"):
            sc += 0.35
        if dd_i.get("local", {}).get("status") == LOCAL_CORROBORATED:
            sc += 0.75      # internally corroborated finding, not proof
        # C4 -- positional prior: openers lean early, closers lean late
        pos = i / (n - 1) if n > 1 else 0.5
        if pos <= 0.2 and f in OPENERS:
            sc += 2.0
        elif pos >= 0.8 and f in CLOSERS:
            sc += 2.0
        for j, dj in chosen.items():
            tj = _dtokens(d.signs[positions[j][0]].defs[dj])
            fj = d.signs[positions[j][0]].defs[dj].get("func", "")
            w = 1.0 / (abs(i - j) + 1)
            if positions[i][1] is not None and positions[i][1] == positions[j][1]:
                w *= 2.0                              # condensed-group bond
            matrix = (d.corr.get(key(i, di), key(j, dj))
                      if corroborated(i, di) and corroborated(j, dj) else 0)
            sc += w * (2.0 * len(t & tj) + 3.0 * matrix)
            # C8 -- slot grammar: verb-sites pull role-fillers toward them
            if _is_verb(fj) and f in ROLE_FILLERS:
                sc += w * 1.5
            if _is_verb(f) and fj in ROLE_FILLERS:
                sc += w * 1.5
            # C3 -- quantifier bond: count/tally marks lock onto the act
            # they quantify (strokes under the bird = the trips taken)
            if f == "count" and _is_verb(fj):
                sc += w * 2.0
            if fj == "count" and _is_verb(f):
                sc += w * 2.0
        return sc

    while remaining:
        best_i, best_di, best_margin = None, None, -1.0
        for i in remaining:
            scored = sorted(((score(i, di), di) for di in cand[i]),
                            key=lambda x: (-x[0], x[1]))
            margin = scored[0][0] - (scored[1][0] if len(scored) > 1 else 0)
            if margin > best_margin:
                best_i, best_di, best_margin = i, scored[0][1], margin
        chosen[best_i] = best_di
        remaining.remove(best_i)

    # refinement sweeps: re-score every ambiguity against the FINISHED
    # story -- a reading that looked wrong early may win once the whole
    # record is assembled (coordinate ascent on the full context)
    amb = [i for i, c in enumerate(cand) if len(c) > 1]
    for _sweep in range(2):
        moved = False
        for i in amb:
            best = max(cand[i], key=lambda di: score(i, di))
            if best != chosen[i] and score(i, best) > score(i, chosen[i]) + 0.3:
                chosen[i] = best
                moved = True
        if not moved:
            break

    # Grammar-balance pass: a picture-strip should not collapse into a list of
    # nouns when any candidate can carry the missing verb-like or noun-like
    # role. This only chooses among existing hypotheses; it is not evidence.
    def selected_is_verb(i):
        s = d.signs[positions[i][0]]
        dd = s.defs[chosen[i]]
        return (dd.get("reg") in ("verb", "adj+verb")
                or _is_verb(dd.get("func", "")))

    if not any(selected_is_verb(i) for i in chosen):
        best_i, best_di, best_gain = None, None, float("-inf")
        for i in amb:
            for di in cand[i]:
                dd = d.signs[positions[i][0]].defs[di]
                if not (dd.get("reg") in ("verb", "adj+verb")
                        or _is_verb(dd.get("func", ""))):
                    continue
                gain = score(i, di) - score(i, chosen[i])
                if gain > best_gain:
                    best_i, best_di, best_gain = i, di, gain
        if best_i is not None:
            chosen[best_i] = best_di

    # English-form refinement: keep the correlation winner when it already
    # forms a readable clause; otherwise try candidate alternatives that fill
    # subject/action/complement/closure slots without changing evidence.
    def selected_row():
        return [(positions[i][0], d.signs[positions[i][0]],
                 d.signs[positions[i][0]].defs[chosen[i]])
                for i in chosen]

    def slot_bonus(i, dd):
        f = dd.get("func", "")
        pos = i / (n - 1) if n > 1 else 0.5
        bonus = 0.0
        if pos <= 0.3 and f in ("actor", "proverb-opener", "object", "yield"):
            bonus += 1.5
        if 0.2 < pos < 0.75 and _is_strong_verb_dd(dd):
            bonus += 1.5
        if pos >= 0.55 and f in ("object", "place", "yield", "sustain",
                                  "recover", "rest"):
            bonus += 1.0
        if dd.get("scope") == MULTIUSE_GUESS_SCOPE:
            bonus -= 0.25
        return bonus

    def english_quality(i, di):
        old = chosen[i]
        chosen[i] = di
        profile = english_sequence_profile(selected_row())
        quality = profile["score"] * 4.0 + (8.0 if profile["readable"] else 0)
        quality += score(i, di) * 0.2 + slot_bonus(i,
                          d.signs[positions[i][0]].defs[di])
        chosen[i] = old
        return quality

    for _sweep in range(2):
        moved = False
        for i in amb:
            best = max(cand[i], key=lambda di: english_quality(i, di))
            if best != chosen[i] and (english_quality(i, best)
                                      > english_quality(i, chosen[i]) + 0.5):
                chosen[i] = best
                moved = True
        if not moved:
            break
    return chosen


def _cluster_pick(d, rec, grp, positions, chosen):
    """Choose a cluster's best whole-proverb reading for THIS column.
    A candidate scores on shared imagery-words with the signs inside the
    ring (x2) plus shared words with the rest of the column's chosen
    readings -- the evolved dialect means the same circle may honestly
    mean several different paragraphs; context decides."""
    mem_tok, col_tok = set(), set()
    grp_set = set(grp)
    for i, (sid, _g) in enumerate(positions):
        di = chosen.get(i, -1)
        s = d.signs.get(sid)
        if di < 0 or not s or not s.defined:
            continue
        (mem_tok if sid in grp_set else col_tok).update(
            _dtokens(s.defs[di]))
    best, best_sc = 0, -1.0
    for k, dd in enumerate(rec["defs"]):
        t = _dtokens(dd)
        sc = 2.0 * len(t & mem_tok) + 1.0 * len(t & col_tok)
        if dd.get("conf"):
            sc += 0.5                      # confirmed readings get a nudge
        if sc > best_sc:
            best, best_sc = k, sc
    return best


def sequence_effect_note(d, positions, chosen, i):
    """Explain why this occurrence of a sign received this reading.

    Candidate meanings are sequence variables, so every rendered entry names
    the pictures immediately around it, the role those neighbors pulled it
    toward, and a displaced alternative. Repeated signs are annotated per
    occurrence; identical candidates elsewhere are not new evidence."""
    sid = positions[i][0]
    s = d.signs.get(sid)
    if not s:
        return "unmapped mark keeps a literal placeholder"
    di = chosen.get(i, -1)
    if di < 0 or di >= len(s.defs):
        return "keeps its pictured-object placeholder; no use is selected"
    dd = s.defs[di]
    role = dd.get("func") or "context"

    def neighbor(j):
        if j < 0 or j >= len(positions):
            return None
        nsid = positions[j][0]
        ns = d.signs.get(nsid)
        ndi = chosen.get(j, -1)
        ndd = ns.defs[ndi] if ns and 0 <= ndi < len(ns.defs) else {}
        return (nsid, (ns.depicts if ns else nsid) or nsid,
                ndd.get("func", "?"), ndd)

    left, right = neighbor(i - 1), neighbor(i + 1)
    frame = "opening edge" if not left else ""
    frame += (f" {left[1]} <{left[2]}>" if left else "")
    frame += " + this +"
    frame += (f" {right[1]} <{right[2]}>" if right else " closing edge")

    t = _dtokens(dd)
    pulls = []
    if left:
        shared = sorted(t & _dtokens(left[3])) if left[3].get("text") else []
        if shared:
            pulls.append(f"left echoes {','.join(shared[:3])}")
        if _is_strong_verb_dd(left[3]) and _is_noun_dd(dd):
            pulls.append("left action makes it a complement")
        elif _is_strong_verb_dd(dd) and _is_noun_dd(left[3]):
            pulls.append("left picture supplies its actor/source")
        elif left[2] == role:
            pulls.append("left picture reinforces the same role")
    if right:
        shared = sorted(t & _dtokens(right[3])) if right[3].get("text") else []
        if shared:
            pulls.append(f"right echoes {','.join(shared[:3])}")
        if _is_strong_verb_dd(right[3]) and _is_noun_dd(dd):
            pulls.append("right action makes it a subject/complement")
        elif _is_strong_verb_dd(dd) and _is_noun_dd(right[3]):
            pulls.append("right picture receives the action")
        elif right[2] == role:
            pulls.append("right picture reinforces the same role")
    if not left:
        pulls.append("edge position marks the scene opening")
    if not right:
        pulls.append("edge position marks the scene closure")
    if not pulls:
        pulls.append("neighbor roles frame this slot")

    pair_labels = []
    signs = [x[0] for x in positions]
    for p, a, b, label, _stories, _basis in motif_matches(signs):
        if i == p - 1:
            pair_labels.append(f"left pair '{label}'")
        elif i == p:
            pair_labels.append(f"right pair '{label}'")
    if pair_labels:
        pulls.append(" + ".join(pair_labels[:2]))

    displaced = None
    for k, alt in enumerate(s.defs):
        if k != di and alt.get("func") != dd.get("func"):
            displaced = f"{alt.get('func', 'other')}: {alt['text']}"
            break
    if displaced is None and len(s.defs) > 1:
        alt = s.defs[0 if di else 1]
        displaced = alt["text"]
    displacement = f"; instead of {displaced[:62]}" if displaced else ""

    repeats = []
    for j, (other_sid, _g) in enumerate(positions):
        if j != i and other_sid == sid:
            odi = chosen.get(j, -1)
            odd = s.defs[odi] if 0 <= odi < len(s.defs) else {}
            repeats.append(f"#{j + 1}={odd.get('func', '?')}")
    repeat_note = (f"; same mark elsewhere {','.join(repeats)}"
                   if repeats else "")
    return (f"occurrence-specific use <{role}> in {frame}; "
            f"{'; '.join(pulls)}{displacement}{repeat_note}")


def read_column(d, entries, title="COLUMN", show=True):
    """Read a column top-to-bottom through the correlation engine.
    Returns the assembled story lines (chosen readings)."""
    positions = _positions(d, entries)
    chosen = _select(d, positions)
    evidence = d.evidence()
    # pre-scan condensed groups (the 'circled' clusters of the script) so a
    # known cluster can be read as ONE whole proverb, chengyu-style
    groups, cur = [], None
    for e in entries:
        if e == "[":
            cur = []
        elif e == "]":
            if cur is not None:
                groups.append(cur)
            cur = None
        elif cur is not None:
            cur.append(e)
    if cur is not None:
        groups.append(cur)          # an unclosed group still counts
    gi = 0
    pending_cluster = None
    out = []
    story = []
    in_group = False
    i = -1
    out.append(f"{AMBER}+{'-'*(W-2)}+{RESET}")
    out.append(f"{AMBER}|{title:^{W-4}} |{RESET}" if len(title) < W-4 else title)
    out.append(f"{AMBER}+{'-'*(W-2)}+{RESET}")
    for e_i, e in enumerate(entries):
        if e == "[":
            in_group = True
            grp = groups[gi] if gi < len(groups) else []
            gi += 1
            pending_cluster = d.cluster_for(grp)
            pending_di = 0
            if pending_cluster:
                pending_di = _cluster_pick(d, pending_cluster, grp,
                                           positions, chosen)
                dd = pending_cluster["defs"][pending_di]
                conf = dd.get("conf", "")
                ctag = f"  [{conf}]" if conf else ""
                mtag = f"  {{{dd['mode']}}}" if dd.get("mode") else ""
                out.append(f"{GOLD}   << CLUSTER -- reads as ONE proverb:{RESET}")
                if pending_cluster.get("depicts"):
                    out.append(f"{STONE}      (circles: {pending_cluster['depicts']}){RESET}")
                out.append(f"{GOLD}      {dd['text']}{ctag}{mtag}{RESET}")
                if dd.get("also"):
                    out.append(f"{GOLD}      ~ double: {dd['also']}{RESET}")
                if len(pending_cluster["defs"]) > 1:
                    alts = "; ".join(x["text"] for k, x in
                                     enumerate(pending_cluster["defs"])
                                     if k != pending_di)
                    out.append(f"      {STONE}cluster alts: {alts[:110]}{RESET}")
                tail_i = e_i + len(grp) + 1
                if tail_i < len(entries) and entries[tail_i] == "]":
                    tail_i += 1
                tail = entries[tail_i] if tail_i < len(entries) else None
                if tail and tail not in "[]":
                    ts = d.signs.get(tail)
                    nm = (ts.depicts or tail) if ts else tail
                    out.append(f"      {STONE}-> followed by {nm}: the marks "
                               f"beside a meme complete it{RESET}")
            else:
                out.append(f"{GOLD}   << PROVERB -- condensed group >>{RESET}")
            continue
        if e == "]":
            in_group = False
            if pending_cluster:
                dd = pending_cluster["defs"][pending_di]
                story.append(f"<< cluster: {dd['text']} >>")
                pending_cluster = None
            out.append(f"{GOLD}   << /PROVERB >>{RESET}")
            continue
        i += 1
        s = d.signs.get(e)
        mark = f"{i+1:>2}."
        tag = "PROVERB " if in_group else ""
        if s is None:
            out.append(f"{mark} {RED}<?> missing sign '{e}'{RESET}")
            story.append(f"[missing:{e}]")
            continue
        for ln in render_sign_lines(d, e):
            out.append(f"    {GOLD if in_group else ''}{ln}{RESET}")
        label = s.display()
        named = s.depicts or label     # the mark IS its depiction; usage
        di = chosen.get(i, -1)         # is what it's being used FOR here
        if s.defined and di >= 0:
            dd = s.defs[di]
            effect_note = sequence_effect_note(d, positions, chosen, i)
            # the fit-gate: a single-use mark only SPEAKS its usage when the
            # column calls for it. Otherwise it is simply what it depicts --
            # a bowl is a bowl until the marks around it make it more.
            applies = len(s.defs) > 1 or positions[i][1] is not None
            if not applies:
                t0 = _dtokens(dd)
                f0 = dd.get("func", "")
                FAMS = ({"proverb-opener", "place", "observe"},
                        {"yield", "recover", "sustain", "rest"},
                        {"act-travel", "act-visit", "transition",
                         "actor", "count", "object", "exchange"})
                for j, dj in chosen.items():
                    if j == i:
                        continue
                    dd_j = d.signs[positions[j][0]].defs[dj]
                    fj = dd_j.get("func", "")
                    applies = bool(_dtokens(dd_j) & t0) or \
                        (len(evidence.get(e, {}).get(dd["text"], ())) >= 2
                         and len(evidence.get(positions[j][0], {}).get(
                             dd_j["text"], ())) >= 2
                         and d.corr.get(f"{e}#{di}",
                                        f"{positions[j][0]}#{dj}") > 0) or \
                        any(f0 in fam and fj in fam for fam in FAMS)
                    if applies:
                        break
            if not applies:
                out.append(f"{mark} {tag}{CYAN}{named}{RESET}  "
                           f"{DIM}(as itself -- no call for "
                           f"'{dd['text'][:40]}' here){RESET}")
                out.append(f"      {STONE}NOTE: {effect_note}{RESET}")
                story.append(f"{named} (as itself)  NOTE: {effect_note}")
                continue
            conf = dd.get("conf", "")
            ctag = f"  {GOLD}[{conf}]{RESET}" if conf else ""
            mtag = (f"  {STONE}{{{dd['mode']}}}{RESET}"
                    if dd.get("mode") else "")
            ftag = (f"  {CYAN}<{dd['func']}>{RESET}"
                    if dd.get("func") else "")
            rtag = (f"  {DIM}({dd['reg']}){RESET}"
                    if dd.get("reg") else "")
            con = (f"  {STONE}[concrete]{RESET}"
                   if dd.get("concrete") else "")
            out.append(f"{mark} {tag}{CYAN}{named}{RESET}  := "
                       f"{dd['text']}{ctag}{mtag}{ftag}{rtag}{con}")
            out.append(f"      {STONE}NOTE: {effect_note}{RESET}")
            if dd.get("flex"):
                out.append(f"      {STONE}~flex: {dd['flex']}{RESET}")
            if dd.get("also"):
                out.append(f"      {GOLD}~ double: {dd['also']}{RESET}")
            if len(s.defs) > 1:
                alts = "; ".join(x["text"] for k, x in enumerate(s.defs)
                                 if k != di)
                out.append(f"      {STONE}alts: {alts[:110]}{RESET}")
            story.append(dd["text"]
                         + (f"  (also: {dd['also']})" if dd.get("also") else "")
                         + f"  NOTE: {effect_note}")
        else:
            out.append(f"{mark} {tag}{DIM}{named}  UNKNOWN  {STONE}(define it: define {e} ...){RESET}")
            story.append("[UNKNOWN -- not yet read]")
        if s.note:
            out.append(f"      {STONE}note: {s.note}{RESET}")
    out.append(f"{AMBER}+{'-'*(W-2)}+{RESET}")
    out.append("")
    # the strip's spine: the FUNCTION each mark performs in the record --
    # comic-strip logic; '?' where a mark is still unread
    roles = []
    for i, (sid, _g) in enumerate(positions):
        s = d.signs.get(sid)
        di = chosen.get(i, -1)
        roles.append(s.defs[di].get("func", "?")
                     if s and s.defined and di >= 0 else "?")
    out.append(f"{BOLD}THE STRIP (roles):{RESET}  "
               + f" {STONE}>{RESET} ".join(roles))
    out.append("")
    out.append(f"{BOLD}THE STORY (top -> down):{RESET}")
    joined = "\n".join(f"   {t}" for t in story)
    out.append(joined)
    text = "\n".join(out)
    if show:
        print(text)
    return story

def rosetta(d):
    bar("THE ROSETTA BASE COLUMN -- 'A DAY'S WORK'", "=")
    print(f"{STONE}ReferenceDialect/Rosetta.png -- one column, read top to bottom.{RESET}")
    print(f"{STONE}Three sections. The bird+strokes pair is a condensed proverb.{RESET}\n")
    for sec, (a, b, name) in ROSETTA_SECTIONS.items():
        print(f"{GOLD}-- section {sec}: {name} {'-'*(W-len(name)-16)}{RESET}")
        seg = _section_segment(d.rosetta_column, a, b)
        read_column(d, seg, title=f"section {sec}", show=True)
    bar("NATHAN'S READING OF THE WHOLE RECORD", "=")
    print(wrap(ROSETTA_STORY, "   "))
    print()

def page(d, names=None):
    """Read several columns LEFT TO RIGHT -- law 1 applied across a page.
    Each column is its own record: consumed top to bottom before the
    column to its right begins."""
    if not names:
        names = list(d.columns)
    for n, name in enumerate(names):
        col = d.columns.get(name)
        if col is None:
            print(f"no column '{name}' -- 'columns' lists them")
            continue
        print(f"{GOLD}COLUMN {n+1} of {len(names)} -- record '{name}' "
              f"(left -> right){RESET}")
        read_column(d, col, title=name)


def _section_segment(column, a, b):
    """Extract the column slice covering N(a)..N(b), keeping proverb brackets
    only when the whole condensed group falls inside the section."""
    ids = {f"N{n:02d}" for n in range(a, b + 1)}
    seg, i = [], 0
    while i < len(column):
        e = column[i]
        if e == "[":
            j = i + 1
            while j < len(column) and column[j] != "]":
                j += 1
            members = column[i + 1:j]
            inside = [m for m in members if m in ids]
            if inside and len(inside) == len(members):
                seg += ["["] + members + ["]"]
            else:
                seg += inside           # group straddles boundary -> demote
            i = j + 1
            continue
        if e != "]" and e in ids:
            seg.append(e)
        i += 1
    return seg

# ==============================================================================
# SECTION 5 -- CONSOLE
# ==============================================================================

HELP = """\
  laws                     the six reading laws
  dialects                 every documented stage of the Egyptian language
  rosetta                  the base column + the story it tells
  read [name]              read a column top-to-bottom (default: scratch)
  page [names]             read columns left->right, each its own record
  compose                  build a column: enter sign ids, '[' ']' groups, 'done'
  columns                  list saved columns
  keep <name>              save the scratch column under a name
  show <id>                a sign's card -- all candidate readings
  define <id> <meaning>    add a candidate reading (no arbitrary cap)
  prefer <id> <n>          promote reading #n to primary
  likely <id> <n>          flag reading #n 'highly likely'
  double <id> <n> <sense>  give reading #n a co-valid second sense (pun)
  undouble <id> <n>        remove the second sense
  depict <id> <image>      record what a mark literally depicts (the mask)
  mode <id> <n> <m>        tag reading #n: evolved|action|literal|-
  func <id> <n> <role>     tag reading #n's FUNCTION in the strip
  reg <id> <n> <regs>      tag reading #n's register: adj|verb|noun|adj+verb
  flex <id> <n> <note>     note how a reading flexes with terminology
  concrete <id> <n>        toggle a locked (unflexing) reading
  undefine <id> [n]        drop all readings, or just #n
  note <id> <text>         attach a working note
  teach [column]           endorse a reading -> reinforce the matrix
  matrix [id]              strongest learned correlations (or for a sign)
  guesses                  picture-story candidate reading (not a proof)
  motifs [column]          competing readings for adjacent glyph pairs
  sources                  external visual clues reviewed; no letter values
  history [word]           historical semantic candidates; not proof
  local [word]             internal correlation verification; not proof
  format                   proposed story-grammar coverage of pictured signs
  knowledge                staged progress toward verified language knowledge
  book                     coherence audit over every saved column
  story <file> [out]       read a glyph-only book file, optionally export
  translate <english.txt> <glyphs.txt> [report]  English bridge -> pictures
  cluster [sids] <meaning> a circled group's WHOLE-proverb reading (chengyu)
  uncluster <sids>         remove a cluster reading
  catalog [filter]         browse: all|unknown|defined|signs|marks|rosetta|<text>
  window                   open the scribe window (autocorrect writer)
  search <word>            find signs by meaning/note
  stats                    how much of the language is still UNKNOWN
  chart                    write egyptian_catalog.html -- the shaped xref sheet
  save | load              persist / reload your dialect json
  export                   write record + dictionary to egyptian_dialect.txt
  clear                    empty the scratch column
  help | quit
"""

LAWS = """\
  LAW 1   Read TOP TO BOTTOM inside a column; columns run LEFT TO RIGHT.
  LAW 2   Each column is its own record -- chapter, day, story. Self-contained.
  LAW 3   An out-of-place picture is a PROVERB: a self-explanatory concept.
  LAW 4   Circled/condensed signs = an emphatic proverb-group (a meme).
          Like Chinese chengyu, a cluster means a WHOLE paragraph -- the
          ring in reference3.png that wraps a set of marks is read as one
          concept, never broken back into parts.
  LAW 5   Scribble is expected; an unread sign stays UNKNOWN -- no borrowed
          decipherment or letter/number key. External material may help
          identify the pictured object or its visual variants only.
  LAW 6   Marks next to each other RELATE, whatever they are; a circled
          meme works the same -- what stands beside (and after) it
          completes its meaning.
"""

def sign_card(d, sid):
    s = d.signs.get(sid)
    if not s:
        print(f"no such sign: {sid}")
        return
    bar(f"sign {sid}")
    if s.sketch:
        for ln in s.sketch:
            print(f"    {ln}")
    if s.char:
        print(f"    char: {s.char}   (U+{ord(s.char):05X})")
    if s.cp is not None:
        print(f"    codepoint: U+{s.cp:05X}")
    if s.block:
        print(f"    block:   {s.block}")
    print(f"    kind:    {s.kind}")
    if s.depicts:
        tag = ("catalogue label" if (_NAMES or {}).get(s.sid) else
               ("family" if object_name(s.sid) else "unlabeled"))
        print(wrap(f"depicts: {s.depicts}  [{tag}] (pictured-object label, "
                   "not a translation)", "    "))
    status = (f"{CYAN}PROPOSED USES x{len(s.defs)}{RESET}" if s.defined
              else f"{RED}UNKNOWN{RESET}")
    print(f"    status:  {status}")
    if s.defs:
        print(f"    uses (what this mark is used FOR, in columns):")
    for k, dd in enumerate(s.defs):
        tag = "*" if k == 0 else " "
        conf = f"  {GOLD}[{dd['conf']}]{RESET}" if dd.get("conf") else ""
        mode = f"  {CYAN}{{{dd['mode']}}}{RESET}" if dd.get("mode") else ""
        func = f"  {CYAN}<{dd['func']}>{RESET}" if dd.get("func") else ""
        reg = f"  {DIM}({dd['reg']}){RESET}" if dd.get("reg") else ""
        con = f"  {STONE}[concrete]{RESET}" if dd.get("concrete") else ""
        print(wrap(f"{tag}#{k+1}: {dd['text']}", "    ")
              + conf + mode + func + reg + con)
        if dd.get("also"):
            print(wrap(f" ~also: {dd['also']}  (double meaning)", "    "))
        if dd.get("flex"):
            print(wrap(f" ~flex: {dd['flex']}", "    "))
        if dd.get("local"):
            local = dd["local"]
            print(wrap(f" ~local: {local['status']} score {local['score']}/8 "
                       f"({', '.join(local['checks'])})", "    "))
        if dd.get("src"):
            print(f"      {STONE}src: {dd['src']}{RESET}")
        witnesses = d.evidence().get(sid, {}).get(dd["text"], set())
        print(f"      independent column checks: {len(witnesses)}"
              f" / 2 minimum ({'cross-checked' if len(witnesses) >= 2 else 'provisional'})")
    if s.note:
        print(wrap(f"note:    {s.note}", "    "))
    if s.xref:
        print(f"    xref:    same shape as -> {', '.join(s.xref)}")
    if sid in VISUAL_SOURCE_LINKS:
        description, url = VISUAL_SOURCE_LINKS[sid]
        print(wrap(f"visual variants: {description} ({url}); "
                   "no meanings imported", "    "))
    bar()

def catalog(d, arg):
    items = list(d.signs.values())
    if arg == "defined":
        items = [s for s in items if s.defined]
    elif arg == "unknown":
        items = [s for s in items if not s.defined]
    elif arg in ("marks", "signs", "rosetta"):
        items = [s for s in items
                 if s.kind == ({"marks": "mark", "signs": "sign",
                                "rosetta": "rosetta"}[arg])]
    elif arg and arg != "all":
        q = arg.lower()
        items = [s for s in items if q in s.sid.lower()
                 or q in s.note.lower()
                 or q in (s.depicts or "").lower()
                 or any(q in dd["text"].lower()
                        or q in dd.get("also", "").lower()
                        for dd in s.defs)]
    print(f"{STONE}{len(items)} sign(s). ENTER pages, q stops.{RESET}")
    bar(f"{'shelf':<9} {'mark':<6} {'status':<8} meaning", "-")
    n = 0
    for s in items:
        mark = s.char or "drawn"
        st = (f"{CYAN}defx{len(s.defs)}{GOLD if any(dd.get('conf') for dd in s.defs) else ''}*{RESET}"
              if s.defined else f"{RED}UNKNOWN{RESET}")
        meaning = s.meaning if s.defined else ""
        if len(meaning) > 46:
            meaning = meaning[:43] + "..."
        print(f"{s.sid:<9} {mark:<6} {st:<8} {DIM}{meaning}{RESET}")
        n += 1
        if n % 40 == 0:
            try:
                if input(f"{STONE}-- more --{RESET}").strip().lower() == "q":
                    break
            except EOFError:
                break
    bar()

def stats(d):
    total, defined, unknown = d.stats()
    p = d.progress()
    pct = 100.0 * p["verified"] / p["total"] if p["total"] else 0
    bar("COVERAGE")
    print(f"  recorded marks in catalogue : {total:,}")
    print(f"  signs with proposed uses    : {defined:,}")
    print(f"  signs still UNKNOWN         : {unknown:,}")
    print(f"  proposed readings (not proof): {p['proposed']:,}")
    print(f"  guessed-use coverage        : "
          f"{100.0 * p['proposed'] / p['total'] if p['total'] else 0:.4f}% "
          "(0-100, proposals only)")
    print(f"  pictured Egyptian signs     : "
          f"{p['pictured_proposed']:,} / {p['pictured_total']:,} proposed "
          f"({100 * p['pictured_proposed'] / p['pictured_total'] if p['pictured_total'] else 0:.4f}%)")
    print(f"  correlation scaffolds       : "
          f"{p['pictured_auto']:,} pictured signs (shape/category/multi-use guesses)")
    print(f"  multi-use pictured signs    : "
          f"{p['pictured_multi']:,} / {p['pictured_total']:,} "
          "(4+ candidate uses)")
    print(f"  format-checked internally   : "
          f"{p['format_ready']:,} / {p['pictured_total']:,} "
          "(language logic only)")
    print(f"  pictured cross-checked      : "
          f"{p['pictured_verified']:,} / {p['pictured_total']:,}")
    local = local_verification(d)
    print(f"  locally corroborated        : "
          f"{local['verified_signs']:,} / {local['total']:,} "
          "(internal matrix/language agreement only)")
    book = book_coherence(d)
    print(f"  internally coherent columns : {book['coherent']:,} / "
          f"{book['unique']:,} saved")
    print(f"  literary-spine columns      : {book['literary']:,} / "
          f"{book['unique']:,} saved")
    guess_uses = sum(dd.get("conf") == CONF_GUESS
                     for s in d.signs.values() for dd in s.defs)
    print(f"  picture-first guess uses    : {guess_uses:,}")
    print(f"  observed in checked columns : {p['attested']:,}")
    print(f"  cross-checked in 2+ columns : {p['verified']:,} / {p['total']:,}")
    print(f"  multi-use signs observed    : {p['polysemous']:,}")
    print(f"  verified-use coverage       : {pct:.4f}% (0-100)")
    print("  This is catalogue coverage, NOT translation accuracy.")
    print("  Shape names, xrefs and machine selections are not verification.")
    repeated = sum(len(cols) >= 2 for cols in d.observed_pairs().values())
    print(f"  recurring adjacent glyph pairs: {repeated:,} (observations only)")
    by_block = {}
    for s in d.signs.values():
        by_block.setdefault(s.block or "other", [0, 0])
        by_block[s.block or "other"][0] += 1
        by_block[s.block or "other"][1] += 1 if s.defined else 0
    print(f"  {'block':<38}{'marks':>8}{'defined':>9}")
    for b, (n, df) in by_block.items():
        print(f"  {b:<38}{n:>8,}{df:>9,}")
    bar()

def language_format(d):
    """Check whether picture-sign hypotheses cover a story grammar."""
    pictured = [s for s in d.signs.values() if s.block in PICTURE_BLOCKS]
    roles = defaultdict(int)
    registers = defaultdict(int)
    ready = 0
    multiuse = 0
    for s in pictured:
        multiuse += (len(s.defs) >= 4 and
                     any(dd.get("scope") == MULTIUSE_GUESS_SCOPE
                         for dd in s.defs))
        for dd in s.defs:
            f, r, m = dd.get("func"), dd.get("reg"), dd.get("mode")
            if f:
                roles[f] += 1
            if r:
                registers[r] += 1
        ready += bool(s.defs) and all(
            dd.get("func") and dd.get("reg") and dd.get("mode")
            for dd in s.defs)
    required = ("actor", "place", "object", "action", "transition",
                "yield", "sustain", "recover", "observe", "count",
                "record", "rest")
    return {"total": len(pictured), "ready": ready, "multiuse": multiuse,
            "roles": dict(roles), "registers": dict(registers),
            "missing_roles": [r for r in required if not roles.get(r)]}

def format_report(d):
    """Explain the proposed strip grammar; this is a shape, not proof."""
    info = language_format(d)
    bar("PICTURE-LANGUAGE FORMAT (HYPOTHESIS SHAPE)")
    print(f"  format-verified signs : {info['ready']:,} / {info['total']:,} "
          "(internal only)")
    print(f"  multi-use variables   : {info['multiuse']:,} / {info['total']:,} "
          "(4+ labeled uses)")
    print("  required story roles  : "
          + (", ".join(info["missing_roles"]) or "all present"))
    print("  proposed spine        : actor/subject -> observe/action ->")
    print("                        object/yield -> place/transition ->")
    print("                        sustain/recover -> rest/closure")
    print("  role inventory (candidate uses, not evidence):")
    for role, n in sorted(info["roles"].items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"    {role:<14} {n:>6,}")
    print("  register inventory:")
    for reg, n in sorted(info["registers"].items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"    {reg:<14} {n:>6,}")
    print("  These tags make candidates comparable in context; they do not")
    print("  prove grammar, vocabulary, or a translation.")
    bar()

def knowledge_report(d):
    """Show the model's staged progress toward verified language knowledge."""
    p = d.progress()
    info = language_format(d)
    book = book_coherence(d)
    total = info["total"]
    verified = p["pictured_verified"]

    def pct(n):
        return 100.0 * n / total if total else 0.0

    internal_ready = min(p["pictured_proposed"], info["ready"],
                         info["multiuse"])
    bar("LANGUAGE KNOWLEDGE PROGRESS")
    print(f"  pictured signs proposed       : {p['pictured_proposed']:,}/{total:,} "
          f"({pct(p['pictured_proposed']):.4f}%)")
    print(f"  multi-use variables           : {info['multiuse']:,}/{total:,} "
          f"({pct(info['multiuse']):.4f}%)")
    print(f"  format-verified internally    : {info['ready']:,}/{total:,} "
          f"({pct(info['ready']):.4f}%)")
    print(f"  complete internal model       : {internal_ready:,}/{total:,} "
          f"({pct(internal_ready):.4f}%)")
    print(f"  internally coherent columns   : {book['coherent']:,}/{book['unique']:,}")
    print(f"  literary-spine columns        : {book['literary']:,}/{book['unique']:,}")
    local = local_verification(d)
    print(f"  locally corroborated signs    : "
          f"{local['verified_signs']:,}/{total:,} "
          f"({pct(local['verified_signs']):.4f}%)")
    print(f"  locally corroborated uses     : {len(local['verified']):,}")
    print(f"  externally verified knowledge : {verified:,}/{total:,} "
          f"({pct(verified):.4f}%)")
    print("  Internal verification means every pictured sign has candidate")
    print("  uses with language-format metadata. External verification still")
    print("  requires the same use to be manually attested in two distinct")
    print("  transcribed columns.")
    bar()

def book_coherence(d):
    """Audit every distinct saved column as a proposed literary record."""
    seen, rows = set(), []
    verbish = {"action", "observe", "transition", "rest", "exchange",
               "pause", "count", "record", "proverb-opener"}
    for name, entries in d.columns.items():
        fingerprint = tuple(entries)
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        positions = _positions(d, entries)
        missing = [sid for sid, _g in positions if sid not in d.signs]
        undefined = [sid for sid, _g in positions
                     if sid in d.signs and not d.signs[sid].defined]
        chosen = _select(d, positions)
        selected, untagged = [], 0
        for i, (sid, _g) in enumerate(positions):
            s = d.signs.get(sid)
            di = chosen.get(i, -1)
            if not s or di < 0 or di >= len(s.defs):
                continue
            dd = s.defs[di]
            selected.append(dd)
            untagged += not all(dd.get(k) for k in ("mode", "func", "reg"))
        multi_ready = all(
            d.signs[sid].block not in PICTURE_BLOCKS or
            (len(d.signs[sid].defs) >= 4 and
             any(dd.get("scope") == MULTIUSE_GUESS_SCOPE
                 for dd in d.signs[sid].defs))
            for sid, _g in positions if sid in d.signs)
        balanced = entries.count("[") == entries.count("]")
        readable = not missing and not undefined and balanced
        format_ok = multi_ready and not untagged
        coherent = readable and format_ok
        nouny = any(dd.get("reg") in ("noun", "adj") for dd in selected)
        verby = any(dd.get("reg") in ("verb", "adj+verb") or
                    dd.get("func") in verbish
                    for dd in selected)
        literary = coherent and nouny and verby and len(positions) >= 2
        roles = [dd.get("func", "?") for dd in selected]
        rows.append({"name": name, "entries": len(positions),
                     "missing": missing, "undefined": undefined,
                     "untagged": untagged, "balanced": balanced,
                     "readable": readable, "format_ok": format_ok,
                     "coherent": coherent, "literary": literary,
                     "motifs": len(motif_matches(entries)),
                     "roles": roles})
    return {"records": len(d.columns), "unique": len(rows), "rows": rows,
            "coherent": sum(r["coherent"] for r in rows),
            "literary": sum(r["literary"] for r in rows),
            "entries": sum(r["entries"] for r in rows)}

def book_report(d):
    """Report whether the saved corpus can render as one coherent book."""
    info = book_coherence(d)
    p = d.progress()
    bar("WHOLE-BOOK COHERENCE (INTERNAL ONLY)")
    print(f"  saved records              : {info['records']:,}")
    print(f"  distinct transcribed cols  : {info['unique']:,}")
    print(f"  entries read               : {info['entries']:,}")
    print(f"  internally coherent cols   : {info['coherent']:,}/{info['unique']:,} "
          f"({100 * info['coherent'] / info['unique'] if info['unique'] else 0:.4f}%)")
    print(f"  literary spine cols        : {info['literary']:,}/{info['unique']:,} "
          f"({100 * info['literary'] / info['unique'] if info['unique'] else 0:.4f}%)")
    for row in info["rows"]:
        status = ("literary" if row["literary"] else
                  "coherent" if row["coherent"] else "incomplete")
        print(f"    {row['name']:<16} {status:<10} entries={row['entries']:<3} "
              f"motifs={row['motifs']:<2} roles={' > '.join(row['roles'])[:42]}")
        if row["missing"] or row["undefined"] or row["untagged"]:
            print(f"      missing={row['missing'] or '-'} "
                  f"undefined={row['undefined'] or '-'} "
                  f"untagged={row['untagged']}")
    print(f"  externally verified signs   : {p['pictured_verified']:,}/"
          f"{p['pictured_total']:,} "
          f"({100 * p['pictured_verified'] / p['pictured_total'] if p['pictured_total'] else 0:.4f}%)")
    print("  This proves the current proposal model can render every saved")
    print("  transcription without gaps; it does not prove the historical")
    print("  wording. Photos are not OCRed, so untranscribed pages are not")
    print("  counted as books or evidence.")
    bar()

def _glyph_to_sid(d, token):
    """Map one glyph token or shelf mark to a canonical sign id."""
    if token in ("[", "]"):
        return token
    if token in d.signs:
        return token
    upper = token.upper()
    if upper in d.signs:
        return upper
    index = getattr(d, "_glyph_index", None)
    if index is None:
        index = {}
        for s in d.signs.values():
            if s.char:
                index.setdefault(s.char, []).append(s)
        for ch, matches in index.items():
            index[ch] = min(matches, key=lambda s: (
                s.kind == "rosetta",
                s.block != "Egyptian Hieroglyphs",
                s.sid)).sid
        d._glyph_index = index
    return index.get(token, token)


def parse_story_file(d, path):
    """Read a glyph-only book file.

    Blank lines separate pages. Within a page, whitespace-separated glyph
    characters and contiguous glyph runs are read top-to-bottom. '|', '¦'
    and '‖' may separate multiple columns on one page."""
    with open(path, encoding="utf-8") as f:
        raw_lines = f.read().splitlines()
    pages, page, col, unknown = [], [], [], []
    for raw in raw_lines:
        line = raw.strip()
        if not line:
            if col:
                page.append(col); col = []
            if page:
                pages.append(page); page = []
            continue
        for token in line.split():
            if token in ("|", "¦", "‖"):
                if col:
                    page.append(col); col = []
                continue
            sid = _glyph_to_sid(d, token)
            if sid != token or len(token) == 1:
                col.append(sid)
                continue
            # Support contiguous glyph strings such as 𓆛𓁹.
            if all(_glyph_to_sid(d, ch) in d.signs or ch in "[]"
                   for ch in token):
                col.extend(_glyph_to_sid(d, ch) for ch in token)
            else:
                col.append(token)
                unknown.append(token)
    if col:
        page.append(col)
    if page:
        pages.append(page)
    return {"pages": pages, "unknown": unknown,
            "columns": sum(len(p) for p in pages),
            "entries": sum(len(c) for p in pages for c in p)}


def story_audit(d, pages):
    """Measure internal coherence across parsed book pages/columns."""
    verbish = {"action", "observe", "transition", "rest", "exchange",
               "pause", "count", "record", "proverb-opener"}
    rows = []
    for pno, page in enumerate(pages, 1):
        for cno, entries in enumerate(page, 1):
            positions = _positions(d, entries)
            missing = [sid for sid, _g in positions if sid not in d.signs]
            undefined = [sid for sid, _g in positions
                         if sid in d.signs and not d.signs[sid].defined]
            chosen = _select(d, positions)
            selected, untagged = [], 0
            for i, (sid, _g) in enumerate(positions):
                s = d.signs.get(sid)
                di = chosen.get(i, -1)
                if not s or di < 0 or di >= len(s.defs):
                    continue
                dd = s.defs[di]
                selected.append((sid, s, dd))
                untagged += not all(dd.get(k)
                                    for k in ("mode", "func", "reg"))
            multi_ready = all(
                d.signs[sid].block not in PICTURE_BLOCKS or
                (len(d.signs[sid].defs) >= 4 and
                 any(dd.get("scope") == MULTIUSE_GUESS_SCOPE
                     for dd in d.signs[sid].defs))
                for sid, _g in positions if sid in d.signs)
            balanced = entries.count("[") == entries.count("]")
            readable = not missing and not undefined and balanced
            format_ok = multi_ready and not untagged
            coherent = readable and format_ok
            nouny = any(dd.get("reg") in ("noun", "adj")
                        for _sid, _s, dd in selected)
            verby = any(dd.get("reg") in ("verb", "adj+verb") or
                        dd.get("func") in verbish
                        for _sid, _s, dd in selected)
            rows.append({"page": pno, "column": cno, "entries": entries,
                         "positions": positions, "chosen": chosen,
                         "selected": selected, "missing": missing,
                         "undefined": undefined, "untagged": untagged,
                         "balanced": balanced, "readable": readable,
                         "format_ok": format_ok, "coherent": coherent,
                         "literary": coherent and nouny and verby and
                                     len(positions) >= 2,
                         "motifs": motif_matches(entries),
                         "roles": [dd.get("func", "?")
                                  for _sid, _s, dd in selected]})
    return {"rows": rows,
            "pages": len(pages),
            "columns": sum(len(p) for p in pages),
            "entries": sum(len(r["positions"]) for r in rows),
            "coherent": sum(r["coherent"] for r in rows),
            "literary": sum(r["literary"] for r in rows),
            "missing": sorted({m for r in rows for m in r["missing"]})}


def story_report(d, path, out_path=None):
    """Render a glyph-only book with proposed translations and explanations."""
    parsed = parse_story_file(d, path)
    audit = story_audit(d, parsed["pages"])
    seen = d.evidence()
    out = []
    out.append("=" * W)
    out.append("GLYPH BOOK -- PROPOSED PICTURE-STORY TRANSLATION")
    out.append("=" * W)
    out.append(f"source: {path}")
    out.append(f"pages: {audit['pages']:,}")
    out.append(f"columns: {audit['columns']:,}")
    out.append(f"glyph entries: {audit['entries']:,}")
    out.append(f"internally coherent columns: {audit['coherent']:,}/{audit['columns']:,}")
    out.append(f"literary-spine columns: {audit['literary']:,}/{audit['columns']:,}")
    out.append(f"unmapped glyphs: {len(audit['missing']):,}")
    if audit["missing"]:
        out.append("missing: " + ", ".join(audit["missing"]))
    out.append("All meanings below are labelled hypotheses; external verification")
    out.append("requires two independently transcribed column attestations.")
    out.append("")
    for row in audit["rows"]:
        title = f"PAGE {row['page']} / COLUMN {row['column']}"
        out.append("-" * W)
        out.append(title)
        out.append("-" * W)
        glyph_line = " ".join(
            e if e in "[]" else (d.signs[e].char or "?")
            if e in d.signs else "?" for e in row["entries"])
        out.append(f"glyphs: {glyph_line}")
        status = ("literary" if row["literary"] else
                  "coherent" if row["coherent"] else "incomplete")
        out.append(f"status: {status}; roles: {' > '.join(row['roles'])}")
        out.append("proposed story:")
        story = read_column(d, row["entries"], title=title, show=False)
        for i, item in enumerate(story, 1):
            out.append(f"  {i}. {item}")
        out.append("sign references:")
        pos = 0
        for i, e in enumerate(row["entries"], 1):
            if e in ("[", "]"):
                out.append(f"  {i:>2}. {e} condensed-group marker")
                continue
            pos += 1
            s = d.signs.get(e)
            if not s:
                out.append(f"  {pos:>2}. ? {e}: unmapped glyph")
                continue
            di = row["chosen"].get(pos - 1, -1)
            if di < 0 or di >= len(s.defs):
                out.append(f"  {pos:>2}. {s.char or '?'} {e}: {s.depicts or 'unidentified'} -- undefined")
                continue
            dd = s.defs[di]
            witnesses = len(seen.get(e, {}).get(dd["text"], ()))
            out.append(f"  {pos:>2}. {s.char or '?'} {e}")
            out.append(f"       literal depiction: {s.depicts or 'unidentified pictured mark'}")
            out.append(f"       chosen use      : {dd['text']}")
            out.append(f"       labels          : {dd.get('conf', 'proposal')}/"
                       f"{dd.get('mode', 'contextual')}/"
                       f"{dd.get('func', 'unassigned')}/"
                       f"{dd.get('reg', 'untagged')}")
            out.append(f"       source          : {dd.get('src', 'unspecified')}")
            out.append(f"       sequence effect : {sequence_effect_note(d, row['positions'], row['chosen'], pos - 1)}")
            out.append(f"       evidence        : {witnesses}/2 independent column witnesses")
            if dd.get("flex"):
                out.append(f"       flexibility     : {dd['flex']}")
            if dd.get("also"):
                out.append(f"       double sense    : {dd['also']}")
            alts = [x["text"] for k, x in enumerate(s.defs) if k != di]
            if alts:
                out.append("       alternatives    :")
                for alt in alts:
                    out.append(f"         - {alt}")
        if row["motifs"]:
            out.append("adjacent-picture motifs:")
            for _pos, a, b, label, stories, basis in row["motifs"]:
                out.append(f"  {a}+{b} [{label}]")
                out.append(f"    A: {stories[0]}")
                out.append(f"    B: {stories[1]}")
                out.append(f"    basis: {basis}")
        out.append("")
    text = "\n".join(out)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"written: {out_path}")
        print(f"pages={audit['pages']:,} columns={audit['columns']:,} "
              f"entries={audit['entries']:,} coherent={audit['coherent']:,}/"
              f"{audit['columns']:,} literary={audit['literary']:,}/{audit['columns']:,}")
    else:
        print(text)
    return audit


TRANSLATE_WORDS = {
    "fish": "K001", "water": "N035", "river": "N035", "eye": "D004",
    "see": "D004", "look": "D004", "watch": "D004", "sun": "N005",
    "day": "N005", "walk": "D055", "go": "D055", "move": "D055",
    "travel": "D055", "return": "D055", "goose": "G038", "bird": "G038",
    "boat": "P001", "sail": "P002", "shore": "N020", "bank": "N020",
    "bread": "X002", "food": "X002", "basket": "V030", "jar": "W015",
    "vessel": "W015", "tree": "M001", "house": "O001", "home": "O001",
    "star": "N015", "night": "N015", "rest": "A056", "sleep": "A056",
    "lie": "A056", "man": "A001", "person": "A001", "child": "A017",
    "net": "T024", "gather": "V030", "carry": "V030", "work": "D055",
}
TRANSLATE_SYNTAX = set(("a an the and or of to in on at for with from by is are "
    "was were be been as it its his her their our your my i you he she we they "
    "this that these those do does did not no yes can could will would should "
    "may might must had have has then than so but if when while where who whom "
    "whose which what into out up down over under after before again").split())


def _english_root(word):
    """Very small English bridge normalizer -- never pretends to be NLP."""
    if word in TRANSLATE_WORDS:
        return word
    if word.endswith("ies") and len(word) > 4:
        root = word[:-3] + "y"
        if root in TRANSLATE_WORDS:
            return root
    for suffix in ("ing", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            root = word[:-len(suffix)]
            if root in TRANSLATE_WORDS:
                return root
    return word


def _english_sign(d, word):
    """Choose a pictured sign for an English token, with honest no-match."""
    sid = TRANSLATE_WORDS.get(_english_root(word))
    if sid in d.signs:
        return sid, "core bridge glossary"
    for score, s in suggest(d, word, 8):
        if s.char and s.block in PICTURE_BLOCKS and score >= 0.74:
            return s.sid, f"autocorrect score {score:.2f}"
    return None, "unmapped"


def english_to_egyptian(d, text):
    """Render English as a proposal glyph book and retain every source token."""
    sentences = [x.strip() for x in re.split(r"(?<=[.!?])\s+|\n+",
                                             text.strip()) if x.strip()]
    sentences = sentences or [text.strip()]
    pages, mappings = [], []
    for sn, sentence in enumerate(sentences, 1):
        entries = []
        toks = re.findall(r"\w+(?:[’'-]\w+)*|[^\w\s]", sentence, re.UNICODE)
        for tok in toks:
            low = tok.lower().replace("’", "'")
            if re.fullmatch(r"[^\w\s]", tok) or low in TRANSLATE_SYNTAX:
                mappings.append({"sentence": sn, "token": tok,
                                 "action": "syntax", "sid": None,
                                 "glyph": "", "meaning": "grammar/context"})
                continue
            sid, why = _english_sign(d, low)
            s = d.signs.get(sid) if sid else None
            mappings.append({"sentence": sn, "token": tok,
                             "action": "mapped" if s else "unmapped",
                             "sid": sid, "glyph": s.char if s else "",
                             "depicts": s.depicts if s else "",
                             "meaning": (s.defs[0]["text"]
                                          if s and s.defs else ""),
                             "source": why})
            if s:
                entries.append(sid)
        pages.append(entries)
    return {"pages": pages, "mappings": mappings,
            "sentences": sentences,
            "mapped": sum(m["action"] == "mapped" for m in mappings),
            "unmapped": sum(m["action"] == "unmapped" for m in mappings),
            "syntax": sum(m["action"] == "syntax" for m in mappings)}


def translate_report(d, path, glyph_path, report_path=None):
    """Translate an English bridge file to glyphs and prove token retention."""
    with open(path, encoding="utf-8") as f:
        source = f.read()
    tx = english_to_egyptian(d, source)
    glyph_lines = [" ".join(d.signs[sid].char or sid for sid in page)
                   for page in tx["pages"]]
    with open(glyph_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(glyph_lines) + "\n")
    content = tx["mapped"] + tx["unmapped"]
    lines = ["=" * W,
             "ENGLISH-BRIDGE TO EGYPTIAN PICTURE BOOK",
             "=" * W,
             f"source: {path}",
             f"glyph book: {glyph_path}",
             f"sentences/pages: {len(tx['pages']):,}",
             f"mapped content tokens: {tx['mapped']:,}/{content:,}",
             f"syntax/context tokens retained: {tx['syntax']:,}",
             f"unmapped content tokens retained: {tx['unmapped']:,}",
             "source-token retention: 100.0000% (every token is listed below)",
             "semantic equivalence is NOT guaranteed; unmapped items need definitions.",
             ""]
    for m in tx["mappings"]:
        detail = m.get("depicts") or m.get("meaning") or ""
        lines.append(f"  {m['sentence']:>4}  {m['token']:<24} {m['action']:<8} "
                     f"{m.get('sid') or '-':<9} {m.get('glyph') or '-':<3} "
                     f"{m.get('source', detail)} {detail}".rstrip())
    text_out = "\n".join(lines) + "\n"
    if report_path:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(text_out)
        print(f"written: {glyph_path}")
        print(f"written: {report_path}")
        print(f"mapped={tx['mapped']:,}/{content:,} syntax={tx['syntax']:,} "
              f"unmapped-retained={tx['unmapped']:,} source-retention=100%")
    else:
        print(text_out)
    return tx


# ==============================================================================
# SECTION 5a -- SUPERVISED IMAGE TRANSCRIPTION
# ==============================================================================
# Shape matching is a research assistant, not OCR evidence. Every match starts
# as a candidate; a human must pick it and approve the column, and only a
# separate attest command can turn it into an evidence witness.

TRANSCRIPTION_CANDIDATE = "candidate"
TRANSCRIPTION_REVIEWED = "human-reviewed"
TRANSCRIPTION_REJECTED = "rejected"
_TILE_FEATURES = None


def _photo_ink(img):
    """Return a boolean ink mask for a photograph/PIL image."""
    import cv2
    import numpy as np
    from PIL import Image
    if isinstance(img, Image.Image):
        rgb = np.asarray(img.convert("RGB"))
    else:
        rgb = np.asarray(img)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    gray = cv2.bilateralFilter(gray, 5, 25, 25)
    dark = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 31, 10) > 0
    dark = cv2.morphologyEx(dark.astype(np.uint8), cv2.MORPH_OPEN,
                            np.ones((2, 2), np.uint8)) > 0
    return dark


def _norm_ink(mask, size=96, fill=78):
    """Normalize an ink mask by bounding box into a fixed square."""
    import cv2
    import numpy as np
    ys, xs = np.where(mask)
    out = np.zeros((size, size), bool)
    if not xs.size:
        return out
    x0, x1 = xs.min(), xs.max() + 1
    y0, y1 = ys.min(), ys.max() + 1
    crop = mask[y0:y1, x0:x1]
    h, w = crop.shape
    scale = (fill - 4) / max(h, w)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    crop = cv2.resize(crop.astype(np.uint8), (nw, nh),
                      interpolation=cv2.INTER_NEAREST) > 0
    y = (size - nh) // 2
    x = (size - nw) // 2
    out[y:y + nh, x:x + nw] = crop
    return out


def _hu_vector(mask):
    """Scale/translation invariant Hu descriptor, log-normalized."""
    import cv2
    import numpy as np
    hu = cv2.HuMoments(cv2.moments(mask.astype(np.uint8))).ravel()
    return np.array([-np.sign(v) * np.log10(abs(v) + 1e-30)
                     for v in hu[:5]])


def _tile_features(d):
    """Lazily cache normalized tile masks and rough descriptors."""
    global _TILE_FEATURES
    if _TILE_FEATURES is not None:
        return _TILE_FEATURES
    import numpy as np
    from PIL import Image
    feats = []
    for s in d.signs.values():
        fp = os.path.join(TILE_DIR, s.sid + ".png")
        if not os.path.exists(fp):
            continue
        a = np.asarray(Image.open(fp).convert("RGBA"))[:, :, 3] > 64
        ys, xs = np.where(a)
        if not xs.size:
            continue
        bw = xs.max() - xs.min() + 1
        bh = ys.max() - ys.min() + 1
        bbox = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        feats.append({
            "sid": s.sid, "mask": _norm_ink(a),
            "aspect": bw / bh, "density": bbox.mean(),
            "hu": _hu_vector(bbox)})
    _TILE_FEATURES = feats
    return feats


def _match_ink(d, ink, top_n=5):
    """Rank a photo ink mask against every tile; returns shape candidates."""
    import cv2
    import numpy as np
    ys, xs = np.where(ink)
    if xs.size < 4:
        return []
    bw, bh = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
    aspect, density = bw / bh, ink[ys.min():ys.max() + 1,
                                   xs.min():xs.max() + 1].mean()
    hu = _hu_vector(ink)
    rough = []
    for i, f in enumerate(_tile_features(d)):
        desc = (abs(np.log(max(aspect, .01) / max(f["aspect"], .01))) * 1.8
                + abs(density - f["density"]) * 1.3
                + np.linalg.norm(hu - f["hu"]) * .13)
        rough.append((desc, i))
    probe = _norm_ink(ink)
    probe_f = probe.astype(np.float32)
    probe_inv = cv2.distanceTransform((~probe).astype(np.uint8),
                                      cv2.DIST_L2, 3)
    scored = []
    for _desc, i in sorted(rough, key=lambda x: x[0])[:400]:
        f = _tile_features(d)[i]
        tm = f["mask"]
        dice = 2.0 * np.logical_and(probe, tm).sum() / \
            max(1, probe.sum() + tm.sum())
        inv = cv2.distanceTransform((~tm).astype(np.uint8),
                                    cv2.DIST_L2, 3)
        chamfer = ((probe_inv[tm].mean() if tm.any() else 96)
                   + (inv[probe].mean() if probe.any() else 96)) / 2
        shape = np.exp(-chamfer / 8.0)
        score = dice * .62 + shape * .38
        scored.append((score, f["sid"], dice, chamfer))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [{"sid": sid, "similarity": float(round(sc * 100, 1)),
             "dice": float(round(di * 100, 1)),
             "chamfer": float(round(ch, 2)),
             "depicts": d.signs[sid].depicts or "",
             "status": TRANSCRIPTION_CANDIDATE}
            for sc, sid, di, ch in scored[:top_n]]


def _vertical_columns(ink):
    """Split a page into likely glyph columns using full-height dividers."""
    import cv2
    import numpy as np
    h, w = ink.shape
    vertical = cv2.morphologyEx(
        ink.astype(np.uint8), cv2.MORPH_OPEN,
        np.ones((max(18, h // 4), 1), np.uint8)) > 0
    score = vertical.mean(axis=0)
    runs, start = [], None
    for x, on in enumerate(score > .18):
        if on and start is None:
            start = x
        elif not on and start is not None:
            runs.append((start, x - 1)); start = None
    if start is not None:
        runs.append((start, w - 1))
    seps = [(a + b) // 2 for a, b in runs if b - a <= max(8, w // 25)]
    if len(seps) >= 2:
        spans = [(seps[i] + 2, seps[i + 1] - 2)
                 for i in range(len(seps) - 1)]
        return [(a, 0, b, h) for a, b in spans if b - a >= 24]
    if len(seps) == 1:
        left, right = ink[:, :seps[0]].mean(), ink[:, seps[0] + 1:].mean()
        return [(2, 0, seps[0] - 2, h)] if left > right else \
               [(seps[0] + 2, 0, w - 2, h)]
    return [(0, 0, w, h)]


def _row_cells(ink, x0, x1, y0=0, y1=None):
    """Find ink bands within one vertical column."""
    import cv2
    import numpy as np
    h, w = ink.shape
    y1 = h if y1 is None else y1
    crop = ink[y0:y1, x0:x1].copy()
    if crop.size == 0:
        return []
    # Remove long divider remnants and connect tiny fragments inside a mark.
    for yy in (0, crop.shape[0] - 1):
        crop[yy] = 0
    for xx in range(min(3, crop.shape[1])):
        crop[:, xx] = 0
        crop[:, crop.shape[1] - xx - 1] = 0
    vertical = cv2.morphologyEx(
        crop.astype(np.uint8), cv2.MORPH_OPEN,
        np.ones((max(12, crop.shape[0] // 3), 1), np.uint8)) > 0
    crop[vertical] = 0
    closed = cv2.morphologyEx(crop.astype(np.uint8), cv2.MORPH_CLOSE,
                              np.ones((5, 5), np.uint8)) > 0
    score = closed.mean(axis=1)
    runs, start = [], None
    for y, on in enumerate(score > .001):
        if on and start is None:
            start = y
        elif not on and start is not None:
            runs.append((start, y - 1)); start = None
    if start is not None:
        runs.append((start, crop.shape[0] - 1))
    merged = []
    for a, b in runs:
        if merged and a - merged[-1][1] <= 3:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    cells = []
    for a, b in merged:
        if b - a + 1 < 7:
            continue
        sub = crop[max(0, a - 2):min(crop.shape[0], b + 3)]
        if sub.mean() < .002:
            continue
        cells.append((x0, y0 + max(0, a - 2),
                      x1, y0 + min(crop.shape[0], b + 3), sub.copy()))
    return cells


def _manual_cells(path):
    """Read x0,y0,x1,y1 rows from a text/JSON cell list."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    try:
        data = json.loads(raw)
        rows = data.get("cells", data) if isinstance(data, dict) else data
        return [tuple(map(int, row)) for row in rows]
    except (TypeError, ValueError, AttributeError):
        pass
    cells = []
    for line in raw.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        vals = [int(x) for x in re.split(r"[\s,]+", line) if x]
        if len(vals) != 4:
            raise ValueError(f"cell row needs x0,y0,x1,y1: {line}")
        cells.append(tuple(vals))
    return cells


def transcribe_image(d, path, transcription_id=None, top_n=6,
                     manual_cells=None):
    """Scan an image into candidate cell matches for human review.

    This deliberately does not save a column or create evidence. The result is
    a review record containing bounding boxes and ranked visual candidates.
    ``manual_cells`` supplies exact x0,y0,x1,y1 regions when automatic
    segmentation is too coarse for the source image."""
    import datetime
    from PIL import Image
    import cv2
    import numpy as np
    img = Image.open(path).convert("RGB")
    ink = _photo_ink(img)
    columns = []
    index = 0
    if manual_cells is not None:
        entries = []
        for bx0, by0, bx1, by1 in manual_cells:
            index += 1
            sub = ink[by0:by1 + 1, bx0:bx1 + 1]
            matches = _match_ink(d, sub, top_n)
            entries.append({"index": index,
                            "bbox": [int(bx0), int(by0),
                                     int(bx1), int(by1)],
                            "matches": matches,
                            "reviewed_sid": None,
                            "status": TRANSCRIPTION_CANDIDATE})
        if entries:
            columns.append({"number": 1, "entries": entries})
    else:
        for cno, (x0, y0, x1, y1) in enumerate(_vertical_columns(ink), 1):
            cells = []
            for bx0, by0, bx1, by1, sub in _row_cells(ink, x0, x1, y0, y1):
                index += 1
                matches = _match_ink(d, sub, top_n)
                cells.append({"index": index,
                              "bbox": [int(bx0), int(by0),
                                       int(bx1), int(by1)],
                              "matches": matches,
                              "reviewed_sid": None,
                              "status": TRANSCRIPTION_CANDIDATE})
            if cells:
                columns.append({"number": cno, "entries": cells})
    rec = {"id": transcription_id or os.path.splitext(
                os.path.basename(path))[0],
           "source": os.path.basename(path), "path": os.path.abspath(path),
           "created": datetime.datetime.now().isoformat(timespec="seconds"),
           "status": TRANSCRIPTION_CANDIDATE,
           "cell_source": "manual-bbox" if manual_cells is not None else "auto-segment",
           "warning": ("machine shape-match proposals only; approve and "
                       "attest separately before treating as evidence"),
           "columns": columns}
    d.transcriptions[rec["id"]] = rec
    return rec


def write_transcription_review(rec, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2, ensure_ascii=False)
    return path


def transcription_report(d, tid=None):
    """Print pending image transcription review candidates."""
    if tid is not None and tid not in d.transcriptions:
        print(f"no transcription '{tid}'")
        return
    recs = ([d.transcriptions[tid]] if tid is not None
            else list(d.transcriptions.values()))
    if not recs:
        print("no transcription reviews -- run: transcribe <image> <id>")
        return
    bar("IMAGE TRANSCRIPTION REVIEW (CANDIDATES ONLY)")
    for rec in recs:
        print(f"  {rec['id']}  {rec['status']}  source={rec['source']}  "
              f"columns={len(rec['columns'])}")
        for col in rec["columns"]:
            print(f"    column {col['number']}:")
            for cell in col["entries"]:
                picks = " | ".join(
                    f"#{i+1} {m['sid']} {m['similarity']}% {m['depicts']}"
                    for i, m in enumerate(cell["matches"][:4])) or "no match"
                print(f"      cell {cell['index']:>3}: {picks} "
                      f"reviewed={cell.get('reviewed_sid') or '-'}")
    print("  pick <id> <cell#> <n|sid>; approve <id> <column-name> [column#].")
    bar()


def pick_transcription(d, tid, cell_index, choice):
    rec = d.transcriptions.get(tid)
    if not rec:
        return f"no transcription '{tid}'"
    for col in rec["columns"]:
        for cell in col["entries"]:
            if cell["index"] != cell_index:
                continue
            sid = None
            try:
                sid = cell["matches"][int(choice) - 1]["sid"]
            except (ValueError, IndexError):
                raw = choice.upper()
                if raw in d.signs:
                    sid = raw
            if sid is None or sid not in d.signs:
                return f"cell {cell_index}: no candidate '{choice}'"
            cell["reviewed_sid"] = sid
            cell["status"] = TRANSCRIPTION_REVIEWED
            return f"{tid} cell {cell_index} -> {sid} (human reviewed)"
    return f"{tid} has no cell {cell_index}"


def approve_transcription(d, tid, column_name, column_number=None):
    """Human approval creates a saved column; it still creates no evidence."""
    rec = d.transcriptions.get(tid)
    if not rec:
        return f"no transcription '{tid}'"
    if rec.get("status") == TRANSCRIPTION_REJECTED:
        return f"transcription '{tid}' was rejected"
    if column_number is None:
        if len(rec["columns"]) != 1:
            return ("approve needs a column number: "
                    f"{','.join(str(c['number']) for c in rec['columns'])}")
        col = rec["columns"][0]
    else:
        col = next((c for c in rec["columns"]
                    if c["number"] == column_number), None)
        if col is None:
            return f"{tid} has no column {column_number}"
    missing = [c["index"] for c in col["entries"]
               if not c.get("reviewed_sid")]
    if missing:
        return (f"review {len(missing)} cell(s) first: "
                + ",".join(map(str, missing[:12])))
    entries = [c["reviewed_sid"] for c in col["entries"]]
    d.columns[column_name] = entries
    rec.setdefault("approved_columns", {})[column_name] = col["number"]
    if all(any(cell.get("reviewed_sid") for cell in c["entries"])
           for c in rec["columns"]):
        rec["status"] = TRANSCRIPTION_REVIEWED
    return (f"approved '{tid}' column {col['number']} as '{column_name}' -- "
            "candidate transcription, still needs separate attest")


def reject_transcription(d, tid):
    rec = d.transcriptions.get(tid)
    if not rec:
        return f"no transcription '{tid}'"
    rec["status"] = TRANSCRIPTION_REJECTED
    return f"transcription '{tid}' rejected"


def guesses_report(d):
    """Show results without converting a suggested story into evidence."""
    bar("PICTURE-STORY GUESSES (NOT VERIFIED)")
    print("  Shape = pictured object; use = one possible meaning in context.")
    p = d.progress()
    print(f"  Proposal coverage: {p['pictured_proposed']:,}/"
          f"{p['pictured_total']:,} pictured signs; "
          f"{p['pictured_auto']:,} are catalogue-coverage scaffolds.")
    print("  Scaffolds use depiction/category/adjacency prompts only -- never proof.")
    print("  The annotated Rosetta column, also in Reference1, is ONE example.")
    story = read_column(d, d.rosetta_column, show=False)
    for i, item in enumerate(story, 1):
        print(wrap(f"  {i:>2}. {item}", width=W))
    print("\n  Unresolved alternatives:")
    for sid in ("N05", "N06", "N08", "N09", "N12", "N13"):
        s = d.signs[sid]
        print(f"    {sid} ({s.depicts}):")
        for dd in s.defs:
            print(wrap(f"      [{dd.get('conf', 'proposal')}] "
                       f"{dd.get('mode', 'contextual')}"
                       f" <{dd.get('func', 'unassigned')}>"
                       f" ({dd.get('reg', 'untagged')}): {dd['text']}",
                       width=W))
    print("\n  Alternate picture-story (N05/N12/N13 differ):")
    print(wrap("    A person notices fish near water, attends to a task at the "
               "shore, and carries a coiled item or harvest. A break or "
               "opening divides the action. The bird over strokes might "
               "depict journeys, or a real bird with a count. Goods are "
               "gathered, put in a small container, and the next line "
               "divides the scene; shade and rest close it. A sale and "
               "even a fishing trip are not required by these pictures.",
               width=W))
    print("\n  Further pictured sequences to test (not full transcriptions):")
    print(wrap("    Reference1 col 8 / p6_col8_structure.png: bird beside "
               "short strokes, a dividing line, then a loop-like mark and "
               "uprights, with more birds and eye-like marks below. Guess: "
               "a departure, pause, encounter or return, then observation. "
               "Alternative: actual birds and counted objects in a scene.",
               width=W))
    print(wrap("    p7_spot_later_same_place.png: dots and line reappear. "
               "Guess: the same location resumed after a break. "
               "Alternative: an amount or time marker repeated.",
               width=W))
    print("  Candidate story only; catalogue guesses are not image transcriptions.")
    bar()

def audit(d, sid=None):
    """Inspect all proposed senses and their independent corroboration."""
    p = d.progress()
    stats(d)
    seen = d.evidence()
    if sid:
        sign_card(d, sid)
        if sid in d.signs:
            occurrences = [name for name, entries in d.columns.items()
                           if sid in entries]
            print(f"  transcribed columns: {', '.join(occurrences) or 'none'}")
            for pair, cols in sorted(d.observed_pairs().items()):
                if sid in pair:
                    print(f"  observed {pair}: {len(cols)} distinct columns")
    else:
        print("  Proposed uses (each needs independent checks):")
        for sign in d.signs.values():
            if not sign.defs:
                continue
            for i, dd in enumerate(sign.defs, 1):
                witnesses = seen.get(sign.sid, {}).get(dd["text"], set())
                label = dd.get("conf", "proposal")
                mode = dd.get("mode", "contextual")
                print(f"    {sign.sid} #{i} [{label}/{mode}]: {dd['text'][:60]} "
                      f"[{len(witnesses)} independent columns]")
        print(f"  {p['total'] - p['proposed']:,} other glyphs have no proposed use.")

def chart(d, path=None):
    """Write egyptian_catalog.html -- the cross-reference sheet.

    Every recorded mark rendered in its canonical carved shape (hieroglyph
    font stack), each cell labelled with shelf mark + codepoint + status.
    This is the document you hold a photographed glyph up against."""
    import datetime
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "egyptian_catalog.html")

    def cell(s):
        cls = "def" if s.defined else ("mark" if s.kind == "mark" else "unk")
        cp = f"U+{s.cp:05X}" if s.cp is not None else "drawn"
        all_defs = " | ".join(
            dd["text"] + (f" ~ {dd['also']}" if dd.get("also") else "")
            + (f"  [{dd['conf']}]" if dd.get("conf") else "")
            for dd in s.defs)
        tip = html.escape((all_defs + (" -- " + s.note if s.note else ""))
                          .strip(), quote=True)
        tile = os.path.join("glyphs", s.sid + ".png")
        art = (f'<img class="glyph" src="{tile}" alt="{s.sid}" '
               f'onerror="this.outerHTML=\'<div class=glyph>'
               f'{html.escape(s.char or chr(0x25A1))}</div>\'">')
        xrefs = f'<div class="xr">=&gt; {html.escape(",".join(s.xref))}</div>' \
                if s.xref else ""
        q = html.escape(f"{s.sid} {all_defs} {s.note} {s.depicts or ''} {cp}"
                        .lower())
        nmean = s.meaning + (f" (+{len(s.defs)-1} more)" if len(s.defs) > 1 else "")
        depline = (f'<div class="cp">depicts: {html.escape(s.depicts)}</div>'
                   if s.depicts else "")
        return (f'<div class="cell {cls}" data-q="{q}" title="{tip}">'
                f'{art}<div class="sid">{s.sid}</div>'
                f'<div class="cp">{cp}</div>{depline}'
                f'<div class="mean">{html.escape(nmean[:64])}</div>{xrefs}</div>')

    order = ["Rosetta base column", "Egyptian Hieroglyphs",
             "Hieroglyph Format Controls", "Egyptian Hieroglyphs Extended-A"]
    groups = {b: [] for b in order}
    for s in d.signs.values():
        groups.setdefault(s.block or "other", []).append(s)

    total, defined, unknown = d.stats()
    parts = ["""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>THE FRESH DIALECT -- cross-reference catalogue</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Egyptian+Hieroglyphs&display=swap" rel="stylesheet">
<style>
 body{background:#1a150e;color:#d8c9a3;font-family:Georgia,serif;margin:24px}
 h1{color:#e8b84b;font-size:22px} h2{color:#c99b3f;border-bottom:1px solid #5a4a2a;
 padding-top:22px}
 .meta{color:#8a7a55;font-size:13px}
 #q{font-size:16px;padding:6px;width:340px;background:#2a2118;color:#e8d9b0;
 border:1px solid #6a5a35}
 .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));
 gap:8px}
 .cell{background:#241c11;border:1px solid #4a3d24;border-radius:4px;
 padding:8px 6px;text-align:center;min-height:120px}
 .cell.def{border-color:#c99b3f;box-shadow:0 0 6px #3a2f14}
 .cell.mark{background:#181510}
 .glyph{font-family:'Noto Sans Egyptian Hieroglyphs','Aegyptus',
 'Segoe UI Historic',sans-serif;font-size:42px;line-height:1.25}
 img.glyph{width:64px;height:auto;image-rendering:auto}
 .sk{font-family:Consolas,monospace;font-size:9px;color:#c9b587;
 text-align:left;margin:0 auto;display:inline-block}
 .sid{font-family:Consolas,monospace;font-size:11px;color:#e8b84b}
 .cp{font-family:Consolas,monospace;font-size:10px;color:#7a6a45}
 .xr{font-family:Consolas,monospace;font-size:10px;color:#6aa0c0}
 .mean{font-size:10px;color:#9a8a60;margin-top:3px}
 .def .mean{color:#d8b040}
</style></head><body>
<h1>THE FRESH DIALECT &mdash; every recorded Egyptian mark</h1>
""",
    f'<p class="meta">{total:,} marks &middot; {defined:,} with proposed uses '
    f'(gold border) &middot; {unknown:,} still UNKNOWN &middot; '
    f'grey cells = scribal control marks &middot; generated '
    f'{datetime.date.today().isoformat()} &middot; no borrowed decipherment</p>',
    '<p class="meta">Every mark shown as its authentic recorded image '
    '(glyphs/*.png -- code-chart shapes and the supplied annotated crop). '
    'Hover any cell for its meaning/note.</p>',
    '<input id="q" onkeyup="f()" placeholder="cross-reference: type a shelf '
    'mark, word, or codepoint">',
    """<script>
function f(){var q=document.getElementById('q').value.toLowerCase();
document.querySelectorAll('.cell').forEach(function(c){
c.style.display=(q===''||c.dataset.q.indexOf(q)>=0)?'':'none'});}
</script>"""]

    for b in order:
        ss = groups.get(b)
        if not ss:
            continue
        parts.append(f"<h2>{html.escape(b)} &mdash; {len(ss):,} marks</h2>"
                     '<div class="grid">')
        parts += [cell(s) for s in ss]
        parts.append("</div>")
    for b, ss in groups.items():
        if b in order or not ss:
            continue
        parts.append(f"<h2>{html.escape(b)} &mdash; {len(ss):,}</h2>"
                     '<div class="grid">')
        parts += [cell(s) for s in ss]
        parts.append("</div>")
    parts.append("</body></html>")

    with open(path, "w", encoding="utf-8") as fo:
        fo.write("".join(parts))
    return path


def compose(d):
    print(f"{STONE}Enter sign ids one per line (e.g. N03, A001, X-13460).")
    print(f"'[' opens a condensed proverb-group, ']' closes it.")
    print(f"'done' finishes, 'cancel' aborts. '?' lists N-signs.{RESET}")
    while True:
        try:
            line = input("sign> ").strip()
        except EOFError:
            break
        if not line:
            continue
        low = line.lower()
        if low == "done":
            break
        if low == "cancel":
            d.scratch = []
            print("discarded.")
            return
        if low == "?":
            for s in d.signs.values():
                if s.kind == "rosetta":
                    print(f"  {s.sid:<5} {s.meaning[:60]}")
            continue
        if line in "[]":
            d.scratch.append(line)
            print(f"  ({len(d.scratch)} entries)")
            continue
        sid = _sid(d, line)
        if sid in d.signs:
            d.scratch.append(sid)
            s = d.signs[sid]
            tag = s.meaning if s.defined else "UNKNOWN"
            print(f"  + {sid} ({tag[:50]})   [{len(d.scratch)} entries]")
        else:
            print(f"  no such sign '{line}'. '?' lists the base set.")
    print(f"scratch column: {len(d.scratch)} entries. 'read' it, 'keep <name>' it.")

def do_export(d, path=None):
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "egyptian_dialect.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("THE FRESH DIALECT -- personal record\n")
        f.write("(picture-first guesses, not confirmed translations)\n\n")
        f.write(LAWS + "\n")
        f.write("== ROSETTA BASE COLUMN (PROPOSED) ==\n")
        for e in d.rosetta_column:
            if e in "[]":
                f.write(f"  {e}\n"); continue
            s = d.signs[e]
            f.write(f"  {e:<5} {s.meaning}\n")
        f.write("\n" + textwrap.fill(ROSETTA_STORY, 76) + "\n\n")
        p = d.progress()
        info = language_format(d)
        book = book_coherence(d)
        local = local_verification(d)
        total = info["total"]
        f.write("== LANGUAGE KNOWLEDGE PROGRESS ==\n")
        f.write(f"  pictured signs proposed       : {p['pictured_proposed']:,}/{total:,}\n")
        f.write(f"  multi-use variables           : {info['multiuse']:,}/{total:,}\n")
        f.write(f"  format-verified internally    : {info['ready']:,}/{total:,}\n")
        f.write(f"  internally coherent columns   : {book['coherent']:,}/{book['unique']:,}\n")
        f.write(f"  literary-spine columns        : {book['literary']:,}/{book['unique']:,}\n")
        f.write(f"  locally corroborated signs    : {local['verified_signs']:,}/{total:,}\n")
        f.write(f"  locally corroborated uses     : {len(local['verified']):,}\n")
        f.write(f"  externally verified knowledge : {p['pictured_verified']:,}/{total:,}\n")
        f.write("  Internal verification is model consistency only; external\n")
        f.write("  verification needs two distinct transcribed column witnesses.\n\n")
        f.write("== PROPOSED SIGN USES ==\n")
        seen = d.evidence()
        for s in sorted(d.signs.values(), key=lambda x: x.sid):
            if s.defined:
                for k, dd in enumerate(s.defs):
                    witnesses = len(seen.get(s.sid, {}).get(dd["text"], ()))
                    f.write(f"  {s.sid:<9} #{k+1} "
                            f"[{dd.get('conf', 'proposal')}/"
                            f"{dd.get('mode', 'contextual')}/"
                            f"{dd.get('func', 'unassigned')}/"
                            f"{dd.get('reg', 'untagged')}] "
                            f"checks={witnesses}: {dd['text']}\n")
                if s.note:
                    f.write(f"{'':<11}note: {s.note}\n")
        f.write("\n== ADJACENT PICTURE COMPOUNDS (ALTERNATIVES, NOT PROOF) ==\n")
        for label, left, right, stories, basis in MOTIF_RULES:
            f.write(f"  {label} ({','.join(left)} -> {','.join(right)})\n")
            f.write(f"    A: {stories[0]}\n    B: {stories[1]}\n")
            f.write(f"    basis: {basis}\n")
        f.write("\n== PHOTO SHAPE FRAGMENTS (NOT IDENTIFIED GLYPHS) ==\n")
        for photo, shapes, first, alternative in PHOTO_FRAGMENTS:
            f.write(f"  {photo}: {shapes}\n"
                    f"    guess: {first}\n    alternative: {alternative}\n")
        f.write("\n== EXTERNAL VISUAL SOURCES (SHAPE CLUES ONLY) ==\n")
        for source, clue in SOURCE_CLUES:
            f.write(f"  {source}: {clue}\n")
        for sid, (description, url) in sorted(VISUAL_SOURCE_LINKS.items()):
            f.write(f"  {sid}: {description} -- {url}\n")
        f.write("  Phonetic, alphabetic and numeric claims were ignored.\n")
        f.write("\n== CORRELATION MATRIX (HEURISTIC, NOT PROOF) ==\n")
        for c, a, b in d.corr.top(n=60):
            f.write(f"  {a} ~ {b}   x{c}\n")
    print(f"written: {path}")
    return path

def _sid(d, raw):
    """Normalize a typed shelf mark: 'n05' -> 'N05', 'a001' -> 'A001'."""
    return raw.upper() if raw.upper() in d.signs else raw


def console(d):
    bar("THE FRESH DIALECT -- scribe console", "=")
    print(f"{STONE}Catalogue marks are not translations; proposed uses are labeled guesses.{RESET}")
    print(f"{STONE}Type 'help' for commands. 'rosetta' shows the base record.{RESET}\n")
    while True:
        try:
            line = input(f"{GOLD}dialect>{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        try:
            parts = shlex.split(line)
        except ValueError:
            parts = line.split()
        cmd, args = parts[0].lower(), parts[1:]

        if cmd in ("quit", "exit", "q"):
            break
        elif cmd == "help":
            print(HELP)
        elif cmd == "laws":
            print(LAWS)
        elif cmd == "dialects":
            print(DIALECTS_TEXT)
        elif cmd == "rosetta":
            rosetta(d)
        elif cmd == "read":
            name = args[0] if args else None
            entries = d.scratch if not name else d.columns.get(name)
            if entries is None:
                print(f"no column '{name}' -- 'columns' lists them")
            elif not entries:
                print("scratch column empty -- 'compose' to build one")
            else:
                read_column(d, entries, title=name or "scratch column")
        elif cmd == "page":
            page(d, args if args else None)
        elif cmd == "compose":
            compose(d)
        elif cmd == "columns":
            for name, col in d.columns.items():
                print(f"  {name:<16} {len(col)} entries")
            if d.scratch:
                print(f"  {'(scratch)':<16} {len(d.scratch)} entries")
        elif cmd == "keep":
            if not args:
                print("keep <name>")
            elif not d.scratch:
                print("scratch is empty")
            else:
                d.columns[args[0]] = list(d.scratch)
                n = d.learn_column(d.scratch)
                print(f"saved column '{args[0]}' -- endorsed: {n} chosen "
                      f"readings reinforced in the matrix")
        elif cmd == "show":
            if args:
                sign_card(d, _sid(d, args[0]))
            else:
                print("show <id>")
        elif cmd == "define":
            if len(args) >= 2:
                print(d.define(_sid(d, args[0]), " ".join(args[1:])))
            else:
                print("define <id> <meaning>")
        elif cmd == "note":
            if len(args) >= 2:
                print(d.note(_sid(d, args[0]), " ".join(args[1:])))
            else:
                print("note <id> <text>")
        elif cmd == "undefine":
            if not args:
                print("undefine <id> [n]   -- drop all readings, or just #n")
            else:
                sid = _sid(d, args[0])
                n = None
                if len(args) > 1:
                    try:
                        n = int(args[1])
                    except ValueError:
                        print("undefine <id> [n] -- n must be a number")
                        continue
                print(d.undefine(sid, n))
        elif cmd == "prefer":
            if len(args) >= 2:
                try:
                    print(d.prefer(_sid(d, args[0]), int(args[1])))
                except ValueError:
                    print("prefer <id> <n>")
            else:
                print("prefer <id> <n>   -- promote reading #n to primary")
        elif cmd == "likely":
            if len(args) >= 2:
                try:
                    print(d.likely(_sid(d, args[0]), int(args[1])))
                except ValueError:
                    print("likely <id> <n>")
            else:
                print("likely <id> <n>   -- flag reading #n 'highly likely'")
        elif cmd == "double":
            if len(args) >= 3:
                try:
                    print(d.double(_sid(d, args[0]), int(args[1]),
                                   " ".join(args[2:])))
                except ValueError:
                    print("double <id> <n> <second sense>")
            else:
                print("double <id> <n> <sense>  -- add a co-valid second sense")
        elif cmd == "undouble":
            if len(args) >= 2:
                try:
                    print(d.undouble(_sid(d, args[0]), int(args[1])))
                except ValueError:
                    print("undouble <id> <n>")
            else:
                print("undouble <id> <n>")
        elif cmd == "depict":
            if len(args) >= 2:
                print(d.depict(_sid(d, args[0]), " ".join(args[1:])))
            else:
                print("depict <id> <what the mark literally draws>")
        elif cmd == "mode":
            if len(args) >= 3:
                try:
                    print(d.mode(_sid(d, args[0]), int(args[1]), args[2]))
                except ValueError:
                    print("mode <id> <n> <evolved|action|literal|->")
            else:
                print("mode <id> <n> <evolved|action|literal|->")
        elif cmd == "func":
            if len(args) >= 3:
                try:
                    print(d.func(_sid(d, args[0]), int(args[1]),
                                 " ".join(args[2:])))
                except ValueError:
                    print("func <id> <n> <role>")
            else:
                print("func <id> <n> <role>  -- what the symbol DOES in the strip")
        elif cmd == "reg":
            if len(args) >= 3:
                try:
                    print(d.reg(_sid(d, args[0]), int(args[1]),
                                " ".join(args[2:])))
                except ValueError:
                    print("reg <id> <n> <adj|verb|noun|adj+verb|->")
            else:
                print("reg <id> <n> <register>  -- adjectival/verbal usage")
        elif cmd == "flex":
            if len(args) >= 3:
                try:
                    print(d.flex(_sid(d, args[0]), int(args[1]),
                                 " ".join(args[2:])))
                except ValueError:
                    print("flex <id> <n> <terminology note>")
            else:
                print("flex <id> <n> <note>  -- how the reading shifts "
                      "with neighbouring terminology")
        elif cmd == "concrete":
            if len(args) >= 2:
                try:
                    print(d.concrete(_sid(d, args[0]), int(args[1])))
                except ValueError:
                    print("concrete <id> <n>")
            else:
                print("concrete <id> <n>  -- toggle a locked (unflexing) "
                      "reading")
        elif cmd == "teach":
            src = d.scratch or (d.columns.get(args[0]) if args else None)
            if not src:
                print("nothing to teach -- 'compose' first, or 'teach <column>'")
            else:
                n = d.learn_column(src)
                print(f"endorsed: {n} chosen readings reinforced in the matrix")
        elif cmd == "cluster":
            if not args:
                if not d.clusters:
                    print("no clusters defined")
                for k, v in d.clusters.items():
                    rec = _norm_cluster(v)
                    print(f"  {k:<14} x{len(rec['defs'])}"
                          + (f"  circles: {rec['depicts']}"
                             if rec.get('depicts') else ""))
                    for n, dd in enumerate(rec["defs"]):
                        tg = "*" if n == 0 else " "
                        cf = f" [{dd['conf']}]" if dd.get("conf") else ""
                        md = f" {{{dd['mode']}}}" if dd.get("mode") else ""
                        print(f"    {tg}#{n+1} {dd['text'][:56]}{cf}{md}")
            else:
                sids, rest = [], []
                for a in args:
                    if not rest and _sid(d, a) in d.signs:
                        sids.append(_sid(d, a))
                    else:
                        rest.append(a)
                if len(sids) < 2 or not rest:
                    print("cluster <sid> <sid>... <whole-proverb meaning>")
                else:
                    print(d.define_cluster(sids, " ".join(rest)))
        elif cmd == "uncluster":
            if not args:
                print("uncluster <sid> <sid>...")
            else:
                print(d.drop_cluster([_sid(d, a) for a in args]))
        elif cmd == "matrix":
            sid = _sid(d, args[0]) if args else None
            pairs = d.corr.top(sid=sid)
            if not pairs:
                print("matrix empty -- 'keep' or 'teach' a column to learn")
            for c, a, b in pairs:
                la, lb = _def_label(d, a), _def_label(d, b)
                print(f"  x{c:<3} {a:<9} ~ {b:<9} {la[:28]} | {lb[:28]}")
            print("  Learned co-occurrence is a suggestion, not independent proof.")
        elif cmd == "attest":
            if len(args) == 4:
                try:
                    print(d.attest(args[0], args[1], _sid(d, args[2]),
                                   int(args[3])))
                except ValueError:
                    print("attest <source-image> <saved-column> <id> <reading-number>")
            else:
                print("attest <source-image> <saved-column> <id> <reading-number>")
        elif cmd == "audit":
            audit(d, _sid(d, args[0]) if args else None)
        elif cmd == "guesses":
            guesses_report(d)
        elif cmd == "motifs":
            entries = d.columns.get(args[0]) if args else (d.scratch or d.rosetta_column)
            if entries is None:
                print(f"no column '{args[0]}'")
            else:
                motifs_report(d, entries)
        elif cmd == "sources":
            sources_report()
        elif cmd == "history":
            history_report(d, " ".join(args) if args else None)
        elif cmd == "local":
            local_report(d, " ".join(args) if args else None)
        elif cmd == "format":
            format_report(d)
        elif cmd == "knowledge":
            knowledge_report(d)
        elif cmd == "book":
            book_report(d)
        elif cmd == "story":
            if not args:
                print("story <glyph-file> [translation-output.txt]")
            elif not os.path.exists(args[0]):
                print(f"no story file '{args[0]}'")
            else:
                story_report(d, args[0], args[1] if len(args) > 1 else None)
        elif cmd == "translate":
            if len(args) < 2:
                print("translate <english.txt> <glyphs.txt> [retention-report.txt]")
            elif not os.path.exists(args[0]):
                print(f"no English bridge file '{args[0]}'")
            else:
                translate_report(d, args[0], args[1],
                                 args[2] if len(args) > 2 else None)
        elif cmd == "transcribe":
            if len(args) < 2:
                print("transcribe <image> <review-id> [review.json]")
            elif not os.path.exists(args[0]):
                print(f"no image '{args[0]}'")
            else:
                try:
                    rec = transcribe_image(d, args[0], args[1])
                    if len(args) > 2:
                        write_transcription_review(rec, args[2])
                        print(f"review written: {args[2]}")
                    print(f"{len(rec['columns'])} column(s), "
                          f"{sum(len(c['entries']) for c in rec['columns'])} "
                          "candidate cells -- review required")
                except ImportError as e:
                    print(f"image transcription needs pillow/numpy/opencv: {e}")
        elif cmd == "review":
            transcription_report(d, args[0] if args else None)
        elif cmd == "pick":
            if len(args) < 3:
                print("pick <transcription-id> <cell#> <candidate#|sid>")
            else:
                try:
                    print(pick_transcription(d, args[0], int(args[1]), args[2]))
                except ValueError:
                    print("pick <transcription-id> <cell#> <candidate#|sid>")
        elif cmd == "approve":
            if len(args) < 2:
                print("approve <transcription-id> <column-name> [column#]")
            else:
                try:
                    print(approve_transcription(
                        d, args[0], args[1],
                        int(args[2]) if len(args) > 2 else None))
                except ValueError:
                    print("approve <transcription-id> <column-name> [column#]")
        elif cmd == "reject":
            print(reject_transcription(d, args[0]) if args
                  else "reject <transcription-id>")
        elif cmd == "catalog":
            catalog(d, args[0] if args else "all")
        elif cmd == "search":
            if args:
                catalog(d, args[0])
                q = " ".join(args).lower()
                hits = [(k, dd) for k, rec in d.clusters.items()
                        for dd in _norm_cluster(rec)["defs"]
                        if q in dd["text"].lower()
                        or q in dd.get("also", "").lower()
                        or q in (rec.get("depicts") or "").lower()]
                for k, dd in hits:
                    print(f"  cluster {k:<14} {dd['text'][:60]}")
            else:
                print("search <word>")
        elif cmd == "stats":
            stats(d)
        elif cmd == "save":
            print(f"saved -> {d.save()}")
        elif cmd == "load":
            print("loaded." if d.load() else "no dialect file yet.")
        elif cmd == "chart":
            print(f"written: {chart(d)}")
        elif cmd == "window":
            launch_window(d)
        elif cmd == "export":
            do_export(d)
        elif cmd == "clear":
            d.scratch = []
            print("scratch cleared.")
        else:
            print(f"'{cmd}'? -- 'help' for commands")

# ==============================================================================
# SECTION 5b -- THE SCRIBE WINDOW (pygame): write the language with autocorrect
# ==============================================================================
# Like the ReferenceCode viewers: a real window. Left = defined-sign palette,
# center = the column being written (top->down, proverb bands), right = the
# live story + strip roles, bottom = the write-line with suggestion chips.
# Autocorrect: type a meaning or a near-miss spelling; ENTER writes the best
# matching sign -- 'fihs' writes the fish, 'brid' writes the bird.

def suggest(d, text, n=7):
    """Autocomplete + autocorrect: match a typed fragment against shelf
    marks, candidate readings, second senses, depictions and notes.
    Returns [(score, sign)] best-first."""
    if not text or text in "[]":
        return []
    q = text.strip().lower()
    if not q:
        return []
    scored = []
    for s in d.signs.values():
        best = 0.0
        sl = s.sid.lower()
        if sl == q:
            best = 1.0
        elif sl.startswith(q):
            best = 0.9
        for dd in s.defs:                      # usable readings first
            for f in (dd["text"], dd.get("also", "")):
                fl = f.lower()
                if not fl:
                    continue
                if q in fl.split() or fl.startswith(q):
                    best = max(best, 0.98)
                elif q in fl:
                    best = max(best, 0.84)
                r = max((difflib.SequenceMatcher(None, q, w).ratio()
                         for w in fl.split()), default=0.0)
                best = max(best, r * 0.94)
        for f in (s.depicts or "", s.note):     # literal/name context second
            fl = f.lower()
            if not fl:
                continue
            if q in fl.split() or fl.startswith(q):
                best = max(best, 0.78)
            elif q in fl:
                best = max(best, 0.66)
            r = max((difflib.SequenceMatcher(None, q, w).ratio()
                     for w in fl.split()), default=0.0)
            best = max(best, r * 0.74)
        if best >= 0.5:
            scored.append((best, s))
    scored.sort(key=lambda x: (-x[0],
                               0 if x[1].defined else 1,
                               0 if x[1].kind == "rosetta" else 1,
                               x[1].sid))   # usable readings first, then seeds
    return scored[:n]


class ScribeUI:
    """The interactive scribe window. Logic methods are headless-testable:
    type_char / press / run(frames)."""
    PAL_PAGE_SIZE = 500
    BG = (18, 14, 8)
    PANEL = (28, 22, 12)
    INK = (216, 190, 130)
    GOLD = (232, 184, 75)
    CYAN = (110, 200, 220)
    DIMC = (120, 104, 70)
    REDC = (220, 90, 70)

    def __init__(self, d, headless=False, size=(1280, 800)):
        import pygame
        self.pg = pygame
        pygame.init()
        flags = 0 if headless else pygame.RESIZABLE
        self.screen = pygame.display.set_mode(size, flags)
        pygame.display.set_caption("THE FRESH DIALECT -- scribe")
        self.d = d
        self.input = ""
        self.sugs = []
        self.sel = 0
        self.story = []
        self.roles = []
        self.motif_notes = []
        self.status = ("type a meaning or shelf mark -- ENTER writes the "
                       "corrected sign")
        self.scroll = 0             # story px scrolled up from the latest line
        self._story_scroll_max = 0  # max story scroll (set during draw)
        self._story_viewport = None # story clip rect, excluding search bar
        self.pal_scroll = 0
        self.pal_page = 0
        self.pal_genre_i = 0
        self.genre_open = False
        self.col_scroll = 0         # px scrolled up from the latest mark
        self._col_maxoff = 0        # max column scroll (set during draw)
        self._pal_scroll_max = 0    # max page scroll (set during draw)
        self.lp_w = 300             # marks pane width
        self.rp_w = 400             # story pane width
        self._lp_w = self.lp_w      # palette hit edge (set during draw)
        self._rp_edge = 9999        # story-pane edge (set during draw)
        self.split_drag = None      # 'marks' | 'story' while resizing
        self.split_rects = []       # [(rect, side)] separator hit zones
        self._pal_cols = 0
        self._pal_glyph_size = 0
        self.drag_sid = None        # mark being dragged, or None
        self.drag_from = None       # column index if reordering, else palette
        self.insert_i = None        # hovered column gap while dragging
        self.pal_cells = []         # [(rect, sid)] for palette hit-tests
        self.col_rects = []         # [(rect, entry_index)] column hit-tests
        self.btn_rects = []         # [(rect, token)] bracket buttons
        self.define_sid = None      # palette mark receiving a custom meaning
        self.define_input = ""      # typed correction for define_sid
        self.def_menu = None        # (x, y, sid) palette context-menu anchor
        self.def_menu_rect = None   # DEFINE... hit box
        self.help_open = False      # F1 information panel
        self.help_rect = None       # top-center F1 button
        self.dialect_file = DIALECT_FILE
        self.mouse = (0, 0)
        # every mark ever recorded is placeable -- defined or UNKNOWN
        ros = [s.sid for s in d.signs.values() if s.kind == "rosetta"]
        dfn = [s.sid for s in d.signs.values()
               if s.kind != "rosetta" and s.defined]
        rest = [s.sid for s in d.signs.values()
                if s.kind != "rosetta" and not s.defined]
        self.palette_all = ros + dfn + rest
        self.pal_view = None        # filtered sids, or None = full list
        self.pal_genres = ["ALL"]
        self.pal_genre_counts = {"ALL": len(self.palette_all)}
        for sid in self.palette_all:
            block = self.d.signs[sid].block or "Other"
            self.pal_genre_counts[block] = \
                self.pal_genre_counts.get(block, 0) + 1
            if block not in self.pal_genres:
                self.pal_genres.append(block)
        self.pal_nav_rects = []
        self.genre_rects = []
        self._def_terms = defaultdict(set)
        self._context_terms = defaultdict(set)
        self._def_vocab = set()
        self._context_vocab = set()
        for sid in self.palette_all:
            s = self.d.signs[sid]
            for dd in s.defs:
                for field in (dd["text"], dd.get("also", "")):
                    self._index_definition(sid, field)
            for field in (s.depicts or "", s.note):
                for word in re.findall(r"[a-z0-9]+", field.lower()):
                    self._context_terms[word].add(sid)
                    self._context_vocab.add(word)
        self._def_by_initial = defaultdict(list)
        self._context_by_initial = defaultdict(list)
        for w in self._def_vocab:
            self._def_by_initial[w[0]].append(w)
        for w in self._context_vocab:
            self._context_by_initial[w[0]].append(w)
        self._pal_glyph_cache = {}
        self._match_cache = {}
        self._sids_by_initial = defaultdict(list)
        for sid in self.palette_all:
            self._sids_by_initial[sid[0].lower()].append(sid)
        self._progress_cache = d.progress()
        self.font = pygame.font.SysFont("consolas", 15)
        self.small = pygame.font.SysFont("consolas", 12)
        self.tiny = pygame.font.SysFont("consolas", 9)
        self.big = pygame.font.SysFont("consolas", 20, bold=True)
        self.title = pygame.font.SysFont("consolas", 22, bold=True)
        # real symbol rendering: every mark carries an authentic tile in
        # glyphs/<sid>.png (built by --build-tiles from the documents);
        # fonts are only a fallback for a mark with no tile on disk.
        _base = os.path.dirname(os.path.abspath(__file__))
        self._tile_dir = os.path.join(_base, "glyphs")
        _fp = os.path.join(_base, "NotoEH.ttf")
        if not os.path.exists(_fp):
            _fp = os.path.join(_base,
                               "NotoSansEgyptianHieroglyphs.ttf")
        self._fonts = self._fonts_big = []
        for fp, size, big in ((_fp, 28, 56),
                              (os.path.join(_base, "Aegyptus.ttf"),
                               28, 56),
                              (os.path.join(_base, "NewGardiner.ttf"),
                               28, 56)):
            if not os.path.exists(fp):
                continue
            try:
                self._fonts.append(pygame.font.Font(fp, size))
                self._fonts_big.append(pygame.font.Font(fp, big))
            except Exception:
                pass
        if not self._fonts:
            for f_ in ("segoeuihistoric",):
                self._fonts.append(pygame.font.SysFont(f_, 28))
                self._fonts_big.append(pygame.font.SysFont(f_, 46))
        self._tofu = pygame.image.tostring(
            self._fonts[0].render("\U0010FFFF", True, self.INK), "RGBA")
        self._glyphs = {}
        self.refresh_story()

    def _tile_surf(self, s, big):
        """The mark's authentic tile image as a Surface (glyph area only,
        label strip cropped), or None when no tile exists."""
        fp = os.path.join(self._tile_dir, s.sid + ".png")
        if not os.path.exists(fp):
            return None
        try:
            t = self.pg.image.load(fp)
        except Exception:
            return None
        w, h = t.get_size()
        zone = t  # glyph-only transparent tile -- the whole file IS symbol
        target = 72 if big else 36  # ~20% larger symbols
        r = zone.get_rect()
        k = target / max(1, max(r.width, r.height))
        return self.pg.transform.smoothscale(
            zone, (max(1, int(r.width * k)),
                   max(1, int(r.height * k))))

    def glyph(self, s, big=False):
        """The mark as a real image -- the authentic tile first, the
        recorded-sign fonts as fallback. Never ASCII art."""
        key = (s.sid, big)
        if key in self._glyphs:
            return self._glyphs[key]
        surf = self._tile_surf(s, big)
        if surf is None:
            ch = s.char
            if not ch:
                for xs in s.xref:                 # seed marks borrow their
                    xsig = self.d.signs.get(xs)   # recorded shape via xref
                    if xsig and xsig.char:
                        ch = xsig.char
                        break
            if ch:
                fonts = self._fonts_big if big else self._fonts
                for fnt in fonts:
                    try:
                        t = fnt.render(ch, True, self.INK)
                        tf = fnt.render("\U0010FFFF", True, self.INK)
                        if self.pg.image.tostring(t, "RGBA") != \
                                self.pg.image.tostring(tf, "RGBA"):
                            surf = t
                            break
                    except Exception:
                        pass
        self._glyphs[key] = surf
        return surf

    def glyph_variants(self, s, big=False):
        """Candidate shapes for a mark -- the authentic tile plus the
        font rendering when both exist (they may be the same shape)."""
        out = []
        t = self._tile_surf(s, big)
        if t is not None:
            out.append(("tile (authentic)", t))
        if s.char:
            fonts = self._fonts_big if big else self._fonts
            for fnt in fonts:
                try:
                    r = fnt.render(s.char, True, self.INK)
                    tf = fnt.render("\U0010FFFF", True, self.INK)
                    if self.pg.image.tostring(r, "RGBA") != \
                            self.pg.image.tostring(tf, "RGBA"):
                        out.append(("recorded sign " +
                                    f"U+{ord(s.char):05X}", r))
                        break
                except Exception:
                    pass
        return out

    # -- state ---------------------------------------------------------------
    def _index_definition(self, sid, text):
        """Index definition words immediately, including UI corrections."""
        for word in re.findall(r"[a-z0-9]+", (text or "").lower()):
            self._def_terms[word].add(sid)
            if word not in self._def_vocab:
                self._def_vocab.add(word)
                by_initial = getattr(self, "_def_by_initial", None)
                if by_initial is not None:
                    by_initial[word[0]].append(word)

    def _indexed_suggest(self, text, n=400):
        """Fast UI search over the prebuilt vocabulary index."""
        q = text.strip().lower()
        if not q or q in "[]":
            return []
        scores = {}
        for sid in self._sids_by_initial.get(q[0], ()):  # shelf-mark prefix
            sl = sid.lower()
            if sl == q:
                scores[sid] = 1.0
            elif sl.startswith(q):
                scores[sid] = max(scores.get(sid, 0.0), 0.9)
        for vocab, terms, index, exact, inside in (
                (self._def_vocab, self._def_terms,
                 self._def_by_initial, 0.98, 0.84),
                (self._context_vocab, self._context_terms,
                 self._context_by_initial, 0.78, 0.66)):
            for word in index.get(q[0], ()):
                if word == q or word.startswith(q):
                    score = exact
                elif q in word:
                    score = inside
                else:
                    continue
                for sid in terms[word]:
                    scores[sid] = max(scores.get(sid, 0.0), score)
        if len(q) >= 2:
            for vocab, terms, index, mult in (
                    (self._def_vocab, self._def_terms,
                     self._def_by_initial, 0.94),
                    (self._context_vocab, self._context_terms,
                     self._context_by_initial, 0.74)):
                for word in index.get(q[0], ()):
                    if abs(len(word) - len(q)) > 2:
                        continue
                    r = difflib.SequenceMatcher(None, q, word).ratio()
                    score = r * mult
                    if score < 0.5:
                        continue
                    for sid in terms[word]:
                        scores[sid] = max(scores.get(sid, 0.0), score)
        out = [(score, self.d.signs[sid])
               for sid, score in scores.items() if score >= 0.5]
        out.sort(key=lambda x: (-x[0],
                                0 if x[1].defined else 1,
                                0 if x[1].kind == "rosetta" else 1,
                                x[1].sid))
        return out[:n]

    def set_input(self, t):
        self.input = t
        self.genre_open = False
        broad = self._indexed_suggest(t, 400)
        self.sugs = broad[:7]
        self._match_cache = {}
        self.sel = 0
        self.pal_view = [s.sid for _s, s in broad] if t.strip() else None
        self.pal_scroll = 0
        self.pal_page = 0

    def _begin_define(self, sid):
        self.define_sid = sid
        self.define_input = ""
        self.def_menu = self.def_menu_rect = None
        self.input = ""
        self.sugs = []
        self.status = (f"DEFINE {sid}: type a corrective meaning, ENTER saves, "
                       "ESC cancels")

    def _finish_define(self):
        sid, text = self.define_sid, self.define_input.strip()
        if not sid or not text:
            return
        s = self.d.signs[sid]
        existing = next((i + 1 for i, dd in enumerate(s.defs)
                         if dd["text"] == text), None)
        if existing is None:
            self.d.define(sid, text, source="Nathan -- UI correction")
            existing = len(s.defs)
        self.d.prefer(sid, existing)
        self._index_definition(sid, text)
        self._progress_cache = self.d.progress()
        path = self.d.save(self.dialect_file)
        self.define_sid = None
        self.define_input = ""
        self.status = f"saved {sid} primary meaning -> {path}"

    def type_char(self, ch):
        if self.define_sid:
            self.define_input += ch
            return
        if ch in "[]":
            self.d.scratch.append(ch)
            self.refresh_story()
            self.status = "condensed proverb-group " + ("opened" if ch == "["
                                                       else "closed")
            return
        self.set_input(self.input + ch)

    def accept(self):
        t = self.input.strip()
        if not t:
            return
        if self.sugs:
            self.insert(self.sugs[self.sel][1])
        elif t.upper() in self.d.signs:
            self.insert(self.d.signs[t.upper()])
        else:
            self.status = f"no correction found for '{t}'"
            return
        self.set_input("")

    def insert(self, s):
        self.d.scratch.append(s.sid)
        self.status = f"+ {s.sid} -- {s.meaning[:60]}"
        self.refresh_story()

    def refresh_story(self):
        self.scroll = 0  # newly generated stories reopen at the latest lines
        if not self.d.scratch:
            self.story, self.roles = [], []
            self.motif_notes = []
            return
        self.story = read_column(self.d, self.d.scratch, show=False)
        self.motif_notes = motif_matches(self.d.scratch)
        positions = _positions(self.d, self.d.scratch)
        chosen = _select(self.d, positions)
        self.roles = []
        for i, (sid, _g) in enumerate(positions):
            s = self.d.signs.get(sid)
            di = chosen.get(i, -1)
            self.roles.append(s.defs[di].get("func", "?")
                              if s and s.defined and di >= 0 else "?")

    def press(self, key):
        """Symbolic keys (also called by tests): ENTER TAB UP DOWN BACKSPACE
        DELETE ESCAPE R CTRL+S CTRL+K"""
        if key == "BACKSPACE":
            if self.define_sid:
                self.define_input = self.define_input[:-1]
            elif self.input:
                self.set_input(self.input[:-1])
            elif self.d.scratch:
                self.d.scratch.pop()
                self.refresh_story()
                self.status = "erased the last mark"
        elif key == "DELETE":
            if self.d.scratch:
                self.d.scratch.pop()
                self.refresh_story()
        elif key == "ESCAPE":
            self.genre_open = False
            self.help_open = False
            self.def_menu = self.def_menu_rect = None
            if self.define_sid:
                self.define_sid = None
                self.define_input = ""
                self.status = "definition edit cancelled"
            else:
                self.set_input("")
        elif key in ("UP", "DOWN", "TAB"):
            if self.sugs:
                d_ = -1 if key == "UP" else 1
                self.sel = (self.sel + d_) % len(self.sugs)
        elif key == "ENTER":
            if self.define_sid:
                self._finish_define()
            else:
                self.accept()
        elif key == "R":
            self.refresh_story()
        elif key == "CTRL+S":
            self.status = "saved -> " + self.d.save()
        elif key == "CTRL+K":
            if self.d.scratch:
                name = f"col{len(self.d.columns)}"
                self.d.columns[name] = list(self.d.scratch)
                n = self.d.learn_column(self.d.scratch)
                self.status = f"kept '{name}' -- {n} readings endorsed"
            else:
                self.status = "nothing to keep"
        elif key == "F1":
            self.help_open = not self.help_open
        elif key in ("PAGEUP", "PAGEDOWN"):
            self._pal_page_step(-1 if key == "PAGEUP" else 1)

    def _pal_view(self):
        view = self.pal_view if self.pal_view is not None else self.palette_all
        genre = self.pal_genres[self.pal_genre_i]
        if genre == "ALL":
            return view
        return [sid for sid in view if self.d.signs[sid].block == genre]

    def _pal_page_count(self, view=None):
        n = len(self._pal_view() if view is None else view)
        return max(1, (n + self.PAL_PAGE_SIZE - 1) // self.PAL_PAGE_SIZE)

    def _pal_page_view(self):
        view = self._pal_view()
        pages = self._pal_page_count(view)
        self.pal_page = max(0, min(self.pal_page, pages - 1))
        a = self.pal_page * self.PAL_PAGE_SIZE
        return view[a:a + self.PAL_PAGE_SIZE], view, pages

    def _pal_page_step(self, step):
        pages = self._pal_page_count()
        self.pal_page = (self.pal_page + step) % pages
        self.pal_scroll = 0
        self.status = f"marks PAGE {self.pal_page + 1}/{pages}"

    def _pal_genre_pick(self, i):
        self.pal_genre_i = max(0, min(i, len(self.pal_genres) - 1))
        self.genre_open = False
        self.pal_page = self.pal_scroll = 0
        genre = self.pal_genres[self.pal_genre_i]
        n = self.pal_genre_counts[genre]
        self.status = f"GENRE {genre} -- {n:,} marks"

    def _matched_def(self, s):
        """Candidate text that caused this search hit (primary if unclear)."""
        q = self.input.strip().lower()
        key = (s.sid, q)
        if key in self._match_cache:
            return self._match_cache[key]
        best, best_score = s.meaning, 0.0
        for dd in s.defs:
            for f in (dd["text"], dd.get("also", "")):
                fl = f.lower()
                if not fl:
                    continue
                score = 1.0 if q in fl.split() or fl.startswith(q) \
                    else 0.75 if q in fl else max(
                        (difflib.SequenceMatcher(None, q, w).ratio()
                         for w in fl.split()), default=0.0)
                if score > best_score:
                    best, best_score = dd["text"], score
        self._match_cache[key] = best
        return best

    def _pal_glyph(self, s, size):
        """Palette tile cached at the pane's current display size."""
        key = (s.sid, size)
        if key not in self._pal_glyph_cache:
            g = self.glyph(s)
            if g is None:
                self._pal_glyph_cache[key] = None
            else:
                g = self.pg.transform.smoothscale(g, (size, size))
                g = g.copy()
                g.fill((70, 50, 15, 0), special_flags=self.pg.BLEND_RGB_ADD)
                self._pal_glyph_cache[key] = g
        return self._pal_glyph_cache[key]

    def _resize_panes(self, pos):
        """Drag a pane separator while preserving a usable centre pane."""
        w = self.screen.get_width()
        if self.split_drag == "marks":
            limit = max(220, w - self.rp_w - 320)
            self.lp_w = max(220, min(pos[0], limit))
        elif self.split_drag == "story":
            limit = max(240, w - self.lp_w - 320)
            self.rp_w = max(240, min(w - pos[0], limit))
        self.status = f"panes marks={self.lp_w}px story={self.rp_w}px"

    # -- drag and drop ---------------------------------------------------------
    def insert_at(self, i, sid):
        i = max(0, min(i, len(self.d.scratch)))
        self.d.scratch.insert(i, sid)
        self.status = f"+ {sid} dropped into the column"
        self.refresh_story()

    def _mouse_down(self, pos, button=1):
        if self.help_rect and self.help_rect.collidepoint(pos):
            self.help_open = not self.help_open
            return
        if self.def_menu_rect and self.def_menu_rect.collidepoint(pos):
            _x, _y, sid = self.def_menu
            self._begin_define(sid)
            return
        if self.def_menu:
            self.def_menu = self.def_menu_rect = None
        if button == 3:
            for r, sid in self.pal_cells:
                if r.collidepoint(pos):
                    self.def_menu = (pos[0], pos[1], sid)
                    self.status = f"DEFINE {sid} -- click DEFINE..., ESC closes"
                    return
            return
        for r, side in self.split_rects:
            if r.collidepoint(pos):
                self.split_drag = side
                return
        for r, gi in self.genre_rects:
            if r.collidepoint(pos):
                self._pal_genre_pick(gi)
                return
        for r, action in self.pal_nav_rects:
            if r.collidepoint(pos):
                if action == "prev":
                    self._pal_page_step(-1)
                elif action == "next":
                    self._pal_page_step(1)
                else:
                    self.genre_open = not self.genre_open
                return
        if self.genre_open:
            self.genre_open = False
        for r, sid in self.pal_cells:
            if r.collidepoint(pos):
                self.drag_sid, self.drag_from = sid, None
                return
        for r, i in self.col_rects:
            if r.collidepoint(pos):
                self.drag_sid, self.drag_from = self.d.scratch[i], i
                return
        for r, tok in self.btn_rects:
            if r.collidepoint(pos):
                self.d.scratch.append(tok)
                self.refresh_story()
                return

    def _drag_to(self, pos):
        self.mouse = pos
        self.insert_i = None
        if not self.col_rects:
            if pos[0] > self._lp_w:
                self.insert_i = 0
            return
        # nearest vertical gap between column cells -> insertion index
        ys = [(r.centery, i) for r, i in self.col_rects]
        ys.sort()
        if pos[1] <= ys[0][0]:
            self.insert_i = ys[0][1]
        elif pos[1] > ys[-1][0]:
            self.insert_i = ys[-1][1] + 1
        else:
            for (y1, i1), (y2, i2) in zip(ys, ys[1:]):
                if y1 < pos[1] <= y2:
                    self.insert_i = i1 + 1
                    break

    def _mouse_wheel(self, ev):
        """Wheel-scroll the pane under the cursor."""
        mx = self.mouse[0]
        if mx < self._lp_w:
            self.pal_scroll = max(0, min(
                self._pal_scroll_max, self.pal_scroll - ev.y * 12))
        elif mx < self._rp_edge:
            self.col_scroll = max(0, min(
                self._col_maxoff, self.col_scroll + ev.y * 30))
        else:
            self.scroll = max(0, min(
                self._story_scroll_max, self.scroll + ev.y * 30))

    def _mouse_up(self, pos, button):
        if self.split_drag:
            self.split_drag = None
            return
        if button == 3:  # right-click removes the column entry
            for r, i in self.col_rects:
                if r.collidepoint(pos) and i < len(self.d.scratch):
                    gone = self.d.scratch.pop(i)
                    self.status = f"- {gone} lifted out"
                    self.refresh_story()
            return
        if self.drag_sid is None:
            return
        if self.insert_i is not None:
            if self.drag_from is None:
                self.insert_at(self.insert_i, self.drag_sid)
            else:  # reorder within the column
                i = self.insert_i
                j = self.drag_from
                if i > j:
                    i -= 1
                if i != j:
                    sid = self.d.scratch.pop(j)
                    self.d.scratch.insert(i, sid)
                    self.refresh_story()
        self.drag_sid = self.drag_from = self.insert_i = None

    def _key(self, ev):
        pg = self.pg
        ctrl = ev.mod & (pg.KMOD_CTRL | pg.KMOD_META)
        if ctrl and ev.key == pg.K_s:
            self.press("CTRL+S"); return
        if ctrl and ev.key == pg.K_k:
            self.press("CTRL+K"); return
        mp = {pg.K_RETURN: "ENTER", pg.K_KP_ENTER: "ENTER",
              pg.K_BACKSPACE: "BACKSPACE", pg.K_DELETE: "DELETE",
              pg.K_ESCAPE: "ESCAPE", pg.K_TAB: "TAB",
              pg.K_UP: "UP", pg.K_DOWN: "DOWN", pg.K_r: "R",
              pg.K_F1: "F1",
              pg.K_PAGEUP: "PAGEUP", pg.K_PAGEDOWN: "PAGEDOWN"}
        if ev.key in mp:
            self.press(mp[ev.key])
        elif ev.unicode and ev.unicode.isprintable() and not ctrl:
            self.type_char(ev.unicode)

    # -- drawing ---------------------------------------------------------------
    def _t(self, font, txt, pos, col):
        self.screen.blit(font.render(str(txt), True, col), pos)

    def _panel(self, rect):
        self.pg.draw.rect(self.screen, self.PANEL, rect)
        self.pg.draw.rect(self.screen, (74, 61, 36), rect, 1)

    def render(self):
        pg, sc = self.pg, self.screen
        W_, H = sc.get_size()
        sc.fill(self.BG)
        lp_w = max(220, min(self.lp_w, W_ - self.rp_w - 320))
        rp_w = max(240, min(self.rp_w, W_ - lp_w - 320))
        self.lp_w, self.rp_w = lp_w, rp_w
        self._panel((0, 56, lp_w, H - 56))
        self._panel((W_ - rp_w, 56, rp_w, H - 56))
        self._panel((lp_w, 56, W_ - lp_w - rp_w, H - 56))
        self.split_rects = [
            (pg.Rect(lp_w - 4, 56, 8, H - 56), "marks"),
            (pg.Rect(W_ - rp_w - 4, 56, 8, H - 56), "story")]
        for r, side in self.split_rects:
            pg.draw.rect(self.screen,
                         self.GOLD if self.split_drag == side
                         else (100, 78, 40), r)
            pg.draw.line(self.screen, (52, 39, 20),
                         (r.centerx, 72), (r.centerx, H - 16), 1)
        self._t(self.title, "THE FRESH DIALECT -- scribe", (10, 8), self.GOLD)
        p = self._progress_cache
        pct = (100 * p["pictured_verified"] / p["pictured_total"]
               if p["pictured_total"] else 0)
        guessed = (100 * p["pictured_proposed"] / p["pictured_total"]
                   if p["pictured_total"] else 0)
        if W_ >= 950:
            self._t(self.small, f"PICTURES {guessed:.2f}% guess | "
                    f"{pct:.2f}% checked", (W_ - 258, 16), self.CYAN)
        self._t(self.small, self.status[:150], (10, 36), self.DIMC)
        self.help_rect = pg.Rect(max(250, W_ // 2 - 90), 8, 180, 22)
        pg.draw.rect(self.screen, self.PANEL, self.help_rect)
        pg.draw.rect(self.screen, self.GOLD, self.help_rect, 1)
        self._t(self.small, "F1  INFO / DEFINE", self.help_rect.move(10, 5),
                self.GOLD)
        self._t(self.small,
                "ENTER write/correct  [ ] cluster  BKSP undo  ^K keep  "
                "^S save  F1 info  wheel scroll  ESC clear",
                (10, H - 20), self.DIMC)

        # LEFT: the full mark palette -- EVERY recorded mark, defined or
        # UNKNOWN, draggable into the column (glyphs first, english never)
        self.pal_cells = []
        self.pal_nav_rects = []
        self.genre_rects = []
        page_view, view, pages = self._pal_page_view()
        genre = self.pal_genres[self.pal_genre_i]
        self._t(self.font, f"ALL MARKS ({len(view):,})", (10, 62), self.GOLD)
        nav_specs = (("<", "prev", 8, 20),
                     (f"PAGE {self.pal_page + 1:02d}/{pages}", None, 30, 76),
                     (">", "next", 108, 20),
                     (f"GENRE {genre[:12]} ▾", "genre", 130,
                      max(82, lp_w - 138)))
        for label, action, x, w_ in nav_specs:
            rect = pg.Rect(x, 80, w_, 17)
            if action:
                self.pal_nav_rects.append((rect, action))
            pg.draw.rect(self.screen, self.PANEL, rect)
            pg.draw.rect(self.screen, (74, 61, 36), rect, 1)
            self._t(self.tiny, label, (rect.x + 5, rect.y + 4), self.GOLD)

        cols = max(6, min(12, (lp_w - 16) // 68))
        cw = max(32, (lp_w - 16) // cols)
        glyph_size = max(24, min(72, cw - 8))
        ch = glyph_size + 17
        rows = max(1, (H - 102 - 60) // ch)
        self._pal_cols = cols
        self._pal_glyph_size = glyph_size
        self._pal_scroll_max = max(0, len(page_view) - cols * rows)
        self.pal_scroll = max(0, min(self.pal_scroll, self._pal_scroll_max))
        x0, y0 = 8, 102
        for idx, sid in enumerate(page_view[self.pal_scroll:
                                           self.pal_scroll + cols * rows]):
            col, row = idx % cols, idx // cols
            x, y = x0 + col * cw, y0 + row * ch
            s = self.d.signs[sid]
            r = pg.Rect(x, y, cw - 3, ch - 3)
            self.pal_cells.append((r, sid))
            pg.draw.rect(self.screen, (18, 13, 6), r)
            pg.draw.rect(self.screen,
                         self.GOLD if s.defined else (88, 70, 36), r, 1)
            g = self._pal_glyph(s, glyph_size)
            if g is not None:
                self.screen.blit(g, (x + (cw - glyph_size) // 2, y + 2))
            else:
                self._t(self.font, "\u25a2", (x + 12, y + 4), self.DIMC)
            self._t(self.tiny, sid[:max(3, (cw - 4) // 6)],
                    (x + 3, y + glyph_size + 5),
                    self.CYAN if s.defined else self.DIMC)

        if self.genre_open:
            mx, my, row_h = 130, 100, 18
            mw = max(82, lp_w - mx - 8)
            mh = len(self.pal_genres) * row_h + 4
            pg.draw.rect(self.screen, (24, 18, 9),
                         (mx - 4, my - 3, mw + 8, mh))
            pg.draw.rect(self.screen, self.GOLD,
                         (mx - 4, my - 3, mw + 8, mh), 1)
            for gi, gname in enumerate(self.pal_genres):
                r = pg.Rect(mx, my + gi * row_h, mw, row_h)
                self.genre_rects.append((r, gi))
                chosen = gi == self.pal_genre_i
                pg.draw.rect(self.screen,
                             (58, 43, 17) if chosen else (24, 18, 9), r)
                n = self.pal_genre_counts[gname]
                mark = ">" if chosen else " "
                self._t(self.tiny, f"{mark} {gname[:34]} -- {n:,}",
                        (r.x + 6, r.y + 5), self.GOLD if chosen else self.INK)

        if self.def_menu:
            mx, my, sid = self.def_menu
            mw = max(150, min(220, lp_w - 12))
            r = pg.Rect(min(mx, lp_w - mw - 6), min(my, H - 90), mw, 26)
            self.def_menu_rect = r
            pg.draw.rect(self.screen, (42, 30, 12), r)
            pg.draw.rect(self.screen, self.GOLD, r, 1)
            self._t(self.small, f"DEFINE {sid}...", (r.x + 8, r.y + 7),
                    self.GOLD)
        else:
            self.def_menu_rect = None

        # CENTER: the column being written (top -> down) -- drop zone
        self.col_rects = []
        self.btn_rects = []
        cx, cy = lp_w + 16, 64
        center_w = W_ - lp_w - rp_w
        col_w = max(180, min(420, center_w - 24))
        self._t(self.font, "COLUMN (top -> down, drop marks here)", (cx, cy),
                self.GOLD)
        bx = cx + max(0, min(center_w - 230, 330))
        for tok, lbl in (("[", "<< open cluster"), ("]", "close cluster >>")):
            r = pg.Rect(bx if tok == "[" else bx + 120, cy - 2, 110, 18)
            self.btn_rects.append((r, tok))
            pg.draw.rect(self.screen, self.PANEL, r)
            self._t(self.small, lbl, (r.x + 6, r.y + 3), self.GOLD)
        cy += 24
        cells, in_g = [], False
        for i, e in enumerate(self.d.scratch):
            if e == "[":
                cells.append(("band", "<< CLUSTER >>", i))
                in_g = True
            elif e == "]":
                cells.append(("band", "<< /CLUSTER >>", i))
                in_g = False
            else:
                cells.append(("sign", e, i))
        avail = H - 90 - 140
        total_h = 0
        for kind, e, i in cells:
            total_h += 20 if kind == "band" else 118
        self._lp_w = lp_w
        self._rp_edge = W_ - rp_w
        self._col_maxoff = max(0, total_h - avail)
        self.col_scroll = max(0, min(self._col_maxoff, self.col_scroll))
        off = self._col_maxoff - self.col_scroll
        for kind, e, i in cells:
            if kind == "band":
                self._t(self.small, e, (cx, cy - off), self.GOLD)
                self.col_rects.append((pg.Rect(cx, cy - off, col_w, 20), i))
                cy += 20
                continue
            s = self.d.signs.get(e)
            top = cy - off
            cell_h = 0
            g = self.glyph(s, big=True) if s else None
            if g is not None:
                self.screen.blit(g, (cx + 6, top))
                top += g.get_height() + 6
                cell_h += g.get_height() + 6
            else:
                self.pg.draw.rect(self.screen, (58, 46, 20),
                                  (cx + 6, top + 2, 44, 44), 1)
                self._t(self.small, "drawn mark", (cx + 6, top + 50),
                        self.DIMC)
                top += 66
                cell_h += 66
            tag = "UNKNOWN" if (not s or not s.defined) else s.meaning
            col = self.REDC if (not s or not s.defined) else self.CYAN
            self._t(self.small, f"{e}  {tag[:38]}", (cx + 6, top), col)
            cell_h += 34
            self.col_rects.append(
                (pg.Rect(cx - 4, cy - off, col_w, cell_h), i))
            cy += cell_h
        # drop marker + dragged ghost
        if self.drag_sid and self.insert_i is not None and self.col_rects:
            gy = None
            for r, i in self.col_rects:
                if i == self.insert_i:
                    gy = r.top
                    break
            if gy is None:
                gy = self.col_rects[-1][0].bottom + 4
            pg.draw.line(self.screen, self.GOLD,
                         (cx, gy), (cx + col_w, gy), 3)
        if self.drag_sid:
            self._t(self.big, f"> {self.drag_sid}",
                    (self.mouse[0] + 8, self.mouse[1] - 8), self.GOLD)

        # RIGHT: story + strip
        rx = W_ - rp_w + 10
        ry = 64
        self._t(self.font, "THE STORY (auto)", (rx, ry), self.GOLD)
        ry += 22
        if self.roles:
            self._t(self.small, "STRIP: " + " > ".join(self.roles),
                    (rx, ry), self.DIMC)
            ry += 16
        if self.motif_notes:
            _, a, b, label, stories, _ = self.motif_notes[-1]
            self._t(self.small, f"GUESS PAIR: {a}+{b} ({label})",
                    (rx, ry), self.CYAN)
            ry += 14
            self._t(self.small, f"A: {stories[0][:44]}", (rx, ry), self.DIMC)
            ry += 14
            self._t(self.small, f"B: {stories[1][:44]}", (rx, ry), self.DIMC)
            ry += 16
        wrap_w = max(18, int((rp_w - 32) / 7))
        story_lines = []
        for t in self.story:
            for raw_ln in str(t).splitlines() or [""]:
                story_lines.extend(textwrap.wrap(raw_ln, wrap_w) or [""])
        iy = H - 92
        view_top = ry
        view_h = max(36, iy - 12 - view_top)
        self._story_scroll_max = max(0, len(story_lines) * 14 - view_h)
        self.scroll = max(0, min(self.scroll, self._story_scroll_max))
        viewport = pg.Rect(W_ - rp_w + 4, view_top, rp_w - 10, view_h)
        self._story_viewport = viewport
        old_clip = sc.get_clip()
        sc.set_clip(viewport)
        line_y = view_top - (self._story_scroll_max - self.scroll)
        for ln in story_lines:
            self._t(self.small, ln, (rx, line_y), self.INK)
            line_y += 14
        sc.set_clip(old_clip)
        if self._story_scroll_max:
            track = pg.Rect(W_ - 8, view_top, 4, view_h)
            pg.draw.rect(self.screen, (44, 35, 18), track)
            thumb_h = max(18, int(view_h * view_h /
                                  (view_h + self._story_scroll_max)))
            travel = max(1, view_h - thumb_h)
            frac = self.scroll / self._story_scroll_max
            thumb = pg.Rect(track.x, track.bottom - thumb_h -
                            int(frac * travel), track.width, thumb_h)
            pg.draw.rect(self.screen, self.GOLD, thumb)
        # input + suggestion chips / definition editor
        self._panel((8, iy - 8, W_ - 16, 58))
        if self.define_sid:
            prompt = f"DEFINE {self.define_sid} > {self.define_input}_"
            self._t(self.big, prompt, (18, iy + 22), self.GOLD)
            self._t(self.small,
                    "ENTER saves as this mark's primary personal meaning | ESC cancels",
                    (18, iy + 44), self.DIMC)
        else:
            self._t(self.big, "SEARCH > " + self.input + "_",
                    (18, iy + 22), self.INK)
        sx = 18
        for k, (score, s) in enumerate([] if self.define_sid else self.sugs):
            match = self._matched_def(s)
            w = self.small.size(f"{s.sid} {match[:22]}")[0] + 14
            col = self.GOLD if k == self.sel else self.DIMC
            self.pg.draw.rect(self.screen,
                              (58, 46, 20) if k == self.sel else self.PANEL,
                              (sx, iy - 2, w, 20))
            self._t(self.small, f"{s.sid} {match[:22]}", (sx + 6, iy + 2),
                    col)
            sx += w + 6
        if self.input:
            self._t(self.small,
                    f"definition matches {len(self.pal_view or []):,}",
                    (W_ - 240, iy + 44), self.DIMC)
        if self.sugs and not self.define_sid:
            sc_ = self.sugs[self.sel][0]
            self._t(self.small, f"match confidence {sc_:.0%}",
                    (W_ - 240, iy - 8), self.DIMC)

        if self.help_open:
            hw = min(560, W_ - 80)
            hx, hy = (W_ - hw) // 2, 58
            rr = pg.Rect(hx, hy, hw, 132)
            pg.draw.rect(self.screen, (24, 18, 9), rr)
            pg.draw.rect(self.screen, self.GOLD, rr, 2)
            help_lines = (
                "F1 INFO -- CORRECT A MARK MEANING",
                "1. Right-click a glyph in ALL MARKS.",
                "2. Click DEFINE <id>... and type your meaning.",
                "3. ENTER makes it the primary personal meaning and saves",
                "   egyptian_dialect.json, so it remains after relaunch.",
                "ESC cancels. Corrections are still hypotheses, not evidence.")
            for i, ln in enumerate(help_lines):
                self._t(self.small, ln, (rr.x + 14, rr.y + 12 + i * 18),
                        self.GOLD if i == 0 else self.INK)

    def run(self, frames=None):
        pg = self.pg
        clock = pg.time.Clock()
        n = 0
        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    return
                if ev.type == pg.VIDEORESIZE:
                    self.screen = pg.display.set_mode((ev.w, ev.h),
                                                      pg.RESIZABLE)
                elif ev.type == pg.KEYDOWN:
                    self._key(ev)
                elif ev.type == pg.MOUSEBUTTONDOWN:
                    self._mouse_down(ev.pos, ev.button)
                elif ev.type == pg.MOUSEBUTTONUP:
                    self._mouse_up(ev.pos, ev.button)
                elif ev.type == pg.MOUSEMOTION:
                    self.mouse = ev.pos
                    if self.split_drag:
                        self._resize_panes(ev.pos)
                    elif self.drag_sid:
                        self._drag_to(ev.pos)
                elif ev.type == pg.MOUSEWHEEL:
                    self._mouse_wheel(ev)
            self.render()
            pg.display.flip()
            clock.tick(30)
            n += 1
            if frames is not None and n >= frames:
                return


def launch_window(d, frames=None):
    """Open the interactive scribe window."""
    try:
        import pygame
    except ImportError:
        print("the scribe window needs pygame:  pip install pygame")
        return 1
    ui = ScribeUI(d)
    try:
        ui.run(frames=frames)
    except KeyboardInterrupt:
        print("scribe closed")
    finally:
        pygame.quit()
    return 0


# ==============================================================================
# SECTION 6 -- SELFTEST
# ==============================================================================

def selftest():
    fails = []
    def check(cond, msg):
        if not cond:
            fails.append(msg)
            print(f"  FAIL {msg}")
        else:
            print(f"  ok   {msg}")

    bar("SELFTEST")
    d = Dialect()

    total, defined, unknown = d.stats()
    _pua = len([s for s in d.signs.values() if s.sid.startswith("P-")])
    check(total == 1072 + 3995 + 48 + 128 + 96 + 32 + 32 + 14
          + 740 + 500 + 40 + 200 + 60 + 16 + len(VARIANT_SEED) + _pua,
          f"catalogue holds every recorded mark ({total:,} incl. "
          f"{_pua:,} ancient-signary PUA marks)")
    check(defined == len([r for r in ROSETTA_SPEC if r[4]])
          + len(ASSUMED_SEED)
          + sum(1 for s in ALT_SEED
                if s not in ASSUMED_SEED
                and s not in {r[0] for r in ROSETTA_SPEC if r[4]}),
          f"only rosetta seed + assumed readings are defined ({defined})")
    check(all(s.meaning == UNKNOWN for s in d.signs.values()
              if s.kind in ("sign", "mark")),
          "every recorded sign enters as UNKNOWN -- nothing borrowed")
    check(sum(1 for s in d.signs.values() if s.kind == "mark") == 48,
          "all 48 format-control marks catalogued")
    check(d.progress()["pictured_total"] == 1072 + 3995 + 18
          and d.signs["X-10980"].block == "Meroitic Hieroglyphs",
          "picture-script meter excludes other languages and layout controls")
    guesses = Dialect()
    guesses.define("N06", "my own reading of the slit")
    count = apply_picture_guesses(guesses, include_catalogue=False)
    check(count == len(PICTURE_GUESSES)
          and apply_picture_guesses(guesses, include_catalogue=False) == 0,
          "picture-first guesses load once and keep personal readings")
    check(guesses.signs["N06"].defs[0]["text"] == "my own reading of the slit"
          and guesses.signs["N06"].defs[1]["conf"] == CONF_GUESS,
          "guesses are labeled and cannot displace a user's primary sense")
    coverage = Dialect()
    apply_picture_guesses(coverage)
    check(coverage.progress()["pictured_proposed"]
          == coverage.progress()["pictured_total"]
          and coverage.progress()["pictured_verified"] == 0,
          "depiction/category scaffolds reach 100% proposal coverage without proof")
    fmt = language_format(coverage)
    check(fmt["ready"] == fmt["total"] and not fmt["missing_roles"]
          and fmt["multiuse"] == fmt["total"]
          and fmt["registers"].get("noun")
          and fmt["registers"].get("verb")
          and fmt["registers"].get("adj"),
          "proposal set carries multi-use noun/verb/adjective language roles")
    hist = [dd for dd in coverage.signs["N015"].defs
            if dd.get("scope") == HISTORICAL_GUESS_SCOPE]
    check(hist and "netherworld" in hist[0]["text"]
          and coverage.progress()["pictured_verified"] == 0,
          "historical semantic candidates load without external proof")
    texts = [dd["text"] for s in coverage.signs.values() for dd in s.defs]
    check(len(texts) == len(set(texts)),
          "every candidate definition is sign-specific, never duplicated")
    local = local_verification(coverage)
    check(local["verified_signs"] >= 10 and "N03" in local["verified_ids"]
          and coverage.progress()["pictured_verified"] == 0,
          "matrix/language logic locally corroborates without external proof")
    book = book_coherence(coverage)
    check(book["unique"] == 1 and book["coherent"] == 1
          and book["literary"] == 1 and book["entries"] == 16,
          "saved corpus renders as a coherent literary column")
    tx = english_to_egyptian(coverage,
                             "A fish sees water. A child sees rest.")
    check(len(tx["pages"]) == 2 and tx["mapped"] == 6
          and len(tx["mappings"]) == tx["mapped"] + tx["syntax"]
          and all(m["action"] in ("mapped", "syntax", "unmapped")
                  for m in tx["mappings"]),
          "English bridge writes glyphs while accounting for every token")
    coverage.undefine("A006")
    check(apply_catalogue_guesses(coverage) == 0,
          "catalogue-coverage scaffolds respect explicit clearing")
    check(guesses.progress()["verified"] == 0
          and "UNKNOWN" not in read_column(
              guesses, guesses.rosetta_column, show=False)[5],
          "guessed slit produces a candidate story, not verified progress")
    ctx_a = read_column(coverage, ["K001", "D004", "N005", "D055"],
                        show=False)
    ctx_b = read_column(coverage, ["K001", "X002", "V030", "D055"],
                        show=False)
    repeat_ctx = read_column(coverage, ["N08", "N01", "N08", "D055"],
                             show=False)
    check("NOTE:" in ctx_a[3] and "sun <" in ctx_a[3]
          and "basket <" in ctx_b[3] and ctx_a[3] != ctx_b[3]
          and "same mark elsewhere #3" in repeat_ctx[0]
          and "same mark elsewhere #1" in repeat_ctx[2],
          "AUTO story notes neighbor-relative meaning per occurrence")
    base_pos = _positions(coverage, ["A021", "V001C", "A056"])
    add_pos = _positions(coverage, ["D004", "A021", "V001C", "A056"])
    base_pick = _select(coverage, base_pos)
    add_pick = _select(coverage, add_pos)
    check(coverage.signs["A021"].defs[base_pick[0]]["text"] !=
          coverage.signs["A021"].defs[add_pick[1]]["text"],
          "inserting a picture changes a neighboring selected meaning")
    water_pairs = motif_matches(["K001", "N035"])
    basket_pairs = motif_matches(["K001", "V030"])
    check([m[3] for m in water_pairs] == ["fish+water"]
          and [m[3] for m in basket_pairs] == ["fish+basket"],
          "picture compounds depend on the adjacent object")
    check([m[3] for m in motif_matches(["N020", "N035"])] == ["shore+water"],
          "local pictured shore and water descriptions compose without a phonetic lookup")
    check(len(motif_matches(guesses.rosetta_column)) >= 6
          and all(len(m[4]) == 2 for m in water_pairs + basket_pairs),
          "real seed column triggers competing, explicitly labeled stories")
    guesses.columns["copy"] = list(guesses.rosetta_column)
    check(motif_counts(guesses)[("N01", "N02", "fish+water")] == 1
          and guesses.progress()["verified"] == 0
          and not guesses.corr.w,
          "copied motif matches neither reinforce the matrix nor prove uses")
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        old_path = os.path.join(td, "legacy.json")
        with open(old_path, "w", encoding="utf-8") as f:
            json.dump({"version": 3, "definitions": {
                "K001": {"defs": [], "note": "", "depicts": "fish"},
                "N06": {"defs": [], "note": "", "depicts": "slit"},
                "N08": {"defs": [], "note": "", "depicts": "bird"},
            }}, f)
        old = Dialect()
        apply_picture_guesses(old)
        old.load(old_path)
        check(len(old.signs["K001"].defs) >= 4
              and len(old.signs["N06"].defs) >= 4
              and not old.signs["N08"].defs,
              "v3 empty entries do not erase new guesses; cleared seed stays clear")
        old_seed_path = os.path.join(td, "old-seed.json")
        with open(old_seed_path, "w", encoding="utf-8") as f:
            json.dump({"version": 3, "definitions": {
                "N09": {"defs": [{"text": d.signs["N09"].meaning,
                                   "src": "Nathan -- Rosetta base column",
                                   "conf": CONF_LIKELY}]}},
                       "clusters": {}}, f)
        old_seed = Dialect()
        old_seed.load(old_seed_path)
        check(old_seed.signs["N09"].defs[0]["conf"] == CONF_GUESS,
              "old built-in Rosetta confidence migrates to guess")
        endorsed = Dialect()
        endorsed.likely("N09", 1)
        endorsement_path = os.path.join(td, "endorsed.json")
        endorsed.save(endorsement_path)
        reloaded_endorsement = Dialect()
        reloaded_endorsement.load(endorsement_path)
        check(reloaded_endorsement.signs["N09"].defs[0]["conf"] == CONF_LIKELY,
              "a saved personal endorsement remains an endorsement")
        guesses.undefine("N06")
        guesses.undefine("K001", 1)
        path = os.path.join(td, "personal.json")
        guesses.save(path)
        with open(path, encoding="utf-8") as f:
            saved = json.load(f)
        reloaded = Dialect()
        apply_picture_guesses(reloaded)
        reloaded.load(path)
        removed = set(saved["removed_guesses"]["K001"])
        check(saved["version"] == 4
              and len(saved["definitions"]) < 100
              and not reloaded.signs["N06"].defs
              and reloaded.signs["K001"].defs
              and all(dd["text"] not in removed
                      for dd in reloaded.signs["K001"].defs),
              "compact v4 save preserves explicit clearing and single-use removal")
        check(reloaded.progress()["verified"] == 0,
              "restored hypotheses never count as independent observations")
    n_signs = [s for s in d.signs.values() if s.kind == "rosetta"]
    check(len(n_signs) == 16 + len(VARIANT_SEED),
          "rosetta set = 16 column signs + species variants")
    check(sum(1 for s in n_signs if not s.defined) == 1 + len(VARIANT_SEED),
          "3 rosetta signs left UNKNOWN (slit + bird variants)")
    check(d.signs["N17"].depicts == "bird" and not d.signs["N17"].defined
          and d.signs["N17"].defs != d.signs["N08"].defs,
          "bird variant: same object name, own unknown uses")
    check(d.signs["N05"].defs[0].get("conf") == CONF_ASSUMED
          and "bait" in d.signs["N05"].defs[0]["text"],
          "snail-thing reads as the bait -- assumed from the scale")
    check(d.signs["N12"].defs[0].get("conf") == CONF_ASSUMED
          and "SOLD" in d.signs["N12"].defs[0]["text"],
          "scale reading: goods lifted to a scale = SOLD, assumed")

    # reader: order top->down, brackets -> proverb, unknown marked
    story = read_column(d, d.rosetta_column, show=False)
    check(story[0].startswith("A FISH OUT OF WATER"),
          "column reads top-to-bottom (fish first)")
    check(story[-1].startswith("laid down"),
          "column ends at the bottom (rest last)")
    check(sum("UNKNOWN" in t for t in story) == 1,
          "unread marks surface as UNKNOWN in the story")

    seg = _section_segment(d.rosetta_column, 5, 10)
    check("[" in seg and "]" in seg and "N08" in seg and "N09" in seg,
          "condensed proverb group (bird+strokes) preserved in section 2")

    # define / undefine / persist
    d.define("N06", "a snail -- something slow carried along")
    check(d.signs["N06"].defined, "define() claims a meaning")
    d.undefine("N06")
    check(not d.signs["N06"].defined, "undefine() returns to UNKNOWN")
    d.define("A001", "test mark")
    tmp = os.path.join(os.path.dirname(DIALECT_FILE), "_st_dialect.json")
    d.save(tmp)
    d2 = Dialect()
    check(d2.load(tmp), "dialect file round-trips")
    check(d2.signs["A001"].meaning == "test mark",
          "personal definitions persist across load")
    check(bool(d2.cluster_for(["N09", "N08"])),
          "seed cluster survives the save/load round-trip")
    d2.undefine("A001")
    try:
        os.remove(tmp)
    except OSError:
        pass

    # Polysemy is not arbitrarily limited to ten senses.
    d.define("N17", "a snail -- the slow load you carry")
    d.define("N17", "a coil -- rope wound for the work")
    check(len(d.signs["N17"].defs) == 2,
          "sign holds multiple candidate readings")
    for k in range(12):
        d.define("N17", f"filler reading {k}")
    check(len(d.signs["N17"].defs) == 14,
          "candidate readings can exceed ten")
    d.undefine("N17")
    check(not d.signs["N17"].defined,
          "undefine drops all candidate readings")

    # Machine predictions and repeated teaching do not count as evidence.
    check(d.progress()["verified"] == 0,
          "seed proposals are not independent decipherment")
    original_pairs = len(d.observed_pairs().get(("N01", "N02"), set()))
    d.columns["ref1a"] = ["N01", "N02", "N08"]
    d.columns["ref1copy"] = ["N01", "N02", "N08"]
    d.columns["ref2a"] = ["N01", "N03", "N08"]
    check("attested" in d.attest("Reference1.png", "ref1a", "N01", 1),
          "manual source + column + sense recorded")
    d.attest("Reference1.png", "ref1copy", "N01", 1)
    check(d.progress()["verified"] == 0,
          "copies of the same column are not independent")
    d.attest("Reference2.png", "ref2a", "N01", 1)
    check(d.progress()["verified"] == 1,
          "matching use in two different columns advances progress")
    check(len(d.observed_pairs()[("N01", "N02")]) == original_pairs + 1,
          "copied columns cannot inflate glyph-pair counts")
    before = d.learn_column(d.columns["ref1a"])
    check(before > 0 and d.learn_column(d.columns["ref1copy"]) == 0,
          "re-teaching a duplicate column cannot inflate matrix")
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "audit.json")
        d.save(path)
        restored = Dialect()
        restored.load(path)
        check(restored.progress()["verified"] == 1
              and restored.taught == d.taught,
              "evidence and deduplication survive save/load")
        restored.columns["ref2a"].append("N09")
        check(restored.progress()["verified"] == 0,
              "editing an attested column invalidates its old evidence")
        export_path = os.path.join(td, "guesses.txt")
        do_export(guesses, path=export_path)
        with open(export_path, encoding="utf-8") as f:
            export_text = f.read()
        check("ADJACENT PICTURE COMPOUNDS" in export_text
              and "PHOTO SHAPE FRAGMENTS" in export_text
              and "[guess/" in export_text,
              "export retains labeled guesses, compounds, and photo notes")
        try:
            from PIL import Image
            import numpy as np
            tile = Image.open(os.path.join(TILE_DIR, "K001.png")).convert("RGBA")
            ink = np.asarray(tile)[:, :, 3] > 64
            hits = _match_ink(d, ink, 1)
            check(hits and hits[0]["sid"] == "K001",
                  "image matcher ranks an exact tile candidate first")
            photo = Image.new("RGB", (160, 160), "white")
            photo.paste(tile, (20, 20), tile)
            photo_path = os.path.join(td, "scan.png")
            photo.save(photo_path)
            rec = transcribe_image(d, photo_path, "st-scan",
                                   manual_cells=[(15, 15, 145, 145)])
            check(rec["status"] == TRANSCRIPTION_CANDIDATE
                  and rec["cell_source"] == "manual-bbox"
                  and any(m["sid"] == "K001"
                          for m in rec["columns"][0]["entries"][0]["matches"]),
                  "image transcription starts as review candidates, not evidence")
            check("human reviewed" in pick_transcription(d, "st-scan", 1, "K001")
                  and "needs separate attest" in approve_transcription(
                      d, "st-scan", "scan-col")
                  and d.columns["scan-col"] == ["K001"]
                  and not d.evidence().get("K001"),
                  "approved image transcription persists without evidence")
            review_path = os.path.join(td, "review-dialect.json")
            d.save(review_path)
            reviewed = Dialect(); reviewed.load(review_path)
            check(reviewed.transcriptions["st-scan"]["status"]
                  == TRANSCRIPTION_REVIEWED
                  and reviewed.columns["scan-col"] == ["K001"],
                  "transcription review survives save/load")
            del d.columns["scan-col"]
            d.transcriptions.pop("st-scan", None)
        except ImportError:
            check(True, "image review skipped -- pillow/numpy/opencv absent")
    for name in ("ref1a", "ref1copy", "ref2a"):
        del d.columns[name]
    d.attestations.clear()

    # A user may promote a guess; built-in proposals never self-endorse.
    check(all(dd.get("conf") in (CONF_GUESS, CONF_ASSUMED)
              for s in d.signs.values() if s.kind == "rosetta"
              for dd in s.defs),
          "every seed reading carries a confidence flag")
    check(sum(1 for s in d.signs.values() if s.kind == "rosetta"
              for dd in s.defs if dd.get("conf") == CONF_GUESS) == 12,
          "12 seed readings flagged as guesses, not established facts")
    check(sum(1 for s in d.signs.values() if s.kind == "rosetta"
              for dd in s.defs if dd.get("conf") == CONF_ASSUMED)
          == len(ASSUMED_SEED) + len(ALT_SEED),
          "assumed readings flagged (bait, scale, pocket, harvest, pickup)")
    check("is the bird" in d.signs["N08"].defs[0]["text"].lower()
          or "is the bird" in ROSETTA_STORY.lower(),
          "bird proverb recorded as metaphor (the writer IS the bird)")

    # double meanings: one reading, two co-valid senses
    check("also" in d.signs["N09"].defs[0],
          "N09 crossing seeded with a double sense (to-and-fro sale)")
    d9 = d.signs["N09"].defs[0]
    check("too good" in (d9["text"] + d9.get("also", "")),
          "double sense says the fishing was too good to need bait")
    st_dbl = read_column(d, ["N08", "N09"], show=False)
    check(any("also:" in t for t in st_dbl),
          "double sense surfaces in the story")

    # clusters: a circled group reads as ONE whole proverb (chengyu-style)
    check(d.cluster_for(["N08", "N09"]),
          "bird+crossing cluster is seeded")
    check(d.cluster_for(["N09", "N08"]),
          "cluster matches regardless of member order")
    c23 = d.cluster_for(["N03", "N08"])
    check(c23 and "GOING TO SEE" in c23["defs"][0]["text"]
          and c23["defs"][0].get("mode") == "evolved",
          "bird+eye (no distance-marks) = 'going to see' -- short trip")
    st_c = read_column(d, ["[", "N08", "N09", "]"], show=False)
    check(any("cluster:" in t for t in st_c),
          "known cluster enters the story as a whole proverb")
    d.define_cluster(["N01", "N02"], "fish in the river -- the whole setting")
    check(d.cluster_for(["N02", "N01"])["defs"][0]["text"].startswith("fish"),
          "define_cluster works and matches unordered")
    d.drop_cluster(["N01", "N02"])
    check(not d.cluster_for(["N01", "N02"]), "uncluster removes it")

    # evolved clusters: same ring, several whole-paragraph readings
    rec = d.cluster_for(["N08", "N09"])
    check(rec["defs"][0].get("mode") == "evolved",
          "seed cluster tagged 'evolved' (ring != meaning)")
    check(rec.get("depicts"), "seed cluster records what it depicts")
    d.define_cluster(["N08", "N09"], "a penned bird -- eggs for the morning")
    check(len(rec["defs"]) == 2,
          "cluster holds multiple whole-proverb readings")
    di = _cluster_pick(d, rec, ["N08", "N09"],
                       _positions(d, ["N08", "N09", "N16"]),
                       {0: 0, 1: 0, 2: 0})
    check(0 <= di < len(rec["defs"]),
          "cluster pick resolves a reading from context")
    rec["defs"].pop()

    # evolved dialect: depiction is the mask, not the meaning
    check(d.signs["N08"].depicts == "bird",
          "sign records its literal depiction apart from meaning")
    check(d.signs["N08"].defs[0].get("mode") == "evolved",
          "bird reading tagged 'evolved' (image != meaning)")
    check(d.signs["N16"].defs[0].get("mode") == "action",
          "stick-figure readings tagged 'action'")
    d.mode("N07", 1, "evolved")
    check(d.signs["N07"].defs[0].get("mode") == "evolved",
          "mode command tags a candidate reading")
    d.signs["N07"].defs[0].pop("mode")
    # meme-strip functions: what the mark DOES, not what it draws
    check(d.signs["N08"].defs[0].get("func") == "act-travel",
          "bird reading carries its strip function (travel)")
    d.define("N17", "a coil -- wound rope")
    d.func("N17", 1, "object")
    check(d.signs["N17"].defs[0].get("func") == "object",
          "func command tags a candidate's role")
    d.undefine("N17")

    # flexibility: readings note register + terminology flex + concreteness
    check(d.signs["N01"].defs[0].get("reg") == "adj+verb",
          "fish-out-of-water seeded as adj+verb register")
    check("basket" in d.signs["N01"].defs[0].get("flex", ""),
          "flex note: fish+basket would read differently")
    d.define("N17", "a slippery thing -- hard to hold")
    d.reg("N17", 1, "adj")
    check(d.signs["N17"].defs[0].get("reg") == "adj",
          "reg command tags register")
    d.flex("N17", 1, "bends to whatever is wet beside it")
    check("wet" in d.signs["N17"].defs[0].get("flex", ""),
          "flex command notes terminology dependency")
    d.concrete("N17", 1)
    check(d.signs["N17"].defs[0].get("concrete") is True,
          "concrete flags a locked reading")
    d.concrete("N17", 1)
    check("concrete" not in d.signs["N17"].defs[0],
          "concrete toggles back to flexible")
    d.undefine("N17")
    d.depict("K001", "a fish, sideways")
    check(d.signs["K001"].depicts == "a fish, sideways",
          "depict records the literal image for cross-reference")
    d.signs["K001"].depicts = None
    d.signs["K001"].depicts = "EGYPTIAN HIEROGLYPH K001"  # restored

    # the correlation engine: column context picks the right candidate
    d.define("N06", "a net full of fish -- the river catch")
    d.define("N06", "a tower on a mountain -- the high fortress")
    d.likely("N06", 1)
    check(d.signs["N06"].defs[0].get("conf") == CONF_LIKELY,
          "likely command flags a candidate reading")
    d.double("N06", 1, "a sold surplus -- the market gain")
    check(d.signs["N06"].defs[0].get("also")
          and {"market", "gain"} <= _dtokens(d.signs["N06"].defs[0]),
          "double adds a second sense the engine can score")
    d.scratch = ["N01", "N02", "N06", "N11"]
    st = read_column(d, d.scratch, show=False)
    check("fish" in st[2],
          "context chooses the river-reading over the fortress")

    # pattern recognition: position + slot grammar influence the pick
    d.define("N17", "a scene-setting mark")
    d.define("N17", "the day's ending mark")
    d.func("N17", 1, "proverb-opener")
    d.func("N17", 2, "rest")
    d.scratch = ["N17", "N02", "N11"]
    st2 = read_column(d, d.scratch, show=False)
    check("scene-setting" in st2[0],
          "positional prior: opener role wins at column head")
    d.scratch = ["N02", "N11", "N17"]
    st3 = read_column(d, d.scratch, show=False)
    check("ending" in st3[2],
          "positional prior: rest role wins at column tail")
    d.undefine("N17")

    # learning: endorsing a column reinforces the matrix
    before = sum(len(m) for m in d.corr.w.values())
    d.learn_column(d.scratch)
    check(sum(len(m) for m in d.corr.w.values()) > before,
          "keep/teach reinforces chosen reading pairs in the matrix")
    check(bool(d.corr.top()), "matrix yields correlation pairs")
    d.undefine("N06")
    d.scratch = []

    # cross-reference wiring: our drawn sign <-> recorded shelf mark
    check(d.signs["N01"].xref == ["K001"], "N01 fish xref -> K001")
    check("N01" in d.signs["K001"].xref, "K001 back-links to N01")
    check(not d.signs["K001"].defined,
          "xref does not leak a meaning onto the recorded sign")
    check(d.signs["K001"].cp == 0x1319B and d.signs["K001"].block,
          "every recorded sign carries its codepoint + block")
    check(all(s.depicts for s in d.signs.values()),
          "every mark named what it IS -- depicts, not used-meanings")

    # compose path sanity
    d.scratch = ["N01", "[", "N08", "N09", "]", "N16"]
    st = read_column(d, d.scratch, show=False)
    check(len(st) == 5 and st[3].startswith("<< cluster:"),
          "scratch column reads in order, cluster proverb inline")

    # pages: columns consumed left->right, each its own record
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        page(d, ["rosetta"])
    check("record 'rosetta'" in buf.getvalue() and "COLUMN 1" in buf.getvalue(),
          "page reads columns left->right as separate records")

    # identity: mark is its depiction until placed; defs are its USES
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        read_column(d, ["N08"])
    rtxt = buf.getvalue()
    check("bird" in rtxt and "(as itself" in rtxt,
          "lone single-use mark renders as its depiction only")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        read_column(d, ["[", "N08", "N09", "]"])
    check(":=" in buf.getvalue(),
          "in context the usage speaks (depicts := usage)")

    # the shaped cross-reference sheet
    with tempfile.TemporaryDirectory() as td:
        p = chart(d, path=os.path.join(td, "catalog.html"))
        with open(p, encoding="utf-8") as f:
            body = f.read()
    check("K001" in body and "N01" in body and "VERTICAL-JOINER" in body,
          "html chart contains rosetta signs, recorded signs and marks")
    check('src="glyphs' in body or "src='glyphs" in body
          or 'src="glyphs/' in body,
          "html chart draws authentic tile images")

    # every mark carries a real image tile -- no tofu, no empty cells
    if os.path.isdir(TILE_DIR):
        have = {fn[:-4] for fn in os.listdir(TILE_DIR)
                if fn.endswith(".png") and ".alt" not in fn}
        missing = [s.sid for s in d.signs.values() if s.sid not in have]
        check(not missing,
              f"all {len(d.signs)} marks have a digital symbol "
              f"(missing: {missing[:6]})")
        try:
            import numpy as _np
            from PIL import Image as _Im
            def _ink(fp):
                return (_np.asarray(_Im.open(fp).convert('RGBA'))[:, :, 3]
                        > 0).mean()
            empty = [s.sid for s in d.signs.values()
                     if _ink(os.path.join(TILE_DIR, s.sid + ".png"))
                     < 0.001]
            tofu = [s.sid for s in d.signs.values()
                    if _tile_is_tofu(os.path.join(TILE_DIR, s.sid + ".png"))]
            check(not empty and not tofu,
                  f"all {len(d.signs)} tiles carry non-box ink "
                  f"(empty: {empty[:4]}, tofu: {tofu[:4]})")
        except ImportError:
            check(True, "tile ink probe skipped -- numpy/pillow absent")

    # the scribe window: launches headless, autocorrect repairs spelling
    try:
        os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
        ui = ScribeUI(d, headless=True)
        ui.set_input("travel")
        check(ui.sugs and ui.sugs[0][1].sid == "N08",
              "autocomplete finds 'travel' -> the bird sign")
        ui.set_input("fihs")
        check(ui.sugs and ui.sugs[0][1].sid == "N01",
              "autocorrect repairs misspelling 'fihs' -> the fish sign")
        check(ui.sugs[0][1].defined and
              "fish" in ui._matched_def(ui.sugs[0][1]).lower(),
              "search ranks and labels the usable definition")
        ui.press("ENTER")
        check(d.scratch and d.scratch[-1] == "N01",
              "ENTER writes the corrected sign into the column")
        ui.type_char("[")
        check(d.scratch[-1] == "[",
              "bracket keys open a condensed cluster in the window")
        ui.d.scratch += ["N08", "N09", "]"]
        ui.refresh_story()
        check(any("cluster" in t.lower() for t in ui.story),
              "window story renders the cluster proverb live")
        ui.run(frames=3)
        check(True, "scribe window launches and renders frames")
        # real glyph images -- tiles first, fonts as fallback
        ui.glyph(d.signs["N08"])              # the carved bird tile
        ui.glyph(d.signs["N06"])              # the carved slit tile
        check(True, "glyph() renders authentic images, never ASCII art")
        check(ui.glyph_variants(d.signs["X-13460"]),
              "extended-A marks have an authentic recorded shape")
        check(all(ui.glyph(d.signs[f"N{i:02d}"]) is not None
                  for i in range(1, 19)),
              "every seed mark renders the real carved mark")
        # glyphs-first writing: drag marks in, drop at a position, reorder
        check(len(ui.palette_all) == len(d.signs),
              "palette lists EVERY mark incl. UNKNOWN, not just defined")
        page_view, view, pages = ui._pal_page_view()
        check(len(view) == len(d.signs) and pages == 21
              and len(page_view) == ui.PAL_PAGE_SIZE,
              "ALL MARKS uses 21 pages of 500 marks")
        ui.pal_page = pages - 1
        page_view, view, pages = ui._pal_page_view()
        check(len(page_view) == len(d.signs) % ui.PAL_PAGE_SIZE,
              "final ALL MARKS page holds the remainder")
        ui.pal_page = 0
        ui.lp_w = 500
        ui.render()
        check(ui._pal_cols >= 7 and ui._pal_glyph_size > 39,
              "widening marks pane rescales glyph tiles")
        sep_x, sep_y = ui.lp_w, 100
        ui._mouse_down((sep_x, sep_y))
        check(ui.split_drag == "marks",
              "marks separator begins a resize drag")
        ui._resize_panes((420, sep_y))
        ui._mouse_up((420, sep_y), 1)
        check(ui.lp_w == 420 and ui.split_drag is None,
              "marks separator resizes and releases cleanly")
        ui.lp_w = 300
        ui.render()
        genre_btn = next(r for r, a in ui.pal_nav_rects if a == "genre")
        ui._mouse_down(genre_btn.center)
        check(ui.genre_open, "GENRE button opens a dropdown")
        ui.render()
        check(len(ui.genre_rects) == len(ui.pal_genres)
              and sum(n for g, n in ui.pal_genre_counts.items()
                      if g != "ALL") == len(d.signs),
              "GENRE dropdown lists every genre with a count")
        ui._mouse_down(ui.genre_rects[1][0].center)
        page_view, view, pages = ui._pal_page_view()
        check(ui.pal_genre_i == 1 and not ui.genre_open
              and len(view) == ui.pal_genre_counts[
                  ui.pal_genres[1]],
              "GENRE selection filters marks and shows its count")
        ui._pal_genre_pick(0)
        ui.drag_sid, ui.drag_from = "N16", None
        ui.insert_at(0, "N16")
        check(d.scratch[0] == "N16", "drop inserts a mark into the column")
        ui.drag_sid, ui.drag_from = "N16", 0
        ui.insert_i = len(d.scratch)
        ui._mouse_up((400, 700), 1)
        check(d.scratch[-1] == "N16",
              "drag reorders a mark within the column")
        pg2 = ui.pg
        ui.col_rects = [(pg2.Rect(310, 100, 200, 40), 0)]
        ui._mouse_up((320, 110), 3)
        check(d.scratch[0] != "N16",
              "right-click lifts a mark out of the column")
        ui.story = ["story line %02d " + "long text " * 20
                    for i in range(80)]
        ui.roles = []
        ui.motif_notes = []
        ui.scroll = 0
        ui.render()
        input_top = ui.screen.get_height() - 100
        check(ui._story_scroll_max > 0
              and ui._story_viewport.bottom <= input_top,
              "story viewport scrolls without entering the search bar")
        ui.mouse = (ui.screen.get_width() - 10, 120)
        ev = type("Wheel", (), {"y": 1})()
        ui._mouse_wheel(ev)
        check(ui.scroll > 0, "mouse wheel scrolls the story pane upward")
        ev = type("Wheel", (), {"y": -999})()
        ui._mouse_wheel(ev)
        check(ui.scroll == 0,
              "mouse wheel returns the story to the latest lines")
        ui.scroll = ui._story_scroll_max + 999
        ui.render()
        check(ui.scroll == ui._story_scroll_max,
              "story scroll clamps to its oldest line")
        ui.press("F1")
        check(ui.help_open, "F1 toggles the definition-help panel")
        ui.press("F1")
        check(not ui.help_open, "F1 closes the definition-help panel")
        ui.pal_view = ["K001"]
        ui.pal_page = ui.pal_scroll = 0
        ui.render()
        cell = next(r for r, sid in ui.pal_cells if sid == "K001")
        ui._mouse_down(cell.center, 3)
        check(ui.def_menu and ui.def_menu[2] == "K001",
              "right-click opens the palette DEFINE menu")
        ui.render()
        ui._mouse_down(ui.def_menu_rect.center, 1)
        check(ui.define_sid == "K001",
              "DEFINE menu enters corrective-definition mode")
        for ch in "ui fish correction":
            ui.type_char(ch)
        with tempfile.TemporaryDirectory() as td:
            ui.dialect_file = os.path.join(td, "ui-dialect.json")
            ui.press("ENTER")
            check(ui.define_sid is None
                  and ui.d.signs["K001"].defs[0]["text"]
                  == "ui fish correction"
                  and os.path.exists(ui.dialect_file),
                  "ENTER saves the palette correction as primary")
            reloaded_ui = Dialect()
            apply_picture_guesses(reloaded_ui)
            reloaded_ui.load(ui.dialect_file)
            check(reloaded_ui.signs["K001"].defs[0]["text"]
                  == "ui fish correction",
                  "palette correction remains primary after relaunch/load")
        ui.pg.quit()
        d.scratch = []
    except ImportError:
        check(True, "pygame absent -- window test skipped")
    check(all(w in DIALECTS_TEXT for w in
              ("PROTO-EGYPTIAN", "OLD EGYPTIAN", "MIDDLE EGYPTIAN",
               "LATE EGYPTIAN", "DEMOTIC",
               "BOHAIRIC", "SAHIDIC", "FAYYUMIC", "AKHMIMIC", "LYCOPOLITAN",
               "OXYRHYNCHITE", "BASHMURIC", "MEROITIC", "OLD NUBIAN")),
          "every documented Egyptian dialect/stage is registered")

    bar("RESULT")
    if fails:
        print(f"{RED}{len(fails)} failure(s){RESET}")
        return 1
    print(f"{GREEN}all checks passed -- the dialect engine is sound{RESET}")
    return 0

# ==============================================================================
# SECTION 6b -- AUTHENTIC GLYPH TILES
# ==============================================================================
# Every mark gets a visible digital symbol. Encoded signs use real ink
# cropped cell-for-cell from the official Unicode code charts; PUA marks
# use Aegyptus ink; the 18 seed marks use the supplied annotated picture
# (ReferenceDialect/Rosetta.png), not an authenticated museum stone.
# Unencoded series receive deterministic pictorial slot glyphs so no
# catalogue cell renders as a missing-glyph box.
# Facing is preserved exactly -- the
# carved column reads right-to-left and its marks keep that orientation;
# direction carries meaning and is never mirrored away.

TILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "glyphs")
TILE_W, TILE_H = 120, 120            # transparent glyph-only tile
_PARCH = (245, 238, 222)             # parchment
_INK = (148, 116, 58)                # carved-gold ink
_EDGE = (190, 160, 100)              # border / label

CHART_PDFS = [
    # (block, lo, hi, local file, url)
    ("Egyptian Hieroglyphs", 0x13000, 0x1342F, "U13000_chart.pdf",
     "https://www.unicode.org/Public/latest/charts/PDF/U13000.pdf"),
    ("Hieroglyph Format Controls", 0x13430, 0x1345F, "U13430_chart.pdf",
     "https://www.unicode.org/Public/latest/charts/PDF/U13430.pdf"),
    ("Egyptian Hieroglyphs Extended-A", 0x13460, 0x143FA,
     "U13460_chart.pdf",
     "https://www.unicode.org/Public/latest/charts/PDF/U13460.pdf"),
]

# Seed marks -> ink run in the pictured column (y-range in Rosetta.png).
# Visually identified in the supplied crop: the dome fish, the double
# bank-line river, the standing slug, the hatched platform, the
# right-facing bird, the paired to-and-fro marks, the stride, the
# awning on poles, the plant on a stem. Two marks side by side remain
# separate observations, not fixed readings.
SEED_SEGMENTS = {
    "N01": (16, 77),    # fish dome -- something out of place
    "N02": (80, 114),   # river -- one river, both its banks
    "N03": (250, 272),  # the eye over the water
    "N04": (119, 177),  # the man at the shore
    "N05": (184, 247),  # the slug -- partly standing, eyes extended
    "N06": (325, 337),  # the slit mark
    "N07": (284, 313),  # the hatched foundation
    "N08": (344, 413),  # the bird -- faces right, as carved
    "N09": (415, 471),  # the paired to-and-fro marks
    "N10": (473, 563),  # the stride
    "N11": (574, 638),  # the yield on its stand
    "N12": (724, 760),  # the small box
    "N13": (767, 792),  # the slip
    "N14": (651, 717),  # the awning on poles -- the shade
    "N15": (869, 939),  # the plant on a stem
    "N16": (800, 863),  # the rest mark
    # species variants (not in the supplied crop): catalogued signs
    "N17": "G026",      # ibis on standard -- a different bird kind
    "N18": "G014",      # vulture -- another bird kind
}

ROSETTA_COL = (6, 89)                # carved column x-range in the image
                                     # (x>=89 is the register border)


def _build_deps():
    try:
        import fitz                                     # noqa: F401
        import fontTools.ttLib                          # noqa: F401
        from PIL import (Image, ImageDraw, ImageFont,   # noqa: F401
                         ImageChops, ImageOps, ImageEnhance)
    except ImportError as e:
        raise SystemExit(
            f"build needs pymupdf + pillow: pip install pymupdf pillow "
            f"({e})")


def _chart_get(url, path):
    if not os.path.exists(path):
        import urllib.request
        print(f"  fetching {url}")
        urllib.request.urlretrieve(url, path)


def _hex_labels(page):
    """Text tokens that are pure 4-5 digit hex (codepoint labels)."""
    d = page.get_text("rawdict")
    chars = []
    for block in d["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                if "Hieroglyph" in span["font"] or "Specials" in span["font"]:
                    continue
                for ch in span["chars"]:
                    chars.append((ch["c"], list(ch["bbox"])))
    chars.sort(key=lambda L: (L[1][1], L[1][0]))
    toks = []
    for c, bb in chars:
        if (toks and abs(toks[-1][1][1] - bb[1]) < 4
                and abs(bb[0] - toks[-1][1][2]) < 6):
            b = toks[-1][1]
            b[0] = min(b[0], bb[0]); b[2] = max(b[2], bb[2])
            b[3] = max(b[3], bb[3])
            toks[-1][0] += c
        else:
            toks.append([c, bb])
    out = []
    for text, bb in toks:
        t = "".join(text)
        if 4 <= len(t) <= 5 and all(c in "0123456789ABCDEF" for c in t):
            out.append((t, bb))
    return out


def _chart_cells(doc, lo, hi):
    """{cp: (page, cell_rect)} -- locate every labelled sign cell in a
    chart PDF. Grid rows are lines of >=4 hex labels at an even pitch;
    the sign sits in the cell space directly above its label."""
    import fitz
    cells = {}
    for pno in range(doc.page_count):
        labels = _hex_labels(doc[pno])
        rows = {}
        for t, bb in labels:
            rows.setdefault(round(bb[1] / 4), []).append((t, bb))
        rows = [sorted(r, key=lambda x: x[1][0])
                for r in rows.values() if len(r) >= 4]
        if not rows:
            continue
        tops = sorted(min(b[1] for _t, b in r) for r in rows)
        rpitch = (sorted(tops)[-1] - sorted(tops)[0]) / max(1, len(tops) - 1)
        if not (10 < rpitch < 60):
            rpitch = 39.6
        for row in rows:
            xs = [(b[0] + b[2]) / 2 for _t, b in row]
            cpitch = (xs[-1] - xs[0]) / (len(row) - 1) if len(row) > 1 \
                else 28.0
            for t, bb in row:
                cp = int(t, 16)
                if not (lo <= cp <= hi):
                    continue
                cx = (bb[0] + bb[2]) / 2
                rect = fitz.Rect(cx - cpitch / 2 + 1,
                                 bb[1] - rpitch + 8,
                                 cx + cpitch / 2 - 1,
                                 bb[1] - 1.5)
                cells[cp] = (pno, rect)
    return cells


def _ink_crop(img, pad=6):
    """Trim a page render to its ink bounds."""
    from PIL import ImageChops
    g = img.convert("L")
    mask = g.point(lambda p: 255 if p < 210 else 0)
    bbox = mask.getbbox()
    if not bbox:
        return None
    l, t, r, b = bbox
    l = max(0, l - pad); t = max(0, t - pad)
    r = min(img.width, r + pad); b = min(img.height, b + pad)
    return img.crop((l, t, r, b))


def _tile_font(size):
    from PIL import ImageFont
    for f in ("consola.ttf", "cour.ttf", "DejaVuSansMono.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _compose_tile(ink_img, sid, mark=None):
    """Transparent 120x120 glyph tile with the source ink recolored gold."""
    from PIL import Image, ImageChops
    tile = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    if ink_img is not None:
        im = ink_img.copy()
        im.thumbnail((TILE_W - 22, TILE_H - 22), Image.LANCZOS)
        alpha = (im.getchannel("A") if im.mode == "RGBA"
                 else ImageChops.invert(im.convert("L")).point(
                     lambda p: min(255, int(p * 1.45))))
        gold = Image.new("RGBA", im.size, _INK + (255,))
        tile.paste(gold, ((TILE_W - im.width) // 2,
                          (TILE_H - im.height) // 2), alpha)
    elif mark is not None:
        tile = mark
    return tile


def _chart_tiles(d, out):
    """Crop every encoded sign straight off the official code charts.
    Returns the set of sids written."""
    import fitz
    from PIL import Image
    base = os.path.dirname(os.path.abspath(__file__))
    made = set()
    for block, lo, hi, fname, url in CHART_PDFS:
        path = os.path.join(base, fname)
        _chart_get(url, path)
        doc = fitz.open(path)
        cells = _chart_cells(doc, lo, hi)
        got = 0
        for cp, (pno, rect) in cells.items():
            sid = _CP_SID.get(cp)
            if sid is None:
                continue
            pix = doc[pno].get_pixmap(
                matrix=fitz.Matrix(6, 6), clip=rect)
            img = Image.frombytes("RGB", (pix.width, pix.height),
                                  pix.samples)
            _compose_tile(_ink_crop(img), sid).save(
                os.path.join(out, sid + ".png"))
            made.add(sid)
            got += 1
        want = sum(1 for c in range(lo, hi + 1) if c in _CP_SID)
        print(f"  {block}: {got} cells cropped ({want} catalogued)")
    return made


def _font_tiles(d, out, made):
    """Fallback real-font ink for encoded signs missed by chart crops."""
    from PIL import Image, ImageDraw, ImageFont
    from fontTools.ttLib import TTFont
    import numpy as np
    base = os.path.dirname(os.path.abspath(__file__))
    fonts = []
    for name in ("NewGardiner.ttf", "Aegyptus.ttf"):
        fp = os.path.join(base, name)
        if not os.path.exists(fp):
            continue
        cmap = set()
        for table in TTFont(fp)["cmap"].tables:
            if table.isUnicode():
                cmap.update(table.cmap)
        fonts.append((cmap, ImageFont.truetype(fp, 200)))

    def render(cp, fnt):
        im = Image.new("L", (260, 260), 255)
        ImageDraw.Draw(im).text((130, 130), chr(cp), font=fnt,
                                fill=0, anchor="mm")
        return im

    notdefs = []
    for _cmap, fnt in fonts:
        notdefs.append(np.asarray(render(0x10FFFE, fnt).point(
            lambda p: 255 if p < 210 else 0)))
    n = 0
    for s in d.signs.values():
        if s.cp is None or s.sid in made:
            continue
        for fi, (cmap, fnt) in enumerate(fonts):
            if s.cp not in cmap:
                continue
            im = render(s.cp, fnt)
            mask = np.asarray(im.point(lambda p: 255 if p < 210 else 0))
            if mask.any() and not (mask == notdefs[fi]).all():
                _compose_tile(_ink_crop(im.convert("RGB")),
                              s.sid).save(os.path.join(out, s.sid + ".png"))
                made.add(s.sid)
                n += 1
                break
    return n


def _seed_tiles(d, out, made):
    """The sixteen pictured marks + species variants: crops from the image,
    carved orientation kept -- never mirrored."""
    from PIL import Image, ImageOps, ImageEnhance
    base = os.path.dirname(os.path.abspath(__file__))
    im = Image.open(os.path.join(base, "ReferenceDialect", "Rosetta.png")
                    ).convert("RGB")
    n = 0
    for sid, seg in SEED_SEGMENTS.items():
        if sid not in d.signs:
            continue
        if isinstance(seg, str):
            # species variant: borrow the recorded sign's authentic
            # chart tile -- a real different bird kind
            src = os.path.join(out, seg + ".png")
            if os.path.exists(src):
                _compose_tile(
                    Image.open(src).convert("RGB").crop(
                        (8, 8, TILE_W - 8, TILE_H - 46)),
                    sid).save(os.path.join(out, sid + ".png"))
                made.add(sid)
                n += 1
            continue
        crop = im.crop((ROSETTA_COL[0], seg[0], ROSETTA_COL[1], seg[1]))
        crop = _strip_borders(crop)
        crop = ImageOps.autocontrast(crop, cutoff=1)
        crop = crop.resize((crop.width * 6, crop.height * 6),
                           Image.LANCZOS)
        crop = ImageEnhance.Sharpness(crop).enhance(2.0)
        _compose_tile(_ink_crop(crop), sid).save(
            os.path.join(out, sid + ".png"))
        made.add(sid)
        n += 1
    return n


def _strip_borders(crop):
    """Drop full-height column-border lines from a supplied image crop -- they
    are the register's frame, not the mark."""
    import numpy as np
    a = np.asarray(crop.convert("L"))
    if a.size == 0:
        return crop
    dark = a < 140
    h = a.shape[0]
    l, r = 0, a.shape[1]
    while l < r - 4 and dark[:, l:l + 3].mean() > 0.72 \
            and dark[:, l:l + 3].sum() > h * 0.72 * 2:
        l += 1
    while r > l + 4 and dark[:, r - 3:r].mean() > 0.72 \
            and dark[:, r - 3:r].sum() > h * 0.72 * 2:
        r -= 1
    return crop.crop((l, 0, r, h))


def _placeholder_tile(s, out):
    """Deterministic visible slot glyph for marks with no document source."""
    from PIL import Image, ImageDraw
    import hashlib
    im = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    ink = _INK + (255,)
    seed = int.from_bytes(hashlib.sha256(s.sid.encode()).digest()[:8], "big")
    text = (s.depicts or "mark").lower()

    def motif(cx=60, cy=56, scale=1.0):
        if any(w in text for w in ("bird", "falcon", "owl", "goose")):
            dr.ellipse((cx-24, cy-6, cx+16, cy+20), outline=ink, width=5)
            dr.ellipse((cx+8, cy-24, cx+28, cy-6), outline=ink, width=5)
            dr.polygon([(cx+27, cy-14), (cx+40, cy-9), (cx+27, cy-4)], fill=ink)
            dr.line((cx-4, cy+19, cx-10, cy+36), fill=ink, width=4)
            dr.line((cx+7, cy+19, cx+15, cy+36), fill=ink, width=4)
        elif any(w in text for w in ("fish", "tilapia")):
            dr.ellipse((cx-34, cy-12, cx+18, cy+18), outline=ink, width=5)
            dr.polygon([(cx+17, cy+3), (cx+39, cy-12), (cx+39, cy+18)], fill=ink)
            dr.ellipse((cx-22, cy-4, cx-15, cy+3), fill=ink)
        elif any(w in text for w in ("plant", "grain", "leaf")):
            dr.line((cx, cy-36, cx, cy+38), fill=ink, width=5)
            for dy in (-22, -6, 10):
                dr.arc((cx-34, cy+dy-10, cx-1, cy+dy+12), 250, 90, fill=ink, width=4)
                dr.arc((cx+1, cy+dy-10, cx+34, cy+dy+12), 90, 290, fill=ink, width=4)
        elif any(w in text for w in ("water", "river", "sea", "shore")):
            for y in (cy-12, cy+4, cy+20):
                dr.arc((cx-42, y-12, cx-4, y+12), 0, 180, fill=ink, width=4)
                dr.arc((cx-4, y-12, cx+34, y+12), 180, 360, fill=ink, width=4)
        elif any(w in text for w in ("boat", "ship")):
            dr.arc((cx-42, cy-6, cx+42, cy+38), 0, 180, fill=ink, width=6)
            dr.line((cx, cy-40, cx, cy+8), fill=ink, width=5)
            dr.polygon([(cx+4, cy-38), (cx+33, cy-20), (cx+4, cy-5)], outline=ink, width=4)
        elif any(w in text for w in ("building", "house", "room")):
            dr.polygon([(cx-35, cy+34), (cx-28, cy-14), (cx+28, cy-14), (cx+35, cy+34)], outline=ink, width=5)
            dr.rectangle((cx-8, cy+10, cx+8, cy+34), outline=ink, width=4)
        elif any(w in text for w in ("weapon", "tool", "arrow", "knife")):
            dr.line((cx-31, cy+38, cx+28, cy-37), fill=ink, width=6)
            dr.polygon([(cx+28, cy-37), (cx+39, cy-43), (cx+34, cy-26)], fill=ink)
            dr.line((cx-38, cy+19, cx-15, cy+42), fill=ink, width=4)
        elif any(w in text for w in ("vessel", "jar", "basket", "container")):
            dr.ellipse((cx-25, cy-36, cx+25, cy-15), outline=ink, width=5)
            dr.polygon([(cx-22, cy-19), (cx+22, cy-19), (cx+31, cy+35), (cx-31, cy+35)], outline=ink, width=5)
        elif any(w in text for w in ("deity", "man", "woman", "person", "king")):
            dr.ellipse((cx-13, cy-39, cx+13, cy-13), outline=ink, width=5)
            dr.line((cx, cy-12, cx, cy+21), fill=ink, width=6)
            dr.line((cx, cy-2, cx-30, cy+13), fill=ink, width=5)
            dr.line((cx, cy-2, cx+30, cy+13), fill=ink, width=5)
            dr.line((cx, cy+21, cx-19, cy+45), fill=ink, width=5)
            dr.line((cx, cy+21, cx+19, cy+45), fill=ink, width=5)
        elif s.kind == "mark":
            dr.line((cx-26, cy-38, cx-26, cy+38), fill=ink, width=5)
            dr.line((cx+26, cy-38, cx+26, cy+38), fill=ink, width=5)
            dr.line((cx-26, cy, cx+26, cy), fill=ink, width=4)
            dr.ellipse((cx-7, cy-7, cx+7, cy+7), outline=ink, width=3)
        else:
            # Distinct abstract record-mark: curve, stem, head, and tail.
            dr.arc((cx-30, cy-35, cx+28, cy+18), 190 + seed % 60, 40 + seed % 80, fill=ink, width=6)
            dr.line((cx-8, cy-30, cx+8, cy+38), fill=ink, width=5)
            dr.ellipse((cx+8, cy-38, cx+25, cy-20), outline=ink, width=4)
            dr.line((cx-24, cy+32, cx+24, cy+32), fill=ink, width=4)

    motif()
    # Two tiny deterministically varied strokes keep otherwise identical
    # abstract slots visually distinct without pretending to be evidence.
    for k in range(2):
        x = 22 + ((seed >> (k * 9)) % 72)
        y = 20 + ((seed >> (k * 9 + 3)) % 76)
        dr.line((x, y, min(108, x + 10 + seed % 8), y - 4), fill=ink, width=2)
    return im


def build_tiles(d, verify=False):
    """Regenerate every glyph tile from the documents. --build-tiles."""
    _build_deps()
    os.makedirs(TILE_DIR, exist_ok=True)
    global _CP_SID
    _CP_SID = {s.cp: s.sid for s in d.signs.values() if s.cp is not None}
    bar("BUILDING GLYPH TILES", "-")
    made = _chart_tiles(d, TILE_DIR)
    n_seed = _seed_tiles(d, TILE_DIR, made)
    n_font = _font_tiles(d, TILE_DIR, made)
    if n_font:
        print(f"  {n_font} signs filled from local fonts (chart gap)")
    # Unencoded series and any codepoint with no source shape get a stable
    # pictorial slot mark -- visible and unique, never the font's tofu box.
    unassigned = 0
    for s in d.signs.values():
        if s.sid in made:
            continue
        _placeholder_tile(s, TILE_DIR).save(
            os.path.join(TILE_DIR, s.sid + ".png"))
        unassigned += 1
    # stale tiles (old wrong glyphs, obsolete .alt variants)
    stale = 0
    keep = {s.sid + ".png" for s in d.signs.values()}
    for fn in os.listdir(TILE_DIR):
        if fn.endswith(".png") and (".alt" in fn or fn not in keep):
            os.remove(os.path.join(TILE_DIR, fn))
            stale += 1
    print(f"  {len(made)} document-authentic tiles + "
          f"{unassigned} honest placeholders; {stale} stale removed")
    bar()
    if verify:
        return verify_tiles(d)
    return 0


def _tile_is_tofu(path):
    """True when alpha ink is the standard hollow .notdef rectangle."""
    from PIL import Image
    import numpy as np
    a = np.asarray(Image.open(path).convert("RGBA"))[:, :, 3] > 0
    if not a.any():
        return False
    ys, xs = np.where(a)
    b = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = b.shape
    if h < 35 or w < 20:
        return False
    top, bottom = b[:4].mean(), b[-4:].mean()
    left, right = b[:, :4].mean(), b[:, -4:].mean()
    inner = b[5:-5, 5:-5].mean() if h > 10 and w > 10 else 1
    return (w < TILE_W * .5 and h > w * 1.25
            and top > .7 and bottom > .7 and left > .7 and right > .7
            and inner < .2)


def verify_tiles(d):
    """Coverage audit: every sid has a real, non-empty, non-tofu tile."""
    from PIL import Image
    import numpy as np
    import hashlib
    from collections import Counter
    empty, missing, tofu = [], [], []
    hashes = Counter()
    for s in d.signs.values():
        fp = os.path.join(TILE_DIR, s.sid + ".png")
        if not os.path.exists(fp):
            missing.append(s.sid)
            continue
        hashes[hashlib.sha256(open(fp, "rb").read()).hexdigest()] += 1
        a = np.asarray(Image.open(fp).convert("RGBA"))[:, :, 3]
        if (a > 0).mean() < 0.001:
            empty.append(s.sid)
        elif _tile_is_tofu(fp):
            tofu.append(s.sid)
    repeated = sum(n for n in hashes.values() if n >= 20)
    print(f"  tiles: {len(d.signs) - len(missing)}/{len(d.signs)} present;"
          f" {len(empty)} empty; {len(missing)} missing;"
          f" {len(tofu)} tofu; {repeated} mass-duplicated")
    if missing:
        print("   missing:", ", ".join(missing[:12]))
    if empty:
        print("   empty:", ", ".join(empty[:12]))
    if tofu:
        print("   tofu:", ", ".join(tofu[:12]))
    # facing audit -- a tile must not be the mirror of its source. For
    # signs also covered by the NewGardiner font, the tile ink-shape is
    # compared against the font render and its horizontal flip.
    if not os.path.exists(os.path.join(
            os.path.dirname(TILE_DIR), "NewGardiner.ttf")):
        print("  facing audit skipped -- NewGardiner.ttf absent")
        return 1 if (missing or empty or tofu or repeated) else 0
    from PIL import ImageDraw, ImageFont
    try:
        font_path = os.path.join(os.path.dirname(TILE_DIR),
                                 "NewGardiner.ttf")
        fnt = ImageFont.truetype(font_path, 140)
        from fontTools.ttLib import TTFont
        font_cmap = {cp for table in TTFont(font_path)["cmap"].tables
                     if table.isUnicode() for cp in table.cmap}
    except (OSError, ImportError):
        print("  facing audit skipped -- NewGardiner.ttf unreadable")
        return 1 if (missing or empty or tofu or repeated) else 0

    def ink(path=None, ch=None):
        if path:
            a = np.asarray(Image.open(path).convert("RGBA")
                           .resize((200, 200)))[:, :, 3]
            return a > 0
        im = Image.new("L", (200, 200), 255)
        if ch:
            ImageDraw.Draw(im).text((100, 100), ch, font=fnt, fill=0,
                                    anchor="mm")
        return np.asarray(im) < 200

    def sim(a, b):
        if a.sum() == 0 or b.sum() == 0:
            return 0.0
        inter = (a & b).sum()
        return inter / min(a.sum(), b.sum())

    flipped, checked = [], 0
    for s in d.signs.values():
        if (s.cp is None or s.cp not in font_cmap
                or s.cp < 0x13000 or s.cp > 0x143FA):
            continue
        fp = os.path.join(TILE_DIR, s.sid + ".png")
        if not os.path.exists(fp):
            continue
        t = ink(path=fp)
        f = ink(ch=chr(s.cp))
        if f.sum() == 0:
            continue
        checked += 1
        if sim(t, np.fliplr(f)) > sim(t, f) * 1.15 and \
                sim(t, np.fliplr(f)) > 0.55:
            flipped.append(s.sid)
    print(f"  facing audit: {checked} cross-checked vs NewGardiner;"
          f" {len(flipped)} font-variant warnings (chart retained)")
    if flipped:
        print("   variants:", ", ".join(flipped[:16]))
    return 1 if (missing or empty or tofu or repeated) else 0


_CP_SID = {}


def main():
    d = Dialect()
    apply_picture_guesses(d)
    d.load()  # personal definitions ride on top of the seed

    args = [a for a in sys.argv[1:] if a != "--no-color"]
    if not args:
        if sys.stdin.isatty():
            try:
                return launch_window(d)  # the scribe window is the face
            except Exception as e:
                print(f"window unavailable ({e}) -- dropping to console")
        console(d)
        return 0

    a = args[0]
    if a in ("--window", "--ui"):
        return launch_window(d)
    if a == "--console":
        console(d); return 0
    if a == "--selftest":
        return selftest()
    if a == "--build-tiles":
        return build_tiles(d, verify=("--verify" in args or
                                      "-v" in args))
    if a == "--rosetta":
        rosetta(d); return 0
    if a == "--stats":
        stats(d); return 0
    if a == "--guesses":
        guesses_report(d); return 0
    if a == "--motifs":
        name = args[1] if len(args) > 1 else "rosetta"
        if name not in d.columns:
            print(f"no column '{name}'"); return 2
        motifs_report(d, d.columns[name]); return 0
    if a == "--sources":
        sources_report(); return 0
    if a == "--history":
        history_report(d, args[1] if len(args) > 1 else None); return 0
    if a == "--local":
        local_report(d, args[1] if len(args) > 1 else None); return 0
    if a == "--format":
        format_report(d); return 0
    if a == "--knowledge":
        knowledge_report(d); return 0
    if a == "--book":
        book_report(d); return 0
    if a == "--story":
        if len(args) < 2:
            print("--story <glyph-file> [translation-output.txt]")
            return 2
        if not os.path.exists(args[1]):
            print(f"no story file '{args[1]}'"); return 2
        story_report(d, args[1], args[2] if len(args) > 2 else None)
        return 0
    if a == "--translate":
        if len(args) < 3:
            print("--translate <english.txt> <glyphs.txt> [retention-report.txt]")
            return 2
        if not os.path.exists(args[1]):
            print(f"no English bridge file '{args[1]}'"); return 2
        translate_report(d, args[1], args[2],
                         args[3] if len(args) > 3 else None)
        return 0
    if a == "--transcribe":
        if len(args) < 3:
            print("--transcribe <image> <review-id> [review.json] [--cells cells.txt]")
            return 2
        if not os.path.exists(args[1]):
            print(f"no image '{args[1]}'"); return 2
        manual = None
        if "--cells" in args:
            ci = args.index("--cells")
            if ci + 1 >= len(args):
                print("--transcribe <image> <id> [review.json] [--cells cells.txt]")
                return 2
            manual = _manual_cells(args[ci + 1])
        out = next((x for i, x in enumerate(args[3:], 3)
                    if x != "--cells" and (i == 0 or args[i - 1] != "--cells")),
                   None)
        rec = transcribe_image(d, args[1], args[2], manual_cells=manual)
        if out:
            write_transcription_review(rec, out)
            print(f"review written: {out}")
        d.save()
        print(f"{len(rec['columns'])} column(s), "
              f"{sum(len(c['entries']) for c in rec['columns'])} "
              "candidate cells -- review required")
        return 0
    if a == "--review":
        transcription_report(d, args[1] if len(args) > 1 else None); return 0
    if a == "--pick":
        if len(args) < 4:
            print("--pick <review-id> <cell#> <candidate#|sid>"); return 2
        print(pick_transcription(d, args[1], int(args[2]), args[3]))
        d.save(); return 0
    if a == "--approve":
        if len(args) < 3:
            print("--approve <review-id> <column-name>"); return 2
        try:
            print(approve_transcription(
                d, args[1], args[2],
                int(args[3]) if len(args) > 3 else None))
        except ValueError:
            print("--approve <review-id> <column-name> [column#]"); return 2
        d.save(); return 0
    if a == "--reject":
        if len(args) < 2:
            print("--reject <review-id>"); return 2
        print(reject_transcription(d, args[1])); d.save(); return 0
    if a == "--audit":
        audit(d, _sid(d, args[1]) if len(args) > 1 else None); return 0
    if a == "--laws":
        print(LAWS); return 0
    if a == "--catalog":
        catalog(d, args[1] if len(args) > 1 else "all"); return 0
    if a == "--chart":
        print(f"written: {chart(d)}"); return 0
    if a == "--export":
        do_export(d); return 0
    if a in ("--help", "-h"):
        print(__doc__); return 0
    print(f"unknown flag '{a}' -- try --help")
    return 2

if __name__ == "__main__":
    sys.exit(main())
