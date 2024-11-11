# Auto Vulnerability Scanning Tool

![Banner](https://img.shields.io/badge/AutoVuln-Scanning%20Tool-blue)

An automated vulnerability scanning tool designed for security testing of web applications, created by **Justdan**. This tool simplifies the process of running various security tools and gathers results in an organized way, helping developers and security professionals identify potential weaknesses in their applications.

## Features

- **Automated Installation**: Installs required Python packages and security tools if missing.
- **Modular Scanning**: Allows users to select specific tools for a customized scanning process.
- **Popular Security Tools Integrated**:
  - [Nuclei](https://github.com/projectdiscovery/nuclei) - Template-based vulnerability scanning.
  - [Katana](https://github.com/projectdiscovery/katana) - Web crawling for endpoint discovery.
  - [Subfinder](https://github.com/projectdiscovery/subfinder) - Subdomain discovery.
  - [HTTPX](https://github.com/projectdiscovery/httpx) - Probes HTTP responses.
  - [Naabu](https://github.com/projectdiscovery/naabu) - Port scanning.

## Installation

1. **Clone the Repository**:
   ```bash
   https://github.com/JustDanz/Autovuln.git
   cd Autovuln
   ```

2. **Install Python Dependencies**:
   This tool requires `Python 3.8+`. Run the following to install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Tool Installation**:
   Some tools require `Go` to be installed on your system. Install Go tools with:
   ```bash
   go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
   go install -v github.com/projectdiscovery/katana@latest
   # ... other tools as needed
   ```

   Run the script, and it will automatically check and install missing tools.

## Usage

1. **Run the Script**:
   ```python
   python3 vuln.py
   ```
   if it say pemission denied
  ```
sudo python3 vuln.py
```

3. **Select Tools**:
   The script presents an interactive menu where you can select which tools to run.

4. **Enter Target URL**:
   Input the target URL to initiate scanning.

5. **Review Output**:
   Results are saved in `.txt` files for each tool (e.g., `nuclei_output.txt`).

## Tool Descriptions

- **Nuclei**: Executes vulnerability templates to detect known vulnerabilities.
- **Katana**: Crawls URLs to find endpoints and assets for further analysis.
- **Subfinder**: Discovers subdomains, useful for identifying additional assets.
- **HTTPX**: Checks for live HTTP assets, useful for asset inventory.
- **Naabu**: Conducts port scanning to discover open ports.

## Contributing

Feel free to open issues or submit pull requests to improve this tool. Contributions are welcome to enhance functionality, add more tools, or optimize the code.

## Credits

This tool leverages several open-source security tools. Credits to the respective tool creators:
- [Nuclei](https://github.com/projectdiscovery/nuclei)
- [Katana](https://github.com/projectdiscovery/katana)
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [HTTPX](https://github.com/projectdiscovery/httpx)
- [Naabu](https://github.com/projectdiscovery/naabu)
- [GhauRi](https://github.com/r0oth3x49/ghauri)
- [Dalfox](https://github.com/hahwul/dalfox)
- [SQLMap](https://github.com/sqlmapproject/sqlmap)
- [Admin Panel Finder](https://github.com/s0md3v/Arjun)
- [ParamSpider](https://github.com/devanshbatham/ParamSpider)

---

Developed by Justdan
```

**Note:** Replace `"https://github.com/JustDanz/Autovuln"` with the actual GitHub repository URL once available.

```
Here’s how to add "Coming Soon" tools to your README file:

---

## Coming Soon Tools

In future updates, additional tools will be integrated into the Auto Vulnerability Scanning Tool. Here’s a preview of these planned additions:

### 1. **SQLMap** (Coming Soon)
   - **Description**: SQLMap automates the detection and exploitation of SQL injection vulnerabilities. It helps testers identify database flaws and supports various DBMS platforms (e.g., MySQL, PostgreSQL, Oracle).
   - **Planned Integration**: SQLMap will be used to scan target URLs for SQL injection vulnerabilities and report findings in a detailed output file.

   - **Repository**: [SQLMap on GitHub](https://github.com/sqlmapproject/sqlmap)

### 2. **Admin Panel Finder** (Coming Soon)
   - **Description**: This tool searches for hidden or hard-to-find admin panels on websites, which can be crucial for security testing by identifying potential attack surfaces.
   - **Planned Integration**: Admin Panel Finder will allow users to uncover admin pages, which could expose sensitive controls if left unprotected.

   - **Repository**: [Admin Panel Finder on GitHub](https://github.com/s0md3v/Arjun)

### 3. **ParamSpider** (Coming Soon)
   - **Description**: ParamSpider is designed to find URL parameters across a target website, useful for expanding test coverage and enhancing injection or fuzzing operations.
   - **Planned Integration**: With ParamSpider, this tool will help automate parameter discovery for comprehensive testing.

   - **Repository**: [ParamSpider on GitHub](https://github.com/devanshbatham/ParamSpider)

### 4. **GhauRi** (Coming Soon)
   - **Description**: GhauRi is an advanced SQL injection scanner that focuses on identifying complex SQL vulnerabilities. It's particularly useful for deeper SQL testing when automated tools may miss complex injection points.
   - **Planned Integration**: GhauRi will be integrated as an alternative to SQLMap for enhanced SQL injection detection and testing on a separate module.

   - **Repository**: [GhauRi on GitHub](https://github.com/r0oth3x49/ghauri)

### 5. **Dalfox** (Coming Soon)
   - **Description**: Dalfox is a powerful XSS scanning tool that detects and tests for cross-site scripting vulnerabilities in web applications. It's known for its speed and thoroughness in detecting common XSS attack vectors.
   - **Planned Integration**: Once integrated, Dalfox will allow users to scan for XSS vulnerabilities efficiently and generate reports on potential exploits.

   - **Repository**: [Dalfox on GitHub](https://github.com/hahwul/dalfox)

---

Stay tuned for updates as these tools are added, offering expanded functionality for more comprehensive security testing. Contributions are welcome!
