import logging
from app.first import First
from app.second import Second


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    f = First()
    s = Second()

    logger.debug('decrease in number')
    f.decrement_number()
    logger.debug('decrease in number')
    f.decrement_number()

    f.current_number
    logger.debug(f'number --> {f.current_number}')
    logger.debug(f'increase in number')
    f.increment_number()
    logger.debug(f'number --> {f.current_number}')

    logger.debug('Starting the system')
    s.enable_system()
    logger.debug('Stopping the system')
    s.disable_system()


if __name__ == '__main__':
    main()
