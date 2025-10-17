import torch
import torch
import torch.nn as nn
import torch.optim as optim
import random

# Treaning data - savol va javoblar
training_data = [
    ("salom", "salom! qandaysan?"),
    ("qanday xoling?", "Men juda yaxshiman, rahmat!"),
    ("mening ismim Ahror", "Salomalaikum Ahror!"),
    ("sizning ismingiz nima?", "Men chatbot bo'lib, ismim yoq!"),
    ("vaqt nima?", "Kechirasiz, men vaqtni bilmayman"),
    ("qanday kuni?", "Bugun qanday kunmi bilmayman"),
    ("xayr", "Xayr! Yana ko'rishguncha!"),
    ("rahmat", "Arziydi!"),
    ("menga yordam ber", "Keling, qanday yordam kerak?"),
    ("bu nima?", "Bu PyTorch chatbot!"),
]

# Foydalanuvchi kiritish
user_input = input("Savol bering: ")

# Matn to'plami
all_text = " ".join([q + " " + a for q, a in training_data])
vocab = sorted(set(all_text.lower().split()))
word_to_idx = {w: i for i, w in enumerate(vocab)}
idx_to_word = {i: w for i, w in enumerate(vocab)}

def text_to_vec(text):
    """Matnni vektorga aylantirish"""
    words = text.lower().split()
    vec = torch.zeros(len(vocab))
    for word in words:
        if word in word_to_idx:
            vec[word_to_idx[word]] += 1
    return vec / (len(words) + 1e-5)

# Prepare training data
questions = [text_to_vec(q) for q, _ in training_data]
answers = [text_to_vec(a) for _, a in training_data]

X_train = torch.stack(questions)
y_train = torch.stack(answers)

# Neural Network
class ChatbotNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

input_size = len(vocab)
hidden_size = 64
output_size = len(vocab)

model = ChatbotNN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training
print("Chatbot tarbiyalashda...")
for epoch in range(500):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

print("\n✅ Chatbot tayyor!")
print("=" * 50)

# Savollarga javob berish
def get_response(user_text):
    user_vec = text_to_vec(user_text)
    with torch.no_grad():
        output = model(user_vec)
    
    # Eng yaxshi javobni topish
    top_indices = torch.argsort(output, descending=True)[:5]
    
    # Eng yaqin savolni topish
    similarities = torch.cosine_similarity(user_vec.unsqueeze(0), X_train)
    best_match_idx = torch.argmax(similarities).item()
    
    if similarities[best_match_idx] > 0.3:
        return training_data[best_match_idx][1]
    else:
        return "Kechirasiz, shunga javob bilmayman. Boshqa savol bering!"

# Chat loop
print("Chatbot: Salom! Menga savol ber (chiqish uchun 'exit' yoz)")
print("-" * 50)

while True:
    user_input = input("\nSiz: ").strip()
    if user_input.lower() == "exit":
        print("Chatbot: Xayr!")
        break
    if user_input:
        response = get_response(user_input)
        print(f"Chatbot: {response}")