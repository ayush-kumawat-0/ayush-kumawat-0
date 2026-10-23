# Ayush Kumawat — animated GitHub profile

## Files

- `README.md` — profile layout.
- `source-photo.png` — clean colour headshot source.
- `source-prepped.png` — grayscale, background-cleaned source used by the ASCII renderer.
- `ayush-ascii.svg` — animated terminal-style ASCII portrait.
- `stats.svg` — animated contribution/streak card.
- `contrib-heatmap.svg` — animated GitHub-style contribution calendar.
- `data/contributions.json` — current contribution snapshot.
- `scripts/` — generators used by the GitHub Action.
- `.github/workflows/update-profile-art.yml` — daily refresh.

## Local portrait rebuild

```bash
python -m pip install -r scripts/requirements.txt
python scripts/prep_photo.py
python scripts/make_ascii_svg.py
```

The source portrait is intentionally head-only. The bright background is converted
to blank space so the ASCII renderer does not reproduce the original photograph's
sky, buildings, road, or clothing.

## Contribution refresh

The GitHub Action fetches the public contribution calendar for:

`ayush-kumawat-0`

No GitHub token is required. The workflow regenerates `data/contributions.json`,
`contrib-heatmap.svg`, and `stats.svg`.

## GitHub profile repository

This repository is intended to be the special profile repository:

`ayush-kumawat-0/ayush-kumawat-0`
