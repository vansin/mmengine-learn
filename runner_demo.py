# 准备训练任务所需要的模块
import torch
from torch import nn
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
from mmengine.model import BaseModel
from mmengine.optim.scheduler import MultiStepLR

# 定义一个多层感知机网络
class Network(BaseModel):
    def __init__(self):
        super().__init__()
        self.mlp = nn.Sequential(nn.Linear(28 * 28, 128), nn.ReLU(), nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, 10))
        self.loss = nn.CrossEntropyLoss()

    def forward(self, batch_inputs: torch.Tensor, data_samples = None, mode: str = 'tensor'):
        x = batch_inputs.flatten(1)
        x = self.mlp(x)
        if mode == 'loss':
            return {'loss': self.loss(x, data_samples)}
        elif mode == 'predict':
            return x.argmax(1)
        else:
            return x

model = Network()

# 构建优化器
optimzier = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# 构建参数调度器用于调整学习率
lr_scheduler = MultiStepLR(milestones=[2], by_epoch=True)
# 构建手写数字识别 (MNIST) 数据集
train_dataset = datasets.MNIST(root="MNIST", download=True, train=True, transform=transforms.ToTensor())
# 构建数据加载器
train_dataloader = DataLoader(dataset=train_dataset, batch_size=10, num_workers=2)