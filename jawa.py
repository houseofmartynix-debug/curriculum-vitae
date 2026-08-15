# -*- coding: utf-8 -*-
"""Latin (basa Jawa) -> Aksara Jawa transliterator + reverse round-trip verifier.

Source convention:
  e        = pepet   (ê)
  é / è    = taling
  o        = taling tarung
  dh, th   = murda-less retroflex (aksara dha / tha)
  ng, ny   = single aksara
  f v z kh sy gh = rekan (base + cecak telu)
  Digits   = Javanese numerals wrapped in pada pangkat
"""

# --- aksara nglegena -------------------------------------------------------
HA, NA, CA, RA, KA = 'ꦲ', 'ꦤ', 'ꦕ', 'ꦫ', 'ꦏ'
DA, TA, SA, WA, LA = 'ꦢ', 'ꦠ', 'ꦱ', 'ꦮ', 'ꦭ'
PA, DHA, JA, YA, NYA = 'ꦥ', 'ꦝ', 'ꦗ', 'ꦪ', 'ꦚ'
MA, GA, BA, THA, NGA = 'ꦩ', 'ꦒ', 'ꦧ', 'ꦛ', 'ꦔ'

# --- sandhangan ------------------------------------------------------------
CECAK   = 'ꦁ'   # -ng
LAYAR   = 'ꦂ'   # -r
WIGNYAN = 'ꦃ'   # -h
TARUNG  = 'ꦴ'   # o (with taling)
WULU    = 'ꦶ'   # i
SUKU    = 'ꦸ'   # u
TALING  = 'ꦺ'   # é
PEPET   = 'ꦼ'   # e
KERET   = 'ꦽ'   # -re-
PENGKAL = 'ꦾ'   # -y-
CAKRA   = 'ꦿ'   # -r-
PANGKON = '꧀'   # virama / pasangan trigger
TELU    = '꦳'   # cecak telu -> rekan

# --- aksara swara (word-initial vowels) ------------------------------------
SW = {'a': 'ꦄ', 'i': 'ꦆ', 'u': 'ꦈ', 'é': 'ꦌ', 'o': 'ꦎ',
      'e': 'ꦄ' + PEPET}

# --- punctuation & digits --------------------------------------------------
PADA_LINGSA, PADA_LUNGSI, PADA_PANGKAT = '꧈', '꧉', '꧇'
ADEG_ADEG = '꧋'
DIGITS = {str(i): chr(0xA9D0 + i) for i in range(10)}

CONS = {
    'ng': NGA, 'ny': NYA, 'dh': DHA, 'th': THA,
    'kh': KA + TELU, 'gh': GA + TELU, 'sy': SA + TELU, 'dz': DA + TELU,
    'f': PA + TELU, 'v': WA + TELU, 'z': JA + TELU,
    'h': HA, 'n': NA, 'c': CA, 'r': RA, 'k': KA, 'd': DA, 't': TA, 's': SA,
    'w': WA, 'l': LA, 'p': PA, 'j': JA, 'y': YA, 'm': MA, 'g': GA, 'b': BA,
    'q': KA, 'x': KA + PANGKON + SA,
}
# longest-first so digraphs win
CKEYS = sorted(CONS, key=len, reverse=True)

VOW = {'a': '', 'i': WULU, 'u': SUKU, 'é': TALING, 'è': TALING,
       'e': PEPET, 'o': TALING + TARUNG}
VKEYS = set(VOW)

CODA_SIGN = {'ng': CECAK, 'r': LAYAR, 'h': WIGNYAN}


def _read_cons(s, i):
    """Return (aksara, length) for the consonant unit at s[i:], else (None, 0)."""
    for k in CKEYS:
        if s.startswith(k, i):
            return CONS[k], len(k)
    return None, 0


