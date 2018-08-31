
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

### Production environment

Inspired on this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) to understand and set it up as in our server.

- Set up (see above)
- Create server.sh from template: `cp server.sh.template server.sh`
- `chmod +x server.sh`
- Edit variables to match your environment and add extra if required (see environment variables available above)
- Create restart.sh from template: `cp restart.sh.template restart.sh`
- `chmod +x restart.sh`
- Edit variables to match your environment and add extra if required (see environment variables available above)
- Run `restart.sh`. This will update the database, dependecies and static files.
- Set up Systemd (read next section)

#### Set up gunicorn service in Systemd
Needs: Systemd.

- Edit this file `/etc/systemd/system/api.service`
- Add this content
```
[Unit]
Description=api daemon
After=network.target

[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/project_folder
ExecStart=/home/user/project_folder/server.sh >>/home/user/project_folder/out.log 2>>/home/user/project_folder/error.log

[Install]
WantedBy=multi-user.target

```

- Replace `user` for your linux user.
- Replace `project_folder` by the name of the folder where the project is located
- Create and enable service: `sudo systemctl start api && sudo systemctl enable api`

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
