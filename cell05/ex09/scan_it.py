#!/usr/bin/env python
import sys

if len(sys.argv) != 3:
    print("none")
elif sys.argv[1] not in sys.argv[2]:
    print("none")
else:
    print(sys.argv[2].count(sys.argv[1]))
