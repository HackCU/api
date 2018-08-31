
<br>
<p align="center">
  <img alt="HackCU IV" src="https://github.com/HackCU/splash-page/blob/master/img/hackcu_black.png" width="200"/>
</p>
<br>

API for internal resources

## Setup

Needs: Python 3.X, virtualenv

- `git clone https://github.com/hackcu/api && cd api`
- `virtualenv env --python=python3`
- `source ./env/bin/activate`
- `pip install -r requirements.txt`

## Server

### Local environment

- Set up (see above)
- `python manage.py runserver`
- Sit back, relax and enjoy. That's it!


## Enviroment variables

- **DEBUG**(optional): Set to `false` to disable debug mode on production.
- **SECRET**(optional): Sets web application secret. You can generate a random secret with python running: `os.urandom(24)`
- **DATABASE_URL**(optional): URL to connect to the database. If not sets, defaults to django default SQLite database. See schema for different databases [here](https://github.com/kennethreitz/dj-database-url#url-schema).
- **DOMAIN**(optional): Domain where app will be running. Default: None
- **SLACK**(optional): Slack token to invite hackers automatically on confirmation. You can obtain it [here](https://api.slack.com/custom-integrations/legacy-tokens)


# Want to Contribute?
Read these [guidelines](.github/CONTRIBUTING.md) carefully.

By making a contribution, in any form (including, but not limited to, Issues and Pull Requests), you agree to abide by the [Code of Conduct](.github/CODE_OF_CONDUCT.md). Report any incidents to report@gerard.space and appropriate action will be taken against the offender after investigation.

# License

MIT © HackCU
