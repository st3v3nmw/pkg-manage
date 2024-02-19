import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="cli")
    subparsers = parser.add_subparsers(required=True, dest="subparser")
    subparsers.add_parser("list")
    parser_install = subparsers.add_parser("install")
    parser_install.add_argument("name", type=str)
    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument("name", type=str)
    args = parser.parse_args()

    if args.mode == "cli":
        from pkg_manage.cli import install_pkg, list_pkgs, remove_pkg
    else:
        from pkg_manage.lib import install_pkg, list_pkgs, remove_pkg

    if args.subparser == "list":
        print(list_pkgs()[0])
    elif args.subparser == "install":
        print(install_pkg(args.name)[0])
    else:
        print(remove_pkg(args.name)[0])
