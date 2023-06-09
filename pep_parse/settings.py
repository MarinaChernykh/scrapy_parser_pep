from pathlib import Path


BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

PEP_DOMAIN = 'peps.python.org'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
