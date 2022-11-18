import os
import random
import string
import click
from tqdm import tqdm

# generate some string data to write; should we be worried this isn't
# random? 
# string_data = "".join(string.ascii_lowercase * 1000)

def recurse_gen(level, prefix, branch_factor, leaf_number, file_size, first=False):
    if level == 0:
        # leaf level, generate final directories and create the files
        for l in range(leaf_number):
            leaf_dir = os.path.join(prefix, f"{l:010d}")

            os.makedirs(leaf_dir, exist_ok=True)
            with open(os.path.join(leaf_dir, "random.data"), 'w') as fid:

                string_data = ''.join(random.choices(string.ascii_uppercase +
                                                     string.digits, k=file_size))
                fid.write(string_data)

                          #fid.write(randbytes(file_size))
        
    else:

        if first:
            iterator = tqdm
        else:
            iterator = lambda x: x
        for i in iterator(range(branch_factor)):
            dir_str = f"{i:06d}"
            path = os.path.join(prefix, dir_str)

            os.makedirs(path, exist_ok=True)

            recurse_gen(level-1, path, branch_factor, leaf_number, file_size)

    
@click.command()
@click.option("--recurse-levels", type=click.INT,
              help="how many recursive levels of directories to create")
@click.option("--branch-factor", type=click.INT,
              help="what is the branching factor at each directory level")
@click.option("--leaf-number", type=click.INT,
              help="at the final level how many leaf directories will we have")
@click.option("--file-size", default=1024, type=click.INT,
              help='how large is the leaf file (bytes)')
@click.option("--dryrun", is_flag=True, default=False, help="just do a dry run (don't write anything)")
@click.argument("source_dir", default="./")
def generate_files_recursive(recurse_levels, source_dir,
                             branch_factor, leaf_number,
                             dryrun, 
                             file_size):
    """
    Recursively generate a lot of files. No, really, a lot. 

    """


    num_files = branch_factor ** recurse_levels  * leaf_number

    print(f"This will generate {num_files} directories")
    print(f"This will generate {num_files * file_size/1e9:3.4f} GB of data")

    if dryrun:
        print("Dry run, not creating files")
        return
    recurse_gen(recurse_levels, source_dir, branch_factor,
                leaf_number, file_size, first=True)

if __name__ == "__main__":
    generate_files_recursive()

