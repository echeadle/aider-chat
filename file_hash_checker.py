import os
import hashlib

def hash_file(file_path):
    """Generate a hash for a given file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def store_file_hashes(directory, output_file):
    """Recursively traverse the directory, hash files, and store the hashes."""
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(directory):
            if '.venv' not in root:
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = hash_file(file_path)
                    f.write(f"{file_hash} {file_path}\n")

def find_identical_files(hash_file):
    """Read the hash file and find identical files."""
    hash_dict = {}
    with open(hash_file, 'r') as f:
        for line in f:
            file_hash, file_path = line.strip().split(' ', 1)
            if file_hash in hash_dict:
                hash_dict[file_hash].append(file_path)
            else:
                hash_dict[file_hash] = [file_path]

    for file_hash, paths in hash_dict.items():
        if len(paths) > 1:
            print(f"Identical files with hash {file_hash}:")
            for path in paths:
                print(f" - {path}")

if __name__ == "__main__":
    directory_to_check = "/home/echeadle/Aug_2024"
    hash_output_file = "file_hashes.txt"

    store_file_hashes(directory_to_check, hash_output_file)
    find_identical_files(hash_output_file)
