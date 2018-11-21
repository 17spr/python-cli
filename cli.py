# cli.py
import click

@click.command()
def helloWorld():
    print("✨ Hello World! ✨\nThis is your point of entry into Jesse's command line interface application.\nStay tuned for more exciting functions!")


if __name__=="__main__":
    helloWorld()
