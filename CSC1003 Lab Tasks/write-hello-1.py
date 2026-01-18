#!/usr/bin/env python3

messege = "Hello world.\n"
file_name = "hello.txt"


with open(file_name, "w") as f:
    f.write(messege)
