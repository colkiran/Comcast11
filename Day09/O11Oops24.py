
import HDFCBank

def withdraw(self):
    print("You can withdraw max upto 4000.00 per day...")

HDFCBank.HDFC.withdraw = withdraw               # monkey patching

hdfc = HDFCBank.HDFC()
hdfc.withdraw()