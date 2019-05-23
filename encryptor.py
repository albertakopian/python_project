import decode_and_encode
import hack_and_train
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


def proceed_method(args):
    if args.method == 'train':
        if args.text_file is not None:
            with open(args.text_file, 'r') as inputfile:
                file = inputfile.read()
        else:
            file = input()
        with open(args.model_file, 'w') as modelfile:
            modelfile.write(hack_and_train.train_encode(file))
        return

    if args.input_file is not None:
        with open(args.input_file, 'r') as inputfile:
            file = inputfile.read()
    else:
        file = input()

    if args.method == 'hack':
        with open(args.model_file, 'r') as modelfile:
            l = modelfile.readline()

    if args.output_file is not None:
        with open(args.output_file, 'w') as outputfile:
            if args.method in ('encode', 'decode'):
                outputfile.write(eval('decode_and_encode.' + args.cipher + '_' + args.method)(args.key, file))
            else:
                outputfile.write(hack_and_train.hack(file, l))
    elif args.method == 'hack':
        print(hack_and_train.hack(file, l))
    else:
        print(eval('decode_and_encode.' + args.cipher + '_' + args.method)(args.key, file))


proceed_method(args)