import subprocess
import sys
import socket
import re
import os
from rich.console import Console
from rich import print as rprint
from rich.panel import Panel
from colorama import Fore, Style
from InquirerPy import inquirer
from concurrent.futures import ThreadPoolExecutor
import shutil

# List of required packages and tools
required_packages = ['colorama', 'requests', 'rich', 'InquirerPy']
required_tools = [
    'nmap', 'nuclei', 'katana', 'subfinder', 'httpx',
    'ghauri', 'dalfox', 'naabu', 'tinja', 'sqlmap',
    'admin-panel-finder', 'paramspider'
]

console = Console()

def install_package(package):
    """Install the given package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_packages():
    """Check if required packages are installed and install them if not."""
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            console.print(Fore.YELLOW + f"Module '{package}' not found. Installing now..." + Style.RESET_ALL)
            install_package(package)

def is_tool_installed(tool):
    """Check if a tool is installed by checking the specific paths."""
    specific_paths = {
        "ghauri": "./ghauri",
        "naabu": "./naabu"
    }
    if tool in specific_paths and os.path.isfile(specific_paths[tool]):
        return True
    return False

def move_to_usr_bin(tool_name):
    """Move the Go tools from the go/bin directory to /usr/bin."""
    go_bin_path = os.path.expanduser("~/go/bin")  # Default Go bin directory
    usr_bin_path = "/usr/bin"
    
    tool_path = os.path.join(go_bin_path, tool_name)
    if os.path.isfile(tool_path):
        try:
            shutil.move(tool_path, os.path.join(usr_bin_path, tool_name))
            console.print(Fore.GREEN + f"Moved {tool_name} to {usr_bin_path}" + Style.RESET_ALL)
        except Exception as e:
            console.print(Fore.RED + f"Failed to move {tool_name}: {e}" + Style.RESET_ALL)

def install_tool(tool):
    """Install the specified tool if not already installed and move it to /usr/bin."""
    if is_tool_installed(tool):
        return

    console.print(Fore.YELLOW + f"Installing {tool}..." + Style.RESET_ALL)
    try:
        if tool == "ghauri":
            subprocess.check_call(["git", "clone", "https://github.com/r0oth3x49/ghauri.git", "ghauri"])
            os.chdir("ghauri")
            subprocess.check_call(["go", "build"])
            os.chdir("..")
            subprocess.check_call(["chmod", "+x", "./ghauri"])  # Grant execute permissions
            move_to_usr_bin("ghauri")
        elif tool == "naabu":
            subprocess.check_call(["go", "install", "-v", "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"])
            move_to_usr_bin("naabu")
        elif tool == "dalfox":
            subprocess.check_call(["go", "install", "github.com/hahwul/dalfox/v2@latest"])
            move_to_usr_bin("dalfox")
        elif tool == "httpx":
            subprocess.check_call(["go", "install", "-v", "github.com/projectdiscovery/httpx/cmd/httpx@latest"])
            move_to_usr_bin("httpx")
        console.print(Fore.GREEN + f"{tool} installed and moved successfully!" + Style.RESET_ALL)
    except Exception as e:
        console.print(Fore.RED + f"Failed to install {tool}: {e}" + Style.RESET_ALL)

def check_and_install_tools():
    """Check if required tools are installed and install them if not."""
    for tool in required_tools:
        install_tool(tool)

def clear_console():
    """Clears the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    """Display the banner with credits."""
    console.print(Panel("[bold yellow]Auto Vulnerability[/bold yellow]", title="Welcome, Code Made By Justdan", border_style="cyan"))
    console.print("=" * 40, style="cyan")
    console.print(f"[bold green]Code Made by Justdan[/bold green]")
    console.print(f"[bold blue]Credits to tools used:[/bold blue]")
    console.print(f"{Fore.CYAN}Nuclei: https://github.com/projectdiscovery/nuclei")
    console.print(f"{Fore.CYAN}Katana: https://github.com/projectdiscovery/katana")
    console.print(f"{Fore.CYAN}Subfinder: https://github.com/projectdiscovery/subfinder")
    console.print(f"{Fore.CYAN}HTTPX: https://github.com/projectdiscovery/httpx")
    console.print(f"{Fore.CYAN}Naabu: https://github.com/projectdiscovery/naabu")
    console.print(f"{Fore.CYAN}GhauRi: https://github.com/r0oth3x49/ghauri")
    console.print(f"{Fore.CYAN}Dalfox: https://github.com/hahwul/dalfox")
    console.print(f"{Fore.CYAN}SQLMap: https://github.com/sqlmapproject/sqlmap")
    console.print(f"{Fore.CYAN}Admin Panel Finder: https://github.com/s0md3v/Arjun")
    console.print(f"{Fore.CYAN}ParamSpider: https://github.com/devanshbatham/ParamSpider")
    console.print("=" * 40, style="cyan")

def validate_url(url):
    pattern = r"^(https?://)"
    return bool(re.match(pattern, url))

