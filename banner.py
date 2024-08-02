import pyfiglet
from rich import print
def print_banner():
    title = pyfiglet.figlet_format('L I V E',font="epic")
    sub_title = pyfiglet.figlet_format('WALLPAPER',font="doom")
    print(f'[red]{title}[/red]')
    print(f'[red]{sub_title}[/red]')
    print("[yellow]by: am1ral188[/yellow]")
    print("[yellow]    on github[/yellow]\n")
