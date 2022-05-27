
import logging

logging.basicConfig(level=logging.DEBUG, filename="mylog1.log", filemode=w)

def multiplyMe(x, y):
    return x * y

i = int(input("Enter the first number :"))
j = int(input("Enter ths second number :"))

logging.debug("Product of {0} and {1} is {2}".format(i, j, multiplyMe(i, j)))
logging.info("Product of {0} and {1} is {2}".format(i, j, multiplyMe(i, j)))
logging.warning("Product of {0} and {1} is {2}".format(i, j, multiplyMe(i, j)))
logging.error("Product of {0} and {1} is {2}".format(i, j, multiplyMe(i, j)))
logging.critical("Product of {0} and {1} is {2}".format(i, j, multiplyMe(i, j)))
