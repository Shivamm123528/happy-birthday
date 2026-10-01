# For Chhaya 💗

A soft, personal birthday app built with Streamlit.

## Folder structure
```
app.py
gift_data.py        <- all the text lives here
requirements.txt
prototype.ipynb
assets/
  background.jpg    <- your uploaded photo (jpg/jpeg/png/webp)
  us1.jpg ... us6.jpg   (optional)
audio/
  birthday.mp3, funny.mp3, not_alone.mp3   (optional)
```
Missing photos or audio are simply hidden; nothing breaks.

## Before you deploy
1. The background photo is already included at `assets/background.jpeg`; to change it, replace that file. Keep it under ~2 MB so the app loads fast on phones.
2. Open `gift_data.py` and replace every `[placeholder]` and `MOM_PHONE`.
3. Optional: add `us1.jpg`–`us6.jpg` to `assets/` and record 3 voice notes into `audio/`.

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push this folder to a GitHub repo (use a private repo if you like; Streamlit can access it).
2. Go to share.streamlit.io and sign in with GitHub.
3. Click **Create app**, pick the repo and branch, set main file to `app.py`, then **Deploy**.
4. Share the link with her. On her phone, "Add to Home Screen" makes it one tap away.

## Opening flow
Blank password page (`gate.py`) -> beating heart that bursts into little hearts when touched -> the gift.
The password and hint are in `gift_data.py` (`PASSWORD`, `LOCK_HINT`). This is a sweet gate, not real security,
so keep the repo **private**.

## Push to GitHub
```
cd chhaya-gift
git init
git add .
git commit -m "Birthday gift for Chhaya"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
To update later: `git add .` then `git commit -m "update"` then `git push`. Streamlit Cloud redeploys by itself.
