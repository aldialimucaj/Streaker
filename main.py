import logging
from streaker.date_manager import DateManager

logger = logging.getLogger(__name__)

def main():
    logger.info('Starting Streaker')
    d_mgr = DateManager('test')
    d_mgr.test()


if __name__ == '__main__':
    main()
