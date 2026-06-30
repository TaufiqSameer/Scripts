import hashlib
import string
import argparse
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed


def generate(file):
    with open(file, "r") as f:
        for line in f:
            yield line.strip()


def check_password(password, target_hash, hash_fn):
    hashed = hash_fn(password.encode()).hexdigest()

    if hashed == target_hash:
        return password

    return None


def hash_type(hash_):
    length = len(hash_)

    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA-1"
    elif length == 56:
        return "SHA-224"
    elif length == 64:
        return "SHA-256"
    elif length == 96:
        return "SHA-384"
    elif length == 128:
        return "SHA-512"
    else:
        return "Unknown"


def crack_hash(hash_, file):

    algo = hash_type(hash_)

    print("Hash Type:", algo)

    algorithms = {
        "MD5": hashlib.md5,
        "SHA-1": hashlib.sha1,
        "SHA-224": hashlib.sha224,
        "SHA-256": hashlib.sha256,
        "SHA-384": hashlib.sha384,
        "SHA-512": hashlib.sha512,
    }

    if algo not in algorithms:
        print("Unsupported hash type.")
        return

    hash_fn = algorithms[algo]

    with ThreadPoolExecutor(max_workers=4) as exe:

        futures = []

        for password in generate(file):
            future = exe.submit(check_password,password,hash_,hash_fn)
            futures.append(future)
        for future in tqdm(as_completed(futures), total=len(futures)):
            result = future.result()
            if result:
                print(f"\nPassword Found: {result}")
                return
    print("\nPassword not found.")
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple Hash Cracker")

    parser.add_argument("hash", help="Target hash")
    parser.add_argument("wordlist", help="Wordlist file")

    args = parser.parse_args()

    crack_hash(args.hash, args.wordlist)