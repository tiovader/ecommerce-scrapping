from ecommerce.src.spiders import SPIDERS
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
base = f'{dir_path}/venv/Scripts/activate'
if os.name == 'nt':
    ACTIVATE_ENV = base + '.bat'
else:
    ACTIVATE_ENV = f'source {base}'

CHANGE_DIRECTORY = 'cd ecommerce'
RUN_SPIDER = 'scrapy crawl {}'
COMMANDS = ' && '.join((ACTIVATE_ENV, CHANGE_DIRECTORY, RUN_SPIDER))

def main():
    for spider in SPIDERS:
        os.system(COMMANDS.format(spider.name))


if __name__ == '__main__':
    main()
