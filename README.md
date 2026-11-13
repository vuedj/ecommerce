# DRF Ecommerce

```sh
uv init --bare --python 3.15
uv add -r <(iconv -f UTF-16 -t UTF-8 requirements.txt | sed 's/==/>=/g')
uv lock --upgrade
uv sync --locked

# uv run manage.py makemigrations store
# uv run manage.py migrate
# uv run manage.py createsuperuser --username admin --email admin@admin.com
uv run manage.py runserver
```
