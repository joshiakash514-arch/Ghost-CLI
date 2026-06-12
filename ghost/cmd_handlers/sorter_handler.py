from ghost.core.download_sorter import (
    sorter
)

def sorter_handler(args):
    if(args.module == "sort"):
        sorter(args.path)