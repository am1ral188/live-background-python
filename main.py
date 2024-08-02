import os
import time
from PIL import Image
import argparse
import banner
def main():
    banner.print_banner()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    # Run command
    run_parser = subparsers.add_parser("run", help="Run {input gif file} {output png set it as your background}")
    run_parser.add_argument("input_gif", help="input gif file")
    run_parser.add_argument("output", help="output png set it as your background")
    run_parser.set_defaults(func=run)

    args = parser.parse_args()

    if args.command == "run":
        print("running  Ctrl+C to kill it")
        print("attention it may slow down your pc")
        run(args.input_gif,args.output)
def run(image_path,output_path):
    im=Image.open(image_path)
    while True:
         for i in range(im.n_frames):
            im.seek(i)
            im.save(output_path)
            os.system("RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters 1, True")
            time.sleep(0.1)


if __name__ == '__main__':
     main()