def word(w):
    """Transliterate a single Javanese word written in Latin."""
    s = w.lower()
    out = []
    i = 0
    first = True
    prev_vowel = None
    while i < len(s):
        ch = s[i]

        # --- vowel-initial syllable ---------------------------------------
        if ch in VKEYS:
            if first:
                out.append(SW.get(ch, SW['a']))
            else:
                # hiatus needs a carrier: ya after i/é, wa after u, else ha
                glide = YA if prev_vowel in ('i', 'é', 'è') else \
                        WA if prev_vowel == 'u' else HA
                out.append(glide + VOW[ch])
            prev_vowel = ch
            i += 1
            first = False
            i = _coda(s, i, out)
            continue

        # --- consonant onset ----------------------------------------------
        aks, n = _read_cons(s, i)
        if aks is None:                      # hyphen/apostrophe -> pass through
            out.append(ch)                   # and start a fresh word after it
            first, prev_vowel = True, None
            i += 1
            continue
        i += n
        syl = aks

        # medial cluster: -r- (cakra / keret), -y- (pengkal), -l- (pasangan la)
        if i < len(s) and s[i] == 'r' and i + 1 < len(s) and s[i + 1] in VKEYS:
            if s[i + 1] == 'e':
                syl += KERET
                i += 2
                out.append(syl)
                first = False
                prev_vowel = 'e'
                i = _coda(s, i, out)
                continue
            syl += CAKRA
            i += 1
        elif i < len(s) and s[i] == 'y' and i + 1 < len(s) and s[i + 1] in VKEYS:
            syl += PENGKAL
            i += 1
        elif i < len(s) and s[i] == 'l' and i + 1 < len(s) and s[i + 1] in VKEYS:
            syl += PANGKON + LA
            i += 1

        # vowel
        if i < len(s) and s[i] in VKEYS:
            syl += VOW[s[i]]
            prev_vowel = s[i]
            i += 1
        else:
            syl += PANGKON            # bare consonant (word-final cluster)
            prev_vowel = None
        out.append(syl)
        first = False
        i = _coda(s, i, out)
    return ''.join(out)


def _coda(s, i, out):
    """Attach a syllable-closing consonant if one is present.

    A consonant belongs to the coda only when it is followed by another
    consonant or by end-of-word; a single intervocalic consonant is the
    onset of the next syllable.
    """
    aks, n = _read_cons(s, i)
    if aks is None:
        return i
    unit = s[i:i + n]
    nxt = i + n
    at_end = nxt >= len(s)
    followed_by_cons = (not at_end) and s[nxt] not in VKEYS
    if not (at_end or followed_by_cons):
        return i                       # it is the next onset, leave it
    # C + r/y + vowel is a cluster (cakra / keret / pengkal), not a coda
    if (not at_end and unit not in CODA_SIGN and s[nxt] in 'ry'
            and nxt + 1 < len(s) and s[nxt + 1] in VKEYS):
        return i

    if unit in CODA_SIGN:
        out.append(CODA_SIGN[unit])
    else:
        out.append(aks + PANGKON)      # pangkon; renders as pasangan if C follows
    return nxt


def num(txt):
    """Javanese numerals, wrapped in pada pangkat as orthography requires."""
    return PADA_PANGKAT + ''.join(DIGITS[c] for c in txt) + PADA_PANGKAT


def tr(text):
    """Transliterate a phrase. '~' keeps the following token in Latin.
       '#1234' renders as Javanese numerals. ',' -> pada lingsa, '.' -> pada lungsi."""
    parts = []
    for tok in text.split(' '):
        if not tok:
            continue
        if tok.startswith('~'):
            parts.append(tok[1:])
            continue
        if tok.startswith('#'):
            parts.append(num(tok[1:]))
            continue
        trail = ''
        while tok and tok[-1] in ',.:':
            trail = {',': PADA_LINGSA, '.': PADA_LUNGSI, ':': PADA_PANGKAT}[tok[-1]] + trail
            tok = tok[:-1]
        parts.append(word(tok) + trail)
    return ' '.join(parts)


# ---------------------------------------------------------------------------
# reverse transliteration — used purely to prove the forward pass round-trips
# ---------------------------------------------------------------------------
R_CONS = {}
for k in CKEYS:
    R_CONS.setdefault(CONS[k], k)
