import os
import sys

if len(sys.argv) > 2:
    print("Too many Arguments...")
elif len(sys.argv) < 2:
    print("Pass 2 Arguments Only...")

i=sys.argv[0]
print(i)
i=sys.argv[1]
print(i)