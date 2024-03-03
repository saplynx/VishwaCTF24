#!/usr/bin/python
# Based off a script originally found here: https://teamrocketist.github.io/2017/08/29/Forensics-Hackit-2017-USB-ducker/
# Additions include: More keys, deletion

KEY_CODES = {
    0x04:['a', 'A'],
    0x05:['b', 'B'],
    0x06:['c', 'C'],
    0x07:['d', 'D'],
    0x08:['e', 'E'],
    0x09:['f', 'F'],
    0x0A:['g', 'G'],
    0x0B:['h', 'H'],
    0x0C:['i', 'I'],
    0x0D:['j', 'J'],
    0x0E:['k', 'K'],
    0x0F:['l', 'L'],
    0x10:['m', 'M'],
    0x11:['n', 'N'],
    0x12:['o', 'O'],
    0x13:['p', 'P'],
    0x14:['q', 'Q'],
    0x15:['r', 'R'],
    0x16:['s', 'S'],
    0x17:['t', 'T'],
    0x18:['u', 'U'],
    0x19:['v', 'V'],
    0x1A:['w', 'W'],
    0x1B:['x', 'X'],
    0x1C:['y', 'Y'],
    0x1D:['z', 'Z'],
    0x1E:['1', '!'],
    0x1F:['2', '@'],
    0x20:['3', '#'],
    0x21:['4', '$'],
    0x22:['5', '%'],
    0x23:['6', '^'],
    0x24:['7', '&'],
    0x25:['8', '*'],
    0x26:['9', '('],
    0x27:['0', ')'],
    0x28:['\n','\n'],
    0x2a:['\ndelete\n','\ndelete\n'],
    0x2b:['\ntab\n','\ntab\n'],
    0x2C:[' ', ' '],
    0x2D:['-', '_'],
    0x2E:['=', '+'],
    0x2F:['[', '{'],
    0x30:[']', '}'],
    0x32:['#','~'],
    0x33:[';', ':'],
    0x34:['\'', '"'],
    0x36:[',', '<'],
    0x38:['/', '?'],
    0x37:['.', '>'],
    0x2b:['\t','\t'],
    0x4b:['\nPageUp\n','\nPageUp\n'],
    0x4c:['\nFwdDelete\n', '\nFwdDelete\n'],
    0x4d:['\nEnd\n','\nEnd\n'],
    0x4e:['\nPageDown\n','\nPageDown\n'],
    0x4f:[u'→',u'→'],
    0x50:[u'←',u'←'],
    0x51:[u'↓',u'↓'],
    0x52:[u'↑',u'↑']
}
   
#tshark -r ./usb.pcap -Y 'usb.capdata' -T fields -e usb.capdata > keyboards.txt
keyboardData = open('keyboard').read().split('\n')[:-1]
# Keyboard data is of format:
# 00:00:00:00:00:00:00:00
# 00:00:50:00:00:00:00:00
# 00:00:00:00:00:00:00:00
# 00:00:2a:00:00:00:00:00
# 00:00:00:00:00:00:00:00

cursor_x = 0
cursor_y = 0
offset_current_line = 0
output = []

for data in keyboardData:
    if data.split(':')[0] != '':
        shift = int(data.split(':')[0], 16) / 2
        key = int(data.split(':')[2], 16)
        
        if shift > 0:
            shift = 1

        if key == 0:
            continue
        elif KEY_CODES[key][shift] == u'↑':
            print "cursor y"
            lines[cursor_y] += output
            cursor_y -= 1
        elif KEY_CODES[key][shift] == u'↓':
            print "cursor y"
            lines[cursor_y] += output
            cursor_y += 1
        elif KEY_CODES[key][shift] == u'→':
            print "cursor x"
            cursor_x += 1
        elif KEY_CODES[key][shift] == u'←':
            print "cursor x"
            cursor_x -= 1
        elif KEY_CODES[key][shift] == '\n':
            print "newline"
            output.insert(cursor_x, KEY_CODES[key][shift])
        elif KEY_CODES[key][shift] == '\ndelete\n':
            print 'delete'
            cursor_x -= 1
            output.pop(cursor_x)
        else:
            output.insert(cursor_x, KEY_CODES[key][shift])
            cursor_x += 1
    print cursor_x, len(''.join(output))

print ''.join(output)


