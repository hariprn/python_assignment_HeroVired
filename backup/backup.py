import sys
import os
import shutil
import time

if len(sys.argv) != 3:
    print("Usage: python backup.py <source> <destination>")
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]

if not os.path.exists(src):
    print("Source directory does not exist")
    sys.exit(1)

if not os.path.exists(dest):
    print("Destination directory does not exist")
    sys.exit(1)

for file in os.listdir(src):
    src_file = os.path.join(src, file)

    if os.path.isfile(src_file):
        dest_file = os.path.join(dest, file)

        if os.path.exists(dest_file):
            timestamp = time.strftime("%Y%m%d%H%M%S")
            file = f"{timestamp}_{file}"
            dest_file = os.path.join(dest, file)

        shutil.copy(src_file, dest_file)

print("Backup completed successfully")
