import encode_
import decode_
import train_
import hack_
import argparse

parser = argparse.ArgumentParser()
subs = parser.add_subparsers()
encode = subs.add_parser('encode', description='encode')
encode.set_defaults(method='encode')
encode.add_argument('--cipher', type=str, required=True, help='type of cipher')
encode.add_argument('--key', type=str, required=True, help='key of cipher')
encode.add_argument('--input-file', type=str, required=False, help='')
encode.add_argument('--output-file', type=str, required=False, help='')

decode = subs.add_parser('decode', description='decode')
decode.set_defaults(method='decode')
decode.add_argument('--cipher', type=str, required=True, help='type of cipher')
decode.add_argument('--key', type=str, required=True, help='key of cipher')
decode.add_argument('--input-file', type=str, required=False, help='')
decode.add_argument('--output-file', type=str, required=False, help='')

train = subs.add_parser('train', description='train')
train.set_defaults(method='train')
train.add_argument('--text-file', type=str, required=False, help='')
train.add_argument('--model-file', type=str, required=True, help='')

hack = subs.add_parser('hack', description='hack')
hack.set_defaults(method='hack')
hack.add_argument('--input-file', type=str, required=False, help='')
hack.add_argument('--output-file', type=str, required=False, help='')
hack.add_argument('--model-file', type=str, required=True, help='')

args = parser.parse_args()

if args.method == 'encode':
    if args.input_file is not None:
        with open(args.input_file, 'r') as inputfile:
            file = inputfile.read()
    else:
        file = input()

    if args.output_file is not None:
        outputfile = open(args.output_file, 'w')
        outputfile.write(encode_.code(args.cipher, args.key, file))
        outputfile.close()
    else:
        print(encode_.code(args.cipher, args.key, file))

elif args.method == 'decode':
    if args.input_file is not None:
        with open(args.input_file, 'r') as inputfile:
            file = inputfile.read()
    else:
        file = input()

    if args.output_file is not None:
        outputfile = open(args.output_file, 'w')
        outputfile.write(decode_.code(args.cipher, args.key, file))
        outputfile.close()
    else:
        print(decode_.code(args.cipher, args.key, file))

elif args.method == 'train':
    if args.text_file is not None:
        with open(args.text_file, 'r') as inputfile:
            file = inputfile.read()
    else:
        file = input()
    modelfile = open(args.model_file, 'w')
    modelfile.write(train_.train_encode(file))
    print(train_.train_encode(file))
    modelfile.close()

elif args.method == 'hack':
    if args.input_file is not None:
        with open(args.input_file, 'r') as inputfile:
            file = inputfile.read()
    else:
        file = input()

    modelfile = open(args.model_file, 'r')
    l1 = modelfile.readline()
    l2 = modelfile.readline()
    modelfile.close()

    if args.output_file is not None:
        outputfile = open(args.output_file, 'w')
        outputfile.write(hack_.hack(file, l1, l2))
        outputfile.close()
    else:
        print(hack_.hack(file, l1, l1))
