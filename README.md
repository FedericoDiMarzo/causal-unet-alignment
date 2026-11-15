# Causal U-Net alignment

Interactive visualisation of a causal 1-D U-Net for time-domain speech enhancement:

- **Encoder**: `CausalConv1d` (stride `s`, kernel `K`), with a `lookahead` toggle.
- **Decoder**: `CausalConvTranspose1d` (stride `s`, kernel `k = K`, `s ≤ k ≤ 2s`), overlap tail cropped / carried as state.
- **Skip connections** between encoder and decoder rows of the same resolution.

Each input dot is one time step `t` (negative `t` = past context). Hover any sample to see
which input samples it reads through the bottleneck path (blue) and through the skip path (red),
and its lookahead in samples. Play / Step advance one input sample at a time.

The summary table reports, for `t ≥ 0`:

- the centre offset between skip and bottleneck input windows at each skip level
  (`lookahead=False` → shifted by `(K − s)` per layer, `(K − s)(sᴰ − 1)/(s − 1)` samples at the bottleneck);
- the output lookahead in samples, compared with the `0 … S−1` caused by block buffering alone (`S = sᴰ`).

## Run locally

Everything is in `index.html`; no build step and no dependencies.

```bash
# Node (>= 16)
npm start            # → http://localhost:8000

# or Python 3
python serve.py      # → http://localhost:8000 (opens the browser)

# or just open index.html in a browser
```

Fonts load from Google Fonts when online; offline it falls back to system fonts.

## Create a private GitHub repo

```bash
cd causal-unet-alignment
git init -b main
git add .
git commit -m "Causal U-Net alignment visualisation"

# with the GitHub CLI
gh repo create causal-unet-alignment --private --source=. --push

# or without it: create an empty private repo on github.com, then
git remote add origin git@github.com:<your-user>/causal-unet-alignment.git
git push -u origin main
```

## Layout

```
index.html   the visualisation (HTML + CSS + JS in one file)
server.js    zero-dependency Node static server (npm start)
serve.py     Python static server
package.json npm metadata, private, no dependencies
```
