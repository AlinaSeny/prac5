import sys


def wav_format():
    if len(f) < 44:
        return False
    elif f[:4] != b'RIFF' or f[8:16] != b'WAVEfmt ' or f[36:40] != b'data':
        return False
    return True


f = sys.stdin.buffer.read()
if not wav_format():
    print("NO")
else:
    print(f"Size={int.from_bytes(f[4:8], 'little')}",
          f"Type={int.from_bytes(f[20:22], 'little')}",
          f"Channels={int.from_bytes(f[22:24], 'little')}",
          f"Rate={int.from_bytes(f[24:28], 'little')}",
          f"Bits={int.from_bytes(f[34:36], 'little')}",
          f"Data={int.from_bytes(f[40:44], 'little')}", sep=', ')
