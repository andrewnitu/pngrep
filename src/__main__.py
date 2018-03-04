import click


# The main entry point
@click.group()
@click.option('--no-cached', '-n')
def main():
    return


# Reindex subcommand, this fully rewrites the index
@main.command()
@click.option('--clear', '-c')
def reindex():
    return


if __name__ == "__main__":
    main()
