ipMask = raw_input('enter ip/mask: ')
ip = ipMask.split('/')[0]
mask = ipMask.split('/')[1]
ipDecList = ip.split('.')
ipMaskStrOnes = '1' * int(mask)
print(ipDecList)
print(ipMaskStrOnes)
ipMaskStr_template = '{:032}'
ipMaskStr = ipMaskStr_template.format(ipMaskStrOnes)
print ipMaskStr
