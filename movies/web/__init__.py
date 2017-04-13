import logging

try:
    logger = logging.getLogger('ServerMovies')
    logger.setLevel(logging.INFO)
    hdlr = logging.FileHandler('/tmp/server_movies.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s :%(lineno)s - %(funcName)s() %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
except Exception as e:
    print str(e)