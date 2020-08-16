# notice how rich isn't installed by default, we have to manually install it
from rich import print as rprint
def print_dummy(x):
	rprint("[red]{}[/red]".format(x))