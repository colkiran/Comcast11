
import logging

logging.basicConfig(level=logging.DEBUG, filename="mylog2.log",
                    format="%(asctime)s : %(name)s : %(levelname)s , %(message)s : %(filename)s : %(lineno)d")

inv = 1
num = 0

try:
    inv = 1 / num

except ZeroDivisionError as z:
    logging.debug(z)
except TypeError as t:
    logging.debug(t)
except Exception as e:
    logging.error(e)
else:
    print(f"The inverse of {num} is :{inv}")
    logging.info(f"inverse of {num} is :{inv}")

finally:
    print("Finally block of code.....")