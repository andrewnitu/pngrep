import click
import db.db as db
import files.lookup as lookup
from click_ext.default_group import DefaultGroup


# The main entry point
@click.group(cls=DefaultGroup, default='search', default_if_no_args=True)
def cli():
    pass


@cli.command()
@click.option('--no-cached', '-n', is_flag=True)
@click.argument('search-string', required=True)
@click.argument('files', nargs=-1, type=click.Path('rb'))
def search(no_cached, search_string, files):
    print("SEARCHING")
    db.init()

    if no_cached:
        print(search_string)
        print(files)
        print(lookup.lookup_no_cache(search_string, files))
    else:
        print("grep using cache")
        print(files)


@cli.command()
def reindex():
    print("REINDEXING")
    db.clear_all_file_text()
    return


if __name__ == "__main__":
    cli()
