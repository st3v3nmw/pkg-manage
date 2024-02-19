from typing import Any, Callable

import gi

gi.require_version("PackageKitGlib", "1.0")

from gi.repository import PackageKitGlib


def progress(progress: Any, *_: Any) -> None:
    """Print out the progress."""
    status = progress.get_status()
    if status == PackageKitGlib.StatusEnum.UNKNOWN:
        return

    percentage = progress.get_percentage()
    percent_text = "" if percentage < 0 else f" {percentage}%"

    print(f"{status.to_localised_text(status)}{percent_text}")


progress_no_op = lambda *_: None


def explode_if_err(func: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        err = result.get_error_code()
        if err:
            raise RuntimeError(err.get_details())
        return result

    return wrapper


def get_package_id(pk_client: Any, name: str) -> str:
    """Get the package id from its name."""
    result = explode_if_err(pk_client.resolve)(
        filters=PackageKitGlib.FilterEnum.NONE,
        packages=[name],
        cancellable=None,
        progress_callback=progress_no_op,
        progress_user_data=None,
    )
    package_ids = result.get_package_array()
    # return the first match
    return package_ids[0].get_id()


def list_pkgs() -> None:
    """List installed packages."""
    pk_client = PackageKitGlib.Client()

    results = explode_if_err(pk_client.get_packages)(
        # TODO: Fix this filter, NOT WORKING
        filters=PackageKitGlib.FilterEnum.INSTALLED,
        cancellable=None,
        progress_callback=progress,
        progress_user_data=None,
    )

    pkgs = results.get_package_sack().get_array()
    for pkg in pkgs:
        name = pkg.get_name()
        version = pkg.get_version()
        arch = pkg.get_arch()
        print(f"{name}-{version}.{arch} ({pkg.get_data()})")


def install_pkg(name: str) -> None:
    """Install a package."""
    pk_client = PackageKitGlib.Client()
    package_id = get_package_id(pk_client, name)

    explode_if_err(pk_client.install_packages)(
        transaction_flags=True,
        package_ids=[package_id],
        cancellable=None,
        progress_callback=progress,
        progress_user_data=None,
    )


def remove_pkg(name: str) -> None:
    """Remove a package."""
    pk_client = PackageKitGlib.Client()
    package_id = get_package_id(pk_client, name)

    explode_if_err(pk_client.remove_packages)(
        transaction_flags=True,
        package_ids=[package_id],
        allow_deps=False,
        autoremove=True,
        cancellable=None,
        progress_callback=progress,
        progress_user_data=None,
    )
