
import subprocess
import sys
import time
from pathlib import Path

# Always run from the project directory
PROJECT_DIR = Path(__file__).resolve().parent

processes = []


def start_process(name, script, *args):
    """Start a script using the current Python interpreter."""
    command = [sys.executable, str(PROJECT_DIR / script), *args]

    print(f"Starting {name}...", flush=True)

    process = subprocess.Popen(
        command,
        cwd=PROJECT_DIR,
    )
    processes.append((name, process))

    # Give the script a moment to start
    time.sleep(1)

    if process.poll() is not None:
        print(
            f"Warning: {name} exited with code "
            f"{process.returncode}",
            flush=True,
        )
    else:
        print(f"{name} launched (PID {process.pid})", flush=True)

    return process


try:
    print(f"Python interpreter: {sys.executable}", flush=True)
    print(f"Project directory: {PROJECT_DIR}", flush=True)

    # 1. Start the Thrift client
    start_process("Thrift client", "thrift_client.py")

    # 2. Start the Thrift server
    start_process("Thrift server", "thrift_server.py")

    # 3. Start the Django HTTPS server
    django = start_process(
        "Django HTTPS server",
        "manage.py",
        "runsslserver",
        "--certificate",
        "webapps2025.crt",
        "--key",
        "webapps2025.key",
    )

    # Keep this launcher alive while Django runs
    django.wait()

except KeyboardInterrupt:
    print("\nStopping application...", flush=True)

finally:
    # Stop the other processes when the launcher exits
    for name, process in reversed(processes):
        if process.poll() is None:
            print(f"Stopping {name}...", flush=True)
            process.terminate()

    # Allow processes to shut down gracefully
    for name, process in reversed(processes):
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print(f"Force-stopping {name}...", flush=True)
            process.kill()
            process.wait()

    print("Application stopped.", flush=True)
