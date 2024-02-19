import subprocess


def run_cmd(cmd: str) -> str:
    proc = subprocess.run(
        cmd.split(),
        capture_output=True,
        text=True,
    )

    return f"{proc.stdout} {proc.stderr}"


def list_pkgs() -> None:
    """List installed packages."""
    print(run_cmd("pkcon get-packages --filter installed --plain"))


def install_pkg(name: str) -> None:
    """Install a package."""
    print(run_cmd(f"pkcon install {name} -y --plain"))


def remove_pkg(name: str) -> None:
    """Remove a package."""
    print(run_cmd(f"pkcon remove {name} -y --plain"))
