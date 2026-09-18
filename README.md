# Marco Selva Oknam — Elite Interactive SecOps Curriculum Vitae

[![Live CV - English](https://img.shields.io/badge/Live_CV-English_Edition-00dc82?style=for-the-badge&logo=githubpages&logoColor=white)](https://houseofmartynix-debug.github.io/curriculum-vitae/en/)
[![Live CV - Aksara Jawa](https://img.shields.io/badge/Live_CV-ꦄꦏ꧀ꦱꦫ_ꦗꦮ-38bdf8?style=for-the-badge)](https://houseofmartynix-debug.github.io/curriculum-vitae/)
[![Transliteration Round-Trip](https://img.shields.io/badge/Transliteration-100%25_Round--Trip_Verified-a855f7?style=for-the-badge)](./jawa.py)
[![Security Standard](https://img.shields.io/badge/Standard-Bugcrowd_VRT_·_CVSS_v3.1-f59e0b?style=for-the-badge)](./build.py)
[![Responsible Disclosure](https://img.shields.io/badge/Compliance-ISO%2FIEC_29147-f43f5e?style=for-the-badge)](./build.py)

Interactive, dual-language Curriculum Vitae and security research dossier of **Marco Selva Oknam** (Application Security Researcher, Penetration Tester & Bug Bounty Hunter). Engineered with an automated bidirectional Latin $\leftrightarrow$ Aksara Jawa (Javanese script) transliteration compiler and an elite developer terminal / SecOps workstation aesthetic.

---

## 🌐 Live Demonstrations

* 🇬🇧 **English Edition:** [https://houseofmartynix-debug.github.io/curriculum-vitae/en/](https://houseofmartynix-debug.github.io/curriculum-vitae/en/)
* ꦗꦮ **Aksara Jawa Edition (Canonical):** [https://houseofmartynix-debug.github.io/curriculum-vitae/](https://houseofmartynix-debug.github.io/curriculum-vitae/)

---

## 🛡️ Professional Security Profile & High-Value Impact

* **Core Domains:** Web Application & API Penetration Testing (REST / GraphQL / WebSockets), Source Code Review (Java JAR / Bytecode Decompilation / AST Analysis), Multi-Tenant Access Control & Authorization (IDOR / BOLA), Privilege Escalation, SSRF Chains, Cloud/IAM Security, Responsible Disclosure.
* **Bug Bounty Platforms:** Bugcrowd, HackerOne, YesWeHack, Gerobug.
* **Enterprise Risk Mitigation:**
  * **50+ High-Impact Security Findings** triaged and verified across public and private bug bounty programmes.
  * **$5,900 in bounty rewards** and **223 Bugcrowd researcher points**, all solo — **$2,600 / 80 points** on the Accxia Marketplace Bug Bounty engagement (headlined by a **P1 Critical** authorisation bypass), **$300 / 10 points** from Gliffy, and a further **$3,000** across additional Bugcrowd and Atlassian Data Center programmes withheld here under coordinated-disclosure terms.
  * **17 paid bounties across nine separate programmes**, spanning P1 Critical through accepted-informational.
  * **100% Coordinated Responsible Disclosure Compliance** under ISO/IEC 29147 standards.
  * Multi-million dollar critical infrastructure data breaches and tenant workspace takeovers prevented.

### Selected Findings & Hall of Fame Highlights

| ID | Title & Vulnerability Mechanism | Target Classification | Severity / Score | Status & Proof |
| :--- | :--- | :--- | :--- | :--- |
| `FND-01` | **Admin-Page Resolver Routes Execute for Any Licensed User (No Authorisation Check)** | Intelligent User Manager (IUM) for Jira Cloud 6.4.0 · Atlassian Forge | **P1 Critical** (Bugcrowd VRT `broken_access_control > privilege_escalation`) | Accepted & rewarded **$1,500 / 40 points** — Accxia Marketplace Bug Bounty. |
| `FND-02` | **Non-Administrator Grants a Paid JSM Agent Seat to Any Account via `startAssignment`** | Intelligent User Manager (IUM) for Jira Cloud 6.4.0 · Atlassian Forge | **P3** (Bugcrowd VRT `broken_access_control > privilege_escalation`) | Accepted, **resolved** & rewarded **$300 / 10 points** — Accxia Marketplace Bug Bounty. |
| `FND-03` | **Cross-Project Assignee Read & Unassign — `ium-assignee-field` Resolvers Ignore the Caller's Permissions** | Intelligent User Manager (IUM) for Jira Cloud 6.4.0 · Atlassian Forge | **P3** (Bugcrowd VRT `broken_access_control > idor`) | Accepted & rewarded **$300 / 10 points** — Accxia Marketplace Bug Bounty. |
| `FND-04` | **Blind SSRF in the Diagram Import Route Reaches Internal Network Services** | Gliffy for Confluence | **P3** (CVSS 5.8) | Accepted & rewarded **$300 / 10 points** — Gliffy. |
| `FND-05` | **Arbitrary File Write & Overwrite in `JIRA_HOME` by Any Logged-In Non-Administrator** | Intelligent User Manager (IUM) for Jira Data Center 5.4.5 | **P4** (Bugcrowd VRT `broken_access_control > privilege_escalation`) | Accepted, **resolved** & rewarded **$100 / 5 points** — Accxia Marketplace Bug Bounty. |
| `FND-06` | **Missing Space-Permission Check Exposes Restricted Spaces' Q&A Statistics** | Questions for Confluence · Atlassian-Built Apps | **P5 Accepted** (CVSS 4.3 as reported) | Accepted as informational — Atlassian-Built Apps. |
| `FND-07` | **Authenticated SSRF — Fetch-Action URL Filter Performs No DNS Resolution** | Balsamiq Wireframes for Jira (Data Center) | **P5 Accepted** (CVSS 3.1 as reported) | Accepted as informational — Balsamiq for Atlassian Products. |
| `FND-08` | **Unauthenticated Test Route Returns Any Account's Live Email OTP, Clearing the Email Gate** | Global digital-asset exchange *(anonymized — in triage)* | **P5 Accepted** (CVSS 8.1 as reported) | Accepted as informational by the programme. |
| `FND-09` | **Privilege Escalation to SYSTEM_ADMIN via Predictable Impersonation Token** | Enterprise Jira/Confluence DC Plugin | **P2 High** (CVSS 8.8) | Validated live in production; Full workspace takeover prevented. |
| `FND-10` | **Cleartext Database Credentials over Encrypted TLS Connections** | Popular Node.js Database Connector | **CVE Pending** (CVSS 5.9) | Triaged & CVE assigned; Coordinated disclosure in progress. |
| `FND-11` | **User Enumeration & PII Disclosure via National ID (NIK) Endpoint** | Diskominfo Kota Tangerang Selatan (Gerobug) | **Medium** (CVSS 5.3) | Official Certificate of Appreciation `7C0B38027836`. |
| `FND-12` | **Source Code & Sensitive Configuration Disclosure** | Diskominfo Kota Tangerang Selatan (Gerobug) | **Medium** (CVSS 5.3) | Official Certificate of Appreciation `7C0B36916030`. |
| `FND-13` | **Model Context Protocol (MCP) Unauthenticated Localhost HTTP Exposure** | Desktop AI & Dev Application | **CVSS 7.3 High** | Reported via official programme; Patched cross-origin tool execution. |
| `FND-14` | **Approval Flow Bypass & Open OAuth 2.0 Dynamic Client Registration** | Production Enterprise SaaS Platforms | **High** (CVSS 8.1) | Under active triage; Intercepted authorization code leakage. |
| `FND-15` | **Application-Wide Configuration Store Readable & Writable by Any Licensed User (Back-End Never Checks Privilege)** | Atlassian Cloud backup application (Forge) — vendor withheld | **P2** (Bugcrowd VRT `broken_access_control > privilege_escalation`) | Under active triage; break/restore chain proves server-side consumption. |
| `FND-16` | **Back-End Derives Identity From a Client-Supplied `accountId` — Ordinary User Acts as Administrator** | Atlassian Cloud backup application (Forge) — vendor withheld | **P1** (Bugcrowd VRT `broken_authentication_and_session_management > authentication_bypass`) | Under active triage; signed platform context ignored in favour of a request-body field. |
| `FND-17` | **Stored Credentials Replayed to a Redirect Target Host** | Atlassian Data Center plugin — vendor withheld | **P3** (Bugcrowd VRT `sensitive_data_exposure > disclosure_of_secrets`) | Accepted, **resolved** & rewarded **$300 / 10 points**; vendor shipped the fix in two releases. |
| `FND-18` | **Global Realtime Channel Leaks Another User's Session Context** | Atlassian Cloud application (Forge) | **P4** (Bugcrowd VRT `broken_access_control`) | Accepted & rewarded **$100 / 5 points** — Accxia Marketplace Bug Bounty. |

---

## ⚡ Elite Interactive Terminal & SecOps Features

1. **Integrated Interactive Terminal Shell (`>_ CLI`):**
   * Accessible via button or `Ctrl+K` / `` ` `` keyboard hotkeys.
   * Fully functioning interactive command shell supporting `help`, `whoami`, `cat bio`, `skills`, `vulns`, `poc <id>`, `cve`, `certs`, `contact`, `tools`, `matrix`, `sound`, `theme <name>`, `neofetch`, `pdf`, and `clear`.
2. **Interactive Vulnerability Dossier & PoC Explorer Modal:**
   * Click any finding card to open a technical modal featuring CVSS v3.1 vector strings, CWE classifications, root cause bytecode analysis, sanitized reproduction PoCs, business impact assessments, and remediation roadmaps.
3. **Interactive AppSec Toolbox Sandbox:**
   * **JWT Inspector:** Real-time client-side Base64Url header/payload decoder, signature analysis, and insecure `alg: "none"` detector.
   * **Crypto & Encoding Swiss-Knife:** Instant Plaintext $\leftrightarrow$ Base64, Hex dump, URL-encoding, ROT13, and SHA-256 computation.
   * **Sinik-Pro NIK Inspector:** Privacy-preserving client-side Indonesian National ID decoder (Province, Regency, Gender, DOB) without server calls.
4. **Theme Engine with Instant Persistence:**
   * ⚡ **Cyber Emerald:** Kali Linux / hacker workstation default.
   * 🌌 **Neon Synth:** Cyberpunk cyan & magenta palette.
   * 🛡️ **Midnight Stealth:** Titanium slate & graphite dark mode.
   * 🖥️ **Amber CRT:** Vintage 1980s phosphor terminal.
   * 🩸 **Crimson Root:** Red-team crimson & rose palette.
   * 📄 **Clean Paper:** Recruiter high-contrast executive mode.
   * Every surface — shell chrome, telemetry bars, input wells, modal chrome — is driven by theme tokens, so the light theme is genuinely light rather than a dark chassis with light text.

8. **Layered Ambient Backdrop:**
   * A masked-portrait backdrop sits at the base of the stack, veiled by a radial/linear falloff so the centre — where the shell and its body text live — stays dark enough to read against. The shell is deliberately light-blurred glass (`blur(7px)`), because a heavy blur smears the figure into mush and it stops reading through.
   * Above it: a drifting multi-stop aurora field, a slow diagonal light beam, an engineering grid, CRT scanlines, a vignette and a film-grain pass — all theme-aware, all pure CSS, and all disabled under `prefers-reduced-motion` and in print.
   * The `paper` theme drops the backdrop to `0.13` opacity and print hides it entirely, so recruiter mode stays clean.
   * Reading-progress rail and `IntersectionObserver` scroll reveals (applied from JS, so a no-JS visitor still sees the full document).
5. **Opt-In Soundtrack (`▶ Music`):**
   * Two-track playlist in `music/`, wired through a single `<audio>` element with `preload="none"` — the ~10 MB is never fetched unless a visitor actually presses play.
   * Never autoplays. Click to play, click again to pause, shift-click to skip; `music` and `next` also work from the terminal shell. Tracks advance automatically on `ended`.
   * The button flips state optimistically and shows a `buffering…` chip, then confirms on the `playing` event — otherwise a 5 MB track leaves the control looking dead on a slow connection.
   * Animated equaliser bars in the button while playing; the now-playing chip is hidden in print.

6. **Programmatic Web Audio API Sound FX:**
   * Pure synthesized cyber mechanical keyclicks and modal chimes (zero external audio asset latency), toggleable via header switch.
6. **Canvas Matrix Digital Rain:**
   * 60 FPS hardware-accelerated digital rain animation toggleable on demand.
7. **Recruiter-Grade Print / PDF Engine (`@media print`):**
   * One-click **Print / Export PDF** action producing a crisp, monochrome ATS-friendly executive resume with all interactive UI controls automatically hidden.

---

## ⚙️ Architecture & Build System

The entire dual-language suite is compiled from a single unified Python compiler:

```
curriculum-vitae/
├── build.py            # Single-source compiler (renders index.html & en/index.html)
├── jawa.py             # Bidirectional Javanese transliterator + round-trip verifier
├── style.css           # Comprehensive SecOps design system & print stylesheet
├── tools-portrait.py   # Portrait pipeline: crop → depth-of-field → tone → Base64
├── tools-backdrop.py   # Backdrop pipeline: resize → blur → tone → Base64
├── photo.b64           # Embedded Base64 profile portrait (zero network lag)
├── photo-formal.b64    # Alternate formal studio headshot (swap in over photo.b64)
├── bg.b64              # Embedded Base64 page backdrop portrait
├── music/              # Soundtrack, served as files (never inlined)
├── index.html          # Rendered Aksara Jawa canonical edition (root)
└── en/
    └── index.html      # Rendered English edition (/en/)
```

### 100% Round-Trip Transliteration Guarantee
`jawa.py` enforces a bidirectional mathematical invariant:
$$\text{Latin} \xrightarrow{\text{forward}} \text{Aksara Jawa} \xrightarrow{\text{reverse}} \text{Latin}' \implies \text{Latin} \equiv \text{Latin}'$$
Every single Javanese string is verified upon build; builds will fail if a single character cannot be deterministically decoded back to its source Latin representation.

---

## 🚀 Local Development & Build

1. **Prerequisites:** Python 3.8+
2. **Compile Pages:**
   ```bash
   python3 build.py
   ```
   *Expected Output:*
   ```text
   strings transliterated : 198
   exact round-trip       : 198
   needs eyeball          : 0

   index.html    : ~230 KB
   en/index.html : ~234 KB
   ```
3. **Preview Locally:**
   ```bash
   python3 -m http.server 8080
   ```
   Open `http://localhost:8080` in your web browser.

---

## 📬 Contact & Channels

* **Email:** [houseofmartynix@gmail.com](mailto:houseofmartynix@gmail.com)
* **LinkedIn:** [linkedin.com/in/mrcslvknm](https://linkedin.com/in/mrcslvknm)
* **GitHub:** [github.com/houseofmartynix-debug](https://github.com/houseofmartynix-debug)
* **Phone / WhatsApp:** +62 812-3160-2472
* **PGP Fingerprint:** `Available upon verified request`

---

*© Marco Selva Oknam. All vulnerability research adheres strictly to ISO/IEC 29147 Coordinated Vulnerability Disclosure guidelines.*
