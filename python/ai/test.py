import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Load and preprocess the dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# Define the Neural Network
class SimpleNN(nn.Module):
	def __init__(self):
		super(SimpleNN, self).__init__()
		self.fc1 = nn.Linear(28 * 28, 128)  # Fully connected layer (784 -> 128)
		self.fc2 = nn.Linear(128, 64)	   # Fully connected layer (128 -> 64)
		self.fc3 = nn.Linear(64, 10)		# Fully connected layer (64 -> 10)
		
	def forward(self, x):
		x = x.view(-1, 28 * 28)  # Flatten the image (28x28 -> 784)
		x = torch.relu(self.fc1(x))
		x = torch.relu(self.fc2(x))
		x = self.fc3(x)
		return x

net = SimpleNN()

# Define Loss Function and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

# Train the Network
for epoch in range(5):  # loop over the dataset multiple times
	running_loss = 0.0
	for i, data in enumerate(trainloader, 0):
		# get the inputs; data is a list of [inputs, labels]
		inputs, labels = data

		# zero the parameter gradients
		optimizer.zero_grad()

		# forward + backward + optimize
		outputs = net(inputs)
		loss = criterion(outputs, labels)
		loss.backward()
		optimizer.step()

		# print statistics
		running_loss += loss.item()
		if i % 100 == 99:  # print every 100 mini-batches
			print(f'[Epoch: {epoch + 1}, Mini-batch: {i + 1}] loss: {running_loss / 100}')
			running_loss = 0.0

print('Finished Training')

# Test the Network
correct = 0
total = 0
with torch.no_grad():
	for data in testloader:
		images, labels = data
		outputs = net(images)
		_, predicted = torch.max(outputs.data, 1)
		total += labels.size(0)
		correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct / total}%')

# Save the Trained Model
torch.save(net.state_dict(), 'simple_nn.pth')