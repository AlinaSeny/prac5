import sys

bufin = sys.stdin.buffer.read(1)
tail = sys.stdin.buffer.read()
if tail[-1] == 10:
    tail = tail[:-1]
L = len(tail)
N = bufin[0]

res = []
for i in range(N):
    res.append(tail[int(i*L/N) : int((i + 1)*L/N)])
res.sort()
res = b''.join(res)
#res = res.replace(b'\n', b'')
sys.stdout.buffer.write(bufin)
sys.stdout.buffer.write(res)