def get_ip_from_url(url):
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        ip_address = socket.gethostbyname(domain)
        console.print(f"Resolved IP for {domain}: {Fore.GREEN}{ip_address}{Style.RESET_ALL}")
        return ip_address
    except socket.gaierror:
        console.print(Fore.RED + "Error resolving domain to IP address." + Style.RESET_ALL)
        return None

def run_command(command, output_file):
    """Run a command in a subprocess and redirect its output to a file."""
    with open(output_file, "w") as f:
        try:
            process = subprocess.Popen(command, stdout=f, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            if stdout:
                console.print(f"stdout: {stdout}")
            if stderr:
                console.print(Fore.RED + f"stderr: {stderr}" + Style.RESET_ALL)

            if process.returncode != 0:
                console.print(Fore.RED + f"Error running command: {stderr}" + Style.RESET_ALL)
            else:
                console.print(f"[+] Output saved to {output_file}")
                console.print(f"[bold green]Tool run successfully![/bold green] [italic]Credit to tool authors above.[/italic]")
        except FileNotFoundError:
            console.print(Fore.RED + f"{command[0]} not found. Ensure it is installed on your system." + Style.RESET_ALL)

def select_tools():
    """Allow the user to select which tools they want to run, with GhauRi, Dalfox, SQLMap, Admin Page Finder, and Paramspider as 'coming soon'."""
    tools = [
        "Nuclei", "Katana", "Subfinder", "HTTPX", 
        "Naabu",
    ]
    
    coming_soon_tools = [
        "GhauRi (Coming Soon)", "Dalfox (Coming Soon)",
        "SQLMap (Coming Soon)", "Admin Page Finder (Coming Soon)", 
        "Paramspider (Coming Soon)"
    ]
    
    selected_tools = inquirer.checkbox(
        message="Select tools to run:",
        choices=tools + coming_soon_tools
    ).execute()
    return selected_tools

def run_ghauri(url):
    """Display 'Coming Soon' message for GhauRi."""
    console.print(Fore.YELLOW + "[*] GhauRi is coming soon but this script already installs it for you, so you can still use the tool separately. Stay tuned!" + Style.RESET_ALL)

def run_dalfox(url):
    """Display 'Coming Soon' message for Dalfox.""" 
    console.print(Fore.YELLOW + "[*] Dalfox is coming soon but this script already installs it for you, so you can still use the tool separately. Stay tuned!" + Style.RESET_ALL)

def run_sqlmap(url):
    """Display 'Coming Soon' message for SQLMap."""
    console.print(Fore.YELLOW + "[*] SQLMap is coming soon but will be integrated shortly. Stay tuned!" + Style.RESET_ALL)

def run_admin_page_finder(url):
    """Display 'Coming Soon' message for Admin Page Finder."""
    console.print(Fore.YELLOW + "[*] Admin Page Finder is coming soon. Stay tuned!" + Style.RESET_ALL)

def run_paramspider(url):
    """Display 'Coming Soon' message for Paramspider."""
    console.print(Fore.YELLOW + "[*] Paramspider is coming soon. Stay tuned!" + Style.RESET_ALL)

def run_nuclei_scan(url):
    """Run Nuclei scan.""" 
    command = ["nuclei", "-u", url, "-t", "nuclei-templates"]
    run_command(command, "nuclei_output.txt")

def run_katana_crawl(url):
    """Run Katana crawl."""
    command = ["katana", "-u", url, "-d", "2"]
    run_command(command, "katana_output.txt")

def run_subfinder(url):
    """Run Subfinder."""
    command = ["subfinder", "-d", url]
    run_command(command, "subfinder_output.txt")

def run_httpx(url):
    """Run HTTPX."""
    command = ["httpx", "-u", url]
    run_command(command, "httpx_output.txt")

def run_naabu_scan(url):
    """Run Naabu scan."""
    command = ["naabu", "-h", url]
    run_command(command, "naabu_output.txt")

def main():
    clear_console()
    banner()

    check_and_install_packages()
    check_and_install_tools()

    selected_tools = select_tools()

    url = inquirer.text(message="Enter the target URL:").execute()

    if not validate_url(url):
        console.print(Fore.RED + "Invalid URL format! Please enter a valid URL starting with http:// or https://" + Style.RESET_ALL)
        return

    for tool in selected_tools:
        if tool == "Nuclei":
            run_nuclei_scan(url)
        elif tool == "Katana":
            run_katana_crawl(url)
        elif tool == "Subfinder":
            run_subfinder(url)
        elif tool == "HTTPX":
            run_httpx(url)
        elif tool == "Naabu":
            run_naabu_scan(url)
        elif tool == "GhauRi (Coming Soon)":
            run_ghauri(url)
        elif tool == "Dalfox (Coming Soon)":
            run_dalfox(url)
        elif tool == "SQLMap (Coming Soon)":
            run_sqlmap(url)
        elif tool == "Admin Page Finder (Coming Soon)":
            run_admin_page_finder(url)
        elif tool == "Paramspider (Coming Soon)":
            run_paramspider(url)

if __name__ == "__main__":
    main()
