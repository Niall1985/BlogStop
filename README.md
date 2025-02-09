# BlogStop - A Simple Blogging Platform

BlogStop is a minimal and user-friendly blogging platform built with **Streamlit** and **Google Gemini AI**. Users can create, view, and manage their blog posts with AI-assisted content generation.

---

## 🚀 Features
- **User Authentication**: Login and signup functionality to secure user access.
- **Create Posts**: Users can write their own blog posts.
- **AI-Assisted Writing**: Generate engaging content using **Google Gemini AI**.
- **View Posts**: Browse through previously created blog posts.
- **Logout Option**: Securely sign out from the platform.

---

## 📂 Project Structure
```
BlogStop/
│── posts.json             # Stores blog posts
│── .gitignore             # Ignores unnecessary files (e.g., posts.json)
│── login_signup.py        # Handles user authentication
│── home.py                # Displays the home page with recent posts
│── create_post.py         # Allows users to write and publish posts
│── requirements.txt       # Lists required dependencies
│── README.md              # Documentation for the project
```

---

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Niall1985/BlogStop.git
cd BlogStop
```

### 2️⃣ Set Up a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key
Create a `.env` file and add your **Google Gemini AI** API key:
```
key=your_api_key_here
```

### 5️⃣ Run the Application
```bash
streamlit run login_signup.py
```

---

## 🏗 Usage Guide
- **Login/Signup**: Users must log in before accessing the platform.
- **Create Post**: Navigate to `Create Post` and write your blog.
- **AI Writing Assistance**: Click `Write with AI` to generate AI-powered content.
- **View Posts**: Browse through published blog posts on the homepage.
- **Logout**: Securely sign out using the `Signout` option.

---

## 📝 To-Do List
- [ ] Add database integration (SQLite/PostgreSQL) for persistent storage.
- [ ] Implement user authentication with hashed passwords.
- [ ] Improve UI with custom CSS and styling.
- [ ] Deploy the app on a cloud platform (e.g., Heroku, Render).

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, make enhancements, and submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

---