find . -type d -name "maybe*" | find . -type f ! -perm /u=x,g=x,o=x | find . -type f -size 1033c
