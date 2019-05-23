import decode_and_encode
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


def get_args(args):
    input_data = None
    output = None
    arguments = {}
    if args.method == 'train':
        if args.text_file is not None:
            with open(args.text_file, 'r') as file:
                train_text = file.read()
        else:
            train_text = input()
        arguments['train_text'] = train_text

    else:
        if args.method == 'hack':
            with open(args.model_file, 'r') as modelfile:
                bar_chart = modelfile.readline()
            arguments['bar_chart'] = bar_chart

        if args.input_file is not None:
            with open(args.input_file, 'r') as inputfile:
                input_data = inputfile.read()
        else:
            input_data = input()

        if args.output_file is not None:
            output = args.output_file
        arguments['input_data'] = input_data
        arguments['output'] = output
    return arguments


def print_output_data(output_data, curr_args):
    if output_data is None:
        return
    else:
        if curr_args['output'] is None:
            print(output_data)
        else:
            with open(curr_args['output'], 'w') as file:
                file.write(output_data)


curr_args = get_args(args)
output_data = None

if args.method == 'encode':
        if args.cipher == 'caesar':
            output_data = decode_and_encode.caesar_encode(args.key, curr_args['input_data'])
        elif args.cipher == 'vigenere':
            output_data = decode_and_encode.vigenere_encode(args.key, curr_args['input_data'])

elif args.method == 'decode':
        if args.cipher == 'caesar':
            output_data = decode_and_encode.caesar_decode(args.key, curr_args['input_data'])

        elif args.cipher == 'vigenere':
            output_data = decode_and_encode.vigenere_decode(args.key, curr_args['input_data'])

elif args.method == 'hack':
        output_data = hack_.hack(curr_args['input_data'], curr_args['bar_chart'])

elif args.method == 'train':
        with open(args.model_file, 'w') as modelfile:
            modelfile.write(hack_.train_encode(curr_args['train_text']))


print_output_data(output_data, curr_args)
