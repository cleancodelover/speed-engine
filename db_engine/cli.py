
import click

from db_engine.engine import DatabaseEngine


@click.group()
def cli():
    """Speed Engine CLI."""
    pass

@cli.command()
@click.option("--models-path", default="models", help="Path to the models folder.")
def migrate(models_path):
    """Run database migrations"""
    from config import DATABASE_CONFIG
    db = DatabaseEngine(DATABASE_CONFIG["adapter"], **DATABASE_CONFIG)
    db.create_tables_from_folder(models_path)
    click.echo("Migrations completed successfully!")

if __name__ == "__main__":
    cli()