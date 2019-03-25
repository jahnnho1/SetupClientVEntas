import click


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.passcontext
def create(ctx, name, company, email, position):
    """CReate a new Client"""
    pass


@clients.command()
@click.passcontext
def listx(ctx):
    """List all CLients"""
    pass


@clients.command()
@click.passcontext
def update(ctx, client_uid):
    """Update A client"""
    pass


@clients.command()
@click.passcontext
def delete(ctx, client_uid):
    """DEletes a client"""
    pass


all = clients