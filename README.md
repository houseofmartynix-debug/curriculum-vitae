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
  * **100% Coordinated Responsible Disclosure Compliance** under ISO/IEC 29147 standards.
  * Multi-million dollar critical infrastructure data breaches and tenant workspace takeovers prevented.

### Selected Findings & Hall of Fame Highlights

| ID | Title & Vulnerability Mechanism | Target Classification | Severity / Score | Status & Proof |
| :--- | :--- | :--- | :--- | :--- |
| `FND-01` | **Privilege Escalation to SYSTEM_ADMIN via Predictable Impersonation Token** | Enterprise Jira/Confluence DC Plugin | **P2 High** (CVSS 8.8) | Validated live in production; Full workspace takeover prevented. |
| `FND-02` | **Cleartext Database Credentials over Encrypted TLS Connections** | Popular Node.js Database Connector | **CVE Pending** (CVSS 5.9) | Triaged & CVE assigned; Coordinated disclosure in progress. |
| `FND-03` | **User Enumeration & PII Disclosure via National ID (NIK) Endpoint** | Diskominfo Kota Tangerang Selatan (Gerobug) | **Medium** (CVSS 5.3) | Official Certificate of Appreciation `7C0B38027836`. |
| `FND-04` | **Source Code & Sensitive Configuration Disclosure** | Diskominfo Kota Tangerang Selatan (Gerobug) | **Medium** (CVSS 5.3) | Official Certificate of Appreciation `7C0B36916030`. |
| `FND-05` | **SSRF & Blind SSRF via Webhook & Attachment Handlers** | Multiple Enterprise Atlassian DC Plugins | **P2 / P3 High** (CVSS 7.7) | Triaged & accepted; Blocked cloud metadata (169.254.169.254) extraction. |
| `FND-06` | **Model Context Protocol (MCP) Unauthenticated Localhost HTTP Exposure** | Desktop AI & Dev Application | **CVSS 7.3 High** | Reported via official programme; Patched cross-origin tool execution. |
| `FND-07` | **Approval Flow Bypass & Open OAuth 2.0 Dynamic Client Registration** | Production Enterprise SaaS Platforms | **High** (CVSS 8.1) | Under active triage; Intercepted authorization code leakage. |

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
   * 📄 **Clean Paper:** Recruiter high-contrast executive mode.
5. **Programmatic Web Audio API Sound FX:**
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
├── build.py          # Single-source compiler (renders index.html & en/index.html)
├── jawa.py           # Bidirectional Javanese transliterator + round-trip verifier
├── style.css         # Comprehensive SecOps design system & print stylesheet
├── photo.b64         # Embedded Base64 profile portrait (zero network lag)
├── index.html        # Rendered Aksara Jawa canonical edition (root)
└── en/
    └── index.html    # Rendered English edition (/en/)
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
   strings transliterated : 145
   exact round-trip       : 145
   needs eyeball          : 0

   index.html    : ~122 KB
   en/index.html : ~124 KB
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
