# -*- coding: utf-8 -*-
"""Build the CV in two languages from one source.

    index.html      aksara Jawa  (canonical)
    en/index.html   English

Every piece of copy is a (javanese_latin, english) pair. The Javanese half is
transliterated by jawa.py and round-trip verified; nothing reaches the page
without proving it decodes back to its Latin source.
"""
import pathlib
import jawa

HERE = pathlib.Path(__file__).parent
PHOTO = (HERE / 'photo.b64').read_text().strip()
CSS = (HERE / 'style.css').read_text()

AUDIT = []


def J(latin):
    """Transliterate + record for the round-trip audit."""
    aks, back, ok = jawa.check(latin)
    AUDIT.append((latin, aks, back, ok))
    return aks


# English build: drop the Javanese metrics and restore the original Latin styling.
EN_OVERRIDE = """<style>
  :root{--jv:'DM Sans',sans-serif}
  .tag,.sec-label{letter-spacing:1.8px;text-transform:uppercase;font-size:11px;
    line-height:1.5;padding-bottom:0}
  .title-row{font-size:12px;letter-spacing:1.8px;text-transform:uppercase;line-height:1.5}
  .comp{font-size:11.5px;letter-spacing:.3px;line-height:1.5}
  .lang-badge{font-size:10.5px;line-height:1.5}
  .exp-period{font-size:11px;line-height:1.5;padding:3px 9px}
  .c-pill .lbl{font-size:10px;letter-spacing:0.8px;text-transform:uppercase;line-height:1.5}
  .find .cert-id{font-size:11.5px;line-height:1.5}
  .sec-note{font-size:12.5px;line-height:1.65}
  .edu-school,.edu-year{font-family:var(--mono)}
  .bio{line-height:1.75}
  .langsw a.jvlbl{font-family:'Noto Sans Javanese',sans-serif}
</style>"""

MONTHS = {
    'jan': ('Januari', 'January'),     'feb': ('Fèbruari', 'February'),
    'apr': ('April', 'April'),         'mei': ('Mèi', 'May'),
    'jun': ('Juni', 'June'),           'aug': ('Agustus', 'August'),
    'sep': ('Sèptèmber', 'September'), 'oct': ('Oktober', 'October'),
    'nov': ('Nopèmber', 'November'),
}


