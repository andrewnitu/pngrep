import click
import sys
import db.db as db
import files.lookup as lookup
import format.format as formatting
import colorama
from click_ext.default_group import DefaultGroup


# The main entry point
@click.group(cls=DefaultGroup, default='search', default_if_no_args=True)
def cli():
    pass


# Search and update
@cli.command()
@click.option('--no-cached', '-n', is_flag=True)
@click.option('--parallel', '-p', is_flag=True)
@click.argument('search-string', required=True)
@click.argument('files', nargs=-1, type=click.Path('rb'))
def search(no_cached, parallel, search_string, files):
    db.init()

    if no_cached:
        sys.stdout.write(formatting.format_results(lookup.lookup_no_cache(files, parallel), search_string))
    else:
        sys.stdout.write(formatting.format_results(lookup.lookup_with_cache(files, parallel), search_string))


# Clear the cache
@cli.command()
def clear():
    db.clear_all_file_text()
    return


if __name__ == "__main__":
    colorama.init()
    cli()
