import subbreaker

import argparse

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Evaluate the model')
    argparser.add_argument('-i','--input', type=str, required=True, help='Input file')
    argparser.add_argument('-o', '--output', type=str, required=True, help='Output file')

    args = argparser.parse_args()

    print(args.input)
    print(args.output)
    with open(args.input, 'r') as f:
        lines = f.readlines()

    with open("EN.json", 'r') as f:
        breaker = subbreaker.Breaker(f)

    with open(args.output, 'w') as f:
        for line in lines:
            result = breaker.break_cipher(line.strip("\n"))
            f.write(line.strip("\n") + " | " + result.plaintext + " - " + str(result.fitness) + "\n")
    