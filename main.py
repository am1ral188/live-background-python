import ctypes
import os
import time

import rich
from PIL import Image
import argparse
import banner
from rich.console import Console
closing = False


def main():
    tmp_dir = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\live-wallpaper'
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    filePath = os.path.join(tmp_dir, "background.png")

    banner.print_banner()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    # Run command
    run_parser = subparsers.add_parser("run", help="Run {input gif file}")
    run_parser.add_argument("input_gif", help="input gif file", default="theme.gif")
    run_parser.set_defaults(func=run)

    args = parser.parse_args()

    if args.command == "run":
        print("running  Ctrl+C to kill it")
        print("attention it may slow down your pc\n")
        run(args.input_gif, filePath)


def run(image_path, output_path):
    im = Image.open(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, output_path, 3)
    while True:
        for i in range(im.n_frames):
            try:
                im.seek(i)
                im.save(output_path)
                os.system("RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters 1, True")
                time.sleep(0.1)
            except KeyboardInterrupt:
                im.close()
                rich.print("\n[yellow]GoodBye[/yellow]")
                exit(1)


if __name__ == '__main__':
    try:
        console=Console()
        con = "app is running"
        with console.status(
                  con, spinner="dots"
          ):
            main()
    except KeyboardInterrupt:
        rich.print("[yellow]GoodBye[/yellow]")
        exit(1)
