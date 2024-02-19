import subprocess


def run_cmd(cmd: str) -> tuple[str, bool]:
    proc = subprocess.run(
        cmd.split(),
        capture_output=True,
        text=True,
    )

    return (
        f"{proc.stdout} {proc.stderr}",
        proc.returncode == 0,
    )


def list_pkgs() -> tuple[str, bool]:
    """List installed packages."""
    return run_cmd("pkcon get-packages --filter installed --plain")


def install_pkg(name: str) -> tuple[str, bool]:
    """Install a package."""
    return run_cmd(f"pkcon install {name} -y --plain")


def remove_pkg(name: str) -> tuple[str, bool]:
    """Remove a package."""
    return run_cmd(f"pkcon remove {name} -y --plain")
