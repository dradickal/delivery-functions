import torch

def main():
    x = torch.rand(5, 3)
    return {
        'body': f'Torch Results: {x}'
    }