import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head("UNet Model"),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 1, 32, "(0,0,0)", "(0,0,0)", 128, 128, 2),
    to_Conv("conv2", 32, 64, "(2,0,0)", "(conv1-east)", 64, 64, 2),
    to_Conv("conv3", 64, 128, "(2,0,0)", "(conv2-east)", 32, 32, 2),
    to_Conv("conv4", 128, 256, "(2,0,0)", "(conv3-east)", 16, 16, 2),
    to_Conv("conv5", 256, 512, "(2,0,0)", "(conv4-east)", 8, 8, 2),
    to_Pool("pool1", "(0,0,0)", "(conv1-east)", 128, 128, 1),
    to_connection("conv1", "pool1"),
    to_Pool("pool2", "(0,0,0)", "(conv2-east)", 64, 64, 1),
    to_connection("conv2", "pool2"),
    to_Pool("pool3", "(0,0,0)", "(conv3-east)", 32, 32, 1),
    to_connection("conv3", "pool3"),
    to_Pool("pool4", "(0,0,0)", "(conv4-east)", 16, 16, 1),
    to_connection("conv4", "pool4"),
    to_SoftMax("soft1", 1, "(4,0,0)", "(conv1-east)", "Output"),
    to_connection("pool4", "soft1"),
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()