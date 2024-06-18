import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import matplotlib.pyplot as plt
from tqdm import tqdm
import json

device = "cuda:0"

try:
    with open("gradient_norms.json", "r") as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = {"individual_gradient_norms": {}, "batch_gradient_norms": {}}

# Define the batch sizes
# batch_sizes = [16, 32, 64, 128]
batch_sizes = [256, 512]

# Load and transform the MNIST dataset
transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])


# Create ResNet-18 model function
def create_resnet18_model():
    model = models.resnet18(pretrained=False)
    model.conv1 = nn.Conv2d(
        1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False
    )
    model.fc = nn.Linear(model.fc.in_features, 10)  # Adjust for MNIST
    model.to(device)
    return model


# Function to compute gradient norms
def compute_gradient_norms(model):
    individual_norms = []
    total_norm = 0
    for param in model.parameters():
        if param.grad is not None:
            norm = param.grad.norm().item()
            individual_norms.append(norm)
            total_norm += norm**2
    total_norm = total_norm**0.5
    return individual_norms, total_norm


# Prepare for storing gradient norms
individual_gradient_norms = {batch_size: [] for batch_size in batch_sizes}
batch_gradient_norms = {batch_size: [] for batch_size in batch_sizes}

# Training loop for each batch size
for batch_size in batch_sizes:
    # Data loader for the current batch size
    trainset = torchvision.datasets.MNIST(
        root="./data", train=True, download=True, transform=transform
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True
    )

    # Initialize the model and optimizer
    net = create_resnet18_model()
    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

    for epoch in range(10):  # Number of epochs
        with tqdm(trainloader, unit="batch") as tepoch:
            for data in tepoch:
                tepoch.set_description(f"Epoch {epoch+1}, Batch Size {batch_size}")

                inputs, labels = data[0].to(device), data[1].to(device)
                optimizer.zero_grad()
                outputs = net(inputs)
                loss = nn.CrossEntropyLoss()(outputs, labels)
                loss.backward()
                optimizer.step()

                # Compute and store gradient norms
                ind_norms, batch_norm = compute_gradient_norms(net)
                individual_gradient_norms[batch_size].extend(ind_norms)
                batch_gradient_norms[batch_size].append(batch_norm)

import json

# Save the gradient norms data to a file
data = {
    "individual_gradient_norms": individual_gradient_norms,
    "batch_gradient_norms": batch_gradient_norms,
}

with open("gradient_norms.json", "w") as f:
    json.dump(data, f)