def render(lang):
    jv = lang == 'jv'
    C = ' jv' if jv else ''                      # class hook, Javanese only

    def T(jw, en):
        return J(jw) if jv else en

    def Y(n):                                    # year / numeral
        return jawa.num(n) if jv else n

    def M(key):
        return T(*MONTHS[key])

    # ------------------------------------------------------------- top bar ---
    status_txt = T('Siyaga nampa pakaryan kaamanan', 'Available for AppSec & Pentest Roles')
    print_lbl  = T('Cithak / Simpen ~PDF', 'Print / Export PDF')
    copied_txt = T('Tersalin!', 'Copied!')

    # ------------------------------------------------------------- header ---
    tag   = T('serat riwayat gesang', 'curriculum vitae')
    role  = T('juru uji penétrasi', 'Penetration Tester')
    role2 = T('pamburu celah kaamanan', 'Bug Bounty Hunter')
    bio = T(
        'Panaliti kaamanan sing nggarap uji penétrasi aplikasi web, ~API, lan '
        'plugin perusahaan. Nemokake sarta nglaporake celah kaamanan ing program '
        'sayembara umum: munggah drajat wewenang, ~SSRF, nrabas wates wewenang, '
        'lan bocoran kredensial. Kulina maca kodhe sumber saka asil dékompilasi, '
        'banjur mbuktèkake temuan nganggo bukti konsép sing kauji langsung.',
        'Security researcher focused on penetration testing of web applications, '
        'APIs, and enterprise plugins. Finds and reports vulnerabilities on public '
        'bounty programmes: privilege escalation, SSRF, authorization bypass, and '
        'credential exposure. Comfortable reading decompiled source and proving '
        'findings with proof-of-concepts validated against live systems.')

    l_telp  = T('telepon', 'phone')
    l_surel = T('surel', 'email')
    l_papan = T('papan', 'location')
    papan   = T('Malang, Jawa Wétan, Indonésia', 'Malang, East Java, Indonesia')

    s_exp   = T('pengalaman', 'experience')
    s_find  = T('asil panemu pinilih', 'selected findings')
    s_cert  = T('sertifikat', 'certifications')
    s_edu   = T('pendhidhikan', 'education')
    s_skill = T('kaprigelan teknis', 'technical skills')
    s_comp  = T('kabisan inti', 'core competencies')
    s_lang  = T('basa', 'languages')
    s_port  = T('portofolio', 'portfolio')

    now = T('saiki', 'present')

    # --------------------------------------------------------- experience ---
    EXP = [
        (T('Panaliti Kaamanan Mandhiri', 'Independent Security Researcher'),
         f'{M("jan")} {Y("2026")} – {now}',
         'Bugcrowd · HackerOne · YesWeHack · Gerobug',
         T('Nguji aplikasi web, ~API, lan plugin ~Atlassian ~Data ~Center kanggo '
           'program sayembara celah kaamanan, kalebu program pamaréntah. Nindakake '
           'pemetaan permukaan serangan, maca kodhe sumber saka asil dékompilasi '
           '~JAR, sarta nggawe bukti konsép sing kauji langsung. Nulis lapuran '
           'manut standar ~VRT lan ~CVSS, banjur ngurus komunikasi karo tim triase '
           'nganti temuan ditampa. Uga mbangun piranti otomasi dhéwé kanggo mantau '
           'owah-owahan lingkup program.',
           'Tests web applications, APIs, and Atlassian Data Center plugins for '
           'public bug bounty programmes, including government programmes. Performs '
           'attack-surface mapping, reads source recovered from JAR decompilation, '
           'and builds proof-of-concepts validated against live systems. Writes '
           'reports to VRT and CVSS standards and carries triage communication '
           'through to acceptance. Also builds custom automation to monitor '
           'programme scope changes.')),

        (T('Ahli Penjualan', 'Sales Expert'),
         f'{M("mei")} {Y("2024")} – {M("aug")} {Y("2025")}',
         'PT Aspirasi Hidup Indonesia Tbk (ACE Hardware) · ' + T('Kontrak', 'Contract'),
         T('Mènèhi rékomendasi produk adhedhasar risiko lan kabutuhan pelanggan, '
           'sarta ngandharake fitur teknis marang wong sing ora teknis. Kaprigelan '
           'iki kepaké nalika nerangake dampak celah kaamanan marang tim non-teknis.',
           'Delivered risk-based product recommendations aligned to customer needs '
           'and explained technical features to non-technical customers. The same '
           'skill now carries over to explaining vulnerability impact to '
           'non-technical stakeholders.')),

        (T('Staf Pemasaran lan Penjualan', 'Sales & Marketing Staff'),
         f'{M("sep")} {Y("2021")} – {M("nov")} {Y("2022")}',
         'FIFGROUP · ' + T('Kontrak', 'Contract'),
         T('Nyusun lan nglakokake program pemasaran adhedhasar analisis data '
           'pelanggan lan pasar, ngurus promosi digital sarta lapangan. Nglatih '
           'maca data lan nemokake pola sing ora lumrah.',
           'Planned and ran marketing programmes driven by customer and market data '
           'analysis, managing both digital and on-ground promotion. Built the habit '
           'of reading data and spotting anomalous patterns.')),

        (T('Kru Toko', 'Store Crew'),
         f'{Y("2019")} – {Y("2021")}',
         'PT Indomarco Prismatama Tbk (Indomaret)',
         T('Ngladèni pelanggan lan ngurus operasi toko saben dina kanthi tliti. '
           'Nguwatake katliten, disiplin, lan tundhuk marang prosedur — sing dadi '
           'dhasar ing pakaryan kaamanan.',
           'Served customers and ran daily store operations with high accuracy. '
           'Strengthened attention to detail, discipline, and procedural '
           'compliance — the groundwork for security work.')),
    ]

    # ------------------------------------------------------------ findings ---
    find_note = T(
        'Target lapuran sing isih ing triase ora disebut jenengé ing kaca umum iki, '
        'awit aturan disclosure platform mbutuhake idin tinulis saka program. '
        'Rincian jangkep kena dijaluk.',
        'Targets still in triage are not named on this public page: platform '
        'disclosure terms require the programme’s written consent first. '
        'Full detail available on request.')

    FIND = [
        (T('Enumerasi pangguna liwat ~NIK ing layanan pamaréntah',
           'User enumeration via national ID (NIK) in a government service'),
         'Diskominfo Kota Tangerang Selatan · Gerobug',
         'Medium',
         T('piagam panghargaan', 'certificate of appreciation') + ' 7C0B38027836'),

        (T('Bocoran kodhe sumber ing layanan pamaréntah',
           'Source code disclosure in a government service'),
         'Diskominfo Kota Tangerang Selatan · Gerobug',
         'Medium',
         T('piagam panghargaan', 'certificate of appreciation') + ' 7C0B36916030'),

        (T('Munggah drajat wewenang tekan administrator liwat token '
           'panyamaran sing kena ditebak',
           'Privilege escalation to administrator via a predictable '
           'impersonation token'),
         T('Plugin Jira/Confluence perusahaan', 'Enterprise Jira/Confluence plugin'),
         'P2',
         T('kauji langsung ing lingkungan urip — tekan',
           'validated on a live instance — reached') + ' SYSTEM_ADMIN'),

        (T('Sandhi database kekirim tanpa enkripsi senajan ~TLS diuripake',
           'Database credential sent in cleartext despite TLS being enabled'),
         T('Konektor database ~Node.js sing akèh dienggo',
           'Widely used Node.js database connector'),
         'CVE Pending',
         T('lolos triase — ~CVE wis ditetepake, advisory durung metu',
           'triaged — CVE assigned, advisory pending')),

        (T('~SSRF, kalebu ~SSRF buta, ing plugin ~Atlassian ~Data ~Center',
           'SSRF, including blind SSRF, in Atlassian Data Center plugins'),
         T('Rong vendor plugin kapisah', 'Two separate plugin vendors'),
         'P2 / P3',
         T('loro-loroné lolos triase', 'both triaged')),

        (T('Layanan ~MCP mbukak liwat ~HTTP tanpa autentikasi',
           'MCP service exposed over HTTP without authentication'),
         T('Aplikasi desktop', 'Desktop application'),
         'CVSS 7.3',
         T('dilapurake liwat program resmi', 'reported through official programme')),

        (T('Nrabas alur persetujuan lan registrasi klien ~OAuth sing mbukak',
           'Approval-flow bypass and open OAuth client registration'),
         T('Rong program kapisah', 'Two separate programmes'),
         'In Triage',
         T('dilapurake, isih ing triase', 'reported, currently in triage')),
    ]

    # -------------------------------------------------------- certificates ---
    CERT = [
        (T('Uji Penétrasi Web', 'Web Penetration Testing'), 'Cyber Academy Indonesia',
         f'{M("oct")} {Y("2025")}', 'BWH01110254258'),
        (T('Kaamanan Siber', 'Cyber Security') + ' 101', 'TryHackMe',
         f'{M("apr")} {Y("2026")} — {M("apr")} {Y("2029")}', 'THM-0G7VUW6K0M'),
        (T('Sertifikat Kaamanan Dhasar', 'Pre Security Certificate'), 'TryHackMe',
         f'{M("feb")} {Y("2026")} — {M("feb")} {Y("2029")}', 'THM-R4E0NX6WTU'),
        (T('Pambuka Kaamanan Siber', 'Introduction to Cybersecurity'),
         'Cisco Networking Academy', f'{M("jan")} {Y("2026")}', None),
    ]

    edu_deg = T('Sekolah Menengah Ndhuwur — Ilmu Sosial',
                'High School Diploma — Social Studies')
    edu_sch = (J('SMAN') + ' ' + jawa.num('1') + ' ' + J('Sumberpucung')) if jv \
        else 'SMAN 1 Sumberpucung'
    edu_yr = T('lulus', 'graduated') + ' ' + Y('2017')

    SKILLS = [
        (T('Uji penétrasi aplikasi web lan ~API',
           'Web application & API penetration testing'), 'OWASP Top 10 · REST · GraphQL'),
        (T('Nyegat lan ngowahi panjaluk', 'Request interception & tampering'),
         'Burp Suite · Caido'),
        (T('Audit kodhe sumber lan dékompilasi', 'Source code audit & decompilation'),
         'JADX · Procyon · javap'),
        (T('Pemetaan permukaan serangan', 'Attack surface mapping'),
         'subfinder · httpx · nuclei · katana'),
        (T('Nrabas wates wewenang', 'Authorization bypass'), 'IDOR · BOLA · authz'),
        (T('Injeksi lan déserialisasi', 'Injection & deserialization'),
         'SSRF · XXE · RCE'),
        (T('Uji token lan sesi', 'Token & session testing'), 'JWT · OAuth · SAML'),
        (T('Uji aplikasi ~Android', 'Android application testing'),
         'apktool · frida · objection'),
        (T('~Linux lan skrip otomasi', 'Linux & automation scripting'),
         'Kali · Bash · Python'),
        (T('Analisis lalu lintas jaringan', 'Network traffic analysis'),
         'Wireshark · tcpdump'),
        (T('Nulis lapuran lan mbiji risiko', 'Report writing & risk scoring'),
         'CVSS · VRT'),
    ]

    COMP = [T('pamikiran analitis', 'Analytical thinking'),
            T('tliti marang prakara cilik', 'Attention to detail'),
            T('ngudi kanthi mempeng', 'Persistence'),
            T('mbukak temuan kanthi tanggung jawab', 'Responsible disclosure'),
            T('komunikasi lapuran', 'Report communication'),
            T('sinau mandhiri', 'Self-directed learning')]

    LANGS = [(T('Jawa', 'Javanese'), T('lair', 'Native'), 'native'),
             (T('Indonésia', 'Indonesian'), T('lair', 'Native'), 'native'),
             (T('Inggris', 'English'), T('lantih', 'Advanced'), 'advanced'),
             (T('Rusia', 'Russian'), T('sedhengan', 'Intermediate'), 'inter')]

    REPOS = [
        ('appsec-payload-notes', 'https://github.com/houseofmartynix-debug/appsec-payload-notes',
         T('Cathetan ~payload lan métodhologi ing ~30 kelas celah',
           'Payload and methodology notes across 30 vulnerability classes')),
        ('marco-scanner', 'https://github.com/houseofmartynix-debug/marco-scanner',
         T('Piranti pamindhai celah aplikasi web proyèk portofolio',
           'Web vulnerability scanner portfolio project')),
        ('soc-home-lab', 'https://github.com/houseofmartynix-debug/soc-home-lab',
         T('Lab ~SOC ~Wazuh — detéksi ancaman manut ~MITRE ~ATT&CK',
           'Wazuh SOC lab — detection engineering & IR playbooks')),
        ('sinik-pro', 'https://github.com/houseofmartynix-debug/sinik-pro',
         T('Pamariksa lan pangudhar ~NIK Indonésia tanpa server',
           'Client-side Indonesian NIK validator and decoder')),
        ('bugcrowd-scope-monitor', 'https://github.com/houseofmartynix-debug/bugcrowd-scope-monitor',
         T('Otomasi ~Telegram kanggo owah-owahan lingkup ~Bugcrowd',
           'Telegram alerts on Bugcrowd scope updates via CI/CD cron')),
        ('god-recon-bot', 'https://github.com/houseofmartynix-debug/god-recon-bot',
         T('Bot ~Telegram kanggo narik lingkup program lintas platform',
           'Telegram bot pulling programme scopes across platforms')),
    ]

    # ---------------------------------------------------------------- html ---
    nl = chr(10)
    exp_html = ''.join(
        f'''        <div class="exp">
          <div class="exp-meta"><div class="exp-role{C}">{r}</div><div class="exp-period{C}">{p}</div></div>
          <div class="exp-company">{co}</div>
          <p class="exp-desc{C}">{d}</p>
        </div>
''' for r, p, co, d in EXP)

    def sev_badge(sev):
        if not sev:
            return ''
        s_cls = 'badge-p2'
        if 'P1' in sev:
            s_cls = 'badge-p1'
        elif 'P2' in sev or 'CVSS 7' in sev:
            s_cls = 'badge-p2'
        elif 'P3' in sev or 'Medium' in sev:
            s_cls = 'badge-p3'
        elif 'P4' in sev or 'Triage' in sev or 'CVE' in sev:
            s_cls = 'badge-p4'
        return f'<span class="badge-pill {s_cls}">{sev}</span>'

    find_html = ''.join(
        f'''        <div class="cert find">
          <div class="cert-name{C}">{n} {sev_badge(sev)}</div>
          <div class="cert-issuer">{o}</div>
          <div class="cert-id{C}">{note}</div>
        </div>
''' for n, o, sev, note in FIND)

    cert_html = ''.join(
        f'''        <div class="cert">
          <div class="cert-name{C}">{n}</div>
          <div class="cert-issuer">{i} &nbsp;·&nbsp; <span class="{C.strip()}">{w}</span></div>
          {f'<div class="cert-id">Credential ID: {cid}</div>' if cid else ''}
        </div>
''' for n, i, w, cid in CERT)

    skill_html = ''.join(
        f'        <div class="skill"><div class="sk-dot"></div><div>'
        f'<span class="{C.strip()}">{s}</span><span class="sk-tool">{t}</span></div></div>{nl}'
        for s, t in SKILLS)

    comp_html = ''.join(f'          <span class="comp">{k}</span>{nl}' for k in COMP)
    lang_html = ''.join(
        f'        <div class="lang"><span class="lang-name{C}">{n}</span>'
        f'<span class="lang-badge {cls}">{lv}</span></div>{nl}' for n, lv, cls in LANGS)

    repo_html = ''.join(
        f'''        <a class="repo-card" href="{url}" target="_blank" rel="noopener">
          <div class="repo-name"><span>{name}</span><span class="repo-arrow">↗</span></div>
          <div class="repo-desc{C}">{desc}</div>
        </a>{nl}''' for name, url, desc in REPOS)

    jw_label = J('Jawa') if jv else 'ꦗꦮ'
    switch = (f'<div class="langsw"><a class="on jvlbl" href="./">{jw_label}</a>'
              f'<a href="./en/">EN</a></div>') if jv else \
             (f'<div class="langsw"><a class="jvlbl" href="../">{jw_label}</a>'
              f'<a class="on" href="./">EN</a></div>')

    return f'''<!DOCTYPE html>
<html lang="{'jv' if jv else 'en'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Marco Selva Oknam — {role} · {role2}</title>
<meta name="description" content="Marco Selva Oknam — Penetration Tester, Application Security Researcher &amp; Bug Bounty Hunter.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,300&family=Noto+Sans+Javanese:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
{EN_OVERRIDE if not jv else ''}
</head>
<body>
<div class="bg-grid"></div>
<div class="cv">

  <div class="top-bar">
    <div class="status-badge">
      <span class="status-dot"></span>
      <span class="{C.strip()}">{status_txt}</span>
    </div>
    <div class="action-tools">
      <button class="btn-tool" onclick="window.print()" title="Print CV or Save as PDF">
        <span>🖨️</span>
        <span class="{C.strip()}">{print_lbl}</span>
      </button>
      {switch}
    </div>
  </div>

  <header class="header">
    <div>
      <div class="tag">{tag}</div>
      <h1 class="name"><em>Marco</em>SELVA OKNAM</h1>
      <div class="title-row">{role} <span class="sep">·</span> {role2} <span class="cursor"></span></div>
      <p class="bio{C}">{bio}</p>
    </div>
    <div class="photo-wrap">
      <div class="photo-frame">
        <img src="data:image/jpeg;base64,{PHOTO}" alt="Marco Selva Oknam">
      </div>
      <div class="pc tl"></div><div class="pc tr"></div><div class="pc bl"></div><div class="pc br"></div>
    </div>
  </header>

  <div class="contact-strip">
    <div class="c-pill" onclick="copyText(this, '+6281231602472', '{copied_txt}')" title="Click to copy phone number">
      <span class="icon">📱</span><span class="lbl">{l_telp}</span>+62 812-3160-2472
      <span class="copy-toast">{copied_txt}</span>
    </div>
    <div class="c-pill" onclick="copyText(this, 'houseofmartynix@gmail.com', '{copied_txt}')" title="Click to copy email address">
      <span class="icon">✉️</span><span class="lbl">{l_surel}</span>houseofmartynix@gmail.com
      <span class="copy-toast">{copied_txt}</span>
    </div>
    <span class="c-pill"><span class="icon">📍</span><span class="lbl">{l_papan}</span><span class="{C.strip()}">{papan}</span></span>
    <a class="c-pill" href="https://linkedin.com/in/mrcslvknm" target="_blank" rel="noopener"><span class="icon">💼</span>linkedin.com/in/mrcslvknm</a>
    <a class="c-pill" href="https://github.com/houseofmartynix-debug" target="_blank" rel="noopener"><span class="icon">🐙</span>github.com/houseofmartynix-debug</a>
  </div>

  <div class="main">
    <div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_exp}</span><div class="sec-line"></div><span class="sec-num">01</span></div>
{exp_html}      </div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_find}</span><div class="sec-line"></div><span class="sec-num">02</span></div>
        <p class="sec-note{C}">{find_note}</p>
{find_html}      </div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_cert}</span><div class="sec-line"></div><span class="sec-num">03</span></div>
{cert_html}      </div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_edu}</span><div class="sec-line"></div><span class="sec-num">04</span></div>
        <div class="edu-card">
          <div class="edu-degree{C}">{edu_deg}</div>
          <div class="edu-school{C}">{edu_sch}</div>
          <div class="edu-year{C}">{edu_yr}</div>
        </div>
      </div>

    </div>

    <div>
      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_skill}</span><div class="sec-line"></div></div>
        <div class="skill-group">
{skill_html}        </div>
      </div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_comp}</span><div class="sec-line"></div></div>
        <div class="comp-grid">
{comp_html}        </div>
      </div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_lang}</span><div class="sec-line"></div></div>
{lang_html}      </div>

      <div class="section">
        <div class="sec-head"><span class="sec-label">{s_port}</span><div class="sec-line"></div></div>
        <a class="portfolio-header" href="https://github.com/houseofmartynix-debug" target="_blank" rel="noopener">
          <span><span class="gh-icon">🐙</span> houseofmartynix-debug</span>
          <span>↗</span>
        </a>
        <div class="repo-list">
{repo_html}        </div>
      </div>
    </div>
  </div>

</div>

<script>
function copyText(el, text, msg) {{
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(text).then(function() {{
      showToast(el, msg);
    }}).catch(function() {{
      fallbackCopy(text);
      showToast(el, msg);
    }});
  }} else {{
    fallbackCopy(text);
    showToast(el, msg);
  }}
}}
function fallbackCopy(text) {{
  var ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.select();
  try {{ document.execCommand('copy'); }} catch(e) {{}}
  document.body.removeChild(ta);
}}
function showToast(el, msg) {{
  var toast = el.querySelector('.copy-toast');
  if (toast) {{
    toast.textContent = msg || 'Copied!';
    toast.classList.add('show');
    setTimeout(function() {{ toast.classList.remove('show'); }}, 1800);
  }}
}}
</script>
</body>
</html>
'''


jv_doc = render('jv')
en_doc = render('en')
(HERE / 'index.html').write_text(jv_doc, encoding='utf-8')
(HERE / 'en').mkdir(exist_ok=True)
(HERE / 'en' / 'index.html').write_text(en_doc, encoding='utf-8')

bad = [a for a in AUDIT if not a[3]]
print(f'strings transliterated : {len(AUDIT)}')
print(f'exact round-trip       : {len(AUDIT) - len(bad)}')
print(f'needs eyeball          : {len(bad)}')
for latin, aks, back, ok in bad:
    print('  ~', latin[:70], '\n    back:', back[:70])
print(f'\nindex.html    : {len(jv_doc)} bytes')
print(f'en/index.html : {len(en_doc)} bytes')
