import torch
import torch.nn as nn
from torchvision import models
from torch.nn.functional import relu, sigmoid

class UNet(nn.Module):
    def __init__(self, n_class):
        super().__init__()
        
        # Encoder
        # In the encoder, convolutional layers with the Conv2d function are used to extract features from the input image. 
        # Each block in the encoder consists of two convolutional layers followed by a max-pooling layer, with the exception of the last block which does not include a max-pooling layer.
        # -------
        # input: 512x512x3
        self.e11 = nn.Conv2d(3, 64, kernel_size=3, padding=1) # output: 512x512x64
        self.e12 = nn.Conv2d(64, 64, kernel_size=3, padding=1) # output: 512x512x64
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2) # output: 256x256x64

        # input: 256x256x64
        self.e21 = nn.Conv2d(64, 128, kernel_size=3, padding=1) # output: 256x256x128
        self.e22 = nn.Conv2d(128, 128, kernel_size=3, padding=1) # output: 256x256x128
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2) # output: 128x128x128

        # input: 128x128x128
        self.e31 = nn.Conv2d(128, 256, kernel_size=3, padding=1) # output: 128x128x256
        self.e32 = nn.Conv2d(256, 256, kernel_size=3, padding=1) # output: 128x128x256
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2) # output: 64x64x256

        # input: 64x64x256
        self.e41 = nn.Conv2d(256, 512, kernel_size=3, padding=1) # output: 64x64x512
        self.e42 = nn.Conv2d(512, 512, kernel_size=3, padding=1) # output: 64x64x512
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2) # output: 32x32x512

        # input: 32x32x512
        self.e51 = nn.Conv2d(512, 1024, kernel_size=3, padding=1) # output: 32x32x1024
        self.e52 = nn.Conv2d(1024, 1024, kernel_size=3, padding=1) # output: 32x32x1024

        # # Custom: color finding
        # # 3*n_class are new channels to be appended to the output of encoder
        self.f1 = nn.Linear(32*32*1024, 512)
        self.f2 = nn.Linear(512, 3*n_class) # output: 3*n_class

        # Decoder
        self.upconv1 = nn.ConvTranspose2d(1042, 512, kernel_size=2, stride=2)
        # self.upconv1 = nn.ConvTranspose2d(1024, 512, kernel_size=2, stride=2)
        self.d11 = nn.Conv2d(1024, 512, kernel_size=3, padding=1)
        self.d12 = nn.Conv2d(512, 512, kernel_size=3, padding=1)

        self.upconv2 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.d21 = nn.Conv2d(512, 256, kernel_size=3, padding=1)
        self.d22 = nn.Conv2d(256, 256, kernel_size=3, padding=1)

        self.upconv3 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.d31 = nn.Conv2d(256, 128, kernel_size=3, padding=1)
        self.d32 = nn.Conv2d(128, 128, kernel_size=3, padding=1)

        self.upconv4 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.d41 = nn.Conv2d(128, 64, kernel_size=3, padding=1)
        self.d42 = nn.Conv2d(64, 64, kernel_size=3, padding=1)

        # Output layer
        self.outconv = nn.Conv2d(64, n_class, kernel_size=1)

    def forward(self, x):
        # Encoder
        xe11 = relu(self.e11(x))
        xe12 = relu(self.e12(xe11))
        xp1 = self.pool1(xe12)

        xe21 = relu(self.e21(xp1))
        xe22 = relu(self.e22(xe21))
        xp2 = self.pool2(xe22)

        xe31 = relu(self.e31(xp2))
        xe32 = relu(self.e32(xe31))
        xp3 = self.pool3(xe32)

        xe41 = relu(self.e41(xp3))
        xe42 = relu(self.e42(xe41))
        xp4 = self.pool4(xe42)

        xe51 = relu(self.e51(xp4))
        xe52 = relu(self.e52(xe51))

        # # Custom: color finding
        f1 = relu(self.f1(torch.flatten(xe52, 1)))
        f2 = sigmoid(self.f2(f1))
        f3 = f2.view(f2.size(0), f2.size(1), 1, 1)
        f4 = f3.expand(f3.size(0), f3.size(1), 32, 32)
        f5 = torch.cat([xe52, f4], dim=1)
        color_out = f2
        
        # Decoder
        # xu1 = self.upconv1(xe52)
        xu1 = self.upconv1(f5)
        xu11 = torch.cat([xu1, xe42], dim=1)
        xd11 = relu(self.d11(xu11))
        xd12 = relu(self.d12(xd11))

        xu2 = self.upconv2(xd12)
        xu22 = torch.cat([xu2, xe32], dim=1)
        xd21 = relu(self.d21(xu22))
        xd22 = relu(self.d22(xd21))

        xu3 = self.upconv3(xd22)
        xu33 = torch.cat([xu3, xe22], dim=1)
        xd31 = relu(self.d31(xu33))
        xd32 = relu(self.d32(xd31))

        xu4 = self.upconv4(xd32)
        xu44 = torch.cat([xu4, xe12], dim=1)
        xd41 = relu(self.d41(xu44))
        xd42 = relu(self.d42(xd41))

        # Output layer
        out = self.outconv(xd42)

        return out, color_out