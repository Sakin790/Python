import subprocess

def run_wsl():
    try:
        command = ["wsl", "-d", "Ubuntu-24.04"]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: 'wsl' command not found. Make sure WSL is installed and available in your PATH.")

if __name__ == "__main__":
    run_wsl()