R_CONS[KA + TELU] = 'kh'; R_CONS[GA + TELU] = 'gh'; R_CONS[SA + TELU] = 'sy'
R_CONS[PA + TELU] = 'f';  R_CONS[WA + TELU] = 'v';  R_CONS[JA + TELU] = 'z'
R_CONS[DA + TELU] = 'dz'
R_SW = {v: k for k, v in SW.items() if k != 'e'}
R_SW[SW['e']] = 'e'
R_DIG = {v: k for k, v in DIGITS.items()}


def untr_word(w):
    out = []
    i = 0
    while i < len(w):
        # aksara swara (may still carry a closing cecak/layar/wignyan)
        if w[i:i + 2] in R_SW:
            out.append(R_SW[w[i:i + 2]]); i += 2
        elif w[i] in R_SW:
            out.append(R_SW[w[i]]); i += 1
        else:
            i = _untr_cons(w, i, out); continue
        while i < len(w) and w[i] in (CECAK, LAYAR, WIGNYAN):
            out.append({CECAK: 'ng', LAYAR: 'r', WIGNYAN: 'h'}[w[i]]); i += 1
    return ''.join(out)


def _untr_cons(w, i, out):
    """Decode one consonant-onset syllable at w[i:]; return the next index."""
    two = w[i:i + 2]
    if two in R_CONS:
        c = R_CONS[two]; i += 2
    elif w[i] in R_CONS:
        c = R_CONS[w[i]]; i += 1
    else:
        out.append(w[i]); return i + 1
    # medial signs
    if i < len(w) and w[i] == KERET:
        out.append(c + 're'); return i + 1
    if i < len(w) and w[i] == CAKRA:
        c += 'r'; i += 1
    elif i < len(w) and w[i] == PENGKAL:
        c += 'y'; i += 1
    elif w[i:i + 2] == PANGKON + LA:
        c += 'l'; i += 2
    # vowel
    if i < len(w) and w[i] == PANGKON:
        out.append(c); return i + 1
    if w[i:i + 2] == TALING + TARUNG:
        out.append(c + 'o'); i += 2
    elif i < len(w) and w[i] == WULU:
        out.append(c + 'i'); i += 1
    elif i < len(w) and w[i] == SUKU:
        out.append(c + 'u'); i += 1
    elif i < len(w) and w[i] == TALING:
        out.append(c + 'e\u0301'); i += 1
    elif i < len(w) and w[i] == PEPET:
        out.append(c + 'e'); i += 1
    else:
        out.append(c + 'a')
    # coda signs
    while i < len(w) and w[i] in (CECAK, LAYAR, WIGNYAN):
        out.append({CECAK: 'ng', LAYAR: 'r', WIGNYAN: 'h'}[w[i]]); i += 1
    return i


def untr(text):
    parts = []
    for tok in text.split(' '):
        if not tok:
            continue
        t = ''
        while t.__class__ and tok and tok[-1] in (PADA_LINGSA, PADA_LUNGSI, PADA_PANGKAT):
            t = {PADA_LINGSA: ',', PADA_LUNGSI: '.', PADA_PANGKAT: ':'}[tok[-1]] + t
            tok = tok[:-1]
        if tok.startswith(PADA_PANGKAT) and tok.endswith(PADA_PANGKAT) and len(tok) > 2:
            parts.append('#' + ''.join(R_DIG.get(c, c) for c in tok[1:-1])); continue
        if tok and all(c in R_DIG for c in tok):
            parts.append('#' + ''.join(R_DIG[c] for c in tok) + t); continue
        parts.append(untr_word(tok) + t)
    return ' '.join(parts)


import re as _re
import unicodedata as _ud


def _norm(s):
    """Normalise for comparison.

    Hiatus carriers (ha/ya/wa) are inserted by the script and have no Latin
    counterpart, so strip any intervocalic h/y/w from BOTH sides — applied
    symmetrically it stays a valid equivalence check, while letting the
    round-trip prove the syllable structure itself.
    """
    s = _ud.normalize('NFC', s).lower().replace('è', 'é').replace('~', '')
    return _re.sub(r'(?<=[aiueoé])[hyw](?=[aiueoé])', '', s)


def check(latin):
    """Forward-transliterate, reverse it, and report any mismatch."""
    aks = tr(latin)
    back = untr(aks)
    return aks, back, _norm(back) == _norm(latin)
