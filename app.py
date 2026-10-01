"""
File Manager Studio — Aurora Edition
A vivid, animated Streamlit front-end over a simple file CRUD engine.
All operations are sandboxed inside a local 'workspace/' folder.

Run with:
    streamlit run app.py
"""

from pathlib import Path
from datetime import datetime

import streamlit as st

# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------
WORKSPACE = Path("workspace")
WORKSPACE.mkdir(exist_ok=True)

st.set_page_config(
    page_title="File Manager Studio",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded",
)

EXT_ICON = {
    ".txt": ("📄", "#00c6ff"), ".md": ("📝", "#6a5cff"), ".py": ("🐍", "#ffd93d"),
    ".json": ("🧾", "#ff6b6b"), ".csv": ("📊", "#4ade80"), ".log": ("🪵", "#c084fc"),
    ".html": ("🌐", "#f97316"), ".css": ("🎨", "#38bdf8"), ".js": ("📜", "#fbbf24"),
}
DEFAULT_ICON = ("📁", "#94a3b8")

# --------------------------------------------------------------------------
# Styling — animated aurora background, glowing cards, gradient everything
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

        /* Animated aurora background */
        .stApp {
            background: #0a0c14;
            background-image:
                radial-gradient(at 15% 20%, rgba(106,92,255,0.25) 0px, transparent 50%),
                radial-gradient(at 85% 10%, rgba(0,198,255,0.20) 0px, transparent 50%),
                radial-gradient(at 50% 90%, rgba(255,107,107,0.15) 0px, transparent 50%),
                radial-gradient(at 90% 80%, rgba(74,222,128,0.15) 0px, transparent 50%);
            background-attachment: fixed;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(14px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes shimmer {
            0% { background-position: -400px 0; }
            100% { background-position: 400px 0; }
        }
        @keyframes glowPulse {
            0%, 100% { box-shadow: 0 0 18px rgba(106,92,255,0.35); }
            50% { box-shadow: 0 0 32px rgba(0,198,255,0.5); }
        }

        /* Hero header */
        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(120deg, #6a5cff 0%, #00c6ff 55%, #4ade80 100%);
            background-size: 200% 200%;
            animation: fadeInUp 0.6s ease, glowPulse 4s ease-in-out infinite;
            border-radius: 20px;
            padding: 32px 36px;
            margin-bottom: 26px;
        }
        .hero h1 {
            color: white;
            margin: 0;
            font-size: 2.3rem;
            font-weight: 800;
            text-shadow: 0 2px 12px rgba(0,0,0,0.25);
        }
        .hero p {
            color: rgba(255,255,255,0.92);
            margin-top: 8px;
            font-size: 1.05rem;
            font-weight: 500;
        }

        /* Stat cards — each a distinct color */
        .stat-box {
            border-radius: 16px;
            padding: 18px 20px;
            text-align: center;
            animation: fadeInUp 0.6s ease;
            border: 1px solid rgba(255,255,255,0.12);
            transition: transform 0.2s ease;
        }
        .stat-box:hover { transform: translateY(-4px) scale(1.02); }
        .stat-purple { background: linear-gradient(145deg, rgba(106,92,255,0.25), rgba(106,92,255,0.05)); }
        .stat-blue   { background: linear-gradient(145deg, rgba(0,198,255,0.25), rgba(0,198,255,0.05)); }
        .stat-green  { background: linear-gradient(145deg, rgba(74,222,128,0.25), rgba(74,222,128,0.05)); }
        .stat-box .num { font-size: 1.8rem; font-weight: 800; color: #ffffff; }
        .stat-box .lbl { font-size: 0.82rem; color: #c3c9d9; margin-top: 4px; font-weight: 500; }

        /* File cards */
        .file-card {
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.09);
            border-left: 4px solid var(--accent, #6a5cff);
            border-radius: 14px;
            padding: 16px 20px;
            margin-bottom: 12px;
            animation: fadeInUp 0.45s ease;
            transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
        }
        .file-card:hover {
            transform: translateX(4px);
            box-shadow: 0 6px 22px rgba(0,0,0,0.35);
        }
        .file-card .fname { font-weight: 600; color: #f5f6fa; font-size: 1.04rem; }
        .file-card .fmeta { color: #8d94a5; font-size: 0.8rem; margin-top: 5px; }
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #6a5cff, #00c6ff);
            color: white;
            padding: 3px 12px;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 700;
            margin-left: 10px;
            letter-spacing: 0.3px;
        }

        /* Buttons */
        .stButton>button {
            border-radius: 12px;
            padding: 0.6rem 1.4rem;
            font-weight: 700;
            border: none;
            background: linear-gradient(135deg, #6a5cff, #00c6ff);
            color: white;
            transition: all 0.2s ease;
            box-shadow: 0 4px 14px rgba(106,92,255,0.35);
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 22px rgba(0,198,255,0.5);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #12141c 0%, #0a0c14 100%);
            border-right: 1px solid rgba(255,255,255,0.06);
        }

        .section-title {
            background: linear-gradient(90deg, #ffffff, #b8bfff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 1.45rem;
            margin-bottom: 4px;
        }
        .section-sub {
            color: #8d94a5;
            font-size: 0.9rem;
            margin-bottom: 20px;
        }

        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {
            border-radius: 10px !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def safe_path(filename: str) -> Path:
    return WORKSPACE / Path(filename).name


def human_size(num_bytes: int) -> str:
    n = float(num_bytes)
    for unit in ["B", "KB", "MB", "GB"]:
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def icon_and_color(path: Path):
    return EXT_ICON.get(path.suffix.lower(), DEFAULT_ICON)


def list_files():
    return sorted(WORKSPACE.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)


def flash(kind: str, message: str, celebrate: str | None = None):
    st.session_state["flash"] = (kind, message, celebrate)


def show_flash():
    if "flash" in st.session_state:
        kind, message, celebrate = st.session_state.pop("flash")
        getattr(st, kind)(message)
        if celebrate == "balloons":
            st.balloons()
        elif celebrate == "snow":
            st.snow()


# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🗂️ File Manager Studio")
    st.caption("✨ Aurora Edition — Python + Streamlit")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["📁 Browse", "➕ Create", "📖 Read", "✏️ Update", "🗑️ Delete"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption(f"Workspace: `{WORKSPACE.resolve().name}/`")

# --------------------------------------------------------------------------
# Hero header + stats
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🗂️ File Manager Studio</h1>
        <p>Create, read, update and delete files — in one vibrant dashboard.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

files = list_files()
total_size = sum(f.stat().st_size for f in files) if files else 0

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="stat-box stat-purple"><div class="num">{len(files)}</div><div class="lbl">📦 Total Files</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="stat-box stat-blue"><div class="num">{human_size(total_size)}</div><div class="lbl">💾 Storage Used</div></div>', unsafe_allow_html=True)
with c3:
    last_mod = datetime.fromtimestamp(files[0].stat().st_mtime).strftime("%d %b, %I:%M %p") if files else "—"
    st.markdown(f'<div class="stat-box stat-green"><div class="num" style="font-size:1.15rem;">{last_mod}</div><div class="lbl">⚡ Last Activity</div></div>', unsafe_allow_html=True)

st.write("")
show_flash()

# --------------------------------------------------------------------------
# Browse
# --------------------------------------------------------------------------
if page == "📁 Browse":
    st.markdown('<div class="section-title">Your files</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Everything you\'ve created, newest first</div>', unsafe_allow_html=True)

    if not files:
        st.info("No files yet. Head to **➕ Create** to add your first file.")
    else:
        search = st.text_input("🔍 Search", placeholder="Type a filename...", label_visibility="collapsed")
        for f in files:
            if search and search.lower() not in f.name.lower():
                continue
            stats = f.stat()
            modified = datetime.fromtimestamp(stats.st_mtime).strftime("%d %b %Y, %I:%M %p")
            icon, color = icon_and_color(f)
            st.markdown(
                f"""
                <div class="file-card" style="--accent:{color};">
                    <span class="fname">{icon} {f.name}</span>
                    <span class="badge">{human_size(stats.st_size)}</span>
                    <div class="fmeta">Last modified: {modified}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# --------------------------------------------------------------------------
# Create
# --------------------------------------------------------------------------
elif page == "➕ Create":
    st.markdown('<div class="section-title">Create a new file</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Give it a name and some content to get started</div>', unsafe_allow_html=True)

    with st.form("create_form", clear_on_submit=True):
        filename = st.text_input("File name", placeholder="e.g. notes.txt")
        content = st.text_area("Content", height=220, placeholder="Write something...")
        submitted = st.form_submit_button("✨ Create file", use_container_width=True)

    if submitted:
        if not filename.strip():
            flash("error", "Please enter a file name.")
        else:
            path = safe_path(filename)
            if path.exists():
                flash("error", f"A file named '{path.name}' already exists.")
            else:
                try:
                    path.write_text(content, encoding="utf-8")
                    flash("success", f"File '{path.name}' created successfully.", celebrate="balloons")
                except Exception as err:
                    flash("error", f"Could not create file: {err}")
        st.rerun()

# --------------------------------------------------------------------------
# Read
# --------------------------------------------------------------------------
elif page == "📖 Read":
    st.markdown('<div class="section-title">Read a file</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Select a file to preview or download it</div>', unsafe_allow_html=True)

    if not files:
        st.info("No files available to read yet.")
    else:
        choice = st.selectbox("Select a file", [f.name for f in files])
        if choice:
            path = safe_path(choice)
            try:
                text = path.read_text(encoding="utf-8")
                st.text_area("Content", text, height=320, disabled=True)
                st.download_button("⬇️ Download", data=text, file_name=path.name, use_container_width=True)
            except Exception as err:
                st.error(f"Could not read file: {err}")

# --------------------------------------------------------------------------
# Update
# --------------------------------------------------------------------------
elif page == "✏️ Update":
    st.markdown('<div class="section-title">Update a file</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Rename it, append to it, or overwrite it completely</div>', unsafe_allow_html=True)

    if not files:
        st.info("No files available to update yet.")
    else:
        choice = st.selectbox("Select a file", [f.name for f in files])
        path = safe_path(choice)
        action = st.radio("What would you like to do?", ["Rename", "Append text", "Overwrite content"], horizontal=True)

        if action == "Rename":
            new_name = st.text_input("New file name")
            if st.button("Rename file", use_container_width=True):
                new_path = safe_path(new_name)
                if not new_name.strip():
                    flash("error", "Please enter a new name.")
                elif new_path.exists():
                    flash("error", f"A file named '{new_path.name}' already exists.")
                else:
                    path.rename(new_path)
                    flash("success", f"Renamed to '{new_path.name}'.")
                st.rerun()

        elif action == "Append text":
            extra = st.text_area("Text to append", height=150)
            if st.button("Append", use_container_width=True):
                try:
                    with open(path, "a", encoding="utf-8") as f:
                        f.write("\n" + extra)
                    flash("success", f"Appended text to '{path.name}'.")
                except Exception as err:
                    flash("error", f"Could not append: {err}")
                st.rerun()

        elif action == "Overwrite content":
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            new_content = st.text_area("New content", value=current, height=220)
            if st.button("Overwrite", use_container_width=True, type="primary"):
                try:
                    path.write_text(new_content, encoding="utf-8")
                    flash("success", f"Overwrote '{path.name}'.")
                except Exception as err:
                    flash("error", f"Could not overwrite: {err}")
                st.rerun()

# --------------------------------------------------------------------------
# Delete
# --------------------------------------------------------------------------
elif page == "🗑️ Delete":
    st.markdown('<div class="section-title">Delete a file</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">This action is permanent, so we ask you to confirm first</div>', unsafe_allow_html=True)

    if not files:
        st.info("No files available to delete.")
    else:
        choice = st.selectbox("Select a file to delete", [f.name for f in files])
        st.warning("This action cannot be undone.")
        confirm = st.checkbox(f"I confirm I want to permanently delete '{choice}'")
        if st.button("Delete file", type="primary", disabled=not confirm, use_container_width=True):
            try:
                safe_path(choice).unlink()
                flash("success", f"Deleted '{choice}'.", celebrate="snow")
            except Exception as err:
                flash("error", f"Could not delete: {err}")
            st.rerun()