import argparse
import glob
import logging
import os
import random
import re
import sys

# global directory variables
basedir = os.path.dirname(os.path.abspath(sys.argv[0]))
wordlistsdir = os.path.join(basedir, "wordlists")

# logging 
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger("passphraser")


def roll_dice(x=5):
    return "".join([str(random.randint(1,6)) for _ in range(0,x)])


def load_wordlist_file_info():
    global wordlistsdir
    return {os.path.split(wordlist)[-1].split('.')[0]: wordlist for wordlist in glob.glob(wordlistsdir + "/*.wordlist.asc")}


def load_wordlist_dict(name):
    global wordlistsdir
    fullpath = "{}/{}.wordlist.asc".format(wordlistsdir, name)
    return { line.split()[0]: line.split()[1] for line in open(fullpath).readlines() if re.match("^\d{5}\t", line) }


def parse_args():
    parser = argparse.ArgumentParser(description="Diceware Password Generator")
    parser.add_argument("wordlist", type=str)
    parser.add_argument("-d", "--delimiter", type=str, default=" ")
    parser.add_argument("-w", "--num_of_words", type=int, default=5)
    parser.add_argument("-p", "--num_of_passphrases", type=int, default=20)
    parser.add_argument("-s", "--seed", default=None, help="see this: https://docs.python.org/2/library/random.html#random.seed")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    return parser, args


def generate_passphrase(wordlist_dict, seed, num_of_words, delimiter):
    logger.debug("setting random seed")
    random.seed(seed)
    
    passphrase = []
    for i in range(num_of_words):
        passphrase.append(wordlist_dict[roll_dice()])

    print delimiter.join(passphrase)


def main():
    wlfi = load_wordlist_file_info()
    parser, args = parse_args()
   
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if not args.wordlist in wlfi.keys():
        parser.error("Available wordlists: %s" %  wlfi.keys())

    #print "loading wordlist dictionary" 
    wldict = load_wordlist_dict(args.wordlist)

    for i in range(0, args.num_of_passphrases):
        generate_passphrase(wldict, args.seed, args.num_of_words, args.delimiter)


if __name__ == "__main__":
    main()
