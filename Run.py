import os, sys
try:
    __import__("Pro").main()
except Exception as e:
    exit(str(e))
