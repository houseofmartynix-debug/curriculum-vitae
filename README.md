# Marco Selva Oknam — Interactive Curriculum Vitae

[![Live CV - English](https://img.shields.io/badge/Live_CV-English-00e599?style=for-the-badge&logo=githubpages&logoColor=white)](https://houseofmartynix-debug.github.io/curriculum-vitae/en/)
[![Live CV - Aksara Jawa](https://img.shields.io/badge/Live_CV-ꦄꦏ꧀ꦱꦫ_ꦗꦮ-38bdf8?style=for-the-badge)](https://houseofmartynix-debug.github.io/curriculum-vitae/)
[![Transliteration Round-Trip](https://img.shields.io/badge/Transliteration-100%25_Verified-a855f7?style=for-the-badge)](./jawa.py)

Interactive, dual-language Curriculum Vitae of **Marco Selva Oknam** (Application Security Researcher, Penetration Tester & Bug Bounty Hunter), engineered with a single-source compiler and an automated bidirectional Latin $\leftrightarrow$ Aksara Jawa (Javanese script) transliterator.

---

## 🌐 Live Pages

* 🇬🇧 **English Edition:** [https://houseofmartynix-debug.github.io/curriculum-vitae/en/](https://houseofmartynix-debug.github.io/curriculum-vitae/en/)
* ꦗꦮ **Aksara Jawa Edition (Canonical):** [https://houseofmartynix-debug.github.io/curriculum-vitae/](https://houseofmartynix-debug.github.io/curriculum-vitae/)

---

## 🛡️ Professional Profile Overview

* **Specialization:** Web Application & API Penetration Testing, Source Code Review (JAR Decompilation / White-box), Authorization & Access Control Logic Flaws (IDOR / BOLA / Tenant Scoping), Privilege Escalation, SSRF, Responsible Disclosure.
* **Platforms:** Bugcrowd, HackerOne, YesWeHack, Gerobug.
* **Public Acknowledgements & Hall of Fame:**
  * **Diskominfo Kota Tangerang Selatan (Gerobug):** User Enumeration via NIK (Certificate of Appreciation `7C0B38027836`) & Source Code Disclosure (Certificate of Appreciation `7C0B36916030`).
  * **Enterprise Jira/Confluence DC Plugin:** Live-validated Privilege Escalation to `SYSTEM_ADMIN` via predictable impersonation token (P2).
  * **Node.js Ecosystem:** Cleartext database credentials across TLS connections (CVE Assigned).
  * **Atlassian DC Ecosystem:** SSRF & Blind SSRF across multiple commercial enterprise plugins (Triaged).
  * **Model Context Protocol (MCP) Service:** Unauthenticated remote HTTP exposure in desktop application (CVSS 7.3).

---

## ⚙️ Architecture & Build System

The repository generates both the English and Aksara Jawa editions from a unified single source file:

```
curriculum-vitae/
├── build.py          # Single-source compiler (renders index.html & en/index.html)
├── jawa.py           # Bidirectional Javanese transliterator + round-trip verifier
├── style.css         # Shared modern cybersecurity styling + print stylesheet
├── photo.b64         # Embedded Base64 profile portrait (zero external asset latency)
├── index.html        # Rendered Aksara Jawa edition (root)
└── en/
    └── index.html    # Rendered English edition (/en/)
```

### Features
1. **Bidirectional Transliteration Verification (`jawa.py`):**
   * Enforces a zero-error round-trip contract (`jawa.check(latin) == (aksara, back_to_latin, True)`).
   * Verifies that every single Javanese word can be accurately converted back to its exact Latin representation.
2. **Executive Cybersecurity Aesthetic (`style.css`):**
   * Slate obsidian palette (`#090d12`) with emerald green (`#00e599`) and electric blue (`#38bdf8`) accents.
   * Interactive one-click **Copy to Clipboard** for contact channels (Phone, Email) with instant toast feedback.
   * Direct links to open-source security tools and research repositories.
3. **Print & PDF Optimization (`@media print`):**
   * One-click **Print / Export PDF** action (`window.print()`).
   * Clean executive monochrome layout, crisp typography, and automatic page-break preservation for physical copies or formal PDF submissions.

---

## 🚀 Local Development & Build

1. **Prerequisites:** Python 3.8+
2. **Compile Pages:**
   ```bash
   python3 build.py
   ```
   *Expected Output:*
   ```text
   strings transliterated : 101
   exact round-trip       : 101
   needs eyeball          : 0

   index.html    : ~69 KB
   en/index.html : ~70 KB
   ```
3. **Preview Locally:**
   ```bash
   python3 -m http.server 8080
   ```
   Open `http://localhost:8080` in your browser.

---

## 📬 Contact & Links

* **Email:** [houseofmartynix@gmail.com](mailto:houseofmartynix@gmail.com)
* **LinkedIn:** [linkedin.com/in/mrcslvknm](https://linkedin.com/in/mrcslvknm)
* **GitHub:** [github.com/houseofmartynix-debug](https://github.com/houseofmartynix-debug)
