# File-Handling
A visually rich file management app built with Python &amp; Streamlit. Create, read, update, and delete files through an animated, gradient-themed dashboard with live stats, search, and file-type icons. Safe sandboxed storage, clean UI/UX, and smooth micro-interactions for a polished user experience.

# 🗂️ File Manager Studio — Aurora Edition

A visually rich, animated file management app built with **Python + Streamlit**. Create, read, update, and delete text files through a clean, colorful dashboard — no command line needed.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Full CRUD operations** — Create, Read, Update (rename / append / overwrite), and Delete files
- **Live dashboard** — total files, storage used, and last activity at a glance
- **File-type aware UI** — different icons and accent colors for `.py`, `.txt`, `.csv`, `.json`, `.md`, and more
- **Search** — quickly filter files by name
- **Download support** — download any file straight from the Read view
- **Safe by design** — all operations are sandboxed inside a local `workspace/` folder
- **Polished UI/UX** — animated gradient background, glowing hero header, hover effects, and celebratory balloons/snow on actions

## 🖼️ Preview

> _Add a screenshot or screen recording GIF here after running the app locally._
>
> ```
> ![App Screenshot](screenshots/dashboard.png)
> ```

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **Core concepts:** File I/O, `pathlib`, exception handling, session state

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/Ritesh-raj75/file-manager-studio.git
cd file-manager-studio

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

## 📂 Project Structure

```
file-manager-studio/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── workspace/           # Auto-created folder where your files live
└── README.md
```

## 🎯 What I Learned

- Building interactive UIs in Python using Streamlit (forms, session state, custom CSS)
- Safe file-handling patterns using `pathlib` and exception handling
- Designing a clean, modern UI/UX with gradients, animations, and micro-interactions

## 📌 Future Improvements

- [ ] Support for binary files (images, PDFs)
- [ ] Folder/subfolder navigation
- [ ] Multi-file upload
- [ ] Dark/light theme toggle
- [ ] Deploy live demo on Streamlit Community Cloud

## 👤 Author

**Ritesh Raj**
M.Tech, Artificial Intelligence & Data Science — IIT Patna
[GitHub](https://github.com/Ritesh-raj75) · [LinkedIn](https://linkedin.com/in/ritesh-raj-18775a238)

## 📄 License

This project is licensed under the MIT License.
