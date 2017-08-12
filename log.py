import logging

# logging.basicConfig(filename='myapp.log',
#                     level=logging.INFO,
#                     format='[%(asctime)s]:%(message)s',
#                     datefmt='%Y/%m/%d %I:%M:%S %p')
#
# def main():
#     print 'hello world.'
#     logging.info('the main function get started...')
#     logging.info('say hello to the world.')
#     logging.info('logging is ending...')
#
#
# main()

logging.basicConfig(filename="myapp.log",
                    level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s  %(message)s '
                    )
logger=logging.getLogger()
logger.info("Good morning.")
logger.info("Hello world.....")
#print logger.level  #if not set the level , level will be 30(Warning)
