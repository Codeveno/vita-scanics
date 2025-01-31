import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms

# Define a simple CNN model
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(32 * 128 * 128, 128)
        self.fc2 = nn.Linear(128, 10)  # 10 classes for example

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 32 * 128 * 128)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Define a custom dataset
class MedicalImageDataset(Dataset):
    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image = cv2.imread(self.image_paths[idx], cv2.IMREAD_GRAYSCALE)
        if self.transform:
            image = self.transform(image)
        label = self.labels[idx]
        return image, label

# Training function
def train_model():
    # Define transforms
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Example dataset
    image_paths = ["path/to/image1.png", "path/to/image2.png"]  # Replace with actual paths
    labels = [0, 1]  # Replace with actual labels
    dataset = MedicalImageDataset(image_paths, labels, transform=transform)
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    # Initialize model, loss function, and optimizer
    model = CNNModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    for epoch in range(10):  # 10 epochs
        for images, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch + 1}, Loss: {loss.item()}')

    # Save the trained model
    torch.save(model.state_dict(), 'cnn_model.pth')

if __name__ == '__main__':
    train_model()