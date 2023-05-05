# Image Classifier with PyTorch - 4302

**Language**: `Python`

**Lines of code**: `75`

## Description

This program uses PyTorch to create a deep neural network that can classify images. The program uses a pre-trained model to extract features from the images and then trains a fully connected network on top of these features to classify the images into one of several categories.

## Code

``` Python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt

# Define the transforms to be applied to the data
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load the CIFAR10 dataset
trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

# Define the pre-trained model
model_conv = torchvision.models.resnet18(pretrained=True)
for param in model_conv.parameters():
    param.requires_grad = False

# Replace the final fully connected layer of the model with a new one that has 10 outputs
num_ftrs = model_conv.fc.in_features
model_conv.fc = nn.Linear(num_ftrs, 10)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model_conv.fc.parameters(), lr=0.001, momentum=0.9)

# Train the model for a few epochs
for epoch in range(5):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # Get the inputs and labels
        inputs, labels = data

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward + backward + optimize
        outputs = model_conv(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # Print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Finished Training')

# Test the model on some images
dataiter = iter(trainloader)
images, labels = dataiter.next()

# Show the images and their predicted labels
outputs = model_conv(images)
_, predicted = torch.max(outputs, 1)

fig, axs = plt.subplots(2, 2)
fig.tight_layout()

for i in range(4):
    axs[i//2, i%2].imshow(np.transpose(images[i], (1, 2, 0)))
    axs[i//2, i%2].set_title(f"Predicted: {trainset.classes[predicted[i]]}")

plt.show()

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.

Your response should include machine learning using pytorch
```