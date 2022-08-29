# PYTHON BUILTINS
import os
from typing import NamedTuple

# EXTERNAL MODULES
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

__all__ = (
    "Cloudinary",
    "Django",
    "GithubAuth",
    "HOST",
    "Jazzmin",
    "SocialAuth",
    "ToolsConstant",
    "Recaptcha",
)


class HOST(NamedTuple):
    host_uri=os.getenv("SITE_HOST_URI")


class GithubAuth(NamedTuple):
    auth_client_id =os.getenv("GITHUB_AUTH_CLIENT_ID")
    auth_client_secret =os.getenv("GITHUB_AUTH_CLIENT_SECRET")


class ToolsConstant(NamedTuple):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    alphabets = 'abcdefghijklmnopqurstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    specialcharacters = ''' !"#$%&'()*+,-./:‸⁁⎀;‱©†¤©‡(ɔ)<=>?@[\]^_`{|}~⟨ ⟩⁂±¶®℗™∴'''
    numbers='0123456789'


class Cloudinary(NamedTuple):
    cloud_name = os.getenv('CLOUD_NAME')
    api_key = os.getenv('API_KEY')
    api_secret =   os.getenv('API_SECRET')


class Django(NamedTuple):
    SITE_ID = int(os.getenv("SITE_ID"))
    ALLOWED_HOSTS = [os.getenv("SITE_HOST_DOMAIN"), 'localhost', '127.0.0.1']
    CSRF_TRUSTED_ORIGINS = [os.getenv("SITE_HOST_URI"), "http://localhost:3000"]
    INSTALLED_APPS = [
    # JAZZMIN
    'jazzmin',

     # DJANGO IN BUILTS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # EXTERNAL
    'anymail',
    'cloudinary',
    'compressor',
    'crispy_forms',
    'mathfilters',
    'simpleinliner',
    'captcha',


    # DJANGO APP CREATED WITH `django-admin startapp`
    'home.apps.HomeConfig',
    'api.apps.ApiConfig',
    'member.apps.MemberConfig',
    'blog.apps.BlogConfig',
    'tools.apps.ToolsConfig',
    'search.apps.SearchConfig',
    'verify.apps.VerifyConfig',
    'conversations.apps.ConversationsConfig',
    'application.apps.ApplicationConfig',

    # SOCIAL AUTH
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    ## SOCIAL AUTH PROVIDERS
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.spotify',

    ]

    MIDDLEWARES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
    def get_default_template(BASE_DIR=None):
        return {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ## DJANGO IN BUILTS
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    }

    def get_database(BASE_DIR=None):
        data = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

        db_from_env = dj_database_url.config(conn_max_age=None, ssl_require=True)
        data['default'].update(db_from_env)

        return data

    AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
    
    ]    

    AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
] 


class SocialAuth(NamedTuple):
    PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'user:email',
            'read:email',
        ],
    }
}

class Jazzmin(NamedTuple):
    
    SETTINGS = {

    # Logo to use for this site
    "site_logo": "images/favicon.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Text Analyzer Admin Panel",

    # Copyright on the footer
    "copyright": "Text Analyzer Ltd",

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "/contact",
            "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

    ],
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",



    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "View Site", "url": "/",
            "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # UI BUILDER
    "show_ui_builder": bool(os.getenv('ADMIN_UI_BUILDER')),

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        # ADDING ICONS TO THE DJANGO IN BUILT MODELS
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "sites.Site" : "fas fa-globe",

       # ADDING ICONS TO THE CUSTOM DJANGO APPS MADE WITH `django-admin startapp`
        "api.Contact": "fas fa-phone-alt",        
        "member.Profile" : "fas fa-user-circle",
        "blog.Blog" : "fab fa-blogger",
        "blog.Comment" : "fas fa-comments",
        "search.SearchDB" : "fas fa-search",
        "verify.VerifyUser" : "fas fa-certificate",
        "application.Application" : "fas fa-scroll",

        # DJANGO SOCIAL AUTH
        "account.EmailAddress" : "fas fa-envelope",
        "socialaccount.SocialAccount" : "fas fa-user-circle",
        "socialaccount.SocialToken" : "fas fa-coins",
        "socialaccount.SocialApp" : "fas fa-mobile",
    },
}

    UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

class Recaptcha(NamedTuple):
    sitekey = "6LcTDY8hAAAAAMsgJmPUvu2R-91zsDrquww1Eltk"
    secretKey = os.getenv("RECAPTCHA_SITE_SECRET")
