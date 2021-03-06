from block import block
from script import script

blockfile = '/home/marzig76/.bitcoin/blocks/blk00000.dat'

blockstream = open(blockfile, 'rb')

parsed_block = block(blockstream)
print parsed_block

# script examples
# orig              76a914fb96940932cc00274cf6ce423623e0cb0aa32ccf88ac
# 0x4c OP_PUSHDATA1 76a94c14fb96940932cc00274cf6ce423623e0cb0aa32ccf88ac
# 0x4d OP_PUSHDATA2 76a94d0100deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef88ac
# 0x4d OP_PUSHDATA2 76a94d0001ff88ac
# 0x4e OP_PUSHDATA4 76a94e00000001ff88ac
# 0x6a OP_RETURN    6a13636861726c6579206c6f766573206865696469
pk_script = script('6a13636861726c6579206c6f766573206865696469'.decode('hex'))
print pk_script
