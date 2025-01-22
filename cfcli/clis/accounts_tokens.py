import click

import cfcli
from cfcli.lazy_group import LazyGroup
from cfcli import cfclient

@click.group(name="tokens", cls=LazyGroup,
  lazy_subcommands={
    "list": "cfcli.clis.accounts_tokens.list_tokens",
    "create": "cfcli.clis.accounts_tokens.create_token",
    "delete": "cfcli.clis.accounts_tokens.delete_token",
    "update": "cfcli.clis.accounts_tokens.update_token",
    'verify': "cfcli.clis.accounts_tokens.verify_token",
    "show": "cfcli.clis.accounts_tokens.show_token",
    'permission_groups': "cfcli.clis.accounts_tokens.permission_groups",
    'value': "cfcli.clis.accounts_tokens.value"
  },
  help="Manage Cloudflare Account tokens")
def accounts_tokens():
  pass

@click.group(name="permission_groups", cls=LazyGroup,
  lazy_subcommands={
    "list": "cfcli.clis.accounts_tokens.list_permission_groups.list",
})
def permission_groups():
  pass

@click.group(name="value", cls=LazyGroup,
  lazy_subcommands={
    "list": "cfcli.clis.accounts_tokens.value.roll", 
})
def value():
  pass

@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
@click.option('--direction', '-d', required=False, help='Direction', type=click.Choice(choices=['asc', 'desc']))  
@click.option('--page', '-p', required=False, help='Page')
@click.option('--per-page', '-pp', required=False, help='Per Page')
def list_tokens(account_id, direction, page, per_page):
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.tokens.list(account_id=account_id, direction=direction, page=page, per_page=per_page)
  click.echo(response)

@click.command()
@click.option('--account-id', '-i', required=False, help='Account ID')
def create_token():
  raise cfcli.NotImplementedError("Not implemented yet")
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.tokens.create()
  click.echo(response)
  
@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
@click.option('--token-id', '-t', required=True, help='Token ID')
def delete_token(account_id, token_id):
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.tokens.delete(account_id=account_id, token_id=token_id)
  click.echo(response)
  
@click.command()
def update_token():
  raise cfcli.NotImplementedError("Not implemented yet")
  # cf = cfclient.CFCLIClient()
  # response = cf.cf.accounts.tokens.update()
  # click.echo(response)
  
@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
def verify_token():
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.tokens.verify()
  click.echo(response)
  
@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
def list_pgs(account_id):
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.tokens.permission_groups.list(account_id=account_id)
  click.echo(response)
  
@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
@click.option('--token-id', '-t', required=True, help='Token ID')
def reroll(account_id, token_id):
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.tokens.value.update(account_id=account_id, token_id=token_id, body={})
  click.echo(response)