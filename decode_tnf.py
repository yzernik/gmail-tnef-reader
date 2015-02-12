import sys
import base64


from tnefparse import TNEF


def decode_tnef(fname):
    data = open(fname, "rb").read().decode('base64')
    t = TNEF(data)
    for attch in t.attachments:
        save_attachment(attch)


def save_attachment(attch):
    name = attch.long_filename()
    print name
    with open(name, 'w') as f:
        data = attch.data
        f.write(data)


def main():
    if len(sys.argv) < 2:
        print 'missing input file arg'
        sys.exit(2)
    tnef_fname = sys.argv[1]
    decode_tnef(tnef_fname)
    


if __name__ == "__main__":
    main()
