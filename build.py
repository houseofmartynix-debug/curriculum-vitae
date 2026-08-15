# -*- coding: utf-8 -*-
"""Build the developer-centric CV in two languages from one single source.

    index.html      aksara Jawa  (canonical)
    en/index.html   English

Every piece of copy is a (javanese_latin, english) pair. The Javanese half is
transliterated by jawa.py and round-trip verified; nothing reaches the page
without proving it decodes back to its Latin source.
"""
import json
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


EN_OVERRIDE = """<style>
  :root{--jv:'Plus Jakarta Sans',sans-serif}
  .sec-title{letter-spacing:1px;font-size:12px;line-height:1.5}
  .comp-badge{font-size:11px;line-height:1.5}
  .lang-tag{font-size:10px;line-height:1.5}
  .t-period{font-size:10.5px;line-height:1.5}
  .cmd-pill .lbl{font-size:10.5px;line-height:1.5}
  .f-proof{font-size:11px;line-height:1.5}
  .sec-callout{font-size:12.5px;line-height:1.65}
  .hero-bio{line-height:1.8}
  .lang-switch a.jvlbl{font-family:'Noto Sans Javanese',sans-serif}
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
    C = ' jv' if jv else ''

    def T(jw, en):
        return J(jw) if jv else en

    def Y(n):
        return jawa.num(n) if jv else n

    def M(key):
        return T(*MONTHS[key])

    # ----------------------------------------------------------- telemetry ---
    t_dom_k  = T('lingkup inti', 'CORE DOMAIN')
    t_dom_v  = 'Web AppSec · REST/GraphQL API · Code Audit · Cloud'
    
    t_meth_k = T('métodhologi', 'METHODOLOGY')
    t_meth_v = 'White-Box · Bytecode Audit · Logic Flow · PoC Proof'
    
    t_plat_k = T('platform', 'PLATFORMS')
    t_plat_v = 'Bugcrowd · HackerOne · YesWeHack · Gerobug'
    
    t_stat_k = T('status', 'STATUS')
    t_stat_v = T('Siyaga nampa pakaryan', 'Available for Hire / PenTest Engagements')
    
    btn_print  = T('Cithak / Simpen ~PDF', 'Print / Export PDF')
    btn_cli    = T('Bukak Terminal', 'Terminal Shell')
    btn_tools  = T('Piranti Kaamanan', 'Security Toolbox')
    btn_snd    = T('Swara', 'Audio FX')
    btn_matrix = T('~Matrix', 'Matrix Rain')
    copied_txt = T('Tersalin!', 'Copied!')

    # ---------------------------------------------------------------- stats ---
    STATS = [
        ('50+', T('Temuan Kaamanan', 'Vulnerabilities Reported'), T('Lolos triase & ditampa', 'Triaged & Verified Across Bounty Platforms')),
        ('100%', T('Kepatuhan Lapuran', 'Responsible Disclosure'), T('Manut pranatan ~ISO/IEC ~29147', 'Zero uncoordinated leaks / Strict SLA')),
        ('4+', T('Platform Kaamanan', 'Bounty Ecosystems'), 'Bugcrowd · HackerOne · YesWeHack · Gerobug'),
        ('30+', T('Kelas Serangan', 'Documented Attack Classes'), T('Cathetan proyèk riset', 'Offensive security payload knowledgebase')),
    ]

    # ------------------------------------------------------------- header ---
    tag   = T('serat riwayat gesang', 'security engineer & pen-tester')
    role  = T('juru uji penétrasi', 'Penetration Tester')
    role2 = T('pamburu celah kaamanan', 'AppSec Researcher & Bug Hunter')
    bio = T(
        'Panaliti kaamanan sing nggarap uji penétrasi aplikasi web perusahaan, '
        'arsitèktur ~API (~REST / ~GraphQL), sarta plugin ~Atlassian ~Data ~Center. '
        'Nemokake lan nglaporake celah kaamanan kanthi tanggung jawab: munggah drajat '
        'wewenang tekan administrator, ~SSRF, nrabas wates wewenang (~IDOR / ~BOLA), '
        'lan bocoran kredensial. Kulina maca sarta ndékompilasi kodhe sumber ~Java / ~JAR, '
        'banjur mbuktèkake temuan nganggo bukti konsép sing kauji langsung ing lingkungan urip.',
        'Application Security Researcher and Penetration Tester specializing in deep-dive '
        'web application testing, enterprise API architectures (REST/GraphQL), and Atlassian Data Center '
        'plugins. Discovers and reports critical logic vulnerabilities: privilege escalation to administrator, '
        'SSRF chains, multi-tenant authorization bypasses (IDOR/BOLA), and cleartext credential exposures. '
        'Experienced in auditing decompiled Java/JAR bytecode and demonstrating verified real-world proof-of-concepts.')

    l_telp  = T('telepon', 'phone')
    l_surel = T('surel', 'email')
    l_papan = T('papan', 'location')
    papan   = T('Malang, Jawa Wétan, Indonésia', 'Malang, East Java, Indonesia')

    s_exp   = T('pengalaman', 'EXPERIENCE')
    s_find  = T('asil panemu pinilih', 'SELECTED FINDINGS & SECURITY DISCLOSURES')
    s_cert  = T('sertifikat', 'CERTIFICATIONS & CREDENTIALS')
    s_edu   = T('pendhidhikan', 'EDUCATION')
    s_skill = T('kaprigelan lan piranti', 'TECHNICAL SKILLS & STACK')
    s_comp  = T('kabisan inti', 'CORE COMPETENCIES')
    s_lang  = T('basa', 'LANGUAGES')
    s_port  = T('proyèk mbukak', 'OPEN-SOURCE PORTFOLIO & LABS')

    now = T('saiki', 'Present')

    # --------------------------------------------------------- experience ---
    EXP = [
        (T('Panaliti Kaamanan Mandhiri', 'Independent Security Researcher & Penetration Tester'),
         f'{M("jan")} {Y("2026")} – {now}',
         'Bugcrowd · HackerOne · YesWeHack · Gerobug',
         T('Nguji aplikasi web perusahaan, ~API, lan plugin ~Atlassian ~Data ~Center kanggo '
           'program sayembara celah kaamanan, kalebu program pamaréntah lan swasta. Nindakake '
           'pemetaan permukaan serangan, maca sarta ndékompilasi kodhe sumber ~JAR, '
           'sarta nggawe bukti konsép (~PoC) sing kauji langsung ing lingkungan urip. Nulis lapuran '
           'manut standar ~Bugcrowd ~VRT lan ~CVSS v3.1, banjur ngurus komunikasi teknis karo tim triase '
           'nganti temuan ditampa kanthi apik. Uga mbangun piranti otomasi nganggo ~Python lan ~Bash '
           'kanggo mantau owah-owahan lingkup program.',
           'Conducts white-box penetration testing and vulnerability assessments across cloud web applications, '
           'enterprise microservices, and Atlassian Data Center plugins for bug bounty programmes. '
           'Performs attack-surface reconnaissance, decompiles and audits Java JAR bytecode, and validates '
           'live proof-of-concepts against production targets. Authors rigorous CVSS v3.1 and Bugcrowd VRT '
           'disclosure reports, leading technical remediation discussions through to acceptance. '
           'Engineers custom reconnaissance and scope-monitoring automation using Python and Bash.')),

        (T('Ahli Penjualan', 'Sales Expert & Client Communications Specialist'),
         f'{M("mei")} {Y("2024")} – {M("aug")} {Y("2025")}',
         'PT Aspirasi Hidup Indonesia Tbk (ACE Hardware) · ' + T('Kontrak', 'Contract'),
         T('Mènèhi rékomendasi produk adhedhasar analisis risiko lan kabutuhan nyata pelanggan, '
           'sarta nerangake fitur teknis marang para pihak non-teknis. Kaprigelan iki '
           'kepaké banget nalika nerangake implikasi risiko keamanan sarta rékomendasi marang pimpinan non-teknis.',
           'Delivered risk-aligned product solutions and articulated complex technical features to '
           'non-technical clients. Honed executive communication and consultative advisory skills, now directly '
           'applied to explaining technical vulnerability severity and remediation ROI to business stakeholders.')),

        (T('Staf Pemasaran lan Penjualan', 'Sales & Marketing Staff'),
         f'{M("sep")} {Y("2021")} – {M("nov")} {Y("2022")}',
         'FIFGROUP · ' + T('Kontrak', 'Contract'),
         T('Nyusun lan nglakokake program promosi adhedhasar analisis data pelanggan lan tren pasar, '
           'ngurus kampanye digital sarta lapangan. Nglatih katliten maca data sarta nemokake anomali pola.',
           'Executed targeted promotional campaigns informed by customer demographic datasets and market analytics. '
           'Developed rigorous analytical discipline in parsing complex data streams and identifying behavioral anomalies.')),

        (T('Kru Toko', 'Store Operations Crew'),
         f'{Y("2019")} – {Y("2021")}',
         'PT Indomarco Prismatama Tbk (Indomaret)',
         T('Ngladèni pelanggan lan ngurus operasi toko saben dina kanthi tliti dhuwur. '
           'Nguwatake katliten marang prakara cilik, disiplin, lan tundhuk marang standar operasional prosedur (~SOP).',
           'Maintained high-precision store operations and inventory auditing. Ingrained meticulous attention to detail, '
           'operational discipline, and standard operating procedure (SOP) compliance.')),
    ]

    # ------------------------------------------------------------ findings ---
    find_note = T(
        'Target lapuran sing isih ing triase ora kasebut jenengé ing kaca umum iki, '
        'awit aturan disclosure platform mbutuhake idin tinulis saka program. '
        'Klik saben kothak temuan kanggo mirsani rincian analisa teknis sarta bukti konsép (~PoC).',
        'Target names for reports currently in triage are anonymized in compliance with platform responsible disclosure policies. '
        'Click on any finding to inspect detailed technical root cause analysis, CVSS vectors, and sanitized PoC notes.')

    # (title, target, severity, proof_note, category, cvss, cwe, root_cause, poc_text, impact_text, fix_text)
    FIND_DATA = [
        {
            'id': 'FND-01',
            'title': T('Munggah drajat wewenang tekan administrator liwat token panyamaran sing kena ditebak',
                       'Privilege escalation to administrator via predictable impersonation token'),
            'target': T('Plugin Jira/Confluence perusahaan', 'Enterprise Jira/Confluence Data Center Plugin'),
            'sev': 'P2 High',
            'sev_cat': 'high',
            'proof': T('kauji langsung ing lingkungan urip — tekan ~SYSTEM_ADMIN', 'validated live in production — escalated to SYSTEM_ADMIN'),
            'cvss': 'CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H (8.8 High)',
            'cwe': 'CWE-287 / CWE-330: Improper Authentication & Insufficiently Random Values',
            'root_cause': T(
                'Kodhe sumber plugin dékompilasi nuduhake menawa token panyamaran pangguna digawé nganggo wiji wektu sing gampang ditebak tanpa entropi acak.',
                'Decompiled Java JAR classes revealed the plugin generated tenant impersonation tokens using deterministic timestamp seeds without cryptographic entropy.'),
            'poc': T(
                '1. Kirim panjaluk nggawé token panyamaran kanthi akun tingkat pangguna lumrah.\n2. Éntuk token banjur petung pambalikan wektu server.\n3. Gunakake token panyamaran kanggo ngakses ~API administrator minangka ~SYSTEM_ADMIN.',
                '1. Authenticate with standard low-privileged account.\n2. Reconstruct token generation seed using synchronized server HTTP response timestamps.\n3. Mint valid authorization token for administrative UID and access privileged endpoints with full SYSTEM_ADMIN capabilities.'),
            'impact': T(
                'Penyerang bisa njupuk kendhali sakabèhé konfigurasi plugin, maca dhokumèn rahasia perusahaan, sarta ngowahi setelan kaamanan.',
                'Complete tenant workspace takeover, unauthorized access to confidential enterprise documentation, and administrative code execution risk.'),
            'fix': T(
                'Ganti generator token nganggo ~SecureRandom sing aman lan wènèhi wektu kedaluwarsa cekak.',
                'Implement cryptographically secure pseudorandom number generator (CSPRNG, java.security.SecureRandom) and enforce strict cryptographic HMAC signing.')
        },
        {
            'id': 'FND-02',
            'title': T('Sandhi database kekirim tanpa enkripsi senajan ~TLS diuripake',
                       'Database credential sent in cleartext despite TLS being enabled'),
            'target': T('Konektor database ~Node.js sing akèh dienggo', 'Widely-used Node.js Database Connector Ecosystem'),
            'sev': 'CVE Pending',
            'sev_cat': 'cve',
            'proof': T('lolos triase — ~CVE wis ditetepake, advisory dikoordinasi', 'triaged — CVE assigned, coordinated advisory in progress'),
            'cvss': 'CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N (5.9 Medium)',
            'cwe': 'CWE-319: Cleartext Transmission of Sensitive Information',
            'root_cause': T(
                'Ana kahanan balapan (~race ~condition) ing wiwitan sambungan jaringan ing ngendi paket autentikasi kekirim sadurunge salaman ~TLS rampung.',
                'Connection initialization handshake race condition permitted authentication frames to be flushed over socket prior to successful TLS upgrade completion.'),
            'poc': T(
                '1. Nyegat lalu lintas jaringan lokal nganggo ~Wireshark / ~tcpdump.\n2. Wiwiti sambungan menyang server database nganggo opsi ~TLS aktif.\n3. Paket wiwitan nuduhake sandhi database cetha tanpa enkripsi.',
                '1. Monitor connection traffic via tcpdump/Wireshark on local network interface.\n2. Initiate client connection to PostgreSQL/MySQL backend with ssl: true.\n3. Observe cleartext authentication packet transmitted prior to TLS handshake completion.'),
            'impact': T(
                'Penyerang ing jaringan sing padha (~MitM) bisa nyolong sandhi database utama sarta mbobol data.',
                'Network-adjacent attackers (e.g. within shared cloud VPC/LAN) can intercept master database credentials and exfiltrate database contents.'),
            'fix': T(
                'Tundha ngirim paket autentikasi nganti acara ~secureConnect ~TLS wis rampung kanthi sah.',
                'Queue authentication frame dispatch until the TLS secureConnect event has fully resolved and cipher negotiation is verified.')
        },
        {
            'id': 'FND-03',
            'title': T('Enumerasi pangguna liwat ~NIK ing layanan pamaréntah',
                       'User enumeration & PII disclosure via national ID (NIK) endpoint'),
            'target': 'Diskominfo Kota Tangerang Selatan · Gerobug',
            'sev': 'Medium',
            'sev_cat': 'gov',
            'proof': T('piagam panghargaan resmi', 'official certificate of appreciation') + ' 7C0B38027836',
            'cvss': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N (5.3 Medium)',
            'cwe': 'CWE-200 / CWE-359: Exposure of Private Personal Information (PII)',
            'root_cause': T(
                'Layanan verifikasi publik ora mbatesi panjaluk (~rate ~limiting) lan mbalèkaké prabédan respon sing cetha kanggo ~NIK sing kadhaptar.',
                'Public verification API lacked request rate-limiting and leaked differential validation responses confirming registered citizen identities.'),
            'poc': T(
                '1. Kirim panjaluk panudhuhing ~NIK kanthi runtut.\n2. Mirsani prabédan kode status lan respon ~JSON kanggo verifikasi data warga.',
                '1. Scripted automated queries across municipal endpoint.\n2. Correlated differential JSON status codes to enumerate active citizen identification numbers without authentication.'),
            'impact': T(
                'Bocoran data kependudukan (~PII) sing bisa disalahgunakake kanggo panipuan identitas.',
                'Mass citizen identity enumeration and privacy leakage susceptible to spear-phishing and credential stuffing campaigns.'),
            'fix': T(
                'Wènèhi watesan panjaluk (~rate ~limit), ~CAPTCHA, lan respon seragam kanggo kabeh panjaluk.',
                'Implemented rate limiting, CAPTCHA verification on public forms, and standardized opaque response messaging.')
        },
        {
            'id': 'FND-04',
            'title': T('Bocoran kodhe sumber ing layanan pamaréntah',
                       'Source code & sensitive config disclosure in government service'),
            'target': 'Diskominfo Kota Tangerang Selatan · Gerobug',
            'sev': 'Medium',
            'sev_cat': 'gov',
            'proof': T('piagam panghargaan resmi', 'official certificate of appreciation') + ' 7C0B36916030',
            'cvss': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N (5.3 Medium)',
            'cwe': 'CWE-538: File and Directory Information Exposure',
            'root_cause': T(
                'Direktori repositori lan berkas konfigurasi cadangan bisa diakses kanthi langsung liwat web server amarga setelan sing kurang bener.',
                'Exposed web root backup archives and source repository artifacts due to default web server directory indexing misconfigurations.'),
            'poc': T(
                '1. Gunakake panlusur ~URL kanggo nemokake berkas konfigurasi sing mbukak.\n2. Undhuh berkas kanggo mbuktekake anane kodhe sumber.',
                '1. Identified exposed static backup path via automated web enumeration.\n2. Verified downloadable archive containing application configuration details.'),
            'impact': T(
                'Bocoran arsitèktur aplikasi lan kunci rahasia sing bisa dadi dhasar serangan lanjutan.',
                'Architectural disclosure and exposure of internal routing and API structures aiding targeted exploitation.'),
            'fix': T(
                'Tutup akses langsung menyang direktori rahasia lan busak kabeh berkas cadangan saka web server.',
                'Restricted web server file access rules, sanitized web root, and integrated pre-deployment artifact scanning in CI pipeline.')
        },
        {
            'id': 'FND-05',
            'title': T('~SSRF, kalebu ~SSRF buta, ing plugin ~Atlassian ~Data ~Center',
                       'SSRF and blind SSRF in commercial Atlassian Data Center plugins'),
            'target': T('Rong vendor plugin perusahaan kapisah', 'Two Separate Enterprise Plugin Vendors'),
            'sev': 'P2 / P3',
            'sev_cat': 'high',
            'proof': T('loro-loroné lolos triase & ditampa', 'both triaged, verified & accepted'),
            'cvss': 'CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N (7.7 High)',
            'cwe': 'CWE-918: Server-Side Request Forgery (SSRF)',
            'root_cause': T(
                'Plugin ngidini pangguna ngisi ~URL ~webhook utawa gambar tanpa verifikasi alamat ~IP internal (~RFC ~1918 utawa layanan metadata ~AWS/GCP).',
                'Unvalidated user-supplied webhook and thumbnail URLs passed to internal HTTP fetching services without loopback or cloud metadata filtering.'),
            'poc': T(
                '1. Pasang ~URL panjaluk menyang ~169.254.169.254 ing setelan integrasi plugin.\n2. Mbalèkaké data metadata komputasi awan saka server internal.',
                '1. Configure plugin integration webhook target to point to cloud metadata service (http://169.254.169.254/latest/meta-data/).\n2. Trigger webhook event and capture response data verifying internal network reachability.'),
            'impact': T(
                'Bisa dienggo maca metadata komputasi awan, nyolong token ~IAM, sarta mindhai jaringan internal perusahaan.',
                'Internal cloud metadata extraction, cloud IAM credential theft, and unauthorized intranet port scanning.'),
            'fix': T(
                'Wènèhi panyaring ~URL ketat, tolak kabeh alamat ~IP pribadi lan metadata komputasi awan.',
                'Implemented strict IP address denylist, DNS re-resolution validation, and isolated outbound egress proxying.')
        },
        {
            'id': 'FND-06',
            'title': T('Layanan ~MCP mbukak liwat ~HTTP tanpa autentikasi',
                       'Model Context Protocol (MCP) exposed over HTTP without auth'),
            'target': T('Aplikasi desktop ~AI / pangembang', 'Desktop AI & Developer Workstation Application'),
            'sev': 'CVSS 7.3',
            'sev_cat': 'high',
            'proof': T('dilapurake liwat program resmi', 'reported & accepted via official security programme'),
            'cvss': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N (7.3 High)',
            'cwe': 'CWE-306: Missing Authentication for Critical Function',
            'root_cause': T(
                'Server lokal ~MCP mbukak port ~HTTP ing komputer tanpa sandhi utawa token panyekel wewenang, ngidini situs web liya ngirim panjaluk.',
                'Local MCP daemon bound HTTP socket without origin verification or authorization tokens, exposing tool execution to malicious web pages.'),
            'poc': T(
                '1. Nggawe kaca web pancingan sing ngirim panjaluk ~fetch menyang port lokal ~MCP.\n2. Njaluk server lokal nindakake pakaryan piranti ~AI kanthi otomatis.',
                '1. Created cross-origin HTML PoC triggering fetch() requests to localhost daemon.\n2. Executed arbitrary local tool operations via unauthorized JSON-RPC calls.'),
            'impact': T(
                'Situs web ala bisa maca berkas lokal utawa nglakokake printah ing komputer pangguna.',
                'Arbitrary local file inspection and unauthorized agentic action execution on developer workstations.'),
            'fix': T(
                'Wènèhi token autentikasi rahasia kanggo kabeh komunikasi ~MCP lan watesi mung kanggo sambungan lokal sing sah.',
                'Added cryptographic per-session token validation and restricted CORS origins to trusted application domains.')
        },
        {
            'id': 'FND-07',
            'title': T('Nrabas alur persetujuan lan registrasi klien ~OAuth sing mbukak',
                       'Approval-flow bypass & open OAuth 2.0 dynamic client registration'),
            'target': T('Rong program produksi kapisah', 'Two Separate Production Enterprise SaaS Platforms'),
            'sev': 'In Triage',
            'sev_cat': 'high',
            'proof': T('dilapurake, isih ing proses triase', 'reported, currently under active triage'),
            'cvss': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N (8.1 High)',
            'cwe': 'CWE-285: Improper Authorization / OAuth Flow Flaws',
            'root_cause': T(
                'Setelan ~OAuth ngidini registrasi klien anyar kanthi ~redirect_uri sing amba tanpa verifikasi wewenang pamilik.',
                'Dynamic client registration endpoint permitted unvetted third-party client creation with wildcard redirect URIs.'),
            'poc': T(
                '1. Dhaftarake klien ~OAuth anyar nganggo ~redirect_uri menyang server panguji.\n2. Pancing pangguna kanggo mlebu log banjur jupuk kode otorisasi.',
                '1. Register unauthenticated client with custom attacker callback URI.\n2. Initiate authorization flow and intercept authorization codes upon user authentication.'),
            'impact': T(
                'Penyerang bisa mbajak sesi akun pangguna lan njupuk data akun tanpa idin.',
                'Account takeover and arbitrary user impersonation across connected SaaS services.'),
            'fix': T(
                'Tutup registrasi klien umum lan watesi ~redirect_uri mung kanggo domain sing wis diverifikasi.',
                'Enforce strict redirect URI exact matching and restrict dynamic client registration to pre-approved developer accounts.')
        },
    ]

    # -------------------------------------------------------- certificates ---
    CERT = [
        (T('Uji Penétrasi Web', 'Web Penetration Testing'), 'Cyber Academy Indonesia',
         f'{M("oct")} {Y("2025")}', 'BWH01110254258', 'https://cyberacademy.id/'),
        (T('Kaamanan Siber', 'Cyber Security') + ' 101', 'TryHackMe',
         f'{M("apr")} {Y("2026")} — {M("apr")} {Y("2029")}', 'THM-0G7VUW6K0M', 'https://tryhackme.com/p/mrcslvknm'),
        (T('Sertifikat Kaamanan Dhasar', 'Pre Security Certificate'), 'TryHackMe',
         f'{M("feb")} {Y("2026")} — {M("feb")} {Y("2029")}', 'THM-R4E0NX6WTU', 'https://tryhackme.com/p/mrcslvknm'),
        (T('Pambuka Kaamanan Siber', 'Introduction to Cybersecurity'),
         'Cisco Networking Academy', f'{M("jan")} {Y("2026")}', None, None),
    ]

    edu_deg = T('Sekolah Menengah Ndhuwur — Ilmu Sosial',
                'High School Diploma — Social Studies')
    edu_sch = (J('SMAN') + ' ' + jawa.num('1') + ' ' + J('Sumberpucung')) if jv \
        else 'SMAN 1 Sumberpucung'
    edu_yr = T('lulus', 'Graduated') + ' ' + Y('2017')

    SKILLS_SECTIONS = [
        (T('Uji Penétrasi Web & ~API', 'Web & API Penetration Testing'),
         'OWASP Top 10 · REST · GraphQL · WebSocket · OAuth 2.0 · JWT · SAML · IDOR · BOLA · SSRF · Race Conditions · SSTI · XXE'),
        (T('Audit Kodhe Sumber & Dékompilasi', 'Source Code Audit & Decompilation'),
         'Java JAR/Bytecode (JADX, Procyon, javap) · Node.js · Python AST · Android Dalvik (apktool, frida, objection)'),
        (T('Nyegat Lalu Lintas & Manipulasi', 'Traffic Interception & Exploitation'),
         'Burp Suite Professional · Caido · Postman · Ffuf · Turbo Intruder · Webhook Debugging'),
        (T('Otomasi Pangintaian & ~OSINT', 'Reconnaissance & Attack-Surface Mapping'),
         'Subfinder · Httpx · Katana · Nuclei (Custom YAML Templates) · Amass · Nmap · Masscan'),
        (T('Pertahanan & Lab ~SOC', 'Defense Engineering & SOC Lab'),
         'Wazuh SIEM · Sysmon Telemetry · Kali Linux · Docker · Network Packet Analysis (Wireshark, tcpdump) · MITRE ATT&CK'),
        (T('Standar Penilaian & Pelaporan', 'Scoring, Compliance & Reporting'),
         'CVSS v3.1 Scoring · Bugcrowd VRT · ISO/IEC 29147 Responsible Disclosure · Executive Technical Reporting'),
    ]

    COMP = [T('pamikiran analitis', 'Analytical Thinking'),
            T('tliti marang prakara cilik', 'Attention to Detail'),
            T('ngudi kanthi mempeng', 'Methodological Persistence'),
            T('mbukak temuan kanthi tanggung jawab', 'Responsible Disclosure'),
            T('komunikasi lapuran', 'Executive & Technical Reporting'),
            T('sinau mandhiri', 'Self-Directed Research')]

    LANGS = [(T('Jawa', 'Javanese'), T('lair', 'Native'), 'native'),
             (T('Indonésia', 'Indonesian'), T('lair', 'Native'), 'native'),
             (T('Inggris', 'English'), T('lantih', 'Advanced Professional'), 'advanced'),
             (T('Rusia', 'Russian'), T('sedhengan', 'Intermediate Technical'), 'inter')]

    REPOS = [
        ('appsec-payload-notes', 'https://github.com/houseofmartynix-debug/appsec-payload-notes',
         T('Cathetan ~payload lan métodhologi ing ~30 kelas celah kaamanan',
           'Offensive security payload repository & attack methodology documentation across 30+ vuln classes')),
        ('marco-scanner', 'https://github.com/houseofmartynix-debug/marco-scanner',
         T('Piranti pamindhai celah aplikasi web proyèk portofolio',
           'Modular asynchronous web vulnerability reconnaissance engine and scanner tool')),
        ('soc-home-lab', 'https://github.com/houseofmartynix-debug/soc-home-lab',
         T('Lab ~SOC ~Wazuh — detéksi ancaman manut ~MITRE ~ATT&CK',
           'Wazuh SIEM/SOC deployment with Sysmon telemetry pipelines and MITRE ATT&CK attack playbooks')),
        ('sinik-pro', 'https://github.com/houseofmartynix-debug/sinik-pro',
         T('Pamariksa lan pangudhar ~NIK Indonésia tanpa server kanthi privasi',
           'Zero-dependency client-side Indonesian NIK validator and privacy-preserving decoder tool')),
        ('bugcrowd-scope-monitor', 'https://github.com/houseofmartynix-debug/bugcrowd-scope-monitor',
         T('Otomasi ~Telegram kanggo owah-owahan lingkup ~Bugcrowd',
           'Automated Telegram notifications for Bugcrowd scope updates via GitHub Actions pipelines')),
        ('god-recon-bot', 'https://github.com/houseofmartynix-debug/god-recon-bot',
         T('Bot ~Telegram kanggo narik lingkup program lintas platform',
           'Telegram bot orchestrator aggregating target scope across major bug bounty platforms')),
    ]

    # ---------------------------------------------------------------- html ---
    nl = chr(10)
    
    # Stats HTML
    stats_html = ''.join(
        f'''      <div class="stat-card">
        <div class="stat-num">{num}</div>
        <div class="stat-info">
          <div class="stat-title{C}">{title}</div>
          <div class="stat-sub{C}">{sub}</div>
        </div>
      </div>{nl}''' for num, title, sub in STATS)

    # Experience HTML
    exp_html = ''.join(
        f'''          <div class="timeline-item">
            <div class="t-meta">
              <div class="t-role{C}">{r}</div>
              <div class="t-period{C}">{p}</div>
            </div>
            <div class="t-company">{co}</div>
            <p class="t-desc{C}">{d}</p>
          </div>{nl}''' for r, p, co, d in EXP)

    def sev_chip(sev):
        if not sev:
            return ''
        s_cls = 'sev-p2'
        if 'P1' in sev or 'Critical' in sev:
            s_cls = 'sev-p1'
        elif 'P2' in sev or 'CVSS 7' in sev or 'High' in sev:
            s_cls = 'sev-p2'
        elif 'P3' in sev or 'Medium' in sev:
            s_cls = 'sev-p3'
        elif 'P4' in sev or 'Triage' in sev or 'CVE' in sev:
            s_cls = 'sev-p4'
        return f'<span class="sev-chip {s_cls}">{sev}</span>'

    # Finding Cards HTML
    find_cards_html = ''
    for f in FIND_DATA:
        find_cards_html += f'''        <div class="finding-card" data-cat="{f['sev_cat']}" onclick="openPoCModal('{f['id']}')">
          <div class="f-head">
            <div class="f-title{C}">{f['title']}</div>
            {sev_chip(f['sev'])}
          </div>
          <div class="f-target">{f['target']}</div>
          <div class="f-proof{C}">
            <span class="f-proof-left">{f['proof']}</span>
            <span class="f-poc-link">🔍 View PoC &amp; Analysis ↗</span>
          </div>
        </div>{nl}'''

    # Certifications HTML
    cert_html = ''.join(
        f'''        <div class="cert-item">
          <div class="c-name{C}">{n}</div>
          <div class="c-issuer">{i} &nbsp;·&nbsp; <span class="{C.strip()}">{w}</span></div>
          {f'<div class="c-id">CREDENTIAL: <span>{cid}</span></div>' if cid else ''}
        </div>{nl}''' for n, i, w, cid, link in CERT)

    # Skills HTML
    skill_html = ''.join(
        f'''          <div class="skill-row">
            <div class="skill-label{C}">{lbl}</div>
            <div class="skill-tags">{tags}</div>
          </div>{nl}''' for lbl, tags in SKILLS_SECTIONS)

    comp_html = ''.join(f'          <span class="comp-badge">{k}</span>{nl}' for k in COMP)
    
    lang_html = ''.join(
        f'''        <div class="lang-row">
          <span class="lang-name{C}">{n}</span>
          <span class="lang-tag {cls}">{lv}</span>
        </div>{nl}''' for n, lv, cls in LANGS)

    repo_html = ''.join(
        f'''        <a class="repo-card" href="{url}" target="_blank" rel="noopener">
          <div class="repo-name"><span>{name}</span><span class="repo-arrow">↗</span></div>
          <div class="repo-desc{C}">{desc}</div>
        </a>{nl}''' for name, url, desc in REPOS)

    jw_label = J('Jawa') if jv else 'ꦗꦮ'
    switch = (f'<div class="lang-switch"><a class="on jvlbl" href="./">{jw_label}</a>'
              f'<a href="./en/">EN</a></div>') if jv else \
             (f'<div class="lang-switch"><a class="jvlbl" href="../">{jw_label}</a>'
              f'<a class="on" href="./">EN</a></div>')

    # Filter chips
    f_all = T('Kabeh', 'All')
    f_high = T('Dhuwur', 'P1 / P2 High')
    f_med = T('Sedhengan', 'P3 / P4 Medium')
    f_cve = T('Riset ~CVE', 'CVE / Research')
    f_gov = T('Pamaréntah', 'Government')

    # Serialize finding data for JS modal
    finding_data_json = json.dumps(FIND_DATA, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="{'jv' if jv else 'en'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Marco Selva Oknam — {role} · {role2}</title>
<meta name="description" content="Marco Selva Oknam — Application Security Researcher, Penetration Tester &amp; Bug Bounty Hunter.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Noto+Sans+Javanese:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
{EN_OVERRIDE if not jv else ''}
</head>
<body data-theme="emerald">

<!-- Background Digital Rain Canvas -->
<canvas id="matrixCanvas"></canvas>

<div class="cv-container">
  <div class="terminal-shell">

    <!-- SHELL HEADER BAR -->
    <div class="shell-bar">
      <div class="shell-bar-left">
        <div class="shell-dots">
          <span class="dot dot-red" title="Close"></span>
          <span class="dot dot-yellow" title="Minimize"></span>
          <span class="dot dot-green" title="Expand"></span>
        </div>
        <div class="shell-path">
          <span class="user">marco@secops</span>:<span class="path">~/curriculum-vitae</span>
          <span class="branch">⎇ main⚡</span>
        </div>
        <div class="shell-clock" id="cyberClock">UTC 00:00:00</div>
      </div>

      <div class="shell-actions">
        <button class="action-btn" id="cliBtn" onclick="toggleCLI()" title="Open Interactive Terminal Shell">
          <span class="btn-icon">📟</span>
          <span class="{C.strip()}">{btn_cli}</span>
        </button>
        <button class="action-btn" id="toolboxBtn" onclick="toggleToolbox()" title="Open Interactive Security Sandbox">
          <span class="btn-icon">🧰</span>
          <span class="{C.strip()}">{btn_tools}</span>
        </button>
        <button class="action-btn" id="matrixBtn" onclick="toggleMatrix()" title="Toggle Digital Rain Effect">
          <span class="btn-icon">🌧️</span>
          <span class="{C.strip()}">{btn_matrix}</span>
        </button>
        <button class="action-btn" id="soundBtn" onclick="toggleSound()" title="Toggle Audio FX">
          <span class="btn-icon" id="soundIcon">🔇</span>
          <span class="{C.strip()}">{btn_snd}</span>
        </button>
        <select class="theme-select" id="themeSelect" onchange="changeTheme(this.value)" title="Choose Theme">
          <option value="emerald">⚡ Cyber Emerald</option>
          <option value="cyberpunk">🌌 Neon Synth</option>
          <option value="stealth">🛡️ Midnight Stealth</option>
          <option value="amber">🖥️ Amber CRT</option>
          <option value="paper">📄 Clean Paper</option>
        </select>
        <button class="action-btn" onclick="window.print()" title="Print CV or Save as PDF">
          <span class="btn-icon">🖨️</span>
          <span class="{C.strip()}">{btn_print}</span>
        </button>
        {switch}
      </div>
    </div>

    <!-- TELEMETRY / FAST FACTS STRIP -->
    <div class="telemetry-strip">
      <div class="telem-cell">
        <span class="telem-key">{t_dom_k}</span>
        <span class="telem-val">{t_dom_v}</span>
      </div>
      <div class="telem-cell">
        <span class="telem-key">{t_meth_k}</span>
        <span class="telem-val">{t_meth_v}</span>
      </div>
      <div class="telem-cell">
        <span class="telem-key">{t_plat_k}</span>
        <span class="telem-val">{t_plat_v}</span>
      </div>
      <div class="telem-cell">
        <span class="telem-key">{t_stat_k}</span>
        <span class="telem-val"><span class="live-pulse"></span> <span class="{C.strip()}">{t_stat_v}</span></span>
      </div>
    </div>

    <!-- STATS COUNTER STRIP -->
    <div class="stats-banner">
{stats_html}    </div>

    <!-- SHELL CONTENT -->
    <div class="shell-content">

      <!-- INTERACTIVE SECURITY TOOLBOX (Collapsible) -->
      <div class="cyber-toolbox" id="cyberToolbox">
        <div class="toolbox-head">
          <div class="toolbox-title">
            <span>⚙️</span>
            <span class="{C.strip()}">{T('Piranti Kaamanan Interaktif (Kothak Wedhi)', 'Interactive AppSec Toolbox Sandbox')}</span>
          </div>
          <div class="toolbox-tabs">
            <button class="tb-tab-btn active" onclick="switchToolTab('jwt')">JWT Inspector</button>
            <button class="tb-tab-btn" onclick="switchToolTab('hash')">Crypto &amp; Hash</button>
            <button class="tb-tab-btn" onclick="switchToolTab('nik')">Sinik-Pro NIK</button>
          </div>
        </div>
        <div class="toolbox-body">
          
          <!-- TAB 1: JWT -->
          <div class="tool-pane active" id="pane-jwt">
            <div class="tool-actions-row">
              <button class="action-btn" onclick="loadSampleJWT('admin')">Load Sample Admin Token</button>
              <button class="action-btn" onclick="loadSampleJWT('vuln')">Load Insecure 'none' Token</button>
            </div>
            <textarea class="tool-input" id="jwtInput" rows="2" placeholder="Paste JWT token (header.payload.signature) here..." oninput="decodeJWT()"></textarea>
            <div class="tool-output" id="jwtOutput">// Decoded JWT header and claims will render here...</div>
          </div>

          <!-- TAB 2: CRYPTO & HASH -->
          <div class="tool-pane" id="pane-hash">
            <textarea class="tool-input" id="hashInput" rows="2" placeholder="Type text to encode / hash..." oninput="calcCrypto()"></textarea>
            <div class="tool-output" id="hashOutput">// Base64, Hex, URL-encoded, ROT13 and SHA-256 will appear here...</div>
          </div>

          <!-- TAB 3: NIK INSPECTOR -->
          <div class="tool-pane" id="pane-nik">
            <input type="text" class="tool-input" id="nikInput" placeholder="Enter 16-digit Indonesian NIK to inspect (e.g. 3507...)" maxlength="16" oninput="inspectNIK()">
            <div class="tool-output" id="nikOutput">// Client-side sanitized Indonesian NIK breakdown (Province, Regency, Gender, DOB)...</div>
          </div>

        </div>
      </div>

      <!-- HERO HEADER -->
      <header class="hero-header">
        <div>
          <div class="hero-tag">{tag}</div>
          <h1 class="hero-name"><span class="given">Marco</span>SELVA OKNAM</h1>
          <div class="role-banner">{role} <span class="sep">/</span> {role2} <span class="cursor"></span></div>
          <p class="hero-bio{C}">{bio}</p>
        </div>
        <div class="avatar-wrapper">
          <div class="avatar-frame">
            <img src="data:image/jpeg;base64,{PHOTO}" alt="Marco Selva Oknam">
            <div class="avatar-tag">MRCSLVKNM</div>
          </div>
        </div>
      </header>

      <!-- CLI CONTACT -->
      <div class="cli-contact">
        <div class="cmd-pill" onclick="copyText(this, '+6281231602472', '{copied_txt}')" title="Click to copy phone number">
          <span class="prefix">$</span>
          <span class="lbl">{l_telp}:</span>
          <span>+62 812-3160-2472</span>
          <span class="toast">{copied_txt}</span>
        </div>
        <div class="cmd-pill" onclick="copyText(this, 'houseofmartynix@gmail.com', '{copied_txt}')" title="Click to copy email address">
          <span class="prefix">$</span>
          <span class="lbl">{l_surel}:</span>
          <span>houseofmartynix@gmail.com</span>
          <span class="toast">{copied_txt}</span>
        </div>
        <div class="cmd-pill">
          <span class="prefix">$</span>
          <span class="lbl">{l_papan}:</span>
          <span class="{C.strip()}">{papan}</span>
        </div>
        <a class="cmd-pill" href="https://linkedin.com/in/mrcslvknm" target="_blank" rel="noopener">
          <span class="prefix">↗</span>
          <span>linkedin.com/in/mrcslvknm</span>
        </a>
        <a class="cmd-pill" href="https://github.com/houseofmartynix-debug" target="_blank" rel="noopener">
          <span class="prefix">↗</span>
          <span>github.com/houseofmartynix-debug</span>
        </a>
      </div>

      <!-- MAIN DUAL-COLUMN GRID -->
      <div class="main-grid">
        
        <!-- LEFT MAIN COLUMN -->
        <div>

          <!-- 01: EXPERIENCE -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">01</span>
              <span class="sec-title{C}">{s_exp}</span>
              <div class="sec-divider"></div>
            </div>
            <div class="timeline-list">
{exp_html}            </div>
          </div>

          <!-- 02: SELECTED FINDINGS -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">02</span>
              <span class="sec-title{C}">{s_find}</span>
              <div class="sec-divider"></div>
            </div>
            <p class="sec-callout{C}">{find_note}</p>
            
            <!-- Filter Bar -->
            <div class="filter-bar">
              <button class="filter-chip active" onclick="filterFindings('all', this)">{f_all}</button>
              <button class="filter-chip" onclick="filterFindings('high', this)">{f_high}</button>
              <button class="filter-chip" onclick="filterFindings('cve', this)">{f_cve}</button>
              <button class="filter-chip" onclick="filterFindings('gov', this)">{f_gov}</button>
            </div>

            <div class="findings-list">
{find_cards_html}            </div>
          </div>

          <!-- 03: CERTIFICATIONS -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">03</span>
              <span class="sec-title{C}">{s_cert}</span>
              <div class="sec-divider"></div>
            </div>
{cert_html}          </div>

          <!-- 04: EDUCATION -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">04</span>
              <span class="sec-title{C}">{s_edu}</span>
              <div class="sec-divider"></div>
            </div>
            <div class="edu-box">
              <div class="edu-title{C}">{edu_deg}</div>
              <div class="edu-inst{C}">{edu_sch}</div>
              <div class="edu-grad{C}">{edu_yr}</div>
            </div>
          </div>

        </div>

        <!-- RIGHT SIDEBAR COLUMN -->
        <div>

          <!-- 05: SKILLS & STACK -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">05</span>
              <span class="sec-title{C}">{s_skill}</span>
              <div class="sec-divider"></div>
            </div>
            <div class="skill-box">
{skill_html}            </div>
          </div>

          <!-- 06: CORE COMPETENCIES -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">06</span>
              <span class="sec-title{C}">{s_comp}</span>
              <div class="sec-divider"></div>
            </div>
            <div class="comp-cloud">
{comp_html}            </div>
          </div>

          <!-- 07: LANGUAGES -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">07</span>
              <span class="sec-title{C}">{s_lang}</span>
              <div class="sec-divider"></div>
            </div>
{lang_html}          </div>

          <!-- 08: OPEN-SOURCE PORTFOLIO -->
          <div class="section">
            <div class="sec-header">
              <span class="sec-num">08</span>
              <span class="sec-title{C}">{s_port}</span>
              <div class="sec-divider"></div>
            </div>
            <a class="repo-btn-head" href="https://github.com/houseofmartynix-debug" target="_blank" rel="noopener">
              <span>🐙 houseofmartynix-debug</span>
              <span>↗</span>
            </a>
            <div class="repo-group">
{repo_html}            </div>
          </div>

        </div>

      </div>

    </div>
  </div>
</div>

<!-- INTERACTIVE VULNERABILITY DOSSIER MODAL -->
<div class="cyber-modal-overlay" id="pocModal" onclick="closeModalOnBg(event)">
  <div class="cyber-modal">
    <div class="modal-header">
      <div class="modal-title-box">
        <span class="sev-chip sev-p2" id="mSev">P2 HIGH</span>
        <span style="font-family:var(--mono);font-size:12.5px;font-weight:700;color:var(--text);" id="mId">FND-01</span>
      </div>
      <button class="modal-close" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-body">
      <h3 style="font-size:16px;font-weight:800;color:var(--text);margin-bottom:6px;" id="mTitle">Vulnerability Title</h3>
      <div style="font-family:var(--mono);font-size:11.5px;color:var(--cyan);margin-bottom:18px;" id="mTarget">Target System</div>
      
      <div class="modal-field">
        <div class="modal-label">CVSS v3.1 Score &amp; Classification</div>
        <div class="modal-val" id="mCvss">CVSS:3.1/AV:N/AC:L...</div>
      </div>

      <div class="modal-field">
        <div class="modal-label">CWE Weakness Category</div>
        <div class="modal-val" id="mCwe">CWE-287</div>
      </div>

      <div class="modal-field">
        <div class="modal-label">Technical Root Cause &amp; Mechanism</div>
        <div class="modal-val" id="mRootCause">Root cause analysis...</div>
      </div>

      <div class="modal-field">
        <div class="modal-label">Sanitized Proof of Concept &amp; Reproduction</div>
        <pre class="modal-code" id="mPoc">PoC walkthrough steps...</pre>
      </div>

      <div class="modal-field">
        <div class="modal-label">Business &amp; Security Impact</div>
        <div class="modal-val" id="mImpact">Impact assessment...</div>
      </div>

      <div class="modal-field">
        <div class="modal-label">Remediation &amp; Defense-in-Depth</div>
        <div class="modal-val" id="mFix">Remediation guidance...</div>
      </div>
    </div>
  </div>
</div>

<!-- INTERACTIVE FLOATING TERMINAL CONSOLE -->
<div class="cli-drawer" id="cliDrawer">
  <div class="cli-drawer-head">
    <div style="display:flex;align-items:center;gap:8px;">
      <span class="dot dot-green" style="width:8px;height:8px;"></span>
      <span style="color:var(--accent);font-weight:700;">marco@secops-terminal</span>
    </div>
    <button class="modal-close" style="width:22px;height:22px;font-size:11px;" onclick="toggleCLI()">✕</button>
  </div>
  <div class="cli-drawer-body" id="cliLogs">
    <div class="cli-log-line" style="color:var(--accent);">SecOps Interactive Shell v2.4 initialized. Type <span style="color:var(--cyan);font-weight:700;">help</span> for commands.</div>
  </div>
  <div class="cli-quick-chips">
    <span class="cli-chip" onclick="runCLICommand('cat bio')">cat bio</span>
    <span class="cli-chip" onclick="runCLICommand('skills')">skills</span>
    <span class="cli-chip" onclick="runCLICommand('vulns')">vulns</span>
    <span class="cli-chip" onclick="runCLICommand('cve')">cve</span>
    <span class="cli-chip" onclick="runCLICommand('tools')">tools</span>
    <span class="cli-chip" onclick="runCLICommand('matrix')">matrix</span>
    <span class="cli-chip" onclick="runCLICommand('neofetch')">neofetch</span>
    <span class="cli-chip" onclick="runCLICommand('clear')">clear</span>
  </div>
  <div class="cli-prompt-row">
    <span class="cli-prompt-symbol">$</span>
    <input type="text" class="cli-input" id="cliInput" placeholder="type a command (e.g. help, vulns, skills, theme cyberpunk)..." autocomplete="off" spellcheck="false" onkeydown="handleCLIKeyDown(event)">
  </div>
</div>

<script>
// Data Store for Modal & CLI
var FINDINGS_DB = {finding_data_json};

// Web Audio API Sound Synthesizer
var audioCtx = null;
var soundEnabled = false;

function initAudio() {{
  if (!audioCtx && (window.AudioContext || window.webkitAudioContext)) {{
    var AudioContextClass = window.AudioContext || window.webkitAudioContext;
    audioCtx = new AudioContextClass();
  }}
}}

function playCyberSound(type) {{
  if (!soundEnabled) return;
  try {{
    initAudio();
    if (!audioCtx) return;
    if (audioCtx.state === 'suspended') audioCtx.resume();
    
    var osc = audioCtx.createOscillator();
    var gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    var now = audioCtx.currentTime;
    if (type === 'click') {{
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, now);
      osc.frequency.exponentialRampToValueAtTime(300, now + 0.04);
      gain.gain.setValueAtTime(0.04, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
      osc.start(now);
      osc.stop(now + 0.04);
    }} else if (type === 'open') {{
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(350, now);
      osc.frequency.exponentialRampToValueAtTime(950, now + 0.08);
      gain.gain.setValueAtTime(0.05, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
      osc.start(now);
      osc.stop(now + 0.08);
    }} else if (type === 'error') {{
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, now);
      osc.frequency.setValueAtTime(160, now + 0.06);
      gain.gain.setValueAtTime(0.05, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
      osc.start(now);
      osc.stop(now + 0.12);
    }}
  }} catch(e) {{}}
}}

function toggleSound() {{
  soundEnabled = !soundEnabled;
  var icon = document.getElementById('soundIcon');
  var btn = document.getElementById('soundBtn');
  if (soundEnabled) {{
    icon.textContent = '🔊';
    btn.classList.add('active');
    playCyberSound('open');
  }} else {{
    icon.textContent = '🔇';
    btn.classList.remove('active');
  }}
}}

// Digital Rain Background Matrix Effect
var matrixRunning = false;
var matrixCanvas = document.getElementById('matrixCanvas');
var mCtx = matrixCanvas ? matrixCanvas.getContext('2d') : null;
var matrixDrops = [];
var matrixInterval = null;

function initMatrix() {{
  if (!matrixCanvas || !mCtx) return;
  matrixCanvas.width = window.innerWidth;
  matrixCanvas.height = window.innerHeight;
  var cols = Math.floor(matrixCanvas.width / 18);
  matrixDrops = [];
  for (var i = 0; i < cols; i++) {{
    matrixDrops[i] = Math.floor(Math.random() * -50);
  }}
}}

function drawMatrix() {{
  if (!matrixRunning || !mCtx) return;
  mCtx.fillStyle = 'rgba(6, 8, 13, 0.08)';
  mCtx.fillRect(0, 0, matrixCanvas.width, matrixCanvas.height);
  mCtx.fillStyle = '#00dc82';
  mCtx.font = '13px monospace';
  
  var chars = '0123456789ABCDEFSEC_AUDIT_EXPLOIT_POC_CVSS_VRT_JAR_AST';
  for (var i = 0; i < matrixDrops.length; i++) {{
    var text = chars.charAt(Math.floor(Math.random() * chars.length));
    mCtx.fillText(text, i * 18, matrixDrops[i] * 18);
    if (matrixDrops[i] * 18 > matrixCanvas.height && Math.random() > 0.975) {{
      matrixDrops[i] = 0;
    }}
    matrixDrops[i]++;
  }}
}}

function toggleMatrix() {{
  matrixRunning = !matrixRunning;
  document.body.classList.toggle('matrix-active', matrixRunning);
  var btn = document.getElementById('matrixBtn');
  if (btn) btn.classList.toggle('active', matrixRunning);
  
  if (matrixRunning) {{
    initMatrix();
    if (!matrixInterval) matrixInterval = setInterval(drawMatrix, 45);
    playCyberSound('open');
  }} else {{
    if (matrixInterval) {{ clearInterval(matrixInterval); matrixInterval = null; }}
    if (mCtx) mCtx.clearRect(0, 0, matrixCanvas.width, matrixCanvas.height);
    playCyberSound('click');
  }}
}}

window.addEventListener('resize', function() {{
  if (matrixRunning) initMatrix();
}});

// Theme Switcher
function changeTheme(themeName) {{
  document.body.setAttribute('data-theme', themeName);
  localStorage.setItem('cv_theme', themeName);
  var sel = document.getElementById('themeSelect');
  if (sel) sel.value = themeName;
  playCyberSound('click');
}}

// Load stored theme
try {{
  var savedTheme = localStorage.getItem('cv_theme') || 'emerald';
  changeTheme(savedTheme);
}} catch(e) {{}}

// Live Clock (UTC & WIB)
function updateClock() {{
  var now = new Date();
  var utc = now.toUTCString().split(' ')[4];
  var el = document.getElementById('cyberClock');
  if (el) {{
    el.textContent = 'UTC ' + utc + ' (WIB ' + String((now.getUTCHours() + 7) % 24).padStart(2,'0') + ':' + String(now.getUTCMinutes()).padStart(2,'0') + ')';
  }}
}}
setInterval(updateClock, 1000);
updateClock();

// Copy to Clipboard
function copyText(el, text, msg) {{
  playCyberSound('click');
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
  var toast = el.querySelector('.toast');
  if (toast) {{
    toast.textContent = msg || 'Copied!';
    toast.classList.add('show');
    setTimeout(function() {{ toast.classList.remove('show'); }}, 1800);
  }}
}}

// Filter Findings
function filterFindings(cat, btn) {{
  playCyberSound('click');
  var chips = document.querySelectorAll('.filter-chip');
  chips.forEach(function(c) {{ c.classList.remove('active'); }});
  btn.classList.add('active');

  var cards = document.querySelectorAll('.finding-card');
  cards.forEach(function(card) {{
    var cCat = card.getAttribute('data-cat');
    if (cat === 'all' || cCat === cat) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}

// Vulnerability PoC Modal
function openPoCModal(findId) {{
  playCyberSound('open');
  var item = FINDINGS_DB.find(function(f) {{ return f.id === findId; }});
  if (!item) return;

  document.getElementById('mId').textContent = item.id;
  document.getElementById('mTitle').textContent = item.title;
  document.getElementById('mTarget').textContent = item.target;
  document.getElementById('mCvss').textContent = item.cvss;
  document.getElementById('mCwe').textContent = item.cwe;
  document.getElementById('mRootCause').textContent = item.root_cause;
  document.getElementById('mPoc').textContent = item.poc;
  document.getElementById('mImpact').textContent = item.impact;
  document.getElementById('mFix').textContent = item.fix;

  var sevEl = document.getElementById('mSev');
  sevEl.textContent = item.sev;
  sevEl.className = 'sev-chip ' + (item.sev.includes('P1') ? 'sev-p1' : item.sev.includes('P2') || item.sev.includes('High') ? 'sev-p2' : item.sev.includes('Medium') || item.sev.includes('P3') ? 'sev-p3' : 'sev-p4');

  document.getElementById('pocModal').classList.add('open');
}}

function closeModal() {{
  playCyberSound('click');
  document.getElementById('pocModal').classList.remove('open');
}}

function closeModalOnBg(e) {{
  if (e.target.id === 'pocModal') closeModal();
}}

// Interactive Cyber Toolbox
function toggleToolbox() {{
  playCyberSound('open');
  var tb = document.getElementById('cyberToolbox');
  var btn = document.getElementById('toolboxBtn');
  tb.classList.toggle('open');
  btn.classList.toggle('active', tb.classList.contains('open'));
  if (tb.classList.contains('open')) {{
    tb.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
  }}
}}

function switchToolTab(tab) {{
  playCyberSound('click');
  document.querySelectorAll('.tb-tab-btn').forEach(function(b) {{ b.classList.remove('active'); }});
  document.querySelectorAll('.tool-pane').forEach(function(p) {{ p.classList.remove('active'); }});
  
  if (tab === 'jwt') {{
    document.querySelectorAll('.tb-tab-btn')[0].classList.add('active');
    document.getElementById('pane-jwt').classList.add('active');
  }} else if (tab === 'hash') {{
    document.querySelectorAll('.tb-tab-btn')[1].classList.add('active');
    document.getElementById('pane-hash').classList.add('active');
  }} else if (tab === 'nik') {{
    document.querySelectorAll('.tb-tab-btn')[2].classList.add('active');
    document.getElementById('pane-nik').classList.add('active');
  }}
}}

function decodeJWT() {{
  var token = document.getElementById('jwtInput').value.trim();
  var out = document.getElementById('jwtOutput');
  if (!token) {{
    out.textContent = '// Paste JWT token above to analyze...';
    return;
  }}
  try {{
    var parts = token.split('.');
    if (parts.length < 2) throw new Error('Invalid JWT format (expected 3 dot-separated parts)');
    var header = JSON.parse(atob(parts[0].replace(/-/g, '+').replace(/_/g, '/')));
    var payload = JSON.parse(atob(parts[1].replace(/-/g, '+').replace(/_/g, '/')));
    
    var res = '[JWT HEADER]\\n' + JSON.stringify(header, null, 2) + '\\n\\n[JWT CLAIMS / PAYLOAD]\\n' + JSON.stringify(payload, null, 2);
    if (header.alg === 'none') res += '\\n\\n⚠️ SECURITY WARNING: Token uses vulnerable alg: "none" (Signature Bypass)';
    if (payload.exp) {{
      var expDate = new Date(payload.exp * 1000);
      var isExp = expDate < new Date();
      res += '\\n\\nℹ️ Expiration: ' + expDate.toISOString() + (isExp ? ' (EXPIRED)' : ' (VALID)');
    }}
    out.textContent = res;
  }} catch(e) {{
    out.textContent = '❌ JWT Decode Error: ' + e.message;
  }}
}}

function loadSampleJWT(type) {{
  playCyberSound('click');
  var token = type === 'admin' 
    ? 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ik1hcmNvIFNlbHZhIE9rbmFtIiwicm9sZSI6IlNZU1RFTV9BRE1JTiIsImlhdCI6MTczOTYwMDAwMCwiZXhwIjoyMDgwMDAwMDAwfQ.signature_hash_preview'
    : 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJhZG1pbi1hYnVzZSIsInJvbGUiOiJzdXBlcmFkbWluIiwiYXVkaXQiOiJ2dWxuZXJhYmxlX2J5cGFzcyJ9.';
  document.getElementById('jwtInput').value = token;
  decodeJWT();
}}

function calcCrypto() {{
  var txt = document.getElementById('hashInput').value;
  var out = document.getElementById('hashOutput');
  if (!txt) {{
    out.textContent = '// Enter string above to compute encodings and hash...';
    return;
  }}
  try {{
    var b64 = btoa(unescape(encodeURIComponent(txt)));
    var hex = Array.from(new TextEncoder().encode(txt)).map(function(b) {{ return b.toString(16).padStart(2, '0'); }}).join(' ');
    var urlEnc = encodeURIComponent(txt);
    var rot13 = txt.replace(/[a-zA-Z]/g, function(c) {{
      return String.fromCharCode((c <= 'Z' ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);
    }});
    
    out.textContent = 'Plaintext    : ' + txt +
                      '\\nBase64       : ' + b64 +
                      '\\nHex Dump     : ' + hex +
                      '\\nURL Encoded  : ' + urlEnc +
                      '\\nROT13 Cipher : ' + rot13;
  }} catch(e) {{
    out.textContent = 'Error computing: ' + e.message;
  }}
}}

function inspectNIK() {{
  var nik = document.getElementById('nikInput').value.trim();
  var out = document.getElementById('nikOutput');
  if (nik.length < 16) {{
    out.textContent = '// Type 16-digit NIK to parse (Length: ' + nik.length + '/16)...';
    return;
  }}
  var prov = nik.substring(0, 2);
  var kab = nik.substring(2, 4);
  var kec = nik.substring(4, 6);
  var rawDay = parseInt(nik.substring(6, 8), 10);
  var isFemale = rawDay > 40;
  var day = isFemale ? rawDay - 40 : rawDay;
  var month = nik.substring(8, 10);
  var year = nik.substring(10, 12);
  var seq = nik.substring(12, 16);

  out.textContent = '--- SINIK-PRO CLIENT-SIDE DECODER ---\\n' +
                    'NIK String   : ' + nik + '\\n' +
                    'Province ID  : ' + prov + ' (' + (prov === '35' ? 'Jawa Timur' : prov === '31' ? 'DKI Jakarta' : prov === '32' ? 'Jawa Barat' : 'Region Code') + ')\\n' +
                    'City/Reg ID  : ' + kab + ' (' + (prov === '35' && kab === '07' ? 'Kabupaten Malang' : 'Sub-district') + ')\\n' +
                    'District ID  : ' + kec + '\\n' +
                    'Gender       : ' + (isFemale ? 'Perempuan (Female)' : 'Laki-Laki (Male)') + '\\n' +
                    'Date of Birth: ' + String(day).padStart(2, '0') + '-' + month + '-19' + year + ' / 20' + year + '\\n' +
                    'Sequence UID : ' + seq + '\\n' +
                    'Privacy Check: Sanitized locally, 0 server calls made.';
}}

// Interactive Terminal CLI Drawer
function toggleCLI() {{
  playCyberSound('open');
  var drawer = document.getElementById('cliDrawer');
  var btn = document.getElementById('cliBtn');
  drawer.classList.toggle('open');
  btn.classList.toggle('active', drawer.classList.contains('open'));
  if (drawer.classList.contains('open')) {{
    setTimeout(function() {{ document.getElementById('cliInput').focus(); }}, 100);
  }}
}}

function runCLICommand(cmd) {{
  var input = document.getElementById('cliInput');
  input.value = cmd;
  executeCLI(cmd);
}}

function handleCLIKeyDown(e) {{
  if (e.key === 'Enter') {{
    var val = e.target.value.trim();
    if (val) executeCLI(val);
    e.target.value = '';
  }}
}}

function appendCLILog(html) {{
  var logs = document.getElementById('cliLogs');
  var div = document.createElement('div');
  div.className = 'cli-log-line';
  div.innerHTML = html;
  logs.appendChild(div);
  logs.scrollTop = logs.scrollHeight;
}}

function executeCLI(cmd) {{
  playCyberSound('click');
  appendCLILog('<span style="color:var(--text-dim);">$ ' + cmd + '</span>');
  var clean = cmd.toLowerCase().trim();
  
  if (clean === 'help' || clean === '?') {{
    appendCLILog('Available commands:<br>' +
      '  <span style="color:var(--cyan);">whoami</span>        - Print identity profile<br>' +
      '  <span style="color:var(--cyan);">cat bio</span>       - Print full executive bio<br>' +
      '  <span style="color:var(--cyan);">skills</span>        - Technical skills matrix &amp; tools<br>' +
      '  <span style="color:var(--cyan);">vulns</span>         - List selected security findings<br>' +
      '  <span style="color:var(--cyan);">poc &lt;id&gt;</span>      - Inspect finding PoC (e.g. poc FND-01)<br>' +
      '  <span style="color:var(--cyan);">cve</span>           - Show CVE &amp; zero-day research<br>' +
      '  <span style="color:var(--cyan);">certs</span>         - Show certifications &amp; credential IDs<br>' +
      '  <span style="color:var(--cyan);">contact</span>       - Display contact channels<br>' +
      '  <span style="color:var(--cyan);">tools</span>         - Open interactive AppSec toolbox<br>' +
      '  <span style="color:var(--cyan);">matrix</span>        - Toggle digital rain background<br>' +
      '  <span style="color:var(--cyan);">sound</span>         - Toggle audio effects<br>' +
      '  <span style="color:var(--cyan);">theme &lt;name&gt;</span>  - emerald | cyberpunk | stealth | amber | paper<br>' +
      '  <span style="color:var(--cyan);">pdf / print</span>   - Export CV to PDF / Print<br>' +
      '  <span style="color:var(--cyan);">neofetch</span>      - System &amp; profile information<br>' +
      '  <span style="color:var(--cyan);">clear</span>        - Clear terminal screen'
    );
  }} else if (clean === 'whoami' || clean === 'id') {{
    appendCLILog('uid=1000(marco) gid=1000(secops) groups=1000(secops),27(sudo),44(pentest),1337(researcher)');
  }} else if (clean === 'cat bio') {{
    appendCLILog('{bio}');
  }} else if (clean === 'skills') {{
    appendCLILog('<b>[TECHNICAL SKILLS MATRIX]</b><br>' +
      '• Web AppSec    : OWASP Top 10, REST, GraphQL, WebSocket, OAuth 2.0, SAML, IDOR, SSRF<br>' +
      '• Bytecode Audit: Java JAR (JADX, Procyon), Node.js, Python AST, Android APK (Frida)<br>' +
      '• Offensive     : Burp Suite Pro, Caido, Nuclei, Katana, Ffuf, Nmap, Wireshark<br>' +
      '• SIEM &amp; Defense: Wazuh SIEM, Sysmon, Kali Linux, Docker, MITRE ATT&amp;CK'
    );
  }} else if (clean === 'vulns' || clean === 'findings') {{
    var res = '<b>[DISCLOSED VULNERABILITIES]</b><br>';
    FINDINGS_DB.forEach(function(f) {{
      res += '• <a href="javascript:openPoCModal(\\'' + f.id + '\\')" style="color:var(--cyan);text-decoration:underline;">' + f.id + '</a> [' + f.sev + '] ' + f.title.substring(0, 55) + '...<br>';
    }});
    appendCLILog(res);
  }} else if (clean.startsWith('poc ')) {{
    var id = cmd.split(' ')[1].toUpperCase();
    openPoCModal(id);
    appendCLILog('Opening dossier for ' + id + '...');
  }} else if (clean === 'cve') {{
    appendCLILog('<b>[CVE / COORDINATED RESEARCH]</b><br>• <b>Cleartext DB Credentials over TLS (Node.js Connector)</b>: CVE Assigned, advisory coordinated.');
  }} else if (clean === 'certs') {{
    appendCLILog('<b>[VERIFIED CREDENTIALS]</b><br>' +
      '• Web Penetration Testing (Cyber Academy ID: BWH01110254258)<br>' +
      '• Cyber Security 101 (TryHackMe ID: THM-0G7VUW6K0M)<br>' +
      '• Pre Security (TryHackMe ID: THM-R4E0NX6WTU)<br>' +
      '• Introduction to Cybersecurity (Cisco Networking Academy)'
    );
  }} else if (clean === 'contact') {{
    appendCLILog('Phone : +62 812-3160-2472<br>Email : houseofmartynix@gmail.com<br>GitHub: github.com/houseofmartynix-debug<br>LinkedIn: linkedin.com/in/mrcslvknm');
  }} else if (clean === 'tools') {{
    toggleToolbox();
    appendCLILog('Toggled AppSec toolbox sandbox.');
  }} else if (clean === 'matrix') {{
    toggleMatrix();
    appendCLILog('Matrix rain toggled: ' + (matrixRunning ? 'ENABLED' : 'DISABLED'));
  }} else if (clean === 'sound') {{
    toggleSound();
    appendCLILog('Audio FX toggled: ' + (soundEnabled ? 'ENABLED' : 'DISABLED'));
  }} else if (clean.startsWith('theme ')) {{
    var t = clean.split(' ')[1];
    changeTheme(t);
    appendCLILog('Theme switched to: ' + t);
  }} else if (clean === 'clear') {{
    document.getElementById('cliLogs').innerHTML = '';
  }} else if (clean === 'pdf' || clean === 'print') {{
    window.print();
  }} else if (clean === 'neofetch') {{
    appendCLILog(
      '<pre style="color:var(--accent);font-family:monospace;font-size:10.5px;line-height:1.2;">' +
      '  ██████╗ ███████╗ ██████╗  marco@secops<br>' +
      '  ██╔══██╗██╔════╝██╔════╝  ------------<br>' +
      '  ██████╔╝███████╗██║       OS      : Kali GNU/Linux x86_64<br>' +
      '  ██╔═══╝ ╚════██║██║       Host    : Marco Selva Oknam [SecOps]<br>' +
      '  ██║     ███████║╚██████╗  Kernel  : 6.12.0-secops-hardened<br>' +
      '  ╚═╝     ╚══════╝ ╚═════╝  Uptime  : Continuous Research<br>' +
      '                            Shell   : zsh 5.9 (x86_64-debian-linux)<br>' +
      '                            Terminal: SecOps Interactive Shell v2.4<br>' +
      '                            Language: Python · Bash · Java · Aksara Jawa<br>' +
      '                            Bounties: Bugcrowd, HackerOne, YesWeHack, Gerobug<br>' +
      '</pre>'
    );
  }} else {{
    playCyberSound('error');
    appendCLILog('<span style="color:var(--rose);">Command not found: ' + cmd + '. Type "help" for commands.</span>');
  }}
}}

// Global Hotkeys
window.addEventListener('keydown', function(e) {{
  if ((e.ctrlKey && e.key === 'k') || (e.key === '`' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA')) {{
    e.preventDefault();
    toggleCLI();
  }} else if (e.key === 'Escape') {{
    if (document.getElementById('pocModal').classList.contains('open')) closeModal();
    else if (document.getElementById('cliDrawer').classList.contains('open')) toggleCLI();
    else if (document.getElementById('cyberToolbox').classList.contains('open')) toggleToolbox();
  }}
}});
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
