# 🚀 Deploy Portfolio to Render (Step-by-Step)

## Why data is safe
- **PostgreSQL** on Render is a separate persistent service — it is NEVER deleted on redeploy
- **Images/files** are stored on Cloudinary (free) — also never deleted on redeploy
- SQLite is NOT used on Render (it resets on every deploy)

---

## STEP 1 — Get a free Cloudinary account (for images)
1. Go to https://cloudinary.com → Sign Up (free)
2. After login → Dashboard → copy the **"API Environment variable"**
   - Looks like: `cloudinary://123456:abcdef@mycloud`
3. Save it — you'll paste it into Render later

---

## STEP 2 — Push your code to GitHub
```bash
git init
git add .
git commit -m "Initial portfolio"
# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
git push -u origin main
```

---

## STEP 3 — Create a Render account
- Go to https://render.com → Sign up with GitHub

---

## STEP 4 — Deploy using render.yaml (Blueprint)
1. Render Dashboard → **New** → **Blueprint**
2. Connect your GitHub repo
3. Render reads `render.yaml` automatically and creates:
   - ✅ A **Web Service** (your Django app)
   - ✅ A **PostgreSQL database** (persistent, free)

---

## STEP 5 — Set Environment Variables in Render Dashboard
Go to your Web Service → **Environment** tab → Add these:

| Key | Value |
|-----|-------|
| `DJANGO_SUPERUSER_USERNAME` | `admin` |
| `DJANGO_SUPERUSER_EMAIL` | `your@email.com` |
| `DJANGO_SUPERUSER_PASSWORD` | `YourStrongPassword123!` |
| `CLOUDINARY_URL` | `cloudinary://xxx:yyy@zzz` (from Step 1) |
| `EMAIL_HOST_USER` | `your_gmail@gmail.com` |
| `EMAIL_HOST_PASSWORD` | Gmail App Password |
| `CONTACT_RECEIVER_EMAIL` | `your_gmail@gmail.com` |
| `RENDER_EXTERNAL_URL` | `https://your-app-name.onrender.com` |

---

## STEP 6 — Deploy
- Click **Manual Deploy** → **Deploy latest commit**
- Wait ~3 minutes for build to finish
- `build.sh` will automatically:
  - Install packages
  - Run migrations on PostgreSQL
  - Create your admin superuser

---

## STEP 7 — Access Admin Panel
```
https://your-app-name.onrender.com/admin/
Username: (what you set in DJANGO_SUPERUSER_USERNAME)
Password: (what you set in DJANGO_SUPERUSER_PASSWORD)
```

Add your profile, projects, skills etc. from admin — data stays **permanently** in PostgreSQL.

---

## STEP 8 — Update your CSRF origin
In `render.yaml`, change this line:
```yaml
value: https://YOUR-APP-NAME.onrender.com
```
to your actual Render URL, then push to GitHub and redeploy.

---

## ❓ FAQ

**Q: Will my data be deleted when I redeploy?**
A: No. PostgreSQL database and Cloudinary files are separate services — redeploy only updates your code.

**Q: Admin panel shows CSRF error?**
A: Make sure `RENDER_EXTERNAL_URL` env var is set to your exact Render URL.

**Q: Images not showing after deploy?**
A: Make sure `CLOUDINARY_URL` is set. Without it, images uploaded locally won't appear on Render.

**Q: How do I update my portfolio content?**
A: Go to `/admin/` → edit anything → it saves to PostgreSQL → shows on site immediately.
