import hashlib
import os
import sys

import click


def get_appdata_dir():
    if sys.platform == 'win32':
        appdata_dir = os.path.join(os.getenv("APPDATA"), "port-gen")
    else:
        appdata_dir = os.path.join(os.path.expanduser("~"), ".config", "port-gen")

    if not os.path.exists(appdata_dir):
        os.makedirs(appdata_dir)

    return appdata_dir


def generate_salt():
    return hashlib.sha256(os.urandom(32)).hexdigest()


def generate_port(service_name: str, salt: str):
    src = service_name + ":" + salt
    dst = hashlib.sha256(src.encode()).hexdigest()

    dst_int = int(dst[:8], 16)
    port = (dst_int % 16384) + 49152

    return port


@click.command()
@click.option("--salt", default=None, help="Specify salt manually.")
@click.option("--no-store", is_flag=True, default=False, help="Don't store salt to disk.")
@click.argument("service_name")
def main(salt: str, service_name: str, no_store: bool):
    """Generate a random port within the Ephemeral Ports range"""
    appdata_dir = get_appdata_dir()
    salt_path = os.path.join(appdata_dir, "salt.txt")

    if salt is None:
        if os.path.exists(salt_path):
            with open(salt_path, "r") as f:
                salt = f.read().strip()
        else:
            salt = generate_salt()

            if not no_store:
                with open(salt_path, "w") as f:
                    f.write(salt)

    port = generate_port(service_name, salt)

    print("Service Name:", service_name)
    print("Salt:", salt)
    print("Port:", port)


if __name__ == '__main__':
    main()
