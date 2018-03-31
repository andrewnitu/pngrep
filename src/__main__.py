import click
import db.db as db


# The main entry point
@click.group(invoke_without_command=True)
@click.option('--no-cached', '-n', is_flag=True)
@click.pass_context
def cli(ctx, no_cached):
    db.init()
    if ctx.invoked_subcommand is not None:
        return

    if no_cached:
        print("grep with nocached")
    else:
        print("grep using cache")
    return


@cli.command()
def reindex():
    db.clear_all_file_text()
    return


if __name__ == "__main__":
    cli()
