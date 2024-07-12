AUTHOR = 'Joe El Khoury'
SITENAME = 'Joe El Khoury - Data Scientist & MLOps Expert'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LinkedIn', 'https://linkedin.com/in/joe-e-03869096'),
         ('Medium', 'https://medium.com/@jelkhoury880'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://linkedin.com/in/joe-e-03869096'),
          ('Medium', 'https://medium.com/@jelkhoury880'),)

# Disable pagination
DEFAULT_PAGINATION = False

THEME = 'themes/custom_theme'
THEME_STATIC_DIR = 'theme'

# Static paths
STATIC_PATHS = ['images', 'favicon.ico']

# Content path settings
# Add these lines to your pelicanconf.py
PAGE_PATHS = ['pages']
PAGES = [
    ('pages/about.md', 'about.html', 'about.html', 'About'),
    ('pages/cv.md', 'cv.html', 'cv.html', 'CV'),
]

ARTICLE_PATHS = ['articles']

# URL settings
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# Disable unused pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Custom settings
COPYRIGHT_YEAR = '2024'

# Add these lines to your existing pelicanconf.py
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


# Ensure this line is present and correct
THEME = 'themes/custom_theme'

# Add this line to generate the blog category page
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'

# Disable author pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Disable archives pages
ARCHIVES_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''



