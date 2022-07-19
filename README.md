# DC Sonar User Layer

It's the part of [dc-sonar](https://github.com/ST1LLY/dc-sonar) project

## Deploy for development

Clone [dc-sonar-user-layer](https://github.com/ST1LLY/dc-sonar-user-layer)

```bash
git clone https://github.com/ST1LLY/dc-sonar-user-layer.git
```

### Windows

Open Powershell, cd to created dc-sonar-user-layer folder

Create Python virtual environment

```powershell
&"C:\Program Files\Python310\python.exe" -m venv venv
```

Active venv

```
.\venv\Scripts\Activate.ps1
```

Install pip packages

```
pip install -r .\requirements.txt
```

Open dc-sonar-user-layer folder in IDE - PyCharm for example

### Ubuntu

Go to folder where directory with source is located

Deactivate previous venv if uses

```shell
deactivate
```

Create venv

```shell
python3.10 -m venv venv-user-layer
```

Activate venv

```shell
source venv-user-layer/bin/activate
```

Install dependencies

```shell
pip install -r dc-sonar-user-layer/requirements.txt
```

Deactivate venv

```
deactivate
```



### PyCharm settings



See common settings in [common PyCharm settings](https://github.com/ST1LLY/dc-sonar#pycharm-settings)



#### Pylint

Arguments: `--max-line-length=119 --disable=too-few-public-methods,import-error,import-outside-toplevel,broad-except,wrong-import-position,duplicate-code --load-plugins pylint_django --django-settings-module=dc_sonar_web.settings`

### Config

Copy `dc_sonar_web/sensitive_settings_blank.py` to `dc_sonar_web/sensitive_settings.py`

Fulfil params

`S_DATABASES` contains value for [DATABASES](https://docs.djangoproject.com/en/4.0/ref/settings/#databases) in `dc_sonar_web/settings.py` used for DB connection

`S_SECRET_KEY` contains value for [SECRET_KEY](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#secret-key) in `dc_sonar_web/settings.py` 

`S_SIGNING_KEY` contains value for Simple JWT [SIGNING_KEY](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html#signing-key)  in `dc_sonar_web/settings.py`

`S_AES_256_KEY` contains value for `AES_256_KEY` in `dc_sonar_web/settings.py` using for decryption and  encryption saved passed of acc have been bruted

Example:

```python
S_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_app_db',
        'USER': 'dc_sonar_user_layer',
        'PASSWORD': 'f}jod5?y3R>,RsLqmAt-e5G*sujRL1+?1Wip!YX:e86n>]suA3n)V!:YqeE~*LVN',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

S_SECRET_KEY = 'q5W04kBYo5-e1N]yyJJ+MD_L>~+ERn:M9JPAVbMNiC>9ZMWzkd>+9qtsvAPdc?)F'
S_SIGNING_KEY = 'r?r:f2dP,N0k!HW?_TJ?z_d}Fu0Z?n]Qrv_6U}qtvyT%jm8C5?]s#@E2W6oKc3uc'
S_AES_256_KEY = '8^xjD=0v3Lk_1QNZW+1sb6u)oDQw0nhcPvu^gh:jHCyR*}jn+_T#Ak%*>3p_yvZe'
```

